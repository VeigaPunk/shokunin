# kasegi — round 80 report (attempt 1)

Lane HEAD `7629cc563dee8ad7f48b7eaaebdb860e5ddb9252` (master, pushed). Base `58905f2bbc52db6b1634566cc1be9c92cdddebfb`, freeze `4ab545865f747fca8456370b5927fe51236fe579`, landing `0039d6708158f26655ee4fad2af4893a5f6c1cb7`, wave results `7629cc56`.

## Work performed

Declared claims (frozen in `.ufo/waves/round-80/claims.json` at `4ab54586`):
- **C1 — depth:verifiability (lowest non-retired axis, 4, nominal per R58):** land the recheck-cwd census successor `420151fd…5698`. Scored by a new counter whose exception classifier keys on the `FAIL exception=` marker (QUALITY R129) against a 28-row frozen mutant table that includes the nine round-79 routed real-gap survivors. **VERIFIED.**
- **C2 — coverage (8):** admit Frontier F56, the OSV.dev POST /v1experimental/ubuntu/binary-to-source contract, on S114, which was opened this round (the sourced claim). **VERIFIED.**

Work items:
- History read before the freeze: the rejected closures r76–r79 (MANIFEST `rejected-honest-stop`) and `corpus/lessons/round-79-verifier-spotcheck.md`. Round 79 failed on a counter classifier defect (M79-2), not on its candidate.
- Built the candidate `.ufo/waves/round-80/c1/recheck-cwd-census.py` from the unlanded r79 candidate. It closes the routed survivor classes:
  - F4 constant-argument wiring finding (T1)
  - the RESULT limb's ret conjunct is fed a negative input (T2)
  - a wrong-predicate-in-consumed() row (N10)
  - the row count is bound by `GATE_ROWS` (N11)
  - new fixture entries: exit-1, exit-7 and fresh-cwd (N21, N30)
  - side-log and superset rows (N25, N26)
  - `both_headers_ok` as a two-polarity gate predicate (N27)
- Built the counter `c1/mutbat.py` (R129 classifier, plus a selftest row whose assertion FAIL mentions "exception") and the table builder `c1/build-table.py`, which writes the 28-row table.
- Controls executed and committed in the freeze (`.ufo/waves/round-80/controls/`):
  - base: `killed=0` (`baseline=bad`), rc 1
  - r79 candidate: `killed=13`, rc 1
  - print-stub forgery: `survived=28`, rc 1
  - R129 control: the r80 counter's selftest passes (rc 0); the same counter with the r79 classifier fails it (rc 1)
  - nonexistent TMPDIR: base rc 1 with a traceback; candidate rc 2
  - C2 do-nothing: rows 55, knowledge 93; S114 recheck rc 0; literal B6 0/6
- Captured S114 (`corpus/source-snapshots/round-80/S114.txt`, sha256 `e1ccfb9b…88d2`) and wrote a six-quote manifest. The ordering clause is not pinned, because F54 already holds that rule-shape.
- Wave `w1` (12 seats) scored and attacked both claims. Receipts are in `.ufo/waves/round-80/w1/`, for example:
  - `ExecC1Battery.md`: `killed=28` twice
  - `ReviewC1.md` and `ReviewC2.md`: no blocker
  - `ScoutDistinct.md`: 6/6 clauses novel; a live re-capture matched the committed snapshot byte for byte
- Integrated ReviewC2's findings F-1 to F-6 into the entry before landing.
- Wrote the landing receipt `.ufo/waves/round-80/l1/L1-landing-r80.txt`. P1–P8 and B0–B7 all hold. I re-ran P2, P3 and B3 on a `git archive` of `0039d670`, with the same results.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, c1 bytes, controls, S114 snapshot and manifest, S114 row `queued` | LOG.md `## Round 80` bullet 1–2 | `4ab545865f747fca8456370b5927fe51236fe579` |
| `corpus/instruments/recheck-cwd-census.py` → `420151fd…`; SKILL.md and instruments/README pin rows `cases=15` | LOG.md `## Round 80` bullet 4 | `0039d6708158f26655ee4fad2af4893a5f6c1cb7` |
| `corpus/knowledge/osv-ubuntu-binary-to-source-mapping.md`; S114 `mined`; knowledge-expected; README F56 row; PROVINCE F56 line | LOG.md `## Round 80` bullet 5 | `0039d670` |
| `corpus/lessons/round-80.md` (M80-1, M80-2); QUALITY R130, R131; appended corrections in `corpus/lessons/round-79.md` (routed defects 1 and 2) | LOG.md `## Round 80` bullet 6 | `0039d670` |
| SCORECARD `## Round 80`; wave spec, dispatch, seat reports, L1 receipt | LOG.md `## Round 80` | `0039d670` |
| `w1-results.json` | LOG.md `## Round 80` bullet 3 | `7629cc563dee8ad7f48b7eaaebdb860e5ddb9252` |

