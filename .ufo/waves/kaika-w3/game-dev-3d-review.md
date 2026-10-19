# kaika W3 — non-author verification: game-dev-3d round 108

Verifier: W3ReviewGameDev3d (fresh orchestrator-dispatched; not a lane seat). Subject: lane commits `09192f6` + `3f53896` on `kaika/round` (base `7c4e5897d`). Fleet report: `.ufo/reports/round-108/game-dev-3d.md` (fleet-ledger, uncommitted). All writes stayed in `/tmp/kaika-verify/game-dev-3d/` (removed at end); the lane worktree was read-only (`git status --short` empty before and after).

## 0. Recommendation

**ADMIT-with-findings.** Every counting command in the report reproduces exactly at both commits. The SOURCES census exits 0. Provenance, append-only, and credential checks are clean. Re-run replays of the boundary rows, the r95 harm check, and the unreal-mcp gate all match the report.

Not a clean admit: four items need fixing or relabelling before closure (F-1, F-2, F-3, F-4 in §7). One score movement (calibration 0→8) is not independently verified and should be recorded as provisional.

## 1. Provenance — PASS

`git log --format='%h %an <%ae> | %cn <%ce> | %s' 7c4e5897d..3f53896ff` → 2 commits (`09192f6`, `3f53896`). Both have author and committer `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`.

## 2. Append-only — PASS

- `git diff --stat 7c4e5897d..3f53896ff -- LOG.md corpus/lessons corpus/QUALITY.md …`: LOG.md `@@ -1498,3 +1498,47 @@` is a pure end-of-file append. `corpus/lessons/round-108.md`, `corpus/QUALITY.md`, `corpus/SOURCES.md` are new files.
- Deleted lines across all modified files: `git diff 7c4e5897d..3f53896ff -- LOG.md corpus/lessons corpus/QUALITY.md corpus/README.md PROVINCE.md SCORECARD.md SKILL.md | grep -E '^-' | grep -vc '^--- '` → `0`.
- `corpus/fixtures/run_battery.py`: 10 insertions, 0 deletions. Sha `f456bd00…` → `2a01b91f…`, which matches the SKILL stamp. Sha of `slope3d_boundary.gd` is `6f5af99d…`, matching the boundary-scan header.

## 3. Claims — per-claim verdicts

Command: `bash reports/round-108/measure.sh <commit>` at `7c4e5897d` and `3f53896ff` (read-only, committed blobs). Outputs are in `/tmp/kaika-verify/game-dev-3d/measure-{before,after}.txt`. Every number matches the report's table.

| claim | row | base → head (re-run) | report | verdict |
|---|---|---|---|---|
| C1 calibration | QUALITY criteria / mistake rows / captured by Q | 0/0/0 → 18/22/22 | same | **verified (counts)** |
| C1 | scored rows / saturation / verdict blocks / capability rows | 0/0/30/0 → 3/1/36/3 | same | verified (counts) |
| C1 | calibration score | 0 → 8 | 0 → 8 | **not verified as a movement** — see D-1 |
| C2 coverage (capability `source-registry`) | SOURCES rows | 0 → 35 | same | **verified** |
| C2 | README map+Frontier / surfaces / PROVINCE C/F/A | 0/0/0 → 2/27/3 | same | verified |
| C2 | coverage score | base 5 → 8 | 5 → 8 | base 5 verified (`git show 7c4e5897d:corpus/knowledge/engines.md \| grep -cE '^\| (Godot\|Unity\|Unreal Engine\|three\.js\|Blender)'` → 5); 8 anchor not exhaustively checked |
| C3 depth | CASES / slope3d / within-1° / SKILL row | 350/4/0/0 → 355/9/5/1 | same | **verified (counts)**; "within-1°" counts row-name prefix `slope3d_bound_`, not tilt values |
| C3 | boundary resolution | 30° vs 60° → 45.57° vs 45.58° | same | **verified** — base `slope3d_angle.gd` `SHALLOW_ANGLE := 30.0`, `STEEP_ANGLE := 60.0`; head re-run below |
| C3 | depth score | 8 → 8 | 8 → 8 "within anchor" | verified (no score move); verdict "improved" should read "verified, no score move" |
| expansion (trend) | knowledge entries with `source:` | 0 → 2 | same | verified |

