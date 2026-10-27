# tsukuroi — round 46 report (hyaku run 9; L1 TsukuroiR46, attempt 1)

Lane `tsukuroi-shokunin`, branch `master`. Base `2042117cfb724170772f4c128cc2ddba0b61d817`, lane tip
`102cf670c16bb0edf23a30487bebe92ddd4e23b4` (`git ls-remote origin refs/heads/master` prints it). Outcome: **C1 PASS,
C2 FAIL**. This is an honest stop: admission needs every claim to verify, and C2 does not.

## Work performed

Declared claims, frozen at `72cc2609` before any seat (`SCORECARD.md` "Round 46 — declaration"):

- **C1 — operability.** Capability `census-identity`, sourced from S250 and S251, both opened this round.
  `tools/tsukuroi-census.sh --identity` prints one line naming the bytes bash executes. This closes routed debt D12,
  open since round 10.
- **C2 — depth.** Sourced from S246-S249. The goal was to admit the pending round-45 rows GR1-GR3 through verdicts the
  seats write into their own report files, each bound to the exact row bytes it read (orchestrator note,
  R45-C2-BINDING-CHANNEL).

Work items:

- **Frozen counters and controls.** Two counters with pre-data controls: C1 9/9 and C2 22/22 as expected
  (`.ufo/waves/round-46/controls/battery-summary-c1.jsonl`, `battery-summary-c2.jsonl`). The first C1 counter draft let
  the path-hasher control K2 PASS (`battery-summary-c1-draft1.jsonl`). I fixed the counter before the freeze by adding a
  case for a file replaced after bash opened it.
- **C1 implementation.** First landing `a4477049`. The wave then found two defects, fixed at `61e06740`:
  - seat C1LabUlimit found a wrong digest with `verified=yes` when a parent passes in a file descriptor
    (`.ufo/waves/round-46/w1/C1LabUlimit.md`). The fix: only the single `O_CLOEXEC` script descriptor is hashed. The
    old and new behaviour are recorded in `l1/held-fd-old-new.txt`.
  - seat C1RevImpl found that `--identity --help` exited 0. It now exits 2.
  - Selftest: 154 → 162 cases, including eight `(R46-C1)` cases.
- **C2.** GR2 and GR3 were narrowed at `b57740c2` after the counted `partly` reads. Twelve counted seats ran in `w1`
  and four residual seats in `r1`. GR2 was read `partly` again on its narrowed bytes by both residual seats
  (`r1/V46ResCritGR2.md`, `r1/V46ResRevGR2.md`). Rows stay pending: entry section "Gate status — round 46" in
  `corpus/knowledge/btrfs-scrub-grounding-r45.md`.
- **Routed defects:**
  - D1: SKILL and README status notes for round 44 (`c7e4d7d9`).
  - D2 and D3: correction notes (`b57740c2`).
  - D4: sources census run at this attempt's own start (`before/sources-census-start.txt`).
  - D5: the C2 counter binds seats by name and names no wave (control K15).
- **Gate registry.** Added the round46 table; registry coverage is PASS with 74 of 74 tools covered (`c7e4d7d9`).
- **Lesson and LOG.** Lesson `corpus/lessons/round-46.md` (six mistakes) and a LOG entry (`b313963c`).

## Landed changes

| Commit | Change | LOG.md round-46 entry |
|---|---|---|
| `72cc2609` | declaration, counters, controls, before receipts, S250/S251 snapshots | "freeze" |
| `a4477049` | `--identity`, entry `census-identity-r46.md`, SOURCES S250/S251 | "C1 … `a4477049`" |
| `b57740c2` | GR2/GR3 narrowing; D2/D3 notes | "GR2/GR3 narrowed", "D2/D3" |
| `61e06740` | C1 hardening (O_CLOEXEC, `--help`) | "hardened `61e06740`" |
| `c7e4d7d9` | SKILL identity section, D1 notes, registry round46, README note | "D1 …, registry round46" |
| `b313963c` | outcome: lesson, LOG, SCORECARD outcome/axes/capabilities, entry gate status, wave evidence | the entry itself |
| `b2eafc38` | r1 results and late reports; sources census and self-assessment final receipts | outcome receipts |
| `102cf670` | C2 final receipt; kill-rule receipts | outcome receipts |

## Before → after measurements

**C1**

Command:

```
python3 tools/score-census-identity-r46.py --revision <REV> --scratch <DIR>
```

- Before, at `2042117c`: FAIL. identity_ok 0, cli_ok 0, selftest_r46 0 (`before/c1-before-base.jsonl`).
- After, at `61e06740`: **PASS**. Every leg is 1; selftest 162/162; selftest_r46 8 (`l1/c1-61e06740.jsonl`).
- Kill rules did not fire:
  - Live PLANE and rollup lines and exit code 2 are unchanged. The only difference is the drivers memory counters,
    and those also differ between two runs of the base revision (`l1/planediff/`).
  - The census writes nothing in live mode (`w1/C1ExecLiveWrite.md`).
  - The adjacency anchors gate is PASS, and no line at or before :3383 moved (`w1/C1ExecAdjacency.md`).
  - The predecessor counters r39, q82 and r32 are PASS at the final revision. r35b is FAIL at both base and final
    with the same values (`l1/killrule/`, `w1/C1ExecPriorC.md`).
  - The A and B counter runs (r45, r44, r43, r42, r41, r40) at the final revision were still running when this report
    was filed. Their seats' runs at `a4477049` are under `w1/C1ExecPriorA`, `C1ExecPriorB`.

