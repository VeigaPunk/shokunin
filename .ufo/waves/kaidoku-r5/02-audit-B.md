# kaidoku-r5 · 02-audit-B — adversarial re-verification of four r4 entries

Lane: kaidoku-shokunin round 5 audit (Devin host). Date: 2026-10-13.
Scope: `2026-10-13-r4-09-js-export-compare.md`, `-r4-11-managed-unlock.md`,
`-r4-12-godot-arm64-scale.md`, `-r4-13-pwntools-persist.md`.
REA under test: `npx -y rea-agents@6.4.0` (npm latest = 6.4.0, re-verified
`npm view rea-agents versions`). Host: Linux x86_64, node v24.21.0.

Key environmental fact enabling this audit: **the r4 `/tmp` staging area is
fully intact** — every `cmp-*-{in,out}.json`, both app.asar analyses,
`/tmp/obs-{1127,1137}`, `/tmp/mini-{a,b}`, `/tmp/dnfenv`,
`/tmp/corelib-8664.dll`, `/tmp/godot-arm64-*.json`, and the jq/crash
scratch outputs all survive. Live re-runs could therefore be compared
byte-for-byte against r4's retained outputs, not just re-executed.

Environment drift noted (affects one check only, detailed below):
`REA_PWNTOOLS_PYTHON` is now exported in `~/.bashrc:58` and `~/.profile:7`
and present in this session's env; the r4-13 entry documented it as unset
at write time. All refusal checks were run under `env -u REA_PWNTOOLS_PYTHON`
to reproduce the claimed conditions.

---

## File 1 — `2026-10-13-r4-09-js-export-compare.md`

| check | claimed | observed | verdict |
|---|---|---|---|
| sha256 pin: app.asar 1.12.7 | `a92d31a5…18e`, 73,056 B | `a92d31a51840c50035919f7fc4a0caf1f34db50a6f9a9205613e9f95f6a1118e`, 73,056 B (`/tmp/obs-1127/usr/lib/obsidian/app.asar`) | CONFIRMED |
| sha256 pin: app.asar 1.13.7 | `8588f1fd…c52`, 480,052 B, = `/usr/lib/obsidian/app.asar` | `8588f1fd23c9f63d3507a9740d656252cf0fbe0538e00e5d8eb7660533416c52`, 480,052 B | CONFIRMED |
| `{}` input contract | RC=1 `invalid_request`/`invalid_input`, 6 `missing_argument` issues | RC=1, exactly 6 issues (`left,right,left_module_path,left_export_name,right_module_path,right_export_name`) | CONFIRMED |
| identity rule | `left.evidence_id === right.evidence_id` rejected via superRefine `…Schemas.js:52-59` | `validateJavaScriptExportShapeIdentities` present in `dist/domain/javascript/javascriptExportShapeComparisonSchemas.js` doing exactly that check | CONFIRMED |
| real diff `serialize` 5v5 | RC=0 `ev_c9b2fcdf…`/`jesc_72edc740…`, 10 rows all `paired:false`, summary `{unknown:10}`, coverage `partial` | re-run **BYTE-IDENTICAL** to `/tmp/cmp-serialize-out.json` (`cmp -s` clean, 14,320 B); summary `{added:0,removed:0,changed:0,unknown:10}`, 10 inventory rows all `paired:false`, both selectors `selected`, coverage `partial`/`partial`+`partial` | CONFIRMED |
| literal-discriminant pair `getElectronBinding` | `ev_b9ad0fe7…`, 1 pair via `{path:"",value:null}`, `summary:{unknown:4}`, pair emits no row | BYTE-IDENTICAL (8,858 B); 6 inventory rows, exactly one `paired:true` per side with discriminant `{path:'',value:None}`; `changes:4`, no row for the pair | CONFIRMED |
| const export `browserModuleNames` | `unavailable` ×2, binding exists (1 match each), no return-shape obs | BYTE-IDENTICAL (5,312 B); `unavailable` both, 1 candidate each `matches_requested_*:true`, limitation `"No exact static return-shape observation is available for the selected export."` verbatim | CONFIRMED |
| bogus selector | `missing`, 24-candidate census, 0 matches, right `selected` | BYTE-IDENTICAL (11,880 B); left `missing`, `candidates:24`, `fullmatch:0`, `omitted:0`, `selected_node_id:null`; limitation `"No exact export binding matched no/such/module.js:nope."` verbatim | CONFIRMED |
| cross-file app.asar vs obsidian.asar | left `selected`, right `missing`, exactly 8 surviving bindings, `ev_99b42bc2…`, 63 MB request | re-run on the 62,983,772 B input **BYTE-IDENTICAL** (7,595 B); left `selected`, right `missing`, `candidates:8`, `fullmatch:0`; input evidences `ev_4c3202c9…` + `ev_e8a2c4ba…` verified inside | CONFIRMED |
| synthetic diff taxonomy | `ev_ec6d721d…` `{added:2,changed:1}`, `complete-within-inputs`, discriminant `/nested/flag=true`; tags `ev_71ed7485…` `added /2`; rev `ev_c330884f…` `{removed:2,changed:1}` | all three **BYTE-IDENTICAL** (6,549/5,009/6,553 B); mini-config summary `{added:2,removed:0,changed:1,unknown:0}`, coverage `complete-within-inputs`, discriminant `{path:'/nested/flag',value:true}`, changes `changed /mode`, `added /extra`, `added /nested/second` — verbatim | CONFIRMED |
| **inline-Evidence vs retained-ref** (flagged check) | CLI rejects `{"kind":"retained-evidence","evidence_id":"ev_<64hex>"}` RC=1 `invalid_input`; MCP-session resolver only | re-ran `/tmp/cmp-mini-ref2-in.json` → RC=1 `invalid_request`/`invalid_input`: every Evidence field `missing_argument`/`invalid_value`, **`kind` flagged `unknown_argument`** on both sides — verbatim. `EvidenceInputResolver.js:9` shows the retained store is session-scoped ("Evidence retained in this session") | CONFIRMED |
| fixture gotcha `module.exports={…}` | shorthand → 1 `default` binding, 0 return shapes | re-synthesized `/tmp/mini-c` (`module.exports = {config,tags}`) → `analyze-javascript-application` RC=0, **export-binding:1 (`default`), export-return-shapes:0**. v2 fixtures on disk show `exports.X = function` form. (v1 evidence `de3385f9…` itself was overwritten by v2 — mechanism re-verified by synthesis instead) | CONFIRMED |

