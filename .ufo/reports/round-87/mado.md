# mado — round 87 report (hyaku run 15, attempt 1)

Lane repo `mado-shokunin`, branch `master`. Lane HEAD at report time: `f4dfd0a9bd54d5bad518e58297c9b222f6be9b62` (pushed; `ls-remote origin refs/heads/master` matches). Measured revision: `00c967214e338d8f0ebb02b78f98fd61a542a515`. Content commit: `7563452f9b35af0141c49dc4cc7f791968ca0c90`. Base: `e4875ba5619053cc3f91bb2f4d819e189df4088c`.

## Work performed

**Declared claims (frozen in `.ufo/waves/round-87/claims-declaration-r87.md`; pre-scoring errata appended):**

- **C1 — capability, axis coverage (frontier → core).** Mako effective settings for one notification (the `include=` chain, criteria AND, per-option last-wins, the mode gate). Stagnation nudge applied: every axis at 10 and no capability row since round 82. **Verdict: TARGET_MISSED.** The tool answers 22/22 frozen cases and both do-nothing controls fall below N, but 5 of 10 frozen mutants are killed. Predicate requires all ten.
- **C2 — calibration (self-assessment vs observed state).** The r86 held-rule control figure `0/1` (entry line 112, SCORECARD r86 C2 row) re-derives as `1/1` from the held round-85 counter. **Verdict: TARGET_MET** (before 5.0 `TARGET_MISSED`, after 10.0).

**Work items (evidence pointers):**

- Round-start baselines: census exit 0, 427 rows (`.ufo/waves/round-87/receipts/census-start-r87.txt`); index 107/107; ledger 158/158; gate selftest 460/460; file plane CLEAN (`receipts/`).
- Wave `w1` (v1, band 8–16): **12 seats** — scout 1, executor 3 (`R87ExecMako`, `R87ExecCounter`, `R87ExecFidelity`), scribe 2, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1. Attack share 4/12 = 33 %. Dispatched once (`w1-dispatch.json`), `WAVE-DONE` received, `w1-results.json` (12 settled, 0 dead seats, 0 residual calls; round total 12). Seat reports: `.ufo/waves/round-87/w1/`.
- The scout pinned the mako 1.11.0 manual (`/usr/share/man/man5/mako.5.gz`), derived the grammar with manual line numbers, and authored the frozen case set (22 cases, `controls/mako-cases-r87.json`, sha256 `0a9558743a721f70bb64b48d188b375f1468a140b00ca75ac93ab59c316d5fe3`). The executor wrote `tools/mado-mako.py` (stdlib, read-only, selftest 29/29) and ten mutants (`controls/mako-mutants-r87.json`) without reading the case file.
- Attack seats: reviewer `R87ReviewMako` (22/23 on its own early case bytes; findings D1–D3, G1), reviewer `R87ReviewFidelity` (HIGH R87RF-D1: F2 stated text wraps across SCORECARD lines), critic `R87Critic` (C1 "not held" wrong; manual pin label wrong; C2 correction-disjunct weakness), mutation-tester `R87MutTester` (19 added mutants; 14 survive the early case bytes), sentinel `R87Sentinel` (case-file schema and C13 path defects on the early bytes; `$HOME` fallback; containment).
- Repairs before scoring (all disclosed as errata in the declaration): tool `$HOME` fallback removed and `--home` required; bare `none`/`invoke-default-action` refuse trailing words; refusal wording; figure F2 re-pointed to a single line; manual pin corrected (container `17ffc88c…`, text `f717848f…`); "Not held" withdrawn; case-file rewrite during the wave recorded (final bytes scored); C1 counter accepts upper-case mutant ids (`00c96721`).
- Measured C1 and C2 at `00c96721` (receipts below). Base `e4875ba`: C1 `SETUP` (no tool at base, `receipts/c1-base-r87.txt`); C2 fixture with the base correction blocks: 5.0.
- Frontier step: S493 opened (2026-11-05), knowledge entry `corpus/knowledge/mako-criteria-resolution-r87.md` (sourced claim, S493), mistakes mined (`corpus/lessons/round-87.md` `## Mistakes`, M87-1–M87-5), correction blocks appended (`corpus/knowledge/refusal-records-clause-observations-r86.md` and `SCORECARD.md`, heading `## Correction (round 87 — held-rule witness figure)`).

## Landed changes

| change | commit | log / record |
|---|---|---|
| `tools/mado-mako.py` (read-only resolver), `quality/counters/c1-r87-mako-criteria.py`, `quality/counters/c2-r87-control-fidelity.py`, `.ufo/waves/round-87/` (declaration, controls, figure file, wave evidence, receipts), knowledge entry, S493 row, r86 correction blocks, README/PROVINCE/ledger rows, lesson | `7563452f9b35af0141c49dc4cc7f791968ca0c90` | LOG round 87 |
| C1 counter accepts upper-case mutant ids (pre-score setup repair) | `00c967214e338d8f0ebb02b78f98fd61a542a515` (measured revision) | LOG round 87 |
| measurements, lesson census and measurements, SCORECARD round-87 section, LOG round-87 entry, measurement receipts | `f4dfd0a9bd54d5bad518e58297c9b222f6be9b62` (lane HEAD) | LOG round 87; SCORECARD `## Round 87` |

