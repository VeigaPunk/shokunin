# game-dev-3d round 71 — depth move: distance_to_target is postprocessing-invariant (Euclidean)

**Stamp.** game-dev-3d lane, round 71 (devin host, wave `shokunin-train-20261013-w2`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `6888875`, report-last `996ea37` — identity `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`.

## Work performed

Resolved whether `path_postprocessing` changes the r70-established Euclidean `distance_to_target` semantics. Result: **invariant** — 3.605551 (√13, raw `target_position`) under corridorfunnel(0)/edgecentered(1)/none(2) while the queried path provably changes: pathlen 4.130649 → 4.707107 (edgecentered via edge midpoints) → 4.549510 (none, raw corridor); `next` (2,0,1)→(2,0,0.5); npts 3→4. The declared claim's `get_final_position`-changes clause was **measured false** — `final`=(2.5,0,3.5) invariant under all values; pinned as an invariance witness instead of asserted. Critic's reachable-clamped arm proves the raw-target referent holds under postprocessing too.

## Landed changes

- `corpus/fixtures/navagent3d_detour.gd` +45 additive (`--post-edgecentered`/`--post-none` arms; enum constants on `NavigationPathQueryParameters3D`, set before `target_position`) + `run_battery.py` +4 (two CASES rows with per-arm pathlen pins — `next` alone can't separate edgecentered/none, gap 0.1576 ≈ 39× tol rides on `path[2]`/pathlen).
- `corpus/lessons/r71-navagent-postproc-review.md` — per-value semantics table, companion facts (no-requery, empty-path-before-first-next, simplify_path falsifier, server `query_path` parity), retained UNKNOWNs.
- `reports/round-71/` — 8 seat reports + verifier + adjudicator.
- Boundary measured the next surfaces: `path_metadata_flags` per-bit companion-array gate; `pdd` Euclidean waypoint-pop with saturate-at-last-index; `is_navigation_finished` two-mode (reachable→`euclid(agent,raw target)<tdd` strict / unreachable→`euclid(agent,clamped final)≤~pdd`); `reachable` inclusive vs `reached` strict at equality; through-wall fire reproduced.

## Before → after measurements

| metric | before | after |
|---|---|---|
| Godot battery | 88/88 + 4 probes (frozen `9458c18`) | **90/90 + 4 probes** (author + verifier) |
| prior rows | — | **88/88 × 11 fields, 0 mismatches** |
| Node suites | 31/31 | 31/31 unchanged |
| postprocessing surface | unprobed | three values pinned; falsification path live (`distance:=pathlen` → exit 1 measured) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose (falsified clause recorded, not softened)
- [x] Named non-author replay passed all old + new classifications
- [x] No axis harmed (+49/−0 total; 88 prior rows byte-stable; seeds_unchanged)
- [x] Bounded claims; UNKNOWNs retained honestly

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. Learning trends: expansion/quality/discernment all **improved**. No promotion action.
