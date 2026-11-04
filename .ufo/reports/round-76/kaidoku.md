# kaidoku — round 76 (attempt 1)

Lane: `kaidoku-shokunin` (reverse engineering of shipped artifacts with REA; axes coverage + depth +
calibration). Round 76, one steered round, worked end to end by the L1 `KaidokuR76`.

**Declared claims (2, distinct axes, causally separable).**

- **R76-C1 — calibration, capability acquisition (`capability-row binding`).** The record audit gains
  `D24_capability_rows`: every round section that claims capability rows entered is parsed at paragraph
  granularity and each claimed name must be a `## Capabilities` row with a real description, a resolving
  evidence pointer and its claiming round. Before: the round-75 record claims two rows the card does not hold
  and the round-75 audit is **green** over its eight atoms. After: nine atoms, `mismatch_count 0`, six red
  fixtures.
- **R76-C2 — operability, capability acquisition (`executable printed counting command`).** A plan's
  `counting-command` block is refused on any unbound placeholder or shell metacharacter before execution, run
  with no shell under a four-key child environment inside the work root, and its receipt's counter is read.
  Before: the round-75 printed command exits 2 as printed (`arms_ok 0`). After: `arms_ok 3` and seven
  controls (three do-nothing plus four guard arms) each failing in its named way.

## Work performed

- **R76-C1 — the capability-rows atom.** `tools/round-76/record-audit.py` keeps D16–D23 byte-identical and
  adds D24 with six red fixtures and one wrapped-claim accept case; the two rows the round-75 section claims (`A12 case-independence closure`,
  `exact-grammar record audit`) and the two this round enters enter the table. Evidence:
  `.ufo/waves/round-76/l1/scores/c1-at-tip.json` (mismatch 0, nine atoms, `validate {defects [], atoms 9}`),
  `.ufo/waves/round-76/pre/c1-at-base.json` (mismatch 1, D24 only, both absent rows named),
  `.ufo/waves/round-76/pre/c1-control-r75audit-at-base.json` (the round-75 audit green at base — the
  do-nothing control), `.ufo/waves/round-76/pre/audit-selftest.json` (17 cases at the freeze) and
  `l1/scores/audit-selftest-at-tip.json` (18 cases, 0 failures at the closure).
- **R76-C2 — the printed-command gate.** `tools/round-76/plan-command.py` extracts the block, applies the
  static grammar before any execution, tokenises with `shlex.split`, runs `python3 -I -B tools/...` with no
  shell under `PATH/HOME/TMPDIR/LANG`, contains `$WORK`/`$OUT` by `realpath`+`commonpath`, and reads the
  counter. Evidence: `.ufo/waves/round-76/l1/scores/c2-at-tip.json` (`arms_ok 3`, exit 0),
  `.ufo/waves/round-76/pre/c2-at-base.json` (`arms_ok 0`), `.ufo/waves/round-76/pre/r75-printed-exec.txt`
  (the printed command: rc 2, `missing required arguments: work`), `.ufo/waves/round-76/pre/gate-selftest.json`
  (3 cases at the freeze) and `l1/scores/gate-selftest-at-tip.json` (7 cases, 0 failures).
- **Pre-freeze instrument revision (`58316c92`).** The first `missing-required-arg` control removed `--root`,
  which the audit defaults, so the control could not fail; the selftest caught it and the control now removes
  the required `--rev`. R76-C2's green arm was also made executability-only (rc 0 or 1, integer counter) so
  the two claims are causally separable; the plan's predicate was restated before the container.
- **Instrument revision before the landing score (`a8908930`, disclosed).** D24 compared a claim's bare name
  against a table cell that carries backticks, so it reported four absent rows on a correct table; and D20's
  round-75 erratum clause was bound to the live registry, so adding rows made a historical sentence false. Both
  fixed, both receipts now record their own instrument sha256, and `claims.json` discloses the revision.
- **Fixture closure after the wave (`98407fad`).** The mutation battery's five survivors were closed: the
  absent-row fixture now populates its table (the empty-table guard had masked the check), `cap-wrapped-claim-accepts`
  binds the paragraph grammar, and four gate controls bind the angle-placeholder half, `$OUT` containment, the
  argv allowlist and the metacharacter scan. `tools/round-76/mutation-check.py` scores nine mutants: **0
  survivors, eight sole detectors** (`.ufo/waves/round-76/l1/scores/mutation-check-at-tip.json`). The revision is
  disclosed in `claims.json` (`da6266c2`) and the registry gains its row (`SKILL.md`).
