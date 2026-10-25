# CgroupMemoryEvents — user-slice and fleet cgroup memory census

**Member:** CgroupMemoryEvents · **Item:** mori/CgroupMemoryEvents · **Wave:** shokunin12h-20261014-p4-mori-r1
**Lane:** mori-shokunin (detect and report only) · **Axes:** coverage · operability · calibration
**Role of this file:** advisory data. Not a `MORI_CENSUS` verdict. No remediation was performed (no kill, restart, cgroup write, `systemctl start/stop`, pacman, or dispatch).

**Primary measure:** `2026-10-15T00:33:03Z` (UTC), python reads of cgroupfs. Later probes are stamped separately. Host journal lines are in `-03:00`.
**Boot:** `/proc/sys/kernel/random/boot_id` = `d7f0bc8d-938e-4249-b4a1-f250cbfacf58` at `2026-10-15T00:36:15Z`. `/proc/stat` `btime` = `1791899878`. `/proc/uptime` first field = `124696.21` seconds. Same boot as the journal lines below (`journalctl -b` / `--user -b`).

## 0. How to read a row

`memory.events` field `max` is an event counter. `memory.max` is a different file (limit). They are never the same number here.

`memory.events` is the hierarchical file (this cgroup and descendants). `memory.events.local` was read only to stop a parent counter being treated as a kill inside that cgroup. The assigned surface is `memory.events`.

A missing or unreadable file is `unavailable` plus errno. That is not an unhealthy reading.

`memory.current` is a point sample (volatile). Event counters are cumulative for the life of that cgroup instance.

Stable ids below are the FindingIds vocabulary (`CGROUP_OOM_KILL`, `CGROUP_MEM_HIGH`, `CGROUP_MEM_CURRENT_UNAVAILABLE`, `SURFACE_UNAVAILABLE`) applied to these observations. Severity is that vocabulary's, not a gate weight claimed by this member. FixtureDesign's strings `CGROUP_MEMORY_HIGH` and `CGROUP_UNAVAILABLE` are a different spelling; this file does not emit them.

## 1. Probe log

