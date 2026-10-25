# mori — round 14 (attempt 1)

## Work performed

**One claim: C1 — coverage**, repairing round 13's rejected-harmed journal cutover while acquiring typed subject/result handling. Restore `OOM_KILL_JOURNAL` critical/DRIFT, fleet-only failed-unit findings and non-fleet tsukuroi routing, preserve all six independently scoped counters, and retain supported signal warnings. **Verified at the bounded measured scope; independent closure remains pending.** Coverage is the lowest owned axis (6 versus operability 7); no extra scalar point is awarded for repairing a prior harm.

- Read `corpus/lessons/round-13-verifier-spotcheck.md` first and learned all six routed mori defects. Historical author admission/no-harm statements are explicitly superseded, not rewritten (`corpus/lessons/round-14.md`, `SCORECARD.md` round-14 section; commit `8d22d18fb4a4124becb35123ca839c93cbae0028`).
- Restored exactly one global `OOM_KILL_JOURNAL severity=crit` when either journal scope has an OOM notice or `UNIT_RESULT=oom-kill`. Four scope/source counts remain separate; no notice/kill total is summed. OOM result alarms do not depend on subject classification (`tools/mori-census.sh` `probe_journal`; `evidence/green-after-accepted/evidence.json` under `.ufo/waves/round-14/`).
- Restored fleet/non-fleet partition using exactly one valid `UNIT` or `USER_UNIT`, independent of journal query scope. Both generic routes remain **INFO**, matching the pre-r13 policy. Non-fleet output names `owner=tsukuroi`; ambiguous/missing/malformed subjects are separately unattributed with `owner=unresolved`. Manager emitter fields are never substituted. The historical name-token rule is a heuristic, not exhaustive membership proof (same gate; `corpus/knowledge/journal-alarm-routing-r14.md`).
- A source/critic review found the pre-r13 user `UNIT_RESULT=signal` warning was also lost. Restored that arm alongside process SIGKILL, with separate `process_sigkill`/`user_unit_signal` counts and unknown sender/cause. Generic `signal` does not prove signal 9 (`R14_UNIT_SIGNAL_WARN`; lesson M7).
- Registered both verdict-producing regression gates, added real isolated self-invocation checks, qualified F01 whole-function/F02 reconstructed-shim provenance, corrected historical index/Q16 wording, and replaced the overbroad “no structured field” reason. These are supporting conformance/learning repairs, not extra claims (`SKILL.md` Gates; QUALITY Q29–Q32; lesson M1–M8).
- One validated **32-seat** wave, payload unchanged: 9 executors, 6 scouts, 3 connectors, 3 reviewers, 4 critics, 3 scribes, 2 sentinels, 1 revenger, 1 mutation-tester. L1 held the canonical planner seat; no `model` parameter or routing change. Specs, dispatch and bound registry: `.ufo/waves/round-14/{spec.json,dispatch.json,build/swarm-registry.json}`. Seats made source/fixture observations; only L1 ran the integrated gates/selftests.

All lane-relative evidence paths below resolve under `/home/vgpnk/Projects/shokunin/mori-shokunin`.

## Landed changes

**Pushed lane HEAD: `52512aea760472e30e9d08f8838ad48d122dd109`.** Lane working tree was clean after push and before this report was written. All commits use `mori-shokunin <mori@shokunin.local>`; the lane started clean at `dbe85009253c092fe50e4e93056fceeae273ec31`. Protected verifier/aggregator lessons and SHONEN were not edited.

| Commit | Landed work | LOG linkage |
|---|---|---|
| `a5cc313` | Original entering census/oracle bytes, independent expected repair gradient, wave specification/dispatch, initial source census | LOG round-14 “Repair expectations … a5cc313” |
| `8d22d18` | Production alarm/subject repair, 104-case census selftest, migrated r13 gate, new r14 gate, sources/knowledge/quality/active-doc corrections and 32 seat reports | LOG round-14 declaration, source-read severity correction and provenance correction |
| `5601d12` | Corrected a **measured gate setup bug**, retained original failed receipts and initial integrated checks | LOG “Integrated code/knowledge checkpoint …” and lesson M8 |
| `52512ae` | Accepted red/green receipts, live parity/drift evidence, counting command, score/capability/trend records and final documentation | LOG “Correction measured …” through round-end assessment |

