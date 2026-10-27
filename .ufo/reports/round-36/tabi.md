# tabi — round 36

## Work performed

Declared claims: **C1 adjacency** — move the lowest-scoring non-retired axis by replacing the closed-pool newMapped quota with a sourced completeness/drift/delta meter; **C2 operability** — amend and measure the Firefox WebDriver-BiDi counter at the declared 16-row threshold with pinned binaries and live egress observation. Both claims were frozen before data at `2e7b7a8920bff47fae6f75c3d06e48e37767099e`.

- C1: landed the 307-row sibling-drift ledger and method note; 16 chunk seats, an independent connector scan and the counter all report 307/307 audited, 0 findings, empty delta. Evidence: `.ufo/waves/round-36/measure/c1-at-20a69e0.json`, `w1/AdjDrift01–16/`, `w1/ConnDeltaScan/report.md`.
- C2: amended counter v2, retained the honest 16-row Firefox evidence, and ran a fresh live session at the measured revision: 16 admitted, 0 failing, 0 non-loopback egress. Evidence: `.ufo/waves/round-36/measure/c2-at-20a69e0.json`, `provenance-20a69e0.txt`, w1 `MutC2/report.md` and `CritC2/report.md`.
- Frontier/source: added sourced method entry `corpus/knowledge/adjacency-drift-audit-r36.md` citing S142, and indexed it in `corpus/README.md`; w2 `RevS142` reopened git-show with the same digest. Evidence: `corpus/SOURCES.md:156` (S142), `w1/ScribeSrcGitDocs/fetch-receipts.md`, `w2/RevS142/report.md`.
- Routed S125 defect: changed only the S125 recheck cell to `on-release`, with its receipt row, two decoded tag blobs and refetch file. Gate at the landing reads population 24 / resolved 24 / holds 17. Evidence: `f2f3f14555ec1db6d8c3a6dc9e4059ef9489b8c7`, w1 `ExecS125/report.md`, `w2/RevS125/report.md`.
- W2 falsification: 32 fresh seats attacked the counters, controls, S125/S142 landing, entry, lesson draft, census and w1 consensus. Evidence: `.ufo/waves/round-36/w2-results.json`, `.ufo/waves/round-36/w2/`.
- W2 findings (frozen artifacts left unchanged): C1 F1 pins-unbound/T8, the frozen build tool's 39-character kama pin, moved-note first-token ambiguity and live-tip relocation-note drift; C2 replace-ref reads, abnormal-SIGTERM browser cleanup and unbound `observed` receipt decoration. The canonical measured clone carries no replace refs and its predicate remains true; each hardening item is carried to round 37. Evidence: `w1/CritC1/report.md`, `w2/ExecPinsAssertion/report.md`, `w2/ExecDeltaLive/report.md`, `w2/CritC1b/report.md`, `w2/SentinelScope2/report.md`, `w2/CritC2b/report.md`.
- Incomplete w2 outputs (no verification credit; `w2-results.json` has no separate error note): `RevF1` has no report and stops at “Need only make the first mutation commit and generated-led…”; `RevC2b` returns `{"aborted":true,"error":"Still incomplete: J4/J5 fixture construction and mandatory report not complete. Scratch clone/fixture work was started but available tool execution did not finish the battery."}`; `MutC2b` returns `{"aborted":true,"error":"Need execute mutation battery in isolated scratch; still ongoing."}`; `ExecEgressLive` has no report and its last output says “Let me resolve an apparent inconsistency in my fix verification with a clean, unambiguous test.” The other 28 w2 seats have report files. All 33 w1 seat report files exist; w1 results lack parseable final verdict labels for `AdjDrift08` and `MutC2`, which `w2/CritW1Dead/report.md` records.
- w2 `RevD11`'s alleged broken replacement path is a false finding: at `f2f3f145…` both the entry and README point to `.ufo/waves/round-35/w2/SentinelDriverEgress/evidence/sockets-summary.txt`, which is 1,765 bytes; the reported `corpus/evidence/...` path is absent. Evidence: `git show f2f3f145…:corpus/knowledge/webdriver-bidi-firefox-runtime-round-35.md` lines 339–344 and `w2/RevD11/report.md`.
- Fresh-start review: read the round-33, round-34 and round-35 verifier spot-checks; the round-35 routed defects informed the frozen C1/C2 work. Evidence: `corpus/lessons/round-{33,34,35}-verifier-spotcheck.md`.
- Prompt conformance: w2 used the exact host Godspeed directive bytes after `/skill:godspeed`; w1's frozen generator used an ASCII hyphen and paraphrased the immediate-stop sentence. The w1 dispatch is not rewritten after data; this status-neutral defect is recorded in `LOG.md` under Round 36. Evidence: `.ufo/waves/round-36/w1-dispatch.json`, `w2-dispatch.json`, `skill://godspeed/directive.md`.

