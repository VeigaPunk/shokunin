# audio round 70 — depth/calibration move: fifo writer-hold measured as a transition band (chunked feed refutes binary-on-attach)

**Stamp.** Audio lane, round 70 (devin host, wave `shokunin-train-20261014-w9`, 8-lane seat set + Sol adjudication). Lane commits: work `59a7440`, report-last `e4e0444`.

## Work performed

Laddered the fifo writer-hold constant `fifo_writer_hold_s=1.0` on the `dec_act` member — the arm whose verdict needs the ffmpeg bridge's second open. `--probe-fifo-hold-ladder-r70`: 6 holds {0,0.05,0.2,0.5,1.0,2.0}s × 2 feeds (oneshot, chunked) × 10 reps, per-cell verdict distributions. `fifo_feed` gained a chunked variant (60B chunks @ 50ms — attach-through-delivery); `fifo_hold_leg` runs the child in its own session + killpg.

**Measured: the bound is a transition zone, not a point.** Oneshot: h=0 → 10/10 `blocked: no verdict within 10 s` (writer detaches before open #2; the bridge grandchild dead-locks in `openat`); h≥50ms → 10/10 exit-2 au-magic. Zone ≈ (0, ~50ms] on this host — reported as `{max_divergent, min_stable}` per feed per run (critic correction; a finer sweep found mixed ~18ms). **Chunked lands 10/10 at every hold including h*=0** — feed duration spans the open window, refuting strict binary-on-attach with the predicted third outcome (attach-through-delivery). Pinned 1.0s = ~20x margin — defensible, never a bound.

**Critic corrections integrated at `59a7440`**: `wall_s` floats removed from the committed receipt (byte-identity discipline); point `h*` relabeled `hold_transition_band_s` + load-zone semantics; `/proc` cmdline `reap_fifo_orphans` backstops killpg on BOTH fifo legs (the bridge grandchild escapes the child's process group — falsified by a 5-min survivor); canonical `transport_matrix` fifo arm gets the same reap.

## Landed changes

- `measure_audio.py` +252 (`fifo_writer_hold_s` env-param + `fifo_feed` + `fifo_hold_leg` + `fifo_hold_ladder_entry` + reap); `build_artifacts.py` +9 (self-sufficient probe flag).
- `corpus/knowledge/2026-10-14-sox-fifo-hold-bound.md`; `reports/round-70/` 4 landed seat reports + adjudicator.

## Before → after measurements

| metric | before | after |
|---|---|---|
| writer-hold constant | chosen 1.0s point (r67) | measured transition band {0, ~50ms] oneshot / none→0.0 chunked — load-dependent zone |
| outcome model | binary-on-attach hypothesis | refuted — third outcome: attach-through-delivery (chunked stable at h*=0) |
| orphan safety | killpg assumed sufficient | falsified (5-min survivor) → killpg + /proc reap on both fifo legs |
| receipt discipline | floats-free | preserved — distributions only, wall_s kept out of the committed receipt |

## SHONEN

- [x] Declared falsifiable axis-move (depth/calibration); claim resolved to a measured band + the binary branch falsified-by-construction
- [x] Non-author replay — verifier seat lost to rate limits (5 respawn attempts wave-wide); operator adjudicator probe on `59a7440` + baseline's independent 10-rep ladder agree verbatim (blocked 10/10 @ h=0; exit-2 10/10 ≥50ms; chunked all-stable); adjudicator dec_act byte-stability check vs r69 receipt: identical
- [x] No axis harmed — default 1.0s preserved; prior-119 rows byte-stable; additive flag only
- [x] Bounded claims (SoX_ng 14.8.0.1 USING_FFMPEG + ffmpeg n9.0.1; zone load-dependent; outcome space = attach × close-before-deadline)
