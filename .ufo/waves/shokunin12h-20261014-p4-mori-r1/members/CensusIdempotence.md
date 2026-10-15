# CensusIdempotence — double-run proof of `tools/mori-census.sh`

**Seat:** CensusIdempotence (mutation-tester, leaf). Advisory data, not a judge verdict. Parent integrates.
**Wave:** shokunin12h-20261014-p4-mori-r1
**Subject:** landed gate `mori-shokunin/tools/mori-census.sh`
**sha256:** `8745a4fce9bfb50a654e30944847bf59d8de643228b2c1e7fd4878c0b122728b`
**size / inode / mtime:** 37255 bytes, inode `11550470`, `2026-10-14 21:48:42.112294555 -0300`
**Measured:** `2026-10-14T21:49:05-03:00` … `2026-10-14T21:49:39-03:00`
**Host:** bash `5.3.15(1)-release`, `strace` present
**Write scope of this seat:** this file only. The gate was not edited. `/tmp` trees are harness scratch, not fleet state.

The live file moved while this seat was measuring (`7432255f…`, `8e655187…`, `580a0e31…`, `81e716de…`, then this blob). Numbers below are for `8745a4fc…` only. That hash matched the live file at the start of the fixture proof, at the end of it (`SNAPSHOT_STILL_LIVE`), and again at `2026-10-14T21:49:39-03:00` after the live pair. The delta from `81e716de…` is `set +o xtrace` (`:56`) plus `realpath -m` before the sysfs check (`:413-416`).

## Axes

| Axis | What was tested |
|---|---|
| coverage | one frozen fixture, twice; `--selftest` twice; one bounded live pair (`MORI_ROSTER_LANES=kama`, clock pinned); one scratch mutation of the read-only claim |
| operability | proof command below, no oral context, no fleet write |
| calibration | same-fixture stdout is idempotent; live stdout is not, and the only mover on this pair is `current=`. Selftest's own hash check does not see a write outside the fixture. Its cleanup trap still does not run, and `set +o xtrace` now hides that from `bash -x`. |

## Probe result

| Claim | Result |
|---|---|
| Same fixture, two census runs, stdout identical | **holds** (both exit 0, `diff` empty) |
| Same fixture bytes before and after those runs and a third strace run | **holds** (21-file manifest identical) |
| No successful host write during the fixture census | **holds** (strace: 0 forbidden paths) |
| `--selftest` twice, harness stdout identical | **holds** (both exit 0, 14/14 PASS) |
| No successful host write during `--selftest` | **holds** for absolute paths outside the temp dir (0). Writes are the fixture builder. The temp dir is not removed (D1). |
| No successful host write during bounded live census | **holds** (strace: 0 forbidden paths) |
| Live stdout byte-identical under a pinned clock | **fails** — only `current=` moved (−397312). Verdict line did not. |
| Selftest removes its temp dir | **fails** — D1 |
| `bash -x` still shows the empty `rm` | **fails** on this blob — `set +o xtrace` blinds it. The leftover directory is the detector. |
| Stdout-diff alone catches a silent write | **fails** — mutant M1 survived stdout-diff and was killed by the write check |

## Proof command

Run from anywhere. Writes only under `/tmp` (fixture, proof dir, strace log). Does not write the fleet tree. Success is empty `diff`s and `forbidden 0`, not a golden stdout hash: the receipt embeds the fixture path, so a new `mktemp` changes the hash without breaking the pair.

