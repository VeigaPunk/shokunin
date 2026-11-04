# tameshi — round 81 (hyaku run 15, attempt 1)

Lane: `tameshi-shokunin` (axes: depth + calibration; verification-fixture
craft). Base `56a0129fe9bfd0ce607290a36350e38ac4df9c72` (= `origin/master`, the
round-80 closure and spot-check tip). Declaration
`1b115ba038e3d3bffc1432e62bbe5eb422c81266` (plan + base controls + the three
instruments). Landing `349bad61fffb04e2e0257e4472b18f85fd559635` (the fixes,
evidence, sources and records), cleanup `e27f28e8271062c3a1217f85cf51620735bb4e99`,
records `1415fb65f50c12de960eb24d712b1386686cd284`, wave commit
`fc7ccfb7e9e4c64749fd453d420abb839bbe5bd8` (**the measured commit**), final
receipts `ccef5f1de17bd44df6adacbb7f024f18628444ec` (= lane tip = `origin/master`).

## Work performed

Three claims frozen before data in `plans/round-81.plan.md` @ `1b115ba0`, one
per axis: **R81-C1 calibration** (the round-80 non-author closure's routed
defect register bound to repo state), **R81-C2 freshness** (every standing
self-state row pins settled instrument bytes), **R81-C3 coverage** (the suite's
own assertion text is pinned, so the two round-80 test-text survivors die). At
least one claim works the lowest scored axis: calibration 8 (depth 10 and
freshness 9 sit above it); the stagnation nudge does not fire (round 80 entered
a capability).

