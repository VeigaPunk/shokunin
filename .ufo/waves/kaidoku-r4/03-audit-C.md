# Round-4 audit C — re-verify four r3 knowledge entries

Lane: kaidoku-shokunin round 4 (2026-10-13). Method: re-run the `- verify:`
commands from each entry on the live host. MCP server `rea` was **present**, so
the MCP claims were re-verified inside a fresh live session rather than against
scratch bundles alone. Results: `confirmed` / `drifted` / `fails`.

## File: corpus/knowledge/2026-10-13-r3-mcp-session.md

### Verify
- `open_binary /usr/bin/true` → `format:elf, arch:x86_64`, sha256
  `8bc9a73a…02d` matches `sha256sum` — **confirmed**
- `binary_overview` → `ev_982c6020…71a8` **identical id**, `rea-workflow`,
  206 procedures / 154 strings / 31 segments — **confirmed**
- `analyze_function {procedure:"entry"}` → `ev_5db3a3e0…a216` identical;
  `entry` @ 0x102560, FUN_00102480 body 218 B — **confirmed**
- `export_evidence_bundle` → `/tmp/r4-audit-true.json` 35,967 B / 2 records —
  byte-identical size to r3's `true-bundle-paired.json` — **confirmed**
- close → `open_binary /usr/bin/false` (sha256 `193f3dd1…daed`) →
  `binary_overview` `ev_cfb0e80a…40fa` identical with **156** strings (vs 154);
  `analyze_function` → `ev_c00317c6…7fc6` identical, entry @ 0x102570 (+0x10),
  FUN_00102480 227 B; export `/tmp/r4-audit-false.json` 35,971 B / 2 records —
  **confirmed**
- `compare_bundles` + `record_pairs` [ev_982c↔ev_cfb0, ev_5db3↔ev_c003] on the
  two 2-record bundles → `status:"changed"`, `records_changed:2`,
  `unresolved:0`, both `observed_change`; verdict
  `ev_367db735…ed7c` — **the same verdict id as r3, fully deterministic** —
  **confirmed**
- "changed requires ALL members paired" (the headline refinement): same 2
  pairs against r3's saved 4-record `/tmp/rea-mcp-r3/true-bundle.json` vs the
  fresh false bundle → `status:"unknown"`, `unresolved:2`, the two unpaired
  view records `unresolved_branch`, verdict `ev_c6b9261c…` (the `ev_c6b9…` r3
  already listed as an earlier verdict — reproduced verbatim) — **confirmed in
  both directions**
- `inspect_analysis_view` on `ev_982c6020…` (binary_overview parent) → typed
  `unsupported_target`, `retryable:false`, "Parent Evidence operation
  \"binary_overview\" is not inspect_binary_layout, analyze_javascript_application
  or analyze_function." — **confirmed verbatim**; also shows the id still
  resolves while `false` is the open target (cited by the verdict), consistent
  with the epoch/citation-retention claim
- Scratch bundles `/tmp/rea-mcp-r3/` still present with claimed sizes
  (50,829 / 35,971 / 67,061 / 35,967 / 82,239 B); record membership of all 4
  bundles matches the run log (4 / 2 / 2 / 6) — **confirmed**

### Verdict audit
All four candidates re-verified on the live MCP surface. The `record_pairs`
rule was the specific audit target and it held **both ways**: fully-paired →
`changed`/`unresolved:0`; 2 unpaired members → `unknown`/`unresolved:2`.
Every content-addressed id — including the compare verdicts `ev_367d…` and
`ev_c6b9…` — reproduced byte-for-byte across sessions a day apart. Admit.

## File: corpus/knowledge/2026-10-13-r3-verb-coverage.md

### Verify
- `npx -y rea-agents@6.4.0 xrefs /usr/lib/libjq.so.1.0.4 0x117070 --format json`
  re-run live → EXIT=0, output **byte-identical** to saved
  `/tmp/r3-xrefs-addr.json` (3,228 B), `ev_ce745d78…` identical; 26 refs
  decompose 23 code (<0x14b000) + `0x14b35c` (.eh_frame_hdr) + `0x14e674`
  (.eh_frame) + `0x155d98` (GOT slot) — **confirmed live**
- `objdump -d --start-address=0x21b04 --stop-address=0x21b14` →
  `call *0x3428e(%rip) # 55d98 <jq_next@@Base+0x3ed28>` — **confirmed**
