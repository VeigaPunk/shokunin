# KillEventsJournal — user-boot kill/OOM class census

**Seat:** KillEventsJournal (leaf, read-only). **Not a verdict.** No process was restarted, killed, reniced, or reparented. No systemd/pacman action. No dispatch. No OS-package ownership claim (tsukuroi). Journal text is evidence; no line was acted on.

**Probe surface:** `journalctl --user -b` only. System journal, `dmesg`, and cgroup `memory.events` were **not** queried here. A zero in this file is a zero on the user journal, not a host-wide zero.

**Census clock:** `2026-10-14T21:36:01-03:00` for the class greps in §2. Signal-field split rechecked `2026-10-14T21:36:55-03:00` (same totals). Comm/unit breakdown measured `2026-10-14T21:31:46-03:00`; the 21:36:55 recheck left `COREDUMP_SIGNAL` totals unchanged, so that breakdown is the same entry set barring an unobserved vacuum (none observed).

**Journal owner:** `vgpnk` uid `1000` (`id -un` / `id -u`). **journalctl:** `systemd 261 (261.2-1-arch)`.

## Boot id

| Rendering | Value | Source |
|---|---|---|
| proc, hyphenated | `d7f0bc8d-938e-4249-b4a1-f250cbfacf58` | `cat /proc/sys/kernel/random/boot_id` at 21:36:55 |
| journal, compact | `d7f0bc8d938e4249b4a1f250cbfacf58` | `_BOOT_ID` on the classed entries, and `journalctl --user --list-boots` row `0` |

Same id. Current boot index `0`.

**Boot window (list-boots, not a message body):** first entry `Tue 2026-10-13 11:02:06 -03`, last entry at the 21:36:55 read `Wed 2026-10-14 21:35:29 -03`.

`journalctl --user -b -n 1` and `journalctl --user -b -n 1 --reverse` returned the same newest entry. That invocation does **not** yield the oldest entry. Window start is the list-boots first-entry column only.

The newest entry's message is an application session-keepalive log. It contains an account identifier. **Shape only: identifier present, not copied.** It matches none of the class greps below.

Surface status: **available**. `journalctl --user -b` returned entries. `JOURNAL_UNAVAILABLE` does not apply. A class count of 0 is observed absence, not an unavailable surface, not unhealthy.

## 1. Locked class counts

Entry counts (`-o json` lines), not `-o cat` line counts. `-o cat | wc -l` is a trap: `dumped core` was **154687** cat-lines and **1044** entries (multiline stack traces).

| Class | Count | Exact command | rc |
|---|---:|---|---:|
| `oom-kill` | **1** | `journalctl --user -b --no-pager --case-sensitive=true -g 'oom-kill' -o json` | 0 |
| `killed-by-signal` | **0** | `journalctl --user -b --no-pager --case-sensitive=true -g 'killed-by-signal\|killed by signal\|code=killed' -o json` | 1 (no match, empty stderr) |
| `segfault` | **656** | `journalctl --user -b --no-pager -o json COREDUMP_SIGNAL=11` | 0 |
| `unit-failure` | **2** | `journalctl --user -b --no-pager --case-sensitive=true -g 'Failed with result' -o json` | 0 |

The segfault count is a **field match**, not a MESSAGE grep. A MESSAGE grep cannot see these entries. That is the operability result, not a substitute count.

### Literal class-token grep (the trap)

```text
journalctl --user -b --no-pager --case-sensitive=true -g 'oom-kill|killed-by-signal|segfault|unit-failure' -o json
```

**1 entry** (rc 0). The only MESSAGE that contains any of those four tokens is the oom-kill unit line. `killed-by-signal`, `segfault`, and `unit-failure` are **not** strings systemd wrote this boot. A gate that greps the class nicknames will report segfault=0 and unit-failure=0 while the operational counts are 656 and 2.

