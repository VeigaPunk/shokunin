# game-dev-3d — round 108 (kaika W2a)

Lane worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/game-dev-3d-shokunin`, branch `kaika/round`, base `7c4e589`.
**Lane commits:** `09192f6` (round work) + `3f53896` (one-line SCORECARD count fold). Measurements below are taken at `3f53896`.
Steered round 108 (r107 aborted at `7c4e589`). Collision check: neither `.ufo/reports/round-108/game-dev-3d.md` (fleet root or ledger) nor a LOG round-108 entry existed at start.
**No push.** The standing operator rule "No push" overrides MISSION.md's commit-then-push, so the lane commits stay local. This report is uncommitted; the integrator commits it.

## Work performed

Declared claims (three, one per owned axis, each with its own counting command):

- **C1 — calibration (lowest axis; no axis was scored at base, and calibration had no measurement infrastructure):** an admission bar, mistakes mined from the lane's own history, and a scored self-assessment.
- **C2 — coverage (capability acquisition `source-registry`):** a contract-v1 source registry, a coverage map with Frontier, and PROVINCE Core/Frontier/Adjacent sections.
- **C3 — depth:** Godot 4.7.2 `CharacterBody3D` floor/wall boundary at `floor_max_angle = 45°`, measured with adjacent samples.

Work items:

- **QUALITY bar.** `corpus/QUALITY.md` has 18 criteria (Q1–Q18). Each cites its lesson and has a check. The bar points to `corpus/SOURCES.md` for tiers and to chousa for method; it does not copy either.
- **Mistakes lesson.** `corpus/lessons/round-108.md` `## Mistakes` lists 22 classes (M1–M22), each with an evidence pointer, a capturing Q and a fix. Seven classes are new relative to the W1 STATE dossier, among them `<WORK>` placeholders, report-last work hashes that are not ancestors of HEAD, future-dated blocks, and the r98 seed clobber.
- **SCORECARD.** Appended a 0/5/8/10 rubric (marked provisional and frozen from r108) and scores. Declared a saturation line of 8 with N=3. Added three capability rows, each demonstrated this round. Added retroactive blocks for r90 (REJECT), r91 (unverified), r92 (ADMIT-corr), r99 and r100, plus correction notes. Pointer: `SCORECARD.md` `## Axes — scored (r108)` through `## Round 108 verdict`.
- **Registry.** `corpus/SOURCES.md` has 35 rows, all opened on 2026-10-19 (contract rule 1). Two are rejected with a flip condition (S010 Vulkan CI determinism, S030 LLM-agent diagnosis). There are four `## Paths` sequences plus a search log and leads. Quotes are in `corpus/lessons/round-108.md` `## Gate`.
- **Coverage map.** `corpus/README.md` gained `## Coverage map` (27 surfaces) and `## Frontier` (8 ordered moves). `PROVINCE.md` gained `## Core/Frontier/Adjacent` and a dated note correcting the dead `.shokunin/` scope. Both changes only add lines; `git diff 7c4e589 -- PROVINCE.md` has no deleted lines.
- **Boundary fixture.** New seed `corpus/fixtures/slope3d_boundary.gd` (sha `6f5af99d…`) and five CASES rows, `slope3d_bound_{naive,in,edge_in,edge_out,out}` at 45.1, 45.5, 45.57, 45.58 and 45.65°. `run_battery.py` sha went `f456bd00…` → `2a01b91f…`; it has 10 added lines and none changed. Boundary scan, GodotPhysics3D and Jolt: floor at ≤45.57°, wall at ≥45.58°. The source predicts 45.573° (`FLOOR_ANGLE_THRESHOLD 0.01`, Godot `4.7-stable` `character_body_3d.cpp:41,546,598`). Receipt: `reports/round-108/battery/boundary-scan.txt`.
- **Knowledge entries.** Two entries were admitted through the bar: `corpus/knowledge/godot-floor-angle-threshold.md` and `corpus/knowledge/godot-headless-not-render.md`. This is expansion work, not a claim. The pass lists are in `corpus/lessons/round-108.md` `## Gate`.
- **SKILL.md.** Added a one-line pointer to SOURCES/QUALITY, one error-pattern row (`nominal-threshold read`) and a §6 stamp note for the new runner hash.
- **L2 swarm.** One batch of 11 seats: planner, connector, scout, scribe, 5 executors, reviewer and critic. This was the first `task` batch, retried until job slots freed. Provider exhaustion (named): 4 of 5 executors died on a rate limit and the 5th stalled and was stopped. All 5 fresh re-dispatches died at provider capacity. A third dispatch of the 4 non-fixture executors landed, and the L1 wrote and ran the fixture seat itself. A post-landing batch added a reviewer, a critic and a mutation tester. All seat outputs are in `reports/round-108/seats/`.
- **Seat findings.**
  - Non-author replay of the 7 slope rows: 7/7 with `seats/post-reviewer.md` and `reports/round-108/battery/replay-nonauthor-20261019T222103636356Z.verdicts.json`.
  - Mutation: 5/5 mutants killed (`seats/mutation.md`).
  - The pre-critic's separability attack and the post-critic's six findings were folded: cannon-es and pybullet added to the map, two `teaches` cells narrowed, scores labelled provisional, C1's own capability named, and a fixtures README count note added.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `corpus/QUALITY.md`, `corpus/lessons/round-108.md` (Mistakes, Gate), SCORECARD rubric, scores, saturation, capabilities, retro blocks | `LOG.md` "ROUND 108" bullet (C1) | `09192f6`, count fold `3f53896` |
