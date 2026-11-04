# tameshi — round 79 (hyaku run 15, attempt 1)

Lane: `tameshi-shokunin` (verification-fixture craft; axes depth + calibration).
Base `0cac8e4604e01ff2e2bc0813c745c99d928b5dd5` (= `origin/master`, the round-78
non-author closure verdict commit). Lane tip at report time:
`069a9472d3bacb2ee9cc195b7a70b341d8a9c87c` (`ls-remote origin
refs/heads/master` prints it; `jj-lane.sh state` reads `ahead=0 behind=0`,
`tracked=0 untracked=0`). Report commit: the fleet commit that carries this
file.

Round shape: **one v1 wave, 12 seats** under
`scripts/hyaku/ufo-wave-policy.json` (band 8–16) — 3 executor, 1 scribe,
2 scout, 2 reviewer, 1 critic, 1 mutation-tester, 1 connector, 1 sentinel;
attack seats 4/12 = 33.3 %. Round total 12 seats; **dead seats: 0**
(`w1-results.json`: 12 seats, 12 results, every seat produced output). No
residual call. Frozen plan `plans/round-79.plan.md` at declaration
`92c007052cdd9503ef32de8f901c0a4805049e28`.

## Work performed

Three claims on distinct axes, all landed and all measured; C1 works
calibration, the lowest scored axis (8) — round 78 entered a capability row
(`non-Python instrument freshness row`), so the stagnation nudge did not fire.

- **R79-C1 — calibration, capability acquisition (sourced on S289, re-opened
  this round).** A receipt's recorded tool sha must exist in the committed
  bytes of a revision the receipt names. `tools/receipt-bytes-bind.py` is the
  new standing counter (declared population, `bound`/`corrected`/`unbound`
  states, setup refusals before any row effect), and the eight round-78
  receipts that named `6f532752…` while recording tool bytes that first exist
  at `091d50e4…` get one append-only `# measured_bytes_rev: 091d50e4…` line
  each. The capability row `receipt-bytes binding sweep` enters `SCORECARD.md`'s
  `## Capabilities` table and its figure is a live selfstate row
  (`receipt-bind-selftest`). Evidence:
  `.ufo/evidence/round-79/c1-base-sweep.txt` (before),
  `c1-landed-sweep.txt` (after, regenerated at the work commit),
  `c1-selftest.txt`, `c1-false-correction.txt` (the false-correction control),
  `c1-standing-sweep.txt` (`receipts=14 bound=6 corrected=8 unbound=0` over the
  whole evidence tree), `census-before.txt` / `census-after-append.txt`.
- **R79-C2 — coverage (sourced on S305, re-opened this round).** The two
  survivors the round-78 wave named become fixture coverage: the leftover
  detector's positive branch (`_leftover(path)` extracted; arm22 measures a
  live path → 1 and the removed path → None) and the pinned fixture's
  `HEAD != rev` refusal (`_build_listing_fixture(..., second_commit=False)`
  measured by arm23). `SELFTEST_ARMS` 21 → 23;
  `tools/wave-reconcile-mutants.spec` 10 → 12 defects. Evidence:
  `c2-base-selftest.txt`, `c2-control-battery.txt` (the do-nothing control:
  landed tool minus the two arm registrations → `killed=10 survived=2`),
  `c2-landed-selftest.txt`, `c2-landed-battery.txt`.
- **R79-C3 — operability (sourced on S307, opened this round).** The selfstate
  runner's python tuple `-I` is load-bearing: arm14 runs the real CLI against a
  git fixture whose instrument prints `sys.flags.isolated`, so a tuple without
  `-I` measures `stale`. `SELFTEST_ARMS` 13 → 14; the new
  `tools/selfstate-freshness-mutants.spec` is the standing battery. Evidence:
  `c3-base-selftest.txt`, `c3-control-battery.txt` (base bytes + the spec →
  `killed=0 survived=1`), `c3-landed-selftest.txt`, `c3-landed-battery.txt`.
- **Registry curation (§2b).** S307 appended (Python 3.15 *Command line and
  environment*, tier A, the `-I` ground) and S289/S305 re-opened (`used-by`
  old → new only); census exit 0 before (`census-before.txt`, 166 rows) and
  after (`census-after-append.txt`, 167 rows). Criteria 130 (receipt bytes bind
  to a named revision) and 131 (a new guard is positively exercised) written
  from the two mined mistakes; `corpus/lessons/round-79.md` carries the Gate
  block and four mistakes.
