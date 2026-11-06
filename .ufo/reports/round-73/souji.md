# souji — round 73 report (attempt 2, L1 `SoujiR73a2`)

Lane `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Final lane hash: `d8380f6d04dbda5f3c8ac804eb3149466f9b256b`. `git ls-remote origin refs/heads/master` prints that hash.

## Work performed

Declared claims (frozen by attempt 1 in `census/round-73/preregistration.txt` at freeze `23ecd0700be05a78b71ad88ae6fca2d2d8f5468b`; this attempt ran them unchanged):

- **C1 — operability** (surface: the receipt writer `tools/souji-receipt-write.py`; sourced on S315, S316). The writer re-hashes every status-clean stage-0 tracked file (`git hash-object --stdin-paths`) and symlink target against the index object id, before and after the wrapped command, and re-compares the instrument after the run. A stat-concealed forgery refuses as `RECEIPT-WORKTREE-STAT-CONCEALED`. Routed r72 defect D3(a), S72Sentinel HIGH.
- **C2 — calibration** (lowest owned axis, 7; surface: the counter's forgery crediting, `census/round-73/c1-counter.py`). The counter credits a refuse row that the base writer accepts as a base forgery only when it observed the fixture worktree diverge from the row's revision. `base_unwitnessed` enters the verdict. Routed r72 defect D4(c), S72MutCounter MF HIGH.

Work items:

- **Inherited from attempt 1.** `.ufo/watchdog.log:3072` records `lane-dead-no-report souji round=73`. Attempt 1 landed and pushed five commits:
  - freeze F `23ecd070`
  - counter I `1eac307f`
  - C1 controls K `aaacba33`
  - writer W `b84ff90b`
  - after-arms A `312e8f29`

  Re-verified and kept: uncommitted SCORECARD, SKILL, QUALITY Q133, README frontier, SOURCES S315/S316, the knowledge r73 section, the lesson draft and `census/round-73/records/m2-guard-canfail.txt`. The wave seats reproduced every number these files cite (below), and the census validates EXIT=0. The writer had a half-finished, unused `_stat_forge_code(link=)` parameter. It was completed into selftest case 45 rather than discarded. Nothing was discarded.
- **Frozen predicates reproduced from committed bytes by the wave:**
  - S73ExecC1: all 5 items, including the mk-counter replay (byte-identical) and the freeze chronology F < I < K < W < A.
  - S73ExecC2: 10/10 receipts, probe 15/15, selftest 52/52.
  - S73Reviewer: zero prereg-vs-receipt mismatches. Grafting case 43 into the lane-base writer fails it (43/44), so the case discriminates.
  - Evidence: `census/round-73/records/wave-w1/seats/S73ExecC1.md`, `S73ExecC2.md`, `S73Reviewer.md`.
- **Wave repair after measurement (lesson M1)**, `4534dd17`. S73MutWriter found two writer mutants that kept both frozen detectors green: M05 (symlink target not compared, HIGH) and M01 (pre-run truth check dropped, MEDIUM).
  - Case 43's pre-run subcase now asserts that the wrapped command never ran.
  - New case 45 forges a tracked symlink behind a rewritten index stat entry, pre-run and in-run.
  - `census/round-73/records/wave-repair/selftest-writer.txt`: `SELFTEST cases=45 pass=45 fail=0`.
  - `selftest-M01.txt` and `selftest-M05.txt`: each `pass=44 fail=1`, EXIT=1.
  - No-harm: `c1-main-arm-wave-writer.txt` gives the same SUMMARY as `c1-after.txt`, EXIT=0.
- **Domain trial.** The stage-W writer ran over the lane itself (18987 tracked files) and wrote a receipt in about 2 s (attempt-1 L1). S73Reviewer's replica measured 0.81 s per truth pass with 0 false refusals (`S73Reviewer.md` item 1).
- **Frontier step.**
  - S315/S316 were opened this round. Captures are in `census/round-73/srcs/`. S73Scribe re-fetched both (HTTP 200, sha256 equal to the captures).
  - Gate: `corpus/lessons/round-73.md` `## Gate`.
  - Four mistakes mined: `## Mistakes` M1–M4.
  - Sourced claim: C1 rests on S315 and S316. The knowledge r73 section cites both.
