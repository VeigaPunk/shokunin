# kotoba — round 55 report (hyaku campaign, attempt 1)

Lane HEAD (pushed): `f9244c6c06532c483ff8bfe8e22d475cc6aabfd9` (`jj-lane.sh state` → `local=remote=f9244c6c… ahead=0 behind=0 tracked=0 untracked=0`). Base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`.
Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims (plan `a10240c0`, `plans/round-55.md`):
- **C1 — depth** (lowest owned axis; the learning claim; the sourced claim). Surface: new `SKILL.md` decision table `### Explicit invocation by client`, entry `corpus/knowledge/explicit-invocation-round55.md`, SOURCES S065–S071. Frontier row *Implicit-intent fidelity*.
- **C2 — operability.** Surface: the could-not-evaluate error paths of thirteen registered gates under `verifiers/`.

Work items:
- Plan, both frozen counters and the §9 do-nothing and shortcut control receipts, before data: `a10240c0` (`verifiers/check_explicit_invocation.py`, `verifiers/check_could_not_evaluate.py`, `.ufo/waves/round-55/controls/C1-base.txt`, `C1-shortcut.txt`, `C2-base.txt`, `C2-shortcut.txt`).
- Plan erratum 1, before any C1 content: wave-1 critic `CriticC1Sizing` met the v1 C1 predicate with real quotes that hold no invocation form (W1) and a case flip (W3). Counter v2 is strictly stricter; receipts `controls/C1-shortcut-W1W3.txt` (v1 met, v2 not met) and `controls/C1-v2-controls.txt`: `b04a9005`.
- C1 content: `96155796`. Falsify corrections to its rows and entry: `e0e5cc21` and `f9244c6c`.
- C2 content (eight seat patches, Fix*): `e966cd59`.
- Routed round-54 defect 3 (four over-wide C1 cells narrowed), plus the SKILL.md budget move (anti-pattern prose moved verbatim to `skill-overlap-levers-round51.md`; sha256 `1423f8ce…` on both sides, `ReviewSkillMove`), plus registry rows for the two new counters: `ed3e8996`.
- Routed defect 5 (registry counter closes the probe route and matches exact flag handlers; all-probe control `0 of 26`) and defect 6 (`fault_injection_corpus.sh` harness repairs; self-test exit 0; entry still red on real corpus findings): `4d700b17` (`ReviewRegistryHarden`, `ReviewFaultInjection` HOLD).
- Routed defect 2 and the frontier mistakes: QUALITY Q34–Q37; lesson `corpus/lessons/round-55.md` § Gate, § Mistakes M48–M51, § Routed defects 1–8: `f2cc4099`.
- Routed defect 1: base receipts naming their revision (`build/ExecBaseReceipts.md`; the lane-path checklist is 11/11, exit 0). Tip receipts are in `falsify/NoHarmGates.md`.
- L0 line for the 12 earlier SOURCES in-place edits: fleet `d2b2c5664365d693ca1cc84dd41ae5f92da1ae0f`.
- SCORECARD and LOG: `722e474a`; LOG falsify entry: `f9244c6c`.

Round shape: default, two v1 waves.
- **Build:** 36 seats (scribe 14, executor 12, scout 4, critic 2, mutation-tester 2, connector 1, reviewer 1). Grant: `granted … seats=36 live=25 cap=90`. `MutC2Counter` was cancelled at the settle deadline; its report had already been written at 00:06:05Z.
- **Falsify:** 40 seats (reviewer 31, critic 4, mutation-tester 2, executor 2, scout 1). Grant: `granted … seats=40 live=24 cap=256`. 33 reports. Seven seats were cancelled at the settle deadline (~00:21Z) without reports: ReviewFixBoxProof, ReviewFixMcpInstructions, ReviewFixAssertionFloors, ExecHandProbes, ReviewQuality, ReviewLessonMistakes, ReviewControlsReceipts.
- **Round total:** 76 seats; no dead seat, no refusal, no residual call.
- **Planner seat:** the L1 held it. Its data-walk rode scout `ScoutPlanWalk`.
- **Bounds incident:** seat `CriticC2Sizing` ran a real `git status` at the fleet root (index mtime refreshed, no content change). It disclosed this itself; recorded as M51.
- **Misroot sweep** (`ScoutMisroot`): no untracked fleet-root file names this round.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `a10240c0` | plan, frozen counters, control receipts | LOG § Round 55 |
| `ed3e8996` | routed defect 3, SKILL.md verbatim move, registry rows | LOG § Round 55 |
| `b04a9005` | erratum 1, C1 counter v2, shortcut receipts | LOG § Round 55 |
| `96155796` | C1 content | LOG § Round 55 |
| `4d700b17` | routed defects 5 and 6 | LOG § Round 55 |
| `e966cd59` | C2 gate fixes | LOG § Round 55 |
| `f2cc4099` | QUALITY Q34–Q37, lesson | LOG § Round 55 |
| `f0e6b695` | build-wave evidence | LOG § Round 55 |
| `722e474a` | SCORECARD and LOG, C2 receipt | LOG § Round 55 |
| `e0e5cc21` | C1 falsify corrections, C1 receipt | LOG § Round 55 falsify |
| `f9244c6c` | falsify evidence, entry corrections, census end | LOG § Round 55 falsify |

## Before → after measurements

**C1** — `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch`, run with the v2 counter (`b04a9005` bytes, sha256 `e13eb88d…`). Receipts: `.ufo/waves/round-55/C1-measure.txt` and `falsify/W2RerunC1.md`.

