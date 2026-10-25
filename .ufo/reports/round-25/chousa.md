# chousa — round 25 (same claimed round, attempt 2)

## Work performed

Declared claims: **C1 operability / metadata-screen capability**, **C2 freshness / index reconciliation**, and **C3 calibration / stale-restatement reconciliation**. Each has its own frozen population and before→after in `chousa-shokunin/corpus/evidence/round25-claims.md`. Operability is the lowest numerically scored non-retired axis (3/10); no new numeric scores are invented. Paths below are relative to `chousa-shokunin/` unless explicitly fleet-rooted.

- **C1:** added `verify-metadata`, naming the three legacy missing-recheck headers without pretending to enforce semantic QUALITY6. Final opened-fd/bounded-reader corrections, refusal controls, calendar-qualified recheck handling and structured-output token non-disclosure are documented in `tools/research-gate.sh:2288-2495`, `corpus/knowledge/metadata-screen-r25.md`, and `SKILL.md`'s final registry correction. The capability is in `SCORECARD.md`.
- **C2:** indexed the two missing base files and later outside spot-check; reconstructed Frontier rounds 11–23; placed the frozen 43 receipt rows under their owning rounds; reconciled eight historical capability rows without calling them new round-25 acquisitions. Evidence: `corpus/README.md`, `corpus/evidence/README.md`, `SCORECARD.md`, and `corpus/evidence/round25-landed-measure.log`.
- **C3:** replaced duplicate SKILL totals/open-finding restatements with their owner and recount command; appended ledger addenda; corrected the owning tuple's arithmetic; restored the historic GSHA line and resolved it append-only. Evidence: `corpus/knowledge/hardening-r10.md:677-715`, `corpus/evidence/round25-final-ledger.log`, and `round25-final-counter-controls.json`. The original raw-token-zero prediction is withdrawn: historical raw1/unresolved1 becomes raw1/unresolved0, never deletion of filed history.
- **Frontier and learning:** opened-source curation, superseding precision rows, prior outside-review intake and shown-to-fail criteria are in `corpus/SOURCES.md`, `corpus/QUALITY.md` (Round-25 additions), and `corpus/lessons/round-25.md`. S029/S033 support the new entry within scoped claims; medical/HTTP/ontology authority was not absorbed as a new province.
- **Recovery:** replacement writer `ChousaR25` inherited checkpoint `e93ac711`, both validated waves, their reports, and the uncommitted final gate/counter/source/ledger corrections. Reused after measurement: these corrections and retained evidence. Discarded as final proof: checkpoint154 tallies, the in-place GSHA fill, superseded source teachings, and working-tree-only packaging claims. Historical reports remain intact. Attempt1's absence of output is distinct from this same-attempt replacement. Evidence: lesson replacement reconciliation and prior coordinator's retained wave registries.

### Waves, routing and failures

Both inherited waves were validated under policy v2 and dispatched as one unchanged batch each; their complete task payloads contain the verbatim Godspeed directive. No wave was replayed. The canonical planner seat was held by the L1, not inserted as the validator-forbidden `planner` role. Current session role routing was used without model parameters or configuration changes; old model tables in the rendered prompt are not current availability evidence.

| Wave / batch | Seats | Role mix | Observed outcome |
|---|---:|---|---|
| build | 68 | executor5, scout23, critic4, sentinel1, reviewer12, scribe12, connector4, revenger6, simplifier1 | 68 reports; no dead seats |
| falsify | 68 | reviewer49, revenger8, critic3, scout1, mutation-tester2, connector3, sentinel1, scribe1 | 52 reports; 16 dead seats |
| bounded post-recovery residual batch | 3 | reviewer3 | 3 reports; no dead seats; final corrections reviewed, not replacements |
| **Round total** | **139** | two valid-band waves plus the bounded residual review | **0 replacements** |

Wave evidence: `.ufo/waves/round-25/{build-spec.json,build-dispatch.json,falsify-spec.json,falsify-run.json}`, both `swarm-registry.json` files, and `corpus/evidence/round25-final-pin.json`. Role counts were executed with:

