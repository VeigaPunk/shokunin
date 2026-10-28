# souji — round 39 report

lane: souji-shokunin · round 39 (hyaku run 11, attempt 1) · agent SoujiR39 · lane base
`ed30b7f5b77939c9073348d810730bc4f355708d` · freeze `b769bfb84a264d8b284c09bc211d99f39a3e9126`
· claims measured at `2f6e981a105fc759205767d2a749a5f7d4fd0b8a` · lane tip `0242085909fb6a4ee041c5443d76316ac6d59d4b` · stale-lane: no (respawn-per-round driver;
no other mission of this lane is open).

## Work performed

Three declared claims, one per owned axis: **C1 calibration** (the 16 defects the round-38
non-author spot-check routed, closed as 16 anchored predicates plus a citation register that
exercises the commit arm), **C2 operability** (`tools/souji-citation-reconcile.py` resolves its
revisions and refuses a non-commit one with exit 2; `tools/souji-worktree-drift.py`'s record-class
docstring matches the classes it raises) and **C3 coverage** (four documented record-parser
behaviours no earlier drift fixture asserted, mutation-scored).

- C1 instrument: `census/round-39/c1-counter.py` + `census/round-39/c1-items.tsv` — 16 anchored
  predicates over committed bytes and a six-row register whose every row names a `commit` later
  than its `receipt_rev` (`census/round-39/cells.tsv`, emitted by `census/round-39/make-cells.py`).
- C1 corrections: `corpus/lessons/round-38.md` (`R39-C1-01`, `-02`, `-14`), `corpus/lessons/round-39.md`
  (`R39-C1-05`, `-07`, `-15`), `census/round-38/preregistration.txt` (`R39-C1-08` = A10, `R39-C1-09`
  = A11), `SCORECARD.md` (`R39-C1-10`), `LOG.md` (`R39-C1-11`, `-12`), `corpus/QUALITY.md`
  (`R39-C1-13`), `corpus/lessons/round-36.md` (`R39-C1-16`), `SKILL.md` (`R39-C1-06`).
- C1 wave evidence: wave wait receipt `census/round-39/records/waves-wait.txt` (R3) and the committed
  capture `census/round-39/waves/` with its verify receipt `census/round-39/records/waves-capture.txt`
  (R4), both landing after every seat settled.
- C2 repairs: revision resolution and the three-valued ancestor predicate in
  `tools/souji-citation-reconcile.py`; the record-class docstring in `tools/souji-worktree-drift.py`
  (including the unreachable `EISDIR` word a wave seat found); new `tests/fixtures/r39-citation-rev.py`.
- C3 coverage: `tests/fixtures/r39-drift-record-rules.py` (7 cases) and `census/round-39/c3-counter.py`
  (M11-M14).
- Sources: `corpus/SOURCES.md` rows S247-S249 opened this round, each with URL, access date and a
  ≤25-word located quote in `corpus/lessons/round-39.md` `## Gate`.
- Wave: one v2 wave, 71 seats (executor 19, reviewer 10, scribe 10, critic 8, scout 8,
  mutation-tester 5, connector 4, simplifier 4, revenger 2, sentinel 1; attack roles 26 = 36.6 %).
  The planner seat stayed with the L1 (validator rejects `planner`); the bounded planning data-walk
  rode scout/connector items. Spec, dispatch, registry and every seat report are captured under
  `census/round-39/waves/`.
