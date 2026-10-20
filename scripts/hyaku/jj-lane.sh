#!/usr/bin/env bash
# jj-lane.sh — lane-repo VCS writes through Jujutsu (jj) in colocated mode.
#
# Replaces git commit/push for shokunin lane repos while keeping every
# git-based fleet tool working against the same repo (git log / merge-base /
# status / rev-list all see the jj-exported refs). Exit codes mirror
# scripts/hyaku/fleet-commit.sh:
#   0 ok / nothing to do · 1 failure ·
#   3 committed but push failed (commit kept) · 64 usage.
#
#   jj-lane.sh init   <lane-dir> <lane-id>
#   jj-lane.sh commit <lane-dir> --as <id> -m <message> -- <path>...
#   jj-lane.sh push   <lane-dir>
#   jj-lane.sh state  <lane-dir>
#
# Rules enforced here (lane contract):
#   * commits are pathspec-limited — never everything;
#   * author AND committer are "<id>-shokunin <<id>@shokunin.local>"
#     (per-command --config, so closures pass --as protocol);
#   * a cited hash must be the PUSHED hash; a pushed commit is never amended;
#   * push retries recover by fetch + rebase of ONLY the unpushed commits
#     (<branch>@origin..<branch>) onto the moved <branch>@origin — remote
#     commits are never rewritten and the push is never forced;
#   * every read-only jj call carries --ignore-working-copy.
set -u

JJ_BIN=${JJ_BIN:-}
if [ -z "$JJ_BIN" ]; then
  JJ_BIN=$(command -v jj 2>/dev/null || true)
  [ -n "$JJ_BIN" ] || JJ_BIN="$HOME/.local/bin/jj"
fi
[ -x "$JJ_BIN" ] || { echo "jj-lane: jj not found (set JJ_BIN)" >&2; exit 1; }

STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}

usage() {
  cat >&2 <<'EOF'
usage:
  jj-lane.sh init   <lane-dir> <lane-id>
  jj-lane.sh commit <lane-dir> --as <id> -m <message> -- <path>...
  jj-lane.sh push   <lane-dir>
  jj-lane.sh state  <lane-dir>
exit: 0 ok/nothing-to-do · 1 failure · 3 committed but push failed · 64 usage
EOF
  exit 64
}

err() { echo "jj-lane: $*" >&2; }

# Resolve the lane branch. Colocated repos leave git HEAD detached on the
# working-copy commit, so prefer origin/HEAD, then master/main, then the
# first local branch.
detect_branch() {
  local dir=$1 b ref
  b=$(git -C "$dir" symbolic-ref -q --short HEAD 2>/dev/null || true)
  if [ -n "$b" ]; then printf '%s\n' "$b"; return 0; fi
  ref=$(git -C "$dir" symbolic-ref -q refs/remotes/origin/HEAD 2>/dev/null || true)
  if [ -n "$ref" ]; then printf '%s\n' "${ref#refs/remotes/origin/}"; return 0; fi
  if   git -C "$dir" show-ref -q --verify refs/heads/master; then echo master
  elif git -C "$dir" show-ref -q --verify refs/heads/main;   then echo main
  else
    b=$(git -C "$dir" for-each-ref --format='%(refname:short)' refs/heads/ | head -1)
    [ -n "$b" ] && printf '%s\n' "$b" || return 1
  fi
}

# Pure-git, read-only state line (safe for `state`; no jj calls at all).
print_state() {
  local dir=$1 branch local_h remote_h ahead=0 behind=0 head status tracked untracked
  branch=$(detect_branch "$dir" 2>/dev/null) || branch="?"
  local_h=$(git -C "$dir" rev-parse --verify -q "refs/heads/$branch" 2>/dev/null || echo -)
  remote_h=$(git -C "$dir" rev-parse --verify -q "refs/remotes/origin/$branch" 2>/dev/null || echo -)
  if [ "$local_h" != - ] && [ "$remote_h" != - ]; then
    ahead=$(git -C "$dir" rev-list --count "refs/remotes/origin/$branch..refs/heads/$branch" 2>/dev/null || echo 0)
    behind=$(git -C "$dir" rev-list --count "refs/heads/$branch..refs/remotes/origin/$branch" 2>/dev/null || echo 0)
  fi
  if git -C "$dir" symbolic-ref -q HEAD >/dev/null 2>&1; then head=attached; else head=detached; fi
  status=$(git -C "$dir" status --porcelain 2>/dev/null)
  tracked=$(printf '%s\n' "$status" | grep -c '^[ MADRCU][MADRCU ]' 2>/dev/null || true)
  untracked=$(printf '%s\n' "$status" | grep -c '^??' 2>/dev/null || true)
  echo "state branch=$branch local=$local_h remote=$remote_h ahead=$ahead behind=$behind head=$head tracked=$tracked untracked=$untracked"
}

