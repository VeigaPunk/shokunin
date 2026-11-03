# souji round 57 — the inline-comment class (v6) and the receipt revision-binding gate

Lane: souji (`/home/vgpnk/Projects/shokunin/souji-shokunin`), branch `master`, final lane hash
`dcbcd05c467508f00a04f35bf544d0d83f745e73` (verified by `git ls-remote origin refs/heads/master`). Round 57, attempt 1.
Base `b4ef0bc84ada3fb3aefd6a0b1a841a6517b84acd` (the round-56 non-author verifier spot-check commit,
verdict ok / **rejected-harmed**). Freeze `d749f7ee081ec1b382b2f92577eb22bfba1c7761`.
Shape: one v1 wave, 12 seats; no residual call; round total 12.

## Work performed

Declared claims (frozen in `census/round-57/preregistration.txt` at the freeze commit):

1. **C1 — calibration 7** (the lowest non-retired axis): the correction-filing counter is amended to
   **v6**, adding the inline HTML-comment hidden class — a `<!--` on a visible line that does not start
   the line opens a comment ending at the first `-->` after it, including one on a later line — so the
   r56 harm shapes `B4-INLINE-NBSP-OPENER` and `C4-INLINE-CLOSED-COMMENT` are refused where v5 filed
   them, `F29` and the new `C6-INLINE-SAME-LINE` stay visible, the finding detail carries
   `hidden_by=fence|block|inline`, and the selftest asserts the FULL ordered finding list.
2. **C2 — operability 8** (capability acquisition): a new receipt revision-binding gate
   (`census/round-57/c2-counter.py`) plus a recorder (`census/round-57/record-receipt.sh`) — a receipt
   must name a durable full-40-hex `rev=`, an `EXIT=` line, and an `instrument_sha256=` equal to the
   named instrument's committed blob at that revision. This is the Q109 repair the r56 closure routed.

Items (each with its evidence pointer):

- Freeze before any post-freeze measurement: both counters, the 36-fixture builder, the expected TSVs,
  the recorder, the stub control, the before manifest, the pre-freeze matrices, the M1
  red-before/after pair, the three source captures and the preregistration —
  `census/round-57/preregistration.txt` pins; commit `d749f7ee`.
- C1 matrix, both arms over all 36 fixtures, official run byte-identical to the pre-freeze dry-run:
  `census/round-57/records/c1-matrix-v{5,6}.tsv`, `c1-matrix-run.txt` (`cmp -s` → SAME), target
  re-derivation in `c1-targets.txt`.
- C1 target details: B4/C4 hidden class receipt `c1-hidden-class.txt` (both findings carry
  `hidden_by=inline`); v6 selftest `records/c1-selftest.txt` (`SELFTEST pass cases=36`); real lane at
  the freeze `records/c1-tip.txt` (`unfiled=0 … fenced=0`, `rev=d749f7ee…`, EXIT=0).
- C1 kill-power: the r56 M1 mutant dies only under the all-findings assertion —
  `records/m1-red-before.txt` (first-finding-only arm `SELFTEST pass cases=36`, rc 0; frozen arm
  `SELFTEST fail cases=36`, rc 1 on `F24-PAIR-HIDDEN-FILING`).
- C2 before state: the r56 standing receipt carries no revision → `RECEIPT-REV-MISSING`
  (`records/c2-before.txt`, EXIT=1); the always-clean stub `controls/c2-stub.py` cannot satisfy that
  half; C2 selftest `records/c2-selftest.txt` (`SELFTEST pass cases=8`,
  `control=FALSE-GREEN-REJECTED`).
- C2 after state: the standing receipt re-produced by the recorder at the round's content revision
  (`records/standing.txt`), the gate verdict over the two earlier receipts (`records/c2-tip.txt`), and
  the final three-row manifest verdict (`manifests/after.tsv`, `records/c2-after.txt`,
  `SUMMARY receipts=3 findings=0`).
- Frontier step: S279 (WHATWG HTML §13.1.6), S280 (CommonMark 0.31.2 §6.6) admitted and S281 (MDN)
  rejected, each opened live this round with a committed capture and a verified ≤25-word located quote
  (`census/round-57/sources/`, `records/source-quotes.txt`); the knowledge entry
  `corpus/knowledge/inline-html-comment-visibility-r57.md`; QUALITY Q115/Q116; SKILL registry rows and
  the inline-comment error pattern; README `### Frontier (r57)`.
