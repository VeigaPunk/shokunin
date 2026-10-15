# OwnerMap — Remediation Ownership Routing Table & Handover Contract

**Member:** `OwnerMap` (connector leaf)  
**Wave:** `shokunin12h-20261014-p4-mori-r1` / `Shokunin12hP4MoriR1`  
**Lane:** `mori-shokunin` (森) — fleet & host observability (shonen probation round 1)  
**Advisory Status:** Member report data only. Not a judge verdict, not a gate admission, and not a remediation order. Parent (Sol 6.1) integrates.  
**Role:** UFO-FSD connector — finding one non-obvious move that improves the round's declared axes without harming another.  
**Judged on:** coverage · operability · calibration  
**Measured host snapshot:** `2026-10-15T00:36:12Z` (local `2026-10-14T21:36:12-03:00`), host `plazir27`, kernel `7.2.3-arch1-3`, boot `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`.  
**Hard Boundary:** mori **detects and reports only; never remediates**. No restarting or killing a process, no reparenting, no systemd/pacman action, no deleting or resizing anything, no dispatch (kumitate), no OS-package state claims (tsukuroi), no endpoint health claims (kama). Credentials/oauth/server.token are shape only.

---

## 0. Executive Summary & Proposed Move

### 0.1 The Core Contradiction in Current Round Proposals
A review of the sibling proposals across this probation round exposes a structural contradiction between the finding catalog and lane provinces:
1. **The Automated Lane Remediation Fallacy:** `FindingIds.md` §5 notes that `WATCHDOG_*`/`WAVE_*` route to `kumitate`, while `JOURNAL_*`/`OOM_*`/`CGROUP_*` route to `tsukuroi`. But `tsukuroi-shokunin/PROVINCE.md:16-17` explicitly states: *"Never installs, upgrades, or removes packages; never restarts services. Detection and report; the operator remediates."* Likewise, `kama-shokunin/PROVINCE.md:22-26` explicitly states: *"kama never writes to `~/.config`, `~/.omp`, or systemd units. Those are operator-owned; kama detects and reports stale pins, and the operator repoints them."*
2. **The Operator Drowning Trap:** Conversely, routing every finding generically to `operator` as the sole actor leaves the human operator flooded with raw kernel crash traces, cgroup counter deltas, and cryptic wave JSON mismatches without the specialized diagnostic playbooks owned by `tsukuroi` (OS packages/systemd/drivers), `kumitate` (orchestration queue/wall/settlement), and `kama` (local model loopback port collisions).

### 0.2 The Proposed Move: Two-Tier Closed-Loop Remediation Handover
We synthesize a **Two-Tier Closed-Loop Remediation Handover Protocol** that distinguishes:
- **Tier 1: Triage & Diagnosis Owner (Domain Specialist):** The specialized shokunin lane that analyzes the finding using its own read-only diagnostic corpus, correlates multi-plane evidence, and emits a structured remediation proposal.
  - `tsukuroi`: OS substrate, pacman DB/library integrity, systemd user units, driver/DKMS/GSP state.
  - `kumitate`: Wave settlement, dispatcher queue/latch maintenance, watchdog log/state coherence, tmux sighting wall.
  - `kama`: Loopback model port squatter identification, consumer baseURL drift, llama.cpp served model reconciliation.
  - `mori-maintainers`: Census gate internal hygiene, fixture drift, probe refusals.
- **Tier 2: Actuation Authority (Remediation Actor):** The exact entity authorized to mutate state:
  - `kumitate`: Automated orchestration tooling actuation (e.g. `scripts/ufo-swarm-wave.mjs settle`, `scripts/fleet-dispatcher.mjs repend`, `scripts/ufo-sighting complete`).
  - `operator`: Privileged physical/system host mutations (restarts, pacman commands, cgroup limits, file deletion, mount provisioning, config writes).

mori **never** appears in either tier. It emits the observation with a typed `Handover Payload Shape` so the domain specialist can triage without re-running brittle probes, and the actuation authority can execute with zero oral context.

---

## 1. Axes Moved

