# kaidoku-r2 — 04 — CONSISTENCY audit (index files vs corpus on disk)

Audit date: 2026-10-13. Scope: `corpus/README.md`, `corpus/QUALITY.md`, `PROVINCE.md`,
`SKILL.md`, `LOG.md` vs `corpus/knowledge/*`, `corpus/lessons/*`, commit `a43d442`,
wave evidence at `<shokunin>/.ufo/waves/kaidoku-r1/`, and live host probes.

## corpus/README.md

- PASS: Knowledge table — all 14 rows resolve to existing files
  (`corpus/knowledge/2026-10-13-*.md`), and all 14 corpus `.md` files have a row.
  Exact 1:1 (`.gitkeep` correctly unrowed).
- PASS: Lessons table — sole row `2026-10-13-round-1` resolves to
  `corpus/lessons/2026-10-13-round-1.md`; no unindexed lesson file.
- PASS: Coverage map — every entry slug resolves to a knowledge file and every
  knowledge file appears exactly once; section states match corpus content
  (3/7 registrations devin/omp/kimi per `mcp-registrations`; 127 commands +
  `--llms`/`--llms-full`/`--schema` per `rea-cli-surface`; v37 contract;
  Ghidra 12.1.4 8/8 + JDK 21.0.12.1; 30/167/190 jq numbers; 413 PEs surveyed-
  not-held; 6 asars + wave-16 `analyze_javascript_application` e2e; 1556 signed
  archives; ~341 framework DLLs + AnyCPU rejection; 174 zstd cores unprobed).
- PASS: Frontier and Known-gaps sections are consistent with the corpus — no
  diff run recorded anywhere; `tool_availability` wave-16-only; `skill: stale`
  attributed to the missing `~/.claude/skills/` destination (live: dir holds only
  `omarchy`); `~/.local/bin/jq` impostor frontier matches `pacman-packages`.

## corpus/QUALITY.md

Sampled 5 admitted candidates across 5 files: (A) `rea-live-jq-e2e` "one-shot
analyze→search→decompile pipeline", (B) `asar-surface` "Obsidian app.asar is the
main-process bundle", (C) `managed-assemblies` ".NET host + two runtimes, no SDK",
(D) `doctor-taxonomy` "environment_healthy=false caused by 6 config_drift checks",
(E) `pacman-packages` "unowned `~/.local/bin/jq` shadow".

- PASS (criterion 4 — artifact identity): all 5 name absolute paths plus stable
  identity (A: full sha256 `e8156675…7806`; B: paths + sha256 prefixes + `pacman
  -Q obsidian 1.13.7-2`; C: `/usr/bin/dotnet` v10.0.11 + pacman pkgs; D:
  `rea-agents@6.4.0` + npx cache dir `dea9475797100b20`; E: path + digest
  `b1c22172…70f`). Minor: E and B use truncated digests (prefix+suffix), weaker
  than the criterion's full-SHA-256 letter but still host-unique.
- FAIL (criterion 5 — observation/inference/unknown labels): 4 of 5 sampled
  files do not label conclusions. Only `elf-observation-jq.md` carries explicit
  OBSERVATION/INFERENCE blocks (and `pe-surface.md` partial inline
  "(OBSERVED)/(INFERRED)" tags). Concrete violation: `rea-live-jq-e2e.md:54`
  states the decompiler-derived "FUN_00103fa0 is jq's `process()` loop" as fact
  in the admit rationale — exactly the inference-masquerading-as-conclusion
  class criterion 5 governs. The corpus schema (`claim/source/verify/suggested`)
  implicitly separates tool output from claim but never assigns the required
  label; criteria 4–9 were admitted in the same commit as the entries, so the
  corpus carries a retroactive-consistency gap.
- PASS (criterion 6 — Evidence ID or reproducing call): every REA-derived claim
  in the sample cites the exact reproducing call with expected output (e.g. A's
  `analyze … → expect 167`); none invokes an Evidence ID it cannot produce.
