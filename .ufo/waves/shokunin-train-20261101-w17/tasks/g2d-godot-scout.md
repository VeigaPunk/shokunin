# GODOT-SCOUT (g2d) — under-exercised surface inventory

Write corpus/live/gd-scout/ + reports/round-77/gd-scout.md ONLY —
do not touch any tracked fixture; run_battery.py + the *.gd fixtures
are stable territory (LOVE battery is where the live round is).

Recon, measured where cheap:
- run_battery.py structure: how many godot cells exist, when last
  touched (git log), which classes they exercise vs the love/pygame
  batteries' class coverage — where is the lattice thinnest?
- godot-2d surface gaps vs what the love lane has proven: contact
  callbacks, deferred writes, abort classes, teardown semantics —
  which of the r71-r77 LOVE findings have NO godot-2d counterpart
  cell? (Godot 2D physics runs the same server-threaded engine as
  g3d's — cross-pollination with the g3d r85 jolt/dummy lattice is the
  cheapest new frontier.)
- A quick smoke: run run_battery.py once, record totals; probe 2-3
  cells' outputs to see pin structure. Check godot binary version.
- pygame surface same question: pygame_battery.py structure, last
  touched, coverage class map vs love classes.
Deliver: coverage-gap matrix + ranked next-frontier candidates for
r78-r80 (godot-2d deferred-write lattice? pygame audio sub-helpers?
physics_server_2d analogs of the g3d arms?) with measured support.
