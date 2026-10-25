# kotoba — round 54 (hyaku campaign, attempt 1)

Lane `kotoba-shokunin`, branch `master`, base `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` → landed tip
`c501cd537c75155e0196e217bda013ec164ad770` (pushed). Plan `plans/round-54.md` @ `e33715486a45a4a857b64c30e6b695f7995858b8`.

## Work performed

Declared claims (two):
- **C1 — depth** (lowest owned axis, 9; the learning claim and the sourced claim): `SKILL.md` § Description
  thresholds by client, a decision table with real thresholds grounded in a new admitted entry. Frontier row:
  *Per-render consumption* (offer-render half), untouched since round 46.
- **C2 — consistency** (owned; the calibration sub-axis): `SKILL.md` § Gate registry, one row per lane verifier
  (routed defect 4 of the round-53 spot-check).

Drift sentinel honoured: no freshness claim, no change to `verifiers/verify_surfaces.py`, nothing on the
executed-checklist / always-on-box row. Owned-axes reading of the lowest-axis duty is met by C1 (depth 9), so
the open L0 question (round 47) does not decide this round.

- Frozen counters `verifiers/check_description_thresholds.py`, `verifiers/check_gate_registry.py` committed with
  the plan, before content (`e3371548`); both byte-identical plan → tip (`W2RerunC1`, `W2RerunC2`).
- Plan errata before the content each bounds: `d051ec40` (misstated before-value times, M46), `3b2535d2`
  (C2 bounded to the counter; guard: four gates must carry their own exiting-0 self-test — `CriticC2Sizing`),
  `90cae9af` (C1 unchecked items named, prior holds measured, guards a–c — `CriticC1Sizing`).
- Enabling move `7ad05d34`: 43 verifier-bullet lines moved verbatim from `SKILL.md` § Sources to
  `verifiers/README.md` (593 → 552 lines; `diff` empty).
- C2 prerequisite `b55550b9`: own `--self-test` modes for `box_proof_case_deletion.py`, `check_alwayson_boxes.py`,
  `check_callee_rename.py`, `check_opencode_repin.py` (each exited 2 on `--self-test` before; counting lines
  unchanged; seats `Reg*`).
- C2 content `bf65974c`: 24-row registry + M45's fix `verifiers/check_sources_append_only.py` (seat `ScribeMistake`).
- C1 content `5a097e12`: entry `corpus/knowledge/skill-listing-thresholds-round54.md`, SOURCES S053–S064, lesson
  `corpus/lessons/round-54.md` (Gate, M45–M47), README index + Frontier note (seats `Src*`, `Scribe*`).
- Routed round-53 defects: (1) addendum appended to `corpus/lessons/round-53.md`; (2) S046 → S060 correction row;
  (3) S050 → S061 + M45 gate (red on `e792607e`); (4) C2; (5) tip runs `.ufo/waves/round-54/build/ExecTipRuns.md`
  and `LOG.md` now names `e5355a62`; (6) `verifiers/baseline.json` note cites the regeneration command (`fed56863`,
  no pin changed); (7) carried.
- Falsify-wave corrections `cae8f2ea` (seat per item in `LOG.md` § Round 54) and corpus baseline re-recorded last
  (78→81, 49→51; `verify_corpus_integrity.py` 9/9).

## Landed changes

All under `LOG.md` § "2026-10-22 — Round 54". Commits (helper `landed` lines): `e3371548` plan+counters ·
`7ad05d34` enabling move · `d051ec40` erratum 1 · `fed56863` baseline note · `3b2535d2` erratum 2 · `90cae9af`
erratum 3 · `b55550b9` four self-tests · `bf65974c` C2 · `5a097e12` C1 · `58db81c4` build evidence (40 reports) ·
`cae8f2ea` falsify corrections, LOG, SCORECARD, baseline · `c501cd53` falsify evidence (41 reports).

## Before → after measurements

| claim | command | before | after |
|---|---|---|---|
| C1 depth | `python3 -B verifiers/check_description_thresholds.py --rev <rev>` | `backed 0 of 7 clients`, exit 1 @ `422ffd10`, `e3371548`, `bf65974c` | `7 of 7`, exit 0 @ `5a097e12` and `cae8f2ea`; `--fetch` 7 of 7 |
| C2 consistency | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | `0 of 21 …; phantom 0`, exit 1 @ `422ffd10` (0 of 23 @ `b55550b9`) | `24 of 24 lane verifiers; phantom 0`, exit 0 @ `bf65974c` and `cae8f2ea` |