The initial r14 gate crashed in fixture setup: a literal shell `printf '%s'` was mistakenly consumed by Python `%` formatting. That rc1 is **not** behavioral red evidence. Its actual selftest rejected missing stable ids/evidence. L1 escaped it as `%%s` and mapped unexpected internal errors to explicit could-not-evaluate exit 2. Original `evidence/{r14-selftest,red-before,green-after}.json` receipts remain; accepted receipts have distinct names. Census/oracle/r13-gate bytes did not change during this correction.

## Before → after measurements

Measured production census SHA-256: `0e41cb83fce2e8c5c711171e1cde2e6fa2809dcfce630eccabe52bcbe41516d9`.
Frozen entering census: `39abda0a67028575d888d9157b8548dec0b4944c3d8c165691e88ab657fc3985`.
Accepted r14 gate: `c39e5a7352666d09dc662293e1ea7be47ee3523b53247a5a6ae02e7dda19288d`.
The paired strict measurements name commit **`5601d1201926124f7884bc694568abac2ead6d5c`**.

Commands executed from the lane root:

```sh
python3 tools/mori-round14-regressions.py --census .ufo/waves/round-14/frozen/mori-census.sh --output .ufo/waves/round-14/evidence/red-before-accepted
# exit 1: 43 failed strict assertions, with named behavioral failures below
python3 tools/mori-round14-regressions.py --census tools/mori-census.sh --output .ufo/waves/round-14/evidence/green-after-accepted
# exit 0: 43 cases + one required frozen-red control = 44 pass
jq -s '[.[] | [.claims[] | select(.id == "R14_OOM_ALARM_USER" or .id == "R14_OOM_ALARM_SYSTEM" or .id == "R14_UNIT_OOM_KILL" or .id == "R14_UNIT_FAILED_FLEET" or .id == "R14_UNIT_FAILED_NONFLEET" or .id == "R14_UNIT_SIGNAL_WARN") | select(.status == "fail")] | length]' .ufo/waves/round-14/evidence/red-before-accepted/evidence.json .ufo/waves/round-14/evidence/green-after-accepted/evidence.json
# [6,0], exit 0
```

| C1 acceptance arm | Frozen entering → repaired | Evidence |
|---|---|---|
| User/system OOM notices | CLEAN/rc0, no critical alarm → DRIFT/rc1, exactly one global critical alarm | `R14_OOM_ALARM_USER`, `R14_OOM_ALARM_SYSTEM` |
| OOM unit result, including non-fleet or unusable subject | Missing critical alarm → critical/DRIFT independently of subject validity | `R14_UNIT_OOM_KILL`, `R14_UNIT_OOM_NONFLEET`, missing/array-subject cases |
| Fleet/non-fleet routing | Generic unpartitioned unit finding/no tsukuroi route → fleet-only INFO and non-fleet INFO owner=tsukuroi | `R14_UNIT_FAILED_FLEET`, `R14_UNIT_FAILED_NONFLEET`, `R14_UNIT_PARTITION` |
| Legacy user signal result | CLEAN → KILL_SIGNAL_JOURNAL WARN/DRIFT; not asserted to be signal 9 | `R14_UNIT_SIGNAL_WARN`; system signal-result control stays informational |
| Six raw scoped counters | Identical nonzero fixture vectors before/after: user **3/0/2/1/2/1**, system **2/1/4/3/0/2** | `evidence/c1-measurement.json`, `R14_SCOPED_PARITY` stdout for frozen/SUT |
| Live scoped counts | Two scoped rows retained; **12/12** source-bracketed cells match, all zero | `evidence/live-measurement.json`, including exact Python reproducer and query argv |

