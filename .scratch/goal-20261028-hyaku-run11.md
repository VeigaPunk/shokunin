# hyaku run 11 — 2026-10-28

Operator directive (verbatim): "ok, let's continue the training rounds; i want you to do 10
rounds per shokunin, so we can keep consistency and not get messy with commits and
dispatches; the goal is to reach round 100 on each; choose the order you deem best to do so.
| /skill:godspeed | we are on the hyaku mode, which seems the one that works best; make sure
to adapt to the 64-128 per round directive; max ceiling of 256 | use the same model
delegations we were using as before | i want you to use m_flash for all roles; only use
m_grok for the scout role" — plus "m_flash on high effort" (alias already :high).

## Routing (never pass `model`)

Every role `@m_flash` except `scout` `@m_grok` — L1 seats, closures, and every wave role
(`task.agentModelOverrides` in `~/.omp/agent/config.yml`, applied at run-11 start).

## Round shape

64–128 seats per round, 256 hard ceiling. One v2 wave or two v1 waves; ≥25 % attack seats;
a few connector seats. File the report only after WAVE-DONE for every launched wave.

## Lane order

Lowest `next/` round first (queue order), resuming in-flight claims first. ~4 lanes live at
once (two 64–128 seat waves fill in tranches under the ~90-seat host cap; more L1s just
queue). Each lane runs its 10-round block, one steered round per dispatch, non-author
closure before the next dispatch.

| # | lane | run-11 start (next) | block target | notes |
|---|------|--------------------|--------------|-------|
| 1 | souji | 36 | 45 | fresh-start: three rejected closures r33–35 |
| 2 | kasegi | 42 | 51 | resume claim attempt 3 (a2 died mid-wave; w2.ready artifact removed) |
| 3 | tabi | 42 | 51 | fresh-start: three rejected closures r39–41 |
| 4 | kaidoku | 44 | 53 | resume claim attempt 2 |
| 5 | tsukuroi | 49 | 58 | |
| 6 | kengaku | 50 | 59 | |
| 7 | tameshi | 54 | 63 | resume claim attempt 2 |
| 8 | mado | 55 | 64 | |
| 9 | mori | 60 | 69 | fresh-start: three rejected closures r57–59 |
| 10 | chousa | 61 | 70 | |
| 11 | kama | 63 | 72 | |
| 12 | kake | 64 | 73 | |
| 13 | kumitate | 69 | 78 | |
| 14 | revenger | 73 | 82 | |
| 15 | kotodama | 79 | 88 | |
| 16 | kotoba | 82 | 91 | |

## Holds

- **kagi (next 29)** — operator HOLD stands: 2026-10-21 content-safety refusal; open L0
  question `kagi | round-28` on whether the HOLD stays and the open C1 fail-open ruling.
  Not dispatched this run.
- protocol/aggregator — fleet meta-lanes, not in the pool (closures stand in for protocol).
- audio, game-dev-2d, game-dev-3d, lore — already ≥100 (101, 105, 108, 103 reports).

## Fresh-start rule

souji, tabi, mori: first run-11 round reads the last three rejected closures and
spot-checks first; declares only claims a do-nothing control cannot reach (addendum §9).

## Run-start repairs (operator)

- kasegi r42: stale `w2.ready` deleted + committed via jj-lane.sh — it pointed at a spec
  file (no `taskCall`) and crash-looped the dispatcher's register() (`KeyError taskCall`,
  09:14–09:57). The new attempt-3 L1 inherits round-42 work under the lane repo.
- revenger r72 `.partial`: tracked wave residue; `.dispatched` exists so the dispatcher
  never re-registers it. Left in place (wave evidence).
- mori/souji/tabi `blocked/` files removed (streak blocks, lifted per run-start directive).
