#!/usr/bin/env bash
# hyaku inline — mechanical driver steps for IN-SESSION rounds (operator directive
# 2026-10-19: "do it inline with multiple swarms of subagents"). The parent omp session
# dispatches each lane round's L1 as a `task` subagent (canonical OMP host mapping:
# "In-session lane round | task with the filled round prompt") and each non-author
# closure as a fresh `task`; this script does everything mechanical around them,
# reusing the canonical driver's render_prompt / report_of / record_report_baseline / log.
#
#   inline.sh queue                 eligible lanes, lowest next round first (pool order breaks ties)
#   inline.sh dispatch <lane> [base]  claim + render prompt + baseline + commit dispatch evidence + launch line
#   inline.sh verify <lane>         landed? (report_of, committed — swept if not, pushed); logs complete
#   inline.sh fail <lane> <why>     record a failed attempt; blocks the lane after MAX_ATTEMPTS
#   inline.sh closure <lane>        render + commit the non-author closure prompt; prints its path
#   inline.sh closed <lane>         hyaku closure rows for the claimed round + outcome
#   inline.sh advance <lane>        next=round+1, record outcome, release claim (3 rejected in a row -> blocked)
set -u
FLEET=/home/vgpnk/Projects/shokunin
H="$FLEET/scripts/hyaku"
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
CANON=${SHOKUNIN_PLUGIN:-$HOME/Projects/kimi-shokunin}
export SHOKUNIN_ROOT=$FLEET HYAKU_STATE=$STATE
mkdir -p "$STATE"/{next,claims,blocked,logs,outcome}
# shellcheck disable=SC1091
. "$FLEET/scripts/shokunin-watchdog.sh"
TARGET=100 MAX_ATTEMPTS=3 L1_MODEL=@m_strong JUDGE_MODEL=@m_opus
# shellcheck disable=SC1091
[ -f "$H/hyaku.env" ] && . "$H/hyaku.env"

ev() { printf '%s inline %s\n' "$(date -Is)" "$*" >> "$STATE/events.log"; }
die() { echo "inline.sh: $*" >&2; exit 1; }
claim() { cat "$STATE/claims/$1/$2" 2>/dev/null; }

subst() { # template lane round attempt -> stdout (literal, & safe)
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

closure_count() { # lane n -> "count outcome"
  python3 - "$FLEET/MANIFEST.json" "$1" "$2" <<'EOF'
import json,sys
d=json.load(open(sys.argv[1])); l=sys.argv[2]; n=int(sys.argv[3])
rows=[r for r in d["rounds"] if r.get("campaign")=="hyaku" and r.get("lane")==l and r.get("lane_round")==n]
last=rows[-1] if rows else {}
print(len(rows), "admitted" if last.get("admitted") is True else ("rejected" if rows else "none"))
EOF
}

cmd=${1:-}; shift || true
case $cmd in
queue)
  while read -r l _; do
    case $l in ''|\#*) continue ;; esac
    [ -e "$STATE/blocked/$l" ] && continue
    [ -d "$STATE/claims/$l" ] && continue
    n=$(cat "$STATE/next/$l" 2>/dev/null) || continue
    [ "$n" -le "$TARGET" ] && printf '%s %s\n' "$n" "$l"
  done < "$H/pool.txt" | sort -s -n -k1,1 | awk '{print $2, $1}'
  ;;
dispatch)
  lane=${1:?lane}; [ -n "${LANE_CWD[$lane]:-}" ] || die "unknown lane $lane"
  [ -e "$STATE/blocked/$lane" ] && die "$lane is blocked: $(cat "$STATE/blocked/$lane")"
  n=$(cat "$STATE/next/$lane") || die "no next round for $lane"
  c="$STATE/claims/$lane"
  if [ -d "$c" ] && [ "$(claim "$lane" round)" = "$n" ]; then a=$(( $(claim "$lane" attempt) + 1 ))
  else rm -rf -- "$c"; mkdir -p "$c"; a=1
       printf '%s\n' "${2:-$(git -C "${LANE_CWD[$lane]}" rev-parse HEAD)}" > "$c/base"; fi
  printf 'inline\n' > "$c/owner"; printf '%s\n' "$n" > "$c/round"; printf '%s\n' "$a" > "$c/attempt"
  date -Is > "$c/dispatched"
  mkdir -p "$UFO/reports/round-$n"
  render_prompt "$lane" "$n" || die "render failed"
  subst "$H/lane-addendum.md" "$lane" "$n" "$a" >> "$UFO/prompts/$lane-round-$n.md" || die "addendum failed"
  record_report_baseline "$lane" "$n" || die "baseline failed"
  "$H/fleet-commit.sh" --as "$lane" -m "round-$n: $lane dispatch evidence (hyaku inline attempt $a)" \
    -- ".ufo/prompts/$lane-round-$n.md" >/dev/null || ev "warn prompt-commit-failed lane=$lane round=$n"
  log "launch $lane round=$n pgid=$$ driver=hyaku-inline attempt=$a"
  ev "launch lane=$lane round=$n attempt=$a model=$L1_MODEL"
  printf '%s %s %s %s\n' "$lane" "$n" "$UFO/prompts/$lane-round-$n.md" "${LANE_CWD[$lane]}"
  ;;
