# tameshi round 42 report

L1 tameshi, hyaku run 6, attempt 1 (2026-10-25). Lane HEAD at report time: `fee1977f73b864c6abaaea20da6465a6ee29ec30` (the deciding measurements were taken at `242c1b4a1bb793d6ca4ac4e3b0da153767e78739`; the records landed at `32d5d22f`; wave evidence at `fee1977f`).

## Work performed

Claims (1–3, each falsifiable; contract `.ufo/evidence/round-42/contract.json` frozen at `322b5cd32b4319a05340d249ae752d12a9e6b19f` before any seat scored and before the deciding run; post-freeze amendments P1–P6 change citations and disclosures only — the frozen `claims.*`, predicate, counters, targets and kill rules are byte-unchanged, verified by wave-2 ReviewReadmeContract and CriticAmendments):

- **C1 (calibration, lowest non-retired axis at 6):** the lane's self-assessment records agree with observed repo state — no committed wave receipt asserts a report presence the tree contradicts without a covering superseding receipt (m10), and round-41/42 records cite no unmined round-42 S-id (m7), no unresolvable repo path under a line-scoped extractor (m8) and no unreachable revision (m11); standing sources-registry count matches the registry (m6). Live mismatch at base: the round-41 residual receipt says `present:false` for `ResidualReceipts.md`, which is in the tree (round-41 closure defect 2). Repair: appended superseding receipt `.ufo/waves/round-42/supersede/round-41-residual-receipt.json` (drafted byte-exact by seat ExecSupersedeDraft, sha256 `987f82b4…`; verified by ReviewSupersede).
- **C2 (depth, capability acquisition):** write-path census v4 (`tools/write-path-census-v4.py`) binds instance-attribute destinations through same-class method returns and argparse output-flag destinations through every in-module call, resolving the three live v3 false positives (`tools/context-capture.py:1682`, `:1685`, `tools/registry-replay.py:123`) with `mkdtemp`/`--out` in the resolved text, keeping ten counter fixtures at their declared classes, and killing every declared mutant of the new resolution code under an exit-plus-FAIL oracle. Knowledge entry `corpus/knowledge/r42-attribute-and-outflag-destinations.md` (S157/S158 new rows; S001/S153 held).
- Frontier step (§2b: SOURCES curation, census before→after, mined mistake, sourced claim) rode inside the round per the contract. Assimilation theme: mutant outcome vocabulary — two entries admitted, one refused, one left unadopted.

Round shape: **default — two v1 waves** (policy v1, band 32–64). Wave 1 (build + first falsifiers): **47 seats** — 13 scout, 8 reviewer, 7 executor, 6 mutation-tester, 6 critic, 6 scribe, 1 connector; 47 completed, 0 dead. Wave 2 (falsify): **38 seats** — 14 reviewer, 7 scout, 7 critic, 6 mutation-tester, 3 executor, 1 connector; 37 completed, 1 dead (`ReviewLessonLimits`, provider error "Unable to reach the model provider"; stays dead in evidence). Round total **85 seats**, ≤128. No residual call. The canonical §3 planner seat is held by the L1 (the validator rejects `planner` as a swarm role — recorded, not bypassed). Both waves dispatched as exactly one `task` call carrying the validator's `taskCall` unchanged (`.ufo/waves/round-42/{spec,dispatch}-w{1,2}.json`), after validating under policy v1.

Key work items and evidence: wave-1 specs/registries under `.ufo/waves/round-42/w1/`; wave-2 under `w2/`; counters and receipts under `.ufo/evidence/round-42/{before,control,prerun,after,census-sources}/`; source snapshots under `.ufo/evidence/round-42/sources/` (sha256.txt). Planned/planned: the round's counter, contract and controls were authored and frozen by the L1 before any seat; the base receipts and the do-nothing/junk controls were committed before data (contract `do_nothing_control` scenarios reproduced by ReviewControls and ReviewC1Counter).

## Landed changes (all via the lane helper, all pushed; lanes landed: `322b5cd3` freeze, `5f739acf` wave-1 integration, `a21845f5` lesson guard-rewording + pre-run receipts, `f6762b80` wave-2 integration (mutants, w2 evidence), `242c1b4a` falsifier fixes (S158 row, contract P4–P6, lesson/entry/README corrections, census-after), `32d5d22f` deciding-run verdict records, `fee1977f` wave-2 spec/dispatch evidence)

