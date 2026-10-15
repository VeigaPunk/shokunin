# Section honesty audit — advisory, not a verdict

Read-only. No section was added or removed. This report does not admit a score, a gate verdict, or a round close.

Audit HEAD: lane `8baa62cf8645100ea73d0ae2b68469368bf5f8a3` (clean). Origin tree `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`. The lane moved during the audit (`175de6ba` at dispatch, then later commits through `8baa62cf`). Findings below are the tree at `8baa62cf`. The only delta after frozen note snapshot `1ed7f103` is `SCORECARD.md` (S4 cell, R1 cell) and `corpus/knowledge/sighting-wall.md`. R3–R7 notes did not change in that delta.

## What was checked

A phantom is a `## ` heading whose first backticked token is path-like (contains `/`, contains `*`, or ends in a filename extension) and does not resolve to a file in the live tree. An omission is a live member the yes-cell declares for which none of that row's notes has such a heading. Deleted files are not declared members and were not invented back into a family. Directory tokens (`collect-omp-native-handoff-lib/`) are expansions, not missing files. K notes were resolved with `lstat` under `~/.kimi-code` (no secret file was opened). S/R notes were resolved against the origin worktree.

Declared membership is the current cell's own names and globs, expanded on the live tree, remainder families last, no overlap (0 overlaps observed). `native*.rs` is not treated as an R1 declaration: the cell names 8 files and says the glob is not the declaration. See the pattern leak below.

## Commands and observed output

```
git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse HEAD
8baa62cf8645100ea73d0ae2b68469368bf5f8a3

find scripts -maxdepth 1 -type f -name '*.mjs' | wc -l          # 73
find scripts -mindepth 2 -type f | wc -l                        # 18
find crates/ufo-core-runtime/src -maxdepth 1 -type f -name '*.rs' | wc -l   # 88
find crates/ufo-cli/src -maxdepth 1 -type f -name '*.rs' | wc -l            # 4
```

S_members = 73 + 18 = 91. R_members = 88 + 4 = 92. Origin `git status --porcelain` is 5 modifications (`README.md`, `config/ufo.json`, two bundled JSON files, `scripts/fleet-dispatcher.test.mjs`). None is an add or a delete. Membership is the worktree.

Absent, basename search 0, and no `## ` heading names them:

```
ABSENT crates/ufo-core-runtime/src/native_epoch.rs
ABSENT crates/ufo-core-runtime/src/native_epoch_tests.rs
ABSENT crates/ufo-core-runtime/src/native_launch_tests.rs
ABSENT crates/ufo-core-runtime/src/replay_falsification_probes.rs
ABSENT crates/ufo-core-runtime/src/rfc3339.rs
ABSENT crates/ufo-cli/src/admission.rs
ABSENT scripts/atomic-write.mjs
ABSENT scripts/collect-omp-native-handoff-lib/refusal-line.mjs
ABSENT scripts/charter-scribe/sync.test.mjs
```

Independent heading walk of every `corpus/knowledge/*.md` `## ` path-like token (fences skipped), exact path or unique basename, against an origin walk that prunes `.git` `.ufo` `target` `node_modules`:

```
CHECKED 220 MISS 0
```

`LC_ALL=C sort` on both sides, then `comm -3` of live glob expansion vs note sections that resolve to `crates/ufo-core-runtime/src/*.rs`:

```
=== comm -3 R3 ===
crates/ufo-core-runtime/src/cost_ledger_validation_tests.rs
crates/ufo-core-runtime/src/execution_profile_tests.rs
crates/ufo-core-runtime/src/native_profile.rs
decl 5 sec 2

=== comm -3 R4 ===
crates/ufo-core-runtime/src/lane_overlay_tests.rs
crates/ufo-core-runtime/src/lease_tests.rs
crates/ufo-core-runtime/src/live_tests.rs
decl 6 sec 3

=== comm -3 R5 ===
crates/ufo-core-runtime/src/native_admission_rules.rs
crates/ufo-core-runtime/src/native_admission_text.rs
crates/ufo-core-runtime/src/native_seats.rs
crates/ufo-core-runtime/src/native_text.rs
decl 4 sec 0

=== comm -3 R6 ===
crates/ufo-core-runtime/src/distill_tests.rs
crates/ufo-core-runtime/src/l3_swarm_tests.rs
decl 4 sec 2

=== comm -3 R7 ===
crates/ufo-core-runtime/src/bounded_fs.rs
crates/ufo-core-runtime/src/bounded_fs_tests.rs
crates/ufo-core-runtime/src/fs_durability.rs
crates/ufo-core-runtime/src/local_ship.rs
crates/ufo-core-runtime/src/local_ship_tests.rs
decl 5 sec 0
```

