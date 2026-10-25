# Mado ART dossier — Wayland desktop, 2025–2026

**Prepared:** 2026-10-19. **Lane:** mado (desktop & compositor craft). **Scope:** external current art, not a host-health report. No upstream fact below asserts that this machine advertises, implements, or uses the cited behavior. This dossier is research material for later curation; its source rows are queued or watch, not admitted knowledge. No lane repo or live session was changed or probed.

**Research axes:** (1) primary-source authority and currentness; (2) usefulness within mado’s read-only boundary, keeping upstream protocol guarantees separate from host observations.

## Uncovered ground

- **Observed local boundary:** `PROVINCE.md:3-16` makes mado’s domain the desktop/compositor configuration plane (Hyprland, Waybar, Walker, terminals, themes and display behavior); all configuration trees are read-only, and live compositor state is not to be mutated. `SKILL.md:173-244` gives the corresponding measurement and safety fence.
- **Observed corpus coverage:** `corpus/README.md:10-33,47-64` indexes host-specific Hyprland configuration, binds/rules, live verification, Waybar/Walker, terminals, themes, idle/lock and Omarchy evidence. Those routes explicitly distinguish dated measurements from live truth. Its `## Frontier` (`corpus/README.md:66-84`) leaves rendering, dispatcher/rule effects, idle/lock transitions and other declared unknowns open.
- **Observed portal foothold:** the playbook names the Hyprland screen-share picker (`SKILL.md:73-75`) and has a read-only config/debug route (`SKILL.md:100-108,217-239`); it does not establish portal request success or a protocol-wide support inventory.
- **Uncovered seam [INFERENCE]:** the indexed evidence is primarily “what this host declares / what its approved read probes report.” It contains no linked study note for the contemporary upstream protocol lifecycle, compositor-advertised globals, standardized-versus-compositor-specific output management, portal frontend/backend routing, or a kernel-input-to-Wayland debugging ladder. These are complementary to the existing configuration plane, not permission to infer host behavior from release notes.
- **Admission implications:** the lane’s bar requires falsifiable source-cited claims, separation of observation/inference/unknown, append-only corrections, and retained rejections (`corpus/QUALITY.md:3-8`). A future entry should label external documentation as documentation and keep any host result separately version-pinned; a configuration declaration or global advertisement is not an end-to-end functional test.

## Current art — 2025–2026