| Axis | What this map moves |
|---|---|
| **coverage** | Maps 100% of finding ids (42 distinct ids across all 7 families: Watchdog, Waves, Kill/Journal, Cgroup Memory, Disk Runway, Lane Silence, Meta/Census Hygiene) to unambiguous owners. Zero orphaned findings. |
| **operability** | Provides exact CLI remediation entrypoints, explicit parameters, and runbook commands for both automated tooling (`kumitate`) and human runbooks (`operator`). Replaces vague "remediate" advice with executable handover commands. |
| **calibration** | Enforces honest boundaries: honors `tsukuroi` and `kama` read-only contracts; separates observation payload from remediation action; explicitly handles ambiguous multi-domain events (e.g. OOM kills) via disambiguation rules. |

---

## 2. Complete Remediation Routing Table

Legend:
- **Sev:** Severity (`crit` = critical, `high`, `warn`, `info`).
- **Triage Owner:** Domain specialist owning root-cause analysis.
- **Actuation Owner:** Entity authorized to execute the fix (`operator` or `kumitate`).
- **Handover Shape:** Key payload fields mori attaches to the finding line.

### 2.1 Watchdog Liveness & Fleet Driver

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `WATCHDOG_ABSENT` | crit | kumitate | operator | `driver=shokunin-watchdog; last_log_age_s=<N>; last_verb=<V>` | If fleet program is active: verify no orphaned panes, then launch driver: `nohup scripts/shokunin-watchdog.sh > .ufo/watchdog.log 2>&1 &`. If fleet-wrap intended: mark quiescent (`touch .ufo/fleet-wrap`). |
| `WATCHDOG_TICK_STALE` | high | kumitate | operator | `pid=<PID>; log_age_s=<N>; threshold_s=900` | Driver wedged. Inspect stack: `cat /proc/<PID>/stack`. Terminate stuck process: `kill -TERM <PID>`, then restart driver via operator shell. |
| `WATCHDOG_LOG_UNAVAILABLE` | info | kumitate | kumitate | `path=.ufo/watchdog.log; reason=<ENOENT\|EACCES>` | Restore directory permission or recreate empty log file: `touch .ufo/watchdog.log && chmod 0644 .ufo/watchdog.log`. |
| `WATCHDOG_LOG_STALE` | high | kumitate | operator | `log_age_s=<N>; last_line=<L>` | Cross-check with `WATCHDOG_ABSENT`. If driver absent without complete, triage daemon death (`operator-demand.md`). |
| `WATCHDOG_WEDGED` | warn | kumitate | operator | `pid=<PID>; tick_age_s=<N>; last_tick=<N>` | Driver process alive but loop blocked on subshell/lock. Trace syscall: `strace -p <PID> -s 128`. If unrecoverable, restart driver. |
| `WATCHDOG_NO_COMPLETE_LINE` | high | kumitate | kumitate / operator | `lane=<NAME>; last_verb=<V>; pid=<PID>` | Abnormal daemon disappearance mid-flight. Kumitate inspects queue: `scripts/fleet-dispatcher.mjs status`. Reselect or repend uncompleted mission. |
| `STATE_COUNTER_UNAVAILABLE` | info | kumitate | kumitate | `path=.ufo/state/<lane>.round; reason=ENOENT` | Initialize missing counter file to last known completed round from `watchdog.log`: `echo "<N>" > .ufo/state/<lane>.round`. |
| `STATE_COUNTER_LOG_MISMATCH` | warn | kumitate | kumitate | `lane=<NAME>; counter=<N>; log_last_round=<M>` | State counter drifted from last log dispatch. Kumitate aligns counter to authoritative log launch/wrap integer (`scripts/shokunin-watchdog.sh:80`). |
| `WATCHDOG_COUNTER_DRIFT` | warn | kumitate | kumitate | `lane=<NAME>; state_round=<N>; completed_in_log=<M>` | Align state counter with log event series. Run `StateCounterAudit` check logic. |
| `WATCHDOG_SURFACE_UNAVAILABLE` | info | tsukuroi | operator | `probe=watchdog-liveness; missing=pgrep\|/proc` | Host OS capability missing. Tsukuroi verifies `procps-ng` package: `pacman -Q procps-ng` or `/proc` mount options. |

