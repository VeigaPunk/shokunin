# kaidoku-r4 lane 04 — CONSISTENCY audit (round-4)

Scope: cross-file consistency of README index, r3 errata, PROVINCE, QUALITY
criteria 10–11 application, SKILL tables, and LOG-vs-commit 8f89dbd. Read-only
audit; verify commands re-run where cheap (`command -v`, config line reads,
git diffs). No repo files touched.

## corpus/README.md

- PASS: Knowledge table ↔ files is exact 1:1 — 38 rows ↔ 38 files in
  `corpus/knowledge/` (diff of sorted backtick names vs `ls` output is empty).
  Note: the round-4 dispatch said "39 knowledge"; actual is 38 (14 r1 + 12 r2
  + 12 r3). README is internally consistent — the 39 expectation is off, not
  the file.
- PASS: Lessons table ↔ files 1:1 — 3 rows ↔ `2026-10-13-round-{1,2,3}.md`.
- PASS: Coverage map references — every entry name in all 19 coverage rows
  resolves to an existing knowledge file, and every one of the 38 files
  appears in at least one coverage row (both `comm` directions empty).
- PASS: Coverage-map states match reality — "resolved" host anomaly triage is
  backed by `r3-jq-provenance` (kimi swarm agent-2, 2026-10-03); "frontier"
  firmware matches `r2-firmware-probe` + live `command -v binwalk unblob`
  → absent; "mechanism held (32 MiB cap)" crashes matches
  `r2-crash-inspect-probe:22`; "surveyed — narrow" managed matches the AnyCPU
  rejection; "18 ops, 8 available" matches `r2-provider-capability-matrix:24-26`;
  all r3 "held" rows (EVM, runtime-obs, synth carriers, APK, verb families)
  match their entries' admitted claims.
- PASS: Frontier / Known-gaps sections consistent with corpus (bytenode `.jsc`
  gap from typora, `REA_WAKARU_COMMAND`, 32MiB cap, partial-pairing rule,
  stale-skill explanation).

## Errata (round 3) blocks

- PASS: `2026-10-13-r2-jq-shadow-verdict.md:223` — corrects the real claim at
  lines 75–77 (`search --kind procedures` "returns 0 rows for any pattern");
  corrected mechanism + criterion-5 labeling erratum + provenance closure all
  recorded in-file.
- PASS: `2026-10-13-r2-provider-capability-matrix.md:127` — corrects the real
  claim at lines 96–103/123 (`capability_unavailable` "fail (exit 0)");
  verbatim re-runs exit 1, `retryable` is the true differentiator; second
  bullet confirms `record_pairs` MCP-only via `dist/` grep.
- PASS: `2026-10-13-r2-firmware-probe.md:107` — corrects the real defective
  verify at line 67 (`providers --format json | grep -i firmware` matches
  embedded catalog tags); replacement verify cites `capabilities[]` filter.
- PASS: `2026-10-13-r2-version-diff-compare.md:223` — host-surface erratum is
  accurate: pre-commit README said "8-dim function compare on CLI" and
  PROVINCE said "compare_functions (8 typed dims, CLI)"; commit 8f89dbd
  corrects both ("no CLI verb"); partial-pairing rule added matches
  `r3-mcp-session` run-log rows 15/18.
- PASS: Exactly 4 `## Errata (round 3)` blocks exist, one per file —
  matches LOG.md's "4 errata appended" and the named list (jq-shadow
  mechanism, capability_unavailable exit code, firmware verify,
  compare_functions attribution).

## PROVINCE.md

- PASS: All r3 Core promotions are corpus-backed — Runtime observation
  (r3-05→`r3-runtime-observation`), EVM (r3-07→`r3-evm-interface`), synth
  carriers (r3-13→`r3-keyed-archive-carriers`), APK (r3-06→`r3-apk-inventory`),
  `.node` (r3-11→`r3-node-addons`), MCP session (r3-14→`r3-mcp-session`),
  Verb families (r3-15→`r3-verb-coverage`), PE ARM64 frontier bullet
  (r3-08→`r3-pe-arm64`). Lane numbers verified against
  `.ufo/waves/kaidoku-r3/` staging filenames.
- PASS: Drift value `~/.kimi-code/config.toml:1284` verified live — line 1284
  is `[mcp_servers.rea]` (the commit corrected 1285→1284).
- PASS: Frontier items still genuinely unprobed — `command -v binwalk unblob
  jadx apktool pwntools ilspycmd` all absent this host; runtime-obs extended
  verbs (`observe-web-session`, `observe-web-execution`,
  `list/observe-javascript-runtime`, `capture-electron-scenario`,
  `reconcile_javascript_runtime`) are absent from `r3-runtime-observation`'s
  exercised set; `compare_javascript_export_shapes` never ran in
  `r3-mcp-session` (only `compare_bundles`); EVM real-bytecode frontier is
  named by `r3-evm-interface` itself; macOS surfaces correctly stay
  `unsupported_host` records.
- FAIL: `PROVINCE.md:39` stale claim — Core row "Electron/ASAR/JavaScript"
  still says "6 asar archives on host (obsidian ×2, signal, 1Password,
  electron39/43 stubs)". `r3-typora-signal` widened the census: typora adds 3
  archives (`app.asar`/`lib.asar`/`node_modules.asar` under
  `/usr/share/typora`) → ≥9 host-wide, and the corpus entry states r1's
  "6 archives" was root-scoped, not host-complete. The README coverage row was
  updated for typora; the PROVINCE row was not.

## corpus/QUALITY.md — criteria 10-11 applied to 4 r3 entries

