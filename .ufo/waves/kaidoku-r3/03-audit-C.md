# kaidoku-r3 · 03-audit-C — round-3 re-verification audit of round-2 knowledge files

Audit lane: kaidoku-shokunin round 3. Date: 2026-10-13 ~12:43–12:47 -03 (host up 1:49, no reboot since round 2). All commands re-run live in this audit window; nothing installed, nothing modified. Note on dispatch path: the assigned file `2026-10-13-r2-doctor-reverify.md` exists on disk as `2026-10-13-r2-doctor-reverify-r2.md` (extra `-r2` suffix) — audited under its real name. `rea` is not on PATH; all `rea <verb>` rows re-run as `npx -y rea-agents@6.4.0 <verb>` (same pinned package). Incidental: my own scratch `/tmp/kaidoku-r3-doctor.json` (68,124 B, written 12:43) was selectively deleted mid-audit — every other r3 scratch file survived; all values were already extracted. Recorded as /tmp churn, not evidence drift.

## File: corpus/knowledge/2026-10-13-r2-evidence-bundle-schema.md

### Verify: `sha256sum /usr/bin/true; stat -c %s /usr/bin/true` → expect `8bc9a73a…`, 43,320 B
- result: confirmed — `8bc9a73afd7d85061160857536e093ded799dae7a2f0cf5758c4553f2f83002d`, 43,320 B, identical to the pinned target.

