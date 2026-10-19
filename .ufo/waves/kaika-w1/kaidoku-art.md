# kaika W1 — ART dossier — lane `kaidoku` (shipped-artifact RE with REA)

Scout: W1ArtKaidoku · date 2026-10-19 · repo read-only `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`
(all `corpus/…`, `PROVINCE.md`, `SKILL.md` commands below run with that repo as cwd).

**Tooling note.** `web_search` was available. Blocked fetches: IEEE Xplore (bot wall) and ACM DL (HTTP 403) —
the S&P 2022 SoK abstract was read via `api.semanticscholar.org` instead; the ACM 2025 EIR paper stays a lead.
Unauthenticated GitHub API calls from `curl` hit HTTP 403 rate limits partway through (the `read` tool still
worked). **Prompt injection:** none of the fetched content carried instructions aimed at the agent. Two tier-C
pages (S029, S030) carried promotional claims and links. They were treated as data and rejected below.
**Hand-off:** STATE drift sent to `W1StateKaidoku` (recorded there as D14): a fourth `rea-agents` npx cache
`~/.npm/_npx/9b9809298fe40d2c` (6.7.0) is missing from `PROVINCE.md:19-23`. The peer verified it comes from an unpinned
`rea-agents` spec and has a byte-identical payload to `a1722018…`. The two mtime readings are both right: the dir is
15:19:40 -0300, `package.json` files are 10:06:03 -0300.

---

## 1. Uncovered ground (held vs. not held)

**Held (from the index).** 90 knowledge entries (`ls corpus/knowledge/*.md | wc -l`), split by date as
62×10-13 / 10×10-14 / 7×10-16 / 2×10-18 / 9×10-19
(`ls corpus/knowledge/*.md | sed -E 's#.*/(2026-10-[0-9]{2}).*#\1#' | sort | uniq -c`). 10 lessons
(`ls corpus/lessons/*.md | wc -l`). QUALITY bar: 15 admission criteria
(`sed -n '/^## Admission/,/^## Signals/p' corpus/QUALITY.md | grep -cE '^\| [0-9]+ \|'`) plus 6 weak-material
signals (`sed -n '/^## Signals/,$p' corpus/QUALITY.md | grep -cE '^\| [0-9]+ \|'`). 54 coverage-map rows
(`sed -n '/^## Coverage map/,/^## Knowledge/p' corpus/README.md | grep -cE '^\| [^-s]'`). Frontier bullets: 10 in
`corpus/README.md` (`sed -n '/^## Frontier/,/^## Known gaps/p' corpus/README.md | grep -c '^- '`), 5 in PROVINCE
Frontier (`sed -n '/^## Frontier/,/^## Adjacent/p' PROVINCE.md | grep -c '^- \*\*'`), and 8 in PROVINCE Round-4
frontier (`sed -n '/^### Round-4 frontier/,$p' PROVINCE.md | grep -c '^- \*\*'`). SKILL.md has 11 headings
(`grep -cE '^#{1,4} ' SKILL.md`).
The held ground is REA operation on this host:
- doctor and session verdicts
- the Ghidra 12.1.4 provider: ELF jq/libjq; PE x86-64/ARM64; the 91.6 MB ARM64 PE wall
- Electron/ASAR: obsidian, signal, 1Password, typora `.jsc` disassembly; the nine-fuse sentinel
- APK/AppImage/pacman archives, managed IL, crashes ≤32 MiB, firmware (binwalk/unblob)
- CDP runtime observation, EVM selectors
- the evidence-id domain per verb family
All of it was learned from **tool runs**. External sources appear only as tool pointers (e.g. jsc2js/jscd in
`corpus/knowledge/2026-10-13-r4-07-jsc-bytecode.md:152,186-188`); there is no curated registry (see the first row below).

**Not held (each row carries its sweep).**

