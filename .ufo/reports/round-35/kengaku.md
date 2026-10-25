## Work performed
Round 35 declared two claims: **C1, coverage** (the lowest non-retired axis, tied with novelty at 7). It admits the pinned Terminal-Bench 2.0 `protein-assembly` grader as a knowledge entry and adds an executed offline probe. **C2, calibration**. It adds a persistent routed-defect ledger and closes the round-34 closure's defects D1–D5. Both frozen predicates pass at the final lane tip. Each claim also brings a capability row. The wave-2 falsifiers found real weaknesses in both counters; these are reported below and are not hidden.

- Freeze `11d64530179b78e33ba6074fc77d63d36ee7ac31` (lane): `plans/round-35-claims.md`, counters `plans/round35_c1_verify.py`, `plans/defect_ledger.py`, probe `plans/tb2_grader_probe.py` (18 cases with predictions), and four red controls in `.ufo/waves/round-35/claims/control-{c1-nothing,c1-skip,c2-nothing,c2-flip}.txt`. Baseline lane tip `5d0c73db` is the round-34 spot-check commit on top of `58a19f37`, which the claims file names; the only difference is +80 lines in `corpus/lessons/round-34-verifier-spotcheck.md`.
- Re-opened the six pinned files live on 2026-10-25. They are byte-identical to the round-34 captures (`build/R35ReopenPins.md`), and the round-34 `/tasks/…` URLs return 404. The probe matched all 18 predictions (`corpus/evidence/round35/tb2-grader-probe.txt`). The run is deterministic, including under Python 3.13 (`R35ProbeRerun.md`). An independent re-implementation agrees on 18/18 cases (`R35IndepGrader.md`), and running the real pytest runner in a namespace agrees on 3/3 cases (`falsify/F35PytestRunner.md`).
- C2 repairs (`dfcd294c`):
  - Deleted the 109,413 committed mirror paths under the round-34 mirror roots. History keeps them; nothing was rewritten.
  - Moved the round-34 plan drafts to `.ufo/waves/round-34/drafts/`.
  - Appended the evaluator digests to the round-34 `SHA256SUMS`.
  - Appended the SCORECARD D4 correction and the `round-34.md` S091 erratum. Live re-check: the quote is present (`R35ScoutQuarantine.md`).
  - Added QUALITY criterion Q23. This mines considerthese `2026-10-25.md` proposal 2.
- Wave-1 falsifiers found holes in the frozen counters after the freeze: a junk package passes C1 (`build/R35CritControls.md`), and false but labelled D4/D5 lines pass C2 (`build/R35CritC2.md`). The frozen rules were **not** changed. Post-hoc `plans/round35_hardening.py` fails on all 5 counterexamples (`corpus/evidence/round35/hardening-counterexamples.txt`) and is recorded as a `## Mistakes` fix only.
- Wave 2 led to appended errata (`1d4084fa`):
  - The longest passing gBlock is **2768 nt, not 2766** (`falsify/F35MaxNt.md`).
  - Findings 1 and 3 hold more narrowly than stated (`F35GOnlyLinker.md`).
  - `non-acgt-base` is a confounded case (`F35IndepWindows.md`).
  - The README's "executes test.sh" was wrong (`F35RevReadme.md`).
  - The S105/S107 anchor word counts were wrong (`F35ReopenS106S107.md`).
  - C2's green state was attributed to the wrong commit (`F35LogDraft.md`).
- Misroot sweep: the fleet `status --porcelain --untracked-files=all` shows one untracked file, `.ufo/waves/round-30/wave1/ScribeLesson.md`. It is a round-30 scribe report from another lane, so it was left untouched. No round-35 seat wrote into the fleet root.
- Inherited state: round-34's 1,425 untracked paths were resolved in `dfcd294c`. Three cited drafts and two scratch JSONLs were committed. The untracked `R34MutReadme-*` nested-repo mirrors (~10 GB) and the untracked mirror copies were removed. This was the first attempt; there was no earlier dead attempt.

