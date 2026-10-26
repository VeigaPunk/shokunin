# tabi — round 33 report (hyaku run 9, attempt 1; L1 TabiR33)

Lane HEAD `6f4053dbdbddbed24f4515ff01a895b1038d2f37` (`git ls-remote origin refs/heads/master` prints it). Baseline
`b7d16fb8a9405f09bf064e9ea51905b8f9fe66cd`. Freeze `e6b0a9074d434ccc307badd312ae7379d1193fea`. Measured revision
`0aa2281a4fe3df3d0e6d07f4cde6935e75de1fb7`.

## Work performed

The round declared two claims. Claims, counters and controls were frozen before data in `e6b0a907`
(`.ufo/waves/round-33/claims.json`):
- **C1: adjacency.** This was the lowest non-retired axis (8, unique). The stagnation nudge was inactive because the round-32 capability restarts the window. The claim: the sibling-overlap map answers a frozen sweep of 52 browser-domain lines in sibling `PROVINCE.md` files. Target: unaccounted 0 and at least 4 new verified rows that name the other side.
- **C2: operability, sourced.** BiDi runtime gate v2 must refuse the 8 receipt forgeries of the frozen battery, and must still admit the honest receipts (H0/H1/H2).

Work items:
- Frozen counters `.ufo/waves/round-33/counters/c1-adjacency-sweep.mjs` and `c2-bidi-forgery-battery.mjs`, and the control driver `baseline/controls.mjs`. All 7 controls exited 1 before data (`baseline/controls-summary.json`). These include C2 controls for reject-all and for a whitelist gate.
- C1 build:
  - New ledger `corpus/adjacency-screen.tsv` with 44 screens.
  - Map rows 12–14 in `corpus/adjacency.tsv` (kake JS rendering, robots.txt, accessibility execution).
  - The tabi side is stated in `SKILL.md` §"Round 33 — sibling-overlap declarations".
  - The fourth row (kake:347, crawl budget) was **withdrawn** after wave 2 showed it re-keys the mapped crawler split (lesson round-33 M6).
- C2 build:
  - `scripts/check-bidi-runtime.mjs` v2. It adds duplicate-id and Measured-cell findings, run/session provenance, the driver allow-list, and an s1 Gate-row check, with self-test 44/44.
  - The live leg now uses the real binary, drops `--no-sandbox`, and gets a throwaway HOME and XDG config/cache/data/state. The caller-TMPDIR deletion branch is gone. These changes follow w1 SentinelLiveLeg and w2 SentinelLiveV2.
  - New note `corpus/knowledge/bidi-runtime-gate-v2-round-33.md`, citing S127–S129.
- Frontier step:
  - SOURCES S127–S129.
  - Lesson `corpus/lessons/round-33.md` with Gate, C1 gate decisions, Mistakes M1–M8 + M9 closed, errata intake, search log, a wave-2 ledger and the misroot sweep.
  - QUALITY criteria 87–91.
- Round-32 routed defects 1–7: each has a disposition in the lesson. 1 → C2. 2 → carried. 3 → kept 90d, reason withdrawn under w2 attack, routed forward. 4 → named corrections. 5 → errata intake A/B/C landed. 6 → M9 closed. 7 → controls reproducibility recorded, 6 of 7.
- Waves (shape: two v1 waves):
  - w1 build + first falsifiers: 36 seats — 18 scribe, 5 critic, 4 executor, 3 connector, 2 reviewer, 2 mutation-tester, 1 sentinel, 1 scout.
  - w2 falsify: 38 seats — 21 critic, 6 reviewer, 5 executor, 2 mutation-tester, 2 connector, 1 scout, 1 sentinel.
  - Round total 74. No residual call. Dead seats 0: `w1-results.json` 36 of 36 and `w2-results.json` 38 of 38 non-empty outputs.
  - The L1 held the canonical planner seat. The planning data-walk rode ConnRound.

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `e6b0a907` | freeze: claims.json, counters, controls, receipts, measure.sh | LOG round-33 entry |
| `bf48b81c` | w1 integration: map rows, screen ledger, gate v2, S127–S129, v2 note, lesson, QUALITY 87–90, errata, corrections, baseline measurement | same |
| `042d6d9a` | one-line SCORECARD tally correction (selfassessment mismatch 1 at `bf48b81c`) | same, wave-2 corrections |
| `0aa2281a` | w2 integration: crawl-budget row withdrawn, declaration and registry corrections, XDG data/state isolation, v2 note §8, lesson w2 + M6–M8, QUALITY 91 | same |
| `9f008f6c` | measurement at `0aa2281a`, dispositions, late w2 reports | LOG round-33 disposition paragraph |
| `6f4053db` | tally-attribution correction for `SCORECARD.md:1829` (selfassessment read 1 at `9f008f6c`; 0 at `6f4053db`), w2 results | — |

## Before → after measurements

Measured at `0aa2281a` in a clean clone with the counter bytes from the freeze commit (`.ufo/waves/round-33/measure/provenance-0aa2281.txt`: porcelain 0, digests equal frozenDigests, check-adjacency digest equal to the pinned value).

- **C1.** Command: `node .ufo/waves/round-33/counters/c1-adjacency-sweep.mjs --rev <REV> --json`.
  - Before (`baseline/measure-at-baseline/c1-at-b7d16fb.json`): candidates 52, mapped 5, screened 0, unaccounted 47, newMapped 0, adjacency clean 10/10.
  - After (`measure/c1-at-0aa2281.json`): mapped 8, screened 44, unaccounted 0, newMapped 3, adjacency clean 13/13, predicate false, exit 1.
  - **Target missed (newMapped ≥ 4): C1 not met — honest stop.** The integration `bf48b81c` read newMapped 4 (`measure/c1-at-bf48b81.json`). Wave 2 (CritRowCrawlBudget, CritC1Overrides) showed that the fourth row came from an L1 reversal of a w1 screen with no sibling-side ground, so the row was withdrawn rather than kept to meet the target.
