# kotodama — round 16 report (2026-10-18)

Loop 1, GLM round 2 of 2 — operator regimen (amended). One 16-worker batch on
`zai-coding-plan/glm-5.3-flash-low` (zai MAX thinking effort; 16/16 completed).
Baseline `0ce7714`; work commit **f30b6f8188937632bbedd0e7b29aeefff6f8b07b**.

## Work performed

- **Coverage (claim C):** partition-wide staleness map
  (`reports/round-16/civ-map.json`) — 94/94 civilizations entries receipted:
  82 current, 12 stale-documented with named reasons (inuit's stable-404
  Dorais locator; maya-classic couples gap; mesoamerica/mongol/muisca
  hard-fail URLs; 7 rows whose URL sets were never swept — deferred by the
  freshness pause, not evidence of breakage); 8 shard receipts with dated
  command evidence; independent auditor re-derived the map, spot-checked 20
  entries, re-verified all 12 stale reasons; 2 map defects found and fixed by
  the integrator.
- **Operability (claim O):** the three round-15 reviewer findings closed with
  controls — edge `source` validation (E-SOURCE-UNKNOWN; selftests 31→38);
  `#L<n>` line-anchor vs record-id collision closed (dangling links rejected,
  real ids and non-JSON anchors intact); handoff link coverage completed
  (33 orphans → 0) via keyed build `packet-v2-07` (83/83 links, gate 16/16 +
  20/20, frozen baseline refreshed).

## Landed changes

Commit `f30b6f81` — SCORECARD/LOG records. Integrator acts: map repoint +
row annotations (3 defect classes); v2-07 baseline re-frozen after the verify
seat pinned a freeze/verify canonicalization divergence; settled-tree
validation rerun.

## Before → after measurements

`python3 reports/round-16/run-validation.py` → exit 0. Verdicts in
`SCORECARD.md` §"Axes — round 16": coverage/operability/calibration improved;
depth/freshness/adjacency unchanged.

## SHONEN

- [~] SKILL.md decision tables — uncertainty table (r15) stands (author-asserted)
- [~] End-to-end domain task — civ-map + harness closure executed (author-asserted)
- [~] Instructions executable — 38-check link suite + validators (author-asserted)
- [~] No cross-domain bleed — filed rounds 8-15 preserved; pause respected (author-asserted)

Promotion review not requested; boxes remain `[~]`.
