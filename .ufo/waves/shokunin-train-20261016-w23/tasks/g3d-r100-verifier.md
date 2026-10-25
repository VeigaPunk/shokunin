# g3d-r100-verifier — wave-B gate on the r100 landing commit (fill at dispatch)

Standard verifier duties on the r100 landing: git archive the landing commit into a pinned tree under corpus/live/r100-verifier/tree/, re-run the full battery, re-derive cell claims where feasible, forgery/mutation sensitivity on the signature gate.

- Zero tracked writes; commit nothing. godot --headless + timeout-bounded.
- Report reports/round-100/r100-verifier.md.
- Return: report path, verdict, findings, blockers.
