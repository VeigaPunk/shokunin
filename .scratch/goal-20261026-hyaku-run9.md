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
| tameshi | 1 | r48–r57 | r48 rejected-harmed (`rounds[765]`, `d98fe66c`; cold-read 60 → 57 below its floor), r49 admitted (`rounds[772]`, `fa882d7d`; calibration 6 → 8, coverage F10 held; spot-check `e3729de8`), r50 admitted (`rounds[782]`, `08a3cdfa`; 85 seats; calibration and coverage improved, F6 open → held; no conformance defects; S022 status, missing gate rows and README frontier routed; spot-check `9962033f`) | r51 in flight (TameshiR51, ~20:21) |
| tabi | 2 | r32–r35 | r32 admitted (`rounds[756]`), r33 rejected-honest-stop (`[763]`), r34 rejected-honest-stop (`[769]`, `e9949eaf`), r35 rejected-honest-stop (`[778]`, `01eef374`; C1 newMapped 0/2, C2 Firefox BiDi capability met, coverage improved, nothing harmed; spot-check `11c64b96`) | **blocked** ~19:22 by `advance` (three consecutive rejected closures r33–r35); block ended at 4 rounds, slot 2 → mori |
| mori | 2 | r51–r60 | r51 admitted (`rounds[786]`, `ae7bc14a`; 68 seats, one v2 wave; operability and depth improved, nothing harmed; 3/3 gate decisions agreed; 8 items routed back; spot-check `4f266ef2`; operator notes on the dispatcher memory gate carried to the final report) | r52 in flight (MoriR52, ~20:45) |
| souji | 3 | r33 | r33 rejected-honest-stop (`rounds[764]`) | **blocked** 16:39 by `advance` (three consecutive rejected closures through r33); block ended early at 1 round, slot 3 → kama |
| kama | 3 | r46–r55 | r46 admitted (`rounds[770]`, `a4a605eb`), r47 admitted (`rounds[777]`, `30fd6e51`; calibration and operability improved, capability live-receipt-replay added; D1–D8 routed incl. C2 counter sufficiency), r48 admitted (`rounds[780]`, `44fabc61`; calibration and operability improved; 69-seat wave; report rewritten in place `15710a2a`→`dcc079e7` as a conformance defect; true m_flash share 26/69 because critic now routes to `@m_kfc`; High archive-hash hang routed to r49; spot-check `438127bc`) | r49 landed ~21:00: report `f8cdb853`, lane HEAD `5b395257`, measured at `24e906f0`; one 71-seat v2 wave, m_flash 39/71 excluding critics; C1 replay execution witness met (witnessed 3/3), C2 append-only v4 met (scenarios 8/8, ungraded 89 → 82); counter gaps (decoy replay, env injection, under-reporting tool) routed to r50; `verify` OK; CloseKamaR49 spawned 21:02 |
| kasegi | 4 | r36–r40 | r36, r37 admitted (`rounds[755]`, `[758]`), r38 rejected-honest-stop (`[762]`), r39 rejected-honest-stop (`[771]`, `13277204`; attempt 2 after attempt 1 hit the request budget; C1 not verified (G2 red, 7/8), C2 verified; expansion improved), r40 rejected (`[779]`, `b0513537`; attempt 2 after attempt 1 hit the request budget at ~19:10; 54+35 = 89 seats; C1 depth:verifiability NOT verified, kill rule fires on the lane's own wave-2 fixtures; C2 coverage 7→8 verified; D1–D7 routed; spot-check `5b29ea14`) | **blocked** ~19:56 by `advance` (three consecutive rejected closures r38–r40); block ended at 5 rounds, slot 4 → chousa |
| chousa | 4 | r52–r61 | r52 admitted (`rounds[787]`, `f0b61b4a`; 83 seats; operability, depth, coverage and calibration improved, nothing harmed; 8/8 sampled gate decisions agreed, one refusal reason disputed; 5 defects routed; spot-check `5b550133`) | r53 in flight (ChousaR53, ~20:53) |
| kaidoku | 5 | r39–r42 | r39 admitted (`rounds[757]`), r40 rejected-honest-stop (`[768]`; C1 3/4 counter suffix defect, C2 met), r41 rejected-honest-stop (`[774]`, `25d2770c`; C1 coverage met and improved, C2 not met on the counter's `declared` key gap; D1–D5 routed), r42 rejected-honest-stop (`[783]`, `eb2c2e94`; C1 SquashFS v3 Frontier→Core met, coverage improved; C2 triage v4 stopped on its own frozen binding (combo C02); 43 seats, below the 64 floor, wave 2 never dispatched; R42-V1–V5 routed; installed backhand-cli 0.25.5 into `~/.local/opt/backhand-0.25.5-v3`; spot-check `6b9e64fe`) | **blocked** ~20:28 by `advance` (three consecutive rejected closures r40–r42); block ended at 4 rounds, slot 5 → kake |
| kake | 5 | r58–r67 | — | r58 in flight (KakeR58, ~20:29; budget/seat-floor and misroot guidance sent) |
| kengaku | 6 | r40–r49 | r40, r41 admitted (`rounds[759]`, `[766]`), r42 admitted (`rounds[775]`, `de34e23c`; calibration and coverage improved; judge disagreed with the Dockerfile reject; R1–R6 routed), r43 admitted (`rounds[781]`, `d259c7cc`; calibration and coverage improved; 38 seats, below the 64 floor, wave 2 never dispatched; judge disagreed with one gate flip verdict (task.toml/solve.sh); R1–R5 routed; spot-check `0cb2e225`) | r44 in flight (KengakuR44, ~20:06; routing correction and the seat-floor reminder sent) |
| tsukuroi | 7 | r41–r50 | r41 rejected-honest-stop (`rounds[761]`), r42 rejected (`rounds[776]`, `e93c3831`; C1 operability improved, C2 depth failed its own kill rule on SC1/SC3; nothing harmed; spot-check `6951ead9`), r43 admitted (`rounds[785]`, `3037d575`; 80 seats; operability and depth improved, nothing harmed; R43-SR1-LIMITS-CONTRADICTION routed; spot-check `98020ece`; rejection streak reset) | r44 in flight (TsukuroiR44, ~20:41) |
| mado | 8 | r44–r53 | r44, r45 admitted (`rounds[760]`, `[767]`; r45 one 41-seat wave, routed as a defect), r46 admitted (`rounds[773]`, `f1da69fc`; operability and coverage improved, nothing harmed; spot-check `60edb66e`; R1–R4 routed), r47 admitted (`rounds[784]`, `9eeac2c3`; 85 seats; operability and coverage improved; judge overruled one seat's FALSIFIES=yes on C1; D1–D4 routed; spot-check `579f694b`) | r48 in flight (MadoR48, ~20:35) |

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
