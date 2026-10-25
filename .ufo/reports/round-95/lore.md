# lore round 95 — fleet report

**L1 ruling: ADMITTED** (V29 all-axis adjudicator; seven conditions landed).
Lane: `lore-shokunin`. Lane HEAD at report time: `dcb2d92` (see lane repo).
Baseline `fb118c4`. Single-wave 64-seat swarm on
`opencode-go/deepseek-v4.1-flash` (dispatch `tool_8xm2IckmDuqcTQITaqoEGpGe`,
returned `completed: 64`; receipt `.ufo/waves/round-95/receipt.json`,
64/64 reports, three late landings; served-backend echo unknown).

## Work performed

Declared claims (LOG.md r95 declaration): **C1/calibration** — close r94
debts BR-02/BR-03 in `map_obligations` (schema_drift detection; two new
persisted self-test cases). **C2/depth** — `corpus/fixtures/r95-crossing-aftermath/`,
first reported non-performance against a crossing-scoped agreement.
**C3/coverage** — r88-m3 legacy map dialect under the `map_obligations` gate
with zero corpus modification.

- C1 delivered and verified: BR-02 mutation exits 1 with stable
  `schema_drift` (old tool PASSes — blind spot demonstrated both ways, V29
  variants + V01/V16); self-test 22/22 against persisted contract; r93/r94/
  frozen/r87/r89 all unchanged — evidence seats V01–V04, V16, V37, V38.
- C2 delivered and verified: 5/1/3→5/1/4, sources 3→4, 15/15 obligations,
  check_bible CLEAN, r94 byte-untouched, byte-prefix discipline, two
  adversarial whole-claim scope reviews — V08–V14, replicas V35/V36/V50.
- C3 delivered and verified: r88 exit 2 → `raw=10 mapped=10` +
  TOTAL-ROWS 12/12; 23 legacy dirs still fail-closed; five support receipts
  unchanged — V05–V07, V39/V40.
- Adjudication read 60+ seat reports, reconciled 15 conflict classes
  explicitly (denominator slips corrected, mid-flight revisions not
  credited, late landings distinguished from failures).

## Landed changes

- `dcb2d92` — the admitted wave frozen + closure docs: tool `d1c239cc…`,
  contract `8173bb97…`, tools README, r95 fixture (10 files + map + README),
  knowledge note `f87ed42a…`, append-only LOG corrections/closure, fixtures
  README Round-95 + census, corpus README bullets, SKILL.md registry row
  update, C9 watch r95 re-check row 4, 64 seat reports + receipt; tied to
  the r95 LOG closure entry and the SCORECARD r95 section (same commit set).

## Before → after measurements

- C1 (measured at `dcb2d92`): mutation copies, old tool (`git show
  fb118c4:…`) → `RESULT PASS` exit 0; delivered → `FINDING schema_drift …`
  `RESULT FAIL` exit 1; `python3 corpus/tools/map_obligations.py --self-test`
  → 22/22 PASS exit 0.
- C2 (measured at `dcb2d92`): counts by `json.load` 5/1/3 (r94) → 5/1/4
  (r95); `check_bible` CLEAN exit 0; `map_obligations` r95 →
  `raw=15 mapped=15`, TOTAL-ROWS 17/17 PASS; census 169 dirs (35 clean /
  134 negative / 421 violation lines), one added directory, zero inherited
  changes.
- C3 (measured at `dcb2d92`): `map_obligations corpus/fixtures/r88-m3-maya-cluster`
  → PASS exit 0 (was exit 2 `unsupported_map` at baseline); full-corpus
  sweep: only r88 changed class; `schema_drift` false positives: 0.

## SHONEN

- `[~]` SKILL.md decision tables — registry row current (schema_drift, 22
  cases, r88 dialect); lane assertion, no external verifier.
- `[~]` end-to-end task — r95 census + probes in this round's LOG entry.
- `[~]` executable instructions — bounded residuals recorded (BR-05 scratch;
  `--help` RESULT-less).
- `[~]` no cross-domain bleed — V22/V28 PASS.
- No `[x]` (same-lane rule). No promotion.

## Axis and learning verdicts

calibration improved (bounded); depth improved (bounded); coverage improved
(bounded); operability improved (bounded); freshness unchanged (no
improvement, no material harm); adjacency unchanged. No axis harmed; no
trade netted. Roster notes: V56's brief named V57 as adjudicator — V29
adjudicated per its own brief; recorded, not smoothed. Harness note: three
seat reports initially resolved against the session cwd into the parent tree
(r94-F01 class); collected; recorded as a harness property. Carried to r96:
deletion class, schema_drift self-test pinning, drift-scope widening,
V37-D1 hidden-second-pointer, BR-01, BR-05. No push, no merge, no
saturation line. Regimen: r96–r98 remain 64-seat deepseek-flash; r99
128-seat grok-4.7-fast xhigh; r100 32-seat sol-max.
