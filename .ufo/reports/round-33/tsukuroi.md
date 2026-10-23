# tsukuroi — round 33 report (attempt 3, L1 TsukuroiR33A3)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`, claim base `1f521b93`, lane HEAD `ca768636f3525c9567842674789cb6e798b5e6c1` (pushed; `jj-lane.sh state`: local = remote, ahead 0, untracked 0).

## Work performed

The round declared two claims:

- **C1 (operability, measured):** `tools/_revision.py` `clean_env()` and `tools/mutants-owed-statements-r29-v4shapes.py` `ENV` build git children's environment from an allow-list instead of copying the ambient environment. The surface is the environment those two builders hand to git. The counter is the frozen probe `tools/probe-child-env-allowlist-r33.py`.
- **C2 (adjacency, exploratory):** a per-class kill/OOM boundary note between this lane and mori.

The round-32 spot-check's routed defects were handled as repairs, not claims.

- **Inherited state.** Attempts 1 and 2 died. Their landed commits `c2e69f3e`, `965bc5d9` and `9c89ff4f` (declaration, amendment 1, amendment 2) were re-read; the probe at `9c89ff4f` is the frozen counter. Attempt 2 left 247 uncommitted entries (spec, dispatch, seat outputs). They were moved out of the lane, unread and uncited, to `/fast/scratch/hyaku/tsukuroi-r33-attempt2-scratch/untracked.tar` (sha256 `ab282e1c…`). Its uncommitted round-32 erratum was discarded and re-derived. Recorded in `SCORECARD.md` "Round 33 — attempt 3: start" (`5a967ce2`).
- **Pre-data control wave a3w1 (45 seats).** Nineteen fresh control designs were scored under the frozen probe and committed at `4e521ce0` before the change existed. Every control that skips the work reads at least 3 of 15 or is a harness error. The positive control C16 reads 0. Table: `corpus/lessons/round-33.md` "Pre-data control wave". Receipts: `.ufo/waves/round-33/a3w1/C*/`.
- **C1 change, written by the L1 after the controls** (`c8fcfbf6`): `clean_env()` returns a fixed dict, v4shapes' `ENV` is a fixed dict display, and the `_revision.py` sha256 pins in `check-pause-gate.py:245` and `report-red-causes.py:203` move to `fc861ec8…`. The same commit also carries the C2 draft note and its `PROVINCE.md` append. The probe does not read either file (RevC1Diff: separable).
- **After receipt:** `.ufo/waves/round-33/a3/after/c1-after-c8fcfbf6.jsonl`, 0 of 15, exit 0 (`783d79e0`).
- **Registry:** a round33 superseding table with the probe's row (`f761fade`). check-registry-coverage moves from exit 1 at base to exit 0.
- **Falsify wave a3w2 (37 seats).** It re-ran the counter (before and after, twice), the regression set, five mutants of the landed builders (all killed), the gates and the selftests. It re-opened all C2 pointers (QB1 to QB7) and all six sources. Critics attacked C1's axis fit, control coverage and sequence, and C2's absorption and gaps. Results are in `corpus/lessons/round-33.md` "Wave-2 results".
- **Wave-2 repairs** (`3846bd1a`, `eb388c9c`):
  - IN-101 reclassified `UNRESOLVABLE`, because C1 removed its quoted expression. This fixes the `check-adjacency-anchors` harm found at `f761fade`.
  - The C2 note gained a `recheck:` line, which fixes the `check-recheck-commands` harm.
  - Two unescaped table pipes were fixed.
  - Four census-read classes found by CritC2Gaps were added, with a routing reading.
  - Round-33 axes table: check-self-assessment moves from exit 1 at base (K10 stale) to exit 0.
- **Residual review call a3res (3 seats).** JudgeC2Exploratory (reviewer) is the named non-author reviewer and ruled C2 `unprovable-but-better`. CritC2AddedRows found three wording defects after the ruling; they are owed, and the judged note is not edited. RevTipRepairs verified the repairs, counts, sources and gate receipts.
- **Round-32 routed defects** (`corpus/lessons/round-33.md` "Routed defects"):
  1. Census counter v4 was built and scored: tip 24/24, K11 1/24, content-free 0/24. Wave-2 MutR1CounterV4 then passed it with a fixture-label-keyed census, so **defect 1 stays open** (R33-FIXTURE-LABEL-SHORTCUT).
  2. The value channel kills the round-32 survivors m3 to m6 (RevR2Kills confirms the exact NAME=VALUE clause fired). `check-owed-statements-r29.py` is not a target: it has no `--selftest` mode, so it is a harness error (ScoutOwedStatementsTarget).
  3. Closed by C1.
  4. Erratum appended (`5a967ce2`), verified by RevErratumR32.
  5. No data executor ran outside a validated wave. The L1 wrote the declared change.
  6. Carried items are listed.
