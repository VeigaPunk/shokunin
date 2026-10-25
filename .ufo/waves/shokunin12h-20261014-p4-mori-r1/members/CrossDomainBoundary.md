# CrossDomainBoundary — mori/tsukuroi/kumitate/kama Boundary Verification

**Member:** `CrossDomainBoundary` (connector)  
**Wave:** `shokunin12h-20261014-p4-mori-r1`  
**Lane:** `mori-shokunin` (shonen probation round 1)  
**Contract Boundary:** mori reads journal+cgroup as FLEET evidence; must NOT claim OS-package ownership (`tsukuroi`), dispatch/orchestration (`kumitate`), or endpoint identity (`kama`).  
**Role:** UFO-FSD connector — deliver one non-obvious move (compatible synthesis across the round's proposals) improving declared axes without harm. Data only; not a verdict.  
**Declared Axes:** `coverage` · `operability` · `calibration`  
**Host Probes:** Read-only over `plazir27` (`Linux 7.2.3-arch1-3`, boot id `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`).

---

## 1. Evidence (Ground Truth & Cross-Domain Audit)

### 1.1 The Domain Contracts
The fleet province definitions establish strict boundaries between four adjacent lanes:

| Lane | Province & Authority | Owns | Must Refuse (Out of Province) |
|---|---|---|---|
| **`mori`** | `mori-shokunin/PROVINCE.md`<br>`SKILL.md` | Fleet & host observability: shokunin watchdog liveness (pid, log freshness, counters); `.ufo/waves/*` settlement join; kill/OOM events as **fleet evidence**; resource runway (disk, memory pressure); lane silence. Detection and reporting only; **never remediates**. | Dispatch & orchestration mechanism (→ `kumitate`); OS package, systemd unit, driver/firmware and boot state (→ `tsukuroi`); endpoint & model-serving health (→ `kama`); credentials/vault ops (→ `kagi`). |
| **`tsukuroi`** | `tsukuroi-shokunin/PROVINCE.md`<br>`oom-event-plane.md`<br>`package-state-plane.md` | OS substrate operability & repair: pacman package state (`pacman -Qkk`, foreign/AUR packages, `.pkg.tar.zst` receipts); systemd user units & timers (`systemctl --user`, unit files, failed states); journal/boot triage (`journalctl -b`, dmesg error classes); driver/firmware plane (`nvidia-smi`, kernel modules). | Endpoint/model serving health (→ `kama`); secrets (→ `kagi`); binary RE (→ `kaidoku`/`revenger`). Never installs/restarts packages or services. |
| **`kumitate`** | `kumitate-shokunin/PROVINCE.md` | Orchestration & tooling: OMP task/hub, ufo-fsd scripts & runtime, dispatch mechanism, substrate launch commands, tmux session lifecycle, swarm registry & run structures. | External domains; reports cross-domain evidence back to orchestrator. |
| **`kama`** | `kama-shokunin/PROVINCE.md`<br>`consumer-registry.md` | Local model serving & endpoint health: baseURL drift, served-model reconciliation (`GET /v1/models` vs `--alias`), probe conventions (`/health`, `/props`, `/slots`), `endpoint-consumers.tsv`, `qwen-coder.service` on port 34113. | Model quality/eval (`kengaku`), credentials (`kagi`), dispatch/route mechanism (`kumitate`), remote web (`kake`). Never writes to `~/.config` or systemd units. |

### 1.2 Boundary Audit of the Round 1 Census Design
Auditing the design artifacts produced in this wave (`GateDesign.md`, `FindingIds.md`, `FixtureDesign.md`, `CorpusMap.md`, `LiveReceipt.md`):

#### A. The `tsukuroi` Boundary: Two Specific Overreaches Identified
1. **Cumulative Cgroup Monotonic Counter vs. Fleet Scope Overreach (`CGROUP_OOM_KILL`)**:
   - *Design state*: In `GateDesign.md` (`probe_cgroup()`, L433-444) and `FindingIds.md` (L129), `CGROUP_OOM_KILL` is emitted at severity `crit` whenever `oom_kill > 0` in `/sys/fs/cgroup/user.slice/user-1000.slice/memory.events`.
   - *Live Host Observation*:
     ```text
     /sys/fs/cgroup/user.slice/user-1000.slice/memory.events:
       oom_kill 1
     /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/memory.events:
       oom_kill 0
     /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/tmux-spawn-882f0c6c-86dc-4c76-acd8-7f0f7d740cec.scope/memory.events:
       oom_kill 0
     /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/tmux-spawn-cfb2824c-8cad-4995-a489-02d2d465d291.scope/memory.events:
       oom_kill 0
     ```
   - *Forensic Origin*: Tsukuroi's `corpus/knowledge/oom-event-plane.md:28` establishes that this single `oom_kill 1` occurred on 2026-10-13 23:44:30 (Event A: an interactive terminal `python3` process in `app-Hyprland-xdg-terminal-exec-dd9e67bd.scope` killed by the kernel during Chromium `GpuWatchdog` memory exhaustion). The scope exited over 24 hours ago.
   - *Contradiction & Bleed*: Cgroup v2 `memory.events` are cumulative monotonic counters over the lifetime of the cgroup. By probing the root user slice without delta tracking or fleet leaf scoping, `tools/mori-census.sh` permanently fires `CGROUP_OOM_KILL crit` -> `MORI_CENSUS: DRIFT` for the entire remaining boot lifetime, despite **every active fleet process having `oom_kill = 0`**. This absorbs general OS boot triage (tsukuroi's plane) and misclassifies it as active fleet unhealthiness.

2. **Unscoped Systemd Unit and Crash Scraping (`UNIT_FAILURE_JOURNAL` / `SEGFAULT_JOURNAL`)**:
   - *Design state*: In `GateDesign.md` (`probe_journal()`, L402, 416) and `FindingIds.md` (L117-118), `journalctl --user -b` is grepped for `Failed with result|Unit entered failed state` (`UNIT_FAILURE_JOURNAL` / `UNIT_FAIL_EVENT`) and `segfault|general protection fault` (`SEGFAULT_JOURNAL` / `SEGFAULT_EVENT`).
   - *Live Host Observation*:
     ```text
     $ journalctl --user -b --no-pager -o cat -g 'Failed with result'
     app-Hyprland-xdg-terminal-exec-dd9e67bd.scope: Failed with result 'oom-kill'.
     pipewire-pulse.service: Failed with result 'core-dump'.
     ```
     `LiveReceipt.md` measured 1044 user core dumps (top: `love` 574, `godot` 318, `pw-play` 84, `waybar` 6) and 588 system segfaults.
   - *Contradiction & Bleed*: `systemd` user units and timers (`systemctl --user`, unit files, failed states) are explicitly owned by `tsukuroi` (`tsukuroi-shokunin/PROVINCE.md:8`). While `GateDesign.md` appropriately muted `UNIT_FAILURE_JOURNAL` to `info` severity in r1, capturing `pipewire-pulse.service` (desktop audio) or non-fleet graphical scopes under mori is an out-of-province claim on OS user-unit state.
   - *Clean Tsukuroi Aspect*: Mori cleanly executes **zero** package queries (`pacman`, `pacman -Qkk`, etc. are completely absent).

#### B. The `kumitate` Boundary: Clean Separation Maintained
- *Dispatch & Orchestration*: `GateDesign.md` and `mori-shokunin/SKILL.md` strictly honor non-remediation. Mori contains no dispatch code, no OMP task launching, no tmux process creation/killing, and no process restarting.
- *Settlement Join vs Failure Claim*: In `GateDesign.md` (`probe_waves()`, L328, 357-363) and `FindingIds.md` (§3.2), an unsettled wave aged beyond threshold emits `WAVE_UNSETTLED_AGE` with `settle=0`, explicitly obeying `SKILL.md:16` ("assuming an unsettled wave is a failed one is NEVER permitted"). Mori evaluates the presence/absence of registry + results pairs; kumitate and the operator own dispatch triage.
- *Tmux Probe*: Probing `tmux ls` is optional and read-only (`GateDesign.md:32`).

#### C. The `kama` Boundary: Clean Separation Maintained
- *Model Serving & Endpoints*: No HTTP probes (`GET /v1/models`, `/health`), no socket checks against port 34113 or 8080, and no inspection of `baseURL` in consumer configs appear anywhere in the census design. Model endpoint health is completely deferred to `kama`.

#### D. The `kagi` Boundary: Clean Separation Maintained
- *Credentials & Secrets*: No command reads `~/.kimi-code/credentials/`, `~/.config/the-janitor/`, `oauth/`, `op.env`, or `server.token`. `GateDesign.md` uses bounded `grep -ciE` (counts only) for journal events, preventing any inadvertent credential leakage.

---

## 2. Affected Axes

| Axis | Pre-Move Tension in Round 1 Design | Post-Synthesis State |
|---|---|---|
| **`coverage`** | Gate sweeps arbitrary desktop core dumps (`pw-play`, `pipewire-pulse`) while simultaneously risking blind spots by treating the root user slice as the sole cgroup anchor. | Focuses cgroup and journal probes on actual fleet execution scopes (`tmux-spawn-*`, `ufo-sighting`, `shokunin-watchdog`, `node`, `omp`), achieving precise fleet coverage without swallowing OS desktop noise. |
| **`operability`** | Because `user-1000.slice/memory.events` currently has `oom_kill=1`, running `tools/mori-census.sh` live forces an immediate, un-clearable `MORI_CENSUS: DRIFT` (exit 1) on this healthy host, destroying its operability as an automated gate. | Live gate evaluates clean (`MORI_CENSUS: CLEAN`, exit 0) when the fleet is healthy, while remaining fully operational to fire on real in-flight fleet failures. |
| **`calibration`** | Conflates historical monotonic boot-level OS metrics (owned by `tsukuroi`) with active in-mission fleet process state (owned by `mori`), violating truth in labeling. | Separates historical background substrate facts (`owner=tsukuroi; scope=substrate; info`) from active fleet process failure events (`owner=mori; scope=fleet; crit`), preventing false DRIFT. |

---

## 3. Proposed Move: Fleet-Scoped & Delta-Gated Observability Boundary

**One non-obvious move synthesizing `GateDesign.md`, `FindingIds.md`, and `tsukuroi`'s `oom-event-plane.md`:**

### 3.1 Fleet Leaf Cgroup Scoping & Background Counter Partitioning
In `tools/mori-census.sh` (`probe_cgroup()`), partition cgroup memory evaluation into two distinct tiers:
1. **Tier 1 (Fleet Leaf Scopes — Active Authority):**  
   Inspect the leaf cgroups associated with the fleet runtime:  
   `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/tmux-spawn-*.scope/memory.events`  
   (and any cgroup holding processes matching `ufo-sighting`, `shokunin`, `node`, `omp`).  
   - If any active fleet leaf scope has `oom_kill > 0`, emit `CGROUP_OOM_KILL` (`crit` -> `DRIFT`).
2. **Tier 2 (Root User Slice — Contextual Substrate Authority):**  
   For `/sys/fs/cgroup/user.slice/user-1000.slice/memory.events`:  
   - A static snapshot of `oom_kill > 0` where leaf fleet scopes are clean (0) must emit `CGROUP_OOM_HOST_HISTORICAL` (`info`, payload: `owner=tsukuroi; scope=substrate; fleet_relevant=false`). It **does not** flip the gate verdict from CLEAN to DRIFT.  
   - `CGROUP_OOM_KILL` on the parent slice fires only when a monotonic delta is measured within the mission window (`Δ oom_kill > 0`) or when corroborated by a fleet-attributed journal event.

### 3.2 Fleet Attribution Filter for Journal Events
In `probe_journal()`:
1. Scope `OOM_KILL_JOURNAL` and `UNIT_FAILURE_JOURNAL` by matching the unit or task comm against fleet signatures (`shokunin`, `watchdog`, `tmux`, `ufo`, `kimi`, `opencode`, `omp`).
2. Any journal OOM or unit failure originating from an external desktop unit (e.g. `app-Hyprland-xdg-terminal-exec-dd9e67bd.scope`, `pipewire-pulse.service`) is tagged:  
   `finding=UNIT_FAILURE_EXTERNAL severity=info payload="owner=tsukuroi; unit=<name>; out_of_province=report_only"`.  
   This preserves complete observability without overreaching into tsukuroi's domain.

### 3.3 Explicit Owner Routing Table Integration
Codify in `mori-shokunin/corpus/knowledge/cross-lane-boundaries.md` and `FindingIds.md` §5 that all host substrate events (`owner=tsukuroi`) and endpoint events (`owner=kama`) captured by mori are emitted as `OUT_OF_PROVINCE_REPORT` with severity `info`. This operationalizes the core shokunin rule: *"Out of province → report, never absorb."*

---

## 4. Risks & Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| **Over-restrictive fleet regex** | An unexpected fleet helper (e.g. an isolated subprocess) dies of OOM in an unmapped scope and is missed. | The Tier-2 parent slice probe monitors the cumulative counter: if `user-1000.slice/memory.events` `oom_kill` increments during the mission (`Δ > 0`), mori raises `CGROUP_OOM_UNMAPPED_DELTA` (`warn`), ensuring zero undetected deaths. |
| **Dynamic leaf cgroup discovery overhead** | Globbing or finding `tmux-spawn-*.scope` might incur filesystem IO or fail if cgroups are ephemeral. | User 1000 has read access to its entire slice tree. In bash, globbing `app-graphical.slice/tmux-spawn-*.scope/memory.events` is instantaneous; if no tmux scopes exist, the probe reports `unavailable` (info), never failing the gate. |

---

## 5. Verification

### 5.1 Live Host Probe Verification
Executed read-only probes directly on `plazir27` to verify the boundary partition:

1. **Leaf Fleet Scopes (Empirical Clean State)**:
   ```bash
   $ grep -H oom_kill /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/tmux-spawn-*.scope/memory.events
   /sys/fs/cgroup/.../tmux-spawn-882f0c6c-86dc-4c76-acd8-7f0f7d740cec.scope/memory.events:oom_kill 0
   /sys/fs/cgroup/.../tmux-spawn-cfb2824c-8cad-4995-a489-02d2d465d291.scope/memory.events:oom_kill 0
   ```
   *Result*: Active fleet scopes (running `ufo-sighting.mjs` and swarm agents) have `oom_kill = 0`. Under the synthesized move, these verify cleanly as expected.

2. **Root User Slice vs. Parent Service**:
   ```bash
   $ grep oom_kill /sys/fs/cgroup/user.slice/user-1000.slice/memory.events
   oom_kill 1
   $ grep oom_kill /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/memory.events
   oom_kill 0
   ```
   *Result*: Proves the single OOM kill is isolated to the historical scope and absent from the user service tree. Tagging the parent counter as `CGROUP_OOM_HOST_HISTORICAL` (`info`, `owner=tsukuroi`) prevents false DRIFT while truthfully recording the host condition.

3. **Journal Unit Attribution**:
   ```bash
   $ journalctl --user -b --no-pager -o cat -g 'Failed with result'
   app-Hyprland-xdg-terminal-exec-dd9e67bd.scope: Failed with result 'oom-kill'.
   pipewire-pulse.service: Failed with result 'core-dump'.
   ```
   *Result*: Both observed unit failures are non-fleet desktop units. Fleet-relevance filtering prevents `pipewire-pulse` core-dump from triggering false fleet failure alarms.

### 5.2 Fixture Verification Contract for `tools/mori-census.sh --selftest`
Add two explicit test cases to `FixtureDesign.md`:
- **Case `cgroup_host_historical_clean_fleet`**: Synthetic fixture with `user-1000.slice/memory.events` having `oom_kill 1` and `tmux-spawn/memory.events` having `oom_kill 0`.  
  *Assertion*: Exit `0`, verdict `MORI_CENSUS: CLEAN`, finding `CGROUP_OOM_HOST_HISTORICAL` present at severity `info`.
- **Case `cgroup_fleet_oom_kill_fires`**: Synthetic fixture with `tmux-spawn/memory.events` having `oom_kill 1`.  
  *Assertion*: Exit `1`, verdict `MORI_CENSUS: DRIFT`, finding `CGROUP_OOM_KILL` present at severity `crit`.