## Landed changes
Lane commits, in order, with `landed` hashes from `jj-lane.sh`. All are logged in `LOG.md` § Round 35 and its errata.
- `11d64530179b78e33ba6074fc77d63d36ee7ac31`: freeze (claims, counters, probe, ledger, controls).
- `dfcd294c60a00215c55bc4ce0b620440cd5e402f`: C2 repairs, ledger closed, Q23.
- `4fe72a9aab65c59b3a740406024d928234a7e23f`: C1 package (entry `corpus/knowledge/tb2-protein-assembly-grader.md`, rows S105–S107, README index/coverage/frontier rows, `corpus/evidence/round35/`, PROVINCE round-35 paragraph, lesson, hardening script).
- `6ac9611a260d7dea20c1fccd52cbb28618c85ca5`: SCORECARD round-35 section, capability rows, LOG entry.
- `056e192a2766c9d80f33f80c6d59d321e8687902`: lesson Gate package rejects and census receipts.
- `dfee6fff631ebc5f623ba4506e5c7992a215401c`: wave-1 evidence (32 reports, spec, dispatch, results).
- `1d4084fa166798e5e0ebaf86bcf62e2b276e7550`: falsify-wave errata and wave-2 evidence.
- `e7f0decda220ccc55bac4a4ba8f3e130af73bdca`: `falsify-results.json` and final wave-2 reports (no corpus change). **This is the final lane tip.** `git ls-remote origin refs/heads/master` → `e7f0decda220ccc55bac4a4ba8f3e130af73bdca`.

## Before → after measurements
- **C1, coverage.** Command: `python3 plans/round35_c1_verify.py --lane .`
  - Before (freeze): `checks=6 defects=5`, exit 1.
  - After, at `1d4084fa`: `checks=6 defects=0`, `PREDICATE C1 pass`, exit 0. A fresh clone also passes (`F35RunC1.md`).
  - Verdict: **predicate met; score 7→7 held**, because of the L0 coverage cap (`.ufo/l0-questions.md:163`).
  - Limits: the counter does not prove the probe or the entry's content. A stub probe plus one-word quotes passes it.
- **C2, calibration.** Command: `python3 plans/defect_ledger.py --lane .`
  - Before: `rows=5 closed=0 observed_pass=0 mismatches=0`, `PREDICATE C2 fail`, exit 1.
  - After, at `1d4084fa`: `rows=5 closed=5 observed_pass=5 mismatches=0`, `PREDICATE C2 pass`, exit 0. A clone gives 5/5 (`F35RunC2.md`).
  - The predicate first held on committed bytes at `4fe72a9a`, not at `dfcd294c` (erratum).
  - Verdict: **predicate met; score 8→8 held**. Reasons: the D4/D5 checks are token co-occurrence (`falsify/F35CritC2.md`, verdict "falls" as a truth instrument), D1 is a working-tree check, and 28 recursive mirrors remain outside D2's roots (`F35MutLedgerD2.md`).
- Separability: each claim still verifies with the other reverted (`F35SeparabilityC1.md`, `F35SeparabilityC2.md`). No-harm audit: `F35CritHarm.md` reports harm-0 (`grader.py` PASS, `state_check` exit 0). Diff scope OK, and no frozen instrument changed after the freeze (`F35RevDiffScope.md`).

