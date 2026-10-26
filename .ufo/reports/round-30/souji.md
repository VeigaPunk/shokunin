# souji — round 30 report (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Base `9420341d9a814cb6089c25fb03a4cc9b23dc0d1b`. Final lane HEAD `2726c3d819a025dd2c193a5c780645d7fb71319a`; `git ls-remote origin refs/heads/master` prints that hash, and `jj-lane.sh state` reads `ahead=0 behind=0 tracked=0 untracked=0`. Lane L1: SoujiR30.

## Work performed

Declared claims (frozen in `census/round-30/records/preregistration.txt`, preregistration commit `d4928ec86b667e3d1ed0adb07fb088e500cf1631`; controls `bae103cba91884947a0557940e60c320f5512f75`; both landed before any seat ran):

- **C1 — calibration** (lowest non-retired axis, 7): the capability table's stated runnable counts agree with what the committed commands print. Verdict: **met**.
- **C2 — operability** (8): `tools/souji-landing-gate.py` evaluates a round's committed capture `census/round-N/waves/` and stops flagging template and capture-mapped pointers. Verdict: **missed** by the frozen kill rule at its landing commit.
- **C3 — coverage** (8; F1 frontier "keep-ref expiry unmeasured"): one sourced, measured knowledge entry. Verdict: **met**. This is the round's sourced claim (S220, S221 opened this round).

Work items:

- Preregistration, three frozen counters (`tools/souji-capability-agreement.py`, `census/round-30/c2-counter.py`, `census/round-30/c3-counter.py`), the 18-row C1 enumeration `census/round-30/c1-rows.tsv`, start census and axis check (`claims=3 flags=0`): commit `d4928ec86b667e3d1ed0adb07fb088e500cf1631`.
- Do-nothing and junk controls scored with the frozen counters (`census/round-30/records/controls.tsv`), plus the full C1 base output (`c1-before.txt`): commit `bae103cba91884947a0557940e60c320f5512f75`.
- Routed r29 closure defect D3: committed the observed green outputs of the r29 and r28 fixtures (`census/round-30/records/d3-green-*.txt`): commit `df6afe817d096e4ad71ba2b9cc21a83f126eb658`.
- Wave-1 attacks (SwarmCritic24/25/26, SwarmReviewer20/23, SwarmRevenger34) showed no-op cheats meeting the frozen C2 and C3 targets and a `cmd=` bypass of C1. Stricter-only amendments A1 (C2 v2), A2 (C3 v2), A3 (C1 tool) and amended controls landed before any claim: commit `02aea483b4366da8705342657995a310cd21a708` (`census/round-30/records/amendments.txt`, `controls-amended.tsv`).
- C1: 13 append-only `R30-CORRECTION` lines at the end of SCORECARD.md: commit `7b16731fcd8ab9b95220b50603314aa8dc92b2ec`.
- C2: the gate change plus the frozen D1-D7 fixture `tests/fixtures/r30-landing-gate-discovery.py` and its red-before record: commit `68447afef62e4761249af55a2467657f04046537`.
- C1/C2 landing measurements and the wave-1 evidence capture: commit `aea0525305167b8765ce36a3f20e68b1996274b8`.
- C3: `corpus/knowledge/jj-keep-ref-expiry.md`, new rows S220 and S221, used-by additions on S054 and S063, fixture `tests/fixtures/r30-jj-keep-expiry.sh`, record `census/round-30/records/jj-keep-expiry-run.txt`, tag-pinned snapshots `census/round-30/sources/`, the F1 map row, and the README, PROVINCE and SKILL text: commit `76c94eb41fc38093d7143a016006b6275e102d5d`.
- Mined mistake fix: an append-only carry of round 29's seven uncarried seat failures, plus the D4 per-entry reject reasons, in `corpus/lessons/round-29.md`. Commit `936efc8a0f5a6a0d38a7d6ddb7d28f7a96273265`; on round 29 the gate went from rc 1 `findings=7` to rc 0 `findings=0` (`census/round-30/records/m1-r29-carry-red-before.txt`, commit `9dcd367655fc28ba73d679a0e2cadaff96d2bcb8`).
- Wave-2 integration: capture of both waves (425 records), five refuted entry sentences corrected append-only, the SKILL keep-ref headline corrected, the r29 carry disposition corrected, and the cited literal-history file committed at its path: commit `f732978506f3fa8ef32d4af1b4ee5bc962603aaf`.
- Lesson `corpus/lessons/round-30.md` (Gate, Findings, Seat-reported failures, Mistakes, Receipts, Residuals, Wave), QUALITY Q63-Q66, SCORECARD r30 measurements, capability rows and planned r31, LOG entry, end census: commit `393b011a8221259abe6825fc3b637fcdc1b0e1eb`.
- Final-tip receipt `census/round-30/records/final-tip-measure.txt`, serial runs at `393b011…`: commit `2726c3d819a025dd2c193a5c780645d7fb71319a`.

