# DiskRunway — fleet/host disk runway census

**Role:** scout (leaf) · **Wave:** shokunin12h-20261014-p4-mori-r1 · **Lane:** mori-shokunin
**Advisory:** data only. Not a gate verdict, not `MORI_CENSUS: CLEAN|DRIFT`, not a remediation order.
**Published snapshot:** `2026-10-14T21:34:29-03:00` (host local, UTC−03). Byte table and `-h` table are sequential `/usr/bin/df` invocations inside that same second. Earlier samples in this seat (21:28, 21:31) moved by megabytes and are **not** mixed into the rows below.
**Hard rule:** read-only. No delete, no mkdir, no mount, no quota edit, no dispatch.

## Axes

| Axis | What this report does |
|---|---|
| coverage | Fleet root plus every scratch root the live resolver and UFO source name (`/tmp`, `/scratch/tmp`, `/scratch/tmp/vgpnk`). Host tmpfs that are **not** in that chain are listed as checked-and-out-of-scope, not dropped silently. |
| operability | Each row names the binary, the argv, and the timestamp. Bare `df` is a shell builtin here; the census command is `/usr/bin/df`. |
| calibration | A missing path is `unavailable`, never unhealthy. `df` Use% is not available-percent. btrfs chunk-fill is not capacity. Shared-pool bytes are not a subvolume quota. |

## 1. Which roots are in scope

**Fleet root (observation).** `/home/vgpnk/Projects/shokunin` exists, is a directory, `st_dev=57`, mountpoint `/home`. Lane checkouts under that tree and `/home/vgpnk/Projects/ufo-fsd-alpha` share `st_dev=57`. One filesystem row covers them. This is not a claim about other disks.

**Scratch resolution (source + one live call).** `scripts/ufo-sighting-lib/argv.mjs:206-218` (`/home/vgpnk/Projects/ufo-fsd-alpha`) defines `DEFAULT_SCRATCH_ROOT = "/scratch/tmp"` and `scratchSessionRoot()` as: `env.TMPDIR`, then `/scratch/tmp`, then `os.tmpdir()`, skipping candidates that are not an absolute existing directory. The same order is copied in `scripts/run-omp-native-trial.mjs:30-33`. Comment at `tests/ufo-sighting.test.js:305-306` says session dirs resolve `TMPDIR → /scratch/tmp → os.tmpdir()` so tmp writes persist to a second NVMe when that root is present.

Live read-only call at the snapshot second:

```text
DEFAULT_SCRATCH_ROOT=/scratch/tmp
scratchSessionRoot=/tmp
TMPDIR=unset
```

`node -e "console.log(require('os').tmpdir())"` in the same window printed `/tmp`.

**Named fleet scratch paths that are not separate filesystems:**

| Path | Why it is in scope | At snapshot |
|---|---|---|
| `/scratch/tmp` | `DEFAULT_SCRATCH_ROOT` | absent |
| `/scratch/tmp/vgpnk` | `UFO_TEST_SCRATCH` default in `scripts/fleet-dispatcher.test.mjs:41` | absent |
| `/tmp` | `os.tmpdir()` fallback; also the value `scratchSessionRoot()` returned | present |

`/scratch` is the missing ancestor of those two paths, not itself a named scratch root. It is recorded so a later compare can see the absence chain.

**Checked, not fleet scratch roots (observation, no finding):**

| Path | Why it is not a fleet scratch root |
|---|---|
| `/var/tmp` | Present. `st_dev=31`, same device as `/`. Not in `scratchSessionRoot()` or `UFO_TEST_SCRATCH`. |
| `/dev/shm` | Present tmpfs, 1% used at 21:31. Not in the resolver chain. |
| `/run`, `/run/user/1000` | Present. `XDG_RUNTIME_DIR=/run/user/1000` in this process. Runtime dir, not the scratch chain. |
| `$TMPDIR` | Unset in this process, unset in `systemctl --user show-environment` (no `TMPDIR`/`TMP`/`TEMP` line), unset in all 97 readable `/proc/<pid>/environ` at 21:34:29. |

## 2. Commands (re-run)

Pin the binary. In this agent shell `type df` prints `df is a shell builtin` and `df --version` prints `df 0.8.0`. `/usr/bin/df --version` prints `df (GNU coreutils) 9.11`. Numbers below are GNU coreutils only.

