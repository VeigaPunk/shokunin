# kake round 31 report (hyaku, in-session L1 KakeR31a2, attempt 2)

Lane tip (pushed): `08ff06c224620f1fd259b421430b1ba8fafdff67` (branch `master`; `jj-lane.sh state`: local = remote, ahead 0, untracked 0). Base `f1ffb81738c92c0537b99b30970143ab9419f990`, unchanged from the claim.

Attempt 1 (L1 `KakeR31`) died in an omp process restart at 17:26Z (`.ufo/watchdog.log` line 734, `lane-dead-no-report kake round=31`) after landing up to `92235a0`. Attempt 2 re-measured that tip, re-checked the attempt-1 draft of this report claim by claim, and finished it.

## Work performed

Declared claims (`SCORECARD.md` "Round 31 — declared claims", committed at `a16602a` before implementation; C2 strict supplement at `b801ac8` before any C2 after-measurement). Neither claim was narrowed after landing:
- **C1, operability, repair:** the citing-set fixture runner `scripts/citing_set_selftest.py` refuses the five hostile fixture shapes the round-30 closure routed (N1, N2, N3, N5, N6), each with a committed hostile spec checked by a committed hostile selftest. This is the only citing-set work this round (drift watch: citing-set gate).
- **C2, freshness, frontier (learning claim and sourced claim):** Render web-service and Blueprint (`render.yaml`) semantics enter held knowledge as `corpus/knowledge/render-web-services.md`, grounded in S057–S060 opened this round, with an offline key-by-key check of the lane's own `render.yaml` (ds4cc-marketplace `1fbdb8ed`, blob `d17ab7e5`).

Work items, attempt 1 (re-verified by attempt 2 and by wave-2 seats):
- Frozen counters `.ufo/waves/round-31/c1_sandbox_probes.py` (sha256 `4707cebf…6d1a`) and `c2_quote_truth.py` (`de48d460…31b8`); before receipts C1 0/5 with K1 holding, C2 0/4 (`verification/c1-before-f1ffb81.json`, `c2-before-f1ffb81.json`). Wave-2 `RerunC1Counter` and `RerunC2Counters` reproduced every receipt field for field.
- Sources S057–S061 opened one GET each at 15:41:23–29Z (`.ufo/waves/round-31/fetch_sources.py`, `sources/receipts.json`, committed `a16602a`). Wave-2 `ReopenS057S058`, `ReopenS059S060` and `ReopenS061Resolution` re-opened all five at 18:06–18:08Z: visible text sha256 equal to the receipts; bodies differ only in deploy ids and asset names.
- Runner repair `c88b97e` and hostile selftest with specs P1–P5; C2 entry, rows, lesson, SKILL, QUALITY, PROVINCE, README at `fde133a`; measured results at `92235a0`.

