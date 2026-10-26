<!-- ORCHESTRATOR-OWNED run state (hyaku run 9). Not a misroot: lanes and seats never move, copy-then-delete, or edit this file. -->
# hyaku run 9 — 10-round blocks toward round 100 (2026-10-26)

Operator directive, verbatim: "ok, let's continue the training rounds; i want you to do 10 rounds per shokunin,
so we can keep consistency and not get messy with commits and dispatches; the goal is to reach round 100 on each;
choose the order you deem best to do so. | /skill:godspeed | we are on the hyaku mode, which seems the one that
works best; make sure to adapt to the 64-128 per round directive; max ceiling of 256 | use the same model
delegations we were using as before" (run start 2026-10-26 ~12:15 -03).

## Routing — run-8 map; critic → `@m_glm53` ~18:05, → `@m_kfc` ~18:20 -03

`~/.omp/agent/config.yml` `task.agentModelOverrides` re-read at run start (lines 350-368): task/main/planner
`@m_opus`; reviewer/mutation-tester/security-reviewer `@m_zfl`; scout `@m_sonnet`; distiller/seance `@m_haiku`;
connector `@m_kfc`; executor/labrat/scribe/sonic/simplifier/critic/revenger/sentinel `@m_flash`. No edit.
Probe 2026-10-26T12:22:54-03:00 (`scripts/hyaku/probe-alias.sh`, receipts `/fast/scratch/hyaku-run9/probe/`), all
primary-ok: m_opus anthropic/claude-opus-5-5, m_zfl zai/glm-5.3-flash, m_sonnet anthropic/claude-sonnet-5-5,
m_haiku anthropic/claude-haiku-5-5, m_kfc kimi-code/kimi-for-coding, m_flash opencode-go/deepseek-v4.1-flash.

**Operator, ~16:38 -03, verbatim:** "can you make it so m_kfc fallback chain is actually the kimi-for-coding primary
and m_swe as secondary fallback?" Done in `~/.omp/agent/config.yml:428-431`: `retry.fallbackChains.m_kfc` is now
`["@m_swe", inception/mercury-3:max, openai-codex/gpt-6-luna:low]`; the primary `modelRoles.m_kfc`
(kimi-code/kimi-for-coding:max) is unchanged. `cfg://retry/fallbackChains` shows the new chain live. It applies to
connector seats spawned after the edit.

**17:45 -03, chain wipe (not this session).** The operator's separate omp session "FLBK" (session file
`~/.omp/agent/sessions/-tmp/2026-10-26T20-42-29-908Z_01a179f3-….jsonl`) was asked to set
`m_glm53 → zai/glm-5.3:max, then m_swe, then openai-codex/gpt-6-luna:low`. It wrote `{}` to
`cfg://retry/fallbackChains/save` twice (20:45:21Z, 20:45:40Z) and so cleared every fallback chain in
the global config. It said so in its own reply. `config.yml` mtime 17:45:21 matches.

**Operator, ~18:05 -03, verbatim:** "insert some m_glm53 on a suitting m_flash role". Done in
`~/.omp/agent/config.yml` (backup `config.yml.pre-glm53critic-20261026`):
- `task.agentModelOverrides.critic` is now `"@m_glm53"` (`zai/glm-5.3:max`).
- Why critic: it is the m_flash role whose job is adversarial falsification. It is about a quarter of each wave's
  seats. With executors on DeepSeek flash and critics on GLM, the attacker and the builder are different model
  families.
- `retry.fallbackChains` is restored from that session's own pre-wipe read (20:44:51Z, 26 chains, including
  this run's m_kfc chain). The one change is the m_glm53 chain the operator asked for there:
  `["@m_swe", openai-codex/gpt-6-luna:low]`.
- `cfg://task/agentModelOverrides` and `cfg://retry/fallbackChains` show both changes live.
- Critic seats spawned after the edit route to GLM. Seats already running keep the chain they captured at spawn.
- Observed: the 11 tameshi r49 w2 critic seats spawned at 20:55Z answered on `zai/glm-5.3`. Critic seats from
  20:47Z answered on `opencode-go/deepseek-v4.1-flash`. Source: the first `model_change` in each seat's session file.

