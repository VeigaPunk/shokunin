# CensusIdempotence — double-run proof of `tools/mori-census.sh`

**Seat:** CensusIdempotence (mutation-tester, leaf). Advisory data, not a judge verdict. Parent integrates.
**Wave:** shokunin12h-20261014-p4-mori-r1
**Subject:** landed gate `mori-shokunin/tools/mori-census.sh`
**sha256:** `81e716de978a9540f9d310309d83660bb196650aa1ab809ae6fd6ee3cc4bfba9`
**size / inode / mtime:** 36844 bytes, inode `11550470`, `2026-10-14 21:44:46.158413662 -0300`
**Measured:** `2026-10-14T21:46:07-03:00` … `2026-10-14T21:47:38-03:00`
**Host:** bash `5.3.15(1)-release`, `strace` present
**Write scope of this seat:** this file only. The gate was not edited. `/tmp` trees are harness scratch, not fleet state.

The gate file moved several times while this seat was measuring (observed blobs `7432255f…`, `8e655187…`, `580a0e31…`, then this one). The numbers below are for `81e716de…` only. That hash matched the live file at the start of the fixture proof, at the end of it, and again at `2026-10-14T21:47:38-03:00`. An earlier draft of this note cited `7432255f…`; that draft is withdrawn.

## Axes

| Axis | What was tested |
|---|---|
| coverage | one frozen fixture, twice; `--selftest` twice; one bounded live pair (`MORI_ROSTER_LANES=kama`, clock pinned); one scratch mutation of the read-only claim |
| operability | proof command below, no oral context, no fleet write |
| calibration | same-fixture stdout is idempotent; live stdout is not, and the only mover on this pair is `current=`. Selftest's own hash check does not see a write outside the fixture, and its cleanup trap does not run. |

## Probe result

| Claim | Result |
|---|---|
| Same fixture, two census runs, stdout identical | **holds** (both exit 0, `diff` empty) |
| Same fixture bytes before and after those runs and a third strace run | **holds** (21-file manifest identical) |
| No successful host write during the fixture census | **holds** (strace: 0 forbidden paths) |
| `--selftest` twice, harness stdout identical | **holds** (both exit 0, 14/14 PASS) |
| No successful host write during `--selftest` | **holds** for absolute paths outside the temp dir (0). Writes are the fixture builder. The temp dir is not removed (D1). |
| No successful host write during bounded live census | **holds** (strace: 0 forbidden paths) |
| Live stdout byte-identical under a pinned clock | **fails** — only `current=` moved (+344064). Verdict line and finding rows did not. |
| Selftest removes its temp dir | **fails** — D1 |
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

`MORI_CGROUP_LOCAL_EVENTS` and `MORI_CGROUP_SERVICE_EVENTS` have to be set. If they are not, the gate falls through to `/sys/fs/cgroup/user.slice/user-$(id -u).slice/user@$(id -u).service/memory.events` (`tools/mori-census.sh:381`) and the run is no longer a frozen fixture.

## Observed on this run

`FX=/tmp/mori-idem-fx.Cd6qRG`. Gate sha256 before and after: `81e716de978a9540f9d310309d83660bb196650aa1ab809ae6fd6ee3cc4bfba9`.

| Check | Observed |
|---|---|
| `run1.rc` / `run2.rc` | `0` / `0` |
| stdout sha256, both runs | `f1bee63e559f01cef1c03b46ec3d33a7c7c8eab23e915910c3a5ea35c355246c` |
| stdout `diff` | empty |
| stderr | 0 bytes both runs |
| fixture manifest sha256 before, after two runs, and after strace | `d6081403e20709ad7f7105005e9ea66c18297c9fc822b56e20f91b39ea31fe15` (21 files) |
| strace successful writes outside the fixture | `0` |
| strace successful `/dev` opens | 30 (`/dev/null`, `/dev/tty`) |
| strace failed mutation syscalls | 5, all `openat /dev/tty` `ENXIO` (no tty under `strace`) |
| `.ufo/watchdog.log` inode/size/mtime across the proof | unchanged (`9822068`, 19396, `2026-10-13 16:44:48.524 -0300`) |

