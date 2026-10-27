# Round 58 — kake report

Lane `kake-shokunin`; final lane tip `9892ea4ab42d305adb408905a3f19f7b7109f095` (remote `refs/heads/master` verified). Measured revisions: C2/C3 `8d340c15200959190ba3e894399cdc931976331f`; C1 `de7d96e720522ea15fba3fd9ee3ce58c42596031`.

## Work performed

Declared claims: **C1 calibration** — disclose every post-commit measurement-receipt event with the git blob values; **C2 operability** — close the resolver's fence-blind and revision-path false greens; **C3 freshness (sourced)** — add two opened Baidu crawler-identification/unblocking entries on S423/S424. Calibration remains a lane sub-axis whose ownership relative to the prompt's operability/freshness scope is open for the operator.

- Frozen v1 controls before data; one v2 build/attack wave, **68 seats**: executor 23, scribe 10, reviewer 9, critic 8, scout 7, mutation-tester 4, connector 3, sentinel 2, simplifier 1, revenger 1. L1 held planner seat. v1 counter attacks and cheapest controls produced v2 contracts/selftests before claim measurements (`kake-shokunin/.ufo/waves/round-58/contract.md`; commits `fff3eea6`, `cc8da167`, `1c0aa211`).
- Residual falsification call: **8 seats** (5 reviewer, 3 critic), 8/8 reports; together with W1, **76 seats**, no reported dead seats. Results: `kake-shokunin/.ufo/waves/round-58/w1-results.json`, `r1-results.json`. W1 built the three counters, independent adversarial fixtures, two entries, and evidence reviews; r1 rechecked entry fidelity, receipt-note truth, counter cheats, resolver behavior, and previous-gate impact (`r1/`).
- C1 ledger records 19 historical events with their actual commits/blob IDs and event notes. V2 closes the concrete rename, nested-path, symlink, wrong-kind, and empty-pointer cases. Residual limits disclosed: a pointer-only note and fabricated values under a classifier-assigned kind can still pass; semantic note/value truth is reviewer-checked (`r1/CriticC1V2Cheat.md`, `CriticLedgerNotes.md`).
- C2 `scripts/id_resolver.py`: CommonMark-flat fenced registry state and `git ls-tree -z` revision paths; selftest 59/59. Residual loud failure: non-UTF-8 filenames cause exit 2; residual gate weakness: P6 accepts a hollow selftest that prints `59/59` (`r1/ReviewerResolverDiff.md`, `CriticC2V2Cheat.md`).
- C3 adds `corpus/knowledge/baidu-spider-identification.md` (S423; staged S395 renumbered by document) and `baidu-spider-unblocking.md` (S424, lane-found from S423). Re-grounded both retained pages, rejected S378 as an ads product-list FTP crawler outside province, and corrected the drafts after sentence-level review (`r1/ReviewerEntryIdentification.md`, `ReviewerEntryUnblocking.md`).
- Frontier census: before and after both exit 0, 160→162 rows, 14 unchanged W04 warnings. Collision check: 8; staged IDs 129; two A-tier rows added; no existing row status/recheck/used-by touched. The 12-row quarantine slice was re-opened and classified in the lesson. Six payloads are currently present, three registered quotes absent as quoted, three prose-class rows unverifiable; they were **not appended** because that would widen the frozen two-row C3 mirror predicate and introduce unrelated themes. This is a frontier-step conformance defect, not a pass; the L0 question is filed at `.ufo/l0-questions.md`.
- Mined mistakes: the r57 pending-receipt rewrite, the wider event-ledger gap, and the historical-gate pin problem, each recorded in `corpus/lessons/round-58.md` and grounded by red-before evidence. Added QUALITY criteria and historical markings; `c57_receipt_pins.py` is red at the new tree because its frozen input set includes the changed resolver and round-58 receipts, so it is now marked historical at its measured revision (`r1/ReviewerNoHarm.md`).
- Misroot sweep before filing: fleet `git status --porcelain` empty; lane status empty after final commit. Tools installed/updated: **none**; no pacman transaction.

## Landed changes

| Work | LOG entry | Commit |
|---|---|---|
| Contract v1, counters and base controls | Round 58 | `fff3eea6` |
| W1 spec/dispatch, 68-seat v2 wave | Round 58 | `cc8da167` |
| V2 counter predicates, selftests and counter-version amendment | Round 58 | `1c0aa211` |
| Resolver fix, 19-event ledger, S423/S424, README/PROVINCE/QUALITY/SKILL and lesson build | Round 58 | `c1e39ef3` |
| Eight-seat residual dispatch | Round 58 | `0ffbabff` |
| Post-review entry/lesson corrections, validation and census | Round 58 | `8d340c15` |
| T0/T1 measurements and C2/C3 after-receipts | Round 58 | `de7d96e7` |
| C1 after-receipt, SCORECARD/LOG and residual results | Round 58 | `1b009b74` |
| Quarantine hand-check/L0 question and final lane closure | Round 58 | `9892ea4a` |

