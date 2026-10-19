# kaika W1 — Cross-Lane Adjacency and Source-Sharing Map

**Author:** W1ConnectSources (UFO-FSD connector)  
**Date:** 2026-10-19  
**Tool Availability:** `web_search` and `read` (public web and local filesystem) were available, functioning, and exercised; all claims and rows are grounded in files opened and read in this session.

---

## 1. Executive Summary & Fleet Map Topology

Across the 21 lane repositories under `/home/vgpnk/Projects/shokunin/*-shokunin` (`21 — ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l`), all 21 maintain a formal `PROVINCE.md` (`21 — ls /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md | wc -l`), while 19 maintain a `corpus/README.md` (`19 — ls /home/vgpnk/Projects/shokunin/*-shokunin/corpus/README.md 2>/dev/null | wc -l`). Two lanes—`audio-shokunin` and `revenger-shokunin`—currently lack a top-level `corpus/README.md`, representing immediate documentation debt.

The fleet holds 663 knowledge entries (`663 — find /home/vgpnk/Projects/shokunin/*-shokunin/corpus/knowledge -maxdepth 2 -name "*.md" 2>/dev/null | wc -l`) and 540 lesson entries (`540 — find /home/vgpnk/Projects/shokunin/*-shokunin/corpus/lessons -maxdepth 2 -name "*.md" 2>/dev/null | wc -l`). However, knowledge is largely siloed within lane boundaries despite heavy technical overlap in headless execution, process observation, binary inspection, prompt engineering, and verification discipline.

---

## 2. (a) Shared Frontier Topics & Hand-off Protocols

Analysis of all 21 `PROVINCE.md` and `corpus/README.md` files reveals six major shared frontier zones:

### 1. Browser Automation & CDP Session Discipline
- **Lanes Involved:** `tabi-shokunin`, `kake-shokunin`, `kaidoku-shokunin`, `kagi-shokunin`.
- **Evidence:**
  - `tabi-shokunin/PROVINCE.md:6-14` owns browser and web-interaction craft (`kimi-webbridge`, headless Chromium, screenshot/DOM determinism, multi-step journeys).
  - `kake-shokunin/SKILL.md:161` asserts a machine-wide lease of the `the-musketeer` Chrome profile for web properties and deployment audits.
  - `kaidoku-shokunin/PROVINCE.md:53,128` exercises CDP targets for passive network capture and script extraction (`export-web-scripts`).
  - `kagi-shokunin/PROVINCE.md:43` monitors the 1Password Chrome CDP bridge on port 9222.
- **Hand-off Protocol:**
  - `tabi` is the fleet's sole method owner for CDP connection parameters, target attach/detach, wait states, and DOM/screenshot determinism.
  - `kake` and `kaidoku` hand off browser-driving implementation patterns to `tabi`, consuming only output artifacts or documented launch flags.
  - `kagi` restricts its concern to filesystem permissions (0600) on native messaging manifests, delegating profile runtime behavior to `tabi`.

### 2. Shipped-Artifact Reverse Engineering vs Host Substrate Diagnosis
- **Lanes Involved:** `kaidoku-shokunin`, `revenger-shokunin`, `tsukuroi-shokunin`, `game-dev-3d-shokunin`.
- **Evidence:**
  - `tsukuroi-shokunin/PROVINCE.md:42` (ADJ-06) explicitly triggers a boundary: *"Driver/firmware/package mechanism requires shipped-artifact reverse engineering beyond health inventory -> protocol integrator — kaidoku/revenger ownership unresolved"*.
  - `game-dev-3d-shokunin/PROVINCE.md:8-12,38-41` uses REA for static container/asset format checks but refuses live reverse engineering.
  - `kaidoku-shokunin/corpus/README.md:13-70` holds 70+ verified knowledge entries spanning Ghidra 12.1.4, PE ARM64, ASAR, APK, and ELF binaries.
  - `revenger-shokunin/SCORECARD.md:3-15` scores calibration and replay over saved PE evidence ledgers.