Work items, attempt 2:
- Re-measured the inherited tip `92235a0`: C1 5/5 K1 holds, C2 4/4, strict 5/5 (`.ufo/waves/round-31/verification/c1-a2-at-92235a0.json`, `c2-a2-at-92235a0.json`, `c2-strict-a2-at-92235a0.json`).
- Wave 2 (falsify), 36 seats, `.ufo/waves/round-31/a2-w2/` (35 reports, `seat-status.json`). Repairs it caused, all at `9a7f5be`:
  - A dot-named symlinked case is now a failed case. Before, it was skipped silently (`a2-w2/CriticSymlinkCases.md`, `CriticC1Wording.md`). Spec P5 gained `.h5b`, and the `fde133a` runner fails it (`verification/a2-fixes/hostile-selftest-fde133a-runner.json`: exit 1, P5 false).
  - The ambiguous `--r` is refused by the runner (`CriticArgvAllowlist.md`).
  - A scratch path containing ":" is refused, because Git splits `GIT_CEILING_DIRECTORIES` on it (`CriticGitPins.md`). Under the `fde133a` runner such a path exits 0; under the repaired runner it exits 2 (`a2-fixes/colon-tmpdir-*.json`).
  - The "symlinks are refused" wording now appears only for ELOOP (`CriticExpectedRead.md`).
  - The hostile selftest now runs a benign `h0-control` copy, so a runner that refuses cases by name fails it. That sham passed the `c88b97e` selftest with exit 0 and fails the repaired one with exit 1 (`a2-fixes/hostile-selftest-*-name-sham.json`; finding `ReviewHostileSelftestCode.md` F1, F2).
  - Appended corrections to the entry ("Round-31 wave-2 corrections"): the PORT mechanism is stated by S058; secret files follow `.dockerignore` per S059; lines 23, 39 and 67 are narrowed. All 7 new quotes are exact substrings of the retained text, and C2 and strict still score 4/4 and 5/5.
  - Appended to SKILL ("Citing-set runner containment — round 31, wave-2 repairs and narrowings", hostile-selftest control note, triage-table correction), QUALITY ("Round-31 wave-2 corrections to the round-31 criteria", from `CriticQualityCriteria.md` F2–F5), PROVINCE and README (`ReviewProvinceReadme.md` F1–F4), and SOURCES (S059 anchor note, `ReviewSourceRows.md`).
  - Census-mode receipts, because the validate receipts cannot show the row change (`ReviewCensusAfter.md` F1): `census-mode-before-f1ffb81.txt`, `census-mode-after-a2.txt`.
- Round-30 routed items 1–6 (`corpus/lessons/round-30-verifier-spotcheck.md:248-286`):
  - (1) C1, extended by the attempt-2 repairs.
  - (2) Open items carried by name in SKILL and in the lesson's "Carried open (attempt 2)". `CriticOpenItemsCarried` found none dropped from the lane.
  - (3) `render-static-sites.md` "Round-31 corrections" (`ReviewStaticSitesCorrections`: correct and append-only).
  - (4) S061, with S053 and S054 kept `rejected` (`ReopenS061Resolution`: hold).
  - (5) `.ufo/waves/round-30/w2/partial-reports.json`, 20/20 coverage (`ReviewPartialReportsList`). Its `history://KakeR30.*` pointers no longer resolve; this is recorded in that seat's report.
  - (6) A closure command that can pass as written (`verification/closure-command-check.txt`). The QUALITY check for it was replaced, because step 1 could never fail (`CriticQualityCriteria` F2).
- Inherited leftovers, both committed at `9a7f5be` (none reverted):
  - `.ufo/waves/round-31/census-after.txt` is byte-identical to a fresh validate run.
  - `.ufo/waves/round-31/w2/swarm-registry.json` is the attempt-1 wave-2 registry. All 36 members have `agentId` null: that wave was specified but never dispatched (confirmed by `CriticSeatAccounting`).
  - Attempt 1's commits `a16602a`, `c88b97e`, `b801ac8`, `fde133a` and `92235a0` were kept, after a re-check by `ReviewLogScorecard` and `NoHarmRangeScan`.
  - The fleet draft of this report was finished in place after every claim was re-measured.

## Landed changes

All landed through `jj-lane.sh`. Each change is tied to a LOG.md entry ("Round 31 — attempt 1" or "Round 31 — attempt 2"):
- `a16602a` declaration, counters, fetcher, sources, before receipts, census before.
- `c88b97e` C1 runner repair, hostile selftest, five hostile specs.
- `b801ac8` C2 strict supplement and its before receipts; C1 after receipt.
- `fde133a` C2 entry, rows S057–S061, lesson, static-site corrections, S053/S054 note, SKILL, QUALITY, PROVINCE, README, LOG, round-30 partial-report list, wave-1 evidence.
- `92235a0` SCORECARD measured results, after receipts at `fde133a`, attempt-1 wave-2 spec.
- `9a7f5be2b2091fc9b76adc803b8b442d5c292d08`: the attempt-2 wave-2 repairs and appended corrections listed above, the inherited leftovers, the a2-w2 spec and dispatch, re-measure and fix receipts.
- `08ff06c224620f1fd259b421430b1ba8fafdff67`: SCORECARD "Round 31 — attempt 2 re-measure and wave-2 repairs", the LOG attempt-2 entry, lesson row notes, wave-2 reports and `seat-status.json`, receipts at `9a7f5be`.