Vector order: kernel-OOM notice, oomd notice, coredump notice, signal11 record, process-SIGKILL record, unit-failure record. Scopes are never summed. The live observation is **not positive-load, killer activity, unique-victim or fleet-cause proof**. One live wall-time pair was 3.022859 → 2.975920 seconds, not a speedup/distribution claim.

**Red-run limitation:** every frozen strict case also fails newly required metadata/query-shape invariants, including controls. Thus 43 failed assertions are **not 43 production defects** and the coarse total is not the claimed improvement. The six named arms additionally have inspected missing-alarm/roll/route reasons; raw-counter preservation is measured independently. Both commands used the same committed gate/expected values and case ids. Temporary paths differ; byte-identical full fixture trees are not claimed (`evidence/c1-measurement.json`).

Other checks actually exercised:

| Check | Measured result / revision |
|---|---|
| `bash -n tools/mori-census.sh` | exit 0 at 8d22d18 |
| `bash tools/mori-census.sh --selftest` | **104/104**, exit 0 at 8d22d18; final census bytes unchanged |
| `python3 tools/mori-round13-regressions.py --selftest` | **33 checks + 2 isolated cases**, exit 0 at 8d22d18 on gate SHA `304cb223…` |
| r14 gate `--selftest` | **20 checks**, including real red rc1/tamper rc2 subprocesses, exit 0 at 5601d12 |
| r13 gate `--mutation both --jobs 1 --output .ufo/waves/round-14/evidence/r13-preserved` | **24 pass + 2 mutation-red**, exit 0 at 8d22d18; exact-author progressing held, BANANA 0/28 and honest oracle 28/28 held |
| Old r10 `--drift corpus/evidence/baseline-r10-20261015T2231Z.json` | exit **1** at 5601d12, retained and not re-pinned; not a freshness pass |

Receipts are `evidence/{census-syntax,census-selftest,r13-selftest,r14-selftest-accepted,r13-preserved,drift-current}.json` under round-14 waves. Historical r13 24-check selftest at 80bd58a is not misattributed to delivered c13df48. F01 mutations replace the whole frozen `grade_lane`; F02 uses a reconstructed prefix shim, not original function bytes. Original-frozen failures remain primary historical defect evidence.

Per-axis verdicts:

| Axis | Verdict | Score / basis |
|---|---|---|
| coverage | **improved** | 6 held; six named acceptance failures 6 → 0; no point for repair alone |
| operability | **unchanged** | 7 held; F01/F02 retained, actual delivered selftests measured; gate setup defect corrected honestly |
| depth | **unchanged** | 5 held; sources support C1, no separate depth move |
| freshness | **unchanged** | 5 held; live recheck recorded, old drift pin remains red |
| calibration | **unchanged** | 5 held; lesson-backed criteria and qualified claims, no scalar self-credit |
| adjacency | **improved** | 6 held; collateral restoration within C1, measured tsukuroi route and no ownership takeover |

Notice alarms and system-scope OOM-result alarms are **explicit operator-required extensions**, not a claim that every pre-r13 MESSAGE pattern matched those notices. Historical user `oom-kill` and `signal` result alarms are restored through typed fields. Mori reports host events; tsukuroi diagnoses OS units; the operator owns host actuation. No remediation or sibling-file mutation occurred.

Retained limitations: client-set labels can forge positives; malformed MESSAGE_ID can make a whole class unavailable and hide a valid alarm (`R14_SEC_DUP_MSGID_MIXED`); unavailable itself does not cause DRIFT; environment-selected binaries/timeout overrides remain trusted/unvalidated; partial access/retention, exhaustive fleet-name recall, arbitrary oracle tally corruption/aggregate vacuity and adaptive forgery remain outside the guarantee. Selected cgroup-local counters do not substitute for journal alarms. No live GPF regression or complete coverage is asserted.

## Sources & frontier

Required command executed at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Before (exit 0), retained in `.ufo/waves/round-14/sources-before.json`:

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

After (exit 0), retained in `sources-after.json` and `evidence/sources-after.json`:

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

