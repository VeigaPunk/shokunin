# DeletionBoundaryArithmetic — round-32 deletion-boundary arithmetic

**Role:** leaf advisory (read-only). Not a verdict. Not a stanza edit.
**Lane:** `kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha`
- pin (frozen layer baseline): `5725fa7d3` (`5725fa7d clean(siblings) r03: …`)
- live HEAD: `964f443ee53df0ce06bd689af01f0dea031b01f9` short `964f443ee` (`964f443e routing: regenerate omp-seat-routing…`)

## Axes this report feeds

- `coverage:script-layer` denominator `S_members`
- `coverage:runtime-layer` denominator `R_members`
- per-family retired-member lists the registry notes must drop

## Files inspected

| Path | Why |
|---|---|
| `kumitate-shokunin/SCORECARD.md` (`## Planned` round 32; registry table; layer formulas) | frozen 114/98 claim + family definitions |
| `kumitate-shokunin/corpus/README.md` | 19-family map |
| `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` | layer-universe definition |
| `kumitate-shokunin/corpus/knowledge/{route-probe-cluster,remaining-scripts-census,runtime-remainder-census,ops-watchers,gate-verdict,native-judge-pipeline}.md` | pin-era member sections |
| origin tree `scripts/`, `crates/ufo-core-runtime/src/`, `crates/ufo-cli/src/` at HEAD + `git ls-tree` at `5725fa7d3` | live vs pin membership |
| `git diff --diff-filter=D --name-only 5725fa7d3 HEAD -- scripts crates` | authoritative deletion set |

## Layer-universe definition (frozen)

- **Script layer:** `scripts/<name>.mjs` (depth-1) ∪ every regular file under `scripts/*/` (recursive). Not: top-level `scripts/*.sh`.
- **Runtime layer:** `crates/ufo-core-runtime/src/*.rs` ∪ `crates/ufo-cli/src/*.rs` (depth-1 only).

---

## Exact commands + observed output

### Revisions

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse --short=9 5725fa7d3
5725fa7d3
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse --short=9 HEAD
964f443ee
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9
```

### Full deletion set (git, scripts+crates)

```
$ LC_ALL=C git -C /home/vgpnk/Projects/ufo-fsd-alpha \
    diff --diff-filter=D --name-only 5725fa7d3 HEAD -- scripts crates \
  | LC_ALL=C sort
```

**Observed: 50 paths** (complete list):

```
crates/ufo-cli/build.rs
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
crates/ufo-core-runtime/tests/godspeed_inject_full_prefix.rs
crates/ufo-core-runtime/tests/vector_anchors.rs
scripts/atomic-write.mjs
scripts/charter-scribe/sync.test.mjs
scripts/collect-omp-native-handoff-lib/refusal-line.mjs
scripts/local-helper.test.mjs
scripts/omp-global-config.test.mjs
scripts/omp-role-work.test.mjs
scripts/prepare-ephemeral-l1.test.mjs
scripts/primeagent-refinement-ledger.test.mjs
scripts/probe-redact.test.mjs
scripts/probe-ufo-route-health.test.mjs
scripts/project-devin-subagents.test.mjs
scripts/run-omp-native-trial.test.mjs
scripts/sync-global-routing.test.mjs
scripts/ufo-drills.test.mjs
scripts/ufo-ground-handler.test.mjs
scripts/ufo-mission-lifecycle.test.mjs
scripts/ufo-mission-result.test.mjs
scripts/ufo-sighting-lib/display-overview.mjs
scripts/ufo-sighting-lib/environment.mjs
scripts/ufo-sighting-lib/launch-verb.mjs
scripts/ufo-sighting-lib/layout.mjs
scripts/ufo-sighting-lib/mission-identity.mjs
scripts/ufo-sighting-lib/options.mjs
scripts/ufo-sighting-lib/pane-register.mjs
scripts/ufo-sighting-lib/pane-run.mjs
scripts/ufo-sighting-lib/queue.mjs
scripts/ufo-sighting-lib/resume-verb.mjs
scripts/ufo-sighting-lib/runner-attach.mjs
scripts/ufo-sighting-lib/spawn-pane.mjs
scripts/ufo-sighting-lib/status-verb.mjs
scripts/ufo-sighting-lib/status-view.mjs
scripts/ufo-sighting-lib/steer-peek.mjs
scripts/ufo-sighting-lib/stop-restore.mjs
scripts/ufo-sighting-lib/twins.mjs
scripts/ufo-sighting-lib/verbs-core.mjs
scripts/ufo-sighting-lib/wall-display.mjs
scripts/ufo-sighting-lib/wall-schema.mjs
scripts/ufo-sighting-lib/wall-verbs.mjs
scripts/ufo-sighting-lib/wall.mjs
scripts/ufo-statusline-gate.test.mjs
scripts/ufo-statusline-hook-machinery.test.mjs
```

**Partition of the 50:**

| Bucket | Count | Paths |
|---|---:|---|
| Script-layer universe deletions | **41** | all `scripts/…` rows above |
| Runtime-layer universe deletions | **6** | `admission.rs`, `native_epoch.rs`, `native_epoch_tests.rs`, `native_launch_tests.rs`, `replay_falsification_probes.rs`, `rfc3339.rs` |
| Outside layer universe (not in `S_members`/`R_members`) | **3** | `crates/ufo-cli/build.rs`, `crates/ufo-core-runtime/tests/godspeed_inject_full_prefix.rs`, `crates/ufo-core-runtime/tests/vector_anchors.rs` |
| **Total git-D** | **50** | 41+6+3 |

### Live enumeration

```
$ # S_members live
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts -maxdepth 1 -name '*.mjs' -type f | wc -l
73
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts -mindepth 2 -type f | wc -l
18
$ # → S_members = 73 + 18 = 91

