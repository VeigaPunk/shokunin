# kaidoku-r5 audit lane A — adversarial re-verification of three r4 corpus entries

Audit host: same machine as r4 (node v24.21.0, npx 11.19.0, chromium 152.0.7977.82,
/usr/lib/electron39 + /usr/lib/electron43 v43.6.0). REA invoked as
`npx -y rea-agents@6.4.0` (no `rea` on PATH — dispatch note correct).
Scratch root `/tmp/r5-audit/` (lane-specific r4 /tmp dirs were removed; all inputs
re-synthesized per the recipes). No files written outside this report; all spawned
test processes (chromium :9222, http.server :8878, node --inspect :9229/:9230,
xvfb electron) killed and ports verified closed.

Legend: CONFIRMED = observed matches claim; FAIL = observed contradicts claim;
UNVERIFIABLE = cannot re-run or no evidence either way. Sha256 pins checked first —
all pins match, so comparisons below are against undrifted targets.

---

## FILE 06 — `corpus/knowledge/2026-10-13-r4-06-1password-asar.md`

## Verdict: HOLDS (one wording erratum, two cosmetic deltas)

### Sha256 pins — all CONFIRMED verbatim

| artifact | claimed | observed |
|---|---|---|
| `app.asar` | `769e0962…31e2d21`, 40,708,328 B | `769e0962f9092909ebba96a2c406bd859427a0777fc3b7156f4c19f3d31e2d21`, 40,708,328 B ✓ |
| `index.node` | `1cb3e361…fa7778`, 187,997,016 B | `1cb3e361ae85c304544d7b9b063e5eacec4f20c7009ce504e8f93f4d48fa7778` ✓ |
| `CREDITS.html` | `6ef045b5…d2ad4`, 593,734 B | `6ef045b554b28959c22b856296456e4722d1a78ed49fe11d8186a58bca6d2ad4` ✓ |
| `main.js` | `b4b5d16f…`, 236,724 B | `b4b5d16f447d…0963`, 236,724 B ✓ (also REA `entry_sha256`) |
| `preload.js` | `7e7a6888…`, 2,994 B | `7e7a6888935a…bfbd`, 2,994 B ✓ |
| `package.json` | `9ef1fe85…aedd` | `9ef1fe8585b3…aedd` ✓ |
| version | `8.12.42-32.BETA` | `1password --version` → same ✓ |

### Re-run results per claim

- **C1 census — CONFIRMED with one erratum.** Re-extracted asar: 415 `.js`,
  6 `.html`, 5 `.css`, 3 `.woff2`, 22 `.svg`, 20 `.png`, 6 `.ico`, package.json,
  LICENSE.txt, index.node — every count matches. `webpackChunk_1password_oph`
  present; 407 `/N.js` numbered chunks ("~400 lazy chunks" ✓). Re-ran the full
  REA `analyze-javascript-application` (fresh 59,167,198 B evidence): statistics
  block is **byte-identical** — relevant_files 423, parsed_javascript_files 415,
  visited_ast_nodes 1,712,317, findings 3997, modules 1311, parse_failures 0,
  text_bytes_read 16,168,007. `entry_sha256` ×423 present; main.js/preload.js/
  index.node/CREDITS hashes all match disk sha256s.
  - **ERRATUM (minor):** "asar holds 423 inventory files" conflates REA's
    `relevant_files:423` with archive membership — the asar actually lists 480
    file entries (486 list lines − 6 dirs). The entry's own extension census
    sums to 480; the 423 figure is REA's relevant-file subset (415 js + 6 html +
    package.json + LICENSE.txt). Substance unaffected.
