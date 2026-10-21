#!/usr/bin/env bash
# hyaku wave-slot — self-service global seat gate for swarm waves (operator 2026-10-21:
# "swwwarm heavy, 64-100 concurrent parallelization"). Every L1 calls `acquire` right before its
# ONE validated wave task call and dispatches the moment it prints `granted`; no orchestrator
# round-trip. A wave is granted when the running agents + recently granted seats + the wave fit
# under CAP (default 98). The session process refuses (does not queue) further `task` spawns once
# 100 background jobs run, process-wide, nested seats and coordinators included ("Background job
# limit reached (100)"; a batch that hits it mid-way starts only part of the wave).
#   wave-slot.sh acquire <lane> <wave> <seats> [timeout-seconds=7200]  -> exit 0 `granted …`, 3 timeout
#   wave-slot.sh release <lane> <wave>
#   wave-slot.sh status
# Running agents = subagent transcripts (*.jsonl, any depth) under the live session dir that have
# no non-empty `<id>.md` output yet (every subagent writes it when it finishes; measured against
# proc:// 2026-10-21: 23 + 2 revived = 25 vs 26 jobs), plus REVIVED (agents revived by message
# after a first completion already own an .md). Session dir: $HYAKU_SESSION_DIR, else the path
# in $STATE/live-session-dir.
set -euo pipefail
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
CAP=${HYAKU_WAVE_CAP:-98} REVIVED=${HYAKU_WAVE_REVIVED:-3} PENDING=${HYAKU_WAVE_PENDING:-120}
LEDGER="$STATE/wave-slots" LOCK="$STATE/wave-slots.lock"
mkdir -p "$STATE"; touch "$LEDGER"
die() { echo "wave-slot: $*" >&2; exit 2; }
session_dir() {
  local d=${HYAKU_SESSION_DIR:-}
  [ -n "$d" ] || d=$(cat "$STATE/live-session-dir" 2>/dev/null) || true
  [ -n "$d" ] && [ -d "$d" ] || die "no live session dir (set HYAKU_SESSION_DIR or $STATE/live-session-dir)"
  printf '%s\n' "$d"
}
live() {
  local n=0 f
  while IFS= read -r -d '' f; do [ -s "${f%.jsonl}.md" ] || n=$((n + 1)); done \
    < <(find "$(session_dir)" -name '*.jsonl' -print0 2>/dev/null)
  echo $(( n + REVIVED ))
}
pending() { awk -v t="$(( $(date +%s) - PENDING ))" '$1 >= t {s += $2} END {print s + 0}' "$LEDGER"; }
cmd=${1:-}; shift || true
case $cmd in
acquire)
  lane=${1:?lane} wave=${2:?wave} seats=${3:?seats} timeout=${4:-7200}
  [[ $seats =~ ^[0-9]+$ ]] || die "seats must be an integer"
  end=$(( $(date +%s) + timeout ))
  while :; do
    exec 9>"$LOCK"; flock -x 9
    a=$(live) p=$(pending)
    if [ $(( a + p + seats )) -le "$CAP" ]; then
      printf '%s %s %s %s\n' "$(date +%s)" "$seats" "$lane" "$wave" >> "$LEDGER"
      flock -u 9
      echo "granted lane=$lane wave=$wave seats=$seats live=$a pending=$p cap=$CAP"
      exit 0
    fi
    flock -u 9
    [ "$(date +%s)" -lt "$end" ] || { echo "timeout lane=$lane wave=$wave seats=$seats live=$a pending=$p cap=$CAP"; exit 3; }
    sleep 20
  done
  ;;
release)
  lane=${1:?lane} wave=${2:?wave}
  exec 9>"$LOCK"; flock -x 9
  awk -v l="$lane" -v w="$wave" '!($3 == l && $4 == w)' "$LEDGER" > "$LEDGER.tmp" && mv "$LEDGER.tmp" "$LEDGER"
  echo "released lane=$lane wave=$wave"
  ;;
status)
  echo "running=$(live) pending=$(pending) cap=$CAP revived_allowance=$REVIVED"
  cat "$LEDGER"
  ;;
*) sed -n '2,16p' "$0"; exit 64 ;;
esac