```bash
GATE=/home/vgpnk/Projects/shokunin/mori-shokunin/tools/mori-census.sh
PROOF=$(mktemp -d /tmp/mori-idem-proof.XXXXXX)
FX=$(mktemp -d /tmp/mori-idem-fx.XXXXXX)

mkdir -p -- "$FX/ufo/state" "$FX/ufo/waves/wave-settled" "$FX/stub" \
  "$FX/cgroup" "$FX/root/kagi-shokunin" "$FX/bin"
printf '2026-10-14T12:00:00Z tick=1\n' > "$FX/ufo/watchdog.log"
printf '1\n' > "$FX/ufo/state/kagi.round"
printf 'mission-x\n' > "$FX/ufo/state/kagi.mission"
printf '{}\n' > "$FX/ufo/waves/wave-settled/swarm-registry.json"
printf '{}\n' > "$FX/ufo/waves/wave-settled/dispatch.json"
printf '{"schema":"ufo-swarm-results-v1","members":[]}\n' > "$FX/ufo/waves/wave-settled/results.json"
printf 'low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\noom_group_kill 0\n' > "$FX/cgroup/memory.events"
printf 'low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\noom_group_kill 0\n' > "$FX/cgroup/memory.events.local"
printf '123456\n' > "$FX/cgroup/memory.current"
printf 'x\n' > "$FX/root/kagi-shokunin/LOG.md"
printf '1234 bash scripts/shokunin-watchdog.sh\n' > "$FX/stub/pgrep"
printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\n/dev/fx 1000000 10000 990000 2%% /fx\n' > "$FX/stub/df"
: > "$FX/stub/journalctl"
printf 'sess: 1 windows\n' > "$FX/stub/tmux"
touch -d @1700000000 -- "$FX/ufo/watchdog.log" "$FX/root/kagi-shokunin/LOG.md" \
  "$FX/ufo/waves/wave-settled/"*
for c in pgrep df journalctl tmux; do
  printf '#!/bin/sh\ncat "$MORI_FIXTURE/stub/%s"\n' "$c" > "$FX/bin/$c"
  chmod 700 "$FX/bin/$c"
done

fx_manifest() { find "$1" -type f -exec sha256sum {} + | LC_ALL=C sort; }
runfx() {
  env -i PATH="$FX/bin:/usr/bin:/bin" HOME=/tmp LC_ALL=C \
    MORI_FIXTURE="$FX" \
    MORI_SHOKUNIN_ROOT="$FX/root" \
    MORI_UFO_DIR="$FX/ufo" \
    MORI_WATCHDOG_LOG="$FX/ufo/watchdog.log" \
    MORI_STATE_DIR="$FX/ufo/state" \
    MORI_WAVES_DIR="$FX/ufo/waves" \
    MORI_CGROUP_EVENTS="$FX/cgroup/memory.events" \
    MORI_CGROUP_LOCAL_EVENTS="$FX/cgroup/memory.events.local" \
    MORI_CGROUP_SERVICE_EVENTS="$FX/cgroup/memory.events.local" \
    MORI_CGROUP_CURRENT="$FX/cgroup/memory.current" \
    MORI_DF_BIN="$FX/bin/df" MORI_PGREP_BIN="$FX/bin/pgrep" \
    MORI_JOURNALCTL_BIN="$FX/bin/journalctl" MORI_TMUX_BIN="$FX/bin/tmux" \
    MORI_DISK_TARGETS="$FX/root" MORI_ROSTER_LANES=kagi \
    MORI_NOW_EPOCH=1700000000 \
    bash --noprofile --norc "$GATE"
}

fx_manifest "$FX" > "$PROOF/before.txt"
runfx > "$PROOF/run1.out" 2>"$PROOF/run1.err"; echo $? > "$PROOF/run1.rc"
runfx > "$PROOF/run2.out" 2>"$PROOF/run2.err"; echo $? > "$PROOF/run2.rc"
fx_manifest "$FX" > "$PROOF/after.txt"
diff -u "$PROOF/run1.out" "$PROOF/run2.out"    # empty
diff -u "$PROOF/before.txt" "$PROOF/after.txt" # empty

strace -f -e trace=openat,creat,mkdir,mkdirat,unlink,unlinkat,rename,renameat \
  -o "$PROOF/strace.txt" \
  env -i PATH="$FX/bin:/usr/bin:/bin" HOME=/tmp LC_ALL=C \
    MORI_FIXTURE="$FX" MORI_SHOKUNIN_ROOT="$FX/root" MORI_UFO_DIR="$FX/ufo" \
    MORI_WATCHDOG_LOG="$FX/ufo/watchdog.log" MORI_STATE_DIR="$FX/ufo/state" \
    MORI_WAVES_DIR="$FX/ufo/waves" \
    MORI_CGROUP_EVENTS="$FX/cgroup/memory.events" \
    MORI_CGROUP_LOCAL_EVENTS="$FX/cgroup/memory.events.local" \
    MORI_CGROUP_SERVICE_EVENTS="$FX/cgroup/memory.events.local" \
    MORI_CGROUP_CURRENT="$FX/cgroup/memory.current" \
    MORI_DF_BIN="$FX/bin/df" MORI_PGREP_BIN="$FX/bin/pgrep" \
    MORI_JOURNALCTL_BIN="$FX/bin/journalctl" MORI_TMUX_BIN="$FX/bin/tmux" \
    MORI_DISK_TARGETS="$FX/root" MORI_ROSTER_LANES=kagi MORI_NOW_EPOCH=1700000000 \
    bash --noprofile --norc "$GATE" >/dev/null
python3 - "$PROOF/strace.txt" "$FX" << 'PY'
import sys
trace, allowed = sys.argv[1], sys.argv[2]
bad = 0
for line in open(trace, errors="replace"):
    mut = ("openat(" in line and any(k in line for k in ("O_WRONLY","O_RDWR","O_CREAT","O_APPEND","O_TRUNC"))) or any(k in line for k in ("mkdir(","mkdirat(","unlink(","unlinkat(","rename(","renameat(","creat("))
    if not mut or '"' not in line or " = -1 " in line:
        continue
    path = line.split('"', 2)[1]
    if path.startswith("/dev/") or path.startswith("/proc/") or path == allowed or path.startswith(allowed.rstrip("/") + "/"):
        continue
    if not path.startswith("/"):
        continue
    bad += 1
    print("BAD", path)
print("forbidden", bad)
sys.exit(1 if bad else 0)
PY
```