| when (UTC) | command | result used for |
|---|---|---|
| 2026-10-15T00:28:14Z | `cat /proc/self/cgroup`; `id -u`; `findmnt -t cgroup2` | caller is uid 1000; cgroup2 at `/sys/fs/cgroup` (`rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot,memory_hugetlb_accounting`) |
| 2026-10-15T00:28:44Z | `systemctl --user list-units --type=service --all --plain`; `--type=scope` | no user unit whose name is shokunin, ufo, webbridge, kimi, or watchdog |
| 2026-10-15T00:29:18Z | `systemctl list-units --type=service --all` name filter; `systemctl --user list-unit-files` name filter; `tmux ls`; `find /sys/fs/cgroup -maxdepth 6 -type d` name filter | `tmux ls` → `ufo_sighting: 1 windows (created Wed Oct 14 20:14:40 2026) (attached)`. Only fleet-named cgroup dirs were the two `tmux-spawn-*.scope` paths below. System-unit grep false-hit `omp` inside `complete`; those units are not fleet subjects |
| 2026-10-15T00:30:14Z | `pgrep -a -f shokunin-watchdog`; `pgrep -a -f 'webbridge\|web-bridge\|kimi-web'`; `pgrep -a -f 'ufo-fsd\|ufo-sighting\|ufo_sighting'` | watchdog pgrep exit 1 (no match). webbridge pgrep exit 1. ufo pgrep listed pids 937995, 938031, 938085, 938105, 938122 |
| 2026-10-15T00:30:56Z | `systemctl --user show` and `systemctl show` of `shokunin-watchdog.service`, `webbridge.service`, `kimi-webbridge.service` (`-p LoadState -p ActiveState -p FragmentPath`) | each: `LoadState=not-found`, `ActiveState=inactive`, `FragmentPath=` empty. Show does not start a unit |
| 2026-10-15T00:32:12Z | `command -v docker`; `docker ps -a --no-trunc`; `ls` of `/sys/fs/cgroup/system.slice/docker.service` | docker at `/usr/bin/docker`, `docker ps` exit 0, header only (zero containers). `docker.service` cgroup has no child cgroup dirs |
| 2026-10-15T00:33:03.633174Z–00:33:03.637740Z | python `os.walk("/sys/fs/cgroup")` reading `memory.events` and `memory.events.local`, plus `memory.current`/`memory.max` on the required set; `os.stat` of hypothesized unit paths | primary numbers in §2–§5. Walk: 101 cgroups had a `memory.events` file, 0 unreadable, 2 with `oom`/`oom_kill`/`high`/`max`/`oom_group_kill` > 0 |
| 2026-10-15T00:34:28Z | `journalctl --user -b -g 'oom-kill\|Out of memory\|Killed process\|oom_kill' --output=short-iso`; `journalctl -k -b -g 'oom-kill\|Out of memory\|Killed process' --output=short-iso`; `ls` of slice children; `cat` of `system.slice/memory.events` | attribution lines in §6. User filter: 1 line. Kernel filter: 3 lines. Caps (`head`) were not what truncated them; a recount at 00:35:55Z was 1 and 3 |
| 2026-10-15T00:34:28.544589Z | read `cgroup.procs` + `/proc/<pid>/cmdline` for the fleet scopes and `session-4.scope` | membership in §3. Later than the byte sample |
| 2026-10-15T00:35:55Z | `stat` of slice dirs; `journalctl --user -b -g dd9e67bd`; `journalctl -b -g 1732581`; `journalctl --user -b -g 'webbridge\|kimi-webbridge'` | dead scope ENOENT; scope start line; webbridge user-journal count 0, exit 1. `stat -c %w` birth = `-` (unavailable; stat itself succeeded) |
| 2026-10-15T00:36:15Z | `systemctl show user.slice`, `user-1000.slice`, `user@1000.service` `-p ActiveEnterTimestamp -p InvocationID -p LoadState -p ActiveState` | instance dates in §6. Read-only show |

Re-run the assigned files without python:

```text
cat /sys/fs/cgroup/user.slice/memory.events
cat /sys/fs/cgroup/user.slice/memory.events.local
cat /sys/fs/cgroup/user.slice/memory.current
cat /sys/fs/cgroup/user.slice/memory.max
```

Same four names under each path in §2 and §3. Event counters are comparable across runs on this boot; `memory.current` is not.

## 2. User slice — assigned surface

Only child of `/sys/fs/cgroup/user.slice` is `user-1000.slice` (listing at 00:34:28Z). uid in this session is 1000 (`id -u`).

Root `/sys/fs/cgroup/{memory.events,memory.events.local,memory.current,memory.max}` at `2026-10-15T00:33:03.633198Z`: **unavailable**, errno **2** `ENOENT` `No such file or directory`. Not unhealthy. Children of the root do expose `memory.*`. This root is not the user slice.

### 2.1 `/sys/fs/cgroup/user.slice`

Readable. Measured `2026-10-15T00:33:03.633230Z` (`memory.events`) through `.633275Z` (`memory.max`).

`memory.events` (hierarchical):

```text
low 0
high 0
max 0
oom 0
oom_kill 1
oom_group_kill 0
sock_throttled 77943
```

`memory.events.local`:

```text
low 0
high 0
max 0
oom 0
oom_kill 0
oom_group_kill 0
sock_throttled 0
```

| assigned field | file | value |
|---|---|---|
| oom | memory.events | 0 |
| oom_kill | memory.events | 1 |
| high | memory.events | 0 |
| max | memory.events | 0 |
| (bytes) | memory.current | 24998629376 |
| (limit token) | memory.max | `max` |

`memory.events.local` `oom_kill` = 0. The hierarchical 1 is not an event charged to `user.slice` itself.

Derived (not a second probe): 24998629376 bytes = 23.281694412 GiB. `memory.max` token `max` is not a number, so `current/max` is **unavailable**, not low and not high.

### 2.2 `/sys/fs/cgroup/user.slice/user-1000.slice`