- **R81-C1 — the register bound.** `tools/defect-bind.py` (five row kinds:
  `tree-paths`, `tree-bytes`, `receipt-tokens`, `sources-cell`,
  `doc-contains`; every input read from git objects; manifest-level refusals
  before any row effect, a row's own unreadable input a setup refusal at that
  row) and `tools/defect-bind.json` (six rows over D1a/D1b, D2, D4, D5, D6 —
  D3 is C2's, so the claims verify independently). Before: `DEFECT_BIND:
  rows=6 closed=0 open=6 unexpected=6` exit 1
  (`.ufo/evidence/round-81/controls/c1-before.txt`; re-measured with the
  corrected instrument at `controls/c1-before-instrument-v2.txt`). After:
  `rows=6 closed=6 open=0 unexpected=0` exit 0
  (`.ufo/evidence/round-81/final/c1-sweep.txt`), `--selftest` 11/11
  (`final/c1-selftest.txt`).
- **R81-C1 — the six fixes.** D1: the two round-80 7 MB receipts and the
  census receipt committed by explicit path (`349bad61`; the 0-byte
  `coldread-before.txt` blob is the state the closure found — the cause is
  recorded as a symptom, not a mechanism); D2: the SCORECARD erratum naming
  the receipt's true `24/24` / `17/17` tokens; D4: S289's `used-by` cell gains
  the round-80 and round-81 lessons; D5: the S289 re-open fetch receipt
  committed (`.ufo/evidence/round-81/sources/s289-cat-file.html` +
  `.headers`); D6: the Round 80 and Round 81 bounded-search notes inside
  `corpus/SOURCES.md`'s `## Search log` slice.
- **R81-C2 — the pin audit.** `--pin-audit` / `--pin-rev` in
  `tools/selfstate-freshness.py` (byte equality at pin vs tip; an unresolvable
  pin rev or a path absent at the tip is setup exit 2) + arms 18–20. Before:
  `SELFSTATE_PINS: rows=23 settled=20 stale=3` exit 1 (`controls/c2-before.txt`),
  naming `receipt-exists-selftest` (pin `21ef81e9`, last change `4af6695f`),
  `receipt-bind-selftest` and `registry-bind-selftest` (pin `ae591d5a`, last
  change `01ca77cd`). After: `settled=23 stale=0` exit 0
  (`final/c2-pins.txt`), the standing sweep green (`SELFSTATE: rows=23 match=21
  stale=2 unexpected=0`, exit 0; the two `stale` rows are the declared red
  arms), `SELFSTATE_SELFTEST: 21/21 pass`.
- **R81-C3 — the text pin.** `SELFTEST_TEXT_SHA256` + `ARM21_selftest_text_pin`
  (selfstate) and `arm25-selftest-text-pin` (wave-reconcile): a digest of
  `inspect.getsource(selftest)` against a pinned constant, so an arm-text edit
  fails an arm. The two round-80 survivors were appended to the standing specs
  (`ss-bom-only`, `wr-prefix`). Before (base tool bytes, same single edits):
  `MUTATE: DONE (target=c3-base-ss defects=1 killed=0 survived=1 …)` and the
  wave twin, both `CONTROL: GREEN` (`controls/c3-base-ss.txt`,
  `c3-base-wr.txt`). After: `defects=5 killed=5 survived=0` and `defects=14
  killed=14 survived=0`, both `CONTROL: GREEN`, restore byte-identical
  (`final/c3-battery-ss.txt`, `final/c3-battery-wr.txt`),
  `SELFSTATE_SELFTEST: 21/21`, `WAVE_RECONCILE_SELFTEST: 25/25`.
- **Registry coupling (no-harm).** `SELFTEST_ARMS` 17 → 21 and 24 → 25 moved
  two live registry figures; `tools/registry.json` (both selftest rows and the
  wave-reconcile mutants row, `defects=14`, label `wave-reconcile-arms-r81`),
  the SKILL.md round-81 registry section (`SKILL.md:2241`) and three new rows
  (`defect-bind-selftest`, `defect-bind-sweep`, `selfstate-pins`) landed;
  `REGISTRY_BIND: rows=7 match=7 stale=0 absent=0 error=0 unexpected=0` exit 0
  (`final/noharm-registry-bind.txt`).
- **Standing sweeps at the measured commit.** `WAVE_RECONCILE: rows=6 met=6
  unexpected=0`, `RECEIPT_BIND: receipts=29 bound=14 corrected=8 design=7
  unbound=0`, `ADDRANGE: rows=11 met=11 unexpected=0`, `ARM_LIVENESS: rows=9
  live=9 dead=0`, `COUNT_RECHECK: rows=7 met=7 unexpected=0`,
  `POINTER_RECHECK: rows=12 met=12 unexpected=0`, `FIGURE_ATTRIBUTION: rows=3
  met=3 unexpected=0`, `ANCHOR_DRIFT: rows=16 met=16 unexpected=0`,
  `MUTATE_SELFTEST` `VERDICT: PASS` (`final/noharm-*.txt`).
- **Frontier step (§2b).** `corpus/lessons/round-81.md` carries the two mined
  mistakes, the Gate (S310 opened, S289 re-opened), the corrections of record
  the wave found, and the wave findings; `corpus/QUALITY.md` gains criteria
  78–79 from the two mistakes.
- **Wave evidence.** `.ufo/waves/round-81/w1-spec.json`, `w1-dispatch.json`,
  `w1.ready(.dispatched)`, `w1-results.json`, `w1/` (11 seat reports +
  registry), all committed at `fc7ccfb7`.

## Landed changes

Every change is carried by a `LOG.md` entry (`## Round 81 (2026-11-04) — the
closure's six routed defects, bound`, `LOG.md:4373`, with its "As landed" and
"Final re-derivation" blocks) and by the commits below.

| Change | Commit |
|---|---|
| Plan + base controls + `tools/defect-bind.py` + `tools/defect-bind.json` + `--pin-audit`/arms 18–20 in `tools/selfstate-freshness.py` + `arm25`/constant in `tools/wave-reconcile.py` | `1b115ba0` |
| The six D1/D2/D4/D5/D6 fixes, the three re-pins, `corpus/SOURCES.md` (S310 row + S289 cell + two search-log notes), `SCORECARD.md` erratum/declaration/capabilities, `SKILL.md` round-81 registry, `LOG.md`, `corpus/lessons/round-81.md`, the two spec appends, evidence and source receipts | `349bad61` |
| Cleanup: `defect-bind.py`'s ignored sweep `rev` parameter removed | `e27f28e8` |
| Records: measured claims table, LOG "As landed", round-81 receipts, census after | `1415fb65` |
| Wave commit: D2 check made faithful to the declared predicate, source metadata corrected (S310/S307), capability figure and spec headers refreshed, scribe deltas, `QUALITY.md` 78–79, 11 seat reports + wave artifacts | `fc7ccfb7` |
| Final receipts at `fc7ccfb7`; measured-commit cells point at the wave commit | `ccef5f1d` |

## Before → after measurements

- **R81-C1** — counting command
  `python3 -I -X utf8 tools/defect-bind.py --repo . --manifest tools/defect-bind.json`.
  Before `rows=6 closed=0 open=6 unexpected=6` exit 1 (`c1-before.txt`, and the
  corrected-instrument re-measure `c1-before-instrument-v2.txt`); after
  `rows=6 closed=6 open=0 unexpected=0` exit 0 (`final/c1-sweep.txt`); measured
  commit `fc7ccfb7`. The population is not narrowed between declaration and
  measured tip: `git rev-parse 1b115ba0:tools/defect-bind.json` = `git rev-parse
  fc7ccfb7:tools/defect-bind.json` (`.ufo/evidence/round-81/manifest-binding.txt`).
- **R81-C2** — counting command
  `python3 -I -X utf8 tools/selfstate-freshness.py --repo . --manifest
  tools/selfstate-freshness.json --pin-audit --pin-rev HEAD`. Before `rows=23
  settled=20 stale=3` exit 1 (`c2-before.txt`); after `rows=23 settled=23
  stale=0` exit 0 (`final/c2-pins.txt`); measured commit `fc7ccfb7`. The
  re-pin delta is exactly three `instrument.rev` lines and nothing else
  (`manifest-binding.txt`).
- **R81-C3** — the two battery commands of the plan. Before, base tool bytes
  with the same single edits: `defects=1 killed=0 survived=1` per tool
  (`c3-base-ss.txt`, `c3-base-wr.txt`); after `defects=5 killed=5` and
  `defects=14 killed=14`, `CONTROL: GREEN`, restore byte-identical
  (`final/c3-battery-ss.txt`, `final/c3-battery-wr.txt`); measured commit
  `fc7ccfb7`.

All three were re-derived at the lane tip `ccef5f1d` after the receipts commit:
identical outputs (`DEFECT_BIND: rows=6 closed=6 open=0 unexpected=0`;
`SELFSTATE_PINS: rows=23 settled=23 stale=0`; `REGISTRY_BIND: rows=7 match=7`).

## Sources & frontier

SOURCES census,
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
— before exit 0 with warnings only (`.ufo/waves/round-81/assimilation/census-before.txt`),
after exit 0, verdict line `tameshi ok …/corpus/SOURCES.md`
(`.ufo/evidence/round-81/final/census-after.txt`).

- Rows before → after: **169 → 170**; status `mined` 136 → 137, `queued` 22,
  `rejected` 11; tiers A 151 → 152, B 14, C 4.
- Rows added by tier: **S310 — Python 3.15 `inspect` docs, tier A docs**
  (`mined`, `recheck 365d`, `used-by corpus/lessons/round-81.md`), opened this
  round; fetch receipt `.ufo/evidence/round-81/sources/inspect315.html` +
  `.headers` (HTTP 200, `date: Wed, 04 Nov 2026 08:40:02 GMT`, 221,837 B,
  sha256 `7570b79d…`, byte-identical to the scout's later fetch).
- Rows touched old → new: **S289** re-opened (fetch 08:40:02 GMT, 79,488 B,
  sha256 `91805d9a…`, byte-identical to the round-79 snapshot), `used-by`
  `… round-64.md, round-79.md` → `… round-64.md, round-79.md, round-80.md,
  round-81.md`; **S310** quote metadata `(11 words, page line 1183)` →
  `(10 words, page line 1193)`; **S307** quote metadata `(8 words…)` →
  `(7 words…)` (pre-existing row, same instrument error; both logged in the
  lesson's corrections of record).
- Frontier rows advanced: none (`corpus/README.md` `## Frontier` unchanged) —
  this round's knowledge delta is verification method, not frontier ground.
- Sourced claims: **C2 rests on S289** (re-opened this round), **C3 rests on
  S310** (opened this round). Assimilation: none — the round's claims are the
  closure's routed defects and the `shokuknow/merge/tameshi` package holds no
  instrument or fixture for them (connector T81W1CN1 §2); nothing was opened
  from it and no row was appended. `considerthese/`: nothing mined this round —
  the claims are the closure's routed defects and no proposal fits them.

## Trend verdicts

- **expansion — improved.** Three capability rows enter `SCORECARD.md`
  (`closure-defect bind`, `standing-pin audit`, `selftest-text pin`, each with
  a runnable evidence pointer and first-working round 81) and three registry
  rows enter the lane's home. Coverage grew by the test-text edge class.
- **quality — improved.** Both standing sweeps gained the ability to fail on a
  weakened assertion (21 and 25 arms), `selfstate-freshness` gained a
  byte-level audit mode, and `defect-bind`'s D2 row now implements the frozen
  predicate after the critic's counterexample (a heading-only erratum used to
  measure `closed`; it no longer does). Every after-state has `CONTROL: GREEN`
  and a byte-identical restore.
- **discernment — improved.** The round's own attacks changed it: the source
  scout caught two word-count defects (S310 mine, S307 pre-existing), the
  surface scout caught a live capability figure and both spec headers a step
  behind, the reviewer and the critic independently broke the D2 row, and the
  mutation-tester showed two mutants that would make the *before-states
  certify*. Each is disclosed, most are repaired, and the unclosed ones are
  named below — none is smoothed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:2241` (round-81 registry section: five live gate/probe rows with verdict maps, pinned values and write scopes); lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-1`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:4373` (round-81 entry with before/after lines and every receipt path) and the ten `final/noharm-*.txt` receipts; lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-2`).
- [~] Instructions executable by an agent without oral context — `tools/defect-bind.py:1-60` (contract, kinds, exit map), `--selftest` 11/11 (`final/c1-selftest.txt`); the wave's executors rebuilt the counters from the plan text alone (T81W1E1, T81W1E2, T81W1E3); input-keyed monitor only, no independent promotion verifier (`.ufo/evidence/round-21/coldread/ledger.json`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round; the new instruments stay inside the lane's verification-fixture province; lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-4`).

## Mid-round corrections (attacked and repaired, all disclosed)

1. **D2's instrument did not implement the declared predicate.** Reviewer
   T81W1R1 §3 and critic T81W1C1 independently produced the counterexample (a
   committed candidate keeping only the erratum heading still measured
   `closed=6`). The check now requires each token in the span bytes AND in the
   receipt bytes, the manifest's span was extended to the sentence pair that
   carries `24/24` and `17/17`, and both states were re-measured (base
   `open=6` exit 1, tip `closed=6` exit 0). Predicate, population and kill rule
   unchanged — a correction toward the declaration.
2. **S310/S307 quote metadata** corrected old → new (see Sources & frontier).
3. **A live capability figure** (`wave-record reconciliation`, `23/23` →
   `25/25`) and **both mutant-spec headers** were a step behind their
   instruments; refreshed.
4. **`defect-bind.py`'s contract sentence** said refusals precede any row
   effect; a row's own unreadable blob fires at that row. Rewritten.
5. **The scribe's eight deltas** to the record were applied (criteria 78/79
   now exist; "two" → "three" stale rows; the sweep's exact figure; the
   round-79-only snapshot wording; the census verdict line; the
   before-measurement revision; the LOG's unverified cause rewritten as a
   symptom).

## Round shape

One v1 wave (`w1`), 13 seats under `scripts/hyaku/ufo-wave-policy.json`
(band 8–16): 4 executor · 2 scout · 1 scribe · 2 reviewer · 1 critic ·
1 mutation-tester · 1 sentinel · 1 connector; attack seats 5 = 38.5 %; one
connector seat; residual calls: none. The §3 planner seat stays with the L1
(the validator rejects `planner`); its data walk rode the scout items.
**Settlement: 13 seats, 11 reports, 2 dead.** `T81W1E4` died with no report
(its last text: mid-clone, extracting the spec diffs); `T81W1SN1` returned an
empty output and no report. Neither was replaced; the battery rebuild E4 owed
is covered by R2's independent 38-run matrix and the L1's landed batteries,
and SN1's security surface is partly covered by E1's cheat register and R1's
source audit. Results: `.ufo/waves/round-81/w1-results.json`.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is
open this round. **Tool installs:** none (system `git`, `python3`, `curl`,
`sha256sum`; pacman untouched).

## Limits and routed observations (round 82's axes)

- **Population not revision-bound (connector D-CN3).** `defect-bind.py` reads
  its manifest from the given path; "no row removed / `expect` relaxed /
  population narrowed" is enforced by the frozen commit plus the round's
  manifest-binding receipt, not by the instrument. `--manifest-rev` (the souji
  `--register-rev` precedent) is the named move; adding it mid-round would have
  changed a frozen selftest count.
- **`tree-paths` accepts a tree; `tree-bytes` is mode-blind (reviewer R1 §2.1,
  executor E1's cheat register).** A directory at a cited path satisfies
  `tree-paths`; a symlink entry whose target string is large enough satisfies
  `min_bytes` (the blob is the link target). The live rows are real blobs
  today; D1a and D5 are existence-only, and hardening them is round 82's.
- **C3's digest region and its boundary (executor E3).** The pin covers the
  selftest *function*, so a module-level constant or a vacuous comment inside
  the function is an over-kill / a miss respectively; the two-edit evasion
  (weaken + recompute) is real and declared. `defect-bind.py`'s own text is
  **not** pinned — the C3 class does not yet cover the round's newest
  instrument.
- **C3 sizes as two commands** (one per tool) by construction; its predicate is
  the conjunction of the two summaries, as the plan writes it.
- **A failed `--selftest` returns 1**, the same code as an open register
  (connector D-CN1); the summary line disambiguates. A lane-wide code is a
  convention decision, not this round's.
- **Two pin doctrines (D-CN4):** `arm-liveness.json` pins a revision to
  re-execute that verifier; `selfstate-freshness` rows must pin the tip's
  bytes. Both are right for their object and stay separately named.
- **Not fixed, disclosed:** S1's F4 (measured commit): the table cites
  `fc7ccfb7`, the receipts commit is `ccef5f1d`, and both re-derive
  identically. Unattributed stray at the fleet root: `after` (one line,
  `== SCORECARD diff base-`) names no lane or round and was left untouched.