take_lock() {
  local dir=$1 base
  base=$(basename "$dir")
  mkdir -p "$STATE" || { err "cannot create $STATE"; exit 1; }
  exec {lk}>"$STATE/jj-$base.lock" || { err "cannot open lock $STATE/jj-$base.lock"; exit 1; }
  flock -w 300 "$lk" || { err "jj lane lock timeout (300s)"; exit 1; }
}

# jj revset helper: print commit/change ids, one per line, read-only.
jj_ids() { # <revset> <template>
  "$JJ_BIN" --ignore-working-copy log --no-graph -T "$2 ++ \"\\n\"" -r "$1" 2>/dev/null
}

# Push $BRANCH to origin, recovering from a moved remote by fetch + rebase of
# only the unpushed commits. Prints "pushed <hash>" or "nothing to push".
# Returns 0 on success/already-synced, 1 on failure. Caller's cwd = lane dir.
do_push() {
  local attempt
  for attempt in 1 2 3; do
    # Never push a commit with a conflicted tree: jj exports conflicts as
    # .jjconflict-* artifacts and would spray them across the remote tree.
    if [ -n "$(jj_ids "heads(bookmarks(${BRANCH})) & conflicts()" commit_id)" ]; then
      err "local $BRANCH tip has unresolved conflicts — resolve in the lane, then retry"
      return 1
    fi
    if "$JJ_BIN" git push --remote origin --bookmark "$BRANCH" 2>"$STATE/jj-push.err"; then
      # Remote-tip hash after the push = the hash a report may cite.
      echo "pushed $(jj_ids "heads(${BRANCH}@origin)" commit_id | head -1)"
      return 0
    fi
    # Rejected: fetch the real remote state, then rebase ONLY the commits the
    # local bookmark has beyond <branch>@origin onto the new remote tip. The
    # per-command --ignore-immutable lifts the lane's ::bookmarks() alias for
    # this rebase only; commits already on the remote are never rewritten.
    "$JJ_BIN" git fetch --remote origin >/dev/null 2>&1 || { sleep "$attempt"; continue; }
    tip=$(jj_ids "heads(${BRANCH}@origin..bookmarks(${BRANCH}))" change_id | head -1)
    if [ -n "$tip" ]; then
      "$JJ_BIN" --ignore-immutable rebase -b "$tip" -d "${BRANCH}@origin" >/dev/null 2>&1 || continue
      "$JJ_BIN" --ignore-working-copy bookmark set "$BRANCH" -r "$tip" >/dev/null 2>&1 || continue
    else
      # Local bookmark had nothing beyond the remote (behind-only or absent):
      # point it at the remote tip so the next attempt is a no-op push.
      "$JJ_BIN" --ignore-working-copy bookmark set "$BRANCH" -r "${BRANCH}@origin" >/dev/null 2>&1 || continue
    fi
    sleep "$attempt"
  done
  err "push failed after 3 attempts: $(head -3 "$STATE/jj-push.err" 2>/dev/null | tr '\n' ' ')"
  return 1
}

cmd_init() {
  [ $# -eq 2 ] || usage
  local dir=$1 id=$2 branch
  [ -d "$dir/.git" ] || { err "not a git repo: $dir"; exit 1; }
  case $id in ''|*[!a-z0-9-]*) echo "bad lane id: $id" >&2; exit 64 ;; esac
  take_lock "$dir"
  cd "$dir" || exit 1
  branch=$(detect_branch .) || { err "cannot determine lane branch"; exit 1; }
  if [ ! -d .jj ]; then
    # Colocate with auto-track disabled from the very first snapshot so seat
    # scratch and oversized untracked files never enter jj.
    "$JJ_BIN" --config 'snapshot.auto-track="none()"' git init --colocate . \
      || { err "jj git init --colocate failed"; exit 1; }
  fi
  # --ignore-working-copy on every config call: `jj config set` otherwise
  # snapshots the working copy BEFORE auto-track="none()" is in the repo config,
  # and that default all() snapshot tracks every untracked file (seat scratch,
  # operator sweep dirs), which git then shows as intent-to-add (" A") entries.
  "$JJ_BIN" --ignore-working-copy config set --repo snapshot.auto-track '"none()"' || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo user.name  "${id}-shokunin"       || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo user.email "${id}@shokunin.local" || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo 'revset-aliases."trunk()"' "\"${branch}@origin\"" || exit 1
  # A pre-existing .jj (tameshi, mado) may already track scratch in @ from an
  # earlier default-auto-track snapshot: report it; untracking is a lane decision.
  local added
  added=$("$JJ_BIN" --ignore-working-copy diff --summary -r @ 2>/dev/null | grep -c '^A ' || true)
  [ "${added:-0}" -gt 0 ] && echo "warn: working-copy commit @ already tracks $added added path(s); inspect: jj --ignore-working-copy diff --summary -r @" >&2
  # Existing repo config (e.g. a custom immutable_heads() alias) is left
  # intact — config set only touches the keys above.
  "$JJ_BIN" --ignore-working-copy bookmark track "${branch}@origin" >/dev/null 2>&1 || true
  print_state .
}