`--case-sensitive=true` was set on every class grep above. Help text: `--case-sensitive[=BOOL] Force case sensitive or insensitive matching`. Default folding was not assumed from a man page. Observation: `-g oomd` **without** `--case-sensitive` matched the substring `OOMD` inside `OOMDetails` in coredump stacks (38 entries, all `SYSLOG_IDENTIFIER=systemd-coredump`). Those are not oom-kill events. See §4.

## 2. Per-class evidence

### 2.1 `oom-kill` — 1

Same entry via `UNIT_RESULT=oom-kill` (1, rc 0). No second oom-kill line.

| Field | Value |
|---|---|
| id | `OOM_KILL_EVENT` |
| subject | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;ts=1791945871603010` |
| cursor | `s=c55f7dd7155740a3818b8eec3ba0ff79;i=23d3d;b=d7f0bc8d938e4249b4a1f250cbfacf58;m=ab5613bda;t=65dc3e9223542;x=6f73778c68c4ea6f` |
| time | `2026-10-13T23:44:31.603010-03:00` |
| MESSAGE_ID | `d9b373ed55a64feb8242e02dbe79a49c` (catalog subject: Unit failed) |
| CODE_FUNC | `unit_log_failure` |
| USER_UNIT | `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope` |
| `_SYSTEMD_USER_UNIT` | `init.scope` (the logger, not the failed unit) |
| `_PID` | `1573` (`systemd`) |
| UNIT_RESULT | `oom-kill` |
| PRIORITY | 4 |
| MESSAGE | `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: Failed with result 'oom-kill'.` |

Checked and **0** on this user boot (case-sensitive MESSAGE grep unless noted):

| Signature | Entries |
|---|---:|
| `Killed process` | 0 |
| `Out of memory` | 0 |
| `systemd-oomd` | 0 |
| `MESSAGE_ID=d989611b15e44c9dbf31e3c81256e4ed` (catalog: systemd-oomd killed one or more processes) | 0 |
| `SYSLOG_IDENTIFIER=systemd-oomd` | 0 |
| `oom_kill_process` / `oom_kill_process.cold` | 0 |
| `unit_check_oom` | 0 |

The user-journal line does not name a pid, a signal, or a cgroup. Mechanism (kernel OOM vs systemd-oomd vs other) is **unknown from this probe**. System journal was not read here; do not treat that as zero kernel lines. Recheck at `2026-10-14T21:42:01-03:00`: `Killed process`, `Out of memory`, `oom_kill_process.cold`, and `unit_check_oom` are still 0 on `--user -b`. Those strings are not in the oom-kill count. A sibling report of one system-journal `Out of memory: Killed process` was not re-measured here.

`fleet_relevant`: **unknown**. Observation: `USER_UNIT` is a Hyprland xdg-terminal scope; the name does not contain `tmux`, `ufo`, `watchdog`, or a fleet path. The killed pid is not in the line. This seat does not claim the unit is or is not a fleet process.

This line is also a unit-failure line (§2.4). Primary class for compare: `oom-kill` / `OOM_KILL_EVENT`. Do not also emit `UNIT_FAIL_EVENT` for this same line (FindingIds dedup).

### 2.2 `killed-by-signal` — 0

The hyphenated token is not a systemd format string. `libsystemd-shared-261.2-1.so` contains `Child process %i was killed by signal %s, ignoring.` and `Child process %i dumped core by signal %s, ignoring.` Neither phrase was emitted.

| Signature | Entries | rc |
|---|---:|---:|
| `-g 'killed-by-signal'` case-sensitive | 0 | 1 |
| `-g 'killed by signal'` case-sensitive | 0 | 1 |
| `-g 'was killed by signal'` | 0 | 1 |
| `-g 'dumped core by signal'` | 0 | 1 |
| `-g 'code=killed'` case-sensitive | 0 | 1 |
| `-g 'status=9/KILL'` | 0 | 1 |
| `-g 'status=15/TERM'` | 0 | 1 |
| `-g 'SIGKILL'` | 0 | 1 |
| `-g 'SIGTERM'` | 0 | 1 |
| `UNIT_RESULT=signal` | 0 | 0 |
| `EXIT_CODE=killed` | 0 | (field; 0 entries) |
| `COREDUMP_SIGNAL=9` (SIGKILL) | 0 | 0 |
| `COREDUMP_SIGNAL=15` (SIGTERM) | 0 | 0 |
| `COREDUMP_SIGNAL=2` (SIGINT) | 0 | 0 |
| `COREDUMP_SIGNAL=1` (SIGHUP) | 0 | 0 |
| `COREDUMP_SIGNAL=13` (SIGPIPE) | 0 | 0 |

`KILL_SIGNAL_EVENT` predicate (SIGKILL/SIGTERM, or the phrase `killed by signal`) is false this user boot. Not unavailable. Recheck at `2026-10-14T21:42:01-03:00`: `status=9/KILL` and `status=15/TERM` still 0 on `--user -b`. A system-journal `status=9/KILL` for `user@1000` at session close, if it exists, is outside this surface and is not added.

`-g` with no matches exits **1** with empty stderr. An unrecognized option also exits **1**, with stderr `journalctl: unrecognized option '--not-a-real-flag'`. A field match with zero hits was observed to exit **0** (`UNIT_RESULT=signal`). A gate must not treat rc 1 alone as `JOURNAL_UNAVAILABLE`.

### 2.3 `segfault` — 656

MESSAGE greps, case-sensitive:

| Grep | Entries |
|---|---:|
| `segfault` | 0 |
| `segmentation fault` | 0 |
| `SIGSEGV` | 0 |
| `status=11/SEGV` | **1** (unit process-exit line, not a coredump MESSAGE) |

Field match `COREDUMP_SIGNAL=11`: **656** entries. All 1051 `SYSLOG_IDENTIFIER=systemd-coredump` entries (`MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1`) have a `COREDUMP_SIGNAL`. Signal 11 is the segfault class. Signals 5, 6, and 7 are not (§5).

Span of the 656: first `2026-10-13T14:45:31-03:00`, last `2026-10-14T20:54:35-03:00`.

Comm / exe / user unit (observation, 21:31:46; totals still 656 at 21:36:55):

| comm | exe | n |
|---|---|---:|
| `love` | `/usr/bin/love` | 558 |
| `pw-play` | `/usr/bin/pw-cat` | 84 |
| `blender` | `/usr/bin/blender` | 7 |
| `python3` | `/usr/bin/python3.14` | 4 |
| `bash` | `/usr/bin/bash` | 1 |
| `pw-cat` | `/usr/bin/pw-cat` | 1 |
| `pipewire-pulse` | `/usr/bin/pipewire` | 1 |

| COREDUMP_USER_UNIT | n |
|---|---:|
| `app-Hyprland-xdg\x2dterminal\x2dexec-4b06c09c.scope` | 625 |
| `app-Hyprland-xdg\x2dterminal\x2dexec-c550e4d0.scope` | 18 |
| `app-Hyprland-xdg\x2dterminal\x2dexec-d7a10fd5.scope` | 11 |
| `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope` | 1 |
| `pipewire-pulse.service` | 1 |

`pw-play` comm with exe `/usr/bin/pw-cat` is two fields on the same entries, not two populations. 84+1=85 `pw-cat` exe.

**Additional segfault line (not inside the 656):**

| Field | Value |
|---|---|
| id | `SEGFAULT_EVENT` |
| subject | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;ts=1792014861351047` |
| cursor | `s=c55f7dd7155740a3818b8eec3ba0ff79;i=28018;b=d7f0bc8d938e4249b4a1f250cbfacf58;m=1ac57d3f1f;t=65dd3f93e3887;x=e5fee71bae617399` |
| time | `2026-10-14T18:54:21.351047-03:00` |
| MESSAGE_ID | `98e322203f7a4ed290d09fe03c09fe15` (catalog: Unit process exited) |
| CODE_FUNC | `unit_log_process_exit` |
| USER_UNIT | `pipewire-pulse.service` |
| EXIT_CODE / EXIT_STATUS | `dumped` / `11` |
| `_PID` | `1203171` (systemd, the logger) |
| MESSAGE | `pipewire-pulse.service: Main process exited, code=dumped, status=11/SEGV` |

