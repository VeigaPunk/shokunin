# LiveReceipt — mori-shokunin r1 live host/fleet census

**Role:** leaf member LiveReceipt (UFO-FSD scribe for live probes).  
**Lane:** mori-shokunin (森) — detect and report only; **no remediation** performed.  
**Wave:** `shokunin12h-20261014-p4-mori-r1` / `Shokunin12hP4MoriR1`.  
**Host:** `plazir27` (Linux 7.2.3-arch1-3 x86_64).  
**User:** `vgpnk` (uid 1000).  
**Boot id:** `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`  
**Boot start (observed):** `2026-10-13T11:02` local (`who -b` / `last -x`).  
**Uptime at close:** ~1 day 10:31.

This file is **execution evidence**, not a gate verdict and not a judge claim.  
Finding ids follow the wave contract in `FindingIds.md`. Severity is carried for compare; parent/gate owns `MORI_CENSUS: CLEAN|DRIFT`.

---

## 0. Axes (godspeed)

| Axis | What this receipt optimizes |
|---|---|
| **coverage** | All province surfaces probed: watchdog, waves, journal kill/OOM, cgroup memory, disk runway, lane silence, tmux/sighting, host mem/load |
| **operability** | Every row names command + measured timestamp; missing → `unavailable` (never `unhealthy`) |
| **calibration** | observation / inference / unknown separated; stable ids; before→after window recorded |

---

## 1. Measure window (before → after)

| Label | UTC | Local (`-03:00`) | Notes |
|---|---|---|---|
| **T0 before** | `2026-10-15T00:31:36Z` | `2026-10-14T21:31:36-03:00` | First full probe batch (`date`, `ps`, `df`, `journalctl`, waves ls) |
| **T1 mid** | `2026-10-15T00:32:01Z` … `00:32:48Z` | `21:32:01` … `21:32:48` | Cgroup user.slice, PSI, wave settlement scan, watchdog log/state |
| **T2 after** | `2026-10-15T00:33:23Z` | `2026-10-14T21:33:23-03:00` | Closing snapshot (mem, load, journal class counts, members ls) |

**Window length:** ~107 s. Host remained interactive; no probe wrote, restarted, killed, or dispatched anything.

**Compare note:** T0→T2 memory/process deltas are normal fleet churn under the live mori swarm (member reports appearing; omp workers). They are **payload**, not remediation evidence.

---

## 2. Surface census (observations)

### 2.1 Host identity & load

| Field | T0 | T2 | Command |
|---|---|---|---|
| hostname | `plazir27` | same | `hostname` |
| kernel | `7.2.3-arch1-3 #1 SMP PREEMPT_DYNAMIC … x86_64` | same | `uname -a` |
| nproc | 32 | 32 | `nproc` |
| loadavg | `0.51 0.54 0.57` | `0.16 0.42 0.52` | `cat /proc/loadavg` / `uptime` |
| `/proc/uptime` | `124417.75` s | (not re-read; wall +~107s) | `cat /proc/uptime` @T0 |
| process count | 597 | 597 | `ps -e --no-headers \| wc -l` |
| sessions | 4 users @T0; `w` showed 1 user line @T1 | tmux pts attached | `w` / `who` |
| zombies | — | 4 (`uwsm-app`×3, `systemctl`×1) | `ps -eo stat,pid,cmd` awk `/Z/` |

**Inference (not observation):** load cooled during the census window; not a health claim.

### 2.2 Memory runway (host)

Commands: `free -b`, `grep … /proc/meminfo`, `cat /proc/pressure/memory`.

| Metric | T0 | T2 |
|---|---|---|
| MemTotal | 32483102720 B (≈30.26 GiB) / 31721780 kB | same |
| MemAvailable | 21679656960 B ≈ 20.19 GiB; meminfo 21170416 kB | meminfo **20701920 kB**; free avail 21175857152 B |
| MemFree | 968572928 B | 443719680 B |
| SwapTotal | 36779188224 B | same |
| Swap used | ≈10067566592 B (≈9.38 GiB) | ≈10067456000 B |
| PSI memory (`/proc/pressure/memory`) | `some avg10=0.00 …` / `full avg10=0.00 …` | (not re-sampled; was zero pressure avgs @T1) |
| Available % of total (meminfo) | ≈66.7% | ≈65.3% |