- **C2.** Command: `node .ufo/waves/round-33/counters/c2-bidi-forgery-battery.mjs --rev <REV> --json`.
  - Before (`baseline/measure-at-baseline/c2-at-b7d16fb.json`): forgeriesAccepted 8/8, honest true.
  - After (`measure/c2-at-0aa2281.json`): forgeriesAccepted 0/8; H0/H1/H2 true at population 17, admitted 16, failing 0; selftest exit 0 (44/44); digestLiterals []. Exit 0. **Met.**
  - Disclosed holes:
    - The predicate is satisfiable by a stub keyed on battery commit subjects (w1 CritC2Counter, M7). w2 RevGateV2Code confirms that v2 refuses each variant for the construction-correct reason.
    - Survivors are listed in note §8: CritForgeV2B (a)(b) and CritForgeV2C (same-host junk Gate row).
    - w2 MutGateV2: 11 of 20 mutants survive both detectors.
- **No-harm** (`measure/noharm-at-0aa2281.txt`): 28 of 28 offline gates and self-tests exit 0, against 28/28 at baseline.
  - `check-selfassessment`: mismatches 0 at `0aa2281a` and at the final tip `6f4053db`. Twice an intermediate commit read 1 (`bf48b81c`, `9f008f6c`). Each was corrected append-only in the next commit.
  - `measure/numstat-at-0aa2281.txt`: 0 deleted lines outside the rewritten gate.
  - Live leg (`measure/c2-live-at-0aa2281.json`): 16/16, binding null, exit 0.

## Sources & frontier

- Rows 126 → 129. Counting command: `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md`. Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:
  - Start: `tabi ok`, exit 0, 20 W04 (`baseline/census-start.txt`).
  - End: `tabi ok`, exit 0, 20 W04 (`measure/census-end.txt`).
- Added S127, S128, S129. All are `mined`, recheck 90d.
  - S127: ChromeDriver util.cc `GenerateId`, tier A, code.
  - S128: Arch chromium PKGBUILD + chromium-launcher, tier A, code.
  - S129: Chromium `sandbox/linux/README.md`, tier A, docs.
- Rows touched old→new: none. S125 stays 90d, and the on-release receipt option is routed forward.
- Frontier advanced:
  - The sibling-overlap jurisdiction is now bounded: 52/52 PROVINCE lines are accounted for.
  - BiDi receipt provenance is now gate-checked.
  - New frontier row: 34 sibling overlaps outside PROVINCE (w1 ConnSiblingScan).
- Sourced claim: C2. The v2 note's `source:` cites S127–S129.
- Mistakes mined:
  - M1 `vacuous`: the round-32 feasibility sentence.
  - M4 `stale-premise`: L1 claims.json `notClaimed`.
  - M5: the C1 feasibility sentence understated cheap constructions.
  - M6 `scope`: aimed L1 overrides, so the row was withdrawn; QUALITY 91.
  - M7: the battery tell.
  - M8: XDG data/state isolation.
- Assimilation: none. No `merge/tabi/` theme touches these surfaces, and the quarantine hand-check was already run (rounds 22 and 27). This lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.**
  - One admitted entry on ground the coverage map did not hold: BiDi receipt forgery checking, `bidi-runtime-gate-v2-round-33.md`, citing 3 `mined` rows opened this round.
  - The sibling-overlap map gains 3 boundaries and a bounded screen ledger.
- **quality: improved.**
  - Errata intakes A/B/C landed append-only.
  - S127 and S129 were re-opened byte-identical by w2.
  - Live-leg harms found by sentinels were fixed.
  - Defects found in this round's own entries were marked: v2 note §8, SKILL wave-2 corrections.
  - Three low precision items remain carried (w2 CritErrataLanded, ReopenS128). They are named, not left unmarked.
- **discernment: improved, pending the outside check.** The gate decisions are on record for the closure's spot-check:
  - Admits: S127–S129, map rows 12–14.
  - Rejects: 44 screens, the withdrawn crawl-budget row, and rejected source candidates (docs/linux/sandboxing.md 404, suid_sandbox_development.md).
  - Criteria 87–91 cite lessons with red states.
  - The non-author spot-check is owed to the closure.

Axis verdicts:
- adjacency: unchanged at 8; C1 not met.
- operability: improved, C2 met, score held at 9.
- depth, coverage, freshness, calibration: unchanged, no harm measured.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` round-33 sections (map-vs-screen decision rule, registry row, declarations). Non-author verifier not on record.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the v2 live leg on the loopback fixture, `.ufo/waves/round-33/measure/c2-live-at-0aa2281.json`, LOG round-33 disposition.
- [~] Instructions executable by an agent without oral context — w2 RerunLiveV2, RerunC1 and RerunC2 re-ran the commands from the lane text. They are lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged. w2 CritAdjacencyHarm found no absorbed ground. The accessibility declaration overclaim was corrected (SKILL round-33 wave-2 corrections).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/goal-20261026-hyaku-run9.md` (orchestrator), `.ufo/reports/round-33/souji.md` and `.ufo/reports/round-48/tameshi.md`. All belong to other owners. No tabi misroot. Scratch `/fast/scratch/hyaku/tabi-r33` removed.
Open L0 questions: none filed this round.
