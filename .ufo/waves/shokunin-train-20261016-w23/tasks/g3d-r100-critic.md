# g3d-r100-critic — wave-B gate on the r100 landing commit (fill at dispatch)

Standard critic duties on the r100 main-loop rate + runtime-probe landing (author seat's commit; read reports/round-100/r100-author.md for the claim set, r100-scout.md + r100-boundary.md for the evidence base).

- COMMITTED tree only, load preferred. Attack the landed bytes: re-derive signatures, hunt false-positive paths, adversarial edge legs.
- Zero tracked writes; commit nothing. corpus/live gitignored — seat receipts under corpus/live/r100-critic/.
- Report reports/round-100/r100-critic.md. godot --headless + timeout-bounded.
- Return: report path, verdict, findings, blockers.
