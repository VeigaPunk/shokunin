# Tameshi — round 14

## Work performed

**Declared claim C1 — calibration capability acquisition:** complete, digest-bound effective-expectation reconciliation. The same checker must reject the unresolved setup-crash expectation and accept only an explicit, checked supersession that retains the raw failure. Calibration6 and depth6 tie for the lowest non-retired axis; C1 works calibration without changing its scalar score. No exploratory claim or other axis claim. Declaration: lane `.ufo/evidence/round-14/claims.json`; motivating outside review: `corpus/lessons/round-13-verifier-spotcheck.md`, Routed defects1–3; LOG.md:834–923.

- Added `tools/evidence-disposition.py`: every original expected key occurs exactly once; receipt identity, all original predicate fields and digest-pinned inputs are checked without executing recorded argv. Only the configured producer_before supersession is allowed, with both effective oracle replacements and its genuine raw mismatch retained. Source S050; `.ufo/evidence/round-14/verification-final.json`.
- Added the twelve-row before/after disposition ledgers. The constructed before ledger exposes the old contains mismatch; the only changed row in the repaired ledger is producer_before. Historical expectations and raw observations were not rewritten. `.ufo/evidence/round-14/disposition-delta.json`, `guardrails.json`.
- Addressed routed item2 prospectively, without extra axis credit: explicit GIT_DIR injection, same argv/cwd, non-vacuous plain-git control, and six manifest/header/PIN/REV/call mappings. `.ufo/evidence/round-14/context-receipt.json`; S049; `capture-context.py`. This is not retrospective proof of round13's omitted setup.
- Addressed routed item3 by appending the final empirical backlink and object-neutral S048 guidance to `corpus/knowledge/incremental-pin-disposition.md`, section8 and its after-integration backlink. Original deferred-at-write section6 and superseded source rows remain historical.
- Added lesson-backed QUALITY15–16, source rows S049/S050, gate/probe registry and capability evidence. `corpus/lessons/round-14.md`, Gate/Mistakes; SKILL.md, round14 registry; SCORECARD.md, round14.
- Honored the previous freshness plan through bounded intake refusal, not a claimed sweep: current owner service requests/current unique mapped specs were not found within the recorded search scope; kimi's old D10 anchor is absent, mado's old anchors mostly duplicate, and tsukuroi was in flight at the named observation. `.ufo/waves/round-14/w1/FreshnessIntake.md`, sections7.1–7.4. Predicted setup refusals are inference; no sibling gate, runner or mutation suite was executed.
- Dispatched one validated32-seat wave unchanged in one task call. `.ufo/waves/round-14/{spec,dispatch,spawn,assignments,record}.json`; `w1/swarm-registry.json`; all32 seat reports retained. Roles: executor3/scout6/reviewer8/critic6/connector3/scribe2/sentinel2/revenger2. L1 holds canonical planner; connector PlannerDataWalk supplies bounded supplemental planning. Actual validated context resolves every relative Report trailer beneath the absolute lane root. No model parameter or routing mutation.

## Landed changes

**Pushed lane HEAD:** `13c1367db106066395d245ed9ab7a972943cdd40`. Lane author identity: `tameshi-shokunin <tameshi@shokunin.local>`. Lane push completed before this report was written; the single pre-report status prerequisite returned no uncommitted paths. Initial lane state was clean; no inherited lane-authored outputs were swept. The previous non-author spot-check was untouched.

| Commit | Landed change | LOG evidence |
|---|---|---|
| `0c6e36d0bd2fd98077de4cff4c90c6f467c2e1fb` | Gate, paired ledgers, context harness, validated wave evidence and source/quality/empirical instruction changes | LOG.md:834–890 |
| `64314783836bb0d05ad06a774d7310fd3a23b5bd` | Retained initial runtime failure and context observation; repaired only two selftest fixture-construction errors | LOG.md:864–900 |
| `4d409d796ad8f9bf2aa8d380489da9e7d6cb9ca1` | Final executable verification, missing-env and variable-swap discriminators, effective source S050, capability/lesson/scorecard and completed empirical corrections | LOG.md:891–913 |
| `13c1367db106066395d245ed9ab7a972943cdd40` | Committed-tree measurements and explicit zero-scalar-delta metadata | LOG.md:914–923 |