- **Hand-off Protocol:**
  - `tsukuroi` triages host packages and kernel module states (e.g., nvidia open dkms and GSP firmware); if a binary mechanism must be decompiled, `tsukuroi` produces an exact artifact hash and passes it to the protocol integrator for assignment to the RE lane.
  - `game-dev-3d` uses only static inspection schemas verified by `kaidoku` and never invokes debuggers or decompilation engines directly.

### 3. Fictional Worldbuilding vs World Bible Canon vs Game/Audio Assets
- **Lanes Involved:** `kotodama-shokunin`, `lore-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, `audio-shokunin`.
- **Evidence:**
  - `kotodama-shokunin/PROVINCE.md:9-17` owns linguistic-cultural generative craft (conlangs, naming, myths, materials), holding 224 knowledge files, but explicitly refuses claiming canon: *"kotodama hands off systems; lore records and verifies them"*.
  - `lore-shokunin/PROVINCE.md:3-10` owns entities, relations, and timelines, refusing to claim canon without in-world citation or to verify game mechanics.
  - `audio-shokunin/PROVINCE.md:15` refuses narrative canon (`lore`) and game mechanics (`game-dev-2d`).
  - `game-dev-2d-shokunin/PROVINCE.md:10` and `game-dev-3d-shokunin/PROVINCE.md:35` refuse narrative canon.
- **Hand-off Protocol:**
  - `kotodama` delivers structured linguistic/mythic systems to `lore` via `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
  - `lore` validates entity/timeline coherence and mints canonical in-world citations.
  - `game-dev-2d`, `game-dev-3d`, and `audio` ingest canon-certified names, motifs, and lore briefs from `lore` as read-only inputs, never inventing narrative tokens.

### 4. Local Model Serving Health vs Capability Evaluation vs Prompt Craft
- **Lanes Involved:** `kama-shokunin`, `kengaku-shokunin`, `kotoba-shokunin`, `kumitate-shokunin`.
- **Evidence:**
  - `kama-shokunin/PROVINCE.md:3-39` monitors local serving ports (`8080`, `34113`) and detects baseURL drift, reporting 3 registry rows as `DEAD` connection-refused (`exit 2`).
  - `kengaku-shokunin/PROVINCE.md:24-25,43-48` evaluates model capabilities (bench-arena, planning horizons), noting that llama-server flags (q4_0 KV cache, `--parallel 2`) materially bias evaluations.
  - `kotoba-shokunin/PROVINCE.md:3` audits skill frontmatter, description render cliffs, and prompt-trigger fidelity.
  - `kumitate-shokunin/PROVINCE.md:3` governs OMP task/hub dispatch and runtime routing.
- **Hand-off Protocol:**
  - `kama` provides objective endpoint availability to `kengaku` and `kumitate`.
  - `kengaku` reports prompt-induced capability defects (e.g., tools without system prompts causing `finish=tool_calls`) to `kotoba`.
  - `kotoba` crafts verified skill descriptions and system prompt contracts, handing them to `kumitate` for OMP/UFO orchestration integration.

### 5. Host OS Health vs Fleet Process Observability vs Repository Hygiene
- **Lanes Involved:** `tsukuroi-shokunin`, `mori-shokunin`, `souji-shokunin`.
- **Evidence:**
  - `tsukuroi-shokunin/PROVINCE.md:21-25,40` (ADJ-04) notes that OS memory and kill events must be correlated with fleet waves by `mori`.
  - `mori-shokunin/PROVINCE.md:6-10` monitors watchdog liveness, wave settlement, cgroups memory events, and lane silence grading.
  - `souji-shokunin/PROVINCE.md:8-17` performs receipt-gated removal of stale scratch and dead worktree metadata.
- **Hand-off Protocol:**
  - `tsukuroi` observes systemd and kernel error events and hands timestamped metric packets to `mori`.
  - `mori` correlates system stalls with active wave task IDs and publishes progress/silence grades.
  - `souji` scans for abandoned wave scratch trees (`.scratch/`, dead worktrees) identified by `mori`, gating deletion on git-clean and Obsidian preservation receipts.

