# kasegi — round 81 report (attempt 1)

Lane HEAD `a5269eee40b7fdb5f2f2b3e918e1197b1f35350d` (master, pushed; `git ls-remote origin refs/heads/master` prints it). Base `191e6ba8f872d08802d83b57cd7fcf4bfa122f0e`, freeze `7ad3118c86ee14fde433d73671cc407668533cec`, landing `a5269eee` (it also carries the wave results).

## Work performed

Declared claims (frozen in `.ufo/waves/round-81/claims.json` at `7ad3118c`):
- **C1 — depth:verifiability (lowest non-retired axis, 4, nominal per R58; the scored `resolve.py` citation census does not read this instrument):** land the recheck-cwd census successor `a3b58aa5…dbec0`. Score it with a new counter that has three limbs: case-matched kills on each row's declared `kill_cases`, a clean baseline, and neutral rows that must pass from a moved copy. The table has 59 rows: the 28 r80 rows, 28 new rows for the r80 routed survivors, and 3 neutral rows. Five stub forgeries that the r80 counter scores `killed=56` must exit 1 under the r81 counter. **VERIFIED (P1–P8)**, with the limits listed below.
- **C2 — coverage (8):** admit Frontier F57, OSV.dev GET /v1experimental/importfindings/{source}, on S115. S115 was opened this round and is the round's sourced claim. A new entry-content gate, B8, applies. **VERIFIED (B0–B8).**

Work items:
- History read before the freeze: the r80 closure (MANIFEST `admitted`) and `corpus/lessons/round-80-verifier-spotcheck.md`, with routed defects 1–3. The r80 seat reports ReviewC1, MutC1Hunt and CriticClaims supplied the survivor and forgery set.
- Candidate `.ufo/waves/round-81/c1/recheck-cwd-census.py` adds seven checks: prefix-literal, conform-limbs, tmpdir-file, timeout-bucket, tmpdir-unset, usage-guards and output-lines. It also adds 12 gate-predicates rows (GATE_ROWS 28→40). Census and main behaviour are unchanged.
- Counter `c1/mutbat.py` (`fa96223b…`), builder `c1/build-table.py` and table `c1/mutant-table.json` (`abcc834e…`). The old rows' `kill_cases` come from their frozen r80 `expect` prose. Forgery driver: `controls/c1-forgeries-r81.py`.
- Controls executed and committed in the freeze (`.ufo/waves/round-81/controls/`):
  - landed r80 bytes under the r81 counter: `baseline=bad killed=28 survived=28 neutral_ok=0/3`, rc 1
  - candidate: `killed=56 neutral_ok=3/3`, rc 0
  - F1–F5: rc 0 with `killed=56` under the r80 counter, rc 1 under the r81 counter (`c1-forgeries-r81.txt`)
  - C2 do-nothing: rows 56, knowledge 94
  - B8: selftest ok; the F56 positive control passes; the six-quote junk dump fails with rc 1
- Captured S115 (`corpus/source-snapshots/round-81/S115.txt`, sha256 `e304eb88…6f7f`, HTTP 200) and wrote a six-quote manifest. Not pinned:
  - the :32 status sentences, held by F51 at `osv-post-v1-query-contract.md:75`
  - the :39 case-sensitivity note, held by F51 at `:31`
  - the samples at :41 and :43
- Wave `w1` (13 seats) scored and attacked both claims; receipts are in `.ufo/waves/round-81/w1/`. Measured outcomes:
  - ExecC1Battery: P3 run twice with identical output; P4 reproduced
  - ScoutDistinct: `novel=6/6 live_sha_match=yes`
  - ReviewC2: findings F-1 and F-2, both applied before landing
