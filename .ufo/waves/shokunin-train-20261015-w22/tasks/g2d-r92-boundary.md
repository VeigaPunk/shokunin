# Seat: g2d r92 boundary — attack r92 scout claims under load
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Read reports/round-92/r92-scout.md + its probe in corpus/live/r92-scout/probes/. Falsify under quiet + >=12 hogs + --fixed-fps variants where relevant (r91 boundary proved fixed-fps breaks nav timing claims — check scheduler-sensitivity everywhere). Probes r92b_*; godot headless; timeouts<=25s KILL. reports/round-92/r92-boundary.md + corpus/live/r92-boundary/. No tracked writes, no commits, kill hogs.