- **C2 — CONFIRMED.** `require("./index.node")` present; `gql_invoke`,
  `gql_create_channel`, `gql_subscription_send`, `complete_future`, `localize`,
  `get_resource`, `webauthnSign`, `protect_process_memory`,
  `should_disable_seccomp`, `dev_tools_enabled`, `send_crash_reports` all found.
  `invoke({type:"…"})` literals: **59 unique** (claim: ≥59). `nm -D
  --defined-only index.node` → **27 dynsyms** incl. `napi_register_module_v1` +
  `rust_u2f_mgr_register`; ELF DYN x86-64 not stripped, BuildID `ac08c3a1…b43` ✓.
- **C3 — CONFIRMED.** `app.asar.unpacked/` = exactly index.node + CREDITS.html.
- **C4 — CONFIRMED.** webPreferences verbatim: `preload:…preload.js,
  nodeIntegration:!1, contextIsolation:!0, sandbox:!1→!0,
  disableBlinkFeatures:"Auxclick", devTools:a().dev_tools_enabled()`;
  `Mr.app.enableSandbox()` ×1 global; identical CSP meta in all 5 renderer HTMLs
  (primary/secondary/quickAccess/authPrompt/passkeyPrompt). Nuance: a 6th HTML
  (`CREDITS.html`, in the unpacked dir) carries no CSP meta — claim's "every
  shipped HTML" is accurate for the 5 window HTMLs it enumerates; noted only for
  completeness (CREDITS is not a webPreferences window target).
- **C5 — CONFIRMED verbatim.** `Mr.protocol.handle` http/https/ws/wss (default
  session) + `n.protocol.handle` http/https/ws/wss (persist:1password partition)
  = 4 schemes × 2 sessions; `session.protocol.handle` resource + file-icon;
  `registerSchemesAsPrivileged` verbatim `{bypassCSP:!0,supportFetchAPI:!0,
  standard:!0}` ×2; `fromPartition("persist:1password",{cache:!1})` ✓.
- **C6 — CONFIRMED (headline checks verbatim).**
  - `rpc.handle("…")` literals: **80 unique** ✓ (claim: 80).
  - `file://` prefix gate: verbatim `if(e.senderFrame){if(e.senderFrame.url
    .startsWith("file://"))return t(e,...n);throw \`unknown RPC user…\`` inside
    class `ba.handle` wrapping every registration; `'unknown RPC user'` ×1. ✓
  - Preload gate verbatim: `"file:"===window.location.protocol&&
    e.contextBridge.exposeInMainWorld("op",…)`; allowlist `n` = **exactly 84**
    `:!0` keys (claim "~84") ✓; `invoke:(n,...t)=>e.ipcRenderer.invoke("invoke",
    n,...t)` ✓; literal channels invoke/executeGql/gqlSubscriptionRequest/
    gqlSubscriptionResponse/SendPendingEvent/CoreLog.
  - REA summary (re-run): `context_bridge_apis:1` (`api_key:"op"`,
    `world:"main"`, `api_status:"dynamic"`), `ipc.operations:10`
    (renderer_transmissions:7 + renderer_listeners:3 = invoke×3+send×4+on×3),
    `literal_channels:6`, `sender_validation_observations:1` — all verbatim ✓.
  - Delta: main→renderer unique literal `.send("…")` channels observed = **35**
    (claim "~40"); all 9 named examples present (gqlSubscriptionResponse,
    SendPendingEvent, UnlockWithSso, ShowToastNotification, InitialAuthPromptData,
    InitialPasskeyPromptData, ImportLoginSso, DuoMfaTimeout, EmbeddedAuthFallback).
    Approximation, not falsification.
- **C7 — CONFIRMED verbatim.** `handle("invoke",((e,t,n)=>this.core.invoke(
  {type:t,content:n}))` — renderer supplies type+payload; `executeGql`→
  `core.executeGql`; `secureCopy`→`SecureCopy` direct path present (×11
  SecureCopy refs).
