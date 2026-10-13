<!-- r4 AUDIT lane A — re-verifies round-3 corpus entries by re-running their
     verify commands. Debug-port endpoints were NOT relaunched per task scope;
     claims hinging on them were audited via recorded outputs + schema/binary
     surface re-runs. All scratch (/tmp/r4-*) removed; sibling r4 lanes' files
     left untouched. Re-run date: 2026-10-13. -->

## File: corpus/knowledge/2026-10-13-r3-runtime-observation.md

### Verify: `npx -y rea-agents@6.4.0 inspect-web-network-capture --schema`
- result: **confirmed** — required args `{capturePath:"Absolute local capture path", format: enum[har,mitmproxy]}`; options `record` (ordinal array) + `sensitiveValue` (literal redaction list). No endpoint parameter exists → strictly-offline claim holds verbatim.

### Verify: `npx -y rea-agents@6.4.0 inspect-web-page --help` (+ `inspect-electron-page --help`, `list-browser-targets --help`, `list-electron-targets --help`, `capture-browser-scenario --schema`, `capture-electron-scenario --help`, `observe-web-session --help`, `capture-web-screenshot --help`)
- result: **confirmed** — `inspect-web-page <endpoint> <targetId>` positional with `--observation-ms` default **500**, `--allowed-origins`, and all 7 include* flags (console-text, json-body-shapes, websocket-shapes, script-sources, storage-keys, storage-fingerprints, accessibility-text) — the recorded "opt-in depth dial" surface. `inspect-electron-page` shows `--observation-ms` default **100** exactly as claimed. `capture-browser-scenario <inputJson>` ("Inline browser scenario JSON or JSON file path") positional. `capture-electron-scenario` exists — the frontier note "exists and is the obvious next probe" is accurate. All enumerated live-endpoint verbs present with recorded signatures.

### Verify: `npx -y rea-agents@6.4.0 list-browser-targets http://127.0.0.1:9222 --allowed-origins '["http://example.invalid"]'`
- result: **confirmed** — `invalid_request`/`invalid_input`, `retryable:true`, raised at argument parsing *before* any endpoint contact (port dead — proves it errs closed on the token, not on connect). The "bare scalar per flag, not a JSON-array string" claim holds.

### Verify: `chromium --version`; `/usr/lib/electron43/electron --version`; grep `disconnected-external`/`process_ownership` in npx-cached rea-agents dist
- result: **confirmed** — `Chromium 152.0.7977.82` (exact recorded product), electron `v43.6.0` (recorded `Electron/43.6.0`), `/usr/lib/electron43` + `xvfb-run` present. `disconnected-external` + `process_ownership` strings found in `dist/domain/browserScenarioCapture.js`, `dist/browser/PlaywrightScenarioSession.js`, `dist/application/BrowserScenarioEvidence.js` — connect-mode external-ownership cleanup claims are in the shipped source.

### Verdict audit
- **holds.** Every claim auditable without relaunching CDP endpoints reproduces: verb surface, positional args, flag defaults (500/100 ms), scalar `--allowed-origins` semantics, offline-only capture intake, host binaries (chromium 152, electron 43.6.0, xvfb), and scenario-cleanup source strings. Live-binding claims (target enumeration payloads, `capture_window`, excluded-reason histograms) were not re-executed per lane scope — they rest on recorded outputs only; none is contradicted by the surface re-run.

## File: corpus/knowledge/2026-10-13-r3-apk-inventory.md

### Verify: `sha256sum`/`file`/`unzip -l` on `android_debug.apk`
- result: **confirmed** — `59e0073f0fa59f552684a861d8f4266b0b34b488a140d6657eac7dd70d1a0a0d`, "Android package (APK), with gradle app-metadata.properties", 127,260,725 B. `unzip -l` lists 129 file rows: 13 `classes*.dex`, 8 `.so` across arm64-v8a/armeabi-v7a/x86/x86_64. Minor note: unzip lists 129 rows vs the graph's 130 central-directory occurrences — one non-file/dir central entry is invisible to `unzip -l`; the graph claim itself re-verified exactly (below).

### Verify: `npx -y rea-agents@6.4.0 inspect-artifact --schema`; `inspect-artifact <apk> --format json`  ← flagged 120-node graph re-check
- result: **confirmed** — schema: `args.path` required positional, `integrityPolicy ∈ {fail, record-and-continue}` default `fail`. Re-run: same deterministic evidence `ev_5a05f9561fe3…`, provider `rea-artifact-graph` v1, `authority: shipped-artifact`, `confidence: observed`, `root_format:"apk"`, `root_sha256` = file sha. **node_count 120 / occurrence_count 130 / edge_count 129 — exact.** Format histogram `file`×110, `elf`×8, `zip`×1, `mach-o-universal`×1 — exact. All 130 occurrences `hash_status:"verified"`, `integrity_contradictions:[]`. Mach-O false positive = `DebugProbesKt.bin` 1,738 B (`art_e7b3fb27…`). ZIP central-directory limitation present verbatim. `libc++_shared.so` node `art_22eb01a8…` at 1,374,336 B — exact.

