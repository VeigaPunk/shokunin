# g2d-r97-verifier — wave-B gate on the r97 landing commit (fill at dispatch)

Standard verifier duties on the r97 landing: git archive the landing commit into a pinned tree under corpus/live/r97-verifier/tree/, re-run the full battery, re-derive cell claims where feasible, forgery/mutation sensitivity on the signature gate.

- Zero tracked writes; commit nothing. godot --headless + timeout-bounded.
- Report reports/round-97/r97-verifier.md.
- Return: report path, verdict, findings, blockers.
