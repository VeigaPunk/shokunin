# kagi — round 14 (freshness 8 → 9)

Repo: `VeigaPunk/kagi-shokunin`, commit **`round-14`** (pushed). Working dir at
open: `HEAD` `4b8c018` (round-13 close, clean tree).

Axis chosen: **freshness** — the lowest-scoring axis this lane owns, tied at 8
with depth/coverage/operability/adjacency. One axis-move: the *knowledge surface*
(the lane's actual product) gets a re-verification link, machine-checked. The
round also resolves the plan round 13 left open (see §"The round-13 plan"), which
is recorded as a calibration increment, not a second move.

## Before → after

| Axis | Before | After | Pointer in `SCORECARD.md` |
|---|---|---|---|
| freshness | 8 | **9** | round-14 pre/post tables; `R14-01`, `R11-09` |
| calibration | 9 | 9 (increment recorded) | `R14-01`; the H/N/R census in `corpus/lessons/round-14.md` |
| operability | 8 | 8 | `R11-09` (72 → 94 cases) |
| depth | 8 | 8 | `corpus/knowledge/claim-ledger.md` §Class 6 |
| coverage | 8 | 8 | `R11-01`, `R11-11` |
| adjacency | 8 | 8 | `corpus/README.md`; `corpus/lessons/round-14.md` |

The five non-moved cells say in-cell that the increment is claimed under freshness
and name their ceilings.

## The pre-state (measured three ways at the frozen revision)

At `4b8c018`, over the 17 `corpus/knowledge/*.md` entries:

- **1 of 17** named any claim row at all (and that one also cites the illustrative
  `R13-99`); **0 of 17** declared any re-verification
  (`grep -c '^Reverify:' corpus/knowledge/` ⇒ `0`); **10 of 17** were not in
  `corpus/stamps.tsv` (7 knowledge entries pinned of 17).
- Reproduced independently: the L1 census, the pre-state scout's python census
  (frozen blobs *and* live tree), the drafter's `grep`. The scout also corrected
  two of my dispatch numbers — the scorecard has **5 pre + 5 post** sections, not
  6 + 4, and `stamp_pointed=41` is not "stamp-only cells = 35".

The landed gate measured the same gap itself: `DOC_AUDIT: BROKEN (entries=17
row_linked=0 by_hand=0 undeclared=17 missing_ids=0 unpinned=10
duplicate_reasons=0 floor=9)`, exit 1.

## What landed

- **`corpus/claim-ledger.sh` — sixth mode `docs`.** Every `corpus/knowledge/*.md`
  entry must carry exactly one declaration at column 0 —
  `Reverify: R11-04, R11-05` (every id must resolve) or
  `Reverify: by-hand: <class> — <reason>` with a **closed** class set
  (`control-plane-scratch|opencode-internal|interactive-only|vault-refusal`) and a
  **unique** reason of ≥24 characters — and must be a row in `corpus/stamps.tsv`.
  `UNDECLARED` / `MISSING-ID` / `UNPINNED` / `DUPLICATE-REASON` and a corpus where
  `row_linked*2 < entries` (floor `ceil(n/2)`) are exit 1; shape errors (no
  entries, a second declaration, a malformed `Reverify` line, unknown class,
  short/padded reason, hidden entry, bad entries dir) are exit 2. Selftest
  72 → **94** cases.
- **17 declarations** — 14 row-linked, 3 by-hand
  (`config-layering` `opencode-internal`; `control-plane-hardening`,
  `handler-trust-boundary` `control-plane-scratch`). Two independent L2 drafts
  agreed with each other on the 14/3 split and with me on 14 of 17 row sets.
- **All 17 entries stamped** — pin set 33 → **44** rows; the three by-hand entries
  were among the ten that had never been pinned.
- **Five score-card pointers** — the reachable half of round 13's plan (see
  below): the round-10 coverage/calibration/operability and round-12
  freshness/coverage cells now cite `R11-01`, `R11-03`, `R11-09`, `R11-04`,
  `R11-01`, the rows that re-run the commands those cells' **own Evidence columns
  already quoted**.
