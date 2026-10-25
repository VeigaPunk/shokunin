# r82 VERIFIER (g3d) — independent replay on the committed tree

Read SHARED.md + the r82 author brief.

Poll until the author commit lands (it may be operator-committed under a different seat). Replay the full battery/arm on HEAD, run it twice for determinism, byte-compare the prior-rows receipt vs the newest committed run, AGREE/DISAGREE per claim item with evidence. If your replay's head moved since the author commit (report-last folds), verify the delta is comment/report-only.
Report -> reports/round-82/r82-verifier.md.
