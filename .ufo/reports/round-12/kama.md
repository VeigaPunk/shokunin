# Kama round 12 — exact source correspondence, not digest self-consistency

## Work performed

Declared **C1 — calibration**, the lowest assigned axis (7 versus operability 8): make historical snapshot correspondence independently fail-capable and correct the earlier integrity-only overstatement. For one routed source path, the retained old snapshot has one source mismatch and the new corrective snapshot has zero. These are two snapshots, not an overwritten history or a newly discovered defect. Calibration stays **7 → 7, delta 0**. No capability acquisition, exploratory claim, runtime freshness or coverage expansion is asserted.

- **D1:** preserve the old truncated auxiliary SOURCES snapshot, introduce a byte-exact corrective snapshot and manifest, and compare against independently pinned git revision/path/OID/SHA-256/length. Evidence: `kama-shokunin/.ufo/waves/round-12/{fidelity.py,reproduce.py,frozen/expected.json}`; `corpus/lessons/round-12.md` §§Gate, Exact D1 erratum target; measured work `33f46685b418af868259952884e34b93633820cb`.
- **D1 learning:** append QUALITY KQ15 and an explicit LOG erratum: eleven internally consistent frozen digests never established source-commit correspondence. The outside round-11 closure had already found the defect; this round credits the fail-capable prevention and correction, not rediscovery. Evidence: `kama-shokunin/corpus/QUALITY.md:45-49`, `LOG.md:644-661`, lesson §Claim limit and prior-overlap credit.
- **D2–D4:** append source-opening-date/K02 navigation corrections, complete applicable QUALITY authority, and explicit S031 inference versus lane-registry supersession boundaries. Evidence: `kama-shokunin/corpus/SOURCES.md:66-70`, `SKILL.md:376-409`, `corpus/knowledge/served-identity-crosswalk.md:87-135`, lesson §Mistakes.
- **D5:** put a prominent historical/nonexecuted override before the undelivered round-10 protocol. L1 expressly authorized prepending this warning to a **non-corpus planning artifact**, preserving all original bytes as a suffix, rather than leaving a warning below the obsolete binding title. This is not a corpus/LOG append-only exception. Evidence: `kama-shokunin/.ufo/round-10/SEAT-PROTOCOL.md:1-31`, `LOG.md:663-670`. The final evidence commit corrects the new banner's chronology: D5 followed the original introduction commit.
- **Sourced claim:** L1 opened the official [Git git-show manual](https://git-scm.com/docs/git-show), DESCRIPTION and DISCUSSION, on 2026-10-20; S032 docs/A supports historical blob capture semantics, not the snapshot's outcome. Located quotes and access date are in the lesson's **Gate**. OllamaSource reopened S031's remote-field schema for D4. Evidence: `corpus/SOURCES.md:44,59,70`, lesson §§Gate, Opened source and sourced-claim binding; wave `advice/{GitSource,OllamaSource}.md`.
- **Swarm:** one validated **32-member** wave, one unchanged validator `taskCall` dispatched in one task call: **7 executor, 5 scout, 4 connector, 7 reviewer, 4 critic, 2 sentinel, 2 scribe, 1 revenger**. L1 holds the canonical planner seat; revenger PlannerWalk is a bounded data-walk advisor, not a bypassed planner role. No model parameter or route mutation. Evidence: `kama-shokunin/.ufo/waves/round-12/{spec,dispatch,record,spawn-result,wave-summary}.json` and `advice/`. The initially unsupported spec key was removed before successful validation; no refused wave was dispatched. Advisor mid-integration observations are not final-tree failures or outside verification.
- **Inheritance and scope:** initial lane working tree was clean at `79fa257719e8688692ed1dc443589331ba22b7fe`; no lane-authored leftovers to resolve. The committed non-author `round-11-verifier-spotcheck.md` was read fully and never changed. Every routed D1–D5 item is addressed above. Evidence: `inherited-state.json`, lesson §Work and scope. No endpoint/service/config/environment-value/credential probe, runtime restoration, schedule, provider substitution or sibling-tree mutation occurred. Tools installed/updated: **none**.
- **Cross-domain handoff:** protocol owner may consider the general observation that digest integrity misses capture-time corruption; kama enacts only a lane-local evidence gate, not a fleet protocol rule. Main retains the round-11 misrooted-advisor cleanup item; this lane neither deletes those fleet files nor claims cleanup ran. Evidence: round-11 verifier §Routed defects, wave `advice/ProvinceOverlap.md`, lesson §Advisor dispositions.

Stale-lane: respawn-per-round; no other kama mission is open. No new L0 question. Relevant standing operator-owned questions remain runtime restoration/permanent disposition (kama round-1 freshness addendum) and snapshot invocation cadence/timer (kama round 2); neither blocks this historical-evidence repair and neither is acted on here.

## Landed changes

**Pushed lane HEAD: `1df80eab01bc5663deea65680673fef24f35d5b0`.** Lane commits carry `kama-shokunin <kama@shokunin.local>`. Push completed before this report was written; the required final lane status was empty.

| Commit | Landed change | LOG binding |
|---|---|---|
| `33f46685b418af868259952884e34b93633820cb` | Fidelity gate, compact stdout-only reproduction runner, exact corrective snapshot/pin, wave dispatch/registry/advice, S032, KQ15, SCORECARD/lesson/index, D2–D5 clarification | `LOG.md:606-670` — motivation, individual routed changes, limits and explicit frozen-source erratum |
| `1df80eab01bc5663deea65680673fef24f35d5b0` | Committed-revision receipt, final source census, measured SCORECARD/lesson/LOG results, archive-banner chronology correction | `LOG.md:672-700` — actual commands/results, census, claim/trend disposition and correction |

Original round-11 frozen evidence and outside verifier files remain unchanged. No `[x]` SHONEN box, promotion, new serving capability or new knowledge entry is landed.

## Before → after measurements

Counting/reproduction command (actually run once from the fleet root):

```sh
python3 /home/vgpnk/Projects/shokunin/kama-shokunin/.ufo/waves/round-12/reproduce.py
```

Measured revision **`33f46685b418af868259952884e34b93633820cb`**, recorded before and after the run with unchanged HEAD. Complete stdout/stderr/exit and parsed receipt: `kama-shokunin/.ufo/waves/round-12/acceptance.json`. Overall **exit 0, ok true**, all seven records met literal expectations.

| C1 / control | Before / negative | Corrective / expected observation |
|---|---|---|
| Source correspondence, fixed one-path denominator | Old snapshot: `source_anchor_matches=true`, `source_matches=false`, source mismatch count **1**, exit **1** `source_mismatch` | New snapshot: anchor true, source match true, count **0**, exit **0** `clean`; independently verified integrity pin |
| Independent authority | Source revision `2f7303c242319c1dc96c6bcf7702ac18b3ca1aad`, path `corpus/SOURCES.md`; old SHA-256 `52665cf2d648112be2683c61485d42da1bf1dc859ea1df41d857672c60142fa1` | Source/new SHA-256 `9dc40d25a595b3d42b39649e17094cfa4e7190cfbf340331252dd29dea22093a`; OID `7de1360655eadada356fe110813c6e1338142551`, 18,898 bytes; all independent checks true |
| Self-invocation | Isolated temporary snapshot/manifest fixtures, read-only immutable-source access | **11 passed / 0 failed**, exit 0; actual child CLI exit/finding assertions |
| Coherent snapshot + manifest mutation | Changed snapshot with matching changed pin | Exit **1** `source_mismatch`, source count 1; manifest cannot substitute its own source authority |
| Manifest-only corruption | Pristine source bytes, wrong integrity pin | Exit **2** `snapshot_tampered`, **source count 0** — pin failure is not source mismatch |
| Source-manifest redirect | Redirect to the committed old truncated copy | Exit **2** `manifest_invalid`, never clean |
| Missing source | Temporary empty git repository | Exit **2** `source_unavailable`, not a successful comparison |

The new copy's match is a construction check; the prevention is demonstrated by the same command failing for the known bad copy and independent controls. Original mismatch evidence is intentionally retained. A forged git-object/source-anchor failure is a static guard, **not** an exercised additional attack. Gate/code/frozen bytes did not change after measurement; the final commit adds receipts/prose and the banner chronology correction only.

| Axis | Author verdict | Scope |
|---|---|---|
| calibration | **improved**, score 7 → 7, delta 0 | Separately source-anchored, fail-capable evidence plus precise integrity-only erratum; no universal mastery-score conversion |
| operability | unchanged | Existing serving tools/consumer pins unmodified; no serving probe or restoration |
| freshness | unchanged | No live endpoint revalidation; exact history is not current runtime truth |
| coverage | unchanged | No new admitted knowledge or covered ground |
| depth | unchanged | No separate domain-depth claim |
| adjacency | unchanged | Protocol, host/service, routing, credentials and cleanup stay with their owners |

All author measurements verify; no axis harm observed within this bounded scope. **Independent non-author round-12 admit/reject sampling remains required for admission.** Author-dispatched agreement is not that closure.

## Sources & frontier

Required validation command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

**Before output, exit 0:**

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

**After output, exit 0:**

```text
kama W04 S031 duplicate url docs.ollama.com/api/tags across scopes
kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

Counting command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama
```

Both counting invocations exited **0**. Full streams: `kama-shokunin/.ufo/waves/round-12/{sources-before,sources-final}.json`.

| Census | Before → after |
|---|---|
| rows | **31 → 32** |
| tiers | A **28 → 29**, B 0 → 0, C 3 → 3 |
| statuses | mined **21 → 22**, queued 5 → 5, rejected 5 → 5 |
| invalid tiers/statuses; missing registries | 0 → 0 |

- Added by tier: **A +1 (S032 docs), B +0, C +0**. Opened URL/date and ≤25-word located quotes are in lesson **Gate**. S032's scope is capture method, not endpoint truth or independent proof of the measured outcome.
- Rows touched old → new: **S032 absent → mined**, opened 2026-10-20, recheck on-release, used-by `corpus/lessons/round-12.md`. **S001–S031 status/recheck/used-by unchanged.** S031 was reopened for field/inference clarification, not counted as a new independent source. W04 is the existing scoped same-URL supersession, not a waived error.
- Frontier rows advanced: **0**; K02 already held, K05 still operator-runtime dependent. New admitted knowledge entries: **0**. Registry row growth is not expansion.
- Mined mistake: D1 capture-time truncation hidden by a self-consistent digest; KQ14 → grounded KQ15 and observed red-before/green-after/coherent-mutation evidence. D2–D5 are separately mapped clarifications, not four extra measured claims. Evidence: lesson §§Mistakes, Measured author disposition; `LOG.md:644-661`.

## Trend verdicts

- **expansion — unchanged:** zero new covered ground/knowledge entries/capabilities; S032 is research-method support for historical-evidence repair, not serving-domain expansion.
- **quality — improved:** new corrective evidence is independently source-anchored and integrity-pinned, the same CLI rejects known-corrupt/coherently changed captures, and D1–D5 overstatement/navigation/inference/archival limits are explicit. Evidence: receipt, KQ15, LOG erratum, lesson §Advisor dispositions.
- **discernment — unchanged:** outside round-11 feedback is learned in KQ15, but this round's author gate decisions still await independent admit/reject sampling. No author advisor is presented as a non-author reviewer.

## SHONEN

- [~] Decision tables, error patterns, checklists and cited sources: `kama-shokunin/SKILL.md` §§Decision table, Historical error signatures, Checklist; round-12 complete-criteria correction and gate registry. Author assertion; no new named non-author certification.
- [~] End-to-end domain task executed and logged: historical `kama-shokunin/LOG.md` rounds 1–3 record endpoint reconciliation/invocation history; round 12 is historical-evidence repair, not a fresh serving execution.
- [~] Instructions executable without oral context: `kama-shokunin/SKILL.md:388-409`, committed scripts/manifest and actual `acceptance.json`; independent promotion execution review remains separate.
- [~] No cross-domain bleed: `kama-shokunin/PROVINCE.md`, lesson §Work and scope, this report's handoffs; host mutation, routing, secrets and fleet protocol governance remain excluded. No `[x]` mark is claimed.