- PASS (criterion 7 — names the unexamined): D names scoped modes not run and
  hopper sub-checks that "cannot fire here"; A names pwntools absence and
  snapshot≠DB-cache; C enumerates absent SDK/Mono/decompiler; B names the
  `~/.config` zero-yield scope. A does not record per-call detail levels — thin
  but inside tolerance for a CLI probe.
- PASS (criterion 8 — version pins + claim source): all capability claims pin
  `rea-agents@6.4.0`, Ghidra 12.1.4, JDK 21.0.12.1, node v24.21.0, or pacman
  pkg versions, and say whether the source is live tool output or shipped text.
- PASS (criterion 9 — runtime-behavior provenance): no sampled entry derives
  runtime behavior from a static graph; `elf-observation-jq.md:100-127` even
  files `jq --version` explicitly as the runtime-evidence class.

## PROVINCE.md

- PASS (Core — REA MCP server): live re-verified — `rea-agents@6.4.0` present in
  `~/.config/devin/mcp_config.json` and `~/.omp/agent/mcp.json`;
  `[mcp_servers.rea]` stanza confirmed in `~/.kimi-code/config.toml` (block spans
  ~:1284-1291; the `:1285` pin lands on its `command = "npx"` line — resolves,
  off-by-one vs the block header). `devin/omp aligned` backed by
  `doctor-taxonomy.md`.
- PASS (Core — `rea` CLI): probe re-run #1 — `npx -y rea-agents@6.4.0 --version`
  → `6.4.0`; `which rea` → absent; 127-command count backed by `rea-cli-surface`.
- PASS (Core — Ghidra provider): probe re-run #2 — install = 876M;
  `Ghidra/application.properties` holds `application.version=12.1.4`, build
  `2026-Sep-21`, rev `8b6bbb85…`; native decompiler ELF present. Note: the
  version property lives in `Ghidra/application.properties`, not an install-root
  file — PROVINCE's `application.version=12.1.4` shorthand resolves but could
  name the path (`ghidra-install.md:12` itself warns about this).
- PASS (Core — JDK 21): probe re-run #3 — `java -version` → `21.0.12.1`;
  `JAVA_HOME` line-pins verified verbatim at `~/.bashrc:24` and `~/.profile:4`.
- PASS (Core — Native ELF): `rea-live-jq-e2e` backs 30 segments / 167 procedures
  / 190 strings / ~5.5s; `/usr/bin/jq` sha256 re-verified live
  (`e8156675…7806`). Minor: "decompile 0x103fa0 recovered `process()` loop" is a
  decompiler inference asserted unlabeled (see QUALITY criterion-5 finding).
- PASS (Core — ASAR): wave-16 draft records `default_app.asar` (electron43) →
  5 files, 41 findings, `ev_2628de89b0f4…` — verbatim match to the table row.
