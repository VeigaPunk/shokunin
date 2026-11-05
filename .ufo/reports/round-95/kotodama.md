# kotodama — round 95 (attempt 1)

Lane HEAD for this report: `feb94bc3353182e9554e41faa4203d8c5707335f` (branch `main`, `ls-remote origin refs/heads/main` matches, `jj-lane.sh state` `ahead=0 behind=0`). Freeze commit: `d41eb594d27fa71869c0c28d9c2dc051fda40079`. Base: `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`. Stale-lane: the respawn driver; no other mission of this lane is open.

## Work performed

Declared claims (2), frozen before any data at `d41eb594` in `reports/round-95/claims.json`:

- **Claim O — operability (successor move, grader v5 → v6).** Target: close the round-94 closure's routed defects R95-1 (head-qualify pin missing), R95-2 (stale `dispo-fallback` pattern) and R95-3 (seven CriticO94 surviving counterfeit classes). Frozen predicate O0–O4 in `reports/round-95/predispatch.py`.
- **Claim C — coverage (sourced claim).** Target: a dedicated knowledge entry on the funerary lament / dirge sung-register surface, which had no owner at base, with ≥3 new tier-A/B registry rows. Frozen predicate C1–C5.
- The frontier step (§2b) is not a third claim: `corpus/SOURCES.md` curated (S970–S974 opened this round), census before/after recorded, one mistake mined (R95-M3 closed this round), and claim C cites S970–S974, all opened 2026-11-05 (sourced claim requirement met).
- Lowest-axis obligation: **not met and not waived.** The historically lowest non-retired axis is freshness; its move is paused by the open L0 questions (`.ufo/l0-questions.md` line 47 round-11 and line 303 round-89, no ANSWER). Neither declared claim is freshness. Operator ruling needed (see L0 note below).

Work items, each with its evidence pointer:

1. Pre-freeze do-nothing control — `reports/round-95/predispatch-base.txt`: frozen counter over the base tree prints `PREDISPATCH-95: FAIL legs=4/10`; the control cannot reach either target. Two counter defects found by this control before freezing (POSIX-class regex parsing 0 rows; C3 requiring git inside an archive) and fixed; `reports/round-95/counter-revisions.md`.
2. Freeze — commit `d41eb594`: `reports/round-95/claims.json` (sha256 `5d6cfcbf…`), `reports/round-95/predispatch.py` (sha256 `e6d92eb3…`), `predispatch-base.txt`, SCORECARD planned row.
3. Wave w1 — one v1 wave, 13 seats, validated under `scripts/hyaku/ufo-wave-policy.json`, dispatched 15:15:18 via the inline handoff (`.ufo/waves/round-95/w1.ready`, `w1.ready.dispatched`), settled and reported at WAVE-DONE (`.ufo/waves/round-95/w1-results.json`). Seat roles: executor 4 (ExecBattery95, ExecGraderV6, ExecMutants95, ExecRegistry95), scout 1 (ScoutTopic95), scribe 2 (ScribeEntry95, ScribeLesson95), connector 1 (ConnectorOverlap95), reviewer 2 (ReviewerO95, ReviewerC95), critic 2 (CriticO95, CriticC95), mutation-tester 1 (MutationTester95). Attack seats 5/13 = 38 % (≥25 %). Connectors 1. Residual call: none. Dead seats: none (13/13 wrote DONE or report files; `w1-results.json` records the orchestrator kernel restart mid-wave, and the seat reports in the wave dir are the retained outputs).
4. Claim O grader v6 — `tools/check-advance-evidence.py` (`f7981ba2…`): named refusals for combining marks (`VERDICT-COMBINE`), format characters (`VERDICT-FORMAT`), whitespace in the verdict (`VERDICT-TAB`), lookalike id letters (`ID-NONASCII`), and nested / roman / second-token numbered headings that anchor nothing (TOPIC). Selftest 126 → 134 with a head-qualify pin (the pin fails under the mutant, `reports/round-95/controls/`). Stage: `.ufo/waves/round-95/w1/stage/ExecGraderV6/` (receipts selftest, battery, reg-diff).
5. Claim O battery — `.ufo/waves/round-95/w1/stage/ExecBattery95/battery95.py` (sha256 `342237cd…`), 14 classes; red-before over v5 `controls/red-before-v5.txt`: `BATTERY-SUMMARY survivors=7 unnamed=0 refused=7` (the 7 new classes survive rc 0; the 7 round-94 classes refused).
6. Claim O mutation — `.ufo/waves/round-95/w1/stage/ExecMutants95/mutants95.py` (sha256 `ff450980…`), 95 entries: 88 round-94 carried + 7 new. Red-before over v5: `controls/mutation-red-before-v5.txt` `87/95 killed, 1 survived, 7 broken-pattern` (deviation from the predicted composition, disclosed in the lesson; the refreshed `dispo-fallback` pattern matches v5 once).
7. Independent attacks on claim O — ReviewerO95 `REVIEWER-O-95: PASS legs=5/5` (own reruns: selftest ×4 concurrent, battery, REG, mutation, `diff -u` of v5 vs v6: no removed check, no weakened refusal); MutationTester95 `MUTATION-INDEPENDENT: MATCH` (95/95, byte-identical per-mutant lines, hand probes `head-qualify-off` → selftest 133/134, `cd1-refusal-off` → 133/134).
8. Claim C entry — `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` (50614 B, 12 h2, table 11×5, six frozen phrases in headings/table cells, topic line byte-equal). Drafted by ScribeEntry95; CriticC95's seven findings (F1 two paragraphs restating the lullaby entry; F2 Seremetakis footnote attributed to a Corsican claim; F3 unsourced cross-tradition claim; F4 vocative gloss attributed to S974; F5 "classical division"; F6 spliced quote; F7 Ó Madagáin attribution) were applied before landing, each as a named line edit (lines 31, 60, 68, 90, 112, 114, 133, 157, 250).
9. Claim C rows — `corpus/SOURCES.md` S970–S974 (tier A, kind paper, mined, opened 2026-11-05, recheck 180d, used-by the entry), captures `reports/round-95/evidence/S97{0..4}.txt|.pdf`; anchor quotes located once each in their own capture (ExecRegistry95, ReviewerC95 re-count). S975–S981 were staged by the scout and not landed: reasons recorded in the lesson (R95-M6).
10. Evidence manifest — `reports/round-95/evidence/manifest.json` (R95-M5 closed; url, http_status 200, sha256, bytes, quote, fetched_at = scout-stage capture instants).
11. Registry index and README — `corpus/README.md` (revision block, linguistics entry row, round-95 footer; 266 → 267 files).
12. Lesson — `corpus/lessons/round-95.md` (`## Gate`, `## Mistakes` R95-M1..M7, `## Routed to round 96`, `## L1 integration record`). Gate-quote check: `GATE_QUOTES: 0 findings`, rc 0.
13. SKILL registry row for the grader (R95-M3 closed): `SKILL.md` `## Gates and probes`, row `check-advance-evidence (grader v6)`.
14. Bookkeeping: `SCORECARD.md` round-95 axes, capability row `grader v6 counterfeit refusals`, and the round-94 capability row marked unadmitted (R95-4); `LOG.md` round-95 entry; `reports/round-95/counter-revisions.md`.

## Landed changes

Landed in lane commit `feb94bc3353182e9554e41faa4203d8c5707335f` (153 files, `jj-lane.sh commit`, `landed` line printed after remote verification):

- `tools/check-advance-evidence.py` — grader v6, LOG.md round-95 entry (claim O).
- `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` — new entry (claim C), LOG.md round-95 entry.
- `corpus/SOURCES.md` — S970–S974 (5 rows; 893 → 898; search-log line), LOG.md round-95 entry.
- `corpus/README.md` — index row, footer, revision block.
- `corpus/lessons/round-95.md` — Gate, Mistakes, Routed, integration record.
- `SKILL.md` — grader v6 registry row (R95-M3), LOG.md round-95 entry.
- `SCORECARD.md`, `LOG.md` — round-95 rows and entries.
- `reports/round-95/` — claims, counter, do-nothing and lands receipts, controls, evidence captures and manifest, counter-revisions.
- `.ufo/waves/round-95/` — spec, dispatch, ready files, results, all 13 seat stages and reports (wave evidence).
- Freeze commit `d41eb594` (claims, counter, base control, SCORECARD planned row) precedes the work commit.

## Before → after measurements

