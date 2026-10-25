# MemoryPressureReading — host memory runway (point reading)

**Lane:** mori-shokunin. Detect and report only. No remediation, no dispatch, no unit/package claim.
**Role:** advisory member data. Not a judge verdict and not `MORI_CENSUS: CLEAN|DRIFT`.
**Item:** `mori/MemoryPressureReading`
**reading_class:** `healthy`
**clean_label:** `MEM_HEADROOM_OK` (catalog non-finding; not a DRIFT id)
**findings_fired:** none (`MEM_HEADROOM_LOW` false; `MEM_PRESSURE_UNAVAILABLE` false; `CGROUP_MEM_CURRENT_UNAVAILABLE` false)
**compare_subject:** `scope=host;cgroup=/sys/fs/cgroup/user.slice`
**boot_id:** `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`

## 0. Receipt

```
reading_id: MEM_PRESSURE_HOST
reading_class: healthy
measured_at_utc: 2026-10-15T00:33:26.132840Z
window_end_utc: 2026-10-15T00:33:31.133867Z
mem_available_kib: 20878456
mem_total_kib: 31721780
mem_available_pct_x1000: 65817
pswpin_pages: 76930329
pswpout_pages: 100847043
pswpin_delta_pages: 0
pswpout_delta_pages: 0
swap_rate_window_s_x1000000: 5000080
user_slice_memory_current_bytes: 25019912192
user_slice_memory_max: max
user_slice_memory_max_bytes: null
predicates: H1=false H2=not-applicable
```

`mem_available_pct_x1000` is `floor(MemAvailable * 100000 / MemTotal)` so a later run can compare without float drift. Volatile raw bytes stay payload; the class is the compare field.

## 1. Class rule

One class for this reading. A missing required surface is `unavailable`, never `unhealthy` and never `low-headroom`.

| class | when |
|---|---|
| `unavailable` | any required surface cannot be read |
| `low-headroom` | every required surface read, and H1 or H2 is true |
| `healthy` | every required surface read, H1 false, H2 false or not applicable |

Required surfaces (all read in the window below):

| surface | path | result |
|---|---|---|
| MemAvailable (+ MemTotal, needed for the ratio) | `/proc/meminfo` | read |
| swap in/out counters | `/proc/vmstat` `pswpin`, `pswpout` | read, including a 5.000080 s delta |
| user-slice current | `/sys/fs/cgroup/user.slice/memory.current` | read |
| user-slice max | `/sys/fs/cgroup/user.slice/memory.max` | read; token `max` |

`user.slice` is the user slice. Its only `user-*` child is `user-1000.slice` (uid 1000). That child is reported so the name is not ambiguous; the assigned comparator is `user.slice`.

### Thresholds used, and why

**H1 — host MemAvailable.** `low-headroom` if `MemAvailable * 100 / MemTotal < 10`.

Why 10, not the FindingIds proposal of 15:

- `/etc/systemd/oomd.conf` `[OOM]` contains only commented compile-time defaults: `SwapUsedLimit=90%`, `DefaultMemoryPressureLimit=60%`, `DefaultMemoryPressureDurationSec=30s`. No drop-in dirs exist (`/etc/systemd/oomd.conf.d`, `/run/systemd/oomd.conf`, `/run/systemd/oomd.conf.d`, `/usr/lib/systemd/oomd.conf`, `/usr/lib/systemd/oomd.conf.d` all absent). `systemd-analyze cat-config systemd/oomd.conf` at `2026-10-15T00:30:41Z` printed that same file and nothing else.
- `oomd.conf(5)` on this host (systemd 261.2): `SwapUsedLimit=` acts when **both** the fraction of memory used and the fraction of swap used exceed the limit. Default 90%.
- `/usr/lib/systemd/systemd-oomd` strings, adjacent to `/proc/meminfo`, name `MemTotal:`, `MemAvailable:`, `SwapTotal:`, `SwapFree:`, plus the check `MemAvailable (%lu) cannot be greater than MemTotal (%lu)`. This was not an exhaustive string inventory. **Inference (high, not a local source comment):** memory-used fraction is `(MemTotal - MemAvailable) / MemTotal`, because those are the memory fields the binary was observed to name and it rejects MemAvailable above MemTotal. The complement of the 90% used line is MemAvailable below 10% of MemTotal. If that inference is wrong, the 10% line needs revision; the raw percentage does not.
- 15% / 5% in `members/FindingIds.md` are marked proposal and have no local source. A 15% warn would call low-headroom while the host policy's memory predicate is still false. Id string `MEM_HEADROOM_LOW` stays; this report revises the numeric bound to 10. `MEM_HEADROOM_CRITICAL` at 5% is not adopted: no local authority sets 5%. The sourced stronger line is the oomd conjunction (memory-used and swap-used both ≥ 90%), and that conjunction is not this reading's class.

