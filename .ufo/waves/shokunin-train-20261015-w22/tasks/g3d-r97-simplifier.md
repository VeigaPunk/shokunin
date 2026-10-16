# g3d-r97-simplifier — wave-B gate on committed ec27b78

Standard simplifier duties on the r97 nodelat landing (ec27b78, 324 rows, fixtures r97_nodelat.gd + 10 r97_probe_*.gd, 79 cells/83 children). Boundary-surviving claims only. Known risks: xr pins degenerate rc=134 distribution (envelope phrased); softfloor two-valued census; ClassDB census corrected 44->45.

- COMMITTED tree only, load preferred. Zero tracked writes; commit nothing.
- corpus/live is gitignored here. Report reports/round-97/r97-simplifier.md.
- Return: report path, verdict, findings, blockers.
