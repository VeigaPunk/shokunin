# fleet report — lore r91 (round-91, world-bible lane)

Lane: `lore-shokunin` · Repo HEAD measured: `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (`c2ab3d0`).
Baseline: `a7c6a1773d5994246a76e4eff30d645f161920e0` (`a7c6a17`, r90 closure).
Wave: work wave `.ufo/waves/round-91/` — 33 seat reports + `wave-spec.md` (34 `.md`) + `wave-spec.json`
+ 22 `patches/` artifacts — landed as `6332115` (76 files, +11136/−227) + amendment `c2ab3d0`
(2 files, +18); follow-up judging wave `.ufo/waves/round-91/followup/` — 32 `.md` reports + 21 JSON
receipts/companions (53 files), all untracked at this snapshot.
**Snapshot cutoff for this report: `2026-10-17T08:47:26-03:00`, 53 follow-up files.** Every
measurement below is taken on the delivered tree at `c2ab3d0`; sibling figures are attributed.
Written by seat **P3** (follow-up) under explicit parent authorization; the round's `P1` seat never
delivered an artifact (SE2 F2: `.ufo/reports/round-91/lore.md` absent at 08:36, no duplicate
anywhere) — this file closes that gap. The umbrella MANIFEST `rounds[]` entry and its commit remain
owed (outside this writer's authorization).

Tree state at measure: HEAD `c2ab3d0` at every check; `git status --porcelain` = only the untracked
`followup/` directory; no seat committed; `git rev-list --left-right --count origin/main...main` →
`0 12` (12 ahead, 0 behind) — **no push**. `git diff --name-only a7c6a17 c2ab3d0 | wc -l` → 77
(20 under `corpus/`, 57 under `.ufo/`).

Protocol checks (this seat, two 60 s wait-checks then work with what exists): #1
`2026-10-17T08:33:34-03:00` (1 artifact: `H4-probes.json`); #2 `08:34:34` (+ `H4-c1-discrimination.json`,
`H4-census.json`, `H4-lineage.json`, `JCAL5-delta.json`). The wave completed during the seat: 53
files by 08:47.

**Axis verdicts: `ruled` — the setter of verdicts is L1.** Judge recommendations on record:
JAXIS's follow-up synthesis (read in full; recommendation only) grades **calibration improved
(bounded)**, **coverage improved (bounded)**, **depth harmed (bounded) at the delivered tree** —
becoming improved (bounded) only after its repair set R1–R3 — and offers two admission modes:
**A. repair, then admit (recommended)**; **B. admit with recorded harm** (record depth harmed while
the boundary-document condition stands; do not net C1/C2/C3 gains). P2's SCORECARD draft proposed
improved for all three and differs on depth; CAL judges (JCAL1/2/3/5, V2) propose calibration
improved with bounds. No harm was measured on the calibration or coverage surfaces themselves. All
bounds/debts below are recorded, not netted.

## Work performed

Three claims were declared for round 91 (`.ufo/waves/round-91/wave-spec.md`), one per owned axis;
the declared roster is 32 seats but names 30 (Q2: 2 unnamed declared slots, `CB-prep` reportless,
`CB1` unrostered; delivered 33), and the spec's landing record (W1) covers a
`07:36:41-03:00` cutoff where 15 of 30 named seats had any artifact.

- **C1 — calibration**: two durable DISCRIMINATING fixtures (a null-chain fixture whose output
  differs between the `e97613c` checker and the delivered checker, and a tick-under-genuinely-
  unresolved-holder fixture whose tick line differs while its chain-break stays qualified) so a
  silent revert of either r90 repair fails the census; the shipped-checker hash + the C9
  falsification trigger pinned in `corpus/knowledge/r91-c9-watch.md`.
- **C2 — coverage**: harden the support command against the two r90-found silent-failure vectors —
  expected-inventory assertion, distinct-anchor/duplicate-row reporting, JSON-FACTS/EDITORIAL receipt
  split.
- **C3 — depth**: decide JDEP2's three prospective edges — R8 failed-gate disposition + withhold
  precedence, R9 reprint boundary + reliability criterion, R10 `source_id` namespace scoping — each
  with owner, trigger, and worked example.

Seat roster (work wave): C1 B1/B2/B3 census, S1 watch design, X1/F2 fixture authors, C5/C6/C8/C10
critics+verifier, E1 wording, CB1 (unrostered boundary audit); C2 M1/M2/M4/M6 hardening, M3 map
wording, S2 scout, C7 discipline, K1 connector, V1 freeze verifier; C3 D1/D2 edges, T1 verifier,
R1 reviewer, J3 register, E2 wording; record W1/W2/Q1/Q2/SE1/SE4. Follow-up wave (25 seats'
artifacts at snapshot): H1–H5, JCAL1–3/5, JCOV1–4, JDEP1–4, CB1, E1, K1, P2, P3, P4, Q1, Q2, SE2,
V2, W1.

## Landed changes

- **C1 — `corpus/fixtures/r91-c1-null-chain/` and `corpus/fixtures/r91-c1-tick-unresolved/`** (each
  README + 5 section JSONs) and **`corpus/knowledge/r91-c9-watch.md`**. Commit `6332115`.
  Checker deliberately untouched (r91 is not a new generation).
- **C2 — `corpus/tools/support_check.py`** (M2+M6 stack; +125/−23 in the diff) and
  **`corpus/tools/README.md`** (contract + two named M2 deviations, +13/−1); the two cluster maps
  and the r89 paraphrase demo's Inventory line (`c2ab3d0` +4) adjusted to the hardened contract.
- **C3 — `corpus/knowledge/r88-sourced-inspiration-decision-table.md`** +63 lines at the two
  commits: R8 failed-gate disposition + withhold-scope precedence, R9 reprint boundary (owner,
  trigger, decision, worked example, embedded verification command), R10 namespace scoping.
- **Boundary doc — `corpus/knowledge/holder-assessment-boundary.md`** reconstructed in `6332115`:
  the r90 closure had committed CB1's r90 *instruction sheet* as the tracked contract; the
  reconstruction rebuilds from the r89-landed base. See the forensics below — real repair, but
  spliced/partially applied and graded harmed vs its declared target by the follow-up.
- **Wave evidence** — `.ufo/waves/round-91/` (33 seat reports + spec + `wave-spec.json` + 22
  patches), commits `6332115` + `c2ab3d0`. `wave-spec.json` is the fleet's first (r90-Q2-P2 partial;
  no `seats[]`/`amendments[]`/validator — Q2).
- **Not committed:** the entire `followup/` wave (53 files, untracked); no push, no sibling-repo
  write, no registry write.
- **Round record:** `git diff --stat a7c6a17 c2ab3d0 -- PROVINCE.md SHONEN.md LOG.md SCORECARD.md`
  → empty. Proposals only: `followup/P3-log-r91.md` (LOG; supersedes W2's pre-delivery draft),
  `followup/P2-scorecard-r91.md` (+`P2-verdicts.json`), `followup/P4-shonen.md`. No
  `l0-questions.md` append (K1: no r91 L0 need; K1.md receipts). **`corpus/tools/__pycache__/` is
  now named in `.gitignore`** (r90-closure repair; Q89-044 closed) — a transient appeared during
  the r91 follow-up window and was swept.

## Before → after measurements

All commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless noted.

### Freeze — the r91 checker is unchanged

```sh
sha256sum corpus/fixtures/check_bible.py
git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum
git show c2ab3d0:corpus/fixtures/check_bible.py | sha256sum
git diff --stat a7c6a17 c2ab3d0 -- corpus/fixtures/check_bible.py
```

Observed: all `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; diff empty; the
watch's pinned hash matches. Corroboration: H4 (9 generations × 5 r85 probes; `r90closure_eq_r91:
true`, `r91_new_generation: false`; all five probe outputs byte-identical `c2ab3d0` vs `a7c6a17`;
two control probes still receipt-exact), V2, JDEP4, JCAL1/2/3/5, H1, K1. Baseline checker at
`e97613c` remains `e2bb9639…`.

### Census — 0 changed + 2 new of 166, 0 exit changes

```sh
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/p3r91/census.py   # 166 subprocesses
```

```text
DELIVERED_CENSUS dirs=166
exits={0: 32, 1: 134} violations=421 stderr_nonempty=0
baseline_paths=164 changed=0 []
added=['corpus/fixtures/r91-c1-null-chain', 'corpus/fixtures/r91-c1-tick-unresolved']
b2_agree=164/164   exit_changes=[]
NEW null-chain {'exit': 1, 'stdout_sha256': '615dc056…', 'violation_count': 1}
NEW tick-unresolved {'exit': 1, 'stdout_sha256': 'd754e96f…', 'violation_count': 3}
```

Reproduced independently by H3 (whole-corpus scan: only the two new dirs differ between `e97613c`
and delivered stdout; 0 exit diffs), H4 (`H4-census.json`, against B1's manifest sha `5433f6af…`),
JCAL1 (2×, plus a baseline-checker-on-head replay), JCAL5 (3rd method + replicate), V2, JDEP4, P2.
Wording precision (SE2 F3 / JAXIS): "0 changed" is **tuple-level** — 3 inert editorial `.md` edits
inside pre-existing fixture dirs do not move any checker tuple (`check_bible.py` reads section
JSONs only).

### C1 — discrimination on the two new fixtures

`e97613c` checker vs delivered, identical invocations, exit 1, empty stderr:

- `r91-c1-null-chain` — before: `… possible provenance chain break, not a definite identity
  mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable
  (0 raw entity rows carry this id, but only 0 is in the resolved index)`; after:
  `provenance chain break; expected from_holder 'mira', got None`.
- `r91-c1-tick-unresolved` — before tick line hedged by holder identity; after:
  `provenance tick 1 must be greater than previous tick 3`, while the separate chain-break line
  (`… 'f3-dup' is not uniquely resolvable … got 'mira'`) is byte-identical across checkers.

Both READMEs declare both blocks, byte-exact (H4/JAXIS/P4/V2/H5 verified 4/4 blocks). Revert
controls: JCAL2's X3-revert flips only the tick fixture back to the `e97613c` bytes; X2-revert only
the null fixture; V2's hybrids same (one dir each); JDEP4-check: `DISCRIMINATION HELD` exit 0 vs
`REGRESSION-DETECTED` exit 2 — a runnable companion. The C9 watch pins the hash, restates the
integer-only ruling, and states a four-gate falsification trigger + probe (S1 → next C1 owner);
JCOV4/V2 note the watch keeps placeholder paths and omits the `e97613c` hash (bounds CAL-D2).

### C2 — support command receipts and controls

Delivered receipts (this seat + JCOV1/P2/P4/JAXIS): r87 `INVENTORY JSON-FACTS 14/14;
EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22 … SOURCE-SUPPORT 14/14;
EDITORIAL-ANCHORS 8/8; … MODES 22/22; VALIDATED-ROWS 22/22 — RESULT PASS` exit 0; r88-m3 `10/10 …
6/6; repeated-references=4; DUPLICATE-ROWS 0 … SOURCE-SUPPORT 10/10 … WARN: unreferenced excerpt
declaration: source-excerpt.md (mode=verbatim) — RESULT PASS WITH WARNINGS` exit 0; demo
`SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors) — RESULT PASS` exit 0.

Negative controls (this seat's scratch copy of the demo, swept; JCOV1/P2/JCOV2/JCOV4 add more):

```text
missing inventory line          → exit 2  FAIL: map must contain exactly one expected inventory declaration
renamed "## JSON facts" heading → exit 2  FAIL: fact table must be under a JSON facts or Editorial rows heading
duplicated mapped row           → exit 1  INVENTORY JSON-FACTS 2/1; TOTAL-ROWS 2/1; DUPLICATE-ROWS 1;
                                          FAIL: duplicate mapped row entities.json#/0/claims/0 appears 2 times
