# kotoba — round 98 report (KotobaR98, attempt 1, Linux host, omp)

Lane repo `kotoba-shokunin`, branch `master`. Base `a33f262fc94e3cf27f3c935b5c53c1336bb94166` →
final lane tip `f5181e0fc01b1193983e5e8d30204ad5b83b654a` (`git ls-remote origin refs/heads/master`
prints `f5181e0fc01b1193983e5e8d30204ad5b83b654a`). Verdicts belong to the non-author closure.

## Work performed

I declared **two** claims.

- **C1 — depth.** This is the lowest owned non-retired axis, at score 9. The dispatch-prompt
  checker's self-test (`verifiers/verify_dispatch_prompts.py --self-test`) must kill nine frozen
  survivors, t01..t09. They are MutTesterDispatchR97's verdict-bearing survivors m20, m22–m28 and m31.
  m32 and m34 were excluded by rule as no-verdict mutants.
- **C2 — consistency (calibration sub-axis, score 10).** The new v6 kill counter must refuse the
  round-97 forgery worlds g10 (compares itself against the committed HEAD) and g11 (replays the
  schedule from a seed). It must also still refuse g3, g7 and g8 and hold the honest worlds h1 and
  h2. C2 is sourced on S277, S278 and S279, opened this round, and on the re-opened S265.

**Outcome as frozen:** C1 is MET. **C2 is UNMET at the landing reading** (4 of 5), so C2 is an honest
stop (see below).

- **Inherited state.** The lane was clean at the base. `.ufo/watchdog.log` shows a single launch of
  round 98 and no `lane-dead-no-report kotoba round=98`, so there was nothing to inherit. There is no
  operator lesson. The eight routed defects in `corpus/lessons/round-97-verifier-spotcheck.md` are
  dispositioned in `plans/round-98.md:18-41`.
  - Defect 2 → C2.
  - Defect 4 → C1.
  - Defect 5 (traceback) → v6 rule 10.
  - Defect 6 → excluded no-verdict mutants.
  - Defect 7 → line excerpts kept beside the digests.
  - Defects 1 and 3 → carried and measured.
- **Instruments, commit `a060b450a43673ebc54720a5192e99df188e80ce`:**
  - the v6 counter `verifiers/fixtures/round-98/selftest-kills.py` (sha256 `2f31fe04…`), which adds
    rule 8 (a git-less `git archive` world copied per run with reflink), rule 9 (a minimal six-variable
    child environment and a non-dumpable counter) and rule 10 (a total exit ladder), plus the new
    `c1` table;
  - the C2 runner `verifiers/fixtures/round-98/forgery-controls.py` (sha256 `c4710da7…`).
- **Freeze, commit `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`.** It contains the plan and the pre-data
  receipts in `.ufo/waves/round-98/receipts/`:
  - `redbefore-c1-base.txt`: 0 of 9, UNMET;
  - `poscontrol-r97c1/r96c1/r95c1-base.txt`: all MET;
  - `c2-before-v5.txt` and `c2-v6-as-v5.txt`: 3 of 5 each;
  - `c2-v6.txt`: 5 of 5;
  - `sources-opened.txt`.
