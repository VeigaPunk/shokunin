# audio round 65 — coverage move: preemptor-collision autodetect ordering on RIFF files

**Stamp.** Audio lane, round 65 (devin host, wave `shokunin-train-20261013-w4`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `1b0d276`, report-last `30e5e32` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Mapped the pre-act autodetect preemptor ordering on RIFF+0x84@256 files. Total first-match-wins order measured: **`wve ≺ gsrt ≺ hcom ≺ act ≺ wav`** — no preemptor-shaped file ever routes act. Only `gsrt` (`ring.bin\0`@16–24, len≥25) and `hcom` (`FSSD`@65–68 ∧ `HCOM`@128–131, len≥132) geometrically intersect the act trigger; conjunction-exact, len gates exact; post-act rows shadowed.

## Landed changes

- `corpus/live/round-65/pair_preempt_{act,gsrt,hcom,both}.wav` (11,588 B each; sole signature-span diffs; `act` byte-identical to r63 `pair_route_84`); `build_artifacts.py` +40/−1, `measure_audio.py` +65/−4; ledger 92→96 (44/52).
- `corpus/knowledge/2026-10-14-sox-autodetect-preemptor-ordering.md`; `reports/round-65/` — 8 seat reports + verifier + adjudicator.
- Critic corrections absorbed: preemptor-detected ≠ reader-fail (hcom decodes 9 samples); `premature EOF` non-attributing; fd seekability conjunct (gsrt decodes 11,076 on pipes where ffmpeg bridge dies).

## Before → after measurements

| metric | before | after |
|---|---|---|
| autodetect surface | one pinned predicate (act) | total order + precedence semantics + tracked collision family |
| ledger | 92 (44/48) | **96 (44/52)**, prior-92 receipts byte-identical |
| reader-fate model | detection conflated with accept | decoupled — detection, open, decode are separate stages |
| stdin | "dead combination" | refined: ffmpeg bridge dies, native gsrt/hcom survive pipes |

## SHONEN

- [x] Declared falsifiable axis-move (coverage), evidence over prose (4 independent sweeps converge)
- [x] Named non-author replay passed all old + new (AGREE all five claims, committed-state)
- [x] No axis harmed (additive +105/−5; prior receipts byte-identical)
- [x] Bounded claims; UNKNOWNs retained (preemptor reader internals, other builds, non-RIFF carriers)

Per-axis verdicts (Sol): coverage **improved locally**, depth **improved locally**, calibration **unchanged**. No promotion action.
