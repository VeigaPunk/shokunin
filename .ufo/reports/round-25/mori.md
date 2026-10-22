# mori — round 25 report (attempt 1, L1 MoriR25)

Lane tip (pushed, `jj-lane.sh` `landed`): `e0e33c118e1eea2d40241a58861b7d0ad536e062`. Entering tip `28b79d3d1b76824f0c825aabe6cb6c5dc49961bf`.
Contract: `mori-shokunin/.ufo/waves/round-25/contract.md` (declared `7634be75`; amendments A1–A5, each landed before the code it governs).
Scope frozen at Main's 11:43Z notice; nothing new was started after it.

## Work performed

Declared claims: **C1** calibration (lowest active score 5, tied with depth and freshness): repair the round-24 routed defects and the standing SCORECARD Axes table, counted by `tools/mori-routed-r24.py`. **C2** coverage (6), a capability and the round's learning claim: read the omp harness background-job runway with `tools/mori-job-runway.py`, sourced from S098–S104 and S112–S113.

- Contract and 21 frozen C2 cases before any tool: `7634be75`. Amendments A1 `51ddd019`, A2 `6a92d5ee`, A3 `042d75bd`, A4 `9b1a2f12`, A5 `efaa1578`.
- C2 tool landed after the cases: `09f55b62`; A2 abstentions and the co-evolved supplementary cases `9a3d5118`; empty-selftest guard `fbecc596`; supplementary R19–R24 from wave 2 `d3b7af2a`.
- C2 knowledge `corpus/knowledge/harness-job-capacity-r25.md` (`90ed9b77`, `cb51e846`, `02084f27`, `d3b7af2a`, `51dc8209`). Key facts: the effective cap is `max(1, floor(min(100, async.maxJobs)))`, computed at the one manager construction site (S099 `sdk.ts:2284`; installed binary byte 164406766, S102). Every running, non-queued bash, task and eval job in the root session tree counts (S098). Auto-backgrounded bash and eval fall through to the foreground at the cap (S112, S113). The settings page states no maximum (S101); the eval page says "default and maximum 100" (S103). The ceiling dates from the feature commit (S104).
- C2 evidence with revision headers: `evidence/runway-selftest.txt`, `runway-selftest-supplementary.txt` and `runway-live-run.txt` (`47b2b939`).
- SKILL error pattern for `Background job limit reached (100)` (`8ef481ea`); PROVINCE and README FR15 notes (`1888bc62`).
- C1 tool `e54b644b`, then D5 `e06d4a02`. D1 evidence `evidence/pressure-selftest.txt` (`7bb0fe61`). D2 sweep in place, including the K3 and P4 rows (`02084f27`). D3 correction line (`ec840f9d`). D4 rule, narrowed after it hid 212 tracked `.pyc` files (`e43d8831`). Axes table fixed (`e68855d5`).
- QUALITY 76–77 (`ec840f9d`). Survivor replay: all six round-24 survivors are killed at the tip, and supplementary pressure cases S08–S16 kill nine neighbours (`ec840f9d`).
- Lesson `corpus/lessons/round-25.md`: mistakes M1–M4, Gate, routed defects (`b5b126f5`, `8aa9fa41`). SCORECARD declaration, measured outcome, capability rows and corrections (`0099a391`, `8aa9fa41`). LOG (`0099a391`, `e0e33c11`).
- Dispatch binding: each wave payload was committed before its call (`0099a391`, `e5e1b7bc`), and each ledger is LEDGER_CLEAN (`129832e3`, `07a31ae8`). `mori-routed-check.py --round 25` held 4/4. Each attempt row copies the seat gate's own ledger line (`1792663083 34 mori r25-w1`, `1792668957 38 mori r25-w2`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| contract, frozen cases, SCORECARD declaration | LOG "round 25 attempt 1: declaration" | `7634be75`, `0099a391` |
| C2 tool, supplementary cases, evidence | LOG "round 25 attempt 1: outcome" | `09f55b62`, `9a3d5118`, `fbecc596`, `d3b7af2a`, `47b2b939` |
| C2 knowledge, sources S098–S113, SKILL, PROVINCE/README | outcome | `90ed9b77`, `cb51e846`, `8ef481ea`, `1888bc62`, `51dc8209` |
| C1 tool, D1–D5 fixes, evidence | outcome | `e54b644b`, `e06d4a02`, `7bb0fe61`, `02084f27`, `ec840f9d`, `e43d8831`, `e68855d5`, `9b1a2f12`, `26c84859` |
| wave records and seat reports | outcome | `129832e3`, `9ec786ec`, `07a31ae8`, `e0e33c11` |

## Before → after measurements

- **C1:** `python3 -I -B tools/mori-routed-r24.py --repo <lane> --rev <rev>`.
  - At `28b79d3d`: `items 4, held 0, mismatches 4`, hygiene red, exit 1 (`evidence/routed-r24-before-a5.txt`).
  - At `e06d4a02`, and re-run at `e0e33c11`: `items 4, held 4, mismatches 0`, hygiene held, exit 0 (`routed-r24-after-a5.txt`).
  - Reported in two parts:
    - the A1 set D1–D3 went 3 → 0 at `e54b644b` (`routed-r24-before.txt` / `routed-r24-after.txt`);
    - D5, added by A5 after that result, went 1 → 0.
