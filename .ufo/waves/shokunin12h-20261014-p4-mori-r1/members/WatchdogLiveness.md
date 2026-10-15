# WatchdogLiveness

Advisory census data. Not a judge verdict. Not a `MORI_CENSUS` gate result. No remediation was performed or recommended as an action this lane takes.

Snapshot window: `2026-10-14T21:34:37-03:00` unless a row names an earlier command time. User: `vgpnk`. Host clock offset: `-03:00`.

Driver under test: `scripts/shokunin-watchdog.sh` (header: shokunin-watchdog v4; `SK=/home/vgpnk/Projects/shokunin`; `INTERVAL=450`; `LANES` on line 14). Read, not executed.

## Stable ids

A later run can compare these ids. Class is not severity and not a health grade. `unavailable` means the surface could not be read, or the file is absent. It does not mean unhealthy.

| id | class | surface |
|---|---|---|
| `WATCHDOG_ABSENT` | observation | no running driver pid |
| `WATCHDOG_START_UNAVAILABLE` | unavailable | driver start time |
| `WATCHDOG_LOG_AGE` | observation | last log-line timestamp vs snapshot |
| `WATCHDOG_LOG_MTIME_DIVERGENCE` | observation | file mtime is not the last line |
| `WATCHDOG_COUNTER_<lane>` | observation | `.ufo/state/<lane>.round` + `.mission` |
| `WATCHDOG_COUNTER_UNAVAILABLE_<lane>` | unavailable | roster id with no `.round` file |
| `WATCHDOG_DRIVER_STDOUT_UNAVAILABLE` | unavailable | `.ufo/watchdog-driver.log` |
| `WATCHDOG_FLEET_WRAP_UNAVAILABLE` | unavailable | `.ufo/fleet-wrap` |
| `WATCHDOG_LSOF_UNAVAILABLE` | unavailable | `lsof` binary |

## Commands

```text
# snapshot 2026-10-14T21:34:37-03:00
date -Is
id -un
awk '/^btime /{print $2}' /proc/stat
pgrep -af 'shokunin-watchdog|ufo-night-watchdog|ufo-stale-watchdog'   # stdout empty; exit masked, see recheck
fuser -v /home/vgpnk/Projects/shokunin/.ufo/watchdog.log; echo FUSER_EXIT:$?
stat -c 'size=%s mtime=%y atime=%x ctime=%z mode=%a inode=%i' /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
wc -lc /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
sha256sum /home/vgpnk/Projects/shokunin/.ufo/watchdog.log
stat /home/vgpnk/Projects/shokunin/.ufo/watchdog-driver.log
stat /home/vgpnk/Projects/shokunin/.ufo/fleet-wrap
ls -1 /home/vgpnk/Projects/shokunin/.ufo/state
tmux ls
tmux list-panes -a -F '#{session_name}|#{window_index}.#{pane_index}|pid=#{pane_pid}|cmd=#{pane_current_command}|title=#{pane_title}|dead=#{pane_dead}'
git -C /home/vgpnk/Projects/shokunin rev-parse HEAD:.ufo/watchdog.log 17c1fadfddc5ecbfa5ef362ef44d111792fa3e94:.ufo/watchdog.log
git -C /home/vgpnk/Projects/shokunin log -1 --format='%H %cI %s' -- .ufo/watchdog.log

# /proc cmdline scan, same second (592 pids)
# needles: watchdog, shokunin-watchdog, fleet-override, watchdog.log

# recheck 2026-10-14T21:35:15-03:00
pgrep -af 'shokunin-watchdog'; echo PGREP_EXIT:$?
date -d @1791899878 -Is
ls -1a /home/vgpnk/Projects/shokunin/.ufo/state
stat /home/vgpnk/Projects/shokunin/.ufo/state/<lane>.round   # absent roster ids, below

# counter bytes 2026-10-14T21:30:27-03:00
# for f in .ufo/state/*.round .ufo/state/*.mission; do basename; cat -A; done

# counter mtimes 2026-10-14T21:29:25-03:00
# stat -c '%n size=%s mtime=%y' .ufo/state/*
```

Refused, not run:

- `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting status --lite` — the driver uses this for `live=1` (`scripts/shokunin-watchdog.sh` lines 90–93). Sighting CLI side effects are not established, and dispatch is out of this lane. Blocker only for "are the stored mission ids still live in UFO". Not required to answer pid / log age / counter bytes.
- `systemctl` — OS unit state is not this lane's claim. Not required for the pid question.
- `journalctl` — not this member's surface. Exit reason of a missing pid is therefore unknown, not classified.

## Driver process

`WATCHDOG_ABSENT`

- `2026-10-14T21:34:37-03:00` `/proc` cmdline scan: `scanned_pids=592 unreadable_cmdline=0 hits=1`. The only hit was `PID 1203316` cmdline `Hyprland --watchdog-fd 4`. That is the compositor flag, not `scripts/shokunin-watchdog.sh`. Excluded.
- Same scan needles included `shokunin-watchdog`, `fleet-override`, and `watchdog.log`. No hit.
- `2026-10-14T21:35:15-03:00` `pgrep -af 'shokunin-watchdog'` printed no stdout. `PGREP_EXIT:1`.
- `2026-10-14T21:34:37-03:00` `fuser -v` on `.ufo/watchdog.log` printed no holders. `FUSER_EXIT:1`.
- Earlier corroboration, `2026-10-14T21:30:27-03:00`: same `/proc` scan, `scanned_pids=599 unreadable_cmdline=0`, same single Hyprland hit. `lsof` was not available (`command not found`) — `WATCHDOG_LSOF_UNAVAILABLE`. `fuser` is the open-fd probe that ran.

No pid means there is no `/proc/<pid>` start time.

`WATCHDOG_START_UNAVAILABLE` — reason: no driver pid. The script does not write a pid file (read through line 116; writes are `.ufo/state/<lane>.round`, `.ufo/state/<lane>.mission`, and appends to `.ufo/watchdog.log`). Do not treat a `tick=1` line as a process start time.

tmux is a different surface. `2026-10-14T21:34:37-03:00` `tmux ls` showed one session: `ufo_sighting: 1 windows (created Wed Oct 14 20:14:40 2026) (attached)`. Panes: `pid=938122 cmd=node title=UFO fleet overview dead=0` and `pid=938031 cmd=node title=UFO Sighting · idle dead=0`. Neither command is the watchdog script. This census does not grade that session.

Script identity, measured `2026-10-14T21:30:27-03:00`:

- path `scripts/shokunin-watchdog.sh` size `5540` mode `755` mtime `2026-10-13 16:44:48.534747785 -0300`
- sha256 `b8b01a78b9f66e343a6d5eefd027622b3c3718f79db2c7c06bb69c047fbe2226`
- `git hash-object` equals `HEAD:scripts/shokunin-watchdog.sh` blob `6ade1aaebb0c09e7f9c7ab900b00c51821d77aed`
- `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` (line 14)
- tick sleep `INTERVAL=450` (lines 10 and 115)

## Log freshness

Surface present: `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log`.

`2026-10-14T21:34:37-03:00`:

- size `19396` lines `294` mode `644` inode `9822068`
- mtime `2026-10-13 16:44:48.524089950 -0300`
- ctime `2026-10-13 16:44:48.524089950 -0300` (equal to mtime)
- atime `2026-10-14 16:50:37.433603511 -0300`
- sha256 `c16382b5a59c956d57d96fddaeb288f429998b7693b029d058877d4ca0dc1798`
- git blob `5423397e46baee780490c1cda5754f822a6428a3`
- `git rev-parse HEAD:.ufo/watchdog.log` and `git rev-parse 17c1fadfddc5ecbfa5ef362ef44d111792fa3e94:.ufo/watchdog.log` both returned that blob
- `git log -1 -- .ufo/watchdog.log` → `17c1fadfddc5ecbfa5ef362ef44d111792fa3e94` `2026-09-29T00:19:02-03:00`
- `git hash-object` at `2026-10-14T21:30:27-03:00` matched `HEAD` for the log and for all 18 `.round` / `.mission` files. `git diff --numstat` on those paths was empty.

Last line, confirmed by `tail -c` / `od` at `2026-10-14T21:30:27-03:00` (file ends with newline; line count 294 matches the read):

```text
2026-09-28T23:55:00-03:00 tick=3
```

First line:

```text
2026-09-28T15:44:59-03:00 watchdog tick (live-missions-in-last-status≈64)
```

`grep` for `2026-09-29|2026-10-` in the log: no matches.

`WATCHDOG_LOG_AGE`

- last-line timestamp `2026-09-28T23:55:00-03:00`
- snapshot `2026-10-14T21:34:37-03:00`
- age `1373977` seconds (`15d 21h 39m 37s`), from `python3` datetime subtraction at `2026-10-14T21:35:15-03:00` against that fixed snapshot
- script interval on disk: `450` seconds
- arithmetic only, not a gate verdict: `1373977 / 450 = 3053.28` intervals
- `tick=3` is not a lifetime tick count. The same file contains `tick=39` (line 248) and later `tick=1` (lines 250, 269, 275). Freshness uses the timestamp prefix, not the tick integer.

Boot: `btime 1791899878` at `2026-10-14T21:34:37-03:00`, converted `date -d @1791899878 -Is` → `2026-10-13T10:57:58-03:00`. The last log line is before this boot. No log line is dated during this boot.

`WATCHDOG_LOG_MTIME_DIVERGENCE`

- mtime is `1270188` seconds after the last line (same python expression)
- mtime age at the snapshot: `103788` integer seconds
- all 18 state files shared that same mtime to the nanosecond at `2026-10-14T21:29:25-03:00` (`2026-10-13 16:44:48.524089950 -0300`). Driver launch lines in the log are seconds apart, so this shared mtime is not a series of launch writes.
- worktree bytes equal the `17c1fad` blob, whose in-file timestamps stop at `2026-09-28T23:55:00-03:00`

Do not use mtime as "last tick".

`WATCHDOG_DRIVER_STDOUT_UNAVAILABLE` — `stat .ufo/watchdog-driver.log` at `2026-10-14T21:34:37-03:00`: `No such file or directory (os error 2)`, exit 1. The v4 script appends to `.ufo/watchdog.log` only. This path is a missing extra surface, not a failed read of the driver log, and not unhealthy.

`WATCHDOG_FLEET_WRAP_UNAVAILABLE` — `stat .ufo/fleet-wrap` at the same time: ENOENT, exit 1. The script tests this path (line 104). Current absence is the probe result. Log lines at `2026-09-28T23:54:59-03:00` / `23:55:00` say `wrap … NOT respawning (fleet-wrap)`. Those lines are evidence about that instant, not evidence the file exists now.

## Lane counters

Writer contract, from the script (lines 79–80): on a successful launch the driver writes the round integer to `.ufo/state/<lane>.round` and the run id to `.ufo/state/<lane>.mission`. Wrap/complete lines do not update those files. A counter is the last recorded launch, not proof a round is running.

Inventory `ls -1a .ufo/state` at `2026-10-14T21:35:15-03:00`: `.gitkeep` plus 9 `.round` and 9 `.mission`. No other names. `.gitkeep` is not a counter.

Bytes via `cat -A` at `2026-10-14T21:30:27-03:00`. Each value ended with a single newline and no spaces. Each run id appears once in `.ufo/watchdog.log` as the launch line cited. The last wrap line for that lane (lines 285–293) names the same round integer. No log line is newer than `2026-09-28T23:55:00-03:00`.

| id | round | mission run id | launch line | last wrap line |
|---|---:|---|---|---|
| `WATCHDOG_COUNTER_protocol` | 14 | `shokunin-r14-protocol-r1790648098` | 264 `2026-09-28T23:15:00-03:00` | 285 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_aggregator` | 10 | `shokunin-r10-aggregator-r1790645840` | 247 `2026-09-28T22:37:21-03:00` | 286 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kasegi` | 17 | `shokunin-r17-kasegi-r1790648100` | 266 `2026-09-28T23:15:03-03:00` | 287 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kengaku` | 13 | `shokunin-r13-kengaku-r1790648103` | 268 `2026-09-28T23:15:05-03:00` | 288 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kake` | 16 | `shokunin-r16-kake-r1790647152` | 255 `2026-09-28T22:59:14-03:00` | 289 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kumitate` | 16 | `shokunin-r16-kumitate-r1790646699` | 252 `2026-09-28T22:51:41-03:00` | 290 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kotoba` | 16 | `shokunin-r16-kotoba-r1790648057` | 261 `2026-09-28T23:14:20-03:00` | 291 `2026-09-28T23:54:59-03:00` |
| `WATCHDOG_COUNTER_kagi` | 16 | `shokunin-r16-kagi-r1790647154` | 257 `2026-09-28T22:59:16-03:00` | 292 `2026-09-28T23:55:00-03:00` |
| `WATCHDOG_COUNTER_kama` | 1 | `shokunin-r1-kama-r1790646247` | 249 `2026-09-28T22:44:08-03:00` | 293 `2026-09-28T23:55:00-03:00` |

