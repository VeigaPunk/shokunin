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
| tameshi | 1 | r48–r57 | r48 rejected-harmed (`rounds[765]`, `d98fe66c`; cold-read 60 → 57 below its floor), r49 admitted (`rounds[772]`, `fa882d7d`; calibration 6 → 8, coverage F10 held; spot-check `e3729de8`), r50 admitted (`rounds[782]`, `08a3cdfa`; 85 seats; calibration and coverage improved, F6 open → held; no conformance defects; S022 status, missing gate rows and README frontier routed; spot-check `9962033f`) | r51 attempt 1 RETRYABLE fail ~23:10 (TameshiR51 exceeded its soft request budget, 302/200); attempt 2 (TameshiR51a2) killed in the 23:57 session exit (w2 61/64 settled; salvage `53afb4aa`) -> attempt 3 in flight (TameshiR51a3, 00:18 Oct 27; last attempt) |
| tabi | 2 | r32–r35 | r32 admitted (`rounds[756]`), r33 rejected-honest-stop (`[763]`), r34 rejected-honest-stop (`[769]`, `e9949eaf`), r35 rejected-honest-stop (`[778]`, `01eef374`; C1 newMapped 0/2, C2 Firefox BiDi capability met, coverage improved, nothing harmed; spot-check `11c64b96`) | **blocked** ~19:22 by `advance` (three consecutive rejected closures r33–r35); block ended at 4 rounds, slot 2 → mori |
| mori | 2 | r51-r60 | r51 admitted (`rounds[786]`, `ae7bc14a`; 68 seats, one v2 wave; operability and depth improved, nothing harmed; 3/3 gate decisions agreed; 8 items routed back; spot-check `4f266ef2`; operator notes on the dispatcher memory gate carried to the final report), r52 admitted (`rounds[790]`, `205f5ce2`; report `aacd7a83`, lane HEAD `37af57f2`; one 68-seat v2 wave; C1 met 8 -> 0 mismatches, C2 met 28/28 entailed dissent 0, rows re-voted by non-author voters) | r53 attempt 1 (MoriR53) killed in the 23:57 session exit (w1 66/67 settled; salvage `0df80303`) -> attempt 2 in flight (MoriR53a2, 00:18 Oct 27) |
| souji | 3 | r33 | r33 rejected-honest-stop (`rounds[764]`) | **blocked** 16:39 by `advance` (three consecutive rejected closures through r33); block ended early at 1 round, slot 3 → kama |
| kama | 3 | r46–r55 | r46 admitted (`rounds[770]`, `a4a605eb`), r47 admitted (`rounds[777]`, `30fd6e51`; calibration and operability improved, capability live-receipt-replay added; D1–D8 routed incl. C2 counter sufficiency), r48 admitted (`rounds[780]`, `44fabc61`; calibration and operability improved; 69-seat wave; report rewritten in place `15710a2a`→`dcc079e7` as a conformance defect; true m_flash share 26/69 because critic now routes to `@m_kfc`; High archive-hash hang routed to r49; spot-check `438127bc`), r49 admitted (`rounds[788]`, `15f9a639`; 71 seats; operability and calibration improved; 5/5 sampled gate decisions agreed; R1–R5 routed; R6 operator-side: the prompt still quotes critic as `@m_flash`; spot-check `26ecba64`), r50 admitted (`rounds[794]`, manifest `977e7be9`; report `9e38a361`, lane tip `5a1e29a1`; 66 seats; the closure re-measured both claims on a fresh clone with the frozen counters: C1 3/3 at tip vs base fail, C2 12/12 vs base 9/12; operability and calibration improved; 3/3 admits + 3/3 rejects agree, spot-check `57a2e25b`; R1–R7 routed incl. wrong SOURCES row counts in the report (236→239, not 237→240) and R7 operator: stale route map in the prompt; processed late, see Incidents) | r51 attempt 1 (KamaR51) killed 7 min in by the 23:57 session exit (no lane writes) -> attempt 2 in flight (KamaR51a2, 00:18 Oct 27) |
| kasegi | 4 | r36–r40 | r36, r37 admitted (`rounds[755]`, `[758]`), r38 rejected-honest-stop (`[762]`), r39 rejected-honest-stop (`[771]`, `13277204`; attempt 2 after attempt 1 hit the request budget; C1 not verified (G2 red, 7/8), C2 verified; expansion improved), r40 rejected (`[779]`, `b0513537`; attempt 2 after attempt 1 hit the request budget at ~19:10; 54+35 = 89 seats; C1 depth:verifiability NOT verified, kill rule fires on the lane's own wave-2 fixtures; C2 coverage 7→8 verified; D1–D7 routed; spot-check `5b29ea14`) | **blocked** ~19:56 by `advance` (three consecutive rejected closures r38–r40); block ended at 5 rounds, slot 4 → chousa |
| chousa | 4 | r52-r61 | r52 admitted (`rounds[787]`, `f0b61b4a`; 83 seats; operability, depth, coverage and calibration improved, nothing harmed; 8/8 sampled gate decisions agreed, one refusal reason disputed; 5 defects routed; spot-check `5b550133`), r53 admitted (`rounds[792]`, manifest `f7ecd958`; report `3ffca1dd`, lane HEAD `d21eb285`; C1 45/45 at 8/8 PASS, C2 SOURCES 116->120 append-only, 2/2 admits + 2/2 rejects agreed; defects routed incl. w2 results never arrived, counter forgeable 5 rounds; spot-check `c49ffc6c`; w2.ready orphaned - L1 exited before dispatcher marked wave), r54 admitted (`rounds[795]`, manifest `3e4e1607`; report `86023b97`, lane tip `25abbe82`; C1 operability 1/6 → 6/6 (OLE `.doc` reader, re-measured against a LibreOffice export), C2 depth rows 120 → 123 with 33/33 quotes located once, calibration 9/9 anchored corrections; nothing harmed, all three trends improved; 3 admits + 2 rejects agreed; filed before w2 settled; w2 integration, C1 counter forgeability RW-1 (sixth round), QUALITY 97 offsets and lesson Mistakes row 2 routed to r55; spot-check `714cf555`; late w2 output salvaged `78ebc257`, r53 w2.ready marked abandoned `dba605de`) | r55 in flight (ChousaR55, 00:24 Oct 27; base `dba605de`) |
| kaidoku | 5 | r39–r42 | r39 admitted (`rounds[757]`), r40 rejected-honest-stop (`[768]`; C1 3/4 counter suffix defect, C2 met), r41 rejected-honest-stop (`[774]`, `25d2770c`; C1 coverage met and improved, C2 not met on the counter's `declared` key gap; D1–D5 routed), r42 rejected-honest-stop (`[783]`, `eb2c2e94`; C1 SquashFS v3 Frontier→Core met, coverage improved; C2 triage v4 stopped on its own frozen binding (combo C02); 43 seats, below the 64 floor, wave 2 never dispatched; R42-V1–V5 routed; installed backhand-cli 0.25.5 into `~/.local/opt/backhand-0.25.5-v3`; spot-check `6b9e64fe`) | **blocked** ~20:28 by `advance` (three consecutive rejected closures r40–r42); block ended at 4 rounds, slot 5 → kake |
| kake | 5 | r58-r67 | r58 admitted (`rounds[791]`, manifest `718878f4`; report `8f8c5365`, lane HEAD `9892ea4a`; 68-seat v2 wave + 8-seat residual = 76; C1 calibration, C2 operability, C3 freshness all improved; spot checks 3/3 agree `fd6303ce`; defects routed incl. D1 stale UA, D2 sentinel counter limits, open L0 quarantine-hold) | r59 attempt 1 (KakeR59) killed in the 23:57 session exit (w1 66/66 settled; r1 2/8 spawned, abandoned; salvage `7eff1faf`) -> attempt 2 in flight (KakeR59a2, 00:18 Oct 27) |
| kengaku | 6 | r40-r49 | r40, r41 admitted (`rounds[759]`, `[766]`), r42 admitted (`rounds[775]`, `de34e23c`; calibration and coverage improved; judge disagreed with the Dockerfile reject; R1-R6 routed), r43 admitted (`rounds[781]`, `d259c7cc`; 38 seats, below the 64 floor, wave 2 never dispatched; judge disagreed with one gate flip verdict; R1-R5 routed; spot-check `0cb2e225`), r44 admitted (`rounds[789]`; report `e7b06154`, lane tip `7857ce55`; 76 seats one v2 wave + residual; C1 battery44 kills 5/5, C2 TB2 feal-linear grader admitted, counter defects 8 -> 0; fence bypasses and V11 lookup-table predictor routed to r45; CloseKengakuR44 admitted, advance -> r45) | r45 attempt 1 RETRYABLE fail (~22:27; gpt-6-luna invalid_prompt); attempt 2 (`KengakuR45-2-2`) killed in the 23:57 session exit (w2 39 seats killed, 5 reports; fleet report draft left uncommitted; salvage `fbad1c56`) -> attempt 3 in flight (KengakuR45a3, 00:18 Oct 27; last attempt) |
| tsukuroi | 7 | r41–r50 | r41 rejected-honest-stop (`rounds[761]`), r42 rejected (`rounds[776]`, `e93c3831`; C1 operability improved, C2 depth failed its own kill rule on SC1/SC3; nothing harmed; spot-check `6951ead9`), r43 admitted (`rounds[785]`, `3037d575`; 80 seats; operability and depth improved, nothing harmed; R43-SR1-LIMITS-CONTRADICTION routed; spot-check `98020ece`; rejection streak reset), r44 rejected-harmed (`rounds[793]`, manifest `0eb6f284`; 78 seats; C1 coverage PASS 16/16, C2 depth FAIL verdicts_ok 0/3; adjacency harmed: anchor IN-109 moved unmarked; D1–D10 routed; spot-check `5bbd5ff5`; first report commit `5908743b` failed `verify` for a missing SHONEN heading, fixed as `0e363a51`) | r45 attempt 1 (TsukuroiR45) killed in the 23:57 session exit (w1 14/66 spawned, abandoned; salvage `5b3029bf`) -> attempt 2 in flight (TsukuroiR45a2, 00:18 Oct 27); rejections at r45 and r46 would block it |
| mado | 8 | r44-r53 | r44, r45 admitted (`rounds[760]`, `[767]`; r45 one 41-seat wave, routed as a defect), r46 admitted (`rounds[773]`, `f1da69fc`; operability and coverage improved, nothing harmed; spot-check `60edb66e`; R1-R4 routed), r47 admitted (`rounds[784]`, `9eeac2c3`; 85 seats; operability and coverage improved; judge overruled one seat's FALSIFIES=yes on C1; D1-D4 routed; spot-check `579f694b`) | r48 attempt 1 RETRYABLE fail ~21:59 (incomplete); attempt 2 RETRYABLE fail ~22:30 (MadoR48a2 invalid_prompt refusal); attempt 3 (MadoR48-5) killed in the 23:57 session exit (w2 47/48 with results; integration drafts salvaged `cf3deeec`), not counted toward the cap -> attempt 4 in flight (MadoR48a4, 00:18 Oct 27; final) |

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
- 18:44 -03, post-closure write to a closed round. KaidokuR41 filed its report (`4c87e06d`) before its wave 2
  settled, and CloseKaidokuR41 closed r41 at 18:36 on that report (`rounds[774]`, `25d2770c`). The last w2 seat
  results then woke the r41 L1, which committed lane `ae5dc3f3` (wave-2 reports, results ledger, lesson wave-2
  section) and rewrote its report in place (`00171131`, 7 insertions / 6 deletions). That is a closed round's
  report edited after its MANIFEST row. The r42 L1 had started at 18:50 on top of `ae5dc3f3` (`fdabdfa4`), so the
  lane history stayed linear. The MANIFEST row still cites `4c87e06d`, which resolves and is an ancestor. Left in
  place; the closure verdict stands; this is a conformance item for kaidoku r42's closure. Same pattern as
  souji r33 at 16:26: an L1 that yields before WAVE-DONE gets woken by late seat results.
- 18:45-19:05 -03, disk runaway, fleet-wide hazard. Mado r47 seat `ExecRefB` left a shell write running that
  streamed `x\n` into `/fast/scratch/hyaku/mado-r47/ExecRefB/probeA/d1/applications/bad` at ~0.5 GB/s. The
  file reached ~590 GB and `/fast` went from 26% to 83% used; `inline.sh dispatch kama` refused r48 with
  "disk pressure". Cancelling the ExecRefB job did not stop the write: the writer was a `tokio-rt-worker` thread
  of the orchestrator's own `omp.real` (pid 3438, task 1512186, fds 600/601 in a private fd table), so killing
  it would have killed the whole session. What worked:
  - `truncate -s 0` on the file (space back at once; `/fast` 24%), with a 15 s truncation loop as a stopgap.
  - `prlimit --pid 3438 --fsize=274877906944:unlimited`. `omp.real` ignores SIGXFSZ (SigIgn bit 25), so writes
    past 256 GiB fail with EFBIG instead of killing the process. The writer's offset was ~588 GB, so it stopped;
    the file stayed at 0 B afterwards. The 256 GiB soft cap stays in place and is inherited by new children.

  The MadoR47 L1 was told to record ExecRefB as cancelled by the orchestrator. Kama r48 was dispatched once the
  guard read green.
- 19:50 -03, fleet-root misroot. Mori r51 seats `Mo51CritEntail12` (ENTAILMENT vote seat, 6 vote lines) and
  `Mo51ConnSiblings` wrote their reports to `<fleet>/.ufo/waves/round-51/w1/` (cwd = fleet root, relative path).
  The orchestrator moved both, bytes unchanged (sha256 `351684a6…`, `c85e3277…`), into
  `mori-shokunin/.ufo/waves/round-51/w1/`, removed the fleet dir, and told MoriR51. It is a conformance item for
  mori r51's closure.
- 19:55-19:56 -03, fleet-root strays. Three untracked files appeared at the fleet root: `=1239` (16 B, `== shift I- for`),
  `=3900` (49 B, `=== tracked-all siblings SKILL.md: near tsukuroi`) and `T` (0 B). Their names and contents
  look like a seat shell command whose `>=`/`>` redirect misparsed, with cwd = fleet root; the text points at a
  tsukuroi r43 pin-audit seat, but no w2 report quotes those strings, so the writer is unattributed. KamaR48
  saw them at report time and left them. The orchestrator moved them, bytes unchanged, to the ignored
  `.tower/quarantine/fleet-root-strays-20261026T1956/`. No tracked file was touched (`git status` clean after).
- 20:10 -03, fleet-root strays again. `p.out` (62 B, build-spans.py output naming S115) and `p.err` (0 B), from a
  chousa r52 w1 seat with cwd = fleet root. Found by tsukuroi seat SentScopeFinal (F2) and by TameshiR50. The
  orchestrator moved both, bytes unchanged, to the ignored `.tower/quarantine/fleet-root-strays-20261026T2010/`
  and told ChousaR52. It is a conformance item for chousa r52's closure.
- 20:44 -03, fleet-root stray. `tree.json` (347495 B, a GitHub API tree dump of hyprwm/Hyprland `efb50993`)
  appeared at the fleet root; the Hyprland keymap scouting shape attributes it to a mado r48 w1 seat with cwd =
  fleet root. The orchestrator moved it, bytes unchanged, to the ignored
  `.tower/quarantine/fleet-root-strays-20261026T2055/` (sha256 in `SHA256SUMS` there) and told MadoR48. It is a
  conformance item for mado r48's closure. `.ufo/reports/round-49/kama.md` (untracked at the same moment) is
  KamaR49's in-flight fleet report, not a stray; left alone.
- 21:08 -03, fleet-root stray. A fixture tree `fx/A2-uppercase-fsid-sysfs/sysfs/<fsid>/devinfo/1/scrub_speed_max`
  (1 file) appeared at the fleet root; the btrfs scrub fsid/sysfs shape attributes it to a tsukuroi r44 w1 C1
  scrub-arm seat building a fixture with a relative path, cwd = fleet root. The orchestrator moved it, bytes
  unchanged, to the ignored `.tower/quarantine/fleet-root-strays-20261026T2114/` (`SHA256SUMS`, `TREE.txt`) and told
  TsukuroiR44. It is a conformance item for tsukuroi r44's closure. `.ufo/reports/round-44/kengaku.md` (untracked
  at the same moment) is KengakuR44's in-flight fleet report; left alone.
- ~21:13-21:45 -03, host process leak (tsukuroi r44). The frozen C1 counter `tools/score-scrub-arm-r44.py` hit its
  1200 s timeout mid-run and leaked a private mount namespace (tmpfs `r44lib`/`r44view` mounts) plus 8 hung
  processes — found by seat SentMisroot-2 (F1 HIGH) at ~21:41. The leaked bash trees (2369032 + children,
  3823343/3823351 + children) were orphaned to `systemd --user` after the counter died; the r44 tmpfs mounts lived
  only inside their namespace (`findmnt -t tmpfs` on the host shows nothing). The orchestrator SIGKILLed/SIGTERMed
  the orphans at ~21:55; `/proc/*/mountinfo` now shows zero r44 mounts and the processes are gone. Remediation routed
  to tsukuroi r44's L1: counter must DEVNULL+start_new_session children and killpg+reap on TimeoutExpired.
- ~21:55 -03: kake r58 r1-wave results handoff. All 8 r1 seats had settled (reports committed) but the dispatcher's
  next tick had not yet re-checked liveness, so KakeR58 was still waiting on WAVE-DONE. The orchestrator ran
  `finalize()` directly: `.ufo/waves/round-58/r1-results.json` written and `WAVE-DONE` delivered to KakeR58.
- ~22:04-22:14 -03, premature `advance` hazard (kake r58). `inline.sh closed` printed `0 none` because the
  closure judge's MANIFEST commit had not landed yet; `advance` then walked `next/kake` 58->59 recording
  `none` and a second `advance` call walked it to 60. `advance` does not verify a round ran — it records
  whatever `closure_count` (MANIFEST hyaku rows for lane_round=n) says and unconditionally bumps next.
  Recovery: `next/kake` reset to 59, the two phantom `outcome/kake-r58`/`kake-r59` files deleted, r59
  re-dispatched and KakeR59 spawned. Correct order: wait for the closure job's result, confirm the
  MANIFEST row, then `closed` -> `advance` -> `dispatch`. `advance` must not run before the verdict lands.
- ~22:20 -03, operator routing change: `executor`, `labrat`, `sentinel`, `mutation-tester`,
  `reviewer`, and `security-reviewer` now route to `@m_mim`; `scribe`, `sonic`, `simplifier`,
  and `revenger` remain `@m_flash`; critic/connector stay `@m_kfc`. Existing in-flight work
  retains its spawn-time routing; the revised map applies to future delegations. Addendum updated.
- ~23:00 -03, operator routing amendments 2 and 3: "use some more m_zfl on the roles assignment" moved
  reviewer/mutation-tester/security-reviewer back to `@m_zfl`; "also, m_flash on some other roles" moved
  labrat/sentinel back to `@m_flash`. Live map read back from `cfg://task/agentModelOverrides` (source:
  global config): task/main/planner `@m_opus`; executor `@m_mim`; reviewer/mutation-tester/security-reviewer
  `@m_zfl`; scribe/sonic/simplifier/revenger/labrat/sentinel `@m_flash`; critic/connector `@m_kfc`; scout
  `@m_sonnet`; distiller/seance `@m_haiku`. The routing bullet in `lane-addendum.md` now states this map,
  and the ≥50 % m_flash share rule no longer binds. Routing notes went to the seven in-flight L1s.
- ~22:25–22:45 -03, fallback-chain exhaustion: L1s KengakuR45 (attempt 1) and MadoR48a2 (attempt 2) and
  seats R54CritSeparable, R54ConnSiblings and CritCounterTiming died with `[openai-codex/gpt-6-luna] Codex
  error event: Invalid prompt ... (code=invalid_prompt)`. Every fallback chain ends at
  `openai-codex/gpt-6-luna:low`; the delivered errors do not show why the earlier links failed. Both L1s
  were retried: mado attempt 3 (MadoR48-5, the last allowed) and kengaku attempt 2.
- ~22:35–23:30 -03, L1 name collisions and orphaned waves. Attempt-2 spawns without the attempt suffix reused the
  attempt-1 name, so the runtime deduplicated the new agents' ids: kengaku attempt 2 runs as `KengakuR45-2-2` and mado
  attempt 3 as `MadoR48-5`. Writes to `agent://KengakuR45` revived the dead attempt-1 agent twice instead of reaching
  attempt 2. The dispatcher's `live()` matched only `<name>-N`, so kengaku's `w1.ready` (`l1=KengakuR45`) sat orphaned
  and tameshi's half-spawned w2 (`l1=TameshiR51`, 46/64 seats) froze when TameshiR51 died on its request budget. Fixes:
  `live()` now also matches `<name>-N-M` and `<name>aK` (kernel and `scripts/hyaku/inline-dispatcher.py:193-195`);
  a `finalize` wrapper delivers WAVE-DONE through an `L1_RETARGET` map (mado w2 -> `MadoR48-5`, kengaku w1 ->
  `KengakuR45-2-2`, tameshi w2 -> `TameshiR51a2`); later retries are spawned with the attempt suffix.
- ~23:40 -03, routing amendment (operator: "use m_antigravity as connector and m_kfc as scout"): connector
  `@m_kfc` → `@m_antigravity` (google-antigravity/gemini-3.8-flash:high), scout `@m_sonnet` → `@m_kfc`
  (`~/.omp/agent/config.yml:360,367`; `cfg://task/agentModelOverrides` read back live). Addendum routing
  bullet updated (`scripts/hyaku/lane-addendum.md:10-20`); notes sent to all 7 in-flight L1s.
- ~23:40 -03, chousa r54 w1 straggler settle: ChousaR54 asked the orchestrator to settle w1 (44/49 reports,
  integration landed `447cf7ed`, W2 spec ready). Three seats (R54ExecNegSweep, R54ExecPdfForm,
  R54SentCounters) had been silent 20–65 min, each transcript ending on a finished tool call with no
  reply after it. They were cancelled via `proc://<id>/kill`. R54CritSeparable and R54ConnSiblings had
  already died on the gpt-6-luna invalid_prompt fallback. Cancelling a seat loses its output; it was done
  because the L1 asked for it.
- ~23:38 -03, misrouted seat IRC: kengaku r45 w1 seats address their L1 as `KengakuR45`, so seat
  R45ProbeFirst's report reached the dead attempt-1 agent, which forwarded it. The orchestrator relayed it
  to `KengakuR45-2` and told it to read the w1 seat report files directly instead of relying on IRC.
- ~23:37 -03, host observation: seat R45PkgEntry saw the `~/.local/bin` content digest move between 23:34
  and 23:37. The cause is one new file, `~/.local/bin/OpenBot-0.51.1-x86_64.AppImage` (296,219,269 B,
  mtime 23:36:46). It is not a shim over an existing command, and no lane claimed it. Left in place for
  the operator.
- 23:57:36 -03, orchestrator session exit. The operator's `omp update` sent SIGHUP to the orchestrator session
  (`session_exit` reason `sighup` in its transcript; omp 18.12.6 → 18.13.1). Every L1, closure and seat in it died:
  KakeR59, KamaR51, KengakuR45-2-2, MadoR48-5, MoriR53, TameshiR51a2, TsukuroiR45 and ~80 seats. ChousaR54 had
  already filed (`86023b97`, verified 23:55) with its w2 still running. Recovery in the new session (00:03–00:18 Oct 27):
  - Kernel rebuilt (`HYAKU_LOAD_MAX=120`, `HYAKU_SEAT_CEILING=96`, dispatcher `%load`, tick helpers). `finalize` now
    delivers WAVE-DONE to a live `<l1>aK` respawn when the named L1 is gone.
  - Every unsettled wave got a `<wave>-results.json`; seat outputs that had reached the old session were recovered
    verbatim from its transcript (chousa w2 22/38, kengaku w2 3/39, mori w1 66/67, tameshi w2 61/64). The two
    still-filling waves (kake r1 2/8, tsukuroi w1 14/66) got ABANDONED `.dispatched` markers.
  - Salvage commits of each dead attempt's working tree, lane identity: kake `7eff1faf`, kengaku `fbad1c56`, mado
    `cf3deeec`, mori `0df80303`, tameshi `53afb4aa`, tsukuroi `5b3029bf`. Kama had no lane writes. Chousa's 25 late
    w2 paths stay uncommitted until its closure is in.
  - `inline.sh fail` recorded six deaths (kake, kama, mori, tsukuroi attempt 1; kengaku, tameshi attempt 2). Mado's
    attempt 3 was logged by hand in the same format and not counted toward `MAX_ATTEMPTS`: an orchestrator-caused
    exit should not block a lane. All seven were re-dispatched on their original bases and spawned with
    per-lane resume notes (KakeR59a2, KamaR51a2, KengakuR45a3, MadoR48a4, MoriR53a2, TameshiR51a3, TsukuroiR45a2).
    CloseChousaR54 was spawned on the landed report.
  - Misroot: tameshi seat `T51W2Read14` had also written its report to the fleet root `.ufo/waves/round-51/w2/`
    (byte-identical to the lane copy, sha256 `9b17352c…`); moved to `.tower/quarantine/fleet-root-strays-20261027T0020/`.
  - The 256 GiB `prlimit --fsize` soft cap was re-applied to the new omp process (pid 875345; SIGXFSZ ignored, so
    oversized writes fail with EFBIG instead of killing the session). omp 18.13.1 still caps running jobs at 100.
- 00:3x -03 Oct 27, operator: "m_mim should be working, i have a new subscription, you are not selecting the correct one".
  Finding: the route is right (`m_mim` → `minimax-code/MiniMax-M3.1-Flash`; executor seats' first `model_change` shows it),
  but both stored `minimax-code` keys return 429. `/v1/token_plan/remains` per key: credential 55 (added Oct 22) has its
  5-hour window at 72 % but weekly at 0 % until Oct 29 14:17; credential 65 (new subscription, added Oct 26 22:27) has weekly
  at 89 % but its 5-hour window at 0 % until 03:27:12 today (the fleet's executor seats burned it in ~2 h). omp blocks a
  429'd key for only 30 min, so it kept retrying the dead old key; executor seats have been answering on the
  `opencode-go/deepseek-v4.1-flash` fallback. Fix (backup `~/.omp/agent/agent.db.pre-mimblock-20261027`):
  `auth_credential_blocks` now holds key 55 until its weekly reset and key 65 until 03:27:12, and `auth_change_revision` was bumped.
  From 03:27, executor seats should land on key 65 only. Not yet observed.
- 00:3x -03 Oct 27: the operator interjection cancelled a `tw()` tick and wiped the Python kernel again. Rebuilt from
  `/fast/scratch/hyaku-run9/tick-helpers.py` (new: the tick glue as a file, `%load`/exec after the dispatcher);
  `bootstrap()` re-adopted kake a2r1, kengaku a3w1 and the mori a2r1 / tsukuroi a2w1 fills, and the 8 live L1s.