**File verdict: HOLDS.** Eight compare invocations reproduced byte-identical
evidence — the entry is not just directionally right, it is bit-exact
reproducible on this host. The inline-vs-retained distinction is exactly as
claimed: strict `evidenceSchema` rejects the ref object at input validation;
retained refs are a per-MCP-connection affordance a fresh CLI process never sees.

---

## File 2 — `2026-10-13-r4-11-managed-unlock.md`

| check | claimed | observed | verdict |
|---|---|---|---|
| **machine map: 0x14c accepted** (flagged check) | all 36 Pinta dlls (i386-marked AnyCPU) pass `inspect-managed-artifact`; Mono.Cecil → `ev_573dc…`, machine 332/0x014c | `inspect-managed-artifact /usr/lib/pinta/Mono.Cecil.dll` RC=0 → `ev_573dc0b65601e12151827a95a87c1e5e2a0bdf81862abce959db329722f8718c`, `machine_hex:'0x014c'`, `architecture:'x86'`, TypeDef 343 / MethodDef 3019 in `table_row_counts`. `file` on all 36 dlls → `Intel i386` + `Mono/.Net` | CONFIRMED |
| **0xfd1d refused** (flagged check) | `target_unavailable` / `unsupported PE architecture`, retryable false | `inspect-managed-artifact …/9.0.19/System.Private.CoreLib.dll` → `{"code":"target_unavailable","category":"unavailable","message":"Cannot open artifact: unsupported PE architecture…","retryable":false}` verbatim | CONFIRMED |
| x64 path via patched copy | `/tmp/corelib-8664.dll` (0xfd1d→0x8664) parses as x86_64, `cli.flags:12`, runtime "2.5" | patched copy still in `/tmp`; run → RC=0 `ev_1f7f8f77…`, `machine_hex:'0x8664'`, `architecture:'x86_64'`, `cli.flags:12`, `runtime_version:'2.5'` | CONFIRMED |
| host census | exactly 196 × 0x14c + 181 × 0xfd1d, zero native-arch managed dlls | same find+file pipeline → `196 Intel i386`, `181 Unknown processor 0xfd1d`, nothing else | CONFIRMED |
| dnfile+dncil unlock | dnfile 0.18.0; Mono.Cecil 0x14c, 343 TypeDef, 3019 MethodDef; RVA-reader shim decodes all bodies (`2914/2914`, `ldarg.0`/`newobj token(0x0A00002F)`/`ret`) | `/tmp/dnfenv` intact: dnfile 0.18.0; dnPE→`Machine 0x14c`, TypeDef 343, MethodDef 3019. Rebuilt the `CilMethodBodyReaderBase` shim over `pe.get_data` (contract: `read/tell/seek` + tuple-returning `read_uintN` via `_unpack`) → **tried 2914, decoded 2914**; first bodies disassemble to literally `ldarg.0`,`ldc.i4.1`,`newobj token(0x0A00002F)`,`ret` | CONFIRMED |
| 64 MiB decode budget | `ManagedDecodeBudget.js:4` `64*1024*1024`; sweep 22 pass ≤204,800 B / 14 fail ≥220,160 B incl. Pinta.Effects 220,160 pass vs Pango-1.0 220,160 fail | `ManagedDecodeBudget.js:4` verbatim `MAX_METADATA_REPRESENTATION_BYTES = 64 * 1024 * 1024`, message `…exceeds the 67108864 byte representation budget`. Re-ran the full 36-dll sweep: **22×0 resource-limit (≤204,800), 14×1 (≥220,160)** — boundary anomaly reproduced exactly (Pinta.Effects 220,160→0, Pango-1.0 220,160→1) | CONFIRMED |
| native-boundaries/members on small assemblies | `metadata.status: complete` + full `table_row_counts` on freetype2-2.0.dll | `inspect-managed-native-boundaries freetype2-2.0.dll` → `metadata.status:'complete'`, full row counts (Module 1, TypeDef 35, MethodDef 112, …) | CONFIRMED |
| Mono.Cecil/dotnet dead end | no SDK (`--list-sdks` empty, `tool list -g` exit 155), no ilspycmd/monodis/ikdasm/mono/csi/pwsh/csc/mcs | `dotnet --list-sdks` → empty (runtimes 9.0.19+10.0.11 only); `dotnet tool list -g` → RC=155 "No .NET SDKs were found"; all nine tools absent from PATH | CONFIRMED |

