# tsukuroi — round 29 report (attempt 1, 2026-10-22, L1 TsukuroiR29)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`. Claim base `16e9ab2abfac430b4e960e8ce64b90420f602342`. Lane branch `master` equals remote at **`d411c3d8729cf1bad38a9f819bd156fbc14b39b6`**, the helper's last `landed` line; the commit adds one evidence file. Dispatched 19:46Z; declaration landed 19:53Z; last lane commit about 20:46Z.

## Work performed

Declared claims, in `SCORECARD.md` section "Round 29 — declaration, attempt 1", landed in `81a061a67466c5e1be812814a895a4b5ed89b4ff` together with both counting tools:

- **C1 (depth, 8, the lowest axis).** The twelve owed statements O01–O12 each carry one source-backed correction marker. They come from the round-27 spot-check, routed defects 4 and 5, carried by round 28:
  - O01–O04: the "+200 band scanned first" kernel OOM reading.
  - O05–O07: the MP4 "nothing monitored" qualifier debt.
  - O08: a `driver-firmware-plane.md` `[unk]`.
  - O09–O12: four statements in `storage-health-r26.json`.
  
  Counter: `python3 tools/check-owed-statements-r29.py --revision <REV>` → `marked`. This is the sourced claim: O01–O04 cite S148 and S149, both opened this round.
- **C2 (operability, 9).** The eight frozen lane tools that run git writes no longer follow an inherited `GIT_DIR`, `GIT_WORK_TREE` or `GIT_INDEX_FILE`. This is round-28 routed defect 2, widened from two batteries to all eight tools. Counter: `python3 tools/probe-git-env-leak.py --revision <REV>` → `leaking`, `targets`, `harness_errors`. The probe fails before the fix: it read 3 of 8 at the declaration commit.

Work items:
- C1 markers landed in the six target files, all append-only (`fc07fecc`). Supporting changes:
  - A new `SKILL.md` section, "Kernel OOM victim selection — round 29": the v7.2 `oom_badness` rule, a decision table, and a magnitude check of row F7 (`fc07fecc`; precision fixes in `06e00daf` and `67df330b`).
  - Sources S148 (proc.rst), S149 (mm/oom_kill.c) and S150 (sysctl/vm.rst), all mined, and S151 (LWN 2009), rejected.
- C2 fix: every git child of `tools/mutants-adjacency-overlap.py`, of `tools/mutants-kernel-taint.py` and of the selftest helper of `tools/check-adjacency-overlap.py` runs with every `GIT_*` variable removed (`fc07fecc`). Global and system git config are also ignored (`409ceed4`, after wave-1 SentinelGitEnv).
- Outside the frozen set, the selftest `git init` of `tools/check-self-assessment.py` was scrubbed too (`fc07fecc`; RevProbeDesign found it). It is not counted.
- The C1 counter was hardened three times after attacks. The declared target was unchanged each time and each version re-measured the claim:
  - v2 (`fc07fecc`): wave-1 CritOwedCounterShapes showed the declared counter counted 18 of 20 should-fail shapes.
  - v3 (`75257ea6`): wave-2 CritOwedV2Shapes found 25 of 26 new shapes counted by v2.
  - v4 (`67df330b`): residual ResCritV3OverStrict found v3 refused 19 of 27 legitimate variants. v4 relaxes only those shapes.
- Two committed batteries (QUALITY 73) back the counter. `tools/mutants-owed-statements-r29.py` builds markers on the marker-free declaration commit (`fc07fecc`; survivor shapes added in `75257ea6`). `tools/mutants-owed-statements-r29-landed.py` mutates the landed markers (`75257ea6`).
- Routed repairs from the round-28 spot-check (`corpus/lessons/round-28-verifier-spotcheck.md:87-95`):
  - Item 1: a C2 battery receipt at the tip counter `99f35675…` (`.ufo/waves/round-29/measure/r28-c2-battery-at-16e9ab2a.jsonl`): 0 of 5, control 6.
  - Item 2: claim C2.
  - Item 3: an R4a selftest case; m1 and m7 now fail (`fc07fecc`, RevR4aFix).
  - Item 4: the padding-shapes repair landed in `10d5288f` and was **reverted** in `75257ea6` as over-strict. Wave-2 CritPaddingOverStrict found it refused 15 of 19 correct register variants and still accepted 24 new padding shapes. Owed.
  - Item 5, carried round-27 defects: 4 and 5 are claim C1. Defect 6 is fixed (self-assessment hyphenated headings, docstring, four cases; `fc07fecc`, RevSelfAssessFix).
  - Item 6: the lost RevFamilyB2 review was redone (RevFamilyB2Redo). B2 alone refuses its family, and 0 of 38 evasions were accepted.
  - Item 7: the axis framing (below).
