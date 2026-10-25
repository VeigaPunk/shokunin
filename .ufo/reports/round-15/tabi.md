# tabi — round 15 (hyaku, attempt 1)

## Work performed

Declared **C1 operability**: one verified USER counter reason/applicability contract **0→1**, working a lowest non-retired tie (operability8). Declared **C2 calibration**: one enforced historical cleanup/qualification-mirror and canonical snapshot-classification contract **0→1**. Claims are causally separable; no exploratory claim, scalar increase, new browser execution, knowledge ground or capability.

**Pushed lane HEAD:** `36240c70ee114347a79abb91cacab6c63044ce36`. `git push` observed `7054a5e..36240c7 master -> master`; following `git status --porcelain` was empty. Lane author identity is `tabi-shokunin <tabi@shokunin.local>`. This report is written after that push.

- C1 gives six closed refusal reasons, exact child-record parsing, explicit applicable/absent versus N/A marker fields, reason-only decoys and a real baseline/repaired/masking-mutant witness. USER selftest passed42 aggregate records:32 fixtures+alias+six committed counts+count witness+diagnostic witness+reason control. Evidence: `scripts/check-user-round-contract.mjs`; `corpus/evidence/round-15/user-diagnostics.json`, `user-diagnostic-witness.json`; LOG.md round15.
- C2 validates all six cleanup and eight qualification fields against raw proofs; independent literal aggregate controls cover mixed/two-worker, incomplete and closed-versus-refused data. Canonical source digest drift exits2 `snapshot_tampered` before semantic comparison. Metadata selftest passed36 CLI cases+4 helpers. Evidence: `scripts/check-aria-metadata.mjs`; `corpus/evidence/round-15/metadata/{expected-fixtures.json,mirror-contract.json}` and `metadata-selftest.json`.
- Actual old/new checker execution accepted nine single-field false mirror variants before and refused them after, with exact field-finding sets. Same spec alteration changed old semantic failure1 to `snapshot_tampered`/could_not_evaluate2. Both untampered controls accept; all originals remain unchanged. Evidence: `.ufo/waves/round-15/metadata-witness.py`; `corpus/evidence/round-15/metadata-differential.json` and its raw command receipt. This is stronger than `--witness-mirrors`, whose legacy arm is explicitly static, not executed.
- Original receipt check remains exit1 with only `R14-ARIA-CLEANUP-LISTENING-AFTER-01`; corrected check and metadata witness exit0. Final committed-docs production is ROUND clean10/exit0 and USER honest round_count6/10/exit1. Evidence: `metadata-original.json`, `metadata-corrected.json`, `metadata-witness.json`, `final-production.json` under the round15 evidence directory. USER production stops before per-round counting; it is not full green.
- Reopened S029 and added direct machine-evidence provenance, a first-added Gate/Mistakes lesson, QUALITY20/21 and named SKILL/README qualifications. Evidence: `corpus/evidence/round-15/source-index.json`, `corpus/lessons/round-15.md`, `corpus/QUALITY.md:65-77`, SKILL.md round15.
- Source audit corrected an overbroad prior outside-review inference: frozen `aria-loopback.spec.mjs:269` asserts Node minimum, invoked per case at:924. Only the launcher's **runtime.pinned summary** and spec's `runtimePinStatus()` omit Node; the launcher records runtime.node. These are two enforcement layers over one recorded observation, not independent runtime signals or exact Node equality. Prior outside/runtime bytes stay unchanged. Main acknowledged the non-author erratum action; evidence: source-index, w1/SkillCorrection.md and w2/AttackNodeErratum.md.
- Wave1 validated/dispatched64 seats in one unchanged taskCall: executor3/revenger5/scout11/reviewer18/critic9/sentinel4/scribe8/connector6. Completed48, provider-failed16; initial17 estimate corrected because SourceLocators completed. Wave2 validated/dispatched32 distinct delivered-byte attacks: critic7/reviewer12/sentinel3/revenger2/scout4/scribe2/connector2; all32 completed. **Round total96**,80 completed/16 failed, no replacement identities or per-task model parameters. L1 held canonical planner; LowestAxis carried bounded planning reconnaissance but failed after sending anchors. Evidence: `.ufo/waves/round-15/{w1,w2}/{spec.json,validation.json,swarm-registry.json,dispatch-result.json}`, `policy-provenance.json`, `build-snapshot.json` and `verified-code-snapshot.json`. Host routing changed during the round; static route names are not claimed as authentication/routing certification.
- Wave2 caught the self-matching mask needle, non-causal wrong-reason decoys, misleading isolation labels and consumer/schema mismatches; all scoped repairs preceded final verification. Attacks bind build72dcf03, not repaired bytes. The final command receipts bind repaired code27dfd98. C2's first counter run genuinely failed0/exit1 and remains recorded; only that consumer was repaired/re-executed, without rerunning passing gates or altering expected truths. Evidence: w2/AttackWrongReason.md, w2/AttackMeasureC2.md, `count-after-c2.json`, `count-after-c2-repaired.json`.

