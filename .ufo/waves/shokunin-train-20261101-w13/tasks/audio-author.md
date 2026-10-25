# r74 AUTHOR (audio) — lavf no-seek demuxer sweep + pw-cat ops-2

Read SHARED.md + r73 author/adjudicator/critic reports first.

ARM A — lavf no-seek demuxer sweep (xconnector X2, top mechanism yield).
Source-derived UNMEASURED claim under test: a lavf demuxer forks mpv on
the seekable-bit IFF (1) content-probe detects it, (2) demuxer has no
`.read_seek`/`.read_timestamp`, (3) no AVFMT_GENERIC_INDEX, (4) codec is
not pcm_*+block_align (mpv PCM seek hack). Predicted FORK: iss
(IMA_ADPCM_Sound), apc (CRYO_APC), acm (Interplay ACM). Predicted
INVARIANT controls: wav, aifc already on corpus; if generatable, one
GENERIC_INDEX member (adx or wv) as the index-seek control.
Member generation is the cost driver: try `ffmpeg -f lavfi` synth ->
mux via ffmpeg into iss/apc/acm if encoders exist; else hand-build
minimal headers (hcom member ~600B precedent). If a member cannot be
generated, record the exact blockage — degrade to a demuxer-inventory
receipt rather than fabricate.
Secondary cells (cheap): (i) multi-packet member on a no-seek demuxer
predicts head-truncation rc=0 fork not rc=2 (wound-shape corollary);
(ii) `mpv --start=N` on wav predicts a POSITION fork (file seeks, fifo
plays from 0).
Implement: `--probe-lavfsweep-r74` + receipts under `runs/<ts>-lavfsweep-
r74`. Parse lavf log fields (detected format, probe score, seek_failed,
audio_track, playback reason) — NEVER bare rc. timeout -s KILL on all
fifo arms. Members that generate land under corpus/live/ (new members
documented in the report).

ARM B — pw-cat ops-2 (xconnector X3, mostly pre-measured).
Pin the hang taxonomy measured by r73-boundary + fb-pipewire:
writerless-fifo open-block (SIGTERM-immune, wait_for_partner — already
pinned, add the missing kill-escalation rc cell); `--target 0`
unlinked-stream class (TERM-terminable, boundary measured rc124@4s —
pin as a NEGATIVE ops case with bounded timeout); `-a/--raw` bypass
kills the name axis (identical .snd bytes through raw mode on the
.wav-named fifo predicts rc=0 — the name axis dies without the decode
layer). Zero-sink private-daemon cell ONLY if cheap (private
PIPEWIRE_RUNTIME_DIR); else record blockage.
Extend consumer_ops_entry with an ops2 sub-block or a parallel
`pwcat_ops2` key — insertion-only.

Viability gates: ffmpeg lavfi/muxers present; pipewire daemon live.
Preserve ALL prior rows byte-identical. Report writes to
reports/round-74/r74-author.md. If a prediction fails, report the
measurement — falsification is the deliverable.