**H2 — user-slice ceiling.** If `memory.max` is a positive integer byte count, `low-headroom` if `memory.current * 100 / memory.max >= 90`. Same 90% figure, applied to the ceiling this item asks to compare. `memory.high` is recorded but is not a second threshold: on this host it is also `max`, so there is no configured throttle.

Token `max` is **not** an unknown max. It is a successful read of "no byte ceiling" (same fact as `systemctl show user.slice -p MemoryMax` → `infinity` at `2026-10-15T00:30:41Z`). H2 is then not applicable, which is not `unavailable` and not `low-headroom`. Unreadable `memory.max` would be `unavailable`. This rejects the FindingIds clause "unknown max → unavailable" for the literal token `max`. Unknown and unlimited are different observations.

**Swap in/out — measured, not a class threshold.** No host policy in `oomd.conf(5)` sets a swap-rate limit. Documented swap predicates are occupancy percents (`SwapUsedLimit`, ruleset `SwapUsageMax`), which are not in/out. `pswpin`/`pswpout` are cumulative since boot; a large total is history. A non-zero short-window rate would be recorded as activity and would still not, alone, set `low-headroom`: `vm.swappiness = 60` (`sysctl vm.swappiness` at `2026-10-15T00:30:41Z`) means the kernel swaps under ordinary reclaim. Stall and runway are H1 plus the PSI context below, not the lifetime page counters.

**Not class drivers** (reported so a later gate does not invent them): PSI, swap occupancy, zram fill, `memory.current / MemTotal`, kswapd scan/steal, `memory.events` `oom_kill`. See §4.

## 2. Observations

Probe: one read-only Python process opened the paths below, slept 5 s, and read the counters again. No write, restart, kill, or fetch. `proc(5)` is not installed on this host (`man -w proc` → no manual entry); MemAvailable is used as the kernel field `/proc/meminfo` exports, not as a quoted man sentence.

### 2.1 MemAvailable

Command-equivalent: read `/proc/meminfo`. Timestamp `2026-10-15T00:33:26.132840Z` (t0). Repeat at `2026-10-15T00:33:31.133127Z` (t1) after 5.000080 s.

| field | t0 | t1 |
|---|---:|---:|
| MemTotal kB | 31721780 | 31721780 |
| MemAvailable kB | 20878456 | 20844356 |
| MemFree kB | 631948 | 691396 |
| SwapTotal kB | 35917176 | 35917176 |
| SwapFree kB | 26085676 | 26085676 |

H1 input is the t0 pair. t1 is the same window as the swap delta, not a second class.

### 2.2 Swap in/out

Command-equivalent: read `/proc/vmstat` fields `pswpin` and `pswpout`. Page size `os.sysconf('SC_PAGE_SIZE')` = 4096. Uptime at t0: `/proc/uptime` first field `124527.25` seconds. Boot id above.

| counter | t0 pages | t1 pages | delta pages | delta bytes |
|---|---:|---:|---:|---:|
| pswpin | 76930329 | 76930329 | 0 | 0 |
| pswpout | 100847043 | 100847043 | 0 | 0 |

Short-window rate over 5.000080 s: **0 bytes/s in, 0 bytes/s out.**

Same file, not used as in/out: `pgscan_kswapd` 718600310 → 718625294 (delta 24984 pages); `pgsteal_kswapd` 623967707 → 623991844 (delta 24137 pages); `pgscan_direct` and `pgsteal_direct` unchanged; `oom_kill` 1 → 1. That is kswapd reclaim during the window, not swap in/out.

### 2.3 user.slice `memory.current` / `memory.max`

Read after t1, before `2026-10-15T00:33:31.133867Z`.

`/sys/fs/cgroup/user.slice`:

| file | value |
|---|---|
| memory.current | 25019912192 |
| memory.max | `max` |
| memory.high | `max` |
| memory.low | 0 |
| memory.min | 0 |
| memory.swap.current | 10033684480 |
| memory.swap.max | `max` |
| memory.events | low 0, high 0, max 0, oom 0, oom_kill 1, oom_group_kill 0, sock_throttled 77943 |
| memory.events.local | all listed counters 0, including oom_kill 0 |
| memory.pressure | some avg10/60/300 = 0.00; full avg10/60/300 = 0.00 |
| cgroup.controllers | includes `memory` |

Selected `memory.stat` (bytes): anon 5215580160, file 17688850432, kernel 2041995264, shmem 1594843136, swapcached 228360192. Cgroup-local cumulative `pswpin` 76905719, `pswpout` 100823016 (not the host `/proc/vmstat` counters; do not mix them).

`/sys/fs/cgroup/user.slice/user-1000.slice` (not the assigned comparator; coverage so the slice name is exact):

| file | value |
|---|---|
| memory.current | 25012457472 |
| memory.max | `max` |
| memory.high | `max` |
| memory.swap.current | 10033684480 |
| memory.events oom_kill | 1 |
| memory.events.local oom_kill | 0 |
| memory.pressure | some and full avg10/60/300 = 0.00 |

Directory listing of `/sys/fs/cgroup/user.slice`: the only `user-*` child is `user-1000.slice`. Difference `user.slice` current minus `user-1000.slice` current = 7454720 bytes.

Host PSI, same process, t0, `/proc/pressure/memory`: some avg10/60/300 = 0.00 total=80287565; full avg10/60/300 = 0.00 total=78204772. Totals are microseconds.

### 2.4 Swap composition (not in/out)

Follow-up, immediately after the snapshot process: `swapon --show --bytes`. Sum of USED equals `(SwapTotal - SwapFree) * 1024` from t0 (10067456000), so the device table did not move relative to that meminfo pair.

| name | type | size bytes | used bytes | prio |
|---|---|---:|---:|---:|
| /swap/swapfile | file | 32484225024 | 5773864960 | 0 |
| /dev/zram0 | partition | 4294963200 | 4293591040 | 100 |

`/sys/block/zram0/disksize` = 4294967296. That is 4096 bytes above the swapon size; swapon size is the one matched to meminfo. `stat -c %s /swap/swapfile` = 32484229120, also one page above the swapon size. Use the swapon table for used/size.

## 3. Derived (not raw observations)

Arithmetic on §2 only.

| quantity | value | formula |
|---|---|---|
| MemAvailable / MemTotal at t0 | 65.817416% | 20878456 / 31721780 |
| memory-used fraction at t0 | 34.182584% | (31721780 - 20878456) / 31721780 |
| MemAvailable / MemTotal at t1 | 65.709919% | 20844356 / 31721780 |
| H1 line | 3172178.0 kB available | 10% of MemTotal |
| kB available above H1 | 17706278.0 | 20878456 - 3172178 |
| swap used / SwapTotal | 27.372698% | 9831500 / 35917176 |
| zram used / swapon size | 99.968052% | 4293591040 / 4294963200 |
| zram free bytes | 1372160 | size - used |
| swapfile free bytes | 26710360064 | 32484225024 - 5773864960 |
| since-boot mean pswpin | 2471.116 KiB/s | 76930329 * 4096 / 1024 / 124527.25 |
| since-boot mean pswpout | 3239.357 KiB/s | 100847043 * 4096 / 1024 / 124527.25 |
| user.slice current / MemTotal | 77.024391% | 25019912192 / (31721780 * 1024) |
| file / user.slice current | 70.699091% | 17688850432 / 25019912192 |
| anon / user.slice current | 20.845717% | 5215580160 / 25019912192 |
| host PSI some, life / uptime | 0.064474% | (80287565 / 1e6) / 124527.25 |
| host PSI full, life / uptime | 0.062801% | (78204772 / 1e6) / 124527.25 |
| kswapd scan in window | 19986.880 KiB/s | 24984 * 4 / 5.000080 |
| kswapd steal in window | 19309.291 KiB/s | 24137 * 4 / 5.000080 |

Since-boot means are averages over the whole boot, including whatever pressure happened earlier. They are not the current rate. The current rate is the 5 s delta: 0.

## 4. Inference

