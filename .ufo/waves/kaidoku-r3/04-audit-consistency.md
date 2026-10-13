# kaidoku-r3 — 04 — CONSISTENCY audit (round-2 consistency lane)

Audit date: 2026-10-13. Scope: `corpus/README.md` row↔file 1:1 + coverage-map
states, `## Errata (round 2)` blocks in the 8 r1 files, `PROVINCE.md` r2-backed
Core rows / frontier freshness / drift-prone pins, `corpus/QUALITY.md` criteria
4–9 applied to 4 new r2 entries, `LOG.md` round-2 entry vs commit `5f1d4dd`.
Live spot-checks: `rea --help` compare verbs, kimi `config.toml` lines,
coredumpctl/journal, `.unpacked` natives, Ghidra dir, JDK.

## corpus/README.md

- FAIL: Knowledge row `2026-10-13-r2-doctor-reverify` (line 58) resolves to no
  file — the on-disk entry is `corpus/knowledge/2026-10-13-r2-doctor-reverify-r2.md`
  (filename carries a redundant `-r2` suffix). Mechanical cross-check of all
  backticked slugs vs `corpus/knowledge/*.md` confirms this is the only break in
  the 26-row table; every other Knowledge row resolves 1:1, and both Lessons
  rows (`round-1`, `round-2`) resolve to `corpus/lessons/` files.
- FAIL: Coverage map "Cross-version diff" state claims "8-dim function compare
  **on CLI**". Live `npx -y rea-agents@6.4.0 --help` shows the 8 `compare-*`
  CLI verbs (`compare`, `compare-application-versions`,
  `compare-javascript-export-shapes`, `compare-managed-members`,
  `compare-process-captures`, `compare-source-to-bundle`, `compare-web-captures`,
  `compare-web-screenshots`) — **no `compare-functions` CLI verb exists**. The
  8-dim compare was exercised via `node --input-type=module` domain calls
  (`r2-version-diff-compare` run log rows 16–21). The "`record_pairs` MCP-only"
  half of the state is accurate.
- FAIL (minor): Coverage map omits 4 admitted knowledge files entirely —
  `r2-jq-shadow-verdict`, `r2-doctor-reverify-r2`, `r2-skill-references-deep`,
  `r2-libjq-engine`. The r1 audit invariant was "every knowledge file appears
  exactly once"; completeness regressed.
- PASS: Other coverage states match reality — PE held (cli-64.exe e2e, 142
  procedures, deterministic re-run), ASAR held (obsidian app.asar 170-node
  graph, summary→page→item chain demonstrated), crash mechanism held (32 MiB
  cap, `ev_3686f9…`), managed assemblies surveyed (AnyCPU probe → typed
  rejection), firmware/APK/runtime-obs frontier (blocked/unprobed per
  `r2-frontier-prereqs`), provider matrix held (18 host ops, 8 available —
  matches `r2-provider-capability-matrix`).
- PASS (nit): EVM row state "unblocked — no carrier probed" sits outside the
  held/surveyed/frontier vocabulary; substance is correct (frontier/unprobed,
  bundled EVMole WASM per `r2-frontier-prereqs`).

## corpus/knowledge — Errata (round 2) blocks (8 r1 files)

- PASS: All 8 files carry `## Errata (round 2)` and each corrects a claim
  verifiably present in its own file:
  - `ghidra-install`: 35→34 feature modules (targets lines 49–50 claim + 64
    summary; summary still reads "35" — errata-block convention, not a rewrite).
  - `mcp-registrations`: `grep -ni 'mcp\|rea\|ghidra'` verify defect (targets
    line 26) + kimi stanza pin — live-verified: `[mcp_servers.rea]` header at
    `config.toml:1284`, `command` at :1285, `startup_timeout_sec` at :1287,
    env vars at :1290–1291. Erratum is exactly right.
  - `doctor-taxonomy`: `decompile -v` produces no output; verify line at 51 is
    the target. Correct.
  - `elf-observation-jq`: "full RELRO unverified" resolved — targets the
    explicit deferral at lines 150–153; raw-note slips target the predicted
    `grep -c symtab → 1` (lines 78–80) and `x86 feature used` transcription
    (line 146). Correct.
  - `pe-surface`: "end-to-end import inferred" → PROVEN (targets line 73;
    points at `r2-pe-e2e-proof`). Correct.
  - `rea-live-jq-e2e`: `/tmp/rea-jq.snap.json` reboot loss + `FUN_00103fa0 =
    process()` flagged as unlabeled decompiler inference — the exact
    criterion-5 violation the r2 consistency audit cited (lines 54, 96, 74–75).
    Correct.
