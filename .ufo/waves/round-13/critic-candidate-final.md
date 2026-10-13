# Round-13 rebased candidate critique

## Commands and scope

The rebased source was read from `PROTOCOL.md:8-541`; body from `.ufo/waves/round-13/PROTOCOL.compact.md:1-459`; sibling from `.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md:1-40`. The candidate body is 459 lines and the single-file candidate 493 lines, per the integrator message. I did not edit candidates.

## Re-check rulings

### 1. Lifecycle / sibling mint — SAME, but one presentation defect

Source (`PROTOCOL.md:23-37`) requires, in order: scan `MANIFEST.json` and every `PROVINCE.md` and record the rejected roster map; create `{id}-shokunin/` and its GitHub remote; seed `SKILL.md`, `PROVINCE.md`, canonical-template `SHONEN.md`, `AGENTS.md`, `LOG.md`, and `MINT.md` with reasoning/cause/demand evidence/rejected fit/boundary; wire `LANE_CWD`/`LANE_MODEL`/`LANE_AXES` with operator-side route-map escalation; self-iterate through at least three verified rounds building `corpus/` + `PROVINCE.md`; only then add `MANIFEST.json` and `ROADMAP.md` rows, with probation in `rounds[].notes`; and prohibit writes outside the minting lane's repo/seed files and prohibit roster or sibling post-seed edits.

Candidate (`PROTOCOL.compact.md:21-35`) contains all of those predicates and ordering: “In order: (a) scan `MANIFEST.json` + every `PROVINCE.md`…; (b) create… seeding… plus a `MINT.md`…; (c) wire it into the driver…; the sibling self-iterates through at least three verified rounds… before roster rows exist; (d) only after those rounds land…; The minting lane never writes outside…” **SAME** for obligation preservation. The candidate has a textual typo, `- - **Sibling mint`, which is a malformed list marker but does not narrow the rule. Fix it as hygiene: `- **Sibling mint…`.

### 2. Marker consequences — SAME

Source (`PROTOCOL.md:174-183`) says a marker is a no-work report; integrator records `failed`, **keeps the marker file as a conformance defect**, and **names counter advancement**; a real committed hash is `ok` plus minimum-content defect; an uncheckable marker is failed; and “This does not relax step 1.” Candidate (`PROTOCOL.compact.md:142-150`) says the same marker definition, “records… `failed`, keeps the marker file as a conformance defect, and names the counter advancement,” the same real-hash distinction, and failed uncheckable marker. **NARROWED only because the candidate omits the final source sentence “This does not relax step 1: contract violations inside a real report stay status-neutral defects.”** Exact accepted correction after candidate line 150:

> `This does not relax step 1: contract violations inside a real report stay status-neutral defects.`

This is HIGH: it prevents a consumer from treating “real report” as exempt from contract checks.

### 3. Appendix path in write scope / file contract — LOST

Source integrator sentence (`PROTOCOL.md:185-193`) lists main-repo writes and exactly six, ending with `.ufo/history-pin.json`. Candidate (`PROTOCOL.compact.md:151-161`) likewise says “expand by exactly six” and lists no `PROTOCOL-APPENDIX.md`. Candidate file contract (`PROTOCOL.compact.md:358-368`) lists only the seven child-repo contract rows; no root appendix row exists. The body does say the digest “moved to the committed sibling artifact `PROTOCOL-APPENDIX.md` (repo root, protocol-owned)” (`:455-459`), but this is not an ownership/write-scope rule and does not say the protocol lane commits it.

**Verdict: must fix, CRITICAL.** Exact wording accepted in the integrator paragraph (and adjust “exactly six” to “exactly seven,” or explicitly classify appendix as part of the closure-gate artifact set):

> `The protocol lane also writes and commits the protocol-owned root file PROTOCOL-APPENDIX.md as the required sibling of PROTOCOL.md; this is part of the closure-gate artifact set and is not an ordinary lane write.`

Add a root-artifact contract row:

> `| PROTOCOL-APPENDIX.md | Protocol-owned incident digest; REQUIRED sibling input for appendix-pointer verification; append-only incident rows and the body’s first-column rule keys |`

