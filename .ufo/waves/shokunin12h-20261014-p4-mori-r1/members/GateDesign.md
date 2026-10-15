# GateDesign — `tools/mori-census.sh`

**Member:** GateDesign (executor) · **Wave:** shokunin12h-20261014-p4-mori-r1  
**Lane:** mori-shokunin (shonen probation r1) · **Role:** design only — parent lands the file  
**Axes:** coverage · operability · calibration  
**Measured:** 2026-10-15T00:28:58Z (UTC) · host read-only; no remediation

---

## 1. Contract (from SKILL.md + wave)

| Item | Value |
|---|---|
| Path | `mori-shokunin/tools/mori-census.sh` |
| Modes | default `verify` (live) · `--selftest` (hermetic) · `--help` |
| Verdict line | `MORI_CENSUS: CLEAN\|DRIFT (…counts…)` |
| Exit | `0` CLEAN · `1` DRIFT · `2` setup/usage |
| Write scope | **selftest temp dir only** (`mktemp -d /tmp/mori-census-selftest.XXXXXX`); live mode creates **zero** files |
| Remediation | **none** — detect and report only (PROVINCE.md) |
| Secrets | shape-only; never opens `credentials/`, `oauth/`, `server.token`, `op.env`, session payloads |

### Surfaces (six families + optional tmux)

| # | Surface | Primary probes (live) | DRIFT finding ids (stable) |
|---|---|---|---|
| 1 | Watchdog liveness | `pgrep -af shokunin-watchdog` · `stat` on `.ufo/watchdog.log` · `.ufo/state/*.round` | `WATCHDOG_ABSENT` · `WATCHDOG_STALE` · `WATCHDOG_LOG_UNAVAILABLE` |
| 2 | Wave settlement | `.ufo/waves/*/{swarm-registry,dispatch,run,results,closeout,task-response}.json` | `WAVE_UNSETTLED_AGE` |
| 3 | Kill/OOM journal | `journalctl --user -b` greps (class counts only) | `OOM_KILL_JOURNAL` · `KILL_SIGNAL_JOURNAL` · `SEGFAULT_JOURNAL` · `UNIT_FAILURE_JOURNAL` |
| 4 | Cgroup memory | `memory.events` / `memory.current` under user slice | `CGROUP_OOM_KILL` · `CGROUP_UNAVAILABLE`† |
| 5 | Disk runway | `df -P` on fleet root + `/tmp` + optional scratch | `DISK_LOW` · `DISK_CRITICAL` · `DISK_UNAVAILABLE`† |
| 6 | Lane silence | HEAD time vs newest non-`.git` mtime vs report dir (PROTOCOL.md:158-167) | `LANE_SILENT` |
| 7 | tmux (optional) | `tmux ls` | informational only — absence → `unavailable`, not DRIFT |

† `*_UNAVAILABLE` is **observation**, never rolled into DRIFT by itself (unavailable ≠ unhealthy).

### CLEAN vs DRIFT (calibration)

- **CLEAN** — every readable surface answers; no severity-bearing finding id is raised. `unavailable` rows and pure observation lines do not flip the rollup.
- **DRIFT** — one or more severity-bearing findings fired (table above without the † rows).
- **Exit 2** — bad CLI, selftest harness failure, or required override path unusable in a way that means the gate itself cannot run (usage/setup). A live missing optional surface is **not** exit 2.

### Thresholds (proposal-marked where evidence-thin)

| Knob | Default | Env override | Basis |
|---|---|---|---|
| Watchdog log stale | 900 s (2× tick 450 s from `scripts/shokunin-watchdog.sh`) | `MORI_WATCHDOG_STALE_S` | driver INTERVAL=450 |
| Wave unsettled age | 7200 s | `MORI_WAVE_UNSETTLED_S` | proposal — long enough to outlive a normal wave; parent may retune |
| Disk warn / critical | 85% / 95% used | `MORI_DISK_WARN_PCT` / `MORI_DISK_CRIT_PCT` | proposal — no fleet write-rate evidence yet (DiskThresholds peer) |
| Lane silence window | 7200 s | `MORI_LANE_SILENCE_S` | aligned with PROTOCOL two-tick spirit; commit sparsity ≠ silence |
| Journal classes that DRIFT | oom_kill, kill_signal (segfault/unit_failure = observe-only in r1) | fixed | mint demand = undetected OOM death |

---

## 2. Output shape (stable for later compare)

```
mori-census census-r1 — ts=<ISO8601Z> — mode=live|fixture — read-only
SURFACE watchdog: <ok|drift|unavailable> (cmd=…; …)
SURFACE waves: …
SURFACE journal: …
SURFACE cgroup: …
SURFACE disk: …
SURFACE silence: …
SURFACE tmux: …
FINDING <ID> severity=<info|warn|crit> obs=<one-line observation>
…
MORI_CENSUS: CLEAN|DRIFT (findings=N drift=M unavailable=U surfaces=S)
```

Every `SURFACE` / `FINDING` line is one observation. Inference (e.g. “wedged”) is never printed as fact; age numbers are raw.

---

## 3. Hermetic `--selftest`

- Creates `/tmp/mori-census-selftest.XXXXXX` only; trap removes it.
- Stubs: `pgrep`, `journalctl`, `df`, `tmux`, `git` via PATH + `MORI_*` path overrides.
- Fixture tree holds synthetic `.ufo/`, cgroup files, meminfo, journal text, disk table.
- Each case asserts: exit code · final `MORI_CENSUS:` verdict · at least one finding id (or its absence) · fixture tree sha256 unchanged after the run.
- Minimum cases (FixtureDesign peer expands): clean all-quiet · watchdog absent · watchdog stale · wave unsettled aged · journal OOM · cgroup oom_kill · disk critical · lane silent · unavailable-not-drift · CLI usage exit 2 · mutation-free.

---

## 4. Boundary refusals (enforced in script)

| Refusal | Enforcement |
|---|---|
| No restart/kill/reparent | no `kill`, `systemctl`, `tmux kill-*`, no writes to pid files |
| No pacman/systemd ownership | journal/cgroup read as **fleet evidence** only; no package queries |
| No dispatch | never calls `ufo-sighting` / launch helpers |
| No external fetch | no curl/wget/network |
| No secret read | path allowlist; no `credentials`, `op.env`, `server.token` |
| Selftest write fence | only under `$work` temp dir; `fx_no_mutation` after every case |

---

