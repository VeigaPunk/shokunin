# chousa — round 26, attempt 1 — recovery and honest non-admission

## Work performed

Declared claims, registered at `f361d12e44687841e30ec35710ddb366c6f795e0` against `ba3333254dd337658a4f25e7a9471f9cf4e4567e`:

- **C1 / operability:** remove metadata-entry reader allocation amplification while preserving plain output and refusals; the lowest measured axis remains the narrow r1 score3/10. Four frozen shapes amplified4/4 before and0/4 after. **Narrow measured improvement, not verified under the complete claim contract**: the cumulative selftest fails and falsification is incomplete. Evidence: `chousa-shokunin/corpus/evidence/round26-{claims.md,measure-before.log,inherited-after.log}`.
- **C2 / freshness:** compute explicit-as-of assessment deadlines. Frozen counters meet predictions, but independent input-domain counterexamples falsify the implementation. **Harmed / falsified**, not admitted. Evidence: lane `.ufo/waves/round-26/falsify/FDateHugeCadence.md`, `FDateAsOfUsage.md`, `FDateExplicitDate.md`.
- **C3 / calibration:** screen local registry ID/status/exact rooted backlinks and descriptive verification text, not semantic source support. Frozen counters meet predictions, but parser-state/tokenization/refusal counterexamples falsify the implementation. **Harmed / falsified**, not admitted. Evidence: lane falsify `FRegistryHeaderless.md`, `FRegistryIdBoundary.md`, `FRegistryAbsentRow.md`, `FRegistryRegistryDeny.md`.

**Round verdict: NOT ADMITTED.** The no-harm condition fails;31 falsify assignments produced no report. No missing test is inferred green, no threshold/oracle was relaxed, and no capability or promotion is awarded. This report completes the author's durable record; separate non-author closure owns admission and fleet state.

- Recovered the already-held round26/attempt1; no new claim or round. The recovery request understated inherited work: ChousaR26R had integrated/pushed production target `0e9784bd52eca456b24d0bc40921480a47f91a2b` and dispatched falsify68 after original build64. Evidence: lane `corpus/evidence/round26-measured-revision.json`, both retained dispatches/registries/spawn manifests, `recovery-dispatch-provenance.json`.
- Reconciled every132 original identity against its terminal transcript and report. Build39 reports/25 no-report; falsify37 reports/31 aborted no-report. All132 have terminal session_exit records; observed proc state listed no live Chousa build/falsify child. No seat was spawned, resumed, replaced or rerouted by this recovery. Evidence: lane `.ufo/waves/round-26/{build,falsify}-final-reconciliation.json`.
- Preserved all inherited seat evidence. Four build reports had late in-place revisions: checkpoint bytes are now retained as each report's prefix, with the complete late revision appended. Final combined hashes and exact late bodies are in `append-only-report-preservation.json`; these supersede the initial recovery report hashes only for those four paths. No finding was discarded.
- Preserved the inherited critic's exact counting output and provenance rather than rerunning a known failed check: `corpus/evidence/round26-inherited-after.log`, `round26-inherited-measurement.json`. The critic exceeded its bounded assignment by running full probe/selftests and background shell jobs; that procedural defect is recorded, not relabelled authorized L1 or outside verification.
- Marked unsafe implementation claims and withheld knowledge admission in the three round26 notes, SKILL, README and SCORECARD; appended mistake/disposition rows R26-M5–M13. No production executable, counting probe, oracle or registry bytes changed in final recovery. Identity evidence: `corpus/evidence/round26-recovery-identity.json`.
- Reconciled previous outside-check intake from `MANIFEST.json rounds[395]` (read-only) and the existing round24 verifier lesson. C1 exercises the routed allocation risk; the appender race, other readers, filesystem races, parent-root rechecks, receipt gaps and source/span pairing remain open. Evidence: lane lesson `round-26.md` Spot-check intake and final disposition; build `ScoutCarriedDebt.md`, `ExecReaderCensus.md`.

## Landed changes

**Pushed lane commit:** `64eec5d41c7cf7f17f5ce1e968e28b3769952596` — helper printed `landed 64eec5d41c7cf7f17f5ce1e968e28b3769952596`.

Every recovery change is tied to `chousa-shokunin/LOG.md:1034-1072` (Round26 final recovery disposition), following the original declared-work/checkpoint entries at963–1032:

| Change | LOG/evidence | Carrying landing |
|---|---|---|
| Durable late build/falsify reports, reconciliation, exact terminal errors and append-only report preservation | LOG1038–1050; lane `.ufo/waves/round-26/` final manifests | `64eec5d41c7cf7f17f5ce1e968e28b3769952596` |
| Inherited measurement receipt, provenance, executable identity and final census | LOG1052–1065; `corpus/evidence/round26-*.json`, `round26-inherited-after.log` | same |
| SCORECARD measured verdicts and no-admission/capability disposition | LOG1066–1070; SCORECARD `Round26 recovery verdict` | same |
| SKILL/index/three knowledge-note safety and withdrawal addenda; lesson mistakes and source/debt reconciliation | LOG1066–1070; lesson `Final recovery and falsification disposition` | same |

