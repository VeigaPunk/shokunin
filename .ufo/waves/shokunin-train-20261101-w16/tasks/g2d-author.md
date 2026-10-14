# r76 AUTHOR (g2d) — drain-observer cells + destroy edges

Read SHARED.md + r75 author/adjudicator/critic/boundary first. The
boundary's drain-deferral hazard is the ordered frontier.

ARM — `love_battery.py` + `love_phys_probe/` extension (insertion-only;
all 44 prior cases byte-identical; fatal cells still last):
- drain-deferral hazard cell (r75 boundary): an accepted queued destroy
  PLUS an uncontained throw inside the same callback — the queued
  destroy's epilogue drain is skipped (drains one step late). Arm the
  measured class honestly (it may be `anomaly`-shaped today; if it
  earns a real class, name it).
- `world:destroy()` inside a callback + double-`destroy()` on the same
  body (in-callback then post-update). Pin whatever lands.
- SayGoodbye-instrumented drain observer (stretch): if LOVE 11.5
  exposes `world:setCallbacks`-adjacent joint/fixture destroy
  notification or a per-contact drain event, arm a witness that makes
  the joint drain *point* observed rather than inferred (closes the
  r75-critic F3 residual). If nothing exists, record blocked honestly.
- per-contact `preSolve return false` variant (stretch): return false
  for ONE contact of a multi-contact pair — pin whether the impulse
  mask is contact-scoped or pair-scoped.
Report -> reports/round-76/r76-author.md.