```

JCOV1 additionally reproduces the integration exactly: `M2+M6` applied on a `a7c6a17` extraction is
byte-identical to the delivered `corpus/tools/` files, including the `c2ab3d0` +4 fixup. Bounds:
inventory is self-attested (COV-D1); the two M2 contract deviations are README-named, not fixed
(exit 2 on missing inventory vs S2's expected 1 + `RESULT FAIL`; no terminal failure summaries);
the check is a lexical preflight; the r88-m3 WARN is declaration-conditioned and the two Spence
comparisons are bullets, not rows (r92).

### C3 — the decided edges

`git diff a7c6a17 c2ab3d0 -- corpus/knowledge/r88-sourced-inspiration-decision-table.md` → 63
changed lines: R8 failed-gate disposition + `Withhold-scope precedence (decided r91)`; R9
`reprint boundary clarified r91` (owner/trigger/decision/worked example + embedded verification
command, `11/11` exit 0 on the delivered table); R10 `Namespace scoping (decided r91)`; live
register correctly absent (`corpus/knowledge/cross-cluster-contradictions.md` does not exist;
absence alone is not proof of correct emptiness — W2). Integration drops named by JDEP1/JDEP2:
R8/R10 lack spec-form Owner/Trigger/Worked-example labels; R8's inseparable/constitutive branch and
R10's deliberate-convention gap dropped (DEP-D2/D2b).

### Boundary doc — mis-landing confirmed, reconstruction forensics

```sh
for rev in e97613c ca7f9ef a7c6a17; do git show $rev:corpus/knowledge/holder-assessment-boundary.md | sha256sum; done
sha256sum corpus/knowledge/holder-assessment-boundary.md
git diff --stat e97613c ca7f9ef -- corpus/knowledge/holder-assessment-boundary.md   # empty
```

- `e97613c` = `ca7f9ef` = `a4b1b331…` (630 lines): the r90 work wave never refreshed the doc.
- `a7c6a17` = `0d42c988…` (316 lines) and byte-identical to `.ufo/waves/round-90/followup/
  CB1-boundary-refresh.md` — the r90 closure committed CB1's **instruction sheet**
  (`# CB1 — Boundary-doc refresh proposal…`, `Status: proposal only`) as the tracked contract.
