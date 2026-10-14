# game-dev-2d round 63 — depth move: merged-stream signature-spoof forgery boundary

**Stamp.** game-dev-2d lane, round 63 (devin host, wave `shokunin-train-20261013-w3`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `de78edb`, report-last `a7e0cb1` — identity `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`.

## Work performed

Pinned the r62-critic-measured signature-spoof as a tracked known-accepting boundary. `classify_process` matches `signature in output` over merged `stdout+stderr` — presence-only, origin-blind. Landed: `descendant_pipe_forged_signature_release` CASES row (post-death descendant signature + pipe release before bound → **PASS on a signature the child never emitted**) + `probe_descendant_signature_spoof` meta (hold arm → forged signature inside a TIMEOUT record, rejected via error axis only). Boundary is documented-accepting, not fixed — a policy decision for a future round.

## Landed changes

- `corpus/fixtures/descendant_pipe_probe.gd` +31/−1 (`--spawn-forge-hold`/`--spawn-forge-release`, child withholds signature, reparenting-gated post-exit write with `write_ppid=` echo) + `run_battery.py` +189/−0 (CASES row + meta, **10 discriminations**). Classifier internals byte/ast-identical.
- `corpus/lessons/r63-signature-spoof-boundary.md`; `reports/round-63/` — 8 seat reports + verifier + adjudicator.
- Integration corrections (critic-driven): `hold_write_ppid_kernel_corroborated` (kernel `/proc` ppid == self-reported reparented ppid ≠ godot pid — closes the fabricated-`write_ppid` slip that scored 8/8 pre-fix) + `release_withheld_banner_present` (provenance anchor).

## Before → after measurements

| metric | before | after |
|---|---|---|
| seven-flag battery | 94/94 (frozen `edbd945`) | **96/96** |
| prior rows | — | **94/94 field-identical** (0 mismatches vs r62 non-author receipt) |
| signature attribution | presence-only, unpinned | forged-PASS row + forged-TIMEOUT meta both tracked; provenance fields named |
| forgery surface | depth-1 measured | **depth-agnostic** (boundary: doubly-orphaned grandchild forges PASS) |

## SHONEN

- [x] Declared falsifiable axis-move (depth), evidence over prose
- [x] Named non-author replay passed all old + new classifications (96/96, fabricated-ppid spot-check caught)
- [x] No axis harmed (additive-only; classifier untouched)
- [x] Bounded claims; UNKNOWNs retained honestly (receipt-level provenance, release-arm kernel check impossible, subreaper host-specific)

Per-axis verdicts (Sol): depth **improved locally**, coverage **improved locally**, calibration **unchanged**. No promotion action.
