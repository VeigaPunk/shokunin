# tabi — round 28 (attempt 1)

## Work performed

Claims declared before data: **C1 depth** — bind S106 evidence to source bytes at a named measurement revision, retain CNE behavior, and add matching/mismatch controls; **C2 calibration** — make selfassessment supersession require a citation containing the exact stale tally line, with unrelated-line/timestamp red controls. Lowest non-retired score tie is 8; C1 works depth. Frozen claim record: `tabi-shokunin/.ufo/waves/round-28/claims.json`.

- Read round-27 outside review and carried its routed defects: false-clear of `LOG.md:221` and missing S106 measurement revision binding (`corpus/lessons/round-27-verifier-spotcheck.md:15-17,46-49`).
- Reopened S106 committed source bytes at `corpus/evidence/round-26/sources/content-features-154.0.8037.97.cc:186-187`; matching decoded anchor supports claim C1 and is recorded in this round's lesson Gate.
- Reopened rejected S125 URL this round; the RFC6265bis draft identifies itself as cookie-state-management text, not rate-limit material. Rejection retained; lesson `corpus/lessons/round-28.md` Gate.
- One v2 wave `w1`, validated and handed off inline through `.ufo/waves/round-28/w1.ready`; 64 results are in `w1-results.json`. Seat role counts from results: 24 executor, 8 scribe, 8 critic, 8 reviewer, 8 mutation-tester, 4 connector, 4 scout. All 64 returned output; zero missing/dead. Attack roles 24/64 (37.5%); m_flash role majority executor/scribe/critic 40/64 (62.5%). L1 held the planner seat; no residual calls. Reports: `.ufo/waves/round-28/w1/`.
- Post-data implementation updated S106 receipt/gate and selfassessment line-citation matcher; `corpus/QUALITY.md:374-385` and SKILL registry Round 28 record the intended invariants. Claim self-tests/counters were **not run by L1**; this is not verification. Implementations and rationale are documented in `LOG.md` Round 28 and lesson M1/M2.
- Fleet-root misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed shared `.ufo/state/*`, `.ufo/watchdog.log`, `.ufo/waves/round-30/`, and an unrelated untracked `corpus/knowledge/journalctl-v262-field-filter-r36.md`; no round-28 tabi seat file was found there. All foreign/operator paths were left untouched.

## Landed changes

Round-28 lane work is committed and pushed at `b4128c420009a9736c8a64f75ccc02fc94c68502` (helper output `landed`). Changes in that commit are tied to `LOG.md` Round 28: `scripts/check-s106-evidence.mjs`, `corpus/evidence/round-26/sources/s106.json`, `scripts/check-selfassessment.mjs`, `corpus/QUALITY.md`, `SKILL.md`, `SCORECARD.md`, `corpus/lessons/round-28.md`, and `.ufo/waves/round-28/` evidence.

## Before → after measurements

| Claim | Counting command | Before | After / verdict |
|---|---|---|---|
| C1 depth | `node scripts/check-s106-evidence.mjs --selftest` | 5 cases at baseline `eb23c0b84668afc48ebab8bd7e4a8a4457407cc4` (baseline run from w1 reports, e.g. `Crit02.md`, `Crit06.md`) | Not run by L1 after edit. **Unprovable**; target is not declared met. The source binding implementation points at measured commit `0c666adc217685e1ece2af8596b732b303a3b15c`; matching and divergent source fixtures were added. |
| C2 calibration | `node scripts/check-selfassessment.mjs --rev <REV> --json`; `node scripts/check-selfassessment.mjs --selftest` | Prior verifier reports `LOG.md:221` claimed 8 / observed 12 / `superseded=true`; baseline selftest 17 cases (`w1/Crit01.md`, `Crit05.md`) | Not run by L1 after edit. **Unprovable**; target remains whether `LOG.md:221` persists absent an exact citation and regression cases reject unrelated citations. |

No numeric axis score delta claimed. No do-nothing target claim admitted; both claims remain **unprovable pending main verification**. Claims do not establish a round pass.

## Sources & frontier

Census command, run at round start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`

Before (exit 0):
```text
tabi	W04	S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi	W04	S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi	W04	S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi	W04	S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
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

After (exit 0):
```text
tabi	W04	S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi	W04	S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi	W04	S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi	W04	S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
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

- Rows 107→107. Tier additions A=0, B=0, C=0. Rows touched: none; status/recheck/used-by transitions: none. Frontier rows advanced: none. S106 was reopened from committed bytes and cited by C1; no new registry row was required. S125 remained rejected, with no registry change.
- `Assimilation: none` — no `considerthese/` directory exists and no new `merge/tabi/` item was adopted. Existing §10 quarantine/L0 conflict is not silently resolved. Lesson Gate records the reopened admit and reject.

## Trend verdicts

- **Expansion: unchanged** — no knowledge entry or coverage-map ground was added; census stayed 107 rows.
- **Quality: unchanged** — no corpus knowledge entry was deepened, superseded, or re-verified; gate edits are unverified and do not constitute an entry-quality verdict.
- **Discernment: unchanged** — no outside non-author admit/reject spot-check this round; dispatched seats are lane-author work.

## SHONEN

[~] SKILL decision tables/error patterns/checklists — `SHONEN.md:5-6`.
[~] End-to-end domain task logged — `SHONEN.md:7-8`.
[~] Executable instructions without oral context — `SHONEN.md:9-10`.
[~] Province accurate / no cross-domain bleed — `SHONEN.md:11-12`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs/updates: none. No L0 question newly filed; round-27 S114/S140 question remains open and unassumed answered. No domain-source tree writes.
