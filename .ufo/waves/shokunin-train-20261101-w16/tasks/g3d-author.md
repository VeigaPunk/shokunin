# r85 AUTHOR (g3d) — backend cross-product + refused shapes

Read SHARED.md + r84 author/adjudicator/critic/reviewer first. The
backend matrix is the frontier.

ARM — `phys3d_events.gd` extension (insertion-only; all 188 prior cases
byte-identical; child arms keep total dispatch + stale-log unlink +
timeout-KILL + ObjectDB scan):
- `jolt_threaded` cross-product arm: generated child with BOTH
  physics_engine="Jolt Physics" AND 3d/run_on_separate_thread=true —
  pin whether the backend split ({same|differs-constants|inverts})
  holds identically under the threaded stepper, or shifts. This is the
  third child-spawn site — consider whether the simplifier's deferred
  V2 (_spawn_child single-sourcing) is now justified; if you fold it,
  the two prior arms' receipts must stay byte-identical.
- Dummy-backend refused-shape cells (now classifiable post-guards):
  generated child with physics_engine="Dummy" — pin what the query
  arms report (expected: zero/silent reads -> 'unexpected' classes,
  NOT the known-class labels). This is a negative-control row: the
  cell proves the split is backend-real, not map coincidence.
- server-write phase-delta (stretch): PhysicsServer3D-level writes
  (body_set_state direct) vs object-level position writes — do they
  land on different tier boundaries? Measure honestly.
Report -> reports/round-85/r85-author.md.