## Before → after measurements

| Claim | Command | Before | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-31/c1_sandbox_probes.py --root . --revision <commit>` | 0/5 at `f1ffb81`, K1 holds | 5/5, K1 holds | `c88b97e`, `fde133a`, `92235a0`, `9a7f5be` (`verification/c1-after-*.json`, `c1-a2-at-*.json`) |
| C1 hostile selftest | `python3 -B scripts/citing_set_hostile_selftest.py --root <export> --tmpdir <dir> [--runner <base runner>]` | base runner exit 1, 0/5 | exit 0, 5/5 (with `h0-control` and `.h5b`) | `9a7f5be` (`verification/hostile-selftest-a2-at-9a7f5be.json`, `hostile-selftest-a2-base-runner.json`) |
| C2 | `python3 -B .ufo/waves/round-31/c2_quote_truth.py --root . --revision <commit>` | 0/4 at `f1ffb81` | 4/4, control not broken | `fde133a`, `92235a0`, `9a7f5be` (`verification/c2-after-fde133a.json`, `c2-a2-at-*.json`) |
| C2 strict (closure supplement) | `python3 -B .ufo/waves/round-31/c2_strict_checks.py --root . --revision <commit>` | 0/5 at `f1ffb81` | 5/5 | `fde133a`, `92235a0`, `9a7f5be` (`verification/c2-strict-*.json`) |

The 45 committed fixtures stay clean at `9a7f5be` (`verification/benign-a2-at-9a7f5be.json`, runner `7c95a18e…8969`). Limits that wave 2 found and that were not repaired are in SCORECARD "Round 31 — attempt 2 re-measure and wave-2 repairs":
- The frozen C1 counter trusts the runner's reported failure names, so a sham runner committed in its place scores 5/5.
- The Git pins and mutant m3 are not probed alone (`MutRunnerGuards`: m1, m2, m4 and m5 are killed; m3 survives).
- The C2 strict supplement certifies quote provenance, not truth: three constructed hollow or false commits score 5/5 (`ReviewC2StrictChecker`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`. At round start it exited 0, and at round end (attempt 2, 18:40Z) it exited 0 again. Both runs print only the pre-existing `S033 duplicate url` W04 and `ok` (`.ufo/waves/round-31/census-before.txt`, `census-after.txt`).
- Census mode, before → after: rows 56 → 61, tier A 47 → 52, B 1 → 1, C 8 → 8, mined 43 → 48, queued 6 → 6, rejected 7 → 7 (`census-mode-before-f1ffb81.txt`, `census-mode-after-a2.txt`). The `grep -c '^| S0' corpus/SOURCES.md` count is 61.
- Rows added by tier: A ×5 (S057–S061, all `mined`).
- Rows touched, old → new: S053 `rejected` → `rejected` and S054 `rejected` → `rejected`. Their flip conditions are met, the resolution is logged, and no cell changed. S059's anchor label was corrected by a tail note only; no status, recheck or used-by changed.
- Frontier advanced: Render web services and the Blueprint file moved from open to held Frontier knowledge (no gate, not Core). Accessibility conformance and crawl/JS canonical signals stay open.
- Mined mistakes, `corpus/lessons/round-31.md` "Mistakes": 4 rows from attempt 1, plus 4 from attempt 2:
  - doc claim wider than its probe;
  - inference mark on a stated fact;
  - attempt lost with an unlanded placeholder report;
  - selftest trusts the reported names.

  Each row names what should have caught it and gives a fix shown able to fail.
- Sourced claim: C2 cites S057–S060, all opened this round.

## Trend verdicts