- FAIL (minor): `crash-evidence` erratum asserts "Core corpus unchanged: still
  175 entries / 174 present / same 133/39/3 split" — but sibling entry
  `r2-crash-inspect-probe` run log records `coredumpctl list → 176 entries`
  the same day. Unqualified cross-entry contradiction; plausibly intra-round
  drift (live list already shows fresh node SIGABRT cores at 12:46–12:47,
  post-commit) but the corpus carries both numbers with no time-stamp note.
- PASS (nit): `asar-surface` erratum (`.unpacked` larger than claimed) is
  verified live — `signal-desktop` ships 4 `.node` natives
  (libsignal-client/ringrtc/sqlcipher/xattr), `1Password` ships `index.node`.
  The correction is true; the literal "index.node" naming fits only
  1Password — signal's natives carry different names.

## PROVINCE.md

- PASS: Core rows for PE and crash-mechanism are backed by r2 corpus entries —
  "Native PE via Ghidra" cites cli-64.exe sha256 `bbb3de57…`, 8 segments/142
  procedures, deterministic re-run (`r2-pe-e2e-proof`); "Recorded crashes
  (mechanism)" cites crash-godot core → `ev_3686f9…`, 27 regs, 32 MiB cap
  (`r2-crash-inspect-probe`). Both accurate.
- FAIL: Core row "Cross-version compare" claims "`compare_functions` (8 typed
  dims, **CLI**)" — no `compare-functions` CLI verb exists (live `--help`
  verified, above); the 8-dim diff ran only as MCP-tool-name / direct domain
  calls. The `record_pairs`-MCP-only clause is right; the CLI tag is not.
- FAIL (minor): Drift-prone pin `~/.kimi-code/config.toml:1285` retains the
  pre-erratum line number — the landed mcp-registrations erratum establishes
  the stanza header at `:1284` (:1285 is the `command` line). Verified live.
- FAIL (minor): Frontier bullet "Android APK" claims "archive inventory of an
  APK is already Core via `inspect_artifact`" — no `inspect_artifact` e2e run
  exists anywhere in the corpus (only `available:true` declarations);
  `r2-frontier-prereqs` itself proposes that exact call as the round-3 probe
  ("inventory leg open now"). Held-status overclaim.
- FAIL (minor): Frontier bullet "Cross-version diffing" is stale — states the
  three ops are "catalog-listed; needs a two-version artifact pair", but r2
  already used the `1password-cli` 2.34.1↔2.40.0 pair (domain `compareBundles`
  with `record_pairs` → `status:changed`, `observed_change`) and probe-refused
  `compare-application-versions` on native records (JS-graph-only). Frontier
  status survives (no MCP-session run, no JS pair) but the stated reason is
  wrong.
- PASS: Remaining frontier items still genuinely unprobed — PE ARM64/managed
  (only x86-64 exercised e2e), managed AnyCPU (still rejected), firmware
  (`REA_BINWALK_COMMAND` gated per `r2-firmware-probe`), crashes >32 MiB
  (cap-bound), offline ELF layout (pwntools env unset; uv recipe documented
  not persisted), alternate providers (JEB absent, port 8425 closed), runtime
  observation (zero CDP endpoints), macOS ops (`unsupported_host` re-confirmed
  live), EVM (unblocked, no carrier).
- PASS: Other drift-prone values verified live — Ghidra `12.1.4` install dir
  present, JDK `21.0.12.1`, env wiring at kimi `config.toml:1290–1291`
  (matches `r2-doctor-reverify-r2`), `rea-agents@6.4.0` pin, 170-tools/127-
  commands counts, `tools_sha256 25802f6d…`.

## corpus/QUALITY.md — criteria 4–9 on 4 new r2 entries

Scope: the 4 entries backing the new Core rows + headline (`r2-pe-e2e-proof`,
`r2-crash-inspect-probe`, `r2-version-diff-compare`, `r2-jq-shadow-verdict`).

- PASS `r2-pe-e2e-proof`: c4 absolute path + full sha256; c5 labels "OBSERVED
  end-to-end" (nit: "MSVC `entry` stub" identification asserted flatly);
  c6 exact verify calls (nit: determinism claimed but literal `evidence_id`
  never printed); c7 names unexercised PE subtypes; c8 pins 6.4.0/12.1.4;
  c9 no runtime-behavior claims. Compliant.
- PASS `r2-crash-inspect-probe`: c4 resolvable identity via coredumpctl
  PID + size + comm (nit: the core's own sha256 never quoted — envelope is
  said to carry "sha256'd subject"); c6 full `ev_3686f9…` + reproducing call;
  c7 `limitations[7]` + explicit frontier split; c8 pwntools stack pinned;
  c9 recorded-crash provenance correct. Compliant.
