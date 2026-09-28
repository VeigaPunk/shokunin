# Shokunin Fleet Mission — Source of Truth (fleet-2)

Binding mission instruction for every L1 lane. Changes persist into
`scripts/shokunin-watchdog.sh` prompt generation and are relayed to live lanes
by steer.

## Fleet shape (8 L1 lanes)

| Lane | Repo/cwd | Model | Axes owned |
|---|---|---|---|
| protocol | `~/projects/shokunin` | `@m_qwen` | fleet-meta: protocol soundness, gate integrity |
| aggregator | `~/projects/shokunin` | `@m_qwen` | cross-lane quality, mint/dormancy calls, corpus review |
| kasegi | `kasegi-shokunin/` | `@m_qwen` | depth + coverage (bounty/security research) |
| kengaku | `kengaku-shokunin/` | `@m_qwen` | novelty + calibration (LLM eval/research) |
| kake | `kake-shokunin/` | `@m_z53` | operability + freshness (web properties) |
| kumitate | `kumitate-shokunin/` | `@m_flash` | operability + coverage (orchestration/tooling) |
| kotoba | `kotoba-shokunin/` | `@m_flash` | depth + consistency (prompt/skill craft) |
| kagi | `kagi-shokunin/` | `@m_flash` | freshness + calibration (secrets/vault ops) |

Round-robin across lanes; `respawn-per-round`: a round ends when
`.ufo/reports/round-<N>/<lane>.md` lands; watchdog completes the mission and
launches a fresh process for round N+1. Cap: 1024/lane. Tick: 450s.

## The axes framework

`AXES.md` defines the six expertise axes (depth, coverage, operability,
freshness, calibration, adjacency). A lane's round is **one axis-move**: pick
the lowest-scoring axis in `SCORECARD.md`, land one verifiable improvement,
measure it, record before→after in `SCORECARD.md`, log evidence in `LOG.md`.
Axes may be retired on saturation or split into sub-axes — recorded in
`SCORECARD.md` with the reason. Axis assignments above are initial; lanes may
add/remove axes on evidence (falsifiable claim per move).

## L2 concurrency — required

Every L1 lane MUST dispatch **at least 8 L2 task subagents per round**, one
batched `task` call. Route bucket (persisted globally + `/tmp/fleet-override.yml`):

| Role class | Model |
|---|---|
| planner, connector | `@m_lunamax` |
| executor, scribe, scout | `@m_flash` |
| reviewer, critic, sentinel, revenger, labrat, mutation-tester, simplifier, distiller | `@m_zfl` |

## Round end

Commit inside the owning repo then `git push`. Reports: `.ufo/reports/round-<N>/<lane>.md` on the main repo, commit + push.

## L0 side channel

The operator is reachable via `.ufo/l0-questions.md` in this repo: append a
line `<lane> | round-<N> | <question or decision needed>`. The aggregator lane
surfaces entries each round; the L0 answers by editing the file in place.
