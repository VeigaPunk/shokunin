# kotoba — round 14 report (DRAFT — pending batch-2 verdicts)

**Lane:** kotoba-shokunin (prompt & skill craft) · **Round:** 14 · **Axis move:**
`coverage` 8.0 → **[PENDING `R14Critic`]** (`SCORECARD.md`; the move was selected by
the mission's lowest-axis rule — see § 1).

**Lane repo:** `VeigaPunk/kotoba-shokunin`, landing commit `29c17be` (+ the LOG/
SCORECARD commit and the corpus-baseline re-record, listed in § 2).

**Pre-registration (written before landing, `/tmp/round14-preregistration.md`,
sha256 `[PENDING]`):** the claim under test, the P1–P5 properties, the outcome
bands (full ⇒ 8.5, partial ⇒ 8.25, no-move ⇒ 8.0), the measurement plan, and the
scope fences — including "do not relabel an operability gain as coverage".

## 1. Move selection

`SCORECARD.md`'s lowest row was `coverage` (8.0, advisory label per the lane's
AXES↔MISSION reconciliation), and the round-13 close had already named the exact
half withheld from that score: *"the pre-registered 8.5 was withheld to 8.0
because the machine check is vacuous for opencode"*. The round-13 plan's second
item (make one `SKILL.md` checklist box executable) stays **carried** for the same
reason as rounds 12–13: it improves `operability`, an axis this lane does not own,
and its accounting question is still unanswered at L0 (`../.ufo/l0-questions.md`,
kotoba round-13 entry, re-recorded in § 8).

## 2. What landed

| Artifact | Content |
|---|---|
| `verifiers/verify_surfaces.py` | 4 → **7 checks** (+`surfaces.opencode_extract`, +`surfaces.literal_parity`, +`surfaces.kind_parity`); `--self-test` 28 → **75 assertions**; exit map unchanged 0/1/2/3 |
| `verifiers/surfaces-baseline.json` | 41 → **42 ids** (opencode 8 → 9) |
| `verifiers/fixtures/surfaces/` | the opencode fixture world becomes coherent: 10 synthetic dumps (clean + one drop-one per rule + extra-class), 4 new inventory fixtures (`literal-drift`, `kind-drift`, `id-not-first`, `no-literal-cell`), `baseline-oc-empty.json`, and both 12-entry baselines extended so every self-test case runs opencode two-way parity |
| `corpus/knowledge/opencode-extraction-round14.md` | the round's evidence file: rule table OC-1…OC-6 with anchors as shapes + derive-vs-witness per rule, the anti-vacuity contract, the falsifier matrix, the row-column parity table, the ceilings |
| `corpus/knowledge/instruction-surface-census-round13.md` | round-14 amendment + § Honest ceiling rewritten where it had a hole: the "vacuous by construction for opencode" bullet is now a named boundary backed by the new check, and the mutation-escape bullet records which columns are machine-checked (id/literal/kind) and which are prose |
| `SKILL.md`, `corpus/README.md` | the surface-check sentence and the corpus index row updated to the two-harness check |
| `.gitignore` | `__pycache__/`, `*.pyc` (a stray `.pyc` was staged by an import) |

## 3. Falsifiers, run (all at `29c17be`, commands verbatim in the corpus file)

| Case | Result |
|---|---|
| live tree | **7/7 PASS, exit 0** — `opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`; 42 loader-kind entries verified; 42 ids in parity; ≈4.5 s warm / ≈18 s cold |
| fixtures | `--self-test` → **0 failure(s) over 75 assertions**, exit 0 |
| empty baseline, live dumps | exit 1, `FAIL surfaces.opencode_extract` naming **all 9** opencode ids (+ `no_uncovered_class` naming all 8 omp ids, + table/literal/kind parity FAILs) |
| zero extraction | exit 1, `vacuity: extraction produced 0 class(es) from 7 rule(s)` |
| drop-one, each rule | exit 1 naming that rule's ids (fixtures) |
| census literal rewrite | exit 1 `FAIL surfaces.literal_parity … omp:agents-md/AGENTS.md` while `table_parity` PASSes — the round-13 escape, closed |
| census kind rewrite | exit 1 `FAIL surfaces.kind_parity … census kind 'loader-literal' != baseline context_kind 'loader-group'` |
| live OC-1 anchor deleted from a dump copy | exit 1 `declared opencode class(es) produced by no rule: …` |
| other instruments | `verify_corpus_integrity.py` **9/9** (tracked 43, pointers 28, commits 24, all zero-modes 0), `verify_corpus_independent.py` exit 0, `verify_harness_claims.py` **27/27**, `fault_injection_corpus.sh --self-test` **OK** |

## 4. Non-author verification (L2 batch 2) — [PENDING]

- `R14Rebuild` (reviewer): live re-measure + independent re-derivation → [PENDING]
- `R14MutationsPost` (mutation-tester): escape matrix → [PENDING]
- `R14Critic` (critic): band + attack → [PENDING]
- `R14Simplify` (simplifier): dead-weight/vacuity audit → [PENDING]
- `R14Distill` (distiller): merged findings table → [PENDING]

