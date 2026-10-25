# tameshi — round 31 report (L1 TameshiR31, attempt 1)

Lane head `08125328f87df92d3f25d0034ee792253ecbcbd9` (pushed; `jj-lane.sh state`: local=remote, ahead=0,
tracked=0 untracked=0). Base `36c1d3933f680125aeefc447f07db0f03004901a`.

## Work performed

Declared claim (one): **C1 — calibration, measured.** The surface is the standing rows of `SCORECARD.md`:
10 `| Capability |` rows and 2 `| Axis | Score (0–10) |` rows, each checked against what its own command
prints. The counter, contract, predicate (label `C1_R31_PASS`), target and kill rule were frozen at
`c111dab5` before any seat ran (`.ufo/evidence/round-31/contract.json`, `c1-measure.py`). C1 is sourced on
S055 (re-opened), S095 and S096 (new), through `corpus/knowledge/executable-self-assessment.md`.

- Repair first (round-30 spot-check routed items 1-6): the JudgeC1 "non-author" erratum is in the SCORECARD
  round-31 block, with QUALITY 66. The cold-read recipe now sets a per-seat `--workdir` and checks the cwd
  before any kill (`SKILL.md:1886`, QUALITY 67). The committed dead-seat check is
  `.ufo/evidence/round-31/dead-seat-check.py`: on the round-30 pair it flags ConnectorOverlap and exits 1,
  and it ran before wave 2 (`dead-seat-check-w2.txt`). Binding v4 became v5 before any data; the controls
  are in `.ufo/evidence/round-31/ctl/`. The `:60-62` cite and the stale `Next unused id: S092.` line are
  corrected append-only. The owner of `/tmp/tameshi-r4-2-regression.j0FKnk` is TameshiR30A3.ColdA08
  (`.ufo/waves/round-31/w1/RevengerStrayTmp.md`, agreed by `w2/ReviewStrayOwner.md`).
- Deferred with a reason: the runner's per-leg tally check and its 8 surviving guard mutants.
  `tools/mutate-and-run.sh` is an input of 270 of 456 ledger entries, so changing it would drift about 26
  credited sections (`w1/ReviewRoutedR30.md`). This re-defers round 30's route; it is routed to round 32.
- Pre-data control wave (wave 1, 32 seats). The do-nothing control reads `mismatches=7`, PASS false. Junk,
  label, deleted, hidden and rewrite controls all read false. Copying correct values from committed
  receipts reads true; the contract declared that route before data. CtlWrongHeader shape C
  (`| Axis | Score |`) reads true, which shows the code's header test is looser than the contract text; this
  is recorded as Mistake 5. Summary: `.ufo/evidence/round-31/ctl/c1-controls-summary.txt`.
- Content revision `2da841bd`: SCORECARD re-stated tables, S095-S096 added and S055 re-opened, the knowledge
  entry plus its README row, QUALITY 66-71, and the SKILL.md line. Wave 2 gave each of the 9 drifted
  sections three cold reads. All 24 entries were kept by v5, and the ledger grew 456 → 480 at `83c001a5`
  (`coldread/append-receipt-w2.json`).
- Falsifiers (wave 2): every row mutation turns its statement into a MISMATCH
  (`w2/MutateC1RowsA.md`, `w2/MutateC1RowsB.md`). The rows, entry, sources, census, QUALITY, binding,
  dead-seat check, ordering and no-harm were all reviewed. One `--regression` flip traced to a SIGPIPE race
  in tsukuroi's pinned suite (`w2/RegressionFlake.md`).
- Planner seat: held by the L1 (the validator rejects `planner`). Planning data walks went to scouts
  (ScoutStatements, ScoutFrontier).

## Gate

- **Reject: SrcDoctest's draft row for the doctest page.** It duplicates S055's URL (census E04 risk).
  S055 was re-opened instead.
- **Reject: SrcRustdoc's id S095.** It collides with the Go row; rustdoc became S096.
- **Reject: binding v4, before data.** CtlBindV4New kept 63/63 forged entries using five lexical shapes.
  v5 kills those 9 new shapes, the 7 old shapes and the 5 controls, and keeps 63/63 real round-30 entries
  (`ctl/README-bind-v5.txt`, `contract-addendum-1.json`).