```sh
python3 -c 'import json,collections,pathlib; p=pathlib.Path("/home/vgpnk/Projects/shokunin/chousa-shokunin/.ufo/waves/round-25"); [(lambda d,w:print(w,len(d["members"]),dict(collections.Counter(x["role"] for x in d["members"].values()))))(json.loads((p/w/"swarm-registry.json").read_text()),w) for w in ("build","falsify")]'
```

Two pre-build whole-batch refusals were `Background job limit reached (100)`; neither spawned seats. The later unchanged batch spawned all68 (`build-dispatch-attempts.json`). No refused wave was split.

Dead seats, all retained in `falsify-dead-seats.json`: **FxCapR17, FxCapR18, FxCapR21, FxCapR23, FxConnectSeparability, FxFrontierR12R13, FxFrontierR14R15, FxFrontierR16R17, FxMetaDirectory, FxMetaRecheck, FxMetaRoot, FxMetaSchedule, FxRegistryAppend, FxSkillCurrent, FxSrcFAIR, FxSrcProvO**. FxMetaDirectory's final error was `[zai/glm-5.3-flash] Retry budget exhausted after 5 retries: 429 Rate limit reached for requests (type=1302)`. The other15 ended with `[openai-codex/gpt-6-luna] Retry budget exhausted after 5 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`. No failover-cause or answering-model quality claim is inferred.

The three residual reports are `.ufo/waves/round-25/residual-final-{meta,measures,sources}.md`. Metadata review found no blocker in its bounded correction scope; source review reopened S029/S033 and rejection S025, and its study-path finding was fixed with an appended resolution. Counter review prompted further anti-deletion guards and the README snapshot qualification. These are author-lane advice, not independent outside closure.

Stale-lane: this replacement owns only the existing round25 claim; no other mission of this lane is open and no round26 was started. Misroot sweep before reporting used `git -C /home/vgpnk/Projects/shokunin status --porcelain`: only a foreign round21 CLI-catalog note remained; it was left untouched and routed to KaidokuR21-2. The earlier three chousa misroots/copy observations remain documented in lesson R25-M12, not re-certified against deleted originals. Tool installs/updates: none reported by the retained seats or residual reviewers; none performed by this replacement.

## Landed changes

Final pushed lane tip: **`ba3333254dd337658a4f25e7a9471f9cf4e4567e`**. Measured production revision: **`c125d8bc20e5433947df26fe0af3d3b58d0b37d3`**. Later commits add only measurement identity, receipt indexing and comparable baseline evidence; the gate is unchanged.

| Change | LOG entry / evidence | Helper-landed commit |
|---|---|---|
| Final source, index, ledger, QUALITY and counter corrections; wave reports/registries; current capability documentation | `LOG.md:898-938`; lesson R25-M14; final pin and counter controls | `c2a6e338bb29cf183c32e8f2263a98aae5bdcd1d` (not final gate proof) |
| Actual final161-case metadata reader | `LOG.md:940-955`; lesson R25-M15; exact measured gate SHA985a6320 | `c125d8bc20e5433947df26fe0af3d3b58d0b37d3` |
| Explicit measured-commit SCORECARD entry, packaging erratum, receipt index and eleven-input binding artifact | `LOG.md:940-955`; `corpus/evidence/round25-measured-revision.json` | `516170a03faa325aa8464ba3375271799bd229a3` |
| Final counting probe re-run on the base archive, preserving comparable before values | `LOG.md:957-961`; `corpus/evidence/round25-final-before.log` | `ba3333254dd337658a4f25e7a9471f9cf4e4567e` |

Packaging honesty: the first replacement helper call explicitly named the gate but still retained stale63a39282 in c2a6e338. The required SHA comparison caught it. The orchestrator approved one gate-only helper retry, which landed c125d8bc; all11 measured input blobs then matched. Cause remains unresolved and was reported to Main/tool QA. This differs from the earlier L1 omitted-path incident; neither is hidden by helper success. No direct Git/JJ mutation or fleet-helper edit was used.

Final lane helper state: `local=ba3333254dd337658a4f25e7a9471f9cf4e4567e remote=ba3333254dd337658a4f25e7a9471f9cf4e4567e ahead=0 behind=0 head=detached tracked=0 untracked=0`. The integrator-owned `corpus/lessons/round-24-verifier-spotcheck.md` was read and indexed, never edited.

