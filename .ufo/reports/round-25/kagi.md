# kagi — round 25

BASE `4587c61a348e4528717404a68912c373f3ef4d03` (r24 admitted). Final pushed lane tip **`1bf3eec48d3761580ffd375c88143232485ae814`**; measured code/data revision **`9b755f5b44ace949fc4d71c9d6d8f125a560e9cf`**. The final commit adds measurement receipts and outcome metadata/pins; no runtime code changes follow the measured revision. Claim already held, attempt1; no dispatch/claim or next round started. Lane initially clean; no inherited uncommitted work.

## Work performed

Declared claims: **C1 calibration** — bind reviewed current-tense numeric self-descriptions to their source (routed SKILL.md:46 debt); **C2 operability** — make lone-clone citation/verify limits explicit without a false CLEAN (routed R11-08 debt); **C3 freshness/capability** — bind and observe every registry `on-release` clock, sourced by newly opened S033–S037, with S038 rejected. All six scalar axes remain9; all tie lowest, no stagnation waiver or retirement. The L1 held the frozen planner seat; bounded planning data walks rode scouts/reviewers/revengers/connectors.

- C1: `kagi-shokunin/corpus/self-counts.py` and `.tsv`, ledger R25-01/R25-02. **38 reviewed bindings**, not exhaustive digit/corpus completeness. Live `ledger:` sources execute non-host checks; `expect:` reads a committed pin without execution and reports `pinned=`, not `live=`. SKILL.md:46 now states **88 stamps +65 claims**, reflecting this round's added members (BASE truth was83/61, not63/39). Also corrected the97-case instructions and index counts. Evidence: `kagi-shokunin/.ufo/waves/round-25/final-verification.json`, `corpus/lessons/round-25.md` M25-1/R25-C5/C6.
- C2: no `[fleet]` tag or row skip landed. `citations` still runs; self-references resolve in-tree; fleet-only misses are `FLEET-ABSENT`, final `INCOMPLETE` exit3. Verify names `LAYOUT-INCOMPLETE R11-08` and ends `INCOMPLETE` exit1, never CLEAN. Local/self/nested lane-owned defects remain UNRESOLVED. Fixed the dropped last-token-per-line bug. Fresh falsifiers also tightened nested ownership and diagnostic classification. Evidence: `corpus/claim-ledger.sh`, R11-08/R11-09/R18-03, `falsify/FOwnUfo.md`, `FIncompleteReceipt.md`, `FEol.md` under the wave directory.
- C3: `corpus/release-clock.py`, `.tsv`, R25-03/R25-04. **28 clocks:18 feed,10 declared-quote**;15 derived anchors explicitly counted. Observations agree with a byte-pinned retained receipt; a contradicted TSV observation fails. S012 fired against its already-stale Vault version anchor and its teaching was re-verified. Observation is on-demand and dated, not continuous freshness or provider attestation. Evidence: `observe-1.json`, `falsify/FSeparability.md`, `FQuoteIntegrity.md`, repaired receipt gate.
- Frontier/learning: six new source rows, a registered empty-feed rejection, release-clock study path, QUALITY QM21–QM23 and M25-1..M25-5. New demonstrated capability enters the main SCORECARD capabilities table. Sources and teaching limits are explicit in `corpus/lessons/round-25.md`; no new host/vault surface acquired.

## Landed changes

Every production change belongs to LOG.md §Round25 and its fresh-falsification/final-outcome appends. Helper-confirmed pushed hashes:

| commit | landed content |
|---|---|
| `82745e2c60e726b49499b8f309529935dc4eff2b` | candidate C1/C2/C3, source rows S033–S037, docs and all88 build reports |
| `9b755f5b44ace949fc4d71c9d6d8f125a560e9cf` | fresh falsifier repairs, S038 rejection, receipt binding, measurement instruments,52 falsify reports and12 deaths |
| `1bf3eec48d3761580ffd375c88143232485ae814` | actual immutable measurements, three claim-only overlays, final SCORECARD/LOG/lesson outcome metadata and pins |

Expectation migrations: `.ufo/waves/round-25/expectation-migrations.json` in the lane. Stamp membership83→88: all83 original paths retained,5 added,0 dropped. Ledger61→65: all original IDs retained, R25-01..04 added. Original source rows/captures unchanged. Historical LOG line1202's candidate spacing edit was restored byte-exact; the tokenizer handles adjacent spans instead. The append-only conformance defect and restoration are recorded, not erased from history.

## Before → after measurements