- **Host observation, not a claim:** the boot-0 coredump count rose from 265 to 1603 between about 07:14Z and 07:44Z (MutR1CounterV4 finding 7). This is a live coredump storm and next round's census input.

Round shape: default, two v1 waves plus one residual call. a3w1: 45 seats, 23 mutation-tester, 13 scribe, 3 executor, 2 scout, 1 reviewer, 1 critic, 1 sentinel, 1 connector. a3w2: 37 seats, 17 reviewer, 7 scout, 6 mutation-tester, 5 critic, 1 sentinel, 1 connector. Residual a3res: 3 seats, 2 reviewer and 1 critic, counted in the total. Round total for attempt 3: 85 seats.

Planner mapping: the L1 holds the §3 planner seat. The validator rejects `planner` as a swarm role.

Holds (refused by a provider safety filter, `code=cyber_policy`; not evidence; not retried): a3w1 X01OpenSearchObserved and X02OpenSearchSpawnSide. No seat died otherwise.

Seat gate: a3w1 granted 45 at 07:03:57Z; a3w2 granted 37 at 07:31:19Z; a3res granted 3. All three were released when settled.

## Landed changes

Every commit is pushed (`jj-lane.sh` printed `landed <hash>` for each).

| Commit | What | LOG.md entry |
|---|---|---|
| `5a967ce2` | attempt-3 start note, round-32 controls erratum, census start, a3w1 spec | Round 33 (LOG.md, last entry) |
| `4e521ce0` | a3w1 control receipts (pre-data), spec role fix | same |
| `c8fcfbf6` | C1 change (two builders, two pins); C2 note draft and `PROVINCE.md` append | same |
| `783d79e0` | C1 after receipt; a3w2 spec | same |
| `f761fade` | `SKILL.md` round33 registry table | same |
| `3846bd1a` | wave-2 repairs (IN-101, C2 note), SOURCES S180 to S185, lesson draft | same |
| `eb388c9c` | round-33 axes self-assessment table | same |
| `dd426fe1` | gate receipts at `eb388c9c` | same |
| `38191181` | measured outcome, LOG, lesson results, `SHONEN.md` box 4 pointer, a3w2 and a3res evidence, census end | same |
| `ca768636` | final gate receipts at `38191181` | same |

Inherited from attempts 1 and 2 (re-read, not re-authored): `c2e69f3e`, `965bc5d9`, `9c89ff4f`.

