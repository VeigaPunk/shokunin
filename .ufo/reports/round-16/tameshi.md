# tameshi — round 16 report (hyaku phase 2, attempt 1)

Lane HEAD `017a2b0c0d1a8fe513e41710416c87b9d6ef9ae9` (pushed; ahead 0, porcelain clean). Baseline `28aeef498cc070c3183271b709bc79d344ff547a`. Measured commit `09ee1d099190918ec388019bb79afbb6b93f1ff2`.

## Work performed

Declared claims (2), both on the tied-lowest owned axes (depth 6, calibration 6):

- **C1 — depth 6→7:** a seventh recorded mutation case. The target is kumitate `scripts/round-gate.mjs`, ledger leg `js-round-gate`.
- **C2 — calibration 6→8:** a full-page cold-read of `SKILL.md`. It earns the SHONEN box-3 lane assertion that round 1's Appendix A+B-only read could not earn (QUALITY 13).

Work items:

- **Pre-registration.** I assembled 10 single-edit defects with predictions (5 kill-aimed, 5 hole-aimed) from arm-class-matrix §13 and the wave-1 seat fragments. Committed and pushed in `e69b488` (committer time 10:39:59-03:00) before any mutant ran. Files: `.ufo/evidence/round-16/round-gate/{round-gate.defects.spec,predictions.json,suite.txt}`; spec sha `e99b87eb…`.
- **Sweep.** Run at 13:40:15Z under runner `75ed934d…`. Result: `MUTATE: DONE (… killed=5 survived=5 inconclusive=0 kill-rate=50%)`, control GREEN, `MUTATE_RESTORE: OK`. All 10 of 10 predictions held (`round-gate/sweep/results.tsv`).
- **Guarded suite.** The suite runs under `env -i` with a private HOME and TMPDIR per defect. RGSentinel showed that an exported `GIT_DIR` makes the pristine control commit into a foreign repo. The guard scrubs the environment but does not confine; GuardAudit's limits are recorded in note §6.
- **Ledger leg 7.** Embedded in `tools/mutate-and-run.sh` (final sha `0673d2e5…`):
  - `--regression` → `REGRESSION: PASS (cases=7 passed=7; ledger legs exact …)`, rc 0.
  - `--selftest` → `83/83 pass`.
  - A new leg-count agreement check fails on the dropped-tuple mutant that MutateLeg found surviving (`round-gate/legcount-redbefore-mutant.txt`: 81/82).
- **Survivor witnesses.** Probes for A2, B2 and E1 (pristine 0 / mutant 1) and a 1040-byte C1059 probe (`round-gate/survivor-probes/`). CKIND is argued equivalent for gate behaviour; CKINDCheck held.
- **Knowledge note.** `corpus/knowledge/mutation-case-kumitate-round-gate.md`, with appended rows in the fleet-kill-rate ledger, arm-class matrix §13 errata, the README coverage row and the PROVINCE Core append.
- **C2 wave-1 cold-read.** 30 seats covered 51 of 51 snapshot buckets. They found 13 wrong or stale statements, repaired in place with line counts kept; AnchorCheck: 22 of 22 self-anchors resolve. The repairs are listed in `SKILL.md` §"Errata — round 16 full-page cold-read".
- **C2 re-reads.** Fresh seats re-read every bucket changed after a read: wave 2 had 17 RR/replica seats plus WholePage; the residual check had 8+1 seats (`w3/RX*.md`). Ledger `.ufo/evidence/round-16/coldread/ledger.json` has 75 entries across 4 page versions and covers 54 of 54 buckets of the measured page (sha `906fb649…`).
- **Counting command fix.** `.ufo/evidence/round-16/measure.py` was repaired to read SHONEN's continuation-line link. Red-before at the same rev: `measure-repair/old-tool-at-c699c8c.json` false, repaired tool true. Selftest 38/38.
- **Routed defect 1 (round-15 spot-check).** The sibling-overlap scan is credited: `w1/Overlap1.md` covers 23 of 23 `shokunin.conf` lanes with 0 ownership contests. Its manifest is `.ufo/evidence/round-16/Overlap1/`; the replay drift is shown, not hidden. Overlap2 and C1Overlap also ran.
- **Routed defect 2.** Usage attribution, repaired append-only with `.ufo/evidence/round-16/attribution/reattribute.py`:
  - `correction.json` names exactly `usage-proof-new` and `gate-usage` (`context_consistent→usage_error`).
  - `verification-3.json` sha `3c419055…` is unchanged.
  - The selftest has 8 fixtures (new rule 8/8, old rule fails 5/8, old-rule fidelity 14/14). It kills 5 of 6 weaker-rule mutants; the sixth is equivalent (`selftest-mutants.json`).
