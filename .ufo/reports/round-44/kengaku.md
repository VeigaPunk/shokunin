# kengaku — round 44 report (hyaku run 9, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read `0cb2e22598a39b7cd0bf5582d86d62492b57fa12`;
frozen claims `plans/round-44-claims.md` (freeze `5f16ed04b04a80a17a5a1a060c12093d9a152a64`); first recorded probe run
`45dc0bc81e42e02ecd272712086c372c8844b108`; claim landing `2a263e5a56ef6d48d06805e1ccd106de5de9ba66`; final lane hash
`7857ce551283a49f6eec4a4065982061f65cc7dc` (`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR44`; the L1 holds the canonical
planner seat (the validator rejects `planner`; the round-45 data walk rode scout `R44PlanNext`). Earlier attempts: none
(`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=44` line; `.ufo/waves/round-44/` absent at start).

## Work performed

Declared claims (2), frozen with red controls before any `plans/battery44` fixture and before the first recorded probe run:

- **C1 — calibration (8):** five behaviours `plans/anchor_digest_check.py` and `plans/order_check.py` (both unedited)
  advertise that no landed battery demonstrates — U5 (`digest-short` label), U6 (`digest-long` label), U7 (a token
  resolving to twin captures is not a defect), U9 (lessons read from the working tree), U14c (unparseable claims name is
  exit 2), priced by round-43 `R43PlanNext` §B. U3 was dropped before the freeze because battery43 already kills it
  (`.ufo/waves/round-44/claims/control-c1-standing-batteries-six-mutant-draft.txt`). Counter `plans/round44_c1_verify.py`
  = round-43 counter + fence repairs **F1–F6** (`R43SentinelCounter`). `TOTAL = 5`, `FLOORS = {anchor: 4, order: 1}`.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break; capped by L0 `kengaku | round-33`):** the
  pinned Terminal-Bench 2.0 `feal-linear-cryptanalysis` grader (round-43 histogram class F1, constant-compare, 0 of 14
  read) admitted as `corpus/knowledge/tb2-feal-linear-cryptanalysis-grader.md` with a 14-case bubblewrap probe
  (`plans/feal_linear_probe.py`), rows S138–S146 (tier A); counter `plans/round44_c2_verify.py` = round-43 V1–V10
  re-pointed + **V11 held-out predictor** (closure R5: the entry's `predict(text)` must agree with the executed captured
  grader on 48 generated states; no verdict stored in the counter).

Work items:

- Protocol load: round prompt, `skill://godspeed`, SCORECARD `### Planned (round 44)`, round-43 report and closure
  spot-check (`corpus/lessons/round-43-verifier-spotcheck.md` §5 R1–R5), `R43PlanNext`, `R43SentinelCounter`.
- Captures fetched by the L1 at pin `2fd12b88` 2026-10-26 20:10:09 -03 (eleven files + `SHA256SUMS`,
  `corpus/evidence/round44/tb2-feal-linear-cryptanalysis/`).
- Freeze `5f16ed04`: claims, both counters, probe, spec `plans/pkg-spec-r44.json`, dry table (`cases=14 predicted_pass=8
  predicted_fail=6`), witness `claims/witness/w_u.py`, hostile modules f1–f6, controls (`.ufo/waves/round-44/claims/`):
  witness run 5/5 killed `value=differs`; nothing `killed=0 survived=5` exit 1; standing batteries 42+43 (71 fixtures)
  `killed=0 survived=5`; witness-as-battery `PREDICATE C1 pass`; no-mutants, span-forced, value-forced, tool-edited all
  fail; U7 mislabel `SURVIVED exhibits=0>1,rc-mirror`; f1–f6 each admitted (or hung, f4 `exit=124`) under the round-43
  counter and refused by SETUP here; C2 nothing `checks=11 defects=8`; V11 predictor control: always-True / token-set /
  exact-lines DEFECT, substring ok (`CONTROL-C2-PREDICTOR red-as-required`); stage-check 14/14; census-before exit 0.
  Round-43 residue (closure R3) committed in the same commit.
- First recorded probe run `45dc0bc8`: `cases=14 observed_pass=8 observed_fail=6 mismatches=0`, `regrade cases=14
  differ=0`; `order_check` → `ORDER RESULT PASS`.