- Mistake mined: the frozen T3 parenthetical miscount (ERRATUM-R57-1), the partial-tree before-census
  receipt, and the standing-suite dirty-tree refusal — `corpus/lessons/round-57.md` `## Mistakes`.
- Wave: one validated v1 wave of 12 seats (`w1-spec.json`, `w1-dispatch.json`, counts spawn 12 /
  resume 0; evidence committed under `census/round-57/wave/w1/`); attack roles 4/12 (33%), connector 1,
  three executors, the planner seat held by the L1.
- Fleet/root hygiene: misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no
  file a r57 seat wrote (the stray `after` file at the fleet root predates the wave, 20:05, and is not
  this lane's); the r56 `census/round-56/__pycache__` artifact was deleted (`git ls-files` prints
  nothing for it).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: v6 counter, receipt gate + recorder, 36-fixture builder, expected TSVs, stub control, before manifest, pre-freeze matrices, M1 pair, three source captures, preregistration | `Round 57` claim/freeze bullet | `d749f7ee081ec1b382b2f92577eb22bfba1c7761` |
| sources S279/S280 admitted, S281 rejected, knowledge entry, QUALITY Q115/Q116, SKILL registry + error pattern, README frontier | `Round 57` sources bullet | `805482129d022b13db672654f5478952def607a6` |
| round content: LOG round entry, SCORECARD round-57 measurements + capability row + r58 plan, lesson (Gate/mistakes/errata/limits/routes), sources S282/S283, README frontier, official matrices/selftests/target/probe receipts, wave evidence | `Round 57` measured/controls/routed bullets | `8d8f046377a9cf5c0d16092b4d190d3a71341b63` |
| SCORECARD evidence-pointer repairs — the standing suite flagged 8 then 4 unfiled declared-evidence pointers in the new rows; each is now a full lane-relative path | `Round 57` measured bullet (pointer repair note) | `bb11421122aca19a9215b7195297997b8b5ad4cb`, `44a983a3e72923d8e809100763a9fcd8c458a244` |
| evidence: standing receipt (green at `44a983a3`), C2 two-row and three-row manifest verdicts | `Round 57` C2 bullet | `9d61c0a83cc588d7b48717e7f9e9e07a0e8d4a0b` |
| close-out: LOG addendum + lesson note (standing-suite pointer repair 8→4→0, C2 after half) | `Round-57 addendum` | `dcbcd05c467508f00a04f35bf544d0d83f745e73` |

## Before → after measurements

| claim | axis | before | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 correction-filing counter v6 | calibration 7 | v5 arm: exit-0 count 10 of 36; B4 and C4 exit 0 (`-`) — parent-free hidden filings counted as filed | v6 arm: exit-0 count 8 of 36; B4 and C4 exit 1 with `CORRECTION-IN-FENCE,CORRECTION-IN-FENCE` and `hidden_by=inline`; C6/F29/F17/F18/F19 exit 0 under both; 34 rows identical | `awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-57/records/c1-matrix-v5.tsv census/round-57/records/c1-matrix-v6.tsv` → `10`, `8`; details `census/round-57/records/c1-targets.txt` | `d749f7ee081ec1b382b2f92577eb22bfba1c7761` |
| C2 receipt revision binding | operability 8 | over `manifests/before.tsv`: `FINDING RECEIPT-REV-MISSING census/round-56/records/landing-suite-final.txt`, `SUMMARY receipts=1 findings=1`, EXIT=1 | over `manifests/after.tsv`: `SUMMARY receipts=3 findings=0`, EXIT=0; each receipt carries `rev=<full40>`, a matching `instrument_sha256=` and an `EXIT=` line; the standing suite itself is green at that revision (`assertions=627 mismatches=76 registered=76 unfiled=0`, EXIT=0) | `python3 -B census/round-57/c2-counter.py --root . --manifest census/round-57/manifests/before.tsv` then `… --manifest census/round-57/manifests/after.tsv` | before `d749f7ee…` (`records/c2-before.txt`), after `44a983a3e72923d8e809100763a9fcd8c458a244` (`records/standing.txt`, `c2-tip.txt`, `c2-after.txt`) |

## Wave disposition

