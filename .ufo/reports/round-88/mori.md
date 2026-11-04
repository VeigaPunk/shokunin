# mori — round 88 (attempt 1)

## Work performed

**Declared claims:** **C1 operability** — six surviving clauses in the r87 C1 counter gain
load-bearing tests (18 → 24 arms; six mutants killed). **C2 calibration** — the r87 receipt gate
refuses the two frozen counterfeit receipts while retaining its seven-receipt positive control
(17 → 23 arms). Calibration is tied lowest at 5; operability is 7. No score increases.

**Final verdict: honest stop, not admission.** Both numeric targets reproduce, but C1's
instrument assurance is **unprovable**, and C2 introduces an **operability harm**: a genuine
`./tools/mori-record-sweep.py` replay is rejected by token spelling. The counterexample is not
waived merely because the seven original receipts still pass. Closure remains non-author work.

Final lane tip **`838576cb1073d446ec8b002265a8f3609e02e5dd`**, pushed; the pre-report command
`git -C /home/vgpnk/Projects/shokunin/mori-shokunin ls-remote origin refs/heads/master` printed
that exact hash. Entering tip: `1bd5ec3fa260458f74eb32a2e5bb157209c5934d`.

- Froze the predicates, counters and do-nothing/label-only controls at `2a5e3ad9`:
  `.ufo/waves/round-88/{contract.md,count-c1.py,count-c2.py,evidence/controls-r88.txt}`.
- Added six real C1 arms and three C2 helpers with six arms in the r87 counters (`4d0f7bf0`);
  corrected the missing fixture tally lines at `d5e2eda4`. The first C1 run was genuinely unmet
  (`killed=4 survivors=2`), retained rather than hidden; `Mo88S01Lesson.md` reproduces it.
- Recorded the after receipt at `9c775ac2`, measuring `d5e2eda4`. Its command was replayed in a
  shared clone and its body compared equal. Final verification is separately committed at
  `.ufo/waves/round-88/evidence/final-verification-r88.txt`.
- Registered r87/r88 instruments as SKILL registry rows 21/22; added explicit limits, QUALITY
  183–185, the corrected knowledge entry/index, SCORECARD outcome and LOG correction.
  Evidence: `SKILL.md:1373-1381`, `corpus/QUALITY.md:2122-2156`, final lane tip above.
- Curated S604–S606 from one opened TUF document; corrected the erroneous locator through S605,
  retained the duplicate rejection as S606, and mined the fixture, anchor and correction-guard
  mistakes. Evidence: `corpus/lessons/round-88.md`, Gate and final disposition.
- Ran **one v1 wave of 12 seats**: 3 executor, 2 scribe, 1 scout, 2 reviewer, 1 critic,
  1 mutation-tester, 1 connector, 1 simplifier; attack share **4/12**, one connector, no residual
  call. The L1 holds the planner seat; `Mo88Sc01Scope` performed the bounded data walk.
  Validator: `w1-dispatch.json` counts `spawn=12`; parent sent **WAVE-DONE mori r88 w1** before
  this report. `w1-results.json` contains 12 terminal outputs and reports no deaths, but omits
  per-seat IDs/status fields; no missing fields are fabricated. No model override was passed.

### Material attack results

- `Mo88E01C1Arms.md` and `Mo88R01ReviewC1.md` independently map each real mutant to its promised
  new failing arm. Nevertheless, `Mo88C01Critic.md:23-50` constructs an **arms-free checksum
  canary** that meets the counter. The broad kill rule accepts nonzero exit, including unrelated
  failure, and does not establish killer attribution. This prevents treating the met line alone
  as proof of the intended capability.
- `Mo88E02C2Gate.md` independently hand-builds the frozen receipt fixtures and agrees with their
  refusal. `Mo88R02ReviewC2.md:7-16` bypasses token binding using a shell comment; the critic also
  passes a self-printing body that includes the bound path token, and proves the genuine `./path`
  false refusal (`Mo88C01Critic.md:97-136`). These are recorded, not repaired post-data.
- Mutation testing found **32 mutants: 20 killed, 12 surviving**, with exact anchors and witness
  proposals in `Mo88M01Mut.md`. The simplifier measured 33 candidates, 12 target-preserving and
  one recommended deletion; pure duplicate/dead assignments are deferred because receipt-bound
  instrument bytes must not silently change (`Mo88Si01Simplify.md`).
