# audio-r89-fold — correct r89 co-tenancy arms (queued BEHIND r87+r88 fold custody)

Runs ONLY after the r87+r88 fold commits. Target measure_audio.py pwprof block from ec5228ff.

Defects (critic ec5228ff, verifier-pending):
1. g_hup: child inherits launcher SIGHUP SIG_IGN — restore_signals() doesn't cover HUP. Fix: add SIGHUP to the restore mask (verifier's corrected launcher already proven: 3/3 replays green).
2. x_foot: client-census bracket race, 17.6% natural fail rate — client half AND node half both sampled transiently. Fix: retry/ownership-filter or coverage_blocked instead of hard equality.

Preserve all encoded laws (254/254 mutation evals pass; 52 leg deletions all crash loud — do NOT touch the law layer). Fixed-path lock stays. After fix: run pwprof family twice green, then report reports/round-89/r89-fold.md. Commit nothing.
Return: report path, green-run shas, blockers.

Reviewer (f1) addition: fix = reset armed signals to SIG_DFL in child process_setup (covers SIGHUP+any launcher-ignored signal). Also F2: x_top must reject `status R, quant 0, 0.0us` refresh rows (0/0 row is not a measurement — treat as coverage_blocked or sample-again).

Verifier (1484-cell census) specifics: x_top needs real-value guard + same-window band (0.0us/0.0us refresh rows exist solo too, busy ratio 0.203). x_foot must measure OWN footprint (r89a_ namespace), not global client/node census. g_hup A/B proven: HUP=SIG_DFL→rc-1 x3, SIG_IGN→rc-9 x3. Also fix leg-count arithmetic: 52 legs (27/12/4/9), report said 47.