Readable. `memory.events` at `2026-10-15T00:33:03.633288Z`.

`memory.events`:

```text
low 0
high 0
max 0
oom 0
oom_kill 1
oom_group_kill 0
sock_throttled 77943
```

`memory.events.local`: all of `low high max oom oom_kill oom_group_kill sock_throttled` = 0.

| assigned field | file | value |
|---|---|---|
| oom | memory.events | 0 |
| oom_kill | memory.events | 1 |
| high | memory.events | 0 |
| max | memory.events | 0 |
| (bytes) | memory.current | 24991174656 |
| (limit token) | memory.max | `max` |

Local `oom_kill` is 0. Same hierarchical pattern as the parent slice.

### 2.3 `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service`

Readable. `memory.events` at `2026-10-15T00:33:03.633350Z`. This is the live user manager, not a second user slice. Included because it is the cgroup that holds this uid's services.

`memory.events`:

```text
low 0
high 0
max 0
oom 0
oom_kill 0
oom_group_kill 0
sock_throttled 13705
```

`memory.events.local`: all listed counters 0, including `sock_throttled`.

| assigned field | file | value |
|---|---|---|
| oom | memory.events | 0 |
| oom_kill | memory.events | 0 |
| high | memory.events | 0 |
| max | memory.events | 0 |
| (bytes) | memory.current | 23866155008 |
| (limit token) | memory.max | `max` |

A census that read only `user@1000.service` would have reported `oom_kill` 0 and missed the ancestor counter. That is an observation about these three files, not a gate design.

### 2.4 Other live child of `user-1000.slice` (attribution, not a fleet service)

`/sys/fs/cgroup/user.slice/user-1000.slice/session-4.scope` at `2026-10-15T00:33:03.633319Z`:

| file | oom | oom_kill | high | max (events) | memory.current | memory.max |
|---|---:|---:|---:|---:|---:|---|
| memory.events | 0 | 0 | 0 | 0 | 4288512 | `max` |
| memory.events.local | 0 | 0 | 0 | 0 | — | — |

Procs at `2026-10-15T00:34:28.544589Z`: 3. Comms: `sddm-helper`, `sh` (`uwsm` signal-handler), `systemctl --user start --wait wayland-session-envelope@hyprland.desktop.target`. Session socket path omitted (shape only). This scope is a login/session cgroup, not a fleet service. It is the only live sibling of `user@1000.service`, and it is not the `oom_kill` site.

## 3. Fleet-relevant live cgroups

**Inclusion rule**

- Observation, included: a cgroup whose live `cgroup.procs` cmdline contains `ufo-sighting.mjs` or whose `tmux` command names session `ufo_sighting`, and the scope is not a mixed desktop terminal.
- Inference, included and labeled: an exclusive cgroup whose only proc is `omp __omp_worker_daemon_broker` (harness process, not a systemd unit name).
- Observation, read but not attributed: a scope that contains a fleet pid and unrelated co-tenants. `memory.current` of that scope is not that service's usage.
- Excluded with evidence: desktop units, `docker.service` (zero containers), kernel `watchdogd` (cgroup `0::/`, empty cmdline), `Hyprland --watchdog-fd`, a `kimi` CLI sharing a terminal scope (no `webbridge` in its cmdline).

On-disk scope names contain the literal systemd escape `\x2d` (four characters), not a hyphen. Paths below are the paths that were opened.

### 3.1 Exclusive ufo-sighting scopes

Both measured `2026-10-15T00:33:03.633439Z` and `.633471Z`. Procs re-read `2026-10-15T00:34:28.544589Z`.

| path | procs | memory.events oom / oom_kill / high / max | memory.events.local same four | memory.current | memory.max |
|---|---|---|---|---:|---|
| `.../app-graphical.slice/tmux-spawn-882f0c6c-86dc-4c76-acd8-7f0f7d740cec.scope` | 1: pid 938122 `node .../ufo-fsd-alpha/scripts/ufo-sighting.mjs overview --watch` | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 28364800 | `max` |
| `.../app-graphical.slice/tmux-spawn-cfb2824c-8cad-4995-a489-02d2d465d291.scope` | 1: pid 938031 `node .../ufo-sighting.mjs __idle` | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 18575360 | `max` |

