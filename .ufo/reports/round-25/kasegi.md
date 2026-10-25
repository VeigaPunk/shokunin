# Kasegi round 25 report

## Work performed

Declared claims: C1, depth:verifiability (lowest non-retired axis, score 4), repairs the 35-entry recheck surface; C2, coverage (score 7), admits F10 “vendor-side disclosure policies as corpus objects.” C1 is measured on the frozen 35-entry surface and separately on the final 37-entry tree; its frozen predicate/counter weakness is disclosed rather than hidden.

- Rewrote 29 `recheck:` lines in place; all existing base tests preserved. Evidence: lane commit `98261ebaf06b6415badaec362c69623d0e1db880`; `corpus/instruments/recheck-audit.py`; `.ufo/waves/round-25/c1-receipt-index.txt`.
- Captured and re-grounded S036–S040; admitted two F10 entries, appended five normalized registry rows, and validated the round-25 manifest. Evidence: `corpus/source-snapshots/round-25/manifest.json` (5 records/40 quotes); `corpus/lessons/round-25.md` §Gate; census exit 0.
- Closed routed defects D24-1..D24-5: current report cites lane HEAD; assertion count corrected to 76; bound-8 mutant measured on landed bytes; L4 verdict reconciled to its receipt; cwd dependence removed. Evidence: `corpus/instruments/README.md`, `SCORECARD.md`, `corpus/lessons/round-24.md` appended erratum, `.ufo/waves/round-25/d24-3/receipt.txt`, `.ufo/waves/round-25/wave1/RevL4Reconcile.md`.
- Mined one still-unimplemented consideration, proposal 2 (2026-10-24): capture rendering and raw-digest metadata remain unrecorded; documented as routed debt in `corpus/lessons/round-25.md` §Routed debt. Evidence: `.ufo/waves/round-25/wave1/ScoutConsiderthese.md`.
- Mined mistakes M25-1..M25-5 and recorded the assimilation admit/reject gate in `corpus/lessons/round-25.md`.
- Repaired the round-1 wave-report misroot in the fleet root: copied `ScoutFetchCisco.md` byte-exact into the lane, verified `cmp`, removed the fleet copy. The wave-1 scribe had independently placed `RevD24Counts.md` in the lane; the lane’s misroot sweep found no remaining fleet-root round-25 files. Evidence: `corpus/lessons/round-25.md` M25-4; `.ufo/waves/round-25/wave1/ScoutMisroot.md` and `SentinelCapture.md`.
- Wave 1: `kasegi-r25-build`, 38 seats; roles reviewer 12, scout 7, executor 5, scribe 5, critic 4, mutation-tester 2, connector 1, sentinel 1, simplifier 1; 0 dead/refused. Wave 2: `kasegi-r25-falsify`, 32 seats; roles reviewer 16, critic 7, scout 4, mutation-tester 2, simplifier 1, sentinel 1, connector 1; all 32 reports landed, 0 dead/refused. Total: 70 seats, two v1 waves. The L1 held the planner seat; the `CritC2Ground`/`C1AxisVerdict` items supplied bounded planning walks. Evidence: `.ufo/waves/round-25/{wave1,wave2}/swarm-registry.json`, dispatch JSON, and 32 wave-2 reports.
- Tool installs/upgrades: none. Pacman was not used.

## Landed changes

- C1 recheck surface, counter, three pinned-surface receipts, isolating controls, and associated lessons/SCORECARD/SHONEN updates — LOG.md round 25; lane commit `98261ebaf06b6415badaec362c69623d0e1db880`.
- F10 entries, captures, manifest, registry/index/frontier updates, and assimilation gate — LOG.md round 25; lane commit `98261ebaf06b6415badaec362c69623d0e1db880`.
- D24 routed-defect corrections, round-24 erratum, bound-8 mutant receipt, and wave evidence — LOG.md round 25; lane commit `98261ebaf06b6415badaec362c69623d0e1db880`.
- Lane HEAD citation in LOG.md — lane commit `41a77b83f3a338053fa69629d753546b8d592617`.

## Before → after measurements

