#!/usr/bin/env bash
# hyaku fleet-commit — the only way hyaku lane/closure sessions commit to the
# fleet repo. Serializes every fleet-repo commit+push behind one flock so
# concurrent lanes never race on the index or on origin, keeps commits
# pathspec-limited (never add -A / commit -a), and carries the lane identity.
#
#   fleet-commit.sh --as <lane-id> -m "<message>" -- <repo-relative path>...
#
# Exit: 0 committed+pushed (or nothing to commit) · 1 commit failed ·
#       3 committed locally but push failed (commit is kept; next push carries it) · 64 usage.
set -u
FLEET=${SHOKUNIN_ROOT:-/home/vgpnk/Projects/shokunin}
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
LOCK="$STATE/fleet-git.lock"
REMOTE=${FLEET_REMOTE:-origin}
BRANCH=${FLEET_BRANCH:-master}

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

mkdir -p "$STATE"
exec {lk}>"$LOCK" || { echo "cannot open lock $LOCK" >&2; exit 1; }
flock -w 1200 "$lk" || { echo "fleet lock timeout (1200s)" >&2; exit 1; }

cd "$FLEET" || exit 1
g() { git -c "user.name=${id}-shokunin" -c "user.email=${id}@shokunin.local" "$@"; }

existing=()
for p in "$@"; do
  if [ -e "$p" ] || git ls-files --error-unmatch -- "$p" >/dev/null 2>&1; then existing+=("$p")
  else echo "warn: skipping missing path $p" >&2; fi
done
[ ${#existing[@]} -gt 0 ] || { echo "nothing to commit (no such paths)"; exit 0; }

g add -- "${existing[@]}" || { echo "git add failed" >&2; exit 1; }
if git diff --cached --quiet -- "${existing[@]}"; then
  echo "nothing to commit"
else
  g commit -q -m "$msg" -- "${existing[@]}" || { echo "git commit failed" >&2; exit 1; }
  echo "committed $(git rev-parse HEAD)"
fi

# Push whatever local master carries beyond origin (also re-sends earlier
# commits whose push failed). No rebase: the tracked driver log keeps the
# tree dirty, and all fleet pushes go through this lock.
ahead=$(git rev-list --count "$REMOTE/$BRANCH..HEAD" 2>/dev/null || echo 1)
[ "$ahead" = 0 ] && exit 0
for i in 1 2 3 4; do
  if git push -q "$REMOTE" "HEAD:$BRANCH" 2>"$STATE/fleet-push.err"; then
    echo "pushed $(git rev-parse --short HEAD) ($ahead ahead)"; exit 0
  fi
  sleep $((i * 15))
done
echo "push failed (commit kept locally): $(head -3 "$STATE/fleet-push.err" | tr '\n' ' ')" >&2
exit 3
