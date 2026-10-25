# ART dossier — `game-dev-2d`

Prepared 2026-10-19. Read-only lane research; this artifact is the only write. Local scope was limited to the ART-named `PROVINCE.md`, `corpus/README.md`, and the two `corpus/knowledge/` entries; external source rows below were opened in this session. No instruction-like content or prompt-injection attempt was observed in the opened material.

## Uncovered ground

**Observed local corpus.** `PROVINCE.md:3` defines the lane as 2D game production verified by executable headless fixtures, including loop, input, physics, scenes, camera, UI, levels, juice, and export readiness. It names Godot 4.7.2 as the runtime (`PROVINCE.md:5–10`). The corpus index describes a project-local fixture battery and headless probes for input, collisions, scene flow, camera, UI, TileMapLayer level metadata/runtime contact, animation, audio, export, and launch (`corpus/README.md:3–24`; `corpus/knowledge/seed.md:20–29`). The knowledge filenames found are `seed.md` and `2026-10-12-production-checklist.md`.

**Explicitly uncovered.** The index says rendered camera framing, production/rendered UI, and rendered animation/juice remain unprobed (`corpus/README.md:7–10`). The checklist calls save/load, export-template checks, and test bundling production surfaces (`corpus/knowledge/2026-10-12-production-checklist.md:15–17`), while the seed lists save/load, export-template check, and autotest bundling among candidate production axes (`corpus/knowledge/seed.md:27–29`). The current local evidence is rich in headless logic and contact behavior but does not establish visual parity, deterministic replay guarantees, an engine-version upgrade matrix, or an end-to-end clean-checkout import/export/runtime pipeline.

**Current-art gaps suggested by this research.**

- Godot 4.5 deprecated `TileMap` in favor of multiple `TileMapLayer` nodes; the 4.5 migration notes document changed `get_coords_for_body_rid()` precision after physics chunking was enabled. Existing lane notes cover TileMapLayer metadata and contact, not the migration/chunk-attribution boundary (S002–S005).
- Godot 4.6 changed 2D batching internals and added rotatable scene tiles. That current rendering/editor surface is not represented by the named headless lessons, and a logical headless PASS cannot by itself establish visible output or renderer performance (S012, S024).
- Godot’s physics docs explicitly disavow deterministic physics. Existing repeated battery runs are valuable regressions but must not be presented as proof that a physics replay yields bit-identical state across runs (S009–S010, S025).
- Current official GUT and gdUnit4 materials expose headless-capable test runners, scene-level tests, reports, and distinct exit/warning semantics. The named lane index describes its own Python/Godot fixture battery; it does not document a decision or integration test for either framework (S016–S023).
- Godot CLI export requires a named preset and available platform templates; official engine CI separately exercises import/export, package launch, and captured output. A scratch export or scene-level headless test alone does not establish that a clean-checkout artifact launches (S006–S008, S024).

## Current art (2025–2026)