Round shape: **two v1 waves**, dispatched inline by the orchestrator through ready files. W1 `souji-r30-w1` (build plus first falsifiers) had 35 seats: executor 7, scribe 8, scout 4, reviewer 4, critic 4, mutation-tester 3, connector 2, sentinel 1, revenger 1, simplifier 1. Flash roles were 22/35 and attack seats 11/35. W2 `souji-r30-w2` (falsify the landed claims) had 34 seats: executor 7, critic 9, reviewer 6, mutation-tester 5, scout 2, connector 2, scribe 1, sentinel 1, simplifier 1. Flash roles were 19/34 and attack seats 20/34. Round total: **69 seats**, no residual call, **0 dead seats**: 35/35 and 34/34 results entries carry non-empty output (`census/round-30/waves/w1-results.json`, `w2-results.json`). The L1 held the canonical planner seat. The validator rejects `planner`, so the §3 planner role is recorded as the L1 itself. The §3 L2 floor (connector, executor ×3, scribe, scout, reviewer, critic) is met inside W1. Seat routing followed the host route table; no `model` was passed.

## Landed changes

Each change ties to `LOG.md` entry "2026-10-26 — Round 30 attempt 1: capability-row literal agreement, committed-capture report discovery, F1 keep-ref expiry" and to its commit:

| change | commit |
|---|---|
| preregistration, frozen counters, C1 rows, start census | `d4928ec86b667e3d1ed0adb07fb088e500cf1631` |
| controls + C1 base output | `bae103cba91884947a0557940e60c320f5512f75` |
| D3 green fixture outputs | `df6afe817d096e4ad71ba2b9cc21a83f126eb658` |
| amendments A1-A3, amended controls | `02aea483b4366da8705342657995a310cd21a708` |
| C1 SCORECARD corrections | `7b16731fcd8ab9b95220b50603314aa8dc92b2ec` |
| C2 gate + fixture | `68447afef62e4761249af55a2467657f04046537` |
| C1/C2 measurements, wave-1 capture | `aea0525305167b8765ce36a3f20e68b1996274b8` |
| C3 entry, rows, fixture, record, snapshots, docs | `76c94eb41fc38093d7143a016006b6275e102d5d` |
| r29 lesson carry + D4 | `936efc8a0f5a6a0d38a7d6ddb7d28f7a96273265` |
| C3 measurements, M1 receipt | `9dcd367655fc28ba73d679a0e2cadaff96d2bcb8` |
| wave-2 integration and corrections | `f732978506f3fa8ef32d4af1b4ee5bc962603aaf` |
| lesson, QUALITY, SCORECARD, LOG, end census | `393b011a8221259abe6825fc3b637fcdc1b0e1eb` |
| final-tip receipt | `2726c3d819a025dd2c193a5c780645d7fb71319a` |

Inherited state: the worktree was clean at round start (`tracked=0 untracked=0`), and `.ufo/watchdog.log` has no earlier attempt of this round. Nothing was inherited and nothing was discarded.

## Before → after measurements

- **C1** — `python3 -B tools/souji-capability-agreement.py --root <lane> --rev <full40> --base 9420341d9a814cb6089c25fb03a4cc9b23dc0d1b --list-rev d4928ec86b667e3d1ed0adb07fb088e500cf1631` (v1 is the blob at `d4928ec`; A3 is the current file).
  - Before, at base: `SUMMARY k1=13 k2=0 mismatches=13 rows=18 pointers=10` (`census/round-30/records/c1-before.txt`).
  - After, at the C1 landing commit `7b16731fcd8ab9b95220b50603314aa8dc92b2ec`: `SUMMARY k1=0 k2=0 mismatches=0 rows=18 pointers=10` under both v1 and A3 (`c1-after-v1.txt`, `c1-after-a3.txt`).
  - Final tip `393b011…`: the same reading (`final-tip-measure.txt`).
  - **Met.** Honest split of the 13 base mismatches:
    - 7 are notation (the stated numbers equal the printed ones).
    - 4 are counts that grew after the row was written.
    - R16's cell omits a required `--tool`.
    - R18 is a v1 stdout+stderr artifact.
  - The capability cells stay as written; the record now carries the observed state beside them.
