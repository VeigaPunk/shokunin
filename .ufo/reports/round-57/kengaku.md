# kengaku — round 57 report (hyaku run 13, 2026-11-01)

Lane: `fleet/kengaku-shokunin`, branch `master`. Base `c9ce9a713de770b2cb0c594fe3f9ad5019b64e0f`
(the round-56 verifier spot-check tip). Measurement environment: WSL2 Ubuntu-24.04 (python
3.12.3, bwrap 0.9.0, git 2.56, numpy 2.5.4, biopython 1.85; `uv` absent — the r56 A3.4
canonical counter environment preserved; **no environment mutation this round**). All
executions ran in WSL from script files with in-file `EXIT=$?` capture (the r56 relay
lesson).

## Work performed

- **Carried obligation discharged first (R56-V1, load-bearing, plus a second root cause it
  carried).** Re-derived the before-state at base in WSL from a clean clone: registry
  counter `ADVERTISED total=83 / REGISTERED total=82 rows=84`, `MISSING
  plans/round56_landcheck.py`, `PREDICATE R52-C2 fail`, exit 1; full entry-truth run
  `executed=83 … laundered=2` — `LAUNDERED round52-c2`, `LAUNDERED routed-findings` —
  `PREDICATE R55-C2 fail`, exit 1 (receipts `.ufo/waves/round-57/fix/c1-before-*.txt`,
  committed). Two tip-only regressions, both landed by the round-56 close commit `d834d89d`
  after the canonical measured revision: (1) the SCORECARD round-56 section advertised the
  landcheck with no registry row; (2) the R56-F2 findings row's `source` field carried prose
  after the path (`corpus/lessons/round-56.md:Corrections`), the same strict-shape defect
  the round-56 corrections already fixed for R56-F1's row. Fix landed as wave A `f754593b`:
  the landcheck's registry row (all eight cells, measured verdicts) + its entry-truth
  ledger row (the r54/r55 counters enforce registry↔ledger bijection: adding the registry
  row alone would have regressed the counters via `missing=1`) + the R56-F2 `source`
  corrected to `corpus/lessons/round-56.md:60` with the correction history appended to the
  row's note. Both ledger/registry edits are byte-stable text insertions (V4's rule). The
  fix was pre-verified on a scratch clone before committing: all three counters green, the
  landcheck itself `LANDCHECK PASS n=4` (6.7 s).
- **R56-V2/V3/V4 corrections** (same wave-A commit): PROVINCE SF14 row re-counted and dated
  (197 — the round-56 cell's "195" was that round's before-count, stale on arrival);
  SCORECARD round-56 section carries the dated precision block (14 literal green→red flips
  + 2 already-red fragment refreshes + stage-scan's argv re-declaration = the honest
  decomposition of "seventeen"; "sixteen declared-green rows false here" = 14
  declared-green-measured-false + 2 declared-red rows with missing evidence fragments);
  V4's append-only rule adopted in this round's own writers and recorded in the LOG.
- **R57-C1 (operability 9→10)** — see the claim table below.
- **R57-C2 (coverage, held at its L0 cap, predicate met)** — the fourteenth TB2 task grader
  (`largest-eigenval` @ pin `2fd12b88`) read and executed offline: the corpus's first
  wall-clock-performance gate. Sources S205–S208 opened this round (fetch, hash, commit);
  probe instrument `plans/round57_c2_eigen_probe.py` frozen with the prediction table at
  `c0e7e100` BEFORE the first capture run; first run `cases=24 observed_pass=15
  observed_fail=9 mismatches=0 setup=0`, `PREDICATE R57-C2 pass` (receipt
  `corpus/evidence/round57/eigen-probe.txt`, sha256 `4638777…8c784`); grader-class findings
  recorded (exact-but-slow fails; timing-equal is host noise — the two observed-only U cases
  split F/P in one run and flipped F/F on re-run; maximally-wrong wins the speed leg;
  anti-monkeypatch reference capture — a corpus first); maintainer oracle read from
  `solution/solve.sh:14` (`eigenpy.EigenSolver`); knowledge entry + corpus index row +
  PROVINCE coverage row (14 of 89) landed with the probe's registration in wave C
  `44ae8046`.
