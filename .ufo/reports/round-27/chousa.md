# chousa round 27 — recovery, bounded repairs, C3 partially falsified

## Work performed

Declared, causally distinct claims (frozen at `corpus/evidence/round27-claims.md`, base `64eec5d41c7cf7f17f5ce1e968e28b3769952596`): **C1 operability** (lowest measured axis: repair the three failing usage selftests without weakening them); **C2 freshness** (ASCII dates and nonrecursive leading-zero cadence normalization); **C3 calibration** (registry-header state, S-id occurrence identity and complete-filesystem-path checks).

**Final disposition: NOT ADMITTED.** C1 and C2 improve bounded behavior. C3 remains **partially falsified / harmed**: the complete-path repair closes the earlier-colon hidden-denylist defect, but citation-prefix refusal is retained and extended to a new claims-canonical path. Green suites do not establish the entire frozen claim or no-harm. No r28 was started.

- Recovered the same held r27/attempt1 after the host session died. Re-verified inherited lane checkpoint `dd72641e574679c4f7882dd43de072b4c8892d6f`, its executable digest and archived receipts; reconciled every build/falsify seat with durable transcripts and report hashes (`.ufo/waves/round-27/inherited-final-reconciliation.json`).
- Retained the inherited C1–C3 repairs, S040–S042 and 58 synthetic controls. Original187 selftest identities were not deleted or weakened; first210 identities remain unchanged from the inherited checkpoint, including the original187 (`final/identity.json`).
- Triaged 63 inherited falsifier reports. Corrected escaped-pipe width/index consistency, per-token cost, quadratic trailing-CR stripping and usage-matcher fail-open; residual review then exposed a second source-scanner fault path, now fail-closed (`corpus/lessons/round-27.md`, R27-M10–M16; S043).
- Added five selftest cases (211–215) and a final32-control suite. Kept the original `round27-regressions.py` unchanged. Failure injection distinguishes tokenizer/filter faults from genuine no-match; exactly one `META_SOURCE_SCAN_FAILED` crit is emitted (`corpus/evidence/round27-falsify-controls.py`).
- Preserved the frozen negative prefix-refusal controls rather than changing expectations to erase C3's contradiction. `residual/ResC3Clause.md` demonstrates the unfixed new over-refusal `plain.md -> k.env:1`; L0 policy adjudication is requested.
- Updated QUALITY19–22, SKILL status and corpus frontier disposition, SCORECARD and LOG. No new knowledge/capability admission, full-GFM guarantee, source-truth certification or promotion is claimed. Domain sources, sibling repos, fleet scripts/MANIFEST/state/routing were not modified.

Unless otherwise qualified, wave paths below are relative to `chousa-shokunin/.ufo/waves/round-27/`.

## Landed changes

All work is tied to `LOG.md` **Round27 — rejected-contract repairs and post-crash recovery** and the detailed round27 lesson.

| helper-landed commit | changes / LOG linkage |
|---|---|
| `dd72641e574679c4f7882dd43de072b4c8892d6f` | Inherited integrated C1–C3 repairs, original58 controls, S040–S042, QUALITY19/20, build64 receipts; LOG “Landed production and evidence”, first bullet. |
| `cb895a2bdd259eb38bec29ef70011d8211a508b5` | Post-falsify width/cost/CR/matcher repairs, five appended selftests, initial26 additional controls, S043 and falsify-wave evidence; LOG second bullet. This checkpoint was subsequently falsified and is not silently called final. |
| `4f48419425f5165a8f950e1db4c0a781cf845d40` | Final production: one shared escaped-cell split; separately checked ASCII scanner stages; final32 controls; residual reports, oracle bundle, source census, lesson and documentation; LOG third bullet. |
| `457fbb04fa872c88ce5c5da9a48d3a767eaf51ff` | Final immutable measurement receipts, SCORECARD verdict, LOG and skill/lesson closure; LOG fourth bullet. **Final lane tip**, clean and pushed: ahead0/behind0, tracked0/untracked0. |

Measured production revision is **4f484194**, not an uncommitted working tree. Gate SHA-256: `ac1315ddaa12e79b68069d1a9866b9b1b55e3a43efef3ba0cb5ca5e665835765`. `final/identity.json` binds the revision, argv, cwd, environment, exits and digests. Historical `corpus/evidence/round27-*-after.*` remain unchanged dd72641e receipts (PASS210); `post-falsify/` records cb895a2 (PASS215); **`final/` supersedes both for final behavior**.

## Before → after measurements

Before behavior is the accepted committed r26 falsification, **not a rerun to confirm reported failures**. The non-executing source-mechanism probe is a separate lexical count, not a semantic verdict. Commands below ran in an isolated archive of **4f484194**; the final full battery ran once after all eight residual seats finished.

