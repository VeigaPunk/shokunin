# audio round 64 — coverage move: valid-bits→codec step map under the act/ffmpeg bridge

**Stamp.** Audio lane, round 64 (devin host, wave `shokunin-train-20261013-w3`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `4c12342`, report-last `b1e286c` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Mapped the `wValidBitsPerSample`→codec reclassification under the act-forced ffmpeg route established at r63. Three independent sweeps (author 74 variants, scribe 85, simplifier+boundary 17+39) converge on an exact **non-monotonic** step map: `w=(V+7)>>3` bytes → {1:pcm_u8, 2:s16le, 3:s24le, 4:s32le, 5–7:NONE, 8:s64le, >64:NONE}; seven boundaries pinned at adjacent sole-byte-38 pairs (0|1, 8|9, 16|17, 24|25, 32|33, 56|57, 64|65). Critic falsified the unscoped "pure function of vb" phrasing — the map is gated on the `0xFFFE ∧ cbSize≥22 ∧ PCM-GUID` envelope; precondition carried in all records.

## Landed changes

- `corpus/live/round-64/pair_valid_{8,9,24,25,56,57}.wav` (tracked; sole byte-38 diffs, all byte-256=0x84 act-forced) + `--probe-ui-extensible-valid-*-r64` modes; `build_artifacts.py` +36/−1, `measure_audio.py` +56/−4. Ledger 86→92.
- `corpus/knowledge/2026-10-13-sox-validbits-codec-map.md` — map, gate precondition, packet-residue application, attribution rules, UNKNOWNs.
- `reports/round-64/` — 8 seat reports + verifier + adjudicator.

## Before → after measurements

| metric | before | after |
|---|---|---|
| ledger | 86 (43/43) | **92 (44/48)**, prior-86 receipts byte-identical (3rd generation) |
| valid-bits surface | single families (17/24/32) | exhaustive step map + 3 tracked boundary pairs |
| envelope gate | undisclosed | measured (tag≠0xFFFE → container wins; cb21→NONE vs cb22→s24le) |
| residue mechanism | codec-inherent assumption | alignment×width proven (vb17@24-bit → lossless 3,840) |

## SHONEN

- [x] Declared falsifiable axis-move (coverage), evidence over prose
- [x] Named non-author replay passed all old + new classifications (AGREE all four claims)
- [x] No axis harmed (additive +92/−5; prior receipts byte-identical)
- [x] Bounded claims; UNKNOWNs retained honestly (non-USING_FFMPEG builds, float-GUID branch, stdin dead-combination)

Per-axis verdicts (Sol): coverage **improved locally**, depth **improved locally**, calibration **unchanged**. No promotion action.