| Surface | Current evidence opened in this session | Why it matters to mado |
|---|---|---|
| Hyprland releases/config | The official v0.55 announcement calls Lua the new configuration path; the companion migration note says old hyprlang continues temporarily and is selected at startup. The v0.55 release also lists removals/moves of options and ICC color-management work. The v0.56 announcement highlights expanded Lua/workspace and monitor APIs, interactive XDG drags and other changes. The opened release feed surfaces v0.56.2 (2026-08-05), whose patch notes include a toplevel-capture software-cursor fix. Sources S001–S004. | A `.conf` file, a version pin, and the new docs’ preferred syntax must not be conflated. Existing local notes are pinned to Hyprland 0.56.2 (`SKILL.md:20-25`); version-specific docs and supported syntax need a recheck before re-use. |
| wlroots | Maintainer Simon Ser’s 2025-05-15 release note says wlroots 0.19 added color-management-v1 and ext-image-copy-capture-v1, fully supported explicit synchronization, and still had backend/renderer color-management pieces under review. The official 0.20.0 release (2026-03-26) adds Vulkan renderer/backend/scene-graph support for color-management-v1 and color-representation-v1, ext-workspace and foreign-toplevel image-capture-source support, and deprecates the older wlr-screencopy-v1/data-control-v1 implementations. Sources S017–S018. | Separate protocol implementation, renderer/backend path, and working display outcome. The 0.20 release details mark progress since 0.19, but still do not prove any host compositor/GPU path. |
| wayland-protocols | The opened official announcements show a clear change stream: 1.45 (2025-06-13) adds staging background-effects and pointer-warp protocols plus experimental session-management/input-method work; 1.46 and 1.47 carry color-management and input/text-input updates; 1.48 (2026-04-01) adds staging XDG session management and a minor text-input update, with experimental `xx-` work; 1.49 (2026-06-07) adds multi-GPU linux-dmabuf and Windows BT.2100 color descriptions, plus experimental fractional scaling. Sources S009–S016. | Version numbers and phase are part of the evidence. The project README distinguishes experimental, staging and stable; a release freezes protocols at that release’s state. A “staging” directory is not a runtime advertisement or stable API promise. |
| Output management / color | The current wlroots `wlr-output-management-unstable-v1` XML remains explicitly experimental (manager/head version 4 in the opened file) and limits its purpose to output configuration; the generated wlroots API documents test/apply feedback and setting a current configuration. Hyprland’s current monitor docs separately describe compositor config fields, including ICC/color-management/HDR options. Sources S006, S019–S020. | Keep user-configured monitor rules distinct from a client-facing protocol for changing outputs; treat `zwlr_*` as versioned experimental API, not generic stable Wayland output metadata. |
| Portals and capture | The current XDG portal overview describes a shared D-Bus frontend with desktop-specific backends. `portals.conf` routes each interface; Hyprland’s portal guide says XDPH does not implement FileChooser and documents GTK fallback/routing and portal-service debugging. ScreenCast v6 has a CreateSession → SelectSources → Start → PipeWire flow; it deprecates node-ID stream targeting in favor of `pipewire-serial`/`PW_KEY_TARGET_OBJECT`. Sources S008, S024–S030. | A running portal process or valid `xdph.conf` does not prove which backend served an app or that screen capture succeeded. Separate request, user consent, backend choice and stream connection. |
| Input and compositor debugging | Wayland’s architecture docs place input routing and KMS/display control in the compositor. The official debugging page recommends `wayland-info` for advertised globals and documents `WAYLAND_DEBUG` plus protocol-dumper options. libinput’s helper docs distinguish kernel/libinput inventory and `debug-events`, and warn that `list-devices` reports libinput defaults, not desktop settings. Sources S021–S023. | Triage must identify which layer a probe can actually observe. The “libinput default” is not a compositor-applied value; protocol visibility is not proof of pixels or input behavior. |

## SOURCES.md candidate registry

