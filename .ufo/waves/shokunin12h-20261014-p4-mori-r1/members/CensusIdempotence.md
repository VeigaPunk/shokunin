# CensusIdempotence — double-run proof of `tools/mori-census.sh`

**Seat:** CensusIdempotence (mutation-tester, leaf)  
**Wave:** shokunin12h-20261014-p4-mori-r1  
**Advisory:** data, not a judge verdict. Parent integrates.  
**Subject:** landed gate `mori-shokunin/tools/mori-census.sh`  
**sha256:** `7432255ff56dc69f0f2814e631961a0482e51d52f392f547de5dac42df387d3f`  
**size / mtime:** 31588 bytes, `2026-10-14 21:35:14.739 -0300` (unchanged across every run below)  
**Measured:** `2026-10-14T21:35:56-03:00` … `2026-10-14T21:38:11-03:00`  
**Host:** bash `5.3.15(1)-release`, `strace` present, kernel `7.2.3-arch1-3`  
**Write scope of this seat:** this file only. The gate was not edited. `/tmp` proof trees are harness scratch, not host fleet state.

## Axes

| Axis | What was tested |
|---|---|
| coverage | both modes the design actually has: `--selftest` (14 cases) and one frozen fixture census (`MORI_*` overrides, `MORI_NOW_EPOCH` pinned) |
| operability | one proof command, re-runnable, no oral context |
| calibration | idempotent on a frozen fixture; **not** byte-idempotent live, because `memory.current` moves. Selftest claims it deletes its temp dir; it does not. |

## Verdict of the probe

| Claim | Result |
|---|---|
| Same fixture, two census runs, stdout identical | **holds** (`diff` empty, both exit 0, `MORI_CENSUS: CLEAN`) |
| Same fixture bytes before and after both runs | **holds** (20-file sha256 manifest identical, including a third strace run) |
| `--selftest` twice, stdout identical | **holds** (both exit 0, `PASS (14 cases, 14 passed, 0 failed)`) |
| No host path opened for write during fixture census | **holds** (strace: only `/dev/null` ×22, `/dev/tty` ×5; zero non-`/dev` mutations) |
| No host path opened for write during `--selftest` | **holds** for absolute paths outside `/tmp` and `/dev` (0). Writes are the fixture builder under `/tmp/mori-census-selftest.*` |
| No host path opened for write during bounded live census | **holds** (`MORI_ROSTER_LANES=kama`, strace: 6198 read `openat`, 68 mutation events, **0** absolute writes outside `/dev` `/proc` `/tmp`) |
| Selftest removes its temp dir | **fails** — see defect D1 |
| Live stdout byte-identical across two runs | **fails** — see defect D2 (payload only; verdict and finding ids stable) |

## Proof command

Run from anywhere. Writes only under `/tmp` (the fixture, two stdout files, `strace` log). Does not write the fleet tree.

