# mori — round 24 report (attempt 2)

L1: MoriR24, a fresh in-session lane subagent. The lane's pushed tip is `4f05dd5a32055e85a9297eb8fc8dfec7dfc4625e` (branch master, and `jj-lane.sh state` shows `ahead=0 behind=0`). The round started at `c725aa37aa3c9ec4f34e3c2abc8ca1b616c7c130`. Attempt 1 was a stale author from 2026-10-21. It was not resumed, and its private trees under `/fast/scratch/hyaku/mori-r24-author*` were not reused.

## Work performed

The round declared two claims (`.ufo/waves/round-24/contract.md`, landed at `29c1bf45` before any implementation, with amendments A1–A5 landed before the code they govern):

- **C1 (calibration, the lowest active score at 5): repair the routed round-23 defects.** The new tool `tools/mori-routed-check.py` checks four byte-checkable items from `corpus/lessons/round-23-verifier-spotcheck.md:60-66`.
  - R4 is the repair: each dispatch must be bound before its call.
  - R1–R3 are regression guards.
  - Routed item 5 is an adjacency boundary that has no byte predicate. It is a why-not and is not counted.
- **C2 (coverage 6, frontier FR12): a capability to read system CPU, IO and IRQ pressure.** The new tool `tools/mori-pressure.py` reads `/proc/pressure`. It comes with sourced knowledge in `corpus/knowledge/system-pressure-r24.md`. This is the round's learning claim.

Work items:

- **Declaration and binding.**
  - The declaration and contract landed at `29c1bf45`.
  - Each wave's payload was committed before its task call: wave 1 at `06d4f4d2` (call `at` 05:14:13-03:00) and wave 2 at `753d2273` (call `at` 05:56:44-03:00).
  - Both were bound with `tools/mori-dispatch-ledger.py`. The evidence is `.ufo/waves/round-24/wave{1,2}-attempts.json` and `evidence/wave{1,2}-bind.json`.
- **C2 cases frozen first.** A separate executor seat wrote twelve cases, P01–P12 (`tools/fixtures/mori-pressure/cases.json`), which landed at `f6a29702`. The tool landed afterwards at `6ee62487`.
  - `tools/mori-freeze-order.py` grades this order `pre-build` (`evidence/freeze-order-c2.json`, exit 0).
  - The frozen register itself carries `tip: null`, which the tool rejects (exit 2). That is lesson M2. The measurement used a copy, `evidence/c2-freeze-check-register.json`.
  - The tool seat read the cases while it was building (`w1/BuildPressureTool.md:228`). The bytes therefore show the order, not that the tool was written independently of the cases (lesson M8).
- **C1 tool.** It landed at `88f96200` and was hardened at `1046aca3` and `575a9f3f` after wave 2 found three bypasses:
  - added content lines that begin `++ `;
  - a worktree `.gitattributes` that marks LOG.md as binary;
  - a file name under `tools/` that is not valid UTF-8.

  Each fix was probed in a sandbox clone: the old tool held 4, and the fixed tool turned red (see the lesson).
- **Sources.** Eight wave-1 scribe seats opened sources this round, and wave-2 reviewers re-opened them.
  - S090–S096 were admitted at tier A: Linux v7.2 psi.rst, psi.c, cgroup-v2.rst, init/Kconfig, kernel-parameters.txt and psi_types.h, plus the commit `52b1364ba0b1` that added PSI_IRQ.
  - S097 (proc_pressure(5)) was rejected because the page returns HTTP 404.
  - The Gate rows are in `corpus/lessons/round-24.md`.
- **Knowledge, SKILL and PROVINCE.**
  - New knowledge entry with twelve facts, a decision table, limits, and a corrections section that responds to wave 2.
  - `SKILL.md` gained a "Reading system pressure" decision table and two registry rows.
  - `PROVINCE.md` and `corpus/README.md` gained appended notes. The Core advance is marked pending admission. The resident trigger watcher and cgroup-scoped pressure stay in Frontier.
