<!-- ORCHESTRATOR-OWNED run state (hyaku run 7). Not a misroot: lanes and seats never move, copy-then-delete, or edit this file. -->
# hyaku run 7 — inline swarm rounds toward round 100 (2026-10-25)

Operator directive, verbatim: "ok let's go back to training the shokunins, following that meethod of
doing swarms inline for each round, and pushing towards round 100 on each shokunin that hasn't gotten
to that threshold; we should assimilate the 'considerthese' in their repos, and also the shokuknow
dirs on their given shokunins that match the contents; do it with high parallelization; this will be
hyaku 7th run; choose the shokunin orders. for delegations, i want a mix of m_zfl, m_flash, m_kcode,
m_mim, m_glm53 | delegate accordingly. | i want the swarm rounds to be of 64-100 subagents per
shokunin;" — interjections: "use more m_flash"; "oh, its m_kfc; my bad, not m_kcode"; "also, include
m_antigravity as the connector" (probe: google-antigravity/gemini-3.8-flash primary-ok).

## Routing (global role map, `~/.omp/agent/config.yml`; backup `config.yml.pre-run7-20261025`)

Probe 2026-10-25 (`scripts/hyaku/probe-alias.sh`): all five primaries answered (m_zfl→zai/glm-5.3-flash,
m_flash→commandcode/deepseek-v4.1-flash, m_kfc→kimi-code/kimi-for-coding, m_mim→minimax-code/MiniMax-M3.1-Flash,
m_glm53→zai/glm-5.3).

| roles | alias |
|---|---|
| task, main, planner (L1s, closure judges) | @m_kfc |
| critic, revenger, sentinel | @m_glm53 |
| scout, distiller, seance | @m_mim |
| reviewer, mutation-tester, security-reviewer | @m_zfl |
| connector | @m_antigravity |
| executor, labrat, scribe, sonic, simplifier | @m_flash (≥50% of each wave's seats) |

## Round shape

64–100 seats per round: one v2 wave (64–100) or two v1 waves summing 64–100. Addendum §6 run-7 block.

## Assimilation

Every round: one `merge/<lane>/` theme matching PROVINCE (addendum §10 contract) and/or one
`considerthese/` proposal. Lanes without considerthese: tabi, souji, kaidoku, kotodama.

## Lane order (orchestrator choice)

4 concurrent lane slots (each ≤100 seats → ≤400 + L1s + closures under async.maxJobs 450).
A lane runs 3 consecutive rounds, then yields its slot to the next lane in this order:

1. souji (26), tabi (27), kasegi (28), kengaku (33) — furthest behind
2. kaidoku (35), tsukuroi (37), mado (39), kama (40)
3. tameshi (45), mori (47), chousa (49), kake (55)
4. kumitate (63), revenger (70), kotoba (72), kotodama (73)

Then repeat from the lowest next-round.

## Blocks / holds

- Unblocked at run start (operator directive covers every lane below 100): kaidoku, tsukuroi,
  kumitate, revenger. Each first run-7 round is a **fresh-start round**: read the last three
  rejected closures + spot-checks, and declare claims a do-nothing control cannot reach (addendum §9);
  open L0 questions are routed around, never assumed answered.
- kagi stays HOLD: operator ruling on L0 `kagi | round-28` (content-safety refusal) not given.

## Incidents
