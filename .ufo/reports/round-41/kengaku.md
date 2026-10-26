# kengaku — round 41 report (hyaku run 9, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read at start `e50c134556b4ba48e29dc7ff364e90d6ef07a3f3`;
frozen claims `plans/round-41-claims.md` (freeze `8ef8b4fc7c6302c527db90244d69aa18f53e83bf`); first recorded probe run
`f774a87ad071122acd39ba02a9901b5b56d9910a`; landing `74513c0625df7886357b866074104a0cf4bf9cc1`; final lane hash
`e61aff6f72c7cc358f854762dd769cd55ef296b7` (`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR41`; the L1
holds the canonical planner seat (the validator rejects `planner`; the round-42 planning data walk rode scout `R41PlanNext`).
Earlier attempts: none (`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=41` line; `.ufo/waves/round-41/` absent at start).

## Work performed

Declared claims (2), frozen with red controls before any battery41 fixture and before the first recorded probe run:

- **C1 — calibration (owned, 8):** what `plans/tip_receipts.py` and the CLI half of `plans/sources_adopt.py` (both unedited) advertise
  and no `plans/battery41` fixture demonstrates — 23 frozen mutants (receipts T01–T13, sources S01–S09, S11; 21 `direct`, 2 `indirect`
  advertised), every direction witnessed before freeze; counter `plans/round41_c1_verify.py` binding `TOTAL = 23` and per-tool
  `FLOORS` (the round-40 plan's predicate was satisfiable by an empty list), exact exit-pair directions for the CLI, builds and tool runs
  in `bwrap --ro-bind / /` with a fixed system PATH.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break; capped by L0 `kengaku | round-33`):** the pinned
  Terminal-Bench 2.0 `constraints-scheduling` grader admitted as `corpus/knowledge/tb2-constraints-scheduling-grader.md` with a 25-case
  bubblewrap probe (`plans/constraints_probe.py`), rows S122/S123 (+S124 tier B, TB2.1 PR #245, closed unmerged); counter
  `plans/round41_c2_verify.py` (round-40 V1–V7 re-pointed + V8 order gate).

Work items:

- Protocol load: round prompt, `skill://godspeed`, `skill://shokunin`, `skill://swarm`, AXES (stagnation rule), SCORECARD `### Planned (round
  41)` and round-40 wave-2 outcome, round-40 report and spot-check (`corpus/lessons/round-40-verifier-spotcheck.md` §5 R1–R5),
  `.ufo/waves/round-40/build/R40PlanNext.md`, `.ufo/waves/round-40/falsify/F40CritPlanNext.md` (D1–D10 against the plan),
  `considerthese/2026-10-26.md`. Orchestrator host-safety rule (round-40 D1) placed verbatim in both wave contexts and every C1 seat task.
- TB2 task files fetched by the L1 at the pin 2026-10-26 15:19 -03, ten captures + `SHA256SUMS` (`corpus/evidence/round41/tb2-constraints-scheduling/`).
- Freeze `8ef8b4fc`: claims, both counters, probe, spec `plans/pkg-spec-r41.json`, dry table (`cases=25 predicted_pass=6 predicted_fail=19`),
  captures, controls (`.ufo/waves/round-41/claims/`): C1 do-nothing `killed=0 survived=23` exit 1; emptied-mutant-list copy `MUTANTS total=0
  … PREDICATE C1 fail` exit 1 (the control `F40CritPlanNext` D2 asked for); witness modules as battery `PREDICATE C1 pass` (reachable by
  witnessed work); tool-edited `PINS mismatched=1`, 13 invalid; hostile host-write module `build_write=OSError lane_read=FileNotFoundError`,
  probe-stub write denied, no marker after the run; witness run 23/23 in declared directions; S10 withdrawn as rc-equivalent
  (`s10_equivalence.txt` `ref_rc=5 mut_rc=5`); C2 do-nothing `checks=8 defects=5`; stage-check `cases=25 failed=0`; census-before exit 0.
- First recorded probe run `f774a87a`: `cases=25 observed_pass=6 observed_fail=19 mismatches=2` (the pilot's two mispredictions, carried
  verbatim and disclosed in the claims), `regrade cases=25 differ=0`, second run byte-equal; `order_check` → `ORDER RESULT PASS`.
- Wave 1 (spec/dispatch `fc79f2a4`, 38 seats, 38 reports, `.ufo/waves/round-41/build-results.json`). Seven executors wrote `plans/battery41/`
  (48 fixtures). C2 package integrated from `R41PkgEntry`/`R41PkgRows`/`R41PkgProse` with the critics' corrections appended to the entry
  (`R41CritProbe` D1–D5: RFC witnesses are LF files, lowercase failure is SUMMARY-only, `later-valid-wed-1105` is invalid, `decoy-second-vevent`
  non-discriminating, no tag for `instruction.md:21`). Independent: real pytest 3.13 parity 25/25 (`R41CritPytest`), re-derivation 25/25 + 3
  (`R41CritIndep`), probe mutants 10/10 caught (`R41MutProbe`), C2 counter mutants 22/24 (`R41MutC2Counter`).
- C1 counter limits found in wave 1 (frozen counter not edited): a probe stub can read the bound variant and steer verdicts; T03/T04 creditable
  on a dead site (`R41CritC1Counter` A1′ §3); AF_UNIX, SysV IPC, relative argv escapes (`R41SentinelCounter` F1–F4); counter guards 9/15 caught
  by committed controls (`R41MutC1Counter`). Round-40's PATH-shim vector blocked twice.
- Landing `74513c06`: battery41, C2 package, registry rows `round41-c1-mutants`, `round41-c2`, `constraints-probe`, `round-close-check` + the
  Round-41 registry addendum (round-40 closure R3/D2), QUALITY Q31/Q32, `plans/routed_open.py` + `corpus/routed-findings.jsonl` (rider).
  Measured on a clean clone (`integrate/measure-final.txt`): C1 `PREDICATE C1 pass`, C2 `PREDICATE C2 pass`; determinism receipt byte-equal
  across seeds 1/99 and jobs 1/8 (`integrate/c1-determinism-seed1-jobs1.txt`); rider `--observe` `mismatched=0`.
- Docs (`0d574196`): lesson `corpus/lessons/round-41.md`, SCORECARD round-41 section (+3 capability rows), LOG entry, planned round 42.
- Wave 2 (falsify, spec/dispatch `d7c77895`, 34 seats, 34 reports, `.ufo/waves/round-41/falsify-results.json`; integrated in `53b9e4e5`):
  attribution 23/23 (every killing fixture executes its mutated line, `F41C1Attribution`); the landed battery passes 23/23 under a hardened
  counter copy whose five repairs each bite (`F41C1Hardened`); battery reviewed 47/48 honest, 1 incidental, 0 dishonest (`F41RevBat*`); errata
  appended to the entry (9 wrong, 3 unsupported sentences, 8 overclaims — none reverses a finding), PROVINCE, QUALITY, LOG, lesson; S124 anchor
  location corrected; SCORECARD `### Wave 2 outcome` and a corrected `### Planned (round 42)`. Tip re-measure at `53b9e4e5`
  (`integrate/measure-tip2.txt`, committed `e61aff6f`): every verdict line equal to the landing measurement.
- **Hygiene incident:** wave-1 seat `R41CritIndep` ran `rm -rf -- /fast/scratch/hyaku/kengaku-r41` (the round root) at 15:42:24 -03, deleting
  running seats' clones and the L1's first baseline run (re-run). Seats informed by the L1 re-ran affected steps; recorded in the lesson
  (Mistakes) with the transcript pointer; wave 2 carried a guard sentence; unguarded by tooling (routed).
- **L1 mistake:** the first `### Planned (round 42)` paste took the planning report's title line as anchor (data walk §0–§2.2 pasted);
  superseded in-round by an appended corrected block, nothing deleted (lesson, SCORECARD wave-2 outcome).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists only `.ufo/reports/round-48/tameshi.md`
  (another lane's) beside orchestrator `.scratch/`/`.ufo/state/`; no kengaku round-41 file (`R41ScoutMisroot`, `F41ScoutMisroot`: misroot 0,
  host writes 0, `~/.local/bin` unchanged). Two seat strace receipts over the helper's size limit (`F41CritSeparability/H-c1.strace` 44 MB
  sha256 `9c86c318…`, `H-c2.strace` 1.7 MB `a537c275…`) were not committed and were removed; the seat's report quotes their content. Scratch
  `/fast/scratch/hyaku/kengaku-r41` removed by the L1 after landing.

Round shape: two v1 waves. Wave 1: 38 seats — 11 executor, 6 scribe, 5 scout, 4 critic, 4 mutation-tester, 4 connector, 2 sentinel, 2 reviewer;
m_flash roles 23/38, attack 10/38, 0 dead (38/38 reports). Wave 2: 34 seats — 13 critic, 8 reviewer, 5 executor, 4 mutation-tester, 2 connector,
1 sentinel, 1 scout; m_flash roles 19/34, attack 25/34, 0 dead (34/34 reports). Round total 72 seats, no residual call. Wave 2 dispatched after
WAVE-DONE build; report filed after WAVE-DONE falsify. Routing from the host table (run-8 map); no `model` passed.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none on the host by the L1; seats used existing `uv` (Python 3.13 + pytest 8.4.1 in scratch, `R41CritPytest`), removed with scratch.
pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `8ef8b4fc` | freeze: claims, C1/C2 counters, constraints probe, spec, dry table, captures, controls, witnesses | round 41 entry ¶1 |
| `f774a87a` | first recorded probe receipt | ¶1, C2 bullet |
| `fc79f2a4` | wave-1 spec and dispatch | ¶1 |
| `74513c06` | `plans/battery41/` (7 modules), C2 package (entry, S122–S124, README/PROVINCE/SKILL), registry rows, rider, Q31/Q32 | C1, C2, Frontier/routed bullets |
| `0d574196` | lesson, SCORECARD and LOG round-41 sections, landing measurement, census receipts | entry |
| `3d0058fb` | wave-1 reports/results (38/38), determinism and rider-observe receipts | Wave 2 bullet (wave-1 evidence) |
| `d7c77895` | wave-2 spec and dispatch | — |
| `53b9e4e5` | wave-2 reports/results (34/34); entry/PROVINCE/QUALITY/LOG/lesson errata; S124 anchor; SCORECARD wave-2 outcome + corrected plan | Wave 2 bullet, LOG erratum |
| `e61aff6f` | tip re-measure at `53b9e4e5`, final census | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round41_c1_verify.py --lane .` on a clean clone.
  - Before, at freeze (`claims/control-c1-nothing.txt`): `PINS total=2 mismatched=0`, `BATTERY fixtures=0`, `MUTANTS total=23 killed=0
    survived=23`, `MUTANTS-BY-TOOL receipts=0/13 sources=0/10`, `PREDICATE C1 fail`, exit 1.
  - After, at `74513c06` (`integrate/measure-final.txt`) and `53b9e4e5` (`integrate/measure-tip2.txt`): `BATTERY fixtures=48 wrong=0 tampered=0
    sidechannel=0`, `MUTANTS total=23 killed=23 survived=0 invalid=0 null_detected=0`, `MUTANTS-BY-TOOL receipts=13/13 sources=10/10`,
    `PINS-AFTER mismatched=0`, `PREDICATE C1 pass`, exit 0.
  - Verdict: **frozen predicate met.** Score **8 → 8 held**. The counter is forgeable by a hostile stub, so admission also rests on wave 2:
    attribution 23/23, hardened-copy 23/23, battery 47/48 honest + 1 incidental. Erratum: the count is over `plans/battery41`, not "no committed
    fixture" (the freeze's witnesses kill 23/23). The two tools advertise 58 behaviour rows; the 23 mutants price 24 (`F41CritC1Count`).
- **C2 (coverage)** — `python3 plans/round41_c2_verify.py --lane . --work <dir>` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=8 defects=5` (V2, V3, V4, V7, V8), exit 1.
  - After, at `74513c06` and `53b9e4e5`: `checks=8 defects=0`, `PREDICATE C2 pass`, exit 0; probe `cases=25 observed_pass=6 observed_fail=19
    mismatches=2`, re-run byte-equal.
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap). The frozen V1–V8 admit a content-free filler (`R41CritClaims` D2) and
    do not read the PROVINCE paragraph, §Frontier narrowing or S124; those were checked by hand at landing and by wave-2 reviewers.
