# Wave-14 closeout — consumer-class breadth + physics-server interiors

Closed 2026-10-14 ~17:30Z. Recovery wave: the first seat generation
(dispatched 16:10Z) died with its parent session; all landed work is the
16:20Z+ respawn generation whose IDs are recorded under
`recovery_dispatch` in registry.json. Lane pushes held per operator
policy; remote state is not claimed.

| lane | round | verdict | commits | headline |
|---|---|---|---|---|
| audio | r75 | ADMIT-corr | `db46fba`+`5f60747`+`2250be9` | 3 playback consumers (paplay pacat/libpulse, aplay in-process ALSA, ffplay lavf pull-model) on 9×4 matrix — 27/27 transport-invariant verdict groups; kill-class partition {-15, -9, 123}; non-transfers pinned (pw-cat .snd axis absent on paplay, mpv seek fork absent on ffplay, aplay raw-accept); 4 falsifications folded (term1 scope, vacuity guard, -ss silent-abort, dead tail anchor) |
| g2d | r74 | ADMIT-corr | `ae6cb16`+`35dcbf7`+`b2b20f2` | LOVE/Box2D interior-write lattice {refused×7, deferred×3, applied×5, fatal(lua)×2, captured×1}; re-entrancy defeats IsLocked; fatal classes split (fatal(lua) vs uncontainable SIGABRT→died); containment-level relativity recorded → r75 |
| g3d | r83 | ADMIT-corr | `e9145d9`+`4c1c100`+`c4b2fa2` | PhysicsServer3D two-tier lattice armed: queries edge-0 vs generated events tick-bound; write-phase dependency (delta=1 physics / delta=2 process); `static_nopair` GodotPhysics-scoped (Jolt inverts it); ST refusal = deterministic context gate (12/12 in-physics), not a race; threaded child timeout folded |

## Cross-wave observations

- Second consecutive wave where a carried guard needed narrowing
  (w13 pw-cat TERM-immune → r75 renamed `alive_after_term1`; r74 LOVE
  fifo-open not TERM-immune). Pattern: propagated claims decay at
  runtime boundaries — keep falsifiers armed per consumer/engine.
- Both physics lanes hit backend/partition falsifications of the
  *brief's* premise (g2d containment relativity; g3d partition by event
  kind + write-phase deltas) — the scout premise-check pattern is
  paying off; keep scouts on the falsify-the-frame axis.

## Wave-15 dispatched next (overlapped per swarm mandate)
audio r76, g2d r75, g3d r84 — frontier seeds in lane LOG/SCORECARD and
this wave's critic/boundary deferrals.
