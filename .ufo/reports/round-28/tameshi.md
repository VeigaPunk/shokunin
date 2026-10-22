# tameshi — round 28 report (TameshiR28, attempt 1)

Lane head (pushed): `1076914abf513c723d454b9d35b7f04d9101d3af`. Base: `06b59b93697c9b0a8795ac2d0fe3d0bd7e18572c`.
Verdict proposed by the lane: **C1 missed — honest stop** (60/64 → 62/64; target 64/64 not reached).

## Work performed

Declared claims: **one** claim. C1 works **calibration** (lowest-scoring non-retired axis, 6). It is a harm repair routed by
`corpus/lessons/round-27-verifier-spotcheck.md` "Routed defects" item 1. Counter (frozen since round 27, byte-identical at base and head):
`python3 .ufo/evidence/round-27/c1-measure.py --repo . --rev REV`. Target at the landed head: `covered=64/64 restraint=8 box3_mismatch=0`, exit 0.
The claim counts mismatches between self-assessment and repo state: SHONEN box 3 `[~]` cites the cold-read ledger, but the monitor does not credit the whole page.

- Content revision `b05d2ee`: SKILL.md "Round-21 gate/probe registry" gets an appended Round-28 correction. It covers the ReRead03 gap-blocking finding: `.ufo/evidence/round-21/c2-count.py:19,52` reads the live lane through `FLEET`. The correction is at `SKILL.md:2086-2102`.
- Frontier: S059 re-opened (Bazel Remote Caching), `used-by` extended, lookup note and `Next unused id: S092` appended (routed item 3) — `corpus/SOURCES.md`, lesson `## Gate`.
- Mined mistake (`corpus/lessons/round-28.md` `## Mistakes` 1): one blank line appended to `corpus/SOURCES.md` drops the monitor 60 → 50. README → 55, QUALITY → 57, SHONEN → 59, LOG/SCORECARD → 60, all six → 47. Receipt: `.ufo/evidence/round-28/append-probe.txt`. Seat MutateAppendProbe reproduced the receipt independently (`.ufo/waves/round-28/w1/MutateAppendProbe.md`).
- Round shape: **one v1 wave** (policy v1). `spec-w1.json` → `dispatch-w1.json`, 38 seats: reviewer 30, executor 3, mutation-tester 1, critic 1, connector 1, scout 1, scribe 1. The 28 cold reads are two independent fresh readers per uncovered section (14 sections) at `b05d2ee`; the other 10 seats are falsifiers or recon. No wave 2: after the dead and late seats, fewer than 32 genuine attack items remained before the freeze. No residual call. **Round total 38.** Planner seat: held by the L1; the planning data walk rode the scout ScoutNextFrontier.
- Dead seats (12, never replaced). Each died with `Retry budget exhausted after 5 retries: Devin stream error resource_exhausted: Reached free model rate limit … reset … at 19:43 UTC`: Read01A, Read02A, Read03A, Read05B, Read07B, Read10A, Read11A, Read12A, Read12B, Read13B, Read14A, ReviewSkillCorrection.
- Late at the cut: Read14B (still running at report time; not assembled). RegistryCheckAtR finished after the cut, and its report was committed separately (it is not cold-read evidence). Read04B, Read05A and Read06A finished at about 19:24Z and were assembled in a second pass; Read09B finished at 19:26Z and was assembled in a third pass. Each pass rewrites the ledger from the `b05d2ee` bytes and appends every finished report.
- Falsifiers: CriticC1 (`w1/CriticC1.md`): honest delta is 4 sections over base, not 14, and 64/64 needs every read to pass. RerunC1 (`w1/RerunC1.md`): confirms base 60/64 and `b05d2ee` 50/64, with the counter byte-identical. RerunCensus (`w1/RerunCensus.md`): census exit 0 at base and `b05d2ee`, and S059 changed only `used-by`. ReopenS059 (`w1/ReopenS059.md`): agree; it found a quote word count 13→14, corrected in the lesson. ConnectorOverlap: overlaps in souji, mori and tabi, report-only. ScoutNextFrontier ranked routed items by credit-drift cost: 6 (runner, 199 entries) > 3 (99) > 4 (54) > 5 (31). ScribeMistakes drafted 14 candidate rows.

## Landed changes

| Commit (landed, pushed) | Content | LOG.md entry |
|---|---|---|
| `b05d2ee8e7f80b18428e8f38b9ad535cf9d99a1a` | SKILL Round-21 correction, S059 re-open, lesson draft, append probe, census start | `LOG.md` "Round 28" bullets 1–3 |
| `a20e2ba00e6903283faf7462993a3898d70f3853` | 12 cold-read entries appended (ledger 354 → 366), wave records, traces, lesson mistake 2 | bullet 4 |
| `ae7a11de7f50b223ffead2a031cc898ad1099493` | SCORECARD/LOG round-28 blocks, monitor explain receipt | bullet 4 |
| `c30926e38bc6204f33f33cb84248b7caf27e8324` | late reads re-assembled (ledger appended from the `b05d2ee` ledger: 354 → 369, prefix equal as data) | bullet 5 |
| `a269d90ec20d06d8d6aeb63ef5f3d51ce8d6cf9a` | C1 reading 61/64 appended to SCORECARD/LOG | bullet 5 |
| `bdf0aa5e4f74273df33db62f7426a685347edb9a` | Read09B re-assembled (ledger 354 → 370) | bullet 6 |
| `c4e00982f78f178c2146b6e5943822e75e16ad09` | final C1 reading 62/64 appended to SCORECARD/LOG | bullet 6 |
| `1076914abf513c723d454b9d35b7f04d9101d3af` | late seat report RegistryCheckAtR (no cold-read input) | — (wave record) |

