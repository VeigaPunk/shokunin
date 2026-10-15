# Round 14 — registry-home planner

Planning evidence only; no conformance judgment, score change, or executed verification is asserted here. Scope is `context.md:1-10`; the L1 owns integration and its round-plan declaration. No shipping file was edited and no build, lint, test, self-test, or formatter was run.

## Observations and concrete data walk

1. **Input identity → lane kind.** `MISSION.md:9-15,19-29` declares `protocol` and `aggregator` at the fleet root, unlike child-repo lanes. Sharing a cwd does not merge their ownership. `SCORECARD.md:3-7,132-138` already separates the protocol and aggregator sections.
2. **Lane kind → unusable current home.** `PROTOCOL.md:382-387` sends every registry row to its lane's `SKILL.md`; `PROTOCOL.md:399-402` independently makes that same path a conformance prerequisite. The root directory read shows no root `SKILL.md`. This is the actual missing-root-SKILL case, not a missing gate implementation.
3. **Recorded baseline → explicit defect.** `SCORECARD.md:24-25,95-105` holds protocol-soundness at 8, gate-integrity at 9, and names this contradiction and the need for revision-bearing verdicts. `before.json:4-7` records baseline revision `e163d15bb1b080ae567ada3b86441455e9808f9b`, `protocol_registered_closure_gates=0`, `root_SKILL_exists=False`, exit 0. Those are the parent's recorded outputs, not a worker rerun or independently authenticated commit measurement.
4. **Existing mechanism → row contents.** `.ufo/waves/round-15/closure-check.py:64-77` declares exits 0/1/2/3 and stdout/stderr-only writes; `:1850-1875` locates fixture expectations; `:1984-1998` declares `--repo`, `--selftest`, `--frozen`, and `--pin`. The existing frozen expectation files were located at `.ufo/waves/round-15/frozen/r15-pre-003400/expected.json` and `.../r15-post-012710/expected.json`. Static interface discovery is not a successful replay.
5. **Proposed resolution → same evidence interface.** Per `context.md:5`, child rows remain in child `SKILL.md`; the two main-repo lanes use explicitly lane-owned root `SCORECARD.md` sections. Register only the existing protocol closure gate, before `## Aggregator lane`; preserve all aggregator bytes. Neither a fake root skill nor the routed-defect ledger is a valid repair.

## Proposed axes and verdict conditions

These are proposed round-plan evaluation dimensions, not new scored fleet axes. `MISSION.md:38-46` and `AXES.md:25-31` require one measurable axis-move; L1 declares the round's set.

| Dimension | Acceptance condition for L1 verification | Falsifier / unavailable evidence |
|---|---|---|
| **protocol-soundness — selected move** | Registry and Delivery agree on homes for both main-repo lanes and children; protocol row is discoverable at its declared, owner-specific home with all fields. | Either clause still universally requires root `SKILL.md`; only protocol gets an exception; row is missing, ambiguous, or in the ledger. Sources: `PROTOCOL.md:382-402`, `SCORECARD.md:95-100`. |
| **gate-integrity — held invariant** | Keep existing implementation, expected values, exit semantics, qualified frozen names, and revision-bearing two-evidence obligation. Parent records actual post-integration results. | New implementation/re-pinned expectations, undeclared exit, legacy/unpinned or tampered inputs treated as comparable, or self-test green substituted for measurement. Sources: `PROTOCOL.md:364-381`, `SCORECARD.md:101-105`. No score increase follows from registration alone. |
| **ownership and non-regression — constraint** | Child homes unchanged; protocol row stays before aggregator section; aggregator bytes and external/runtime surfaces unchanged. | Child relocation, copied inventory/expected values in the ledger, aggregator edits, or routing/runtime mutation. Sources: `context.md:5-10`, `PROTOCOL.md:384-392`, `SCORECARD.md:132-138`. |
| **evidence/calibration — constraint** | Distinguish historical claims, static facts, and actual new runs; attach command/output/revision to new measurements. | Unrun pass claims, anonymous moving-tree verdict, or literal row count treated as semantic conformance. Sources: `SCORECARD.md:9-20,95-100`, `PROTOCOL.md:374-381`. |

## Minimal acceptance skeleton — ordered steps and evidence