- Frontier and quality:
  - Lesson `corpus/lessons/round-29.md`: Gate, routed dispositions, four Mistakes rows, wave-2 and residual corrections.
  - QUALITY 74–76.
  - Registry rows round29 in `SKILL.md`: 37 of 37 tools covered.
  - SCORECARD measured outcome and axes table round 29; LOG entry (`06e00daf`, `434a7903`).
- Axis framing (round-28 routed 7, operator ruling pending): each claim sits on the axis its counting command measures. This is the author's reading. Wave-1 CritAxisFraming and wave-2 CritClaimFraming2 argue that only O01–O04 add new depth. O05–O12 carry corrections already argued in the Markdown files into their companions (QUALITY 67) or close an `[unk]` from an existing capture.

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `81a061a67466c5e1be812814a895a4b5ed89b4ff` | declaration; `tools/check-owed-statements-r29.py`; `tools/probe-git-env-leak.py`; round-28 tip-counter battery receipts | LOG "Round 29" |
| `3c94d7308e561832a0df0981cbc39dda270e32d8` | before receipts (C1 0 of 12, C2 3 of 8) | LOG "Round 29" |
| `fc07fecc9ff9526d23f80aa2c21d59a79b519af5` | wave-1 integration: markers, S148–S151, SKILL OOM section, GIT_* scrub, counter v2 + battery, R4a and self-assessment fixes, QUALITY 74–76, lesson, registry, wave-1 evidence | LOG "Round 29" |
| `409ceed4f067f4296f27fcb9cb843c7ca54d2e5d` | global/system git config ignored in the three fixed tools | LOG "Round 29" |
| `adcc7a677a8c003a9934d9d8aef1319821ae0df3` | after receipts; registry row for the battery | LOG "Round 29" |
| `10d5288fc1051364e711203855e7c53710dfcc21` | padding repair (later reverted) and receipts | LOG "Round 29" |
| `75257ea68b1b5c87b429a221bee4d1f8e5d7f54a` | wave-2 repairs: counter v3, landed-marker battery, O07 `now` corrected, S150 used-by trimmed, padding revert, lesson corrections, wave-2 evidence | LOG "Round 29" |
| `06e00dafbbaa4695bc74decf68c816da8151b00a` | SCORECARD measured outcome, axes table round 29, LOG entry, SKILL precision fix, final receipts | LOG "Round 29" |
| `67df330bef72bff00dd8cd9c4deeca5298ba8f8c` | counter v4 (over-strictness fixes), SKILL event-B wording | LOG "Round 29" |
| `434a7903b06e931ddc3413dbe4687a36bf118245` | residual evidence; record corrections; final-tip receipts | LOG "Round 29" |
| `9ac9d785…`, `d411c3d8729cf1bad38a9f819bd156fbc14b39b6` | late-arriving wave evidence files | LOG "Round 29" |

Gates at `434a7903` (the last content revision), run by the L1:

| Gate | Result |
|---|---|
| `check-self-assessment` | PASS, 27 checks, 0 mismatches |
| `check-registry-coverage` | PASS, 37 of 37 |
| `check-memory-pressure` | PASS |
| `check-storage-health` | PASS |
| `check-owed-statements-r29` | 12 of 12 |
| `probe-git-env-leak` | 0 of 8 |
| sources census | exit 0 |

At `06e00daf` the same gates also passed, along with kernel-taint, adjacency-overlap and freshness-r17. Round-28 batteries at `67df330b`: 0 of 24 and 0 of 5, both controls 6 (`measure/final-tip/`). Census selftest: PASS, 97 of 97.

## Before → after measurements