- delivered `c2ab3d0` = `c0c59daf…` (549 lines): contract title back, instruction sheet gone,
  reconstruction banner `:3-6` naming base `e97613c`, set `D1–D13`, and one skipped item
  (`D1 — Decision-table row 2 code refs.`).

Follow-up grading (CB1 audit + H1/H5/P4/V2/JAXIS, all read): **9 of 13 sheet blocks landed
verbatim**, 5 prescribed items unapplied (D4 header/banner, D6/D7 anchor remap, D1 row 2, D9
second range, D13 labels) + D2's new bullet absent, while only 1 is named; 3 headings lost
(`The contract`, `Commands`, `Status split`) with dangling `"Commands"` references; 12–13
`Precise limits` bullets lost (content regression, `R91-CB1-LIMITS-LOSS`); a duplicate
contradictory decision-table row (`:179` retired vs `:184` current); 35 unlabeled stale anchors
(14/26 needle tests fail, `:429-430` still pins the superseded `e2bb9639` as "delivered"); 4+
splice/duplicate sites (`:1`/`:8` double H1, `:37-41`, `:46-56`, `:121-135`, `:227-243`).
Sound: 7/7 fenced blocks byte-identical to `ca7f9ef`, and the r85 five-case replay still matches
the delivered checker (CB1 live receipt; this seat's spot checks agree). **JAXIS-only finding:**
the surviving D11 paragraph (`:394-397`) still says the null-chain definite form has no fixture
"and is not owed" — contradicted by the two fixtures shipped in the same commit. CB1's verdicts:
doc-state fidelity vs target **harmed** (improved vs `a7c6a17`), reconstruction accounting
**harmed**, internal coherence **harmed**; E1 likewise grades prose consistency harmed (bounded).
Repair path (CB1/JAXIS R1): re-derive from `git show ca7f9ef:…` applying the sheet by anchor
(replace, not insert-before); do not patch the delivered file in place.

### Round record, SHONEN, province, process

- Round record surfaces unchanged at `c2ab3d0` (see Landed changes). LOG/SCORECARD/SHONEN proposals
  exist only as follow-up drafts. `SHONEN.md` unchanged; P4 proposes boxes stay `[~]`/`[ ]` with
  box 3 held at `[ ]` while the contract is unrepaired; no `[x]`.
- **Province:** all 77 changed paths under `corpus/` (20) or `.ufo/` (57); `PROVINCE.md` bytes
  unchanged; the two `chousa` cross-references in the decision table predate the round (present at
  `a7c6a17`, absent from the r91 diff); K1 found no operator-level need (L0 file unchanged, 5
  entries, no append).
- **Documentation-parity debt:** `corpus/fixtures/README.md` still ends at `## Round 90` — no
  Round-91 section, neither new fixture nor the watch indexed (H5 F7, V2-5, JCAL1-5, P3);
  `r91-c9-watch.md` is referenced by no `corpus/` text.
- **Process:** `/tmp` at ~99–100% inode use through the window (this seat observed 1,713–1,816
  free; H4 1,880→1,724; Q2 records the oscillating ceiling); two 60 s wait-checks per seat were the
  norm; Q2's process audit: helper not landed as specified (1 file of negative mentions, one lost
  terminal record M2, one 83 s restart gap CB1, three canceled pre-authoritative attempts), roster
  delta (32 declared / 30 named / 33 delivered; spec↔JSON contradiction), amendment provenance is
  prose-only (no hash-stamped record for the reconstruction), r90 residue unswept (20 entries /
  2,140 files); W1 landing record shipped in the work commit as the spec's Landing record +
  `wave-spec.json`; SE2's five conformance checks pass (naming, zero tracked modifications, HEAD
  exact, no seat commits, no duplicate report location).