- **No harm at the tip** (`measure-tip2.txt` vs baseline `measure-baseline.txt` at `fc79f2a4`): round-40 C1 `killed=21` pass, C2 pass; round-39
  C1 `killed=7` pass, C2 pass; round-38 C1 `killed=21 survived=1` as landed, C2 pass; round-37 C1 `killed=55` pass, C2 pass; round-36 C2 pass;
  anchor check `rows=117 tokens=24 defects=0`; ledger-tip `mismatches=0`; tip receipts `receipts=27 byte_equal=7 differ=0 skipped=20`; frozen
  digests (r39, r40, r41) OK; `order_check` r38 exit 1 (as before), r39/r40/r41 exit 0; `round_close.py --round 41` exit 0.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` gives 114 → 117. Tier A +2 (S122
  `constraints-scheduling/tests/test_outputs.py`, S123 `instruction.md`, terminal-bench-2 @ `2fd12b88`), tier B +1 (S124 TB2.1 PR #245, closed
  unmerged, opened live 2026-10-26 15:37 -03); all `mined`, all used by the new entry.
- Rows touched old→new: S124 anchor cell "PR body §Proposed PR description" → "PR body preamble paragraph (pr245-body.md:11; …)" (wave-2
  `F41ReopenRows` F1; logged in the lesson `## Gate changes`). Four drift-risk rows re-opened, no change (`R41SourcesRecheck`; `overdue` 0 lines).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before exit 0, `kengaku ok`,
  15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok`, 15 W04 — the same duplicate-URL-across-scopes warnings
  (`integrate/census-final.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a seventh task (7 of 89 read); one new executed edge class (a verdict computed by a
  scheduling model embedded in the grader over sha256-pinned input calendars; the graded ICS read with regexes). Knowledge files 47 → 48.
