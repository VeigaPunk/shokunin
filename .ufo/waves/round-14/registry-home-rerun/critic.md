# Round 14 registry-home rerun — adversarial review

## Scope and evidence boundary

Read-only review of one proposed move: declare the main-repo lanes' owner-separated registry home and register the existing protocol closure gate. No gate/runtime/routing changes, executions, tests, selftests, formatters, ledger edits, native judgment or promotion verification performed. This file is the only write.

Binding sources read: root `MISSION.md`, `AXES.md`, and `registry-home-rerun/context.md`. Axes under review: **protocol-soundness** (the intended improvement), **gate-integrity** (must not regress), and the evidence-quality dimensions **operability**, **calibration**, **freshness**, **adjacency**. No saturation claim follows from this move.

Fresh measurement authority is `registry-home-rerun/before.json`: commit `99efc52b3a6f3648f7d8e097d78460901ad3c91c`, recorded stdout `protocol_registered_closure_gates=0\nroot_SKILL_exists=False\n`, return code 0. Those are the parent's captured results, not commands re-executed by this critic. At my source inspection checkpoint, `PROTOCOL.md:382-402` still required `SKILL.md` in both Registry and Delivery, and no closure registry row was present in `SCORECARD.md`. The findings below attack the proposed design; they do not claim to certify the later integrated edits.

Inherited `registry-home/live-closure.json` is read-only evidence from commit `e163d15bb1b080ae567ada3b86441455e9808f9b`, not a fresh rerun result. Its captured command was `python3 .ufo/waves/round-15/closure-check.py --repo . --json --no-citations`; return code 1, stdout empty, stderr traceback ending `TypeError: '<' not supported between instances of 'NoneType' and 'int'`. The assignment identifies the historical `round:null` trigger. This failure is ground truth and was not rerun.

## Named counterexamples

### C1 — A registered row under the wrong owner

**Counterexample:** Add a correctly formatted closure row after `## Aggregator lane`, put the inventory in `.ufo/reports/AGGREGATE.md`, or invent root `SKILL.md` to satisfy the old wording. Alternatively, put a row before the boundary but name the aggregator as owner. None registers the protocol gate at its own authoritative home.

**Evidence:** `SCORECARD.md:3-7` assigns the upper section to protocol; `SCORECARD.md:132-138` assigns the lower section to aggregator and explicitly discusses shared-path collision D-77. `PROTOCOL.md:384-385` keeps the aggregator ledger a routed-defect queue, not another inventory; `PROTOCOL.md:449-450` already permits both main-repo lanes' root scorecards. The fresh baseline records root skill absence. The gate's module description names the protocol lane (`closure-check.py:2`).

**Impacted axis/invariant:** protocol-soundness, adjacency; single owner/authority, unchanged child homes, protected aggregator bytes.

**Smallest correction:** Put one explicitly protocol-owned registry subsection and row before the existing aggregator boundary; owner `protocol`. Define aggregator's own subsection as its allowed home without fabricating an aggregator gate or modifying its current section. Keep child rows in each child's `SKILL.md`; keep the ledger pointer-only with respect to inventories. Parent must preserve the existing aggregator section byte-for-byte, using the fresh baseline's section digest `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf` as its recorded comparator.

### C2 — Registry moves, Delivery still forbids the move

**Counterexample:** Change Registry to root `SCORECARD.md`, leave Delivery requiring the lane's `SKILL.md`. The new row exists, yet closure still cannot acknowledge that home. A numeric 0→1 count conceals an unresolved normative contradiction.

**Evidence:** Original `PROTOCOL.md:382-387` defines Registry; `:399-402` separately conditions conformance on a row in the lane's own skill. Root skill is absent. `SCORECARD.md:95-100` already names this exact falsifier.

**Impacted axis/invariant:** protocol-soundness; Registry/Delivery agreement and no second authority.

**Smallest correction:** Update both clauses coherently: child `SKILL.md`; protocol/aggregator explicitly lane-owned root `SCORECARD.md` subsections. Delivery may refer back to the declared Registry home, but must not retain an unconditional skill-only requirement. This changes the necessary registry-location condition, not the sufficient conditions for full gate conformance.

