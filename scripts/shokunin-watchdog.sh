#!/usr/bin/env bash
# shokunin-watchdog — keep the shokunin fleet at 7 L1 missions.
# Polls `ufo-sighting status` every 450s; relaunches any missing lane with the
# same lane prompt and model binding. Lane list and prompts are the contract.
set -u
SK=/home/vgpnk/projects/shokunin
UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting
OV=/tmp/fleet-override.yml
INTERVAL=450

declare -A LANE_CWD=(
  [protocol]="$SK"
  [kasegi]="$SK/kasegi-shokunin"
  [kengaku]="$SK/kengaku-shokunin"
  [kake]="$SK/kake-shokunin"
  [kumitate]="$SK/kumitate-shokunin"
  [kotoba]="$SK/kotoba-shokunin"
  [aggregator]="$SK"
)
declare -A LANE_MODEL=(
  [protocol]=@m_swe [kasegi]=@m_swe [kengaku]=@m_swe
  [kake]=@m_swe [kumitate]=@m_swe [kotoba]=@m_swe
  [aggregator]=@m_qwen
)

while :; do
  sleep "$INTERVAL"
  live=$("$UFO" status --lite 2>/dev/null | grep -c 'running' || true)
  for lane in "${!LANE_CWD[@]}"; do
    if ! "$UFO" status --lite 2>/dev/null | grep -q "r1:${lane}"; then
      ts=$(date +%s)
      "$UFO" launch --run-id "shokunin-r1-${lane}-r${ts}" \
        --session-id "sess-${lane}-${ts}" \
        --title "r1:${lane}" --substrate omp --fleet shokunin \
        --cwd "${LANE_CWD[$lane]}" \
        -- omp --model "${LANE_MODEL[$lane]}" --config "$OV" \
           "@${SK}/.ufo/prompts/${lane}-L1.md" >/dev/null 2>&1 || true
    fi
  done
  echo "$(date -Is) watchdog tick (live-missions-in-last-status≈$live)" >> "$SK/.ufo/watchdog.log"
done
