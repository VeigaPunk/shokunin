# Seat: g2d r93 boundary — attack r93 scout claims under load
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Read reports/round-93/r93-scout.md + its probe in corpus/live/r93-scout/probes/. Falsify under quiet + >=12 hogs + --fixed-fps variants where relevant (r91 boundary proved fixed-fps breaks nav timing claims — check scheduler-sensitivity everywhere). Probes r93b_*; godot headless; timeouts<=25s KILL. reports/round-93/r93-boundary.md + corpus/live/r93-boundary/. No tracked writes, no commits, kill hogs.