### 6. Headless Game Engine Execution & Audio Stems
- **Lanes Involved:** `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, `audio-shokunin`.
- **Evidence:**
  - `game-dev-2d-shokunin/PROVINCE.md:3-9` owns 2D Godot 4.7.2 headless fixtures (physics, camera, UI, level contact).
  - `game-dev-3d-shokunin/PROVINCE.md:3-12` owns 3D movement, transforms, and projection across engines.
  - `audio-shokunin/PROVINCE.md:3-5` synthesizes and verifies audio stems via headless analysis (duration, loudness, spectral centroid, loop seam).
- **Hand-off Protocol:**
  - `game-dev-2d` and `3d` share headless runner architecture (`run_battery.py`, scratch isolation, stream attribution).
  - Game lanes provide event trigger constraints and duration windows to `audio`.
  - `audio` delivers deterministic WAV assets meeting EBU R128 loudness and seamless loop criteria back to game fixtures without altering engine scene trees.

---

## 3. (b) Techniques One Lane Holds That Another Needs

The fleet contains several mature, battle-tested craft instruments that solve common architectural problems across lanes:

| Providing Lane | Technique / Instrument | Description & Capabilities | Target Lanes in Need |
|---|---|---|---|
| `chousa` | **5-Section Composed Verification Gate** (`tools/research-gate.sh` / `verify-all`) | Validates claim spans (`verify-claims`), citation chains (`verify-chain`), falsifiable sweeps (`verify-sweeps`), and referential integrity (`verify-integrity`) with fail-closed token boundary checks (`tok_span_at`). | **All 21 lanes** for `corpus/SOURCES.md` and new `corpus/knowledge/` admissions to prevent unanchored or drifted claims. |
| `tameshi` | **Hermetic Mutation Testing & Kill-Rate Suite** (`tools/mutate-and-run.sh`) | Generates single-edit mutants in disposable `/tmp` copies with count-invariance gates to measure test suite sensitivity and detect unasserted branches (80% kill-rate baseline). | `kagi`, `kumitate`, `tsukuroi`, `mori`, `kotoba` (all lanes authoring executable verification gates). |
| `kagi` | **Shape-Only Non-Leaking State Census** (`corpus/surface-census.sh`, `state-shape.tsv`) | Verifies sensitive runtime files (SQLite magic header, permissions 0600, log size floors, JSON key structures) without logging secret values or tokens. | `tabi` (browser cookies/profiles), `kama` (API endpoints/configs), `souji` (quarantine scans), `kumitate` (Kimi binary secrets). |
| `mori` | **Behavioral Drift Baseline with Volatile Masking** (`tools/mori-census.sh --pin / --drift`) | Captures canonical output snapshots while masking known volatile fields (timestamps, churning counters, PIDs) to distinguish true behavioral regressions from clock drift. | `tsukuroi` (OS state drift), `kake` (sitemap/deploy drift), `kama` (listener drift), `chousa` (gate baselines). |
| `kotodama` | **Exhaustive Topic-Index Parity Sweep** (`reports/round-28/readme/sweep.py`) | Enforces exact two-way matching between `corpus/README.md` index rows and files on disk (filename order, byte-equal topic text, section counts, totals line, footer vectors). | `audio` & `revenger` (currently lacking `corpus/README.md`), `kotoba`, `kengaku`, `kumitate`, `lore`. |
| `kaidoku` | **Observation / Inference / Unknown Discipline** (`PROVINCE.md:5-7`, `corpus/knowledge/seed.md`) | Strict epistemic labelling (`[OBS]`, `[INF]`, `[UNK]`) preventing inferred hypotheses from being recorded as verified runtime facts. | `mado` (config vs rendered UI), `tsukuroi` (boot log vs delay causes), `tabi` (DOM vs pixels), `kama` (config pin vs live server). |
| `souji` | **Dual-Hash Preservation Ledger** (`corpus/knowledge/obsidian-ledger.tsv`) | Enforces that no artifact is removed or declared "moved to archive" without matching `source_sha256` and `vault_sha256` receipts. | `kasegi` (tracking lost roots), `kengaku` (benchmark archives), fleet root (wave scratch pruning). |

---

## 4. (c) Contested Scope (Reported, Never Absorbed)

The following five scopes represent unresolved cross-lane ownership boundaries. Per protocol, they are reported here for integrator ruling and must never be silently absorbed by any lane:

1. **`$HOME/.local/share/the-musketeer/chrome-profile` (CDP 9222 Lease & Profile Ownership)**
   - *Contested between:* `kake` vs `kagi` vs `tabi`.
   - *Evidence:* `kake/SKILL.md:161` asserts a machine-wide lease of the profile directory; `kagi/PROVINCE.md:43` records it as contested in `corpus/adjacency.tsv` (presence-only, mode unchecked); `tabi/PROVINCE.md:8` owns browser profile shape censuses.
   - *Status:* Unresolved. Reported to the protocol integrator.

2. **`$HOME/.config/opencode` (Configuration Layering & Agent Ceilings)**
   - *Contested between:* `kotoba`, `kama`, `kengaku`, `kumitate`, `kagi`.
   - *Evidence:* `kagi/corpus/README.md:85` documents multi-claim status across 24 files in kotoba, 14 in kama, 9 in kengaku, 2 in kumitate. Kotoba claims the instruction/agent markdown files; kama claims baseURL endpoint configuration; kagi claims credential hygiene; kumitate claims runner invocation.
   - *Status:* Unresolved. Recommended resolution: structural partition by filename/subpath under fleet contract.

3. **Shipped-Artifact Reverse Engineering with REA (`kaidoku` vs `revenger`)**
   - *Contested between:* `kaidoku-shokunin` vs `revenger-shokunin`.
   - *Evidence:* Both claim reverse engineering of shipped binaries/packages using REA (`kaidoku/PROVINCE.md:3-6` vs `revenger/PROVINCE.md:3-7`). Explicitly cited as unresolved in `tsukuroi/PROVINCE.md:42` (ADJ-06) and `tsukuroi/corpus/README.md:28-29`.
   - *Status:* Unresolved duplicate domain. Recommended resolution: specialize `kaidoku` for live Linux environment binary/package analysis (Ghidra, apktool, unblob) and `revenger` for cross-platform offline evidence ledger verification.

4. **The Model-Serving Plane (llama-server flags, slot/batch config, unit management)**
   - *Contested / Unowned:* `kama` vs `kengaku` vs operator.
   - *Evidence:* `kama/PROVINCE.md:25-29,45-49` refuses writing systemd units or restarting services; `kengaku/PROVINCE.md:24-25` refuses managing server flags while documenting that q4_0 KV quantization alters benchmark results.
   - *Status:* Unowned orphan substrate plane. Escalated to operator/integrator.

5. **World-Building Inspiration vs Fictional World Canon**
   - *Contested between:* `kotodama`, `lore`, and game dev lanes (`game-dev-2d`, `game-dev-3d`, `audio`).
   - *Evidence:* `kotodama/PROVINCE.md:16-17` refuses canon; `lore/PROVINCE.md:9` refuses un-cited canon; game and audio lanes refuse canon but occasionally mint names in fixtures.
   - *Status:* Formally governed by `worldbible-integration-contract.md`; requires active gate enforcement to reject uncertified world tokens in game fixtures.

---

## 5. (d) Candidate Fleet-Shared Source Pool

The following sources were opened, read, and verified in this session. Each provides authoritative guidance useful to two or more lanes.

### Curated SOURCES Table

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|Chrome DevTools Protocol: Page Domain — https://chromedevtools.github.io/devtools-protocol/tot/Page/|spec|A|Page navigation lifecycle, addScriptToEvaluateOnNewDocument isolated world evaluation, and captureScreenshot viewport clipping|queued|2026-10-19|on-release|tabi, kaidoku, kake|
|S002|Linux Kernel Documentation: Pressure Stall Information (PSI) — https://docs.kernel.org/accounting/psi.html|docs|A|/proc/pressure/{cpu,memory,io} some vs full stall mechanics, poll() threshold notification API, and cgroup2 memory.pressure accounting|queued|2026-10-19|180d|mori, tsukuroi|
|S003|EBU R 128: Loudness normalisation and maximum level of audio signals (EBU / ITU-R BS.1770) — https://en.wikipedia.org/wiki/EBU_R_128|spec|A|-23.0 LUFS integrated loudness target, -1 dBTP true peak ceiling, and absolute (-70 LUFS) / relative (-10 LU) gating functions|queued|2026-10-19|on-release|audio, tameshi, game-dev-2d|
|S004|Godot Engine 4.x Command Line Tutorial & Headless Reference — https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html|docs|A|--headless flag setting display/audio to dummy, --quit/--quit-after loop bounds, and -s script parsing for automated test execution|queued|2026-10-19|on-release|game-dev-2d, game-dev-3d, audio|
|S005|Yue Jia & Mark Harman: An Analysis and Survey of the Development of Mutation Testing — https://mutationtesting.uni.lu/|paper|A|Competent Programmer Hypothesis, Coupling Effect, first-order vs higher-order mutants, and equivalent mutant cost-reduction taxonomies|queued|2026-10-19|360d|tameshi, kumitate, kagi, chousa|
|S006|Aaron Maxwell: Use the Unofficial Bash Strict Mode (Unless You Love Debugging) — http://redsymbol.net/articles/unofficial-bash-strict-mode/|docs|B|set -euo pipefail with IFS=$'\n\t' mechanics, unmasking pipeline exit codes, and preventing silent unbound variable propagation|queued|2026-10-19|360d|mori, chousa, tsukuroi, kagi|
|S007|W3C WebDriver BiDi Specification (Editor's Draft) — https://w3c.github.io/webdriver-bidi/|spec|A|Bidirectional asynchronous browser automation protocol via CDDL commands and streaming events replacing HTTP polling|queued|2026-10-19|90d|tabi, kake, kaidoku|
|S008|SQLite 3 Database File Format Specification — https://www.sqlite.org/fileformat.html|spec|A|16-byte magic header string ('SQLite format 3\000'), write/read version 1 vs 2 (WAL), page size bounds, and change counter mechanics|queued|2026-10-19|on-release|kagi, kaidoku, kotoba, chousa|

### Candidate Knowledge Entries (Fleet-Shared)

1. **`fleet-shared/cdp-screenshot-determinism.md`**
   - *Falsifiable claim:* `Page.captureScreenshot` produces bit-exact PNG outputs across repeated runs only when `clip` viewport dimensions, `fromSurface: true`, and device metrics override are explicitly pinned.
   - *Source:* S001 (`https://chromedevtools.github.io/devtools-protocol/tot/Page/#/Page.captureScreenshot`), line 61: *"Capture page screenshot... fromSurface: boolean Capture the screenshot from the surface, rather than the view. Defaults to true."*
   - *Fills:* `tabi` (CDP evidence patterns), `kaidoku` (runtime observation), `kake` (visual regression).
   - *Quality criteria:* Passes `tabi`'s `QUALITY.md` via two independent headless runs with SHA-256 byte comparison.