**Stale-lane:** sole tabi mission, no other tabi mission open. Both waves completed before the operator wrap-up; no planned wave was skipped and no new worker or later round started afterwards. Already-active consumer repair finished, then landing proceeded. Misroot sweep returned no files at fleet `.ufo/waves/round-15/w1/*` or `w2/*`; `wrapup-misroot.json` records exact patterns/output. CountProduction's9652-byte misplaced fleet report was copied byte-exact into the lane (SHA256 `e3f8959d1afbc382122dd9ded982c7208f8e079bd2f79ad4eb077a850b58b470`); Main owned fleet-original removal. SourceCuration recorded its separate misplaced-write/move incident. **Tools installed/updated: none.** Later host-wide pacman pause was relayed and included in wave2 context.

## Landed changes

All changes are motivated/recorded in **LOG.md:828-961** (round15, with appended corrections; subsequent final lines complete the measurements). No inherited uncommitted lane work existed. Non-author `round-14-verifier-spotcheck.md` and all round13/14 evidence/lessons were intentionally unchanged.

| Commit | Landed work / LOG linkage |
|---|---|
| `c138bea` | USER diagnostic implementation and round15 declaration/motivation; LOG round15 trigger/claims |
| `72dcf03` | First metadata contract, retained64-seat build wave and revision probe; LOG build snapshot (not claimed passing) |
| `27dfd98bd6bbd85fe77fb028d531691ce066031a` | Falsifier-driven gate/oracle repairs and complete32-seat attack evidence; LOG wave2 corrections; this is the exercised gate-code revision |
| `b7cf0446a31014a81b4882857c90c565ebc14210` | Actual executions, immutable first-added lesson, sources/QUALITY/SKILL/index/README and direct S029 provenance; LOG exercised outcomes |
| `9fd8bca99d60cc1612faeeac633e1436d231bde3` | Consumer-only ARIA token/status repair plus honest failed counter/final production receipts; LOG actual failure and repair |
| `36240c70ee114347a79abb91cacab6c63044ce36` | Final C2 counter success, measurement dossier, SCORECARD and LOG verdicts; pushed final lane HEAD |

Boundaries are explicit, not silently certified: arbitrary noncanonical receipt/pin paths are semantic fixture inputs, not authenticated historical snapshots; unchecked known/advisory labels and complete sidecar-byte authentication are outside C2. Worker-directory set drift, digest-then-reread races and arbitrary --check refusal classes remain uncredited. The generated Node note now differs, so source review reports that --derive refuses overwriting the old sidecar rather than promising its prior idempotent output; no new derive invocation was executed this round. Original correction acceptance is exercised and unchanged. Shared writer/checker derivation is not itself an independent oracle; literal controls and pinned historical bytes provide the separate expectations.

Broader inherited USER survivor replay/r07, user-record freezing, IPv6 origin, Git environment/hooks/config/PATH and external-validator pin debt remains open. Commands were exercised under a recorded minimal environment with system/global Git config disabled; no hostile-environment safety is claimed. Publishing remains kake-owned, credentials kagi-owned and forensic RE revenger/kaidoku-owned; no cross-domain action occurred.

## Before → after measurements

Measured input baseline: `7054a5e1068538349b4dbb0d291c2fe8643802f2`; after: `b7cf0446a31014a81b4882857c90c565ebc14210`. Gate code is byte-identical to exercised27dfd98 at the after revision. Exact argv/stdout/stderr/exits and probe identities: `corpus/evidence/round-15/measurements.json`.