**C3 behaviour, re-run in scratch** (`godot --headless --path <scratch> --script res://slope3d_boundary.gd -- --tilt T`, Godot `4.7.2.stable.arch_linux.ed1daf0bf`, default and Jolt projects):
- DEFAULT: 45.57 → `PASS … on_floor=true on_wall=false`; 45.58 → `NEGATIVE REJECTED … on_floor=false on_wall=true`.
- Jolt: identical flip.

**Harm checks:**
- Knowledge recheck, 5 rows: `totals: cases=5 pass=5 fail=0` (head scratch, `run_battery.py --only slope3d_bound_naive,…,slope3d_bound_out`).
- 7 slope rows at head: `totals: cases=7 pass=7 fail=0`.
- `r95_bullet_shm`, `r95_bullet_solver`: `FAIL exit=0 expected=0 reasons=['exact stdout marker missing']` at **both** head and base. The base commit's own runner fails identically, so this is host drift (lesson M5), not this round.
- Full 355-case run not re-run by me. The receipt `reports/round-108/battery/full-run.stdout.txt` reads `totals: cases=355 pass=353 fail=2 ordinary=294 negative_controls=61`.

**Capability rows re-run:**
- `unreal-mcp-gate` in scratch (`GATE_WORKDIR=… bash corpus/knowledge/unreal-mcp/gate/run_gate.sh`): `POINTERS=103 … UNRESOLVED=0`, `GATE RESULT: PASS (checks failed: 0)`.
- `source-registry`: `bash reports/round-108/census.sh` (see §4); `fixture-battery-targeted`: 7/7 above.

## 4. SOURCES — PASS

Validate: `bash …/sources-census.sh validate <lane>` → `game-dev-3d-shokunin	ok	…/corpus/SOURCES.md`, exit **0**.

Lane `census.sh` at head: `35` rows, `0` malformed, `A=32 B=2 C=1 `, `mined=5 queued=28 rejected=2 `, duplicate / enum / inflation / missing-path lines empty.

Re-opened rows (5 of 35; contract rule 1):

| row | tier | re-opened at | result |
|---|---|---|---|
| S011 | A (code) | `raw.githubusercontent.com/godotengine/godot/4.7-stable/scene/3d/physics/character_body_3d.cpp` | line 41 `#define FLOOR_ANGLE_THRESHOLD 0.01`; lines 546–547 `if (floor_angle <= floor_max_angle + FLOOR_ANGLE_THRESHOLD)`; 598–600 same predicate in wall reclassification. **Matches the Gate and the knowledge entry.** |
| S004 | A (docs) | RenderingServer class ref, `Headless mode` | "Most functions from RenderingServer will return dummy values in this case." — **verbatim** |
| S005 | A (docs) | command-line tutorial, `--headless` row | "Enable headless mode (`--display-driver headless --audio-driver Dummy`). Useful for servers and with `--script`." — **verbatim** |
| S034 | A (release notes) | `JoltPhysics/releases/tag/v5.6.0`, Bug Fixes | "Fixed an issue where a character could get stuck." — **verbatim**. Scope gap: the fix is upstream `CharacterVirtual`; the row does not show that Godot 4.7.2 ships Jolt 5.6.0 (D-7). |
| S030 | B, **rejected** | arXiv 2509.22170v1 §3.5 | "The overall false alarm rate of TITAN is 30%, which is relatively low in practice" — **verbatim**; rejection reasoning consistent with §3.5 "flagged cases can serve as potential issues". |

Not re-opened: S012 (its negative claim "the class reference omits the allowance" is unverified), S010.

## 5. Discernment spot-check (LEARNING.md) — ≥1 admit, ≥1 reject