## Landed changes

Every change below is tied to the Round 36 `LOG.md` entry and its commit; the append-only landed-commit ledger is at `LOG.md` §“Round 36 — landed-commit ledger”.

| Change | Evidence / LOG entry | Lane commit |
|---|---|---|
| Claims/counters/controls freeze; inherited D11 correction and w1 dispatch/evidence | `LOG.md` Round 36; `.ufo/waves/round-36/claims.json` | `2e7b7a8920bff47fae6f75c3d06e48e37767099e`; `e6959879c87f2504e699c00c5e4ab869b4effb20`; `bd688fc6455add4aa1f3e13d4391ced13c4d4a46` |
| Late w1 seat evidence and complete w1 results | `LOG.md` Round 36; `w1-results.json` | `72e19a51b9679c2b2c5d050ce2a6ae7ab2ba3dd5`; `53937aa651880cf58dbd29a332bded12e26ec4d7` |
| S125 cadence + four companions, S142 and sourced method entry | `LOG.md` Round 36; w1 `ExecS125` and `ScribeSrcGitDocs` | `f2f3f14555ec1db6d8c3a6dc9e4059ef9489b8c7` |
| Validated w2 spec/ready, rendered dispatch/registry, settled results | `LOG.md` Round 36; `w2-results.json` | `12915bc33a611362324d4f66f3763002aad2e5ba`; `1ee2ab1aaee3c29681d553c3a353d6ee5c4930f1`; `badc697386896d3cbfb624fb94652e9a9e9fb4d3` |
| Post-freeze method clarification and README index row | `LOG.md` Round 36; method entry appended correction; README Round 36 row | `20a69e0ae33292a71504e40be326f1513cd5a81b` |
| Lesson, scorecard, measurement receipts and census/input-stability receipts | `LOG.md` Round 36; `corpus/lessons/round-36.md`; `SCORECARD.md` Round 36 | `410e91b75784391a14b34c780d237b6a6b5d106e`; `ac2160c771f30e7b3057d13b5813916142d02535` |
| Append-only landed-commit and w1 Godspeed-fidelity notes | `LOG.md` Round 36 | `7be129d3d2aee14e32ec5beb65878e7fcacb3813`; `354eb330f1601913e3489da91f120907252a9159` |

Final lane HEAD: `354eb330f1601913e3489da91f120907252a9159`. `jj-lane.sh state` reports `ahead=0 behind=0`; `git ls-remote origin refs/heads/master` prints the same hash.

## Before → after measurements

**C1 — adjacency (measured at `20a69e0ae33292a71504e40be326f1513cd5a81b`; counters from freeze `2e7b7a8920bff47fae6f75c3d06e48e37767099e`).**

Counting command:

```sh
node .ufo/waves/round-36/counters/c1-adjacency-sweep-v4.mjs --rev <REV> --repo <clean clone> --fleet /home/vgpnk/Projects/shokunin --json
```

Before, c1-J1 do-nothing had `auditCoverage=0/307`, `auditMissing=307`, predicate false. After: predicate true; 383 candidates, 383 screened, unaccounted 0; drift total 307, coverage 307, findings 0, classes 304 unchanged / 3 moved / 0 stale; delta total 0, unaccounted 0, screen findings 0. Scorecard records adjacency **8 → 8** (the metric moved; no numerical rubric authorized an automatic score bump). Evidence: `measure/c1-at-20a69e0.json`, `baseline/c1-J1-do-nothing.json`, `measure/pins-binding-at-20a69e0.txt` (all eight frozen digests match at REV; freeze-to-REV diffs empty).