- **Round-close discipline — including one capture worth naming.** After wave C landed, the
  round's own tip counters caught the wave-C corpus growth tripping two pinned instruments:
  the r50 pointer audit resolves every 40-hex token in SCORECARD/SHONEN/PROVINCE against
  LANE git objects and my PROVINCE section had cited the upstream TB2 pin in full 40-hex
  form (`LAUNDERED round50-c2`), and the r35 coverage checker's stale index expectation
  moved 59→60 with the new knowledge entry (`EVIDENCE-MISSING round35-c1-coverage`) —
  `PREDICATE R55-C2 fail` at tip `44ae8046` (receipt
  `.ufo/waves/round-57/integrate/tipc-entryargv-full.txt`). Fix wave `ca63378d`: the pin
  shortened to the house short form (full sha stays in the SOURCES rows and the oracle
  note, which the audit does not scan), and the red row's fragment honestly refreshed with
  a dated note (60/60, class unchanged — the r56 re-declaration pattern). Both re-verified
  on a scratch clone before landing; the mistake is mined in
  `corpus/lessons/round-57.md`. Final receipts at the close tip `ca63378d` (all four
  counters green) and a fresh re-derivation at the final pushed tip `e8e08b01`; census
  re-validated at round end (exit 0); scratch removed.

## Landed changes (all committed via the treecommit helper, pushed to origin master)

| commit | content |
|---|---|
| `f754593b` | wave A — R56-V1 fix (SKILL landcheck row, ledger landcheck row, R56-F2 source shape), R56-V2/V3/V4 corrections, before-receipts, LOG round-57 entry |
| `c0e7e100` | wave B — claims freeze (`plans/round-57-claims.md`, predictions before first run), probe instrument, TB2 largest-eigenval captures (`corpus/evidence/round57/tb2-eigenval/`), SOURCES S205–S208 (197→201) |
| `44ae8046` | wave C — knowledge entry `tb2-largest-eigenval-grader.md` + README index row + PROVINCE round-57 section (14 of 89), probe registration (SKILL registry row + ledger row, 85/85), SCORECARD round-57 section (C1 admitted 9→10, C2 held 7), LOG measured close, lesson `corpus/lessons/round-57.md`, probe receipts |
| `ca63378d` | close C2 — the tip-C capture fixed (PROVINCE pin to house form; r35 evidence fragment refreshed with dated note), lesson + LOG mistake rows |
| `e8e08b01` | wave E — tip receipts (`.ufo/waves/round-57/integrate/`: the tipc capture, the tipd all-green counters, census-end exit 0). **Final head `e8e08b01` re-derived green**: registry `PREDICATE R52-C2 pass`; landcheck `LANDCHECK PASS n=4`; full entry-truth `executed=85 timeout=0 mismatched=0 evidence_missing=0 laundered=0`, TIPSTATE declared 51g/34r equal to observed, `PREDICATE R55-C2 pass` — the round-56 closure's "re-derive at lane head" now reproduces at the pushed head |

LOG entries: round-57 fix entry + measured close entry (LOG.md, both waves). SCORECARD:
round-57 section + `timing-gate-grader-probe` capability row + round-56 precision-corrections
block + planned round 58.

## Before → after measurements (counting commands, measured at the named commits)

- **R57-C1 (operability)** — before, at base `c9ce9a71` (WSL, clean clone,
  `.ufo/waves/round-57/fix/`):
  `python3 plans/round52_c2_registry.py --lane <clone>` → `ADVERTISED total=83 / REGISTERED
  total=82`, `MISSING plans/round56_landcheck.py`, `PREDICATE R52-C2 fail`, exit 1;
  `python3 plans/round55_c2_entryargv.py --lane <clone> --source <clone> --work <scratch>
  --jobs 6 --timeout 900` → `laundered=2` (`LAUNDERED round52-c2`,
  `LAUNDERED routed-findings`), `PREDICATE R55-C2 fail`, exit 1.
  After, at the round's close tip(s) (`.ufo/waves/round-57/integrate/`): registry →
  `MISSING 0`, `PREDICATE R52-C2 pass`, exit 0; full entry-truth → `laundered=0`, TIPSTATE
  declared equal to observed, `PREDICATE R55-C2 pass`, exit 0 (85 rows executed,
  including the landcheck and the new probe as green ledger rows). Measured revision:
  wave A `f754593b` for the fix; after-receipts committed at `ca63378d` (tipd-*.txt, SOURCE
  rev `ca63378d…`) and re-derived at the final pushed tip `e8e08b01` (same predicate lines).
- **R57-C2 (coverage)** — before, at base: `grep -c 'fourteenth' PROVINCE.md` → 0;
  `grep -c S205 corpus/SOURCES.md` → 0; instrument absent. After: probe
  `python3 plans/round57_c2_eigen_probe.py --lane . --work <scratch> --receipt
  corpus/evidence/round57/eigen-probe.txt` → `cases=24 observed_pass=15 observed_fail=9
  mismatches=0 setup=0`, `PREDICATE R57-C2 pass`, exit 0 (measured at the freeze tip
  `c0e7e100`; second bare run green with the U cases flipped, `.ufo/waves/round-57/claims/
  c2-bare-run.txt`); `grep -c 'fourteenth' PROVINCE.md` → 3;
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 201 (197→201);
  capture sha-refusal kill → `SETUP grader sha256 418ba750… != frozen pin cdc58e3a…`,
  exit 2 (`.ufo/waves/round-57/claims/c2-sha-kill.txt`). Measured revision: freeze tip
  `c0e7e100` (receipt), landing tips `44ae8046` → `e8e08b01` (PROVINCE/SOURCES greps:
  `fourteenth` 3, rows 201 at the final tip).