```bash
GATE=/home/vgpnk/Projects/shokunin/mori-shokunin/tools/mori-census.sh
PROOF=$(mktemp -d /tmp/mori-idem-proof.XXXXXX)
FX=$(mktemp -d /tmp/mori-idem-fx.XXXXXX)

mkdir -p "$FX/ufo/state" "$FX/ufo/waves/wave-settled" "$FX/stub" \
  "$FX/cgroup" "$FX/lanes/kagi-shokunin" "$FX/root" "$FX/bin"
printf '2026-10-14T12:00:00Z tick=1\n' > "$FX/ufo/watchdog.log"
printf '1\n' > "$FX/ufo/state/kagi.round"
printf 'mission-x\n' > "$FX/ufo/state/kagi.mission"
printf '{}\n' > "$FX/ufo/waves/wave-settled/swarm-registry.json"
printf '{}\n' > "$FX/ufo/waves/wave-settled/dispatch.json"
printf '{"schema":"ufo-swarm-results-v1","members":[]}\n' > "$FX/ufo/waves/wave-settled/results.json"
printf 'low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\noom_group_kill 0\n' > "$FX/cgroup/memory.events"
printf '123456\n' > "$FX/cgroup/memory.current"
printf 'MemAvailable: 20000000 kB\n' > "$FX/meminfo"
printf '1234 bash scripts/shokunin-watchdog.sh\n' > "$FX/stub/pgrep"
printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\n/dev/fx 1000000 10000 990000 2%% /fx\n' > "$FX/stub/df"
: > "$FX/stub/journal"
printf 'sess: 1 windows\n' > "$FX/stub/tmux"
printf '1700000000\n' > "$FX/stub/git"
printf 'x\n' > "$FX/lanes/kagi-shokunin/LOG.md"
touch -d @1700000000 "$FX/ufo/watchdog.log" "$FX/lanes/kagi-shokunin/LOG.md" \
  "$FX/ufo/waves/wave-settled/"*
for c in pgrep df journalctl tmux git; do
  printf '#!/bin/sh\ncat "$MORI_FIXTURE/stub/%s"\n' "$c" > "$FX/bin/$c"
  chmod +x "$FX/bin/$c"
done

fx_manifest() { find "$1" -type f -exec sha256sum {} + | LC_ALL=C sort; }
fx_manifest "$FX" > "$PROOF/before.txt"

runfx() {
  env -i PATH="$FX/bin:/usr/bin:/bin" HOME=/tmp MORI_FIXTURE="$FX" \
    MORI_SHOKUNIN_ROOT="$FX/root" MORI_UFO_DIR="$FX/ufo" \
    MORI_WATCHDOG_LOG="$FX/ufo/watchdog.log" MORI_STATE_DIR="$FX/ufo/state" \
    MORI_WAVES_DIR="$FX/ufo/waves" \
    MORI_CGROUP_EVENTS="$FX/cgroup/memory.events" \
    MORI_CGROUP_CURRENT="$FX/cgroup/memory.current" \
    MORI_MEMINFO="$FX/meminfo" \
    MORI_DF_BIN="$FX/bin/df" MORI_PGREP_BIN="$FX/bin/pgrep" \
    MORI_JOURNALCTL_BIN="$FX/bin/journalctl" MORI_TMUX_BIN="$FX/bin/tmux" \
    MORI_GIT_BIN="$FX/bin/git" MORI_DISK_TARGETS="$FX/root" \
    MORI_ROSTER_LANES=kagi MORI_NOW_EPOCH=1700000000 \
    MORI_WATCHDOG_STALE_S=900 MORI_WAVE_UNSETTLED_S=7200 \
    MORI_DISK_WARN_PCT=85 MORI_DISK_CRIT_PCT=95 MORI_LANE_SILENCE_S=7200 \
    bash "$GATE"
}

runfx > "$PROOF/run1.out" 2>"$PROOF/run1.err"; echo $? > "$PROOF/run1.rc"
runfx > "$PROOF/run2.out" 2>"$PROOF/run2.err"; echo $? > "$PROOF/run2.rc"
fx_manifest "$FX" > "$PROOF/after.txt"

diff -u "$PROOF/run1.out" "$PROOF/run2.out"   # empty
diff -u "$PROOF/before.txt" "$PROOF/after.txt" # empty
cmp "$PROOF/run1.rc" "$PROOF/run2.rc"         # both contain 0

strace -f -e trace=openat,creat,mkdir,mkdirat,unlink,unlinkat,rename,renameat \
  -o "$PROOF/strace.txt" \
  env -i PATH="$FX/bin:/usr/bin:/bin" HOME=/tmp MORI_FIXTURE="$FX" \
    MORI_SHOKUNIN_ROOT="$FX/root" MORI_UFO_DIR="$FX/ufo" \
    MORI_WATCHDOG_LOG="$FX/ufo/watchdog.log" MORI_STATE_DIR="$FX/ufo/state" \
    MORI_WAVES_DIR="$FX/ufo/waves" \
    MORI_CGROUP_EVENTS="$FX/cgroup/memory.events" \
    MORI_CGROUP_CURRENT="$FX/cgroup/memory.current" \
    MORI_MEMINFO="$FX/meminfo" \
    MORI_DF_BIN="$FX/bin/df" MORI_PGREP_BIN="$FX/bin/pgrep" \
    MORI_JOURNALCTL_BIN="$FX/bin/journalctl" MORI_TMUX_BIN="$FX/bin/tmux" \
    MORI_GIT_BIN="$FX/bin/git" MORI_DISK_TARGETS="$FX/root" \
    MORI_ROSTER_LANES=kagi MORI_NOW_EPOCH=1700000000 \
    bash "$GATE" >/dev/null
# host-write check: absolute mutation paths other than /dev and /proc
python3 - "$PROOF/strace.txt" << 'PY'
import sys
bad=[]
for line in open(sys.argv[1], errors="replace"):
    if '"' not in line: continue
    mut = ("openat(" in line and any(k in line for k in ("O_WRONLY","O_RDWR","O_CREAT","O_APPEND","O_TRUNC"))) or any(k in line for k in ("mkdir(","unlink","rename"))
    if not mut: continue
    path=line.split('"',2)[1]
    if path.startswith("/dev/") or path.startswith("/proc/"): continue
    bad.append(path)
print("nondev_mutations", len(bad))
sys.exit(1 if bad else 0)
PY
```