### 2.2 Wave Settlement (`.ufo/waves/*`)

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `WAVE_REGISTRY_ABSENT` | warn | kumitate | kumitate | `wave=<DIR>; artifacts=<LIST>` | Dispatch artifact corrupted or incomplete. If `run.json` contains embedded registry, extract it: `node -e '...' > swarm-registry.json`. If draft only, clean workspace. |
| `WAVE_DISPATCH_ABSENT` | warn | kumitate | kumitate | `wave=<DIR>; has_registry=true` | Registry present without dispatch record. Kumitate inspects dispatch generator `scripts/ufo-swarm-wave.mjs` or marks wave as draft. |
| `WAVE_SPEC_ONLY` | info | kumitate | operator | `wave=<DIR>; spec=<PATH>` | Pre-dispatch draft wave. No remediation needed unless operator intended dispatch: `ufo-swarm-wave.mjs plan --spec <PATH>`. |
| `WAVE_UNSETTLED` | warn | kumitate | kumitate | `wave=<DIR>; age_s=<N>; missing=results.json` | Wave running or awaiting collection. If workers finished, execute settlement join: `scripts/ufo-swarm-wave.mjs settle --registry .ufo/waves/<DIR>/swarm-registry.json`. |
| `WAVE_UNSETTLED_AGE` | high | kumitate | kumitate | `wave=<DIR>; age_s=<N>; threshold_s=7200` | Stalled/abandoned wave. Kumitate invokes fail-closed settlement: `scripts/ufo-swarm-wave.mjs settle --registry ...` to write `ufo-swarm-results-v1` with `cancelled`/`aborted` rows. |
| `WAVE_SETTLED_PARTIAL` | warn | kumitate | kumitate | `wave=<DIR>; unmapped=<MEMBERS>; unexpected=<ROWS>` | Registry and results member set divergence. Kumitate re-runs `scripts/ufo-swarm-collect.mjs --wave ...` to reconcile bijection. |
| `WAVE_RESULTS_SCHEMA_DRIFT` | info | kumitate | kumitate | `wave=<DIR>; schema=<STR>` | Results file present but schema drifted from `ufo-swarm-results-v1`. Update schema marker or re-collect. |
| `WAVE_ORPHAN_RESULTS` | info | kumitate | kumitate | `wave=<DIR>; results=<PATH>` | Results artifact present without registry. Kumitate associates with parent run or archives orphan artifact. |
| `WAVE_REGISTRY_PATH_ABSENT` | info | kumitate | kumitate | `wave=<DIR>; pointed_path=<PATH>` | `.ufo/scopes/<scope>/swarm-registry.json` absent while wave-local registry exists. Kumitate updates pointed path or symlinks scope registry. |
| `WAVE_SURFACE_UNAVAILABLE` | info | tsukuroi | operator | `path=.ufo/waves; reason=EACCES\|ENOENT` | Verify directory permissions and filesystem integrity: `chmod 0755 .ufo/waves`. |

### 2.3 Kill / OOM Journal (`journalctl --user -b`)

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `OOM_KILL_EVENT` (Fleet-internal worker) | high | kumitate | kumitate / operator | `boot=<BOOT>; ts=<TS>; pid=<PID>; comm=<COMM>; cgroup=<CGROUP>; anon_rss_kb=<KB>` | OMP subagent or worker process killed (e.g. `python3` runner, `omp __omp_worker`). Kumitate reduces subagent concurrency (`maxLanes`), constrains prompt context, or fixes agent worker leak. Operator kills runaway tree if still lingering. |
| `OOM_KILL_EVENT` (Model Server) | high | kama | operator | `boot=<BOOT>; comm=llama-server; port=34113` | Local LLM server exceeded physical RAM. Kama recalculates GGUF layer offload and context window (`--ctx-size 16384` → `8192` in `~/.config/systemd/user/qwen-coder.service`). Operator restarts unit: `systemctl --user restart qwen-coder.service`. |
| `OOM_KILL_EVENT` (System / OS service) | high | tsukuroi | operator | `boot=<BOOT>; unit=<UNIT>; result='oom-kill'` | Systemd unit terminated by kernel OOM killer or systemd-oomd. Tsukuroi analyzes unit memory limit (`MemoryMax`) vs leak. Operator adjusts unit configuration or restarts service. |
| `KILL_SIGNAL_EVENT` / `SIGKILL_EVENT` | warn | tsukuroi / kumitate | operator | `boot=<BOOT>; pid=<PID>; comm=<COMM>; signal=9\|15` | External termination. Tsukuroi determines caller from audit logs. If fleet task killed by timeout, kumitate extends session timeout. |
| `SEGFAULT_EVENT` | warn | tsukuroi | operator | `boot=<BOOT>; comm=<COMM>; ip=<ADDR>; sp=<ADDR>; error=<N>` | Native binary memory corruption (observed on host: `pw-play`, `godot`, `love`). Tsukuroi checks package version (`pacman -Qo <binary>`), coredump (`coredumpctl info <PID>`), and library ABI mismatch. |
| `UNIT_FAIL_EVENT` / `UNIT_FAILURE_JOURNAL` | info / warn | tsukuroi | operator | `boot=<BOOT>; unit=<UNIT>; result=<RESULT>` | Systemd user unit failure. Tsukuroi inspects unit journal: `journalctl --user -u <UNIT> -b --no-pager -n 50`. Operator runs unit repair or reload: `systemctl --user daemon-reload && systemctl --user restart <UNIT>`. |
| `JOURNAL_UNAVAILABLE` | info | tsukuroi | operator | `probe=journal-user-boot; error=<ERR>` | User journal unreadable or systemd-journald degraded. Tsukuroi checks socket permissions: `systemctl status systemd-journald`. |
| `JOURNAL_PROBE_REFUSED` | info | mori-maintainers | mori-maintainers | `probe=journal; reason=<REASON>` | Gate policy refusal. Mori maintainers verify probe parameters stay strictly read-only and unprivileged. |

