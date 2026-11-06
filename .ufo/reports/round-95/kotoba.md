# kotoba — round 95 report (attempt 2, L1 KotobaR95a2; attempt 1 KotobaR95; Linux host, omp)

Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Pushed lane tip at report time: **`7578906425d06e3124d8ea1c652883d4f4e89bef`** (`git ls-remote origin refs/heads/master` prints this hash; `jj-lane.sh state` → `ahead=0 behind=0 tracked=0`). Round base: `2d886a91e57efd3555ec9076a63209e2d8bfbb8d`. Freeze: `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`. Landing (code + corpus): `d1144fab4b31f1f5196cb347303894e7b1e54eda`. Record: `f6a9f76a28fed4446e30d97a040b4c94736308ce`. Wave evidence: `7578906425d06e3124d8ea1c652883d4f4e89bef` (the tip).

## Work performed

**Declared claim (1, frozen before any data in `plans/round-95.md` at `673d1e2e`):**

- **C1 — depth (the lowest owned non-retired axis; score held at 9).** `verifiers/check_mutation_battery.py --self-test` kills the round-94 MutTesterBattery94 survivors N1 (the `--rev` kill-set check reads the manifest at `HEAD`), N5 (the target-set refusal labelled `arm kill-set-size:`) and N11 (the pin accepts two rows above it). The claim is measured with a new v3 counter. Its rule 1 says a kill is a reported failure and a crash is a RUN-ERROR. Rule 1 is sourced on S270 (Python `unittest`, errors vs failures), which was opened this round. My measured reading at `d1144fab`: **MET**. The verdict belongs to the non-author closure.

Work items:

1. **Freeze (`673d1e2e`, attempt 1).** These were committed together:
   - the plan;
   - the v3 counter `verifiers/fixtures/round-95/selftest-kills.py` (sha256 `d6ae74af…1d269001`), with three rules: RUN-ERROR is its own class, a code decoy is added beside the comment decoy, and mutant runs are source-blind;
   - the control-world builder `verifiers/fixtures/round-95/build-forgeries.py` and six forgery patches;
   - the pre-data receipts (`.ufo/waves/round-95/receipts/redbefore-c1-base.txt`, `poscontrol-r94c1-base.txt`, `forgery-f1..f6-*.txt`, `census-before.txt`).
2. **Wave `r95-w1`** (`.ufo/waves/round-95/`: `gen-w1.py`, `r95-w1-spec.json`, `r95-w1-dispatch.json`, `r95-w1.ready`/`.ready.dispatched`, `r95-w1-results.json`, seat outputs in `w1/`). Every seat prompt leads with `/skill:godspeed`.
3. **Builders:**
   - ExecBatteryKills (`w1/ExecBatteryKills.md`, patch sha256 `f9506fe3…`, C1) adds one 67-line hunk inside `self_test()`, taking the self-test from 38 to 46 assertions.
   - ScribeCorpusR95 (`w1/ScribeCorpusR95.md`) wrote S270, the lesson scaffold and the README row.
   - ScoutSourcesR95 (`w1/ScoutSourcesR95.md`) re-opened S270 and S260 and screened candidates.
   - ConnectorOverlapR95 (`w1/ConnectorOverlapR95.md`) ran the overlap scan and carried the planning data-walk.
   - ExecBaseBattery (`w1/ExecBaseBattery.md`) took the base no-harm readings and measured the floors timeout.
4. **Attack seats:**
   - ReviewerBatteryKills (`w1/ReviewerBatteryKills.md`): no blocking finding. It hand-applied each mutant and named the failing behavioural arm.
   - ReviewerCounterV3 (`w1/ReviewerCounterV3.md`): f8, a guard-aware bytecode sniffer; F1–F3 on the exit ladder and timeout.
   - ExecCounterForgery (`w1/ExecCounterForgery.md`): worlds g1–g5, all UNMET. g2 is a bytecode sniffer and g3 is recompile-and-compare; each kills single targets with its decoys held.
   - MutTesterBattery95 (`w1/MutTesterBattery95.md`): m08 survives; m11 shows RUN-ERROR live.
   - CriticClaimR95 (`w1/CriticClaimR95.md`): F1 is N4 provenance; F2 says the rule-1 control is run-granular.
   - SentinelScopeR95 (`w1/SentinelScopeR95.md`): scope, no-harm and safety all PASS on candidate `cbadcf02`.
   - MutTesterCounter95: **incomplete** (see Round shape).
