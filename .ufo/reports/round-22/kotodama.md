# kotodama — round 22 report (2026-10-18)

Loop 2, integrate round — operator regimen (amended). One 32-worker batch on
`openai-cex/gpt-6.1-sol` at max effort (9 completed; 6 seats aborted
mid-flight by operator interrupt — among them the D-claim implementation
seats).
Baseline `cd9c8e4`; work commit **0e81d9d99514631d6717e1ff354d5a5a759aa980**.

## Work performed

- **Operability (claim O — verified):** all six round-21 routed items
  dispositioned in `reports/round-22/routed-resolution.json` —
  declared_in restored on the 34 carried edges (exact-equality controls,
  truncation removed, packet 3.1.1, new frozen revisions); deterministic
  content-based tie-break (23/23 controls; the PLACEHOLDER_RE wording false
  positive routed to round 25, not weakened); projector alias coercion fails
  closed (132/132 selftest; paired before/after control); the r17
  clone-snapshot mechanism reproduced (the scanner filters absolute paths
  containing the ancestor `.scratch`); the r18 supersession documented as a
  named row with a green successor; the baseline-binding new-pin discipline
  codified. Integrator re-ran all regressions green (battery, craft, adapter,
  d4/d2 gates, handoff v2/v3, projector).
- **Calibration (claim C — verified):** `reports/round-22/loop2-retrospective.md`
  — loop 2 final tally: 4 admissions / 1 rejection; the r17/r18 arc assessed
  honestly (the executable repair is real; the original 6-hold/0-note contract
  was not unchanged); 23 defect entries classified once; auditors verified the
  numbers and every pointer.
- **Depth (claim D — FAILED as declared):** the D4 fixture-bleed fix was
  analyzed (24 rank-provenance fields + 3 quarantine citations + 14 short
  references; injection at the projector's unconditional D2 `build_payload`)
  and designed (family-clean packaging, paired controls) — but the
  implementation seats were aborted before landing. Routed to round 25 with
  the full recipe.

## Landed changes

Commit `0e81d9d9` — routed resolutions, retrospective, records. The r22
D-rejection stands; the analysis/design artifacts carry the round-25 recipe.

## Before → after measurements

O/C verified by integrator re-runs (all regressions exit 0); D not
executable this round. Verdicts: `SCORECARD.md` §"Axes — round 22".

## SHONEN

- [~] SKILL.md decision tables — standing (author-asserted)
- [~] End-to-end domain task — routed-fix program executed (author-asserted)
- [~] Instructions executable — 23/23 tie-break controls, 132/132 projector (author-asserted)
- [~] No cross-domain bleed — scope clean at recorded observations (author-asserted)

Promotion review not requested; boxes remain `[~]`.
