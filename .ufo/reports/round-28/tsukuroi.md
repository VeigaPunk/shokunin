# tsukuroi — round 28 report (attempt 1, 2026-10-22, L1 TsukuroiR28)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`; claim base `3b9e0430b88d01415c241dd5a18b8939b8a520ac`; lane branch `master` = remote = **`ca6b14997a97dd024194633a4135674079f1affe`** (helper `landed` line). Short box (dispatch 18:50Z); two small repair claims from the round-27 routed list.

## Work performed

Declared claims (`SCORECARD.md` section "Round 28 — declaration, attempt 1", landed `f8e3a8f2`):

- **C1 (adjacency, 8):** `tools/check-adjacency-overlap.py` refuses the 24 should-fail register shapes of round-27 CritC2Tool (routed defect 2), live register control stays 6. Command: `python3 tools/mutants-adjacency-overlap.py --base <REV> --counter-rev <REV>` → `should_fail_accepted`, `control_live_anchored_rows`.
- **C2 (depth, 8):** `tools/check-kernel-taint.py` refuses the five routed should-fail shapes (routed defect 3: one-word quotes ×2, quote from an uncited source; plus Gate heading substring and Gate source-cell bugs), live entry control stays 6. Command: `python3 tools/mutants-kernel-taint.py --base <REV> --counter-rev <REV>` → `should_fail_accepted`, `control_verified_rows`.

Work items:
- C1 counter rules B1-B7 with selftest 17 → 43 cases, and the committed battery rebuilt from round-27 CritC2Tool `driver.py`/`driver2.py` (`f8e3a8f2`; repaired after wave 1 in `9a0654ba`).
- C2 counter rules R4a-R4c, docstring R4 corrected (R27-CHECKER-DOC-LAG), selftest 46 → 52 cases, and the committed battery from round-27 CritC1Tool `mutants.py` (`79d4264d`; R4b normalisation in `9a0654ba`).
- Registry rows for both batteries: `SKILL.md` "Gate and probe registry — round28" (`bd5bd683`); `check-registry-coverage.py` 33 of 33, exit 0 (`.ufo/waves/round-28/measure/final2/registry.json`).
- Frontier: S146 mined, S147 rejected; lesson `corpus/lessons/round-28.md` Gate, routed-defect dispositions, Mistakes (`9a0654ba`).
- Routed 7: QUALITY 69 names R27-SIBLING-POINTER-DRIFT; new QUALITY 73 (R28-BATTERY-MEASURE) (`9a0654ba`).
- Measured outcome, axes self-assessment (round 28) clearing the inherited K10 stale count, LOG entry (`938ca8ec`); `check-self-assessment.py --revision 938ca8ec` → PASS, 0 mismatches (`measure/final2/self-assessment.json`).
- Wave-1 findings repaired before closing: four-space-indented PROVINCE table newly accepted and `./` lane paths past B5 (CritC1NewShapes, CritAxisHarm); over-strict B3 window and LANE-GAP cap (CritC1OverStrict); three old selftest cases no longer discriminating (CritAxisHarm 3, re-checked: each removed rule now fails the selftest); R4b false refusal for object-shaped sources (CritC2RuleDesign 2); missing registry row (CritClaimSizing 7).

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `f8e3a8f2960b26ba5027d2298e50d5c9d6564cc0` | declaration; C1 counter B1-B7; `tools/mutants-adjacency-overlap.py` | LOG "Round 28" |
| `79d4264d66de8a9bccc3b6370a54e87ad4ef65ae` | C2 counter R4a-R4c; `tools/mutants-kernel-taint.py` | LOG "Round 28" |
| `bd5bd683499039a5262de5f0c47008fc8d33f0cc` | `SKILL.md` registry round28 | LOG "Round 28" |
| `9a0654ba8eb053a39e6374a97a25d91f6464b965` | wave-1 repairs of both counters; QUALITY 69/73; SOURCES S146/S147; lesson round-28; wave-1 evidence and receipts | LOG "Round 28" |
| `938ca8ec564f911df22162cec64ae3c48a9f1eb5` | measured outcome, axes table round 28, LOG entry, final receipts | LOG "Round 28" |

