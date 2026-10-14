# audio round 69 — coverage move: extension-suffix sweep on no-match bytes + dead-CHECK census

**Stamp.** Audio lane, round 69 (devin host, wave `shokunin-train-20261014-w8`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `30bb86d`, report-last `fe4c1d1` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Swept extension suffixes on identical 512-byte no-match bodies across all four transports + ran the first dead-CHECK-row census over committed receipts. `build_artifacts.py` (5 members `extsuffix_nomatch.{wav,bin,txw,f32,snd}` — byte-identical bodies, suffix-only difference); `measure_audio.py` (+`--probe-transport-extsuffix-*-r69` rows + `rows_hit`/`rows_dead` census). Ledger 114→119 rows (49 exit-0 / 70 exit-1), prior-114 byte-stable.

**Measured: identical bytes produce ≥5 distinct named-arm verdict classes — the suffix is load-bearing, not the bytes.** `.wav` → WAV reader `RIFF header not found`; `.bin` → `no handler for file extension 'bin'`; `.txw` → TXW reader rejects header + refuses pipes; `.f32` → raw float reader decodes 128 samples; `.snd` → ext-gated `sndr` detection decodes 504 samples at the selected rate. And `.txw` splits 3 ways within named transports.

**`.snd` is the first tracked member where detection itself forks by transport name**: `{file,fifo_path}` → detected `sndr`; `{stdin_pipe,redirected_fd}` → `None`. Scout refined it further: the `sndr` row is content-gated — needs zeros at bytes {0,1,7} — an ext-parameterized CHECK row (`formats.c:247-248`), the only one in the table.

**Census**: 130 active CHECK rows over 77 format types; pre-r69 committed receipts hit only 5 rows ever (act, gsrt, hcom, txw, wav — gsrt:81, txw:86, hcom:90, act:93, wav:95); **108/130 rows have never first-matched** within recorded scope; `.snd` adds the first `sndr` hit. Critic caveat absorbed: "dead" is a coverage statement, not deadness — 28/31 never-hit types actually detect; only `wma` is provably dead.

## Landed changes

- Members: `corpus/live/round-69/extsuffix_nomatch.{wav,bin,txw,f32,snd}` — byte-identical bodies, suffix-only.
- `corpus/knowledge/2026-10-14-sox-extension-suffix.md`; `reports/round-69/` all 9 seat reports + adjudicator.
- Verifier: full 119-row ledger replay — 49/70/0 (exit0/exit1/unparsed), 114 prior rows stable, census reproduced across 4,929 committed receipts.

## Before → after measurements

| metric | before | after |
|---|---|---|
| named-transport behavior | 2-class post-table partition (r68) | ≥5 verdict classes on identical bytes — suffix is the discriminating field |
| detection-fork members | `.snd` hypothesis (r68 beyond-claim) | first tracked member: `sndr` on named transports, `None` anonymous — content-gated {0,1,7}-zeros |
| CHECK-row coverage | unmeasured | 130-row census: 5 rows ever hit (96.2% dead in scope); `wma` provably dead |
| ledger | 114 rows | **119 rows**, prior-114 byte-stable |

## SHONEN

- [x] Declared falsifiable axis-move (coverage); ≥3-class claim exceeded (5 named classes + 3-way `.txw` split + detection fork)
- [x] Named non-author replay — **verifier AGREE 6/6** on `30bb86d` (119-row replay, verbatim member rebuilds, census independently reproduced)
- [x] No axis harmed — prior 114 rows byte-stable; additive members + census receipt only
- [x] Bounded claims (SoX_ng 14.8.0.1; `.snd` fork is content-gated; "dead" = never-hit-in-scope per critic, not undetectable)
