# kumitate — round 96 report (hyaku run 15, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kumitate-shokunin`, branch `master`. Base `bba139792d92604df1d83f2df3b74d53b9ed67a0`
(round-95 closure spot-check tip). L1 `KumitateR96` (holds the §3 planner seat; the validator refuses `planner`).
Not a fresh-start round (Amendment-46 fresh start was r92; r92–r95 admitted). No `lane-dead-no-report kumitate round=96`
line in the watchdog log: nothing inherited.

## Work performed

Declared claims (one): **C1 — operability** (lowest non-retired axis; integer 9, terminal under `f_O`):
`scripts/round-gate.mjs` declares upstream pins only from `corpus/SOURCES.md` rows **inside the `## Registry` section as
the fleet census reads it** (`sources-census.sh` `row_pass`), and lists every outside row-shaped line in the
always-present `citations.outsideRows` (+ one non-finding text line `SOURCES_ROWS_OUTSIDE`). Sourced on S275
(CommonMark 0.31.2), opened this round. Source of the claim: round-95 pre-registration item (1) / K95CriticB.

- Pre-freeze adoption of the round-95 spot-check into the README map (M94-1 ordering): lane commit `8191f90e`
  (`.ufo/waves/round-96/close-l1/adopt-r95-spotcheck.txt`: `README_MAP: DRIFT … uncovered:lessons/round-95-verifier-spotcheck.md`
  → `SPOTCHECK_ADOPT: ADOPTED … wrote=both`, `README_MAP: CLEAN files=246`).
- Freeze `617e80cd8b01efb5748d729dbdcac95734bc461d`: plan (`.ufo/waves/round-96/plan.md`), frozen counter
  `probe/probe96-c1.mjs` with a 22-clause section battery whose expected lists are re-derived from the census itself on
  every run, generator `probe/make-controls96.py`, **20 pre-data controls** (`controls/*.txt`: positive HELD, do-nothing
  + 18 single-clause violations UNMET). The counter's first draft let `ctl-defaultin` reach HELD; repaired before the
  freeze and disclosed (`controls/prefreeze-run1/ctl-defaultin.txt` HELD vs `controls/ctl-defaultin.txt` UNMET).
- Wave w1 (validated dispatch `f5873bff`): candidate `K96ExecTool/round-gate.mjs` (READY `9975be54…`, `score1.txt`/`score2.txt`
  HELD, `arm-teeth.txt` 18/18); hand review `w1/K96Reviewer.md` (no blocker); harm battery `K96ExecHarm/battery-diff.txt`
  (only expected pin drift + the added key); counter attack `K96CriticA/constructions.md` (8 of 14 new wrong gates
  reach HELD); framing `w1/K96CriticB.md` (sound mechanism, narrow live surface); differential `K96CriticC/H96.md`
  (H96 survives: 75/75 kumitate registry revisions, 21/21 lanes, 300/300 seeded mutations agree with census E12);
  mutation `K96Mutation/mutants.md` (25 mutants, 24 killed, survivor `b20-spaceclass`); parser parity
  `w1/K96Connector.md` (census gawk vs census bash vs lane `sources-check.mjs`); fleet survey `w1/K96Scout.md`;
  source row `K96ScribeSources/quotes.md`; knowledge draft + Q90 command `K96ScribeLesson/`.
- Integration M `09de67917b5b7731aa06ae019c7e9b94359981c9`: READY bytes + L1 arms (xxvi)/(xxvii) for K96CriticA's HELD
  constructions (`close-l1/integration-arms.js`, `close-l1/integration-diff-ready-vs-M.txt`); selftest 89 → 94;
  `pin.round-gate` aba737dc… → edaa115f…; re-mutation of the shipped bytes **30/31** killed + `b20-spaceclass` killed
  (`close-l1/integration-remut.txt`).
- Frontier: S275 row + search-log entry, knowledge `corpus/knowledge/round-gate-registry-section.md` (verified-at M),
  QUALITY Q90, SKILL `round-gate` row (`outsideRows` decision), lesson `corpus/lessons/round-96.md` — lane commit `6777f306`.
- Routed r95 spot-check items: (1) lesson URL — this lesson carries it and Q90 checks it (`close-l1/q90-round-96.txt`
  `LESSON_URLS: CLEAN new=1`); (2) battery per revision — `close/battery-M.txt` and `close/battery-final.txt` state each
  revision's verdict exactly (see below); (3) `round-gate-registry-shape.md` `verified-at` re-pointed to `a59fbedc`
  (the shipped r95 bytes) in `6777f306`; (4) carried items routed to r97; (5) adopted before the freeze (`8191f90e`).

## Landed changes

