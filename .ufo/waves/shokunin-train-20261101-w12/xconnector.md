# xconnector — cross-lane synthesis over wave-12 landings + frontier seats

Seat: xconnector, wave `shokunin-train-20261101-w12`. LEAF read-only
(subagent_explore — synthesis + receipt re-reads + upstream doxygen; no
runtime probes this seat). Written to file by operator, verbatim synthesis.

## Answers to the three explicit questions

### (a) lavf demuxers beyond hcom — refined fork rule + candidates

Measured (r73 `febf34b`): only `dec_hcom` forks — mpv 0.41.0 + lavf
63.1.101, {file,redirected_fd} -> synthetic EPERM rc=2 (0 failing syscalls)
vs {stdin_pipe,fifo} -> rc=0. pw-cat x .snd is a separate NAME-axis fork.
All other members transport-invariant.

Source-derived rule (UNMEASURED): fork requires ALL of (1) content-probe
detection; (2) demuxer has no `.read_seek` and no `.read_timestamp`;
(3) no AVFMT_GENERIC_INDEX; (4) codec not pcm_*+block_align (mpv
demux_lavf.c "PCM seek hack" rescues — why dec_act stayed invariant).

| demuxer | predicted |
|---|---|
| iss (IMA_ADPCM_Sound) | fork — candidate #1 |
| apc (CRYO_APC) | fork — candidate #2 |
| acm (Interplay ACM; NO_BYTE_SEEK flags) | fork — candidate #3 (ENOSYS-class, same wound) |
| wav/aifc/au/sol/vqf/dss/pp_bnk (own read_seek) | no fork |
| wady/sdr2/aax/adx/wv (GENERIC_INDEX) | no fork (index seek) |

Wound-shape corollary: seekable-arm rc=2 requires find_stream_info to
consume the whole stream — a MULTI-PACKET member on a no-seek demuxer
predicts head-truncation rc=0 fork, not rc=2. Same axis, two wound shapes.
W11 X2 corollary: `mpv --start=N` on seeking member -> position fork.

### (b) bpy evalcat residue — enumerable, 2 critic categories uncovered

r81 landed 4/6 critic categories (catalogue 8->14). Still uncovered:
`update_tag` (tag!=eval — purest discriminating witness) + one
custom-setter. ~80 measured-inert-untracked classes; a second ~6-class
representative fold adds witnesses, folding all ~80 is inert noise.

### (c) non-Python reorder — already measured on host

`corpus/live/r72-critic/c_reorder.c` + c-matrix.txt: C stdio buffered ->
`CHILD\nHEAD\nTAIL\n` prefix_reorder 3/3; flush-head -> midline splice.
Reorder is libc-general {CPython, bpy-embedded, C stdio}; LuaJIT io.write
splice. **Node.js v24.21.0 on host = live falsifiable next cell**:
prediction — libuv uv_write try-write fast path -> small writes
synchronous -> splice; >64KB write -> queue remainder -> infix (third
withholding layer: event-loop queue). Either outcome is signal.

## Ranked wave-13 arms

- **X2 lavf no-seek demuxer sweep (audio, top mechanism yield)** — iss/apc/
  acm predicted fork; controls wav+aifc; member generation is the cost
  driver (ffmpeg-mux or hand headers); degrade to inventory receipt if
  generation fails. Secondary cells: multi-packet truncation-fork,
  `mpv --start=N` position fork.
- **X4 reorder topology depth (g2d)** — pin {infix via paced flush, detach
  EOF-hold, fd2-inversion}; all measured unpinned in r72/r81-boundary;
  bounded-range pins not exact offsets.
- **X1 owner census (rides with X4)** — Node small-write (splice
  prediction) + >64KB (infix prediction) + C cell re-pin. Viability-
  conditional on node presence.
- **X7+X6 (g3d)** — evalcat residual fold (~6 classes incl update_tag +
  custom-setter) + parser-hazard pinned cells (forged violations=0 row,
  dup_flush forged logical-last) through tracked parse_arms. Pin-level
  completion of measured evidence.
- **X5 physics interior writes (biggest cost, banked)** — LOVE
  beginContact/preSolve/postSolve write classes; Godot PhysicsServer3D
  generated-event two-tier + run_on_separate_thread + Jolt-availability.
- **X3 pw-cat hang taxonomy (audio, mostly measured)** — block-location
  partition {writerless-fifo SIGTERM-immune | --target 0 TERM-terminable
  rc124 | zero-sink private daemon unmeasured}; `-a/--raw` bypass kills
  the name axis. Folds into r74 as ops-2 arm if seats have capacity.

## Scope guards (report must carry)

Consumer polarity is member-local not corpus-wide; topology is the
fd1-OWNER's mode not descendant's; bpy PYTHONUNBUFFERED inert without
--python-use-system-env; buffer constant per-build (131072 on CPython
3.14.7 only); wire order + write-order both required as witness; parser
survives != parser safe (r81 contract = distinct keys + marker presence
+ physical last-wins + drop-not-misattribute on the demonstrated glue);
evalcat closure bounded to probed catalogue; timing leaves jitter unless
semantically pinned.

## Risks

Node lands either family — both signal; iss/apc/acm need valid member
bytes; Jolt may be absent from host Godot (record availability first);
interior-write cells may crash probe (order last); truncation-fork could
produce rc2 instead (the cell measures this).
EOF