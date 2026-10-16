# Seat: g3d r93 author — Area3D signal-in-tick ordering surface

Lane: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin
Head: 75739bc (r92 fold committed; run_battery.py is yours)

Scout: reports/round-93/r93-scout.md — signal ordering lattice.
Boundary: reports/round-93/r93-boundary.md (454aea1) — ordering law CONFIRMED under batching: signal lands after _integrate_forces, before _physics_process in the detecting tick.

## MANDATORY boundary folds
- queue_free exit lands AFTER _physics_process (post-E), not in-step — pin the measured truth.
- monitoring writes inside signal dispatch are REFUSED (`ERROR: Function blocked during in/out signal`) — pinnable expected-error.
- Backend splits: GP does NOT detect frozen-body teleports, Jolt DOES; Jolt multi-overlap order is ~12% unstable — pin only per-backend facts, never per-body order.
- Same-tick monitoring off->on differs GP vs Jolt.
- Dummy backend: no detection — vacuous, pin as backend-qualified if at all.
- Adopt `--fixed-fps` (r100 scout: deterministic scheduler, byte-identical under 8-way load) for new probe arms where it helps determinism.

## Conventions
- r92-shaped rows in run_battery.py; extend expected-error floor gate to `r93_` rows like r92's.
- Probe lands at corpus/fixtures/r93_*.gd; sha in row comments; >=6 fresh reps per pin; envelopes where modes are real.
- Battery 258+N twice green on final bytes before reporting.
- Report: reports/round-93/r93-author.md + corpus/live/r93-author/ (gitignored; manifest + shas in report). No commits.