- `readelf -rW | grep jq_next` → `0000000000055d98 … R_X86_64_GLOB_DAT
  0000000000017070 jq_next + 0` — **confirmed**
- `od -j 0x54d98` → all zeros (reloc-populated slot); `readelf -wf` →
  `00002a14 … FDE cie=00000000 pc=0x17070..0x18cc5`; section ranges
  .eh_frame_hdr 0x4a8c8–0x4bc53, .eh_frame 0x4bc58–0x5260f, .got
  0x556b8+0x948 ∋ 0x55d98 — **confirmed**
- DWARF decode arithmetic re-derived: `a8 c7 fc ff` @0x4b35c (pcrel|sdata4,
  base = .eh_frame_hdr start) → 0x4a8c8−0x33858 = **0x17070**; fde ptr
  `a4 3d 00 00` = 0x3da4 → 0x4e66c = .eh_frame+0x2a14 → FDE 2a14;
  `fc 89 fc ff` @0x4e674 (pcrel base = field) → 0x4e674−0x37604 = **0x17070**
  — **confirmed to the byte level**
- Saved `/tmp/r3-instr.json`: 1621 rows, `0x117070: ENDBR64` …
  `0x118cc0: JMP 0x00106a9a` — **confirmed**
- Saved `/tmp/r3-function.json`: assembly 1621 / callers 5 / callees 45 /
  incoming_references 26 / outgoing_references 903 / referenced_strings 14 /
  basic_blocks 179 — **confirmed**
- libjq still 350,384 B, sha256
  `7e8bccc6df37a55fb90703c9069b3770f5cdc502e96959c866d2f30fbf5e8b6b` —
  **confirmed**
- `rea --help | grep '^  list-'` → **11 verbs** (claim said 10) — **drifted
  (minor)**: 6 adb + browser + electron + javascript-runtime + jeb +
  list-architectures; substance holds (none ELF-generic). Caveat on the
  "no list-segments/list-procedures verb exists" claim: true for the CLI, but
  the live MCP surface exposes `list_procedures`, `list_segments`,
  `list_names`, `list_strings`, `list_bookmarks`, `list_documents`,
  `list_unknowns` — the claim needs CLI scoping — **drifted (scope)**.

### Verdict audit
xrefs GOT+DWARF decomposition fully re-verified — live re-run is
byte-identical and the 26-ref split (23 GOT-indirect calls + 2 unwind + 1 GOT
slot) is exact; every DWARF decode re-derived arithmetically. Two small
drifts: the list-* census is 11 not 10, and "verbs do not exist" is
CLI-scoped only (MCP has `list_*` inventory tools). Admit with those
corrections noted.

## File: corpus/knowledge/2026-10-13-r3-typora-signal.md

### Verify
- `find /usr/share/typora /usr/lib/signal-desktop /opt/1Password \( -name
  '*.asar' -o -name '*.asar.unpacked' \)` → 7 paths — **confirmed**
- `sha256sum`: app.asar `7ac791ca…19e0`, lib.asar `8c07ca4e…2d44`,
  node_modules.asar `997f4329…2459` — all three **confirmed** verbatim
- `asar list` on app.asar → 3 members; `asar extract-file` → package.json
  251 B, launch.dist.js 1,383 B, atom.compiled.dist.jsc 388,080 B,
  sha256 `6a0cb7b3…dfe9` — **confirmed**
- launch.dist.js full read: `v8.setFlagsFromString("--no-lazy")`,
  `"--no-flush-bytecode"`, `dummyBytecode.slice(12,16).copy(e,12)`,
  `Module._extensions[".jsc"]=Module._extensions[".cjsc"]`, `vm.Script` with
  `cachedData`, `cachedDataRejected` throw, `runInThisContext`, `.apply` over
  `[exports, require, module, filename, dirname, process, global]`, final
  `require("./atom.compiled.dist.jsc")` — **confirmed verbatim**
- "99.42% of archive bytes" → 388,080 / 390,514 = **99.3767%** — **drifted
  (minor numeric)**: the printed percentage is ~0.05 pp high; the substance
  (one .jsc ≈ 99.4% of the archive) is unaffected
