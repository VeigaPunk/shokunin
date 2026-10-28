# souji round 37 — receipt citations, the drift tool's write envelope, and fixture discrimination

Lane: `/home/vgpnk/Projects/shokunin/souji-shokunin` · hyaku run 11 · round 37 attempt 1.
Lane base `0d974ffcb7dfb70617947531cab2d7e96cd8f9fd`; frozen contract
`census/round-37/preregistration.txt` (freeze commit `d5c6498c5f72a63c9df32b26ee143e8d775eebbd`,
amendments A1/A2/A2.4 appended after the wave-1 seats that produced them); measured landing
`0be9bd0bf0c8143483bc4da609a6225b2c47ab64`; lane tip and `origin/master`
`a269e7204da048f0548b61565db57cbc396326de`. The round repairs the three defect classes the
round-36 non-author spot-check routed (Routed defects 1, 3, 4 in
`corpus/lessons/round-36-verifier-spotcheck.md`).

## Work performed

The round declares **three claims on three distinct axes**:

- **C1 calibration (score 7, the lowest non-retired axis)** — every routed self-assessment cell is
  corrected (in place where it is a current registry cell, append-only where the bytes are frozen)
  and carries a value its cited receipt actually holds at a commit where that receipt exists.
  Nine originally-routed cells plus the two `cases=8` selftest-arm cells = eleven register rows
  (`census/round-37/citation-cells.tsv`) checked by `tools/souji-citation-reconcile.py` with both a
  citation arm (one anchored line, whole-token expected, receipt named, stale absent) and a receipt
  arm (a `SUMMARY` line at `receipt_rev` carries the token), the register pinned with
  `--register-rev`.
- **C2 operability (score 8)** — the F1 drift tool's write envelope matches its docstring:
  `--root` containment (`RECORD-OUTSIDE-ROOT`), a whitelisted child git environment with config
  discovery neutralised, a multi-link/FIFO refusal, and a per-component `O_NOFOLLOW` write of
  `--json` on the resolved path. `tests/fixtures/r37-drift-escapes.py` reproduces six escapes on
  the r36 blob and none on the landing.
- **C3 coverage (score 8)** — six frozen single-defect mutants of the drift tool (the routed
  `live_repos = len(rows) - unreachable` survivor, a `drift_rows` counter that drops UNRECORDED, an
  unrecorded-loop failure not counted unreachable, a one-sided REGS-CHANGED, ABSENT reported as
  UNREACHABLE, and an exit code that ignores drift) all die on named cases of
  `tests/fixtures/r37-drift-discrimination.py`, measured by `tests/fixtures/r37-drift-mutants.py`.

Work items and evidence pointers:

- C1 counter, register, fixture and corrections: `tools/souji-citation-reconcile.py`,
  `tests/fixtures/r37-citation-reconcile.py` (`cases=12 pass=12 fail=0
  control=FALSE-GREEN-REJECTED`, `census/round-37/records/c1-fixture-after.txt`),
  `SCORECARD.md` `### Round 37 receipt reconciliation` (R37-C1-1..4, R37-C1-10), the two SKILL
  registry cells and `SKILL.md:247`, `corpus/lessons/round-36.md` (Claims line corrected in place
  plus a settlement block), and the appended `R37-C1-8`/`R37-C1-9` blocks in the r36 prereg.
- C2 tool repair and escape fixture: `tools/souji-worktree-drift.py` (`CHILD_ENV` whitelist,
  `RECORD-OUTSIDE-ROOT`, `JSON-HARDLINKED` fd check, per-component `open_nofollow`, regular-file
  record guard); `tests/fixtures/r37-drift-escapes.py` (`census/round-37/records/c2-after.txt`).
- C3 discrimination fixture and mutant battery: `tests/fixtures/r37-drift-discrimination.py`,
  `tests/fixtures/r37-drift-mutants.py` (`census/round-37/records/c3-after.txt`).