**Finding predicate (FindingIds defaults):** warn if available < 15% total → **not fired**.  
→ clean label `MEM_HEADROOM_OK` (no finding id).

| id | sev | subject | status |
|---|---|---|---|
| *(none)* | — | `scope=host` | MEM_HEADROOM_OK |

### 2.3 Disk runway

Commands: `df -P`, `df -h -x tmpfs…`, `python3 os.statvfs`, `test -e /scratch/tmp`.

| mount / path | fs | size | used | avail | use% | T0→T2 |
|---|---|---|---|---|---|---|
| `/` (`/dev/mapper/root`) | btrfs-like mapper | 974646272 KiB (≈930G) | ≈96589444 KiB | ≈875440588 KiB | **10%** | used +~592 KiB @T2 (noise) |
| `/home` | same device | same | same | same | **10%** | same |
| fleet root `/home/vgpnk/Projects/shokunin` | same | same | — | avail ≈896451162112 B | **9.91%** used_pct (statvfs) | — |
| `/tmp` | tmpfs | 15860892 KiB | 9505280 KiB | 6355612 KiB | **60%** | unchanged @T2 |
| `/boot` | `/dev/nvme0n1p1` | 2093048 KiB | 285440 KiB | 1807608 KiB | **14%** | — |
| `/scratch` | — | — | — | — | — | **absent** |
| `/scratch/tmp` | — | — | — | — | — | **`test -e` exit 1** → `unavailable` |

Threshold defaults (FindingIds proposal): `DISK_WARN_PCT=85`, `DISK_CRIT_PCT=95`, `DISK_TMP_WARN_PCT=80`, avail floors 5 GiB / 1 GiB.

| id | sev | subject | status | payload |
|---|---|---|---|---|
| *(none)* | — | `mount=/` | DISK_RUNWAY_OK | use%=10 avail≈835G |
| *(none)* | — | `mount=/tmp` | DISK_RUNWAY_OK under defaults | use%=60 < 80 |
| `DISK_ROOT_UNAVAILABLE` | info | `mount=/scratch/tmp` | **emit** | path absent; not unhealthy |

### 2.4 Watchdog liveness (shokunin driver)

Commands @T1/`T2`:

```text
pgrep -af 'shokunin-watchdog'
pgrep -af 'scripts/shokunin-watchdog'
stat /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
tail -n 30 /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
ls -la /home/vgpnk/Projects/shokunin/.ufo/state/
```

| Observation | Value |
|---|---|
| `pgrep` shokunin-watchdog | **empty** (T1 and T2) |
| log path | `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log` **readable** |
| log mtime | `2026-10-13T16:44:48.524089950-03:00` (size 19396) |
| log last lines | fleet-wrap series ending `2026-09-28T23:55:00-03:00 tick=3` with `wrap <lane> … NOT respawning (fleet-wrap)` for aggregator/kasegi/kengaku/kake/kumitate/kotoba/kagi/kama/protocol |
| age of log mtime at T2 | ≈ **28.8 h** since mtime; content timestamps are older (Sep 28) — observation only |
| `.ufo/state/*.round` | present for: aggregator=10, kagi=16, kake=16, kama=1, kasegi=17, kengaku=13, kotoba=16, kumitate=16, protocol=14 (all mtime `2026-10-13 16:44`) |
| mori / chousa / tsukuroi state files | **absent** in `.ufo/state/` (no `mori.round`) → not a counter mismatch; surface simply has no mori row |

**Related live process (NOT the shokunin-watchdog driver):**

| pid | etime @T1 | cmd |
|---|---|---|
| 937995 | ~1h18m | `tmux new-session -d -s ufo_sighting … ufo-sighting.mjs __idle` |
| 938031 | ~1h18m | `node … ufo-sighting.mjs __idle` |
| 938122 | ~1h18m | `node … ufo-sighting.mjs overview --watch` |
| 938085 | ~1h18m | `alacritty --class=org.omarchy.ufo-sighting -e …/ufo-sighting` |
| 237 | 1-10:34 | kernel `watchdogd` (OS; out of province as ownership) |
| 1203316 | ~8h21m | `Hyprland --watchdog-fd 4` (compositor; not fleet driver) |

`tmux ls` @T0/T2: `ufo_sighting: 1 windows (created Wed Oct 14 20:14:40 2026) (attached)`.

