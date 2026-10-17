# kotodama — round 8 report (2026-10-17)

Loop 1, build 1 of 4 — operator regimen (3 loops × 7 rounds, lane rounds 8–28).
One 64-worker batch on `opencode-go/deepseek-v4.1-flash` (all 64 completed).
Baseline `cf338a7`; work commit **e1694bad6ac96aca45a11ca5746582b275929355**
(lane repo HEAD at report time; `git merge-base --is-ancestor e1694ba HEAD` holds).

## Work performed

- **Freshness (claim F):** 15 residual round-6 reconciliation rows rechecked
  against live sources — `kotodama-shokunin/reports/round-8/freshness/R8-F01..F15-receipt.{json,md}`;
  per-receipt quote verification against extracted texts; documented access
  failures carried (e.g. R8-F01: 6). Spot-check audit: `freshness/audit.md`.
- **Operability (claim O):** round-7 harness defect diagnosed
  (`operability/o01-diagnosis.md`) and fixed in new `tools/harness/r8_checks.py`
  (regression controls both directions); 20 legacy defects inventoried from
  supplemental reviews 26/29 (`defect-inventory.json`); 10 isolated negative
  controls (`operability/neg-controls/neg-04..13/`); five gate files hardened
  (duplicate-key/depth-cap/anchor-tag rejections);
  `operability/battery-rerun.json` (battery 10/10, craft 10/10 + 18/18 CLI);
  round-3 frozen manifests reproduce 7/7 isolated.
- **Depth (claim D, capability `d2-typed-labels`):** `tools/d2-typed-labels.py`
  (five kinds, declaration-based typing, TL-01/TL-02 holds, borrow-ledger
  clock checks); design spec + shard fragments + adversarial reviews under
  `reports/round-8/depth/`; typed projection
  `examples/culture-d2/typed-labels.d2.yml`; SKILL.md label-typing decision
  table + 15 error rows landed from `depth/skill-table-draft.md`.
- **Metadata sweep:** 11 shard fragments (`reports/round-8/metadata/`)
  repaired `source`/`verified-at`/`recheck` frontmatter across 179
  `corpus/knowledge/` entries (in place, own-lane files only).
- **Scribe/audit:** `corpus/lessons/round-8.md` (gate-keeper survey + Gate
  section); `reports/round-8/adjacency.md` (no bleed; scope-checked).

## Landed changes

All in commit `e1694ba` (336 files) — each tied to a `LOG.md` entry under
"2026-10-17 — Round 8 admitted". Orchestrator integration on top of swarm
output: D2 packet regenerated (`tools/assemble-d2.py`) to re-pin the
reader sha after the legitimate costume-gate repair; SKILL.md table landed;
SCORECARD round-8 section; LOG entry. No sibling-lane, template, or script
writes (git-scope verified, `adjacency.md`).

## Before → after measurements

Counting command: `python3 reports/round-8/run-validation.py` → exit 0
(`reports/round-8/validation.json`, independent re-run `rerun.json`).

| claim / axis | before → after |
|---|---|
| F / freshness | 15 residual rows, 0 round-8 receipts → 15/15 receipts, 215 distinct substantive passage keys (harness count), reconciled 11 partial-support / 4 unresolved (raw 15× supported preserved) |
| O / operability | harness mis-rejected duplicate-parent-receipt controls; unrepaired legacy selftest/parser defects → fix green both directions, 20 defects inventoried, 10 negative controls, selftest batteries green |
| D / depth | no typed-label handling → capability runs, selftest 39/39, D2 packet byte-identical regeneration, frozen replay clean |

Axis verdicts (full table): `kotodama-shokunin/SCORECARD.md` §"Axes — round 8".
depth improved, coverage unchanged, operability improved, freshness improved,
calibration improved (unclaimed observation), adjacency unchanged. No axis
harmed; no exploratory claims. Admission: all three claims verify.

Limits: receipts are current-constraint rechecks, not historical
certifications; 4 rows remain unresolved; typed-label holds are
representation discipline, not real-language clearance.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — label-typing table landed round 8 (`kotodama-shokunin/SKILL.md` "Label typing"; author-asserted, no non-author verifier this round)
- [~] At least one end-to-end domain task executed and logged — D2 typed-label pipeline + 15 source rechecks (`LOG.md` 2026-10-17 round-8 entry; author-asserted)
- [~] Instructions executable by an agent without oral context — gates/selftests run green (`reports/round-8/operability/battery-rerun.json`; author-asserted)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `reports/round-8/adjacency.md`; contract-digest drift escalated to `.ufo/l0-questions.md`, not absorbed

Promotion review: not requested this round; all boxes remain `[~]` for lack of
a named non-author verifier.

L0: `kotodama | round-8 | worldbible-integration-contract digest drift vs lore's open r93 ratification — owner of the digest update?`
