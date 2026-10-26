# tameshi — round 49 report (attempt 1, L1 TameshiR49)

Lane `tameshi-shokunin`, branch `master`. Base `8ca67421111fa354b47b803358391d0b07fc6db9`. Freeze `14d03ea4270c6904064022b62b6faf467e5c0968`. Content (deciding) revision `bda60768afe172fe9e81359f51c835d8d53494d9`. Final lane hash `7d3d977f39acaa5723a696dff85ab183c80ddc8b` (a receipts-only commit after `143d91e9`) (`git ls-remote origin refs/heads/master` prints it). The watchdog shows no earlier attempt of this round, so nothing was inherited.

## Work performed

The round declared two claims on distinct axes. They were pre-registered with both counters, the controls, the no-harm monitors and the deciding script in `.ufo/evidence/round-49/contract.json`, with `amendments: []`.

- **C1, calibration** (the lowest non-retired axis, at 6). Seven SKILL.md sections had lost their cold-read credit. Each one was read pointer by pointer, its stale pointers and false statements were corrected, and it was re-credited with entries that a record append cannot lapse. Label `C1_R49_PASS`.
- **C2, coverage** (frontier F10). This is the round's sourced claim and a capability acquisition: one property-based generator, `tools/pbt-staged-id.py`, against the named gate `tools/staged-id-guard.py`, scored by a hidden 12-mutant panel. Label `C2_R49_PASS`.

Work items:

- **Freeze and controls before any seat.**
  - Freeze `14d03ea4` (`.ufo/evidence/round-49/freeze.json`).
  - Controls were scored at the freeze bytes and committed at `6885adb4` (`.ufo/evidence/round-49/control/c1-controls.stdout`, `c2-controls.stdout`). C1: CTL_0 `total=105`, CTL_J (the round-36 refresh shape) `durable_covered=60/64 total=94`, CTL_K `total=2`; all false. The fabrication positive control CTL_K2 printed `total=0` true. C2: CTL_ABSENT `total=25` false; CTL_FIX (the guard's own 14 fixtures) `confirmed=6` false; the witness cases confirmed all 12 mutants, so none is equivalent.
  - Both counter selftest receipts were committed before any wave (`control/c{1,2}-selftest.*`).
- **C1 reading.**
  - 18 reader seats covered the 90 base pointers: 80 hold, 2 stale, 5 unresolved, 3 absent by design (`.ufo/waves/round-49/w1/T49Read*.rows.json`).
  - 7 section critics checked 135 other statements: 15 false, 7 unverifiable (`T49Sec*.findings.json`).
  - 3 executors re-ran the round-12/13/14 recipes (`T49ExecR1{2,3,4}Cmd.md`).
  - 49 line-neutral corrections, each attributed to the seat that raised it (`.ufo/evidence/round-49/c1/corrections.json`): 45 from wave 1 and 4 from the wave-2 re-reads. They landed in `6db4b931`, `9b9b2a01` and `54a52365`.
  - The 94 read rows are in `.ufo/evidence/round-49/c1/reads.json`.
  - The re-key reads record files through git blobs (`.ufo/evidence/round-49/c1/refresh.py`; receipts `.ufo/evidence/round-49/coldread/rekey-54a52365/`, landed `fc5ac743`).
- **C2 generator and sources.**
  - The generator was built by a seat that never saw the panel (`T49ExecGenerator.md`). It was copied byte-exact to `tools/pbt-staged-id.py` (sha256 `0cbee392…`).
  - Rows S269 (QuickCheck, ICFP 2000) and S270 (Smallbone TR 76L) are at `corpus/SOURCES.md:144-145`. The pilot entry is `corpus/knowledge/pbt-generator-pilot.md`, and the F10 line is in `corpus/README.md` `## Round 49`.
  - The panel and witness cases were revealed in `bda60768` (`.ufo/evidence/round-49/c2/panel.json`, sha256 `d6dd2cf3…`, which matches the contract pin).
- **Mined mistake and its fix.** Round 48 scored its controls after the deciding run. The fix is gate 0 of `deciding-run.sh` plus QUALITY criterion 99 (`corpus/QUALITY.md`, `## Criteria appended — round 49`). Two independent seats showed the gate refusing (`T49ExecMistakeGate.md`, `.ufo/waves/round-49/w2/T49W2ExecMistake.md`).
- **Routed round-48 items.** Cold-read credit is restored (routed defect 1). The deciding script writes start/exit receipts and gates on control order (defects 2 and 3). The SCORECARD "pasted byte-exact" correction is appended (defect 5).
- **Deciding run.** One invocation at `bda60768` (`.ufo/evidence/round-49/after/`, exit 0), landed in `143d91e9`.

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `14d03ea4` | pre-registration, counters, controls harnesses, no-harm, deciding script | round 49 (`LOG.md`, 2026-10-26 round 49) |
| `6885adb4`, `455b2cd6` | control receipts; wave-1 spec and dispatch (generator kept blind to the panel) | same |
| `6db4b931` | 44 C1 corrections, integration tools, SCORECARD pre-registration, round-48 correction | same |
| `9b9b2a01` | content: generator, S269/S270, pilot entry, README F10, QUALITY 99, lesson, LOG, wave-1 reports | same |
| `f181a961`, `5f597fa8` | first re-key (candidate); precheck; wave-2 spec | same |
| `54a52365`, `fc5ac743` | wave-2 integration (4 clause fixes, row cells, entry limits, excerpt overrides); final re-key | same |
| `bda60768` | lesson fixes, precheck receipt, panel reveal (deciding revision) | same |
| `143d91e9` | deciding receipts, census end, SCORECARD deciding section and capability row | same |
| `7d3d977f` | `w2-results.json` and the late T49W2RevGenCode review (receipts only) | same |

## Before → after measurements

- **C1** — `python3 .ufo/evidence/round-49/c1/measure.py --lane LANE --rev REV --work EMPTY_DIR`
  - Before (base, CTL_0): `sections=64 covered=57 score=6 durable_covered=57/64 pointers=90 unresolved=9 unverified=81 total=105 C1_R49_PASS=false`.
  - After (REV `bda60768`): `covered=64 score=8 durable_covered=64/64 headings=7/7 pointers=94 unresolved=0 unverified=0 excerpt_miss=0 not_holds=0 absent=3 total=0 C1_R49_PASS=true` (`after/c1.stdout`).
  - Calibration moves 6 → 8. At the lane tip the monitor still credits 64 of 64 with score 8.
- **C2** — `python3 .ufo/evidence/round-49/c2/measure.py --lane LANE --rev REV --work EMPTY_DIR --panel PANEL`
  - Before (freeze, CTL_ABSENT): `generator=absent total=25 C2_R49_PASS=false`.
  - After (REV `bda60768`): `violations=0 cases=400 oracle_disagree=0 classes_short=0 confirmed=12 target=11 selftest_kills=6 records_bad=0 total=0 C2_R49_PASS=true` (`after/c2.stdout`).
- **No-harm** at REV: `FROZEN_UNCHANGED=1`; all nine monitors ok (registry 130, commandD 9); QUALITY 98 precheck `57→64 lost=0`; census exit 0.

### Verdicts

- **C1: verifies (measured).** Disclosed non-deciding invocation of the counter: wave-2 seat T49W2ExecC1Probe ran it at candidate `f181a961` and got `total=0`.
  - Known blind spots of the frozen counter: it cannot see whether an excerpt actually supports its sentence (contract `cannot_see`), and `absent` is uncapped (`T49CritC1Contract.md` F1).
  - This round's reads use `absent` for 3 of 94 pointers, each a path the section itself says is not a file.
  - The 7 rows the wave-2 seats judged weak were re-read by the L1 (`.ufo/evidence/round-49/c1/l1-overrides.json`).
- **C2: verifies (measured).** The counter cannot tell a property-based generator from a differential one (`T49CritC2Contract.md` F1). This one does not diff against the pristine guard: an access trace shows it never opens the pristine guard (`.ufo/waves/round-49/w2/T49W2ExecGenTrace.md`).
  - Its oracle is transcribed from the guard's rules (`T49W2CritGenOracle.md`); the entry says so.

## Sources & frontier

- **Rows.** 128 → 130 (`git show REV:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} \|'`).
  - Added: tier A 1 (S269), tier B 1 (S270), both opened 2026-10-26.
  - Rows touched old → new: none held. Two same-round cell corrections on S269/S270 are logged in the lesson `## Gate`.
- **Census.** Start exit 0 (`.ufo/evidence/round-49/census-start.exit`); end exit 0 (`census-end.exit`, at `bda60768` content).
- **Frontier.** F10 open → held (round 49).
- **Sourced claim.** C2.
- **Mined mistake.** `corpus/lessons/round-49.md` `## Mistakes`.
- **Assimilation.** Theme F10 from `merge/tameshi/`:
  - Admitted: staged S182 → S269 and S183 → S270, renumbered by document. S183's anchor was corrected from §4.1 p. 44 to §2.10 p. 34.
  - Refused: `r4-quickcheck-primary-correction.md` (false premise) and `pbt-generator-craft-author.md`.
  - Deferred: `pbt-generator-as-fixture.md`.
  - Id lists: reg-ids 128, staged-ids 103, collisions 8 (S153-S160). Renumber map: S182→S269, S183→S270. Evidence: `.ufo/waves/round-49/w1/T49ExecIdGuard/`.
- **considerthese.** `2026-10-26.md` proposal 3 was mined: 44 defects in 26 classes, 10 of which recur. It lands as a lesson section.

## Trend verdicts

- **expansion: improved.** New coverage-map ground: F10 moved from open to held through an admitted, sourced entry (S269, S270).
- **quality: improved.** 49 seat-sourced corrections to the seven sections (false statements, stale pointers, bare pointers). A generator with a measured kill record. No held entry was left stale: the routed items outside the seven sections are listed in the lesson.
- **discernment: improved.**
  - The lane's self-assessment now matches the repo: the cold-read instrument went 57/64 → 64/64 by reading, not re-keying.
  - Two package entries were refused on located evidence, and one package anchor was corrected.
  - The wave-2 semantic re-reads were integrated.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `reports/round-1-calibration.md#box-1` (lane assertion; no independent verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `reports/round-1-calibration.md#box-2`
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-21/coldread/ledger.json` (64/64 sections credited at `bda60768`, `.ufo/evidence/round-49/after/c1.stdout`; lane-dispatched readers, not independent)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `reports/round-1-calibration.md#box-4`; `.ufo/waves/round-49/w1/T49ConnSiblingPBT.md`

## Round shape, seats, hygiene

- **Shape: two v1 waves.**
  - `w1` (build): 55 seats — scribe 25, critic 9, executor 8, scout 3, connector 3, reviewer 3, mutation-tester 2, revenger 1, sentinel 1. All 55 settled with output (`w1-results.json`).
  - `w2` (falsify): 33 seats — critic 11, reviewer 10, executor 6, mutation-tester 2, connector 2, scout 1, sentinel 1. All 33 settled (`w2-results.json`). T49W2RevGenCode reported after the deciding run; its findings (F1 major: an unreadable guard exits 1 instead of 2, unreachable in the deciding run because the counter writes readable copies; F2/F3 minor error paths) are routed to round 50, not claimed fixed. Dead seats: 0.
  - Round total: 88 seats. No residual call. The L1 held the §3 planner seat; the planning data walk rode T49RevengerLapse.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `?? .ufo/reports/round-42/kengaku.md`, which is another lane's file and was left untouched. No misroot of mine (`.ufo/waves/round-49/w2/T49W2ScoutMisroot.md`).
- **Scratch.** `/fast/scratch/hyaku/tameshi-r49` was removed after landing. The hidden panel copy remains in `~/.local/state/tameshi-r49/`; it is revealed and committed.
- **Tool installs:** none.
- **Open L0 questions:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