- **r72 spot-check** (`corpus/lessons/round-72-verifier-spotcheck.md`). Routed D3(a) is answered by C1, D4(c) by C2 and D2 by the counter docstring. D1 is bookkeeping, done in the knowledge header. D3(b), D4(d) and D5 are routed on, named in the prereg and the lesson.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `?? .scratch/run15-wrapup/misroot-cff0b4cb/` (orchestrator-owned, not touched) and the uncommitted report. No seat wrote into the fleet root.
- **Pointer check.** `python3 -B tools/souji-pointer-check.py --root . --rev d8380f6d… corpus/lessons/round-73.md` gives `missing=4`, EXIT=1. None is a defect:
  - two `D1..D5` range spellings
  - the fleet-root `.ufo/watchdog.log`
  - the empty `S73CriticDiscern/` dir, which git does not track

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `23ecd070` `1eac307f` `aaacba33` `b84ff90b` `312e8f29` | attempt 1: freeze, counter + matrix, C1 controls, writer, after-arms | LOG.md "## Round 73 … attempt 2", bullet 1 |
| `4534dd17765fc9fc59a5dd3530220a49c819ca4f` | wave repair (writer cases 43/45), S315/S316, Q133, knowledge r73, README frontier, SKILL rows, SCORECARD r73/r74, LOG, lesson, `records/census-after.txt`, `records/m2-guard-canfail.txt`, `records/wave-repair/` | bullets 1–5 |
| `35192856ada1f1cec9243f988a1825e68d3ca614` | wave w1 evidence mirrored to `census/round-73/records/wave-w1/` (spec, dispatch, results, ready markers, 12 seat dirs, 7 reports) | bullet 3 |
| `d8380f6d04dbda5f3c8ac804eb3149466f9b256b` | lesson pointers moved to the committed mirror | bullet 3 |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `controls/c1-K-a-do-nothing.txt`: `new_forgeries=3 new_honest=21 class_mismatches=3`, EXIT=1 (FX1–FX3 `new=accept`). Blanket refusal `new_honest=0` EXIT=1. Forger `new_forgeries=15` EXIT=1. | `records/c1-after.txt`: `SUMMARY matrix=80 base_forgeries=15 base_honest=21 base_mismatches=0 base_unwitnessed=0 new_unwitnessed=0 new_forgeries=0 new_honest=21 class_mismatches=0 new_echo=0 errors=0 regress=PASS`, EXIT=0. Writer selftest 44/44. | `grep -E '^(SUMMARY\|EXIT=)' census/round-73/records/c1-after.txt census/round-73/controls/c1-K-a-do-nothing.txt` | writer `b84ff90bff05fb057c5a8c4b0661a9ec41d9e4a2` |
| C2 | `controls/c2-before-r72-D1..D5.txt`: the r72 counter with each defang edit gives `base_forgeries=12 base_mismatches=0`, EXIT=0 each. 0 of 5 detected. | `records/c2-after-D1..D5.txt`: `base_unwitnessed=1`, plus `base_witness=no` on the edited row (FWr FWi FWp FWs FC3). 5 of 5 detected. Positive control: `base_unwitnessed=0`. Counter selftest 52/52. | `for k in 1 2 3 4 5; do grep -cE '^SUMMARY .*base_unwitnessed=1( \|$)' census/round-73/records/c2-after-D$k.txt; done` | counter `1eac307f7cc8d1e30df009eabb693875ace97976` |

Both frozen predicates are met, and each claim beat its committed do-nothing control. No owned axis score changed: calibration 7, coverage 8, operability 8.

Qualifications from the wave, reported rather than prettified:

- **C2 witness is tree-global, not per-row** (S73ExecC2 MEDIUM). Defanged FWw, FC1 and FC2 still print `base_witness=yes`. The witness discriminates on 12 of the 15 base-accepted refuse rows. The frozen D1–D5 predicate is unaffected. This contradicts Q133's per-row wording, mined as lesson M2 and routed to r74.
- **Four counter mutants survived** (S73MutCounter): M08 (fail-open witness read), M14 (symlink witness kind), M15 (gitlink skip), M17 (`new_unwitnessed` ungated). A fifth survivor, M12, is equivalent. 12 of 17 mutants were killed.
- **C1 coverage was narrower than its text** at `b84ff90b` (M01 and M05). Both were repaired in-round after measurement, as shown above. M03 (instrument re-compare shadowed) is routed.

## Sources & frontier

- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  - before: `census/round-73/records/census-before.txt`, `souji ok`, 86 W04, EXIT=0
  - after: `census/round-73/records/census-after.txt`, `souji ok`, 86 W04, EXIT=0
- **Rows** (counted with `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 237 → 239.
  - Added: tier A ×2. S315 is racy-git.adoc at v2.56.0; S316 is git-hash-object(1) `--no-filters`. Both are `mined`, and both are cited by `corpus/knowledge/filter-filemode-witness.md` r73.
  - Rejected: S73Scribe's alternative S316 anchor and its 26-word racy-git quote (over the cap).
  - Rows touched old→new: none.
- **Frontier advanced.** New README entry "Frontier (r73 index stat cache and forgery witness)": a clean `git status` is a stat-cache verdict. It stays frontier, not Core.
- **Assimilation: none.** `considerthese/` is absent in this lane, and no shokuknow theme fits the frozen claims (§10 frozen/resumed rounds).

## Trend verdicts

- **expansion: improved.** Two tier-A rows on new ground: the stat-cache shortcut and the hash-object conversion. A new knowledge section and two SKILL gate rows (r73 matrix, defang set). The writer refuses a new forgery class, and the counter gained a self-witness.
- **quality: improved.** Own instrument defects were found by seats and repaired in-round, with fixes shown able to fail: M01 and M05 went from survived to killed. Every number in the attempt-1 drafts was re-derived by 3 seats from committed bytes.
- **discernment: unchanged.** Q133 was added, but the lane's own wave showed the counter meets it on only 12 of 15 rows. Five seats left no verdict file, and no non-author spot-check has run yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r73 byte-truth matrix with forgery witness (C1/C2)" and "r73 defang set (C2)" (`4534dd17`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 73". The stage-W writer ran over the lane's 18987 tracked files, and the 80-row matrix ran end to end (`census/round-73/records/c1-after.txt`, `records/wave-repair/c1-main-arm-wave-writer.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: three seats ran the prereg/SKILL commands as written and reproduced every predicate (`census/round-73/records/wave-w1/seats/S73ExecC1.md`, `S73ExecC2.md`, `S73Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: the sibling clean-tree gate findings were documented, not edited (`census/round-73/records/wave-w1/seats/S73Connector.md`), and there was no fleet misroot.

## Other

- **Round shape: one v1 wave `w1` of 12 seats**, dispatched by attempt 1 (`census/round-73/records/wave-w1/w1-dispatch.json`). WAVE-DONE was received by this attempt. No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1.
  - Attack seats: 5 of 12 (42 %).
  - The L1 holds the §3 planner seat.
- **Dead seats: 0 reported.** `w1-results.json` carries no seat output because the orchestrator kernel restarted mid-wave. Seven seats wrote report files. Five did not, and are counted as no verdict: S73ScoutSources, S73ExecEvade, S73CriticClaims, S73CriticDiscern, S73Sentinel. Lesson M4.
- **Routed to r74** (lesson "Routed to round 74"):
  - a row-specific witness
  - counter survivors M08, M14, M15, M17
  - writer M03
  - the lane's own `git status`-trusting gates (`tools/souji-pre-report-gate.sh:36-37`, `tools/souji-verify.sh`; S73Connector HIGH)
  - `base_forgeries` is not witness-gated
- **Open L0 questions:** none new. Earlier `souji | round-67`, `round-68` and `round-70` remain with the operator.
- **Stale-lane:** respawn-per-round driver; this lane has no other open mission.
- **Tool installs:** none. No pacman transaction, and no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r73/` was removed at landing.