| id | sev | subject | status | notes |
|---|---|---|---|---|
| `WATCHDOG_ABSENT` | critical | `driver=shokunin-watchdog` | **emit** under profile `expect_driver=yes` | no matching pid |
| — | — | wrap-quiescence | **reading** | last log lines are explicit `fleet-wrap`; gate may take `expect_driver=wrap-ok` and downgrade — that is gate input, not a second id |
| `WATCHDOG_LOG_UNAVAILABLE` | info | `log=.ufo/watchdog.log` | **not emit** | file readable |
| `STATE_COUNTER_UNAVAILABLE` | info | `path=.ufo/state` | **not emit** for dir | dir lists; mori-specific counter file simply not in roster snapshot |

### 2.5 Wave settlement (`.ufo/waves/*`)

Command: directory walk + JSON key presence @T1; newest-file age @T2 (`python3`).

**Wire shapes observed:**

- **train:** `swarm-registry.json` + `dispatch.json` (+ optional `closeout.*`); **no** `results.json` on any train dir sampled.
- **12h/ufo-swarm:** `run.json` (`schema: ufo-swarm-wave-dispatch-v1`) + `spec.json` + optional `task-response.json` + optional `results.json` (`p1-repair` only among 12h phases).

#### Train waves (dispatched, no results.json)

| wave | reg | disp | res | newest_file_age_s @T2 | grade |
|---|---|---|---|---|---|
| shokunin-train-20261013 | Y | Y | N | 95330 | `WAVE_UNSETTLED` + `WAVE_UNSETTLED_AGE` (≥1800s) |
| …-w2 | Y | Y | N | 89551 | same |
| …-w3 | Y | Y | N | 84381 | same |
| …-w4 | Y | Y | N | 81519 | same |
| …-w5 | Y | Y | N | 70473 | same |
| shokunin-train-20261014-w6 | Y | Y | N | 53225 | same (has `closeout.json`) |
| …-w7 | Y | Y | N | 49865 | same |
| …-w8 | Y | Y | N | 45385 | same |
| …-w9 | Y | Y | N | 41099 | same |
| shokunin-train-20261101-w10 | Y | Y | N | 36596 | same |

**Reading:** `closeout.json` is **not** the settlement join defined as `results.json` / results members. Unsettled ≠ failed.

#### Spec-only / alternate registry name (no swarm-registry.json)

| wave | artifacts | id |
|---|---|---|
| shokunin-train-20261101-w11 | spec+closeout+x* | `WAVE_SPEC_ONLY` (info) — no swarm-registry/dispatch |
| …-w12 …-w16 | `registry.json` (not `swarm-registry.json`) + spec | **observation:** non-canonical registry filename; treat as shape drift / possible `WAVE_REGISTRY_ABSENT` under strict name match — payload `registry_filename=registry.json` |
| …-w17, w19 | spec±closeout/SHARED | `WAVE_SPEC_ONLY` |
| w18, w20 | no top-level dispatch artifacts in scan | non-subject or empty — no forced unhealthy |

#### 12h program waves

| wave | run | res | task-response | members_dir files @scan | newest_age_s | grade |
|---|---|---|---|---|---|---|
| shokunin12h-20261014-p1-audit | Y | N | Y | 31 | 1053 | `WAVE_UNSETTLED` (age < 1800 → **no** AGE) |
| shokunin12h-20261014-p1-repair | Y | **Y** | Y | 32 | 1151 | **settled shape** (`results.json` present; schema keys `schema,members`) |
| shokunin12h-20261014-p2-kumitate | Y | N | Y | 24 | 568 | `WAVE_UNSETTLED` young |
| shokunin12h-20261014-p3-kengaku | Y | N | N | 0 | 1007 | `WAVE_UNSETTLED` young |
| **shokunin12h-20261014-p4-mori-r1** | Y | N | Y | 3→growing | 320 | `WAVE_UNSETTLED` **in-flight** (this wave) |
| shokunin12h-20261014-p5-chousa-r1 | Y | N | N | 0 | 303 | `WAVE_UNSETTLED` young |

**This wave run.json @T1:**

- `schema`: `ufo-swarm-wave-dispatch-v1`
- `wave`: `Shokunin12hP4MoriR1`
- `counts`: `{spawn:32, resume:0, total:32}`
- `registry.schema`: `ufo-swarm-registry-v1`, **32 members**
- `taskCall.tasks`: 32
- `results.json`: **absent** (`has_results False`)

