# kaidoku r3 — audit B: re-verification of four r2 corpus entries

Lane: kaidoku-shokunin r3 audit. Date: 2026-10-13. Host: Linux x86_64, node v24.21.0.
Package under audit: `rea-agents@6.4.0` (both npx caches `af752b90495482d7` and
`dea9475797100b20` confirmed `"version": "6.4.0"` — no package drift since r2).
Method: re-ran each file's verify commands verbatim where possible; used inline-JSON
argv and the surviving `/tmp` artifacts (`/tmp/obsidian-app-analysis.json`,
`/tmp/rea-capabilities.json`, `/tmp/rea-pe-*.json`) instead of writing new files.
Named re-checks: `record_pairs` MCP-only, Binwalk version gate, per-op `available`
vs provider `availability.status` — all three CONFIRMED (details below).

## File: corpus/knowledge/2026-10-13-r2-version-diff-compare.md

### Verify
- `npx -y rea-agents@6.4.0 compare --help` → usage `rea compare <left> <right>` only; no `record_pairs` flag. — **confirmed**
- `npx -y rea-agents@6.4.0 compare --schema --format json` → args schema `{left,right}`, `additionalProperties:false`; `record_pairs` absent. — **confirmed**
- `grep -rn record_pairs <pkg>/dist/` → hits only at `dist/domain/bundleComparison.js:21` (schema field) and `dist/server/registerBundleComparisonTool.js:24,43` (MCP tool binding). Zero hits under `dist/cli/`. — **confirmed**
- `rea compare /tmp/obsidian-app-analysis.json /tmp/obsidian-app-analysis.json` → `evidence_integrity_mismatch`/`integrity_mismatch`: "Expected an Evidence bundle with records and manifest arrays, but this JSON is one Evidence record (ev_039c8069…). Export a session bundle with the MCP export_evidence_bundle tool" — exit 1. Reproduces run-log row 5 verbatim. — **confirmed**
- `rea compare /usr/bin/expac /usr/bin/expac` (binary, non-JSON) → `evidence_integrity_mismatch`/`execution_failure`, `details.reason:"invalid-json"` — exit 1. Same refusal class as feeding TOON (run-log row 4). — **confirmed**
- `rea analyze /usr/bin/expac` (default format) → TOON-shaped output (`key:` rows). Evidence `ev_6cbf4a97fc5605…`, subject sha256 `a4ee2982…` — byte-identical to r2's expac-10-13 record ID/digest: **deterministic ID reproduction re-witnessed live**. — **confirmed**
- `rea compare-application-versions '{"left":<rea-pe-analyze binary_overview>,"right":<rea-pe-decompile procedure_pseudo_code>,…}'` (inline argv, both native records, distinct ev_ids) → `invalid_request`/`invalid_input`, `issues:[{path:["left","operation"],message:"Expected authenticated JavaScript analysis, runtime reconciliation, or managed application graph Evidence."}]` — exit 1. Reproduces row 13 verbatim. — **confirmed**
- Source spot-checks: `dist/config/ghidraStartupTimeout.js` `DEFAULT_GHIDRA_STARTUP_TIMEOUT_MS = 330_000` (line 3); `dist/config/environment.js:34` binds `REA_GHIDRA_STARTUP_TIMEOUT_MS`; `dist/domain/functionComparisonNormalization.js` `functionMatch` body at :9-25 and `isAutoName` regex at :142 (`sub_*|fcn.*|FUN_*`) — exactly as cited. — **confirmed**

### Verdict audit
- **`record_pairs` is MCP-only: VERDICT HOLDS.** CLI surface exposes only `<left> <right>`
  (help + JSON schema); the field exists solely in the domain schema and the MCP server
  registration. No CLI path to `record_pairs` in 6.4.0 — the headline claim stands exactly.
- **compare-application-versions refuses native records: VERDICT HOLDS.** Typed refusal at
  `left.operation` reproduced with two real native records from `/tmp`.
- **TOON-default / invalid-json / single-record rejections: VERDICT HOLDS.** All three
  envelope shapes re-witnessed.
- Minor imprecision (non-fatal): cited file `javascriptApplicationVersionComparisonSchemas.js`
  actually lives at `dist/domain/javascript/` (not `dist/domain/`); content matches
  (`compareApplicationVersionsInputSchema` = two `evidenceSchema` + native-observation
  arrays + superRefine). The error string itself lives in
  `dist/application/javascript/JavaScriptApplicationEvidenceGraph.js:51`.
