#!/usr/bin/env bash
# Bounded real-process regression for the source-gate retry report lifecycle.
# Usage: bash driver-retry-regression.sh [path/to/shokunin-watchdog.sh]
set -uo pipefail

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
ROOT=$(CDPATH='' cd -- "$SCRIPT_DIR/../../.." && pwd)
EMPTY_DIGEST=$(printf '' | sha256sum)
EMPTY_DIGEST=${EMPTY_DIGEST%% *}

record() {
  local label=$1 rc=$2
  if [ "$rc" -eq 0 ]; then printf 'PASS  %s\n' "$label"; PASS=$((PASS+1))
  else printf 'FAIL  %s\n' "$label"; FAIL=$((FAIL+1)); fi
}
check_eq() {
  local label=$1 expected=$2 actual=$3
  if [ "$expected" = "$actual" ]; then record "$label" 0
  else printf '      expected=<%s> actual=<%s>\n' "$expected" "$actual"; record "$label" 1; fi
}
file_digest() {
  local out
  out=$(sha256sum < "$1") || return 1
  printf '%s\n' "${out%% *}"
}
make_report() {
  local file=$1 marker=$2
  mkdir -p "$(dirname -- "$file")"
  {
    printf '## SHONEN\nreport payload %s\n## Sources & frontier\n' "$marker"
    printf '%0100d\n' 0
  } > "$file"
}
prepare_fixture() {
  local root=$1
  mkdir -p "$root/.ufo" "$root/templates" "$root/scripts" "$root/beta-shokunin"
  cat > "$root/shokunin.conf" <<'EOF'
LANES='beta|beta-shokunin|retry regression'
SUBSTRATE_CMD='sleep 90'
TICK_SECONDS=1
ROUND_CAP=8
MIN_REPORT_BYTES=96
EOF
  printf 'You are {{LANE}}, round {{ROUND}}. Working dir: {{LANE_REPO}}\n' > "$root/templates/round-prompt.md"
  cat > "$root/scripts/sources-census.sh" <<'EOF'
#!/usr/bin/env bash
case "$(cat "$SHOKUNIN_ROOT/gate" 2>/dev/null || printf fail)" in
  pass) exit 0 ;;
  *) printf 'simulated source-gate finding\n' >&2; exit 1 ;;
esac
EOF
  chmod +x "$root/scripts/sources-census.sh"
  printf 'fail\n' > "$root/gate"
  export SHOKUNIN_ROOT="$root" SHOKUNIN_CONF="$root/shokunin.conf"
}
cleanup_processes() {
  local pid
  for pid in "${PIDS[@]:-}"; do
    case $pid in ''|*[!0-9]*) continue ;; esac
    if kill -0 -- "-$pid" 2>/dev/null; then
      kill_mission beta "$pid" >/dev/null 2>&1 || {
        kill -KILL -- "-$pid" 2>/dev/null || true
        wait "$pid" 2>/dev/null || true
      }
    fi
  done
}
start_lane() {
  local round=$1 mid i
  launch_lane beta "$round"
  mid=$(mission_of beta)
  PIDS+=("$mid")
  for ((i=0; i<40; i++)); do
    mission_live beta "$mid" && { printf '%s\n' "$mid"; return 0; }
    sleep 0.05
  done
  return 1
}
wait_lane_dead() {
  local mid=$1 i
  for ((i=0; i<100; i++)); do
    if ! kill -0 -- "-$mid" 2>/dev/null; then return 0; fi
    sleep 0.05
  done
  return 1
}

