# audio-r95-foldfix

Lane repo: /home/vgpnk/Projects/shokunin/audio-shokunin
Round: 95 | Landed at ffeb5155 | Roles: foldfix-author
Critic C1-C5 + reviewer F1-F8 both fired live; PipeWire daemon was wedged host-wide and has since been restarted (pactl info responsive again). Fix the r95 JACK<->PipeWire family in corpus/fixtures/measure_audio.py, then prove a fresh green on the NOW-RESPONSIVE daemon.

Required fixes (union of both gate reports):
- Preserve entry["legs"] in _jack_r95_block on every exit path (F2/C1).
- Run the exit residue census on failure/blocked paths too; except paths must still census (F3/C2).
- Daemon unavailable / graph unreadable / open-timeout => named coverage_blocked with diagnostics, NEVER failures:[] while measuring nothing (C3).
- a_avail: a client that never opened is a BLOCK, not a version-law red (F4).
- Metadata key collision: keys are literal r95a/key1 but census keys by key alone (F1) — disambiguate per-client.
- Force-quantum restore must exist harness-side on the failure path, not only as fixture client (F5).
- Move the family lock to a host-global path (F6/C4) and use bounded/nonblocking acquisition; handle stale locks explicitly.
- sinks_gone vacuous in 2/5 entries — make the leg measure something or name it (F7).

Contract: work on lane HEAD; do NOT commit (orchestrator commits). File report at reports/round-95/r95-foldfix.md with before/after runs: the family must go green on committed-bytes archive tree on the responsive daemon, with legs+census populated on the green receipt. Bounded probes only (timeout-wrap every pw-*/pactl call); if the daemon re-wedges, name it coverage_blocked, never fake green.
