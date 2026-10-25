# r83 AUTHOR (g3d) — Godot PhysicsServer3D generated-event two-tier lattice

Read SHARED.md + frontier ports/frontier/fb-physserver.md + r82 author report.

ARM — the two-tier claim (xconnector X5): PhysicsServer3D QUERIES are
edge-0 same-turn (r82-banked frontier: flat {*:0}) while GENERATED
events (contact signals, body_test_motion results, cast_motion,
intersect_shape) bind at the PHYSICS TICK — a two-tier lattice inside
one server. Extend the Godot-side probe family in corpus/fixtures/
(the Godot battery machinery is run_battery.py + godot probes):
- generated-event cells: body_test_motion/cast_motion/intersect_shape
  called mid-frame vs at-tick; contact signal emission timing
- run_on_separate_thread=true project setting: inline->deferred
  conversion cell (does the same-turn query still bind edge-0?)
- Jolt availability gate FIRST: check PhysicsServer3DManager /
  project settings for the backend; absent -> record which backend
  this build ships and bound the claim to it.
Viability-conditional; engine-semantic pins (callables invoked vs not),
never timing-only. bpy battery untouched. Report ->
reports/round-83/r83-author.md.
