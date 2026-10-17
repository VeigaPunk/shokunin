# fleet report — lore r87 (round-87, world-bible lane)

Lane: `lore-shokunin` · Repo HEAD measured: `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (tree clean at
start of the follow-up wave; only untracked `.ufo/waves/round-87/followup/`).
Wave: 39 work seats + follow-up seats, `.ufo/waves/round-87/`. All measurements below are on the
delivered tree at `2b48ca7`, never on intent or on a scratch patch.
Verdicts (ruled by L1 at closure): calibration **improved (bounded)**, depth **improved**, coverage
**improved (bounded)**; no axis harmed; round **admitted**. Closure census: 145 fixture dirs, prior
133 tuples byte-identical (0 changed). The wave-time "uncommitted" notes below were resolved by the
closure commits — see the Closure addendum at the end.

## Work performed

Three claims were declared for round 87, one per owned axis:

- **C1 — calibration**: per-record unassessed disclosure for ambiguous provenance holders
  (masked-break repair). The r85 latent defect: an ambiguous holder id latches
  `can_check_chain=False` and the item's later records carry **no** local disclosure, so an encoded
  downstream holder mismatch is silently unassessed.
- **C2 — depth**: a provenance-chain decision-table knowledge file (boundary state → output →
  editor action), plus the holder-assessment boundary-knowledge refresh and the census extension.
- **C3 — coverage**: a new `r87-myth-cluster` world-bible fixture (breadth of entity/relation/timeline
  records with a sourced real-world inspiration).

Work items (evidence pointers):

- **C1 implementation + regression fixtures** — delivered by commits `03c6746` (checker hunk + 4
  fixture dirs). Candidate family and the mask analysis: `.ufo/waves/round-87/X1.md`, `X2.md`,
  `X3.md`, `X4.md`; branch/exit-path map `S1.md`; critic `C5.md`; independent verifier `V1.md`
  (+`patches/V1-verify.json`), mutation `V4.md` (+`patches/V4-mutation.json`); masked-fixture
  producer `F1.md`/`F2.md`. `R1.md` ranked the minimal `X3` variant first; `C6.md` audited the
  full-corpus delta.
- **C3 myth cluster** — delivered by commit `e4708cb`. Three independent drafts `M1.md`/`M2.md`/
  `M3.md` (patches under `patches/`), compliance review `M4.md`, PROVINCE-boundary review `C7.md`,
  evidence audit `R2.md`, prose audit `JCOV4.md`.
- **C2 decision table** — drafts `D1.md` + `patches/D1-decision-table.md` and `D2.md` +
  `patches/D2-decision-table.md`; audits `T1.md`, `T2.md`, `R2.md`; sequencing scout `SE1.md`.
  Consolidated and refreshed to the delivered C1 after-state by follow-up seat `I1` —
  `corpus/knowledge/r87-provenance-chain-decision-table.md` (262 lines, **uncommitted** in the
  working tree; see Landed changes).
- **Boundary knowledge** — drift audit `CB1.md` (+`patches/CB1-drift.json`); refresh drafted by
  follow-up seat `I2` (uncommitted in the working tree).
- **Census / evidence** — baseline census `B1.md` (+`patches/B1-tuples.json`), style scout `S2.md`,
  census-extension procedure `S4.md`; executed by follow-up seat `I3`
  (`.ufo/waves/round-87/followup/I3.md`, `r87-extended-tuples.json`, `I3-stdout.json`).
- **Boundary / scope** — connector `K1.md`, sibling-overlap `S3.md`, follow-up re-scan `K2`
  (+`followup/K2-adjacency.md`), `l0-questions.md` append.
- **Wording / verification follow-up** — `E2.md` (landed-vs-candidate wording),
  `H3.md` (mutation harm sweep), `H4.md`, `JCAL1.md` (calibration replay), `JCOV1/JCOV2`, `Q1`
  (symbolism taste, input only), `P2` (scorecard draft), `P4` (SHONEN draft), `I2` (boundary refresh).
- **Wave evidence commit** — `2b48ca7` lands all 39 seat reports + patches under `.ufo/waves/round-87/`.

## Landed changes

Each landed change is tied to the future LOG entry it will record:

- **C1 — `corpus/fixtures/check_bible.py` (+17 lines) and four fixture dirs**
  (`r87-chain-unique-valid`, `r87-chain-unique-broken`, `r87-masked-break-to-ambiguous`,
  `r87-masked-break-from-ambiguous`). Commit **`03c6746`**. Future LOG entry:
  *“Round 87 — C1: per-record unassessed disclosure for ambiguous provenance holders.”* The
  delivered checker is byte-identical to the `X1-c1` candidate (sha256
  `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237`; baseline `28706dc` =
  `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132`).
- **C2 — `corpus/knowledge/r87-provenance-chain-decision-table.md` (262 lines)**. Landed by
  follow-up seat `I1`, **uncommitted in the working tree** (untracked). Future LOG entry:
  *“Round 87 — C2: provenance-chain decision table (30 rows, C1-refreshed).”* Supersedes the
  pre-C1 `D2` snapshot; every row is re-pointed at a durable fixture shipping in this tree,
  including the two new probe dirs `corpus/fixtures/r87-probe-entry-shape/` and
  `corpus/fixtures/r87-probe-record-and-chain/` (untracked).
- **C3 — `corpus/fixtures/r87-myth-cluster/` (9 files)**. Commit **`e4708cb`**. Future LOG entry:
  *“Round 87 — C3: r87-myth-cluster world-bible fixture (breadth + sourced inspiration).”*
- **Wave evidence — `.ufo/waves/round-87/` (39 seat reports + patches)**. Commit **`2b48ca7`**.
  Future LOG entry: *“Round 87 — work-wave evidence (39 seats, luna-max).”*
- **Not committed (open for the integrator):**
  - **C2 decision table + probe fixtures (I1)** — the table and its two `r87-probe-*` fixture dirs
    are untracked at `2b48ca7`; the file's own snapshot line pins `2b48ca7` and checker
    `3ae4134d…`, so it is already refreshed to the delivered C1 behavior.
  - **Boundary-knowledge refresh (I2)** — `corpus/knowledge/holder-assessment-boundary.md` is
    modified in the working tree (`git diff --stat` → 1 file, +159/−52) but **uncommitted**; at
    `2b48ca7` it is still the pre-C1 file, whose contract text says “Exactly one notice per item”
    (`:52-55`) and is therefore stale against the delivered checker. `P4` records four residual
    stale blocks even after I2's edit.
  - **`l0-questions.md` append (K2)** — one operator-question line is modified but uncommitted:
    `lore | round-87 | C3 source-method adjacency with chousa …`.
  - **LOG entry (P3)** — drafted at `followup/P3-log-r87.md`; `LOG.md` unmodified.

## Before → after measurements

### C1 — calibration (masked-break disclosure)

- **Counting / replay command (delivered tree, canonical form):**
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/<fixture>` and, for the masked pair,
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous`.
- **Measured commit:** `03c6746` (delivered). **Baseline:** `28706dc`.
- **Masked fixture, before → after** (delivered output, verbatim):
  ```
  VIOLATION: entities[5].id: duplicate entities id 'dup'
  VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
  VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
  VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
  VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
  6 violation(s); no canon changed        # exit 1
  ```
  Baseline at `28706dc` emitted only the duplicate-id, the field-local ambiguity, and the single
  item-global notice (3 findings). `r87-masked-break-from-ambiguous` is symmetric (`from_holder`,
  6 findings, exit 1).
- **Disclosure-count delta over the stored r85 probes** (`corpus/live/runs/round-85/probe-inputs/`):
  `r85-control` and `r85-unique-break-control` byte-identical; `r85-masked-ambiguous` 3→5,
  `r85-isolated-ambiguous` 3→4, `r85-harbor-repro` 5→7 findings (all additions are holder
  disclosures; every prior line survives verbatim). Independently replayed by `I2`, `H3`, `JCAL1`.
- **Preservation count (my replay, canonical invocation):** all **133 inherited
  `corpus/fixtures/` tuples byte-identical, 0 changed** — baseline checker (`28706dc`) vs delivered
  checker (`03c6746`) over the same 133 input dirs. (A first harness using *absolute* fixture paths
  reported 5 spurious diffs; the diffs were the absolute path embedded in `cannot load JSON:
  [Errno 2] …` and vanish under the canonical relative-path form. Same caveat recorded by `I2`.)
  A whole-`corpus` census (incl. `corpus/live` probes) shows 142 input dirs, 139 unchanged, 3
  changed (the r85 probes) — `C6.md`.
- **Harm sweep:** `H3` — 8/8 provenance mutations exit 1 with an independent report or a
  per-record disclosure, 0 silent passes; corpus-wide pre-C1 vs delivered over 146 dirs → no exit
  changes, no fixture loses a reported finding (gains only). `JCAL1` recommends **calibration
  improved** over 156 replayed cases.

### C3 — coverage (r87-myth-cluster)

- **Counting command:** `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster`.
- **Measured commit:** `e4708cb` (delivered). **Baseline:** `28706dc` (dir absent).
- **Before:** directory absent → 5 `cannot load JSON: [Errno 2] …` findings, exit 1 (`M4`).
- **After:** `CLEAN: schema, citations, relations, timeline; 0 violations` — exit 0.
- **Structural counts (parsed from the four JSON tables, delivered tree):**
  `entities=7 factions=2 relations=4 allied_with=2 reciprocal_alliance=True events=4
  dependency_edges=3 contradictions=1 sources=5`; 4 prose files (`README.md`,
  `inspiration-note.md`, `lowwater-hymn-excerpt.md`, `symbolism-clause-map.md`).
  The delivered cluster is the **M3** candidate (`M4`/`C7`/`R2` convergence); `JCOV4` re-derived
  the same counts field-for-field.
- **Named debt carried:** `entities.json` attributes `mother-tide-gate.first_appearance` and one
  claim to source `lowwater-hymn`, but the delivered excerpt contains no proper place name
  (`grep -c "Mother-Tide" lowwater-hymn-excerpt.md` → 0). Not a checker violation; a support gap
  (`Q1`, `P2`). Also carried: `art-east-asian-design` (named rights recipient) is not a fleet-root
  sibling (`K2`).

### C2 — depth (decision table)

- **Counting command:** `wc -l corpus/knowledge/r87-provenance-chain-decision-table.md` and the
  per-row replay `python3 corpus/fixtures/check_bible.py corpus/fixtures/<fixture>`.
- **Measured at:** working tree on top of `2b48ca7` — the file **is present** (262 lines, untracked;
  absent at `2b48ca7` itself). Before: no decision-table knowledge file at either proposed path
  (`D1`/`D2` are baseline-only drafts). After: 30 rows in lifecycle order (entry gate → holder/record
  validation → source resolution → chain comparison → post-stop), each with a code anchor, a verbatim
  emitted signature, a durable verifying fixture, and pasted observed output, plus a Receipts block.
- **Refresh to the delivered C1 after-state:** the table's own snapshot line pins `2b48ca7` and
  checker `3ae4134d…`, and row 15 states the C1 after-state; it explicitly supersedes the pre-C1
  `D2` snapshot. `R2`'s pre-landing requirements are met: the `item-chain-valid` positive control is
  present (row 30), ambiguous-source wording is narrowed (rows 18–19), and the previously scratch-only
  tail probes are now durable fixtures (`r87-probe-record-and-chain`, `r87-probe-entry-shape`).
- **My replay of its receipts (spot check, delivered tree):**
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-record-and-chain` → 35 violations,
  exit 1, including the C1 pair at `entities[5].provenance[0]` (item-level notice **and** the
  self-referential disclosure) and the per-record disclosure at `provenance[1]`;
  `... r87-probe-entry-shape` → 2 violations (duplicate `rope` id, `lamp` non-array `provenance`),
  exit 1. Both match the table's pasted output.
