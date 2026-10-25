# kaidoku-shokunin — round-1 quality-bar DRAFT

Draft for the integrator; not yet merged into `corpus/QUALITY.md` or
`corpus/README.md`. Bases cited: `corpus/QUALITY.md` rows 1-3, CORPUS.md
evidence rules (count-carries-command, negative-claim-carries-sweep,
quote-names-location), MINT.md domain claim, and the installed REA skill
`~/.agents/skills/reverse-engineer-anything/SKILL.md` (v37, tool_count 170,
rea-agents@6.4.0) — read 2026-10-13 on this host.

## Admission criterion 4 — Target identity is pinned

| field | value |
|---|---|
| proposed row | `4 | Names the artifact under analysis by absolute path plus a stable identity (SHA-256, or package name + version + arch triple when hashing is impractical); "the app" alone is inadmissible | REA binds GUI input by SHA-256 and refuses to select an example target on the user's behalf (`SKILL.md`: "Paths in unrelated saved reports and nearby test fixtures do not select the user's target"); CORPUS.md falsifiability | —` |
| basis | REA skill target-resolution rules; MINT.md "target routing" core |

## Admission criterion 5 — Observation / inference / unknown are labeled

| field | value |
|---|---|
| proposed row | `5 | Every conclusion is labeled observation, inference, or unknown; decompiler/pseudocode output and layout-derived claims are inference, never "observed behavior" | REA SKILL.md: "Every conclusion must distinguish observations, inferences, and unknowns… never imply that static analysis observed execution"; the lane's own charter sentence in QUALITY.md header | —` |
| basis | Core domain discipline; stated verbatim in the lane's minted scope |

## Admission criterion 6 — REA citations are resolvable

| field | value |
|---|---|
| proposed row | `6 | A claim drawn from REA cites its Evidence ID / retained parent_evidence_id, or the exact reproducing call (tool name, target SHA-256, detail level, filters per get_evidence_bundle: operation, analysis-profile digest, procedure address) | REA evidence-paging model (inspect_analysis_view, export_evidence_bundle, "retention: complete-record"); generalizes CORPUS.md "a count carries its command" to tool-output evidence | —` |
| basis | `references/evidence-workflows.md`; CORPUS.md count rule |

## Admission criterion 7 — Coverage boundary is stated

| field | value |
|---|---|
| proposed row | `7 | The entry names what was NOT examined: detail level used (summary vs complete), truncated/paged views, unvisited modules or functions, providers absent on this host (IDA, Hopper) | REA SKILL.md: "preserve limitations and incomplete coverage"; bounded negative searches; "value-flow truncation and unknown metadata remain separate" | —` |
| basis | REA staged-workflow step 7 (finding ledger with "search boundary, and remaining unknowns") |

## Admission criterion 8 — Tool and provider versions are pinned

| field | value |
|---|---|
| proposed row | `8 | Capability claims name the server release (rea-agents@6.4.0), provider (Ghidra 12.1.4 at /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC, JDK 21), and the source of the claim (live tool list / binary_session result.tool_availability vs installed skill text) | SKILL.md warns a main-branch skill "may describe capabilities absent from an older npm release"; availability "depends on the operation, target, and host" | —` |
| basis | REA connection model; MINT.md provider path claim |

## Admission criterion 9 — Static and runtime evidence are typed apart

| field | value |
|---|---|
| proposed row | `9 | Runtime-behavior claims are admitted only with runtime-evidence provenance (browser/Electron target, process capture, recorded crash/HAR); recorded captures carry capture-time scope and no live-attribution claim | REA workflow step 5: runtime observation only when static evidence cannot answer; inspect_web_network_capture operates "without fetching recorded URLs or claiming live attribution" | —` |
| basis | `references/runtime-observation.md`; HAR/capture rules in SKILL.md |

## Weak signal 1 — Inference wearing observation's clothes

| field | value |
|---|---|
| proposed row | `1 | Pseudocode, string tables, filenames, or section layout narrated as what the program "does" — behavior asserted with no Evidence ID behind it | SKILL.md: "do not infer behavior from filenames, strings, or layout alone"; observation/inference split |` |
| basis | The canonical RE hallucination; directly named in the task and REA docs |

## Weak signal 2 — Unbounded completeness