Coredump entry for the same second, different cursor, signal 11, pid **1203790**, comm `pipewire-pulse`, unit `pipewire-pulse.service`, first line `Process 1203790 (pipewire-pulse) of user 1000 dumped core.` Cursor `s=c55f7dd7155740a3818b8eec3ba0ff79;i=28016;b=d7f0bc8d938e4249b4a1f250cbfacf58;m=1ac57d3404;t=65dd3f93e2d6c;x=43922068338df63d`.

**Inference:** those two entries plus the unit-failure line in §2.4 are one death. The process-exit line does not carry the pid, so the shared-pid link is not on that line. Not proven; time, unit, and signal agree.

Class count stays **656** (field) plus **1** process-exit line. Union of journal entries = 657. Inferred deaths = 656. A later run that diffs only `COREDUMP_SIGNAL=11` will not see the process-exit line; the `status=11/SEGV` grep will.

Per-entry cursors for the 656 were not inlined. Generator: the field command above. Compare key for the aggregate: `boot=d7f0bc8d938e4249b4a1f250cbfacf58;class=segfault;probe=COREDUMP_SIGNAL=11` payload `count=656`.

Stack traces were not copied. `COREDUMP_ENVIRON` / `COREDUMP_CMDLINE` were not requested.

### 2.4 `unit-failure` — 2

