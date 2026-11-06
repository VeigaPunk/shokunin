# kengaku — round 98 (hyaku run 15, attempt 1)

## Work performed

Declared claims (frozen at F `e1a3afd9069a19e38fd0bc3b015970231f303fc7`, `plans/round-98-claims.md`):
**R98-C1 — coverage** (lowest non-retired axis, L0 cap 7): a sixteenth located offline replay of a pinned
Terminal-Bench 2.0 grader, `regex-chess`. **R98-C2 — freshness** (ceiling 10, exercised): 39 SOURCES rows
whose digests name committed nested replay captures that the frozen anchor-digest gate could not bind are
re-verified through one provenance file. No gate, row or capture byte changes.

- Protocol load: lane prompt, SKILL/SCORECARD/LOG tails, `corpus/lessons/round-97.md` and
  `round-97-verifier-spotcheck.md` (routed defects 1–5 dispositioned in `corpus/lessons/round-98.md`
  §Round-97 routed defects), QUALITY Q79–Q81, `skill://swarm`, `skill://godspeed`. The last three closures are r95
  admitted, r96 rejected-harmed and r97 rejected-honest-stop, so no pause or fresh-start rule applies.
- P0 `5584a6f7`: eight regex-chess files captured flat (`corpus/evidence/round98/tb2-regex-chess/`, HTTP 200,
  `SHA256SUMS`), 12 mechanism predictions (`.ufo/waves/round-98/L1/predictions-mechanism.txt`), census start rc 0
  (`L1/census-start.txt`).
- P1 `350d0e59`: `plans/round98_regexchess_probe.py`, `plans/round98_c1_replay.py`,
  `plans/round98_c2_nested_bind.py`, `plans/round98_provenance_build.py`, control runners, dry runs 1–3
  (`L1/dryrun/README.md`: two verdict-parsing failures, then 12/12), C2 BASE population (`L1/c2-pop.txt`).
- P2 `c71f04e6`: 6 C1 and 9 C2 controls. Each battery ran twice, and the verdict lines agreed (Q80,
  `L1/controls/README.md`). Candidate bytes were retained.
- F `e1a3afd9`. C = T `8e37fc65d5649bb37166fdd6b1657445a8cb55b9` holds only the candidate files and the official receipt
  (`L1/freeze-tip.txt`: 13/13 instruments and 4/4 candidates match). Measurement receipts are in `363fa03c`.
- Integration `4654ffc1`: `corpus/knowledge/tb2-regex-chess-grader.md`, `corpus/README.md` coverage-map rows,
  `corpus/lessons/round-98.md`, QUALITY Q82/Q83, wave spec/dispatch. Harm battery, outside-population census,
  final verification and census end are in `f90cf415`.
- Wave w1: 11 seats (3 executor, 2 reviewer, 1 critic, 2 mutation-tester, 1 scout, 1 connector, 1 scribe;
  5/11 attack). All seats settled with no dead seats (`.ufo/waves/round-98/w1-results.json`). Settlement commit
  `4a5dc030`.
- L0 `kengaku | round-98` appended (coverage-cap ruling, mined from `considerthese/2026-11-05.md` §1 proposal 5).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| P0 capture, predictions, case table, census start | `LOG.md` Round 98, bullet 1 | `5584a6f7d157ba491d6c64909bfe3c0670f46778` |
| P1 instruments, runners, dry runs, population | bullet 1 | `350d0e59faceebdc53ccf338bcac8df54020d58e` |
| P2 controls ×2 | bullet 1 | `c71f04e6167fe0a5acbed27239a9120de7a87cf1` |
| F frozen claims | bullet 1 | `e1a3afd9069a19e38fd0bc3b015970231f303fc7` |
| C ledger flip, SKILL class cells and four registry rows, S326–S333, `corpus/evidence/PROVENANCE.md`, probe receipt | bullets 2–3 | `8e37fc65d5649bb37166fdd6b1657445a8cb55b9` |
| measurement receipts (C1/C2 at T and BASE, freeze integrity) | bullets 2–3 | `363fa03caffcd558ad0709c5c625924a84457ab8` |
| knowledge entry, README rows, lesson, Q82/Q83, wave spec | bullet 4 | `4654ffc1c3d129dcc08caff9b76017e2152d5680` |
| harm battery, outside-population census, final verification, census end, lesson M4 | bullet 5 | `f90cf4157c256705c463acb9e7eda5ee6604f3de` |
| wave reports and results, knowledge corrections, lesson wave findings and M5, SCORECARD, LOG | bullets 6–9 | `4a5dc030ba7dcf2398f2a5c424757b812cca2225` |

