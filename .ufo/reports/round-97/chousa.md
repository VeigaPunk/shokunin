# chousa — round 97 report (L1 `ChousaR97`, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`. Base `c8087ac5` (round-96 landing).
Freeze F `9a0ce201`; carrier `4de41332`; wave-forced re-freeze F2 `d84f4e1e`; F3 `1042eb97` (C2 wording only);
landing `c523b3de3768014925d50adbe14a512f552acca8` (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (2, both measured; no exploratory claim):

- **C1 `C1-SELFTEST-GRIP-R97` — operability** (lowest-scoring non-retired axis, historical 3/10): `tools/search-rerun.py
  --selftest` scored against the mutants round-96 and round-97 *seats* wrote (non-author targets), with per-case and
  outer guards so a crash is a FAIL with a summary — SCORECARD planned-r97 item 1, round-96 spot-check D2.
- **C2 `C2-ENTRY-R97` — depth**: new entry `corpus/knowledge/press-checklist-questions-r97.md`, the PRESS 2015
  checklist held question by question through Cochrane's reprint (`S225`, B) corroborated against Karolinska's
  (`S226`, C); both opened this round — the round's sourced claim. CADTH Table 9 rejected for route (`S227`, 403).

Work items:

- Protocol load: prompt §1-§8 incl. Amendments 59-65; r96 closure admitted, no fresh-start rule binds r97; round-96
  spot-check D1-D3 handled (D1 open with corrected reason, `LOG.md` Round 97; D2 → C1; D3 carried).
- Routes: all primary PRESS routes 403 from this host, `web.archive.org` TCP timeout (pre-table probes recorded in
  `corpus/lessons/round-97.md` `## Gate`); approval table `corpus/evidence/round97/egress-approval.md`; three GETs
  through `tools/capture-fetch.py` (`corpus/evidence/round57/refetch.tsv` tail; captures `347c55ba…`, `80a844fe…`).
- C1: `tools/search-rerun.py` self-test 32 → 47 (F) → 48 cases (F2), `_selftest_cases` inside an outer guard;
  battery `corpus/evidence/round97/selftest-controls-r97.py` reads the 29 `R96MutantsC1` mutants from committed round-96
  bytes via `ast`, adds s1/s2 (R96SentinelC1) and x1-x3 (R97ScribeLesson), DO_NOTHING on the base tool, the 23 r96
  mutants, 3 stand-ins, NO_WRITE with battery-start status+diff digest, r95 regression legs, named-case-line check.
- C2: entry (8 rows, 29 located quotes, 7 GNU-grep searches at base), registry rows `corpus/SOURCES.md:237-239`,
  Search log entry `corpus/SOURCES.md:421`; battery `corpus/evidence/round97/entry-controls-r97.py` (r96 groups
  re-pointed + SOLE_SUPPORT, CORROBORATION incl. Lane-cell counts, ONE_LINE).
- Do-nothing controls committed at the freeze: `before/c1-base.txt` (base tool under F battery `EXTERNAL_KILLED=10/30`,
  FAIL), `before/c2-base.txt` (entry absent, gate exit 2); at F2 `before-f2/c1-base.txt` (`10/34`, FAIL, exit 1).
- Wave: 12 seats; amendments A1-A5, B1-B12 forced by named seat artifacts (`plans/round-97.md` § Amendments);
  re-freeze F2 `d84f4e1e`, F3 `1042eb97`.
- Frontier step: SOURCES 223 → 226; 5 mistakes mined + misroot (`corpus/lessons/round-97.md` `## Mistakes`);
  QUALITY 227-228; README Round97 section; SKILL.md correction line after the r96 one (`SKILL.md:186`).

## Landed changes

| commit | contents | LOG.md |
|---|---|---|
| `9a0ce2015fa0254848f2f32f612b20caf7dc5478` (F) | tool self-test, C1/C2 batteries, entry, S225-S227, captures, refetch rows, claims, plan, before receipts, egress table, SKILL correction | Round 97 |
| `4de413323913b1df0f6de560cb678e68773b6113` | after receipts at F, wave spec + dispatch | Round 97 |
| `d84f4e1e77b681088e72f215f49a1c4e70114e02` (F2) | A1-A5 tool/battery, B1-B10 entry/SOURCES/controls, claims and plan amendments | Round 97 |
| `1042eb9706313e4c51035c1601f664cf652dbc4d` (F3) | B11 entry limit, after-f2 and before-f2 receipts | Round 97 |
| `c523b3de3768014925d50adbe14a512f552acca8` | wave evidence + results, ledger, lesson, LOG, SCORECARD, QUALITY 227-228, README, after-f3, census end, misrooted seat receipts | Round 97 |

## Before → after measurements

- **C1** (commit F2 `d84f4e1e`; C1 paths byte-identical to F3, `corpus/evidence/round97/after-f3/c1-f2-equals-f3.txt`):
  `python3 -B tools/search-rerun.py --selftest` → `SEARCH_RERUN_SELFTEST: PASS cases=48/48`, exit 0;
  `python3 -B corpus/evidence/round97/selftest-controls-r97.py --root . --work <scratch>` →
  `POSITIVE=1/1 EXTERNAL_KILLED=34/34 DO_NOTHING_REFUSED=1/1 R96_MUTANTS_KILLED=23/23 ORACLES_REJECTED=3/3 NO_WRITE=1/1 REGRESSION_R95=2/2 BASE_KILLED=10/34 CASES=48`,
  `SELFTEST_CONTROLS_R97=PASS`, exit 0 (`after-f2/c1-all.txt`). Before: base tool under the same battery
  `EXTERNAL_KILLED=10/34`, `SELFTEST_CONTROLS_R97=FAIL`, exit 1 (`before-f2/c1-base.txt`). Harm check: `verify` plain and
  `--strict` byte-identical to base on 3 records (`after-f2/c1-verify-harm-and-c2-separable.txt`).
- **C2** (commit F3 `1042eb97`): `gate-records.py verify` → `GATE_RECORDS files=1 records=30 ok=30 fail=0`;
  `research-gate.sh verify-metadata` → `METADATA_COMPLETE=1/1 RESEARCH_GATE: CLEAN`; `search-rerun.py verify` →
  `searches=7 rev_match=7/7 SEARCH_RERUN: CLEAN`; `entry-controls-r97.py` → `POSITIVE=1/1 FORGERY_REFUSED=8/8
  BINDING_REFUSED=3/3 SOLE_SUPPORT=2/2 CORROBORATION=3/3 SEARCHES=3/3 DO_NOTHING_REFUSED=1/1 ORACLE_REJECTED=1/1`,
  `LQ_BOUND=29/29 WARRANTS_OK=8/8 WARRANT_TERMS=8/8 LANE_FILLED=8/8 SOLE_SUPPORT=8/8 ONE_LINE=29/29 VERBATIM=10/26
  LETTERS=14/26`, `ENTRY_CONTROLS=PASS`, all exit 0 (`after-f3/c2-all.txt`). Before: entry absent, gate exit 2; no base
  capture line holds "Are there any spelling errors" or "orphan lines" (`before/c2-base.txt`).
- Pre-file ledger: `python3 scripts/hyaku/prefile-falsification.py --lane chousa --round 97` → `PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=8 findings=0`, exit 0.

## Sources & frontier

Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 223 before, 226 after.
Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`: start exit 0
(`corpus/evidence/round97/census-start.txt`), end exit 0 (`census-end.txt`; one new warning W01: S226 tier C mined).
Rows added by tier: A 1 (S227, rejected for route), B 1 (S225, mined), C 1 (S226, mined, corroboration only). Rows
touched old→new: none existing. Frontier advanced: README:1456's gap ("the PRESS 2015 checklist's own element
wording") held at question level through a reprint; round-96 self-test blind spots closed for the named mutants.
Sourced claim: C2 cites S225/S226. Assimilation: none (no `merge/chousa/` theme taken this round).
considerthese: not mined this round (no proposal fits the two claims).

## Trend verdicts

- **expansion: improved** — one new knowledge entry on a named gap (README:1456), three registry rows (226).
- **quality: improved** — the search-rerun gate's self-test now fails with a summary on 34 non-author mutants vs 10
  for the round-96 tool (`before-f2/c1-base.txt` vs `after-f2/c1-all.txt`).
- **discernment: improved** — two reprints measured against each other (10/26 verbatim) rather than either taken as
  the guideline; tier C kept out of sole support; a primary route rejected with a flip condition; QUALITY 227-228
  from the round's own errors.

## Round shape

One v1 wave `w1`, 12 seats (`.ufo/waves/round-97/w1-results.json`): executor 2, mutation-tester 2, reviewer 2, critic 1,
sentinel 1, scout 1, revenger 1, connector 1, scribe 1; attack seats 5/12 (42 %); dead seats 0; no residual call;
round total 12. L1 holds the canonical planner seat. Routing per `task.agentModelOverrides` (not passed).

## Ledger gate

`.ufo/waves/round-97/claim-falsification.tsv`: 16 rows, 9 `falsifies-wording` (each narrowed in `plans/round-97.md`
§ Amendments and filed on the F2/F3 sentences), 7 `neutral`. Gate line: `PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=8 findings=0`, exit 0.

## Open questions and notes

- L0: none new. Routed: D1 (refetch `S224` names two documents) needs a reader rule; R97MutantsC1's 19 uncovered
  survivors; R97SentinelC1 F1-F3 battery-wording corrections (LOG.md Round 97) — all in SCORECARD planned r98.
- Misroot: 16 `R97RevenPrior-*.txt` at the fleet root, moved byte-exact (cmp) into the lane (`corpus/lessons/round-97.md`).
- Tool installs: none.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:186` (r97 correction), `corpus/knowledge/press-checklist-questions-r97.md` decision table (no non-author verifier yet)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 97 (sources opened, entry written, searches re-run)
- [~] Instructions executable by an agent without oral context — `python3 -B tools/search-rerun.py --selftest`; `corpus/evidence/round97/after-f2/c1-all.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; entry Lane column confined