- The final knowledge review said **ENTRY needs-changes**, D1–D18. Integration answers these in
  the rewritten entry, including the load-bearing space in the self-print example, provenance,
  explicit scratch, necessary-condition wording and missing limits. No clean re-review or
  outside spot-check of the rewrite is claimed.

## Landed changes

Every row is tied to **LOG.md Round 88** and its appended **Round-88 correction of record**.
All hashes are ancestors of the final pushed lane tip.

| Work | Carrying commit |
|---|---|
| Frozen contract, both counters, controls | `2a5e3ad96deb978ed1fb958e87b4be8221fb23b7` |
| r87 subject tests and receipt-gate changes | `4d0f7bf0b0a0d978fa65d9b93edc37a2e6556550` |
| Tally literals in **both** r87 subject and r88 detector | `d5e2eda494877a85edaa4e287d6ad81843d9a8a1` |
| After receipt, measuring d5e2eda4 | `9c775ac2131da13c4c4cfdf2b14077184076f557` |
| Initial corpus, gate rows, selftest receipt, source copy and wave spec/handoff | `7c4946c218985e6589b851b8ef7efedc8a21a369` |
| Lesson/LOG, seat reports and E1–E3; subsequent lesson correction | `fecfc10af9408c548f4b4f376957143b9fbf07b7`, `f443b754a1a9f83b784f341bf471f4c8bbd9a1e5` |
| Final verdict, E4, S605/S606, corrected entry/index, final review outputs, results and final verification | `838576cb1073d446ec8b002265a8f3609e02e5dd` |

**Record corrections:** E1 incorrectly said no subject bytes moved; E4 explicitly corrects it:
the subject and detector fixtures both changed after the first measurement. The numeric target,
mutant population and kill rule did not change, but detector fixture drift was post-data.
E2 corrects the M5 sketch (`arms=54` in the r87 subject, not 24); E3 records the claim-scope
counterexamples. No report or history was rewritten to conceal them.

## Before → after measurements

Run from the lane, replacing R with the named revision; create the scratch directory first:

```sh
mkdir -p "${HYAKU_SCRATCH:-/fast/scratch/hyaku}/mori-r88/recheck"
python3 -I .ufo/waves/round-88/count-c1.py R --scratch "${HYAKU_SCRATCH:-/fast/scratch/hyaku}/mori-r88/recheck"
python3 -I .ufo/waves/round-88/count-c2.py R --scratch "${HYAKU_SCRATCH:-/fast/scratch/hyaku}/mori-r88/recheck"
```

| Claim | Before: entering `1bd5ec3f` | After: measured `d5e2eda4` | Admission limit |
|---|---|---|---|
| C1 | `C1=unmet mutants=6 killed=0 survivors=6 total=6 arms=18`, rc1; label-only control: arms24/survivors6, rc1 | `C1=met mutants=6 killed=6 survivors=0 total=6 arms=24 rev=d5e2eda49487`, rc0 | Real tests verify; checksum-canary also meets the counter: assurance unprovable |
| C2 | `C2=unmet real=met fx=4 clean=1 refused=0 absent=1 arms=17`, rc1 | `C2=met real=met fx=4 clean=1 refused=2 absent=1 arms=23 rev=d5e2eda49487`, rc0 | Exact counterfeits refused; genuine equivalent path newly rejected |

Evidence: frozen controls, after receipt and final-verification receipt. The final post-wave pass
ran seven commands, all rc0: entering/final source censuses, final validate, detector selftests
(25/0 and 17/0), and both target runs at the measured revision. This does not rerule the attacks.
The original freeze C1 counter also reproduced the final target in the critic's run; detector
fixture drift still remains a disclosed protocol defect.

**Axes:** operability **harmed** (genuine-input rejection despite better test coverage);
calibration **unchanged** (narrow refusal improvements, broader assurance not established);
depth improved in the bounded final entry; coverage, freshness and adjacency unchanged.
Scores remain 6/7/5/5/5/6, delta 0; no admitted capability-table addition.

## Sources & frontier

Counting commands:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin mori`
and `... sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.
Entering census is re-derived from `git show 1bd5ec3f:corpus/SOURCES.md` with the same census parser;
full commands/TSV are in `evidence/final-verification-r88.txt`.