- **Frontier step.** `corpus/SOURCES.md` 191 → 194 rows: S286 (`shlex.split`, mined), S287 (`argparse`,
  mined), S288 (`bash(1)`, rejected; the plan's `sh(1)` URL 404s and the substitution is recorded in the search
  log). Three blocking findings from the scout seat were repaired before the record (see *Sources & frontier*).
- **Record corrections carried (round-75 spot-check defects 3, 5, 6, 7, 8).** `668e545e` (frozen-battery
  reproduction) and `fcf17efe` (record gate's disclosures check) are named here as the two round-75 commits the
  round-75 report omitted; the round-75 receipts' revisions are restated in *Before → after*; the `LOG.md`
  "defects 1-8" clause takes an appended correction; the freeze ledger's disclosure sentence takes a companion
  row in `corpus/claim-freezes-corrections.tsv`; and both round-76 receipts carry their own `exit`.
- **Coverage self-assessment (unclaimed).** The two new entries grew the population to 157: the Owned-axes
  coverage row now cites 157/157 at the round-76 record and keeps 155/155 as the round-75 historical
  measurement; `tools/round-66/coverage-selfcheck.py --selfcheck` reports `mismatches 0`, exit 0
  (`.ufo/waves/round-76/l1/scores/coverage-selfcheck-at-record.json`). The registry census reports 118 rows,
  0 nonconformant, 0 duplicates (`l1/scores/registry-census-at-record.json`).
- **Gate.** The round-29 freeze gate audits the round-76 freeze **CLEAN** with no findings and two instrument
  paths (`l1/scores/gate-at-freeze.txt`), and at the tip with `--disclosures` reports 51 of 51 exact, exit 0
  (`l1/scores/gate-at-tip.txt`).
- **Wave.** `r76-w1`, one v1 wave, 14 seats (4 executor, 2 scribe, 1 scout, 1 connector, 2 reviewer, 1 critic,
  1 mutation-tester, 1 sentinel, 1 revenger): attack roles 5/14 = 35.7 %, one connector; the L1 holds the
  planner seat; no residual call. Dispatched `06:44:50`, settled with `WAVE-DONE`; records in
  `.ufo/waves/round-76/r76-w1-results.json`. **Eight seats landed a report or receipt**; **four returned an
  empty output with no terminal error line** (`ExecBaseArms`, `ExecAuditAtoms`, `ReviewerC2`, `SentinelScope` —
  cause unknown, `note: null`, zero bytes) and **two returned mid-work prose with no artifact** (`ReviewerC1`,
  222 bytes; `CriticClaims`, 139 bytes). No seat was replaced. What landed did real falsification: the
  mutation battery found **five survivors** (closed in `98407fad`), the grammar attack rejected every cosmetic
  construction, the arms seat reproduced C2 without the gate, the scout found three blocking source defects
  (repaired in `da41dfba`), the probe showed the printed command's two defects are the whole set, and the
  connector found no fleet overlap to absorb. The unlanded assignments are reported as unverified: no
  independent end-to-end C1 re-derivation and no security review of the plan-command executor.
- **Inherited state.** No earlier attempt of round 76 exists (`.ufo/watchdog.log` carries one `launch kaidoku
  round=76` line and no `lane-dead-no-report` for it); `.ufo/waves/round-76/` did not exist at round start.

## Landed changes

Every change is tied to the `LOG.md` entry "2026-11-04 — round 76" and to the commit that carries it.

| commit | change | LOG |
|---|---|---|
| `be99e4f9` | declaration: the two instruments, `plans/round-76-claims.md`, the two fixtures, the census-start receipt | round-76 entry, "Gate" |
| `4df5e0f0` | pre-freeze instrument revision: the missing-argument control removes `--rev` (it removed a defaulted `--root` and could not fail) | round-76 entry, "Gate" |
| `58316c92` | pre-freeze instrument revision: C2's green arm executability-only; fixtures under a declared prefix; receipts carry `exit` | round-76 entry, "R76-C2" |
| `5824d5d8` | freeze: `claims.json` (nine atoms, two instrument pins, two loaded-by-counter pins), base and declaration receipts, three controls, both selftests | round-76 entry, "Gate" |
| `bc8f1a44` | wave evidence: the `r76-w1` spec and its generator | round-76 entry, "Wave" |
| `201df797` | the freeze ledger row and the round-29 gate receipt | round-76 entry, "Gate" |
| `821d9eb6` | landing: the four capability rows, the round-76 section, both knowledge entries, the three source rows and their snapshots, the lesson, the coverage-map row, the PROVINCE additions, the two SKILL registry rows, the LOG entry and its correction, the freeze-ledger correction row | round-76 entry, "Record" |
| `a8908930` | instrument revision before the landing score (D24 backtick-stripped keys, D20 bound to the round-75 record, receipts record their instrument) and every receipt re-taken | round-76 entry, "R76-C1"/"R76-C2" |
| `891902a7` | `claims.json` discloses `a8908930` for both instruments | round-76 entry, "Gate" |
| `67f07e6f` | the Owned-axes coverage row at 157/157 plus the record receipts (`c1-at-record`, `c2-at-record`, census-end, registry census, gate-at-record) | round-76 entry, "coverage self-assessment" |
| `62f31482` | the coverage self-check receipt at the tip (157/157, mismatches 0) | round-76 entry, "coverage self-assessment" |
| `da41dfba` | the scout's three blocking source findings repaired (S286 scope/teaches/anchor, S287 attribution and doc version, S288 inverted fragment), the entry's rc-2 section rewritten, old→new logged in the lesson Gate | round-76 entry, "Sources" |
| `bf20422b` | the census count corrected to the receipt's 23 W04 lines (a seat caught the L1's miscount); the round-72/73 historical statements stay byte-identical | round-76 entry, "Sources" |
| `570b5600` | the container's predicate sentences byte-identical with the plan's (QUALITY row 68) and the plan's own C2-block receipt | round-76 entry, "R76-C2" |
| `98407fad` | the wave's five mutation survivors closed: populated absent-row fixture, wrapped-claim case, four gate controls, `tools/round-76/mutation-check.py` | round-76 entry, "Wave" |
| `da6266c2` | the container discloses the fixture-closure revision `98407fad` for both instruments and pins the mutation battery; the pre receipts re-taken | round-76 entry, "Gate" |
| `1de75ea1` | the mutation battery's SKILL registry row and the guard-mask lesson in the capability-row entry | round-76 entry, "Record" |
| `1ab1e164` | wave evidence: the 14 seat records and results, the eight landed seat reports, the wave section of the lesson | round-76 entry, "Wave" |
| `862c48a8` | the tip scores: C1 0, C2 3, mutation 0 survivors, registry 118/0, coverage 157/157, gate CLEAN, census 194 | round-76 entry, "Gate" |
| `875e6488` | the gate receipt at the final tip and the wave handoff record | round-76 entry, "Gate" |

