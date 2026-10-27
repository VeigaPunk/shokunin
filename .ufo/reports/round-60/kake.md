# kake — round 60 report (attempt 2, run-10)

Lane repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (jj-colocated, branch `master`).
Base `97cdc122379711c2b02a8970752c8782da3ac81d`; lane tip `437f53b1f6cd22dbf307f1187f41d1c0850a1ac2`
(pushed, `ls-remote origin refs/heads/master` verified ahead=0 behind=0). Measured revisions: T0
`8001f8d5579303ff390305f9dcddb785834f2084` (attempt 1), T1 `9f671056c6fb5ca49bc62ed4210745f620ed4cae`
(attempt 2 integration commit). Contract `.ufo/waves/round-60/contract.md`/`contract.json` (`b3b9e29`,
before any seat ran).

## Work performed

Declared claims (contract v1, frozen before any data; three distinct axes; C1 works the lowest-scoring
non-retired axis, calibration at score 2):

1. **C1 — calibration**: the SKILL.md gate-registry status labels of the 28 round 48–59 counters match
   their observed exits (re-derive every label from runs; 12 rows added, three relabels).
2. **C2 — operability (capability acquisition)**: new tool `scripts/append_guard.py` — an append-only
   correction guard for knowledge files — passes 24 frozen cases (closes routed defect R59-D1).
3. **C3 — freshness (sourced: S427, S428, S429 opened this round)**: the S425 scope overstatement
   superseded on a re-opened page and the robots.txt posture of Google user-triggered fetchers
   re-verified on a later, category-specific page.

Attempt 1 was stopped by the run-9 operator wrap-up (~04:49 -03), not a lane fault; its in-flight state
was committed (`592c2ae`). This attempt inherited it, read `git log` and the wave dir first, integrated
the settled wave-2 reports and landed the round. No wave was rewritten; no new wave was launched.

- Wave-2 integration (34 settled reports, `.ufo/waves/round-60/w2/`; 4 dead seats recorded): fixed the
  C1 counter's fence-closer rule, never-met overlap classes, timeout and exception verdicts (v3,
  `c60_gate_status.py`); added the three guard selftest cases; fixed the c53 verdict map and completed
  the crawler-identity Kind-cell disclosure in `SKILL.md`; fixed the six location-description findings
  in `corpus/knowledge/robots-txt-limits.md`; recorded the C1↔C3 causal coupling as a stated limit;
  mined four mistakes into the lesson; added four QUALITY criteria; removed a stray `__pycache__`.
  Evidence: commits `9f671056`, `437f53b1`; contract § Counter versions version 3; lesson
  `corpus/lessons/round-60.md` § Attempt 2.
