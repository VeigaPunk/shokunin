# kaidoku — round 31 (attempt 1)

Lane tip `f2f5977b8266d8233927fe1f1a77507df59c26fa` (pushed). Base `c369242fee9f559f895e3f7956b1242076c7b1be`. In-session hyaku L1, dispatched 03:52Z, filed about 04:50Z.

## Work performed

Declared claims (frozen at `35ba7c52`, `.ufo/waves/round-31/claims.json`, before any REA run on a carrier or request):
- **R31-C1, coverage.** The surface is PROVINCE Core, which gains REA's SQLite reader (`inspect-sqlite-database` / `inspect_sqlite_database`). The reader runs at scope `database` on 12 published SQLite files: 5 PROJ `proj.db` from pyproj wheels, 2 Chinook v1.4.5 databases, and 5 pyogrio GeoPackages that carry R*Tree virtual and shadow tables. Each result is compared with an independent reader.
- **R31-C2, depth.** The surface is a SKILL.md decision table of 23 refusal and edge outcomes (20 refusals, 3 acceptances). All 23 were predicted from the 6.5.0 code before any run.

Anti-loop: round 30 worked REA's Rust reader. This round moves to a different frontier area, the SQLite reader, and keeps round 30's admitted shape.

Lowest axis: coverage, depth and calibration are tied at 10 and none is retired. On a tie every owned axis is a lowest axis, so both claims satisfy the rule. The basis was stated in `claims.json` before data.

Work items:
- Instruments were written before the freeze:
  - `tools/round-31/sqlite_oracle.py`: a pure-Python `sqlite_schema` b-tree parser plus libsqlite3 PRAGMAs.
  - `tools/round-31/c1-sqlite-positive.py`: compares the full committed envelope and checks that the Core row is placed under a Core heading.
  - `tools/round-31/c2-sqlite-refusals.py`: compares the full committed envelope, which repairs M30-3.
  - The 12 carriers and the mutants were made `chattr +i` before any seat ran.
- Before receipts: both counters exit 2 at the base (`.ufo/waves/round-31/before/c1-sqlite-positive-at-c369242f.txt`, `.ufo/waves/round-31/before/c2-sqlite-refusals-at-c369242f.txt`).
- Pre-data control wave w1 (44 seats). The receipts were committed at `7474d269`, before the data commit `f368a101` (`.ufo/waves/round-31/controls/receipts.tsv`). No control met a target:
  - C1: do-nothing, junk-row, all-false, no-reader and the id-rotated shortcut all scored 0 of 12. A Core-placement shortcut that used real envelopes still failed `province_ok`.
  - C2: predictions copied as observations scored 0 of 23; the same control scored 16 of 19 in round 30. All-accept scored 0, and the id-rotated shortcut scored 1 of 23.
- Data: 35 live REA 6.5.0 envelopes at `f368a101`. The entries, the PROVINCE row, the SKILL table, SOURCES S092–S097, QUALITY rows 52–56 and the lesson landed at `0007731e`.
- Falsify wave w2 (38 seats) found no break in either claim:
  - Six seats re-derived all 12 C1 envelopes with non-oracle readers. All matched except one GeoPackage note: REA does not expand virtual-table columns, by design.
  - Four seats re-checked all 23 C2 rows.
  - Two seats re-ran the counters independently.
  - Six seats re-opened S092–S097. All six rows were admitted. S092's used-by was incomplete and has been fixed.
  - A live REA 6.7.0 probe confirmed the predicted budget-refusal drift.
  - Corrections were appended to both entries (`## Wave-2 corrections`).
- Round-30 routed defects 1–8 are dispositioned in `corpus/lessons/round-31.md` (section "Round-30 routed defects"):
  - Defect 1, gate PASS claims without committed receipts: `tools/round-31/cited-runs-gate.py` exits 1 on the round-30 report (`.ufo/waves/round-31/after/cited-runs-gate-round30-report.txt`).
  - Defect 2: the full-envelope check described above.
  - Defects 3 and 4: corrections appended to the round-30 refusals entry.
  - Defect 5: the owned-axes rows were refreshed to the `c369242f` recount.
  - Defect 6: the placement check.
  - Defect 7: a correction appended to the round-30 lesson.
  - Defect 8: a docstring-only fix to the round-29 counter, plus a supersession entry.

