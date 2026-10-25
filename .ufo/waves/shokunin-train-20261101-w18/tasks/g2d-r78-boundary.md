# r78 BOUNDARY (g2d) — adversarial attack on the nested-update claims

The r78 scout claims (a) the inner update owns an epilogue drain, (b)
depth-2 via a body-drain EC SIGSEGVs, (c) fixture-drain-EC nesting is
refused not fatal, (d) zombie contacts UAF, (e) every-entry abort
livelocks. Attack each with an independent probe (own LOVE processes,
own scratch): is the inner drain REAL or a re-entrant observer of the
outer queue? Does the depth-2 crash reproduce at depth 1 with different
contact order? Can a forged drain EC pass a gate? Is the livelock bound
deterministic or wall-clock? Report -> reports/round-78/r78-boundary.md.