`MORI_CGROUP_LOCAL_EVENTS` and `MORI_CGROUP_SERVICE_EVENTS` have to be set. If they are not, the gate falls through to `/sys/fs/cgroup/user.slice/user-$(id -u).slice/user@$(id -u).service/memory.events` (`tools/mori-census.sh:398`) and the run is no longer a frozen fixture.

## Observed on this run

`FX=/tmp/mori-idem-fx.4o2brD`. Gate sha256 before and after: `8745a4fce9bfb50a654e30944847bf59d8de643228b2c1e7fd4878c0b122728b`.

| Check | Observed |
|---|---|
| `run1.rc` / `run2.rc` | `0` / `0` |
| stdout sha256, both runs | `a22590b8abf4b6c398710d18334aefdaaa9d3302cbb342fc78af477d15dbc695` |
| stdout `diff` | empty |
| stderr | 0 bytes both runs |
| fixture manifest sha256 before, after two runs, and after strace | `3dc76cb102288db61b838ac1d3c9f0e6bb4d86de60faf5030ed2cf5b48c1e80a` (21 files) |
| strace successful writes outside the fixture | `0` |
| strace successful `/dev` opens | 31 |
| strace failed mutation syscalls | 5 (not line-classified on this blob; none succeeded) |

Verdict line both times:

```text
MORI_CENSUS: CLEAN (findings=0 drift=0 unavailable=0 surfaces=7)
```

`ts=` is `2023-11-14T22:13:20Z` because `MORI_NOW_EPOCH=1700000000`. Without that pin the two stdouts differ by the clock even when every finding is identical.

Surface row that the pin does **not** freeze:

```text
SURFACE cgroup: ok (... current=refused:outside-sysfs-cgroup; ts=2023-11-14T22:13:20Z)
```

`tools/mori-census.sh:413-416` runs `realpath -m` on `MORI_CGROUP_CURRENT` and refuses the result unless it is under `/sys/fs/cgroup/`. It does not read the file. The fixture file containing `123456` was not printed. `realpath -m` of a `/tmp` path stays under `/tmp`, so the refusal is stable and the pair is still idempotent. A fixture of this shape cannot prove that a numeric `current=` is stable. That measurement is the live pair below.

Journal stub must be named `stub/journalctl` (the dispatcher `cat`s `$MORI_FIXTURE/stub/$name`). A file named `stub/journal` makes `cat` exit 1; the gate treats rc 1 as an empty journal and still prints CLEAN. This run used the matching name and recorded `rc=0`.

## `--selftest` double run (same gate)

```bash
bash --noprofile --norc "$GATE" --selftest > /tmp/mori-st1.out
bash --noprofile --norc "$GATE" --selftest > /tmp/mori-st2.out
diff -u /tmp/mori-st1.out /tmp/mori-st2.out   # empty
```

Observed on this blob: both exit `0`, harness stdout sha256 both `33225c2ecce32431c8a96d07863aa6cc203e3bd4280eb69225769bb05e009118`, last line:

```text
MORI_CENSUS_SELFTEST: PASS (14 cases, 14 passed, 0 failed)
```

That hash is the PASS/FAIL harness text, not the inner census receipts. It matched earlier blobs' harness text too; it is not evidence that inner receipts are stable across gate edits.

Cases, all `PASS`: `clean: all quiet`, `WATCHDOG_ABSENT`, `WATCHDOG_STALE`, `WAVE_UNSETTLED_AGE`, `unsettled young wave does not fire`, `OOM_KILL_JOURNAL`, `CGROUP_OOM_KILL`, `DISK_CRITICAL`, `disk under warn`, `LANE_SILENT`, `CGROUP_UNAVAILABLE is not DRIFT`, `empty journal`, `cli: unknown arg exit 2`, `cli: --help exit 0`.

`fx_no_mutation` (`:631`, called at `:733`) hashes the case fixture and passed for all 14. It does not see a write outside that fixture, and it does not see the temp dir surviving (D1).

`strace` of one `--selftest` (`/tmp/mori-census-selftest.AzYR3w`): **0** successful absolute writes outside that directory and `/dev`. 125 successful relative `mkdir`/`openat` names (`bin`, `fx`, `cgroup`, `state`, …) are `mkdir -p` component walks after the temp dir exists. `/tmp/bin` does not exist. Failed syscalls (560) are not writes; they include `mkdir("/tmp")` `EEXIST`.

## D1 — selftest temp dir survives, and `bash -x` no longer shows it

**Site:** `mori-shokunin/tools/mori-census.sh:592-594`

```bash
run_selftest() {
  local work bin FX PASS=0 FAIL=0
  work=$(mktemp -d /tmp/mori-census-selftest.XXXXXX)
  trap 'rm -rf -- "${work:-}"' EXIT INT TERM
```

`work` is `local`. The EXIT trap runs after the function returns, when `work` is already out of scope, so the expansion is empty.

On the previous blob (`81e716de…`) `bash -x` showed the empty removal:

```text
+ work=/tmp/mori-census-selftest.AdtWiD
+ trap 'rm -rf -- "${work:-}"' EXIT INT TERM
+ rm -rf -- ''
```

This blob runs `set +o xtrace` at `:56` before the trap is set. `bash -x "$GATE" --selftest` on `8745a4fc…` printed `+ set +o xtrace` and then no `work=` and no `rm -rf`. The trace detector is dead. The directory detector is not.

