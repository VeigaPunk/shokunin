# r86 BOUNDARY (g3d) — exec-capable probe seat
Read reports/round-86/r86-scout.md + round-85 seats first. Do NOT edit
tracked files (author races). Probes in corpus/live/r86-boundary/.
- Attack the script-size fragility: exact line-count boundary for the
  dss fetch refusal under each backend — does a 1-line shrink flip the
  landed jolt_threaded child to dss-null?
- Deferred-coroutine hang: which await shapes hang vs error
  (process_frame under threaded, physics_frame chains, signal awaits)?
  Which leave zombie RIDs (leak scan should catch)?
- Dummy floor: does anything on Dummy EVER refuse loudly? map
  server-call -> {silent-empty, error, hang} exhaustively on ~12 calls.
- Backend tier edges: direct_space_state vs server state under each;
  do Dummy writes ERROR or vanish?
- Threaded child: allow_inaccessible whitelist is by-text — can a
  DIFFERENT error sneak under the same text? (mutation probe)
Report reports/round-86/r86-boundary.md + corpus/live/r86-boundary/.