- **Status:** delivered but **uncommitted**; the table and its two probe fixture dirs are untracked.

### Census extension (measurement, not an axis claim)

- **Command:** replay of `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` over every
  immediate `corpus/fixtures/*` dir.
- **Measured:** `2b48ca7`. **Baseline:** `28706dc`.
- **Result:** `133 → 138` fixture dirs (+5: four C1 fixtures + `r87-myth-cluster`); exits
  `{0:28, 1:105} → {0:30, 1:108}`; corpus `*.json` `705 → 730` (25 new paths, all in the 5 new
  dirs); inherited JSON changed/missing = 0/0; non-empty stderr 0 before and after.
  Reproduced independently by `I3` (`followup/I3.md`, `r87-extended-tuples.json`), `P2`, `P4`,
  `JCAL1`. `S4`'s anticipated `133 + 1 = 134` is superseded by the observed `138` (S4 predates the
  four C1 fixtures).

## SHONEN

`SHONEN.md` is unchanged this round (`git diff --name-only 28706dc..2b48ca7 -- SHONEN.md` → empty);
four boxes at `SHONEN.md:5,6,8,9`. No `[x]` is claimed — no named non-author verifier has executed
the lane's instructions cold. Drafted by follow-up seat `P4` (`followup/P4-shonen.md`).

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists, cited
  sources* — **untouched**. No `SKILL.md` exists in the lane (`test -e SKILL.md` → ABSENT;
  `git ls-files | grep -Ei 'SKILL'` → no matches), so the box's subject does not exist to assert.
  Round 87's decision-table material is in `corpus/knowledge/r87-provenance-chain-decision-table.md`
  (C2, uncommitted) and `corpus/knowledge/holder-assessment-boundary.md`, not in a SKILL.md.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* — lane
  assertion retained; not upgraded. The round executed end-to-end domain work (commits `03c6746`,
  `e4708cb`; census and fixture replays above), but `git diff --name-only 28706dc..2b48ca7 -- LOG.md`
  → empty, so the “logged in LOG.md” clause is not satisfied for r87. Pointer:
  `LOG.md` “Fleet round 1 — calibration declaration before batched dispatch”;
  `reports/round-1/baseline-probes.json`.
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* — **untouched;
  counter-evidence at `2b48ca7`**. The lane's only instruction surface is
  `corpus/knowledge/holder-assessment-boundary.md`, which as committed contradicts delivered
  behavior: it says “exactly one notice per item” (`:52-55`, `:73`) while the delivered checker
  emits 4 `unassessed` lines per masked fixture; its named recheck command
  `corpus/fixtures/measure_holder_disclosure.py` is absent (exit 2); its status is
  `STATIC PENDING PARENT RUNTIME`. I2's refresh repairs most of this but is **uncommitted** and still
  leaves four residual blocks (`followup/P4-shonen.md`).
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — lane assertion
  retained; consistent with this round. `PROVINCE.md` bytes unchanged
  (`git diff --name-only 28706dc..2b48ca7 -- PROVINCE.md` → empty); every changed path is under
  `corpus/` or `.ufo/`. C3 keeps attribution/rights/AI-training as three separate open questions and
  reports the place contradiction without resolving it (`PROVINCE.md:7,9`); C1 is consistency
  verification, which `PROVINCE.md:3` owns.

