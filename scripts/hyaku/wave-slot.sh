#!/usr/bin/env bash
# hyaku wave-slot — self-service global seat gate for swarm waves (operator-requested target: 200).
# Every L1 calls `acquire` right before its ONE validated wave task call and dispatches the moment
# it prints `granted`; no orchestrator round-trip. A grant reserves seats when the estimated live
# agents + recent reservations + requested wave fit under the configured target (default 200).
# Observed 2026-10-21: L1 sessions kept dispatching full waves (~160 jobs at once overall) while
# Main's own spawns were refused with "Background job limit reached (100)"; reviving an idle
# agent by message still worked. A grant also waits while MemAvailable < MIN_AVAIL_MB (a seat
# workload spike stalled memory at 20% PSI full).
#   wave-slot.sh acquire <lane> <wave> <seats> [timeout-seconds=7200]  -> exit 0 `granted …`, 3 timeout
#   wave-slot.sh release <lane> <wave>
#   wave-slot.sh status
# Live estimate = subagent transcripts (*.jsonl, any depth) under the live session dir that have
# no non-empty `<id>.md` output yet (every subagent writes it when it finishes; measured against
# proc:// 2026-10-21: 23 + 2 revived = 25 vs 26 jobs), plus REVIVED (agents revived by message
# after a first completion already own an .md). Session dir: $HYAKU_SESSION_DIR, else the path
# in $STATE/live-session-dir.
set -euo pipefail
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
CAP_SOURCE=default REVIVED=${HYAKU_WAVE_REVIVED:-3} PENDING=${HYAKU_WAVE_PENDING:-120}
MIN_AVAIL_MB=${HYAKU_WAVE_MIN_AVAIL_MB:-6144}
LEDGER="$STATE/wave-slots" LOCK="$STATE/wave-slots.lock"
mkdir -p "$STATE"; touch "$LEDGER"
die() { echo "wave-slot: $*" >&2; exit 2; }
configured_cap() {
  local value source cap_file="$STATE/wave-cap"
  if [[ ${HYAKU_WAVE_CAP+x} ]]; then
    value=$HYAKU_WAVE_CAP
    source=environment
  elif [[ -e "$cap_file" || -L "$cap_file" ]]; then
    local -a lines
    if ! mapfile -t lines < "$cap_file"; then die "cannot read target from $cap_file"; fi
    [[ ${#lines[@]} -eq 1 ]] || die "$cap_file must contain one positive decimal integer"
    value=${lines[0]}
    source=state
  else
    value=200
    source=default
  fi
  [[ $value =~ ^[0-9]+$ ]] || die "wave target must be a positive decimal integer"
  while [[ ${#value} -gt 1 && ${value:0:1} == 0 ]]; do value=${value:1}; done
  [[ $value != 0 ]] || die "wave target must be a positive decimal integer"
  CAP=$value CAP_SOURCE=$source
}
fits_cap() {
  local used=$1 cap=$2
  [[ $used =~ ^[0-9]+$ ]] || return 1
  if ((${#used} < ${#cap})); then return 0; fi
  if ((${#used} > ${#cap})); then return 1; fi
  [[ $used == "$cap" || $used < $cap ]]
}
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
mem_avail_mb() { awk '/^MemAvailable:/ {print int($2 / 1024)}' /proc/meminfo; }
cmd=${1:-}; shift || true
case $cmd in
acquire)
  lane=${1:?lane} wave=${2:?wave} seats=${3:?seats} timeout=${4:-7200}
  [[ $seats =~ ^[0-9]+$ ]] || die "seats must be an integer"
  end=$(( $(date +%s) + timeout ))
  while :; do
    exec 9>"$LOCK"; flock -x 9
    configured_cap
    a=$(live) p=$(pending) m=$(mem_avail_mb) used=$((a + p + seats))
    if fits_cap "$used" "$CAP" && [ "$m" -ge "$MIN_AVAIL_MB" ]; then
      printf '%s %s %s %s\n' "$(date +%s)" "$seats" "$lane" "$wave" >> "$LEDGER"
      flock -u 9
      echo "granted lane=$lane wave=$wave seats=$seats live=$a pending=$p cap=$CAP"
      exit 0
    fi
    flock -u 9
    [ "$(date +%s)" -lt "$end" ] || { echo "timeout lane=$lane wave=$wave seats=$seats live=$a pending=$p cap=$CAP mem_avail_mb=$m min=$MIN_AVAIL_MB"; exit 3; }
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
  configured_cap
  a=$(live) p=$(pending)
  echo "live_estimate=$a recent_reservations=$p cap=$CAP cap_source=$CAP_SOURCE revived_allowance=$REVIVED mem_avail_mb=$(mem_avail_mb) min_avail_mb=$MIN_AVAIL_MB"
  cat "$LEDGER"
  ;;
*) sed -n '2,16p' "$0"; exit 64 ;;
esac
