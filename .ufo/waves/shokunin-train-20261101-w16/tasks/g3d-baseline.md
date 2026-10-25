# r85 BASELINE (g3d) — freeze + post-commit zero-drift

Read SHARED.md. Two-phase:
1. PRE-COMMIT: freeze the r84-closed tree (`ac025b2` head): archive the
   fixture + full replay (godot 188/188 + bpy + three.js suites) into
   corpus/live/r85-baseline/freeze/; record the normalized prior-186
   prefix sha and the two r84 rows.
2. POST-COMMIT: watch git log for the author commit; when it lands,
   re-run everything on the committed tree; verify prior rows
   byte-identical, new rows appended (insertion-only), seed digests
   unchanged.
Report both phases -> reports/round-85/r85-baseline.md. If the author
commit has not landed by your deadline, file phase-1 with the freeze
receipts and note the pending phase.
