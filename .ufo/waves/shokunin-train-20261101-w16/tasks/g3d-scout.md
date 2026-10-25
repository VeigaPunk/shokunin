# r85 SCOUT (g3d) — backend x threading surface map

Read SHARED.md + r84 reports first. Pre-measure the r85 frontier:
- Jolt x threaded: does a Jolt child under run_on_separate_thread=true
  produce the same arm split? Any new timing classes?
- Dummy backend inventory: what does physics/3d/physics_engine="Dummy"
  actually return for each query arm? (ClassDB registration? null
  space? zero-size returns? exceptions?)
- server-write surfaces: which PhysicsServer3D direct writes bypass
  the object-level lock? body_set_state vs position assignment timing.
- remaining backend gap: is there any 4th engine value registered on
  this build (hint enumeration); is 'Jolt Physics' the only working
  non-DEFAULT?
- sweep for OTHER under-armed query surfaces in phys3d_events (ray
  vs shape vs point vs motion coverage asymmetries).
Report -> reports/round-85/r85-scout.md.