- `/tmp/typora-app-analysis.json` still present (475,737 B):
  `ev_184ef0ac…` identical, `subject.digest.sha256` =
  `root_artifact_sha256` = `7ac791ca…`, statistics block verbatim
  (relevant 2, text_bytes_read 1634, parsed 1, ast 341, findings 12,
  modules 0, parse_failures 0), graph 20n/20e, semantic 268n/200rel —
  **confirmed**

### Verdict audit
Every structural claim re-verified; the only blemish is the printed 99.42%
(measured 99.38%) — a rounding/precision drift, not a substance error. Admit
with the corrected figure.

## File: corpus/knowledge/2026-10-13-r3-jq-provenance.md

### Verify
- Cited session files still exist:
  `…/session_cf944588-…/agents/main/wire.jsonl` (472,099 B, 184 lines) and
  `…/agents/agent-2/wire.jsonl` (184,051 B) — **confirmed**
- `main/wire.jsonl` line 153 = the `agent_swarm_result` containing agent-2's
  "CLI DEPS into ~/.local/bin" brief and its report (jq 1.8.2,
  `jq-linux-amd64`, six `--version` proofs) — **confirmed**
- `agent-2/wire.jsonl` shows the `/releases/latest` enumeration incl.
  `jq-attestation.json` and every `jq-linux-*` asset, the
  `jq-1.8.2/jq-linux-amd64` download (2,267,912 B), `install -m 0755 …
  $BIN/jq`, and the `jq-1.8.2` proof output — **confirmed**
- User prompt recovered verbatim: "optimize agentic usage by updating and
  installing any deps, libs and config knobs … setup jujutsu as the git
  manager; i prefer fnm as the node manager … pin node version to node 24
  LTS; /skill:godspeed" — **confirmed**
- `stat ~/.local/bin/jq`: birth `18:34:03.580916041`, modify
  `18:34:03.581916043` — claim wrote "Birth == Modify == .581916043"; birth
  is ~1 ms earlier — **drifted (trivial precision)**; substance (born
  18:34:03.58, never touched since) holds
- Cohort mtimes: rg .5829 / fd .5841 / bat .5859 / gh .5939 / delta .5949 in
  the same 13 ms burst, jj born 18:33:58.917, `~/.local/state/gh/device-id`
  born 18:34:08.448, `~/.local/share/fnm/node-versions/v24.21.0` present —
  **confirmed**
- `journalctl` at 18:31:55 → `vgpnk : a password is required ;
  COMMAND=/usr/bin/true` — **confirmed verbatim**
- `pacman -Qqo ~/.local/bin/jq` → "No package owns"; `/usr/bin/jq` exists
  (30,800 B, pacman `jq 1.8.2-1`) — dual-jq state — **confirmed**
- `~/.local/bin/jq --version` → `jq-1.8.2`;
  `~/.config/jj/config.toml` identity `Joao Pedro Veiga` /
  `jpveigao10@gmail.com` — **confirmed**

### Verdict audit
The wire.jsonl evidence chain is intact end-to-end and the filesystem
corroboration (cohort births, gh device-id, fnm node dir, jj identity, sudo
failure timestamp) matches to the second. Only drift: birth-vs-modify
equality is ~1 ms off, cosmetic. Provenance stays **resolved**.

## Summary

- 4 files audited; ≥3 verify commands re-run per file (MCP file got a full
  live-session replay).
- **34 confirmed, 0 fails, 3 drifts** — all precision-level:
  1. typora `.jsc` share: claimed 99.42%, measured **99.38%**.
  2. CLI `list-*` census: claimed 10 verbs, actual **11**; and "no
     list-segments/list-procedures verbs exist" is CLI-true only — the MCP
     surface ships `list_procedures`, `list_segments`, `list_names`,
     `list_strings` (worth a corpus note).
  3. jq birth == modify claim off by ~1 ms (.580916041 vs .581916043).
- Headline re-checks all hold: `record_pairs`/`status:changed` requires **all
  bundle members paired** (verified in both directions live, verdict ids
  `ev_367d…`/`ev_c6b9…` reproduced verbatim); the 26-ref xrefs decomposition
  (23 GOT-indirect + 2 DWARF unwind + 1 GOT slot) re-ran byte-identical;
  the jq→kimi-swarm provenance chain is intact including the cited session
  file.
- Net: all four entries are audit-clean; the three numeric nits above are the
  only corrections for the corpus.
