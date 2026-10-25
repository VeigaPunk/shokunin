# OomClassTaxonomy

Advisory data for mori probation round 1. Not a verdict. No CLEAN/DRIFT claim. mori detects and reports; this note remediates nothing.

Axes this table is built for: coverage (every assigned class, plus observed signatures that must not be forced into one), operability (re-runnable match, stable id, journal surface), calibration (observation / inference / unknown kept apart; a missing signature is unobserved, not healthy and not unhealthy).

## Measurement

| field | value |
|---|---|
| measured | 2026-10-14T21:30:05-03:00 .. 2026-10-14T21:37:45-03:00 |
| host | plazir27 |
| boot 0 | `d7f0bc8d938e4249b4a1f250cbfacf58` |
| boot 0 window | first entry 2026-10-13T11:02:03-03:00; last entry seen 2026-10-14T21:30:03-03:00 |
| retained boots | `-12` .. `0` (`journalctl --list-boots --no-pager`) |
| journal size | 197.3M (`journalctl --disk-usage`) |
| journalctl | systemd 261 (261.2-1-arch); `-g` is case-insensitive when the pattern is all lowercase; `--case-sensitive=true` exists |

Commands are the ones named under each row. Counts for boot 0 are point-in-time and will rise while the boot continues. A later run compares signature form and id, not the count. A higher segfault count on the same boot is not taxonomy drift.

User name in a PAM line below is session-adjacency evidence, not a credential. No token, oauth, or session payload was opened. kimi lines (2198, case-sensitive `kimi`) were counted and scanned for kill-words only; their text is not quoted.

## Visibility (the contract probe is not enough)

Contract probe `journalctl --user -b` sees user-manager `Failed with result` lines and coredump records. It does not see kernel victim lines. MESSAGE grep `terminated abnormally with signal` is 0 on `--user` (rechecked 2026-10-14T21:44:43-03:00). The shorter phrase `terminated abnormally` is not 0: 7 entries, all `terminated abnormally without generating a coredump`, `COREDUMP_SIGNAL=5`, comm `MainThread`. Those 7 are not signal 11.

Remeasured 2026-10-14T21:43:03-03:00 after KillEventsJournal's recount at 21:42:01. Counts below are journal entries, not cat-lines. Boot id is the same 32 hex with or without hyphens: `d7f0bc8d938e4249b4a1f250cbfacf58` / `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`.

| signature family | `--user -b` boot 0 | system `-b` boot 0 |
|---|---|---|
| `Out of memory: Killed process` (MESSAGE) | 0 | 1 |
| `segfault at` (MESSAGE) | 0 | 588 |
| helper MESSAGE `terminated abnormally with signal 11/SEGV` (`CODE_FUNC=coredump_kernel_helper`, no `MESSAGE_ID`) | 0 | 657 |
| `MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1` entries | 1051 (11/SIGSEGV 656, 6/SIGABRT 365, 5/SIGTRAP 25, 7/SIGBUS 5) | not separately entry-counted in this pass |
| `COREDUMP_SIGNAL=11` entries | 656 | 657 |
| `SIGTERM` or `signal 15` | 0 | 0 |
| `Failed with result` | 2 (`oom-kill`, `core-dump`) | 3 (those two plus `signal` from pid 1) |

The one-entry gap (system 657 vs user 656 on `COREDUMP_SIGNAL=11`) is observed. Which pid is system-only is unknown. ABRT/TRAP/BUS field counts on `--user` match the system helper histogram exactly.

A `--user -b` MESSAGE grep for `segfault at` or `terminated abnormally with signal` misses the crash mass and misses the kernel victim line. The shorter grep `terminated abnormally` returns 7, all SIGTRAP with no coredump, and still misses the 656 SIGSEGV. The probe with `COREDUMP_SIGNAL=11` sees the crash mass. The only oom signature on `--user` is still `Failed with result 'oom-kill'.`

