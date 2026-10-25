# kotodama - round-66 report

Lane tip (lands+records): `4589ebdd36659060a978d0bb5b41b8c4e275a549`
Lands commit: `65fe8572822ef83f1750593af77daddf34a1e337`
Records commit: `4589ebdd36659060a978d0bb5b41b8c4e275a549` (direct child of lands)

## Claims declared (claims.json, frozen pre-data)

1. C - coverage (sourced register): new entry `scent-perfume-aromatics-codes.md`
   + 22 registry rows S779-S800 (shrunk from S777-S800 after seat ScoutRow01
   died pre-lands; the missing rows are named in the lesson). Verdict:
   ACCEPT-C-66 PASS at `65fe8572` (`reports/round-66/telemetry/final-measures-c.txt`).
2. O - operability (separability bound, R65-D4): `tools/check-claim-separability.py`
   gains --jobs/--budget/--max-runs/--static-only + honest-partial; 63/63
   selftest; the round-66 manifest ran to a complete verdict (9 runs, 8
   findings, exit 1 - the Ca dispositions genuinely couple to the claims they
   verify). Verdict: ACCEPT-O-66 PASS (`final-measures-o.txt`).
3. Ca - calibration (R65-D1..D4 dispositions): D1 PASS (S753 re-capture
   sha256-bound, games re-pointed to S776), D2 PASS (receipts parented on the
   lands commit), D3 PASS (63 named seats' reports on disk + 1 declared dead),
   D4 PASS (manifest run complete). Verdict: ACCEPT-CA-66 PASS
   (`final-measures-ca.txt`, stamped revision = lands rev per criterion 17).

## Wave prepared status

Single task call dispatched the full 64-seat wave (spec-v2, ~56% attack
roles); 63/64 seats returned reports filed under
`.ufo/waves/round-66/w1/` (named per-seat in
`reports/round-66/telemetry/seat-evidence.txt`); ScoutRow01 dead
(provider error, no output - S777/S778 never produced). Row fragments
`.ufo/waves/round-66/rows/` integrated; 4 out-of-range rejects (S801-S804)
excluded by the shrunk claim.

## Noted

- S795's first row draft paired an archive.org PDF with a JSTOR capture (a
  different page). Replaced with JSTOR Daily (live+capture both verbatim);
  recorded as lesson mistake R66-M1 under new QUALITY criterion 18.
- Separability verdict prints 8 findings by design: Ca's counter legitimately
  names the other claims' counters and records; O's counter relies on
  round-66 counter files present only in other units. The manifest and run are
  receipts, not claim gates.

## SHONEN

- [~] Box 1 — `SKILL.md:20` decision table, `:468` error patterns, `:522` checklist; sources in `corpus/SOURCES.md` (lane assertion, no non-author verifier).
- [~] Box 2 — end-to-end work and measurements are logged in `LOG.md` Round 66 and `SCORECARD.md` Round 66.
- [~] Box 3 — instructions and counters are executable from repo paths; C/O/Ca receipts and census outputs are under `reports/round-66/telemetry/`.
- [~] Box 4 — PROVINCE scope holds; entry hands canon to lore and names adjacent partial owners one-way (`corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`, Boundaries).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
