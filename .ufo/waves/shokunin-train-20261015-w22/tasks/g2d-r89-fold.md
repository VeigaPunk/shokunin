# g2d-r89-fold — apply correction queue

Custody free (r90 author landed ee20575). Apply to game-dev-2d-shokunin:

1. Simplifier f535ddb: remove the `names` dead accumulator (−2 lines), report corpus/live dir has the patch — verify byte-identical battery first.
2. Critic F1 (68756af): geo2d_lattice_lineempty is crash-cause-blind (merged stdout+stderr; foreign SIGABRT classifies PASS). Add a stderr-fragment pin for the expected Clipper2 assert text.
3. Critic F5: delete dead arms bridge_hole/bridge_hole2 + fix the falsified comment.
4. Reviewer findings (61355e2): custody items A-list where they touch armed rows.

Rerun full battery twice on final bytes (tolerate only documented flake classes). Commit nothing; report reports/round-89/r89-fold.md + receipts corpus/live/r89-fold/. Return: report path, diffstat, battery verdicts, blockers.
