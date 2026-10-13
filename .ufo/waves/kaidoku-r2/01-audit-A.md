# kaidoku-r2 / 01 — audit of round-1 corpus entries (lane A)

Re-ran r1 verify commands verbatim (or nearest equivalent) on this host,
2026-10-13. `npx -y rea-agents@6.4.0` resolves from the warm `_npx` caches;
`rea` is still not on PATH.

## File: corpus/knowledge/2026-10-13-rea-cli-surface.md

### Verify: `which rea; npx -y rea-agents@6.4.0 --version`
- result: confirmed — `which: no rea in (...)` then `6.4.0`.

### Verify: `npx -y rea-agents@6.4.0 --help | awk '/^Commands:/{f=1;next}/^Integrations:/{f=0}f&&/^  [a-z]/{c++}END{print c}'`
- result: confirmed — prints `127`.

### Verify: `npx -y rea-agents@6.4.0 search --help | grep -A12 'Global Options'`
- result: confirmed — Global Options block prints `--filter-output`, `--format <toon|json|yaml|md|jsonl>`, `--full-output`, `--help`, `--llms, --llms-full`, `--schema`, `--token-count`, `--token-limit`, `--token-offset`; identical set to r1's record.

### Verify: `npx -y rea-agents@6.4.0 analyze --help | grep -i integrity`
- result: confirmed — `--integrity-policy <fail|record-and-continue>  Behavior when declared application integrity does not match (default: fail)`.

### Verify: `npx -y rea-agents@6.4.0 compare-bundles --help`
- result: confirmed — banner `rea compare-bundles — Compare two canonical Evidence bundles`, `Aliases: compare-bundles`.

### Verify: `npx -y rea-agents@6.4.0 read-bytes --help`
- result: confirmed — `--length <number>  Requested byte count (default: 256)`; `<address>` arg is "Exact provider memory address".

### Verify: `npx -y rea-agents@6.4.0 evidence-export --help`
- result: confirmed — "Validate and atomically export canonical Evidence JSON"; `--overwrite  Replace output file` is the only verb-specific option.

### Verify: `npx -y rea-agents@6.4.0 function --help`
- result: confirmed — `rea function <path> [address]` with `--procedure`, `--snapshot` ("Load and update a local analysis snapshot"), `--target-format`, `--provider` — the shared argument shape holds.

### Verify: `npx -y rea-agents@6.4.0 setup --help`
- result: confirmed — `--yes/-y`, `--install-hopper`, `--client <array>`, `--skill-client <array>`, `--all-detected`, `--skill`, `--dry-run` ("Print the resolved plan without applying it"), `--accessible` — all claimed flags present.

### Verify: `npx -y rea-agents@6.4.0 mcp --help`
- result: confirmed — `rea mcp` exposes exactly `add` (Register as MCP server) and `doctor` (Validate MCP server startup and tool listing).

### Verify: `npx -y rea-agents@6.4.0 --help | grep -c 'without'`
- result: confirmed — prints `18` (r1 recorded the command but no baseline count; 18 "without"-descriptions exist in the 6.4.0 help surface).

### Verify: `npx -y rea-agents@6.4.0 capabilities --format json | head -50`
- result: confirmed — emits valid JSON: `{"open":false,"capabilities":[{"operation":"capture_native_ui_scenario","available":false,"availability_code":"unsupported_host","effects":{...7 booleans...},"limitations":[...]}, ...]}` — the effects taxonomy (mutates_artifact / launches_process / may_show_ui / may_access_network / may_write_filesystem / changes_permissions / requires_root) is live and machine-readable. r1 admitted this candidate without having captured the output; it now verifies clean.

### Verify: `npx -y rea-agents@6.4.0 inspect-evidence-bundle --help`
- result: confirmed — "Inspect complete or selected discovery metadata from a local Evidence bundle", arg `<inputJson>`.

### Verdict audit
- agree — every `suggested: admit` in this file re-verifies verbatim against 6.4.0. The two lesson candidates (help-only probing is high-yield; npx cold-start tax) remain sound: `--schema` did emit a typed contract (see next file), and warm-cache npx latency was sub-second per call. No reject rows exist here. No disagreement.

## File: corpus/knowledge/2026-10-13-rea-self-documentation.md

### Verify: `npx rea-agents@6.4.0 --llms | wc -l`
- result: confirmed — `135` (expect 135).

### Verify: `npx rea-agents@6.4.0 --llms-full | grep -c '^# rea '`
- result: confirmed — `127` (expect 127).