## Sources & frontier

`SOURCES.md` rows before→after: 197 → 201 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 201; census-validated at round end, exit 0). Rows S205–S208 opened this
round (Gate table in `corpus/lessons/round-57.md`: URL/path, access date 2026-11-01, ≤25-word
located quotes, all four admit tier A; no rejections, no flips of existing rows). C2 is the
round's sourced claim (rides S205–S208 + the receipt). Mistake mining:
`corpus/lessons/round-57.md` `## Mistakes` — two rows (the stale-index `git diff` trap on
this host, captured by a byte-compare against `git show HEAD:`; the byte-stable ledger
insertion's wrong-indent brace bug, captured by the pre-commit `json.load` validation before
any commit landed). Census receipts: round start `.ufo/waves/round-57/census-start.txt`
(exit 0, verdict `ok`, the same 15 pre-existing W04 duplicate-url warnings); round end in the
integrate receipts.

## Trend verdicts

- **expansion: improved** — coverage ground moved where it had not been: the fourteenth
  grader read and executed, and it is a grader CLASS the corpus lacked entirely (a
  wall-clock performance gate — the executed corpus now spans content predicates
  (multiset/membership/regex/service/dual-runtime) and its first cost predicate). Registry
  197→201; frontier count 13→14 of 89; one capability enters
  (`timing-gate-grader-probe`). The score stays 7 by the lane's own standing L0 design
  (`kengaku | round-25/33/51` unanswered) — the expansion is in ground and repertoire, and
  the report says so rather than moving a capped number.
- **quality: improved** — the round's own headline property: the pushed branch tip now
  re-runs its whole advertised self-assessment surface green from one command per counter,
  measured at the tips that carry them (the exact gap the round-56 closure's R56-V1 found
  in r56's close); the writers that landed data this round are byte-stable over existing
  rows; the probe refuses drifted captures (kill measured, exit 2).
- **discernment: improved** — predictions frozen before the first capture run with an honest
  U class for the two cases a static reading cannot decide (and the runs then demonstrated
  the flip empirically — the finding was recorded, not laundered into a prediction);
  the round-56 self-assessment's two overcounting labels corrected by a dated precision
  block at an unchanged score; the V1 fix extended beyond the routed defect to its second
  root cause (the F2 source shape) instead of stopping at the named one.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` (1376 lines; `## Decision table` sections; `## Gate/probe registry` now 85
  rows including the landcheck and the eigen probe, both measured this round)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `LOG.md`
  round-57 entries; the end-to-end domain task is R57-C2: a pinned benchmark grader fetched,
  captured, sha-pinned, executed offline under bwrap against a frozen prediction table, and
  its class-level findings recorded
- `[~]` Instructions executable by an agent without oral context — this round's evidence:
  every measurement ran from committed instructions alone on a fresh clone (`plans/round-57-claims.md`
  → probe runs at the freeze tip; the counters at the close tip), receipts committed
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-57 section
  dated; SF14 re-count corrected in place (R56-V2); the chess/oracle and coverage paragraphs
  remain the operator's surfaces; nothing absorbed (reported out: none)

## Assimilation

`considerthese/` mined (eight files, 2026-10-19…26, unchanged on disk since the round-56
mining): the 2026-10-20 standing round-close-gate proposal is already implemented
(`plans/round_close.py`); the 2026-10-25 tip-receipts proposal is implemented and registered
(`plans/tip_receipts.py`); the 2026-10-26 r52-repair proposal stays refused on its
demonstrated regression. Nothing new adoptable this round. `Assimilation: none — shokuknow
unreachable`.

## L2 floor disclosure (standing)

The batched ≥8-L2 dispatch surface is again unavailable in this session (the standing L0
`kengaku | round-56` remains unanswered; nothing assumed answered). The round routed around
it as before: the frozen instruments' own falsification machinery (the counters at three
tips, the probe's plumbing selftest + sha-refusal kill, the pre-verified fix clone) and the
orchestrator's non-author closure are the adversarial coverage. Ruling still with the
operator.

## Claim sizing (§9)

Both claims are do-nothing-unreachable: C1 requires landing registry/ledger rows and
re-measuring at tips (the committed before-receipts show the same commands red at base —
no-op cannot turn them green); C2 requires live pinned fetches, a sha-refusing offline
executor and bwrap (none exists at base). Not a FRESH-START round; no prior-rejection
spot-check required.
