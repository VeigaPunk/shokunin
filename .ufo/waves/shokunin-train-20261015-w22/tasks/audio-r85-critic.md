# audio-r85-critic — wave-B gate on committed 2a49d540

Standard critic duties on the r85 pactl/monstreams landing (2a49d540, 87 legs/5 entries). Encoded: serial monotonicity, mix taps + solo reference, aplay env targeting, boundary-corrected capture lattice, negctl table. THREE host-bimodal realizations armed both ways (latebind, cdup serial-first, sd_prop) — verify they're pinned as either-way, not silently absorbing.

- COMMITTED tree only, load preferred. Zero tracked writes; commit nothing.
- Report reports/round-85/r85-critic.md + receipts corpus/live/r85-critic/.
- /tmp near quota — TMPDIR=~/Projects/shokunin/tmp. Return: report path, verdict, findings, blockers.
