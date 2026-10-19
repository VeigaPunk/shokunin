# kotodama — round 39 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 7. One 16-seat batch on
`zai-coding-plan/glm-5.3-flash` — the schedule's zai lane as declared, no
deviation. The batch completed 15/16 on the first dispatch (C05 hit a
concurrency error); C05 re-dispatched as the round's completion seat — 16/16.
Baseline `dfb0719`. Claims C/Ca. Acceptance:
`python3 reports/round-39/run-validation.py` → `reports/round-39/validation.json`.

## Work performed

- **Coverage (claim C — verified):** four sourced entries landed in the
  verification partition (20 → **24**; total 212 → **216**):
  `worked-example-verification`, `index-sweep-verification`,
  `contact-strata-verification-gate` (K01's gap G1), and
  `append-only-record-verification`. Each carries the round-35/36 contract; all
  four audited pre-landing by C05 (4/4 PASS; C03 clean; named S2/S3 defects on
  the other three, zero fabrication across 137 re-resolved citations). C01's
  entry demonstrates the gate is not green-by-construction — it audits
  `timekeeping-instruments.md:134` and files 3 real defects. `corpus/README.md`
  reconciled to revision 2.2 — the round-28 sweep reports 216 rows == 216 files,
  zero findings. A seat's stray in-corpus staging file (`C03-draft.md`) was
  removed at integration (provenance proven by digest).
- **Calibration (claim Ca — verified):** the isolation-replay protocol landed
  (`calib/isolation-replay-protocol.md`): a bwrap mount-namespace method that
  replays a filed runner at its close commit inside a disposable clone bound at
  the live root, defeating the O12 absolute-chdir hazard (Tier A canonical;
  Tier B no-bwrap fallback; Tier C documented as altered-source replay). Ca02
  replay-verified all four of the r37 recount's could-not-reproduce rows
  (R37-Ca-05..08) normalized-identical to their filed receipts; the successor
  ledger (`calib/recount-ledger-successor.json`) re-dispositions them
  reproduced-under-protocol, with R01-1's ruling (the mechanism alters executed
  bytes by design) recorded as the disposition basis. The basename-couples
  fallback is now documented policy (`calib/basename-couples-policy.md`,
  verified by Ca04 with two one-sentence defects filed for the queue).

## Landed changes

- `corpus/knowledge/verification/` — four new entries; `corpus/README.md` —
  revision 2.2 (sweep-green).
- `reports/round-39/calib/` — the protocol, the policy, the successor ledger.
- Filed bytes: **zero** other writes (P1 clean; the 212 baseline corpus entries
  byte-identical).

## Before → after measurements

Counting command: `python3 reports/round-39/run-validation.py` (exit 0 at
close; receipt `reports/round-39/validation.json`).

- **C:** verification 20 → 24, total 212 → 216; sweep 216 == 216, zero
  findings; 4/4 pre-landing audits PASS.
- **Ca:** 4 could-not-reproduce rows → 4 reproduced-under-protocol with
  evidence; the O12 hazard now has a canonical safe-replay protocol; the
  basename fallback is policy (334 = 319 direct + 15 fallback reproduced).

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. Named: the C05 concurrency
failure + completion re-dispatch; the stray staging file (removed); K01's
remaining gaps G2-G4 (unclaimed, routed); Ca04's two one-sentence defects.
