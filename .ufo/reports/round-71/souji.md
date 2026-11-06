# souji — round 71 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`. Lane base `8b9345b1f2c4bb908ae418588d4cbde6a34a5bd0` (r70 admitted). Final lane hash `9332fde2df586d33fd2717fda4821d99e7fb3bd1` (`git ls-remote origin refs/heads/master` → `9332fde2df586d33fd2717fda4821d99e7fb3bd1`). L1 `SoujiR71`. Not a fresh-start round: r68, r69 and r70 were admitted. No earlier attempt (`.ufo/watchdog.log` has no `lane-dead-no-report souji round=71` line).

## Work performed

Declared claims (2), frozen at `aa91d1cad89200ec733edd3475461010a372923d` (`census/round-71/preregistration.txt`):
- **C1 — operability** (writer surface `tools/souji-receipt-write.py`): the clean-tree witness is no longer forgeable through a clean filter driver or a repository-local `core.fileMode=false`. The candidate scrubs `GIT_ATTR_SOURCE`, pins `-c core.fileMode=true`, and refuses `RECEIPT-FILTER-DRIVER-SET`. Sourced claim: S306, S307 and S308, all opened this round.
- **C2 — calibration** (counter self-assessment surface `census/round-71/c1-counter.py`, the lowest owned axis at 7): the counter's own selftest kills the five counter mutants that survived the r70 counter's selftest (S70MutCounter X6–X10). The mutants were written by a seat in the previous round and frozen unchanged.

Work items:
- Freeze, with controls executed and committed before any candidate bytes existed (`aa91d1ca`):
  - C1 do-nothing control (round-start writer): `new_forgeries=7 class_mismatches=7`, EXIT=1.
  - F1 blanket presence refusal: `new_honest=16` of 19, EXIT=1.
  - F2 attr-source scrub only and F3 fileMode pin only: `new_forgeries=5` each, EXIT=1.
  - C2 before-arm, r70 counter: `x_survived=5 score=5`, EXIT=1.
  - CF1 always-failing counter: EXIT=2 (invalid).
  - Evidence: `census/round-71/controls/*.txt`; probe `census/round-71/probes/attr-filemode-probe-base.txt`.
- Candidate writer `a1db6c85`: selftest cases 39–40.
- After-arms `52e8c3fa`: `census/round-71/records/c1-after.txt`, `c2-after.txt`, `writer-selftest.txt` (40/40) and `counter-selftest.txt` (39/39).
- Counter hardening for S70Sentinel F3/F4/F5: member-name, sums-name and symlink checks in `verify_members` (selftest section 8e), and harness label validation plus run-dir cleanup (`census/round-71/c2-harness.py`).
- Wave repairs, landed after the frozen measurement. The claims are unchanged (lesson M4).
  - `45a94c83`:
    - A filter attribute value of `set`, `unset` or `unspecified` is no longer exempt (S71Reviewer F1).
    - The post-run driver check now runs before the post-run status read, so a self-unlinking in-run filter is caught (S71Sentinel HIGH-1).
    - Every writer git call pins `core.checkStat=default` and `core.trustctime=true` (S71Sentinel HIGH-2).
  - `f13d575e`: `ident` and `working-tree-encoding` are refused with `RECEIPT-CHECKIN-CONVERSION-SET` (S71CriticClaims HIGH).
  - Receipts:
    - Writer selftest 42/42 (`records/writer-selftest-repair.txt`).
    - Each repair was reverted alone and fails its case (`records/repair-canfail.txt`: R1, R2, R3a, R3b and R4 each `fail=1`).
    - The frozen counter at the repaired tip still prints the frozen SUMMARY with EXIT=0 (`records/c1-at-repair.txt`).
  - Measured residual (named limit): a same-second in-place edit is invisible to `git status` under any config (`probes/stat-granularity-probe.txt`).
- r70 routed defects:
  - D1: correction appended to SCORECARD.
  - D2: erratum appended to `corpus/lessons/round-70.md` (`1c2239cd`).
  - D3: `tools/souji-pointer-check.py --selftest` adopted from seat S71ExecPointer. It passes 4/4, and two mutants fail it (`records/pointer-check-selftest.txt`). A SKILL.md gate row was added.
  - D4(a–d): see C1, C2 and the counter hardening above. Base-slot rc binding is routed to r72.
  - D5: the wave context carried the empty-variable and toplevel fixture guard. No fleet misroot occurred this round.
