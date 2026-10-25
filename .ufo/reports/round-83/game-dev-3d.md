# game-dev-3d round 83 — PhysicsServer3D two-tier lattice

**Stamp.** g3d lane, round 83 (wave `shokunin-train-20261101-w14`; recovery dispatch — gen-1 seats died 16:10Z, respawned 16:20Z; model mix: swe-2 author, deepseek-flash analysis seats, swe-2 baseline/verifier). Lane commits `e9145d9` (arm) + `4c1c100` (folds) + `c4b2fa2` (report-last).

## Work performed

New `corpus/fixtures/phys3d_events.gd` (+597) + 10 CASES rows in `run_battery.py` (+20) + README section: the query/event split inside PhysicsServer3D — `intersect_shape`/`cast_motion`/`body_test_motion`/`intersect_ray` (via `pp_queries`) vs `get_contact_count`, `body_entered`/`body_exited`, `area_set_monitor_callback`, `body_set_state_sync_callback`; `static_nopair` negative; `threaded_edge` re-exec under `run_on_separate_thread=true`.

## Measured (independent verifier + critic convergence)

- **Two-tier split confirmed by event kind** (scout premise-correction, not the brief's dss-vs-server guess): query APIs edge-0 in process and physics context; generated events land at the next physics tick; sync-callback once per active tick.
- **Critic counterexamples folded (r83-corr):** tick latency is write-phase-dependent (delta=1 physics-phase / delta=2 process-phase — 5/5 ×3 across DEFAULT/threaded/Jolt); `static_nopair` is GodotPhysics3D-scoped — Jolt fires ov=1 sig=1 (3/3 on copied seeds); `sig_log` cleared before the control.
- **Reviewer folds:** `timeout -s KILL 30` envelope on the threaded child (hung child previously orphaned past the battery kill — orphan evidence receipt); named fail on null dss; unexpected-ERROR scan on the child log.
- **ST characterization corrected:** process-context `space_get_direct_state` refusal is a deterministic context gate — the single granted sample is always the in-physics one (12/12); `nulls >= 8` pin retained for host variance. Jolt measured live-only: 7/10 cells re-bind, cast/btm differ on constants.

## Remaining / next frontier

- r84 seeds: Jolt-pinned backend rows (additive cells for the inverted negative + solver constants), contact-signal timing depth (write-phase deltas as first-class cells), DSS startup-window usability hole, body_entered node-level exit directions.
- Bounded: Godot 4.7.2.stable.arch_linux.ed1daf0bf, GodotPhysics3D + Jolt backends, this host.

## Seat record

9/9 landed: author, scout, boundary, baseline (bpy 83/83, godot 186/186, three.js 31/31 zero-drift on freeze `f8a088c`), scribe (dead-draft archive + stdout→stderr join hazard flagged pre-landing), critic (C1/C2 landed), reviewer (F1–F6), simplifier (D1/D2/D4/D5/V6 replay-identical), verifier AGREE 18/18 (case tables byte-identical ×4). Adjudicator: ADMIT-corr.
