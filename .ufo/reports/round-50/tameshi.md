# tameshi — round 50 report (attempt 1, L1 TameshiR50)

Lane `tameshi-shokunin`, branch `master`. Base `e3729de862f73ae080d98fcf522a7081ce16e40a`. Freeze `cdbf24c07f9be3a991997c25b1f1d4bb375014ae`. Content (deciding) revision `b28a9780098ec3fe69d58e257ad0d2af6323eeb0`. Final lane hash `616dee6709a99c20d362ae099c50e537dd1957c2` (receipts only after `b28a9780`); `git ls-remote origin refs/heads/master` prints it. The watchdog shows no earlier attempt of this round, so nothing was inherited.

## Work performed

The round declared two claims on distinct axes, pre-registered with both counters, the frozen 49-item defect set, the controls, the no-harm monitors and the deciding script in `.ufo/evidence/round-50/contract.json` (`amendments: []`):

- **C1, calibration** (the lowest non-retired axis, at 8). Surface: the lane's disposition of the 49 items its round-40..49 closures routed, made into one checkable ledger, `corpus/routed-defects.json`, with at least five items closed this round. Label `C1_R50_PASS`.
- **C2, coverage** (frontier F6). This is the round's sourced claim and a capability acquisition: `tools/shrink-case.py`, a 1-minimal shrinker of a gate's killing case that states its cost in guard runs, scored on 12 public and 8 hidden mutants. Label `C2_R50_PASS`.

Work items:

- **Freeze and controls before any seat.**
  - Freeze `cdbf24c0` (`.ufo/evidence/round-50/freeze.json`, 14 digests).
  - Controls and both counter selftests were scored at freeze bytes and committed at `f87910fe` (`.ufo/evidence/round-50/control/`).
    - C1: CTL_0 `total=74`, CTL_OPEN `74`, CTL_PLANOPEN `27`, CTL_DECLINE `64`, all false. The fabrication control CTL_FAB printed `fixed=40 fixed_this_round=2 total=5`, false.
    - C2: CTL_ABSENT `total=23` and CTL_IDENTITY `total=20` are false. The positive control CTL_REF (the counter's greedy reference) printed `ok=20 total=0`, true.
  - Selftests call `measure()` end to end: C1 25/25, C2 9/9.
- **C1 dispositions.**
  - Ten disposer seats and ten independent cross-coders coded the 49 items (`.ufo/waves/round-50/w1/T50Disp4*.rows.json`, `T50Cross4*.json`).
  - They agreed on 30 of the 44 items both coded. The L1 resolved 14 disagreements, giving a reason for each (`.ufo/evidence/round-50/integrate/agreement.json`, `overrides.json`, `resolutions.json`).
  - The ledger lands 31 fixed, 7 open and 11 declined, landed in `80ea77e9` and finalised in `b28a9780`.
- **C1 fixes this round.** Nine routed items are closed by this round's commits:
  - R49.4: the standing axis table re-stated with calibration 8 (`4afb060c`).
  - R49.1: generator error paths, four selftest cases red before and green after (`43bfa7ae`; `.ufo/waves/round-50/w1/T50ExecGenFix.md`).
  - R49.2: successor counters, `.ufo/evidence/round-50/successor/reads-v2.py` and `sandboxed-confirm.py`.
  - R45.2 and R47.2: seven selftest receipts that no round had committed (`.ufo/evidence/round-50/routed/receipts/MANIFEST.md`).
  - R40.2, R40.3 and R40.4: corrections in `corpus/lessons/round-50.md` `## Corrections to earlier records`.
  - R46.4: an appended fold block in `corpus/lessons/round-46.md`.
  - The commits that carry these fixes are `79f44b55` and `b28a9780`.
- **C2 shrinker and sources.**
  - The shrinker was built blind to the hidden panel (`T50ExecShrinker.md`; ddmin with a verdict cache) and copied byte-exact to `tools/shrink-case.py` (`43bfa7ae`).
  - Row S271 (Zeller & Hildebrandt, TSE 2002) is at `corpus/SOURCES.md:146`.
  - Entries: `corpus/knowledge/fixture-shrinking-pilot.md` and the admitted, edited `corpus/knowledge/delta-debugging-minimization-contract.md`.
  - The README `## Round 50` F6 line is conditioned on the deciding receipt.
- **Frontier and quality.**
  - QUALITY 100: landed wave artifacts are append-only, with a falsifier.
  - QUALITY 101: a claim counter's selftest must reach `measure()`. Falsifier `.ufo/evidence/round-50/quality/reach-r49.stdout` is red; `reach-r50.stdout` is green.
  - Mistakes are mined in `corpus/lessons/round-50.md` `## Mistakes`.
- **Disclosed attacks on the frozen counters** (lesson `## C1`, `## C2`, `## Wave 2`).
  - A fabricated ledger passes C1 (`T50CritC1Contract.md` F1-F2).
  - A shrinker could rewrite C2's judge copies and its own run log (`T50SentinelShrink.md` F1-F2, `T50CritC2Contract.md` F1-F2).
  - Wave 2 checked the actual artifacts outside the counters:
    - 48 of 49 ledger rows agree. The one weak row (R40.4) was re-pointed.
    - The shrinker source review found no forgery route used (`T50W2RevShrinkCode.md`).
    - An outside `strace` count matches the stated runs, 188 = 188 (`T50W2ExecShrinkTrace.md`).
- **Deciding run.** One invocation at `b28a9780` (`.ufo/evidence/round-50/after/`, `DECIDING_RUN_EXIT=0`), landed in `616dee67`.

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `cdbf24c0` | pre-registration: contract, frozen counters, defect set, controls harnesses, no-harm, deciding script, census start | round 50 (`LOG.md`, 2026-10-26 round 50) |
| `f87910fe` | control and selftest receipts at freeze bytes | same |
| `65a2215b`, `4efa5cf5` | wave-1 and wave-2 specs and validated dispatches | same |
| `4afb060c` | SCORECARD pre-registration; standing axis table re-stated (R49.4) | same |
| `43bfa7ae` | `tools/shrink-case.py`; generator error-path fix (R49.1) | same |
| `79f44b55` | F6 entries, S271 and S022/S024 cells, README F6 line, lesson, QUALITY 100-101, routed fixes and receipts, successor counters | same |
| `80ea77e9` | ledger, integration records, Planned (round 51), LOG, wave-1 reports (candidate) | same |
| `b28a9780` | content revision: wave-2 integration, wave-2 reports, hidden panel revealed | same |
| `616dee67` | deciding receipts, census end, SCORECARD deciding section and capability row | same |

## Before → after measurements

- **C1** — `python3 .ufo/evidence/round-50/c1/measure.py --lane LANE --rev REV --explain`
  - Before (freeze tree, CTL_0): `rows=0 missing=49 fixed_short=20 this_round_short=5 total=74 C1_R50_PASS=false`.
  - After (REV `b28a9780`): `defects=49 rows=49 fixed=31 open=7 declined=11 fixed_this_round=9 … total=0 C1_R50_PASS=true` (`after/c1.stdout`).
- **C2** — `python3 .ufo/evidence/round-50/c2/measure.py --lane LANE --rev REV --work EMPTY --panel .ufo/evidence/round-49/c2/panel.json --hidden HIDDEN`
  - Before (freeze, CTL_ABSENT): `shrinker_absent=1 records_bad=2 total=23 C2_R50_PASS=false`.
  - After (REV `b28a9780`): `mutants=20 ok=20 units_before=164 units_after=43 entry=1 readme_f6=1 … total=0 C2_R50_PASS=true` (`after/c2.stdout`).
- **No-harm** at REV: `FROZEN_UNCHANGED=1`; ten monitors ok (commandD 9; cold-read score 8, 64 of 64 credited; r45 freshness 73/71; registry 131); QUALITY 98 precheck `64 → 64 lost=0`; census exit 0.
  - At the candidate `80ea77e9`, r45 freshness was red (population 74). The cause was S022 `queued → mined`, and the cell was restored before the deciding run (`T50W2ExecNoHarm.md`).

### Verdicts

- **C1: verifies (measured).** Calibration stays 8, which is the monitor's ceiling; the claim moves the surface, not the score.
  - The PASS line certifies form, not truth. In a scratch clone, re-pointing 29 of 31 fixed rows at unrelated keyed lines keeps the same PASS (`T50W2ExecC1Probe.md`).
  - The content evidence is the two independent codings plus 17 wave-2 row attacks, which agree on 48 of 49 rows.
  - Disclosed non-deciding invocations: the L1 scratch probe (`integrate/l1-probe-c1.stdout`) and T50W2ExecC1Probe at `80ea77e9`.
- **C2: verifies (measured).** The frozen counter's forgery routes are disclosed.
  - The landed shrinker uses none of them: source review and outside run tracing.
  - A plain greedy loop also passes (CTL_REF), so the claim is the capability with its stated cost, not search efficiency.
  - Disclosed non-deciding invocation: T50W2ExecC2Probe at `80ea77e9`, with a synthetic hidden panel.

## Sources & frontier

- **Rows.** 130 → 131 (`git show REV:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} \|'`).
  - Added: tier A 1 (S271), opened 2026-10-26.
  - Rows touched old → new: S022 used-by `—` → the pilot entry (status kept `queued`); S024 used-by gains the two F6 entries. Logged in the lesson `## Gate`.
- **Census.** Start exit 0 (`.ufo/evidence/round-50/census-start.exit`); end exit 0 (`census-end.exit`, at `b28a9780`).
- **Frontier.** F6 open → held (round 50), for the method on killing cases. The round-29 B5 survivor is not discharged.
- **Sourced claim.** C2.
- **Mined mistakes.** `corpus/lessons/round-50.md` `## Mistakes`, rows 1-3. Row 3 is found this round and routed, not fixed.
- **Assimilation.** Theme F6 from `merge/tameshi/`:
  - Admitted: `delta-debugging-minimization-contract.md`, with edits.
  - Refused: the staged S167 row as-is, and the entry's 139-runs attribution.
  - Deferred: `r7-ieice-mutant-abstraction-authority.md`.
  - Id lists: reg-ids 130, staged-ids 103, collisions 8 (S153-S160). Renumber map: S167 → S271, by document.
  - Evidence: `.ufo/waves/round-50/w1/T50ExecIdGuard/`.
- **considerthese.** `2026-10-26.md` proposal 3 is implemented as C1's ledger. The recurrence half is still open and planned.

## Trend verdicts

- **expansion: improved.** F6 moved from open to held through two admitted entries citing S271, which was opened and quote-checked twice. The capability row is demonstrated by the deciding run.
- **quality: improved.**
  - Nine routed defects were closed with evidence. They include the generator's error paths, with red-before and green-after receipts, and five correction or receipt gaps carried for up to ten rounds.
  - Two new QUALITY criteria, each with a falsifier.
  - Wave 2 found no-harm, wording and inference defects; these were corrected before the deciding run.
- **discernment: improved.**
  - Every routed item now has a disposition coded twice independently, and the disagreements were resolved with reasons.
  - One package entry was admitted with corrections; one staged row and one cost claim were refused on located evidence.
  - The counters' own forgery routes were found and disclosed, not hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `reports/round-1-calibration.md#box-1` (lane assertion; no independent verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `reports/round-1-calibration.md#box-2`; round-50 LOG entry (shrinker over 20 mutants, `.ufo/evidence/round-50/after/c2.stdout`)
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-21/coldread/ledger.json` (64/64 credited at `b28a9780`, `.ufo/evidence/round-50/after/no-harm.stdout`; lane-dispatched readers, not independent)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `reports/round-1-calibration.md#box-4`; `.ufo/waves/round-50/w1/T50ConnSiblingShrink.md` (no sibling holds reduction ground)

## Round shape, seats, hygiene

- **Shape: two v1 waves.**
  - `w1` (build): 50 seats — scribe 19, critic 12, executor 8, connector 3, scout 2, mutation-tester 2, reviewer 2, revenger 1, sentinel 1. All 50 settled (`w1-results.json`); T50Cross40 returned its codes in its output and wrote no json file.
  - `w2` (falsify): 35 seats — critic 13, reviewer 13, executor 5, connector 2, mutation-tester 1, scout 1. All 35 settled (`w2-results.json`).
  - Dead seats: 0.
  - Round total: 85 seats. No residual call. The L1 held the §3 planner seat; the planning data walk rode T50RevengerRecur.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `?? p.err` and `?? p.out` (20:10, content "QUOTE S115 … spans/S115-1.txt"). Neither names tameshi or round 50, so they were left untouched as another lane's files. No misroot of mine.
- **Scratch.** `/fast/scratch/hyaku/tameshi-r50` was removed after landing. The hidden panel copy in `~/.local/state/tameshi-r50/` was removed after its committed reveal (`.ufo/evidence/round-50/c2/panel-hidden.json`, sha256 `5c14e9a6…` = contract pin).
- **Tool installs:** none (bwrap 0.13.1 and strace were already present).
- **Open L0 questions:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
