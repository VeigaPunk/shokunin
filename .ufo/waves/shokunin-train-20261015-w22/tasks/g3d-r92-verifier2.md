# Seat: g3d r92 verifier-r2 — verify folded bytes 75739bc

Lane: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin
Verify the FOLDED tree (75739bc), not the author's original.

## What to verify
1. `r92_timing_steps` / timing rows — the verifier FAILED these pre-fold (`time_scale=10` leaked `delta=0.016667` under batching). Fold re-anchored E0/E1/E2 to mutation→process_frame→3 settled ticks. Run those arms 20+ times under hog load; every settled delta must be on-pin.
2. `r92_animphys` idlemode envelope — legal set x∈[0,3], y∈[1.8,2.0005]; run reps incl. starved scheduling if reachable.
3. SP1–SP5 deletions behaviorally inert — marker set unchanged except declared re-pins.
4. Full battery 258/258 on final bytes; run under load too.
5. r93-baseline F1/F2 (navagent 1-tick miss, size-gate granted-under-load) are PRE-FOLD observations on different rows — note if they still fire but they are not r92 defects.

## Deliverables
- reports/round-92/r92-verifier2.md — verdict + per-item evidence
- corpus/live/r92-verify2/ (gitignored; manifest + receipt shas in report)
- No tracked writes beyond report; kill hogs on exit.
