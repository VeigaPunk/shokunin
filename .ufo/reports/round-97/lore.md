# lore round 97 — fleet report

**L1 ruling: ADMITTED** (V35 all-axis adjudicator; six conditions
discharged). Lane: `lore-shokunin`. Lane HEAD at report time: `9a3d648`
(see lane repo). Baseline `f3e09f9`. Single-wave 64-seat swarm on
`opencode-go/deepseek-v4.1-flash` (dispatch `tool_X1OZlGbgZtVEcklt3o9IBuUR`,
returned `completed: 64`; 64/64 reports, three late landings; receipt
`.ufo/waves/round-97/receipt.json`; served-backend echo unknown).

## Work performed

Declared claims (LOG.md r97 declaration): **C1/calibration** — pin the
carried calibration residuals (`dual_pointer` persisted case; strict
loader). **C2/coverage** — close the carried `dependency_freeze` hazards
(scope guard, path binding, named DIGEST-MISMATCH, 16-case self-test,
guarded re-freeze of the r96 repair). **C3/depth** —
`corpus/fixtures/r97-crossing-acknowledgment/` (third beat, unresolved
preserved) plus the byte-minimal r96 map cosmetic repair.

- C1 verified first-hand: 25/25 pinned with the dual_pointer case;
  dropped-pin contract variants fail closed (the r96 23/24 tolerance
  demonstrated on the old tool as the closed pre-state); pin load-bearing
  under neutralization; battery byte-stable — V01–V05, V31, V44.
- C2 verified: SCOPE-REFUSED with no write; PATH-MISMATCH on a
  byte-identical foreign copy (real path clean); DIGEST-MISMATCH names the
  file; 16/16 self-test; revision-only re-freeze reproducible through the
  guarded path; chain 4/4 — V06–V12, V30, V45, V48, V55.
- C3 verified: 5/1/5→5/1/6, 17/17 obligations, 16 inherited rows
  unchanged, CLEAN, census 171 with zero inherited changes; two
  constructibility probes failed to build any resolution/blame reading;
  the r96 repair is exactly two lines with both r96 receipts identical —
  V13–V20, V29, V43, V50–V54.
- Two seat FAILs confirmed and recorded (not re-rolled): V12 (the freeze
  pin payload covers the JSON tables only — the map digest is not pinned;
  discharged by append-only erratum) and V46 (the r97 tick-13 edge is
  unfrozen — r97 outside the declared pin set; r98 candidate).

## Landed changes

- `9d25df9` + `9a3d648` — the admitted wave frozen + closure docs: tool
  `86b52949…`, contracts `2142b991…` / `27273be2…` (r96 pin revision
  refreshed), tools README + Round-97 supersession, r96 map repair
  `e851f068…`, r97 fixture (10 files), knowledge note `5e3b4225…`,
  append-only LOG errata/closure, fixtures README Round-97 + census,
  corpus README bullets, SKILL.md registry rows, C9 row 6, `.gitignore`
  `*-self-test-*/`, 64 seat reports + receipt; one embedded scratch clone
  (V37 `mirror-freeze`) dropped from the wave tree in `9a3d648`.

## Before → after measurements

- C1 (at `9d25df9`): contract carries 25 cases; `--self-test` → `SELF-TEST
  CASES 25/25 pinned` PASS exit 0; dropped-pin variants → `FINDING
  self_test_contract …` exit 2; r96 tool + 24-case contract → `23/24
  pinned` PASS (the closed pre-state).
- C2 (at `9d25df9`): foreign-path verify → `FINDING PATH-MISMATCH …` exit
  2; delivered chain → 4/4 `RESULT PASS` exit 0; `--self-test` 16/16.
- C3 (at `9d25df9`): counts 5/1/5 (r96) → 5/1/6 (r97), sources 5→6;
  `check_bible` CLEAN exit 0; `map_obligations` r97 `raw=17 mapped=17`,
  TOTAL-ROWS 19/19; census 171 dirs (37 clean / 134 negative / 421 lines),
  +1 clean, zero inherited changes.

## SHONEN

- `[~]` SKILL.md decision tables — both tool rows current (25/16 cases,
  guards, bounds); lane assertion.
- `[~]` end-to-end task — r97 census + probes in this round's LOG entry.
- `[~]` executable instructions — freeze hazards and scratch pattern
  recorded in the registry rows and `.gitignore`.
- `[~]` no cross-domain bleed — V28/V34; zero parent-tree strays.
- No `[x]` (same-lane rule). No promotion.

## Axis and learning verdicts

calibration improved (bounded); depth improved (bounded); coverage improved
(bounded); operability improved (bounded); freshness unchanged; adjacency
unchanged (not harmed). No axis harmed; no trade netted. Process records:
endgame mutual-poll class recurred and was characterized (all-reports polls
must subtract SELF); `/tmp` inode exhaustion recurred and cleared; one
embedded scratch clone dropped at closure; kotodama-shokunin's concurrent
parent-root activity attributed by path ownership (untouched by this lane).
Carried to r98: pin r97; r95 map carried sentence; stale note pins; BR-01
prose half. No push, no merge, no saturation line. Regimen: r98 is the last
64-seat deepseek-flash round; then r99 (128-seat grok-4.7-fast xhigh) and
r100 (32-seat sol-max).
