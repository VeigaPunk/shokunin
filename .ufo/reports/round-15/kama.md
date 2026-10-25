# Kama — round 15

## Work performed

**Declared C1 — calibration: executable declared-name duplicate-corpus admission repair.** Calibration7 is the lowest assigned axis versus operability8 (`shokunin.conf` kama row). The runner promised duplicate rejection but enforced only a minimum unique-name count. This round repairs the executable predicate and demonstrates the original defect through actual CLI runs; it is not a wording-only calibration claim. Numeric score **7 → 7, delta0**. No second claim, new capability row or stagnation waiver.

Lane paths below resolve under `/home/vgpnk/Projects/shokunin/kama-shokunin`. **Pushed lane HEAD:** `b8bdc56efc43fe6baad9415d0ca75b7b81ffa952`. **Measured implementation:** `4b1b4ad1ba31660cc44c82d204dc85c1355e36d2`. The final lane commit carries the receipts and ledger append, not a different implementation. Lane status output after push was empty.

- Added the missing preflight comparison between declared-name and stripped-unique-name counts, before the child branch. Preserved the existing minimum and classifier policy; narrowed active prose to nonblank string declarations rather than promising new schema validation. Evidence: `.ufo/waves/round-14/measure.py`; `corpus/lessons/round-14-verifier-spotcheck.md` R1; `.ufo/waves/round-15/fidelity.json`.
- Added independently authored literal corpus-guard controls and a CLI harness executing the actual runner and actual classifier. A wrapper-entry marker and runner-side audit events are separate observations; `_posixsubprocess.fork_exec` is included. No fake classifier or live runtime is used. Evidence: `tests/ollama-corpus-guard/`; `.ufo/waves/round-15/run-{before,causal_red,after,selftest}.json`.
- Preserved the exact original runner and a separate derived predicate-only red control. Direct Git-blob correspondence and a literal expected digest are checked independently of the new manifest; the derived control is final source minus only the two guard lines, not historical provenance. Evidence: `.ufo/waves/round-15/frozen/`; `fidelity.json`; lesson §Historical locator and control-execution precision.
- Learned outside R1 through KQ18 and appended a named correction to the historical receipt/prose promise without rewriting the old receipt. Learned outside R2: substantive committed advice does not prove terminal success, and a provider failure does not imply absent output. Discovery remains CloseKamaR14's; this round earns no discovery credit. Evidence: `corpus/QUALITY.md:74–98`; `corpus/lessons/round-15.md` named R1/R2 corrections; `corpus/knowledge/ollama-evidence-replay.md:317–374`.
- Completed build64 then falsify32, **96 actual seats**, under separately validated v2/v1 policies. Build mix: executor17, scout20, reviewer9, critic6, connector4, scribe4, sentinel2, revenger2. Falsify mix: reviewer12, critic6, scout4, connector4, scribe2, sentinel2, revenger2. L1 held the canonical planner seat; PlannerWalk supplied a bounded revenger data-walk. Each admitted wave was one task call with the validated context/tasks, no model parameter. Evidence: `.ufo/waves/round-15/{build,falsify}/dispatch.json`, assignments, registries and completion summaries; falsify used `validation-final.json` after the host pacman pause, not its preliminary unspawned rendering.
- Two initial build attempts were completely refused with `Background job limit reached (100)` and spawned no seats; a direct retry admitted64. Four build scouts failed with provider402 credit errors and were not replaced: CaseAudit00,04,14,19. Build60 completed; falsify32 completed with no failures. Same-handle continuations are not additional seats. Evidence: build `spawn-result*.json`, `direct-spawn-result.json`, `provider-failures.json`, `completion-summary.json`; falsify spawn/completion records. Refused attempts are not counted as extra seats.
- Cross-domain boundary: dispatch-limit mechanics belong to kumitate; Main supplied the host-cap diagnosis/admission workaround, not an endpoint inference. Credentials remain kagi's, model evaluation kengaku's, and service/consumer actions operator-owned. No sibling implementation, routing, credential or service scope was absorbed. Evidence: `PROVINCE.md`; wave `SiblingBoundary.md`, `BoundaryOwners.md`; lesson §Executed author disposition.

Stale-lane: respawn-per-round; no other kama mission is open. Initial lane tree was clean; no inherited lane-authored work was swept. The outside round14 verifier file was read and preserved, not edited. No operator-teaching file was found by the recorded bounded glob. Tools installed/updated: **none**. The later host-wide pacman pause was relayed to live seats and embedded before falsify dispatch; no host transaction occurred.