## Findings & named debt

Consolidated identifiers below are JAXIS's (its synthesis read the J-family reports in full);
evidence line references are the follow-up artifacts'.

- **DEP-H1 (depth, blocking-class) — boundary-doc assembly defect.** Spliced/partially applied
  reconstruction; doc-state fidelity vs the declared target harmed; 12–13 lost limits bullets;
  36/54 delivered-context anchors stale; superseded checker pinned "delivered"; no wave receipt for
  the reconstruction; skipped-debt count 1 named vs claimed 2 (H1, H5 A2/A4, CB1, K1, JDEP3, P3).
  Repair R1 specified; do not certify delivered-true.
- **DEP-D2/D2b/D3 — C3 integration drops.** R8/R10 Owner/Trigger/Worked-example labels absent;
  R8 inseparable branch and R10 deliberate-convention case dropped; R9's embedded command targets
  the patch, not the doc (JDEP1/JDEP2).
- **CAL-D1…D6 — calibration bounds.** B3 tick receipt shape-exact not byte-exact; watch wording
  (placeholder paths, no `e97613c` hash); tick README parent/composition note; census
  path-convention sensitivity (5 fixtures); README Round-91 index owed; C9 successor not named
  (JCAL3/V2/JCOV4/JCAL1).
- **COV-D1…D5 — coverage bounds.** Inventory self-attested; two S2 deviations README-named not
  fixed; Spence comparison rows + WARN conditioning (r92); old R9/JDEP2 probes need re-pointing;
  retelling-anchor tolerance (JCOV2/JCOV4/JDEP1).
