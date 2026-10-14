# game-dev-3d round 79 — coverage/new-runtime: Blender bpy headless two-layer lattice

**Stamp.** 3D lane, round 79 (wave `shokunin-train-20261101-w10`; massacre — scout landed pre-massacre, operator-substituted author). Lane commits `08d1b10` + `9a2e7b1`.

## Work performed

`corpus/fixtures/bpy_sync_probe.py` (9 arms; scout's probes promoted + membership/draincheck/shared folded in) + `bpy_battery.py` sibling runner — 37 pinned cases. `run_battery.py` untouched → 176 prior rows byte-stable.

## Measured (37/37 PASS; scout lattice reproduced verbatim on tracked fixture)

Claim half-confirmed/half-narrowed: the split is **write-through vs evaluation-gated**, not RNA-vs-depsgraph — derived RNA (`matrix_world`) lags at w0 like held handles. `evaluated_depsgraph_get()` IS the eval event; graph shared (`is_same=True`) — one get flushes held handles. **No implicit drain** (3× stale through unrelated reads) — Godot's per-tick serve has no bpy analogue. Held-handle staleness unbounded (map_off-analogue). Membership via `object_instances` propagates held-stale/fresh-fresh. Evaluated `visible_get`/`hide_get` = pinned non-signal.

## Remaining

Verifier/critic v2 pending. Open cells: bpy.ops/driver/constraint eval edges, same-frame frame_set, wall-time drain check (frontier seat dispatched).
