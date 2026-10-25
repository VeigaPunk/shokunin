# Goal — game-dev-2d-shokunin training loop (39 rounds) + 3D Epic re-vendoring side-round

Created 2026-10-18 by write-goal flow with the operator. This file is the
binding verbatim contract; the `CreateGoal` objective references this path
and summarizes it. If the two diverge, this file wins.

## Intent

Train the game-dev-2d-shokunin lane (fleet root /home/vgpnk/Projects/shokunin/,
lane repo game-dev-2d-shokunin/) through 39 shokunin craft rounds — a 13-round
provider/subagent schedule repeated 3 cycles — and, as one orchestrator-driven
side round, re-vendor the EpicGames unreal-engine-skills-for-claude-code-plugin
repository from scratch into game-dev-3d-shokunin with a UE-runtime unlock
attempt. All rounds run under the shokunin protocol: 1–3 single-axis claims per
round, per-axis verdicts only, no scalars, honest stop.

The two game-dev lanes are integrated by nature but keep distinct, properly
differentiated methods: this run must leave each lane's method stated and
differentiated —

- 2D: executable headless-fixture battery on Godot 4.7.2
  (depth/coverage/calibration lattice);
- 3D: multi-engine census, executability cards, static/format-level
  verification with REA support, runtime labeled proven/unproven —

with cross-lane integration only via routed, evidence-cited lesson imports,
never scope absorption.

## DONE WHEN

- 39 consecutive 2D rounds, numbered 101–139 (if 101 is occupied when the run
  starts, shift to the first free round and keep 39 consecutive), each closed
  in the fleet MANIFEST.json rounds[] ledger with claims, per-axis verdicts,
  and evidence pointers.
- Each 2D round has a contentful report at
  game-dev-2d-shokunin/reports/round-<N>/ (work performed with evidence
  pointers; landed changes tied to LOG.md entries and commits; before→after
  per claim with its counting command; SHONEN section). Marker-file reports
  count as failed rounds.
- Every 2D round commits under the lane identity
  `game-dev-2d <game-dev-2d@shokunin.local>`; LOG.md grows append-only, one
  entry per round.
- The 3D side-round is closed: Epic repo re-vendored at a fresh recorded pin
  (PROVENANCE.md); 12/12 tracked files byte-identical 3-way verification;
  executability cards + Claude→Kimi adaptation table updated; close-out gate
  green with adversary seats; UE runtime status honestly labeled (proven with
  command evidence if the docker unlock succeeds, else unproven with the
  attempt log); and the method-differentiation statement landed in both lanes'
  PROVINCE.md/SKILL.md, non-author verified, cross-checked against both SHONEN
  box 4 (no cross-domain bleed).
- SHONEN.md reflects reality at all times; if all four boxes become checkable
  by named non-author verifiers mid-run, stop and request the operator's
  promotion review (promotion itself is operator-owned).

## ROUND SCHEDULE

2D round = 100 + k for k = 1..39; loop position p = ((k-1) mod 13) + 1;
exactly one batched AgentSwarm per round:

| p | 2D rounds | provider / model | seats |
|---|---|---|---|
| 1–3 | r101–103, 114–116, 127–129 | opencode-go/deepseek-v4.1-flash | 64 |
| 4 | r104, 117, 130 | hyper/deepseek-v4.1-flash (fallback: devin/deepseek-v4-1-flash-high) | 32–64 |
| 5 | r105, 118, 131 | openai-codex/gpt-6-luna-max — verification round: audit current cycle's prior rounds for correctness, missed defects, unverifiable verdicts | 64 |
| 6 | r106, 119, 132 | xai-oauth/grok-4.7-fast | 128 |
| 7–8 | r107–108, 120–121, 133–134 | zai-coding-plan/glm-5.3-flash | 16–32 |
| 9 | r109, 122, 135 | openai-codex/gpt-6.1-sol-max | 16–32 |
| 10 | r110, 123, 136 | devin/deepseek-v4-1-flash-high | 64–128 |
| 11 | r111, 124, 137 | devin/glm-5-3-flash-max | 32–64 |
| 12 | r112, 125, 138 | antigravity/gemini-3.8-flash | 16–32 |
| 13 | r113, 126, 139 | antigravity/gemini-4-argon | 8–16 |

The 3D re-vendoring side-round runs once before 2D r105 (first verification
round), dispatched on devin/deepseek-v4-1-flash-high with 32–64 seats.

## LOOP (every 2D round)

