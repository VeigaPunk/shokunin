# kotodama — round 14 report (2026-10-17)

Loop 1, integrate round — operator regimen (amended: expand rounds
cancelled). One 32-worker batch on `openai-codex/gpt-6.1-sol` at max effort
(27/32 completed; 5 scribe seats failed — consolidation by the orchestrator).
Baseline `a7bc9e9`; work commit **b02cfbc9468aa906f0ff8301ec643770fb2bcfd8**.

## Work performed

- **Operability (claim O):** all 8 round-12 routed items dispositioned in
  `reports/round-14/routed-resolution.json` — battery default roots fixed
  (default run exit 0, 7/7 gates, 29/29 selftest controls), tracker verifier
  pointer appended (original rows byte-identical), r8 audit-count erratum
  filed, draft-status reconciliations, runner-hash disposition,
  index-classification correction, status-conflict resolution,
  r11-draft-census reconciliation. Filed bytes of rounds 8-12 untouched.
- **Depth (claim D, capability `receipt-guard`):**
  `tools/harness/receipt_guard.py` — round runners refuse to overwrite a
  committed validation.json unless REFRESH_RECEIPTS=1 (exit 3 with named
  diagnostic); selftest both modes; retro-tests prove it would have caught
  the r8/r9 clobber; rounds 8-11 runners deliberately left filed/unchanged.
- **Calibration (claim C):** `reports/round-14/loop1-retrospective.md` —
  loop-1 final states: 4 admitted (8, 9, 10, 12), 1 rejected (11), 1
  operator-skipped (13); claim flags 14 passed / 1 failed; round-11
  denominators explicit (147/189 = 0.778; 147/192 = 0.7656 — both < 0.95);
  freshness-threshold question restated for the operator.

## Landed changes

Commit `b02cfbc` — SCORECARD round-14 section + loop-1 summary, LOG entry.
Integrator acts: routed-resolution.json authored; drafts landed; 5 failed
scribe seats' coverage folded; one disposition aligned to its evidence
(STATCONFL → resolved-by-documentation).

## Before → after measurements

`python3 reports/round-14/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 14" — operability/depth/calibration improved;
coverage/freshness/adjacency unchanged (freshness axis-moves still paused).

## SHONEN

- [~] SKILL.md decision tables with cited sources — unchanged (author-asserted)
- [~] End-to-end domain task executed and logged — integrate round executed (author-asserted)
- [~] Instructions executable without oral context — guard + battery selftests (author-asserted)
- [~] No cross-domain bleed — filed bytes untouched; fleet root clean (author-asserted)

Promotion review not requested; boxes remain `[~]`.
