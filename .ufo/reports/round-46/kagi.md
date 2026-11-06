# kagi round 46 (attempt 1) — report

Lane: `kagi-shokunin` (secrets & vault ops). Branch `master`. Lane final hash (ls-remote verified after the last lane commit): **`f4a33d3df3996f947114743b9f6317ad7dc323e6`**. Shape: one v1 build wave of 12 seats (run-15 band 8–16); no residual call; no wave 2. Round total: 12 seats, all settled (WAVE-DONE received; `.ufo/waves/round-46/build-results.json`). Dead seats: none.

Commits: predeclaration `44808ced56359c98f35995178fb24a6482899263`; candidate `0bd88889689115141d7bfb5a98deee62a1b3b627`; landing (wave evidence + final receipts) `f4a33d3df3996f947114743b9f6317ad7dc323e6`. Claim BASE `f5977284a8ce5bab09252be8196ee5dc18489926`.

## Work performed

Declared claims (two, two distinct axes):

- **C1 operability**: the declared-claim gate's own `--selftest` (`corpus/claims-declared.sh`) kills the three frozen mutants of its round-45 plan-to-manifest leg. All four equivalent mutants still pass and the real tree stays CLEAN. Target 3. This closes round-45 closure routed item 2 and sentinel S-07.
- **C2 freshness**: all 29 BASE `on-release` registry rows were re-observed live on 2026-11-06, and the release-clock gate reads CLEAN on the real tree again. It had read FAILED on every tip from the round-39 landing `4776f71` through BASE. Target 29.
- Axis duty: all six axes tie at 9, so each claim works a tied-lowest axis. The stagnation condition holds (the last capability round is 40). Its capability/frontier directive is declined this round (critic D-9; lesson E46-2).

Work items, with evidence:

- Frozen plan and instruments (`44808ced`): `plans/round-46.md`, `plans/round-46-c1.sh`, `plans/round-46-c2.sh`, `plans/round-46-controls.py`.
  - The pre-freeze controls were executed and committed before any seat scored: 11 controls, all MATCH (`.ufo/waves/round-46/controls/controls-prefreeze.txt`).
  - C1 controls: do-nothing 0; reference positive 3; byte-keyed forgery 0 (killed 3, equiv 0); constant-PASS forgery 0; broken-real forgery 0.
  - C2 controls: do-nothing 0; live positive 29; dates-only forgery 0; S098-deletion forgery 0; fired-row re-cadence 28; hand-written receipt 29 (named ceiling).
  - BASE receipts: `controls/c1-base.txt`, `c2-base.txt`, `gates-base.txt`, `census-start.txt`, `instrument-sha256.txt`.
- Failure onset: the L1 bisected the release-clock gate over six tips (`plans/round-46.md` §C2). The first red tip is `4776f71` (round 39).
- C1 candidate (`0bd88889`): `--run-selftest` cases 9–12 (seat K46ExecSelftest wrote 9–11; case 12 comes from reviewer K46RP-02). The diff hunks sit only inside the self-test block (lines 36..108; `final/measured-at-candidate.txt`).
- C2 candidate (`0bd88889`):
  - Live receipt `.ufo/waves/round-46/final/observe-r46.json`: 29 records, failed 0, sha256 `6091c529…5fa7`.
  - `corpus/release-clocks.tsv`: S040/S041 rows retired (verbatim copies in the lesson); S098 bound to its capture quote `Revision 25`; rows synced from the receipt.
  - `corpus/release-clock.py`: default receipt path and digest repointed. The round-36 and round-26 receipts are kept as history.
  - `corpus/source-fetches.tsv`: S098 quote/location changed (old→new recorded in the lesson §Gate).
  - `SKILL.md:48,787` and `PROVINCE.md:75` corrected.
- Non-author live re-observation (K46ReviewerLive): 29/29 ids agree, with byte-identical bodies (`build/K46ReviewerLive/report.md`). Scout K46ScoutFeeds re-observed at 19:10Z and also agrees (`build/K46ScoutFeeds.md`).
- M46-1 fix: ledger R36-03's expectation was migrated from 30/15 to 29/13 (`.ufo/waves/round-46/expectation-migrations.json`). Red witness: at BASE the command reads FAILED, rc 1 (`final/r36-03-red-witness.txt`). Added QM57.
- Curation:
  - `corpus/README.md` gains coverage-map rows for the ISO/IEC 11770-3 and feed-token-boundaries entries (closure routed 1).
  - Erratum E46-1 covers the round-45 receipt hygiene (closure routed 3).
- Pre-candidate attacks were turned into candidate-side legs, each recorded in `final/measured-at-candidate.txt`. No frozen sentence changed.
  - Reviewer K46RP-01: the diff leg.
  - Reviewer K46RP-02: case 12.
  - Reviewer K46RP-03: the mutants exit rc 1 with FAIL lines.
  - Reviewer K46RP-04/05: receipt dates and digest checked.
  - Critic D-6: no fired row was rearmed.
  - Critic D-12: the manifest rows and the post-move section landed in one commit.
- Planner mapping: the L1 held the planner seat. The validator rejects `planner` as a swarm role.

Tooling: no tool was installed or upgraded (all seats report "none"). pacman stayed paused. No host sysctl was changed.
Refusal boundary: no secret value, token, cookie, vault field or `op://` reference path was read or written (sentinel `build/K46Sentinel.md`). Every fetch was a public GET.

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Predeclaration: plan, counters, controls, BASE receipts | `44808ced56359c98f35995178fb24a6482899263` | `LOG.md` Round 46 |
| Candidate: C1 self-test cases; C2 clocks/receipt/repoint; R36-03 migration; QM57; README rows; SKILL/PROVINCE; lesson; SCORECARD; manifest rows; stamps | `0bd88889689115141d7bfb5a98deee62a1b3b627` | `LOG.md` Round 46 |
| Landing: wave evidence (12 seats), `final/measured-at-candidate.txt` | `f4a33d3df3996f947114743b9f6317ad7dc323e6` | `LOG.md` Round 46 (verdict line points at the final receipt) |

