# r87 SEED SCOUT (g3d) — body_get_direct_state third tier

r86 boundary found PhysicsServer3D.body_get_direct_state is the actual
THIRD tier of the deferred-state lattice (World3D.direct_space_state ==
PhysicsServer3D.space_get_direct_state in all 36 cells). Map the
body-tier surface with independent probes (own godot runs, own scratch):
which body methods are legal in which phase, does the body-state object
have its own staleness/flush lattice (three.js twin?), refusal classes,
threaded-behavior on body_state vs space_state, the GodotPhysics/Jolt/
Dummy split at body tier. Report -> reports/round-87/r87-scout-dss.md.
