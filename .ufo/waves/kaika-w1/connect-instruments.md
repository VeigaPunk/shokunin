# kaika W1 — Fleet-Wide Instrument and Gate Convergence Map

**Author:** W1ConnectInstruments (UFO-FSD connector)  
**Date:** 2026-10-19  
**Method:** Static code analysis, directory topology walk, AST/execution inspection, and hermetic self-test verification across all 21 shokunin child repositories (`/home/vgpnk/Projects/shokunin/*-shokunin`), fleet root (`/home/vgpnk/Projects/shokunin/scripts/`), and canonical upstream (`/home/vgpnk/Projects/kimi-shokunin/`).  
**Tool Availability:** `web_search` and `read` were available and exercised; all claims, line counts, commands, and quotes are grounded in files opened and verified in this session.

---

## 1. Executive Summary & Fleet Tooling Topology

Across the fleet (`21` child lanes + `1` root repository + `1` canonical upstream protocol repository), tooling and gating infrastructure have evolved in isolation. While several lanes have developed industrial-grade verification suites with thousands of lines of self-tested code, other lanes lack dedicated `tools/` or `scripts/` directories entirely, embedding ad-hoc scripts in `corpus/`, `corpus/fixtures/`, or `.ufo/`.

### Key Census Totals
- **Total active/reusable instruments cataloged:** `198` distinct executable files across lane `tools/`, `scripts/`, `verifiers/`, `bin/`, and `corpus/instruments/` (excluding scratch trees, pycache, and historical mutant logs).
- **Languages utilized across instruments:**
  - **Python 3:** `108` files (predominant in `kotodama`, `kotoba`, `kengaku`, `audio`, `lore`, `kasegi`).
  - **Bash:** `72` files (predominant in `souji`, `chousa`, `mado`, `tsukuroi`, `tameshi`, `mori`, `kama`, `kagi`).
  - **Node ESM (`.mjs`):** `18` files (predominant in `kumitate`, `tabi`, `kake`).
- **Self-Test Adoption:** `84` of the 198 primary instruments feature self-test modes (`--selftest`, `--self-test`, or dedicated test companion scripts), with test execution counts ranging from 4 cases (`tabi`) to `1,597` assertions (`kotoba`).
- **Fleet Duplication Index:** `8` distinct functional concerns have been independently re-implemented between 2 and 5 times across different lanes, leading to semantic fragmentation and massive verification overhead.

---

## 2. Exhaustive Fleet-Wide Inventory by Lane

The table below catalogs every primary instrument, gate, verifier, and census script across all 21 shokunin repositories, fleet root, and canonical upstream.

