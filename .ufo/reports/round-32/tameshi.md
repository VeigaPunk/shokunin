# tameshi — round 32 report (L1 TameshiR32, attempt 1)

Lane head `6706bbd67835f8cc63ab47c434aba2151bc59377` (pushed; `jj-lane.sh state`: local=remote, ahead=0,
tracked=0 untracked=0). Base `e24688b2ff6cca1c9ad20e112f02c629b8597ff8`.

## Work performed

The round declared one claim: **C1, operability, capability acquisition.** The stagnation nudge applied:
depth 9 and calibration 8 were at or above the saturation line 8, and no capability row had entered since
round 25. The surface was a new versioned tool, `tools/tally-audit.py`. It audits `tools/mutate-and-run.sh`
without editing it, in three checks:

- static per-leg presence in the `--regression` tally;
- the tally block run against an oracle over every status 0–255, with stress;
- the runner's own tally harness run against a panel of 27 faulty blocks.

Building the fix in a new tool meant the runner could stay byte-identical. The runner is an input of 282
of 480 cold-read entries. **C1 is a miss.** C1 is sourced on S097 and S099 (new) and S094 (re-opened),
through `corpus/knowledge/runner-tally-audit.md`.

- **Repair first.** All five items routed by `corpus/lessons/round-31-verifier-spotcheck.md` were handled:
  - Items 1–2: `.ufo/evidence/round-32/repair/c1-r31-measure-v2.py` requires the header to equal
    `Score (0–10)` and tests append-only as a byte prefix. It gives the same verdicts as v1 at `36c1d393`
    (7 mismatches) and at `08125328` (0) (`.ufo/waves/round-32/w1/RunCounterV2.md`). CtlHeaderV2 shapes C
    and D are rejected.
  - Item 4: the round-31 base monitor receipt is `repair/c1monitor-at-r31-base-36c1d393.*` (`covered=64/64
    restraint=8`, exit 0). Command D receipts with `.exit` files exist at `67c0e013` and `08125328`.
  - Item 3 (per-leg tally check and the 8 MutateHead survivors) became C1. The fix lives in a new tool, and
    the file the ledger entries were read at is untouched.
- **Freeze `c3181497`:** counter v1, contract, base receipts. `before/mutant-fidelity.txt` confirms the 8
  frozen survivor copies and T07 are byte-identical to MutateHead's mutated SHA-256 column.
- **Wave 1 (35 seats): pre-data control wave.** Fifteen controls scored with v1 read false
  (`.ufo/waves/round-32/w1/Ctl*.md`). CriticC1's counter-reading allowlist read **true**
  (`w1/CriticC1.md`), so v1 was re-designed before data.
  - **Counter v2** (`v2/c1-measure-v2.py`, amendment 1 `b50a18f0`) runs the tool under bwrap, pins the tool
    bytes, and adds a sealed held-out set. The set is written after the freeze by seats who did not write
    the tool, and the counter validates each copy.
  - **Amendment 2** (`528f8dee`) re-pinned the tool at sha256 `9639c458…99ef`. DeterminismProbe had found a
    blind spot at harness singleton positions 0 and 1. The amendment also closed a copy-order side channel
    (ReviewCounter F2). This happened before any v2 run (`w2/ReviewAmend2Facts.md`). The amendment discloses
    a dev sweep on the public v1 families: 688 bodies, 0 misses.
- **Content revision `a4f71813`:** the tool; the knowledge entry and its README row; S097/S099; S094 used-by;
  `.ufo/evidence/round-32/receipt-check.py`; the SCORECARD/LOG round-32 blocks. Monitor there: 59/64, by design.
- **Wave 2 (33 seats):**
  - 9 cold readers for the 5 drifted sections. 13 entries were kept by binding v5 and the ledger went
    480 → 493 (`4b529ee9`). ColdA01's JSON did not parse, and the assembler rejected it.
  - 8 sealed held-out authors; 3 died (holds below).
  - 16 falsifiers: tool review and mutation (MutateToolA/B/C, ReviewTool), SentinelTool, sources, census,
    counter v2 review and mutation, and critics.