### C3 — Prefix-count success with an unusable or incomplete row

**Counterexample:** `| closure-check | gate | nonexistent-command |` increments the fresh baseline's literal-prefix count. The same counter accepts six missing schema fields, wrong owner, `--self-test` instead of `--selftest`, or an entry invoking the old round-12 checker. Thus its result alone cannot prove registration quality.

**Evidence:** `before.json:9` counts only lines starting `| closure-check | gate |` before the first aggregator heading. The eight required fields are in `PROTOCOL.md:382-384`. Actual parser spelling is `--selftest` (`closure-check.py:1989-1990`); selftest fixtures are rooted relative to the selected script (`:1850-1852`). The assignment selects `.ufo/waves/round-15/closure-check.py`, not an older checker.

**Impacted axis/invariant:** operability, calibration, protocol-soundness; complete schema and executable identity.

**Smallest correction:** Keep the prefix count as a narrow row-count metric only. Alongside it, establish that exactly one owner-correct eight-field row names a complete root-relative command such as `python3 .ufo/waves/round-15/closure-check.py --repo . --json`, the real selftest command `python3 .ufo/waves/round-15/closure-check.py --selftest`, and precise persisted-value paths. The live command's existence is not a claim that it currently completes successfully. No new implementation is needed to improve discoverability honestly.

### C4 — Frozen names resolve, but the evidence is absent or not the claimed evidence

**Counterexample:** Cite an `expected.json` path that does not exist, cite the older unpinned round-12 snapshots, use ambiguous bare snapshot names, or call historical round-15 frozen cleanliness current live cleanliness.

**Evidence:** `_resolve_frozen` recognizes `<wave>/<name>` at `closure-check.py:1013-1018` and rejects ambiguous bare names at `:1024-1026`. The required actual files exist under `round-15/frozen/r15-pre-003400/` and `round-15/frozen/r15-post-012710/`. Pre `expected.json:89-97` persists exit 1, 17 debt triples and six input digests; post `expected.json:2-11` persists exit 0, empty debt and six input digests. Each directory contains the six named inputs plus `expected.json`. Source `:1800-1818` checks declared digests; `:1828-1839` compares debt triples and exit. `load_frozen` explicitly disables citation/ancestry checks (`:449`); history-pin checking distinguishes live from frozen (`:935-936`).

**Impacted axis/invariant:** gate-integrity, freshness, calibration; persisted baselines, named revision, no false provenance.

**Smallest correction:** Cite exact paths and replay selectors `round-15/r15-pre-003400` and `round-15/r15-post-012710`; include fixture expected values and the live `.ufo/history-pin.json` as distinct pin roles, not as interchangeable authority. Frozen exit 0 means only the bounded snapshot's expected closure-debt result, not full live conformance, current citation validity or current history-pin validity. This critic inspected path/schema presence, not recomputed snapshot digests or replay outcomes; fresh execution evidence belongs to the parent's integrated pass.

### C5 — An exception's process exit is mistaken for a gate verdict

**Counterexample:** Report inherited live exit 1 as ordinary debt/failed, derive lane statuses from it, or map `3 = no-baseline` to fleet `failed`. Worse, advertise registration as a clean live verdict because the historical post snapshot expects exit 0.

**Evidence:** Inherited live artifact has **no stdout and no emitted closure verdict**, only the traceback. Source sorting at `closure-check.py:1143` orders raw round values before the following row checks, matching the recorded exception site. Declared exit map (`:64-75`) is 0 clean, 1 debt/contradiction, 2 could-not-evaluate, 3 no-baseline; fleet Registry requires an outer class for every code (`PROTOCOL.md:364-368`).

**Impacted axis/invariant:** calibration, gate-integrity; verdict provenance, no fabricated closure statuses, status neutrality.

