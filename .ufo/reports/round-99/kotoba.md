# kotoba — round 99 report (KotobaR99, attempt 1, Linux host, omp)

Lane repo `kotoba-shokunin`, branch `master`. Base `52e8e95ac4faf4ded84d7b82cbc204792590d0f7` →
final lane tip `0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3` (`git ls-remote origin refs/heads/master`
prints `0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3`). Verdicts belong to the non-author closure.

## Work performed

I declared **two** claims:

- **C1 — depth** (the lowest owned non-retired axis, score 9). The dispatch-prompt checker's self-test
  (`verifiers/verify_dispatch_prompts.py --self-test`) must kill twelve frozen survivors, t01..t12.
  These are MutTesterDispatchR98's verdict-bearing survivors n01–n05, n07–n11, n13 and n14. Four of
  them reach the live CLI (`run_checks`, `main`'s exit code and `--check`, `read_text`'s substrate
  error), which the self-test had never called. C1 is sourced on S281 (Python argparse,
  `action='append'`), opened this round.
- **C2 — consistency** (calibration sub-axis, score 10). The three tip-battery gates must read green
  without weakening any gate. The gates are `verify_skill_checklist.py` (red since the round-81
  record), `verify_corpus_integrity.py` and `verify_corpus_independent.py` (both red since round 88).
  This was round-98 closure routed defect 6.

**Outcome as frozen:** C1 is MET and C2 is MET at the landing `bacb1541`.

- **Inherited state.** The lane was clean at the base. The watchdog shows one launch and no
  `lane-dead-no-report`, so nothing was inherited. There is no operator lesson. The round-98
  spot-check's six routed defects are dispositioned in `kotoba-shokunin/plans/round-99.md` §
  Inherited state:
  - Defect 6 → C2.
  - Defects 2, 3 and 5 → corrections C99-1, C99-2 and C99-3 in `corpus/lessons/round-99.md`, plus a
    SCORECARD correction.
  - Defect 4: there were no g11 runs this round, and `ls /dev/shm | grep -c r97` gives 0.
  - Defect 1 (the v7 counter) is **carried to round 100**, with the reason stated in the plan.
