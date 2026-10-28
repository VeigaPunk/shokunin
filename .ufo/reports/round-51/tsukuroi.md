# tsukuroi — round 51 (hyaku run 11, attempt 1) — INCOMPLETE, reported honestly

Lane: `tsukuroi-shokunin`. L1: `TsukuroiR51`. Base `c0ad548a93425a3bf8813d28d92f26fe2f64b9d4` → FREEZE
`2732ee6c06108c031c4d8043239b994e0504eb2f` → w1 spec/dispatch `6d051ef06f653ca090668591ec12296c2f733fac` → AMENDMENT 1
`6abef5d0edd19e0c6d21870b6add3b4c71c5ea68` → final lane tip `912278293a5c0a2915964d53499e11e78d5d5a0b`
(`git ls-remote origin refs/heads/master` prints it).

**Status: the round did not finish.** The run hit the session request budget after wave `w1` and the pre-w2
amendment. Wave `w2` (the counted 18-seat cohort and the final falsifiers) was **never dispatched**, no claim was
measured at an integrated revision, and `WAVE-DONE w1` was not received before filing (52 of 54 w1 reports existed;
`R51CritCheatC2b` and `R51MutC2` were still running). Per the prompt this is a failed attempt; no claim is
admitted and none is narrowed. A relaunch can resume from the committed state below.

Round shape chosen: two v1 waves (`w1` 54 seats dispatched, validated policy v1; `w2` 40 seats specified in
`make-spec.py`/`w2-items.py`, not validated, not dispatched). L1 held the planner seat. Seat mix of w1: reviewer 11,
critic 12, scout 12, mutation-tester 5, executor 4, scribe 6, connector 2, sentinel 1, simplifier 1 (attack share
28/54). Dead seats: none observed; 2 seats outstanding at filing.

## Work performed

Declared claims (frozen at `2732ee6c`, `.ufo/waves/round-51/frozen/FROZEN.md`):
1. **C1 depth (lowest tied, 8)** — rows GR1-GR3 of `corpus/knowledge/btrfs-scrub-grounding-r45.md`; counter
   `check-scrub-admission-r51.py`; target `structural_ok 1, lint_ok 3, quotes_ok 3, verdicts_ok 3, seats_ok 18, marks_ok 3`.
2. **C2 operability (census-gate instrument)** — `check-selftest-matcher-r51.py` + `score-counter-cheats-r51.py`;
   target `real_pass 1, cheats 5, cheats_rejected 5, r50_cheats_rejected 0` (amended from 4 → 5 pre-w2, strictest direction).
3. **C3 adjacency (lowest tied, 8)** — `check-adjacency-table-r51.py`; the round-50 legs plus bound/exact/ancestry/recipient/override legs.
C2 and C3 are instrument claims: the census, `PROVINCE.md` and the registry are unchanged; do-nothing controls are the
round-50 counters (`before/c2-cheats-at-base.json`: r50 rejects 0/4; `before/c3-at-base.json`: `r50_blind 1`).

Items with evidence:
- Round-start sources census exit 0, 256 rows (`before/sources-census-start.txt`); end census exit 0 (`after/sources-census-end.txt`).
- New tools (committed at `2732ee6c`, hardened at `6abef5d0`): `tools/lint-grounding-r51.py`,
  `check-scrub-admission-r51.py`, `check-selftest-matcher-r51.py`, `score-counter-cheats-r51.py`,
  `check-adjacency-table-r51.py`; 11 gate-registry rows added to `SKILL.md` (6 previously missing + 5 new).
- GR2 rewritten and GR1/GR3 rewritten from the 12 uncounted w1 pre-read reports (`w1/R51W1Pre*.md`): GR2 universal
  "any call" qualified, ioctl pre-call returns listed, progress-query stated per device scrub context, cancel/suspend
  clauses and `by SR7` removed; GR1 gained the uncited support lines; GR3 gained the SIGHUP step, signal source lines,
  `-B` and the 1546-1710 handler window. New host receipt `.ufo/waves/round-51/host/host-btrfs-progs.txt`
  (`btrfs-progs 7.1-1`, `SendSIGHUP=no`, unit sha256 = S244 snapshot).
- w1 attacks that changed the instruments (Amendment 1, `FROZEN.md`): `R51RevLint`/`R51CritLintCheat`/`R51MutLint*`
  (lint tokenizer, quote, range, pin holes → lint rewritten); `R51CritCheatC2a/b`... `R51RevC2` (self-checking liar
  passed the freeze C2 counter; 18 SIGPIPE spellings missed → equivalence mutant E1, broader scan, fifth cheat);
  `R51RevC3`/`R51CritCheatC3a/b` (duplicate rows, digest-list scan, mutable checker, `--lane`, coordinated relink,
  off-master pin → new legs and override gate).