- **Measurement revision `24a5a5bb`:** 22 held-out files from the 5 completed authors, committed unedited
  (`cmp` 22/22). Also the S099 used-by fix: the lane census v2 had flagged it (`w2/RerunCensus.md`).
- **Residual call (4 seats, ordinary task):**
  - RerunV2 reproduced the result: 0 of 22 held-out outcomes differ, with a fresh seed and with the L1's seed.
  - CtlV2Controls: all 4 controls false. The embedded allowlist got `v1 18/18 8/8` but `ho_accept=0/12`.
  - CriticMeasurement and ReviewRepairs also returned.
- **Planner seat:** held by the L1, because the validator rejects `planner`. Planning data walks went to
  ScoutDeferrals, ScoutFrontier and DriftSim.

## Gate

- **Reject: counter v1, before data.** The CriticC1 allowlist met it: `kill=18/18 accept=8/8
  C1_R32_PASS=true`, on two seeds.
- **Reject: tool `158202f8`, before any v2 run.** Its harness panel missed skipped positions 0 and 1:
  16 of 72 gH05 pairs escaped.
- **Reject: tool `9639c458` as a capability.** It meets its public fixtures but fails 13 of 22 sealed copies.
- **Reject: S098.** The gnu.org Conditional-Constructs page timed out, so no row was written.
- **Reject: HeldOutHarnessCmp's four scratch files.** The seat died on the safety filter, so the files are
  not evidence.
- Sources opened (URL, date, located quote): see `corpus/lessons/round-32.md` `## Gate`.

## Landed changes

| Commit | What | LOG |
|---|---|---|
| `c3181497` | freeze: counter v1, contract, base and repair receipts, counter-v2 repair | LOG Round 32 |
| `e9f3b957` | wave-1 spec and dispatch record | " |
| `b50a18f0` | counter v2 + amendment 1; tool frozen `158202f8` | " |
| `528f8dee` | amendment 2: tool re-frozen `9639c458`, side channel closed, dev receipts | " |
| `a4f71813` | content revision | " |
| `21f7de32` | wave-2 spec, items, dispatch record, content monitor | " |
| `4b529ee9` | 13 bound cold reads appended (480 → 493); entry errata | " |
| `24a5a5bb` | sealed held-out set, S099 fix, wave-2 reports (measurement revision) | " |
| `29712da5` | measured result, lesson, LOG, after receipts, residual reports | " |
| `6706bbd6` | final-head receipts | " |

## Before → after measurements

C1 used `python3 .ufo/evidence/round-32/v2/c1-measure-v2.py --lane LANE --rev REV --work EMPTY_DIR`:

| Revision | Result | Receipt |
|---|---|---|
| base `e24688b2` | no tool. v1: `kill=0/18 accept=0/8 … C1_R32_PASS=false`, exit 1 | `before/c1-at-base.stdout` |
| `24a5a5bb` (first full v2 run) | `C1_R32V2: v1_kill=18/18 v1_accept=8/8 ho_kill=1/10 ho_accept=8/12 ho_invalid=0 tool_sha_ok=1 runner_sha_ok=1 heldout_after_freeze=1 seed=63d2e2e95a1e35c5 … C1_R32V2_PASS=false`, exit 1 | `after/c1v2-at-measurement.stdout` |

Verdict: **miss** under the frozen kill rule. The result was not re-scaled, re-seeded or amended.

No harm was measured with `python3 .ufo/evidence/round-27/c1-measure.py --repo . --rev REV`:

- base: 64/64, restraint 8.
- `a4f71813`: 59/64, by design.
- `24a5a5bb` and `29712da5`: `covered=64/64 restraint=8 box3_mismatch=0 depth_score=9`.