- **Round-78 closure routed defects paid (status-neutral).** (1) the eight
  misattributed receipts bind via the append-only correction (C1); (2) a
  cold-read receipt now names the content tip and the tip itself is measured
  (`coldread-at-a55.json`, and `COLDREAD_PORTABLE rev=069a9472… credited=65/65`
  at the lane tip); (3) the round-78 control receipt gains the observed
  `rc=2` line and a re-run receipt (`.ufo/evidence/round-79/r78-control-rerun.txt`);
  (4) `plans/round-78.plan.md` gains the append-only note naming the
  superseded arm20 mechanism sentence.
- **Wave attacks that changed the landed bytes** (all disclosed, none argued
  away): the sentinel's two probes against the new C1 instrument found real
  holes — a malformed duplicate `# tool:` line escaped the setup refusal
  (`receipt-header-malformed` folded into ARM6; falsification: with the guard
  disabled ARM6 FAILs `9/10` and the malformed receipt binds) and the
  absolute-path form of the tool path had no arm (folded into ARM10; the
  wave's mutation-tester measured `absolute-tool-path-accepted` surviving
  before the fold and dying after) — plus a containment must-fix: the
  selfstate fixture builders lacked `rev-parse --show-toplevel` assertions and
  every fixture/production git call inherited `GIT_DIR`/`GIT_WORK_TREE` (under
  a decoy environment the suites read the wrong repository: selfstate crashed
  and wave-reconcile read `21/23`; with the isolated env both read `14/14` and
  `23/23`). The mutation-tester's independent sweep killed three of its five
  mutants and its two survivors were folded into existing arms (`mode-unknown`
  into arm23, `absolute-path` into ARM10) — both now die; `python-utf8-dropped`
  survives and is named for round 80. The reviewers re-derived every frozen
  clause (R1 PASS on C1 (i)–(v) with (vi) landing; R2 PASS on all eleven C2/C3
  clauses, with vacuousness proven by deleting each new arm and watching its
  mutant survive 22/22). The scout contradicted two premises: the carrying
  commit postdates the receipt's `at_utc` and is not unique (the correction
  wording is "a commit whose committed bytes carry the recorded sha"), and the
  C3 landed receipt had been measured on pre-hardening bytes (the final
  receipts are regenerated at the work commit). The critic returned two static
  counterexamples without a report (recorded in the lesson). The connector
  confirmed `Assimilation: none` (eight staged id collisions; same ids,
  different documents) and its one documentation proposal is adopted.
- **No-harm.** Arms 1–21 of `wave-reconcile` and arms 1–13 of `selfstate` are
  byte-identical between the base and landed selftests; the first ten spec
  defects keep their frozen kill sets; standing sweeps at the work commit
  `1f6709d0`: `WAVE_RECONCILE: rows=6 met=6 unexpected=0`,
  `SELFSTATE: rows=22 match=20 stale=2 unexpected=0` (the base 21 rows plus the
  new `receipt-bind-selftest` row), `RECEIPT_BIND: receipts=14 bound=6
  corrected=8 unbound=0`; `MUTATE_SELFTEST: 107/107 pass` unchanged; the
  cold-read monitor reads `credited=65/65` at the lane tip
  (`069a9472d3ba`, measured).

## Landed changes

| Commit | What it carries | LOG entry |
|---|---|---|
| `92c00705` | frozen plan + design evidence + the three do-nothing controls | Round 79 declared |
| `1f6709d0` | tools, specs, the eight receipt corrections, the capability row, criteria 130–131, SOURCES rows, the lesson, the round-78 payments | Round 79 measured |
| `8da96ef6` | SCORECARD measured block, LOG wave close, the `receipt-bind-selftest` manifest row, final receipts, wave evidence | Round 79 measured |
| `a4b2d4c7` | cold-read rekey settlement batch 1 (14 entries; trace paths hardcoded to round-78 — superseded, kept append-only) | Round 79 measured |
| `1a210b1f` | rekey settlement batch 2 with repo-relative trace paths (ledger 976 → 990; monitor 65/65) | Round 79 measured |
| `d21aebb6` | monitor receipt at the settlement tip | Round 79 measured |
| `a55de2ae` | lesson mistake 4 (the rekey trace-path drift and its fix) | Round 79 measured |
| `069a9472` | monitor receipt at the content tip (`a55de2ae`) | Round 79 measured |

## Before → after measurements

One row per claim; each command is pasteable from the lane root at the
revision it names. The after receipts are regenerated at the work commit
`1f6709d0` by `.ufo/evidence/round-79/gen-receipts-r79.py`, so every receipt
names the revision whose bytes it measured.