- Not re-run (cost): the 330 s `provider_timeout` on the 41 MB Go binary, live
  `compareFunctions` 8-dim diffs, `--snapshot` accumulation. Env knob and default constant
  confirmed in source; the live long-running repro is unchanged-risk — verdicts on those
  candidates rest on r2's own run log plus confirmed source cites.

## File: corpus/knowledge/2026-10-13-r2-firmware-probe.md

### Verify
- `file /usr/lib/firmware/nvidia/610.57.04/*.bin` → `ucodes_*.bin` = `data`; `gsp_*.bin` = `ELF 64-bit LSB relocatable, UCB RISC-V, soft-float ABI, not stripped`. `pacman -Qo` → all owned by `nvidia-utils 610.57.04-1`. `head -c 8 ucodes_tu10x.bin` → `NVUCODES`. — **confirmed**
- `rea inspect-firmware-regions ucodes_tu10x.bin --format json` (env unset) → `capability_unavailable`/`unsupported_provider`, `provider_id:"binwalk"`, "requires Linux and an absolute REA_BINWALK_COMMAND" — exit 1. — **confirmed**
- `REA_BINWALK_COMMAND=true` → identical absolute-path refusal. `REA_BINWALK_COMMAND=/nonexistent` → `ENOENT … realpath '/nonexistent'`. — **confirmed**
- `REA_BINWALK_COMMAND=/bin/true` → version gate: "Unsupported tool version true (GNU coreutils) 9.11 …; accepted releases are Binwalk 3.1.x (verified with 3.1.0)". — **confirmed**
- `rea extract-firmware ucodes_tu10x.bin /tmp/x` → `capability_unavailable`, `provider_id:"unblob"`, `operation:"extract_firmware"` — exit 1. `REA_UNBLOB_COMMAND=/bin/true` → "accepted releases are Unblob 26.6.x (verified with 26.6.4)". — **confirmed**
- `extract-firmware … --offset 16` (no `--length`, unblob env unset) → `invalid_request`/`invalid_input`, retryable:true — validation fires before any provider gate. — **confirmed**
- `rea analyze gsp_tu10x.bin` → `target_unavailable`/"unsupported ELF architecture" — exit 1; `rea analyze ucodes_tu10x.bin` → `target_unavailable`/"unsupported binary format" — exit 1. ELF fallback closed. — **confirmed**
- `rea doctor --format json` → `providerInspections` = `["ghidra","ida"]` exactly. `command -v binwalk unblob` → both absent. — **confirmed**
- `rea providers --format json | grep -i firmware` → **NOT empty** (see audit). — **drifted (as written)**

### Verdict audit
- **Binwalk version gate: VERDICT HOLDS.** Banner-parse gate reproduced exactly
  (`true (GNU coreutils) 9.11` → "Binwalk 3.1.x (verified with 3.1.0)"), plus the
  absolute-path and ENOENT rungs of the env contract.
- **Unblob gate + arg-validation ordering: VERDICT HOLDS.** Provider gate precedes
  filesystem effects; schema validation precedes the provider gate.
- **doctor/providers blind spot: VERDICT HOLDS in substance — its verify command is
  defective.** `capabilities[]` contains zero firmware ops and doctor inspects only
  ghidra+ida — the real claim. But `providers --format json | grep -i firmware` returns a
  match on this same version: the envelope embeds `server_identity.catalog.tools[]` whose
  surface tags include `firmware-provider` (2 entries — r2's own matrix file lists that
  histogram). The r2 "→ empty" verify expectation is falsified as written; the conclusion
  (no firmware capability/host op visible) remains true. Corrected verify: enumerate
  `capabilities[].operation` (zero firmware — re-run shows 0/18).
- All typed envelopes, exit codes, and the `capability_unavailable` vs r1's
  `provider_unavailable` code distinction re-witnessed unchanged.

## File: corpus/knowledge/2026-10-13-r2-asar-deep-obsidian.md