## Named gaps and limits for L1

- **C2 is delivered but uncommitted** (the decision table + its two probe fixture dirs are untracked
  at `2b48ca7`). Depth's landed artifact exists only in the working tree.
- **I2's boundary refresh is uncommitted** and still has residual stale blocks; the committed
  knowledge file contradicts delivered C1 behavior.
- **Shipped C1 wording ≠ every verified scratch patch.** The delivered checker is the `X1` variant;
  `V1`/`V4` verified X1, but `V3` verified the `X3` variant that did **not** ship, and `R1` ranked
  X3 first. `E2`/`P2` flag that the delivered text was never independently verified *as shipped*.
- **Disclosure, not report.** The masked downstream break is *disclosed as unassessed*, never
  *reported* as a break (`H3` D2). The `input-structural finding, not sourced-canon` qualifier is
  unreachable from any delivered fixture (`E2-contrast.json`: `fixtures_emitting_qualifier: 0`).
- **Mixed stop cause uncovered.** If an unknown source latched the gate before a later ambiguity, the
  disclosure names only the ambiguity (`C5`, `P2`); no delivered fixture covers this.
- **V4's F2 indices** describe a non-delivered fixture (`r87-f2-masked-break-from-ambiguous`); do not
  cite them as delivered-tree evidence (`H3` D1).
