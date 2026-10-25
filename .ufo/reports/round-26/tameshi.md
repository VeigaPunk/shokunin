# tameshi — round 26 report

L1 TameshiR26, attempt 1, 2026-10-22. Lane repo `tameshi-shokunin`, base
`d4140796f4e48e8ec81b793facba73fbd03b4443`, pushed lane head
**`e08444d3f2b40fc6734be4f1c57a56639add9c2d`** (`jj-lane.sh state`: local = remote, ahead 0, tracked 0, untracked 0).

## Work performed

Declared claims (frozen in `.ufo/evidence/round-26/contract.json` at `622d31d` before any mutant ran):
**C1 depth** (learning claim; depth and calibration tie lowest at 8): a ninth recorded mutation-ledger leg on a kumitate gate.
**C2 calibration** (record repair): the three lane-record mismatches routed by `corpus/lessons/round-25-verifier-spotcheck.md:189-199`.

- Pre-registered a 10-defect spec (5 kill-aimed, 5 hole-aimed) and predictions for kumitate `scripts/cite-check.mjs` at `1205c66` (blob sha256 `40573448…c10c9f`) — `.ufo/evidence/round-26/cite-check/`, commit `622d31d` (10:01:47Z); sweep 10:02:07Z: 5/10 killed, 10/10 verdict predictions held (`cite-check/sweep/sweep.txt`).
- Wired leg `js-cite-check` into `tools/mutate-and-run.sh` (pin, table, spec heredoc, replay call, selftest tuples) and `tools/mte-interop.py` (`LEG_TABLE`) — `a08e85c`. Selftest 97/97; regression `REGRESSION: PASS (cases=9 passed=9 …)` (`cite-check/regression-worktree.stdout`); interop `MTE_INTEROP: PASS legs_conforming=9/9`, selftest 17/17 (`after/mte-check-a08e85c.stdout`, `after/mte-selftest-a08e85c.stdout`).
- New entry `corpus/knowledge/mutation-case-kumitate-cite-check.md` citing new rows S088 (the pinned gate) and S089 (Stryker, equivalent mutants), both opened this round. Wave-1 probes: four survivors are suite holes with hermetic off-suite witnesses (`w1/ProbeSOOREDGE.md`, `ProbeSSTRICT.md`, `ProbeSUSAGE.md`, `ProbeSPININCLUDES.md`); `S_EMPTY_GUARD` is an equivalent mutant (`w1/ProbeSEMPTYGUARD.md`, `w1/CriticEquivalence.md`). SKILL.md "## Ninth recorded case — round 26" carries the survivor decision table and the equality-assert error pattern.
- C2 fixes: registry rows `mte-interop-selftest` and `mte-interop-check` plus a SKILL.md registry row (item 1); amendment-3 corrections appended to SCORECARD and `corpus/lessons/round-25.md` (item 2); refreshed `verified-at` in `corpus/knowledge/mte-report-interop.md` naming tool sha256 `193ea6e3…` at `a08e85c` and two committed receipts (item 3).
- QUALITY 51 (verified-at binds tool bytes and receipt) and 52 (wave contexts name jj; registry `source` form), lesson-backed. Routed item 5 closed in both wave contexts (`w1/ScoutJjBounds.md`).
- Routed item 4 explained, not fixed: 17 command-binding weakenings still survive (`w1/MtGuardGapsRecheck.md`; 16 distinct edits); 14 re-attack findings, round-24 spot-check items 2–4 and unpinned emitted reports unchanged (`w1/ScoutRoutedOpen.md`, `w1/ReviewMteLeg9.md`).
- Mid-round harms caught and repaired: two new registry rows had a prose `source`, so `registry-check.py` could not evaluate the registry at `a08e85c` (`w1/RegistryCheck.md`) — fixed in `40a12bf`; `mte-interop-check` then differed as non-hermetic (48/49 at `40a12bf`, `after/registry-40a12bf.json`) — fixed in `2b064cf`, `--only` reads held 1/1.

## Landed changes

| Commit | What | LOG |
|---|---|---|
| `622d31d` | contract, frozen counters, spec, predictions, before receipts | LOG.md round 26 |
| `a08e85c` | ninth leg in runner and interop, registry rows, SKILL ninth-case section, sweep evidence | LOG.md round 26 |
| `40a12bf` | entry, S088/S089, SKILL survivor table and stale count updates, registry source fix, QUALITY 51–52, PROVINCE/README appends, round-25 corrections, verified-at refresh, LOG, lesson | LOG.md round 26 |
| `d2206cd` | SCORECARD measured results, after receipts | LOG.md round 26 |
| `2b064cf` | `mte-interop-check` row uses the clone's fleet mirror; harmed monitor receipts | lesson After measurement |
| `e08444d` | after measurement, retained harm, errata, end census, wave reports, unsent wave-2 spec | lesson After measurement |

