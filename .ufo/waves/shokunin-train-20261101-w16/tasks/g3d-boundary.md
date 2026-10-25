# r85 BOUNDARY (g3d) — adversarial backend edges

Read SHARED.md + r84 boundary/critic first. Attack the r84 landing:
- impersonation edges the guard misses: physics_engine strings not yet
  tested ('Jolt Physics ' trailing space, 'JOLT PHYSICS', empty, int)
  — what does the child actually run?
- the new total dispatch: --child --arm=<each known arm>; --child with
  --arm=jolt_edge under a DEFAULT project (arm/backend mismatch);
  --child --arm=threaded_edge under a Jolt project.
- stale-log forge re-test post-fold: does remove_absolute actually
  close it (craft a pre-existing child.log with forged CHILD_RESULT
  lines, confirm the spawn overwrites)?
- ObjectDB leak arm: can a child leak an Object in a way that evades
  the mirrored WARNING scan (different message text)?
- phase_delta edge: write from _ready (pre-first-frame), write during
  a callback, write during physics via call_deferred — do they all
  land on the two measured deltas or is there a third class?
Report -> reports/round-85/r85-boundary.md.
