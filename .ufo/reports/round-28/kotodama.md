# kotodama — round 28 report (2026-10-18)

Loop 3, build 4 of 4 — operator regimen (amended; devin provider). One
64-worker batch on `devin/deepseek-v4-1-flash-high` (24/64 completed).
Baseline `69cecbc`; work commit **3b13a2f2821ed6f8ac1217842ab6830d592c7935**.

## Work performed

- **Depth (claim D):** the register-law replay leg
  (`tools/gates/register-law-gate.py`) — six `D4L-LAW-*` classes over four
  resolutions; the speaker leg resolves by exact token with polarity in
  `kind` (a substring matcher would grant exactly the two offices "stamp-holder
  only — no master, no delegate" forbids — designed out). RL-4 fixed: 8
  records now reach the packet (four-site pin cascade). The leg immediately
  earned its keep: **4 real D4L-LAW-DANGLING findings on the clean packet** —
  every `design_row` (QREG-05..08) names registers records that do not exist;
  the design's own defect, surfaced by its own checker, priced for round 30.
  Calibration honesty: the leg reports 6 findings on the clean packet and says
  why; two control classes are inert-by-saturation and reported as such.
- **Operability (claim O):** the final build-round pin sweep — all surfaces
  re-verified against the amended packet; new-row re-pins; battery 9/9;
  replays green.
- **Coverage (claim C):** the RL-3 ceiling recorded in the register-strata
  entry (append-only amendment) + the register-lexicon-ceilings knowledge
  entry; README reconciled.

## Landed changes

Commit `3b13a2f2` — law replay leg, RL-4 fix + cascade, sweep, ceiling
knowledge, records. Loop 3 builds complete (rounds 25-28).

## Before → after measurements

`python3 reports/round-28/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 28".

## SHONEN

- [~] SKILL.md decision tables — standing (author-asserted)
- [~] End-to-end domain task — the law now checks itself (author-asserted)
- [~] Instructions executable — sweep + gates green (author-asserted)
- [~] No cross-domain bleed — scope clean (author-asserted)

Promotion review: the round-24 dossier stands; boxes remain `[~]` pending the
operator's decision.
