# kotodama — round 12 report (2026-10-17)

Loop 1, verify round — audits rounds 8-11. One 64-worker batch on
`openai-codex/gpt-6-luna-max` (25/64 completed; route capacity — recount
coverage completed by the orchestrator: 61 commands re-run and normalized to
the licensed disposition schema).
Baseline `69d0c21`; work commit **44070b4a6038f54e78d8d5be551e549fe202b0ee**.

## Work performed

- **Calibration (claim C):** 89-row recount ledger (`reports/round-12/recount/`):
  rounds 8-11 counting commands re-run, observed-vs-recorded compared, 12
  exact matches, 16 worker dispositions, 61 integrator coverage rows; round-11
  rejection numbers independently reproduced with the ratio correction
  (147/192 = 0.7656; 0.778 = 147/189 — both denominators now recorded).
- **Operability (claim O):** consolidated defect ledger
  (`reports/round-12/defects/ledger.json`, 15 entries): 7 fixed-with-control
  bounded — including rounds 8+9 filed `validation.json` clobbered post-commit
  by drift-ledger re-runs of round validators, restored byte-exact from
  `e1694ba`/`9dc18ec` — and 8 routed to round 14 with owner notes; regression
  battery green.
- **Adjacency (claim A):** consolidated audit (`reports/round-12/adjacency/`):
  10 new entries PASS (3 boundary-sensitive, no lane-authored rulings);
  PROVINCE accurate; handoff packet **rejected on semantics** — shape passes
  (16/16 fields, 20/20 glossary) but the claim ledger lacks an uncertainty
  dimension and bilateral acknowledgment is pending; zero unfiled bleed.

## Landed changes

Commit `44070b4` — LOG.md round-12 entry. Integrator acts: 61-command coverage
completion; 18+43 ledger rows normalized; defects + adjacency ledgers
consolidated; routed.md status conflicts harmonized; filed receipts r8/r9
restored.

## Before → after measurements

`python3 reports/round-12/run-validation.py` → exit 0 (C/O/A PASS). Verdicts:
`SCORECARD.md` §"Axes — round 12" — calibration/operability/adjacency
improved; depth/coverage/freshness unchanged (freshness axis-moves remain
paused pending the operator's threshold ruling).

## SHONEN

- [~] SKILL.md decision tables with cited sources — unchanged (author-asserted)
- [~] End-to-end domain task executed and logged — cross-round audit executed (author-asserted)
- [~] Instructions executable without oral context — recount/defect ledgers re-runnable (author-asserted)
- [~] No cross-domain bleed — zero unfiled bleed; handoff reject filed (author-asserted)

Promotion review not requested; boxes remain `[~]`.