### Verify: `npx -y rea-agents@6.4.0 analyze /usr/bin/true --snapshot /tmp/kaidoku-r3-audit.snap.json --format json`
- result: confirmed — snapshot written 10,323 B mode `0600` (byte-size identical to r2's), envelope keys exactly `{binding, entries, evidence_bundle, target, workflow_entries}`. `evidence_id` = `ev_982c6020636b96c8a515f43081fd749cec7c15f448023d9b4b18b7e5780171a8` — the same `ev_982c…` semantic id as r2, content-addressing reproduced across rounds. Record provider `rea-workflow` v1, operation `binary_overview`, confidence `derived`.

### Verify: snapshot internals — `binding` sha256-free, `target.sha256` carries digest, workflow entry carries `analysis_profile`
- result: confirmed — `target = {sha256:8bc9a73a…, kind:executable, format:elf, architecture:x86_64}`; `binding` keys exactly `{provider, analysis_profile}` with no sha256 anywhere inside (`"sha256" in json(binding)` → False); `binding.provider` = ghidra 12.1.4, `analysis_profile.digest` = `a04af771…`. `workflow_entries[0].execution` keys = `{analysis_profile, limitations, locations, provider, raw_result, result, subject}` — the extra `analysis_profile` field vs plain entries confirmed structurally.

### Verify: population asymmetry — `entries` vs `workflow_entries` after CLI `analyze`
- result: confirmed — after one CLI `analyze`: `entries` length 0, `workflow_entries` length 1, `records` length 1, `providers:[rea-workflow]` only (ghidra enters the manifest when a `search` record lands). Matches the `isWorkflowEvidenceTool` / provider-direct split described from `DirectAnalysis.js`.

### Verify: `inspect-evidence-bundle /tmp/…snap.json` (bare path) → expect invalid_input failure
- result: confirmed — `code:invalid_request, category:invalid_input, retryable:true`. Minor wording note: the candidate text says a bare path "fails `missing_argument path`" — actual top-level code is `invalid_request`/`invalid_input` with generic message (run log row 4's `invalid_input` is the accurate part). Substance holds: a bare path is parsed as the spec and rejected.

### Verify: `inspect-evidence-bundle '{"path":"<envelope>"}'` → expect evidence_integrity_mismatch
- result: confirmed verbatim — `code:evidence_integrity_mismatch, category:integrity_mismatch, retryable:false`, message `artifacts: Invalid input: expected array, received undefined (6 more issues)`. The envelope is still refused by the canonical-bundle path.

### Verify: extract inner `evidence_bundle` → `inspect-evidence-bundle '{"path":"<bundle>"}'` → OK; `evidence-export` envelope → mismatch; inner → OK; `evidence-import` → `{imported:1,…}`
- result: confirmed — inner bundle inspect echoes canonical bundle with `artifacts[1] = {sha256:8bc9a73a…, elf, x86_64}`. Export of the envelope: `evidence_integrity_mismatch`. Export of the inner bundle: `{bytes:4687, records:1}` — same 4,687-byte size as r2's 1-record export, and canonical-JSON comparison shows the exported file is exactly the inner `evidence_bundle` (`json.dumps(sort_keys)` equal). Import: `{imported:1, unknowns_added:0, total:1}`.

### Verify: `detail:"summary"` + `filters.operation:"binary_overview"` → `evidence-bundle-summary` matching_records 1; bogus filter key → `unknown_argument`; filters without summary → fail
- result: confirmed — summary returns `{kind:evidence-bundle-summary, filters:{operation:binary_overview}, total_retained_records:1, matching_records:1, unknown_revisions:0, records:[{evidence_id, subject, provider, operation, confidence:derived, authority:shipped-artifact, analysis_profile_digest, retention:complete-record, limitation_count:1, …}]}` — the documented projection. Bogus filter key: `invalid_request`/`invalid_input` with `details.issues[0] = {path[2]: filters,bogus_key, reason:"unknown_argument"}` — the `unknown_argument` reason string exists at issue level, so the file's claim is substantively exact. `filters` without `detail:"summary"`: same `invalid_request`/`invalid_input` rejection.

### Verdict audit: candidate 1 (envelope ≠ canonical bundle on CLI) — agree — both refusal directions and the accept path reproduced byte-faithfully; export is still canonically identical to the inner `evidence_bundle`.
### Verdict audit: candidate 2 (content-addressed records; replay = entry + record) — agree — identical `ev_982c…` reproduced a day later; schema fields and the workflow-entry `analysis_profile` extra confirmed in the live file.
### Verdict audit: candidate 3 (spec object, two detail levels, five filter keys) — agree — all three behaviors re-verified; `unknown_argument` confirmed as the issue-level reason string.
### Verdict audit: candidate 4 (manifests are derived projections) — agree — `providers:[rea-workflow]` after analyze-only demonstrates projection from `records` (ghidra absent until a ghidra-produced record exists).

## File: corpus/knowledge/2026-10-13-r2-frontier-prereqs.md

### Verify: `command -v apktool jadx adb aapt aapt2 apkanalyzer baksmali dex2jar smali fastboot sdkmanager emulator`; `find /usr /opt ~ -maxdepth 6 -name '*.apk'`; `ls -d ~/Android/Sdk /opt/android*`
- result: confirmed — all 12 tools absent, no SDK dirs, and exactly the same 2 APKs (`android_debug.apk` 127,260,725 B + `android_release.apk` 104,803,334 B, both mtime Oct 11, Godot 4.7.2.stable). **No new APKs appeared.**

### Verify: `echo $REA_JADX_MCP_JAR $REA_JEB_MCP_URL $REA_APKTOOL_COMMAND`; `grep REA_ ~/.config/devin/mcp_config.json ~/.omp/agent/mcp.json`; `find … -iname '*jadx*'`; `java -version`
- result: confirmed — all three env keys unset, zero `REA_*` hits in either client MCP config, no jadx jar anywhere under `/usr /opt ~`, JDK `21.0.12.1` present (the "full JDK" leg still satisfied).

### Verify: `ss -tln | grep -E ':(5037|8425|9222|9223|9229|5858)'`; `pgrep -af remote-debugging` → expect zero listeners/procs
- result: **drifted-transiently, then re-confirmed** — at 12:44–12:46 port **9222** was live (headless chromium `--remote-debugging-port=9222 --user-data-dir=/tmp/kaidoku-chrome`, `/json/version` answering `Chrome/152.0.7977.82`) and port **9223** was live (`/usr/lib/electron43/electron --remote-debugging-port=9223 /tmp/kaidoku-electron`, `/json/list` = 1 page target `file:///tmp/kaidoku-electron/index.html`, profile `~/.config/kaidoku-probe`). Both are kaidoku-named sibling round-3 lanes executing this file's own "smallest viable r3" suggestions verbatim. By 12:47 both were closed — zero debug listeners again, matching the claimed baseline. No 5037 (adb) or 8425 (JEB) at any point.

### Verify: `command -v forge cast anvil solc geth hevm hardhat`; `find ~ -maxdepth 6 (foundry.toml|hardhat.config.*|*.sol|*.evm)`
- result: confirmed — all EVM tools absent, zero carrier/config files. The `inspect_evm_interface`-needs-nothing-external correction stands unchallenged (contract claim, re-read not repeated — no counter-evidence on host).

### Verify: JEB leg — `find /opt /usr/local ~ -iname '*jeb*'`; port 8425
- result: confirmed — no install, port closed, env unset. Absent stays absent.

### Verify: `npx -y rea-agents@6.4.0 capabilities --format json` → 10 macOS ops `unsupported_host`, 3 counter-samples `available:true`
- result: confirmed — all ten (`inspect_macho, inspect_plist, inspect_asset_catalog, demangle_swift, capture_native_ui_scenario, observe_native_ui, observe_native_calls, inspect_signature, inspect_native_dispatch_metadata, list_architectures`) still `available:false / unsupported_host`; counter-samples `inspect_keyed_archive`, `decode_interface_builder`, `trace_dylib_resolution` still `available:true`.

### Verify: substrate leg — chromium, playwright cache, electron binaries, burnerchrome staleness
- result: confirmed — `/usr/bin/chromium`, playwright + agent-browser on PATH, `~/.cache/ms-playwright/{chromium-1248,chromium_headless_shell-1248,ffmpeg-1013}`, `/usr/lib/electron39/electron` + `/usr/lib/electron43/electron` all present; `~/.local/share/burnerchrome/` still the stale Oct-6 profile.

### Verdict audit: candidate (Android APK surface) — agree — corpus present, decode tooling absent; no drift.
### Verdict audit: candidate (Runtime observation) — agree-with-annotation — the "zero bindable endpoints" claim is true at baseline and was true at r2 verified-at, but **during this wave it is transiently false**: sibling lanes are exercising 9222/9223 exactly as suggested. The claim should be read as a host-baseline statement, not a wave-time guarantee. New datum for r3+: the suggested probes demonstrably work end-to-end (Chrome 152 answers `/json/version`; electron43 exposes a file:// page target).
### Verdict audit: candidate (Mach-O closed) — agree — 10/10 unsupported_host reproduced live.
### Verdict audit: candidate (EVM) — agree — host still carrier-free; no new tooling.
### Verdict audit: candidate (JEB) — agree — absence re-verified on every leg.

## File: corpus/knowledge/2026-10-13-r2-doctor-reverify-r2.md

### Verify: `npx -y rea-agents@6.4.0 doctor --json` → 8 keys, audit-wide, scope_checks===checks, informational 0
- result: confirmed — exit 1, identical 8 top-level keys, `scope.mode:"audit-wide"`, `scope_checks` content-equal to `checks`, `informational_checks` length 0.

### Verify: check roster — 18 checks, 10 pass / 8 fail, named failing set
- result: confirmed — exactly 18 checks, 10/8 split, failing set identical: `hopper, ida-registration, skill:identity, registration:{claude_code, codex, grok_build, opencode, pi}`.

### Verify: catalog digests + counts
- result: confirmed — `tools_sha256 25802f6de8c14ba736dc61ff1cbc7c5cd738fd74426aa01338f2dd03e0911166`, `prompts_sha256 5296f0301566cadaf89243e774512011f11045af36d48405f76a3ff9a8947ac2`, `combined_sha256 85d80276ecacf937bf3e803b7a31748ae1a8286f556fa5cf734eef768cc7d72a`; counts `{cli_commands:127, mcp_tools:170, mcp_prompts:6}` — byte-for-byte stable across r1→r2→r3.

### Verify: identity — versions, skill, registrations, providers
- result: confirmed — `cli_package_version 6.4.0`, `expected_skill_version 37`, sdk `{server,client_test,core}=2.3.1`, `live_server.state:"unknown"`, `installations.state:"single"`, skill `{installed_version:37, installed_tool_count:170, state:"stale"}`; registrations: devin + omp `aligned` on `["npx","-y","rea-agents@6.4.0","mcp"]`, grok_bot `manual`, five `missing`; providers: ghidra `configured+available, 12.1.4`, 8/8 sub-checks ok; ida `not_configured`. `node --version` = v24.21.0.

### Verify: env wiring — `grep GHIDRA_INSTALL_DIR|JAVA_HOME` in the three client configs
- result: confirmed — `~/.config/devin/mcp_config.json:11-12`, `~/.omp/agent/mcp.json:12-13`, `~/.kimi-code/config.toml:1290-1291` — same lines, same values (`ghidra_12.1.4_PUBLIC`, `java-21-openjdk`).

### Verify: `npm view rea-agents version`; npx caches at 6.4.0
- result: confirmed-with-footnote — registry still `6.4.0`; both pinned caches `af752b90495482d7` and `dea9475797100b20` still materialized at 6.4.0. `~/.npm/_npx` now holds 6 dirs total (vs 2 in r2) — the 4 new caches (`48f14ab5…, 4b0e2640…, 801188df…, e2094862…`) contain other packages, not rea-agents; the pinned claim "two rea caches both at 6.4.0" remains literally true.

### Verify: `/tmp/rea-ghidra-*` orphan/churn state
- result: confirmed-as-pattern — 4 dirs at 12:44 (`AJQe3R, kd5lXN, N86yEE, SZcFSx`) rotating to 1 (`xgAuTa`, `posix-process-group`, created 12:46) at 12:47. Same live-churn signature r2 recorded; zero stale orphans observed.

### Verdict audit: all nine `verdict: unchanged` checks — agree — third consecutive identical read on every pinned value; the envelope, roster, digests, identity, registration matrix, env wiring, and version pins are byte-stable across three rounds. Session-dir churn remains the only moving part and behaves as recorded.

## File: corpus/knowledge/2026-10-13-r2-libjq-engine.md

### Verify: `readlink -f /usr/lib/libjq.so.1; sha256sum; file; stat; jq --version`
- result: confirmed — resolves to `/usr/lib/libjq.so.1.0.4`, sha256 `7e8bccc6df37a55fb90703c9069b3770f5cdc502e96959c866d2f30fbf5e8b6b`, ELF64 LSB shared object x86-64 **stripped**, 350,384 B, jq-1.8.2.

### Verify: `nm -D` census + named addresses → 181 T / 148 U; `jq_next` 0x17070, `jq_report_error` 0x16fd0
- result: confirmed — exactly 181 `T` exports, 148 `U` imports; `jq_next` at `0x17070` and `jq_report_error` at `0x16fd0` — both pinned addresses intact.

### Verify: `npx -y rea-agents@6.4.0 analyze /usr/lib/libjq.so.1.0.4 --format json` → 29/924/1212
- result: confirmed — `segment_count:29, procedure_count:924, string_count:1212`, `evidence_id ev_bf0875fae37e99efec…` (same id as r2), document `target-7e8bccc6df37.4`. Clarification, not drift: the record's `provider` field is `rea-workflow` v1 (the composed workflow); ghidra 12.1.4 is the underlying engine — visible as `binding.provider` in snapshots. The file's "via provider ghidra 12.1.4" describes the engine correctly.

### Verify: `search --kind procedures --pattern '.' --mode regex` → 924 rows bucketed 181/446/291/6
- result: confirmed — 924 rows; buckets **181** `jq_*`/`jv_*`, **446** `FUN_`, **291** `<EXTERNAL>::`, **6** infra — and the six are the identical set: `_DT_INIT, _DT_FINI, _INIT_0, _FINI_0, thunk_FUN_00106be6, switchD_001195cd::default`.

### Verify: **+0x100000 rebase rule** — `nm` `jq_next` 0x17070 ↔ `search` address on libjq
- result: confirmed — `search --pattern 'jq_next'` returns exactly `{address:"0x117070", value:"jq_next"}`. nm `0x17070` + `0x100000` = `0x117070`. The mapping rule holds exactly (second sample `jq_report_error` 0x16fd0 → implied 0x116fd0 consistent).

### Verify: `decompile /usr/lib/libjq.so.1.0.4 jq_next` → ~839 lines, `switch(uVar17)`, `src/execute.c` asserts, named `jv_*` calls
- result: confirmed — JSON envelope 62,040 B (byte-identical size to r2's), decompiled body 839 lines, `switch(uVar17)` dispatch present, `src/execute.c` referenced 12×, signature present as `undefined1  [16] jq_next(undefined8 *param_1)` (two spaces after `undefined1` — the file's single-space rendering is a transcription nicety), `confidence:observed`, `authority:shipped-artifact`.

### Verdict audit: candidate (libjq identity) — agree — every pinned field identical.
### Verdict audit: candidate (29/924/1212 analyze) — agree — identical evidence id reproduced, strongest possible confirmation.
### Verdict audit: candidate (924 = 181+446+291+6 census) — agree — bucket counts and the six infra names reproduced exactly.
### Verdict audit: candidate (jq_next 839-line VM loop) — agree — byte-identical envelope size, all structural markers present.
### Verdict audit: candidate (driver↔engine inversion + rebase rule) — agree — the +0x100000 rebase is exact and re-verified against live REA output; keep it as the standing nm↔REA mapping rule.

## Summary

31 verify-command groups re-run live across the 4 assigned round-2 files: **29 confirmed, 1 transiently-drifted-then-confirmed, 0 fails, 0 contradictions**.

- **+0x100000 rebase rule: CONFIRMED exactly** — nm `jq_next` `0x17070` → REA `0x117070` on libjq; the full analyze (`ev_bf0875…`, 29/924/1212) and the 924-row census (181/446/291/6 with the same six infra names) reproduce identically.
- **Two-format distinction: CONFIRMED verbatim** — envelope `{target,binding,entries,workflow_entries,evidence_bundle}` mode 0600 still refused by export/inspect (`evidence_integrity_mismatch`, `artifacts: expected array`); inner 7-key bundle accepted; export canonically equal to the inner bundle at the same 4,687 B; `unknown_argument` exists as the issue-level reason for bad filter keys; snapshot `binding` still carries no target sha256.
- **Frontier prereqs: no new APKs, no new tooling, env keys still unset, all closed legs still closed.** The one moving surface: CDP debug ports **9222 and 9223 were transiently live mid-wave** — sibling kaidoku-r3 lanes running the file's own suggested probes (chromium headless on 9222 answering `Chrome/152.0.7977.82`; electron43 on 9223 serving a `file:///tmp/kaidoku-electron/index.html` page target) — both closed again by audit end. Baseline claim remains true; annotate it as host-baseline, not wave-time.
- **Doctor reverify: all nine "unchanged" verdicts upheld for a third consecutive read** — same 8-key envelope, 18 checks 10/8, same failing octet, same three catalog digests (`85d80276…`), same identity/registration/provider rows, same env-wiring line numbers. `/tmp/rea-ghidra-*` churn continues as documented.
- Verdict audit: every `suggested: admit` across all four files upheld; no verdict requires downgrade. Cosmetic notes only: bare-path inspect error is `invalid_request`/`invalid_input` (not literally `missing_argument`), record provider is `rea-workflow` wrapping ghidra, decompile signature carries a double space, and `~/.npm/_npx` grew to 6 dirs (4 non-rea caches — pinned claim unaffected). One self-incident logged: my `/tmp/kaidoku-r3-doctor.json` scratch was selectively deleted mid-audit by external /tmp churn; all values had been extracted.
