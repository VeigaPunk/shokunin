# DRAFT — kaidoku-shokunin PROVINCE.md (round-1 curation, for integrator)

Drafted from live host probes on 2026-10-13; every Core row carries the named
command that re-checks it. Source docs: `kaidoku-shokunin/MINT.md`,
`kaidoku-shokunin/SKILL.md`, shipped REA skill
`~/.agents/skills/reverse-engineer-anything/SKILL.md` (v37, 170 tools) +
`references/native-and-artifacts.md`, `references/evidence-workflows.md`.

**Domain:** reverse engineering of shipped artifacts with REA on this Linux
host — native ELF through the Ghidra 12.1.4 provider, Electron/ASAR/JavaScript
bundles, archives and packages; evidence-first static analysis that keeps
observation, inference and unknowns separate. Surface summary: the `rea` MCP
server (stdio, `npx -y rea-agents@6.4.0 mcp`, 170 MCP tools + 127 CLI commands,
catalog tools_sha256 `25802f6d…`) plus its `rea` CLI; the Ghidra provider at
`/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`; host binutils as non-REA
fallback readers. Drift-prone values: `GHIDRA_INSTALL_DIR` and `JAVA_HOME` in
`~/.config/devin/mcp_config.json` and `~/.omp/agent/mcp.json`; the pinned
`rea-agents@6.4.0` version; the installed REA skill version (v37, `rea doctor`
reports `skill: stale`, expected by package vs installed); Ghidra's own
`application.version`; unset provider env keys (`REA_IDA_MCP_CONFIG`,
`REA_PWNTOOLS_PYTHON`, `HOPPER_LAUNCHER_PATH`). Probe/reconciliation
conventions: `rea doctor` is the environment verdict; `binary_session {}` is
the live-server verdict (`result.tool_availability` + provider candidates);
a catalog-listed tool is *available*, not *held* — ground moves to Core only
after an end-to-end probe lands a `LOG.md` entry citing its `evidence_id` and
subject sha256. The domain is a frontier, not a fence: it grows by evidence
(LEARNING.md).

## Core

Surfaces owned now — each verified on this host 2026-10-13.

| Surface | Ports / paths / config keys | Liveness / readiness probe (named command) | Verified evidence |
|---|---|---|---|
| REA MCP server (live) | `~/.config/devin/mcp_config.json` `mcpServers.rea`; `~/.omp/agent/mcp.json` `mcpServers.rea`; both spawn `npx -y rea-agents@6.4.0 mcp` with env `GHIDRA_INSTALL_DIR`, `JAVA_HOME` | MCP call `binary_session {}` in an attached client → `analysis_provider_candidates` + `capabilities[]`; CLI: `npx -y rea-agents@6.4.0 doctor` (registrations: devin `aligned`, omp `aligned`) | This session: `binary_session` returned live catalog; doctor registrations devin/omp `state: aligned` |
| `rea` CLI | npm bin `rea`/`rea-agents` (npx cache `~/.npm/_npx/*/node_modules/rea-agents@6.4.0`); 127 commands incl. `doctor`, `analyze-javascript-application`, `open-binary`-family, `inspect-evidence-bundle` | `npx -y rea-agents@6.4.0 --version` → `6.4.0`; `npx -y rea-agents@6.4.0 doctor` | doctor run 2026-10-13: node 24.21.0 ok, host ok |
| Ghidra provider | `GHIDRA_INSTALL_DIR=/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`; headless `support/analyzeHeadless`; decompiler `Ghidra/Features/Decompiler/os/linux_x86_64/decompile` (elf x86_64, matches linux/x64) | `npx -y rea-agents@6.4.0 doctor` → providerInspections `id: ghidra, configured: true, available: true`, 8/8 checks | doctor: `application.version=12.1.4`, headless path ok, native_decompiler ok |
| JDK 21 substrate | `JAVA_HOME=/usr/lib/jvm/java-21-openjdk` | `/usr/lib/jvm/java-21-openjdk/bin/java -version` → `openjdk 21.0.12.1` (doctor check `ghidra-java`: accepted 64-bit full JDK 21+) | verified 2026-10-13 |
| Native ELF analysis via Ghidra | `open_binary {path}` → focused tools `analyze_function`, `procedure_pseudo_code`, `search_strings`, `xrefs`, `binary_overview`, `read_bytes`, `address_to_file_offset`, `inspect_native_load_image`; ephemeral-session import, original bytes untouched | `open_binary` on an ELF → `binary_overview` returns segments/procedures/strings | `open_binary /usr/bin/true` → elf x86_64 sha256 `8bc9a73a…`; `binary_overview` → 31 segments, 206 procedures, 154 strings, evidence `ev_982c6020636b96c8a515f43081fd749cec7c15f448023d9b4b18b7e5780171a8` |
| Electron/ASAR/JavaScript static analysis | `analyze_javascript_application {input_path}` on `.asar` or extracted JS tree; graph paging `inspect_analysis_view`, `trace_application_feature`, `recover_javascript_sources`, `compare_application_versions`; on-host targets: `/usr/lib/obsidian/{app,obsidian}.asar`, `/usr/lib/signal-desktop/resources/app.asar`, `/opt/1Password/resources/app.asar`, `/usr/share/typora/resources/{app,lib,node_modules}.asar`, `/usr/lib/electron{39,43}/resources/default_app.asar` | `analyze_javascript_application` `detail:"summary"` on a small asar → statistics + coverage + limitations | `/usr/lib/electron43/resources/default_app.asar` (sha256 `06d4a28b…`) → 5 files, 3 parsed JS, 41 findings, IPC ops 2, evidence `ev_2628de89b0f446fc6d4a1a42a89129621b49d19ff50a5322cde7635edd85269a` |
| Archive/package member inventory | `inspect_artifact` / `extract_artifact` (ZIP/APK/IPA/MSIX/AppX/DMG/directory; ASAR nested auto-expansion, no bulk extract); on-host target `~/Applications/Grok_Bot_0.68.1.AppImage` | `binary_session {}` `capabilities[]` → both `available: true` (live, 2026-10-13) | availability row in live `binary_session` output |
| Evidence discipline (observation / inference / unknown separation) | `detail:"summary"` + `parent_evidence_id` paging via `inspect_analysis_view`; `get_evidence_bundle` filters; `export_evidence_bundle` / CLI `rea inspect-evidence-bundle` for portable records | every Core probe emits `evidence_id` + `limitations[]`/`unknowns[]` — a claim without them is not evidence | demonstrated in both live probes above (41 findings with 451 declared semantic unknowns) |
| Host fallback readers (non-REA) | `/usr/bin/file`, `readelf`, `objdump`, `nm`, `strings`, `unzip`, `tar`, `gdb`, `jq`, `python3`, node/npx (fnm v24.21.0) | `command -v <tool>` | verified 2026-10-13; absent: `7z`, `cabextract`, `xxd`, `radare2`/`rizin`, `strace`, `ltrace`, `upx` |

