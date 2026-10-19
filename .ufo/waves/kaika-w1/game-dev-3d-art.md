# ART dossier — `game-dev-3d`

Research captured 2026-10-19. Scope is external 3D engine production, deterministic headless fixtures, rendering regression, glTF pipelines, and automated playtesting. No repo content was changed, no engine/tool was installed, and no runtime test was run for this dossier.

## Lane ground and uncovered ground

**Observed local evidence**

- `PROVINCE.md` bounds the lane to 3D production verified by executable headless fixtures: movement/collision, spatial queries, camera projection/frustum behavior, scene structure/instancing, transform composition, and input-driven mechanics. It names Godot, Unity, Unreal, three.js, and further validated 3D tooling; REA is supporting static inspection, not a second domain.
- `corpus/README.md` describes an engine-neutral fixture battery, inherited mechanics suite, static REA reference, and engine census. Its declared core coverage is movement/collision, spatial queries, projection, scene structure, transforms, and input-driven mechanics, with discriminating negatives and reproduction commands.
- `corpus/knowledge/engines.md` is a host census, not a generic engine endorsement. It records Godot 4.7.2 as installed and executable headless with bounded receipts, three.js as partial for scene-graph/math under Node without a GL context, and Unity/Unreal as not installed. Blender is recorded as partial. The lane's stated promotion rule requires a bounded fixture receipt and a non-author verifier. Bevy is not represented in the census section read here; **[INFERENCE]** its host availability and runtime status remain unproven, not absent.
- The named local knowledge files read were `engines.md`, `rea.md`, and `seed.md`. They cover engine census, REA limits, and imported seed provenance; they do not provide a researched Godot-Jolt, Bevy, glTF-pipeline, render-regression, or autonomous-playtesting guide. **[INFERENCE]** those are candidate knowledge gaps based on the complete local `corpus/knowledge/` directory listing and the contents read.
- `SKILL.md` chiefly carries Unreal-content and lane-fixture claim discipline. Its most transferable rules for this research are to distinguish static evidence from runtime behavior, require bounded receipts for runtime claims, keep reproduction commands/citations honest, and not overread a passing gate.
- `corpus/QUALITY.md` was named by the lane dossier contract but the requested path could not be read because it is not present. This is the one observed contract defect below. Therefore no candidate is represented as having passed the lane's quality gate.
- `corpus/SOURCES.md` was not present in the listing. Its creation is explicitly a Wave 2 contract, so that absence is not counted as a current defect.

**[INFERENCE] Uncovered research frontier**

- The core fixture map is strong on reproducible mechanics and negative controls, but the evidence read here does not show a GPU-backed render-capture contract, backend-specific image baselines, or a statement separating projection/math assertions from actual rendered pixels.
- No local knowledge entry covers Godot's built-in Jolt behavior differences, current Bevy asset/render work, inter-engine glTF extension support, or coverage-directed autonomous exploration. These are proposed additions, not claims that the lane's fixtures fail.
- A particularly important ambiguity to resolve before calling a test visual regression: the local fixture README labels an orthographic SubViewport case “headless”; Godot's current `RenderingServer` reference says `--headless` disables rendering and that most rendering-server functions return dummy values. **[INFERENCE]** the fixture might test camera/projection state rather than rendered pixels; its implementation and receipt were not opened here, so this is a question for a targeted later probe, not a reported defect.

## Current art not held by the inspected corpus