Commands from `kagi-shokunin/`; `<after>` is `9b755f5b44ace949fc4d71c9d6d8f125a560e9cf`, `<base>` is `4587c61a348e4528717404a68912c373f3ef4d03`. Exact argv/stdout/exits and per-run revisions: **`kagi-shokunin/.ufo/waves/round-25/final-verification.json`**,15/15 checks PASS.

| claim | counting command | before → after / verdict |
|---|---|---|
| C1 | `bash .ufo/waves/round-25/tools/c1-measure.sh --common <after> <docs-rev> <label>` | IDENTICAL34 pre-existing bindings: **8 STALE→0**, before exit1/unlocated0/ambiguous0, after exit0. Full after38 CLEAN. **Measured bounded doc/source agreement**, not statistical calibration or completeness. |
| C1 control | `bash .ufo/waves/round-25/tools/c1-measure.sh --mutate SC-SKILL-STAMPS <after> <after> mutation` | one-digit document mutation → exactly one STALE, exit1; selftest48 passes. Earlier candidate BASE POLICY/unlocated receipts are retained but NOT the valid before-count. |
| C2 | `bash .ufo/waves/round-25/tools/c2-measure.sh <rev> <label>` | lone BASE BROKEN unresolved88/exit1 → after **INCOMPLETE unresolved0/fleet_absent48/exit3**. Fleet CLEAN in both (1371→1639 checked citations). **Measured explicit layout diagnosis**, not a claim absent evidence was checked. |
| C2 controls | same recorder | after local/self/nested-owned misses all UNRESOLVED/exit1 in both layouts; fleet missing-target control red. Ledger selftest170 passes. FLoneName additionally reproduced BASE name-dependence88vs46 and after identical48 in both clone names. |
| C3 | `python3 .ufo/waves/round-25/tools/c3-measure.py <rev>` | on_release28: **bound0/unbound28→bound28/unbound0/observed28**, orphan0, fired1. **Measured declared clock coverage plus dated observations**. |
| C3 controls | `python3 corpus/release-clock.py` / `--selftest` | byte-pinned receipt-bound CLEAN28; selftest67 PASS; S008 TSV version contradicted against retained receipt → RECEIPT-MISMATCH/exit1, observed27, never CLEAN. |

Full default verify at the measured revision, empty HOME and no host-consent flag: **exit0** `CLAIM_LEDGER: CLEAN (claims=65 deferred=0 stamped=88 ids=65 cited=55 labeled_ids=20 orphans=10 host_skipped=12)`.12 host rows unexecuted/uncredited; account-free `op` byte fixtures run only with scratch HOME/XDG as established in R21-01.

**Executed causal separability:** `separability-final.json` in the wave directory. Each constructed tree starts at BASE and extracts pinned blobs from `<after>`: C1-only common34 CLEAN with BASE membership83/61 and selftest151 (C2/C3 code absent); C2-only INCOMPLETE/absent48/unresolved0 (C1/C3 code absent); C3-only CLEAN28 with its pinned receipt (C1/C2 code absent). These are measured claim-only constructed trees, NOT full-ledger-clean commits. SHA256 inputs and exact commands/exits retained.

## Sources & frontier

Registry/captures **32→38**; added **6 tierA**,0 tierB/C: S033 SOPS, S034 Vault, S035 OpenBao, S036 Python, S037 curl (mined), **S038 WHATWG HTML empty release feed (rejected)**. New URLs opened this round; Gate records dates,located≤25-word quotes and rejection flip. **Existing status/recheck/used-by changes: none.** New feeds use90d, not on-release, so no clock-for-clock population inflation. C3 is sourced by S033–S037; S038 grounds the living-standard fallback rejection. No new knowledge entry; demonstrated capability and release-clock frontier path added. S011 footer changes and multi-claim quote coverage remain bounded limitations, not silently covered.

