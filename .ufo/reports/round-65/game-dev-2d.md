# game-dev-2d round 65 — depth move: forged-REJECTION dual (post-death ERROR: flips a genuine PASS→FAIL)

**Stamp.** Game-dev-2d lane, round 65 (devin host, wave `shokunin-train-20261013-w5`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `414eb8e`, report-last `44b6d2b` + boundary `b8a5a04` + hygiene `37b4…` — identity `game-dev-2d-shokunin`.

## Work performed

XConnector Arm 1 measured: a reparent-gated descendant emits an un-allowlisted `ERROR:` marker after parent death into held pipes; the merged classifier flips a clean exit-0/signature-present record to **rejected** — the reject-axis dual of r63's accept-axis forgery. Sole cause pinned by counterfactual strip; forged-vs-genuine records identical on classification-visible fields (quiet arm removes even provenance); hold arm rejects on the timeout axis alone after stripping (`hold_timeout_alone_rejects`, 29th discrimination, simplifier add landed at integration). The r64 while-live signature gate ACCEPTS the forged-error arm — rejection stays in the un-gated classifier; the remedy direction inverts (error-axis protection must exclude post-death bytes, not reject them).

## Landed changes

- `descendant_pipe_probe.gd` +35 (`--spawn-errforge-{release,hold}`, `--emit-errforge`), `run_battery.py` +467/−0 (`probe_descendant_error_spoof` meta: release/hold/genuine records, dual-marker gated reps, stream-split arms, 29 discriminations).
- `corpus/lessons/r65-forged-rejection-dual.md`; `reports/round-65/` — 8 seats + verifier + adjudicator.
- Absorbed: critic CE-1 (operative precondition is capture-before-pipe-EOF, not death ordering — detach arm stays PASS) and CE-2 (merged concat not line-faithful — splice fabricates reject lines); boundary edges (newline-split evasion, allowlist admittance, reader-drain/memory surface, 64.4 GB/3 s pump).

## Before → after measurements

| metric | before | after |
|---|---|---|
| forgery surface | accept-axis only (r63) | **both axes symmetric** — manufactured PASS and FAIL on identical fields |
| discriminations | — | **29/29 True** (incl. sole-cause strip, kernel-ppid corroboration, gate-blindness) |
| battery | 97 rows | **87/87 verdicts + meta**, prior 97 rows 0-mismatch |
| gate coverage | signature-scoped | measured verdict-blind to forged errors (mirror-image divergence) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), claim confirmed by measurement
- [x] Named non-author replay (AGREE 6/6, committed-state, independent /proc corroboration)
- [x] No axis harmed (purely additive meta; prior rows field-stable)
- [x] Bounded claims; UNKNOWNs retained (line-faithfulness, live-window forge, stream-faithfulness)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