## Before → after measurements

The **same final counting probe** was executed against base **`d730ae4c33989ad9c8535764d4cae77b4db869f6`** (isolated `git archive`) and the final delivered production bytes bound to **`c125d8bc20e5433947df26fe0af3d3b58d0b37d3`**:

```sh
bash /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/evidence/round25-measure.sh TREE_ROOT
```

`TREE_ROOT` is the base archive or the lane tree. Receipts: `corpus/evidence/round25-final-before.log` and `round25-landed-measure.log`; both counting-probe executions exit0. **Exit0 means measurement completion, not admission**: the printed values, explicit controls and retained content review are the evidence.

| Claim / axis | Before | After | Verdict / score delta |
|---|---|---|---|
| C1 operability, new metadata-screen capability | mode absent, rc2, no named legacy-header findings | mode rc1; `METADATA_COMPLETE=25/28`; exactly archives-verified-r9.md, audit-r11.md and gate-baseline-r8.md each `META_RECHECK_ABSENT`; 33 findings =3 warn+30 info | **improved**, qualified syntactic screen; numeric operability3→3/delta0 on its original r1 construct; capability demonstrated and entered |
| C2 freshness | `STALE_INDEX_ITEMS=66` =2 unindexed+13 Frontier gaps+43 misfiled receipt rows+8 missing capability rows | each component0, total0 | **improved**, bounded index freshness; no numeric freshness score invented |
| C3 calibration | `STALE_RESTATEMENTS=15` =1 open finding+3 tuples+2 queues+1 unresolved slot+8 missing addenda | each component0, total0; historical raw slot remains1 | **improved**, qualified lexical/content-review result; no numeric calibration score invented |

Additional exercised checks:

- `bash tools/research-gate.sh --selftest`: **136→161 cases, 0 skipped**; legacy cases1–136 compare identically. Full retained final stdout is `round25-retained-final-selftest.log`; current owner runs are recorded in the measure/hold receipts.
- `bash corpus/evidence/round25-meta-differential.sh` from the lane root: **AGREE=54/54**, exact27 unique fixture files × normal/strict modes, exit0 (`round25-landed-differential.log`). This is not coverage of every new fd/race branch.
- `bash corpus/evidence/round25-holds/battery.sh /home/vgpnk/Projects/shokunin/chousa-shokunin /home/vgpnk/Projects/shokunin`: **12 MATCH results**, exit0 (`round25-final-holds.log`). Broken controls retain expected exit1; MATCH is not universal CLEAN.
- `bash tools/research-gate.sh --drift corpus/evidence/gate-baseline-r12-20261019T115519Z.json`: **GATE_DRIFT: none**, exit0; r1 counting probe **VERDICT_BEARING_EXPORTS=3/3**. No baseline re-pin.
- `python3 corpus/evidence/round25-ledger-recount.py`: **rows71, by-design38/carried22/closed8/finding0/operator3, sum71; queue_committed24 versus queue_true25** (`round25-final-ledger.log`).
- Seven isolated counter/population controls preserve exact executed programs and outputs in `round25-final-counter-controls.json`: C3 clean0, slot deletion1, marker relocation1, empty addendum1, recount deletion1; fixture parser clean0/table-row deletion1. These demonstrate failure sensitivity, not full semantic validity of every index cell.
- `round25-measured-revision.json` records **11/11 SHA matches** between persisted measurement inputs and `git show c125d8bc:<path>` bytes, including final gate SHA256 `985a63200ca4c5712806d8752ba27a8f3448b026f773659079e71ca602e56ef7`.

Limits remain explicit: C2 row/heading/capability counts need manual evidence review; C3 3b's removal-to-owner-pointer design and addendum lexical checks are not semantic proof. Metadata source presence and verified-at date shape do not establish support/truth or full QUALITY6. Calendar-invalid rechecks are info in default mode; strict mode drifts. Same-inode writes/pre-open races, Linux/GNU dependencies, and raw setup/open path diagnostics remain named limits. Concurrent JSON appenders, other parent-root rechecks, historical receipt gaps and source/span pairing remain unclaimed debt. Depth, coverage-as-a-measured-axis and adjacency are **unchanged**; no observed harm is claimed away.