One `--selftest` on this blob exited 0 and left `/tmp/mori-census-selftest.DMHT6M` (still present at `2026-10-14T21:49:39-03:00`). Header lines 19-20 say `--selftest` writes only under that temp dir and the trap is what bounds it. The writes stay under `/tmp` (not the fleet), but each invocation leaves the tree. This seat did not patch the gate and did not delete the leftovers.

## M1 — silent write outside the fixture (scratch copy only)

**Mutant:** copy of the proved blob, one line inserted after the banner at `:566`:

```bash
printf '%s\n' "$TS_UTC" >> '/tmp/mori-idem-census/r2/canary'
```

| Bytes | sha256 |
|---|---|
| pristine / restored scratch | `8745a4fce9bfb50a654e30944847bf59d8de643228b2c1e7fd4878c0b122728b` |
| mutant | `f3853bca4dd58c495999805ede1a68b8186737b3806b8586056bff221dfb51d0` |

**Expected detector:** the proof command's write check (successful absolute mutation outside the fixture). Stdout-diff was not expected to kill this mutant.

**Output:**

| Detector | Result |
|---|---|
| two mutant runs, stdout `diff` | empty, both exit 0 — **survived** |
| mutant stdout vs pristine stdout | empty — **survived** |
| fixture manifest before vs after | empty — **survived** |
| canary after the two runs | present, 42 bytes, sha256 `ce8319bab0bd40b145d3a62b1f29f36a47a4a9596239ea10181589d7d2052848` (pinned timestamp written twice) |
| strace write check | `forbidden 1`, path `/tmp/mori-idem-census/r2/canary` — **killed** |

**Verdict:** killed by the read-only detector. Survived by stdout-diff and by `fx_no_mutation`. That is a coverage gap of a diff-only or fixture-hash-only check, not a license to change the contract. The lane file was not the mutant.

**Restoration:** scratch copy `cmp` equal to the proved blob; repeat of the fixture pair matched pristine stdout; canary absent; fixture manifest unchanged. Live gate inode, size, and mtime unchanged across the mutation (the mutant never was the live file).

## Bounded live pair (same blob, not a fixture)

Clock pinned `MORI_NOW_EPOCH=1792025368`, `MORI_ROSTER_LANES=kama`, so silence does not `find` every lane repo. Both exit 1, stderr empty. Verdict line identical:

```text
MORI_CENSUS: DRIFT (findings=10 drift=7 unavailable=0 surfaces=7)
```

This exit 1 is the gate's DRIFT code, not a probe failure. It is not this seat's census of the fleet.

The only stdout difference, on the `SURFACE cgroup` line:

```text
- current=25001836544
+ current=25001439232
```

Delta **−397312** bytes. No other line differed, so finding rows matched. `CGROUP_OOM_KILL` did not fire on the earlier blob of this same verdict shape; this pair was not re-listed id by id. A raw stdout diff still moves on `current=` when the verdict line does not.

Strace of a separate run with the same roster and a pinned clock: **0** successful writes outside `/dev` and `/proc`. The two failed mutation syscalls were `openat /dev/tty` `ENXIO` and `mkdir("/tmp/tmux-1000")` `EEXIST` (real `tmux ls` probing its socket directory; the directory already existed, and this run did not create it).

## What was not claimed

- No judge score. The live `DRIFT` line is probe output.
- No edit to `mori-census.sh`. D1 is observed landed behavior. M1 lived only in `/tmp`.
- FixtureDesign's 33-case table is a sibling contract. This proof ran the landed 14-case suite plus one quiet fixture, not that table.
- `/dev/null` and `/dev/tty` opens are process stdio, not fleet paths.
- This report does not delete leaked `/tmp/mori-census-selftest.*` trees. Deleting them would hide D1.
- A later compare of live receipts on this blob must drop or ignore `current=`. Pinning `MORI_NOW_EPOCH` froze every other line on this pair; it did not freeze `memory.current`.
- If the live file's sha256 is no longer `8745a4fc…`, this note does not cover the newer bytes. Re-run the proof command.
