# GST-SCOUT (audio) — NEW RUNTIME: GStreamer capture/playback surface

Write corpus/live/gst-scout/ + reports/round-77/gst-scout.md ONLY.
gst-launch-1.0 + gst-inspect-1.0 are on PATH (1.x). python-gi absent —
use CLI tools only. BYTE-CAP every pipeline (timeout + num-buffers).

Map, measured not read:
- inventory: which source/sink plugins exist on this host
  (pulsesrc/sink, pipewiresrc/sink, alsasrc/sink, autoaudiosrc/sink,
  filesrc/sink + parsing/wavparse/wavenc families) — gst-inspect counts.
- capture lattice: pipewiresrc vs pulsesrc vs alsasrc viability;
  audiotestsrc->filesink is the known-good loop control; does
  pipewiresrc->wavenc->filesink capture a real monitor? (compare with
  the pw-record lattice — same PipeWire substrate, different client).
- sever classes: TERM vs KILL on a running gst pipeline — does the
  wavenc finalize (GST handles SIGINT via own handler; SIGTERM too?) —
  compare the pw-record/parec/arecord wound taxonomy. num-buffers cap
  vs timeout cap vs byte cap (which bounds are honest?).
- reader disagreement port: does the same KILL-wound file confuse
  ffprobe/soxi the same way? (cross-consumer wound-matrix row).
- format/property axis: audiotestsrc wave types/freqs; wav vs flac
  encoders; buffer-time/latency knobs on pulse/alsa sources.
- Prior-art axis: gst-launch error classes (could not link, no
  element, state-change failures) — named refusal taxonomy vs the
  pw/pulse/alsa ones.
Deliver a coverage proposal: the smallest gst fixture probe
(--probe-gst-rNN) worth adding to measure_audio.py, with measured
evidence for every claim, byte caps baked in, and named
contention/host-state caveats.