The maintained validator treats W04 as informational for separately scoped rows. Row census: **36 → 38**, A33 → A35/B2/C1, mined15 → 17/queued20/rejected1. Counting code used by L1 (equivalent replay command is stored in `sources-after.json`):

```python
import re, collections, pathlib
rows = [line.split('|')[1:-1] for line in pathlib.Path('corpus/SOURCES.md').read_text().splitlines()
        if re.match(r'^\|\s*S\d{3,}\s*\|', line)]
print(len(rows), dict(collections.Counter(r[3].strip() for r in rows)),
      dict(collections.Counter(r[7].strip() for r in rows)))
# before: 36 {'A':33,'B':2,'C':1} {'mined':15,'queued':20,'rejected':1}
# after:  38 {'A':35,'B':2,'C':1} {'mined':17,'queued':20,'rejected':1}
```

- Added **S037 docs/A**: manager subject UNIT/USER_UNIT versus emitter metadata, [official journal-fields documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html).
- Added **S038 code/A**: exact `SERVICE_FAILURE_OOM_KILL → "oom-kill"` vocabulary, [pinned service.c:6598](https://github.com/systemd/systemd/blob/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/src/core/service.c#L6598).
- Reopened S002/S013/S015/S035/S036. Only allowed used-by cells changed; exact old → new lists and ≤25-word located quotes/access dates are in `corpus/lessons/round-14.md`. No immutable row fields were rewritten.
- New sourced knowledge on the FR1 typed subject/result plane is demonstrated by fixtures, not row volume. Kernel-victim event-time attribution, signal sender and fleet causal correlation remain frontier; a no-marker unit can still be real fleet work. Existing counter/source claims are retained with their historical text-selected sample qualifications.
- Mistakes M1–M8 and Q29–Q32 learn the previous outside rejection and this round's caught setup failure. Independent round-14 admit/reject spot-check is still required; dispatched seats are the author lane.

## Trend verdicts

- **expansion: improved** — `journal-alarm-routing-r14.md`, citing mined S037/S038, adds working typed subject/result-plane classification and explicit unattributed handling on FR1 ground. Restored policy alone and two extra source rows are not the expansion argument.
- **quality: improved** — the rejected no-harm inference is marked and repaired, nonzero counter preservation and all-zero live recheck are separately evidenced, and registered gates exercise actual isolated subprocesses. The setup crash is retained as a failure, not disguised as red-before.
- **discernment: improved** — the prior non-author disagreement becomes Q29–Q32 and able-to-fail witnesses (lesson M1–M8). This does not claim current outside agreement or treat L1's seats as independent reviewers.

Stale-lane: respawn-per-round assignment; mori round 14 progressed through the lane-authored commits above. No other mori mission is assigned to this L1, and no driver restart/steering occurred.

L0: none added or blocking. The historical `mori | round-1 | Which operator-selected remote URL…` question remains filed; this round's configured lane push succeeds, so it is not an operational blocker and its original line is not rewritten. No rank/promotion decision or ledger edit is made here.

Tools installed/updated: **none** by L1 or seats. Read-only domain sources stayed read-only; push scope was the own lane and the serialized fleet report only.

## SHONEN

All actual SHONEN boxes remain `[ ]`; the lines below are author assessments, not non-author promotion marks.

- [~] SKILL decision tables/error patterns/checklist and cited authorities: `SKILL.md`, SOURCES S037/S038, `journal-alarm-routing-r14.md`; current outside verification pending.
- [~] End-to-end domain task executed/logged: LOG round-14 live task, strict red/green fixtures and `evidence/live-measurement.json`; live positives are not claimed.
- [~] Executable without oral context: registered CLI/exit maps, census 104/104, r13 33 checks/2 cases, r14 20-check selftests and committed generators/digests; old drift pin intentionally remains red.
- [~] No cross-domain bleed / province accurate: `PROVINCE.md` and measured non-fleet `owner=tsukuroi` routing; detection/report only, no OS or sibling mutation; outside closure still owns the no-harm/promotion decision.