- **Ledger rows**: `R14-01` (`bash corpus/claim-ledger.sh docs`) plus four counted
  rows re-pinned because this round moved their quantities — `R11-09` (72 → 94),
  `R12-03` (33 → 44), `R13-01` (10 → 12 sections), `R13-02` (17 → 18 rows).
- Docs: `corpus/knowledge/claim-ledger.md` §Class 6 + bounds 17–23 + a Round-14
  before→after table, `SKILL.md`, `PROVINCE.md`, `corpus/README.md`,
  `SCORECARD.md`, `LOG.md`, `corpus/lessons/round-14.md`.

## The round-13 plan: split, not merely falsified

Round 13 asked for `row_pointed` ≥ half the checked cells by adding rows for the
quantities the *historical* cells assert. I first wrote that off as unreachable —
**and a lane falsified me.** Two measurements with different rubrics:

- critic (executed): **0 of 35** row-less cells where a *newly written* row would
  honestly support the score beside it;
- pre-state scout (own census): **11 H / 19 N / 5 R** (+2 borderline) — and its
  five are cells whose **Evidence column already quotes a live command**;

so the *ratio* half was reachable exactly at the boundary (25 → **30 of 60**), and
the other half (rows re-deriving historical numbers) stays refused as pointer
inventory. The five pointers are cited this round; `row_pointed` is now **38 of
72** and the round-13 half-floor is met rather than argued. The correction is
recorded in `corpus/lessons/round-14.md` §"The round-13 plan" and in
`SCORECARD.md` — an author sentence about what is *unreachable* is itself a
measurement.

## Evidence (shipped revision)

```
bash corpus/claim-ledger.sh docs
  → DOC_AUDIT_RATIO: row_linked=14/17 floor=9 by_hand=3 duplicate_reasons=0
  → DOC_AUDIT: CLEAN (entries=17 row_linked=14 by_hand=3 undeclared=0 missing_ids=0
                      unpinned=0 duplicate_reasons=0)                                    exit 0
   pre-move, same mode, same corpus: BROKEN (entries=17 row_linked=0 by_hand=0
                      undeclared=17 … unpinned=10 floor=9)                              exit 1
bash corpus/claim-ledger.sh verify
  → CLAIM_LEDGER: CLEAN (claims=18 stamped=44 ids=18 cited=18 labeled_ids=17 orphans=0)  exit 0
bash corpus/claim-ledger.sh cells
  → CELL_AUDIT: CLEAN (cells=72 row_pointed=38 stamp_pointed=47 uncited=0 missing_ids=0
                       rows_run=14 row_failures=0 stale_pointers=0 self_skipped=4
                       orphans=0)                                                        exit 0
bash corpus/claim-ledger.sh citations
  → CITATION_GATE: CLEAN (cites=734 docs=45 unresolved=0 ephemeral=0 labeled=13)         exit 0
bash corpus/claim-ledger.sh --selftest
  → SELFTEST: PASS (94 cases)                                                            exit 0
```

Siblings unchanged (re-run this round): `DRIFT_PINS: CLEAN (files=15 symbols=20)`
+ `DRIFT_SELFTEST: PASS (13 cases)`; `SURFACE_CENSUS: CLEAN (assets=20 runtime=15
scanned=4 ok=34 absent=2 skipped=0)` + `--verbs CLEAN (pass=7 skip=3)` +
`SELFTEST: PASS (16 cases)`; `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5
warns=2)` exit 1 by design; `OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7
divergent=5 edge=10 sig=6)` + `OP_REF_SELFTEST: PASS (29 cases)` (the ledger's own
`verify`/`cells` runs execute this gate; it execs `op run` over **generated
fabricated plain values** and refuses any op-side ref token before exec — the
no-op-execution rule held for every lane, and the gate is unchanged since
round 12).

## Defects this round found in its own first implementation

Each by execution, each now pinned by a case:

| Defect | How it surfaced | Fix |
|---|---|---|
| `nrows: unbound variable` on the `UNDECLARED` path under `set -u` | the live run printed `UNDECLARED` and then aborted; the case for that message **passed anyway** | counters initialised before the branch; the case upgraded to assert the exact `DOC_AUDIT: BROKEN …` summary (`tcase_last`) |
| a directory of only hidden entries reported "no entries" instead of naming the hidden file | selftest `docs-hidden-entry` failed | hidden-entry refusal moved before the empty-surface refusal |
| a fabricated declared id was counted in `row_linked` | scribe lane fixture `Reverify: R11-04, R99-99` ⇒ `MISSING-ID` **and** `row_linked=2` | `row_linked` counts only resolving ids; summary pinned for that fixture |
| a 24-space by-hand reason passed the ≥24-char floor | mutation lane's predicted class, implemented and executed | reason trimmed before measurement (`docs-padded-reason`) |
| a `Reverify`-prefixed line that is not a declaration read as `UNDECLARED` | planner lane | count comparison refuses it (exit 2, `docs-malformed-line`) |
| 17 identical by-hand reasons satisfied the rule | critic lane's executed fixture | `DUPLICATE-REASON` (case-folded, whitespace-collapsed) |

Process note, recorded because it will bite other lanes: two of my own `edit`
calls **deleted a `##` heading** in three entries by anchoring on a heading and
not reproducing it in the replacement; a post-edit heading census caught it and
all three were restored.

## L2 wave (14 lanes, one batched dispatch)

planner, connector, 2 scouts (entry evidence, pre-state), scribe, 2 executors
(mode draft, declaration draft), reviewer, critic, sentinel, labrat,
mutation-tester, simplifier, distiller. The distiller's first pass found no
artifacts, said so instead of inventing a synthesis, and was revived after the
wave. What each attack produced:

- **critic** (executed): identical by-hand reasons ⇒ CLEAN; an unrelated-but-
  resolving row ⇒ CLEAN; **0 of 35** row-less cells have an honest *writable* row;
  the forbidden sentence ("every score is now machine-verified") is named and is
  not written anywhere in this round's docs.
- **pre-state scout**: independent pre-state (17/7/1/0), cells 60/25/41, the
  5+5 section split, "stamps.tsv has no header line", and the falsification of my
  unreachability claim (25 → 30 reachable).
- **entry-evidence scout**: a per-entry verdict table with the criterion *"declare
  a row iff its verdict changes when the entry's asserted fact changes"*; it
  **rejected three of my draft links** (`R11-10` for `janitor-lifecycle` and
  `op-env-refs` — a pin-file row count is not a host fact — and `R11-06` for
  `handler-on-disk-state`) and added four (`R11-08`, `R11-01`, `R11-02`, and
  `R11-10`+`R11-11` on `surface-census`). All adopted.
- **declaration drafter** (independent): same 14/3 split, five disagreements; used
  as the second opinion (my superset kept where the two diverged, e.g.
  `op-env-refs` keeps `R12-01`).
- **mode executor** (independent implementation): 18 cases + a documented
  ambiguity list; mined for cases. Its one real divergence is recorded rather
  than smoothed: it accepted `Reverify:by-hand: …` after trimming, the shipped
  code requires the `Reverify: ` spelling and refuses the rest loudly (exit 2).
- **mutation-tester**: 18 mutations, all surviving at its (pre-`docs`) revision,
  which is the expected result at that revision; its demanded cases — malformed
  line, padded reason, hidden entry, ratio floor **and** boundary, summary-order —
  are all shipped.
- **labrat** (executed): the cheapest `docs` CLEAN path — 9 entries on one broad
  row, 8 unique by-hand reasons, all stamp **members**; a fabricated `deadbeef`
  stamps row passes `docs` and fails `verify`. Adopted as bounds 19/20
  (membership vs freshness; the floor is coverage, not evidence).
- **sentinel** (31 probes): no reachable vulnerability; the zero-entry case must be
  exit 2 per the existing setup convention — implemented; its `..`/absolute stamps
  probes are covered by the existing cases.