| field | value |
|---|---|
| proposed row | `2 | "no X in the binary", "all functions/strings enumerated", "fully analyzed" without the search command, filters, or detail level; a truncated MCP preview or client-truncated frame treated as the complete record | SKILL.md: treat a client-truncated preview "as incomplete… do not parse the preview as canonical JSON"; CORPUS.md negative-claim rule |` |
| basis | CORPUS.md sweep rule + REA transport truncation guidance |

## Weak signal 3 — Floating target

| field | value |
|---|---|
| proposed row | `3 | Findings attach to "the app"/"the binary" with no path+hash/version, or cite a saved report/test fixture as if it were the analyzed artifact | SKILL.md target-selection paragraph: fixtures and old reports "do not select the user's target" |` |
| basis | Same lesson as criterion 4, seen from the reject side |

## Weak signal 4 — Version-free capability claims

| field | value |
|---|---|
| proposed row | `4 | "REA supports/refuses X" asserted from docs or memory without consulting the connected server's actual tool list or binary_session tool_availability on this host | SKILL.md: "Use the connected server's actual tool list and input schemas"; IDA/Hopper absent here (MINT.md frontier) |` |
| basis | Release-vs-docs skew is endemic (skill v37 vs npm 6.4.0) |

## Weak signal 5 — Static graph parading as runtime

| field | value |
|---|---|
| proposed row | `5 | Dynamic claims ("when the user logs in the app sends…", "at runtime it loads…") sourced from a static call graph or recorded capture presented as live observation | SKILL.md: "never imply that static analysis observed execution"; captures forbid live attribution |` |
| basis | Criterion 9's failure mode; the domain's highest-severity mislabel |

## Coverage section — REA service and connection

Rows to hold: MCP registration state (`~/.config/devin/mcp_config.json`, OMP),
`rea doctor` readiness output, CLI fallback (`npx -y rea-agents@6.4.0`), live
tool list vs installed-skill drift, `binary_session` /
`result.tool_availability` readings, recovery-guide blockers observed on this
host.

## Coverage section — Provider readiness on this host

Rows to hold: Ghidra 12.1.4 (`/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`,
JDK 21 `/usr/lib/jvm/java-21-openjdk`) verified state; IDA/Hopper absent
(frontier); caller-supplied JADX, Binwalk/Unblob, pwntools presence and
versions; headless vs attached profile notes.

## Coverage section — Native binaries (ELF/PE)

Rows to hold: `open_binary` active-target workflows, `analyze_function`,
pseudocode, `binary_overview` (Ghidra), `inspect_binary_layout` offline
pwntools route, NativeAOT boundary, mitigation/symbol/reloc evidence;
per-artifact entries keyed by path+SHA-256.

## Coverage section — Electron / ASAR / JavaScript

Rows to hold: `analyze_javascript_application` summary→module paging,
`trace_application_feature`, module-graph roles vs file paths, bundled-app
inventory (package.json, ASAR member layout), version-diff recipes.

## Coverage section — Archives, packages, managed assemblies

Rows to hold: `open_binary`/`inspect_artifact` member inventory for
ZIP/APK/IPA/MSIX/AppX/DMG; `inspect_managed_artifact` for .NET/CLI PE;
`inspect_android_package` (frontier — no APK demand yet); per-format quirks.

## Coverage section — Firmware, captures, and recorded crashes

Rows to hold: `inspect_firmware_regions`, `extract_firmware` output-dir
convention, Binwalk/Unblob prerequisite state; `inspect_web_network_capture`
provenance and credential exclusions; `list_browser_targets` /
`list_electron_targets` runtime-observation scope; crash-artifact intake
format once one is seen.

## Coverage section — Evidence management and cross-version comparison

Rows to hold: Evidence ID lifecycle, `inspect_analysis_view` paging,
`export_evidence_bundle` / `rea inspect-evidence-bundle`, `get_evidence_bundle`
filter vocabulary, finding-ledger format, `inspect_evm_interface` carrier rules,
artifact-diff procedure (same tool, two SHA-256s).

## Summary

Draft adds six RE-specific admission criteria (pinned target, labeled observation/inference/unknown, resolvable Evidence-ID citation, stated coverage boundary, pinned tool/provider versions, typed static-vs-runtime evidence) and five weak signals, plus a seven-section coverage-map skeleton mirroring the domain's surfaces; all grounded in the installed REA skill v37 and CORPUS.md evidence rules, for integrator merge into the lane's QUALITY.md/README.md.