run_case() {
  local which=$1 root=$CASE_ROOT mid oldmid newmid report prefix before_hash after_hash before_mtime after_mtime rc stale_rc round next_round next_digest size launches baseline_file baseline_round baseline_digest upper_digest
  local -a baseline_temps=()

  case $which in
    dead)
      report="$UFO/reports/round-1/beta.md"
      mid=$(start_lane 1); rc=$?; record 'A-initial-attempt-started-live' "$rc"
      oldmid=$mid
      kill_mission beta "$oldmid"; rc=$?; record 'A-failed-attempt-stopped' "$rc"
      wait_lane_dead "$oldmid"; rc=$?; record 'A-failed-attempt-process-group-dead' "$rc"
      make_report "$report" 'dead-attempt'
      file_digest "$report" > "$root/report.before"
      before_hash=$(cat "$root/report.before")
      report_of beta 1; rc=$?; record 'A-valid-failed-attempt-report-observed' "$([ "$rc" -eq 0 ] && echo 0 || echo 1)"

      advance beta 1; rc=$?; record 'A-dead-gate-failure-retries' "$rc"
      newmid=$(mission_of beta); PIDS+=("$newmid")
      mission_live beta "$newmid"; rc=$?; record 'A-retry-process-live-same-round' "$rc"
      check_eq 'A-retry-round-remains-N' 1 "$(round_of beta)"
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      check_eq 'A-report-bytes-unchanged-by-retry' "$before_hash" "$after_hash"
      baseline_file="$UFO/state/beta.report-baseline"
      baseline_round=1; baseline_digest=$before_hash
      if [ -f "$baseline_file" ]; then
        read -r baseline_round baseline_digest < "$baseline_file"
      fi
      upper_digest=${baseline_digest^^}
      if [ "$upper_digest" != "$baseline_digest" ]; then record 'A-uppercase-baseline-probe-changed-digest-encoding' 0; else record 'A-uppercase-baseline-probe-changed-digest-encoding' 1; fi
      printf '%s %s\n' "$baseline_round" "$upper_digest" > "$baseline_file"
      report_of beta 1; rc=$?
      if [ "$rc" -ne 0 ]; then record 'A-uppercase-equal-baseline-rejects-unchanged-report' 0; else record 'A-uppercase-equal-baseline-rejects-unchanged-report' 1; fi
      printf '%s %s\n' "$baseline_round" "$baseline_digest" > "$baseline_file"

      before_mtime=$(stat -c %Y -- "$report")
      touch -m -d '@946684800' -- "$report"
      after_mtime=$(stat -c %Y -- "$report")
      if [ "$before_mtime" != "$after_mtime" ]; then record 'A-mtime-only-probe-really-changed-mtime' 0; else record 'A-mtime-only-probe-really-changed-mtime' 1; fi
      printf 'pass\n' > "$SHOKUNIN_ROOT/gate"
      report_of beta 1; stale_rc=$?
      if [ "$stale_rc" -ne 0 ]; then record 'A-registry-fix-alone-rejects-unchanged-report' 0; else record 'A-registry-fix-alone-rejects-unchanged-report' 1; fi
      if [ "$stale_rc" -eq 0 ]; then
        advance beta 1 "$newmid"; rc=$?; record 'A-no-stale-completion-attempt' 1
      fi
      mission_live beta "$newmid"; rc=$?; record 'A-registry-fix-alone-keeps-retry-alive' "$rc"
      check_eq 'A-registry-fix-alone-keeps-round-N' 1 "$(round_of beta)"
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      check_eq 'A-mtime-change-did-not-change-report-bytes' "$before_hash" "$after_hash"

      if [ "$(round_of beta)" -eq 1 ] && mission_live beta "$newmid"; then
        prefix="$root/report-prefix"
        cp -- "$report" "$prefix"
        size=$(wc -c < "$prefix")
        printf '\n## Fresh completion marker: %s\n' 'dead-retry-fresh-report' >> "$report"
        cmp -n "$size" -- "$prefix" "$report"; rc=$?; record 'A-fresh-append-preserves-all-prior-report-bytes' "$rc"
        report_of beta 1; rc=$?; record 'A-fresh-report-is-accepted' "$([ "$rc" -eq 0 ] && echo 0 || echo 1)"
        advance beta 1 "$newmid"; rc=$?; record 'A-fresh-report-closes-round' "$rc"
        check_eq 'A-fresh-report-advances-exactly-to-N-plus-1' 2 "$(round_of beta)"
      else
        record 'A-fresh-report-closes-round' 1
        record 'A-fresh-report-advances-exactly-to-N-plus-1' 1
      fi
      if [ -f "$report" ]; then record 'A-original-report-remains-in-place' 0; else record 'A-original-report-remains-in-place' 1; fi
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      if [ "$before_hash" != "$after_hash" ]; then record 'A-fresh-report-appended-new-bytes' 0; else record 'A-fresh-report-appended-new-bytes' 1; fi

      next_round=''; next_digest=''
      if [ -f "$UFO/state/beta.report-baseline" ]; then
        read -r next_round next_digest < "$UFO/state/beta.report-baseline" || true
      fi
      check_eq 'A-round-N-plus-1-baseline-is-round-scoped' 2 "$next_round"
      check_eq 'A-round-N-plus-1-absent-report-baseline-is-empty-digest' "$EMPTY_DIGEST" "$next_digest"
      if [ "$next_round" = 2 ]; then
        mkdir -p "$UFO/reports/round-2"
        cp -- "$report" "$UFO/reports/round-2/beta.md"
        report_of beta 2; rc=$?; record 'A-round-N-report-digest-is-not-reused-for-N-plus-1' "$([ "$rc" -eq 0 ] && echo 0 || echo 1)"
      else
        record 'A-round-N-report-digest-is-not-reused-for-N-plus-1' 1
      fi
      ;;

    live)
      report="$UFO/reports/round-1/beta.md"
      mid=$(start_lane 1); rc=$?; record 'B-attempt-started-live' "$rc"
      make_report "$report" 'live-attempt'
      file_digest "$report" > "$root/report.before"
      before_hash=$(cat "$root/report.before")
      report_of beta 1; rc=$?; record 'B-valid-live-attempt-report-observed' "$([ "$rc" -eq 0 ] && echo 0 || echo 1)"
      advance beta 1 "$mid"; rc=$?; record 'B-live-gate-failure-does-not-error' "$rc"
      check_eq 'B-gate-failure-keeps-existing-mission-id' "$mid" "$(mission_of beta)"
      mission_live beta "$mid"; rc=$?; record 'B-live-gate-failure-does-not-kill-process' "$rc"
      launches=$(grep -cF 'launch beta round=1' "$UFO/watchdog.log" || true)
      check_eq 'B-live-gate-failure-does-not-relaunch' 1 "$launches"
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      check_eq 'B-live-gate-failure-preserves-report-bytes' "$before_hash" "$after_hash"

      before_mtime=$(stat -c %Y -- "$report")
      touch -m -d '@946684800' -- "$report"
      after_mtime=$(stat -c %Y -- "$report")
      if [ "$before_mtime" != "$after_mtime" ]; then record 'B-mtime-only-probe-really-changed-mtime' 0; else record 'B-mtime-only-probe-really-changed-mtime' 1; fi
      printf 'pass\n' > "$SHOKUNIN_ROOT/gate"
      report_of beta 1; stale_rc=$?
      if [ "$stale_rc" -ne 0 ]; then record 'B-registry-fix-alone-rejects-unchanged-report' 0; else record 'B-registry-fix-alone-rejects-unchanged-report' 1; fi
      if [ "$stale_rc" -eq 0 ]; then
        advance beta 1 "$mid"; rc=$?; record 'B-no-stale-completion-attempt' 1
      fi
      mission_live beta "$mid"; rc=$?; record 'B-registry-fix-alone-keeps-live-process' "$rc"
      check_eq 'B-registry-fix-alone-keeps-round-N' 1 "$(round_of beta)"
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      check_eq 'B-registry-fix-alone-preserves-report-bytes' "$before_hash" "$after_hash"

      if [ "$(round_of beta)" -eq 1 ] && mission_live beta "$mid"; then
        prefix="$root/report-prefix"
        cp -- "$report" "$prefix"
        size=$(wc -c < "$prefix")
        printf '\n## Fresh completion marker: %s\n' 'live-retry-fresh-report' >> "$report"
        cmp -n "$size" -- "$prefix" "$report"; rc=$?; record 'B-fresh-append-preserves-all-prior-report-bytes' "$rc"
        report_of beta 1; rc=$?; record 'B-fresh-report-is-accepted' "$([ "$rc" -eq 0 ] && echo 0 || echo 1)"
        advance beta 1 "$mid"; rc=$?; record 'B-fresh-report-closes-round' "$rc"
        check_eq 'B-fresh-report-advances-exactly-to-N-plus-1' 2 "$(round_of beta)"
        wait_lane_dead "$mid"; rc=$?; record 'B-only-tagged-live-attempt-group-is-dead-after-close' "$rc"
      else
        record 'B-fresh-report-closes-round' 1
        record 'B-fresh-report-advances-exactly-to-N-plus-1' 1
        record 'B-only-tagged-live-attempt-group-is-dead-after-close' 1
      fi

      mkdir -p "$UFO/reports/round-7"
      printf '## SHONEN\nshort\n' > "$UFO/reports/round-7/probe.md"
      report_of probe 7; rc=$?
      if [ "$rc" -ne 0 ]; then record 'content-size-floor-still-rejects-short-report' 0; else record 'content-size-floor-still-rejects-short-report' 1; fi
      { printf 'no SHONEN heading\n'; printf '%0100d\n' 0; } > "$UFO/reports/round-7/probe.md"
      report_of probe 7; rc=$?
      if [ "$rc" -ne 0 ]; then record 'content-heading-check-still-rejects-missing-marker' 0; else record 'content-heading-check-still-rejects-missing-marker' 1; fi
      make_report "$UFO/reports/round-7/probe.md" 'content-checks'
      report_of probe 7; rc=$?
      if [ "$rc" -eq 0 ]; then record 'content-heading-and-size-still-accept-valid-report' 0; else record 'content-heading-and-size-still-accept-valid-report' 1; fi
      ;;
    capture)
      report="$UFO/reports/round-1/beta.md"
      printf '1\n' > "$UFO/state/beta.round"
      make_report "$report" 'baseline-capture-failure'
      before_hash=$(file_digest "$report")
      mkdir "$UFO/state/beta.report-baseline"
      advance beta 1; rc=$?
      if [ "$rc" -ne 0 ]; then record 'C-directory-baseline-capture-fails-closed' 0; else record 'C-directory-baseline-capture-fails-closed' 1; fi
      check_eq 'C-capture-failure-keeps-round-N' 1 "$(round_of beta)"
      launches=$(grep -cF 'launch beta round=1' "$UFO/watchdog.log" || true)
      check_eq 'C-capture-failure-does-not-retry-launch' 0 "$launches"
      check_eq 'C-capture-failure-does-not-write-mission' '' "$(mission_of beta)"
      after_hash=$(file_digest "$report" 2>/dev/null || printf unreadable)
      check_eq 'C-capture-failure-preserves-report-bytes' "$before_hash" "$after_hash"
      if [ -f "$report" ]; then record 'C-capture-failure-keeps-report-in-place' 0; else record 'C-capture-failure-keeps-report-in-place' 1; fi
      shopt -s nullglob
      baseline_temps=( "$UFO/state/beta.report-baseline.tmp."* )
      shopt -u nullglob
      check_eq 'C-capture-failure-cleans-temporary-state' 0 "${#baseline_temps[@]}"
      if grep -qF 'report-baseline-fail beta round=1 :: cannot replace state' "$UFO/watchdog.log"; then
        record 'C-directory-target-replacement-failure-is-logged' 0
      else
        record 'C-directory-target-replacement-failure-is-logged' 1
      fi
      ;;
    *) printf 'unknown case: %s\n' "$which" >&2; return 2 ;;
  esac
  printf 'CASE-SUMMARY %s pass=%d fail=%d\n' "$which" "$PASS" "$FAIL"
  [ "$FAIL" -eq 0 ]
}

