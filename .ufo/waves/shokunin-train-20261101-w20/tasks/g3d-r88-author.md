# r88 AUTHOR (g3d) — PhysicsDirectSpaceState3D read family + body inertia getters

Arm the r88 scout's measured lattice: reports/round-88/r88-scout.md +
receipts corpus/live/r88-scout/ (driver.py, probes/*.gd, runs/* — 980
receipt files). Repo: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin.
Fixture convention: extend corpus/fixtures/phys3d_events.gd with new arms
OR add a sibling fixture (e.g. phys3d_query.gd) — keep CASES appends
insertion-only at the tail of corpus/fixtures/run_battery.py (the crash
row must remain last-or-later-than-it; crash-class rows go at the tail).

Arm cells (prioritize; each needs whole-dict verdict pins + fail-closed
gates + the allow_lines/count convention from r87):
1. cast_motion motion-honored vs collide_shape/get_rest_info/intersect_shape
   motion-ignored (same params object, same geometry) — THE semantic split.
2. Fetch-gate lattice: threaded refuses at every out-of-phase position
   (init + _process) with 3 errors; non-threaded hands out everywhere;
   Dummy floor. bds.get_space_state() BYPASS on threaded F position.
3. Inactive-space: space_create+active(false) fetch succeeds non-threaded
   at every position, refused threaded F; stashed handle answers either way.
4. Threaded race classes as NAMED non-deterministic classes (never pin a
   distribution — pin "answer-or-empty envelope", and the Jolt rc=134
   abort as a crash-class row with the envelope-provenance convention
   the r87 fold added: breadcrumb prefix + crash line + no marker).
5. Param-object purity: no read method mutates params; shape_rid beats
   shape; fresh containers each call (same_object=false, byte-equal).
6. Body inertia getters: rigid box values; static/kinematic split
   (GP zeros vs Jolt nonzero placeholders vs Dummy floor);
   BODY_PARAM_INERTIA write reflected; tensor is world-space R·diag·Rᵀ.
7. Wrong-args class: wrong param types/null => typed empties rc=0,
   wrapper-layer error text identical across backends.
8. Freed-space postconditions PER METHOD x BACKEND: GP all-134; Jolt
   shape-channel 134 + pt/ray process-sensitive (pin as crash-class or
   dead-handle class honestly — the scout saw BOTH across reps, so gate
   on "134 or dead-handle typed-empty" with rc+result conjuncts, never a
   single mode as law); Dummy typed empties rc=0.
9. Backend-geometry splits: boundary-touch pt counts, cast_motion bracket
   asymmetry GP vs Jolt, rest_info normal split — pin envelopes, never
   cross-backend equality.
Rules: whole-dict verdict compares; every engine-line claim log-counted;
host/version bound in README; no marker without a real witness; the
spawned-child and allow_lines conventions from r86/r87 apply. Run the
full battery at least twice after landing; prior 201 rows must stay
byte-identical. Reports -> reports/round-88/r88-author.md. Do NOT touch
reports/round-87 or commit — leave the tree dirty for the fold pass.