| revision | output | exit |
|---|---|---|
| `f0e5de82` | `user-typed invocation forms found on the live page 0 of 0; new ground 0` | 1 |
| `96155796` | `user-typed invocation forms found on the live page 5 of 5; new ground 4` | 0 |
| `f0e6b695` | same as `96155796` | 0 |

The predicate needs F ≥ 4 and G ≥ 2, so it is met. The v1 line is reported beside it, never in its place: `7 of 7; new ground 7`. v1 is met by a shortcut, which is why erratum 1 exists.

In substance only Cursor's `/skill-name` and opencode V2's `@skill-id` are forms new to the lane. Codex `$…` and Copilot CLI `/…` were held at base under other example names (`CriticNewGround`). G ≥ 2 holds on the new forms alone, with no margin.

**C2** — `python3 -B verifiers/check_could_not_evaluate.py --rev <rev>`, frozen at `a10240c0`, sha256 `0c1258e2…`.

| revision | output | exit |
|---|---|---|
| `f0e5de82` | `could-not-evaluate probes honoured 13 of 25; controls held 13 of 13` (`controls/C2-base.txt`) | 1 |
| `e966cd59` | `25 of 25; controls held 12 of 13` (`C2-measure-e966cd59.txt`, load average ~105) | 1 |
| `f0e6b695` | `25 of 25; 12 of 13`, measured by `W2RerunC2` and twice by `CriticC2Landed` (also with `PYTHONSAFEPATH=1`) | 1 |

The only miss is `check_assertion_floors.py` exiting 2 on the real revision. It runs a nested `verify_harness_independent.py --self-test` under a 120 s timeout, and that self-test takes 185–222 s under the host load. **A miss as declared.**

Separately, wave-1 critic `CriticC2Sizing` met the frozen predicate with three shortcuts, after seats had already scored:
- a remap of findings from exit 1 to exit 2;
- an entry check alone;
- an `argparse` shadow module.

The predicate was therefore not sound (M50). It was not amended.

## Sources & frontier

SOURCES rows went 64 → 71 (`grep -c '^| S[0-9]' corpus/SOURCES.md`).

Census, start and end: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `kotoba ok`, exit 0 at both. Receipts: `.ufo/waves/round-55/census-start.txt` (23:11:55Z) and `census-end.txt`. The six W04 duplicate-url warnings at start were S018, S019, S021, S054, S055 and S056.

- **Rows added:** S065–S071, all tier A, `mined`, opened 2026-10-22. Gate quotes and fetch records are in the lesson § Gate. All seven were re-opened by falsify seats: the bytes and sha256 were identical, and the quotes were byte-exact or carried a stated normalisation.
- **Rows touched:** none. `check_sources_append_only.py --base f0e5de82 --rev f0e6b695` → `0 protected-cell changes`, exit 0 (`NoHarmScores`).
- **Rejections:** 5, listed in the lesson Gate.
- **Frontier:** row *Implicit-intent fidelity* advanced in part. See the `corpus/README.md` Round 55 note; the intent-labeling pass itself is not held.
- **Mined mistakes:** M48 (receipt pinned to the wrong revision), M49 (hollow C1 control), M50 (C2 predicate reachable by a shortcut, found after data), M51 (bounds incident).
- **Sourced claim:** C1 rests on S065–S071.

## Gate

Real rejects, each with its reason:
1. The v1 C1 counter as the claim's rule: met by real-text shortcut W1, so it was replaced before data (erratum 1).
2. The Copilot CLI reference page `cli-command-reference.md:1277`: already base rows S031, S038 and S056.
3. The Codex `build-skills.md:218` `$skill`: held at base, and re-citing it would re-score held knowledge.
4. Gemini `skills.md` `/skills`: a listing command, not an invocation.
5. The Copilot concept route: still 404; the route move is recorded and the reject decision stands.

## Trend verdicts

- **expansion: improved.** Knowledge entries went 41 → 42, and seven sourced rows were added on a Frontier row. The new forms are Cursor's and opencode V2's.
- **quality: improved.**
  - Four over-wide round-54 cells were narrowed.
  - The registry counter's probe-route and substring holes were closed: the all-probe control went 26/26 → 0/26.
  - The fault-injection harness was repaired, though the gate stays red on real corpus findings.
  - Eight gates now exit 2 on an unknown revision or with git absent; the red anchors and real verdicts are unchanged (`ReviewFix*`).
  - Q34–Q37 were added.
- **discernment: improved.**
  - Two hollow predicates were caught by the lane's own critics. One was fixed before data; one was reported, not amended.
  - Falsify seats caught five over-wide cells, all corrected before the report.
  - The C2 miss is reported as a miss.

No axis was harmed:
- SCORECARD scores are identical at base and tip.
- LOG and SOURCES are append-only; no files were deleted; SKILL.md went 599 → 598.
- Finding delta `f0e5de82..722e474a`: `new 0, resolved 1`, exit 0. Registry: `26 of 26`.

One caveat: the floors gate exits 2 at the tip. Its cause is the host-load timeout, which also hits a code path this round did not change. That gate's change added only a git preflight (`W2RerunC2`, `CriticC2Landed`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md § Explicit invocation by client (S065–S071), re-opened by falsify seats `Reopen*`
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `corpus/knowledge/cold-run-round11.md` (unchanged this round)
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md` (unchanged)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `falsify/../build/ConnSiblingOverlap.md` (sibling scan, no absorption)

## Open L0 questions, installs

- **L0:** `kotoba | round-55 |` the 12 earlier SOURCES in-place edits, ratify or correct (fleet `d2b2c566`). The round routed around it.
- **Installs:** none, by the L1 or any seat.