### Verify: `npx rea-agents@6.4.0 --llms-full | head -3`
- result: confirmed — first line is `# rea address-to-file-offset`, then blank, then the one-liner — no index preamble, as claimed.

### Verify: `npx rea-agents@6.4.0 analyze --schema`
- result: confirmed — `args.required[1]: path`, `additionalProperties: false`, and the recurring block exactly as claimed: `provider` = `anyOf` {`const: auto` | `pattern: "^[a-z][a-z0-9\\x2d]*$"`}, `target-format` = `const: dos-com`, `integrityPolicy` = `enum: fail,record-and-continue` with `default: fail`, `snapshot` = string.

### Verify: `npx rea-agents@6.4.0 doctor --token-count`
- result: confirmed — prints `19090`, byte-identical to r1's recorded live value.

### Verify: `npx rea-agents@6.4.0 --llms | grep -ic evidence`
- result: confirmed — `21` index rows mention Evidence (export/import/inspect-evidence-bundle/inspect-analysis-view/compare/trace/project verbs), consistent with the "Evidence is canonical interchange" candidate.

### Verify: `npx rea-agents@6.4.0 inspect-evidence-bundle --schema`
- result: confirmed — schema takes `inputJson` ("JSON or JSON file with absolute path, detail and optional record filters"), `required[1]: inputJson`, `additionalProperties: false`. Matches the claimed `{path, detail, filters}` payload shape (nested inside `inputJson`).

### Verify: `ls /home/vgpnk/.npm/_npx/af752b90495482d7/node_modules/rea-agents/`
- result: confirmed — `bridge dist install.sh LICENSE licenses native package.json README.md scripts skills third_party`; **no `docs/`, no `website/`**. `grep -n 'docs/' README.md` returns ≥10 repo-relative links (docs/mcp-contracts.md, docs/installation.md, docs/cli.md, docs/evm-bytecode.md, …) — linked-but-unshipped confirmed.