| `ca6b14997a97dd024194633a4135674079f1affe` | residual CritC2OverStrict repair (R4a floor 16 → 10 characters, Gate `Id`/`Source id` column read first; 55-case selftest); lesson residual section and Mistake R28-SEAT-COMMITTED-IN-LANE; residual reports and `measure/final2/` receipts | LOG "Round 28" |

Gates at `ca6b1499`: C1 battery 0 of 24, control 6; C2 battery 0 of 5, control 6; `check-kernel-taint.py --revision` 6 rows; `check-self-assessment.py` PASS, 0 mismatches; `check-registry-coverage.py` PASS; sources census exit 0; lane worktree clean.

**Lane HEAD repair (orchestrator-approved 19:17Z).** A wave-1 seat committed battery mutants inside the lane at 16:13 -03 (sandbox commit `a330fb0dfad349c0a3d6583cf1f64f4cc45ca241` and children `ee430cd`, `f92e181`, `db56413`, `2f2db7a`; B2-family mutant names, seat RevFamilyB2 by assignment and timing), leaving git HEAD detached at `a330fb0` and the helper refusing ("working copy has changes on a non-tip base"). Before: `git rev-parse master origin/master HEAD` → `938ca8ec…`, `938ca8ec…`, `a330fb0d…`; `jj-lane.sh state` → `local=938ca8ec… remote=938ca8ec… ahead=0 behind=0 head=detached`. Ran once: `git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin update-ref --no-deref HEAD 938ca8ec564f911df22162cec64ae3c48a9f1eb5` (exit 0). After: all three `938ca8ec…`, master and origin/master unchanged; the helper then landed `ca6b1499`. The sandbox chain was not touched. Recorded as Mistake R28-SEAT-COMMITTED-IN-LANE in `corpus/lessons/round-28.md`.

## Before → after measurements

| Claim | Before | After | Measured at |
|---|---|---|---|
| C1 | 19 of 24 accepted (counter `dd94cb1f`, data `3b9e0430` and `9a0654ba`/`938ca8ec`) | **0 of 24**, control 6, exit 0; `should_pass_accepted` 4 | `79d4264d`, `9a0654ba`, `938ca8ec`, `ca6b1499` (`measure/c1-*.jsonl`, `measure/final/`, `measure/final2/c1-after.jsonl`) |
| C2 | 5 of 5 accepted (counter `75f410c8`, data `3b9e0430` and `938ca8ec`) | **0 of 5**, control 6, exit 0 | `79d4264d`, `9a0654ba`, `938ca8ec`, `ca6b1499` (`measure/c2-*.jsonl`, `measure/final2/c2-after.jsonl`; `ca6b1499` re-run by the L1 before this report) |