| Claim | Literal counting commands | Observed result / evidence |
|---|---|---|
| C1 operability | `node .ufo/waves/round-15/measure.mjs 7054a5e1068538349b4dbb0d291c2fe8643802f2 --claim C1`; same command with `b7cf0446a31014a81b4882857c90c565ebc14210` | **0→1**, both exit0;42/42 aggregate records,8 cause assertions/6 reasons,3 applicable/39 N/A,8 isolated reason controls; USER production blocked6/10. `count-before-c1.json`, `count-after-c1.json`; probe at27dfd98 |
| C2 calibration | `node .ufo/waves/round-15/measure.mjs 7054a5e1068538349b4dbb0d291c2fe8643802f2 --claim C2`; same command with `b7cf0446a31014a81b4882857c90c565ebc14210` | **0→1**, final exits0;9/9 actual mirror differentials refused; snapshot2/snapshot_tampered; canonical correction1; browser_executed0. `count-before-c2.json`, `count-after-c2-repaired.json`; repaired probe at9fd8bca; original failed counter retained separately |

Per-axis author verdicts: **operability improved (C1), calibration improved (C2); depth, coverage, freshness and adjacency unchanged**. Six scalar deltas remain0. No demonstrated axis harm is claimed from unchanged historical evidence or explicit uncredited limits; independent admission remains the non-author closure's duty, including review of the disclosed derive interface change. Saturation8/window3, position2 after the round13 capability; no waiver/retirement. Planned survivor/user-record and new browser-frontier work remains open, not counted complete.

## Sources & frontier

No new source row: **29→29**, A23/B4/C2, mined24/queued3/rejected2; added tiers A0/B0/C0. S029 was opened this round at `cleanup.server.perWorker[0].listeningAfter`; dated located two-word quote and all transitions are in the lesson Gate. Only used-by changed: `corpus/lessons/round-14.md`→`corpus/lessons/round-14.md, corpus/lessons/round-15.md`; status/recheck/opened/immutable cells unchanged. Direct source-index cites S029; frozen v1 used-by stays lesson/knowledge paths. No frontier row advanced, knowledge/map32/32, no missing path, no new capability. Existing extension↔daemon, native WebMCP, rate/rights real-site, real-site journey and WebMCP-mining ground stays open. Source-row/fixture growth is not expansion.

Histogram counting commands (each exit0):

```sh
node .ufo/waves/round-15/measure.mjs 7054a5e1068538349b4dbb0d291c2fe8643802f2 --histogram
node .ufo/waves/round-15/measure.mjs b7cf0446a31014a81b4882857c90c565ebc14210 --histogram
```

Both output rows29, tiers A23/B4/C2, queued3/mined24/rejected2, knowledge32/mapped32/missing[]. Receipts `histogram-before.json`, `histogram-after.json`. Source live gate exit0/29 clean in `sources-live.json`.

Start and end census command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

Both observed exit0, both exact stdout:

```text
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```

Receipts `.ufo/waves/round-15/before.json` and `corpus/evidence/round-15/census-after.json`. No operator-* teaching files matched the bounded glob. The Mistakes table mines wrong-cause controls, unchecked mirrors, tamper classification, report misrooting, source-layer overreach and L1's erroneous quote-count correction; actual causal failures are retained, not merely proposed tests.

Open L0: prior tabi round5 external-action approval and round1 namespace/dispatch questions remain untouched; no new question appended. Orchestrator actions: independently spot-check current admits/rejects, verify/file the Node-spec non-author erratum to round14 wording, and supply the outstanding current frozen step1/step4 closure certification. Neither wave validation nor manual source reading substitutes for that certification.

## Trend verdicts

- **expansion: unchanged** — no new knowledge note, capability or newly held frontier; histogram/maps remain32/32.
- **quality: improved** — actual cause-specific counter controls and canonical historical-metadata mirror/tamper checks improve held evidence; originals remain fixed, genuine failed counter/USER production preserved. Evidence: source-bound diagnostic/differential receipts and corrected parser result.
- **discernment: improved** — prior outside routed precision findings become lesson-backed QUALITY20/21; source audit distinguishes the executed spec from its pin summaries and routes the outside-review erratum without rewriting it. This is learning, not current outside agreement: independent round15 admit/reject verification remains pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md round15 decision table/current registry; S029 and `source-index.json`; no non-author certification claimed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — historical `corpus/knowledge/multi-step-journey.md`; retained round13 browser receipt and LOG round13; round15 is static evidence repair, not another browser task.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md`; current exact command receipts/registry; prior executor was author-side.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md; own-lane browser-evidence/counter changes only; external publishing/credential/forensic boundaries retained. No promotion or [x].
