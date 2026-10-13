# x-connector — sibling-overlap scan (wave shokunin-train-20261013)

Seat: connector (leaf, `fleet/sibling-overlap`). Judged axes: expansion, quality, discernment.
Scan executed 2026-10-13 while the wave was in flight; all evidence below is read-only
(`git log`/`git show`/`git status`, `diff`, `grep`, file reads). No lane repo was written
by this seat; sole write is this file.

Lanes in scope (worktree cwd → canonical repo via `.shokunin/<lane>` symlink):
- audio r62-in-flight (declared axis: depth — resolve r61 SoX decode-length UNKNOWN; task `AudioR62*`)
- game-dev-2d r61-in-flight (declared axis: coverage — land tracked spontaneous-crash row from r60; task `G2dR61*`)
- game-dev-3d r70-in-flight (declared axis: depth — Euclidean-vs-path-sum discrimination via detour navmesh; task `G3dR70*`)

Fleet domain labels (`~/Projects/shokunin/MANIFEST.json` roster):
- audio: "game audio production — SFX + soundtrack, headless-verified"
- game-dev-2d: "2D game production via executable headless fixtures (Godot 4.7.2)"
- game-dev-3d: "3D game production via headless fixtures across Godot/three.js/Unity/Unreal"

---

## (a) Contested scope

### a.1 — engine-audio: audio ↔ game-dev-2d (the real overlap)

Both provinces have a defensible claim to **engine-mediated audio verification** (Godot
`AudioServer`/`AudioStreamPlayer`/`AudioStreamWAV` behavior), and neither PROVINCE.md names
the boundary.

**audio's claim is by domain, but it cannot reach the layer.**
- `audio-shokunin/PROVINCE.md` owns "game audio production — SFX (UI, impacts, movement,
  ambience) and soundtrack (motifs, loops, stems, adaptive layers) — verified by headless
  analysis: duration, loudness, spectral content, loop-seam continuity."
- Its boundary checklist (round 24) explicitly refuses engine-ward actions: "wiring adaptive
  layer selection in engine → refuse"; "export an audio-only asset into an engine directory
  → refuse"; refuses "engine source mutation" outright.
- Its toolchain census (`corpus/knowledge/seed.md`) lists ffmpeg/ffprobe/sox/aplay/pipewire/
  numpy only — no Godot. `grep -il 'godot\|AudioServer\|AudioStream'` over
  `audio-shokunin/**/*.py,*.md` → **0 hits**. The lane's verification surface is file-level
  (container/signal properties), structurally unable to observe the engine.

**game-dev-2d holds the entire engine-audio surface by occupation, unnamed in its province.**
- `game-dev-2d-shokunin/PROVINCE.md` owns "2D game production verified by executable headless
  fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness."
  The word "audio" appears in neither Owns nor Refuses.
- Yet `corpus/fixtures/` contains the fleet's only engine-audio verification:
  - `audio_playback.gd` (r12): synthesizes a 22,050-sample 440 Hz sine in GDScript into
    `AudioStreamWAV`, asserts `is_playing()` + transport-position advance > 0.001 s.
  - `audio_bus_route.gd` (r59): `AudioServer.add_bus()`/`set_bus_name`/`get_bus_index`/
    `remove_bus`; proves explicit non-Master `FixtureBus` resolves index 1, and that an
    invalid route silently falls back to `Master`/index 0 with transport advancing
    (`corpus/lessons/r59-audio-non-author.json`, SCORECARD coverage row at r59).
  - `classify_audio_process` + `--probe-audio-warning` (r14, commit `f870fd4`,
    `run_battery.py:201-209,244-259`): an audio-specific verdict layer scoping the r12
    `ObjectDB`-leak warning (`AudioStreamWAV`/`AudioStreamPlaybackWAV`) to audio fixtures.
- `corpus/lessons/r12-headless-audio.md` records the honest bound: "No audible output
  established."

