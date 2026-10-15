# Rogue-edit audit (held-out foreign-fleet artifacts)

Audited 2026-10-15 during the post-r85 close. Both diffs were authored by
the sibling ufo-fsd fleet session, not by this training fleet. Verdict:
**REFUSED — do not commit; keep held out in the working tree.**

## audio-shokunin/SHONEN.md (dirty since fleet session, +10/−7)

Replaces the lane's completed probation record — four `[x]` boxes, each
verified by a named non-author verifier with an evidence pointer
(`audio-r1-verifier`, `r2-verifier`, `r3-adjudicator`, `r24-verifier`) —
with an unchecked "Promotion checklist" asserting SKILL.md absent and
path drift. Refusing because: (1) it discards verified probation state
by reverting checkmarks, a record falsification; (2) the promotion
rubric is a foreign-fleet template this lane never adopted; (3) its
"SKILL.md is absent" claim ignores that the lane's convention keeps
corpus material rather than a standalone SKILL.md. If promotion is ever
pursued it must be a fresh verdict, not a rewrite of the probation file.

## game-dev-2d-shokunin/SCORECARD.md (dirty, +29/−1)

Prepends a "Round 1 — current evidence-readiness baseline" rubric
scoring depth/coverage/calibration 0/10 on a lane at round 85 with 174
committed battery rows. It does retain the historical table as
"Inherited scorecard", but the rubric and its scoring convention belong
to the sibling fleet's mint protocol, not this lane's LOG-driven
evidence convention. Refusing; the current round-selection signal lives
in LOG.md + reports/round-*.

## Disposition

Files remain dirty in-tree per held-out convention. A future lane close
MAY restore HEAD bytes (`git checkout -- <file>`) once the operator
confirms the sibling fleet no longer needs the diffs — that restoration
is itself a destructive revert of the foreign artifact and is deferred.