**reading_class = healthy.** H1 is false (65.817% available vs a 10% line). H2 is not applicable (`memory.max` token `max`) and therefore not low-headroom. No required surface was missing, so the class is not `unavailable`.

Why nearby numbers do not flip the class:

- `memory.current` is 77.0% of MemTotal, but 70.7% of that current is file cache. Comparing current to MemTotal treats cache as pressure. H2 compares current to `memory.max` only. There is no numeric max.
- Lifetime `pswpin`/`pswpout` are large (315106627584 and 413069488128 bytes). The 5 s window moved 0 pages. History is not current headroom.
- zram is 99.968% of its swapon size. Aggregate swap used is 27.373%, under the 90% occupancy line, and the lower-priority swapfile still has 26710360064 bytes free. Device fill is not host stall. PSI avg10/60/300 are 0.00 on the host and on both slices.
- kswapd scanned and stole pages during the window while direct reclaim, swap in/out, and PSI averages stayed at zero. That is background reclaim with MemAvailable still ~19.9 GiB, not a crossed H1 line.
- `oom_kill 1` on `user.slice` and `user-1000.slice` `memory.events`, with `memory.events.local` `oom_kill 0`, means a descendant tripped the counter sometime this boot. It is not an input to H1 or H2. This report does not classify the kill, name a pid, or treat the counter as current pressure.
- Host PSI `full` avg10 0.00 is below `DefaultMemoryPressureLimit=60%`. A point sample cannot prove the 30 s duration in `oomd.conf(5)`; it can show the 10 s, 60 s, and 300 s averages are under that limit. PSI is context, not an H predicate. It did not need to be consulted to reach `healthy`.
- `oomctl` at `2026-10-15T00:30:41Z` failed: `Could not activate remote peer 'org.freedesktop.oom1': activation request failed: unknown unit`. The 90% / 60% figures are the configured defaults in the file. This report does not claim a live killer is enforcing them, and does not claim unit enablement (that would be tsukuroi).

`systemctl show` at `2026-10-15T00:30:41Z` (corroboration, earlier than the snapshot): `user.slice` `MemoryMax=infinity`, `MemoryHigh=infinity`, `ManagedOOMSwap=auto`, `ManagedOOMMemoryPressure=auto`. Same for `user-1000.slice` and `user@1000.service`. `auto` means this cgroup is not itself opted into oomd monitoring. Not a class input.

## 5. Unknown

- Which descendant pid or cgroup produced `oom_kill 1`, and when. Journal/cgroup kill census owns that. Not resolved here.
- Swap bursts outside the 5.000080 s window. Counters are unchanged across the window edges, so none inside it. Earlier bursts exist only as the cumulative totals.
- Whether MemAvailable stays near 66%. This is one window. t0→t1 moved MemAvailable by -34100 kB with MemFree rising; that is noise relative to H1, not a trend.
- The exact kernel watermark arithmetic inside MemAvailable. Not re-derived. The field is used as exported.
- The subtraction formula for oomd "memory used" is inferred from the binary's field set and the MemAvailable≤MemTotal check, not from a local comment that states the subtraction. If that inference were wrong, H1's 10% line would need revision; the raw MemAvailable percentage would not.

## 6. Predicate revision for the integrator

Id strings unchanged. Bounds this reading actually used:

| id | this reading | bound |
|---|---|---|
| `MEM_HEADROOM_LOW` | not fired | H1: MemAvailable < 10% of MemTotal, **or** H2: numeric `memory.max` and current ≥ 90% of max. Subject `scope=host` for H1, `cgroup=/sys/fs/cgroup/user.slice` for H2. |
| `MEM_HEADROOM_CRITICAL` | not used | 5% proposal not adopted. No local source. |
| `MEM_PRESSURE_UNAVAILABLE` | not fired | would fire only if MemAvailable or the user-slice current/max pair could not be read. Partial reads would still be listed. |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | not fired | both files readable. |
| `MEM_HEADROOM_OK` | clean label | available above H1 and no numeric ceiling breach. Not a finding id. |

Do not emit `MEM_HEADROOM_LOW` from: cumulative `pswpin`/`pswpout` > 0, since-boot mean si/so, zram fill, `memory.current / MemTotal`, file-cache-inclusive current, or `memory.max=max`.

No probe was refused. No process was restarted, killed, or reparented. No file outside this report was written.