| Claim | Command | Before (declaration `81a061a6`) | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 tools/check-owed-statements-r29.py --revision <REV>` → `marked` | 0 of 12: declared counter `5b6cf227…` (`measure/c1-before-81a061a6….jsonl`), v2 (`measure/final-tip/c1-v2-before-81a061a6.jsonl`), v3 (`measure/final/c1-v3-before-….jsonl`) | **12 of 12**, exit 0, under the declared counter, v2 `c3f9cfe7…`, v3 `1c37d492…` and v4 `3516d579…` | `409ceed4` (`measure/c1-after-*`), `75257ea6` (`measure/final/`), `434a7903` (v4, L1 run) |
| C2 | `python3 tools/probe-git-env-leak.py --revision <REV>` → `leaking` | 3 of 8, probe `46a55ce7…` (`measure/c2-before-81a061a6….jsonl`) | **0 of 8**, `harness_errors` [], exit 0 | `409ceed4`, `75257ea6` (`measure/final/c2-…`), `434a7903` |

C1 battery results:

| Counter | Marker-free battery, should-fail accepted | Landed battery, mechanical shapes accepted |
|---|---|---|
| declared | 20 of 25 | — |
| v2 | 0 of 25 | 18 of 19, and refuses should-pass P1 |
| v3 | 0 of 29 | 0 of 19 |
| v4 | 0 of 29 | 0 of 19 |

Every control reads 12. Receipts: `measure/c1-battery-*`, `measure/final/c1-*battery-v3.jsonl`, `measure/c1-landed-battery-counter-v2.jsonl`. The seven semantic shapes are reported but not gated.

Independent re-derivations:
- C1: RerunC1Counters, CritClaimFraming2, ResRevV3Counter.
- C2: RerunProbe, CritClaimFraming2, SentinelResidualEnv. Each C2 fix is load-bearing: MutScrubAdjBattery, MutScrubKtBattery and MutScrubAdjSelftest each reverted one fix and the probe flagged that tool.
- Per-marker review in wave 2: eleven hold. O07 partly held: its `now` overclaimed ancestor monitoring and was rewritten before closure; residual ResRevO07 confirmed the repair holds.

Open findings, disclosed:
- An italic or unbalanced-asterisk id still counts under v3 and v4 (ResRevV3Counter).
- v4 had no independent attack.
- Git-environment channels not closed: a PATH `git` wrapper, a per-user attributes file, enclosing-repo discovery, and the probe's own inherited `HOME` (SentinelResidualEnv).
- Three of the eight targets leaked, seen only as exit-code divergences. The other five never leaked. Outside the set, 0 of 12 further git-writing selftests leak (RevProbeOutsideSet).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
- Start: exit 0, 147 rows, 25 W04 advisories (`.ufo/waves/round-29/w1/ExecGatesStart/sources-census.txt`).
- End: exit 0, 151 rows, 26 W04 advisories, last line `tsukuroi ok …/corpus/SOURCES.md` (`.ufo/waves/round-29/measure/final-06e00daf…/census.txt`; re-run at `434a7903` with the same result).

Rows added:
- Tier A, `mined`: S148 (Linux v7.2 `Documentation/filesystems/proc.rst`, oom_score_adj), S149 (`mm/oom_kill.c`), S150 (`Documentation/admin-guide/sysctl/vm.rst`, oom_kill_allocating_task).
- Tier C, `rejected` with reason and flip: S151 (LWN "Taming the OOM killer", 2009; its heuristic has no surviving term in v7.2).

Rows touched, old → new, logged in the lesson:
- S133 and S134 used-by: `…storage-health-r26.md` → `…storage-health-r26.md, …storage-health-r26.json`.
- S150 used-by, on this round's own new row: the two OOM notes are removed, leaving `SKILL.md, corpus/lessons/round-29.md`.

Every new row was re-opened by a wave-2 non-author seat (RevSourceS148, S149, S150, S151Reject). Sha256 and located quotes match; S151's live page differs only by an advertising block. RevSourceS150 disagreed with S150's admit reason ("needed for O01–O04"); the row was corrected.

Other frontier items:
- Sourced claim: C1. The O01–O04 markers cite S148 and S149.
- Mistakes mined (`corpus/lessons/round-29.md` `## Mistakes`): R29-ATTRIBUTION-BY-TIMING, R29-GIT-ENV-LEAK, R29-OWED-FROZEN, R29-UNBATTERIED-COUNTER. Each fix is shown able to fail: the attribution check prints FAIL on the round-28 bytes, the probe reads 3 before, the counter reads 0 before, and the battery fails the declared counter.
- `PROVINCE.md` frontier rows: none advanced.

## Trend verdicts

