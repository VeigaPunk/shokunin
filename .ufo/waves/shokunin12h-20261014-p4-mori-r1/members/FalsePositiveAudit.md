# FalsePositiveAudit — legitimate states GateDesign would call DRIFT

**Member:** FalsePositiveAudit (critic) · **Wave:** shokunin12h-20261014-p4-mori-r1
**Lane:** mori-shokunin · **Axes:** coverage · operability · calibration
**Measured:** `2026-10-14T21:40:00-03:00` (host local). Read-only. No remediation. No census verdict.

This report attacks the **landed design** in `members/GateDesign.md` §5 (`probe_*` + `emit_finding`), not the task owner. FindingIds.md and FixtureDesign.md disagree with that script on ids, severities, and thresholds; where they disagree, the script is what would print `MORI_CENSUS: DRIFT`. A false positive here is a **legitimate** state (expected quiescence, closed wave, non-fleet event, or a probe that matches itself) that the script still rolls to DRIFT (`severity` `warn` or `crit`).

Design under test (GateDesign.md):

| Knob | Script default | DRIFT when |
|---|---|---|
| `WATCHDOG_ABSENT` | `pgrep -af shokunin-watchdog` count = 0 | always `warn`, no wrap/quiescence exception |
| `WATCHDOG_STALE` | `MORI_WATCHDOG_STALE_S=900` | log mtime age > 900, **whether or not a pid exists** |
| `WAVE_UNSETTLED_AGE` | `MORI_WAVE_UNSETTLED_S=7200` | `swarm-registry.json` **or** `dispatch.json` **or** `run.json`, and none of `results.json` / `closeout.json` / `mission-result.json`, and newest file age > 7200 |
| `OOM_KILL_JOURNAL` | class regex | count > 0 → `crit`. Also matches `Killed process` |
| `KILL_SIGNAL_JOURNAL` | class regex | count > 0 → `warn` |
| `CGROUP_OOM_KILL` | `oom_kill > 0` on `user-$(id -u).slice` | `crit`, absolute, no baseline |
| `DISK_LOW` / `DISK_CRITICAL` | 85% / 95% | `df -P` Capacity on `ROOT` and `/tmp` |
| `LANE_SILENT` | `MORI_LANE_SILENCE_S=7200` | roster lane HEAD **and** newest non-`.git` file both older than the window → `warn` |

`SEGFAULT_JOURNAL` and `UNIT_FAILURE_JOURNAL` are `info` in this script, so they do **not** flip DRIFT. They are out of scope below.

Live anchors below are observations that show the predicate is not hypothetical. They are not a `MORI_CENSUS` verdict. Each fixture is hermetic: `MORI_NOW_EPOCH=1760472000`, `MORI_FLEET_ROOT=$FX` (script name: `MORI_SHOKUNIN_ROOT`), stubs only, no live `/proc`, journal, cgroup, or `df`.

---

## FP-1 — Deliberate fleet-wrap quiescence is `WATCHDOG_ABSENT` + `WATCHDOG_STALE`

**Legitimate state.** `scripts/shokunin-watchdog.sh` writes `wrap <lane> round=N complete; NOT respawning (fleet-wrap)` and then stops launching. A stopped driver after a full wrap is the success path, not a death. FindingIds.md §3.1 already says: pid gone after an explicit `complete`/`wrap` is expected quiescence, and `expect_driver=wrap-ok` must not raise critical. GateDesign has no such input. `probe_watchdog` emits `WATCHDOG_ABSENT` whenever `pid_n=0`, and `WATCHDOG_STALE` whenever log mtime age > 900, including when the last line is a wrap.

**Live anchor (observation).**

| Fact | Command | At |
|---|---|---|
| no driver pid | `/usr/bin/pgrep -af shokunin-watchdog` → rc 1, empty (procps-ng 4.0.7). `/proc` cmdline scan for `shokunin-watchdog` → 0 hits | `2026-10-14T21:34:33-03:00` |
| log age 103842 s (> 900) | `stat -c %Y .ufo/watchdog.log` = `1791920688`; `date +%s` = `1792024473` | same |
| last line is a tick after wraps, not a crash | `tail -n 1 .ufo/watchdog.log` → `2026-09-28T23:55:00-03:00 tick=3` | same |
| wrap completed the roster | `grep -c ' NOT respawning (fleet-wrap)' .ufo/watchdog.log` → `22` | same |
| `.ufo/fleet-wrap` file is **absent now** | `ls .ufo/fleet-wrap` → `No such file or directory` | same |

The predicate keys off mtime and pid count. It never reads the wrap lines. The flag file is also gone, so a design that only checks `[ -f .ufo/fleet-wrap ]` still false-positives on this log.

**Not a false positive (do not “fix” by suppressing these ids).** Pid gone, log stale, **and** last line is `lane-dead-no-report` or `launch-fail` with no later `wrap`/`complete` is the mint case (daemon death). That must stay DRIFT.