Token grep `-g 'unit-failure'` case-sensitive: **0**. Catalog subject text `entered the 'failed' state`: **0** entries. Live MESSAGE is `Failed with result`, not the catalog subject.

`MESSAGE_ID=d9b373ed55a64feb8242e02dbe79a49c`: **2**, same two lines as `Failed with result`.

| # | time | USER_UNIT | UNIT_RESULT | primary class | MESSAGE |
|---|---|---|---|---|---|
| 1 | `2026-10-13T23:44:31.603010-03:00` | `app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope` | `oom-kill` | `oom-kill` (§2.1) | `Failed with result 'oom-kill'.` |
| 2 | `2026-10-14T18:54:21.351493-03:00` | `pipewire-pulse.service` | `core-dump` | core-dump / segfault-adjacent | `Failed with result 'core-dump'.` |

Line 2 subject: `boot=d7f0bc8d938e4249b4a1f250cbfacf58;ts=1792014861351493`. Cursor `s=c55f7dd7155740a3818b8eec3ba0ff79;i=28019;b=d7f0bc8d938e4249b4a1f250cbfacf58;m=1ac57d40dd;t=65dd3f93e3a45;x=41353fdb0a9528d0`. MESSAGE_ID `d9b373ed55a64feb8242e02dbe79a49c`. CODE_FUNC `unit_log_failure`. `_PID` `1203171`. 446 µs after the `status=11/SEGV` process-exit line.

Other unit-result field counts this user boot: `signal` 0, `exit-code` 0, `timeout` 0, `watchdog` 0, `start-limit-hit` 0, `resources` 0, `failure` 0, `success` 0. `Failed to start` / `Failed to stop`: 0.

**Dedup (catalog, not a second count):** both lines are already classed (`oom-kill`, `core-dump`). Residual `UNIT_FAIL_EVENT` (Failed with result **other than** oom-kill/core-dump) = **0**. The assignment class `unit-failure` is still **2 lines**. A gate that counts `Failed with result` and also counts `oom-kill` will double-count line 1 unless it dedups.

The two lines were logged by different systemd pids (`1573`, then `1203171`). That is an observation about `_PID`. Whether the user manager restarted is **not** established by these two lines alone. Not a finding of this seat.

