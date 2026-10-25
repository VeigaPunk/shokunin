# kotodama — round 24 report (2026-10-18)

Loop 2, GLM round 2 of 2 — operator regimen (amended). One 16-worker batch on
`zai-coding-plan/glm-5.3-flash-low` (zai MAX thinking effort; 16/16 completed).
Baseline `8fbcee9`; work commit **e06581b7fc2b50050a336f7f38a7e2baebcc6abc**.

## Work performed

- **Calibration (claim C):** the promotion-review dossier
  (`reports/round-24/promotion-review.md`) — the four SHONEN boxes
  independently verified by 10+ named non-author reviewers: box 1
  verified-with-conditions (143 citations over 88 files resolve, zero
  fabrications; coverage deep, 7 executables unnamed — condition); box 2
  verified-with-conditions (D2→D3→D4→handoff chain re-executed green,
  byte-identical SHAs; LOG misquote erratum); box 3 verified-with-conditions
  (four fresh-context cold-run seats; conditions N1-N7); box 4
  verified-with-conditions (bleed fixed live; PROVINCE byte-accurate; three
  named conditions). The promotion decision is operator-owned.
- **Operability (claim O):** box-3 cold-run — ~80 invocations by seats reading
  only the four front-door files; every documented steady state reproduces;
  seven breaks/ambiguity findings dispositioned (seven wording-level SKILL.md
  fixes with measured controls; seven named box-3 conditions).
- **Depth (claim D):** the first full SKILL.md staleness audit — every
  executable claim re-run green; 8 stale spots fixed with controls or dated
  errata; a 123-row per-row disposition table; zero silent staleness.

## Landed changes

Commit `e06581b7` — dossier, cold-run consolidation + fixes, staleness audit +
per-row table, records. Loop 2 is complete (rounds 17-24: six admissions, one
rejection, one rejection-repaired, one provider substitution).

## Before → after measurements

`python3 reports/round-24/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 24".

## SHONEN

- [~] Box 1 (real decision tables, cited sources) — verified-with-conditions, non-author reviewers named in the dossier (not self-attested)
- [~] Box 2 (end-to-end domain task executed and logged) — verified-with-conditions, non-author reviewers named
- [~] Box 3 (executable without oral context) — verified-with-conditions, non-author reviewers named
- [~] Box 4 (no cross-domain bleed; PROVINCE accurate) — verified-with-conditions, non-author reviewers named

All four boxes carry named non-author `verified-with-conditions` verdicts with
traced conditions — the strongest probationary evidence the lane has produced.
The promotion decision itself is the operator's; this round makes no roster
claim.
