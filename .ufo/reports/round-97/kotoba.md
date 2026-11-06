# kotoba — round 97 report (KotobaR97, attempt 1 relaunch, Linux host, omp)

Lane repo `kotoba-shokunin`, branch `master`. Base `fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520` →
final lane tip `1d44bd820cf4ec53a37baba2b45f6da7776a84bd` (`git ls-remote origin refs/heads/master`
prints `1d44bd820cf4ec53a37baba2b45f6da7776a84bd`). Verdicts belong to the non-author closure.

## Work performed

Declared claims: **two**. **C1 — depth** (the lowest owned non-retired axis, score 9): the
dispatch-prompt checker's self-test (`verifiers/verify_dispatch_prompts.py --self-test`, the executable
proof of SKILL.md § Dispatch-prompt fidelity boxes `dispatch.04`/`dispatch.08`) kills thirteen more frozen
survivors t01..t13. **C2 — consistency (calibration sub-axis, score 10)**: the v5 kill counter refuses the
three round-96 no-arm forgery worlds g3/g7/g8 while the honest worlds h1/h2 hold. C2 is sourced on S273
and S274, both opened this round.

- **Inherited state (earlier attempt).** `.ufo/watchdog.log` shows the first launch at 00:44 and three
  `lane-dead-no-report kotoba round=97` lines. That attempt landed the instrument commits
  `7c01b10d`/`94a10217` and the freeze `148395bf42af97436b1b832a97a175515f981939`. It dispatched and
  settled wave `r97-w1` (`.ufo/waves/round-97/r97-w1.ready.dispatched`, `r97-w1-results.json`, 11
  seats) and staged the integration in the working tree, but nothing landed after the freeze. **What I
  reused after re-verifying it:**
  - the freeze and pre-data receipts, unchanged;
  - the wave results;
  - the staged verifier diff. It equals `w1/ExecArmsR97/ExecArmsR97.patch` (sha256 `22638a4e…8973c80`,
    matches `ExecArmsR97_READY`; `git apply --check -R` is clean) and is one hunk inside `self_test()`;
  - the staged corpus rows, Q87, the README row and the lesson draft, all census-clean.

  **Discarded:** nothing. No new wave was needed, because the frozen claims run unchanged (§10 "Frozen
  and resumed rounds").
- **Round-96 spot-check** (`corpus/lessons/round-96-verifier-spotcheck.md`): its seven routed defects
  are dispositioned in `plans/round-97.md` § Inherited state.
  - defect 1 → correction C97-1 in `corpus/lessons/round-97.md` § Corrections;
  - defect 2 → C2;
  - defect 3 → C1;
  - defect 4 → v5 rule 7 (not claimed);
  - defects 5 and 6 → carried or bounded;
  - defect 7 → orchestrator-side.
- **Freeze `148395bf`** (`plans/round-97.md`):
  - v5 counter `verifiers/fixtures/round-97/selftest-kills.py` (sha256 `b4200c52…`). It adds rules 4–6:
    per-run fresh clone, TMPDIR, HOME and XDG_CACHE_HOME; a mirror run with the mutant bytes on disk;
    and an honest bracket of shuffled runs with a printed seed.
  - C2 runner `forgery-controls.py` (sha256 `28fbdb9f…`);
  - pre-data receipts under `.ufo/waves/round-97/receipts/`;
  - a pre-freeze marker-confound amendment, recorded in `receipts/predraft/`.
- **Wave `r97-w1`** (seat reports in `.ufo/waves/round-97/w1/*.md`):
  - ExecArmsR97 added 27 behavioural arms (78 → 105 assertions).
  - ScribeCorpusR97 added S273/S274 and the lesson draft.
  - ReviewerArmsR97 and ReviewerCounterV5 found nothing blocking.
  - CriticClaimR97 judged C1 MET and C2 MET on its predicate, with D1/D2 bounding it.
  - SentinelScopeR97 passed on scope and production identity.
  - ExecForgeryV5 built g9–g12. g10 and g11 read MET under v5.
  - MutTesterCounterV5 ran 9 counter-rule mutants; C2 kills 2 of them.
  - MutTesterDispatchR97 ran 15 new mutants; 11 survive.
  - ConnectorOverlapR97 ran the overlap scan and the planning data-walk (floor slack, sibling instances).
  - ScoutSourcesR97 re-opened S273 byte-identically and found S274.
- **Integration** (`plans/round-97-addendum-1.md` A1–A5, post-data disclosures; nothing frozen changed):
  - A1: the g10 committed-reference forgery reads MET under v5. It is now a named bound in
    `corpus/QUALITY.md` Q87.
  - A2: the g11 seeded-replay forgery reads MET when `KOTOBA_R97_SEED` is set. The landing readings
    are unseeded.
  - A3: counter-rule mutants V4–V9 survive C2's worlds.
  - A4: 11 new dispatch-checker survivors.
  - A5: t10 behaves differently under root, t09's framing overstates one of the 13, an uncaught
    exception exits with a traceback, and the assertion floor is 56 against 105 observed.
- **Planner seat:** held by me as L1, because the validator rejects `planner`. The planning data-walk
  rode ConnectorOverlapR97 Part 3.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/*`
  (orchestrator-owned) and `w4lines.txt`. The latter has mtime 2026-11-05 16:57, before this round,
  and no kotoba content, so I left it. No misroot.
- **Scratch:** `/fast/scratch/hyaku/kotoba-r97` was removed after landing; the landing runner also
  removes its own dir.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `7c01b10d54fbdcd97dd9ba06fe0954828e8a880f`, `94a1021762a888d8a360ba6efa759372cef392fb` | instruments (earlier attempt): v5 counter, C2 runner, marker fix before the freeze | § Round 97, "Claims as frozen" |
| `148395bf42af97436b1b832a97a175515f981939` | freeze (earlier attempt): plan, pre-data receipts | § Round 97, "Pre-data controls" |
| `693be9c321c26078a2adbf32c220dfcd371cbe35` | landing: verifier self-test arms (+231 lines inside `self_test()`); S273–S276; Q87; README row; `corpus/lessons/round-97.md` | § Round 97, "Inherited state", "Landing" |
| `38361a2513dabe6e01a1d63a5abde89e7b521271` | record: lesson settlement, Q87 committed-reference bound, addendum 1, LOG, SCORECARD, landing receipts and runner | § Round 97, "No-harm at landing", "Integration", "Frontier step" |
| `1d44bd820cf4ec53a37baba2b45f6da7776a84bd` | wave evidence: spec, dispatch, ready, results, 11 seat outputs, generator | § Round 97, "Wave" |

The last three commits each printed `landed <hash>` from `jj-lane.sh`. `jj-lane.sh state` shows
`local=remote=1d44bd82… ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

**C1**, counting command `python3 -B verifiers/fixtures/round-97/selftest-kills.py c1 <rev>`:

- Before, at base `fa1bebae` (`receipts/redbefore-c1-base.txt`): `C1 targets killed 0 of 13`, giving
  `C1-PREDICATE-UNMET` rc 1. This is the do-nothing control; `--rules v4` gives the same.
- After, at landing `693be9c321c26078a2adbf32c220dfcd371cbe35` (`receipts/landing/c1-v5.txt`):
  `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`
  → `C1-PREDICATE-MET` rc 0.
  - Under `--rules v4` the tally is the same (`c1-rulesv4.txt`), so C1 does not depend on C2's
    hardening.
  - Self-test went from `0 failure(s) over 78 assertions` to `0 failure(s) over 105 assertions`.
- Kill-rule conjuncts at landing:
  - v5 `r96c1` and `r95c1` MET;
  - `--box-proof` gives `boxes proven 2`;
  - production code is byte-identical outside `self_test()` (`prod-identity.txt`: one hunk,
    `1102a1103,1333`).

**C2**, counting command `python3 -B verifiers/fixtures/round-97/forgery-controls.py v5 <rev>`:

- Before, with the v4 counter (`receipts/c2-before-v4.txt`):
  `forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`, giving UNMET rc 1.
- Cause control (`receipts/c2-v5-as-v4.txt`): v5 run with `--rules v4` refuses 0 of 3.
- After, at landing `693be9c3` (`receipts/landing/c2-v5.txt`):
  `C2 v5: forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET` → `C2-PREDICATE-MET` rc 0.
  The counter and runner bytes equal the instrument commit.
- **Disclosed bound (A1/A2):** this does not show that v5 refuses no-arm forgeries in general. g10
  (committed reference) and g11 (seeded replay) read MET. The reviewer source check remains the guard
  for those classes.

**No-harm at landing** (`receipts/landing/`, runner `.ufo/waves/round-97/landing-run.sh`):

- round-96 counter `c1`/`r95c1` MET;
- round-95 `c1`/`r94c1` MET;
- round-93 `c1-killpin-rev.sh` MET;
- round-92 `controls-run.sh`: `shortcuts refused 2 of 2; honest held 2 of 2`;
- live dispatch run gives identical verdict lines with base and landing bytes (`dp-live-equal.txt`
  rc 0): `dispatch.04` 1195 PASS / 6 FAIL / 22 N/A, `dispatch.08` 1176 / 10 / 29;
- gate registry `74 of 74 … phantom 0`;
- floors self-test `0 failure(s) over 176 assertions`;
- tip battery `guards 5 of 5; tip battery exit 0: 3 of 6`. The three reds are the same ones as at the
  round-96 landing: `verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`;
- SKILL.md unchanged (`skill-identity.txt` rc 0).

## Sources & frontier

- **Census** with `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`:
  - round start: rc 0 (`receipts/census-before.txt`, 34 `W04`);
  - round end: rc 0 (`receipts/landing/census.txt` at the landing; re-run again after the last commit, rc 0), last line
    `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, 34 `W04` (none new).
- **Rows** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): 198 → 202.
  - Added, tier A admitted: S273, Bazel "Test encyclopedia" § Test interaction with the filesystem
    (grounds rule 4); S274, GoogleTest "Advanced" § Shuffling the Tests (grounds rule 6).
  - Added, tier A rejected: S275, pytest `tmp_path` (redundant corroboration); S276, pathlib
    `is_dir` (deferred). Both carry a flip condition.
  - All four were opened 2026-11-06, with access record and located quote in
    `corpus/lessons/round-97.md` § Gate.
  - Rows touched old→new: none (append-only).
- **Sourced claim:** C2 cites S273 and S274 (plan § C2 "Sourced", lesson § Gate).
- **Mined mistake:** `shared-state-between-scored-runs` (`corpus/lessons/round-97.md` § Mistakes).
  - captured-by: none;
  - fix: v5 rules 4–6 plus criterion Q87;
  - shown able to fail: with the fix switched off (v5-as-v4) the counter refuses 0 of 3.
- **Correction** C97-1: the round-96 receipt's S272 word count, 19 recorded vs 22 measured.
- **Assimilation:** none; this round takes no `merge/kotoba/` theme. `considerthese/2026-10-26.md` was
  re-read and no proposal implemented (lesson § Considerthese).
- **Wave evidence bytes (Q82):** `du -sb .ufo/waves/round-97` gives 1505669, against 1941368 in
  round 96. Source HTML was stored as digest plus excerpt, per closure defect 6.

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted. S273/S274 are registry rows cited by
  the plan and the lesson.
- **quality: improved.** The province instrument's self-test kills 13 behaviours it missed (0 → 13 at
  `693be9c3`), and the kill counter refuses three forgery classes it accepted (0 → 3 of 3). Production
  code is byte-identical and every no-harm reading held.
- **discernment: improved.** Two sources were admitted and two rejected on stated reasons. Two new
  forgery classes (g10, g11) were disclosed and named in Q87 instead of being claimed away. The
  round-96 word-count defect was corrected append-only.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SHONEN.md:5`; boxes `dispatch.04`/`dispatch.08` now carry a self-test that kills 13 more frozen mutants (`.ufo/waves/round-97/receipts/landing/c1-v5.txt`); SKILL.md unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence `LOG.md` § Round 97 (freeze → wave → landing → no-harm, lane-run; no non-author credit claimed).
- [~] Instructions executable by an agent without oral context — evidence `corpus/lessons/round-8-aggregator-box3-coldrun.md`; untouched this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `PROVINCE.md` § Adjacent; unchanged this round. ConnectorOverlapR97 Part 2 found the shared-run-state class in sibling wave harnesses (tsukuroi, revenger, mado); I reported it and edited no sibling (`.ufo/waves/round-97/w1/ConnectorOverlapR97.md`).

## Extras

- **Round shape:** one v1 wave `r97-w1`, 11 seats: executor 2, scout 1, scribe 1, connector 1,
  reviewer 2, mutation-tester 2, critic 1, sentinel 1. Attack seats are 5 of 11 (45 %). The earlier
  attempt dispatched it at 01:08 and it settled by 01:43. No residual call; round total 11. Dead seats:
  0 (all 11 returned final output).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (by me or any seat, per their reports).
- **Open L0 questions:** none new. considerthese proposal 2 stays L0-routed as before.
