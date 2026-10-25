# r77 AUTHOR (audio) — source-selection + fallback law + reader matrix

Read SHARED.md + reports/round-77/r77-scout.md (frontier PRE-MEASURED:
fallback law, sustained_after_target_loss, split-sentinel rename,
reader matrix) + r76 adjudicator. Insertion-only on
corpus/fixtures/measure_audio.py (--probe-<name>-r77, prior rows
untouched; keep the r76 folds' guards — data_actual_zero, leg-totality,
named-busy carve-outs).

ARM candidates (pin the scout's measurements):
- sink-fallback lattice: -P stream.capture.sink=true with
  {sink-name honored, source-name/default/pulse/garbage -> silent
  fallback to default-sink monitor}; content witness + pw-link -l are
  the discriminators (pw-dump target.object LIES); without the prop,
  sink/monitor/auto names -> 44-byte finalized empty WAV.
- sustained_after_target_loss: unload the captured sink mid-run ->
  capture continues at 100% rate, rc=1, finalized, byte-identical to
  no-event baseline. Name the class.
- device-dependent TERM: arecord TERM on sysdefault ->
  placeholder_80000000 + alsa_read_eintr (vs hw:* finalize) — pin the
  per-route partition.
- split-sentinel: unbounded-ish -D null hits the 2 GiB sentinel ->
  file RENAMED <name>-01.wav — byte-cap the leg hard (the scout
  flooded 36 GB once; your cells must use -d/-s + tmpfs guards).
- reader matrix on KILL wounds: {stdlib wave, ffprobe, soxi, sndfile-info}
  — sndfile-info honest; soxi lies 12173.9s on a 2.375s wound; wave
  rejects. Pin per-reader per-wound.
- format axis: pw-record --format/--rate/--channels legality
  (refusals leave NO file, --help dump; --channels 6 -> EXTENSIBLE).
Byte-cap every leg; rotation dirs bounded. Report ->
reports/round-77/r77-author.md.
