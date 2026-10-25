# tsukuroi — round 26 report (attempt 1, 2026-10-22)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`. Pushed lane tip cited by this report: `420a1ae106fc28524b9e7a7aa98080dea976ac15` (`jj-lane.sh state`: local = remote, ahead 0, behind 0). Claim base `e9f5356cd68c9281d07a22e54d1bfd72b12306ac`. Dispatched 2026-10-22T13:33:23Z (`.ufo/watchdog.log` line `launch tsukuroi round=26 pgid=2784134 driver=hyaku-inline attempt=1`). No earlier attempt of round 26 exists (no `lane-dead-no-report tsukuroi round=26` line).

## Work performed

Declared claims (SCORECARD.md section "Round 26 — declaration, attempt 1", commit `b13e991f`, refined before any measurement in `4de2b6b1`):

- **C1 — depth (tied lowest at 8), learning claim, sourced, new PROVINCE frontier area:** storage-integrity entry `corpus/knowledge/storage-health-r26.md` and `.json` with rows SH1 to SH6 (btrfs device error counters, their persistence, scrub verification and repair by profile, this host's scrub record, how smartctl derives NVMe health, NVMe lifetime counters). Counting command `python3 tools/check-storage-health.py --revision <REV>`, field `verified_rows`; declared after-value 6.
- **C2 — calibration:** self-assessment mismatch count under check set v2 (K01 to K27). Counting command `python3 tools/check-self-assessment.py --revision <REV>`, field `mismatches`; declared after-value 0 of 27.

Work items:

- Canonical protocol files read before any wave, with sha256 of all seven recorded in the declaration commit (routed defect 6, third recurrence closed): `SCORECARD.md` round-26 declaration; wave-1 RevCanonicalDigests re-derived all seven and the commit time (`.ufo/waves/round-26/w1/RevCanonicalDigests.md`).
- Read-only host capture of btrfs and NVMe state by the L1: `.ufo/waves/round-26/capture/capture.sh` and `capture.txt` (sha256 `002bef16de9bfbffff7905904a1e7f44dae486ca2e60f38090ac2a87132a71dd`), committed in `b13e991f`. Only read-only sudo queries; no scrub, counter reset, service or package action (wave-1 SentinelCaptureSafety).
- Twelve sources opened and snapshotted under `.ufo/waves/round-26/sources/` (S128 to S139), registered in `corpus/SOURCES.md` with anchors carrying each snapshot sha256, Gate records in `corpus/lessons/round-26.md`.
- Two counting tools built in separate push-disabled clones and pinned before any data: `tools/check-storage-health.py` (sha256 `6aadca51…f367`, 41-case selftest) and `tools/check-self-assessment.py` v2 (sha256 `77c946a9…c26d`, 13-case selftest), commit `4de2b6b1`.
- Routed defects 1 to 8 of the round-25 spot-check: dispositions in `corpus/lessons/round-26.md` section "Routed defects from the round-25 spot-check", corrected by its section "Wave-2 findings and corrections" (defects 1, 2, 6 fixed; 3, 5, 7 partly; 4 landed at `7f9f0889`; 8 fixed in form by S136 to S138 with a residual).
- Routed defect 4: `tools/check-memory-pressure.py` hardened (six rule changes, crash fixed); replay of the 17 round-25 wave-2 mutants: 16 killed, 1 survived (was 8 of 17) — `.ufo/waves/round-26/w1/ExecMemCheckerHarden/result-w2.json`.
- Wave-2 falsify findings applied as appended corrections (entry section "Wave-2 corrections", SKILL notes, PROVINCE correction, README correction, memory-pressure note), plus QUALITY 60 to 66 and lesson Mistakes rows.
- L1 mutation evidence after the four wave-2 mutation-tester seats died: `.ufo/waves/round-26/l1-mutation/README.md` (C1 20 of 20 rule mutants killed; C2 8 of 8 rule mutants killed, plan prose correctly ignored).

## Landed changes

Every commit carries the lane identity `tsukuroi-shokunin <tsukuroi@shokunin.local>` and was landed by `jj-lane.sh` (landed and remote-verified):

| Commit | What | LOG.md entry |
|---|---|---|
| `b13e991fb96972b423b868ba122187f75357368c` | Declaration, canonical digests, capture | "Round 26 — storage integrity frontier and self-assessment v2" |
| `4de2b6b1c0cde1f7c7ca9e5727965bcf6aa6ba9e` | Counting tools pinned; declaration refinements | same entry |
| `ef72f10d79c5b9fee3655e432da52d054b7a018d` | C1 entry, S128-S139 and snapshots, Gate, SKILL section and registry, PROVINCE frontier, README row, routed defects 1, 2, 6, 7, 8, QUALITY 60-63, SHONEN evidence lines, wave-1 evidence | same entry |
| `7dfea9244a84a0e2439f0698e54491e5d7b7c467` | Round-26 axes table with dated ordinal record; measured outcome; receipts | same entry |
| `7f9f08894fce41146f76fa5c3f3282037211555a` | Routed defect 4 (memory-pressure checker), wave-2 spec | same entry |
| `75449b13526a57378bfbb6bce929c360ad4c8842` | Wave-2 repairs (appended corrections), QUALITY 64-66, falsify-wave outcome | "Round 26 falsify wave and final measurement" |
| `dd923c036fe0801cddd197ba8952b311217c18a3` | Late corrections; axes table re-stated after a count change | same |
| `03b9990e934850266266dfa866e08081fd80b3a8` | Final receipts at `dd923c03`, wave-2 reports | same |
| `420a1ae106fc28524b9e7a7aa98080dea976ac15` | Receipts at `03b9990e`, last wave-2 report, lesson note | same |

Inherited: commit `4677350a5249a56da693005a78f636d815bbc372` ("considerthese: 2026-10-22 daily reflection", author João Pedro Veiga) landed on the lane between the dispatch and the declaration; the helper rebased the declaration over it (`rewritten 78e7575… -> b13e991f…`). It is not round work and was not edited. Two empty L1 files remain untracked (`.ufo/waves/round-26/w1-dispatch.err`, `w2-dispatch.err`, 0 bytes, validator stderr). No uncommitted round work.

## Before → after measurements

| Claim | Command | Before at `e9f5356c` | After | Measured revision | Author verdict |
|---|---|---|---|---|---|
| C1 | `python3 tools/check-storage-health.py --revision <REV>` → `verified_rows` | exit 2, `SH-CAPTURE-MISSING`, 0 (`measure/c1-e9f5356c.json`) | exit 0, 6 of 6 | `7dfea924` (`measure/c1-7dfea924.json`); re-run 6 of 6 at `dd923c03` and `03b9990e` | Declared target met. The count proves complete evidence links (quotes in committed snapshots whose digests are in the anchors, Gate records, unique capture pointers, SKILL rows), not true statements. Wave-2 row reviewers found statement errors, each now marked by an appended correction: SH6's Unexpected Power Losses trigger omitted a second branch (verdict split, `UNVERIFIED` for that count); SH4 "ordinary reads do verify checksums" and SH2 "only on an explicit reset" withdrawn as universals; SH1, SH3, SH5 wording narrowed. |
| C2 | `python3 tools/check-self-assessment.py --revision <REV>` → `mismatches` | exit 1, 5 of 27 (K02, K06, K10, K24, K26; `measure/c2-e9f5356c.json`) | exit 0, 0 of 27 | `7dfea924`; 0 of 27 again at `dd923c03` and `03b9990e` (after a re-stated table; at the repair commit `75449b13` it read 2, K08 and K11, `measure/c2-75449b13.json`) | Declared target met by the declared command. What it proves (wave-2 CritCalibrationClaim): the 21 observed-state checks K07 to K27 moved 3 → 0 (K10 stale lesson count; K24 and K26 SHONEN citations of a superseded note). K01 to K06 compare the table with an ordinal-record line this round wrote in the same commit, so they show self-agreement only; K02 and K06 were cleared by that line. Under the rule as declared at `b13e991f`, before refinement, the move is also 3 → 0. QUALITY 65 records the fix owed. |

Tool bytes at the measured revisions equal the pins at `4de2b6b1` (`git diff --quiet` exit 0 for both tools). Registry coverage PASS 29 of 29 and memory-pressure 6 of 6 at `dd923c03` (`measure/registry-dd923c03.json`, `memory-pressure-dd923c03.json`). No ordinal changed; no capability entered the table.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.

- Round start: exit 0, `tsukuroi ok`, 22 W04 warnings, 127 rows.
- Round end (at `dd923c03`, `.ufo/waves/round-26/measure/census-final.txt`): exit 0, `tsukuroi ok`, 25 W04 warnings (the three new ones are S136, S137, S138, which reuse the URLs of the rows they supersede by design), 139 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Frozen manual census (wave-2 RerunCensusRegistry): malformed 0, tiers A=129 B=3 C=7, statuses mined=125 queued=5 rejected=9, no duplicates, no enum breaks, no missing used-by paths.
- Rows added by tier: 12, all tier A, all `mined`, opened 2026-10-22: S128 to S135 and S139 (btrfs-progs v7.1 docs, Arch btrfs-progs 7.1-1 timer, Linux v7.2 `volumes.c` and `sysfs.c`, smartmontools 7.5 `nvmeprint.cpp`, NVMe Base Specification 2.4) used by the new entry; S136 to S138 superseding S121, S122, S118 (routed defect 8).
- Rows touched old → new: none (no `status`, `recheck` or `used-by` change). Owed Gate records for round-25 rows S126 and S127 added from re-opened sources (digests equal the anchors).
- Frontier advanced: new frontier area "storage integrity" (PROVINCE.md section "Round-26 frontier — storage integrity" and its correction; README coverage row); the unopened scrub-documentation half of the old firmware-and-Btrfs lead is now opened (release notes and Fwupd remain unopened, recorded). Search-log note for round 26 appended in `corpus/SOURCES.md`.
- Sourced claim: C1 rests on S128 to S135 and S139.
- Mistakes mined (`corpus/lessons/round-26.md` `## Mistakes` and "Mistakes added after wave 2"): R26-UNDISCLOSED-INPLACE, R26-GATE-RECORD-MISSING, R26-SELF-REFERENT-ORDINAL, R26-PREMISE-BEFORE-SOURCE, R26-GATE-COLUMN-OFFSET, R26-SELF-AGREEMENT-ORDINAL, R26-TEACHES-OVERSTATED, R26-DRAFT-DRIFT, R26-LEAD-OVERSTATED; criteria QUALITY 60 to 66, each citing the lesson.
- Sibling source from the session note (mori `system-pressure-r24.md@4f05dd5a`): re-read only for the owed S127 Gate record; no new row.

## Trend verdicts

- **expansion: improved (provisional, owed to the outside spot-check).** New admitted entry on ground the coverage map did not hold (wave-2 CritLearningClaim and CritTrendVerdicts: no storage-integrity statement in the lane at `e9f5356c`), every source a `mined` tier-A row, coverage-map row and frontier paragraph added.
- **quality: unchanged.** S136 to S138 supersede overstated teaches cells and the old JSON statements of MP4 and MP6 are now marked, but no prior admitted entry was superseded by a stronger one or re-verified (QUALITY 49), and the new entry itself needed wave-2 corrections. Every error found is marked by an appended correction, so no admitted entry is left false and unmarked.
- **discernment: improved (provisional).** Round-25 routed defects 1 to 3 became Mistakes rows and grounded QUALITY 60 to 62; wave-2 disagreements became lessons and QUALITY 64 to 66; the lesson corrects its own overstated dispositions. The outside spot-check of round 26 is owed and not self-granted.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md` box 1 evidence line (round-26), `SKILL.md` section `## Storage integrity — round 26` plus its wave-2 notes; no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/host-health-report-r3.md`, `LOG.md` round-3 and round-26 entries (capture → entry → operator actions).
- [~] Instructions executable by an agent without oral context — `SHONEN.md` box 3 evidence line; whole-SKILL retest not executed (`corpus/knowledge/executor-test-sufficiency.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-26 frontier paragraph and its correction (free space split by question with mori); box 4 evidence line overstates "acknowledgement unobserved" (lesson late notes).

## Round shape, seats and process

- Shape: default two v1 waves (policy `scripts/hyaku/ufo-wave-policy.json`). Wave 1 build: 33 seats (16 scribe, 4 reviewer, 3 executor, 3 critic, 3 scout, 2 mutation-tester, 1 connector, 1 sentinel). Wave 2 falsify: 35 seats (26 reviewer, 4 critic, 4 mutation-tester, 1 scout). Round total 68; attack roles (reviewer, critic, mutation-tester) 9 + 34 = 43 of 68 (63 percent). No residual call.
- Planner seat: held by the L1 (validator rejects `planner`).
- Dead seats: wave 2 MutC1Run, MutC2Run, MutC1GateParse, MutC2Ordinal died at start (2.5 s each) with "Error: No model selected. Use /login, set an API key environment variable, or create /home/vgpnk/.omp/agent/agent.db". 4 of 35 (11 percent); not replaced; the L1 ran the mutation evidence itself.
- Slow seats: five wave-1 seats (DraftEntry, ScribeRouted1Scorecard51, ScribeGateS126S127, ScribeMistakes, ExecMemCheckerHarden) ran 59 to 87 minutes; the L1 integrated their items itself and asked them to report; all returned before wave 2. Every seat of both waves returned before this report.
- Seat gate: `wave-slot.sh acquire` granted both waves (r26-w1 33, r26-w2 35); both released after every seat returned. No job-cap refusal.
- Payload deviations, recorded: one `solutionSpace` string added per task as the tool requires; and in both waves each task text also carried the operator's tooling-directive block appended after the validator's text (not in the validated `taskCall`). Nothing else changed.
- Seat-to-seat messages were forbidden in every wave context; the L1 sent five wrap-up messages to wave-1 seats and one rule refinement to ExecSelfAssessV2.
- Executors worked only in clones with push URL `/nonexistent/no-push-to-lane`; `jj-lane.sh state` showed `ahead=0` before each helper commit.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` shows no file written by a round-26 seat (wave-2 ScoutLeftovers; the fleet-root `write` file predates the round).
- Cross-lane observation for mori (reported, not absorbed): `/tmp` is now an xfs partition on the second NVMe device, while mori's corpus records it as tmpfs (wave-2 RevProvinceReadme).
- Snapshot-boot premise P3: operator-owned; not claimed.
- Installs: none by the L1; every seat reported `Installs: none`.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open; this mission is progressing (nine lane-authored commits since launch).
- L0 questions: none opened this round.
