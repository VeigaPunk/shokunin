# r88 SCOUT (g3d) — the untested space-state read API family

The dss tier mapped get_direct_state acquisition/use. UNTESTED surface:
the OTHER PhysicsDirectSpaceState3D methods — intersect_shape (param
object identity), collide_shape (array return), cast_motion
(motion-vector shape query), get_rest_info, intersect_point, and the
PhysicsDirectBodyState3D getters not yet pinned (inverse_inertia,
inverse_mass, principal_inertia_axes under rotation, transform_basis).
Measure on GodotPhysics + Jolt + Dummy where each differs; pin exit
codes and return shapes; find any method that bypasses the access
gate (some queries run against the broadphase). Bounded probes, fresh
processes, byte-stable reps x3. Scratch corpus/live/r88-scout/;
report -> reports/round-88/r88-scout.md. Do NOT touch
phys3d_events.gd (r87 author in flight).