**File verdict: HOLDS.** The r1 erratum (machine-allowlist, not AnyCPU-reject)
is accurate in both directions: 0x14c accepted (all 36 Pinta dlls), 0xfd1d
refused with the typed envelope, 0x8664 works via the documented patch. The
dnfile+dncil unlock reproduced end-to-end including the exact 2914/2914 count.

---

## File 3 — `2026-10-13-r4-12-godot-arm64-scale.md`

| check | claimed | observed | verdict |
|---|---|---|---|
| target identity | sha256 `7a2ccd68…a292`, 91,662,336 B, `file` → PE32+ ARM64 8 sections | `7a2ccd688f6c3d53d2d67878bc98a96bebe8463bf97acf986b9c2c9e1ba9a292`, 91,662,336 B, `PE32+ executable for MS Windows 6.00 (GUI), ARM64, 8 sections` at `~/.local/share/godot/export_templates/4.7.2.stable/windows_release_arm64.exe` | CONFIRMED |
| **`provider_timeout` envelope** (flagged check) | `{"error":"Analysis failed","code":"provider_timeout","category":"timeout",…"retryable":true,…"operation":"list_documents","timeout_ms":90000}` | r4's saved probe `/tmp/godot-arm64-timeout-probe.json` (363 B) contains it verbatim; **fresh 90 s probe re-run now** (`REA_GHIDRA_STARTUP_TIMEOUT_MS=90000`) → identical envelope byte-for-byte, exit 1, wall ~91 s (stderr mtime 14:56:36 → stdout 14:58:07) | CONFIRMED |
| ~900 s internal deadline / 15m01.8s wall | run died at real 15m01.8s = 900,000 ms deadline + ~1.8 s teardown; outer `timeout 1500` did not fire | not re-run (instructed: no 15-min re-run). Mechanism verified: `dist/config/ghidraStartupTimeout.js:3` `DEFAULT_GHIDRA_STARTUP_TIMEOUT_MS = 330_000` and env override honored verbatim at 90 s; envelope's `timeout_ms` echoes the configured value; failure chain `GhidraClient.js:607` + `GhidraClientStartup.js:25` (`failure("timeout","Ghidra startup deadline elapsed")`) → `GhidraProviderClient.js:470` (`kind==="timeout"`→`AnalysisTimeoutError`) → `analysisErrorProjection.js:140` (`provider_timeout`, retryable list `:442`) → `analysisErrorPresentation.js:122` (`"timeout"`) — all line-pins verified in shipped dist | CONFIRMED (mechanism); the specific 15m01.8s figure is accepted as r4-reported — corroborated by retained artifacts, not re-measured |
| `--filter-output` strips error envelope → `{}` | filtered stdout = `{}` (3 B) | `/tmp/godot-arm64-analyze.json` is literally `{}` (3 B); envelope keys are indeed none of the requested summary paths | CONFIRMED |
| admission cap | `NATIVE_AOT_MAX_SOURCE_BYTES = 128 MiB`, `nativeAotPe.js:7` | `dist/domain/native/nativeAotPe.js:7` verbatim `= 128 * 1024 * 1024` | CONFIRMED |
| **small-target control** (flagged check) | re-run on `cli-arm64.exe` → `ev_f4e02f93…` byte-identical, 7/136/77 | first attempt on the wrong setuptools copy (`…/cpython-3.11.17…/setuptools/cli-arm64.exe`, sha256 `e4c4cddc…`) yielded `ev_6367df9a…` — evidence_id binds input path+content, and **two different setuptools builds of `cli-arm64.exe` exist on this host** (both 13,824 B). Re-run on the r3-pinned copy `~/.cache/uv/archive-v0/M1E0QXq07p7Gx3Fp/setuptools/cli-arm64.exe` (sha256 `b9a7d08d…`) → **`ev_f4e02f932f3f6078d763d9ac3334632bd07731096388e798c86e86d33411facf` exactly**, 7 segments incl. `.pdata`/`.reloc`, `subject.architecture:"arm64"`, upstream provider ghidra 12.1.4 | CONFIRMED |
| Ghidra-side timeline (import ~20 s, AARCH64:LE:64:v8A, VarnodeContext errors, kill ~14:02) | per live `/tmp/rea-ghidra-hKzt9I/ghidra.log` | that dir was cleaned at `-deleteProject`; a stale `/tmp/rea-ghidra-UU4kw1` (13:50, different target `193f3dd1f3e7`) is unrelated. Timeline details (PngDataType error, ~30 VarnodeContext errors, gdt applications, FidAnalyzer miss) | UNVERIFIABLE (log destroyed by design; consistent with — but not provable from — remaining evidence) |

