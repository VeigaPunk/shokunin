# kaidoku-r4 · 02-audit-B — re-verify of r3 corpus entries (renderer-asar, node-addons, appimage, keyed-archive-carriers)

Auditor: round-4 audit lane. Method: re-run the verify commands recorded in each corpus
entry against the live host (Linux x86_64, node v24.21.0, python3 3.14.7,
`npx -y rea-agents@6.4.0`). r3 `/tmp` scratch (main.js, app.js, both analysis
JSONs, r3-asar-list.txt, trace inputs) still present — digests re-checked before
use. Keyed-archive carriers had been removed per r3's log; re-synthesized under
`/tmp/r4-audit/` and removed again after the runs.

## File: corpus/knowledge/2026-10-13-r3-renderer-asar.md

### Verify
- `sha256sum /usr/lib/obsidian/obsidian.asar` → `a52a7daf…4059d`, 25,787,463 B — **confirmed** (target unchanged).
- `npx -y @electron/asar list` piped to `diff` vs `/tmp/r3-asar-list.txt` → **0 diff lines, 380 entries** — confirmed.
- `python3` on `/tmp/obsidian-renderer-analysis.json` → `evidence_id ev_e8a2c4ba61ff…`, `subject.digest.sha256 a52a7daf…`, graph 235n/344e, semantic 23,527n/33,119r, `summary.ipc` = `{operations:45, literal_channels:45, dynamic:0, main_handlers:45, renderer_*:0}` — confirmed.
- **Named re-check — 45 literal ipcMain ops:** `grep -o 'ipcMain' /tmp/main.js | wc -l` → **45**; `grep -oE 'ipcMain\.(handle|on)\("' | uniq -c` → 44 `on` + 1 `handle`; all 44 channel literals + `register-cli` match the recorded list 1:1 — claim **confirmed**. BUT the recorded verify command `grep -c 'ipcMain' /tmp/main.js` returns **1**, not 45: main.js is a 69-line minified file with all 45 occurrences on one line, and `grep -c` counts matching *lines*. Same defect in the recorded renderer-side check: `grep -c ipcRenderer` → 1/1/1, while `grep -o | wc -l` correctly reproduces the claimed 64 (app.js) / 8 (starter.js) / 5 (help.js). `/tmp/main.js` sha256 `25b0705d…c85f`, app.js `8efbf581…9898` — files identical to r3.
- Electron block dump (graph node 126, `javascript-asset`): 45 ipc records all `side:"main"`, `handler_kind:"inline-function"`; 2 `browser_windows` (`options_status dynamic/dynamic` and `object-literal/dynamic`, `preload_path:null` both); 1 `sender_validations` `{subject:"process-id", mechanism:"comparison:===", expected:dynamic f.processId, enforcement:"unknown", line 69 col 1864}` — confirmed exactly.
- Limitations census: **29** `Resource constraint` records — 6 heap-exhaustion files (app.js, help.js, worker.js, starter.js, defuddle.full.js, openjpeg_nowasm_fallback.js — all six named in r3, exact) + 22 named budget files + 1 generic record. r3 wrote "~24 records" — direction and partition confirmed, count is really 29 (the "~" hedge covers it). h8 bundle: `ev_6cf34bde…`, 285n/391e, ipc 45/45, resource records **33** — confirmed exactly.
- `recover-javascript-sources /tmp/app.js /tmp/r4-recovered` → RC=1 `capability_unavailable`/`unsupported_provider`, message verbatim ("Provide an absolute REA_WAKARU_COMMAND … Wakaru ^1.13.0 … verified with 1.14.0") — confirmed.
- `trace-application-feature /tmp/trace-appjs.json` (module seed, r3's own input file) → `evidence_id ev_3d267786f29d…` **identical to r3** (deterministic minting), `source_evidence_id ev_e8a2c4ba…`, 1 matched seed, 235n/344e traced, 102 terminal paths, 378 observed / 262 inferred / 29 unavailable, coverage `partial` — confirmed. (trace_id differs per run, expected.)
- Entrypoint topology (kind-filter dump): `electron-main` → `package.json:main = index.js` `resolution_status:"not-found"`; `electron-preload` → `declared_path "metadata"` `resolution_status:"external"`; 3 `electron-renderer` resolved (`index.html`, `help.html`, `starter.html`, `html-script-entrypoint`) — confirmed.

### Verdict audit
**HOLDS.** Every substantive claim reproduces: 380-entry census, evidence
digests, 45-literal IPC surface on obsidian.asar's main.js (44 `on` +
`handle register-cli`), dynamic webPreferences posture, coverage partition
(6 heap-OOM files, budget class), h8 redistribution result, Wakaru refusal,
and the trace playbook (module seed works, channel facts live on file nodes).
Two defects worth annotating in the corpus: (1) the recorded `grep -c`
verifies are line-count commands on minified files — they yield 1, not the
claimed counts; `grep -o … | wc -l` is the correct recipe (claims themselves
reproduce). (2) Resource-constraint count is 29 (6 heap + 23 budget-class
records), r3 hedged "~24" — fine, but exact is better.