- Consumer regressions (Q73): `census/round-37/records/consumers-after.txt` — r36 drift fixture
  `cases=12 pass=12 fail=0 control=STUB-REJECTED`, r36 report-gate fixture `cases=21 pass=21
  fail=0 control=STUB-REJECTED`, r27 gate `cases=4 pass=4 control=FALSE-GREEN-REJECTED`.
- F1 live reading kept current: `census/round-37/records/live-run-after.txt`
  (`record_repos=26 record_regs=27 record_prunable=0 live_repos=22 live_regs=23 live_prunable=1
  drift_rows=5 unreachable=0`, the four recorded phantom paths still ABSENT).
- Frontier: `corpus/lessons/round-37.md` (`## Claims`, `## Gate`, `## Mistakes`, `## Named limits`,
  `## Frontier`), `corpus/SOURCES.md` S236–S238, `corpus/QUALITY.md` Q83–Q85, `LOG.md` round entry.
- Wave verification and adjudication: `.ufo/waves/round-37/` (spec, dispatch JSON, per-seat
  reports; that directory is listed in `.gitignore:1`, so the wave evidence is **not** committed —
  the committed evidence is `census/round-37/records/`).

## Landed changes

| commit | content | LOG anchor |
|---|---|---|
| `d5c6498c5f72a63c9df32b26ee143e8d775eebbd` | freeze: prereg, register, three counters/fixtures and their before-control receipts | LOG `Round 37` bullets 1–2 |
| `e987a27c960baa74c08abe7f7ccbd980d9d88460` | C2 tool repair + C3 discrimination fixture/battery + C1 receipt corrections (9 cells) | LOG `Round 37` bullets 2–5 |
| `68d38c3828de92bc84b0640a1ee5bf6844806064` | lesson, SOURCES S236–S238, QUALITY Q83–Q85, SCORECARD measurements, LOG | LOG `Round 37` bullets 5–7 |
| `d30476d25e999d0db93ec2619b44ea7dc221a653` | A1/A2: pinned register, receipt-bound citations, selftest-arm cells; hardlink/parent-swap `open_nofollow`, property env-witness, measured case | LOG `Adjudications` |
| `047564f84e8843a58e34680727ea41140f541f9a` | whole-row anchors; truncate the `--json` target only after the multi-link check | LOG `Adjudications` |
| `bb98c6086dac61df66c11064316173526260f514` | after receipts at `047564f`, SCORECARD measured commits | LOG `Adjudications` |
| `0be9bd0bf0c8143483bc4da609a6225b2c47ab64` | A2.4: refuse a FIFO record instead of blocking; `record-fifo` case; texts | LOG `Adjudications` |
| `6024a76874287ea57e691637e8740dce2906376d` | after receipts at `0be9bd0` | LOG `Adjudications` |
| `a269e7204da048f0548b61565db57cbc396326de` | frozen predicate sentences superseded append-only after A1/A2 (wave-1 connector W1ConnOverlap); measured commit named in LOG | LOG `Adjudications` |

Every commit is lane identity (`souji-shokunin <souji@shokunin.local>`) through `jj-lane.sh`;
`git ls-remote origin refs/heads/master` prints `131ea876…` (the lane tip).

## Before → after measurements

Measured at `0be9bd0bf0c8143483bc4da609a6225b2c47ab64` (receipts committed in the following
commit, `6024a768…`).

