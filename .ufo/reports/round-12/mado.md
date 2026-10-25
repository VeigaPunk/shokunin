# mado — round 12 (kaika)

Lane: mado-shokunin (desktop & compositor craft). Steered round 12 (`.ufo/waves/kaika/steer.md`).
Lane worktree `.tower/worktrees/kaika/mado-shokunin`, branch `kaika/round`, base `e1d81d4`.
Commits on the lane branch, in order:
- `a6528e6` — pre-registration
- `5174e15` — content
- `6e3b75f` — post-integration fixes (**the measured commit**)
- `b7ca008`, `4e92a87` — scorecard
- `a6df2f5`, `bed2b90` — lesson
- `aeb33b5` — LOG post-integration entry, recovered from a fleet-root misplacement (see Integrator notes)

Lane HEAD is `aeb33b5`. Nothing was pushed (see Landed changes).

## Work performed

The round declared three claims. Each sits on a different axis and each can be checked without the other two:
- **C1 — calibration.** QUALITY criteria grounded in lessons. Calibration was one of two lowest axes, tied with coverage at 0.0000.
- **C2 — freshness.** An append-only re-anchor of the gkeep drift from 2026-10-17.
- **C3 — coverage, as a capability acquisition: "sources registry".** Creates `corpus/SOURCES.md` and admits entries on uncovered ground U1–U3.

There was no exploratory claim.

- **Pre-registration first.** Claims, six-axis baselines, U1–U7 and saturation (line 9.0, window N=3) were committed before any work in `a6528e6` (`SCORECARD.md` § "Round 12 (kaika) — pre-registered…"). Baselines are in `.ufo/evidence/round-12/before*.txt`. The reviewer seat re-derived every baseline from committed bytes (`git archive a6528e6`) and found no mismatch (`.ufo/evidence/round-12/l2-reviewer.md` §1).
- **L2 swarm.** One batched call of 12 seats: planner, connector, scout, scribe, six executors, reviewer and critic. Every prompt began with `/skill:godspeed` followed by the verbatim `directive.md` bytes. No model was passed; the route table assigned them. Two earlier identical batched calls were refused whole with `Background job limit reached (100)`, so no seat started from those. A second batched call (post-integration reviewer and critic) reviewed `5174e15`. Seat outputs: `.ufo/evidence/round-12/l2-*.md`.
- **C1.**
  - `corpus/lessons/round-12.md` `## Mistakes` covers M1–M14, re-measured at `a6528e6`:
    - `a5171`: 52 occurrences in 17 files;
    - `/tmp` pointers: 79 paths in 51 directories, 0 existing;
    - `getprop` appears at line 51 of `hyprctl --help`.
  - It also covers the external inference traps M01–M07, `## Gate` (39 row records), and `## Mistakes made in this round` R12-a to R12-d with a correction.
  - `corpus/QUALITY.md` gains criteria 6–16. Each cites its lesson on the same line (lesson file, the QUALITY diff in `5174e15`), and provenance notes were appended in `6e3b75f`.
- **C2.**
  - The gate's only red row was a true alarm: `hypr.root.include_graph` read 18 source lines against 17 expected (`before-no-live.txt`).
  - Provenance: `~/Projects/gkeep/install.sh:21-36`. The backup `hyprland.conf.bak.1792267376` equals the old pin `4f52854a…` (2026-10-17T20:02:56Z).
  - Recorded in `corpus/knowledge/config-drift-r12.md`, plus `SKILL.md` errata (a pointer after the `:40-46` paragraph and an EOF section).
  - The gate erratum sits above `declare -a EXPECT`. EXPECT gains `~/.config/hypr/gkeep.conf`; the selftest fixture gains the same include.
  - Selftest scenario B now removes `gkeep.conf` and asserts `sources_resolve` FAIL. A mutant flipping the FAIL arm to PASS survived behaviourally at `5174e15` and is killed at `6e3b75f` (`gate-mutant-sources-resolve.txt`). A mutant dropping the gkeep EXPECT line is also killed (`gate-mutant-gkeep.txt`).
  - Third re-cut killed 10/10 (`gate-recut-3.txt`). `PIN_MADO` moved to `538d178b…`; `TABLE_MADO` is unchanged.
  - The harness was pinned explicitly: `MADO_VERIFY_HARNESS=/home/vgpnk/Projects/shokunin/tameshi-shokunin/tools/mutate-and-run.sh`, sha `75ed934d…`. The default path would have resolved into the sibling kaika tameshi worktree.
  - An intermediate `LOCAL+=(gkeep)` widening was dropped before commit. It had no behavioural covering mutant, and `sources_resolve` already checks the file (LOG round-12 entry, C2).
