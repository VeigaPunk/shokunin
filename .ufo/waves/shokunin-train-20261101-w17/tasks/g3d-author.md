# r86 AUTHOR (g3d) — threading-invariance ext + Dummy floor + hang class

Read ../SHARED.md-equivalent + reports/round-86/{r86-scout,nas-scout,bpx-scout}.md
+ reports/round-85/r85-adjudicator.md. Base: 3d42f77 (post-r85).

ARM — phys3d_events.gd + run_battery.py, insertion-only (prior 191 rows
byte-identical; the jolt_threaded child.log is NOT byte-stable — map
only):
- script-size ladder cell: the deferred process-context dss fetch is
  size-gated (released in (338,638] per r85-scout; 2D twin (308,508]).
  Arm a row proving the fetch succeeds at a padded-safe size and name
  the accident class (latent fixture fragility, not engine behavior).
- deferred-coroutine hang class: an await-dangling coroutine under
  threading hangs to timeout/rc137 — name the class (vs Dummy silent
  floor). Bound the child hard (timeout-s KILL).
- backend-write tier matrix ext: area gravity/damping overrides,
  query margins, separation rays under {GodotPhysics,Jolt,Dummy} —
  scout pre-measured differences; add 1-2 cells where classes split.
- Dummy silent-floor cell: dummy returns RID(0)/empty everywhere —
  pin the silent-floor signature as a class (vs refuse).
- OPTIONAL nav surface seed (nas-scout): set_velocity() silent no-op
  on agent node vs server RID deliver — one cell if clean.
Witness discipline: jt_threaded-style self-report needs a parent-side
or engine-level corroboration where one exists (dss class, refusal
counts); dummy_class NOTE key stays as-landed (pinned sha) — rename
deferred. Report -> reports/round-86/r86-author.md.
