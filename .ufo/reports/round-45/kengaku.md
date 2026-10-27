# kengaku — round 45 report (hyaku run 9, attempt 3, 2026-10-27)

L1 `KengakuR45a3` (canonical planner seat; attempt 3 and last). Attempt 1 died on an invalid_prompt policy refusal
(no wave, report or commit; `.ufo/watchdog.log:1618`); attempt 2's L1 `KengakuR45-2` and its 39 wave-2 seats died in
the orchestrator session exit at 2026-10-26 23:57:36 -03 (`.ufo/watchdog.log:1629`); the orchestrator salvaged its
tree as lane commit `fbad1c5`. Lane tip (landed, `git ls-remote origin refs/heads/master`): `3d9ea54a558b40993dba251474535edbf33afa21`. This report replaces attempt 2's uncommitted draft, which said both claims landed
before wave 2 had been read; its verdicts are withdrawn below.

## Work performed

Declared claims (frozen `plans/round-45-claims.md`, freeze `b4fcd35` + pre-data amendments `9271dda`):
**C1 — calibration** (the advertised fixture fence vs the observed one, `plans/fixture_fence.py`) and
**C2 — coverage**, the lowest non-retired axis (tied with novelty; frozen tie-break) — the pinned TB2
`password-recovery` grader as the second F1 constant-compare exemplar.

- Inheritance re-verified (attempt 3): both frozen counters re-run in the envelope on a `--no-local` clone of `fbad1c5`
  — `PREDICATE C1 pass` (`kengaku-shokunin/.ufo/waves/round-45/integrate/a3-tip-c1.txt`) and `checks=11 defects=0`,
  `PREDICATE C2 pass` (`integrate/a3-tip-c2.txt`); `sha256sum -c .ufo/waves/round-45/claims/frozen-digests.txt` →
  18/18 OK; no-harm set re-run (`integrate/a3-noharm.txt`: r44 C1 pass, r44 C2 `checks=11 defects=0`, anchor
  `rows=149 tokens=55 defects=0`, `routed_open=24 oldest_round=39`, `ROUND-CLOSE RESULT PASS`), the same values as
  `w2/R45ExecNoHarm.md`.
- Keyed do-nothing control for C1 (attempt 3, before any verdict): `.ufo/waves/round-45/claims/fences/keyed_name.py`
  inspects nothing and refuses iff `/refusals45-` is in the fixture path; the frozen counter prints
  `REFUSALS total=10 clean=10`, `HONEST fixtures=104 admitted=104`, `CALIBRATION advertised=10 contradicted=0`,
  `PREDICATE C1 pass`, exit 0 (`claims/control-c1-fence-keyed_name.txt`). Name-blinded dev counter
  (`claims/dev_blind_c1_verify.py`, 3-line diff `dev-blind-c1.diff`, not the frozen predicate): keyed fence
  `contradicted=10`, exit 1 (`dev-blind-c1-keyed.txt`); landed fence `contradicted=0`, exit 0 (`dev-blind-c1-landed.txt`).
- Wave `a3w1` (34 seats, the killed wave-2 items re-dispatched unchanged plus an attempt-3 context note;
  `.ufo/waves/round-45/a3w1-dispatch.json`, validated under policy v1, spec renderer `make_a3w1_spec.py`):
  held-out hostile modules vs the landed fence — 8 of 10 modules admitted (`a3w1/R45HoIncludeIf.md` 3/3 with 12 outside
  reads, `R45HoSymlinks.md` `.git/objects` symlink out `ADMIT opens=8`, `R45HoArgvEnv.md` NUL argv → uncaught
  `ValueError` = admitted, `R45HoCommondir2.md` 2/4), `R45HoConfigKeys.md` `core.attributesFile` outside `d` admitted (git honours it); corroborated by `R45CritLandedFence.md` and
  `R45CritIntent.md` (no fixture-name keying in the fence; brace-prefix bypass for non-lane path options); fence
  mutation 7/15 caught (`R45MutLandedFence.md`).
- C2 attacks (`a3w1`): `R45RevRowCells.md` 13 cell defects (S152/S153/S154 anchors cite a line without the quote;
  ranges overshoot files; word counts; `kind`); `R45RevEntryQuotes.md` 19/19 located quotes and 16/16 mechanism quotes
  verbatim, but the entry's `## Predictor` disagrees with the captured grader on 3 of 9 lone-CR states;
  `R45CritV11Bypass.md` 4 lint-clean lookup predictors pass V11; `R45SentC2Grader.md` F1 gate P10 fetches
  `biopython==1.85` via `uv` outside the sandbox when host python lacks `Bio`, F2/F3 P9 fails on wave evidence at the
  live tip and ignores modified tracked files; `R45CritReceipt.md` receipt re-run mismatches 0, hand-check 3/3;
  `R45CritDryVsObserved.md` 0 mismatches; `R45CritCaseFidelity.md` 3 recipe-description defects, 0 label-changing;
  `R45CritFrozenDigest.md` digest drift 0; `R45ExecTipRerun.md` tip C1 pass, C2 pass; `R45MutC2Checks` and `R45MutC1Instrument2` died reportless (below), so the C2-check and C1-instrument mutation items are unattacked.
