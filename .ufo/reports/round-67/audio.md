# audio round 67 — depth move: transport as a first-class ledger axis

**Stamp.** Audio lane, round 67 (devin host, wave `shokunin-train-20261014-w6`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `366fcc1`, report-last pending scout landing — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Transport promoted to a first-class measured axis over the complete 10-member tracked autodetect set: single parameterized `transport_leg`/`transport_matrix` in `measure_audio.py` over `{file, stdin_pipe, redirected_fd, fifo_path}`, detection tracked separately from decode-stage verdicts, deterministic fifo via the pinned `TRANSPORT_R67_FIFO_WRITER_HOLD_S = 1.0` writer-linger. Result: **112-row transport ledger (49 exit-0 / 63 exit-1, zero UNPARSED)**, prior-102 receipts byte-identical.

**Measured partition:** detection NEVER forks (`sox_detected_format` identical across all 40 cells). Decode-stage fork set = exactly the 5 act/gsrt-detected members `{preempt_act, preempt_gsrt, preempt_both, dec_act, lengate_gsrt_25}`; the 5 hcom/wav-detected members are transport-invariant. Fork locus attributed: native gsrt reader forks on the fd **seekable bit** (checksum gate skipped on non-seekable); the act/ffmpeg bridge forks on **child-side name resolvability** — file decodes (278), anonymous-seekable fd → `premature EOF`, pipe/fifo → `can't find Sun/NeXT/DEC identifier`.

## Landed changes

- `measure_audio.py` transport arms + 10 `--probe-transport-*-r67` modes (+mechanical pyc regen); `corpus/knowledge/2026-10-14-sox-transport-axis.md`; `reports/round-67/` 8 seat reports + verifier + adjudicator.
- Boundary refinement absorbed: the contract is *what the ffmpeg child can re-resolve*, not the `{named × seekable}` proxy — fifo+dead-writer hangs the whole command; early-EOF fifo flips DETECTION at each member's len gate; scribe added a timing-free `fifo_hold` (`O_RDWR` holder) transport landing identical verdicts.
- Critic absorptions: verdict-tuple reading pinned ({exit,samples}-only → 2-member fork set; implemented tuple → 5); receipt byte-stability bounded to SERIAL execution (non-atomic `build_artifacts.py` rebuild race disclosed, fix deferred).

## Before → after measurements

| metric | before | after |
|---|---|---|
| transport knowledge | seekability conjunct (r65) + per-member anecdotes | **10×4 matrix receipt-pinned**; fork partition exact |
| fork locus | "transport matters" | attributed: native-reader seekable bit / bridge name-resolvability |
| fifo protocol | one-shot writer (racy) | **pinned 1.0s linger** in every receipt + `O_RDWR`-holder variant measured identical |
| ledger | 102 commands | **112 (49/63)**, prior byte-identical |

## SHONEN

- [x] Declared falsifiable axis-move (depth), measured exactly
- [x] Named non-author replay — verifier **AGREE 5/5**, 10 receipts byte-identical to author
- [x] No axis harmed (additive; prior receipts byte-identical)
- [x] Bounded claims; UNKNOWNs retained (serial-execution bound; fifo residual race; txw/smp pipe-refusal member gap → r68 frontier)