- **C3.**
  - `corpus/SOURCES.md` follows contract v1. Its 39 rows were merged from five seat fragments and renumbered S001–S039. It also has `## Paths` (6), `## Search log` and `## Leads`.
  - Three entries were admitted:
    - U1 `corpus/knowledge/window-rule-effects-getprop.md`: `hyprctl getprop` is an *effect* read with no rule attribution. Measured with `class:Alacritty` → opacity 0.97 / 0.9 (`getprop-measure.txt`). It corrects `arc-synthesis.md:300` without editing that note.
    - U2 `hyprland-config-era-r12.md`: 0.53 rule-syntax break; 0.55 Lua plus a hyprlang window of "1 - 2 releases" (S024). The host reports `configProvider: hyprlang`.
    - U3 `xdg-portal-routing-r12.md`: `hyprland-portals.conf` is `default=hyprland;gtk`; ScreenCast v6, read via properties only.
  - Integrator changes at merge:
    - S014's text was updated after the dropped widening;
    - S020's kind changed from own-work to code;
    - S002 was joined into U1's `source:`.
- **Elegance.** `SKILL.md` gains three durable error-pattern rows (MADO-R12-1/2/3) and one pointer line to `corpus/SOURCES.md` (`SKILL.md:20`, `:353-355`). `corpus/README.md` gains four coverage-map rows and a Frontier bullet.
- **Review dispositions.** All recorded in the LOG round-12 entry ("Reviewer/critic dispositions", "Post-integration review"):
  - Accepted: C3 is counted by a join; C1 is counted only where the citation resolves; README rows were added; the LOCAL widening was dropped; the harness is pinned; the tie is stated; freshness candidate (a) is recorded; the gkeep-removal case was added; `after-measure.sh` prints every command.
  - Kept open: operator intent (L0); depth and adjacency rubrics; the SKILL EOF errata block (needed so corrections sweep every mention, `PROTOCOL.md` §Evidence).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Pre-registered claims, rubrics, baselines, saturation | "2026-10-19 — round 12 (kaika)" § Pre-registration | `a6528e6` |
| `corpus/lessons/round-12.md`; `corpus/QUALITY.md` criteria 6–16 | same entry, § C1 | `5174e15` |
| `config-drift-r12.md`; `SKILL.md` errata; `tools/mado-verify.sh` EXPECT, fixture, erratum, re-cut | § C2 | `5174e15` |
| `corpus/SOURCES.md`; U1–U3 entries; README rows; SKILL rows and pointer | § C3 | `5174e15` |
| Gate scenario-B removal case + third re-cut; QUALITY provenance notes; lesson and drift errata | § Post-integration review | `6e3b75f` |
| SCORECARD results, capabilities, planned round 13; formatting fix | § Post-integration review (measurement) | `b7ca008`, `4e92a87` |
| Lesson: mistakes made this round + correction | § Post-integration review | `a6df2f5`, `bed2b90` |
| LOG post-integration paragraph (recovered verbatim after fleet-root misplacement) + misplacement note | § Post-integration review | `aeb33b5` |

**No push.** The standing operator rule "No push" (kaika binding §6.6) takes precedence over MISSION.md's commit-then-push rule (`MISSION.md:79`). Operator-gated artifacts are committed, not pushed. This report is left uncommitted in the ledger worktree for the integrator, per §6.1.

## Before → after measurements

