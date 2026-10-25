# g3d-r94-author — author the cannon.js/PyBullet-style lattice

r93 author just landed (661749f) — run_battery.py custody is free. Read scout reports/round-94/ + boundary reports/round-94/r94-boundary.md (heavy falsifications: internalStep NOT pure, body-add-order not neutral, dt=0 NaN freeze, 15*mu*g law is mu/v0-dependent, fixedStep wall-clock, GridBroadphase unusable).

- Author ONLY rows whose claims survived the boundary; encode corrected laws; negative controls for the crash/refusal classes.
- Insertion-only edits to run_battery.py; new fixture files under corpus/fixtures/.
- Battery to green on final bytes (tolerate only documented load-flake rows). Commit nothing — leave work + report untracked for orchestrator.
- Report to reports/round-94/r94-author.md. Return: report path, files changed, row count, blockers.
