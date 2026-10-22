# tameshi — round 27 report (L1 TameshiR27, attempt 1, 2026-10-22)

Lane head (pushed): `35a01b3c5afa9b4b7f6497bcb196125ee759141b`. Base: `91edf9cd82ccc72e10f62f81d37181f549d593b8`.
Round shape: one v1 wave of 51 seats, plus one residual call of 8 reviewer seats. Round total: 59 seats.

## Work performed

Two claims were declared and frozen in `.ufo/evidence/round-27/contract.json`, landed in `70df8d6`:

- **C1, calibration, harm repair.** This is round-26 closure item 1. The goal was to restore the strict cold-read monitor through independent seat cold reads. The calibration claim counts the mismatch between SHONEN box 3 `[~]` and the monitor.
- **C2, coverage, frontier F8 (oracle anchoring), learning claim, sourced.** The four round-26 cite-check hole survivors are re-judged against expectations anchored outside the mutated code.

Work items:

- **Pre-registration.** The counters `c1-measure.py` and `c2-measure.py`, the before-values and an appended SCORECARD correction of the round-26 C2 row ("numeric 8 → 8" was really 8 → 6) landed in `70df8d6a485418d9e57fed9d21e84fba71d4be66`. The anchors and the probe were committed before the probe ran, in `06a6707904582cc2f268d8a74861c6a8d09dd1fe`.
- **C2 content** landed in `2227d8338c02aa9a5fd7d95c1a41b76865ad7647`:
  - entry `corpus/knowledge/oracle-anchored-survivors.md`;
  - probe receipt `.ufo/evidence/round-27/f8/receipt.json` (`ANCHOR_PROBE: ran=4/4 anchored_holes=4`);
  - SOURCES: S012 moved from queued to mined; S090 and S091 are new;
  - README F8 section;
  - QUALITY 53 and 54;
  - counter amendment 1 (`contract-amendment-1.json`). The frozen S012 `opened` check could only pass by breaking the SOURCES append-only rule. The target stayed unchanged.
- **Negative control** after wave findings, landed in `2abb018`. With deliberately unsupported expectations, the probe gives `anchored_holes=0` (`f8/probe-negative-control.stdout`). This shows the probe judges against the anchor, not against the pristine run.
- **Wave 1** (51 seats, spec `.ufo/waves/round-27/spec-w1.json`, record `record-w1.json`). 39 cold reads ran at `2227d83`. 27 sections were credited and 12 failed on real page defects. The 12 failing sections were corrected in SKILL.md, each with a pointer to its seat and with line counts kept. The ledger append (38 entries, prefix preserved) landed in `b1cc95e1fb62532646d74e2863770c4fed0851cc`. The receipt is `coldread/append-receipt-w1.json`.
- **Residual call** (8 reviewer seats, `spec-residual.json`). The 12 corrected sections were re-read at `b1cc95e`. 8 were credited. 3 were `wrong-expectation`; two of those errors were introduced by the L1's own corrections. 1 was `gap-blocking` after its seat dropped receipts that read the live lane. The ledger append (12 entries) and further corrections of the 3 failing sections landed in `af7b70daf7754f1d9363669cf9bc97ec01f61f9c`.
- **Routed items.**
  - Item 2: the SCORECARD correction is appended.
  - Item 3: a full registry run at `2227d83` in a fleet mirror reads `held=49/49 superseded=7` (`after/registry-2227d83.stderr`). A clone without siblings reads a false 46/49; this is recorded as Mistake 3.
  - Item 4: the new C2 counter binds its receipt to the probe and anchors sha256. QUALITY 54 records this rule.
  - Item 5: the `--regression` check that leg results add up to `nlegs` is **not fixed**. A runner edit would re-drift most cold-read entries. It is routed forward.
- **Mistakes mined.** Six are recorded in `corpus/lessons/round-27.md` under `## Mistakes`: the round-26 harm, the counter clause, the registry run outside a fleet mirror, a seat misroot, whole-tree `git status` receipts, and one report that did not parse.

## Landed changes

| Commit | Content | LOG entry |
|---|---|---|
| `70df8d6` | contract, C1 and C2 counters, before-values, census start, round-26 C2 correction | LOG.md "Round 27" motivation lines |
| `06a6707` | `f8/anchors.json`, `f8/anchor-probe.py` (before the run) | same |
| `2227d83` | F8 entry, receipt, SOURCES S012/S090/S091, README F8, QUALITY 53–54, amendment 1 | same |
| `2abb018` | lesson draft, registry receipt, negative control, `40a12bf` monitor receipt | same |
| `b1cc95e` | wave-1 cold reads, traces, ledger append, 12 SKILL section corrections | "Result C1" line |
| `af7b70d` | residual cold reads, ledger append, 3 further SKILL corrections | "Result C1" line |
| `35a01b3` | SCORECARD measured results, LOG results, lesson after-measurement, after receipts | "Result C1/C2" lines |