- Sourced claim: C2 (S122, S123, S124 opened this round).
- Mined mistakes (`corpus/lessons/round-41.md` §Mistakes): the vacuous planned predicate (fixed: `TOTAL`/`FLOORS`, shown able to fail by
  `control-c1-no-mutants.txt`); S10 rc-equivalence (withdrawn before freeze); a PR cited as publication without its state; the witness-copy
  loophole; a seat deleting the shared round scratch root; "no committed fixture" wording recurring; a forgeable frozen counter; the L1's
  mis-anchored SCORECARD paste; C2's filler admission.
- Assimilation: `considerthese/2026-10-26.md` proposal 1 (routed-findings burn-down) → `plans/routed_open.py` + `corpus/routed-findings.jsonl`
  (10 rows, `routed_open=5 oldest_round=39`, `--selftest` 12/12). `merge/kengaku/`: adopted nothing; package unchanged since round 40; id lists
  `build/R41MergeRescreen/reg-ids` (114) and `staged-ids` (175), collision count 38; guard proven on an indented `  | S002 |` fixture; renumber map:
  none (nothing appended); quarantine slice derived (S091, S105), not hand-checked (nothing adopted). 2 admit-candidates (benchmark cards) fit no
  round-41 claim; one now also collides with S122–S124.

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (a seventh TB2 grader, the first whose verdict is computed by an embedded
  scheduling model over pinned inputs) citing three `mined` rows; three capability rows demonstrated (`cli-exit-pair-mutants`,
  `embedded-model-grader-probe`, `routed-findings-burndown`). One instance and one edge class, not breadth.