$ # R_members live
$ find /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src -maxdepth 1 -name '*.rs' -type f | wc -l
88
$ find /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src -maxdepth 1 -name '*.rs' -type f | wc -l
4
$ # → R_members = 88 + 4 = 92
```

### Pin-era enumeration (`git ls-tree` at `5725fa7d3`)

```
$ # S pin = top-level *.mjs ∪ scripts/*/** 
$ # observed: S_pin = 114 (= 72 + 42)
$ # R pin = runtime src *.rs ∪ cli src *.rs
$ # observed: R_pin = 98 (= 93 + 5)
```

### Master subtraction (pin − live + add)

| Layer | Pin | Deleted | Added | Live | Check |
|---|---:|---:|---:|---:|---|
| Script | 114 | 41 | 18 | **91** | 114 − 41 + 18 = **91** |
| Runtime | 98 | 6 | 0 | **92** | 98 − 6 + 0 = **92** |

Frozen stanza still claims `S_members=114` / `R_members=98`. Live is 91 / 92. Gates reading DRIFT are correct.

Scorecard round-32 prose said “14 top-level `*.test.mjs`”; measured top-level `*.test.mjs` deletions = **16** (see S7+S8 lists). Prefer the measured set.

---

## Family pin membership (reproducible partition)

Pin-era family definitions match the SCORECARD registry + census notes. R3 test companion is `cost_ledger_validation_tests.rs` (not `cost_ledger_tests.rs`).

| Family | Pin n | Definition |
|---|---:|---|
| S1 | 1 | `fleet-dispatcher.mjs` |
| S2 | 8 | `run-omp-native-trial.mjs` + `collect-omp-native-handoff.mjs` + `collect-omp-native-handoff-lib/` ×6 |
| S3 | 2 | `ufo-swarm-wave.mjs` + `ufo-swarm-collect.mjs` |
| S4 | 27 | `ufo-sighting.mjs` + `ufo-sighting-lib/` ×26 |
| S5 | 2 | `omp-global-config.mjs` + `ufo-mission-result.mjs` |
| S6 | 5 | five ops watchers |
| S7 | 9 | 7 `probe-*.mjs` + `atomic-write.mjs` + `fake-omp.mjs` |
| S8 | 60 | pin-S ∖ (S1∪…∪S7) |
| **S Σ** | **114** | |
| R1 | 8 | eight `native{,_header,_schema,_contract,_scores,_plan_digest,_launch,_telemetry}.rs` |
| R2 | 12 | ten `loop_driver*.rs` + `state.rs` + `state_tests.rs` |
| R3 | 5 | `execution_profile*`, `cost_ledger.rs`, `cost_ledger_validation_tests.rs`, `native_profile.rs` |
| R4 | 6 | `lane_overlay*`, `lease*`, `live*` |
| R5 | 4 | seats/admission text |
| R6 | 4 | `distill*`, `l3_swarm*` |
| R7 | 5 | `local_ship*`, `bounded_fs*`, `fs_durability.rs` |
| R8 | 4 | transcript/ledger/seat_coverage/dispatch_topology |
| R9 | 1 | `native_tests.rs` |
| R10 | 2 | `gate.rs` + `gate_tests.rs` |
| R11 | 47 | pin-R ∖ (R1∪…∪R10) |
| **R Σ** | **98** | |

---

## Deletions grouped by family

### Script layer (41)

#### S1 — 0 deleted
(live still 1)

#### S2 — 1 deleted → live **7**

```
scripts/collect-omp-native-handoff-lib/refusal-line.mjs
```

#### S3 — 0 deleted
(live still 2)

#### S4 — 22 deleted → live **5** (`ufo-sighting.mjs` + 4 lib files)

```
scripts/ufo-sighting-lib/display-overview.mjs
scripts/ufo-sighting-lib/environment.mjs
scripts/ufo-sighting-lib/launch-verb.mjs
scripts/ufo-sighting-lib/layout.mjs
scripts/ufo-sighting-lib/mission-identity.mjs
scripts/ufo-sighting-lib/options.mjs
scripts/ufo-sighting-lib/pane-register.mjs
scripts/ufo-sighting-lib/pane-run.mjs
scripts/ufo-sighting-lib/queue.mjs
scripts/ufo-sighting-lib/resume-verb.mjs
scripts/ufo-sighting-lib/runner-attach.mjs
scripts/ufo-sighting-lib/spawn-pane.mjs
scripts/ufo-sighting-lib/status-verb.mjs
scripts/ufo-sighting-lib/status-view.mjs
scripts/ufo-sighting-lib/steer-peek.mjs
scripts/ufo-sighting-lib/stop-restore.mjs
scripts/ufo-sighting-lib/twins.mjs
scripts/ufo-sighting-lib/verbs-core.mjs
scripts/ufo-sighting-lib/wall-display.mjs
scripts/ufo-sighting-lib/wall-schema.mjs
scripts/ufo-sighting-lib/wall-verbs.mjs
scripts/ufo-sighting-lib/wall.mjs
```

S4 lib survivors (live): `argv.mjs`, `base.mjs`, `observe.mjs`, `surface.mjs`.

#### S5 — 0 deleted
(live still 2)

#### S6 — 0 deleted
(live still 5)

#### S7 — 3 deleted → live **6**

```
scripts/atomic-write.mjs
scripts/probe-redact.test.mjs
scripts/probe-ufo-route-health.test.mjs
```

S7 survivors: `fake-omp.mjs`, `probe-redact.mjs`, `probe-token-plan-{kimi,models,shared}.mjs`, `probe-ufo-route-health.mjs`.

#### S8 — 15 deleted + 18 added → live **63** (= 60 − 15 + 18)

**Deleted from S8:**

```
scripts/charter-scribe/sync.test.mjs
scripts/local-helper.test.mjs
scripts/omp-global-config.test.mjs
scripts/omp-role-work.test.mjs
scripts/prepare-ephemeral-l1.test.mjs
scripts/primeagent-refinement-ledger.test.mjs
scripts/project-devin-subagents.test.mjs
scripts/run-omp-native-trial.test.mjs
scripts/sync-global-routing.test.mjs
scripts/ufo-drills.test.mjs
scripts/ufo-ground-handler.test.mjs
scripts/ufo-mission-lifecycle.test.mjs
scripts/ufo-mission-result.test.mjs
scripts/ufo-statusline-gate.test.mjs
scripts/ufo-statusline-hook-machinery.test.mjs
```

**Added into S8 remainder** (live ∖ pin, all new top-level `scripts/*.mjs` — none claimed by S1–S7):

```
scripts/check-hand-authored-sets.mjs
scripts/check-hand-authored-sets.test.mjs
scripts/check-routing-free-config.mjs
scripts/check-routing-free-config.test.mjs
scripts/land-fleet-run.mjs
scripts/omp-wave-context.mjs
scripts/prepare-ephemeral-fleet.mjs
scripts/prepare-ephemeral-fleet.test.mjs
scripts/render-seat-tables.mjs
scripts/render-seat-tables.test.mjs
scripts/ufo-godspeed-inject.test.mjs
scripts/ufo-night-watchdog.test.mjs
scripts/ufo-refinement-context.mjs
scripts/ufo-refinement-context.test.mjs
scripts/ufo-route-preflight.mjs
scripts/ufo-route-preflight.test.mjs
scripts/ufo-state-census.mjs
scripts/ufo-state-census.test.mjs
```

#### Script family live sizes (must sum 91)

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Σ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 2 | 5 | 2 | 5 | 6 | 63 | **91** |

### Runtime layer (6)

#### R1–R10 — 0 deleted each
(live sizes unchanged: 8+12+5+6+4+4+5+4+1+2 = **51**)

#### R11 — 6 deleted → live **41** (= 47 − 6)

```
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

#### Runtime family live sizes (must sum 92)

| R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | Σ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 12 | 5 | 6 | 4 | 4 | 5 | 4 | 1 | 2 | 41 | **92** |

R11 live also = (88 runtime − 51 R1–R10) + 4 CLI = 37 + 4 = **41**.

---

## `LC_ALL=C sort` + `comm -3` proofs

Every `comm` below had **both** inputs `LC_ALL=C sort`ed. Empty output = match.

### 1. Pin family union ≡ pin universe

```
$ LC_ALL=C comm -3 \
    <(cat fam-S{1..8}-pin.txt | LC_ALL=C sort) \
    pin-S.txt
# (empty)  lines=0  bytes=0

$ LC_ALL=C comm -3 \
    <(cat fam-R{1..11}-pin.txt | LC_ALL=C sort) \
    pin-R.txt
# (empty)  lines=0  bytes=0
```

### 2. Live family union ≡ live universe

```
$ LC_ALL=C comm -3 \
    <(cat fam-S{1..8}-live.txt | LC_ALL=C sort) \
    live-S.txt
# (empty)  lines=0  bytes=0   # proves derived S members = 91 live files

$ LC_ALL=C comm -3 \
    <(cat fam-R{1..11}-live.txt | LC_ALL=C sort) \
    live-R.txt
# (empty)  lines=0  bytes=0   # proves derived R members = 92 live files
```

### 3. git-D ∩ layer-universe ≡ pin−live deletions

```
$ # git-D-S = deleted-all paths matching scripts/*.mjs or scripts/*/**
$ LC_ALL=C comm -3 git-D-S.txt S-deleted.txt
# (empty)  # 41 = 41