## File: corpus/knowledge/2026-10-13-r3-node-addons.md

### Verify
- **Named re-check — `nm -D | grep -c ' U napi'` taxonomy** on all 7 `.node` paths → `btime 36`, `get-fonts 39`, `fs-xattr 21`, `sqlcipher 51`, `libsignal-client 0`, `libringrtc 0`, `1Password index.node 0`; the three family-B modules each grep ` U dlopen`/` U dlsym` = **2** — confirmed exactly, taxonomy rule reproduces.
- Host N-API provider: `nm -D /usr/lib/electron43/electron | grep -cE ' T napi_'` → **145**, ` T node_api` → **14**; `/usr/lib/signal-desktop/signal-desktop` → **145** + **14** — confirmed.
- Fringe enumeration: `find /usr/lib /opt -name '*.asar.unpacked'` → **3** trees; `find … -name '*.node' -path '*unpacked*'` → **7** files at the recorded paths (incl. 1Password's root-level `index.node`) — confirmed.
- ELF fingerprints: both obsidian addons `ELF 64-bit LSB shared object, x86-64, SYSV, not stripped`; sha256 `3bdc3fce…`/`fc94d394…` match; NEEDED `libstdc++/libgcc_s/libc`, SONAME literally `binding.node`, `.comment` GCC Ubuntu 13.3.0 — confirmed.
- Registration fingerprint: `objdump -d --disassemble='napi_register_module_v1' -M intel` on btime → exactly **1** `call`: tail `call _Z4InitN4Napi3EnvENS_6ObjectE@plt`; get-fonts exports `napi_register_module_v1` + `node_api_module_get_api_version_v1`, 9 hits for `FontWorker|napi_create_promise|napi_queue_async` — confirmed.
- REA decompile (the recorded verify): `rea-agents@6.4.0 decompile …/btime/binding.node 0x104120` → RC=0, demangled header `btime(Napi::CallbackInfo const&)`, `napi_is_buffer`/`napi_get_typedarray_info`/`napi_get_value_int64`/`napi_create_double` resolved by name, `"bad arguments, expected: (buffer path, seconds btime)"` literal present, and the `btime((CallbackInfo *…)` self-call wart **does** reproduce — confirmed (wart included).
- 1Password `index.node`: 187,997,016 B, sha256 `1cb3e361…7778` matches, `.comment` = LLD 22.1.8 + rustc 1.98.1 (48a229cea 2026-09-01) + GCC 9.4.0 + clang 15.0.7 — confirmed verbatim.

### Verdict audit
**HOLDS.** The two-family linkage taxonomy is exact on re-run (36/39/21/51 vs
0/0/0 + dlopen/dlsym), the host-as-N-API-provider claim reproduces on both
Electron binaries (145 `T napi_` + 14 `node_api*` each), the 7-file/3-tree
inventory is unchanged, and the REA decompile at the +0x100000-rebased address
still resolves napi names, the error literal, and the self-recursion wart.
No drift found in this file.

## File: corpus/knowledge/2026-10-13-r3-appimage.md

### Verify
- `sha256sum` → `2fe7c5ac…ba5b`, 134,055,925 B — confirmed (target unchanged).
- `./Grok_Bot_0.68.1.AppImage --appimage-offset` → **188392**; `python3 -c "print(186344+32*64)"` → 188392 — confirmed (offset = end of section-header table).
- `dd bs=188392 skip=1 | file -` → `Squashfs filesystem, little endian, version 4.0, zlib, 133724992 bytes, 164 inodes, blocksize 131072` — confirmed. Trailer `dd bs=1 skip=133913384 count=142541 | file -` → `data` — confirmed.
- `rea inspect-artifact` → **`ev_90c5bc2a…` reproduced identically** (deterministic evidence), `format: elf`, limitation `"Artifact has no child container entries."`, `next_probe open_binary` — confirmed.
- `rea extract-artifact` → `unsupported_target`, `"Artifact format has no extraction reader: elf"`, `retryable:false` — confirmed verbatim.
- `rea inspect-binary-layout` → `provider_unavailable`, `retryable:true` — confirmed (pwntools-elf gap persists).
- **Named re-check — `unallocated_0` payload:** `rea analyze` → `segment_count 35`, `procedure_count 621`, `string_count 456`, segment `unallocated_0` length **133,867,533** (= 134,055,925 − 188,392, byte-exact); `rea read-bytes "unallocated_0:0x0" --length 32` → `bytes_hex 68737173a4000000cb76c46a…` — live `hsqs` superblock through the overlay, byte-identical to r3 — **confirmed**. Bad grammar `unallocated_0::0x0` → `invalid_request`/`invalid_input` with per-arg reason `invalid_format` (r3 recorded the code as `invalid_format`; actual envelope code is `invalid_request`, the `invalid_format` string lives in the issue's `reason` field — cosmetic precision note only).
- `rea inspect` → `evidence_id ev_32ec7e29…` **byte-identical to this run's `rea analyze` output** — the strongest possible confirmation that `inspect` ≡ `analyze` (same normalized bundle → same evidence hash).

### Verdict audit
**HOLDS.** The headline negative (artifact layer sees monolithic ELF, one
node, zero members, no extraction reader) and the headline nuance (native
layer maps the whole post-ELF payload as one `unallocated_0` overlay,
133,867,533 B byte-exact, `hsqs` readable via `<space>:0x<hex>`, excluded
from strings/procedures) both reproduce exactly — including identical
`inspect-artifact` evidence id. `inspect`≡`analyze` is now proven by
evidence-hash equality. One cosmetic correction: the bad-address rejection
code is `invalid_request` with `invalid_format` as the per-field reason.
The 142,541-B trailer remains `data`/unidentified — frontier unchanged.

## File: corpus/knowledge/2026-10-13-r3-keyed-archive-carriers.md

### Verify
- **Named re-check — synth recipe still works:** rebuilt the NSKeyedArchiver binary plist with `plistlib` (`FMT_BINARY`, `plistlib.UID` refs; `$null` + archived `NSMutableDictionary` + class-descriptor + 4 scalars) → **363 B** (r3: 365), `file` → `Apple binary property list`. `inspect-keyed-archive` file leg → `archive_format binary-plist`, `roots {root:{UID:1}}`, **7 objects** (`nil`/`archived-object`/`class-descriptor`/`scalar`×4) and **6 resolved refs** identical to r3's edge list (`root→1`, `1.$class→2`, `1.NS.keys[i]→5,6`, `1.NS.objects[i]→3,4`) — **confirmed**. New evidence id `ev_464caf10…` (content-bound to my rebuilt bytes — expected, differs from r3's `ev_0524ef94…`).
- Bundle leg: `inspect-keyed-archive /tmp/r4-audit/Fake.app Contents/Resources/MainMenu.nib` → `archive_path` echoed, same 7 objects — confirmed positional-archive addressing.
- `--archive` as a flag → `{"code":"UNKNOWN","message":"Unknown flag: --archive"}` — schema-to-CLI wart confirmed verbatim.
- Plain plist carrier → `unsupported_target`, `"no $archiver key"`, remediation names `inspect_plist` + `"requires a macOS host"` — dead-breadcrumb refusal confirmed verbatim.
- `inspect-plist` on a valid binary plist → `capability_unavailable`/`unsupported_provider`, `"Native macOS utilities require macOS"`, `provider_id composite:native-macos+rea-artifact-graph+rea-dotnet-static` — confirmed; the macOS gate still precedes carrier inspection.
- `decode-interface-builder` on rebuilt `Fake.app` (binary `Info.plist` + `CFBundleExecutable:Fake` + arm64 Mach-O at `Contents/MacOS/Fake` + loose `MainMenu.nib` + `.storyboardc/` scene) → RC=0, **2 documents** (`nib` + `storyboard_scene`), `object_count:1`, `hierarchy_complete:true` each — confirmed.
- `trace-dylib-resolution` on rebuilt 352-B arm64 `MH_EXECUTE` (LC_SEGMENT_64 + 2×LC_LOAD_DYLIB + LC_LOAD_WEAK_DYLIB + 2×LC_RPATH, 8-aligned cmdsizes): parses, coverage `complete`, 3 edges all `undetermined`; candidates carry provenance `rpath`/`executable_path`/`literal`; bare file → `escapes-target`×2 + `outside-target`×2; `Fake.app` → `resolved_path Contents/Frameworks/lib{dep,kaidoku}.dylib`, `install_name_matches:null` ×3 — the honest-`undetermined` semantics and rpath stack resolution **confirmed**.

### Verdict audit
**HOLDS with one drift.** All four ops behave exactly as catalogued: the
keyed-archive recipe (file + bundle legs), the typed refusal taxonomy, the
`--archive` positional wart, the `inspect_plist` macOS gate, the IB bundle
contract, and `undetermined`/`outside-target`/`escapes-target` dyld honesty.
**Drift:** r3 recorded the `LC_LOAD_WEAK_DYLIB` edge as *"silently absent
from `edges`"*; on my spec-equivalent carrier the weak edge IS emitted
(`weak:true`, install name `/usr/lib/libweak.dylib`, status `undetermined`,
literal candidate). Either r3's 872-B carrier differed in a detail that
suppressed it, or the op now surfaces weak loads — on the current evidence
the "silently absent" sub-claim does not reproduce; the documented
"absolute install names not evaluated" limitation still holds as
`undetermined`. Carrier reconstruction note: plistlib emits 363 B vs r3's
365 — structurally identical (7 objects, same refs); the 2-B delta is plist
serialization detail, not behavior.

## Summary

- **Verdict: all four files HOLD.** 30+ verify commands re-run across the four entries; every headline claim reproduces, several with byte- or evidence-id-identical output (`ev_90c5bc2a`, `ev_3d267786`, `inspect`≡`analyze` hash equality, `hsqs` overlay bytes, both `.node` sha256s, host `napi_*` export counts).
- **Named re-checks:** (1) 45-literal `ipcMain` count — **confirmed** 1:1 via `grep -o`, but the file's recorded `grep -c` verify yields 1 on the minified single-line occurrence (same defect hits the `ipcRenderer` counts; correct recipe is `grep -o … | wc -l`). (2) `nm -D | grep -c ' U napi'` taxonomy — **confirmed exactly** (36/39/21/51 vs 0/0/0, family-B dlopen/dlsym×2). (3) AppImage `unallocated_0` — **confirmed** (133,867,533 B, `68737173` live read). (4) Keyed-archive synth recipes — **confirmed working** (rebuilt carriers decode identically; weak-dylib edge presence is the one drifted detail).
- **Drifts logged:** `grep -c` verify commands (recipe error, claim sound); resource-constraint count 29 vs "~24" (hedged); `invalid_format` sits in the issue-reason field under `invalid_request`, not as top-level code; `LC_LOAD_WEAK_DYLIB` edge emitted, not absent.
- Host unchanged where it matters: obsidian 1.13.7 asar sha, AppImage sha, all 7 `.node` files, electron43/signal-desktop export surfaces.
- Scratch (`/tmp/r4-audit`, `/tmp/r4-x`, `/tmp/r4-recovered`, diff file) removed; no repo files modified by this lane besides this report.
