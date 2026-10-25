# r92 AUTHOR (g3d) — RemoteTransform3D frame-boundary law + AnimationPlayer×body + SceneTree timing edges

Arm the r92 scout's measured surface: `reports/round-92/r92-scout.md` +
evidence `corpus/live/r92-scout/` (`probes/` 5 scripts, `driver.py`,
`runs/` 386 files — 114 cells ×3 backends, 342/342 rc=0, 111/114
rep-stable; the 3 exceptions named in §6).

Repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`. Harness:
`corpus/fixtures/run_battery.py` + `.gd` probes; per-round children are
named `r<N>_*.gd`/`r<N>_child.*` (see r90_child.gd, r91_child.py). Land
new probe script(s) as `corpus/fixtures/r92_*.gd` (or per convention),
append CASES insertion-only. Backends to sweep per cell: `proj`
(GodotPhysics), `proj_jolt`, `proj_dummy` — the scout reports all RT
cells backend-identical; pin the split rows where they differ (Dummy:
`body_get_state`/ray null+miss, `AnimatableBody3D`+sync_to_physics does
NOT move, resting depth 0.0000).

Claims to pin (from scout §0/§6):
- **RemoteTransform3D writes land at the next frame boundary**, never
  inside the writing frame — both write phases (physics cb, idle cb),
  read by same-frame-later node AND next-frame node (`rt_proj_phase`
  verbatim rows).
- AnimationPlayer×body surface: pin `ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS`
  — the fixture-design law (idle-callback animation is not rep-stable
  under unthrottled headless; key on `pf`-stamped observables `pos`,
  `srv`, `lv`, `tr`, never `seq`/`n_e`/`n_f`/`anim_t`).
- SceneTree timing edges + the rider-settle split (GP 2.9973 / Jolt
  3.0000 / Dummy 3.0000) and keyless-track resting depth per-backend
  table.
- `Animation` `-1` return edge (scout §warning): an author who ignores
  the -1 return gets a fixture that "plays" and destroys silently — pin
  the error-return check.
- The 3 non-rep-stable cells (§6): arm as envelopes/distributions, never
  constants — teardown/lifecycle cells carry ≥6 reps (r90 lesson).

After landing: run the FULL battery ≥2× — all prior rows byte-identical
(name the count), new cells rep-stable or enveloped. Report →
`reports/round-92/r92-author.md` with counts, counting commands, and any
scout correction (disclose). Do NOT commit.
