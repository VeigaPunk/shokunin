# r78 AUTHOR (g2d) — the nested-update damage surface

Read SHARED brief ../w17 SHARED.md + reports/round-78/r78-scout.md
(31 cells, all byte-stable, classes OFFERED not verdicts) + r77
adjudicator + r77-boundary §6 (the nested-update lock-clear).

ARM — love_battery.py + love_phys_probe/main.lua, insertion-only
(prior 75 cells byte-identical at positions; fatal cells stay LAST):
- nested lock-clear cells: inner world:update inside a callback clears
  e_locked -> setPosition APPLIES, destroy() executes IMMEDIATELY (not
  deferred). Pin both witnesses (pos_after + target_dead mid-callback).
- inner-drain ownership: the nested update runs its OWN epilogue drain
  while the outer callback is on the stack (drain_n>=1, inner_cb=true).
- depth-2 drain-EC: nested update from a BODY-drain EC -> SIGSEGV
  rc=-11 (fatal tail); the fixture-triggered drain EC variant is
  REFUSED (ok=false, Box2D lock assertion) — pin the partition.
- contacting-destroy escape: destroy a contacting object mid-nested-step
  -> dispatch escape class (scout §1.3); pcall does NOT contain a signal.
- zombie-contact handles: drain-EC use-after of an already-destroyed
  contact (z_drain_use_after / z_abort_use_after / z_touch_then_end).
- livelock/convergence: drain_n=3 converges; every-entry abort livelocks
  (drain_n=197=aborts) — pin both classes with bounded witnesses.
Classifier: extend iw_classify only where measured classes require;
keep every gate fail-closed; rc persisted; insertion-only.
Report -> reports/round-78/r78-author.md.
