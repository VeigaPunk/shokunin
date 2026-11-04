# kaidoku — round 75 (attempt 1)

Lane: `kaidoku-shokunin` (reverse engineering with REA). Axes: coverage + depth + calibration.
Base `3c15a156239af06114e1ece8d1044a0d8205379b`; declaration
`8dff07b9ac7dfc3f099c97d98ee97cc5f69efb3a`; freeze `ec149dc497b4de53ccb3e7a125baa226a66daaa7`;
landing `1f2f7062c11cbf620bc132e52f3709a7618280bb`; measured revision (the record commit the
counter receipts name) `538b8b810f5c50b74fc0330a19e0849b38b27267`; final lane tip
`cbd921e6c86b49d7ae6f0cb3dd233b57506cb54d` (the wave results, their record corrections, and the
receipts naming the measured revision). Full-hash and `ls-remote` proof are in the closing
paragraph.

## Work performed

The round declared two claims on two distinct axes, both capability acquisitions and causally
separable, plus the child-lane frontier step inside the same cap.

- **R75-C1 (operability) — the A12 case set becomes independent and its three survivors close.**
  The round-74 wave found three A12 selftest survivors outside the frozen class set
  (`home_under`/`tmpdir_under` identity checked with `is True` but every fixture boolean; the
  witness keeping one sample per shim name; `lie_clean`'s exact key list replaceable by a superset
  test) and one cross-binding (deleting the `canary_present` field also failed
  `a12-kernel-multiple-samples`). The round-75 probe flattens a name's samples
  (`_name_samples` accumulates, `_samples` flattens), makes the multi-sample case canary-free, and
  adds `a12-genuine-field-identity`, `a12-sample-name-merge` and `a12-lie-clean-keys-exact`
  (`tools/round-75/seam-probe.py`, 25-case selftest). The battery
  (`tools/round-75/probe-mutation.py`) scores a fifteen-class patch set, records
  `sole_detector` per mutant, and compares a supplied pin **before** any generated copy executes
  (round-74 SentinelScope SS74-5). Evidence:
  `.ufo/waves/round-75/pre/c1-base-arm.json` (the before world: 4 survivors, canary failing two
  cases), `.ufo/waves/round-75/pre/c1-post-at-declaration.json` (the after at the declaration:
  0 survivors, sole true, pristine 25), `.ufo/waves/round-75/l1/scores/c1-at-landing.json` and
  `c1-at-tip.json` (the landing/tip re-runs).
- **R75-C2 (calibration) — the record audit's atom grammar becomes exact.** The round-74 audit's
  D9–D12 passed on four cosmetic constructions the wave demonstrated and its D14/D15 did not reach
  the routed receipt or the plan's tool set. `tools/round-75/record-audit.py` re-derives the
  round-74 spot-check's routed defects 1–7 as eight atoms `D16`–`D23` with parsed cell grammars
  (used-by path list, search-note fields and integer counts, rejected-row reason+flip, erratum
  values bound to the measured census), an embedded `validate` block, and one red fixture per
  grammar in its selftest. Evidence: `.ufo/waves/round-75/pre/c2-at-base.json` (8 mismatches at
  base), `.ufo/waves/round-75/l1/scores/c2-at-landing.json` and `c2-at-tip.json` (0), and the
  committed `c2-validate-at-landing.json` (`defects []`).