S8 identity diff against `remaining-scripts-census.md` headings: `comm -3` empty, decl 63, sec 63.

## Phantom sections

None at this HEAD. Those six runtime/CLI paths were `## ` headings in `runtime-remainder-census.md` at lane `85b2b70` (lines 244, 250, 262, 335, 363, 455 in that revision). They are gone from the note now, and no other knowledge note grew a heading for them. Do not put those sections back.

## Omissions — yes cell, no `## ` section for a live declared member

Seventeen. Each citation is the yes cell. The note searched is the cell's note. These are not phantoms: the files exist.

### R3 — `SCORECARD.md:129` — `corpus/knowledge/cost-and-profile.md`

Cell: 5 files (`execution_profile*`, `cost_ledger*`, `native_profile.rs`). Live expansion is exactly 5. Headings that count: `cost-and-profile.md:6` `cost_ledger.rs`, `cost-and-profile.md:63` `execution_profile.rs`. Missing:

- `crates/ufo-core-runtime/src/cost_ledger_validation_tests.rs`
- `crates/ufo-core-runtime/src/execution_profile_tests.rs`
- `crates/ufo-core-runtime/src/native_profile.rs`

### R4 — `SCORECARD.md:130` — `corpus/knowledge/runtime-support.md`

Cell: 6 files (`lane_overlay*`, `lease*`, `live*`). Live expansion is exactly 6. Headings: `runtime-support.md:10`, `:45`, `:81`. Missing:

- `crates/ufo-core-runtime/src/lane_overlay_tests.rs`
- `crates/ufo-core-runtime/src/lease_tests.rs`
- `crates/ufo-core-runtime/src/live_tests.rs`

### R5 — `SCORECARD.md:131` — `corpus/knowledge/native-admission-detail.md`

Cell names 4 files. The note's `## ` headings are topic headings (`native-admission-detail.md:8`, `:32`, `:58`), not file sections. All four are named in prose (`:13`, `:23`, `:27`, `:28`) and still omitted as sections:

- `crates/ufo-core-runtime/src/native_seats.rs`
- `crates/ufo-core-runtime/src/native_admission_text.rs`
- `crates/ufo-core-runtime/src/native_admission_rules.rs`
- `crates/ufo-core-runtime/src/native_text.rs`

### R6 — `SCORECARD.md:132` — `corpus/knowledge/distill-and-l3.md`

Cell: 4 files (`distill*`, `l3_swarm*`). Live expansion is exactly 4. Headings: `distill-and-l3.md:3`, `:78`. Missing:

- `crates/ufo-core-runtime/src/distill_tests.rs`
- `crates/ufo-core-runtime/src/l3_swarm_tests.rs`

`test-inventories.md:128` sections `distill_tests.rs`, but that note is R9's. It does not cover R6.

### R7 — `SCORECARD.md:133` — `corpus/knowledge/local-ship.md`

Cell: 5 files (`local_ship*`, `bounded_fs*`, `fs_durability.rs`). Live expansion is exactly 5. No heading's first token is a `.rs` file. `local-ship.md:128` is a heading whose first token is `bounded_fs`, not `bounded_fs.rs`. Missing:

- `crates/ufo-core-runtime/src/local_ship.rs`
- `crates/ufo-core-runtime/src/local_ship_tests.rs`
- `crates/ufo-core-runtime/src/bounded_fs.rs`
- `crates/ufo-core-runtime/src/bounded_fs_tests.rs`
- `crates/ufo-core-runtime/src/fs_durability.rs`

`test-inventories.md:115` sections `local_ship_tests.rs` for R9, not for R7.

The default claims gate will not error these five rows. R5 and R7 are topic-form (`ROW_NO_SECTIONS`, warn). R3, R4, and R6 match `N files` with fewer sections (`MEMBER_COUNT_SUSPECT`, warn). A `CLAIMS: MATCH` does not mean these notes have one section per declared member.

## Families with no phantom and no omission