- PASS (minor flags) `r2-version-diff-compare`: c4 — six target sha256s
  truncated to 8-hex prefixes (pkg name+version+pkgrel identity path covers
  the criterion; truncation previously tolerated as host-unique); c5 nit —
  `FUN_00102080` named "(main, LEA target in `entry`)" unlabeled inference;
  c6 multiple `ev_*` ids + dist/ source lines; c7 names untested dossier
  scale; c8 pins; c9 n/a. Compliant with nits.
- FAIL `r2-jq-shadow-verdict` (criterion 5): Candidate 5 maps
  `FUN_00492360`=`__libc_start_main`, `FUN_00407130`=`jq_init`,
  `FUN_00423540`=`jq_util_input_init`, `FUN_00403e10`=process loop etc. as
  flat `=` identifications — decompiler-derived inference asserted as fact,
  the same class recorded as erratum-worthy in r1. Partially mitigated by the
  explicit "Unknown:" section and by the sha256 identity proof (attribution no
  longer rides on the identifications). c4/c6/c7/c8/c9 pass (smoke filter was
  actually executed — runtime claim carries runtime provenance; "anything a
  user script can observe" is a mild generalization bounded by the hash).

## LOG.md

- PASS: Round-2 entry vs commit `5f1d4dd` — "16 lanes" matches 16 wave files
  (`01–12, 14–17`; no lane 13); "4 audit + 12 expansion" per lessons file;
  "~100 verify commands re-run" and "all admit/reject verdicts upheld" match
  the audit reports; "1 factual erratum (34 Ghidra features)", "2
  verify-command defects" (mcp grep, `decompile -v`), "criterion-5 labeling
  gap" all have landed errata; Core promotions and the jq-shadow headline are
  in PROVINCE/corpus; commit touches 24 files = 12 new r2 knowledge + 1
  lessons + 8 errata-carrying r1 files + README/PROVINCE/LOG.
- FAIL: The r2 consistency audit prescribed corrections to the round-1 LOG
  entry that never landed — it still claims "evidence_id-bearing output" for
  the jq run (unevidenced), still groups firmware regions under
  "probed-not-held" (r1 only catalog-listed it), and the `SHONEN.md` change in
  `a43d442` remains unrecorded despite AGENTS.md requiring every change
  logged.
- FAIL (minor): Round-2 entry records no admission count — 12 new knowledge
  entries + 1 lessons file were committed but uncounted (round-1 entry counted
  "14 knowledge entries admitted"). Also "1 factual erratum" undercounts if
  the kimi-stanza line fix is classed factual — the errata blocks carry ≥2
  factual corrections (34 features; 1284/1287 line pins) plus raw-note
  transcription fixes (symtab count, property-note name).

## Summary

FAILs and required errata:

1. **README broken row** — `2026-10-13-r2-doctor-reverify` → file is
   `…-doctor-reverify-r2.md`. Erratum: rename the file (drop the doubled
   `-r2`) or fix the row slug.
2. **README + PROVINCE "on CLI" misattribution** — `compare_functions` is not
   a CLI verb (live `--help`: no such command; 8-dim compare ran via domain
   calls). Erratum: both index files should read "8-dim function compare via
   MCP `compare_functions` / domain call", keeping "`record_pairs` MCP-only".
3. **PROVINCE stale pin** — `config.toml:1285` → stanza header `:1284` per the
   landed erratum (live-verified).
4. **PROVINCE frontier overclaims** — "archive inventory of an APK is already
   Core via `inspect_artifact`" (no `inspect_artifact` run exists; r2 itself
   schedules it as the r3 probe); "Cross-version diffing" bullet's stated
   reason ("needs a pair") is stale — the 1password pair was already compared
   and `compare-application-versions` was probe-refused.
5. **QUALITY c5 on `r2-jq-shadow-verdict`** — FUN_*→named-function
   identifications asserted without inference labels (same class as the r1
   `FUN_00103fa0` violation).
6. **LOG unlanded r1 corrections** — the r2 audit's prescribed LOG errata
   (SHONEN touch, "evidence_id-bearing" overclaim, firmware "probed-not-held"
   grouping) never landed.
7. **Crash-corpus count conflict** — erratum "still 175" vs sibling entry's
   "176 entries" same day; needs a time-qualified note.
8. Minor (non-blocking): coverage map drops 4 admitted files
   (jq-shadow-verdict, doctor-reverify-r2, skill-references-deep,
   libjq-engine); LOG omits the round-2 admission count (12) and arguably a
   2nd factual erratum (kimi pin); EVM state label "unblocked" sits outside
   the held/surveyed/frontier vocabulary; `version-diff-compare` truncates
   sha256s to 8 hex; asar erratum's literal "index.node" naming fits only
   1Password (signal natives are named differently — substance true).