cmd_commit() {
  [ $# -ge 1 ] || usage
  local dir=$1 id='' msg='' branch hash p; shift
  while [ $# -gt 0 ]; do
    case $1 in
      --as) id=${2:-}; shift 2 || usage ;;
      -m)   msg=${2:-}; shift 2 || usage ;;
      --)   shift; break ;;
      *)    usage ;;
    esac
  done
  [ -n "$id" ] && [ -n "$msg" ] && [ $# -gt 0 ] || usage
  case $id in *[!a-z0-9-]*) echo "bad lane id: $id" >&2; exit 64 ;; esac
  for p in "$@"; do
    case $p in /*|*..*|.) echo "path must be repo-relative without '..': $p" >&2; exit 64 ;; esac
    case $p in .ufo/state/*|.ufo/watchdog.log)
      echo "driver runtime is never committed by a lane: $p" >&2; exit 64 ;; esac
    case $p in *[*?[]*) echo "glob characters are not allowed in paths: $p" >&2; exit 64 ;; esac
  done
  [ -d "$dir/.jj" ] || { err "not jj-colocated (run: jj-lane.sh init $dir $id): $dir"; exit 1; }
  take_lock "$dir"
  cd "$dir" || exit 1
  branch=$(detect_branch .) || { err "cannot determine lane branch"; exit 1; }

  local existing=()
  for p in "$@"; do
    if [ -e "$p" ] || git ls-files --error-unmatch -- "$p" >/dev/null 2>&1; then
      existing+=("$p")
    else
      echo "warn: skipping missing path $p" >&2
    fi
  done
  [ ${#existing[@]} -gt 0 ] || { echo "nothing to commit (no such paths)"; exit 0; }

  # Track listed-but-untracked paths explicitly. --include-ignored (which also
  # admits files over snapshot.max-new-file-size, jj's default 1 MiB) applies
  # only to paths named as FILES; a named directory is tracked like `git add
  # <dir>`, so its ignored content (caches, seat scratch) never enters a commit.
  local files=() dirs=()
  for p in "${existing[@]}"; do
    if [ -d "$p" ]; then dirs+=("$p"); else files+=("$p"); fi
  done
  if [ ${#files[@]} -gt 0 ]; then
    "$JJ_BIN" file track --include-ignored -- "${files[@]}" >/dev/null 2>&1 || {
      err "jj file track failed"; exit 1; }
  fi
  if [ ${#dirs[@]} -gt 0 ]; then
    "$JJ_BIN" file track -- "${dirs[@]}" >/dev/null 2>&1 || {
      err "jj file track failed"; exit 1; }
  fi

  if [ -z "$("$JJ_BIN" diff --summary -- "${existing[@]}" 2>/dev/null)" ]; then
    echo "nothing to commit"
  else
    # Stamp the working-copy author first: `jj commit <paths>` splits @ and
    # keeps @'s existing author, so a plain --config would only fix the
    # committer. metaedit --update-author under the same per-command identity
    # makes author and committer both "<id>-shokunin <<id>@shokunin.local>".
    "$JJ_BIN" --config "user.name=${id}-shokunin" \
              --config "user.email=${id}@shokunin.local" \
              metaedit --update-author >/dev/null 2>&1 || { err "metaedit failed"; exit 1; }
    "$JJ_BIN" --config "user.name=${id}-shokunin" \
              --config "user.email=${id}@shokunin.local" \
              commit -m "$msg" -- "${existing[@]}" || { err "jj commit failed"; exit 1; }
    hash=$(jj_ids '@-' commit_id | head -1)
    [ -n "$hash" ] || { err "cannot read committed hash"; exit 1; }
    "$JJ_BIN" --ignore-working-copy bookmark set "$branch" -r "$hash" >/dev/null 2>&1 \
      || { err "bookmark set failed"; exit 1; }
    echo "committed $hash"
  fi

  BRANCH=$branch
  do_push || exit 3
  exit 0
}

cmd_push() {
  [ $# -eq 1 ] || usage
  local dir=$1 branch
  [ -d "$dir/.jj" ] || { err "not jj-colocated: $dir"; exit 1; }
  take_lock "$dir"
  cd "$dir" || exit 1
  branch=$(detect_branch .) || { err "cannot determine lane branch"; exit 1; }
  BRANCH=$branch
  do_push || exit 3
  exit 0
}

cmd_state() {
  [ $# -eq 1 ] || usage
  local dir=$1
  [ -d "$dir/.git" ] || { err "not a git repo: $dir"; exit 1; }
  print_state "$dir"
}

case ${1:-} in
  init)   shift; cmd_init "$@" ;;
  commit) shift; cmd_commit "$@" ;;
  push)   shift; cmd_push "$@" ;;
  state)  shift; cmd_state "$@" ;;
  *)      usage ;;
esac
