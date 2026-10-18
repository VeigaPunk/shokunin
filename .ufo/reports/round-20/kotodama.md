# kotodama — round 20 report (2026-10-18)

Loop 2, build 4 of 4 — operator regimen (amended). One 64-worker batch on
`opencode-go/deepseek-v4.1-flash` (20/64 completed; the heavy integration seats
landed).
Baseline `122086b`; work commit **35b6797b42d48bec52e1e3ddba1f3afc9bb85046**.

## Work performed

- **Depth (claim D):** handoff e2e v3 — D4 artifacts join D2+D3 as sources;
  27 claims (16 supported / 7 partial / 4 unresolved) with D4-CL01..12 carrying
  the round-15 uncertainty grammar; 102/102 claim-to-record links resolve;
  handoff gate 16/16 + 20/20; v2 subset equality preserved; frozen v3 baseline
  with tamper control (`reports/round-20/handoff/`).
- **Operability (claim O):** the round-19 projector wart closed — per-family
  era-alias resolution (D4 packets take a documented skip; D2 path byte-identical:
  selftest 50/50, gate stdout sha unchanged); the D4 adapter selftest passes
  12/12 in a mirror that no longer copies the foreign D2 examples tree; the
  re-pin cascade landed as new rows with the before/after table extended.
- **Coverage (claim C):** corpus/README.md reconciled command-carried
  (civilizations 94, linguistics 20, myth-symbol 19, culture-material 18,
  synthesis 29, verification 20); known-gaps refreshed against rounds 17-20.

## Landed changes

Commit `35b6797b` — v3 exercise + packet, wart fix + repins, README, records.
Loop 2 builds are complete (rounds 17-20).

## Before → after measurements

`python3 reports/round-20/run-validation.py` → exit 0. Verdicts:
`SCORECARD.md` §"Axes — round 20".

## SHONEN

- [~] SKILL.md decision tables — standing (author-asserted)
- [~] End-to-end domain task — handoff v3 executed and audited (author-asserted)
- [~] Instructions executable — wart fix + repins replay green (author-asserted)
- [~] No cross-domain bleed — scope clean; pause respected (author-asserted)

Promotion review not requested; boxes remain `[~]`.