**Fixture `fp-watchdog-wrap-quiescent`.** Expect today: exit 1, `FINDING WATCHDOG_ABSENT`, `FINDING WATCHDOG_STALE`. Expect after the smallest correction: exit 0, no those two ids (info `WATCHDOG_WRAPPED` is optional and must not flip DRIFT).

```text
$FX/proc/            # empty — ps/pgrep stub prints no watchdog pid
$FX/ufo/watchdog.log # mtime = MORI_NOW_EPOCH - 100000 (> 900)
```

Log body (the gate must read the last non-empty line, not only `stat`):

```text
2026-09-28T23:54:59-03:00 wrap protocol round=14 complete; NOT respawning (fleet-wrap)
2026-09-28T23:54:59-03:00 wrap aggregator round=10 complete; NOT respawning (fleet-wrap)
2026-09-28T23:55:00-03:00 tick=3
```

Pgrep stub: empty stdout, rc 1. No `fleet-wrap` file (matches this host).

**Smallest safe correction.** Before emitting `WATCHDOG_ABSENT` or `WATCHDOG_STALE`, if the last non-empty log line matches ` wrap ` or ` complete ` and every roster lane has a later-or-equal `wrap` line, record observation `quiescent=wrap` and do not flip DRIFT. Keep both ids when the last substantive line is `lane-dead-no-report` or `launch-fail`.

---

## FP-2 — A live driver with a quiet tick still ages the log file into `WATCHDOG_STALE`

**Legitimate state.** The driver appends one line per tick, then `sleep 450` (`INTERVAL=450` in `scripts/shokunin-watchdog.sh:10,114-115`). Between appends the log mtime is the **previous** tick. A healthy pid whose last tick is 901–1800 s old is between ticks or one missed tick, not wedged. GateDesign’s own header says “two driver ticks” (900 s) but `probe_watchdog` compares **file mtime** with `> 900` and does not require the pid to be dead. FindingIds separates `WATCHDOG_TICK_STALE` (pid alive, bound 2×INTERVAL) from absence. The script collapses both into `WATCHDOG_STALE` and stacks it on `WATCHDOG_ABSENT` (FP-1).

Boundary: age 900 must not fire (`-gt`). Age 901 must not fire either if the contract is “two full ticks”: the tick line is written **then** the process sleeps 450, so mtime age approaches 450 on a healthy tick and exceeds 900 only after a second missed wake.

**Fixture `fp-watchdog-alive-one-missed-tick`.** Pid alive, log age **901**.

```text
$FX/proc/4242/comm = watchdogd
$FX/ps.out         = "4242 00:20 /bin/bash scripts/shokunin-watchdog.sh"
$FX/ufo/watchdog.log   mtime = MORI_NOW_EPOCH - 901
  last line: "<iso> tick=4"
```

Expect today: exit 1, `FINDING WATCHDOG_STALE`. Expect after correction: exit 0. A paired true-positive fixture keeps age **1801** with pid alive → `WATCHDOG_STALE` (or FindingIds’ `WATCHDOG_TICK_STALE`) stays DRIFT.

**Smallest safe correction.** Stale bound for a **live** pid is `> 2 * INTERVAL` (1800), matching FindingIds §3.1. File mtime alone must not use the one-tick value 900.

---

## FP-3 — `pgrep -af` matches the census argv, so a dead driver looks alive — and the inverse filter is not in the script

**Legitimate state (two edges of one predicate).**

1. **False CLEAN (coverage hole, named so the false-positive fix does not overshoot).** Procps `pgrep -f` matches any cmdline containing the pattern and excludes only its own process. Measured: `bash -c '/usr/bin/pgrep -af shokunin-watchdog'` matched **that bash**, rc 0 (`pid 1872191`). A parent whose argv is the gate script text, or `bash -c` that embeds the pattern, makes `pid_n≥1`. `WATCHDOG_ABSENT` does not fire. A dead driver plus a self-match is reported healthy on the pid axis.
2. **False DRIFT if a later edit greps `-v pgrep` or `-v mori-census` too broadly.** GateDesign’s comment says “Filter the pgrep line itself” but the code does not filter. The inverse bug is real: `/bin/bash /tmp/mori-fp-shokunin-watchdog.*.sh` (a `sleep 3` script, not the driver) was matched by `/usr/bin/pgrep -af shokunin-watchdog` (pid `1873720`). Dropping every line that merely **contains** the pattern, or dropping every `bash` line, marks a real driver `WATCHDOG_ABSENT`.

Shell builtin `pgrep` on this host is not procps (`pgrep 0.2.0`, `-af` does not behave as procps). The gate must pin `/usr/bin/pgrep` or match `/proc/<pid>/cmdline` itself. Otherwise fixture and live disagree.

**Fixture `fp-pgrep-parent-argv`.** Dead driver, but the pgrep stub prints one line that is the census parent:

```text
42421 bash tools/mori-census.sh
```