**C2**

Command:

```
python3 tools/check-scrub-admission-r46.py --revision <REV>
```

- Before, at `2042117c`: FAIL. r45_legs_ok 1, verdicts_ok 0, marks_ok 0.
- After, at `b2eafc38`: **FAIL**. r45_legs_ok 1, verdicts_ok 1, marks_ok 0 (`after/c2-final.jsonl`).
  - GR3 binds `holds` from two residual seats.
  - GR2 binds `partly` from two residual seats.
  - GR1 has four `holds` reports in `w1/`, but they bind only once the orchestrator writes `w1-results.json`, which had
    not been written at filing time. Once it lands, verdicts_ok reaches 2 at most. The C2 verdict is FAIL either way.

## Sources & frontier

- **Census.** Command:

  ```
  scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi
  ```

  At start it exited 0 with 249 rows (`before/sources-census-start.txt`). At the end it exited 0 with 251 rows
  (`after/sources-census-final.txt`).
- **Rows added:** two tier-A rows. S250 is code: GNU bash 5.3 `shell.c`, `general.c`, `general.h`. S251 is docs:
  `proc_pid_fd(5)`.
- **Old rows:** none changed a cell. S246-S248, S237 and S242-S244 were re-fetched byte-identical, and the S249 capture
  was re-run.
- **Gate rows.** The Gate rows, the reject table (bash manuals, the GNU manual, which was unreachable, `input.c`, and
  the staged registry) and the touched-row log are in the lesson's `## Gate`.
- **Sourced claim:** C1 rests on S250 and S251.
- **Mistake mined:** R46-C2-RESIDUAL-UNIVERSE-ONE-SHOT, with five more in the lesson.
- **Assimilation:** none. 52 id collisions (`.ufo/waves/round-46/assimilation/`), with the guard proved; the
  quarantine slice has 12 rows, none hand-checked.
- **considerthese:** "Burst-aware reading" mined from `considerthese/2026-10-26.md`.
- **Frontier:** nothing moves.

## Trend verdicts

- **expansion `unchanged`.** Knowledge 66 → 67 with the identity entry. GR1-GR3 were not admitted, and assimilation is
  none.
- **quality `improved`.** C1 landed and was hardened by falsification: the wrong-digest reproducer now prints
  unverifiable. Pins were re-fetched byte-identical. D1-D3 are corrected.
- **discernment `improved`.**
  - The pre-freeze battery caught a counter that a path hasher passed.
  - C2 refused to admit rows on `partly` reads.
  - Gaps were logged honestly: C2 counter holes F1-F3 and K22/K23, and the census selftest failing when TMPDIR contains
    a space, which is also true at base (`w1/C1ExecRerunB.md`).

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, sources: SKILL.md "Census identity — round 46" table (`c7e4d7d9`); no non-author verifier.
- [~] End-to-end domain task logged: the identity line and its `git log` lookup demonstrated (`w1/C1ExecRevLookup.md`); author-side.
- [~] Executable without oral context: `corpus/knowledge/census-identity-r46.md` re-derivation loop, run by seat C1CritClaim (`w1/C1CritClaim.md` (b)); seats are the lane.
- [~] No cross-domain bleed: adjacency anchors PASS (`w1/C1ExecAdjacency.md`); sibling scan `w1/ConnSiblings.md`.

## Round shape, seats, incidents

- **Round shape:** one v2 wave `w1` of 66 seats plus a residual call `r1` of 4 counted reviewer/critic seats, 70 seats
  in total.
- **w1 role mix:** executor 18, critic 14, reviewer 13, scribe 9, connector 4, scout 3, mutation-tester 2, sentinel 2,
  simplifier 1. Attack roles make up 44%.
- **Planner seat:** held by the L1.
- **Settled waves:** `r1` settled (WAVE-DONE received). The `w1` WAVE-DONE had not arrived at filing time. Reports
  still missing then: C1ExecPriorA, C1MutIdentity, C1SimplifyIdentity, EntryReview, ScoutR45Defects. Dead seats are
  whatever `w1-results.json` records once it lands.
- **Incidents:**
  - Fleet-root misroot of 12 files by seat C2ExecLiveSources, quarantined by the orchestrator (R46-FLEET-ROOT-MISROOT).
  - Seat D2D3Draft wrote tracked lane files (R46-SEAT-WROTE-LANE-FILES); its text was verified and adopted.
- **Lane state:** two late seat files are uncommitted in the lane wave dir.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **L0 questions:** none.