Do not print coredump payload fields. The record carries `COREDUMP_ENVIRON`, `COREDUMP_CMDLINE`, `COREDUMP_PROC_STATUS`, `COREDUMP_PROC_MAPS`, `COREDUMP_OPEN_FDS`. Key names observed; values not read. Census `--output-fields` is `COREDUMP_SIGNAL,COREDUMP_SIGNAL_NAME,COREDUMP_COMM,COREDUMP_PID,COREDUMP_UNIT,COREDUMP_USER_UNIT,COREDUMP_CGROUP,MESSAGE_ID`.

## Taxonomy

Primary class is what a counter increments. A line can also be a unit-failure annotation of the same death. Do not add those.

| id | class (count as) | verbatim signature | exemplar (journal time, boot, surface) | fleet meaning |
|---|---|---|---|---|
| `MORI-OOM-KERNEL-KILL` | `oom_kill` | `Out of memory: Killed process 1732581 (python3) total-vm:56727648kB, anon-rss:27873696kB, file-rss:16kB, shmem-rss:0kB, UID:1000 pgtables:110928kB oom_score_adj:200` | 2026-10-13T23:44:30.638238-03:00, boot 0, system, `kernel`, priority 3, no `MESSAGE_ID` | The one host-global kill in the retained journal. Named victim is `python3` pid 1732581, anon-rss 27873696kB, `oom_score_adj=200`, UID 1000. This is the event to count. |
| `MORI-OOM-CONSTRAINT` | `oom_kill` (same event, do not add) | `oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=user.slice,mems_allowed=0,global_oom,task_memcg=/user.slice/user-1000.slice/user@1000.service/app.slice/app-graphical.slice/app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope,task=python3,pid=1732581,uid=1000` | 2026-10-13T23:44:30.638184-03:00, boot 0, system, kernel | `global_oom` + `CONSTRAINT_NONE`: host memory, not a cgroup `memory.max` kill. `task_memcg` is the scope join key. `CONSTRAINT_MEMCG` was not observed; do not invent that form. |
| `MORI-OOM-INVOKER` | `oom_kill` (context, do not add) | `GpuWatchdog invoked oom-killer: gfp_mask=0x140cca(GFP_HIGHUSER_MOVABLE\|__GFP_COMP), order=0, oom_score_adj=200` | 2026-10-13T23:44:30.570564-03:00, boot 0, system, kernel | Names the invoker. Here `GpuWatchdog`, not a fleet unit. Not itself a victim. |
| `MORI-OOM-UNIT-CHECK` | `oom_kill` (annotation, do not add) | `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: The kernel OOM killer killed some processes in this unit.` | 2026-10-13T23:44:30.574948-03:00, boot 0, systemd pid 1573. Same text on `user@1000.service` at .576028 (systemd pid 1) and on `user-1000.slice` at 2026-10-14T13:10:59.400591 | `MESSAGE_ID=fe6faa94e7774663a0da52717891d8ef`, `CODE_FUNC=unit_check_oom`. Walks up the cgroup. The slice line is 14h after the only kernel kill line, emitted as the slice stopped. Inference, high: same counter, not a second kill. The slice timestamp is not the kill time. |
| `MORI-OOM-UNIT-RESULT` | `oom_kill` and `unit-failure` (count the kernel line, not this) | `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: Failed with result 'oom-kill'.` | 2026-10-13T23:44:31.603001-03:00, boot 0, systemd pid 1573. In the user journal and the system journal | `MESSAGE_ID=d9b373ed55a64feb8242e02dbe79a49c`, `CODE_FUNC=unit_log_failure`. Arrives ~1.0s after the kernel kill. This is the only oom signature `--user -b` sees. Scope died because the kernel killed its process. Not a fleet-lane unit name. |
| `MORI-SIGKILL-STATUS9` | withheld. not `sigkill-user` | `user@1000.service: Main process exited, code=killed, status=9/KILL` | 2026-10-14T13:10:59.380873-03:00, boot 0, systemd pid 1, system only | `MESSAGE_ID=98e322203f7a4ed290d09fe03c09fe15`, `CODE_FUNC=unit_log_process_exit`. Only `status=9/KILL` in retained boots (system count 1, user count 0). 33ms after `pam_unix(sddm-autologin:session): session closed for user vgpnk` and `Removed session 1`. 13h after the OOM. Inference: session teardown of the user manager, not a user `kill -9` and not the OOM. Fleet reading: that user session's manager died; a new manager (pid 1203171) starts at 13:11:07. Actor field is absent, so the class is withheld. |
| `MORI-SIGKILL-USER-UNOBSERVED` | `sigkill-user` | no verbatim line | retained boots `-12..0`, measured 2026-10-14T21:33:40-03:00 | `journalctl -g SIGKILL` = 0, `journalctl -g 'signal 9'` = 0, user and system. The class is unobserved. Absence is not "no process was SIGKILLed": a kill of a non-unit pid leaves no journal line. Do not fill this class with `status=9/KILL`. |
| `MORI-SIGTERM-SDDM` | `sigterm` | `sddm[1579]: Signal received: SIGTERM` | 2026-10-13T10:57:27.702980-03:00, boot `-1` `73a8e2fc20cc48749b3cbd24ed5dc7c1`, system. Same text on sddm and sddm-helper at other boot-end stamps (2026-10-03 19:08:34, 2026-10-09 13:34:01, 2026-10-10 08:50:30, 2026-10-10 12:39:09) | Receiver self-report. The 2026-10-13 cluster is 11ms after `systemd-logind: The system will reboot now!` (observation of adjacency). Session/display stop, not a lane crash. Boot 0 count of `SIGTERM` is 0. |
| `MORI-SIGTERM-UWSM` | `sigterm` | `Received SIGTERM, stopping wayland-session-envelope@hyprland.desktop.target...` | 2026-10-09T13:34:01.954527-03:00, boot `-6`, uwsm pid 1600, user and system (`_TRANSPORT=stdout`) | Graphical session envelope stopping. Takes user services with it. Fleet-relevant as a session-stop marker, not as a lane fault. Two such lines in retained journals. Boot 0: 0. |
| `MORI-SIGTERM-APPDAEMON` | `sigterm` | `Received signal 15, stopping app daemon...` | 2026-10-13T10:57:27.704931-03:00, boot `-1`, `uwsm_app-daemon`, user unit `wayland-wm-app-daemon.service` | Same reboot cluster as the sddm line. Five lines, identical in user and system journals. `status=15/TERM` count is 0 everywhere: systemd never wrote that form. Match `signal 15`, not `status=15/TERM`. |
| `MORI-SIGTERM-AVAHI` | `sigterm` | `avahi-daemon[1378]: Got SIGTERM, quitting.` | 2026-10-13T10:57:27.724173-03:00, boot `-1`, system | Host daemon stop on the reboot path. Not a fleet process. Same text at the other boot-end stamps listed above. |
| `MORI-SIGTERM-GPG` | `sigterm` | `gpg-agent[393237]: SIGTERM received - shutting down ...` | 2026-10-10T08:50:30.467346-03:00, boot `-5`, system. Companion: `dirmngr[393186]: SIGTERM received - shutting down ...` at .467225 | Agent shutdown self-report at boot end. Not a fleet kill. |
| `MORI-SIGTERM-JOURNALD` | `sigterm` | `Received SIGTERM from PID 1 (systemd).` | 2026-10-11T16:14:45.012042-03:00, boot `-2` `2d8f74c552a247f999604450a379c77e`, `systemd-journald` pid 1038, system | Not a host shutdown. Same second: `Journal stopped`, new journald pid 108161 `Journal started`, and pid 1 stops then starts journald, resolved, timesyncd, udevd. Inference: pid-1 restart of journald. A SIGTERM tally that treats every receipt as fleet death false-positives on this restart and on reboot. |
| `MORI-SIGTERM-STATUS15-UNOBSERVED` | `sigterm` | `code=killed, status=15/TERM` not present | `journalctl -g 'status=15/TERM'` user 0, system 0, all retained boots, measured 2026-10-14T21:31:27-03:00 | The systemd exit form is unobserved. The class is still observed, via the self-report wordings above. Boot 0 has none of those either. |
| `MORI-SEGFAULT-KERNEL` | `segfault` | `love[3809675]: segfault at 55e953319 ip 00007fe0ff31f1b1 sp 00007ffe927bf020 error 4 in liblove-11.5.so[11f1b1,7fe0ff216000+299000] likely on CPU 12 (core 12, socket 0)` | 2026-10-14T15:25:09.186659-03:00, boot 0, system, kernel, priority 6, no `MESSAGE_ID` | CPU fault. Boot 0: 588 lines, all joined on pid to a `signal 11/SEGV` coredump (588/588). Dominant comm is `love`. A love segfault is a lane-runner crash, not host death and not OOM. |
| `MORI-SEGFAULT-GPF` | `segfault` only when joined to `11/SEGV` | `traps: love[3847294] general protection fault ip:7ff84911f1ae sp:7fffbf424ca0 error:0 in liblove-11.5.so[11f1ae,7ff849016000+299000]` | 2026-10-14T15:27:43.182658-03:00, boot 0, system, kernel | The kernel line has no signal number. Observation: all 38 boot-0 GPF lines share a pid with `terminated abnormally with signal 11/SEGV`. A matcher on `segfault at` alone misses these 38. Do not file the GPF text as segfault without that join. |
| `MORI-SEGV-HELPER` | `segfault` (system count only) | `Process 1129600 (love) of user 1000 terminated abnormally with signal 11/SEGV, processing...` | boot 0, `systemd-coredump`, `CODE_FUNC=coredump_kernel_helper`, no `MESSAGE_ID`. Timestamped companion: `Process 1203790 (pipewire-pulse) of user 1000 terminated abnormally with signal 11/SEGV, processing...` at 2026-10-14T18:54:21.261453-03:00 | System-journal event line. Boot 0: 657. User MESSAGE grep of this phrase: 0. Of the 657, 588 join to `segfault at`, 38 join to GPF, 31 have neither (23 `love`, 7 `blender`, 1 `bash`). The bash exemplar's stack is in `kill` / `kill_builtin` (pid 244048, 2026-10-13T14:45:31.224916-03:00): signal 11 is not always a CPU fault. The other 30 unmatched kernel companions are unknown. |
| `MORI-SEGV-USER-FIELD` | `segfault` (user-journal count) | no MESSAGE phrase. Field `COREDUMP_SIGNAL=11` (`COREDUMP_SIGNAL_NAME=SIGSEGV`) on `MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1` | `--user -b` 656 entries, system 657, measured 2026-10-14T21:43:03-03:00 | This is the contract-probe match. `COREDUMP_COMM`, `COREDUMP_UNIT`, `COREDUMP_USER_UNIT`, `COREDUMP_CGROUP` are the join. Do not also count the helper line. Do not output `COREDUMP_ENVIRON` or `COREDUMP_CMDLINE`. |
| `MORI-SEGV-DUMPED-CORE` | `segfault` (same event, do not add) | `Process 1203790 (pipewire-pulse) of user 1000 dumped core.` | 2026-10-14T18:54:21.348195-03:00, boot 0, systemd-coredump pid 761917 | MESSAGE text of the `fc2e22bc` record, when present. `--user -b -g 'dumped core'` returned 1044 entries at 21:43:03 against 1051 field entries. MESSAGE grep undercounts. Field match is the count. |
| `MORI-UNIT-DUMPED-11` | `segfault` and `unit-failure` (count the coredump line) | `pipewire-pulse.service: Main process exited, code=dumped, status=11/SEGV` | 2026-10-14T18:54:21.350354-03:00, boot 0, systemd pid 1203171 (user manager) | `MESSAGE_ID=98e322203f7a4ed290d09fe03c09fe15`. Only present when the dead pid is a unit main process. 657 SIGSEGV deaths, 2 `code=dumped` lines in all retained journals. The fleet crash mass is not a unit-failure. |
| `MORI-UNIT-CORE-DUMP` | `unit-failure` (and `segfault` if joined to status 11) | `pipewire-pulse.service: Failed with result 'core-dump'.` | 2026-10-14T18:54:21.350449-03:00, boot 0, user journal and system journal | `MESSAGE_ID=d9b373ed55a64feb8242e02dbe79a49c`. 95ms after the kernel `pipewire-pulse[1203790]: segfault at 0 ... in libpipewire-0.3.so.0.1608.0`. A user session service died mid-boot (consumed 5h 43min). That is a service crash, not host OOM. Second exemplar, different reading: `app-com.onepassword.OnePassword@autostart.service: Failed with result 'core-dump'.` at 2026-10-13T10:57:28.011711-03:00, boot `-1`, same second as the reboot. Shutdown-adjacent; do not call it a mid-run fleet fault without a kernel line. |
| `MORI-UNIT-SIGNAL` | `unit-failure` | `user@1000.service: Failed with result 'signal'.` | 2026-10-14T13:10:59.381949-03:00, boot 0, systemd pid 1 | Same `MESSAGE_ID` as every other `Failed with result`. The result token `signal` is not a cause. Read the preceding `unit_log_process_exit` line (`status=9/KILL`). See withheld row. |
| `MORI-UNIT-EXIT-CODE` | `unit-failure` (not a kill) | `elephant.service: Failed with result 'exit-code'.` | 2026-10-11T16:14:34.699064-03:00, boot `-2`, systemd pid 1582, user journal | Preceded by `elephant.service: Main process exited, code=exited, status=1/FAILURE` at .698531. Followed by `Scheduled restart job, restart counter is at 1.` and `Started Elephant.` Non-zero exit, not a signal, not OOM. A gate that fires on every `Failed with result` false-positives here. mori does not restart it. |

