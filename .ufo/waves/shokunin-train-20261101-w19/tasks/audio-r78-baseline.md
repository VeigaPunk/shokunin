# r78 BASELINE (audio) — freeze + post-commit zero-drift

Phase 1 at CURRENT HEAD (post-731937c): archive tree, run the capture
battery probes (r76+r77 entries) — NOTE: the host topology changed
(DualSense is default source) so r76's parec_no_device + arecord
legs FAIL environmentally — record them as the environmental set, not
drift; hash all fixtures incl. __pycache__; record the r77 receipt as
reference. Phase 2 when the r78 arm lands: re-run r76+r77; prior
cells must be byte-stable modulo the SAME named environmental set +
declared contention classes. Report -> reports/round-78/r78-baseline.md.
