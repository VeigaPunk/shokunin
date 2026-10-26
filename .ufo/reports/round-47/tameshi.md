# Tameshi — round 47

author: tameshi L1 TameshiR47 (hyaku run 7, attempt 1)
date: 2026-10-25
lane HEAD: `663e068287a19ebfeabfefec10620957b3dad0f4` (`master`; `jj-lane.sh state` local=remote, ahead=0; `git ls-remote origin refs/heads/master` prints the same hash)
content revision (deciding runs): `8b0e15d25ea598c0bf908d183fb410a085bf3a18`; freeze `9acfbe21435e1976636a276448dee1d5e7155915`; base `0b5b7cd2b2c15d23086e811a0f0348d84261277b`

## Work performed

Declared claims (frozen at `9acfbe21…`, `.ufo/evidence/round-47/contract.json`, `amendments: []`), three distinct axes, none exploratory: **C1 calibration** (lowest non-retired axis, monitor 6) — the 22 standing SCORECARD rows state value, exit, tool sha256 (22 of 22; 17 before) and a `deps` clause equal to the dependences observed under six profiles; **C2 operability** — the v2 hardened counters kill at least 150 of 183 pool mutants (baseline 122) and none of 14 neutral ones; **C3 coverage** (sourced, assimilation, F3 measurement half) — rows for arXiv 2302.09330, arXiv 2607.09345 and the Semantic Scholar ICST 2024 record, each cited by a re-grounded, indexed entry.

- Freeze (before any seat): three counters with selftests (C1 35/35, C2 pool 14/14, C3 24/24), statements v2, the 183+14 deterministic mutant pool (`hardening/pool.json`), controls CTL_A–K with receipts (`control/controls-at-freeze.stdout`), snapshots, package copies, no-harm at base (7 ok). Do-nothing/cheapest controls: C1 unchanged tree `total=22`, all rows `deps none` `dep_mismatch=5`, positive control `total=0`; C2 unchanged `killed=122`, AST pin `neutral_killed=14`, bare-assert pin `killed=0`, always-fail `pristine=0`; C3 byte-exact/relabelled/rows-only `entries=0`.
- Wave 1 (40 seats, all 40 reported): C1 observation seats (five) found 5 of 22 statements dependent; nine C2 executors wrote the selftest additions (`.ufo/waves/round-47/w1/T47Hard*.addition.py`); three scribes re-grounded the entries, one the rows; id guard, mirror dry run, held/quarantine/province/predicate reviews, mutation audits of the three counters, dead-code scan, mistake mining. Findings that changed the round: `T47CritC2Control` showed the frozen C2 counter is passable in-band by an embedded differential oracle (160/183, neutral 0) → `quality/addition-lint.py` added to the deciding run (disclosed; counter, pool and target unchanged); `T47CritC1Control` showed the pins are self-referential → the deciding script's frozen diff now covers `tools/` and the pinned evidence dirs.
- Assimilation: theme "F3 measurement half" from `merge/tameshi` (staged S155→S261, S158→S262, S206→S263, S207→S264 by document; S155/S158 collide with held rows); considerthese 2026-10-25 idea 3 mined (dead-code scan: 2 unreferenced helpers, routed). Quarantine slice 17 rows; S110 (= the Lam PDF) hand-checked and adopted as S262.
- Mistake mined with a red-before checker: `quality/lesson-quote-check.py` + QUALITY 91 (round-46 lesson exits 1, one-character repair exits 0: `quality/c91-lesson-quote-red-green.stdout`); QUALITY 92 and 93 appended with falsifiers (`quality/falsifiers.sh`, receipt `c91-92-falsifiers.stdout` taken before 91 was added to the script).
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): only `.ufo/state/tameshi.report-baseline` (driver file, untouched); no seat file at the fleet root. Inherited state: none. Stale-lane: respawn-per-round; no other mission open. Tools installed/updated: none (pacman paused; nothing needed).
- Host incident: `/tmp` reached 100% mid-wave (each C1 counter pass clones the lane twelve times, ~2.3 GB; one seat held ~20 GB); seats relocated to `/var/tmp`, two probe runs died on ENOSPC and were rerun, none scored.

## Landed changes

All tied to the LOG.md entry `## 2026-10-25 — round 47`; every hash is a helper `landed` line verified on the remote:
- `9acfbe21435e1976636a276448dee1d5e7155915` — freeze.
- `a944eb55d64a2e0a77e3561c44bf89faadf04bb9` — before receipts, deciding script, falsifiers, wave-1 spec and dispatch.
- `8b0e15d25ea598c0bf908d183fb410a085bf3a18` — content revision: rows S261–S264, three entries, README block, v2 counters, SCORECARD standing tables, QUALITY 91–93, lesson, LOG, wave-1 evidence.
- `edd4ca44635c9fdf796a4c11953b37481e753537` — deciding receipts and the unrun wave-2 spec/dispatch (`git diff --name-only 8b0e15d2 edd4ca44` outside `after/`, `census-end.*`, `.ufo/waves/round-47/` → 0 paths).
- `663e068287a19ebfeabfefec10620957b3dad0f4` — SCORECARD deciding results and the C1 miss errata (records only).

## Before → after measurements