| claim | axis | before | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 receipt-citation reconciliation | calibration 7 | `SUMMARY cells=11 mismatches=11`, rc 1 — receipts resolve at the base, no correction line exists; the frozen nine-cell register reads 9 at the base and 3 at the landing (two non-unique anchors + one unnamed receipt), i.e. the frozen instrument could not reach the target (`census/round-37/records/c1-before.txt`) | `SUMMARY cells=11 mismatches=0`, rc 0 (`c1-after.txt`); fixture `cases=12 pass=12 fail=0 control=FALSE-GREEN-REJECTED` (`c1-fixture-after.txt`) | `python3 -B tools/souji-citation-reconcile.py --root /home/vgpnk/Projects/shokunin/souji-shokunin --rev <full40> --register census/round-37/citation-cells.tsv --register-rev <full40>`; fixture `python3 -B tests/fixtures/r37-citation-reconcile.py` | `0be9bd0` |
| C2 drift-tool write envelope | operability 8 | the r36 tool bytes reproduce nine escapes: `cases=12 pass=3 fail=9 base_fail=9 escapes=9`, rc 1 (`c2-before.txt`) | `cases=12 pass=12 fail=0 base_fail=9 escapes=9 control=ESCAPE-REPRODUCED`, rc 0 (`c2-after.txt`); consumers green (`consumers-after.txt`) | `python3 -B tests/fixtures/r37-drift-escapes.py --base-tool <1e771ed blob>`; live `python3 -B tools/souji-worktree-drift.py --root /home/vgpnk/Projects/shokunin --record census/round-35/records/prune-census.tsv --timeout 20` | `0be9bd0` |
| C3 drift fixture discrimination | coverage 8 | the battery against the r36 fixture blob: `mutants=6 killed=4 survived=2` — the routed `live_repos` survivor and the `drift_rows` mutant pass 12/12 (`c3-before.txt`) | `mutants=6 killed=6 survived=0`, rc 0 (`c3-after.txt`); the r36 fixture stays byte-identical and 12/12 | `python3 -B tests/fixtures/r37-drift-mutants.py --fixture tests/fixtures/r37-drift-discrimination.py` | `0be9bd0` |

Owned score values are unchanged (calibration 7, operability 8, coverage 8): the lane still has no
reproducible 0–10 mapping from a verdict to a number, so the rows carry the measurements and the
verdict rather than a number. No axis is harmed: no predicate, counter or record was weakened; the
r36 fixture files are byte-identical; the r35 census record is left as filed.

## Sources & frontier

SOURCES census before → after: **159 rows, rc 0 → 162 rows, rc 0**
(`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin souji`; receipts `census/round-37/records/census-before.txt` and
`census-after.txt`). Rows added by tier: **A ×3** — S236 (git(1) `GIT_TRACE_REFS`) and S237 (git(1)
`GIT_CONFIG_NOSYSTEM`) are `mined`, S238 (git-config(1) `GIT_CONFIG_COUNT`) is `rejected`; each
carries URL, opened 2026-10-28, recheck `365d`, and a ≤25-word located quote in
`corpus/lessons/round-37.md` `## Gate` (quotes read from `MANWIDTH=100 man git` in git 2.56.0-1).
Rows touched old→new: **none**; no existing row's `status`, `recheck` or `used-by` cell changed.
Frontier rows advanced: **none** — the two admitted rows ground the C2 repair, not new frontier
ground; no `ground: F<k>` entry changed, so no F row moves. The sourced-claim requirement is met by
C2, which cites S236/S237. Assimilation: **none** — no `merge/souji/` theme was adopted this round.
`considerthese/` does not exist in this lane, so no proposal was mined.

## Verification and adjudication (wave 1)

Wave 1 (37 seats) verified all three targets and falsified instrument premises, every one repaired
under a disclosed tighter-only amendment **before** the final after-data:

- **A1 (C1).** The frozen register carried two non-unique anchors and could read `mismatches=2` at
  the landing at best; the register was read from the working tree; a bare correction line (no
  receipt) forged a pass; `receipt` could point at the citation file; matching was substring;
  `--record`-adjacent none. Repaired: unique anchors, `--register-rev` pins the register, a
  corrected line must name its receipt, whole-token matching, `SUMMARY`-bound receipt arm, header /
  unique-id / stale-mandatory register rules, scrubbed git env; the two `cases=8` selftest cells
  added (C1-10, C1-11) → `cells=11`.
- **A2 (C2).** A hardlinked `--json` target outside `--root` truncated an in-root file; an ancestor
  directory swapped after the guard redirected the write; `env-witness` asserted four literals, so
  a blacklist built from them passed; a fixed-summary stub could pass; a control-free run exited 0.
  Repaired: `JSON-HARDLINKED` on the opened fd (truncate only after the check), per-component
  `O_NOFOLLOW` walk, property-level env assertion, `case-measured`, non-zero on a control-free run;
  A2.4 refuses a FIFO record instead of blocking. Fixture `cases=12`, `base_fail=9`, `escapes=9`.
