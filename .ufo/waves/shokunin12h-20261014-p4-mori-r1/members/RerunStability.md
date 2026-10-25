# RerunStability — live census receipt is not byte-stable; compare key is

**Seat:** `RerunStability` (leaf). Advisory data, not a judge verdict, not a remediation.
**Lane:** `mori-shokunin` · gate `tools/mori-census.sh` · version string `census-r1`
**Measured:** `2026-10-15T00:37:44Z`–`2026-10-15T00:37:59Z`
**Script:** blob `43a2f5f84e1f254706cea7ebde5d81e78e19797d` = `HEAD:tools/mori-census.sh` at `72da7cd2edc4127d5ac6d7dea6219f15e59acc53` (worktree clean for that path). SHA-256 `7432255ff56dc69f0f2814e631961a0482e51d52f392f547de5dac42df387d3f` (31588 bytes).
**Host writes by this seat:** none except this file. Invocations were `bash tools/mori-census.sh` (live; script stderr empty) plus read-only `df`/`stat`/`find`/`git` for the margins below. No `--selftest` (that path writes under `/tmp`).

## Claim

The live receipt is **not** byte-identical across two runs on the same host minute. After the normalization below, the four receipts **are** identical, including a pair whose clock was pinned.

What is stable without stripping: exit code, `MORI_CENSUS:` verdict line, surface states, finding ids, severities, and subject keys. What moves, and how a later compare must treat it, is the rest of this note.

## Runs

| run | clock | exit | duration | bytes | stderr |
|---|---|---|---|---|---|
| A | live `date +%s` → `ts=2026-10-15T00:37:44Z` | 1 | 3.649s | 2579 | empty |
| B | live → `ts=2026-10-15T00:37:48Z` | 1 | 3.677s | 2579 | empty |
| C | `MORI_NOW_EPOCH=1792024671` → `ts=2026-10-15T00:37:51Z` | 1 | 3.639s | — | empty (not re-printed; stdout only differed from D on `current=`) |
| D | same pin `1792024671` | 1 | 3.711s | — | same |

`BYTE_IDENTICAL(A,B)=false`. `BYTE_IDENTICAL(C,D)=false`. Stripping `ts=`, `age_s=`, `mtime_age_s=`, and `current=` makes A=B=C=D.

Verdict line, all four, byte-identical:

```text
MORI_CENSUS: DRIFT (findings=10 drift=9 unavailable=0 surfaces=7)
```

Exit 1 is the gate's DRIFT code, not a probe failure. `rc=0` on the journal surface both live runs.

## Live pair (verbatim)

A:

```text
mori-census census-r1 — ts=2026-10-15T00:37:44Z — mode=live — read-only
SURFACE watchdog: drift (cmd=pgrep -af shokunin-watchdog; stat /home/vgpnk/Projects/shokunin/.ufo/watchdog.log; ls /home/vgpnk/Projects/shokunin/.ufo/state; pids=0; log=ok; age_s=103976; stale_threshold_s=900; state_rounds=9; ts=2026-10-15T00:37:44Z)
SURFACE waves: drift (cmd=find /home/vgpnk/Projects/shokunin/.ufo/waves -maxdepth 1 -mindepth 1 -type d; total=33 settled=7 unsettled=10 aged_unsettled=5 empty=16 threshold_s=7200; ts=2026-10-15T00:37:44Z)
SURFACE journal: drift (cmd=journalctl --user -b --no-pager; oom_kill=1 kill_signal=0 segfault=0 unit_failure=2 rc=0; ts=2026-10-15T00:37:44Z)
SURFACE cgroup: drift (cmd=cat /sys/fs/cgroup/user.slice/user-1000.slice/memory.events; cat /sys/fs/cgroup/user.slice/user-1000.slice/memory.current; oom_kill=1 oom=0 high=0 max=0 current=25967091712; ts=2026-10-15T00:37:44Z)
SURFACE disk: ok (cmd=df -P; targets=/home/vgpnk/Projects/shokunin /tmp; warn_pct=85 crit_pct=95; ts=2026-10-15T00:37:44Z)
SURFACE silence: ok (cmd=git -C <repo> log -1 --format=%ct; find <repo> -newermt @window; silent=0 progressing=9 progressing_weak=0 skipped=0 window_s=7200; ts=2026-10-15T00:37:44Z)
SURFACE tmux: ok (cmd=tmux ls; sessions=1; ts=2026-10-15T00:37:44Z)
FINDING WATCHDOG_STALE severity=warn obs=watchdog.log mtime_age_s=103976 threshold_s=900 path=/home/vgpnk/Projects/shokunin/.ufo/watchdog.log
FINDING WATCHDOG_ABSENT severity=warn obs=no shokunin-watchdog process matched by pgrep -af
FINDING WAVE_UNSETTLED_AGE severity=warn obs=wave=shokunin-train-20261013 age_s=95591 threshold_s=7200 reg=1 disp=1 run=0 settle=0
FINDING WAVE_UNSETTLED_AGE severity=warn obs=wave=shokunin-train-20261013-w2 age_s=89812 threshold_s=7200 reg=1 disp=1 run=0 settle=0
FINDING WAVE_UNSETTLED_AGE severity=warn obs=wave=shokunin-train-20261013-w3 age_s=84642 threshold_s=7200 reg=1 disp=1 run=0 settle=0
FINDING WAVE_UNSETTLED_AGE severity=warn obs=wave=shokunin-train-20261013-w4 age_s=81780 threshold_s=7200 reg=1 disp=1 run=0 settle=0
FINDING WAVE_UNSETTLED_AGE severity=warn obs=wave=shokunin-train-20261013-w5 age_s=70734 threshold_s=7200 reg=1 disp=1 run=0 settle=0
FINDING OOM_KILL_JOURNAL severity=crit obs=class=oom_kill count=1 boot=current scope=user
FINDING UNIT_FAILURE_JOURNAL severity=info obs=class=unit_failure count=2 boot=current scope=user
FINDING CGROUP_OOM_KILL severity=crit obs=oom_kill=1 oom=0 high=0 max=0 current=25967091712 path=/sys/fs/cgroup/user.slice/user-1000.slice/memory.events
MORI_CENSUS: DRIFT (findings=10 drift=9 unavailable=0 surfaces=7)
```