| Row | Declared | Sections | Rule |
|---|---|---|---|
| S1 | 1 | 1 | `fleet-dispatcher.mjs` |
| S2 | 7 | 7 | two top-level mjs + 5 files under `collect-omp-native-handoff-lib/` |
| S3 | 2 | 2 | `ufo-swarm-wave.mjs`, `ufo-swarm-collect.mjs` |
| S4 | 5 | 5 | `ufo-sighting.mjs` + 4 files under `ufo-sighting-lib/` |
| S5 | 2 | 2 | `omp-global-config.mjs`, `ufo-mission-result.mjs` |
| S6 | 5 | 5 | the five named watchers |
| S7 | 6 | 6 | 5 `probe-*.mjs` + `fake-omp.mjs` |
| S8 | 63 | 63 | top-level `*.mjs` not in S1–S7, plus `charter-scribe/` and `lean-cargo/` |
| R1 | 8 | 8 | the eight named files, not the glob |
| R2 | 12 | 12 | `loop_driver*.rs` (10) + `state.rs` + `state_tests.rs` |
| R8 | 4 | 4 | the four named files |
| R9 | 1 | 1 in-family | `native_tests.rs` (3 extra sections, below) |
| R10 | 2 | 2 | `gate.rs`, `gate_tests.rs` |
| R11 | 41 | 41 | runtime `*.rs` not in R1–R10 (37) + `crates/ufo-cli/src/*.rs` (4) |
| K1 | 3 | 3 | `config.toml`, `tui.toml`, bak chain as one member (12 generations on disk) |
| K2 | 25 | 25 | 18 `agents/secondary/*.md` + 5 `skills/` entries + `plugins/installed.json` + `plugins/managed/kimi-webbridge` |
| K3 | 9 | 9 | the nine named paths, directories counted as directories |
| K4 | 9 | 9 in-family | the nine named paths (2 extra sections, below) |
| K5 | 3 | 3 | `workspaces.json`, `tui.toml.bak`, `rc-qrcode.png` |

S2 paths: `scripts/run-omp-native-trial.mjs`, `scripts/collect-omp-native-handoff.mjs`, `scripts/collect-omp-native-handoff-lib/{base,events,evidence,policy,screening}.mjs`.

S4 paths, each with a heading: `sighting-wall.md:83`, `:121`, `:142`, `:165`, `:188`. The bash shim `scripts/ufo-sighting` exists and is not a member. Its section is gone. Removal is recorded at `sighting-wall.md:232`. Not a phantom.

S7 live probes: `probe-redact.mjs`, `probe-token-plan-kimi.mjs`, `probe-token-plan-models.mjs`, `probe-token-plan-shared.mjs`, `probe-ufo-route-health.mjs`, plus `fake-omp.mjs`.

S8 (63, `comm -3` empty): `scripts/charter-scribe/config.json`, `scripts/charter-scribe/prompts/kimi-update.prompt.txt`, `scripts/charter-scribe/sync.mjs`, `scripts/charter-scribe/systemd/charter-scribe.service`, `scripts/charter-scribe/systemd/charter-scribe.timer`, `scripts/check-hand-authored-sets.mjs`, `scripts/check-hand-authored-sets.test.mjs`, `scripts/check-routing-free-config.mjs`, `scripts/check-routing-free-config.test.mjs`, `scripts/fleet-dispatcher.test.mjs`, `scripts/fleet-ledger-read.mjs`, `scripts/fleet-ledger-read.test.mjs`, `scripts/fleet-ledger-rotate.mjs`, `scripts/fleet-ledger-rotate.test.mjs`, `scripts/fleet-selfheal-verify.mjs`, `scripts/gates-plan.mjs`, `scripts/land-fleet-run.mjs`, `scripts/lean-cargo/README.md`, `scripts/lean-cargo/bin/cargo-shim.sh`, `scripts/lean-cargo/install-shim.sh`, `scripts/lean-cargo/measure.sh`, `scripts/local-helper.mjs`, `scripts/omp-native-shutdown.mjs`, `scripts/omp-role-work.mjs`, `scripts/omp-wave-context.mjs`, `scripts/prepare-ephemeral-fleet.mjs`, `scripts/prepare-ephemeral-fleet.test.mjs`, `scripts/prepare-ephemeral-l1.mjs`, `scripts/primeagent-recovery-assess.mjs`, `scripts/primeagent-refinement-ledger.mjs`, `scripts/project-devin-subagents.mjs`, `scripts/render-seat-tables.mjs`, `scripts/render-seat-tables.test.mjs`, `scripts/sync-global-routing.mjs`, `scripts/sync-ufo-contracts.mjs`, `scripts/the-tick-config.mjs`, `scripts/ufo-credential-screen.mjs`, `scripts/ufo-drills.mjs`, `scripts/ufo-godspeed-inject.test.mjs`, `scripts/ufo-l0-monitor-hook.test.mjs`, `scripts/ufo-l0-monitor.test.mjs`, `scripts/ufo-l0-watch.test.mjs`, `scripts/ufo-mission-activity.mjs`, `scripts/ufo-mission-activity.test.mjs`, `scripts/ufo-mission-lifecycle.mjs`, `scripts/ufo-mission-observation.mjs`, `scripts/ufo-mission-observation.test.mjs`, `scripts/ufo-native-names.mjs`, `scripts/ufo-night-watchdog.test.mjs`, `scripts/ufo-refinement-context.mjs`, `scripts/ufo-refinement-context.test.mjs`, `scripts/ufo-route-preflight.mjs`, `scripts/ufo-route-preflight.test.mjs`, `scripts/ufo-stale-watchdog.test.mjs`, `scripts/ufo-state-census.mjs`, `scripts/ufo-state-census.test.mjs`, `scripts/ufo-state-retention.mjs`, `scripts/ufo-state-retention.test.mjs`, `scripts/ufo-statusline-hook.test.mjs`, `scripts/ufo-swarm-collect.test.mjs`, `scripts/ufo-swarm-wave.test.mjs`, `scripts/ufo-watchdog-repend.mjs`, `scripts/ufo-watchdog-repend.test.mjs`.

