# Seat: g2d r89 simplifier — proven dead-code/dead-row deletions
Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Find deletions in the r89 diff (8cea888) + newly-orphaned code: unused probe arms, unreachable paths, dead expected_errors entries (cross-check vs whitelist + receipts). PROVE each: byte-identical outputs before/after on >=2 reps, or static reachability. Output a patch + per-item proof in reports/round-89/r89-simplifier.md + corpus/live/r89-simplifier/. Do NOT apply to tracked files; no commits.