No `proc/<pid>/cmdline` ending in `scripts/shokunin-watchdog.sh`. Log fresh (age 60) so only the pid axis is in play.

Expect today: `pid_n=1`, no `WATCHDOG_ABSENT` (false CLEAN). Expect after correction: `WATCHDOG_ABSENT` **does** fire (this case is a true positive the current predicate misses).

**Fixture `fp-pgrep-path-not-driver`.** Stub prints only:

```text
5151 /bin/bash /tmp/mori-fp-shokunin-watchdog.AAAA.sh
```

Expect today: no `WATCHDOG_ABSENT` (false alive). Expect after correction: `WATCHDOG_ABSENT` fires unless cmdline matches `(^|/)scripts/shokunin-watchdog\.sh( |$)`.

**Smallest safe correction.** Count a hit only when cmdline matches the driver path, not the substring `shokunin-watchdog`. Do not subtract lines by grepping out `pgrep` or `mori-census` from an already-correct path match.

---

## FP-4 — Closed train wave whose closeout is `closeout.md` is `WAVE_UNSETTLED_AGE`

**Legitimate state.** Later train waves close by writing `closeout.md` plus `registry.json`. GateDesign settles only on `results.json` OR `closeout.json` OR `mission-result.json`. It treats `run.json` / `dispatch.json` / `swarm-registry.json` as dispatched. `closeout.md` is invisible, so a closed wave stays “unsettled” and ages past 7200 s into DRIFT. SKILL.md: “wave registry present, no results — age it, do not call it failed.” A present closeout **is** the result payload; the extension changed, the state did not.

**Live anchor.**

| Wave | Gate sees | Newest age at measure | Legitimate? |
|---|---|---|---|
| `shokunin-train-20261101-w12` | `registry.json`, `closeout.md`, no `run.json`/`dispatch.json`/`swarm-registry.json` | `closeout.md` age **33755 s** | Closed. Header: “Wave-12 closeout … Closed 2026-10-14 ~15:15Z”. Gate **does not fire today** because the dispatch filenames moved too |
| `shokunin-train-20261101-w11` | `closeout.json` present | 36054 s | Closed; gate correctly settled (`settle=1`) |
| `shokunin-train-20261013` … `w5` | `swarm-registry.json` + `dispatch.json`, **no** closeout of any name | 95414 s down to 70557 s | **Not** this FP — absent closeout stays a real age finding |

w12 proves the **filename hole**. The false positive appears as soon as a wave has both the old dispatch name and a markdown closeout (the mixed shape already exists across w6–w11 vs w12–w18).

**Fixture `fp-wave-closeout-md`.**

```text
$FX/ufo/waves/wave-closed-md/swarm-registry.json   # "{}"
$FX/ufo/waves/wave-closed-md/dispatch.json         # "{}"
$FX/ufo/waves/wave-closed-md/closeout.md           # "# closeout\nClosed.\n"
```

All three mtimes = `MORI_NOW_EPOCH - 30000` (> 7200). No `results.json`, no `closeout.json`.

Expect today: exit 1, `FINDING WAVE_UNSETTLED_AGE` `wave=wave-closed-md`. Expect after correction: exit 0.

**Smallest safe correction.** Treat `closeout.md` as a settle file the same way as `closeout.json`. Do not drop the age rule for registry+dispatch with **no** closeout (w1–w5 must still fire).

---

## FP-5 — ufo-swarm `task-response.json` is the results payload; the gate does not count it

**Legitimate state.** 12h waves dispatch with `run.json` and finish with `task-response.json`. GateDesign’s own header lists `task-response.json` in the filename set (“Primary probes”) but `probe_waves` never reads it. Settlement is only `results.json|closeout.json|mission-result.json`. FindingIds §3.2: “12h/ufo-swarm waves: `run.json` + optional `results.json` + optional `task-response.json`.” FixtureDesign case 10 treats `task-response.json` as the results-class payload for `wave-settled-QUIET`.

**Live anchor.** `shokunin12h-20261014-p1-audit` has `run.json` + `task-response.json` and no `results.json` / `closeout.json` / `mission-result.json`. Newest age **284 s** at measure, so the 7200 s gate does not fire **yet**. The same tree at age 7201 s is DRIFT while the wave has a results payload. `p1-repair` has `mission-result.json` and is settled by accident of a second filename. `p4-mori-r1` (this wave) is the same shape, age ~59 s: an in-flight wave must **not** fire (FixtureDesign case 9); after it lands `task-response.json` and sits, it must not fire either.

**Fixture `fp-wave-task-response-aged`.**

```text
$FX/ufo/waves/wave-12h-done/run.json            mtime = NOW-8000
$FX/ufo/waves/wave-12h-done/spec.json           mtime = NOW-8000
$FX/ufo/waves/wave-12h-done/task-response.json  mtime = NOW-8000
  body: {"text":"ok","details":{}}
```

Expect today: exit 1, `WAVE_UNSETTLED_AGE`. Expect after correction: exit 0.

