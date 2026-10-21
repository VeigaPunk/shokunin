#!/usr/bin/env bash
# hyaku wave-slot — self-service global seat gate for swarm waves (operator 2026-10-21:
# "swwwarm heavy, 64-100 concurrent parallelization"). Every L1 calls `acquire` right before its
# ONE validated wave task call and dispatches the moment it prints `granted`; no orchestrator
# round-trip. A wave is granted when the measured live agents + recently granted seats + the
# wave fit under CAP, or when the session is nearly idle (so an oversize wave never starves).
# CAP defaults to 92: the session process refuses (does not queue) further `task` spawns once 100
# background jobs run, process-wide, nested seats and coordinators included ("Background job limit
# reached (100)"; a batch that hits it mid-way starts only part of the wave). Blocked coordinators
# write no transcript, so 8 job slots stay reserved for them: keep every wave at <= 88 seats.
#   wave-slot.sh acquire <lane> <wave> <seats> [timeout-seconds=7200]  -> exit 0 `granted …`, 3 timeout
#   wave-slot.sh release <lane> <wave>
#   wave-slot.sh status
# Live agents = subagent transcripts (*.jsonl, any depth) under the live session dir modified in the
# last WINDOW seconds (an agent inside one long tool call can look idle: undercount, by design
# corrected by PENDING). Session dir: $HYAKU_SESSION_DIR, else the path in $STATE/live-session-dir.
set -euo pipefail
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
CAP=${HYAKU_WAVE_CAP:-92} IDLE=${HYAKU_WAVE_IDLE:-10} WINDOW=${HYAKU_WAVE_WINDOW:-150} PENDING=${HYAKU_WAVE_PENDING:-180}
LEDGER="$STATE/wave-slots" LOCK="$STATE/wave-slots.lock"
mkdir -p "$STATE"; touch "$LEDGER"
die() { echo "wave-slot: $*" >&2; exit 2; }
session_dir() {
  local d=${HYAKU_SESSION_DIR:-}
  [ -n "$d" ] || d=$(cat "$STATE/live-session-dir" 2>/dev/null) || true
  [ -n "$d" ] && [ -d "$d" ] || die "no live session dir (set HYAKU_SESSION_DIR or $STATE/live-session-dir)"
  printf '%s\n' "$d"
}
live() { find "$(session_dir)" -name '*.jsonl' -newermt "@$(( $(date +%s) - WINDOW ))" 2>/dev/null | wc -l; }
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
    if [ $(( a + p + seats )) -le "$CAP" ] || [ $(( a + p )) -le "$IDLE" ]; then
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
  echo "live=$(live) pending=$(pending) cap=$CAP idle=$IDLE window=${WINDOW}s"
  cat "$LEDGER"
  ;;
*) sed -n '2,13p' "$0"; exit 64 ;;
esac