## Landed changes

| commit | content | LOG.md |
|---|---|---|
| `35ba7c52` | freeze: instruments, carriers, predictions, before receipts | round-31 entry |
| `7474d269` | control receipts, freeze-integrity gate, w1 reports | round-31 entry |
| `f368a101` | data: 12 C1 + 23 C2 envelopes | round-31 entry |
| `0007731e` | entries, PROVINCE Core row, SKILL table, SOURCES S092–S097, QUALITY 52–56, lesson, round-30 defect fixes | round-31 entry |
| `1288285e` | SCORECARD round-31 section, LOG, round-29 supersession | round-31 entry |
| `16c00c2d` | w2 reports, wave-2 corrections, settle ledger | round-31 entry (correction line) |
| `f2f5977b` | tip receipts, S092 used-by separator | round-31 entry |

## Before → after measurements

- **R31-C1**
  - Counting command: `python3 -I -B tools/round-31/c1-sqlite-positive.py --root <LANE> --rev <REV>`.
  - Before: exit 2 at `c369242f` (`.ufo/waves/round-31/before/c1-sqlite-positive-at-c369242f.txt`).
  - After: `carriers=12 pass=12 target=12` with exit 0, at `0007731e` (`.ufo/waves/round-31/after/c1-sqlite-positive-at-0007731e.txt`) and at `16c00c2d` (`.ufo/waves/round-31/after/c1-sqlite-positive-at-tip-16c00c2d.txt`).
  - Unmoved command at the base: `git show c369242f:PROVINCE.md | grep -c -E 'inspect[_-]sqlite[_-]database'` gives 0.
- **R31-C2**
  - Counting command: `python3 -I -B tools/round-31/c2-sqlite-refusals.py --root <LANE> --rev <REV>`.
  - Before: exit 2 at `c369242f` (`.ufo/waves/round-31/before/c2-sqlite-refusals-at-c369242f.txt`).
  - After: `requests=23 matches=23 target=23` with exit 0, at `0007731e` (`.ufo/waves/round-31/after/c2-sqlite-refusals-at-0007731e.txt`) and at `16c00c2d` (`.ufo/waves/round-31/after/c2-sqlite-refusals-at-tip-16c00c2d.txt`).
- Commit `f2f5977b` changes only `corpus/SOURCES.md`, the lesson and receipts. Neither counter reads those files.
- Freeze integrity: `freeze-integrity: CLEAN` at the tip (`.ufo/waves/round-31/after/freeze-integrity-at-tip-16c00c2d.txt`).
- Settle ledger: `settle: PASS` (`.ufo/waves/round-31/after/settle-gate.txt`).
- Write-mode runs are committed under `.ufo/waves/round-31/data/`. They are not receipts (M31-3).

## Sources & frontier

- SOURCES rows went 91 → 97 (`grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`).
- Rows added by tier: 6 at tier A:
  - S092: rea-agents 6.5.0, `dist/sqlite` code.
  - S093: PyPI records for pyproj 3.4.1–3.7.1.
  - S094: the Chinook v1.4.5 release.
  - S095: the PyPI record for pyogrio 0.11.1.
  - S096: the SQLite file format spec.
  - S097: the SQLite PRAGMA docs.
- Rows touched old→new: S092 used-by changed from the refusals entry alone to the refusals and positive entries (lesson Gate).
- Census:
  - Round start: `.ufo/waves/round-31/before/sources-census-start.txt` shows `kaidoku ok`, exit=0. It was run at 04:21Z, after the freeze; SOURCES.md was unchanged from the base at that time.
  - Round end: `.ufo/waves/round-31/after/sources-census-end.txt` shows `kaidoku ok`, exit=0. It adds one expected W04 for S092, which shares the 6.5.0 tarball URL with S083 and S090.
- Sourced claims:
  - C1's entry cites S096, S097, S093, S094 and S095.
  - C2's entry cites S092.
  - All six rows were opened this round.
