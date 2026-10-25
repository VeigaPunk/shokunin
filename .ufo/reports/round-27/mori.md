# mori — round 27 report (attempt 1, L1 MoriR27)

Lane tip (pushed): `df886be1cc75f1052002698bdb4a3d18a2eaf6c6` (`jj-lane.sh state`: local = remote, ahead 0).
Entering tip: `fc09f96c8036094bef06370dbb4b436edf96e6e3`. Contract: `.ufo/waves/round-27/contract.md` (landed
`761b4cdb`; amendment W1 `dd4dbb20`).

## Work performed

Declared claims: **C1 — depth (score 5, tied lowest):** a sourced knowledge entry on FR10 "fleet attribution of a
victim": how earlyoom 1.9.0 and the Linux 7.2 kernel choose an OOM victim and where the fleet stands in that ranking.
**C2 — operability:** freeze cases for the round-26 tool's ten amendment-A2 rules (routed D7). **C2 was withdrawn
before any data** (amendment W1): its case-writer seat died at spawn, and dead seats are never replaced. One counted
claim. No new tool (orchestrator drift watch).

- Counters committed before data: `.ufo/waves/round-27/count-c1.sh`, `count-c2.sh`; before receipts
  `evidence/c1-before.txt`, `c2-before.txt` (`761b4cdb`).
- New entry `corpus/knowledge/oom-victim-selection-r27.md`: earlyoom picks the highest `oom_score` it computes (±300
  for prefer/avoid name matches, size only under `--sort-by-rss`); the kernel exports `(1000 + badness*1000/totalpages)
  * 2/3` and scales `oom_score_adj` by memory size; the fleet's 200 comes from systemd's per-user manager (100 + 100,
  `src/core/main.c:3063`), not the harness (whole-tree negative over oh-my-pi v18.12.6 and Bun 1.4.3); task seats run
  in-process in the session's `omp` process (S142); in boot -1 earlyoom sent 39 lines (python 27, other 11, omp 1),
  8 above the kernel ceiling for their adjustment (prefer-matched, under stated conditions); no fleet record names a
  kill cause (`126e192d`, then wave-2 corrections through `df886be1`).
- Host captures (aggregates only): `evidence/oom-score-classes.{py,txt}`, `evidence/boot-send-classes.{py,txt}`.
- SKILL.md `## Round27 — OOM victim selection` table (8 decision rows, 3 error patterns); README index row and FR10
  row; PROVINCE round-27 note (`5e500d99`).
- Routed r26 D1 (four late wave-2 reports committed, tally corrected), D2 (S117 description, new S137), D3 (S124
  restored, S133 supersedes), D4 (oomd xattrs wording plus O2, O14, O17), D5 (README range) fixed; D6 explained; D7
  debt (C2 withdrawn). r25 R3 (SKILL rows, S134–S136) and R7 (S138–S141, two entries) fixed; R1 and R5 debt (code,
  executor route down). Disposition table: `corpus/lessons/round-27.md`.
- New check `.ufo/waves/round-27/check-row-identity.py` (QUALITY 81) found five more rows edited in place in rounds
  24–25; S090 and S093 restored with S143, S144; S096, S097, S101 carried.
- A harness settings value was withheld from four lines of `harness-job-capacity-r25.md` (pre-existing; not added).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| contract, counters, before receipts, declaration | round 27 declaration | `761b4cdb` |
| wave-1 spec, run, dispatch | declaration | `5fa0a00f` |
| amendment W1, README D5 | declaration | `dd4dbb20` |
| C1 entry, S127–S132, SKILL table, evidence, wave-1 reports, r26 late w2 reports (D1) | outcome | `126e192d` |
| D2–D4, R3, S133–S137, lesson, QUALITY 80–82, row-identity check | outcome | `79ecf58b` |
| R7, S138–S141 | outcome | `5f00fd04` |
| wave-2 spec; measured outcome | outcome | `0becc421`, `b97b2e3f` |
| wave-2 corrections, S142, hardened check, index rows, S143–S144, LOG outcome | outcome | `b89ac342`, `47f6543a`, `5e500d99`, `9c2c7de9`, `df886be1` |

## Before → after measurements

| Claim | Command | Before (`fc09f96c`) | After |
|---|---|---|---|
| C1 | `bash .ufo/waves/round-27/count-c1.sh <rev>` | `entry=absent new_rows_cited=0 skill_rows=0`, `C1=unmet`, exit 1 | at `df886be1`: `entry=present new_rows_cited=7 skill_rows=11`, `C1=met`, exit 0 (`evidence/c1-after.txt` holds the `0becc421` run: 6 / 10, met) |
| C2 | `bash .ufo/waves/round-27/count-c2.sh <rev>` | `a2_cases=0 a2_rules_covered=0/10`, `C2=unmet`, exit 1 | withdrawn (W1); not measured |