## Before → after measurements

- **R76-C1 — counter `mismatch_count`.**
  `python3 -I -B tools/round-76/record-audit.py --root . --rev <measured> --json-out <receipt>`.
  Before, at base `5303a662`: exit 1, `mismatch_count 1`, mismatches `["D24_capability_rows"]`, D24's defects
  naming `A12 case-independence closure` and `exact-grammar record audit`
  (`.ufo/waves/round-76/pre/c1-at-base.json`). After, at the measured revision `875e6488`: exit 0,
  `mismatch_count 0`, nine atoms `D16`–`D24` all `ok true`, `validate {defects [], atoms 9}`
  (`.ufo/waves/round-76/l1/scores/c1-at-tip.json`). Do-nothing control: the round-75 audit at `5303a662`
  reports `mismatch_count 0` over its eight atoms while both rows are absent
  (`pre/c1-control-r75audit-at-base.json`). The record revision `891902a7` scored the same 0
  (`l1/scores/c1-at-record.json`); the landing revision `821d9eb6` scored 1 by construction, because the
  receipt its rows point at first appears in that commit (`l1/scores/c1-at-landing.json`).
- **R76-C2 — counter `arms_ok`.**
  `python3 -I -B tools/round-76/plan-command.py --root . --rev <measured> --work <scratch> --battery
  --json-out <receipt>`.
  Before, at base `5303a662`: exit 1, `arms_ok 0` of 3, all three arms `BLOCK_ABSENT`/`FIXTURE_ABSENT`
  (`.ufo/waves/round-76/pre/c2-at-base.json`); the round-75 printed command itself, run by hand, exits 2 with
  `{"unevaluable": "missing required arguments: work"}` (`pre/r75-printed-exec.txt`). After, at `da41dfba`:
  exit 0, `arms_ok 3` of 3 — `plan-c1` executed with rc 0 and `mismatch_count 0`, `r75-printed` refused with
  `PLACEHOLDER_UNBOUND` and nothing executed, `r75-argv` executed at rc 2 with the missing-argument message
  (`.ufo/waves/round-76/l1/scores/c2-at-tip.json`). Controls: `prose-plan`, `missing-required-arg`,
  `ellipsis-rev` met at the declaration (`pre/controls-at-declaration.json`), and the four guard arms
  (`angle-placeholder`, `escape-out`, `script-outside`, `shell-meta`) met at the closure
  (`l1/scores/gate-selftest-at-tip.json`, seven cases).

