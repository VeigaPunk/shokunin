# souji — round 33 report (attempt 1, fresh-start round)

L1: SoujiR33 (hyaku run 9, block r33–r42). Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`.
Base 6017a482e7068d5afb7617640198fbb0fe743357 → final lane hash af7fd250c8a862130f88b8f77ad29debf343e54d (pushed; `git ls-remote origin refs/heads/master` prints it).
This round is a fresh-start round under the run-8 rule: the r30, r31 and r32 closures were rejected. I read those three closures and their spot-checks first. In all three rounds, C1/C2 targets were unreachable under their own frozen rules.

## Work performed

Declared claims (two; frozen at 2d9bca55a9f042a2c9ed60a797a8069e74c41f46, `census/round-33/preregistration.txt`):
- **C1 calibration (lowest axis, 7): capability-table currency.** 24 (command, stated outcome) pairs from the SCORECARD capability rows. Target: `mismatches=0` at the landing commit and at the tip.
- **C2 operability: the scratch-discipline repairs routed by the r32 closure, measured by executing them.** Five legs (O1–O5) and six no-harm guards (G1–G6). Target: `legs=11 pass=5 fail=0 harm=0` at the landing commit and at the tip.

Work items:
- Preregistration, frozen counters, item and leg files, and pre-freeze feasibility receipts (QUALITY Q70 legs a and b). Evidence: commit 2d9bca55a9f042a2c9ed60a797a8069e74c41f46 and `census/round-33/records/feasibility.txt`.
- Do-nothing controls under the frozen counters: C1 `mismatches=5`; C2 `pass=0 fail=5 harm=0`. Evidence: 3aec290ea5c4f3fe7f12a54e5b18e8072826ff92, `census/round-33/records/controls.txt`.
- Feasibility leg for the sandbox item shape (O1), run before wave w1 was dispatched. It reproduces why r32's O1 repair was reverted: `census/round-21/run-acceptance.py:503` compared a pinned r21 payload with the live tool. Evidence: fef88f2159f6380a4d1360f73365b3d595973a37, `census/round-33/records/feasibility-o1.txt`.
- C1 landing: five appended restatement rows (K04, K05, K16, K17, K18), each carrying an executed cause commit. Evidence: a416d0b26495ce78b76ea82316533bd8a9ef368c, `SCORECARD.md` `### Round 33 capability currency`.
- C2 repairs. Evidence: a7c35c24bdd8bae5cff9766ace02a81915756701. The changes:
  - `tools/souji-evidence-cache.py` and the `census/round-21/run-acceptance.py` gate-digest read;
  - `tests/fixtures/r15-census-config.py`;
  - `tests/fixtures/r15-preservation-frozen/regenerate.py`;
  - `tools/souji-census.sh` (`CENSUS_TMP_ROOT`);
  - `tools/souji-round9-selftest.sh`.
- r15 frozen re-pin, made by the fixture's own script and committed separately, with the arm counts in the commit message. Evidence: 756d77f0ccba35585055cc5cb4468028a6fbff5f, `census/round-33/records/repin.txt`. Two earlier attempts timed out under host load.
- Integration: lesson, QUALITY Q75–Q78, SKILL gate rows and an error pattern, SOURCES S224–S229 with snapshots, SCORECARD measurements, LOG. Evidence: 4d9bf0256f6f61a49ebfec55a524556090015f60.
- Final-tip receipt and wave capture: d65a5c4328896742d2ec951f7156c6a70aa9325a.
- Planner seat: held by the L1. The validator rejects `planner`, and no data-walk was delegated.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| preregistration, counters, items/legs, feasibility, start census | LOG.md `## 2026-10-26 — Round 33 attempt 1` | 2d9bca55a9f042a2c9ed60a797a8069e74c41f46 |
| do-nothing controls | same | 3aec290ea5c4f3fe7f12a54e5b18e8072826ff92 |
| O1 feasibility leg (before w1 dispatch) | same | fef88f2159f6380a4d1360f73365b3d595973a37 |
| C1 restatement rows | same | a416d0b26495ce78b76ea82316533bd8a9ef368c |
| C2 repairs | same | a7c35c24bdd8bae5cff9766ace02a81915756701 |
| r15 frozen re-pin (C2 landing commit) | same | 756d77f0ccba35585055cc5cb4468028a6fbff5f |
| integration (lesson, QUALITY, SKILL, SOURCES, SCORECARD, LOG, records) | same | 4d9bf0256f6f61a49ebfec55a524556090015f60 |
| final-tip receipt, census end, wave-1 capture | same | d65a5c4328896742d2ec951f7156c6a70aa9325a |