`_SYSTEMD_USER_UNIT` on both is `init.scope`. Key failed units off `USER_UNIT`, not `_SYSTEMD_USER_UNIT`.

## 3. Overlap

| Pair | Shared entries | Note |
|---|---:|---|
| oom-kill ∩ unit-failure | 1 | the 23:44:31 line |
| killed-by-signal ∩ any other class | 0 | class is empty |
| `COREDUMP_SIGNAL=11` ∩ unit-failure lines | 0 | different entries; inferred same death as the core-dump unit line |
| `status=11/SEGV` ∩ unit-failure | 0 | sibling lines, 446 µs apart |
| `UNIT_RESULT=core-dump` | 1 | the pipewire unit-failure line only |

## 4. Adjacent entries — not filed into the four classes

All `systemd-coredump` entries: **1051**. Phrase split: `dumped core` **1044** + `terminated abnormally` **7** = 1051. The 7 are all `COREDUMP_SIGNAL=5`.

| COREDUMP_SIGNAL | name | n | first | last | why not a class |
|---|---|---:|---|---|---|
| 11 | SIGSEGV | 656 | 2026-10-13T14:45:31-03:00 | 2026-10-14T20:54:35-03:00 | **is** the segfault class |
| 6 | SIGABRT | 365 | 2026-10-13T12:43:33-03:00 | 2026-10-14T21:00:36-03:00 | not segfault; not `killed by signal`; not SIGKILL/SIGTERM |
| 5 | SIGTRAP | 25 | 2026-10-13T13:47:12-03:00 | 2026-10-13T15:16:55-03:00 | same; 7 say `terminated abnormally without generating a coredump` |
| 7 | SIGBUS | 5 | 2026-10-13T22:48:02-03:00 | 2026-10-14T01:07:28-03:00 | bus error, not segfault |

SIGABRT comm (not a class count): `godot` 318, `MainThread` 25 (exe node `v24.21.0`), `love` 16, `waybar` 6.

SIGTRAP comm: `MainThread` 22, `Typora` 2, `electron` 1.

SIGBUS comm: `grok-bot` 3, `chrome_crashpad` 2.

Filing ABRT/TRAP/BUS into `killed-by-signal` would change that class from 0 to 395. This census does **not**. The journal did not use the killed-by-signal signature, and the assignment lists segfault separately from killed-by-signal, so signal identity is the class boundary.

`oomd` substring, default grep (case-folded, see §1): **38** coredump entries. Sampled match context is the C++ symbol fragment `ReportOOMFailure` / `OOMDetails`, not a systemd-oomd kill. Not added to `oom-kill`.

Scope `dd9e67bd` also has **100** coredump entries (signal 6 ×77, 5 ×22, 11 ×1), span `2026-10-13T12:43:33-03:00` to `2026-10-13T23:37:48-03:00`, comm `godot` 52 / `MainThread` 47 / `bash` 1. The oom-kill line for that scope is **23:44:31**, after the last of those coredumps. Co-located unit name. **Not** evidence that those crashes are the oom-kill, or that the oom-kill caused them.

## 5. Observation / inference / unknown

**Observation**

- Boot id, window, and the four counts in §1, with the commands that produced them.
- Verbatim MESSAGEs in §2.
- `COREDUMP_SIGNAL` histogram 11/6/5/7 = 656/365/25/5.
- Literal nickname grep returns 1, not 1+0+656+2.
- `-o cat` line counts over-count multiline messages.
- `-g` no-match rc is 1 with empty stderr; that is not an unavailable journal.

**Inference**

- pipewire-pulse coredump pid 1203790, the `status=11/SEGV` line, and `Failed with result 'core-dump'` are one death. Shared pid is only on the coredump entry.
- `\x2d` in the scope name is systemd's escaped hyphen. Decoded display form `app-Hyprland-xdg-terminal-exec-dd9e67bd.scope` is that escape, not a second unit. Compare on the JSON `USER_UNIT` string, not a rendered form.
- `pw-play` is `/usr/bin/pw-cat` (both fields present).