### 2.4 Cgroup Memory Events (`/sys/fs/cgroup/user.slice/...`)

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `CGROUP_OOM_KILL` | high | kumitate / tsukuroi | operator | `cgroup=<PATH>; oom_kill=<N>; current_bytes=<B>` | Cumulative slice kill counter incremented. Disambiguate per §2.3: if worker scope, kumitate throttles dispatch; if OS unit, tsukuroi tunes unit memory; operator reclaims memory. |
| `CGROUP_OOM_EVENT` | warn | kumitate | kumitate | `cgroup=<PATH>; oom_count=<N>; current=<B>` | Memory pressure trip without termination. Kumitate slows wave dispatch cadence or reduces parallel subagent slots. |
| `CGROUP_MEM_HIGH` / `CGROUP_MEMORY_HIGH` | warn | kumitate / tsukuroi | operator | `cgroup=<PATH>; high_count=<N>; current/max=<RATIO>` | Cgroup hitting throttle boundary. If `memory.high` configured, throttle is active. Operator evaluates increasing memory limit or pruning background processes. |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | info | tsukuroi | operator | `cgroup=<PATH>; reason=ENOENT` | Cgroup path missing or unmounted. Tsukuroi inspects cgroup2 unified hierarchy mount: `findmnt -t cgroup2`. |
| `MEM_HEADROOM_LOW` | warn | tsukuroi | operator | `avail_pct=<PCT>; threshold=10%; mem_available_kb=<KB>` | Host MemAvailable dropped below 10% (recalibrated from 15% via `oomd.conf(5)`). Tsukuroi inventories top RSS consumers: `ps -eo pid,ppid,user,rss,comm --sort=-rss`. Operator terminates or renices non-critical background jobs. |
| `MEM_HEADROOM_CRITICAL` | high | tsukuroi | operator | `avail_pct=<PCT>; threshold=5%; swap_free_kb=<KB>` | Immediate OOM danger. Conjunction of memory and swap exhaustion. Operator terminates memory hogs immediately to prevent kernel freeze. |
| `MEM_PRESSURE_UNAVAILABLE` | info | tsukuroi | operator | `probe=mem; error=<ERR>` | Inability to read `/proc/meminfo` or `/proc/pressure/memory`. Tsukuroi verifies kernel procfs integrity. |
| `CGROUP_UNAVAILABLE` | info | tsukuroi | operator | `cgroup=<PATH>; reason=ENOENT` | Surface missing; unavailable, not unhealthy. Tsukuroi verifies user slice hierarchy. |