- **Wave-2 responses to C2.** These were added after the measurement and do not count toward the 12:
  - matcher negative controls (`MATCHER: rejected 48/48`);
  - a supplementary case file, written with the tool rather than frozen before it (`PASS 7/7`);
  - non-UTF-8 content is now labelled `malformed`;
  - a counter that went backwards no longer hides a threshold breach;
  - a committed live bracket check, which passed 5 of 5 runs (`evidence/bracket-check-run.json`).
- **Mistake mining.** `corpus/lessons/round-24.md` `## Mistakes` holds M1–M9. M1 is the round-23 record writing labels and numbers as one token (256 fused tokens). Its check failed on the round-23 text. On this round's 502 added lines it gives 28 hits, and all 28 are identifiers, so it needs an allowlist before it can gate. M2 is the unreadable register, shown failing with exit 2.

## Landed changes

All lane commits went through `jj-lane.sh`, and all are pushed. Each is tied to an entry in LOG.md: "round 24 attempt 2: declaration" and "outcome".

| Commit | Change |
|---|---|
| `29c1bf45` | declaration (SCORECARD, LOG, contract) |
| `06d4f4d2`, `4059ffb5` | wave-1 payload before the call; ledger and registry |
| `f7eb430c`, `11d8f71a`, `f299bd79`, `f38dbbdc` | amendments A1–A4 |
| `f6a29702` | frozen C2 cases and register |
| `6ee62487` | `tools/mori-pressure.py` |
| `06a7686e` | freeze-order measurement register |
| `88f96200` | `tools/mori-routed-check.py` and QUALITY 72–75 |
| `df4db54a` | S090–S097, knowledge entry, lesson, evidence |
| `6fce88a3` | SKILL, PROVINCE and README notes |
| `a730ecfe` | 33 wave-1 reports and A5 |
| `753d2273`, `13208d2a` | wave-2 payload before the call; ledger |
| `89849a76`, `6a344d25`, `c484f6d0` | pressure-tool responses to wave 2 and the bracket evidence |
| `a536b184`, `7c77fba3`, `1046aca3`, `575a9f3f` | knowledge and source corrections; routed-check fixes |
| `4f05dd5a` | measured outcome, capability rows, QUALITY wording, lesson corrections, 36 wave-2 reports |

## Before → after measurements

Both claims were measured at the lane tip `4f05dd5a32055e85a9297eb8fc8dfec7dfc4625e`.

- **C1.**
  - Before: `python3 -I tools/mori-routed-check.py --repo <lane> --rev c725aa37aa3c9ec4f34e3c2abc8ca1b616c7c130 --round 23` gives held 3 of 4, exit 1. R4 is red because 8 wave-1 ledger rows record an `at` earlier than their dispatch commit `22772c1`. The same command with `--round 24` at `c725aa37` gives held 3 of 4 (`no_round_ledger`).
  - After: `python3 -I tools/mori-routed-check.py --repo <lane> --rev 4f05dd5a… --round 24` gives held 4 of items 4, exit 0. The output is compact JSON, so the text reads `"held":4`. Timing mismatches went from 8 to 0.
  - Wave-2 reviewer RerunC1Count reproduced both values independently.
- **C2.**
  - Before: `git cat-file -e c725aa37:tools/mori-pressure.py` exits 128.
  - After: `python3 -I tools/mori-pressure.py --selftest` prints `MORI_PRESSURE_SELFTEST: PASS 12/12` and exits 0. It then prints `MATCHER: rejected 48/48 corrupted expectations`.
  - Wave-2 reviewer RerunC2Count reproduced the result, and so did the freeze-order check (`pre-build`).

## Sources & frontier