1. **Resolve the contract in its existing two locations.** Contract owner aligns Registry and Delivery, retaining the eight fields: name; `gate|probe`; entry command; code→class map; self-test command/spelling; pinned-value path; write scope; owner. Evidence: integrated `PROTOCOL.md` clauses and corresponding incident/reference corrections in the required paired appendix (`PROTOCOL.md:504-505`). No unrelated gate or prompt semantics change.
2. **Land the representative row.** Registry owner adds `closure-check`, `gate`, owner `protocol`, root-cwd entry `python3 .ufo/waves/round-15/closure-check.py`, self-test `python3 .ufo/waves/round-15/closure-check.py --selftest`, and complete map `0→clean; 1→failed; 2→could-not-evaluate; 3→could-not-evaluate (no-baseline)`. Pin pointers resolve to `.ufo/waves/round-15/fixtures/closure-sample/*/expected.json`, both named frozen `expected.json` files above, and `.ufo/history-pin.json` for live history evidence. Write scope is stdout/stderr only, not permission to modify inspected surfaces. Evidence: row-to-source/path resolution, using script lines cited above; no copied expected values.
3. **Generalize without expanding implementation.** Read the new rule as a protocol reader, an aggregator reader, and a child reader. Both main-repo owners must resolve to their respective section of the shared scorecard; children must still resolve to their own skill. Aggregator home usability is a contract property here, not authorization to insert or migrate aggregator gate rows. Evidence: home/owner mapping, both contract clauses, and unchanged aggregator/child bytes.
4. **Parent-only verification after the batch.** Resolve every row citation and use the existing paired-protocol verifier, reporting any archival exact-text overfit rather than re-pinning its wording. Run the registered closure self-test and these two frozen commands once against the integrated, named revision:
   - `python3 .ufo/waves/round-15/closure-check.py --frozen round-15/r15-pre-003400`
   - `python3 .ufo/waves/round-15/closure-check.py --frozen round-15/r15-post-012710`
   `SCORECARD.md:85,87,90` historically claims pre exit 1/debt 17 and post exit 0/debt 0, plus 27/27 self-tests. These are comparison expectations, not this round's results. Acceptance requires actual output, matching frozen expected verdicts and input digests, plus self-test capability evidence; pre's expected red verdict is not itself a registry defect. `PROTOCOL.md:393-398` keeps gate redness status-neutral unless an existing round rule says otherwise.
5. **L1 measures and records only observed deltas.** Compare baseline missing-home/missing-row evidence to resolved homes and the integrated row, carrying the measured revision; update only parent-owned score/measurement, log, report, and closure surfaces. Evidence: exact before/after contract pointers and recorded commands/results. Historical `round-15` paths and frozen names remain unchanged; current protocol round stays 14 (`context.md:2,5`).

## One-case overfit and generalization falsification matrix

| Case | Required result of the contract/registry review | Reject this overfit |
|---|---|---|
| Protocol, missing root `SKILL.md`, existing closure script | Resolve to protocol-owned scorecard registry; all eight fields and paths resolve. | Create a root skill, point only at the executable, or count an exact pipe-row spelling as proof of conformance. |
| Aggregator, same missing root skill and same cwd | Rule resolves to aggregator-owned scorecard section without touching its bytes this round. | Protocol-only exception or shared unowned registry; do not claim an aggregator gate was registered. |
| Child lane with its own skill | Registry and Delivery still require that lane's own `SKILL.md` row. | Move all fleet rows to the root scorecard or ledger. |
| Main-repo row placed under the wrong owner | Ownership review rejects it despite the file existing. | File-existence-only or gate-name-only acceptance. |
| Row missing exit 3, self-test spelling, pin path, scope, or owner | Schema review rejects incomplete declaration. | Treat prose saying “registered” as a complete interface. |
| Self-test cited without frozen input evidence or revision | Evidence review withholds conformance claim. | Reuse historical 27/27 or a live clean verdict as new two-evidence proof. |
| Archived checker rejects changed incidental wording | Parent reports exact overfit and underlying semantic obligation separately. | Rewrite the committed expectations merely to turn an archival text check green (`context.md:10`). |

## Assumptions and hard blockers

- No hard blocker to this plan was found in the inspected sources. Post-integration verification and committed-evidence availability remain unverified, not successful outcomes.
- The baseline revision/output in `before.json` and historical scorecard tallies are attributed records, not proof that the moving worktree equals those revisions. Parent must bind its new evidence to the measured tree/revision.
- This artifact does not authenticate resumed-run continuity or a last-known-good runtime; inherited round-15 names are historical evidence identifiers, not authority to renumber the assigned round or enlarge its scope.