B differs from A in exactly these substitutions (every other character matches):

| field | A | B | delta |
|---|---|---|---|
| `ts=` (banner + 7 surface lines) | `2026-10-15T00:37:44Z` | `2026-10-15T00:37:48Z` | +4s |
| watchdog `age_s` and `mtime_age_s` | 103976 | 103980 | +4 |
| wave `age_s` (5 findings, same order) | 95591, 89812, 84642, 81780, 70734 | 95595, 89816, 84646, 81784, 70738 | +4 each |
| `current=` (surface + `CGROUP_OOM_KILL`) | 25967091712 | 26013732864 | +46641152 bytes |

Age delta equals the clock delta on every age field. That is clock, not mtime movement. Cross-check: `stat -c %Y` on `.ufo/watchdog.log` = `1791920688`; `1791920688 + 103976 = 1792024664`, which is `2026-10-15T00:37:44Z`. `age_s` is integer subtraction (`NOW_EPOCH - stat %Y`, and for waves `cut -d. -f1` on `%T@`), not a noisy sample.

## Pinned pair — residual is only `current=`

`MORI_NOW_EPOCH` is the gate's clock pin (`tools/mori-census.sh` header: "pin now (selftest)"; lines 88–90). With the same pin, C and D matched on every `ts=` and every `age_s`/`mtime_age_s`. The only differing lines:

```text
C SURFACE cgroup: ... current=25970823168; ts=2026-10-15T00:37:51Z
D SURFACE cgroup: ... current=25969070080; ts=2026-10-15T00:37:51Z
C FINDING CGROUP_OOM_KILL ... current=25970823168 path=.../memory.events
D FINDING CGROUP_OOM_KILL ... current=25969070080 path=.../memory.events
```

Delta D−C = **−1753088** bytes. Within a run the surface value and the finding value match, because `cur` is read once and reused (lines 338 and 343–347), not because memory was still.

## Volatile fields and the normalization that actually exists

The gate has **no** `payload_norm` and no compare mode. It prints raw magnitudes. A sibling note (`members/FindingIds.md`) proposes dropping `pid` / `available_bytes_raw` / `measured_at` / `cursor`; that proposal is not what this binary does. Normalization below is what the script implements, plus the strip a comparer must add.

