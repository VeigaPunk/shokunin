# Kake — round 23

## Work performed

Declared claims, frozen before implementation in lane `.ufo/waves/round-23/contract.json`:

- **C1 — freshness:** re-verify the 16 historical knowledge entries and SKILL property map, with dated claim-level observations, HOLD/STALE/UNVERIFIABLE dispositions and appended corrections: **0/17 → 17/17 valid unit receipts**. Freshness is a tied-lowest owned axis. Evidence: `SCORECARD.md:314`, `receipts/`, `recovery-counts.json`, `recovery-final-counts.json` under the round-23 wave directory.
- **C2 — operability/capability:** execute GET-only capture and reproducible offline canonical preflight over the 12 frozen owned surfaces: **0/12 → 12/12 complete receipts**, not twelve clean sites. Evidence: `scripts/live_snapshot.py`, round-23 `c2-population.json`, `live/`, `recovery-final-counts.json`; repertoire row `SCORECARD.md:193`.

Both claims are **locally verified, bounded improvements**, with ratings HOLD 10→10. Independent admission and the outside admit/reject spot-check remain the separate closure review's responsibility. C1 and C2 use disjoint receipts and independent counters; neither requires the other's numerator. No new round was claimed or dispatched.

- C1 records **176 selected claims: 79 HOLD, 55 STALE with corrections, 42 UNVERIFIABLE with reasons**. A receipt's accepted structure does not authenticate its GET/HOLD assertion; producer/seat observations and outside review carry that authority. Historical bytes and original dates are not relabelled as live. Evidence: `measure_c1.py`, `receipts/`, `recovery-audits.json`, lesson §Measurement and recovery errata.
- C2's outcomes are **3 clean, 5 failed-policy with finding `canonical_missing`, 4 not-served (404)**. Clean: ds4cc primary, plazir15 GHP, charter GHP. Missing canonical under explicit local policy: ds4cc Kimi, burnerchrome Kimi, vault index, ufo-fsd Kimi pro, lucario GHP. Not-served: plazir27 Kimi, lucario Kimi, plazir15 Kimi, charter Kimi. Evidence: `live-summary.json`, `live/*/audit.json`, `recovery-final-counts.json`.
- End-to-end domain task: capture the named public surfaces read-only → retain response metadata and served bytes → run canonical policy → replay receipts → hand off the named source/deployment findings here. Actual repair/publication remains operator-owned. Evidence: `LOG.md:784`, `corpus/knowledge/static-canonical-preflight.md` §Live snapshot handoff, `live/`.
- Made real body-only SVG/MathML and self-closed void markup evaluable without accepting body bases or unsupported foreign parsing. Added targeted guards and falsification witnesses, including foreign end-tag mismatch. These are C2 implementation details, not a third claim. Evidence: `scripts/canonical_audit.py`, `relaxation_probe.py`, `postfix/relaxation-v2-cand.json`, recovery verification.
- Hardened stored-response/output handling and redirect-chain consistency. RecoveryDocsAudit found a surviving non-string contentType crash; the same expanded loopback probe was red **11/12, exit 1**, then green **12/12, exit 0**, with the named field now producing JSON input error exit 2. This final narrow repair was coordinator-implemented after two zero-spawn job-cap refusals and Main's explicit direct-implementation steer. Evidence: `snapshot-field-before.json`, `snapshot-field-after.json`, `recovery-dispatch.json`.
- Addressed the round-22 verifier's inverted QUALITY predicate, misplaced report copies and temporary-runner reproducibility; retained the old paths red and independent-promotion limits. Evidence: `corpus/lessons/round-22-verifier-spotcheck.md`, round-23 lesson §Routed, `.ufo/waves/round-22/postfix/REPRODUCE.md`.
- RecoveryDocsAudit identified in-place corrections to committed round-23 lesson count/source lines. Restored the original lines and appended an authoritative erratum with correct count, digest pairing and quote locator; this does not erase the intermediate preservation defect. The older FixDocsEvidence recommendation remains historical. Evidence: lesson §Recovery audit errata, `recovery-audits.json`.
- Cross-domain boundary: rendering/browser state stays tabi's province; credential/account custody stays kagi's; publishing and source restoration remain operator-owned. A surviving burnerchrome source candidate was read only, and its title/h1 match is not a deployment binding. Evidence: `PROVINCE.md` §Round-23 live use; `receipts/property-map.json`.

### Inherited work, waves and failures

