# g2d-r93-critic — wave-B gate on committed 4b75151

Standard critic duties on the r93 anim/tween landing (4b75151, 295 rows, fixtures anim_lattice.gd + r93b_anim.gd). Encoded: runtime overshoot (BACK<start, SPRING>end), N-1 await law, crossfade w_i=(i-1)/(N-1) at 3 granularities, DEFERRED->process+physics flush; floor gate r93_expected_errors_all_matched.

- COMMITTED tree only, load preferred. Zero tracked writes; commit nothing.
- Report reports/round-93/r93-critic.md + receipts corpus/live/r93-critic/.
- Return: report path, verdict, findings, blockers.
