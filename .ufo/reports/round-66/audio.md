# audio round 66 — coverage move: preemptor-map completion (wve + decodable controls + exact length gates)

**Stamp.** Audio lane, round 66 (devin host, wave `shokunin-train-20261013-w5`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `014b532`, report-last `0df212f` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Completed the preemptor map on the RIFF+0x84@256 domain. `wve` predicate pinned byte-exact (`len≥15 ∧ file[0:15]=="ALawSoundFile**"`, all 15 bytes load-bearing, floor exactly 15) — and the declared wve-on-RIFF ordering claim hit its **else-branch**: byte-0 `0x41` vs `0x52` makes a wve-shaped RIFF impossible-by-construction; the reachable pre-act set is provably exactly **{gsrt, hcom}**. wve does preempt gsrt/hcom/act on non-RIFF carriers (table row 80 is live, just unreachable on RIFF). Landed the tracked decodable-preemptor pair (`pair_dec_hcom` — byte-identical to r65-critic's D1, native hcom reader decodes 9 samples — ↔ `pair_dec_act`, sole-byte@68 flip to the ffmpeg bridge at 278) and exact length-gate members (gsrt 24‖25, hcom 131‖132 — read-window property, re-pinned on bare carriers).

## Landed changes

- `corpus/live/round-66/` six members; `build_artifacts.py` +113, `measure_audio.py` +93; ledger 96→102 (44 exit0/58 exit1); prior receipts byte-identical.
- `corpus/knowledge/2026-10-14-sox-preemptor-map-complete.md`; `reports/round-66/` — 8 seat reports + verifier + adjudicator.
- Absorbed: detector≠reader contract table (wve detector looser than 18-B reader ID; gsrt stricter @24; hcom chain-gated); stdin+ffmpeg-bridge structurally dead; gsrt reader floor 34>25; hcom integrity guards inert; `pair_dec_act` bridge decode regular-file-only; txw/smp refuse pipes. SCORECARD r65 wording corrected (wve scoped off-RIFF).

## Before → after measurements

| metric | before | after |
|---|---|---|
| preemptor set on RIFF | {gsrt, hcom} measured w4 | **{gsrt, hcom} proven complete** — wve geometrically excluded, all pre-act rows byte-0-anchored |
| decodable-preemptor controls | critic scratch only | **tracked pair**, three-way sha-convergent |
| ledger | 96 (44/52) | **102 (44/58)**, prior receipts byte-identical |
| transport model | seekability conjunct | + stdin-bridge-dead, reader-floor bands, pipe-refusal classes |

## SHONEN

- [x] Declared falsifiable axis-move (coverage), else-branch recorded honestly
- [x] Named non-author replay (AGREE all five claims — 102/102 ledger exits+receipts byte-identical)
- [x] No axis harmed (additive; prior receipts byte-identical)
- [x] Bounded claims; UNKNOWNs retained (wve reader interior, ffmpeg-less builds, non-RIFF breadth)

Per-axis verdicts (Sol): coverage **improved locally**, depth **improved locally**, calibration **unchanged**. No promotion action.