| Claim | Before | After | Counting command | Measured commit |
|---|---|---|---|---|
| R79-C1 | `RECEIPT_BIND: receipts=12 bound=4 corrected=0 unbound=8` exit 1 (eight named receipts, `detail=bytes-rev-absent`) | `RECEIPT_BIND: receipts=12 bound=4 corrected=8 unbound=0` exit 0; `RECEIPT_BIND_SELFTEST: 10/10 pass`; false-correction control `unbound=1` `detail=bytes-rev-mismatch` exit 1; eight corrections `1 0` numstat, zero deletions | `python3 -I -X utf8 tools/receipt-bytes-bind.py --repo . --root .ufo/evidence/round-78`; `python3 -I -X utf8 tools/receipt-bytes-bind.py --selftest` | `1f6709d0` |
| R79-C2 | control `defects=12 killed=10 survived=2` (survivors `leak-detector-blind`, `head-guard-removed`), control suite `21/21` | `WAVE_RECONCILE_SELFTEST: 23/23 pass`; battery `defects=12 killed=12 survived=0`, `CONTROL: GREEN`, byte-identical restore; kill matrix as frozen (ten base sets unchanged; the two new mutants die on arm22 only / arm23 only) | `python3 -I -X utf8 tools/wave-reconcile.py --selftest`; the battery command in `c2-landed-battery.txt` | `1f6709d0` |
| R79-C3 | control `defects=1 killed=0 survived=1`, base suite `13/13` | `SELFSTATE_SELFTEST: 14/14 pass`; battery `defects=1 killed=1 survived=0`, the mutant's FAIL set exactly `ARM14_python_isolation_tuple`, byte-identical restore | `python3 -I -X utf8 tools/selfstate-freshness.py --selftest`; the battery command in `c3-landed-battery.txt` | `1f6709d0` |

## Sources & frontier

`SOURCES.md` rows: 166 → 167 (S307 added, tier A, `mined`, opened 2026-11-04,
`used-by corpus/lessons/round-79.md`); two re-opens (S289 git-cat-file, S305
git-ls-tree; `used-by` old → new only, every other cell byte-identical).
Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin tameshi` → exit 0 before
(`.ufo/evidence/round-79/census-before.txt`, 19 W-lines, no E-finding) and
after (`census-after-append.txt`, 19 W-lines). Rows added by tier: A ×1.
Frontier rows advanced: none — no `corpus/knowledge/` entry was added; the
round's sourced claims rest on the opened/re-opened rows and land as criteria
and arms. `Assimilation: none` — the connector re-derived the eight
staged-package id collisions (same ids, different documents; staged PIT
documents map to the held S155/S156), so no package row was appended.
`considerthese`: one still-unimplemented proposal read (the 2026-10-28
reflection's cold-read-cost lesson); it is already implemented as the rekey
run-book this round used, so nothing new was mined.

## Trend verdicts

- **expansion — improved.** A capability enters `SCORECARD.md`
  (`receipt-bytes binding sweep`, first-working round 79, with a live selfstate
  row) and the registry gains one opened tier-A row (S307) plus two re-opens on
  grounds the lane did not hold at those rows. No `knowledge/` entry and no
  frontier row moved.
- **quality — improved.** Three named round-78 survivors become measured
  coverage (C2's two arms, C3's isolation arm), each with a do-nothing control
  and a 100 % kill battery on byte-identical restore; the new C1 instrument
  closes the round-78 routed record class over the whole evidence tree
  (`receipts=14 bound=6 corrected=8 unbound=0`); two real holes the wave found
  in that instrument were fixed and falsified; the cold-read monitor is green
  at the tip (65/65). Relapse: the copied rekey tool carried a hardcoded
  round-78 trace path and the monitor caught it at the settlement tip (51/65);
  batch 2 fixed the copy and restored 65/65 — a recurrence of the round-78
  mistake class, recorded as mistake 4 and fixed in-round.
- **discernment — improved.** The non-author spot-check's four routed defects
  are paid with receipts; the wave's falsifiers were adopted rather than argued
  away (two sentinel must-fixes, two mutation-tester survivors folded, two
  scout premise contradictions, the critic's two counterexamples recorded); the
  claims' own limits are named (a rewritten sha line sweeps clean — the guard
  is the frozen no-existing-line-change rule; C3 measures fixture coverage, not
  production behaviour).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-1`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-2`)
- [~] Instructions executable by an agent without oral context — lane assertion, input-keyed monitor only; no independent promotion verifier (`.ufo/evidence/round-21/coldread/ledger.json`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-4`)

Stale-lane: none — respawn-per-round driver; no other mission of this lane is
open. Tool installs: none this round (no install or upgrade was run; pacman
stayed paused per the addendum guard).