Disclosed process deviations: one build seat's broad lane-local grep matched a historical `.ufo/interactive-sessions/` snippet, and another name search may have listed that directory. No further transcript open, host database/credential access or write was reported; snippet-derived material is excluded and Main was notified. A scribe evaluated the guard in-process and the harness owner used AST syntax parsing despite no-execution/no-verification instructions. Those are not the measured gate runs. L1 performed all recorded post-integration runner/classifier executions. Evidence: lesson §Advisory safety and §Final falsification dispositions; wave HostSafety/LedgerR1/GuardHarness reports.

## Landed changes

All groups are tied to `LOG.md` §round15 executable duplicate-corpus admission repair and §round15 committed red/green measurement and bounded verdict (`LOG.md:854–923`).

| Commit | Landed work / LOG binding |
|---|---|
| `70af36c2b15b46d3b4b3c15ef20459cff640dfaf` | Initial two-line guard, literal matrix/harness, build evidence, KQ18, source curation and named R1/R2 corrections; first round15 LOG entry |
| `4b1b4ad1ba31660cc44c82d204dc85c1355e36d2` | Final declared-name prose qualification, fork-exec audit observation, predicate-only causal control and complete falsify evidence; measured code revision named in second LOG entry |
| `b8bdc56efc43fe6baad9415d0ca75b7b81ffa952` | Actual command streams, acceptance/fidelity receipts, final source census and appended lesson/SCORECARD/LOG measurements; pushed before this report was written |

Existing classifier, original cases/receipt, serving tools, endpoint registry, province, promotion checklist and historical round14 lesson/verifier remain byte-equal to their starting blobs (`fidelity.json`). No domain tree or operator config was changed or pushed.

## Before → after measurements

Measured implementation: `4b1b4ad1ba31660cc44c82d204dc85c1355e36d2`; original source revision `e545ed99aaa519196a2a7779b0a293b2ce4c765c`, path `.ufo/waves/round-14/measure.py`, blob `783004569af9072afdeb32c6eeacc462868eb76b`, SHA256 `fda61e001ca8c2533c99a1759bb4b82f3260a72fafccf72f863f3f4e3684b60d`. Original and derived controls are distinct and both retained. All runs below actually executed after both waves returned.

Counting command from lane root:

```sh
python3 tests/ollama-corpus-guard/check.py --runner PATH
```

Before PATH `.ufo/waves/round-15/frozen/measure-before.py`; after PATH `.ufo/waves/round-14/measure.py` (also the default). The harness always supplies explicit temporary `--tool` and `--cases` flags, so the frozen copy's relocated defaults cannot fake rejection.

| Run / receipt | Real exit | Passed / failed | Observed interpretation |
|---|---:|---:|---|
| Original before, `run-before.json` | 1 | 23 / 27 | All27 duplicate controls actually measured instead of rejecting; positives work |
| Predicate-only red, same command with `--runner .ufo/waves/round-15/frozen/guard-only-red.py`, `run-causal_red.json` | 1 | 23 / 27 | Removing only the guard from final source reproduces the same defect |
| Final after, `python3 tests/ollama-corpus-guard/check.py`, `run-after.json` | 0 | 50 / 0 | All27 duplicate controls rejected, all23 valid controls measured |
| `python3 tests/ollama-corpus-guard/check.py --selftest`, `run-selftest.json` | 0 | 50 / 0 | clean; same literal oracle, not independent corroboration |
| Original-corpus retention, `python3 .ufo/waves/round-14/measure.py`, `run-retention.json` | 0 | 51 / 0 | Exact literal findings/exits/readiness/scope retained, unique names51 |

The fixed matrix is **50 tests = 27 negative + 23 positive**, across12 files with50 unique IDs. Every negative has at least16 distinct stripped nonblank names plus a duplicate; every positive is all-distinct. Literal data, totals and per-file digests are in `fidelity.json`; the command emits all IDs and nested case counts. This is one already-held passing classifier payload cloned under different case names, not50 new classifier semantics or885 new facts.

| Counter, summing the actual retained records | Before | After |
|---|---:|---:|
| Duplicate-control classifier entries / runner Popen calls | 483 / 483 | 0 / 0 |
| Valid-control classifier entries / runner Popen calls | 402 / 402 | 402 / 402 |
| Duplicate-control process-audit events | 966 | 0 |

After rejection has exact `corpus: duplicate case names`, runner exit1, tool present, all findings/exits null, passed false, exact corpus reasons, and no runner process events. Positive controls defeat reject-all. A positive child raises Popen and private fork-exec events, so804 positive audit events mean402 children, not804. Outer harness exit, corpus failure, unmeasured finding and event count are never conflated.

`acceptance.json`: **ok true, errors[]**. It records each reproducible command, full-receipt digest, fixed denominator, observed signature and extra per-record checks. `fidelity.json` records direct source correspondence, literal digest, final guard plus prose-only qualification, causal-only deletion, ten protected-file equalities, six prefix-preservation checks, allowed source cells and matrix digests against the named measured revision. L1 also compared current measured implementation/matrix bytes with that commit before sealing acceptance. These are finite offline inputs, not a mutable fleet-artifact verdict or live-runtime integration.

