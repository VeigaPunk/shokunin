# r92 BOUNDARY (g3d) — honest edges of the RT/anim surface

Repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`. Read
`reports/round-92/r92-scout.md` — work its §7 remaining unknowns and the
edges of the pinned claims. Bounded empirical probe: fresh `godot
--headless --path <proj> --script` runs (backend projects `proj`,
`proj_jolt`, `proj_dummy` per scout convention — copy the scout's
`corpus/live/r92-scout/` project-gen approach or reuse `driver.py`),
`timeout 15` + per-rep cap; scratch `corpus/live/r92-boundary/`, report →
`reports/round-92/r92-boundary.md`, [O]/[I]/[?], ≥3 reps per claim (≥6 for
teardown/lifecycle).

Probe candidates (pick the sharpest):
- The RT propagation mechanism: `set_process(false)`/
  `set_physics_process(false)` do NOT stop it (§7.1) — is there ANY
  script-visible switch that stalls RemoteTransform3D propagation? Try
  `update_callback`, reparenting, `top_level`, visibility, process_mode.
- Negative `time_scale`: `_physics_process` receives `delta=-0.016667` —
  what does it do to body state over N ticks? (bounded, fresh proj)
- `physics_jitter_fix` axis: the scout's `jitfix` arm was a no-op
  (default value) — write 0.0 and 1.0 and measure whether ANY pinned
  observable shifts.
- `AnimationMixer._reset()`/`reset_on_save` reachability from script.
- `Engine.get_physics_interpolation_fraction()` under a runtime
  `physics_interpolation` write.

No tracked writes, no commits. Cleanup: no stray godot processes at exit.