### Assigned class with no confirming signature

`sigkill-user` has no journal line that says a user sent SIGKILL. Mapping `status=9/KILL` onto it is the false positive this table exists to prevent.

`systemd-oomd` / `Killed ... due to memory pressure` / `oomd.service`: 0 lines (`journalctl -b -g systemd-oomd` rc 1; `journalctl -g oomd.service --case-sensitive=true` = 0). Unobserved. Unit enablement is not claimed (that is tsukuroi).

## Match rules

Use `--case-sensitive=true`. Default `-g` with an all-lowercase pattern matched `OOMDetails` inside coredump stacks: boot 0, `oomd`, `OOMD`, and `OOMDetails` each returned 3037 cat-lines. Those stacks are V8 `ReportOOMFailure` / `FatalProcessOutOfMemory` / `OOMDetails`, paired with `signal 6/ABRT`, not with the kernel kill line.

Count an event once. On `--user`, count `COREDUMP_SIGNAL`, not the helper phrase (that phrase is absent there). On the system journal, the helper line and `COREDUMP_SIGNAL` are the same death; do not add them. Do not request `COREDUMP_ENVIRON` or `COREDUMP_CMDLINE`.

```
journalctl -b --case-sensitive=true -g '^Out of memory: Killed process ' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g '^oom-kill:constraint=' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'invoked oom-killer:' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'The kernel OOM killer killed some processes in this unit\.' -o short-iso-precise --no-pager
journalctl --user -b --case-sensitive=true -g "Failed with result 'oom-kill'." -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'code=killed, status=9/KILL' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'SIGTERM|signal 15' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'segfault at ' -o short-iso-precise --no-pager
journalctl -b --case-sensitive=true -g 'terminated abnormally with signal 11/SEGV, processing' -o short-iso-precise --no-pager
journalctl --user -b COREDUMP_SIGNAL=11 -o json --output-fields=COREDUMP_SIGNAL,COREDUMP_SIGNAL_NAME,COREDUMP_COMM,COREDUMP_PID,COREDUMP_UNIT,COREDUMP_USER_UNIT,COREDUMP_CGROUP,MESSAGE_ID --no-pager
journalctl -b --case-sensitive=true -g "Failed with result '(oom-kill|signal|core-dump|exit-code)'." -o short-iso-precise --no-pager
```