| field | emitted where | moved this pair? | normalization |
|---|---|---|---|
| `ts=` | banner; every `SURFACE` line | yes (+4s live) | **Pin** `MORI_NOW_EPOCH`. Default live does not strip it. Compare key must ignore it; it is the observation stamp the contract requires, not identity. |
| `age_s`, `mtime_age_s` | watchdog surface, `WATCHDOG_STALE`, `WAVE_UNSETTLED_AGE` | yes, exactly +elapsed | **Same pin.** Not binned. Predicate is `age > threshold`; payload keeps raw seconds. |
| `current=` | cgroup surface and `CGROUP_OOM_KILL` | yes, even pinned (−1753088) | **Not normalized.** Identity is `oom_kill`/`oom`/`high`/`max` (stable at 1/0/0/0). Drop `current=` from the compare key. Do not bin unless a later gate adds a bin; this one has none. |
| pid list | not emitted | no (`pids=0`) | **Reduced to a count.** `pgrep` self-line filtered (`grep -vF pgrep`). |
| journal line text | not emitted | no (counts 1/0/0/2) | **Reduced to class counts.** |
| tmux session names | not emitted | no (`sessions=1`) | **Reduced to a count.** |
| disk `size`/`used`/`avail` | omitted on the ok surface | not in the receipt | **Omitted unless** `DISK_LOW` / `DISK_CRITICAL` fires; those findings would carry raw bytes and integer `used_pct`, unbinned. |
| silence `head_epoch` / `newest_epoch` | omitted unless `LANE_SILENT` | not in the receipt | **Omitted on the ok path.** |
| finding order | emission order | matched | **Not sorted.** Wave findings follow bash glob order (`LANG=en_US.UTF-8`, `LC_ALL` unset). Compare should sort by `(id, subject)` before a text diff. Not required to explain this pair. |

Finding identity that matched on all four runs, in emission order:

| id | sev | subject |
|---|---|---|
| `WATCHDOG_STALE` | warn | `path=…/watchdog.log` |
| `WATCHDOG_ABSENT` | warn | no process (no pid payload) |
| `WAVE_UNSETTLED_AGE` ×5 | warn | `wave=` the five `shokunin-train-20261013*` dirs above |
| `OOM_KILL_JOURNAL` | crit | `boot=current` `count=1` |
| `UNIT_FAILURE_JOURNAL` | info | `boot=current` `count=2` (does not increment `drift=`) |
| `CGROUP_OOM_KILL` | crit | `oom_kill=1` on `user-1000.slice` |

`findings=10` = 9 warn/crit + 1 info. That split was stable.

## Latent movers that did not fire

These are state changes the formatter will print if they happen. They are not formatter noise, and they did not happen in this window.

- **Threshold flicker.** Watchdog age 103976 vs bound 900 (margin ~103076s). Youngest aged wave 70734 vs 7200 (margin 63534s). A rerun seconds later cannot clear those findings unless an mtime in that directory is updated. None of those five newest-mtimes moved between A and B (age delta was exactly the clock delta).
- **Disk percent.** Ok surface has no byte fields, so `df` jitter cannot change it until integer Capacity crosses 85 (warn) or 95 (crit). Side sample, not a census field: fleet fs **10%** (`/dev/mapper/root`), `/tmp` **61%** (`df -P` during this write-up). Neither is adjacent to 85.
- **Silence grade.** Counts stayed `silent=0 progressing=9 progressing_weak=0 skipped=0` across four runs. Side measurement after the runs (same rule as the gate: newest non-`.git` file epoch vs `now-7200`): every roster lane margin was **6780–7199s**, so none was near a flip. `protocol` and `aggregator` both map to the fleet root, so member-report writes under `.ufo/waves/` refresh them; that keeps them `progressing`, it does not oscillate the count while the wave is being written.
- **Journal / tmux / pid / wave counters.** Stable this pair. A new journal line, a tmux session, a watchdog pid, or a new/removed wave dir would change the receipt. That would be a new observation, not a nondeterministic field.

## Observation / inference / unknown

- **Observation.** A≠B. Differences are only `ts`, ages (+4 each), and `current` (+46641152). C≠D only in `current` (−1753088) under a shared `MORI_NOW_EPOCH`. Verdict line and finding keys identical. Script stderr empty.
- **Inference.** A comparer that pins or strips clock fields and drops `current=` will not report false drift from a rerun on this host state. The gate does not do that strip itself.
- **Unknown.** Not measured: a second locale's glob order (these wave names are ASCII; order matched under `en_US.UTF-8` only); journal growth over a gap longer than ~15s; `df` byte movement between A and B (not emitted, so not in the diff).

## Honesty nits (do not treat as volatility)

- Silence `cmd=` is a fixed label (`find <repo> -newermt @window`). The probe that ran is `find -printf '%T@'` plus `git log -1 --format=%ct` (lines 417 vs 430–436). The label did not vary between runs. It is not a copy of argv.
- `progressing-weak` is not produced when any non-`.git` file is inside the window (lines 447–448). This receipt's `progressing_weak=0` is that rule, not a sampled author check.

## Re-run

```text
bash tools/mori-census.sh
MORI_NOW_EPOCH=$(date +%s) bash tools/mori-census.sh
```

Compare after removing `ts=…Z`, `age_s=<digits>`, `mtime_age_s=<digits>`, and `current=<digits>`. Do not expect raw stdout to match. Do not treat exit 1 as a failed rerun while the verdict line is `DRIFT`.
