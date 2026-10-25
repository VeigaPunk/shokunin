# r76 SCOUT (g2d) — drain/destroy surface map

Read SHARED.md + r75 reports first. Pre-measure the r76 frontier so the
author doesn't guess:
- the drain-deferral hazard: queued destroy + uncontained throw in one
  callback — when does the queued destroy actually drain? (one step
  late? never? next callback?) Receipt-level measurement.
- `world:destroy()` in-callback: does it refuse, defer, abort, or
  corrupt? Double-destroy: second call's class (refused? no-op?
  "attempt to use destroyed")?
- SayGoodbye instrumentability: what drain-time observers exist in
  LOVE 11.5 (World callbacks, Fixture/Joint isDestroyed after
  destruction, contact:endContact on destroyed fixtures)? Enumerate.
- per-contact return-false granularity: does preSolve's return apply
  per-contact or per-pair in a multi-contact frame?
- Scan for any other unarmed Box2D callback-write surface (fixture
  create/destroy inside cb, raycast/body enumeration inside cb).
Report -> reports/round-76/r76-scout.md.