- **DEP-D1 skipped-debt count and DEP-D4 namespace conventions** (JDEP3); **DEP-D5 capabilities
  row** — JDEP4 recommends a third row `checker-regression discrimination` with its runnable
  companion (L1 owns).
- **PROC-1 delivered-figure wording + roster arithmetic** (H1 M9/SE1/H5/Q2); **PROC-2 this fleet
  report** (SE2 F2 — now written by this seat; umbrella MANIFEST entry still owed); **PROC-3**
  `/tmp` exhaustion, pycache resolved, r85 sealed-receipt debt carried (H4/SE2; the three ambiguous
  r85 probes have not matched their sealed `.txt` receipts since r86 — carried, unchanged).
- **Carried:** B1/B2 tuple manifests are semantically identical but not byte-equal (compare tuples,
  not bytes); H4's sealed-receipt item above.

## Pointers

- Wave evidence: `lore-shokunin/.ufo/waves/round-91/` (33 seat reports + `wave-spec.md` +
  `wave-spec.json` + 22 patches). Work commits `lore-shokunin@6332115`, `@c2ab3d0` (baseline
  `a7c6a17`); no push (12 ahead).
- Follow-up artifacts: `lore-shokunin/.ufo/waves/round-91/followup/` (53 files at
  `2026-10-17T08:47:26-03:00`; untracked).
