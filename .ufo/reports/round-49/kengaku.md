# Kengaku round 49 — honest stop; neither claim admitted

## Work performed

Declared claims: **R49-C1 calibration** — repair fixture-fence honest over-refusal under a v3 counter with committed mutant floor; **R49-C2 coverage** — admit the TB2 `polyglot-c-py` package under a Q40 counter with tag coverage, probe repair, mutation floor, and stage-2→stage-3 receipt ordering.

- Froze both claims before data at `plans/round-49-claims.md` (`9d2900af41e4d1fc6022eff99010436fde6dbd93`); round-48 fresh-start provenance and routed defects are named in that file and `corpus/lessons/round-49.md`.
- Validated and dispatched one policy-v2 wave: 64 seats, 40 attack roles, L1 held canonical planner; dispatch/results: `kengaku-shokunin/.ufo/waves/round-49/w1-dispatch.json` and `w1-results.json`. WAVE-DONE reported 64 settled; 61 seat reports are present and `R49C2TagInv`, `R49C2MutOrder`, `R49C2MutReceipt` have no report files. Role counts from results: critics 15, mutation-testers 14, executors 11, reviewers 11, scribes 4, connectors 4, scouts 3, sentinel 1, revenger 1. No seat replacement.
- C1 before evidence: base fence `HONEST fixtures=120 admitted=112 refused=8`; candidate A reported 120/120 admitted with refusal 20/20 and sealed 12/12 on the same r48 120-case set. The new deterministic population is 124 fixtures, and the candidate was not measured on its four new cases. Candidate counter has selftests and a mutant-leg design but no stage-2 landed implementation or landing-tip score. Evidence: `kengaku-shokunin/.ufo/waves/round-49/w1/R49C1ExecCounter.md`, `R49C1ExecFenceA.md`, `R49C1ExecHonest.md`.
- C2: new dry table has 20 cases and includes violating cases for `both-print` and `toolchain`; repaired candidate probe passes `--stage-check` 18/18, while old `22b7779e` fails 18/18 on this host. A stub-grade control shows seed+recipe are run by the repaired candidate. Counter candidate exercises ordering attacks and controls in scratch, but its stage-2/3 fixture uses r46 stand-ins and still reports V7 defect; no real stage-2 amendment, fresh stage-3 receipt, or scored landing run exists. Evidence: `kengaku-shokunin/.ufo/waves/round-49/w1/R49C2ExecCases.md`, `R49C2ExecProbe.md`, `R49C2ExecCounter.md`, `R49RevClosure.md`.
- Reopened S166 at the pinned raw URL on 2026-10-28; HTTP 200, SHA-256 `b94a7a9882decd8114835bdf52b5bc42fc78e9fe67ecad9bd19050b11781ddec`, byte-equal to committed capture. Quote at `test_outputs.py:27`: `test_cases = [(42, "267914296"), (10, "55"), (0, "0")]`. Gate records S166 accept and tbench.ai hub lead reject in `corpus/lessons/round-49.md`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only unrelated chousa report, orchestrator scratch files, and `o.bin`/`oldrep*.out`; no kengaku seat bytes were copied or removed.
- No tools installed or updated; no pacman transaction attempted. Stale-lane: this round completed with report committed; no other mission of this lane is open.

## Landed changes

- Stage-1 claims freeze, wave dispatch/evidence, round-49 lesson, LOG and SCORECARD honest-stop rows landed in lane commit `71f5f5f77591d8c3d19297ee9785436da45209e4`. LOG entry: `LOG.md` Round 49; score/claim rows: `SCORECARD.md` Round 49; lesson: `corpus/lessons/round-49.md`.
- Lane remote `master` verified at `71f5f5f77591d8c3d19297ee9785436da45209e4` (`jj-lane.sh state`: local=remote, ahead=0, behind=0).
- Claims verdicts: **R49-C1 not admitted / unverified**, calibration 8→8; **R49-C2 not admitted / unverified**, coverage 7→7 (L0 cap). No score or capability entered; no axis harm observed. Candidate-only evidence is not represented as a landed improvement.

## Before → after measurements

- **R49-C1 — calibration.** Counting command for the baseline receipt: `python3 plans/round49_c1_verify.py --lane .` is the frozen command, but the counter is not present in the committed landing tree, so no before/after landing-tip pair exists. Candidate selftest at `REV 9d2900af…`: base fence on 120 cases `HONEST fixtures=120 admitted=112 refused=8`; repaired variant A on the same 120 cases `HONEST fixtures=120 admitted=120 refused=0`, `REFUSALS total=20 clean=20`, `SEALED total=12 clean=12`. The stage-2 124-case population and landed mutant floor were not scored; claim not admitted.
- **R49-C2 — coverage.** Frozen counting command `python3 plans/round49_c2_verify.py --lane .` is absent from committed landing tree; no before/after landing-tip pair or full probe receipt exists. Candidate evidence: old probe stage-check `cases=18 failed=18`; repaired candidate `cases=18 failed=0`; amended dry table has `cases=20 predicted_pass=8 predicted_fail=12`. These are candidate controls, not admission; V7 and the real staged package remain unverified.

## Sources & frontier

Start and end census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.

- Before: exit 0; 165 rows; tier A=141, B=22, C=2; status mined=149, queued=8, rejected=8; `kengaku ok`.
- After: exit 0; 165 rows; tier A=141, B=22, C=2; status mined=149, queued=8, rejected=8; `kengaku ok`.
- Rows added by tier: A=0, B=0, C=0. Rows touched old→new: none. Frontier rows advanced: none. S166 was re-opened this round but its existing row was not changed. Assimilation: none.

## Trend verdicts

- **expansion — unchanged:** no `corpus/knowledge/` entry or `SOURCES.md` row was added, and the source census remains 165 rows.
- **quality — unchanged:** no admitted knowledge entry was re-verified, superseded, or falsified; C1/C2 candidates were not admitted.
- **discernment — unprovable-but-better:** L1 reopened S166 and rejected one live hub lead with a located basis, but the required non-author spot-check of at least one admit and one reject is not yet available; dispatched seats are lane-author evidence. No outside discernment improvement is claimed.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
[~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:7`
[~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`
[~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:129`