`Failed with result` shares one `MESSAGE_ID` (`d9b373ed55a64feb8242e02dbe79a49c`). The result token is the discriminator. `unit_log_process_exit` shares `98e322203f7a4ed290d09fe03c09fe15` across `status=9/KILL` and `code=dumped, status=11/SEGV`. Do not key a class on `MESSAGE_ID` alone.

Negative exemplars, not events:

| id | verbatim | why it is not a class hit |
|---|---|---|
| `MORI-OOM-STACKFRAME` | `oom_kill_process.cold+0x8/0x91` (2026-10-13T23:44:30.634812-03:00, kernel, two leading spaces) | Call frame inside the oom dump. A substring search for `oom_kill` counts it. |
| `MORI-OOM-V8-STACK` | `_ZN2v85Utils16ReportOOMFailureEPNS_8internal7IsolateEPKcRKNS_10OOMDetailsE` inside a coredump stack | Case-insensitive `oomd` hit. Process-local heap abort. See ABRT row. |
| `MORI-OOM-SLICE-DELAY` | `user-1000.slice: The kernel OOM killer killed some processes in this unit.` at 2026-10-14T13:10:59.400591-03:00 | Same `unit_check_oom` id, stamped at slice stop. Not a new kill. |

## Adjacent signatures (observed, not one of the five)