## Before → after measurements

- **C1** — `flock <scratch>/c1.lock python3 -B census/round-33/c1-counter.py --root <lane> --rev <full40> --list-rev 2d9bca55a9f042a2c9ed60a797a8069e74c41f46 --scratch <dir>`
  - Before (do-nothing at the preregistration): `SUMMARY items=24 agree=19 mismatches=5 restated=0`.
  - After at the landing commit a416d0b26495ce78b76ea82316533bd8a9ef368c: `SUMMARY items=24 agree=24 mismatches=0 restated=5`.
  - At the C2 repair commit a7c35c2…: the same reading.
  - At the tip: `SUMMARY items=24 agree=24 mismatches=0 restated=5` at 4d9bf0256f6f61a49ebfec55a524556090015f60 (load ~11 → 7).
  - Records: `census/round-33/records/c1-at-landing.txt`, `c1-at-c2-repair.txt`, `final-tip-measure.txt`.
  - **Met on the frozen counter. Self-verdict: value contested.** All five restated cells had already been restated at r30 (`R30-CORRECTION` R04, R05, R14, R15, R16) and superseded at r31 (L05, L06, L32, L33, L35). The frozen counter's before-state ignores those rows. What r33 adds is the executed cause commit for each row and a currency section that is re-run at the measured revision. I mined this as M3 and added QUALITY Q76.
  - Wave-1 seats also found counter loopholes: any digit-bearing line can serve as the statement, an argv correction may name an unrelated command, and `--only` reports a partial pass. None of the five landed rows uses these loopholes; each quotes its command's own summary line.
- **C2** — `python3 -B census/round-33/c2-counter.py --root <lane> --rev <full40> --base 6017a482e7068d5afb7617640198fbb0fe743357 --list-rev 2d9bca55a9f042a2c9ed60a797a8069e74c41f46 --scratch <dir>`
  - Before: `SUMMARY legs=11 pass=0 fail=5 harm=0`.
  - At the repair commit a7c35c2…: `pass=4 fail=1 harm=1` (G4 red until the re-pin).
  - At the C2 landing commit 756d77f0ccba35585055cc5cb4468028a6fbff5f: `SUMMARY legs=11 pass=3 fail=2 harm=0`.
  - At the tip: `SUMMARY legs=11 pass=4 fail=1 harm=0` at 4d9bf0256f6f61a49ebfec55a524556090015f60 (O3 FAIL; O4 PASS at low load).
  - **MISSED** (honest stop). O1, O2 and O5 pass, and all six guards pass.
  - O3 fails because `regenerate.py` runs the namespace arm. That arm's fixture, `tests/fixtures/r14-census-boundary.py:691`, still writes to a literal `/var/tmp`, and its bytes are pinned as `NAMESPACE_SHA256` (`tools/souji-preservation-evidence.py:307`) under the standing NAMESPACE hold. I did not touch it. My feasibility leg covered only the item's shape, not the item itself (M5, Q78).
  - O4 fails because the census selftest flips between runs: `1 failed` without the slash and `2 failed` with it, against `0 failed` at base. A run under load at the repair commit even read base `6 failed`, so a PASS there would only have been two flaky runs agreeing.

## Sources & frontier

- Census start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` printed `souji ok`, exit 0 (36 W04 lines; `census/round-33/records/census-start.txt`). Census end: `souji ok`, exit 0 (`census/round-33/records/census-end.txt`).
- Rows: 147 → 153. Counting command: `grep -cE '^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. All six new rows are tier A; each source was opened live on 2026-10-26.
  - Admitted (`mined`): S224 POSIX.1-2024 §3.254/§4.16 (repeated slashes), S225 proc_pid_fd(5), S226 Python 3.14 tempfile.
  - Rejected and kept with reason and flip: S227 path_resolution(7), S228 readlink(2), S229 Python 3.15.2 tempfile.
  - Existing rows touched: none. A Round-33 provenance paragraph was added.
  - Snapshots: `census/round-33/sources/SHA256SUMS`. Gate quotes: `corpus/lessons/round-33.md` `## Gate`.