2. **`fleet-shared/linux-psi-pressure-polling.md`**
   - *Falsifiable claim:* Writing `<some|full> <stall_us> <window_us>` to `/proc/pressure/memory` allows unprivileged userspace polling via `POLLPRI` if window size is a multiple of 2 seconds.
   - *Source:* S002 (`https://docs.kernel.org/accounting/psi.html`), section "Monitoring for pressure thresholds": *"Unprivileged users can also create monitors, with the only limitation that the window size must be a multiple of 2s"*.
   - *Fills:* `mori` (memory pressure detection), `tsukuroi` (ADJ-04 host pressure packets).
   - *Quality criteria:* Passes `tsukuroi`'s and `mori`'s quality bars by running non-root poll probe without kernel panic or permissions error.

3. **`fleet-shared/bash-pipefail-sigpipe-trap.md`**
   - *Falsifiable claim:* Under `set -eo pipefail`, piping stdout into an early-exiting `grep -q` causes the upstream writer to receive SIGPIPE (exit code 141), causing the entire pipeline to fail unless `PIPESTATUS` or temporary file redirection is used.
   - *Source:* S006 (`http://redsymbol.net/articles/unofficial-bash-strict-mode/`), section "set -o pipefail": *"If any command in a pipeline fails, that return code will be used as the return code of the whole pipeline."*
   - *Fills:* `mori` (selftest flake closeout r9), `chousa` (gate hardening), `tsukuroi` (census error traps).
   - *Quality criteria:* Reproduces the exact 141 exit code in a minimal 2-line test script and confirms fix via capture-file.

