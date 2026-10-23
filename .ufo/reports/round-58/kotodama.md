# kotodama — round 58 report (hyaku phase 4, attempt 2, L1 KotodamaR58A2)

## Work performed

Declared claim (1), one frozen predicate (`reports/round-58/claims.json`, claim base `80f48c2c`, declaration and control receipts `97577f6c`, dry-run `adc28834`):
- **C — coverage** (learning claim, sourced claim): new entry `corpus/knowledge/linguistics/toponymy-place-names.md`; predicate ACCEPT-C-58 (`reports/round-58/accept-c.py`, fifteen legs incl. live LOCATE/BOILER/TOPIC with no slack, RELEVANCE (a)-(e), DISTINCT, TIER and SUPPORT over registered non-author reviewer verdicts). Surface: frontier → core, a topic with 0 filename owners at base (`git ls-tree -r --name-only 91e50d7e corpus/knowledge | grep -ciE 'topon|place-?name|placename|onomast'` → 0); overview owner `naming-systems.md` §3/§5 is pointed to one-way.
- One claim, not two: the routed defects are records work and no second axis move was independent and cheap (`claims.json` `one_claim_note`).

Work items:
- Routed defect 2 (LOCATE blind to relevance) built into C's counter before data. Five pre-data revisions, each forced by a control that met the previous counter (`claims.json` `revision_note`; commits `a43f5336`, `c42121f4`, `edecdc90`, `1a07344e`, `80f48c2c`): 8-seat control wave (`.ufo/waves/round-58/control/`: CtlOffTopicEcho58, CtlLexiconKey58 and CtlNoReader58 met earlier revisions — BLOCKING; CtlJunk58, CtlAllFalse58, CtlFooter58 ALL-FAIL; MutRowcheck58 35/36 killed; MutLegIsolation58 honest green PASS and 17/17 single-leg mutations fail); blind support-control review (SupportCtlA58/B58/C58: 17/18 shortcut rows NOT-SUPPORTED unanimously, one split; 8/8 real rows SUPPORTED; planted misquote caught); receipt `reports/round-58/telemetry/controls-c.txt` (123 fixtures re-scored at `6faef400`, 0 pass).
- Build wave (41 seats, `.ufo/waves/round-58/build/`): 22 scouts opened 44 rows S500-S543 (23 hosts); entry written by the L1 from them (`ddc17f4a`).
- Support wave (6 reviewer seats, `.ufo/waves/round-58/support/`): 44/44 rows SUPPORTED (`a7e47abd`).
- Records (`e27c8a67`, `45bb7e1a`): CODH bukan erratum (reason false; re-tested by the locator, 4/4 LOCATED; registered S576); heraldry :41 re-sourced to S575 (Lyon Information Leaflet No. 4); superseding rows S560-S562, S564-S574; S428 finding shown false (no row owed); QUALITY criterion 12; lesson `corpus/lessons/round-58.md`.
- Correction filed (routed defect 5): the round-57 report's tier count "A 34, B 8" is wrong; committed S413-S454 are **A 36 / B 6** (three community-kind rows, tier B).

## Landed changes

| commit (landed) | change | LOG |
|---|---|---|
| `91fb8fd9`, `3d790714`, `a43f5336`, `c42121f4`, `edecdc90`, `1a07344e`, `80f48c2c`, `6faef400` | instruments, declaration, five pre-data revisions, declarations naming each base | LOG round 58 |
| `97577f6c`, `adc28834` (and dry-run receipts `ee7caddc`, `d4a5ea31`, `25919ac4`) | control receipts and evidence; final pre-data dry-run | LOG round 58 |
| `ddc17f4a` | claim C: entry, `corpus/README.md` (234), SOURCES S500-S543 | LOG round 58 (C) |
| `a7e47abd` | support verdicts and registry | LOG round 58 |
| `e27c8a67`, `45bb7e1a`, `af1a3489` | records, census and final-measure receipts, SCORECARD, LOG, wave records | LOG round 58 |

Lane tip `af1a348980f9b9ac20cdf8829e5bdd176b401735` (pushed by `jj-lane.sh`, `ahead=0 behind=0`).

## Before → after measurements