$ LC_ALL=C comm -3 git-D-R.txt R-deleted.txt
# (empty)  # 6 = 6
```

### 4. Σ family deletions ≡ layer deletions

```
$ LC_ALL=C comm -3 \
    <(cat del-S{1..8}.txt | LC_ALL=C sort) \
    S-deleted.txt
# (empty)  # 0+1+0+22+0+0+3+15 = 41

$ LC_ALL=C comm -3 \
    <(cat del-R{1..11}.txt | LC_ALL=C sort) \
    R-deleted.txt
# (empty)  # 0×10 + 6 = 6
```

### 5. Direct pin↔live set difference

```
$ LC_ALL=C comm -23 pin-S.txt live-S.txt | wc -l
41
$ LC_ALL=C comm -13 pin-S.txt live-S.txt | wc -l
18
$ LC_ALL=C comm -23 pin-R.txt live-R.txt | wc -l
6
$ LC_ALL=C comm -13 pin-R.txt live-R.txt | wc -l
0
```

---

## Derived live member lists (complete)

### S1 (1)

```
scripts/fleet-dispatcher.mjs
```

### S2 (7)

```
scripts/collect-omp-native-handoff-lib/base.mjs
scripts/collect-omp-native-handoff-lib/events.mjs
scripts/collect-omp-native-handoff-lib/evidence.mjs
scripts/collect-omp-native-handoff-lib/policy.mjs
scripts/collect-omp-native-handoff-lib/screening.mjs
scripts/collect-omp-native-handoff.mjs
scripts/run-omp-native-trial.mjs
```

### S3 (2)

```
scripts/ufo-swarm-collect.mjs
scripts/ufo-swarm-wave.mjs
```

### S4 (5)

```
scripts/ufo-sighting-lib/argv.mjs
scripts/ufo-sighting-lib/base.mjs
scripts/ufo-sighting-lib/observe.mjs
scripts/ufo-sighting-lib/surface.mjs
scripts/ufo-sighting.mjs
```

### S5 (2)

```
scripts/omp-global-config.mjs
scripts/ufo-mission-result.mjs
```

### S6 (5)

```
scripts/the-tick-ping.mjs
scripts/ufo-ground-handler.mjs
scripts/ufo-l0-monitor.mjs
scripts/ufo-l0-watch.mjs
scripts/ufo-stale-watchdog.mjs
```

### S7 (6)

```
scripts/fake-omp.mjs
scripts/probe-redact.mjs
scripts/probe-token-plan-kimi.mjs
scripts/probe-token-plan-models.mjs
scripts/probe-token-plan-shared.mjs
scripts/probe-ufo-route-health.mjs
```

### S8 (63)

```
scripts/charter-scribe/config.json
scripts/charter-scribe/prompts/kimi-update.prompt.txt
scripts/charter-scribe/sync.mjs
scripts/charter-scribe/systemd/charter-scribe.service
scripts/charter-scribe/systemd/charter-scribe.timer
scripts/check-hand-authored-sets.mjs
scripts/check-hand-authored-sets.test.mjs
scripts/check-routing-free-config.mjs
scripts/check-routing-free-config.test.mjs
scripts/fleet-dispatcher.test.mjs
scripts/fleet-ledger-read.mjs
scripts/fleet-ledger-read.test.mjs
scripts/fleet-ledger-rotate.mjs
scripts/fleet-ledger-rotate.test.mjs
scripts/fleet-selfheal-verify.mjs
scripts/gates-plan.mjs
scripts/land-fleet-run.mjs
scripts/lean-cargo/README.md
scripts/lean-cargo/bin/cargo-shim.sh
scripts/lean-cargo/install-shim.sh
scripts/lean-cargo/measure.sh
scripts/local-helper.mjs
scripts/omp-native-shutdown.mjs
scripts/omp-role-work.mjs
scripts/omp-wave-context.mjs
scripts/prepare-ephemeral-fleet.mjs
scripts/prepare-ephemeral-fleet.test.mjs
scripts/prepare-ephemeral-l1.mjs
scripts/primeagent-recovery-assess.mjs
scripts/primeagent-refinement-ledger.mjs
scripts/project-devin-subagents.mjs
scripts/render-seat-tables.mjs
scripts/render-seat-tables.test.mjs
scripts/sync-global-routing.mjs
scripts/sync-ufo-contracts.mjs
scripts/the-tick-config.mjs
scripts/ufo-credential-screen.mjs
scripts/ufo-drills.mjs
scripts/ufo-godspeed-inject.test.mjs
scripts/ufo-l0-monitor-hook.test.mjs
scripts/ufo-l0-monitor.test.mjs
scripts/ufo-l0-watch.test.mjs
scripts/ufo-mission-activity.mjs
scripts/ufo-mission-activity.test.mjs
scripts/ufo-mission-lifecycle.mjs
scripts/ufo-mission-observation.mjs
scripts/ufo-mission-observation.test.mjs
scripts/ufo-native-names.mjs
scripts/ufo-night-watchdog.test.mjs
scripts/ufo-refinement-context.mjs
scripts/ufo-refinement-context.test.mjs
scripts/ufo-route-preflight.mjs
scripts/ufo-route-preflight.test.mjs
scripts/ufo-stale-watchdog.test.mjs
scripts/ufo-state-census.mjs
scripts/ufo-state-census.test.mjs
scripts/ufo-state-retention.mjs
scripts/ufo-state-retention.test.mjs
scripts/ufo-statusline-hook.test.mjs
scripts/ufo-swarm-collect.test.mjs
scripts/ufo-swarm-wave.test.mjs
scripts/ufo-watchdog-repend.mjs
scripts/ufo-watchdog-repend.test.mjs
```

### R1 (8) … R10 (2)

Unchanged from pin (lists above under “LIVE R*” in the measurement dump). Full paths retained in measurement; summary sizes only repeated here for R1–R10 since zero deletions.

### R11 (41)

```
crates/ufo-cli/src/main.rs
crates/ufo-cli/src/main_tests.rs
crates/ufo-cli/src/titanium.rs
crates/ufo-cli/src/titanium_tests.rs
crates/ufo-core-runtime/src/axes.rs
crates/ufo-core-runtime/src/axes_tests.rs
crates/ufo-core-runtime/src/axis_checks.rs
crates/ufo-core-runtime/src/axis_checks_tests.rs
crates/ufo-core-runtime/src/bounded_fixture.rs
crates/ufo-core-runtime/src/bounded_fixture_tests.rs
crates/ufo-core-runtime/src/build_json.rs
crates/ufo-core-runtime/src/config.rs
crates/ufo-core-runtime/src/config_tests.rs
crates/ufo-core-runtime/src/fixture_spawn.rs
crates/ufo-core-runtime/src/godspeed.rs
crates/ufo-core-runtime/src/godspeed_tests.rs
crates/ufo-core-runtime/src/lanes.rs
crates/ufo-core-runtime/src/lanes_tests.rs
crates/ufo-core-runtime/src/lib.rs
crates/ufo-core-runtime/src/mutation.rs
crates/ufo-core-runtime/src/native_agents.rs
crates/ufo-core-runtime/src/native_continuity.rs
crates/ufo-core-runtime/src/native_digests.rs
crates/ufo-core-runtime/src/native_evidence.rs
crates/ufo-core-runtime/src/native_route.rs
crates/ufo-core-runtime/src/operator_guidance.rs
crates/ufo-core-runtime/src/probe.rs
crates/ufo-core-runtime/src/process_group.rs
crates/ufo-core-runtime/src/process_group_tests.rs
crates/ufo-core-runtime/src/profile_shape_refusal_tests.rs
crates/ufo-core-runtime/src/proposal.rs
crates/ufo-core-runtime/src/proposal_tests.rs
crates/ufo-core-runtime/src/provenance.rs
crates/ufo-core-runtime/src/provenance_tests.rs
crates/ufo-core-runtime/src/report.rs
crates/ufo-core-runtime/src/round.rs
crates/ufo-core-runtime/src/round_digest.rs
crates/ufo-core-runtime/src/round_digest_tests.rs
crates/ufo-core-runtime/src/rules.rs
crates/ufo-core-runtime/src/specialist.rs
crates/ufo-core-runtime/src/test_env.rs
```

---

## Sections that notes must retire (cross-domain / owner)

Parent integrates; this seat does not edit notes. Owners of note edits:

| Family | Note | Sections to remove (deleted members) | Owner seat class |
|---|---|---|---|
| S2 | native-trial / handoff notes naming `refusal-line.mjs` | 1 section | S2 recensus |
| S4 | `knowledge/sighting-wall.md` | 22 lib member sections | S4 recensus |
| S7 | `knowledge/route-probe-cluster.md` | `atomic-write.mjs`, `probe-redact.test.mjs`, `probe-ufo-route-health.test.mjs` | S7 recensus |
| S8 | `knowledge/remaining-scripts-census.md` | 15 deleted; **add** 18 new member sections before claiming `yes` | S8 recensus |
| R11 | `knowledge/runtime-remainder-census.md` | 6 members listed above | R11 recensus |

S1/S3/S5/S6 and R1–R10: no deletion-boundary change.

## Score thresholds (arithmetic only; not a claims-gate run)

For score ≥ 7 with C1_layer = 1.0:

- script: `S_sections ≥ ceil(0.7 × 91) = 64` → need `floor(10 × S_sections/91) ≥ 7` ⇒ `S_sections ≥ 64`
- runtime: `R_sections ≥ ceil(0.7 × 92) = 65` → `R_sections ≥ 65`

This report does **not** measure `S_sections`/`R_sections` (claims gate / note editors).

## Unresolved blockers

- None for the deletion-boundary arithmetic itself: all `comm -3` proofs empty; 114−41+18=91; 98−6=92.
- Note/registry/stanza updates are out of this seat’s write scope (parent + family recensus members).
- Mid-round upstream churn: if HEAD moves past `964f443ee`, re-run the same command block; do not reuse these lists blindly.

## Cross-domain findings

| Finding | Owner |
|---|---|
| `crates/ufo-cli/build.rs` deleted but outside R-universe (build script, not `src/*.rs`) | runtime packaging / CLI crate — not a layer-member event |
| Two `crates/ufo-core-runtime/tests/*.rs` deleted — outside `src/*.rs` universe | same |
| 18 new script members all fall into S8 remainder by construction (not S1–S7) | S8 must sectionize before `yes` |
| SCORECARD r32 prose “14 top-level `*.test.mjs`” under-counts measured **16** | SCORECARD prose hygiene (parent) |

## Summary equation (the reproducible subtraction)

```
S_members_live = S_members_pin − |S_deleted| + |S_added|
               = 114 − 41 + 18
               = 91
               = 73 (scripts/*.mjs) + 18 (scripts/*/**)

R_members_live = R_members_pin − |R_deleted| + |R_added|
               = 98 − 6 + 0
               = 92
               = 88 (ufo-core-runtime/src/*.rs) + 4 (ufo-cli/src/*.rs)

Family_S_live = { S1:1, S2:7, S3:2, S4:5, S5:2, S6:5, S7:6, S8:63 }
Family_R_live = { R1:8, R2:12, R3:5, R4:6, R5:4, R6:4, R7:5, R8:4, R9:1, R10:2, R11:41 }

git-D(scripts∪crates) = 50 = 41 (S) + 6 (R) + 3 (outside universe)
```

All set equalities above are `LC_ALL=C comm -3`-empty.

---

*End of advisory. No stanza write. No note edit. No gate run.*