## 5. Full script (parent lands at `mori-shokunin/tools/mori-census.sh`)

```bash
#!/usr/bin/env bash
# mori-census.sh — read-only fleet/host observability census (mori-shokunin r1).
#
# Domain: whether the fleet, its waves and its host are alive and progressing.
# Product: verdict + surface lines + stable finding ids. Never remediates.
#
# Verdict: MORI_CENSUS: CLEAN|DRIFT
# Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
#
# Surfaces:
#   watchdog  pid + .ufo/watchdog.log freshness + .ufo/state/*.round
#   waves     .ufo/waves/* settlement (registry/dispatch/run × results/closeout)
#   journal   journalctl --user -b kill/OOM class counts (this boot)
#   cgroup    memory.events / memory.current (user slice)
#   disk      df runway on fleet root + /tmp + optional scratch
#   silence   lane silent|progressing|progressing-weak (PROTOCOL.md)
#   tmux      optional session list (absence = unavailable, not DRIFT)
#
# Live mode writes nothing. --selftest writes only under
# /tmp/mori-census-selftest.XXXXXX and asserts the fixture tree is unchanged.
#
# Env overrides (selftest / operator pin); empty = live host defaults:
#   MORI_SHOKUNIN_ROOT   fleet root (default: parent of tools/../ or cwd probe)
#   MORI_UFO_DIR         default $ROOT/.ufo
#   MORI_WATCHDOG_LOG    default $UFO/watchdog.log
#   MORI_STATE_DIR       default $UFO/state
#   MORI_WAVES_DIR       default $UFO/waves
#   MORI_CGROUP_EVENTS   default user-slice memory.events path
#   MORI_CGROUP_CURRENT  default user-slice memory.current path
#   MORI_MEMINFO         default /proc/meminfo
#   MORI_DF_BIN          default df
#   MORI_PGREP_BIN       default pgrep
#   MORI_JOURNALCTL_BIN  default journalctl
#   MORI_TMUX_BIN        default tmux
#   MORI_GIT_BIN         default git
#   MORI_DISK_TARGETS    space-separated paths for df (default: ROOT /tmp)
#   MORI_WATCHDOG_STALE_S MORI_WAVE_UNSETTLED_S MORI_DISK_WARN_PCT
#   MORI_DISK_CRIT_PCT    MORI_LANE_SILENCE_S
#   MORI_ROSTER_LANES    space-separated lane ids for silence grading
#   MORI_NOW_EPOCH       pin "now" (selftest)
#   MORI_FIXTURE         selftest marker (optional)
#
# Finding ids (stable compare contract):
#   WATCHDOG_ABSENT WATCHDOG_STALE WATCHDOG_LOG_UNAVAILABLE
#   WAVE_UNSETTLED_AGE
#   OOM_KILL_JOURNAL KILL_SIGNAL_JOURNAL SEGFAULT_JOURNAL UNIT_FAILURE_JOURNAL
#   CGROUP_OOM_KILL CGROUP_UNAVAILABLE
#   DISK_LOW DISK_CRITICAL DISK_UNAVAILABLE
#   LANE_SILENT
#
set -euo pipefail

VERSION=census-r1
SELF=$(readlink -f -- "${BASH_SOURCE[0]}" 2>/dev/null || {
  p=$0
  case "$p" in /*) printf '%s' "$p" ;; *) printf '%s' "$PWD/$p" ;; esac
})
SCRIPT_DIR=$(cd -- "$(dirname -- "$SELF")" && pwd)
# tools/ -> lane root -> prefer lane's parent (shokunin root) when layout matches
LANE_ROOT=$(cd -- "$SCRIPT_DIR/.." && pwd)
DEFAULT_ROOT=$LANE_ROOT
case "$(basename -- "$LANE_ROOT")" in
  *-shokunin) DEFAULT_ROOT=$(cd -- "$LANE_ROOT/.." && pwd) ;;
esac

# ---- defaults (overridable) -------------------------------------------------
ROOT=${MORI_SHOKUNIN_ROOT:-$DEFAULT_ROOT}
UFO=${MORI_UFO_DIR:-$ROOT/.ufo}
WATCHDOG_LOG=${MORI_WATCHDOG_LOG:-$UFO/watchdog.log}
STATE_DIR=${MORI_STATE_DIR:-$UFO/state}
WAVES_DIR=${MORI_WAVES_DIR:-$UFO/waves}
CGROUP_EVENTS=${MORI_CGROUP_EVENTS:-/sys/fs/cgroup/user.slice/user-$(id -u).slice/memory.events}
CGROUP_CURRENT=${MORI_CGROUP_CURRENT:-/sys/fs/cgroup/user.slice/user-$(id -u).slice/memory.current}
MEMINFO=${MORI_MEMINFO:-/proc/meminfo}
DF_BIN=${MORI_DF_BIN:-df}
PGREP_BIN=${MORI_PGREP_BIN:-pgrep}
JOURNALCTL_BIN=${MORI_JOURNALCTL_BIN:-journalctl}
TMUX_BIN=${MORI_TMUX_BIN:-tmux}
GIT_BIN=${MORI_GIT_BIN:-git}
DISK_TARGETS=${MORI_DISK_TARGETS:-"$ROOT /tmp"}
WATCHDOG_STALE_S=${MORI_WATCHDOG_STALE_S:-900}
WAVE_UNSETTLED_S=${MORI_WAVE_UNSETTLED_S:-7200}
DISK_WARN_PCT=${MORI_DISK_WARN_PCT:-85}
DISK_CRIT_PCT=${MORI_DISK_CRIT_PCT:-95}
LANE_SILENCE_S=${MORI_LANE_SILENCE_S:-7200}
ROSTER_LANES=${MORI_ROSTER_LANES:-"protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"}

NOW_EPOCH=${MORI_NOW_EPOCH:-}
if [ -z "$NOW_EPOCH" ]; then NOW_EPOCH=$(date +%s); fi
TS_UTC=$(date -u -d "@$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -r "$NOW_EPOCH" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ)

# ---- counters / findings ----------------------------------------------------
N_FINDINGS=0
N_DRIFT=0
N_UNAVAIL=0
N_SURFACES=0
ROLL=CLEAN
declare -a FINDING_LINES=()
declare -a SURFACE_LINES=()

usage() {
  cat <<'EOF'
usage: mori-census.sh [--selftest] [--help]

  (no flags)   live read-only census over fleet/host observability surfaces
  --selftest   hermetic fixture-tree proof (writes only under
               /tmp/mori-census-selftest.*); exit 0 pass, 1 fail
  --help       this text

Verdict: MORI_CENSUS: CLEAN|DRIFT (findings=N drift=M unavailable=U surfaces=S)
Exit:    0 CLEAN | 1 DRIFT | 2 setup/usage
Read-only: live mode creates no files; never remediates.
EOF
}

die_usage() { printf 'mori-census: %s\n' "$1" >&2; usage >&2; exit 2; }

# severity: info does not flip ROLL; warn|crit flips to DRIFT
emit_finding() { # id severity observation
  local id=$1 sev=$2 obs=$3
  N_FINDINGS=$((N_FINDINGS + 1))
  FINDING_LINES+=("FINDING $id severity=$sev obs=$obs")
  case "$sev" in
    warn|crit)
      N_DRIFT=$((N_DRIFT + 1))
      ROLL=DRIFT
      ;;
  esac
}

emit_surface() { # name state detail
  local name=$1 state=$2 detail=$3
  N_SURFACES=$((N_SURFACES + 1))
  SURFACE_LINES+=("SURFACE $name: $state ($detail)")
  if [ "$state" = unavailable ]; then
    N_UNAVAIL=$((N_UNAVAIL + 1))
  fi
}

have() { command -v "$1" >/dev/null 2>&1; }

cap() { # run read-only; capture stdout+stderr + rc without set -e trip
  set +e
  CAP_OUT=$("$@" 2>&1)
  CAP_RC=$?
  set -e
}

read_file() { # first line or empty
  local f=$1
  [ -r "$f" ] || return 0
  head -n1 -- "$f" 2>/dev/null | tr -d '\r' || true
}

cgroup_field() { # file key -> value
  local f=$1 k=$2
  [ -r "$f" ] || return 0
  awk -v key="$k" '$1 == key { print $2; exit }' "$f" 2>/dev/null || true
}

epoch_mtime() {
  local f=$1
  stat -c %Y -- "$f" 2>/dev/null || stat -f %m -- "$f" 2>/dev/null || printf ''
}

# ---- surface: watchdog ------------------------------------------------------
probe_watchdog() {
  local detail pids pid_n log_state age= stale=0 cmd_bits=''
  cmd_bits="pgrep -af shokunin-watchdog; stat $WATCHDOG_LOG; ls $STATE_DIR"

  pid_n=0
  pids=''
  if have "$PGREP_BIN" || [ -x "$PGREP_BIN" ]; then
    cap "$PGREP_BIN" -af shokunin-watchdog
    # Filter the pgrep line itself and empty
    pids=$(printf '%s\n' "$CAP_OUT" | grep -E 'shokunin-watchdog' | grep -vF 'pgrep' || true)
    if [ -n "$pids" ]; then
      pid_n=$(printf '%s\n' "$pids" | grep -c . || true)
    fi
  else
    emit_surface watchdog unavailable "cmd=$cmd_bits; pgrep=missing; ts=$TS_UTC"
    emit_finding WATCHDOG_LOG_UNAVAILABLE info "pgrep binary missing — cannot assess pid"
    # still try log
  fi

  if [ ! -e "$WATCHDOG_LOG" ]; then
    log_state=missing
    emit_finding WATCHDOG_LOG_UNAVAILABLE info "watchdog.log absent path=$WATCHDOG_LOG"
  elif [ ! -r "$WATCHDOG_LOG" ]; then
    log_state=unreadable
    emit_finding WATCHDOG_LOG_UNAVAILABLE info "watchdog.log unreadable path=$WATCHDOG_LOG"
  else
    log_state=ok
    age=$((NOW_EPOCH - $(epoch_mtime "$WATCHDOG_LOG")))
    if [ "$age" -gt "$WATCHDOG_STALE_S" ]; then
      stale=1
      emit_finding WATCHDOG_STALE warn "watchdog.log mtime_age_s=$age threshold_s=$WATCHDOG_STALE_S path=$WATCHDOG_LOG"
    fi
  fi

  local state_n=0
  if [ -d "$STATE_DIR" ]; then
    state_n=$(find "$STATE_DIR" -maxdepth 1 -type f -name '*.round' 2>/dev/null | wc -l | tr -d ' ')
  fi

  if [ "$pid_n" -eq 0 ]; then
    emit_finding WATCHDOG_ABSENT warn "no shokunin-watchdog process matched by pgrep -af"
  fi

  local st=ok
  if [ "$pid_n" -eq 0 ] || [ "$stale" -eq 1 ]; then st=drift; fi
  if [ "$log_state" = missing ] || [ "$log_state" = unreadable ]; then
    # log missing alone is unavailable if we also lack pids assessment path
    if [ "$pid_n" -eq 0 ] && [ "$log_state" != ok ]; then st=drift; fi
  fi

  detail="cmd=$cmd_bits; pids=$pid_n; log=$log_state; age_s=${age:-?}; stale_threshold_s=$WATCHDOG_STALE_S; state_rounds=$state_n; ts=$TS_UTC"
  emit_surface watchdog "$st" "$detail"
}

# ---- surface: waves ---------------------------------------------------------
# Settlement join (r1):
#   train-style: swarm-registry.json + dispatch.json + (results.json|closeout.json)
#   12h-style:   run.json + task-response.json + optional results.json
# Settled if results.json OR closeout.json OR mission-result.json exists.
# Dispatched-but-unsettled if registry|dispatch|run present and no settle file.
# Age = NOW - newest file mtime in the wave dir (observation only).
# Unsettled + age > WAVE_UNSETTLED_S => WAVE_UNSETTLED_AGE (DRIFT).
# Never call unsettled "failed".
probe_waves() {
  local cmd="find $WAVES_DIR -maxdepth 1 -mindepth 1 -type d"
  local n_total=0 n_settled=0 n_unsettled=0 n_empty=0 n_aged=0
  local d base has_reg has_disp has_run has_settle newest age st

  if [ ! -d "$WAVES_DIR" ]; then
    emit_surface waves unavailable "cmd=$cmd; waves_dir=missing path=$WAVES_DIR; ts=$TS_UTC"
    return 0
  fi

  st=ok
  for d in "$WAVES_DIR"/*; do
    [ -d "$d" ] || continue
    base=$(basename -- "$d")
    case "$base" in round-*|.*) continue ;; esac
    n_total=$((n_total + 1))
    has_reg=0 has_disp=0 has_run=0 has_settle=0
    [ -f "$d/swarm-registry.json" ] && has_reg=1
    [ -f "$d/dispatch.json" ] && has_disp=1
    [ -f "$d/run.json" ] && has_run=1
    [ -f "$d/results.json" ] || [ -f "$d/closeout.json" ] || [ -f "$d/mission-result.json" ] && has_settle=1

    newest=$(find "$d" -type f -printf '%T@\n' 2>/dev/null | sort -n | tail -1 | cut -d. -f1)
    age=0
    if [ -n "${newest:-}" ]; then age=$((NOW_EPOCH - newest)); fi

    if [ "$has_settle" -eq 1 ]; then
      n_settled=$((n_settled + 1))
    elif [ "$has_reg" -eq 1 ] || [ "$has_disp" -eq 1 ] || [ "$has_run" -eq 1 ]; then
      n_unsettled=$((n_unsettled + 1))
      if [ "$age" -gt "$WAVE_UNSETTLED_S" ]; then
        n_aged=$((n_aged + 1))
        emit_finding WAVE_UNSETTLED_AGE warn "wave=$base age_s=$age threshold_s=$WAVE_UNSETTLED_S reg=$has_reg disp=$has_disp run=$has_run settle=0"
        st=drift
      fi
    else
      n_empty=$((n_empty + 1))
    fi
  done

  emit_surface waves "$st" "cmd=$cmd; total=$n_total settled=$n_settled unsettled=$n_unsettled aged_unsettled=$n_aged empty=$n_empty threshold_s=$WAVE_UNSETTLED_S; ts=$TS_UTC"
}

# ---- surface: journal kill/OOM ----------------------------------------------
# Classes counted (content is evidence; never acted on):
#   oom_kill      Out of memory|oom-kill|oom_reaper|Killed process
#   kill_signal   status=9/KILL|Failed with result 'signal'|SIGKILL
#   segfault      segfault|general protection fault
#   unit_failure  Failed with result|Unit entered failed state
# DRIFT on oom_kill>0 or kill_signal>0 (mint demand). segfault/unit_failure = info.
probe_journal() {
  local cmd="$JOURNALCTL_BIN --user -b --no-pager"
  local text='' rc=0
  local c_oom=0 c_kill=0 c_seg=0 c_unit=0
  local st=ok

  if ! have "$JOURNALCTL_BIN" && [ ! -x "$JOURNALCTL_BIN" ]; then
    emit_surface journal unavailable "cmd=$cmd; journalctl=missing; ts=$TS_UTC"
    return 0
  fi

  cap "$JOURNALCTL_BIN" --user -b --no-pager
  rc=$CAP_RC
  text=$CAP_OUT
  # rc 0/1 both acceptable (1 can mean empty on some builds); other = unavailable
  if [ "$rc" -gt 1 ]; then
    emit_surface journal unavailable "cmd=$cmd; rc=$rc; ts=$TS_UTC"
    return 0
  fi

  c_oom=$(printf '%s\n' "$text" | grep -ciE 'Out of memory|oom-kill|oom_reaper|Killed process' || true)
  c_kill=$(printf '%s\n' "$text" | grep -ciE 'status=9/KILL|Failed with result .signal|SIGKILL' || true)
  c_seg=$(printf '%s\n' "$text" | grep -ciE 'segfault|general protection fault' || true)
  c_unit=$(printf '%s\n' "$text" | grep -ciE 'Failed with result|Unit entered failed state' || true)

  if [ "$c_oom" -gt 0 ]; then
    emit_finding OOM_KILL_JOURNAL crit "class=oom_kill count=$c_oom boot=current scope=user"
    st=drift
  fi
  if [ "$c_kill" -gt 0 ]; then
    emit_finding KILL_SIGNAL_JOURNAL warn "class=kill_signal count=$c_kill boot=current scope=user"
    st=drift
  fi
  if [ "$c_seg" -gt 0 ]; then
    emit_finding SEGFAULT_JOURNAL info "class=segfault count=$c_seg boot=current scope=user"
  fi
  if [ "$c_unit" -gt 0 ]; then
    emit_finding UNIT_FAILURE_JOURNAL info "class=unit_failure count=$c_unit boot=current scope=user"
  fi

  emit_surface journal "$st" "cmd=$cmd; oom_kill=$c_oom kill_signal=$c_kill segfault=$c_seg unit_failure=$c_unit rc=$rc; ts=$TS_UTC"
}

# ---- surface: cgroup memory -------------------------------------------------
probe_cgroup() {
  local cmd="cat $CGROUP_EVENTS; cat $CGROUP_CURRENT"
  local oom_kill='' oom='' high='' max='' cur='' st=ok

  if [ ! -r "$CGROUP_EVENTS" ]; then
    emit_surface cgroup unavailable "cmd=$cmd; events=unreadable path=$CGROUP_EVENTS; ts=$TS_UTC"
    emit_finding CGROUP_UNAVAILABLE info "memory.events unreadable path=$CGROUP_EVENTS"
    return 0
  fi

  oom_kill=$(cgroup_field "$CGROUP_EVENTS" oom_kill)
  oom=$(cgroup_field "$CGROUP_EVENTS" oom)
  high=$(cgroup_field "$CGROUP_EVENTS" high)
  max=$(cgroup_field "$CGROUP_EVENTS" max)
  cur=$(read_file "$CGROUP_CURRENT")
  oom_kill=${oom_kill:-0}

  # presence flag semantics (tsukuroi note): oom_kill is a flag/counter, not a meter to clear
  if [ "$oom_kill" -gt 0 ] 2>/dev/null; then
    emit_finding CGROUP_OOM_KILL crit "oom_kill=$oom_kill oom=${oom:-?} high=${high:-?} max=${max:-?} current=${cur:-?} path=$CGROUP_EVENTS"
    st=drift
  fi

  emit_surface cgroup "$st" "cmd=$cmd; oom_kill=$oom_kill oom=${oom:-?} high=${high:-?} max=${max:-?} current=${cur:-?}; ts=$TS_UTC"
}

# ---- surface: disk runway ---------------------------------------------------
probe_disk() {
  local cmd="$DF_BIN -P"
  local st=ok t line fs size used avail pctp pct target_found=0

  if ! have "$DF_BIN" && [ ! -x "$DF_BIN" ]; then
    emit_surface disk unavailable "cmd=$cmd; df=missing; ts=$TS_UTC"
    return 0
  fi

  for t in $DISK_TARGETS; do
    if [ ! -e "$t" ]; then
      emit_finding DISK_UNAVAILABLE info "target_absent path=$t"
      continue
    fi
    target_found=1
    cap "$DF_BIN" -P "$t"
    if [ "$CAP_RC" -ne 0 ]; then
      emit_finding DISK_UNAVAILABLE info "df_failed path=$t rc=$CAP_RC"
      continue
    fi
    # second line of df -P
    line=$(printf '%s\n' "$CAP_OUT" | awk 'NR==2 {print}')
    if [ -z "$line" ]; then
      emit_finding DISK_UNAVAILABLE info "df_empty path=$t"
      continue
    fi
    fs=$(printf '%s\n' "$line" | awk '{print $1}')
    size=$(printf '%s\n' "$line" | awk '{print $2}')
    used=$(printf '%s\n' "$line" | awk '{print $3}')
    avail=$(printf '%s\n' "$line" | awk '{print $4}')
    pctp=$(printf '%s\n' "$line" | awk '{print $5}')
    pct=${pctp%%%}
    if [ -z "$pct" ] || ! [ "$pct" -eq "$pct" ] 2>/dev/null; then
      emit_finding DISK_UNAVAILABLE info "df_parse path=$t line=$line"
      continue
    fi
    if [ "$pct" -ge "$DISK_CRIT_PCT" ]; then
      emit_finding DISK_CRITICAL crit "path=$t fs=$fs size=$size used=$used avail=$avail used_pct=$pct threshold=$DISK_CRIT_PCT"
      st=drift
    elif [ "$pct" -ge "$DISK_WARN_PCT" ]; then
      emit_finding DISK_LOW warn "path=$t fs=$fs size=$size used=$used avail=$avail used_pct=$pct threshold=$DISK_WARN_PCT"
      st=drift
    fi
  done

  if [ "$target_found" -eq 0 ]; then
    emit_surface disk unavailable "cmd=$cmd; targets=$DISK_TARGETS; none present; ts=$TS_UTC"
  else
    emit_surface disk "$st" "cmd=$cmd; targets=$DISK_TARGETS; warn_pct=$DISK_WARN_PCT crit_pct=$DISK_CRIT_PCT; ts=$TS_UTC"
  fi
}

# ---- surface: lane silence --------------------------------------------------
# PROTOCOL.md:158-167 — progressing = lane-authored commit OR non-git files
# newer than launch/window; sibling-authored alone = progressing-weak;
# neither = silent. Commit sparsity is NOT silence.
# r1 approximation without launch-ts ledger: window = NOW - LANE_SILENCE_S.
# Grade per roster lane against $ROOT/<lane>-shokunin (protocol/aggregator -> ROOT).
lane_repo() {
  case "$1" in
    protocol|aggregator) printf '%s' "$ROOT" ;;
    *) printf '%s/%s-shokunin' "$ROOT" "$1" ;;
  esac
}

probe_silence() {
  local cmd="git -C <repo> log -1 --format=%ct; find <repo> -newermt @window"
  local st=ok lane repo head_t newest_t window_start grade n_silent=0 n_prog=0 n_weak=0 n_skip=0
  window_start=$((NOW_EPOCH - LANE_SILENCE_S))

  for lane in $ROSTER_LANES; do
    repo=$(lane_repo "$lane")
    if [ ! -d "$repo" ]; then
      n_skip=$((n_skip + 1))
      continue
    fi
    head_t=0
    if have "$GIT_BIN" || [ -x "$GIT_BIN" ]; then
      if [ -d "$repo/.git" ]; then
        cap "$GIT_BIN" -C "$repo" log -1 --format=%ct
        if [ "$CAP_RC" -eq 0 ] && [ -n "$CAP_OUT" ]; then
          head_t=$(printf '%s\n' "$CAP_OUT" | head -n1 | tr -d '[:space:]')
        fi
      fi
    fi
    newest_t=$(find "$repo" -type f -not -path '*/.git/*' -printf '%T@\n' 2>/dev/null | sort -n | tail -1 | cut -d. -f1)
    newest_t=${newest_t:-0}
    head_t=${head_t:-0}

    grade=silent
    # progressing: head or files inside window
    if [ "$head_t" -ge "$window_start" ] 2>/dev/null || [ "$newest_t" -ge "$window_start" ] 2>/dev/null; then
      # r1: without author check, treat in-window activity as progressing
      # (progressing-weak needs author ≠ lane — deferred; sibling-commit alone
      # without file mtime would need git log --format=%an — kept weak only when
      # head is in-window but files are not and we cannot prove authorship).
      if [ "$newest_t" -ge "$window_start" ] 2>/dev/null; then
        grade=progressing
        n_prog=$((n_prog + 1))
      elif [ "$head_t" -ge "$window_start" ] 2>/dev/null; then
        grade=progressing-weak
        n_weak=$((n_weak + 1))
      fi
    else
      n_silent=$((n_silent + 1))
      emit_finding LANE_SILENT warn "lane=$lane head_epoch=$head_t newest_epoch=$newest_t window_s=$LANE_SILENCE_S"
      st=drift
    fi
  done

  emit_surface silence "$st" "cmd=$cmd; silent=$n_silent progressing=$n_prog progressing_weak=$n_weak skipped=$n_skip window_s=$LANE_SILENCE_S; ts=$TS_UTC"
}

# ---- surface: tmux (optional) -----------------------------------------------
probe_tmux() {
  local cmd="$TMUX_BIN ls"
  if ! have "$TMUX_BIN" && [ ! -x "$TMUX_BIN" ]; then
    emit_surface tmux unavailable "cmd=$cmd; tmux=missing; ts=$TS_UTC"
    return 0
  fi
  cap "$TMUX_BIN" ls
  # rc 1 often means no server — unavailable, not drift
  if [ "$CAP_RC" -ne 0 ]; then
    emit_surface tmux unavailable "cmd=$cmd; rc=$CAP_RC; ts=$TS_UTC"
    return 0
  fi
  local n
  n=$(printf '%s\n' "$CAP_OUT" | grep -c . || true)
  emit_surface tmux ok "cmd=$cmd; sessions=$n; ts=$TS_UTC"
}

# ---- live run ---------------------------------------------------------------
run_census() {
  local mode=${1:-live}
  printf 'mori-census %s — ts=%s — mode=%s — read-only\n' "$VERSION" "$TS_UTC" "$mode"

  probe_watchdog
  probe_waves
  probe_journal
  probe_cgroup
  probe_disk
  probe_silence
  probe_tmux

  local line
  for line in "${SURFACE_LINES[@]:-}"; do printf '%s\n' "$line"; done
  for line in "${FINDING_LINES[@]:-}"; do printf '%s\n' "$line"; done

  printf 'MORI_CENSUS: %s (findings=%d drift=%d unavailable=%d surfaces=%d)\n' \
    "$ROLL" "$N_FINDINGS" "$N_DRIFT" "$N_UNAVAIL" "$N_SURFACES"

  case "$ROLL" in
    CLEAN) exit 0 ;;
    DRIFT) exit 1 ;;
    *) exit 2 ;;
  esac
}

# ---- hermetic selftest ------------------------------------------------------
run_selftest() {
  local work bin FX PASS=0 FAIL=0
  work=$(mktemp -d /tmp/mori-census-selftest.XXXXXX)
  trap 'rm -rf -- "${work:-}"' EXIT INT TERM
  bin="$work/bin"
  mkdir -p "$bin" "$work/fx"

  # dispatcher stubs — answer only from MORI_FIXTURE tree
  cat > "$bin/.dispatch" <<'STUB'
#!/usr/bin/env bash
set -uo pipefail
name=${0##*/}
fx=${MORI_FIXTURE:-}
[ -n "$fx" ] || { printf 'fixture dispatcher: MORI_FIXTURE unset\n' >&2; exit 97; }
rc_of() { local f="$fx/stub/$1.rc"; if [ -f "$f" ]; then cat "$f"; else printf 0; fi; }
out_of() { local f="$fx/stub/$1"; if [ -f "$f" ]; then cat "$f"; fi; }
case "$name" in
  pgrep)
    out_of pgrep; exit "$(rc_of pgrep)" ;;
  journalctl)
    out_of journal; exit "$(rc_of journal)" ;;
  df)
    # ignore args; emit fixture table
    out_of df; exit "$(rc_of df)" ;;
  tmux)
    out_of tmux; exit "$(rc_of tmux)" ;;
  git)
    out_of git; exit "$(rc_of git)" ;;
esac
printf 'fixture dispatcher: unknown %s\n' "$name" >&2
exit 96
STUB
  chmod 700 "$bin/.dispatch"
  local c
  for c in pgrep journalctl df tmux git; do ln -s .dispatch "$bin/$c"; done

  ok() { PASS=$((PASS + 1)); printf 'PASS %s\n' "$*"; }
  bad() { FAIL=$((FAIL + 1)); printf 'FAIL %s\n' "$*" >&2; }

  fx_hash() { find "$1" -type f -exec sha256sum {} + 2>/dev/null | LC_ALL=C sort | sha256sum | cut -d' ' -f1; }
  fx_no_mutation() {
    local d=$1 before=$2 after
    after=$(fx_hash "$d")
    if [ "$after" != "$before" ]; then bad "fixture mutated ($d)"; fi
  }

  # Build a quiet baseline fixture under $1
  # Layout: $d is MORI_SHOKUNIN_ROOT (fleet root). Lane repos live at
  # $d/<lane>-shokunin so silence grading resolves the same as live.
  fx_quiet() {
    local d=$1
    mkdir -p "$d/.ufo/state" "$d/.ufo/waves" "$d/stub" \
      "$d/cgroup" "$d/kagi-shokunin/.git" "$d/diskroot"
    printf '2026-10-14T12:00:00Z tick=1\n' > "$d/.ufo/watchdog.log"
    printf '1\n' > "$d/.ufo/state/kagi.round"
    printf 'mission-x\n' > "$d/.ufo/state/kagi.mission"
    mkdir -p "$d/.ufo/waves/wave-settled"
    printf '{"wave":"wave-settled"}\n' > "$d/.ufo/waves/wave-settled/swarm-registry.json"
    printf '{"wave":"wave-settled"}\n' > "$d/.ufo/waves/wave-settled/dispatch.json"
    printf '{"schema":"ufo-swarm-results-v1","members":[]}\n' > "$d/.ufo/waves/wave-settled/results.json"
    printf 'low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\noom_group_kill 0\n' > "$d/cgroup/memory.events"
    printf '123456\n' > "$d/cgroup/memory.current"
    printf 'MemAvailable: 20000000 kB\n' > "$d/meminfo"
    printf '1234 bash /path/scripts/shokunin-watchdog.sh\n' > "$d/stub/pgrep"
    printf 0 > "$d/stub/pgrep.rc"
    : > "$d/stub/journal"; printf 0 > "$d/stub/journal.rc"
    printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\n/dev/fx 1000000 10000 990000 2%% /fx\n' > "$d/stub/df"
    printf 0 > "$d/stub/df.rc"
    printf 'fx_session: 1 windows\n' > "$d/stub/tmux"; printf 0 > "$d/stub/tmux.rc"
    printf '%s\n' "1700000000" > "$d/stub/git"; printf 0 > "$d/stub/git.rc"
    printf 'x\n' > "$d/kagi-shokunin/LOG.md"
  }

  EXTRA_ENV=()
  FRESHEN_WD=1
  FRESHEN_WAVES=1
  FRESHEN_LANE=1
  check() { # LABEL WANT_RC WANT_VERDICT [WANT_RE...]
    local label=$1 wrc=$2 wverdict=$3
    shift 3
    local out rc before re miss='' env_now
    env_now=${PIN_NOW:-1700000000}
    # Optional freshen — drift cases that pin old mtimes set FRESHEN_*=0
    if [ "${FRESHEN_WD}" = 1 ] && [ -f "$FX/.ufo/watchdog.log" ]; then
      touch -d "@$env_now" "$FX/.ufo/watchdog.log" 2>/dev/null || touch "$FX/.ufo/watchdog.log"
    fi
    if [ "${FRESHEN_LANE}" = 1 ] && [ -f "$FX/kagi-shokunin/LOG.md" ]; then
      touch -d "@$env_now" "$FX/kagi-shokunin/LOG.md" 2>/dev/null || true
    fi
    if [ "${FRESHEN_WAVES}" = 1 ] && [ -d "$FX/.ufo/waves" ]; then
      find "$FX/.ufo/waves" -type f -exec touch -d "@$env_now" {} + 2>/dev/null || true
    fi

    before=$(fx_hash "$FX")
    set +e
    out=$(env -i \
      PATH="$bin:/usr/bin:/bin" \
      HOME="$work/home" \
      MORI_FIXTURE="$FX" \
      MORI_SHOKUNIN_ROOT="$FX" \
      MORI_UFO_DIR="$FX/.ufo" \
      MORI_WATCHDOG_LOG="$FX/.ufo/watchdog.log" \
      MORI_STATE_DIR="$FX/.ufo/state" \
      MORI_WAVES_DIR="$FX/.ufo/waves" \
      MORI_CGROUP_EVENTS="$FX/cgroup/memory.events" \
      MORI_CGROUP_CURRENT="$FX/cgroup/memory.current" \
      MORI_MEMINFO="$FX/meminfo" \
      MORI_DF_BIN="$bin/df" \
      MORI_PGREP_BIN="$bin/pgrep" \
      MORI_JOURNALCTL_BIN="$bin/journalctl" \
      MORI_TMUX_BIN="$bin/tmux" \
      MORI_GIT_BIN="$bin/git" \
      MORI_DISK_TARGETS="$FX/diskroot" \
      MORI_ROSTER_LANES="kagi" \
      MORI_NOW_EPOCH="$env_now" \
      MORI_WATCHDOG_STALE_S=900 \
      MORI_WAVE_UNSETTLED_S=7200 \
      MORI_DISK_WARN_PCT=85 \
      MORI_DISK_CRIT_PCT=95 \
      MORI_LANE_SILENCE_S=7200 \
      "${EXTRA_ENV[@]+"${EXTRA_ENV[@]}"}" \
      bash "$SELF" 2>&1)
    rc=$?
    set -e
    if [ "$rc" -ne "$wrc" ]; then
      bad "$label: exit $rc want $wrc; tail=$(printf '%s' "$out" | tail -n3 | tr '\n' '|')"
    elif ! printf '%s\n' "$out" | grep -qE "^MORI_CENSUS: ${wverdict} "; then
      bad "$label: verdict want $wverdict; got=$(printf '%s\n' "$out" | grep '^MORI_CENSUS:' | head -n1)"
    else
      miss=''
      for re in "$@"; do
        printf '%s\n' "$out" | grep -qE -- "$re" || miss="$miss |$re|"
      done
      if [ -n "$miss" ]; then
        bad "$label: missing match $miss"
      else
        ok "$label (exit $rc $wverdict)"
      fi
    fi
    fx_no_mutation "$FX" "$before"
    EXTRA_ENV=()
    FRESHEN_WD=1
    FRESHEN_WAVES=1
    FRESHEN_LANE=1
  }

  check_cli() {
    local label=$1 wrc=$2; shift 2
    local res=() out rc miss=''
    while [ $# -gt 0 ] && [ "$1" != '--' ]; do res+=("$1"); shift; done
    [ "${1:-}" = '--' ] && shift
    set +e
    out=$(bash "$SELF" "$@" 2>&1)
    rc=$?
    set -e
    if [ "$rc" -ne "$wrc" ]; then
      bad "$label: exit $rc want $wrc"
    else
      miss=''
      for re in "${res[@]}"; do
        printf '%s\n' "$out" | grep -qE -- "$re" || miss="$miss |$re|"
      done
      if [ -n "$miss" ]; then bad "$label: missing $miss"; else ok "$label (exit $rc)"; fi
    fi
  }

  # --- cases ---------------------------------------------------------------
  PIN_NOW=1700000000

  FX="$work/fx/clean"; mkdir -p "$FX"; fx_quiet "$FX"
  check 'clean: all quiet' 0 CLEAN \
    '^SURFACE watchdog: ok' \
    '^MORI_CENSUS: CLEAN '

  FX="$work/fx/wd-absent"; mkdir -p "$FX"; fx_quiet "$FX"
  : > "$FX/stub/pgrep"; printf 1 > "$FX/stub/pgrep.rc"
  check 'drift: WATCHDOG_ABSENT' 1 DRIFT \
    'FINDING WATCHDOG_ABSENT' \
    '^MORI_CENSUS: DRIFT '

  FX="$work/fx/wd-stale"; mkdir -p "$FX"; fx_quiet "$FX"
  printf 'old\n' > "$FX/.ufo/watchdog.log"
  touch -d '@1600000000' "$FX/.ufo/watchdog.log" 2>/dev/null || true
  FRESHEN_WD=0
  check 'drift: WATCHDOG_STALE' 1 DRIFT \
    'FINDING WATCHDOG_STALE' \
    '^MORI_CENSUS: DRIFT '

  FX="$work/fx/wave-aged"; mkdir -p "$FX"; fx_quiet "$FX"
  mkdir -p "$FX/.ufo/waves/wave-hang"
  printf '{}\n' > "$FX/.ufo/waves/wave-hang/swarm-registry.json"
  printf '{}\n' > "$FX/.ufo/waves/wave-hang/dispatch.json"
  touch -d '@1600000000' "$FX/.ufo/waves/wave-hang/swarm-registry.json" \
    "$FX/.ufo/waves/wave-hang/dispatch.json" 2>/dev/null || true
  FRESHEN_WAVES=0
  check 'drift: WAVE_UNSETTLED_AGE' 1 DRIFT \
    'FINDING WAVE_UNSETTLED_AGE' \
    'wave=wave-hang'

  FX="$work/fx/wave-fresh-unsettled"; mkdir -p "$FX"; fx_quiet "$FX"
  mkdir -p "$FX/.ufo/waves/wave-live"
  printf '{}\n' > "$FX/.ufo/waves/wave-live/run.json"
  check 'clean: unsettled young wave does not fire' 0 CLEAN \
    '^SURFACE waves: ok'

  FX="$work/fx/oom-journal"; mkdir -p "$FX"; fx_quiet "$FX"
  printf 'kernel: Out of memory: Killed process 4242\n' > "$FX/stub/journal"
  check 'drift: OOM_KILL_JOURNAL' 1 DRIFT \
    'FINDING OOM_KILL_JOURNAL' \
    '^MORI_CENSUS: DRIFT '

  FX="$work/fx/cgroup-oom"; mkdir -p "$FX"; fx_quiet "$FX"
  printf 'low 0\nhigh 0\nmax 0\noom 1\noom_kill 1\noom_group_kill 0\n' > "$FX/cgroup/memory.events"
  check 'drift: CGROUP_OOM_KILL' 1 DRIFT \
    'FINDING CGROUP_OOM_KILL'

  FX="$work/fx/disk-crit"; mkdir -p "$FX"; fx_quiet "$FX"
  printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\n/dev/fx 1000000 960000 40000 96%% /fx\n' > "$FX/stub/df"
  check 'drift: DISK_CRITICAL' 1 DRIFT \
    'FINDING DISK_CRITICAL'

  FX="$work/fx/disk-ok"; mkdir -p "$FX"; fx_quiet "$FX"
  printf 'Filesystem 1024-blocks Used Available Capacity Mounted on\n/dev/fx 1000000 10000 990000 2%% /fx\n' > "$FX/stub/df"
  check 'clean: disk under warn' 0 CLEAN \
    '^SURFACE disk: ok'

  FX="$work/fx/lane-silent"; mkdir -p "$FX"; fx_quiet "$FX"
  printf '0\n' > "$FX/stub/git"
  printf 'old\n' > "$FX/kagi-shokunin/LOG.md"
  touch -d '@1600000000' "$FX/kagi-shokunin/LOG.md" 2>/dev/null || true
  FRESHEN_LANE=0
  EXTRA_ENV=(MORI_LANE_SILENCE_S=60)
  check 'drift: LANE_SILENT' 1 DRIFT \
    'FINDING LANE_SILENT' \
    'lane=kagi'

  FX="$work/fx/cgroup-unavail"; mkdir -p "$FX"; fx_quiet "$FX"
  rm -f "$FX/cgroup/memory.events"
  check 'clean: CGROUP_UNAVAILABLE is not DRIFT' 0 CLEAN \
    'FINDING CGROUP_UNAVAILABLE' \
    '^SURFACE cgroup: unavailable' \
    '^MORI_CENSUS: CLEAN '

  FX="$work/fx/journal-empty-ok"; mkdir -p "$FX"; fx_quiet "$FX"
  : > "$FX/stub/journal"
  check 'clean: empty journal' 0 CLEAN \
    '^SURFACE journal: ok'

  check_cli 'cli: unknown arg exit 2' 2 'mori-census:' -- --bogus
  check_cli 'cli: --help exit 0' 0 'usage: mori-census' -- --help

  printf 'MORI_CENSUS_SELFTEST: %s (%d cases, %d passed, %d failed)\n' \
    "$([ "$FAIL" -eq 0 ] && printf PASS || printf FAIL)" "$((PASS + FAIL))" "$PASS" "$FAIL"
  [ "$FAIL" -eq 0 ]
}

# ---- main -------------------------------------------------------------------
main() {
  local selftest=0
  while [ $# -gt 0 ]; do
    case "$1" in
      --selftest) selftest=1; shift ;;
      --help|-h) usage; exit 0 ;;
      verify|--verify) shift ;; # accepted alias
      *) die_usage "unknown argument: $1" ;;
    esac
  done
  if [ "$selftest" -eq 1 ]; then
    run_selftest
    return
  fi
  run_census live
}

main "$@"
```

