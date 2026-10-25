# kotodama — round 38 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, position 6. Declared: 32 workers on
`xai-oauth/grok-4.7-fast` (xhigh). **Observed route (named deviation):** grok
returned `403 out of credits` for all 32 seats (attempt-1,
`telemetry/availability-attempt-1.json`); the batch dispatched on
`devin/deepseek-v4-1-flash-high`, was interrupted after 22 seats, and completed
by a 10-seat completion dispatch — **32/32 total**. Baseline `9bccc9b`.
Claims D/O. Acceptance: `python3 reports/round-38/run-validation.py` →
`reports/round-38/validation.json`.

## Work performed

- **Depth (claim D — verified):** the r36 register residue landed under the
  corrected claim. (a) The F-6 counters: D01's fenced patch (the corrected
  `derived_failures`-based `derived_ok` formula — the block's drafted
  `derived_pairs - violations` reads −1 on a synthetic two-failure fixture)
  landed byte-exact (sha `8c7dd098…`); the live packet now reports
  `derived_forms=8 derived_ok=8`; argot selftest 27→35. (b) The RL-8 era leg:
  adapted in-session from D08's verified law-gate design to the **argot gate**
  emitting `D4L-ARGOT-ERA`, per the wave's trade analysis (X01 T1: only that
  host+id is typed-pipeline-visible and pin-free; the law-gate host would red
  the battery's r30-post pin). Selftest 39/39 including the four era controls
  (fires on E0, names row+stage, silent on E1, not masked by a missing law
  block); planted-probe verification: a planted E0 stamp form turns the typed
  pipeline red via L3b-argot, the real packet stays 20/20.
- **Operability (claim O — verified):** the read-set roster guard landed as
  O01's fenced patch (triple-verified by O02/O03/O08 before application): the
  r7 row's missing 13th component (`13-register-law.yml`) is now named by a
  `manifest-roster` record without failing the row; selftest carries m15a/m15b;
  the r7 default chain still exits 0 with packet `45f57132…` byte-identical.
  Recorded limit (not overclaimed): the guard is naming, not detection.

## Landed changes

- `tools/gates/argot-derivation-gate.py` — F-6 counters + RL-8 era leg (landed
  sha `10c88433…`; pin-neutral: the gate is in no battery tuple).
- `tools/exercise-handoff-e2e.py` — the manifest-roster guard (sha
  `e5812751…`, matching the pre-application verification exactly).
- `reports/round-38/` — the full round record (32 fragments + the two fenced
  patches' provenance).
- Filed bytes: **zero** other writes; r7 freeze bytes untouched; the 212
  baseline corpus entries byte-identical (P1 clean).

## Before → after measurements

Counting command: `python3 reports/round-38/run-validation.py` (exit 0 at
close; receipt `reports/round-38/validation.json`).

- **D:** no `derived_forms/derived_ok` emitter, no era leg → counters live at
  8/8 and the era leg fires only on a genuine E0 stamp form (39/39 controls);
  law gate green; typed pipeline 20/20.
- **O:** the r7 read-set omission invisible to every instrument → a named
  `manifest-roster` row on the r7 class, with m15a/m15b selftest controls and a
  documented fix route (the next re-freeze absorbs the member).
- **Cross:** the wave's deeper findings are filed, not absorbed: the guard is
  row-blind by design (O03's G5 per-row check found four asymmetric filed rows,
  not two); nine seats carried cross-claim ids the claims.json never declared
  (X01, low severity).

## SHONEN

All four boxes untouched; marks stay operator-owned; nothing here is a
promotion, canon, clearance or closure verdict. Named deviations on record: the
grok→devin route, the interrupted-batch completion, the 0-byte O07 fragment.