The lane HEAD is `4a5dc030ba7dcf2398f2a5c424757b812cca2225`. `git ls-remote origin refs/heads/master` prints that hash.
Operator commit `febd88b9` (`considerthese/2026-11-06.md`) landed between P1 and P2. It is not lane work, and no
round-98 instrument reads it.

## Before → after measurements

**R98-C1 (coverage).**
- Command: `python3 plans/round98_c1_replay.py --lane . --rev REV --work DIR --grader-venv G`
  (G = `uv venv -p 3.13` + `pytest==8.4.1 chess==1.11.2`).
- BASE `49a1c4f1`: `PREDICATE R98-C1 fail`, rc 1 (`L1/c1-base.txt`; ledger executed 41 of 88).
- T `8e37fc65`: `LEGS L1..L10=pass`, `TARGET executed_rows=42 member=regex-chess
  cells=file-artifact:33,serialization-schema:8 set_equals_base_plus_member=1 located=1 executed=1 cases=12
  legs=60 mismatches=0 new_rows=8 new_rows_flagged=0 defects=0`, `PREDICATE R98-C1 pass`, rc 0 (`L1/c1-tip.txt`).
  The same result holds at `4654ffc1` (`L1/final-verification.txt`).
- Independently reproduced by ExecC1 (also two probe reruns, all 12 DETAIL digests rebuilt, C04/C07/C09 re-run
  under real pytest), ReviewC1, CriticClaims, ScoutSources and ScribeLesson.
- Located grading gaps:
  - C04: a missing legal move hides behind a duplicate. On the start position, g1f3 is dropped and g1h3 is doubled.
  - C07: an invented en-passant square passes through the `rpartition` fallback.
  - C09: a 103-entry lookup table of the three public games passes.
- MutC1: 18/18 input mutants killed; the survivors are counter self-integrity and unread informational receipt
  fields, which are routed.
- Verdict: **met**. Score 7 → 7, held at the L0 cap; an operator ruling is requested.

**R98-C2 (freshness).**
- Command: `python3 plans/round98_c2_nested_bind.py --lane . --rev REV --work DIR`.
- BASE: `TARGET pop=39 cleared=0 still=39 unbound=39 …`, fail, rc 1 (`L1/c2-base.txt`).
- T: `LEGS K1..K7=pass`, `TARGET pop=39 cleared=39 still=0 unbound=0 rows_changed=0 captures_changed=0
  new_old_row_defects=0`, `PREDICATE R98-C2 pass`, rc 0 (`L1/c2-tip.txt`).
- Re-verification result: the gate `python3 plans/anchor_digest_check.py --lane .` drops from 86 to 45 findings.
- Independently reproduced by ExecC2 (an own 39/39 check that does not use the round-98 counter), ReviewC2,
  CriticClaims, ScoutSources and ScribeLesson.
- Verdict: **met on the frozen predicate, with a disclosed finding**. The URL column of the provenance file also
  reaches the gate's provenance-URL fallback. That clears two rows outside the population (S213 `anchor-unbound`;
  S230 `digest-wrong-capture`) and re-binds two clean rows (S237, S272), so 41 findings clear, not 39
  (`L1/outside-pop-census.txt`, ReviewC2 F1–F3, CriticClaims C2-1).
- No (sid, class) pair is new at T, and every token involved resolves to its true capture bytes. The effect was
  undeclared, and K7 cannot see removals. It is recorded as lesson M4 and not repaired in round, per the freeze
  rule. The round-99 fix is a three-column provenance table or a symmetric census.
- MutC2: 21/29 mutants killed; the survivors are routed.
- Score 10 → 10.

**Harm.**
- L1 battery: 23 standing checks, BASE vs `4654ffc1` (`L1/harm/summary-4654ffc1.txt`). Every rc is unchanged.
  Finding counts are unchanged except two:
  - anchor 86 → 45 (cleared);
  - r82-c3 sweep 29 → 30: `STATUS-LINE-MISSING regex-chess` in an already-red gate. Every new member produces
    this frozen-declaration delta; r97 recorded 27 → 28.
- ExecHarm (22 checks, BASE vs T) found no green→red and no new DEFECT.
- The r97 C1 standing counter still passes at `4654ffc1` (`L1/harm-r97-c1.txt`).

## Sources & frontier