### Verify
- `sha256sum /usr/lib/obsidian/app.asar` → `8588f1fd23c9…416c52`, 480,052 B — matches claim. — **confirmed**
- Full census re-run on surviving `/tmp/obsidian-app-analysis.json` (12,367,708 B): `evidence_id ev_039c8069…`, `subject.digest.sha256 = 8588f1fd…52`; graph 170 nodes / 221 edges with the exact kind histogram (javascript-module 90, asar-entry 27, javascript-asset 19, ipc-channel 15, artifact 7, package 5, ipc-handler 2, native-export 2, native-addon 2, electron-main 1) and relation histogram (imports 76, contains 53, exposes 46, maps_to 28, sends 13, loads 3, handles 2); semantic_graph 6,710 nodes / 6,344 relations; 1,995 unknowns split object-flow 820 / data-flow 637 / call-flow 515 / promise-ownership 17 / event 6; statistics `findings:135, modules:0, parsed_javascript_files:19, visited_ast_nodes:9464`. Every number reproduces. — **confirmed**
- IPC census: 17 `ipc-channel`/`ipc-handler` nodes, all under `@electron/remote`. — **confirmed**
- main.js ambiguity census: exactly **19** `javascript-module` nodes carry `main.js` somewhere in their identity/observation payload (1 `source-module` + 18 unresolved-reference/semantic nodes) — count matches r2. — **confirmed**
- `rea analyze-javascript-application --schema` → args `path` only; options `maxHeapMb/analysisTimeoutMs/artifactFormat/integrityPolicy`; **no `detail` option**. `rea inspect-analysis-view --schema` → `inputJson` only. — **confirmed**
- `rea inspect-analysis-view '{"source":{"kind":"retained-evidence","evidence_id":"ev_039c8069…"},"view":{"kind":"summary"}}'` (inline argv) → `evidence_integrity_mismatch`/`integrity_mismatch`: "Evidence ev_039c8069… is not retained in this session…" — exit 1, verbatim. — **confirmed**
- Source: `dist/domain/analysisView/analysisView.js` — `analysisViewSourceSchema` = discriminatedUnion `retained-evidence` (`ev`-prefixed digest) | `inline` (`evidenceSchema`), ~lines 98-107. — **confirmed**

### Verdict audit
- **End-to-end analysis + census claims: VERDICT HOLDS** — every statistic, histogram, and
  digest re-derived from the surviving sealed Evidence; artifact sha256 independently
  re-measured.
- **`retained-evidence` is session-scoped: VERDICT HOLDS**, reproduced via inline JSON.
- **No `detail` flag on CLI: VERDICT HOLDS** — schemas re-dumped.
- New nuance (refines, does not contradict): `inputJson` must be a *regular file* or an
  inline JSON string — `/dev/stdin` is refused with a typed `invalid_request`
  (`"The JSON input must be a regular file (ENOTFILE)"`). The r2 phrasing "passed as a JSON
  file path" is correct; future lanes should also know inline argv works for small inputs
  and pipes do not.
- Not re-run (cost): the ~280 s `analyze-javascript-application` execution itself (sealed
  output preserved and re-censused instead), the live `selector.path:"main.js"` ambiguity
  error (its census predicate — 19 candidates — confirmed; re-running the verb needs a
  workflow file, which this lane may not create), the page-cursor walk.

## File: corpus/knowledge/2026-10-13-r2-provider-capability-matrix.md

### Verify
- `cmp <(rea providers --format json) <(rea capabilities --format json)` → differ at byte **76335** (r2 recorded 76332); deep field-diff of r2's saved `/tmp/rea-capabilities.json` vs a fresh `providers` payload shows **only** `server_identity.server.started_at` differs (`15:19:20.229Z` → `15:45:16.991Z`). — **confirmed** (byte offset drifted 3 bytes — layout position of the timestamp field; substance identical)
- Envelope top-level keys → exactly the 8 claimed (`open, capabilities, analysis_provider_binding, analysis_provider_candidates, analysis_run, analysis_activity, provider_operation_health, server_identity`); no-target state `open:false`, binding/run/health `null`, `analysis_activity.status:"not_observed"`. — **confirmed**
- Host op matrix → 18 ops, same 8 `available:true` (`availability_code:null`), same 10 `unsupported_host`; zero `mutates_artifact`/`requires_root`/`changes_permissions` across all 18. — **confirmed**
- `analysis_provider_candidates` → 3 entries: `ghidra available` (28 ops), `hopper unavailable executable_missing` (36), `ida unavailable not_configured` (12). — **confirmed**
- Per-op `available` flag count per provider → 28/28, 36/36, 12/12 `available:true` even for the two unavailable providers. — **confirmed** (named re-check)
- `rea inspect-binary-layout /usr/bin/jq` → `provider_unavailable`/`unavailable`, `retryable:true`, `candidate_ids:["pwntools-elf"]`, REA_PWNTOOLS_PYTHON remediation (pwntools 4.15.0 + pyelftools 0.33 + Unicorn 2.1.2) — exit 1. — **confirmed**
- `rea list-adb-devices` / `rea inspect-adb-client` / `rea inspect-jeb-client` → `capability_unavailable`/`unsupported_provider` with the recorded remediations — **but exit 1, not 0.** — **drifted**
- `server_identity` → `rea-agents@6.4.0`, `rea 6.4.0`, sdk `{2.3.1}³`, skill expected_version `37`, `build_commit:null`, `catalog.counts {cli_commands:127, mcp_tools:170, mcp_prompts:6}`; digests `tools_sha256:25802f6d…1166`, `prompts_sha256:5296f030…c7a2`, `combined_sha256:85d80276…d72a`; surface histogram identical on all 14 surfaces. — **confirmed**

