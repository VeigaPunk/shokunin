# Seat: g2d r90 author — RigidBody2D gravity/COM/integrator lattice
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Head: 8cea888 (r89 landed; run_battery.py is yours).
Scout: reports/round-90/r90-scout.md — rb2d gravity/COM/integrator lattice, 12/12 rep-stable, custom_integrator delta closed.
Boundary: reports/round-90/r90-boundary.md (520ed6d) — ordering law CONFIRMED 60/120tps BUT 30tps exposes late_body pairing (startup-race class); damp oracle is ENGINE-CONDITIONAL (Dummy silently vacuous - pin engine hint); dy=n*g*dt^2 confirmed; typed refusals set_inertia:334/set_mass:324; COM :376 sole path; freeze window load-proof.
## MANDATORY boundary folds
- Pin only 60tps-verified values OR qualify by tps; never pin the 30tps unstable N.
- Any motion-asserting row needs an engine precondition (Dummy = silent vacuity).
- impulse/extreme cells: inertia >=1e9 collapses the 6dp oracle; pin below that.
## Conventions
- r89-shaped rows; extend floor gate to r90_ prefixes; probe sha in comments; >=6 fresh reps per pin; envelopes for real modes; battery 235+N x2 green on final bytes.
- reports/round-90/r90-author.md + corpus/live/r90-author/. No commits.