| LOG.md entry | lane commit | what |
|---|---|---|
| Round 96 (LOG.md, section + one-line record) | `8191f90e2e254a5a6130b2c8e96ab4938fc77ca8` | r95 spot-check adopted into README map before freeze |
| same | `617e80cd8b01efb5748d729dbdcac95734bc461d` | freeze: plan, counter, generator, 20 controls (+ pre-freeze run), open receipts |
| same | `f5873bff899d2ac271e05fde90252a19660bd664` | wave spec + validated dispatch |
| same | `09de67917b5b7731aa06ae019c7e9b94359981c9` | M: `scripts/round-gate.mjs` R96 + arms, `pin.round-gate`, counter receipts, re-mutation |
| same | `6777f3063e9781b682344070d229928934addf2e` | lesson, knowledge, S275, Q90, SKILL, README map, LOG, SCORECARD move-log + disposition + r97 pre-registration |
| same | `416009977b060b1b5ad93d8141ff7ef23b28b536` | wave w1 evidence (11 seat dirs, trailers, results, ready markers) |
| same | `4a57390d6f71a603c25588cffe9762c403b98c9d` | proxy stanza re-declared; battery at M |
| same | `b0084b2042ec91436d85b07cdd886b6d88541c4b` | battery-final, census-after, selftest at M, Q88 PASS — lane tip; `git ls-remote origin refs/heads/master` → `b0084b2042ec91436d85b07cdd886b6d88541c4b` |

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 | `node .ufo/waves/round-96/probe/probe96-c1.mjs --tool <(git show <rev>:scripts/round-gate.mjs) --work <scratch> --freeze 617e80cd8b01efb5748d729dbdcac95734bc461d` | BASE `aba737dc…`: `C96_C1: UNMET a=0/1 b=0/1 c=0/1 d=0/1 e=0/79 f=1/1` (`controls/ctl-nothing.txt`; fixture A BASE declares 15 tokens, 8 of them from outside rows) | `C96_C1: HELD a=1/1 b=1/1 c=1/1 d=1/1 e=79/79 f=1/1 tool_sha256=edaa115f…` twice (`close/probe1.txt`, `close/probe2.txt`) | `09de67917b5b7731aa06ae019c7e9b94359981c9` |

Kill rules: K1 not fired (HELD). K2: shipped selftest kills all 18 violating control shapes (`close-l1/integration-remut.txt`).
K3, per revision: base (`open/battery-before.txt`) `PROXY: DRIFT` on C2/C2_total bookkeeping only, all else CLEAN; **at M**
(`close/battery-M.txt`) `PROXY: DRIFT` on A_wave/C2/C2_total bookkeeping only (pin matches), readme-map, sources-check,
counter-pins, spotcheck-adopt, `round-gate --tracked`, `--round 95`, census all CLEAN/ok exit 0; **at final**
(`close/battery-final.txt`) `PROXY: MATCH` (also `--strict`) and every tool CLEAN exit 0. K4: plan/probe/controls/open
unchanged since the freeze. Caveat M96-2: 8 counter constructions reach HELD; 7 die on the shipped selftest,
`hardcode-fixtures` is keyed on the counter's fixed fixture (disclosed limit).

Axes: operability 9 → 9 (terminal; the move is the instrument), every coverage row 10 → 10 (`PROXY: MATCH`). No axis harmed.

## Sources & frontier

SOURCES rows before → after: **212 → 213** (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md`). Added by tier: A +1 (S275,
CommonMark spec 0.31.2, https://spec.commonmark.org/0.31.2/, `mined`, recheck `on-release`, used-by
`corpus/knowledge/round-gate-registry-section.md`). Rows touched old→new: none. Frontier: the claim cites S275 (opened
this round by K96ScribeSources, re-opened by the L1: `close-l1/l1-open-commonmark.txt`, HTTP 200, sha256 `c85f56cc…`).
Census, round start (`open/census-before.txt`) and end (`close/census-after.txt`):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate
start: 8 × W04 (pre-existing) … kumitate ok …/corpus/SOURCES.md   exit=0
end:   8 × W04 (pre-existing) … kumitate ok …/corpus/SOURCES.md   exit=0
```

Mistake mined: M96-1 (lesson rows admitted without URLs; captured-by none; fix Q90, shown able to fail on r95/r94 and pass
on r34–r36/r46) and M96-2 (counter clause coverage, third recurrence). Assimilation: none (no `merge/kumitate/` theme fits a
gate section rule). considerthese: not mined this round (latest `considerthese/2026-11-06.md`; no proposal fits C1).

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | improved | new knowledge entry `round-gate-registry-section.md` citing mined S275, README row; SOURCES 212 → 213 |
| quality | improved | gate declares only from census-registry rows (20 controls, counter HELD ×2, selftest 89 → 94, re-mutation 30/31 + b20); r95 spot-check items 1–3 answered; Q90 shown able to fail |
| discernment | improved | admits/rejects recorded in the lesson `## Gate` (CommonMark reader rejected, "counter pins clauses" rejected with 8 receipts, `sources-check` reader rejected); census self-disagreement found and routed |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:610` round-gate row now carries the `outsideRows` decision (lane commit `6777f306`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 96` (gate, frozen counter and fleet census exercised on a 22-clause registry battery).
- [~] Instructions executable by an agent without oral context — `node scripts/round-gate.mjs --selftest` → `ROUND_GATE_SELFTEST: 94/94 pass`, exit 0 (`.ufo/waves/round-96/close-l1/selftest-M.txt`; `K96ExecTool/selftest.txt` for the READY bytes).
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched this round.

## Round shape, seats, extras

- Shape: ONE v1 wave `w1`, **11 seats** (executor ×2, scribe ×2, scout, connector, reviewer, critic ×3,
  mutation-tester); attack 5/11 = 45 %; no residual call; round total 11. Dead seats: 0 (`w1-results.json`, 11 results).
  The planned `labrat` item was refused by the validator (`unknown_role`) and rode a critic seat (K96CriticC); the plan's
  frozen text still says labrat (not edited after the freeze). K96ExecTool wrote READY late (after the other seats had
  attacked its on-disk bytes, which were identical: sha256 `9975be54…` throughout).
- L0 question filed: `kumitate | round-96 |` fleet census section readers disagree on `\r` (appended to `.ufo/l0-questions.md`).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep: none from this round (`close-l1/misroot-sweep.txt`; `trail-ids.txt` at the fleet root predates the round).
- Tool installs: none.
