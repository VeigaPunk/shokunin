#!/usr/bin/env bash
# hyaku probe-alias — which provider/model actually answers an alias right now.
# A failing primary silently walks a fallback chain, so "it replied" is not evidence
# the alias works; this prints the answering hop and every errored hop before it.
#   probe-alias.sh m_zfl [m_flash ...]
for a in "$@"; do
  out=$(timeout 180 omp -p --no-session --no-tools --no-skills --no-rules --mode json \
        --model "@$a" "Reply with exactly the word PONG." 2>/dev/null)
  printf '%s\n' "$out" | python3 -c '
import json, sys
alias = sys.argv[1]; hops = []; ok = None
for line in sys.stdin:
    try: e = json.loads(line)
    except Exception: continue
    m = e.get("message")
    if e.get("type") == "message_end" and isinstance(m, dict):
        tag = str(m.get("provider")) + "/" + str(m.get("model"))
        if m.get("stopReason") == "error":
            hops.append(tag + " ERR " + (m.get("errorMessage") or "")[:70].replace("\n", " "))
        else:
            ok = tag
print(f"{alias}: answered-by={ok} primary-ok={not hops and ok is not None}")
for h in hops: print("   " + h)
' "$a"
done