Before = `e1d81d4` (`.ufo/evidence/round-12/before.txt`). After = `6e3b75f`, from `REV=6e3b75f bash .ufo/evidence/round-12/after-measure.sh`; the output in `.ufo/evidence/round-12/after.txt` prints every command next to its result.

**C1 — calibration.**
- Command: `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md` over `grep -cE '^[0-9]+\. ' corpus/QUALITY.md`, plus the resolver loop in `after.txt`.
- Before: 0/5 → 0.0000.
- After: 11/16 → **6.8750**. All 11 resolve.
- Strict reading (lane incidents only; criteria 15–16 rest on external traps): `grep -E '^[0-9]+\. .*lessons/round-12.md#mistakes' corpus/QUALITY.md | wc -l` → 9/16 → 5.6250.

**C2 — freshness.**
- Command: `bash tools/mado-verify.sh --no-live | awk '$3=="FAIL"||$3=="UNKNOWN"' | wc -l`.
- Before: 1 (pass 28/29 → 9.6552).
- After: **0** (pass 29/29 → 10.0000).
- Claim-level check: present-tense SKILL contradictions without an erratum went 1 → 0. `grep -c '^> Erratum (round 12' SKILL.md` → 1 and `grep -c '^## Errata (round 12)' SKILL.md` → 1.

**C3 — coverage.**
- Command: the join loop in `after.txt` § C3, i.e. head-15 `source:` S-ids × a `mined` row naming the file × distinct `covers:` values.
- Before: 0/7.
- After: **3/7 = 4.2857** (U1, U2, U3).
- The capability's census is clean (see Sources & frontier).

**Harm watch at `6e3b75f`:**

| Check | Before | After |
|---|---|---|
| Navigation counter (literal fence, sha `8b59b503…`, `REV=6e3b75f`) | 22/22 | **26/26, exit 0** |
| `--selftest` | 268/268 | 269/269 |
| Live gate | 51 pass / 1 fail | 52 pass / 0 fail / 8 notes, CLEAN |
| `--regression` | PASS at `dc7c4141…` | PASS at `538d178b…` |
| Gate sha | `93e43f8f…` | `ea798ad0…` |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:353-355` (round-12 rows) + `corpus/SOURCES.md`; lane-asserted, no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG round-12 entry § C2 (drift detected → re-verified → re-anchored → gate CLEAN, `gate-*-after.txt`); lane-asserted.
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-12/after-measure.sh` re-runs every claim count; lane-asserted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `config-drift-r12.md` § Disposition (gkeep reported, not absorbed); `.ufo/evidence/round-12/l2-connector.md`; lane-asserted.

## Sources & frontier

**SOURCES rows:** 0 → **39**.
- Commands: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `6e3b75f`. Before, the file was absent (`test -e corpus/SOURCES.md` → 1).
- By tier: A=35, B=1, C=3 (tier awk).
- By status: mined=28, queued=9, rejected=2.

**Census at `6e3b75f`:** malformed 0; duplicate ids none; enum and tier-inflation none; mined `used-by` paths missing: none. The join check passes in both directions.

**Rejected rows:**
- S011: fleet MANIFEST verdicts used as mado axis history (45 improved keys, 28 manifest-only). Flip condition: verdicts bound to the round's claims.
- S012: a third-party Hyprland blog with no version anchor. Flip condition: a version-pinned rewrite.

**Rows touched old→new:** none. The registry is new this round.

**Frontier advanced:**
- U1, U2 and U3 moved from frontier to sourced ground (`corpus/README.md` Frontier bullet).
- U4 and U6 have queued study paths (S005–S010). Neither `wayland-info` nor `libinput` is installed (`l2-scout.md`).
- Still open: rule *attribution*, U4–U7 and Waybar module text.

## Mistakes

**Classes mined:** 14 lane classes (M1–M14) and 7 external inference traps (M01–M07).

**Criteria added:** 11 QUALITY criteria (6–16):
- 9 grounded in lane incidents (M1, M2, M3, M6, M7, M8, M9, M11, M13);
- 2 grounded in the external traps.