**Observed on this run** (`FX=/tmp/mori-idem-fx-landed.sORgQg`):

| Check | Observed |
|---|---|
| `run1.rc` / `run2.rc` | `0` / `0` |
| stdout sha256 run1 | `c391937ff43805b5d3cca06bf5957555e97796b3bc5dd1145aca81ea4355d9ba` |
| stdout sha256 run2 | same |
| `diff` stdout | empty |
| fixture manifest sha256 before | `60aed7bf6dd19db85d9396f74ed75dfc4424e1035704eb0755521fa28b4666f5` (20 files) |
| fixture manifest sha256 after two runs **and** after strace | same |
| strace mutations not under `/dev` | `0` (`/dev/null` 22, `/dev/tty` 5) |
| stderr | 0 bytes both runs |
| gate sha256 after | still `7432255f…df387d3f` |

Verdict line both times:

```text
MORI_CENSUS: CLEAN (findings=0 drift=0 unavailable=0 surfaces=7)
```

`measured_at` inside the surface lines is `ts=2023-11-14T22:13:20Z` because `MORI_NOW_EPOCH=1700000000`. Without that pin the two stdouts would differ by the clock even when every finding is identical.

## `--selftest` double run (same gate)

```bash
bash "$GATE" --selftest > /tmp/mori-st1.out
bash "$GATE" --selftest > /tmp/mori-st2.out
diff -u /tmp/mori-st1.out /tmp/mori-st2.out   # empty
```

Observed `2026-10-14T21:35:56-03:00`: both exit `0`, stdout sha256 both `33225c2ecce32431c8a96d07863aa6cc203e3bd4280eb69225769bb05e009118`, last line:

```text
MORI_CENSUS_SELFTEST: PASS (14 cases, 14 passed, 0 failed)
```

Cases (all `PASS`): `clean: all quiet`, `WATCHDOG_ABSENT`, `WATCHDOG_STALE`, `WAVE_UNSETTLED_AGE`, `unsettled young wave does not fire`, `OOM_KILL_JOURNAL`, `CGROUP_OOM_KILL`, `DISK_CRITICAL`, `disk under warn`, `LANE_SILENT`, `CGROUP_UNAVAILABLE is not DRIFT`, `empty journal`, `cli: unknown arg exit 2`, `cli: --help exit 0`.

Per-case fixture digest is enforced inside the gate (`fx_hash` / `fx_no_mutation` at `tools/mori-census.sh:549-554` and the call at `:672`). That check passed for all 14; it does **not** cover the temp dir leaking after exit (D1).

A `strace -f -e trace=openat,creat,mkdir,mkdirat,unlink,unlinkat,rename,renameat` of `--selftest` (`/tmp/mori-census-selftest.fV6kzl`): **0** absolute mutation paths outside `/tmp` and `/dev`. Relative `mkdir("fx")` / `mkdir("ufo")` lines are components of that same temp tree (mkdir follows cwd). One `unlinkat(AT_FDCWD, "", 0) = ENOENT` is the broken cleanup in D1, not a host unlink.

Host metadata across the two selftest runs (inode, mtime, size): `.ufo/watchdog.log`, `.ufo/state`, `mori-shokunin/tools/mori-census.sh` unchanged. The `diff` of the snapshot files differs only in the `TAG before` / `TAG after` label line.

