#!/usr/bin/env bash
# shokunin-watchdog v3 — respawn-per-round fleet driver.
#
# Structure (matches PROTOCOL.md round-robin + operator directive):
#   - 8 lanes, each owned by exactly one live OMP TUI mission at a time.
#   - A lane's round ends when its report lands at
#     .ufo/reports/round-<N>/<lane>.md (or the pane dies = failed round).
#   - On round end the watchdog COMPLETES the mission and LAUNCHES a fresh
#     process with a generated round-N+1 prompt. Lanes self-iterate by
#     respawning, not by steer-queued turns.
#   - Round counters + missionIds persist in .ufo/state/<lane>.{round,mission}.
#   - Cap: 1024 rounds per lane. Tick: 450s.
set -u
SK=/home/vgpnk/projects/shokunin
UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting
OV=/tmp/fleet-override.yml
INTERVAL=450
MAX_ROUNDS=1024
mkdir -p "$SK/.ufo/state" "$SK/.ufo/prompts" "$SK/.ufo/reports"

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
mission_of() { cat "$SK/.ufo/state/$1.mission" 2>/dev/null; }
report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ] || [ -f "$SK/.ufo/reports/round-$2/${1}-shokunin.md" ]; }

lane_prompt() {
  local lane="$1" n="$2"
  mkdir -p "$SK/.ufo/reports/round-$n"
  case "$lane" in
    aggregator)
      cat <<EOF
You are the shokunin aggregator L1 (model m_qwen), round $n of up to $MAX_ROUNDS. Working dir: /home/vgpnk/projects/shokunin.
1. Read PROTOCOL.md, CORPUS.md, MANIFEST.json, and every child repo's latest LOG.md + corpus/ state.
2. Review all reports under .ufo/reports/round-$n/ and round-$((n-1))/AGGREGATE.md if present.
3. Ensure each shokunin child repo has corpus/{README,knowledge/,lessons/} per CORPUS.md; seed missing pieces only inside corpus/ (never sibling-owned files).
4. Write .ufo/reports/round-$n/aggregator.md: per-lane quality review, cross-lane learnings worth generalizing into PROTOCOL.md, mint/no-mint assessment (mint only on >=2 documented demand instances or explicit operator directive).
5. L2 subagents: executor/scribe m_flash, reviewer m_composer, planner m_lunamax, critic m_zfl, connector m_antigravity, scout m_flash, sentinel m_grok, others m_zfl. | godspeed
EOF
      ;;
    protocol)
      cat <<EOF
You are the shokunin-protocol L1, round $n of up to $MAX_ROUNDS. Working dir: /home/vgpnk/projects/shokunin.
1. Inspect every child repo's new commits/LOG.md/corpus/ since your last round.
2. Land warranted protocol improvements in PROTOCOL.md / ROADMAP.md only (never MANIFEST.json, never child repos) and commit on the main repo.
3. Write .ufo/reports/round-$n/protocol.md with findings + landed changes. | godspeed
EOF
      ;;
    *)
      cat <<EOF
You are the ${lane}-shokunin L1, round $n of up to $MAX_ROUNDS. Working dir: /home/vgpnk/projects/shokunin/${lane}-shokunin.
Self-iterate your domain: pick the highest-value gap in your corpus/lessons, corpus/knowledge, or SKILL.md against your domain's real surfaces; land it inside ${lane}-shokunin/ only (SKILL.md, PROVINCE.md, corpus/, LOG.md), commit 'round-$n'; then write .ufo/reports/round-$n/${lane}.md in the main repo.
L2 subagents: executor/scribe m_flash, reviewer m_composer, planner m_lunamax, critic m_zfl, connector m_antigravity, scout m_flash, sentinel m_grok, others m_zfl. | godspeed
EOF
      ;;
  esac
}

launch_lane() {
  local lane="$1" n="$2" ts
  ts=$(date +%s)
  lane_prompt "$lane" "$n" > "$SK/.ufo/prompts/${lane}-round-$n.md"
  out=$("$UFO" launch \
    --run-id "shokunin-r${n}-${lane}-r${ts}" \
    --session-id "sess-${lane}-${ts}" \
    --title "r${n}:${lane}" \
    --substrate omp --fleet shokunin \
    --cwd "${LANE_CWD[$lane]}" \
    -- omp --model "${LANE_MODEL[$lane]}" --config "$OV" \
       "@${SK}/.ufo/prompts/${lane}-round-$n.md" 2>&1 || true)
  mid=$(printf '%s' "$out" | grep -o '"missionId": "[^"]*"' | head -1 | cut -d'"' -f4)
  if [ -n "$mid" ]; then
    echo "$mid" > "$SK/.ufo/state/$lane.mission"
    echo "$n" > "$SK/.ufo/state/$lane.round"
    echo "$(date -Is) launch ${lane} round=${n} mission=${mid}" >> "$SK/.ufo/watchdog.log"
  else
    echo "$(date -Is) launch-fail ${lane} round=${n} :: $(printf '%s' "$out" | tail -2)" >> "$SK/.ufo/watchdog.log"
  fi
}

tick=0
while :; do
  tick=$((tick+1))
  status=$("$UFO" status --lite 2>/dev/null || true)
  for lane in "${!LANE_CWD[@]}"; do
    n=$(round_of "$lane"); mid=$(mission_of "$lane")
    live=0; [ -n "$mid" ] && printf '%s' "$status" | grep -q "$mid" && live=1
    if [ "$n" -eq 0 ]; then
      launch_lane "$lane" 1
    elif [ "$live" -eq 0 ]; then
      # mission gone before report: count failed, respawn same round
      if report_of "$lane" "$n"; then
        launch_lane "$lane" $((n+1))
      else
        echo "$(date -Is) lane-dead-no-report ${lane} round=${n}; retry same round" >> "$SK/.ufo/watchdog.log"
        launch_lane "$lane" "$n"
      fi
    elif report_of "$lane" "$n" && [ "$n" -lt "$MAX_ROUNDS" ]; then
      # round complete: retire mission, respawn for next round
      "$UFO" complete --mission "$mid" --note "round $n complete" >/dev/null 2>&1 || true
      echo "$(date -Is) complete ${lane} round=${n}; respawning" >> "$SK/.ufo/watchdog.log"
      launch_lane "$lane" $((n+1))
    fi
  done
  echo "$(date -Is) tick=$tick" >> "$SK/.ufo/watchdog.log"
  sleep "$INTERVAL"
done