4. **`fleet-shared/godot-headless-dummy-drivers.md`**
   - *Falsifiable claim:* Invoking `godot --headless` automatically initializes `--display-driver headless` and `--audio-driver Dummy`, suppressing all audio output unless explicitly overridden.
   - *Source:* S004 (`https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html`), line 69: *"--headless ... Enable headless mode (--display-driver headless --audio-driver Dummy). Useful for servers and with --script."*
   - *Fills:* `game-dev-2d` (headless fixture suite), `game-dev-3d` (engine execution reality), `audio` (headless WAV playback verification).
   - *Quality criteria:* Verified by executing `godot --headless --version` and checking stdout attribution.

### Study Paths (`## Paths`)

- **Path 1: Automated Headless Testing Architecture**
  - Sequence: `S006` (Bash Strict Mode) $\rightarrow$ `S005` (Mutation Testing) $\rightarrow$ `S004` (Godot CLI / Headless) $\rightarrow$ `S001` (CDP Spec).
  - *Rationale:* Build fail-closed bash runners first; apply mutation testing to ensure suites kill real bugs; drive game engines headlessly; automate UI/browser interactions.
- **Path 2: Substrate Observability & Hygiene**
  - Sequence: `S008` (SQLite File Format) $\rightarrow$ `S002` (Linux PSI) $\rightarrow$ `S006` (Bash Strict Mode).
  - *Rationale:* Understand durable database state shapes without secret leakage; monitor system contention signals via PSI; enforce pipeline reliability.