if [ "${1:-}" = '--case' ]; then
  CASE_NAME=$2
  DRIVER=$3
  CASE_ROOT=$4
  PASS=0; FAIL=0; PIDS=()
  prepare_fixture "$CASE_ROOT"
# shellcheck disable=SC1090
  . "$DRIVER"
  trap cleanup_processes EXIT
  printf 'CASE %s driver=%s sha256=%s\n' "$CASE_NAME" "$DRIVER" "$(sha256sum -- "$DRIVER" | cut -d' ' -f1)"
  run_case "$CASE_NAME"
  exit $?
fi

DRIVER=${1:-"$ROOT/scripts/shokunin-watchdog.sh"}
case $DRIVER in /*) ;; *) DRIVER=$(CDPATH='' cd -- "$(dirname -- "$DRIVER")" && pwd)/$(basename -- "$DRIVER") ;; esac
BASE=/tmp/kaika-verify/DriverCompletionFix
rm -rf -- "$BASE"
mkdir -p "$BASE"
printf 'REGRESSION driver=%s sha256=%s\n' "$DRIVER" "$(sha256sum -- "$DRIVER" | cut -d' ' -f1)"
PASS=0; FAIL=0
for case_name in dead live capture; do
  output="$BASE/$case_name.out"
  bash "$SCRIPT_DIR/driver-retry-regression.sh" --case "$case_name" "$DRIVER" "$BASE/$case_name" > "$output" 2>&1
  rc=$?
  cat "$output"
  if [ "$rc" -eq 0 ]; then record "case-$case_name" 0
  else record "case-$case_name" 1; fi
done
printf 'SUMMARY pass=%d fail=%d\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