- Seat findings integrated: `W1ExecC2Docstring` §5 (unreachable `EISDIR` in the new docstring line —
  fixed at `790d16b`), `W1ExecC1Anchors` (the `line-unique` claim in the items header is imprecise and
  item C1-04's token set is satisfiable by a quoted shape string — named limits below),
  `W1ExecCapture` (the capture CLI's real shape; R4 was capability-ready and only the act was
  missing).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: prereg, C1 items, three counters, two fixtures, three control receipts | Round 39 | b769bfb |
| C2: revision resolution (`REV-UNRESOLVED`, exit 2), drift class contract, `r39-citation-rev`, amendment A1 | Round 39 | bbd9b97 |
| C2: drift docstring triggers on their class lines | Round 39 | 601195a |
| C1: 14 routed-defect corrections, r39 lesson (Gate, Mistakes, dispositions), three SOURCES rows, nine registry rows | Round 39 | c0b007b |
| C1: single-line anchor bullets for R5/R7/R15 | Round 39 | 50972f0 |
| C1: R7 line names the reaped path as `$HYAKU_SCRATCH` | Round 39 | 094e531 |
| C2: drop the unreachable `EISDIR` claim (`W1ExecC2Docstring` §5) | Round 39 | 790d16b |
| PROVINCE boundary note | Round 39 | 2201778 |
| C3/scratch: caller's `TMPDIR` in c3-counter git children and the citation fixture's tool child (`W1ExecScratch`) | Round 39 | d4c1755 |
| receipts: control commands recorded, controls re-measured on final instruments, prereg freeze-prefix proof (`W1RevFreeze`) | Round 39 | f8ba3f3 |
| sources: S250 supersedes S247 with the refusal clause (`W1CritSources`) | Round 39 | e9958ee |
| lesson: wave-1 repairs recorded | Round 39 | 2605bf2 |
| integrate wave-1 lane edits (LOG/SKILL/QUALITY cells with revision pins), scratch-root exit 2 in the three counters, amendment A2, receipts | Round 39 | 5230a34 |
| wave evidence: committed capture + wait receipt (R3/R4) | Round 39 | a8e6d75 |
| register: six rows with `commit` later than `receipt_rev` and their anchored lines | Round 39 | 9440270 |
| register second set: anchored lines must not name their own stale token | Round 39 | a6fe389 |
| wave receipts: settled counts from `w1-results.json`, capture including the results handoff | Round 39 | 2f6e981 |
| measurements: SCORECARD rows/capabilities/planned, LOG entry, three after receipts | Round 39 | 5441045 |
| final-tip re-measure receipt | Round 39 | 8f1c808 |
| lesson: `## Seat-reported failures` carry for `W1CritAssimilation` | Round 39 | c2dcd62 |
| lesson: carry entry names its resolution token | Round 39 | 0242085 |
| wave receipts, capture, SCORECARD/LOG measurements, register | Round 39 | 5441045 |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 routed-defect closure (calibration 7) | `SUMMARY items=16 open=16 register_cells=0 register_mismatches=0 commit_distinct=0` rc 1 (`census/round-39/records/c1-before.txt`) | `SUMMARY items=16 open=0 register_cells=6 register_mismatches=0 commit_distinct=6` rc 0 (`census/round-39/records/c1-after.txt`) | `python3 -B census/round-39/c1-counter.py --root <lane> --rev <full40> --items census/round-39/c1-items.tsv --register census/round-39/cells.tsv --scratch <dir>` | `2f6e981a105fc759205767d2a749a5f7d4fd0b8a` |
| C2 tool contracts (operability 8) | `SUMMARY legs=6 pass=2 fail=4 harm=0` rc 1 (`census/round-39/records/c2-before.txt`) | `SUMMARY legs=6 pass=6 fail=0 harm=0` rc 0 (`census/round-39/records/c2-after.txt`): L1/L2 rc 2 `REV-UNRESOLVED` against rc 1 with 20 findings on the base blob; L5 `cases=8 pass=8` against `pass=4`; L6 five consumers green | `python3 -B census/round-39/c2-counter.py --root <lane> --rev <full40> --base-rev ed30b7f5b77939c9073348d810730bc4f355708d --scratch <dir>` | `2f6e981a105fc759205767d2a749a5f7d4fd0b8a` |
| C3 record-rule mutation coverage (coverage 8) | `SUMMARY mutants=4 killed=0 survived=4 pristine=ok base_killed=0 cases=10` rc 1 (`census/round-39/records/c3-before.txt`, r38 fixture) | `SUMMARY mutants=4 killed=4 survived=0 pristine=ok base_killed=0 cases=7` rc 0 (`census/round-39/records/c3-after.txt`); every mutant still survives the r38 fixture | `python3 -B census/round-39/c3-counter.py --root <lane> --rev <full40> --base-rev ed30b7f5b77939c9073348d810730bc4f355708d --scratch <dir>` | `2f6e981a105fc759205767d2a749a5f7d4fd0b8a` |

All three were re-read at the tip `0242085909fb6a4ee041c5443d76316ac6d59d4b`
(`census/round-39/records/final-tip-measure.txt`) with identical SUMMARY lines, so the readings are
the filed ones.

## Sources & frontier

Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin souji`: before (`--file` over `ed30b7f:corpus/SOURCES.md`)
rows=170, W04=47; after rows=174, W04=47, rc 0 (`census/round-39/records/census-before.txt`,
`census-after.txt`). Rows added: 4, all tier A `mined` (S247 gitrevisions `^{<type>}`, S248
`ast.get_docstring`, S249 argparse exit status, and S250 superseding S247 after a wave seat showed its
quote cut before the refusal clause); rows touched old→new: none (S247 stays as filed). Frontier rows advanced:
none — the rows ground the C2 repair and two disclosures, and no `ground: F<k>` line moved.
C1 rests on S250 (S247's fact, corrected quote). Assimilation: none — the staged `merge/souji/` entries do not serve one of the
three frozen claims (`W1CritAssimilation` checked all 68 knowledge files and 134 staged rows against
the C1/C2/C3 surfaces), and adoption would first need a renumber-by-document pass because the staged
id range S109–S242 now collides with the lane's own S109–S249.

## Trend verdicts

- expansion: **unchanged** — no knowledge entry landed and no frontier map row moved; three registry
  rows ground a repair, not new ground.
- quality: **improved** — two documented tool contracts repaired against a base arm that reproduces
  the defect (rc 1 with findings vs exit 2; a docstring that named the wrong trigger), a new
  revision fixture that fails four cases on the base blob, four record-rule mutants killed where
  every earlier fixture left them alive, and all five consumers green with a harm leg.
- discernment: **improved** — 16 routed defects became 16 falsifiable predicates with a do-nothing
  control at base, a wave seat's residual defect (`EISDIR`) was integrated rather than argued away,
  a fixture case whose expectation had gone stale was corrected under a disclosed tighter-only
  amendment before data, and the wave's two instrument criticisms are carried as named limits.

## Stale-lane

Not stale. The driver is respawn-per-round and no other mission of this lane is open; the lane tip
`0242085909fb6a4ee041c5443d76316ac6d59d4b` is pushed (`ls-remote` matches) and the working tree is
clean (`jj-lane.sh state` tracked=0 untracked=0).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — this round
  adds nine gate-registry rows and `SKILL.md` keeps its tables; sources S247-S250 (S250 supersedes S247); `corpus/lessons/round-39.md`.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` `## 2026-10-28 — Round 39`;
  receipts `census/round-39/records/`.
- [~] Instructions executable by an agent without oral context — `census/round-39/preregistration.txt`
  plus the three counters' `--help`-reachable predicates; wave spec
  `census/round-39/waves/w1-spec.json`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` `## Round 39 boundary note`;
  certification OFF, K5 HELD.

## Errata (r38 report bytes outside this lane's write scope)

- The r38 report's "162 → 167" row-count line and its "4 + 0 dead" opening are corrected in lane
  bytes (`corpus/lessons/round-38.md` `R39-C1-01`/`R39-C1-02`): the measured r38 close is 170 rows,
  8 added, 47 W04, and 42/42 + 32/32 seat reports with 0 dead — `W2MutBattery` settled 19 minutes
  after the report commit.
- The r38 Landed-changes table omitted nine commits (`6949319`, `78ea25a`, `f10a3a8`, `20eea73`,
  `a512efb`, `9b9e2f8`, `cb5737a`, `be66886`, `c5050ea`); they are named in
  `corpus/lessons/round-39.md` `R39-C1-15`.

## Named limits

- C1 binds tokens, not authorship or provenance: a line that quotes the right tokens satisfies it
  (`W1RevC1Forge`), and item C1-04's token set already appears as a quoted shape in
  `census/round-29/records/preregistration.txt` (`W1ExecC1Anchors`). The counter prints `items_sha=`
  so the instrument travels with the reading.
- The items header's "line-unique anchors" wording is imprecise: the predicate requires one *matching
  line*, not a unique anchor (`W1ExecC1Anchors`).
- C2's L4 reads one docstring line per class by the frozen rule; a wrapped trigger reads False by
  construction (M1), and the class-to-trigger pairs beyond MISSING/MALFORMED are not checked.
- C3's mutants are the class boundaries chosen this round; multiple-TOTAL, `--skip-unrecorded` and
  non-UTF-8 records stay uncovered (`W1MutDriftRules`).
- Dead seats: 0 dead of 71 seats; 71 settled, 70 report files — `W1ScoutLaneFiles` settled with its findings in `w1-results.json` and named a report path it did not write (`census/round-39/records/waves-wait.txt`)..

## Tools installed

None. pacman stayed paused; no `uv`/`npx`/binary install was needed.