- Every wave-1 finding that the repairs do not close is named in `corpus/lessons/round-37.md`
  `## Named limits`: `--record X --json X` self-overwrite, a hardlink/parent swap installed after
  the guard, nested-repository discovery, the `TOTAL` cross-checks and duplicate-row refusal absent
  from the r37 fixture, the `receipt_rev` arm's non-discrimination (receipts are blob-identical at
  both revisions), the `42ea92e` measured-commit arm (schema cannot express a commit-only
  citation), and two pre-existing never-true cites (`SCORECARD.md:40` `cases=16`,
  `corpus/lessons/round-35.md:8` `cases=5`). These are routed to round 38, status-neutral.

## Trend verdicts

- **expansion: improved** — two mined tier-A sources and one rejected row (census 159 → 162, rc 0),
  three QUALITY criteria Q83–Q85, one capability row (self-assessment receipt reconciliation), and
  two new runnable instruments with fixtures; the new discrimination fixture widens the drift
  tool's killed-mutant surface from 4/6 to 6/6.
- **quality: improved** — nine reproduced write escapes closed on the drift tool (`base_fail=9
  escapes=9` at the final fixture to none; the landing blob still failed three of the later cases,
  closed at `4c257b7`) with its r36 consumers still green; three instrument forgeries closed in the citation
  counter; the six frozen mutants die on named cases; the r36 fixture is byte-identical.
- **discernment: improved** — the routed never-true numbers are reconciled against receipts at a
  commit where they exist (`mismatches 11 → 0`); wave-1 falsification changed the instruments and
  the frozen texts disclosedly (A1/A2/A2.4) instead of being absorbed; every unclosed finding is
  named as a limit rather than claimed fixed (the routed r38 list is now carried in the lesson's `## Named limits`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the SKILL gate registry is updated to the landed rows/fixtures (`SKILL.md` r37 rows, `cases=16`/`cases=12`/`cases=6`), with S236/S237 grounded.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## 2026-10-28 — Round 37 attempt 1` plus `Adjudications`, tied to `d5c6498`…`a269e72`.
- [~] Instructions executable by an agent without oral context — every counting command in this report and `census/round-37/preregistration.txt` runs from the lane root (the pre-freeze before-controls ran with the working register, as their receipts state; the pinned `--register-rev` form runs at every later revision); fixtures are self-contained under `TMPDIR`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touches only repo/workspace hygiene (citations, worktree drift, fixture discrimination); no sibling lane was edited; the connector scan was read-only and its report is untracked under `.ufo/waves/`, so the committed record is this line.

## Waves

Shape: two v1 waves (policy `ufo-wave-policy.json`, band 32–64), validated with
`ufo-swarm-wave.mjs run`. **Wave 1: 37 seats** — 15 executor, 6 reviewer, 4 critic, 4 scout,
3 scribe, 2 sentinel, 2 mutation-tester, 1 connector; attack roles 12/37 = 32.4 %. **Wave 2: 32
seats** — 12 reviewer, 7 critic, 7 mutation-tester, 4 scout, 2 sentinel; attack roles 26/32 =
81.3 %. Round total 69 seats, inside the 64–128 band. The inline ready marker was written and not
taken (no dispatcher process for this lane); the contract's dispatch bridge was used instead: one
`task` call per wave carrying the validator's `taskCall` unchanged (`w1-dispatch.json`,
`w2-dispatch.json`, `w1-dispatch-fallback.txt`). At filing, wave 1 has **35 of 37** seat reports on
disk and wave 2 has been dispatched (0 settled); dead seats: **0** reported in wave 1. Wave 2's
late results, if any, ride into round 38 as errata (the r36 precedent). `.ufo/waves/` is
`.gitignore:1`, so no wave file is committed; the committed evidence is
`census/round-37/records/`.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. No tools were installed or
upgraded (pacman stayed paused); certification OFF, K5 HELD, NAMESPACE hold unchanged.