| Metric | Before | Final after |
|---|---:|---:|
| rows | 376 | 379 |
| tier A/B/C | 337/19/20 | 340/19/20 |
| mined/queued/rejected | 320/24/32 | 322/24/33 |
| validate exit | 0 | 0 |
| E findings / W04 warnings | 0/35 | 0/35 |

- Added **three tier-A rows but one distinct document**: S604 initial locator, **S605 supersedes
  S604** with the correct §5.3 step 5.3.5, and S606 rejected alternate-index duplicate.
  Opened 2026-11-04: [TUF v1.0.37](https://theupdateframework.github.io/specification/v1.0.37/)
  and its `index.html`; HTTP200, zero redirects, 248698 bytes/4997 lines, equal SHA
  `f20fda0dda7128f3b9cc1f12f3d90301b0f6e163576ba285bfe485d1671e8def`.
  The Gate carries the 23-word quote for each new row; exact sentence raw lines 3505–3506.
- Existing-row change: S604 `used-by` **knowledge entry → round-88 lesson**; status/recheck
  unchanged. The original immutable locator is restored; the corrected row is append-only S605.
  An intermediate pushed in-place edit happened and is explicitly corrected, not erased.
  The initial assertion that E04 prevented supersession was wrong: the parser exempts
  `teaches` beginning `supersedes S…` (`sources-census.sh:646-649`).
- The sourced C2 entry cites **S605**, includes TUF source-silence (an analogy, not receipt
  semantics), and is indexed in README. No FR row advanced: this deepens existing instrument
  ground, not a new host-observability surface. The full-census value snapshot was excluded
  before data and remains the recorded next-round depth item.
- `considerthese/2026-10-26.md` suggestion 4 is implemented as the lesson's adoption-status
  table. **Assimilation: none**; no shokuknow package was adopted or changed.

## Trend verdicts

- **expansion: unchanged** — one source document deepens the existing receipt-instrument surface;
  three registry rows are not three sources, and the demonstrated instruments are not admitted
  repertoire additions.
- **quality: harmed** — the valid `./path` replay regression is real and retained; green fixture
  counts do not make that trade an improvement. Evidence: critic `:97-113`, contract E4.
- **discernment: unchanged** — criticisms and source/entry mistakes became corrections and QUALITY
  185, but lane-owned seats do not supply the required outside admit/reject spot-check. Pending
  non-author closure; no outside agreement is invented.

## SHONEN

- [~] Real decision tables, error patterns and checklists: SKILL existing domain sections and new
  gate rows 21/22 with explicit instrument limits; no promotion verification asserted.
- [~] End-to-end work executed/logged: LOG Round 88, frozen controls, after/final receipts and
  all twelve settled seat outputs — including the adverse verdicts.
- [~] Executable instructions: explicit-scratch commands and expected rc/output in contract,
  receipts and the final knowledge entry; canary/path limitations are disclosed, not waived.
- [~] Province boundary retained: own instrument/corpus changes only; connector cites tameshi,
  mado, kotodama and chousa, absorbs none; PROVINCE unchanged.

## Settlement, scope and carried debt

**Stale-lane:** launched 2026-11-04T10:43:28-03:00; progressing through lane-authored commits above.
No other mission of this lane is open. Formal WAVE-DONE preceded this report.
Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only orchestrator
`.scratch` files and pre-existing `after` (Nov 3); no mori-seat misroot required movement.
Round scratch `/fast/scratch/hyaku/mori-r88` was removed after landing; no scratch path is an
irreplaceable evidence pointer. No tools installed/upgraded; pacman stayed paused.

Routed for the next round: subject identity/declared-killer attribution, comment/selfprint
binding bypasses, path identity false refusal, inherited label-substring arms, the 12 counter
mutant survivors, dead/duplicate assignments and FX wording. These are not silently fixed after
freeze. r87 gate-registration and exact counterfeit defects are addressed; F3 host-path replay
and the eight r86 record defects remain carried. No new L0 question; existing mori r65/r73
instrument and r61 assimilation questions were neither answered nor altered.

Correction to the r87 report's “16 survivors”: the committed probe has 23 MUTANT rows,
17 survived and 6 killed (`corpus/lessons/round-87-verifier-spotcheck.md`, defect 1). This report
carries the erratum; the r87 report bytes stay unchanged. Its missing historical stdout is not
retroactively claimed supplied by this round's new selftest receipt.