- **Instrument commit `c0489d14156a7687d10ae5389d72eaa923b2bc29`.** It contains two counters:
  - `verifiers/fixtures/round-99/selftest-kills.py` (v6.1): the v6 rules unchanged, a new `c1` table,
    and the old table kept as `r98c1`.
  - `verifiers/fixtures/round-99/carried-reds.py` (v1). It runs the three gates in a fleet-shaped
    sandbox, their self-tests at the base assertion floors (1864/178/109), and four frozen-byte
    conjuncts:
    - both corpus gates are byte-identical to the base;
    - the battery is identical outside `INSTRUMENT_PINS`;
    - the checklist is identical outside its `GOVERNANCE_CORRECTIONS` data (literal-eval'd, base rows kept);
    - the battery's guards read 5 of 5.
- **Freeze commit `b53e209603e7c480cd975ea543e415b66f695438`.** It contains the plan, the pre-data
  receipts and five committed C2 forgery controls (w1–w5, `receipts/ctl-worlds/*.patch`), all UNMET.
  w4 forces a PASS and admits its blob in the battery pins; the frozen-bytes conjunct alone refuses it.
- **Addendum 1, commit `e215f0f9c053d8d914f94c19ead4d8ea2bc22fa9`, made before any landing reading.**
  ScoutSourcesR99 F1 showed that the `/3/` argparse page is a rolling build: its digest changes with
  the footer timestamp. S281 therefore cites the version-pinned `release/3.15.2` page. S253, S270 and
  S276 have the same rolling-digest defect; that is routed to round 100.
- **Wave `r99-w1`.** 11 seats; the reports are in `kotoba-shokunin/.ufo/waves/round-99/w1/*.md`.
  - **ExecArmsR99** wrote the C1 arms: +270 lines in one hunk inside `self_test()`, taking the
    self-test from 128 to 154 assertions.
  - **ExecRedsR99** wrote the C2 data-only repair:
    - 9 coverage-map rows;
    - `round-81.md:8` hash quoting;
    - one appended LOG.md correction notice and 16 correction rows, including the re-pin of row 2621
      from 158 to 161;
    - one battery pin;
    - a baseline re-record.
  - **ScribeCorpusR99** wrote S281 and the lesson.
  - **ScoutSourcesR99** found the rolling-digest defect and supplied the S279 CAP_SYS_PTRACE conjunct.
  - **ReviewerArmsR99** found nothing blocking.
  - **ReviewerRedsR99** found no laundering: every corrected token names the same artefact (Q64/M118 test).
  - **CriticClaimR99** judged both claims MET on the full candidate, with defects D4 and D5. It also
    found that C2 is not separable at its single-patch candidate.
  - **SentinelScopeR99** found scope clean and no-harm PASS.
  - **MutTesterRedsR99** found that 4 of its 10 new worlds read MET under the C2 counter.
  - **MutTesterDispatchR99** found 8 of 22 new mutants surviving.
  - **ConnectorOverlapR99** mapped the cross-claim coupling, sibling instances of the same class, and
    round-100 candidates.
- **Integration.** I applied the patches in the order ExecRedsR99 `bd32f78d…`, ScribeCorpusR99
  `94a39dee…`, ExecArmsR99 `9b705bc8…`. I then:
  - added QUALITY **Q89**;
  - filled the lesson's Settlement and added a second mined mistake;
  - re-recorded the baseline equal counts as 204/175/72, after every corpus file was in place. This
    is CriticClaimR99 D4: the builder's interim 203/174/72 were counted on its single-patch tree.
  - removed an untracked 366 MB clone a seat had left at the lane root (a directory named repo).
- **Addendum 2** (`kotoba-shokunin/plans/round-99-addendum-2.md`) records the post-data disclosures B1–B5.
- **Planner seat.** I held it as L1, because the validator rejects `planner`. ConnectorOverlapR99
  Part 3 carried the planning data-walk.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*`
  (orchestrator-owned) and `w4lines.txt`, a pre-existing file with numeric content and no kotoba
  content. No fleet misroot. The lane-root misroot is the one above.
- **Scratch.** I removed `/fast/scratch/hyaku/kotoba-r99` after landing.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `c0489d14156a7687d10ae5389d72eaa923b2bc29` | instruments: v6.1 kill counter and carried-reds v1 | § Round 99, "Claims as frozen" |
| `b53e209603e7c480cd975ea543e415b66f695438` | freeze: plan, pre-data receipts, w1–w5 control patches, S281 access record, wave generator | § Round 99, "Pre-data controls" |
| `e215f0f9c053d8d914f94c19ead4d8ea2bc22fa9` | addendum 1: S281 cites the version-pinned page | § Round 99, "Addendum 1" |
| `bacb154137ced07e088acf63199f5cb297b531f7` | landing: arms r99-t01..t12; C2 repair (index rows, round-81 quoting, correction notice + rows, pin, baseline 204/175/72); S281; Q89; lesson; LOG; SCORECARD (r98 correction, r100 plan) | § Round 99, "Integration" |
| `e6c59844c0a510f681c116563dc9f8d23dad86c8` | record: landing receipts, addendum 2, wave evidence (spec, dispatch, ready, results, 11 reports), LOG and SCORECARD annotations | § Round 99, "Landing readings", "No-harm", "Wave" |
| `0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3` | tip no-harm receipts: C2 MET at the record tip; census | § Round 99, "No-harm" (the tip reading) |

Every commit printed `landed <hash>` from `jj-lane.sh`. `jj-lane.sh state` shows
`local=remote=0a65cceb… ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

### C1

Counting command: `python3 -B verifiers/fixtures/round-99/selftest-kills.py c1 <rev>`.

- **Before**, at the base `52e8e95a` (`kotoba-shokunin/.ufo/waves/round-99/receipts/redbefore-c1-base.txt`):
  `C1 targets killed 0 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12`,
  giving `C1-PREDICATE-UNMET` rc 1. `--rules v5` gives the same result.
- **After**, at landing `bacb1541` (`receipts/landing/c1-v61.txt`):
  `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12`,
  giving `C1-PREDICATE-MET` rc 0. `c1-rulesv5.txt` is MET with the same tally.
- **Kill-rule conjuncts:**
  - `r98c1` 9/9, `r97c1` 13/13, `r96c1` and `r95c1` are all MET;
  - `--box-proof` reads `boxes proven 2` rc 0;
  - `prod-identity.txt` shows the single hunk `@@ -1514,0 +1515,270 @@ def self_test()`;
  - `instr-identity.txt`: the counter bytes equal `c0489d14`.

### C2

Counting command: `python3 -B verifiers/fixtures/round-99/carried-reds.py <rev>`.

- **Before**, at `52e8e95a` (`receipts/c2-base.txt`):
  `C2 carried reds green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok`, giving
  `C2-PREDICATE-UNMET` rc 1.
- **Forgery controls w1–w5:** all UNMET (`receipts/c2-ctl-*.txt`).
- **After**, at landing `bacb1541` (`receipts/landing/c2.txt`):
  `C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok`, giving
  `C2-PREDICATE-MET` rc 0. The battery line inside it reads
  `guards 5 of 5; tip battery exit 0: 6 of 6`.
- **At the record tip `e6c59844`** (`receipts/landing/c2-record-tip.txt`): also MET.
- **Disclosed bound** (addendum 2 B1). MutTesterRedsR99 built four worlds after the freeze that read
  MET without the honest content:
  - in-place rewrite of governance lines;
  - a correction target that is not bound to the original artefact;
  - a correction row pinned to a pre-existing line;
  - a wildcard index row.

  The landing uses none of these shapes (`receipts/landing/post-hoc-holes.txt`):
  - LOG.md and SCORECARD.md are append-only from the base;
  - the 16 new correction rows pin lines 3586–3601, after the base's 3580 lines;
  - the 9 added rows contain 0 wildcards.

  The frozen kill rule names only the frozen controls, so these four worlds are counter findings
  routed to round 100, not a kill. That is for the closure to rule on.
- **Separability** (addendum 2 B2). C1 reads MET on its single-patch candidate. C2 cannot by
  construction, because its index row precedes the lesson file. The landing is C2's smallest green unit.

## Sources & frontier

- **Census.** Command:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
  - Round start: rc 0, 34 `W04` (`receipts/census-before.txt`).
  - Round end, at landing and at the tip: rc 0, last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, 34 `W04` (`receipts/landing/census-end.txt`, `census-end-tip.txt`).
- **Rows.** Counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 206 → 207.
- **Added, tier A, mined:** S281, Python argparse at `https://docs.python.org/release/3.15.2/library/argparse.html`.
  It was opened 2026-11-06: HTTP 200, 327874 B, sha256 `36e8d536…`, with a 22-word quote at HTML
  989–990. The L1's `/3/` reading is recorded in the row as superseded-by-pin. The Gate is in
  `corpus/lessons/round-99.md`.
- **Rows touched old→new:** none. S279, S253, S270 and S276 were re-opened and deliberately left
  unedited (lesson § Status changes).
- **Frontier rows advanced:** none.
- **Sourced claim:** C1's t08 arm rests on S281.
- **Mined mistakes** (`corpus/lessons/round-99.md`):
  1. `governance-cell-cites-fleet-path-repo-rooted`.
     - captured-by: `governance.citation_resolves`, but the landing no-harm rule accepted an
       unchanged red set from round 92 on.
     - fix: C2 plus **Q89**.
     - shown able to fail: `c2-base.txt` reads 0 of 3.
  2. `seat-scratch-clone-misrooted-in-lane`.
     - fix: removed before landing, and the lane-root status was added to the sweep.
- **Corrections:**
  - C99-1: the round-98 report's "+183 lines inside `self_test()`" is **182**; 183 was the two-file total.
  - C99-2: the SCORECARD round-98 red-before revision is `a060b450`, not `63cd48d9`; also appended to SCORECARD.md.
  - C99-3: S279 omits step (4)'s `CAP_SYS_PTRACE` conjunct.
  - C99-4: rolling-alias digests.
- **Assimilation:** none; this round takes no `merge/kotoba/` theme. `considerthese/2026-10-26.md` was
  re-read; all five proposals remain unimplemented and are measured in the lesson § Considerthese.

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was added. S281 is a registry row that grounds an
  instrument arm.
- **quality: improved.** Two changes:
  - C1: the province instrument's self-test now kills twelve more frozen behaviours, 0 → 12, with
    production code unchanged. For the first time it covers the CLI exit and `--check` paths.
  - C2: the lane's own tip battery reads 6 of 6, where it had been red since the round-81 record. No
    gate code changed: both corpus gates are byte-identical, and the checklist changed only in its
    corrections data.
- **discernment: improved.** Sources and disclosures:
  - The rolling-digest defect was caught before landing and the row was re-pointed to a pinned page,
    with three older rows named.
  - Five frozen forgery controls preceded the C2 data.
  - The four post-freeze C2 counter holes and eight C1 survivors are disclosed, not claimed away.
  - The laundering review found every correction to be the same artefact.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `kotoba-shokunin/SHONEN.md:5`. SKILL.md is unchanged this round. The checklist gate that proves its boxes now reads all 11 checks PASS (`kotoba-shokunin/.ufo/waves/round-99/receipts/landing/c2.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence `kotoba-shokunin/LOG.md` § Round 99 (freeze → wave → landing → no-harm, run by the lane; no non-author credit claimed).
- [~] Instructions executable by an agent without oral context — evidence `kotoba-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md`; untouched this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `kotoba-shokunin/PROVINCE.md` § Adjacent, unchanged. ConnectorOverlapR99 Part 2 reported sibling instances of the unchanged-red-set and repo-rooted fleet citation classes, and no sibling was edited (`kotoba-shokunin/.ufo/waves/round-99/w1/ConnectorOverlapR99.md`).

## Extras

- **Round shape:** one v1 wave, `r99-w1`, with 11 seats:
  - executor 2, scribe 1, scout 1, connector 1;
  - reviewer 2, mutation-tester 2, critic 1, sentinel 1.

  Attack seats are 5 of 11 (45 %). There was no residual call; the round total is 11. Roles were
  routed by `task.agentModelOverrides`, and no `model` was passed.
- **Dead seats:** 0. All 11 settled and wrote reports (`r99-w1-results.json`).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none, by me or by any seat according to their reports.
- **Open L0 questions:** none new. considerthese proposal 2 stays L0-routed.
- **Routed to round 100** (SCORECARD "Round 100 planned"):
  - the v7 counter for g11 and g16;
  - the `strip_token_dressing` comma-anchor code fix;
  - superseding rows for S253, S270 and S276;
  - the four C2 counter holes;
  - the C1 exit-2-ladder survivors (MutTesterDispatchR99 F2).