- Round shape: **one v1 wave `w1` of 12 seats.**
  - Spec `census/round-71/records/wave-w1/w1-spec.json`, validated as `ufo-swarm-wave-dispatch-v1` spawn 12 under band 8–16.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats are 5 of 12 (42%).
  - There was no residual call, so the **round total is 12**.
  - **Dead seats: 0** (`w1-results.json`).
  - The L1 held the canonical planner seat. WAVE-DONE was received before this report was filed.
  - Seat evidence is mirrored to `census/round-71/records/wave-w1/seats/` (`c0dd4476`).
- Wave reproductions:
  - C1 was reproduced byte for byte by S71ExecC1 (5/5 runs), S71Connector, S71Reviewer, S71CriticClaims and S71ScoutSources.
  - C2 was reproduced by S71ExecC2, S71Connector, S71Reviewer and S71ScoutSources.
  - The X6–X10 edits reproduce the r70 seat mutants 5/5.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): only ` M .scratch/run15-state.json` and `?? .scratch/run15-wrapup/misroot-cff0b4cb/`. Both are orchestrator-owned and were not touched. No seat-written fleet-root files.

## Landed changes

All commits went through `jj-lane.sh` and were pushed. LOG entry: `LOG.md` "## Round 71".
- `aa91d1ca` freeze: preregistration, counter, matrix, harness, mutant set, controls, probe, `srcs/`, census-before.
- `a1db6c85` C1 candidate writer.
- `52e8c3fa` after-arms; S306–S310; knowledge entry `corpus/knowledge/filter-filemode-witness.md`; README frontier; SKILL rows; correction of the r67 knowledge entry.
- `1c2239cd` size-changing probe re-run (labelled post-freeze); r70 D2 erratum.
- `45a94c83`, `f13d575e` wave repairs to the writer (selftest cases 41–42); stat-granularity probe.
- `c0dd4476` wave integration: lesson `corpus/lessons/round-71.md`, SCORECARD and LOG, source-row corrections and S311, pointer-check selftest, repair receipts, census-after, wave mirror.
- `9332fde2` pointer-check receipt `census/round-71/records/pointer-check-r71.txt` (`missing=0`, EXIT=0).

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 | `grep -E '^(SUMMARY\|EXIT=)' census/round-71/records/c1-after.txt` (frozen r71 counter, `--base-rev 8b9345b1 --rev a1db6c85 --tool tools/souji-receipt-write.py`) | `controls/c1-do-nothing.txt`: `new_forgeries=7 new_honest=19 class_mismatches=7`, EXIT=1 | `SUMMARY matrix=70 base_forgeries=7 base_honest=19 new_forgeries=0 new_honest=19 class_mismatches=0 new_echo=0 errors=0 regress=PASS`, EXIT=0 | candidate `a1db6c8514771c0a0321c29741831606d09cc2a5`; same at repaired `f13d575e` (`records/c1-at-repair.txt`) |
| C2 | `grep -E '^(SUMMARY\|EXIT=)' census/round-71/records/c2-after.txt` (frozen harness) | `controls/c2-before-r70.txt`: `x_killed=0 x_survived=5 score=5`, EXIT=1 | `SUMMARY label=c2-after-r71 positive_selftest=PASS x_mutants=5 x_killed=5 x_survived=0 cm_mutants=4 cm_killed=4 cm_survived=0 score=0`, EXIT=0 | counter frozen at `aa91d1ca`, run at `52e8c3fa` |

Both after-lines match the frozen predicates byte for byte. The wave's qualifications are not counted as passes:
- **C1, prose wider than the counter:** the wave forged the frozen candidate on three unmeasured filter-class routes (driver named `set`, self-unlinking in-run filter, `ident`) and one stat route. All four were repaired in-round, and each repair is shown able to fail (M4). The repaired routes are measured by selftest cases and probes, not by the frozen matrix.
- **C1, what the predicate admits:** it accepts any design that emits the frozen class strings (S71CriticClaims).
- **C1, over-refusal:** an honest repository with a configured driver on a tracked path is refused. No row measures this.
- **C1, AS1/AS2 rows:** they cannot tell a GIT_ATTR_SOURCE scrub from an unfiltered dirty tree (S71MutCounter F2).
- **Counter, base slot:** `claim_upheld` ignores the base slot. Mutants Y6/Y10 drop `base_forgeries` from 7 to 2 with EXIT=0 (S71MutCounter F1, routed).
- **C2, mutant-set specific:** a neighbouring `clean_env` defect passes the selftest (S71CriticClaims).
- **C2, calibration label:** it holds by r70 precedent, qualified.

