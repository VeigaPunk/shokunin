# tameshi — round 30 report

L1 TameshiR30A3 (attempt 3 of round 30; attempts TameshiR30 and TameshiR30A2 died with the
orchestrator at 05:25:25Z and 06:19:06Z). Lane `/home/vgpnk/Projects/shokunin/tameshi-shokunin`, base
`9ed6db840dc97a0a5f4758b6b5f60cee83a61645`, lane head `8abf67c05cc31b46cba6dc7d892dcdcab0714889`
(pushed; `jj-lane.sh state`: `local=remote`, `ahead=0`).

## Work performed

Declared claim (one; exploratory): **C1 — operability (exploratory)**: the `--regression` case tally of
`tools/mutate-and-run.sh` gets a runtime completeness guard, and the runner's own `--selftest` gets
a behavioral harness that runs the extracted tally block. Routed by `round-29-verifier-spotcheck.md`
item 7 (MutateLegSum); sourced on S087, S093, S094. It was declared exploratory before data
(`.ufo/evidence/round-30/contract-amendment-4.json`, `713dee6a`) after counters v1-v4 were each met
by a control before data. Round shape: one exploratory claim plus routed repairs and a calibration
no-harm restoration (the leg's anti-loop guidance).

- Repair first. Each routed defect of `corpus/lessons/round-29-verifier-spotcheck.md` has a
  disposition in `corpus/lessons/round-30.md` "Routed defects" (seat ReviewRoutedR29:
  `.ufo/waves/round-30/wC/ReviewRoutedR29.md`, 4 resolved, 1 resolved for the lane share, 2 partial;
  the L1 closed both partial items in attempt 3: dead controls recorded in
  `.ufo/evidence/round-30/attempt3/attempt2-dead-seats.txt`, and the round-29 erratum is below).
- Inherited state re-verified (attempt 3): strict monitor at `bb681566` re-run (33/64, the same stdout
  as the committed receipt) and at base (64/64). The 23 uncommitted wave-A reports were each written
  by their own seat (`attempt3/inherited-wA-receipt.txt`, from the host transcripts) and are committed
  in `9207f226`. Ten other untracked leftovers were moved out of the lane with sha256s and are never
  cited (`attempt3/inherited-removed.txt`). Attempt 2's wave B was registered but never spawned (no
  seat transcript), so it was not resent. Wave C is a new spec with new seat names.
- Binding controls before data (L1-built, `attempt3/bind-controls.txt`, `9207f226`): a transcript
  holding only one assistant line `COLDREAD <seat>:` met binding v2 (32/32 kept on the round-29 pilot).
  Binding v3 (`coldread/bind-select-v3.py`) was frozen before the wave-C dispatch. It keeps 0/32 for the
  do-nothing, prompt-only, prose-mention and no-result controls, and 31/32 for the real transcripts.
- Wave C (`a2fa6c92` spec + validated dispatch; 38 seats, none dead): 22 fresh cold readers for the 31
  drifted sections, plus C1 judge, attacks, no-harm and frontier seats. Assembly
  (`coldread/assemble-wC.sh`): 63 entries, binding v3 63/63, ledger 393 → 456 as an append
  (`4df5107f`). Post-data audit (supporting only): 211/211 traces tied to a real `bash` call with a
  later non-error result (`coldread/audit-bound-wC.out`).
- C1 judgment: seat JudgeC1 (reviewer, non-author) `JUDGE C1: unprovable-but-better`, with reasons
  (`.ufo/waves/round-30/wC/JudgeC1.md`). Supporting evidence: RerunC1Head (the v4 receipt reproduces
  byte-identical at `bb681566`) and CriticC1Exploratory (the declaration predates the content
  revision). Limits: MutateHead (18 mutants: 7 killed, 3 equivalent, 8 real survivors, routed to
  round 31).
- No-harm checks:
  - RegressionReplayHead: nine-leg `--regression` PASS at `bb681566`.
  - SelftestsNoHarmHead: equal exits at base and `bb681566`. The jj-dependent cell was run by the L1
    in sandbox clones: 66/66 at both revisions (`attempt3/evidence-disposition-selftest.txt`).
  - Depth D 9 → 9. Census exit 0.
- Frontier: S092, S093 and S094 were re-opened (ReopenS092, ReopenS093S094). Knowledge-entry errata
  E1-E4 were appended (`corpus/knowledge/regression-tally-completeness.md`). Lesson `corpus/lessons/round-30.md`
  has five mistakes.
- Residual review (3 seats after wave C, `.ufo/waves/round-30/res/`, landed `8abf67c0`):
  - RerunMonitorHead independently re-ran the monitor: 64/64, restraint 8 at `957c5ddb`; 33/64 at
    `bb681566`; 64/64 at base. The ledger append is prefix-equal, and `bind-select-v3.py` is
    byte-identical at `9207f226` and the head.
  - SampleBoundReads: 6 of 6 sampled bindings are transcript-backed. Two `gap-minor` instruction
    entries rest on replays stopped at the seat's deadline (ColdA01 on section 375, ColdB02 on section
    933). Both sections also hold a full read by another seat.
  - ReviewLesson30: no blocking error. Six imprecisions in the lesson were corrected before filing.

