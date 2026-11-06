# kengaku — round 100 (hyaku run 15, attempt 1)

## Work performed

Declared claims (frozen at F `54df15ca1f9b689b25c6ffc3b2fccd1253bdd6c2`, `plans/round-100-claims.md`):

- **R100-C1 — coverage** (the lowest non-retired axis, L0 cap 7). An eighteenth located offline replay of
  a pinned Terminal-Bench 2.0 grader, `financial-document-processor`, picked by Q86 from the three-way
  minimum class tie (`crypto-credential 4/12`, lift +1/12; shell-exec has no offline-feasible member).
  It is the first member graded through sha512 sets over agent-moved files, with an OCR positive control.
- **R100-C2 — freshness** (ceiling 10, exercised). Nine BASE SOURCES rows whose digest equals the committed
  copy of the very upstream file their pinned URL names, but which the frozen gate bound to a different
  file (8 `digest-wrong-capture`) or to nothing (S300), are bound by three new three-cell
  `corpus/evidence/round<N>/PROVENANCE.md` files. All 9 upstream files were re-fetched live before the
  freeze and still matched. A row-level census covers all 333 BASE rows; this closes round-99 routed
  defect 3 (F6/M17).

Round work:

- Protocol load: the lane prompt; `skill://shokunin`, `skill://godspeed`, `skill://swarm`; AXES.md,
  LEARNING.md, RULES.md; SCORECARD r99 section and its round-100 Planned rows; `corpus/lessons/round-99.md`;
  `round-99-verifier-spotcheck.md`, whose routed defects 1–6 are dispositioned in `corpus/lessons/round-100.md`
  §Round-99 routed defects; QUALITY Q84–Q86; `considerthese/2026-11-06.md`; round-99 ConnectorOverlap (c).
- Round status: the last three closures are r97 rejected-honest-stop, r98 admitted and r99 admitted, so no
  pause applies. The watchdog shows no `lane-dead-no-report kengaku round=100` line, so there is no
  inherited attempt.
- P0 `fb0f125c`:
  - 25 blobs captured flat with `SHA256SUMS`. All 26 pin-tree blobs were opened at 12:06 -03, HTTP 200;
    git blob ids equal the pin tree, and the 17 document sha512s equal the grader's 17
    (`L1/capture-time.txt`). `.gitignore` was opened and not captured.
  - The maintainer OCR solution was run once offline (fixture `corpus/evidence/round100/fdp-solution/`).
  - Mechanism predictions were written before any grader run (`L1/predictions-mechanism.txt`).
  - Census start rc 0.
- P1 `4df35de8`:
  - Instruments: `plans/round100_fdp_probe.py`, `plans/round100-cases.json`, `plans/round100_c1_replay.py`
    (L1–L13), `plans/round100_c2_rowcensus_bind.py` (K1–K10), `plans/round100_provenance_build.py`,
    `plans/round100_prefreeze_check.py`.
  - C2 population at BASE (`L1/c2-pop.txt`) and live re-fetch (`L1/c2-live-refetch.txt`, 9/9 equal).
  - Dry runs 1–2: 15/15, with equal observations.
- P1b `934b984a` and P1c `f07c026e`: amendments 1 and 1b before any freeze (`L1/amendment-1.txt`). They were
  exposed by two dry control batteries, archived in `controls/dryrun-p1a/` and `dryrun-p1b/` (lessons M2–M4):
  - C2 censuses now start from REF = F~1.
  - The K5 rule is now a token-set rule.
  - The `^{commit}` reference fix is now `~1`.
  - S343's quote was made visible to the line gate.
- P2 `5220b71d`: 32 controls, each run twice with agreeing results, against the P1c bytes
  (`L1/controls/README.md`).
  - Every forgery's tree diff from its positive was asserted (Q85).
  - The pre-freeze standing-gate check on the candidate tree is clean (`prefreeze-both-run{1,2}.txt`).