Run ids are the driver's launch identifiers (`shokunin-r<N>-<lane>-r<unix>`). They are not session tokens. The script also passes `--session-id` to the sighting CLI and does not store that string in `.ufo/state`. Those session ids were not read and are not reconstructed here.

`protocol` and `aggregator` have counters and are in `LANES`. They are not ids in the `MANIFEST.json` `roster` array (lines 5–110, read `2026-10-14`). That is an observation about the two lists, not a grade.

Roster ids with no counter file, `stat` at `2026-10-14T21:35:15-03:00`, each `No such file or directory (os error 2)`:

| id | path |
|---|---|
| `WATCHDOG_COUNTER_UNAVAILABLE_audio` | `.ufo/state/audio.round` |
| `WATCHDOG_COUNTER_UNAVAILABLE_game-dev-2d` | `.ufo/state/game-dev-2d.round` |
| `WATCHDOG_COUNTER_UNAVAILABLE_game-dev-3d` | `.ufo/state/game-dev-3d.round` |
| `WATCHDOG_COUNTER_UNAVAILABLE_lore` | `.ufo/state/lore.round` |
| `WATCHDOG_COUNTER_UNAVAILABLE_revenger` | `.ufo/state/revenger.round` |
| `WATCHDOG_COUNTER_UNAVAILABLE_kaidoku` | `.ufo/state/kaidoku.round` |

Those six ids are in `MANIFEST.json` `roster` and are not in the driver's `LANES` string. Absence is `unavailable`, not unhealthy, and not a silence grade.

Also ENOENT, same command, not roster rows and not in `LANES`: `.ufo/state/mori.round`, `.ufo/state/chousa.round`. Same class: unavailable counter surface. Not a lane-failure claim.

## Inference

Labeled inference, not extra observations:

- The v4 driver is not running at the snapshot. The process table was readable (`unreadable_cmdline=0`), so this is absence, not a failed probe.
- Log mtime and the shared state-file mtime are not append/launch times. Content identity is the `17c1fad` blob / sha256 above.
- Counter integers are last recorded launches as of the log's last line. They do not mean those rounds are in progress.
- `WATCHDOG_ABSENT` is a driver-process finding. It is not a per-lane failure, and it is not a claim about the `ufo_sighting` tmux session.
- `Hyprland --watchdog-fd` must stay excluded or a substring search false-matches a running driver.

## Unknown

- Why the driver process is absent. The script has no exit log line. This member did not read the journal. Do not infer crash, stop, or fleet-wrap halt of a still-running process. The log's last action is `tick=3` after per-lane `wrap` lines, and the process is not there now. Those are two observations, not a cause.
- Whether the nine stored mission ids are still live in UFO. The status CLI was refused.
- Start time of whatever process last appended the log. Not recorded on this surface.
- Whether a driver exists in a pid namespace not visible under this `/proc`. Inside the scanned namespace the cmdline read was complete.
- The checkout event that set mtime to `2026-10-13 16:44:48.524089950 -0300`. `git diff --stat e867f786^ e867f786 -- .ufo/state .ufo/watchdog.log` (`2026-10-14T21:35:15-03:00`) shows those paths added relative to that commit's first parent (log `294` insertions, each state file `1` insertion). This report does not establish that that diff is the working-tree write.

## Not claimed

- No healthy / unhealthy / wedged / daemon-death grade.
- No `MORI_CENSUS: CLEAN|DRIFT`.
- No restart, kill, reparent, systemd, or dispatch action.
- No OS-package or unit state.
- No endpoint or model health.
- No claim that an unsettled wave failed. Wave settlement is not this surface.
