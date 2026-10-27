<!-- ORCHESTRATOR-OWNED run state (hyaku run 10). Not a misroot: lanes and seats never move, copy-then-delete, or edit this file. -->
# hyaku run 10 — 10-round blocks toward round 100 (2026-10-27)

Operator directive, verbatim (identical to run 9): "ok, let's continue the training rounds; i want you to do 10
rounds per shokunin, so we can keep consistency and not get messy with commits and dispatches; the goal is to reach
round 100 on each; choose the order you deem best to do so. | /skill:godspeed | we are on the hyaku mode, which seems
the one that works best; make sure to adapt to the 64-128 per round directive; max ceiling of 256 | use the same model
delegations we were using as before" (run start 2026-10-27 ~04:52 -03, right after run-9 wrap-up `5c8af59c`).

## Routing — the end-of-run-9 map, unchanged

`~/.omp/agent/config.yml:350-368` `task.agentModelOverrides` read at run start; no edit: task `@m_kfc`; main/planner
`@m_opus`; executor `@m_mim`; critic/scout/reviewer/mutation-tester `@m_kfc`; security-reviewer `@m_zfl`;
scribe/sonic/simplifier/revenger/labrat/sentinel `@m_flash`; connector `@m_antigravity`; distiller/seance `@m_haiku`.
L1s and closure judges spawn as `task` → `@m_kfc`.
Probe 2026-10-27T04:54:19-03:00 (`scripts/hyaku/probe-alias.sh`, receipts `/fast/scratch/hyaku-run10/probe/`), all
primary-ok: m_opus anthropic/claude-opus-5-5, m_kfc kimi-code/kimi-for-coding, m_mim minimax-code/MiniMax-M3.1-Flash,
m_flash opencode-go/deepseek-v4.1-flash, m_zfl zai/glm-5.3-flash, m_antigravity google-antigravity/gemini-3.8-flash,
m_haiku anthropic/claude-haiku-5-5.

## Host limits

omp 18.13.1 still caps a session at 100 running jobs. Kernel gates as run 9 ended: `HYAKU_SEAT_CEILING=96`,
`HYAKU_LOAD_MAX=120`, `MEM_MIN_GB` 4. `prlimit --fsize` 256 GiB soft cap applied to orchestrator omp pid 3047691
(SIGXFSZ ignored → oversized writes fail with EFBIG). Host at start: load 0.26, 24 GiB available, /tmp 3 %, /fast 24 %.

## Round shape

64–128 seats per round, 256 hard ceiling (lane-addendum §6 run-10 block, which keeps the run-9 band).

## Blocks and order (orchestrator choice)

Eight lane slots (run-9 operator ruling "use 8 slots, more concurrency"; same directive now). Each lane runs 10
consecutive rounds (dispatch → L1 lands → non-author closure → `advance` → next round), then yields its slot. A lane
that `advance` blocks or that fails three attempts of one round ends its block early; its slot goes to the next lane.

- Slots 1–3: the three claims left open at run-9 wrap-up resume first (in-flight state committed in-lane):
  **chousa** r57 (block r57–r66), **kake** r60 (r60–r69), **mado** r50 (r50–r59).
- Slots 4–8, lowest next round first: **souji** 34, **tabi** 36, **kasegi** 41, **kaidoku** 43, **tsukuroi** 47.
- Queue, in order: kengaku 48, tameshi 53, kama 55, mori 56, kumitate 68, revenger 71, kotoba 75, kotodama 75.
- Cycle 2 when the queue empties: lowest next round first again, 10-round blocks, until every lane reaches 100.

Why: the open claims carry committed in-flight state that a later re-dispatch would have to rebuild; after them,
lowest-first works the lanes with the most rounds left and keeps the fleet level.

## Holds / unblocks

- **Unblocked at run start** (streak blocks, run-8/9 precedent: a run-start directive to bring every lane to 100
  lifts them): souji, tabi, kasegi, kaidoku, tsukuroi, kengaku. Block files copied to
  `/fast/scratch/hyaku-run10/unblocked/`. Their first run-10 round is a fresh-start round (addendum run-10 block).
  If closures keep being rejected, `advance` re-blocks them.
- **kagi stays on HOLD** (operator content-safety HOLD, L0 `kagi | round-28`; not a streak).
- Open operator items carried from run 9: shokuknow `.qcache` restore (chousa capture counters), kama `ed135b3c`
  LOG-line ruling. Lanes route around them.

## Block ledger

| lane | slot | block rounds | closed (admitted / rejected) | state |
|---|---|---|---|---|

## Incidents
