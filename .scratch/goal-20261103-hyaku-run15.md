# hyaku run 15 — 2026-11-03 (Linux/omp host; continues zcode run 14)

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

## Start-state reconciliation

The zcode run-14 campaign (`.scratch/goal-20261031-hyaku-zcode-run14.md`, Windows host, 2026-10-31 to
2026-11-02) advanced every pool lane while this host sat on run-13 state. Reconciled 2026-11-03:
- Fleet repo: local run-15 setup commit rebased onto origin tip b73780ab; stale local commit
  "round-60: hyaku closure dispatch for tameshi" (tameshi r60 was already closed remotely) abandoned.
- Lane repos: all 17 fast-forwarded to their remote tips (all were ahead=0, behind 6-98). Dead run-13
  working-copy residue (tracked diffs + untracked strays) preserved under /tmp/run13-orphans/<lane>/.
- Local hyaku state rebuilt from MANIFEST closure rows: next = closed_max+1, outcome files per closed
  round; run-13 claims moved aside. kake r68 landed unclosed on zcode (report 9d56e80b) → claim
  reconstructed (base = r67 closure lane tip a6cb7efa), closed first.
- chousa r70-72 rejected on the Windows host (no flock, sibling load): streak lifted at run start,
  fresh-start rule applies to chousa r73.
- 574 lane-rounds remain at start: revenger 89, tsukuroi 64, kama 70, tameshi 72, tabi 56, mado 65,
  mori 79, souji 52, kaidoku 64, kake 68, kagi 30, kasegi 57, chousa 73, kengaku 63, kumitate 74,
  kotoba 85, kotodama 82 (next round per lane). Critical path: kagi (71 sequential rounds).

## Progress

State file: `.scratch/run15-state.json` (rounds trained this run, per-lane block progress).
