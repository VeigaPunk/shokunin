#!/usr/bin/env bash
# scratch_failover_test.sh -- prove the zai -> devin fallthrough on scratch
# ports, without touching the live unit or the operator's zai quota.
#
# Two triggers are exercised, both aimed at leg 1 (zai):
#   A. connection error  -- leg 1 pointed at a port nothing listens on (:9)
#   B. HTTP 429          -- leg 1 pointed at scripts/mock_429.py
# In both cases the request must be answered by leg 2 (devin) and the response
# must carry devin's fingerprint: model id glm-5-3-flash-max.
#
# Usage: scratch_failover_test.sh [<shim.py> <port>]
set -euo pipefail
SHIM="${1:-$HOME/.local/share/glm-flash-shim/shim.py}"
PORT="${2:-8795}"
MOCK_PORT="$((PORT + 1))"
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
trap 'kill $(jobs -p) 2>/dev/null || true; wait 2>/dev/null || true' EXIT

start_shim() {  # $1 = leg1 url, $2 = log file
  GLM_SHIM_PORT="$PORT" GLM_SHIM_BIND=127.0.0.1 \
  GLM_LEG1_NAME="$3" GLM_LEG1_URL="$1" GLM_LEG1_KEY=dummy GLM_LEG1_MODEL= \
  GLM_SHIM_TIMEOUT=5 \
    nohup python3 "$SHIM" >"$2" 2>&1 &
  echo $!
}

wait_port() {
  for _ in $(seq 1 40); do
    curl -s --max-time 1 "http://127.0.0.1:$1/health" >/dev/null && return 0
    sleep 0.25
  done
  echo "port $1 never came up" >&2
  return 1
}

probe() {
  curl -s --max-time 60 -w ' http_code=%{http_code} time_total=%{time_total}s' \
    -H 'Content-Type: application/json' -X POST \
    "http://127.0.0.1:$PORT/v1/chat/completions" \
    -d '{"model":"glm-5.3-flash","messages":[{"role":"user","content":"Reply with exactly one word: pong"}],"max_tokens":64}'
  echo
}

echo "=== A. leg-1 connection error -> leg 2 ==="
PID=$(start_shim "http://127.0.0.1:9/v1/chat/completions" "$TMP/a.log" zai-dead)
wait_port "$PORT"
curl -s --max-time 5 "http://127.0.0.1:$PORT/health"; echo
probe | tee "$TMP/a.probe.txt"
kill "$PID" 2>/dev/null || true; sleep 0.5
grep -E 'leg=[0-9]/' "$TMP/a.log" || true
echo "--- leg chain as the scratch shim logged it ---"
grep -E '^.*leg [0-9]:' "$TMP/a.log" || true

echo
echo "=== B. leg-1 HTTP 429 -> leg 2 ==="
python3 "$HERE/mock_429.py" "$MOCK_PORT" &
sleep 0.6
PID=$(start_shim "http://127.0.0.1:$MOCK_PORT/v1/chat/completions" "$TMP/b.log" zai-429)
wait_port "$PORT"
probe | tee "$TMP/b.probe.txt"
kill "$PID" 2>/dev/null || true; sleep 0.5
grep -E 'leg=[0-9]/' "$TMP/b.log" || true
kill %2 2>/dev/null || true

echo
echo "=== verdict inputs ==="
for f in a b; do
  printf '%s: ' "$f"
  grep -o '"model": *"[^"]*"' "$TMP/$f.probe.txt" | head -1
done
echo "scratch dir: $TMP"