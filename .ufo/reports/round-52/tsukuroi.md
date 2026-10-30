# tsukuroi — round 52 (hyaku run 11 continuation, attempt 1)

Lane `tsukuroi-shokunin`; L1 `TsukuroiR52`. Base `cc88b81d78bcbe06bce3f6bf722a108432ad276f` →
FREEZE `ff9470ea9ff06966a37dd91c1cbe823ffe46ecf0` → wave evidence `4ee3226daa221c72acab23eacaacc8f3c9616954` →
integration `fc2684145b4483c962bd8ca75e189483733d934d` → receipts `c5a95106f405683d79ea15ae1d3c32014827cc4f`
(final lane tip; `git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` local=remote=ahead=0).
This is a **resume round**: rounds 49-51 each closed `rejected-honest-stop` on the same depth claim; round 52
measured the frozen resume state with ONE wave and closed the two instrument debts the round-51 closure routed.

**Round-level admission: not admitted — C1 failed honestly; no axis harmed.**

## Work performed

Declared claims (frozen before any seat, SCORECARD "Round 52 — declaration", `.ufo/waves/round-52/frozen/FROZEN.md`):
1. **C1 depth (lowest tied, 8; sourced S237 S240 S242 S243 S246 S247 S248)** — the round-51 AMENDMENT-1 row
   bytes of `corpus/knowledge/btrfs-scrub-grounding-r45.md` read `holds` by a fresh counted 18-seat cohort in
   wave `w1`; counter `tools/check-scrub-admission-r52.py` (the r51 counter with wave path, R52 seat names,
   round-52 admission marks and base changed — no logic change; r51 counter sha256 in its docstring).