- PASS (Core — archives, evidence discipline, fallback readers): 1556-archive
  signed corpus per `pacman-packages`; byte-identical-jq claim consistent with
  live sha256; snapshot-is-evidence-not-DB per `rea-live-jq-e2e`; `command -v`
  re-sweep confirms all 16 named tools present and every claimed absence
  (`7z`, `cabextract`, `xxd`, radare2/rizin, strace/ltrace, `upx`,
  pacman-contrib's `paccheck`/`pactree`/`pacfiles`).
- PASS (Frontier genuinely unprobed): no corpus entry claims any frontier item
  held — PE `open_binary` ("no PE open_binary has run end-to-end", wave-16),
  managed AnyCPU (typed `unsupported PE architecture`), `inspect_recorded_crash`/
  `inspect_firmware_regions`/APK/EVM/runtime-observation/cross-version diffing
  all catalog-listed only, macOS surfaces `unsupported_host`,
  `inspect-binary-layout` typed `provider_unavailable`.

## SKILL.md

- PASS: `npx -y rea-agents@6.4.0` → live `6.4.0`; "170 tools / 127 commands"
  matches doctor `identity.catalog.counts` recorded in `doctor-taxonomy.md`.
- PASS: Ghidra path `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC` and JDK 21
  resolve live.
- PASS: every tool name in the routing contract resolves against the corpus-
  recorded v37 table (`analyze_javascript_application`, `inspect_artifact`,
  `open_binary`, `inspect_managed_artifact`, `inspect_recorded_crash`,
  `inspect_firmware_regions`, `inspect_binary_layout`, `inspect_analysis_view`,
  `binary_session`, `parent_evidence_id`, `detail:"summary"`).
- PASS: "(SKILL v37 table)" — installed `~/.agents/skills/reverse-engineer-
  anything/SKILL.md` carries `version: "37"` (live).
- PASS: `/tmp/rea-ghidra-*` ephemerality, `--snapshot` = evidence not DB,
  pwntools absent, referenced `corpus/knowledge/2026-10-13-elf-observation-jq.md`
  exists; anti-trigger consistent with REA skill's own source-repo non-goal;
  `/usr/bin/jq` and `default_app.asar` verification claims match corpus + wave-16.

## LOG.md

- PASS: "16-lane curation wave" — `.ufo/waves/kaidoku-r1/` holds exactly 16 lane
  files; "14 knowledge entries admitted" — commit adds exactly 14 knowledge
  files; "4 reject candidates retained in-file" — exactly 4 `suggested: reject`
  rows exist (doctor-taxonomy ×2, asar-surface ×1, elf-observation-jq ×1).
- PASS: lessons file, QUALITY grown to 9 criteria + 5 signals, PROVINCE/SKILL
  fills, and README build are all present in the `a43d442` diff; "167
  procedures" matches `rea-live-jq-e2e`.
- FAIL (minor): "evidence_id-bearing output" for the jq run is unevidenced —
  neither the corpus entry nor `kaidoku-r1/10-rea-live.md` records a literal
  `ev_*` id for the jq CLI run (only snapshot `evidence_bundle` keys). Verbatim
  `ev_` ids exist only for wave-16's MCP runs on other targets.
- FAIL (minor): "Frontier probed-not-held: … firmware regions" — firmware was
  catalog-listed, never probed (wave-16: "catalog-listed"); the other four
  items were probed to typed failures. Grouping overclaims one item.
- FAIL (minor, omission): commit `a43d442` also modifies `SHONEN.md` (ticks 3
  promotion checkboxes) — unrecorded in the LOG entry; repo AGENTS.md requires
  every change logged with motivating evidence.
- PASS (note): "`fleet .ufo/waves/kaidoku-r1/`" resolves outside the repo
  (sibling `.ufo/` of `shokunin/`) — shorthand used consistently in corpus
  headers; flagged for awareness, not counted as a FAIL.

## Summary

All five index files are structurally consistent with the on-disk corpus —
every table row resolves, every Core claim traces to a corpus entry or a live
probe (3 probes re-run: `rea-agents --version` → 6.4.0, `java -version` →
21.0.12.1, fallback-reader `command -v` sweep — all exact matches), every
Frontier item is confirmed unprobed, and all SKILL.md references resolve.

FAILs and required errata:

1. **QUALITY.md criterion 5 vs corpus** — admitted entries (all files except
   `elf-observation-jq.md`, plus partial `pe-surface.md`) do not label
   conclusions observation/inference/unknown; concrete violation at
   `corpus/knowledge/2026-10-13-rea-live-jq-e2e.md:54`. Erratum: either annotate
   admitted entries with the labels or add a superseding criterion-5 row
   declaring the `claim` field an implicit observation unless tagged.
2. **LOG.md vs commit a43d442** — (a) `SHONEN.md` checkbox change unrecorded;
   (b) "evidence_id-bearing output" has no recorded `ev_` id for the jq run;
   (c) firmware listed under "probed-not-held" though only catalog-listed.
   Erratum: one appended LOG line noting the SHONEN touch, and tighter wording
   on the two claims.

Minor errata (not blocking): truncated SHA-256s under criterion 4
(`b1c22172…70f`, `8588f1fd…`); PROVINCE `application.version` shorthand vs
`Ghidra/application.properties`; `config.toml:1285` pin off-by-one vs stanza
header `:1284` (also in `mcp-registrations.md:11` "lines 1285-1292"); `.ufo/`
paths in LOG/corpus headers resolve outside the repo root.