### Verify: `unzip -o -j <apk> 'lib/arm64-v8a/libc++_shared.so'` + `sha256sum`/`file` + `analyze <so> --format json`
- result: **confirmed** — extracted sha256 `c4c2fe5cbcb1fba0003a31fc7ab29a9bb12df6cc187ec45a806462540e83d93b` = graph node sha (provenance chain closes). `file` → ELF 64-bit LSB aarch64, Android 21, NDK r28, stripped. `analyze` → same deterministic evidence `ev_63bb52bd51f7…`, `architecture:"arm64"`, `import_mode:"ephemeral-source-immutable"`, doc `target-c4c2fe5cbcb1`, **32 segments / 3,009 procedures / 3,332 strings — exact**, `.note.android.ident` + `__lcxx_override` segments present.

### Verify: `inspect-android-package <apk>`; `decode-android-resources <apk>`; `inspect-binary-layout <so>`; `doctor --format json`
- result: **confirmed** — all three refusals verbatim: jadx `capability_unavailable`/`unsupported_provider`/`retryable:false`/`REA_JADX_MCP_JAR`; apktool same shape/`REA_APKTOOL_COMMAND`; pwntools-elf `provider_unavailable`/`unavailable`/`retryable:true`/`REA_PWNTOOLS_PYTHON` (pwntools 4.15.0 + pyelftools 0.33 + Unicorn 2.1.2). `doctor` → `healthy:false`; ghidra 12.1.4 + java 21 + node 24.21.0 healthy; `hopper`/`ida-registration` `missing_analysis_engine`; `skill:identity` + 5 MCP registrations `config_drift` — identical set.

### Verdict audit
- **holds.** Every numeric and refusal claim reproduces byte-exactly, including the flagged 120/130/129 graph and the 32/3009/3332 bridge analysis. Deterministic evidence IDs identical to r3 (same input → same `ev_*`). Only cosmetic footnote: `unzip -l` counts 129 file rows vs the graph's 130 occurrences (expected — graph counts all central-directory entries); worth one clarifying line in a future edit, not a correction.

## File: corpus/knowledge/2026-10-13-r3-evm-interface.md

### Verify: `inspect-evm-interface --schema`; `inspect-evm-interface --help`; `<file> --encoding hex`  ← flagged positional-encoding quirk re-check
- result: **confirmed** — schema advertises `{path, encoding enum[raw,hex]}` both required; `--help` usage is `rea inspect-evm-interface <path> <raw|hex>` — encoding is positional. `--encoding hex` → `Unknown flag: --encoding`, real exit code **1** unpiped (the recorded pipe-masking caveat is accurate). Quirk confirmed on both axes: schema-shape ≠ CLI-shape, flag form rejected.

### Verify: `inspect-evm-interface /tmp/r4-evm-c1.hex hex` (recreated `6001600101` carrier) + `0x`-prefixed twin + ENOENT + `zzzznothex`
- result: **confirmed** — carrier sha `27dc8217…a87c3`, decoded bytecode sha `b20db086…e54fb` (both exact), `evmole-interface`/`evmole@0.9.3`, `functions:[]`, `kind`/`hardfork`/`deployment_authenticity` all `unknown`, `evidence_kind:"inferred"`, `runtime_execution:"not-performed"`. `0x6001600101` → identical bytecode sha. ENOENT → `invalid_request`/`invalid_input`/`retryable:true` exit 1. Malformed hex → verbatim "Hex carrier requires complete hexadecimal byte pairs, an optional 0x prefix and outer ASCII whitespace; interior separators are invalid."

### Verify: `inspect-evm-interface` on rebuilt 3-selector dispatcher (`hex` + `raw` twin)
- result: **drifted (minor)** — the original `/tmp/evm-carrier-3.hex` bytes were elided in the staging file and are unrecoverable, so its exact sha256 (`3e2fd6ca…fe67`) and offsets (62/68/74) cannot be re-derived. On an equivalent hand-assembled dispatcher (Solidity `DUP1;PUSH4;EQ;PUSH1;JUMPI` chain, same 3 selectors): **all 3 recovered** (`a9059cbb`, `70a08231`, `095ea7b3`), `dispatch:"abi"`, zero false positives, empty `inferred_arguments` — capability confirmed. Two nuances vs the r3 text: (a) `bytecodeOffset` reported = the function-body JUMPDEST addresses (40/47/54), not "the PUSH4 sites" as claimed — the offset-semantics wording drifts; (b) `inferred_state_mutability` came back `payable` on my stubs vs `pure` on theirs — honest inference variance by body content, not tool drift. Bonus finding: a DUP1-less dispatch chain (semantically dead after first EQ) recovers only the first selector — EVMole prunes unreachable comparisons; worth a cookbook line.
- `raw`-encoding twin of the same 62 bytes → identical selector set + identical bytecode sha256 — **confirmed** raw≡hex convergence.

