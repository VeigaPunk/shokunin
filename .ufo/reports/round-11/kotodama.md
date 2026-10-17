# kotodama — round 11 report (2026-10-17)

Loop 1, build 4 of 4 — operator regimen. One 64-worker batch on
`opencode-go-2/deepseek-v4.1-flash`; 54/64 completed (10 late scribe-class
seats failed; no core-claim seat lost).
Baseline `e3ef171`; work commit **a3f6fcef2d92a1099581140c81d4264e9a4e2aa3**.

## Work performed

- **Depth (claim D — verified):** typed-label pipeline wired into the D2 flow
  (`reports/round-11/depth/`): design names the expected hold set
  pre-implementation (15 holds: 10× D2L-FORM-UNRESOLVED GAR-01..10, 2×
  D2L-NATIVE, 3× D2L-RANK); derived typed packet + `typed-pipeline-gate.py`;
  the five legacy gate scripts deliberately untouched (frozen-pin integrity);
  e2e findings exactly == expected hold set; measured differential: naming
  gate 17→7 findings, PHON-INVENTORY 10→0; negatives (channel smuggle,
  silent form-drop, hold laundering) each caught; 4 adversarial reviews.
- **Operability (claim O — verified):** `tools/exercise-handoff-e2e.py`
  assembles a handoff packet from live D2/D3 artifacts — 16/16 fields, 20/20
  glossary entries, `handoff-packet-check.py` green in isolation, committed
  frozen baseline with tamper control (`reports/round-11/handoff/`).
- **Freshness (claim F — FAILED as declared):** 192/192 drift-ledger rows
  rechecked (`reports/round-11/recheck/`); 147 stable = **0.778 < 0.95**;
  all 45 drifts dispositioned with named causes: dominant = round-10/11's own
  legitimate changes (SKILL +31/-17, 10 new corpus entries, errata),
  environmental (absolute-path embedding in JSON outputs), 3 transcription
  defects (incl. ledger row 187 whose grep leg was truncated at recording;
  its sha256sum leg reproduces the recorded prior exactly).

## Landed changes

Commit `a3f6fce` — tied to the LOG.md round-11 entry. Integrator acts:
3 receipt schema repairs (1:1 command text restored, row-047 hash
contradiction, row-187 disposition), summary.json recomputed.

## Before → after measurements

`python3 reports/round-11/run-validation.py` → D PASS, O PASS, F FAIL
(stability threshold). Verdicts: `SCORECARD.md` §"Axes — round 11".

## Round status: REJECTED

Claim F misses its declared threshold; D and O verify; no axis harmed. The
0.95 stability assumption cannot hold across build rounds that legitimately
change the tree — operator recalibration queued at `.ufo/l0-questions.md`.
Freshness axis-move claims pause; round 12 (Luna verify) audits this round.

## SHONEN

- [~] SKILL.md decision tables with cited sources — unchanged this round (author-asserted)
- [~] End-to-end domain task executed and logged — typed pipeline + handoff e2e (author-asserted)
- [~] Instructions executable without oral context — new gate/exercise selftests (author-asserted)
- [~] No cross-domain bleed — gate scripts untouched; fleet root clean (author-asserted)

Promotion review not requested; boxes remain `[~]`.
