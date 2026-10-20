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
#   jj-lane.sh commit <lane-dir> --as <id> -m <message> [--allow-large] -- <path>...
#   jj-lane.sh push   [--no-rebase] <lane-dir>
#   jj-lane.sh state  <lane-dir>
#
# Rules enforced here (lane contract):
#   * commits are pathspec-limited — never everything;
#   * author AND committer are "<id>-shokunin <<id>@shokunin.local>"
#     (per-command --config, so closures pass --as protocol; the push-recovery
#     rebase carries the same identity);
#   * a cited hash must be the LANDED hash — the only citable output line is
#     `landed <hash>`, printed after `git ls-remote` verifies the remote tip;
#   * pushes are fast-forward only: nothing is ever rewritten, the remote is
#     never moved backwards or sideways, and a remote that stopped being a
#     descendant of the last-seen remote tip stops the helper (exit 3);
#   * push retries recover by fetch + rebase of ONLY the unpushed commits
#     (<branch>@origin..<branch>) onto the moved <branch>@origin;
#   * `.ufo`, `.ufo/state`, `.git` and `.jj` are never committable;
#   * every snapshotting jj call carries --config 'snapshot.auto-track="none()"';
#   * every read-only jj call carries --ignore-working-copy.
set -u

unset JJ_USER JJ_EMAIL

JJ_BIN=${JJ_BIN:-}
if [ -z "$JJ_BIN" ]; then
  JJ_BIN=$(command -v jj 2>/dev/null || true)
  [ -n "$JJ_BIN" ] || JJ_BIN="$HOME/.local/bin/jj"
fi
[ -x "$JJ_BIN" ] || { echo "jj-lane: jj not found (set JJ_BIN)" >&2; exit 1; }

STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}

# The fleet root is never a lane. The literal path is the deployment anchor;
# the derived path covers helpers invoked from a copy elsewhere in the tree.
FLEET_ROOT_REAL=/home/vgpnk/Projects/shokunin
SELF_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
FLEET_ROOT_DERIVED=$(cd "$SELF_DIR/../.." 2>/dev/null && pwd -P || echo "")

usage() {
  cat >&2 <<'EOF'
usage:
  jj-lane.sh init   <lane-dir> <lane-id>
  jj-lane.sh commit <lane-dir> --as <id> -m <message> [--allow-large] -- <path>...
  jj-lane.sh push   [--no-rebase] <lane-dir>
  jj-lane.sh state  <lane-dir>
exit: 0 ok/nothing-to-do · 1 failure · 3 committed but push failed · 64 usage
output: `landed <hash>` is the only citable line; `rewritten <old> -> <new>`
        precedes it when push recovery rewrote this run's commit;
        `nothing to commit` prints no hash.
EOF
  exit 64
}

err() { echo "jj-lane: $*" >&2; }

# Per-command snapshot config for every call that can write the working copy.
AUTOTRACK_OFF='snapshot.auto-track="none()"'

# ---- lane guards -----------------------------------------------------------

# Refuse the fleet root and anything that is not a real clone (worktrees and
# submodules have .git as a FILE). Prints the lane's physical path on stdout.
lane_realdir() { # <dir>
  local dir=$1 phys
  [ -d "$dir/.git" ] || { err "not a real clone (missing .git directory): $dir"; return 1; }
  phys=$(cd "$dir" 2>/dev/null && pwd -P) || { err "cannot enter $dir"; return 1; }
  if [ "$phys" = "$FLEET_ROOT_REAL" ] || { [ -n "$FLEET_ROOT_DERIVED" ] && [ "$phys" = "$FLEET_ROOT_DERIVED" ]; }; then
    err "the fleet root is not a lane: $phys"
    return 1
  fi
  printf '%s\n' "$phys"
}

