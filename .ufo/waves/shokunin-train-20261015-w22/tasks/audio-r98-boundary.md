# audio-r98-boundary — boundary under load

Read `~/Projects/shokunin/audio-shokunin/reports/round-98/` scout report and the laws it proposes. Attack every pinnable claim:

- Replay the scout's armed cells under load (>=12 concurrent hogs, record loadavg) AND quiet-ish; fresh-process reps.
- Vary the independent axes: PipeWire rates/quantum, CLI flag order, default-node state, sibling seat presence.
- Confirm/extend/falsify each law with exact receipts. Namespace all objects `r98b_*`; kill only own PIDs; no namespace-blind sweeps (r95 incident is precedent).
- Zero tracked writes; commit nothing. Write report `reports/round-98/r98-boundary.md` + receipts under `corpus/live/r98-boundary/` with manifest.sha256.
- Disclose foreign contention observed. Return: report path, verdict table, falsified claims, blockers.