---

## 6. Operability notes for parent landing

1. `mkdir -p mori-shokunin/tools && install -m 0755` the script body (strip the markdown fence).
2. Run `bash tools/mori-census.sh --selftest` → expect `MORI_CENSUS_SELFTEST: PASS (N cases, N passed, 0 failed)` exit 0.
3. Run `bash tools/mori-census.sh` live → expect a `MORI_CENSUS: CLEAN|DRIFT` line; on this host at design time the live state is **likely DRIFT** (`WATCHDOG_ABSENT` + `WATCHDOG_STALE` — log mtime 2026-10-13, no `shokunin-watchdog` pid; `CGROUP_OOM_KILL` oom_kill=1 on user slice). That is the mint demand signal, not a gate defect.
4. FixtureDesign / FindingIds peers may retune ids or case matrix; keep id strings stable once SCORECARD cites them.
5. Registry row (GateRegistryRow peer): gate · `bash tools/mori-census.sh` · `MORI_CENSUS: CLEAN|DRIFT` · `--selftest` · write scope = selftest temp only · owner = mori.

---

## 7. Evidence retained (this seat)

| Fact | Command / source | Timestamp |
|---|---|---|
| SKILL gate row names CLEAN\|DRIFT exit 0/1/2 + selftest | `mori-shokunin/SKILL.md` Gates | read this wave |
| PROVINCE owns watchdog/waves/kill/cgroup/disk/silence; refuses remediation | `PROVINCE.md` | read this wave |
| Watchdog tick INTERVAL=450 | `scripts/shokunin-watchdog.sh` L10 | read this wave |
| Silence grades silent / progressing / progressing-weak | `PROTOCOL.md:158-167` | read this wave |
| Live watchdog.log last mtime | `stat` → 2026-10-13 16:44:48 -0300 | 2026-10-15T00:28:58Z |
| Live user-slice oom_kill | `cat …/user-1000.slice/memory.events` → oom_kill 1 | 2026-10-15T00:28Z |
| No `shokunin-watchdog` pid | `pgrep -af shokunin-watchdog` → empty | 2026-10-15T00:28Z |
| Sibling pattern | `tsukuroi-shokunin/tools/tsukuroi-census.sh` selftest + env overrides | pattern reuse |
| Wave settle shapes | train: registry+dispatch+closeout/results · 12h: run+task-response+results | live `.ufo/waves/*` |