**Paired true positive (must still fire):** `fp-wave-run-only-aged` — `run.json` + `spec.json` only, age 8000, no `task-response.json`. That is `shokunin12h-20261014-p3-kengaku` (measured age **1121 s**, under the bound today). Aging that fixture past 7200 s **is** DRIFT. Do not treat “has `run.json`” as settled.

**Smallest safe correction.** Add `task-response.json` to the settle-file set. Keep age DRIFT when `run.json` exists and none of the settle files do.

---

## FP-6 — Newest-mtime age hides a stalled dispatch behind a late scratch file, then the inverse fires on a finished-but-untouched wave

**Legitimate state, calibration defect.** `probe_waves` sets age from the newest file anywhere under the wave dir. Two legitimate shapes:

1. **False CLEAN.** Dispatch is old; a later reader touches `x-sentinel.md`. Age looks young. `shokunin-train-20261013` newest file is `x-sentinel.md` at `2026-10-13 19:04`, not the registry. A one-byte touch would clear `WAVE_UNSETTLED_AGE` with no settlement.
2. **False DRIFT (this audit’s case).** Wave settled in the sense the operator stopped it, registry unchanged, no new file, age > 7200. The predicate cannot tell “abandoned” from “settled under a filename it does not know” (FP-4, FP-5). Using newest mtime means a **closed** wave that simply stops receiving writes becomes DRIFT even after FP-4’s extension if the closeout file is older than 7200 s and the predicate still requires a fresh mtime. Settlement must be filename presence, not recency. Recency is only for the unsettled arm.

**Fixture `fp-wave-settled-old-mtime`.** Same tree as FP-4 (with `closeout.md` recognized) but mtime age 30000. Expect exit 0. If the implementation “fixes” FP-4 by requiring closeout mtime `< 7200`, this fixture goes red — that fix is wrong.

**Fixture `fp-wave-scratch-touch-not-settle` (false-CLEAN guard).**

```text
wave-stale/swarm-registry.json  mtime = NOW-90000
wave-stale/dispatch.json        mtime = NOW-90000
wave-stale/x-sentinel.md        mtime = NOW-30
```

Expect: exit 1, `WAVE_UNSETTLED_AGE`, and the age payload must be computed from the dispatch/registry mtime (or `dispatched_at`), **not** from `x-sentinel.md`. Today the script uses newest-of-all and would CLEAN this fixture. That is the paired hole; fixing FP-4/FP-5 by “any new file resets age” widens it.

**Smallest safe correction.** Age the **dispatch** artifact (`dispatched_at` inside registry/run, else mtime of `dispatch.json`/`run.json`/`swarm-registry.json` only). Ignore later report/scratch mtimes. Settle-file presence clears the finding regardless of age.

---

## FP-7 — One user-scope terminal oom-kill sticks for the whole boot

**Legitimate state.** `journalctl --user -b` on this boot contains a single oom-class line, and it is not a fleet daemon:

```text
2026-10-13T23:44:31-03:00 plazir27 systemd[1573]: app-Hyprland-xdg\x2dterminal\x2dexec-dd9e67bd.scope: Failed with result 'oom-kill'.
```

Command: `journalctl --user -b --no-pager -o short-iso -g 'Out of memory|oom-kill|oom_reaper|Killed process'` → that one line, rc 0. Boot id `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`, userspace up since `2026-10-13 11:02:02` (`uptime -s`). The script counts any match (`c_oom>0`) and emits `OOM_KILL_JOURNAL` at `crit`, with no unit denylist and no fleet-path filter. FindingIds says emit the id either way but put `fleet_relevant=true|false` in the payload; the **gate weight** for a non-fleet unit is what GateDesign got wrong by always flipping DRIFT.

A Hyprland xdg-terminal scope dying is a desktop event. The fleet can be healthy for the rest of a multi-day boot (`-b` does not reset until reboot). Every later census repeats the same crit.

**Also a class-collision, not a second id:** the same line matches `Failed with result`, so `UNIT_FAILURE_JOURNAL` (`info`) fires beside `OOM_KILL_JOURNAL`. FindingIds §3.3: one physical line, one primary class. The info twin does not change the verdict; the crit does.

**Fixture `fp-journal-desktop-oom-not-fleet`.** Journal stub body, rc 0:

```text
Oct 13 23:44:31 fx systemd[1573]: app-Hyprland-xdg-terminal-exec.scope: Failed with result 'oom-kill'.
```

No other lines. Expect today: exit 1, `OOM_KILL_JOURNAL`. Expect after correction: exit 0, and if the line is still reported, `severity=info` (or payload `fleet_relevant=false`) so the rollup stays CLEAN.

**Paired true positive:** replace the unit with `kimi-webbridge.service` or a cmdline containing `ufo` / `shokunin-watchdog` → `OOM_KILL_JOURNAL` stays `crit`. That is the mint demand (undetected daemon OOM).