- No push, no registry write, no sibling-repo write. C2/I2/K2 working-tree changes are left for the
  integrator's commit decision.

## Pointers

- Wave reports + patches: `lore-shokunin/.ufo/waves/round-87/` (39 seat reports, `patches/`).
- Follow-up artifacts: `lore-shokunin/.ufo/waves/round-87/followup/` (`I2`, `I3`, `K2`, `Q1`,
  `JCOV1/2/4`, `E2`, `H3`, `H4`, `JCAL1`, `P2`, `P3`, `P4`, plus JSON receipts).
- Uncommitted round-87 deliverables in the working tree:
  `corpus/knowledge/r87-provenance-chain-decision-table.md` (C2, I1),
  `corpus/fixtures/r87-probe-entry-shape/` and `corpus/fixtures/r87-probe-record-and-chain/` (C2
  fixtures, I1), `corpus/knowledge/holder-assessment-boundary.md` (refresh, I2), `l0-questions.md`
  (append, K2); LOG draft at `followup/P3-log-r87.md`.
- Commits: `03c6746` (C1), `e4708cb` (C3), `2b48ca7` (wave evidence).
- MANIFEST closure entry draft: `.ufo/waves/round-87/followup/P1-manifest-entry.json`.

## Closure addendum (L1, 2026-10-17)