If the integrator insists that the appendix is included in “closure-gate artifacts under `.ufo/waves/round-<N>/`,” the exact sentence must instead say that the root sibling is committed by the protocol lane as part of that set. Silence is not acceptable.

### 4. Cross-file pointers — verifier fixed, cold-reader contract still incomplete

The new verifier result is accepted as evidence: `sh .ufo/waves/round-13/verify-protocol.sh <body> --appendix <sibling> --max-lines 460` reportedly returns `clean checks=9 failed=0`; self-test is 12/12 two-file and the missing appendix fails closed. That resolves the mechanical check.

The candidate pointer block (`PROTOCOL.compact.md:455-459`) says the digest moved to root `PROTOCOL-APPENDIX.md`, is protocol-owned, gives the wave copy path, and says every pointer resolves by first column. The sibling preamble (`PROTOCOL-APPENDIX.compact.md:1-5`) says the rows motivate a rule in `PROTOCOL.md` and every `(§Appendix, "X")` resolves to a first-column row. The 16 distinct pointer labels found by:

```sh
grep -o '(§Appendix, "[^"]*")' .ufo/waves/round-13/PROTOCOL.compact.md | sort -u | wc -l
```

are mechanically checked by the new mode. **SAME mechanically; NARROWED for cold-reader semantics.** `§Appendix` is still a section reference, but the body’s `## Appendix` is only a pointer block and not the rows. A reader holding the body can follow the explicit root path; a reader holding only the sibling cannot resolve body section/rule context. This is acceptable only if the pair is declared REQUIRED together. Add to the pointer block:

> `PROTOCOL.md and PROTOCOL-APPENDIX.md are a REQUIRED pair for protocol reading and verification; a reader or gate MUST fail closed if either is absent. “§Appendix” means the sibling file’s first-column rule key, not an in-body incident table.`

Reverse direction has no dangling section references in the 40-line sibling; its preamble's `PROTOCOL.md` dependency is now explicit under this pair rule.

### 5. Citation migration and quantified cost

A clean sweep excluding synthetic mutants was run:

```sh
find . -path './.git' -prune -o -path './.ufo/waves/round-12/mutants' -prune -o -type f -print | xargs grep -nHE 'P:[0-9]|PROTOCOL\.md:[0-9]' | wc -l
395
find . -path './.git' -prune -o -path './.ufo/waves/round-12/mutants' -prune -o -type f -print | xargs grep -lHE 'P:[0-9]|PROTOCOL\.md:[0-9]' | wc -l
64
```

This total includes already-stale citations and nonnumeric prose, so it is not a count of newly broken references. The named `.ufo/waves/round-12/closure-check.py` docstring has the 10 requested ranges (`P:202-260`, `P:215-224`, `P:150-155`, `P:124-136`, `P:206-213`, `P:218-221`, `P:224-228`, `P:244-249`, `P:256-260`, `P:209-213`) and its runtime finding strings include further numeric `P:` anchors visible in the sweep. All numeric line ranges become unsafe after compaction; migrating them to section/rule names in the same landing commit is the correct fix.

Child-repo citations that break or remain invalid include `kumitate-shokunin/scripts/round-gate.mjs` `PROTOCOL.md:263-267` (owner kumitate; already stale), and child/report evidence cited in `.ufo/waves/round-11/protocol-reference-sweep.md` (`:101-102`, `:292-298`, `:394`, `:453-454`) and `.ufo/reports/round-9/aggregator.md:175` (`:434-435`). Those owners must migrate their own artifacts; the protocol lane must provide stable section/rule names and route the defects. Do not claim all 395 lines are new damage. Gate evidence strings specifically contribute at least the 10 closure-check docstring ranges plus its runtime templates.

### 6. Prompt fidelity and ledger warning — NARROWED / LOST

Source prompt rule (`PROTOCOL.md:86-97`) says prompts embed the operative contract verbatim, names the five child items and aggregator set, and explicitly says a prompt-fidelity defect in notes does not fix the template; the integrator report **must also carry the exact corrected `lane_prompt()` text**. Candidate (`PROTOCOL.compact.md:71-80`) retains the contract items and exact corrected-text duty, so this is **SAME**.

