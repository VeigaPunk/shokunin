# tabi — round 20

## Work performed

**C1 — depth:** improve the playbook with a finite sample of12 current, source-bound
WebMCP completion-lifecycle decisions, measured **0→12**. Scalar depth remains8;
this is not12 newly discovered predicates, exhaustive coverage or a runtime capability.
Author verdict: **improved, bounded; declared target met**. Independent non-author
admission remains the parent's responsibility. Round19 stays closed and its d4 remains unprovable.

- Distilled conditions, direct callsites, callback ordering/guards and internal null-String
  handling from pinned Chromium154 source into the current corrected table in `SKILL.md`
  and `corpus/knowledge/webmcp-completion-lifecycle-round-20.md`; current manifest
  `corpus/evidence/round-20/lifecycle/decisions.json` (lane `e7cf11a810003d4a65cc85bd265f2c17dd65b738`).
- Retained original prose as superseded history, corrected field/effect overreach and
  preserved earlier r17/r19 observations. All current LC01–LC12 are ENTAILED in the four
  author-side residual slices under `.ufo/waves/round-20/residual/ResidualRowsA.md`
  through `ResidualRowsD.md`; these are not non-author closure.
- Landed source identity/anchor/render checks, fixed independently persisted oracles,
  canonical-table selection, malformed-row/anchor controls and a frozen metadata gate.
  Main CLI selftests passed45/45 and27/27; the actual frozen triple matched its clean pin.
  Full streams and identities: `.ufo/waves/round-20/final/serial-checks.json` at `e45b05280ac0255670a7d5206c9a00586d48f7f5`.
- W1 actor-settlement overclaims were explicitly withdrawn, not reconstructed into passes.
  W2 return was pushed before exact committed repair blobs were imported. Evidence:
  `.ufo/waves/round-20/w1/ordering-correction.json`, `repair-ledger.json`, freeze commit
  `e0b5d02a6aef76b0d2799d92618f79f1bca40062`. No complete-isolation certification or r19 repair is claimed.
- Completed the frontier audit and one-initial-commit lesson: `corpus/lessons/round-20.md`
  (`e41ae33c238540a469e4a031fad3ad00ef112616`), including Gate, retained rejects, exact source audit and Mistakes.

## Landed changes

| Landed lane commit | Changes and motivating LOG pointer |
|---|---|
| `4ae99816b8994fdedc159156d8d9d242dd5c4782` | Initial source table/manifest/note, S100 and S096 backlink, code and isolated writer evidence; `LOG.md:1194-1222` |
| `e0b5d02a6aef76b0d2799d92618f79f1bca40062` | W2 return frozen before payload repairs; w1 all-actor flags withdrawn; `LOG.md:1224-1238` |
| `ac10319843f718489a10b89a8d2a568879aaf980` | Append-only canonical source corrections,45-case oracle,27-case frozen gate, correction index and QUALITY50–51; `LOG.md:1240-1267` |
| `e45b05280ac0255670a7d5206c9a00586d48f7f5` | Restored missing SEPARATOR_ROW found by residual review; committed serial verification commands and artifact identities; `LOG.md:1269-1294` |
| `e41ae33c238540a469e4a031fad3ad00ef112616` | Executed measurements, binding manifest, one-write lesson, source audit and recovered misrooted report; `LOG.md:1296-1323` |
| `e7cf11a810003d4a65cc85bd265f2c17dd65b738` | Post-lesson no-growth and binding receipts; `LOG.md:1325-1333` |

**Lane tip / remote:** `e7cf11a810003d4a65cc85bd265f2c17dd65b738`. Helper state observed:
`branch=master local=remote=e7cf11a810003d4a65cc85bd265f2c17dd65b738 ahead=0 behind=0 head=detached tracked=0 untracked=0`.
Only the fleet and tabi remotes were pushed; no domain source tree or sibling repo was modified.

## Before → after measurements

