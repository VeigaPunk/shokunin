# game-dev-3d round 75 — depth move: map/link mutation under a committed path

**Stamp.** 3D lane, round 75 (devin host, wave `shokunin-train-20261014-w6`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `6498973`, wording hygiene `cefc821`, report-last pending verifier — identity `game-dev-3d-shokunin <g3d@shokunin.local>`.

## Work performed

Measured NavigationServer3D map/link/region mutations under a committed path — the XConnector-recommended "zombie waypoint" arm. 11 `mut_*` arms on `navagent3d_detour.gd` (+464/−11), each a `steps` program of teleport/set_target/mutate/wait phases with `wait>=1` enforced for sync-blind readback. **156/156 + 4/4 probes + Node 31/31.**

**Measured model — the two-stage gate:** server-side (RID-level) mutations are gated (1) setter→server-sync (~2–3 physics frames) — a same-turn forcing call in this window serves stale/dead-link data, the bounded zombie window, NOT a universal bar; then (2) sync→first-forcing-call — the stored array stays byte-identical until a forcing getter re-queries anchored at live agent position; pure readers serve stale data indefinitely. Agent-side `navigation_layers` write is the synchronous exception (same-turn clear). **Latched zombie:** `is_navigation_finished` early-returns BEFORE the dirty check — a finished agent serves its pre-mutation path through `region_transform +5x` AND full `region_delete` until any `target_position` re-assignment unlatches. Re-mutations rematerialize without retargeting; empty-path tuple pinned (`next`=agent pos, `final=(0,0,0)`).

## Landed changes

- `navagent3d_detour.gd` +464/−11 (11 arms); `run_battery.py` rows + docstring fix for the thrice-flagged relative-`--runs` trap; `corpus/lessons/r75-navagent-map-mutation.md`; `reports/round-75/` 8 seat reports + adjudicator (+verifier pending).
- Corrections absorbed: "never SERVED" → post-sync scope (critic+reviewer, independent); r74 lesson pmd operand corrected to leg-SEGMENT; author-report stale sentence fixed (`cefc821`).

## Before → after measurements

| metric | before | after |
|---|---|---|
| mutation-under-path model | unmeasured (authoring-time setters only) | two-stage gate + latch interaction measured end-to-end |
| "zombie waypoint" | hypothesized | pinned: bounded same-turn window (pre-sync) + permanent under finished latch |
| battery | 145/145 | **156/156**, Node 31/31 |

## SHONEN

- [x] Declared falsifiable axis-move (depth); falsifications absorbed (universal "never served" → post-sync bound)
- [x] Named non-author replay — verifier in flight (respawned after rate-limit kill; spot-checks landing)
- [x] No axis harmed (additive arms; prior 145 rows 0-mismatch per baseline)
- [x] Bounded claims; UNKNOWNs retained (4.7.2 headless, single map/region; sync timing measured-not-cased; multi-agent/node-link unexercised)