- Landing receipt `.ufo/waves/round-81/l1/L1-landing-r81.txt`: P1–P8 and B0–B8 all hold on the landing bytes.
- Wave findings that falsify parts of the claims' prose. The frozen predicates hold, and these are recorded rather than turned into verdict changes:
  - **CriticClaims (a):** a table-reading forgery (`w1/CriticClaims-receipts/forgery-selfdiff.py`) scores `killed=56 … neutral_ok=3/3` rc 0 under the r81 counter. So the tally rejects the five enumerated forgeries, not every forgery. The claim's `axis_score` phrase "independence from the byte pin" overstates this; mined as M81-3.
  - **CriticClaims (c):** a one-line junk edit skips six rechecks and still keeps P1, P3 and P5 green.
  - **CriticClaims (d) and MutEntryGate:** B8 checks shape, not content. A labelled six-quote dump passes it, and only 3 of 94 admitted entries pass it.
  - **ReviewC1 Major:** row S07 kills a neighbour of the routed survivor rather than the survivor itself. The new rows are therefore 27 routed survivors plus one neighbour; all 28 survive on the r80 bytes.
  - **MutCounter:** 6 of 15 counter mutants survive every detector. None of them lets a forgery pass P3.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, c1 bytes (candidate, counter, table, builder), c2 entry gate, controls, S115 snapshot and manifest, S115 row `queued` | LOG.md `## Round 81` bullets 1–2 | `7ad3118c86ee14fde433d73671cc407668533cec` |
| `corpus/instruments/recheck-cwd-census.py` → `a3b58aa5…`; SKILL.md and instruments/README pin rows `cases=22` | LOG.md `## Round 81` bullet 4 | `a5269eee40b7fdb5f2f2b3e918e1197b1f35350d` |
| `corpus/knowledge/osv-importfindings-record-quality-feedback.md`; S115 `mined`; knowledge-expected; README F57 rows; PROVINCE F57 line | LOG.md `## Round 81` bullet 5 | `a5269eee` |
| `corpus/lessons/round-81.md` (M81-1, M81-2, M81-3); QUALITY R132; appended corrections in `corpus/lessons/round-80.md` (routed defects 1, 2) | LOG.md `## Round 81` bullet 6 | `a5269eee` |
| SCORECARD `## Round 81`; wave spec, dispatch, seat reports, results, L1 receipt, assimilation check | LOG.md `## Round 81` | `a5269eee` |

## Before → after measurements

- **C1** (measured at landing `a5269eee`). Counting command: `python3 -B .ufo/waves/round-81/c1/mutbat.py --target corpus/instruments/recheck-cwd-census.py --table .ufo/waves/round-81/c1/mutant-table.json --expect-cases 22 --work $SCRATCH`
  - Before (base `191e6ba8`, landed r80 bytes `420151fd`): `baseline=bad rows=59 killed=28 survived=28 miskilled=0 dirty=0 notderived=0 neutral_ok=0/3`, rc 1
  - After: `MUTBAT target_sha256=a3b58aa5… baseline=ok rows=59 killed=56 survived=0 miskilled=0 dirty=0 notderived=0 neutral_ok=3/3`, rc 0
  - Selftest: `cases=15` → `cases=22 failures=0`
  - Forgeries F1–F5: r80 counter `killed=56` rc 0 → r81 counter rc 1
  - Score: 4 → 4 (delta 0; nominal per R58)
- **C2** (measured at landing `a5269eee`). Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before (freeze `7ad3118c`): `rows=56 admitted=56 … registry=115`, knowledge 94, S115 `queued`
  - After: `FRONTIER-CENSUS rows=57 admitted=57 closed=57 problem-rows=0 registry=115`, `FRONTIER-PASS F57 ids=S115`, knowledge 95, S115 `mined`
  - `ENTRY-GATE-RESULT pass`
  - Score: 8 → 8 (the coverage denominator is operator-owned)
