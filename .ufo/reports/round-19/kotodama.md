# kotodama — round 19 report (2026-10-18)

Loop 2, build 3 of 4 — operator regimen (amended; **hyper provider
substitution** per operator directive). One 64-worker batch on
`hyper/deepseek-v4.1-flash` (17/64 completed — the hyper route is slow;
orchestrator-authored validation after the scribe seat failed).
Baseline `169c616`; work commit **caf1beac19b55f3bbce47e4a9e7e8710cc1c581d**.

## Work performed

- **Depth (claim D):** SKILL.md gains the D4-derived craft subsections —
  slot-label routing (one routing row per translated label; the owed slot
  named once, on the slot's own row) and derivation-replay discipline
  (machine-readable pattern/output pairs; the serializer round-trip corruption
  class; the text-transform rule). Three analyst + two reviewer fragments;
  the reviews' pre-repair red measurements (L2 fail, red selftest) were
  superseded by the round-18/19 integration fixes and are errata'd in the
  drafts, not re-rolled.
- **Coverage (claim C):** ten new sourced entries — verification 15→20,
  synthesis 24→29; integrator audit: zero defects (every entry gap-named,
  frontmatter-complete, decision-record carrying, source-resolving).
- **Operability (claim O):** the battery registers 9 gates (7 structural
  executed + the 2 D4 adapters under duty-2 baseline inspection — the mirror
  cannot host peer-dependent gates; the mode is documented); committed
  expected.json baselines for both D4 gates (17 valid baseline rows);
  battery selftest 35/35; adapter selftest repaired to 12/12.

## Landed changes

Commit `caf1beac` — entries, SKILL subsections, battery registration, D4
baselines, records. Integrator acts: errata + landings; selftest repair (the
projector's era-alias leg requires a D2 component even for D4 packets —
documented wart routed); availability record closed
(`reports/round-19/availability.json`).

## Before → after measurements

`python3 reports/round-19/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 19".

## SHONEN

- [~] SKILL.md decision tables — two D4 subsections landed (author-asserted)
- [~] End-to-end domain task — entries + craft codification executed (author-asserted)
- [~] Instructions executable — battery 35/35, adapter 12/12 (author-asserted)
- [~] No cross-domain bleed — scope clean (author-asserted)

Promotion review not requested; boxes remain `[~]`.