## 5. Findings that moved the artifact mid-round

1. **The blind witness found a class the census governed only in prose.** L2 lane
   `R14OcShapes` (never read the census or any scratch) enumerated opencode's
   instruction surfaces from the binary and found **two parallel subsystems**:
   v1 `@opencode/Instruction` and v2 `instruction-context` (context key
   `core/instructions`, ambient all-match walk, ungated config candidate). The
   census described the split in prose but gave v2 no class id, so the inventory's
   own claim ("every loader-derived class is governed or excluded with a reason")
   was overstated by one class. Round 14 declares **`opencode:instruction-context/AGENTS.md`**
   as the 42nd id and pins it with rule OC-6. Live proof the pin is load-bearing:
   with the rule present and the id undeclared, the live run FAILed
   `extracted opencode class(es) undeclared in baseline: opencode:instruction-context/AGENTS.md`.
2. **A lane-vs-lane false negative, decided by bytes.** L2 lane `R14CensusFresh`
   (reviewer) first reported the census's `core/instructions` literal as ABSENT
   from the dump; re-checked on request, it is PRESENT — `BP=XH.Key.make("core/instructions")`
   in the `InstructionContext.File` chunk — and the reviewer explained the earlier
   probe as a malformed grep. Same class of error the round forbids: a probe whose
   command cannot distinguish absent from mis-quoted.
3. **Numbering divergence across lanes, resolved by anchor.** The planner numbered
   its rules OC-1..OC-5 (its OC-3 = the globUp switch); the landed numbering is
   OC-1..OC-6 (OC-5 = the switch, OC-6 = v2). Every cross-lane drop fixture maps to
   the landed rules **by anchor, not by number** — recorded in the evidence file so
   a reader cannot be misled by the overlap.
4. **Pre-state mutation matrix (L2 `R14MutationsPre`)** found the round-13 literal
   escape already closed by the in-flight `literal_parity`, and three escapes in the
   same family: `kind`, `governed by`, `evidence` columns. `kind` has an exact
   machine counterpart, so `surfaces.kind_parity` now closes it; the two prose
   columns are named as the standing residual (§ 6).

## 6. Honest residual (named, not smoothed)

- **Two census columns are still prose.** `governed by` and `evidence` have no
  machine counterpart in the baseline, so a rewrite there is caught by a reader,
  not by the checker. Id, literal and kind **are** compared per id.
- **Extraction, not injection.** A rule matching proves the loader shape ships in
  the binary; it is not proof any file reached a prompt this session.
- **Extraction-set completeness.** Seven rules are a documented set; nothing here
  proves no other opencode instruction surface exists, only that every declared
  class has a load-bearing witness and a vanished anchor FAILs.
- **`surfaces.literal_present` still reports `PASS` with `0 entries verified`** when
  a baseline declares no loader-kind entries (a vacuous PASS inside one check;
  masked at exit-code level by the other checks). Held for the simplifier/critic
  verdict rather than silently "fixed" mid-verification — see § 8.
- **Forty `SKILL.md` checklist boxes** remain lane-attested (unchanged).

## 7. Cross-domain (routed, not absorbed)

- `R14FleetPattern` (connector): kagi's `surface-census.sh` has no census-row floor
  and can return clean on a readable empty census; kake's `probe-delta.mjs` is a
  report that exits 0 for any nonempty parse — both are kagi/kake territory, routed
  here, not fixed. Kumitate's `cite-check.mjs` (nonempty scan + ≥1 resolved
  citation) is the convention kotoba's parity check extends.
- `~/Projects/bounties` remains GONE (round-13 finding; kasegi's PROVINCE root,
  kasegi round-15 L0 entry) — no host count in this round's artifacts names it.

## 8. L2 roster (14 dispatches, one batch of 9 + one batch of 5)

| Batch | Lanes (role seat) | Model route |
|---|---|---|
| 1 | `R14Plan` (planner), `R14FleetPattern` (connector) | @m_lunamax |
| 1 | `R14OcExtractor`, `R14FixtureWorld` (executor/scout) | @m_flash |
| 1 | `R14OcShapes` (scout — blind witness) | @m_flash |
| 1 | `R14DropOne` (labrat), `R14MutationsPre` (mutation-tester), `R14CensusFresh` (reviewer), `R14FixtureSafety` (sentinel) | @m_zfl |
| 2 | `R14Rebuild` (reviewer), `R14MutationsPost` (mutation-tester), `R14Critic` (critic), `R14Simplify` (simplifier), `R14Distill` (distiller) | @m_zfl |

L0 status: the round-13 question (may a lane work an advisory axis as its
lowest-axis move; and D-78's AXES↔MISSION naming) is still unanswered, and round 14
again worked the lowest row (`coverage`) rather than an owned axis. Recorded, not
re-litigated.

[PENDING: final score, critic verdict, rebuilder numbers, post-mutation escapes]