### Verdict audit
- **holds with one wording drift.** The flagged positional-encoding quirk is confirmed in full (positional usage, flag rejection, exit 1, schema/CLI divergence). Baseline decode, typed refusals, `0x` handling, and selector recovery all reproduce. The single drifted item is interpretive: `bytecodeOffset` tracks jump-destination bodies, not PUSH4 sites — amend candidate-3 wording next corpus pass. Staging file should also stop eliding carrier bytes; exact-byte provenance was unrecoverable.

## File: corpus/knowledge/2026-10-13-r3-pe-arm64.md

### Verify: `sha256sum`/`file`/`llvm-readobj --file-headers` on `cli-arm64.exe`
- result: **confirmed** — `b9a7d08da880dfac8bcf548eba4b06fb59b6f09b17d33148a0f6618328926c61`, 13,824 B, "PE32+ executable for MS Windows 6.02 (console), ARM64, 6 sections"; `Machine: IMAGE_FILE_MACHINE_ARM64 (0xAA64)`, `AddressOfEntryPoint: 0x1E10`, `ImageBase: 0x140000000`.

### Verify: `analyze cli-arm64.exe --format json`  ← flagged segment/procedure counts re-check
- result: **confirmed** — same deterministic evidence `ev_f4e02f932f3f…`, `architecture:"arm64"`, `available_architectures:["arm64"]`, `import_mode:"ephemeral-source-immutable"`. **segment_count 7 / procedure_count 136 / string_count 77 — exact.** Segment names identical: Headers, .text, .rdata, .data, .pdata, .rsrc, .reloc. Cosmetic quirk re-observed verbatim: `native_aot_metadata.contract_revision` = `rtr-9.1-x64-pe-read-only-v3` while architecture correctly says `arm64`.

### Verify: `search --kind procedures --mode regex --pattern '.*'`; `decompile entry --format json`
- result: **confirmed** — search evidence `ev_d0069932cc84…` (same id): 136-entry list; `entry` resolves at `0x140001e10`; `__security_push_cookie`, `__security_pop_cookie`, `_guard_dispatch_icall`, `_guard_check_icall` + KERNEL32/CRT import thunks all present. Decompile evidence `ev_93ada8d19161…` (same id): `DWORD entry(void)` → calls `FUN_140002178()` then returns `FUN_140001c60()`, result `limitations:[]` — verbatim match.

### Verdict audit
- **holds.** The flagged counts (7/136/77), entry-point resolution (ImageBase+0x1E10), named ARM64/MSVC bodies, and the clean `entry` pseudocode all reproduce exactly under Ghidra 12.1.4; deterministic evidence IDs identical to r3. Whole analyze→search→decompile chain confirmed end-to-end.

## Summary

- **4 files audited, 4 verdicts hold** (1 with a minor wording drift). 16 verify groups re-run; 15 confirmed, 1 drifted, 0 fails.
- **Flagged re-checks all pass exactly:** APK graph 120 nodes/130 occurrences/129 edges with identical histogram and all-verified hashes; PE-ARM64 7 segments/136 procedures/77 strings with identical segment names; EVM positional-encoding quirk confirmed (schema-shape vs positional CLI, `--encoding` rejected exit 1).
- **Deterministic evidence IDs:** `ev_5a05f956…` (artifact), `ev_63bb52bd…` (so), `ev_f4e02f93…`/`ev_d0069932…`/`ev_93ada8d1…` (PE chain) — all identical to r3, so recorded outputs were genuine tool output.
- **Drift to amend:** r3-evm-interface candidate 3 — `bytecodeOffset` is the jump-destination/body entry, not "the PUSH4 sites". Also record that staging elided carrier bytes (exact-sha provenance unrecoverable) and that DUP1-less dispatch chains recover only the first reachable selector.
- **Not re-verified by design:** live CDP endpoint payloads (no relaunch per task scope); all surface-level claims around them confirmed instead. Android-decode/pwntools providers remain blocked-by-config — do not retry in-loop.
- No repo files modified; no commits; all audit scratch removed from /tmp.
