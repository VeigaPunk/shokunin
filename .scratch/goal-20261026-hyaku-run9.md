<!-- ORCHESTRATOR-OWNED run state (hyaku run 9). Not a misroot: lanes and seats never move, copy-then-delete, or edit this file. -->
# hyaku run 9 — 10-round blocks toward round 100 (2026-10-26)

Operator directive, verbatim: "ok, let's continue the training rounds; i want you to do 10 rounds per shokunin,
so we can keep consistency and not get messy with commits and dispatches; the goal is to reach round 100 on each;
choose the order you deem best to do so. | /skill:godspeed | we are on the hyaku mode, which seems the one that
works best; make sure to adapt to the 64-128 per round directive; max ceiling of 256 | use the same model
delegations we were using as before" (run start 2026-10-26 ~12:15 -03).

## Routing — run-8 map, unchanged

`~/.omp/agent/config.yml` `task.agentModelOverrides` re-read at run start (lines 350-368): task/main/planner
`@m_opus`; reviewer/mutation-tester/security-reviewer `@m_zfl`; scout `@m_sonnet`; distiller/seance `@m_haiku`;
connector `@m_kfc`; executor/labrat/scribe/sonic/simplifier/critic/revenger/sentinel `@m_flash`. No edit.
Probe 2026-10-26T12:22:54-03:00 (`scripts/hyaku/probe-alias.sh`, receipts `/fast/scratch/hyaku-run9/probe/`), all
primary-ok: m_opus anthropic/claude-opus-5-5, m_zfl zai/glm-5.3-flash, m_sonnet anthropic/claude-sonnet-5-5,
m_haiku anthropic/claude-haiku-5-5, m_kfc kimi-code/kimi-for-coding, m_flash opencode-go/deepseek-v4.1-flash.

## Host limits (measured at run start)

- omp 18.12.6 caps a session at 100 running jobs whatever `async.maxJobs` says (450 here): the bundled
  `~/.local/bin/omp.real` builds its job manager with `maxRunningJobs: () => Math.min(100, …)`, and `register()`
  throws `Background job limit reached (100)` when 100 non-queued jobs are running. Queued, completed and service
  entries do not count. This is the "live limit of 100" runs 7 and 8 observed.
- Host: 32 cores, 30 GiB RAM, booted ~12:09 -03 (uptime 9 min and load 0.28 at 12:17:59). Run 8 wedged it at
  ~92 live agents (load ~45).
- So 256 is a per-round seat ceiling (validator `maxLanes` 256), not a concurrency figure. The dispatcher now
  stops seat spawns at 88 running jobs (`SEAT_CEILING`), at 1-min load > 40 (`LOAD_MAX` = 1.25 × nproc) and at
  MemAvailable < 4 GiB (`MEM_MIN_GB`). A 128-seat wave fills in tranches.

## Round shape

64–128 seats per round, 256 hard ceiling (lane-addendum §6 run-9 block). One v2 wave (64–128) or two v1 waves
(32–64 each) summing to 64–128.

## Blocks and order (orchestrator choice)

Four lane slots. Each lane runs 10 consecutive rounds (dispatch → L1 lands → non-author closure → `advance` →
next round), then yields its slot to the next lane in the queue. Round 100 is a lane's last round, so a final
block may be shorter.

- Start: **tameshi** (r48 claim open: Phase 0 attempt 3 opens its block), **tabi** (32), **souji** (33,
  fresh-start), **kasegi** (36).
- Queue, in order: kaidoku (39), kengaku (40), tsukuroi (41), mado (44), kama (46), mori (51), chousa (52),
  kake (58), kumitate (66), revenger (71), kotoba (75), kotodama (75).
- Cycle 2 starts when the queue is empty: lowest next round first again, 10-round blocks, until every lane
  reaches 100.

Why: lowest-first works the lanes with the most rounds left and keeps the fleet level. Four slots roughly match
the seat capacity: past rounds took ~1–1.5 h at 64–71 seats with waves of 15–45 min, so 88 concurrent seats carry
about 2–3 rounds per hour. Run 8's six slots queued past that capacity and wedged the host. Kotodama goes last
on its tie with kotoba because of its open L0 questions (round-69, r74 frozen-claim conflict).

Block rules:
- A lane's next round is dispatched only after the previous round's closure row is in `MANIFEST.json` and
  `inline.sh advance` ran.
- A lane that `advance` blocks (three rejected closures in a row) or that fails three attempts of one round ends
  its block early. Its slot goes to the next lane; the short block is recorded below.

## Holds / unblocks

- **souji unblocked** at run start. Its block was a rejection streak (r30, r31, r32, `rounds[737,745,753]`), and a
  run-start directive to bring every lane to 100 lifts streak blocks (run-8 precedent: tabi, kaidoku, tsukuroi,
  revenger). Block file copied to `/fast/scratch/hyaku-run9/unblocked/souji`. Its first run-9 round is a
  fresh-start round (addendum run-8 rule). If closures keep being rejected, `advance` re-blocks it.
- **kagi stays on HOLD.** Its block is an operator content-safety HOLD waiting on a specific ruling (L0
  `kagi | round-28`, "Documentary close landed …"), not a rejection streak; runs 7 and 8 kept it held under equally
  broad directives.

## Phase 0

- tameshi r48: attempt 2 of 3 failed RETRYABLE in run 8 (claim open, base 473336d9d789). `inline.sh dispatch
  tameshi` runs attempt 3, the last before the lane is blocked.

## Block ledger

| lane | slot | block rounds | closed (admitted / rejected) | state |
|---|---|---|---|---|
| tameshi | 1 | r48–r57 | — | starting (r48 attempt 3) |
| tabi | 2 | r32–r41 | — | starting |
| souji | 3 | r33–r42 | — | starting (fresh-start) |
| kasegi | 4 | r36–r45 | — | starting |

## Incidents