Every commit went through the `jj-lane.sh` helper, and every hash above is from its `landed` line. The ledger stays append-only: receipt `.ufo/evidence/round-28/coldread/append-receipt-w1.json` (`prefix_entries_equal_as_data: true`). Format is kept: indent 2, `git diff --numstat` shows additions only, which closes the re-indent part of routed item 7.

## Before → after measurements

| Claim | Command | Before (06b59b93) | After | Measured commit |
|---|---|---|---|---|
| C1 | `python3 .ufo/evidence/round-27/c1-measure.py --repo . --rev REV` | `covered=60/64 restraint=6 box3_mismatch=1`, exit 1 | `covered=62/64 restraint=6 box3_mismatch=1`, exit 1 | `bdf0aa5e…` (receipt `c1-after-final2.stdout`) |

Intermediate readings: `b05d2ee` 50/64 (own SOURCES edit), `a20e2ba` 60/64, `c30926e` 61/64. The Read09A entry for "Effective expectation reconciliation — round 14" records an input digest that does not match at the revision (`input-drift:.ufo/evidence/round-14/context-missing-env.json`), so it does not credit; Read09B credits that section. Still uncovered at the head:
- "Round-18 gate/probe registry": both readers dead.
- "Round-21 gate/probe registry": one reader dead, one late.

Receipts: `.ufo/evidence/round-28/c1-after-ledger.stdout`, `c1-after-final.stdout`, `c1-after-final2.stdout`, `monitor-a20e2ba-explain.json`.

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
- Start, at `06b59b93` in a mirror: exit 0, `ok`, W04 warnings only. Receipts: `.ufo/evidence/round-28/census-start.{stdout,exit}`.
- End, at the head: exit 0, `ok`, the same W04 set.

Rows 89 → 89 (`grep -c '^| S[0-9]' corpus/SOURCES.md` at base and head; no tier change; 0 added). Touched row: S059 `used-by` changed from `corpus/knowledge/input-keyed-coldread-credit.md` to that path plus `, corpus/lessons/round-28.md`. Status `mined` and recheck are unchanged.

Sourced claim: C1's mined mistake cites S059, re-opened this round (lesson `## Gate`: quote, location and HTML sha256 `9e3a2ebb…`). Seat ReopenS059 and seat RerunCensus both noted that S059's pinned markdown-alternate digest `0d362d11…` no longer reproduces (live `266915c5…`). Fixing that needs a supersedes row next round. No F-row advanced.

## Trend verdicts

- **expansion: unchanged.** No new entry or row; S059 was re-opened, not added.
- **quality: improved.** Two lesson-backed fixes landed: the Round-21 section correction against `c2-count.py:19,52`, and the stale next-id line (routed item 3). The sections it covers are not yet re-credited, and the one fresh reader of Round-21 is late.
- **discernment: improved.** The input-drift mechanism behind the round-26 harm is now measured file by file and reproduced by a non-author seat. Lesson Mistake 1 carries a failing case. A drafted duplicate source row was caught by the census before commit (Mistake 2).

Calibration remains harmed against the pre-harm round-26 base (62/62, restraint 8). Relative to this round's base, no axis is harmed: 60 → 62, and `depth_score` 9 → 9.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion (`SHONEN.md` box 1), no independent verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion (box 2).
- [~] Instructions executable by an agent without oral context — monitor 62/64 at `bdf0aa5e` (`.ufo/evidence/round-28/c1-after-final2.stdout`); the box and the repo still disagree (box3_mismatch 1).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion (box 4).

## Extras

- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists `AGENTS.md`, `live_s228.html`, `nama.html`, `tf_bavelas.html`, `write` and `.ufo/reports/round-28/kaidoku.md`. None names tameshi round 28, so nothing was moved.
- Inherited state: no `lane-dead-no-report tameshi round=28` line exists; the lane was clean at base (`jj-lane.sh state`: tracked=0 untracked=0).
- Routed items 4, 5 and 6 were not done. Each edits a widely read input (README 54, QUALITY 31, runner 199 ledger entries) and would re-drift C1 (ScoutNextFrontier). Item 2: seat RegistryCheckAtR ran `tools/registry-check.py` from a fleet mirror and got `REGISTRY_CHECK: held=49/49 superseded=7`, exit 0, at both `b05d2ee` and base, with byte-identical stdout (`.ufo/waves/round-28/w1/RegistryCheckAtR.md`). That is a seat receipt, not an L1 re-run. Item 8 is cross-lane.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. Open L0 questions: none.