- **C2** — `python3 -B census/round-30/c2-counter.py --root <lane> --rev <full40> --base 9420341d9a814cb6089c25fb03a4cc9b23dc0d1b --fleet-root /home/vgpnk/Projects/shokunin`, plus A1 `census/round-30/c2-counter-v2.py` with the same arguments.
  - Before, at base: `reports=0 cne=1 dangling=3 other=0 fixture=fail redarm=fail regress=same` (`controls.tsv`).
  - At the C2 landing commit `68447afef62e4761249af55a2467657f04046537`: `reports=86 cne=0 dangling=1 other=7 fixture=ok redarm=ok regress=same` (`c2-after-v1.txt`). The A1 v2 run printed `bind=fail` (`dangling=1`) and `regress_full=differs` (`c2-after-v2.txt`).
  - Final tip `393b011…`: v1 `reports=86 cne=0 dangling=0 other=0 fixture=ok redarm=ok regress=same`; v2 every leg `ok` except `regress_full=differs`.
  - **Missed.** The prereg requires the target at the landing commit and at the tip, and the landing commit printed `dangling=1`.
  - Cause of the dangling pointer: the C1 SCORECARD block (landed one commit earlier) cited `.ufo/waves/round-30/w1/deliver-c1-literal-history.tsv` before any round-30 capture existed. The changed gate reported that real dangling pointer correctly.
  - Cause of `regress_full=differs`: A1's err-tail regex expects a tab where the selftest prints a space.
  - Wave-2 SwarmCritic17 and SwarmCritic20 independently confirmed the MISS reading.
- **C3** — `python3 -B census/round-30/c3-counter.py --root <lane> --rev <full40>`, plus A2 `census/round-30/c3-counter-v2.py`.
  - Before, at base: `SUMMARY legs=9 fail=8 f1_entries=2`; v2 `e1..e4=fail f1_exact=2`.
  - After, at the C3 landing commit `76c94eb41fc38093d7143a016006b6275e102d5d` and again at the final tip: `SUMMARY legs=9 fail=0 f1_entries=3`; v2 `e1=ok e2=ok e3=ok e4=ok f1_exact=3` (`c3-after-v1.txt`, `c3-after-v2.txt`, `final-tip-measure.txt`).
  - **Met.** Wave 2 refuted five sentences of the entry; they were corrected append-only before closing.

No-harm counters, base → final tip (`final-tip-measure.txt`; wave-2 SwarmExecutor04/05):

| counter | base → final tip |
|---|---|
| registry agreement | `k1=0 k2=0 mismatches=0` → same |
| coverage agreement | `grounded=15 mapped=15` → `grounded=16 mapped=16 dangling=0 mismatches=0` |
| declared-evidence | `mismatches=21` → `21` (it was 22 at `7b16731`, repaired at `f732978`) |
| r29 receipts counter | `manifests=5 failed=0 uncovered=0 floor_violations=0` at the tip |
| round-30 capture verify | `records=425 failed=0 uncovered=0` at the tip |
| every lane fixture/selftest green at base | still green at the tip (26 commands, 0 harms) |

Owned scores are unchanged (calibration 7, coverage 8, operability 8).

## Sources & frontier

- **SOURCES rows:** `git show <rev>:corpus/SOURCES.md | grep -cE '^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` gives 143 at base `9420341d…` and 145 at the tip `2726c3d8…`.
- **Rows added by tier:** A=2 — S220 (jj CLI reference at v0.45.1, docs) and S221 (jj `docs/operation-log.md` at v0.45.1, docs). Both are `mined` and opened 2026-10-26.
- **Rows touched (old → new):**
  - S054 `used-by`: `corpus/knowledge/jj-colocation-receipts.md` → that path plus `corpus/knowledge/jj-keep-ref-expiry.md`.
  - S063 `used-by`: the same change.
  - The changes are logged in `corpus/lessons/round-30.md` `### SOURCES touched-row log`.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  - Start: `souji ok …/corpus/SOURCES.md`, exit 0, 36 W04 (`census/round-30/records/census-start.txt`).
  - End: exit 0, 36 W04, no error class (`census-end.txt`).