**Smallest safe correction.** DRIFT only when the matched unit/cgroup/cmdline contains a fleet marker (`shokunin`, `ufo`, `watchdog`, roster lane names) **or** an explicit `MORI_FLEET_UNITS` entry. Desktop scopes (`app-Hyprland-`, `xdg-terminal`) stay info. Do not drop the oom class itself.

---

## FP-8 — `Killed process` inside an oom line double-counts, and a non-kill “Killed process” string fires `OOM_KILL_JOURNAL`

**Legitimate state.** The oom regex is `Out of memory|oom-kill|oom_reaper|Killed process`. Kernel kill lines look like `Out of memory: Killed process 1732581 (python3) …` (system journal, this boot; **not** in the user journal — `journalctl --user -b -g 'Killed process'` → `-- No entries --`). On a host where that line is visible to the user journal, one event increments `c_oom` twice (two greps, not `grep -c` on unique lines — actually one `grep -ciE` counts **lines**, so a single line matching both alternatives counts once). Line count is fine. The false positive is the **bare alternative**: any line containing `Killed process` is classed oom-kill. A narrative line in a user unit (“Killed process tree on purpose during shutdown”) is a legitimate non-event.

`KILL_SIGNAL_JOURNAL` is the sharper false positive: regex `status=9/KILL|Failed with result .signal|SIGKILL`. `Failed with result .signal` matches `Failed with result 'signal'` **and** any `Failed with result Xsignal…`. A unit that fails with result `signal` because the user stopped it (`systemctl --user stop` → SIGTERM, often `status=15/TERM`, not always 9) is an intentional stop. The script has no SIGTERM id, but `status=9/KILL` on `app-Hyprland-*` or `pipewire` is the same desktop class as FP-7. This boot’s user journal had **zero** kill-signal lines (`c_kill=0`), so this one is structural, not a current live fire.

**Fixture `fp-journal-killed-process-narrative`.**

```text
Oct 14 01:00:00 fx my-backup.service[9]: Killed process lock removed, backup ok
```

Expect today: exit 1, `OOM_KILL_JOURNAL`. Expect after correction: exit 0 (no oom class). The true-positive line remains:

```text
Oct 14 01:00:00 fx kernel: Out of memory: Killed process 9 (kimi-webbridge)
```

**Fixture `fp-journal-user-stop-sigterm`.**

```text
Oct 14 01:00:00 fx systemd[1]: foo.service: Main process exited, code=killed, status=15/TERM
```

Expect today: exit 0 (pattern does not match 15/TERM — **keep it that way**). Guard only: do not “fix” kill detection by adding `status=15` or bare `signal`.

**Smallest safe correction.** Require oom class to match `oom-kill` OR `oom_reaper` OR `Out of memory:` (the kernel prefix), not bare `Killed process`. Keep `status=9/KILL` for `KILL_SIGNAL_JOURNAL`, but apply the FP-7 fleet-marker gate before it flips DRIFT.

---

## FP-9 — `oom_kill` is a sticky cgroup counter, and `max=max` means there is no current pressure

**Legitimate state.** `memory.events` `oom_kill` counts kills since the cgroup was created. It is not cleared when memory recovers. GateDesign comments “presence flag, not a meter to clear” and then treats `oom_kill>0` as **current** crit on every run.

**Live anchor.**

| Path | `oom_kill` | `oom` | `high` | `memory.current` | `memory.max` |
|---|---|---|---|---|---|
| `/sys/fs/cgroup/user.slice/user-1000.slice/memory.events` | **1** | 0 | 0 | `24600768512` (~22.9 GiB) | `max` (unlimited) |
| `/sys/fs/cgroup/user.slice/memory.events` | **1** | 0 | 0 | (parent) | — |

`/proc/meminfo`: `MemAvailable` **21371900 kB** / `MemTotal` **31721780 kB** (~67% available). `oom` and `high` are 0. The only descendant with `oom_kill>0` within depth 3 is the user slice itself, not a fleet service cgroup. Headroom is fine. The script still emits `CGROUP_OOM_KILL` crit because it never reads a baseline and never checks `memory.max`.

FindingIds §3.4: fire on **increase** vs census baseline, or absolute `>0` only for an explicit `baseline=boot-zero` profile. Default absolute-on-every-run makes the first kill a permanent DRIFT until reboot **of the cgroup**, which on a user slice means until logout/reboot — longer than the journal boot window.

**Fixture `fp-cgroup-sticky-oom-kill-headroom-ok`.**

```text
$FX/cgroup/memory.events:
  low 0
  high 0
  max 0
  oom 0
  oom_kill 1
$FX/cgroup/memory.current: 1000000000
$FX/cgroup/memory.max:     max
$FX/meminfo: MemTotal 32000000 kB / MemAvailable 21000000 kB
$FX/baseline/cgroup.oom_kill: 1
```

