# souji — round 61 (attempt 1)
Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Lane tip at report time: `0256c2bc51391e7939995ece37d6a6fa3b85d468` (`git ls-remote origin refs/heads/master` prints the same hash). Campaign: run 15, hyaku phase 7, resume under operator Amendment 27 (2026-11-05).

## Work performed

**Declared claims: 1.** C1 calibration (the lane's lowest owned axis, score 7). Its move: the `--substance` arm of `tools/souji-freeze-check.py` requires a claim's red `Control:` receipt to have its exact bytes at a strict ancestor of the freeze commit (`CONTROL-ADDED-NOT-BEFORE-FREEZE`). Motivating defect: round 60 was rejected-harmed because both control receipts were added by the freeze commit itself while its preregistration said they were committed earlier (`corpus/lessons/round-60-verifier-spotcheck.md`; critic Finding 1 in `census/round-60/wave/w1/S60CriticRound/S60CriticRound.md`). The r60 arm could not see it. The numeric axis score is unchanged (no reproducible 0–10 mapping; closure rules admission). **C2 (receipt-writer fixture and mutant kill-power) was built by a wave seat and is not declared**: the critic classed its axis as coverage (r25 precedent), and the reviewer found the honest writer accepts skip-worktree concealment (`census/round-61/wave/w1/S61ReviewerC2.md` HIGH-1). It is routed to round 62.

Work items, each with an evidence pointer:

- Wave: one v1 wave, 12 seats, validated under `ufo-wave-policy.json` (band 8–16), dispatched by the orchestrator from `.ufo/waves/round-61/w1.ready` (dispatched marker `.ufo/waves/round-61/w1.ready.dispatched`), WAVE-DONE received for all 12 seats, results `census/round-61/wave/w1-results.json`, seat outputs `census/round-61/wave/w1/`.
- Protocol and fresh-start reads: fleet `MISSION.md`, `AXES.md`; canonical `PROTOCOL.md`, `CORPUS.md`, `LEARNING.md`, `skills/shokunin/SKILL.md`; lane `SCORECARD.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md` (`## Frontier`); rejected closures r56–r60 and their spot-checks (`corpus/lessons/round-5{6,7,8,9}-verifier-spotcheck.md`, `round-60-verifier-spotcheck.md`); answers to each routed defect in `corpus/lessons/round-61.md` § Fresh-start reads.
- Candidate instrument (content-bound rule), `tools/souji-freeze-check.py` at `da7ceba3950fc3ac946a611791f56e12174272bd` (sha256 `5794ab27…1c5`). Replaces the add-commit rule that the wave's critic and reviewer showed blind to a receipt rewritten red at freeze (`S61CriticRound` F2, `S61ReviewerC1` HIGH-2). Default output without `--substance` is unchanged (the sweep below).
- Frozen matrix and counter: `census/round-61/c1-counter.py` (sha256 `7206e973…`), `census/round-61/build-matrix.py`, `census/round-61/c1-matrix.tsv` (12 rows), `census/round-61/matrix/` (12 case dirs, fixed-date fixtures; commit hashes pinned in each `expected.txt`).
- Do-nothing control: `census/round-61/controls/c1-do-nothing.txt` (base bytes in the new slot; red, EXIT=1), committed at `da7ceba3`.
- Freeze: `census/round-61/preregistration.txt` at `9849e71851e28d5f1e88ef658418d3c136f94692`, Base `c7228424`, Counter and Population digests at freeze, Control path = the do-nothing receipt. Freeze record check at the freeze revision: `census/round-61/records/real-r61-freeze-candidate.txt` (`SUMMARY claims=1 findings=0`, EXIT=0).
- After-measurement at the freeze revision (data, after freeze): `census/round-61/records/c1-after.txt`.
- Real-record arm: `census/round-61/records/real-r60-prereg-candidate.txt` (candidate: two `CONTROL-ADDED-NOT-BEFORE-FREEZE`, EXIT=1) and `real-r60-prereg-base.txt` (base: `findings=0`, EXIT=0).
- Selftests: `census/round-61/records/selftest-candidate-plain.txt` (`cases=41 pass=41`), `selftest-candidate-substance.txt` (`cases=15 pass=15`).
- Lane-history sweep, base vs candidate over all 37 `census/round-*/preregistration.txt` at full-40 `HEAD` in both modes: `census/round-61/records/substance-sweep.txt`.
- Erratum for round 60 (append-only, `SCORECARD.md` § Round 60 erratum, `R61-ERRATUM-R60`): both r60 control receipts are added by freeze `2670e96a…`; the prose "committed at `3b552509…`" is wrong (`git cat-file -e 3b552509…:census/round-60/controls/c1-do-nothing.txt` → EXIT=128). Evidence `.ufo/waves/round-61/w1/S61ExecRealRecord/erratum-evidence.txt`. Frozen bytes are not rewritten.
- Frontier step: `corpus/SOURCES.md` S290 and S291 admitted (`mined`); knowledge `corpus/knowledge/control-chronology-binding.md` (cites S290) and `corpus/knowledge/skip-worktree-concealment.md` (cites S291); re-opened S288 hash unchanged; captures `census/round-61/sources/` with `SHA256SUMS`.
- Quality criteria: `corpus/QUALITY.md` Q121 (every C/H wave finding surfaced in the lesson) and Q122 (content-bound chronology). Lesson `corpus/lessons/round-61.md` carries Gate, Mistakes, Named limits, a Q121 disposition table of every C/H finding, and fresh-start reads.
- Index and maintenance: `corpus/README.md` § Frontier (r61) indexes the three F1 entries (including the r60 entry that the r60 spot-check said was unindexed); `SKILL.md` § Round 61 documents the interface; the broken r60 evidence path at `SKILL.md:796` is corrected to `census/round-60/wave/w1/…`.

## Landed changes

| commit | content | LOG.md / SCORECARD.md |
|---|---|---|
| `da7ceba3950fc3ac946a611791f56e12174272bd` | candidate freeze checker, frozen counter, matrix, builder, do-nothing control (pre-freeze) | LOG `## Round 61` bullets 1–2; SCORECARD § Round 61 measurements |
| `9849e71851e28d5f1e88ef658418d3c136f94692` | frozen preregistration (freeze commit) | LOG `## Round 61` bullet 2 |
| `0256c2bc51391e7939995ece37d6a6fa3b85d468` | after-records, real-record and sweep evidence, wave evidence, sources, knowledge, Q121/Q122, lesson, README, SKILL, SCORECARD erratum and r62 plan, LOG entry | LOG `## Round 61` (all bullets) |

Every cited hash above is an ancestor of `refs/heads/master` (`git merge-base --is-ancestor`), and the lane state is `local=remote=0256c2bc…`, `ahead=0 behind=0`, `tracked=0 untracked=0`.

## Before → after measurements

Claim C1, one counter, two arms, one matrix. Counting command (both arms):

`python3 -B census/round-61/c1-counter.py --root . --matrix census/round-61/c1-matrix.tsv --base-tool-rev c7228424c3919ecf142bab1aec8181722d86467b --rev <commit> --work DIR [--new-arm plain | --new-tool tools/souji-freeze-check.py]`

| measurement | before (do-nothing: base bytes) | after (candidate) | commit measured |
|---|---|---|---|
| 12-case matrix | `new_forgeries=2 class_mismatches=2 stubs=REJECTED`, EXIT=1 (`census/round-61/controls/c1-do-nothing.txt`) | `matrix=12 base_forgeries=2 base_honest=4 new_forgeries=0 new_honest=4 class_mismatches=0 stubs=REJECTED`, EXIT=0 (`census/round-61/records/c1-after.txt`) | `--rev 9849e718…` (freeze); candidate tool `da7ceba3…` |
| real r60 freeze record | `SUMMARY claims=2 findings=0`, EXIT=0 | `CONTROL-ADDED-NOT-BEFORE-FREEZE` ×2, EXIT=1 | `--rev d05a0001…` (r60 tip) |
| real r61 freeze record | n/a (r61 freeze) | `SUMMARY claims=1 findings=0`, EXIT=0 | `--rev 9849e718…` |
| lane sweep, 37 preregistrations, default path | — | 0 differences from base (`plain_diff=0`) | `--rev <HEAD full-40>` |
| lane sweep, substance path | — | 11 differences, all additions of `CONTROL-ADDED-NOT-BEFORE-FREEZE`; no base finding removed; round 60 flips pass→fail; rounds 41–55 were already red | `census/round-61/records/substance-sweep.txt` |
| candidate selftests | base `41/41`, substance `12/12` (base) | candidate `41/41`, substance `15/15` | `da7ceba3…` |

Axis scores: calibration 7, coverage 8, operability 8, unchanged. No axis is harmed by the measured data: the candidate adds refusals only, and it refuses no honest row in the matrix (`new_honest=4`).

## Sources & frontier

- SOURCES census: round start `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` → EXIT 0; round end → EXIT 0 (`souji ok …/corpus/SOURCES.md`; advisory W04 duplicate-URL warnings: 68 at round end).
- Rows before → after: 213 → 215 by `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (base `c7228424` gives 213; working tree and tip give 215). Malformed rows: 0 (`awk` NF≠13 check).
- Rows added by tier: A 2 (S290 git-log path-limited history; S291 git-update-index skip-worktree NOTES caveat), B 0, C 0. Rows touched old→new: none (S288 re-opened, cells unchanged; S289 unchanged).
- Status: S290 and S291 `mined` (cited by their knowledge entries). S291 also carries the rejected inference "a silent porcelain status certifies content" (quote-rejected on the NOTES caveat; discernment sample).
- Frontier rows advanced: F1 (git-native housekeeping vs receipts), two entries on receipt chronology and receipt-instrument worktree blindness. F1 stays `frontier, entries held`; not promoted to Core.
- Assimilation: none. No `considerthese/` directory exists in the lane; no `merge/souji/` theme was adopted, no append from a shokuknow package was made, so no collision or quarantine check was required (the connector seat ran a read-only overlap scan: `.ufo/waves/round-61/w1/S61ConnSibling.md`).
- Non-author verification: S290 and S291 gate decisions are **pending** a non-author spot-check (LEARNING.md). The L1 does not self-attest the admits or the rejection.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries on F1 receipt-chronology ground, each citing a `mined` row (S290, S291); index rows in `corpus/README.md`. Evidence: `corpus/knowledge/control-chronology-binding.md`, `corpus/knowledge/skip-worktree-concealment.md`, `corpus/README.md` § Frontier (r61).
- **quality: improved.** The chronology gate now refuses the r60 defect shape and a rewrite-at-freeze shape the add-commit rule accepted (`rewritten-at-freeze`: base accepts, candidate refuses; `census/round-61/controls/c1-do-nothing.txt`, `census/round-61/records/c1-after.txt`); the r60 knowledge entry is indexed and the broken SKILL path is repaired. No admitted entry is found false in this round. Named limits are in `corpus/lessons/round-61.md`.
- **discernment: unchanged.** The round surfaces its own process gaps (lesson Mistakes M1–M4, including a critic finding that r60 left unsurfaced) and adds Q121, but the outside check of this round's gate decisions is pending. Recorded as `unchanged` until a non-author spot-check agrees or disagrees.

## Other report items

- **Stale-lane:** no other souji mission is open; this round's mission is the only one.
- **Tools:** none installed or updated; no pacman transaction (pacman stays paused). Scratch lived under `/fast/scratch/hyaku/souji-r61/` and is removed at landing.
- **Dead seats:** none (12/12 settled). Seats whose outputs were short or narrated were not counted as evidence.
- **Wave shape:** one v1 wave, 12 seats, no residual call. Roles: executor 3 (`S61ExecChronoArm`, `S61ExecRealRecord`, `S61ExecC2Fixture`), scout 1, scribe 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1, revenger 1. Attack share 4/12 (reviewer ×2, critic, mutation-tester; 33%). Planner held by the L1 (the wave validator refuses planner).
- **Open L0 questions:** none appended this round.
- **Inherited state:** attempt 1; `.ufo/watchdog.log` has no earlier `lane-dead-no-report souji round=61` line; no inherited uncommitted lane work.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `?? tools/` (`tools/mori-source-digest.py`, mori's file). It is not this lane's, so it was left in place. No souji-written fleet-root files.
- **Operator item:** this round's critic (F13 item 2, Q59) names a `## MACHINE BLOCK` preregistration requirement that the r61 prereg does not carry; the requirement is not confirmed as a gate on this lane's preregistrations, so it is routed to round 62 as a question, not a defect.

## Named limits

- Bytes, not execution: the chronology rule proves a receipt's bytes existed before freeze, not that a command produced them.
- History-bounded: merges that hide a path-touching ancestor make the check refuse (fail closed); the matrix is linear.
- F3 (delete and re-add at freeze with new bytes) is refused by the same rule but has no matrix row.
- Eleven historical freeze records (rounds 41–55 and 60) gain the chronology class; reported, not rewritten.
- C2 not declared. The honest receipt writer accepts skip-worktree concealment of a non-instrument file (HIGH-1); its fixture and mutants remain wave evidence in `census/round-61/wave/`.
- The mutation counter's `m1-newest-add` survivor is retired with the add-commit rule.
- A wave seat (revenger) showed the r60 tag case passed for an accidental reason; the r61 matrix uses the orphan-commit shape instead.

## SHONEN

Lane assessment, asserted by the author. No box is `[x]`; the non-author verifier is the closure.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` § Round 61 (gate-registry row); `corpus/SOURCES.md` S290, S291 rows; `corpus/lessons/round-61.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 61` (freeze `9849e718`; after-record `census/round-61/records/c1-after.txt`).
- [~] Instructions executable by an agent without oral context — `census/round-61/c1-counter.py` with `census/round-61/c1-matrix.tsv` and `census/round-61/matrix/`; recheck command in `corpus/knowledge/control-chronology-binding.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round; the sibling mechanisms are routed in `census/round-61/wave/w1/S61ConnSibling.md` (no overlap with other lanes' forks beyond name).
