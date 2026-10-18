# kotodama — round 18 report (2026-10-18)

Loop 2, build 2 of 4 — operator regimen (amended). One 64-worker batch on
`opencode-go-2/deepseek-v4.1-flash` (19/64 completed; orchestrator built the
D4 adapter the wave never delivered).
Baseline `c66ac3c`; work commit **e5718945a1ab0a0c3db955338d2cae77d68fd348**.

## Work performed

- **Operability (claim O):** the typed-pipeline gate generalized — declared
  assembler identity (packet-declared pin; D4 profile via
  `tools/gates/typed-pipelines.json`), default D2 path byte-identical (16/16
  legs pre- and post-change); re-pin cascade green (round-18 repin-d2 manifest
  11/11 reproduced, round-9 baseline pins, round-16 v2-07 helper pins);
  L2-channel D4-family accounting (removed-artifact count vs costumes whose
  field actually moved); before/after digest table
  (`d96958b6 → 04ad4bb4`).
- **Depth (claim D):** `tools/assemble-d4-typed.py` built (text-transform
  architecture — original packet bytes preserved; the serializer round-trip
  corruption class diagnosed: regex backslash doubling, boolean/null
  stringification). The generalized gate runs D4 **19/19 legs**: findings
  exactly equal the 15-hold + 1-note expected set; routing 12 rows (6 garment +
  6 slot, owed slots named once); channel differential = exactly the 6
  PHON-INVENTORY artifacts removed with zero additions; round-18 frozen
  manifest replays green.
- **Coverage (claim C):** round-18 civ-map revision applies the round-17 patch
  (round-16 map untouched).

## Landed changes

Commit `e5718945` — gate generalization, D4 adapter, frozen manifests, map
revision, records. The round-17 D-rejection stands on record; its artifacts
are now fully verified.

## Before → after measurements

`python3 reports/round-18/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 18": operability/depth/coverage/calibration
improved; freshness/adjacency unchanged.

## SHONEN

- [~] SKILL.md decision tables — unchanged (author-asserted)
- [~] End-to-end domain task — D4 typed pipeline gate-verified (author-asserted)
- [~] Instructions executable — adapter selftest + 19/19 gate legs (author-asserted)
- [~] No cross-domain bleed — filed rounds preserved; pause respected (author-asserted)

Promotion review not requested; boxes remain `[~]`.