### Rejected Candidates (Evidence of Taste)

1. *Generic Web Scraping Blog Summaries on Chrome DevTools Protocol* (e.g. ScrapeGraphAI/Medium posts).
   - *Reason for rejection:* Secondary rehash; omits exact parameter types (e.g. `Viewport` clip struct, `fromSurface` defaults), error codes, and version-specific deprecations; tier C.
2. *Unconditional "set -e" Wrapper Templates Without SIGPIPE or Trap Mitigation*.
   - *Reason for rejection:* Promotes naive `set -e` without addressing SIGPIPE 141 pipeline failures under `pipefail` (the exact defect class mined in Mori r9 and Chousa r1); tier C.
3. *Godot 3.x Headless CLI Tutorials* (e.g., using `--no-window`).
   - *Reason for rejection:* Deprecated architecture; Godot 4.x replaced `--no-window` with `--headless` and changed audio dummy driver initialization, failing on Godot 4.7.2; tier C.

### Leads (Unopened)
- *W3C Web Platform Tests (WPT) WebDriver BiDi Test Suite* — `https://github.com/web-platform-tests/wpt/tree/master/webdriver/tests/bidi`
- *EBU Tech 3341 ("EBU Mode" Loudness Metering Specification)* — `https://tech.ebu.ch/publications/tech3341`
- *Papadakis et al. (2018) "Mutation Testing Advances: An Analysis and Survey"* — `https://mutationtesting.uni.lu/survey.pdf`

