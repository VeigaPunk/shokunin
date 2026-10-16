# Seat: g2d r94 boundary — attack r94 scout claims under load
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Read reports/round-94/r94-scout.md + its probe in corpus/live/r94-scout/probes/. Falsify under quiet + >=12 hogs + --fixed-fps variants where relevant (r91 boundary proved fixed-fps breaks nav timing claims — check scheduler-sensitivity everywhere). Probes r94b_*; godot headless; timeouts<=25s KILL. reports/round-94/r94-boundary.md + corpus/live/r94-boundary/. No tracked writes, no commits, kill hogs.