**File verdict: HOLDS.** Envelope class, deadline knob, admission bound, and
control reproduction all verified live. The 15-minute wall itself was
deliberately not re-run per audit scope; every checkable mechanism behind the
claim pins to the shipped source at the cited lines.

---

## File 4 — `2026-10-13-r4-13-pwntools-persist.md`

| check | claimed | observed | verdict |
|---|---|---|---|
| **persistent venv** (flagged check) | `~/.local/share/kaidoku-pwnenv`, CPython 3.11.17, pins pwntools 4.15.0 / pyelftools 0.33 / unicorn 2.1.2, 174M | venv present; `bin/python` → `…/uv/python/cpython-3.11-linux-x86_64-gnu/bin/python3.11` (alias chain resolving to the 3.11.17 install — claim's `cpython-3.11.17-…` is the resolved target; `sys.version` reports **3.11.17**). `importlib.metadata`: pwntools **4.15.0**, pyelftools **0.33**, unicorn **2.1.2**. `du -sh` → **174M** | CONFIRMED (symlink path is the `cpython-3.11` alias, not the literal `cpython-3.11.17` dir — cosmetic delta only) |
| `inspect-binary-layout /usr/bin/jq` first run | exit 0, 79,955 B, `ev_294a449c…`, provider `pwntools-elf` `pwntools@4.15.0;pyelftools@0.33;unicorn@2.1.2`, artifact sha256 `e815667…` | re-run → RC=0, **79,955 B exactly**, `ev_294a449cecf2d7b6e72b63b8385b6dcacf589b58c55d9de3ce1b0a81760a71bd` exactly, provider string verbatim, `sha256 e815667571d07cb7a7be98eb6e9920a9e7e20d64074c132882e7fc94984f7806` = live `sha256sum /usr/bin/jq` | CONFIRMED |
| layout counts | 28 sections, 15 segments, 80 symbols, 79 relocations + 1 packed RELR, 3 DT_NEEDED, inferred PIE/NX/no-exec-stack/canary/Full RELRO, `relocation_inventory_completeness:unknown`, 12 limitations, empty diagnostics | 28/15/80/79 exact; `packed_relative_relocations: 1` block (3 decoded entries `0x7b70/0x7b78/0x8008` — "1 packed RELR entry" = 1 block); `needed_libraries` = libjq.so.1/libonig.so.5/libc.so.6 each with raw bytes+offsets; mitigations `inferred` + all five flags verbatim; `unknown`; **12 limitations**; `diagnostics {stdout:'',stderr:'',truncated:false}` | CONFIRMED |
| bare run → `provider_unavailable` | exit 1, `candidate_ids:["pwntools-elf"]`, refusal demands 4.15.0/0.33/2.1.2 | under `env -u REA_PWNTOOLS_PYTHON` → RC=1, verbatim refusal JSON incl. `executable_path:""`. **Note environment drift**: in a current login shell the var IS exported (`~/.bashrc:58`, `~/.profile:7`, both written after the r4 lane — .bashrc 2,399→2,955 B, .profile 256→619 B, each now containing exactly the documented export line). The entry's "files not edited / var unset" was accurate at write time; the documented recipe was subsequently applied (by the operator, per the entry's own recipe — the lane itself did not edit them) | CONFIRMED (mechanism); write-time file-state claim is now stale environment, not an entry error |
| relative path refused | `REA_PWNTOOLS_PYTHON=kaidoku-pwnenv/bin/python` → `provider_unavailable` | refused verbatim, `executable_path:"kaidoku-pwnenv/bin/python"` echoed in diagnostics | CONFIRMED |
| **`coredumpctl dump` decompression** (flagged check) | `dump` emits already-decompressed ELF; manual `zstd -d` only needed on the stored `.zst`; `zstd -dc … | cmp` byte-identical | original pid 1150573's storage is now `(missing)` in the journal — **the specific artifact rotated out**. Substitute pid 244048 (bash SIGSEGV, stored `.zst` 66.6K): `coredumpctl dump 244048 -o /tmp/audit-r5-core` → **724,992 B ELF core** (identical size to r4's dump — same bash binary/layout); `od` magic `7f 45 4c 46`; `zstd -dc <stored .zst> | cmp -` → **CMP-IDENTICAL**. Mechanism fully re-verified on substitute | CONFIRMED (on substitute; original pid artifact gone to journal rotation) |
| `inspect-recorded-crash` re-verify | exit 0, ~25,690 B, 1 thread × 27 regs w/ file locations, 40 segments, 8 notes, SIGSEGV `note_index:2 number:11`, `target_execution:not-performed`, `live_process_identity:unknown` | on substitute core → RC=0, 25,677 B (delta = path-length echo), 1 thread × **27** registers, **40** segments, **8** notes, `signals:[{note_index:2,number:11,code:0,errno:0,fault_address:null/unknown}]`, `not-performed`, `unknown` — schema verbatim | CONFIRMED |
| `rea doctor` blind to aux provider | `providerInspections` = ghidra + ida only | `doctor --json` → `['ghidra','ida']` — pwntools-elf invisible | CONFIRMED |