Full prefix: `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/`.

`oom_group_kill` 0 and `sock_throttled` 0 on both files of both scopes. No errno.

### 3.2 Sighting client scope (two procs, both sighting)

`/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-e4be04ca.scope`

`memory.events` at `2026-10-15T00:33:03.633502Z`: `oom 0`, `oom_kill 0`, `high 0`, `max 0`, `oom_group_kill 0`, `sock_throttled 0`. Local file identical on those counters. `memory.current` = 35815424. `memory.max` = `max`.

Procs at 00:34:28Z: pid 938085 `alacritty --class=org.omarchy.ufo-sighting -e .../scripts/ufo-sighting`; pid 938105 `tmux attach-session -d -t ufo_sighting:1`.

### 3.3 Exclusive omp broker scope (inclusion is inference)

`/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-e9c449da.scope`

`memory.events` at `2026-10-15T00:33:03.633533Z`: `oom 0`, `oom_kill 0`, `high 0`, `max 0`, `oom_group_kill 0`, `sock_throttled 14`. Local file matches, including `sock_throttled 14`. `memory.current` = 589062144. `memory.max` = `max`.

Procs at 00:34:28Z: 1 pid, 3071566, `/home/vgpnk/.local/bin/omp __omp_worker_daemon_broker`.

### 3.4 Shared scope — fleet pids present, usage not attributed

`/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-6bd28f41.scope`

`memory.events` at `2026-10-15T00:33:03.633563Z`: `oom 0`, `oom_kill 0`, `high 0`, `max 0`, `oom_group_kill 0`, `sock_throttled 194`. Local matches those counters (`sock_throttled 194`). `memory.current` = 11582369792. `memory.max` = `max`.

Procs at 00:34:28Z: **25**. Observed fleet-relevant members in that list: pid 937995 `tmux new-session -d -s ufo_sighting -n fleet ... ufo-sighting.mjs __idle`; pid 935236 `omp`; pid 950506 `omp __omp_worker_daemon_broker`. Co-tenants include alacritty, bash, `npm`/`node` rea mcp, and omp python runners. The 25-count also included a concurrent census `python3 -c` from this member; it is not a service. **Do not read 11582369792 as any one of those processes.**

Caller cgroup at 00:28:14Z was this same scope (`/proc/self/cgroup`).

### 3.5 Intermediate slices checked while attributing (not services)

All at `2026-10-15T00:33:03Z`. `memory.max` = `max`. Events `oom`/`oom_kill`/`high`/`max` = 0 on both `memory.events` and `memory.events.local`.

| path | memory.current | memory.events sock_throttled (hierarchical) |
|---|---:|---:|
| `.../user@1000.service/app.slice` | 23741579264 | 13705 |
| `.../user@1000.service/app.slice/app-graphical.slice` | 23452143616 | 13703 |
| `.../user@1000.service/init.scope` | 5615616 | 0 |

## 4. Walk — where the non-zero event counters actually are

Command: python `os.walk("/sys/fs/cgroup")`, read `memory.events` and `memory.events.local` wherever the filename existed. Window `2026-10-15T00:33:03.633625Z`–`00:33:03.637565Z`.

| fact | value |
|---|---|
| cgroups with `memory.events` | 101 |
| both event files unreadable | 0 |
| cgroups with `oom` or `oom_kill` or `high` or `max` or `oom_group_kill` > 0 | 2 |

Those two are only:

- `/sys/fs/cgroup/user.slice` — hierarchical `oom_kill 1`, local `oom_kill 0`
- `/sys/fs/cgroup/user.slice/user-1000.slice` — hierarchical `oom_kill 1`, local `oom_kill 0`

No live cgroup had local `oom_kill` > 0. No live cgroup under `user@1000.service` had hierarchical `oom_kill` > 0.

