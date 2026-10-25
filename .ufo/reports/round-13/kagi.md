# kagi — round 13 (calibration 8 → 9)

Repo: `VeigaPunk/kagi-shokunin`, commit **`4b8c018`** (pushed). Working dir at
open: `HEAD` `4391b3b` + the **round-12 set still uncommitted** (the round-12
process never committed; `corpus/op-ref-probe.sh`, `knowledge/op-ref-consumption.md`,
`lessons/round-12.md` and the round-12 `SCORECARD`/`stamps` edits were carried into
this commit, and the round-12 numbers in this report were re-measured before use).

Axis chosen: **calibration** — the recorded next move in `SCORECARD.md` (rounds 11
and 12 both left it partially landed). One axis-move, one verifiable improvement,
before→after recorded.

## Before → after

| Axis | Before | After | Pointer in `SCORECARD.md` |
|---|---|---|---|
| calibration | 8 | **9** | round-13 pre/post tables; `R13-03`, `R11-09` |
| depth | 8 | 8 | `corpus/knowledge/claim-ledger.md` |
| coverage | 8 | 8 | `R11-01`, `R11-11` |
| operability | 8 | 8 | `R13-03`, `R11-09` |
| freshness | 8 | 8 | `R11-04` |
| adjacency | 8 | 8 | `corpus/lessons/round-13.md` |

The five non-moved cells state the increment is claimed under calibration rather
than double-counted, and name their ceilings in the same cell.

## The two holes the round-11 gate had (measured, three ways each)

1. **Forward-only iteration.** `verify` walked rows → commands; nothing walked
   documents → rows. At the dispatch revision, a doc citing the fabricated
   `R13-99` and `R12-88` produced `CITATION_GATE: CLEAN (cites=1 docs=1
   unresolved=0 ephemeral=0 labeled=0)`, exit 0 (labrat lane, `/tmp` copy). Five
   ledger rows (`R11-01/02/04/05/07`) were cited by nothing and nothing could say so.
2. **An unaudited scorecard.** First audit of `SCORECARD.md`:
   `CELL_AUDIT: BROKEN (cells=48 row_pointed=3 stamp_pointed=28 uncited=20 …)`,
   exit 1 — 20 round-table cells whose evidence pointer resolved to nothing.
   Reproduced by four independent code paths (L1 gate; scribe replica
   `ANCHORED_AUDIT: cells=48 row_pointed=3 stamp_pointed=28 uncited=20`; scout
   python census; executor re-implementation).

## What landed

- `corpus/claim-ledger.sh` — `verify` resolves claim ids both ways; new `cells`
  mode; read-side stamp containment; nested-audit refusal + `SKIP-SELF`;
  72-case selftest.
- `corpus/knowledge/claim-ledger.md` — §Class 4 (claim ids), §Class 5 (scorecard
  cells), round-13 before→after table, bounds 17–23, round-13 falsifiers.
- `SCORECARD.md` — round-13 pre/post tables, pointers on the 20 uncited cells
  (row id where the claim is re-runnable, stamped artifact where it is
  historical), one corrected historical number (round-11 pre-move said 21
  runtime shape pins; the count was already 22, pinned by `R11-10`), revised
  `Planned` section.
- `corpus/claim-ledger.tsv` — `R13-01..03` added; `R11-09` and `R12-03` re-pinned.
- `corpus/lessons/round-13.md`, `LOG.md`, `PROVINCE.md`, `corpus/README.md`,
  `SKILL.md`, `corpus/stamps.tsv` (33 rows).

## Evidence (shipped revision)

```
bash corpus/claim-ledger.sh cells
  → CELL_AUDIT: CLEAN (cells=60 row_pointed=25 stamp_pointed=41 uncited=0 missing_ids=0
                       rows_run=14 row_failures=0 stale_pointers=0 self_skipped=3 orphans=0)   exit 0
   pre-move, same command: BROKEN (cells=48 row_pointed=3 stamp_pointed=28 uncited=20)          exit 1
bash corpus/claim-ledger.sh verify
  → CLAIM_LEDGER: CLEAN (claims=17 stamped=33 ids=17 cited=17 labeled_ids=13 orphans=0)          exit 0
bash corpus/claim-ledger.sh citations
  → CITATION_GATE: CLEAN (cites=700 docs=43 unresolved=0 ephemeral=0 labeled=13)                exit 0
bash corpus/claim-ledger.sh --selftest
  → SELFTEST: PASS (72 cases)                                                                   exit 0
```

Siblings unchanged (re-run this round): `DRIFT_PINS: CLEAN (files=15 symbols=20)`
+ `DRIFT_SELFTEST: PASS (13 cases)`; `SURFACE_CENSUS: CLEAN (assets=20 runtime=15
scanned=4 ok=34 absent=2 skipped=0)` + `--verbs CLEAN (pass=7 skip=3)` +
`SELFTEST: PASS (16 cases)`; `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5
warns=2)` exit 1 by design; `OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7
divergent=5 edge=10 sig=6)` + `PASS (29 cases)`.

## The defect this round found in its own first implementation