Filing these into `segfault` or `oom_kill` is the misclassification.

| id | verbatim signature | exemplar | reading |
|---|---|---|---|
| `MORI-ABRT-COREDUMP` | `Process 71222 (MainThread) of user 1000 terminated abnormally with signal 6/ABRT, processing...` | 2026-10-13T12:43:31.986776-03:00, boot 0 | Boot 0: 365. Comm: godot 318, MainThread 25, love 16, waybar 6. No kernel `segfault at` join (365/365 unmatched). Not OOM. Not segfault. |
| `MORI-TRAP-INT3` | `traps: Typora[102768] trap int3 ip:55cd4a871195 sp:7fff38bf1a20 error:0 in Typora[70ea195,55cd45e08000+9aa1000]` | 2026-10-13T13:47:02.148653-03:00, boot 0 | 25/25 join to `signal 5/TRAP`. Companion: `Process 102768 (Typora) of user 1000 terminated abnormally with signal 5/TRAP, processing...` at .149334. Not segfault. |
| `MORI-TRAP-NOCORE` | `Process 149109 (MainThread) of user 1000 terminated abnormally without generating a coredump.` | 2026-10-13T13:55:35.050269-03:00, boot 0, `--user`, systemd-coredump pid 149118. Same shape for pids 154780, 189795, 196055, 253012, 253029, 256319 | 7 entries, rechecked 2026-10-14T21:44:56-03:00. Same `MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1` as dumped-core records, `COREDUMP_SIGNAL=5`. A `dumped core` grep misses them. Not segfault. Not the 656-vs-657 SIGSEGV gap. |
| `MORI-BUS-COREDUMP` | `Process 1282371 (chrome_crashpad) of user 1000 terminated abnormally with signal 7/BUS, processing...` | 2026-10-13T22:48:02.949171-03:00, boot 0 | Boot 0: 5 (chrome_crashpad 2, grok-bot 3). No kernel fault line in the `segfault`/`gpf`/`int3` set. Not segfault. |
| `MORI-HYPRLAND-SEGV-AFTER-SESSION` | `Hyprland[1203102]: segfault at 0 ip 00007f0949128fe1 sp 00007ffcb9a67fb0 error 4 in libaquamarine.so.0.15.0[bbfe1,7f0949098000+e3000] likely on CPU 4 (core 4, socket 0)` | 2026-10-14T13:11:07.408647-03:00, boot 0 | 8s after the user-manager `status=9/KILL`, during the new session (`Stopping... "start-hyprland"` at 13:11:07.370). Observation of order: it did not precede the SIGKILL. Do not cite it as the cause of the session drop. |

