# souji — round 38 (hyaku run 11, attempt 1)

Lane: `souji-shokunin` (`/home/vgpnk/Projects/shokunin/souji-shokunin`), jj-colocated, branch
`master`. Lane base `ca4369a9296011644636711a624da6a8074e8e2a`; freeze
`4090ee5b04ca3205d61c044b89fd9f318cf9850c`; landing `fcdecaaf293f0fee3c39cc148ae91389e04ef63c` (the lane tip at filing; the layout is
freeze `4090ee5`, claim commits through `8093c70`, each named in **Landed changes**). Round shape: two v1 waves, 42 +
32 = 74 seats, 4 + 0 dead, inside the 64–128 band.

## Work performed

The round declares three claims on two axes (one axis carries two, disclosed and separable):

- **C1 — calibration (score 7, the lowest non-retired axis).** Add the commit arm the r37 lesson
  named ("the schema binds an expected token to both a citation line and a receipt blob, and a
  commit id is in neither") and reconcile the ten routed self-assessment cells that the lane owns
  (r37 spot-check routed defects 2, 3 and 7).
- **C2 — operability (score 8).** Close the three drift-tool output-envelope defects the r37 named
  limits list: a `--json` FIFO that blocks forever, `--record X --json X` overwriting its own
  input, and a docstring exit map four classes short (routed defect 6).
- **C3 — coverage (score 8).** Put the drift tool's record-validation refusal surface under a
  fixture and a four-mutant battery with the pristine control the r37 battery lacked.

Work items, each with its evidence pointer:

- **Commit arm in `tools/souji-citation-reconcile.py`** (8-column register, five classes:
  `COMMIT-UNRESOLVED`, `COMMIT-NOT-ANCESTOR`, `COMMIT-UNNAMED`, `COMMIT-RECEIPT-ABSENT`,
  `COMMIT-RECEIPT-DISAGREES`); seven-column registers stay valid.
  Evidence: `tools/souji-citation-reconcile.py:22-36,161-183,227-231`; `census/round-38/records/c1-after2.txt`.
- **Ten append-only reconciliation rows** (six SCORECARD, three LOG, one QUALITY) that each name a
  receipt, a commit where it carries the value, and the r38 counter that binds it.
  Evidence: `SCORECARD.md:643-661`; `LOG.md:1864-1869`; `corpus/QUALITY.md:212-214`;
  `census/round-38/cells.tsv`.
- **Commit-arm fixture** `tests/fixtures/r38-citation-commit.py`, 14 cases + a zero-reporting stub
  control; amendment A2 gives the two receipt-at-commit cases anchors that name their own commits
  (`census/round-38/records/a2-anchor-isolation.txt`).
- **Write-envelope repairs in `tools/souji-worktree-drift.py`**: `O_NONBLOCK` open with an
  `S_ISREG` refusal (`JSON-NOT-REGULAR`), `JSON-IS-RECORD` refusal by resolved path and inode, and a
  docstring that names all ten refusal classes.
  Evidence: `tools/souji-worktree-drift.py:41-59,212-252,298-313`; `census/round-38/records/c2-after3.txt`.
- **Envelope fixture** `tests/fixtures/r38-drift-write-envelope.py`, 12 cases + `--base-tool` arm +
  `BASE-BEHAVIORAL` composition line; amendment A1 rewrote the `docstring-enum` case onto
  `ast.get_docstring` + `tokenize.untokenize` + whole-token both-direction matching
  (`census/round-38/records/a1-docstring-variants.txt`); A3 publishes the base-failure composition
  (`census/round-38/records/c2-base-composition.txt`).
- **Record fixture and mutant battery** `tests/fixtures/r38-drift-record.py` (10 cases) and
  `tests/fixtures/r38-drift-mutants.py` (4 single-defect mutants, pristine control, base-fixture
  arm). Amendment A0 corrected a twelve-case claim about the r37 fixture to its measured six
  (`census/round-38/records/c3-after2.txt`).
- **Durable counter-arms fixture** `tests/fixtures/r38-counter-arms.py` (six cases + stub
  control) rebuilt the three A7 exploits from committed code, replacing the scratch-path receipt a
  closure could not re-run (`census/round-38/records/counter-arms.txt`); amendments A8/A9 reworked
  the docstring token exclusion and the record fixture's filenames after wave-2 findings.
- **Frontier curation**: five rows opened this round — S239 git-merge-base(1), S240 git-cat-file(1),
  S241 fifo(7) and S242 open(2) admitted tier A `mined`; S243 pipe(7) rejected. The Python
  `os.open` page was opened by a seat and is recorded as **not** a valid source for the FIFO-open
  fact (`W1ScoutFifoDocs`), so no row was written for it.
  Evidence: `corpus/SOURCES.md:188-192`; `corpus/lessons/round-38.md` `## Gate`.
- **Lesson, criteria, scorecard, log**: `corpus/lessons/round-38.md` (Claims, Gate, Mistakes M1–M6,
  Adjudications, Frontier, Named limits), `corpus/QUALITY.md` Q86–Q88, `SCORECARD.md:643-693`,
  `LOG.md:1864-1869`.
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time is
  recorded below; the only files the round wrote outside the lane are its spec/dispatch files under
  the lane's `.ufo/waves/round-38/` and the reports under `.ufo/waves/round-38/{w1,w2}/`.
- **Wave 1 (42 seats, 0 dead)**: 10 executor, 8 reviewer, 5 critic, 6 scout, 6 scribe, 2 sentinel,
  2 mutation-tester, 1 connector, 1 revenger, 1 simplifier (17 attack seats, 40 %). Reports:
  `.ufo/waves/round-38/w1/*.md`. Wave-1 findings that changed the artifacts: A0–A7 (seats
  `W1ExecC3Battery` F1, `W1MutCounter` 1–2, `W1RevDocstring` 1–5, `W1CritC2`, `W1SentEnvelope`
  F1/R3, `W1RevBattery`, `W1RevRecordFixture` F1/F2, `W1SentCounter` S1/S3/S4) and the
  adjudications recorded in the lesson's `## Adjudications`.
- **Wave 2 (32 seats, 0 dead)**: 10 reviewer, 10 critic, 6 mutation-tester, 4 scribe, 2 scout
  (26 attack seats, 81 %). Reports: `.ufo/waves/round-38/w2/*.md`. Wave 2 re-ran every counter and
  receipt, re-opened every new source row, attacked the A1 instrument (A8: docstring token by AST
  span, whole-token behavioural cases), found the S239/S242 locator defects (S244/S245) and the
  `c2-after3` label defect (F5, superseded by `c2-after5`), and validated the filed report.
- **Planner seat**: held by the L1 (the validator rejects `planner` seats); no bounded planning
  data-walk was separately delegated.

## Landed changes

Every change is inside the lane repo except the report and the L0 file; each row names the LOG
entry and the commit that carries it.

| change | LOG entry | commit |
|---|---|---|
| freeze: preregistration, commit-arm counter, four fixtures/battery, do-nothing control receipts | `LOG.md` §Round 38 (claims bullet) | `4090ee5b04ca3205d61c044b89fd9f318cf9850c` |
| ten reconciliation rows, S239–S243 rows, lesson draft | §Round 38 R38-C1-7/8/9 | `cb80d0d09b04ff63c18d78ee5c1ec7bf6ea5c83d` |
| first after receipts (C1/C2/C3 + vacuity + consumers) | §Round 38 (claims bullet) | `828f86b1581dd22a2ac656b7e185e587e4390389` |
| amendments A0–A2 (docstring case, anchor isolation, six-case correction) | §Round 38 (claims bullet) | `2843805d4631b040219ed1ba60053035b5a86f07` |
| final after receipts at the amended landing + SCORECARD measurement/capability rows | §Round 38 | `7b542e22dca0098c5c743b586ce0e0fda67a856b` |
| A3 base-failure composition line + receipt | §Round 38 | `020cfd5ecd404c9068fb60940fa0c4eb1b49c248` |
| lesson adjudications and named limits, QUALITY Q86–Q88 | §Round 38 | `9b4432000f51ea28caa21e8f92df23e9a5d9a01e` |
| wave-2 findings integrated (this report's integration commit) | §Round 38 | `<integration>` |

Pre-existing lane bytes the round left untouched: the r36/r37 fixtures, the r35 census record,
`tools/souji-census.sh`, `tools/souji-verify.sh` and every other tool. The only two tools changed
are the reconciler (additive arm) and the drift tool (three repairs).

## Before → after measurements

Each row carries its counting command and the commit it was measured against; the receipts are
under `census/round-38/records/`.

| claim | axis | before (base `ca4369a`) | after (landing) | counting command |
|---|---|---|---|---|
| C1 | calibration 7 | `SUMMARY cells=10 mismatches=10`, rc 1 (`c1-before.txt`) | `SUMMARY cells=10 mismatches=0`, rc 0 (`c1-after8.txt`, measured at `99efe06`); vacuity control `mismatches=9` rc 1 (`c1-vacuity5.txt`); fixture `cases=14 pass=14 fail=0 control=FALSE-GREEN-REJECTED`; `r38-counter-arms.py` `cases=6 pass=6 fail=0 control=FALSE-GREEN-REJECTED` | `python3 -B tools/souji-citation-reconcile.py --root <lane> --rev <tip> --register census/round-38/cells.tsv --register-rev 4090ee5b04ca3205d61c044b89fd9f318cf9850c` |
| C2 | operability 8 | base blob hangs on `--json` FIFO, overwrites its record, misses four doc classes; `base_fail=6 behavioral_fail=3` (`c2-before.txt`, `c2-base-composition2.txt`) | `SUMMARY cases=12 pass=12 fail=0 base_cases=12 base_fail=6 behavioral_fail=3`, rc 0 (`c2-after7.txt`) | `python3 -B tests/fixtures/r38-drift-write-envelope.py --base-tool <git show ca4369a:tools/souji-worktree-drift.py>` |
| C3 | coverage 8 | `SUMMARY mutants=4 killed=0 survived=4 pristine=ok` against the r37 fixture (`c3-before.txt`) | `cases=10 pass=10 fail=0` and `mutants=4 killed=4 survived=0 pristine=ok base_killed=0`, rc 0 (`c3-arms-filed.txt`) | `python3 -B tests/fixtures/r38-drift-mutants.py --fixture tests/fixtures/r38-drift-record.py --base-fixture tests/fixtures/r37-drift-discrimination.py` |

Consumers unchanged (`consumers-after5.txt`): r37 citation 16/16, r38 citation 14/14, r36 drift
12/12, r37 discrimination 6/6, r37 escapes 12/12 `base_fail=9 escapes=9`, r36 report gate 21/21,
r38 record 10/10. Owned score values are unchanged (7/8/8): the lane still has no reproducible
0–10 mapping, so the SCORECARD carries measurements and verdicts, not numbers.

## Sources & frontier

Counting command and both exit codes:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
# round start: souji ok corpus/SOURCES.md, rc 0, 162 rows
# round end:   souji ok corpus/SOURCES.md, rc 0, 167 rows
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
167
```

- Rows before → after: **162 → 167** (rc 0 both ends; 44 W04 duplicate-URL warnings, which the
  census allows).
- Rows added by tier: **A ×5** — S239 (git-merge-base `--is-ancestor`), S240 (git-cat-file `-e`),
  S241 (fifo(7) blocking open), S242 (open(2) ENXIO) admitted `mined`; S243 (pipe(7)) admitted as a
  kept `rejected` row with its flip condition. No B or C rows.
- Rows touched old→new: **none** (no `status`, `recheck` or `used-by` change to a pre-existing row).
- Frontier rows advanced: **none**. No `ground: F<k>` line moved; the four admitted rows ground the
  C1/C2 repairs, not new frontier ground, so F1–F5 stay as recorded.
- Curation note: the Python `os.open` documentation was opened and is **not** a source for the
  FIFO-open fact (it defers to `open(2)`); recording it as a row would have been a false teach
  (`W1ScoutFifoDocs`).
- Assimilation: **none** — the `merge/souji/` package's staged entries do not touch citation
  auditing or a tool's output envelope, and adopting one would not serve a frozen claim. No row from
  `SOURCES.append.md` was appended, and the id-collision check was therefore not needed this round.
  `considerthese/` is absent in this lane.

## Trend verdicts

- expansion: unchanged — five rows opened (four admitted), but expansion counts admitted knowledge
  entries on new coverage-map ground; no `knowledge/` entry landed and no F row moved
  (`corpus/README.md` frontier rows unchanged). The round's new instruments are capability, not
  corpus expansion.
- quality: improved — three drift-envelope defects closed with a 12-case fixture that reproduces all
  three on the base blob (3 behavioural base failures) and kills four repair mutants 4/4
  (`W1MutEnvelope`); record-validation moves from 0/4 to 4/4 killed with a pristine control; the
  citation counter gains an arm whose five classes each have a killing mutant (`W1MutCounter` 5/5).
  Consumers all green.
- discernment: improved — wave 1 falsified four of the round's own instruments (A0–A3) and the
  corrections are disclosed rather than folded away; every source row was re-opened by a non-author
  seat and the panel agreed on the four admits and the reject; the r37 routed defects now have an
  explicit ledger and the limits the round cannot close are named in the lesson. `W1CritC1`'s
  forged-pass demonstration is recorded as a limit of the arm, not hidden.

## r37 routed defects — ledger

| # | r37 routed defect | r38 disposition |
|---|---|---|
| 1 | r37 report cites `131ea876` as the lane tip | **not fixed** — the r37 report is a fleet-repo file outside this round's write scope; erratum E1 below records it |
| 2 | receipt/revision pairing wrong in the r37 report and SCORECARD rows | **narrowed** — every lane-owned cell is reconciled with a named commit (C1); the r37 report rows are errata E2 below; the register itself has `commit == receipt_rev` on all rows (named limit) |
| 3 | residual stale counts in sibling cells | **narrowed** — SCORECARD, LOG, QUALITY cells corrected append-only; the wave-2 stale sweep's remaining candidates are listed under `## Open items` |
| 4 | in-place rewrite of `corpus/lessons/round-36.md:23` | **open** — this round added no rewrite; the correction stays owed as an appended entry |
| 5 | unreachable pointer in S238 | **narrowed** — S238 is a rejected row whose `teaches` explains the absent control; no row cites an untracked wave file this round |
| 6 | docstring vs code exit map | **closed** — the docstring names all ten classes and the case binds it (`docstring-enum`, A1) |
| 7 | revision naming for the frozen-register number | **closed for the lane** — the correction rows name their revisions; the r37 report sentence is erratum E3 |
| 8 | prompt committed by the lane | **not repeated** — this round committed no `.ufo/prompts/` path |

## Errata for round 37's report

- **E1.** The r37 report's "lane tip" `131ea876` is superseded by `cb443f5499fe4ccaa1f1f035050b0752aefadd92`,
  the branch tip at its closure (`git ls-remote origin refs/heads/master`, recorded in
  `corpus/lessons/round-37-verifier-spotcheck.md`).
- **E2.** The r37 measurement rows pair C2/C3 with `0be9bd0`; the receipts are current at
  `93a10b6`/`e6be059` and were re-published at `02b4339`/`bbefcee`. The lane-owned SCORECARD rows
  are corrected append-only in this round's reconciliation block.
- **E3.** "reads 9 at the base and 3 at the landing" is revision-sensitive: 3 at `e987a27`, the
  revision `c1-before.txt`'s A1.1 block reports; a plain anchor count at `0be9bd0` finds four.
- **E4.** The r37 report's live reading `live_regs=23 drift_rows=5` is a real observation of an
  earlier window (`68d38c3`); the committed receipt at the tip reads 24/6 (`W1Revenger37`
  reproduced both). The report paired the older window with the newer path.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` Gate registry rows `r37-citation-reconcile`/`souji-worktree-drift`; `corpus/SOURCES.md`
  S239–S243; `corpus/lessons/round-38.md` M1–M6.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 38
  (three claims measured, receipts under `census/round-38/records/`).
- [~] Instructions executable by an agent without oral context — the four new fixtures and the
  battery run from the lane root with only `python3`/`git`; every counter command is in the
  SCORECARD rows.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; this round's
  surfaces are the lane's own evidence and tooling, and the sibling scan found no contested ground.

## Waves, seats and dead seats

| wave | seats | role mix | dead | reports |
|---|---|---|---|---|
| w1 | 42 | executor 10, reviewer 8, critic 5, scout 6, scribe 6, sentinel 2, mutation-tester 2, connector 1, revenger 1, simplifier 1 | 0 | `.ufo/waves/round-38/w1/` |
| w2 | 32 launched (11 reports at filing) | reviewer 10, critic 10, mutation-tester 6, scribe 4, scout 2 | 0 reported | `.ufo/waves/round-38/w2/` |

Round total **74** (band 64–128), attack share 43/74 (58 %). Wave 2 had not settled when the
round's budget stop arrived (11 of 32 reports on disk, no WAVE-DONE); every wave-2 finding already
on disk is integrated above, and the closure should read the wave-2 result file as the record of
what settled. Specs and dispatches:
`.ufo/waves/round-38/{w1,w2}-{spec,dispatch}.json` (untracked: `.gitignore` ignores `.ufo/waves/`,
as in r36/r37).

## Stale-lane

Stale-lane: no — this is a respawn-per-round driver round; no other mission of this lane is open.

## Tool installs

None. `python3`, `git` 2.56.0, `man` 2.13.1 and the man-pages 6.19 were already present; pacman
stayed paused, no partial upgrade was attempted, and no tool was installed or upgraded.

## Disclosed limits (wave 1 and wave 2)

- **C1's row composition.** Four of the ten reconciliation rows bind cells that were stale at the
  base (the three LOG lines and the QUALITY evidence cell); the six SCORECARD rows re-cite values
  the lane already held at the freeze (the r33 M3 class), so they add a commit binding, not a
  corrected number. The measured-commit cell class (r37 routed defect 2) is bound by **no** row and
  survives; the commit arm is demonstrated by fixture case R6 only, and all ten register rows carry
  `commit == receipt_rev`. The frozen predicate (`cells=10 mismatches=0`) holds; the cell-repair
  credit is four rows, not ten.
- **The commit cell is author-chosen.** `W1CritC1` executed the cheapest forged pass: an author who
  writes the line and the cell can name the receipt's own revision and leave the defective commit in
  the prose; the counter still scores 0. `mismatches=0` means the ten rows are faithful to the
  commits they name.
- **Envelope residuals (not claimed, measured).** A post-guard rename can still swap the record onto
  the `--json` path (`W1ExecAliasMatrix` `info-rename-swap`); the measured-tree guard is a path
  check while the writer re-walks the path (`W1SentEnvelope` F2/R2: 31/60 runs wrote inside
  `--root` after a directory swap; F3: a `--json` path in a measured repository's gitdir is
  written); a write error after `ftruncate` leaves the target empty (A10); `--json ""` is ignored
  (`W1RevEnvelope` F1).
- **Receipt labels and probe worlds.** Two receipts (`a7-counter-fixes.txt`, `c2-after3.txt`)
  named a revision that predates the instrument their body needs; both are superseded by
  `a7-counter-fixes2.txt`/`counter-arms.txt` and `c2-after5.txt`, and the sources census was red on
  the intermediate landing commits (`cb80d0d`-`da92035`) because the S242 pipe fix was committed
  only at `4bda5f6` — green at the final tip (rc 0, 169 rows).
- **The receipt is any blob with a SUMMARY line** (`W1SentCounter` S2): the counter checks the named
  blob and its exact command shape, not that the blob is a receipt.
- **The 15 s bound conflates blocked with slow** (`W1CritC2`: a 16 s sleeper reads as a hang), and
  `base_fail` mixes behavioural with class-only failures — `behavioral_fail=3` is now published.
- **The docstring case's remaining blind spots**: underscore-token raises and `argparse`'s own
  exit 2 are outside it (`W1RevDocstring` e/g); the phantom arm recognises three prefixes only
  (`JSON-`, `RECORD-`, `USAGE`) (`W2RevC2` F2), and a helper docstring quoting `REFUSAL X:` is
  over-collected (`W2RevC2` F3, fail-closed).
- **C3's marginal coverage is three classes, not four** (`W1CritC3`: the TOTAL-repos check already
  dies on the r36 fixture); the fixture's other record rules are asserted but not mutation-scored.

## Filing note

The report is filed after wave 1 settled (42/42, `w1-results.json`) and while wave 2 was still
settling: 11 of 32 reports were on disk and no `w2-results.json` existed at filing time. The
wave-2 findings that had landed (A8 docstring-token exclusion, A9 random record names, S244-S246,
the durable counter-arms fixture, the kama adjacency) are integrated; seats that settle after this
commit are unread by the round owner and are not claimed. The lane's final tip at filing is
`fcdecaaf293f0fee3c39cc148ae91389e04ef63c`; the report contract checker reads `checks=7 pass=7
fail=0` on these bytes and the pre-report gate reads `rc 0`.

## Open items (carried to r39)

- Commit-arm register design: give at least two rows a `commit` different from `receipt_rev`
  (`W1MutCounter`, `W1CritC1`).
- The arm cannot police an author who names the receipt's own commit; the forged-pass demonstration
  is recorded (`W1CritC1` DEMO2).
- The C2 fixture's 15 s bound conflates blocked with slow (`W1CritC2`); the docstring case's
  remaining blind spots are named limits above.
- C3's marginal coverage is three refusal classes, not four (`W1CritC3`: the TOTAL-repos check
  already dies on the r36 fixture).
- r37 routed defect 4 (the r36 lesson rewrite) is still owed as an appended entry.
- L0 questions opened this round: none. (No operator decision was needed; the round routed around
  none.)