| sample | decision | verdict | reason |
|---|---|---|---|
| `corpus/knowledge/godot-floor-angle-threshold.md` | admitted | **agree** | Source lines and the 5-row and 7-row recheck reproduce; default and Jolt flip reproduced at 45.57 / 45.58. Caveat: the Q6 "non-author replay" was by lane seat `W2RoundGameDev3d.R108PostReviewer` (D-3). The admission stands on my external replay; the lane's label does not. |
| `corpus/knowledge/godot-headless-not-render.md` | admitted | **agree** | S004/S005 quotes verbatim; both recheck greps behave as written (§6). |
| S030 (TITAN LLM-agent) | rejected row | **agree** | Quote verbatim; the 30% false-alarm framing plus "potential issue" status is a valid reason; flip condition is concrete. |
| rejected *knowledge* candidates | — | **no sample exists** | The round's `## Gate` logs no rejected knowledge candidates. LEARNING.md requires "candidates considered, admitted, rejected (with reasons)" (D-5). |

## 6. New knowledge entries — PASS with caveats

- Header trio (`source:` / `verified-at:` / `recheck:`) present in both files, lines 1–3.
- Floor entry recheck: `… run_battery.py --only slope3d_bound_naive,…,slope3d_bound_out` → `totals: cases=5 pass=5 fail=0` (re-run, §3).
- Headless entry recheck: `git grep -nE 'get_texture|get_image|RenderingServer|readPixels' <head> -- corpus/fixtures/` matches only `corpus/fixtures/r94vendor/three.module.js` (vendored library, outside the recheck glob `*.gd`/`three/*.mjs`), so the recheck prints nothing as claimed. `"--headless"` matches at `run_battery.py` lines 1007, 1088, 1114, 1278, as claimed.
- Camera API names (`unproject_position`, `is_position_in_frustum`, `is_position_behind`) present in `camera3d_{project,depth,ortho}.gd`.
- Not verified: the floor entry's negative claim about S012.

## 7. Defects by severity

- **F-1 (Major) — Q17 unapplied; fixture prose still stale.** `corpus/fixtures/README.md:5` still reads "235 registered cases (189 ordinary and 46 negative controls)"; the runner has 355 rows. The round appended a note at line 1072 instead of updating line 5. Post-reviewer FINDING 3 asked for the line-5 update, and it was not applied. QUALITY Q17 says "then update all affected documentation". This reproduces lesson M15's own class. Fix: update line 5 to the measured counts.
- **F-2 (Major) — Q16 self-violation.** `SCORECARD.md:394` contains a literal `… <r108 commit>` placeholder in the round-108 verdict block. Lesson line 84 claims "Q16 (no placeholder or future date in r108 records …) — pass". That claim is false as written. Separately, the correction note quotes the `<WORK>` token, so a naive `grep -c '<WORK>'` returns 3 (base 2). Fix: fill the hash or cite the fleet-report pointer without a placeholder token; reword the correction note.
- **F-3 (Major) — "non-author" label applied to lane-internal evidence.** LOG.md round-108 REVIEW bullet: "lane L2, non-author of the artifacts". Lesson Q6 and the floor entry both say "non-author replay" for `W2RoundGameDev3d.R108PostReviewer`. The protocol says otherwise: LEARNING.md: "A subagent the lane dispatched is still the lane." AXES.md: "a dispatched subagent does not count." Prompt §6.6: "Your reviewer and critic L2s are still the lane." Fix: relabel as lane replay. Record this review as the first non-lane replay (5-row and 7-row sets reproduced above).
- **F-4 (Major) — calibration score movement is tautological.** Base calibration is 0 by the rubric's own definition: "0: no scored rubric or admission bar" (SCORECARD round-108 block). The rubric was written in the same round and the lane says so ("provisional retrospective baseline"). Lane selection of calibration as "lowest axis" was made post hoc because base mint rows read `unscored`. Recommend: record calibration 0→8 as provisional, not as a verified improvement. The lane has already routed a freeze-and-test (LOG ROUTED bullet).
- **D-5 (Medium) — LEARNING Gate ledger incomplete.** `corpus/lessons/round-108.md ## Gate` has admission pass lists and row-level rejections, but no knowledge candidates-considered/rejected section and no spot-check slot. Fix: add a "Knowledge candidates" block (even if zero rejected, say so).
- **D-6 (Medium) — quality trend overstated.** Report says "Quality: improved", with evidence from new fixture rows and capabilities. LEARNING's quality trend counts entries re-verified, deepened, or superseded. No existing knowledge entry was changed or superseded; the only re-verification is the unreal-mcp gate, which passed unchanged. Recommend "unchanged".
- **D-7 (Low) — S034 teaches over-reaches.** The Jolt fix is upstream; the row does not show Godot 4.7.2's bundled Jolt version.
- **D-8 (Low) — "ONE batched" swarm not literal.** Report describes an 11-seat first batch, retries, and a later post-landing batch (disclosed). Seat outputs in `reports/round-108/seats/` carry no `/skill:godspeed` lead, so that requirement is unverifiable from the repo.
- **D-9 (Low) — SHONEN statuses.** Report lists box 2 as `[~]`; `SHONEN.md` (unchanged by the round) has `[x]` there. Report's `[~]` for the other three boxes is consistent with the file's `[ ]`.
- **D-10 (Low) — Frontier labelling contradictory.** `PROVINCE.md ## Frontier` bullet says "moved to core in r108 … still frontier". `corpus/README.md` Frontier item 4 is also "moved to core" yet still listed. The report acknowledges keeping it as a record.
- **D-11 (Low) — "within-1°" metric.** It counts row-name prefix `slope3d_bound_`, not tilt values. The tilt values are correct in `run_battery.py` (verified by diff), but the counting command does not check them.
- **D-12 (Low) — saturation line.** Line 8 equals all three new scores, so every owned axis is at saturation on declaration. The "lowest-axis" rule becomes vacuous next round. Q2/Q3 cite M14 (absence of the bar) as their lesson, which is weak grounding for header and tier criteria.