## Sources & frontier
- **Counts:** SOURCES rows go from **97 to 100**. Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` gives exit 0 before and exit 0 after, with 15 W04 warnings each time. Receipts: `corpus/evidence/round35/census-{before,after}.txt`.
- **Rows added by tier (A/B/C):** 3/0/0. These are S105 (`tests/test_outputs.py`), S106 (`tests/test.sh`) and S107 (`instruction.md`), all at terminal-bench-2 `2fd12b88` and all `mined`.
- **Rows touched:** two rows from this round had their anchor word counts corrected, S105 9→11 and S107 16→15. No status, recheck or used-by value changed.
- **Frontier rows advanced:** 1. The README §Frontier clause for "Terminal-Bench 2.0's" scoring code is now discharged for `protein-assembly` only.
- **Sourced claim:** C1 cites S105–S107, all opened this round.
- **Mined mistakes:** in `corpus/lessons/round-35.md` §Mistakes:
  - the S091 false refusal;
  - the committed scratch mirrors;
  - the unbacked manifest;
  - frozen counters that were weaker than the skip-control;
  - the confounded probe case;
  - plus three wave-2 rows.
- **Assimilation:**
  - considerthese `2026-10-25.md` proposal 2 was mined into C2 and Q23.
  - From `merge/kengaku/`, two entries were refused: `toolathlon-grader-behaviour-probe-2026-10-23.md` and `terminal-bench-release-identity.md`.
  - Two admit-candidates (`grader-predicate-input-types.md` and the fixture-probe amendment lineage) are **held**: the claims were frozen before the screen.
- **Id-collision check:** 97 registry ids against 175 staged ids gives 21 collisions (S077–S086, S090–S094, S097, S100–S104). The guard was proven on an indented-row fixture (`build/R35IdGuard.md`). No package row was appended. The quarantine slice is 2 rows: S091 was re-grounded (quote present) and not appended, and the staged S105 was not appended.

## Trend verdicts
- **expansion — improved.** One knowledge entry and three tier-A rows were added (knowledge 41→42, registry 97→100), on ground the lane did not hold: one TB2 task's scoring code, read and executed. Two capabilities were added: `pinned-grader-probe` and `routed-defect-ledger`.
- **quality — improved.** The round-34 D3 manifest gap was closed, and the entry carries 22 located quotes that a counter checks against the capture lines. Wave 2 found 3 numeric or wording errors in the entry; they were corrected by appended errata, not silently.
- **discernment — unchanged.** Lane seats found that both frozen counters accept junk, which is a self-calibration miss at freeze time. The post-hoc hardening is not yet a rule. A non-author closure has not run yet.

## SHONEN
[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` (unchanged this round; author-asserted)
[~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` § Round 35 (grader probe executed; receipt `corpus/evidence/round35/tb2-grader-probe.txt`)
[~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48` (unchanged)
[~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-35 paragraph; `falsify/F35ConnSiblingCheck.md` (0 contested)

Round shape: two v1 waves.
- **Wave 1 (build):** 32/32 seats spawned and reported. Roles: executor 10, scribe 6, scout 4, reviewer 3, critic 3, mutation-tester 3, connector 2, simplifier 1. Results: `build-results.json`. The orchestrator kernel restarted mid-wave, so seat outputs exist only as report files.
- **Wave 2 (falsify):** 32 seats, all settled per `falsify-results.json` (committed `e7f0decd`). Roles: executor 13, reviewer 5, scout 3, critic 3, mutation-tester 3, scribe 2, connector 2, simplifier 1.
- **Totals:** 64 seats, 0 dead, no residual call.
- **Role mix:** m_flash roles (executor, scribe, critic, simplifier) are 41/64. Attack roles (reviewer, critic, mutation-tester) are 20/64, rising to 29/64 if wave-2 executors doing mutation and verification are counted.
- **Planner:** the L1 held the planner seat.

Incident: seat F35MutReceipt reported that its `/tmp/k35f-*` fixture was deleted by someone else. It re-ran its probe and reported 4/4 kills.

Stale-lane: progressing — one round per dispatch; no other mission open.
Tool installs: biopython 1.85 was loaded through `uv run --no-project --with`. That is an ephemeral uv cache environment from the uv/PyPI channel, used because it is the grader's pinned dependency. Nothing else was installed and pacman was not used.
Open L0: `kengaku | round-33` coverage-cap decision packet (`.ufo/l0-questions.md:163`), still unanswered and routed around.