- Freeze commit `322b5cd3`: contract + C1/C2 counters (self-pin against the freeze copy, records=6 gate, line-scoped backtick extraction, m10 supersede rule, m11 revision reachability; C2 out-of-process tool runs, counter-side v3/v2 digest constants, `resolved`-text inspection, exit-plus-FAIL kill oracle).
- C1 repair: `.ufo/waves/round-42/supersede/round-41-residual-receipt.json` (all 8 residual seats re-asserted with tree truth); out-of-claim correction `.ufo/waves/round-42/supersede/round-20-outcomes.json` (round-20 snapshot's `report_exists:false` for an existing report).
- C2 tool: `tools/write-path-census-v4.py` (v3 + attr binding, method-return fold, output-flag trace; depth 8). First build by seat ExecV4Tool reached 3/10 fixtures and was replaced by the L1 (amendment P4). Declared mutants: `.ufo/evidence/round-42/census/mutants.json` (6 mutants, attr/method/outflag, authored by non-author seat MutantAuthor, committed unchanged).
- Knowledge: `corpus/knowledge/pit-outcome-vocabulary.md` (new) and `corpus/knowledge/r42-attribute-and-outflag-destinations.md` (new, corrected after wave-2 falsifiers); `corpus/README.md` round-42 coverage rows (F1/F1b status corrected against round-25/26 records).
- Registry: four rows S155–S158 (S155/S156 assimilated `staged:S159`/`staged:S160`, re-grounded; S157/S158 new), used-by cells extended for S001/S153; 109 → 113 rows; census exit 0 at start and end with the same warning set (`.ufo/evidence/round-42/census-sources/{start,after}.stdout`).
- QUALITY criteria 81 (presence receipt written after the writes it describes, or superseded) and 82 (a kill is a completed run with a failed check; a crash is a run error, not a kill), each with a falsifier shown to fail.
- Lesson `corpus/lessons/round-42.md`: Gate (admit/reject/deferral with located quotes and access dates, collision guard proof, renumber map, quarantine slice, recheck normalization, used-by log), Mistakes (six rows incl. stale-receipt and newline-spanning-extractor), C1/C2 instrument limits, Holds, considerthese proposal 5 (SHONEN readiness table).
- LOG.md and SCORECARD.md round-42 sections incl. the deciding-run verdict block.

## Before → after measurements

### C1 — calibration (counting command: `python3 .ufo/evidence/round-42/calibration/measure.py --lane LANE --rev REV --freeze 322b5cd…`)

- Before (base `c77c2b7e…`): `C1_R42: self_pin=1 m6=0 m7=0 m8=0 m10=1 m11=0 total=1 records=3 sources_rows=109 … C1_R42_PASS=false`, exit 1 (`.ufo/evidence/round-42/before/c1-at-base.stdout`). Do-nothing control (records added, no supersede): m10=1, `C1_R42_PASS=false` (`.ufo/evidence/round-42/control/c1-do-nothing.stdout`).
- After (measurement revision `242c1b4a`): `C1_R42: self_pin=1 m6=0 m7=0 m8=0 m10=0 m11=0 total=0 records=6 sources_rows=113 … C1_R42_PASS=true`, exit 0 (`.ufo/evidence/round-42/after/c1-at-242c1b4a.stdout`). **Verdict: improved.**

### C2 — depth (counting command: `python3 .ufo/evidence/round-42/census/measure.py --lane LANE --rev REV --freeze 322b5cd…`)

- Before (base): `C2_R42: tool_absent=1 v3_sha_ok=1 v2_sha_ok=1 live_unflagged_v3=3 … C2_R42_PASS=false`, exit 1 (`.ufo/evidence/round-42/before/c2-at-base.stdout`). Controls: v3 in the v4 slot fails F01/F04 and the three live sites; the junk tool passes 1/10 fixtures (`.ufo/evidence/round-42/control/`).
- After (measurement revision `242c1b4a`): `fixtures_pass=10/10 … live_1682_ok=1 live_1685_ok=1 live_123_ok=1 live_unflagged_v4=0 … mutants_declared=6 mutants_killed=4` → `C2_R42_PASS=false`, exit 1 (`.ufo/evidence/round-42/after/c2-at-242c1b4a.stdout`). **Verdict: missed** — the declared mutant gate is not met (survivors `outflag_no_parse_args_check` and `method_fold_several_returns`; the miss is reported, not narrowed; mutants committed unchanged). The tool itself resolves the live sites and passes its ten fixtures; the claim's target is not reached.
- No axis harmed: depth 9 → 9 (command D), calibration 6 → 6 (round-21 coldread monitor), receipts `.ufo/evidence/round-41/census/command-d.stdout`, wave-1/2 re-runs (ExecCommandD, ReplayNoHarm). No SHONEN box moved. `git diff --numstat` on LOG/SCORECARD/QUALITY/README shows insertions only.

## Sources & frontier

- Rows before → after: **109 → 113** (`grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md` → 113). Added by tier: S155/S156/S157 tier A docs, S158 tier A code (all mined, opened 2026-10-25, recheck 180d, pinned to committed snapshots under `.ufo/evidence/round-42/sources/`). Rows touched old→new: S001 used-by + `pit-outcome-vocabulary.md`, `r42-attribute-and-outflag-destinations.md`; S153 used-by + `r42-attribute-and-outflag-destinations.md`; S158 teaches corrected after wave-2 review (score-sum anchor extended to `ScorePrecursor.java:44-45`/`MutationStatistics.java:84-85`). S155/S156 renumbered from `staged:S159`/`staged:S160` by document; collision guard proven (0–3-space extractor catches the indented row; column-zero misses it), post-append hazard S153–S158 recorded.
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi` → exit 0 at round start (109 rows; `.ufo/evidence/round-42/census-sources/start.stdout`) and exit 0 at round end (113 rows; `after.stdout`), identical warning set (9 × W04 + 1 × W01), zero E codes.
- Frontier: F1 report-interop already held (round-25/26 MTE reports); F1b open; PIT outcome vocabulary adds cross-tool scoring ground. F4 write-path half gains v4 + entry; the tool's false-negative classes are recorded, not hidden. Assimilation: **two entries admitted** (`pit-outcome-vocabulary.md`, `r42-attribute-and-outflag-destinations.md`), one refused (`survivor-classification.md`: drifted quote, false recheck, duplicates held F8), one left unadopted (`mutation-score-semantics-cjk.md`: gates admit; sibling ground; flip recorded). considerthese: proposal 5 mined as a SHONEN-readiness table (lesson).
- Mined mistake: stale-receipt (round-41 residual receipt written before the report it describes) — captured-by none; fix C1 m10 + supersede rule, shown able to fail by selftest T2_* and the base receipt; QUALITY criterion 81. Also newline-spanning-extractor, half-true-citation, delegated-build-without-interface-test, entry-overclaim, gate-quote-incompleteness (six rows in the lesson).
- Sourced claim: C2 rests on S157 (argparse, opened this round); the kill oracle cites S001 (re-opened) and S158 (divergence). P1/P5 record that PIT support was withdrawn and that S157 is exercised in the counter only via the tool's selftest (critic finding).

## Trend verdicts

- **expansion: improved** — two admitted entries on ground the lane did not hold (PIT outcome vocabulary beyond held Stryker semantics; the two new census edge classes with S157/S158 rows), re-grounded and snapshot-pinned in-round.
- **quality: improved** — C1's live mismatch repaired with an append-only supersede receipt; QUALITY criteria 81/82 added; appendix-only repair rule held (insertions-only diff); the C2 miss is reported honestly with the surviving mutants kept as committed evidence rather than tuned.
- **discernment: improved** — outside closure input (round-41 spot-check defects 1–3) routed into the counter classes; wave-2 falsifiers independently re-opened every new row, re-ran every counting command, and attacked each claim; the lesson records instrument limits, including the deletion/rewrite counterexamples (V1–V6) and the battery's blind spots, none of which was used to reach or hide the verdicts.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — no standing command (considerthese table, lesson); `[~]` At least one end-to-end domain task executed and logged in LOG.md — round-42 LOG section lands this round; `[~]` Instructions executable by an agent without oral context — coldread monitor `python3 .ufo/evidence/round-21/coldread/measure.py --rev REV` exits 0 at the base, selftest 12/12; `[~]` No cross-domain bleed (PROVINCE.md still accurate) — no tool reads PROVINCE.md (considerthese table). No box changed; all remain `[~]` lane-asserted.

Stale-lane: no other mission of this lane is open (respawn-per-round driver).

Misroot sweep (before report): `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` — the untracked files are driver-owned (`.scratch/goal-20261025-hyaku-12h.md`, `.ufo/state/*`, `.omp/mcp.json`, `.ufo/waves/round-24/w2/RevUnlandedResolution.md` [tabi]); none is a tameshi round-42 misroot (wave-1 ScoutMisroot and wave-2 ScoutMisrootW2 both report the same set). No seat misroots to repatriate.

Tool installs: none (curl/git/python3 pre-existing; pacman guard respected — no transactions).

Open L0 questions: none new (`d0531d78` from round 38 is not re-filed).