| Claim | Before | After | Counting command / measured code |
|---|---|---|---|
| C1 depth — current documented source rows |0, exit0, baseline `c49929430d996b016dde2e3a3a5be380f3433fdb`|12, exit0, clean `e45b05280ac0255670a7d5206c9a00586d48f7f5`|`node .ufo/waves/round-20/measure-c1.mjs REV`; field `c1_lifecycle_decisions`; counter SHA-256 `19921191fad84ba79414188e1a7b1bc05acdb491b1e6052ed5b70454864f7945`|

Exact argv and full outputs: `corpus/evidence/round-20/measurements.json` and serial receipt.
There are retained historical rows too; only the unique corrected-source section is current
and counted. The counter does not establish semantic truth, novelty or runtime behaviour.
The four counted inputs are SOURCES, current manifest, source body and knowledge note;
SKILL's mirror was separately reviewed. No extra axis or capability credit is taken.

Main serial verification, once all subagents returned, at `e45b05280ac0255670a7d5206c9a00586d48f7f5`:

-28/28 expected outcomes, including22 historical-clean invocations, both new CLI selftests,
  real frozen input, both measurement arms and corpus counts.
- `MEASURE_C1_SELFTEST verdict=clean cases=45 reasons=24` (exit0).
- `CHECK_WAVE_SELFTEST verdict=clean cases=27 failed=0` (exit0).
- Actual frozen triple: `verdict=frozen_match`, findings[], pinnedExit0 (exit0).
- Known inherited red USER production gate deliberately **not rerun to confirm its error**.
  It is not called clean. Delivered lessonDrift enumeration remains exactly
  `round-18.md`, `round-19.md`; round20 has no later MDRT commit. This probe covers the
  lesson predicate, not every USER condition.

Executed pipeline:
```sh
python3 .ufo/waves/round-20/run-checks.py e45b05280ac0255670a7d5206c9a00586d48f7f5 .ufo/waves/round-20/final/serial-checks.json
```

Delivered-tip binding was actually reproduced, not inferred from the checkpoint:
```sh
/home/vgpnk/.local/share/fnm/node-versions/v24.21.0/installation/bin/node scripts/check-measurement-binding.mjs --check .ufo/waves/round-20/measurement-binding.json --at e7cf11a810003d4a65cc85bd265f2c17dd65b738 --reproduce --json
```
Exit `0`; producer `scripts/check-measurement-binding.mjs` SHA-256
`388c2b4987bbb9f39f172cd40ca392b03bc9c869c1682b77576b0b986c14af74`. Exact stdout:
```json
{"schema":"tabi-measurement-binding-check-v1","mode":"check","manifest":"/home/vgpnk/Projects/shokunin/tabi-shokunin/.ufo/waves/round-20/measurement-binding.json","repo":"/home/vgpnk/Projects/shokunin/tabi-shokunin","at":"e7cf11a810003d4a65cc85bd265f2c17dd65b738","verdict":"clean","claims":1,"bound":1,"vocabulary":{"findings":["measured_revision_not_ancestor","counter_digest_unrecorded","counter_digest_mismatch","counter_changed_since_measurement","counted_inputs_undeclared","counted_input_changed","argv_unsupported","counter_failed","count_not_reproduced"],"couldNotEvaluate":["manifest_unreadable","manifest_schema_invalid","revision_unresolved","git_failed","usage"]},"findings":[]}
```
The exact `git diff --name-only e45b05280ac0255670a7d5206c9a00586d48f7f5 e7cf11a810003d4a65cc85bd265f2c17dd65b738 --` over the four counted inputs
and counter returned empty, exit0. The final lesson probe command
`node .ufo/waves/round-20/lesson-history.mjs e7cf11a810003d4a65cc85bd265f2c17dd65b738` exited0 with the two inherited
paths and no round20 MDRT commits. The earlier committed receipts are in `final/lesson-history.json`,
`binding-after-lesson.json` and `count-input-drift.json`; the executions just described are at the delivered tip.