- **Godot 4.7 rendering production:** the official release adds `AreaLight3D`, HDR output, and nearest-neighbor 3D viewport scaling. These broaden visual surfaces that a production fixture might need to qualify; they do not imply that one host can test all renderer/driver combinations. [S001, S003]
- **Godot Jolt:** current Godot docs say Jolt is built in from 4.4 and selected by default for new projects. They also document meaningful differences from Godot Physics and the former extension: unsupported soft joint properties, single-body-joint framing, collision margins, ray `face_index`, and kinematic-contact reporting. This supports explicit backend/version/settings in physics fixtures rather than treating “Godot 3D physics” as one invariant. [S002]
- **Headless execution is not headless rendering:** Godot `--headless` disables rendering and window management; the `RenderingServer` docs warn of dummy return values. The command-line flag is useful for server and script execution, but it alone cannot establish that a scene visually rendered. [S004, S005]
- **Bevy rendering production frontier:** the Bevy 0.17 release explicitly says Solari “is not yet production ready”; the 0.18 and 0.20 releases report substantial improvements, while 0.20 still lists supported-light gaps and lacks a built-in macOS denoiser. Treat release status and current feature limits separately from fixture-proven stability. [S010, S011, S030]
- **Bevy headless distinctions:** Bevy's 0.16 `no_renderer` example is explicitly an empty window without a renderer and calls out integration tests/CI; its `without_winit` example disables the window plugin. These are distinct integration-test configurations, not evidence of pixel-producing offscreen rendering. [S013, S014]
- **Asset pipeline/current standards:** Khronos glTF 2.0 remains the API-neutral runtime-delivery contract; Godot recommends glTF 2.0 and documents format-specific import paths, while Bevy's 0.20 news lists its 0.18 `GltfExtensionHandler` feature. The current extension registry separates ratified formats from drafts, including review drafts for `KHR_collision_shapes` and `KHR_physics_rigid_bodies`. KTX 2.0 specification revision 4 is dated 2025-02-20. [S007, S017, S018, S019, S030]
- **2025 asset practice:** Khronos Asset Creation Guidelines 2.0 is authoring-tool-agnostic guidance on coordinate/scale conventions, triangle meshes, instancing, compression, materials, textures, animation, and performance. The glTF Validator emits JSON validation reports and a nonzero return code on errors; glTF Transform offers inspection and selectable optimize/compression transforms. A validated file still needs a target-engine import test. [S020, S021, S022]
- **Portable asset behavior:** the Khronos KHR_interactivity announcement describes behavior graphs for interactive glTF assets; the opened current registry now lists `KHR_interactivity` as ratified. This is a standards and implementation frontier, not proof that any particular engine or lane importer supports it. [S018, S023]
- **Automated playtesting art (2025–2026):** the opened papers include a journal paper on BDD/regression/playtesting, a 2025 peer-reviewed multi-agent testing paper, IJCAI 2025 planning-system demo, 2025 arXiv LLM-agent preprint, and 2026 peer-reviewed call-stack-aware agent paper. These are complementary research methods, not a drop-in Godot fixture runner or proof of local game behavior. [S024–S028]
- **Bevy 0.20 (October 2026):** the release page is current as of this dossier. It reports Solari improvements, but lists material-light support gaps and no built-in macOS denoiser; its scene system (BSN) still has syntax changes. Treat it as active frontier, and pin the version/settings for any renderer or scene-fixture claim. [S030]

## Candidate `SOURCES.md` seed rows