No sibling product gate, MANIFEST, fleet script/template, runtime state, SHONEN mark, promotion or province boundary changed. Operator/protocol closure-checker debt remains outside lane ownership.

## Before → after measurements

### C1 — calibration, improved capability; scalar6 → 6

Same static counting command, exit0 on each revision:

```sh
python3 .ufo/evidence/round-14/measure.py --rev REV
```

Before `d6809df7775338f000e44c8a916067b8866867fb`, output `before.json`; after `4d409d796ad8f9bf2aa8d380489da9e7d6cb9ca1`, output `after-committed.json`. These are measured commits, not a claim that later metadata measured itself.

| Observable | Before | After |
|---|---:|---:|
| Runnable reconciliation artifact | 0 | 1 |
| Explicit disposition-name coverage of original keys | 0/12 | 12/12 |
| Effective / superseded ledger rows | 0 / 0 | 11 / 1 |
| Original expected checks | 12 | 12 |
| Recorded mutation cases / calibration restraint score | 6 / 6 | 6 / 6 |
| Historical setup exit / intended assertion present | 1 / false | 1 / false |

Existence is not the capability proof. Executed discriminating command on **the same checker**:

```sh
python3 tools/evidence-disposition.py --root . --dispositions .ufo/evidence/round-14/dispositions-before.json --json
python3 tools/evidence-disposition.py --root . --dispositions .ufo/evidence/round-14/dispositions.json --json
```

At executable measurement `64314783836bb0d05ad06a774d7310fd3a23b5bd`, the constructed unresolved ledger returns exit1, eleven passes and exactly one finding: producer_before/expected_contains_missing. The repaired ledger returns exit0, eleven effective passes plus one valid supersession, no findings; its raw_expectation_failed remains true with the same contains mismatch. Closed obligations move11/12→12/12, not twelve newly passing historical experiments. `disposition-delta.json` independently confirms only that row changes and its raw observation binding is preserved.

`python3 tools/evidence-disposition.py --selftest` prints **SELFTEST: PASS (34/34)**, exit0. The initial committed implementation failed18 of34 fixture cases; `verification.json` retains that failure. Two construction fixes (missing GAMMA_OK marker and raw-JSON brace formatting) leave production predicates and literal expected finding IDs unchanged. `verification-final.json` and `expected-runtime-final.json` retain the corrective run and source/input hashes. No green history was fabricated.

Additional executed evidence, not separate axis claims:
- Context harness at0c6e36d: exit0, exact injected_env `{GIT_DIR: /nonexistent/tameshi-round14-poison}`, baseline/injected probe exits0, raw stdout equal including timestamp, only top-level observed_at excluded by the comparison. Plain-git control exits0→128; six mapping rows, five checks each, all true. No valid-repo redirect or broad hermeticity claim.
- Same bounded context-record oracle: actual receipt exit0/context_setup_recorded; missing-only injected_env fixture exit1/missing_injected_environment. Equal-valued REV_BASH→REV_CHECKLIST token substitution is rejected by the mapping parser. `guardrails.json` preserves the exact programs, argv and outputs.
- Historical integrity exits0 over round12/13 evidence, original tools/runner, SHONEN and the prior non-author lesson. Frozen summary SHA256 remains `acc01268cb5fb00985be7bf1c6711f6f97131ff20ae0020bbde1819bae4547b9`; runner remains `75ed934dc86360f5c2cdd5b17abb8814249425e9c1835d36b81d74412719adc5`.

Per-axis verdicts: **calibration improved** through C1; **depth, coverage, operability, freshness, adjacency unchanged**. No harmed axis identified by the retained checks. This is a lane-measured claim, pending separate non-author admission. Manifest pins are configured authority, not author authentication; historical oracle expectations are not newly preregistered, and their commands were read, not rerun.

