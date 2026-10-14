# r74 REVIEWER (audio) — correctness review of the landed diff

Read SHARED.md + the r74 author brief.

Poll the worktree/HEAD until the author commit lands, then review: defect class (correctness bugs, broken guards, unstable receipts, claim-vs-implementation drift), reproduction, severity. Replay the battery/arm yourself on the committed tree — never trust the author's numbers alone. Flag any touched prior bytes.
Report -> reports/round-74/r74-reviewer.md.
