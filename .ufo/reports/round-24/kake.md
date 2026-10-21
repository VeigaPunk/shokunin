# kake — round 24, attempt 1: measured repairs; policy-stop admission hold

## Work performed

Declared claims: **C1 freshness — reconcile the frozen filesystem-path population**, and **C2 operability — reject malformed publishing receipts without accepting or crashing**. Both work the tied-lowest owned axes (legacy 10/10); scores remain HOLD, not a new claim of corpus-wide cleanliness. C1 and C2 have recorded bounded local improvements. **Round admission/progression is withheld:** the original coordinator encountered `cyber_policy`, the falsify wave has no completed reports, and independent non-author review/no-harm remains incomplete.

Unless prefixed with the fleet path, evidence paths below are relative to `/home/vgpnk/Projects/shokunin/kake-shokunin`.

- Reused the same already-held round24/attempt1 claim; no dispatch claim, different round, or next round was started. Preserved the original claims, populations and preservation amendment (`.ufo/waves/round-24/{contract,contract-amendment}.json`; `SCORECARD.md` Round24).
- C1 reconciled **19 path targets**, distinct from **101 frozen original citation coordinates** and **30 sidecar correction records** (4 absent, 26 restored). Dated observations support adding12 actual misses and removing4 recovered tokens from the pin (55→63). Original citation lines and the two non-author lesson files remain unchanged; sidecars plus EOF notes supply corrections. This is not source restoration, retirement, deployment verification or publishing authority (`c1-population.json`, `c1-receipts/`, `corpus/knowledge/freshness-sidecar.json`; recovery/docs-audit.md).
- C2 integrated `scripts/receipt_replay.py` as the maintained successor to the byte-preserved round23 readers. The frozen population has130 cases:110 expected rejects and20 accepted controls. Timestamp/calendar/offset/bounds, typed media metadata and JSON integrity policies are source-grounded but explicitly local where stricter than an RFC. Existing pristine controls remain17/17 and12/12 (`c2-population.json`, `population-selection.json`, `implementation-suite.json`; SKILL.md maintained receipt-replay registry).
- Opened primary sources S032–S034 during the original build; retained URL/access/digest/located-quote evidence and the admitted/rejected policy choices. Added the omitted bounded source-search note during recovery (`corpus/SOURCES.md:40-42,73`; `corpus/lessons/round-24.md` Gate; w1/SourceRFC3339.md, SourceRFC9110MediaType.md, SourceRFC8259Json.md).
- Re-verified inherited partial artifacts by documentary Git-blob, digest, revision, terminal-record and receipt-output audits, **not by rerunning the policy-interrupted assignments**. The two new recovery seats audited bookkeeping only, and neither substitutes for a missing falsifier (`recovery/{provenance-audit,interruption-inventory,counting-recipes}.json`, `{docs-audit,evidence-audit}.md`). All these audits remain author-side.
- Retained the original evidence without hiding the selftest shape-only defect: concrete temporary/home-resolved paths occur in saved selftest output, while recorded argv omits override-variable/isolation shape. That violates the local evidence criterion; it does not by itself falsify the tally. The receipts were not rewritten, and no complete isolation/no-harm claim is made (`recovery/docs-audit.md`; lesson Documentary-audit dispositions).
- No refused probe was rephrased, rerouted, retried or replaced. Original coordinator error at **2026-10-21T12:22:15.004Z**: `Codex error event: This content was flagged for possible cybersecurity risk.`, code `cyber_policy`. The documentary record and L0 disposition request preserve the stop rather than manufacturing successful falsification (`recovery/interruption-inventory.json`; fleet `.ufo/l0-questions.md`, kake round24 “Policy-stop disposition”).

## Landed changes

Final lane commit, pushed and remotely verified by the lane helper: **`6883f1d580d811f7c434d1db4642596362f822b1`**. Required lane `git status --porcelain` immediately after that landing printed nothing. No later lane changes or tests were made.