Negative control, separate `cat` at `2026-10-15T00:34:28Z`: `/sys/fs/cgroup/system.slice/memory.events` and `memory.events.local` are `low 0`, `high 0`, `max 0`, `oom 0`, `oom_kill 0`, `oom_group_kill 0`, `sock_throttled 0`. `system.slice` is not classified as a fleet service; it was read to locate the non-zero.

`sock_throttled` is outside the assigned field set. It is in the raw files above. No finding id is invented for it.

## 5. Named services with no resolved cgroup

Discovery (not a guessed path): no live pid, `LoadState=not-found`, empty `FragmentPath`. The cgroup path is therefore **unresolved**. That is `unavailable`. It is not an unhealthy unit, and it is not `WATCHDOG_ABSENT` (that predicate is the watchdog surface; this file only resolves cgroup paths).

Hypothesized paths were `stat`'d so the errno is on disk, not implied. All 15 returned errno **2** `ENOENT` at `2026-10-15T00:33:03.637665Z`–`.637735Z`. They are probes of a hypothesis, not discovered unit paths.

| hypothesized path | errno |
|---|---|
| `/sys/fs/cgroup/system.slice/shokunin-watchdog.service` | 2 ENOENT |
| `/sys/fs/cgroup/system.slice/webbridge.service` | 2 ENOENT |
| `/sys/fs/cgroup/system.slice/kimi-webbridge.service` | 2 ENOENT |
| `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/shokunin-watchdog.service` | 2 ENOENT |
| `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/webbridge.service` | 2 ENOENT |
| `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/kimi-webbridge.service` | 2 ENOENT |
| `.../user@1000.service/app.slice/{shokunin-watchdog,webbridge,kimi-webbridge}.service` | 2 ENOENT |
| `.../user@1000.service/session.slice/{shokunin-watchdog,webbridge,kimi-webbridge}.service` | 2 ENOENT |
| `.../user@1000.service/background.slice/{shokunin-watchdog,webbridge,kimi-webbridge}.service` | 2 ENOENT |

`journalctl --user -b -g 'webbridge|kimi-webbridge'` at `2026-10-15T00:35:55Z`: 0 lines, exit 1. That is "no matching user-journal line this boot", not a failed journalctl. Kernel/system journal was not scanned for the string `webbridge` beyond the oom class filter in §6.

Operator demand text that a webbridge daemon OOM'd is a prior account (`.ufo/scopes/shokunin-12h-20261014/operator-demand.md`). It was not re-run. This census does not identify that account with the python3 kill in §6.

## 6. What the hierarchical `oom_kill 1` is attached to

### 6.1 Observations

User journal (`journalctl --user -b`, filter in §1), one class hit:

```text
2026-10-13T23:44:31-03:00 plazir27 systemd[1573]: app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: Failed with result 'oom-kill'.
```

Same scope, same command, three further lines (not a second kill):

```text
2026-10-13T11:14:28-03:00 ... systemd-run --user --scope --slice=app-graphical.slice '--unit=app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope' ... xdg-terminal-exec --dir=/home/vgpnk
2026-10-13T23:44:30-03:00 ... app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: The kernel OOM killer killed some processes in this unit.
2026-10-13T23:44:31-03:00 ... Consumed 19h 12min 17.770s CPU time over 12h 30min 3.509s wall clock time, 27.4G memory peak, 30.7G memory swap peak.
```

Kernel journal (`journalctl -k -b`), same instant:

```text
2026-10-13T23:44:30-03:00 plazir27 kernel: GpuWatchdog invoked oom-killer: gfp_mask=0x140cca(GFP_HIGHUSER_MOVABLE|__GFP_COMP), order=0, oom_score_adj=200
2026-10-13T23:44:30-03:00 plazir27 kernel: oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=user.slice,mems_allowed=0,global_oom,task_memcg=/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope,task=python3,pid=1732581,uid=1000
2026-10-13T23:44:30-03:00 plazir27 kernel: Out of memory: Killed process 1732581 (python3) total-vm:56727648kB, anon-rss:27873696kB, file-rss:16kB, shmem-rss:0kB, UID:1000 pgtables:110928kB oom_score_adj:200
```