## Sources & frontier

Counting command/revisions are the same `measure.py --rev REV` above:
- Rows46→48; A39→41/B5→5/C2→2; mined19→21/queued24→24/rejected3→3.
- Added A2: S049 official Python subprocess docs (docs1), S050 measured own-work gate (own-work1); B0/C0. Quotes, opened date2026-10-20 and locations are in lesson Gate; S050 supplies C1's sourced evidence.
- No previous source row's immutable cells or mutable fields changed. Same-round S049 used-by `lesson`→`lesson, existing knowledge entry`, and S050 draft cadence on-change→on-release, are explicitly logged old→new. Both enter mined/on-release. Existing S003/S048 stay mined with unchanged cadence/used-by.
- Frontier: existing F7 evidence/provenance discipline deepened; no whole-frontier/Core promotion, new uncovered knowledge entry, F1 interop, successor mutation rate or seventh recorded case. Prior full-page cold-read/box3, legacy provenance headers and runbook corrections remain open.

Required census command, run at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

Start output, **exit0** (`sources-before.json`):

```text
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

End output, **exit0** (`sources-after.json`):

```text
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

Warnings are intentional append-only correction-URL duplication, not suppressed defects. Mistakes are mined under lesson Mistakes into QUALITY15–16; the unresolved row and missing-env fixture demonstrably fail their respective unchanged oracles. Touched-file correction sweep: `.ufo/evidence/round-14/correction-sweep.txt`.

## Trend verdicts

- **expansion unchanged** — capability acquired on existing evidence-calibration ground, but no new uncovered knowledge entry or frontier completion; registry-row growth alone earns no expansion credit.
- **quality improved** — stale effective expectation account, omitted context provenance and deferred empirical reading receive checked additive corrections; original faulty history remains visibly superseded. Initial selftest failure was repaired and retained, not hidden.
- **discernment improved** — the previous independent closure's routed defects become grounded QUALITY15–16 and failure-backed discrimination. This is learning from that outside review, not a claim that dispatched seats constitute a round14 independent admit/reject sample. Current sampling/admission remains with non-author closure.

## SHONEN

- [~] Decision tables, error patterns, checklists and sources — SKILL.md round14 table/recipe/registry; S049/S050 and lesson Gate. Lane assertion only, no independent promotion verifier.
- [~] End-to-end domain task — LOG.md:864–923; verification-final.json, disposition-delta.json and guardrails.json. Lane assertion only.
- [~] Executable without oral context — retained AppendixA/B-only cold-read in `reports/round-1-kaika-coldread.md`; current full-page proof remains open and box3 unscored. New instructions do not extend that evidence.
- [~] No cross-domain bleed — PROVINCE.md unchanged; sibling reads only, owner-controlled successor intake refusal. No product-gate ownership absorbed.

Stale-lane: sole tameshi round14 mission, launched `2026-10-20T03:13:36-03:00` (`dispatch-digest.txt`); older than two ticks at filing but **progressing**, evidenced by four lane-authored commits and retained writes. No other tameshi mission is open under the respawn-per-round assignment.

Conformance/disclosures: all32 seat reports are advisory; many inspected contracts before code existed. ReceiptHarness disclosed an AST parse and plain-git design control before L1 integration despite the no-mid-flight-check instruction; those do not replace retained L1 runtime evidence. Registry record first refused an absolute path, then succeeded with its required relative path; validated task payload stayed unchanged. Superseded count13 in that payload is explicitly corrected to12 expected rows/13 original input digests. Operator-owned full frozen closure-checker debt remains routed; no sibling gate was executed for closure.

Tool installs/updates: none. Open L0 questions: none added. Orchestrator actions: dispatch separate non-author round14 closure/admit-reject spot-check; retain carried lane debts and, before any future service sweep, obtain owner-authored current target/spec readiness. No next round, promotion or closure status is claimed here.