## Landed changes

Every commit below is tied to the LOG.md entry "Round 30 — 2026-10-23" (`65b6e84f`). The lane helper
printed `landed <hash>` for each attempt-3 commit:

| Commit | Content |
|---|---|
| `dcdf2d08`, `e59728df`, `8a8d2540` | attempt 1: contract, counters v1-v3, control receipts, reachability witness |
| `f09d3425`, `713dee6a` | attempt 2: counter v4 + controls; C1 declared exploratory (before the content revision) |
| `bb681566` | attempt 2 content revision: runner guard + selftest harness, SOURCES S092-S094 and S087 used-by, QUALITY 58-65, README Round-30, knowledge entry |
| `07ed440a` | attempt 2 head receipts at `bb681566`, bind-select v2 |
| `9207f226` | attempt 3: binding v3 + control receipts, inherited wave-A reports, leftovers receipt, wave-C generator |
| `a2fa6c92` | attempt 3: wave-C spec and validated dispatch |
| `4df5107f` | attempt 3: wave-C reports, traces, assembly, bind receipt, ledger append, audit, dead-seat record |
| `65b6e84f` | attempt 3: lesson, SCORECARD and LOG blocks, entry errata, monitor receipt at `4df5107f` |
| `957c5ddb` | attempt 3: head receipts at `65b6e84f` |
| `8abf67c0` | attempt 3: residual review reports and dispatch; lesson corrections and residual section |

## Before → after measurements

- **C1 (exploratory, operability).** No counting command (exploratory). The judged object is
  `bb681566`, measured by the judge's own run:

  | | base `9ed6db84` | `bb681566` |
  |---|---|---|
  | dropped-leg tally | `REGRESSION: PASS (cases=9 passed=8)`, exit 0 | `REGRESSION: SETUP (case-tally mismatch: cases=9 counted=8)`, exit 2 |
  | dropped-leg mutant under `--selftest` | not caught (base selftest 97/97) | fails, 98/106 |

  Verdict: `unprovable-but-better` (JudgeC1). Supporting only, not the verdict: `python3
  .ufo/evidence/round-30/c1-measure-v4.py --repo CLONE --rev REV --sealed .ufo/evidence/round-30/v4/c1-sealed.json`.
  It gives `C1_R30_PASS=false` at `9ed6db84` (`v4/base.stdout`) and `true` at `bb681566`
  (`v4/head.stdout`, reproduced by RerunC1Head). CtlS2SymEval also meets it, so it cannot separate
  running the tally from modelling it.
- **Calibration no-harm monitor.** Command: `python3 .ufo/evidence/round-27/c1-measure.py --repo CLONE --rev REV`.

  | Revision | Monitor reading | Receipt |
  |---|---|---|
  | `9ed6db84` (base) | `covered=64/64 restraint=8 box3_mismatch=0` | `monitor-at-base.stdout`; re-run by the L1 |
  | `bb681566` | `covered=33/64 restraint=6 box3_mismatch=1` | `head/c1monitor-at-bb681566.stdout` |
  | `4df5107f` | `covered=64/64 restraint=8 box3_mismatch=0`, exit 0 | `head/c1monitor-at-4df5107f.stdout` |
  | `65b6e84f` | `covered=64/64 restraint=8 box3_mismatch=0`, exit 0 | `head/c1monitor-at-65b6e84f.stdout` |

  `957c5ddb` and `8abf67c0` add only receipt files, residual seat reports and lesson text (the lesson
  is a monitor-exempt append file). The L1 re-ran the monitor at `8abf67c0`: `covered=64/64
  restraint=8 box3_mismatch=0`, exit 0. That run is an observation, not a committed receipt; the
  measured commit is `65b6e84f`.
- **Depth (command D, SCORECARD.md).** `recorded_cases=9 depth_score=9` at base and at `65b6e84f`
  (`head/depth-shonen-at-65b6e84f.stdout`).
- **SHONEN (command C).** `boxes=4 checked=0 asserted=4` at base and head.

## Sources & frontier

- Rows: 89 → 92. Command: `git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'`, base `9ed6db84`
  → head `8abf67c0`. All three new rows landed in `bb681566`.
