# souji — round 63 (attempt 1): honest stop

Lane `souji` (`/home/vgpnk/Projects/shokunin/souji-shokunin`), lane base `728ab685617e412172a8e5cb6260f7098b486aec`,
final lane tip `ed76491462451e5b0a8f165da16577f129e1ed87` (pushed; `ls-remote origin refs/heads/master` matches).
Outcome: **neither declared claim is admitted.** No production writer, SKILL.md or knowledge bytes changed; no
preregistration was frozen. The lesson is `corpus/lessons/round-63.md`.

## Work performed

**Declared claims (2, distinct axes; not admitted):**

- **C1, operability.** The receipt writer refuses a change made by the wrapped command while it runs (flag set, tracked
  edit, untracked creation) and classes unmerged, gitlink and absent index entries under their own tokens. Target axis
  operability (score 8). Evidence: candidate `eba4f7e0d1218d88158459426de3ad505e7401201af7ad006415daed31f9586f`,
  `.ufo/waves/round-63/w1/S63ExecWriter/souji-receipt-write.py`; diagnostic counters in `census/round-63/`.
- **C2, calibration** (lane's lowest owned axis, score 7). Three SKILL.md statements about the writer's enforced scope
  agree with the writer bytes in both directions. Evidence: `census/round-63/c3-counter.py`, `census/round-63/c3-statements.tsv`.

**Why not admitted (lesson `corpus/lessons/round-63.md` `## Mistakes`):** the candidate was scored before any predicate
froze (M2); the C1 H4 sparse row was removed after the sentinel measured it unrealizable (F6, M1); the C2 population was
narrowed after a seat's scored run (M3). Under the lane's rule that a rule changed after scoring is not the claim's rule,
both are recorded as unprovable as declared. No preregistration was frozen, to avoid laundering the change.

**Work items, each with evidence:**

- Protocol and state load: MISSION, AXES, CORPUS, LEARNING, protocol files, `SCORECARD.md` (planned r63), QUALITY
  Q119–Q123, round-62 lesson and both round-62 spot-checks (`corpus/lessons/round-62-verifier-spotcheck.md`).
- Wave: **one v1 wave, 11 seats**, validated and dispatched through the inline handoff
  (`.ufo/waves/round-63/w1.ready`, `.ufo/state/inline-dispatcher.log` `spawned souji 63 w1 11`); WAVE-DONE received
  from Main. Seat mix: scout 1, executor 3 (writer, C1 counter, C2 counter), mutation-tester 1, reviewer 2, critic 1,
  sentinel 1, scribe 1, connector 1. Attack seats 5/11 (45%). Planner held by the L1 (validator refuses a planner
  role; recorded). Residual call: none. Dead seats: none observed in deliverables. Seat answering models: not verified.
  Results file `.ufo/waves/round-63/w1-results.json` (11 seats).
- Attacks that shaped the design (`.ufo/waves/round-63/w1/`): critic `S63CriticClaims.md` (C2 misattributed to
  operability; C3 mixed surface; comment-only marker forgery); reviewer `S63ReviewerDesign.md` (H1–H8, C2.1–C2.7,
  C3.1–C3.5, including H3 and H5 critical); reviewer `S63ReviewerCandidate.md`; sentinel `S63SentinelScope.md`
  (F1 HIGH allow-dirty; F6 H4 unrealizable; F10 population); mutation `S63MutKill/kills.txt`.
- Candidate writer and self-tests: `S63ExecWriter/REPORT.md` (selftest 20/20, r60 8/8, r62 counter regress PASS).
- Frozen-candidate counters rerun by the L1 (committed bytes, in scratch): C1 selftest `cases=8 pass=8 fail=0`;
  C1 candidate `new_forgeries=0 class_mismatches=0 regress=PASS` EXIT 0; C2 candidate `new_class_mismatches=0` EXIT 0;
  C3 selftest `cases=7 fail=0`.
- Controls committed before any freeze (commit `d7bd4ff2`, then `ed764914`): C1 and C2 do-nothing red; C3 do-nothing
  red; C3 kind-only forgery red.
- Source work: scout `S63ScoutSources` probed the gitlink mode, sparse absent S, and the unmerged `M` tag; the `M` letter
  is already in the committed S292 capture. S294 row added (below).
- Connector `S63ConnectorOverlap`: read `shokuknow/merge/souji/MERGE-REPORT.md` read-only; no theme adopted; no
  `considerthese/` directory.

## Landed changes

| commit | change | LOG.md entry |
|---|---|---|
| `d7bd4ff2` | pre-freeze controls, counters, matrices, statement population, wave evidence (`census/round-63/`, `.ufo/waves/round-63/`) | Round 63 |
| `703a724f` | S294 row (`corpus/SOURCES.md`), round-63 lesson, round-62 correction, SCORECARD and LOG entries, S294 capture | Round 63 |
| `e984223d` | restore S292 used-by to one path (census E11 flagged the two-path cell; the first attempt was a conformance defect, fixed) | Round 63 |
| `ed764914` | C3 do-nothing and kind-only forgery control receipts | Round 63 |

Not landed: the candidate writer (`eba4f7e0`), SKILL.md (round-62 R1 overreach still present at SKILL.md:830), knowledge
entries. Routed to round 64 (lesson `## Routed to round 64`).

## Before → after measurements

Counting commands (run by the L1 on committed bytes; the `<dir>` is a scratch work dir outside the lane, not `/tmp`,
not `TMPDIR`). Diagnostic only: none of these is a frozen predicate.

| claim | before (do-nothing, base bytes `728ab685`) | after (candidate `eba4f7e0`, not landed) | counting command | measured at |
|---|---|---|---|---|
| C1 in-run refusal + edge classes, 9-row matrix | `new_forgeries=4 class_mismatches=4` EXIT 1 | `new_forgeries=0 new_honest=3 class_mismatches=0 regress=PASS` EXIT 0 | `python3 -B census/round-63/c1-counter.py --root . --matrix census/round-63/c1-matrix.tsv --base-rev 728ab685617e412172a8e5cb6260f7098b486aec --new-tool .ufo/waves/round-63/w1/S63ExecWriter/souji-receipt-write.py --work <dir>` | controls `d7bd4ff2`; receipt `census/round-63/records/c1-after-candidate-eba4f7e0.txt` |
| C2 edge classes H1–H3, 5-row matrix | `base_class_mismatches=3` EXIT 1 | `new_class_mismatches=0` EXIT 0 | `python3 -B census/round-63/c2-counter.py --root . --matrix census/round-63/c2-matrix.tsv --base-rev 728ab685617e412172a8e5cb6260f7098b486aec --rev 728ab685617e412172a8e5cb6260f7098b486aec --tool .ufo/waves/round-63/w1/S63ExecWriter/souji-receipt-write.py --work <dir>` | receipt `census/round-63/records/c2-after-candidate-eba4f7e0.txt` |
| C3 statement agreement, 3 SKILL rows | `findings=1` (s2 overreach) EXIT 1 | not measured (no after-wording landed) | `python3 -B census/round-63/c3-counter.py --root . --rev 728ab685617e412172a8e5cb6260f7098b486aec --tsv-rev d7bd4ff2743b4e1cb84217301c95340ebfda7634` | `census/round-63/controls/c3-do-nothing.txt` |
| C3 kind-only forgery control | `findings=4` EXIT 1 (after-wording on base writer) | — | same, `--rev 74f2aee258eb19aae7b4a1b21ac195acf9f6a1b5` (scratch commit) | `census/round-63/controls/c3-kind-only-forgery.txt` |

Owned scores unchanged: calibration 7, coverage 8, operability 8. No reproducible 0–10 mapping exists (open L0).

## Sources & frontier

- `SOURCES.md` rows, before → after: **216 → 217** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
  Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` **rc 0 at start and rc 0 at end**
  (`souji ok`; 68 W04 advisory warnings at end).
- Rows added by tier: **S294 (tier A, docs, mined)** — git-fast-import(1), mode 160000 is a gitlink; located quote 13
  words (tag-stripped offset 31053, raw 109019, contiguous); capture `census/round-63/sources/s294-git-fast-import.html`,
  sha256 `4830e69cf2f4bb8971361a6b8b9b7f13e9c6f252b11afc3702dff866b70d72e9`. Opened 2026-11-05.
- Rows touched old→new: S292 `used-by` widened to two paths in one cell and **restored to the original single path**
  (census E11; net change zero). S292's `M`-tag quote was re-located in the committed capture (no new row).
- Frontier rows advanced: none (F1 stays `frontier, entries held`). The gitlink and sparse-S limits are named in the lesson,
  not admitted as knowledge.
- Assimilation: none. `considerthese/`: absent in this lane.
- Connector overlap and assimilation scan: `S63ConnectorOverlap` (read-only).

## Trend verdicts

- **expansion: unchanged.** One sourced row (S294) and no knowledge entry on uncovered ground; no capability row.
- **quality: unchanged.** No shipped change; the candidate beats do-nothing on its counters but is not landed or admitted.
- **discernment: unchanged.** Four chronology and scope defects were found by the lane's own checks and recorded (M1–M4);
  no outside non-author spot-check of this round's gate decisions yet (pending).

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Mistakes (round 63)

M1 unrealizable frozen matrix row (H4); M2 candidate scored before freeze; M3 population narrowed after a scored run; M4 round-62
quote-location misstatement (appended correction in `corpus/lessons/round-62.md`). Lesson `## Mistakes` carries the captured-by
and fix columns; no fix is counted as shown able to fail. Misroot sweep (below): no seat or L1 file landed at the fleet root.

## Open L0 questions (appended to `.ufo/l0-questions.md`; not answered)

1. Edge-class refusals (unmerged / gitlink / absent): operability (Q59, round-62 F1) or coverage (round-25 C2 row, SCORECARD)?
   The lane record holds both precedents; the next claim cannot cite either without a ruling.
2. Still open from round 62: `## MACHINE BLOCK` preregistration binding; numeric axis mapping.

## Tool installs

None. No pacman transaction. No host sysctl or service touched (the sysctl incident in the run notes was not caused by this
round's seats).

## Pre-report gate and sweeps

- `git -C souji-shokunin ls-remote origin refs/heads/master` → `ed76491462451e5b0a8f165da16577f129e1ed87` (final lane hash).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows ` M .scratch/run15-state.json` only
  (orchestrator-owned; not touched). No untracked fleet-root file from this lane's seats.
- Scratch: `/fast/scratch/hyaku/souji-r63/` and `/fast/scratch/hyaku/tmp-souji63/` removed after landing.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md (unchanged this round);
  `corpus/SOURCES.md` S294; `corpus/lessons/round-63.md` `## Gate`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 63`; `census/round-63/records/c1-after-candidate-eba4f7e0.txt`
  and `c2-after-candidate-eba4f7e0.txt` (diagnostic, not admitted).
- [~] Instructions executable by an agent without oral context — `census/round-63/c1-counter.py`, `c2-counter.py`,
  `c3-counter.py` with their matrices and population (commands above).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`; connector read-only overlap scan
  `.ufo/waves/round-63/w1/S63ConnectorOverlap.md`.
