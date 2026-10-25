# r87 AUTHOR (g3d) — the body-tier deferred-state lattice

Read reports/round-87/r87-scout-dss.md (the body_get_direct_state tier,
PRE-MEASURED: singleton live handle, gate-controls-acquisition-not-use,
out-of-phase held-handle writes land, step-stamped getters, contact
buffer last-step, Jolt/GP/Dummy splits, freed-space intersect_ray crash)
+ r86 adjudicator + bpx-scout.md/nas-scout.md for cross-runtime seeds.

ARM — phys3d_events.gd + run_battery.py insertion-only (prior 195 rows
byte-identical at positions; new cells appended):
- held-handle cell: body_get_direct_state object == the _integrate_forces
  handle AND survives detach/reattach (identity law).
- acquisition-vs-use split: fetch refused out-of-phase under threading,
  but a HELD handle reads live + writes land at every position incl.
  _process (the gate controls acquisition, not use).
- step-stamped getters cell: get_step/get_total_gravity/damp are
  step-stamped (init constants pre-first-solve); contact buffer is
  last-step data; needs max_contacts_reported>0.
- write-loss race cell: out-of-phase held-handle write measured lost
  (sleeping=false vs true across reps) — pin as a race class honestly
  (may be flaky — use a bounded repeated-observation form).
- backend split at body tier: Jolt real get_contact_impulse vs GP zeros;
  contact_local_shape -1 vs 0; set_sleep_state zeroes velocity on Jolt.
- freed-space crash: intersect_ray via space-state of a freed space —
  SIGSEGV on GodotPhysics, std::system_error abort on Jolt, {} on Dummy.
  Pin per-backend (crash class rows go in the fatal tail).
Keep every gate fail-closed; run full battery + bpy/three.js siblings.
Report -> reports/round-87/r87-author.md.