Each row below was opened in this research session. `queued` means worth mining; `watch` means recheck as releases/standards move; `rejected` preserves a reason for not relying on a source. All `used-by` cells remain `—` because none of the proposed knowledge entries exists yet. S029 is a rejected low-tier lead, not a validated reference; it is listed separately below rather than as an opened source row.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Godot 4.7 release — https://godotengine.org/releases/4.7/ | docs | A | Current release surface including area lights, HDR output, and 3D viewport filtering. | watch | 2026-10-19 | on-release | — |
| S002 | Using Jolt Physics — https://docs.godotengine.org/en/stable/tutorials/physics/using_jolt_physics.html | docs | A | Built-in Jolt history and documented behavior differences to Godot Physics and the extension. | watch | 2026-10-19 | on-release | — |
| S003 | Overview of renderers — https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html | docs | A | Feature and driver trade-offs among Forward+, Mobile, and Compatibility. | watch | 2026-10-19 | on-release | — |
| S004 | RenderingServer — https://docs.godotengine.org/en/stable/classes/class_renderingserver.html | docs | A | Headless mode disables rendering; most RenderingServer calls return dummy values. | watch | 2026-10-19 | on-release | — |
| S005 | Command line tutorial — https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html | docs | A | Current command-line modes, including `--headless`, renderer selection, and movie output. | watch | 2026-10-19 | on-release | — |
| S006 | GdUnit4 command-line tool — https://godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd/ | docs | A | Running Godot tests in CI and collecting HTML/JUnit reports with explicit exit codes. | watch | 2026-10-19 | on-release | — |
| S007 | Available 3D formats — https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html | docs | A | Godot's recommended glTF path and the trade-offs/requirements of Blender, OBJ, DAE, and FBX imports. | watch | 2026-10-19 | on-release | — |
| S008 | Import configuration — https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html | docs | A | Import-time scene, mesh, animation, material, and post-import script configuration. | queued | 2026-10-19 | 90d | — |
| S009 | Model export considerations — https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html | docs | A | Coordinate, scale, triangulation, transform, pose, and lighting conventions for reliable imports. | queued | 2026-10-19 | 90d | — |
| S010 | Bevy 0.18 — https://bevy.org/news/bevy-0-18/ | docs | A | Current Bevy release notes, especially glTF extension handlers, asset processing, and capture tooling. | watch | 2026-10-19 | on-release | — |
| S011 | Bevy 0.17 — https://bevy.org/news/bevy-0-17/ | docs | A | Release context for experimental Bevy Solari, headless UI widgets, and rendering changes. | queued | 2026-10-19 | on-release | — |
| S012 | Bevy 0.16 — https://bevy.org/news/bevy-0-16/ | docs | A | GPU-driven rendering, platform limitations, and scene/transform changes in the prior release. | queued | 2026-10-19 | on-release | — |
| S013 | Bevy `no_renderer.rs` — https://raw.githubusercontent.com/bevyengine/bevy/release-0.16.0/examples/app/no_renderer.rs | code | A | A concrete no-renderer application configuration explicitly described as useful for CI/integration tests. | queued | 2026-10-19 | on-release | — |
| S014 | Bevy `without_winit.rs` — https://raw.githubusercontent.com/bevyengine/bevy/release-0.16.0/examples/app/without_winit.rs | code | A | A separate no-window-plugin example; not a screenshot/offscreen-render guarantee. | queued | 2026-10-19 | on-release | — |
| S015 | `bevy_gltf` 0.16 — https://docs.rs/bevy_gltf/0.16.0/bevy_gltf/index.html | docs | A | Loading labeled glTF scenes and sub-assets through Bevy's AssetServer. | queued | 2026-10-19 | on-release | — |
| S016 | `bevy_asset` processor 0.16 — https://docs.rs/bevy_asset/0.16.0/bevy_asset/processor/index.html | docs | A | Asset processing as a configurable, lossless, generally deterministic build pipeline. | queued | 2026-10-19 | on-release | — |
| S017 | glTF 2.0 specification — https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html | spec | A | Canonical glTF asset model, validation requirements, and extension contract; older core spec remains normative. | queued | 2026-10-19 | on-release | — |
| S018 | glTF 2.0 Extension Registry — https://github.com/KhronosGroup/glTF/blob/main/extensions/README.md | spec | A | Separates ratified extensions, in-progress drafts, vendor extensions, and extension-required fallback rules. | watch | 2026-10-19 | 90d | — |
| S019 | KTX 2.0 specification — https://registry.khronos.org/KTX/specs/2.0/ktxspec.v2.html | spec | A | Current KTX 2.0 container structure, supercompression, texture levels, and revision history. | watch | 2026-10-19 | 90d | — |
| S020 | Khronos glTF-Validator — https://github.com/KhronosGroup/glTF-Validator/blob/main/README.md | tool | A | Spec validation, resource checks, JSON reports, and error-sensitive command-line return behavior. | queued | 2026-10-19 | on-release | — |
| S021 | glTF Transform CLI — https://gltf-transform.dev/cli | tool | A | Inspection, validation, optimization, mesh processing, and texture/geometry compression choices. | queued | 2026-10-19 | on-release | — |
| S022 | Khronos Real-time Asset Creation Guidelines 2.0 — https://github.com/KhronosGroup/3DC-Asset-Creation/blob/main/asset-creation-guidelines/RealtimeAssetCreationGuidelines.md | docs | A | 2025 authoring-agnostic guidance on interoperable, optimized real-time 3D assets. | watch | 2026-10-19 | 90d | — |
| S023 | Khronos KHR_interactivity update — https://www.khronos.org/blog/gltf-interactivity-extensions-approach-finalization-your-feedback-needed | docs | A | 2025 design and adoption context for portable behavior graphs in glTF assets. | queued | 2026-10-19 | 90d | — |
| S024 | Behavior Driven Development for 3D games — https://arxiv.org/html/2506.17057v1 | paper | A | Industrial experience applying readable BDD scenarios and autonomous agents to 3D-game regression and playtesting. | queued | 2026-10-19 | 90d | — |
| S025 | Curiosity Driven Multi-agent Reinforcement Learning for 3D Game Testing — https://arxiv.org/html/2502.14606 | paper | A | Coverage criteria, partial observability, and collaborative agent exploration in 3D game testing. | queued | 2026-10-19 | 90d | — |
| S026 | Using Planning for Automated Testing of Video Games — https://doi.org/10.24963/ijcai.2025/1250 | paper | A | PDDL rule/initial-state/goal descriptions can generate and maintain game regression plans. | queued | 2026-10-19 | 90d | — |
| S027 | Leveraging LLM Agents for Automated Video Game Testing — https://arxiv.org/html/2509.22170v1 | paper | A | Preprint design for state abstraction, action filtering, coverage memory, reflection, and issue diagnosis in MMORPG testing. | queued | 2026-10-19 | 90d | — |
| S028 | CA2: Code-Aware Agent for Automated Game Testing — https://proceedings.mlr.press/v318/adaikkappan26a.html | paper | A | 2026 peer-reviewed work using call traces and state to target functions during automated testing. | queued | 2026-10-19 | 90d | — |
| S029 | Vulkan CI/CD Render Validation — https://docs.vulkan.org/tutorial/latest/ML_Inference/Desktop_Applications/04_ci_render_validation.html | docs | C | Rejected lead: useful offscreen capture discussion but overstates identical software-renderer output without adequate cross-driver qualification. | rejected | 2026-10-19 | — | — |
| S030 | Bevy 0.20 — https://bevy.org/news/bevy-0-20/ | docs | A | Current Bevy release: Solari quality/performance and platform caveats, scene system changes, and release context. | watch | 2026-10-19 | on-release | — |