**Legacy dirs** (`kaidoku-*`, `round-*`, `aggregator-r11`): no top-level reg/run/disp/res/spec in the settlement scanner → not scored as dispatched waves (non-subjects for WAVE_* join). Age values exist but without dispatch artifacts.

| id | sev | example subjects | status |
|---|---|---|---|
| `WAVE_UNSETTLED` | warn | train w6–w10, 12h p1-audit/p2/p3/p4/p5 | **emit** |
| `WAVE_UNSETTLED_AGE` | high | all listed train waves with age≫1800s | **emit** |
| `WAVE_SPEC_ONLY` | info | train w11,w17,w19 | **emit** |
| *(settled)* | — | `shokunin12h-20261014-p1-repair` | no UNSETTLED |

### 2.6 Journal kill / OOM classes (this boot)

Commands:

```text
journalctl -b --no-pager -q
journalctl --user -b --no-pager -q
# class greps (counts @T2)
```

**Boot id:** `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`

| class | count @T2 | source | notes |
|---|---|---|---|
| invoked oom-killer | **1** | system journal | `GpuWatchdog invoked oom-killer` |
| `oom-kill:` line | **1** | system | constraint=CONSTRAINT_NONE, global_oom |
| `Out of memory: Killed process` | **1** | system | pid **1732581** `python3`, anon-rss ≈27.8 GB, `oom_score_adj=200` |
| user unit `Failed with result 'oom-kill'` | **1** | `--user` | `app-Hyprland-xdg-terminal-exec-dd9e67bd.scope` @ `2026-10-13T23:44:31-03:00` |
| segfault (case-insensitive) | **588** | system | many `pw-play`, `love`, `godot`, … |
| user `dumped core` | **1044** | `--user` | top names: love 574, godot 318, pw-play 84, MainThread 40, blender 7, waybar 6, … |
| `Failed with result` (user, all) | **2** | `--user` | includes the oom-kill unit fail |
| dbus oom1 activation miss | 1 line @T0 sys grep | system | `Activation request for 'org.freedesktop.oom1' failed` — **observation**; not classified as OOM_KILL |

**Canonical OOM event (verbatim class fields):**

```text
2026-10-13T23:44:30 plazir27 kernel: GpuWatchdog invoked oom-killer: …
2026-10-13T23:44:30 plazir27 kernel: oom-kill:… task=python3,pid=1732581,uid=1000
2026-10-13T23:44:30 plazir27 kernel: Out of memory: Killed process 1732581 (python3) total-vm:56727648kB, anon-rss:27873696kB, …
2026-10-13T23:44:31-03:00 plazir27 systemd[1573]: app-Hyprland-xdg-terminal-exec-dd9e67bd.scope: Failed with result 'oom-kill'.
```

**fleet_relevant payload:** cgroup path is Hyprland xdg-terminal scope (interactive terminal python), not tmux/ufo-sighting/watchdog — `fleet_relevant=false` for driver, still **in-boot OOM evidence**.

| id | sev | subject | status |
|---|---|---|---|
| `OOM_KILL_EVENT` | high | `boot=d7f0bc8d-…;ts=2026-10-13T23:44:30` | **emit** (dedup one physical kill; unit fail not double-fired as UNIT_FAIL) |
| `SEGFAULT_EVENT` | warn | boot aggregate + per-signature samples | **emit** (N=588 segfault lines / 1044 user cores) — gate may bin by comm |
| `JOURNAL_UNAVAILABLE` | info | — | **not emit** (journals readable) |

### 2.7 Cgroup memory events

Commands: `cat` on cgroupfs paths @T1; re-read user.slice @T2.

| path | memory.events | memory.current | memory.max | memory.high | memory.peak | swap.current |
|---|---|---|---|---|---|---|
| `/sys/fs/cgroup/memory.events` (root) | **unavailable** (No such file) | unavailable | unavailable | unavailable | — | — |
| `/sys/fs/cgroup/memory.pressure` | readable (`avg10=0.00`) | — | — | — | — | — |
| `/sys/fs/cgroup/user.slice` | `oom_kill 1` (low/high/max/oom=0) | ~25.3e9 @T2 | max | max | — | — |
| `/sys/fs/cgroup/user.slice/user-1000.slice` | **oom_kill 1**, sock_throttled 77943 | 24914141184 @T1 → **25284395008** @T2 | max | max | 30699745280 | 10033762304 |
| `…/user@1000.service` | oom_kill **0** | 23789121536 | max | max | 27360264192 | 9286422528 |
| `…/app.slice` | oom_kill 0 | 23660318720 | max | max | 27206492160 | 9162694656 |
| `…/system.slice` | all 0 | 835756032 | max | max | — | — |

