# mori — round 35 (attempt 1, L1 MoriR35)

Lane tip `42a8ae651a006443ab17e2690279e28623af8d39` (entering `dd76eb79`). Round shape: default v1. One pre-data
control wave C0 (12 seats, plain task call), wave 1 (32, validated v1), wave 2 (36, validated v1), and one residual call
(3). Total: 83 seats.

## Work performed

Declared claim (1, frozen before any seat at `f2d28711`): **C1 — calibration (5, tied lowest)**. The last
`## Capabilities` section of SCORECARD binds every capability that fleet MANIFEST@`37b51a24` records under an admitted
mori closure (18 of them). Each row carries its key, its round and a strong artifact, and the section holds no other
row (P-C1, `.ufo/waves/round-35/contract.md`). Sourced: S199 (protocol AXES.md) and S200 (MANIFEST), both opened this
round.

- **C1 measured.** `count-c1.py` at the tip gives `C1=met` (`evidence/c1-after.txt`), reproduced by ExecTipRerun and
  by an independent oracle (ExecOracleIndep). **C1 is not verified (honest stop), and this is the L1's own proposal.**
  - Before data, control 10c met P-C1 (empty capability and what cells, `evidence/c1-controls.txt`). The L1 ruled it a
    residual. QUALITY 98, which held at entry, required a re-design instead.
  - After data, the denial, word-bag and off-topic controls also met P-C1 (`w2/CtlDenial.md`, `CtlWordBag.md`,
    `CtlOffTopic.md`). This is the shape of kaidoku r32's falsifier.
  - CritC1Verdict agrees (`w2/CritC1Verdict.md`). The counter, rule and target were never amended.
- **Register content judged row by row** (non-author, rule quoted from the pre-data receipt):
  - 18/18 rows `supported`, and 18/18 pointers relevant (`w2/JudgeRows*.md`).
  - JudgeCanary shows the rule flags 5/5 altered rows (`w2/JudgeCanary.md`).
  - This rests on judges, not on P-C1.
- **Round-34 routed defects** (spot-check §6), with the outcome table in `corpus/lessons/round-35.md`:
  - Supersede rows S201 (S182) and S202 (S193), and a correction of `round-34.md:46`.
  - An append-only correction to the dangling `w1/` pointer in `disk-write-rate-r33.md`.
  - `SKILL.md:834` marked as observed, not sourced. Seventeen files were opened and S203 and S204 rejected.
  - A QUALITY 98 correction (D1, D2, D4).
  - QUALITY 100, which answers clause 2 of r33 §8 item 1.
  - All were reviewed in wave 2 (`w2/Review*.md`, `Gate*.md`).
- **Axes table.** The operability and depth `Last change` cells now read round 31 (`SCORECARD.md:11-12`;
  `w2/ReviewAxesFix.md`).
- **Mistakes M1–M5** (lesson `## Mistakes`):
  - M1: a met control was ruled a residual. Fix: QUALITY 101.
  - M2: SOURCES cells were edited in place. Fix: QUALITY 102 plus `check-sources-appendonly.py`, which can fail:
    `round_changed=[S182,S193]`, exit 1, at `dd76eb79`.
  - M3: the capabilities field sat stale at "none yet" since `d677cf3`.
  - M4: the L1 ran `git add -N .` in the lane.
  - M5: Gate format and count errors.
- **No-harm repairs.**
  - CritNoHarm found depth, operability and calibration harm at `cedb0ec4` (N1–N3). These were revised at `6d3d94b3`.
  - The residual call confirmed that N1 and N2 are fixed.
  - It found a new N3 gap (endpoint-blind `round_changed`). That gap was fixed at `42a8ae65` and is not re-judged.

## Landed changes

| Commit | LOG entry | What |
|---|---|---|
| `f2d28711` | `LOG.md` Round 35 | freeze: contract, `count-c1.py`, before receipt, census start |
| `913df22e` | same | C0 control receipts (12 seats), wave-1 spec |
| `721040a9` | same | C1 capabilities register (18 rows) |
| `cedb0ec4` | same | S199–S204, round-34 repairs, QUALITY 98 correction and 100–102, Axes fix, lesson, append-only check, wave-1 reports |
| `6d3d94b3` | same | wave-2 reports and revisions after wave 2, SCORECARD outcome, LOG, C1 after receipt, census end |
| `42a8ae65` | same | residual reports, checker `round_changed` fix, count corrections |