- **Routed defect 6 (security) in the instruments.** `freeze-pins.py` now lexically refuses
  absolute and traversal pins and resolves worktree paths with `realpath`+`commonpath` before any
  open (SS74-1); `probe-mutation.py` compares the pin before execution and kills a timed-out
  detector by process group (SS74-5/cleanup); `seam-probe.py`'s A11 shims use the fixed-source
  sidecar writer and `_parse_shims`/A11 no longer serialise raw environment values (SS74-4/SS74-3,
  QUALITY #128).
- **Frontier step.** `corpus/SOURCES.md` 189 → 191 rows (S284 `os.path.commonpath` mined, S285
  `environ(7)` rejected; S283 `re.fullmatch` written and withdrawn the same round as a duplicate
  of S143; S277's `used-by` gains the round-75 entry); the search log carries the round-75 note and
  the row-`opened` convention; the mistake class is mined in `corpus/lessons/round-75.md`; the
  sourced claim lands as `corpus/knowledge/2026-11-04-r75-a12-case-independence.md`.
- **Wave.** One v1 wave `r75-w1` (14 seats) — see the wave paragraph.
- **Gate.** The round-29 gate audits the round-75 freeze **CLEAN** with no findings and four
  instrument paths, with four disclosed instrument revisions (`ad53c1e1` runner binding, `0465f251` controls
  identities, `4e93c1a5` freeze-ledger clause, `7edb005e` live-cell grammars):
  `.ufo/waves/round-75/l1/scores/gate-at-freeze.txt` and, at the record revision,
  `gate-at-record.txt` (with `--disclosures`, 50 of 50 rows exact, no missing/stray).

## Landed changes

Every change is in `LOG.md`'s round-75 entry and carried by a commit on the lane branch
(`git log --oneline 3c15a156..<tip>`); the commits, oldest first:

| commit | carries |
|---|---|
| `8dff07b9` | the five round-75 instruments, `plans/round-75-claims.md`, the census-start receipt |
| `ec149dc4` | the freeze container and the pre receipts |
| `bfdf03dd` | the lesson, the sourced entry, the registry rows, QUALITY rows 133/134 |
| `ad53c1e1` | the runner-binding revision and the plan's instrument list |
| `4e0329a4` | the runner disclosure and the re-taken pre receipts |
| `6864a780` | the landing receipts and the four selftest inventories |
| `1f2f7062` | the landing record, the tip receipts and the corrected source ledger |
| `b5f4196d` | the tip re-runs, the landing controls, the record gate |
| `23893e23`, `501b3c09` | the five instruments in the SKILL registry |
| `98825979` | the wave spec, the dispatch and the ready handoff |
| `60d404f5`, `e44d8a8b` | the coverage-map repair and its self-check receipt |
| `cd3892da` | the coverage self-check at the record |
| `ac978bfa` | the round-75 PROVINCE Core additions |
| `6e6b0643` | the lesson's first wave findings |
| `0465f251` | the renamed-case control's exact identities |
| `13d1498f` | the controls revision disclosure |
| `517570c0` | the landing receipt's by-construction mismatch stated |
| `4e93c1a5` | the freeze-pin atom's ledger clause |
| `9817d41a` | the audit revision disclosure |
| `5c0135ff` | the tip counter receipts at that revision |
| `7edb005e` | the grammar atom over live cells |
| `142e78c4` | the second audit revision disclosure |
| `69bb3f7b` | the tip counter receipts at the second revision |
| `8992e7d0`, `20e816fb` | the lesson: ReviewerClaims' verdict and the routed-defect table |
| `8713a508` | the search note's final row ids |
| `be9a0bd4`, `71728000` | the determinism re-run and its receipt |
| `e1944b65`, `eaef97ba` | the wave's seat findings, the D1 erratum, the lesson synthesis |
| `156c4729` | the wave results and the seat evidence |
| `538b8b81`, `f6f3d399` | the wave shape and the four incomplete seats in the record |
| `cbd921e6` | the counter receipts naming the measured revision |

`corpus/claim-freezes-v2.tsv` carries the round-75 `CLEAN` row with its pointer; the freeze's
four disclosed instrument revisions are in `claims.json` `instrument_supersessions`.

## Before → after measurements

- **R75-C1** — counter `survivor_count`. Before:
  `python3 -I -B tools/round-75/probe-mutation.py --root . --rev 3c15a156 --tool
  tools/round-74/seam-probe.py --patch-set r75base --expect-survivors 4` →
  `4` survivors (`d-home-under-truthy, d-tmpdir-under-truthy, d-name-samples-last-wins,
  d-lie-clean-superset`), pristine 20 cases, `b-drop-canary-field` failing
  `["a12-kernel-multiple-samples","a12-kernel-canary-field"]`
  (`.ufo/waves/round-75/pre/c1-base-arm.json`, measured against `3c15a156`). After:
  `python3 -I -B tools/round-75/probe-mutation.py --root . --rev 538b8b81 --tool
  tools/round-75/seam-probe.py --patch-set r75probe --expect-survivors 0
  --expect-target-sha256 1fc1c8fc… --expect-sole b-drop-canary-field` → `0` survivors, 15 killed
  by their declared cases, `sole_detector["b-drop-canary-field"] true` with
  `failed == ["a12-kernel-canary-field"]`, pristine 25, `target_pin {matched true,
  pinned_before_exec true}` (`l1/scores/c1-at-landing.json`, `c1-at-tip.json` at `538b8b81`).
  Controls: `.ufo/waves/round-75/pre/controls-at-declaration.json` (4/4 arms) and
  `l1/scores/controls-at-landing.json` (4/4 at the landing revision).
- **R75-C2** — counter `mismatch_count`. Before:
  `python3 -I -B tools/round-75/record-audit.py --root . --rev 3c15a156` → `8` mismatches naming
  `D16`–`D23` (`.ufo/waves/round-75/pre/c2-at-base.json`). After: the same command at `538b8b81`
  → `0` mismatches, `validate {defects [], atoms 8}` (`l1/scores/c2-at-tip.json`); the landing
  receipt `c2-at-landing.json` and its `--validate` receipt agree. Controls:
  `c2_do_nothing` (8 at base) and `c2_red_fixtures` (four grammars reject their fixture) in the
  same control receipts.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kaidoku` — round start exit 0, **189 rows, 23 W04 warnings**
  (`l1/census-start.txt`); round end exit 0, **191 rows, 23 W04 warnings** (`l1/census-end.txt`).
  Rows added by tier: **2** — S284 (docs/A, `mined`) and S285 (docs/A, `rejected`). One candidate
  row (S283, `re.fullmatch`) was written and withdrawn the same round as a duplicate of S143; its
  id stays a gap (ids never reused).
- Rows touched old→new: **S277 `used-by`** `corpus/knowledge/2026-11-04-r73-kernel-witness-record.md`
  → `… , corpus/knowledge/2026-11-04-r75-a12-case-independence.md` (logged in
  `corpus/lessons/round-75.md` §Gate). The S275 old→new used-by change made in round 74 is
  **re-logged** there, naming `.ufo/waves/round-74/w1/ScribeRows.md` (round-74 routed defect 2).
- Frontier rows advanced: S284 moves `os.path.commonpath` from an unheld surface (path containment
  as a component test, not a string prefix) into the lane's mined set; S285 records the refused
  `environ(7)` page with its flip.
- Sourced claim: R75-C1's evidence lands as
  `corpus/knowledge/2026-11-04-r75-a12-case-independence.md`, which cites S284 (the `under()`
  containment predicate in every witness sample), S143 (`re.fullmatch`, reused), S277 (argv as the
  process's claim) and S278 (the read-permission gate).
- Assimilation: `Assimilation: none` — `merge/kaidoku/` does not serve these claims, and
  `considerthese/` is absent in this lane.
- Search log: a round-75 note with question, where searched, the four integer counts and a stop
  rationale, plus the convention sentence (a row's `opened` is the first-opening date; a
  retrospective row names its opening round).

## Trend verdicts

- **expansion: improved.** Two registry rows enter (one mined, one rejection) and one existing row
  gains a consumer; the admitted entry rests on ground the coverage map did not hold (path
  containment as a component test; the multi-sample witness rule), and its citation chain was
  re-opened this round. Bounded honestly: one candidate row was withdrawn as a duplicate.
- **quality: improved.** The round-74 routed security and evidence defects close with selftest arms
  (containment, pin-before-execution, process-group cleanup, value redaction, sidecar shims), and
  the record audit's four cosmetic-pass grammars are replaced by parsed cells with committed red
  fixtures. The two A12 witnesses now keep every sample, and the cross-binding is gone.
- **discernment: improved.** The round-74 spot-check's eight routed defects are resolved
  item-by-item (defect 8, a report rounding, is corrected in this report and not atomised); the
  round's own candidate row was caught as a duplicate by the lane's census and withdrawn with the
  reason in the lesson; the wave's falsifications are listed below with their disposition.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  instrument-registry block carries five round-75 rows (`SKILL.md`, `<!-- instrument-registry v2 -->`
  block, paths `tools/round-75/*.py`), each with its exit contract, command, pins and write scope;
  the atoms' verdict-meaning tables remain in the craft blocks. No non-author verifier is named for
  this box, so it stays `[~]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's two claim
  instruments ran end-to-end (`l1/scores/c1-at-tip.json`, `c2-at-tip.json`) and `LOG.md`'s
  round-75 entry carries the receipts; `[~]` because the run is the lane's own, not an outside
  verification.
- [~] Instructions executable by an agent without oral context — the frozen predicate commands in
  `plans/round-75-claims.md` were re-run from the committed bytes by ExecBattery
  (`.ufo/waves/round-75/w1/ExecBattery/receipt-A-r75probe.json`, `receipt-B-r75base.json`) and by
  ReviewerClaims (`.ufo/waves/round-75/w1/ReviewerClaims-3/`), both from the frozen revision with
  no lane-file edits; `[~]` until the non-author closure records its own spot-check.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`'s round-75 section names
  only the lane's own instrument/record surface; ConnectorCross reports the sibling-overlap scan
  (`.ufo/waves/round-75/w1/ConnectorCross.md`). `[~]` pending the closure's read.

## Wave

One v1 wave `r75-w1`, 14 seats: 5 executor, 2 scribe, 1 scout, 1 connector, 2 reviewer, 1 critic,
1 mutation-tester, 1 sentinel; attack roles 4/14 = 28.6%; one connector; the L1 held the planner
seat (the validator rejects a planner role). No residual call. Results:
`.ufo/waves/round-75/r75-w1-results.json` (all 14 settled; ten landed a report or receipt, four
returned mid-work prose with no artifact).

Completed and used: **ExecProbeCases** (hand-mutated the round-74 blob: four survivors reproduced,
cross-binding confirmed), **ExecBattery** (both frozen arms re-run, `--validate` clean),
**ExecAuditBase** (eight atoms false at base for their routed reasons; finding D1, below),
**ExecAuditGrammars** (six cosmetic fixtures all rejected, two accepts clean),
**ExecControls** (four arms plus a negative control shown able to fail), **ScribeRows** (fresh GETs
byte-identical to the landed pins; drafts under the pre-correction numbering, drift check names the
landed S277/S285), **ScoutSource** (eight located passages; the pages support the boundary halves,
none of the predicate halves), **ConnectorCross** (duplication with named divergences; no
assimilation), **ReviewerClaims** (R75-C1 re-derived end to end, no blocking defect; F1 below),
**SentinelScope** (all four SS74 items FIXED; five residual LOW/INFO items).

Incomplete, recorded with no verification credit: **ScribeLesson** (stopped reconciling the
renumbered rows), **ReviewerAudit** (stopped diffing the frozen and working-tree audit blobs),
**CriticClaims** (never applied a mutation), **MutationTester** (evidence dir empty). Their
assignments remain unverified; the claims rest on the completed seats above.

Findings that bound the claims: **F1** (ReviewerClaims) — the committed base receipt's
`runner.sha256` is `d7757ae2…`, the disclosed revised battery, because the frozen blob would write
`null` for a base that predates the tool; the two differ only in the runner-binding block and the
frozen blob reproduces every base count (`l1/scores/frozen-base-arm-reproduction.json`). **D1**
(ExecAuditBase) — the plan frozen at `ec149dc4` named four of the five pinned instruments, completed
at `ad53c1e1`; recorded as an erratum in `claims.json`, and D21 reads the completed plan at the
measured revision. **Residual security items** (SentinelScope) — `controls.py` executes a
caller-selected `--after-rev` blob without a pin, unredacted stdout/stderr tails could carry bytes
from a future measured tool, and `pinned_before_exec` is a constant label; all LOW/INFO and
claim-independent.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Round 75 is the only round this
L1 works; round 76 is not started.

## Tool installs

None. No tool was installed or upgraded; no pacman transaction ran (the host-wide pause holds).

## Honest notes

- The landing receipt `c2-at-landing.json` was produced at `6864a780`, one commit before itself:
  `D16` cannot be true in the commit that first contains the receipt it reads. The claim's counter
  is the tip run at `1f2f7062` (`c2-at-tip.json`, 0 mismatches); the landing receipt shows 1
  (`D16`) and its `validate` block is defect-free.
- `tools/round-68/registry-conformance.py` at the tip reports the five round-75 instruments
  registered and no duplicates/unregistered rows; two pre-existing `thin` rows
  (`tools/round-72/capsule_audit.py`, `tools/round-73/capsule_audit.py`) remain from earlier rounds
  and are outside this round's claims.
- No tool was installed or upgraded this round; no pacman transaction ran.
- **Receipt trust model.** Atoms `D16`, `D18`, `D19` and `D22` read committed receipts; they
  re-derive the receipts' internal claims and pin sets but do not re-execute the instruments
  (the PROTOCOL §Gate standard: verified, never executed). A hand-forged receipt whose fields are
  mutually consistent would pass them; what binds the receipts is `D21`'s runner/pin check and the
  freeze gate's instrument pins, not a cryptographic signature.
- The S275 re-log (round-74 routed defect 2) is a lesson entry, not a registry edit: the registry
  cell itself was already correct at the round-74 tip.
- Round-74 planned item (e) — ExecArm's A2 `--expect-upx` recipe (use the route receipt's own
  recorded argv0 path) — is not exercised this round: no route run was made, and the recipe is
  recorded for the next route round rather than silently claimed.
- Round-74 routed defect 8 (the report's 4/15 printed as 27%) is corrected here: the wave is
  14 seats with 4 attack seats, 28.6%.
- The `c2-at-landing.json` receipt records 1 mismatch (`D16`) by construction: it was produced in
  the commit that first contains it. The claim's counter is the tip run (`c2-at-tip.json`, 0).

## Routed defects (round 76 queue)

1. **`c2-at-landing`'s by-construction `D16`.** The landing receipt can never be clean in the
   commit that first contains it; a future round should read the tip receipt in `D16` (or emit the
   landing receipt one commit later and name that commit), so the landing receipt and the claim's
   counter are the same object.
2. **`multi_detected` is not empty.** `a-drop-lie-clean` also fails `a12-lie-clean-keys-exact`
   (expected: dropping the conjunct makes the exact-keys case fail too). The battery records it,
   but a future round should state per-mutant expected multiplicity instead of only the canary's
   sole detector.
3. **Atom `D23`'s Gate-row check is positional.** It requires a Gate row whose first cell starts
   `S2` and whose text names a retrospective round; a Gate table that stops using source ids as
   first cells would false-green. Tighten to the table's declared columns.
4. **`parse_census_erratum` scans every integer in the section.** A section that happens to carry
   the measured count for another reason would pass; bind the value to the erratum sentence.
5. **Round-74 planned item (e)** (A2's `--expect-upx` recipe) is still unexercised — carry it to the
   next route round.
6. **Registry conformance's two `thin` rows** (`tools/round-72/capsule_audit.py`,
   `tools/round-73/capsule_audit.py`) predate this round and remain; their verdict cells do not
   match the current verdict grammar.

## Closing proof

- Lane branch tip: `cbd921e6c86b49d7ae6f0cb3dd233b57506cb54d`
  (`/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh state
  /home/vgpnk/Projects/shokunin/kaidoku-shokunin` → `local=… remote=… ahead=0 behind=0`);
  `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin ls-remote origin refs/heads/main` prints
  the same hash.
- The report commit is made by `scripts/hyaku/fleet-commit.sh --as kaidoku` after the lane push;
  its hash is the fleet branch's parent of the driver's `complete` line.
- Scratch: `/fast/scratch/hyaku/kaidoku-r75` is removed after the close; `/tmp` holds no evidence
  path cited by this report.