## Before → after measurements

| Claim | Command | Before (d4140796) | After | Measured commit |
|---|---|---|---|---|
| C1 | `python3 .ufo/evidence/round-26/c1-measure.py --repo CLONE_AT_REV` | `recorded_cases=8 wired_legs=8 depth_score=8`, exit 1 | `recorded_cases=9 wired_legs=9 depth_score=9`, exit 0 (command D also 9) | `40a12bf34f34977a5789e81b930303b97c4038d1` |
| C2 | `python3 .ufo/evidence/round-26/c2-measure.py --repo CLONE_AT_REV` | `mismatches=3/3`, exit 1 | `mismatches=0/3`, exit 0 | `40a12bf34f34977a5789e81b930303b97c4038d1` |

Bounds (seat findings, recorded in SCORECARD and the lesson): C1's counter checks wiring, not table truth (a leg copied from leg 8 passes it and the regression, `w1/CriticC1.md`). C2's counter can be gamed to 0/3 by token-bearing prose (`w1/MutateC2Counter.md`); only item 2 is a SCORECARD self-assessment row in the strict sense (`w1/CriticC2.md`).

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`: start exit 0 (85 rows), end exit 0 (87 rows), seven pre-existing W04 warnings (`after/census-end.stdout`). Rows added: tier A 2 (S088 code, S089 docs), both mined, used by the new entry. Rows touched: none (S052 re-opened by a seat, unchanged). Frontier rows advanced: none (the ninth leg is Core ground; F3 stays open). Mined mistakes: two, in `corpus/lessons/round-26.md` `## Mistakes`. Sourced claim: C1 (S088, S089).

## Trend verdicts

- **expansion: improved** — new entry on a never-swept-in-full gate (S088, S089), ninth recorded leg.
- **quality: unchanged** — verified-at refreshed and corrections appended, but no entry superseded; the cold-read monitor is harmed (below).
- **discernment: improved** — equivalent mutant identified and kept as a survivor by an explicit rule (S089), one prediction-witness mismatch named, four holes witnessed off-suite.

**Harm, retained and not restored:** strict cold-read monitor 62/62, restraint 8 at base → 25/64, restraint 6 at `2b064cf` (`after/monitor-harmed-*.json`; runner, registry and corpus inputs drifted 37 sections; 2 new headings). The repair (wave 2, 39 independent cold reads) was validated but not dispatched; the author re-anchor tool refuses new sections. Calibration reads harmed on that monitor; the closure rules.

## SHONEN

- [~] SKILL.md tables, error patterns, cited sources — `SHONEN.md` box 1 pointer; ninth-case table at SKILL.md end.
- [~] end-to-end domain task logged — `LOG.md` round 26.
- [~] executable without oral context — `.ufo/evidence/round-21/coldread/ledger.json`; monitor harmed at head (25/64).
- [~] no cross-domain bleed — `PROVINCE.md` round-26 append; `w1/ConnectorOverlap.md` finds no contested scope.

## Round shape and seats

Shape: default v1, wave 1 only. Wave 1 `round-26-w1`: 39 seats (10 executor, 8 scribe, 6 scout, 6 reviewer, 5 mutation-tester, 3 critic, 1 connector; 36 % attack roles); 37 completed, 2 cancelled by the L1 after their items were superseded (DraftQuality, DraftProvinceReadme), 0 dead. Planner seat held by the L1. Wave 2 (55 seats; 39 cold reads) validated (`spec-w2.json`, `dispatch-w2.json`) but its gate request was cancelled at 11:47Z after Main's wave-size steer and the freeze; no residual call. Round total: **39 seats**. Gate wait for wave 1: 2510 s.

## Other

- L0 questions: none opened.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Installs: none (ephemeral `uv run --with jsonschema==4.25.1` from cache).
- Misroot sweep: `git status --porcelain` at the fleet root shows no file from this lane's seats (only `.ufo/waves/round-49/`, another lane's).
- Recommendations for kumitate (owner, read-only here): add hermetic cases for line n+1, `--strict` with one warning, an unknown flag's exit 64, and an interior-slice content pin.
- Next round: drift sentinel (calibration claimed five rounds from routed items) — work a different frontier area; restore the monitor first.
