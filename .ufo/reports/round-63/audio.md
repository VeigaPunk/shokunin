# audio round 63 — depth move: `act` autodetect predicate pinned exactly

**Stamp.** Audio lane, round 63 (devin host, wave `shokunin-train-20261013-w2`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `1a97b0e`, report-last `37d4c57` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Pinned the r62-disclosed fixture fragility to an exact, source-cited predicate. SoX_ng 14.8.0.1 reads at most 257 bytes (`AUTO_DETECT_SIZE`, sized "for act") and runs first-match-wins CHECK rows; the act row `CHECK(act, 0,4,"RIFF", 256,1,"\x84")` (formats.c:93) precedes wav's (:95). Established: `detected==act ⟺ len≥257 ∧ file[0:4]=="RIFF" ∧ file[256]==0x84 ∧ ¬earlier-CHECK` with preemptors gsrt `ring.bin\0`@16 and hcom `FSSD`@65∧`HCOM`@128. Closed r62's retained ordering UNKNOWN: `open_read` dispatches once — no fallback chain; `act` IS the ffmpeg pseudo-handler (G729A voice); the terminal `premature EOF` is the au reader on an empty ffmpeg pipe.

## Landed changes

- `corpus/fixtures/build_artifacts.py` +32/−1 (`build_ui_route_act_r63_probe` → `corpus/live/round-63/pair_route_{84,00}.wav`, sole byte-256 diff) + `measure_audio.py` +25/−4 (`--probe-ui-route-act-{84,00}-r63`, `sox_detected_format`/`sox_route` receipt fields).
- `corpus/knowledge/2026-10-13-sox-act-autodetect-predicate.md` — predicate, routing chain, observable signatures, fixture-authoring rule, retained UNKNOWNs.
- `reports/round-63/` — 8 seat reports + verifier + adjudicator; seat scratch + receipts committed per lane convention.

## Before → after measurements

| metric | before | after |
|---|---|---|
| act trigger | UNKNOWN disclosed as fragility | exact predicate, 23,738+1,408+293+~30 probe rows, source-cited |
| designated ledger | 84 (43/41) | **86 (43/43)**, prior 84 verbatim |
| tracked routing control | none | `pair_route_{84,00}.wav` — act/ffmpeg/3839 vs wav/native-fatal-exit2 |
| non-author replay | — | **86/86 exits + 86/86 receipts byte-identical** |
| fallback-ordering UNKNOWN | open | closed: single dispatch, no retry (`goto error`) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose
- [x] Named non-author replay passed all old + new classifications
- [x] No axis harmed (additive-only +57/−5; prior-84 byte-identical)
- [x] Bounded claims; UNKNOWNs retained honestly (non-USING_FFMPEG builds, stdin path, exotic preemptors)

Per-axis verdicts (Sol): depth, coverage, calibration each **improved locally**. Learning trends: expansion/quality/discernment all **improved**. No promotion action.
