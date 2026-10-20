#!/usr/bin/env bash
# hyaku (百) slot driver — respawn-per-round shokunin training, one slot of N.
#
# Operator directive 2026-10-19: train every shokunin lane to at least round
# 100, 2-3 lanes concurrently, each round its own omp session rooted in the
# lane's own repo, swarm waves of 32-64, commit+push after every round.
#
# Reuses the canonical driver (scripts/shokunin-watchdog.sh, sourced for its
# definitions only): render_prompt, report_of, record_report_baseline, log.
# Differences from the canonical tick loop, by design:
#   - the lane process runs in the FOREGROUND and is never killed on report
#     landing (no report-written-but-uncommitted kill race, no tick latency);
#   - after a landed round a fresh non-author closure session (integrator of
#     record) verifies it and appends the MANIFEST.json closure entry, before
#     the lane's next round starts;
#   - lanes are scheduled lowest-round-first across slots (claims under flock).
#
#   slot-driver.sh <slot-id>
# Control files under $HYAKU_STATE: stop (all slots exit after their current
# round), pause-<slot>, blocked/<lane>, next/<lane>, claims/<lane>/owner.
set -u
SLOT=${1:?usage: slot-driver.sh <slot-id>}
FLEET=/home/vgpnk/Projects/shokunin
H="$FLEET/scripts/hyaku"
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
CANON=${SHOKUNIN_PLUGIN:-$HOME/Projects/kimi-shokunin}
export SHOKUNIN_ROOT=$FLEET HYAKU_STATE=$STATE
mkdir -p "$STATE"/{next,claims,blocked,logs,outcome}

# Canonical driver definitions (sourcing runs config parsing only; main() is not invoked).
# shellcheck disable=SC1091
. "$FLEET/scripts/shokunin-watchdog.sh"

load_env() { # re-read every round so routing/limits change without restarting slots
  L1_MODEL=@m_strong JUDGE_MODEL=@m_opus TARGET=100 MAX_ATTEMPTS=3
  ROUND_MAXTIME=170m ROUND_TIMEOUT=180m CLOSURE_MAXTIME=60m CLOSURE_TIMEOUT=70m
  # shellcheck disable=SC1091
  [ -f "$H/hyaku.env" ] && . "$H/hyaku.env"
}

ev() { printf '%s slot=%s %s\n' "$(date -Is)" "$SLOT" "$*" >> "$STATE/events.log"; printf '%s %s\n' "$(date -Is)" "$*"; }
status() { printf '%s %s\n' "$(date -Is)" "$*" > "$STATE/slot-$SLOT.status"; }

