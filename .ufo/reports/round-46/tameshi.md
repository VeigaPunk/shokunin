# Tameshi — round 46

author: tameshi L1 TameshiR46 (hyaku run 7, attempt 1)
date: 2026-10-25
lane HEAD: `b5425635961c3279c1bca95b8b42ca3816825df4` (`master`; `jj-lane.sh state` local=remote, ahead=0; `git ls-remote origin refs/heads/master` prints the same hash)
content revision (deciding runs): `3ae8b0484977c17dc9ce8b01e55c6afcebe2b116`; freeze `745a583181648cfc7f9c1b476cd1be7dc68f7433`; base `683eedde3a50441c34d85a22f5fd5346f8b1ec6d`

## Work performed

Declared claims (frozen at `745a5831…`, contract `.ufo/evidence/round-46/contract.json`, `amendments: []`), three distinct axes, none exploratory:
**C1 calibration** (lowest non-retired axis, monitor 6) — the last standing SCORECARD row of each of 22 frozen statements states what its frozen command prints (value, exit code, tool sha256 prefix). **C2 operability** — the round-45 counters' selftests kill ≥23 of 25 declared survivors and none of 6 neutral mutants. **C3 coverage** (sourced, assimilation, frontier F3) — rows S258/S259/S260 each cited by a re-grounded, indexed entry.

- Built three counters with selftests (C1 18/18, C2 8/8, C3 24/24; `.ufo/evidence/round-46/selftest/`), the sha256-pinned statements list, a declared mutant manifest (25 + 6 neutral), controls and base receipts, all committed at the freeze before any seat. Controls: package entries byte-exact / relabelled / rows-only → `entries=0`; length-pinning selftest → `neutral_killed=6`; unchanged round-45 counters → `killed=0` (`control/controls-at-freeze.stdout`). No-harm monitors all ok at base (`before/no-harm-at-base.stdout`).
- Wave 1 (37 seats): 7 executors re-observed all 22 statements twice (stable); 6 executors wrote selftest additions (`.ufo/waves/round-46/w1/Hard*.addition.py`), assembled by `hardening/assemble.py`; 3 scribes re-grounded the entries, one drafted the rows; critics, reviewers, mutation-testers and a mirror dry run attacked the counters; ExecRegressionClasses grounded considerthese proposal 2 (no older record-agreement class regressed; all 5 hits are by-construction false positives).
- Wave 2 (35 seats, `T46`-prefixed names): re-observation of all statements at the content revision, claim critics, entry reviewers and critics, four mutation-testers with 73 fresh mutants, landing/separability/quality/gate reviews. Findings fixed in place before the deciding runs: a false carrier rationale for S260, inference stated as observation and overreach in all three entries (one BLOCKING), the stale id ledger, `deciding-run.sh` reading the worktree, and a `PROVINCE.md` append that cost the cold-read monitor 5 credited sections (60 → 55; reverted). The rest is recorded as SCORECARD errata and routed (`SCORECARD.md` "Round 46 — wave-2 results, errata and disclosed limits").
- Assimilation: theme "flaky-failure evidence for F3" from `merge/tameshi/`; considerthese proposal 2 mined (lesson table + C1). Quarantine slice 17 rows, none adopted, no new verdicts.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no pathspec): only `.scratch/goal-20261025-hyaku-run7.md`, untracked `.ufo/waves/round-30/` and `.ufo/waves/round-41/w1/ExecQuarantineSlice.md`; none names tameshi round 46, left alone. Inherited state: none.
- Stale-lane: respawn-per-round; no other mission of this lane is open. Tools installed/updated: none (pacman paused; nothing needed).

## Landed changes

All tied to the round-46 LOG.md entry (`## 2026-10-25 — round 46`); every hash is a helper `landed` line verified on the remote:
- `745a583181648cfc7f9c1b476cd1be7dc68f7433` — freeze: contract, counters, statements, manifest, controls, snapshots, guard receipts.
- `10a05fdf56d210988a30cf1a0a9dcd349441ba1a` — before receipts, assembler, wave-1 spec and dispatch.
- `a6892b196f923efbed242ce9ea599a3f745b2138` — wave-1 evidence, hardened counters, rows S258–S260, three entries, README index.
- `e630ae791a831828f51b8f192996a907ff8ed78d` — SCORECARD standing tables, QUALITY 88–90, deciding-run script.
- `6f2168e028ce7ff6e82ac92093ac05dd1f147c32` — first content revision (wave-2 target): lesson, LOG, SCORECARD block.
- `eada0b36d4c9e6380d111d2037acd97cdf91d2eb` — wave-2 spec and dispatch.
- `3ae8b0484977c17dc9ce8b01e55c6afcebe2b116` — content revision: wave-2 evidence, corrections, errata, `PROVINCE.md` reverted.
- `b5425635961c3279c1bca95b8b42ca3816825df4` — deciding receipts only (`git diff --name-only 3ae8b048 master` outside `after/` and `census-end.*` → 0 paths).

## Before → after measurements

- **C1 calibration.** `python3 .ufo/evidence/round-46/calibration/measure.py --lane LANE --rev REV --base 683eedde3a50441c34d85a22f5fd5346f8b1ec6d --work EMPTY_DIR`
  - Before at freeze (exit 1): `statements=22 mismatches=2 unparsed=19 unobservable=0 append_only=1 total=21 C1_R46_PASS=false` (calibration stated 8 vs observed 6; regression row truncated).
  - After at `3ae8b048…` (exit 0, `after/c1.stdout`): `self_pin=1 stmts_pin=1 statements=22 mismatches=0 unparsed=0 unobservable=0 append_only=1 total=0 C1_R46_PASS=true`.
  - Calibration monitor 6 → 6: no raise claimed. Caveat: three statements are host-dependent (census over the live fleet root, `jj`/`bwrap` on PATH); a later one-line counter edit passes `self_pin`, so the deciding run adds `FROZEN_UNCHANGED=1` (`after/frozen.stdout`).
