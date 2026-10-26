#!/usr/bin/env bash
# disk-guard.sh — driver-side disk-pressure guard for hyaku runs (layers 1-2).
#
# WHAT
#   One place that answers "is any fleet root under disk pressure?", reclaims abandoned round
#   scratch safely, and can be run in a loop by the driver. It exists because every long run has
#   ended with /tmp at 100 %: seats clone lane repos and build multi-GB work trees under /tmp,
#   those trees outlive seat death, nothing reclaims them, and later seats die of ENOSPC.
#
# CONTRACT
#   disk-guard.sh check                      exit 0 = every root below SOFT_PCT on its filesystem;
#                                            1 = pressure on >=1 root; 2 = usage/environment error
#   disk-guard.sh status                     table: root, use%, free, then top-15 consumers per root
#                                            (bounded `du`); exit code as `check`
#   disk-guard.sh sweep [--dry-run] [--emergency] [--all]
#                                            for each root above SOFT_PCT (or always with
#                                            --all/--emergency): collect top-level entries, drop
#                                            excluded/keep-listed/symlinks, drop entries younger
#                                            than MIN_AGE_MIN, size them (`timeout $DU_TIMEOUT
#                                            du -xsk`; timeout => size unknown, ordered after the
#                                            sized entries but still eligible), then delete
#                                            largest-first every IDLE entry until use% < TARGET_PCT.
#                                            Liveness is re-checked right before each rm; rm is
#                                            `rm -rf --one-file-system -- "<realpath>"` on an exact
#                                            top-level path, never a glob. (A --dry-run decides
#                                            from that pass's snapshot: nothing is removed, so
#                                            there is nothing to re-check.) --emergency: IDLE_MIN=10,
#                                            plain files >= 100 MB become eligible, SOFT gate
#                                            ignored. --all: SOFT gate ignored (run-end purge).
#                                            --dry-run logs/prints decisions, deletes nothing.
#                                            exit 0 = below SOFT after (or nothing to do);
#                                            1 = still >= SOFT on some root; 2 = usage/env
#   disk-guard.sh purge-lane <lane> <round> [--dry-run]
#                                            removes exactly "$HYAKU_SCRATCH/<lane>-r<round>" when
#                                            it exists and holds no live process; round-close hook.
#                                            exit 0 = removed or absent; 1 = live process inside;
#                                            2 = usage/env
#   disk-guard.sh watch [--interval SECS]    loop forever: check; on pressure sweep (--emergency
#                                            when any root >= HARD_PCT); sleep; log every pass
#   disk-guard.sh selftest                   fixture-based self-test, including the seeded-defect
#                                            arm that proves the gate can fail.
#                                            exit 0 = pass; 1 = fail
#
# ENV — precedence: explicit environment > `$FLEET/scripts/hyaku/hyaku.env` > built-in defaults.
#   The env file is *parsed*, never sourced: only the whitelisted KEY=VALUE lines below are read.
#     HYAKU_DISK_ROOTS   ("/tmp /var/tmp /fast/scratch/hyaku" — missing roots are skipped silently)
#     SOFT_PCT (70)  TARGET_PCT (60)  HARD_PCT (90)  IDLE_MIN (45)  MIN_AGE_MIN (10)
#     HYAKU_SCRATCH (/fast/scratch/hyaku)  DU_TIMEOUT (30)  FLEET (script's grandparent dir)
#     HYAKU_DISK_KEEP (file of exact absolute paths never deleted;
#                      default $FLEET/.ufo/state/disk-guard.keep if present)
#     HYAKU_DISK_LOG ($FLEET/.ufo/state/disk-guard.log — driver runtime, append-only)
#     HYAKU_DISK_USAGE_OVERRIDE ("<root>=<pct>[@<total_kb>] …" — test hook replacing df;
#                      the optional @<total_kb> gives the modelled size of the filesystem so the
#                      selftest can observe usage dropping as bytes are freed)
#
# LIVENESS — an entry is LIVE when any /proc/<pid>/{cwd,exe,root} or /proc/<pid>/fd/* resolves to
#   it or under it (scanned as the current user, and additionally through passwordless `sudo -n`
#   when available), or when any file under it was modified within IDLE_MIN minutes (bounded
#   `timeout 20 find … -newermt`). Unknown liveness is treated as live: never delete on doubt.
#
# LOG — append-only, one line per decision on stdout too:
#   <ISO ts> <action> <path> <size_mb|?> idle=<min|?> <reason>
#   action in delete|dry-run|keep-live|keep-young|keep-listed|keep-excluded|defer|pressure|ok
#
# EXIT CODES  0 = clean · 1 = pressure/live · 2 = usage or environment error
#
# Run: bash scripts/hyaku/disk-guard.sh {check|status|sweep|purge-lane|watch|selftest}
set -u

LC_ALL=C
export LC_ALL

die() { printf 'disk-guard: %s\n' "$*" >&2; exit 2; }
warn() { printf 'disk-guard: %s\n' "$*" >&2; }

# ───────────────────────────────────────────────────────────────── configuration

ENV_KEYS='HYAKU_SCRATCH HYAKU_DISK_ROOTS SOFT_PCT TARGET_PCT HARD_PCT IDLE_MIN MIN_AGE_MIN'