Every lane commit went through `jj-lane.sh`. The last helper line was `landed 35a01b3c5afa9b4b7f6497bcb196125ee759141b`, and the state reads `local=remote ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

- **C1.** Command: `python3 .ufo/evidence/round-27/c1-measure.py --repo CLONE --rev REV`.
  - Before, at `91edf9cd`: `C1_MONITOR: covered=25/64 restraint=6 box3_mismatch=1`, exit 1.
  - After, at `af7b70d` and again at `35a01b3`: `covered=60/64 restraint=6 box3_mismatch=1`, exit 1.
  - Target `64/64 restraint=8 box3_mismatch=0`: **missed, honest stop.** Calibration is still harmed relative to round 26's base (restraint 8).
  - Uncovered at head: "The report shape", "Triggers T1–T3", "Gate/probe registry" (each corrected again but not re-read), and "Round-21 gate/probe registry" (gap-blocking).
- **C2.** Command: `python3 .ufo/evidence/round-27/c2-measure.py --repo CLONE --rev REV`.
  - Before, at `91edf9cd` (frozen and amended counter alike): `classified=0`, exit 1.
  - After, at `af7b70d` and `35a01b3`: `C2_F8: survivors=4 classified=4 anchored_holes=4`, exit 0. **Target met.**
  - Bound, from seats CriticAnchors and MutateC2Counter: the counter is necessary but not sufficient. It cannot tell an anchored expectation from one copied off the pristine run. The honest anchor-strength count is 3 header-anchored holes plus 1 held by convention only (S_PIN_INCLUDES).

## Sources & frontier

- Census start: exit 0, 87 rows. Census end: exit 0, 89 rows (`after/census-end.stdout`). Counting command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`. The same seven W04 warnings appear before and after.
- Rows added (tier A): S090 (sysexits(3), FreeBSD) and S091 (gitrevisions).
- Rows touched: S012 status `queued` → `mined`, used-by `—` → the F8 entry. Each change is logged in the lesson's `## Gate` with a located quote of at most 25 words.
- Frontier: F8 moved from open to **partly held**, on one gate at one pin. The next move is in the lesson: 17 of 35 survivors on the other eight legs have a header anchor (seat ScoutLegAnchors).
- Open item: `corpus/SOURCES.md:338` still says "Next unused id: S090". Editing SOURCES.md would drift cold-read entries, so the fix is routed forward.
- The sourced claim is C2: the entry cites S012, S090 and S091, all opened this round.

## Trend verdicts

- **expansion: improved.** One admitted entry on uncovered frontier ground (F8), citing three rows opened this round.
- **quality: improved.** 15 wrong or unsupported statements in SKILL.md were found by cold reads and corrected, each with its seat named. No entry was superseded.
- **discernment: improved.** The pristine-differential hole calls are now separated from anchored ones; the negative control discriminates between them. Anchor strength is reported per survivor instead of as one count.
- **calibration (axis): harmed, not restored.** Monitor credit is 60/64; restraint stays 6, against 8 at round 26's base.

## SHONEN

- [~] Box 1, SKILL.md tables, patterns, sources: lane assertion, no independent promotion verifier (`SHONEN.md`).
- [~] Box 2, end-to-end task: lane assertion (`SHONEN.md`).
- [~] Box 3, instructions executable cold: cold-read ledger 60/64 at `35a01b3`, not full-page. The mismatch is still 1 (`after/c1-measure-af7b70d.stdout`).
- [~] Box 4, no cross-domain bleed: lane assertion (`SHONEN.md`).

## Round mechanics

- **Wave 1:** 51 seats, policy v1. Roles: reviewer 42 (39 cold reads), executor 3, critic 2, mutation-tester 1, connector 1, scout 1, scribe 1. Attack roles: 45 of 51.
  - Gate: acquired 12:21:53Z, granted 12:42:01Z (`live=33`), dispatched 12:42:05Z. One task call, no refusals.
- **Residual:** 8 reviewer seats. Gate granted at 13:28:13Z; dispatched in one call.
- **Totals:** 59 seats. No seat died. Seats asked to revise only their own reports: Read17, Read24, Read29 and ReRead03. Every seat returned, and both gate reservations were released.
- **Planner seat:** held by the L1. The planning data walk rode the scout item ScoutLegAnchors.
- **Task adapter:** `solutionSpace` was added to each item (`task-adapter-*.json`). No `model` parameter was passed.
- **Misroot sweep:** no tameshi file was left at the fleet root. Seats Read38 and ReRead02 wrote there first and moved their reports into the lane themselves.
- **Inherited state:** the lane was clean at the start. No earlier-attempt leftovers existed.
- **Kumitate, routed to the owner via the integrator.** The round-26 routing of the four cite-check holes was dropped by kumitate R39-5 (seat ConnectorOverlap).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- L0 questions: none.
