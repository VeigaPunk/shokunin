# kotodama — round 17 report (2026-10-18)

Loop 2, build 1 of 4 — operator regimen (amended). One 64-worker batch on
`opencode-go/deepseek-v4.1-flash` (30/64 completed; orchestrator integration).
Baseline `9b49a4a`; work commit **3dd3754207032cb81f5fb3e202fe85cf79211339**.

## Work performed

- **Coverage (claim C — verified):** the 12 round-16 stale-documented civ
  entries dispositioned — 7 fixed with live, content-verified replacement
  locators (inuit, muisca, mongol, mesoamerica, maya-classic + never-swept
  rows), 5 replacement attempts documented; 4 verifier seats re-ran the
  evidence; map-patch proposed (`reports/round-17/civ/`).
- **Operability (claim O — verified):** `tools/assemble-culture-d4.py` durable
  assembler (81/81 selftest controls; `--check` byte-identical); integrator
  eras normalization (flat tag list per the projector contract + mapping
  records under `era_records`, recorded in the packet's normalizations).
- **Depth (claim D — FAILED as declared):** examples/culture-d4/ is complete
  (12 components, deterministic packet e7ecd204…) and the typed projection
  runs over it (74 labels / 15 holds / 0 fails emitted) — but the round-11
  `typed-pipeline-gate` L1 assembler-identity leg pins assemble-d2 output
  bytes and structurally cannot consume a D4 packet. "Gate findings == D4
  hold set" is not executable this round.

## Landed changes

Commit `3dd37542` — D4 tree + assembler + eras fix + typed projection +
civ fixes + records. Integrator acts: eras normalization; design-fork ruling
(delivered tree rules); gate-boundary diagnosis with the round-18 recipe
(parameterize the assembler-identity leg; re-pin cascade: round-11 frozen
manifest, round-9 baselines, round-16 v2-07 expected.json helper pins).

## Before → after measurements

`python3 reports/round-17/run-validation.py` — C PASS, O PASS, D FAIL.
Verdicts: `SCORECARD.md` §"Axes — round 17".

## Round status: REJECTED on D

C/O verify; no axis harmed; the D4 artifacts stand for round 18's gate
generalization. The design fork (three D4 concepts in doc seats) is recorded
as a calibration lesson: design-authority seats must converge before
component seats build.

## SHONEN

- [~] SKILL.md decision tables — unchanged (author-asserted)
- [~] End-to-end domain task — D4 culture built + civ fixes executed (author-asserted)
- [~] Instructions executable — assembler 81/81 (author-asserted)
- [~] No cross-domain bleed — NON-CANON posture; scope clean (author-asserted)

Promotion review not requested; boxes remain `[~]`.
