# mori — round 15

## Work performed

**Declared claim C1 — coverage:** retain the existing critical OOM/DRIFT and user-signal WARN/DRIFT alarms from individually qualified current-boot structured records when an adjacent semantically invalid record invalidates the aggregate class. Preserve raw totals and the subject-owner partition as unavailable, never substitute a subset for a total. This works the lowest owned non-retired axis, coverage6 versus operability7; no stagnation waiver or extra claim. Other axes are checked for harm, not awarded points.

**Pushed lane HEAD:** `61cce328935924d9c9e03bab2f6267ed259e1512`. Lane was clean before this report was written. Entering HEAD was `0fa5e0de194bcc270a927a166664113e6821442b`; no inherited uncommitted work was present.

- Added four per-scope `positive_*` evidence fields, strict scalar id/current-boot selectors and explicit subset/validation/firing bases. Healthy classes reuse their existing counts; only semantic aggregate failure invokes another parser pass over the same capture. No second journal query. Raw fields, severities, scope separation and aggregate-only owner routing survive. Evidence: `tools/mori-census.sh:1039–1055,1127–1268,1465–1630`; LOG.md round-15 integration/final entries; final paired manifests below.
- Landed an independently expected, pinned-input regression gate, 16 fixture packs/63 core cases, and seven additional capture-boundary cases. Frozen controls must actually complete and specifically miss a wanted alarm: timeout, execution/integrity failure or arbitrary red cannot certify the control. Hidden control-bypass flags were removed. Evidence: `tools/mori-round15-regressions.py` (`classify_control`, `analyze_case`, `guard_output`); `.ufo/waves/round-15/expected.json`, `boundary-expected.json`; `evidence/control-bypass-refused.json`.
- Learned all routed round-14 items: prospective exact dirty-path/input provenance; corrected class-count versus per-record wording; documented unavailable legacy process counts beside an independently valid signal arm; explicitly labelled old nonzero vectors as fixture evidence. Kept the old red drift pin and trust/access/retention/name-token qualifications. Protected reviews and all SHONEN boxes are untouched. Evidence: `corpus/lessons/round-15.md`, QUALITY Q33–Q36, new knowledge note; prior non-author `round-14-verifier-spotcheck.md:134–141`.
- Internal final review caught control-trust defects before L1 measurement. A later real capture-fixture setup failure exposed an oracle derivation bug: failed-producer bytes were still used to derive expected alarms. The fix omits failed scopes but retains independently available scopes. This is not production behavioral red. Evidence: `build/ReviewHarnessGate.md`, `evidence/boundary-pin-red.json`, `boundary-fixtures/capture.json`, LOG.md boundary-correction entry, all under the lane's round-15 evidence root.
- Executed one validated **64-seat** policy-v2 wave in exactly one batched task call with the validator payload unchanged, no model parameter: executor24/scout8/connector6/reviewer8/scribe6/critic8/sentinel2/revenger2. Round total64; no second wave. L1 held the canonical planner seat; ConnectPlannerWalk supplied a bounded data walk, not a planner-role bypass. All64 scoped reports exist; later nudges reused these identities. Evidence: `.ufo/waves/round-15/spec.json`, `dispatch.json`, `task-response.json`, `assignments.json`, `build/swarm-registry.json`, `evidence/c1-measurement.json`. Role routing remained host-owned; no runtime model distribution is inferred from the prompt's alias table.
- Cross-domain evidence remains routed, not absorbed: tsukuroi owns OS/unit diagnosis and the preserved non-fleet INFO route; kumitate owns dispatch/settlement semantics. No OS remedy, service restart, wave actuation or new ownership claim. Evidence: PROVINCE.md Core/Adjacent, `build/ConnectSiblingOverlap.md`, preserved r14 routing cases.

## Landed changes

All paths in this section resolve under `mori-shokunin/`.