- Self-assessment corrections landed (each with the command that refutes the old text): SCORECARD cited the claims
  file's sha256 `cb2fae38` as a commit (`git cat-file -t cb2fae38` → fatal); "byte-equal" A/B C2 receipts
  (`cmp` → differ, line 1; equal on non-`ENVELOPE` lines); a receiptless `untracked=2/14` lesson sentence (replaced by
  `a3w1/R45SentC2Grader/c2-verify.txt:12` `P9 DEFECT untracked=30`); lesson Gate rejects without flip conditions
  (`R45RevLesson.md` finding 1); round titles "fence closed / 10/10 hostile classes refused" (`R45CritC1Overclaim.md`);
  orphaned `### Planned (round 45)` heading moved back under round 44 (`R45RevScorecard.md` finding 1).
- New QUALITY criterion Q39 (`kengaku-shokunin/corpus/QUALITY.md`, section "Round45 criterion"): a fence counter hides
  every name it chose from the procedure under test and freezes a name-keyed control that must fail — shown able to
  fail by the keyed/blinded pair above.
- Planner seat: held by the L1 (validator rejects `planner`); the round-46 data walk rode scout `R45PlanNext` (w1).

## Landed changes

- `f660ae04a1c54d859ae2ba53665ac3c2dd04c069` — attempt 3: keyed control + blinded dev counter + receipts, tip
  re-measure, no-harm, a3w1 dispatch, Q39, lesson §Attempt 3 + corrections, SCORECARD round-45 verdicts rewritten,
  LOG.md `### Round 45 attempt 3`, README lesson row.
- `3d9ea54a558b40993dba251474535edbf33afa21` — a3w1 seat reports and receipts, results record, final lesson/SCORECARD/LOG sync (LOG.md
  `### Round 45 attempt 3`).
- Inherited, re-verified and kept (LOG.md `## Round 45` entry): `b4fcd35` freeze, `52d7486`, `05b02e2` first probe
  run, `7d062c0` C2 package, `9271dda` freeze amendments, `6decc71` C2 receipts, `8f9a898` C1 fence (variant A),
  `0ac30a1`, `4290d64`, `d4c0cdf`, `a448a47` (w1 reports and results).
- Inherited, kept as a record and NOT cited as evidence: salvage commit `fbad1c5` (`w2-results.json`, killed seats'
  partial files `w2/R45HoCommondir2/h2_gitfile.py`, `w2/R45MutC1Instrument2/receipts/*`, one line in
  `w2/R45ExecNoHarm.md` whose numbers attempt 3 re-measured). Discarded: the attempt-2 report draft (rewritten here).

## Before → after measurements

- **C1** — `python3 plans/round45_c1_verify.py --lane <clean clone> --work <scratch>` (envelope). Before:
  `claims/control-c1-nothing.txt` `PREDICATE C1 fail`; r44 fence `claims/control-c1-fence-r44.txt`
  `REFUSALS total=10 clean=3 leaked=3 read=4`, `contradicted=7`, fail. After, measured at `8f9a898`
  (`integrate/measure-final.txt`) and at `fbad1c5` (`integrate/a3-tip-c1.txt`): `PINS total=33 mismatched=0`,
  `REFUSALS total=10 clean=10 leaked=0 read=0 hung=0 build_errors=0`, `HONEST fixtures=104 admitted=104 refused=0`,
  `CALIBRATION advertised=10 contradicted=0`, `PREDICATE C1 pass`. Control at `fbad1c5`: keyed fence → the same
  `PREDICATE C1 pass`. **Verdict: not admitted — unprovable on its frozen counter** (a do-nothing control reaches the
  target; 8 of 10 held-out modules admitted). Calibration score unchanged (8).
- **C2** — `python3 plans/round45_c2_verify.py --lane <clean clone> --work <scratch>` (envelope). Before:
  `claims/control-c2-nothing.txt` `checks=11 defects=8`, `PREDICATE C2 fail`, exit 1. After at `8f9a898`
  (`integrate/measure-final.txt`) and `fbad1c5` (`integrate/a3-tip-c2.txt`): `checks=11 defects=0`, `PREDICATE C2
  pass`, exit 0; probe `cases=16 observed_pass=5 observed_fail=11 mismatches=0`, `regrade cases=16 differ=0`, V11
  `states=48 grader_pass=18 grader_fail=30 disagree=0`. **Verdict: predicate met; admission for the closure to rule**
  — four routed package defects the counter does not check (row anchors S152–S154, predictor lone-CR divergence, V11
  lookup bypasses, P10 unpinned fetch). Coverage stays capped at 7 (L0 `kengaku | round-33`).