- Axis synthesis: `followup/JAXIS.md` + `JAXIS-verdicts.json`. Round-record drafts:
  `followup/P3-log-r91.md`, `followup/P2-scorecard-r91.md` (+`P2-verdicts.json`),
  `followup/P4-shonen.md`.
- Boundary-doc forensics: `followup/CB1.md` + `CB1-docstate.json`, `followup/H5.md`,
  `followup/H1.md`; r90 instruction sheet preserved at
  `.ufo/waves/round-90/followup/CB1-boundary-refresh.md`.
- Debt ledger: `.ufo/waves/round-91/patches/Q1-r91-debt.json` (work-wave ledger; the r90 mis-landing
  flagged for L1), `followup/Q1.md`, `followup/Q2.md` (process + three measurable r92 fixes).
- Receipts: `followup/H3-*`, `H4-*`, `JCAL5-delta.json`, `JCOV1.md`, `JDEP4-check.md`,
  `SE2.md`, `W1-disposition.json`.

## Handoff

- **Delivered revision:** `c2ab3d0`; every figure in this report is an observed output on that tree
  (this seat's census/discrimination/support/doc-forensics receipts, or the attributed follow-up
  artifact named beside it). Scratch `/tmp/p3r91` swept; no tracker write beyond this file.
- **L1 decisions owed:** (a) rule the three axes — JAXIS recommends the repair-then-admit path
  (Option A) with depth harmed (bounded) at the delivered tree until R1–R3 land, or Option B
  (admit with the harm recorded); (b) if repairing: R1 re-derive the boundary doc (CB1/JAXIS
  spec), R2 README Round-91 + R8/R10 label transplant + probe re-pointing, R3 the cheap calibration
  wordings; (c) rule the capabilities row (JDEP4); (d) decide the fate of the untracked `followup/`
  wave and the round-record drafts; (e) admit this fleet report (umbrella MANIFEST `rounds[]`
  entry + commit — owed, outside this writer's authorization).
- **Overall round assessment:** C1 verifies exactly (0 changed + 2 new of 166, 0 exit changes,
  live discrimination with single-gate revert controls, freeze PASS, watch pin), C2 verifies
  (receipts + all named silent vectors now failing/warning, integration stack byte-reproduced),
  C3 verifies in substance with named integration drops; the checker is provably unchanged. The
  round's harm is the boundary-document assembly (repaired from the mis-landed sheet, but not
  certifiable as delivered) — recorded here, in JAXIS's synthesis, and in the seat reports, not
  netted.

## Closure addendum (L1)

- [to be filled by L1: verdicts, repairs applied, admission decision, closure commit, MANIFEST entry]

## Closure addendum (L1, 2026-10-17)

- **Verdicts ruled:** calibration **improved (bounded)** — five independent censuses (0 changed + 2 new of 166), discrimination verified including simulated single-gate reverts, the C9 watch reproduces verbatim; coverage **improved (bounded)** — hardened receipts fail/warn on all five r90 silent-failure vectors, the r88-m3 WARN is the correct surfacing (r92 row-add); depth **improved (bounded)** — the three edge decisions verified, register correctly absent, and the fourth doc-parity harm repaired by honest deferral: the boundary doc was restored to the last certifiable contract (e97613c) under a SUPERSEDED-PENDING banner naming what the C9 ruling superseded, with the anchor-based re-derivation explicitly handed to r92 (restoration commit referenced in the lore LOG). Round **admitted** — every claim verifies; no unresolved trade.
- **Capabilities** gains its third row (checker-regression discrimination) per JDEP4's runnable evidence and the L1 ruling recorded in SCORECARD.md.
- **Wave accounting:** work 33 seats (luna max) + follow-up 32 seats (alibaba-token-plan deepseek flash, operator-directed); 2 follow-up seats (JCAL4/JCOV5) interrupted without output, material covered by siblings. Two follow-up retries (JCAL5/JDEP4) and the fleet report itself were completed on resume.
- **Lore closure commit (this round's record):** SCORECARD/LOG round-91 sections, capabilities row 3, the boundary-doc restoration (already committed), and all follow-up artifacts. No push, no registry write, no sibling-repo write; L0 unchanged (K1).
