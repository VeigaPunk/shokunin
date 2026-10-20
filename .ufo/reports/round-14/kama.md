# Kama — round 14 (attempt 1)

## Work performed

**Declared C1 — calibration capability: `ollama-offline-evidence-replay`.** Calibration 7 is the lowest assigned axis, versus operability 8 (`shokunin.conf` kama row; lane `SCORECARD.md` §Round 14). Before: no executable offline Ollama tags/ps capture reconciler. After: 51/51 separately authored fixed adversarial cases match exact CLI exits/findings and schema/readiness/scope invariants. Numeric calibration remains **7 → 7, delta 0**. This is substantive new runnable repertoire, not another wording-only claim or a claim that the already-held available/running/remote distinction is new. No stagnation waiver or exploratory claim.

- Implemented a read-only stdlib CLI with exact name/digest selection, explicit unknown/remote/invalid evidence, strict conflict precedence and child-CLI selftest. Every classification reports `readiness: unknown` and `scope: offline-captures-not-runtime`. Evidence: lane `tools/kama-ollama-evidence.py`, `tests/ollama-evidence/cases.json`, `SKILL.md` §Round-14 registry; work commit `e545ed99aaa519196a2a7779b0a293b2ce4c765c`.
- Added a source-grounded operational workflow and KQ17; reopened S012/S031 official documentation, distinguishing vendor fields from the lane's **[INFERENCE]** join/precedence policy. Evidence: `corpus/knowledge/ollama-evidence-replay.md`, `corpus/QUALITY.md:63–72`, `corpus/lessons/round-14.md` §Gate; same work commit.
- Integrated two actual same-round code mistakes found by L1 static review: remote markers preempted missing selected digests, and no-tags return preempted duplicate ps selection. Preserved the actual draft; isolated a causal red control changing only `classify()` back to its draft body. Both reproduce exactly two failures, fixed by final ordering. Evidence: lane `.ufo/waves/round-14/{rulings.json,acceptance.json,frozen/precedence-before.py,frozen/precedence-only-red-manifest.json}`.
- Addressed all prior outside-review routed items without touching non-author/history files: round-13 D1 already resolved; D2 now has an appended named clarification of round-12's verified-anchor mismatch count **1** versus outer `manifest_invalid` / exit **2**. Optional independent-calculation phrasing is bounded as separate-command/same-object-store evidence, never external provenance authority. D2 earns no C1/axis/trend credit; outside closure determines disposition. Evidence: `corpus/lessons/round-13-verifier-spotcheck.md` §Routed defects; new `corpus/lessons/round-14.md` §Named historical clarification; `QUALITY.md` KQ17.
- Dispatched one validated **32-seat wave** in exactly one unchanged `taskCall`, without a model parameter. Role mix: executor6, revenger2, scout5, connector3, reviewer7, critic4, sentinel2, scribe2, simplifier1. L1 holds the canonical planner seat; PlannerWalk is bounded revenger data-walk, not an invalid planner role. One scout, ExistingProbe, died with `Cursor RESOURCE_EXHAUSTED`; no replacement/extra wave. Its bounded normalization recon was covered by existing SKILL/crosswalk and final no-normalization controls. Evidence: lane `.ufo/waves/round-14/{spec.json,dispatch.json,validation.json,assignments.json,spawn-result.json,record.json,integration-review.json}` and `advice/`.

Stale-lane: respawn-per-round; no other mission of kama is open. Initial tree clean at `e1b3d746dbfd2100b61c67b6389217252592460f`; no inherited author leftovers. Prior verifier artifacts are untouched. Tools installed/updated: **none**. New L0 questions: **none**. No current endpoint, live Ollama integration, service restoration, local-weight proof, generation, routing, credential or operator-config action is claimed. Cross-domain boundaries: credentials/auth → kagi; routing/alias traversal → kumitate; model quality → kengaku; service/config changes → operator.

## Landed changes

**Pushed lane HEAD: `06cc6dbea42b88849fb1808d40ae38a08dced21c`.** Lane was clean after that push, before this report was written. Both round commits use `kama-shokunin <kama@shokunin.local>` and pathspec-limited staging.

| Commit | Landed work | LOG binding |
|---|---|---|
| `e545ed99aaa519196a2a7779b0a293b2ce4c765c` | Classifier, literal fixture corpus, measurement runner, workflow, KQ17, source used-by links, SKILL registry, corpus navigation, claim/ruling/validated wave evidence and actual draft snapshot | lane `LOG.md` §round 14 — executable offline Ollama evidence reconciliation |
| `06cc6dbea42b88849fb1808d40ae38a08dced21c` | Actual acceptance receipt, isolated causal red artifact/manifest, preservation checks, final census, demonstrated capability row and measured lesson/scorecard/LOG disposition | lane `LOG.md` §round 14 — committed measurement and capability admission by author |

No historical lesson/receipt/verifier, old serving tool, tracked registry, PROVINCE or SHONEN bytes changed. Direct Git-object comparisons in `.ufo/waves/round-14/preservation.json` found all **25 protected tracked files** equal, all five active instruction/ledger prefixes preserved, and source immutable cells unchanged. Ignored history files are not inferred from git. No old serving/fidelity/sibling gate was executed.

## Before → after measurements

Measured implementation revision: **`e545ed99aaa519196a2a7779b0a293b2ce4c765c`**, pushed before measurement. The final receipt/docs commit does not alter the measured tool or cases. Complete command argv/cwd/stdout/stderr/real exits and parsed outputs: lane `.ufo/waves/round-14/acceptance.json`, **ok true**, errors `[]`.

Counting command, from `/home/vgpnk/Projects/shokunin/kama-shokunin`:

```sh
python3 .ufo/waves/round-14/measure.py --tool PATH
```

| C1 measurement | PATH / command | Exit | Observed |
|---|---|---:|---|
| Before capability | `.ufo/waves/round-14/frozen/before/tools/kama-ollama-evidence.py` (absent) | 1 | **0/51 supported**, all records unsupported; no child fallback |
| After capability | `tools/kama-ollama-evidence.py` (also runner default) | 0 | **51/51 literal matches**, 0 failed |
| Actual current-round draft mistake | `.ufo/waves/round-14/frozen/precedence-before.py` | 1 | 49/51, two named failed findings |
| Causal red control | `.ufo/waves/round-14/frozen/precedence-only-red.py` | 1 | 49/51, exactly the same two failed findings, only `classify()` restored |
| Child-CLI selftest | `python3 tools/kama-ollama-evidence.py --selftest` | 0 | `clean`, 51 passed / 0 failed |

The retrospective absent-tool baseline is grounded by actual immutable start-tree `git ls-tree e1b3d746dbfd2100b61c67b6389217252592460f -- tools/kama-ollama-evidence.py`: exit0, empty output (`before-capability.json`). It is **new capability absence**, not a false claim of old classifier misbehavior.

All harness observations use identical cases SHA-256 `4a4de0b85009c42804e43c8ae8833bd6f0673edc71ae5ec8baa1e3201e158ae4`. Expected findings: loaded10, available3, unknown10, conflict5, remote5, invalid18; a constant-answer tool could match at most18/51. The two actual red controls are `remote_missing_digest` (unknown2 expected, remote_inventory1 observed) and `tags_none_ps_duplicates` (invalid_input2 expected, unknown2 observed). Final matches both; equal numeric exit alone is insufficient. Harness/selftest each assert exit, stable finding, schema, reported exit, readiness and scope. They share one separately authored same-round oracle, **not independent external corroboration**.

**Per-axis verdicts:** calibration **improved**, score7→7; operability, freshness, depth, coverage and adjacency **unchanged**. No observed axis harm within this finite offline scope. Capability row added only after demonstration; no universal correctness or actual serving-readiness guarantee. Author claim verifies; **independent non-author admission remains pending**.

## Sources & frontier

C1 is sourced by **S012/S031**, both reopened by L1 and source seats on 2026-10-20: <https://docs.ollama.com/api/ps> and <https://docs.ollama.com/api/tags>, OpenAPI3.1.0/info.version0.1.0. Located quotes (≤25 words) and source/inference distinctions are recorded in lane `corpus/lessons/round-14.md` §Gate and `advice/Sources.md`.

Required command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

Before output, exit **0**:

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

After output, exit **0**:

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

Counting command: same CLI with `census` instead of `validate`; both exit0, full streams in lane `.ufo/waves/round-14/sources-{before,final}-{validate,census}.json`.

| Census | Before → after |
|---|---|
| rows | 33 → 33 |
| A / B / C | 30 / 0 / 3 → 30 / 0 / 3 |
| mined / queued / rejected | 23 / 5 / 5 → 23 / 5 / 5 |
| invalid tier / status; missing | 0 / 0; 0 → 0 / 0; 0 |

Rows added by tier: A0/B0/C0. Allowed old→new touches: S012 used-by `[runtime-health-surface-matrix.md, served-identity-crosswalk.md]` → same paths plus `corpus/knowledge/ollama-evidence-replay.md`; S031 used-by `[served-identity-crosswalk.md]` → same path plus replay. Exact full repo-relative strings are in lesson §Source curation. No status/recheck/immutable-cell changes or new row. W04 is existing scoped same-URL curation, not independent support. Search: two URLs identified/screened/reopened, zero new rows/excluded; stop when needed fields and limits located.

Frontier advanced: **executable offline replay repertoire**, not new API concepts or live integration. Prior conceptual crosswalk receives explicit credit. Mistakes mined: outside D2 historical count presentation, initial policy-order ambiguity, and actual same-round implementation precedence drift; the last is demonstrated fail-capable by preserved draft and isolated causal red results. Runtime/context-capacity frontier remains operator-dependent.

## Trend verdicts

- **Expansion: improved.** One demonstrated capability enters SCORECARD, with sourced operational workflow/coverage-map row. Credit is executable repertoire, not source-row growth or rediscovery of tags/ps concepts.
- **Quality: unchanged.** No existing serving-knowledge entry is revalidated/deepened/superseded and no runtime is sampled. New operational documentation and gate correctness are not double-counted as refreshed serving truth.
- **Discernment: unchanged.** Current design mistakes ground KQ17 and demonstrable rejection controls; D2 receives historical clarification without new credit. All 32-seat advice is author-side. Outside round-14 admit/reject sampling is still required; no promotion or self-admission.

Orchestrator action: arrange independent non-author closure/admit–reject sampling against committed evidence; do not run sibling gates. No new operator decision or L0 append is needed. Existing runtime-restoration/context-capacity prerequisites are not silently removed.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources — lane `SKILL.md` existing domain sections plus round-14 registry and `corpus/knowledge/ollama-evidence-replay.md`; author assertion, no new named non-author certification.
- [~] End-to-end domain task executed/logged — historical endpoint work remains dated; this round executes offline replay through actual CLI and records results in `LOG.md`/`acceptance.json`, not fresh serving integration.
- [~] Instructions executable without oral context — literal workflow, fixed fixtures, selftest, exit/scope tables and measured commands; author assertion pending independent review.
- [~] No cross-domain bleed / PROVINCE accurate — lane `PROVINCE.md` unchanged; no credentials, route/alias traversal, quality evaluation, remote web or host-service mutation absorbed. No `[x]` promotion box written.