**Not turned into QUALITY criteria:**
- M5 stays a gate-maintenance rule.
- M4 and M10 stay process rules.
- M12 and M14 are fleet-level and routed below.

**Mistakes made and caught this round (R12-a to R12-d in the lesson):**
- R12-a: an uncovered gate widening, dropped.
- R12-b: the wrong re-anchor protocol was cited. Corrected in the lesson; the gate citation is round-13 work.
- R12-c: `after.txt` printed commands that differed from the ones run. Replaced by a script that prints each command.
- R12-d: trap-grounded criteria were filed under the incidents heading. A provenance note was added and the score is reported both ways.

## Trend verdicts

- **Expansion: improved.**
  - Three `knowledge/` entries on pre-registered uncovered ground (U1–U3), each opening with `source:` that cites `mined` rows (join check in `after.txt`).
  - The coverage map went from 22 to 26 notes.
- **Quality: improved.**
  - The gate went from DIVERGED to CLEAN on both planes.
  - The present-tense SKILL contradiction now carries an erratum.
  - Triple-header entries went from 3/22 to 7/26 (observational).
  - The selftest gained a behavioural assertion: red-before / green-after mutant, `gate-mutant-sources-resolve.txt`.
- **Discernment: unprovable-but-better, pending outside review.**
  - Rejected rows, `## Rejected` sections in all four entries, lesson-grounded criteria, and in-round self-caught mistakes.
  - The required non-author admit/reject spot-check is the orchestrator's after landing. Suggested sample:
    - admit: S018 (tagged `HyprCtl.cpp`) or U1;
    - reject: S012, or the dropped `LOCAL` widening.

## L0 questions

- mado | round-12 | Is `~/Projects/gkeep` a kept part of this desktop? The gate's EXPECT now requires `source = ~/.config/hypr/gkeep.conf` (C2 re-anchor, inferred from the operator-run installer and gkeep commits after the install). If gkeep is temporary, mado reverts EXPECT by an appended erratum, and C2's freshness credit becomes "re-anchor owed".
- mado | round-12 | Ratify fleet round 1 (2026-10-15, LIVE-blocked, +0) as *superseded, unadmitted* by round 12 (LOG round-12 entry). This supersedes the still-open `.ufo/l0-questions.md:37` namespace question for mado.

## Integrator notes

