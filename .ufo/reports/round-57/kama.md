# kama — round 57

## Work performed

Declared claims: C1 operability — reject the round-56 roster-only counter's no-op control; C2 calibration — correct the stale verifier-spotcheck count in the lane SCORECARD.

- C1 updated `tools/round56-prereg-check.py` to bind the declared battery roster to AST call sites. Genuine roster remains `met=True`; preserved no-op control now returns `met=False`, exit 1 (`.ufo/waves/round-57/measured/{c1-committed-tip,noop-c1}.out`; source row S516).
- C2 corrected the SCORECARD calibration count from 42 to the observed 43 verifier-spotcheck files. Frozen counter base had `mismatches=1`; measured final counter reports `mismatches=0 met=True`, exit 0 (`.ufo/waves/round-57/controls/base-c1.out`, `.ufo/waves/round-57/measured/c2-committed-tip.out`).
- The lane reopened S515 at its Git documentation URL, and opened/admitted own-work S516 for the battery's named call sites this round (`corpus/lessons/round-57.md` §Gate; `corpus/SOURCES.md` S516).
- Revisited the round-56 outside disagreement on S513 and the inherited append-only-audit defect; both remain explicitly unresolved in the round-57 lesson Mistakes, with reasons they were not changed in this counter-focused round.
- Dispatched one v2 wave with 64 seats; L1 held the planner seat. The validated role mix was scout 8, connector 7, executor 8, scribe 7, reviewer 8, critic 7, mutation-tester 7, revenger 4, sentinel 4, simplifier 4. Attack roles (reviewer + critic + mutation-tester) were 22/64. On user instruction to wrap, the wave had not sent WAVE-DONE; settled/dead-seat counts and final results handoff were unavailable, so no seat outcome is represented as settled. Dispatch and spec: `.ufo/waves/round-57/w1-{spec,dispatch}.json`.
- Pre-data claim freeze and control receipts: `.ufo/waves/round-57/controls/`; the claim ordering clarification was committed before any seat results were received.
- Round-start source census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0, 256 registry rows (start output `.ufo/waves/round-57/census/start.out`). Round-end: same command → exit 0, 257 rows (end output `.ufo/waves/round-57/census/end.out`, exit `.ufo/waves/round-57/census/end.exit`).
- No tool installs. `pacman` remained paused.

## Landed changes

- Freeze and no-op controls — lane commit `89dc4f5239fe1f875adda4613812e77fb9bbc7cc`.
- Pre-data claim-order clarification — `7c873d7b4e3839489a93d6334cdf93fe5d34d19f`.
- Counter, SCORECARD, LOG and lesson work — `7b74e2f2515a6f598918488fa5144658ff29925f` and `8640e34cad02adcd247ba0862da63f6fb2aab0df`.
- S516, round lesson and census evidence — `16efcf5eedf4887df188790eec48afbb023e7991` and `3d2d5d4d6cba3028ec5358832a67f192cc0e41ec`.
- Final-tip measurement receipts — `77e7f5eef2b0c759b7509056c7c511255477496d`.
- Preserved no-op fixture and routed-defect notes — `87bb7d4ccf51622b6f362956e242d81fb78ccf2f`.

Each change is described in `LOG.md` round 57. Final lane tip cited: `87bb7d4ccf51622b6f362956e242d81fb78ccf2f`.

## Before → after measurements

- C1 (operability 8→8): genuine roster positive control remains `met=True`; matching-roster no-op changes from the round-56 false green (`met=True`, exit 0; `corpus/lessons/round-56-verifier-spotcheck.md:14`) to `met=False`, exit 1 (`.ufo/waves/round-57/measured/noop-c1.out`). Counting command: `python3 tools/round56-prereg-check.py --repo <repo> --tip <revision>`. Final positive measurement: `.ufo/waves/round-57/measured/c1-committed-tip.out`, measured at `3d2d5d4d6cba3028ec5358832a67f192cc0e41ec`.
- C2 (calibration 7→7): frozen counter base `mismatches=1 met=False` (stale expectation 42, observed 43) → final `mismatches=0 maxN=57 met=True`, exit 0. Counting command: `python3 tools/round42-selfdesc-reconcile.py --repo <repo> --tip <revision>`. Base: `.ufo/waves/round-57/controls/base-c1.out`; final: `.ufo/waves/round-57/measured/c2-committed-tip.out`, measured at `3d2d5d4d6cba3028ec5358832a67f192cc0e41ec`.

Both measured counters verify their declared predicates; no score scalar changed. The C1 checker establishes call-site presence, not that every possible runtime effect of every call succeeds. The swarmed falsification review remains unsettled at report time, so these are author measurements, not an outside admission.

## Sources & frontier

