#!/usr/bin/env bash
# shokunin-watchdog v4 — respawn-per-round fleet driver, fleet-2 lane map.
# SSOT: MISSION.md. A lane's round ends when .ufo/reports/round-<N>/<lane>.md
# lands; watchdog completes the mission and launches a fresh process for
# round N+1. Cap 1024/lane. Tick 450s.
set -u
SK=/home/vgpnk/Projects/shokunin
UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting
OV=/tmp/fleet-override.yml
INTERVAL=450
MAX_ROUNDS=1024
mkdir -p "$SK/.ufo/state" "$SK/.ufo/prompts" "$SK/.ufo/reports"

LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"
declare -A LANE_CWD=(
  [protocol]="$SK"
  [aggregator]="$SK"
  [kasegi]="$SK/kasegi-shokunin"
  [kengaku]="$SK/kengaku-shokunin"
  [kake]="$SK/kake-shokunin"
  [kumitate]="$SK/kumitate-shokunin"
  [kotoba]="$SK/kotoba-shokunin"
  [kagi]="$SK/kagi-shokunin"
  [kama]="$SK/kama-shokunin"
)
declare -A LANE_MODEL=(
  [protocol]=@m_swe [aggregator]=@m_swe [kasegi]=@m_swe [kengaku]=@m_swe
  [kake]=@m_swe
  [kumitate]=@m_swe [kotoba]=@m_swe [kagi]=@m_swe [kama]=@m_swe
)
declare -A LANE_AXES=(
  [protocol]="fleet-meta: protocol soundness, gate integrity"
  [aggregator]="cross-lane quality, mint/dormancy calls, corpus review"
  [kasegi]="depth + coverage (bounty/security research)"
  [kengaku]="novelty + calibration (LLM eval/research)"
  [kake]="operability + freshness (web properties)"
  [kumitate]="operability + coverage (orchestration/tooling)"
  [kotoba]="depth + consistency (prompt/skill craft)"
  [kagi]="freshness + calibration (secrets/vault ops)"
  [kama]="operability + freshness (local model serving/endpoints)"
)

round_of() { cat "$SK/.ufo/state/$1.round" 2>/dev/null || echo 0; }
mission_of() { cat "$SK/.ufo/state/$1.mission" 2>/dev/null; }
report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }

lane_prompt() {
  local lane="$1" n="$2"
  mkdir -p "$SK/.ufo/reports/round-$n"
  cat > "$SK/.ufo/prompts/${lane}-round-$n.md" <<EOF
You are the ${lane} L1, round $n of up to $MAX_ROUNDS. Working dir: ${LANE_CWD[$lane]}.

BINDING: Read MISSION.md + AXES.md at /home/vgpnk/Projects/shokunin first — they are the mission SSOT. Your axes: ${LANE_AXES[$lane]}.

Each round is ONE axis-move: pick the lowest-scoring axis in ${LANE_CWD[$lane]}/SCORECARD.md (create it per AXES.md if missing), land one verifiable improvement, measure it, record before→after in SCORECARD.md, log evidence in LOG.md. Saturated or wrong-fit axes may be retired/split — record the reason.

L2 CONCURRENCY: dispatch at least 8 L2 task subagents in ONE batched task call this round — per-surface scouts, executors drafting sections into scratch, a critic falsifying claims, a connector for sibling overlap, a reviewer verifying citations. Route map: planner/connector @m_lunamax; executor/scribe/scout @m_flash; reviewer/critic/sentinel/revenger/labrat/mutation-tester/simplifier/distiller @m_zfl (fallback: @m_flash).

Write .ufo/reports/round-$n/${lane}.md on the main repo.
Round end: commit 'round-$n' inside the repo then push; also commit+push the main-repo report. PUSH ONLY to VeigaPunk/shokunin and your own VeigaPunk/${lane}-shokunin remote — domain source trees (ufo-fsd-alpha, bounties, webzites, llm-wiki) are read-only; upstream work is documented in the report, not pushed.
L0 side channel: if you need an operator decision, append "<lane> | round-$n | <question>" to /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md. | godspeed
EOF
}

launch_lane() {
  local lane="$1" n="$2" ts out rid
  ts=$(date +%s)
  rid="shokunin-r${n}-${lane}-r${ts}"
  lane_prompt "$lane" "$n"
  out=$("$UFO" launch \
    --run-id "$rid" \
    --session-id "sess-${lane}-${ts}" \
    --title "r${n}:${lane}" \
    --substrate omp --fleet shokunin \
    --cwd "${LANE_CWD[$lane]}" \
    -- omp --model "${LANE_MODEL[$lane]}" --config "$OV" \
       "@${SK}/.ufo/prompts/${lane}-round-$n.md" 2>&1 || true)
  if printf '%s' "$out" | grep -q 'activeMissions\|"ok":true'; then
    echo "$rid" > "$SK/.ufo/state/$lane.mission"
    echo "$n" > "$SK/.ufo/state/$lane.round"
    echo "$(date -Is) launch ${lane} round=${n} runId=${rid}" >> "$SK/.ufo/watchdog.log"
  else
    echo "$(date -Is) launch-fail ${lane} round=${n} :: $(printf '%s' "$out" | tail -2)" >> "$SK/.ufo/watchdog.log"
  fi
}

tick=0
while :; do
  tick=$((tick+1))
  status=$("$UFO" status --lite 2>/dev/null || true)
  for lane in $LANES; do
    n=$(round_of "$lane"); mid=$(mission_of "$lane")
    live=0; [ -n "$mid" ] && printf '%s' "$status" | grep -q "$mid" && live=1
    if [ "$n" -eq 0 ]; then
      launch_lane "$lane" 1
    elif [ "$live" -eq 0 ]; then
      if report_of "$lane" "$n"; then
        launch_lane "$lane" $((n+1))
      else
        echo "$(date -Is) lane-dead-no-report ${lane} round=${n}; retry same round" >> "$SK/.ufo/watchdog.log"
        launch_lane "$lane" "$n"
      fi
    elif report_of "$lane" "$n"; then
      if [ -f "$SK/.ufo/fleet-wrap" ]; then
        "$UFO" complete --mission "$mid" --note "fleet wrap: round $n landed, not respawning" >/dev/null 2>&1 || true
        echo "$(date -Is) wrap ${lane} round=${n} complete; NOT respawning (fleet-wrap)" >> "$SK/.ufo/watchdog.log"
      elif [ "$n" -lt "$MAX_ROUNDS" ]; then
        "$UFO" complete --mission "$mid" --note "round $n complete" >/dev/null 2>&1 || true
        echo "$(date -Is) complete ${lane} round=${n}; respawning" >> "$SK/.ufo/watchdog.log"
        launch_lane "$lane" $((n+1))
      fi
    fi
  done
  echo "$(date -Is) tick=$tick" >> "$SK/.ufo/watchdog.log"
  sleep "$INTERVAL"
done
