# audio round 73 — coverage: consumer class (pw-cat realtime + mpv lavf) on the transport matrix

**Stamp.** Audio lane, round 73 (wave `shokunin-train-20261101-w12`; 9-seat fleet, deepseek analysis seats + swe-2 authors). Lane commits `f5d7faf` (r72 reviewer-fold) + `febf34b` (r73 arm).

## Work performed

`--probe-consumers-r73` arm in `measure_audio.py` (+466/-3): pw-cat (PipeWire realtime, libsndfile decode layer) + mpv (lavf) across the canonical 9-member × 4-transport matrix + `consumer_pwcat_ops_r73_probe` operational entry (daemon gate, fifo writer-attach, playback pacing, trickle, name-axis 2×2).

## Measured (operator replay + 4-seat convergence)

- **mpv × dec_hcom inverted seekability fork** — {file, redirected_fd} rc=2 via lavf refresh-seek → synthetic `Operation not permitted` (strace: 0 failing syscalls; hcom demuxer has no read_seek); {stdin_pipe, fifo} rc=0 + 3520 PCM bytes. Member-local; opposite polarity to sox × txw.
- **pw-cat × extsuffix_snd name-axis fork** — {file, fifo} rc=0 vs {stdin, rfd} rc=1; `pwcat_name_axis` cell isolates name-vs-transport (same bytes, fifo renamed `.snd/.wav/.bin` → rc {0,1,1}). Frontier's "no suffix axis" falsified — member-set artifact.
- Ops: daemon gate rc=1 "Host is down" in ~2ms before open; writerless fifo blocks `wait_for_partner` (SIGKILL-bound); playback-paced drain 4.03s/4s; starved trickle blocks to EOF.
- Corpus-wide "consumer polarity partition" claim **falsified** (2 forks / 40 legs, different drivers); member-local restatement confirmed.

## Remaining

Author report + verifier replay in flight at adjudication; r73 baseline env pending. wall_s leaves = measured realtime jitter (pins on verdict signatures). Bounded: PipeWire 1.6.8, mpv 0.41.0/lavf 63.1.101, this host.