| claim | before → measured after | counting command and evidence | verdict |
|---|---|---|---|
| C1 operability | accepted r26 **FAIL3/187 → PASS215/215**, zero skips; original C1 controls6/6 and final additional5/5; original r1 scalar3→3, delta0 | `bash tools/research-gate.sh --selftest`; original and added control commands below; `final/selftest.log`, `final/identity.json`; r26 `FNoTrade.md:115–137` | **improved, bounded** |
| C2 freshness | accepted r26 locale and long-zero failures → original21/21 + final additional8/8 match, date differential9024/9024 | `python3 corpus/evidence/round27-regressions.py --gate tools/research-gate.sh`; `python3 corpus/evidence/round27-falsify-controls.py --gate tools/research-gate.sh`; `bash corpus/evidence/round26-date-differential.sh TREE/tools/research-gate.sh`; final logs/JSON | **improved, bounded** |
| C3 calibration | accepted r26 header/rescan/colon-hidden-denylist defects → original31/31 + final additional19/19 match, registry48/48; **negative no-prefix clause still fails** and a claims-canonical over-refusal is new | same two Python commands; `bash corpus/evidence/round26-registry-differential.sh TREE`; `residual/ResC3Clause.md:47–119`, final logs | **partially falsified / harmed**, not verified |

`TREE` denotes the isolated full archive, not the live lane; exact absolute argv are in `final/identity.json`. Final commands/results, all exit0:

- Original regression suite: **58 controls,0 mismatches**; final additional suite: **32 controls,0 mismatches** (`final/regressions.json`, `final/falsify-controls.json`). These populations do not cover every frozen C3 requirement.
- `python3 corpus/evidence/round27-mechanisms.py tools/research-gate.sh`: lexical C1/C2/C3 **1/2/5 → 0/0/0** (`corpus/evidence/round27-mechanisms-before.json`, `final/mechanisms.log`). This can be fooled by source spelling and never establishes admission.
- Selftest environment: `LANG=en_US.UTF-8`, `LC_ALL` unset. First210 name/number identities equal dd72641e; first161 ok-line SHA remains `5eac4a7e2af964f6e81631f66990426e5c8ef58fb41ba6ec6d0054ef819e01cb`. Under exported `LC_ALL=C`, ten inherited claims/verify-all cases fail on both intermediate checkpoints; this is disclosed locale sensitivity, not a final no-harm claim.
- Date9024/9024; registry48/48; `bash corpus/evidence/round25-meta-differential.sh`:54/54,27 fixtures; `bash tools/research-gate.sh --drift corpus/evidence/gate-baseline-r12-20261019T115519Z.json`: `GATE_DRIFT: none`. Logs under `final/`.
- Original A/B/C archive calls with explicit fleet `--root`: each exit1 and exactly one DRIFT summary, **VERDICT_BEARING_EXPORTS=3/3**; per-input argv/outcomes in identity.json. The scalar is not a resource or field-readiness score.

Independent residual checks are author-lane advice, not outside admission: ResReceipts reproduces every cb895a2 receipt; ResUsageMatcher kills three fail-open mutants; ResCrStrip records52 byte-identical fixtures and38,725 expression-fuzz lines; ResWidthFix checks2256 header rows and51 fixtures against two GFM oracles, exposing shifted columns before validating the shared-split candidate. `residual/scanner-followup.json` binds the **exact final gate digest**:1005 equivalent source values, tokenizer/filter/missing-grep faults produce one crit,32 controls and215 selftests pass.

**Limits and trades:** three initial post-falsify controls fail deterministically at dd72641e; a fourth is a60-second timeout, not an incorrect date (67.38 seconds completes correctly). Timing ratios are load-dependent. A final dense2 MiB scan takes224.75 ms versus faulty cb895a2's209.25 ms (+7.4% due to captured tokens) and dd72641e's16253.01 ms. The L1's base dense-input300-second timeout and ResReceipts'64-second completion both remain recorded; no universal timing/RSS guarantee is inferred. Full GFM, one-dash delimiters, Markdown raw/rendered cell equivalence, races and source truth remain unverified. Original frozen-prefix controls stay intact; C3/no-harm rejection is not traded away.

## Sources & frontier

Census command, before and after:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Both outputs: `chousa\tok\t/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md` (actual tabs), **exit0 → exit0**. Durable counts and source digests: `corpus/evidence/round27-census-before.json` and `round27-census-after.json`; reproduced by ResReceipts and final census.

- Rows **39→43**; tierA **33→37**, B1→1, C5→5; mined16→20, queued19→19, rejected4→4. Row counter: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; frozen tier/status histograms are CORPUS.md §Census.
- Added **S040–S043**, all own-work tierA/mined, opened locally2026-10-21: usage-record diagnosis, date normalization diagnosis, registry diagnosis, in-round falsifier counterexamples. Each is cited by `corpus/lessons/round-27.md`; both `## Gate` sections carry located short quotes and the access date.
- Existing status/recheck/used-by mutations: **none**. No old row is silently reclassified. The r26 candidate notes stay qualified/withdrawn.
- Frontier advanced in investigation only: parser-representation, matcher-failure and cost evidence; **zero new admitted knowledge entries/capabilities/core areas**. Source-row growth is not expansion. QUALITY19–22 cite the mistakes and failing controls; R27-M17 records the residual item's out-of-contract instrumented base run, which is excluded from before evidence.
- No external live-target research, host-secret/live-process probe or domain-source write. Official PyPI package installation for the local oracle is the only new package-fetch activity.