- Source re-opens (sourced claim): scouts `R51ScoutReopenS237/S240/...` and `R51ScoutS256` reports are in `w1/`; S237 and S240
  live bytes read byte-identical to their pins (`w1/R51ScoutReopenS237.md`, `S240.md`). **No SOURCES.md row was added or
  touched this round and the lesson Gate block was not written**, so no claim yet rests on a row opened *and logged* this round.
- Controls (pre-data): FREEZE batteries C1 11/11, C2 2/2, C3 7/7; AMEND1 batteries C1 26/26, C3 15/15
  (`.ufo/waves/round-51/controls/battery-summary-r51-{freeze,amend1}-c*.jsonl`). The AMEND1 C2 scorer run
  (`before/c2-cheats-at-amend1.json`) is **empty**: it was running when I cleared the shared scratch directory and was
  broken by it — my error; the amended C2 instrument has therefore *no* committed control receipt.
- Assimilation: none (not reached). `considerthese` proposal (counter-attack scoreboard): scout seat output exists
  (`w1/R51ScoutConsider.md`), not integrated.
- Misroot: one — an `edit` call on the bare name `SCORECARD.md` resolved to the FLEET repo file; the appended section was
  removed byte-exact (`git -C /home/vgpnk/Projects/shokunin diff --stat -- SCORECARD.md` is empty). Final sweep found
  no file of this lane at the fleet root.

## Landed changes

LOG.md was **not** updated this round (no LOG entry exists for round 51); SCORECARD.md carries a "Round 51 — declaration"
section (at `2732ee6c`, with the pre-amendment C2/C3 predicates; the amended ones are in `FROZEN.md` Amendment 1).
- `2732ee6c` FREEZE: tools, GR2 rewrite, SKILL registry rows, FROZEN, SCORECARD declaration, before receipts.
- `6d051ef0` w1 spec, validated dispatch (54 seats, policy v1), C1/C3 freeze batteries.
- `6abef5d0` Amendment 1: rows rewritten, lint/counters hardened, batteries extended, host receipt, w2 item draft.
- `91227829` w1 reports and receipts, amend1 batteries, A5 control fix, end sources census.

## Before → after measurements

**None taken.** The after-values are undefined because w2 and the integrated measurement did not run.
Before-values at base `c0ad548a`: C1 `lint_ok 0, quotes_ok 2` (the base entry lacks the gap block and the `* ` leader;
`before/c1-at-base.json`); C2 round-50 counter rejects 0 of the 4 original cheats (`before/c2-cheats-at-base.json`);
C3 `r50_blind 1`, all legs PASS at base (`before/c3-at-base.json`). Round-start `check-self-assessment.py`: 27 checked,
1 mismatch (K10 lesson-file count); `check-registry-coverage.py`: 6 missing (the freeze commit registers them; not re-run
at the tip). The SCORECARD axes block was **not** restated, so calibration will read mismatches until the next round.
Verdicts: C1, C2, C3 — **not measured** (neither verified nor failed).

## Sources & frontier

Registry 256 → 256 rows; census exit 0 at start and end (40 W04). No row added, no status/recheck/used-by change, no
frontier row advanced. SOURCES: unchanged this round — the lesson Gate block and any `used-by` edits were not reached.
Assimilation: none; `corpus/lessons/round-51.md` (Gate, Mistakes) was **not written**; the misroot above and the scorer-scratch
deletion are the mistakes to mine next time (captured-by: fleet-root diff check; rule: absolute paths for every edit, never
remove a shared scratch dir while a job runs).

## Trend verdicts

- expansion: **unchanged** — nothing admitted, no source row added.
- quality: **unprovable-but-better** — row defects were found and fixed and instruments hardened against 40+ named holes,
  but no counted cohort or integrated measurement confirms it.
- discernment: **unprovable-but-better** — w1 attackers falsified the freeze lint, C2 counter (self-checking liar) and C3
  counter; all are lane-dispatched seats, not an outside sample.

## SHONEN

[~] Box 1 — decision tables and cited checklist: `SKILL.md` registry rows added at `2732ee6c`; no new decision content verified.
[ ] Box 2 — end-to-end task executed and logged: not touched (no LOG entry this round).
[ ] Box 3 — instructions executable without oral context: not touched.
[ ] Box 4 — no cross-domain bleed: not touched; no sibling scope absorbed (`PROVINCE.md` unchanged).

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 questions: none. Tool installs/updates: none.
Next-round resume point: `w2-items.py`/`make-spec.py w2 6abef5d0 2732ee6c` is drafted; re-run the AMEND1 C2 scorer in an undisturbed scratch,
validate and hand off `w2`, then integrate, restate SCORECARD axes, write the lesson and LOG entry.