## Before → after measurements

| Claim | Counting command | BASE `f5977284…` | Candidate `0bd88889…` |
|---|---|---|---|
| C1 operability | `bash plans/round-46-c1.sh <rev>` | `value=0 killed=0 positive=1 equiv=1 real=1` (m1=m2=m3=0) | `value=3 killed=3 positive=1 equiv=1 real=1` (e1..e4=0, m1=m2=m3=1; `PASS (12 cases)`; `CLEAN (claims=19)`) |
| C2 freshness | `bash plans/round-46-c2.sh <rev>` | `value=0 fresh=0 default=0 pinned=0 kept=1` (gate FAILED rc 1) | `value=29 fresh=29 default=1 pinned=1 kept=1` (`RELEASE_CLOCK: CLEAN (on_release=29 bound=29 unbound=0 observed=29 fired=13 derived=15)`) |

Supporting measurements at the candidate:

- Release-clock self-test: `PASS (116 cases)`.
- R36-02 → `0`; R36-03 → CLEAN.
- Gates: `QUOTE_LOCATE: CLEAN located=8`; `ANCHOR_PINS: CLEAN`; `STAMP_DRIFT: rows=123 drift=0`.

Harm check:

- Self-description sweep: n=7 at BASE and n=7 at the final tip, with identical lines (archive trees).
- Fleet census: `kagi ok` rc 0.
- The lane-local census FAILED with 3 findings at both BASE and the candidate (S094/S099; pre-existing, routed).

Frozen kill rules: none fired.

Named ceilings (from controls and attacks, all routed to round 47):

- A hand-written or date-shifted receipt scores 29. The non-author live re-observation is the leg that can catch it.
- C1's KILLED counts any non-zero exit.
- Ten counter-mutation survivors (`build/K46MutCounters.md`).

## Sources & frontier

- Registry rows before → after: **102 → 102**, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` returned rc 0 at round start (`controls/census-start.txt`) and rc 0 at round end (`kagi ok`).
- Rows added by tier: A 0, B 0, C 0.
- Rows touched old→new: none in SOURCES.md. The S098 capture row in `corpus/source-fetches.tsv` had its declared quote changed from the title to `Revision 25` and its location corrected (lesson §Gate).
- Sourced claim: C2 rests on S033, S034, S035, S036, S037 and S098, each opened 2026-11-06. The lesson §Gate carries the URL, the newest stable version and a ≤25-word located quote for each.
- Frontier rows advanced: none.
- Mistakes mined:
  - M46-1: R36-03 was red from round 39 onward and dismissed as inherited.
  - M46-2: a forgery control matched itself (caught pre-freeze).
  - M46-3: L1 misroot of one failed-run transcript into the fleet root. It was deleted, and no lane value was lost.
  - M46-4: stale SKILL/PROVINCE lines.
- Misroot sweep: `git status --porcelain` on the fleet shows only `.scratch/run15-state.json` (orchestrator-owned).
- Assimilation: none (no staged `merge/kagi/` theme matches either claim).
- Considerthese: no new file after `2026-10-26.md`.
- Open curation (scout §3): S040/S041 carry an overdue ISO recheck `2026-11-05` while S095/S096 supersede them. This is routed and not changed.

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry or ground. The coverage-map rows index held entries.
- **quality: improved.**
  - A held gate that was red for seven tips is CLEAN over a live observation, with 29/29 non-author agreement.
  - The declared-claim gate's self-test now detects four weakenings of its leg, including the axis-blind one.
  - Two stale self-descriptions were corrected.
- **discernment: improved.**
  - The S098 title clock was refused in favor of a revision quote that can fire.
  - The duplicate ledger row (R46-01) was refused in favor of migrating R36-03.
  - The frozen M46-1 `captured-by: none` was corrected to R36-03 on non-author evidence. QM57 is lesson-backed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md:48` (release-clock decision row, corrected this round). No non-author verifier for this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md:20` (round-3 pipeline entry). This round's live re-observation of 29 clocks is a domain fetch task, not the vault pipeline.
- [~] Instructions executable by an agent without oral context — evidence: `bash corpus/claims-declared.sh --selftest` (PASS, 12 cases); `python3 corpus/release-clock.py` CLEAN.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md:75` corrected; connector `build/K46Connector.md` reports no subject overlap for either claim.

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Wave evidence and WAVE-DONE

- Wave `kagi-r46-build`, one v1 wave, 12 seats:
  - executor 3: K46ExecSelftest, K46ExecClocks, K46ExecLedger
  - scribe 1: K46ScribeCurate
  - scout 1: K46ScoutFeeds
  - connector 1: K46Connector
  - reviewer 2: K46ReviewerPlan, K46ReviewerLive
  - critic 1: K46CriticClaims
  - mutation-tester 1: K46MutCounters
  - sentinel 1: K46Sentinel
  - revenger 1: K46Revenger
- Attack share is 4/12 = 33 %.
- Dispatch: `build-dispatch.json` (spawn 12); `build.ready` → `build.ready.dispatched`. WAVE-DONE was received and all 12 seats settled.

## Open questions

- No new L0 question this round. Earlier kagi L0 lines are routed around, not treated as answered.

## Verdict on the round

C1 (0 → 3) and C2 (0 → 29) each measured at their frozen targets at the candidate, and no frozen kill rule fired. No axis was harmed (sweep and census readings are unchanged from BASE). The non-author closure rules on admission.
