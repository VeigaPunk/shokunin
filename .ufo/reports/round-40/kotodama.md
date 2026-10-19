# kotodama — round 40 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 8 — the loop-1 midpoint
consolidation round. One 24-seat batch on `zai-coding-plan/glm-5.3-flash`,
**24/24 completed**. Baseline `fd55e1f`. Claims C/Ca/A. Acceptance:
`python3 reports/round-40/run-validation.py` → `reports/round-40/validation.json`.

## Work performed

- **Coverage (claim C — verified):** four linguistics entries landed (21 →
  **25**; total 216 → **220**): `taboo-strata-lifecycle`,
  `dialect-register-consistency`, `translation-protocol-fidelity`,
  `sacred-registers-liturgical-language` — K01-r39's routed gaps G2-G4. Each
  audited pre-landing 4/4 PASS (C05; C07 independently verified the delta
  numbers and re-audited; one S2 on C04's Reading-2 pin + minor S3s named).
  README revision 2.3 — sweep-green at 220 rows == 220 files.
- **Calibration (claim Ca — verified):** the defect-queue v2 landed
  (`op/defect-queue-v2.json`, **38 rows**): all 24 r37 rows re-dispositioned
  (8 reclassified fixed-with-evidence with pointers), the r38/r39 findings
  folded, every row owner-complete with next-touches aligned to positions
  41-46. The reviewers' mandated folds are applied: five rows (N3 argot-digest
  supersession, N6 wrapped-field extractor, N7 receipt fidelity, the r39 I-C05
  resolver durability, F-A02-1's stale era prose), the chdir locator corrected,
  and the R36-D-DECLARATION class ruling recorded. Ca02 sampled 72.7% of the
  draft against origin records — 24/24 match.
- **Adjacency (claim A — verified):** the consolidated r37-40 audit (A01/A02,
  independently re-run by A03): every touched surface verdict-filed, zero
  unfiled bleed, PROVINCE byte-accurate at HEAD (`c53782a`), contested items
  routed-not-absorbed.

## Landed changes

- `corpus/knowledge/linguistics/` — four new entries; `corpus/README.md` — rev 2.3.
- `reports/round-40/op/defect-queue-v2.json` — the 38-row queue.
- `reports/round-40/run-validation.py` — **the O12 cure**: the first runner in
  the r34-r39 absolute-ROOT streak to resolve its root relatively
  (`Path(__file__).resolve().parents[2]`, no chdir), with non-null
  `runner_sha256` and round-specific findings (the N7 receipt-fidelity cure).
- Filed bytes: **zero** other writes (P1 clean).

## Before → after measurements

Counting command: `python3 reports/round-40/run-validation.py` (exit 0 at
close; receipt `reports/round-40/validation.json`).

- **C:** linguistics 21 → 25, total 216 → 220; sweep 220 == 220; audits 4/4.
- **Ca:** r37-aged 24-row queue → 38-row owner-complete queue-v2 with the
  r38/r39 findings and the reviewers' folds; 72.7% sample match.
- **A:** no consolidated r37-40 adjacency pass → every surface verdict-filed;
  PROVINCE byte-accurate.

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. Named: the reviewers' queue-v2
completeness catch (folded, not smoothed); the N7 finding curing itself in this
runner; F-A02-1 routed (packet surface, next content round); K02's remaining
census cross-check carried to r41.