- **Release/support context:** the official policy lists Godot 4.7 and 4.6 as supported branches, 4.5 as partial support, and 4.4 as end-of-life. The lane’s stated 4.7.2 runtime is therefore a reasonable current baseline, but source/version compatibility should be recorded and revisited on engine/add-on releases (S001).
- **Tilemaps:** use `TileMapLayer` for new work; the old `TileMap` class is deprecated and the editor offers layer extraction. TileMapLayer batches updates, and its physics quadrant size groups similar tile collisions; in 4.5, higher values make body-RID-to-cell attribution less precise, while size 1 preserves exact cell coordinates. This is a concrete migration boundary for executable level/contact fixtures (S002–S005).
- **2D renderer:** the 4.6 release reports a redesign of 2D batching to reduce GPU cost, and adds 90-degree rotation for scene tiles. The release’s performance claim is specific to its tested GPU-bound scenarios, not a universal lane threshold. Keep logic checks headless, but add a renderer-pinned graphical canary for visible behavior/performance claims (S012, S024). The 4.5.2 maintenance notes also include a TileSet-atlas boundary fix, another reason to rerun representative level fixtures on supported patch releases (S014).
- **Headless testing:** GUT’s CLI returns a process status and can export JUnit, but its documentation says pending tests do not change the return value. gdUnit4 provides CLI suites, HTML/JUnit reports, and exit codes that distinguish failures from warnings; its Scene Runner can simulate scene frames and inputs for integration tests. Both are viable tools to study, not reasons to discard the existing custom fixture battery without a measured comparison (S016–S023).
- **CI/export:** Godot documents `--headless`, `--import`, `--export-release`, and `--export-pack`; exports require a configured preset and installed templates. `.godot/export_credentials.cfg` is sensitive and should not be committed, unlike `export_presets.cfg`. Upstream Godot CI checks exported packs and runs project/package scenarios under Xvfb, capturing output; this supports a staged import → export → launch/visual-smoke gate, not just “export command exited” (S006–S008, S024).
- **Replay/physics:** physics runs on fixed ticks (60 ticks/s by default), and interpolation smooths rendering between ticks; neither fact promises deterministic physics. Treat exact state hashes as an experiment to measure, not an engine guarantee. Prefer recording input plus explicit gameplay invariants, retain divergences, and separate simulation from rendering assertions (S009–S011, S025).

## Curated source registry