Verdict line both times:

```text
MORI_CENSUS: CLEAN (findings=0 drift=0 unavailable=0 surfaces=7)
```

`ts=` is `2023-11-14T22:13:20Z` because `MORI_NOW_EPOCH=1700000000`. Without that pin the two stdouts differ by the clock even when every finding is identical.

Surface row that the pin does **not** freeze:

```text
SURFACE cgroup: ok (... current=refused:outside-sysfs-cgroup; ts=2023-11-14T22:13:20Z)
```

`tools/mori-census.sh:403-409` refuses `MORI_CGROUP_CURRENT` unless the path is under `/sys/fs/cgroup/`, and does not read the file. The fixture file `memory.current` containing `123456` was not printed. Both runs print the same refusal, so the pair is still idempotent. A fixture of this shape cannot prove that a numeric `current=` is stable. That measurement is the live pair below.

Journal stub must be named `stub/journalctl` (the dispatcher `cat`s `$MORI_FIXTURE/stub/$name`). A file named `stub/journal` makes `cat` exit 1; the gate treats rc 1 as an empty journal and still prints CLEAN. This run used the matching name and recorded `rc=0`.

## `--selftest` double run (same gate)

```bash
bash --noprofile --norc "$GATE" --selftest > /tmp/mori-st1.out
bash --noprofile --norc "$GATE" --selftest > /tmp/mori-st2.out
diff -u /tmp/mori-st1.out /tmp/mori-st2.out   # empty
```

Observed `2026-10-14T21:46:07-03:00`: both exit `0`, harness stdout sha256 both `33225c2ecce32431c8a96d07863aa6cc203e3bd4280eb69225769bb05e009118`, last line:

```text
MORI_CENSUS_SELFTEST: PASS (14 cases, 14 passed, 0 failed)
```

That hash is the PASS/FAIL harness text, not the inner census receipts. It matched an earlier blob's harness text too; it is not evidence that inner receipts are stable across gate edits.

Cases, all `PASS`: `clean: all quiet`, `WATCHDOG_ABSENT`, `WATCHDOG_STALE`, `WAVE_UNSETTLED_AGE`, `unsettled young wave does not fire`, `OOM_KILL_JOURNAL`, `CGROUP_OOM_KILL`, `DISK_CRITICAL`, `disk under warn`, `LANE_SILENT`, `CGROUP_UNAVAILABLE is not DRIFT`, `empty journal`, `cli: unknown arg exit 2`, `cli: --help exit 0`.

`fx_no_mutation` (`:624`, called at `:726`) hashes the case fixture and passed for all 14. It does not see a write outside that fixture, and it does not see the temp dir surviving (D1).

`strace` of one `--selftest` (`/tmp/mori-census-selftest.pNiAXU`): **0** successful absolute writes outside that directory and `/dev`. 125 successful relative `mkdir`/`openat` names (`bin`, `fx`, `cgroup`, `state`, …) are `mkdir -p` component walks: the trace shows `mkdir("/tmp")` `EEXIST`, then `mkdir("mori-census-selftest.pNiAXU")` `EEXIST`, then `mkdir("bin")` `= 0`. `/tmp/bin` does not exist. The leaked tree contains `bin/` and `fx/`. Failed syscalls (560) are not writes; they include `mkdir("/tmp")` `EEXIST` and the empty `rm` in D1.

## D1 — selftest temp dir survives

**Site:** `mori-shokunin/tools/mori-census.sh:585-587`

```bash
run_selftest() {
  local work bin FX PASS=0 FAIL=0
  work=$(mktemp -d /tmp/mori-census-selftest.XXXXXX)
  trap 'rm -rf -- "${work:-}"' EXIT INT TERM
```

