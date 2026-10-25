# game-dev-3d round 73 — depth move: off-mesh navigation-link traversal gating

**Stamp.** game-dev-3d lane, round 73 (devin host, wave `shokunin-train-20261013-w4`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `b41fb33`, report-last `e435a01` — identity `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`.

## Work performed

Formalized off-mesh link gating into 15 tracked CASES arms on the detour fixture. All four declared claims confirmed: (a) companion arrays carry LINK-type at hop-start under `path_metadata_flags` per-bit control — **opt-OUT, default 7** (critic wording correction; meta=0 empties); (b) layers-bitmask / bidirectional-exit-side / enabled=false each independently drop the link to byte-identical no-link tuples (link-only mask → empty path + `final=(0,0,0)` third mode); (c) `enter_cost` structurally inert (10/100/1e6 — mechanism unexplained) vs `travel_cost` live; (d) pop-through symmetric — `next` points across the void forward AND retro.

## Landed changes

- `corpus/fixtures/navagent3d_detour.gd` +337/−2 (island quad, server+node link authoring, 15 `--arm=link_*` presets, flag read-back honesty gate) + `run_battery.py` +30/−0. `corpus/lessons/r73-navagent-link-gating-review.md`; `reports/round-73/` — 8 seat reports + verifier + adjudicator.
- Boundary bonuses: mid-flight `next` endpoint-switches never interpolated; chained links compose; `dist < link_connection_radius` strict; mid-hop retarget re-anchoring; `vertices.append_array` non-write-through gotcha pinned.

## Before → after measurements

| metric | before | after |
|---|---|---|
| Godot battery | 112/112 + 4 probes | **127/127** + 4 probes, 112×12 fields 0-mismatch |
| Node suites | 31/31 | 31/31 |
| link surface | greenfield (zero refs) | gate system measured end-to-end (metadata/gates/costs/pop-through) |
| enter_cost | anomaly suspected | **structurally inert** up to 1e6 (pinned, unexplained) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose (86+49+33+32 independent probes)
- [x] Named non-author replay passed all old + new (AGREE all five claims, 127/127 verbatim)
- [x] No axis harmed (additive-only; seeds_unchanged)
- [x] Bounded claims; UNKNOWNs retained (inertness mechanism, tie-break internals, moving agent)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