- **Wave `r98-w1`.** 12 seats, with reports in `.ufo/waves/round-98/w1/*.md`.
  - **ExecArmsR98** added 23 behavioural arms (`ExecArmsR98.md`). The self-test went from 105 to 128
    assertions.
  - **ScribeCorpusR98** wrote the rows and the lesson scaffold.
  - **ScoutSourcesR98** re-opened all four sources. It found the duplicate URL and the missing denial
    authority, ptrace(2).
  - **ScoutTipReds** traced the three carried red gates to round 81/82 governance-pin drift and to
    corpus-index drift.
  - **ReviewerArmsR98** and **ReviewerCounterV6** found nothing blocking. ReviewerCounterV6 probed
    rules 8, 9 and 10 directly: no `.git` in the world, six environment variables, a
    `PermissionError` on reading environ, and exit 2 instead of a traceback.
  - **CriticClaimR98** judged C1 MET and C2 MET at the freeze. Its defects D1–D7 include that t07 is
    observable-only.
  - **SentinelScopeR98** passed scope and safety, and flagged the census W04 that addendum 1
    resolved.
  - **ExecForgeryV6** built g13–g16:
    - g13 (cmdline) and g15 (filesystem scan) read MET, which is the disclosed bound;
    - g16 (reads the pristine export) reads MET under v6 only;
    - g14 (environ) is refused.
  - **MutTesterCounterV6** found that C2's world set kills 3 of 12 counter-rule mutants (W1, V6, V8).
    It also built new control worlds for the nine survivors.
  - **MutTesterDispatchR98** ran 20 new mutants: 16 survive at the candidate, and n15 was killed
    incidentally.
  - **ConnectorOverlapR98** ran the anchor-collision scan and the sibling g10/g11-class census, and
    proposed three round-99 candidates.
- **Addendum 1** (`plans/round-98-addendum-1.md`, written before the landing reading):
  - The subprocess page is cited by its existing id S265, per Q84, instead of a new row.
  - ptrace(2) is admitted as S279.
  - Rows are re-pointed by document: S277 git-archive, S278 proc_pid_environ, S279 ptrace(2), S280
    PR_SET_DUMPABLE (rejected).
- **Addendum 2** (`plans/round-98-addendum-2.md`, post-data disclosures B1–B6):
  - B1: C2 landing reading UNMET;
  - B2: t07 is observable-only;
  - B3: g13, g15 and g16;
  - B4: the tip battery under host load;
  - B5: carried items;
  - B6: diagnostic re-read.
- **Planner seat.** I held it as L1, because the validator rejects `planner`. ConnectorOverlapR98
  Part 3 carried the planning data-walk.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*`
  (orchestrator-owned) and `w4lines.txt`. The latter predates this round and carries no kotoba
  content. No misroot.
- **Scratch.** `/fast/scratch/hyaku/kotoba-r98` was removed after landing. Leftover 1-byte
  `/dev/shm/.r97-g11-run.*` markers come from g11 world runs, both mine and the seats'. I did not
  remove them, because they cannot be attributed to one owner.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `a060b450a43673ebc54720a5192e99df188e80ce` | instruments: the v6 counter and the C2 runner | § Round 98, "Claims as frozen" |
| `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248` | freeze: plan and pre-data receipts | § Round 98, "Pre-data controls" |
| `e61629f5d582e5518ccfe023c62d1fd26dd1870d` | landing: self-test arms r98-t01..t09 (+183 lines inside `self_test()`); S277–S280; S265 `used-by`; Q88; `corpus/lessons/round-98.md`; README index row; addendum 1 | § Round 98, "Addendum 1", "Landing" |
| `280d8d01e3992b00c026b751c88b8c2bf317e66c` | record: landing receipts and runner, addendum 2, lesson settlement, LOG, SCORECARD | § Round 98, "No-harm at landing", "Integration" |
| `f5181e0fc01b1193983e5e8d30204ad5b83b654a` | wave evidence: spec, dispatch, ready, results, 12 seat reports with receipts, generator; end census; C2 diagnostic re-read; addendum 2 B6 | § Round 98, "Wave" |

Every commit printed `landed <hash>` from `jj-lane.sh`. `jj-lane.sh state` shows
`local=remote=f5181e0f… ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

### C1

Counting command: `python3 -B verifiers/fixtures/round-98/selftest-kills.py c1 <rev>`.

- **Before**, at the instrument commit `a060b450` (`receipts/redbefore-c1-base.txt`):
  `C1 targets killed 0 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`,
  giving `C1-PREDICATE-UNMET` rc 1. Production and self-test bytes there equal the round base. This
  is the do-nothing control; `--rules v5` gives the same result.
- **After**, at landing `e61629f5d582e5518ccfe023c62d1fd26dd1870d` (`receipts/landing/c1-v6.txt`):
  `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`
  and `rules v6: honest runs CLEAN 3 of 3; mirror runs reported 10 of 10`, giving `C1-PREDICATE-MET`
  rc 0.