### Erratum (2026-10-28, appended after filing)

Wave-1 connector seat `W1ConnOverlap` found the round committing the exact defect class C1
repairs: the FROZEN PREDICATE SENTENCE block in `census/round-37/preregistration.txt` still read
`cells=9` and `cases=6 … base_fail>=3` after A1.3/A2.3/A2.4 had moved the in-force targets to
`cells=11` and `cases=9 … base_fail=6`. The sentences are now superseded **append-only** in the
same file (block after the frozen sentence, naming `0be9bd0bf0c8143483bc4da609a6225b2c47ab64`),
committed at `a269e7204da048f0548b61565db57cbc396326de`, and `LOG.md` names that commit. No
target, receipt or stale cell changed; the measured landing is unchanged. At erratum time wave 1
has 36 of 37 seat reports on disk and wave 2 remains unsettled.

### Erratum 2 (2026-10-28, after wave-2 receipts)

Wave-2 seats found the round re-committing the class it repairs in its own text. Fixed at
`a269e7204da048f0548b61565db57cbc396326de`:

- `SCORECARD.md` and `corpus/lessons/round-37.md` quoted `cells=11 mismatches=9`; the receipt reads
  `mismatches=11` (`c1-before.txt`). The capability row quoted `cells=9` / the 7-case fixture; it
  now reads `cells=11` / `cases=12`.
- `LOG.md` quoted the pre-amendment C2 numbers (`cases=6 … base_fail=4`) and the freeze-era C1
  before value; both now match the final receipts (`cases=9 … base_fail=6`, `cells=11 … 11`).
- `SKILL.md` rows `r37-citation-reconcile` and `r37-drift-escapes` quoted `cases=7` and
  `cases=6/base_fail=4`; both now read `cases=12` and `cases=9/base_fail=6`.
- The A1 wording said the frozen register read `mismatches=2`; the landing counter reads `3`
  (two non-unique anchors plus the unnamed-receipt arm) and the freeze-era counter read `2` — both
  are now stated.
- The `live-run-after.txt` header now says it is a live-fleet window observation (a wave-2 seat's
  worktree changed `live_regs`/`drift_rows` during the round; `W2ScoutAfter`).
- New named limits: the `env-witness` case asserts the documented child-env contract as a key set
  and can false-kill a stricter spelling / miss a tool-injected trace or a first-call-only
  neutralisation (`W1ExecEscapeCaseC`); the report-contract checker's stale-lane **line** arm has no
  fixture case (`W2MutReportGate` P1 survives); S236's exclusion of "trace output options" was
  narrowed because the output target is what makes the escape caller-visible (`W2RevSource236`).
  All routed to r38.

Before receipts were also regenerated with the final counters/fixtures at
`8edcb04212b641203862921297655a1d329808e4` (C1 `cells=11 mismatches=11`; C2
`cases=9 pass=3 fail=6 base_fail=6`); the measured landing, targets and kill rules are unchanged.

### Erratum 3 (2026-10-28, after wave-2 mutation probes)

Wave-2 found the C1 fixture's implicit discrimination claim weak: 8 of 11 mutants of the counter
survived the 12-case suite, including an arm-reads-working-tree mutant
(`W2MutCounter2`). Fixed at `53a67f7`: the fixture now has **16 cases** — `worktree-tamper`
(committed bytes beat a tampered working copy), `empty-register`, `duplicate-id`, `stale-dash` —
and the worktree-reader mutant is killed by `register-pinned` and `worktree-tamper`
(`cases=16 pass=16 fail=0 control=FALSE-GREEN-REJECTED`, receipt `c1-fixture-after.txt`). The
counter is unchanged, so C1's measured target (`cells=11 mismatches=0`) is unaffected.