- **expansion: improved.** A new entry on open Frontier ground, a SKILL triage table and 5 new tier-A rows. Wave-2 `CriticLearningClaimAfter` judged that the entry adds real knowledge. It also found gaps (the port defaults, the missing `ARG`); the port and `ARG` gaps were corrected in the appended section. [author view; the closure decides]
- **quality: improved.** Routed overreaches in `render-static-sites.md` were corrected, and the runner gained containment checked by hostile specs. Wave 2 found three runner defects and a selftest hole; all four are repaired at `9a7f5be` and each repair is shown able to fail. [author view]
- **discernment: improved.** Wave 2's 36 attack items found real defects and named the limits of both counters: name-trusting C1 and provenance-only strict C2. Those limits are recorded rather than hidden. The QUALITY criteria were corrected where a check could not fail. [author view]

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Render web service and Blueprint triage — round 31" (S057–S060 quotes) and its wave-2 correction (`SKILL.md` after line 873).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG "Round 31 — attempt 1": the lane's `render.yaml` was checked key by key against the Blueprint reference. Wave-2 `ReviewEntryRenderYaml` found no wrong pointer.
- [~] Instructions executable by an agent without oral context — SKILL "Citing-set runner containment — round 31" and "… wave-2 repairs and narrowings" (rules, command, exit map, open items).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE "Round-31 Render web-service frontier step", plus its wave-2 narrowing (live fetches were Render Docs only; no operator-owned property was touched).

## Round shape

- Shape: default, two v1 waves, 69 seats in total.
- Wave 1, `kake-r31-w1` (attempt 1, dispatched 15:54:35Z; policy v1): 33 seats.
  - Roles: scribe 13, critic 5, reviewer 5, scout 4, executor 3, mutation-tester 2, connector 1.
  - Outcomes: 13 returned. 18 died at spawn ("No model selected"; all executor, scribe and mutation-tester seats; `w1/dead-seats.json`). 1 refused (`KakeR31.CriticC1Counter`). 1 returned after an automatic model switch (`KakeR31.CriticSandboxThreatModel`).
  - The §3 floor (connector, 3 executors, scribe, scout, reviewer, critic) was dispatched in wave 1, but the executor and scribe seats died there. The L1 holds the planner seat; the validator rejects `planner`.
- Wave 2, `kake-r31-a2-w2` (attempt 2, wave-slot granted, dispatched 18:04Z; policy v1, `a2-w2-dispatch.json`): 36 seats.
  - Roles: reviewer 23, critic 11, scout 1, mutation-tester 1.
  - Outcomes: 0 dead, 0 refused, 0 model switches. 35 returned. `ReviewRunnerDiff` had not returned when this report landed, so its review is not evidence for this round.
  - The attempt-1 wave-2 item `ReviewC1CounterDesign` was dropped as a rephrase of the held CriticC1Counter. `MutRunnerGuards` was added; the guards it tests did not exist when wave 1 ran.
  - `ReviewHostileSelftestCode` (an attempt-1 planned item) built a name-refusing runner, an attack close to the held item's ground. It completed with no refusal, and its finding is used above.
- The attempt-1 wave 2 (`kake-r31-w2`, 36 specified) was never dispatched: no slot was granted before the restart. It counts 0 seats.
- No residual call.

## Open items and extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` at 18:0xZ (`a2-w2/ScoutMisrootSweep.md`) found no seat-written file at the fleet root naming kake round 31, `KakeR31` or `KakeR31a2`. The only hit was this report's own path. No file was moved or deleted.
- Tool installs: none by the L1, and no seat reported one.
- Holds for the ledger (refusals; never retried, rerouted or rephrased):
  - `KakeR31.CriticC1Counter` (critic) ended on a provider cyber-content block.
  - `KakeR31.CriticSandboxThreatModel` (critic) returned after "Claude Opus 5.5 hit a safety filter, and the conversation was automatically switched to Claude Opus 4.8." Its findings are advisory and unverified.
- Not repaired, carried by name: lesson "Carried open (attempt 2)", SKILL wave-2 section.
- L0 questions: none.