**The contradiction, stated, not smoothed:** audio owns "game audio" as a subject but has
refused every path that would let it verify audio *inside* the engine; game-dev-2d owns
"executable headless fixtures" as a method and thereby holds all engine-audio evidence, but
its province never claims audio as a domain. The contested ground — Godot audio-runtime
behavior — is claimed by occupation (2d) and by domain (audio) simultaneously.

**Three concrete seams this creates:**
1. *End-to-end audio claims are unownable.* "Does `stem_layer.wav` play/route in Godot?"
   requires writing an audio artifact into an engine context — refused by audio's boundary
   checklist (destination out of scope) and unclaimed by 2d's domain (2d verifies engine
   mechanics, not audio assets). No single lane can both produce the asset and prove
   in-engine behavior.
2. *2d is producing audio content outside audio's discipline.* `audio_playback.gd` and
   `audio_bus_route.gd` each synthesize a raw signal (440 Hz sine, `FORMAT_16_BITS`,
   `mix_rate=22050`) inside 2d write scope — original audio content with zero
   audio-lane measurement (no duration/loudness/spectral/seam proxy, only engine-state
   assertions). Benign today (fixture-local test tone, not a shipped asset), but it is
   audio production happening in a lane whose province never mentions audio.
3. *Latent triple-collision: `AudioStreamPlayer3D` / positional audio.* Dimension-agnostic
   `AudioServer` plus a 3D-node player is simultaneously a natural game-dev-3d surface, an
   audio-domain subject, and adjacent to 2d's occupied engine-audio pattern. 3d currently
   has zero audio fixtures (`grep -rln 'Audio\|audio' corpus/fixtures/` → none).

**This wave: no live collision.** audio r62 is SoX decode-length mechanism depth;
2d r61 is crash-classification coverage; 3d r70 is nav-agent distance depth. The contest is
structural — it will bind on the first engine-side audio claim, not this round.

### a.2 — game-dev-2d ↔ game-dev-3d: managed, with one quarantine note

3d's province explicitly refuses "2D production scope (game-dev-2d — shared fixture patterns
are inherited, 2D product surfaces are not)." The inherited 2D-shaped material
(`corpus/predecessor/corpus/` — verbatim games-engine-mechanics r15 import at commit
`4671a6b`, per `corpus/knowledge/seed.md`) is quarantined under `predecessor/`; the active
`corpus/fixtures/` tree is entirely 3D-suffixed/three.js. Clean separation — the residual
overlap is harness architecture and the shared Godot 4.7.2 runtime, not product surface.

---

## (b) Shared-harness drift — run_battery.py

Lineage (established, not assumed):
- Upstream seed has **no** battery runner: `corpus/predecessor/corpus/` (games r15)
  contains fixtures + round-reports but no `run_battery.py`.
- 2d authored its runner at r1: commit `5024828` (2026-10-12), 102 lines, sole flag
  `--probe-failing`.
- 3d authored its own at r1: commit `82c21b4` (2026-10-13), **already 294 lines** with
  `seed_digests()`, a data-driven `MUTATION` dict, and the full exit-contract docstring —
  i.e., a re-implementation of the shared pattern at fork time, not a stale copy.
- Today: 2d = 969 lines, sha `42104d95af5f…`; 3d = 703 lines, sha `b992c7a5f135…`;
  `diff -u` = 1,631 diff lines. ~60+ rounds of independent evolution in both directions.

**Divergence inventory (direction matters):**