All source rows were opened in this session. `used-by` remains `—` because none of these pages has yet been cited by a lane knowledge or lesson path; proposed candidates below are not admitted corpus entries. `S015` is retained as a rejected source because its pre-release status makes it unsuitable as normative guidance for current stable behavior.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Godot release policy — [docs](https://docs.godotengine.org/en/stable/about/release_policy.html) | docs | A | Supported-branch lifecycle and compatibility guidance; patch updates are recommended, while minor upgrades require testing. | watch | 2026-10-19 | on-release | — |
| S002 | TileMapLayer class — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/classes/class_tilemaplayer.html) | docs | A | Current TileMapLayer API, batched updates, physics/rendering quadrants, RID-to-cell precision, and serialized cell bounds. | watch | 2026-10-19 | on-release | — |
| S003 | TileMap class — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/classes/class_tilemap.html) | docs | A | TileMap is deprecated; use separate TileMapLayer nodes and the editor’s extraction tool to migrate layers. | queued | 2026-10-19 | on-release | — |
| S004 | Using TileMaps — [Godot 4.5 guide](https://docs.godotengine.org/en/4.5/tutorials/2d/using_tilemaps.html) | docs | A | Layer organization, reusable external TileSets, rendering/physics/navigation settings, and pitfalls such as stacked navigation. | queued | 2026-10-19 | on-release | — |
| S005 | Upgrading from Godot 4.4 to 4.5 — [migration guide](https://docs.godotengine.org/en/4.5/tutorials/migrating/upgrading_to_godot_4.5.html) | docs | A | Physics chunking changes TileMapLayer body-RID coordinate precision; size 1 restores exact cell coordinates. | queued | 2026-10-19 | on-release | — |
| S006 | Command line tutorial — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html) | docs | A | Headless, editor import, export, test, rendering, and bounded-run CLI options; unknown options may be silently ignored. | watch | 2026-10-19 | on-release | — |
| S007 | Exporting projects — [Godot stable docs](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html) | docs | A | Export presets and templates, CLI output paths, resource inclusion, and the boundary between public presets and confidential credentials. | watch | 2026-10-19 | on-release | — |
| S008 | Import process — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html) | docs | A | Imported resources are internalized; commit `.import` metadata, avoid committing `.godot/`, and use ResourceLoader for imported assets. | watch | 2026-10-19 | on-release | — |
| S009 | Physics introduction — [Godot stable docs](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html) | docs | A | Godot physics is not deterministic; collision object types, layers/masks, and physics-process boundaries guide test design. | watch | 2026-10-19 | on-release | — |
| S010 | Physics interpolation introduction — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/tutorials/physics/interpolation/physics_interpolation_introduction.html) | docs | A | Physics ticks and rendered frames differ; interpolation smooths fixed-tick transforms and can add visual/input delay. | watch | 2026-10-19 | on-release | — |
| S011 | Using InputEvent — [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/tutorials/inputs/inputevent.html) | docs | A | Input routing order, GUI consumption, gameplay `_unhandled_input()`, InputMap actions, and synthetic event parsing. | queued | 2026-10-19 | on-release | — |
| S012 | Godot 4.6 release — [official release page](https://godotengine.org/releases/4.6/) | docs | A | 2D batching redesign and rotatable scene tiles; performance claims are scoped to tested GPU-bound scenarios. | watch | 2026-10-19 | on-release | — |
| S013 | Godot 4.6.1 maintenance release — [official release notes](https://godotengine.org/article/maintenance-release-godot-4-6-1/) | docs | A | Patch-release contents and upgrade advice; confirms physics/rendering/platform fixes land in maintained patch releases. | queued | 2026-10-19 | on-release | — |
| S014 | Godot 4.5.2 maintenance release — [official release notes](https://godotengine.org/article/maintenance-release-godot-4-5-2/) | docs | A | Supported-branch backports include a TileSet atlas tile-boundary fix and rendering/platform corrections. | queued | 2026-10-19 | on-release | — |
| S015 | Godot 4.5 dev 1 snapshot — [official pre-release article](https://godotengine.org/article/dev-snapshot-godot-4-5-dev-1/) | docs | A | Rejected for current normative use: this pre-release article is historical; use stable 4.7 class/migration docs for behavior. | rejected | 2026-10-19 | — | — |
| S016 | GUT 9.6.1 overview — [official docs](https://gut.readthedocs.io/en/v9.6.1/index.html) | docs | A | GUT version family mapping, Godot 4 orientation, and test feature index. | watch | 2026-10-19 | on-release | — |
| S017 | GUT repository at v9.6.0 — [maintainer README](https://github.com/bitwes/Gut/tree/v9.6.0) | code | A | Version matrix, minimum Godot versions, GDScript testing features, CLI, and JUnit export. | queued | 2026-10-19 | on-release | — |
| S018 | GUT 9.6.0 command line — [official guide](https://gut.readthedocs.io/en/v9.6.0/Command-Line.html) | docs | A | CLI suite selection and exit status; pending tests do not alter the process return value. | watch | 2026-10-19 | on-release | — |
| S019 | GUT 9.6.1 result export — [official guide](https://gut.readthedocs.io/en/v9.6.1/Export-Test-Results.html) | docs | A | JUnit XML result export and stable output-path/timestamp configuration for CI aggregation. | queued | 2026-10-19 | on-release | — |
| S020 | gdUnit4 command-line tool — [official docs](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd/) | docs | A | Run selected suites, store HTML/JUnit reports, and distinguish success, test failure, and warning exit codes. | watch | 2026-10-19 | on-release | — |
| S021 | gdUnit4 Scene Runner — [official docs](https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/sceneRunner/) | docs | A | Scene integration tests can simulate frames, time factors, and input events while inspecting scene state. | watch | 2026-10-19 | on-release | — |
| S022 | gdUnit4-action — [official project README](https://github.com/godot-gdunit-labs/gdUnit4-action) | docs | A | Official CI action configures Godot/add-on versions, test paths, timeouts, warning policy, reports, and GDScript/C# runs. | watch | 2026-10-19 | on-release | — |
| S023 | gdUnit4-action PR workflow — [official workflow source](https://raw.githubusercontent.com/godot-gdunit-labs/gdUnit4-action/master/.github/workflows/ci-pr.yml) | code | A | Compatibility matrix tests multiple Godot/add-on versions and asserts incompatible combinations fail explicitly. | watch | 2026-10-19 | on-release | — |
| S024 | Godot upstream project-export CI action — [pinned source](https://raw.githubusercontent.com/godotengine/godot/df623583/.github/actions/godot-project-export/action.yml) | code | A | Engine CI imports/exports packs, launches exported/package scenarios, captures output under Xvfb, and checks logs/artifacts. | queued | 2026-10-19 | on-release | — |
| S025 | Godot physics replay issue 112976 — [official tracker discussion](https://github.com/godotengine/godot/issues/112976) | community | B | Maintainer discussion and a user reproduction describe same-build 2D rerun divergence around moving bodies and reload timing; treat as a lead, not a guarantee. | queued | 2026-10-19 | 90d | — |

## Candidate knowledge entries

All entries below are proposals, not admitted findings. Each needs an executable fixture, a discriminating negative control, bounded serial replay, and non-author verification under the lane protocol. Known seed discipline is cited; actual `corpus/QUALITY.md` is absent, so none can be certified as passing that gate.

### Candidate C1 — `tilemaplayer-physics-quadrant-attribution`

- **Falsifiable claim:** For a TileMapLayer contact fixture, `physics_quadrant_size = 1` disables physics chunking and permits exact cell attribution through `get_coords_for_body_rid()`; higher quadrant sizes can make that attribution less precise. Fixture should exercise authored cell metadata and real runtime contact, then compare exact attribution at size 1 with default chunking; include collision-disabled negative control.
- **Source and exact location:** S002, *TileMapLayer → Property Descriptions → physics_quadrant_size*: “Within a physics quadrant, cells with similar physics properties are grouped together and their collision shapes get merged.” S005, *Behavior changes → TileMapLayer*, documents the 4.4-to-4.5 coordinate change.
- **Coverage row filled:** Existing level/tile collision and TileMapLayer fixture surface (`corpus/README.md:11–13`); proposed Frontier topic: chunked collision/RID attribution across engine versions (no existing `## Frontier` heading found).
- **Recheck:** S002 `physics_quadrant_size` and `get_coords_for_body_rid()`; S005 `Behavior changes → TileMapLayer`. Execute the paired settings as a new fixture before admitting the knowledge claim.
- **QUALITY fit:** Proposed positive/negative runtime fixture matches the known seed requirement for a discriminating negative (`corpus/knowledge/seed.md:11–13`), but clearance against the missing `corpus/QUALITY.md` is unknown.

### Candidate C2 — `physics-replay-determinism-boundary`

- **Falsifiable claim:** Fixed-rate physics, fixed-FPS capture, and a repeated input stream do not establish bit-identical physics state across Godot runs; the engine explicitly provides no such determinism guarantee. Replay fixtures should state gameplay invariants and record divergent observations rather than silently retrying until a matching state appears.
- **Source and exact location:** S009, *Physics introduction → Warning*: “Physics in Godot, regardless of physics engine, is not deterministic.” S010, *Physics ticks and rendered frames*, explains fixed ticks/interpolation; S025 is a bounded reproduction lead, not normative evidence.
- **Coverage row filled:** Existing causal input/physics/contact regression surface (`corpus/README.md:12–13`); proposed Frontier topic: repeat-run replay invariants and divergence reporting.
- **Recheck:** S009 Warning and S010 *Physics ticks and rendered frames*; proposed fixture replays the same recorded actions in separate bounded runs and reports exact state plus a predeclared gameplay invariant. Do not turn documentation into an untested deterministic claim.
- **QUALITY fit:** Preserve the lane’s bounded-run, serial-only, and failure-retention discipline (`corpus/knowledge/seed.md:10,14,18`); actual quality admission cannot be checked without `corpus/QUALITY.md`.

### Candidate C3 — `clean-checkout-import-export-launch-gate`

- **Falsifiable claim:** A green export command is insufficient evidence that the exported game starts; a clean-checkout CI gate must verify the configured preset/template, import resources, export the target, then launch the resulting artifact and retain diagnostics. Add a missing-preset negative and assert it fails with the expected diagnostic.
- **Source and exact location:** S007, *Exporting from the command line*: “Exporting from the command line still requires an export preset to define the export parameters.” S006 documents `--import` and export CLI; S024’s source separately exports and runs folder/package scenarios.
- **Coverage row filled:** Existing scratch export and launch cases (`corpus/README.md:11,15–16`); proposed Frontier topic: reproducible clean-checkout release pipeline, templates, imports, and artifact startup.
- **Recheck command:** For a project whose preset is named `Linux`, `godot --headless --path "$PROJECT" --export-release "Linux" "$OUTPUT"`; first run the documented editor import step and then launch/capture the produced artifact. The missing-preset control must fail, not be counted as a successful export.
- **QUALITY fit:** A bounded positive artifact launch plus a discriminating configuration-negative follows known fixture discipline (`corpus/knowledge/seed.md:10–13`); certification against `corpus/QUALITY.md` is blocked by that file’s absence.

### Candidate C4 — `runner-exit-warning-and-pending-contracts`

- **Falsifiable claim:** A test gate that checks only the process exit code can miss pending GUT tests; gdUnit4 separately reports test-failure and warning statuses. A framework adapter must record suite/pending/warning counts and preserve JUnit output, not normalize these frameworks to one assumed status contract.
- **Source and exact location:** S018, *Command Line → Return code note*: “pending doesn’t affect the return value.” S020, *Return Codes* and *The Report*, documents separate failure/warning codes and HTML/JUnit outputs; S019 covers GUT JUnit export.
- **Coverage row filled:** Existing executable fixture battery (`corpus/README.md:3`) but no named GUT/gdUnit integration; proposed Frontier topic: runner-neutral CI gate semantics and result retention.
- **Recheck:** S018 *Options/Run Options* and return-code note; S020 *Return Codes* and *The Report*. Add one pending GUT case, one failing case, and one gdUnit4 warning case as framework probes before choosing an adapter.
- **QUALITY fit:** The proposal makes failure and warning controls observable, aligning with the seed’s false-PASS and diagnostic rules (`corpus/knowledge/seed.md:11–13`); actual gate requirements are unknown without `corpus/QUALITY.md`.

### Candidate C5 — `renderer-pinned-2d-visual-canary`

- **Falsifiable claim:** Headless logical fixture success does not establish rendered 2D output; Godot 4.6 changed 2D batching, so visible regressions/performance must be measured in a graphical, renderer-pinned canary and not inferred from a cross-driver byte hash. Keep assertions scoped to an explicit renderer/engine baseline.
- **Source and exact location:** S012, *Massive optimizations to the 2D renderer*: “we did a huge overhaul to the design of our 2D renderer to reduce the GPU performance cost when batching.” S024 demonstrates upstream capture and artifact checks in a controlled Xvfb job.
- **Coverage row filled:** Explicitly unprobed rendered camera, UI, and animation surfaces (`corpus/README.md:7–10`); proposed Frontier topic: controlled 2D screenshots/rendered motion/performance canary.
- **Recheck:** S012 *Massive optimizations to the 2D renderer* and S024 “Run project files from folder”/“Run exported project PCK/ZIP”; implement a graphical canary with a pinned renderer and deliberate baseline/control before asserting pixel or performance results.
- **QUALITY fit:** The test separates render proof from headless logic proof and requires an explicit control. Whether the actual lane admission bar allows visual hashes or performance thresholds cannot be determined without `corpus/QUALITY.md`.

## Paths

- **TileMap migration and collision attribution** — S004 → S003 → S005 → S002: start with authored layer workflow, understand deprecation/migration, then test the current chunking API and exact cell-attribution boundary.
- **Replay invariants without overstating determinism** — S011 → S010 → S009 → S025: define what input is replayed, separate physics ticks from rendering, read the engine guarantee, then use the issue only as an experiment lead.
- **From test runner to shipped artifact** — S020 → S021 → S018 → S019 → S006 → S008 → S007 → S024: compare integration/CLI reporting semantics, make resource import explicit, export with named configuration, then verify package launch and captured output.

## Rejected candidates

- **“Fixed timestep means deterministic replay.”** Rejected: official physics docs explicitly reject the guarantee; interpolation addresses visual smoothness, not replay determinism (S009–S010).
- **“Require cross-renderer exact screenshot hashes as the default 2D gate.”** Rejected: renderer behavior changes across supported releases and the upstream image checks run in a controlled Xvfb pipeline; use a pinned graphical baseline, not a universal cross-driver hash (S012, S024).
- **“Replace the custom fixture battery with GUT or gdUnit4 before a comparison.”** Rejected: the local corpus already has a bespoke fixture/verifier practice; framework documents establish capabilities, not a need to discard proven lane tooling (corpus/README.md:3–24; S016–S023).
- **“Treat the 4.5-dev snapshot or its performance headline as the current production contract.”** Rejected: it is pre-release history, whereas current stable documentation and support policy supersede it; vendor performance results are scoped to tested scenes (S001, S012, S015).

## Mistakes mined from existing lane evidence

- **Early `assert(false)` could hang a negative fixture;** the seed records `quit(1)` instead. Captured by the standing fixture rule in `corpus/knowledge/seed.md:11`.
- **Parallel fixture launches caused frame flakiness;** the seed therefore makes PASS evidence serial-only. Captured by the standing rule in `corpus/knowledge/seed.md:14`.
- **A non-discriminating negative could false-PASS a broken baseline;** the seed requires a targeted diagnostic for a failing mutant. Captured by the standing rule in `corpus/knowledge/seed.md:12`.

The specified `SKILL.md` and `corpus/QUALITY.md` are absent, so these mistakes cannot be checked against those documents or used to certify a candidate admission bar. The available seed does record the three rules; no extra quality rule is inferred here.

## Contract defects found

- **Missing lane understanding file:** `SKILL.md` was not present at the named lane path. Check: `test -f SKILL.md`.
- **Missing quality gate:** `corpus/QUALITY.md` was not present at the named lane path. Check: `test -f corpus/QUALITY.md`.
- **Missing Frontier map section:** the heading sweep of `corpus/README.md` found no `## Frontier`, although the expected lane shape calls for coverage map plus Frontier rows. Check: `grep -cE '^## Frontier$' corpus/README.md`.

No conclusion is made about branch/HEAD, scorecard, log, or git cleanliness; those are outside this ART read-only scope. `corpus/SOURCES.md` is a wave-2 registry deliverable, not counted as a defect here.

## Census commands

- Source rows: **25** — `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-game-dev-2d-art.md`
- Tier A rows: **24** — `grep -cE '^\| S[0-9]{3} \|[^|]*\|[^|]*\| A \|' local://kaika-w1-game-dev-2d-art.md`
- Tier B rows: **1** — `grep -cE '^\| S[0-9]{3} \|[^|]*\|[^|]*\| B \|' local://kaika-w1-game-dev-2d-art.md`
- Tier C rows: **0** — `grep -cE '^\| S[0-9]{3} \|[^|]*\|[^|]*\| C \|' local://kaika-w1-game-dev-2d-art.md || true`
- Candidate knowledge entries: **5** — `grep -cE '^### Candidate C[1-5] — ' local://kaika-w1-game-dev-2d-art.md`
- Mistakes mined: **3** — `grep -cE '^- \*\*(Early|Parallel|A non-discriminating)' local://kaika-w1-game-dev-2d-art.md` counts the three entries under “Mistakes mined from existing lane evidence.”
- Contract defects: **3** — `grep -cE '^- \*\*(Missing lane understanding file|Missing quality gate|Missing Frontier map section)' local://kaika-w1-game-dev-2d-art.md` counts the three entries under “Contract defects found.”
