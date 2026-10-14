# r74 AUTHOR (g2d) — LOVE physics interior-write lattice

Read SHARED.md + frontier ports/frontier/fb-lovephysics.md + r73 author report.

ARM — fold the pre-measured love.physics frontier into the tracked
battery: writes inside Box2D callbacks (beginContact/preSolve/postSolve)
are gated per class — {refused | deferred | fatal} is the falsifiable
partition. Extend corpus/fixtures/love_battery.py (or the love probe
fixture, whichever carries the r70 splice cells):
- in-step mutation cells: setPosition/newBody/destroy inside
  beginContact — pin each class's actual gating (the frontier measured
  in_step=true + per-callback channel-split snapshots, byte-identical
  determinism x7)
- interior vs exterior write contrast cells (the same mutation outside
  the callback = control)
- contact-mask / active-body availability edges
Order interior-write cells LAST (a fatal crash kills the probe early —
frontier note); pin partial-capture detection so a crash mid-arm is a
measured FAIL not a silent truncated receipt.
Viability: love2d on host (r70 established). Box2D debug-vs-release
assert behavior is build-dependent — record which this build is.
pygame battery untouched = control. Report -> reports/round-74/r74-author.md.