| ground | corpus sweep (count — command) | host / REA state | why it matters |
|---|---|---|---|
| External source registry | 0 — `ls corpus/SOURCES.md 2>/dev/null \| wc -l` | — | the corpus has no curated "where to learn more" registry |
| LLM-assisted decompilation evaluation | 0 — `grep -rliE 'LLM4Decompile\|DecompileBench\|re-executab' corpus \| wc -l` | — | evidence authority of LLM-refined pseudocode (§4 K3) |
| Binary lifting / IR | 0 — `grep -rliE 'remill\|binary lift\|lifter' corpus \| wc -l` | rizin RzIL, Ghidra p-code in use, but not studied | which lifted IR supports which claims |
| rizin / Cutter verbs | 0 — `grep -rliE 'execute.rizin.command\|rizin.debug.session\|cutter.command' corpus \| wc -l` | REA 6.5.0 and 6.7.0 dist name `execute_rizin_command` (12 files each), `start_rizin_debug_session` (10), `cutter_command` (11 / 12) — `grep -rlo '"execute_rizin_command"' ~/.npm/_npx/a1722018f28f9df2/node_modules/rea-agents/dist \| wc -l`; `command -v rizin` → absent | a declared provider that has never been exercised (§4 K5) |
| Go ≥ 1.26 symbol-recovery mechanism | GP-6528: 0 — `grep -rli 'GP-6528' corpus \| wc -l`; go1.26 mentions: 3 — `grep -rliE 'go1\.26' corpus \| wc -l` | Ghidra 12.1.4 gates Go at 1.15–1.25 | r4-10's collapse is left "observed-not-cited" (`corpus/knowledge/2026-10-13-r4-10-real-version-pair.md:70-73`) (§4 K1) |
| Name-free cross-version pairing (BSim, ghidriff) | ghidriff 0 — `grep -rli 'ghidriff' corpus \| wc -l`; BSim 1 (install listing only) — `grep -rli 'BSim' corpus \| wc -l` | BSim installed (ChangeHistory.md:844, GP-5435) | r4-10: "pair by ELF role/address, not symbol name" has no tool behind it |
| Electron code outside the ASAR (V8 heap snapshots) | 0 — `grep -rli 'v8_context_snapshot' corpus \| wc -l`; CVE-2025-55305: 0 | `/usr/lib/signal-desktop/v8_context_snapshot.bin` is present | ASAR-only findings say nothing about snapshot content (§4 K2) |
| `.jsc` → source (beyond disassembly) | View8: 2 files, frontier mentions only — `grep -rli 'View8' corpus \| wc -l` | r4-07 ranks paths but has no 2026 pipeline | S025/S026 |
| Mach-O on Linux (ipsw, LIEF) | 0 / 0 — `grep -rli 'ipsw' corpus \| wc -l`; `grep -rliw 'lief' corpus \| wc -l` | macOS-only REA ops are `unsupported_host` | Linux-capable DSC/Mach-O routes exist (S027) |
| ARM64EC / ARM64X | 2 files, frontier mentions only — `grep -rliE 'ARM64EC\|ARM64X' corpus \| wc -l` | no carrier on host | named frontier with a concrete tool gap (§4 K6) |
| Adversarial content in LLM-assisted RE | prompt injection 0 — `grep -rliE 'prompt.injection' corpus \| wc -l`; `untrusted_content` 0 — `grep -rliE 'untrusted_content\|untrusted content' corpus SKILL.md \| wc -l` | REA marks target content `_meta.provenance.untrusted_content` (server instructions) | §4 K4 |
| Dart AOT / Flutter | 0 — `grep -rliE 'dart_aot\|dart-aot\|flutter' corpus \| wc -l` | REA dist names `identify_flutter_build` (11 files), `inspect_dart_aot` (14) | S016 |
| WASM | 0 — `grep -rliE 'inspect.wasm\|wabt' corpus \| wc -l` | REA dist names `inspect_wasm_artifact` (15 / 16 files); key `REA_WABT_BIN_DIRECTORY` | — |
| debuginfod DWARF for Arch binaries | 0 — `grep -rli 'debuginfod' corpus \| wc -l` | `DEBUGINFOD_URLS=https://debuginfod.archlinux.org` (`/etc/debuginfod/archlinux.urls`); Ghidra 12.1 supports it (WhatsNew.md:115-118); use from REA headless runs is **unknown** | could turn `FUN_*` inference into DWARF-named observation |
| Ghidra Swift demangling | 0 — `grep -rliE 'GHIDRA_SWIFT_DEMANGLER\|swift-demangle' corpus \| wc -l` | `command -v swift-demangle swift` → none; 12.1.4 requires the env var or a known location (GP-7238) | Swift ELF/Mach-O names stay mangled on this host |

---

## 2. Current art 2025–2026 the corpus does not hold

**Ghidra (the provider REA runs; installed 12.1.4, build 2026-09-21)**
- **Go 1.26 is fixed only on master.**
  - Installed state: Go support is gated at `"1.15-1.25"` (S003, GoRttiMapper.java:79). The analyzer bootstraps from version-keyed `go<maj>.<min>.0.json` snapshots — 11 installed, the last is go1.25.0 (`ls $GHIDRA_INSTALL_DIR/Ghidra/Features/Base/data/typeinfo/golang/*.json | wc -l`).
  - Upstream: GP-6528 adds go1.26.0.json (10,556,117 B) and widens the gate to `"1.15-1.26"` (S004, master GoRttiMapper.java:79). It landed 2026-03-03.
  - No release carries it yet: the newest GitHub release is `Ghidra_12.1.4_build`, published 2026-09-21T17:38:59Z (`api.github.com/repos/NationalSecurityAgency/ghidra/releases?per_page=4`), and `grep -c GP-6528 $GHIDRA_INSTALL_DIR/docs/ChangeHistory.md` → 0.
- **12.1 headline features** (S002):
  - the decompiler now recovers bitfield names (WhatsNew.md:85)
  - the Objective-C analyzers were rewritten, with `_objc_msgSend` resolution and AARCH64 ARC call-fixups (:96-113)
  - DWARF can be fetched from debuginfod (:115-118)
  - Jython moved to an extension
- **12.1.x patch-level changes that affect REA runs** (S001):
  - the Swift demangler needs `GHIDRA_SWIFT_DEMANGLER` (GP-7238, :4); 12.1.3 expects swift on `PATH` (GP-7045, :30)
  - `ElfLoader` recognizes Swift and golang binaries (GP-3960, :236)
  - the Golang analyzer handles some obfuscation (GP-6291, :168)
  - the Rust demangler was ported from the official Rust implementation (GP-6108, :211-212)
  - `dyld_shared_cache` parsing is safer (GP-7046, :34)
  - the Headless Analyzer no longer writes user preferences (GP-7096, :32)