| Change | Landed commit | LOG/evidence |
|---|---|---|
| Freeze populations, counters, source observations and build evidence | `ab85dbdba4499f35f7dab9c9635b9b605679dbe5` | LOG.md Round24, baseline measurement entry; round24 contract/populations |
| C1 preservation-safe paths reconciliation, observations, pin adjustment and sidecar workflow | `3d07733b482f88c42cb008397188237c80e42b67` | LOG.md:845,849; `measure-c1-c1-only.json`; lesson Path reconciliation |
| C2 maintained replay, source-backed knowledge, QUALITY criteria and SKILL registry | `faace82dcf50e1c563d437f2caecb77a9a865880` | LOG.md:850; scripts/receipt_replay.py; original after/control receipts |
| Durably retain after-measurement suite, falsify spec/dispatch/registry, corrected death accounting, documentary audits, source-search note and append-only disposition | `6883f1d580d811f7c434d1db4642596362f822b1` | LOG.md:852-889; SCORECARD/lesson recovery sections; `.ufo/waves/round-24/recovery/` |

The first three hashes were already pushed by the original coordinator; the final helper landing retains their ancestry. Historical round23 runners/receipts are not replaced. Recovery edits are bookkeeping/source-search prose, not a new runtime implementation. No unrelated operator/sibling files were swept into the lane landing.

## Before → after measurements

These are **original executed measurements**, preserved and audited in recovery. Their measured implementation revision is `faace82dcf50e1c563d437f2caecb77a9a865880`, not the later bookkeeping commit. No gate, selftest or falsification was rerun by the replacement.

Run from the lane root, with `<revision>` replaced by the full commit below:

```sh
python3 -B .ufo/waves/round-24/measure_c1.py --root . --revision <revision> --json
python3 -B .ufo/waves/round-24/measure_c2.py --root . --revision <revision> --json
```

| Claim | Before: `ab85dbdba4499f35f7dab9c9635b9b605679dbe5` | After: `faace82dcf50e1c563d437f2caecb77a9a865880` | Verdict/evidence |
|---|---|---|---|
| C1 freshness | accepted0/19; paths exit1; command exit1 | accepted19/19; paths exit0; command exit0 | improved-bounded locally, 10→10 HOLD; `measure-c1-{before,after}.json` |
| C2 operability | correct81/130: reject61/110, accept20/20; command exit1 | correct130/130: reject110/110, accept20/20; command exit0 | improved-bounded locally, 10→10 HOLD; `measure-c2-{before,after}.json` |

C1-only separation: at `3d07733b482f88c42cb008397188237c80e42b67`, the same commands yield C1 19/19 exit0 while C2 remains81/130 exit1 (`measure-{c1,c2}-c1-only.json`). The counter digests are identical at all three revisions; C2 population SHA256 is `16da1936f30e2e7bfa405d9b51dfc18ab686edbd9f1d36f65d76626b0cab7b8f`. This is causal separation, **not** outside admission.

The inherited implementation suite records both pristine replay controls (17/17 with79 HOLD/55 STALE/42 UNVERIFIABLE;12/12 with3 clean/5 failed-policy/4 not-served), replay selftest129, C1selftest53 assertions, matrix selftest7, sweep35, canonical matrix32 and clean corpus-contract. These results are bounded local checks; selftest shape-only conformance is defective as disclosed above. They do not fill the absent falsify reports or prove originating network truth. Exact argv/stdout/stderr/exits: `implementation-suite.json` and its per-command JSON receipts.

The frozen contract's `count` fields omit `-B`/`--json` and are shorthand, not exact executed argv. Receipt argv is authoritative. The after JSONs have no `executedAt`; the original coordinator tool-event projection spans **12:18:27.711Z–12:19:08.152Z**, records both after-counter exits0, and precedes the12:22:15.004Z policy error (`recovery/provenance-audit.json`). Commit times are not measurement times. The first round-open paths run (11:33:15Z) and saved JSON capture (`generatedAt`11:35:35Z) are separate observations.

## Sources & frontier

Source validation command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Start output (`census-before.txt`):