Each row is a claim about what the opened source teaches, not an assertion that mado has incorporated it. Tiers are A because these are specifications, primary project documentation/releases, source or maintainer publications. `queued` means opened and worth mining; `watch` means a fast-moving source to recheck on release/change. Nothing is marked `mined` because no knowledge entry in the lane repo has yet cited it.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Hyprland v0.55.0 — https://github.com/hyprwm/Hyprland/releases/tag/v0.55.0 | docs | A | Release-level changes, option removals/moves, ICC pipeline, device tags and compositor behavior to check before carrying old config-era claims forward. | watch | 2026-10-19 | on-release | — |
| S002 | Hyprland 0.55 release announcement — https://hypr.land/news/update55/ | docs | A | Maintainer’s overview of Lua configuration, user-defined layouts, ICC profiles and renderer/color-management changes. | watch | 2026-10-19 | on-release | — |
| S003 | Hyprland 0.56 release announcement — https://hypr.land/news/update56 | docs | A | Current release highlights include Lua API expansion, monitor/workspace APIs, XDG interactive drags and no breaking changes in this release. | watch | 2026-10-19 | on-release | — |
| S004 | Hyprland v0.56.2 — https://github.com/hyprwm/Hyprland/releases/tag/v0.56.2 | docs | A | Patch-release evidence includes a toplevel-capture software-cursor fix; use the release’s exact version rather than extrapolating from current main. | watch | 2026-10-19 | on-release | — |
| S005 | Hyprland Crashes and Bugs — https://wiki.hypr.land/crashes-and-bugs/ | docs | A | Current logging guidance: enable debug logs/OpenGL messages only as needed, and turn them off because they negatively affect performance. | queued | 2026-10-19 | 90d | — |
| S006 | Hyprland Monitors — https://wiki.hypr.land/configuring/core/monitors/ | docs | A | Monitor configuration field meanings and defaults, including mode, scale, position, ICC profile, color-management/HDR and VRR fields. | queued | 2026-10-19 | 90d | — |
| S007 | Hyprland Devices — https://wiki.hypr.land/Configuring/Advanced-and-Cool/Devices/ | docs | A | Per-device configuration guidance; the current page says hyprlang is deprecated in favor of Lua since 0.55 and points to the older syntax separately. | queued | 2026-10-19 | 90d | — |
| S008 | xdg-desktop-portal-hyprland — Hyprland Wiki — https://wiki.hypr.land/Hypr-Ecosystem/xdg-desktop-portal-hyprland/ | docs | A | XDPH’s documented role, file-picker limitation, backend routing/fallback, and read-oriented debugging hints for the service. | queued | 2026-10-19 | 90d | — |
| S009 | wayland-protocols README — https://gitlab.freedesktop.org/wayland/wayland-protocols/-/raw/main/README.md | docs | A | Defines experimental/staging/stable phases, compatibility expectations, directory meanings, and the fact that each release freezes protocol state. | watch | 2026-10-19 | on-release | — |
| S010 | wayland-protocols governance — https://gitlab.freedesktop.org/wayland/wayland-protocols/-/raw/main/GOVERNANCE.md | docs | A | Specifies namespace, review, implementation and approval requirements for inclusion and stable promotion. | queued | 2026-10-19 | 90d | — |
| S011 | wayland-protocols 1.45 announcement — https://lore.freedesktop.org/wayland-devel/aEw0AP7h6T8l11ug@gmail.com/ | docs | A | Enumerates the two new staging protocols and the separate experimental session-management/input-method work in this release. | watch | 2026-10-19 | on-release | — |
| S012 | wayland-protocols 1.46 announcement — https://lore.freedesktop.org/wayland-devel/AzTKh6JewwfUBFKaOS86DT4obISpv5b5bjFghXGwYrMPyk6Wxpz6H4_trRcEOyF9VpVV-0p1-UTNv7_esjO6ppw5SyIyGxWB8R5xI_SJYfA=@emersion.fr/ | docs | A | Records color-management clarifications and further experimental input-method/text-input work. | watch | 2026-10-19 | on-release | — |
| S013 | wayland-protocols 1.47 announcement — https://lore.freedesktop.org/wayland-devel/aUAqqkhyv6-OKvUo@gmail.com/ | docs | A | Records a minor color-management update and the deprecation of the sRGB piece-wise transfer-function entry. | watch | 2026-10-19 | on-release | — |
| S014 | wayland-protocols 1.48 announcement — https://lore.freedesktop.org/wayland-devel/ac0NAPBFafhcgzE3@gmail.com/ | docs | A | Adds staging XDG session management and text-input changes, and names the concurrent experimental protocols. | watch | 2026-10-19 | on-release | — |
| S015 | wayland-protocols 1.49 announcement — https://lore.freedesktop.org/wayland-devel/Sb0TL9RxdBgNMuAKZmlfhbXVQoqGTjMaoqWmu6S_JBcYNv7Aw82KvaXX5zHaBpjfl7aF9nzz1hSgtYxQalwMUTiOpritlvtoo_Q-wQCX9EU=@emersion.fr/ | docs | A | Documents multi-GPU linux-dmabuf, Windows BT.2100 descriptions and an experimental fractional-scaling protocol; records the wayland-scanner requirement. | watch | 2026-10-19 | on-release | — |
| S016 | Wayland release news — https://wayland.freedesktop.org/releases.html | docs | A | Official release timeline cross-links dated Wayland, wayland-protocols and Weston releases; useful for version/date rechecks. | watch | 2026-10-19 | on-release | — |
| S017 | Status update, May 2025 — Simon Ser — https://emersion.fr/blog/2025/status-update-76/ | docs | A | Maintainer’s wlroots 0.19 release context: color-management protocol support is not complete renderer/backend HDR support, while image-copy capture and explicit synchronization are noted. | watch | 2026-10-19 | on-release | — |
| S018 | wlroots 0.20.0 release — https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/0.20.0 | docs | A | Official 0.20.0 release lists Vulkan color-management/color-representation support, ext-workspace and capture-source support, and deprecation of wlr-screencopy-v1/data-control-v1. | watch | 2026-10-19 | on-release | — |
| S019 | wlroots output-management API — https://wlroots.pages.freedesktop.org/wlroots/wlr/types/wlr_output_management_v1.h.html | docs | A | Documents compositor-side output-manager configuration, test/apply signals and success/failure feedback. | queued | 2026-10-19 | 90d | — |
| S020 | wlr-output-management protocol XML — https://gitlab.freedesktop.org/wlroots/wlroots/-/raw/master/protocol/wlr-output-management-unstable-v1.xml | spec | A | Defines output heads and configuration requests; explicitly labels the API experimental and limits it to output-configuration purposes. | watch | 2026-10-19 | on-release | — |
| S021 | Wayland Architecture — https://wayland.freedesktop.org/docs/book/Architecture.html | book | A | Explains the compositor’s role in input routing, KMS control, client buffers and display composition. | queued | 2026-10-19 | 90d | — |
| S022 | Wayland debugging extras — https://wayland.freedesktop.org/extras.html | tool | A | Describes what `wayland-info` observes, `WAYLAND_DEBUG`, and protocol-dumping/proxy tools. | queued | 2026-10-19 | 90d | — |
| S023 | libinput helper tools — https://wayland.freedesktop.org/libinput/doc/latest/tools.html | tool | A | Distinguishes device/kernel inventory, event observation, recording and the default-settings limitation of `list-devices`. | queued | 2026-10-19 | 90d | — |
| S024 | XDG Desktop Portal documentation — https://flatpak.github.io/xdg-desktop-portal/docs/ | docs | A | Describes the portal frontend/backend model and links app- and desktop-developer API guidance. | queued | 2026-10-19 | 90d | — |
| S025 | portals.conf — https://flatpak.github.io/xdg-desktop-portal/docs/portals.conf.html | docs | A | Defines per-desktop configuration and interface-specific backend selection; backend routing is not a compositor protocol guarantee. | queued | 2026-10-19 | 90d | — |
| S026 | Portal Requests — https://flatpak.github.io/xdg-desktop-portal/docs/requests.html | docs | A | Documents asynchronous request handles and the later Response signal following user interaction. | queued | 2026-10-19 | 90d | — |
| S027 | ScreenCast portal — https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html | spec | A | Documents ScreenCast v6 session flow, source/cursor choices, persistence and safer PipeWire stream targeting. | watch | 2026-10-19 | on-release | — |
| S028 | RemoteDesktop portal — https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.RemoteDesktop.html | spec | A | Documents user-granted remote input devices, session persistence, ScreenCast integration and EIS as the recommended input method. | watch | 2026-10-19 | on-release | — |
| S029 | xdg-desktop-portal 1.21.0 — https://github.com/flatpak/xdg-desktop-portal/releases/tag/1.21.0 | docs | A | Tagged release notes include Global Shortcuts `ConfigureShortcuts` and activation-token changes; the GitHub page marks this tag pre-release. | watch | 2026-10-19 | on-release | — |
| S030 | xdg-desktop-portal 1.22.0 — https://github.com/flatpak/xdg-desktop-portal/releases/tag/1.22.0 | docs | A | Release fixes cover Dynamic Launcher icon handling and Document Portal path resolution for FileChooser/OpenURI. | watch | 2026-10-19 | on-release | — |

