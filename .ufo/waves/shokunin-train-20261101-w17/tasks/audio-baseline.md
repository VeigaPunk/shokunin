# r77 BASELINE (audio) — freeze + drift
Standard two-phase: freeze HEAD (post-18deef6), replay
--probe-capture-r76 + --probe-consumers2-r75 on frozen bytes; after the
author commit lands (poll), replay post-commit — prior rows stable
modulo declared host-drift leaves (pw_capture_ports, aplay tail, hw
contention). File reports/round-77/r77-baseline.md.