### 2.5 Disk Runway (`df -P`)

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `DISK_LOW` | warn | kumitate (`/tmp`) / operator (`/home`) | operator | `mount=<MOUNT>; use_pct=<PCT>; avail_bytes=<B>; threshold=85%` | If `/tmp` (tmpfs 60% observed): kumitate cleans abandoned session temp directories (`/tmp/mori-census-selftest.*`, `ufo-*`). If `/home` (btrfs): operator balances btrfs chunks or prunes pacman cache (`paccache -r` or `/var/cache/pacman/pkg`). |
| `DISK_CRITICAL` | crit | operator | operator | `mount=<MOUNT>; use_pct=<PCT>; avail_bytes=<B>; threshold=95%` | Immediate disk exhaustion. Operator purges build artifacts (`target/`, `.cache/`) or expands volume. If `/tmp`, purge immediately to avoid swap thrashing. |
| `DISK_ROOT_UNAVAILABLE` / `DISK_UNAVAILABLE` | info | kumitate | operator | `mount=/scratch/tmp; fallback_in_use=/tmp` | `/scratch/tmp` absent (observed live). Kumitate uses `/tmp` fallback. Operator creates dedicated scratch mount on NVMe to prevent RAM-backed tmpfs pressure: `sudo mkdir -p /scratch/tmp && sudo chmod 1777 /scratch/tmp`. |
| `DISK_PROBE_UNAVAILABLE` | info | tsukuroi | operator | `probe=disk; error=<ERR>` | `/usr/bin/df` failure or coreutils missing. Tsukuroi inspects coreutils package: `pacman -Q coreutils`. |

### 2.6 Lane Silence

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `LANE_SILENT` | warn | kumitate | operator | `lane=<NAME>; elapsed_s=<N>; last_commit=<TS>; last_mtime=<TS>` | Lane inactive for >2 ticks (900s) with no commits or file mtime. Kumitate checks lane's mission row in `ufo-sighting`. Operator checks agent terminal or re-prompts lane. (Commit sparsity alone is never failure; silence rule honored). |
| `LANE_PROGRESSING_WEAK` | info | kumitate | kumitate | `lane=<NAME>; author=sibling; head_sha=<SHA>` | Lane has activity, but only authored by sibling seats. Informational compare data; no remediation required unless lane stalls. |
| `LANE_REPORT_ABSENT` | warn | kumitate | kumitate | `lane=<NAME>; round=<N>; expected_path=<PATH>` | Driver expects round N report but file is missing. Kumitate checks whether subagent completed or crashed before report write. |
| `LANE_GRADE_UNAVAILABLE` | info | kumitate | operator | `lane=<NAME>; reason=repo_missing\|not_git` | Lane worktree not initialized or corrupted. Operator checks `git status` or re-clones lane. |

### 2.7 Meta & Census Hygiene

| Finding ID | Sev | Triage Owner | Actuation Owner | Handover Payload Shape | Remediation Action & Entrypoint |
|---|---|---|---|---|---|
| `SURFACE_UNAVAILABLE` | info | mori-maintainers | mori-maintainers | `surface=<NAME>; reason=<REASON>` | Generic probe surface missing. Update probe fallback logic. |
| `PROBE_REFUSED` | info | mori-maintainers | mori-maintainers | `probe=<NAME>; reason=<REASON>` | A probe would violate read-only, non-remediating, or secrecy fences. Verify refusal correctness in `BoundaryRefusal.md`. |
| `CENSUS_PAYLOAD_VOLATILE` | info | mori-maintainers | mori-maintainers | `field=<NAME>` | Normalization filter dropped volatile field (pid, timestamp, raw bytes). Maintainer documentation only. |
| `CENSUS_SELFTEST_DRIFT` | high | mori-maintainers | mori-maintainers | `case=<NAME>; want_rc=<RC>; got_rc=<RC>; diff=<DIFF>` | Gate script internal failure. Maintainers fix bug in `mori-shokunin/tools/mori-census.sh` or update fixture definitions in `FixtureDesign.md`. |

---

## 3. Detailed Domain Ownership & Boundary Contracts

```
                   +----------------------------------+
                   |           MORI CENSUS            |
                   |   (Read-Only Probe & Detector)   |
                   +-----------------+----------------+
                                     | Emits Finding + Typed Payload
                                     v
                  +------------------------------------+
                  |    TIER 1: DOMAIN TRIAGE OWNER     |
                  +------------------+-----------------+
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
         v                           v                           v
  +--------------+            +--------------+            +--------------+
  |   TSUKUROI   |            |   KUMITATE   |            |     KAMA     |
  |  (OS Planes) |            | (Orchestrate)|            | (Model Ports)|
  +-------+------+            +-------+------+            +-------+------+
          |                           |                           |
          | Diagnostic                | Tooling                   | Endpoint
          | Runbook                   | Fixes                     | Diff
          v                           v                           v
+------------------+        +------------------+        +------------------+
| TIER 2: OPERATOR |        | TIER 2: KUMITATE |        | TIER 2: OPERATOR |
|  (Privileged)    |        | (Auto-Tooling)   |        | (Config Edits)   |
+------------------+        +------------------+        +------------------+
```