The first `cells` pointer test was an unanchored substring match
(`grep -qF "token<TAB>"`). Every scorecard cell carries a bare score digit, and a
stamps row carries sha256/line/byte fields — so `7<TAB>`/`9<TAB>` matched *inside
a hash or a counts column* and the gate printed
`CELL_AUDIT: CLEAN (cells=48 row_pointed=3 stamp_pointed=48 uncited=0)` exit 0
against a scorecard with 20 unpointed cells: a false clean of the round-11 critic
CE1 class. Caught by a throwaway token probe (`HIT [7]`, `HIT [9]`) against the
scribe lane's independent replica (which said `stamp_pointed=28`). Fixed by
loading stamp rows into arrays and comparing the first field exactly; pinned by
selftest case `cells-numeric-anchored`. A second part of the same class: the
first draft's `section_check` used the same variable for the doc-set membership
flag, so `cells --scorecard/--docs` died `sec_head: unbound variable` (caught by
the drafting lane, fixed before landing).

## L2 wave (12 lanes; two batched calls — the first payload was malformed)

planner, connector, 2 scouts, 3 executors, reviewer, critic, sentinel,
mutation-tester, labrat, scribe. What each attack produced:

- **critic** (executed): a `calibration | 9 | R11-10` cell was CLEAN while
  `R11-10` only counts `state-shape.tsv` rows, and a poisoned stamp row
  (`deadbeef/0/0`) was CLEAN under membership-only. **Both real** → the two teeth
  (re-run cited rows, re-compare cited pins) were added; the residual (a pointer
  can be irrelevant to the score) is the stated calibration ceiling, and the
  report does not claim the rule verifies evidence.
- **mutation-tester** (executed): `R12-03a` resolved as `R12-03`; `**Depth**` /
  `Depth (owned)` silently skipped an axis; a comment-only id defeated a naive
  grep; a stamped-but-deleted path passed. **All real** → whole-word id
  extraction, exact array membership, comment-skipping row load, six-axis
  completeness rule; five selftest cases.
- **planner**: acceptance command list, T1-1 (fence-blind id scan), T2-1
  (partial axis drift) → zero-cell/vacuity exits and the six-axis rule.
- **sentinel** (31 probes): 7 dispatched classes NOT-reachable on the landed code
  (no eval on tokens, equality-based lookups, `/etc/passwd` refused before
  parsing, every empty-input class exit 2). Two **WARNs adopted**: stamps
  read-side containment asymmetry (`../outside.txt` row → hash oracle + a cell
  pointing outside the root) and round-heading drift (`## Round 1 pre-move`
  dropping six cells silently) — both now exit 2, both pinned by selftest.
- **scribe**: the `in_set` clash (5 failing cases) and the **recursion** question
  — a scorecard cell may cite a row that runs this gate. Adopted as a bound:
  `verify` refuses a nested self-audit, `cells` skips self-invoking rows
  (`SKIP-SELF`, counted). Consequence: the ledger cannot pin its own `verify`
  summary; `R13-03` pins the `cells` summary.
- **reviewer**: 12 of 13 round-12 numbers VERIFIED; caught a
  `lineno: unbound variable` crash in a **mid-edit** revision (never shipped) and
  reported the stamp mismatch of the moving script honestly.
- **labrat**: the before-state proof used as this report's before-evidence.
- **scout (census)**: every id token, the five orphans, the unpointed cells with
  line numbers — identical to the gate's numbers.
- **executor** (independent implementation): converged on the same semantics and
  gave the fourth reproduction of `uncited=20`.
- **connector**: sibling overlap (see §Adjacency).

## Bounds (why 9, not 10)

- A pointer's **relevance** to the score beside it is not machine-checkable; the
  audit buys resolvability + freshness, not semantics (critic's counterexample).
- `row_pointed` (25) vs `stamp_pointed` (41): most cells still rest on a
  hash-pinned revision rather than a re-run command. The next falsifiable target
  recorded in `SCORECARD.md`: raise `row_pointed` above half the cells by adding
  rows that measure the quantities the historical cells assert.
- The ledger cannot pin its own `verify` summary (nested-audit refusal).
- Scores remain author-assigned; only the pointers are machine-checked.
- Nothing schedules any of the five gates (operator-scope ceiling, unchanged).

## Adjacency (reported, not absorbed)

kumitate `round-gate.mjs` and kotoba `verify_corpus_integrity.py` resolve **commit**
ids; kengaku `grader.py` scores predictions in a table; kasegi's checker source
lives outside the sibling checkout. None implements an `R…-…` row-id or
score-cell contract, so this round duplicates nothing — a shared "a cited id must
resolve" contract stays with the integrator. The already-reported dead pointer
(`.ufo/reports/round-8/aggregator.md`, three tokens in
`corpus/lessons/round-8-aggregator-box3-coldrun.md`) is unchanged and still
labelled where cited.

## Hygiene

No vault access, no `op` vault/item read, no handler start/stop, no CDP/Chrome,
no real `op.env` value read; `OP_*` values in dry runs were fabricated. No secret
value, vault ref path, account value, or private-file hash in any artifact. All
L2 execution was scratch-only (`/tmp/kagi-r13/…`), and the only repo writes were
the L1's.