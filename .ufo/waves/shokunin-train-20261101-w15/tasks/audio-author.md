# r76 AUTHOR (audio) — capture-side consumers: record direction

Read SHARED.md + r75 author/adjudicator/critic first. The corpus has only
PLAYBACK consumers — this arm adds the CAPTURE direction.

ARM — `--probe-capture-r76` (new ledger family, same ledger idiom):
capture consumers on a bounded record operation:
- `pw-record` (PipeWire native capture)
- `parec`/`parecord` (pacat capture path — PulseAudio-compat)
- `arecord` (ALSA direct — `-D` device axis; scout reports card/source
  inventory)
- `ffmpeg` capture (`-f pulse -i default` / `-f alsa -i <dev>` — second
  lavf leg in the capture direction)
Gates first: enumerate sources (`pactl list sources short`,
`pw-link -o`, `arecord -l`); absent source/device -> honest `blocked`
verdict with the exact enumeration recorded — never fabricate audio.

Cells (falsifiable partition):
- source-presence gate per consumer (named failure vs inferred).
- bounded capture: `-t`/duration/byte cap honored per consumer;
  captured bytes land with a parseable header (or the consumer's own
  format leg).
- sever classes: SIGTERM / SIGKILL mid-capture -> does the consumer
  finalize the header (usable partial wav) or truncate mid-write?
  Per-consumer class pinned; `timeout -s KILL` is the outer bound.
- output name axis: extension-driven format choice vs explicit flags
  (`.wav` vs `.raw` vs `-t wav`).
- roundtrip cell (stretch): where a monitor/loopback source exists,
  capture a played member and feed captured bytes back through an
  existing detect leg — do captured bytes land in the same verdict
  class as their source member?
All record arms bounded (SIGTERM then `timeout -s KILL`). Insertion-only;
prior rows byte-identical. Report -> reports/round-76/r76-author.md.