- Mined mistakes: M31-1 to M31-8. Four fixes are shown able to fail:
  - M31-1: the multi-spelling grep finds l7-04.
  - M31-2: freeze-integrity exits 1 on the amended-predictions clone (`.ufo/waves/round-31/controls/freeze-integrity-ctl-rewritepred.txt`).
  - M31-4: the cited-runs gate exits 1 on the round-30 report.
  - M31-6: the cited-runs selftest failed before its fix (`.ufo/waves/round-31/after/cited-runs-gate-selftest-before-fix.txt`).

## Trend verdicts

- **expansion: improved.**
  - PROVINCE Core gains SQLite schema reading, which had 0 rows under any spelling.
  - SKILL gains a 23-row decision table.
  - Knowledge files went 116 → 118 (recipe A, w2 `RecipeAAtTip.md`). SOURCES went +6.
- **quality: improved.**
  - Both committed-record checks now compare the full envelope (M30-3 repaired; copied-predictions control 0/23).
  - Non-author seats re-derived 12 of 12 C1 envelopes and 23 of 23 C2 rows.
  - Wave-2 overstatements were corrected in the entries:
    - "distinct branches" was false;
    - the 6.7.0 sentence "the other 21 rows' code paths are unchanged" overstated the static comparison;
    - the trivial-predictor ceiling is 7/23, not 3/23.
- **discernment: improved.**
  - The pre-data critics caught the false novelty sentence (M31-1) and a post-freeze edit gap (M31-2), both before data.
  - The pre-data axis rulings were narrow fit for C1 and fit for C2. The after-data rulings were the same (`w2/CriticAxisC1After.md`, `w2/CriticAxisC2After.md`).

## SHONEN

- [~] Decision tables / error patterns / cited sources: `SKILL.md` section "SQLite databases (`inspect-sqlite-database`) — round 31", 23 rows backed by S092. Non-author seats checked every row (w2 `ReviewC2EnvA..D.md`).
- [~] End-to-end domain task logged: the round-31 entry in LOG.md, with evidence ids in `corpus/knowledge/2026-10-23-r31-sqlite-positive.md`.
- [~] Executable instructions: the recheck lines in both entries. Independent seats re-ran them (w2 `ReRunC1.md`, `ReRunC2.md`).
- [~] No cross-domain bleed: the PROVINCE section was appended, and earlier text is unchanged. A sibling scan found 0 conflicts (w1 `ConnSiblings.md`, w2 `ConnAfter.md`).

## Gate

Real rejects, with reasons:
- A SOURCES row for REA's `main`-branch SQLite guide was rejected. It describes a later release, not the 6.5.0 pin.
- A separate row for pyproj 3.7.2 was not made. Its `proj.db` is byte-identical to 3.7.1's (w1 `ReviewCarrierProvenance.md`).
- The refusals entry's nominal S096/S097 citation was rejected and removed (w2 `ReopenS097.md`).

## Round shape, seats, holds

- **Shape:** the default, two v1 waves.
  - w1: 44 seats (scribe 11, critic 10, mutation-tester 9, reviewer 5, executor 3, revenger 2, scout 2, sentinel 1, connector 1). All 44 returned.
  - w2: 38 seats (reviewer 19, scout 9, critic 5, mutation-tester 3, sentinel 1, connector 1). 33 returned.
  - Round total: 82. No residual call.
  - Planner seat: held by the L1.
- **Dead seats (w2, not replaced):** `ReviewProvinceSkill` and `ReviewCensus`, both with `[inception/mercury-3] 429 Rate limit reached: output token limit exceeded`.
- **Cancelled at wrap-up:** w2 `ReviewEntryC1`, `ReviewQualityLesson` and `CriticHarm`, cancelled when the L1 reached its request budget. Their findings were not integrated.
- **Integration fix:** the cited-runs gate's selftest was path-dependent (M31-6) and was fixed before it was committed.
- **Containment:**
  - Carriers, mutants and downloads were `chattr +i` before dispatch, and every pin is intact (w1 `SentinelContainment.md`).
  - One w2 seat ran `git commit` in the fleet repo. It made no commit (M31-7).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no untracked file that names kaidoku round 31.
- **Hold:** item `U064N008Hf47eb933` remains held and untouched.
- **L0 questions:** none.
- **Tool installs:** none by the L1. Seats report none, except that w1 `CriticOracle` used an apsw 3.54.1 build in a scratch uv venv (see its report). No pacman transaction.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