- **C** — `python3 -B reports/round-58/accept-c.py`: at `adc28834` exit 1 (SET 233, SWEEP 233, FLOOR 0, live legs and SUPPORT 0 cited) (`telemetry/declaration-dry-run.txt`). After, four live runs in fresh clones (`telemetry/final-measures.txt`): `a7e47abd` FAIL (BOILER S510 page-unfetchable), `e27c8a67` FAIL (TOPIC S511 page-unfetchable), `e27c8a67` FAIL (BOILER S510 root-unfetchable), `45bb7e1a` FAIL (BOILER/TOPIC S511 unfetchable). Every other leg PASS on every run (cited 44, LOCATE 44/44, RELEVANCE 44/44, DISTINCT 23 hosts, SUPPORT 44/44 by 6 seats). S510 and S511 pass alone (`rowcheck.py --row`), so the failures are fetch-class at two .gov.au hosts, but the frozen predicate has no slack: **C does not verify as declared** (reported, not amended). Separability (`tools/check-claim-separability.py`) also reports `SEPARABILITY_DEPENDENCY`: C's acceptance needs `.ufo/waves/round-58/support/`, a path its declared lands omit.

## Sources & frontier

- `grep -c '^| S[0-9]' corpus/SOURCES.md`: 465 → 525. Added: 44 claim rows S500-S543 (tier A 38 / B 6, all `mined`); 16 records rows S560-S562, S564-S576 (S575 `mined`, others `queued`).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`: start not run at round start (conformance defect); run late on a base clone `kotodama ok`, exit 0 (`telemetry/census-start.txt`); end run 1 exit 1 (17 E05 kind `web`/`record` on rows added this round, R58-M6), corrected to `docs`, end run 2 `kotodama ok`, exit 0 (`telemetry/census-end.txt`).
- Mined mistakes R58-M1 (false not-registered reasons twice; QUALITY criterion 12), R58-M2 (tier arithmetic), R58-M3 (prompt committed by the lane identity — not repeated this round), R58-M4 (counter met by controls five times before data), R58-M5 (two scribe misroots into `reports/round-58/`, moved), R58-M6 (kind enum). Sourced claim: C cites only rows opened this round.
- Gate rejects with tool output: Toronto street-naming page (TOPIC `terms 0`), Barnet policy (`HTTP Error 403`), GSI Japan (`UNSAFE_LEGACY_RENEGOTIATION_DISABLED`), an undergraduate essay (tier judgment); S563 not filed (finding false).

## Trend verdicts

- **expansion: improved** — new ground (toponymy, 0 filename owners), 44 rows opened and judged SUPPORTED by non-author seats; the claim itself did not verify.
- **quality: improved** — relevance is now judged (SUPPORT) and the counter withstood 123 control fixtures; but the no-slack live legs made the claim fail on host flakiness, and the separability manifest missed the support land.
- **discernment: improved** — two false prior judgments corrected (CODH reason, S428 finding); criterion 12 added; three blocking controls adopted before data.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:5`; registry 525 rows.
- [~] End-to-end domain task logged — `LOG.md` round 58.
- [~] Instructions executable without oral context — support and control seats ran from committed paths (`.ufo/waves/round-58/support/`, `control/`).
- [~] No cross-domain bleed — entry §2 one-way pointers, §13 lore handoff NON-CANON.

## Round shape and seats

Shape: control wave (8: 6 critic, 2 mutation-tester) + blind support-control (3 reviewer) as plain task calls before data; build wave 41 validated under policy v1 (23 scout, 9 reviewer, 3 scribe, 3 executor, 2 connector, 1 critic; `.ufo/waves/round-58/build-dispatch.json`); support wave 6 reviewers (plain task call). No wave 2. Round total 58. Planner seat: the L1. Dead seats: none. Cancelled at the cut: ExecReasonSweep58, ExecR57RowsNewBar58, ExecHarmCheck58 (no report integrated). Attempt-1 scratch: accept-c/rowcheck/locator/agree/dry-run reused after full re-read; calibration receipt deleted unused. Misroots: two scribe reports in `reports/round-58/` moved into `build/` (R58-M5); lane-root untracked `carriers.txt`, `flagged_rows.txt`, `locator_diff.txt`, `met_check.txt`, `plwiki_check.txt`, `s313_check.txt`, `s435_entry.txt`, `s452_locate.txt`, `tier_rule.txt`, `uncited_terms.txt`, `wayback_rows.txt` (mtimes 02:05-02:16Z, about round-57 rows; not attributable to a round-58 seat) left untouched. Uncommitted control page caches moved to `/fast/scratch/hyaku/kotodama-r58/lane-untracked/`. The dispatched prompt was not committed from the lane.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (pypdf 5.4.0 ephemerally via `uv run --with`). Open L0 questions: none new.
