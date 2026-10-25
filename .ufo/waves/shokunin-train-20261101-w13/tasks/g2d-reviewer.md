# r73 REVIEWER (g2d) — correctness review of the landed diff

Read SHARED.md + the r73 author brief.

Poll the worktree/HEAD until the author commit lands, then review: defect class (correctness bugs, broken guards, unstable receipts, claim-vs-implementation drift), reproduction, severity. Replay the battery/arm yourself on the committed tree — never trust the author's numbers alone. Flag any touched prior bytes.
Report -> reports/round-73/r73-reviewer.md.