- **C1 calibration — MISS.** `python3 .ufo/evidence/round-47/calibration/measure.py --lane LANE --rev REV --base 0b5b7cd2b2c15d23086e811a0f0348d84261277b --work EMPTY_DIR`. Before at freeze (exit 1): `unparsed=22 total=22 C1_R47_PASS=false`. After at `8b0e15d2…` (exit 1, `after/c1.stdout`): `mismatches=1 dep_mismatch=1 total=2 C1_R47_PASS=false`. The one statement is `six-leg regression ledger`: the content-revision `--emit` the row restates caught a flaky P0 run (`FAIL (cases=9 passed=7`); the deciding run printed `PASS (cases=9 passed=9`, deps `fleet-root,node`. The other 21 rows matched, 17 with `deps none`. Target not narrowed; row not edited after the run (errata appended). Instability evidence: `hermetic env-differential probe` printed 9/9 or 2/9 under the same profile across runs, so two of 22 observations are load-sensitive; the counter cannot separate that from a dependence.
- **C2 operability — met.** `python3 .ufo/evidence/round-47/hardening/pool.py --lane LANE --rev REV --targets v2`. Before (`--targets base`): `killed=122` of 183. After at `8b0e15d2…` (exit 0, `after/c2.stdout`): `killed=183 applicable=183 neutral_killed=0 pristine=2 equivalence=1 C2_R47_PASS=true`; `HARDENED_REBUILD=1`, `ADDITION_LINT_OK=1` (no embedded oracle, no pin: nine additions). Limits: the frozen counter alone is passable by an oracle (disclosed, lint closes it for these additions); no fresh-mutant generalization was measured (wave 2 did not run); 183/183 includes mutants the baseline classed unkillable-looking, which no non-author has yet re-sampled.
- **C3 coverage — met.** `python3 .ufo/evidence/round-47/coverage/measure.py --lane LANE --rev REV`. Before: `rows=0 entries=0`. After (exit 0, `after/c3.stdout`): `rows=3 entries=3 indexed=3 covered=3 row_ids=S261,S263,S264 C3_R47_PASS=true`, `ENTRY_NAMES_OK=1`. S262 is an uncounted fourth row. Expansion credit: all three on ground `T47ScoutHeld` found unheld.
- **No-harm** at base and at `8b0e15d2…`: seven monitors ok (`after/no-harm.stdout`), cold-read sections 60, census exit 0 (`census-end.exit`), `FROZEN_UNCHANGED=1`.

## Sources & frontier

`SOURCES.md` census-valid rows 120 → 124 (`grep -cE '^ {0,3}\| S[0-9]{3,} \|' corpus/SOURCES.md`). Rows added by tier: A=3 (S261, S262, S263), B=1 (S264), C=0; all mined, opened 2026-10-25. Rows touched old→new: none. Frontier: F3 gains the prediction, rerun-price and cost documents; F3 and F7 stay `open`. Sourced claim: C3. Assimilation: theme above; admitted 4 rows / 3 entries; refused: `r14-quarantine-threshold-is-a-policy`, `r13-flaky-false-red-rate`, `r12-flaky-mitigation-and-quarantine`, `r8-gtest-order-and-seed`, `r8-predictive-test-selection-cost` (reasons and flips in `corpus/lessons/round-47.md` `## Gate`). Id check: `reg-ids` 120, `staged-ids` 103, `collisions` 8 (S153–S160); renumber map by document S155→S261, S158→S262, S206→S263, S207→S264; guard `verdict=answered`, proof-it-can-fail in `w1/T47ExecIdGuard.receipts.md`. considerthese: idea 3 of 2026-10-25 mined. Mined mistakes: 5 rows. Census start (exit 0, `census-start.stdout`) and end (exit 0, `census-end.stdout`): same 11 warnings, 124 rows at end.

## Trend verdicts

- **expansion: improved** — three admitted entries on ground the coverage map did not hold (prediction from recorded history, rerun budget, non-static flakiness, cost of a failed pipeline), each citing a newly mined row (0 → 3 rows/entries by the C3 counter).
- **quality: unprovable-but-better** — the pool kills 183 of 183 (122 before) with the lint and quote checker added, but no non-author has re-sampled the kills and no fresh-mutant generalization was measured; one standing row states a flaky observation (C1 miss), recorded as errata.
- **discernment: unchanged** — no non-author spot-check has run on this round; the round-46 routed defects became QUALITY 91–93 and a frozen-diff widening, which is not yet checked from outside.

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited sources — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-1`; no new independent verifier.
- [~] At least one end-to-end domain task executed and logged — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-2`; no new promotion verdict.
- [~] Instructions executable without oral context — prior pointer `tameshi-shokunin/.ufo/evidence/round-21/coldread/ledger.json`; monitor unchanged (6, 60/64 credited at `8b0e15d2`), no independent promotion verifier.
- [~] No cross-domain bleed — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-4`; per-entry PROVINCE gate in `.ufo/waves/round-47/w1/T47RevProvince.md` (lane-dispatched, not independent).

**Round shape:** one v1 wave actually ran; a second v1 wave (32 seats, `.ufo/waves/round-47/spec-w2.json`, `w2-dispatch.json`, built and validated at `8b0e15d2`, 12 critic/6 reviewer/8 executor/4 mutation-tester/1 scout/1 connector) was **planned and not dispatched**: the orchestrator reported the spawn cap at 0 and wrapped the run up. Round total **40 seats, below the 64–100 floor**; the falsification wave did not run, so no attack of the entries, the additions or the restated rows by fresh seats exists. No residual call. §3 planner seat held by the L1.
- w1, 40 seats: 19 executor, 5 scribe, 4 critic, 4 reviewer, 3 mutation-tester, 3 scout, 2 connector (m_flash roles 28 of 40); all 40 reported (`w1-results.json` was never written by the orchestrator; counted from the 40 reports under `.ufo/waves/round-47/w1/`). Dead seats: none (two probe runs died on ENOSPC and were rerun by their seats).
- Dispatch: w1 spawned by the orchestrator from `w1.ready`; `w2.ready` removed before dispatch.
- Open L0 questions filed this round: none.
