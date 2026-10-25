# kaika steer table — orchestrator, 2026-10-19

Rule: a lane with a declared-but-unlanded round is steered to that round (finish or close it
honestly; its declared claims come first). Otherwise the round is the lane's own counter + 1,
taking the maximum across the lane `LOG.md` / `SCORECARD.md` / reports and the fleet
`MANIFEST.json` (W1 STATE dossier §1 of each lane). Every steered report path
`.ufo/reports/round-<N>/<lane>.md` was checked free in the fleet root on 2026-10-19 before
dispatch. Lanes whose open round is the 2026-10-15 fleet-2 relaunch continuation are steered to
`1` — the relaunch namespace itself is open L0 (`.ufo/l0-questions.md`, relaunch cluster) and
this table does not settle it.

| lane | round | basis (W1 STATE dossier) | note |
|---|---|---|---|
| audio | 101 | reports reach 100, the maximum counter | rounds 87–100 are unlogged in LOG/SCORECARD (87/88 verifier GATE FAIL) |
| chousa | 24 | `SCORECARD.md:1221` pre-registers r24; dispatched, unlanded | this round IS r24 |
| game-dev-2d | 105 | 104 + 1 | r104 adjudicator routes work to r105 |
| game-dev-3d | 108 | r107 aborted (`7c4e589`) consumed 107 | `reports/round-107/` is untracked in the main checkout — not this round's |
| kagi | 21 | max label 20 (blocked, increment 0) + 1 | HEAD `aea7a43` landed an unpinned `--dotenv-bytes` arm |
| kaidoku | 12 | arc3-loop1-round12 halted with frozen claims | finish exactly as frozen (`claims-frozen.md`) |
| kake | 20 | unadmitted r20; `LOG.md:542` says a fresh session resumes it | this round IS the r20 resume |
| kama | 10 | `.ufo/round-10/plan.json` never dispatched | plan files are untracked in the main checkout; read them read-only |
| kasegi | 22 | r21 blocked with zero credit consumed 21 | |
| kengaku | 24 | r23 executed but unadmitted | record r23 honestly; the operator stop covered the earlier 10-round goal |
| kotoba | 46 | r46 WIP committed (`36ab0d3`), no report or ledger row | land r46 if its claims verify on re-measurement, else close it honestly |
| kotodama | 49 | r49 declared FRESH (`reports/round-49/claims.json`), dispatch-blocked | honor the declared claims |
| kumitate | 34 | round-33 continuation record names r34 | |
| lore | 103 | 102 + 1 | |
| mado | 12 | last admitted 11; 2026-10-15 fleet round-1 blocked, never admitted | set `MADO_VERIFY_HARNESS` explicitly in the worktree |
| mori | 12 | lane LOG and MANIFEST agree on 11 | the driver's counter (2) is stale |
| revenger | 1 | fleet round-1 continuation blocked (`MISSING_BINDING`) | lane handoff at the lane's `.ufo/reports/round-1/revenger.md` |
| souji | 12 | r11 failed (cert withheld) | the operator cancelled the 12-round goal after r11; this round runs under the current directive |
| tabi | 1 | fleet round-1 continuation | record or retire the unrecorded `user-20261015-r07` wave first |
| tameshi | 1 | fleet round-1 continuation blocked at dispatch | |
| tsukuroi | 1 | fleet round-1 continuation blocked (route binding) | |
| protocol | 16 | r15 has a report and SCORECARD row; ledger row 15 in-flight | repairs the root-ledger clobber and registry home |
| aggregator | — | counter 10, report 11, ledger row 12 in-flight | steered after lane rounds land |