- Assimilation (attempt 1, this round's frontier step): one theme from `merge/kake/` — robots.txt
  posture and limits per Google crawler category; one entry admitted (`corpus/knowledge/robots-txt-limits.md`,
  staged S415 renumbered by document to S429, re-grounded on the retained S429 body); one staged entry
  refused with a flip (`common-crawlers-japanese.md`, 60-CJK-unit quote); quarantine slice (12 rows)
  hand-checked, held — the round-58 L0 question is unanswered, nothing appended.
- Considerthese: `considerthese/2026-10-26.md` proposal 5 (historical-gate list) implemented as claim C1
  (derived, not hand-kept). Proposals 1, 2, 4 not taken (reasons in the lesson).
- Frontier curation: rows S427–S429 opened, gated and registered; `corpus/README.md` coverage and
  frontier rows advanced (attempt-1 build commit `8b33fd2`).

## Landed changes

- `9f671056` (LOG.md §Round 60 attempt-2 bullet): wave-2 integration — C1 counter v3, guard selftest 54,
  SKILL.md c53 map + crawler-identity C5/C7 disclosure, six `robots-txt-limits.md` fixes, contract v3,
  QUALITY w2 criteria, lesson attempt-2 section, `w2-results.json`, `__pycache__` removed.
- `437f53b1` (LOG.md same bullet): T1 receipts — `controls/after-c{1,2,3}-*-t1.txt`,
  `c1-selftest-v3.txt` (84/84), `c2-tool-selftest-v3.txt` (54/54), `c3-selftest-t1.txt` (140/140),
  `after-guard-real-lane-t1.txt` (`files=53 findings=0`), `census-after-t1.txt` (exit 0),
  SCORECARD/LOG T1 entries.
- Earlier round-60 chain (attempt 1, reused and re-verified): contract `b3b9e29`; counters v1 `1ea30590`;
  assimilation mirror/collision guard `81db050`; w2 spec/dispatch `45f46fb`; build `8b33fd2`; wave-2 fixes
  `8001f8d5`; T0 measurement `7c0d9b0`; wrap-up state `592c2ae`. Every change ties to a LOG.md round-60
  bullet.

## Before → after measurements

Counting commands are the frozen counters (contract § Claims; predicates unchanged across v1→v3).

- **C1** — `python3 -B .ufo/waves/round-60/c60_gate_status.py --root . --revision <rev> --jobs 6`:
  base `97cdc122` → `members=28 mismatches=14 scores_held=3/3 met=False` (exit 1,
  `controls/base-c1-gate-status.txt`); T1 `9f671056` → `members=28 mismatches=0 scores_held=3/3
  met=True` (exit 0, `controls/after-c1-gate-status-t1.txt`); T0 `8001f8d5` identical result
  (`controls/after-c1-gate-status.txt`). **met.** Selftest 84/84 (`controls/c1-selftest-v3.txt`);
  `scores_held` shown able to fail by the score-only mutant (`controls/redbefore-c1-score-mutant.txt`).
- **C2** — `python3 -B .ufo/waves/round-60/c60_guard_cases.py --root . --revision <rev> --seed 60`:
  base (no tool) → `0/24` exit 1 (`controls/base-c2-guard-cases.txt`); T1 → `24/24 met=True` exit 0
  (`controls/after-c2-guard-cases-t1.txt`; T0 `8001f8d5` same). **met.** Tool selftest 54/54; real-lane
  run `python3 -B scripts/append_guard.py --root . --base fd6303ce… --revision 9f671056` →
  `files=53 findings=0` exit 0 (`controls/after-guard-real-lane-t1.txt`); c55 byte-prefix port control
  7/24 (`controls/c2-selftest.txt`).
- **C3** — `python3 -B .ufo/waves/round-60/c60_quote_truth.py --root . --revision <rev>`:
  base → `0/9` exit 1, registry 164 rows (`controls/base-c3-quote-truth.txt`); T1 → `9/9 met=True`
  exit 0, registry 167 rows (`controls/after-c3-quote-truth-t1.txt`; T0 same). **met** (sourced: S427,
  S428, S429, Gate block in `corpus/lessons/round-60.md`). Selftest 140/140
  (`controls/c3-selftest-t1.txt`).

Admission notes (reported for the operator to rule): (a) `w2/ConnW2Cross` revert tests show C1's
after-state cannot hold on a tree without C3's rows — the claims are independently falsifiable by their
own frozen counters at one measured revision but are not isolation-separable at the build; mechanism
recorded in contract § version 3 and the lesson. (b) The C3 predicate is quote truth, not semantic
support (contract limit; `w2/CriticC3CheatV1` reviewer-checked the correction's qualified wording).
No axis harmed: all three counters still pass at T1 with the registry, entries and tools changed only
toward the claims.

## Sources & frontier

Command (frozen): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kake`.

- Before (round start, `controls/census-before.txt`): exit 0, 164 rows, 14 W04. After (round end,
  `controls/census-after-t1.txt`): exit 0, 167 rows, 15 W04 — the new warning is S427 sharing S425's
  URL across scopes by supersession, expected and recorded. Both exits pasted from the validator output
  (`kake ok /home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md` final line each).
- Rows added this round: 3, all tier A, status `mined` — S427 (lane re-open of the S425 URL, supersedes
  S425 by scope), S428 (lane-found from the S426 category table), S429 (assimilated from staged S415,
  renumbered by document). No existing row's status/recheck/used-by changed (pure addition).
- Rows touched old→new: none (S425 unchanged, superseded-not-edited; recorded in the lesson's erratum).
- Frontier rows advanced: `corpus/README.md` coverage rows 79–80 and frontier row 116 list the two new
  entries (`google-user-triggered-fetchers.md` → S428, `robots-txt-limits.md` → S429).
- Assimilation: one theme, one admit (`robots-txt-limits.md`), one refuse-with-flip
  (`common-crawlers-japanese.md`); quarantine slice 12 rows hand-checked and held (round-58 L0
  unanswered). Considerthese: proposal 5 taken (claim C1).

## Trend verdicts

- **expansion — improved.** Two knowledge entries on ground the coverage map did not hold (Google
  user-triggered fetchers and their robots.txt posture, S428; the limits Google states for robots.txt
  itself, S429) plus a new lane capability (the append guard); registry 164 → 167. Evidence:
  `corpus/README.md` rows 79–80/116; SCORECARD capability row (`append_guard.py` at `8001f8d5` line).
- **quality — improved.** The S425 scope overstatement superseded on a re-opened page; the user-triggered
  posture re-verified against a later page and the unqualified sentence corrected append-only; 12
  unregistered counters registered and three wrong labels re-derived from runs; six quote-location
  attribution defects fixed in the S429 entry; C1 counter parsing tightened twice (v2/v3) from wave
  attacks. Evidence: `controls/after-*-t1.txt`; `w2/ReviewerEntryRL.md` vs the fixed entry;
  `corpus/lessons/round-60.md` §Mistakes.
- **discernment — improved.** 15 staged items refused with page counts; one staged entry rejected with a
  flip; three quarantine rows re-checked and held; four new mistakes mined with captures and fixes;
  honest stated limits recorded (causal coupling, semantic-support boundary, carried counter fixtures).
  Evidence: `corpus/lessons/round-60.md` §Gate/§Mistakes/§Attempt 2; contract §Stated limits and
  §version 3.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round-60
  gate-status ledger and 12 registry rows added (`SKILL.md:1311-1358`, build `8b33fd2`); verifier: the
  non-author closure spot-check.
- [~] At least one end-to-end domain task executed and logged — all 28 gate counters re-derived from
  runs at T1 (`LOG.md` §Round 60; `controls/after-c1-gate-status-t1.txt`).
- [~] Instructions executable by an agent without oral context — the three counters and the guard carry
  committed selftests with receipts (`controls/c1-selftest-v3.txt` 84/84, `c2-tool-selftest-v3.txt`
  54/54, `c3-selftest-t1.txt` 140/140).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — both new entries and all three rows are web
  properties (robots.txt, crawler posture); per-entry PROVINCE scope check recorded in the lesson §Gate.

## Round shape and extras

- Shape: two v1 waves, no residual. **w1 build** 44 seats (executor 17, scribe 9, critic 7, scout 4,
  reviewer 4, connector 2, revenger 1), validated under policy v1, dispatched `b3b9e29` chain, results
  44/44 settled. **w2 falsify** 38 attack seats on build `8b33fd24` (reviewer 17, critic 10,
  mutation-tester 4, sentinel 3, scout 3, connector 1), dispatched `45f46fb`; seats died at the run-9
  wrap-up, the run-10 orchestrator settled the wave (`w2-results.json`): 34/34 report files present,
  **4 dead seats: MutC2Counter, ReviewerC2Rerun, CriticNoHarm, CriticAxisV2** (no report, no output —
  recorded, not respawned). Round total **82 seats** (band 64–128, ceiling 256). Attack share: w2 is
  100% attack; across the round 34/82. The §3 L2 floor and role split were met inside w1/w2; the L1 holds
  the planner seat (validator-frozen topology); routing followed the run-10 host route table, no model
  passed.
- Every wave `context` carried the tooling-authorization and pacman-guard sentences; no tools installed
  or upgraded this attempt (none in w1/w2 either); pacman untouched.
- Misroot sweep before the report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` clean — no
  fleet-root strays from kake round 60 (other lanes' quarantined strays under `.tower/` left untouched);
  the one in-lane hygiene stray (`__pycache__`) removed and mined as a mistake.
- Dead-seat accounting is file-based (report files in `w2/`), not parser-bound, per the run-9 lesson.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions (routed around, not treated as answered): the round-58 quarantine-hold question
  (nothing appended from the slice); round-59 rows on calibration ownership and CJK quote units.