| `corpus/SOURCES.md`, `corpus/README.md` map and Frontier, `PROVINCE.md` sections and correction note | `LOG.md` "ROUND 108" bullet (C2) | `09192f6` |
| `corpus/fixtures/slope3d_boundary.gd`, `run_battery.py` +5 rows, `reports/round-108/battery/**`, SKILL row and stamp | `LOG.md` "ROUND 108" + "RE-VERIFICATION" bullets (C3) | `09192f6` |
| two knowledge entries, `corpus/fixtures/README.md` count note | `LOG.md` "ROUND 108", "REVIEW" bullets | `09192f6` |

## Before → after measurements

Counting command: `bash reports/round-108/measure.sh <commit>`, run from the lane root. It reads committed blobs only, so before is `7c4e589` and after is `3f53896`.

| claim | measure | `7c4e589` | `3f53896` |
|---|---|---|---|
| C1 | QUALITY criteria rows / mistake rows / mistakes captured by a Q | 0 / 0 / 0 | 18 / 22 / 22 |
| C1 | scored axis rows / `Saturation line:` / verdict blocks / capability rows | 0 / 0 / 30 / 0 | 3 / 1 / 36 / 3 |
| C1 | calibration score (provisional rubric) | 0 | 8 |
| C2 | SOURCES rows (contract census `bash reports/round-108/census.sh`) | 0 (file absent) | 35; malformed 0; A=32 B=2 C=1; mined 5 queued 28 rejected 2; dup/enum/inflation/missing-path: none |
| C2 | README map+Frontier headings / map surfaces / PROVINCE C/F/A headings | 0 / 0 / 0 | 2 / 27 / 3 |
| C2 | coverage score | 5 | 8 |
| C3 | CASES rows / slope3d rows / rows within 1° of the 45° limit / SKILL threshold row | 350 / 4 / 0 / 0 | 355 / 9 / 5 / 1 |
| C3 | boundary resolution | 30° vs 60° | 45.57° vs 45.58° (both backends) |
| C3 | depth score | 8 | 8 (within anchor) |

Battery state (C3 harm check, commit `09192f6` bytes):
- Full pinned run: `cases=355 pass=353 fail=2`, `seeds_unchanged=true` (`reports/round-108/battery/full-run-20261019T220450573107Z.verdicts.json`). All 5 new rows pass.
- The two failures are `r95_bullet_shm` and `r95_bullet_solver`. The pybullet child's `#`-line count `d` is higher (16 vs 8, 52 vs 44, 5 vs 4). The **base commit's own runner and seeds** fail identically (`base-7c4e589-r95-rows.verdicts.json`), so this is host drift of class M5, not this round.
- Prior CASES definitions: 350/350 unchanged against the r105 receipt (`compare_prior.py`).
- Gate: `GATE RESULT: PASS (checks failed: 0)`, `POINTERS=103 UNRESOLVED=0`.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources. New this round: `SKILL.md` §2 row `nominal-threshold read`, `corpus/QUALITY.md`, `corpus/SOURCES.md`. Pending non-author verification.
- [~] End-to-end domain task executed and logged. `SHONEN.md` already carries `[x]` from r2 (`corpus/lessons/r2-independent-review.md`); this round adds `reports/round-108/battery/README.md` plus the L2 replay. This report does not mark `[x]`.
- [~] Instructions executable without oral context. `reports/round-108/measure.sh`, `census.sh`, `battery/README.md` commands; each knowledge entry's `recheck:` line.
- [~] No cross-domain bleed; PROVINCE remains accurate. `PROVINCE.md` `## Adjacent` (game-dev-2d, mado, kumitate, kengaku, revenger) and the dead-root correction note.

