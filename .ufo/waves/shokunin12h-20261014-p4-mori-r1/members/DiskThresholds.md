# DiskThresholds — falsification of the disk-runway percents

Advisory calibration footnote for mori probation round 1. Not a `MORI_CENSUS` verdict, not a judge result, not a roster claim. Detect/report only: no delete, no quota write, no resize, no remediation.

Compare keys below (`DT-*`) belong to this footnote so a later run can diff them. They are not gate ids. Gate spelling stays on the FindingIds catalog.

## Counterexample

Every proposed warn/critical percent is a bare constant. None is derived from what this fleet writes or how fast. Three notes name three different soft defaults (80, 85, 90) for the same predicate. The only disk failures the fleet reports actually name are quota events (`EDQUOT`, "disk-quota pressure"), which a capacity-% probe cannot see, and the quota numbers are unreadable on this host. Separately, `btrfs` data-chunk fill is 94.25% while `df` Capacity on the same device is 10%: thresholding the chunk percent false-fires `DISK_LOW` today. And the proposed byte floors, if OR'd against `df -P`'s 1024-block Available column, also false-fire today on a filesystem that `df` prints as 10% full.

No replacement percent is supplied. Inventing one would be another unmeasured constant.

## Proposed constants (duplicate authority)

| Source | Soft / warn | Hard / crit | Byte floor | `/tmp` special | Status in that note |
|---|---|---|---|---|---|
| `FindingIds.md` §3.5 (lines 154–164) | `DISK_WARN_PCT=85` on all in-scope roots | `DISK_CRIT_PCT=95` | `DISK_WARN_AVAIL_BYTES=5 GiB`, `DISK_CRIT_AVAIL_BYTES=1 GiB`, fleet+scratch only, **OR** with the percent | `DISK_TMP_WARN_PCT=80` | "proposals until DiskThresholds falsifies" |
| `FixtureDesign.md` §6.5 (lines 262–281) and cases 32–33 | default **85** (84% must not fire; 90% fires warn) | default **95** (96% and 97% fire crit) | none | same pair; any configured root may fire | fixture contract, not a measurement |
| `GateDesign.md` lines 48, 182–183, 486–490 | `MORI_DISK_WARN_PCT` default **85** | `MORI_DISK_CRIT_PCT` default **95** | not implemented | `/tmp` uses the same 85/95 | "proposal — no fleet write-rate evidence yet (DiskThresholds peer)" |
| `CorpusMap.md` §7.5 (lines 510–512) | `MORI-DK-020` default **90** | `MORI-DK-021` default **95** | `MORI-DK-030` "under soft byte floor", **no number** | none | "default", not marked unmeasured |

`operator-demand.md` (25 lines) contains no disk percent. Searched 2026-10-15 for `percent|85|95|disk|runway`: no matches.

A row at 87% is `DISK_LOW` under FindingIds/FixtureDesign/GateDesign and clean under CorpusMap's soft 90. A `/tmp` row at 82% is `DISK_LOW` under FindingIds' 80 and clean under the gate's 85. Those are not two observations. They are two predicates.

## Evidence

### E1. Commands and the live capacity integers

Interactive `df` in this shell is a builtin (`df 0.8.0`). The gate, under `bash`/`sh`, resolves `/usr/bin/df`. Both were asked. One paired sample agreed; that is not a proof they share a formula.

Command, 2026-10-15T00:41:27Z:

```text
/usr/bin/df --version
→ df (GNU coreutils) 9.11

/usr/bin/df -P -B1 /tmp /home/vgpnk/Projects/shokunin
Filesystem           1-blocks        Used    Available Capacity Mounted on
tmpfs             16241553408  9778409472   6463143936      61% /tmp
/dev/mapper/root 998037782528 98916921344 896442683392      10% /home
```

Same second, `/usr/bin/df -P` (1024-blocks) printed Capacity **10%** for `/home/vgpnk/Projects/shokunin`, `/`, `/var/tmp`, and `/home`, with identical `Used=96598556` and `Available=875432308`. `96598556 * 1024 = 98916921344`, matching the `-B1` Used. One space pool, four paths.

`/usr/bin/df -P /scratch` and `/scratch/tmp` at 2026-10-15T00:38:09Z: `No such file or directory`. Missing surface = `unavailable`, not low and not critical.