- **simplifier**: delete the per-entry `ENTRY …` detail lines. **Dissent
  recorded, not adopted** (17 lines of output are what make the by-hand set
  visible without opening 17 files); everything else kept.
- **reviewer**: the landing-invalidated number table (17→18 rows, 33→44 stamps,
  PROVINCE/README/claim-ledger.md lines) + six already-stale historical numbers,
  and the warning that the post-landing case count **must be taken from the tool**
  — which is why `R11-09` was re-pinned from the run (94), not from a guess.
- **planner**: exit-1/exit-2 classification review, acceptance ordering, and the
  mid-flight spec divergence (`DUPLICATE-REASON`, extra summary fields, case
  counts) — recorded as a revision fact; every lane named the hash it read.
- **scribe**: §Class 6 draft + doc deltas + the honest "what this does not prove"
  paragraph (its stamps count 43 → 44 corrected).
- **connector**: sibling doc-coverage verifiers (see §Adjacency).
- **distiller**: revived post-wave; its merge surfaced the D4 correction that
  changed this report's framing of the round-13 plan.

## Bounds (why 9, not 10)

- **A declaration is a pointer, not relevance** (bound 17). `docs` proves a link
  exists and the row is live; it does not prove the row measures the sentences
  beside it, and coverage is partial by construction — the entry review named the
  sentences no row touches (`cdp-bridge`'s open-popup/version lines,
  `op-cli-surface`'s version/signed-out state, `janitor-command-surface`'s
  dispatcher/flock facts, `handler-on-disk-state`'s row counts — re-printed by
  `R11-01`, not pinned by it, `transcript-hygiene`'s `--classify` triage).
- **The ratio floor is coverage, not evidence** (bound 19): nine entries on one
  broad row satisfies it (labrat, measured).
- **The by-hand class is an explicit unverifiable set** (bound 18), not proof of
  effort; the uniqueness check catches the cheapest rubber stamp only.
- **`docs` checks membership; `verify` checks freshness** — a fabricated stamps row
  passes `docs` and fails `verify` (labrat, measured).
- Pending: nothing schedules any of the six gates (operator-scope ceiling,
  unchanged).

## Next target (recorded in `SCORECARD.md`, falsifiable)

Push `by_hand` from 3 → ≤1 **without weakening the class rule**: find a
row-shaped re-verification for one of `config-layering`,
`control-plane-hardening`, `handler-trust-boundary` — a committed script for the
`opencode debug` resolver, or a scratch-serve matrix that exits with a verdict —
and the `DOC_AUDIT_RATIO` line is the number that has to move.

## Adjacency (reported, not absorbed)

The connector lane mapped sibling documentation-coverage verifiers, all
**adjacent** — different unit, none binds an entry to a re-runnable claim row:

| Sibling | Verifier | What it links |
|---|---|---|
| kotoba | `verifiers/verify_skill_checklist.py` | SKILL checklist box → check id / disposition (two-way map parity) |
| kotoba | `verifiers/verify_corpus_independent.py` + `verify_corpus_integrity.py` | corpus Markdown → README index row |
| kumitate | `scripts/proxy-check.mjs` | doc/registry fractions inside a composite coverage score |
| kasegi | `corpus/instruments/anchorcheck.py` | mirror `path:line` anchors in range |
| kengaku | `grader.py` | hard-coded report tables replayed against committed bytes |

The shared-contract question ("does a lane need a written rule that every
documented claim names a re-runnable command?") stays with the integrator. Also
unchanged: `.ufo/reports/round-8/aggregator.md` stays a labelled dead pointer in
`corpus/lessons/round-8-aggregator-box3-coldrun.md`, owned by the aggregator.

## Hygiene

No vault access, no `op` vault/item read, no handler start/stop, no CDP/Chrome,
no real `op.env` value read; `OP_*` values in probes were fabricated. No secret
value, vault ref path, account value, or private-file hash in any artifact. All L2
execution was scratch-only (`/tmp/r14/…`); the only repo writes were the L1's.