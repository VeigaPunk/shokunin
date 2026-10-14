# r77 AUTHOR (g2d) — release/callback-swap/drain-EC legality

Read SHARED.md + reports/round-77/r77-scout.md (the frontier is
PRE-MEASURED — your cells pin what the scout found) + r76 adjudicator.

ARM — love_battery.py + love_phys_probe/main.lua, insertion-only
(prior 49 cells byte-identical; fatal cells stay LAST):
- bc_worldrelease cells: world:release() inside a callback → SIGSEGV
  rc=-11, done=false, witness line = last emit before death; scout
  measured all 5 channels (bc/pre/post/ec-natural/ec-drain). Class:
  corrupt/died variant — decide honestly (rc=-11 vs rc=1 died). Must
  stay at the fatal tail + never run before other cells' witnesses.
- setcallbacks mid-dispatch cells: swap effective for later
  channels/contacts same-step; swapped-out table never fires again;
  nil-nil-nil-nil mutes surface (rc=0, physics untouched).
- fixture_destroy cell: Fixture:destroy in-cb = deferred-family but the
  tracked deferred gate is fixture-blind (scout: fcount unchanged,
  drain EC at locked=false, tunneling effect) — arm a fixture-scoped
  witness (fx_b_dead sibling) rather than forcing the body gate.
- drain-EC legality cells (boundary predictions now measured by scout):
  write inside drain EC = applied; destroy() inside drain EC =
  IMMEDIATE not deferred; abort inside drain EC = distinct signature
  (locked_after=false, no collateral refusal; same contact's EC
  re-fires at locked=true next step; DestroyBody retries one late).
- coroutine ladder: coroutine.resume around the mutation = new
  containment level (error returned, run survives, transient lock +
  collateral refusal) — sits between wrap (fatal) and pcall (wp).
- setmeter cell: love.physics.setMeter in-cb = applied (module global);
  pin the RATIO witness (pos doubles), not the trajectory.
Classifier: extend iw_classify only where measured classes require;
fatal/corrupt rows last; rc persisted; keep every gate fail-closed.
Report -> reports/round-77/r77-author.md.
