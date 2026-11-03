# tabi round 61 (attempt 1)

## Work performed

Declared claims: **C1 adjacency** (lowest owned axis 8), snapshot-bound v20 meter plus wide-screen clause; **C2 coverage**, capability `chromium-pointer-event-domain-linux`. Frozen at `7032914cb5229dc9ce2b867827e6f1ee5db7673b`. **C1 KILLED; C2 UNPROVABLE; round not admitted.** No capability entry or axis-score bump. Final lane `544a40ac8328ee355b7c41bd67da856f058726e2`, remote verified with `git ls-remote origin refs/heads/master`.

- Built v20/rebind tools, pointer runner and receipt counter; baseline `6c5c2a2e`, instrument/wave landing `bcbf6be99988182e58ae0703d79975c1a3aea6f5`; final work `544a40ac`. LOG.md round-61 entry binds this work. Evidence prefix below: `.ufo/waves/round-61/` inside tabi-shokunin.
- Ran a real committed loopback pointer journey: `measure/live-run-command.json`, `measure/live-run.stdout.json`, `measure/c2-live.json`, and `corpus/evidence/round61/chromium-pointer-domain/receipt.json` plus two PNGs. Runner and counter exit 0; page pointer/mouse seq 1–6, focus field, invocation-bound per-character typing. Teardown survivors [], sweep 0, both ports closed, curls 7/7.
- Preserved failure, rather than retroactively admitting repairs: Reviewer A5-HEADER, Critic bottom line, Sentinel G5 and `DATA-PASS-RUNBOOK.md`. Frozen snapshot header restored exactly; repaired header separately retained as candidate. claims.json unchanged. Counter interface/nonce changes after scoring are substantive, not an admission-preserving “pre-data correction”.
- ONE v1 w1 of **11** seats: executor×3, mutation-tester×2, scout, scribe, connector, reviewer, critic, sentinel. Strict attack-role share reviewer+critic+mutation×2 = 4/11 (36%); including sentinel 5/11. One connector. Planner held by L1 because validator excludes it; this is disclosed conformance debt, not a twelfth L2. No residual call, no nested labrat (executor probed directly), no dead seats reported. WAVE-DONE received from Main after all 11 settled; `w1-results.json` contains all 11 outputs (it omits per-seat status/id fields, so identities/models are role-route assignments, not claimed answering-model observations). Routes observed in host config: m_flash implementation roles, m_zfl reviewer/critic, m_antigravity scout; m_mim on no role.

## Landed changes

- `7032914c`: frozen claims, sibling snapshot, census start and red v19 control. LOG.md round 61 and lesson measurements.
- `bcbf6be9`: integrated instruments, fixtures, source receipts and settled wave evidence. LOG.md round 61; final code pins in `measure/instrument-pins.json`. Seat mutations certify their named earlier shas, **not** final integration.
- `544a40ac`: real live pointer data, S164 registry row, lesson, QUALITY 113, SCORECARD disposition, LOG entry and retained checks. No production r61 adjacency ledgers or knowledge note admitted. Candidate adjudications are not an independently verified cutover.
- Fleet L0 routing committed/pushed as `83f4cd404f90ec6a643088a3eaef5d26c105410b`. Existing round-57 assimilation, round-59 kaidoku and round-60 keyup-value questions stay open; new round-61 planner/handoff mapping question.
- Inherited state was clean at round open. Previous integrator spot-check retained untouched; routed R1 honored (no anchor edits), R2 not declared closed, R3 routed to operator, R4/R5 pending. No tool installs or pacman transactions. Observed Node v26.12.0 differs from the frozen descriptive host note's v24.21.0.

## Before → after measurements

Measured work revisions: freeze `7032914c`, instruments `bcbf6be9`, final data `544a40ac`.

**C1 / adjacency — KILLED (K4).**

```sh
node .ufo/waves/round-59/counters/c1-adjacency-host-v19.mjs --rev 6c5c2a2ef5dc9c790426e7d9efe2d3025a156441 --repo /home/vgpnk/Projects/shokunin/tabi-shokunin --fleet /home/vgpnk/Projects/shokunin --json
# before exit 1, predicate false, findingCount 18 (controls/c1-v19-at-round-open.json)
node .ufo/waves/round-60/counters/c1-wide-screen-r60.mjs --scope wide --snapshot .ufo/waves/round-61/c1/snapshot-r61.tsv --json
# frozen after-input exit 2: bad snapshot header "lane\t", expected "lane\thead"
```

Reviewer and Sentinel executed that red counter on frozen bytes. The repaired-header shadow (same heads) greens the old counter at 85775/85775 Markdown blobs; this does not rescue the frozen claim and exposes the thin stale-row-control premise without --verify-rows. Rebind smoke exit 3 with 110 unresolved lines, no production ledgers. Local v20 selftest 42/42 and --list-observed 16 rows are narrower checks only.

**C2 / coverage — UNPROVABLE as frozen claim, integrated artifact demonstrated.**

