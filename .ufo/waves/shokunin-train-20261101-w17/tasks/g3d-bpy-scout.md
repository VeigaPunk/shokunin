# BPX-SCOUT (g3d) — bpy + three.js surface frontier

Write corpus/live/bpx-scout/ + reports/round-86/bpx-scout.md ONLY —
do not touch phys3d_events.gd or run_battery.py (r85 wave-B is
verifying them concurrently); bpy_battery.py + three/ are free.

Recon, measured where cheap:
- bpy_battery.py: 83 cases — class/axis coverage map; when last
  advanced; which classes (refused/deferred/ignored/anomaly analogs)
  exist there vs the godot lattice.
- bpy_sync_probe.py: what does it do, what runtime does it need
  (blender on PATH? bpy pip module?), can it run bounded here?
- three/: the three.js battery — 31 cases — structure, runner,
  coverage classes; node version pinned?
- Cross-pollination candidates: which phys3d findings (write-phase
  deltas, query refusals, backend identity) have bpy/three analogs
  worth arming (e.g., bpy ops-context errors = a refused class;
  three.js raycast against disposed geometry)?
- Blender version + bpy availability check (bounded, timeout-guarded).
Deliver: coverage matrix + ranked frontier list for g3d r87-r90.