Also recorded, status-neutral, routed to r38: (`W2MutFixture2`) of the six frozen C3 mutants, four
die on `rc`/row-text assertions and the "exact-field" discrimination is carried by two
(`match-exact` and `prunable-live` kill no frozen mutant and earn their place on controls); the
`env-witness` case asserts the documented child-env key set and is not a general env-safety proof
(`W1ExecEscapeCaseC`); the report-contract checker's stale-lane line arm has no fixture case
(`W2MutReportGate` P1); C1's `receipt_rev` arm remains non-discriminated (`W2MutCounter2`, wave 1);
and S236's scope now records that the trace output target is what makes the escape caller-visible
(`W2RevSource236`). Before receipts were regenerated with the final instruments at `8edcb04`
(C1 `cells=11 mismatches=11`, C2 `cases=9 pass=3 fail=6 base_fail=6`); the measured landing, the
targets and the kill rules did not change.

### Erratum 4 (2026-10-28, final receipt set)

Wave-2 found two live escapes on the landing tool and two forged-control paths. Fixed at
`4c257b7`/`e6be059` and re-measured at `a269e7204da048f0548b61565db57cbc396326de`:

- **A2.7** — the `--json` guard now also covers the gitdir each row resolves to
  (`rev-parse --absolute-git-dir`), refuses a row whose gitdir is outside `--root`, and skips
  symlinked discovery children. Cases `json-gitfile-write`, `json-symlink-child`,
  `record-symlink` added (a gitfile row and a symlinked row previously truncated an out-of-root
  repository at rc 0).
- **A2.5 (final)** — the control binds observed escape artifacts (`escapes>=6`) as well as the case
  floor (`base_fail>=8`); a stub that merely errors prints `control=ESCAPE-NOT-REPRODUCED`, rc 1.
  Final fixture: `cases=12 pass=12 fail=0 base_fail=9 escapes=9`.
- **A2.6 reverted** — a register-containment check broke the fixture's sibling registers (16 cases,
  10 failures); the cheap register-substitution cheat is closed by `--register-rev` in every
  command string, and the register-as-input semantics are named as a limit.
- Receipt monotonicity: the receipt set was rewritten across revisions (C2 6→8→9→12 cases; C1
  fixture 12→16). The final set is the one at `bbefcee`; readers at intermediate revisions see
  receipts that match neither that revision nor the final rows. Disclosed, not repaired
  retroactively.
- Still routed to r38 (status-neutral): report-contract checker's stale-lane **line** arm
  (`W2MutReportGate` P1); the C3 battery has no pristine-fixture control and conflates a crashing
  fixture with a kill unless the SUMMARY gate is kept (`W2MutBattery`); the `receipt_rev` arm is
  non-discriminated; the `TOTAL` cross-checks and duplicate-row refusal are absent from the r37
  discrimination fixture; nested-repository discovery; `--record X --json X` self-overwrite; and
  the `--json` FIFO hang at the landing blob (fixed for records only, post-landing).

### Erratum 5 (2026-10-28, final tip)

Wave-2 re-runs of C1 found two substring arms in the citation counter. Tightened at
`3e24784`: the corrected line must quote its receipt in backticks (a `fake/<receipt>` path no longer
passes), the four short `expected` tokens became full `cases=N pass=N` phrases (a disagreeing
`pass=0` summary no longer satisfies them), and the before-receipt note about the freeze-era counter
was corrected (that blob does resolve and reads 2). The C1 fixture's synthetic notes quote their
receipt (A1.5); fixture `cases=16 pass=16 fail=0`. Final receipts: C1 `cells=11 mismatches=0` and
16/16 at `b491596`; C2 12/12 `base_fail=9 escapes=9` and C3 6/6 at `bbefcee` (the tool is unchanged
between those commits). The register is an input, not audited evidence; `--register-rev` in every
command string is what closes the substitution cheat, and this is named as the C1 limit.

### Erratum 6 (2026-10-28, closing corrections)

Final lane tip `a269e7204da048f0548b61565db57cbc396326de` (= `origin/master`). Corrections to
this report's own attributions and the round's gate text:

