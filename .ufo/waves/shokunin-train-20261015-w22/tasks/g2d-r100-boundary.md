# g2d-r100-boundary — boundary under load

Read `~/Projects/shokunin/game-dev-2d-shokunin/reports/round-100/` scout report + probe `corpus/live/r100-scout/`. Attack the row lattice:

- Replay all cells quiet + load (>=12 hogs) + `--fixed-fps` 30/60/120 + threaded physics where relevant; multiple fresh processes.
- Hunt ordering/phase/startup-mode artifacts (r95's k(k-1) cycle and r97's flush-order refutation are the pattern).
- Namespace `r100b_*`; kill own PIDs only; zero tracked writes; commit nothing.
- Write `reports/round-100/r100-boundary.md` + `corpus/live/r100-boundary/` receipts + manifest.sha256. Return: report path, verdict per claim, falsifications, blockers.
