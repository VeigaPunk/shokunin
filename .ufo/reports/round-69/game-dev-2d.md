# game-dev-2d round 69 — depth move: fabrication-window referent pinned gap-relative (crossed cells refute absolute edge < ~602ms) + sha256(merged) receipt

**Stamp.** Game-dev-2d lane, round 69 (devin host, wave `shokunin-train-20261014-w9`, 8-lane seat set + Sol adjudication). Lane commits: work `ec2cda6`, report-last `9fb50aa`.

## Work performed

Pinned the midlineforge fabrication-window bound's REFERENT: `--midline-gap-ms=N` fixture flag (default 200 — r66/r68 arm byte-stable) + `--probe-midlineforge-gapladder` battery meta. The declared fixed-offset 5-gap grid was **co-predictive** under gap-relative vs absolute-edge models (critic falsification) — the crossed cells (300,400)/(300,800)/(600,800) are the only distinguishing region and were folded into the TRACKED ladder at integration: 8 cells × 3 reps, `referent_verdict` 3-way {gap_relative, absolute_edge, absolute_write_latency}.

**Measured: referent = the gap.** Splice lands iff descendant write pos ∈ [0, gap) — 0/268 byte-order exceptions (scribe). Crossed cells all fabricate 3/3 (operator replay + reviewer + scribe) → any absolute edge <~602ms refuted; edge re-located ~295–300 at gap=300 (edge ≈ gap − overhead at BOTH gaps); boundary knife-edge at off=80: miss ≤81 / mixed 82 / fabricate ≥83 — the write position IS the edge; jitter floor ~2–5ms (absolute achievability bound inside the window); no ceiling (gap=1500 fabricates). `write_ppid` = provenance only; byte order is ground truth.

**Receipt upgrade**: `raw_merged_sha256 = sha256(so+se)` on every dual_classify record + same-input gate — binds concat order/separator (boundary measured it concat-order-blind on only 9/118 records — power lives on two-stream arms).

## Landed changes

- `descendant_pipe_probe.gd` +18 (`--midline-gap-ms`); `run_battery.py` +271 (ladder meta + crossed cells + raw_merged_sha256).
- `corpus/lessons/r69-fabrication-window-referent.md`; `reports/round-69/` 8 reports + adjudicator.

## Before → after measurements

| metric | before | after |
|---|---|---|
| fabrication bound referent | write-position bound [0,~198ms) at fixed gap (r68) | **gap-relative** — the ~198ms edge resolves to `gap − spawn_overhead`; crossed cells refute absolute edge <~602ms |
| tracked discrimination | fixed-offset grid (co-predictive) | crossed cells in-band — `crossed_cells_refute_absolute_edge` discrimination |
| merge integrity | per-channel sha256 only | `raw_merged_sha256` on all dual records (concat-order binding) |
| flagless surface | 88/88 + 34/34 | **unchanged** |

## SHONEN

- [x] Declared falsifiable axis-move (depth); referent claim CONFIRMED in measured semantics
- [x] Non-author replay — verifier seat lost to rate limits; operator adjudicator replay on `ec2cda6` (88/88 + gapladder PASS + crossed 3/3) + reviewer replay green (sha256 equality all records) + scribe 268-run own-harness
- [x] No axis harmed — flagless 88/88 + surface 34/34 + prior rows byte-stable modulo the additive field (baseline + reviewer)
- [x] Bounded claims (Godot 4.7.2 headless; POSIX pipes; referent portable, nominal edges not; write_ppid provenance-only)