Independent re-derivations: RerunC1Battery (19/24 and 0/24, both data bases), RerunC2Battery (5/5 and 0/5 at `9a0654ba`, cross-run shows the counter bytes carry the change), ExecC2BeforeReplay (5/5 before), RevC1Repairs (0/24 at `9a0654ba`; the wave-1 repairs refuse 6 more shapes and flip no case the wrong way). Residual MutC2Counter: R4a's 2-word half has no independent anchor (two mutants survive) — owed. RevC1Repairs: 15 of 22 wave-1 padding shapes still score 6 and C1 residuals are only in wave reports — owed. Disclosed: C1's 0 of 24 was first seen on uncommitted bytes before the declaration commit (Mistake R28-RUN-BEFORE-DECLARATION).

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`: start exit 0 (145 rows; ExecSourcesCensus, 25 W04 advisories); end exit 0 (147 rows; `measure/final2/census.txt`, last line `tsukuroi ok`). Rows added: S146 tier A `mined` (Stryker mutant states; located quote "When all tests passed while this mutant was active, the mutant survived. You're missing a test for it."), S147 tier B `rejected` with reason and flip (pitest basic concepts; JVM code-mutation mechanism, no operand in a data gate; tameshi ground). Rows touched old→new: none existing. Sourced claim: both batteries and the lesson cite S146 (`used-by`). Mistake mined: R28-RUN-BEFORE-DECLARATION, captured-by none, fix QUALITY 73 with a committed ordering check that fails on round 28 and passes on round 27 (`.ufo/waves/round-28/w1/ScribeMistake/check-order.py`). The Gate records a reject decision (routed 1).

## Trend verdicts

- **expansion: unchanged.** No new domain ground; two counters hardened, two sources registered.
- **quality: improved.** Two evidence counters now refuse the routed should-fail shapes they accepted (19→0 of 24, 5→0 of 5) with live controls intact; docstring R4 corrected; QUALITY 69 link repaired. Limits: CritC1NewShapes lists further padding shapes still accepted (duplicated anchors, PROVINCE-mirror lane quotes, withdrawn markers, clipped words); C2 still accepts eight other CritC1Tool shapes (`other_accepted`).
- **discernment: improved.** The round-27 outside check's routed defects became the claims and a reject decision; wave-1 attacks changed the counters before closing (six repairs listed above). Contested: CritClaimSizing argues both claims are operability moves (one claim on an axis at 9), so the lowest-axis duty is unmet — reported for the operator; targets not narrowed.

## SHONEN

- [~] SKILL.md real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry round28 adds two rows (`bd5bd683`); author evidence only.
- [~] One end-to-end domain task executed and logged — unchanged this round (`SHONEN.md` box 2 pointers).
- [~] Instructions executable without oral context — batteries document usage in their docstrings (`tools/mutants-*.py:1-20`).
- [~] No cross-domain bleed — S147 rejected partly as tameshi ground (OUT-010); mori items not absorbed.

## Round shape, seats and process

- Shape: one v1 wave (validated, policy band 32-64) plus one residual `task` call. **Wave 1: 35 seats** — 17 reviewer, 5 critic, 4 executor, 4 scribe, 2 mutation-tester, 1 sentinel, 1 connector, 1 scout (`.ufo/waves/round-28/w1-spec.json`, `w1-dispatch.json`); a planned labrat item was refused by the validator as a non-swarm role and re-filed as reviewer RevSiblingMode before dispatch. **Residual: 6 seats** (4 reviewer, 2 critic; `residual-dispatch.json`). **Round total 41.** No second wave: fewer than 32 attack items remained after wave 1. Planner seat: held by the L1.
- Dead seats (never replaced): RevFamilyB6, RevBatteryFidelity, RevC1Docstring, RevFamilyB7 — "Retry budget exhausted after 5 retries: Devin stream error resource_exhausted: Reached free model rate limit … Your limit will reset in 28 minutes (at 19:43 UTC)". RevFamilyB2 cancelled by the L1 at 19:15Z as the suspected writer of sandbox commits into the lane. Returned after the first draft and folded in: ExecRegistryCoverage (registry red at `f8e3a8f2`, green from `bd5bd683`), MutC2Counter, RevC1Repairs. Still running at report time: MutC1Counter, SentinelBattery, RevFrontierRows (findings not in this report).
- Observed answering models: minimax-code/MiniMax-M3.1-Flash (ExecSourcesCensus, ExecRerunAllGates), opencode-go/deepseek-v4.1-flash (ScribeMistake), zai/glm-5.3-flash, devin/swe-2, openai-codex/gpt-6.1-sol (ConnSiblingCounters); others not exposed.
- Lane contamination: see Landed changes, "Lane HEAD repair"; working-tree bytes were verified equal to `master` (`cmp` of every round-28 file) before the repair.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no file written by this lane's seats (ScoutLaneState checked the untracked fleet files for tsukuroi content).
- Routed defects owed: 4 (companion debt), 6 (self-assessment tool); 5 ("+200 band") was dispositioned as mori's per the orchestrator note, but RevSpotcheckRouting shows both files are this lane's (`oom-event-plane.md`, `kill-event-deep-r8.md`) — owed by tsukuroi next round.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Installs: none (L1 and every reporting seat). pacman pause respected.
- L0 questions: none new.