Cross-lane registry this lane maintains: the REA surface map — per-client
registration state (doctor `registrations[]`), provider availability
(ghidra/ida/hopper), provider env keys, and the on-host artifact inventory
(asar/ELF/archive/firmware/core paths) — kept in `corpus/knowledge/`, refreshed
by `rea doctor` each round.

## Frontier

Claimed in MINT.md, not yet held. Each moves to Core by a `LOG.md` entry citing
the corpus entries that earned it.

- **PE binaries under this Linux host** — Ghidra loads PE cross-platform, but no
  PE `open_binary` has run end-to-end here; `inspect_pe_resources` (target-free,
  portable) is catalog-listed but unprobed. First move: `open_binary` + overview
  on a real PE, then `inspect_pe_resources` diffed against it.
- **Managed PE/CLI assemblies** — `inspect_managed_artifact`,
  `inspect_managed_members`, `inspect_managed_native_boundaries`,
  `compare_managed_members`, `project_managed_application_graph` all report
  `available: true` (execution-free canonical parser), and on-host targets exist
  (`/usr/share/dotnet/shared/Microsoft.NETCore.App/9.0.19/*.dll`); however the
  first live probe (`inspect_managed_artifact` on `Microsoft.CSharp.dll`)
  returned `target_unavailable: unsupported PE architecture` — the AnyCPU
  assembly class is rejected. Decompiled-C# reconstruction additionally needs a
  caller-supplied decompiler (`import_managed_reconstruction` ingests external
  output); `ilspycmd` absent, and `dotnet` is runtime-only (`dotnet tool list`
  fails: no .NET SDK). Held only when a supported-arch assembly is analyzed end
  to end and the boundary is documented.
- **Firmware images** — `inspect_firmware_regions` (signature candidates, no
  extraction) is catalog-listed; real targets at
  `/usr/lib/firmware/nvidia/610.57.04/*.bin` (GSP blobs) and zst-packed entries.
  `extract_firmware` needs caller-supplied Binwalk/Unblob — both absent
  (`command -v binwalk unblob` → MISSING). Region-signature probing is
  unblocked; extraction is operator-prerequisite-gated.
- **Recorded crashes** — `inspect_recorded_crash` catalog-listed; real x86-64
  ELF cores exist via `coredumpctl list` (chromium SIGTRAP cores,
  `/var/lib/systemd/coredump/*.zst`). Optional `include_debugger_context` facet
  needs caller-supplied GDB/pwndbg (gdb present, pwndbg absent). Unprobed.