- F `54df15ca` → C = T `dbe0cefa`:
  - 16/16 frozen-instrument and 6/6 candidate-byte sha256 match at T.
  - `git diff F T` is exactly the candidates plus the receipt (`L1/freeze-tip.txt`).
  - Receipts `d8ed39bd`.
- Integration `e40b332a`:
  - `corpus/knowledge/tb2-financial-document-processor-grader.md`, `corpus/README.md` §Round-100.
  - `corpus/lessons/round-100.md` (Gate, Mistakes M1–M4) and QUALITY Q87–Q89.
  - The considerthese proposal-1 measurement and the wave spec and dispatch.
- Harm battery `cd0705f6` (`L1/harm/README.md`): finding-set diffs, with revision-scoped r82c1.
- Wave w1 through the inline handoff, with WAVE-DONE from Main. 12 seats, 11 settled with reports, 1 dead
  (ScribeLesson). Settlement `83cde632`.
- No dated correction after T.
- No new L0 question. Carried and open: `kengaku | round-98` (coverage cap) and `kengaku | round-54`
  (assimilation hold).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| P0 capture, OCR solution fixture, predictions, census start | `LOG.md` Round 100, order bullet P0 | `fb0f125cb272be31143a0bc57685b093b356b984` |
| P1 instruments, population, live re-fetch, dry runs, pre-freeze receipts, candidates | order bullet P1 | `4df35de800425ca1dbe66681368f372361b891fe` |
| amendment 1 (before freeze) | order bullet P1b/P1c | `934b984a1d200e61aad84f67cacd7293f394ed9a` |
| amendment 1b (before freeze) | order bullet P1b/P1c | `f07c026ec1b1ac47bb925ffdc70afcf5a8c782d8` |
| P2 controls ×2 | order bullet P2 | `5220b71d337a3703eaba4cdf6b85eaf343497ae0` |
| F frozen claims | order bullet F | `54df15ca1f9b689b25c6ffc3b2fccd1253bdd6c2` |
| C: ledger flip, SKILL cells and registry rows, S342–S349, three PROVENANCE.md, probe receipt | order bullet C | `dbe0cefa607cf57f7f58346fce64bcc127144ca0` |
| measurement receipts, freeze integrity | order bullet receipts | `d8ed39bd8edb95a5721290e860a07fc21c32700b` |
| knowledge entry, README rows, lesson, Q87–Q89, wave spec and dispatch | Sources/knowledge bullet | `e40b332a565d644cf9466071b34dea4f3d237c38` |
| L1 harm battery | Harm bullet | `cd0705f6cc3767092a427becc01b7ecfaf122b1f` |
| wave settlement, census end, lesson wave findings, SCORECARD, LOG | Wave bullet | `83cde63266b53204ef888dc3dae5a8194b24c9bd` |

The lane HEAD is `83cde63266b53204ef888dc3dae5a8194b24c9bd`, and
`git ls-remote origin refs/heads/master` prints that hash.

## Before → after measurements

**R100-C1 (coverage).**
- Command: `python3 plans/round100_c1_replay.py --lane . --rev REV --work DIR --grader-venv G`, where G is
  `uv venv -p 3.13` plus pytest 8.4.1, pandas 2.3.2 and pytest-json-ctrf 0.3.5 (numpy 2.5.4 resolved).
- BASE `78460376`: `PREDICATE R100-C1 fail`, rc 1 (`L1/c1-base.txt`). The ledger had 43 of 88 executed,
  with `crypto-credential` 4/12 and `file-artifact` 34/76.
- T `dbe0cefa`: `REV dbe0cefa…`, `LEGS L1..L13=pass`, then
  `TARGET executed_rows=44 member=financial-document-processor cells=crypto-credential:5,file-artifact:35 set_equals_base_plus_member=1 located=1 executed=1 cases=15 legs=120 mismatches=0 new_rows=8 new_rows_flagged=0 new_rows_line_live=0 changed_outside_table=0 defects=0`,
  then `PREDICATE R100-C1 pass`, rc 0 (`L1/c1-tip.txt`).