## Candidate knowledge entries

These are candidates, not admitted facts about the host. Each can clear the probation quality bar only if the resulting entry preserves its cited source, falsifiable claim and evidence class, separates any host read from upstream documentation, and leaves unknown runtime behavior unknown (`corpus/QUALITY.md:3-8`).

### C1 — `hyprland-lua-config-era.md`

- **Falsifiable claim:** Hyprland’s 0.55 transition makes Lua the forward configuration surface; the project’s own migration notice says hyprlang support lasts only temporarily, and the selected config is chosen at startup. This does not by itself establish whether a particular local `.conf` is accepted by a particular installed build.
- **Source and exact location:** S002, “Old hyprlang syntax”: “The old hyprlang syntax will continue to be supported for 1 - 2 releases starting from 0.55.” (17 words.) Also S002, “Lua configs,” for startup selection.
- **Coverage/frontier filled:** Adds upstream config-era guidance to the existing Hyprland config route (`corpus/README.md:47-49`) and resolves the documentation-era risk explicitly named in `SKILL.md:344` without rewriting local config facts.
- **Recheck:** Compare the exact pinned release’s official migration/release notes, then use only `hyprctl version` and `hyprctl configerrors` for the allowed host version/load observations. Do not reload or edit as a probe (`SKILL.md:205-220`).
- **Quality gate:** Cite the versioned release and exact heading; label the promise as docs; add host config/load observations only as separately sourced observations.