This replacement coordinator inherited the already-pushed implementation through measured revision `5bef55b1464d7ccbff802edab400d138597a621c`, modified LOG/SCORECARD/lesson tails and untracked final/wave-2 evidence. Reused all implementation/evidence after the recorded recovery checks; rejected interpretations remain preserved in the Gate, not credited as success. No inherited artifact was silently discarded, no wave was redone, and no protected aggregator/verifier file was edited. The report did not exist at takeover. Evidence: `recovery-counts.json`, `recovery-verification.json`, `recovery-audits.json`; lesson §Same-claim recovery.

| Dispatch | Seats | Role mix | Returned / dead |
|---|---:|---|---|
| Validated build w1 | 69 | reviewer33, scout19, connector5, critic2, mutation-tester2, sentinel1, simplifier1, scribe3, executor3 | 69 / 0 |
| Validated falsify w2 | 64 | reviewer42, scout14, mutation-tester2, sentinel1, critic3, connector1, executor1 | 25 / 39 |
| Original residual checks of new fixes | 6 | reviewer5, critic1 | 4 / 2 |
| Read-only recovery audits | 3 | reviewer2, scout1 | 3 / 0 |
| **Actual round total** | **142** | L1 holds the planner seat; no planner swarm role | **101 / 41** |

Both full waves retain policy-v2 specs, rendered dispatches and populated registries under lane `.ufo/waves/round-23/{w1,w2}*`; the same validated batch was retried rather than split. w1 records seven cap refusals before the eighth try; w2 one before the second. The two later repair-seat refusals spawned nothing and are not deaths or seats. `wave-inventory.json`, `recovery-dispatch.json` and `recovery-audits.json` carry the accounting. Recovery found and byte-preservingly renamed `w2/ExecGeneratorPages.md` to the registered `w2/ExecRealGeneratorPages.md`.

Dead seats, never replaced or credited:

```text
HoldFireJournalCodes, StaleFreeReadVerbs, StaleGhpSubpathSpotcheck,
HoldGhpSubpathSpotcheck, StaleKeeperTimerInert, HoldKeeperTimerInert,
HoldKimiSubpathAudit, StaleMirrorPitfalls, HoldMirrorPitfalls,
StaleOpsAutomation, StaleOriginRepos, HoldOriginRepos,
StaleProbeDeltaAlerting, HoldProbeDeltaAlerting, StalePublishChannels,
HoldPublishChannels, StalePublishQueue, HoldPublishQueue,
HoldSitemapOrphanAudit, StaleSpeedrunPipeline, HoldSpeedrunPipeline,
StaleVaultProperties, HoldPropertyMap, RecheckPlazir15Ghp,
RecheckDs4ccKimi, RecheckBurnerchromeKimi, RecheckVaultIndexKimi,
RecheckLucarioGhp, RecheckPlazir15Kimi, RecheckCharterKimi,
AttackForeignStack, AttackControlChars, AttackDuplicatePages,
ReopenS031, ReviewKnowledgeDelta, ConnectR23Axes,
AttackBaseGuard, RecheckCharterGhp, ReviewUpstreamFixes;
residual: CritMetaRefreshBoundary, FixCounterCoverage.
```

The first 36 above record `[zai/glm-5.3-flash] Retry budget exhausted after 5 retries: 429 Rate limit reached for requests` and `Rate limit reached for requests (type=1302)`. AttackBaseGuard records `[openai-codex/gpt-6-luna] Retry budget exhausted after 13 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`. RecheckCharterGhp, ReviewUpstreamFixes and both residual deaths have that same Codex message after **5** retries. Exact identities/messages: `w2-deaths.json`, `residual-deaths.json`; the latter preserves original host async notices recovered by RecoveryEvidenceAudit. Configured routing is not availability evidence. Dead attack coverage remains incomplete.

Tool use/install record: no global package or tool was installed by either coordinator. ExecRealGeneratorPages resolved **Eleventy @11ty/eleventy 3.1.2**, official npm registry via **npx**, to exercise an actual two-page generator build; no pacman or global install. Evidence: `w2/ExecRealGeneratorPages.md:12-22`. No host service or package transaction was performed.

## Landed changes

Lane final HEAD: **`f7de3ab4e9f030a15a857a5a08631bd8e690f436`**, committed/pushed by the lane helper. Final code/recovery landing: **`dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1`**. These are the helper's observed `landed` hashes; the earlier revisions below identify measurements/history, not a replacement for push proof.