## Sources & frontier

- **Registry size.** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 0 at `7c4e589` → 35 at `3f53896`. Rows added by tier: A=32 (incl. 1 own-work), B=2 (arXiv preprints S028, S030), C=1 (S010, rejected).
- **Status changes.** All rows are new; the old→new log is in `corpus/lessons/round-108.md` `## Gate`. Five rows are `mined`: S004 and S005 by the headless entry; S011, S012 and S035 by the floor-angle entry.
- **Frontier advanced.** The floor-angle boundary moved from frontier (`SCORECARD.md:18`, "no … floor-angle boundary sweep") to core (`corpus/README.md` Frontier item 4; `PROVINCE.md` `## Frontier`). The render-capture frontier now has an admitted entry stating its boundary. Seven frontier moves remain ordered with first probes.
- **Shared ground with game-dev-2d.** The Godot CLI and GdUnit4 pages appear in both registries (their S006 and S020). The overlap is noted, not absorbed.

## Mistakes

- **Classes mined.** 22 (M1–M22) in `corpus/lessons/round-108.md`: 15 from the STATE dossier, with pointers re-verified and corrected (M4 → `SCORECARD.md:231`; M3 now also cites `r92-adjudicator.md:21,29`), and 7 new (M16–M22).
- **Criteria added.** 18 (Q1–Q18). Every class maps to a criterion. M5 got a second sighting this round as stable host drift.
- **Applied in-round.** Q16: own records carry no placeholders; this commit hash lives here, not in a self-referencing file. Q17: a fixtures README count note was added. Q6: the floor entry was admitted only after the non-author replay. Q13: one fixture writer during the battery.

## Trend verdicts

- **Expansion: improved.**
  - Before → after: 0 → 2 admitted `corpus/knowledge/` entries whose `source:` cites `mined` rows, on ground the coverage map marks as uncovered or frontier.
  - Count: `for p in corpus/knowledge/*.md; do head -1 $p | grep -q '^source:' && echo $p; done | wc -l` → 2.
  - The coverage map now places 27 surfaces.
- **Quality: improved.**
  - Five new discriminating rows: mutation 5/5 killed, non-author replay 7/7.
  - Three capabilities were demonstrated, and the gate passed.
  - Bound: the full battery is red on 2 pre-existing host-drift rows, reproduced at base.
- **Discernment: improved, but self-assessed.**
  - New this round: the admission bar, 22 mistakes all captured by criteria, and retroactive REJECT/unverified records.
  - The scores use a rubric written in the same round, are labelled provisional, and await the orchestrator's non-author check.

## L0 questions

- game-dev-3d | round-108 | The pybullet `r95_bullet_shm` and `r95_bullet_solver` rows now fail on this host, including on the base commit's own runner. The cause is the child `#`-diagnostic count `d` (16 vs pinned 8). Should the lane drop `d` from those markers or give it an envelope? The change touches pinned fixture code, so it needs a ruling.
- game-dev-3d | round-108 | Should the battery gain a second seed project (`physics/3d/physics_engine="Jolt Physics"`) so backend-differential rows such as the floor-angle bracket can run under Jolt? Today they are scratch-only.

## Integrator notes

- **Fleet ledger drift (STATE D12).** `MANIFEST.json` lists lane rounds [70–73]; `.ufo/state/game-dev-3d.round` = 1; the lane is at 108.
- **Mint date conflict (D17).** `MANIFEST.json` mint date 2026-10-11 vs `corpus/README.md` 2026-10-13.
- **W1 dossier corrections (pre-reviewer, `reports/round-108/seats/pre-reviewer.md`):**
  - D8: depth's last change is r70, not r71.
  - D13: there are 2 live dead-root SCORECARD lines, not 3.
  - D15: `reports/round-107/` is absent from the worktree.
  - The W1 plan predicted 45.1° = wall; the measurement shows floor.