Both claims are measured against committed bytes at `875e6488`, the lane tip at filing (the tree is clean and
`prefile-check.sh` passes at that revision; `ls-remote` shows the same hash).

## Sources & frontier

- **Census before → after.** `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
  exits 0 at round start (191 rows, 23 W04 duplicate-URL warnings, `l1/census-start.txt`) and 0 at round end
  (194 rows, 23 W04, `l1/census-end.txt`).
- **Rows added by tier.** S286 docs/A `mined`; S287 docs/A `mined`; S288 docs/C `rejected`. Rows touched
  old→new: the three new rows' `scope`/`teaches`/`anchor` cells were corrected in place after the scout's
  findings (old→new in `corpus/lessons/round-76.md` `## Gate`); no existing row's `status`, `recheck` or
  `used-by` changed.
- **Frontier rows advanced.** None: both instruments are the lane's own record layer (already mapped ground),
  so expansion is `unchanged` by the LEARNING.md definition. The two mined rows feed
  `corpus/knowledge/2026-11-04-r76-plan-command-executability.md`.
- **Mistake mined.** Class `landing` — *a self-assessment sentence written before its artifact existed, and a
  printed command never executed by its author* — with the round-75 spot-check as evidence and D24 plus the
  plan-command gate as the fix, each shown able to fail (`corpus/lessons/round-76.md` `## Mistakes`). A second
  row records the pre-freeze survivor (a control that removed a defaulted argument and could not fail).
- **Sourced claim.** R76-C2 cites S286 and S287 through
  `corpus/knowledge/2026-11-04-r76-plan-command-executability.md`.
- **Assimilation: none.** `merge/kaidoku/` does not serve these claims (`MERGE-REPORT.md` read for headings
  only); `considerthese/` is absent in this lane.
- **Same-round source corrections.** Three blocking findings from the scout seat were repaired before the
  record (S286's scope asserted three negatives the page never states and its `teaches` credited the page with
  the instrument's refusal; S287 grounded the probe's own rc 2 in argparse; S288's quote was a fragment of a
  sentence that says the opposite). The rows were corrected in place, not superseded, because they are this
  round's own unfiled rows and three superseding rows would duplicate the same URLs; the deviation from
  `CORPUS.md` rule 2 is recorded in the lesson and here.

## Trend verdicts

- **expansion: unchanged.** The two new admitted entries deepen the already-mapped instrument/record ground
  (`corpus/README.md` row "Instrument and record layer, round 76"); no frontier ground entered Core and the
  coverage map's population grew only by those two entries (157/157, `mismatches 0`).
- **quality: improved.** The record's repertoire claim is now re-derived against the table it names (nine atoms,
  six red fixtures), and a plan's counting command is executed by the gate that scores it (three arms, seven
  controls, no shell); both were committed with their red fixtures and before receipts before any claim data, and
  the wave's five mutation survivors were closed rather than reported as green.
- **discernment: improved.** The round's atom population is an outside document's routed set (the round-75
  non-author spot-check), and its own wave found three blocking source-attribution defects that were repaired
  before the record rather than defended — including a control that could not fail, caught by the instrument's
  own selftest.

## SHONEN

One line per box of `SHONEN.md` (the lane's own assessment is `[~]`; only a named non-author writes `[x]`).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — two new registry rows
  (`SKILL.md` instrument-registry block, `tools/round-76/record-audit.py` and `tools/round-76/plan-command.py`,
  each with its exit map, self-invocation and pinned values), the D24 grammar described in
  `corpus/knowledge/2026-11-04-r76-capability-row-binding.md`, and the round-76 decision content in
  `corpus/knowledge/2026-11-04-r76-plan-command-executability.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round: two instruments run end
  to end on committed bytes (base and tip), with receipts; `LOG.md` round-76 entry.
- [~] Instructions executable by an agent without oral context — the plan's counting-command block is executed
  verbatim by `tools/round-76/plan-command.py`; the registry rows carry the exact argv and exit maps.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round-76 `PROVINCE.md` additions name only the
  lane's own record layer; `ConnectorCross` found the plan-command gate unique in the fleet (one instrument-class
  file) and the capability-table atom absent from siblings, and absorbed neither.

**Stale-lane.** Respawn-per-round driver; no other mission of this lane is open. The round's mission was open
from the launch line (`2026-11-04T06:22:54-03:00 launch kaidoku round=76 pgid=502647 driver=hyaku-inline
attempt=1`) and is progressing: twenty lane commits by the lane identity, and files written under the lane repo
since launch.

**Tool installs.** None this round: no package was installed or upgraded, and no pacman transaction ran (the
host-wide pause holds).
