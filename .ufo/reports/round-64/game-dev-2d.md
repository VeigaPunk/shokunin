# game-dev-2d round 64 — depth move: while-live signature gate discriminates forged post-death writes

**Stamp.** game-dev-2d lane, round 64 (devin host, wave `shokunin-train-20261013-w4`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `a32920b` + fix `5265da6` (verifier-caught integration miss), report-last `61ec1c0` — identity `game-dev-2d-shokunin <game-dev-2d@shokunin.local>`.

## Work performed

XConnector wave-3 synthesis landed: a **while-live gated signature read** discriminates forged post-death signatures from genuine ones. New meta row `probe_while_live_signature_gate` (selectors/os.read + `poll()` at the marker-completing read): forged release×3 + hold markers observed ~32ms post-death → **REJECTED** (gate rejects a present marker); genuine+detach accepted (+66–71ms margin). 12 discriminations; r63 accepting-boundary row byte-stable — the gate is an observation path, not a classifier fix.

## Landed changes

- `corpus/fixtures/run_battery.py` +228/−0 (one unconditional meta row; classifier/run_process/CASES byte-identical). `corpus/lessons/r64-while-live-gate.md`; `reports/round-64/` — 8 seat reports + verifier + adjudicator.
- Integration corrections: `poll()` primitive pinned in comment (`kill(pid,0)` false-accepts 13/13+29/29+6/6+3/3 across four seats through the zombie window); death-ordering `<`→`<=` (sub-tick forgers).

## Before → after measurements

| metric | before | after |
|---|---|---|
| seven-flag battery | 96/96 | **97/97**; prior 96 rows 0-mismatch |
| forgery boundary | accepting-boundary pinned (r63) | + its measured dual: post-death forgeries rejected under poll-gate |
| zombie window | inferred | quantified: 2.35–2.42s drain under communicate() vs 1–4ms under gate |
| authorship attacks | unprobed | live-window forge defeats gate 6/6+29/29 (bounded_claim load-bearing); stall knee ~0.65s |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose
- [x] Named non-author replay: claims 2/3/4a/4b AGREE; claims 1+5 DISAGREE-as-worded caught a real integration miss — resolved by landing the byte-identical verified blob (committed sha == measured sha)
- [x] No axis harmed (additive-only; prior rows field-identical)
- [x] Bounded claims; UNKNOWNs retained (live-window forge, host/load margins)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