Production measurements below target immutable `0e9784bd52eca456b24d0bc40921480a47f91a2b`, not modified documentation at recovery landing. Six executable/counting/oracle/registry input identities match that target; final recovery adds evidence/qualification only. No stale pre-falsify identity pin is presented as a passing suite.

Final helper state:

```text
state branch=master local=64eec5d41c7cf7f17f5ce1e968e28b3769952596 remote=64eec5d41c7cf7f17f5ce1e968e28b3769952596 ahead=0 behind=0 head=detached tracked=0 untracked=0
```

## Before → after measurements

Counting command, with TREE the isolated archive of the stated measured revision:

```sh
bash corpus/evidence/round26-measure.sh TREE all
```

Before receipt: `corpus/evidence/round26-measure-before.log`, base `ba3333254dd337658a4f25e7a9471f9cf4e4567e`. After receipt: `round26-inherited-after.log`, target `0e9784bd52eca456b24d0bc40921480a47f91a2b`, gate SHA256 `c2c813f1b425bc4e74625a2607eaca1b97addf9898f834e88af8f1fe2143abc6`. Both are actual inherited executions, not reconstructed predictions. The after provenance identifies critic FNoTrade and exact tool-result record `bfe44158`; recovery did not rerun failed checks.

| Claim / hold | Before → after | Interpretation |
|---|---|---|
| C1 amplification |4/4 →0/4 on four8,388,000-byte shapes | Narrow RSS improvement only; control11,644→11,880KiB; newline case2,238,736→54,536KiB; time90.6→86.4s is recorded, not claimed |
| C1 plain frozen29 | rc1, SHA `3f83ba4844cac8d2057b47661be225f84a5945fc7c1db739ec2070b6aa2a4a37` → identical | Complete26/29; three legacy warnings unchanged |
| C2 classification / oracle / planted controls |0/29,0/29,0/6 →29/29,29/29,6/6 | Frozen success is insufficient: independent locale/cadence failures remain |
| C3 controls / positive / prospective frozen population |0/5,0/1,0/5 →5/5,1/1,5/5 | Five-entry population adjudicated true negatives by FRegistryPopulation; broader C3 claim still falsified |
| Shared selftest | PASS161, exit0 → **FAIL3/187, exit1** | Decisive failed registered hold; three new usage assertions incorrectly match help text; no suppression/fix credited |
| Legacy161 case lines | SHA `5eac4a7e2af964f6e81631f66990426e5c8ef58fb41ba6ec6d0054ef819e01cb` → identical | Not a full-suite PASS |
| r12 drift / r1 archived-input observable | none,rc0 /3/3 → same | Operability scalar3→3, delta0; not a resource/readiness score |

The original probe uses an explicit fleet-root equivalent of the original sibling-layout r1 command; FNoTrade also exercised the original form at3/3. Do not attribute the probe's spelling as literally the original command. Probe exit0 means completed, not admitted: it printed the failed selftest. FMutateC1Killed, FMutateC2Killed and FMutateSourceMissingKilled retain bounded0→1→0 behavioral sensitivity runs; the missing FMutateC3Killed report is not inferred from them.

No final recovery build/test/lint/formatter/smoke run is claimed. The remaining counterexamples are explicitly marked in every affected current instruction/note. No new repertoire row was added.

## Sources & frontier

The exact contract census command at inherited start and final recovery end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Both recorded stdout:

```text
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```

Both exit0; stderr empty at end. Evidence: `round26-census-before.json`, `round26-census-end.json`. Counting operation used for row/tier/status inventories (cwd lane root):

```sh
python3 -c 'import pathlib,re,collections; rows=[[c.strip() for c in l.split("|")[1:-1]] for l in pathlib.Path("corpus/SOURCES.md").read_text().splitlines() if re.match(r"^\|\s*S[0-9]{3,}\s*\|",l)]; print("rows",len(rows)); print("tiers",dict(collections.Counter(r[3] for r in rows))); print("statuses",dict(collections.Counter(r[7] for r in rows)))'
```

Observed33→39 rows; tiers A27→33/B1→1/C5→5; statuses mined10→16/queued19→19/rejected4→4. New rows S034–S039: A+6/B+0/C+0. Their opened documents/own-work, access date2026-10-21, ≤25-word located quotes and scope/inference boundaries are in lesson `## Gate`. The public documentation seats corroborated S037/S038/S039; no external live-target research is claimed. S038's mutable served-version observations differ between seats; the exact located quote is corroborated and the drift limit is retained, not silently rewritten.

Only existing field change: S029 used-by `corpus/knowledge/metadata-screen-r25.md` → that path plus `corpus/knowledge/recheck-due-r26.md`; status mined→mined and recheck on-release→on-release unchanged. No other pre-existing status/recheck change. Six new rows remain mined because retained notes cite them; **mined means cited, not admitted implementation**.

