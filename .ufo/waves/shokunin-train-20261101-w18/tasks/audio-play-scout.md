# r78 SEED SCOUT (audio) — the playback-side selection lattice

r77 pinned the CAPTURE-side law (stream.capture.sink fallback lattice,
target.object provenance trap, loss re-link). The WRITE side is
unmapped. With independent probes (own pw-cat/pw-play/paplay/aplay runs,
own scratch, DO NOT touch corpus/fixtures or tracked wavs): does sink
selection have the same fallback lattice (nonexistent sink -> default)?
Does target.object lie on the playback path too? Does removing the
target sink mid-playback re-link (playback-side sustained_after_loss)?
Where does aplay's device axis differ from arecord's? Measure, don't
infer. Report -> reports/round-78/r78-scout-playback.md.
