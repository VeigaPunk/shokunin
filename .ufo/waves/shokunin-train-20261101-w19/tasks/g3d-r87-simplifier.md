# r87 SIMPLIFIER (g3d) — YAGNI deletion on the r87 arm

c57fa40 added +880/-4 to phys3d_events.gd. Find deletable weight:
dead pins restating gate conjuncts, unreachable branches, dead
params/fields, duplicated emit blocks. Prove each deletion by replay
(201/201 both phases, prior rows byte-identical) + differential
fuzz where applicable. Deliver a fold.diff + verified full copies
under corpus/live/r87-simplifier/vfold/. Report ->
reports/round-87/r87-simplifier.md.