- **Census.** The command was `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.
  - At round start it exited 0 with six existing W04 warnings (S035, S037, S073–S076).
  - At round end it exited 0 with the same six W04 warnings and `ok`.
- **Rows.** The registry went from 89 to 97 rows. Tier A gained 7 (S090–S096) and tier C gained 1 (S097, rejected, with a reason and a flip condition).
- **Rows touched.** No older row changed. In-round corrections to S090, S093, S096 and S097 are logged old → new in the lesson. A new reading path and a round-24 search-log entry were added.
- **Frontier.** FR12 is narrowed, not closed: the one-shot system read is proposed for Core. The trigger watcher, cgroup-scoped pressure and the `--interval` rate stay in Frontier.
- **Sourced claim.** C2's knowledge entry cites S090–S096. Files that were read but have no registry row are labelled as pointers, not facts (wave-2 ReviewSourcesShape H1).

## Trend verdicts

- **Expansion: improved.** New sourced knowledge covers system CPU, IO and IRQ pressure, which was previously uncovered. The basis is S090–S096, the knowledge entry, a SKILL decision table, and one capability shown running (12/12, live bracket 5/5).
- **Quality: improved, bounded.**
  - Wave 2 found ten mutant kills and six survivors on the frozen cases. The responses to the survivors are disclosed and are not counted toward the 12.
  - Wave 2 also found three bypasses in the routed check, all fixed and probed, and six knowledge statements, which were corrected before this report.
  - The census is byte-identical to the start, and its selftest passes 134/134 before and after.
- **Discernment: improved.**
  - S097 was rejected.
  - EOPNOTSUPP is reported without inferring a cause, after a wave-1 critic showed the contract's cause was wrong.
  - C1's before-value was rebuilt so it measures the real round-23 defect instead of a value fixed by construction.
  - Statements from unregistered sources were demoted to pointers.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists and cited sources. Pointer: `SKILL.md`, Round24 section (cites S090, S091, S095, S096).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md. Pointer: LOG.md "round 24 attempt 2: outcome", with live pressure runs.
- `[ ]` Instructions executable by an agent without oral context.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate). Pointer: the PROVINCE.md round-24 adjacency bullet on tsukuroi's shared `/proc/pressure/memory`.

## Round shape and seats

- **Shape:** the default, two v1 waves, both validated under `ufo-wave-policy.json`.
  - Wave 1 (build) had 33 seats: 12 scribe, 5 executor, 5 critic, 4 scout, 4 reviewer, 2 connector, 1 mutation-tester.
  - Wave 2 (falsify) had 36 seats: 16 mutation-tester, 14 reviewer, 4 critic, 2 scout.
- **Total:** 69 seats. There was no residual call. No seat died, and no seat was replaced (wave-2 ScoutWaveSettlement checked this).
- **Planner:** the L1 held the §3 planner seat.
- **Seat gate:** both waves were granted by `wave-slot.sh` (`r24-w1` 33 seats, `r24-w2` 36 seats) and released afterwards.
- **No-dispatch call:** one eval cell built a task-call coroutine that was never awaited, so it spawned nothing. The ledger records only the awaited call.

## Other items

- **Routed item 5, why-not:** configuration stays with tsukuroi and the operator, residue with souji, and reclamation with the operator. There is no byte predicate, so the boundary stays in PROVINCE Adjacent.
- **Known C1 limits:**
  - both timestamps are written by the lane, so a backdated commit passes;
  - `at` has no upper bound;
  - the separate-worktree and invocation-reporting clauses are unchecked.
- **Fleet health signal:** the census live run (wave 2) reported DRIFT with 30 findings, including a watchdog log last written at 08:31:57Z and unsettled aged waves. This is host and driver state, not an effect of this round.
- **Misroot sweep:** `git status --porcelain` at the fleet root shows no untracked file from this round's seats. Wave 1 left `/tmp` residue (lesson M7). The L1 removed only the directories its seat reports name; the remaining files are listed in the lesson.
- **Inherited state:** the lane's `.scratch/` (from 2026-10-21) and `tools/__pycache__/` are untracked and were left untouched.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Installs:** none, by the L1 or any seat. pacman was not touched.
- **Open L0 questions:** none.