### C2 — `wayland-protocol-phase-and-release-delta.md`

- **Falsifiable claim:** A wayland-protocols staging entry is encouraged for wider implementation but is not the same declaration as stable; the 1.48 and 1.49 announcements place their named additions in different phases. Verify phase against the exact tagged XML/announcement, not by protocol name or a compositor release note.
- **Source and exact location:** S009, “Protocol phases”: “After a staging protocol has been sufficiently tested in the wild and proven adequate, its maintainers and the community at large may declare it stable.” (25 words.) S014, release summary; S015, release summary.
- **Coverage/frontier filled:** New upstream-protocol lifecycle row beside the local “Hyprland config, binds, rules and display” route; extend `corpus/README.md:66-84` with protocol-version/advertised-global gaps rather than treating a corpus index as support proof.
- **Recheck:** Re-open the exact upstream release tag/README; if making a host claim, inspect the selected compositor’s globals with the read-only `wayland-info` route (S022). A supported XML version is not evidence of enabled runtime behavior.
- **Quality gate:** Keep phase, release membership, compositor advertisement and functional behavior as separate claim classes; preserve exact version/date anchors.

### C3 — `wlr-output-management-is-experimental.md`

- **Falsifiable claim:** The opened wlr-output-management-v1 protocol warns that it is experimental and permits backward-incompatible changes; its own description limits returned state to output configuration, not generic output properties.
- **Source and exact location:** S020, protocol-level description: “The protocol described in this file is experimental and backward incompatible changes may be made.” (14 words.) The same description contrasts the configuration purpose with xdg-output.
- **Coverage/frontier filled:** Deepens the existing monitor/display configuration route (`corpus/README.md:47-49`) by defining the distinct client-facing protocol boundary, version status and output of the protocol.
- **Recheck:** Re-open the current XML and the matching wlroots API page (S019); use a read-only global inventory only to establish advertisement. No client apply/test request or monitor change is a mado probe (`PROVINCE.md:10-16`).
- **Quality gate:** Source-cite the exact XML warning and never imply this wlr-specific interface is stable core Wayland or host-advertised.

### C4 — `xdg-portal-routing-and-screencast-lifecycle.md`