Expect today: exit 1, `CGROUP_OOM_KILL` (baseline file ignored). Expect after correction (default `delta-cgroup`): exit 0, because the counter did not increase and max is unlimited.

**Paired true positive `fp-cgroup-oom-kill-increased`:** baseline file contains `0`, events contain `oom_kill 1` → DRIFT stays.

**Smallest safe correction.** Default profile is delta: DRIFT only when `oom_kill` is greater than the last receipt’s value for that path. First run with no receipt may emit `info` `CGROUP_OOM_KILL_BASELINE` (not DRIFT) unless `MORI_CGROUP_PROFILE=boot-zero`. Unlimited `memory.max` (`max`) must not be treated as a ratio breach (the script already ignores ratio; do not add one that treats the word `max` as a number).

---

## FP-10 — `protocol` and `aggregator` share one git repo, so one quiet tree double-fires `LANE_SILENT`

**Legitimate state.** PROTOCOL.md:158-167: progressing = lane-authored commit **or** non-`.git` file newer than **launch**; sibling-authored commit alone = `progressing-weak` (not silent, not failed); commit sparsity is not silence. GateDesign `lane_repo` maps **both** `protocol` and `aggregator` to `$ROOT`. `probe_silence` does not read launch timestamps, report mtimes, or commit authors. It marks silent when `HEAD` time **and** newest non-`.git` mtime are both older than `NOW - 7200`.

Consequences:

1. One quiet shokunin checkout emits **two** `LANE_SILENT` rows (same HEAD, same files, two subjects).
2. A lane with no commit for days but a file touch in-window is `progressing` (script got this part right — keep it).
3. A lane whose only in-window commit is by `aggregator-shokunin` is graded `progressing` or, if files are old, `progressing-weak` — but `progressing-weak` does not DRIFT. The false DRIFT is the other direction: **no launch is open**. Grading every roster lane against a rolling 7200 s wall clock, rather than “mission open longer than two ticks since launch”, fires on a lane that is simply between rounds. Live roster at measure was all `progressing` (newest file ages 149–586 s; HEAD ages 142–194 s) because this 12h program is mid-write. That is not a counterexample to the predicate; it shows the predicate is dormant until the program pauses for two hours.

**Fixture `fp-silence-shared-root-idle-between-rounds`.** `MORI_ROSTER_LANES="protocol aggregator"`. Both repos are `$FX/root` (one `.git`). `git log -1 --format=%ct` stub returns `MORI_NOW_EPOCH-20000`. Newest non-`.git` file mtime = `NOW-20000`. No open mission file, no `launch` line inside the silence window.

Expect today: exit 1, **two** `FINDING LANE_SILENT` lines. Expect after correction: exit 0 (no open mission → not silence). If a mission file `$FX/ufo/state/protocol.mission` exists with launch epoch `NOW-8000` and no file/commit since, **one** `LANE_SILENT` for `protocol` only; `aggregator` must not inherit it unless its own mission is open.

**Fixture `fp-silence-sibling-author-not-silent` (must stay CLEAN).** HEAD in-window, author `aggregator-shokunin`, no file newer than window. PROTOCOL says `progressing-weak`, never DRIFT. Expect exit 0. The script already does this via the weak branch; a “fix” that treats weak as DRIFT is a new false positive.

**Smallest safe correction.** Silence requires an **open** mission whose launch epoch is older than two ticks (900 s, from the log `launch <lane>` line or `.ufo/state/<lane>.mission` mtime), **and** no lane-authored activity since launch. Do not grade `protocol` and `aggregator` off the same activity twice. Sibling author stays non-DRIFT.

---

## FP-11 — `/tmp` at the warn edge, and `df` on the fleet root reporting the whole disk, are not “fleet runway exhausted”

**Legitimate state.** Defaults: DRIFT at used% ≥ 85 (`DISK_LOW`) and ≥ 95 (`DISK_CRITICAL`) on **each** of `$ROOT` and `/tmp`. Measured `df -P` (`2026-10-14T21:34:33-03:00`):

| Target | Capacity | Available | Verdict under the script |
|---|---|---|---|
| fleet root (`.`, fs `/dev/mapper/root`) | **10%** | 875439056 KiB (~835 GiB) | CLEAN |
| `/tmp` tmpfs | **60%** | 6353668 KiB (~6.1 GiB) | CLEAN |
| `/scratch/tmp` | absent | — | not in default `MORI_DISK_TARGETS` (script defaults `ROOT` and `/tmp` only) |

So this host does not fire. The false positive is the **rule**, and FixtureDesign’s own case 26 makes it the contract: `/tmp` at 97% with fleet at 10% is `DISK_CRITICAL` for the whole census. tmpfs filling toward 85% is a legitimate short-lived compile/test spike (`/tmp` is 60% **right now** without being a fleet incident). It shares RAM with the memory the cgroup probe already watches; a tmpfs spike plus FP-9’s sticky `oom_kill` double-counts one desktop memory event as disk **and** cgroup DRIFT.