**C2 — operability (measured at `20a69e0ae33292a71504e40be326f1513cd5a81b`; same freeze).**

Counting command:

```sh
node .ufo/waves/round-36/counters/c2-firefox-bidi-v2.mjs --rev <REV> --repo <clean clone> --json
```

Before, v2 was absent at the round-start tip. After: predicate true; population 17, admitted 16, failing 0, unmeasured 1, binding null, entry/receipt findings null; live Firefox 158.0.1 / geckodriver 0.37.1, 28 commands, 20 events, 3 samples, 0 non-loopback sockets. Scorecard records operability **9 → 9** (existing axis score held; no new capability). Evidence: `measure/c2-at-20a69e0.json`, `measure/provenance-20a69e0.txt`.

No-harm at the measured revision: 27/29 commands exit 0, including all 18 self-tests. The two nonzero commands reproduce at the baseline: `check-frontier-admission` exit 1 on unadmitted S116/S117 and the frozen `measure.sh` invocation `check-freshness --worktree --rev HEAD` exit 2 (invalid option combination). Final `check-selfassessment.mjs --rev 354eb330… --json` reads `mismatches=0`. Evidence: `measure/noharm-at-20a69e0.txt`, `measure/noharm-baseline-compare.txt`, final command output.

The frozen measurement script printed a missing-path error for its `numstat` output after `cd` into the scratch clone; C1/C2 and other receipts were produced. The exact numstat command was rerun and retained at `measure/numstat-at-20a69e0.txt`. Counter inputs are byte-identical from measured revision to final lane HEAD (`measure/measured-inputs-diff.txt` is empty); the final `SOURCES.md` is also unchanged from the census receipt revision.

## Sources & frontier

`corpus/SOURCES.md` rows: **141 → 142** (`sources-census.sh census` receipts in w2 `ExecCensusEnd/before-census.tsv` and `after-census.tsv`, both exit 0). Tier counts: A 125 → 126, B 7 → 7, C 9 → 9. Status counts: mined 117 → 118, queued 15 → 15, rejected 9 → 9. Added by tier: one tier-A mined row, S142. Existing row touched: S125 recheck `90d` → `on-release`; no other existing cell changed. Frontier advanced by the sourced method entry `corpus/knowledge/adjacency-drift-audit-r36.md`, indexed in README.

Round-start census replay (baseline `11c64b96f357de106c30a71c5e21ca44a3eacdc0`; scratch fleet checkout; exit 0) and round-end census (exact lane root at revision `410e91b75784391a14b34c780d237b6a6b5d106e`; exit 0) both report the 20 existing W04 warnings, no E-codes, and `tabi ok`. The final registry is byte-identical through lane HEAD `354eb330…`. Full outputs and exit codes are committed in `measure/census-start-rederived.txt` and `measure/census-end-final.txt`; the 141→142 count is separately evidenced by the census-mode TSVs.

Round-start output:

```text
command=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /fast/scratch/hyaku/tabi-r36/L1-census-root2 tabi (scratch fleet at round-start baseline 11c64b96f357de106c30a71c5e21ca44a3eacdc0)
tabi W04 S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi W04 S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi W04 S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi W04 S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/panels/application/WebMCPView.ts across scopes
tabi W04 S069 duplicate url developer.chrome.com/blog/webdriver-bidi-2023 across scopes
tabi W04 S070 duplicate url raw.githubusercontent.com/nodejs/node/v24.21.0/doc/api/process.md across scopes
tabi W04 S073 duplicate url github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md across scopes
tabi W04 S074 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/platform/runtime_enabled_features.json5 across scopes
tabi W04 S075 duplicate url developer.chrome.com/docs/ai/webmcp/imperative-api across scopes
tabi W04 S076 duplicate url mpapad.github.io/publications/pdfs/ICST25.pdf across scopes
tabi W04 S077 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi W04 S095 duplicate url html.spec.whatwg.org/multipage/input.html across scopes
tabi W04 S096 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S098 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi W04 S099 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/public/devtools_protocol/domains/WebMCP.pdl across scopes
tabi W04 S100 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S114 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S115 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S118 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
tabi W04 S123 duplicate url www.rfc-editor.org/rfc/rfc9309.txt across scopes
tabi ok /fast/scratch/hyaku/tabi-r36/L1-census-root2/tabi-shokunin/corpus/SOURCES.md
exit=0
```