## 8. Trend verdicts (recommended)

- **Expansion: improved (verified).** 2 admitted entries cite `mined` rows (`S004,S005` and `S011,S012,S035`); the floor-angle ground was frontier at base (`git show 7c4e5897d:SCORECARD.md` line 18: "no … floor-angle boundary sweep").
- **Quality: unchanged** (recommend downgrade from "improved"; see D-6).
- **Discernment: improved, provisional.** My spot-check agrees on 2 admits and 1 reject; caveats D-3, D-5, F-2.

## 9. Per-axis recommended verdicts

- **depth 8 → 8:** score unchanged. C3 verified as a mechanism add with boundary re-derived. Record "verified, no score move".
- **coverage 5 → 8:** verified against the rubric; base 5 measured. 8 anchor ("every PROVINCE surface placed") not exhaustively enumerated by me.
- **calibration 0 → 8:** counts verified; **score movement not verified** (F-4). Provisional.

## 10. Verification gaps

- Full 355-case battery not re-run (receipt cited only).
- S012 negative claim and S010 not re-opened.
- PROVINCE surfaces not enumerated one-by-one against the coverage map.
- Seat-prompt godspeed lead not verifiable from the repo.
- Tower dispatch log not inspected (batch count taken from the report text).

## 11. Commands run (summary)

- `git log` / `git diff --stat` / `git diff … | grep -E '^-'` (append-only, provenance).
- `bash reports/round-108/measure.sh {7c4e5897d,3f53896ff}`.
- `bash …/sources-census.sh validate <lane>` (exit 0); `bash reports/round-108/census.sh`.
- `python3 corpus/fixtures/run_battery.py --only …` in `/tmp/kaika-verify/game-dev-3d/{head,base}` (archived trees) with Node v24.21.0 on PATH.
- `godot --headless --path <scratch> --script res://slope3d_boundary.gd -- --tilt {45.57,45.58}` (default and Jolt).
- `GATE_WORKDIR=<scratch> bash corpus/knowledge/unreal-mcp/gate/run_gate.sh` (scratch).
- Credential sweep: `git diff 7c4e5897d..3f53896ff | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1).
- Web re-opens: S011 (raw source), S004, S005, S034, S030 (see §4).

## 12. Credentials — PASS

The sweep in §11 printed nothing.

## 13. Report conformance — PASS with notes

Required sections present in order: Work performed, Landed changes, Before→after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. No `[x]` box. Round commit cited (`3f53896`, `09192f6`). Non-author label issue: see F-3.