5. **Integration (`plans/round-95-addendum-1.md`, record `f6a9f76a`).** Nothing frozen changed. The addendum discloses:
   - **A1:** the anti-sniffing bound is wider than the plan states, because of bytecode and recompile-compare self-tests. The behavioural proof is the three hand-applied readings.
   - **A2:** the rule-1 control works at run granularity (f6, live m11), not predicate granularity.
   - **A3:** N4, counter exit-ladder hygiene and the m08 survivor.
6. **Attempt 2 (this L1).**
   - I inherited the committed freeze, landing and record, plus the uncommitted wave dir. Everything was re-verified against the receipts and nothing was discarded except the two raw `unittest.html` copies (see below).
   - I received WAVE-DONE (the orchestrator re-pointed it after its crash) and read each seat's report file as its result, because `results.json` carries `output=null` per seat.
   - I committed the wave evidence (`7578906`) and re-ran the end census.
   - I ran the misroot sweep and filed this report.

## Landed changes

| change | commit | LOG.md / record |
|---|---|---|
| freeze: `plans/round-95.md`, v3 `selftest-kills.py`, `build-forgeries.py`, `forgeries/f1..f6.patch`, pre-data receipts | `673d1e2e` | LOG § Round 95 (claim as frozen; pre-data controls) |
| C1: `verifiers/check_mutation_battery.py` (self_test arms only, +67 lines) | `d1144fab` | LOG § Round 95 (landing) |
| corpus: `corpus/SOURCES.md` S270 (195 → 196), `corpus/lessons/round-95.md`, `corpus/README.md` row, `corpus/QUALITY.md` Q84 (round-94 closure defect 1) and Q85 (mined mistake) | `d1144fab`; lesson settlement in `f6a9f76a` | LOG § Round 95 (frontier step) |
| `plans/round-95-addendum-1.md`, landing receipts, LOG § Round 95, SCORECARD round-95 annotations + round-96 intentions | `f6a9f76a` | LOG § Round 95 (integration) |
| wave evidence `.ufo/waves/round-95/` (spec, dispatch, ready, results, 12 seat reports, seat receipts, MutTesterCounter95 salvaged raw matrix) | `75789064` | LOG § Round 95 (wave) |

Unchanged:
- SKILL.md and PROVINCE.md: `git diff --stat 2d886a91 75789064 -- SKILL.md PROVINCE.md` is empty.
- Every `round-*-verifier-spotcheck.md`.

## Before → after measurements

**C1 — depth.** Counting command: `python3 -B verifiers/fixtures/round-95/selftest-kills.py c1 <rev>`, frozen at `673d1e2e`.
- **Before** (base `2d886a91`, `receipts/redbefore-c1-base.txt`): `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-UNMET`, rc 1.
- **After** (`d1144fab`, `receipts/landing/c1-counter.txt`): `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-MET`, rc 0. The self-test reads `0 failure(s) over 46 assertions` (`landing/bat-selftest.txt`).
- **Positive control** `selftest-kills.py r94c1`: MET at the base (`receipts/poscontrol-r94c1-base.txt`) and at landing (`landing/r94c1-counter.txt`).
- **Forgery controls:** f1–f6 all UNMET pre-data. Seat worlds g1–g5 and f8 are also UNMET. Bound A1 is disclosed.

**No-harm at landing (`d1144fab`, `receipts/landing/`):**