Source aggregator rule (`PROTOCOL.md:315-319`) says the report is incomplete unless the ledger was refreshed or explains why no row changed, and “a round filed without the ledger duty keeps the routed-defect queue empty by construction.” Candidate (`PROTOCOL.compact.md:273-280`) retains the incomplete-report condition but deletes the “empty by construction” warning. **NARROWED.** Accepted correction after the candidate’s sentence about no row changing:

> `A round filed without the ledger duty keeps the routed-defect queue empty by construction.`

### 7. History-pin placement — current placement is defensible, but add cross-reference

Candidate puts history pin under Round-robin closure step 4 (`PROTOCOL.compact.md:262-265`), where the integrator appends `MANIFEST.json` rounds. That is the strongest location because the pin protects the closed `rounds[0:k]` prefix and is produced as a closure act. `## Gate standard` should define what a gate verifies, not own the integrator’s mutation/append duty. **Rule: retain placement in Round-robin step 4.** Add one Gate-standard cross-reference so the verifier contract is discoverable:

> `The closure gate MUST verify the history pin as committed evidence; pin failure is a conformance defect routed under Closure consequence.`

Do not duplicate the pin algorithm in Gate standard.

### 8. `type: "mint"` — MUST be defined

`MANIFEST.json:859` contains the observed entry:

```text
   "type": "mint",
```

The candidate round-entry shape (`PROTOCOL.compact.md:198-201`) says `type` is optional and the status vocabulary is for `lanes`, but does not define a mint-only entry with no lane rows. The committed checker reportedly silently skips it. That is a protocol ambiguity: consumers may either reject it as malformed or accidentally omit a real closure event. **HIGH must-fix.** Add after the round-entry shape:

> `A mint entry MAY use type: "mint" and carry no lanes map only when it records a lane-initiated sibling mint; it MUST carry the mint evidence pointer, the probation/rounds[].notes reference, and the resulting roster/ROADMAP transition (or explicitly state that the transition is pending). It is not a lane-round closure row, is excluded from lane status tallies, and MUST NOT be silently skipped by a gate: the gate records and reports it as a recognized non-closure entry.`

If `type: "mint"` is intended to be a normal closure entry instead, require `lanes` and define its status semantics; do not leave the current silent skip.

## Final verdict

**Land with named fixes; do not land as-is.** The rebased candidate now preserves the sibling-mint bullet and marker consequences mostly survive. The remaining blockers are the undocumented root appendix write/contract, the missing final marker status-neutral sentence, the missing ledger “empty by construction” warning, and undefined mint entry semantics. The two-file verifier mode and fail-closed missing-appendix behavior are real improvements and remove the earlier mechanical-pointer blocker, but they do not substitute for protocol text.

## Must-fix list (one edit pass, ranked)

1. **CRITICAL — root appendix ownership and contract.** Add the exact `PROTOCOL-APPENDIX.md` protocol-lane write sentence; make the root sibling a file-contract row; state pair-required reading/verifying. Either change six to seven or explicitly include the root appendix in the closure-gate artifact set.
2. **HIGH — define `type: "mint"`.** Add the exact recognized non-closure semantics above; change the verifier from silent skip to explicit recognized handling.
3. **HIGH — restore marker consequence.** Add the exact “This does not relax step 1…” sentence.
4. **HIGH — restore ledger warning.** Add “A round filed without the ledger duty keeps the routed-defect queue empty by construction.”
5. **HIGH — stable citation migration.** Migrate the 10 closure-check docstring ranges and runtime finding strings; route the named child-repo/report citations to owners; record the clean 395/64 sweep with mutants excluded.
6. **MEDIUM — pointer cold-reader clause.** Add the REQUIRED-pair and fail-closed wording; retain history-pin placement and add the one Gate-standard verification cross-reference.
7. **LOW — fix malformed list marker.** Change candidate `- - **Sibling mint` to `- **Sibling mint`.

The capability additions (169-row census, two-file verifier/selftests, history pin, frozen baselines, mutation evidence) do not change blocker 1’s score logic: compaction remains debt repayment, not a protocol-soundness score increase, until the named semantic and ownership fixes land.

DESPAWN: gx-critic-candidate — signal delivered. Send me shutdown_request.