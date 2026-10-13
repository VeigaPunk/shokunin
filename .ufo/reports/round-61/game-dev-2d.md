# game-dev-2d round 61 — coverage move: tracked spontaneous-crash classification

**Stamp.** game-dev-2d lane, round 61 (devin host, wave `shokunin-train-20261013`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `b95d180`, report-last `08d80dc` — identity `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`.

## Work performed

Landed the r60-identified durable surface for spontaneous-crash classification in the headless Godot 4.7.2 battery: a spontaneous `OS.crash` exits −6 (SIGABRT, via SIGILL→handler on this build) carrying its own `ERROR:` marker, and a self-`OS.kill` exits −9. Both now classify True — the −6 arm via a scoped exact-match `expected_errors` allowlist, the −9 arm unmodified. An unconditional meta row `probe_spontaneous_crash_classification` re-classifies the captured outputs under four mismatched expectations (expected −9 on the −6 capture, missing allowlist, wrong allowlist, expected −6 on the −9 capture) — all must reject — plus a **marker-presence clause** added at integration after the critic's concrete forgeries showed the allowlist forgives but never requires the marker.

## Landed changes

- `corpus/fixtures/spontaneous_crash_probe.gd` (new; executable content byte-identical to twice-measured r60 scratch probe).
- `corpus/fixtures/run_battery.py` **+43/−0** additive (2 CASES rows + 1 expected_errors entry + 1 meta row); runner internals `classify_process`/`run_process`/`classify_streams` byte-identical.
- `corpus/lessons/r61-crash-classification.md` (decision table + bounds) + `r61-crash-non-author.json` (verifier raw receipt).
- `reports/round-61/` — 8 seat reports + verifier + adjudicator; scratch evidence `corpus/live/r61-*/`.
- LOG.md r61 section; SCORECARD.md coverage row → r61 + planned-line update.

## Before → after measurements

| metric | before | after |
|---|---|---|
| seven-flag battery | 89/89 PASS (frozen `git archive` baseline, byte-identical) | **92/92 PASS** (author + parent + named verifier, three independent runs) |
| prior rows | — | **89/89 field-identical** on the 7-field tuple vs `corpus/lessons/r59-audio-non-author.json` |
| spontaneous −6 crash with marker | classified False (unrecognized, scratch-only) | tracked row PASS + discriminations all reject |
| self −9 kill | classified False (scratch) | tracked row PASS unmodified |
| forgery resistance | (untested) | markerless −6 / empty-allowlist / wrong-allowlist / missing-signature constructions all reject — measured by critic + verifier |

## SHONEN

- [x] Declared falsifiable axis-move (coverage), evidence over prose
- [x] Named non-author replay passed all old + new classifications
- [x] No axis harmed (additive-only; all 89 prior rows field-stable; classifier untouched)
- [x] Bounded claims; signal-origin UNKNOWN retained and demonstrated

Per-axis verdicts (Sol): coverage **improved locally**; depth and calibration **unchanged**. Learning trends: expansion/quality/discernment all **improved**. Boundary findings (pipe-EOF timeout misattribution, no process-group kill, startup knee 7.5–7.6 s) recorded as r62+ candidates. No promotion action.