- **Lore closure commit: `dfd1fbc3711f2b28597d74444819aca91fe6bc31`** — C2 decision table (35
  rows) + 7 probe fixtures (incl. 5 attack-closure probes), boundary-doc + masked-README
  reconciliation, SCORECARD/LOG round record, all follow-up artifacts. `l0-questions.md` carries
  the round-87 Chousa-boundary line (K2).
- **JDEP3 attack fully folded in before closure:** U-1 row-shape silent-skip (boundary row 31),
  U-2/U-3 source-prefix variants (`r87-probe-source-prefix`, row 19 re-anchored), U-4
  shape-invalid ambiguous (row 32 + fixture), U-5 rope r8 valid would-break record (row 26 claim
  now demonstrated; 35 → 34 findings), U-6 same-record multi-invalidity (row 33), U-7
  unavailable-sources silence bound stated in Assessment limits, U-8/U-9 (rows 34–35).
- **Closure census: 145 fixture dirs, 30 clean / 115 violations; the 133 prior tuples remain
  byte-identical (0 changed).** Seats JCOV3 and SE2, interrupted twice by the operator, were
  completed inline by the L1 (`followup/JCOV3.md`, `followup/SE2.md`); batch-resume-after-
  -interruption is recorded as process debt for r88.
- **L1 verdicts: calibration improved (bounded), depth improved, coverage improved (bounded);
  no axis harmed; round admitted.** No push, no registry write, no sibling-repo write.