- Wave (v2, spec/dispatch `5e3d3aa0`, 68 seats, reports `.ufo/waves/round-44/wave/`): ten executors wrote
  `plans/battery44/` (10 modules, 33 fixtures, two independent modules per mutant); C2 package from `R44PkgEntry`
  (integration patch, `checks=11 defects=0` in its clone), `R44PkgRows`, `R44PkgProse`; independent checks: real pytest
  14/14 (`R44PytestParity`), re-derivation 14/14 + 3 (`R44CritIndep`), byte-equal re-run 3/3 (`R44LabratRerun`), refetch
  11/11 (`R44ScoutRefetch`), C1 controls reproduce 14/14 (`R44LabratControls`), dishonest-battery vectors 7/7 blocked
  (`R44CritC1Counter`), site-stable 30 runs, mutant rows 5/5, equivalent 0. Limits found: fence bypasses 3/6
  (`R44SentinelFences`: `.git/commondir` HIGH, second-config include, refuse-to-describe), `lane_breach` reads an include
  outside d (`R44LabratLaneInclude`), V11 memorizable 4/7 (`R44CritV11`), V11 mutants 3/6, V9/V10 guards 6/13; fence-code mutants caught 15/18 (`R44MutC1Fences`), round-43 C1 guard set 6/15 (`R44MutC1Guards`); no-harm baseline at the receipt commit 40/44 green, the 4 red expected or carried (`R44ExecNoHarm`).
- Residual call (spec `256cc66a`, 8 seats, `.ufo/waves/round-44/residual/`): battery44 modules honest 4/4, 4/4, 2/2;
  0 single-module flips, 6 dishonest substitutes admitted via the sibling module (intent limit, named at freeze);
  entry quotes 36/36, findings wrong 0; overclaims 0; rows 8/9 at `2a263e5a` (S140 scope phrase — fixed at `02287eed`);
  re-measure pass/pass stable.
- Closure R1–R5 landed `02287eed`: round-43 flip lines corrected + S147/S148 tier B + entry errata (R1, `R44FlipLines`);
  S134/S132 span errata (R2); `plans/gate_flip_check.py` extended to read flip verdicts against entry citations, red
  on the round-43 lesson before the lines and green after (`integrate/flip-verdict-red-green.txt`, selftest 27/27);
  QUALITY Q36–Q38; README lessons index 33 → 63 rows (= 63 files) + evidence sections; SKILL registry rows + section.
- considerthese `2026-10-26.md` proposal 1 (routed burn-down): 15 ledger field changes, `routed_open` 39 → 24.
- Landing measurement `integrate/measure-final.txt` (clean clone of `02287eed`): C1 pass, C2 pass, no-harm diff below;
  tip re-measure `integrate/measure-tip.txt` (`c2ff2114`): C1 pass, C2 pass, flip checks `red=0`, anchor `defects=0`,
  census ok, `round_close --round 44` PASS.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists nothing beside
  orchestrator `.scratch/`/`.ufo/state/` — misroot 0.
- Scratch `/fast/scratch/hyaku/kengaku-r44` removed by the L1 after landing.