## Trend verdicts

- **expansion: unchanged** — four scoped source rows and stronger local controls, but no newly admitted knowledge/capability or frontier-to-core move (`corpus/README.md`, Round27 disposition).
- **quality: harmed** — C1/C2 repairs and full PASS coexist with C3's unresolved new canonical-path over-refusal; admission requires no axis harmed. The trade is disclosed, not netted against green counts (`residual/ResC3Clause.md`, SCORECARD Round27).
- **discernment: unchanged** — mistakes are mined into QUALITY19–22 and frozen C3 is honestly rejected; no fresh outside admit/reject spot-check is self-awarded. Lane-dispatched reviewers remain the lane.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources: SKILL decision table/Gates and round27 correction, QUALITY19–22, S040–S043; author assertion, no non-author promotion verifier.
- [~] End-to-end task executed/logged: historical round9 archive task and r25 explicit-root battery (`SHONEN.md` box2); no new end-to-end domain-success claim.
- [~] Executable instructions: final immutable selftest215 and controls58+32 pass, but C3 remains partially falsified and locale limits are explicit (`final/identity.json`, SKILL). Not promotion evidence from an outside verifier.
- [~] No cross-domain bleed: PROVINCE unchanged; all work is the lane's own research gate/corpus. Model-evaluation, bounty, orchestration lifecycle and credential custody remain sibling provinces; no upstream write or live-target action.

## Waves, recovery, scope and open L0

- **Inherited build64:** scout20, reviewer18, critic8, scribe8, connector4, executor3, revenger2, sentinel1. **Inherited falsify64:** reviewer27, scout17, critic11, mutation-tester4, sentinel1, revenger1, connector1, scribe1, simplifier1. Specs/dispatches/assignment receipts/registries retained; planner is the L1-held canonical seat. Falsify had ten cap refusals, then spawned64 on attempt11.
- **New residual8 (not a padded wave):** reviewer5, critic3; fifteen cap refusals, spawned8 on attempt16. Fewer than64 distinct new attack items existed after integration, so the prompt's ≤8 residual exception was used. Total **136 seats**, within200; no fresh64-seat post-crash wave or dead-seat replacement. Eight residual reports all returned; captured routing was used without model parameters.
- **Dead no-report seats7:** `ChousaR27.ReviewDateUnknown`, `.ReviewRegistryBreak`, `.ReviewPathSynthetic`, `.ScribeQuality`, `.ScribeScorecard`, `.ConnectSibling`; `ChousaR27.IntegSourceGate-11`. Full assigned IDs, report hashes, terminal errors and malformed/truncated transcript counts are in `inherited-final-reconciliation.json`. Three reviewers died with Devin `resource_exhausted: Reached free model rate limit`; two scribes with `Retry budget exhausted after 5 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`; connector and final scribe ended `Request was aborted`. No identity was revived or reissued by this replacement.
- Original L1's earlier Devin weekly-quota death/revival and the parent-caused ~six-minute R2 overlap are separate from the final SIGHUP host crash. R2 stood down without chousa commits; its union merge and byte-exact ReviewDateCalendar misroot move were inherited and re-verified. The73 later R2 seat transcripts actually carry Kotodama r50 goals and are not charged to chousa.
- Inherited/re-verified: dd72641e gate and receipts,121 report files (58+63), uncommitted falsify metadata. Preserved corrections are named above. Nested executor clone sandboxes were manifested, moved out of the lane and then removed; no inherited evidence report was discarded. Fleet misroot sweep found no new chousa misroot; other lanes' state/report/watchdog changes were untouched.
- **Installs:** ResWidthFix used official PyPI/uv `uv run --with` for cmarkgfm2025.10.22 and markdown-it-py4.2.0 (cffi2.1.1, pycparser3.11, mdurl0.1.2), plus uv-managed CPython3.15.0, for independent local GFM oracles. No pacman transaction; no other new install. Bounded oracle corpus/scripts/results retained at `residual/width-oracle-bundle/`.
- **Cleanup:** completed round-owned `/tmp/chousa-r27-*` and `/fast/scratch/hyaku/chousa-r27` removed (~1.5 GiB); bounded oracle bundle copied/manifest-cmp-verified before duplicate cache removal. Old sandbox paths in reports are historical, not promised live artifacts.
- **Open L0:** adjudicate complete-filesystem-path semantics versus retained prefix-refusal expectations before a later policy change. The chousa line in `.ufo/l0-questions.md` was concurrently swept into fleet `72a724b5db6b4a261c0999b64a7fc1ee6d4326a3` by kama-shokunin; attribution is disclosed, not rewritten. Historical round12 receipt/race debts remain carried. This round does not alter claim/outcome/next/blocked state.
- **Stale-lane:** same held r27 claim progressed through pushed lane commits despite provider/host/cap delays; no other chousa mission or r28 was opened. Report closes this replacement's assignment, not the operator's admission/advance decision.
