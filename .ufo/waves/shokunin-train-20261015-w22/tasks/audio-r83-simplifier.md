# audio-r83-simplifier — wave-B gate on committed a151a226

Standard simplifier duties on the r83 pwcat/pw-record landing (a151a226, 128 legs/7 entries in measure_audio.py). Scout falsifications + boundary corrections already folded (rc=255 classes, empty-prop SIGSEGV, -d delay, uint32 wrap, |x| artifact).

- Run against the COMMITTED tree (git archive or commit-pin), under load preferred. Zero tracked writes; commit nothing.
- Report reports/round-83/r83-simplifier.md + receipts corpus/live/r83-simplifier/ + manifest.
- Return: report path, verdict, findings ranked, blockers.