Command D: `recorded_cases=9 depth_score=9`. The runner sha256 stayed at `a7d3f2dd…2eb9`. The full
nine-leg replay through the tool passed: `TALLY_AUDIT_REGRESSION: PASS (cases=9 legs=9 exit=0)`
(`w2/ThenRegression.md`). Numeric scores: depth 9 → 9, calibration 8 → 8.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`:

- Start: 8 W04 warnings, `tameshi ok`, exit 0 (`before/census-start.stdout`).
- End: byte-identical, exit 0 (`after/census-end.stdout`).

Rows went 94 → 96 (`git show REV:corpus/SOURCES.md | grep -c '^| S0'`). Added, tier A: S097 (Bash 5.3
manual source) and S099 (PIT home page). Touched:

- S094 `used-by`: from the regression-tally entry to that entry plus `corpus/knowledge/runner-tally-audit.md`.
- S099 `used-by`: from the tool plus the entry to the entry only.

The lane census v2 is CLEAN with 96 rows (`after/lane-census-v2-at-24a5a5bb.stdout`). No frontier rows
moved: this is core ground (ScoutFrontier). Mistakes mined: 9 rows in the lesson `## Mistakes`.

## Trend verdicts

- **expansion: unchanged.** One new entry on ground the lane already held, and no frontier move. The
  capability did not enter the table.
- **quality: unprovable-but-better.** The routed repairs landed, with receipts. The runner was audited from
  outside, and its byte identity was kept. The tool catches every public fixture and the per-leg defect.
  The sealed set shows the tool is incomplete, though, so no measured quality gain is claimed.
- **discernment: improved.** Four real rejects came before data, including v1 and tool `158202f8`. The
  sealed held-out design turned a dev sweep with zero misses into a measured miss (13 of 22). An embedded
  allowlist that meets the public sets is rejected by v2 (`ho_accept=0/12`).

## SHONEN

- [~] SKILL.md contains real decision tables… — `SHONEN.md:5-6`; unchanged this round
- [~] At least one end-to-end domain task… — nine-leg regression PASS through `--then-regression` (`w2/ThenRegression.md`)
- [~] Instructions executable without oral context — monitor 64/64 at `29712da5` (`after/c1monitor-at-29712da5.stdout`)
- [~] No cross-domain bleed — `SHONEN.md:11-12`; no sibling scope absorbed (`w1/ConnectorOverlap.md`)

## Round shape and seats

The shape was two v1 waves under `ufo-wave-policy.json`, plus one residual `task` call.

| Wave | Seats | Roles | Completed | Dead |
|---|---|---|---|---|
| Wave 1 | 35 | mutation-tester 17, executor 7, scribe 5, reviewer 2, scout 2, critic 1, connector 1 | 35 | 0 |
| Wave 2 | 33 | reviewer 16, mutation-tester 10, executor 4, critic 2, sentinel 1 | 30 | 3 |
| Residual | 4 | executor 1, mutation-tester 1, critic 1, reviewer 1 | 4 | 0 |

Round total: 72 seats. The residual call used a mutation-tester and an executor for its control and rerun
items, which run code (orchestrator note), alongside the reviewer and critic.

Dead seats (holds): **HeldOutFree**, **HeldOutHarnessVectors** and **HeldOutHarnessCmp** (mutation-testers,
wave 2) stopped on the provider safety filter with `Codex error event: This content was flagged for possible
cybersecurity risk … (code=cyber_policy)`. They were not retried or rerouted.

## Other

- Protocol deviations (lesson Mistakes 7 and 5):
  - The amendment-1 control re-score with v2 did not run before the L1's first v2 run. It ran afterwards,
    as an observation, and all controls read false.
  - DeterminismProbe ran counter v1 on the working tool outside its item. That run led to amendment 2, which
    the closure may rule a §9 rule change. The L1's judgment is disclosed in `v2/contract-amendment-2.json`.
- Errata: "270 of 480" in `contract.json` and LOG is 282 of 480 at `a4f71813` (SCORECARD erratum).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. Pacman paused; nothing installed.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no tameshi file. Nothing
  was moved.
- Inherited state: none.
- Open L0 questions: none.