R11 basenames (37 runtime + 4 CLI): `axes.rs`, `axes_tests.rs`, `axis_checks.rs`, `axis_checks_tests.rs`, `bounded_fixture.rs`, `bounded_fixture_tests.rs`, `build_json.rs`, `config.rs`, `config_tests.rs`, `fixture_spawn.rs`, `godspeed.rs`, `godspeed_tests.rs`, `lanes.rs`, `lanes_tests.rs`, `lib.rs`, `mutation.rs`, `native_agents.rs`, `native_continuity.rs`, `native_digests.rs`, `native_evidence.rs`, `native_route.rs`, `operator_guidance.rs`, `probe.rs`, `process_group.rs`, `process_group_tests.rs`, `profile_shape_refusal_tests.rs`, `proposal.rs`, `proposal_tests.rs`, `provenance.rs`, `provenance_tests.rs`, `report.rs`, `round.rs`, `round_digest.rs`, `round_digest_tests.rs`, `rules.rs`, `specialist.rs`, `test_env.rs`, `main.rs`, `main_tests.rs`, `titanium.rs`, `titanium_tests.rs`.

Top-level shell scripts and `scripts/ufo-sighting` are outside `S_members`. They were not assigned to S8.

## Residual — not the two classes

Do not delete these. The files exist.

- `corpus/knowledge/test-inventories.md:81` `loop_driver_tests.rs` — R2's member. R2 already sections it. R9's cell declares only `native_tests.rs`.
- `corpus/knowledge/test-inventories.md:115` `local_ship_tests.rs` — R7's member. R7's own note does not section it.
- `corpus/knowledge/test-inventories.md:128` `distill_tests.rs` — R6's member. R6's own note does not section it.
- `corpus/knowledge/failure-telemetry.md:11` `scripts/ufo-mission-result.mjs` — S5's member, in a note S2 also claims. Removing it would omit an S5 member.
- `corpus/knowledge/kimi-binary-secrets.md:221` `~/.kimi-code/rc-qrcode.png` — K5's member. K5 sections it.
- `corpus/knowledge/kimi-binary-secrets.md:232` `~/.kimi-code/session_index.jsonl` — K3's member. K3 sections it.

Pattern leak, same line as the garbled prose: `SCORECARD.md:127` backticks `native*.rs` inside a sentence that says the glob is not the declaration. `familyPatterns()` (`scripts/claims-check.mjs:256-258`) keeps any backticked token containing `*`. `find crates/ufo-core-runtime/src -maxdepth 1 -type f -name 'native*.rs' | wc -l` → 23. Those 15 extra files were not counted as R1 omissions. The backticks should come off or the gate will widen R1 the way round 17 already refused.

Stale yes-cell prose, notes themselves match the live set:

- `SCORECARD.md:125` still says the note is 9 of 9 and the parenthetical `ls` still names `atomic-write.mjs`. The note has 6 sections. The file is absent. Do not add a section.
- `SCORECARD.md:126` members cell says 63; the yes cell still says 60 of 60. The note has 63 sections and `comm -3` was empty.
- `corpus/knowledge/runtime-remainder-census.md:38` still lists `replay_falsification_probes.rs` in a size table. That is prose, not a `## ` heading. The file is absent.

## Sections added / removed by this audit

None.

## Unresolved blockers

None for the two classes. Anchors and verbatim symbols were not re-checked; a section can exist and still fail `SECTION_DEAD_ANCHOR` or `SECTION_NO_SYMBOL`. That is outside this pass.

## Cross-domain

No new cross-domain defect was established. The filed `membrane-seal write` argv defect was not re-opened and has no owner in this repo. The Cf/Mn note in `native-admission-detail.md:60` was not re-measured.
