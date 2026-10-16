# Seat: g2d r89 author — Geometry2D lattice landing

Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Head: fd59c11 or later (r88 fold committed; run_battery.py is yours to edit)

Scout: reports/round-89/r89-scout.md (committed 7fd640f) — 20 verbatim-ready CASES rows, probe at corpus/live/r89-scout/probes/geo_lattice.gd (land to corpus/fixtures/).
Boundary: reports/round-89/r89-boundary.md (committed 5be63e9) — 19/20 rows confirmed.

## MANDATORY boundary folds
- `input89_edges_exact` is LOAD-BIMODAL: quiet `just_after_flush=w_jp[ex=false inex=true]` vs loaded `…inex=false]`. Use the verbatim alt payload from the boundary report — tuple envelope, not a single pin.
- Edge-input arms: do NOT add rows that hit the boundary's new fatal vectors (bool clip >=1e15, any INF vertex, make_atlas (1e6,1e6), bresenham NaN → hang) unless pinned as crash/hang rows with bounded timeouts.
- Zero-rect atlas poisons the whole atlas; tiny-geometry floors (1e-4/1e-5) and silent sentinels are pinnable laws if you choose those rows.

## Conventions
- Follow r88 row shape in run_battery.py; prefixes get expected-error floor-gate coverage (extend the whitelist-gate loop to `r89_` like `r88_` was added).
- Probe sha goes in the row comment; byte-verify pins against fresh reps (>=6) before landing; envelope any cell you cannot make mode-invariant.
- Battery must be 215+N/215+N twice on final bytes before you report; note r88-fold tree state in the report.
- Report: reports/round-89/r89-author.md; corpus/live/r89-author/ receipts + manifest.

Read the task file; then operate autonomously. Commit nothing — leave work + report untracked for the orchestrator. Return: report path, files changed, row count, blockers.
