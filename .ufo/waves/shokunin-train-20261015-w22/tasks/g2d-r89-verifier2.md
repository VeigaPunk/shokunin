# g2d-r89-verifier2 — verify folded r89 on 53a0be7

Freeze git archive 53a0be7; verify the r89 fold bytes:

- Full battery >=2 reps on folded bytes; every r89 row must PASS with the new required_stderr pin populated; lineempty real PASS vs critic forges (fp_wrongcause/fp_stderr_sig must FAIL).
- Confirm SP1+F5 deletions: 530-line geo2d_lattice.gd, removed arms gone, byte-identical row outputs vs pre-fold 8cea888 pins.
- r90 rows must be untouched (12/12 PASS, byte-identical markers).
- Report reports/round-89/r89-verifier2.md + receipts corpus/live/r89-verify2/. Commit nothing. Return: report path, verdict, blockers.