- No-harm: `integrate/a3-noharm.txt` at `fbad1c5` — every measured line equal to the attempt-2 baseline
  (`w2/R45ExecNoHarm.md`) except the expected +8 anchor rows/tokens.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
  Round start (`.ufo/waves/round-45/claims/census-before.txt`): 15 `W04`, `kengaku ok`, exit 0. Round end (attempt 3, 2026-10-27 01:11 -03, `kengaku-shokunin/.ufo/waves/round-45/integrate/a3-census-after.txt`):
  15 `W04` (same ids), `kengaku ok`, exit 0.
- Rows: 141 → 149 (`grep -cE '^ {0,3}\| *S[0-9]{3}' corpus/SOURCES.md`); added S149–S156, tier A 8, B 0, C 0; rows
  touched in place: none; refused: `gitignore` capture and the runtime seed image (lesson Gate, flips added attempt 3).
- Sourced claim: C2's entry `corpus/knowledge/tb2-password-recovery-grader.md` cites S149–S156, opened 2026-10-26 at
  pin `2fd12b88`; re-opened in attempt 3 by `a3w1/R45RevRowCells.md` (HTTP 200, sha256 = registry for all 8).
- Frontier advanced: `corpus/README.md` §Frontier TB2 sub-bullet narrowed to 11 of 89.
- Mistake mined: `corpus/lessons/round-45.md` §Mistakes (6 rows) + §Attempt 3 Mistakes (4 rows: keyed control, claim
  booked over a verdict-changing finding, receiptless numerals, mislocated anchors).
- Assimilation: none (claims frozen before re-grounding; `w1/R45MergeRescreen.md` 73 collisions, quarantine slice 2
  rows; `w2/R45CritAssimilation.md` S091 quote absent → refuse). considerthese: `2026-10-26.md` proposal 2 mined by
  `w1/R45Considerthese.md`, not landed, carried to round 46.

## Trend verdicts

- `expansion`: **improved** — one knowledge entry and 8 tier-A rows on ground the lane did not hold (51→52 files,
  141→149 rows), predicate C2 met against a failing do-nothing control.
- `quality`: **harmed** — the round landed three row anchors citing the wrong line and an entry predictor that diverges
  from its grader on lone-CR states (`a3w1/R45RevRowCells.md`, `R45RevEntryQuotes.md`); routed, not repaired in-round
  (rows are immutable under Q34; the frozen spec pins them).
- `discernment`: **improved** — the round's own falsifiers withdrew the C1 claim before filing (keyed control,
  held-out modules) and four self-assessment overclaims were corrected with refuting commands; Q39 is shown able to
  fail.

## Round shape and seats

Two v1 waves plus a re-dispatch, policy `scripts/hyaku/ufo-wave-policy.json` (band 32–64 each). Total dispatched
112 (64–128 band): **w1** 39 (attempt 2; executor 11, reviewer 7, scribe 5, scout 5, critic 3, mutation-tester 2,
sentinel 2, connector 2, revenger 1, simplifier 1), all 39 settled, 2 reportless (`R45CriticC2Instrument`,
`R45MutV11States`, recovered from results); **w2** 39 (attempt 2; mutation-tester 10, critic 11, reviewer 9, executor 5,
sentinel 2, simplifier 1, connector 1) — 34 killed at the session exit with no output (last error: "still running at
the session exit and killed - no output delivered"), 5 settled; **a3w1** 34 (attempt 3; mutation-tester 10, critic 10,
reviewer 8, executor 2, sentinel 2, simplifier 1, connector 1) — 34 settled, 32 report files; 2 dead with no report (`R45MutC1Instrument2`, `R45MutC2Checks`; last error text: "orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator session but not retained"). Reused from earlier attempts: 44 seats (w1 39 + w2 5);
new this attempt: 34. No residual call. Attack share a3w1 28/34.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1; no a3w1 report records an install. `a3w1/R45SentSeatAudit.md` H3: an
  `OpenBot-0.51.1-x86_64.AppImage` appeared in `~/.local/bin` at 2026-10-26 23:36:46 with no round-45 seat recording it
  (owner unknown; every envelope bracket stayed `unchanged` within its run).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only this report (`?? .ufo/reports/round-45/kengaku.md`)
  and `?? .ufo/reports/round-48/mado.md` (another lane's) — no kengaku seat misroot.
- Round-44 spot-check routed defects: `R44SentinelFences` V1–V3 and `R44LabratLaneInclude` became frozen refusals f7–f10
  (r44 fence fails them, `contradicted=7`); `R44CritV11` → V11 lint + `Random(45)` landed but is bypassed
  (`R45CritV11Bypass`) — carried.
- Open L0 question: `kengaku | round-33` (coverage cap). No new question.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `kengaku-shokunin/SKILL.md` (unchanged this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `kengaku-shokunin/LOG.md:7`; this round's executed probe `corpus/evidence/round45/password-recovery-probe.txt`
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:129`; `a3w1/R45RevProvince.md` `province-defects-0`
