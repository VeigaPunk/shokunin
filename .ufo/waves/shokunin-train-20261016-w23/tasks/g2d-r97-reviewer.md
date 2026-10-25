# g2d-r97-reviewer — wave-B gate on the r97 landing commit (fill at dispatch)

Standard reviewer duties on the r97 landing. Read reports/round-97/r97-author.md; re-run the full battery on the committed tree inside a pinned checkout; spot-re-derive cell claims.

- COMMITTED tree only. Zero tracked writes; commit nothing.
- corpus/live gitignored — receipts under corpus/live/r97-reviewer/.
- Report reports/round-97/r97-reviewer.md. godot --headless + timeout-bounded.
- Return: report path, verdict, findings, blockers.