SOURCES.md rows: 256→257. Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (baseline bytes at `b89bdab2cc114735ec5d331c6c610134258f7864`; final at the report's lane tip). Added by tier: A=1 (S516 own-work); rows touched old→new: none; frontier rows advanced: none. S515 was reopened this round, without a row-cell change. S516's Gate quote and located line range are in `corpus/lessons/round-57.md`. Assimilation: none. `considerthese/2026-10-26.md` proposal 3 was opened; no multi-round shortcut tally was implemented.

## Trend verdicts

- **expansion — unchanged:** one source row was added, but no new knowledge entry or uncovered domain ground was admitted (`SOURCES.md` S516; `corpus/README.md` Frontier).
- **quality — improved:** the no-op counter control now fails, and the calibration count re-derives at the measured tip (`measured/noop-c1.out`, `measured/c2-committed-tip.out`).
- **discernment — harmed:** the round-56 closure's S513 disagreement remains unlearned as a QUALITY criterion; round 57 had no independent non-author admit/reject spot-check. This is recorded rather than claimed away (`corpus/lessons/round-57.md` §Mistakes).

## SHONEN

[~] Decision table, error-pattern list and checklist — author assertion, `SKILL.md` §§Decision table, Historical error signatures, Checklist; no non-author verifier this round.
[~] End-to-end domain task executed and logged — author assertion, lane-owned lifecycle receipt and `LOG.md`; no non-author verifier this round.
[~] Instructions executable without oral context — author assertion, `SKILL.md` Checklist; no independent execution review this round.
[~] No cross-domain bleed — author assertion, `PROVINCE.md` boundary; no non-author verifier this round.

Stale-lane: respawn-per-round driver; no other kama mission is open. L0 questions: none added; the existing MISSION/config axis discrepancy remains operator-owned and unresolved.

## Erratum — partial seat findings received after filing

This append-only correction supersedes the report's earlier statement that no seat findings were available; WAVE-DONE still had not arrived at this correction.

- R02's independent review found axis attribution, claim separability, freeze ordering and base controls valid, but the rendered wave context retained the pre-amendment claim labels and incorrectly said “expected 46” for `maxN` (`.ufo/waves/round-57/w1/out/R02AxisFit.md`, lane commit `9df8e8ddb4d245611ef3ce65490c42f102ecda95`). The actual frozen C2 defect is the calibration row's 42-versus-43 verifier-spotcheck count, as the committed amendment and SCORECARD record.
- E03's 13-fixture selftest found the C1 repair still accepts dead-code and unused-function call-site no-ops (2/7 cases fail); therefore C1's execution-binding claim does **not** verify. C1 is an honest stop; do not credit its operability move. Evidence: `.ufo/waves/round-57/measured/R57Item05CounterSelftest/` and `.ufo/waves/round-57/reports/R57Item05CounterSelftest-case05{,-evidence}.md`, lane commit `9df8e8ddb4d245611ef3ce65490c42f102ecda95`.
- Quality trend remains improved only on the bounded selftest comparison (frozen-checker no-ops rejected 4/7; repaired-checker no-ops rejected 5/7); surviving dead-code and unused-function no-ops still invalidate C1's frozen execution-binding predicate.
- E02's independent canonical-row instrument rejected the frozen no-op while accepting the genuine 11-row table; it made no lane source edits and does not replace C1's frozen predicate. Evidence: `.ufo/waves/round-57/w1/out/E02CanonicalBinding.md`, lane commit `9df8e8ddb4d245611ef3ce65490c42f102ecda95`.
- Other seats remained unsettled and the results handoff was unavailable. Settled/dead-seat counts remain unknown. The original wave context is a conformance defect; the committed pre-data amendment remains the declared claim authority.
- C1's residual survivors and the no-credit ruling are now append-only in `SCORECARD.md`, `LOG.md` and `corpus/lessons/round-57.md`, lane commit `d7cb74dda164e19eb362536e12dc127926c3735a`. C2 remains measured; no scalar changed.

## Erratum — WAVE-DONE and settled evidence

The orchestrator delivered `WAVE-DONE kama r57 w1`; all 64 seats settled: 62 complete, 1 done and 1 closed, with 0 dead seats (`.ufo/waves/round-57/w1-results.json`, lane integration commit `46d1fde97cd24c2ee1dd3338ee52071fc0bec98e`). This supersedes the earlier unsettled-seat count.

- R57Item29 and E03 independently falsified C1's frozen execution-binding predicate: dead-code and unused-function no-op variants still satisfy the AST-only checker. C1 is not verified and earns no operability credit. The report's first quality-trend statement is narrowed: quality improved only on the bounded selftest comparison, where no-op survivors fell 4/7→2/7 rejected; the surviving shortcuts remain material.
- R02 confirms the claim axes, separability and pre-data freeze chain, and flags the dispatched context's false `maxN expected 46` premise and stale C1/C2 labels. `maxN` is 56 at base; the actual C2 calibration defect is 42 stated versus 43 observed. The committed amendment governs.
- R04CounterSemantics found equal-number duplicate canonical headings select the first match; this is preserved as an unclaimed counter limitation in the round-57 lesson. E02's independent canonical-row prototype rejected the frozen no-op and accepted the 11-row table, but was not integrated and does not replace either frozen claim.
- Lane evidence for all settled seats is committed at `46d1fde97cd24c2ee1dd3338ee52071fc0bec98e`; final lane ledger correction is `83c1c4a5e2c210d9f4e1454b64c686994330f05f`.