## Before → after measurements

Counting commands (run from the lane root; `DIR` is a scratch directory):

- **C1**: `python3 -I quality/counters/c1-r87-mako-criteria.py --repo . --rev 00c967214e338d8f0ebb02b78f98fd61a542a515 --cases .ufo/waves/round-87/controls/mako-cases-r87.json --scratch-root DIR`
  - Base `e4875ba5`: `MADO_MAKO_CRITERIA: SETUP_ERROR … tools/mado-mako.py … not in e4875ba5…`, rc 2 (`receipts/c1-base-r87.txt`).
  - `00c96721`: `MADO_MAKO_CRITERIA: TARGET_MISSED rev=00c96721… cases=22 correct=22 mutants=10 killed=5 naive_correct=7 globals_include_correct=8 score=10.0000`, rc 1 (`receipts/c1-measured-r87.txt`). Survivors: M03, M05, M06, M08, M10.
- **C2**: `python3 -I quality/counters/c2-r87-control-fidelity.py --repo . --rev 00c967214e338d8f0ebb02b78f98fd61a542a515 --figures .ufo/waves/round-87/controls/r86-figures-r87.json --expect-figures-sha256 f206a75907e385fc957aef07c8e1e2037b1328d5d1bcbfbd03c7201bc0b46ea6 --scratch-root DIR`
  - Before (scratch fixture: base correction blocks, `receipts/c2-before-r87.txt`): F1 `reproduced=no reconciled=no`; `MADO_FIGURES: TARGET_MISSED … score=5.0000`, rc 1.
  - After (`receipts/c2-after-r87.txt`): F1 re-derived `1/1`, reconciled by the correction block; F2 `flooding 48/75; held 75/75` reproduces; `MADO_FIGURES: TARGET_MET … score=10.0000`, rc 0.
- **Harm watch** at `00c96721`: index `108/108` (before 107/107); ledger `population=161 uncovered=0` (before 158); standing gate `MADO_SELFTEST: 460/460`; file plane `MADO_VERIFY: CLEAN (29 pass, 4 notes)`; census exit 0, 428 rows (427 before), 55 standing `W04` warnings before and after. Receipts: `.ufo/waves/round-87/receipts/`.

## Sources & frontier

- `corpus/SOURCES.md` rows before → after: **427 → 428** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` exit 0 at start and end; `receipts/census-start-r87.txt`, `receipts/census-end-r87.txt`). Rows added by tier: **S493, tier A** (docs). Rows touched old→new: none (no status, recheck or used-by changed).
- Frontier rows advanced: S493 (mako 1.11.0 manual) opened 2026-11-05; the knowledge entry cites it; the C1 claim rests on it (sourced claim). Mined mistakes: M87-1–M87-5.
- Assimilation: none (`merge/mado` holds no mako theme; `host-producer-outputs-r29` already held). Considerthese: proposal 7 (relayed/re-measured figures) is already held by QUALITY criterion 76; no new criterion added.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry (`mako-criteria-resolution-r87.md`) on a surface the held notes observed only by hand; S493 cited. No capability row entered (C1 missed), so no capability credit.
- **quality — improved.** A false figure in an admitted entry (`0/1`, r86 line 112) is superseded by an append-only, measured correction (`1/1`), reproduced by the counter. The tool's defects found by the wave (D1, D2) are fixed before scoring.
- **discernment — unchanged.** The non-author spot-check of this round's gate decisions is not yet recorded (pending the operator-dispatched closure). The outside attack seats found defects the L1 had not caught (the pin label, the F2 wrap, the "Not held" basis); the L1 accepted them with errata. That is recorded here, not counted as agreement.

## Named limits and routed defects (round 88)

- C1 mutant survivors M03 (relative include accepted), M05 (initial mode), M06 (defaults), M08 (missing input match), M10 (unterminated quote) — next: a superseding case set. The frozen case set was not extended after scoring.
- Symlinked includes escaping HOME are read: the manual allows absolute include paths and states no containment rule.
- Correction blocks are checked for figure id and literal value, not reasoning; the r86 selftest pin (`c2-r86-clause-observations.py:736-737`) is outside the predicate.
- The declared command's sha pin was missing; the measured runs pass it.

## Other extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Installs: none. Read-only queries only (`pacman -Q mako`, `pacman -Qkk mako`, `pacman -Qi mako`). No pacman transaction.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/run15-state.json` (orchestrator-owned, not touched) and three untracked files (`cited-lines.txt`, `run_check_probe.py`, `run_check_probe2.py`) that name other lanes' seats (kengaku r90 paths) — not mine, not moved. No round-87 seat wrote into the fleet root.
- Scratch: all round scratch under `/fast/scratch/hyaku/mado-r87/` and removed on exit.
- Open L0 questions: none added this round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/mako-criteria-resolution-r87.md` §1 (grammar table, manual lines); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` round 87 (mako resolver measured on the frozen case set, `receipts/c1-measured-r87.txt`); no non-author verifier.
- [~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/mako-criteria-resolution-r87.md` and `tools/mado-mako.py` header (manual line map); no non-author verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` round-87 refinement (read-only, no new write surface); no non-author verifier.