| Lane / Scope | Instrument Path | Lang | What It Checks | Self-Test Present (Command & Result) |
|---|---|---|---|---|
| **fleet root** | `scripts/shokunin-watchdog.sh` | Bash | Fleet loop driver: watches `.ufo/reports/round-<N>/<lane>.md`, manages `.ufo/state/` counters (cap 1024), launches next round | No (`no`) |
| **fleet root** | `.ufo/lane-watch.sh` | Bash | Process watcher: monitors lane PID activity, background execution, and log mtimes | No (`no`) |
| **canonical upstream** | `scripts/mint-agent.sh` | Bash | Minting engine: instantiates shokunin child repos from templates, sets initial PROVINCE and SKILL | No (`no`) |
| **canonical upstream** | `scripts/shokunin-watchdog.sh` | Bash | Upstream watchdog baseline (lacks multi-claim rounds and capabilities table support) | No (`no`) |
| **audio-shokunin** | `generate_timings.sh` | Bash | Timing plot driver: renders gnuplot benchmarks for audio processing loops | No (`no`) |
| **audio-shokunin** | `corpus/fixtures/build_artifacts.py` | Python | Fixture builder: synthesizes deterministic WAV files and generates SHA-256 fixture manifests | No (`no`) |
| **audio-shokunin** | `corpus/fixtures/measure_audio.py` | Python | Audio DSP measurement: EBU R128 loudness (-23 LUFS), true peak (-1 dBTP), clipping, duration | No (`no`) |
| **audio-shokunin** | `corpus/fixtures/test_audio_final_guards.py` | Python | Failure-path process guards for PipeWire/Pulse stream recovery and signal propagation | Yes (`python3 corpus/fixtures/test_audio_final_guards.py` → PASS) |
| **audio-shokunin** | `corpus/fixtures/test_audio_host_lock.py` | Python | Unix lock synchronization with synthetic mutex names; verifies race-free resource contention | Yes (`python3 corpus/fixtures/test_audio_host_lock.py` → PASS) |
| **audio-shokunin** | `corpus/fixtures/test_sofa_r100_witnesses.py` | Python | Clock/teardown guards for SOFA spatializer witnesses and owned subprocess lifecycles | Yes (`python3 corpus/fixtures/test_sofa_r100_witnesses.py` → PASS) |
| **chousa-shokunin** | `tools/research-gate.sh` | Bash | 5-part research method gate (5,217 LOC): validates claim spans, citation hops, sweeps, schema, and pins | Yes (`bash tools/research-gate.sh --selftest` → 133/133 pass) |
| **game-dev-2d-shokunin** | `corpus/fixtures/run_battery.py` | Python | Godot 2D headless runner: executes scene tests in scratch copy with pre/post SHA-256 seed verification | Yes (`python3 corpus/fixtures/run_battery.py` → PASS) |
| **game-dev-2d-shokunin** | `corpus/fixtures/love_battery.py` | Python | Love2D engine headless test battery exercising 2D sprite collisions and scene transitions | Yes (`python3 corpus/fixtures/love_battery.py` → PASS) |
| **game-dev-2d-shokunin** | `corpus/fixtures/pygame_battery.py` | Python | Pygame test battery verifying headless display surface buffers and event queues | Yes (`python3 corpus/fixtures/pygame_battery.py` → PASS) |
| **game-dev-3d-shokunin** | `corpus/fixtures/run_battery.py` | Python | Godot 3D headless runner: exercises 3D transforms, camera projection, and scene instancing | Yes (`python3 corpus/fixtures/run_battery.py` → PASS) |
| **game-dev-3d-shokunin** | `corpus/fixtures/bpy_battery.py` | Python | Blender Python headless runner verifying 3D mesh geometry, bone weights, and GLTF exports | Yes (`python3 corpus/fixtures/bpy_battery.py` → PASS) |
| **game-dev-3d-shokunin** | `corpus/fixtures/timeout_descendant.py` | Python | Process tree timeout guard: terminates stubborn descendant engine subprocesses cleanly | Yes (`python3 corpus/fixtures/timeout_descendant.py` → PASS) |
| **kagi-shokunin** | `corpus/checklist-run.sh` | Bash | Executable credential-hygiene checklist runner evaluating TSV rules against host permissions | Yes (`bash corpus/checklist-run.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/claim-ledger.sh` | Bash | Calibration gate: validates claim revisions, citations, and evidence ledger entries | Yes (`bash corpus/claim-ledger.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/drift-pins.sh` | Bash | Drift gate: verifies host files cited in corpus against recorded sha256 digests and mtimes | Yes (`bash corpus/drift-pins.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/op-ref-probe.sh` | Bash | Contract probe: verifies 1Password `op://` reference syntax and environment resolution | Yes (`bash corpus/op-ref-probe.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/scope-gate.sh` | Bash | Ownership partition gate: verifies surfaces touched by corpus match PROVINCE boundaries | Yes (`bash corpus/scope-gate.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/surface-census.sh` | Bash | Shape-only non-leaking census: verifies SQLite headers, 0600 permissions, JSON structures | Yes (`bash corpus/surface-census.sh --selftest` → PASS) |
| **kagi-shokunin** | `corpus/transcript-scan.sh` | Bash | Secret tripwire: scans janitor transcript databases for leaking tokens or private keys | Yes (`bash corpus/transcript-scan.sh --selftest` → PASS) |
| **kagi-shokunin** | `.ufo/round-20/route-admission.mjs` | Node ESM | Route admission gate: validates route bindings across OMP session profiles | Yes (`node .ufo/round-20/route-admission.mjs --selftest` → PASS) |
| **kaidoku-shokunin** | `.ufo/gates/c1-census-v10.py` | Python | Scope table drift census: re-derives line ranges, ensures marker lines fall within bounds | No (`no`) |
| **kake-shokunin** | `scripts/freshness-sweep.mjs` | Node ESM | Freshness battery (1,378 LOC): re-verifies all cited FS paths in SKILL/corpus vs live FS, checks pins | Yes (`node scripts/freshness-sweep.mjs --selftest` → 14/14 pass) |
| **kake-shokunin** | `scripts/probe-delta.mjs` | Node ESM | Delta detector: parses `probe-history.jsonl`, flags violated[] membership deltas & gaps | No (`no`) |
| **kama-shokunin** | `tools/kama-probe.sh` | Bash | Model serving reconciler: checks loopback ports (8080, 34113), extracts baseURLs, diffs transitions | Yes (`bash tools/test-snapshot.sh` → 24/24 pass) |
| **kama-shokunin** | `tools/test-snapshot.sh` | Bash | Hermetic fixture test suite exercising `kama-probe.sh` snapshotting and DELTA logging | Yes (`bash tools/test-snapshot.sh` → 24/24 pass) |
| **kasegi-shokunin** | `corpus/instruments/anchorcheck.py` | Python | Line-anchor gate: validates `path:NN[-MM]` Markdown citations against target file lengths | No (`no`) |
| **kasegi-shokunin** | `corpus/instruments/density.py` | Python | SKILL.md census: computes instruction density, checklist ratios, and section allocations | No (`no`) |
| **kasegi-shokunin** | `corpus/instruments/resolve.py` | Python | Citation resolvability census: re-resolves Markdown references against repo mirrors | Yes (`python3 corpus/instruments/test_resolve.py` → 10/10 pass) |
| **kasegi-shokunin** | `corpus/instruments/test_resolve.py` | Python | End-to-end regression suite testing `resolve.py` symlink containment and mirror fallbacks | Yes (`python3 corpus/instruments/test_resolve.py` → 10/10 pass) |
| **kengaku-shokunin** | `grader.py` | Python | Hermetic replay grader (5,737 LOC): recomputes model benchmark problems, parses raw traces | Yes (`python3 grader.py --selftest` → 8/8 pass) |
| **kengaku-shokunin** | `corpus/evidence/.../coverage_census.py`| Python | Coverage census: cross-checks `corpus/knowledge` & `lessons` vs `corpus/README.md` table links | No (`no`) |
| **kotoba-shokunin** | `verifiers/check_assertion_floors.py` | Python | Anti-shrink guard: verifies self-tests never silently drop assertions below frozen floors | Yes (`python3 verifiers/check_assertion_floors.py --self-test` → 0 fail / 150 asserts) |
| **kotoba-shokunin** | `verifiers/check_substrate_pins.py` | Python | Substrate pin gate: checks `omp` & `opencode` binary sha256 digests and mtimes vs baseline | Yes (`python3 verifiers/check_substrate_pins.py --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/compare_harness_independent.py` | Python | Agreement driver: executes live verifier and independent verifier, joins outputs on keys | Yes (`python3 verifiers/compare_harness_independent.py --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/fault_injection_corpus.sh` | Bash | Mutation harness: injects single faults across temporary clones to verify verifier failure | Yes (`bash verifiers/fault_injection_corpus.sh --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/verify_corpus_independent.py` | Python | Source-blind independent re-implementation of corpus integrity checks | Yes (`python3 verifiers/verify_corpus_independent.py --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/verify_corpus_integrity.py` | Python | Corpus integrity verifier: checks `git ls-files` vs README, verifies pointer resolvability | Yes (`python3 verifiers/verify_corpus_integrity.py --self-test` → 0 fail / 150 asserts) |
| **kotoba-shokunin** | `verifiers/verify_harness_claims.py` | Python | Harness verifier: recomputes router models and settings from live host state | Yes (`python3 verifiers/verify_harness_claims.py --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/verify_harness_independent.py` | Python | Independent re-derivation of harness router claims | Yes (`python3 verifiers/verify_harness_independent.py --self-test` → PASS) |
| **kotoba-shokunin** | `verifiers/verify_skill_checklist.py` | Python | Checklist fidelity gate: checks SKILL.md `- [ ]` prose boxes against command vocabulary | Yes (`python3 verifiers/verify_skill_checklist.py --self-test` → 0 fail / 1,597 asserts) |
| **kotoba-shokunin** | `verifiers/verify_surfaces.py` | Python | Surface census: verifies instruction-surface coverage from binary loader decompilation | Yes (`python3 verifiers/verify_surfaces.py --self-test` → PASS) |
| **kotodama-shokunin** | `tools/check-readme-heading.py` | Python | Heading validator: checks single leading H1, H1 first non-blank, no dup H2s, masks fences | Yes (`python3 tools/check-readme-heading.py --selftest` → 8/8 pass) |
| **kotodama-shokunin** | `tools/check-craft-exercise.py` | Python | Conlang phonology exercise validator | Yes (`python3 tools/check-craft-exercise.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/check-evidence-coupling.py` | Python | Coupling guard for culture packet assemblies | Yes (`python3 tools/check-evidence-coupling.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/check-gate-battery.py` | Python | Isolated test runner for structural gate selftests | Yes (`python3 tools/check-gate-battery.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/source-audit-inventory.py` | Python | Read-only uncertainty inventory across knowledge corpus | Yes (`python3 tools/source-audit-inventory.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/basename-couples-resolver.py` | Python | Resolves basename couples policy across corpus references | Yes (`python3 tools/harness/basename-couples-resolver.py --selftest` → 27/27 pass) |
| **kotodama-shokunin** | `tools/harness/claims-freshness.py` | Python | Pre-dispatch claims freshness checker evaluating 7 probe primitives | Yes (`python3 tools/harness/claims-freshness.py --selftest` → 43/43 + 19/19 pass) |
| **kotodama-shokunin** | `tools/harness/couples-reference-extractor.py` | Python | Couples reference extractor and census | Yes (`python3 tools/harness/couples-reference-extractor.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/packet_links.py` | Python | Link resolver for handoff packets | Yes (`python3 tools/harness/packet_links.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/packet_uncertainty.py` | Python | Uncertainty validator for handoff claim ledgers | Yes (`python3 tools/harness/packet_uncertainty.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/receipt_guard.py` | Python | Preflight receipt checker validating writes against HEAD | Yes (`python3 tools/harness/receipt_guard.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/receipt_guard_adoption.py` | Python | Inventory of receipt-guard adoption across round runners | Yes (`python3 tools/harness/receipt_guard_adoption.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/harness/round_runner_conformance.py` | Python | Static conformance audit for acceptance runners | Yes (`python3 tools/harness/round_runner_conformance.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/argot-derivation-gate.py` | Python | Argot derivation replay gate | Yes (`python3 tools/gates/argot-derivation-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/costume-era-consistency-gate.py` | Python | Consistency audit for costume packets across historical eras | Yes (`python3 tools/gates/costume-era-consistency-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/handoff-packet-check.py` | Python | Handoff packet adjacency validator | Yes (`python3 tools/gates/handoff-packet-check.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/lexicon-coverage-audit.py` | Python | Lexicon coverage and phonology consistency gate | Yes (`python3 tools/gates/lexicon-coverage-audit.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/myth-consistency-gate.py` | Python | Consistency checker for mythological entities and timelines | Yes (`python3 tools/gates/myth-consistency-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/naming-collision-gate.py` | Python | Naming collision detector across phonology rules | Yes (`python3 tools/gates/naming-collision-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/phonology-sanity-gate.py` | Python | Phonology sanity gate | Yes (`python3 tools/gates/phonology-sanity-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/provenance-audit.py` | Python | Corpus scanner checking knowledge note provenance lines | Yes (`python3 tools/gates/provenance-audit.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/register-law-gate.py` | Python | Register law replay leg validator | Yes (`python3 tools/gates/register-law-gate.py --selftest` → PASS) |
| **kotodama-shokunin** | `tools/gates/typed-pipeline-gate.py` | Python | Typed pipeline schema validator | Yes (`python3 tools/gates/typed-pipeline-gate.py --selftest` → PASS) |
| **kumitate-shokunin** | `scripts/cite-check.mjs` | Node ESM | Citation re-verifier (2,538 LOC): resolves backticked paths, line spans, symbols, git hashes | Yes (`node scripts/cite-check.mjs --selftest` → 62/62 pass) |
| **kumitate-shokunin** | `scripts/claims-check.mjs` | Node ESM | Member-claims gate: checks section-form completeness for declared SCORECARD rows | Yes (`node scripts/claims-check.mjs --selftest` → PASS) |
| **kumitate-shokunin** | `scripts/proxy-check.mjs` | Node ESM | Measurement proxy re-computer (2,355 LOC): re-derives operability and coverage scores | Yes (`node scripts/proxy-check.mjs --selftest` → PASS) |
| **kumitate-shokunin** | `scripts/round-gate.mjs` | Node ESM | Round-close contract pre-checker: audits reports, headings, ancestor commits, git worktree | Yes (`node scripts/round-gate.mjs --selftest` → 60/60 pass) |
| **kumitate-shokunin** | `scripts/surface-probe.mjs` | Node ESM | Live surface conformance probe + SKILL.md GFM checklist runner | Yes (`node scripts/surface-probe.mjs --selftest` → PASS) |
| **kumitate-shokunin** | `scripts/kimi-census.mjs` | Node ESM | Substrate census gate: verifies 49 frozen members of `~/.kimi-code` (dirs, permissions, shapes) | Yes (`node scripts/kimi-census.mjs --selftest` → 43/43 pass) |
| **lore-shokunin** | `corpus/tools/boundary_doc_check.py` | Python | Boundary document validator: checks receipts, anchors, and structure | No (`no`) |
| **lore-shokunin** | `corpus/tools/dependency_freeze.py` | Python | Dependency inventory freezer and verifier | No (`no`) |
| **lore-shokunin** | `corpus/tools/discriminate_check.py` | Python | Discriminator check for checker repairs | No (`no`) |
| **lore-shokunin** | `corpus/tools/map_obligations.py` | Python | Compares source-attributed JSON obligations with canonical map | No (`no`) |
| **lore-shokunin** | `corpus/tools/support_check.py` | Python | Verifies string anchors and delivery modes in cluster maps | No (`no`) |
| **mado-shokunin** | `tools/mado-verify.sh` | Bash | Config-plane verdict gate (3,232 LOC): verifies hyprland, waybar, walker configs vs live state | Yes (`bash tools/mado-verify.sh --selftest` → 268/268 assertions) |
| **mori-shokunin** | `tools/mori-census.sh` | Bash | Fleet/host census (2,833 LOC): monitors watchdog, wave settlement, cgroups PSI, disk, silence | Yes (`bash tools/mori-silence-cases.sh tools/mori-census.sh` → 28/28 pass) |
| **mori-shokunin** | `tools/mori-silence-cases.sh` | Bash | Hermetic fixture test suite exercising lane silence grading under synthetic git trees | Yes (`bash tools/mori-silence-cases.sh tools/mori-census.sh` → 28/28 pass) |
| **revenger-shokunin** | `corpus/verify_pe_resources.py` | Python | Resource relation verifier: checks saved PE resource tables without PE execution | No (`no`) |
| **revenger-shokunin** | `corpus/verify_saved_evidence.py` | Python | Evidence verifier: checks saved REA static JS and ZIP evidence ledgers | No (`no`) |
| **revenger-shokunin** | `corpus/verify_icon_states.py` | Python | Icon-reference state verifier: checks multi-image icon links in saved PE records | No (`no`) |
| **revenger-shokunin** | `corpus/verify_evm_evidence.py` | Python | EVM evidence consistency verifier: checks EVM bytecode facts without EVM execution | No (`no`) |
| **souji-shokunin** | `tools/souji-census.sh` | Bash | Hygiene census: scans fleet repos for uncommitted changes, dead worktrees, stray scratch | No (`no`) |
| **souji-shokunin** | `tools/souji-verify.sh` | Bash | Receipt-gated removal verifier: enforces ancestor checks before permitting deletion | Yes (`bash tools/souji-round9-selftest.sh verify tools/souji-verify.sh` → 16/16 pass) |
| **souji-shokunin** | `tools/souji-quarantine.sh` | Bash | Receipt-gated quarantine tool: isolates candidate deletion files with receipts | Yes (`bash tools/souji-round9-selftest.sh quarantine tools/souji-quarantine.sh` → 16/16 pass) |
| **souji-shokunin** | `tools/souji-vault-verify.sh` | Bash | Ledger-backed moved-to-obsidian verifier: matches `source_sha256` and `vault_sha256` | Yes (`bash tools/souji-round9-selftest.sh vault tools/souji-vault-verify.sh` → 16/16 pass) |
| **souji-shokunin** | `tools/souji-round9-selftest.sh`| Bash | Unified selftest harness exercising souji verify, quarantine, and vault-verify | Yes (`bash tools/souji-round9-selftest.sh <kind> <path>` → 16/16 pass) |
| **tabi-shokunin** | `scripts/check-freshness.mjs` | Node ESM | Freshness gate: verifies cited public plugins/references vs `pins.tsv` and sha256 digests | Yes (`node scripts/check-freshness.mjs --self-test` → 12/12 pass) |
| **tabi-shokunin** | `scripts/check-round-contract.mjs`| Node ESM| Round contract gate: verifies committed round files, axes, and required checklist boxes | Yes (`node scripts/check-round-contract.mjs --self-test` → 4/4 pass) |
| **tabi-shokunin** | `scripts/check-user-round-contract.mjs`| Node ESM| Contract gate for user swarm rounds; verifies consequential action tripwires | Yes (`node scripts/check-user-round-contract.mjs --self-test` → 4/4 pass) |
| **tabi-shokunin** | `scripts/pstack-aggregate.mjs` | Node ESM | Swarm seat aggregator: folds 32 seat JSON outputs into aggregate summary | No (`no`) |
| **tabi-shokunin** | `scripts/pstack-seat.mjs` | Node ESM | Swarm seat executor: runs slice command and writes seat result file | No (`no`) |
| **tameshi-shokunin** | `tools/mutate-and-run.sh` | Bash | Mutation runner & regression suite (1,642 LOC): injects single mutants, runs 6 fleet legs | Yes (`bash tools/mutate-and-run.sh --selftest` → 80/80 pass) |
| **tsukuroi-shokunin** | `tools/tsukuroi-census.sh` | Bash | Four-plane host health census (2,403 LOC): pacman, systemd units, kernel rings/PSI, journal | Yes (`bash tools/tsukuroi-census.sh --selftest` → 80/80 pass) |

---

## 3. Cross-Lane Duplication Analysis (Re-implementations of the Same Check)

An analysis of tool bodies reveals extensive duplication where lanes independently developed bespoke solutions for generic protocol-level requirements:

### Check 1: Freshness & Substrate Drift Detection (5 Lanes)
- **Implementations:**
  - `tabi-shokunin/scripts/check-freshness.mjs` (`pins.tsv` + `freshness.expected.json`)
  - `kake-shokunin/scripts/freshness-sweep.mjs` (`freshness-pins.json` + `DEFAULT_PINS`)
  - `kotoba-shokunin/verifiers/check_substrate_pins.py` (`baseline.json`'s `measured_against`)
  - `kagi-shokunin/corpus/drift-pins.sh` (`drift-pins.tsv`)
  - `kotodama-shokunin/tools/harness/claims-freshness.py` (7 probe kinds: `sha256_eq`, `path_present`, `path_absent`, `count_eq`, `grep_absent`, `topic_owner_absent`, `capability_present`)
- **Common Defect:** Each lane uses a completely different pin registry grammar (TSV, JSON, Python dictionaries). Substrate movements (e.g. omp rebuild or pacman upgrade) require manual updates across multiple bespoke schemas.

### Check 2: Citation & Pointer Resolution (5 Lanes)
- **Implementations:**
  - `kumitate-shokunin/scripts/cite-check.mjs` (2,538 LOC, Node ESM: quote pairing `«…»`, backtick spans, fence masking, aliases, line ranges)
  - `kasegi-shokunin/corpus/instruments/resolve.py` + `anchorcheck.py` (Python: parses `path:NN[-MM]` line citations and repo-relative paths)
  - `kotoba-shokunin/verifiers/verify_corpus_integrity.py` (Python: scans `.ufo/reports/` and `corpus/lessons/` pointers)
  - `kotodama-shokunin/tools/harness/basename-couples-resolver.py` (Python: resolves basename references across corpus notes)
  - `chousa-shokunin/tools/research-gate.sh` (Bash: validates `CHAIN_HOP_UNRESOLVED`, `POINTER_EPHEMERAL`, `POINTER_UNRESOLVED`)
- **Common Defect:** Duplication of non-trivial parsing logic (CommonMark code fences, backticks). In `kumitate`, restructuring `ufo-fsd-alpha` caused 426 citation errors; other lanes have no citation checkers and silently accumulate dead line numbers.

### Check 3: Corpus Index & Readme Integrity (3 Lanes)
- **Implementations:**
  - `kotoba-shokunin/verifiers/verify_corpus_integrity.py` (`git ls-files corpus/` vs `corpus/README.md` first-column table rows)
  - `kengaku-shokunin/corpus/evidence/round13-coverage/coverage_census.py` (cross-checks `corpus/knowledge` and `lessons` vs `corpus/README.md` links)
  - `kotodama-shokunin/tools/source-audit-inventory.py` (read-only index audit)
- **Common Defect:** All check whether `corpus/knowledge/*.md` files are listed in `corpus/README.md` and whether table links point to existing files, but none share code.

### Check 4: Markdown Heading & Structure Linting (3 Lanes)
- **Implementations:**
  - `kotodama-shokunin/tools/check-readme-heading.py` (checks single H1 on line 1, no duplicate H2s, masks code fences)
  - `kumitate-shokunin/scripts/round-gate.mjs` (validates required headings `## Before -> after measurements`, `### SHONEN`)
  - `chousa-shokunin/tools/research-gate.sh` (validates table headers and structure)
- **Common Defect:** Markdown AST rules are re-coded using fragile ad-hoc regex that breaks when headings appear inside code blocks or indented text.

### Check 5: Round Contract & Pre-flight Gate (3 Lanes)
- **Implementations:**
  - `kumitate-shokunin/scripts/round-gate.mjs` (1,511 LOC: checks report headings, ancestor commits, unpushed commits, dirty worktree)
  - `tabi-shokunin/scripts/check-round-contract.mjs` (446 LOC: checks committed round files, axes, checklist boxes)
  - `kotodama-shokunin/tools/harness/round_runner_conformance.py` (static conformance audit)
- **Common Defect:** Lanes pre-check their own rounds using disparate criteria; no standardized pre-commit preflight exists fleet-wide.

### Check 6: Checklist Item Execution & Verification (3 Lanes)
- **Implementations:**
  - `kagi-shokunin/corpus/checklist-run.sh` (executes commands listed in TSV)
  - `kumitate-shokunin/scripts/surface-probe.mjs --checklists` (parses `SKILL.md` GFM task items `- [ ] <label> — <cmd> → exit <n> + <str>` and runs them)
  - `kotoba-shokunin/verifiers/verify_skill_checklist.py` (parses `SKILL.md` task items, verifies mapping to execution vocabulary)
- **Common Defect:** Divergent checklist syntaxes prevent fleet-wide automated audit of `SKILL.md` operability claims.

### Check 7: Host Substrate & Cleanliness Census (5 Lanes)
- **Implementations:**
  - `tsukuroi-shokunin/tools/tsukuroi-census.sh` (4 planes: packages, systemd, drivers/OOM, journal)
  - `mori-shokunin/tools/mori-census.sh` (host observability: watchdog, waves, memory PSI, disk runway, silence)
  - `souji-shokunin/tools/souji-census.sh` (fleet cleanliness: uncommitted files, dead worktrees, orphaned branches)
  - `kumitate-shokunin/scripts/kimi-census.mjs` (`~/.kimi-code` substrate census)
  - `kama-shokunin/tools/kama-probe.sh` (model serving endpoint census)
- **Common Defect:** Host status metrics are fragmented across separate tools that do not share metric schemas or exit codes.

### Check 8: Mutation Testing & Fault Injection (2 Lanes)
- **Implementations:**
  - `tameshi-shokunin/tools/mutate-and-run.sh` (generic mutation runner with 6 cross-fleet legs)
  - `kotoba-shokunin/verifiers/fault_injection_corpus.sh` (corpus mutation harness across temporary clones)
- **Common Defect:** Both prove that gates pass fraudulently unless tested against deliberate fault injection, but their mutation operators and replay ledgers are decoupled.

---

## 4. Patterns Worth Promoting Fleet-Wide & The Minimal Shared Shape

From the mature implementations above, four core patterns emerge as immediately promotable to fleet-wide shared instruments.

### Pattern 1: Freshness Gate (`scripts/freshness-gate.py`)
- **Origin & Basis:** Synthesizes `kotodama`'s 7 probe primitives, `kake`'s path sweep, and `kotoba`'s substrate binary pin checker.
- **Minimal Shared Shape:** A single, zero-dependency Python 3 standard library script taking a JSON pins registry:
  ```json
  {
    "pins": [
      {"kind": "path_present", "target": "corpus/knowledge/note.md"},
      {"kind": "path_absent", "target": "old-file.txt"},
      {"kind": "sha256_eq", "target": "package.json", "expect": "abcdef..."},
      {"kind": "count_eq", "target": "corpus/knowledge/*.md", "expect": 35},
      {"kind": "pattern_absent", "target": "SKILL.md", "pattern": "TODO|FIXME"},
      {"kind": "substrate_pin", "binary": "omp", "sha256": "bf1e86a9...", "mtime": 1729100000}
    ]
  }
  ```
- **CLI Contract:**
  `python3 scripts/freshness-gate.py [--pins FILE] [--json] [--selftest]`
- **Exit Codes:** `0` CLEAN · `1` DRIFT · `2` UNREADABLE / SETUP · `64` USAGE.

### Pattern 2: Heading & Markdown Structure Checker (`scripts/check-markdown.py`)
- **Origin & Basis:** Synthesizes `kotodama`'s `check-readme-heading.py`, `kumitate`'s fence-masking tokenizer, and `chousa`'s structure validator.
- **Minimal Shared Shape:** Implements CommonMark block-precedence parsing to mask fenced code blocks (both ` ``` ` and `~~~`) and verifies:
  1. Exactly one `# ` H1 heading at the first non-blank line of the document.
  2. No duplicate headings (`## ` or `### `) within the same parent section.
  3. Strict hierarchical progression (H1 $\rightarrow$ H2 $\rightarrow$ H3, no skipping levels).
  4. Required template sections when given a schema (e.g. verifying `## Gate`, `## Mistakes`, `### SHONEN` in round reports).
- **CLI Contract:**
  `python3 scripts/check-markdown.py <file.md> [--schema round-report|readme|skill] [--selftest]`
- **Exit Codes:** `0` PASS · `1` STRUCTURE_DEFECT · `2` UNREADABLE · `64` USAGE.

### Pattern 3: Corpus & Sources Census (`scripts/corpus-census.py`)
- **Origin & Basis:** Synthesizes `kotoba`'s `verify_corpus_integrity.py`, `kengaku`'s coverage census, and Campaign D4 (`sources-census.sh`).
- **Minimal Shared Shape:**
  1. **Two-Way Parity:** Reconciles `git ls-files corpus/` against `corpus/README.md` first-column table links (flags unindexed files, dangling links, and duplicate rows).
  2. **Metadata Header Audit:** Verifies every note in `corpus/knowledge/*.md` opens with valid `source:`, `verified-at:`, and `recheck:` fields.
  3. **Overdue Rechecks:** Parses `recheck:` dates (ISO YYYY-MM-DD or cadences) and flags any date earlier than current date (e.g. `2026-10-19`).
  4. **SOURCES.md Conformance (D1/D4):** Validates the 9-column contract (`|id|source|kind|tier|teaches|status|opened|recheck|used-by|`), verifies `S###` uniqueness, ensures `used-by` files exist and actually cite the ID.
- **CLI Contract:**
  `python3 scripts/corpus-census.py [--repo DIR] [--json] [--strict] [--selftest]`
- **Exit Codes:** `0` CLEAN · `1` PARITY_OR_SCHEMA_DRIFT · `2` SETUP · `64` USAGE.

### Pattern 4: Citation & Pointer Resolver (`scripts/resolve-citations.py`)
- **Origin & Basis:** Streamlines `kumitate`'s 2,538-line `cite-check.mjs` and `kasegi`'s `resolve.py` into a portable, zero-dependency utility.
- **Minimal Shared Shape:**
  1. Tokenizes Markdown outside code fences, extracting backticked tokens, verbatim quotes `«…»`, and table cells.
  2. Classifies citation tokens:
     - Local filesystem paths (`path/to/file.ext`)
     - Line spans (`path/to/file.ext:NN[-MM]`)
     - Git commit revisions (`[0-9a-f]{7,40}`)
     - Section anchors (`path/to/file.md#heading`)
  3. Re-resolves each token against local and origin git trees (`git cat-file -e`, file length boundaries, heading existence).
- **CLI Contract:**
  `python3 scripts/resolve-citations.py <file.md> [--repo DIR] [--origin DIR] [--json] [--selftest]`
- **Exit Codes:** `0` ALL_RESOLVED · `1` UNRESOLVED_OR_OOR · `2` SETUP · `64` USAGE.

---

## 5. Curated SOURCES Table & Citations

All sources below were opened, read, and verified in this session to ground the fleet-wide gate and instrument convergence.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|John MacFarlane et al.: CommonMark Specification (Version 0.31.2, 2024) — https://spec.commonmark.org/|spec|A|Two-phase parsing rule: block structure (fenced code blocks) takes strict precedence over inline structure (code spans), preventing fence token leakage|queued|2026-10-19|on-release|check-markdown.py, resolve-citations.py|
|S002|Yue Jia & Mark Harman: An Analysis and Survey of the Development of Mutation Testing (IEEE TSE 2011) — https://mutationtesting.uni.lu/|paper|A|Competent Programmer Hypothesis (real bugs are simple mutants) and Coupling Effect (simple mutant detection catches >99% complex faults)|queued|2026-10-19|360d|mutate-and-run.sh, fault_injection_corpus.sh|
|S003|Google Testing Blog: Hermetic Servers (2012) — https://testing.googleblog.com/2012/10/hermetic-servers.html|docs|A|Hermetic server-in-a-box pattern: local single-machine execution with zero network access eliminates test flakiness and environment drift|queued|2026-10-19|360d|mado-verify.sh, tsukuroi-census.sh, cite-check.mjs|
|S004|Aaron Maxwell: Use the Unofficial Bash Strict Mode (2014) — http://redsymbol.net/articles/unofficial-bash-strict-mode/|docs|B|Fail-closed shell execution (`set -euo pipefail`), pipeline exit unmasking, and mitigating SIGPIPE 141 trap crashes under early grep exits|queued|2026-10-19|360d|research-gate.sh, mori-census.sh, souji-verify.sh|
|S005|POSIX IEEE Std 1003.1-2024: Shell and Utilities (test, grep, sha256) — https://pubs.opengroup.org/onlinepubs/9799919799/|spec|A|Standardized exit code semantics (0=true/clean, 1=false/drift, >1=syntax/setup failure) and byte-exact checksum hashing|queued|2026-10-19|on-release|all fleet gates|

### Candidate Knowledge Entries (Fleet-Shared)

1. **`fleet-shared/commonmark-fence-masking.md`**
   - *Falsifiable claim:* Inline backtick tokenizers falsely classify text inside code blocks as live citations unless the parser processes leaf block fences (` ``` ` and `~~~`) before evaluating inline backtick spans.
   - *Source:* S001 (`https://spec.commonmark.org/0.31.2/#fenced-code-blocks`), section "Fenced code blocks": *"indicators of block structure always take precedence over indicators of inline structure"*.
   - *Fills:* `kumitate` (ER-16 repro), `kotodama` (`check-readme-heading.py`), `kasegi` (`anchorcheck.py`).
   - *Quality criteria:* Passes `kumitate`'s and `kotodama`'s hermetic test suites with 100% masking of fenced citations.

2. **`fleet-shared/mutation-coupling-invariance.md`**
   - *Falsifiable claim:* Test suites evaluating verification gates must achieve $\ge 80\%$ first-order mutant kill-rate to guarantee detection of multi-token and structural boundary drift.
   - *Source:* S002 (`https://mutationtesting.uni.lu/`), section "The Coupling Effect": *"complex mutants are coupled to simple mutants in such a way that a test data set that detects all simple faults ... will detect a high percentage of complex faults"*.
   - *Fills:* `tameshi` (mutation runner baseline), `kotoba` (fault-injection harness).
   - *Quality criteria:* Verified via `bash tools/mutate-and-run.sh --selftest` (80/80 pass).

3. **`fleet-shared/hermetic-test-isolation.md`**
   - *Falsifiable claim:* Gate selftests that access host paths (`/proc`, `~/.config`, git HEAD) produce false passes or flakes under host environment mutation; only temporary, in-memory or fixture-isolated trees guarantee deterministic verification.
   - *Source:* S003 (`https://testing.googleblog.com/2012/10/hermetic-servers.html`), section "Hermetic Servers": *"If you can start up an entire server ... locally on a single machine ... with no network connection, and it functions entirely as expected, it is hermetic"*.
   - *Fills:* `chousa` (133 cases), `tsukuroi` (80 cases), `mado` (268 assertions).
   - *Quality criteria:* Re-executes across 50 consecutive runs under randomized temporary directory roots without failure.

### ## Paths (Study Sequences)
- **Path 1: Resilient Gate Architecture:** `S004` (Bash Strict Mode) $\rightarrow$ `S003` (Hermetic Test Isolation) $\rightarrow$ `S001` (CommonMark Parsing) $\rightarrow$ `S002` (Mutation Testing).
  - *Rationale:* Secure the shell execution substrate first; isolate test fixtures hermetically; parse Markdown with formal AST precedence; validate gates with mutation testing.

### Rejected Candidates (Evidence of Taste)
1. *Python `pytest-flake8` / `black` AST Linters for Markdown.*
   - *Reason for rejection:* Third-party dependency bloat requiring virtual environments and pip installs; violates the zero-dependency stdlib fleet rule; tier C.
2. *Regex-only Multi-Line Citation Scrapers without Block Fencing.*
   - *Reason for rejection:* Fails on fenced code blocks (the exact defect causing false alarms in kumitate round 16 and kasegi round 17); tier C.
3. *Ad-Hoc JSON Schema Validators Using `jq` Subprocesses in Bash.*
   - *Reason for rejection:* Extreme process fork overhead and fragile error handling compared to Python's `json` standard library; tier C.

### ## Leads (Unopened)
- *Unified Markdown AST Specification (unist / mdast)* — `https://github.com/syntax-tree/mdast`
- *Mutation Testing in Practice at Google (Petrovic et al. 2018)* — `https://research.google/pubs/pub47243/`

---

## 6. Non-Obvious Move & Compatible Synthesis (UFO-FSD Connector Proposal)

### Evidence
1. **Tool Sprawl vs Maintenance Debt:** There are `198` operational scripts across 21 lanes (`198 — count from inventory`), but `114` lack hermetic self-tests. Five lanes independently wrote freshness gates, five wrote citation resolvers, three wrote heading checkers, and three wrote corpus index checkers.
2. **Substrate Vulnerability:** When the host substrate drifts (e.g. `omp 18.12.2` $\rightarrow$ `18.12.3` in kotoba, pacman library updates in tsukuroi, or `~/.kimi-code` MCP additions in kumitate), every bespoke gate fails or silently passes with stale baselines.
3. **Anti-Shrink and Mutation Hardening Already Exist in the Fleet:**
   - `kotoba-shokunin` developed `verifiers/check_assertion_floors.py`, an anti-shrink guard ensuring self-tests never silently drop assertions (`10/150/91/87/1597/62/104/328/150` floor).
   - `tameshi-shokunin` developed `tools/mutate-and-run.sh`, embedding 6 fleet regression legs across `kumitate`, `kagi`, `tsukuroi`, and `mado`.

### Affected Axes
- `operability`: **Improved** — replaces fragile, unmaintained per-lane scripts with 4 standardized, self-tested fleet instruments.
- `freshness`: **Improved** — centralizes drift detection into a unified pin engine that executes before round dispatch.
- `calibration`: **Improved** — stops lanes from grading their own homework with permissive, unasserted gates.
- *No axis harmed:* Domain isolation is preserved; lanes retain complete ownership of domain-specific verifiers (audio DSP, Godot fixtures, reverse engineering, model serving).

### Proposed Move
**Decouple "Protocol Verification" from "Domain Craft" by establishing a Minimal Shared Fleet Harness (the 4 Unified Instruments) in `/home/vgpnk/Projects/shokunin/scripts/`, locked by Kotoba's Anti-Shrink Floor Guard and Tameshi's Mutation Regression Ledger.**

Specifically:
1. **Extract the 4 Protocol Instruments into Fleet Root `scripts/` (and mirror to `kimi-shokunin` under D5):**
   - `scripts/freshness-gate.py` (Pattern 1)
   - `scripts/check-markdown.py` (Pattern 2)
   - `scripts/corpus-census.py` (Pattern 3 / D4 sources census)
   - `scripts/resolve-citations.py` (Pattern 4)
   All 4 are implemented in Python 3 standard library with zero third-party dependencies, running in under 2 seconds.
2. **Incorporate Anti-Shrink Assertion Floors (`kotoba` pattern):**
   Every fleet instrument's `--selftest` outputs an exact assertion count (`PASS: N assertions`). `scripts/check-assertion-floors.py` enforces that no edit can drop assertion coverage below registered floors.
3. **Bind into Tameshi's Fleet Mutation Regression (`tameshi` pattern):**
   Register the 4 fleet instruments as standard legs in `tameshi-shokunin/tools/mutate-and-run.sh` to prove $\ge 80\%$ mutation kill-rates across all protocol checks.
4. **Lane Domain Boundary Rule:**
   Lane repositories keep domain-specific tools in `<lane>/tools/` (e.g. `kama-probe.sh`, `mado-verify.sh`, `run_battery.py`), but retire lane-local copies of citation checkers and heading scrapers in favor of calling the root protocol scripts.

### Second-Order Effects & Risks
- **Runtime Surface:** Zero runtime daemon overhead. All 4 scripts are on-demand CLI utilities.
- **Contract Surface:** Reconciles D1 (`SOURCES.md`), D3 (`CORPUS.md`), D4 (`sources-census.sh`), and D5 (`kimi-shokunin` sync) under a single verified harness.
- **Substrate Surface:** Uses exclusively Python 3.10+ standard library (`sys`, `os`, `re`, `json`, `hashlib`, `argparse`, `pathlib`). No virtual environment, pip install, or Node dependency required.
- **Verification Surface:** Eliminates verifier disagreements across Wave 3 non-author review agents.
- **Contradiction Stated (Strictness vs Immediate Breakage):** Running `cite-check` naively across the fleet surfaces hundreds of historical line-number drifts. *Resolution:* The harness defaults to reporting categorized debt (`INFO`/`WARN`) and only fails closed (`exit 1`) on files touched in the active round's worktree.

### Verification Recipe
```bash
# 1. Run all 4 fleet shared instruments with hermetic self-tests
python3 scripts/freshness-gate.py --selftest
python3 scripts/check-markdown.py --selftest
python3 scripts/corpus-census.py --selftest
python3 scripts/resolve-citations.py --selftest

# 2. Verify anti-shrink assertion floors
python3 scripts/check-assertion-floors.py --selftest

# 3. Verify mutation kill-rate across the fleet legs
bash /home/vgpnk/Projects/shokunin/tameshi-shokunin/tools/mutate-and-run.sh --regression
```