**Unknown**

- Pid and cgroup of the oom-kill. Not in the user-journal line.
- Whether that oom-kill was kernel OOM, systemd-oomd, or another producer. User-journal oomd catalog id is 0. System journal not read here.
- Whether the oom-killed process was fleet-relevant.
- Whether the user manager restart/re-exec happened between `_PID` 1573 and 1203171.
- Host-wide segfault and kernel oom-kill counts. Out of scope. Not zero.
- Case-sensitive `-g oomd` was not re-counted. The 38 hits are the case-folded invocation.

## 6. Compare keys

A later run diffs these. Payload `measured_at` is volatile. Counts are the compare payload.

| id | subject | payload |
|---|---|---|
| `OOM_KILL_EVENT` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;ts=1791945871603010` | `count=1;unit=app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope;result=oom-kill;fleet_relevant=unknown` |
| `KILL_SIGNAL_EVENT` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;class=killed-by-signal` | `count=0` |
| `SEGFAULT_EVENT` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;class=segfault;probe=COREDUMP_SIGNAL=11` | `count=656` |
| `SEGFAULT_EVENT` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;ts=1792014861351047` | `count=1;unit=pipewire-pulse.service;exit=dumped;status=11` |
| `UNIT_FAIL_LINES` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;class=unit-failure;probe=Failed with result` | `count=2` |
| `UNIT_FAIL_EVENT` | `boot=d7f0bc8d938e4249b4a1f250cbfacf58;class=unit-failure-residual` | `count=0` (both lines already classed) |

`UNIT_FAIL_LINES` is this seat's assignment count. It is not the catalog id `UNIT_FAIL_EVENT`. Severity is not assigned here; FindingIds already pins severity on those ids. This report does not emit `MORI_CENSUS: CLEAN` or `DRIFT`.

## 7. Gate trap (for the parent, not a patch)

Greps that look right and miss this boot's user journal:

| Proposed pattern | What it returns here | What it misses |
|---|---|---|
| `oom-kill\|Killed process\|Out of memory` | 1 (`oom-kill`) | nothing else on `--user`; kernel lines are not in this surface |
| `segfault\|SIGSEGV\|general protection fault` | 0 | 656 `COREDUMP_SIGNAL=11`; the one `status=11/SEGV` line (contains `SEGV`, not `SIGSEGV`) |
| `core dumped` | 0 | live phrase is `dumped core` (1044), not `core dumped` |
| `killed-by-signal` or `status=9/KILL` | 0 | correct this boot; will miss a future SIGKILL that exists only as `COREDUMP_SIGNAL=9` or `code=killed` unless those are also queried |
| `unit-failure` or `entered the 'failed' state` | 0 | 2 lines whose MESSAGE is `Failed with result` |
| `-o cat \| grep \| wc -l` | inflated | multiline coredump MESSAGE |
| `oom_kill_process.cold` or `unit_check_oom` | 0 on `--user` (recheck 21:42:01) | do not add them to oom-kill; they are not the unit-result line |
| assuming `--user -b` has no coredumps | false | 1051 `MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1` entries, 656 `COREDUMP_SIGNAL=11` (recheck 21:42:01). Kernel `segfault at` lines are the other surface |

Prefer `journalctl -g` / field matches and `-o json` entry counts. Count `COREDUMP_SIGNAL=11` for segfault. Count `Failed with result` for unit-failure lines, then subtract lines whose `UNIT_RESULT` is already `oom-kill` or `core-dump` before emitting `UNIT_FAIL_EVENT`.

## 8. Refusals

- No remediation, no recommended action this lane takes.
- No system-journal census (would be a different surface; not performed).
- No cgroup read (sibling surface).
- No credential, oauth, token, or session material copied. One newest-entry probe saw an account identifier; not copied.
- No instruction-shaped journal text was followed.