**Smallest correction / claim ceiling:** Registry map: `0 → clean`, `1 → failed`, `2 → could-not-evaluate`, `3 (no-baseline) → could-not-evaluate`. Separately disclose that the known live invocation raised an unhandled exception and produced **no usable verdict or ledger statuses**; its process code alone is not structured debt evidence. Record no writable closure statuses and route the known gate defect to its owner. Do not patch the gate or historical ledger in this move. Historical frozen results remain historical.

### C6 — Existing selftest tally is sold as complete standard conformance

**Counterexample:** Assert that registering the existing selftest command proves the stable-finding-id requirement. The current comparison can accept the same exit and aggregate counts even if the actual finding identity changes.

**Evidence:** `PROTOCOL.md:369-373` requires exit plus a stable expected finding-id. `closure-check.py:1880-1897` builds comparisons from exit and count fields only. `fixtures/closure-sample/keying-violation/expected.json` stores exit/debt/counts, with no expected finding kind or identity. The gate emits a separate `class` and `kind` in `_finding` (`:700-702`), which this comparison does not inspect. **[INFERENCE]** Replacing the keying finding with another one-debt, non-contradiction finding while preserving the compared counts would escape this fixture comparison. No mutation or test was run.

**Impacted axis/invariant:** gate-integrity, calibration; selftest capability versus full conformance, no invented non-author verification.

**Smallest correction / claim ceiling:** Register the actual command and persisted fixture expectations without declaring the complete §Self-test clause proven. Name the aggregate-count limitation as existing gate evidence debt. Strengthening the checker is outside the single home/registration move; neither relax the protocol nor re-pin an archived source-text check to manufacture a green result.

### C7 — A historical marker or sibling work acquires fresh provenance

**Counterexample:** Overwrite the filed round-14 marker, cite inherited dispatch/review text as this rerun's worker evidence, label an author's `[~]` assessment a non-author `[x]`, or treat this critique as the native Rust judge's decision.

**Evidence:** Fresh context explicitly protects inherited artifacts and the filed report prefix; `registry-home-rerun/before.json` records the marker digest `d2567df3f11018ebd168918c46c7ea69119e45e41ac2f58140b1bf5634f691b4`. The existing report is a marker titled `protocol round-14 closeout (marker)`; it is not this fresh move's delivered report. `PROTOCOL.md:430-431` reserves `[x]` for a named non-author verifier; Gate Scope (`:390-392`) says lane-local evidence never substitutes for the native judge.

**Impacted axis/invariant:** calibration, freshness, gate-integrity; append-only report provenance, no authority/identity laundering.

**Smallest correction:** Keep the marker an exact byte prefix and append the parent's post-commit erratum. Reference fresh rerun artifacts separately from inherited failure evidence, with their actual measured commits. Use the canonical four-box assessment with honest asserted/unmet states; this worker supplies neither promotion verification nor a native verdict.

## What would distinguish real improvement from a cosmetic row

The 0→1 claim is meaningful only as **one existing gate newly registered at a coherent, owner-correct, discoverable home**, backed by all of:

1. The fresh committed baseline and its exact prefix-count predicate, not inherited measurements relabeled fresh.
2. Matching Registry and Delivery homes, with unchanged child-home rules and no fake root skill or duplicate aggregator inventory.
3. One complete eight-field protocol row before the aggregator boundary, naming the selected round-15 script, real flag spelling, full outer verdict map, persisted fixture/frozen/history pin paths, stdout/stderr-only write scope, and protocol owner.
4. Precise distinction among command registration, historical frozen expectations, any actually observed integrated replays, the known unusable live invocation, and unproven full standard conformance.
5. Protected executable, snapshots, history pin, historical ledger, aggregator bytes and marker prefix unchanged within this move; the parent owns integrated evidence for those properties.

A home contradiction can be genuinely removed even while the registered gate has an existing operational defect. The smallest safe move fixes the contract/home and discoverability, carries the defect honestly, and holds gate-integrity at its prior level. Calling that registration live clean, full conformance, promotion, saturation or a native acceptance decision exceeds the available evidence. This review supplies counterexamples and correction boundaries only; the canonical judge owns disposition.