## Sources & frontier

Contract CLI, run at original round start and final landing:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Original start (authentic tool result recovered from the same-attempt coordinator; `round25-driver-census-start.json`, toolCall `toolu_01B8Zoeb91xYXBurCooBcvhq`):

```text
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
exit=0
```

Final (`round25-driver-census-end.log`):

```text
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
EXIT_CODE=0
```

Row census command: `bash corpus/evidence/round25-sources-census.sh` (frozen-contract predicates). Retained before `round25-census-before.log` → final `round25-final-census.log`:

```text
rows:       18 -> 33
malformed:   0 -> 0
tiers:       A14 B1 C3 -> A27 B1 C5
status:      mined8 queued7 rejected3 -> mined10 queued19 rejected4
duplicates:  [] -> []
enum:        [] -> []
missing-used-by: [] -> []
```

Added15 rows by tier: **A13/B0/C2**, including five superseding precision rows rather than five newly searched sources. Original S001–S018 immutable cells and mutable cells are unchanged. S019/S020 changed **mined→queued** and **used-by `corpus/knowledge/metadata-screen-r25.md`→—**; both transitions are logged in the lesson. Recheck cells unchanged. New mined S029/S033 now name the entry in used-by. S025 is retained rejected with its HTTP-versus-research-validity reason and flip. Garner/BMJ blocked403 remained a lead/exclusion, never an invented opened row or quote.

Frontier advanced: a sourced metadata-screen entry/capability on previously uncovered metadata-screen ground, and the study path S029→S032→S033→S023. Periodic assessment, update signals, entity time and verification policy are distinguished; scheduling/recording is labelled lane inference. Lesson `## Gate` supplies access dates, URLs and located ≤25-word quotes. R25-M2/M3 and QUALITY13/14 learn from the prior outside check; arithmetic, independent controls, packaging and deletion-sensitive counters are mined in M7/M11/M13–M15. Source-row growth alone is not the expansion verdict.

Public documentation reading only; no live-target probing, credentials, host mutation or domain-source-tree writes. Outside round25 admit/reject verification is **pending the orchestrator's independent closure**, not replaced by lane-dispatched reviewers.

## Trend verdicts

| Trend | Verdict | Evidence / qualification |
|---|---|---|
| expansion | **improved** | New admitted metadata-screen ground is indexed, cites mined S029/S033 and has a demonstrated capability row; not inferred from15 extra source rows or zero stale-index count alone |
| quality | **improved** (qualified) | Stale index/ledger claims corrected, owning arithmetic reconciled, source overstatements superseded, legacy header debt made visible, final reader and legacy holds exercised; syntactic screen is not semantic verification |
| discernment | **improved** (prior-review learning) | Prior outside-review debts become lesson-backed shown-to-fail QUALITY13/14; S006 quote and new source imprecision are corrected; final false-zero risks are exposed and bounded. This does not claim an independent round25 spot-check has already occurred |

Claim admission remains for the independent non-author closure: this report's measured improvement recommendations are not self-awarded admission. Open L0: the historical **chousa | round-12 | Receipt identity** acceptance-model question remains unanswered in the standing queue; no new blocking question was needed. Remote availability is demonstrated by helper-verified pushes, not left as the round1 remote question. The helper-omission cause is routed to Main and QA, not silently attributed to a model/provider.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — `SKILL.md` and `corpus/knowledge/metadata-screen-r25.md`; lane assertion, no round25 non-author verifier.
- [~] End-to-end domain task executed/logged — `LOG.md` round9 archive verification, `corpus/fixtures/archives-r9/`, and the round25 explicit-root hold battery; lane assertion.
- [~] Instructions executable without oral context — final161-case selftest, metadata differential54/54 and `corpus/evidence/round25-landed-measure.log`; documented cwd/root requirements and limits retained; lane assertion.
- [~] No cross-domain bleed / accurate province — `PROVINCE.md`, metadata entry limits and scoped-source corrections; lane assertion, no promotion or self-attested `[x]`.