- **Fleet probe `critic.md` census line.** The connector reports `NF!=11` there, while the frozen contract says NF=13. The contract's command was used and is correct for an 11-column table with edge pipes.
- **Harness.** `cd` is broken in this harness's shells. All lane commands used the tool `cwd` or absolute paths; no lane write landed outside the worktree. One edit tool call resolved a bare `LOG.md` to the fleet root and was rejected before writing (`git -C /home/vgpnk/Projects/shokunin status --short LOG.md` printed nothing).
- **Provider exhaustion.** The executor route was rate-limited and then at capacity, as described under Work performed.

## Post-review fixes

The orchestrator's adjudication was ADMIT-with-findings. All fixes below are append-only. They land in lane commit **`cab506b`** ("round-108: post-review fixes"), on top of `3f53896`. Files changed: `SCORECARD.md`, `corpus/SOURCES.md`, `corpus/lessons/round-108.md`, `corpus/knowledge/godot-floor-angle-threshold.md`, `corpus/fixtures/README.md` and the new `reports/round-108/measure-strict.sh`. No line was deleted (`git diff 3f53896 cab506b | grep -c '^-[^-]'` → 0). No new claims.

1. **Q17 (fixtures README count).** Line 5 still says 235 (append-only). The `## Count note (r108)` added in `09192f6` and a post-review note added in `cab506b` correct it to 355 registered cases: 294 ordinary and 61 negative controls.
2. **Q16 (`SCORECARD.md:394` `<r108 commit>`).** Filled by the appended `## Post-review corrections`: work `09192f6`, measured at `3f53896`. The `<commit>` tokens in the scored rows are the `measure.sh` usage parameter. The lesson's earlier Q16 pass is superseded by a pass recorded after the fix.
3. **Calibration 0→8 is provisional.** The rubric and the scores were written in the same round, and the base 0 is the rubric's own definition. The move records that the artifacts now exist, not independent calibration (SCORECARD post-review note).
4. **Quality trend.** Revised from "improved" to **unchanged**. The two pybullet rows are red, and the new rows and gate pass do not raise overall quality above base. The earlier `## Trend verdicts` line is superseded.
5. **W3 critic (`kaika-w3-game-dev-3d-critic.md`).** The critic marked no item "blocking". All four fixable defects were fixed:
   - **Fail-closed measuring.** Added `reports/round-108/measure-strict.sh`. A bad ref exits 2. A blob missing at a ref also exits 2 unless explicitly allowed. At `3f53896` it exits 0.
   - **C1-only evidence separated.** The verdict-block count 30→36 is retroactive record-keeping. The capability count 0→3 includes C2's and C3's rows.
   - **Capability round fixed.** `unreal-mcp-gate` first worked in r102; r108 is the round that recorded it.
   - **C2 measured without C3 evidence.** S035, S036 and the floor-angle frontier→core move are assigned to C3. C2 alone is 34 registry rows, 27 surfaces and 3 PROVINCE headings.
   - **C3 wording and source pin.** 45.573° is labelled as derived from source; the run measures the 45.57°/45.58° bracket. New row **S036** supersedes S011 and pins `character_body_3d.cpp` to commit `ed1daf0bf001b61586d9930840f2f1394092c079` of the installed 4.7.2 binary. That file is byte-identical to the 4.7-stable copy (sha256 `97f7a626…`), with lines 41/546/598 re-read. The threshold-0 mutant is no longer counted as a classification falsifier.
   - **Remaining debts:**
     - The C2/C3 overlap remains in the registry (S035, S036 rows exist). This is a separability debt, not a removal.
     - `measure.sh` is kept as written; the strict wrapper is the supported entry point.
     - The rubric needs a non-author application in r109+ before the scores are calibrated.
6. **Registry census after the fixes.**
   - Fleet tool: `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/game-dev-3d-shokunin` → `game-dev-3d-shokunin ok …`, **exit 0**.
   - Contract census (`bash reports/round-108/census.sh`): 36 rows, 0 malformed, A=33 B=2 C=1, mined 6, queued 28, rejected 2. Duplicate, enum and missing-path checks print nothing.
   - S036 is logged old→new in `corpus/lessons/round-108.md` `## Post-review corrections`.