- **expansion: unchanged.** The new sources and the `SKILL.md` OOM section deepen the existing memory and OOM plane; they add no new surface. (Residual ResCritVerdicts read this as improved; the author does not self-grant it.)
- **quality: improved.** A false kernel-mechanism reading present since probation round 6 (revenger RevenPlus200Origin) is corrected against v7.2 sources, with the arithmetic recomputed by five seats. Eleven companion statements are marked. Three tools stop following an inherited git environment. The self-assessment gate moves from FAIL at the base (K10) to PASS. Limits: only O01–O04 are new depth, and the padding repair was reverted.
- **discernment: unchanged.** In favour: the S151 reject, the padding revert after an over-strictness attack, and the lesson correcting its own false sentences ("only refuses more", the S150 citation). Against: the C1 counter was again declared without the QUALITY 73 battery, the third permissive counter in three rounds (Mistake R29-UNBATTERIED-COUNTER).

## SHONEN

- [~] SKILL.md real decision tables, error patterns, checklists, cited sources. `SKILL.md` section "Kernel OOM victim selection — round 29" adds a sourced decision table (S148–S150); author evidence plus wave-2 RevSkillOomSection and RevSourceS149 line checks; no promotion verifier.
- [~] One end-to-end domain task executed and logged. Unchanged this round (`SHONEN.md` box 2 pointers).
- [~] Instructions executable without oral context. The new counter and both batteries document usage in their docstrings (`tools/check-owed-statements-r29.py:1-60`, `tools/mutants-owed-statements-r29*.py:1-25`).
- [~] No cross-domain bleed. Mori's round-27 finding is answered in this lane's own files and not absorbed into mori. ConnSiblingOverlap lists sibling tools with unscrubbed git writes for the integrator (`.ufo/waves/round-29/w1/ConnSiblingOverlap.md`); this lane did not act on them.

## Round shape, seats and process

- **Shape: two v1 waves plus one residual call. Round total: 78 seats.**

  | Call | Seats | Role mix | Dispatched |
  |---|---|---|---|
  | Wave 1, build | 35 | 12 scribe, 10 reviewer, 5 executor, 2 critic, 2 mutation-tester, 1 sentinel, 1 revenger, 1 connector, 1 scout | 19:57Z, spec `.ufo/waves/round-29/w1-spec.json` |
  | Wave 2, falsify | 37 | 27 reviewer, 4 critic, 4 mutation-tester, 1 sentinel, 1 scout; one item per attacked marker, source, fix or counter | about 20:16Z |
  | Residual | 6 | 4 reviewer, 2 critic | `residual-dispatch.json` |

- Both waves were validated under policy v1 and each was dispatched as one `task` call with the validator's `taskCall`. The seat gate was acquired and released for every call.
- Planner seat: held by the L1, which wrote both counting tools before any counted run.
- Dead seats: none; all 78 returned. Refusals: none observed.
- Observed answering models:

  | Model | Seats |
  |---|---|
  | opencode-go/deepseek-v4.1-flash | scribes |
  | openai-codex/gpt-6-luna | executors, mutation-testers |
  | zai/glm-5.3-flash and devin/swe-2 | reviewers |
  | openai-codex/gpt-6.1-sol | connector |

  Several seats did not expose a model.
- Containment:
  - Every seat ran sandbox git under `/fast/scratch/hyaku/tsukuroi-r29/` with `GIT_*` unset.
  - ScoutContamination checked the lane reflog from 16:46 -03 (dispatch) on: it holds only jj `export` entries, and no branch was created.
  - The round-28 residue under `refs/jj/keep/*` (`a080e4ef…`, `ee430cdf…`, `f93be5ab…`, created 16:13 -03 before this round) was left untouched for the operator.
- L1 integration notes:
  - Two executor patches were corrupt (ExecR4aAnchor, ExecPaddingShapes) and were integrated from the seats' sandbox files.
  - The L1 repaired one wrong selftest fixture (`b10-lane-mid-word`); RevPaddingFix confirmed the fix. The fixture left with the revert.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no file written by this lane's seats. The untracked files are other lanes' or the operator's: `AGENTS.md`, `*.html`, `.ufo/waves/round-33/`, a pyc.
- Inherited state: none. The lane was clean at dispatch, and there is no `lane-dead-no-report tsukuroi round=29` line.
- Owed to the next round:
  - Routed 4 (padding shapes), with both seats' fixtures in `.ufo/waves/round-29/`.
  - The residual git-environment channels.
  - The italic-id census leak in the C1 counter.
  - The round-28 routed 1 sub-item: a revision field in selftest receipts.
  - MutC1Counter's absence, disclosed.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Installs: none by the L1. Every reporting seat stated `Installs: none`. The pacman pause was respected.
- L0 questions: none new. The axis-framing dispute (round-28 routed 7) stays with the operator.