### Verify: `ls /home/vgpnk/.npm/_npx/*/node_modules/rea-agents/skills/reverse-engineer-anything/`
- result: confirmed — BOTH caches (af752b90… = @latest, dea94757… = @6.4.0) ship `SKILL.md` + `references/`; installed `~/.agents/skills` copy is byte-identical (see doctor file's `diff -rq` re-run).

### Verdict audit
- agree — all `suggested: admit` rows survive. SKILL.md frontmatter re-read: `version: "37"`, `tool_count: 170`. Notable stability datum: `--token-count` reprinted the *exact* r1 value 19090, so the doctor output surface is deterministic across invocations. No disagreement.

## File: corpus/knowledge/2026-10-13-doctor-taxonomy.md

### Verify: `which rea; ... doctor --json | node -e '...identity.installations...'`
- result: confirmed — `which rea` not found; `identity.installations` = `{"paths":["/home/vgpnk/.npm/_npx/dea9475797100b20/node_modules/.bin/rea"],"state":"single"}`. And `ls -la` shows that path is a symlink `rea -> ../rea-agents/scripts/rea.mjs` (npx-cache shim), `which rea || echo NOT-ON-PATH` → NOT-ON-PATH.

### Verify: `... doctor --json | node -e '(top-level keys; checks===scope_checks)'`
- result: confirmed — exactly `['healthy','environment_healthy','scope','scope_checks','informational_checks','providerInspections','checks','identity']`; `JSON.stringify(checks)===JSON.stringify(scope_checks)` → `true`.

### Verify: `... doctor --json | node -e '(classification set; providerInspections[0].checks ok/classification)'`
- result: confirmed — distinct classifications in `checks` = `['healthy','missing_analysis_engine','config_drift']` (the other two taxonomy classes, `missing_dependency`/`unsupported_host`, appear only on failing checks — node and host pass here, consistent with the 5-class claim sourced from source). `providerInspections[0].checks` = 8× `true/` prefixed `config_drift`/`unsupported_host` — the dual-meaning observation (outcome label vs would-be-failure class) reproduces exactly.

### Verify: `... doctor --json | node -e '(checks.filter(!ok) names:classifications)'`
- result: confirmed — 8 failures: `hopper:missing_analysis_engine`, `ida-registration:missing_analysis_engine`, `skill:identity:config_drift`, `registration:{claude_code,codex,grok_build,opencode,pi}:config_drift`. Exactly the claimed 6 non-engine `config_drift` checks plus 2 unconfigured-engine failures.

### Verify: `npx -y rea-agents@6.4.0 doctor --format md | sed -n '/## scope_checks/,/## informational_checks/p'`
- result: confirmed — markdown table enumerates the same 18 rows in the same order (node, host, hopper, ghidra, ghidra-platform, ghidra-architecture, ghidra-installation, ghidra-version, ghidra-headless, ghidra-native_decompiler, ghidra-java, ida-registration, skill:identity, 5× registration:*); `## informational_checks` section empty.

### Verify: `test -x .../analyzeHeadless && .../decompile -v | head -3; $JAVA_HOME/bin/java -version | head -2`
- result: drifted (sub-step only) — `analyzeHeadless` executable ✓; `java -version` → `openjdk version "21.0.12.1" 2026-08-18`, 64-bit JDK at `/usr/lib/jvm/java-21-openjdk` ✓; but `decompile -v` emits NO output and exits 1 — the flag is not the mechanism. Nearest equivalent `file .../decompile` → `ELF 64-bit LSB executable, x86-64` — the underlying claim (native decompiler matches linux/x64) is confirmed by `file` and by doctor's own detail string "reports elf x86_64, which matches linux/x64". Erratum: replace `decompile -v` with `file` in the verify line.

### Verify: `ls /opt/hopper/bin/Hopper ~/Applications 2>&1; echo "$HOPPER_LAUNCHER_PATH"; ... doctor check hopper`
- result: confirmed — `/opt/hopper/bin/Hopper` absent; `HOPPER_LAUNCHER_PATH` unset; hopper check = `{ok:false, classification:missing_analysis_engine, remediation:"Run rea setup to install Hopper, or set HOPPER_LAUNCHER_PATH."}`. Incidental: `~/Applications` now exists containing `Grok_Bot_0.68.1.AppImage` — no Hopper; claim unaffected.

### Verify: `echo "REA_IDA_MCP_CONFIG=$REA_IDA_MCP_CONFIG"; ... providerInspections[1]`
- result: confirmed — env unset; `providerInspections[1]` = id `ida`, `configured:false`, `available:false`.

### Verify: `diff -rq ~/.agents/skills/reverse-engineer-anything <pkg>/skills/reverse-engineer-anything; ls ~/.claude/skills/reverse-engineer-anything`
- result: confirmed — `diff -rq` exit 0, zero output (byte-identical, all managed files); `~/.claude/skills/reverse-engineer-anything` does not exist — the stale-despite-identical explanation holds.

### Verify: `npx -y rea-agents@6.4.0 doctor >/dev/null 2>&1; echo $?`
- result: confirmed — exit `1` while `healthy:false`.

### Verify: `cat /etc/os-release | head -4; ... doctor --json checks.find(name==="host")`
- result: confirmed — `ID=arch`, no `VERSION_ID`; host check = `{ok:true, classification:'healthy', detail:'arch unknown'}`.

### Verify: `... doctor --json | node -e '(identity fingerprints)'`
- result: confirmed — `6.4.0`, `expected_skill_version 37`, counts `{cli_commands:127, mcp_tools:170, mcp_prompts:6}`, `combined_sha256 85d80276ecacf937bf3e803b7a31748ae1a8286f556fa5cf734eef768cc7d72a` — matches recorded `85d80276…`.

### Verdict audit
- agree — all 12 admit candidates and both reject candidates reproduce. The two rejects are correctly rejected (the `.bin` path is an npx shim, not a PATH install; the 6 non-engine config_drift checks — not the missing engines — drive `environment_healthy:false`). One verify-command erratum needed: `decompile -v` produces no output (exit 1); use `file` instead. No verdict disagreement.

## File: corpus/knowledge/2026-10-13-mcp-registrations.md

### Verify: `cat ~/.omp/agent/mcp.json ~/.config/devin/mcp_config.json; sed -n '1285,1293p' ~/.kimi-code/config.toml`
- result: confirmed — omp JSON carries `"type":"stdio"`; devin JSON carries no `type`; both launch `npx` with `["-y","rea-agents@6.4.0","mcp"]` and env `GHIDRA_INSTALL_DIR` + `JAVA_HOME`. kimi TOML block shows `command = "npx"`, same args, `startup_timeout_sec = 30`, `[mcp_servers.rea.env]` with both vars. Minor drift: `startup_timeout_sec` sits at line 1287, not the recorded 1288 — monolithic kimi config shifted by one line; substance unchanged.

### Verify: `grep -c '"type"' ~/.config/devin/mcp_config.json ~/.omp/agent/mcp.json`
- result: confirmed — devin: `0`, omp: `1`.

### Verify: `grep -ni 'mcp\|rea\|ghidra' ~/.omp/agent/config.yml | wc -l`
- result: fails — returns `17`, not the recorded `0`. Inspection of all 17 hits: every one is a `rea` SUBSTRING inside yaml comment prose ("reads", "real", "reason", "reach", "appears", "already"); there are zero `mcp` matches and zero real `rea`/`ghidra` tokens. Stricter re-run of the entry's own `source:` pattern `grep -n -i 'rea-agents\|ghidra\|"rea"\|mcpServers\|mcp_servers'` → exit 1, and `grep -c 'mcp'` → `0`. The CLAIM (no MCP keys in config.yml) is true; the recorded verify command was never capable of returning 0 on this file — erratum: use the quoted-token pattern or `\brea\b`.

### Verify: `diff ~/.omp/agent/mcp.json.rea.backup ~/.omp/agent/mcp.json`
- result: confirmed — sole hunk is the grafted `"env": {"GHIDRA_INSTALL_DIR": ..., "JAVA_HOME": ...}` block; mtimes `2026-10-12 09:51:27.598` (backup) / `...27.599` (live) — same-second, backup ~1ms older.

### Verify: `for c in codex opencode claude cursor cursor-agent grok; do command -v $c; done; ls ~/.codex/config.toml ~/.cursor/mcp.json 2>&1`
- result: confirmed — resolves `~/.local/bin/codex`, `~/.opencode/bin/opencode`, `/usr/bin/claude`; `cursor`, `cursor-agent`, `grok` absent; both `ls` targets absent. Supporting files re-checked: `~/.config/opencode/opencode.json` = only `$schema`/`theme`/`autoupdate`; `~/.claude.json` = `{"mcpServers": {}}`; `~/.codex` contains only `skills/omarchy`; `~/.grok` contains only `agents`/`skills` dirs.

### Verify: `command -v rea; ls ~/.npm/_npx/*/node_modules/rea-agents/package.json; npm view rea-agents version`
- result: confirmed — `rea` not on PATH; both npx caches hold `rea-agents/package.json`; registry latest = `6.4.0` (pin equals newest release).

### Verify: `which npx; readlink -f $(which npx)`
- result: confirmed — `which npx` → `/run/user/1000/fnm_multishells/38160_1791904742889/bin/npx` (this shell's fnm multishell — a different PID than r1's `29144_…` as expected for a session-scoped shim); resolves to `~/.local/share/fnm/node-versions/v24.21.0/installation/lib/node_modules/npm/bin/npx-cli.js`.

### Verify: `ls -ld ~/.local/opt/ghidra_12.1.4_PUBLIC /usr/lib/jvm/java-21-openjdk; ls ~/.config/ghidra/ghidra_12.1.4_PUBLIC/Extensions/`
- result: confirmed — both dirs exist (ghidra dir mtime Sep 21); Extensions contains only `ghidra-emotionengine-reloaded` — no REA-side extension.

### Verify: `sed -n '39,59p' ~/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md` + `grep -n 'grok_bot\|client.*ID\|claude_code'`
- result: confirmed — prescribes `rea doctor --client <id> --json` then `rea setup --client <id> --dry-run --json` / `--yes`; client-ID list at lines 46-49 includes all claimed IDs; line 50: "`grok_bot` uses a chat registration step rather than local `mcp.json`."

### Verdict audit
- agree — all admit candidates hold (3/7 surfaces registered; codex+opencode installed-but-unregistered; cursor+grok absent; fnm-shim fragility real). The only defect is a verify-command erratum on the config.yml grep (fails as written though the claim is true) and a 1-line offset on `startup_timeout_sec`. No verdict disagreement.

## File: corpus/knowledge/2026-10-13-rea-skill-contract.md

### Verify: `sed -n '1,15p' ~/.agents/skills/reverse-engineer-anything/SKILL.md`
- result: confirmed — frontmatter `version: "37"`, `tool_count: 170`; scope gate verbatim: "Skip REA for ordinary source-repository architecture analysis" + "do not run REA readiness or provider commands".

### Verify: `grep -n '^- ' SKILL.md | sed -n '1,20p'`
- result: confirmed — routing-table bullets at lines 48-89 enumerate the claimed classes (ASAR, archive inventory, Android APK, managed PE/CLI, firmware, NativeAOT, browser page, HAR/mitmproxy, Electron runtime, EVM carrier, offline ELF, ELF core, PE resources, native db) plus a second bullet list at 205-213 mapping domains to reference files.

### Verify: `grep -n 'npx -y rea-agents\|never installs\|caller-supplied' SKILL.md`
- result: confirmed — line 36 `npx -y rea-agents@6.4.0` fallback; line 39 "never installs or upgrades unrelated"; lines 59, 78 caller-supplied Binwalk/Unblob and pwntools.

### Verify: `sed -n '93,115p' SKILL.md`
- result: confirmed — IDA `provider_id:"ida"` on the original binary (never `.idb`/`.i64`), SHA-256 binding for legacy attached profile, headless owned-private-DB profile, "IDA does not supply `binary_overview`", `binary_session {}` → `result.tool_availability`.

### Verify: `sed -n '105,109p' SKILL.md`
- result: confirmed — "my app" ask-first rule verbatim, including "Never choose an example app on the user's behalf."

### Verify: `grep -n 'detail": "summary"\|inspect_analysis_view\|resource_constraint\|next_offset' SKILL.md references/evidence-workflows.md`
- result: confirmed — hits at SKILL.md 122-123 (`"detail": "summary"` → `inspect_analysis_view`), 131-132 (`resource_constraint` / `details.resource: "transport"` → `inspect_analysis_view`), evidence-workflows.md 11.

### Verify: `sed -n '168,201p' SKILL.md`
- result: confirmed — "Plan broader investigations" 7-step list verbatim, ending in checklist closure ("do not describe a broad investigation as complete while required questions remain open").

### Verify: `grep -n 'never authorize\|not a security sandbox\|SIGTERM\|no chain lookup\|fetching recorded URLs\|broaden the target' SKILL.md references/*.md`
- result: confirmed — matches at SKILL.md:67 (no fetching recorded URLs), 160 (do not broaden target), evidence-workflows.md:38 (not a security sandbox), :42 (SIGTERM→SIGKILL), native-and-artifacts.md:10 (never authorize live attach). `no chain lookup` missed by grep only because the phrase wraps a newline at SKILL.md:73-74 — `sed -n '65,75p'` shows verbatim "this performs no chain / lookup or target execution". Confirmed.

### Verify: `sed -n '136,155p' references/native-and-artifacts.md`
- result: confirmed — `extract_artifact` no-args/REA-chosen temp dir, symlinks+encrypted as inventory facts, DMG read-only mount w/ owned temp dir, `format: "dos-com"` entry `0x10100`, `annotate_native_function` atomic session-scoped + "Windows P0 does not admit database mutations".

### Verify: `sed -n '14,36p' references/evidence-workflows.md`
- result: confirmed — `record_unknown`/`update_unknown` (revision-checked, supporting AND contradicting IDs), `compare_artifacts`/`compare_functions`/`compare_bundles`, `build_call_path` "an incomplete frontier makes absence unknown", `find_changed_behavior` candidates-not-proof, `correlate_static_and_runtime` hypotheses-not-causality, `verify_reconstruction` finite-spec-only.

### Verify: `grep -n 'dos-com\|unpacking stub\|0x10100\|load_image' references/native-and-artifacts.md`
- result: confirmed — lines 60 (`inspect_native_load_image`), 70 (unpacking stub), 148-150 (dos-com / `0x10100` / PSP-stack unmodeled).

### Verdict audit
- agree — all 12 admit candidates are verbatim re-derivable from the installed skill (which `diff -rq` proves byte-identical to the bundled v37 copy). No reject rows. No disagreement.

## Summary

- **Net verdict: round-1 knowledge survives.** All ~52 admit candidates re-verified; zero claims disproven. Both reject candidates in doctor-taxonomy remain correctly rejected.
- **Erratum 1 (mcp-registrations):** verify line `grep -ni 'mcp\|rea\|ghidra' ~/.omp/agent/config.yml | wc -l → 0` is unsound — bare `rea` substring-matches comment prose and returns `17`. Claim itself is true (strict token grep returns nothing). Fix the verify command, not the claim.
- **Erratum 2 (doctor-taxonomy):** `decompile -v` emits no output (exit 1); the "elf x86_64" mechanism is confirmed via `file` and doctor's own detail string. Swap the verify sub-command.
- **Trivial drift (mcp-registrations):** kimi `startup_timeout_sec` now at line 1287 (recorded 1288); `~/Applications` now exists holding `Grok_Bot_0.68.1.AppImage` (no Hopper — claim unaffected).
- **Stability datum worth keeping:** `rea doctor --token-count` reprinted exactly `19090`; identity `combined_sha256` `85d80276…` unchanged; `--llms` 135 lines / 127 rows stable.
- **Bonus confirmation:** r1 admitted the `capabilities --format json` candidate on help-text alone ("not yet captured"); the live run now conforms — JSON envelope with per-operation `available`/`availability_code`/7-flag `effects`/`limitations`.