- **Attribution.** The frozen-predicate supersession block was committed at `131ea87`, not at a
  later tip; the own-cell reconciliation (SCORECARD/SKILL/LOG/lesson) at `5379251`; the gitdir and
  symlink containment plus escape-bound control at `4c257b7`; the A2.6 revert at `e6be059`; the
  final receipt set at `bbefcee`/`b491596` and now `93a10b6`. Errata 2–4 named the then-current
  tip where they should have named these commits.
- **A2.6 is reverted.** The prereg now marks it historical: the register-containment check broke
  the fixture's sibling registers (10/16 failures) and was removed at `e6be059`. The substitution
  cheat it targeted is closed by `--register-rev` in every command string; the register is an
  input, not audited evidence, and that is the named C1 limit.
- **One gate, one number.** The escape fixture's docstring, code, SKILL row and prereg
  supersession now all read `cases=12 pass=12 fail=0 base_fail>=8 escapes>=6
  control=ESCAPE-REPRODUCED`; the SKILL row carries `--register-rev`.
- Final receipts at `93a10b6`: C1 `SUMMARY cells=11 mismatches=0` (fixture 16/16); C2
  `SUMMARY cases=12 pass=12 fail=0 base_fail=9 escapes=9 control=ESCAPE-REPRODUCED`; C3
  `mutants=6 killed=6 survived=0`; consumers 12/12, 21/21, r27 4/4.
- Still routed to r38: the report-contract checker's stale-lane **line** arm; the C3 battery's
  missing pristine-fixture control; `receipt_rev` non-discrimination; TOTAL/duplicate-row cases;
  nested-repository discovery; `--record X --json X` self-overwrite; the `--json` FIFO hang on the
  landing blob; the `--gate PATH` interpreter mismatch in the r36 fixture; and the live reading's
  non-reproducibility (a window observation, not a baseline).

### Erratum 7 (2026-10-28, final)

Lane tip and `origin/master`: `a269e7204da048f0548b61565db57cbc396326de`. The wave-1 lesson
scribe found the lesson's shape defects and one receipt-provenance regression; fixed here:

- `corpus/lessons/round-37.md`: S238's Gate row closes as a table row; the S236/S237 locators
  carry `MANWIDTH=100` and the heading/quote lines; M2 now carries a fix **shown able to fail**
  (the pre-fix battery scored a crashing fixture as six kills; the landing battery reports
  `NO-SUMMARY`, `survived=6`, rc 1); the landing line names the code landing `e987a27` and the
  measured landing `02b4339`; C2 reads nine escapes, not six.
- `census/round-37/records/c1-after.txt` and `c2-after.txt` are regenerated **with** header,
  command and `rc` lines (a bare SUMMARY at `40bbd2e` lost the commit binding); values are
  unchanged (`cells=11 mismatches=0`; `cases=12 pass=12 fail=0 base_fail=9 escapes=9`).
- The lane hash in this report's header is superseded by this erratum; the value at the time of
  each filing is recorded in the erratum that follows it. No target, receipt value or kill rule
  changed in this erratum.

### Erratum 8 (closing record)

Lane tip and `origin/master`: `a269e7204da048f0548b61565db57cbc396326de`. The final wave-2 lesson
review found two false sentences in `corpus/lessons/round-37.md`, both fixed in this commit:

- M2 asserted "the frozen mutants, **targets** and predicate sentences did not change". False: A1.3
  and A2.3 raised the C1/C2 targets after the first after-receipt, and the frozen sentences were
  superseded append-only. The lesson now states both changes and that it does not claim a monotone
  receipt history.
- S238's Gate cell cited an untracked wave report for its decisive control. It now states the
  mechanism (`read_very_early_config` ignores command-line/repo config, so only system/global files
  reach trace2) and points at the committed counter arm, naming the wave report as untracked.

This is the closing record for the round: later wave-2 seat reports are errata for r38, not
changes to these verdicts. The measured targets and receipts are unchanged: C1 `cells=11
mismatches=0`, C2 `cases=12 pass=12 fail=0 base_fail=9 escapes=9`, C3 `mutants=6 killed=6
survived=0`.
