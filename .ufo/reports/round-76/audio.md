# Fleet report — audio round 76 (wave-15)

Lane: `audio-shokunin` | Round: 76 | Wave `shokunin-train-20261101-w15`
Verdict: **ADMIT-corr** (Sol) — `d566a31` (work) + `18deef6` (folds) + `b0b5d4d` (report-last)

## Move

The RECORD direction the corpus lacked: six capture entries
(gate/bounded/sever/name-axis/device-axis/roundtrip) over pw-record,
parecord, arecord, ffmpeg-capture — +1150/−3 insertion-only.

## Landed

- Per-consumer **sever wound partition**, byte-level: pw-record/parecord
  KILL → `riff=8`/`data=0` rejected by `wave`; arecord KILL →
  `0x80000000` **accept-and-lie** (8134× inflated frame count, stdlib
  wave accepts); ffmpeg KILL → `0xFFFFFFFF` inflated / 0-byte class.
- **rc is never the verdict**, ×4 shapes: rc=1 complete capture,
  rc=0 empty file, rc=255 valid file.
- `arecord -D null -d 1` is an **unpaced oracle**: 192044 B in ~0.021 s
  (48× wall); unbounded it floods ~5.8 GB/s.
- parecord ~1.9 s **dead start**; 64 KiB flush granules on stdout,
  256 KiB on ffmpeg file output.
- Monitor roundtrip: exact 960044 B capture with both content
  witnesses (nonzero fraction + peak within 3 dB of member).
- Named-failure classes: `pw_connect_failed` / `pa_connect_failed` /
  `ffmpeg_esrch` dead-daemon partition; `alsa_*` set_params family;
  `alsa_busy` contention carve-out honored by every bounded leg.

## Wave-B

- **critic D1 — the round's real defect**: a zero-audio capture passed
  the TERM gate (`data(0)` trivially satisfies finalized+aligned); two
  author receipts carried the vacuous row. Closed with
  `data_actual_zero is False` on all three TERM sites.
- **verifier N1/N2 — unchecked legs**: `ffmpeg_alsa_t` had no check;
  device-axis `sysdefault`/`plughw_first`/`hw_first` emitted-never-
  checked. Both armed (also caught: `sysdefault` is a WORKING capture
  route where `default`/`pipewire` are blocked).
- **verifier sha DISAGREE → rescoped**: canonical whole-receipt sha
  `ba36cd70` is quiescent-host bounded — mechanism measured (pw-record
  monitor teardown lag contends for the card). Pinned leaves +
  `failures:{}` remain the deterministic contract.
- simplifier D1–D9 byte-identical; baseline zero-drift; reviewer
  ADMIT-corr (MEDIUM-1/2 + LOW-3–10 all folded or scoped).
- Sweep: 29 GB unpaced-null rotation artifacts deleted (author scratch,
  uncited); harness + receipts retained.

## Next (r77 seeds — scout pre-measured)

`stream.capture.sink` fallback law (source names silently fall back to
the default-sink monitor; `pw-dump target.object` lies);
`sustained_after_target_loss` (capture survives provider unload at
100% rate, byte-identical); device-dependent TERM shapes
(`sysdefault`→`placeholder_80000000`+`alsa_read_eintr`); the 2 GiB
split-sentinel rename (`<name>-01.wav`); 5-witness reader matrix
(sndfile-info honest 11/11, soxi lies to 3h22m, wave fails safe).
Scout `78a7f8fb` already landed (36-cell lattice, all stable_bytes).