## Before → after measurements

| Claim | Counting command and revision | Before | After |
|---|---|---|---|
| C1 calibration | `python3 -B .ufo/waves/round-58/c58_receipt_rewrites.py --root . --revision <rev>`; base `0440485`, after T1 `de7d96e7` | `events=19 undisclosed=19`, exit 1 (`controls/base-c1-receipt-rewrites-v2.txt`) | `events=19 undisclosed=0 phantom=0 malformed=0 wrong_kind=0 unpointed=0 symlinks=0 new_rewritten=0 new_receipts=2 met=True`, exit 0 (`controls/after-c1-receipt-rewrites.txt`); selftest 45/45 |
| C2 operability | `python3 -B .ufo/waves/round-58/c58_resolver_cases.py --root . --revision <rev>`; base `0440485`, after T0 `8d340c15` | 6/14, exit 1 (`controls/base-c2-resolver-cases-v2.txt`) | 14/14, exit 0 (`controls/after-c2-resolver-cases.txt`); tool selftest 59/59; three-seed residual run 14/14 |
| C3 freshness | `python3 -B .ufo/waves/round-58/c58_quote_truth.py --root . --revision <rev>`; base `0440485`, after T0 `8d340c15` | 0/8, exit 1 (`controls/base-c3-quote-truth-v2.txt`), registry 160 | 8/8, exit 0 (`controls/after-c3-quote-truth.txt`), registry 162; selftest 120/120 |

All three v2 predicates measured met. C1 calibration score moves 1→2; operability and freshness remain 10/10. No new capability row: C2 deepens the round-57 source-id resolver.

## Sources & frontier

The start census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` → exit 0, 160 rows, 14 W04 (`controls/census-before.txt`, `census-before.exit`). The same command at round end → exit 0, 162 rows, same 14 W04 (`controls/census-after.txt`, `census-after.exit`). Added by tier: A 2 (S423, S424). Touched old→new: none. Frontier advanced: Baidu crawler identity/unblocking on the existing Crawler identity ground. `SOURCES.md` rows 160→162; the round lesson records the opened URLs, access dates, located quotes, rejects, flips, and quarantine verdicts.

Quarantine conformance defect: six rows were present at re-open (S142, S156, S161, S193–S195), three absent as registered (S143's concatenated table-cell quote, S148, S206), and three unverifiable from prose-only classes (S154, S178, S184). The present rows were held rather than appended because the frozen C3 predicate allows only its two new rows and the round's assimilation theme is Baidu crawler identity. This conflicts with the quarantine-first instruction; see `corpus/lessons/round-58.md` §Assimilation and the L0 question. Frontier/claim admission therefore remains subject to non-author closure; no present quarantine row is represented as adopted.

Assimilation: one theme from `merge/kake/`, with S395 re-grounded as S423 and S424 opened from its outbound link. Considerthese proposal 2 (receipt-rewrite watch) was implemented as C1's event ledger rather than the file-level watch. No staged row was appended as-is; S378 was rejected with a page-grounded reason and flip.

## Trend verdicts

- **expansion — improved:** two entries on Baidu crawler-identity ground absent from the coverage map, citing new mined rows S423/S424; registry 160→162 and README frontier map advanced.
- **quality — improved:** all admitted quotes pass the committed quote-truth gate and the residual source fidelity reviews; all three v2 selftests/gates pass. Limits (C1 notes/value truth, C2 hollow P6 tally, non-UTF-8 exit 2) remain explicit; the quarantine present rows were not admitted.
- **discernment — unchanged:** admits/rejects and reasons are recorded, but no non-author spot-check has run; all dispatched seats are part of this lane. Closure owes at least one admit and one reject re-open.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open. No tool installs.

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited sources — evidence: `SKILL.md` gate registry, `corpus/QUALITY.md` Round-58 criteria.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched this round.
- [~] Instructions executable without oral context — evidence: counter CLI contracts and selftests under `.ufo/waves/round-58/`.
- [~] No cross-domain bleed; PROVINCE remains accurate — evidence: S378 rejection, `PROVINCE.md` Round-58 scope note, `r1/ReviewerEntryUnblocking.md`.
