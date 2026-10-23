# kotodama — round 57 report (hyaku phase 4, attempt 1, L1 KotodamaR57)

## Work performed

Declared claims (2), each with one frozen predicate (`reports/round-57/claims.json` at declaration `13226c18`, claim base `0314aa98`):
- **C — coverage** (learning claim, sourced claim): new myth-symbol entry `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`; predicate ACCEPT-C-57 (`reports/round-57/accept-c.py`, nine legs incl. live LOCATE and FRESH). Surface: frontier → core, a topic with 0 filename owners at base.
- **O — operability** (capability): `tools/check-gate-quotes.py` reports numeric references without `;` and its selftest kills the three round-56 survivor mutants; predicate ACCEPT-O-57 (`reports/round-57/accept-o.py`, seven legs, run without `--seed`). Surface: the checker's reference grammar and its selftest's kill set.

Work items:
- Repair first (round-56 rejection): rebuilt O's acceptance — run-time generated lessons (random ids, names, hosts, labels, filler from lesson prose, random HTML5 names), a REAL leg on injected copies of `corpus/lessons/round-56.md`, in-process mutants with neutral patches; skip-the-work and shortcut control receipts committed before data: `reports/round-57/telemetry/controls-o.txt` (16/16 as expected; the exact round-56 S-id cheat `reports/round-57/controls/sidcheat-tool.py` fails; the critic's honest green passes) and `controls-c.txt` (7/7; the sourceless stub passes eight legs and fails only LOCATE). Commits `6f08c494`, `51726fa6`, `0c16d15d`, revised `0314aa98`, `13226c18`, `286288f4`.
- Pre-dispatch critics CriticClauseListO57 / CriticClauseListC57 broke the first drafts (seed replay, `Seat: Gen.` keying, identity selftest; echo/search URLs, two-word quotes); instruments revised before any seat built (`.ufo/waves/round-57/predispatch/`).
- O landed `43f1e781` (built by ExecGateBareNumeric, sha256 `54981859`); C landed `78d83b5e` (42 rows S413-S454, all cited).
- Routed spot-check items: koon1244 and R56-M3 errata; S410 effective URL (superseding S491); carried row findings re-opened by six reviewers, superseding rows S481-S490; QUALITY criterion 10 amended (third-party scans); `reports/round-56/accept-c.py:18` SyntaxWarning fixed (raw docstring, stdout byte-identical) — records commit `89b94b69`.
- Residual falsify (8 seats, `.ufo/waves/round-57/residual/`): O re-run 3× PASS and source-edit mutants killed; 7/7 grammar mutants killed; C re-run PASS / base FAIL; separability 0 findings; CriticEntry57 disagreed (fixes applied in `89b94b69`, rest carried); row re-opens found cell defects carried as superseding rows owed.

## Landed changes

| commit (landed) | change | LOG |
|---|---|---|
| `6f08c494` | claim instruments | LOG round 57 |
| `51726fa6`, `0c16d15d` | declaration, control receipts, dry-run | LOG round 57 |
| `0314aa98`, `13226c18`, `286288f4` | instruments revised after pre-dispatch critics (no data yet), revised declaration and dry-run | LOG round 57 |
| `43f1e781` | claim O: `tools/check-gate-quotes.py` | LOG round 57 (O) |
| `78d83b5e` | claim C: entry, `corpus/README.md` rev 2.14, SOURCES S413-S454 | LOG round 57 (C) |
| `89b94b69` | records: lesson, entry falsify fixes, S481-S491, QUALITY c10, r56 raw docstring, SCORECARD, LOG, lessons index, wave records, final measures | LOG round 57 |

Lane tip `89b94b694ac6b06bf69b787166bc0bdd1a8bb848` (pushed by `jj-lane.sh`).

## Before → after measurements