- **Falsifiable claim:** Portal implementation is selected per interface via portal configuration; the Hyprland XDPH guide says XDPH does not implement FileChooser; ScreenCast separates session creation, source selection, user-facing start and PipeWire access.
- **Source and exact location:** S008, “Using the KDE file picker with XDPH”: “XDPH does not implement a file picker”; S025, “DESCRIPTION”; S027, “Session lifecycle”: “Calling Start() typically presents a dialog to the user and, upon success, returns the list of PipeWire streams.” (18 words.)
- **Coverage/frontier filled:** Adds a protocol/API/backend route to the current local screen-share-picker reference (`SKILL.md:73-75`) and clarifies the existing portal/debug surface (`SKILL.md:100-108`).
- **Recheck:** Read the active `portals.conf` and desktop-specific override, and inspect portal service status/log metadata read-only. Do not prompt for screen sharing, start a capture, or infer consent or stream success from a running service.
- **Quality gate:** Include a request-flow diagram/table with each step and owning layer; distinguish D-Bus request response from backend, consent and PipeWire connection.

### C5 — `wayland-input-and-protocol-debugging-matrix.md`

- **Falsifiable claim:** `wayland-info` enumerates the selected compositor’s globals, while libinput `list-devices` describes libinput defaults rather than the desktop-applied configuration; `debug-events` is an input-event observation route.
- **Source and exact location:** S022, “Compositor features” and “Protocol dumpers”; S023, “libinput list-devices”: “This tool does not show your desktop’s configuration, just the libinput built-in defaults.” (13 words.)
- **Coverage/frontier filled:** New compositor-debugging/input lineage beside `corpus/README.md:66-84`; corrects the tendency to treat a lower-layer inventory as a live Hyprland setting, consistent with the evidence routing in `SKILL.md:117-122`.
- **Recheck:** Use `wayland-info` for advertised globals, `libinput list-kernel-devices` for kernel visibility, and `libinput debug-events` only with appropriate device access/consent. For Hyprland, keep within the documented read-only `hyprctl` whitelist; keep logs/session data shape-only where `SKILL.md:31-35,231-236` requires it.
- **Quality gate:** State the observation layer beside each command and do not upgrade global/device inventory into a claim about rendering, config, focus routing or the final on-screen outcome.

### C6 — `wlroots-capture-color-management-capability-boundary.md`
- **Falsifiable claim:** The wlroots 0.19 release context identifies color-management-v1 and ext-image-copy-capture-v1 support, while explicitly stating backend/renderer color-management parts remained under review; the 0.20.0 release documents later Vulkan renderer/backend/scene-graph color-management and color-representation support. Neither release announcement alone proves an installed compositor/GPU path works end-to-end.
- **Source and exact location:** S017, first paragraph: “color-management-v1 lays the first stone of HDR support (backend and renderer bits are still being reviewed)” (16 words.) S018, “Release highlights,” names full Vulkan color-management-v1 and color-representation-v1 support and deprecations.
- **Coverage/frontier filled:** Adds upstream display/capture implementation context to the local monitor and screen-share routes (`corpus/README.md:47-49`; `SKILL.md:65,73-75`) without claiming an installed compositor’s feature set.
- **Recheck:** Use release notes for implementation scope and the selected compositor’s read-only global list for advertisement. A full-HDR claim additionally needs a display/renderer/runtime test that is outside this research artifact.
- **Quality gate:** Preserve the version boundary and distinguish global support, renderer/backend path and observed output.

## Study paths

1. **Protocol maturity and change control:** S009 → S010 → S011 → S014 → S015. Start with phase semantics, then governance, then compare the 1.45, 1.48 and 1.49 additions; the order prevents reading “staging” as “stable.”
2. **Monitor state and output management:** S006 → S019 → S020 → S017 → S003. Begin with Hyprland’s operator-facing monitor fields, move to the wlroots server API and its experimental XML, then read implementation caveats and the compositor’s own release history. This keeps declarative config, protocol state and complete display support distinct.
3. **Screen-share and portal debugging:** S024 → S025 → S026 → S027 → S008 → S022 → S023. Learn the shared frontend, backend selection and async request lifecycle before ScreenCast’s PipeWire flow and Hyprland’s missing FileChooser; finish with low-level protocol and input tools for layer-specific diagnosis.