- **Separability:** `c1-rulesv5.txt` is MET with the same tally.
- **Kill-rule conjuncts at landing:**
  - `r97c1-v6.txt` 13 of 13, `r96c1-v6.txt` 11 of 11 and `r95c1-v6.txt` 3 of 3 are all MET;
  - `dp-boxproof.txt` reads `boxes proven 2`;
  - `prod-identity.txt` shows a single insertion hunk, `1333a1334,1515`, inside `self_test()`.
- **Bound:** eight of the nine kills are verdict-bearing. t07 is observable-only (addendum 2 B2).

### C2

Counting command: `python3 -B verifiers/fixtures/round-98/forgery-controls.py v6 <rev>`.

- **Before:**
  - the do-nothing control, v5 (`receipts/c2-before-v5.txt`), reads
    `forgeries refused 3 of 5; honest held 2 of 2`, UNMET rc 1, with g10 and g11 reading MET;
  - the cause control, v6-as-v5 (`receipts/c2-v6-as-v5.txt`), reads `refused 3 of 5`;
  - the pre-data v6 reading at `a060b450` (`receipts/c2-v6.txt`) reads `refused 5 of 5`, MET.
- **After**, at landing `e61629f5` (`receipts/landing/c2-v6.txt`, 09:08–09:14):
  `C2 v6: forgeries refused 4 of 5; honest held 2 of 2; bound g2b MET` gives **`C2-PREDICATE-UNMET`
  rc 1**. g11 (seeded) read MET. The counter and runner bytes are identical to the instrument commit
  (`instr-identity.txt`).
- **Honest stop as frozen.** The cause is in addendum 2 B1. Under v6, g11 falls back to a marker in
  `/dev/shm`. The interior honest run reads CLEAN only if that marker is gone, and ExecForgeryV6 was
  removing `/dev/shm/.r97-*` during the same window. [INFERENCE: this is the likely trigger; it is not
  proven per run.]
- **Diagnostic only.** After WAVE-DONE, the same command at the same revision read `refused 5 of 5`,
  MET (`receipts/landing/c2-v6-diagnostic-rerun.txt`). It does not replace the landing reading.

### No-harm at landing

All receipts are in `receipts/landing/`:

- round-97 counter: `c1` and `r96c1` MET; the round-97 C2 runner reads `refused 3 of 3; honest held 2 of 2`, MET;
- round-96 `c1`, round-95 `c1`, the round-93 kill-pin and the round-92 controls: all MET;
- gate registry 74 of 74;
- floors self-test 176 assertions;
- live dispatch verdict lines are equal at base and landing (`dp-live-equal.txt` rc 0);
- SKILL.md is unchanged;
- census exit 0 with 34 `W04`.

The tip battery reads `2 of 6` at landing. A paired re-run under the same host load (load ≈ 35)
reads `2 of 6` at the freeze too (`tip-battery-base-rerun1.txt`) and `2 of 6` at landing
(`tip-battery-landing-rerun1.txt`). In both, `check_assertion_floors.py` times out at the flat 280 s
cap. The red set is equal at base and landing, so this is host load and not a landing change
(addendum 2 B4).

## Sources & frontier

- **Census.** Command:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
  - Round start: rc 0, 34 `W04` (`receipts/census-before.txt`).
  - Round end: rc 0, last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, 34 `W04` (`receipts/census-end.txt`).