### 3.1 The Operator
- **Province & Authority:** Human owner of the host machine and supervisor of the shokunin program. Sole authority for root escalation, package installations, service restarts, kernel/driver changes, file deletion, and physical reboot.
- **Refuses:** Manual parsing of high-volume journal logs or raw memory dumps when automated domain tools exist.
- **Remediation Interface:** Receives triaged, validated runbooks from `tsukuroi`, `kumitate`, or `kama`. Never receives bare `mori` findings without a domain routing escort.

### 3.2 Tsukuroi-Shokunin (繕, Mending)
- **Province:** Host operability and OS substrate health: pacman package state (`pacman -Qkk`), systemd user units and timers (`systemctl --user`), kernel journal error triage, driver/firmware/DKMS plane (`nvidia-smi`, `dkms status`).
- **Strict Boundary (Refusal):** Tsukuroi **never** installs, upgrades, or removes packages; never restarts services (`PROVINCE.md:16-17`). It produces a structured diagnosis (`HEALTHY` / `DEGRADED` / `BLOCKED`), names the exact defective package or unit, and outputs the exact suggested operator command.
- **Handover from Mori:** Receives `JOURNAL_UNAVAILABLE`, `UNIT_FAIL_EVENT`, `SEGFAULT_EVENT`, system-scope `OOM_KILL_EVENT`, `MEM_HEADROOM_LOW`, `DISK_PROBE_UNAVAILABLE`.
- **Triage Protocol:** Runs `bash tools/tsukuroi-census.sh` to isolate whether the failure stems from a corrupted package file (`pacman -Qkk`), a failed systemd unit (`systemctl --user list-units --failed`), or a DKMS kernel driver mismatch. Outputs the remediation command to the operator.

### 3.3 Kumitate-Shokunin (組立, Assembly)
- **Province:** Orchestration mechanism and tooling: OMP task/hub dispatch, ufo-fsd runtime scripts, `fleet-dispatcher.mjs`, `ufo-sighting`, `ufo-swarm-wave.mjs`, `scripts/shokunin-watchdog.sh`.
- **Active Remediation Authority (Tooling):** Unlike tsukuroi, kumitate **owns and executes** automated orchestration remediation tooling:
  - Stalled waves → `scripts/ufo-swarm-wave.mjs settle --registry <path>` (writes terminal results, settles blocked queues).
  - Stalled tasks → `scripts/fleet-dispatcher.mjs repend --run <gq16>` (marks task repended, resets claim lock).
  - Dead sighting panes → `scripts/ufo-sighting complete --mission <id>` (cleans tmux wall without killing processes).
- **Handover from Mori:** Receives `WAVE_*` (all settlement findings), `WATCHDOG_*` (liveness and counter drifts), `LANE_*` (silence grades), worker-scope `OOM_KILL_EVENT`, `/tmp` tmpfs disk runway alerts.
- **Triage Protocol:** Evaluates wave registry vs results join. If an in-flight mission died, invokes `settle` or `repend`. If the watchdog driver is wedged, preps the restart command for the operator.

### 3.4 Kama-Shokunin (竈, Hearth)
- **Province:** Local model serving and loopback endpoint health: local LLM serving (`llama-server`), loopback ports (34113 vs 8080 squatter), baseURL configuration in consumer files (`opencode.json`, `janitor.md`, `distiller.md`), served model ID normalization.
- **Strict Boundary (Refusal):** Kama **never** writes to `~/.config`, `~/.omp`, or systemd units (`PROVINCE.md:22-26`). It detects baseURL drift, identifies port squatters via `docker ps` and `ss -ltnp`, and generates the repointing diff for the operator.
- **Handover from Mori:** Receives model-server-scoped `OOM_KILL_EVENT` (`comm=llama-server`), model port exhaustion, or model-related unit failures.
- **Triage Protocol:** Runs `bash tools/kama-probe.sh check` and `bash tools/kama-probe.sh listeners`. Verifies whether `llama-server` crashed due to excessive `--ctx-size` or whether port 34113 collided with another service. Emits configuration patch to the operator.

### 3.5 Mori Gate Maintainers
- **Province:** Internal maintenance of `mori-shokunin/tools/mori-census.sh`, fixture builders, and selftest cases.
- **Handover from Mori:** Receives `CENSUS_SELFTEST_DRIFT`, `PROBE_REFUSED`, `CENSUS_PAYLOAD_VOLATILE`.
- **Triage Protocol:** Fixes shell syntax errors, updates fixture expectations in `FixtureDesign.md`, or adjusts probe allowlists.