1. Read the lane's SCORECARD.md; declare the axes in play.
2. Declare 1–3 claims — each one axis-move with a falsifiable before→after;
   ≥1 on the lane's lowest non-retired axis (stagnation nudge the only waiver).
3. Dispatch ONE AgentSwarm with the scheduled seats; scopes partitioned
   non-conflicting (planner/connector, executor/scribe/scout, reviewer/critic).
4. Land every claim.
5. Judge EVERY axis: improved / harmed / unchanged / unprovable-but-better
   (last only with a named non-author reviewer).
6. Admit only if every claim verifies AND no axis is harmed; a trade anywhere
   is reported, never averaged into an accept.
7. Record: verdicts in SCORECARD.md, evidence in LOG.md, report at
   reports/round-<N>/, closure in MANIFEST.json rounds[]; commit under the
   lane identity.

## INSTALLS (operator-authorized for this run)

- pacman packages; python/node toolchains; Godot export templates (already
  present — verify, don't reinstall); docker images incl.
  wukakuki/unreal-engine:dev-slim-5.8.3 (26.8G; 774G free) for the UE runtime
  unlock.
- Never: Epic-account linking or any credential/login action, license
  acceptance on the operator's behalf, engine source builds that take >2h, or
  publishing.
- Blocked installs go to the L0 channel and are routed around, not forced.

## BOUNDARIES

- 2D rounds write only inside game-dev-2d-shokunin/, the MANIFEST.json
  rounds[] ledger, and fleet .ufo/ side-channel files. The 3D side-round
  writes only inside game-dev-3d-shokunin/. Never edit other sibling lanes,
  the roster, or the Epic upstream (vendored copies keep license + PROVENANCE
  pin).
- Method separation is enforced, not assumed: the 2D battery method and the
  3D census/cards method are each lane's own; a lane may import a sibling's
  lesson only as a routed, cited reference; contested scope is reported via
  the L0 channel, never absorbed.
- Local-first: no publishing, no store submission, no domain-facing actions.
- Never fabricate runtime evidence: label unproven surfaces unproven and
  verify at the strongest available level (headless Godot battery first; UE
  runtime only via the docker unlock, else static/format-level).

## STOP AND REPORT instead of forcing when

- A scheduled provider AND its p4 fallback are exhausted (never substitute an
  unscheduled provider).
- The same blocker repeats 3 consecutive rounds.
- A claim stays unprovable / an axis is harmed — report all verdicts honestly
  and halt progression on that axis.


## Amendments (operator directives, 2026-10-18, mid-run after r103)

These supersede the SCHEDULE/DONE-WHEN text above (operator's live directive
wins over the original contract text; the goal-objective summary carries the
pre-amendment numbers and is governed by this file per "file wins"):

1. **p10 provider swap**: the round-10-position deepseek-v4.1-flash swarm moves
   from `devin/deepseek-v4-1-flash-high` to `hyper/deepseek-v4.1-flash`
   ("use hyper provider for one of the deepseek v4.1 flash swarms instead of
   devin" — exactly one swap). p4 stays hyper; p11 stays devin/glm; the 3D
   side-round keeps its contracted `devin/deepseek-v4-1-flash-high`.
2. **p6 skipped**: the xai-oauth/grok-4.7-fast 128-seat rounds are SKIPPED
   entirely (all three cycles). The cycle becomes 12 positions; total 2D
   rounds = 36, numbered 101–136 (101–103 already closed pre-amendment).
3. **p9 model swap**: the 9th position uses `openai-codex/gpt-6-luna-max`
   instead of `gpt-6.1-sol-max` ("codex luna max"), seat count unchanged
   (16–32).

Amended cycle (positions p1..p12; 2D round = 100+k, k=1..36):
p1–3 opencode-go/deepseek-v4.1-flash x64; p4 hyper/deepseek-v4.1-flash 32–64
(fallback devin/deepseek-v4-1-flash-high); p5 openai-codex/gpt-6-luna-max x64
(verification round); p6 zai-coding-plan/glm-5.3-flash 16–32; p7 zai (same);
p8 openai-codex/gpt-6-luna-max 16–32 (was p9); p9 hyper/deepseek-v4.1-flash
64–128 (was p10, devin→hyper); p10 devin/glm-5-3-flash-max 32–64 (was p11);
p11 antigravity/gemini-3.8-flash 16–32 (was p12); p12 antigravity/gemini-4-argon
8–16 (was p13). Cycle boundary every 12 rounds (verification rounds at
k≡5 mod 12). 3D side-round unchanged: once, before 2D r105, devin/
deepseek-v4-1-flash-high, 32–64 seats.
