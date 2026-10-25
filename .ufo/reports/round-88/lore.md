# fleet report — lore r88 (round-88, world-bible lane)

Lane: `lore-shokunin` · Repo HEAD measured: `2ea9ef13a928475b13fd578740ea521bed4bd649` (`2ea9ef1`).
Baseline: `dfd1fbc3711f2b28597d74444819aca91fe6bc31` (`dfd1fbc`, r87 closure).
Wave: 37 work seats (`.ufo/waves/round-88/`) + follow-up judging seats
(`.ufo/waves/round-88/followup/`). Every measurement below is taken on the delivered tree at
`2ea9ef1` — never on intent, and never on a scratch patch. Scratch was used for probes/controls only.
Tree state at measure: `git status --porcelain` → ` M l0-questions.md` (K1's authorized append) and
`?? .ufo/waves/round-88/followup/`; no other working-tree change.

**Axis verdicts: `PENDING-L1` for calibration, coverage, and depth.** This report records
measurements, the judges' *recommendations*, and named debt; it does not rule. The judges split on
one point and L1 must resolve it: depth is recommended `improved` by JDEP1/JDEP2/JDEP3 and
`harmed` by JDEP4 (checker-semantics fidelity of the `corpus/knowledge` doc set). Because a trade
anywhere is not an improvement, the two claims cannot both be netted away.

## Work performed

Three claims were declared for round 88, one per owned axis (`.ufo/waves/round-88/wave-spec.md`):

- **C1 — calibration** (lowest-axis obligation): close the r87 residual — first-stop *cause* tracking
  replaces the holder-only latch, so (i) a shape-invalid dict record carrying an ambiguous holder id
  arms the stop, (ii) every record at/after **any** provenance stop discloses the *actual* first
  cause instead of the later ambiguity, and (iii) non-holder stops (unknown source, dangling holder,
  malformed record, non-item, unavailable source table, duplicate item id) disclose at all.
- **C2 — coverage**: a second sourced-mythology cluster from a family distinct from r87's
  Sumerian/ETCSL, with passage-level locators and a clause→element symbolism index, plus repair of
  r87's OBS-1 (the Mother-Tide Gate hymn attribution).
- **C3 — depth**: a sourced-inspiration decision table keeping attribution / rights /
  AI-training-permission as three distinct columns, and registration of the r87 ETCSL citation in
  `reference-ledger.md`.

Work items and evidence pointers:

- **C1 implementation + fixtures** — landed by the work commit `2ea9ef1`: `corpus/fixtures/check_bible.py`
  (`git diff --numstat dfd1fbc..2ea9ef1` → `59 20`) plus three new stop-class fixtures. Candidate
  family and design alternatives: `X1.md` (primary), `X2.md` (ordering-only), `X3.md`
  (first-cause-only, + `patches/X3-c1-firstcause-delta.json`), `X4.md` (rejected-record notice
  variant); code scout `S1.md`; wording panel `E1.md` (+ `patches/E1-r88-wording.md`); baseline
  reproducer `B3.md` (+ `patches/B3-before-state.json`); fixture authors `F1.md`/`F2.md`
  (+ `patches/F1-r88-fixtures.patch`); critics `C5.md`/`C5B.md`; audits `C6.md`/`C6B.md`
  (+ `patches/C6B-c1-audit.json`); independent verifiers `V1.md` (+ `patches/V1-delta.json`),
  `J1.md` (+ `patches/J1-postfix.json`).
- **C2 cluster + OBS-1 repair** — landed by `2ea9ef1`. Three independent drafts `M1.md`/`M2.md`/`M3.md`
  (+ `patches/M{1,2,3}-cluster2.patch`), OBS-1 repair `M4.md`
  (+ `patches/M4-obs1-excerpt.patch`, `M4-obs1-repoint.patch`), convergence reviewer `M5.md`
  (+ `patches/M5-compliance.json`), province critics `C7.md`/`C7B.md`, cross-draft `T1.md`.
- **C3 table + ledger row** — landed by `2ea9ef1`. Table drafts `D1.md` (+ `patches/D1-table.md`) and
  `D2.md` (+ `patches/D2-decision-table.md`, `D2-ledger-rows.md`); reviewer `R1B.md` (recommended D1
  only, with a scope note); ledger row `D3.md` (+ `patches/D3-ledger-append.patch`); scout `S2.md`.
- **Boundary / census / record** — baseline census `B1.md` (+ `patches/B1-tuples.json`) and `B2.md`
  (+ `patches/B2-tuples.json`); connector `K1.md`; boundary scout `S3.md`; sequencing `SE1.md`;
  scribes `W1.md` (+ `patches/W1-{log,scorecard}-r88.proposal.md`) and `W2.md`
  (+ `patches/W2-report-r88.skeleton.md`); debt auditor `Q1.md` (+ `patches/Q1-r88-debt-map.json`).
- **Follow-up judging** (`followup/`) — `V2.md` (fixture-README verifier), `JCAL3.md` + `JCAL5.md`
  (independent calibration judges), `JCAL1-delta.json`/`JCAL3-receipts.json`/`JCAL5-delta.json`,
  `JCOV3.md` (branch-exercise coverage judge), `JCOV5.md` (sibling-adjacency coverage judge),
  `JCOV1-measurements.json`/`JCOV2-support.json` (coverage receipts), `JDEP1.md`/`JDEP2.md`/
  `JDEP3.md` (depth judges: table, ledger, table-attacker), `JDEP4.md` (checker-semantics drift
  judge), `JDEP5-receipts.json`, `H2-delta.json`/`H3-*` (harm sweeps), `K1.md` (connector),
  `P2.md` + `P2-scorecard-r88.md` (scorecard draft), `P4-shonen.md` (SHONEN draft),
  `E1-message-inventory.json`.

## Landed changes

Each landed change is tied to the future LOG entry it will record:

- **C1 — `corpus/fixtures/check_bible.py` (+59/−20, 395 lines, sha256 `dcacffd6…`)** and three new
  fixture dirs (`r88-shape-ambiguous-armed`, `r88-mixed-stop`, `r88-nonholder-stop`). Commit
  **`2ea9ef1`**. Future LOG entry: *“Round 88 — C1: first-stop cause tracking replaces the
  holder-only latch; shape-invalid dict records arm the stop; same-record causes summarised.”*
  The checker's disclosure family is a full replacement: the r87 two-string design is gone
  (`grep -c "unassessed because ambiguous holder identity" corpus/fixtures/check_bible.py` → 0).
- **C2 — `corpus/fixtures/r88-m3-maya-cluster/` (10 files)** and the OBS-1 repair to
  `corpus/fixtures/r87-myth-cluster/` (`entities.json` 1/1, `lowwater-hymn-excerpt.md` 1/1,
  `symbolism-clause-map.md` 2/1). Commit **`2ea9ef1`**. Future LOG entry: *“Round 88 — C2: second
  sourced-mythology cluster (K'iche/Maya via Spence 1913, passage-located) + OBS-1 excerpt repair.”*
- **C3 — `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (new, 19 lines) and the ETCSL
  row in `corpus/knowledge/reference-ledger.md` (`git diff --numstat` → `3 2`)**. Commit
  **`2ea9ef1`**. Future LOG entry: *“Round 88 — C3: sourced-inspiration decision table + ETCSL ledger
  registration.”*
- **Wave evidence — `.ufo/waves/round-88/` (37 seat reports + `patches/`)**. Commit **`2ea9ef1`**
  (`git diff --name-status dfd1fbc 2ea9ef1 | awk '{print $2}' | sed 's#/.*##' | sort | uniq -c` →
  `34 corpus`, `69 .ufo`). Future LOG entry: *“Round 88 — work-wave evidence (37 seats, luna-max).”*
- **Not committed (open for the integrator):**
  - **`l0-questions.md` round-88 line (K1)** — one operator question appended (kotodama↔lore
    integration-contract ownership); `l0-questions.md` is `M` in the working tree.
  - **Follow-up judging artifacts** — `.ufo/waves/round-88/followup/` is untracked.
  - **Round record (LOG/SCORECARD)** — `git diff --name-only dfd1fbc 2ea9ef1 -- LOG.md SCORECARD.md`
    → empty. Drafts only: `patches/W1-log-r88.proposal.md`, `patches/W1-scorecard-r88.proposal.md`,
    `followup/P2-scorecard-r88.md`.

## Before → after measurements

### C1 — calibration (first-stop cause tracking)

- **Counting command (delivered tree, canonical form, repo-root-relative paths):** for every
  immediate `corpus/fixtures/*` dir, `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>`,
  capturing `(exit, stdout, stderr)`. My own run over `git archive` copies of both commits:
  ```
  root=/tmp/lore88/base  dirs=145 exit0=30 exit1=115
  root=/tmp/lore88/deliv dirs=149 exit0=31 exit1=118
  new 4 ['r88-m3-maya-cluster','r88-mixed-stop','r88-nonholder-stop','r88-shape-ambiguous-armed']
  gone 0
  changed 9 ['r61-independent-empty','r61-independent-unavailable','r87-masked-break-from-ambiguous',
    'r87-masked-break-to-ambiguous','r87-probe-entry-shape','r87-probe-multi-invalid',
    'r87-probe-nonitem-kinds','r87-probe-record-and-chain','r87-probe-shape-ambiguous']
  exit_changes []
  pre_r87_changed 2 ['r61-independent-empty','r61-independent-unavailable']
  ```
- **Measured commit:** `2ea9ef1`. **Baseline:** `dfd1fbc`.
- **Delta enumerable:** `changed=9, new=4, missing=0, exit_changes=0`; violation lines
  `331 → 367` (the baseline-145 subset is `331 → 352`); 0 non-empty stderr before and after.
  136 of the 145 baseline tuples are byte-identical. The 2 pre-r87 changes are **purely additive**
  (`r61-independent-empty` 17→18, `r61-independent-unavailable` 6→7), each a new first-cause
  disclosure (`provenance attached to a non-item entity`, `source table unavailable`).
  This exact 9+4 delta was independently reproduced four times by different methods: `V1.md`
  (+`patches/V1-delta.json`), `C6B.md`, `JCAL3.md` (own census), `JCAL5.md` (own regenerated
  baseline, shuffled traversal, `python3 -I`), and `P2.md`.
- **The three r87 residuals, before → after** (delivered output, verbatim):

  ```
  $ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
  before (dfd1fbc): 2 findings, 0 `unassessed` lines, tail neither reported nor disclosed
  after  (2ea9ef1): 5 findings, exit 1
    VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
    VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain
      unassessed (input-structural finding, not sourced-canon); first stop: malformed record
      (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
    VIOLATION: entities[5].provenance[1]: … first stop: malformed record (unexpected field set);
      ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]

  $ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop
  after: 6 findings, exit 1 — all three disclosure lines read
    first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
  (the later ambiguous `to_holder` at [1] is still reported as its own finding but never named as the cause)

  $ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-nonholder-stop
  before (baseline checker, same files): 1 finding, no disclosure
  after: 4 findings, exit 1 — disclosures at [0]–[2], first stop unknown source
  ```
  `V2.md` verified all three fixture READMEs line-by-line on `2ea9ef1` and showed each fixture
  **discriminates** against the baseline checker (pre-fix behaviour reproduced under `dfd1fbc`).
- **Grammar / coverage invariant (delivered tree, `JCAL3.md` and `JCAL5.md`, independently):**
  47 disclosure lines across 12 fixtures; `missing qualifier 0`, `non-contiguous disclosure runs 0`,
  `fixtures_with_gaps 0`, `disclosures_containing_causal_because 0`. Every line carries
  `(input-structural finding, not sourced-canon)`. 13 distinct first-stop causes observed.
- **r85 live-probe replays (baseline → delivered), `JCAL3.md`/`JDEP4.md`:**

  | probe | `dfd1fbc` | `2ea9ef1` |
  |---|---:|---:|
  | `r85-control` | 0 (`CLEAN`) | 0 (`CLEAN`, identical) |
  | `r85-unique-break-control` | 1 | 1 (identical line) |
  | `r85-masked-ambiguous` | 5 | **4** |
  | `r85-isolated-ambiguous` | 4 | **3** |
  | `r85-harbor-repro` | 7 | **6** |

  Exits are `0,1,1,1,1` before and after — **0 exit changes**. The net line-count drop is the removal
  of the superseded r87 item-level notice; the scope it asserted is now stated extensionally, one
  line per affected record. So the round's change is **not** "additions-only" (the seat-block
  phrasing) — it is "wording replaced, scope stated per record". `JCAL3` flags
  `patches/X3-c1-firstcause-delta.json`'s `after_violation_total = 351` as a counter artifact; the
  correct figure is **352** over the 145-dir subset (367 over 149).
- **Judge recommendations:** `JCAL1-delta.json` `verdict.calibration = "improved"` (`harmed: []`,
  `unprovable_but_better: []`); `JCAL3.md` and `JCAL5.md` both recommend **calibration improved**.
  `JCAL5` adds the qualification: *"Documentation parity — harmed (this is the trade in the round) …
  C1's 'improved' verdict is contingent … the round as a whole is not a clean improvement while the
  in-repo contract doc contradicts the shipped checker."*

### C2 — coverage (Maya cluster + OBS-1 repair)

- **Counting commands:** `find corpus/fixtures -name inspiration-note.md | wc -l`;
  `ls -d corpus/fixtures/*/ | wc -l`;
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/{r87-myth-cluster,r88-m3-maya-cluster}`.
- **Measured commit:** `2ea9ef1`. **Baseline:** `dfd1fbc`.
- **Inspiration-note files `1 → 2`** (`r87-myth-cluster/inspiration-note.md`,
  `r88-m3-maya-cluster/inspiration-note.md`). **Fixture dirs `145 → 149`** (+`r88-m3-maya-cluster`
  and the three C1 fixtures).
- **Cluster replay:** both clusters → `CLEAN: schema, citations, relations, timeline; 0 violations`,
  exit 0 (the Maya cluster supplies the delivered census's 31st clean exit).
- **Structural counts (parsed from the delivered JSON, my run):**
  - `r88-m3-maya-cluster`: `entities=4 (kinds: character, place) relations=0 timeline=2
    contradictions=0 sources=2`; 5 prose files (`README.md`, `inspiration-note.md`,
    `source-excerpt.md`, `fictional-excerpts.md`, `symbolism-clause-map.md`).
  - `r87-myth-cluster` (unchanged this round): `entities=7 relations=4 timeline=4 contradictions=1
    sources=5`.
  `JCOV3` notes this is a **different** structural surface from r87's: the Maya cluster has no
  factions, no `allied_with` edges, no `depends_on` edges, and an empty contradiction ledger — the
  "second cluster" is not a second copy of r87's surface.
- **OBS-1 repair (r87 cluster, delivered):** the hymn excerpt line now reads
  `… beside the bowl at the Mother-Tide Gate.`; the clause map gained that row (7 → 8 rows); the
  entity claim was narrowed. Clause replay: `gate_named=True; first_appearance=lowwater-hymn;
  claim_source=lowwater-hymn; clause_matches=8/8` — independently reproduced by `JDEP1`, `JCOV3`,
  `JCOV5`, `JDEP5-receipts.json` (`r87-myth-cluster: clauses 8, literal_grep_matches 8, misses []`).
  The **excerpt** variant was integrated, not M4's recommended **repoint** variant.
- **Maya locator / citation:** `source-excerpt.md:3` carries `Chapter V, "The Maya",
  "The Creation-Story", printed p. 209`; `JCOV3` fetched Gutenberg eBook 53080 and confirmed the
  page marker bracketing (`[209]` before, `[210]` after the quoted passage) — the locator is
  independently correct. `JDEP2`'s note that the r88 cluster's *own* clause map is only **1/2
  byte-exact** against the delivered excerpt (map has `“He called out ‘Earth,’”`, the excerpt has
  `“Earth,”`) is confirmed by `JDEP1`, `JCOV1`, `JCOV3`, `P2`, `JDEP5` — 2/2 only after quote
  normalization.
- **Judge recommendations:** `JCOV3.md` and `JCOV5.md` both recommend **coverage improved
  (bounded)**; `JCAL5.md` agrees on the checked evidence. Bounds named: one printed-page locator
  rather than several; the Maya cluster exercises none of the reciprocal-alliance / dependency /
  contradiction branches; the advertised "occupied-slot near-miss" is not a near-miss of the slot
  (occupancy key is `(entity_id, tick)`, and the pair's keys are distinct — `JCOV3` D1);
  `corpus/fixtures/README.md` still has no Round 87/88 section.

### C3 — depth (decision table + ledger registration)

- **Counting commands:** `grep -c '^|' corpus/knowledge/reference-ledger.md`;
  `git diff --numstat dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md`;
  `git diff --name-status dfd1fbc 2ea9ef1 -- corpus/knowledge/`.
- **Measured commit:** `2ea9ef1`. **Baseline:** `dfd1fbc`.
- **Ledger rows `3 → 4`** (6 table lines = header + separator + 4 data rows), every data row
  `ncols=4`, no empty cells. The diff is `3 2` (3 insertions / 2 deletions = 1 new row + 2 reworded
  prose lines); the row-only diff is a pure append (`5a6`) with all three prior rows md5-identical
  and the header/separator untouched (`JDEP2`). Heading broadened from "Real-world method
  references" to "Real-world references"; the "(not in-world canon)" boundary is retained.
- **Decision table:** `corpus/knowledge/r88-sourced-inspiration-decision-table.md` is added
  (`A` in `git diff --name-status`), 7 decision rows × 6 columns, with `Attribution`,
  `Rights status`, and `AI-training permission` as three distinct columns. The R1B scope
  clarification is present as an HTML comment on line 1 (`JDEP1`: the only diff against
  `patches/D1-table.md` is two prepended lines).
- **ETCSL row:** attribution / rights / training-permission in three separate populated cells, rights
  and training recorded as **open questions** (no grant asserted), use bounded to motif-level and
  explicitly not canon; locator `lines 122–163` verified against the live ETCSL page (`JDEP2`).
  Contract `seed.md:26–29` (three distinct questions, separate from canon) is satisfied.
- **Judge recommendations:** `JDEP1.md` (table) and `JDEP3.md` (table attacker) recommend **depth
  improved (bounded)**; `JDEP2.md` (ledger) recommends **improved**. `JDEP4.md` recommends
  **depth harmed** on the narrower scope of checker-semantics fidelity of the `corpus/knowledge`
  doc set. `P2.md` asserts no verdict (PENDING-L1).

### Census (measurement, not an axis claim)

- **Command:** replay of `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` over every
  immediate `corpus/fixtures/*` dir, paths relative to the repo root.
- **Result:** `145 → 149` dirs; exits `{0:30, 1:115} → {0:31, 1:118}`; violation lines
  `331 → 367`; inherited JSON changed/missing `0/0`; 0 non-empty stderr both sides.
- **Reproducibility caveat (measured twice, `P2` and `V1`):** the census must pass fixture paths
  **relative to the repo root**. Passing absolute paths makes the five `cannot load JSON` fixtures
  (`r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-{control,empty,whitespace}`) echo
  the argument path and read as spurious deltas (`changed=14` instead of `9`). Any future census
  receipt should state the path form.

## SHONEN

`SHONEN.md` is unchanged this round (`git diff --stat dfd1fbc 2ea9ef1 -- SHONEN.md` → empty); four
boxes at `SHONEN.md:5,6,8,9`. **No `[x]` is claimed** — no named non-author verifier has executed
the lane's instructions cold. Drafted by follow-up seat `P4` (`followup/P4-shonen.md`).

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists, cited
  sources* — **unchanged**. No `SKILL.md` exists in the lane (`test -e SKILL.md` → ABSENT;
  `git ls-files | grep -Ei 'skill'` → no matches), so the box's subject does not exist to assert.
  Round 88's decision-table material landed at
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (C3), alongside the r87 provenance
  table and the `2026-10-12-*` knowledge files — not in a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* —
  **lane assertion retained; evidence improved this round**. The clause is satisfied at the delivered
  revision by the round-87 record (`LOG.md:1699`, C1 landed + measurements + reproduce commands),
  which did not exist when r87's own follow-up measured the box. Round 88 adds a second end-to-end
  set (149-dir census, `331 → 367` findings, exits `{0:31, 1:118}`, three new stop-class probes, the
  Maya cluster, the D1 table). Round 88's own LOG entry is **not** appended — only
  `patches/W1-log-r88.proposal.md`. The box's evidence pointer is stale (round-1 only).
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* — **unchanged;
  counter-evidence at `2ea9ef1`**. The new D1 table *is* executable (`grep -nF -- '<anchor>' <excerpt>`
  resolves on the delivered Maya cluster and the delivered ledger carries its four-column format),
  but `corpus/knowledge/holder-assessment-boundary.md` is pinned to `2b48ca7` and its own documented
  replay no longer reproduces (doc pastes 5/4/7 findings for `r85-masked-ambiguous` /
  `r85-isolated-ambiguous` / `r85-harbor-repro`; the delivered checker emits 4/3/6 with retired
  wording), and `corpus/knowledge/r87-provenance-chain-decision-table.md` row 32 pastes "zero
  `unassessed` lines" where the delivered checker emits two. The D1 table's row 6 also still frames
  the landed ETCSL ledger row as "D3's patch".
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — **lane assertion
  retained; evidence strengthened**. `PROVINCE.md` bytes unchanged
  (`git diff --stat dfd1fbc 2ea9ef1 -- PROVINCE.md` → empty; `PROVINCE.md:3-11` still resolves, file
  is 11 lines); every changed path is under `corpus/` or `.ufo/`; `l0-questions.md`'s only change is
  K1's authorized round-88 append. The new artifacts keep attribution, rights, and AI-training as
  three separate open questions and assert no rights conclusion.

## Verdicts (ruled by L1 at closure)

calibration **improved (bounded)** — first-stop cause disclosure; 9+4 enumerable census delta,
0 exit changes, five independent census reproductions, 0-mismatch cause audit; bounds named
(same-record combined summary only on the shape-invalid branch; six unexercised first-cause
branches; FN-1/2/3 pre-existing shapes).

coverage **improved (bounded)** — second sourced cluster (Spence 1913 Maya; delivered excerpt,
clause→element index, mechanically verified anchors 10/10), OBS-1 repaired 8/8, notes 1→2,
census 145→149; bounds named (no factions/relations/depends_on by design; shared-tick
near-miss naming corrected; quote glyph fixed at closure).

depth **improved (bounded)** — sourced-inspiration decision table + two ledger rows registered;
**documentation parity harmed (bounded) by the follow-up wave's finding, repaired before
admission**: the r88 checker replacement had drifted `holder-assessment-boundary.md`, the r87
decision table, and seven r87 READMEs; the closure commit re-derived the boundary doc from
CB1's verified refresh (Commands replay reproduces 4/3/6), bannered the r87 table
SUPERSEDED-and-pinned, added README revision notes, and completed ledger/table hygiene.

**Round admitted** — every claim verifies; no axis harmed at closure. The harm-then-repair is
recorded transparently in SCORECARD.md and LOG.md rather than netted away.
## Findings & named debt

- **Doc drift is the round's trade (highest-priority debt).** The C1 commit replaced the checker's
  entire disclosure family without updating the two `corpus/knowledge` docs that state the
  provenance contract: `holder-assessment-boundary.md` (5 dead-notice + 8 dead-disclosure hits) and
  `r87-provenance-chain-decision-table.md` (9 + 16). Both carry explicit recheck triggers keyed to
  the provenance branch, and both triggers fired. `JDEP4.md` enumerates ~15 drifted items in the
  boundary doc (including a now-false fixture census: it says 9 provenance-bearing dirs and "none"
  combining with a duplicated holder id; delivered is 19 and 8) and ~7 rows plus the whole Receipts
  block in the r87 table. `JDEP5-receipts.json` counts 10 of 19 pasted r87-table receipts as stale
  (all exit-preserving). Repair is a find-and-rederive job, not a find-and-replace.
- **Spence is unregistered while ETCSL is.** The Maya cluster's real-world reference (Spence 1913,
  delivered excerpt) has no ledger row (`grep -c Spence corpus/knowledge/reference-ledger.md` → 0),
  while the external-only ETCSL citation does. The landed table's own row 6 asks for the Spence row
  — an asymmetry the round created (`JDEP2` F2, `JDEP1` debt 1, `P2`).
- **The Maya clause map is 1/2 byte-exact against its own delivered excerpt** (`“He called out
  ‘Earth,’”` vs `“Earth,”`) while the same round's decision table requires a fixed-string anchor —
  two artifacts landed in the same commit disagree (`JDEP1` debt 3, `JCOV3` D2, `P2`, `JDEP5`).
- **The D1 table's verification cells rest partly on clusters that did not land.** Rows 1/4/5/7 cite
  M1 (Kojiki) and M2 (Völuspá) evidence; neither `r88-myth-cluster2` nor `r88-norse-cluster` exists
  at `2ea9ef1`. The table also still opens `Draft destination: …`, its row 5 reads in the present
  tense about OBS-1 (now repaired), and R1B's scope clarification landed as a non-rendered HTML
  comment rather than inside the row-5 rule cell (`JDEP1`).
- **Undisclosed r87 support gap.** Under R1B's intended breadth ("every source-attributed in-world
  JSON fact"), the r87 cluster is `1/7` entity claims, `1/7` first-appearance pointers, `0/4`
  relation edges, `0/4` timeline events backed by delivered prose (`JDEP1`, `JCOV2-support.json`).
  The table discloses only OBS-1 plus the M1/M2 gaps.
- **Same-record multi-cause asymmetry.** The combined-cause summary exists only on the shape-invalid
  dict branch; on a shape-valid record with two simultaneous causes the summary names one by
  precedence (holder ambiguity or dangling holder before unknown source) — a documented precedence
  choice, not an exhaustive summary (`JCAL3` debt 1, `JCAL5` D-3).
- **Durable-fixture gaps.** The dangling-holder stop and a two-non-shape-cause record have no durable
  fixture (code paths exist and were exercised only by scratch probes) — `JCAL5` D-2/D-3,
  `JCAL3` debt 4.
- **`corpus/fixtures/README.md` still has no Round 87 or Round 88 section** (last section is Round
  83) — carried from r87 (`JCOV5` D-JCOV5-2, `JCOV3` D4, `P2`).
- **The kotodama↔lore integration contract is still absent.**
  `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md` is declared
  "load-bearing" by `kotodama-shokunin/PROVINCE.md:19-21` and does not exist in either lane
  (`synthesis/` empty; lore has no `synthesis/`). Carried from r87 K2; escalated to `l0-questions.md`
  by K1 this round (`JCOV5` D-JCOV5-1).
- **C1's 9 changed tuples were not adjudicated tuple-by-tuple by a follow-up seat.** `V2` verified 3
  of the 4 new fixtures line-by-line and `JCAL1/JCAL3/JCAL5` independently reproduced the counts, but
  no seat re-derived each changed fixture's delta line-by-line as a formal verdict (`P2`).
- **No push, no registry write, no sibling-repo write.** `l0-questions.md` (K1) and
  `followup/` are left for the integrator's commit decision.

## Pointers

- Wave reports + patches: `lore-shokunin/.ufo/waves/round-88/` (37 seat reports, `patches/`).
- Follow-up artifacts: `lore-shokunin/.ufo/waves/round-88/followup/`.
- Work commit: `lore-shokunin@2ea9ef1` (baseline `dfd1fbc`).
- Uncommitted: `l0-questions.md` (K1 round-88 line); `.ufo/waves/round-88/followup/` (untracked).
- Round-record drafts: `patches/W1-log-r88.proposal.md`, `patches/W1-scorecard-r88.proposal.md`,
  `followup/P2-scorecard-r88.md`, `followup/P4-shonen.md`.
- MANIFEST closure entry draft: `.ufo/waves/round-88/followup/P1-manifest-entry.json`.
- Seat report for this writer: `.ufo/waves/round-88/followup/P1.md`.

## Closure addendum (L1, 2026-10-17)

- **Lore closure commit (this round's record):** SCORECARD/LOG round-88 sections, the
  documentation-parity repair (boundary doc refreshed from CB1's verified proposal; r87
  decision table bannered SUPERSEDED-and-pinned at `2b48ca7`; seven r87 README revision notes;
  Maya clause-map quote glyph; Spence ledger row; D1 table hygiene; fixtures-README Round
  87/88 sections; wave-spec roster amendment), all follow-up artifacts.
- **Verifier convergence on the C1 delta:** five independent censuses (V1, C6B, JCAL1,
  JCAL5 with a regenerated baseline, H2) reproduce exactly 9 changed + 4 new of 149 dirs,
  0 exit changes; the 2 pre-r87 `r61` changes are accurate additive disclosures. The r85
  probes changed by reword-with-merge (7→6, 4→3, 5→4) — the round record says
  "enumerable delta", never "additions-only".
- **Process debts for r89:** 60 s wait-checks missed by 54% of seats (authors up to +24 min);
  the delivered checker carried an integrator amendment whose first verification was phase-2
  V2; wave-spec roster prose drifted (amended in-file). Q2's three improvements: freeze-and-
  reverify the delivered revision; dependency barrier or calibrated deadlines; roster-as-data.
- L0 carries the kotodama integration-contract question (K1's round-88 append). No push, no
  registry write, no sibling-repo write.