- **C8/C9/C10/C11 — CONFIRMED.** will-attach-webview, will-navigate,
  setWindowOpenHandler, preventDefault×3 all present; openExternal allowlist
  strings https/http/onepassword/onepassword8/mailto/x-safari-https + "URL does
  not have a valid protocol" ✓; `new tc.Command`, `arguments("[url]")`, usage
  "[options] [url] …onepassword://", second-instance×2, open-url, open-file,
  captureUrl×13, captureUrlFromClipboard, ClassifyAppUrl ✓; permission handlers
  verbatim `i("media"===n&&e===t?.getURL())` and `"video"===o.mediaType&&(…)`;
  `getCameraAccessStatus`→`"granted"` unconditional ✓.
- **C12/C13/C14/C15 — CONFIRMED.** downloadHtmlAsImage hidden-window body
  verbatim (show:!1, contextIsolation:!0, `data:text/html;charset=utf-8,`+
  encodeURI(renderer arg), capturePage→`wifiQrCode.png`→writeFileSync→
  shell.openPath→close); saveContentToFile/showSaveDialog×4/openPath×4/
  showItemInFolder/profile.pb/dotEnv handlers present; single appendArgument
  `--disable-seccomp-filter-sandbox` immediately before `enableSandbox()`, zero
  appendSwitch; protectProcessMemory×3, setCurrentProcessAumid, crashReporter→
  crashDumps, send_crash_reports, setSecureInput, AppExpired — all present.
- **C16 — CONFIRMED in substance, two numeric deltas.**
  - `integrity_contradictions:[]` ✓; `browser_windows:0`/`main_handlers:0` false
    negatives reproduce in the fresh run ✓; parent budget limit verbatim
    `javascript_analysis_parent_result_budget_bytes` = 2,069,092,508 (~2 GB);
    all 8 named files (main.js, preload.js, vendors.js, 5 renderers) carry
    resource-constraint limitations incl. vendors.js "Owned JavaScript worker
    exhausted its heap" (8 GiB claim ✓); async-chunk self-edge ×1 ✓.
  - Delta 1: top-level `limitations[]` observed = **288 entries** (277
    budget-class; 413 nested "Resource constraint" occurrences incl. doubled
    prefixes) vs claimed "≈560". Under any counting basis I can reproduce the
    figure lands ~½ of 560 — likely a different counting method or r4-era run
    variance. Immaterial to the claim (budget exhaustion proven verbatim).
  - Delta 2: graph nodes 3,058 vs 3,059; edges 6,133 vs "6,135+" (−1/−2,
    trivial). Semantic graph exact: 24,254 nodes / 26,867 relations ✓.
  - Schema nuance: no top-level `coverage` field in this output shape;
    `coverage.status:"partial"` lives per-observation on the big-bundle nodes.
    The claim's wording is loose but the mechanism it describes is verbatim real.