| check | reading |
|---|---|
| round-93 `c1-killpin-rev.sh` / `c2-pinkey.sh` | MET / MET |
| round-94 `selftest-kills.py c1` / `c2` | MET / MET |
| round-92 `controls-run.sh` | `shortcuts refused 2 of 2; honest held 2 of 2`, rc 0 |
| gate registry | `74 of 74 … phantom 0`, rc 0 |
| floors self-test | `0 failure(s) over 176 assertions` |
| tip battery | `guards 5 of 5; tip battery exit 0: 3 of 6`. The floors gate exited 0 in 236.2 s; round-94 read 2 of 6 because of its timeout. The other three reds carry from base. |
| census | rc 0, 34 `W04`, none new |
| SKILL.md | byte-identical |

**Mined-mistake fix, shown able to fail:**
- f6 (`receipts/forgery-f6-crash-report.txt`): the n11 run is RUN-ERROR and the reading is `run errors 1`. The round-94 `rc != 0` rule would have scored that run KILLED.
- Live, MutTesterBattery95 m11 is RUN-ERROR.
- The demonstration is run-granular only (A2).

**Q82 wave-evidence bytes** (`du -sb`, 2026-11-05, measured after landing):

| round | bytes |
|---|---|
| round-95 (committed tree) | 719539 |
| round-94 | 611324 |
| round-93 | 674505 |

Two seat copies of the raw S270 page (`unittest.html`, 336978 B each) were left out of the commit and deleted. Their sha256 `f9510cd7…` is recorded in the lesson Gate and matches; the URL and digest are the evidence.

## Sources & frontier

- **SOURCES.md rows before → after:** 195 → 196. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at `2d886a91` and at `75789064`.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
  - Round start: `receipts/census-before.txt`, exit 0, 34 `W04`.
  - Round end: `receipts/landing/census-validate-end.txt`, exit 0. I re-ran it at report time after `75789064`: exit 0, 34 `W04`, last line `kotoba ok …/corpus/SOURCES.md`, no `E`-code.
- **Rows added by tier:** tier A ×1. S270 is the Python `unittest` docs page (`https://docs.python.org/3/library/unittest.html`), opened 2026-11-05: HTTP 200, 336978 B, sha256 `f9510cd7…`. Located quote: "Each tuple represents a test which raised an unexpected exception." Status `mined`. Tiers B and C: 0.
- **Rows touched old→new:** none (lesson § Status changes). S260 was re-opened as corroboration with no new row, which applies Q84 (round-94 closure defect 1).
- **Same-round reject:** the Apache Ant `junit` task manual, which conflates errors and failures. The reason and flip condition are in the lesson Gate. pytest exit codes and TAP 13 were screened and left for a later round.
- **Sourced claim:** C1 rule 1 cites S270 (plan § C1, lesson § Gate, SCORECARD round-95 annotation).
- **Mined mistake:** `run-error-scored-as-kill` · evidence `.ufo/waves/round-94/w1/CriticClaimsR94.md` D8 · captured-by `none` · fix: rule 1 + Q85, shown able to fail on f6 and m11.
- **Frontier rows advanced:** kill counters now separate a run error from a kill, and the sniffing guard now covers code as well as comments.
- **Assimilation:** none. L0 `kotoba | round-88` is still open and no claim depends on it.
- **Considerthese:** I re-read `considerthese/2026-10-26.md` and implemented nothing. The per-proposal reasons are in lesson § Considerthese.

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted. S270 is a SOURCES row cited by the plan and the lesson.
- **quality: improved.** The battery self-test kills three mutants it missed at the base: `0 of 3 → 3 of 3` under a stricter counter (`redbefore-c1-base.txt` vs `landing/c1-counter.txt`). The counter no longer scores crashes as kills (f6).
- **discernment: improved, conditional.** Round-94 closure defects were routed as follows:
  - 1 → Q84
  - 2 → rule 1 / mined mistake
  - 3 → code decoy + rule 3
  - 4 → C1

  Attack seats widened the counter's disclosed bound (A1), and it is disclosed rather than hidden. The non-author spot-check of S270 and the Ant reject is still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SHONEN.md` box 1 pointers, unchanged; SKILL.md byte-identical between `2d886a91` and `75789064`.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` § Round 95 (C1 arms built, attacked and landed; readings at `d1144fab` in `.ufo/waves/round-95/receipts/landing/`).
