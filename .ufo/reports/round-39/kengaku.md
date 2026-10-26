# kengaku — round 39 report (hyaku run 8, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read at start `b2bdd425fbc042d3075994dae60fe88a51e277ab`
(the round-38 L1 then landed `ef2fba06` at 03:37:53, so the freeze is that commit's child; it moved no frozen input — lesson header);
frozen claims `plans/round-39-claims.md` (freeze `088f7c36e94ce2f15e6f9aa0c5a5c5b75a1646c8`); first recorded probe run
`6a1eb5e1da4a435940b821e28530c31f3411549c`; final lane hash `9d3aff94b0d7dbea2c2a6a3d04da7524633ffc91`
(`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR39`; the L1 holds the canonical planner seat (the
validator rejects `planner`; the round-40 planning data-walk rode scout `R39PlanNext`). Earlier attempts: none
(`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=39` line).

## Work performed

Declared claims (2), frozen with red controls before any battery39 fixture and before the first recorded probe run:

- **C1 — calibration (owned, 8):** the gate behaviours `plans/pkg_gate.py` advertises that the batteries still did not demonstrate
  after round 38 — 7 frozen mutants M01–M07 (round-38 N21 carried as `mirror`; six round-38 wave-2 survivors), each with a
  pre-freeze direction witness (Q29), two new exit-code legs (`rc-silence`, `rc-mirror`), battery38/39 modules built in child
  processes; counter `plans/round39_c1_verify.py`.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break):** the pinned Terminal-Bench 2.0
  `git-leak-recovery` grader admitted as `corpus/knowledge/tb2-git-leak-recovery-grader.md` with a 25-case bubblewrap probe
  (`plans/git_leak_probe.py`), rows S117/S118; counter `plans/round39_c2_verify.py` (round-38 V1–V7, inputs pinned).

Work items:

- Protocol load: the round prompt, `skill://godspeed`, `skill://swarm`, MISSION, AXES, SCORECARD `### Planned (round 39)`
  (`SCORECARD.md:1365-1373` at baseline), the round-38 report and non-author spot-check (`corpus/lessons/round-38-verifier-spotcheck.md`
  §5, R1–R7), round-38 wave-2 reports, `.ufo/waves/round-38/build/R38PlanNext.md`.
- TB2 task files fetched by the L1 at the pin 2026-10-26 03:27 -03, seven captures + `SHA256SUMS`
  (`corpus/evidence/round39/tb2-git-leak-recovery/`).
- Freeze `088f7c36`: claims, both counters, probe, frozen dry table (`cases=25 predicted_pass=13 predicted_fail=12`), captures,
  controls (`.ufo/waves/round-39/claims/`): C1 nothing `killed=3 survived=4`, exit 1; C1 gate-edited `invalid=7`; C1 hostile
  in-process module `killed=3 survived=4` (unchanged); C2 nothing `checks=7 defects=4`, exit 1; census-before exit 0, 15 W04;
  `frozen-digests.txt`. Before the freeze the probe ran only `--dry` and `--stage-check` (grader never imported); the C2 control's
  P10 stopped at `receipt unreadable` (`plans/pkg_gate.py:268-270`).
- First recorded probe run `6a1eb5e1` on a clean clone of the freeze: `cases=25 observed_pass=13 observed_fail=12 mismatches=0`,
  second run byte-equal (`.ufo/waves/round-39/first-run/first-run.txt`).
- Wave 1 (spec/dispatch `75047384`, 36 seats, 36 reports, `.ufo/waves/round-39/build-results.json`).
- C1 battery (`34158b0c`): four executor seats wrote `plans/battery39/` (one fixture per surviving mutant: `p1m` M02, `p3m39` M03,
  `p7m39` M04, `d5m39` M07). Landing on a clean clone of `34158b0c` (`.ufo/waves/round-39/integrate/measure-final.txt`): `PINS
  total=26 mismatched=0`, `BATTERY fixtures=90 wrong=0 renamed_disagree=0 sidechannel=0`, `MUTANTS total=7 killed=7 survived=0
  invalid=0 null_detected=0`, `PREDICATE C1 pass`, exit 0.
- C1 counter limits found in wave 1 (`build/R39CritC1Counter.md`): A1 a daemon flips a fixture's spec between phases, A3 an unpinned
  `plans/battery37/*.py` file is imported in-process (the docstring's isolation sentence is false for that directory), A4 pins hashed
  once, A5 child-reported dirs trusted — each reaches `PREDICATE C1 pass` with a dishonest battery. The frozen counter is not
  edited. Post-hoc `plans/round39_c1_audit.py` (L1, not the frozen rule) re-checks kills, closes the battery37/38 name sets,
  re-hashes pins after the run and uses parent-owned fixture dirs: landed battery `AUDIT C1 clean`; A1 replay `AUDIT C1 dirty`
  (`integrate/audit-a1-replay.txt`); A3 replay refused, exit 2 (`integrate/audit-a3-replay.txt`). Wave 2 then showed a phase-aware
  daemon keeps the audit `clean` (`falsify/F39SentinelAudit.md`), so C1 admission rests on the frozen predicate plus non-author
  review of the four modules (`F39RevBatP1/P3/P7/D5`: honest 4/4; `F39MutBattery`: fixture mutants caught 12/12).
- C2 package (`34158b0c`): `R39PkgEntry` drafted entry, rows, README lines (its clone `checks=7 defects=0`); the L1 integrated them
  with the prior-art section rewritten from `R39ScoutPriorArt` (sources opened: TB's nop-validation contract
  `TASK_REVIEW_AUTOMATION.md:244`, two third-party nop-reject runs, one LLM audit that names and dismisses the reflog gap, no
  upstream issue; two round-38 snippets refused as not found), finding 9 from `R39CritFsckReflog` (git `fsck --lost-found` clears
  `include_reflogs`, `builtin/fsck.c:905-908` at v2.56.0 / `:950-953` at v2.43.0 — why the oracle passes and the untouched repo
  fails only the flag test), contestable tags and case-text corrections from `R39CritProbe` (frozen table not edited). Landing:
  `checks=7 defects=0`, `PREDICATE C2 pass`. Independent: real pytest 8.4.1 25/25 (`R39CritPytest`), re-derivation 25/25
  (`R39CritIndep`), probe mutants 7/7 (`R39MutProbe`), counter mutants 11/11 (`R39MutC2Counter`). PROVINCE round-39 paragraph,
  README index row + coverage bullet + §Frontier sub-bullet (5 of 89), SKILL decision section + three registry rows.
- Frontier / routed (`34158b0c`): `plans/order_check.py` + QUALITY Q30 (R3; considerthese 2(b)): round 38 `ORDER RESULT FAIL` exit 1,
  round 37 FAIL, round 39 PASS (`measure-final.txt`); `## Errata (round 39)` on `corpus/lessons/round-38.md` (R3) and on three TB2
  entries (R4, corrected recheck commands green); anchor check binds each digest to its own locator (R5a, `R39AnchorUnion`, tip
  `rows=111 tokens=19 defects=0`); ledger-tip prints the audited revision and refuses a stale master (R5b, `R39LedgerProvenance`,
  `REF AUDIT … state=match`, `rows=9 … mismatches=0`); direction check redundant leg (R2, `R39DirCheckLeg` 3/3); PROVINCE sibling
  deferral of secret-removal procedure to kagi/souji (`R39ConnSibling`). R1 was closed by the round-38 L1 in `ef2fba06`
  (`git ls-files .ufo/waves/round-38/falsify | wc -l` → 428); `R39R38Integrate` maps its 34 reports / 97 findings.
- L1 mistake caught in-round: appending R4 errata to `tb2-protein-assembly-grader.md` (the round-35 genuine package every battery
  copies) broke battery38 `p7m` (`SETUP … expected exactly one 'recheck:', found 5`); reverted before any commit, recorded in the
  lesson (Mistakes row 2), reproduced by `F39RevErrata` §F4.
- Docs (`a6832f53`, `6081f60c`): lesson `corpus/lessons/round-39.md` (+ wave-2 errata), SCORECARD round-39 section (+2 capability rows,
  `### Wave 2 outcome`, `### Planned (round 40)`), LOG entry; entry `## Errata (round 39, wave 2)` (5 unsupported sentences, 2 claim
  cells, 6 overclaims corrected by appended lines; `F39EntryQuotes`, `F39CritOverclaim`).
- Wave 2 (falsify, spec/dispatch `acf43754`, 34 seats, 34 reports, `.ufo/waves/round-39/falsify-results.json`; integrated in
  `6081f60c`). Tip re-measure at `6081f60c` (`integrate/measure-tip2.txt`): same numbers for every counter.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists no file written by a kengaku
  round-39 seat (entries are orchestrator/other-lane state: `.ufo/state/*`, `.scratch/`, `.tower/`, `demo-cwd.txt` (content
  `/home/vgpnk/Projects/shokunin`, no kengaku reference), `.ufo/waves/round-30/wave1/ScribeLesson.md`); `F39ScoutMisroot`: misroot 0.
  Scratch: two seat dirs left (`R39MergeRescreen`, one wave-2 seat) — seat defects; the L1 removed `/fast/scratch/hyaku/kengaku-r39`
  after landing. One uncited 2.3 MB download a seat left in its report dir (`build/R39SourcesRecheck/scipyjson.json`, sha256
  `a9536ee9…`) was deleted, not committed.

Round shape: two v1 waves. Wave 1 has 36 seats: 8 executor, 8 critic, 7 scribe, 5 scout, 3 connector, 2 reviewer,
2 mutation-tester, 1 sentinel; m_flash roles 24/36, attack 12/36, 0 dead (36/36 reports). Wave 2 has 34 seats: 12 critic,
8 reviewer, 5 executor, 5 mutation-tester, 2 connector, 1 scout, 1 sentinel; m_flash roles 18/34, attack 25/34, 0 dead
(34/34 reports). Round total 70 seats, no residual call. Wave-2 seats were dispatched after WAVE-DONE build; the report is
filed after WAVE-DONE falsify.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none on the host. pytest 8.4.1 (+ pluggy 1.7.0, pygments 2.21.0) into scratch `uv venv -p 3.13` by seats
`R39CritPytest`, `R39CritProbe` (PyPI via uv, removed with scratch); docker base image `ubuntu:24.04` run by `R39CritFsckReflog`
to check apt git 2.43.0 (no task image); biopython 1.85 via `uv run --with` for the gate's P10 (ephemeral). git 2.56.0,
bubblewrap 0.13.1 already installed. pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `088f7c36` | freeze: claims, C1/C2 counters, probe, dry table, captures, controls | round 39 entry ¶1 |
| `6a1eb5e1` | first recorded probe receipt | ¶1, C2 bullet |
| `75047384` | wave-1 spec and dispatch | ¶1 |
| `34158b0c` | `plans/battery39/` (4 modules), C2 package (entry, S117/S118, README, PROVINCE, SKILL), order gate, anchor/ledger/direction fixes, Q30, errata, post-hoc audit, wave-1 reports | C1, C2, Frontier/routed bullets |
| `a6832f53` | lesson, SCORECARD and LOG round-39 sections, landing measurement, census after, audit replays | entry |
| `acf43754` | wave-2 spec and dispatch | — |
| `6081f60c` | wave-2 reports/results, entry and lesson errata, SCORECARD/LOG wave-2 outcome | Wave 2 bullet |
| `9d3aff94` | tip re-measure at `6081f60c` | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round39_c1_verify.py --lane .` on a clean clone.
  - Before, at freeze (`claims/control-c1-nothing.txt`): `PINS total=26 mismatched=0`, `BATTERY fixtures=86 wrong=0 renamed_disagree=0
    sidechannel=0`, `MUTANTS total=7 killed=3 survived=4 invalid=0 null_detected=0`, `PREDICATE C1 fail`, exit 1.
  - After, at `34158b0c` (`integrate/measure-final.txt`) and `6081f60c` (`integrate/measure-tip2.txt`): `BATTERY fixtures=90 wrong=0
    renamed_disagree=0 sidechannel=0`, `MUTANTS total=7 killed=7 survived=0 invalid=0 null_detected=0`, `PREDICATE C1 pass`, exit 0.
  - Advertised-behaviour mismatch count (recount `F39CritC1Count`: 5 of 7 mutants reach an advertising sentence): 2 → 0.
  - Verdict: **frozen predicate met.** Score **8 → 8 held** (the counter alone is gameable; admission rests also on the non-author
    battery review, 4/4 honest).
- **C2 (coverage)** — `python3 plans/round39_c2_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=7 defects=4` (V2, V3, V4, V7), exit 1.
  - After, at `34158b0c` and `6081f60c`: `checks=7 defects=0`, `PREDICATE C2 pass`, exit 0; probe `cases=25 observed_pass=13
    observed_fail=12 mismatches=0`.
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap).
- **Frontier fix shown able to fail:** `python3 plans/order_check.py --lane . --claims plans/round-38-claims.md --receipt
  corpus/evidence/round38/build-pmars-probe.txt` → `ORDER RESULT FAIL`, exit 1; round 39 → `ORDER RESULT PASS`, exit 0.
- **No harm at the tip** (`measure-tip2.txt`): round-38 C1 `killed=21 survived=1` as landed, round-38 C2 pass, round-37 C1 `killed=55`
  pass, round-37 C2 pass, round-36 C2 pass, anchor `defects=0`, ledger-tip `mismatches=0`, tip receipts `byte_equal=4 differ=0`,
  census exit 0, frozen digests 9/9 OK; `F39CritNoHarmDiff`: 0 removed lines in lane-authored docs.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` gives 109 → 111. Tier A +2 (S117
  `git-leak-recovery/tests/test_outputs.py`, S118 `git-leak-recovery/instruction.md`, terminal-bench-2 @ `2fd12b88`), both `mined`,
  both used by the new entry; opened 2026-10-26. Tier B/C: +0.
- Rows touched old→new: none (four rows re-opened by `R39SourcesRecheck` as drift-risk picks, none due; status/recheck unchanged).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before exit
  0, 15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok` (`integrate/census-after.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a fifth task (5 of 89 read); one new executed edge class (graded
  state = a repository's refs, reflog, object store and dangling objects plus a flag file and a work-tree digest).
- Sourced claim: C2 (S117, S118 opened this round).
- Mined mistakes (`corpus/lessons/round-39.md` §Mistakes): the order-of-operations recurrence closed by a gate (shown red on rounds
  37 and 38); the L1's erratum on load-bearing fixture bytes (caught by the C1 counter's SETUP refusal, reverted); the C1 counter's
  isolation overclaim; the `adv`-cell count (corrected to 5 of 7 in the wave-2 errata); the separability sentence.
- Not done as frozen: the claims' frontier sentence says the order class would be recorded with `recurrence=2` in
  `corpus/defects.jsonl`; its checker is the round-35 frozen counter `plans/defect_ledger.py`, which has no check for the class,
  so the row was not written (lesson Mistakes row 1; routed to round 40).
- Assimilation: `considerthese/2026-10-25.md` proposal 2(b) → `plans/order_check.py` + Q30. `merge/kengaku/`: adopted nothing;
  re-screen admit-candidate 2 (card family, deferred), hold 42, refuse 21 (`build/R39MergeRescreen.md`). Id lists
  (`build/R39MergeRescreen/reg-ids` 109, `staged-ids` 175), collision count 33 (S077–S086, S090–S094, S097, S100–S116), guard
  proven on an indented `  | S002 |` fixture; renumber map: none (nothing appended). Quarantine slice derived, not hand-checked
  (nothing adopted).

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (a fifth TB2 grader, the first whose graded state is a git
  repository's history), S117/S118 `mined`, two capability rows entered with demonstrations (`repo-history-grader-probe`,
  `order-of-operations-gate`). One instance and one edge class, not breadth.
- **quality — improved.** Routed defects closed with receipts: R3 (gate red on both prior occurrences, lesson errata), R4
  (three corrected recheck commands green; the fourth recorded in the lesson because its file is fixture bytes), R5a/b, R2's
  direction-check leg; the new entry re-verifies (probe byte-equal 3/3, real pytest 25/25) and carries its wave-2 errata.
  Residuals routed, none an admitted statement found false: `order_check.py` catches 2 of 6 mutants (`F39OrderGateMut`), the
  audit is defeatable by a phase-aware daemon (`F39SentinelAudit`), `tip_receipts.py` skips the new receipt (`F39TipReceipts`).
- **discernment — unprovable-but-better at most; not `improved`.** Last round's routed items became gates, errata and a
  witnessed-direction rule, and the L1 caught its own load-bearing-bytes erratum before commit. Against that, the freeze
  overclaimed the counter's isolation, the `adv` count and separability (all found by wave 1/2, corrected by appended errata,
  not relabelled); the non-author closure decides.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` (coverage cap, novelty conversion) and `kengaku | round-33` (decision packet
for the coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Repository-history TB2 grader — round 39 (decision table, rows citing receipt cases) and registry rows git-leak-probe / round39-c1-mutants / round39-c2; `F39CritSkill` verifies 12 of 15 rows
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 39 entry; `corpus/evidence/round39/git-leak-probe.txt` (25 cases, byte-equal re-runs; real pytest parity 25/25 in `.ufo/waves/round-39/build/R39CritPytest.md`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-39/integrate/measure.sh` re-runs every claim counter, the audit, the order gate and the no-harm set from a clean clone (`integrate/measure-tip2.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round39 partial frontier admission, its report-out and the secret-removal deferral to kagi/souji (`build/R39ConnSibling.md` §1)