---

## 6. Non-Obvious Move & Compatible Synthesis (UFO-FSD Connector Proposal)

### Evidence
1. **Wave 1 Artifact Convergence:** All 21 lanes are being equipped with `corpus/SOURCES.md` (D1) and new knowledge entries (D2) grounded in current art.
2. **Existing Disparate Gate Mechanics:**
   - `chousa` built `tools/research-gate.sh` (`verify-all`), which checks claim spans, citation hops, sweeps, and referential integrity.
   - `tameshi` proved in `corpus/knowledge/mutation-case-*.md` that census gates without mutation test harnesses suffer from 20% survivor blind spots (unasserted branches).
   - `kotodama` proved in `reports/round-28/readme/sweep.py` that two-way mechanical parity checks prevent index drift across hundreds of files.
   - `mori` proved in `tools/mori-census.sh` that `--pin` and `--drift` with volatile-field masking prevent false-alarm churn.
3. **Plan Contract Gap (D4):** Campaign plan deliverable D4 specifies `scripts/sources-census.sh` to aggregate lane sources and flag malformed rows or overdue rechecks.

### Affected Axes
- `calibration`: **Improved** — turns source citation from unchecked prose into machine-verifiable referential integrity.
- `coverage`: **Improved** — enables cross-lane source sharing without domain boundary violation.
- `operability`: **Improved** — provides a single fleet gate with hermetic `--selftest`.
- *No axis harmed:* Zero scalar score collapse; per-axis verdicts and lane domain partitions strictly preserved.

### Proposed Move
**Synthesize D4 (`scripts/sources-census.sh`) with `chousa`'s referential integrity engine, `tameshi`'s mutation verification, and `mori`'s volatile drift-pinning.**

Specifically, structure `scripts/sources-census.sh` as a four-phase contract gate:
1. **Schema & Taxonomy Gate:** Validates every lane's `corpus/SOURCES.md` against the 9-column contract (`id`, `source`, `kind`, `tier`, `teaches`, `status`, `opened`, `recheck`, `used-by`). Flags malformed IDs, unlisted tiers, and invalid status values.
2. **Referential Integrity & Existence Enforcement (`chousa` pattern):**
   - For every row where `status == mined`, verify that the paths listed in `used-by` exist on disk and actually cite the `S###` ID.
   - For every knowledge file in `corpus/knowledge/*.md`, verify that cited `S###` IDs resolve to an opened row in `SOURCES.md` (`REF_UNRESOLVED` detection).
3. **Cross-Lane Promotion & Fleet Aggregation:**
   - Detects sources cited across $\ge 2$ lanes and automatically compiles the **Fleet-Shared Source Pool** (`local://fleet-sources.md`), avoiding duplication and enabling shared learning.
4. **Hermetic Mutation Selftest (`tameshi` pattern):**
   - Implements `--selftest` with pre-registered synthetic mutants (dropped pipe, missing header, invalid tier, dangling `used-by` path, overdue recheck) requiring 100% kill-rate before exit 0.

### Second-Order Effects & Risks
- *Runtime Surface:* Pure read-only shell/node script operating in local scratch; zero impact on running processes or external networks.
- *Contract Surface:* Strictly adheres to the W1 `SOURCES.md` draft contract; requires no changes to `PROTOCOL.md` or lane domain boundaries.
- *Substrate Surface:* Uses existing host utilities (`bash`, `awk`, `python3` or `node`); no new packages required.
- *Risk:* Overly rigid path validation could fail if a lane documents an external or archived path. *Mitigation:* Adopt `chousa`'s `exempt-but-counted` status for documented out-of-corpus references.

### Verification Recipe
```bash
# 1. Run sources census gate across all lane repos
bash scripts/sources-census.sh --verify

# 2. Verify hermetic mutation kill-rate
bash scripts/sources-census.sh --selftest

# 3. Check behavioral drift against baseline
bash scripts/sources-census.sh --drift corpus/evidence/sources-baseline.json
```