2. **C2 operability (instrument-measurement completion; sourced S256 + S257 opened this round)** — a VALID
   5-cheat `score-counter-cheats-r51.py` receipt in an undisturbed scratch, closing the routed round-51 defect
   (the amend1 receipt was broken by the r51 L1's own scratch deletion).
3. **C3 adjacency (lowest tied, 8; instrument-measurement completion)** — `check-adjacency-table-r51.py`
   measured at one named revision with the full leg set, closing routed defect "no named-revision measurement".

Work items with evidence:
- Round-51 routed defects closed in the freeze commit `ff9470ea`: post-hoc `corpus/lessons/round-51.md`
  (## Gate + ## Mistakes) and the round-51 LOG entry (spotcheck defect 3); inherited r51 receipt bytes moved to
  `.ufo/waves/round-52/inherited/` and the tracked file restored (defect 2); SCORECARD axes restated (K08/K09/K10
  → `check-self-assessment` 0 mismatches at freeze, `frozen/self-assessment-at-freeze.json`); SHONEN re-filed below
  (defect 4). QUALITY 95 added (misroot criterion, cites the r51 lesson).
- New source **S257** opened and registered (sourced-claim duty): GNU Bash Reference Manual, Pipelines,
  fetched 2026-10-30 by the L1 (HTTP 200, 7513 B, sha256 `b5629f04…059a`), quote and Gate block in
  `corpus/lessons/round-52.md`; anchor-opener defect found by `R52ScoutS257` and fixed pre-commit
  (`.ufo/waves/round-52/w1/R52ScoutS257.md`).
- Freeze machinery: `tools/check-scrub-admission-r52.py` + SKILL registry row; `controls/battery.py` re-derived
  for the r52 counter; **pre-data batteries all green at the freeze**: C1 26/26, C2 2/2, C3 15/15 as declared
  (`controls/battery-summary-r52-freeze-c{1,2,3}.jsonl`, battery rc 0); before-receipts in `.ufo/waves/round-52/before/`
  (census start exit 0; C1 at base FAIL `lint_ok 3, quotes_ok 3, verdicts_ok 0, seats_ok 0, marks_ok 0`;
  C3 at base all-legs PASS with `r50_blind 1`; self-assessment at base 3 mismatches).
- Wave `w1`: 64 seats, ONE v2 wave, validated rc=0 under policy v2 (`w1-validate.log`), dispatched through the
  inline ready-file handoff (`.ufo/waves/round-52/w1.ready`); WAVE-DONE received before this report was filed.
  Role mix: reviewer 23, critic 17, executor 9, scout 7, scribe 4, mutation-tester 2, sentinel 1, connector 1;
  attack share 42/64 = 65.6%. Counts: spawn 64 / resume 0 / total 64; no residual call.
- Counted outcome and per-seat attacks integrated: entry `## Gate status — round 52` section;
  `corpus/lessons/round-52.md` (Gate admits/rejects, Mistakes, the considerthese scoreboard);
  `corpus/QUALITY.md` item 96; LOG round-52 entry; SCORECARD outcome + axes restatement.

**Dead or file-less seats (4, reported not replaced, per the orchestrator recovery boundary):**
`R52CritGR1b`, `R52CritGR3b` (counted cohort; full transcript outputs, never wrote their report files — cut
mid-turn; last output text in `w1-results.json`), `R52CritLimits`, `R52ScoutArch` (empty output; provider loss
under fleet load). Two further seats ended mid-turn with partial output and no report — their items are
**unverified work**: `R52MutScorer` (scorer-mutant re-run), `R52CritHoleC3Relink` (r51 C3 hole re-run). Scratch
dirs of the mid-cut seats survived them (`/fast/scratch/hyaku/tsukuroi-r52/<seat>/`); removed by the L1 at close.

## Landed changes

All committed via `jj-lane.sh --as tsukuroi` and pushed; each tied to its LOG entry:
- `ff9470ea` FREEZE — claims/predicates/controls, r52 counter + battery, before-receipts, S257 row (queued),
  r51 lesson + LOG entry, axes restatement, QUALITY 95, inherited-residue resolution (LOG "Round 52 — declaration").
- `4ee3226d` wave evidence — spec, validated dispatch (64 seats), validate log, freeze battery receipts (LOG round-52 entry).
- `fc268414` integration — `w1/` seat reports and receipts, `w1-results.json`, entry Gate-status section,
  `corpus/lessons/round-52.md` (S257 flip queued→mined logged old→new), QUALITY 96, LOG measured outcome,
  SCORECARD outcome + final axes restatement (LOG round-52 entry).
- `c5a95106` receipts — `after/` (c1-final, c2-final, c3-final, identity proof, self-assessment 0, census end).

## Before → after measurements

- **C1 depth — FAIL.** Counting command:
  `python3 tools/check-scrub-admission-r52.py --revision <REV> --wave-dir .ufo/waves/round-52/w1 --results-file .ufo/waves/round-52/w1-results.json --dispatch-file .ufo/waves/round-52/w1-dispatch.json`.
  Before at base `cc88b81d`: `structural_ok 1, lint_ok 3, quotes_ok 3, verdicts_ok 0, seats_ok 0, marks_ok 0` FAIL
  (`before/c1-at-base.json`, measured at `cc88b81d`). After at freeze `ff9470ea` / integration `fc268414`:
  `structural_ok 1, lint_ok 3, quotes_ok 3, verdicts_ok 1, seats_ok 16, marks_ok 0` FAIL
  (`after/c1-at-freeze.json`, `after/c1-final.json`). Causes: `seats_ok 16≠18` (two cohort seats file-less) and
  bound negatives — GR2 blocked by all six bound seats (one clause family: a resume-suspended replace still
  shows in `replace_target`; dev-replace.c 1235-1242 vs 170-174/196-210), GR3 `partly` ×3 (the SIGINT
  handler-window sentence overstates the pinned caller; scrub.c 436-443/1546, out at 1712 bypassing the 1710
  reset). GR1 read `holds` by all five bound seats. No admission mark written. The next round amends two clauses
  and re-counts (replacement texts in the blocking reports and the entry's Gate-status section).
- **C2 operability — PASS measured.** Counting command:
  `python3 tools/score-counter-cheats-r51.py --revision <REV> --scratch <DIR>` →
  `real_pass 1, cheats 5, cheats_rejected 5, r50_cheats_rejected 0`, predicate PASS. Before: no valid receipt
  existed anywhere (the r51 amend1 attempt is committed broken — ERROR rows; r51 spot-check graded C2
  `unprovable`; bytes preserved at `inherited/c2-cheats-at-amend1.{json,rc}`). After: two independent valid
  receipts — seat run at the freeze (`w1/R52ExecValidC2/c2-scorer.json`) and L1 run
  (`after/c2-final.json`, revision `ff9470ea`); scorer inputs byte-identical from freeze through integration
  (`after/inputs-identity-proof.txt`: empty diff over census + both counters). Measured at `ff9470ea`,
  receipts committed at `c5a95106`.
- **C3 adjacency — PASS measured.** Counting command:
  `python3 tools/check-adjacency-table-r51.py --revision <REV>` → full-leg predicate PASS at `ff9470ea`
  (`adj_rows 7 … stub_fails 1, display_bound_ok 10, quote_specific_ok 10, digests_bound_ok 10,
  display_forge_fails 1, override_blocked 1, r50_blind 1, anchor_rows_exact 1, adj_exact 1, bare_all 0,
  ancestry_ok 10, recipient_ok 7`; `after/c3-final.json`), battery 15/15 at the freeze
  (`controls/battery-summary-r52-freeze-c3.jsonl`). Before: the counter already passed all legs at base
  (`before/c3-at-base-r52.json`) but no named-revision receipt existed; after, the receipt exists at `ff9470ea`,
  committed at `c5a95106`. Disclosed limit: 6 of 9 r51 counter mutants survive the battery (`R52MutAdj.md`).

## Sources & frontier

Registry **256 → 257 rows**: one tier-A `docs` row added, **S257** (GNU Bash Reference Manual, Pipelines; URL,
access date 2026-10-30, sha256 and ≤25-word located quote in the Gate block of `corpus/lessons/round-52.md`),
opened by the L1 this round; status `queued` at the freeze → `mined` after the lesson landed (old→new logged in
the lesson), `used-by: corpus/lessons/round-52.md`. Rows touched otherwise: none (no status/recheck/used-by
edits). Frontier rows advanced: none. Census:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
exit 0 at start (`before/sources-census-start.txt`), freeze (`frozen/sources-census-freeze.txt`) and end
(`after/sources-census-end.txt`; 40 W04 duplicate-URL warnings at every pass, unchanged).
Sourced claim: **C2** rests on S257 (this round) + S256.
Assimilation: **none** — the staged `merge/tsukuroi` package still collides with the lane registry (57 ids;
round-50 collision receipt stands) and no entry is adopted. `considerthese`: the counter-attack-scoreboard
proposal (`considerthese/2026-10-26.md`) is **landed** this round — the rounds-38-50 table with the verifier's
four convention corrections, in `corpus/lessons/round-52.md` — closing that file's last open proposal bullet.

## Trend verdicts

- expansion: **unchanged** — no knowledge entry admitted and no province Frontier row moved; the S257 row is
  curation and the scoreboard is a lesson table, not admitted entries.
- quality: **improved** — C2 and C3 measured PASS at a named revision (two routed round-51 debts closed); the
  counted cohort bound the GR2/GR3 defects precisely and GR1 read clean 5/5; the entry gained an honest
  Gate-status section with proposed replacement text; the lint stayed clean (3/3) and no previously-passing
  check regressed (`after/self-assessment-final.json`: 27/0; registry coverage 89/89). The depth row itself is
  still not admissible — recorded as FAIL, not smoothed.
- discernment: **unprovable-but-better** — the wave's falsifiers caught real defects the author had just
  accepted (GR2's clause family, GR3's window sentence), a source-row anchor defect (S257), four scoreboard
  convention miscounts (`R52RevScoreboard`), and a full-predicate forgery through the counter's declared
  overrides (`R52CritForgeC1a`); the pre-data battery and the production-path legs (`R52CritForgeC1b`) separate
  capability from measurement. Not `improved`: the required independent non-author admit/reject spot-check is
  the closure's to run — nothing this round was outside-checked in-round.

## SHONEN

[~] Box 1 — SKILL.md decision tables, error patterns, checklists with cited sources: unchanged this round except
the `scrub-admission-r52` registry row (SKILL.md `## Gate and probe registry — round46 superseding current rows`);
author-side evidence as filed in SHONEN.md; non-author verification remains owed.
[~] Box 2 — at least one end-to-end domain task executed and logged in LOG.md: the round-52 entry logs a full
claim → wave → counter → receipt cycle (LOG.md "Round 52 — measured outcome"); historical evidence unchanged.
[~] Box 3 — instructions executable without oral context: the frozen record + spec + counter + battery are
self-contained and were executed by 64 fresh seats without oral context this round; the whole-SKILL
no-oral-context retest remains unexecuted and no non-author has replayed it.
[~] Box 4 — no cross-domain bleed (PROVINCE.md still accurate): `PROVINCE.md` untouched
(`git diff cc88b81d c5a95106 -- PROVINCE.md` is empty); the mori `.cover` strays at the fleet root are mori
round-61 seats' files, named here, not absorbed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 questions: none filed by
this round. Tool installs/updates: none (pacman pause honored; no seat reported an install).
Misroot: none of this lane's files at the fleet root at close (final sweep clean; the two `count-c*.cover`
strays name mori round-61 and were left untouched). Unverified work named: `R52MutScorer` and
`R52CritHoleC3Relink` items (mid-turn cuts), `R52CritLimits` and `R52ScoutArch` (provider deaths) — none was
re-run; their absence does not affect any claim verdict above.
