# kaidoku-r5 · 05-riscv-deep — `target_unavailable` IS bypassable: 2-byte `e_machine` patch + `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default` yields real RISC-V analysis through REA (94 procedures on carved EXEC); direct `analyzeHeadless` accepts the ELF with no patch at all and reaches 10,766 functions / 3.14 M instructions in a 900 s-capped pass

Axes: **coverage** (RISC-V moves from refused → analyzed: REA-routed results on bounded slices, direct-Ghidra full-file results), **evidence-fidelity** (the bypass provably works — but the Evidence envelope's `subject.architecture` records the *patched* value "arm64"; provenance is honest only if the patch is declared), **boundary-precision** (refusal located exactly: `binaryTarget.js:105` + `elfArchitecture` allowlist `:208-222`); **failure-honesty** (dead ends recorded verbatim: `.hop` route, `--target-format dos-com`, `extract-firmware` publishes nothing, 330 s→1800 s `provider_timeout`).

Env: `rea-agents@6.4.0` via npx (three identical npx-cache copies `9b9809298fe40d2c`, `af752b90495482d7`, `dea9475797100b20` — all 6.4.0, same file:line). Ghidra 12.1.4 at `~/.local/opt/ghidra_12.1.4_PUBLIC`, `JAVA_HOME=/usr/lib/jvm/java-21-openjdk` (OpenJDK 21.0.12.1). Host: 32 cores, 30 GiB RAM. Date: 2026-10-13. No repo files edited; no rea-agents dist modified; other lanes' `/tmp/rea-*` dirs untouched.

Subjects (`sha256sum`):
- `gsp_tu10x.bin` (outer REL wrapper) 29,381,504 B `d157e3b7dd5da2ca8d1ccb6ca98958f9e35d10a9ef7326277ebac133e4b0d1a7` (unchanged from r4u-01)
- `/tmp/r4u-embedded-elf.bin` (r4u truncated EXEC carve, 766,595 B) `a92cab9be14e5d3a80f9b64b589c0e9d61d334ac58f1e10d4d4ec2c96b92aad1` — survived in /tmp
- `/tmp/r5-gsp-tu10x-exec-full.bin` (full EXEC carve, 29,367,752 B @ offset 64) `eb4d76c4c3bb3045bafff132c6e4c1d04a538ab32e22a009134843a1fa5acefe` — new, this lane
- `/tmp/r5-embedded-elf-arm64patch.bin` (truncated carve, e_machine 243→183) `9eb8fc34a47875020ac486bacd65e11c357e01fa4eda20427816758fce635ee1` — new
- `/tmp/r5-gsp-tu10x-exec-arm64patch.bin` (full carve, e_machine 243→183) `1aa4061cfc8ab339cd5a2fe122d301dfc6bd4cdfae8b08e34e3cd8e761bbf997` — new
- `/tmp/r5-embedded-elf.hop` (truncated carve renamed, bytes identical to `a92cab9b…`) — new

## Candidate: refusal still fires verbatim — `rea analyze` on the unpatched carved EXEC → RC=1 `target_unavailable` "unsupported ELF architecture"

- claim: Re-ran `npx -y rea-agents@6.4.0 analyze /tmp/r4u-embedded-elf.bin --format json` → RC=1, error envelope byte-identical in shape to r4u-01's: `{"code":"target_unavailable","category":"unavailable","message":"Cannot open artifact: unsupported ELF architecture. …","retryable":false,"details":{"path":…,"reason":"unsupported ELF architecture"}}`. The gate is unchanged in 6.4.0 on this host.
- source: `/tmp/r5-analyze-embedded.json` (envelope), RC captured.
- verify: `npx -y rea-agents@6.4.0 analyze /tmp/r4u-embedded-elf.bin --format json; echo $?` → 1.
- verified-at: 2026-10-13
- suggested: admit — confirms r4u's baseline still holds before bypass work.

## Candidate: the refusal is a hard-coded 5-member e_machine allowlist in `dist/domain/binaryTarget.js` — `elfArchitecture()` maps {3:x86, 62:x86_64, 8:mips, 40:arm, 183:arm64}; EM_RISCV=243 falls through to `err("unsupported ELF architecture")` at line 105

- claim: `dist/domain/binaryTarget.js`: `parseElf` (line 91) reads `e_machine` at offset 18 (line 102) → `elfArchitecture(machine)` (line 103) → `if (architecture === undefined) return err("unsupported ELF architecture")` at **line 105**. The switch is at **lines 208–222** — five cases only, no 243. `dist/domain/binaryTargetTypes.js` corroborates: `BINARY_ARCHITECTURES = ["x86","x86_64","arm","arm64","mips"]`. Call site: `application/BinaryTargetResolver.js:256` inside `parseBinaryTarget` — its own docstring says this runs "before a provider is selected" (line 16). Error → `target_unavailable` projection at `domain/analysisErrorProjection.js:69-71` (`BinaryTargetError` with no `systemCode`). `rea capabilities` output contains zero `riscv` tokens. Every ELF-consuming verb funnels through this one parse; there is no per-verb escape.
- source: verbatim file reads at the npx paths above; `grep -rn "unsupported ELF architecture" dist/` → single hit.
- verify: `sed -n '91,105p;208,222p' ~/.npm/_npx/*/node_modules/rea-agents/dist/domain/binaryTarget.js`.
- verified-at: 2026-10-13
- suggested: admit — pins the gate to file:line and shows it's a parse-time allowlist, not a provider check.

## Candidate: bypass #1 works — patch `e_machine` 243→183 in a copy + `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default` → `rea analyze` RC=0 with `language_id:"RISCV:LE:64:default"`, 94 procedures, and a `csreg:0x0–0x8000` block (proof of real RISCV language load)

- claim: Env knob exists: `config/parseConfig.js:64-72` maps `REA_GHIDRA_LANGUAGE_ID` → `config.ghidraLanguageOverride`; `ghidra/GhidraLauncher.js:255-262` emits `-processor <languageId>` (and optional `-cspec`) in the analyzeHeadless argv when set. On the patched 766 KB carve: RC=0, evidence `ev_e9a735a2975120e5a8f06393808b0a3ddcf76a8944b7b515f7c34649d7b31df6`, `analysis_profile…language_id:"RISCV:LE:64:default"`, `language_selection:"configured-v1"`, `loader:"auto-from-header"`. `normalized_result`: `segment_count:8` including a `csr` block `csreg:0x0–csreg:0x8000` (32,768 B — `csreg` is the RISCV module's CSR register space; present in `riscv.reg.sinc`, `riscv64-fp.cspec`, `RV64.pspec`) and `procedure_count:94`. `rea inspect` on the same target + override → identical result shape. Verbatim provider argv observed on the full-file run: `AnalyzeHeadless … -import /tmp/rea-ghidra-*/target-1aa4061cfc8a.bin -processor RISCV:LE:64:default -readOnly -deleteProject …` (staged copy named for patched sha256). **Caveat (evidence-fidelity):** `subject.architecture:"arm64"` in the envelope is the *patched* header value — REA's identity record lies wherever the patch does; `subject.digest.sha256` is the patched copy's hash. The analysis itself is honest RISC-V; the manifest is not.
- source: `/tmp/r5-bypass-analyze.json`, `/tmp/r5-bypass-inspect.json`; `ps aux` argv capture; Ghidra RISCV ldefs (`id="RISCV:LE:64:default"`, compiler `gcc` → `riscv64-fp.cspec`).
- verify: `printf '\xb7\x00' | dd of=<copy> bs=1 seek=18 conv=notrunc` then `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default rea analyze <copy> --format json` → `language_id:"RISCV:LE:64:default"`, `procedure_count:94`.
- verified-at: 2026-10-13
- suggested: admit — the gate is proven bypassable end-to-end through REA; the trade is a 2-byte artifact mutation + an architecture mislabel in the envelope. This is the route for bounded slices.

## Candidate: control — patched file WITHOUT the override → `rea analyze` RC=0 but `language_id:"auto-from-header"` (arm64), `procedure_count:0`, no `csr` block: the patch alone opens the gate, the env override is what produces real RISC-V analysis

- claim: `rea analyze /tmp/r5-embedded-elf-arm64patch.bin` (no env) → RC=0 `ev_…`, `language_id:"auto-from-header"`, `language_selection` absent → Ghidra auto-selected AARCH64 (from patched e_machine), loaded the same 7 segments, found **0 procedures**. Paired with the bypass run this isolates the mechanism: e_machine patch satisfies `elfArchitecture()`; `REA_GHIDRA_LANGUAGE_ID` steers Ghidra's language back to RISCV despite the patched header.
- source: `/tmp/r5-control-arm64.json` (2,684 B).
- verify: diff the two runs' `analysis_profile…language_id` and `procedure_count`.
- verified-at: 2026-10-13
- suggested: admit — a clean A/B: same bytes, same verb, only the env var differs; 0 vs 94 procedures.

## Candidate: bypass #2 — no patch needed at all if you leave REA: `analyzeHeadless` accepts the carved EXEC directly, auto-detects `RISCV:LE:64:default:gcc`, and (900 s-capped analysis) reaches 39 blocks / 10,766 functions / 3,141,043 instructions / 37,455 defined data / 42,057 symbols; entry disassembles to real RV64 (`addiw/slli/lw/beq` on a chip-ID read)

- claim: `analyzeHeadless /tmp/r5-ghidra-proj r5test -import /tmp/r5-gsp-tu10x-exec-full.bin -readOnly -noanalysis` → `Using Loader: Executable and Linking Format (ELF)`, `Using Language/Compiler: RISCV:LE:64:default:gcc`, `Import succeeded`, RC=0. Full run `-postScript R5Counts.java -analysisTimeoutPerFile 900 -max-cpu 8`: auto-analysis **timed out at 900 s** (partial state saved to project) — then a corrected postScript on the saved program (`-process … -noanalysis -readOnly`) reported: `RISCV:LE:64:default` / cspec `gcc`; 39 memory blocks totaling 29,932,990 B; 7 execute blocks incl. `.section_task_rm_elf_text_instance` @ram:0x04bfa000 size 16,732,160 (the ~16 MB RM task text), `.ga100_text`/`.tu10x_text` @0x4005000/0x4007000, `.bootstrap` @0x4009000, resident texts, plus the `csr` block; `R5_FUNCTIONS=10766`, `R5_INSTRUCTIONS=3141043`, `R5_DEFINED_DATA=37455`, `R5_SYMBOLS=42057`. Entry @0x4009000 = function `entry`; first instructions `addiw t0,zero,0x1; slli t0,t0,0x31; addi …; lw t0,0x0(t0); srli t0,t0,0x14; andi t0,t0,0x1ff; li t1,0x162; beq …` — coherent RV64 (a hardware-ID read+compare). The outer REL wrapper *also* imports (`-noanalysis` → same `RISCV:LE:64:default:gcc` detection, RC=0) but with 0 program headers it loads as sections — the carved EXEC remains the right analysis target. Resource cost: import ~seconds; auto-analysis capped at 900 s and incomplete (analyzer table: Reference 28.8 s, Subroutine References 17.7 s, …); `-process` re-open + counts ~1 min.
- source: `/tmp/r5-ghidra-run.out`, `/tmp/r5-ghidra-analysis.log`, `/tmp/r5-ghidra-scripts/R5Counts.java` + `R5Entry.java` outputs; saved project `/tmp/r5-ghidra-proj2/r5full`.
- verify: `analyzeHeadless <proj> r5full -process r5-gsp-tu10x-exec-full.bin -noanalysis -postScript R5Counts.java -readOnly` → the R5_* lines above.
- verified-at: 2026-10-13
- suggested: admit — Ghidra's RISCV loader works natively on this firmware; full-function analysis of 29 MB exceeds 900 s, so bounded windows or longer budgets are the practical route. REA cannot reproduce these counts until its own timeout is beaten.

## Candidate: REA-route scaling limit — the full 29 MB patched EXEC hits typed `provider_timeout` at `timeout_ms:330000` (default) and at `1800000` when raised via `REA_GHIDRA_STARTUP_TIMEOUT_MS`; the env knob is honored but 30 min still wasn't enough (`operation:"list_documents"`)

- claim: `config/ghidraStartupTimeout.js:3` — `DEFAULT_GHIDRA_STARTUP_TIMEOUT_MS = 330_000`, described as the "absolute deadline for Ghidra import, analysis, bridge, and readiness". First full-file bypass run → `{"code":"provider_timeout","details":{"operation":"list_documents","timeout_ms":330000}}`. Retry with `REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000` → same envelope with `timeout_ms:1800000` — the override provably propagated (330000→1800000), and analysis still wasn't done. Consistent with the direct run's 900 s auto-analysis timeout: ~17 MB of execute-section RV64 needs more than half an hour under REA's launch profile.
- source: `/tmp/r5-bypass-full-analyze.json`, `/tmp/r5-bypass-full-analyze2.json` (365/364 B envelopes).
- verify: rerun with the env var; `timeout_ms` in the envelope tracks the setting.
- verified-at: 2026-10-13
- suggested: admit — bypass works mechanically at any size, but REA-mediated results are practical only for bounded slices (≤ ~1 MB proved ~50 s end-to-end); the full EXEC currently belongs to direct `analyzeHeadless`.

## Candidate: dead ends recorded — `.hop` rename skips the ELF parse but every provider refuses `database` kind; `--target-format` only offers `dos-com` capped at 0xff00 B; `extract-firmware --offset/--length` verifies but does not emit the slice

- claim: (i) `cp embedded-elf.bin x.hop; rea analyze x.hop` → resolver takes the `kind:"database"` route (`BinaryTargetResolver.js:61-69`, `architecture:null` — RISC-V never checked) then provider selection fails: ghidra `target_kind_unsupported` ("Ghidra v1 imports executable targets, not database targets"), hopper `executable_missing` (/opt/hopper absent), ida `not_configured` + `target_kind_unsupported` → `provider_unavailable` RC=1. Parse-bypass exists; no provider accepts it. (ii) `analyze --target-format` help: only "headerless DOS COM interpretation"; `domain/dosCom.js:6` caps length at `0xff00` — a 29 MB (or 766 KB) ELF cannot ride it. (iii) `extract-firmware gsp_tu10x.bin <dir> --offset 64 --length 29367752` → RC=0 `coverage:"complete"`, `selection.sha256 == eb4d76c4…` (byte-identical to my `tail|head` carve), unblob tags the chunk `handler:"elf64"` — but `files:[]`, `published_bytes:0`: unblob's elf64 handler recognizes yet cannot decompose an ELF, so the verb proves the slice without publishing it. `dd`/`tail` remains the carving method.
- source: `.hop` rejection JSON (verbatim candidate_ids + rejections), `--help` output, `/tmp/r5-ef-carve.json`.
- verify: rerun each; all three reproduce typed refusals/zero-publish.
- verified-at: 2026-10-13
- suggested: admit — negative space now pinned: there is no *unmodified-artifact* path through REA for RISC-V; the only REA route is the documented 2-byte patch + env override, else direct Ghidra.

## Run log

| # | Command | Result |
| - | ------- | ------ |
| 1 | `rea analyze /tmp/r4u-embedded-elf.bin` | RC=1 `target_unavailable` (r4u refusal stands) |
| 2 | `tail -c +65 gsp_tu10x.bin \| head -c 29367752 > r5-gsp-tu10x-exec-full.bin` | full EXEC carve 29,367,752 B `eb4d76c4…` (ELF64 EXEC RISC-V, entry 0x4009000, 31 PH/37 SH) |
| 3 | `readelf -h` on carve | confirmed EXEC/RISC-V, e_shoff consistent with true extent |
| 4 | `grep/sed` through `rea-agents@6.4.0 dist/` | gate at `domain/binaryTarget.js:105` + `elfArchitecture` `:208-222` ({3,62,8,40,183}, no 243); call site `BinaryTargetResolver.js:256`; projection `analysisErrorProjection.js:69-71`; `BINARY_ARCHITECTURES` 5-member list |
| 5 | `rea analyze --help` | options: `--snapshot`, `--target-format` (dos-com only), `--provider`, `--integrity-policy` — no arch override |
| 6 | `analyzeHeadless … -import r5-gsp-tu10x-exec-full.bin -readOnly -noanalysis` | RC=0 `Using Language/Compiler: RISCV:LE:64:default:gcc`, `Import succeeded` |
| 7 | python patch e_machine 243→183 on both carves | `9eb8fc34…` (766 KB), `1aa4061c…` (29 MB); readelf now reports AArch64 |
| 8 | `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default rea analyze r5-embedded-elf-arm64patch.bin` | RC=0 `ev_e9a735a2…`, `language_id:"RISCV:LE:64:default"`, 8 segments incl `csr`, **94 procedures** (~50 s) |
| 9 | same, no env (control) | RC=0 `auto-from-header` (arm64), **0 procedures** |
| 10 | `REA_GHIDRA_LANGUAGE_ID=… rea inspect` patched carve | RC=0 same result shape (94 proc) — verb breadth ≥2 |
| 11 | `analyzeHeadless -import full carve -postScript R5Counts.java -analysisTimeoutPerFile 900 -max-cpu 8` | analysis timeout at 900 s; program saved to `r5full` project; first script attempt failed compile (`Listing.getFunctionCount` not a method — fixed to `FunctionManager`) |
| 12 | `-process r5-gsp-tu10x-exec-full.bin -noanalysis -postScript R5Counts/R5Entry` | 39 blocks / 29,932,990 B / **10,766 functions / 3,141,043 instr / 37,455 data / 42,057 syms**; 7 exec blocks (`.section_task_rm_elf_text_instance` 16.7 MB @0x04bfa000 …); entry = real RV64 sequence |
| 13 | `rea analyze` full patched EXEC (default timeout) | RC=1 `provider_timeout` `timeout_ms:330000` op `list_documents` |
| 14 | same + `REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000` | RC=1 `provider_timeout` `timeout_ms:1800000` — knob honored, still not enough |
| 15 | `cp → .hop; rea analyze` | RC=1 `provider_unavailable`; resolver took database route (arch never parsed) but ghidra/hopper/ida all refused `database` kind with typed rejections |
| 16 | `extract-firmware gsp_tu10x.bin <dir> --offset 64 --length 29367752` | RC=0 `coverage:"complete"`, selection sha256 `eb4d76c4…` == my carve, chunk `handler:"elf64"`, `files:[]` published:0 — verifies, does not emit |
| 17 | `analyzeHeadless -import gsp_tu10x.bin` (outer REL) | RC=0 `RISCV:LE:64:default:gcc`, `Import succeeded` (sections-only load; 0 PH) |
| 18 | `rea capabilities` / `list-architectures` probes | capabilities contains zero `riscv` tokens; list-architectures is a macOS-only verb (`capability_unavailable`) |

## Summary

**`target_unavailable` is bypassable — two proven routes, one through REA and one around it.** The refusal is a parse-time allowlist, not a missing engine: `dist/domain/binaryTarget.js:105` returns `err("unsupported ELF architecture")` whenever `elfArchitecture()` (`:208-222`) misses its five cases {x86:3, x86_64:62, mips:8, arm:40, arm64:183}; EM_RISCV=243 has no case, and `BINARY_ARCHITECTURES` in `binaryTargetTypes.js` matches. Route A (REA-mediated): copy the ELF, patch bytes 18–19 `f3 00`→`b7 00` (e_machine→AArch64), then `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default rea analyze <copy>` — the env override (`config/parseConfig.js:64-72` → `ghidraLanguageOverride` → `-processor` in `GhidraLauncher.js:255-262`) forces Ghidra's language back to RISCV. Verified end-to-end: RC=0, 94 procedures + `csreg` block on the 766 KB carve in ~50 s, control run without the env var gives 0 procedures as arm64. Costs honesty tax: the envelope records `architecture:"arm64"` and the patched sha256 — declare the patch wherever the evidence is cited. Route B (direct Ghidra): unpatched carved EXEC imports natively (`RISCV:LE:64:default:gcc` auto-detected; even the outer REL wrapper imports), and a 900 s-capped auto-analysis already yields 10,766 functions / 3,141,043 instructions / 39 blocks with a readable RV64 entry sequence — Ghidra's RISCV module is fully working on this host; REA's preflight is the only wall. Scaling limit measured both ways: REA's absolute session deadline (`REA_GHIDRA_STARTUP_TIMEOUT_MS`, default 330 s) kills the 29 MB target at `list_documents` even when raised to 1800 s — keep REA-route slices ≲1 MB, or go direct for the full firmware. Dead ends pinned: `.hop` rename skips the parse but no provider accepts `database` kind; `--target-format dos-com` caps at 0xff00 B; `extract-firmware --offset/--length` verifies a slice's sha256 but publishes 0 files (unblob's elf64 handler doesn't decompose ELF). Suggested corpus entry: "RISC-V via REA = patch e_machine + `REA_GHIDRA_LANGUAGE_ID=RISCV:LE:64:default`, bounded slices; full GSP EXEC = direct `analyzeHeadless`, budget >30 min for complete auto-analysis."