## D1 — selftest temp dir survives (killed)

**Site:** `mori-shokunin/tools/mori-census.sh:511-513`

```bash
run_selftest() {
  local work bin FX PASS=0 FAIL=0
  work=$(mktemp -d /tmp/mori-census-selftest.XXXXXX)
  trap 'rm -rf -- "${work:-}"' EXIT INT TERM
```

`work` is `local` to `run_selftest`. The EXIT trap runs after the function returns, when `work` is already out of scope, so the expansion is empty.

**Detector:** `bash -x "$GATE" --selftest`. Trace tail:

```text
+ work=/tmp/mori-census-selftest.TgGK1m
+ trap 'rm -rf -- "${work:-}"' EXIT INT TERM
...
+ return
+ rm -rf -- ''
```

Directory count under `/tmp/mori-census-selftest.*`: 10 before that trace, 11 after. `fuser` showed no holder. The suite still printed `PASS` and exited 0 — the leak is outside the case asserts.

**Minimal repro** (same bash 5.3.15), not the gate:

```text
inside work=/tmp/mori-trap-repro.A7wvsh
TRAP work=EMPTY
```

and the directory remained.

Header comment at `:19-20` says `--selftest` writes only under `/tmp/mori-census-selftest.XXXXXX` and the trap is what was supposed to bound that. The writes stay under `/tmp` (not the fleet), but each invocation **leaves** the tree. That is a write the design said it would undo. Not a remediation: this seat did not patch the gate and did not delete the leftovers.

**Fix the parent should land (not applied here):** set the trap variable in the global scope, or `rm -rf -- "$work"` before `run_selftest` returns, and add a selftest assert that the directory is gone after a nested run. A case that only hashes the fixture will not catch this.

## D2 — live stdout is not byte-idempotent (survived as a finding-id compare; killed as byte-diff)

Two live runs with `MORI_ROSTER_LANES=kama` (so silence does not `find` the whole fleet), both exit 1:

```text
MORI_CENSUS: DRIFT (findings=10 drift=9 unavailable=0 surfaces=7)
```

After stripping `ts=` and `age_s=`, the only diff is `memory.current`:

```text
- current=25924329472
+ current=25932652544
```

on both the `SURFACE cgroup` line and `FINDING CGROUP_OOM_KILL`. Finding id set did not change. `oom_kill=1` was stable across the pair.

So: compare-by-id is idempotent on this sample; compare-by-raw-stdout is not, because the gate prints the live counter. Frozen `MORI_NOW_EPOCH` does not freeze `memory.current`. A later diff of receipts must drop or bin `current=` (FindingIds already calls pid/free-bytes/timestamps volatile). This is not a license to change the contract; it is the coverage gap if someone diffs stdout bytes.

Strace of that bounded live run: **0** host write paths. The earlier unbounded live strace (default roster, `find` over every lane repo) was killed by the harness at ~30s after 228070 read-only `openat`s and **0** host writes; it had printed only the banner line. Silence's `find "$repo" -type f` (`:436`) is a read walk, not a write, and it is large enough that an unbounded `strace -f` is the wrong proof tool.

## What was not claimed

- No judge score. No CLEAN/DRIFT verdict for the fleet beyond the two bounded live lines quoted above (those are probe output, not this seat's census).
- No edit to `mori-census.sh`. D1 is a killed mutant of the cleanup trap; the bytes stay as landed.
- FixtureDesign's 33-case table is a sibling contract. The landed gate's suite is 14 cases. This proof runs the landed suite plus one quiet fixture shaped like `fx_quiet`, not the 33-case table.
- `/dev/null` and `/dev/tty` opens are process stdio, not fleet paths.
- This report does not delete the leaked `/tmp/mori-census-selftest.*` trees. Deleting them would hide D1.

## Restoration

Gate bytes before and after: sha256 `7432255ff56dc69f0f2814e631961a0482e51d52f392f547de5dac42df387d3f`, inode `11549680`, size `31588`. Nothing to restore; the subject was never mutated. Proof scratch lives under `/tmp/mori-idem-census/` and `/tmp/mori-idem-fx-landed.sORgQg` and is disposable.