valid_branch() { [[ $1 =~ ^[a-zA-Z0-9][a-zA-Z0-9._/-]*$ ]] && [[ $1 != jj/* && $1 != *..* ]] ; }

# Branch recorded at init. Mutating subcommands read the repo `trunk()` alias
# (init writes `"<branch>@origin"`); `state` stays pure git and reads the
# lane.branch mirror init also writes. Missing alias = "run init".
lane_branch_jj() { # cwd = lane
  local t
  t=$("$JJ_BIN" --ignore-working-copy config get 'revset-aliases."trunk()"' 2>/dev/null || true)
  t=${t%@origin}
  if valid_branch "$t"; then printf '%s\n' "$t"; return 0; fi
  return 1
}

lane_branch_git() { # <dir>
  local b
  b=$(git -C "$1" config --get lane.branch 2>/dev/null || true)
  if valid_branch "$b"; then printf '%s\n' "$b"; return 0; fi
  return 1
}

# Lane id from the jj repo identity init wrote (user.name = "<id>-shokunin").
lane_id_jj() { # cwd = lane
  local n
  n=$("$JJ_BIN" --ignore-working-copy config get user.name 2>/dev/null || true)
  case $n in *-shokunin) printf '%s\n' "${n%-shokunin}"; return 0 ;; esac
  return 1
}

# Branch detection used ONLY by init for a first recording. Prefer an attached
# HEAD's branch (never anything under refs/jj/), else origin/HEAD.
detect_branch() { # <dir>
  local dir=$1 b ref
  b=$(git -C "$dir" symbolic-ref -q HEAD 2>/dev/null || true)
  case $b in
    refs/heads/*) b=${b#refs/heads/}; valid_branch "$b" && { printf '%s\n' "$b"; return 0; } ;;
  esac
  ref=$(git -C "$dir" symbolic-ref -q refs/remotes/origin/HEAD 2>/dev/null || true)
  case $ref in
    refs/remotes/origin/*) b=${ref#refs/remotes/origin/}; valid_branch "$b" && { printf '%s\n' "$b"; return 0; } ;;
  esac
  return 1
}

# ---- lock ------------------------------------------------------------------

# Lock and error files keyed on the lane's physical path, not its basename:
# `commit .` and `commit /abs/lane` contend on one lock.
take_lock() { # <phys-dir>
  local key
  key=$(printf '%s' "$1" | tr '/.' '__' | tr -cd '[:alnum:]_-')
  mkdir -p "$STATE" || { err "cannot create $STATE"; exit 1; }
  LOCKBASE="$STATE/jj-$key"
  exec {lk}>"$LOCKBASE.lock" || { err "cannot open lock $LOCKBASE.lock"; exit 1; }
  flock -w 300 "$lk" || { err "jj lane lock timeout (300s)"; exit 1; }
}

# ---- jj helpers ------------------------------------------------------------

# jj revset helper: print one field per line, read-only.
jj_ids() { # <revset> <template>
  "$JJ_BIN" --ignore-working-copy log --no-graph -T "$2 ++ \"\\n\"" -r "$1" 2>/dev/null
}

# Escape a repo-relative path for a jj fileset string literal.
fileset_escape() { # <path>
  printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' -e 's/	/\\t/g' -e ':a;N;$!ba;s/\n/\\n/g'
}

# ---- state (pure git, read-only; no jj calls) -------------------------------

cmd_state() {
  [ $# -eq 1 ] || usage
  local dir branch local_h remote_h ahead behind head status tracked untracked
  dir=$(lane_realdir "$1") || exit 1
  # The driver reads `state` for every lane, including git-only lanes and lanes
  # colocated before lane.branch existed: fall back to pure-git detection, then
  # to the single existing master/main branch.
  branch=$(lane_branch_git "$dir") || branch=$(detect_branch "$dir") || {
    local c=()
    git -C "$dir" show-ref -q --verify refs/heads/master && c+=(master)
    git -C "$dir" show-ref -q --verify refs/heads/main && c+=(main)
    [ ${#c[@]} -eq 1 ] && branch=${c[0]}
  }
  [ -n "${branch:-}" ] || { err "no lane branch recorded (run: jj-lane.sh init)"; exit 1; }
  local_h=$(git -C "$dir" rev-parse --verify -q "refs/heads/$branch" 2>/dev/null || true)
  remote_h=$(git -C "$dir" rev-parse --verify -q "refs/remotes/origin/$branch" 2>/dev/null || true)
  [[ $local_h =~ ^[0-9a-f]{40}$ ]] || { err "refs/heads/$branch is not a 40-hex hash"; exit 1; }
  [[ $remote_h =~ ^[0-9a-f]{40}$ ]] || { err "refs/remotes/origin/$branch is not a 40-hex hash"; exit 1; }
  ahead=$(git -C "$dir" rev-list --count "refs/remotes/origin/$branch..refs/heads/$branch" 2>/dev/null || echo 0)
  behind=$(git -C "$dir" rev-list --count "refs/heads/$branch..refs/remotes/origin/$branch" 2>/dev/null || echo 0)
  if git -C "$dir" symbolic-ref -q HEAD >/dev/null 2>&1; then head=attached; else head=detached; fi
  status=$(git -C "$dir" status --porcelain 2>/dev/null)
  tracked=$(printf '%s\n' "$status" | grep -c '^[ MADRCU][MADRCU ]' 2>/dev/null || true)
  untracked=$(printf '%s\n' "$status" | grep -c '^??' 2>/dev/null || true)
  echo "state branch=$branch local=$local_h remote=$remote_h ahead=$ahead behind=$behind head=$head tracked=$tracked untracked=$untracked"
}

# ---- push ------------------------------------------------------------------

# A push rejection is recoverable only when it is a stale lease / moved remote;
# hook, permission, tracking, conflict and content rejections are fatal.
classify_push_error() { # <errfile> -> lease|fatal
  local t
  t=$(cat "$1" 2>/dev/null)
  case $t in
    *"unexpectedly moved on the remote"*|*"stale info"*|*"stale-info"*) echo lease ;;
    *) echo fatal ;;
  esac
}

# Static gates that must hold before ANY push attempt. Returns 0 or 1.
push_preflight() { # <branch>
  local b=$1 lane_id an ae cn ce
  lane_id=$(lane_id_jj) || { err "no lane identity recorded (run: jj-lane.sh init)"; return 1; }
  # Conflicted bookmark or conflicted tip: refuse outright.
  if "$JJ_BIN" --ignore-working-copy bookmark list --conflicted 2>/dev/null | awk -v n="$b" '$1==n{f=1} END{exit !f}'; then
    err "bookmark $b is conflicted — resolve it in the lane, then retry"
    return 1
  fi
  if [ -n "$(jj_ids "heads(bookmarks(${b})) & conflicts()" commit_id)" ]; then
    err "local $b tip has unresolved conflicts — resolve in the lane, then retry"
    return 1
  fi
  git show-ref -q --verify "refs/remotes/origin/$b" || {
    err "remote branch origin/$b not found locally (fetch first)"; return 1; }
  # Fast-forward only: the remote tip must be an ancestor of the local tip.
  git merge-base --is-ancestor "refs/remotes/origin/$b" "refs/heads/$b" 2>/dev/null || {
    err "local $b is not a descendant of origin/$b — refusing a backwards/sideways push"
    return 1
  }
  # Every commit in the push range carries the lane or the protocol identity on
  # BOTH author and committer — a stray seat commit or a raw `git commit` under
  # the operator or ci identity never ships.
  while IFS='|' read -r an ae cn ce; do
    [ -n "$an" ] || continue
    case $an in "${lane_id}-shokunin"|protocol-shokunin) ;; *)
      err "push range contains a foreign author: $an <$ae>"; return 1 ;; esac
    case $ae in "${lane_id}@shokunin.local"|protocol@shokunin.local) ;; *)
      err "push range contains a foreign author email: $an <$ae>"; return 1 ;; esac
    case $cn in "${lane_id}-shokunin"|protocol-shokunin) ;; *)
      err "push range contains a foreign committer: $cn <$ce>"; return 1 ;; esac
    case $ce in "${lane_id}@shokunin.local"|protocol@shokunin.local) ;; *)
      err "push range contains a foreign committer email: $cn <$ce>"; return 1 ;; esac
  done < <(git log --format='%an|%ae|%cn|%ce' "refs/remotes/origin/$b..refs/heads/$b" 2>/dev/null)
  return 0
}

# Verify the push landed: remote tip == local tip and this run's commit (when
# given) is its ancestor. Prints `rewritten`/`landed` lines.
report_landed() { # <branch> <own-hash-or-empty>
  local b=$1 own=$2 local_tip remote_tip cid new
  local_tip=$(git rev-parse "refs/heads/$b" 2>/dev/null || true)
  remote_tip=$(git ls-remote origin "refs/heads/$b" 2>/dev/null | head -1 | awk '{print $1}')
  if [ -z "$remote_tip" ]; then
    err "ls-remote: remote branch $b missing after push"
    return 1
  fi
  if [ "$remote_tip" != "$local_tip" ]; then
    err "ls-remote: remote tip $remote_tip != local tip ${local_tip:-none} — remote diverged from this push"
    return 1
  fi
  if [ -n "$own" ] && ! git merge-base --is-ancestor "$own" "$remote_tip" 2>/dev/null; then
    # The recovery rebase rewrote it; find the descendant with its change id.
    cid=$(jj_ids "$own" change_id | head -1)
    new=$(jj_ids "heads(::bookmarks(${b}) & change_id(${cid}))" commit_id | head -1)
    if [ -n "$new" ]; then
      echo "rewritten $own -> $new"
      echo "landed $remote_tip"
      return 0
    fi
    err "this run's commit $own is not an ancestor of the remote tip"
    return 1
  fi
  echo "landed $remote_tip"
  return 0
}

# Re-anchor an EMPTY working copy that is not a child of the branch tip (the
# recovery rebase can leave @ on the pre-rebase parent). A non-empty @ is left
# alone: `jj new` would rewrite its tracked files on disk.
reanchor_wc() { # <branch> <id>
  local b=$1 id=$2 tip base
  tip=$(jj_ids "heads(bookmarks(${b}))" commit_id | head -1)
  [ -n "$tip" ] || return 0
  base=$(jj_ids '@-' commit_id | head -1)
  [ "$base" = "$tip" ] && return 0
  [ -n "$(jj_ids '@' 'if(empty,"x")')" ] || return 0
  "$JJ_BIN" --config "$AUTOTRACK_OFF" \
    --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
    new "$tip" >/dev/null 2>&1 || true
}

# One recovery step after a lease-style rejection: fetch, refuse a rewritten
# remote, rebase only <b>@origin..<b> under the requested identity, re-anchor
# the working copy, and let the caller retry the push. Returns 0 to retry.
recover_remote_move() { # <branch> <id>
  local b=$1 id=$2 old_remote_tip new_remote_tip tips count tip
  old_remote_tip=$(git rev-parse "refs/remotes/origin/$b" 2>/dev/null || true)
  "$JJ_BIN" --ignore-working-copy git fetch --remote origin 2>"$LOCKBASE.err" || {
    err "jj git fetch failed: $(head -3 "$LOCKBASE.err" 2>/dev/null | tr '\n' ' ')"; return 1; }
  new_remote_tip=$(git rev-parse "refs/remotes/origin/$b" 2>/dev/null || true)
  [ -n "$new_remote_tip" ] || { err "remote branch $b disappeared after fetch"; return 1; }
  # The remote never moves backwards or sideways: the tip we last saw must
  # still be an ancestor. A rewritten remote stops the helper.
  if [ -n "$old_remote_tip" ] && ! git merge-base --is-ancestor "$old_remote_tip" "$new_remote_tip" 2>/dev/null; then
    err "origin/$b was rewritten ($old_remote_tip -> $new_remote_tip) — refusing to rebase onto rewritten history"
    return 1
  fi
  # A fetch that found the bookmark on both a local tip and the moved remote
  # leaves it CONFLICTED (concurrent lane pushes). Resolve by choosing the
  # local side before computing the rebase range — there is nothing to choose
  # when the local side matches the remote (count 0 below).
  if "$JJ_BIN" --ignore-working-copy bookmark list --conflicted 2>/dev/null | awk -v n="$b" '$1==n{f=1} END{exit !f}'; then
    tips=$(jj_ids "heads(bookmarks(${b}) & ~::${b}@origin)" change_id)
    count=$(printf '%s\n' "$tips" | grep -c . || true)
    [ "$count" -eq 1 ] || { err "conflicted bookmark $b has $count unpushed tips — refusing"; return 1; }
    tip=$tips
    "$JJ_BIN" --config "$AUTOTRACK_OFF" \
      --config 'revset-aliases."immutable_heads()"="builtin_immutable_heads() | remote_bookmarks()"' \
      --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
      rebase -b "$tip" -d "${b}@origin" 2>"$LOCKBASE.err" || {
        err "recovery rebase failed: $(head -3 "$LOCKBASE.err" 2>/dev/null | tr '\n' ' ')"; return 1; }
    "$JJ_BIN" --ignore-working-copy bookmark set "$b" -r "$tip" >/dev/null 2>&1 || {
      err "bookmark set after rebase failed"; return 1; }
    if [ -n "$(jj_ids "heads(bookmarks(${b})) & conflicts()" commit_id)" ]; then
      err "recovery rebase produced conflicts — resolve in the lane, then retry"
      return 1
    fi
    reanchor_wc "$b" "$id"
    return 0
  fi
  tips=$(jj_ids "heads(${b}@origin..bookmarks(${b}))" change_id)
  count=$(printf '%s\n' "$tips" | grep -c . || true)
  if [ "$count" -gt 0 ]; then
    [ "$count" -eq 1 ] || { err "unpushed range has $count tips (divergent) — refusing"; return 1; }
    tip=$tips
    # Per-command alias narrows immutability to pushed history for this rebase
    # only; --ignore-immutable is never used. The requested identity stays the
    # committer through the rewrite.
    "$JJ_BIN" --config "$AUTOTRACK_OFF" \
      --config 'revset-aliases."immutable_heads()"="builtin_immutable_heads() | remote_bookmarks()"' \
      --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
      rebase -b "$tip" -d "${b}@origin" 2>"$LOCKBASE.err" || {
        err "recovery rebase failed: $(head -3 "$LOCKBASE.err" 2>/dev/null | tr '\n' ' ')"; return 1; }
    "$JJ_BIN" --ignore-working-copy bookmark set "$b" -r "$tip" >/dev/null 2>&1 || {
      err "bookmark set after rebase failed"; return 1; }
    if [ -n "$(jj_ids "heads(bookmarks(${b})) & conflicts()" commit_id)" ]; then
      err "recovery rebase produced conflicts — resolve in the lane, then retry"
      return 1
    fi
  else
    # Nothing local beyond the remote: adopt the remote tip.
    "$JJ_BIN" --ignore-working-copy bookmark set "$b" -r "${b}@origin" >/dev/null 2>&1 || {
      err "bookmark set to ${b}@origin failed"; return 1; }
  fi
  reanchor_wc "$b" "$id"
  return 0
}

# Push <branch> to origin with fetch+rebase recovery on lease rejections only.
# Prints exactly one `landed <hash>` on success. Returns 0/1.
do_push() { # <branch> <id> <own-hash-or-empty>
  local b=$1 id=$2 own=${3:-}
  push_preflight "$b" || return 1
  for _ in 1 2 3; do
    if "$JJ_BIN" --config "$AUTOTRACK_OFF" git push --remote origin --bookmark "$b" 2>"$LOCKBASE.err"; then
      report_landed "$b" "$own" && return 0
      return 1
    fi
    if [ "$(classify_push_error "$LOCKBASE.err")" = lease ]; then
      recover_remote_move "$b" "$id" || return 1
      push_preflight "$b" || return 1
      continue
    fi
    err "push rejected (not a stale lease; no retry): $(head -3 "$LOCKBASE.err" 2>/dev/null | tr '\n' ' ')"
    return 1
  done
  err "push failed after 3 attempts: $(head -3 "$LOCKBASE.err" 2>/dev/null | tr '\n' ' ')"
  return 1
}

# ---- init ------------------------------------------------------------------

cmd_init() {
  [ $# -eq 2 ] || usage
  local dir=$1 id=$2 branch phys status_before status_after
  local local_head local_tip remote_tip adds f
  case $id in ''|*[!a-z0-9-]*) err "bad lane id: $id"; exit 64 ;; esac
  phys=$(lane_realdir "$dir") || exit 1
  take_lock "$phys"
  cd "$phys" || exit 1
  status_before=$(git status --porcelain --untracked-files=no 2>/dev/null)

  if [ -d .jj ]; then
    # CRITICAL: import git HEAD with a snapshotting call BEFORE any other jj
    # call. A .jj whose last op predates newer plain-git commits would
    # otherwise reset the git index to its stale @- tree the first time a
    # transaction commits (observed: ~238 staged `D` entries on tameshi).
    "$JJ_BIN" --config "$AUTOTRACK_OFF" status >/dev/null 2>&1 || {
      err "jj status failed on existing .jj"; exit 1; }
    # Existing jj repo: reuse the recorded branch (init is idempotent and must
    # not flip a lane); detect only when nothing was recorded yet.
    branch=$(lane_branch_jj) || branch=$(lane_branch_git .) || branch=$(detect_branch .) || {
      err "cannot determine lane branch"; exit 1; }
  else
    # First colocation: only on a quiesced, non-diverged branch.
    branch=$(lane_branch_git .) || branch=$(detect_branch .) || {
      err "cannot determine lane branch"; exit 1; }
    local_head=$(git symbolic-ref -q HEAD 2>/dev/null || true)
    local_tip=$(git rev-parse -q --verify "refs/heads/$branch" 2>/dev/null || true)
    remote_tip=$(git rev-parse -q --verify "refs/remotes/origin/$branch" 2>/dev/null || true)
    [ -n "$local_tip" ]  || { err "branch refs/heads/$branch does not exist"; exit 1; }
    [ -n "$remote_tip" ] || { err "branch refs/remotes/origin/$branch does not exist (fetch first)"; exit 1; }
    if [ "$(git rev-list --count "refs/heads/$branch..refs/remotes/origin/$branch" 2>/dev/null)" != 0 ] \
       && [ "$(git rev-list --count "refs/remotes/origin/$branch..refs/heads/$branch" 2>/dev/null)" != 0 ]; then
      err "$branch has diverged from origin/$branch: rebase it first (jj would push it sideways)"
      exit 1
    fi
    if [ -z "$local_head" ] && [ "$(git rev-parse -q HEAD 2>/dev/null)" != "$local_tip" ]; then
      err "HEAD is detached on a non-tip commit — check out $branch first"
      exit 1
    fi
    if [ -e .git/MERGE_HEAD ] || [ -e .git/CHERRY_PICK_HEAD ] || [ -e .git/REVERT_HEAD ] \
       || [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
      err "a merge/cherry-pick/revert/rebase is in progress — finish it before colocating"
      exit 1
    fi
    if [ -n "$(git ls-files -u 2>/dev/null)" ]; then
      err "the index has unmerged entries — finish the merge before colocating"
      exit 1
    fi
    if ! git diff --cached --quiet 2>/dev/null; then
      err "the index has staged entries — jj init would silently unstage them; commit or reset first"
      exit 1
    fi
    "$JJ_BIN" --config "$AUTOTRACK_OFF" git init --colocate . \
      || { err "jj git init --colocate failed"; exit 1; }
  fi

  # Repo config. --ignore-working-copy: no snapshot until auto-track=none() is
  # persisted (a default all() snapshot would track every untracked file).
  "$JJ_BIN" --ignore-working-copy config set --repo snapshot.auto-track '"none()"' || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo user.name  "${id}-shokunin"       || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo user.email "${id}@shokunin.local" || exit 1
  "$JJ_BIN" --ignore-working-copy config set --repo 'revset-aliases."trunk()"' "\"${branch}@origin\"" || exit 1
  # immutable_heads() only when absent — a lane's existing alias (e.g.
  # ::bookmarks()) is left untouched.
  if ! "$JJ_BIN" --ignore-working-copy config list --repo 2>/dev/null | grep -q 'immutable_heads()'; then
    "$JJ_BIN" --ignore-working-copy config set --repo 'revset-aliases."immutable_heads()"' \
      '"builtin_immutable_heads() | remote_bookmarks()"' || exit 1
  fi
  # Record the branch (and lane id) in git config: `state` stays pure git and
  # every subcommand reads the binding instead of re-detecting after HEAD
  # detaches.
  git config lane.branch "$branch" || exit 1
  git config lane.id "$id" || exit 1

  # Track the remote bookmark; fail unless it is (already) tracked.
  if ! "$JJ_BIN" --ignore-working-copy bookmark track "${branch}@origin" >/dev/null 2>&1 \
     && [ -z "$(jj_ids "remote_bookmarks(exact:\"${branch}\", remote=origin)" commit_id)" ]; then
    err "cannot track ${branch}@origin"; exit 1
  fi

  # Untrack whatever @ adds over @- that git does not track (pre-helper
  # all()-snapshot scratch, e.g. a kaika-pilot SKILL.snapshot.md). Untracking
  # never deletes the file.
  adds=0
  local -a untracked=()
  while IFS= read -r f; do
    # "git tracks it" = present in the branch tip commit. The index cannot be
    # the oracle: the jj snapshot may stage additions that HEAD lacks.
    if ! git cat-file -e "refs/heads/$branch:$f" 2>/dev/null; then
      adds=$((adds + 1))
      if "$JJ_BIN" --config "$AUTOTRACK_OFF" file untrack -- "root-file:\"$(fileset_escape "$f")\"" >/dev/null 2>&1; then
        untracked+=("$f")
        echo "untracked (kept on disk): $f"
      else
        echo "warn: could not untrack $f" >&2
      fi
    fi
  done < <("$JJ_BIN" --config "$AUTOTRACK_OFF" diff --summary -r @ 2>/dev/null | sed -n 's/^A //p')

  # The git index/status must be untouched by init — a stale .jj once reset it
  # to an old @- tree. Assert byte-identical tracked status, ignoring the paths
  # init deliberately untracked above (their staged entry is the repair).
  strip_untracked() { # stdin: porcelain v1 -> same minus the untracked paths
    local line p u
    while IFS= read -r line; do
      p=${line:3}
      for u in ${untracked[@]+"${untracked[@]}"}; do
        if [ "$p" = "$u" ] || [ "$p" = "\"$u\"" ]; then continue 2; fi
      done
      printf '%s\n' "$line"
    done
  }
  status_after=$(git status --porcelain --untracked-files=no 2>/dev/null)
  if [ "$(printf '%s\n' "$status_after" | strip_untracked)" != \
       "$(printf '%s\n' "$status_before" | strip_untracked)" ]; then
    err "init changed the git index:
$(diff <(printf '%s\n' "$status_before" | strip_untracked) <(printf '%s\n' "$status_after" | strip_untracked) 2>/dev/null | head -20)"
    exit 1
  fi

  cmd_state .
}

# ---- commit ----------------------------------------------------------------

cmd_commit() {
  [ $# -ge 1 ] || usage
  local dir=$1 id='' msg='' branch lane_id phys q p hash tip own='' allow_large=0
  local diffout base cparent line cpath body pre mid suf left
  shift
  while [ $# -gt 0 ]; do
    case $1 in
      --as)          id=${2:-}; shift 2 || usage ;;
      -m)            msg=${2:-}; shift 2 || usage ;;
      --allow-large) allow_large=1; shift ;;
      --)            shift; break ;;
      *)             usage ;;
    esac
  done
  [ -n "$id" ] && [ -n "$msg" ] && [ $# -gt 0 ] || usage
  case $id in *[!a-z0-9-]*) err "bad --as id: $id"; exit 64 ;; esac
  phys=$(lane_realdir "$dir") || exit 1
  [ -d "$phys/.jj" ] || { err "not jj-colocated (run: jj-lane.sh init <dir> <id>): $phys"; exit 1; }
  take_lock "$phys"
  cd "$phys" || exit 1
  branch=$(lane_branch_jj) || branch=$(lane_branch_git .) || {
    err "no lane branch recorded (run: jj-lane.sh init)"; exit 1; }
  lane_id=$(lane_id_jj) || { err "no lane identity recorded (run: jj-lane.sh init)"; exit 1; }
  [ "$id" = "$lane_id" ] || [ "$id" = protocol ] || {
    err "--as must be the lane id ($lane_id) or protocol: $id"; exit 1; }
  # init is the only writer of auto-track; a repo missing it was never init'd.
  "$JJ_BIN" --ignore-working-copy config list --repo 2>/dev/null \
    | grep -q 'snapshot.auto-track = "none()"' || {
    err "snapshot.auto-track is not \"none()\" in repo config (run: jj-lane.sh init)"; exit 1; }

  # Canonicalize and guard every named path.
  local -a req=() files=() fs_req=() fs_files=() fs_dirs=()
  for p in "$@"; do
    q=$(realpath -m --relative-to=. -- "$p" 2>/dev/null) || { err "bad path: $p"; exit 1; }
    case $q in
      ''|.|..|../*|/*) err "path escapes the lane root: $p"; exit 1 ;;
    esac
    case $q in
      .git|.git/*|.jj|.jj/*)                err "repo internals are never committable: $p"; exit 1 ;;
      .ufo|.ufo/state|.ufo/state/*|.ufo/watchdog.log)
        err "driver runtime is never committed by a lane: $p"; exit 1 ;;
    esac
    if [ -d "$q" ]; then
      req+=("$q"); fs_dirs+=("root:\"$(fileset_escape "$q")\""); fs_req+=("root:\"$(fileset_escape "$q")\"")
    elif [ -e "$q" ] || [ -L "$q" ]; then
      req+=("$q"); files+=("$q")
      fs_files+=("root-file:\"$(fileset_escape "$q")\""); fs_req+=("root-file:\"$(fileset_escape "$q")\"")
      if [ "$allow_large" -eq 0 ] && [ "$(stat -c %s -- "$q" 2>/dev/null || echo 0)" -gt 10485760 ]; then
        err "named file over 10 MiB needs --allow-large: $q"; exit 1
      fi
    elif git cat-file -e "refs/heads/$branch:$q" 2>/dev/null; then
      # Deleted or renamed-away path present in the branch tip: include it so
      # the commit records the deletion.
      req+=("$q"); fs_req+=("root-file:\"$(fileset_escape "$q")\"")
    else
      echo "warn: skipping missing path $p" >&2
    fi
  done
  [ ${#req[@]} -gt 0 ] || { echo "nothing to commit (no such paths)"; exit 0; }

  tip=$(git rev-parse "refs/heads/$branch" 2>/dev/null || true)
  [ -n "$tip" ] || { err "refs/heads/$branch missing"; exit 1; }

  # Record tracking for named paths. --include-ignored (which also admits files
  # over snapshot.max-new-file-size) applies only to named FILES; a named
  # directory is tracked like `git add <dir>`, so ignored content stays out.
  if [ ${#fs_files[@]} -gt 0 ]; then
    "$JJ_BIN" --config "$AUTOTRACK_OFF" file track --include-ignored -- "${fs_files[@]}" 2>"$LOCKBASE.err" || {
      err "jj file track failed: $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"; exit 1; }
  fi
  if [ ${#fs_dirs[@]} -gt 0 ]; then
    "$JJ_BIN" --config "$AUTOTRACK_OFF" file track -- "${fs_dirs[@]}" 2>"$LOCKBASE.err" || {
      err "jj file track failed: $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"; exit 1; }
  fi

  # Snapshot the working copy under the requested paths. A jj failure (held
  # index.lock, stale working copy) is an error — never "nothing to commit".
  if ! diffout=$("$JJ_BIN" --config "$AUTOTRACK_OFF" diff --summary -- "${fs_req[@]}" 2>"$LOCKBASE.err"); then
    err "jj diff failed (held index.lock or stale working copy?): $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"
    exit 1
  fi

  if [ -z "$diffout" ]; then
    echo "nothing to commit"
    exit 0
  fi

  # The working copy must sit on the branch tip or the new commit is a stranded
  # sibling. Empty + wrong parent: re-anchor on the tip. Non-empty + wrong
  # parent: refuse — a seat's `jj commit wip` or a raw detached `git commit`
  # parked @ elsewhere and is never swept in or silently dropped.
  base=$(jj_ids '@-' commit_id | head -1)
  if [ "$base" != "$tip" ]; then
    if [ -n "$(jj_ids '@' 'if(empty,"x")')" ]; then
      "$JJ_BIN" --config "$AUTOTRACK_OFF" \
        --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
        new "$tip" >/dev/null 2>&1 || { err "cannot re-anchor working copy on the branch tip"; exit 1; }
    else
      err "working copy has changes on a non-tip base; refusing to sweep or strand work"
      exit 1
    fi
  fi

  # Stamp the working-copy author first: `jj commit <paths>` splits @ and keeps
  # @'s existing author, so a bare --config would only fix the committer.
  "$JJ_BIN" --config "$AUTOTRACK_OFF" \
    --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
    metaedit --update-author 2>"$LOCKBASE.err" || {
      err "metaedit failed: $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"; exit 1; }
  "$JJ_BIN" --config "$AUTOTRACK_OFF" \
    --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" \
    commit -m "$msg" -- "${fs_req[@]}" 2>"$LOCKBASE.err" || {
      err "jj commit failed: $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"; exit 1; }
  hash=$(jj_ids '@-' commit_id | head -1)
  [ -n "$hash" ] || { err "cannot read committed hash"; exit 1; }

  # Sweep guards (the bookmark stays put on any violation):
  # 1. The commit's parent must be the branch tip — a seat's own `jj commit`
  #    would otherwise be swept in below it.
  cparent=$(git rev-parse "$hash^" 2>/dev/null || true)
  if [ "$cparent" != "$tip" ]; then
    err "new commit's parent is not the $branch tip (a stray commit would be swept in); bookmark not moved"
    exit 1
  fi
  # 2. Every changed path falls under the requested paths; .ufo/state never.
  # 3. Phantom deletion: refuse a committed deletion of a file that still
  #    exists on disk (a nested empty .git dir makes jj see deletions).
  path_ok() { # <path> — every changed path must lie under a requested path
    local cp=$1 rp2
    case $cp in .ufo/state|.ufo/state/*)
      err "commit would touch .ufo/state: $cp"; exit 1 ;;
    esac
    for rp2 in "${req[@]}"; do
      case $cp in "$rp2"|"$rp2"/*) return 0 ;; esac
    done
    err "commit changed a path outside the request: $cp"; exit 1
  }
  while IFS= read -r line; do
    [ -n "$line" ] || continue
    case $line in
      R\ *|C\ *)
        # Rename/copy: `R {old => new}`, `R pre{old => new}suf`, or `R a => b`.
        body=${line:2} pre='' mid='' suf=''
        case $body in
          *"{"*"=>"*"}"*)
            pre=${body%%\{*}; mid=${body#*\{}; mid=${mid%%\}*}; suf=${body#*\}}
            path_ok "$pre${mid%% => *}$suf"
            path_ok "$pre${mid#* => }$suf" ;;
          *" => "*)
            path_ok "${body%% => *}"; path_ok "${body#* => }" ;;
          *) err "cannot parse rename in diff summary: $line"; exit 1 ;;
        esac
        continue ;;
    esac
    cpath=${line:2}
    path_ok "$cpath"
    case $line in
      D\ *)
        if [ -e "$cpath" ] || [ -L "$cpath" ]; then
          err "commit would delete $cpath but it exists on disk (nested repo?) — refusing"
          exit 1
        fi ;;
    esac
  done < <("$JJ_BIN" --ignore-working-copy diff --summary -r "$hash" 2>/dev/null)

  "$JJ_BIN" --ignore-working-copy bookmark set "$branch" -r "$hash" >/dev/null 2>&1 \
    || { err "bookmark set failed"; exit 1; }
  own=$hash

  # Warn about named files that exist but never became tracked (ignored or over
  # the size cap): jj refuses them silently.
  if [ ${#files[@]} -gt 0 ]; then
    left=$(git status --porcelain --ignored -z -- "${files[@]}" 2>/dev/null | tr '\0' '\n' | sed -n 's/^[?!][?!] //p')
    [ -z "$left" ] || printf 'warn: jj refused to track (ignored or over size limit), not committed: %s\n' "$left" >&2
  fi

  do_push "$branch" "$id" "$own" || exit 3
  exit 0
}

# ---- push ------------------------------------------------------------------

cmd_push() {
  local no_rebase=0 dir='' b lane_id phys
  while [ $# -gt 0 ]; do
    case $1 in
      --no-rebase) no_rebase=1; shift ;;
      *)           dir=$1; shift ;;
    esac
  done
  [ -n "$dir" ] || usage
  phys=$(lane_realdir "$dir") || exit 1
  [ -d "$phys/.jj" ] || { err "not jj-colocated: $phys"; exit 1; }
  take_lock "$phys"
  cd "$phys" || exit 1
  b=$(lane_branch_jj) || b=$(lane_branch_git .) || {
    err "no lane branch recorded (run: jj-lane.sh init)"; exit 1; }
  lane_id=$(lane_id_jj) || { err "no lane identity recorded (run: jj-lane.sh init)"; exit 1; }

  if [ "$no_rebase" -eq 1 ]; then
    # Driver durability push: fast-forward only, no fetch, no rebase.
    push_preflight "$b" || exit 3
    "$JJ_BIN" --config "$AUTOTRACK_OFF" git push --remote origin --bookmark "$b" 2>"$LOCKBASE.err" || {
      err "push rejected: $(head -3 "$LOCKBASE.err" | tr '\n' ' ')"; exit 3; }
    report_landed "$b" "" || exit 3
    exit 0
  fi

  do_push "$b" "$lane_id" "" || exit 3
  exit 0
}

case ${1:-} in
  init)   shift; cmd_init "$@" ;;
  commit) shift; cmd_commit "$@" ;;
  push)   shift; cmd_push "$@" ;;
  state)  shift; cmd_state "$@" ;;
  *)      usage ;;
esac
