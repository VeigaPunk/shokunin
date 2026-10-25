# r76 BASELINE (g2d) — freeze + post-commit zero-drift

Read SHARED.md. Two-phase:
1. PRE-COMMIT: freeze the r75-closed tree (`ddd455b` head): archive the
   fixture + a full battery replay (love 44/44 + pygame 80/80) into
   corpus/live/r76-baseline/freeze/; record per-cell receipt shas.
2. POST-COMMIT: watch git log for the author commit; when it lands,
   re-run the full battery on the committed tree; verify prior rows
   byte-identical and new rows appended at end (insertion-only);
   byte-compare all receipts vs the freeze.
Report both phases -> reports/round-76/r76-baseline.md. If the author
commit has not landed by your deadline, file phase-1 with the freeze
receipts and note the pending phase.