- **12.0 changes** (S001):
  - PyGhidra 3.0.0 ships (GP-5637, :654), and Python scripts now default to PyGhidra (GP-5415, :653)
  - experimental Z3 symbolic emulator (GP-5727, :569)
  - LiSA abstract interpretation over low p-code (GP-5566, :568)
  - RISC-V CSRs moved into their own memory space (GP-5975, :649) — relevant to r5-01's RISC-V bypass
  - a headless `-mirror` option exists (12.0 What's New, read on the ghidradocs.com mirror: https://www.ghidradocs.com/12.0.3_PUBLIC/docs/WhatsNew.html)
- BSim is installed by default since 11.4 (GP-5435, :844). Its features are name-, constant- and type-free (S005).

**rizin / Cutter.**
- rizin v0.9.0 (2026-06-21), followed by the 0.9.1 patch (2026-06-29) (S008):
  - project format bumped 19→25
  - ESIL isolated and still deprecated
  - RzIL uplift for x86 SSE/SSE2 floating point and a full SPARC lifter
  - Swift demangling moved to the external `rz-libswift`
- Cutter 2.5.0 (2026-06-30) uses Rizin v0.9.1 and can query debuginfod servers from the analysis dialog (https://github.com/rizinorg/cutter/releases/tag/v2.5.0, read through the GitHub API).
- REA 6.7.0 resolves its rizin provider as `REA_RIZIN_COMMAND ?? "rizin"` and launches it with `-N -0 -d` (`~/.npm/_npx/a1722018f28f9df2/node_modules/rea-agents/dist/rizin/RizinDebugSessionManager.js:109,183-185`).

**JADX.** 1.5.6 (2026-07-10) adds zip-entry path rejection, XML-bomb hardening and a call-graph module (S009). Host `jadx --version` → 1.5.6, which r11-02:191 also records. REA itself drives jadx-headless-mcp 0.7.1, so the jar pin is unaffected.

**Binary lifting.**
- remill lifts instructions accurately and is meant to be used as a library (S010).
- The canonical SoK (S011): lifted IR is "unsuited to rigorous static analysis (e.g., pointer analysis)" but suits diffing and decompilation.
- 2026 current art: LLM retrieval plus a verification loop lifts optimized x86-64/ARM64 code to LLVM IR with >30% higher re-executability than the strongest general LLM baseline (S012). RzIL uplift is growing too (S008).

**LLM-assisted decompilation: evaluation has caught up with the claims.**
- The re-executability metric and the "refine Ghidra pseudocode" model family come from LLM4Decompile (S013).
- DecompileBench (S014): LLMs beat commercial decompilers on understandability "despite 52.2% lower functionality correctness".
- Decompile-Diverge, 2026-09 (S015):
  - outputs that pass every test still diverge in behavior: 4.9% overall, up to 13% for one system
  - LLM refinement of Ghidra output raises the build rate from 75% to 90% while Matched falls from 74% to 62%
  - up to a tenth of CVE functions show "Crash Absence"
- Dart AOT, 2026-07 (S016): only 21.0–23.3% of compiling candidates pass. Removing semantic names drops coverage from 42/154 to 7/154 tasks — names leak the specification.

**LLM agents doing RE.**
- Reveree (S017): failures concentrate in the comprehension stages, and more budget rescues few of them.
- SRE-Bench (S018): frontier agents fully solve 26.9–31.5% of realistic, contamination-free instances.
- RARE (S019): binary-derived text must not gain tool or evidence authority, and multi-tool views of one binary are not independent evidence.

**Electron / ASAR / V8.**
- Fuses (S020, S021): nine fuses, including `wasmTrapHandlers`. The wire format is the sentinel `dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX`, a version byte, a length byte, and one byte per fuse (`0`/`1`/`r`). This matches the nine-state fingerprint in `corpus/knowledge/2026-10-16-l7-03-inspect-electron-fuses.md:12`.
- ASAR integrity is enforced only on macOS (Electron ≥16) and Windows (≥30) (S022). This corroborates l7-03:15's tool-reported limitation.
- CVE-2025-55305 (S023, S024): V8 heap snapshots are code-bearing and sat outside the integrity fuses. Fixed in 35.7.5 / 36.8.1 / 37.3.1 / 38.0.0-beta.6.
- `.jsc` decompilation, 2026 state (S025, S026): a version-matched patched-V8 disassembler feeds View8, then deobfuscation passes. `--normalize` gives deterministic, parse-order function names, which addresses r4-07's 115–116-block nondeterminism band.

**Mach-O / PE on a Linux host.**
- `ipsw dyld extract` runs on all platforms and emits standalone, Ghidra-loadable dylibs (S027).
- LIEF parses CHPE metadata and gives a relocated nested ARM64EC view of ARM64X PEs (S028).
- LIEF 0.17.0 states that Ghidra 11.4.2 is "not able to accurately process Windows ARM64EC binaries" (https://lief.re/blog/2025-09-14-lief-0-17-0/, section "Reverse Engineering Plugins").
- The installed 12.1.4 ChangeHistory has no ARM64EC/ARM64X/CHPE entry: `grep -ciE 'arm64ec|arm64x|chpe' $GHIDRA_INSTALL_DIR/docs/ChangeHistory.md` → 0.

**Diffing and Go symbol recovery.**
- ghidriff (S006):
  - SimpleDiff relies on symbol names
  - VersionTrackingDiff uses correlators, plus BSim correlation (on by default)
  - targets Ghidra 12.0.4 with pyghidra 3.x
- GoReSym (S007): a Ghidra-independent pclntab/moduledata parser covering layouts up to the 1.20 format, with a `-v` version override.

---

## 3. SOURCES.md rows (contract format; 30 rows: 26 A / 2 B / 2 C)

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Ghidra Change History 12.1.4 (installed copy) — /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/docs/ChangeHistory.md | docs | A | GP-numbered changes per release for the provider REA runs — Swift demangler env GP-7238 (:4), Go 1.24/1.25 json bootstrap GP-5470 (:585), ElfLoader Swift+golang GP-3960 (:236), BSim default GP-5435 (:844) | queued | 2026-10-19 | on-release | — |
| S002 | What's New in Ghidra 12.1 (installed copy) — /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/docs/WhatsNew.md | docs | A | 12.1 headline changes: decompiler bitfield names (:85), rewritten Objective-C analyzers + AARCH64 ARC call-fixups (:96-113), debuginfod DWARF download (:115-118), Jython moved to an extension | queued | 2026-10-19 | on-release | — |
| S003 | Ghidra 12.1.4 Base sources — Ghidra/Features/Base/lib/Base-src.zip (sha256 f00d29c20119562eca7efd2740e8c67257ebd63ea24a3dfbc4dbbb9187a8d804) members golang/rtti/GoRttiMapper.java and GoApiSnapshot.java | code | A | Go analyzer gate: SUPPORTED_VERSIONS 1.15-1.25 (:79), version-keyed json bootstrap returning EMPTY when missing (GoApiSnapshot :102-126), then BootstrapInfoException (:359) | queued | 2026-10-19 | on-release | — |
| S004 | Ghidra commit 385e8cd GP-6528 add support for golang 1.26 (2026-03-03) — https://github.com/NationalSecurityAgency/ghidra/commit/385e8cd923d09f10b1a7874108e71748875fa174 | code | A | upstream fix for the r4-10 Go collapse: go1.26.0.json plus gate 1.15-1.26 on master; absent from every release through 12.1.4 | watch | 2026-10-19 | on-release | — |
| S005 | Ghidra BSim tutorial, Introduction (installed copy) — /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/docs/GhidraClass/BSim/BSimTutorial_Intro.md | docs | A | function similarity without names: decompiler feature vectors exclude constants, registers and types (:15-19); the H2 backend needs no server (:71-78) | queued | 2026-10-19 | on-release | — |
| S006 | ghidriff README — https://github.com/clearbluejar/ghidriff | code | A | headless Ghidra patch diffing from the CLI: SimpleDiff (symbol names) vs VersionTrackingDiff correlators with BSim correlation on by default; targets Ghidra 12.0.4 + pyghidra 3.x | queued | 2026-10-19 | on-release | — |
| S007 | GoReSym README (Mandiant) — https://github.com/mandiant/GoReSym | code | A | Go pclntab/moduledata recovery independent of Ghidra: layouts pre-1.2, 1.2, 1.16, 1.18, 1.20; -v version override for stripped binaries | watch | 2026-10-19 | on-release | — |
| S008 | rizin v0.9.0 release notes (2026-06-21) — https://github.com/rizinorg/rizin/releases/tag/v0.9.0 | docs | A | current rizin baseline for REA_RIZIN_COMMAND: project format 19 to 25, ESIL isolated and deprecated, RzIL uplift x86 SSE/SSE2 and SPARC, Swift demangling via rz-libswift; 0.9.1 patch 2026-06-29 | watch | 2026-10-19 | on-release | — |
| S009 | JADX 1.5.6 release notes (2026-07-10) — https://github.com/skylot/jadx/releases/tag/v1.5.6 | docs | A | current jadx (equals host /usr/bin/jadx 1.5.6): zip-entry path rejection, XML-bomb hardening, new call-graph module, Kotlin enum and ternary decompile fixes | watch | 2026-10-19 | on-release | — |
| S010 | remill README — https://github.com/lifting-bits/remill | code | A | instruction-accurate machine code to LLVM bitcode lifting library (AArch64, SPARC32/64, x86/amd64 incl. AVX-512; LLVM 15+), the lifter under McSema | queued | 2026-10-19 | 180d | — |
| S011 | SoK: Demystifying Binary Lifters Through the Lens of Downstream Applications (IEEE S&P 2022; abstract read via api.semanticscholar.org) — https://doi.org/10.1109/SP46214.2022.9833799 | paper | A | canonical lifter study (4 lifters, 252,063 executables): lifted IR suits diffing and decompilation but not pointer analysis; baseline that 2025-2026 work still cites | queued | 2026-10-19 | 365d | — |
| S012 | BRIDGE: Lifting Optimized Binaries to Canonical Compiler IR (ACL 2026) — https://aclanthology.org/2026.acl-long.527/ | paper | A | LLM retrieval plus feedback-verification lifting of x86-64/ARM64 to LLVM IR; over 30% higher re-executability than the strongest general LLM baseline | queued | 2026-10-19 | 180d | — |
| S013 | LLM4Decompile README — https://github.com/albertan017/LLM4Decompile | code | A | origin of the re-executability metric; End (asm to C) vs Ref (refine Ghidra pseudocode) models; 9B-v2 re-executability 64.9%; pointer to the Decompile-Bench pairs | queued | 2026-10-19 | 180d | — |
| S014 | DecompileBench (ACL Findings 2025) — https://aclanthology.org/2025.findings-acl.1194/ | paper | A | 23,400 real functions from 130 programs; 6 decompilers vs 6 LLM approaches; LLMs win understandability despite 52.2% lower functional correctness | queued | 2026-10-19 | 365d | — |
| S015 | When LLM Decompilers Recompile More and Preserve Less (arXiv 2609.05370, 2026-09-04) — https://arxiv.org/abs/2609.05370 | paper | A | fuzz-based divergence oracle: test-passing output still diverges (4.9%, up to 13%); LLM refinement of Ghidra raises builds 75 to 90% while Matched drops 74 to 62% | watch | 2026-10-19 | 180d | — |
| S016 | Evaluating Neural Decompilation of Dart AOT Binaries (arXiv 2607.06125, 2026-07-07) — https://arxiv.org/abs/2607.06125 | paper | A | metric-validity audit: CodeBLEU tracks pass@10 only weakly; 21.0-23.3% of compiling candidates pass; stripping names drops coverage from 42 to 7 of 154 | queued | 2026-10-19 | 180d | — |
| S017 | Reveree: Diagnosing LLM Reverse-Engineering Agents (arXiv 2609.01185, 2026-09-01) — https://arxiv.org/abs/2609.01185 | paper | A | scores RE-agent trajectories (8-stage schema, 9 models, 88 CTFs): failures concentrate in comprehension stages; extra budget rarely rescues them | watch | 2026-10-19 | 180d | — |
| S018 | SRE-Bench, a realistic contamination-free RE benchmark (arXiv 2608.11469, 2026-08-11) — https://arxiv.org/abs/2608.11469 | paper | A | 19 private programs, 44 anti-analysis mechanisms, 1,572 graded tasks; frontier agents fully solve 26.9-31.5%; contamination control and realistic scale both matter | watch | 2026-10-19 | 180d | — |
| S019 | When Binaries Talk Back: Representation-Confusion Attacks on LLM-Assisted RE (arXiv 2607.12507, 2026-07-14) — https://arxiv.org/abs/2607.12507 | paper | A | binary-derived text must not gain tool or evidence authority; grouping support by origin blocks 32/32 false claims that per-tool counting validated | watch | 2026-10-19 | 180d | — |
| S020 | Electron Fuses (docs) — https://www.electronjs.org/docs/latest/tutorial/fuses | docs | A | the nine current fuses with defaults, and the sentinel/wire byte format (0, 1, r) that REA inspect_electron_fuses decodes | watch | 2026-10-19 | on-release | — |
| S021 | Electron fuse schema v44.9.0 — https://github.com/electron/electron/blob/v44.9.0/build/fuses/fuses.json5 | code | A | authoritative wire order and stock defaults (_version 1, nine keys run_as_node through wasm_trap_handlers) to compare observed sentinels against | watch | 2026-10-19 | on-release | — |
| S022 | Electron ASAR Integrity (docs) — https://www.electronjs.org/docs/latest/tutorial/asar-integrity | docs | A | ASAR header integrity (SHA256 block hashes) and where it is enforced: macOS 16+, Windows 30+, never Linux; Info.plist and Integrity-resource carriers | queued | 2026-10-19 | on-release | — |
| S023 | OSV record CVE-2025-55305 (alias GHSA-vmqv-hx8q-j7mg) — https://api.osv.dev/v1/vulns/CVE-2025-55305 | dataset | A | advisory scope (only apps with both integrity fuses on), fixed versions, fix commits; its prose and extracted ranges disagree (36.8.0 vs 36.8.1) — cite the fix commits instead | queued | 2026-10-19 | 90d | — |
| S024 | Trail of Bits, Subverting code integrity checks to locally backdoor Signal, 1Password, Slack, and more (2025-09-03) — https://blog.trailofbits.com/2025/09/03/subverting-code-integrity-checks-to-locally-backdoor-signal-1password-slack-and-more/ | paper | B | the finder's write-up: V8 heap snapshots (v8_context_snapshot.bin) are code-bearing and sat outside ASAR integrity; mksnapshot gadget method | queued | 2026-10-19 | 365d | — |
| S025 | View8 README — https://github.com/suleram/View8 | code | A | .jsc decompiler over per-version patched V8 disassemblers (9.4, 10.2, 11.3 shipped); --normalize gives run-stable function names; serialized pickle input is unsafe | queued | 2026-10-19 | on-release | — |
| S026 | Check Point Research, Breaking the Seal: Static Deobfuscation of JSCeal's Compiled V8 Bytecode (2026-08-31) — https://research.checkpoint.com/2026/breaking-the-seal-static-deobfuscation-of-jsceals-compiled-v8-bytecode/ | paper | B | end-to-end static .jsc pipeline (version-matched disassembler, then View8, then deobfuscation passes) over 23 payloads; deterministic naming; public toolkit | queued | 2026-10-19 | 365d | — |
| S027 | ipsw guide, Parse dyld_shared_cache — https://blacktop.github.io/ipsw/docs/guides/dyld/ | docs | A | Mach-O/DSC route on Linux: ipsw dyld extract emits standalone Ghidra-loadable dylibs on any platform; DSC header, closures and ObjC dumps | queued | 2026-10-19 | on-release | — |
| S028 | LIEF, PE Support Enhancements: ARM64EC/ARM64X (2025-02-16) — https://lief.re/blog/2025-02-16-arm64ec-pe-support/ | docs | A | CHPE metadata and ARM64X dynamic-relocation parsing, a relocated nested ARM64EC view of ARM64X PEs, function seeding from exception tables | queued | 2026-10-19 | on-release | — |
| S029 | JSC Decompiler vs View8 vs ghidra_nodejs (vendor blog, 2026-03-11) — https://jscdecompiler.com/blog/jsc-decompiler-vs-view8-vs-ghidra | community | C | REJECTED: marketing for a hosted service that requires uploading the artifact (breaks custody); its claimed Electron 17-38 range excludes typora's Electron 42 / V8 14.8 (r4-07); no reproducible evaluation | rejected | 2026-10-19 | — | — |
| S030 | AI reverse-engineering tools compared: REA, IDA MCP, GhidraMCP and friends (dev.to, 2026-10-17) — https://dev.to/leemie8848/ai-reverse-engineering-tools-compared-rea-ida-mcp-ghidramcp-and-friends-oct-2026-3hfl | community | C | REJECTED: README restatements with unverifiable star counts (REA about 296k) and promotional links; useful only as a pointer to unopened leads | rejected | 2026-10-19 | — | — |

Self-check commands, against this file and the future `corpus/SOURCES.md`:
`grep -cE '^\| S[0-9]{3} ' local://kaika-w1-kaidoku-art.md` → 30;
tiers via `grep -E '^\| S[0-9]{3} ' <file> | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c` → 26 A, 2 B, 2 C.

### Leads (unopened)
- pyghidra-mcp (https://github.com/clearbluejar/pyghidra-mcp), GhidraMCP (LaurieWired), bethington/ghidra-mcp, HexRaysSA/ida-mcp — MCP peers of REA; only search snippets and S030 seen.
- CrackMeBench (arXiv 2605.10597); "LLM Agent-Assisted RE with Quantitative Readability Metrics" (arXiv 2606.06838).
- SK2Decompile (arXiv 2509.22114); ReF Decompile (arXiv 2502.12221); the Decompile-Bench dataset (HF `LLM4Binary/decompile-bench`).
- "Simplifying Lifter-Generated Emulation Style LLVM IR for Analysis Suitability" (ACM, doi 10.1145/3758316.3765484; HTTP 403); CuLifter (arXiv 2604.27486).
- rizin v0.8.0 notes (only a search snippet seen); `rz-libswift`.
- hasherezade/jsc_deobfuscator v1.0 (prebuilt Linux disassembler); PositiveTechnologies/ghidra_nodejs; jscd (re-check whether V8 14.8 tables have landed, r4-07 frontier); j4k0xb/View8 fork.
- Electron advisory GHSA-vmqv-hx8q-j7mg page and fix commits (23a0293…, 2e5a0b7…, 3f92511…, fdf29ce…); MITRE ATT&CK T1218.015.
- GoReSym releases (check Go 1.26 support); Ghidra 12.2 release when it ships (GP-6528).
- onekey-sec/sasquatch releases (lane frontier); blutter (Dart AOT); apple-oss-distributions/dyld (chained fixups).

### Paths
- Go ≥1.26 symbol recovery — S003 → S004 → S007 → S005 → S006: the installed mechanism, then the upstream fix, then an independent parser that needs no Ghidra upgrade, then name-free BSim pairing, then automated diffing on top of it.
- LLM-assisted decompilation as evidence — S013 → S014 → S015 → S016 → S019 → S017 → S018: the metric's origin, its gap with understandability, test-passing divergence, name leakage, provenance-gated authority, then the agent-level evaluation that builds on all of them.
- Electron beyond app.asar — S020 → S021 → S022 → S023 → S024 → S025 → S026: fuse semantics, then the wire schema, then the integrity platform scope, then the snapshot bypass, then the advisory scope, then `.jsc` decompilation tooling and a 2026 field pipeline.

---

## 4. Candidate knowledge entries (6)

### K1 `2026-10-19-ghidra-1214-go126-bootstrap-gap`
- **Claim (falsifiable).** The installed Ghidra 12.1.4 gates Go at `1.15-1.25` (GoRttiMapper.java:79). It holds 11 bootstrap snapshots, go1.15.0 through go1.25.0. It has no 1.25.x/1.26.x patch diffs: `ls …/typeinfo/golang/patchverdiffs | grep -cE '^go1\.2[56]\.'` → 0.
- **Failure path, from source.**
  - The analyzer only logs "Untested Go version" (:170-171).
  - `GoApiSnapshot.get` returns `EMPTY` when `go1.26.0.json` is absent (GoApiSnapshot.java:105-115, 122-126).
  - Struct mapping then fails and raises `BootstrapInfoException` (`initStructMappings` :351, catch :355-360). `getSharedGoBinary` catches it and returns null (:114-125), so Go naming is disabled for the program.
- **Upstream state.** Go 1.26 support exists only on master (GP-6528, commit 385e8cd, 2026-03-03). It is in no release through 12.1.4.
- **Inference to admit, labeled as inference.** r4-10's go1.26.8 collapse (11,588 / 11,595 `FUN_*`) is this missing-snapshot gate. It is **not** evidence that Go 1.26 changed the moduledata/pclntab layout.
- **Source and quotes.** S003, GoRttiMapper.java:79: `SUPPORTED_VERSIONS = GoVerRange.parse("1.15-1.25");`, and :359: "Missing Go bootstrap type info, unable to extract Go RTTI info." S004 commit message: "GP-6528 add support for golang 1.26".
- **Fills.** Coverage row "Cross-version diff" / `knowledge/2026-10-13-r4-10-real-version-pair`. Replaces the uncited, transient log line at r4-10:70-73 with a cited mechanism. Also proposes a Frontier bullet: Go ≥1.26 recovery waits on a Ghidra release with GP-6528 (operator-owned upgrade); route-arounds are S007, S005 and S006.
- **Recheck.**
  - `unzip -p "$GHIDRA_INSTALL_DIR/Ghidra/Features/Base/lib/Base-src.zip" ghidra/app/util/bin/format/golang/rtti/GoRttiMapper.java | grep -n 'SUPPORTED_VERSIONS = '` → `79: …"1.15-1.25"`
  - `ls "$GHIDRA_INSTALL_DIR"/Ghidra/Features/Base/data/typeinfo/golang/*.json | wc -l` → 11
  - `grep -c GP-6528 "$GHIDRA_INSTALL_DIR/docs/ChangeHistory.md"` → 0
  - `curl -fsSL https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/Base/src/main/java/ghidra/app/util/bin/format/golang/rtti/GoRttiMapper.java | grep -n 'SUPPORTED_VERSIONS = '` → `79: …"1.15-1.26"`
  - **Confirming probe for wave 2:** re-run r4-10 row 2 on `op-2.40.0` (sha256 `8d029d2c…` per r4-10:19) with the Ghidra log retained. Expect `grep -c 'Missing Go bootstrap type info'` ≥ 1, and 0 on `op-2.34.1`.
- **QUALITY.md.**
  - #1, #2: local paths, a commit hash, and counts.
  - #4: install path, Base-src.zip sha256 `f00d29c2…a8d804`, and target identity carried from r4-10.
  - #5: observation = source text and directory listing; inference = the causal link to r4-10; unknown = whether names would come back with only the json added.
  - #7: no live Ghidra run this wave; `GolangSymbolAnalyzer` fallbacks not read.
  - #8: pins 12.1.4 (build 2026-09-21); claim source is the installed source zip, not the docs.
- **Correction form.** This is an append-only erratum to r4-10:70-71: "cannot parse the Go 1.26 moduledata/pclntab layout" names the wrong mechanism.

### K2 `2026-10-19-electron-v8-snapshot-outside-asar-surface`
- **Claim.** The code-bearing surface of the host Signal (`signal-desktop 8.26.0-1`, `pacman -Q signal-desktop`) extends beyond `app.asar`. It ships two V8 snapshot files:
  - `/usr/lib/signal-desktop/v8_context_snapshot.bin` (740,048 B, sha256 `fbe7992da8fe4f7791dac415a417c2a3a35aba1050df3ee36ad1cbe208b63dfe`)
  - `snapshot_blob.bin` (365,488 B, sha256 `8823f193e991b540e7f2eb7710bdb30e8d997b5368421ecfb94e40cc9705aac3`)

  V8 heap snapshots can carry clobbered builtins (S024) and were outside Electron's integrity fuses before the CVE-2025-55305 fixes (S023). The corpus mentions `v8_context_snapshot` in 0 files. Under QUALITY #11, every held Electron finding is therefore ASAR-scoped and *excludes* snapshot content; that is an exclusion, not an "empty" result.
- **Falsifiable probes.**
  - (a) Does REA `inspect-artifact` on `/usr/lib/signal-desktop` inventory the `.bin` snapshots as graph nodes, yes or no?
  - (b) Identity, not safety: does the snapshot sha256 equal the stock file in the matching Electron release? The binary carries the string `Electron/43.5.0`, so the version attribution is itself inference.
- **Source and quotes.**
  - S024, section "From frozen pizza to unsigned code execution": "it did not consider heap snapshots as “executable” application content, and thus it did not perform integrity checking on the snapshots".
  - S023 details: "This only impacts apps that have the embeddedAsarIntegrityValidation and onlyLoadAppFromAsar fuses enabled."
- **Fills.** Coverage row "Electron/ASAR/JS" and `knowledge/2026-10-16-l7-03-inspect-electron-fuses`. New Frontier bullet: non-ASAR code-bearing Electron artifacts.
- **Recheck.**
  - `ls -l /usr/lib/signal-desktop/*.bin; sha256sum /usr/lib/signal-desktop/v8_context_snapshot.bin`
  - `grep -rli 'v8_context_snapshot' corpus | wc -l` → 0
  - `grep -aoE 'Electron/[0-9]+\.[0-9]+\.[0-9]+' /usr/lib/signal-desktop/signal-desktop | sort -u` → `Electron/43.5.0`
- **QUALITY.md.**
  - #4: path, sha256 and package version.
  - #5: observation = files, sizes, hashes, version string; inference = code-bearing per S024; unknown = stock vs custom snapshot, and REA inventory coverage.
  - #9: no runtime claim.
  - #11: the exclusion is stated explicitly.
  - Adjacent guard: the entry must **not** state exploitability or safety (`PROVINCE.md:114-116`).

### K3 `2026-10-19-llm-refined-pseudocode-erases-visible-unknowns`
- **Claim.** LLM refinement of Ghidra pseudocode trades visible unknowns for invented structure. On 300 GitHub library functions plus 287 CVE-grounded ones:
  - the build rate rises from 75% to 90%
  - Matched (behavioral agreement) falls from 74% to 62%
  - up to a tenth of CVE functions show Crash Absence
  - 4.9% of outputs that pass every test still diverge, up to 13% for one system (S015)

  DecompileBench shows the same direction (S014).
- **Lane rule proposed.** LLM-refined or LLM-renamed pseudocode is second-order inference and is never cited for behavior. Raw provider pseudocode, with its visible unknowns (`undefined*`, `FUN_*`, `DAT_*`, `unaff_*`, `in_*`), stays the cited artifact.
- **What would refute it.** A replication in which refinement raises Matched without hiding unknowns.
- **Source and quote.** S015 abstract: "Source-level analysis traces this divergence to introduced fields, types, callees, and guards that replace the visible unknowns traditional tools leave behind."
- **Fills.** New coverage row "LLM-assisted decompilation (methodology)". Sharpens QUALITY #5 and adds a candidate weak-material signal: "LLM-refined pseudocode cited as behavior".
- **Recheck.**
  - `curl -s 'http://export.arxiv.org/api/query?id_list=2609.05370' | grep -c '75% to 90%'` → 1
  - Host baseline for wave 2: re-run the r1 jq `decompile 0x103fa0` carrier and count placeholder tokens with `grep -oE '\b(undefined[0-9]*|FUN_[0-9a-f]+|DAT_[0-9a-f]+|unaff_[A-Za-z0-9_]+|in_[A-Za-z0-9_]+)\b' | wc -l` (QUALITY #13 form).
- **QUALITY.md.**
  - #1–#3: domain-specific (decompiler evidence authority).
  - #4: the artifact is arXiv 2609.05370, plus the pinned `/usr/bin/jq` for the host bridge.
  - #5: labels kept.
  - #7: abstract only; no replication.

### K4 `2026-10-19-multi-tool-corroboration-counts-origins`
- **Claim.** When several tools read the same attacker-controlled bytes, their agreement is one origin, not independent support. RARE fused Ghidra, r2pipe and angr drafts over 16 programs (S019):
  - a per-record Support Gate validated 32/32 planted false claims
  - grouping by origin (Provenance Gate) validated 0/32 and kept 32/32 supported claims
  - under Data-Only rendering, models still proposed 15 unsafe actions; tool authorization denied all of them
- **Lane exposure.** The lane cross-checks REA with host readers in 16 knowledge files (`grep -rliE 'triangulat|cross-check' corpus/knowledge | wc -l`). That agreement corroborates *parsing* (offsets, bytes), but it is one origin for *content meaning* (strings, names, decompiled semantics). The REA marker `untrusted_content` appears in 0 corpus/SKILL files.
- **Proposed criterion #16.** "Corroboration counts distinct origins, not tools; same-file readers are one origin for content claims."
- **Source and quote.** S019 abstract: "views from several tools do not necessarily provide independent evidence".
- **Fills.** Coverage row "Evidence model", QUALITY, and SKILL "Working contract".
- **Recheck.** The S019 abstract numbers; `grep -rliE 'triangulat|cross-check' corpus/knowledge | wc -l` → 16; `grep -rliE 'untrusted_content|untrusted content' corpus SKILL.md | wc -l` → 0.
- **QUALITY.md.** #1–#3 and #5. #6 is n/a (not REA-derived). #7: abstract only; RARE-Bench not run.

### K5 `2026-10-19-rea-rizin-provider-declared-unheld`
- **Claim.** REA 6.5.0 and 6.7.0 (npx caches `ad9a3fdb…`, `a1722018…`) declare rizin and Cutter verbs: `execute_rizin_command` appears in 12 dist files, `start_rizin_debug_session` in 10, `cutter_command` in 11 / 12. The 6.7.0 provider resolves `REA_RIZIN_COMMAND ?? "rizin"` and launches `rizin -N -0 -d …` (RizinDebugSessionManager.js:109, 183-185). Rizin is absent on this host, and 0 corpus files exercise these verbs. Upstream rizin is v0.9.1 (S008). Status: **declared, not held** (QUALITY #10); installing it is operator-owned.
- **Source and quote.** S008: "the on-disk project format version was bumped from 19 to 25 during this cycle". This matters for any persisted rizin/Cutter projects.
- **Fills.** Coverage row "Provider/capability matrix"; new Frontier bullet for the rizin provider.
- **Recheck.**
  - `command -v rizin || echo absent`
  - `grep -n 'REA_RIZIN_COMMAND' ~/.npm/_npx/a1722018f28f9df2/node_modules/rea-agents/dist/rizin/RizinDebugSessionManager.js` → `109:`
  - `grep -rliE 'execute.rizin.command|rizin.debug.session|cutter.command' corpus | wc -l` → 0
- **QUALITY.md.** #8: pins rea-agents 6.5.0/6.7.0; the claim source is dist text, not the live `tools/list`. #10: declared only. #7: `binary_session` availability not run.

### K6 `2026-10-19-arm64x-pe-route-lief-vs-ghidra-1214` (frontier-row update until a carrier exists)
- **Claim.**
  - Ghidra 12.1.4's ChangeHistory has 0 ARM64EC/ARM64X/CHPE entries (`grep -ciE 'arm64ec|arm64x|chpe' "$GHIDRA_INSTALL_DIR/docs/ChangeHistory.md"` → 0).
  - LIEF's maintainer reports that Ghidra 11.4.2 cannot "accurately process Windows ARM64EC binaries" (LIEF 0.17.0 post).
  - LIEF exposes CHPE metadata and a nested ARM64EC view of an ARM64X PE (S028).
- **Falsifiable probe (needs a carrier).** On a legitimately obtained ARM64X DLL, compare REA/Ghidra function recovery with LIEF's ARM64 and x64 exception tables.
- **Source and quote.** S028: "LIEF can now offer a relocated view of the ARM64EC binary that is embedded within an ARM64X binary."
- **Fills.** `corpus/README.md:179` ("PE reserve: ARM64X hybrids") and PROVINCE Frontier "PE subtypes".
- **QUALITY.md.** #1, #2 and #8 clear now. #4 and #10 need an ARM64X carrier, so admit it as frontier-row text only until a probe runs.

---

## 5. Paths
See `### Paths` in §3. Three sequences: Go ≥1.26 recovery; LLM-assisted decompilation as evidence; Electron beyond app.asar.

---

## 6. Rejected candidates (with reasons)
1. **S029** jscdecompiler.com (tier C). Vendor marketing for a hosted service that requires uploading the artifact, which breaks local custody. Its claimed range of Electron 17–38 excludes typora's Electron 42 / V8 14.8 (r4-07). There is no reproducible evaluation.
2. **S030** dev.to "AI RE tools compared" (tier C). README restatements, an implausible "about 296k stars" for REA, and promotional `reaguide.com` links. Kept only as a pointer to leads.
3. **Entry "CVE-2025-55305 applicability to host Signal / 1Password".** Rejected because it is a safety verdict, which is Adjacent ground (`PROVINCE.md:114-116`). The `Electron/43.5.0` string arithmetic is not evidence that a patch is present. Only the coverage and identity framing (K2) is admissible.
4. **arXiv 2605.30667**, "Automatically Attacking SRE AI Agents" (opened, not rowed). An AutoDAN-style proof of concept without measured defenses. S019 covers the same failure with provenance-gate measurements that map onto the lane's evidence rules.
5. **arXiv 2609.07201**, "Recompilation Is Not Enough" (opened, not rowed). Preliminary (104 Coreutils binaries), and the lane never recompiles decompiled C. S015 carries the evidence-authority lesson.
6. **Lane action "drop master's go1.26.0.json into the installed Ghidra".** Rejected as a lane move: modifying the install is operator-owned (`PROVINCE.md:108-113`). It is recorded for the operator as a cheap experiment; the gate at :170-171 only logs.
7. **web_search AI summaries as support.** Never used. Two were wrong on checking:
   - one summary placed View8 support "up to V8 13.6", but the README lists only 9.4 / 10.2 / 11.3
   - one presented Cutter 2.4 / rizin 0.8 as current, while the release API shows Cutter 2.5.0 / rizin 0.9.1

---

## Mistakes mined and defects found
- **Mistake classes found by checking the lane against external art (3), plus 1 preventive:**
  - M1: r4-10 states a causal mechanism ("layout") as fact without a citation (QUALITY #5) → K1.
  - M2: ASAR-only scope says nothing about snapshot content (QUALITY #11 class) → K2.
  - M3: same-origin cross-checks are counted as corroboration in 16 files → K4.
  - Preventive: LLM-refined pseudocode as evidence → K3 (0 lane instances today).
- **Defects (4):**
  - D1, contract: the SOURCES.md example row `|S001|…` (no spaces) does not match the counting command `grep -cE '^\| S[0-9]{3} '`, which needs `| S001 |`. Example-form rows count 0. This dossier uses the spaced form.
  - D2, lane: the r4-10:70-71 mechanism wording (K1 erratum).
  - D3, external: the OSV CVE-2025-55305 prose ("fixed 36.8.1", "through 37.3.1") contradicts its extracted events ("fixed 36.8.0"). Cite the fix commits.
  - D4, STATE (non-exhaustive inventory, not a wrong one): a fourth npx cache `9b9809298fe40d2c` (6.7.0, unpinned spec, payload byte-identical to `a1722018…` per W1StateKaidoku D14) is unlisted in PROVINCE.