---

## 4. Second-Order Effects & Cross-Domain Coupling

Tracing second-order interactions across runtime, substrate, and contract reveals subtle failure loops that single-lane analysis misses:

### 4.1 The `/tmp` Scratch Spillover Loop (Disk Runway ↔ Memory Headroom ↔ OOM)
- **Observation:** `DiskRunway.md` confirms `/scratch/tmp` is absent on the host (`DEFAULT_SCRATCH_ROOT=/scratch/tmp` returns `No such file or directory`). The fallback chain in `ufo-sighting-lib/argv.mjs` selects `/tmp`.
- **Substrate Reality:** `/tmp` is a `tmpfs` (RAM-backed, currently 60% used, 9.1 GiB used of 15.1 GiB).
- **The Coupling:** Large swarm runs (such as 32-member parallel waves) writing session logs and node artifacts into `/tmp` directly consume physical host RAM and swap.
- **The Second-Order Effect:** A high disk usage alert on `/tmp` (`DISK_LOW` at 80% or 85%) is not merely a filesystem storage concern—it directly deprives the kernel of `MemAvailable`, drives swap out (`pswpout`), and triggers `CGROUP_OOM_KILL` / `OOM_KILL_EVENT`!
- **Remediation Routing:**
  1. `kumitate` must immediately reap ephemeral session scratch dirs from completed waves.
  2. `operator` must create a real disk-backed directory on NVMe (`/home/vgpnk/scratch` or `/scratch/tmp` on `/dev/mapper/root`, which has 835 GiB free) and set `TMPDIR=/scratch/tmp`, permanently decoupling swarm disk temp writes from host RAM!

### 4.2 The Unsettled Wave ↔ Queue Latch ↔ Watchdog Timeout Loop
- **Observation:** `WaveSettlement.md` identified 15 `dispatched-but-unsettled` waves (including 10 train waves with ages >10–26 hours) and zero settled waves outside `p1-repair`.
- **Runtime Mechanism:** `kumitate-shokunin/SKILL.md:125-129` explains that unsettled queue rows hold admissions in `admission-latch.json`. If a wave remains unsettled, waiters starve, queue capacity (256 rows) risks exhaustion, and `fleet-dispatcher.mjs` enters `reconcile_error`.
- **The Coupling:** If mori flags `WAVE_UNSETTLED_AGE` and nobody acts, the driver tick slows or blocks, eventually producing `WATCHDOG_TICK_STALE` or `WATCHDOG_WEDGED`.
- **Remediation Routing:**
  - `kumitate` must execute automated settlement: running `scripts/ufo-swarm-wave.mjs settle` on all orphaned train waves to flush the admission latches and clear queue capacity without deleting wave history.

### 4.3 OOM Kill Origin Disambiguation
- **Observation:** `LiveReceipt.md:223,235` documents an actual OOM kill on this boot: `pid 1732581 (python3), anon-rss ≈27.8 GB, in app-Hyprland-xdg-terminal-exec-dd9e67bd.scope`.
- **Contradiction:** Is this an OS kernel bug (`tsukuroi`), a model context leak (`kama`), an OMP agent worker leak (`kumitate`), or an operator interactive command (`operator`)?
- **Disambiguation Matrix:**
  1. If `cgroup` is `user.slice/user-1000.slice/user@1000.service/qwen-coder.service` → **Owner: kama + operator** (model server context allocation).
  2. If `comm` is `omp`, `node` (running worker JS), or `python3` under an `omp` parent PID → **Owner: kumitate** (swarm agent concurrency limit / worker memory ceiling).
  3. If `unit` is a systemd daemon (`systemd-coredump`, `systemd-journald`, `dockerd`) → **Owner: tsukuroi + operator** (system service configuration).
  4. If `cgroup` is `app-Hyprland-xdg-terminal-exec-*.scope` running an interactive user shell → **Owner: operator** (user launched heavy external task).
- **Remediation Routing:** Mori payload includes `comm`, `cgroup`, and `pid_parent` so the finding routes directly to the correct owner rather than causing cross-lane ping-pong.