```sh
/usr/bin/df -B1 -PT -- /home/vgpnk/Projects/shokunin /tmp /var/tmp / /home
/usr/bin/df -B1 -PT -- /scratch /scratch/tmp /scratch/tmp/vgpnk
/usr/bin/df -hPT -- /home/vgpnk/Projects/shokunin /tmp
/usr/bin/df -iP -- /home/vgpnk/Projects/shokunin /tmp /
/usr/bin/findmnt -T /home/vgpnk/Projects/shokunin -n -o TARGET,SOURCE,FSTYPE,OPTIONS
/usr/bin/findmnt -T /tmp -n -o TARGET,SOURCE,FSTYPE,OPTIONS
/usr/bin/findmnt -T / -n -o TARGET,SOURCE,FSTYPE,OPTIONS
```

`df: <path>: No such file or directory` plus `test -e` false is the unavailable observation. Do not rewrite that as a capacity percent.

## 3. Observations — published snapshot `2026-10-14T21:34:29-03:00`

Command: `/usr/bin/df -B1 -PT`. **Percent column is GNU `Capacity` / `-h` `Use%`:** `used / (used + available)`, rounded to integer. It is **not** available/size. Available is `statvfs` `f_bavail` (what this `df` prints), not a health grade.

| row id | subject | surface | filesystem | type | size (1-blocks) | available (1-blocks) | percent (df Capacity) | mounted on |
|---|---|---|---|---|---:|---:|---:|---|
| `DISK_ROW_FLEET_ROOT` | `path=/home/vgpnk/Projects/shokunin` | present | `/dev/mapper/root` | btrfs | 998037782528 | 896449593344 | 10% | `/home` |
| `DISK_ROW_TMP` | `path=/tmp` | present | `tmpfs` | tmpfs | 16241553408 | 6506156032 | 60% | `/tmp` |
| `DISK_ROW_SCRATCH_TMP` | `path=/scratch/tmp` | **unavailable** | — | — | — | — | — | — |
| `DISK_ROW_SCRATCH_VGPNK` | `path=/scratch/tmp/vgpnk` | **unavailable** | — | — | — | — | — | — |

Same-window `/usr/bin/df -hPT` (display rounding, not a second measurement to prefer over the byte table):

```text
Filesystem       Type   Size  Used Avail Use% Mounted on
/dev/mapper/root btrfs  930G   93G  835G  10% /home
tmpfs            tmpfs   16G  9.1G  6.1G  60% /tmp
```

Exact byte companions (derived from the `-B1` columns, 1024-based; labeled derived so they are not a second probe):

| path | size | used (size − not used; df Used column) | available | available/size |
|---|---:|---:|---:|---:|
| fleet root fs | 929.512 GiB | 92.116 GiB (`98909257728`) | 834.996 GiB | 89.821% |
| `/tmp` | 15.125 GiB | 9.067 GiB (`9735397376`) | 6.059 GiB | 40.059% |

Capacity check against the same columns (derived, matches the printed percent): fleet `98909257728 / (98909257728 + 896449593344) = 9.937%` → `10%`. `/tmp` `9735397376 / 16241553408 = 59.942%` → `60%`.

### Filesystem identity (not the df source string alone)

`/usr/bin/findmnt -T` at the same window:

| path | findmnt source | fstype | options that identify the fs |
|---|---|---|---|
| `/home/vgpnk/Projects/shokunin` | `/dev/mapper/root[/@home]` | btrfs | `subvolid=257,subvol=/@home` |
| `/tmp` | `tmpfs` | tmpfs | `size=15860892k,nr_inodes=1048576,inode64,usrquota` |
| `/` | `/dev/mapper/root[/@]` | btrfs | `subvolid=256,subvol=/@` |

`/usr/bin/df` prints both `/` and `/home` as `/dev/mapper/root` with **identical** size, used, and available (`998037782528` / `98909257728` / `896449593344`). They are different subvolumes. Identical df numbers are the shared device pool, not proof of equal exclusive usage.

`/usr/bin/df -iP` at the same window:

| path | inodes | iused | ifree | iuse% | reading |
|---|---:|---:|---:|---|---|
| fleet root (`/home`) | 0 | 0 | 0 | `-` | inode accounting via `df -i` is **unavailable**, not "zero used" and not healthy |
| `/tmp` | 1048576 | 344383 | 704193 | 33% | separate from the 60% byte Capacity; no inode threshold is applied here |
| `/` | 0 | 0 | 0 | `-` | same unavailable inode surface as `/home` |

`lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS` (21:33:19): one NVMe (`nvme0n1`, 931.5G) → LUKS → `root` btrfs mounted at `/`, `/home`, `/var/log`, `/var/cache/pacman/pkg`. Also `zram0` swap, and `sda`/`sr0` iso9660. **No block device mounted at `/scratch`.** `/etc/fstab` (22 lines) has **zero** lines containing `scratch`.

`btrfs filesystem usage -b /home` (21:33:19, rc 0): `Device size` `998037782528` equals the df size column. `Free (statfs, df)` `896450555904` is the same class of number as df Available (it had already drifted a few megabytes from the 21:31 df). `Data,single` `Used:95126949888 (94.24%)` is **fill of the allocated data chunk**, not filesystem capacity. Do not compare that 94.24% to `DISK_CRITICAL`.

## 4. Finding rows (stable ids)

Vocabulary aligned with sibling `FindingIds.md` §3.5 (`DISK_LOW`, `DISK_CRITICAL`, `DISK_ROOT_UNAVAILABLE`). Threshold constants there are marked **proposal**. This seat applies them only as a labeled predicate check. It does not freeze them and does not emit a census banner.

FixtureDesign's disk-missing id is `DISK_UNAVAILABLE`. This report uses FindingIds' `DISK_ROOT_UNAVAILABLE`. Those strings are not reconciled here.

| id | sev | subject | predicate at snapshot | payload |
|---|---|---|---|---|
| `DISK_ROOT_UNAVAILABLE` | info | `mount=/scratch/tmp` | path absent; `/usr/bin/df -B1 -PT -- /scratch/tmp` → `No such file or directory` | not `DISK_LOW`; not unhealthy |
| `DISK_ROOT_UNAVAILABLE` | info | `mount=/scratch/tmp/vgpnk` | path absent; same df error | child of the missing scratch root; fleet test default, not a separate mount |
| `DISK_ROOT_UNAVAILABLE` | info | `mount=/scratch` | path absent; same df error | ancestor, not a named scratch root; included so the absence chain compares |

**Predicates that did not fire** (no finding row; do not invent a CLEAN banner from this sentence):

| id | subject | why it did not fire under FindingIds proposal constants |
|---|---|---|
| `DISK_LOW` | `mount=/home` (fleet root fs) | Capacity 10% < `DISK_WARN_PCT` 85; available 834.996 GiB > `DISK_WARN_AVAIL_BYTES` 5 GiB |
| `DISK_CRITICAL` | `mount=/home` | Capacity 10% < 95; available > 1 GiB |
| `DISK_LOW` | `mount=/tmp` | Capacity 60% < `DISK_TMP_WARN_PCT` 80 and < 85; available 6.059 GiB > 5 GiB |
| `DISK_CRITICAL` | `mount=/tmp` | Capacity 60% < 95; available > 1 GiB |
| `DISK_PROBE_UNAVAILABLE` | `probe=disk` | `/usr/bin/df` returned rows for every present target. Absent paths are per-root unavailable, not a failed probe. |

Compare note from FindingIds §6: keep integer Capacity (`10`, `60`) in `payload_norm`; treat `available_bytes_raw` and `measured_at` as volatile. Between 21:28:41 and 21:34:29, fleet `Used` moved `98901135360` → `98909257728` while Capacity stayed `10%`. `/tmp` Capacity stayed `60%`.

## 5. Inferences (not observations)

1. **Live scratch landing.** Because `TMPDIR` is unset and `/scratch/tmp` is not a directory, `scratchSessionRoot()` returned `/tmp`. Inference: sighting/session code that calls that function on this host, with this environment, uses the `/tmp` tmpfs. This seat did not watch a write.
2. **No second scratch disk is mounted.** One NVMe, no fstab scratch line, `/scratch` absent. The source comment about a second NVMe describes the preferred root when present. It is not evidence that a disk failed.
3. **Fleet available bytes are shared.** df size equals `btrfs filesystem usage` device size, and `lsblk` shows `/var/log` and `/var/cache/pacman/pkg` on the same `root` device. Inference: other writers on that btrfs reduce the number df will print for the fleet root. This is not a pacman-state claim and not a quota measurement.
4. **Bare `df` in this shell is the wrong binary to re-run.** A later agent that copies `df -B1 -PT` without `/usr/bin/df` may hit builtin `df 0.8.0`. The published rows are GNU coreutils 9.11.

