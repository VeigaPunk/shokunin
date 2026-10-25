# r78 SIMPLIFIER (audio) — YAGNI deletion on the r78 arm

d9aa6f9 added +2401/-3 to measure_audio.py. Find deletable weight:
dead pins restating gate conjuncts, unreachable branches, dead
helpers/params, duplicated leg-table shape. Prove every deletion by
re-running the affected probes on both variants (failures:{} identical
+ the pinned leaves unchanged). Deliver fold.diff + vfold copy under
corpus/live/r78-simplifier/. Report -> reports/round-78/r78-simplifier.md.
Read-only on tracked files.
