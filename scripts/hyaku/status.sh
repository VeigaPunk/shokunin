#!/usr/bin/env bash
# hyaku status — slots, lane round counters, blocks, recent events.
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
H=/home/vgpnk/Projects/shokunin/scripts/hyaku
echo "== slots"
for f in "$STATE"/slot-*.status; do [ -f "$f" ] && printf '%s: %s\n' "$(basename "$f" .status)" "$(cat "$f")"; done
echo "== lanes (next round to run; target $(. "$H/hyaku.env"; echo "$TARGET"))"
while read -r l _; do
  case $l in ''|\#*) continue ;; esac
  c=''; [ -d "$STATE/claims/$l" ] && c=" [slot $(cat "$STATE/claims/$l/owner")]"
  b=''; [ -e "$STATE/blocked/$l" ] && b=" BLOCKED: $(cat "$STATE/blocked/$l")"
  printf '  %-10s next=%s%s%s\n' "$l" "$(cat "$STATE/next/$l" 2>/dev/null)" "$c" "$b"
done < "$H/pool.txt"
[ -e "$STATE/stop" ] && echo "!! stop file present"
ls "$STATE"/pause-* >/dev/null 2>&1 && echo "!! paused: $(ls "$STATE"/pause-* | xargs -n1 basename | paste -sd' ')"
echo "== rounds done this campaign: $(grep -c ' round-done ' "$STATE/events.log" 2>/dev/null || echo 0)"
echo "== last events"
tail -n "${1:-15}" "$STATE/events.log" 2>/dev/null
