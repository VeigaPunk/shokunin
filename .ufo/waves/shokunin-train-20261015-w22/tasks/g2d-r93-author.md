# g2d-r93-author — author the AnimationPlayer/Tween lattice

Custody free (r92 landed 5900431). Read scout reports/round-93/r93-scout.md + probe corpus/live/r93-scout/ + boundary (tweens OVERSHOOT not clamp — BACK below start, SPRING above end; await N process_frame => N-1 applied steps; expo closed forms; manual-clock law; DEFERRED vs IMMEDIATE callback split; crossfade w_i=(i-1)/(N-1); ff is a STABILIZER not destabilizer).

- Author only boundary-surviving claims; encode overshoot values, the N-1 await law, crossfade weight formula with step-granularity scope; negative controls.
- Insertion-only run_battery.py; land probe into corpus/fixtures/.
- Battery green twice on final bytes (documented flakes only). Commit nothing. Report reports/round-93/r93-author.md. Return: report path, files, rows, blockers.
