# souji — round 70 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`. Lane base `e063a2fcb3f5f3fb8fb19d2ae1592b1f22e6a333` (r69 admitted). Final lane hash `3b7cce814afae197c7d7dc079f2bdfac3aa389a0` (`git ls-remote origin refs/heads/master` → `3b7cce814afae197c7d7dc079f2bdfac3aa389a0`). L1 `SoujiR70`. Not a fresh-start round: r67, r68 and r69 were admitted.

## Work performed

Declared claims (2), frozen at `0243af04bbcd422302b4efc3473612073c9aa962` (`census/round-70/preregistration.txt`):
- **C1 — operability** (the writer surface `tools/souji-receipt-write.py`): the writer scrubs `GIT_LITERAL_PATHSPECS`, `GIT_GLOB_PATHSPECS`, `GIT_NOGLOB_PATHSPECS` and `GIT_ICASE_PATHSPECS` from its `git()` helper. Sourced claim: S304, opened this round.
- **C2 — calibration** (the counter's self-assessment surface `census/round-70/c1-counter.py`): the counter's own selftest kills four frozen instrument mutants, and its battery arm detects a swapped battery member. This is the lowest owned axis (7).

Work items:
- Freeze with controls executed and committed before any candidate byte existed: the C1 do-nothing control (base writer, EXIT=1), forgery controls F1 refuse-on-presence and F2 literal-only scrub (both EXIT=1), the C2 before-arm on the frozen r69 counter (score=5, EXIT=1), and the invalidity controls CF1/CF2 (EXIT=2). Evidence: `census/round-70/controls/*.txt`, commit `0243af04`.
- Probe of the mechanism: `census/round-70/probes/lp-ls-files-probe.txt` shows that `ls-files -v -z ':(top)'` prints nothing under `GIT_LITERAL_PATHSPECS=1`, and that `ls-tree -- <path>` fails under GLOB and ICASE.
- Writer candidate `93a051b2`: the `PATHSPEC_ENV` scrub in `git()` and selftest case 38 (`tools/souji-receipt-write.py:104-112`, case 38 at `:1499`).
- Successor counter, 59 rows (12 pathspec rows added), with selftest section (7) and `verify_members` (`census/round-70/c1-counter.py`). The C2 harness is `census/round-70/c2-harness.py`.
- After-arms `e84f691b`: `records/c1-after.txt`, `records/c2-after.txt`, and the writer and counter selftest receipts. The selftest receipts close r69 routed D2.
- r69 routed D1: the r69 wave evidence is mirrored byte-identically into `census/round-69/records/wave-w1/` (`0d8ce29a`). D3: SKILL.md registry rows for r69 and r70 (`feb283ee`). D4: unit erratum in `corpus/lessons/round-70.md`.
- Mistake fix that can fail: `tools/souji-pointer-check.py`. It reports 8 MISSING lines and EXIT=1 over the r69 lesson and prereg (`census/round-70/records/pointer-check-r69.txt`), and 0 missing with EXIT=0 over the r70 prereg, knowledge entry and lesson at `faac34e6` (`pointer-check-r70.txt`).
- Probe beyond the claims: the r70 counter run over all 26 r69 battery members gives `all_match=false`, EXIT=1 (`census/round-70/probes/battery-r69-members-r70-counter.txt`). This sits inside the frozen named limit "battery not regenerated".
- Round shape: **one v1 wave `w1`, 12 seats** (`.ufo/waves/round-70/w1-spec.json`, validated `ufo-swarm-wave-dispatch-v1` spawn 12, band 8–16). Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats are 5 of 12 (42%). No residual call, so the **round total is 12**. **Dead seats: 0** (all 12 wrote reports; `w1-results.json`). The L1 held the canonical planner seat. WAVE-DONE was received before this report was filed. Seat evidence is mirrored to `census/round-70/records/wave-w1/` (`170ecb65`).
- Wave verdicts: S70ExecC1, S70ExecC2, S70Reviewer, S70CriticClaims, S70Sentinel, S70MutWriter, S70MutCounter and S70ExecAmbient reproduced C1 and C2 byte for byte. S70Reviewer rated the writer scrub, the counter, the harness, prereg-vs-receipts and SKILL.md SOUND. S70CriticClaims rated C1 STANDS (qualified) and C2 STANDS (qualified). Qualifications are listed under Before → after.
- **Incident (HIGH):** seat S70MutWriter's fixture had a malformed `mktemp` template. `git -C ""` fell back to the fleet root, and the seat committed `cff0b4cbe684ce702bca2a126b579d602f0cd6ae` there ("seed", author `p <p@x>`; it adds versions.html and w4lines.txt and snapshots `.scratch/run15-state.json`; +235/−79; no deletions). That commit is already under origin/main and origin/master. The lane ran no recovery. I messaged the orchestrator and filed an L0 question (fleet commit `78c78a82`). Lesson M6 records it.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only ` M .scratch/run15-state.json`, which belongs to the orchestrator and is not a misroot. No seat-written untracked files remain at the fleet root. The two fleet-root files swept into `cff0b4cb` are now tracked. Their removal is part of the L0 ruling.

## Landed changes

All commits were made through `jj-lane.sh` and pushed. LOG entry: `LOG.md` "## Round 70".
- `0243af04` freeze: preregistration, counter, matrix, harness, control generator, controls, probe, census-before.
- `93a051b2` C1 candidate writer and selftest case 38.
- `e84f691b` after-arms and selftest receipts.
- `0d8ce29a` r69 D1 mirror.
- `feb283ee` S304/S305 registry rows, `corpus/knowledge/pathspec-env-scrub.md`, README frontier, SKILL rows.
- `9167e02d`, `20c117ce`, `4c392c76`, `faac34e6` pointer-check tool, lesson, and wave corrections: S304/S305 anchor offsets, S296 `used-by`, knowledge sentences.
- `63ceb475` SCORECARD capability rows, r70 done bullet and measurements, battery probe.
- `152b46c3` census-after and pointer-check-r69.
- `170ecb65` wave integration: lesson M4–M7, attacks, routed r71, D4 erratum, LOG, SCORECARD and README corrections, wave mirror, wave spec, dispatch and ready.
- `3b7cce81` final pointer-check receipts.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 | `grep -E '^(SUMMARY\|EXIT=)' census/round-70/records/c1-after.txt` (frozen r70 counter, `--base-rev e063a2fc --rev 93a051b2 --tool tools/souji-receipt-write.py`) | `controls/c1-do-nothing.txt`: `new_forgeries=4 new_honest=13 class_mismatches=5`, EXIT=1 | `SUMMARY matrix=59 base_forgeries=4 base_honest=13 new_forgeries=0 new_honest=15 class_mismatches=0 new_echo=0 errors=0 regress=PASS`, EXIT=0 | candidate `93a051b2c936ff6eafca8e8b31d918e3d20fd3da` |
| C2 | `grep -E '^(SUMMARY\|EXIT=)' census/round-70/records/c2-after.txt` (frozen harness) | `controls/c2-before-r69.txt`: `killed=0 survived=4 tamper=undetected score=5`, EXIT=1 | `SUMMARY label=c2-after-r70 positive_selftest=PASS positive_battery=PASS mutants=4 killed=4 survived=0 tamper=detected score=0`, EXIT=0 | counter frozen at `0243af04`, run at `e84f691b` |

Both after-lines match the frozen predicates byte for byte. The forgery controls stay red: F1 `new_honest=11` and F2 `new_honest=13`, both EXIT=1. The invalidity controls CF1 and CF2 give EXIT=2. Qualifications from the wave are not counted as passes:
- **C1, NOGLOB:** the NOGLOB scrub is unmeasured. Mutants W3 (NOGLOB dropped) and W7 (no scrub on `status`) survive both the matrix and the writer selftest.
- **C1, mechanism:** the predicate does not fix the mechanism. A pathspec-free rewrite with no scrub also passes it.
- **C1, case 38:** writer case 38 iterates the same `PATHSPEC_ENV` constant it tests. It fails on the base writer (37/38).
- **C2, authorship:** the four mutants and the tests that kill them were written in the same round, and the CF1/CF2 controls foreshadowed the after-arm (prereg disclosure ii). S70CriticClaims questions the calibration label under `AXES.md` ("SHONEN.md/SCORECARD entries match observed repo state").
- **C2, further mutants:** S70MutCounter ran 10 more counter mutants. 5 survive the selftest (X6–X10). X8, which drops a row's `pathspec_env`, keeps EXIT=0 and is caught only by the frozen byte comparison of SUMMARY.

No owned axis score changed (calibration 7, coverage 8, operability 8). No reproducible 0–10 mapping exists for these moves. Claim verdicts as filed: **C1 improved (operability), C2 improved (calibration), qualified as above**. The operator and the closure rule.

## Sources & frontier

- `corpus/SOURCES.md` rows went from 226 to 228. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` gave EXIT=0 at round start (`census/round-70/records/census-before.txt`) and EXIT=0 at round end (`census-after.txt`). W04 duplicate-URL warnings only.
- Rows added by tier: **A: S304 admit** (git(1) OPTIONS `--literal-pathspecs`, located 20-word quote, byte 11413 of `census/round-66/sources/git-environment.txt`; page sha256 534c674f…f9d1, accessed 2026-11-06) and **A: S305 reject** (git(1) ENVIRONMENT `GIT_LITERAL_PATHSPECS` entry, which never names magic; flip condition: a release adds it). The gitglossary `literal` magic word was considered and rejected without being appended. The rejection is in the lesson Gate.
- Rows touched (old→new): S296 `used-by` changed from `corpus/lessons/round-64.md` to `corpus/lessons/round-64.md, corpus/knowledge/pathspec-env-scrub.md`. The S304/S305 anchor cells were corrected in-round from the non-reproducible "12133/47046" to S298-basis byte offsets (lesson M4).
- Frontier advanced: `corpus/README.md` "### Frontier (r70 pathspec-variable hermeticity)". New knowledge entry: `corpus/knowledge/pathspec-env-scrub.md`. Sourced claim: C1 rests on S304.
- Mistake mined: `corpus/lessons/round-70.md` `## Mistakes` M1–M7. M1 is mined from r69 (D1/M14). Its fix is shown able to fail (pointer check EXIT=1 on r69).
- **Assimilation: none.** `considerthese/` is absent. `grep -ril pathspec /home/vgpnk/Projects/shokuknow/merge/souji/` finds 0 files, so no theme fits.
- Cross-lane, documented only because domain trees are read-only: S70Connector found `kaidoku-shokunin/tools/round-42/prefile-gate.py:311-327` and `kumitate-shokunin/scripts/round-gate.mjs:491,562`. Both read the index through pathspecs with the caller's pathspec variables unscrubbed.

## Trend verdicts

- **expansion: improved.** There is a new knowledge entry on ground `corpus/knowledge/` did not hold: the sourced four-variable pathspec table with the GLOB/ICASE over-refusal polarity. S304 was admitted. The new README frontier section notes that r69's lesson already named the LITERAL route.
- **quality: improved.** Prior material was found false and marked. The r69 prereg cites 5 dead probe pointers (including `probe/fsm`, which r69 M14 missed), now caught by a committed check (`pointer-check-r69.txt`). The r69 "6 flips" unit was corrected (D4 erratum). The r69 seat evidence is now resolvable from committed bytes (D1).
- **discernment: unchanged.** Every source attack came from this lane's own dispatched seats (S70ScoutSources, S70CriticDiscern agree with all three gate decisions). No non-author discernment check has landed. The closure spot-check decides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md "## Round 70" error pattern (empty pathspec-limited read under caller variables, S304) and registry rows for r69/r70 (`feb283ee`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 70". The writer hardening was exercised end to end through the frozen 59-row matrix (`census/round-70/records/c1-after.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: `tools/souji-pointer-check.py`; r69 wave evidence now committed (`census/round-69/records/wave-w1/`); SKILL.md r70 rows run as written (S70Reviewer item 5).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling findings were reported, not edited (`census/round-70/records/wave-w1/seats/S70Connector.md`). The fleet misroot commit `cff0b4cb` by a seat is an open L0 incident, not lane content.

## Other

- Open L0: `souji | round-70` — ruling on fleet commit `cff0b4cb` (filed in fleet commit `78c78a82`). The earlier `souji | round-67` (relative-value trade) and `souji | round-68` (writer verifier) questions remain the operator's.
- Stale-lane: respawn-per-round driver; this lane has no other open mission.
- Tool installs: none. No pacman transaction, and no sysctl, sudo or kernel change.
- Scratch `/fast/scratch/hyaku/souji-r70/` was removed at landing.
