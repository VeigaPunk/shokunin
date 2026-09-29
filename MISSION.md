# Shokunin Fleet Mission — Source of Truth (fleet-2)

Binding mission instruction for every L1 lane. Changes persist into
`scripts/shokunin-watchdog.sh` prompt generation and are relayed to live lanes
by steer.

## Fleet shape (9 L1 lanes)

| Lane | Repo/cwd | Model | Axes owned |
|---|---|---|---|
| protocol | `~/Projects/shokunin` | `@m_swe` | fleet-meta: protocol soundness, gate integrity |
| aggregator | `~/Projects/shokunin` | `@m_swe` | cross-lane quality, mint/dormancy calls, corpus review |
| kasegi | `kasegi-shokunin/` | `@m_swe` | depth + coverage (bounty/security research) |
| kengaku | `kengaku-shokunin/` | `@m_swe` | novelty + calibration (LLM eval/research) |
| kake | `kake-shokunin/` | `@m_swe` | operability + freshness (web properties) |
| kumitate | `kumitate-shokunin/` | `@m_swe` | operability + coverage (orchestration/tooling) |
| kotoba | `kotoba-shokunin/` | `@m_swe` | depth + consistency (prompt/skill craft) |
| kagi | `kagi-shokunin/` | `@m_swe` | freshness + calibration (secrets/vault ops) |
| kama | `kama-shokunin/` | `@m_swe` | operability + freshness (local model serving/endpoints) |

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
| reviewer, critic, sentinel, revenger, labrat, mutation-tester, simplifier, distiller | `@m_zfl` (fallback `@m_flash`) |

## Round end

Commit inside the owning repo then `git push`. Reports: `.ufo/reports/round-<N>/<lane>.md` on the main repo, commit + push.

## Push scope — hard rule

Lanes push ONLY to `VeigaPunk/shokunin` (main repo) or their own
`VeigaPunk/<lane>-shokunin` remote. Domain source trees (e.g.
`~/Projects/origin-work/ufo-fsd-alpha`, `~/Projects/bounties`,
`~/Projects/webzites`) are read-only surfaces: never commit there, never
push to their remotes. Work that belongs upstream is documented in the lane
report; the operator owns those pushes.

## L0 side channel

The operator is reachable via `.ufo/l0-questions.md` in this repo: append a
line `<lane> | round-<N> | <question or decision needed>`. The aggregator lane
surfaces entries each round; the L0 answers by editing the file in place.