- Sourced claim: C2. Its mechanism (repeated slashes collapse in path resolution, but a byte comparison does not; readlink returns the target string; Python tempfile tries `TMPDIR` first) rests on S224–S226. The SKILL error-pattern bullet and the lesson cite them.
- Mined mistakes: M1 capability-currency, M2 unrun-reading (r32 D2), M3 before-state artifact, M4 measurement collision (a fixed `/var/tmp` path in historical r23 fixtures, plus load), M5 feasibility checked per shape instead of per item. Each has a fix that is shown able to fail.
- Assimilation: none. The `merge/souji/` sweep found 12 hits and 0 admit candidates. Two rejections are recorded in the Gate. Id-collision check: 147 registry ids, 134 staged ids, 39 collisions; nothing was appended.
- `considerthese/`: absent in this lane.
- Frontier rows advanced: none. F1–F5 are unchanged.
- r32 spot-check routed defects:
  - Item 2 (C2) was taken as this round's C2. The trailing-slash fixes and both literal `/var/tmp` scripts landed; T08 was repaired, though its leg passed only via the consumer change. T18 was not taken.
  - Item 3 (D2) is mined as M2.
  - Items 1, 4, 5 and 6 carry to r34 (SCORECARD `### Planned (appended at round 33)`).

## Trend verdicts

- **expansion: unchanged.** No knowledge entry was admitted. The new SOURCES rows ground a mechanism, not uncovered ground. No capability row entered from C2, and the C1 counter row only records an instrument.
- **quality: improved.** The two trailing-slash regressions and three of the five routed literal-`/var/tmp` scratch roots are repaired with execution receipts (O1, O2, O5 PASS). The r15 pin was regenerated by its own script with unchanged arm counts. There is no harm under the six guards.
  - Against this: C2 missed and O3's r14 dependency stays open.
- **discernment: unprovable-but-better (pending the non-author spot-check).** Q75–Q78 each cite the r33 lesson. M3 is a self-found flaw in this round's own C1 before-state. The non-author spot-check has not run yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md gate rows `r33-c1-counter`, `r33-c2-counter` and the r33 trailing-slash error-pattern bullet (S224–S226)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep); LOG.md `## 2026-10-26 — Round 33 attempt 1`
- [~] Instructions executable by an agent without oral context — `census/round-33/c1-counter.py`, `census/round-33/c2-counter.py`; `census/round-33/records/controls.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — wave-1 sibling-overlap scan (seat SwarmConnector43): no contested scope; PROVINCE.md unchanged this round

## Round shape and seats

- Shape: one v1 wave, w1, with 48 seats: critic 21, executor 11, scribe 5, connector 3, scout 2, mutation-tester 2, reviewer 2, revenger 1, simplifier 1. Flash share 81 %, attack share 52 %.
- `w1.ready` was written at 13:05 and dispatched at 14:12:17. All 48 reports landed, with 0 dead seats. WAVE-DONE for w1 arrived after this report was first filed (bc8045f684efa2a5368296866c9620a415d00729). Its `w1-results.json` (seats=48; every entry noted "orchestrator kernel restarted mid-wave; seat output … not retained — read the seat report file") is captured at `census/round-33/waves/w1-results.json` (lane commit af7fd250c8a862130f88b8f77ad29debf343e54d). Seat counts come from the 48 committed reports. Filing before WAVE-DONE is a process defect of this round.
- Wave 2 (37 attack items, `make-spec-w2.py`) was built but **not dispatched**. My request budget ran out while wave 1 and every measurement crawled under host load (1-minute load 60–95).
- Round total: **48 seats, below the 64-seat floor**. This is a conformance defect.
- No residual task call was made.
- Seat-reported PARTIALs: SwarmReviewer46 (C2 has no junk control; `sandbox-nt` has no work witness; O4 is flaky; "C1 landing commit" was undefined) and SwarmSimplifier48 (spec text). Both are recorded in the lesson.

## Other

- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.ufo/reports/round-48/tameshi.md` (another lane's file, untouched) and `.scratch/`. None of my seats wrote to the fleet root.
- Inherited state: the lane was clean at start. No `lane-dead-no-report souji round=33` line exists.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. pacman stayed paused.
- Scratch: `/fast/scratch/hyaku/souji-r33` was removed after landing (removed with `rm -rf` after the final commit).
- Holds: Certification is OFF; K5, F5 reap and NAMESPACE holds are unchanged.
- Open L0 questions: none filed.
