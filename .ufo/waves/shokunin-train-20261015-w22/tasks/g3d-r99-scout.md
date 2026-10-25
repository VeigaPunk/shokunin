# r99 SCOUT (g3d) — the AnimationTree / AnimationNodeBlendTree surface

Repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`. You are the
r99 scout. The r92 scout named `AnimationTree`/`AnimationNodeBlendTree`
"the largest unprobed animation surface" (r92 report §7.6, r86 rank 11).
Pre-measure it under `--headless` on Godot `4.7.2.stable.arch_linux.ed1daf0bf`.

Scope guidance (measure, don't enumerate):
- ClassDB census: which AnimationTree/AnimationNode* classes exist and
  `can_instantiate` headless (r97 census method applies).
- Building a minimal AnimationTree from script: root node assignment
  (`AnimationNodeAnimation`, `AnimationNodeBlendTree`, state machine),
  `active=true` semantics, parameter writes (`parameters/conditions/*`,
  blend positions), playback travel/start/stop observable through body or
  transform pins.
- The per-backend question: animation parameters are node-side (expect
  backend-inert — verify on `proj`/`proj_jolt`/`proj_dummy` rather than
  assume).
- Rep-stability: ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS law from r92 —
  which AnimationTree paths remain rep-stable in unthrottled headless?
- Teardown/lifecycle cells ≥6 reps; anything bimodal gets a mode census,
  not a pin.

Contract: leaf seat — zero tracked writes; scratch under
`corpus/live/r99-scout/` (`probes/`, `driver.py`, `runs/` sidecars,
`manifest.sha256`, `RECEIPTS.md`); report → `reports/round-99/r99-scout.md`
with headline claims, verbatim measured values, author directives,
remaining unknowns. `--headless`, `timeout`-bounded, no stray processes.
[O]/[I]/[?] labels.