**Per-axis:** C1 calibration **improved**, numeric7→7; operability, freshness, depth, coverage and adjacency **unchanged**. No observed harm within the declared nonblank-name contract. Missing/blank/non-string names, raw fixture-key ambiguity, Unicode normalization, native/FFI or malicious-runner process containment are not certified. Author measurement verifies C1; independent non-author round15 admit/reject sampling still owns admission. No promotion is claimed.

## Sources & frontier

Both required validation runs used exactly:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

Before output, exit **0** (`sources-before-validate.json`):

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

After output, exit **0** (`sources-final-validate.json`):

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

Original output is TSV; displayed spacing above. W04 is existing scoped same-URL curation, not new independent support. Counting command for the row/tier/status table, actually run before and after, both exit0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama
```

| Census field | Before | After |
|---|---:|---:|
| rows | 33 | 34 |
| A / B / C | 30 / 0 / 3 | 31 / 0 / 3 |
| mined / queued / rejected | 23 / 5 / 5 | 24 / 5 / 5 |
| invalid tier/status; missing | 0 / 0; 0 | 0 / 0; 0 |

Full census streams: `.ufo/waves/round-15/sources-{before,final}-census.json`. Rows added by tier: **A1/B0/C0**. New **S034**, own-work/A/mined, cites the opened frozen original code at its pinned revision, not a new API discovery or repaired outcome. Lesson's appended Gate records source path, 2026-10-20 access date, `corpus_problems`:350–362 and line358 quote `if unique < MINIMUM_UNIQUE_CASES:` (4 words). C1 rests on that direct-code diagnosis and outside R1; the row itself earns no discovery/expansion credit.

Existing **S012.used-by**, old → new:
`corpus/knowledge/runtime-health-surface-matrix.md, corpus/knowledge/served-identity-crosswalk.md, corpus/knowledge/ollama-evidence-replay.md`
→ same three paths plus `corpus/lessons/round-15.md`. No existing status/recheck change; all other existing cells unchanged. S012 https://docs.ollama.com/api/ps was reopened this round, including a falsify re-open. Its OpenAPI3.1.0/info.version0.1.0 GET `/api/ps` 200 description says “Models currently loaded into memory” (5 words), not a readiness predicate or vendor duplicate-corpus policy. Its sampled source boundary is not a live `/api/ps` call.

Mistake mining: outside R1 minimum-cardinality versus injectivity becomes a fail-capable criterion KQ18; red controls expose the original actual implementation, not an absent tool. R2's partial-output/terminal-status distinction is appended with the outside ruling as authority. Exact old→new cells, source search/stop rationale, rejection decisions and scope qualifications are in `corpus/lessons/round-15.md` Gates/Mistakes. No frontier ground or new knowledge/capability row is advanced; existing integration/context-capacity gaps remain operator-dependent and were not sampled.

## Trend verdicts

- **expansion — unchanged.** No new knowledge entry, serving surface or capability row; S034 is source bookkeeping for a known outside diagnosis, not expansion. Evidence: SCORECARD §Round15; corpus README round15 supplement.
- **quality — unchanged.** The guard promise is repaired and marked, but gate machinery alone is not newly reverified/deepened serving knowledge. Original classifier/cases and admitted unique repertoire are preserved; no live knowledge recheck is inferred. Evidence: fidelity/retention receipts and replay entry's named correction.
- **discernment — unchanged.** KQ18 captures the outside ancillary-guard defect, whose discovery remains CloseKamaR14's. The author-dispatched waves are not a fresh independent round15 admit/reject sample. Evidence: lesson Gates and integration-review boundary; independent closure remains pending.

No new L0 question. Standing serving-runtime/cadence actions remain operator-owned and unassessed here; this offline repair needed no operator decision. Orchestrator action: independently sample one admit and one reject, reopen new S034/source boundary as appropriate, then decide admission; do not promote from author evidence.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources: `SKILL.md` domain sections and round15 gate registry; no new independent promotion verifier.
- [~] End-to-end domain task: historical `LOG.md` rounds1–3 remain the author assertion; this round's measured offline repair (`LOG.md:883–923`) is not a fresh serving-runtime task.
- [~] Executable instructions: `SKILL.md:478–505`, corpus replay correction and actual full-matrix/retention receipts; author demonstration only, not non-author promotion verification.
- [~] No cross-domain bleed: unchanged `PROVINCE.md`, protected-file comparisons in `fidelity.json`, and explicit kagi/kumitate/kengaku/operator boundaries above. No promotion box newly certified.