- Added by tier: A ×3. S092 is docs and `queued` (it supersedes S059's anchor). S093 is docs and
  `mined`. S094 is a paper and `mined`.
- Touched, old → new: S087 used-by `corpus/knowledge/mte-report-interop.md` → that path plus
  `corpus/knowledge/regression-tally-completeness.md`. Status and recheck are unchanged.
- Re-opened this round (attempt 3), with the URL, digest and located quote in the lesson `## Gate`:
  - S092: https://bazel.build/remote/caching.md, 2026-10-23T07:14:23Z, `266915c5…`.
  - S093: bwrap.xml v0.13.1, `2cb77df2…`, line 159.
  - S094: arXiv:1411.2664v3, `6e9532a9…`, §1, printed page 2.
- Frontier rows advanced: none. C1 is sourced on S087, S093 and S094, so it is the round's sourced claim.
- Census, start (attempt 3): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
  → `tameshi ok`, exit 0 (`.ufo/evidence/round-30/attempt3/census-attempt3-start.stdout`). Attempt 1's
  start receipt is `census-start.stdout`, also exit 0.
- Census, end: at the lane head → `tameshi ok`, exit 0, with eight W04 duplicate-URL warnings (S092 is
  new among them by design) (`head/census-at-65b6e84f.stdout`).
- Mined mistakes: five, in `corpus/lessons/round-30.md` `## Mistakes`.

## Gate

- Admitted: S092, S093 and S094 re-opened rows (bytes equal to the pins, quotes located); C1's
  exploratory verdict from a named non-author judge; 63 cold-read entries under the frozen binding.
- **Rejected:** binding v2. Reason: a do-nothing transcript met it, 32/32 kept
  (`attempt3/bind-controls.txt`). It was replaced before data by v3.
- **Rejected:** two sentences of the knowledge entry. Reason: "cleared environment" overstates
  `--clearenv`, and the S094 paragraph claims more than §1 says (ReopenS093S094). Errata E1-E4 were
  appended.
- **Rejected:** two control summaries in `contract-amendment-4.json`. Reason: CtlS1Normalize and CtlS4Sniff
  values were copied wrong (CriticC1Exploratory, re-checked against the receipts). The erratum is in
  the lesson; the decision is unchanged.
- **Limit recorded:** five hand-forged transcript shapes keep 31/32 under v3 (CtlBindV3). The stricter
  audit holds 211/211 on the real data. Binding v4 is routed to round 31.

## Trend verdicts

- **expansion: improved.** New ground: `corpus/knowledge/regression-tally-completeness.md` (tally
  completeness and detector limits, sourced S087/S093/S094; errata appended after review). New
  instrument: binding v3 plus the transcript audit (`coldread/bind-select-v3.py`, `audit-bound-wC.py`).
- **quality: improved.** The 31 sections drifted by the content revision were re-verified by 22 fresh
  cold readers (63 entries, no failing read), and the credit is back to 64/64 with restraint 8.
  Overreach in the entry was found and corrected by errata. Remaining survivors in the runner selftest
  are named, not hidden (MutateHead).
- **discernment: improved.** A do-nothing control was scored against the binding before data and
  forced v3. The forged shapes v3 still keeps are reported. Two wrong control summaries in a frozen
  record were caught. JudgeC1 gave `unprovable-but-better`, not a pass.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; `SHONEN.md:5-6`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion; `SHONEN.md:7-8`; this round's replay `.ufo/waves/round-30/wC/RegressionReplayHead.md`.
- [~] Instructions executable by an agent without oral context — monitor 64/64 at `65b6e84f` (`head/c1monitor-at-65b6e84f.stdout`); readers are lane-dispatched seats.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion; `SHONEN.md:11-12`; ConnectorOverlap found no sibling overlap.

## Round shape, seats, routing

- Shape: default, one v1 wave (wave C, 38 seats; fewer than 32 attack items remained for a wave 2)
  plus one residual call of 3 reviewer/critic seats. The attempt-3 total is 41 seats.
  - Earlier attempts, already in this round's history: attempt 2's wave A had 32 seats
    (`dispatch-wA.json`). Attempt 1 ran control seats under `.ufo/waves/round-30/ctl/` (7 reports).
- Wave C role mix: reviewer 26 (22 cold readers), executor 4, mutation-tester 2, critic 2, scout 2,
  connector 1, scribe 1.
  - The planner seat is the L1. The §3 floor is met: connector, 4 executors, scribe, 2 scouts,
    reviewer and critic.
  - Routing is by role (`task.agentModelOverrides`); no model was passed. Every seat prompt leads with
    `/skill:godspeed` and the directive bytes.
- The wave-C dispatch added a `solutionSpace` field per task, which the task tool requires. Nothing
  else in the validator's `taskCall` changed.
- Dead seats in attempt 3: none.
  - Attempt-2 seats that died with their orchestrator are recorded, never resent
    (`attempt3/attempt2-dead-seats.txt`).
  - Mistake 4 records that three wave-C items overlap dead attempt-2 items.
- Containment: ColdA01 killed two processes of another seat's regression workdir and first wrote its
  report at the fleet root. It moved the report itself, and no fleet copy remains (Mistake 5). The
  misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) found no file of this lane.

## Round-29 report erratum (routed item 6)

- The round-29 report's C2 "after" value `quote_located=1` appears in no committed receipt;
  `c2-at-E.stdout` reads `quote_located=0`.
- Its "Measured commit" column should name `bc2058a4`, `7a45f7b9` and `9bb699ad` (the revisions with
  committed receipts), not `6892c3ee`/`1a1e8b22`/`3c16b3a6`.

## Conformance notes

- Lowest-scoring numeric axis: calibration, at 8, the lane-attainable cap without independent
  promotion review. C1 works operability. Calibration work this round is a no-harm restoration plus
  binding v3, not a claim.
- Open questions to L0: none.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (attempt 3). uv 0.13.0 was already present; a seat used an ephemeral
`jsonschema==4.25.1` env via `uv run`.