`findmnt -T` at 2026-10-15T00:38:09Z:

- fleet path → `/home`, source `/dev/mapper/root[/@home]`, `btrfs`, options include `compress=zstd:3`
- `/tmp` → `tmpfs`, `size=15860892k`, `nr_inodes=1048576`, options include `usrquota`

True ratio `Used/(Used+Available)` at the 00:41:27Z `-B1` row:

- btrfs: `98916921344 / 995359604736 = 0.099378` → **9.938%**, printed **10%**
- tmpfs: `9778409472 / 16241553408 = 0.602061` → **60.206%**, printed **61%**

Truncation predicts 60 for tmpfs. Round-half-up (`(used*100 + total/2) / total`) predicts 60. Ceiling of `used*100/(used+available)` predicts 61 and also predicts the printed 10 on btrfs. **[inference]** the local GNU 9.11 print is consistent with ceiling on these two rows and inconsistent with truncation and half-up. The flip-point bytes below use that hypothesis. If the true rule differs by one displayed point, btrfs headroom moves by `995359604736/100 = 9.954 GiB` and tmpfs headroom by `0.151 GiB`. That swing does not turn any proposed percent into a measured write-rate.

Under the ceiling hypothesis, printed `P` begins once the true ratio exceeds `P-1` percent:

| Printed threshold | btrfs bytes still to write | btrfs free when it flips | tmpfs bytes still to write | tmpfs free when it flips |
|---|---|---|---|---|
| 80 | 687417166398 (640.207 GiB) | 194.670 GiB | 3052417721 (2.843 GiB) | 3.176 GiB |
| 85 | 737185146635 (686.557 GiB) | 148.320 GiB | 3864495391 (3.599 GiB) | 2.420 GiB |
| 90 | 786953126872 (732.907 GiB) | 101.970 GiB | 4676573062 (4.355 GiB) | 1.664 GiB |
| 95 | 836721107108 (779.257 GiB) | 55.620 GiB | 5488650732 (5.112 GiB) | 0.908 GiB |

Avail-byte floors against this same `t = Used+Available` (not against the 1024-block column):

| Floor | Where it would bind on btrfs | Printed % then | Where it would bind on tmpfs | Printed % then |
|---|---|---|---|---|
| 5 GiB | after 829.877 GiB more writes | 100 | after 1.019 GiB more writes | 67 |
| 1 GiB | after 833.877 GiB more writes | 100 | after 5.019 GiB more writes | 94 |

On the fleet device the 5 GiB and 1 GiB floors sit *past* printed 95 (free at printed 95 is still 55.620 GiB). They cannot fire first. On tmpfs a 5 GiB floor would arm at printed 67, ~1.019 GiB from this sample — but FindingIds applies that floor to "fleet + scratch", not to `/tmp`, and gives `/tmp` the 80% row instead. The floor is dead on the only device it claims, and unbound on the device where a gigabyte-scale floor could matter.

### E2. What was written, and how fast it was not

mtime-touched apparent bytes are an **upper bound** (a rewrite or a `touch` counts the whole file). They are not a sustained rate. Measured 2026-10-15T00:37:07Z by a walk of regular files, `st_size`, no cross-device descent.

| Tree | Apparent bytes | mtime ≤1h | mtime ≤24h | Directory ctime (UTC) |
|---|---|---|---|---|
| `.ufo` | 15670640 | 2459148 | 7465367 | (pre-existing tree) |
| `.ufo/waves` | (inside `.ufo`) | 2584851 at 00:36:00Z on the waves walk | 6917068 | — |
| `mori-shokunin` | 117029 | 117029 | 117029 | mint tree, all inside 1h |
| `game-dev-2d-shokunin` | 18762132220 | 1353946331 | 17518084408 | 2026-10-14T15:50:50Z |
| `audio-shokunin` | 5426355618 | 3073301 | 5176781360 | 2026-10-14T17:42:32Z |
| `game-dev-3d-shokunin` | 1047715702 | 14555312 | 902776058 | 2026-10-14T12:01:50Z |
| `scripts/shokunin-watchdog.sh` | 5540 | 0 | 0 | mtime 2026-10-13T19:44:48Z |