**File verdict: HOLDS.** Persistence, first-run evidence id, refusal contract
(absent AND relative), decompression mechanism, and doctor-blindness all
re-verified. The two environment notes — exported var now in rc files, original
core rotated — are drift on the *substrate*, not errors in the *entry*.

---

## Roll-up

- **4/4 files: HOLDS.** Zero refuted claims, zero errata required.
- Strongest evidence: 8/8 `compare-javascript-export-shapes` outputs
  byte-identical (`cmp -s`) including a 63 MB request; `ev_f4e02f93…`,
  `ev_294a449c…`, `ev_573dc0b6…` all reproduced bit-exact; 2914/2914 dncil
  decode; 196/181 machine census and the 22/14 sweep boundary anomaly exact.
- UNVERIFIABLE items (with reasons, none load-bearing):
  1. Godot 15m01.8s wall — not re-run per scope (short probe verified the class); retained `{}`/probe artifacts corroborate.
  2. Ghidra-log micro-timeline — `-deleteProject` destroys the log dir by design.
  3. `coredumpctl dump 1150573` — storage rotated to `missing`; verified on substitute pid 244048 (same mechanism, same 724,992 B output size).
  4. v1 mini fixture evidence (`de3385f9…`) — file overwritten by v2; mechanism re-verified by re-synthesizing `/tmp/mini-c` → 1 `default` binding, 0 return shapes.
- Environment drift to record for the fleet: `REA_PWNTOOLS_PYTHON` is now
  persisted in `~/.bashrc` + `~/.profile` — bare `inspect-*` pwntools calls
  succeed in login shells; reproduce r1–r3 refusal semantics only under
  `env -u REA_PWNTOOLS_PYTHON`. Also: two distinct `cli-arm64.exe` builds
  exist in the uv cache (`b9a7d08d…` r3-pinned vs `e4c4cddc…`); evidence ids
  bind path+content, so cite the full path when pinning `ev_f4e02f93…`.