- **Reject: "seven calibration errors" as the size of the gain.** CriticC1 and CriticC1After: 3 of the 7
  base mismatches were stale current statements (the round-17 line's 95/95, 7 legs, 56/56). The other 4
  were dated literals.
- Sources opened (URL, date, located quote): see `corpus/lessons/round-31.md` `## Gate`.

## Landed changes

| Commit | What | LOG |
|---|---|---|
| `c111dab5` | freeze: C1 counter, contract, binding v4, base receipts | LOG Round 31 |
| `ce1d7a64` | wave-1 spec and dispatch record | " |
| `87eb64eb` | wave-1 control receipts, binding v5, dead-seat check, wave-2 generator, addendum 1 | " |
| `2da841bd` | content revision (SCORECARD rows and erratum, SOURCES, entry, README, QUALITY 66-71, SKILL line) | " |
| `3351738a` | wave-2 spec, dispatch record, content monitor, overlap check | " |
| `83c001a5` | 24 bound cold reads appended to the ledger (the measurement revision) | " |
| `67c0e013` | measured-result row, lesson, LOG, wave-2 reports, after receipts | " |
| `08125328` | final-head receipts | " |

## Before → after measurements

C1, measured with `python3 .ufo/evidence/round-31/c1-measure.py --rev REV --work EMPTY_DIR`:

| Revision | Result | Receipt |
|---|---|---|
| base `36c1d393` | `C1_R31: statements=12 mismatches=7 unparsed=0 unobservable=0 append_only=1 … C1_R31_PASS=false`, exit 1 | `before/c1-at-base.stdout` |
| `83c001a5` (first full run) | `C1_R31: statements=12 mismatches=0 unparsed=0 unobservable=0 append_only=1 … C1_R31_PASS=true`, exit 0 | `after/c1-at-83c001a5.stdout` |
| `67c0e013` (last SCORECARD commit) | same line, exit 0 | `after/c1-at-final.stdout` |

No-harm checks, measured with `python3 .ufo/evidence/round-27/c1-measure.py --repo . --rev REV`:

| Revision | Result |
|---|---|
| base | covered 64/64, restraint 8 |
| content revision | 55/64, restraint 6 (by design, before the ledger append) |
| `83c001a5` and `67c0e013` | `covered=64/64 restraint=8 box3_mismatch=0 depth_score=9`, exit 0 |

Command D at `67c0e013`: `recorded_cases=9 depth_score=9`. Numeric scores: calibration 8 → 8, depth 9 → 9.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`:

- Start: 8 W04 warnings, `tameshi ok …/corpus/SOURCES.md`, exit 0 (`before/census-start.stdout`).
- End: the same 8 W04 warnings, `ok`, exit 0 (`after/census-end.stdout`).

Rows 92 → 94 (`git show REV:corpus/SOURCES.md | grep -c '^| S[0-9]'`). Added, tier A: S095 (Go testable
examples) and S096 (rustdoc documentation tests). Touched: S055 `used-by` went from
`corpus/lessons/round-16.md` to that path plus `corpus/knowledge/executable-self-assessment.md`. Frontier:
no F-row changes. The entry is new lane ground (ScoutFrontier) and cites kumitate's
`executable-scorecard.md` as adjacent prior art.

Mistake mined: 7 rows in the lesson `## Mistakes`, each with a fix shown able to fail.

## Trend verdicts

- **expansion: unprovable-but-better.** There is one new entry on ground the lane did not hold, with mined
  S095/S096. It is not a frontier move, and a sibling holds adjacent prior art.
- **quality: improved.** The standing rows now match their commands (7 → 0). The binding moved v4 → v5
  with pre-data receipts. QUALITY 66-71 were added. Calibration credit was restored to 64/64.
- **discernment: improved.** There are four real rejects, including v4 before data and the over-sized
  gain reading. Control results that went against the claim (receipt route, header C) are recorded, not
  hidden.

## SHONEN

- [~] SKILL.md contains real decision tables… — `SHONEN.md:5-6`, `reports/round-1-calibration.md#box-1`
- [~] At least one end-to-end domain task… — `SHONEN.md:7-8`; regression 9/9 PASS at `67c0e013` (`after/c1-at-final.stdout`)
- [~] Instructions executable without oral context — monitor 64/64 at `67c0e013` (`after/c1monitor-at-final.stdout`)
- [~] No cross-domain bleed — `SHONEN.md:11-12`; tsukuroi race reported, not absorbed (`w2/RegressionFlake.md`)

## Round shape and seats

The shape was two v1 waves under `ufo-wave-policy.json`. There was no residual call.

| Wave | Seats | Roles | Completed | Dead |
|---|---|---|---|---|
| Wave 1 | 32 | mutation-tester 10, executor 6, scribe 6, reviewer 3, critic 2, scout 2, revenger 1, connector 1, sentinel 1 | 32 | 0 |
| Wave 2 | 32 | reviewer 17, executor 4, mutation-tester 4, scout 3, critic 3, scribe 1 | 31 | 1 |

Round total: 64 seats.

Dead seat (hold): **CtlBindV5Fresh** (mutation-tester) stopped on the provider safety filter with
`Codex error event: This content was flagged for possible cybersecurity risk … (code=cyber_policy)`. It was
not retried or rerouted.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. Pacman paused; nothing installed.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no tameshi file. Nothing
  was moved.
- Inherited state: none.
- Open L0 questions: none.
