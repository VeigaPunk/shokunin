# audio-r82-verifier2 — verify folded r82 on d6167399

Freeze git archive d6167399; verify fold bytes:

- --probe-ffmpeg-r82 family >=2 full runs, expect 8 entries / 77 legs, failures {}.
- Spot-check every fold item live: pid-class tone pairs (two different pid classes), rc=8 -channels 0 leg, a2 Speaker target + holder_consumers gate, t2 content gate, exact-name unload (foreign prefix name must NOT be destroyed — negative control).
- normal battery receipt vs canonical sha.
- Report reports/round-82/r82-verifier2.md + receipts corpus/live/r82-verify2/. Commit nothing. Return: report path, verdict, blockers.
