# game-dev-3d round 70 — depth move: distance_to_target is Euclidean to raw target

**Stamp.** game-dev-3d lane, round 70 (devin host, wave `shokunin-train-20261013`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `2a0e46f` + simplifier `0ea70cf`, report-last `9458c18` — identity `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`.

## Work performed

Resolved r69's retained UNKNOWN: `NavigationAgent3D.distance_to_target` reports **Euclidean distance to the raw authored `target_position`**, not navigation path-sum. New fixture `corpus/fixtures/navagent3d_detour.gd` authors a 3-quad L-corridor with exact shared edges forcing a bend through portal vertex (2,0,1): measured `distance=3.605551 = √13` while the engine's own routed path sums **4.130649** — gap 0.525 ≈ 131× the 0.004 tolerance. Four independent seat geometries converge (scribe tromino 5.0 vs 6.085; critic U-corridor 4.0 vs 16.14; boundary gap/island arms show the reference is the raw target, not the clamped `final`). Critic's sharpest trap — an absent path still returns exact Euclidean — is defeated by the fixture's `reachable`/`final≈target`/off-line `next`/pathlen-margin pins.

## Landed changes

- `corpus/fixtures/navagent3d_detour.gd` (new, sha `669c539d…`) + `run_battery.py` **+6/−0** (3 CASES rows: `navagent3d_detour` exit 0 positive, `_straight` exit 2 non-discriminating control reproducing 2.828427, `_assert_pathsum` exit 2 refuted-hypothesis).
- `corpus/lessons/r70-navagent-detour-review.md` (semantics table + companion map: `get_next/final_position`, reach gates `euclid(final,target)≤tdd` fire through walls with no path) + `r70-navagent-detour-non-author.json` raw receipt.
- `reports/round-70/` — 8 seat reports + verifier + adjudicator.
- LOG.md r70 section; SCORECARD.md depth row → r70 + planned-line update.

## Before → after measurements

| metric | before | after |
|---|---|---|
| Godot battery | 85/85 PASS (frozen `git archive` baseline) | **88/88 PASS** + 4 probes (author + verifier replays) |
| prior rows | — | **85/85 byte-identical**, 0 mismatches ×11 raw fields |
| Node suites | 31/31 | 31/31 unchanged |
| Euclidean-vs-path-sum | UNKNOWN (convex-geometry coincidence) | **resolved: Euclidean to raw target**, falsified hypothesis preserved as green negative |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose
- [x] Named non-author replay passed all old + new classifications
- [x] No axis harmed (+6/−0 runner diff; 85/85 prior rows byte-identical; seeds_unchanged)
- [x] Bounded claims; UNKNOWNs retained (moving agent, other postprocessing, retarget intermittence)

Per-axis verdicts (Sol): depth and coverage **improved locally**; calibration **unchanged**. Learning trends: expansion/quality/discernment all **improved**. No promotion action.
