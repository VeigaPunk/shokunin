# kotodama — round 36 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 4. Declared: 32 workers on
`hyper/deepseek-v4.1-flash`. **Observed route: devin/deepseek-v4-1-flash-high** —
hyper returned `402 out of credits` for all 32 seats (attempt recorded,
`telemetry/availability-attempt-1.json`); the devin fallback is the regimen's
declared route for exactly this condition. The fallback batch completed **32/32**.
Baseline `ce103bf`. Claims D/C/Ca. **Round status: REJECTED on D (failed as
declared); C and Ca verify; no axis harmed** — the honest-stop precedent of
rounds 17/22/11. Counting command:
`python3 reports/round-36/run-validation.py` → `reports/round-36/validation.json`
(exit 1 by design: the receipt records the rejection).

## Work performed

- **Depth (claim D — FAILED AS DECLARED):** the wave's K01 re-read falsified the
  claim's premise: the "register-form domain is EMPTY" record (r25) was already
  closed by rounds 26/27, which landed the eight register forms and the five-row
  law — both legs green and non-vacuous today (argot gate: 187 records, 8 derived
  pairs, 0 violations; law gate: 5 rows, 0 findings). Nothing was landed under the
  failed claim. The genuine residue — F-6 counters, the unused `head2` domain,
  RL-8's missing era leg, and a 13-vs-12 component read-set asymmetry
  (`13-register-law.yml` in the packet manifest but not the r7 freeze read set) —
  is routed to a future round under a corrected claim, with K01's census as the
  recipe.
- **Coverage (claim C — verified):** the routed round-35 spare landed as
  `culture-material/timekeeping-instruments.md` (40,234 bytes, audit-clean against
  the round-35 runbook with named defects F1-F5 filed); corpus 211 → **212**
  (culture-material 24 → **25**); `corpus/README.md` reconciled to revision 2.1 —
  the round-28 sweep reports 212 rows == 212 files, zero findings — and the delta
  also repairs the rev-2.0 row-order defect (three rows re-sorted ASCII-ascending).
  One named observation: the delivered README digest differs from the audit's
  staged prediction while the sweep is green (prediction-vs-delivery nuance).
- **Calibration (claim Ca — verified):** the mid-loop recount ledger landed
  (`calib/recount-ledger.json`): 17 filed counting commands from rounds 33-35
  re-run (isolated where a runner is involved), 15 exact matches and 2
  dispositioned mismatches (named causes, none smoothed), with the Ca04 sample
  verification.

## Landed changes

- `corpus/knowledge/culture-material/timekeeping-instruments.md` — new entry.
- `corpus/README.md` — revision 2.1 (CM 25, totals 212, order repair).
- `reports/round-36/` — the full round record including the recount ledger.
- Filed bytes: **zero** writes to `reports/round-1..35/**`, the 211 baseline
  corpus entries, `corpus/lessons/*.md`, `tools/gates/frozen/**`.

## Before → after measurements

- **C:** census 21/23/24/29/20/94 = 211 → 21/23/**25**/29/20/94 = **212**;
  sweep green; audits filed.
- **Ca:** no cross-round recount → 17-row ledger, 15 match / 2 named mismatch.
- **D:** register legs measured green with a non-empty domain — the claim's
  before-state is falsified; the receipt's D leg carries the evidence.

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. A rejected round is an honest
outcome: D's premise failed, the evidence is filed, the residue is routed.

## Conformance note

A seat briefly executed the round-35 runner in-tree during the wave (the
r35 receipt showed modified, then byte-identical to HEAD within ~25 s). The
absolute rule was breached; the event and its clean final state are recorded in
LOG.md and the round's telemetry. Final tree state: all filed receipts == HEAD.