Second edge: `df -P "$ROOT"` reports the filesystem Capacity, not “bytes the fleet needs”. The fleet root sits on `/` (`10%`, same filesystem as `df -P /`). A legitimate large image or snapshot that pushes `/` to 85% while 15% of 974646272 KiB remains (~139 GiB) still fires `DISK_LOW`. FindingIds’ OR with `DISK_WARN_AVAIL_BYTES=5 GiB` would **not** fire; GateDesign dropped the byte floor and kept only percent. Percent-only on a ~1 TB disk is the false positive.

**Fixture `fp-disk-tmp-spike-fleet-ok`.**

```text
$FX/disk/fleet.df   Capacity 10%   Available large
$FX/disk/tmp.df     Capacity 90%   Available 2000000   # ~2 GiB still free on tmpfs
MORI_DISK_TARGETS="$FX/root /fx/tmp"
```

Expect today: exit 1, `DISK_LOW` (90 ≥ 85). Expect after correction: exit 0 when **available bytes** on that target stay above the floor (proposal 5 GiB for fleet, and tmpfs must not use the fleet percent — or tmpfs warn is info unless available < 1 GiB).

**Fixture `fp-disk-percent-high-bytes-ok`.** Fleet row `96%` used but Available corresponding to **50 GiB** on a huge device (percent would be `DISK_CRITICAL` today). Expect after correction: not crit if available bytes ≥ crit floor. A **true** positive remains: Available `0` or below 1 GiB → `DISK_CRITICAL`.

**Smallest safe correction.** Fire `DISK_LOW` / `DISK_CRITICAL` on available-bytes floor **or** (percent **and** a small-disk guard), not percent alone. Do not let `/tmp` alone raise `crit` while the fleet filesystem is under the byte floor. Keep `DISK_UNAVAILABLE` as info when `/scratch/tmp` is absent (already true if it is not a default target — do not add it as a hard target).

---

## FP-12 — Selftest `WATCHDOG_STALE` is itself a false-positive fixture

**Legitimate state used as a DRIFT pin.** GateDesign’s selftest case `drift: WATCHDOG_STALE` sets `MORI_WATCHDOG_STALE_S=0` on the **clean** tree (log age 60 s, pid alive). Any positive age fires. That case teaches the gate that “log exists and is younger than one tick” is DRIFT whenever the operator sets the threshold to 0, and it never builds the wrap-quiescent or alive-between-ticks trees. FixtureDesign case 3 (`watchdog-stale-log-FIRE`, age 7200, threshold 3600) conflicts with GateDesign’s 900 s default; a parent that implements **both** will call a 3601 s **healthy** gap DRIFT under FindingIds (bound 900 only when the pid is dead and the line is not wrap) and also DRIFT under FixtureDesign’s 3600 s `WATCHDOG_STALE_LOG`.

**Fixture to add, not to bless:** `fp-selftest-threshold-zero-is-setup`. `MORI_WATCHDOG_STALE_S=0` must be exit **2** (setup) or ignored, not a green selftest of the stale predicate. The stale FIRE case must be the FP-2 true-positive (pid alive, age > 1800) or FP-1’s negative (wrap line, any age, CLEAN).

**Smallest safe correction.** Delete threshold `0` as a positive test. One FIRE fixture per id, with the legitimate neighbour asserted CLEAN in the same selftest.

---

## What is not a false positive (so a fix does not erase it)

| Live or designed state | Why it stays DRIFT | Measured |
|---|---|---|
| Train waves `shokunin-train-20261013` … `w5`: registry + dispatch, no results, no closeout, age 70557–95414 s | Unsettled past the bound. Age them; do not call them failed (SKILL). The **id** is still warranted | `find` mtimes via the wave walk at `2026-10-14T21:36Z` |
| `p3-kengaku`: `run.json` + `spec.json` only, age 1121 s | Under 7200 s today so the script is CLEAN; **past 7200 s without `task-response.json` it must fire** | `stat` on `run.json` → `2026-10-14 21:16:36 -0300` |
| Kernel line `Out of memory: Killed process … (python3)` in the **system** journal | Real kill, but `--user` does not show it (`Killed process` user-journal count 0). If a future probe adds system journal, fleet-marker gate (FP-7) still applies; python3 OOM is not automatically a fleet DRIFT | `journalctl -b -g 'Out of memory'` vs `--user` |
| `pipewire-pulse.service: Failed with result 'core-dump'` | `SEGFAULT`/`UNIT_FAILURE` are `info` in GateDesign — already non-DRIFT. Do not promote them | user journal `2026-10-14T18:54:21-03:00` |
| Absent `/scratch/tmp` | `unavailable`, and not a default target. Must stay non-DRIFT | `df` → `No such file or directory` |
| Sticky `oom_kill=1` **with an increase vs baseline**, or a fleet-unit oom line | True positive under the delta / fleet-marker rule | counter is 1; baseline file does not exist yet |

---

## Fixture index (add these; do not replace the true-positive FIRE cases)