### Verdict audit
- **Per-op `available` vs provider `availability.status`: VERDICT HOLDS** — the named
  re-check confirms all ops report `available:true` inside unavailable providers; the gate
  is provider-level status, exactly as claimed.
- **One-envelope-two-verbs, no-target nulls, 8-of-18 host matrix, 3-candidate registry,
  7-provider-id inventory, catalog digests/histograms: VERDICTS HOLD** — all values
  re-measured identical.
- **`capability_unavailable` exit-code claim: DRIFTED / likely mis-recorded in r2.** The
  matrix table marks adb/apktool/jeb probes "fail (exit 0)" and the taxonomy nuance states
  "`capability_unavailable` exits 0; `provider_unavailable` exits 1". Re-runs give
  **exit 1 for all three capability_unavailable probes** (and every firmware verb in file 2
  also exited 1 for the same code — r2's own firmware doc says exit 1). Reality on 6.4.0:
  both typed classes exit 1; the live differentiators are `code`/`category`/`retryable`
  (`capability_unavailable` retryable:false vs `provider_unavailable` retryable:true), not
  the exit status. The corpus claim should be corrected.
- Minor imprecision (non-fatal): the digest triple lives at `catalog.digests.*`, not flat
  `catalog.tools_sha256` as the prose implies; values are byte-exact.
- cmp byte-offset claim (76332) is now 76335 — cosmetic layout drift, finding intact.

## Summary

- **Named re-checks: 3/3 hold.** `record_pairs` is MCP-only (CLI `compare` exposes only
  `left`/`right`; schema field exists solely in `bundleComparison.js` + the MCP server
  registration). The Binwalk version gate parses `<cmd> --version` and pins "3.1.x
  (verified with 3.1.0)" — reproduced with `/bin/true`. Per-op `available:true` is declared
  capability only — hopper/ida report all ops available while `availability.status` is
  `unavailable`; effective coverage stays ghidra's 28 ops.
- **Files 1–3: all verdicts confirmed end-to-end**, including verbatim typed-error text,
  deterministic evidence IDs (`ev_6cbf4a97` regenerated live on expac-10-13), and every
  census number of the Obsidian evidence re-derived from the preserved artifact.
- **File 4: one real defect** — "`capability_unavailable` exits 0" is wrong; it exits 1
  (same as `provider_unavailable`). The distinguishing field is `retryable`
  (false vs true), not exit status. Recommend a small LOG/corpus correction noting the
  exit-code column of the adb/apktool/jeb table rows.
- **File 2: substance holds; one verify command defective** — `providers | grep -i firmware`
  is non-empty because the envelope embeds `catalog.tools[]` surface tags
  (`firmware-provider`); the true claim (0 firmware ops in `capabilities[]`, invisible to
  doctor) is confirmed. Recommend replacing that verify with an op-name enumeration.
- **Minor citation imprecisions** (non-blocking): digest triple lives under
  `catalog.digests`; `javascriptApplicationVersionComparisonSchemas.js` sits under
  `dist/domain/javascript/`; cmp offset 76332→76335.
- **New operational nuance discovered while auditing:** workflow `inputJson` arguments must
  be regular files or inline JSON strings — `/dev/stdin`/`/dev/fd` pipes are refused with a
  typed `ENOTFILE` `invalid_request`. Worth propagating to the CLI playbook.
- Audit constraint note: this lane may write only this file, so verify commands requiring a
  real workflow input file (paging chain, path-selector ambiguity error) were re-verified
  at their predicates instead of re-executed; every other verify ran live. No files
  modified, nothing committed.