## Rejected candidates / mistakes mined

These are externally evidenced inference traps, not reports of incidents measured on the mado host. The rejection is retained as evidence of taste and as a prompt for future gate/quality checks.

|id|rejected claim|evidence and reason|
|---|---|---|
| M01 | “A Wayland protocol in staging is a stable, backward-compatible guarantee.” | S009 distinguishes experimental, staging and stable; S010 defines the promotion process. Reject because the phase label and version are part of the claim. |
| M02 | “`zwlr_output_manager_v1` is generic stable Wayland monitor metadata.” | S020 calls the protocol experimental and limits it to output configuration; it directs generic output-property consumers elsewhere. Reject as both a stability and scope mismatch. |
| M03 | “XDPH supplies every portal interface, including a file chooser.” | S008 explicitly says it does not implement FileChooser and describes GTK fallback/backend routing. Reject rather than inferring capabilities from the word “portal.” |
| M04 | “`libinput list-devices` proves the compositor-applied touchpad/keyboard settings.” | S023 explicitly states that the command shows libinput built-in defaults, not desktop configuration. Reject as a layer/category error. |
| M05 | “wlroots color-management-v1 support proves complete HDR end-to-end.” | S017 states renderer/backend pieces were still under review at the 0.19 release. Reject the full-path claim unless independently tested. |
| M06 | “Hyprland 0.55 immediately rejects all existing hyprlang configs.” | S002 says old syntax remains supported temporarily, while recommending migration; the migration article says the active config path is selected at startup. Reject the immediate-cutover reading; recheck the actual installed release before any host claim. |
| M07 | “The wlroots 0.19 HDR caveat still describes wlroots 0.20.0’s full color-management support.” | S017 is the 0.19 release context; S018’s 0.20.0 notes document Vulkan renderer/backend/scene-graph color-management support. Reject the stale-era carry-forward; neither upstream release proves this host’s hardware path. |

## Leads (unopened)

- Wayland Explorer’s all-protocol catalog: https://wayland.app/protocols/ — use as a navigation index only, then verify protocol phase and contents in the upstream XML/release source.
| S018 | wlroots 0.20.0 release — https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/0.20.0 | docs | A | Official 0.20.0 release lists Vulkan color-management/color-representation support, ext-workspace and capture-source support, and deprecation of wlr-screencopy-v1/data-control-v1. | watch | 2026-10-19 | on-release | — |
- xdg-desktop-portal-hyprland release/history page: https://github.com/hyprwm/xdg-desktop-portal-hyprland/releases — inspect backend capabilities by version rather than extrapolating from the project overview.
- Full Hyprland debug/contributing guide: https://wiki.hypr.land/Contributing-and-Debugging/ — the crash guide was opened, but not the full maintainer workflow, crash-report package or build-debug guidance.
- Protocol/portal Input Capture implementation status across compositors — no upstream implementation matrix or backend compatibility result was opened in this pass; verify against project sources before claiming availability.

## Counts and reproducible commands

- 30 source rows — `grep -cE '^\| S[0-9]{3} \|' local://kaika-w1-mado-art.md`
- Tier distribution: 30 A, 0 B, 0 C — `grep -E '^\| S[0-9]{3} \|' local://kaika-w1-mado-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`
- 6 candidate entries — `grep -cE '^### C[1-6] — ' local://kaika-w1-mado-art.md`
- 7 mistakes mined — `grep -cE '^\| M[0-9]{2} \|' local://kaika-w1-mado-art.md`
- All source rows were opened on 2026-10-19; the status is queued/watch and every `used-by` is `—` because these entries have not yet been admitted to `corpus/knowledge/`.