Watchdog log, `stat` + `wc -c` + head/tail at 2026-10-15T00:37:19Z: size **19396**, mtime `2026-10-13 16:44:48.524089950 -0300`, first line `2026-09-28T15:44:59-03:00 watchdog tick…`, last line `2026-09-28T23:55:00-03:00 tick=3`. Content is a finished fleet-wrap from 2026-09-28. Current write rate of the driver log is **0**.

The 24h columns on the three large lanes are materializations, not a slope. Each directory ctime is today, and almost every byte in the tree carries an mtime inside that window. The only hour-scale burst inside `game-dev-2d` was two clusters, walked at 2026-10-15T00:38:33Z (age in minutes → bytes): minute 55 → 651059255 (files mtime 2026-10-14T23:42:34Z, seven copies of `fixture.x86_64` at 73703800 each plus the extract), minute 48 → 693141043 (mtime 2026-10-14T23:50:11Z, one tar `HEAD-884a4c4245f7a0838b8e00c8b7595f1056544032.tar` of 688373760). Minutes 0–39 of that hour were empty. After 23:50Z the lane was idle through the walk. Audio's last hour was 3073301 bytes. That is a freeze/extract burst, then stop. It does not justify a percent.

Hostile upper bound, not a forecast: treat the entire `.ufo` 24h mtime-touched mass (7465367 bytes) as if it were new bytes every day. Bytes to printed-85 on btrfs / that mass = **98747 days** (~270 years). Even this over-count never approaches 85. Reaching printed-85 would take **35.1** more copies of `game-dev-2d`'s allocated size (`du -B1` at 2026-10-15T00:32:56Z: 20999217152). Nothing observed says the program does that.

`/tmp` is the only root where the gap to 85 is small in absolute bytes, and it is burst occupancy, not a line. Walk at 2026-10-15T00:37:15Z, regular files, apparent `st_size`, boot `btime 1791899878` (uptime 124760 s at 00:37:19Z, so every tmpfs byte is from this boot):

| Age | Apparent bytes | Files |
|---|---|---|
| 0–15 min | 18007131 | 2740 |
| 15 min–1h | 30105698 | 1006 |
| 1–6h | 2359876073 | 101496 |
| 6–24h | 3609350839 | 89021 |
| >24h (still this boot) | 3215558723 | 37501 |
| total | 9232898464 | 231764 |

`df` Used at 00:41:27Z is 9778409472. The walk's 9232898464 is regular-file apparent size only; the gap is directories, non-regular files, and allocation rounding. Do not subtract them into a rate.

Last hour of `/tmp` is ~48.1 MiB (18.0+30.1), and the newest 15 minutes are 18.0 MiB. The boot-average `9778409472/124760 ≈ 78.4 KiB/s` (~269 MiB/h) is the wrong model: the histogram is lumps. Largest single directory, same walk: `w8-audm8-gate` **1010846312** bytes (~0.941 GiB), newest file 2026-10-14T19:28:16Z, **0** bytes in the last hour. Free tmpfs at 00:41:27Z is 6463143936 (6.019 GiB), which can hold **6.39** more directories of that size. Printed-85 is **3.82** such directories away. Printed-95 leaves **0.908 GiB** free, which is **less than that one observed directory**: a repeat of `w8-audm8-gate` started at the critical line would run out mid-write. That shows 95 is late relative to one scratch, not that some other percent is measured. The multiplier (warn at N copies of the largest scratch) is not in the operator demand, the skill, or any note. **[unknown]** which N would be the requirement. Therefore 80/85/90/95 on `/tmp` stay proposals.

### E3. The percent that would false-fire today