```text
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit: 0
```

Recovery end output (`recovery/source-census.json`):

```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
exit: 0
```

Registry census at base `f7de3ab4e9f030a15a857a5a08631bd8e690f436` versus implementation `faace82dcf50e1c563d437f2caecb77a9a865880`: **31→34 rows; A29→32, C2→2; mined27→30, queued2→2, rejected2→2.** The exact Git-based counting recipe is committed in `recovery/counting-recipes.json` (`commands.sourceRows`); apply it to each named revision. Original31 rows are byte-identical. Added by tier: A3, B0, C0. The warning is a repeated canonical RFC9110 URL under distinct validator/URI/media-type scopes, not concealed validation success with warnings removed.

- New S032–S034 were opened in this same round and ground C2's sourced knowledge section. Each new row's URL, access date and ≤25-word located quote is in the lesson Gate. Source commands/digests remain in the corresponding w1 reports. The interrupted w2 reopening seats are not credited.
- New-row evolution within the round: S032–S034 `used-by` changed from `corpus/lessons/round-24.md` to `corpus/knowledge/static-canonical-preflight.md, corpus/lessons/round-24.md`; status mined→mined, recheck365d→365d. The lesson logs the evolution; no pre-round row cell changed.
- Frontier advanced: the individually qualified citation debt and recovered-source pin re-arming now have dated receipts/sidecar rules. This does **not** restore or retire absent domain trees, reverify deployment/chat binding, or enter rendering/Google-selected-canonical territory (PROVINCE.md Round24; corpus/README.md Round24 frontier maintenance).
- Mined mistakes: lexical/type survivors, stale recovered-source premise, preservation-unsafe suffix proposals, and truncated JSON-pipe output have named evidence/criteria in lesson Mistakes. Policy interruption is recorded as disposition, not a claimed code repair. The inherited red-before matrix is81/130, not selftest evidence substituted for a before measurement.
- Round23 outside ruling is fleet MANIFEST rounds[394]; no standalone `round-23-verifier-spotcheck.md` exists in this lane. Its timestamp/contentType/path defects motivated C1/C2 and the new grounded QUALITY criteria. No operator-* lesson was found by the recovery glob.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only tracked `.ufo/state/*.report-baseline` and watchdog changes, with **zero untracked rows**. No owned misroot was found/copied/deleted; sibling/driver files were untouched (`recovery/counting-recipes.json`).

## Trend verdicts

- **expansion — unchanged.** No new uncovered knowledge entry or capability-table row is admitted. This round maintains existing citation/replay ground; the replay capability keeps first-working round23 (SCORECARD capability maintenance pointer).
- **quality — improved, bounded/local.** Recorded C1/C2 populations improve without changing their counters/population oracle, while original observations and failed-policy/not-served results stay visible. This is not an independent full-round no-harm finding; unfinished falsification and the retained shape-only conformance defect remain explicit (`recovery/docs-audit.md`, provenance-audit.json).
- **discernment — unchanged.** Author-side mistakes/criteria are grounded, but no independent non-author admit-and-reject spot-check for round24 exists. Self-dispatched reviewers and documentary audits cannot grant it. Admission/progression remains withheld.

## SHONEN

No promotion is asserted; SHONEN.md remains unchanged and unchecked. Author-side assessments only:

- [~] Real decision tables/error patterns/checklists/citations: SKILL.md static-preflight and maintained replay registries; corpus/QUALITY.md; sourced knowledge and S032–S034. Non-author verifier pending.
- [~] End-to-end domain work logged: LOG.md Round23 GET/canonical outcome and Round24 dated path reconciliation; no restoration/publication claim. Non-author verifier pending.
- [~] Executable instructions: SKILL.md preservation-safe paths/replay workflow plus recorded control/matrix outputs; the absent falsify wave and shape-only defect preclude an independent executable-instructions pass.
- [~] Domain boundary: PROVINCE.md Round24 keeps source observations read-only and routes browser execution to tabi, research method to chousa, credentials to kagi, publishing/accounts to the operator. Non-author verifier pending.