Round-end output:

```text
command=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
revision=410e91b75784391a14b34c780d237b6a6b5d106e
tabi W04 S058 duplicate url chromewebstore.google.com/detail/webmcp-model-context-tool/gbpdfapgefenggkahomfgkhfehlcenpd across scopes
tabi W04 S065 duplicate url git-scm.com/docs/git-rev-parse across scopes
tabi W04 S066 duplicate url www.selenium.dev/documentation/webdriver/bidi across scopes
tabi W04 S068 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/panels/application/WebMCPView.ts across scopes
tabi W04 S069 duplicate url developer.chrome.com/blog/webdriver-bidi-2023 across scopes
tabi W04 S070 duplicate url raw.githubusercontent.com/nodejs/node/v24.21.0/doc/api/process.md across scopes
tabi W04 S073 duplicate url github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md across scopes
tabi W04 S074 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/platform/runtime_enabled_features.json5 across scopes
tabi W04 S075 duplicate url developer.chrome.com/docs/ai/webmcp/imperative-api across scopes
tabi W04 S076 duplicate url mpapad.github.io/publications/pdfs/ICST25.pdf across scopes
tabi W04 S077 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi W04 S095 duplicate url html.spec.whatwg.org/multipage/input.html across scopes
tabi W04 S096 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S098 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/form_mcp_schema.cc?format=TEXT across scopes
tabi W04 S099 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/public/devtools_protocol/domains/WebMCP.pdl across scopes
tabi W04 S100 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/154.0.8037.97/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S114 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S115 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes
tabi W04 S118 duplicate url github.com/ChromeDevTools/devtools-frontend/blob/66df492aaa0129d090937e933dd44c5389ab24d2/front_end/models/web_mcp/WebMCPModel.ts across scopes
tabi W04 S123 duplicate url www.rfc-editor.org/rfc/rfc9309.txt across scopes
tabi ok /home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
exit=0
```

Assimilation: none (w1 `ScoutAssim`); no `considerthese/` directory. Quarantine slice re-derived to 38 rows (37 payload-absent + unreachable S171), matching the prior hand-check set; no package rows adopted.

## Trend verdicts

- **expansion: improved** — one new knowledge entry on previously unheld adjacency drift-audit ground, citing mined S142 and indexed in README.
- **quality: improved** — the new entry's post-freeze statement was narrowed by an append-only, w2-evidence-backed correction; D11's correction pointer is valid at the committed `.ufo/waves/.../sockets-summary.txt` target.
- **discernment: unchanged** — no outside non-author admit/reject spot-check was present at lane filing; dispatched w1/w2 reviewers remain lane participants.

Stale-lane: respawn-per-round; this is the only tabi round-36 mission, and it progressed through both WAVE-DONE handoffs. No other tabi mission is open.

Tool installs/updates: none. Pacman guard respected. Open L0 questions for tabi round 36: none. The fleet misroot sweep found no tabi round-36 files at fleet root; `.ufo/l0-questions.md` was modified and `.scratch/closure-mado-r50.json` was untracked by other work, left untouched.

## SHONEN

- [~] SKILL.md decision tables, error patterns and cited sources: `SKILL.md` §§Approval table / Evidence ladder; recent method entry `corpus/knowledge/adjacency-drift-audit-r36.md`.
- [~] End-to-end domain task executed and logged: `LOG.md` Round 36; measured C1/C2 receipts under `.ufo/waves/round-36/measure/`.
- [~] Instructions executable without oral context: `corpus/knowledge/executor-test-sufficiency.md`; w1 `ExecSelftest/report.md` 18/18 self-tests.
- [~] No cross-domain bleed: `PROVINCE.md:3-21`; the adjacency ledger reports sibling ground without absorbing it.