One v1 wave, 12 seats, **12/12 settled with output, no dead seat** (`w1-results.json`), attack roles
4/12 (33%), connector 1, three executors; seat reports and receipts are committed under
`census/round-57/wave/w1/` (three >1 MiB sentinel receipts excluded for size, disclosed in
`census/round-57/wave/README-excluded.txt`). Detailed dispositions are in
`corpus/lessons/round-57.md` `## Wave findings`:

- scout01 — pins 13/13 MATCH, fixture determinism, matrices byte-identical, C2 base state reproduced.
- connector01 — LANE-FIRST on the digest binding; no sibling owns the inline-span rule; no sibling
  file edited or executed.
- executor01 / executor02 — AGREE on C1 and C2 independently; the standing suite's dirty-tree refusal
  preserved as a refusal, never a pass.
- executor03 — M1/M2/M3 killed; **M4 and M5 SURVIVED** (closer-line hiding and `<!-->`/`<!--->`
  untested).
- mutation01 — 21 C2 mutants, 9 killed, **12 survived**; harness gaps G1–G8 (no `rc` assertion, id-only
  comparison, silently skipped expected rows, missing symlink/manifest/tag/token-boundary cases).
- reviewer01 — **ATTACK-FOUND (C1)**: HIGH second-opener-after-closer hidden filings (reproduced by the
  L1 in `records/probe-second-opener-harm.txt`), HIGH disclosed lazy-indent4, MEDIUM over-hide classes
  (code span, backslash escape, link destination, block `<!-->`/`<!--->`/`--!>`).
- reviewer02 — **ATTACK-FOUND (C2)**: MEDIUM annotated-tag-object acceptance vs the documented
  `RECEIPT-REV-ABSENT` contract, MEDIUM unconfined manifest paths (`../`/absolute), LOW duplicate-`rev=`
  precedence.
- critic01 — **C1 SURVIVE** on T1–T7 (before arm non-vacuous, change-undone control fails T1, render
  0/0/2/2, counts 10 vs 8, real lane exit 0), with the honest note that the claim's title overstates
  the frozen grammar; **C2 SURVIVE** on T1/T3/T5-before/T6 and its after half was uninstantiated at
  measurement time (it ran before this report's endgame produced `manifests/after.tsv`, `standing.txt`,
  `c2-tip.txt`, `c2-after.txt` — sequencing, not a defect).
- revenger01 — disposition of every r56 routed defect and named limit with receipts: R2/R3/R4 CLOSED
  (wave composition, the `__pycache__` artifact, the B4/C4 repair), R1/R5 **NARROWED** (recorder
  accepts a dirty tree and overwrites an existing OUT; the C2 selftest does not assert `rc`, compares
  ids only, and ignores a ghost expected row), R6 OPEN (all six r56 sentinel findings unchanged).
  New defects it proved: D1 second-opener under-hide, D2 code-span over-hide, **D3 tab-indented opener
  over-hide** (reproduced by the L1 in `records/probe-tab-indent-overhide.txt`), D4 recorder binds
  bytes-not-execution, D5 the r57 `.pyc` class recurring (removed at close), D6 the C2 selftest is not
  idempotent over an existing `--work`.
