# kotodama — round 41 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 9. One 32-seat batch on
`openai-codex/gpt-6-luna-max`, **32/32 in ~7 minutes** — the fastest full wave
of the regimen. Baseline `456674d`. Claims O/Ca. Acceptance:
`python3 reports/round-41/run-validation.py` → `reports/round-41/validation.json`.

## Work performed

- **Operability (claim O — verified):** the round-runner template landed
  (`templates/round-runner-template.py` — the five contract points: relative
  ROOT, no chdir, guard-dominance, non-null runner_sha256, round-specific
  findings/limits) and the conformance checker
  (`tools/harness/round_runner_conformance.py`, selftest green). The 7-runner
  census (`op/runner-census.json`) is precise enough to be uncomfortable:
  r34/r35 carry absolute-root+chdir; r36-r39 add null runner_sha256; **r39 is
  mechanically caught duplicating r38's findings/limits verbatim** — the N7
  smoking gun, detected by the instrument rather than asserted. r40 shows zero
  defects: the conformant reference shape. The reviewers' census-scope question
  (seven vs eight) is named in the record: r33 is the relative-ROOT precedent,
  not a streak member; the streak is r34-r39, cured at r40, governed from here.
- **Calibration (claim Ca — verified):** the N3 pin census converged on one
  live-file hit — `SKILL.md:383`, a dated historical measurement that
  self-marks. The integrator ruling (`calib/pin-supersession.json`): no edit
  required; Ca02's optional rewording filed for a future SKILL pass. The
  queue's N7 + r39-runner-root-regression rows re-classed fixed-with-evidence
  against the checker output.

## Landed changes

- `templates/round-runner-template.py`, `tools/harness/round_runner_conformance.py`,
  `reports/round-41/op/runner-census.json`, `reports/round-41/calib/pin-supersession.json`.
- `reports/round-40/op/defect-queue-v2.json` — the two re-classifications
  (append-only update record).
- Filed bytes: **zero** writes to rounds 1-40, corpus, frozen.

## Before → after measurements

- **O:** no template/checker → both durable; the streak classified per-runner
  with evidence; r40 conformant.
- **Ca:** N3 premise (multiple stale live pins) → one self-marking historical
  hit, ruled; the queue re-classified.

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. Named: the seven-vs-eight
census scope; the trap-fixture output ambiguity (both printed the summary
line; the selftest's false-green controls + the census precision stand as the
verification); Ca02's optional delta carried.
