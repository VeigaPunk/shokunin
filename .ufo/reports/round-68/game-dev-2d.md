# game-dev-2d round 68 — depth/calibration move: midlineforge fabrication-window bound + stream-meta receipt upgrades

**Stamp.** 2D lane, round 68 (devin host, wave `shokunin-train-20261014-w8`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `f754546`, hygiene `e8d4fb7`, report-last `4d8a525`.

## Work performed

Parameterized the r66 midlineforge descendant write as an offset ladder and measured the fabrication-window bound; upgraded the r67 stream-attribution receipt with per-row clause attribution + same-input digest gates. `descendant_pipe_probe.gd` +17/−4 (`--midline-offset-ms=N`, default 80 — r66 arm byte-stable); `run_battery.py` +302/−2 (`--probe-midlineforge-ladder` opt-in meta: 6 offsets × 3 reps through `surface_run`, 8 discriminations, `measured_window` receipt; `divergent_clause` per divergence_table row; `raw_stdout_sha256`/`raw_stderr_sha256` per dual_classify record — discriminations 20→24).

**Measured: the fabrication lands iff the write reaches the captured pipe between head-flush and tail-flush** — write-position space `[0, gap)`, gap 200.02–200.16ms. Nominal-offset space: {0–198} fabricate rep-perfectly, transition band 198.05–198.35 (jitter ~1ms), ≥198.5 never — nominal edge = 200ms gap − ~1.4–2.5ms spawn overhead. Lo edge is a spawn-latency floor (negative offsets all splice — downward-unbounded, boundary). Three regimes: pre/post-miss = standalone ERROR + signature INTACT (verdict still FAIL — the window controls which clause corrupts, never whether); in-window = fused line + signature destroyed; rare straddle H-E-T-E2 (~0.1ms). ppid provenance invariant; crossover ~250–260ms.

Critic falsifications absorbed: declared bound is a write-position bound not a nominal-offset one (~80× resolution overstatement corrected); `divergent_clause` maps WHICH clause not which mechanism (`error_scan` covers 3 mechanisms; `exit` structurally dead — dead conditional deleted `e8d4fb7`); sha256 binds decoded text (b"\xff"≡b"\xfe" collision; empty-vs-absent indistinguishable). Boundary edges: TIMEOUT captures nondeterministic (stderr tail spread; seam under timeout; mid-line byte-truncation); duplicate in-window writes splice independently. Simplifier: minimal bar met; two byte-identical deletions applied (`e8d4fb7`); mirror fidelity proven via AST truth table (0/132 mismatches).

## Landed changes

- `corpus/lessons/r68-midlineforge-fabrication-window.md`; `reports/round-68/` all 9 seat reports + adjudicator.
- Scribe: ~256 own real-pipe runs — bound {0–198}/198.05–198.35/≥198.5 verified sharper than worded; clause map + digest chain verified.
- Verifier: independent ladder 18/18 exact + own instrumented edge ≈198 + from-spec clause recompute 9/9 (not mirrors).

## Before → after measurements

| metric | before | after |
|---|---|---|
| fabrication window | single point-sample at 80ms | strict measured bound both spaces: write-position [0,gap); nominal {0–198} fabricate / ~198.3 transition / ≥198.5 never |
| divergence receipt | per-row `divergent` bool | exact per-row clause tuples (9-row map incl. multi-clause `seam_script`→(blob,error_scan)) + sha256 same-input gate |
| discriminations | 20 | **24** (all True) |
| battery (flagless) | 88/88 | 88/88 (unchanged — opt-in only) |
| battery (both flags) | — | **90/90** |

## SHONEN

- [x] Declared falsifiable axis-move (depth/calibration); declared-grid wording falsified-as-written and corrected semantics landed
- [x] Named non-author replay — **verifier AGREE 5/5** on `f754546` (prior rows 0-mismatch ×5 comparisons; post-verifier `e8d4fb7` is byte-identical-proven)
- [x] No axis harmed — flagless 88/88 unchanged; classifiers byte-identical since r65; upgrades opt-in flagged
- [x] Bounded claims (nominal-offset space on this host; edge ~198.3–198.5 stochastic ~1ms; receipt fields bind decoded text; timeout records nondeterministic)
