# Operator training directive — 2026-10-31

User directive: "hey i want you to train our shokunins, 10 rounds in sequence, using 20 workers concurrently; 8 devin/swe-2 8 zai/glm-5.3-flash; 4 minimax m3.1 flash | each batch of 10 rounds should focus one shokunin that hasn't reached 100 rounds of training yet"

## Current-run precedence

- Run ten sequential rounds on one eligible shokunin below round 100. Parent selects and steers each round; a fresh non-author closure must finish before the next dispatch. Existing security/operator holds remain binding.
- Exactly twenty L2 workers per round, dispatched together in ONE `task` call: eight `model: "devin/swe-2"`, eight `model: "zai/glm-5.3-flash"`, four `model: "minimax-code/MiniMax-M3.1-Flash"`. These selectors were observed in `omp models --json` on 2026-10-31.
- Use explicit per-task model selectors only for this run. No global routing changes or substitute-model fallbacks. Record requested/actual model, agent id and failed seats. Do not silently replace a failed seat or shrink the split.
- This directive supersedes historical round-size, role-route and parent handoff directives in the generated addendum. L1 may call `task` directly for its one twenty-worker batch; no `.ready` handoff is needed. Do not use the old dispatcher that ignores task-level models.
- Keep the substantive craft rules: 1–3 independent claims on distinct axes, frozen predicates and do-nothing controls before scoring, frontier/source curation, assimilation, executable evidence, honest verdicts, lane-local scope, append-only history, lane identities and commit-before-report ordering.
- If using the existing wave validator, copy its policy into the round evidence directory and set waveMinLanes=waveMaxLanes=20 in that snapshot. Do not change global policy. Include a planner data-walk and connector, and at least five genuine adversarial seats. Never pad tasks.
- One integration owner. Workers write only distinct seat-local scratch under `/fast/scratch/hyaku/<lane>-r<N>/<seat>`; never mutate fleet or lane git/jj state. L1 integrates and commits through the existing helpers. Carry the host safety/scratch guards in every seat prompt.
- Every delegated agent is authorized to install helpful tools after reading `/home/vgpnk/.omp/agent/RULES.md`; report tool/version/channel/reason. Do not bypass host package upgrade safety.
- Run the changed domain behavior, retain observed outputs as committed evidence, land the lane report, then return to the parent. Ten round attempts are not ten admitted rounds; retain honest rejection and halt on harmed/unprovable claims under the protocol.