Round shape: **one v2 wave of 68 seats** — executor 22, scribe 11, critic 9, scout 7, mutation-tester 5, reviewer 5,
connector 4, sentinel 2, simplifier 2, revenger 1 (m_flash-routed 38/68; attack 19/68 = 28 %; critic counted as m_kfc per
the orchestrator's 20:07 note) — **plus one residual call of 8** (reviewer 5, critic 3). Round total **76** (band 64–128).
Dead seats: 0 (68 + 8 results). One seat, `R44ScoutMisroot`, returned its verdict (`misroot-0-host-writes-0-sentinel-present`) only in `wave-results.json` and left no report file — the round-43 D3 class recurred once; recorded in `corpus/lessons/round-44.md` §Mistakes; the L1's own sweep stands in. Routing from the host table; no `model` passed. `labrat`/`distiller` are not validator swarm roles,
so those items rode executor/simplifier seats. Report filed after WAVE-DONE for both dispatches.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none by the L1. pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `5f16ed04` | freeze: claims, C1/C2 counters, probe, spec, dry table, captures, controls, witness, hostile f1–f6; round-43 residue | round 44 entry ¶1 |
| `45dc0bc8` | first recorded probe receipt | C2 bullet |
| `5e3d3aa0` | v2 wave spec + validated dispatch | round shape bullet |
| `2a263e5a` | battery44 + feal-linear package (entry, S138–S146, README, PROVINCE) | C1, C2 bullets |
| `256cc66a` | residual dispatch | round shape bullet |
| `02287eed` | closure R1/R2 (flip lines, errata, S147/S148, flip-verdict check), Q36–Q38, README index, SKILL, routed closures, S140 fix | Closure, considerthese bullets |
| `c2ff2114` | lesson, SCORECARD/LOG round-44 sections, landing measurement, census, residual reports | entry |
| `7857ce55` | wave reports + results, tip re-measure (`c2ff2114`; no claim surface changed after it), lesson close notes | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round44_c1_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c1-nothing.txt`; `integrate/measure-baseline.txt` at `5e3d3aa0`): `BATTERY fixtures=0`, `MUTANTS
    total=5 killed=0 survived=5 invalid=0 null_detected=0 unattributed=0`, `PREDICATE C1 fail`, exit 1. Standing batteries
    42+43: `killed=0 survived=5`.
  - After, at `02287eed` (`measure-final.txt`) and `c2ff2114` (`measure-tip.txt`): `PINS total=2 mismatched=0`, `BATTERY
    fixtures=33 wrong=0 tampered=0 sidechannel=0`, `MUTANTS total=5 killed=5 survived=0 invalid=0 null_detected=0
    unattributed=0`, `MUTANTS-BY-TOOL anchor=4/4 order=1/1`, `PINS-AFTER mismatched=0`, `PREDICATE C1 pass`, exit 0.
  - Verdict: **frozen predicate met**; mismatch count 5 → 0. Score **8 → 8 held**.
- **C2 (coverage)** — `python3 plans/round44_c2_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=11 defects=8`, exit 1; at `5e3d3aa0` `defects=7`.
  - After, at `02287eed` and `c2ff2114`: `checks=11 defects=0` (V11 `states=48 grader_pass=24 grader_fail=24
    disagree=0`), `PREDICATE C2 pass`, exit 0.
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap). V11's fixed-seed sample is memorizable
    (`R44CritV11`), routed.
- **No harm** (`measure-baseline.txt` vs `measure-final.txt`, verdict lines): only the round-44 counters (red → green),
  the anchor check `rows=130 tokens=36` → `rows=141 tokens=47` (`defects=0` both), `routed_open=39` → `24`, two new
  `FLIP-CITE … red=0` lines from the extended flip check, and registry/knowledge counts 130/50 → 141/51 differ; rounds
  36–43 counters, ledger-tip, tip receipts, five probes byte-equal, census exit 0, frozen digests r39–r44 OK,
  `round_close.py --round 41/42/43/44` PASS.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 130 → 141. Tier A +9 (S138
  `tests/test_outputs.py`, S139 `instruction.md`, S140 `environment/task-deps/gen.py`, S141 `environment/Dockerfile`,
  S142 `tests/test.sh`, S143 `README.md`, S144 `solution/solve.sh`, S145 `environment/task-deps/decrypt.c`, S146
  `task.toml`; feal-linear-cryptanalysis @ `2fd12b88`, opened by the L1 20:10 -03, re-fetched cmp-identical 20:33 by two
  seats); tier B +2 (S147 `task.toml`, S148 `solution/solve.sh` of feal-differential — round-43 flips that fired, closure
  R1). All `mined`. Rows touched old→new: S140 scope cell `sha256 chain` → `SHA-256 hash chain` (same-round, pre-report
  fix of a hash-shaped phrase the anchor check reads as a token; disclosed in the lesson as a Q34 deviation).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before
  exit 0, `kengaku ok`, 15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok`, 15 W04 (`integrate/census-final.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a tenth task (10 of 89); the F1 constant-compare class
  enters the executed sample (agent-written text file, substring membership of 100 embedded constants). Knowledge files
  50 → 51.
- Sourced claim: C2 (S138–S146 opened this round).
- Mined mistake (`corpus/lessons/round-44.md` §Mistakes, 9 rows): round-43 false `not fired` flip → flip-verdict check
  red on the round-43 lesson, green after the corrected lines (Q36, shown able to fail); also the round-43 38-seat close,
  a reportless seat, a mutant the standing batteries already kill (Q37), a dropping sweep, S140's hash-shaped phrase,
  frozen wording contradicted by captures, a memorizable V11 sample, a fence repair that reads an include.
- Assimilation: none — `merge/kengaku/` unchanged since 2026-10-24 (`R44MergeRescreen`: `reg-ids=130 staged-ids=175
  collisions=54`, guard proven on an indented `  | S002 |` fixture; renumber map: none). Quarantine slice 2 rows, both
  quotes located (`R44Quarantine`). considerthese: `2026-10-26.md` proposal 1 (routed burn-down) landed as 15 ledger
  field changes and a burn-down line (`R44RoutedObserve`).

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (tenth TB2 grader; first of the F1 class) citing nine
  tier-A rows opened this round, plus two tier-B rows; three capability rows demonstrated (`held-out-predictor-leg`,
  `fenced-fixture-discovery`, `flip-verdict-check`).
- **quality — unprovable-but-better.** Two gate tools carry five more attributed kills under a fenced counter; a content
  leg whose key comes from executing the source; routed ledger 39 → 24 open; README index parity restored. Against that:
  the fence and V11 limits above, and one row landed with a defect fixed in-round.
- **discernment — unprovable-but-better; the non-author closure decides.** The round-43 outside disagreement (false
  `not fired`) became a lesson, Q36 and a check shown red → green; the U3 standing-battery drop shows the do-nothing
  control biting before freeze.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` and `kengaku | round-33` (coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Constant-compare TB2 grader — round 44 (decision table citing receipt cases) and registry rows `round44-c1-mutants`, `round44-c2`, `feal-linear-probe`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 44 entry; `corpus/evidence/round44/feal-linear-probe.txt` (14 cases; byte-equal re-run in `integrate/measure-final.txt`; pytest parity 14/14 `R44PytestParity`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-44/integrate/measure.sh` re-runs both claim counters and the no-harm set from a clean clone (`integrate/measure-final.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-44 paragraph (cryptanalysis technique unowned; `R44ConnSibling`)