- **C17 — CONFIRMED.** package.json `@1password/oph@8.12.42-32.BETA`, main
  `./main.js`; react ^19.1.0, @apollo/client ^3.13.8, redux, immer,
  react-router-dom ^6.23.0, jsqr, @lingui (catalog), motion, @dnd-kit/core,
  commander ^7.2.0, @1password/lexical-editor + @1password/* workspace deps ✓.

### Defective/weak verify recipes (file 06)
None blocking. The `verify:` greps are reproducible; the only impractical piece
is the 20-min full REA run — re-ran it anyway (~3 min warm cache), all headline
numbers reproduced.

---

## FILE 07 — `corpus/knowledge/2026-10-13-r4-07-jsc-bytecode.md`

## Verdict: HOLDS (two small numeric deltas; one recipe ordering caveat)

### Sha256 pin — CONFIRMED
Re-extracted `atom.compiled.dist.jsc` (fresh `/tmp/r5-audit/jsc-probe`):
`6a0cb7b32270498ed190c589ca29c990a0e4b5f06f0cd6a5516e19a715c2dfe9` ✓,
388,080 B of 390,514 B asar (99.376% ≈ claimed 99.38%) ✓, `file`→`data` ✓.
`/usr/share/typora/version` = `42.2.0` ✓.

### Re-run results per claim

- **Header/strings — CONFIRMED verbatim.** First 32 B match byte-for-byte
  (`c3 06 de c0 11 2c 84 76 de 9f 03 00 99 0e 36 24 cb ff b0 33 d0 eb 05 00`);
  magic 0xC0DE06C3. `strings -a -n 6` = 2,187 ✓; all 10 named strings present
  (__webpack_modules__, __webpack_require__, ipcMain, BrowserWindow, addLicense,
  abnerworks.Typora, checkForUpdates, autoHideMenuBar, `REG IMPORT "`,
  "A required module cannot be loaded by Typora"). Python histogram: entropy
  6.2911 bits/B, 256/256 byte values, 0x00 ×82,829 — all three exact ✓.
- **REA typed refusal — CONFIRMED verbatim.** `npx -y rea-agents@6.4.0
  analyze-javascript-application <jsc>` → **exit 1**, `error: JavaScript
  application analysis failed`, `code/category: unsupported_target`,
  `retryable: false`, message "accepts only a directory or an .asar file",
  remediation verbatim. `--llms` grep: exactly ONE bytecode-adjacent verb
  (`inspect-evm-interface`, EVM), zero `jsc|bytenode|asar` matches ✓.
- **Host-node rejection — CONFIRMED verbatim.** Host node v24.21.0 =
  V8 13.6.233.17-node.53; live `createCachedData()` magic `0xC0DE0689` ≠ file's
  `0xC0DE06C3`; full loader recipe (flag-hash patch bytes 12–16 from live dummy,
  237,534-char ZWSP dummy source, `new vm.Script(src,{cachedData})`) →
  `cachedDataRejected = true` ✓.
- **launch.dist.js recipe — CONFIRMED verbatim.** 1,383 B; contains
  `v8.setFlagsFromString("--no-lazy")`/`"--no-flush-bytecode"`,
  `setFlagHashHeader` copying dummy bytes 12–16, `getSourceHashHeader` reading
  bytes 8–12 LE, `'"'+"\u200b".repeat(r-2)+'"'` dummy source,
  `Module._extensions[".jsc"]` (+`.cjsc`), `vm.Script(…,{cachedData})`,
  `require("./atom.compiled.dist.jsc")`. Patches ONLY the flag hash ✓.
- **V8 three-way pin — CONFIRMED.** `/usr/share/typora/version`=42.2.0; Typora
  ELF contains literal `14.8.178.14` (×2); jscd v0.1.0 (freshly downloaded from
  the same GitHub release URL) `info` output is verbatim: version_hash
  0x76842c11, source_hash 0x00039fde (237,534 B, non-module), flag_hash
  0x24360e99, ro_checksum absent, payload offset 24, `v8: 14.8.178.14 (brute
  left-fold, V8 ≥ 12)`, `supported: no (tables cover Node 8.0.0-26.10.0 /
  V8 5.8-14.6)` ✓.
- **Typora ignores ELECTRON_RUN_AS_NODE — CONFIRMED.** Bounded re-run emitted
  the same `--ozone-platform=wayland` Vulkan error and never executed the `-e`
  payload (no stdout marker; process hung, killed) ✓.
- **electron@42.2.0 run-as-node — CONFIRMED.** `process.versions` →
  `v8:"14.8.178.14-electron.0"`, node `24.15.0`, electron `42.2.0` — exact.
  Live dummy magic `0xC0DE06C3` = file magic. Plain recipe →
  **`cachedDataRejected = false`** ✓ (blob deserializes).
- **`--print-bytecode` disasm — CONFIRMED with delta.** With the flag set
  correctly: 531,851 B dump, `cachedDataRejected=false`, **115**
  `[generated bytecode for function: …]` blocks vs claimed 530,020 B / 116 —
  +0.35% bytes, −1 block. Run-to-run nondeterminism range; substance (full
  Ignition read via one npx line) holds; disasm contains app-path SFIs with
  source positions.
- **npm probes — CONFIRMED.** bytenode@1.7.0 ✓, wakaru@1.14.0 ✓; v8-disasm,
  bytenode-decompile, unjsc, v8-bytecode, jsc-decompile all E404 ✓.

### Defective verify recipe (file 07) — ordering caveat, not a result error
The verify line `<loader recipe + --print-bytecode>` is **order-sensitive and
underspecified**: `--print-bytecode` must be passed to
`v8.setFlagsFromString` **before** the flag-hash dummy `createCachedData()` is
produced (the flag hash covers V8 flag state). If --print-bytecode is set after
the dummy (natural reading order), the patched hash no longer matches the
runtime flags and you get `cachedDataRejected = true` plus a small 167,759 B /
30-block disasm of the fallback-compiled dummy — i.e., a false-negative
reproduction. I hit this on my first attempt. The report's published numbers
are correct; the recipe needs the ordering note for a future lane to reproduce.

---

## FILE 08 — `corpus/knowledge/2026-10-13-r4-08-observe-verbs.md`

## Verdict: HOLDS (one environmental nuance on the control probe)

Environment re-synthesized: chromium headless `--remote-debugging-port=9222`
(still `Chrome/152.0.7977.82`, CDP 1.3 — exact match to claim), python
http.server on :8878, `node --inspect=0.0.0.0:9229` on a real file, plus a
`node --inspect=0.0.0.0:9230 -e` sibling for the unsupported-location leg.
All six verb names confirmed via `rea --llms`.

### Re-run results per candidate

- **observe-web-session — CONFIRMED verbatim.** `--observation-ms 2500
  --format json` → predicate `rea.web-observation-session`, provider
  `rea-cdp-browser` v2; echoed `allowed_origins:["http://127.0.0.1:8878"]`
  (self-scoped from target origin — claim's core assertion ✓);
  `requested_ms:2500`, `end_reason:"window_elapsed"`; timeline = 5 lifecycle
  events commit→domcontentloaded→load→networkalmostidle→networkidle;
  `completeness.status:"attach_limited"`,
  `attach_limited_sections:["timeline"]`, `dropped_events.total:0`; limitation
  verbatim "An out-of-policy destination ends collection immediately and is
  recorded without its URL." ✓
- **observe-web-execution — CONFIRMED verbatim.** `allowed_origins:[]` (no
  self-scope — asymmetry confirmed); `coverage.state:"captured"`,
  `offset_units:"utf16-code-units"`, `end_offset:"exclusive"`, `scripts:[]`,
  `script_inventory.main_document_scripts:0`,
  `script_inventory.coverage_absence:"unknown"`; instrumentation object
  **byte-identical** (`resets_execution_counters:true,
  disables_optimized_execution:true, takes_one_resetting_sample:true,
  executes_selected_code:false, cleanup:"confirmed", page_ownership:"external"`);
  `rea_progress` 1/2→2/2 on stderr ✓.
- **list-javascript-runtime-targets — CONFIRMED verbatim.** On the `-e`
  inspector: `targets:[]`, `excluded:{unsupported_location:1,unconnectable:0}`.
  On the real file: `targets:[{protocol_type:"node",attached:false,
  location:{kind:"file",file_path:"/tmp/r5-audit/app/main.js"}}]`, excluded
  0/0; runtime `node.js/v24.21.0`, protocol `1.1`, provider `rea-v8-inspector`
  v1 ✓. The `file://`-must-stat binding rule reproduces exactly.
- **observe-javascript-runtime — CONFIRMED.** predicate
  `rea.javascript-runtime-observation`, provider `rea-v8-inspector` v1;
  `runtime_kind:"node"` + `runtime_kind_authority:"caller-declared-unverified"`;
  `events_observed:83, events_retained:83, events_dropped:0` — same count;
  `metadata_bytes_retained:62,202` vs claimed 62,210 (−8 B, context-name/pid
  length — trivial); `truncated:false`; scripts 82 = 81 `node:` builtins
  (`kind:"builtin"`) + main.js (`kind:"file"`); execution_contexts
  `[{name:"node[<pid>]",state:"created"}]` ✓.
- **reconcile-javascript-runtime — CONFIRMED verbatim.** Built live static
  layer (`analyze-javascript-application` on a fresh `/tmp/r5-audit/app`) +
  file-root runtime_mapping + the runtime-observation Evidence above →
  predicate `rea.javascript-runtime-reconciliation`, provider
  `rea-javascript-runtime-reconciliation` v1. Summary **field-identical**:
  `{runtime_targets:1, runtime_scripts:82, matched:1, ambiguous:0, unmatched:1,
  unknown:81, static_loaded:1, static_resident:1}`. Matched script:
  `basis:"artifact-path"`, `reason:"unique-location-match"`,
  `confidence:"medium"`; runtime target entity `unmatched`
  (`entity_kind:"target"`); 81 builtins `unknown`; static_load_states
  `loaded`/`resident-in-loaded-asset` with `runtime-script-correspondence`
  reason; `coverage.status:"partial"`, omitted counts 0 ✓.
- **capture-electron-scenario — CONFIRMED verbatim.** Minimal self-owned app
  (package.json+BrowserWindow main+index.html) against `/usr/lib/electron43/
  electron` (v43.6.0 — the version the report names) under `xvfb-run -a`,
  action `[{step_id:"w1",kind:"wait",duration_ms:500}]` with
  `args:["--no-sandbox","--disable-gpu"]` → **exit 1** with a refusal
  **byte-identical** to the claim: `code:"cleanup_incomplete"`,
  `category:"execution_failure"`, message "…owned Electron lineage was
  unavailable; helper cleanup was not proven…", `retryable:false`,
  `details:{operation:"capture_electron_scenario", reason:"cleanup_failed",
  cleanup:"incomplete", resources:["owned_process_group","run:<uuid>",
  "process-group:<pid>"], cleanup_reason:"…", execution_failure:
  "unreadable_output"}` ✓. No stray electron/Xvfb processes afterward.
- **Control-probe nuance:** on this host the manual `xvfb-run -a electron43
  <app> --no-sandbox` stays up (timeout-killed, healthy); **with
  `--disable-gpu` added it FATALs on "GPU process isn't usable"** — r4's
  control reportedly stayed up with both flags. Environmental delta (xvfb GPU
  path), not a claim falsification: the substantive point — refusal is
  provider-internal, not app/binary failure — holds, since the app launches
  fine without --disable-gpu and the refusal names lineage/cleanup, not launch.
- **Verb inventory — CONFIRMED.** `rea --llms` exposes exactly the six names;
  the dispatch's stale guesses (`list-javascript-runtime`,
  `list-observe-javascript-runtime`) remain absent.

### Defective verify recipes (file 08)
None. The per-verb `--format json` envelopes reproduce; only the transient
target IDs and my re-synthesized `/tmp` paths differ from the r4 artifacts, as
expected.

---

## Cross-file notes for the parent agent

- All sha256 pins held → comparisons are against undrifted targets.
- Worst deltas found: file 06 "asar holds 423 inventory files" (should read
  "REA inventoried 423 relevant files of 480 archive members"); file 06
  "limitations ≈560" (reproduced as 288 entries / 413 nested occurrences — pick
  a counting basis or soften to "~280"); file 07 function-block count 115 vs
  116 and disasm 531,851 vs 530,020 B (nondeterminism band); file 07's
  disasm recipe needs the `--print-bytecode`-before-dummy ordering note.
- Nothing rises to REFUTED. Every admit-verdict and the hold-as-refused
  classification on `capture-electron-scenario` are sound on this host today.