`work` is `local`. The EXIT trap runs after the function returns, when `work` is already out of scope, so the expansion is empty.

**Detector:** `bash -x "$GATE" --selftest`. Trace tail:

```text
+ work=/tmp/mori-census-selftest.AdtWiD
+ trap 'rm -rf -- "${work:-}"' EXIT INT TERM
+ rm -rf -- ''
```

`/tmp/mori-census-selftest.AdtWiD` was still present after the trace (`bin/`, `fx/`). The suite still printed `PASS` and exited 0. Header lines 19-20 say `--selftest` writes only under that temp dir and the trap is what bounds it. The writes stay under `/tmp` (not the fleet), but each invocation leaves the tree. This seat did not patch the gate and did not delete the leftovers.

## M1 — silent write outside the fixture (scratch copy only)

**Mutant:** copy of the proved blob, one line inserted after the banner at `:559`:

```bash
printf '%s\n' "$TS_UTC" >> '/tmp/mori-idem-census/r2/canary'
```

| Bytes | sha256 |
|---|---|
| pristine / restored scratch | `81e716de978a9540f9d310309d83660bb196650aa1ab809ae6fd6ee3cc4bfba9` |
| mutant | `db175b0a6df3080e1d2c020f8ac69d342e5a24bdfba62dfa5d0dc50a1f14bb8d` |

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

Clock pinned `MORI_NOW_EPOCH=1792025194` (`ts=2026-10-15T00:46:34Z`), `MORI_ROSTER_LANES=kama`, so silence does not `find` every lane repo. Both exit 1, stderr empty. Verdict line identical:

```text
MORI_CENSUS: DRIFT (findings=10 drift=7 unavailable=0 surfaces=7)
```

This exit 1 is the gate's DRIFT code, not a probe failure. It is not this seat's census of the fleet.

The only stdout difference:

```text
- current=25050161152
+ current=25050505216
```

Delta **+344064** bytes, on the `SURFACE cgroup` line only. Finding rows matched, including `script_sha256=81e716de978a9540f9d310309d83660bb196650aa1ab809ae6fd6ee3cc4bfba9` on each. Ids in emission order: `WATCHDOG_STALE`, `WATCHDOG_ABSENT`, `WAVE_UNSETTLED_AGE` ×4 (`shokunin-train-20261013`, `-w2`, `-w3`, `-w4`), `OOM_KILL_JOURNAL`, `SEGFAULT_JOURNAL`, `UNIT_FAILURE_OUT_OF_SCOPE`, `CGROUP_OOM_KILL_CUMULATIVE`. `CGROUP_OOM_KILL` did not fire; the surface stayed `ok` with parent `oom_kill=1` and the cumulative finding at info. So on this blob a raw stdout diff moves on `current=` even when the finding set does not, and the moving field is not inside a finding row.

Strace of a third run with the same pin and roster: **0** successful writes outside `/dev` and `/proc`. The two failed mutation syscalls were `openat /dev/tty` `ENXIO` and `mkdir("/tmp/tmux-1000")` `EEXIST` (real `tmux ls` probing its socket directory; the directory already existed, and this run did not create it).

## What was not claimed

- No judge score. The live `DRIFT` line is probe output.
- No edit to `mori-census.sh`. D1 is observed landed behavior. M1 lived only in `/tmp`.
- FixtureDesign's 33-case table is a sibling contract. This proof ran the landed 14-case suite plus one quiet fixture, not that table.
- `/dev/null` and `/dev/tty` opens are process stdio, not fleet paths.
- This report does not delete leaked `/tmp/mori-census-selftest.*` trees. Deleting them would hide D1.
- A later compare of live receipts on this blob must drop or ignore `current=`. Pinning `MORI_NOW_EPOCH` froze `ts=` and `age_s=` on this pair; it did not freeze `memory.current`.