- **C2 before:** `git cat-file -e 28b79d3d:tools/mori-job-runway.py` exits 128.
- **C2 after:** `python3 -I -B tools/mori-job-runway.py --selftest` prints `MORI_JOB_RUNWAY_SELFTEST: PASS 21/21`, exit 0, at `d3b7af2a` and `e0e33c11`. The cases blob `48df844a` is unchanged since `7634be75`.

## Sources & frontier

- Census (`scripts/sources-census.sh validate --root <fleet> mori`): start exit 0, end exit 0. The same six W04 warnings (S035, S037, S073–S076) appear both times.
- Rows 97 → 113, all tier A or C:
  - +9 admitted, `mined`, tier A: S098–S104 and S112–S113;
  - +7 rejected, tier C: S105–S111.
- No existing row was touched. S101's `teaches` cell was rewritten before the report (it overclaimed a contradiction).
- Each new row has a Gate line in `corpus/lessons/round-25.md`.
- Frontier: new FR15 "harness background-job capacity runway" (README and PROVINCE appended notes). The cap read moves to Core, pending admission. Still frontier: the live job count, the settings layers the tool does not read, and the per-root scope. No row was closed.
- Sourced claim: C2.
- Mined mistakes:
  - M1: stale selftest evidence, 3 of 15 re-run files stale, each landed with a tool edit;
  - M2: the L1's blanket ignore rule;
  - M3: string-presence predicates;
  - M4: the late A5 widening.

## Trend verdicts

- **expansion: improved.** FR15 is new ground, with a knowledge entry citing 9 newly opened rows, a capability and a SKILL error pattern.
- **quality: improved.** The admitted `system-pressure-r24.md` was corrected in place: the K5, K4 and P3 body lines plus the K3 and P4 rows, with the banner removed. Not fixed: two F3 citation ranges.
- **discernment: improved.**
  - 7 rejections with flip conditions; wave-2 ReopenRejections agrees with all 7.
  - QUALITY 76–77 are lesson-backed.
  - Wave 2 corrected the S101 overclaim.

## Swarm and seats

- Shape: default, two v1 waves. The L1 held the planner seat; the bounded data walk rode the scout PlanDataWalk.
- Wave 1: 34 seats (12 scribe, 6 scout, 5 reviewer, 4 executor, 4 critic, 2 connector, 1 mutation-tester). All returned.
- Wave 2: 38 seats (15 reviewer, 13 mutation-tester, 6 critic, 4 scout); 25 of 38 seats are attack roles.
- Round total: 72. No residual call. No dead seat.
- At report time, some wave-2 seats were still running (reruns, three C1 mutation seats, reopens, code reviews). Their reports were not integrated. The wave-2 gate reservation was not released before the report.

## Disclosed weaknesses (wave 2)

- **C2 after-value is weak as a detector.** The pre-A2 tool `09f55b62` and a naive evaluator also pass the frozen 21. Mutants M3 and M6 (duplicate `async` keys) and M5 survive the counted file.
- **C2 can return a false number.** `RUNWAY_DEFAULT` reports effective 100, exit 0, for flow-mapping and JSON-form configs that omp reads as 50. This is recorded in the knowledge entry's decision table; the tool is not fixed (it is a defect for round 26).
- **Untested paths.** The CLI exit code and the unreadable-binary branch have no test.
- **Case authorship.** The L1 wrote the cases, not a separate seat.
- **C1 framing.**
  - D2 and D3 are lane self-records outside SCORECARD/SHONEN.
  - D5's pin is the lane's round-24 declaration; the closure confirmed only the calibration and coverage numbers.
  - A5 widened the claim after the 3-of-3 result.
  - The C1 tool has no selftest; three hygiene mutants survive the committed inputs.
- **Sentinel.** The three-rounds-running sentinel is tripped under the class reading, so round 26 must not count a routed repair.
- **Seat bound deviations.** Two seats ran `omp --version` once (SrcJobManager, SrcSettingsDefault).

Route to kumitate: facts F4–F9 of the knowledge entry are the OMP harness contract.

## Installs, L0, misroot, stale-lane

- **Installs:** bun 1.4.3+c6da4a4d3, official GitHub release, checksum-verified, into `~/.local/bin/bun`, installed by seat CriticC2Rules to run omp's own YAML parser. No pacman transaction.
- **L0:** one line appended (`mori | round-25 |`). It gives the evidence for the open hyaku capacity question and asks whether `scripts/hyaku/lane-addendum.md:88-89` and `await-capacity.sh:3` should be corrected.
- **Misroot sweep:** wave-2 ScoutMisrootSweep found no fleet-root path naming mori or round 25, so nothing was moved. It reports one kotoba misroot (`.ufo/waves/round-49/falsify/RowGameDev2d.md`), left to its owner.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the round-25 error pattern cites S098–S113 (`8ef481ea`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the live runway read is logged (`evidence/runway-live-run.txt`, LOG round-25 outcome).
- [ ] Instructions executable by an agent without oral context
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the FR15 note routes mechanism to kumitate and configuration to the operator (`1888bc62`, `51dc8209`).