- **C1, depth:verifiability, score 4 held.** Frozen counter on base bytes: `lines=35 total=35 pass=6`, `executes=12 gated=0 broken=23`, parse_fail=23, cwd_fail=6, exit 1. Same final instrument digest `c3c19adcde927ac83460ad5a9855b5178935c1f5b8ec41291e8a4fd0ba2f6d7f` on the before, frozen-after, and final-after receipts. Frozen 35-file surface: `lines=35 total=35 pass=35 strict=35`, executes=12/gated=23/broken=0, exit 0. Final tree with F10: `lines=37 total=37 pass=37 strict=37`, executes=14/gated=23/broken=0, exit 0. Counter command: `python3 corpus/instruments/recheck-audit.py --json <receipt>`; see `.ufo/waves/round-25/c1-receipt-index.txt`. The score is held because `resolve.py`/`anchorcheck.py` detectors did not change; this round improves the entry-level precondition to re-derive evidence. The three frozen limbs alone were shown gameable; the stricter, additive guard and the post-freeze counter repair are both disclosed in the receipts, lesson, and SCORECARD. A mutation-tester found a separate residual: deleting an entire entry file shrinks the audited set while still passing; this is routed debt, not suppressed.
- **C2, coverage, score 7 held.** Frozen counters: admitted frontier 9→10; entries citing newly registered lane ids 0→2; registry rows 35→40; `frontier-recheck-count.py` 10/10→12/12; census exit 0 before and after. Commands are in `claims.json` and `SCORECARD.md` round 25. S036–S040 are five tier-A rows, all `mined`, `opened=2026-10-25`, `recheck=180d`; all 40 registry rows validate with only pre-existing W04 S028/S029 warnings.
- **D24-2:** 19 manifest records, **76** assertions (`sum(len(s['quotes']) ...)`); the receipt has 95 OK lines = 19 sha pins + 76 assertions. `corpus/instruments/README.md` carries the counting command.
- **D24-3:** landed resolver bytes `db5e0767…` with bound 64→8 mutant `88122e10…`: dispatch 8/8 exit 0; containment 24/24 exit 0. Receipt: `.ufo/waves/round-25/d24-3/receipt.txt`.
- **D24-4:** L4 primary assertion passes; the case fails on the added bounty/mirror citation. Evidence: round-24 baseline receipt lines 5–6 and `wave1/RevL4Reconcile.md`.
- **D24-5:** cwd failures 6→0; parse failures 23→0; all 29 modifications are same-line replacements (`numstat 1 1` each), and 24 original base-test clauses are preserved.

## Sources & frontier

Start census: exit 0, 35 rows, tier A=32/B=1/C=2, mined=23/queued=9/rejected=3, W04 S028/S029. End census: exit 0, 40 rows, tier A=37/B=1/C=2, mined=28/queued=9/rejected=3, the same two pre-existing W04 warnings and no new warning/error codes. Counting command at both boundaries:

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`

Rows added by tier: five tier-A rows, S036–S040; no existing row status/recheck/used-by was changed. Frontier advanced by F10 (admitted); 10/10 admitted. Assimilation: one theme, two lane entries; one staged package entry refused for Q3/Q7/absent F20 ground. Collision check: staged ids S031–S035 collide with existing lane ids; adopted documents were renumbered by document to S036–S040. Indented-row guard fixture caught S002. The derived kasegi absent-defect-register slice has seven rows; S068 is present and adopted as lane S040, three prose-class rows are unverifiable, one cited 404 is absent, and two payload-absent quotes require re-quoting. Evidence: `.ufo/waves/round-25/assimilation/ids/`, `wave1/ScoutQuarantine.md`, `wave2/C2QuarantineSlice.md`.

## Trend verdicts

- **expansion — improved.** F10 adds product-vendor handling policies as admitted frontier ground, with two source-backed entries and five new tier-A rows. Base evidence distinguished S016 (queued) and an existing intake-route fragment from an admitted product-vendor policy entry; see `wave2/C2CoverageGround.md` and lesson §Claims.
- **quality — improved.** The 35-entry recheck surface is executable and cwd-independent; the counter is discriminating against its declared mutations; five captures and 40 quote assertions are hash-pinned; the frontier harness remains 12/12. Known instrument limits are recorded rather than overclaimed.
- **discernment — improved.** Re-grounding caught the staged Cisco “two conditions” error (four bullets), unsupported invitation-only wording, a missing S039 heading, and an S038 quote that initially omitted its subject; corrections are backed by captures and the manifest. The staged crosswalk is refused while the distinct lane re-grounding is admitted.

## Sources & frontier (curation note)

The lane-local `recheck:` convention is not a fleet standard: the fleet SOURCES contract uses `recheck` for cadence, and chousa/kengaku gate that registry cell differently. Connector evidence: `.ufo/waves/round-25/wave2/C2SiblingOverlap.md`. The round’s C1 surface is local to kasegi’s knowledge-entry commands; no sibling corpus was edited.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists/sources — `wave1/ScoutNoHarm.md`; SKILL bytes unchanged (density 154.0; anchorcheck bad=0).
- [~] End-to-end domain task logged — LOG.md round 25; F10 source-grounded entries and C1 commands/receipts.
- [~] Executable instructions without oral context — `c1-receipt-index.txt` (37/37 form-conformant; 14 execute today, 23 gated); frontier harness 12/12.
- [~] No cross-domain bleed — PROVINCE.md F01–F10; `wave2/C2SiblingOverlap.md` reports no F10 collision and names adjacency.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none. No open L0 question was filed.

Lane HEAD at report time: `41a77b83f3a338053fa69629d753546b8d592617`.