**Top app scopes by `memory.current` @T1 (bytes):**

| current | cgroup leaf |
|---|---|
| 11508424704 | `app-Hyprland-xdg-terminal-exec-6bd28f41.scope` (omp session host) |
| 8183648256 | `…-4b06c09c.scope` |
| 2355408896 | `…-c550e4d0.scope` |
| 588095488 | `…-e9c449da.scope` |
| ~141e6 | 1Password scopes |

All listed scope `memory.events` showed `oom_kill 0` at sample (kill accounted on ancestor `user-1000.slice` / `user.slice`).

| id | sev | subject | status |
|---|---|---|---|
| `CGROUP_OOM_KILL` | high | `cgroup=/sys/fs/cgroup/user.slice/user-1000.slice` | **emit** (`oom_kill=1`, baseline=boot-zero absolute) |
| `CGROUP_OOM_KILL` | high | `cgroup=/sys/fs/cgroup/user.slice` | **emit** (same counter visible) |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | info | root cgroup memory.current | **emit** for root-only missing files |
| `MEM_HEADROOM_LOW` | warn | host | **not emit** |

### 2.8 Fleet process cluster (rss snapshot)

Command: `ps -eo pid,ppid,user,rss,… --sort=-rss` @T0; fleet grep @T1.

| pid | rss_KiB @T0 | cmd (truncated) |
|---|---|---|
| 935236 | 1510048 | `omp` (ppid 935067) |
| 1205136 | 752388 | `kimi` |
| 1205475 | 719104 | `devin acp` |
| 1375045 / 1483934 | 512048 / 428552 | omp python runners |
| 935379 | 174348 | `rea mcp` (npx) |
| many | — | `omp __omp_worker_js_eval_process` under 935236 |

Aggregate @T1: `count=36` matching omp|kimi|devin|ufo-sighting, `rss_kb≈5194628` (~5.0 GiB RSS sum — double-counts threads/children possible).

**oom_score** top RSS pids mostly `score_adj=200`; dockerd `adj=-500`.

### 2.9 Lane silence — mori-shokunin (this mission)

Commands @T2:

```text
git -C …/mori-shokunin log -1 --format='%H %ci %s'
git -C …/mori-shokunin status -sb
find …/mori-shokunin -maxdepth 3 -type f
ls …/mori-shokunin/corpus/
ls …/waves/…/members/
```

| field | observation |
|---|---|
| HEAD | `27acf40c418b6d790b58202094e241e571ee6f56` @ `2026-10-14 21:18:00 -0300` — `mint: real province…` |
| worktree | clean `## master` (no unstaged in lane repo) |
| `tools/mori-census.sh` | **absent** (no `tools/` dir) — expected pre-land; parent integrates |
| `corpus/knowledge|lessons` | only `.gitkeep` — map empty (round job is to build it) |
| member reports @T2 | `CorpusMap.md`, `FindingIds.md`, `FixtureDesign.md` (this LiveReceipt follows) |
| wave age | ~minutes since dispatch; member mtimes advancing during census |

**Grade:** **progressing** for mori r1 (lane-authored mint commit + live member report writes in wave members dir).  
→ no `LANE_SILENT`. Not `progressing-weak` (activity is in-mission wave output + seed commit).

| id | sev | subject | status |
|---|---|---|---|
| `LANE_SILENT` | warn | `lane=mori` | **not emit** |
| `LANE_PROGRESSING_WEAK` | info | `lane=mori` | **not emit** |

### 2.10 Meta / refused probes

| probe | result |
|---|---|
| write/restart/kill/dispatch/pacman/systemd mutate | **not attempted** — policy refuse |
| credential/oauth/server.token content read | **not attempted** — shape only |
| `docker ps` | empty output (no running containers listed); docker daemon pid 737528 was live @T0 — observation only |
| root `/sys/fs/cgroup/memory.events` | unavailable (ENOENT) |
| `/scratch/tmp` | unavailable (absent) |
| live `MORI_CENSUS` gate binary | unavailable (`tools/mori-census.sh` not landed) → not a host unhealthy |