`GpuWatchdog` is the kernel line's invoker name. It is not `scripts/shokunin-watchdog.sh` (pgrep exit 1).

Dead scope path, `stat` at `2026-10-15T00:35:55.791492Z`:

`/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope`

**unavailable**, errno **2** `ENOENT`. So `memory.events`, `memory.current`, and `memory.max` on that path are the same errno. No live value.

Instance timestamps (`systemctl show` at `2026-10-15T00:36:15Z`):

| unit | ActiveState | ActiveEnterTimestamp | InvocationID |
|---|---|---|---|
| `user.slice` | active | Tue 2026-10-13 11:02:03 -03 | `55b9dbf353824c42adde6fb84d4d31ac` |
| `user-1000.slice` | active | Tue 2026-10-13 11:02:05 -03 | `cc612e6f66fa4bbcad7fa0b7dd02df19` |
| `user@1000.service` | active | Wed 2026-10-14 13:11:07 -03 | `e288c87781a242ab87ebf3f236a96226` |

Kill time `2026-10-13T23:44:30-03:00` is after both slice enter timestamps and before `user@1000.service` enter. `stat` birth time of the cgroup directories is unavailable (`%w` = `-`). Directory mtime is not used as creation.

Pid 1732581 appears in the kernel lines as comm `python3` only. Full argv was not in those lines. The pid is not in `/proc` (process was killed). No credential material was read.

### 6.2 Inference (not a second measurement)

- One kernel `Killed process` line this boot, hierarchical `oom_kill` 1 on the two slices that have been active since before that line, local `oom_kill` 0 on every live cgroup scanned. The two slice findings are one propagated count, not two kills.
- The current `user@1000.service` instance started at 13:11:07 -03 on 2026-10-14, after the kill, and its `memory.events` `oom_kill` is 0. The counter that still reads 1 lives on the parent slices, not on the live user manager. This is why a service-only read misses it.
- The killed cgroup was a Hyprland `xdg-terminal-exec` scope under the previous user-manager instance. It is not a resolved `webbridge.service` or `kimi-webbridge.service` path.

### 6.3 Unknown

- Argv of pid 1732581. Comm is `python3`. Whether that process was the webbridge daemon named in operator demand is **unknown**. No webbridge string in the user journal this boot.
- Cgroup directory birth time (`stat %w` = `-`).
- Whether any `oom_kill` occurred on a previous boot. These counters and `journalctl -b` are this boot only.
- Host `MemAvailable` ratio. Not measured here. `memory.max` is the token `max`, so a cgroup `current/max` ratio is unavailable, not low.

## 7. Findings (stable ids)

Compare key = id + subject. Payload magnitudes that are volatile (`memory.current`, pid lists, `measured_at`) are not the compare key. `boot_id` is attached so a later boot can tell a reset from a clear.

Predicate source: FindingIds §3.4, profile name `boot-zero` / `baseline=boot-zero` (absolute `oom_kill > 0` on first run). This member does not print `MORI_CENSUS: DRIFT`.

```text
FINDING CGROUP_OOM_KILL severity=high surface=memory.events subject=cgroup=/sys/fs/cgroup/user.slice obs=oom_kill=1 local_oom_kill=0 oom=0 high=0 max=0
FINDING CGROUP_OOM_KILL severity=high surface=memory.events subject=cgroup=/sys/fs/cgroup/user.slice/user-1000.slice obs=oom_kill=1 local_oom_kill=0 oom=0 high=0 max=0
FINDING CGROUP_MEM_CURRENT_UNAVAILABLE severity=info surface=memory.current subject=cgroup=/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope obs=errno=2 ENOENT
FINDING SURFACE_UNAVAILABLE severity=info surface=cgroup-service subject=service=shokunin-watchdog obs=no_resolved_cgroup pgrep_exit=1 LoadState=not-found
FINDING SURFACE_UNAVAILABLE severity=info surface=cgroup-service subject=service=webbridge obs=no_resolved_cgroup pgrep_exit=1 LoadState=not-found
FINDING SURFACE_UNAVAILABLE severity=info surface=cgroup-service subject=service=kimi-webbridge obs=no_resolved_cgroup pgrep_exit=1 LoadState=not-found
```

