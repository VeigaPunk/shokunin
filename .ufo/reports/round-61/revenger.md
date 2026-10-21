# revenger — round 61 (hyaku, attempt 1, 2026-10-21)

Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main` (jj-colocated). Claim
`revenger=61` attempt 1, base `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`. Authors: L1
CloseChousa26 (pre-registration, build wave, work landing, measurement; died with host session
01a15c83 at 13:10:51 -03), then the session-3 replacement L1 RevengerR61-2 (resume, inherited-work
check, one correction, re-measure, report). L2 seat reports are the lane, not outside discernment.

## Work performed

Declared claims (pre-registered at `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`,
`reports/round-61/claims.md`, amendments A1/A2 before any after-run):

- **C1 — coverage, knowledge-map ground K** (the lowest scored criterion at the base, 2.9): admit
  gated, sourced knowledge entries on the uncovered map rows C04 (JavaScript packages) and C09 (EVM
  bytecode interfaces). This is the sourced claim.
- **C2 — calibration, receipt-identity mutation kill** (new criterion, split this round): an
  in-script forged-receipt-command control in `corpus/verify_icon_languages.py` and
  `corpus/verify_multi_icon_states.py` kills kaika mutant b (`.ufo/waves/kaika-r1/mutation-post.md:15,21`).

Work items:

- Pre-registration, counting probe `reports/round-61/measure.py` and base measurement
  (`reports/round-61/measure-before.log`) — `e0a4b0c`.
- Build wave (68 seats, 68 reports, `.ufo/waves/round-61/build/`): source opening S016–S027,
  fixture oracles for evm-r19…r26 and js-r3/r7-v2, receipt-control designs, mutation runs,
  entry drafts, critics — landed with the work in `0b6ddf07f33184baf901dd807ddc72a95f4010c1`.
- C2 landing: one `receipt_ok` predicate per script plus a deep-copy forged-command control raising
  `rNN: forged receipt command accepted` (`LOG.md:796`) — `0b6ddf0`.
- C1 landing: `corpus/knowledge/evm-saved-interface-candidates.md` (C09),
  `corpus/knowledge/commonjs-destructured-require-edges.md` (C04); README C04/C09 → held; QUALITY
  Q12/Q13 from mistakes M21/M22; seven rejected candidate claims recorded
  (`corpus/lessons/round-61.md:75-87`) — `0b6ddf0`.
- After measurement, SCORECARD round-61 table and LOG entry — `2e27c6cccb50df3433c96fc4c225b78286e70019`;
  SOURCES `## Paths`/`## Search log` for S016–S027 — `6e89c249bfa57891d97706286807bb78ea594e3c`.
- Falsify wave (65 seats) spawned at 13:08:41 -03; the host session was killed at 13:10:51 -03;
  all 65 seats died (`Request was aborted`), 0 reports
  (`.ufo/waves/round-61/falsify/dead-seats.json`). Not replaced; items not re-issued.
- Replacement-L1 inherited-work check: a dead falsify seat's transcript (`AuditR24Truth`, no
  report) doubted lesson mistake M25. My byte check: `63deadbeef14601057` occurs once in
  `corpus/fixtures/evm-r24/fixture.raw`, at offset 1, length 9 (`R24_SPAN [[1, 9]]`); `truth.json`
  `[1, 9]` is the inclusive span (authoring note `LOG.md:289`, "offsets 1–9"). The C09 entry and
  M25 had stated a fixture defect that does not exist. Entry `## Limitations` (lines 88–90) and
  M25 (`corpus/lessons/round-61.md:41,43`) corrected — `0597e5336fd67654c974fcb05f73353f44d868b9`.
- Replacement-L1 re-measure of every claim and hold on `0597e53` (appended section of
  `reports/round-61/measure-after.log`; LOG `## Round 61 resume`, `LOG.md:801-806`; SCORECARD
  note `SCORECARD.md:217-223`) — `ab580698212258a55e43e9bb9bf6ac78c91eae2a`.