- **C** — `python3 -B reports/round-57/accept-c.py`: at `13226c18` exit 1, `ACCEPT-C-57: FAIL` (SET count=232, SWEEP rows 232, FLOOR cited=0, LOCATE cited=0) (`reports/round-57/telemetry/declaration-dry-run.txt`); at `78d83b5e` exit 0, `ACCEPT-C-57: PASS`, cited 42, LOCATE 40/42 and 42/42 on two live runs, need 34 (`reports/round-57/telemetry/final-measures.txt`; residual RerunAcceptC57 40/42).
- **O** — `python3 -B reports/round-57/accept-o.py`: at `13226c18` exit 1, `ACCEPT-O-57: FAIL` (GEN 5/5 and REAL 3/3 failing, MUTANTS three survivors); at `43f1e781` exit 0, `ACCEPT-O-57: PASS`, selftest 38/38 → 52/52 (final-measures at `78d83b5e`; residual RerunAcceptO57 3/3 PASS).

## Sources & frontier

- `grep -c '^| S[0-9]' corpus/SOURCES.md`: 412 → 465. Added: 42 claim rows S413-S454 (tier A 34, B 8 incl. community 3), status mined; 11 superseding rows S481-S491 (queued) for S359, S367, S383, S385, S392, S395, S396, S399, S407, S379, S410. No status/recheck/used-by edits to old rows (append-only).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`: start `kotodama ok`, exit 0 (`reports/round-57/telemetry/census-start.txt`); end `kotodama ok`, exit 0 (`census-end.txt`; W04 warnings only).
- Mined mistake: R57-M1 (found-then-parked claim sizing behind the round-56 rejection), shown able to fail by the committed `sidcheat` control; R57-M2, R57-M3 (misroot moved byte-exact). Sourced claim: C cites only rows opened this round.
- Gate rejects (reasons in the lesson): Kashgari 1982 archive.org upload and an MA thesis on islamawareness.net (third-party scans, amended criterion 10); a law report upload; pl.wikipedia (tier C); CODH bukan (not locatable); three Wayback captures not located.

## Trend verdicts

- **expansion: improved** — new ground (identity marks, 0 filename owners), 42 mined rows, one new checker behaviour.
- **quality: improved** — O's acceptance now defeats seven named shortcuts before data; selftest kills its three survivors; row re-opens and the entry critic's high findings applied; remaining cell defects carried, so not every quality signal is clean.
- **discernment: improved** — criterion 10 amendment used to reject three build rows; two pre-dispatch critiques adopted before data; residual entry critic's disagreement recorded and acted on.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:5`; registry now 465 rows.
- [~] End-to-end domain task logged — `LOG.md` round 57 (sources → entry → closure-ready receipts).
- [~] Instructions executable without oral context — residual seats re-ran both predicates from committed paths in fresh clones (`.ufo/waves/round-57/residual/`).
- [~] No cross-domain bleed — entry §2 one-way pointers, §14 lore handoff NON-CANON (`heraldry-emblems-identity-marks.md`).

## Round shape and seats

Default two-wave shape with the falsify part run as a residual call: pre-dispatch 2 critics (CriticClauseListO57, CriticClauseListC57); wave 1 build 50 seats validated under policy v1 (30 scout, 6 reviewer, 4 scribe, 4 critic, 3 connector, 3 executor; `.ufo/waves/round-57/build-dispatch.json`); no wave 2 (fewer than 32 attack items remained); residual 8 seats (4 reviewer, 2 critic, 1 mutation-tester, plus 1 reviewer). Round total 60. Planner seat: the L1 (validator rejects `planner`). Dead seats: none. HOLD `kotodama51-prereg-critic` respected (not recreated). Misroot: ScoutPolishClanArms wrote at the fleet root; moved byte-exact into the lane, fleet copy deleted (R57-M3). Fleet-root untracked files `s395.txt`, `bm.json`, `live_s228.html`, `nama.html`, `tf_bavelas.html` predate this round's dispatch and were not touched.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (pypdf 5.4.0 used ephemerally via `uv run --with`, the locator's declared PDF path). Open L0 questions: none new.