Claim O — counting command: `python3 -B reports/round-95/predispatch.py --root <tree> --work <scratch> --base-rev 19aa4dd03dfd37b435d0b8ea5b313635d9d51592`, measured at `feb94bc3` (scored files byte-identical to the committed tree; `reports/round-95/predispatch-lands.txt`).

| leg | before (base `19aa4dd0`, v5 `7957945d…`) | after (lands, v6 `f7981ba2…`) | evidence |
|---|---|---|---|
| O0 tool sha256 | `7957945d…` | `f7981ba2…` | predispatch-lands |
| O1 selftest | `SELFTEST PASS 126/126` (floor 134 → FAIL) | `SELFTEST PASS 134/134` rc 0, ×4 concurrent | `controls/selftest-lands-run{1..4}.txt` |
| O2 battery95 | survivors=7 unnamed=0 refused=7 | survivors=0 unnamed=0 refused=14 | `controls/battery-lands.txt`, `controls/red-before-v5.txt` |
| O3 mutation95 | 87/95 killed, 1 survived, 7 broken (v5 red-before) | 95/95 killed, 0 survived, 0 broken-pattern | `controls/mutation-score-lands.txt`, `controls/mutation-red-before-v5.txt` |
| O4 REG | — | 34 lines byte-identical to v5 baseline (`reg-diff-v6-vs-v5.txt` empty) | `controls/reg-v5.txt` |
| PREDISPATCH-95 (whole counter) | base control `FAIL legs=4/10` | `PASS legs=10/10` | predispatch-base / predispatch-lands |

Claim C — counting command: same counter (C1–C5), plus `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` and `python3 -B tools/check-corpus-index.py --root .`.

| leg | before | after | evidence |
|---|---|---|---|
| C1 entry | absent | present: 50614 B, 12 h2, table 11×5, phrases 6/6, topic line equal | predispatch-lands |
| C2 registry | 893 rows, highest S969, qualifying 0 | 898 rows, highest S974, qualifying 5 | predispatch-lands |
| C3 append-only | — | added 7 (5 rows + 2 search-log lines), removed 0 | predispatch-lands |
| C4 census | rc 0 (base 893) | rc 0 at HEAD (`reports/round-95/census-head.txt`, last line `kotodama ok`) | census-end, census-head |
| C5 index | OK files=265 rows=265 | `CORPUS-INDEX: OK files=267 rows=267 findings=0` rc 0 | predispatch-lands; census-head |
| entry grader (supporting, not a frozen leg) | — | `ENTRY-EVIDENCE: PASS legs=9/9` | `controls/entry-grader-lands.txt` |

The do-nothing control (base tree) for both claims: `PREDISPATCH-95: FAIL legs=4/10` (`reports/round-95/predispatch-base.txt`).

## Sources & frontier

- `corpus/SOURCES.md` rows before → after: **893 → 898** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; 893 at base `19aa4dd0`, 898 at HEAD). Census start: `C4 PASS census rc=0` in `reports/round-95/predispatch-base.txt`; census end: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` rc 0 (`reports/round-95/census-head.txt`, last line `kotodama	ok`).
- Rows added by tier: **tier A: 5** (S970–S974; kind paper; status mined; opened 2026-11-05; recheck 180d; used-by `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`). Tier B: 0. Tier C: 0.
- Rows touched old → new: none (no existing row's status, recheck or used-by changed). One search-log line appended (APPENDONLY 7 added / 0 removed).
- Search log: `corpus/SOURCES.md` `Search log — funerary laments and dirges (2026-11-05)`; full per-candidate ledger in `corpus/lessons/round-95.md` `## Gate` (rejected/unreachable with reason class per QUALITY criterion 37). Scout search: 12 DOAJ queries, 5 Crossref, 8 OpenAlex, 2 folklore.ee operations, 265 records screened. Staged-but-unlanded candidates S975–S981 (captures in the wave stage) are not rows; reasons in R95-M6.
- Frontier rows advanced: the funerary lament / dirge sung-register surface moved from unowned to a dedicated core entry (claim C).
- Mined mistake: R95-M3 (no SKILL registry row for the grader across rounds 90–94) — closed this round; R95-M1..M7 recorded in `corpus/lessons/round-95.md ## Mistakes`.
- Sourced claim: claim C rests on S970–S974 (opened 2026-11-05 by plain curl, default user agent, `--max-time 30`; located quotes verified once each in the committed captures).
- Assimilation: none. `/home/vgpnk/Projects/shokuknow/merge/kotodama/` exists; no theme was adopted this round, because the round's claims were frozen before the package was read and the quarantine-first verdict list for the lane's register slice is a separate open item.
- considerthese: no `considerthese/` directory in this lane — one line: `considerthese/ absent`.
- Lane quarantine: not run this round (wave-4 quarantine-first completed in rounds 68–71).