| # | Fixture id | Legitimate state | Id that fires today | Exit today | Exit after correction |
|---|---|---|---|---|---|
| FP-1 | `fp-watchdog-wrap-quiescent` | full wrap, no pid, old log, no `fleet-wrap` file | `WATCHDOG_ABSENT`, `WATCHDOG_STALE` | 1 | 0 |
| FP-2 | `fp-watchdog-alive-one-missed-tick` | pid alive, log age 901 | `WATCHDOG_STALE` | 1 | 0 |
| FP-3 | `fp-pgrep-parent-argv` | only match is the census parent argv | (false CLEAN — no `WATCHDOG_ABSENT`) | 0 | 1 |
| FP-3b | `fp-pgrep-path-not-driver` | unrelated script path contains the substring | (false CLEAN) | 0 | 1 |
| FP-4 | `fp-wave-closeout-md` | `closeout.md` + registry + dispatch, age 30000 | `WAVE_UNSETTLED_AGE` | 1 | 0 |
| FP-5 | `fp-wave-task-response-aged` | `run.json` + `task-response.json`, age 8000 | `WAVE_UNSETTLED_AGE` | 1 | 0 |
| FP-6 | `fp-wave-scratch-touch-not-settle` | old dispatch, fresh `x-sentinel.md` | (false CLEAN) | 0 | 1 |
| FP-6b | `fp-wave-settled-old-mtime` | closeout present, mtime old | `WAVE_UNSETTLED_AGE` if closeout unrecognized or recency required | 1 | 0 |
| FP-7 | `fp-journal-desktop-oom-not-fleet` | Hyprland scope `oom-kill` only | `OOM_KILL_JOURNAL` | 1 | 0 |
| FP-8 | `fp-journal-killed-process-narrative` | line contains `Killed process` but is not an oom | `OOM_KILL_JOURNAL` | 1 | 0 |
| FP-9 | `fp-cgroup-sticky-oom-kill-headroom-ok` | `oom_kill` unchanged, `memory.max=max`, MemAvailable high | `CGROUP_OOM_KILL` | 1 | 0 |
| FP-10 | `fp-silence-shared-root-idle-between-rounds` | protocol+aggregator, one quiet repo, no open mission | `LANE_SILENT` ×2 | 1 | 0 |
| FP-11 | `fp-disk-tmp-spike-fleet-ok` | fleet 10%, tmpfs 90% with GiB free | `DISK_LOW` | 1 | 0 |
| FP-12 | `fp-selftest-threshold-zero-is-setup` | `MORI_WATCHDOG_STALE_S=0` on a fresh log | `WATCHDOG_STALE` | 1 | 2 |

---

## Smallest safe correction (one list for the parent)

1. **Watchdog.** Path-match the driver cmdline. Suppress `WATCHDOG_ABSENT` and `WATCHDOG_STALE` when the log’s last substantive lines are a full-roster `wrap`. Live-pid stale bound is `> 1800`, not `> 900`.
2. **Waves.** Settle files include `closeout.md` and `task-response.json`. Age is taken from the dispatch artifact, not the newest scratch file. Young `run.json` without a settle file stays non-DRIFT (FixtureDesign case 9).
3. **Journal.** `OOM_KILL_JOURNAL` / `KILL_SIGNAL_JOURNAL` flip DRIFT only with a fleet marker. Desktop `oom-kill` and bare `Killed process` stay info. Do not add SIGTERM.
4. **Cgroup.** Default delta vs last receipt. Absolute `oom_kill>0` is opt-in `boot-zero`, not every run. `memory.max=max` is unlimited, not a ratio.
5. **Silence.** Only an open mission older than two ticks, missing lane-authored activity. `protocol` and `aggregator` are not one double finding. `progressing-weak` stays non-DRIFT.
6. **Disk.** Byte floor, not percent alone; `/tmp` percent must not crit the fleet census by itself.
7. **Selftest.** Add the FP table above next to the existing FIRE cases. Remove `MORI_WATCHDOG_STALE_S=0` as a success-path DRIFT test.

No id needs to be deleted. The defect is the predicate weight, not the vocabulary.

---

## Limits

- GateDesign.md is a script inside a member report. It is not on disk as `mori-shokunin/tools/mori-census.sh`. Predicates were read from that report (§5, `probe_watchdog` through `probe_silence`), not executed as a live census. No `MORI_CENSUS:` line was produced.
- FindingIds.md and FixtureDesign.md were read as competing contracts. They are not implemented by the script (different id spellings: `WATCHDOG_STALE` vs `WATCHDOG_TICK_STALE` / `WATCHDOG_STALE_LOG`; `OOM_KILL_JOURNAL` vs `OOM_KILL_EVENT`).
- Journal and cgroup values are this boot’s user slice only. System-journal kernel OOM was counted as a contrast, not fed to the gate.
- No process was restarted, killed, or reparented. No file under the host was modified except this report.