- **Rows.** Counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`:
  202 → 206.
- **Added, tier A, mined:**
  - S277: git-archive(1) § DESCRIPTION; grounds rule 8.
  - S278: proc_pid_environ(5); the access check that governs environ reads.
  - S279: ptrace(2), `PTRACE_MODE_READ` list and access-check step (4); the dumpable denial, and the
    located basis of the cmdline bound.
- **Added, tier A, rejected:** S280, PR_SET_DUMPABLE(2const). It is redundant, its reason is
  corrected in the row, and it carries a flip condition.
- All four rows were opened 2026-11-06. Their access records, line excerpts and located quotes are in
  `corpus/lessons/round-98.md` § Gate.
- **Rows touched old→new:** S265 `used-by` gains `corpus/lessons/round-98.md` (S265 was re-opened and
  cited by id per Q84). This is logged in the lesson's § Status changes.
- **Sourced claim:** C2 cites S265, S277, S278 and S279, through the plan § C2 and addendum 1.
- **Mined mistakes** (`corpus/lessons/round-98.md` § Mistakes):
  1. `measured-child-reads-counter-state`.
     - captured-by: Q87, which named neither history nor environment.
     - fix: v6 rules 8–9 plus the new criterion **Q88**.
     - shown able to fail: v6-as-v5 refuses 3 of 5.
  2. `plan-pre-commits-row-on-held-url`, a repeat of the Q84 class.
     - fix: addendum 1, made before landing.
     - shown able to fail: the as-planned candidate read `W04` 35, against 34 after integration.
- **Corrections:**
  - C98-1 and C98-2: receipt word counts of 22 vs 23 and 15 vs 14.
  - C98-3: the S280 rejection reason.
- **Assimilation:** none; this round takes no `merge/kotoba/` theme. `considerthese/2026-10-26.md` was
  re-read and no proposal was implemented (lesson § Considerthese).
- **Wave evidence bytes (Q82):** `du -sb .ufo/waves/round-98` gives 1549978, against 1505669 in
  round 97 and 1941368 in round 96. Source HTML was stored as digest plus excerpt only.

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was added. S277–S280 are registry rows cited by the
  plan, the addenda and the lesson.
- **quality: improved, for C1 only.** The province instrument's self-test now catches nine behaviours
  it missed (0 → 9 at `e61629f5`, eight of them verdict-bearing), and production code is unchanged.
  C2's landing reading missed its target, so that half of the round is not counted.
- **discernment: improved.** Sources and mistakes:
  - Three sources were admitted and one rejected, each with a stated reason.
  - A duplicate-URL row the plan pre-committed was refused by addendum before landing.
  - The C2 miss, the observable-only t07 and three new forgery classes, one of them a v6-specific
    hole (g16), are disclosed rather than claimed away.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SHONEN.md:5`. Boxes `dispatch.04` and `dispatch.08` now carry a self-test that kills nine more frozen mutants (`kotoba-shokunin/.ufo/waves/round-98/receipts/landing/c1-v6.txt`). SKILL.md is unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence `LOG.md` § Round 98 (freeze → wave → landing → no-harm, run by the lane; no non-author credit claimed).
- [~] Instructions executable by an agent without oral context — evidence `corpus/lessons/round-8-aggregator-box3-coldrun.md`; untouched this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `PROVINCE.md` § Adjacent, unchanged this round. ConnectorOverlapR98 Part 2 found the g10/g11 class in sibling harnesses. I reported it and edited no sibling (`kotoba-shokunin/.ufo/waves/round-98/w1/ConnectorOverlapR98.md`).

## Extras

- **Round shape:** one v1 wave, `r98-w1`, with 12 seats:
  - executor 2, scout 2, scribe 1, connector 1;
  - reviewer 2, mutation-tester 2, critic 1, sentinel 1.

  Attack seats are 5 of 12 (42 %). There was no residual call; the round total is 12.
- **Dead seats:** 0. All 12 wrote their report files. `r98-w1-results.json` notes that the
  orchestrator kernel restarted mid-wave and did not retain the seats' final text, so I used the
  report files.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none, by me or by any seat according to their reports.
- **Open L0 questions:** none new. considerthese proposal 2 stays L0-routed as before.
- **Routed to round 99** (SCORECARD § planned):
  - a v7 counter that refuses g11 with its marker deleted and refuses g16, which reads the pristine
    export;
  - committed controls for the nine counter-rule mutants that survive (MutTesterCounterV6);
  - the tip-battery reds with ScoutTipReds' causes;
  - the three-artifact raise of the `dispatch_prompts` floor (56 vs 128).