All six are `landed <hash>` lines from `jj-lane.sh` (remote verified).

## Before → after measurements

- **C1**:
  - Command: `python3 /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-35/count-c1.py <rev>`. The counter
    sha256 is `27b82d71…` and is unchanged since `f2d28711`.
  - Before, at `dd76eb79`: `rows=5 matched=0 missing=18 bad=0 extra=5 mismatches=23 C1=unmet`, exit 1.
  - After, at `cedb0ec4`: `matched=18 missing=0 bad=0 extra=0 mismatches=0 C1=met`, exit 0. The same holds at
    `42a8ae65`.
  - Not verified: see Work performed.

## Sources & frontier

- Rows: `grep -c '^| S[0-9]' corpus/SOURCES.md` went from 198 → 204. Added:
  - S199 and S200: A, `mined`.
  - S201 and S202: A, `mined`, supersede rows.
  - S203: C, `rejected`.
  - S204: `rejected`.
- Rows touched old→new: none. The diff is insertions only (GateS201, GateS202).
- Census:
  - Start: `mori ok`, EXIT=0, 12 W04 (`evidence/census-start.txt`).
  - End: `mori ok`, EXIT=0, 13 W04 (`evidence/census-end.txt`). The new W04 is S201 sharing S182's URL across scopes.
- Frontier: FR6's stacked-device double count is still unsourced. Seventeen files were opened and none states it.
- 18 SOURCES ids carry in-place edits made before round 35. They are listed by the check and routed as debt
  (`w2/ScoutAppendDebt.md`).

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry was added on uncovered ground. The register records existing
  capabilities.
- **quality: improved.**
  - Every round-34 routed repair landed and was judged supported.
  - The 18-row register was judged supported row by row.
  - The SOURCES append-only debt is now detectable, and a check that can fail exists.
- **discernment: improved.**
  - Real gate rejects: S203 and S204, the C1 self-rejection, and five mistakes mined.
  - QUALITY 100–102 were mutation-tested (`w2/MutQ10*.md`).
  - Against: M1 is a discernment miss by the L1.

## SHONEN

- [~] SKILL.md decision tables, error patterns, cited sources: `SKILL.md` Round35 corrections (ReviewSkillCorr,
  ResGateFixes).
- [~] End-to-end domain task logged: `LOG.md` Round 35.
- [~] Instructions executable without oral context: `corpus/QUALITY.md` 102 check command (ResQ102Check reran it).
- [~] No cross-domain bleed: `git diff dd76eb79 42a8ae65 -- PROVINCE.md` is empty (CritNoHarm adjacency holds).

## Gate

Real rejects, each with its reason:
- S203 (collectl docs): it never says the dm I/O lands on the backing line.
- S204 (dm.c): the clone accounting is not shown.
- C1: its counter credits content-free and denial prose.
- RowR25's draft swapped two keys and was fixed before landing.

## Round mechanics

| Wave | Seats | Roles | Dead / no report |
|---|---|---|---|
| C0 (pre-data controls) | 12 | 6 executor, 6 mutation-tester | CtlParserAttack: provider refusal `cyber_policy` (hold, not retried) |
| 1 (v1) | 32 | 19 scribe, 3 executor, 3 reviewer, 2 critic, 2 scout, 1 sentinel, 1 connector, 1 revenger | none |
| 2 (v1) | 36 | 24 reviewer, 6 mutation-tester, 2 executor, 2 critic, 1 sentinel, 1 scout | GateS204 returned without a report |
| residual | 3 | 1 critic, 2 reviewer | none |

- Planner: the L1 holds the planner seat.
- Dispatch: each wave was sent as one task call through `eval tool.task`, carrying the validator's taskCall unchanged.
  The harness requires a `solutionSpace` field, so a generic one was added (`dispatch-log.txt`).
- Misroot: RowR22 wrote empty directories under the fleet path `mori-shokukin/mori-shokunin/`. The L1 removed them with
  `rmdir`. No other fleet-root file names mori or round 35.
- Containment: the L1's `git add -N .` (M4) was reset by the next helper commit. `git status --untracked-files=no` is
  empty.
- **Stale-lane**: respawn-per-round driver; no other mission of this lane is open.
- **Tool installs**: none. **L0 questions**: none.
