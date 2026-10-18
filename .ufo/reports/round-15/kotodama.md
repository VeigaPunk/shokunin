# kotodama — round 15 report (2026-10-17)

Loop 1, GLM round 1 of 2 — operator regimen (amended). One 16-worker batch on
`zai-coding-plan/glm-5.3-flash-low` (zai MAX thinking effort; 12/16 completed,
2h wave; the timed-out builder seat's role was covered by the landed validator
suite + deterministic packet build).
Baseline `c60b17c`; work commit **16652e822e9dd5d83f7ab9e6078cbf010fc8f7e6**.

## Work performed

- **Operability (claim O):** handoff packet v2 (`reports/round-15/handoff/`)
  closes the round-12 semantic reject: 16/16 fields + 20/20 glossary held;
  15/15 claims carry uncertainty {status, basis} (8 supported / 5 partial /
  2 unresolved, zero boilerplate — 23/23 basis locators independently
  resolved); 50/50 claim-to-record links resolve to real records; the D2
  aggregate edge dissolved into 34 atomic typed edges; validators durable
  (packet_uncertainty 19/19, packet_links 31/31 selftests); frozen
  expected.json + freeze/verify tool with 24/24 tamper controls; contract
  audit re-run = **pass-with-named-gaps** (bilateral read + L0 digest remain
  lore-owned; negative control: the same protocol reproduces both round-12
  reject findings on v1).
- **Depth (claim D):** SKILL.md gains the claim-uncertainty decision table
  (three-status + basis grammar + verification-partition crosswalk, 17/17
  rule rows cited) + 13 error-pattern rows
  (`reports/round-15/knowledge/`).

## Landed changes

Commit `16652e82` — SCORECARD/LOG records; SKILL.md subsection. Integrator
acts: settled-tree validation rerun; SKILL BLOCK A landing repaired (slicing
defect caught); reviewer findings F9-1/F9-2/F10-1 routed to round 16.

## Before → after measurements

`python3 reports/round-15/run-validation.py` → exit 0. Verdicts in
`SCORECARD.md` §"Axes — round 15": operability/depth/calibration improved;
coverage/freshness/adjacency unchanged.

## SHONEN

- [~] SKILL.md decision tables with cited sources — uncertainty table landed (author-asserted)
- [~] End-to-end domain task — handoff v2 executed and audited (author-asserted)
- [~] Instructions executable — validators + frozen-verify selftest (author-asserted)
- [~] No cross-domain bleed — filed rounds preserved; lore-owned items stay open (author-asserted)

Promotion review not requested; boxes remain `[~]`.
