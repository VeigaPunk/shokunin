#!/usr/bin/env bash
# lane-watch — live per-lane view of the shokunin fleet for the UFO Sighting wall.
# Read-only: reads .ufo/state/*.round and .ufo/state/*.out, writes nothing.
set -u
ROOT=${SHOKUNIN_ROOT:-/home/vgpnk/Projects/shokunin}
UFO="$ROOT/.ufo"
lanes=$(sed -n 's/^\([a-z0-9-]*\)|.*/\1/p' "$ROOT/shokunin.conf" 2>/dev/null | sort -u)
while :; do
  running=$(pgrep -c -f 'omp -p' 2>/dev/null || echo 0)
  drv=$(pgrep -f shokunin-watchdog.sh 2>/dev/null | head -1)
  printf '\033[2J\033[H'
  echo "SHOKUNIN FLEET   $(date '+%H:%M:%S')   lanes-running=$running   driver=${drv:-DOWN}"
  [ -f "$UFO/fleet-wrap" ] && echo "** FLEET-WRAP PRESENT — respawns halted **"
  printf '%-12s %-6s %-9s %s\n' LANE ROUND STATE LAST-OUTPUT
  for l in $lanes; do
    r=$(cat "$UFO/state/$l.round" 2>/dev/null || echo 0)
    mid=$(cat "$UFO/state/$l.mission" 2>/dev/null || echo "")
    st=idle
    [ -n "$mid" ] && kill -0 "$mid" 2>/dev/null && st=running
    last=$(tail -c 400 "$UFO/state/$l.out" 2>/dev/null | tr -d '\000' | grep -v '^$' | tail -1 | cut -c1-46)
    printf '%-12s %-6s %-9s %s\n' "$l" "$r" "$st" "${last:--}"
  done
  sleep 10
done