`btrfs filesystem usage -b /home` at 2026-10-15T00:42:17Z (same reading, non-root, so per-device chunk detail was refused with the tool's own warning):

```text
Device size:        998037782528
Device allocated:   107399348224
Device unallocated: 890638434304
Data,single: Size:100940120064, Used:95135752192 (94.25%)
```

94.25% of the **allocated data chunk** is not Capacity. Unallocated space is 829.472 GiB. The chunk allocator takes from that pool; `df` Capacity stays 10%. A probe that thresholds `btrfs filesystem df` Data used/size, or copies "94%" into `used_pct`, fires `DISK_LOW` against every proposed soft default and sits 0.75 points under 95, while the fleet root has 835 GiB-class free space (Available 896442683392 bytes = 834.888 GiB). GateDesign's `df -P` parser does **not** make this mistake. The correction is to keep it that way and to stop anyone "improving" the probe onto the chunk percent.

`/usr/bin/df -Pi` at 2026-10-15T00:42:17Z: tmpfs inodes `1048576` used `351046` free `697530` IUse% **34%**. btrfs inodes `0 0 0 -`. Inode percent on the fleet device is **unavailable**, not healthy and not zero. No note proposes an inode percent. None is added here. 34% inode use on tmpfs is not the binding constraint next to 61% blocks.

### E4. Quota and the one ENOSPC line

Historical fleet notes, no use% attached:

- `.ufo/reports/round-11/kotoba.md:84` — "`/tmp/round11` was wiped mid-round by disk-quota pressure". Scratch was rebuilt; the note says scratch is not evidence.
- `.ufo/reports/round-13/kasegi.md:36` — "Transient EDQUOT zeroed ThresholdsReviewer's report file mid-round".

Those are quota failures. A capacity-% gate at 85/95 reports nothing while the quota is already refusing writes. This boot's user journal does not add a filesystem quota event.

Command, 2026-10-15T00:37:19Z:

```text
journalctl --user -b --no-pager -g 'No space left|EDQUOT|Disk quota|ENOSPC' -n 40 -o short-iso
```

One hit, also the only hit from `journalctl -b` with the same pattern:

```text
2026-10-14T18:54:21-03:00 plazir27 pipewire-pulse[1203790]: pw.node: 0x55c247b654e0: can't add port 0x55c247437350: -28, No space left on device
```

`-28` is `ENOSPC` on a pipewire port add, not a block allocation. Classifying that line as `DISK_CRITICAL` would be a false fire. No `EDQUOT` line on this boot in that search.

Quota readout, same evening, read-only `quotactl(Q_GETQUOTA)`:

| special | errno | meaning |
|---|---|---|
| `/tmp`, `/home`, `/` as a path | 15 `ENOTBLK` | not a block device |
| `/dev/mapper/root` | 19 `ENODEV` | no quota device there |

`command -v quota`, `repquota`, and `xfs_quota` were empty. `findmnt` still shows `usrquota` on the tmpfs options. The flag is present; the limits and the current usage are **unavailable**. Unavailable is not "no quota pressure" and not healthy. `btrfs qgroup show` earlier in the hour failed for lack of permission (`can't list qgroup`); qgroup enforcement is **unknown**.

### E5. Unit trap on the byte floor (latent, fatal if wired)

GateDesign parses `df -P` **without** `-B1`. Available is in 1024-byte blocks. At 00:41:27Z that column is `875432308` on the fleet device and `6311664` on `/tmp`.

FindingIds' floors are named `*_AVAIL_BYTES` and given as GiB (`5 * 2^30 = 5368709120`, `1 * 2^30 = 1073741824`). Compared against the **unscaled** `df -P` Available integers:

- `875432308 < 5368709120` and `875432308 < 1073741824` → both floors true on the 10% filesystem
- `6311664 < 1073741824` → both floors true on `/tmp` as well

OR-ing the floor onto the gate's current avail field false-fires `DISK_LOW` / `DISK_CRITICAL` on every configured root **now**, with hundreds of GiB free. The gate does not implement the floor yet. Wiring it without `df -B1` (or `statvfs`) is the bug. The fixture's synthetic `df` (`FixtureDesign.md:277`, `100%` / 1024-blocks) does not catch it, because the floor is absent from the fixture too.

### E6. What is not claimed

- No live `MORI_CENSUS:` line was produced. There is no before/after gate tally here.
- The 1h/24h figures are not a forecast. Linear extrapolation of the boot-average tmpfs fill (~14 h to printed-85) contradicts the age histogram and is rejected.
- Pipewire `-28` is not disk runway.
- 94.25% is not runway.
- This seat did not edit GateDesign, FindingIds, CorpusMap, FixtureDesign, the corpus, or the host.

## Inference vs unknown

**Observed.** `df` Capacity 10% (btrfs, one device for fleet path, `/`, `/home`, `/var/tmp`) and 61% (`/tmp`). `/scratch` and `/scratch/tmp` absent. Watchdog log frozen since 2026-09-28 content. Large lane trees created today and idle after two extract bursts. `/tmp` occupancy is lumpy; largest dir ~0.941 GiB and not growing in the sample hour. Chunk used/allocated 94.25% with 890638434304 bytes unallocated. Quota tools missing; `Q_GETQUOTA` failed; historical notes name quota, not a percent. One pipewire `ENOSPC`. `df -P` Available in KiB is numerically below both GiB floors.

**Inference.** Printed percent behaves like ceiling on the two measured rows. Headroom table in E1. The 24h `.ufo` upper bound does not reach 85% within centuries. Printed-95 on tmpfs is smaller than one observed scratch directory. The 5 GiB/1 GiB floors cannot precede 95% on this btrfs device.

**Unknown.** The actual quota limits behind `usrquota` and behind the round-11/round-13 incidents (no use%, no byte cap recorded). Whether btrfs qgroups enforce anything. Which multiple of the largest scratch, if any, an operator wants as warning. A steady write rate: the samples do not support one. GNU `df`'s source-level rounding (ceiling is a fit, not a reading of `df.c`).

## Impacted axes

- **Calibration.** 85, 95, 80, 90, 5 GiB, and 1 GiB are not write-rate results. Shipping any of them as a measured default launders a proposal. CorpusMap's soft 90 and FindingIds' tmp 80 contradict the gate/fixture pair 85/95, so a later diff cannot even say which proposal was tested.
- **Coverage.** A percent probe misses the only named failure class (quota), reports quota-unavailable as if the percent being fine meant the disk was fine, and does not cover btrfs inodes (`-`). Path aliases of one btrfs pool would emit repeated findings if CorpusMap's six roots were all configured. The chunk percent, if substituted, covers the wrong quantity.
- **Operability.** The byte-floor OR against `df -P` 1024-blocks false-fires at the current 10% and 61% readings. The fixture never exercises a floor. A journal grep for "No space left" false-fires on the pipewire port line. Interactive `df` here is not `/usr/bin/df`; the receipt has to name the binary.

## Smallest safe correction

Do not install a new percent. Keep a single proposal pair and mark it uncalibrated.

1. One soft number and one hard number, both labeled `proposal, not measured`. The fixture already encodes **85/95** (case 32: 84% quiet; case 23: 90% warn; case 22: 96% crit). CorpusMap `MORI-DK-020` default **90** and FindingIds `DISK_TMP_WARN_PCT` **80** must not be described as the default beside that pair. Point those sentences at `MORI_DISK_WARN_PCT` / `MORI_DISK_CRIT_PCT` and say the R1 proposal is 85/95 with no write-rate evidence. Deleting the extra numbers is the whole fix; do not replace them with a "better" percent from this note.
2. Do not OR in `DISK_WARN_AVAIL_BYTES` / `DISK_CRIT_AVAIL_BYTES` until the probe is `df -B1 -P` (or `statvfs`) and the compare is in bytes. On this btrfs device those floors are unreachable before printed 95, so they are not doing work here. Leave them out of the R1 gate rather than wiring the 1024-block bug. `MORI-DK-030` has no number; do not invent one.
3. Capacity stays the integer from `/usr/bin/df -P`. Never the `btrfs` Data,single used/size figure (94.25% today). Record `df --version` on the receipt. Do not treat the shell builtin `df 0.8.0` as the gate's df.
4. One finding per space pool. Fleet path, `/`, `/home`, and `/var/tmp` shared `Used` and `Available` in the 00:41:27Z sample. Repeating them is one observation four times. `/tmp` is a second pool. `/scratch/tmp` absent stays `unavailable` (info), never `DISK_LOW`.
5. Quota readout failure stays `unavailable`. Do not grade the disk healthy because Capacity is 10% while `usrquota` is set and the limits are unreadable. Do not promote the pipewire `-28` line to a disk finding.

## Axis note for the parent footnote

Coverage of the proposed constants: all six numbers in the table were checked against a measured write bound and against the live `df` row; none survived as evidence. Operable correction is the five steps above, all deletions or labels, no new threshold and no host mutation. Calibration result: **proposal, no evidence** for 80, 85, 90, 95, 5 GiB, and 1 GiB.
