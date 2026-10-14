# w17 closeout — audio r77 + g2d r77 wave-A/B, g3d r85 wave-B

## Verdicts
- audio r77: ADMIT-corr — 65790f1 work, 1a84ca7 fold, 731937c report-last.
  Capture-source lattice + fallback law armed; 4-seat consensus defect
  (exclusivity guard) + N2 wall-leg vacuity + F5 RSS + sink_gone vacuity
  all folded; r76 regression classified host-state via prefold A/B.
- g2d r77: ADMIT-corr — 62201e5 work, d48e0fd fold, d4aaa95 report-last.
  26 cells/6 classes; critic D2/D3 gate defects folded; simplifier P3
  67-pin dedup byte-identical. (Scribe later found D2 fold inert —
  tested a key parse_iw never emits; the r78 author diff carries the
  discriminating fix. Recorded in r78 scribe report.)
- g3d r85: ADMIT-corr — f230443/4e6fbe3/3d42f77. Threading-invariance,
  Dummy control, server-write tier; F1/F3 + boundary regex folded.

## Cross-seat receipts
- audio: wave-B 5/5 landed (critic/reviewer/verifier/simplifier/baseline
  + scribe). 12 live seats peak.
- g3d: wave-B 4/4 + boundary; simplifier SP1/SP2 proven.
- g2d: wave-B 4/4; scribe caught missing r76-boundary report on disk
  (reconstructed with provenance note) + byte-count corrections.