- **quality — improved.** Two more lane tools carry a standing, attributed battery (23/23, every mutated line executed on its killer); the
  counter's predicate can no longer be satisfied by an empty list; Q31/Q32 added; the entry's 12 bad sentences and 8 overclaims were found
  in-round and corrected by appended errata, none reversing a finding. Residuals routed: counter limits F1–F4, 34 unpriced advertised rows, near
  variants killed 6/20 and 9/20, C2 filler admission.
- **discernment — unprovable-but-better at most; not `improved`.** S10 was withdrawn on a witness, the planned vacuous predicate was caught and
  bound, prior art was kept honest (S124 closed unmerged; no novelty claimed). Against that: the claims overstated "no committed fixture" and
  "no novelty candidate", the L1 mis-pasted the round-42 plan, and the C2 prose carried overclaims — all caught by the lane's own falsify wave and
  corrected by errata; the non-author closure decides.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` and `kengaku | round-33` (coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Scheduling-constraint TB2 grader — round 41 (decision table citing receipt cases) and four new registry rows; `F41CritSkill` verifies 11/11 rows and 4/4 registry commands
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 41 entry; `corpus/evidence/round41/constraints-probe.txt` (25 cases, byte-equal re-runs 3/3 in `F41C2Rerun`; real pytest parity 25/25 in `.ufo/waves/round-41/build/R41CritPytest.md`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-41/integrate/measure.sh` re-runs every claim counter and the no-harm set from a clean clone (`integrate/measure-tip2.txt`); `F41NoHarm` 25/25 verdicts equal
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round41 partial frontier admission and its routing clause (calendar/RFC 5545 conformance unowned, routed to the orchestrator; `R41ConnSibling`), wave-2 correction appended
