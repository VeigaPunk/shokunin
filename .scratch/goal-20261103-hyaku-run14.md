# hyaku run 14 — 2026-11-03

Operator directive (verbatim): "ok i need you to continue the hyaku run, we will be using 32-40
concurrent workers, you are the orchestrator of each run; i want you to do 10 rounds of training per
shokunin, until each reeach 100 completed rounds. our subagents for the swarms rounds (each round, a
wave composed of m_flash, m_mim, m_zfl on roles you assign) on the hyaku style but using these models
and conc i've assigned; remember, the essence of the shokunin runs is to learn by doing, to activelky
get better and more capable, to have curated source of knowledge (corpus and their own trials)".
Interjection: "you will be running until each shokunin reaches round 100".

## Campaign shape

- **Goal: every pool lane reaches round 100** (17 lanes, 706 lane-rounds remaining at start).
  10-round blocks per lane; a lane holds its slot for its whole block, then the slot goes to the
  lowest-`next/` lane (`inline.sh queue` order) — the long-pole lanes (kagi r29, tabi r44, souji r46)
  stay live continuously.
- **Concurrency 32–40 workers total**: ~6 L1 lanes live at once; dispatcher `SEAT_CEILING=36`
  (seat spawns stop at 36 running jobs); L1/closure spawns only while running jobs < 40; closures
  may use ≤3 helper seats.
- **Round size: ONE v1 wave of 8–16 seats** (`ufo-wave-policy.json` band 8–16; residual ≤4;
  ≥25 % attack seats; ≤2 connector seats).
- Hyaku in-session inline mode unchanged (inline.sh + inline-dispatcher.py, jj lanes, fleet-commit.sh,
  fresh non-author closures, append-closure.py the only MANIFEST writer).

## Routing (never pass `model`; backup `~/.omp/agent/config.yml.pre-run14-20261103`)

| roles | model |
|---|---|
| task (L1 + closure judges), main, planner, reviewer, security-reviewer, critic | @m_zfl |
| executor, revenger, scout, labrat, mutation-tester, simplifier | @m_flash |
| connector, sentinel, scribe, sonic, distiller, seance | @m_mim |

## Start-state reconciliation (run-13 session ended 2026-10-30 with 14 L1s mid-flight)

- tameshi r60: report landed + committed (96eede2f), verified OK → closure first.
- 13 dead L1s (chousa r66, kagi r29, kaidoku r53, kake r65, kama r65, kasegi r50, kengaku r56,
  mado r57, mori r62, revenger r74, souji r46, tabi r44, tsukuroi r53): attempt 1 recorded failed
  (`inline.sh fail`); re-dispatch is attempt 2 and inherits the lane working copy.
- Orphan undispatched readies of dead attempts renamed `*.ready.run13-orphan` (kagi r29, kasegi r50,
  revenger r74, souji r45/r46) so `live()`'s attempt-suffix match cannot revive them for a new
  `<Lane>R<n>a2` L1 (revenger L0 r73 hazard). Tracked readies of closed rounds left untouched.
- Holds: none (operator 2026-10-30 lifted kagi HOLD and mado SECURITY HOLD).

## Progress

State file: `.scratch/run14-state.json` (rounds trained this run, per-lane block progress).