`CGROUP_OOM_KILL` does **not** fire for `user@1000.service` or for any live fleet scope in §3 (`oom_kill` 0). `CGROUP_MEM_HIGH` does not fire anywhere scanned (`high` 0 and events-file `max` 0). Unavailable rows are info. They are not unhealthy and they are not a second kill.

Clean label (not a finding id) for each §3 scope and for `user@1000.service`: `CGROUP_EVENTS_ZERO` on oom/oom_kill/high/max.

`CGROUP_MEM_CURRENT_UNAVAILABLE` on the dead scope means the live path cannot be read. It does not mean the historical kill is unclear: the kill is the `CGROUP_OOM_KILL` rows plus the journal lines. The scope's absence is the expected post-exit state of a failed scope, recorded as unavailable rather than as a still-running fault.

## 8. Exclusions (so a later run does not think they were missed)

| candidate | why excluded | evidence |
|---|---|---|
| kernel `watchdogd` pid 237 | not the fleet driver | cgroup `0::/`, empty cmdline; name match only |
| `Hyprland --watchdog-fd` | compositor flag, not a service under census | cmdline in `wayland-wm@hyprland.desktop.service` |
| `kimi` pid 1205136 | CLI in a mixed terminal, not a webbridge unit | cmdline `kimi`; co-tenants alacritty/bash; no dedicated service cgroup |
| `docker.service` | no container to call a fleet service | `docker ps -a` exit 0, zero rows; no child cgroup |
| desktop user units (pipewire, portals, waybar, …) | not fleet-relevant under the inclusion rule | `systemctl --user list-units` at 00:28:44Z |
| hypothesized unit paths in §5 | not discovered subjects | ENOENT recorded there; not extra findings |

## 9. Blockers

None. Every assigned read either returned bytes or an errno. No probe was refused for wanting a write, a restart, or an external fetch. `stat` birth time is unavailable as a field, not as a failed probe.

## 10. Receipt

```json
{
  "member": "CgroupMemoryEvents",
  "measured_at": "2026-10-15T00:33:03.633230Z",
  "boot_id": "d7f0bc8d-938e-4249-b4a1-f250cbfacf58",
  "verdict_claimed": false,
  "findings": [
    {
      "id": "CGROUP_OOM_KILL",
      "severity": "high",
      "subject": "cgroup=/sys/fs/cgroup/user.slice",
      "oom_kill": 1,
      "oom_kill_local": 0,
      "oom": 0,
      "high": 0,
      "max_events": 0,
      "memory_max": "max"
    },
    {
      "id": "CGROUP_OOM_KILL",
      "severity": "high",
      "subject": "cgroup=/sys/fs/cgroup/user.slice/user-1000.slice",
      "oom_kill": 1,
      "oom_kill_local": 0,
      "oom": 0,
      "high": 0,
      "max_events": 0,
      "memory_max": "max",
      "same_propagated_count_as": "cgroup=/sys/fs/cgroup/user.slice"
    },
    {
      "id": "CGROUP_MEM_CURRENT_UNAVAILABLE",
      "severity": "info",
      "subject": "cgroup=/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\\x2dterminal\\x2dexec-dd9e67bd.scope",
      "errno": 2,
      "errno_name": "ENOENT"
    },
    {
      "id": "SURFACE_UNAVAILABLE",
      "severity": "info",
      "subject": "service=shokunin-watchdog",
      "errno_on_hypothesized_paths": 2
    },
    {
      "id": "SURFACE_UNAVAILABLE",
      "severity": "info",
      "subject": "service=webbridge",
      "errno_on_hypothesized_paths": 2
    },
    {
      "id": "SURFACE_UNAVAILABLE",
      "severity": "info",
      "subject": "service=kimi-webbridge",
      "errno_on_hypothesized_paths": 2
    }
  ]
}
```
