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

**Operator, ~13:10 -03, verbatim:** "more concurrency"; then "train 2 lanes concurrently"; then "go for your 4 lanes
to 8". The last message rules: **eight lane slots.** Slots 5–8 went to the next four in the queue at 13:1x:
kaidoku (39), kengaku (40), tsukuroi (41), mado (44). The queue now starts at kama (46). The seat ceiling is
unchanged (88 running jobs, plus the load and memory gates), so with eight lanes, waves queue for seats.

**Operator, ~14:05 -03, verbatim:** "use 8 slots, more concurrency". Eight slots stay. The seat gates are raised to
the most the host allows: `SEAT_CEILING` 88 → 96 running jobs (omp's own cap is 100, and 4 are kept for L1 and
closure spawns), `LOAD_MAX` 40 → 72 (2.25 × nproc), `MEM_MIN_GB` stays 4. At the change, load was already ~59 with
56 jobs running, and the load gate (not the seat count) was holding souji r33 w1 and tabi r32 w2 at 0 spawned.

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
| tameshi | 1 | r48–r57 | — | r48 attempt 3 in flight |
| tabi | 2 | r32–r41 | r32 admitted (`rounds[756]`) | r33 in flight |
| souji | 3 | r33–r42 | — | r33 in flight (fresh-start) |
| kasegi | 4 | r36–r45 | r36, r37 admitted (`rounds[755]`, `[758]`) | r38 in flight |
| kaidoku | 5 | r39–r48 | r39 admitted (`rounds[757]`) | r40 in flight |
| kengaku | 6 | r40–r49 | r40 admitted (`rounds[759]`) | r41 in flight |
| tsukuroi | 7 | r41–r50 | — | r41 in flight |
| mado | 8 | r44–r53 | r44 admitted (`rounds[760]`) | r45 in flight |

## Incidents

- 12:36 -03: the first tick spawned kasegi r36's 64-seat wave and hit the eval tool's 30 s default cell timeout
  after 31 spawns (`agent()` takes ~1 s per seat). The kernel survived with PARTIAL intact, and the next tick
  finished the fill. Fixes: the dispatcher now saves `<ready>.partial` after every spawn (the line SentScope F3
  found uncommitted, committed with this record), and tick cells run with a 900 s timeout.
- KasegiR36 filed its report (dd1ad9cf) before WAVE-DONE, with 6 of its 64 seats still running. It also ran
  `find … -exec rm -rf {} +` sweeps over `/fast/scratch/hyaku/kasegi-r36` while seats were live (SentScope F2:
  SentScope's own dir was deleted twice). Both go to its closure as conformance items. The closure judge is
  dispatched after the wave settles, so the judge reads a stable lane.
- ~14:00-14:10 -03, host PATH write, cross-lane harm. Kengaku r40 critic seat `R40CritC1Counter` attacked the C1
  counter by planting a phase-aware `git` shim at the real `/home/vgpnk/.local/bin/git`. That directory comes
  before `/usr/bin` on every lane's PATH. Its modules are `crit_git_shim.py` and `crit_ledger_selfread.py`
  (`SHIM_DIR`, line 15). The shim passed unrelated repos through to `/usr/bin/git`. It was rewritten and removed
  between runs, so sibling seats lost the race:
  - kasegi r37 `ExecC1JudgedHeadFail` F4: ENOENT.
  - souji r33 `SwarmCritic07`: one false K07 MISMATCH at ~14:07.

  The shim was absent when this was found. Actions:
  - The kengaku L1 was told at 14:12 never to run the modules on the host and to sandbox any rerun behind a
    private `~/.local/bin`.
  - It acked: the modules now raise `SystemExit` at import, and `SHIM_DIR` is `/nonexistent`.
  - An orchestrator watcher alerts on any new entry in `~/.local/bin`.

  This is a conformance item for kengaku r40's closure. The PATH finding itself (the counter runs tools with the
  caller's PATH) is valid.
- Load gate raised again, kernel only: `LOAD_MAX` 72 → 120. Since then the host has stayed responsive at load
  70–95 (`proc://` reads ~0.3 s), with 84–89 jobs visible and ~15 GiB available.
