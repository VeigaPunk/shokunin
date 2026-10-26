# tabi — round 34 report (hyaku run 9, attempt 1; L1 TabiR34)

Lane HEAD `71a873055ad7627ea4495ce554ff8bfb03513d74` (`git ls-remote origin refs/heads/master` prints it). Baseline
`15dfaccb34601c2d221c78501e2befd8998d600c`. Freeze `59f1b47aae277e1670e4a824173da8cde7e388ee`. Measured revision
`b44b964d1044996ed08f1079916592065dee3094`.

## Work performed

The round declared two claims. Claims, counters and nine control receipts were frozen before any data in `59f1b47a`
(`.ufo/waves/round-34/claims.json`):
- **C1: adjacency.** Adjacency was the lowest non-retired axis (8, unique). The stagnation nudge was inactive (window position 2). The claim: the sibling-overlap map answers 67 sibling lines outside `PROVINCE.md`. These are lines in sibling `SKILL.md`/`corpus/knowledge` that name tabi (38), plus round-33 ConnSiblingScan leads (29). Target: unaccounted 0 and newMapped ≥ 3, where a new row counts only if it has a new tabi declaration naming the sibling.
- **C2: operability, sourced.** The BiDi gate's own `--selftest` must kill all 20 frozen round-33 MutGateV2 mutants, and the neutral, decoy and twin probes must pass. At the baseline the self-test killed 8.

Work items:
- Frozen counters and controls:
  - Counters `.ufo/waves/round-34/counters/c1-adjacency-sweep-v2.mjs` and `c2-gate-mutants.mjs`, with control driver `baseline/controls.mjs`.
  - All 9 controls exited 1 with predicate false (`baseline/controls-summary.json`).
  - The C1 controls included existing-tabi-line rows (J4), which the new-declaration clause refuses.
  - The C2 controls included a self-hash test and a find-sniff test (J2 and J3), which the neutral, decoy and twin probes refuse.
  - w1 RevC1Controls and RevC2Controls reproduced every control receipt.
- C1 build and wave-2 correction:
  - The w1 integration `04f9623d` added map rows 15–18, 62 screens in the new `corpus/adjacency-screen-skill.tsv`, and tabi declarations at `SKILL.md:2921-2924`.
  - Wave 2 withdrew rows 15, 17 and 18:
    - Row 15 re-keyed row 12 (w2 CritRowLiveDelivery).
    - Row 17: the kotoba census rules the pair `none` (w2 CritRowKotoba).
    - Row 18 was a refusal routed nowhere (w2 CritRowKasegi).
  - Two kaidoku rows that the L1 had screened were restored as map rows (w2 CritReversalKaidoku).
  - Ledger notes were corrected. The result is in the w2 integration `b44b964d` and in lesson round-34 §"C1 gate decisions — wave 2".
- C2 build:
  - Twelve `v3-a-*`/`v3-b-*` self-test cases (w1 ExecKillsA/B) were merged by the L1 into `scripts/check-bidi-runtime.mjs`, with one optional `detailIncludes` field. The self-test went from 44 to 56 cases.
  - New entry `corpus/knowledge/bidi-gate-selftest-round-34.md` cites S125, S127 and S130–S132.
  - w2 RevKills×6, MutDetailAssert and RevSelftestCodeRead all hold.
- Frontier step:
  - SOURCES S130–S133; S133 supersedes S128.
  - Lesson `corpus/lessons/round-34.md` with Gate, C1/C2 decisions, Mistakes M1–M5, errata intake and search log.
  - QUALITY 92–97.
- Round-33 routed defects 1–7: each has a disposition in the lesson (§Errata intake):
  - The kake 396/411/422/440 screens in `corpus/adjacency-screen.tsv` were relabelled.
  - Three append-only corrections landed.
  - The S125 cadence change is routed forward, because this round's frozen append-only rule keeps that cell fixed.
- Waves (shape: two v1 waves):
  - w1 build + first falsifiers: 37 seats — 18 scribe, 4 critic, 4 scout, 3 executor, 3 connector, 2 reviewer, 2 mutation-tester, 1 sentinel.
  - w2 falsify: 39 seats — 17 critic, 10 reviewer, 4 scout, 3 executor, 2 mutation-tester, 2 connector, 1 sentinel.
  - Round total 76. No residual call. Dead seats 0 (`w1-results.json` 37/37, `w2-results.json` 39/39 non-empty).
  - The L1 held the planner seat; the data-walk rode w1 ConnRound.

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `59f1b47a` | freeze: claims.json, counters, controls, nine receipts, candidate list, pins, measure.sh, census-start | LOG round-34 freeze entry |
| `04f9623d` | w1 integration: map rows 15–18, screen ledger, declarations, twelve kill cases, entry, S130–S133, lesson, QUALITY 92–96, relabel, carried corrections, tally corrections | LOG "Round 34 wave-1 integration" |
| `b44b964d` | w2 integration: rows 15/17/18 withdrawn, kaidoku rows restored, ledger and entry corrections, lesson M5, QUALITY 97 | same; lesson round-34 §wave 2 |
| `71a87305` | measurement at `b44b964d`, SCORECARD disposition, w2 results, QUALITY wave-2 corrections | LOG "Round 34 disposition" |

## Before → after measurements

