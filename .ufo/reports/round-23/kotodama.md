# kotodama — round 23 report (2026-10-18)

Loop 2, GLM round 1 of 2 — operator regimen (amended). One 16-worker batch on
`zai-coding-plan/glm-5.3-flash-low` (zai MAX thinking effort; 17/17 completed).
Baseline `0e81d9d`; work commit **b5d9844615b32b145fc263e3bd37062dce703b3b**.

## Work performed

- **Operability (claim O):** the two round-22 tails closed. (a) The
  PLACEHOLDER_RE false positive on D4-CL08's "unchanged-foreign-path control"
  was dispositioned via the preferred route — the basis reworded inside the
  uncertainty grammar ("foreign-path-stability control"), the packet re-pinned
  as a new revision (`declared-in-r3`), no placeholder rule weakened
  (wording-check selftest 28/28; successor check 17/17). (b) All six
  combined-source successor pins landed: the D2 live expected-holds re-pin to
  the final combined projector `2819f687…` (with `supersedes_pins` history), a
  new round-23 frozen repin-d2 generation replaying 11/11, the v2 successor
  with a stale-refusal control, and the D4 profile/frozen rows re-verified.
- **Depth (claim D):** the family-clean projection rule was drafted from the
  round-22 design (rule statement; the unconditional-`build_payload`
  injection-point warning; seven paired controls mapped to landed selftest
  lines; the round-25 commitment) and landed into SKILL.md with every row
  cited.
- **Calibration (unclaimed):** an append-only LOG correction records that
  round 22's "never implemented" wording mis-described the tree — two
  independent round-23 seats verified the family-clean implementation is
  present at `0e81d9d`. The r22 ledger row stands with the correction pointer.
- **Conformance:** the round-22 straggler (the O12 regression report completed
  in place after the close commit) was resolved per the scope watch's
  adjudication — filed bytes restored to baseline, the completed report
  preserved as `regression-completed.md`; the close-time validation refresh
  ran under the receipt-guard's REFRESH_RECEIPTS=1.

## Before → after measurements

`python3 reports/round-23/run-validation.py` → exit 0 (isolated copy; O and D
PASS). Verdicts: `SCORECARD.md` §"Axes — round 23".

## SHONEN

- [~] SKILL.md decision tables — family-clean rule landed (author-asserted)
- [~] End-to-end domain task — pins/wording program executed (author-asserted)
- [~] Instructions executable — 11/11 replay, 28/28 + 17/17 checks (author-asserted)
- [~] No cross-domain bleed — scope clean (author-asserted)

Promotion review: round 24 (GLM-2) will run the box-by-box evidence review
prepared in `reports/round-23/shonen-survey.md`; boxes remain `[~]` here.