---

## 8. Risks / blockers

| Risk | Mitigation in design |
|---|---|
| Live DRIFT on first run looks like a broken gate | Documented: current host **is** the mint incident class; CLEAN is not required for r1 land |
| `LANE_SILENT` false positive on commit-sparse but active lanes | File mtime path counts as progressing; threshold env-tunable; PROTOCOL forbids commit-sparsity⇒failed |
| Journal greps over-match noisy unit_failure | unit_failure/segfault severity=info only in r1 |
| `progressing-weak` author detection incomplete | Named deferred; head-without-files graded weak |
| FixtureDesign may want more cases | Script cases cover fire/not-fire per surface; peer can extend without vocabulary change |
| Selftest `touch -d` portability | GNU touch on this Arch host; if fail, cases still pin thresholds via env |

**Blockers for this seat:** none. Parent owns landing + SCORECARD/LOG. This report is data, not a judge verdict.

---

## 9. Axis self-check (advisory, not a score)

- **Coverage:** six PROVINCE surfaces + tmux optional; finding-id table; unavailable≠DRIFT.
- **Operability:** single bash entry, exit map, hermetic `--selftest`, env overrides for every host read.
- **Calibration:** CLEAN\|DRIFT matches SKILL; thresholds cited or marked proposal; live host expected DRIFT explained.