| Landed work | LOG link | Commit carrying the integrated round chain |
|---|---|---|
| C1 current-surface receipts and appended stale corrections | `LOG.md:784-790` | dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1 |
| C2 GET capture, canonical parser guards, snapshots, replay and repertoire | `LOG.md:787-791` | dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1 |
| Source rows S030/S031, quality learning, routed round-22 corrections | `LOG.md:789-793` | dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1 |
| Original wave-2/residual evidence, death records and recovery audits | `LOG.md:796-817` | dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1; final accounting f7de3ab4e9f030a15a857a5a08631bd8e690f436 |
| Append-only errata, precise registry boundary, contentType regression repair | `LOG.md:819-831` | dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1 |
| Committed-tip counters and final audit/pointer clarifications | `LOG.md:833-837`, `SCORECARD.md:368` | f7de3ab4e9f030a15a857a5a08631bd8e690f436 |

No domain source tree was edited, committed or pushed. Only the lane remote and this fleet report's remote are in landing scope.

## Before → after measurements

Run from `/home/vgpnk/Projects/shokunin/kake-shokunin`:

```sh
python3 .ufo/waves/round-23/measure_c1.py --root . --revision <commit>
python3 .ufo/waves/round-23/measure_c2.py --root . --revision <commit>
```

| Claim | Before: frozen contract/populations `6847479d404d1dd93ecb59f99ff735bd7f010a4a` | After: committed recovery `dd58390d3a0b2942ffdd8f0330c0da3dda7b87e1` | Verdict |
|---|---|---|---|
| C1 freshness | accepted0/17, exit1, receipts absent | accepted17/17, exit0; HOLD79/STALE55/UNVERIFIABLE42 | improved, bounded; score10→10 |
| C2 operability | accepted0/12, exit1, capture/audit receipts absent | accepted12/12, exit0; clean3/failed-policy5/not-served4 | improved capability; score10→10 |

Same final runner bytes on both sides: C1 `c217d276…`, C2 `91134d27…`; frozen populations unchanged. Full commands/stdout/stderr/exits: `recovery-counts.json` (before and inherited measured after), `recovery-final-counts.json` (committed recovery after). The inherited `measure-{c1,c2}-{before,after}-v2.json` retain two identical runs apiece at the earlier measured revision `5bef55b1…`. Counters do not authenticate the originating network event. No original timestamp was renewed by offline replay.

Exercised verification, not inferred:

- Recovery verification at the inherited implementation: canonical selftest82/82, counter selftest28/28, relaxation13/13, snapshot11/11, corpus-contract exit0, previous 32-case canonical matrix32/32. Every command exited0; full outputs in `recovery-verification.json`.
- Final contentType-only repair: same expanded snapshot probe **11/12 exit1 → 12/12 exit0**, including exact JSON-error assertion. `snapshot-field-{before,after}.json`; producer digest in after receipt. No exhaustive malformed-record proof is claimed.
- Inherited fail-capable evidence: rejected parser candidate3/13→final13/13; snapshot integrity2/11→11/11; initial counter selftest mutation probe killed13/71, leaving58 survivors before expanded regressions. No exhaustive mutation-kill credit. `postfix/`, `w2/MutateCounterSelftest.md`.
- **Known red retained:** `final-suite.json`, measured at `1b309c93fb0b2007ef15587100e7a1cdb9ef5573`, has paths exit1: three legacy unannotated targets plus **14 newly cited absent targets**; measured missSet55→69, persisted pin remains55. The new warning is not called unchanged/clean or hidden by re-pinning. Those new paths are explicitly checked/annotated absent; restoring/retiring external source trees remains operator-owned. This known failure was not rerun merely to confirm it.
- The current-validator 32-case matrix is not the digest-pinned historical round-22 replay. The latter intentionally requires its historical validator; `SKILL.md` records how to reproduce it. `stable-smoke.txt` includes an intermediate counter record; final authority is `counter-selftest-final.json`, not its first line.

No regression was observed on the exercised original policy population or valid-capture controls. This is not a whole-corpus-clean claim: expanded paths warnings, missing substrates and dead-seat coverage remain disclosed for closure.

## Sources & frontier

Census command, executed at original round start and final/recovery census:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Before (`census-before.txt`):

```text
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit: 0
```

After (`census-after.txt`; independently re-executed in `recovery-frontier.json`):

```text
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit: 0
```