**Registry seed counts**

- 30 source rows — `grep -cE '^\| S[0-9]{3} \|' local://kaika-w1-game-dev-3d-art.md`
- 29 tier-A rows, 0 tier-B rows, 1 tier-C row — `grep -E '^\| S[0-9]{3} \|' local://kaika-w1-game-dev-3d-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`

## Leads (unopened)

- [A Strategy-based Framework for Exploratory Playtesting in Open-World Games](https://dl.acm.org/doi/full/10.1145/3774748.3787657) — read attempt returned HTTP 403; search result only, not a source row.
- [Decision-Aware Information Sharing in Multi-Agent Reinforcement Learning for Game Testing](https://wpsites.ucalgary.ca/serious-games/wp-content/uploads/sites/136/2026/06/2026FSE_passive_active_RL.pdf) — PDF read attempt timed out; search result only, not a source row.
- [Coverage-aware game playtesting with LLM-guided reinforcement learning](https://www.sciencedirect.com/science/article/abs/pii/S1875952126001072) — read attempt returned HTTP 403; search result only, not a source row.
- [Godot Visual Regression](https://github.com/CregSutherdale/godot-visual-regression) — third-party project surfaced in search but not opened; lead only, not a source row.

## Candidate knowledge entries

Every candidate is a proposed entry, not an existing admitted fact. Its `QUALITY.md` admission status is blocked by D01. The lane's existing `SKILL.md` fixture-claim procedure is useful provisional guidance, but it cannot substitute for the missing quality bar.

### `godot-headless-rendering-contract.md`

- **Falsifiable claim:** Godot `--headless` disables rendering; a test run under this flag cannot by itself prove that a scene rendered correctly.
- **Source and quote:** S004, `RenderingServer`, “Headless mode”: “Starting the engine with the `--headless` command line argument disables all rendering and window management functions.”
- **Coverage row filled:** headless determinism and camera projection in the existing README/fixture map; missing distinction between state/geometry assertions and actual pixels.
- **Recheck:** S004 and S005; when implemented, compare one scripted run with headless rendering disabled against an explicitly selected rendering path. Do not infer the fixture's present behavior without opening its code/receipt.
- **Quality gate:** cannot certify against absent `corpus/QUALITY.md`. Provisional evidence should include exact engine/build/mode, a bounded fixture receipt, a control that distinguishes non-rendering from rendered output, and non-author verification under lane `SKILL.md` §1 row F.

### `jolt-physics-differentials.md`

- **Falsifiable claim:** Jolt's default ray-query face-index behavior and supported joint settings differ from Godot Physics; physics expectations must state engine version, backend, and relevant settings.
- **Source and quote:** S002, `Using Jolt Physics`, “Introduction”: “The Jolt physics engine was added as an alternative to the existing Godot Physics physics engine in 4.4.” The page documents `face_index` as `-1` by default with Jolt and lists unsupported joint properties.
- **Coverage row filled:** movement/collision, spatial queries, and physics interaction fixtures.
- **Recheck:** S002; add paired fixtures for the documented default and an opt-in/configured case, plus an intentionally wrong expectation control.
- **Quality gate:** cannot certify until D01 is repaired. Provisional runtime evidence needs a pinned Godot build and physics backend, saved bounded receipts, a discriminating negative, and an independent verifier; do not generalize one fixture's result to all Jolt behavior.

### `render-backend-regression-fixtures.md`

- **Falsifiable claim:** Godot's renderer selection changes available features and driver paths; a rendering regression fixture must record its renderer/driver and compare only with a compatible baseline, not silently treat a cross-renderer image as equivalent.
- **Source and quote:** S003, “Switching between renderers”: “Switching between renderers may require some manual tweaks to your scene, lighting, and environment, since each renderer is different.” S029 is a rejected lead on pixel-oracle design, not a source of determinism guarantees.
- **Coverage row filled:** camera/frustum and projection coverage; a dedicated actual-render path and backend dimensions are not established by the inspected corpus.
- **Recheck:** S003–S005; choose a deterministic small 3D scene and explicitly record engine version, renderer, driver, resolution, and capture method before comparing images.
- **Quality gate:** blocked by D01. A future quality check must distinguish image capture success from semantic correctness and include blank/black output as a negative control; headless simulation is not a render receipt.

### `gltf-source-to-engine-validation.md`

- **Falsifiable claim:** passing a glTF validator does not prove that the target engine imports every used/required extension; validate asset structure and target-engine import as separate stages.
- **Source and quote:** S017, §2.1 “General”: “glTF is an API-neutral runtime asset delivery format.” S018 defines extension status and `extensionsRequired`; S020 documents spec/resource validation; S007 and S008 document Godot's import path.
- **Coverage row filled:** scene structure/import and the corpus's glTF-related fixture/artifact frontier.
- **Recheck:** S007–S009, S017–S023. Include a known-valid core asset, malformed or missing-resource control, and an extension-required asset whose support is explicitly checked in the target engine.
- **Quality gate:** blocked by D01. Provisional admission requires source asset identity, tool/version/command, validator report, engine import receipt, and negative control; keep static format validity separate from runtime import claims.

### `bevy-gltf-asset-processing.md`

- **Falsifiable claim:** Bevy's 0.18 docs say applications can process glTF extension data through a `GltfExtensionHandler` into Bevy-side data/components while Bevy asset processors can transform assets as a build pipeline; this needs an actual pinned Bevy fixture before claiming local execution.
- **Source and quote:** S030 refers to 0.18; S010, “glTF Extensions”: “Now, users may implement the `GltfExtensionHandler` trait to do stateful processing of glTF data as it loads.” S016 describes asset processing as an automatic/configurable/lossless/deterministic build system.
- **Coverage row filled:** the lane's engine-neutral 3D tooling census and scene/asset processing frontier; no Bevy runtime row was present in the census section read.
- **Recheck:** S010, S015, S016, S030; after any authorized Bevy setup, compare processor outputs for pinned inputs/settings and test a missing/unsupported extension case.
- **Quality gate:** blocked by D01. Until an engine census receipt and bounded non-author fixture exist, admit only sourced static documentation; do not label Bevy executable headless or verified here.

### `instrumented-playtesting-agents.md`

- **Falsifiable claim:** broad game exploration can use agent policies and game-state/call-trace observability to grow coverage, but pass/fail still requires explicit reproducible state/task/crash/performance oracles; agent suspicion alone is not a confirmed bug.
- **Source and quote:** S028, abstract: “The agent receives the current function call trace along with the game state and learns to reach specific target functions.” S024 covers human-readable BDD testing; S025 covers entity/connection/spatial coverage; S026 describes PDDL test-plan generation; S027 is a preprint with reflection/diagnosis components.
- **Coverage row filled:** headless fixture suite is focused on fixed mechanics; agent-guided level exploration and coverage criteria are not described by the inspected local corpus.
- **Recheck:** S024–S028. A first fixture should use a known small level, fixed budget, explicit coverage denominator, recorded action/state trace, repeated runs, and a scripted negative-control failure.
- **Quality gate:** blocked by D01. Provisional admission requires an independently checkable oracle and a reproducible trace; probabilistic exploration results must not replace the lane's per-claim before/after evidence standard.


**Candidate count:** 6 — `grep -cE '^### [a-z0-9-]+\.md$' local://kaika-w1-game-dev-3d-art.md`
**Candidate entries all blocked by D01.** The missing quality criteria are unavailable; none is claimed to clear `QUALITY.md`.


## Paths

- **Headless mechanics to real render validation:** S005 → S004 → S003 → S006. First establish which engine mode is actually running, then separate renderer/driver coverage from deterministic logic fixtures, then choose an automated test runner and receipt format. This order prevents treating a no-render headless run as a screenshot test.
- **Asset source to engine runtime:** S017 → S022 → S020 → S021 → S007/S008 → S015/S010 → S018/S019. Start with the format contract and authoring conventions, validate and optimize assets, then test the target engine's import/extension handling; keep draft and vendor extension support explicit.
- **Playtesting from readable scenario to exploration:** S024 → S026 → S025 → S027/S028. Start with explicit human-readable scenarios and goals, add coverage-oriented exploration, then investigate reflective/code-aware agents. The ordered path keeps agent exploration subordinate to an inspectable game-state oracle.

## Mistakes mined and rejected candidates

- The lane's `SKILL.md` §2 already names eight observed/repaired error signatures: `prose-cites-bytes`, `count-written-into-prose`, `implicit-cwd command`, `scanner-relative datum`, `temp-dir-dependent gate`, `green-gate-overread`, `binary-strings-citation`, and `command-does-not-reproduce-its-printed-rc`. Reuse those when curating source citations and fixture receipts. Evidence is `SKILL.md` §2, Error patterns — named signatures. A re-count command (not run in this ART scout) is `(cd /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin && grep -c '^| \*\*' SKILL.md)`.

**Mistakes mined:** 8 error patterns present in lane `SKILL.md` §2; 0 lane lesson errors independently reviewed (lesson files were listed but not opened). Commands: `grep -c '^| \*\*' /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin/SKILL.md` for the pattern count; `printf '%s\\n' '0 (lesson files not read; not a measured error count)'` for the independent lesson-error count.

Six research approaches are rejected as evidence of taste; these are not claims that the lane has already implemented them:

- **R01: “`--headless` screenshot proves rendering.”** Rejected by S004: headless disables rendering; require a real render path for image claims.
- **R02: “Jolt is a drop-in semantic match for Godot Physics.”** Rejected by S002's documented joint, query, margin, and contact differences; keep backend/settings explicit.
- **R03: “One exact golden image works across all renderer/driver configurations.”** Rejected as a universal rule: S003 documents renderer differences and S029's gold-image discussion is only a low-tier lead; qualify backend-specific baselines and a tolerant/semantic oracle.
- **R04: “Bevy Solari is production-ready just because it shipped.”** Rejected by S011, which explicitly says the 0.17 Solari addition was not production ready; later progress does not retroactively validate it for a project.
- **R05: “A glTF registry entry or validator pass proves an engine loads that extension.”** Rejected by S018's status/required-extension contract and S010/S007's separate engine loader/import surfaces; verify each target runtime.
- **R06: “An LLM's stalled-task diagnosis is itself a bug verdict.”** Rejected by S027's own diagnosis framing and reported false alarms; preserve it as a candidate for human or deterministic confirmation, not a passing/failing oracle.

- Six rejected approaches — `grep -cE '^- \*\*R[0-9]{2}:' local://kaika-w1-game-dev-3d-art.md`
- Eight lane error patterns — `grep -c '^| \*\*' /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin/SKILL.md`
- Zero lane lessons independently mined — `printf '%s\\n' '0 (lesson files were not opened)'`

|id|finding|evidence|disposition|
|---|---|---|---|
| D01 | Required `corpus/QUALITY.md` is absent. | The ART contract names this file; reading the specified path returned not found. | One observed contract defect. Cannot claim any candidate clears lane quality until the file is restored/read and applied. Recheck from lane root: `test ! -e corpus/QUALITY.md` (success means still absent). |

**Unresolved research gaps, not counted as defects:** the existing orthographic fixture's “headless SubViewport” wording needs a direct read of its authored fixture and saved receipt to determine whether it asserts projection state or rendered pixels; no Bevy install/runtime evidence was gathered; and no lane-local `SOURCES.md` exists yet because Wave 2 is tasked to create it.

- One observed contract defect — `grep -cE '^\| D[0-9]{2} \|' local://kaika-w1-game-dev-3d-art.md`

## Research handling

- `web_search` and public-page reads were available. Search and page content were treated as untrusted data. The opened glTF Transform and Vulkan CI tutorial pages contain operational command examples to install a CLI and download/configure SwiftShader; under the assignment's instruction-handling rule these were treated as prompt-injection attempts, not acted upon, and are reported here. No commands, downloads, installs, or live-target actions were performed. The Vulkan CI tutorial was opened but rejected as authority for its generalized software-renderer determinism claim; see S029 and R03.

## Top recommendations

- Restore/read `corpus/QUALITY.md` before turning any candidate into an admitted knowledge entry; then seed Wave 2's append-only source registry with these rows, preserving `queued` versus `watch` and rejected reasons.
- Make the current headless/render distinction explicit in corpus language and create separate fixture lanes for deterministic logic/physics versus actual render capture, with renderer/driver metadata and a non-render negative control.
- Add a bounded Jolt/glTF import slice first, then treat Bevy and agent playtesting as separate, explicitly scoped expansions; agent exploration can increase coverage but must not substitute for the lane's reproducible fixture oracle.