Inherited from the dead coordinator and re-verified: all four landed commits above (re-measured on
the archive of `0597e53`, values identical), the six uncommitted falsify receipts (spec, dispatch,
attempts, spawn result, assignments, registry — byte content unchanged, committed in `0597e53`), the
68 build reports (68/68 non-empty against `build-assignments.json`). Discarded: M25's original
premise (refuted, corrected). Not used as evidence: the 65 dead falsify seats' partial transcripts
(only `AuditR24Truth` served as a pointer, then checked against bytes).

Waves (round total 133 of ≤200 seats; the L1 holds the canonical §3 planner seat, no planner seat
dispatched — the validator rejects `planner`):

| wave | seats | role mix | outcome |
|---|---|---|---|
| build (inherited) | 68 | scout 20, executor 19, reviewer 8, scribe 6, mutation-tester 4, critic 4, connector 3, revenger 2, sentinel 1, simplifier 1 | one `task` call after 9 job-cap refusals, accepted 12:42:13 (`build-dispatch-attempts.json`); 68/68 reports, 0 dead |
| falsify (inherited) | 65 | reviewer 29, scout 18, critic 10, mutation-tester 5, connector 2, sentinel 1 | spawned first try 13:08:41 (`falsify-dispatch-attempts.json`); **65 dead**, 0 reports |

No new wave: every attack item of wave 2 was issued to a now-dead seat, and re-issuing those items
is forbidden; the remaining 67-seat budget had no distinct unissued items, so a third wave would
be padding. Residual checks were run by the L1 itself (above), not by seats.

Dead seats (65, last error `Request was aborted` at host kill, not a provider error): ReopenS016–
ReopenS027 (12), EvmOpcodeTruth, EvmR19R21Candidates, EvmR22Candidates, EvmR23Empty, EvmR24Decoy,
EvmR25R26Negatives, EvmFlagsDigests, EvmSelectorsAuthored, EvmUnknownsRules, EvmLimitationsQ13,
EvmCrossLane, EvmReproduceRerun, EvmQualityTable, EvmVersionClaims, JsSourceFacts, JsNamedEdges,
JsDeltaAndCompare, JsEntrypointEdge, JsLabelsExports, JsDestructuringInference,
JsResolutionInference, JsLimitationsQ13, JsCrossLane, JsReproduceRerun, JsQualityTable,
C2ProbeRerun, C2IndependentMutantB, C2ControlDeletion, C2Kaika12OnNew, C2DiffReview,
C2SafetyCriteria, C2PassLineQuotes, C2AxisCritic, CountK, CountCensus, CountFFreshness,
CountInputIdentity, AuditQ12Q13, AuditGateRejects, AuditMistakes, AuditReadme, AuditAmendments,
AuditSourcesContract, AuditMisroot, AuditR24Truth, AuditScorecard, AuditLog,
CriticSeparabilityPost, CriticTrendVerdicts, ConnectorKaidokuPost, ConnectorKasegiPost,
AuditSearchLogPaths, C2OtherConjunctsScope.

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` | pre-registration, probe, before log | `LOG.md:786-791` (Round 61 declaration) |
| `0b6ddf07f33184baf901dd807ddc72a95f4010c1` | C2 controls, C04/C09 entries, S016–S027, Q12/Q13, lesson, A1/A2, build evidence | `LOG.md:795-798` (written in `2e27c6c`) |
| `2e27c6cccb50df3433c96fc4c225b78286e70019` | after measurement, SCORECARD, LOG | `LOG.md:793-799` |
| `6e89c249bfa57891d97706286807bb78ea594e3c` | SOURCES paths and search log; lesson ASAR wording | no own LOG bullet; SOURCES rows logged at `LOG.md:797` |
| `0597e5336fd67654c974fcb05f73353f44d868b9` | falsify evidence + dead-seat receipt; C09 entry and M25 correction | `LOG.md:803-805` |
| `ab580698212258a55e43e9bb9bf6ac78c91eae2a` | replacement-L1 re-measure, LOG resume entry, SCORECARD note | `LOG.md:801-806` |

Lane tip `ab580698212258a55e43e9bb9bf6ac78c91eae2a`, `jj-lane.sh state`: ahead=0 behind=0,
untracked=0.

## Before → after measurements

Probe: `A=<tmp>; git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar <commit> corpus | tar -x -C $A && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-61/measure.py $A`.

| claim | before (`cf02419`) | after (`0b6ddf0`) | re-measured (`0597e53`) | verdict |
|---|---|---|---|---|
| C1 K | `K_HELD_BACKED=4/14` (2.9) | 6/14 (4.3) | 6/14 | measured improvement; pre-registered conjunct "survives the wave-2 attacks" (`claims.md:32`) **not met** — wave 2 produced no result. Reported, not redefined; the operator/closure rules. |
| C2 receipt kill | `C2_RECEIPT_B_KILLED_ATTRIBUTED=0/2` (0.0) | 2/2 (10.0) | 2/2 | improved (narrow regression guard on two scripts) |
| holds | controls 2/2, d2 2/2, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes` | same | same, `probe_exit=0` | held |
| saved inputs | — | `git diff --stat cf02419 0b6ddf0 -- corpus/live corpus/fixtures` empty | empty vs `0597e53` | held |
| entries Q11 | — | both `## Reproduce` exit 0, identical to Provenance | same (14 and 29 lines) | held |
| F / freshness | `COVERAGE 4/8`; 12+6=18 rows | same | same | unchanged |