## Trend verdicts

- **expansion: improved** — a dedicated admitted-shape entry on ground with no filename owner at base, citing five new mined tier-A rows, census rc 0, corpus index OK. Evidence: `predispatch-lands.txt` C1/C2, `census-head.txt`.
- **quality: unchanged** — no admitted entry re-verified, deepened or superseded; `corpus/knowledge/` changes are the new entry only. Evidence: `git show feb94bc3 --stat -- corpus/knowledge`.
- **discernment: unchanged** — author-side gate decisions: five admits (S970–S974) and the rejected/unreachable reasons in the lesson. The non-author seats in this round (ReviewerC95, CriticC95, ReviewerO95, CriticO95) were dispatched by this lane and are the lane under LEARNING.md; no non-author closure has run yet, so no `unprovable-but-better` or `improved` is claimed. Pending the protocol closure.

Per-claim axis verdicts (author-side; closure pending): O — operability **improved** (frozen predicate met at lands, evidence above); C — coverage **improved** (frozen predicate met); adjacency unchanged; depth unchanged; freshness unchanged (paused, L0); calibration unchanged. No axis harmed: `git diff 19aa4dd0 feb94bc3 -- SCORECARD.md` is append-only.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` `## Gates and probes` (grader v6 row added this round, `feb94bc3`); author-side assessment, no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 95` (claim C entry, sourced rows, census and index receipts).
- [~] Instructions executable by an agent without oral context — pointer: `reports/round-95/predispatch.py` run command and `reports/round-95/claims.json` predicates, re-runnable from committed bytes.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` unchanged this round; ConnectorOverlap95 boundary report `.ufo/waves/round-95/w1/stage/ConnectorOverlap95/overlap.md`.

## Open items and L0

- L0 unchanged: round-11 and round-89 freshness questions (`.ufo/l0-questions.md` lines 47, 303; no ANSWER); round-92 ideophones overlap (line 356; no ANSWER). No new L0 line appended this round.
- Routed to round 96 (`corpus/lessons/round-95.md ## Routed to round 96`): CriticO95's nine surviving classes (VT1/FF1/LS1/NEL1 splitlines-severing; NB1 NBSP; ANSI1 ESC; CYR1 homoglyph id gating; BR1 `## (1)`; DASH1 `## -`); the F1 battery class; the teaching-cell / anchor-quote coupling (R95-M4); the raw search-JSON staging gap.
- Host needs (named, not performed): none beyond the standing pacman pause; no sysctl or host setting was touched by any seat.

## Tooling

Installed or upgraded: none (L1 and all 13 seats). No pacman, no sysctl, no `-S`/`-Sy` operations.

## Mistakes and misroot sweep

- Misroot (this round): ReviewerC95's full report was written by the seat to `reports/round-95/w1/ReviewerC95.md` (relative trailer resolved from the lane root, not the wave dir). The L1 moved it byte-exact to `.ufo/waves/round-95/w1/ReviewerC95.md` (`cmp` equal), removed the misrooted copy, and recorded it here. The seat's stage `review.md` and DONE were already correct.
- Fleet-root sweep before this report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/run15-state.json` (orchestrator-owned) and `.ufo/l0-questions.md` (modified by a sibling or the operator, not by this lane; not touched by the L1 this round). No fleet-root file was written by a seat of this lane. Neither file was touched by the L1.
- One L1 mistake, fixed in place: a stray `corpus/lessons/round-95.md.tmp` was created and removed before commit; the LOG entry was written to `LOG.md`.

## Inherited state

Attempt 1; no prior attempt marker. Uncommitted leftovers from earlier attempts: none.

## Pre-report gates

- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-remote origin refs/heads/main` → `feb94bc3353182e9554e41faa4203d8c5707335f`.
- WAVE-DONE received for `w1` (the only wave launched this round).
- `grep -c '^## SHONEN'` on this file must print 1 (checked at filing).