Boot-0 coredump comm histogram (`terminated abnormally with signal`, 1052 lines, 0 non-matching cat lines), measured 2026-10-14T21:35:19-03:00:

| signal | n | comm |
|---|---|---|
| 11/SEGV | 558 | love |
| 6/ABRT | 318 | godot |
| 11/SEGV | 84 | pw-play |
| 6/ABRT | 25 | MainThread |
| 5/TRAP | 22 | MainThread |
| 6/ABRT | 16 | love |
| 11/SEGV | 7 | blender |
| 6/ABRT | 6 | waybar |
| 11/SEGV | 4 | python3 |
| 7/BUS | 3 | grok-bot |
| 5/TRAP | 2 | Typora |
| 7/BUS | 2 | chrome_crashpad |
| 5/TRAP | 1 | electron |
| 11/SEGV | 1 | bash |
| 11/SEGV | 1 | Hyprland |
| 11/SEGV | 1 | pw-cat |
| 11/SEGV | 1 | pipewire-pulse |

Inference, not identity: `love` and `godot` comms match game-dev lane runners. The journal line does not name the wave or the lane. Unknown which wave, if any, owned a given pid.

## Name searches that must not be mapped onto the kill

| search | command | result | reading |
|---|---|---|---|
| webbridge | `journalctl -g webbridge --case-sensitive=true` and `--user` the same, measured 2026-10-14T21:32:10-03:00 | 0 / 0 | The operator account of a 2026-10-14 webbridge OOM (`.ufo/scopes/shokunin-12h-20261014/operator-demand.md`) is demand text, not this journal. Do not attach it to the python3 kill. |
| kimi kill-words | case-sensitive `kimi`, then scan for oom/killed/segfault/SIGKILL/SIGTERM/signal 9/signal 15/core-dump/oom-kill | 2198 lines, 0 co-occurrences, measured 2026-10-14T21:36:04-03:00 | No kill signature on a kimi line. Text not quoted. |

## What a later run compares

Stable: the id, the signature prefix, the `MESSAGE_ID` where present, the result token, which journal surface has the line.

Volatile, not drift: pid, addresses, rss figures, comm counts, boot-0 totals while the boot is open.

Unobserved stays `unobserved` until a line of that form is quoted with its command and timestamp. It does not become `unhealthy`.

One death, five lines, in order, for the only service-scoped segfault this boot (pipewire-pulse pid 1203790, 2026-10-14T18:54:21):

1. kernel `segfault at 0` — `MORI-SEGFAULT-KERNEL` (system journal only)
2. coredump helper `signal 11/SEGV, processing...` — system count; absent from `--user` MESSAGE
3. `MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1` with `COREDUMP_SIGNAL=11` — user-journal count of the same death; do not add to the helper line
4. `Main process exited, code=dumped, status=11/SEGV` — unit annotation
5. `Failed with result 'core-dump'.` — unit-failure token

The only host-global kill (python3 pid 1732581, 2026-10-13T23:44:30) is the kernel `Out of memory: Killed process` line. The scope `Failed with result 'oom-kill'.` is the user-journal shadow of that same death.
