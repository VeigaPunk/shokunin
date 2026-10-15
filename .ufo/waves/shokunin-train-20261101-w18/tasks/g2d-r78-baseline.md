# r78 BASELINE (g2d) — freeze + post-commit zero-drift

Phase 1 at CURRENT HEAD: archive the tree, run love battery (expect
75/75) + pygame battery (80/80), hash-seed all fixtures, record prior
rows as the reference. Report any pre-existing dirty state honestly —
do NOT clean it yourself.
Phase 2 when the r78 author commit lands (watch for it): re-run both
batteries; diff all 75 prior rows at identical positions (stdout+stderr);
exactly the declared inserted rows may differ; every other delta is
undeclared drift. Report -> reports/round-78/r78-baseline.md.