- Do-nothing control: fail, in both runs.
- Located grading gaps:
  - 11 `total` rows pass (C03).
  - Ten copies of one invoice row pass (C04).
  - Copies kept in `/app/documents/keep/` pass (C07).
  - A duplicate invoice copy passes (C08).
  - The 0.01 band is strict (C11/C12).
  - Header order and a BOM fail the structure test but not the content test (C14/C15).
- Independently reproduced by ExecC1 (gaps rebuilt with its own code), ReviewC1, ScoutSources and
  ExecHarm.
- ExecOCR found that the pinned tesseract 5.3.4 gives a placement and summary byte-identical to the
  fixture's.
- Routed: CriticClaims F1 (receipt run identity is self-reported) and MutC1's 19 survivors and its F1
  (TARGET is printed, not asserted).
- Verdict: **met** on the frozen predicate. Score 7 → 7, held at the L0 cap.

**R100-C2 (freshness).**
- Command: `python3 plans/round100_c2_rowcensus_bind.py --lane . --rev REV --work DIR`.
- BASE: `TARGET pop=9 cleared=0 still=9 …`, `PREDICATE R100-C2 fail`, rc 1 (`L1/c2-base.txt`).
- T: `REF 5220b71d…` (= F~1), `GATE defects base=33 ref=32 rev=23`, `LEGS K1..K10=pass`, then
  `TARGET pop=9 cleared=9 still=0 outside_rows=324 outside_removed=0 outside_added=0 outside_rebound=0 base_rows=333 base_rows_not_equal=0 new_provenance_files=3 url_channel_files=0 not_three_cells=0 ids_not_in_pop=0 live_rows=9 rows_changed=0 captures_changed=0`,
  then `PREDICATE R100-C2 pass`, rc 0 (`L1/c2-tip.txt`).
- Controls of note:
  - `outside-row-delete` fails K8 only (round-99 M17 killed).
  - `fabricated-id` and `fourth-cell` fail K4 and K3.
- Independently reproduced by ExecC2 (its own checker, 90/0), ReviewC2 (population re-derived), and
  ScoutSources (9/9 live).
- Routed: CriticClaims F2 and F3, MutC2 T21 (a duplicated same-id row), and ReviewC2's minor findings.
- Verdict: **met** on the frozen predicate. Score 10 → 10, held at the ceiling.

## Sources & frontier

- SOURCES rows: **333 → 341**.
  - Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at
    `78460376` and `83cde632`.
  - Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
    Start: `kengaku ok`, rc 0, 31 W04 (`L1/census-start.txt`). End: `kengaku ok`, rc 0, 32 W04
    (`L1/census-end.txt`). The new W04 is S342, whose URL duplicates an earlier row's across scopes.
- Added by tier: A 7 (S342–S348), B 1 (S349).
- Added by status: 6 mined (S342–S347); 2 rejected (S348, S349), each with its flip stated.
- Rows touched old→new: none. All 333 BASE rows are byte-equal at T (C2 K8). Outside row S295, round 93's
  rejection of this same member, is re-bound by the new capture; its cell is unchanged.
- Frontier advanced:
  - `financial-document-processor` moved from unexecuted to executed (ledger 43 → 44).
  - 9 wrongly bound digests are now bound to their URLs' own files (gate 32 → 23 from REF).
- Sourced claim: R100-C1 rests on S342–S347, opened 2026-11-06 12:06 -03. `corpus/lessons/round-100.md`
  §Gate records the URL, access date and a ≤25-word located quote for each row, and
  `corpus/knowledge/tb2-financial-document-processor-grader.md` cites them.