- **C2 operability.** `python3 .ufo/evidence/round-46/hardening/mutate.py --lane LANE --rev REV --targets hardened`
  - Before (`--targets orig`, exit 1): `declared=25 killed=0 survived=25 neutral_killed=0 C2_R46_PASS=false`.
  - After at `3ae8b048…` (exit 0): `declared=25 killed=25 survived=0 neutral_killed=0 pristine=1 equivalence=1 C2_R46_PASS=true`. Supplementary (`after/extra-receipts.stdout`, `EXTRA_RECEIPTS_BAD=0`): strict unmasked equivalence identical for both counters; 25 of 25 kills by a named rule case.
  - Honest limit: 73 fresh mutants from wave 2 → 17 killed, 56 survived (the additions pin the declared rules and little more); routed. The 0→10 score is definitional; the comparable measure is `killed 0 → 25 of 25`.
- **C3 coverage.** `python3 .ufo/evidence/round-46/coverage/measure.py --lane LANE --rev REV`
  - Before: `rows=0 entries=0 indexed=0 covered=0 C3_R46_PASS=false`.
  - After at `3ae8b048…` (exit 0): `rows=3 entries=3 indexed=3 covered=3 row_ids=S258,S259,S260 C3_R46_PASS=true`; `ENTRY_NAMES_OK=1`.
  - Expansion credit: 2 of 3 entries on unheld ground; the false-red entry restates a held claim through a second, byte-stable carrier.
- **No-harm** at base and at `3ae8b048`: all six monitors ok (`after/no-harm.stdout`), cold-read sections credited 60 (`after/coldread-sections.stdout`), `HARDENED_REBUILD=1`, census exit 0 (`census-end.exit`). Deciding script exit 0 (`DECIDING_RUN_EXIT=0`).

## Sources & frontier

`SOURCES.md` census-valid rows 117 → 120 (`grep -cE '^ {0,3}\| S[0-9]{3,} \|' corpus/SOURCES.md`).
- Rows added by tier: A=3 (S258, S259, S260; mined, opened 2026-10-25, recheck 365d, snapshot-pinned), B=0, C=0. Rows touched old→new: none of earlier rounds (S258/S260 cells were corrected in place before the deciding run, same round).
- Frontier: F3 gains two unheld measurements and a pinned carrier; stays `open`. Sourced claim: C3.
- Assimilation: theme "flaky-failure evidence for F3"; admitted 3 (staged S195→S258, S190→S259, S216→S260); four package claims dropped and three package entries not adopted, each with reason and flip (`corpus/lessons/round-46.md` Gate).
- Id check: `reg-ids` 117, `staged-ids` 103, `collisions` 8 (S153–S160); renumber map S153→S105, S154→S106, S159→S155, S160→S156, map-only S155–S158→S261–S264, adopted as above; guard verdict admitted at the freeze, guard proof for the indented row in `assimilation/guard-proof-collisions`.
- considerthese: proposal 2 of 2026-10-25. Mined mistakes: 9 rows in the lesson.
- Census start (exit 0, `census-start.stdout`) and end (exit 0, `census-end.stdout`): same 11 W04/W01 warnings, 120 rows at end.

## Trend verdicts

- **expansion: improved** — two admitted entries on ground the lane did not hold (clustering, the same-job-rerun blind spot), each citing a newly mined row (counter 0 → 3 rows/entries).
- **quality: improved** — 22 standing statements now machine-checked (21 → 0), 25 declared survivors killed, and wave 2 corrected prose overreach in all three entries before landing; limit: fresh-mutant generalization is poor (17 of 73).
- **discernment: unprovable-but-better** — the lane refused four package claims and recorded 9 mistakes including its own landed-then-refuted README rationale; no non-author closure has spot-checked them yet (T46RevGate is lane-dispatched).

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited sources — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-1`; no new independent verifier.
- [~] At least one end-to-end domain task executed and logged — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-2`; no new promotion verdict.
- [~] Instructions executable without oral context — prior pointer `tameshi-shokunin/.ufo/evidence/round-21/coldread/ledger.json`; monitor unchanged (6, 60/64 credited at `3ae8b048`), no independent promotion verifier.
- [~] No cross-domain bleed — prior pointer `tameshi-shokunin/reports/round-1-calibration.md#box-4`; per-entry PROVINCE gate in `.ufo/waves/round-46/w1/RevProvince.md` (lane-dispatched, not independent).

**Round shape:** two v1 waves (policy `ufo-wave-policy.json`, band 32–64), 72 seats, no residual call. The §3 planner seat is held by the L1; planning walks rode ConnPackageCross and RevManifest.
- w1, 37 seats: 16 executor, 6 scribe, 4 reviewer, 4 scout, 3 mutation-tester, 2 critic, 2 connector (m_flash roles 22 of 37).
- w2, 35 seats: 10 executor, 9 critic, 9 reviewer, 4 mutation-tester, 2 connector, 1 scout; all settled with a report.
- Dead seats: 2 in w1 — MutC1Counter and ScribeQuality (results entries carry other lanes' output through a seat-name collision; no tameshi report). Fix: QUALITY 90 and `quality/seat-name-check.py`; w2 had none.
- Dispatch: both waves spawned by the orchestrator from `<wave>.ready`.
- Open L0 questions filed this round: none.