- PASS: `r3-keyed-archive-carriers` — criterion 10: every "WORKS" verdict is
  post-carrier-run with `ev_` ids (`ev_0524ef94…`, `ev_4fd60561…`,
  `ev_33de3850…`) and explicitly frames `available:true` as declared-vs-proven
  (lines 12, 43, 70); `inspect_plist` refusal kept. Criterion 11: n/a — no
  zero-findings claimed; `undetermined` semantics explained mechanistically.
- PASS: `r3-evm-interface` — criterion 10: "held" claimed only after three
  synthesized carriers ran (`ev_6159275a…`, `ev_6cc06a1e…`, `ev_a428ec89…`).
  Criterion 11: empty `functions:[]` labeled honest-empty on dispatch-less
  bytecode with `discovery_completeness:"unknown"` quoted; `kind:"unknown"`
  recorded as no-inference, not failure.
- PASS: `r3-mcp-session` — criterion 10: every "admit" backed by numbered
  run-log rows + verdict `ev_367db735…`; the retention-pinning mechanism is
  flagged "(partly inference)"/"inference — flagged, testable" (lines 94,
  111-113). Criterion 11: `unresolved:N`/`status:unknown` outcomes explained
  by the all-members-paired mechanism, not presented as absence.
- PASS: `r3-typora-signal` — criterion 10: analyze claim runs RC=0 with
  `ev_184ef0ac…` and sha256 pin. Criterion 11: exemplary (it is the criterion's
  lesson source) — `parse_failures:0` explicitly classed as a pre-parse
  inventory exclusion; all-zero IPC scoped to 0.42% byte coverage (line 41).
- PASS (bonus spot-check): `r3-renderer-asar:45` — `explicit_web_preferences:0`
  annotated "0 statically resolved, not 0 present" — criterion 11 compliant.

## SKILL.md

- PASS: `Unknown flag` row — positional-arg list "(evm encoding,
  keyed-archive `archive`, addresses)" matches corpus 1:1:
  `r3-evm-interface:93-96` (`Unknown flag: --encoding`),
  `r3-keyed-archive-carriers:22-26` (`Unknown flag: --archive`),
  `r3-verb-coverage:88-89,189` (`Unknown flag: --address` on
  read-bytes/address-to-file-offset).
- PASS: `out_of_range` row — "32 MiB crash" matches
  `r2-crash-inspect-probe:22` (33,554,432-byte cap); "16 MiB EVM file"
  matches `r3-evm-interface:126` (16 MiB file cap).
- FAIL: `unsupported_target` row misfiles ">32MiB core" as a wrong-carrier
  example — corpus taxonomy (`r2-crash-inspect-probe:29,33`) assigns >32 MiB
  → `invalid_request`/`out_of_range` and reserves `unsupported_target` for
  wrong file type (ET_EXEC "requires x86-64 ET_CORE"). Same "32 MiB crash"
  fact is correctly listed two rows down under `out_of_range` — the row both
  duplicates and misattributes. Other row members verified: plain plist
  (`r3-keyed-archive:34`), ELF→`extract-artifact` (`r3-appimage:25,35`),
  `binary_overview`→paging (`r3-mcp-session:29`).
- PASS: decision-table spot checks — positional EVM encoding, +0x100000
  rebase (`.so` AND `.node`), AppImage "`extract-artifact` has no ELF
  reader", `record_pairs` all-members-paired, "jq-shadow … do not re-flag"
  all match corpus.

## LOG.md (round-3 entry vs commit 8f89dbd)

- PASS: "4 errata appended" with the four named subjects — all landed (above).
- PASS: "12 new knowledge entries" — commit adds exactly 12 new
  `corpus/knowledge/2026-10-13-r3-*.md` files.
- PASS: "16 lanes" — `.ufo/waves/kaidoku-r3/` holds 01–16.
- PASS: "all SHONEN.md gates now closed" — diff ticks the last checkbox.
- PASS: headline claims verified — jq-shadow provenance resolved
  (r3-jq-provenance), obsidian.asar 45 ipcMain ops (r3-renderer-asar:107),
  content-addressed ev ids across sessions (r3-mcp-session row 16).
- FAIL (minor, omission not fabrication): the entry's "Promoted to Core" list
  omits the **Verb families** Core row (PROVINCE diff adds it, r3-15), and the
  commit's `corpus/QUALITY.md` growth — admission criteria 10 and 11, a
  governance change per AGENTS.md's log-every-change rule — is not mentioned
  anywhere in the LOG entry ("index/province fixes" covers README/PROVINCE
  only).

## Summary

| # | severity | file | finding |
|---|---|---|---|
| 1 | FAIL | PROVINCE.md:39 | Stale "6 asar archives on host" — r3-typora census widened host count to ≥9 (typora app/lib/node_modules added); corpus entry itself flags r1's count as root-scoped. |
| 2 | FAIL | SKILL.md error-patterns `unsupported_target` row | ">32MiB core" misfiled as wrong-carrier; corpus assigns it `invalid_request`/`out_of_range` (already correctly in the `out_of_range` row). |
| 3 | FAIL (minor) | LOG.md round-3 entry | Under-records commit 8f89dbd: Verb-families Core promotion and QUALITY.md criteria 10–11 additions unlogged. |

All other checks pass: README row↔file is exact 1:1 (38+3; dispatch's "39"
was off, README is self-consistent), all 4 r3 errata landed in the right
files correcting claims that exist there, all PROVINCE r3 promotions are
corpus-backed with correct lane numbers, frontier items remain genuinely
unprobed (verified against live `command -v`), and the four audited r3
entries comply with QUALITY criteria 10–11.
