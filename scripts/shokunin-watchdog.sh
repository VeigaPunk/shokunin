#!/usr/bin/env bash
# shokunin-watchdog — fleet driver: keep 8 L1 missions live AND advance
# self-iterating rounds (target 1024/lane) by steering each parked lane at
# every 450s tick. A parked interactive OMP TUI needs an external nudge per
# round; the lane itself owns the iteration content.
set -u
SK=/home/vgpnk/projects/shokunin
UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting
OV=/tmp/fleet-override.yml
INTERVAL=450
MAX_ROUNDS=1024
mkdir -p "$SK/.ufo/state"

declare -A LANE_CWD=(
  [protocol]="$SK"
  [kasegi]="$SK/kasegi-shokunin"
  [kengaku]="$SK/kengaku-shokunin"
  [kake]="$SK/kake-shokunin"
  [kumitate]="$SK/kumitate-shokunin"
  [kotoba]="$SK/kotoba-shokunin"
  [kagi]="$SK/kagi-shokunin"
  [aggregator]="$SK"
)
declare -A LANE_MODEL=(
  [protocol]=@m_swe [kasegi]=@m_swe [kengaku]=@m_swe
  [kake]=@m_swe [kumitate]=@m_swe [kotoba]=@m_swe [kagi]=@m_swe
  [aggregator]=@m_qwen
)

round_of() { cat "$SK/.ufo/state/$1.round" 2>/dev/null || echo 0; }
bump() { echo "$2" > "$SK/.ufo/state/$1.round"; }

steer_for() {
  local lane="$1" n="$2"
  case "$lane" in
    aggregator)
      echo "Round $n of up to $MAX_ROUNDS: review lane reports .ufo/reports/round-* and each child repo's corpus/ + LOG.md; refresh .ufo/reports/round-$((n-1))/AGGREGATE.md quality review + mint/no-mint assessment; then write .ufo/reports/round-$n/aggregator.md." ;;
    protocol)
      echo "Round $n of up to $MAX_ROUNDS: inspect all child repos' new commits/LOG.md since your last round; land warranted protocol improvements (PROTOCOL.md/ROADMAP.md only, commit on main repo); then write .ufo/reports/round-$n/protocol.md." ;;
    *)
      echo "Round $n of up to $MAX_ROUNDS for ${lane}-shokunin: self-iterate — pick the highest-value gap in your own corpus/lessons or SKILL.md against your domain's real surfaces, land it inside ${lane}-shokunin/ only (edit SKILL.md/corpus/LOG.md, commit 'round-$n'), then write .ufo/reports/round-$n/${lane}.md in the main repo." ;;
  esac
}

tick=0
while :; do
  tick=$((tick+1))
  status=$("$UFO" status --lite 2>/dev/null || true)
  for lane in "${!LANE_CWD[@]}"; do
    state_file="$SK/.ufo/state/$lane.round"
    [ -f "$state_file" ] || { echo 0 > "$state_file"; }
    n=$(round_of "$lane")
    if ! printf '%s' "$status" | grep -q "r1:${lane}"; then
      # lane absent — (re)launch parked; it will self-iterate via its prompt
      ts=$(date +%s)
      first_round=$((n+1))
      bump "$lane" "$first_round"
      out=$("$UFO" launch --run-id "shokunin-r${first_round}-${lane}-r${ts}" \
        --session-id "sess-${lane}-${ts}" \
        --title "r1:${lane}" --substrate omp --fleet shokunin \
        --cwd "${LANE_CWD[$lane]}" \
        -- omp --model "${LANE_MODEL[$lane]}" --config "$OV" \
           "@${SK}/.ufo/prompts/${lane}-L1.md" 2>&1 || true)
      mid=$(printf '%s' "$out" | grep -o '"missionId": "[^"]*"' | head -1 | cut -d'"' -f4)
      [ -n "$mid" ] && echo "$mid" > "$SK/.ufo/state/$lane.mission"
      echo "$(date -Is) launch ${lane} round=${first_round} mission=${mid:-none}" >> "$SK/.ufo/watchdog.log"
    elif [ "$n" -lt "$MAX_ROUNDS" ]; then
      next=$((n+1)); bump "$lane" "$next"
      mid=$(cat "$SK/.ufo/state/$lane.mission" 2>/dev/null || echo "shokunin-r1-${lane}")
      "$UFO" steer --mission "$mid" --text "$(steer_for "$lane" "$next")" >/dev/null 2>&1 || true
      echo "$(date -Is) steer ${lane} -> round ${next} via ${mid}" >> "$SK/.ufo/watchdog.log"
    fi
  done
  echo "$(date -Is) tick=$tick" >> "$SK/.ufo/watchdog.log"
  sleep "$INTERVAL"
done
