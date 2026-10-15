# r87 BASELINE (g3d) — freeze + post-commit zero-drift

Phase 1 at CURRENT HEAD: archive tree, run godot battery (expect 195/195),
bpy battery (83/83), three.js (31/31); hash-seed all fixtures; record
prior-195 rows as reference. Honest about pre-existing dirty state.
Phase 2 when the r87 author commit lands: re-run all three; diff prior
rows at identical positions (stdout+stderr bytes); only declared
insertions may differ. Report -> reports/round-87/r87-baseline.md.