- **No axis harmed:**
  - depth:density on SKILL.md: mean 272.8 before and after
  - SCORECARD and LOG diffs are additions only

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, six inherited W04 warnings (S028 S029 S072 S076 S080 S085), rc 0 (`.ufo/waves/round-81/controls/census-start-r81.txt`)
  - Round end (after landing): `kasegi ok`, the same six W04, rc 0
- **Registry rows:** 114 → 115. One row added, tier A `docs`: **S115**, the OSV.dev importfindings page, opened 2026-11-06, HTTP 200.
- **Rows touched (old → new):** S115 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-importfindings-record-quality-feedback.md`. Logged in SOURCES `## Registry changes` and in the lesson.
- **Frontier advanced:** F56 → F57. This was the last of the R-77-F OSV experimental endpoint leads.
- **New lead:** "Properties of a High Quality OSV Record", linked from S115 (unopened).
- **Sourced claim:** C2 rests on S115.
- **Mistakes mined** in `corpus/lessons/round-81.md`:
  - M81-1 `criterion-landed-without-its-check-run`: fix shown failing on `:19` and passing on `:21`
  - M81-2 `tally-prose-unbound-to-list`: fix shown failing on "four" and passing on "three"; it backs QUALITY R132
  - M81-3 `independence-claimed-beyond-the-enumerated-forgeries`: the fix is routed and not yet shown able to fail
- **Assimilation: none.** 85 staged-id collisions (115 registry ids, 94 staged; `.ufo/waves/round-81/assimilation/`); the r77 L0 question is pending.
- **considerthese:** read (ConnectorOverlap); no still-unimplemented proposal fits.

## Trend verdicts

- **expansion: improved.** F57 adds ground the corpus did not hold: the publisher-side import-findings report, its audience, and the not-imported consequence. Before the entry, `grep -rli importfindings corpus/knowledge` was empty. Frontier 56 → 57, knowledge 94 → 95.
- **quality: improved.**
  - The landed gate kills all 56 case-matched mutants, against 28 on the base bytes.
  - The r81 counter rejects five forgery shapes that the r80 counter accepted.
  - B8 adds an entry-shape limb that a six-quote dump fails.
  - Carried limits: the table-reading forgery (M81-3), the junk edit that skips rechecks, and B8 being shape-only.
- **discernment: improved.**
  - Rejected with named held ground: the :32 status sentences (F51 :75), the :39 case-sensitivity note (F51 :31), and the samples.
  - The r80 spot-check's routed defects 1 and 2 are corrected by appended notes whose commands were re-run (R130) and are grounded in R132.
  - This still needs a non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md; the recheck-cwd pin row was updated this round (`SKILL.md:982`); author assertion.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched (`corpus/lessons/round-61.md`).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md`, F57 line appended within OSV API ground (ConnectorOverlap: fits by precedent).

## Round shape and other items

- **Shape:** one v1 wave `w1` of 13 seats (`w1-results.json`: `seats 13`).
  - Roles: executor×3, scribe×1, scout×1, reviewer×3, mutation-tester×3, critic×1, connector×1.
  - Attack seats: 7/13.
  - Dead seats: 0.
  - No residual call. Round total: 13.
- **Planner seat:** held by the L1, because the validator rejects `planner`.
- **Routed to round 82:**
  - a counter-owned second kill limb that rejects `forgery-selfdiff.py`
  - a P5 bound on the sum of the exit buckets
  - a content limb for B8
  - the main()-site S07 transform and the MutC1Hunt r81 survivors (29 survived, 25 of them real gaps)
  - the stale `:19` cite at `corpus/knowledge/osv-determineversion-cc-library-versioning.md:80`
- **Misroot sweep:** `git status --porcelain` on the fleet root shows only orchestrator `.scratch/` entries; no kasegi misroots. Scratch `/fast/scratch/hyaku/kasegi-r81` was removed.
- **Inherited state:** none; the lane was clean at round start.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** r77 staged-package id collisions (R-77-E) and the source-recheck anchor window (R-77-D), both carried and not re-filed.
