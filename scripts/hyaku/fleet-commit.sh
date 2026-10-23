#!/usr/bin/env bash
# hyaku fleet-commit — the only way hyaku lane/closure sessions commit to the
# fleet repo. Serializes every fleet-repo commit+push behind one flock so
# concurrent lanes never race on the repo or on origin, keeps commits
# pathspec-limited (only the named paths; untracked strays are never tracked),
# and carries the lane identity as author AND committer.
#
# VCS is Jujutsu (colocated .jj, operator directive 2026-10-23):
#   * every snapshotting jj call carries --config 'snapshot.auto-track="none()"';
#     every read-only jj call carries --ignore-working-copy;
#   * the first jj call snapshots, so commits made by plain git (HEAD/refs moved
#     outside jj) are imported before any jj transaction builds on them;
#   * main and master are fast-forwarded together to the new commit and pushed
#     with `jj git push`; a bookmark is never moved backwards or sideways and a
#     remote bookmark that is not an ancestor of the local one is never pushed.
#
#   fleet-commit.sh --as <lane-id> -m "<message>" -- <repo-relative path>...
#
# Exit: 0 committed+pushed (or nothing to commit) · 1 commit failed ·
#       3 committed locally but push failed (commit is kept; next push carries it) · 64 usage.
set -u
unset JJ_USER JJ_EMAIL
FLEET=${SHOKUNIN_ROOT:-/home/vgpnk/Projects/shokunin}
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
LOCK="$STATE/fleet-git.lock"
REMOTE=${FLEET_REMOTE:-origin}
BRANCH=${FLEET_BRANCH:-master}
MIRROR=${FLEET_MIRROR:-main}
BACKOFF=${FLEET_PUSH_BACKOFF:-15}
JJ_BIN=${JJ_BIN:-$(command -v jj 2>/dev/null || echo "$HOME/.local/bin/jj")}

usage() { echo "usage: fleet-commit.sh --as <lane-id> -m <message> -- <path>..." >&2; exit 64; }
id='' msg=''
while [ $# -gt 0 ]; do
  case $1 in
    --as) id=${2:-}; shift 2 || usage ;;
    -m) msg=${2:-}; shift 2 || usage ;;
    --) shift; break ;;
    *) usage ;;
  esac
done
[ -n "$id" ] && [ -n "$msg" ] && [ $# -gt 0 ] || usage
case $id in *[!a-z0-9-]*) echo "bad lane id: $id" >&2; exit 64 ;; esac
for p in "$@"; do
  case $p in /*|*..*) echo "path must be repo-relative without '..': $p" >&2; exit 64 ;; esac
  case $p in .ufo/state/*|.ufo/watchdog.log) echo "driver runtime is never committed by a lane: $p" >&2; exit 64 ;; esac
done
[ -x "$JJ_BIN" ] || { echo "jj not found (set JJ_BIN)" >&2; exit 1; }

mkdir -p "$STATE"
exec {lk}>"$LOCK" || { echo "cannot open lock $LOCK" >&2; exit 1; }
flock -w 1200 "$lk" || { echo "fleet lock timeout (1200s)" >&2; exit 1; }

cd "$FLEET" || exit 1
ERR="$STATE/fleet-jj.err"
# Snapshotting call (identity on author via metaedit, committer via config).
jw() { "$JJ_BIN" --config 'snapshot.auto-track="none()"' \
  --config "user.name=${id}-shokunin" --config "user.email=${id}@shokunin.local" "$@"; }
# Read-only call: one field per line for a revset.
jr() { "$JJ_BIN" --ignore-working-copy log --no-graph -r "$1" -T "$2 ++ \"\\n\"" 2>/dev/null; }
jerr() { head -3 "$ERR" 2>/dev/null | tr '\n' ' '; }
fileset() { printf 'root:"%s"' "$(printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"; }

# Import first: picks up git HEAD/refs moved by plain git before any jj write.
jw status >/dev/null 2>"$ERR" || { echo "jj status failed: $(jerr)" >&2; exit 1; }

existing=() track=()
for p in "$@"; do
  if [ -e "$p" ]; then existing+=("$(fileset "$p")"); track+=("$(fileset "$p")")
  elif [ -n "$("$JJ_BIN" --ignore-working-copy file list -r @- -- "$(fileset "$p")" 2>/dev/null)" ]; then
    existing+=("$(fileset "$p")")
  else echo "warn: skipping missing path $p" >&2; fi
done
[ ${#existing[@]} -gt 0 ] || { echo "nothing to commit (no such paths)"; exit 0; }

if [ ${#track[@]} -gt 0 ]; then
  jw file track -- "${track[@]}" >/dev/null 2>"$ERR" || { echo "jj file track failed: $(jerr)" >&2; exit 1; }
fi
changes=$(jw diff --summary -- "${existing[@]}" 2>"$ERR") || { echo "jj diff failed: $(jerr)" >&2; exit 1; }
committed=0
if [ -z "$changes" ]; then
  echo "nothing to commit"
else
  # `jj commit <paths>` keeps @'s author: stamp it first so author == committer.
  jw metaedit --update-author >/dev/null 2>"$ERR" || { echo "jj metaedit failed: $(jerr)" >&2; exit 1; }
  jw commit -m "$msg" -- "${existing[@]}" >/dev/null 2>"$ERR" || { echo "jj commit failed: $(jerr)" >&2; exit 1; }
  echo "committed $(jr @- commit_id)"
  committed=1
fi

# Fast-forward main and master to the commit under the working copy (also
# carries earlier commits whose push failed). Never backwards or sideways.
tip=$(jr @- commit_id)
for b in "$BRANCH" "$MIRROR"; do
  [ -n "$(jr "$b & ::$tip" commit_id)" ] || {
    [ -n "$(jr "$tip & ::$b" commit_id)" ] && continue   # tip already under the bookmark
    echo "push failed (commit kept locally): bookmark $b is not an ancestor of $tip (moved sideways or conflicted)" >&2
    exit 3; }
  "$JJ_BIN" --ignore-working-copy bookmark set "$b" -r "$tip" >/dev/null 2>"$ERR" || {
    echo "push failed (commit kept locally): bookmark set $b: $(jerr)" >&2; exit 3; }
done

# Push whatever main/master carry beyond origin (also re-sends earlier
# commits whose push failed), fast-forward only.
ahead=$(jr "$BRANCH@$REMOTE..$BRANCH" commit_id | grep -c .)
mirror_ahead=$(jr "$MIRROR@$REMOTE..$MIRROR" commit_id | grep -c .)
[ "$ahead" = 0 ] && [ "$mirror_ahead" = 0 ] && exit 0
for b in "$BRANCH" "$MIRROR"; do
  [ -n "$(jr "$b@$REMOTE & ::$b" commit_id)" ] || {
    echo "push failed (commit kept locally): $b@$REMOTE is not an ancestor of $b — refusing a backwards/sideways push" >&2
    exit 3; }
done
for i in 1 2 3 4; do
  if "$JJ_BIN" --ignore-working-copy git push --remote "$REMOTE" --bookmark "$BRANCH" --bookmark "$MIRROR" \
       >/dev/null 2>"$STATE/fleet-push.err"; then
    echo "pushed $(git rev-parse --short "$(jr "$BRANCH" commit_id)") ($ahead ahead)"; exit 0
  fi
  sleep $((i * BACKOFF))
done
echo "push failed (commit kept locally): $(grep -v -e '^Changes to push' -e '^  bookmark: ' "$STATE/fleet-push.err" | head -3 | tr '\n' ' ')" >&2
exit 3