## Sources & frontier

Counting command: `node .ufo/waves/round-20/counts.mjs REV`, baseline `c49929430d996b016dde2e3a3a5be380f3433fdb`
versus `e45b05280ac0255670a7d5206c9a00586d48f7f5` (counted source inputs are unchanged at the delivered tip):

| Measure | Before → after |
|---|---|
| Registry rows |99→100|
| Tiers |A86/B4/C9→A87/B4/C9|
| Status |mined71/queued19/rejected9→mined72/queued19/rejected9|
| Knowledge files |37→38|

Added by tier: A1/B0/C0. **S100 is the same URL/tag/decoded bytes as S096/S078**, an anchor
extension for LC11 and extra source context, not publisher diversity or independent corroboration.
S096's only mutable change: used-by old `corpus/knowledge/webmcp-declarative-validation-round-19.md`
→ that path plus `corpus/knowledge/webmcp-completion-lifecycle-round-20.md`; status mined and
recheck on-release unchanged. Immutable cells stayed unchanged. S100 was initially mined with
its note, not a fabricated queued→mined transition. No other existing row's status/recheck/used-by changed.

The exact URL was opened this round; quote “The site has a programming error: it called”
is at html_form_element.cc:810. URL/date, raw carrier, compressed storage and decoded SHA-256
are in the lesson Gate and `.ufo/waves/round-20/source-opening.json`. W2 reopened the exact
primary source (`w2/ReviewReopenS100.md`). Initial retrieval time remains unknown; no mtime
or recording timestamp is sold as retrieval. Frontier rows closed:0. Real-site/agent-side,
non-autosubmit runtime paths and other builds remain open. This is held-ground deepening,
not expansion by adding rows or files.

Required maintained census command:
```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```
Start output (exit `0`, complete stdout+stderr):
```text
tabi	W04	S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi	W04	S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi	W04	S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi	W04	S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/panels/application/WebMCPView.ts across scopes
tabi	W04	S069 duplicate url developer.chrome.com/blog/webdriver-bidi-2023 across scopes
tabi	W04	S070 duplicate url raw.githubusercontent.com/nodejs/node/v24.21.0/doc/api/process.md across scopes
tabi	W04	S073 duplicate url github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md across scopes
tabi	W04	S074 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/platform/runtime_enabled_features.json5 across scopes
tabi	W04	S075 duplicate url developer.chrome.com/docs/ai/webmcp/imperative-api across scopes
tabi	W04	S076 duplicate url mpapad.github.io/publications/pdfs/ICST25.pdf across scopes
tabi	W04	S077 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi	W04	S095 duplicate url html.spec.whatwg.org/multipage/input.html across scopes
tabi	W04	S096 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S098 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi	W04	S099 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/public/devtools_protocol/domains/WebMCP.pdl across scopes
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```
End output at delivered tip (exit `0`, complete stdout+stderr):
```text
tabi	W04	S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi	W04	S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi	W04	S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi	W04	S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/panels/application/WebMCPView.ts across scopes
tabi	W04	S069 duplicate url developer.chrome.com/blog/webdriver-bidi-2023 across scopes
tabi	W04	S070 duplicate url raw.githubusercontent.com/nodejs/node/v24.21.0/doc/api/process.md across scopes
tabi	W04	S073 duplicate url github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md across scopes
tabi	W04	S074 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/platform/runtime_enabled_features.json5 across scopes
tabi	W04	S075 duplicate url developer.chrome.com/docs/ai/webmcp/imperative-api across scopes
tabi	W04	S076 duplicate url mpapad.github.io/publications/pdfs/ICST25.pdf across scopes
tabi	W04	S077 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi	W04	S095 duplicate url html.spec.whatwg.org/multipage/input.html across scopes
tabi	W04	S096 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S098 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi	W04	S099 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/public/devtools_protocol/domains/WebMCP.pdl across scopes
tabi	W04	S100 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```
Duplicate-URL warnings are intentional same-source/supersession disclosures; end exit0 is conformant.
Census is structural evidence, not independent source admission.