| Carrying commit | Changes | Motivating/log record |
|---|---|---|
| `26f6589dfa2a07e41a6dcfda99c2998bce2c0932` | production positive-alarm retention and explicit object guards; census fixtures; r13/r14 provenance and the sole intentional r14 mixed-control migration; r15 gate/frozen inputs/core packs; skill/province/quality/source/index/knowledge/lesson work; validated swarm evidence | LOG.md `Round 15` and `Round-15 integration before measurement`; r14 outside routed debt and retained mixed-invalid control |
| `1822145d95682709069bbc8f4e1b947ddbe20078` | first committed-input receipts; failed-capture oracle correction; independent boundary fixtures/expectations; regenerated core expected table for the changed gate; generated sandbox cleanup | LOG.md `initial committed-input measurements and boundary correction`; actual `boundary-pin-red.json` setup rejection |
| `61cce328935924d9c9e03bab2f6267ed259e1512` | final paired receipts and seven boundary results, source census/claim measurements; calibrated SCORECARD and appended LOG/knowledge/lesson decisions | LOG.md `Round-15 final measurement`; `.ufo/waves/round-15/evidence/c1-measurement.json` |

All three commits were pushed to the lane remote before this report was created. No historical report, verifier/aggregator lesson, SHONEN mark, fleet runtime or MANIFEST was rewritten.

## Before → after measurements

### C1 coverage — verified at bounded fixture scope

Final gate SHA-256: `6a55c33cc13e2cd862ebd44db66e8af635a35d7cd2a85168360569c886d62ffe`; measured at **1822145d95682709069bbc8f4e1b947ddbe20078**. Both runs use the same committed 63 cases and the same gate. Entering target is pinned census SHA `0e41cb83fce2e8c5c711171e1cde2e6fa2809dcfce630eccabe52bcbe41516d9` from 0fa5e0d; delivered target SHA `f1f8d1b62bb617bbcc4664057ab807d3fed8c275b7aabbdf7b373323c5501ff7`. Parser is `/usr/bin/jq` **jq-1.8.2**, explicitly pinned for L1 verification; the host's unqualified jq reports jaq3.1.1.

Executed from the lane root:

```sh
python3 tools/mori-round15-regressions.py --census .ufo/waves/round-15/frozen/mori-census.sh --fixtures .ufo/waves/round-15/fixtures --expected .ufo/waves/round-15/expected.json --output .ufo/waves/round-15/evidence/red-before-final
# exit 1
python3 tools/mori-round15-regressions.py --census tools/mori-census.sh --fixtures .ufo/waves/round-15/fixtures --expected .ufo/waves/round-15/expected.json --output .ufo/waves/round-15/evidence/green-after-final
# exit 0
/usr/bin/jq -s '[.[].summary.sut_behavior_fail]' .ufo/waves/round-15/evidence/red-before-final/run-manifest.json .ufo/waves/round-15/evidence/green-after-final/run-manifest.json
# [34, 0], exit 0
/usr/bin/jq -s '[.[].summary.sut_fail]' .ufo/waves/round-15/evidence/red-before-final/run-manifest.json .ufo/waves/round-15/evidence/green-after-final/run-manifest.json
# [63, 0], exit 0
```

**Behavioral failures34→0; green63/63.** Full-schema63→0 also includes new metadata absent from the old bytes; neither number is a count of distinct historical bugs. Both bundles reproduce **34/34** specifically missing-alarm frozen controls, with no inconclusive/unexpected controls; the other29 legacy controls pass. The final green manifest records `revision.stable=true`, `inputs.unchanged=true`, actual HEAD and exact dirty paths. Dirty output paths are not concealed or called a clean worktree.

Seven separate boundary cases pass (gate exit0), with frozen1/1 red: producer rc124/137→timeout, rc5, stderr, malformed JSON, a mixed-positive control and a valid system alarm surviving failed user capture. `capture-boundary.json` and its `run-manifest.json` retain the invocation and raw captures. The earlier pin exit2 is retained as setup error, not counted as C1 red; its subsequent pack also adds a distinct other-scope case, so no whole-pack single-delta causal claim is made for that oracle repair.

Executed query-count command:

```sh
/usr/bin/jq '[.runs[].journal_argv_count] | unique' .ufo/waves/round-15/evidence/green-after-final/run-manifest.json
# [12], exit 0
```

All126 paired target runs record12 producer calls. One final paired wrapper measurement took26.863087s before /27.530636s after (each includes its own frozen-control runs); this is not a latency distribution, speedup or no-regression performance proof.

### Preservation and other axes

