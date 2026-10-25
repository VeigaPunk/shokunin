# kotodama — round 25 report (2026-10-18)

Loop 3, build 1 of 4 — operator regimen (amended; **devin provider test**).
One 64-worker batch on `devin/deepseek-v4-1-flash-high` (26/64 completed,
31-min wave).
Baseline `f74fc94`; work commit **fc13cd27b9e78d5d7c4f70740fd26c9383a7447b**.

## Work performed

- **Operability (claim O):** the typed-pipeline gate's false red is
  root-caused (a lossy `yaml_lines` rebuild double-escaping the CX-01 pattern
  and manufacturing 8 DERIV-REPLAYs, plus the `owed_slot` nullish gap) and
  fixed with named input-class refusals (`typed-declared-source`,
  `typed-unresolvable`, `typed-stale-source`, `typed-rebuilt`,
  `typed-unfaithful-rebuild` → exit 2) — the stronger of the two sanctioned
  branches; the source-packet entry still passes 19/19 byte-identical. Handoff
  v3's stale claim prose (8 assertions across 4 revisions) corrected to the
  family-clean present state and re-pinned as `declared-in-r4`.
- **Depth (claim D):** the round-17 argot-derivation forecast delivered as an
  executable leg (derivation replay for register-scoped forms, D4L-ARGOT-DERV
  class, real negatives) — with the delivered-vs-forecast delta named honestly:
  the register-form domain in the delivered D4 packet is empty (design-forecast
  never built into components); the leg stands ready over an empty domain.
- **Coverage (claim C):** `corpus/lessons/README.md` reconciled across all 24
  round files with the open-question queue and owners.

## Landed changes

Commit `fc13cd27` — gate fix + pin cascade, v3 supersession, argot leg,
lessons index, records.

## Before → after measurements

`python3 reports/round-25/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 25".

## Conformance notes

A transient mid-round gate breakage (~90 s, `KeyError: 'owed_slot_of'`) is
documented with its window; measurements inside it are void. Remainders named
by the shard auditors: the r4 twin gap, the empty argot domain, two sibling
pin tails. Devin route: viable for regimen use (slower per-worker; heavy
seats landed).

## SHONEN

- [~] SKILL.md decision tables — standing (author-asserted)
- [~] End-to-end domain task — hazards closed, argot leg delivered (author-asserted)
- [~] Instructions executable — gate selftests byte-identical (author-asserted)
- [~] No cross-domain bleed — scope clean (author-asserted)

Promotion review: the round-24 dossier stands; boxes remain `[~]` pending the
operator's decision.
