# Protocol round 15 — gate integrity 8 → 9

## What changed

- Landed `closure-check.py` with a five-source lane universe (roster, base ids,
  counters, log lines, prompt names), fleet-wrap termination, explicit
  non-closure reporting, could-not-evaluate taxonomy, and invalid-`closed_at`
  rejection.
- Appended `MANIFEST.json` rounds 48–73: 26 entries / 34 lane rows. Frozen
  closure debt moves 17 → 0 between the `00:34:00` pre and `01:27:10` post
  cutoffs.
- Added `freeze-snapshot.py`, 25 fixture repos + 2 parser checks, seven targeted
  mutants, and two input-digest-pinned snapshots.
- Dispatched the required single batched ten-seat L2 audit, after four scoped
  implementation/review seats.

## Evidence pointer

- Implementation: `3687e5a` (`round-15`).
- Gate: `.ufo/waves/round-15/closure-check.py`, sha256
  `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c`.
- Controls: checker 27/27; snapshot generator 37/37; mutations 7/7; protocol
  verifier clean 8/8.
- Replay: `.ufo/waves/round-15/frozen/r15-pre-003400` → exit 1 / debt 17;
  `r15-post-012710` → exit 0 / debt 0; both `baseline: match`, inputs match.
- Accounting: `SCORECARD.md` M22–M29; `LOG.md` round 15.

## Boundary

The post result is cutoff-bounded, not a current-live claim. Final smoke saw
post-cutoff exit 1 / debt 10; this report lands after the post cutoff, so
protocol r15 is re-confirmed by the next closure pass. Frozen prompt indexes do
not encode git trackedness.

## SHONEN

Next move: protocol soundness 8 — resolve the main-repo gate-registry home and
register this gate at a named revision.
