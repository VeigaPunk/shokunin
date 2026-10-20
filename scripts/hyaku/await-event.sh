#!/usr/bin/env bash
# hyaku await-event — block until events.log grows past byte offset <from> with a line
# matching the pattern (default: anything notable), or until <max-seconds> pass.
# Prints the new lines and the next offset. Used by the monitoring session.
#   await-event.sh <from-offset> [max-seconds] [ERE]
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
from=${1:-0} max=${2:-3300}
pat=${3:-'BLOCKED|PAUSED|CLOSURE-DEBT|round-done|infra-fail|attempt-failed|sweep|push-failed|fleet-push-pending|stop-file|render-fail|baseline-fail'}
f="$STATE/events.log"
end=$(( $(date +%s) + max ))
while :; do
  size=$(stat -c %s "$f" 2>/dev/null || echo 0)
  if [ "$size" -gt "$from" ] && tail -c +"$((from + 1))" "$f" | grep -qE "$pat"; then break; fi
  [ "$(date +%s)" -ge "$end" ] && break
  sleep 20
done
size=$(stat -c %s "$f" 2>/dev/null || echo 0)
tail -c +"$((from + 1))" "$f" 2>/dev/null
echo "NEXT_OFFSET=$size"
