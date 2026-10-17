# lore round 96 — fleet report

**L1 ruling: ADMITTED** (V38 all-axis adjudicator; eight conditions
discharged). Lane: `lore-shokunin`. Lane HEAD at report time: `f3e09f9`
(see lane repo). Baseline `dcb2d92`. Single-wave 64-seat swarm on
`opencode-go/deepseek-v4.1-flash` (dispatch `tool_u9BH6dLzBlljBGPW0Eh74iZl`,
returned `completed: 64`; 64/64 reports; receipt
`.ufo/waves/round-96/receipt.json`; served-backend echo unknown).

## Work performed

Declared claims (LOG.md r96 declaration): **C1/calibration** —
`map_obligations` hardening: gating `inventory_mismatch` (deletion class),
persisted self-test pinning (22→24), V37-D1 `dual_pointer` close.
**C2/depth** — `corpus/fixtures/r96-crossing-response/`, second account,
same occasion, unresolved. **C3/coverage** — new gate
`dependency_freeze.py` closing BR-01's JSON-edge half.

- C1 verified first-hand by the adjudicator: deletion mutation old-tool
  exit 0 vs delivered exit 1 `inventory_mismatch`; all three V37-D1 forms
  exit 1 `dual_pointer` with false-positive controls; 24/24 pins
  load-bearing three ways; full non-regression battery green — seats
  V01–V07, V34/V55.
- C2 verified: 5/1/5, 16/16 obligations, 15 inherited rows diff-free
  outside the namespace column, CLEAN, census 170 with zero inherited
  changes, no contradiction constructible — V08–V15, replicas V45/V46/
  V53/V54, V56 crosscheck.
- C3 verified: chain 4/4 clean; BR-01 mutation exits 1
  `REDUCTION-DETECTED` (previously invisible to every gate); addition and
  endpoint mutations exit 1; exit-2 surface complete; 14/14 self-test;
  zero corpus modification — V16–V23, V48/V49.
- V23's FAIL confirmed and discharged at closure: a verifier's `--freeze`
  probe wrote a foreign `c3red` pin into the producer-owned freeze
  contract (byte-ownership breach, self-disclosed); pin removed; self-test
  14/14 and chain 4/4 re-run green on the corrected contract.

## Landed changes

- `f3e09f9` — the admitted wave frozen + closure docs: tool `2b0ba815…`,
  contracts `97b76bb8…` / `c65ac3bd…` (post-C-1), freeze tool `a3b57978…`,
  tools README, r96 fixture (10 files), knowledge note `6db32ca2…`,
  append-only LOG errata/closure, fixtures README Round-96 + census,
  corpus README bullets, SKILL.md registry rows, C9 watch r96 re-check
  row 5, 64 seat reports + receipt; tied to the r96 LOG closure entry and
  SCORECARD section.

## Before → after measurements

- C1 (at `f3e09f9`): deletion-class copies — old tool
  (`git show dcb2d92:…`) `RESULT PASS` exit 0; delivered
  `FINDING inventory_mismatch … RESULT FAIL` exit 1; `--self-test` →
  `SELF-TEST CASES 24/24 pinned`, PASS exit 0.
- C2 (at `f3e09f9`): `json.load` counts 5/1/4 (r95) → 5/1/5 (r96),
  sources 4→5; `check_bible` CLEAN exit 0; `map_obligations` r96
  `raw=16 mapped=16`, TOTAL-ROWS 18/18; census 170 dirs (36 clean / 134
  negative / 421 lines), +1 clean, zero inherited changes.
- C3 (at `f3e09f9`): `dependency_freeze` chain 4/4 exit 0; scratch
  reduction → `REDUCTION-DETECTED` exit 1; addition → `ADDITION-DETECTED`;
  endpoint flip → `ENDPOINT-CHANGE`; `--self-test` 14/14.

## SHONEN

- `[~]` SKILL.md decision tables — six registry gates now; lane assertion.
- `[~]` end-to-end task — r96 census + probes in this round's LOG entry.
- `[~]` executable instructions — freeze hazards and map bounds recorded
  in the registry rows.
- `[~]` no cross-domain bleed — V31 + L1 checks; no parent-tree strays.
- No `[x]` (same-lane rule). No promotion.

## Axis and learning verdicts

calibration improved (bounded); depth improved (bounded); coverage improved
(bounded); operability improved (bounded); freshness unchanged; adjacency
unchanged (not harmed). No axis harmed; no trade netted. Process records:
mutual poll-wait liveness class (V43/V58, self-recorded); verifier
byte-ownership breach (V41, self-disclosed, discharged); host `/tmp` inode
exhaustion as a host condition; V37's unfinished adjacency battery — verdict
rests on V31 + L1. Carried to r97: freeze scope guard / path binding,
BR-01 prose half, `dual_pointer` pin, droppable-pin loader, cosmetic r96 map
fixes, BR-05. No push, no merge, no saturation line. Regimen: r97–r98
64-seat deepseek-flash; r99 128-seat grok-4.7-fast xhigh; r100 32-seat
sol-max.