- **MANIFEST closure (M14).** Record all six axes with claimed axes only:
  - calibration improved;
  - freshness improved (conditional on L0 #1);
  - coverage improved, plus the capability "sources registry";
  - operability unchanged;
  - depth and adjacency **unscored** (no bounded rubric in `SCORECARD.md`; record them as `unscored`, not `unchanged`).

  Past mado entries carry 28 of 45 "improved" verdicts with no claim behind them (S011; `l2-scribe.md`).
- **Outside spot-check pending.** Calibration and discernment credit wait on a non-author spot-check (≥1 admit, ≥1 reject, ≥3 SOURCES rows re-opened, all counting commands re-run via `after-measure.sh`). SHONEN stays `[~]`.
- **Dispatch capacity.** The session job cap of 100 refused two whole batched dispatches before the third ran. This is a dispatch-capacity incident, not a lane defect.
- **Provider exhaustion.** The orchestrator flagged an executor-route rate limit (m_swe, ~22:01Z). No mado seat died; all 14 seats completed.
- **`cd` / relative-path hazard — one out-of-scope write by this lane.** The L1 (not an L2) ran one shell append with no `cwd`. It wrote the 23-line round-12 "Post-integration review" LOG paragraph to the **fleet-root** `/home/vgpnk/Projects/shokunin/LOG.md`.
  - The orchestrator restored that file to HEAD and saved the text to `/tmp/kaika/mado-misplaced-log.md`.
  - It is now appended verbatim to the lane `LOG.md` in `aeb33b5`, with a note. So `6e3b75f`'s LOG lacks it, but the measured content is unaffected.
  - No other mado write left the lane worktree or `/tmp`. Every other write used `cwd`, `git -C` or absolute paths. `git -C /home/vgpnk/Projects/shokunin log --author=mado` is empty, so no fleet-root commit was made.
  - The `cd` notice was relayed verbatim to every L2.
- **Open contract defects** (STATE dossier §5), carried into round 13 planned in `SCORECARD.md`:
  - D1: SKILL frontmatter triggers;
  - D2: gate registry row at `SKILL.md`;
  - D3: PROVINCE Core/Frontier/Adjacent;
  - D7: depth and adjacency unscored (reviewer F7, AXES.md:75-83 non-compliance);
  - D12: errata F2–F4 / walker-deep;
  - D19: `gate-standing-use.md:228` names harness `cf41efaa…` as "today", but the current harness is `75ed934d…`.
- **M12.** The fleet-round-1 report sits only at the lane path `.ufo/reports/round-1/mado.md`, not the fleet path its prompt required.
- **Harness path hazard.** From any kaika worktree, the gate's default harness path resolves into the sibling `kaika/tameshi-shokunin` worktree. Lanes that consume tameshi's harness must set it explicitly.

## Post-review fixes

Commit `8dbfc93` ("round-12: post-review fixes", lane identity, pathspec-limited: `corpus/SOURCES.md`, `corpus/lessons/round-12.md`, `corpus/knowledge/hyprland-config-era-r12.md`). These respond to the orchestrator adjudication and the W3 critic memo. No new claims were made, and every change is append-only except the in-place SOURCES cells that contract rule 2 allows.

1. **S030 is a duplicate of S017.**
   - In-place changes:
     - S030 `status`: mined → rejected;
     - S030 `used-by`: `corpus/knowledge/hyprland-config-era-r12.md` → `—`;
     - S017 `used-by`: gains `corpus/knowledge/hyprland-config-era-r12.md`.
   - Each change is logged old→new with its reason in `corpus/lessons/round-12.md` § Post-review registry changes.
   - S030's `teaches` cell cannot change in place, so the rejection reason and flip condition are in the SOURCES § Search log errata and in the lesson.
   - The U2 entry gets an appended erratum mapping its S030 citations to S017. Its `source:` header still names S030, so the join check prints one line: `entry … cites S030 without a mined row naming it`. That line is expected: the header is append-only and the erratum resolves the reference.
   - C3 is unchanged at 3/7 (U1–U3).
   - Registry status counts are now mined=27, queued=9, rejected=3. The other census results are unchanged: 39 rows, 0 malformed, no duplicate ids, no enum/tier violations, no missing `used-by` paths.
2. **Integrator note corrected.** Depth and adjacency are `unscored`, not `unchanged` (MANIFEST closure note above).
3. **Owed anchors.** S006, S008, S009 and S010 carry a section and an access date but no page revision. They are recorded in SOURCES § Search log as owed: the round that mines one appends a superseding row with the page's source-repo commit. No superseding rows were added now, because a same-URL row reads as a duplicate to the fleet census until the supersedes link is recognised. S007 already pins libinput 1.32.0.
4. **W3 critic memo** (`local://kaika-w3-mado-critic.md`):
   - **Fixed now (blocking, C3):** the portal search-log note used ART dossier ids (S008, S024–S030) that collide with registry ids, and its "excluded 0" count came from an empty `printf`. A search-log erratum maps the ART ids to registry ids (→ S031–S036, S037–S039) and gives the true accounting: 9 screened, 6 selected for U3, 3 kept queued, 0 excluded.
   - **E04/W04:** the validator now reports S030 as W04 (a warning, not an error). This is routed to the validator/contract authority.
   - **Debts, not blocking:**
     - C1 measures citation coverage only, not judgment quality. The rubric stays as pre-registered, and the orchestrator spot-check (U1 admit agreed, S012 reject agreed, S030 disagreed) is now recorded in the lesson § Outside spot-check.
     - C2 stays conditional on L0 #1 (gkeep intent).
     - The fleet-root LOG misplacement stays visible in the Integrator notes above.

**Validator:** `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mado-shokunin` → `W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes`, `ok`, **exit 0**.

Lane HEAD is now `8dbfc93`.
