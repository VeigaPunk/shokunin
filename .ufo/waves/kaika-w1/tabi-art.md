# Tabi ART dossier — browser and web-interaction craft

## Scope and evidence boundary

**Observed:** Tabi owns browser and web-interaction craft: operating real browsers with evidence discipline, CDP capture, browser/profile inventory, rights/rate boundaries, and dynamic-page evidence (`tabi-shokunin/PROVINCE.md:3-19`). The current `SKILL.md` already has a measured CDP loopback runbook, claim-class evidence ladder, network-evidence rung, state-predicate waits, session-material shape-only rules, and interaction approvals (`SKILL.md:87-234,346-474,476-539,660-719`).

This dossier researches current external art only. No browser was launched, no live site was contacted, and no runtime feature-coverage claim was tested. Source rows are limited to material opened in this research session; all entries remain `queued` or `watch` because no lane knowledge entry cites them yet. `SOURCES.md` is absent at `corpus/SOURCES.md`; that is expected here because the draft contract assigns its creation to wave 2, not a present defect.

## Uncovered ground and what Tabi already holds

### Observed corpus and province

- **Held, from the coverage map and knowledge filenames:** webbridge substrate and daemon lifecycle (`webbridge-plugin-anatomy.md`, `webbridge-daemon-disposition.md`, `webbridge-revival-assessment.md`); browser/profile census (`browser-surface-census.md`); CDP capture, dynamic pages, evidence rungs and layer routing (`cdp-evidence-patterns.md`, `live-dynamic-capture.md`, `network-evidence-rung.md`, `layer-routing-synthesis.md`, `async-step-evidence.md`); journeys and state-changing cases (`multi-step-journey.md`, `stateful-fixture-evidence.md`, `state-changing-matrix-r9.md`, `external-class-fixture-v2.md`); interaction approval and hygiene (`interaction-approval-table.md`, `hygiene-sweep-r4.md`); durable-harness, pin, round, and closeout receipts; and public/loopback observations (`example-domain-observation.md`, `loopback-pin-stability.md`, `user-public-observation.md`). These are filename/README observations, not a reread of every note.
- **In-scope declared frontier (historical README section):** extension-to-daemon handshake semantics and version reconciliation; native WebMCP on the measured Chromium host; no measured external-site rate/terms surface; real-site journeys including POST/CSRF/redirect behavior; and durable evidence-byte provenance (`corpus/README.md:22-54`). Treat these as the README's dated frontier, not as a fresh execution result. The local ART question adds a separate external frontier: no dedicated BiDi protocol/implementation matrix, current Playwright selector/ARIA-snapshot reference, or research-curated browser-automation flakiness entry appears in the filenames or coverage-map rows.
- **Quality bar:** claims must be falsifiable or marked opinion, source-cited, separated into observation/inference/unknown, append-only when corrected, and rejections retained (`corpus/QUALITY.md:3-8`). Candidate entries below are scoped to those requirements.

### Coverage-map defect (one)

The README labels its original counts as a round-3 snapshot and explicitly retains that historical status; the defect is that a current coverage index has not caught up with the files now present. The visible README table contains eleven knowledge rows (the original eight plus three later additions), while the current directory has twenty-six Markdown knowledge files and twenty-six lesson files. The README still says lessons are zero in its historical snapshot. These counts were obtained as follows:

- `26` knowledge files — `printf '%s\n' corpus/knowledge/*.md | wc -l`
- `26` lesson files — `printf '%s\n' corpus/lessons/*.md | wc -l`
- `11` README knowledge rows — `grep -cE '^[|] `knowledge/[^`]+\.md` [|]' corpus/README.md`
- `15` knowledge files absent from the README knowledge rows — `echo $(( $(printf '%s\n' corpus/knowledge/*.md | wc -l) - $(grep -cE '^[|] `knowledge/[^`]+\.md` [|]' corpus/README.md) ))`

**Defect D1:** the dated map is honestly marked historical, but it is not a usable current coverage map: fifteen present knowledge files are not indexed by its visible rows, and its lesson count is no longer current. Wave 2 should reconcile the map rather than silently rewriting the historical claims. No other lane defect is counted from this ART-only read.

### Local craft already strong

`SKILL.md` headings and inspected sections show the lane already practices loopback-first CDP, effective launch provenance, multi-signal evidence, wire-vs-client distinction, state-based rather than fixed-duration settling, fixture archiving, and session/right boundaries. Therefore the research should extend that practice, not replace it with generic Selenium/Playwright advice. The most direct additions are: the post-Chrome-136 remote-debugging profile rule; a provider/binding/version-scoped BiDi capability matrix instead of a binary “BiDi supported” label; how Playwright's accessible-name locators and ARIA snapshots differ from an accessibility audit; and reproducible reporting of retries/order-dependent failures.

## Current art sources

Source IDs are new to this dossier only; they are not yet assigned to a lane `SOURCES.md`. `opened` records this session's opening date; `used-by` remains `—` because none is cited by an admitted knowledge note. Tier A is primary/spec/official documentation or original research; tier B is strong documentation/repository metadata that is not itself the normative spec or full paper.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|Chrome DevTools Protocol overview — https://chromedevtools.github.io/devtools-protocol/tot/DOM/|docs|A|CDP is a privileged JSON protocol organized into domains; direct third-party use is unsupported and backward compatibility is not guaranteed; `/json/version` and `/json/list` expose browser/target information.|watch|2026-10-19|on-release|—|
|S002|Changes to remote debugging switches to improve security — https://developer.chrome.com/blog/remote-debugging-port|docs|A|From Chrome 136, remote-debugging switches are ignored against the default data directory; use a non-standard `--user-data-dir`, with Chrome for Testing recommended for automation.|watch|2026-10-19|on-release|—|
|S003|WebDriver BiDi, current W3C Working Draft — https://www.w3.org/TR/2026/WD-webdriver-bidi-20261008/|spec|A|The W3C protocol is a Working Draft defining bidirectional remote control of user agents; a draft specification is not a browser/driver feature-coverage result.|watch|2026-10-19|90d|—|
|S004|WebDriver BiDi: 2023 status update — https://developer.chrome.com/blog/webdriver-bidi-2023|docs|A|Chrome's browser team documents the standards effort, Web Platform Tests as a shared interoperability suite, and historical Chrome/Firefox/framework adoption; keep it as background, not a current support matrix.|queued|2026-10-19|on-release|—|
|S005|WebDriver BiDi production-ready in Firefox, Chrome and Puppeteer — https://developer.chrome.com/blog/firefox-support-in-puppeteer-with-webdriver-bidi|docs|A|The Chrome team says Puppeteer 23 has stable Firefox support via BiDi, while Chrome continues to default to CDP; the post explains why Firefox's former CDP subset was not API parity.|queued|2026-10-19|on-release|—|
|S006|WebDriver BiDi — Selenium — https://www.selenium.dev/documentation/webdriver/bidi/|docs|A|Selenium's 2026 documentation describes enabling the WebSocket capability, event streaming, user-facing BiDi APIs, and a transitional CDP area pending BiDi implementation.|watch|2026-10-19|90d|—|
|S007|Network — Selenium WebDriver BiDi — https://www.selenium.dev/documentation/webdriver/bidi/w3c/network/|docs|A|The network reference gives concrete intercept/event examples by binding and release; its Python example labels `_add_intercept` as the currently available API, so do not infer cross-binding API parity.|watch|2026-10-19|90d|—|
|S008|WebDriver BiDi modules — MDN — https://developer.mozilla.org/en-US/docs/Web/WebDriver/Reference/BiDi/Modules|docs|B|A practical module index explains command/event names, `session.subscribe`, and BiDi modules including browsing context, log, network, script, and storage.|watch|2026-10-19|90d|—|
|S009|Create a WebDriver BiDi connection — MDN — https://developer.mozilla.org/en-US/docs/Web/WebDriver/How_to/Create_BiDi_connection|docs|B|A connection guide describes requesting `webSocketUrl`, Firefox's direct endpoint, and the extra Chromium BiDi wrapper requirement for direct command-line connections.|watch|2026-10-19|90d|—|
|S010|Playwright release notes — Version 1.64 — https://playwright.dev/docs/release-notes|docs|A|The current release adds `page.getByRef()` for ARIA refs from AI-mode snapshots, seeded test shuffling, test locks, and page WebMCP APIs; it also records bundled browser versions and breaking changes.|watch|2026-10-19|on-release|—|
|S011|Locators — Playwright — https://playwright.dev/docs/locators|docs|A|Playwright recommends user-facing role/label/text locators, resolves locator targets at use time, and says role locators do not replace accessibility audits or conformance tests.|watch|2026-10-19|on-release|—|
|S012|Auto-waiting and actionability — Playwright — https://playwright.dev/docs/actionability|docs|A|Actions wait on action-specific visible/stable/enabled/event-receiving conditions; web assertions retry until a condition or timeout rather than requiring arbitrary sleeps.|watch|2026-10-19|on-release|—|
|S013|ARIA snapshots — Playwright — https://playwright.dev/docs/aria-snapshots|docs|A|ARIA snapshots represent accessible roles, names, and states as YAML templates; matching can be partial or strict, and broad structural snapshots differ from targeted assertions.|watch|2026-10-19|on-release|—|
|S014|Locator API — Playwright — https://playwright.dev/docs/api/class-locator|docs|A|The locator reference documents `ariaSnapshot` modes/refs and warns `locator.all()` does not wait for dynamic lists, which can produce unpredictable and flaky results.|watch|2026-10-19|on-release|—|
|S015|Assertions — Playwright — https://playwright.dev/docs/test-assertions|docs|A|Web-specific assertions re-fetch and retry; generic value assertions do not. `expect.poll` and `expect.toPass` are documented for retrying more complex conditions.|watch|2026-10-19|on-release|—|
|S016|Retries — Playwright — https://playwright.dev/docs/test-retries|docs|A|A retry-pass is explicitly classified as flaky, while persistent failure remains failed; the worker/browser is restarted after a test failure, and isolated tests are preferable.|watch|2026-10-19|on-release|—|
|S017|Trace Viewer — Playwright — https://playwright.dev/docs/trace-viewer|docs|A|CI guidance records a trace on the first retry; action traces expose locator calls, before/action/after DOM snapshots, console and network records, and environment metadata.|watch|2026-10-19|on-release|—|
|S018|Fixtures — Playwright — https://playwright.dev/docs/test-fixtures|docs|A|Fixtures are isolated between tests and encapsulate setup/teardown; browser resources can be shared while the page/context test fixtures are isolated.|watch|2026-10-19|on-release|—|
|S019|ARIA Authoring Practices Guide — W3C WAI — https://www.w3.org/WAI/ARIA/apg/|docs|A|The W3C guide explains how to apply ARIA semantics to widgets, keyboard interaction, landmarks, and accessible names; it is semantic authoring guidance, not evidence that a particular page conforms.|watch|2026-10-19|90d|—|
|S020|An Empirical Study of Web Flaky Tests: Understanding and Unveiling DOM Event Interaction Challenges — https://mpapad.github.io/publications/pdfs/ICST25.pdf|paper|A|The original ICST 2025 paper studies web UI flakes and associates failures with event/DOM interactions, response checks, and synchronization/state-transition fixes; treat its sample as bounded, not universal.|queued|2026-10-19|90d|—|
|S021|Non-Flaky and Nearly Optimal Time-Based Treatment of Asynchronous Wait Web Tests — https://research.knu.ac.kr/en/publications/non-flaky-and-nearly-optimal-time-based-treatment-of-asynchronous/|paper|B|The institutional record for the 2025 peer-reviewed paper reports that developers often change wait durations even when causes lie elsewhere, and describes history/similarity-informed wait tuning.|queued|2026-10-19|90d|—|

### Leads (unopened)

- WPT BiDi per-test result data — https://wpt.fyi/results/webdriver/tests/bidi — opened only as a JavaScript application shell; no result matrix was readable in this session, so it is not a source row. Lead for per-command interoperability verification.
- Chromium BiDi Mapper source — https://github.com/GoogleChromeLabs/chromium-bidi — implementation lead for understanding Chromium's BiDi adapter; not opened.
- Chrome DevTools for agents — https://developer.chrome.com/docs/devtools/agents — official supported high-level alternative named by the CDP documentation; not opened.
- “Identifying and Mitigating Flaky Tests in JavaScript,” ICST 2025 — https://www.computer.org/csdl/proceedings-article/icst/2025/10989021/26S4FY12Ab6 — additional recent flaky-test research; not opened.
- WebMCP proposal/spec — https://webmachinelearning.github.io/webmcp/ — relevant to Tabi's declared native WebMCP frontier and Playwright 1.64 hooks; not opened.

## Candidate knowledge entries

These are proposals, not admitted facts. Each source quote is at most twenty-five words. Recommendations marked **[INFERENCE]** are implications to test, not observations from Tabi's browser runs.

### C1 — `chrome-remote-debugging-profile-boundary.md`

- **Falsifiable claim:** Chrome 136 and later ignore remote-debugging switches when launched against the default data directory; the documented automation path uses a non-standard `--user-data-dir`. This is external documentation, not a measurement of Tabi's installed browser.
- **Source and location:** S002, paragraph beginning “Therefore, from Chrome 136”. Quote: “These switches must now be accompanied by the `--user-data-dir` switch to point to a non-standard directory.”
- **Coverage filled:** the browser/profile census and CDP session/runbook surface (`browser-surface-census.md`, `cdp-evidence-patterns.md`, `SKILL.md` Runbook). It adds a current security boundary absent from the listed coverage rows.
- **Recheck:** inspect `chromium --version` and the actual effective child-process arguments; cite S002's Chrome 136 section. Compare the declared `user-data-dir` against the default profile without reading profile contents.
- **Quality fit:** versioned and falsifiable, source-cited, and compatible with Tabi's existing shape-only session-material rule.

### C2 — `webdriver-bidi-feature-matrix.md`

- **Falsifiable claim:** in the Selenium reference opened here, network-interception examples are binding/release-specific; the Python example identifies `_add_intercept` as the currently available API, while the page also presents Java code. **[INFERENCE]** Therefore “BiDi supported” is too coarse for a reliable lane contract: record exact browser, driver, language binding, command/event, and version before routing a capture through BiDi.
- **Source and location:** S003 current status (“Working Draft”); S006 Selenium enablement; S007 “Add network intercept”, Selenium v4.32 Python sample. Quote: “_add_intercept is currently the available Python API for BiDi network intercepts.”
- **Coverage filled:** CDP is extensively measured locally, but no BiDi feature-by-feature/browser-by-browser note appears in the held coverage map or filenames. The new matrix would keep protocol choice separate from the lane's existing evidence-rung claims.
- **Recheck:** run the lane's minimal required command/event cases on each explicitly selected browser/driver/binding version; save results with version identity and compare each claim with the current W3C/module and Selenium API references (S003, S006, S007). WPT result data remains an unopened lead, not current evidence.
- **Quality fit:** the observed API mismatch is tied to precise doc locations; the rollout recommendation is explicitly labeled inference and can be falsified by the resulting compatibility matrix.

### C3 — `playwright-accessible-locators-and-snapshots.md`

- **Falsifiable claim:** Playwright role locators use explicit/implicit accessibility semantics and can be paired with accessible names; ARIA snapshots test an accessible-tree structure, while the locator guide explicitly says role locators are not accessibility audits. Playwright 1.64 adds refs from AI-mode snapshots as a separate locator mechanism.
- **Source and location:** S011 “Locate by role”; S013 “ARIA snapshots” and “Snapshot matching”; S010 Version 1.64 “New APIs”; S014 `locator.ariaSnapshot`. Quote: “Role locators do not replace accessibility audits and conformance tests.”
- **Coverage filled:** no source/knowledge filename in the current inventory is a Playwright locator, ARIA snapshot, accessible-name, or semantic-selector guide. It extends the current `SKILL.md` state-capture/accessibility snapshot surface without treating the accessible tree as pixels or wire evidence.
- **Recheck:** on an authored fixture, assert one control by role plus accessible name, capture its ARIA snapshot, and compare it with a narrowly scoped structural expectation; confirm a separate visual/accessibility audit is not inferred from selector success. Recheck the `getByRef` addition against the pinned Playwright version (S010, S011, S013, S014).
- **Quality fit:** behavior and scope are testable; each tool-specific claim cites official docs; the non-audit limitation is explicit.

### C4 — `web-ui-dom-event-flakiness-evidence.md`

- **Falsifiable claim:** the ICST 2025 paper's studied flaky web UI cases associate flakiness with event/DOM interaction and outcome checks, and its reported repair strategies emphasize DOM synchronization and consistent state transitions. The claim is bounded to that paper's studied set, not all browser automation.
- **Source and location:** S020 abstract; §V “Common strategies and time costs”, Table V. Quote: “Ensure elements are fully loaded and visible before interaction.”
- **Coverage filled:** local Tabi already holds state-predicate waits and a network/DOM evidence ladder (`async-step-evidence.md`, `network-evidence-rung.md`); the missing addition is a curated empirical source and a failure-class taxonomy to test the local rule against, especially across DOM/event boundaries.
- **Recheck:** revisit S020 §III–V and reproduce a local loopback case only if the lane admits a fixture; record before/after state and event/network witnesses. Do not infer external-site behavior or general prevalence from the paper's sample.
- **Quality fit:** source and location are exact; sample scope is bounded; the local reproduction is a future falsifier, not claimed as already run.

### C5 — `retry-order-flake-receipts.md`

- **Falsifiable claim:** Playwright labels a test that fails once and passes on retry “flaky”; Version 1.64 provides a seedable `--shuffle` order to expose and reproduce order-dependent failures, and the trace guide supports retaining a first-retry trace.
- **Source and location:** S016 “Failures” and “Retries”; S010 Version 1.64 “Test runner”; S017 “Recording a trace”. Quote: “flaky — tests that failed on the first run, but passed when retried.”
- **Coverage filled:** existing evidence notes emphasize deterministic capture and execution closeout; no current knowledge filename explicitly covers order-dependent browser-test failures, a reproducible shuffle seed, or first-failure-plus-retry evidence.
- **Recheck:** `npx playwright test --shuffle <seed> --retries=1`; retain the first-run failure, seeded order, retry outcome, and trace from the first retry. Do not report the final green result alone.
- **Quality fit:** each failure state is defined by official docs; the seed and trace make the procedure replayable and falsifiable.

## Study paths

- **Protocol decision path:** S001 → S002 → S003 → S005 → S006 → S007. Start with the local CDP contract and its support/security limits, then read the current standard and a framework's actual binding-specific API before proposing any transport switch.
- **Accessible selector path:** S019 → S011 → S013 → S014 → S010. Learn semantic roles/names first, then use snapshots as structural evidence, inspect ref-selector behavior, and only then pin the release-specific API.
- **Flakiness investigation path:** S018 → S016 → S017 → S020 → S021 → S012 → S015. Isolate fixtures, classify retries, preserve traces, compare against empirical failure/repair research, then prefer predicate/actionability-aware waits and retrying assertions over a naked one-shot read.

## Rejected candidates and mistakes mined

### M1 — “Bless direct raw CDP as a stable, cross-browser public contract” — rejected

S001 explicitly says direct third-party CDP use is unsupported and has no backward-compatibility guarantee. Keep raw CDP as a deliberately pinned, evidenced Chromium technique where the lane needs it; do not turn the current loopback recipe into a claim of stable or cross-browser protocol support.

### M2 — “Replace every CDP capture with BiDi immediately” — rejected

The current W3C text is a Working Draft (S003); Selenium's own examples vary by binding/release (S007), and the opened materials do not establish complete command parity across browser/driver versions. Migrate only after a feature-specific matrix shows the needed capture and evidence surfaces work.

### M3 — “A longer fixed sleep is the default flake fix” — rejected

The local skill already requires state predicates. S020 reports synchronization/state-transition approaches, while S021's 2025 research record says developers often adjust durations even where the underlying cause lies elsewhere. Keep bounded timeouts as failure limits, but wait on a falsifiable state and diagnose the event/DOM transition.

### M4 — “An ARIA snapshot proves accessibility conformance” — rejected

S011 says role locators do not replace accessibility audits/conformance tests; S013 describes snapshots as accessible-tree structural templates. Use them to test declared semantic structure, not as a substitute for an audit or a rendered-pixel check.

### M5 — “A retry-pass is a reliable pass” — rejected

S016 classifies first-run failure followed by retry success as flaky. Preserve the first failure, retry record, order seed, and trace; a successful retry is diagnostic evidence, not proof that the original run was reliable.

## Recommendations for wave 2

- Add a source-backed CDP profile-isolation note and update the runbook only after checking its exact browser/version assumption; keep profile contents shape-only.
- Build a small BiDi capability matrix for Tabi's required capture commands and events; choose CDP or BiDi per evidenced feature rather than protocol branding.
- Add an accessibility-selector and flakiness recipe that combines role/name semantics, narrowly scoped ARIA snapshots, seeded order reproduction, and first-retry trace evidence while retaining Tabi's existing state-predicate and evidence-rung discipline.

## Dossier counts

Counts below are reproducible against this artifact or the lane directory:

- `21` source rows — `grep -cE '^[|]S[0-9]{3}[|]' local://kaika-w1-tabi-art.md`
- `18` tier-A rows — `grep -cE '^[|]S[0-9]{3}[|].*[|]A[|]' local://kaika-w1-tabi-art.md`
- `3` tier-B rows — `grep -cE '^[|]S[0-9]{3}[|].*[|]B[|]' local://kaika-w1-tabi-art.md`
- `0` tier-C rows — `grep -cE '^[|]S[0-9]{3}[|].*[|]C[|]' local://kaika-w1-tabi-art.md`
- `5` candidate knowledge entries — `grep -cE '^### C[1-5] — ' local://kaika-w1-tabi-art.md`
- `5` rejected approaches mined — `grep -cE '^### M[1-5] — ' local://kaika-w1-tabi-art.md`
- `1` defect found — `grep -cE '^\*\*Defect D[0-9]+:' local://kaika-w1-tabi-art.md`