Three new notes32 total files versus29 at base are retained as qualified/withdrawn candidates, **zero admitted expansion credited**. README's earlier held-ground wording is expressly superseded. Sourced candidate C2 cites S035/S037/S038 and reopened S029; its implementation failure prevents treating frontier bookkeeping as claim admission. No province expansion or automatic source truth claim.

Mistake mining: original array-allocation R26-M1 is shown red by4/4 before; C1's narrow0/4 result and real mutation sensitivity are retained. Additional R26-M5–M13 name actual selftest/domain/parser/reader/oracle/scope/preservation failures and the criterion that should catch them. No written rule is counted as a fixed implementation without a failing control. Existing QUALITY18 and QUALITY17 apply; no extra criterion count is invented.

## Trend verdicts

- **expansion: unchanged.** New files/source rows exist but their implementation candidates are not admitted; no acquired capability or new held province ground is credited. Evidence: three note addenda; README `Round26 frontier admission correction`; SCORECARD recovery verdict.
- **quality: harmed.** The delivered executable's shared selftest fails3/187 and independent C2/C3 counterexamples remain. They are now marked rather than left as unqualified instructions, but documentation does not repair the gate. Evidence: FNoTrade and the decisive falsifier reports above.
- **discernment: unchanged.** Falsification and mistaken source/oracle/verification assumptions are explicitly recorded, but lane-dispatched seats are author advice and no round26 outside admit/reject sample exists. The previous round's outside agreement is not reused as a fresh judgment. Evidence: lesson outside-spot-check slot and R26-M5–M13.

## SHONEN

- [~] Real decision tables/error patterns/checklists/sources: SKILL decision table and Gates; round26 safety/status addendum. Lane assertion only, no new non-author verifier.
- [~] End-to-end domain task executed/logged: historical round9 archive task and r25 explicit-root battery, SHONEN.md box2. No new round26 task-success assertion.
- [~] Executable instructions: historical evidence remains, but current shared selftest fails; FNoTrade and current safety addenda disclose it. This is not verification or promotion.
- [~] No cross-domain bleed: PROVINCE unchanged; source notes scope Cochrane/Python/PROV facts versus lane policy. No external live-target action or domain-source write.

## Waves, recovery mechanics and open L0

- **Build64:** executor10, sentinel2, simplifier1, scout21, connector2, reviewer12, revenger4, critic6, scribe6. L1 holds canonical planner; validator excludes planner role. Retained validator dispatch/registry and task adapter are original evidence. Dispatch-attempt record has two job-cap refusals08:44:14/08:47:18, then accepted08:50:18; no split/replacement.
- **Falsify68:** reviewer26, scout32, mutation-tester4, critic2, simplifier2, connector1, scribe1. It already existed before this recovery; no optional new≤64 wave was used. One accepted task call,0 cap refusals; stored core payload context/name/role/task fields equal validator output, with only required solutionSpace schema metadata added. Captured aliases: m_swe26, m_auto35, m_sol4, m_composer2, m_haiku1; no model parameter, no fresh-route change.
- **132 total seats**,0 replacements. Build25 without reports end on retained provider errors;37 historical provider-death marks overlap reports that later landed and must not be added as distinct dead seats. Falsify31 without reports end `Request was aborted`/terminal dispose; the37 retained reports stand on their own evidence. Initial no-report header/reader/separability/mutation/audit assignments remain incomplete. Exact per-seat last error/model/time and report hashes are committed in final reconciliation manifests.
- Coordinator terminal record correction: original ChousaR26 Devin weekly quota; R last assistant error Codex `cyber_policy`; R2 Opus429. Exact messages are retained in `round26-inherited-measurement.json`. No denied workflow was retried, and no policy/routing/runtime setting was changed.
- Slot capture for inherited falsify: granted chousa/r26-falsify68, live116/pending0/cap240. Recovery status live46/recent0/cap240; released `chousa r26-falsify` after confirming all child transcripts terminal. No retroactive acquire or new task call was fabricated.
- Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only tracked driver-runtime changes, no untracked lane seat files. Nothing copied/deleted outside lane; runtime files untouched.
- **Stale-lane:** this same claimed attempt is now durably reported; no other Chousa mission observed open. Predecessor work and current evidence show progressing, not silent. No next round was started.
- **Tools:** no install/update by this recovery; retained seat reports record none. Shared pacman/host recovery L0 remains operator-owned and nonblocking.
- **Open lane L0:** chousa round12 “Receipt identity” authentic-dispatcher receipt requirement remains open. The old round1 remote question is operationally superseded by observed successful lane pushes. No new L0 question required; no ask.
- **Closure ownership untouched:** no MANIFEST/outcome/next/claims closure-state mutation. Separate non-author closure owns the eventual status/admission record; this report explicitly requests no admission from incomplete or falsified evidence.
