# kotodama — round 9 report (2026-10-17)

Loop 1, build 2 of 4 — operator regimen. One 64-worker batch on
`opencode-go-2/deepseek-v4.1-flash` (64/64 completed).
Baseline `a7bb205`; work commit **9dc18ec** (lane repo HEAD at report time).

## Work performed

- **Freshness (claim F):** 4 still-unresolved residuals escalated with 3
  retrieval strategies each (primary/museum-record, scholarly-fulltext,
  alternate-angle) — 12 receipts `reports/round-9/freshness/R9-F0*`;
  verifier chain V01–V03; spot-check audit `freshness/audit.md`;
  reconciliation `freshness/reconciliation.json`. Headline: R8-F01's round-8
  `to-verify` item closed at catalogue + transliteration level (Louvre
  cl010166127, CDLI P220619 = AO 5477 Rimush bilingual; qualified as a
  palaeo-Babylonian copy, not a contemporaneous object; 35 quoted passages
  machine-verified).
- **Operability (claim O):** committed expected.json drift-pin baselines for
  all 7 structural gates (`tools/gates/expected/<gate>/r9-pre/`,
  `tools/gates/frozen/<gate>/r9-pre/`); battery extension validates
  tampered → could-not-evaluate (`reports/round-9/baselines/battery-extension.md`);
  registry `baselines/registry.md`; audits 18–20 confirm baselines re-run
  clean, **zero gate behavior changes**, battery selftest green.
- **Depth (claim D):** D3 acceptance completed as new round-9 work —
  `reports/round-9/d3/` (check-diagnosis, determinism, evidence-coupling,
  replay, cli-negatives, interop, contract-crosscheck, 2 adversarial reviews).
- **Metadata verify:** 11 shards re-audited all 179 knowledge entries'
  frontmatter post-round-8 (`reports/round-9/metadata/`).

## Landed changes

Commit `9dc18ec` (149 files) — tied to the LOG.md round-9 entry.
Orchestrator integration acts (not work defects): reconciliation normalized
to the declared flat `raw_label` contract (verdicts untouched); D3
`expected.json` re-pinned for 3 drifted manifests — all three are round-8's
legitimate committed changes; two out-of-lane worker writes remediated
(fleet-root fragment moved into lane; junk PDF deleted).

## Before → after measurements

Counting command: `python3 reports/round-9/run-validation.py` → exit 0.

| claim / axis | before → after |
|---|---|
| F / freshness | 4 unresolved residuals → 4/4 partial-support, 12 escalated receipts + verifier chain, raw labels preserved apart |
| O / operability | 0/7 gates with committed baselines → 7/7, tamper → could-not-evaluate enforced, zero gate behavior changes |
| D / depth | D3 capability unadmitted → --check byte-identical, frozen replay exit 0 / 0 findings, capability row admitted |

Verdicts: `SCORECARD.md` §"Axes — round 9" — depth/operability/freshness
improved, coverage unchanged, calibration improved (unclaimed observation),
adjacency unchanged. No axis harmed.

## Conformance defects (recorded, status-neutral)

1. Two out-of-lane worker writes (fleet-root fragment; junk PDF) — remediated
   by orchestrator sweep; the X03 in-round adjacency check missed them.
2. `/tmp` inode table 100% full hit ≥5 shards; workers adapted via in-lane
   scratch. Operator cleanup decision queued at `.ufo/l0-questions.md`.

## SHONEN

- [~] SKILL.md decision tables/error patterns with cited sources — round 8 label-typing table stands; round 9 adds gate registry (`reports/round-9/baselines/registry.md`; author-asserted)
- [~] End-to-end domain task executed and logged — D3 acceptance + 4 escalated source rechecks (`LOG.md` round-9 entry; author-asserted)
- [~] Instructions executable without oral context — baselines/battery re-runnable (`audit-18..20`; author-asserted)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — with recorded defect: two out-of-lane writes remediated; contract-digest L0 question still open

Promotion review not requested; boxes remain `[~]` for lack of a named
non-author verifier.