- **Frontier step.** SOURCES gained S052–S057; `corpus/lessons/round-16.md` has 10 `## Mistakes` rows; QUALITY 18–22 were added.
- **Planner seat.** The L1 held the canonical planner seat; PlannerWalk (a connector) was a bounded planning data-walk.

## Landed changes

All lane commits carry `tameshi-shokunin <tameshi@shokunin.local>` and were pushed before this report. The LOG.md entry is "Round 16 — seventh recorded case and full-page cold-read".

- `e69b488` — pre-registration spec, predictions and suite; wave-1 specs and reports; SKILL snapshot.
- `c699c8c` — case-7 note; runner leg 7; SKILL in-place repairs and errata; S052–S057; QUALITY 18–20; lesson draft; PROVINCE, README, ledger and matrix appends; attribution repair; measure.py and assemble.py.
- `05a2247` — post-wave-2 repairs: SKILL residuals; runner leg-count check; hardened attribution, measure and assemble selftests; wave-2 reports.
- `3490708` — cold-read ledger; errata provenance fix; wave-2 corrections (PROVINCE, ledger, matrix appends; QUALITY 21–22); residual reports.
- `09ee1d0` — RX9 errata re-read folded into the ledger. This is the measured commit.
- `017a2b0` — SCORECARD round-16 section and LOG entry.

Inherited state: one remote operator commit, `0baf52e` (`considerthese/2026-10-20.md`). It was rebased under the pre-registration commit and never edited; its proposals 1 and 3 match this round's moves. `corpus/lessons/round-15-verifier-spotcheck.md` is non-author and was never edited; its routed defects 1, 2 and 3 are dispositioned in the lesson. There are no `operator-*.md` lessons and no earlier attempt of this round (watchdog line 476 is attempt 1). No inherited lane leftovers.

## Before → after measurements

Counting command: `python3 .ufo/evidence/round-16/measure.py --rev REV`. It exits 0 at both revisions; outputs are `.ufo/evidence/round-16/measure-28aeef4.json` and `measure-09ee1d0.json`.

| Claim | Before @28aeef4 | After @09ee1d0 |
|---|---|---|
| C1 depth | `recorded_cases 6`, `depth_score 6`; command D (`SCORECARD.md:73`) → `recorded_cases=6 depth_score=6` | `recorded_cases 7`, `depth_score 7`; guardrail header/calls/tuples 7/7/7, `unique_recorded_gates 7` |
| C2 calibration | `calibration_restraint_score 6`, `coldread.sections_covered 0/51` (no ledger), `box3_ledger_link false` | `calibration_restraint_score 8`, `coldread 54/54`, `box3_full_page true`, `box3_ledger_link true`; marks `~ ~ ~ ~` unchanged |

The intermediate measurement `measure-3490708.json` shows 53/54 before the errata re-read. The 8 is the lane cap: the last 2 points need independent promotion review. It is a lane measurement pending non-author closure.

## Sources & frontier

Rows 49 → 55 by the same census, run at round start and round end.

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`

Start output (`.ufo/evidence/round-16/census-start.txt`), exit 0:

```
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

End output (`census-end.txt`), exit 0: identical three lines.