cleanup_own_claims() {
  local d
  for d in "$STATE"/claims/*/; do
    [ -d "$d" ] || continue
    [ "$(cat "$d/owner" 2>/dev/null)" = "$SLOT" ] && rm -rf -- "$d"
  done
}

pick_lane() { # prints the claimed lane, or nothing
  local sl best='' bestn=999999 lane n
  exec {sl}>"$STATE/sched.lock"; flock "$sl"
  while read -r lane _; do
    case $lane in ''|\#*) continue ;; esac
    [ -n "${LANE_CWD[$lane]:-}" ] || continue
    [ -e "$STATE/blocked/$lane" ] && continue
    [ -d "$STATE/claims/$lane" ] && continue
    n=$(cat "$STATE/next/$lane" 2>/dev/null) || continue
    case $n in ''|*[!0-9]*) continue ;; esac
    [ "$n" -le "$TARGET" ] || continue
    if [ "$n" -lt "$bestn" ] || { [ "$n" -eq "$bestn" ] && [ "$lane" = "${LAST_LANE:-}" ]; }; then
      best=$lane; bestn=$n
    fi
  done < "$H/pool.txt"
  if [ -n "$best" ]; then
    { mkdir "$STATE/claims/$best" && printf '%s\n' "$SLOT" > "$STATE/claims/$best/owner"; } || best=''
  fi
  flock -u "$sl"; exec {sl}>&-
  printf '%s\n' "$best"
}

subst() { # template-file lane round attempt -> stdout with hyaku placeholders replaced (literal, & safe)
  local t lane=$2 n=$3 a=$4
  shopt -u patsub_replacement 2>/dev/null || true
  t=$(cat -- "$1") || return 1
  t=${t//"{{LANE_CWD}}"/"${LANE_CWD[$lane]}"}
  t=${t//"{{LANE_REPO}}"/"${LANE_REPO[$lane]}"}
  t=${t//"{{LANE}}"/"$lane"}
  t=${t//"{{ROUND}}"/"$n"}
  t=${t//"{{PREV}}"/"$((n-1))"}
  t=${t//"{{ATTEMPT}}"/"$a"}
  t=${t//"{{TARGET}}"/"$TARGET"}
  t=${t//"{{FLEET_ROOT}}"/"$SHOKUNIN_ROOT"}
  t=${t//"{{CANON}}"/"$CANON"}
  t=${t//"{{BASE}}"/"${BASE:-}"}
  t=${t//"{{HEAD}}"/"${HEADC:-}"}
  t=${t//"{{L1_MODEL}}"/"$L1_MODEL"}
  t=${t//"{{JUDGE_MODEL}}"/"$JUDGE_MODEL"}
  t=${t//"{{DISPATCH_LINES}}"/"${DISPATCH_LINES:-}"}
  printf '%s\n' "$t"
}

run_session() { # out-file cwd model maxtime timeout prompt-file -> rc (foreground; never killed on report)
  local out=$1 cwd=$2 model=$3 maxt=$4 tmo=$5 prompt=$6
  ( cd -- "$cwd" && exec timeout -k 120 "$tmo" omp -p --cwd "$cwd" --model "$model" \
      --config "$H/omp-overlay.yml" --max-time "$maxt" "@$prompt" ) > "$out" 2>&1
}

verify_round() { # lane n -> 0 when a real report landed (committed + pushed)
  local lane=$1 n=$2 rep=".ufo/reports/round-$2/$1.md" cwd=${LANE_CWD[$1]}
  report_of "$lane" "$n" || return 1
  if [ -n "$(git -C "$FLEET" status --porcelain -- "$rep")" ] \
     || [ -z "$(git -C "$FLEET" log -1 --format=%H -- "$rep")" ]; then
    ev "sweep lane=$lane round=$n :: report on disk but uncommitted at exit (attribution defect)"
    "$H/fleet-commit.sh" --as "$lane" \
      -m "round-$n: $lane report (hyaku driver sweep: lane exited without committing; attribution defect)" \
      -- "$rep" || return 1
  fi
  if [ "$(git -C "$cwd" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)" != 0 ]; then
    if git -C "$cwd" push -q 2>>"$STATE/logs/$lane-push.err"; then
      ev "durability-push lane=$lane round=$n :: lane exited with unpushed commits"
    else
      ev "push-failed lane=$lane round=$n"
    fi
  fi
  # flush fleet commits whose push failed earlier (fleet-commit pushes whatever is ahead)
  if [ "$(git -C "$FLEET" rev-list --count origin/master..HEAD 2>/dev/null || echo 0)" != 0 ]; then
    "$H/fleet-commit.sh" --as "$lane" -m unused -- "$rep" >/dev/null 2>&1 || ev "fleet-push-pending"
  fi
  return 0
}

closure_count() { # lane n -> line1 count, line2 admitted|rejected|none
  python3 - "$FLEET/MANIFEST.json" "$1" "$2" <<'EOF'
import json,sys
d=json.load(open(sys.argv[1])); l=sys.argv[2]; n=int(sys.argv[3])
rows=[r for r in d["rounds"] if r.get("campaign")=="hyaku" and r.get("lane")==l and r.get("lane_round")==n]
print(len(rows)); last=rows[-1] if rows else {}
print("admitted" if last.get("admitted") is True else ("rejected" if rows else "none"))
EOF
}

run_closure() { # lane n -> 0 when a hyaku closure row exists
  local lane=$1 n=$2 p=".ufo/prompts/closure/$1-round-$2.md" c try out
  mkdir -p "$FLEET/.ufo/prompts/closure"
  DISPATCH_LINES=$(grep -E "^[^ ]+ (launch|complete|lane-dead-no-report) $lane round=$n( |;|$)" "$UFO/watchdog.log" | tail -8)
  subst "$H/closure-prompt.md" "$lane" "$n" 0 > "$FLEET/$p" || return 1
  "$H/fleet-commit.sh" --as protocol -m "round-$n: hyaku closure dispatch for $lane" -- "$p" >/dev/null || true
  for try in 1 2; do
    out="$STATE/logs/closure-$lane-r$n-t$try.out"
    status "closure $lane r$n try$try since $(date -Is)"
    ev "closure-launch lane=$lane round=$n try=$try model=$JUDGE_MODEL"
    run_session "$out" "$FLEET" "$JUDGE_MODEL" "$CLOSURE_MAXTIME" "$CLOSURE_TIMEOUT" "$FLEET/$p"
    c=$(closure_count "$lane" "$n" | head -1)
    if [ "${c:-0}" -ge 1 ]; then ev "closure-ok lane=$lane round=$n"; return 0; fi
    ev "closure-missing lane=$lane round=$n try=$try"
    sleep 90
  done
  return 1
}

main_loop() {
  local lane n a rc landed t0 elapsed infra=0 outcome streak k
  LAST_LANE=''
  cleanup_own_claims
  ev "slot-start pid=$$"
  while :; do
    load_env
    if [ -e "$STATE/stop" ]; then ev "stop-file: slot exits"; status "stopped"; exit 0; fi
    if [ -e "$STATE/pause-$SLOT" ]; then status "paused"; sleep 60; continue; fi
    lane=$(pick_lane)
    if [ -z "$lane" ]; then status "idle: no eligible lane"; sleep 600; continue; fi
    n=$(cat "$STATE/next/$lane")
    BASE=$(git -C "${LANE_CWD[$lane]}" rev-parse HEAD 2>/dev/null)
    landed=0; a=1
    while [ "$a" -le "$MAX_ATTEMPTS" ]; do
      [ -e "$STATE/stop" ] && break
      mkdir -p "$UFO/reports/round-$n"
      if ! render_prompt "$lane" "$n" || ! subst "$H/lane-addendum.md" "$lane" "$n" "$a" >> "$UFO/prompts/$lane-round-$n.md"; then
        ev "render-fail lane=$lane round=$n"; break
      fi
      record_report_baseline "$lane" "$n" || { ev "baseline-fail lane=$lane round=$n"; break; }
      "$H/fleet-commit.sh" --as "$lane" -m "round-$n: $lane dispatch evidence (hyaku slot $SLOT attempt $a)" \
        -- ".ufo/prompts/$lane-round-$n.md" >/dev/null || ev "warn prompt-commit-failed lane=$lane round=$n"
      t0=$(date +%s)
      status "running $lane r$n a$a since $(date -Is)"
      log "launch $lane round=$n pgid=$$ driver=hyaku slot=$SLOT attempt=$a"
      ev "launch lane=$lane round=$n attempt=$a model=$L1_MODEL"
      run_session "$STATE/logs/$lane-r$n-a$a.out" "${LANE_CWD[$lane]}" "$L1_MODEL" "$ROUND_MAXTIME" "$ROUND_TIMEOUT" \
        "$UFO/prompts/$lane-round-$n.md"
      rc=$?
      elapsed=$(( $(date +%s) - t0 ))
      if verify_round "$lane" "$n"; then
        landed=1; infra=0
        log "complete $lane round=$n; hyaku slot=$SLOT attempt=$a rc=$rc elapsed=${elapsed}s"
        ev "complete lane=$lane round=$n attempt=$a rc=$rc elapsed=${elapsed}s"
        break
      fi
      log "lane-dead-no-report $lane round=$n; retry same round (hyaku slot=$SLOT attempt=$a rc=$rc elapsed=${elapsed}s)"
      if [ "$elapsed" -lt 300 ]; then
        infra=$((infra+1))
        ev "infra-fail lane=$lane round=$n rc=$rc elapsed=${elapsed}s streak=$infra (not counted as an attempt)"
        if [ "$infra" -ge 6 ]; then
          touch "$STATE/pause-$SLOT"; ev "PAUSED slot=$SLOT after $infra quick failures — operator check needed"
          break
        fi
        sleep $((300 * infra)); continue
      fi
      ev "attempt-failed lane=$lane round=$n attempt=$a rc=$rc elapsed=${elapsed}s"
      a=$((a+1)); sleep 60
    done
    if [ "$landed" -eq 1 ]; then
      HEADC=$(git -C "${LANE_CWD[$lane]}" rev-parse HEAD 2>/dev/null)
      run_closure "$lane" "$n" || ev "CLOSURE-DEBT lane=$lane round=$n (no hyaku closure row)"
      printf '%s\n' "$((n+1))" > "$STATE/next/$lane"
      outcome=$(closure_count "$lane" "$n" | tail -1)
      printf '%s\n' "$outcome" > "$STATE/outcome/$lane-r$n"
      streak=0
      for ((k=n; k>n-3 && k>0; k--)); do
        [ "$(cat "$STATE/outcome/$lane-r$k" 2>/dev/null)" = rejected ] && streak=$((streak+1))
      done
      if [ "$streak" -ge 3 ]; then
        printf 'three consecutive rejected closures through round %s (%s)\n' "$n" "$(date -Is)" > "$STATE/blocked/$lane"
        ev "BLOCKED lane=$lane :: 3 consecutive rejected closures (r$((n-2))-r$n) — operator review"
      fi
      ev "round-done lane=$lane round=$n outcome=$outcome next=$((n+1))"
    elif [ ! -e "$STATE/stop" ] && [ ! -e "$STATE/pause-$SLOT" ]; then
      printf 'round %s failed %s attempts (%s)\n' "$n" "$MAX_ATTEMPTS" "$(date -Is)" > "$STATE/blocked/$lane"
      ev "BLOCKED lane=$lane round=$n after $MAX_ATTEMPTS attempts"
    fi
    rm -rf -- "$STATE/claims/$lane"
    LAST_LANE=$lane
  done
}

# HYAKU_RENDER_TEST=<lane>:<round> prints the exact lane prompt a round would receive, then exits.
if [ -n "${HYAKU_RENDER_TEST:-}" ]; then
  load_env
  lane=${HYAKU_RENDER_TEST%%:*} n=${HYAKU_RENDER_TEST##*:}
  f="$UFO/prompts/$lane-round-$n.md"
  [ -e "$f" ] && { echo "refusing: $f already exists" >&2; exit 1; }
  render_prompt "$lane" "$n" && subst "$H/lane-addendum.md" "$lane" "$n" 1 >> "$f" && cat -- "$f"
  rm -f -- "$f"
  exit 0
fi

main_loop
