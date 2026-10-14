# r78 AUTHOR (audio) — the playback-direction lattice

Read reports/round-78/r78-scout-playback.md FIRST (the write-side
frontier, ALL PRE-MEASURED: unresolvable/default/source/.monitor/
absent targets all land the CURRENT default sink — rc=0, empty stderr,
real-time playout, consumers=<default>:playback_FL/FR; the fallback
FOLLOWS live default via pw-metadata but NOT pactl set-default-sink
(rc=0 silent no-op = stale default); prop target.object beats --target
both directions; PIPEWIRE_PROPS second vector; media.class bogus ->
SIGSEGV rc=-11 3/3; mid-play unload -> silent re-link to default;
manual pw-link -d -> no re-link, file consumed into nowhere at
real-time rate (unlinked_sustained_playout); pactl move-sink-input
works mid-play; suspend-sink no-op; set-sink-mute silences the monitor
tap; aplay -D hw: EBUSY when a monitor witness holds the PCM with
~1-7s lock retention; aplay converts vs arecord constrains; hw:0,0
playback 2-8ch S32_LE vs capture stereo-only; alsa_tick_time row
FALSIFIED - do not re-arm it) plus r78-scout.md for capture-side gaps.

ARM — measure_audio.py insertion-only (prior cells byte-stable; new
--probe-capture-r78 / playback entries appended):
- write-side fallback lattice cell: the full target-name matrix ->
  all -> current default sink, witnessed by pw-link consumers +
  content (play a tone, monitor-tap the sink, verify level).
- live-default-follow cell: switch default.audio.sink via
  pw-metadata mid-probe -> fallback rows move; pactl
  set-default-sink rc=0 no-change witness (name the stale-default
  class explicitly).
- mid-play target-loss cell: unload the target sink during playout
  -> silent re-link to default (consumers move, playout continues,
  rc=0); contrast pw-link -d -> unlinked_sustained_playout (no
  re-link, no stall, real-time consumption into nowhere).
- target.object-vs-argv precedence + PIPEWIRE_PROPS vector cell.
- bogus media.class SIGSEGV cell (rc=-11, empty stderr) — pin as a
  crash class in the fatal tail if the harness has one, else as a
  named crash row.
- aplay device-axis cell: EBUSY-under-witness + lock retention
  bracket (+1s busy / +7s free), conversion vs constraint, hw:0,0
  playback channel/format envelope.
- capture-side gaps from r78-scout.md as remaining rows permit:
  unlinked_sustained_zeros, parec --fix-* header mismatch.
Host state: DualSense is the default SOURCE now (stable change);
default sink is SPDIF; per-process sink naming convention from r77
fold applies (use r78_loss_sink_<pid> etc). Keep every gate
fail-closed; the probe must PASS on this host.
Report -> reports/round-78/r78-author.md.
