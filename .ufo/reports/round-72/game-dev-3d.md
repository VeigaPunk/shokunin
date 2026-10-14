# game-dev-3d round 72 — depth move: pdd waypoint-pop + two-mode is_navigation_finished

**Stamp.** game-dev-3d lane, round 72 (devin host, wave `shokunin-train-20261013-w3`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `05405ae`, report-last `f95a16e` — identity `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`.

## Work performed

Formalized the r71-boundary recon into tracked arms. Resolved model: **pop** `idx` while `idx<size−1 && euclid(agent,path[idx])<pdd` — strict, sequential, keyed on live 3D position over the fixed stored path, saturates at `size−1`; **`reached`** = `euclid(agent,rawT)<tdd` strict, through-wall, latched; **`reachable`** = `euclid(final→T)≤tdd` inclusive (only inclusive gate); **`finished`** = `reached OR (¬reachable ∧ idx==size−1 ∧ euclid(agent,final)<pdd)` strict, latched, non-monotone sawtooth across the reachability boundary.

## Landed changes

- `corpus/fixtures/navagent3d_detour.gd` +297/−1 (`--arm=<name>` 22-preset table, authored expectations + falsification path per clause) + `run_battery.py` +44/−0 (22 CASES rows).
- `corpus/lessons/r72-navagent-pdd-finish-review.md`; `reports/round-72/` — seat reports + verifier + adjudicator.
- Critic's `u_gap_pdd2.3` counterexample (idx-conjunct requirement) absorbed as claim-wording — the artifact already encoded the corrected model (byte-exact critic replay).

## Before → after measurements

| metric | before | after |
|---|---|---|
| Godot battery | 90/90 + 4 probes (frozen `996ea37`) | **112/112 + 4 probes** |
| prior rows | — | **90×12 fields, 0 mismatches** |
| Node suites | 31/31 | 31/31 unchanged |
| pop/finished semantics | scratch-measured | tracked arms + strict/inclusive table + sawtooth pin |
| `distance_to_target` | Euclidean to raw target | + **live call-time arithmetic** (boundary); path array frozen; latches recorded |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose (equality edges measured at every gate)
- [x] Named non-author replay passed all old + new classifications (112/112, 16/16 spot-checks verbatim)
- [x] No axis harmed (additive-only; seeds_unchanged)
- [x] Bounded claims; UNKNOWNs retained honestly (metadata-flag behavior, moving-agent dynamics, latch release, this-mesh-only pins)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
