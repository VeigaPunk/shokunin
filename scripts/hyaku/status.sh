#!/usr/bin/env bash
# hyaku status — slots, lane round counters, blocks, recent events.
STATE=${HYAKU_STATE:-$HOME/.local/state/shokunin-hyaku}
H=/home/vgpnk/Projects/shokunin/scripts/hyaku
echo "== in flight (in-session L1 lane rounds)"
for d in "$STATE"/claims/*/; do [ -d "$d" ] && printf '  %-10s round=%s attempt=%s since %s\n' "$(basename "$d")" "$(cat "$d/round")" "$(cat "$d/attempt")" "$(cat "$d/dispatched")"; done
echo "== lanes (next round to run; target $(. "$H/hyaku.env"; echo "$TARGET"))"
while read -r l _; do
  case $l in ''|\#*) continue ;; esac
  c=''; [ -d "$STATE/claims/$l" ] && c=" [in flight]"
  b=''; [ -e "$STATE/blocked/$l" ] && b=" BLOCKED: $(cat "$STATE/blocked/$l")"
  printf '  %-10s next=%s%s%s\n' "$l" "$(cat "$STATE/next/$l" 2>/dev/null)" "$c" "$b"
done < "$H/pool.txt"
[ -e "$STATE/stop" ] && echo "!! stop file present"
echo "== rounds done this campaign: $(grep -c " round-done " "$STATE/events.log" 2>/dev/null)"
echo "== last events"
tail -n "${1:-15}" "$STATE/events.log" 2>/dev/null
