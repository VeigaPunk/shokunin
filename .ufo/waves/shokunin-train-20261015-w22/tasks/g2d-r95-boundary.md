# Seat: g2d r95 boundary — attack r95 scout claims under load
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Read reports/round-95/r95-scout.md + its probe in corpus/live/r95-scout/probes/. Falsify under quiet + >=12 hogs + --fixed-fps variants where relevant (r91 boundary proved fixed-fps breaks nav timing claims — check scheduler-sensitivity everywhere). Probes r95b_*; godot headless; timeouts<=25s KILL. reports/round-95/r95-boundary.md + corpus/live/r95-boundary/. No tracked writes, no commits, kill hogs.
