# game-dev-3d round 74 — depth move: moving-agent semantics (lazy-update model)

**Stamp.** Game-dev-3d lane, round 74 (devin host, wave `shokunin-train-20261013-w5`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `fc9915e`, report-last `35a911c` — identity `game-dev-3d-shokunin`.

## Work performed

Characterized `NavigationAgent3D` under scripted motion — the agent is **fully lazy**: no per-tick update; observable state moves only inside forcing getters (`get_next_path_position`, `get_final_position`, `is_navigation_finished`, `is_target_reachable`) on the live node transform; pure readers (`get_current_navigation_path[_index]`, `is_target_reached`, `distance_to_target`) never trigger. Stored path freeze is **conditional**: re-query iff `euclid(agent, path[idx]) ≥ path_max_distance` (scribe's true-equality datapoint: 5.000000==pmd re-queries — strict `<`, not `≤`), anchored lazily at the first forcing call after re-assignment. Pop is monotone sequential strict-`<` on live position inside the forcing call — no skips, link endpoints pop mid-void. `reached`/`finished` latches survive arbitrary motion and gate even the pmd re-query off; ANY `target_position` assignment — same value included — unlatches, clears the stored path, resets idx. `set_target_position` synchronously clears the result; materialization anchors at read-time, not assignment-time.

## Landed changes

- `navagent3d_detour.gd` +501/−5 (18 `mv_*` stepwise-motion arms: `steps` = ordered tp/set_target/wait tuples pinning the complete per-step path array; `pmd` key; `_run_steps`/`_run_motion_arm`), `run_battery.py` +36/−0.
- `corpus/lessons/r74-navagent-moving-agent.md`; `reports/round-74/` — 8 seats + verifier + adjudicator.
- Measured extras: pmd authored-value gate (pmd=2 breaches at 4.53); bank-side re-anchor both directions; `finished`-latch whole-update freeze (latched agent 10.6 from path keeps stale array); signals as call-time artifacts (`path_changed` at materialization, `waypoint_reached` per pop, `target_reached`+`navigation_finished` co-fire).

## Before → after measurements

| metric | before | after |
|---|---|---|
| update model | "tickless, query-driven" (scout) | **fully pinned** — forcing set vs pure readers, dirty-flag, lazy materialization anchor |
| stored path | frozen-by-default (unbounded) | **conditional freeze** — strict-`<` pmd gate, idx reset, no undo |
| pop semantics | stationary strict-`<` (r72) | same gate, **call-time on live position** under motion |
| latch | observed holding | **release condition pinned** — ANY target re-assignment, no dedup |
| battery | 127 rows | **145/145 + 4/4 probes + Node 31/31**, prior rows byte-preserved |

## SHONEN

- [x] Declared falsifiable axis-move (depth), four claims measured and one refined (pmd strict `<` at equality)
- [x] Named non-author replay (AGREE 6/6 — pmd boundary recomputed independently, 6/6 byte-exact spots)
- [x] No axis harmed (additive; 127 prior rows byte-stable, seeds unchanged)
- [x] Bounded claims; UNKNOWNs retained (internals, map-mutation tracked arms, other builds)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
