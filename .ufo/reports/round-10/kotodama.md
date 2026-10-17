# kotodama — round 10 report (2026-10-17)

Loop 1, build 3 of 4 — operator regimen. One 64-worker batch; attempts 1–3 on
`opencode-go-3/-4/-5` all failed at launch with `402 Insufficient account
funds` (keys unprovisioned; `kotodama-shokunin/reports/round-10/availability-attempt-{1,2,3}.json`), attempt 4 on `opencode-go/deepseek-v4.1-flash` carried the round (61/64 completed; 3 late scribe seats landed before integration).
Baseline `eb348f3`; work commit **94ca098b8ab03be52ec80f6925538e5e2c0ed327**.

## Work performed

- **Coverage (claim C):** 10 new sourced knowledge entries — linguistics
  (`language-shift-obsolescence-revival`, `numerals-and-measures`,
  `sound-symbolism`), myth-symbol (`direction-symbolism`,
  `divination-omen-systems`, `plant-symbolism`), culture-material
  (`transport-mobility-lexicon`, `vessel-container-lexicon`), verification
  (`header-conformance-readings`, `verification-independence-anti-circularity`);
  each gap-named, frontmatter-complete, decision-record carrying; 10 paired
  reviews + 4 audits (`reports/round-10/coverage/`); README index reconciled.
- **Freshness (claim F):** 192-row drift ledger covering 36/36 cited commands
  (14 shard fragments + integrator additions); stale items fixed with
  evidence or documented (`reports/round-10/drift/`).
- **Operability (claim O):** 24/24 findings from rounds 8–9 dispositioned
  (18 fixed-with-control, 5 wont-fix documented, 1 wrong) + verifier re-runs
  (`reports/round-10/findings-tracker.json`).

## Landed changes

Commit `94ca098` — tied to the LOG.md round-10 entry. Integrator acts:
re-ran 14 hashless ledger rows; attached 10 fix-evidence pointers; added the
36th cited command to the ledger; added gap fields to two entries; reverted
filed-receipt rewrites (below); removed worker scratch.

## Before → after measurements

`python3 reports/round-10/run-validation.py` → exit 0. Verdicts in
`SCORECARD.md` §"Axes — round 10": coverage/freshness/operability improved,
depth unchanged, calibration improved (unclaimed), adjacency unchanged.

## Conformance defects (recorded, status-neutral)

1. A stale-fixer rewrote filed round-8/round-9 receipt bytes
   (`reports/round-9/validation.json` stdout hashes,
   `reports/round-8/run-validation.py`); integrator restored both from git —
   staleness is documented in the drift ledger, never back-patched into
   filed receipts.
2. opencode-go keys -3/-4/-5 are unprovisioned (402 at launch); key rotation
   for the regimen is now keys 1/2.

## SHONEN

- [~] SKILL.md decision tables/error patterns with cited sources — registry tables extended this round (author-asserted)
- [~] End-to-end domain task executed and logged — 10-entry coverage expansion + drift sweep (author-asserted)
- [~] Instructions executable without oral context — ledger/tracker re-runnable (author-asserted)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — fleet root verified clean (author-asserted)

Promotion review not requested; boxes remain `[~]`.
