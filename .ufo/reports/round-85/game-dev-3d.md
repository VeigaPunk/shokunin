# fleet report — game-dev-3d r85 (w16)

- Work `f230443` + folds `4e6fbe3` + report-last `3d42f77`: ADMIT-corr.
- Cells: jolt_threaded (threading-invariant at map+constant),
  dummy_refused (Dummy unexpected x5 — backend-determined),
  srv_phase_delta (server-write tier). 188 -> 191 cases.
- Recovery: first author died mid-landing rate-limited with a
  parse-broken diff; boundary caught v1 DOA; deepseek completion seat
  landed it. Wave-B ran all deepseek-flash.
- Evidence: 191/191 x4 executions identical tuple sha; prior 188
  identical positions + stdout/stderr byte-identical; mutations 6/6.
- Recorded: jt_threaded self-report caveat; dummy_class misnamed
  (deferred); jolt_threaded child.log not byte-stable (map-only).
