# audio round 62 — depth move: SoX 3,839 decode gap resolved (ffmpeg packet-residue)

**Stamp.** Audio lane, round 62 (devin host, wave `shokunin-train-20261013`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `cbe763e`, report-last `3c96a69` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Resolved r61's retained UNKNOWN: why SoX_ng 14.8.0.1 decodes `corpus/live/round-61/pair_valid_17.wav` to 3,839 f32 samples vs 5,760 for the valid16 control. Established chain (five independent seat derivations convergent, 28/28 author predictions confirmed): payload byte 256 = `0x84` collides with SoX's `act` autodetect (checked before `wav`) → file routes to the `(ffmpeg)` bridge → `wValidBitsPerSample=17` overwrites coded-sample width → `pcm_s24le` (3-byte) → demuxer packets `8192+3328` on the reclassified bitrate → decoder drops per-packet mod-3 tails → `2730+1109=3839` (one frame = 3 bytes lost). Also explained SoX `--i` "16-bit" display artifact (AU intermediary tag) and the payload-contingent routing fragility (byte-256 flip → native `wav` fatal rejection, which under `check=True` is a receiptless crash).

## Landed changes

- `corpus/fixtures/build_artifacts.py` +28/−1, `measure_audio.py` +13/−4 — additive-only: `build_ui_extensible_valid24_probe()` + `--probe-ui-extensible-valid-24/32-r62` modes emitting `corpus/live/round-62/pair_valid_{24,32}.wav` (second impossible-header family; pair differs only at byte 38).
- `corpus/knowledge/2026-10-13-sox-ffmpeg-packet-residue.md` — the measured law, factor isolation, gate interaction table, byte-256 fragility note, retained UNKNOWNs.
- `reports/round-62/` — 8 seat reports + verifier + adjudicator; seat scratch + all run receipts under `corpus/live/`.
- LOG.md: r62 declare/wave/verdict sections + append-only correction of r61's dangling pre-extraction commit pins (canonical equivalents recorded; blob SHAs verified faithful). SCORECARD.md: retro r61 verdict table + r62 verdict table + planned-line update.

## Before → after measurements

| metric | before | after |
|---|---|---|
| designated command ledger | 82 (43 exit0 / 39 exit1) | **84 (43/41)**, all prior modes verbatim |
| SoX decode of valid17 | 3,839 samples — cause UNKNOWN | 3,839 — fully attributed (mechanism + controls) |
| impossible-header families | 1 (valid17/16) | 2 (+ valid24/32: 3,839 / 2,880, exit 1 each) |
| non-author replay | — | **84/84 exits match, 84/84 receipts byte-identical** (`r62-verifier.md`) |
| frozen before-state | — | `git archive` standalone replay: identical 43/39, 81/82 receipts byte-identical (one absolute-path string inside captured stderr) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose
- [x] Named non-author replay passed all old + new classifications
- [x] No axis harmed (prior-82 preserved verbatim; additive-only diff)
- [x] Bounded claims; UNKNOWNs retained honestly (fallback ordering, packetizer-grid exhaustiveness, other tool versions)

Per-axis verdicts (Sol): depth, coverage, calibration each **improved locally**. Learning trends: expansion/quality/discernment all **improved**. No promotion action — four SHONEN boxes remain checked without promotion.
