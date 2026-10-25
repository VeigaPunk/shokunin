# Seat: g3d r93 baseline-r2 — post-fold anchor on 75739bc
Lane: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin
The r92 fold (75739bc) changed fixtures after r93-baseline (a10f2c4, pre-fold) ran. Re-baseline: git archive 75739bc to a scratch dir, run the full battery x2 (258 rows), report byte-identity vs committed CASES + vs pre-fold baseline receipts; flag any new flakes by name (navagent 1-tick miss, size-gate granted-under-load, bpy render are already on record). reports/round-93/r93-baseline2.md + corpus/live/r93-baseline2/ (gitignored). No tracked writes, no commits.
