# Seat: g3d navagent dissection — the 1-tick-miss flake mechanism
Lane: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin
navagent3d_retarget/follow miss by exactly N diagonal ticks (sqrt2/60) under load (r93 baseline F1). Dissect: reproduce under controlled load, isolate mechanism (move delta quantization? velocity projection? path_recalc timing?), deliver verdict pinnable/envelope/stochastic + fix spec. Probes namespace r101n_*; gitignored corpus/live/navagent-dissection/. reports/round-101/navagent-dissection.md. No tracked writes, no commits.