- [~] Instructions executable by an agent without oral context. Evidence: ReviewerBatteryKills, CriticClaimR95 and SentinelScopeR95 each ran the frozen counter on their own candidates (`w1/*.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md` unchanged; ConnectorOverlapR95 sibling scan (`w1/ConnectorOverlapR95.md`); no sibling file touched.

## Round shape, seats, and lane status

- **Shape:** ONE v1 wave `r95-w1` (band 8–16) of 12 seats:

  | role | seats |
  |---|---|
  | executor | 3 |
  | scout | 1 |
  | scribe | 1 |
  | connector | 1 |
  | reviewer | 2 |
  | mutation-tester | 2 |
  | critic | 1 |
  | sentinel | 1 |

  Attack seats are 5 of 12 = 42 %. There is 1 connector. No residual call; the round total is 12. Routing came from `task.agentModelOverrides` at spawn, and no `model` was passed.
- **Planner seat:** held by the L1. ConnectorOverlapR95 carried the planning data-walk.
- **Dead or incomplete seats:**
  - The orchestrator session crashed mid-wave, and `r95-w1-results.json` holds `output=null` for all 12 seats (note: "orchestrator kernel restarted mid-wave").
  - 11 seats wrote complete report files.
  - **MutTesterCounter95 is not counted.** Its report stops at "Results and verdicts appended below when the job lands", so it has a design and predictions but no verdicts. Its raw matrix outputs (62 files, 78998 B) were salvaged from its scratch dir into `w1/MutTesterCounter95/salvaged-results/` as uncounted evidence for round 96. Two of them read FALSE `C1-PREDICATE-MET`: counter mutant M5 (mutant written to disk) on f5, and M6 (honest conjunct dropped) on its demo world f9. M2, M7 and M8 are not exposed by any committed control. I route this as a gap in the counter's committed control battery, not a C1 finding.
  - No residual wave: C1's reading does not depend on that seat.
- **Earlier attempt:** `.ufo/watchdog.log` 2026-11-05T23:31:19 `lane-dead-no-report kotoba round=95`.
  - Reused after re-verification: commits `673d1e2e`, `d1144fab` and `f6a9f76a`, and the uncommitted wave dir (committed in `75789064`).
  - Discarded: the two raw `unittest.html` copies.
- **Stale-lane:** none. This respawn-per-round driver has no other open mission for this lane.
- **Tooling:** nothing was installed or upgraded by the L1 or any seat (seat reports say so). No pacman and no sysctl.
- **Scratch:** `/fast/scratch/hyaku/kotoba-r95` (about 8 GB, including the dead seat's 3.7 GB tree) was removed by the L1 after landing (`ls /fast/scratch/hyaku | grep -c kotoba-r95` → 0).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned `.scratch/*`, which I did not touch, and the pre-existing `?? w4lines.txt` (mtime 16:57, before this round, no kotoba content), which is not this lane's. No kotoba seat file is at the fleet root.
- **Commits:** all through `jj-lane.sh commit … --as kotoba`. Landed: `673d1e2e…`, `d1144fab…`, `f6a9f76a…`, `7578906425d06e3124d8ea1c652883d4f4e89bef`.

## Open items and L0

- **Routed to round 96:**
  - m08: the target-set `!=` relaxed to `<` survives because there is no extra-target world.
  - N4 is still unobservable.
  - Recompile-compare and bytecode forgery worlds (g2, g3, f8) should become committed controls.
  - Counter exit ladder (ReviewerCounterV3 F1/F3).
  - A predicate-flipping crash world (A2).
  - Counter-mutant gaps M2/M5/M6/M7/M8 from the salvaged MutTesterCounter95 matrix.
  - The tip battery's flat 280 s outer cap on the floors gate.
- **Carried, unchanged:** L0 `kotoba | round-88`, `kotoba | round-73`, `kotoba | round-92`.
- **No new L0 question this round.**
- **Verdicts are measured, not admitted.** The non-author closure rules the round.