- **Frontier advanced:** F1 "keep-ref expiry unmeasured" is now measured (`corpus/README.md` `## Round 30 — F1 keep-ref expiry measured`, F1 map row). F1 stays frontier.
- **Mined mistakes:** in `corpus/lessons/round-30.md` `## Mistakes`. M1 (round 29's uncarried seat failures) is shown able to fail: gate rc 1 → 0 (`m1-r29-carry-red-before.txt`). M2 (the L1 cited an uncommitted wave path, a recurrence of r29's D1) became Q65.
- **Sourced claim:** C3 (S220, S221).
- **Assimilation:** none. Five staged F1 package entries in `merge/souji/` were rejected per entry: they cover git worktree-registration grace periods, not jj keep refs. No package row was appended.
- **considerthese/:** absent in this lane.
- **Gate:** at least one admit (the entry, S220, S221) and at least one reject (the five package entries, plus the loose-ref mtime reading) are recorded for the closure's spot-check.

## Trend verdicts

- **expansion — improved, narrowly.** One admitted entry on F1 ground the map listed as unmeasured, citing `mined` rows S220/S221 opened this round (`census/round-30/records/c3-after-v1.txt`). There are also two capability rows with running demonstrations (SCORECARD `### Round 30 capability rows`). Counter-argument on record: SwarmCritic18 found 10 of 18 propositions restate held text, and five admitted sentences were refuted by wave 2. They were corrected append-only before closing, but the closure may rule that the entry failed its bar at admission.
- **quality — improved.**
  - 13 stale capability literals now carry their observed output (`c1-after-a3.txt`).
  - Round 29's seven uncarried seat failures are carried (gate rc 1 → 0).
  - The D4 reject reasons are corrected and the D3 green outputs committed.
  - The entry's refuted sentences are superseded in-file; no entry is left false and unmarked.
  - C2's claim missed, but the landed gate change harms no fixture.
- **discernment — unchanged.** No outside spot-check of this round's gate exists yet. Criteria Q63-Q66 are lesson-backed (`corpus/lessons/round-30.md` Findings/Mistakes). The admit/reject agreement awaits the non-author closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Gate registry rows `souji-capability-agreement`, `r30-landing-gate-discovery`, `r30-jj-keep-expiry`; error-pattern bullet "a keep ref is removed by jj's own gc threshold"; corpus/SOURCES.md S220/S221
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep); round 30 LOG entry at the end of LOG.md
- [~] Instructions executable by an agent without oral context — census/round-30/records/final-tip-measure.txt (every claim re-measured from committed bytes by documented commands); tests/fixtures/r30-landing-gate-discovery.py 7/7
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md `## Round 30 boundary note (F1 keep-ref expiry)`; census/round-30/waves/w1/SwarmConnector31.md and census/round-30/waves/w2/SwarmConnector31.md (zero contested scope)

## Other report lines

- **Cross-domain evidence encountered:**
  - Sibling scans found no contested scope. `scripts/hyaku/jj-lane.sh` (fleet, operator-side) never runs `jj util gc` or `jj op abandon`, so keep refs in lane repos are never expired by lane tooling. That is fleet-tooling ground, reported, not absorbed.
  - Untracked fleet-root files `baseline-plain.txt` and `.ufo/waves/round-34/` belong to other lanes; they name no souji path and were not touched.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no file written by a souji round-30 seat. No copy or delete was needed.
- **Stale-lane:** this mission launched `2026-10-26T01:12:04-03:00` (`.ufo/watchdog.log`, respawn-per-round driver) and is progressing: 13 lane commits since launch. No other mission of this lane is open.
- **Tool installs:** none, by the L1 or any seat. pacman stayed paused.
- **Scratch:** `/fast/scratch/hyaku/souji-r30` was removed after landing.
- **Open L0 questions:** none filed this round.
- **Residuals routed to r31:** these are listed in SCORECARD `### Planned (appended at round 30)` and in the lesson's `## Residuals`:
  - discovery precedence (one force-added wave file hides the capture);
  - the `round-` cut rule and `%d` templates;
  - A1's regex defect;
  - C1 counter concurrency;
  - enumeration widening (SCORECARD.md:164 and :168);
  - a sentence-to-record check for admitted entries.
