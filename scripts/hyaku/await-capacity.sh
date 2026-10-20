#!/usr/bin/env bash
# hyaku await-capacity — block until the orchestrator session likely has room under the
# background-job cap (async.maxJobs, read once at process start; a `task` call is refused
# while >= cap jobs run). Proxy for "running subagents": subagent transcripts (*.jsonl)
# under the session dir written within the last WINDOW seconds. A subagent inside one
# long tool call can look idle, so this undercounts; a refused dispatch just re-arms it.
#   await-capacity.sh <session-dir> [threshold=85] [max-seconds=3600] [window=90]
d=${1:?session dir}; thr=${2:-85}; max=${3:-3600}; win=${4:-90}
end=$(( $(date +%s) + max )); low=0
while :; do
  n=$(find "$d" -name '*.jsonl' -newermt "@$(( $(date +%s) - win ))" 2>/dev/null | wc -l)
  if [ "$n" -lt "$thr" ]; then low=$((low + 1)); else low=0; fi
  [ "$low" -ge 2 ] && { echo "capacity active=$n threshold=$thr"; exit 0; }
  [ "$(date +%s)" -ge "$end" ] && { echo "timeout active=$n threshold=$thr"; exit 1; }
  sleep 20
done