## Before → after measurements

- **C1** (measured at landing `0039d670`). Counting command: `python3 -B .ufo/waves/round-80/c1/mutbat.py --target corpus/instruments/recheck-cwd-census.py --table .ufo/waves/round-80/c1/mutant-table.json --expect-cases 15 --work $SCRATCH`
  - Battery before (base `58905f2`): `baseline=bad rows=28 killed=0 survived=2 dirty=1 notderived=25`, rc 1
  - Battery after: `MUTBAT target_sha256=420151fd…5698 baseline=ok rows=28 killed=28 survived=0 dirty=0 notderived=0`, rc 0
  - Selftest: `cases=6` → `cases=15 failures=0`
  - Nonexistent TMPDIR: rc 1 with a traceback → rc 2 with a named refusal
  - Score: 4 → 4 (delta 0; nominal per R58)
- **C2** (measured at landing `0039d670`). Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before (freeze `4ab54586`): `rows=55 admitted=55 … registry=114`, knowledge 93, S114 `queued`
  - After: `FRONTIER-CENSUS rows=56 admitted=56 closed=56 problem-rows=0 registry=114`, `FRONTIER-PASS F56 ids=S114`, knowledge 94, S114 `mined`
  - Base `58905f2` registry: 113
  - Score: 8 → 8 (delta 0; the coverage denominator is operator-owned)
- **No axis harmed:**
  - depth:density on SKILL.md: mean 272.8 before and after
  - the SCORECARD diff is additions only

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, six inherited W04 warnings (S028 S029 S072 S076 S080 S085), rc 0 (`.ufo/waves/round-80/controls/census-start-r80.txt`)
  - Round end: `kasegi ok`, the same six W04 warnings, rc 0
- **Registry rows:** 113 → 114. One row added, tier A `docs`: **S114**, the OSV.dev binary-to-source page, opened 2026-11-06, HTTP 200.
- **Rows touched (old → new):** S114 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-ubuntu-binary-to-source-mapping.md`. Logged in SOURCES `## Registry changes` and in the lesson.
- **Frontier advanced:** F55 → F56.
- **Remaining lead:** GET /v1experimental/importfindings (page `/osv.dev/get-v1-importfindings/`, HTTP 200).
- **Sourced claim:** C2 rests on S114.
- **Mistakes mined** in `corpus/lessons/round-80.md`, each with a show-able-to-fail pair:
  - M80-1 `routed-reason-transcribed-unmeasured`
  - M80-2 `line-cite-off-by-one`
- **Assimilation: none.** 84 staged-id collisions (114 registry ids vs 94 staged); the L0 question is pending.
- **considerthese:** read; no proposal mined.

## Trend verdicts

- **expansion: improved.** F56 adds ground the coverage map did not hold (`grep -rli ubuntu corpus/knowledge` was empty before). Frontier 55 → 56, knowledge 93 → 94.
- **quality: improved.** The landed gate kills 28/28 frozen mutants where the base killed 0. It refuses a bad TMPDIR (M77-3 closed on the lane tree), and its counter's classifier is selftested on the r79 failure case.
- **discernment: improved.** Rejected with named held ground:
  - the ordering clause (F54 `:21`)
  - the experimental-status paragraph (F51 `:75`)
  - the payload skeleton and sample values

  ScoutDistinct found 6/6 admitted clauses novel. The false r79 Q12 correction is retracted after re-running its grep (R130). This needs a non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md; the recheck-cwd pin row was updated this round (`SKILL.md:982`); author assertion.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched (`corpus/lessons/round-61.md`).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md`, F56 line appended within OSV API ground.

## Round shape and other items

- **Shape:** one v1 wave `w1` of 12 seats.
  - Roles: executor×3, scribe×1, scout×1, reviewer×3, mutation-tester×2, critic×1, connector×1.
  - Attack seats: 6/12 (50%).
  - Dead seats: 0 (`w1-results.json`: 12 seats, all reports filed).
  - No residual call. Round total: 12.
- **Planner seat:** held by the L1, because the validator rejects `planner`. A `labrat` probe was re-roled as the mutation-tester `MutClassifier` for the same reason (`unknown_role`).
- **Routed to round 81:** findings outside the frozen table, recorded in `corpus/lessons/round-80.md` § L1 verdicts and SCORECARD:
  - ReviewC1 M1 and M2
  - MutC1Hunt's real-gap survivors
  - CriticClaims (a): forgeries reach `killed=28`; only P2's byte pin excludes them
  - MutClassifier P3DEL and P3RAISE
- **Misroot sweep:** `git status --porcelain` on the fleet root shows only orchestrator `.scratch/` entries; no kasegi misroots.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** r77 staged-package id collisions (R-77-E) and the source-recheck anchor window (R-77-D), both carried and not re-filed.
