# audio-r89-foldfix — fold the r89 gate-fail fixes into committed bytes (dispatch after r87r88-foldverify lands)

The r89 verifier reported 1464/1484 green with a gate failure on x_top / x_foot / g_hup arm classes (reports/round-89/r89-verifier.md). The r89 reports name: SIGHUP inheritance on arm children, zero-row behavior, census races, and a 52-leg counting correction. A semantic fix exists for parts of this in the UNCOMMITTED working tree of corpus/fixtures/measure_audio.py — but r87+r88 fold work also lives there; disentangle carefully.

Duties:
1. Read reports/round-89/r89-{author,critic,reviewer,verifier}.md + the fold reports for r87/r88 (reports/round-87/r87-fold.md, reports/round-88/r88-fold.md once filed).
2. Fold only the boundary-surviving r89 fixes into measure_audio.py — SIGHUP inheritance handling, census-race guards, x_top/x_foot/g_hup arm-class accounting, the 52-leg count correction. Never weaken a gate to make it green; classify host/session-manager confounds under named coverage classes instead.
3. Re-run the affected legs bounded; every exit-signature claim needs a live receipt under corpus/live/r89-foldfix/.
4. Keep the change minimal and separately reviewable — insertion-friendly where the harness allows.
5. File reports/round-89/r89-foldfix.md. Zero commits; do not touch other rounds' evidence.

Constraints: seat-owned PipeWire names (prefix r89f_); verify module index before unload; NEVER pactl set-default-sink/source; TMPDIR=/home/vgpnk/Projects/shokunin/tmp.

Return: report path, legs re-run, green/fail census, blockers.
