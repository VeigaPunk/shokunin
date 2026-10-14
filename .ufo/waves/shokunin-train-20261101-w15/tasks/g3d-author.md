# r84 AUTHOR (g3d) — Jolt-pinned backend cells + write-phase deltas

Read SHARED.md + r83 author/adjudicator/critic/reviewer first. The r83
corrections are the ordered frontier.

ARM — `phys3d_events.gd` extension (insertion-only; prior 10 rows +
prior batteries byte-identical):
- `jolt_edge` parent arm: generate a `physics_engine="Jolt Physics"`
  child project (mirror `threaded_edge`'s thrproj pattern -> joltproj),
  re-exec this script `-- --child --arm=jolt_edge`, child prints
  `CHILD_RESULT jolt_<arm>=<outcome>` per reduced arm
  (isect/cast/btm/contact_stale/static_nopair minimum). Parent pins
  the per-arm backend split {same-signature | differs-constants |
  inverts} — `static_nopair` is the known inverter (ov=1 sig=1 under
  Jolt). Jolt availability gate first: absent -> honest `blocked`
  row, never fabricate.
- `phase_delta` arm: a process-phase write followed by the event-tier
  measurement pinning delta=2 (critic C1's correction as a first-class
  cell), contrasted against the physics-phase delta=1 already armed.
- `timeout -s KILL` on the child spawn (F2 fold already landed — keep
  the pattern); child log scan keeps the unexpected-ERROR class check.
Report -> reports/round-84/r84-author.md.