## 6. Unknowns

| topic | why it stays unknown |
|---|---|
| Exclusive `/@home` quota | `btrfs qgroup show -pcre /home` exited 1: `can't list qgroups: Operation not permitted`. Unavailable, not "no quota". |
| Whether `/tmp` `usrquota` is tighter than df Available | `quota` is not installed (`command -v quota` → not found). Not probed further. |
| `TMPDIR` of processes whose `/proc/<pid>/environ` is unreadable | 97 readable, all unset; 496 unreadable at 21:34:29. Not a host-wide proof. |
| Inode exhaustion risk on btrfs | `df -i` does not report btrfs inodes (`IUse%` `-`). |
| Whether any inode threshold should fire on `/tmp` at 33% | No inode constant in the disk vocabulary this seat was given. Not mapped to `DISK_LOW`. |
| Subdirectory residue under `/scratch/tmp/vgpnk/...` (cargo-target, fleet-tmp, historical notes) | Parent path absent, so those paths are absent. Not separately `stat`'d. |

## 7. Refused probes

| id | probe | reason |
|---|---|---|
| `PROBE_REFUSED` | `node scripts/fleet-dispatcher.test.mjs` | `SCRATCH_BASE` calls `mkdirSync("/scratch/tmp/vgpnk")` (`fleet-dispatcher.test.mjs:41-44`). Running it would create the missing root. Read the source; did not run it. |
| `PROBE_REFUSED` | any delete, mount, or quota change on `/tmp` or the btrfs pool | mori does not remediate. 60% Use% is a measurement, not an action. |

## 8. Limits

- One snapshot. Capacity integers were stable across the few minutes observed; byte counts were not.
- Does not implement `tools/mori-census.sh` and does not claim `MORI_CENSUS: CLEAN` or `DRIFT`.
- `DISK_ROW_*` ids are observation keys for this census. Threshold findings use the FindingIds strings only.
- No credential, token, or session payload was read. Environ scan kept only `TMPDIR`, `TMP`, `TEMP`, `UFO_TEST_SCRATCH`, `UFO_FLEET_TMP`, `CARGO_TARGET_DIR`, `LEAN_CARGO_SLOT_ROOT`.

## Raw command output (snapshot window)

```text
MEASURE_BEGIN 2026-10-14T21:34:29-03:00
/usr/bin/df -B1 -PT -- /home/vgpnk/Projects/shokunin /tmp /var/tmp / /home
Filesystem       Type      1-blocks        Used    Available Capacity Mounted on
/dev/mapper/root btrfs 998037782528 98909257728 896449593344      10% /home
tmpfs            tmpfs  16241553408  9735397376   6506156032      60% /tmp
/dev/mapper/root btrfs 998037782528 98909257728 896449593344      10% /
/dev/mapper/root btrfs 998037782528 98909257728 896449593344      10% /
/dev/mapper/root btrfs 998037782528 98909257728 896449593344      10% /home

/usr/bin/df -B1 -PT -- /scratch /scratch/tmp /scratch/tmp/vgpnk
df: /scratch: No such file or directory
df: /scratch/tmp: No such file or directory
df: /scratch/tmp/vgpnk: No such file or directory

/usr/bin/df -hPT -- /home/vgpnk/Projects/shokunin /tmp
Filesystem       Type   Size  Used Avail Use% Mounted on
/dev/mapper/root btrfs  930G   93G  835G  10% /home
tmpfs            tmpfs   16G  9.1G  6.1G  60% /tmp

/usr/bin/df -iP -- /home/vgpnk/Projects/shokunin /tmp /
Filesystem        Inodes  IUsed  IFree IUse% Mounted on
/dev/mapper/root       0      0      0     - /home
tmpfs            1048576 344383 704193   33% /tmp
/dev/mapper/root       0      0      0     - /

findmnt -T fleet root: /home /dev/mapper/root[/@home] btrfs … subvolid=257,subvol=/@home
findmnt -T /tmp:       /tmp  tmpfs[tmpfs]            tmpfs … size=15860892k,nr_inodes=1048576,…,usrquota
findmnt -T /:          /     /dev/mapper/root[/@]    btrfs … subvolid=256,subvol=/@
MEASURE_END 2026-10-14T21:34:29-03:00
```