| Capability | 2d | 3d |
|---|---|---|
| Seed-immutability gate (`seed_digests()` + `seeds_unchanged` SHA-256 map before/after, fails battery on seed mutation) | **absent — never existed** (`git log -S seed_digests` → 0 hits; verdicts.json keys are only `godot,seed,scratch,probe_failing,results,verdict`) | present since r1 (`run_battery.py:101,234`) |
| Process-tree timeout probe (`--probe-tree-timeout`, detached witness via `timeout_descendant.py`, /proc cmdline/stat pid+pgid+ppid+starttime identity check) | **absent — declared open in SCORECARD planned** ("process-tree timeout … remain unprobed") | present since r5 (`c460369`; `run_battery.py:417-535`) |
| `--fault-injection` mode (isolated Python-subprocess fault probes: hang/clean-negative/unrelated-error) | present (`run_battery.py:210-240`); exercised r59/r60 (`corpus/lessons/r59-audio-parent-fault.json`) | absent |
| Export-launch probe (`--probe-export-launch`, bounded scratch Linux/X11 export + launch, artifact SHA capture) | present (`--probe-export-launch`; `__godot_export__`/`__godot_export_missing__` virtual tokens) | absent (3d scorecard: "export templates for 3D … remain unprobed") |
| Audio-warning verdict (`classify_audio_process`, `--probe-audio-warning`) | present (r14 `f870fd4`) | absent |
| Two-process save protocol (`__save_process_writer/reader/missing__` virtual tokens, run-local XDG) | present (r58) | absent |
| Incremental stdout read primitive | `selectors.DefaultSelector` (line ~787, timeout probe) | raw `select.select` (line 333, crash probe) + `Popen.communicate(timeout=3)` |
| Case timeout | per-site bounds (`timeout=5` launches, `bounded_run(case,args,bound)` param) | single `CASE_TIMEOUT_SECONDS = 20` |
| `project.godot` determinism | 3 lines — no physics section | pins `common/physics_ticks_per_second=60` + documents headless 64×64 viewport caveat |
| Fixture header comments (opt-in invocation documented at top of file) | absent on probe fixtures | present on `stream_attribution3d.gd`/`crash_exit3d.gd`/`timeout_tree3d.gd` |
| Adversarial self-check | inline scene-B marker mutation (`assert 'marker = "B"'`, line ~508) | data-driven `MUTATION` dict (case/script/old/new/expected_diagnostic/forbidden_stdout) |
| Probe marker namespaces | `STREAM_*`/`CRASH_EXIT_PROBE`/`TIMEOUT_PROBE` | renamed `STREAM_3D_*`/`CRASH_EXIT_3D`/`TREE_TIMEOUT_3D` + a Node3D spatial setup-sanity arm inside each fixture |

**Meta-pattern worth naming:** conventions propagated fleet-wide while code stayed
lane-local. All three lanes run the same protocol — opt-in `--probe-*` flags, serial
receipts under `corpus/live/runs/<ts>/`, exit 0/1/2 classification, expected-failure
taxonomy, report-last ordering — with zero shared imports. audio's `measure_audio.py`
follows the identical convention (`SPECS` + ~30 `--probe-*` flags + `runs/` receipts +
`expected_pass/expected_failure` status). The shared harness is a *protocol*, not a library.

**The drift that is worth a lesson is asymmetric capability, not divergence itself:**
each sibling independently solved a problem the other still lists as open —
- 3d's tree-timeout machinery (verified at r5, re-verified within every full replay) is the
  exact mechanism 2d's SCORECARD names unprobed, and the exact shape `G2dR61Boundary` is
  tasked to scratch-recon **in this wave** (task file: "process-tree timeout (a Godot child
  spawning a descendant that outlives it — does the harness reap/kill the tree or wait?)").
  2d is about to re-derive what its sibling already ships.
- 2d's fault-injection mode and export-launch probe are the exact shapes 3d's scorecard
  names unprobed ("process-tree/crash policy", "export templates for 3D").

3d's own seed.md already encodes the port rule: lessons were "ported by analogy …
requires this lane's own non-author verification before it counts as evidence here."
The return port never happened.

---

## (c) Lane-repo write attestation

`git status --porcelain` after the scan, before this write:

| repo | observed | attribution |
|---|---|---|
| audio-shokunin | `?? corpus/live/r62-boundary/` | AudioR62Boundary leaf scratch — in-flight, not this seat |
| game-dev-2d-shokunin | `?? corpus/live/r61-baseline/`, `?? corpus/live/r61-reviewer/` | in-flight leaves — not this seat |
| game-dev-3d-shokunin | clean | — |

This seat's only filesystem write is this file:
`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin-train-20261013/x-connector.md`.
No tracked content in any lane repo was created or modified. (Post-write `git status`
re-run will show the same rows or additional in-flight leaf scratch belonging to other seats.)

---

## Proposed move (one, bounded)

**Declared port-round for game-dev-2d: import 3d's verified tree-timeout mechanism as a
coverage move, instead of re-deriving it in scratch.** Concretely: port `timeout_tree3d.gd`
+ `timeout_descendant.py` + `probe_tree_timeout()` (witness pidfile + /proc identity
verification + `start_new_session` process-group semantics) into a 2d-named fixture, exactly
as a normal declared round with 2d's own wave-1 leaves and named non-author replay — the
fleet's own "ported by analogy" rule already requires that, so no new protocol is invented.
`G2dR61Boundary`'s scratch recon this wave can serve as the port's falsification map (where
does 2d's runner semantics differ: selectors vs select, per-case bounds vs 20 s constant).

- *expansion*: closes a coverage hole 2d itself declares open, using sibling-proven evidence
  (3d `tree-timeout-verdicts.json` shape, r5 onward) rather than a greenfield probe.
- *quality*: the ported mechanism carries its own discriminating claim ("One identified
  detached Godot-spawned witness terminated after direct-child timeout; not arbitrary
  process-tree cleanup") — a sharper bounded claim than a fresh recon would produce.
- *discernment*: the boundary is exercised honestly — it is a port between harnesses, not an
  absorption of sibling evidence; 2d's receipts are what count.

Secondary, report-only (not a move this seat can land): name the engine-audio seam in both
provinces at next bookkeeping touch — audio owns artifact-layer verification, game-dev-2d
holds engine-runtime audio as fixture surface, and cross-layer claims ("lane-produced WAV
verified in-engine") stay refused until a named joint protocol exists. Contested scope is
reported, not absorbed — per both provinces' own wording.

## Risks / limits of this scan

- Static + git evidence only: I did not execute either battery; all runner-behavior claims
  cite committed code, committed lessons, and verifier JSON, not fresh runs.
- The port is not free: 3d's probe is Linux `/proc`+POSIX-specific (it self-guards:
  `os.name != "posix" or not Path("/proc/self/stat").exists()` → typed error). Fine on this
  host; the ported claim must stay host-local and must not generalize to process-tree
  policy beyond the one identified witness.
- A `seed_digests` port into 2d would add a `seeds_unchanged` field to verdicts.json —
  additive schema change with unknown strict consumers (audio lane hit exactly this class of
  risk at r9). Keep it out of the tree-timeout move.
- The engine-audio seam text touches two provinces' boundary wording — operator/bookkeeping
  surface, deliberately out of this leaf's write scope.
- Drift table reflects committed state at scan time; in-flight r61/r62/r70 leaves may add
  new fixtures this wave (audio `r62-boundary` scratch already present).

## Verification

Every claim above resolves to: `git -C <lane> log/show` output quoted inline,
`diff -u`/`wc -l`/`sha256sum` on the two runners (969 vs 703 lines; shas
`42104d95…`/`b992c7a5…`; 1,631-line diff), `grep` counts (0 hits for seed_digests in 2d
history; 0 Audio* hits in 3d fixtures; 0 Godot hits in audio lane), or a resolvable path
(`corpus/fixtures/run_battery.py:101`, `:417`, `corpus/lessons/r12-headless-audio.md`,
`corpus/knowledge/seed.md`, MANIFEST roster entries, spec.json item `G2dR61Boundary`).

| godspeed