verify)
  lane=${1:?lane}; n=$(claim "$lane" round) || die "$lane not claimed"
  rep=".ufo/reports/round-$n/$lane.md"; cwd=${LANE_CWD[$lane]}
  report_of "$lane" "$n" || { echo "FAIL report_of (missing, unchanged, no SHONEN heading, or < ${MIN_REPORT_BYTES}B): $rep"; exit 1; }
  if [ -n "$(git -C "$FLEET" status --porcelain -- "$rep")" ] || [ -z "$(git -C "$FLEET" log -1 --format=%H -- "$rep")" ]; then
    ev "sweep lane=$lane round=$n :: report uncommitted at return (attribution defect)"
    "$H/fleet-commit.sh" --as "$lane" -m "round-$n: $lane report (hyaku sweep: L1 returned without committing; attribution defect)" -- "$rep" \
      || { echo "FAIL sweep commit"; exit 1; }
    echo "SWEPT report (attribution defect recorded)"
  fi
  if [ "$(git -C "$cwd" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)" != 0 ]; then
    git -C "$cwd" push -q && { ev "durability-push lane=$lane round=$n"; echo "PUSHED lane repo (L1 left it unpushed)"; } \
      || { ev "push-failed lane=$lane round=$n"; echo "WARN lane push failed"; }
  fi
  [ -n "$(git -C "$cwd" status --porcelain)" ] && echo "WARN lane repo has uncommitted changes: $(git -C "$cwd" status --porcelain | wc -l) paths"
  if [ "$(git -C "$FLEET" rev-list --count origin/master..HEAD 2>/dev/null || echo 0)" != 0 ]; then
    "$H/fleet-commit.sh" --as "$lane" -m unused -- "$rep" >/dev/null 2>&1 || ev "fleet-push-pending"
  fi
  log "complete $lane round=$n; hyaku-inline attempt=$(claim "$lane" attempt)"
  ev "complete lane=$lane round=$n attempt=$(claim "$lane" attempt)"
  echo "OK $lane r$n landed: report $(git -C "$FLEET" log -1 --format=%h -- "$rep") lane HEAD $(git -C "$cwd" rev-parse --short HEAD)"
  ;;
fail)
  lane=${1:?lane}; why=${2:-unspecified}; n=$(claim "$lane" round) || die "$lane not claimed"; a=$(claim "$lane" attempt)
  log "lane-dead-no-report $lane round=$n; retry same round (hyaku-inline attempt=$a: $why)"
  ev "attempt-failed lane=$lane round=$n attempt=$a :: $why"
  if [ "$a" -ge "$MAX_ATTEMPTS" ]; then
    printf 'round %s failed %s attempts (%s): %s\n' "$n" "$a" "$(date -Is)" "$why" > "$STATE/blocked/$lane"
    rm -rf -- "$STATE/claims/$lane"; ev "BLOCKED lane=$lane round=$n"; echo "BLOCKED"
  else echo "RETRYABLE attempt $a/$MAX_ATTEMPTS"; fi
  ;;
closure)
  lane=${1:?lane}; n=$(claim "$lane" round) || die "$lane not claimed"
  BASE=$(claim "$lane" base); HEADC=$(git -C "${LANE_CWD[$lane]}" rev-parse HEAD)
  DISPATCH_LINES=$(grep -E "^[^ ]+ (launch|complete|lane-dead-no-report) $lane round=$n( |;|$)" "$UFO/watchdog.log" | tail -10)
  p=".ufo/prompts/closure/$lane-round-$n.md"; mkdir -p "$FLEET/.ufo/prompts/closure"
  subst "$H/closure-prompt.md" "$lane" "$n" 0 > "$FLEET/$p" || die "closure render failed"
  "$H/fleet-commit.sh" --as protocol -m "round-$n: hyaku closure dispatch for $lane" -- "$p" >/dev/null || true
  ev "closure-launch lane=$lane round=$n model=$JUDGE_MODEL"
  printf '%s\n' "$FLEET/$p"
  ;;
closed)
  lane=${1:?lane}; n=$(claim "$lane" round) || die "$lane not claimed"; closure_count "$lane" "$n"
  ;;
advance)
  lane=${1:?lane}; n=$(claim "$lane" round) || die "$lane not claimed"
  read -r cnt outcome < <(closure_count "$lane" "$n")
  [ "$cnt" -ge 1 ] || ev "CLOSURE-DEBT lane=$lane round=$n (advanced without a hyaku closure row)"
  printf '%s\n' "$outcome" > "$STATE/outcome/$lane-r$n"
  printf '%s\n' "$((n+1))" > "$STATE/next/$lane"
  rm -rf -- "$STATE/claims/$lane"
  streak=0; for ((k=n; k>n-3 && k>0; k--)); do [ "$(cat "$STATE/outcome/$lane-r$k" 2>/dev/null)" = rejected ] && streak=$((streak+1)); done
  if [ "$streak" -ge 3 ]; then
    printf 'three consecutive rejected closures through round %s (%s)\n' "$n" "$(date -Is)" > "$STATE/blocked/$lane"
    ev "BLOCKED lane=$lane :: 3 consecutive rejected closures"; echo "BLOCKED after 3 rejected"
  fi
  ev "round-done lane=$lane round=$n outcome=$outcome next=$((n+1))"
  echo "$lane r$n $outcome -> next $((n+1))"
  ;;
*) sed -n '2,20p' "$0"; exit 64 ;;
esac