- scribe01 — AGREE: three sources re-fetched `cmp`-identical, four quotes verbatim inside their anchors
  with an independent normalizer, the 0/0/2/2 render reproduced, and the three draft rows parse on a
  scratch fleet root. Its two real findings on the committed registry were filed as superseding rows
  S282 (S279 misquoted double quotes) and S283 (S280's quote swallowed by a rendered table); it also
  corrected the S279 quote-2 word count to 19 (ERRATUM-R57-3).
- sentinel01 — write-scope/scratch proof AGREE (`strace` under `--work`, no hardcoded `/tmp`, FIFO and
  symlink receipts refused before `open`, pins intact); **ATTACK-FOUND**: HIGH **H1** — a backticked
  `` `<!--` `` opens a phantom span that suppresses an *unrelated* LOG/README overstatement
  (`log-codespan`: v6 `logunfiled=0` exit 0, v5 refuses), a v6 regression in the silent direction;
  MEDIUM raw control bytes in findings (M2) and a BEL after a correction's line number dropping it
  unjudged (M3, also v5); LOW 1 MiB-token output amplification (L4).

## Sources & frontier

- Counting command (before and after, both exit 0):
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  — before receipt `census/round-57/records/sources-census-before.txt` (202 rows, 61 W04,
  `--file` over a base snapshot that names every extracted path), after receipt
  `census/round-57/records/sources-census-after.txt` (207 rows, 62 W04, `souji ok`).
- Rows added by tier: A 4 (S279 WHATWG spec, S280 CommonMark spec, and their same-round superseding
  rows S282/S283 — S279's `teaches` cell misquoted the page's double quotes, S280's swallowed its own
  quote in a rendered table), B 1 (S281 MDN, rejected), C 0.
- Rows touched old→new: S279 `—`→`corpus/knowledge/inline-html-comment-visibility-r57.md`; S280 same;
  S281 `status=rejected`, `used-by=—`; S282/S283 `mined`, `used-by=corpus/lessons/round-57.md`. No
  existing row's immutable cell was rewritten; the four pre-existing r56 rows' `used-by` were not
  touched.
- Frontier rows advanced: the correction-filing visibility frontier now holds the inline class as
  knowledge (`corpus/knowledge/inline-html-comment-visibility-r57.md`, S279/S280) with the measured
  visibility table; README `### Frontier (r57)` records the next step (renderer-vs-authoring grammar,
  unmodelled block types).
- Assimilation: none — no `considerthese/` directory in this lane; the shokuknow `merge/souji/`
  package stays held by the open r46 L0 question on mass id drift.
- Discernment sample: one admit pair (S279/S280) and one reject (S281) are on record; the non-author
  closure decides whether it agrees.

## Trend verdicts

- **expansion: unchanged** — 202 → 205 registry rows (2 admitted, 1 rejected), one new knowledge entry
  on **existing** Core ground (correction-filing visibility), not uncovered coverage-map ground; no
  capability row is claimed as expansion (C2's capability row is closure-gated). No frontier promotion.
- **quality: harmed** — C1 verifies on its frozen predicate but the instrument still counts a class of
  hidden filings as filed (a second comment opener after the closer, HIGH, reproduced) and newly
  refuses four visible-filing classes (MEDIUM); C2's gate works on its declared checks but its
  documented `RECEIPT-REV-ABSENT` contract and manifest path confinement do not hold, and its selftest
  asserts less than its claim implies.
- **discernment: harmed** — both claims' evidence overstated their instruments' reach (C1 asserted a
  grammar the frozen code does not implement after the first closer; C2 asserted a fixture power the
  selftest does not have). The lane's own reviewers, not an outside spot-check, found both; the
  closure's sample is the first outside judgement of them.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  gate-registry rows `r57 C1 correction-filing counter (v6)`, `r57 receipt revision-binding gate`,
  `r57 receipt recorder`, `r57 matrix runner`, and the inline-comment error pattern; sources S279/S280
  in `corpus/SOURCES.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round measured its own
  grant end to end (freeze → matrices → selftests → real lane → receipts) and the C2 gate is used on
  the lane's own evidence; `LOG.md` `## Round 57`, `census/round-57/records/*`.
- [~] Instructions executable by an agent without oral context — each gate row carries its entry
  command, verdict map, self-test and pinned-value path; `census/round-57/preregistration.txt` carries
  the full recompute commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the work stays inside repository/workspace
  hygiene evidence instruments; connector01 reports sibling mechanisms without editing them;
  `PROVINCE.md` unchanged.

## Stale-lane

Respawn-per-round driver (hyaku inline run 15); no other mission of this lane is open. The lane was
clean at `d749f7ee` → content revision during the round; progress is observable as commits.

## Tool installs

No host install or upgrade. Seats installed `markdown-it-py 4.2.0` (+ `mdurl 0.1.2`) via `uv pip` into
scratch virtualenvs for independent CommonMark rendering (scout/critic/reviewer01/the L1); each scratch
env was deleted. pacman stayed untouched.

## Claim verdicts (as reported to the operator)

- C1 — predicate T1–T7 verified; **calibration harmed**: HIGH second-opener hidden filings, HIGH
  code-span phantom span suppressing an unrelated overstatement (sentinel H1, a v6 regression), MEDIUM
  over-hide classes (code span, escape, link destination, tab indent); **not admitted**.
- C2 — predicate T1/T2/T4/T5/T6 verified; **calibration harmed** (tag-object contract mismatch,
  unconfined manifest paths, selftest weaker than claimed); operability improved on the declared
  surface; **not admitted**.
- Whole round: **rejected-harmed**, honest stop. No operator ruling assumed. Third consecutive rejected
  closure for this lane (r55, r56, r57) — the next dispatched round should read those three closures
  first.