```sh
git ls-tree -r --name-only 7032914c -- corpus/evidence/round61 | wc -l
# before 0
git ls-tree -r --name-only 544a40ac -- corpus/evidence/round61 | wc -l
# after 3
node .ufo/waves/round-61/counters/chromium-receipt-r61.mjs corpus/evidence/round61/chromium-pointer-domain/receipt.json --driver scripts/chrome-cdp-loopback-round61.mjs --expect-driver-sha256 f33f0ab72eec4f13519cd67a0768c5f743a7b14248c68bdc1bc9f639352a4e76 --shot corpus/evidence/round61/chromium-pointer-domain --json
# final integrated live run exit 0, predicate true, findings [], couldNotEvaluate []
node .ufo/waves/round-61/counters/chromium-receipt-r61.mjs --selftest
node .ufo/waves/round-61/counters/chromium-receipt-r61.mjs --path-selftest
# locally exercised before instrument landing: both 129/129, exit 0; idCoverage 68/68
```

Receipts in `measure/counter-*-final.txt`. On the re-smoke, generated f1–f5 each exited 1; r60 cross-refusal exited 1. Those recorded executions are not silently elevated into final-byte mutation certification. Critic residuals include green consistent secondary-button/second-press/move-id forgeries at the sha it tested; no closure of those classes claimed. Original mixed-recorder receipt versus final counter was red; split seq recorder re-smoke green. No new capability row or knowledge note is admitted.

## Sources & frontier

Counting command, run over both committed revisions:

```sh
git show 7032914c:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
git show 544a40ac:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
# 163 -> 164
```

One added tier-A/spec/mined row **S164**, scoped to the served Pointer Events Level 4 Working Draft 2026-10-08 interface. Lesson Gate records URL, access date 2026-11-03 and ≤25-word located quote. Admit pointerType/pointerId/pointerdown interface ground; reject S164 as an isTrusted definition or proof of interoperability. Scout's proposed row was narrowed to avoid those overclaims. S153/S161 re-opened byte-identical; existing rows unchanged, so no status/recheck/used-by old→new edits. Final source gate: rows=164, A:148 B:7 C:9, queued:15 mined:139 rejected:10, findings=0, exit 0 (`measure/check-sources-final.txt`).

Frontier: live pointer experiment measured, but no core/capability admission; knowledge 74 unchanged. Mistakes mined with red/green witnesses in `corpus/lessons/round-61.md`; QUALITY 113 added. Assimilation: none — adoption remains closed on round-57 register issue. `considerthese/` absent. Cross-domain evidence (kagi/kake 9222 lease, kama listener census, kaidoku capture/compare ground) is inventoried in connector/adjudication artifacts, not absorbed or ruled closed.

Census command (both times):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`

Before, exit **0**:
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
tabi	W04	S114 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S115 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S118 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
tabi	W04	S123 duplicate url www.rfc-editor.org/rfc/rfc9309.txt across scopes
tabi	W04	S148 duplicate url nodejs.org/docs/latest-v24.x/api/cli.html across scopes
tabi	W04	S156 duplicate url learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process across scopes
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```
After, exit **0**:
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
tabi	W04	S114 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S115 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi	W04	S118 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
tabi	W04	S123 duplicate url www.rfc-editor.org/rfc/rfc9309.txt across scopes
tabi	W04	S148 duplicate url nodejs.org/docs/latest-v24.x/api/cli.html across scopes
tabi	W04	S156 duplicate url learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process across scopes
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```

Same 22 existing W04 warnings; none added by S164. Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` retained at `controls/fleet-misroot-sweep.txt`: orchestrator .scratch state, L0 file and unattributed `after` file left untouched (its content does not identify this lane/round). No proven seat misroot to move/delete.

## Trend verdicts

- **expansion: unchanged** — real pointer work exists, but no capability/knowledge admission; S164 row alone is not expansion.
- **quality: unchanged** — final local checks improved integration, but no existing admitted entry re-certified or superseded; frozen-input drift and stale mutation pins explicitly marked, not left as false passes.
- **discernment: unchanged** — self-dispatched attacks exposed defects and generated QUALITY 113; independent admit/reject sample still pending. No self-attested non-author judgment.

Stale-lane: this respawn-per-round mission progressed through freezes, wave, live journey and pushed records; no other tabi mission is open. Scratch removed after retained evidence and lane landing. No tools installed.

## SHONEN

- [~] Decision tables/error patterns/checklists: SKILL.md Approval table, Evidence ladder, Runbook; author assessment only (SHONEN.md box 1).
- [~] End-to-end domain task: LOG.md round 61 and committed pointer receipt/PNGs (box 2); no non-author certification.
- [~] Executability: corpus/knowledge/executor-test-sufficiency.md; prior lane-dispatched executor is not a non-author verifier (box 3).
- [~] Domain boundary: PROVINCE.md and connector overlap inventory; no promotion or outside boundary ruling (box 4).