**Operator, ~18:20 -03, verbatim:** "ok swap the m_glm53 for the m_kfc". Read as: replace m_glm53 with m_kfc on the
critic role. `task.agentModelOverrides.critic` is now `"@m_kfc"` (kimi-code/kimi-for-coding:max, chain `@m_swe` →
mercury → luna). Connector stays `@m_kfc`. No role uses m_glm53 now. Its chain stays as the operator set it.
`cfg://task/agentModelOverrides` shows `critic: "@m_kfc"` live.

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
| tameshi | 1 | r48–r57 | r48 rejected-harmed (`rounds[765]`, `d98fe66c`; cold-read 60 → 57 below its floor), r49 admitted (`rounds[772]`, `fa882d7d`; calibration 6 → 8, coverage F10 held; spot-check `e3729de8`) | r50 in flight (TameshiR50, 18:31) |
| tabi | 2 | r32–r41 | r32 admitted (`rounds[756]`), r33 rejected-honest-stop (`[763]`), r34 rejected-honest-stop (`[769]`, `e9949eaf`; C1 newMapped 1/3, C2 met 20/20; operability improved, nothing harmed) | r35 in flight (TabiR35, ~17:58) |
| souji | 3 | r33 | r33 rejected-honest-stop (`rounds[764]`) | **blocked** 16:39 by `advance` (three consecutive rejected closures through r33); block ended early at 1 round, slot 3 → kama |
| kama | 3 | r46–r55 | r46 admitted (`rounds[770]`, `a4a605eb`; C1 freshness and C2 calibration improved, nothing harmed) | r47 in flight (KamaR47, ~18:30) |
| kasegi | 4 | r36–r45 | r36, r37 admitted (`rounds[755]`, `[758]`), r38 rejected-honest-stop (`[762]`), r39 rejected-honest-stop (`[771]`, `13277204`; attempt 2 after attempt 1 hit the request budget; C1 not verified (G2 red, 7/8), C2 verified; expansion improved) | r40 in flight (KasegiR40, ~18:40) |
| kaidoku | 5 | r39–r48 | r39 admitted (`rounds[757]`), r40 rejected-honest-stop (`[768]`; C1 3/4 counter suffix defect, C2 met) | r41 landed (report `4c87e06d`, lane `74064474`; 74 seats over two waves; C1 MET 4/4, C2 honest stop on a counter key-name defect (`carriers[].declared` unread); report filed before w2 WAVE-DONE after the request budget ran out, 15 late paths uncommitted); closure in flight (CloseKaidokuR41, prompt generated seconds after spawn, judge told) |
| kengaku | 6 | r40–r49 | r40, r41 admitted (`rounds[759]`, `[766]`) | r42 landed (report `987413e0`, lane `f9bbee69`; 72 seats; C1 14/14 mutants killed, C2 circuit-fibsqrt admitted; wave-2 m_flash share 14/33 below the 50% rule, disclosed); closure in flight (CloseKengakuR42) |
| tsukuroi | 7 | r41–r50 | r41 rejected-honest-stop (`rounds[761]`) | r42 landed (report `cca21e97`, lane `12421a73`; 77 seats over two waves; C1 verified under the frozen predicate but counter sufficiency falsified by fixture/uid-0 variants, C2 not verified (kill rule fired on SC1/SC3)); closure in flight (CloseTsukuroiR42) |
| mado | 8 | r44–r53 | r44, r45 admitted (`rounds[760]`, `[767]`; r45 one 41-seat wave, routed as a defect) | r46 landed (report `b25732fc`, lane `edc14789`; 66 seats; C1 v3 110/110 + 150/150 TARGET_MET, C2 v2 admitted 1/1; predicates re-registered before data; one 3.3 MB seat file left untracked, disclosed); closure in flight (CloseMadoR46) |

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
- 15:29:11 -03, fleet-root write. Kasegi r38 seat `ExecNoHarm` ran a fixture driver that wrote relative paths
  before `cd`, with cwd = the fleet root. It truncated the tracked `LOG.md` (to 22 B) and `SCORECARD.md` (to 51 B)
  and created `PROVINCE.md`, `SHONEN.md`, `SKILL.md` and five `corpus/` files there. The seat restored both
  ledgers from fleet `HEAD` blobs and removed the created paths. Orchestrator check at 15:32:
  - `git diff --stat HEAD -- LOG.md SCORECARD.md MANIFEST.json PROTOCOL.md ROADMAP.md` printed nothing.
  - The last ledger commit, `2df7532d` (mado r44 closure, 15:19:38), predates the incident, so no uncommitted
    ledger bytes were lost.

  Fix: the dispatcher now appends a host guard (`SEAT_GUARD`) to every seat prompt, file and live kernel: the
  cwd is the fleet root, so cd to scratch first; assert the fixture toplevel before git mutations; no PATH-dir
  writes; no fleet-root tracked-file writes. This is a conformance item for kasegi r38's closure.
- ~16:20 -03, orchestrator kernel restart. An operator interjection cancelled a `tw()` tick, and the Python
  kernel came back empty. Recovery: env `HYAKU_LOAD_MAX=120`, `HYAKU_SEAT_CEILING=96`, `%load` of the
  dispatcher, helpers rebuilt, `bootstrap()` re-adopted kengaku falsify, mado w1, souji w1 and five live L1s.
  Seat AgentHandles were lost, so the mado w1 and souji w1 results files carry `output: null` with the
  restart note, and those L1s read seat reports from the wave dirs.
- 16:26 -03: souji r33's L1 had filed and ended while seat `SwarmExecutor31` (FixO4 census rerun) still ran
  with no consumer. The orchestrator stopped the seat to settle the wave. That woke the L1, which captured the
  results (`af7fd25`) and amended its report (`b1c9f43b`). Orchestrator salvage commit `c442b974` holds
  `.ufo/waves/round-33/w1-results.json`. Closure dispatched after that.
- 16:28 -03: tameshi r48 attempt 3 has had no lane commit since 13:21. Its L1 is blocked on its own control
  driver: CTL_B/D/E finished at 15:11, and CTL_C was still running after 3 h. On the orchestrator's nudge the
  L1 committed to a 17:00 -03 deadline: if CTL_C is not done by then, it is recorded as not evaluated (timed
  out) and the round lands.