Counting command: `bash corpus/sources-census.sh` (R21-02), final CLEAN rows38/A36/C2/queued1/mined34/rejected3/captures38. Required fleet census command, run at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
```

Start (`census-start.txt`), exit0:
```text
kagi W04 S019 duplicate url www.1password.dev/brokered-access across scopes
kagi W04 S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes
kagi W04 S021 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi W04 S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes
kagi W04 S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes
kagi W04 S025 duplicate url openbao.org/docs/auth/jwt across scopes
kagi W04 S026 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi W04 S032 duplicate url www.1password.dev/brokered-access across scopes
kagi ok /home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
exit=0
```
End (`census-end.txt`), exit0 (same eight pre-existing warnings):
```text
kagi W04 S019 duplicate url www.1password.dev/brokered-access across scopes
kagi W04 S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes
kagi W04 S021 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi W04 S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes
kagi W04 S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes
kagi W04 S025 duplicate url openbao.org/docs/auth/jwt across scopes
kagi W04 S026 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi W04 S032 duplicate url www.1password.dev/brokered-access across scopes
kagi ok /home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
exit=0
```

Displayed census fields above are space-rendered; committed receipts preserve original tabs. Mined mistake M25-1: unbound current-tense numbers survived the existing gates; the new binder's mutation now fails. Fresh falsifiers and QM21–QM23 are lesson-backed. Non-author admit/reject spot-check remains for the parent's closure; these dispatched seats are still the author lane.

## Trend verdicts

- **expansion — improved (capability):** release-clock observation demonstrated on28 clocks and entered the main capability table. No new governed host surface or knowledge-entry count claimed.
- **quality — improved:** stale self-descriptions corrected/bound, layout limits made explicit, source identities freshly observed, concrete counterexamples repaired with retained red/green evidence. Knowledge-entry numeric debts are marked in the lesson, not pronounced current.
- **discernment — unchanged pending outside review:** rejects/criteria/mutations are author-side evidence. No non-author agree-on-admit-and-reject judgment is self-certified.

## SHONEN

All remain author assertions, no promotion or named non-author promotion verifier:
- [~] Real decision tables/error patterns/checklists/citations — SKILL.md and `corpus/lessons/round-25.md` Gate; fleet citations CLEAN at measured revision.
- [~] End-to-end domain task logged — historical round3 auth-gate handoff in LOG.md/SHONEN.md; no fresh vault task claimed.
- [~] Instructions executable without oral context — committed scripts,15/15 measurement checks and three isolated overlays.
- [~] No cross-domain bleed — PROVINCE unchanged ownership boundaries; browser lease and vault terminal actions remain operator-owned.

## Waves, safety and conformance

- **Build88:**40 scout /16 reviewer /6 executor /6 connector /6 critic /6 scribe /4 revenger /2 sentinel /2 mutation-tester.88 reports,0 build deaths. One whole-wave job-cap refusal, same unchanged payload retried after~3min.
- **Falsify64:**28 scout /22 reviewer /7 mutation-tester /3 critic /2 sentinel /1 scribe /1 connector.52 reports,**12 provider deaths**, no replacements. Three whole-wave job-cap refusals; fourth identical payload started64. **Total152 seats**, no split/shrink/model parameters. Specs/validated dispatches/registries/outcomes committed under `.ufo/waves/round-25/`.
- Dead falsify seats: FClockS005,FClockS032,FSelfGroup2,FSelfGroup4,FSelfGroup6,FSelfGroup7,FSelfGroup9,FNetworkPolicy,FAnchorIntegrity,FConformance,FConnections,FFeedS035. FConformance: Anthropic Haiku429, retry-after-ms10159000; FConnections: Antigravity429 QUOTA_EXHAUSTED until2026-10-25T11:37:24Z; FSelfGroup7: zai429 type1302, retries exhausted5; remaining nine: `Codex is at capacity … turn_rate_limit_exceeded`, retries exhausted5. See exact task transcripts and `wave-outcomes.json` summaries. Connector kept minimal in wave2 per Main's warning; no dead seat retried.
- Scoped continuations reused original build identities for genuine repairs. XMeasureC1's wake failed on the same Codex capacity error; not replaced; L1 repaired its evidence script. This is a continuation failure, not an extra build/falsify seat. XSelfCounts/XReleaseClock continuations delivered patches.
- Process defects: canonical skill/protocol loaded late; XMeasureC2 transiently edited the live README and restored it; a lane-side normalizer import created pycache (removed); sentinel broad grep matched historical interactive transcripts (not adopted). Some seats ran account-free op fixture rows despite narrower seat no-op instructions. These are disclosed, not retroactively called conformant; no complete whole-round no-private-read attestation is available. No vault/account/handler/CDP operation or host-row consent is credited. LOG historical spacing edit restored in final commit; its candidate defect remains recorded.
- Required fleet misroot sweep: exit0, only operator/driver `.ufo/state/*`/watchdog changes, no kagi seat artifacts to move; those files untouched (`misroot-sweep.txt`). All lane work/evidence pushed before report.
- Tool installs: ClockS010 installed **pyrage1.4.0 via uv pip** in a sandbox venv for throwaway age identities, and fetched official checksum-verified **sops3.13.0/3.13.3** sandbox binaries for key-group comparison. No host PATH/system change; Sigstore verification unrun. L1 installed nothing; no pacman transaction.
- Stale-lane: respawn-per-round driver; this mission progressed through pushed commits; no other mission of this lane is open. Open L0 questions: **none**. MANIFEST/claim/driver/routing configuration untouched; final admission belongs to Main's independent closure.
