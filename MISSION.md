# Shokunin Fleet Mission — Source of Truth

This file is the mission instruction every L1 lane is bound to. Changes here
persist into `scripts/shokunin-watchdog.sh` prompt generation and are relayed
to live lanes by steer.

## Fleet shape

- 8 L1 lanes in `ufo_sighting:shokunin`: protocol, kasegi, kengaku, kake,
  kumitate, kotoba, kagi (all `@m_swe`), aggregator (`@m_qwen`).
- Self-iteration by **respawn-per-round**: a lane's round ends when its
  report lands at `.ufo/reports/round-<N>/<lane>.md`; the watchdog completes
  the mission and launches a fresh process for round N+1. Cap: 1024/lane.

## L2 concurrency — required

Every L1 lane MUST dispatch **at least 8 L2 task subagents per round**, batched
into a single `task` tool call (parallel lanes, not sequential turns). Suggested
splits:

- domain lanes: per-surface scouts, executors drafting SKILL.md sections,
  critic falsifying claims, connector for sibling overlap, reviewer for
  citation verification;
- aggregator: one lane per child repo + cross-cutting seats;
- protocol: per-repo scouts + critic + connector + reviewer.

## L2 route bucket (fixed)

| Role class | Model |
|---|---|
| planner, connector | `@m_lunamax` |
| executor, scribe, scout | `@m_flash` |
| reviewer, critic, sentinel, revenger, labrat, mutation-tester, simplifier, distiller | `@m_zfl` |

Persisted in `~/.omp/agent/config.yml` `task.agentModelOverrides` (global) and
`/tmp/fleet-override.yml` (fleet-local). Do not route L2s outside this bucket.

## Round end

Commit inside the owning repo then `git push`. Reports land in the main repo
under `.ufo/reports/round-<N>/` — commit and push those too.
