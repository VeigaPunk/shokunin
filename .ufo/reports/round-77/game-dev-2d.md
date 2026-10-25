# fleet report — game-dev-2d r77 (w17)

- Work `62201e5` + folds `d48e0fd` + report-last `d4aaa95`: ADMIT-corr.
- 26 cells, 6 new classes: corrupt (rc=-11, release-in-engine), swapped,
  muted, drain_abort, yield_abort, immediate; drain-EC legality pinned
  (lock-state rule); resume=containment, wrap=not.
- Evidence: 75/75 across six executions; verifier AGREE 5/5; baseline
  zero-drift; 43/43 ablations fail (2 harness-degenerate rows recorded).
- Folds: 67-pin dedup; postfire-absence + absent-key fail-closed gates.
- New hazards for r78: nested-update lock-clear (lock cleared -> writes
  apply), drain-EC livelock, zombie contact UAF — scout pre-measured.
