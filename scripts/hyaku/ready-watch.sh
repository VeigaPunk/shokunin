#!/usr/bin/env bash
# hyaku ready-watch — wake the in-session orchestrator when a lane wave is ready to spawn.
#
# This is the run-7 driving pattern (run 8 replaced it with a long blocking drive loop that
# lost kernel state on every interrupt; do not do that). The orchestrator keeps the canonical
# scripts/hyaku/inline-dispatcher.py loaded in its kernel and runs ONE short `await tick()`
# per wake-up. Wake-ups come from (a) seat / L1 / closure completions, which the host delivers
# on its own, and (b) this watcher, started as an async bash job: it exits as soon as some
# <lane>/.ufo/waves/round-N/<wave>.ready has no <wave>.ready.dispatched marker, which delivers
# its output to the orchestrator. Restart it after each tick that leaves waves pending.
#
#   ready-watch.sh [interval-seconds]      default 15
#
# Env: FLEET (default /home/vgpnk/Projects/shokunin).
# Exit: 0 = an undispatched .ready exists (path printed as "READY <path>") · 64 = usage.
set -u
FLEET=${FLEET:-/home/vgpnk/Projects/shokunin}
interval=${1:-15}
case $interval in ''|*[!0-9]*) echo "usage: ready-watch.sh [interval-seconds]" >&2; exit 64 ;; esac
while :; do
  for r in "$FLEET"/*-shokunin/.ufo/waves/round-*/*.ready; do
    [ -e "$r" ] && [ ! -e "$r.dispatched" ] && { echo "READY $r"; exit 0; }
  done
  sleep "$interval"
done