Guards outside the counters (declared in errata before content): C1 (a) S053–S059 absent at the plan commit,
(b) Claude Code `1,536`/`1%` and Codex `2%`/`8,000` absent from `SKILL.md` at the plan commit, (c) fetch 7/7 —
all hold (`W2RerunC1`); C2 four self-tests are the scripts' own and exit 0 at `bf65974c` (`W2RerunC2`; negative
control exit 2 at `7ad05d34`). No-harm: finding delta `--base 422ffd10 --head cae8f2ea` → `new 0, resolved 3`;
checklist 11/11 PASS (`SKILL.md` 599 ≤ 600); correction sweep 0 stale; `W2CriticNoHarm` found no gate moving
pass→fail except the `451a02ff` pointer, fixed in `cae8f2ea`.

## Sources & frontier

Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`: start exit 0 (`kotoba ok`,
W04 ×3); end exit 0 (`kotoba ok`, W04 ×6 — S054/S055/S056 re-open pages already held under other scopes).
Rows 52 → 64 (`grep -c '^| S[0-9]' corpus/SOURCES.md`): 12 added, all tier A (11 docs, 1 code-host changelog):
S053–S059 (one per client), S060 (supersedes S046's teaches), S061 (records S050's in-place edit), S062–S064.
Touched: S046 `used-by` old→new (logged in the lesson). Rejected (with reasons and flips, Gate): docs.github.com
about-agent-skills `.md` (404), cursor.com/changelog.md (HTML shell, 0 "skill"), Copilot CLI plugin-manifest
`Max 1024 chars` (not a skill description); all three re-confirmed by `W2ScoutRejects`. Frontier row advanced:
*Per-render consumption* (offer-render half; join still unheld). Mistakes mined: M45 (SOURCES append-only breach;
fix shown able to fail), M46 (plan times), M47 (gates without self-tests).

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | improved | knowledge entries 40 → 41 (`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c .md$` @ `422ffd10` → `c501cd53`), SOURCES 52 → 64; Cursor/Gemini/Copilot CLI description numbers new to the lane |
| quality | improved | registry 0 → 24 rows; four gates gained self-tests; S046/S050 corrected append-only; corpus integrity 7/9 → 9/9; three over-wide C1 cells corrected before closure |
| discernment | improved | three rejects with reasons, re-confirmed; wave-2 found and the round corrected over-wide cells (Codex "raises", Cursor "warned, not cut", Gemini banner scope) and an M45 miscount |

## Gate

Real rejects this round: the three source rejects above, and the `RegCheckOpencodeRepin` draft row that borrowed a
nested `--self-test` literal (rejected; the counter got its own self-test instead).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` § Description thresholds by client, § Gate registry (lane-run)
- [~] At least one end-to-end domain task executed and logged — `LOG.md` § Round 54; `.ufo/waves/round-54/falsify/W2RerunC1.md`
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no fresh non-author run)
- [~] No cross-domain bleed — `.ufo/waves/round-54/build/ConnSiblingOverlap.md` (no sibling holds this ground)

## Round shape and seats

Default two v1 waves. Build 40 seats (executor 23, scribe 10, critic 2, mutation-tester 2, scout 1, connector 1,
reviewer 1); falsify 41 seats (reviewer 33, critic 4, mutation-tester 2, scout 2). Round total 81; no residual
call; no dead seat; no refusal. Planner seat held by the L1 (data-walk on scout `ScoutPriorHolds`). Validator-taskCall
dispatched unchanged except the host-required `solutionSpace` field added per task. Falsify gate waited 684 s for
capacity (cap 90).

## Carried / holds

Environment failures exiting 1 instead of 2 in several gates; `fault_injection_corpus.sh` red since round 49 and
its self-test red; weak self-tests (callee rename, opencode repin 1/4 mutants); the registry counter's substring
flag test; 12 earlier SOURCES protected-cell changes found by M45's gate (operator decision needed);
`SKILL.md` at 599/600 lines.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none (L1 and seats).
Misroot sweep: `git status --porcelain` at the fleet root shows six untracked files, none naming kotoba or round 54
(not ours, untouched). Open L0: round-47 lowest-axis question (not decisive this round).
