# g3d-r100-reviewer — wave-B gate on the r100 landing commit (fill at dispatch)

Standard reviewer duties on the r100 landing. Read reports/round-100/r100-author.md; re-run the full battery on the committed tree inside a pinned checkout; spot-re-derive cell claims.

- COMMITTED tree only. Zero tracked writes; commit nothing.
- corpus/live gitignored — receipts under corpus/live/r100-reviewer/.
- Report reports/round-100/r100-reviewer.md. godot --headless + timeout-bounded.
- Return: report path, verdict, findings, blockers.
