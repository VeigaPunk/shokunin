# r77 BOUNDARY (g2d) — attack the release/swap surface

Read SHARED.md + r77-scout + r76-critic/boundary. EXEC-CAPABLE seat —
run live probes (the r76 boundary ran read-only; you have shell).
- release() in non-callback contexts the scout missed: inside
  love.update post-update, inside a timer, inside a pcall INSIDE the cb
  (contained release — still SIGSEGV?); release during drain EC.
- setCallbacks swap chains: A->B->A cycles; swap inside the swapped-in
  table's own callback; setCallbacks with partial nils mid-dispatch;
  swap then re-swap same step.
- Fixture:destroy on the LAST fixture of a body (body orphans?); on a
  fixture mid-contact vs idle; on sensor vs solid.
- drain-EC writes: setPosition at locked=false — applied where? does
  the moved body still contact-resolve in the same epilogue?
- coroutine edge: resume INSIDE a cb that yields across update; resume
  of a dead coroutine; nested pcall+resume mixes.
- Abort drain-EC twice consecutively: does the retry converge or loop?
Report -> reports/round-77/r77-boundary.md + corpus/live/r77-boundary/.