### Swarm evidence, failures, and disposition

| Dispatch | Seats | Role mix | Returned reports / failures |
|---|---:|---|---|
| Build w1, one validated batched call |72| scout18, reviewer15, executor9, mutation-tester8, revenger8, scribe6, critic4, sentinel2, connector1, simplifier1 |55 reports;17 unreplaced deaths:16 Haiku429,1 Antigravity429 |
| Falsify w2, one validated batched call |64| reviewer19, mutation-tester17, executor10, critic6, scout4, revenger4, connector1, sentinel1, scribe1, simplifier1 |0 completed report files;62 `Request was aborted`,1 connector quota429,1 interrupted without final |
| New ordinary documentary recovery batch |2| reviewer1, scout1 |2 reports; no runtime probe/test reruns; not replacement falsifiers |

**Round total138 seats;81 build/falsify seats have no completed report.** No dead seat was replaced. L1 holds the planner seat because the validator excludes planner as a swarm role. Specs/dispatch payloads/registries remain under `.ufo/waves/round-24/`; `recovery/counting-recipes.json` derives mixes and report lists. The original host-required `solutionSpace` additions to rendered task items are disclosed in LOG.md:847 rather than described as literally untouched payload bytes. No model parameter or routing/configuration change was made by recovery.

Exact w1 errors are retained in `w1-deaths.json`: Haiku `429 rate_limit_error: This request would exceed your account's rate limit. Please try again later.`; connector `Cloud Code Assist API error (429)` / `QUOTA_EXHAUSTED`, reset2026-10-25T11:37:24Z. Wave2 connector has the same quota reset; all64 terminal projections and the separate coordinator `cyber_policy` termination are in `recovery/interruption-inventory.json`. Missing reports remain uncredited, even when partial transcript tool calls exist.

**Inherited state:** reused55 committed w1 reports, existing frozen/source/pin/implementation commits, baseline/intermediate receipts, and the unlanded after-suite plus w2 spec/dispatch/registry after provenance review. All retained artifacts were committed by the final lane helper. No evidence was discarded; unfinished w2 transcripts were not promoted to completed findings. The two documentary audits leave that verification debt unresolved.

**Tools installed:** original build seat SourcePythonDatetime installed **CPython3.10.22 and3.15.0** using `uv python install 3.10 3.15` (**uv0.13.0**, uv-managed interpreter channel) to compare pre-3.11 parsing with current Python docs (`w1/SourcePythonDatetime.md:72`). No Python package/system upgrade is reported. Replacement coordinator and both documentary recovery seats installed nothing; no pacman transaction or host-service/configuration change occurred in recovery.

**Stale-lane:** respawn-per-round replacement of the same round24/attempt1; the earlier coordinator is terminated, not a second live writer. This mission is progressing through the pushed recovery commit/report; no other mission of this lane is open. No round25 is started.

**Open L0:** kake round24 “Policy-stop disposition” requests operator/non-author admission/progression disposition from the retained record. It asks for no access-tier change or refusal workaround. Existing source restore-or-retire/deployment/account gates remain operator-owned. The report's landing is durability, **not** admission or authorization to resume refused work.

### Documentary population-count recipe

For the distinct C1 units above, the following reproduction command reads the retained JSON data only (lane root; not a gate or a renewed falsifier):

```sh
python3 -c 'import json,collections; p=json.load(open(".ufo/waves/round-24/c1-population.json")); e=json.load(open("corpus/knowledge/freshness-sidecar.json"))["entries"]; print("targets",len(p["targets"]),"citation coordinates",sum(len(t["cites"]) for t in p["targets"]),"corrections",len(e),"kinds",dict(collections.Counter(x["kind"] for x in e)))'
```

Reported documentary values are targets19 / citation coordinates101 / corrections30 / kinds absent4, restored26 (`recovery/docs-audit.md`). This recipe is supplied for reproduction; the replacement did not claim a new runtime measurement from it.