- **Offline ELF layout (`inspect_binary_layout`)** — probed 2026-10-13 on
  `/usr/bin/file`: fails `provider_unavailable`, provider `pwntools-elf` needs
  `REA_PWNTOOLS_PYTHON` = Python with pwntools 4.15.0 + pyelftools 0.33 +
  Unicorn 2.1.2; REA never installs Python packages. Blocked on an
  operator-owned prerequisite, documented.
- **Alternate providers** — IDA (`REA_IDA_MCP_CONFIG` unset,
  `not_configured`), Hopper (`/opt/hopper/bin/Hopper` missing,
  `executable_missing`), JEB client (unprobed). All engine installs are
  operator-owned.
- **Android APK analysis** — `inspect_android_package`, class/method decode,
  `trace_android_references`, adb family are catalog-listed; `apktool`/`jadx`/adb
  presence and an APK corpus unprobed (archive member inventory of an APK is
  already Core via `inspect_artifact`; decoded-manifest/code route is not).
- **Runtime observation** — `list_browser_targets`, `list_electron_targets`,
  `list_javascript_runtime_targets`, `observe_javascript_runtime`,
  `capture_*_scenario`, `inspect_web_network_capture` (HAR/mitmproxy):
  catalog-listed, require user-owned already-open targets or caller-supplied
  captures; none probed.
- **Cross-version diffing** — `compare_application_versions`,
  `compare_bundles`/`compare`, `compare_javascript_export_shapes`,
  `compare_source_to_bundle`: catalog-listed; needs a two-version artifact pair.
- **macOS-only surfaces** — `inspect_macho`, `inspect_plist`,
  `observe_native_calls` (LLDB), `demangle_swift`, `inspect_signature`,
  `list_architectures`, `inspect_asset_catalog`,
  `inspect_native_dispatch_metadata`, `capture/observe_native_ui_*`: live
  `binary_session` reports `unsupported_host` on this Linux host — held closed
  until a macOS host exists; recorded so the lane never claims them.
- **EVM bytecode** — `inspect_evm_interface` catalog-listed; no carrier probed.

## Adjacent

Ground the lane refuses or defers — reported to the orchestrator, never
absorbed (this fleet has no domain sibling besides main-repo `protocol` and
`aggregator`, which own no domain surface; a sibling lane id replaces
`(unowned)` if one is minted).

- **Malware triage at scale** — verdict pipelines, sandbox detonation, bulk
  classification of hostile samples `(unowned — report to orchestrator)`. The
  lane analyzes declared, caller-supplied artifacts; it does not run a triage
  queue or label samples malicious/benign.
- **Non-REA dynamic analysis** — live debugging/instrumentation outside REA's
  declared runtime tools (gdb scripting, strace/ltrace tracing, unpacking by
  execution, Frida-style hooking) `(unowned)`. REA's own boundary: static
  evidence plus *declared* runtime targets only; `observe_native_calls` is
  LLDB/Mach-O and `unsupported_host` here anyway. `gdb` stays a fallback reader
  for supplied cores, not a lane-run tracer.
- **Source-available reconstruction of ordinary repositories** — reading a
  complete source tree is REA's documented anti-trigger ("Skip REA for ordinary
  source-repository architecture analysis") `(unowned; meta/repo-understanding
  rides the two main-repo lanes' scope)`.
- **Installing engines, Python packages, or editing client configs** —
  `rea setup` runs, registration refreshes for `claude_code`/`codex`/
  `grok_build`/`opencode`/`pi` (all `missing` per doctor), installing
  Hopper/IDA/JADX/Binwalk/Unblob/pwntools/ilspycmd/.NET SDK — all
  **operator-owned** (MINT.md adjacent clause; the REA skill itself forbids
  installing unrelated software). The lane documents the gap and the exact
  env key; it never runs the installer.
- **Quality/安全 verdicts on findings** — the lane answers "what does this
  shipped artifact do, per evidence id X" — never "is it safe, trustworthy, or
  licensed for reuse" `(unowned)`.

## Summary

Core holds today: REA MCP+CLI on both clients (registrations `aligned`), Ghidra 12.1.4 + JDK 21 provider green, ELF end-to-end (`/usr/bin/true` → ev_982c6020…), ASAR end-to-end (`default_app.asar` → ev_2628de89…), archive inventory, evidence-discipline paging, host binutils; Frontier holds claimed-but-unprobed PE, managed (probe rejected `unsupported PE architecture`), firmware, recorded crashes, pwntools ELF layout (provider absent), alternate providers, APK/runtime/diff surfaces; Adjacent refuses scale malware triage, non-REA dynamic work, source-repo reconstruction, and all operator-owned installs.