Registry **29→31 rows**: tier A27→29, C2→2; status mined25→27, queued2→2, rejected2→2. Added S030/S031, both scoped tier-A WHATWG primary text; no old status/recheck/used-by cell changed. Exact reproducible counting command and outputs at base `b5d599e1…` and measured revision `5bef55b1…` are in `recovery-source-counts.json`; equivalent pasteable command (supply either full revision):

```sh
python3 -c 'import collections,json,subprocess,sys; text=subprocess.check_output(["git","show",sys.argv[1]+":corpus/SOURCES.md"],text=True); rows=[[c.strip() for c in s.split("|")[1:-1]] for s in text.splitlines() if s.startswith("| S") and s.split("|")[1].strip()[1:].isdigit()]; print(json.dumps({"rows":len(rows),"tiers":dict(collections.Counter(r[3] for r in rows)),"statuses":dict(collections.Counter(r[7] for r in rows))},sort_keys=True))' <revision>
```

S030 syntax/start-tags and S031 parsing/in-body/foreign-content were opened by seats, the original coordinator, the recovery coordinator and RecoveryClaimAudit. Their short located quotes/access date are in the lesson's Gate; its authoritative recovery erratum corrects the original cross-assigned digest/quote-locator record without deleting the original bytes. S021/S023–S026 were reopened without changing rows. Source support enters C2 through `corpus/knowledge/static-canonical-preflight.md`, citing S030/S031; no rejected source row was removed.

Frontier advanced: the formerly offline static-canonical capability now operates on captured owned-property responses, with explicit receipt completeness versus policy outcome boundaries. Rendering, search-engine selected canonical, publication readiness, source restoration and account operations remain open/outside this claim. Evidence: `PROVINCE.md` round-23 addition, `corpus/README.md` round-23 coverage, repertoire row.

Mined mistakes: parser relaxation without adversarial neighbouring regions; all-UNVERIFIABLE false coverage; inverted criterion; in-place corpus correction; array-only metadata regression missed the contentType branch. The lesson's `## Mistakes` and appended recovery table name evidence, captured-by and fix. Red-before witnesses are retained; author-side learning is not outside discernment. Final fleet misroot command `git -C /home/vgpnk/Projects/shokunin status --porcelain` produced empty output, exit0 (`recovery-final-misroot.json`); no fleet file was copied/deleted. The earlier sweep's unrelated operator files/runtime were left alone.

## Trend verdicts

- **expansion: improved** — demonstrated GET-capture/canonical-replay capability entered the repertoire (first-working round23); source-backed static-canonical frontier is now used on actual owned responses. Evidence: `SCORECARD.md:193`, `live/`, committed-tip C2 count.
- **quality: improved, bounded** — stale selected claims receive explicit corrections/unverifiable reasons; parser base/foreign guards and snapshot integrity/field-shape defects have red-before witnesses and passing controls. Existing corpus/path debt is not erased or rounded up to clean. Evidence: lesson Gate/Mistakes/errata, `snapshot-field-*.json`, `recovery-verification.json`.
- **discernment: unchanged** — author-side reviewers found useful mistakes, but none is the independent non-author admit/reject spot-check. Earlier scorecard language “improved locally” is explicitly superseded for this canonical trend. Evidence: `SCORECARD.md` recovery clarification, `recovery-audits.json`; separate closure pending.

## SHONEN

- [~] Decision tables, error patterns, checklist and sourced boundaries: `SKILL.md`, `corpus/knowledge/static-canonical-preflight.md`; author-side assertion, not a named non-author check.
- [~] End-to-end domain preparation/verification/handoff executed: `LOG.md:787`, twelve named capture/audit receipts and findings above; independent verifier still required.
- [~] Executable instructions for the current capture/offline workflow: knowledge §Live snapshot handoff and SKILL registry; historical missing-source recipes remain explicitly bounded, not asserted executable.
- [~] No cross-domain bleed in exercised work: `PROVINCE.md` Core/Frontier/Adjacent and round-23 live-use boundary; publication, accounts, browser execution and domain pushes remain outside the lane.

SHONEN.md itself stays unpromoted and unchecked; no self-dispatched seat grants promotion.

Stale-lane: same claimed round resumed under the respawn-per-round contract; no other mission of this lane is open. No round24 was started. Open L0 questions: no new question; inherited restore-or-retire/publishing decisions remain operator-owned. Independent closure is pending, not a new L0 blocker.