- SOURCES rows: **317 → 325**.
  - Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at
    `49a1c4f1` and `8e37fc65`.
  - Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
    Start: `kengaku ok …/corpus/SOURCES.md`, rc 0 (`L1/census-start.txt`). End: the same, rc 0
    (`L1/census-end.txt`, and again at `4a5dc030`). Only the 30 pre-existing W04 warnings appear.
- Added by tier: A 7 (S326–S332), B 1 (S333).
- Added by status: 5 mined (S326–S330); 3 rejected (S331–S333), each with its flip stated.
- Rows touched old→new: none. The diff is insert-only, and C2 reports `rows_changed=0`.
- Frontier advanced:
  - `regex-chess` moved from unexecuted to executed (ledger 41 → 42).
  - 39 nested-capture digest claims moved from unverifiable to gate-verified.
- Sourced claim: R98-C1 rests on S326–S330, opened 2026-11-06. `corpus/lessons/round-98.md` §Gate records the
  URL, access date and a ≤25-word located quote for each row, and the knowledge entry cites them.
- ScoutSources re-opened all 8 new rows and 5 population rows live; bytes, sha and quotes agree (13/13).
- Mistakes mined: `corpus/lessons/round-98.md` M1–M5 (verdict channel, capture binding, operator interleave,
  provenance side channel, prediction-timing wording). Q82 and Q83 are added from M2 and M1.
- Assimilation: none (inherited `merge/kengaku/` hold, L0 `kengaku | round-54`).
- considerthese: `2026-11-05.md` §1 proposal 5 → L0 `kengaku | round-98`.

## Trend verdicts

- **expansion: improved.** New knowledge entry `corpus/knowledge/tb2-regex-chess-grader.md` covers ground the
  coverage map did not hold: generated-set grading by per-line membership plus a count, a forgiving last-field
  fallback, and fixed public positions. It is indexed in `corpus/README.md`. The C1 counter measures the ledger
  move 41 → 42.
- **quality: improved.** The unchanged gate now re-verifies 39 previously unverifiable digest claims against
  committed bytes (86 → 45 findings, no new pair). ScribeLesson corrections A–E were applied to the knowledge entry,
  and Q82/Q83 were added. The standing battery is unchanged apart from the disclosed per-member r82-c3 delta.
- **discernment: unchanged.** This round's gate made 5 admit and 3 reject decisions, and the in-lane seats agree
  13/13. Seats a lane dispatches still count as the lane (LEARNING.md), and the outside spot-check is
  closure-owned. The provenance side effect (M4) was found by seats after freeze, not by the L1 before freeze.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` class cells and `round98-*` registry rows at `8e37fc65`; reuse rule in `corpus/knowledge/tb2-regex-chess-grader.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — official regex-chess replay `corpus/evidence/round98/regexchess-probe.txt`, `LOG.md` Round 98; reproduced by ExecC1 (`.ufo/waves/round-98/w1/ExecC1.md`).
- [~] Instructions executable by an agent without oral context — frozen commands in `plans/round-98-claims.md`, re-run unaided by eight wave seats (`.ufo/waves/round-98/w1/*.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; ConnectorOverlap §2 finds no sibling-lane overlap.

Round shape: one v1 wave (`ufo-wave-policy.json`, band 8–16) with 11 seats; 5/11 attack seats (2 reviewer,
1 critic, 2 mutation-tester) and 1 connector. There was no residual call, so the round total is 11 seats.
Dead seats: none. The L1 held the planner seat; ConnectorOverlap carried the bounded planning data-walk (§3
next-replay ranking).

Stale-lane: respawn-per-round driver; no other kengaku mission is open.

Inherited uncommitted state at start: orchestrator markers `.ufo/waves/round-97/w1.ready{,.dispatched}`. They are
not lane-authored and were left untouched.

Misroot sweep: fleet `git status --porcelain` shows orchestrator `.scratch/run15-*`, unattributed `w4lines.txt`
and this round's own L0 append. No seat wrote a file at the fleet root.

Tooling: no host install or upgrade. Preinstalled uv 0.13.0 staged CPython 3.13.16, pytest 8.4.1 and chess 1.11.2
(plus rdflib 7.1.4 for the r97 harm re-run) from PyPI into `/fast/scratch/hyaku/kengaku-r98/` for pinned grader
reproduction. That scratch is removed. pacman, sysctls and services were untouched.

Open L0: `kengaku | round-98` (coverage cap). Inherited: `kengaku | round-54` hold.