# Parse only whitelisted KEY=VALUE lines; never source the file.
load_env_file() {
  local file=$1 line key val k wanted
  [[ -r $file ]] || return 0
  while IFS= read -r line || [[ -n $line ]]; do
    line=${line%$'\r'}
    [[ $line == *=* ]] || continue
    key=${line%%=*}
    val=${line#*=}
    key=${key#"${key%%[![:space:]]*}"}
    key=${key%"${key##*[![:space:]]}"}
    wanted=''
    for k in $ENV_KEYS; do
      if [[ $key == "$k" ]]; then wanted=1; break; fi
    done
    [[ -n $wanted ]] || continue
    [[ -n ${!key+x} ]] && continue                 # explicit environment wins
    val=${val#"${val%%[![:space:]]*}"}
    val=${val%"${val##*[![:space:]]}"}
    if [[ $val == \"*\" ]]; then val=${val:1:${#val}-2}; fi
    if [[ $val == \'*\' ]]; then val=${val:1:${#val}-2}; fi
    printf -v "$key" '%s' "$val"
  done < "$file"
  return 0
}

SELF_PATH=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)/$(basename -- "${BASH_SOURCE[0]}")
FLEET=${FLEET:-$(cd -- "$(dirname -- "$SELF_PATH")/../.." && pwd -P)}
load_env_file "${HYAKU_ENV_FILE:-$FLEET/scripts/hyaku/hyaku.env}"

HYAKU_SCRATCH=${HYAKU_SCRATCH:-/fast/scratch/hyaku}
ROOTS_RAW=${HYAKU_DISK_ROOTS:-/tmp /var/tmp /fast/scratch/hyaku}
SOFT_PCT=${SOFT_PCT:-70}
TARGET_PCT=${TARGET_PCT:-60}
HARD_PCT=${HARD_PCT:-90}
IDLE_MIN=${IDLE_MIN:-45}
MIN_AGE_MIN=${MIN_AGE_MIN:-10}
DU_TIMEOUT=${DU_TIMEOUT:-30}
KEEP_FILE=${HYAKU_DISK_KEEP:-$FLEET/.ufo/state/disk-guard.keep}
LOG_FILE=${HYAKU_DISK_LOG:-$FLEET/.ufo/state/disk-guard.log}
JOBS=16
PLAIN_FILE_MIN_KB=102400                            # 100 MB, emergency-only eligibility
STATUS_BUDGET=70                                    # seconds for the whole `status` sizing pass

require_int() { # name value min max
  local name=$1 value=$2 min=$3 max=$4
  [[ $value =~ ^[0-9]+$ ]] || die "env $name must be a nonnegative integer (got '$value')"
  (( value >= min && value <= max )) || die "env $name must be in $min..$max (got $value)"
  return 0
}

validate_env() {
  require_int SOFT_PCT "$SOFT_PCT" 1 100
  require_int TARGET_PCT "$TARGET_PCT" 1 100
  require_int HARD_PCT "$HARD_PCT" 1 100
  require_int IDLE_MIN "$IDLE_MIN" 0 100000
  require_int MIN_AGE_MIN "$MIN_AGE_MIN" 0 100000
  require_int DU_TIMEOUT "$DU_TIMEOUT" 1 3600
  return 0
}

ROOTS=()
read -r -a ROOTS <<<"$ROOTS_RAW" || true

declare -a ROOT_REAL=()
init_root_real() {
  ROOT_REAL=()
  local r rp
  for r in "${ROOTS[@]}"; do
    rp=$(realpath -m -- "$r" 2>/dev/null) || rp=$r
    ROOT_REAL+=( "$rp" )
  done
  return 0
}
init_root_real

under_roots() { # path -> 0 when strictly under a configured root
  local rp=$1 rr
  for rr in "${ROOT_REAL[@]}"; do
    [[ $rp == "$rr"/* ]] && return 0
  done
  return 1
}

# ───────────────────────────────────────────────────────────────── usage / free

OV_PCT_DECL=''
declare -A OV_PCT=() OV_TOTAL=() DEL_KB=()

parse_override() {
  OV_PCT=() OV_TOTAL=()
  local raw=${HYAKU_DISK_USAGE_OVERRIDE:-} tok root pct total
  [[ -n $raw ]] || return 0
  for tok in $raw; do
    if [[ ! $tok =~ ^(.+)=([0-9]{1,3})(@([0-9]+))?$ ]]; then
      warn "ignoring malformed HYAKU_DISK_USAGE_OVERRIDE token '$tok'"
      continue
    fi
    root=${BASH_REMATCH[1]}
    pct=${BASH_REMATCH[2]}
    total=${BASH_REMATCH[4]:-}
    OV_PCT["$root"]=$pct
    [[ -n $total ]] && OV_TOTAL["$root"]=$total
  done
  return 0
}

df_field() { # root field
  local root=$1 field=$2 out
  out=$(df -Pk -- "$root" 2>/dev/null | awk -v f="$field" 'NR==2 {print $f}')
  printf '%s\n' "${out:-}"
}

usage_of() { # root -> whole percent, or rc 1 when unavailable
  local root=$1 base total del pct
  if [[ -n ${OV_PCT[$root]:-} ]]; then
    base=${OV_PCT[$root]}
    total=${OV_TOTAL[$root]:-}
    [[ -n $total ]] || total=$(df_field "$root" 2)
    [[ $total =~ ^[0-9]+$ ]] || total=0
    del=${DEL_KB[$root]:-0}
    if (( total > 0 )); then
      base=$(( base - (del * 100) / total ))
      (( base < 0 )) && base=0
    fi
    printf '%s\n' "$base"
    return 0
  fi
  pct=$(df_field "$root" 5)
  pct=${pct%\%}
  [[ $pct =~ ^[0-9]+$ ]] || return 1
  printf '%s\n' "$pct"
  return 0
}

free_kb_of() { # root -> available KB, or "?"
  local root=$1 avail
  if [[ -n ${OV_TOTAL[$root]:-} ]]; then printf '?\n'; return 0; fi
  avail=$(df_field "$root" 4)
  [[ $avail =~ ^[0-9]+$ ]] || { printf '?\n'; return 0; }
  printf '%s\n' "$avail"
}

human_kb() {
  local kb=$1
  if (( kb >= 1073741824 )); then
    printf '%d.%dT' $(( kb / 1073741824 )) $(( (kb % 1073741824) * 10 / 1073741824 ))
  elif (( kb >= 1048576 )); then
    printf '%d.%dG' $(( kb / 1048576 )) $(( (kb % 1048576) * 10 / 1048576 ))
  elif (( kb >= 1024 )); then
    printf '%d.%dM' $(( kb / 1024 )) $(( (kb % 1024) * 10 / 1024 ))
  else
    printf '%dK' "$kb"
  fi
}

mb_of() { # kb -> "N.D" MB, "?" when unknown
  local kb=$1
  [[ $kb =~ ^[0-9]+$ ]] || { printf '?\n'; return 0; }
  printf '%d.%d\n' $(( kb / 1024 )) $(( (kb % 1024) * 10 / 1024 ))
}

NOW_TS=''
age_min() { # path -> whole minutes since mtime, "?" when unknown
  local p=$1 mtime
  [[ -n $NOW_TS ]] || NOW_TS=$(date +%s)
  mtime=$(stat -c %Y -- "$p" 2>/dev/null) || { printf '?\n'; return 0; }
  [[ $mtime =~ ^[0-9]+$ ]] || { printf '?\n'; return 0; }
  printf '%s\n' $(( (NOW_TS - mtime) / 60 ))
}

total_kb_of() { # root -> filesystem size in KB (modelled size when the hook carries one)
  local root=$1 total
  total=${OV_TOTAL[$root]:-}
  [[ -n $total ]] || total=$(df_field "$root" 2)
  [[ $total =~ ^[0-9]+$ ]] && (( total > 0 )) || total=1
  printf '%s\n' "$total"
}

# ───────────────────────────────────────────────────────────────── logging

LOG_READY=''
LOG_DISABLED=''
log_line() { # action path size idle reason
  local ts
  [[ -n $LOG_DISABLED ]] && return 0
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  if [[ -z $LOG_READY ]]; then
    mkdir -p -- "$(dirname -- "$LOG_FILE")" 2>/dev/null
    LOG_READY=1
  fi
  if ! printf '%s %s %s %s idle=%s %s\n' "$ts" "$1" "$2" "$3" "$4" "$5" >>"$LOG_FILE" 2>/dev/null; then
    warn "cannot append to log $LOG_FILE; logging disabled for this run"
    LOG_DISABLED=1
  fi
  return 0
}

# ───────────────────────────────────────────────────────────────── temp + trap

GUARD_RUNTMP=''
SELFTEST_BASE=''

cleanup_all() {
  [[ -n $GUARD_RUNTMP ]] && rm -rf --one-file-system -- "$GUARD_RUNTMP" 2>/dev/null
  [[ -n $SELFTEST_BASE ]] && rm -rf --one-file-system -- "$SELFTEST_BASE" 2>/dev/null
  return 0
}

setup_runtmp() {
  [[ -n $GUARD_RUNTMP ]] && return 0
  local base=${TMPDIR:-/var/tmp}
  GUARD_RUNTMP=$(mktemp -d "$base/disk-guard.XXXXXX" 2>/dev/null) ||
    GUARD_RUNTMP=$(mktemp -d /var/tmp/disk-guard.XXXXXX 2>/dev/null) ||
    die 'cannot create a temporary directory'
  return 0
}

trap cleanup_all EXIT

# ───────────────────────────────────────────────────────────────── liveness

# One batched /proc scan per pass: every candidate is checked against one link sweep, and a
# per-entry re-check writes a one-line target file and reuses the same program.
SCAN_PY=''

ensure_scan_py() {
  [[ -n $SCAN_PY ]] && return 0
  setup_runtmp
  SCAN_PY=$GUARD_RUNTMP/scan.py
  cat > "$SCAN_PY" <<'PY'
import os
import sys

targets = set()
entries = []
with open(sys.argv[1], 'rb') as handle:
    for raw in handle:
        raw = raw.rstrip(b'\n')
        if not raw:
            continue
        given = os.fsdecode(raw)
        resolved = os.path.realpath(given)
        targets.add(resolved)
        entries.append((resolved, given))

hit = set()


def bump(path):
    node = path
    while True:
        if node in targets:
            hit.add(node)
        parent = os.path.dirname(node)
        if parent == node:
            break
        node = parent


for name in os.listdir('/proc'):
    if not name.isdigit():
        continue
    base = '/proc/' + name
    links = [base + '/cwd', base + '/exe', base + '/root']
    try:
        links.extend(base + '/fd/' + fd for fd in os.listdir(base + '/fd'))
    except OSError:
        pass
    for link in links:
        try:
            raw = os.readlink(link)
        except OSError:
            continue
        if raw.endswith(' (deleted)'):
            raw = raw[:-10]
        if not raw.startswith('/'):
            continue
        bump(os.path.realpath(raw))
    if len(hit) == len(targets):
        break

for resolved, given in entries:
    if resolved in hit:
        print(given, flush=True)
PY
  return 0
}

SUDO_STATE=''
sudo_available() {
  if [[ -z $SUDO_STATE ]]; then
    if command -v sudo >/dev/null 2>&1 && sudo -n true 2>/dev/null; then
      SUDO_STATE=1
    else
      SUDO_STATE=0
    fi
  fi
  [[ $SUDO_STATE == 1 ]]
}

scan_proc_bash() { # fallback when python3 is absent; slow but correct
  local entry=$1 p l rp
  for p in /proc/[0-9]*; do
    for l in "$p/cwd" "$p/exe" "$p/root" "$p"/fd/*; do
      rp=$(readlink -f -- "$l" 2>/dev/null) || continue
      [[ -n $rp ]] || continue
      [[ $rp == "$entry" || $rp == "$entry"/* ]] && return 0
    done
  done
  return 1
}

scan_batch() { # targets_file -> prints the listed paths a process sits in (user, then root)
  local tf=$1 p
  ensure_scan_py
  if command -v python3 >/dev/null 2>&1; then
    python3 "$SCAN_PY" "$tf" 2>/dev/null
    if sudo_available; then
      sudo -n python3 "$SCAN_PY" "$tf" 2>/dev/null
    fi
    return 0
  fi
  while IFS= read -r p; do
    [[ -n $p ]] || continue
    scan_proc_bash "$p" && printf '%s\n' "$p"
  done < "$tf"
  return 0
}

entry_recent() { # path -> 0 when anything under it changed within IDLE_MIN
  [[ -n $(timeout 20 find "$1" -xdev -newermt "-${IDLE_MIN} minutes" -print -quit 2>/dev/null) ]]
}

entry_live() { # path -> 0 live: recent write, or a process inside it right now
  local entry=$1 tf hit
  entry_recent "$entry" && return 0
  setup_runtmp
  tf=$GUARD_RUNTMP/targets.$$
  printf '%s\n' "$entry" > "$tf"
  hit=$(scan_batch "$tf" 2>/dev/null)
  rm -f -- "$tf"
  [[ -n $hit ]]
}

# ───────────────────────────────────────────────────────────────── candidate rules

excluded_name() {
  case $1 in
    systemd-private-*|.X11-unix|.ICE-unix|.font-unix|.XIM-unix|.Test-unix|snap-private-tmp) return 0 ;;
    tmux-*|ssh-*|*.sock|*.lock|dbfix) return 0 ;;
  esac
  return 1
}

declare -a KEEP=()
load_keep() {
  KEEP=()
  local file=${1:-$KEEP_FILE} line
  [[ -r $file ]] || return 0
  while IFS= read -r line || [[ -n $line ]]; do
    line=${line%$'\r'}
    [[ -z $line || $line == '#'* ]] && continue
    KEEP+=( "$line" )
  done < "$file"
  return 0
}

keep_listed() { # path -> 0 when listed in HYAKU_DISK_KEEP
  local p=$1 rp k krp
  ((${#KEEP[@]})) || return 1
  rp=$(realpath -m -- "$p" 2>/dev/null) || rp=$p
  for k in "${KEEP[@]}"; do
    [[ $p == "$k" || $rp == "$k" ]] && return 0
    krp=$(realpath -m -- "$k" 2>/dev/null) || krp=$k
    [[ $rp == "$krp" ]] && return 0
  done
  return 1
}

collect_entries() { # root -> newline-separated top-level entries (hidden included)
  local root=$1 e
  shopt -s nullglob dotglob
  local -a entries=( "$root"/* )
  shopt -u dotglob nullglob
  for e in "${entries[@]}"; do
    printf '%s\n' "$e"
  done
  return 0
}

# classify_entry: log the first applicable keep/defer reason; 0 = eligible for deletion
classify_entry() { # path emergency
  local e=$1 emergency=$2 name age rp
  name=${e##*/}
  if [[ -L $e ]]; then
    log_line keep-excluded "$e" '?' '?' 'symlink-not-followed'
    return 1
  fi
  if excluded_name "$name"; then
    log_line keep-excluded "$e" '?' '?' "hard-exclusion name=$name"
    return 1
  fi
  if keep_listed "$e"; then
    log_line keep-listed "$e" '?' '?' 'listed in keep file'
    return 1
  fi
  rp=$(realpath -e -- "$e" 2>/dev/null) || {
    log_line defer "$e" '?' '?' 'unresolvable realpath'
    return 1
  }
  if ! under_roots "$rp"; then
    log_line defer "$e" '?' '?' "outside-configured-roots realpath=$rp"
    return 1
  fi
  if [[ ! -d $rp && ! -f $rp ]]; then
    log_line keep-excluded "$e" '?' '?' 'not-a-file-or-directory'
    return 1
  fi
  if [[ ! -d $rp ]] && (( ! emergency )); then
    log_line keep-excluded "$e" '?' '?' 'plain-file-requires-emergency'
    return 1
  fi
  age=$(age_min "$rp")
  if [[ $age != '?' ]] && (( age < MIN_AGE_MIN )); then
    log_line keep-young "$e" '?' "$age" "younger-than-min-age=${MIN_AGE_MIN}m"
    return 1
  fi
  return 0
}

sizes_of() { # [overall_budget_s] ; paths on stdin -> "<kb>\t<path>" for the ones du sized
  local budget=${1:-} rc=0
  if [[ -n $budget ]]; then
    timeout --kill-after=5 "$budget" \
      xargs -r -d '\n' -n 1 -P "$JOBS" timeout "$DU_TIMEOUT" du -xsk -- 2>/dev/null || rc=$?
  else
    xargs -r -d '\n' -n 1 -P "$JOBS" timeout "$DU_TIMEOUT" du -xsk -- 2>/dev/null || rc=$?
  fi
  return "$rc"
}

# ───────────────────────────────────────────────────────────────── check

cmd_check() {
  local quiet=${1:-} rc=0 seen=0 root pct
  NOW_TS=$(date +%s)
  for root in "${ROOTS[@]}"; do
    [[ -d $root ]] || continue
    seen=1
    if ! pct=$(usage_of "$root"); then
      log_line pressure "$root" '?' '?' 'usage-unavailable'
      printf 'error root=%s usage-unavailable\n' "$root"
      rc=2
      continue
    fi
    if (( pct >= SOFT_PCT )); then
      log_line pressure "$root" '?' '?' "use=${pct}% soft=${SOFT_PCT}%"
      printf 'pressure root=%s use=%s%% soft=%s%% target=%s%%\n' "$root" "$pct" "$SOFT_PCT" "$TARGET_PCT"
      if (( rc == 0 )); then rc=1; fi
    elif [[ -z $quiet ]]; then
      log_line ok "$root" '?' '?' "use=${pct}%"
      printf 'ok root=%s use=%s%% soft=%s%%\n' "$root" "$pct" "$SOFT_PCT"
    fi
  done
  (( seen )) || warn "no configured root exists (${ROOTS_RAW})"
  return "$rc"
}

# ───────────────────────────────────────────────────────────────── status

status_consumers() { # root
  local root=$1 sized p kb n=0 sizer_rc=0
  local -a paths=()
  while IFS= read -r p; do
    [[ -n $p ]] && paths+=( "$p" )
  done < <(collect_entries "$root")
  if ((${#paths[@]} == 0)); then
    printf '  (no entries)\n'
    return 0
  fi
  setup_runtmp
  sized=$GUARD_RUNTMP/consumers.$$
  printf '%s\n' "${paths[@]}" | sizes_of "$STATUS_BUDGET" > "$sized" 2>/dev/null
  sizer_rc=$?
  # 124/137 = the whole pass was cut at the budget; 123/125 is xargs reporting vanished entries.
  if (( sizer_rc == 124 || sizer_rc == 137 )); then
    warn "du for $root hit the ${STATUS_BUDGET}s budget; listing what was sized"
  fi
  while IFS=$'\t' read -r kb p; do
    n=$(( n + 1 ))
    if (( n > 15 )); then break; fi
    [[ -n $p ]] || continue
    printf '  %8s %8s  %s\n' "$(human_kb "$kb")" "idle=$(age_min "$p")" "$p"
  done < <(sort -rn -- "$sized" 2>/dev/null)
  rm -f -- "$sized"
  return 0
}

cmd_status() {
  local rc=0 root pct free
  local -a present=()
  NOW_TS=$(date +%s)
  printf '%-30s %6s %8s\n' 'root' 'use%' 'free'
  for root in "${ROOTS[@]}"; do
    [[ -d $root ]] || continue
    present+=( "$root" )
    if ! pct=$(usage_of "$root"); then
      printf '%-30s %5s %8s\n' "$root" 'ERR' '-'
      rc=2
      continue
    fi
    free=$(free_kb_of "$root")
    if [[ $free == '?' ]]; then free='-'; else free=$(human_kb "$free"); fi
    printf '%-30s %5s%% %8s\n' "$root" "$pct" "$free"
    if (( pct >= SOFT_PCT )) && (( rc == 0 )); then rc=1; fi
  done
  for root in "${present[@]}"; do
    printf '\ntop consumers %s\n' "$root"
    status_consumers "$root"
  done
  return "$rc"
}

# ───────────────────────────────────────────────────────────────── sweep

sweep_root() { # root dry emergency all -> rc
  local root=$1 dry=$2 emergency=$3 all=$4
  local pct base_pct final kb p mb idle age rp cur rec root_real total_kb sim_kb
  local -a eligible=() order=()
  local -A SIZE=() LIVESNAP=()

  NOW_TS=$(date +%s)
  if ! pct=$(usage_of "$root"); then
    log_line pressure "$root" '?' '?' 'usage-unavailable'
    warn "cannot read usage for $root"
    return 2
  fi
  base_pct=$pct
  if (( pct < SOFT_PCT )) && (( !all && !emergency )); then
    log_line ok "$root" '?' '?' "below-soft use=${pct}% soft=${SOFT_PCT}%"
    printf 'ok %s use=%s%% below soft=%s%%\n' "$root" "$pct" "$SOFT_PCT"
    return 0
  fi
  log_line pressure "$root" '?' '?' "use=${pct}% soft=${SOFT_PCT}% target=${TARGET_PCT}% emergency=${emergency} all=${all}"
  printf 'pressure %s use=%s%% soft=%s%% target=%s%%\n' "$root" "$pct" "$SOFT_PCT" "$TARGET_PCT"

  while IFS= read -r p; do
    [[ -n $p ]] || continue
    classify_entry "$p" "$emergency" || continue
    eligible+=( "$p" )
  done < <(collect_entries "$root")

  if ((${#eligible[@]} == 0)); then
    log_line ok "$root" '?' '?' 'no-eligible-entries'
    printf 'ok %s no eligible entries\n' "$root"
    if (( pct < SOFT_PCT )); then return 0; fi
    return 1
  fi

  setup_runtmp
  local sized=$GUARD_RUNTMP/sizes.$$
  : > "$sized"
  printf '%s\n' "${eligible[@]}" | sizes_of > "$sized" 2>/dev/null
  while IFS=$'\t' read -r kb p; do
    [[ $kb =~ ^[0-9]+$ && -n $p ]] && SIZE["$p"]=$kb
  done < "$sized"
  rm -f -- "$sized"

  # Emergency-only plain files under the 100 MB floor are not worth deleting. They are counted
  # rather than logged one by one: a busy /tmp carries thousands of them and the drivers call
  # `sweep --emergency` on every pressurised dispatch.
  local -a kept=()
  local small_count=0 small_kb=0
  for p in "${eligible[@]}"; do
    if [[ ! -d $p && $emergency -eq 1 ]]; then
      kb=${SIZE[$p]:-}
      if [[ -n $kb ]] && (( kb < PLAIN_FILE_MIN_KB )); then
        small_count=$(( small_count + 1 ))
        small_kb=$(( small_kb + kb ))
        continue
      fi
    fi
    kept+=( "$p" )
  done
  if (( small_count )); then
    log_line keep-excluded "$root" "$(mb_of "$small_kb")" '?' \
      "plain-files-under-${PLAIN_FILE_MIN_KB}kb not-listed count=${small_count}"
  fi
  eligible=()
  ((${#kept[@]})) && eligible=( "${kept[@]}" )

  # Largest first; unknown sizes last but still eligible.
  while IFS= read -r rec; do
    [[ -n $rec ]] && order+=( "$rec" )
  done < <({
    for p in "${eligible[@]}"; do
      kb=${SIZE[$p]:-}
      [[ -n $kb ]] && printf '%s\t%s\n' "$kb" "$p"
    done | sort -rn
    for p in "${eligible[@]}"; do
      [[ -n ${SIZE[$p]:-} ]] || printf '?\t%s\n' "$p"
    done
  })

  root_real=$(realpath -m -- "$root" 2>/dev/null) || root_real=$root
  total_kb=$(total_kb_of "$root")

  # One batched process scan for the whole candidate set: a root can carry thousands of
  # top-level entries, so scanning per entry would cost minutes. Anything actually deleted is
  # re-checked with a fresh targeted scan immediately before the rm.
  local tf=$GUARD_RUNTMP/live.$$
  printf '%s\n' "${eligible[@]}" > "$tf"
  while IFS= read -r p; do
    [[ -n $p ]] && LIVESNAP["$p"]=1
  done < <(scan_batch "$tf" | sort -u)
  rm -f -- "$tf"

  sim_kb=0
  for rec in "${order[@]}"; do
    cur=$(usage_of "$root" 2>/dev/null) || cur=$pct
    if (( dry )); then
      cur=$(( cur - (sim_kb * 100) / total_kb ))
      (( cur < 0 )) && cur=0
    fi
    if (( cur < TARGET_PCT )); then break; fi
    p=${rec#*$'\t'}
    kb=${rec%%$'\t'*}
    [[ -n ${SIZE[$p]:-} ]] && kb=${SIZE[$p]}
    mb=$(mb_of "$kb")
    idle=$(age_min "$p")
    if [[ -n ${LIVESNAP[$p]:-} ]] || entry_recent "$p"; then
      log_line keep-live "$p" "$mb" "$idle" 'live-process-or-recent-write'
      continue
    fi
    rp=$(realpath -e -- "$p" 2>/dev/null) || {
      log_line defer "$p" "$mb" "$idle" 'vanished-before-rm'
      continue
    }
    if ! under_roots "$rp"; then
      log_line defer "$p" "$mb" "$idle" "outside-configured-roots realpath=$rp"
      continue
    fi
    if [[ $(dirname -- "$rp") != "$root_real" ]]; then
      log_line defer "$p" "$mb" "$idle" "not-a-top-level-entry realpath=$rp"
      continue
    fi
    if (( dry )); then
      log_line dry-run "$rp" "$mb" "$idle" "would-delete projected=${cur}%"
      printf 'dry-run %s size_mb=%s idle=%s\n' "$rp" "$mb" "$idle"
      if [[ $kb =~ ^[0-9]+$ ]]; then sim_kb=$(( sim_kb + kb )); fi
      continue
    fi
    if entry_live "$p"; then
      log_line keep-live "$p" "$mb" "$idle" 'live-on-recheck-before-rm'
      continue
    fi
    if rm -rf --one-file-system -- "$rp" 2>/dev/null; then
      if [[ $kb =~ ^[0-9]+$ ]]; then
        DEL_KB["$root"]=$(( ${DEL_KB[$root]:-0} + kb ))
      fi
      log_line delete "$rp" "$mb" "$idle" "freed use-before=${cur}%"
      printf 'delete %s size_mb=%s idle=%s\n' "$rp" "$mb" "$idle"
    else
      log_line defer "$rp" "$mb" "$idle" 'rm-failed'
      printf 'defer %s size_mb=%s rm-failed\n' "$rp" "$mb"
    fi
  done

  if (( dry )); then
    final=$base_pct                        # nothing was removed: pressure is unchanged
  else
    final=$(usage_of "$root" 2>/dev/null) || final=$pct
  fi
  if (( final < SOFT_PCT )); then
    log_line ok "$root" '?' '?' "after-sweep use=${final}%"
    printf 'ok %s use=%s%% after sweep\n' "$root" "$final"
    return 0
  fi
  log_line pressure "$root" '?' '?' "still use=${final}% soft=${SOFT_PCT}%"
  printf 'pressure %s use=%s%% after sweep soft=%s%%\n' "$root" "$final" "$SOFT_PCT"
  return 1
}

cmd_sweep() {
  local dry=0 emergency=0 all=0 arg worst=0 rc seen=0 root
  for arg in "$@"; do
    case $arg in
      --dry-run) dry=1 ;;
      --emergency) emergency=1 ;;
      --all) all=1 ;;
      *) die "sweep: unknown option '$arg'" ;;
    esac
  done
  (( emergency )) && IDLE_MIN=10
  for root in "${ROOTS[@]}"; do
    [[ -d $root ]] || continue
    seen=1
    sweep_root "$root" "$dry" "$emergency" "$all"
    rc=$?
    if (( rc > worst )); then worst=$rc; fi
  done
  (( seen )) || warn "no configured root exists (${ROOTS_RAW})"
  return "$worst"
}

# ───────────────────────────────────────────────────────────────── purge-lane

cmd_purge_lane() {
  local lane='' round='' dry=0 arg mb kb idle rp scrub target
  for arg in "$@"; do
    case $arg in
      --dry-run) dry=1 ;;
      -*) die "purge-lane: unknown option '$arg'" ;;
      *)
        if [[ -z $lane ]]; then
          lane=$arg
        elif [[ -z $round ]]; then
          round=$arg
        else
          die 'purge-lane: too many arguments'
        fi
        ;;
    esac
  done
  [[ -n $lane && -n $round ]] || die 'usage: purge-lane <lane> <round> [--dry-run]'
  [[ $lane =~ ^[a-z0-9-]+$ ]] || die "purge-lane: invalid lane id '$lane'"
  [[ $round =~ ^[0-9]+$ ]] || die "purge-lane: invalid round '$round'"

  target="$HYAKU_SCRATCH/${lane}-r${round}"
  if [[ ! -e $target && ! -L $target ]]; then
    log_line ok "$target" '?' '?' 'absent'
    printf 'absent %s\n' "$target"
    return 0
  fi
  scrub=$(realpath -m -- "$HYAKU_SCRATCH" 2>/dev/null) || scrub=''
  rp=$(realpath -e -- "$target" 2>/dev/null) || {
    log_line defer "$target" '?' '?' 'unresolvable realpath'
    printf 'unresolvable %s\n' "$target"
    return 2
  }
  if [[ -z $scrub || $rp == "$scrub" || $rp != "$scrub"/* ]]; then
    die "purge-lane: $rp is not strictly under $HYAKU_SCRATCH"
  fi
  kb=$(timeout "$DU_TIMEOUT" du -xsk -- "$rp" 2>/dev/null)
  kb=${kb%%[[:space:]]*}
  mb=$(mb_of "${kb:-}")
  idle=$(age_min "$rp")

  if entry_live "$rp"; then
    log_line keep-live "$rp" "$mb" "$idle" "purge-lane ${lane}-r${round}: live process inside"
    printf 'live %s size_mb=%s idle=%s\n' "$rp" "$mb" "$idle"
    return 1
  fi
  if (( dry )); then
    log_line dry-run "$rp" "$mb" "$idle" "purge-lane ${lane}-r${round}"
    printf 'dry-run %s size_mb=%s idle=%s\n' "$rp" "$mb" "$idle"
    return 0
  fi
  if rm -rf --one-file-system -- "$rp" 2>/dev/null; then
    log_line delete "$rp" "$mb" "$idle" "purge-lane ${lane}-r${round}"
    printf 'delete %s size_mb=%s idle=%s\n' "$rp" "$mb" "$idle"
    return 0
  fi
  log_line defer "$rp" "$mb" "$idle" 'rm-failed'
  printf 'defer %s size_mb=%s rm-failed\n' "$rp" "$mb"
  return 2
}

# ───────────────────────────────────────────────────────────────── watch

cmd_watch() {
  local interval=180 rc hard root pct
  while (($#)); do
    case $1 in
      --interval)
        shift
        (($#)) || die 'watch: --interval needs a value'
        interval=$1
        ;;
      --interval=*) interval=${1#--interval=} ;;
      *) die "watch: unknown option '$1'" ;;
    esac
    shift
  done
  [[ $interval =~ ^[0-9]+$ ]] && (( interval > 0 )) || die 'watch: interval must be a positive integer'
  while :; do
    hard=0
    for root in "${ROOTS[@]}"; do
      [[ -d $root ]] || continue
      if pct=$(usage_of "$root"); then
        if (( pct >= HARD_PCT )); then hard=1; fi
      fi
    done
    cmd_check quiet
    rc=$?
    case $rc in
      0) : ;;
      2) warn "check reported an environment error; retrying in ${interval}s" ;;
      *)
        if (( hard )); then
          log_line pressure all '?' '?' "hard-threshold=${HARD_PCT}% sweep-emergency"
          cmd_sweep --emergency || warn "emergency sweep returned $?"
        else
          cmd_sweep || warn "sweep returned $?"
        fi
        ;;
    esac
    printf 'watch: pass rc=%s interval=%ss\n' "$rc" "$interval"
    sleep "$interval"
  done
}

# ───────────────────────────────────────────────────────────────── selftest

ST_BASE='' ST_LOGDIR='' ST_CASE='' ST_OVERRIDE='' ST_ROOTS='' ST_KEEP='' ST_SCRATCH=''
ST_TAP_PASS=0 ST_TAP_TOTAL=0

st_check() { # label expected actual
  local label=$1 expected=$2 actual=$3
  ST_TAP_TOTAL=$(( ST_TAP_TOTAL + 1 ))
  if [[ $expected == "$actual" ]]; then
    ST_TAP_PASS=$(( ST_TAP_PASS + 1 ))
    printf 'PASS %s\n' "$label"
  else
    printf 'FAIL %s: expected %s, got %s\n' "$label" "$expected" "$actual"
  fi
  return 0
}

st_check_bool() { # label expected(1/0) -- command...
  local label=$1 expected=$2 actual
  shift 2
  if "$@"; then actual=1; else actual=0; fi
  st_check "$label" "$expected" "$actual"
}

st_fill() { # path kb
  dd if=/dev/zero of="$1" bs=1024 count="$2" status=none 2>/dev/null
}

st_old_tree() { # path — age the entry and everything under it
  local p=$1
  find "$p" -mindepth 1 -exec touch -d '2 hours ago' -- {} + 2>/dev/null
  touch -d '2 hours ago' -- "$p"
}

st_guard() { # [KEY=VALUE ...] <disk-guard args...>
  local -a overrides=()
  while (($#)); do
    case $1 in
      [A-Z_]*=*) overrides+=( "$1" ); shift ;;
      *) break ;;
    esac
  done
  env -i \
    PATH="$PATH" HOME="$HOME" \
    TMPDIR="$ST_BASE/tmp" \
    FLEET="$ST_BASE/fleet" \
    HYAKU_ENV_FILE="$ST_BASE/absent-hyaku.env" \
    HYAKU_DISK_ROOTS="$ST_ROOTS" \
    HYAKU_DISK_LOG="$ST_LOGDIR/$ST_CASE.log" \
    HYAKU_DISK_KEEP="$ST_KEEP" \
    HYAKU_DISK_USAGE_OVERRIDE="$ST_OVERRIDE" \
    HYAKU_SCRATCH="$ST_SCRATCH" \
    SOFT_PCT=70 TARGET_PCT=60 HARD_PCT=90 \
    IDLE_MIN=45 MIN_AGE_MIN=10 DU_TIMEOUT=30 \
    "${overrides[@]}" \
    bash "$SELF_PATH" "$@"
}

st_log() { printf '%s\n' "$ST_LOGDIR/$ST_CASE.log"; }
st_log_has() { grep -qF -- "$1" "$(st_log)" 2>/dev/null; }

st_case_live_kept() {
  local r="$ST_BASE/root-live" pid out rc
  mkdir -p -- "$r/live-dir" "$ST_BASE/tmp"
  st_fill "$r/live-dir/blob" 300
  st_old_tree "$r/live-dir"
  ( cd "$r/live-dir" && exec sleep 120 ) >/dev/null 2>&1 &
  pid=$!
  ST_ROOTS=$r ST_CASE=live-kept ST_OVERRIDE="$r=80@1000"
  out=$(st_guard sweep 2>&1)
  rc=$?
  : "$out"
  st_check_bool live-process-dir-kept 1 test -d "$r/live-dir"
  st_check_bool live-process-logged 1 st_log_has "keep-live $r/live-dir"
  st_check live-process-exit-code 1 "$rc"
  kill "$pid" 2>/dev/null
  wait "$pid" 2>/dev/null
  return 0
}

cmd_selftest() {
  local rc=0 out label r pid base_keep
  ST_TAP_PASS=0 ST_TAP_TOTAL=0
  ST_BASE=$(mktemp -d "${TMPDIR:-/var/tmp}/disk-guard-selftest.XXXXXX" 2>/dev/null) || {
    printf 'selftest: cannot create fixture base\n' >&2
    return 1
  }
  SELFTEST_BASE=$ST_BASE
  ST_LOGDIR=$ST_BASE/logs
  ST_SCRATCH=$ST_BASE/scratch
  ST_KEEP=$ST_BASE/keep-empty
  mkdir -p -- "$ST_LOGDIR" "$ST_BASE/tmp" "$ST_SCRATCH" "$ST_BASE/fleet"
  : > "$ST_KEEP"

  # 1 — an old, idle directory is deleted
  r=$ST_BASE/root-idle
  mkdir -p -- "$r/abandoned"
  st_fill "$r/abandoned/blob" 300
  st_old_tree "$r/abandoned"
  ST_ROOTS=$r ST_CASE=idle ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  rc=$?
  st_check_bool idle-old-dir-deleted 0 test -e "$r/abandoned"
  st_check idle-old-exit-code 0 "$rc"
  st_check_bool idle-old-logged 1 st_log_has "delete $r/abandoned"

  # 2 — a directory holding a live process is kept
  st_case_live_kept

  # 3 — a directory with a recently modified file is kept
  r=$ST_BASE/root-recent
  mkdir -p -- "$r/recent-dir"
  st_fill "$r/recent-dir/blob" 300
  st_old_tree "$r/recent-dir"
  touch -- "$r/recent-dir/blob"
  ST_ROOTS=$r ST_CASE=recent ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  rc=$?
  st_check_bool recent-file-dir-kept 1 test -d "$r/recent-dir"
  st_check_bool recent-file-logged 1 st_log_has "keep-live $r/recent-dir"

  # 4 — a young directory is kept
  r=$ST_BASE/root-young
  mkdir -p -- "$r/young-dir"
  st_fill "$r/young-dir/blob" 300
  ST_ROOTS=$r ST_CASE=young ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  st_check_bool young-dir-kept 1 test -d "$r/young-dir"
  st_check_bool young-dir-logged 1 st_log_has "keep-young $r/young-dir"

  # 5 — a keep-listed path is kept
  r=$ST_BASE/root-keep
  mkdir -p -- "$r/listed-dir"
  st_fill "$r/listed-dir/blob" 300
  st_old_tree "$r/listed-dir"
  base_keep=$ST_BASE/keep-listed
  printf '%s\n' "$r/listed-dir" > "$base_keep"
  ST_ROOTS=$r ST_CASE=keep ST_OVERRIDE="$r=80@1000" ST_KEEP=$base_keep
  st_guard sweep >/dev/null 2>&1
  st_check_bool keep-listed-dir-kept 1 test -d "$r/listed-dir"
  st_check_bool keep-listed-logged 1 st_log_has "keep-listed $r/listed-dir"
  ST_KEEP=$ST_BASE/keep-empty

  # 6 — hard-excluded names are kept
  r=$ST_BASE/root-excluded
  mkdir -p -- "$r/.X11-unix" "$r/tmux-fixture" "$r/dbfix" "$r/stray.sock"
  for label in .X11-unix tmux-fixture dbfix stray.sock; do
    st_fill "$r/$label/blob" 300
    st_old_tree "$r/$label"
  done
  ST_ROOTS=$r ST_CASE=excluded ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  local kept_all=1
  for label in .X11-unix tmux-fixture dbfix stray.sock; do
    [[ -d $r/$label ]] || kept_all=0
  done
  st_check excluded-names-kept 1 "$kept_all"
  st_check_bool excluded-logged 1 st_log_has "keep-excluded $r/dbfix"

  # 7 — symlinks are kept and not followed
  r=$ST_BASE/root-symlink
  mkdir -p -- "$r" "$ST_BASE/outside-target"
  st_fill "$ST_BASE/outside-target/blob" 300
  st_old_tree "$ST_BASE/outside-target"
  ln -s -- "$ST_BASE/outside-target" "$r/link-out"
  ST_ROOTS=$r ST_CASE=symlink ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  st_check_bool symlink-kept 1 test -L "$r/link-out"
  st_check_bool symlink-target-intact 1 test -f "$ST_BASE/outside-target/blob"
  st_check_bool symlink-logged 1 st_log_has "keep-excluded $r/link-out"

  # 8 — --dry-run deletes nothing
  r=$ST_BASE/root-dry
  mkdir -p -- "$r/doomed"
  st_fill "$r/doomed/blob" 300
  st_old_tree "$r/doomed"
  ST_ROOTS=$r ST_CASE=dry ST_OVERRIDE="$r=80@1000"
  out=$(st_guard sweep --dry-run 2>&1)
  rc=$?
  st_check_bool dry-run-dir-survives 1 test -d "$r/doomed"
  st_check_bool dry-run-printed 1 grep -qF "dry-run $r/doomed" <<<"$out"
  st_check_bool dry-run-logged 1 st_log_has "dry-run $r/doomed"
  st_check dry-run-exit-code 1 "$rc"

  # 9 — usage below SOFT deletes nothing
  r=$ST_BASE/root-quiet
  mkdir -p -- "$r/untouched"
  st_fill "$r/untouched/blob" 300
  st_old_tree "$r/untouched"
  ST_ROOTS=$r ST_CASE=quiet ST_OVERRIDE="$r=50@1000"
  st_guard sweep >/dev/null 2>&1
  rc=$?
  st_check_bool below-soft-dir-survives 1 test -d "$r/untouched"
  st_check below-soft-exit-code 0 "$rc"
  st_check_bool below-soft-logged 1 st_log_has "ok $r"

  # 10 — largest first, then stop below TARGET
  r=$ST_BASE/root-order
  mkdir -p -- "$r/big" "$r/mid" "$r/small"
  st_fill "$r/big/blob" 120
  st_fill "$r/mid/blob" 110
  st_fill "$r/small/blob" 100
  st_old_tree "$r/big"
  st_old_tree "$r/mid"
  st_old_tree "$r/small"
  ST_ROOTS=$r ST_CASE=order ST_OVERRIDE="$r=80@1000"
  st_guard sweep >/dev/null 2>&1
  rc=$?
  st_check_bool largest-deleted 0 test -e "$r/big"
  st_check_bool next-largest-deleted 0 test -e "$r/mid"
  st_check_bool smallest-kept 1 test -d "$r/small"
  st_check order-stopped-below-target-exit-code 0 "$rc"
  st_check largest-first-order "$r/big $r/mid" \
    "$(awk '$2=="delete" {print $3}' "$(st_log)" 2>/dev/null | tr '\n' ' ' | sed 's/ $//')"

  # 11 — purge-lane removes exactly its own round directory
  rm -rf --one-file-system -- "$ST_SCRATCH"/* 2>/dev/null
  mkdir -p -- "$ST_SCRATCH/alpha-r7/seat1" "$ST_SCRATCH/beta-r7/seat1" "$ST_SCRATCH/alpha-r70/seat1"
  st_fill "$ST_SCRATCH/alpha-r7/seat1/blob" 8
  st_old_tree "$ST_SCRATCH/alpha-r7"
  ST_ROOTS=$ST_SCRATCH ST_CASE=purge ST_OVERRIDE="$ST_SCRATCH=50@1000" ST_KEEP=$ST_BASE/keep-empty
  st_guard purge-lane alpha 7 >/dev/null 2>&1
  rc=$?
  st_check purge-lane-exit-code 0 "$rc"
  st_check_bool purge-lane-removed-target 0 test -e "$ST_SCRATCH/alpha-r7"
  st_check_bool purge-lane-kept-sibling 1 test -d "$ST_SCRATCH/beta-r7/seat1"
  st_check_bool purge-lane-kept-other-round 1 test -d "$ST_SCRATCH/alpha-r70/seat1"

  mkdir -p -- "$ST_SCRATCH/alpha-r7/seat1"
  st_fill "$ST_SCRATCH/alpha-r7/seat1/blob" 8
  ( cd "$ST_SCRATCH/alpha-r7/seat1" && exec sleep 120 ) >/dev/null 2>&1 &
  pid=$!
  st_old_tree "$ST_SCRATCH/alpha-r7"       # only the process can make this live
  st_guard purge-lane alpha 7 >/dev/null 2>&1
  rc=$?
  st_check purge-lane-live-exit-code 1 "$rc"
  st_check_bool purge-lane-live-kept 1 test -d "$ST_SCRATCH/alpha-r7/seat1"
  kill "$pid" 2>/dev/null
  wait "$pid" 2>/dev/null

  st_guard purge-lane 'BAD!' 7 >/dev/null 2>&1
  st_check purge-lane-invalid-lane-exit-code 2 "$?"
  st_guard purge-lane alpha 'x7' >/dev/null 2>&1
  st_check purge-lane-invalid-round-exit-code 2 "$?"
  st_guard purge-lane alpha 9 >/dev/null 2>&1
  st_check purge-lane-absent-exit-code 0 "$?"
  st_old_tree "$ST_SCRATCH/alpha-r7"       # the surviving live tree is idle again
  st_guard purge-lane alpha 7 --dry-run >/dev/null 2>&1
  st_check purge-lane-dry-run-exit-code 0 "$?"

  # 12 — exit codes 0 / 1 / 2
  r=$ST_BASE/root-codes
  mkdir -p -- "$r/entry"
  st_old_tree "$r/entry"
  ST_ROOTS=$r ST_CASE=codes ST_OVERRIDE="$r=50@1000"
  st_guard check >/dev/null 2>&1
  st_check check-below-soft-exit-code 0 "$?"
  ST_CASE=codes-pressure ST_OVERRIDE="$r=99@1000"
  out=$(st_guard check 2>&1)
  rc=$?
  st_check check-pressure-exit-code 1 "$rc"
  st_check_bool check-pressure-printed 1 grep -qF "pressure root=$r use=99%" <<<"$out"
  st_guard not-a-command >/dev/null 2>&1
  st_check unknown-command-exit-code 2 "$?"
  ST_CASE=codes-badenv
  st_guard SOFT_PCT=abc check >/dev/null 2>&1
  st_check bad-env-exit-code 2 "$?"
  ST_OVERRIDE="$r=50@1000"
  st_guard status >/dev/null 2>&1
  st_check status-exit-code 0 "$?"

  # 13 — seeded-defect arm: the gate must be able to fail
  if [[ ${DISK_GUARD_SELFTEST_NO_MUTATE:-0} == 1 ]]; then
    printf 'SKIP seeded-defect-arm (mutation run)\n'
  else
    local mutant=$ST_BASE/mutant-disk-guard.sh
    if sed 's|^scan_batch() {\(.*\)$|scan_batch() {\1\n  return 0  # seeded defect: no process is ever live|' \
      "$SELF_PATH" > "$mutant" 2>/dev/null && ! cmp -s "$SELF_PATH" "$mutant"; then
      out=$(env -i PATH="$PATH" HOME="$HOME" TMPDIR="$ST_BASE/tmp" \
        DISK_GUARD_SELFTEST_NO_MUTATE=1 bash "$mutant" selftest 2>&1)
      rc=$?
      printf 'seeded-defect-arm: mutant exit=%s, FAIL lines=%s\n' "$rc" \
        "$(grep -c '^FAIL ' <<<"$out")"
      if (( rc != 0 )) && grep -q '^FAIL ' <<<"$out"; then
        st_check seeded-defect-arm 1 1
      else
        st_check seeded-defect-arm 1 0
      fi
    else
      st_check seeded-defect-arm 1 0
    fi
  fi

  printf 'selftest %s/%s\n' "$ST_TAP_PASS" "$ST_TAP_TOTAL"
  if (( ST_TAP_PASS == ST_TAP_TOTAL )); then
    return 0
  fi
  return 1
}

# ───────────────────────────────────────────────────────────────── dispatch

usage() {
  cat <<'USAGE'
disk-guard.sh check
disk-guard.sh status
disk-guard.sh sweep [--dry-run] [--emergency] [--all]
disk-guard.sh purge-lane <lane> <round> [--dry-run]
disk-guard.sh watch [--interval SECS]
disk-guard.sh selftest
Exits: 0 clean · 1 pressure/live · 2 usage or environment error.
USAGE
}

CMD=${1:-}
if (($#)); then shift; fi
case $CMD in
  check)
    validate_env
    parse_override
    cmd_check
    ;;
  status)
    validate_env
    parse_override
    cmd_status
    ;;
  sweep)
    validate_env
    parse_override
    setup_runtmp
    load_keep
    cmd_sweep "$@"
    ;;
  purge-lane)
    validate_env
    parse_override
    cmd_purge_lane "$@"
    ;;
  watch)
    validate_env
    parse_override
    setup_runtmp
    cmd_watch "$@"
    ;;
  selftest)
    cmd_selftest
    ;;
  ''|-h|--help|help)
    usage >&2
    exit 2
    ;;
  *)
    printf 'disk-guard: unknown command %s\n' "$CMD" >&2
    usage >&2
    exit 2
    ;;
esac
exit $?