Measured at `b44b964d` in a clean clone, with the counter bytes taken from the freeze. `measure/provenance-b44b964.txt` records porcelain 0, digests equal to frozenDigests, the pinned check-adjacency digest, and gate mode 100755.

- **C1.** Command: `node .ufo/waves/round-34/counters/c1-adjacency-sweep-v2.mjs --rev <REV> --json`.
  - Before (`baseline/c1-J1-do-nothing.json`): candidates 67, mapped 1, unaccounted 66, newMapped 0.
  - After (`measure/c1-at-b44b964.json`): mapped 4, screened 63, unaccounted 0, newMapped 1 (kake `lab-performance-tool-runs`), adjacency clean 16/16, predicate false.
  - **Not met: honest stop.** The w1 integration read newMapped 4. Wave 2 withdrew three rows, and none was kept against a finding.
- **C2.** Command: `node .ufo/waves/round-34/counters/c2-gate-mutants.mjs --rev <REV> --json`.
  - Before (`baseline/c2-J1-do-nothing.json`): killed 8 of 20, 12 survivors.
  - After (`measure/c2-at-b44b964.json`): killed 20 of 20, survivors none, unappliable none, twins failing none; pristine, neutral and decoy exit 0; round-33 battery true.
  - **Met.** Disclosed limits:
    - The whitespace-normalised self-sniff residual.
    - 9 of 10 counter mutants are unguarded by the controls (w1 MutC2Counter).
    - The symlink write path (w1 SentinelCounters F1).
    - M04/M05/M06 are killed only through the printed finding detail.
- **No-harm** (`measure/noharm-at-b44b964.txt`): 28 of 28 gates and self-tests exit 0, against 28/28 at baseline.
  - `check-selfassessment` mismatches 0.
  - The round-33 C1 counter reads unaccounted 0 with screenFindings [].
  - `measure/numstat-at-b44b964.txt`: 0 deleted lines in the append-only files.

## Sources & frontier

- Rows 129 → 133. Counting command: `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md`. Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:
  - Start: `tabi ok`, exit 0 (`baseline/census-start.txt`).
  - End: `tabi ok`, exit 0, 20 W04 (all pre-existing) (`measure/census-end.txt`).
- Added, all tier A:
  - S130: Chromium `base/token.cc`, the upper-case target-id shape.
  - S131: the chromium-bidi `CdpTargetManager.ts`, where context id = targetId.
  - S132: ChromeDriver `commands.cc`, one id per session with no dedupe.
  - S133: supersedes S128 (PKGBUILD locator `:13` → `:12`).
  - w2 ReopenS130–S133 re-opened all four; each holds.
- Rows touched old→new: S128 → superseded by S133. S125 recheck is unchanged (`90d`); the `on-release` proposal is routed.
- Sourced claim: C2. Its entry cites S130–S132.
- Frontier advanced:
  - Sibling ground outside PROVINCE is now bounded for tabi-naming lines and round-33 leads (67/67 accounted).
  - Gate rule coverage is now runnable-checked for 20 sites.
- Mistakes mined:
  - M1 `misroot`: the wave-label path; 2 seats were affected and moved.
  - M2 `stale-locator`: the lead off-by-one.
  - M3 `control-gap`: the rename route; QUALITY 96.
  - M4 `premature-impossibility`.
  - M5 `scope`: three withdrawn integration rows; QUALITY 97.
- Assimilation: none. w1 ScoutAssimilation found that no `merge/tabi/` theme touches these surfaces. This lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.**
  - One entry on ground the map did not hold: gate self-test rule coverage, citing 3 rows opened this round.
  - One new sibling boundary: kake lab performance runs.
  - Two kaidoku boundaries.
  - The screen ledger now covers sibling ground outside PROVINCE.
- **quality: improved.**
  - S128 was superseded with corrected locators.
  - Three round-32/33 errata landed append-only, and the relabel landed.
  - Defects found in this round's own entries are marked: the entry §6 and the QUALITY wave-2 corrections.
  - All four new rows were re-opened.
- **discernment: improved, pending the outside check.**
  - Wave 2 overturned three integrator admits, and the round reported the miss rather than keeping them.
  - Admits on record: final map rows 15 (kake lab performance) and 16–17 (kaidoku HAR, screenshot compare), and S130–S133.
  - Rejects on record: withdrawn w1-numbered rows 15, 17 and 18 (live delivery, kotoba, kasegi); source drafts refused as duplicate URLs.
  - These are open to the closure spot-check.

Axis verdicts:
- adjacency: unchanged at 8; C1 not met.
- operability: improved; C2 met, score held at 9.
- depth, coverage, freshness, calibration: unchanged, no harm measured.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §"Round 34 — BiDi gate self-test: what a kill case must show". Non-author verifier not on record.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the gate self-test plus the frozen mutant counter run end-to-end, `measure/c2-at-b44b964.json`, LOG "Round 34 disposition".
- [~] Instructions executable by an agent without oral context — w2 RerunC1, RerunC2 and RerunNoHarm reproduced the readings from lane text. They are lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged. w2 CritAdjacencyHarm: no-harm legs hold. Three rows that overreached were withdrawn.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` is empty, so there is no fleet-root misroot. Two seats wrote into a mislabelled lane dir (`w1 = build + first falsifiers/`); both were moved into `w1/` (lesson M1). Scratch `/fast/scratch/hyaku/tabi-r34` removed.
Open L0 questions: none filed this round.
