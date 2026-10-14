# r76 BOUNDARY (g2d) — hazard extension + adversarial edges

Read SHARED.md + r75 boundary/critic first. Extend the hazard lattice:
- drain-deferral hazard VARIANTS: throw-after-queue at each callback
  channel (bc/pre/post/ec); throw BEFORE the queue; queue-then-throw
  ordering; does the missed drain ever catch up or is it permanent?
- destroy edges: destroy during endContact (the ec channel's own
  deferred witness), destroy of an already-drained body, newBody on a
  drained body's slot.
- SayGoodbye/drain observers: if any exist, measure their timing vs
  the locked=false boundary; if none, pin the inference ceiling.
- Containment lattice gaps the r75 critic flagged: `mode=unp` is
  self-declared — find any emit path where a contained mutant could
  still produce a passing unp receipt (probe the falsifiability).
Report -> reports/round-76/r76-boundary.md.
