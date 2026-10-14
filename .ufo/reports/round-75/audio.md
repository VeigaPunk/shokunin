# audio round 75 — consumer-class breadth: paplay + aplay + ffplay

**Stamp.** audio lane, round 75 (wave `shokunin-train-20261101-w14`; recovery dispatch — gen-1 seats died 16:10Z, respawned 16:20Z; model mix: swe-2 author, deepseek-flash analysis seats, swe-2 baseline/verifier). Lane commits `db46fba` (arm) + `5f60747` (folds) + `2250be9` (report-last).

## Work performed

`measure_audio.py` +936/−3 → `--probe-consumers2-r75`: three playback consumers (paplay pacat/libpulse, aplay in-process ALSA, ffplay lavf pull-model) on the canonical 9-member × 4-transport matrix + per-consumer ops rows (daemon-gate ordering, SDL driver axis, writerless-fifo kill classes, device axis, `-ss` position cell).

## Measured (independent verifier + critic convergence)

- **27/27 transport-invariant verdict groups** — all three consumers' verdicts are transport-blind on this corpus.
- **Cross-consumer non-transfers pinned:** paplay's `.snd` name axis absent (sf_open_fd name-blind — `Failed to open audio file.` on every arm); ffplay does not reproduce mpv's dec_hcom inverted seek fork (avio seeks stay 0 — SDL pull-model); aplay raw fallback invariant-accepts unmatched content.
- **Kill-class partition:** paplay TERM→-15, aplay catches TERM yet blocked→-9, ffplay TERM→graceful 123 with blocked read thread; paplay opens input BEFORE the daemon gate (ordering cell: dead-server + writerless fifo blocks in `open()`).
- **Four falsifications folded same-round:** `alive_after_term1` honest rename (aplay dies to TERM₂); vacuous-invariance guard (dead-server collapse now fails named; content rejection stays a verdict); `-ss` stdin = silent abort not decode-discard rescue; `_PACAT_RACY_TAIL` dead anchor re-anchored + path-only quote scrub (sample-spec witness preserved).
- Simplifier D1–D3 folded byte-identical; integrator post-fold re-run 27/27 clean.

## Remaining / next frontier

- r76 seeds: paplay content-vs-name accept leg (critic C5 — name axis measured only on reject path), consumer tail/parser hardening under load, SDL driver-axis depth, browser/WebAudio or language-binding consumers.
- Bounded: pacat/libpulse 17.0, aplay `-D null`, ffplay lavf + SDL_AUDIODRIVER=dummy, this host.

## Seat record

9/9 landed: author, scout, boundary, baseline, scribe, critic (C1–C5), reviewer (R1–R6 LOW), simplifier (D1–D3 proven, D4 withheld→re-anchor), verifier (AGREE, byte-identical ×5). Adjudicator: ADMIT-corr.