Five oversize "mutant vs frozen" diffs (3 MB each; the whole round's history plus one mutation) are outside the lane at `/fast/scratch/hyaku/tsukuroi-r33a3/oversize/`. The seats' mutation-only patches are committed.

## Before → after measurements

- **C1.** Counting command: `python3 tools/run-receipt.py --revision <REV> --tool-revision 9c89ff4f093d07a6f92925518310ca6a7c8a2fa0 --out <file> -- tools/probe-child-env-allowlist-r33.py --revision '{rev}' --lane '{lane}'`. Probe sha256 `c24f344b…`, label `leaking`.
  - Before at `9c89ff4f` (targets byte-identical to base `1f521b93`): **15 of 15**, harness_errors empty, exit 1 (`.ufo/waves/round-33/a3w1/C01Before/before-claim.jsonl`; re-run by a3w2 RerunBeforeIndependent).
  - After at `c8fcfbf6`: **0 of 15**, harness_errors empty, exit 0 (`.ufo/waves/round-33/a3/after/c1-after-c8fcfbf6.jsonl`; re-run by RerunAfterA and RerunAfterB).
  - Git children per target (279/335/203/226/1176) and stdout digests are unchanged.
  - Regression set (`--set regression`): 5 of 33 → 0 of 33 (RegressionAfter).
- **C2.** No counting command (exploratory).
- **No-harm gates.** Base receipts are at `9c89ff4f` (`.ufo/waves/round-33/a3w1/ExecGateBaselines/`); tip receipts at `38191181` (`.ufo/waves/round-33/a3/gates-final-38191181…/`) and at `eb388c9c`.

| Gate | Base | Tip |
|---|---|---|
| check-self-assessment | 1 | 0 |
| check-registry-coverage | 1 | 0 |
| check-recheck-commands | 0 | 0 |
| check-adjacency-anchors | 0 | 0 |
| check-pause-gate | 1 | 1 (same `GATE-PREMISE P3`) |
| report-red-causes | 0 | 0 |
| 25 `_revision`-importing selftests | — | byte-identical to base |

**Author verdicts (the operator rules):**

- **C1: target met; one declared control class unscored.** The declared open adversarial search is a hold (provider refusal), and CritControlCoverage reads the probe's documented read-side limit as still open. Separately, the counter was amended at `9c89ff4f` after attempt-1 seats had scored under `965bc5d9` (54 quarantined receipts, listing only; lesson R33-AMEND-AFTER-UNCOMMITTED-SCORES). Attempt 2's amendment text did not say so. Both questions are the operator's to rule.
- **C2: `unprovable-but-better`**, ruled by the named non-author reviewer JudgeC2Exploratory (`.ufo/waves/round-33/a3res/JudgeC2Exploratory.md`).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.

- Round start: exit 0, last line `tsukuroi ok …/corpus/SOURCES.md` (`.ufo/waves/round-33/a3/census-start.txt`).
- Round end: exit 0, the same last line, 0 errors (`.ufo/waves/round-33/a3/census-end.txt`). W04 advisories are carried.
- Rows: 179 → 185. All six are tier A: S180 CPython `subprocess.rst`, S181 man-pages procfs, S182 Linux `oom_kill.c`, S183 git-config.adoc, S184 systemd-oomd, S185 psi.rst.

Registry changes (old → new):

- S180, S181, S182: absent → `mined`. S180 and S181 are used by `corpus/lessons/round-33.md`; S182 by `corpus/knowledge/kill-oom-boundary-r33.md`.
- S183, S184, S185: absent → `rejected` as redundant with S163, S122/S137 and S115 respectively (same bytes).
- No existing row changed.

**Gate** (URL, access date 2026-10-23 and a ≤25-word located quote for each row in `corpus/lessons/round-33.md` `## Gate`). Real rejects: S183, S184 and S185, all redundant; each was re-opened by a wave-2 scout, who agreed.

**Sourced claim:** C1 rests on S180, "these are used instead of the default behavior of inheriting the current process' environment." (`subprocess.rst:649-650`).

**Mistakes mined** (`corpus/lessons/round-33.md` `## Mistakes`):

- R33-AMEND-AFTER-UNCOMMITTED-SCORES
- R33-REFUSED-OPEN-SEARCH
- R33-CRITIC-BUILD-CAUGHT
- R33-FIXTURE-LABEL-SHORTCUT

Frontier advanced: C2 maps eleven kill and memory-pressure classes against mori at `24603186`.

## Trend verdicts

- **expansion: `unchanged`.** No new surface is held. The C2 note documents boundaries and adds no route, intake or plane.
- **quality: `improved`.** C1 moved 15 → 0 of 15, with every after-mutant killed. The regression set moved 5 → 0 of 33. check-self-assessment and check-registry-coverage moved 1 → 0. Two wave-2 harms were repaired before the tip, and no gate is worse than base.
- **discernment: `improved`.** In favour:
  - The pre-data control set (19 designs) and wave 2 caught real defects before filing: the IN-101 and recheck harms, four missing C2 classes, a label-keyed shortcut against the repair counter, and two over-wide statements.
  - Three redundant sources were rejected.
  - The judged C2 note was not edited after the ruling.

  Against:
  - The open adversarial search did not run (refusals).
  - Defect 1's repair counter fell to a fixture-label shortcut.
  - An earlier attempt's amendment under-disclosed prior scoring.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md:4-5`. This round adds the round33 registry table (`SKILL.md`, `f761fade`). No non-author replay.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:6-7`. Round-33 LOG entry. No non-author replay.
- [~] Instructions executable by an agent without oral context — `SHONEN.md:8-9`. Unchanged.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:10-12`. The boundary is now examined per class (`corpus/knowledge/kill-oom-boundary-r33.md`, C2 ruled `unprovable-but-better` by lane seat JudgeC2Exploratory). Mori has not acknowledged it, so not `[x]`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (every seat reported `Installs: none`).

Open L0 questions: none appended. The two C1 rulings above are for the closure.
