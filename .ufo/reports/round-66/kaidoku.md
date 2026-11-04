# kaidoku round 66 — lane report (attempt 1)

Lane `kaidoku` (`kaidoku-shokunin`), round 66. Base `311079d869f068bc083a8d180977e49634120fdf`; operative
freeze `7b63dd5d5199ed30bc3f213573d8594434a18eb6`; record `02d4880b9a20965f0518a44ba1d8ee686203eb74`; lane tip
`6d82aa325038fdb67f563b1ff508d0870b14d8c1` (pushed; `git ls-remote origin refs/heads/main` prints it).

## Work performed

Two declared claims, distinct axes, causally separable, each a **counter repair** — a new freeze of a
surface the round-65 non-author closure routed as a defect, never an edit of the frozen r65 bytes:

- **R66-C1 — depth.** The closure counter's boundaries: a post-probe bytecode-cache scan folded into
  `closure.ok`, the frozen 30-entry count asserted, and `--skip-run` stripped of its synthetic closure.
- **R66-C2 — calibration.** The coverage self-assessment: recipe A transcribed verbatim and re-run for
  equivalence, the hidden stems emitted as a list, and two self-assessment atoms counted as mismatches
  against the `## Owned axes` coverage row.

Both target the lane's tied-at-10.0 owned axes (calibration is the lowest-axis obligation's claimant this
round; saturation: SCORECARD `## Saturation`, window N = 10, last capability round 65 → the nudge is not
fired). No claim is exploratory; no capability row enters (both instruments repair registered capabilities —
`tools/round-65/jsc-closure-matrix.py` and `tools/round-65/coverage-recipe.py` — and are registered as gates
under QUALITY #92 instead).

Work items, each with its evidence pointer:

1. **Protocol load and carry-in.** MISSION/AXES/CORPUS/LEARNING/PROTOCOL read at round start; the r65 closure
   (`corpus/lessons/round-65-verifier-spotcheck.md`) read and recorded before any claim was designed —
   LOG `## 2026-11-03 — round 66 … carry-in`, commit `b5b02e1f`, an ancestor of the freeze
   (`l1/records/r66-order.txt`: `merge-base --is-ancestor` exit 0).
2. **Instruments written and committed before the plan** (QUALITY #33): `tools/round-66/closure-boundary.py`
   (sha256 `3c5cfb03…`) and `tools/round-66/coverage-selfcheck.py` (sha256 `1be9d046…`), with their registry
   rows in `SKILL.md` (QUALITY #92) and their do-nothing controls — commit `78fa9666`.
3. **Pre-freeze dry runs** (QUALITY #83/#84), the frozen counters themselves on frozen-shape data:
   `l1/pre/dryrun-c1-verify.json` (5/5, exit 0), `l1/pre/dryrun-c2-selfcheck-at-base.json` (equivalence true,
   hidden 3, mismatches 1, exit 1), selftests `l1/pre/selftest-c1.txt` (30 cases) and `selftest-c2.txt`
   (26 cases), both clean.
4. **Do-nothing controls before the freeze** (the phase-4 rule): `l1/controls/c1-do-nothing.json` **1 of 5**
   arms (the r65 order, the unasserted count, the synthetic skip-run), `l1/controls/c2-do-nothing.json`
   **0 of 3** conditions (the r65 date mode shares only `mapped` with recipe A, emits an integer, has no
   atoms). Committed in `78fa9666`, replayable at the freeze.
5. **Freeze** at `7b63dd5d`: `plans/round-66-claims.md` + `.ufo/waves/round-66/claims.json`, predicates
   byte-identical in plan, container, each counter's `PREDICATE` constant and the counter-emitted receipts
   (C1 `f8c8edb4…`, C2 `d5df2ccd…`; reviewer §3), instruments pinned by sha256, four frozen paths, ten atoms.
6. **One v1 wave `r66-w1`**, 12 seats under the 8–16 policy band (`.ufo/waves/round-66/r66-w1-spec.json`,
   `-dispatch.json`, `.ready`, `.ready.dispatched`; validator exit 0; 12 spawn, 0 resume). Roles: 3 executor,
   1 reviewer, 1 critic, 2 mutation-testers, 1 sentinel, 1 scout, 1 connector, 2 scribes; attack share
   4/12 = 33 %; one connector. All 12 settled, 0 dead (`r66-w1-results.json`). L1 held the planner seat
   (the validator rejects a `planner` role).
7. **`ExecClosure`** ran the frozen C1 counter once in all three modes: `--verify` exit 0, 5/5
   (`w1/ExecClosure/verify.json`); `--manifest` exit 0, `entries 30`, `count_ok true`, cache empty; `--skip-run`
   exit 1 by contract with `closure null` (`w1/ExecClosure/skiprun.json`); instrument sha256 unchanged
   before/after; toolchain cache scan 0 lines.
8. **`ExecCoverage`** ran the C2 arms at the base and the freeze: equivalence true with `diffs {}` at both,
   hidden 3, stem 145/145, atoms A1 true / A2 false (`[142,142]` vs `[145,145]`), mismatches 1, exit 1; recipe
   A at the base 145/142 with score 9.79 and depth 10.0 (27/27 blocks) (`w1/ExecCoverage/`).
9. **`ExecControls`** re-ran both controls (1/5 and 0/3, JSON-equal to the committed receipts) and three
   arm-mutations: `COUNT 30 -> 29` flips a3 and a4, scan-before-probe flips a2, a synthetic skip-run closure
   flips a5 (`w1/ExecControls/m{1,2,3}-verify.json`) — every assigned mutation flipped its arm.
10. **`MutClosure`** 5 mutants: M1–M4 killed by both detectors, **M5 survived** (`arm()` always passes; bound
    by neither detector — a controlled red separates it: pristine 2/5, M5 5/5). **`MutCoverage`** 5 mutants:
    M1/M3/M4/M5 killed, **M2 survived at a green/base revision** (an equivalence arm that returns true without
    running the block; a doctored block drives pristine `--equiv` to rc 1 with three diff keys and M2 to rc 0).
    Both survivors are selftest-coverage gaps, routed to the next freeze (`w1/MutClosure/mutants.md`,
    `w1/MutCoverage/mutants.md`).
11. **`ReviewerClosure`** traced every predicate clause to an implementing line (QUALITY #87), hunted boundary
    escapes, checked #68 predicate identity and #83/#84 dry-run shape, and disposed of the r65 reviewer's
    A1/A3/A5 residuals: no blocking finding, twelve advisory (`w1/ReviewerClosure/review.md`).
12. **`CriticClaims`** ran five attacks. A: a counter without the ordered post-probe check scores 5/5 with a
    byte-identical a2 detail — **counter fails as a witness**. B: a5 is an in-process literal and a1's count
    clause an identity; a counter whose `--skip-run` emits `closure.ok true` still passes a5 — **counter fails**.
    C: equivalence outside `RECIPE_A_KEYS` — **holds today**, latent closed-world tolerance named (`policy`).
    D: row shapes reaching `mismatches 0` — **counter fails** (R2 keeps a stale `142/142` behind a fresh
    fraction; R4 keeps a stale baseline after a multi-arrow score cell). E: the base arm is false for the
    stated numeric reason — **holds** (`w1/CriticClaims/attacks.md`, `evidence/`).
13. **`SentinelScope`** audited five surfaces clean: write scope (14 paths, all lane-relative), no credential
    material, toolchain closure green with 105 files (delta 0 vs the r65 freeze), frozen paths byte-equal at
    freeze and tip, registry rows 7 cells with no escaped pipe (`w1/SentinelScope/audit.md`).
14. **`ScoutSources`** opened the round's source once: CPython `sys.dont_write_bytecode`, HTTP 200, 280617
    bytes, sha256 `572c354e…`, 18-word located Gate quote, dt raw line 585, nearest heading the module h1
    (`w1/ScoutSources/{row.md,gate.md,fetch.json}`) → row **S267**, tier A docs, admitted under its own scope.
15. **`ConnectorCross`** found no sibling owner for the recipe-A reproduction or a closure-count assertion;
    the self-assessment *class* is owned by tsukuroi and souji, but neither computes a knowledge fraction or a
    rounded score — the class precedent is cited and the atoms are not claimed novel as a class
    (`w1/ConnectorCross/overlap.md`).
16. **Scribes** produced the knowledge entry, its coverage-map row, the r65 erratum and the lesson draft
    (`w1/ScribeKnowledge/`, `w1/ScribeLesson/draft.md`); the L1 landed them with the S267 provenance and the
    measured numbers.
17. **One of the lane's own mistakes, mined with a red/green demonstration** (M66-3): the first C1 control run
    shared one fixture between its arm and its r65-order emulation and reported a false pass. Re-produced
    fresh: `l1/records/m66-3-contamination.{py,json}` (`red_demonstrated true`: one root "meets" the a2 arm,
    two roots do not).
18. **Census at round start and round end**: `l1/census-start.txt` (exit 0, 173 rows, 19 W04) and
    `l1/census-end.txt` (exit 0, 174 rows, 19 W04).
19. **Misroot sweep** before the report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
    `.scratch/` driver files (orchestrator-owned), `.ufo/reports/round-75/kake.md` (another lane) and an
    untracked `after` (24 bytes, mtime 20:05, before this round's first commit at 21:09) — none names kaidoku
    or round 66, so none is a misroot of this round and none was touched.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| carry-in: the r65 non-author closure recorded before any measurement (QUALITY #34) | `## 2026-11-03 — round 66, KaidokuR66 — carry-in` | `b5b02e1f` |
| the two repaired counters; their `SKILL.md` registry rows (QUALITY #92); their do-nothing controls and pre-freeze dry runs | `## 2026-11-03 — round 66, KaidokuR66 — landing` (registry paragraph) | `78fa9666` |
| the claims file, the plan with both predicates, the pins and atoms, the freeze | `## 2026-11-03 — round 66, KaidokuR66 — landing` | `7b63dd5d` |
| the coverage row re-derived; S267 + the knowledge entry + its coverage-map row; the r65 erratum; QUALITY #104–#106; the r65 report correction | `## 2026-11-03 — round 66, KaidokuR66 — landing` and `— correction: the round-65 report's …` | `5de8a1de` |
| the single-fraction coverage row; the round lesson with M66-1…M66-7 and the routed witness gaps; the wave evidence; the after-arm receipts | `## 2026-11-03 — round 66, KaidokuR66 — record` (SCORECARD round-66 section) | `02d4880b` |
| the close: both after-arms re-measured at the record, census end, the routed gaps named | `## 2026-11-03 — round 66, KaidokuR66 — close` | `6d82aa32` |

The SCORECARD round-66 section, the coverage row and the capability decision are carried by `5de8a1de` and
`02d4880b`; the r65 knowledge entry's erratum is appended (no filed byte rewritten); `LOG.md` is additions
only; `SKILL.md`'s delta is exactly the two registry rows (`git diff --numstat 311079d8 6d82aa32 -- SKILL.md`
→ `2 0`).

## Before → after measurements

**R66-C1 (depth).** Counting command:
`python3 -I -B tools/round-66/closure-boundary.py --verify --repo . --out RECEIPT` (exit 0 verified / 1 not /
2 could-not-evaluate).
- Before (do-nothing control, the r65 instrument's own semantics, same five arm conditions):
  `l1/controls/c1-do-nothing.json` → **1 of 5** arms (`passed 1`, `arms_total 5`, `ok false`); the r65
  `--manifest` on a one-entry-short copy exits 0 at `entries 29, ok true`, and its `--skip-run` emits
  `closure.ok true`.
- After: `w1/ExecClosure/verify.json` at the freeze `7b63dd5d` → **5 of 5**, exit 0;
  `l1/scores/c1-after-verify-at-record.json` at the record `02d4880b` → **5 of 5**, exit 0. Arm-mutations
  flip their arms (`w1/ExecControls/m{1,2,3}-verify.json`), and the selftest is 30 cases clean.
- Verdict **verified**, with routed witness gaps M66-5/M66-6 (the arms do not prove the ordering by
  themselves; a5's observation is the CLI receipt).

**R66-C2 (calibration).** Counting command:
`python3 -I -B tools/round-66/coverage-selfcheck.py --selfcheck --rev REV --out RECEIPT` (exit 0 verified /
1 not / 2 could-not-evaluate).
- Before at the base `311079d8`: `l1/pre/dryrun-c2-selfcheck-at-base.json` → `recipe_a_equivalent true`,
  `recipe_a_hidden 3`, stem 145/145, atoms A1 true / A2 false (`[142,142]` vs `[145,145]`),
  **`mismatches 1`**, exit 1; the do-nothing control 0 of 3.
- At the freeze `7b63dd5d`: identical (`w1/ExecCoverage/selfcheck-at-freeze.json`) — the row is not repaired
  yet by construction.
- After at the record `02d4880b`: `l1/scores/c2-after-selfcheck-at-record.json` → `recipe_a_equivalent true`,
  `recipe_a_hidden 4`, stem 146/146, atoms A1 `10.0`/`10.0` and A2 `[146,146]`/`[146,146]`,
  **`mismatches 0`**, exit 0.
- Verdict **verified**, with the routed atom weakness M66-7 (first-match/last-arrow; the landed row is
  single-fraction and single-arrow so the frozen atom reads the only claim in it).

## Sources & frontier

Census command, run at round start and round end from the fleet root:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.

- **Round start** (`l1/census-start.txt`): **exit 0**, 173 rows
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 173), 19 W04.
- **Round end** (`l1/census-end.txt`): **exit 0**, 174 rows, 19 W04 (the standing duplicate-url warnings,
  S033 … S248, unchanged), tier `A=160 B=9 C=5`, status `mined=165 rejected=9`.
- **Rows added by tier:** one row, tier **A** (`docs`): **S267** — CPython 3 documentation,
  `sys.dont_write_bytecode`, opened this round (HTTP 200, 280617 bytes, sha256 `572c354e…`; dt raw line 585,
  dd raw lines 587-591; 18-word located Gate quote; nearest heading the module h1 — the page carries no h2).
- **Rows touched old→new:** S267 written `queued → mined` in the same landing commit, `used-by
  corpus/knowledge/2026-11-03-r66-closure-boundary.md` (logged in the lesson and the LOG landing entry).
  No other row's status, recheck or `used-by` changed.
- **Frontier rows advanced:** the `.jsc` route under a complete closure (coverage-map ground held by r65) now
  carries a boundary battery and a self-assessment counter; the new entry's map row is the frontier pointer
  (held as instrument repair, not promoted to core).
- **Assimilation:** none this round — the `merge/kaidoku/` jsc theme was adopted in round 64, no remaining
  staged theme fits two counter repairs, and a bulk append is refused by CORPUS.md rule 4; `considerthese/`
  is absent (`ls considerthese` exit 2, recorded in `w1/ScoutSources/gate.md`).
- **Gate evidence for S267:** `w1/ScoutSources/gate.md` and `fetch.json` (URL, access date 2026-11-03,
  locator, quote, word count, tier category).

## Trend verdicts

- **expansion: improved.** One admitted `corpus/knowledge/` entry on the mapper-closure ground
  (`2026-11-03-r66-closure-boundary.md`), provenance trio citing mined S267, with its coverage-map row; the
  source is a new kind for this ground (the interpreter's own attribute page, re-opened under its own scope
  after r65's anchor-level reject). Registry 173 → 174; census exit 0 at both ends.
- **quality: improved.** The r65 closure's routed counter defects are repaired and demonstrated red/green
  (controls 1/5 and 0/3 before; 5/5 and mismatches 0 after; three arm-mutations and five-plus-five mutants
  scored); the r65 entry's group-table count slip is closed by an appended erratum; no admitted entry was
  found false. Two mutation survivors and three critic attacks are disclosed and routed rather than patched.
- **discernment: improved.** Two mutation-testers and one critic found real gaps in the round's own
  instruments before the L1 read them (a2's cause unbound, a5's in-process literal, the row atoms'
  first-match); the lane routed its own survivors, kept the frozen predicates unchanged, and chose a
  single-fraction row shape the frozen atom can actually certify. Outside closure verification remains
  pending and is not self-certified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — decision tables
  and error-pattern lists present throughout `SKILL.md`; this round adds two instrument-registry rows
  (`tools/round-66/closure-boundary.py`, `tools/round-66/coverage-selfcheck.py`) with verdict maps,
  self-test commands and pins. Author-asserted; a non-author `[x]` remains operator-owned.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's two counter repairs run
  end to end on the retained `.jsc` toolchain and the lane's own corpus (`w1/ExecClosure/verify.json`,
  `l1/scores/c2-after-selfcheck-at-record.json`), logged in the landing/record/close entries.
- [~] Instructions executable by an agent without oral context — both counters carry docstrings with modes,
  exit classes and limits; the plan and the claims container carry the traceable predicates and atoms; the
  registry rows carry entry commands and self-test spellings.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged base → tip
  (`git diff --numstat 311079d8 6d82aa32 -- PROVINCE.md` empty); the sibling-owned self-assessment class is
  reported, not absorbed (`w1/ConnectorCross/overlap.md`).

## Report extras

- **Stale-lane:** this round was a respawn-per-round driver dispatch; no other mission of this lane is open.
  The mission was open from the driver's launch to this report without exceeding two driver ticks.
- **Tool installs:** none. Nothing was installed or upgraded this round; `pacman` was not run.
- **Round shape:** one v1 wave `r66-w1`, 12 seats (policy band 8–16), attack share 4/12 = 33 %, one connector,
  no residual call, round total 12 seats, 0 dead. Dead-seat note: `r66-w1-results.json` records
  name/agent/note/output per seat only (no seat ids, no status field), so "0 dead" rests on all twelve
  outputs being present and every seat's report file existing in `w1/`.
- **Earlier attempt:** `.ufo/watchdog.log` shows no `lane-dead-no-report kaidoku round=66` line; no inherited
  uncommitted outputs existed at round start.

## Erratum — appended after the filed bytes (PROTOCOL corrections clause, 2026-11-03)

- The **Landed changes** table's `5de8a1de` row omits one change that commit carries: the **round-66
  SCORECARD section** (the claims table with both frozen predicates, the receipts paragraph, the two mutation
  survivors, the reviewer/sentinel/connector/sources paragraphs, the wave and trend lines, and the `planned`
  field) is in `5de8a1de`, pointed to by the LOG entry the same row cites
  (`## 2026-11-03 — round 66, KaidokuR66 — landing`, whose files-touched line names "SCORECARD.md (the coverage
  row head and the round-66 section)"). Check: `git -C kaidoku-shokunin show --stat 5de8a1de -- SCORECARD.md`
  lists the file, and `git -C kaidoku-shokunin show 5de8a1de:SCORECARD.md | grep -c '^## 2026-11-03 — round 66'`
  prints `1`. The `02d4880b` row is accurate as filed (the single-fraction row rewrite, the lesson, the wave
  evidence and the after-arm receipts). No other row changes.
