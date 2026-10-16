# audio-r100-boundary — boundary under load

Read ~/Projects/shokunin/audio-shokunin/reports/round-100/ scout report; attack every pinnable claim:

- Replay armed cells under load (>=12 hogs, log loadavg) + quiet-ish; fresh processes. Namespace r100b_* objects only; kill own PIDs only; never sweep foreign objects (r95 incident precedent).
- Vary axes: private-core vs shared graph, rates/quantum, flag order, sibling presence, source-loss/relink timing.
- Zero tracked writes; commit nothing. Write reports/round-100/r100-boundary.md + corpus/live/r100-boundary/ receipts + manifest.sha256.
- Return: report path, verdict table, falsified claims, blockers.