| id | sev | subject | status |
|---|---|---|---|
| `DISK_ROOT_UNAVAILABLE` | info | `/scratch/tmp` | emit |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | info | root memory.current | emit |
| `PROBE_REFUSED` | info | — | none required this run |
| `SURFACE_UNAVAILABLE` | info | `surface=mori-census-gate` | optional note: gate script not in tree yet |

---

## 3. Before → after delta (volatile payload)

| metric | T0 | T2 | delta reading |
|---|---|---|---|
| MemAvailable (meminfo kB) | 21170416 | 20701920 | −468496 kB (~0.45 GiB) under live swarm |
| user-1000.slice memory.current | 24914141184 | 25284395008 | +~370 MB |
| loadavg 1m | 0.51 | 0.16 | down |
| ps count | 597 | 597 | flat |
| user.slice oom_kill | 1 | 1 | **stable** (no new kill during window) |
| shokunin-watchdog pgrep | empty | empty | stable absent |
| tmux ufo_sighting | attached | attached | stable live |
| p4 members/*.md | 2 files @ early T0 ls | 3 files @T2 (`CorpusMap` added) | wave progressing |
| disk / use% | 10% | 10% | stable |

**No remediation. No process signal. No file deletes.**

---

## 4. Findings table (compare contract)

Stable keys: `id + subject`. Severity from FindingIds catalog.

| id | sev | subject | first_seen | payload (non-volatile summary) |
|---|---|---|---|---|
| `WATCHDOG_ABSENT` | critical | `driver=shokunin-watchdog` | T1 | pgrep empty; log mtime 2026-10-13T16:44:48-03; last lines fleet-wrap; expect_driver profile-dependent |
| `WAVE_UNSETTLED` | warn | `wave=shokunin-train-20261013` | T1 | reg+disp, no results.json |
| `WAVE_UNSETTLED_AGE` | high | `wave=shokunin-train-20261013` | T2 | newest_file_age_s≈95330 ≥1800 |
| `WAVE_UNSETTLED` + `WAVE_UNSETTLED_AGE` | warn/high | `wave=shokunin-train-20261013-w2` … `w5`, `20261014-w6`…`w9`, `20261101-w10` | T1/T2 | same pattern; ages 36ks–89ks |
| `WAVE_UNSETTLED` | warn | `wave=shokunin12h-20261014-p1-audit` | T1 | run+task-response, no results; age≈1053s |
| `WAVE_UNSETTLED` | warn | `wave=shokunin12h-20261014-p2-kumitate` | T1 | age≈568s |
| `WAVE_UNSETTLED` | warn | `wave=shokunin12h-20261014-p3-kengaku` | T1 | age≈1007s |
| `WAVE_UNSETTLED` | warn | `wave=shokunin12h-20261014-p4-mori-r1` | T1 | **this wave in flight**; 32 registry members; no results yet |
| `WAVE_UNSETTLED` | warn | `wave=shokunin12h-20261014-p5-chousa-r1` | T1 | age≈303s |
| `WAVE_SPEC_ONLY` | info | `wave=shokunin-train-20261101-w11` (+w17,w19) | T1 | spec without swarm-registry/dispatch |
| `OOM_KILL_EVENT` | high | `boot=d7f0bc8d-938e-4249-b4a1-f250cbfacf58;ts=2026-10-13T23:44:30-03` | T0 | python3 pid 1732581; unit oom-kill fail; fleet_relevant=false (terminal scope) |
| `SEGFAULT_EVENT` | warn | `boot=d7f0bc8d-…;class=segfault` | T0 | sys segfault lines=588; user dumped core=1044 |
| `CGROUP_OOM_KILL` | high | `cgroup=/sys/fs/cgroup/user.slice/user-1000.slice` | T1 | oom_kill=1 |
| `CGROUP_OOM_KILL` | high | `cgroup=/sys/fs/cgroup/user.slice` | T1 | oom_kill=1 |
| `DISK_ROOT_UNAVAILABLE` | info | `mount=/scratch/tmp` | T1 | path absent |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | info | `cgroup=/sys/fs/cgroup` (root memory.current) | T0 | ENOENT |

**Explicit non-findings (clean labels):**  
`DISK_RUNWAY_OK` (`/`, `/home`, fleet root, `/tmp` under proposal thresholds), `MEM_HEADROOM_OK`, `LANE_PROGRESSING` (mori), journal readable, p1-repair settled shape.

**Unknowns (not forced to ids):**  
- Whether operator profile sets `expect_driver=wrap-ok` for post-2026-09-28 fleet-wrap (would change gate weight of `WATCHDOG_ABSENT`).  
- Whether train `closeout.json` should count as terminal settlement in a future id revision (currently **does not** clear `WAVE_UNSETTLED`).  
- Exact 1:1 join quality inside `p1-repair/results.json` members vs registry (file present → settled **shape**; partial join would be `WAVE_SETTLED_PARTIAL` — not fully diffed here).

---

## 5. Command ledger (operability)

| # | when | command (abbrev) | outcome |
|---|---|---|---|
| 1 | T0 | `date -u`, `date`, `hostname`, `uname -a`, `uptime`, `cat /proc/uptime`, `cat /proc/loadavg` | ok |
| 2 | T0 | `free -b`, `free -h`, `grep /proc/meminfo` | ok |
| 3 | T0 | `df -B1` / `df -h` / `df -P`, `os.statvfs` | ok |
| 4 | T0 | `tmux ls`, `ps -eo … --sort=-rss`, `ps` count | ok |
| 5 | T0 | oom_score sample top RSS; `/proc/self/cgroup` | ok |
| 6 | T0 | `journalctl --user -b` grep oom/core; `journalctl -b` oom | ok |
| 7 | T0 | `ls .ufo/waves` | ok |
| 8 | T1 | cgroup `user.slice` / `user-1000.slice` / `user@1000` / `app.slice` / `system.slice` memory.* | ok; root memory.events ENOENT |
| 9 | T1 | `/proc/pressure/{memory,cpu,io}` | ok avgs 0 |
| 10 | T1 | core/segfault class counts; `pgrep` watchdog; `stat`+`tail` watchdog.log; `ls` `.ufo/state` | ok |
| 11 | T1 | wave settlement python scan; fleet ps grep | ok |
| 12 | T1 | `test -e /scratch/tmp` | exit 1 unavailable |
| 13 | T2 | journal class counts; mem/cgroup re-read; `git -C mori-shokunin`; members ls | ok |

**Blocked/refused:** none beyond policy (no writes, no external fetch, no secret paths).

---

## 6. Provenance & limits

| claim | authority |
|---|---|
| All numeric host facts above | commands in §5 at timestamps in §1 |
| Finding id strings / severity | wave member `FindingIds.md` (contract), not invented here |
| Province bounds | `mori-shokunin/PROVINCE.md`, `SKILL.md` |
| Seed commit | `27acf40` observed as HEAD on lane repo |
| Gate script content | **not** implemented in this member (parent / GateDesign) |
| Judge verdict | **none** — unjudged fleet wave; advisory data only |

**Limits:**

- Journal class counts are whole-boot aggregates; individual SEGFAULT rows are not fully enumerated in this receipt (samples + histograms only).  
- Wave age uses **newest file mtime** when `dispatched_at` absent — documented heuristic.  
- Stall bound 1800s and disk/mem thresholds are FindingIds **proposals** until sibling calibrators pin them; ids stay stable if numbers move.  
- `docker ps` empty may mean no containers or client context — not investigated further (avoid scope creep / no mutate).  
- Credential material never opened.

---

## 7. Behavior / gates / surfaces / OOS

| section | content |
|---|---|
| **Behavior** | Read-only live census across mori province surfaces; wrote only this member report path |
| **Gates** | Did not run `tools/mori-census.sh` (absent). No `MORI_CENSUS` banner claimed |
| **Touched surfaces** | ps/proc, journalctl user+system, cgroupfs, df/statvfs, tmux, `.ufo/watchdog.log`, `.ufo/state`, `.ufo/waves/*`, mori git HEAD, wave members dir listing |
| **Out of scope** | remediation; dispatch; pacman/systemd ownership claims; endpoint health; landing corpus/gate into lane repo; subagent dispatch |
| **Artifact path** | `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/LiveReceipt.md` |

---

## 8. Hand-off

Parent may: integrate findings into SCORECARD/LOG, land `tools/mori-census.sh` + corpus notes from sibling members, and diff this receipt against a later LiveReceipt via §4 keys (`added` / `cleared` / `persisted` / `changed-payload`).

**End of live receipt.** Measured window `2026-10-15T00:31:36Z` → `2026-10-15T00:33:23Z`. No remediation.