- ScoutSources re-opened all 8 new rows and the 9 population URLs live: 17/17 agree.
- Mistakes mined (`corpus/lessons/round-100.md` M1–M4), with QUALITY Q87–Q89 added:
  - M1: the pre-freeze standing-gate check. Shown able to fail: red on round-99 T, rc 1.
  - M2/M3: the census reference.
  - M4: a quote invisible to the line gate.
- Assimilation: none (inherited `merge/kengaku/` hold, L0 `kengaku | round-54`).
- considerthese: `2026-11-06.md` §1 proposal 1 was measured. 8 historical frozen tables with 99 rows; 0
  differ at T (`L1/frozen-union-at-T.txt`).

## Trend verdicts

- **expansion: improved.** A new knowledge entry,
  `corpus/knowledge/tb2-financial-document-processor-grader.md`, covers ground not held at BASE: grading
  through sha512 sets plus lookup-by-key CSV checks, the first such `crypto-credential` member. It is
  indexed in `corpus/README.md` §Round-100, with ledger 43 → 44 and S342–S347 mined.
- **quality: improved.**
  - 9 wrongly bound digests were re-verified live and are now bound to the correct committed files.
  - All 333 BASE rows are unchanged under a row-level census.
  - Q87–Q89 are lesson-grounded.
  - No post-T correction was needed.
- **discernment: unprovable-but-better.**
  - ScoutSources, a non-author seat dispatched by the lane, agrees with S342 admit and S348/S349 reject.
  - LEARNING.md requires an outside check, so the closure's spot-check decides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the `SKILL.md` crypto-credential and file-artifact cells (5 of 12, 35 of 76) and the five `round100-*` registry rows at `dbe0cefa`; the grading lessons are in `corpus/knowledge/tb2-financial-document-processor-grader.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the official financial-document-processor replay `corpus/evidence/round100/fdp-probe.txt` and `LOG.md` Round 100. ExecC1 reproduced it (`.ufo/waves/round-100/w1/ExecC1.md`).
- [~] Instructions executable by an agent without oral context — the frozen commands in `plans/round-100-claims.md` were re-run unaided by wave seats (`.ufo/waves/round-100/w1/ExecC2.md`, `ScoutSources.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` is unchanged, and ConnectorOverlap (a) finds no sibling overlap (`.ufo/waves/round-100/w1/ConnectorOverlap.md`).

Round shape: one v1 wave under `ufo-wave-policy.json` (band 8–16), 12 seats.
- Role mix: 4 executor, 2 reviewer, 1 critic, 2 mutation-tester, 1 scout, 1 connector, 1 scribe.
- Attack seats: 5/12.
- There was no residual call, so the round total is 12 seats.
- **Dead seat: ScribeLesson** (scribe). It ran 2 h 13 min without writing a report and was cancelled by the
  orchestrator; its last output is progress narration only (`w1-results.json`). Its partial scratch is not
  evidence.
- The L1 held the planner seat, and ConnectorOverlap (c) carried the bounded planning data-walk.

Stale-lane: respawn-per-round driver; no other kengaku mission is open. Round 100 is the campaign target.

Inherited state: the untracked orchestrator markers `.ufo/waves/round-97/w1.ready{,.dispatched}` are not
lane-authored and were left untouched.

Misroot sweep: the fleet `git status --porcelain` shows the orchestrator's `.scratch/` files and two
untracked files. Neither was written by this round's seats, so nothing was moved:
- `w4lines.txt` (2026-11-05).
- `versions.html` (12:35, before the wave; a Read-the-Docs 404 page naming no lane).

Tooling: none installed. Scratch uv venvs (CPython 3.13.16 from the uv cache; PyPI pins as above, plus the
solve.sh PEP 723 pins for the one OCR run) lived under `/fast/scratch/hyaku/kengaku-r100/`, which was
removed after landing. Host tesseract 5.5.3 was preinstalled. pacman, sysctls and services were untouched.

Open L0: none new. Carried: `kengaku | round-98` (coverage cap) and `kengaku | round-54` (assimilation hold).