### 4.4 Watchdog Absence vs. Fleet-Wrap Quiescence
- **Observation:** `LiveReceipt.md` and `StateCounterAudit.md` observe that `pgrep -af shokunin-watchdog` is empty, but the last log entries represent a clean `fleet-wrap` of all 9 lanes.
- **Contract Tension:** `FindingIds.md` notes that `WATCHDOG_ABSENT` is `critical`. However, if the fleet program has completed, process absence is intentional quiescence.
- **Remediation Routing:**
  - Route to `operator` to distinguish program state. If a new wave is active (e.g. `shokunin12h-20261014-p4-mori-r1` is running right now!), driver absence is indeed a real defect requiring operator launch: `nohup scripts/shokunin-watchdog.sh > .ufo/watchdog.log 2>&1 &`.

---

## 5. Risks and Falsification

### 5.1 Risks of the Proposed Routing Model
1. **Tooling Premature Settlement Risk:** If `kumitate` auto-settles an unsettled wave (`WAVE_UNSETTLED_AGE`) while workers are still computing or slow on network/model responses, it could prematurely mark active agents as `cancelled`.  
   *Mitigation:* Handover requires checking `newest_file_age_s` against a generous stall bound (e.g. 7200s / 2 hours), not merely elapsed wall clock.
2. **Operator Bypass Risk:** If an automated script attempts to execute privileged mutations (restarting services or deleting disk roots) under the guise of "speed", it violates the hard boundary in `PROVINCE.md`.  
   *Mitigation:* Enforce Tier 2 boundary: `tsukuroi` and `kama` scripts must remain 100% read-only, emitting text runbooks for the operator.
3. **Circular Handover Starvation:** If an OOM kill lacks parent PID info, `kumitate` and `tsukuroi` could each claim the other owns it.  
   *Mitigation:* Default to `operator` whenever process ancestry is ambiguous.

### 5.2 Verification Checks (Cold Agent Verifiable)

The validity of this routing contract can be verified cold on this host without oral context using read-only commands:

1. **Verify Tsukuroi Read-Only Boundary:**
   ```bash
   grep -E "Never (installs|upgrades|restarts)" /home/vgpnk/Projects/shokunin/tsukuroi-shokunin/PROVINCE.md
   # PASS: Proves tsukuroi refuses mutating actions; Tier 1 triage only.
   ```

2. **Verify Kama Read-Only Boundary:**
   ```bash
   grep -E "never writes to" /home/vgpnk/Projects/shokunin/kama-shokunin/PROVINCE.md
   # PASS: Proves kama refuses config edits; Tier 1 triage only.
   ```

3. **Verify Kumitate Settlement Actuation Tooling Exists:**
   ```bash
   test -f /home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs || \
   test -f /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs
   # PASS: Proves kumitate owns the executable wave settlement CLI.
   ```

4. **Verify Mori Live Gate Contains Zero Remediation Verbs:**
   ```bash
   python3 -c '
   import re, sys
   from pathlib import Path
   gate = Path("/home/vgpnk/Projects/shokunin/mori-shokunin/tools/mori-census.sh")
   if not gate.exists(): sys.exit(0)
   content = gate.read_text()
   forbidden = re.findall(r"\b(systemctl (?:restart|stop|start)|kill -9|pacman -[SyuR]|pkill)\b", content)
   assert len(forbidden) == 0, f"Found forbidden remediation verbs: {forbidden}"
   print("PASS: mori gate is 100% read-only detection")
   '
   ```

5. **Verify Scratch Path Absence Coupling:**
   ```bash
   test -e /scratch/tmp; echo "scratch_tmp_present=$?"
   # Expected: exit 1 (absent) -> confirms coupling of scratch writes to /tmp tmpfs.
   ```

---

## 6. Synthesis Summary for Parent Integration

The parent integrator (Sol 6.1) should adopt this routing contract when landing the census report and the corpus knowledge notes:
1. Land the routing table in `corpus/knowledge/owner-routing.md` (or inline in `corpus/README.md`).
2. Update `mori-shokunin/SKILL.md` Decision Table to explicitly cross-reference the Tier 1 Triage Owner and Tier 2 Actuation Owner for each finding family.
3. Keep `mori-census.sh` strictly free of remediation verbs (enforcing the closed-set proof documented in `BoundaryRefusal.md`).
4. In the round 1 report (`.ufo/reports/round-1/mori.md`), include this Owner Map under the optional post-SHONEN section `## Owner routing` as the definitive answer to "who acts when mori reports".
