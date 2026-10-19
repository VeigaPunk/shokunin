# kotodama — round 42 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 10. One 32-seat batch on
`devin/deepseek-v4-1-flash-high`, **31/32** (C05 failed at dispatch;
re-dispatched as the completion seat — 32/32). Baseline `ac47c78`. Claims O/C.
**Round status: REJECTED on C (failed as declared); O verifies; no axis
harmed.** Counting command: `python3 reports/round-42/run-validation.py` →
`reports/round-42/validation.json` (exit 1 by design: the receipt records the
rejection).

## Work performed

- **Operability (claim O — verified):** the N6 successor extractor landed
  (`tools/harness/couples-reference-extractor.py`, selftest green; the N6
  regression guard reads the wrapped `phonetics-phonology.md:72-77` field
  whole — all four targets, incl. `tone-prosody.md` via the soft-wrap rule).
  The true defect host was traced to the **filed** r19 instrument (`$` under
  re.M) with r27/r28 successors — filed bytes untouched by rule; the fix lives
  in the successor. The corrected census: 223 entries / 2730 references
  (2556 direct / 166 fallback / 2 unresolved), 1 wrapped field. Also landed:
  the **complete 263-line basename policy** as a successor document — the r39
  landing was a truncation (integrator extraction defect, found by K01's
  byte-comparison; the filed r39 artifact keeps its bytes, the correction is
  append-only).
- **Coverage (claim C — FAILED as declared):** three of four entries landed
  (`mineral-stone-symbolism`, `purity-pollution-boundary-systems`,
  `sacred-topography-pilgrimage` — myth-symbol 23 → **26**, total 220 →
  **223**, README rev 2.4 sweep-green). The fourth **collided**: C01 and C04
  authored the same lithic register mid-wave (the gap scout assigned it
  twice); the integrator ruling lands C04 (ownership-first structure) and
  routes C01 as the named spare (`cov/C01-mineral-spare.md`). The declared
  27/224 is therefore unmet. **Incident:** two seats' stale path proposals
  momentarily overwrote `animal-symbolism.md` and `plant-symbolism.md`; the
  integration census caught the arithmetic, both restored byte-exact from
  HEAD, the drafts re-landed under content-true slugs. Audits: 4/4
  PASS-with-defects (C05 completion audit; 11 named defects).

## Landed changes

- `tools/harness/couples-reference-extractor.py`; `corpus/knowledge/myth-symbol/` — three entries; `corpus/README.md` — rev 2.4.
- `reports/round-42/op/couples-census-corrected.json`, `couples-extractor-census.json`, `calib/basename-couples-policy-full.md`, `cov/C01-mineral-spare.md`.
- Filed bytes: **zero** net writes (the two overwritten entries restored before commit).

## Before → after measurements

- **O:** the wrapped field read as empty → read whole (4/4 targets); the census corrected; the policy truncation corrected.
- **C:** myth-symbol 23 → 26 (not 27); total 220 → 223 (not 224); sweep green; audits PASS-with-defects; the shortfall is ruled, not smoothed.

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. A rejected round is an honest
outcome: the collision, the overwrite incident, and the truncation are on
record with owners; the routed spare makes the retry one claim away.