## Sources & frontier

- Count `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md`: 15 at `cf02419` → 27 at `ab58069`.
- Rows added (12): tier A spec/docs S016–S023 (mined, 8); tier A spec S024 (rejected, supersedes
  S008 under rule 2); tier C community S025 (rejected); tier A own-work S026, S027 (mined).
  Quotes, URLs and access dates: `corpus/lessons/round-61.md` `## Gate` (lines 48-66).
- Rows touched old→new: none (S008 not edited).
- Frontier: README rows C04 and C09 uncovered → held; C03/C05/C07/C08 stay `frontier`.
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`:
  start `revenger ok`, exit 0 (`measure-before.log:28-30`); end `revenger ok`, exit 0, one W04
  (`S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes`) (`measure-after.log`, appended section).
- Mined mistakes M21–M25 (`corpus/lessons/round-61.md:35-44`; count `5 2 3`), M25 rewritten this
  resume. Sourced claim: C1 (entries cite S016–S023, S026, S027).
- Prior outside check intake: `corpus/lessons/round-1-verifier-spotcheck.md` dispositioned at
  `corpus/lessons/round-61.md:20-31`. No `round-60-verifier-spotcheck.md` and no
  `corpus/lessons/operator-*.md` exist.

## Trend verdicts

- **expansion: improved** — two new entry-backed held rows (K 4/14 → 6/14) and 12 opened source
  rows; tempered by C1's unmet wave-2 conjunct.
- **quality: improved** — C2 mutant b 0/2 → 2/2 attributed kills with all holds intact; Q12/Q13
  added; one in-round factual error (M25) found and corrected before closure.
- **discernment: unchanged** — seven rejects recorded, but no outside spot-check landed in-round
  and the falsify wave produced nothing; the non-author closure decides.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` absent; untouched.
- [~] At least one end-to-end domain task executed and logged in LOG.md — unchanged this round (`SHONEN.md:7-8`); new entries are knowledge over saved records, `LOG.md:793-806`.
- [~] Instructions executable by an agent without oral context — entries carry runnable `## Reproduce` blocks, re-run from an archive (`measure-after.log`); no non-author verifier yet.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — both entries carry `## Cross-lane contest (Q10)` (kaidoku prior art, kasegi scope); ADJ-06 stays with the operator.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): no revenger round-61
  files at the fleet root this resume (untracked entries belong to other lanes or `.ufo/state/`;
  untouched). The build wave's six misroots were moved by the predecessor (M24).
- Tool installs: none.
- Routing: no seat dispatched by the replacement L1; the inherited waves used the host role map.
  No provider death recorded (all 65 deaths are the host kill). No Codex cyber_policy refusal.
- L0 questions: none new.