Mistakes mined: r19 missing snapshot remains unprovable; w1 actor-quiescence overclaim withdrawn;
source-anchor drift, callsite/effect overreach, incompatible oracle predictions, missing separator,
misrooted report and unsolicited leaf replay are captured in `corpus/lessons/round-20.md#mistakes`.
Failures are demonstrable in the passing CLI selftests' non-clean controls (wrong phase,
authority loss, changed source digest and snapshot tampering), not a claim of universal resistance.

## Trend verdicts

- **expansion: unchanged.** One new note distills source-held ground; no new runtime surface,
  independent source or capability (`corpus/README.md` round20/correction index).
- **quality: improved, bounded.** Current source semantics corrected and reviewed, identities
  re-opened, fixed-oracle and real-input verification exercised; false historical wording is
  explicitly superseded. No whole-domain recertification is asserted (serial receipt and lesson Gate).
- **discernment: unchanged.** Criteria50–51 are lesson-backed learning, but no external
  non-author admit-and-reject spot-check is claimed. Internal reviewers are still the lane.

## SHONEN

- [~] Real decision/error/checklist/source material: SKILL's corrected-source section and
  `corpus/knowledge/webmcp-completion-lifecycle-round-20.md`; no non-author promotion verifier asserted.
- [~] End-to-end domain task: historical `corpus/knowledge/multi-step-journey.md` and LOG round3;
  this source-only round does not claim a fresh browser journey.
- [~] Executable instructions without oral context: SKILL runbook and historical
  `corpus/knowledge/executor-test-sufficiency.md`; outside cold execution still not asserted.
- [~] Province boundary: unchanged `PROVINCE.md` and `corpus/adjacency.tsv`; no sibling ownership,
  live profile lease or real-site authority acquired.

### Operational record

- W1:64 seats, scout25/reviewer16/critic6/scribe5/revenger5/connector4/executor3.
- W2:64 seats, reviewer34/scout14/critic8/mutation-tester4/scribe2/connector2.
- Ordinary residual:8 seats, reviewer6/critic1/connector1; fewer than64 distinct remaining
  issue classes, so no padded third swarm. Total136 fresh seats; no dead seat, replacement or job-cap refusal.
- L1 holds the canonical planner; ConnPlanner was a bounded data-walk. Both full waves
  were policy-v2 validated and dispatched as exactly one unchanged taskCall each. Role-bound
  host routing was used with no model parameter or routing/configuration edits. No availability/failover claim.
- Same-identity repair steers used isolated clones; durable Git bundles and path/identity
  ledgers remain, clone scaffolds were removed. Original candidate expectations and reports remain evidence.
- Conformance defects disclosed: w1 all-actor flags withdrawn; w2 dispatch-start snapshot
  was after spawning and says so; ReviewBindingInputs ran an unsolicited historical r19
  binding replay (no target/browser execution or writes), not L1 verification or re-adjudication.
- Fleet misroot sweep found one own ResidualFrozen report. It was copied byte-exact to the
  lane, cmp exited0, and only the own fleet copy was removed. Evidence `final/misroot-recovery.json`.
  Fleet runtime/state and foreign files were untouched. Initial lane working tree was clean;
  no inherited uncommitted work was reused. r19 committed artifacts are labelled history.
- **Stale-lane:** respawn-per-round; only this tabi round20 mission was open and progressing
  through commits/wave artifacts; no other open tabi mission is asserted.
- **Tools installed/updated:** none. Main used existing Node24.21.0, Git and the mandated lane/fleet helpers.
- **L0:** no new round20 question. Two inherited round17 questions (the-musketeer/CDP lease;
  reach of the CDP ruling to revenger/kama) remain open. The round19 USER question is resolved-by-ruling.
  No next round was claimed or dispatched.