| Executed check | Observed result | Receipt / measured revision |
|---|---|---|
| `bash tools/mori-census.sh --selftest` | 113 PASS,0 FAIL, exit0; includes primitive-neighbor, primitive-only and truncated-JSON boundaries | `evidence/census-selftest.json`, 26f6589 |
| `python3 tools/mori-round13-regressions.py --selftest` | checks33/cases2, exit0 | `evidence/r13-selftest.json`, 26f6589 |
| `python3 tools/mori-round14-regressions.py --selftest` | checks20, real-gate red rc1/tamper rc2, exit0 | `evidence/r14-selftest.json`, 26f6589 |
| `python3 tools/mori-round15-regressions.py --selftest` | full frozen-control synthetic subprocess checks and control-classifier checks PASS, exit0 | `evidence/r15-selftest-final.json`, 1822145 |
| `python3 tools/mori-round13-regressions.py --mutation both --output .ufo/waves/round-15/evidence/r13-preserved` | 24pass +2mutation-red, exit0 | `evidence/r13-preserved.json` and bundle, 26f6589 |
| `python3 tools/mori-round14-regressions.py --output .ufo/waves/round-15/evidence/r14-preserved` | 44pass, exit0; only mixed-invalid control's intended alarm expectation migrated | `evidence/r14-preserved.json` and bundle, 26f6589 |
| `bash tools/mori-silence-cases.sh` | matched28/total28, exit0 | `evidence/silence-oracle.json`, 26f6589 |
| `bash tools/mori-census.sh` | exit1; findings20/drift11/unavailable1/surfaces8; user/system journal rows both present, all six raw classes and all four positives zero per scope | `evidence/live-census.json`, 26f6589 |
| `bash tools/mori-census.sh --drift corpus/evidence/baseline-r10-20261015T2231Z.json` | exit1, old baseline still red, including declared volatile/schema changes; not re-pinned | `evidence/drift-current.json`, 26f6589 |
| former hidden `--selftest-child --no-frozen-control` combination | unrecognized arguments, exit2 | `evidence/control-bypass-refused.json`, 1822145 |

Evidence root for the table: `.ufo/waves/round-15/`. Census/r13/r14/oracle verdict-driving bytes are unchanged between26f6589,1822145 and pushed HEAD; only r15 gate expectation derivation/cleanup changed between the first two. Whole source/host equivalence is not claimed. The live zero observation is one boot/window, not positive-load evidence or proof of no event. F01 remains a whole-function transplant and F02 a reconstructed shim, not byte-exact single-line causality.

| Axis | Verdict | Score | Evidence / bound |
|---|---|---|---|
| coverage | improved | 6 held | C1 finite behavior34→0; unavailable raw totals preserved |
| operability | unchanged | 7 held | preserved gates and delivered selftest/controls pass; actual setup error disclosed and repaired |
| depth | unchanged | 5 held | sourced predicate/interface details support C1, no separate claim |
| freshness | unchanged | 5 held | live recheck performed; old drift pin remains red debt |
| calibration | unchanged | 5 held | subset0 ≠ absence, fixtures ≠ live load, exact scope/hash provenance; procedural defects disclosed |
| adjacency | unchanged | 6 held | aggregate-only routing retained, no OS/orchestration ownership or actuation |

No scored axis harm was observed at this bounded scope. **Lane claim assessment: verified; final admission remains the independent non-author closure/operator's decision**, including procedural debt below.

## Sources & frontier

Reopened S014/S015/S037/S038 on2026-10-20. The L1 opened the three distinct canonical URLs (S015/S037 share one); quotes, versions, access dates and exact old→new used-by cells are in `corpus/lessons/round-15.md`. No new immutable scope justified a new row. New knowledge cites all four mined source rows.

Required command, executed at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Before output, exit **0**:

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

After output, exit **0**:

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

W04 is informational. Exact tabbed stdout and counts are retained in `.ufo/waves/round-15/sources-before.json` and `sources-after.json` (plus the final command receipt under `evidence/`). Counting code executed in Eval selected `^\|\s*S\d{3,}\s*\|`, split each table row into11 cells, counted tiers at cell3 and statuses at cell7; before text came from `git show 0fa5e0d:corpus/SOURCES.md`, after text from the delivered file. Reproduction from the lane root:

```python
import collections, json, re, subprocess
from pathlib import Path
for label, text in [('before', subprocess.check_output(['git','show','0fa5e0d:corpus/SOURCES.md'], text=True)), ('after', Path('corpus/SOURCES.md').read_text())]:
    r = [[c.strip() for c in s.split('|')[1:-1]] for s in text.splitlines() if re.match(r'^\|\s*S\d{3,}\s*\|', s)]
    print(label, len(r), dict(collections.Counter(x[3] for x in r)), dict(collections.Counter(x[7] for x in r)))
# before 38 {'A':35,'B':2,'C':1} {'mined':17,'queued':20,'rejected':1}
# after  38 {'A':35,'B':2,'C':1} {'mined':17,'queued':20,'rejected':1}
```

Rows38→38; rows added A0/B0/C0; status/recheck unchanged. Only S014/S015/S037/S038 used-by gains `corpus/knowledge/journal-positive-evidence-r15.md`, with every complete prior cell preserved and its transition logged. One new admitted knowledge entry advances **FR1 mixed-class failure-mode ground**, not kernel victim attribution, fleet correlation, deduplication or all-event coverage. FR11 cursor semantics and the reasoned drift re-pin remain unexecuted frontier/debt. Mistakes M1–M3 and the actual setup failure are learned alongside disclosed procedural mistakes M4–M6.

## Trend verdicts

- **expansion: improved** — one new sourced, measured knowledge entry on the previously disclosed FR1 failure-mode gap; the working partial-positive capability is in SCORECARD. Source-row volume is not the metric.
- **quality: improved** — the weaker aggregate-only alarm contract is superseded with finite red/green evidence, capture-failure refusal, explicit object guards and preserved alarm/routing controls. The old r10 red pin remains marked, not silently blessed.
- **discernment: improved** — prior outside provenance/wording findings became lesson-backed Q33–Q36, actual failing witnesses and clearer interface boundaries. This is learning from the prior non-author check, **not** a claim that our64 seats satisfy current outside admit/reject sampling. Current non-author sampling remains pending.

## SHONEN

- [~] Real decision tables, error patterns, checklist and cited sources — SKILL.md; new positive-evidence decision table; S014/S015/S037/S038; author assertion only.
- [~] End-to-end domain task executed and logged — LOG.md round-15 trigger→implementation→committed synthetic/live observation→report handoff; `evidence/live-census.json` and final paired manifests; no live positive OOM inferred.
- [~] Instructions executable without oral context — SKILL gate registry, committed expected/frozen inputs and all delivered command receipts above; author assertion only.
- [~] No cross-domain bleed / province still accurate — PROVINCE.md Core/Adjacent, preserved owner-routing fixtures and detection-only scope; author assertion only.

SHONEN.md itself remains the canonical four unchecked boxes. No promotion, independent verifier identity or `[x]` is self-assigned.

## Conformance, safety and operator handoff

- **Procedural conformance debt:** AttackProvenance admits an out-of-scope `agent://all` broadcast; RegistryFrontier records temporary source downloads under `/tmp` despite lane-only seat write scope; HarnessBuild ran isolated-wrapper selftests before the L1 barrier. These are disclosed violations, not retroactively called conformant. L1 issued exact-id coordination/stop-check corrections. The temporary downloads are not durable evidence; L1 separately reopened canonical URLs. Later committed-input L1 verification, not those midflight checks, grounds the claim. See lesson M4–M6 and retained seat reports.
- Final corpus self-review is **conformant at the bounded knowledge/source contract** (provenance trio, sourced claim, Gate/Mistakes, logged registry transitions, source validator exit0). Round execution is **not fully conformant** because of the procedural debt just named. Gate redness is separately status-neutral debt; no claim of a full-freshness pass.
- Stale-lane: respawn-per-round; this assigned mori round15 progressed through its own commits and report. No other mori mission is assigned/open in this L1's context; no driver state or runtime log was mutated.
- Tool installs/updates: **none** by L1 or reported by its seats. Existing versions recorded: Bash5.3.15, Python3.14.7, Node24.21.0, Git2.55.0; unqualified jq=jaq3.1.1, verification parser=/usr/bin/jq1.8.2. No pacman transaction. Initial host-safety amendment went to all64 exact ids; the later complete pacman pause went to the sole still-live implementation seat. No credential/auth file or agent database was opened, and no separate omp CLI was launched.
- Open L0 questions: **none newly added**; no operator decision blocks this delivered scope. Operator/orchestrator actions: independent closure must sample an admit and reject, adjudicate procedural debt/admission, and keep promotion and any semantic drift re-pin operator-owned. No next round was started.
