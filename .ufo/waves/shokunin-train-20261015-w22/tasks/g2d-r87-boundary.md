# r87 BOUNDARY (g2d) — honest edges of the input lattice

Repo: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`. Read
`reports/round-87/r87-scout.md` — work its remaining-unknowns list and
the edges of pinned arms. Bounded empirical probe: fresh `godot
--headless --path <proj> --script` runs, `timeout 15` shell bound +
per-rep cap; scratch under `corpus/live/r87-boundary/`, report →
`reports/round-87/r87-boundary.md`, [O]/[I]/[?] labels, ≥3 reps per claim.

Probe candidates (pick the sharpest):
- `just_released=1` on first physics-phase read of an API/physics-resume
  press (§2.3 quirk) — characterize when it does/doesn't appear.
- `is_action_pressed(a, exact_match)` granularity — mixed exact+inexact
  bindings held simultaneously; does exactness ever flip a polled answer?
- The flaky-set characterization: `press_phys`/`release_edge`/`ui_ns` —
  is the bimodal choice correlated with frame timing, idle-vs-physics
  read position, or process identity? A ×10 mode census exists
  (`arms-flaky-r10.json`); try to find the selector.
- `InputMap.event_is_action` — census-listed but exercised by no arm.
- `pre_frame` latent-risk arm (shape 1, clean ×9): push reps, does it
  flake?

No tracked writes, no commits. Cleanup: no stray godot processes at exit.
