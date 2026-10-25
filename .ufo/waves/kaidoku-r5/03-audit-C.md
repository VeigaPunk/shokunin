# kaidoku-r5 / 03-audit-C — adversarial re-verification of the six r4u unlock-wave entries

Audit lane (Devin host), 2026-10-13. Method: literal re-runs of the cited verify
commands plus independent ground-truth checks (sha256/readelf/dd/python scans,
rea-agents@6.4.0 via npx, dnfile 0.18.0/dncil 1.0.2 in surviving venv
`/tmp/dnfenv-r4`). All re-runs executed under the r4u env matrix
(`REA_BINWALK_COMMAND=/usr/bin/binwalk`, `REA_UNBLOB_COMMAND=~/.local/bin/unblob`,
`REA_JADX_MCP_JAR=~/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`,
`REA_APKTOOL_COMMAND=/usr/bin/apktool`, `REA_ADB_PATH=/usr/bin/adb`; wakaru
command overridden per-test). Evidence written under `/tmp/r5audit/` only.

**Verdict line: all six files HOLD.** Four are fully clean; two carry minor
secondary-figure errata (locale count 88≠92 in 02; table census 15,992/31≠14,417/17
in 04) that do not touch any load-bearing claim. No file is REFUTED.

---

## File 01 — `2026-10-13-r4u-01-firmware-deep.md` → **HOLDS**

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `sha256sum` on all four blobs | `dcbdf512…`, `3a36ceb2…`, `d157e3b7…`, `c0156954…` — byte-exact | CONFIRMED |
| 2 | `inspect-firmware-regions` ×4 | RC=0 all; ucodes → 0 regions each, `signature_scan`; gsp_tu10x → **56** (elf 2, gpg_signed 50, zlib 2, sha256 1, srecord 1); gsp_ga10x → **156** (zlib 60, gpg 45, gzip 26, elf 13, srecord 5, compressd 4, sha256 2, copyright 1); provider argv `binwalk --quiet --search-all --threads 1 --log /tmp/rea-firmware-*/report.json <staged>` under prlimit — all exact | CONFIRMED |
| 3 | ucodes stub scan | tu10x last nonzero byte = 23; ga10x nonzero bytes confined to 0–23 (19 bytes); header `<8sIIII` = `NVUCODES`, ver 1, count 496/1315, tags `2bae986bab90198d`/`a3251724509f926f` byte-exact | CONFIRMED |
| 4 | `extract-firmware` ucodes | RC=0, `coverage:complete`, `files:[]`, `published_bytes:0`, empty out dir | CONFIRMED |
| 5 | readelf on both GSP wrappers | ELF64 REL RISC-V, 0 PH; tu10x 10 sections (.fwimage @0x40 = 0x1c01dc8, .fwversion=`610.57.04`, 3 `.fwsignature_*` @0x1000, symtab 4 syms); ga10x 19 sections (.fwimage 0x505b000, 12 `.fwsignature_*`); symtab build-path strings verbatim (`r610_85…LibOS_riscv64_release_firmware_tu10x_firmware_elf_stripped_*` / `ga10x_firmware_bin_*`) | CONFIRMED |
| 6 | carve @64 + readelf | embedded ELF64 EXEC RISC-V, entry 0x4009000, 31 PH, 37 SH at e_shoff=29,365,384 (true extent ≈29,367,752 — binwalk's 766,595 confirmed as inferred under-report) | CONFIRMED |
| 7 | ga10x .fwimage head + embedded ELFs | head bytes `97c2 0600 9382…` (RISC-V c-insns, no ELF magic) exact; spot-checked 3 of 12 embedded offsets (450624, 18939968, 19669056): all `\x7fELF` + e_type EXEC + e_machine 0xF3 (RISC-V) | CONFIRMED |
| 8 | `rea analyze` / `inspect` / `inspect-binary-layout` on RISC-V | wrapper REL → `target_unavailable` "unsupported ELF architecture" (exit-1 envelope); carved EXEC → identical refusal (architecture-wide confirmed); `inspect-binary-layout` → `unsupported_target` "requires x86-64 ELF objects" | CONFIRMED |
| 9 | Ghidra processor dirs | `ls ~/.local/opt/ghidra_12.1.4_PUBLIC/Ghidra/Processors` = **39**, includes `RISCV` | CONFIRMED |
| 10 | dd spot-checks | zlib @766659 = `78 da`; srecord @824363 = `53 30` ("S0") + binary, reported 13,756,760 B; gpg @14778314 = non-PGP binary bytes | CONFIRMED |
| 11 | entropy scan (256 KiB windows) | flat ~8.00 reproduced over 0x400000–0xbc0000; tails ~6.2–6.4 after | CONFIRMED |
| 12 | doctor/providers blind spot | `providerInspections` = ghidra+ida only; 0 `binwalk`/`unblob` occurrences in doctor and providers JSON; `extract_firmware` present in catalog | CONFIRMED |

Errata (cosmetic, non-load-bearing):
- gpg `reported_size` range claimed "5–30 B"; actual distribution is **5–85 B**
  (46/50 ≤30; outliers 32, 34, 85, 85). Substance — short-magic FPs — holds.
- ga10x embedded-ELF size band claimed "155,648–759,230 B"; actual
  **45,056–759,230** (two small regions at 45,056/53,248 under the stated floor).
- "`ucodes_ga10x` bytes 0–255 nonzero (range scan `[(0,256)]`)" — exact
  enumeration shows nonzero confined to 0–23, same as tu10x; consistent with a
  256-byte-granularity window scan, but the tuple reads as if nonzero extended
  to 255.
- Entropy "~3.5–6.4 through 0x0–0x3c0000" is approximate: windows hit 6.99
  @0xc0000 and 0.22 @0x380000 (zero-fill gap). Boundary claims exact.

## File 02 — `2026-10-13-r4u-02-jadx-decode.md` → **HOLDS** (one numeric erratum)

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `inspect-android-package` debug.apk | RC=0; `com.godot.game` v1, min 24/target 36, `permissions:[]`, manifest `complete` (incl. `android:debuggable="true"`), `class_count 1925`, `resource_count 129`, `signature_verification:not_performed`; bridge calls exactly `rea_jvm_status, load_apk, get_app_info, get_android_manifest`; engine jadx-headless-mcp 0.7.1 sha256 `6e5eacf5…` | CONFIRMED |
| 2 | `decode-android-resources` ×2 | Both runs → **byte-identical** `ev_a78193a347b799e7defa658c0a5a9c8abb593b6fef13c777c6608bc6ee9a1265` (== claimed id); `coverage:complete`, `decoded_file_count:232`, 11 strings, `subject:null`, `raw_result:null` | CONFIRMED |
| 3 | locales count | **`locales` = 88, not 92** (identical evidence id ⇒ identical payload ⇒ the file's "92" is a miscount; `af…zu`, `b+sr+Latn`, `en-rXC` all present) | **FAIL → erratum** |
| 4 | release APK | 1,920 classes / 121 resources; manifest `diff` vs debug = exactly `- android:debuggable="true"` | CONFIRMED |
| 5 | zip census + signing | debug 129 entries/13 dex, release 121/1 dex; release-only `assets/dexopt/baseline.prof{,m}` + `META-INF/version-control-info.textproto`; `APK Sig Block 42` count 0 and no `META-INF/*.SF|.RSA|.DSA` in **both** → unsigned | CONFIRMED |
| 6 | `search-android-classes ""` | 1,925 dbg / 1,920 rel, `complete`; set diff = exactly the 5 `kotlin.UByte$$ExternalSyntheticBackport1..5` | CONFIRMED |
| 7 | `inspect-android-class` GodotApp | 1 field (`updateWindowAppearance: Runnable`), 10 methods, `dex_descriptor:null` throughout | CONFIRMED |
| 8 | `inspect-android-method` onCreate | `representation:java`, `body_status:available`, `fell_back:false`, `overload_count:1`; body contains `SplashScreen`, `EdgeToEdge`; calls = `rea_jvm_status, load_apk, get_class_summary, get_method_body` | CONFIRMED |
| 9 | jadx evidence-id determinism | my `iap-debug` id `ev_b7940f34…` ≠ recorded `ev_d760cc5c…` (mkdtemp path in `raw_result`); apktool verb id reproduced exactly — both directions of candidate 5 hold | CONFIRMED |

Erratum: the 92-locale figure is wrong (measured 88 on byte-identical
evidence). Cosmetic; frontier note (92→88 `--locale` projections) adjusts to 88.

## File 03 — `2026-10-13-r4u-03-unblob-extract.md` → **HOLDS**

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `unblob --show-external-dependencies` | 15 rows: 5 ✓ (`7z, debugfs, lz4, simg2img, zstd`) / 10 ✗ incl. `sasquatch`, `sasquatch-v4be`, `unar` — verbatim matrix | CONFIRMED |
| 2 | `extract-firmware` ucodes_tu10x | RC=0, `coverage:complete`, `files:[]`, `published_bytes:0`, empty out dir; subject sha256 `dcbdf512…` matches | CONFIRMED |
| 3 | `extract-firmware` base-devel pkg (2,100 B) | zstd→tar→gzip chunks; 5 carved files with exact sizes (`.BUILDINFO` 4827, `.MTREE` 212, `.PKGINFO` 739, `gzip.uncompressed` 278, `zstd.uncompressed` 10240); `.PKGINFO` content verbatim (`makepkg 6.1.0`, `pkgname=base-devel`, `pkgver=1-2`); binwalk on same file = 0 signatures → dominance claim holds | CONFIRMED |
| 4 | `extract-firmware` Grok AppImage (134,055,925 B, sha256 `2fe7c5ac…` ✓) | ELF64 0–188392 carved (carved.elf sha256 `24da8e0e…30bc30` — exact), SQUASHFS_V4_LE 188392–133914600 preserved raw (133,726,208 B = 127.53 MiB), UNKNOWN tail 141,325 B; `ExtractorDependencyNotFoundReport` with `["sasquatch"]` in report | CONFIRMED |
| 5 | carve-then-7z fallback | `7z l` on the carved `.squashfs_v4_le`: `Type = SquashFS`, `Method = ZLIB`, `Cluster Size = 131072`, lists `.DirIcon` | CONFIRMED |
| 6 | per-run evidence ids | my runs mint fresh ids (`ev_a24c574f…`, `ev_cf12d2fe…`, `ev_0791ccc4…`) — consistent with "run-scoped, not content-stable" | CONFIRMED |

Notes: `coverage` on my pkg run reads `partial` (file claimed only 100% chunk
identification, which reproduces — `partial` is the depth-3 truncation signal).
Absent-output-dir precondition and binwalk's empty `.extracted` on the AppImage
are consistent with the file's operational warnings.

## File 04 — `2026-10-13-r4u-04-dnfile-il.md` → **HOLDS** (one numeric erratum)

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `inspect-managed-artifact` Pinta.Docking.dll | RC=0; **evidence id `ev_2fb95e88b4ba45bd073e4c3c359d4fd479aa10e9c02f4d723df5f2b075f5f8a3` reproduced exactly** (this verb is content-deterministic); machine_hex `0x014c`, pe32, runtime `2.5`, `il-only`, ep `none`, classification managed/modern-dotnet/anycpu; table_row_counts all exact (Module 1, TypeRef 65, TypeDef 16, Field 33, MethodDef 71, MemberRef 125, CustomAttribute 95, AssemblyRef 9, MethodSpec 14); MVID `75054b9e-826e-49b1-a752-57ebf762360a`; assembly `Pinta.Docking 3.1.2.0`; `coverage:complete`, `issues:[]` | CONFIRMED |
| 2 | `inspect-managed-members` Docking | RC=0; evid `ev_a2eab98c9bbf46ee…` prefix matches (deterministic); `coverage:partial`, exactly **21** `0x15` (GENERICINST) member issues, zero resource-limit; identical table_row_counts | CONFIRMED |
| 3 | `inspect-managed-members` Pinta.Core.dll | RC=0 but `coverage:unavailable` + `resource-limit metadata.representation "…exceeds the 67108864 byte representation budget"` verbatim | CONFIRMED |
| 4 | budget source | `ManagedDecodeBudget.js:4` = `const MAX_METADATA_REPRESENTATION_BYTES = 64 * 1024 * 1024;` — line-exact | CONFIRMED |
| 5 | dnfile/dncil on Pinta.Core.dll (venv `/tmp/dnfenv-r4`: dnfile 0.18.0, dncil 1.0.2, pefile 2024.8.26) | machine `0x14c`, `CLR_ILONLY`, EP token 0; TypeDef **380**, MethodDef **2,766**; bodies **2,594/2,594** (172 rva-0 skipped), **54,893** instrs, max 578 (`MoveNext` row 2720) — all exact | CONFIRMED |
| 6 | dnfile census figures | "14,417 rows across 17 counted tables" — **not reproduced**: summing all nonzero tables gives **15,992 rows / 31 tables**, and the file's own #~ stream `MaskValid` declares **31** table bits. Primary counts (TypeDef/MethodDef/bodies/instrs) are exact; only this secondary census figure fails | **FAIL → erratum** |
| 7 | entry-point mechanic on Pinta.dll | EP `0x0600007a` → MethodDef row 122 `Main`, owner TypeDef `MainClass`; 650/650 non-empty bodies, 17,523 instrs — exact | CONFIRMED |
| 8 | dnfile API notes | `pe.FILE_HEADER.Machine`, `pe.net.struct.EntryPointTokenOrRva`, ClrHeaderFlags enum — all behave as documented (my shim uses them verbatim) | CONFIRMED |

Erratum: Pinta.Core "14,417 rows / 17 tables" — correct figures are 15,992/31
under dnfile 0.18.0 (header Valid mask = 31 bits). No downstream claim depends
on it.

## File 05 — `2026-10-13-r4u-05-wakaru-oom.md` → **HOLDS**

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `runWakaruCommand` spawn shape | `WakaruCommand.js` (all three npx caches, 6.4.0): `:43` limiter = `REA_JAVASCRIPT_PRLIMIT_COMMAND ?? "/usr/bin/prlimit"`; `:63-73` `spawnOwnedProviderProcess` with `["--as=<as>","--fsize=<out>","--core=0","--cpu=120","--",cmd,…]`; child env = `{TMPDIR:cwd, RAYON_NUM_THREADS:"1", NO_COLOR:"1"}` merged over host env + `REA_PROCESS_RUN_ID` (ProviderProcess.js ~:19-22) — exact | CONFIRMED |
| 2 | limit constants | `WakaruRelease.js:26` `addressSpaceBytes: 1024*1024*1024` (also `outputBytes=128 MiB → --fsize=134217728`, `timeoutMs 120000`); `WakaruExecution.js:29-32` runs `["--version"]` through `runWakaruCommand` — line-exact | CONFIRMED |
| 3 | two-hop shim chain | `wakaru/bin/wakaru` = `#!/usr/bin/env node` + `spawnSync(process.execPath,…)`; `@wakaru/cli/bin/wakaru` = node shim with `PLATFORMS` map → `@wakaru/cli-linux-x64/wakaru`; native ELF exists, **26,793,296 B**, `ELF 64-bit pie x86-64 stripped` | CONFIRMED |
| 4 | literal probe repro | `prlimit --as=1073741824 --fsize=134217728 --core=0 --cpu=120 -- wakaru --version` (node shim) → FatalOOM `Failed to reserve virtual memory for CodeRange`; `prlimit --as=1073741824 -- node -e '1'` → same; `node --version` unaffected in spirit (no isolate) | CONFIRMED |
| 5 | native ELF under same limits | `wakaru 1.14.0`, rc=0 | CONFIRMED |
| 6 | e2e `recover-javascript-sources` (small JS file) | `REA_WAKARU_COMMAND=<native ELF>` → **rc=0**, Evidence envelope `ev_0e4f659a…`, probe `version.exit_code:0` stdout `"wakaru 1.14.0\n"`, `execution.exit_code:0`, `resource_limiter:/usr/bin/prlimit`, output dir populated (manifest/provenance/modules) | CONFIRMED |
| 7 | baseline control | `REA_WAKARU_COMMAND=<node shim>` → `{"code":"capability_unavailable","category":"unsupported_provider","retryable":false}`, stderr embeds `CodeRange` + `Isolate::Initialize` — verbatim gate repro | CONFIRMED |
| 8 | flake-band spot test | `--as=1153433600` (1.1 GiB) FAIL×3 SIGTRAP; `--as=1275068416` (~1.19 GiB) OK×3 — consistent with claimed ≤1 GiB deterministic-FAIL and OK-by-1.19 GiB observations; the ASLR-interleaved middle was not exhaustively re-bisected (inherently probabilistic) | CONFIRMED (endpoints) |
| 9 | `.bashrc:63` binding | **State evolution, not a refutation**: line 63 now carries the file's own suggested resolver (`export REA_WAKARU_COMMAND="$(find "$(npm root -g)/wakaru/node_modules/@wakaru/cli-linux-x64" …)"`) — operator applied the fix post-lane; current env resolves to the native ELF. The file documented the pre-fix `$(command -v wakaru)` binding, and the npm shim chain it described exists verbatim | CONFIRMED (as history) |

## File 06 — `2026-10-13-r4u-06-adb-surface.md` → **HOLDS**

| # | Check | Result | Verdict |
|---|-------|--------|---------|
| 1 | `inspect-adb-client` env-set | `ev_d850ccd0ada3e7b6d44a980b606a4842930413142ddfb933145a49a436f803e2` — **exact claimed id**; `binary_path:/usr/bin/adb`, `path_source:environment`, `contacted_adb_server:false` | CONFIRMED |
| 2 | `inspect-adb-client` env-unset | `ev_519f16a2d4d27145…` — matches claimed id; `path_source:path`, `binary_path:adb` — PATH fallback confirmed | CONFIRMED |
| 3 | `list-adb-devices` honesty | `devices:[]` matching `adb devices -l` (empty); deterministic `ev_d4d8cc77c3950870012fa3d41a0e810e1c569db0aad32e22cdef8b9f66e281db` across two runs — exact claimed id | CONFIRMED |
| 4 | daemon-start false negative | :5037 confirmed free before run → after `list-adb-devices` (`may_have_started_adb_server:false`) a fresh `adb -L tcp:5037 fork-server server` process is LISTENing — false-negative reproduced live | CONFIRMED |
| 5 | dead-serial taxonomy | `inspect-adb-device`/`list-adb-packages`/`pull-adb-file` (with required `device-path`) on `emulator-5554` → `unsupported_target`, retryable:false, "device 'emulator-5554' not found"; missing serial → `VALIDATION_ERROR` | CONFIRMED |
| 6 | divergent edges | `capture-adb-screen` → `unreadable_output` (binary path, no stderr classification); `push-adb-file` w/o `--overwrite` → `unreadable_output` "The device path already exists and overwrite was not requested" (false exists-verdict); `--overwrite` → `unsupported_target`; raw `adb -s emulator-5554 bugreport` prints `- waiting for device -` and parks (killed via timeout) | CONFIRMED |
| 7 | surface census | exactly **24** `*_adb_*` ops in `AdbProvider.js`; `adbCommands.js:30,35` = the only `args: z.object({})` (serial-free) — 22 serial-bound | CONFIRMED |
| 8 | source-line claims | classifier regexes (`unauthorized`, `device not found|offline|…`) at AdbProvider.js:91-106; `BUGREPORT_TIMEOUT_MS = 600_000` at :46; deviceExists probe with "authorization/refusal states surface on push instead" at ~:899-911 | CONFIRMED |
| 9 | doctor blind spot | `providerInspections` = `ghidra`,`ida` only; adb present only in `identity.catalog.tools` | CONFIRMED |

## Cross-cutting observations

- **Determinism asymmetry verified across providers**: `inspect-managed-*` and
  `decode-android-resources`/adb verbs mint content-deterministic evidence ids
  (three claimed ids reproduced byte-exactly); jadx and unblob verbs mint
  per-run ids (all of mine differ). This validates files 02/03's determinism
  claims and lets future lanes cheaply cross-check those providers.
- Host drift since r4u: `.bashrc:63` now binds the wakaru native ELF via the
  file's suggested `find $(npm root -g)` resolver — the fix landed; the corpus
  entry correctly documents the pre-fix state and even proposed this exact
  change. Consider a one-line corpus note that the operator applied it.
- adb daemon left running by my probes was killed after testing (`adb
  kill-server`; :5037 free, no adb procs). Other lanes' `rea-agents mcp` and
  Ghidra `AnalyzeHeadless` processes were observed and left untouched.
- All scratch under `/tmp/r5audit/`; no repo files touched.

## Summary

The r4u unlock wave survives adversarial re-verification: **6/6 HOLD**. Every
load-bearing claim reproduced — firmware region censuses and ELF carve-truths,
the full jadx/apktool verb surface incl. evidence-id determinism asymmetry,
unblob coverage dominance + sasquatch gap, the REA-managed/dnfile split incl.
the 64 MiB budget source line, the complete wakaru OOM causal chain (prlimit
wrap → node shim → V8 CodeRange → native-ELF fix → first successful
`recover-javascript-sources`), and the device-free adb taxonomy. Two cosmetic
numeric errata (locales 88≠92; Pinta.Core census 15,992/31≠14,417/17) and a few
range-bound imprecisions (gpg sizes 5–85; ga10x ELF sizes ≥45,056) should be
noted in the corpus but do not weaken any verdict. The adb daemon telemetry
false-negative and the pre-fix `.bashrc` binding are confirmed behaviors of the
host as documented.
