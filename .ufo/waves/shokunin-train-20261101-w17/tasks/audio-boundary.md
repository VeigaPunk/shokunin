# r77 BOUNDARY (audio) — attack capture assumption edges
Read SHARED.md + r77-scout + r76-critic. Live probes only, byte-capped.
- Fallback law edges: does -P stream.capture.sink=true + --target
  <monitor-node-name> (not sink) bind or fall back? Does a MOVED
  stream follow (pactl move-source-output) or rebind? Multiple -P props?
- sustained_after_target_loss: is the surviving stream zombie-paced?
  KILL the provider hard (not module unload) — same class?
- split-sentinel: does -01.wav accumulate forever or stop at NN? Does
  the sentinel exist on pw-record too (it uses libsndfile, not arecord)?
- reader matrix gaps: mediainfo? ffplay? python soundfile? Does soxi
  -s vs -D differ on the same wound? What does players do (does the
  inflated arecord header PLAY 3h of silence)?
- format axis: legal-but-weird combos (--rate 8000 --channels 1 on a
  stereo source — resample truthfully or garbage?), 24-bit roundtrip.
- Roundtrip under contention: capture monitor while ANOTHER capture
  holds the source.
Report -> reports/round-77/r77-boundary.md + corpus/live/r77-boundary/.