- **Added by tier:** A +5 (S052 Stryker supported mutators, S053 kumitate round-gate.mjs @364f1d5, S054 Diátaxis compass, S055 Python doctest, S056 PIT mutators) and B +1 (S057 Papadakis et al. survey, author preprint; published chapter returned 403). Totals: tiers A 42→47, B 5→6, C 2→2; status mined 22→28, queued 24→24, rejected 3→3; malformed 0.
- **Rows touched old→new:** none. Only the id-allocation footer changed (next id S052→S058), and that is logged in the lesson Gate.
- **Re-opened in wave 2:** all six rows (Reopen* seats), all hold. The frozen manual census commands came out clean (SourcesCensus).
- **Sourced claims:** C1 cites S052, S053, S056 and S057; C2 cites S054 and S055.
- **Frontier:** no item moves to Core (FrontierMap; README round-16 append).

## Trend verdicts

- **expansion: improved.** One new admitted knowledge entry, the case-7 note. It holds a measured gate the coverage map did not hold before; the old map had only the §13 projection. Its `source:` cites mined rows S053, S052, S056 and S057, and its coverage row was added the same round. The ground is Core surface (kumitate `scripts/*`), not frontier.
- **quality: improved.** Stale or wrong entries were superseded with evidence, and no admitted entry failed its re-check:
  - 13+6 SKILL statements repaired and re-read by fresh seats;
  - matrix §13 projections measured, and four of its readings corrected;
  - the PROVINCE "six gates" and service-scope lines corrected by append;
  - EvidenceImmutable: 38 additions, 0 modifications to prior evidence.
- **discernment: improved.** The outside round-15 disagreements (routed 1 and 2) became a credited scan and a failure-backed fix. Ten mined mistakes became QUALITY 18–22, each citing its lesson row and its red-before evidence. This round's own non-author admit/reject spot-check is the closure's duty and is not claimed here.

No-harm monitors (SCORECARD round-16 table): coverage, operability, freshness and adjacency are unchanged. One note on operability: the round-14 disposition gate now exits 2 at `--root .`, by design, because its pinned runner input moved. Its archived-root form exits 0 (RR10, RX5).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, unchanged (`SHONEN.md:5-6`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion, unchanged (`SHONEN.md:7-8`).
- [~] Instructions executable by an agent without oral context — lane assertion, full page. The link now points to `.ufo/evidence/round-16/coldread/ledger.json` (`SHONEN.md:9-10`). There is no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion. PROVINCE Core and corrections were appended this round (`PROVINCE.md:48-71`).

## Waves, seats, extras

- **Wave 1:** 68 seats in one validated `task` call (policy v2, `spec1.json`/`dispatch1.json`), 68 completed, 0 dead. Roles: executor 25, scout 14, reviewer 10, scribe 5, connector 4, critic 4, revenger 4, sentinel 2.
- **Wave 2:** 67 seats in one validated call (`spec2.json`), 67 completed, 0 dead. Roles: executor 22, reviewer 18, scout 8, critic 5, scribe 5, mutation-tester 4, sentinel 3, connector 2.
- **Residual re-read:** one ordinary call of 8 reviewers (`spec3-residual.json`), plus 1 reviewer (`spec4-errata.json`). The session job cap (100) refused that last seat once before it dispatched. Round total: 144 seats.
- **Dispatch payloads:** the host's `task` schema requires `solutionSpace`, so one was added to each validated task payload. Names, roles and task text were passed unchanged.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only driver `.ufo/state/*.report-baseline` files and `watchdog.log`. There are no tameshi round-16 seat strays (MisrootSweep agrees).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none, by the L1 or any seat as reported. No pacman transaction was run.
- **L0 questions:** none appended.
- **Open debts, named:**
  - the six older ledger legs run without the env scrub;
  - `bwrap` confinement for untrusted mutants;
  - successor sweeps of the stale legs;
  - the round-7 runner line anchors.