No-harm: retention scan (`tools/mori-retention-gate.py scan … --policy .ufo/waves/round-18/frozen/c1-policy.json`)
metric 4 at the entering tip and before every landed batch (pre-commit sandbox scans); wave-2 ReviewPrivacyLanded
read 4 at `5f00fd04`. `tools/` unchanged (wave-2 CriticC1Admission: tallies 32/32, 21/21, 12/12, census 134).
The counter checks shape only; the substance was attacked by wave 2 (below).

## Sources & frontier

Census `scripts/sources-census.sh validate --root <fleet> mori`: start exit 0 (six pre-existing W04: S035, S037,
S073–S076); end exit 0, same six warnings. Rows 126 → 144 (`check-row-identity.py` `rows=144`). Added, all tier A,
`mined`: S127–S132, S142 (C1), S133 (supersedes S124), S134–S136 (R3), S137 (D2), S138–S141 (R7), S143 (supersedes
S090), S144 (supersedes S093). Touched old → new (logged in the lesson): used-by on S003, S082, S092, S114, S115,
S118, S119, S120; S124, S090, S093 restored to first-published cells. Frontier: FR10 advanced (victim selection to
Core knowledge); remaining FR10 items listed in `PROVINCE.md` round-27 note. Mistakes mined: M1–M4 (lesson), with
QUALITY 80–82 shown able to fail. Sourced claim: C1 rests on S127–S132, S142, all opened this round.

## Trend verdicts

- **expansion: improved** — new FR10 ground (victim selection, fleet's adjustment origin, send classes), 18 new
  rows, SKILL decision table.
- **quality: improved** — r26 entry corrections (D2, D4), R7 corrections, four rows restored to first-published text,
  wave-2 corrections applied before landing (tie rule, omp process count, overclaims). Known row-level defects in
  S127, S128, S129, S131 are carried, not hidden.
- **discernment: improved** — a new check found five unlogged in-place row edits; wave-2 critics overturned three
  entry statements and they were fixed; outside verification is the closure's.

## SHONEN

- [ ] decision tables (not verified by a non-author)
- [~] end-to-end task logged — `LOG.md` round-27 outcome; `evidence/boot-send-classes.txt`
- [ ] executable without oral context
- [~] no cross-domain bleed — entry Adjacency paragraph; `PROVINCE.md` round-27 note

## Round shape, seats, installs, other

- Shape: default, two v1 waves, both validated. Wave 1 build 34 seats (14 scout, 6 reviewer, 5 critic, 3 executor,
  3 scribe, 2 connector, 1 mutation-tester): 27 returned; **7 dead at spawn (20.6%, over 20%)**, each with
  `Error: No model selected.`: DraftSkillTable, DraftEntryR27, DraftLessonMistakes (scribe), WriteA2Cases,
  HostBootSendClasses, HostOomScoreClasses (executor), MutCounters (mutation-tester). Their work was done by the L1
  (entry, SKILL table, lesson, both captures) or withdrawn (C2). Wave 2 falsify 41 seats (32 reviewer, 7 critic,
  1 scout, 1 connector): 19 returned; 22 cancelled at the run budget, of which ReopenS133, ReopenS135, ReopenS136,
  ReopenS137, ReviewEntryFact1 and ReviewHygieneD2 left files, committed as partial reports in `df886be1`. Round total
  75 seats; attack seats 51 (68%). No residual call. Planner seat held by the L1. The validator rejects `labrat`, so
  the wave-1 inheritance probe ran as critic `CriticInheritProbe` (validator, not route). `solutionSpace` strings were
  added to both validated payloads; nothing else changed.
- Seat gate: wave 2's acquire waited about 50 minutes (phantom seats of the dead route; Main compensated the cap).
- Misroot: wave-2 ScoutMisroot found seven fleet-root files (`base.c`, `oom_kill.c`, `MANPAGE.md`, `main.c`,
  `meminfo.c`, `sd-main.c`, `user@.service.in`) byte-identical to round-27 scratch captures of public upstream
  sources; their content does not name mori or this round and the writer is unknown, so they were left untouched.
- Installs: none.
- Open L0 questions: none new; the history disposition of older lines carrying uid digits (358 lines in 118 files)
  and a harness settings value stays with the operator's open question.
- Stale-lane: respawn-per-round driver; no other mori mission is open.