No owned axis score changed (calibration 7, coverage 8, operability 8). Claim verdicts as filed: **C1 improved (operability), C2 improved (calibration), both qualified as above**. The operator and the closure rule.

## Sources & frontier

- `corpus/SOURCES.md` rows went from 228 to 234. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Census command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Round start: EXIT=0 (`census/round-71/records/census-before.txt`).
  - Round end: EXIT=0 (`census-after.txt`), with W04 duplicate-URL warnings only.
- Rows added, all tier A, all opened 2026-11-06. Captures are in `census/round-71/srcs/`, with sha256 recorded and quotes located at character offsets:
  - **S306** admit, mined: gitattributes(5) `filter` clean, offset 17513.
  - **S307** admit, mined: git(1) `--attr-source`, offset 13322.
  - **S308** admit, mined: git-config(1) `core.fileMode`, offset 82016.
  - **S309** reject: git(1) ENVIRONMENT `GIT_ATTR_SOURCE`, a duplicate anchor of S307.
  - **S310** mined: git-config(1) `attr.tree` precedence, offset 54097.
  - **S311** mined: gitattributes(5) `ident`, offset 17004.
- Rows touched (old→new, all within the round):
  - S306 `teaches` narrowed to the check-in sentence.
  - S307 `teaches` qualified.
  - S309 reject reason corrected.
  - S310 queued→mined, recheck 90d→180d, used-by `corpus/lessons/round-71.md`→`corpus/knowledge/filter-filemode-witness.md`, re-anchored.
  - No pre-r71 row changed. Details are in the lesson Gate.
- Frontier advanced: `corpus/README.md` "### Frontier (r71 filter-driver and core.fileMode witness)" and the new knowledge entry `corpus/knowledge/filter-filemode-witness.md`. Sourced claim: C1 rests on S306–S308.
- Mistakes mined: `corpus/lessons/round-71.md` `## Mistakes` M1–M4.
  - M1 is mined from r67: a false closure sentence in `common-dir-route-receipt-writer.md:41`. The fix is shown able to fail: rows FM1/FM2 forge in the do-nothing control and in control F2.
  - M4's fix is shown able to fail: `records/repair-canfail.txt`.
- Discernment (own seats): S71ScoutSources and S71CriticDiscern agree with S306, S307 and S308. They disagreed with the S309 reason and with S310's status, and both rows were corrected. No non-author check has run yet.
- **Assimilation: none.** `considerthese/` is absent. `grep -ril 'gitattributes\|fileMode\|clean filter' /home/vgpnk/Projects/shokuknow/merge/souji/` finds 0 files.
- Cross-lane, documented only: S71Connector lists 13 sibling clean-tree gates that neither scrub `GIT_ATTR_SOURCE`, pin `core.fileMode` nor check filter drivers (kaidoku, kama, mori, tameshi, audio; `census/round-71/records/wave-w1/seats/S71Connector.md`).

## Trend verdicts

- **expansion: improved.** New knowledge on ground no earlier entry held: attributes and stat settings as clean-tree witness routes, with S306–S308, S310 and S311 mined. Three new capability rows were added.
- **quality: improved.** Prior material was found false and marked: the r67 knowledge sentence (M1), the r70 D1 count and the r70 D2 erratum. In-round source cells were corrected after attack (S306, S307, S309, S310). Four HIGH writer routes were repaired, each with a fix shown able to fail.
- **discernment: unchanged.** All source attacks came from this lane's own seats. No non-author spot-check has run yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md registry rows for the r71 C1 matrix, the C2 harness and the pointer-check gate (`52e8c3fa`, `c0dd4476`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 71"; the writer was hardened and exercised through the frozen 70-row matrix (`census/round-71/records/c1-after.txt`, `c1-at-repair.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: `tools/souji-pointer-check.py --selftest` (`records/pointer-check-selftest.txt`); the wave seats ran the SKILL rows as written (`records/wave-w1/seats/S71Reviewer.md` item 5).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling findings were reported, not edited (`records/wave-w1/seats/S71Connector.md`); no fleet misroot occurred this round.

## Other

- Open L0 questions: none new. Earlier `souji | round-67`, `souji | round-68` and `souji | round-70` remain with the operator.
- Stale-lane: respawn-per-round driver; this lane has no other open mission.
- Tool installs: none. No pacman transaction, and no sysctl, sudo or kernel change.
- Scratch `/fast/scratch/hyaku/souji-r71/` was removed at landing.
