# hyaku (百) phase 2 — orchestrator record (started 2026-10-20 10:15 -03)

Integrator-of-record artifact for the second in-session run of the hyaku campaign. Phase 1 is
`HANDOFF.md` in this directory; its mechanics (`scripts/hyaku/inline.sh`, `fleet-commit.sh`,
`append-closure.py`, state under `~/.local/state/shokunin-hyaku/`) are unchanged.

## Operator directives (verbatim, in order)

1. "ok, we will be doing more training on our shokunins, I want you to train them until round 100;
   do 3 shokunins at a time, use heavy parallelization 64-100 subagents; do it inline | favor using
   m_flash, m_haiku, m_swe for code heavy work"
2. "you can also use m_sol and m_opus"
3. "do not restrict yourself to the 16-32 waves; do it 64-100"
4. "train them on the order you deem best, i prefer you to do 10 sequential rounds on the three that
   you choose"
5. "delegate more to m_flash instead if m_haiku"
6. "you can disable the rea mcp momentarily, we don't need it for now"
7. "let's try to also implement using jj as git manager from now on on shokunin runs"
8. "make sure we are always swarming heavily though;"
9. "increase concurrency, im seeing only 6 subagents now, i would like to always see 64+ running"
10. "continue"
11. "opus is back"
12. "also, swap from m_flash to m_zfl please"
13. "assign more m_zfl please, for future spawns"
14. "executor should use m_flash"
15. "leave scribe as m_haiku"
16. "critic + sentinel (m_opus)"
17. "labrat and scout should be m_flash"
18. "the fallback for the m_zfl should be m_luna max" / "as the last in the cascade"
19. "make m_luna the last fallback for m_flash also"
20. "something definetely bugged up here" / "check what's up and keep back on track"
21. "opus is back" / "now remove m_opus from the subagent delegation though, use m_sol instead"
22. "do not remove m_opus, but put m_swe as critic"
23. "planner m_opus" (already so)
24. "simplifier m_flash"
25. "distiller m_haiku"
26. "sentinel m_luna"
27. "connector m_grok"
28. "executor m_luna"
29. "change the m_grok for the the m_flash"
30. "ok, so, hyper has to be a secondary provider, after commandcode on deepseek v4.1 flash (m_flash) | aside from this, no subagent can inherit m_opus as the fallback; for m_zfl, mflash, m_fast, m_haiku, the last cascade fallback has to be m_luna"
31. "ok let's wrap up and commit and push current progress. dont stop running runs, let them fginish; then we can keep up from where we left off in the same schema"
32. "oh yeah, commit and push what we have developed"
33. "ok, keep the same structure, heavy parallelization, same routings, pick more shokunins to push to round 100  and keeep going"

## Decisions

- **Resume control (directive 33, current).** The operator resumed the campaign without changing
  directives 29–30 routing. Keep ten-round lane blocks, genuine 64–100-seat build/falsify waves,
  jj helper-only lane landings, per-round push, and non-author closure before advancing.
  Reconcile retained claims/reports rather than redispatching claimed rounds or replacing identities.
  Initial next-block candidates from the eligible queue are kengaku r25–34, kumitate r35–44,
  kotoba r47–56; readiness is checked before dispatch. Old-session retry-policy rebinding is
  checked separately; the Kasegi policy hold is not lifted or treated as a quota retry.
- **Historical wrap control (directive 31; pause superseded by directive 33).** Stop new round dispatches and coordinator resumptions.
  SoujiR18, KamaR18 and KagiR22 and their existing workers may finish their current rounds;
  no running agent, worker or service is cancelled. Do not start the next round or advance
  an unclosed claim. Landed author reports awaiting outside closure stay explicitly unadmitted.
  The previously scheduled `bg_9096` backoff wake must not revive anything during this pause;
  KasegiR23 remains separately policy-paused. Preserve claims, attempts and original identities.
  Routing/fallback settings remain session-only: the desired policy above is recorded for resume,
  but no global-save approval or host/MCP restoration is inferred from the wrap request.
- **Order.** Batch 1 = kama (next r16), tameshi (r16), kaidoku (r17): the three lowest-round lanes
  with no closure debt, every phase-1 closure admitted, and provinces that need no host mutation
  while pacman is paused. Ten sequential rounds each: kama r16–r25, tameshi r16–r25, kaidoku
  r17–r26. A lane's next round is dispatched only after the previous round lands and its non-author
  closure is appended (the next L1 reads that spot-check). Later batches: lowest `inline.sh queue`
  first.
- **Closure debt first.** Phase-1 rounds landed without closure (tsukuroi r16, tabi r15, mado r16,
  mori r16, kake r21, souji r15) get non-author closures in parallel with batch 1's first rounds,
  then `inline.sh advance`.
- **Waves.** Every wave is 64–100 seats under policy v2 (`scripts/hyaku/ufo-wave-policy-v2.json`):
  wave 1 build, wave 2 falsify when ≥64 distinct attack items exist; round total ≤200
  (`scripts/hyaku/lane-addendum.md` §6.2).
- **Routing** (session-only `task.agentModelOverrides`, operator-approved 10:11 -03): scout, labrat,
  connector, reviewer, simplifier, distiller, revenger → @m_flash; executor → @m_swe; scribe →
  @m_haiku; critic, sentinel, planner, task (L1s and closures) → @m_opus; mutation-tester → @m_sol;
  main → @m_strong. Global value before the change: every seat @m_flash except critic, planner,
  main → @m_strong.
- **Other session settings** (session-only, operator-approved): `task.agentSoftRequestBudget`
  {"task":1500}; `task.maxConcurrency` 300 (was 100). `async.maxJobs` stays 100 in this process
  (read at process start), so a `task` call is refused while ≥100 background jobs run — L1s retry
  every ~3 min (addendum §6.2 "Job cap").
- **rea MCP disabled** in `~/.omp/agent/mcp.json` (`"enabled": false`, 10:12 -03; pre-edit copy
  `~/.omp/agent/mcp.json.pre-disable-20261020T1015`). The running session keeps its connection
  until `/mcp reload`; kaidoku uses the `rea` CLI (`npx -y rea-agents@6.5.0`). Restore by setting
  `"enabled": true` (or copying the pre-edit file back) when the operator wants it.
- **Concurrency (directive 9).** Six lanes now run concurrently: batch A (kama, tameshi, kaidoku)
  plus batch B (tabi r16, souji r16, mado r17 — the next three in `inline.sh queue`), each still on
  a block of 10 sequential rounds. Gaps between lane waves are filled with real orchestrator waves
  (jj study wave `.ufo/waves/hyaku/jj-w1/`, 67 seats). `async.maxJobs` 1000 is saved globally
  (operator-approved) but this process keeps its start-time cap of 100: every `task`/`agent`/async
  bash call is refused while ≥100 background jobs run, so dispatches retry when capacity dips
  (`scripts/hyaku/await-capacity.sh` proxies the running count from live subagent transcripts).
  The cap lifts on the next omp start.
- **jj lane VCS (directive 7).** `scripts/hyaku/jj-lane.sh` (init/commit/push/state) with a
  sandboxed selftest (`jj-lane-selftest.sh`, 16/16 at commit 67a3123). `HYAKU_VCS=jj` in
  `hyaku.env`: `inline.sh` colocates an idle lane at dispatch and at closure, records lane tips
  from `refs/heads/<branch>` (colocated git HEAD detaches after jj mutations, so `@{u}` is unusable),
  and pushes leftovers through the helper. Lane L1s (addendum §6.4) and closures (closure-prompt
  step 4) commit only through the helper; git writes in a colocated lane are forbidden (jj resets
  the git index on every mutation). The six rounds already in flight were dispatched under the git
  addendum and finish on git; each lane switches at its closure. Fleet-root commits stay on git
  (`fleet-commit.sh`) pending the jj-w1 fleet-root trial. Prior jj state: tameshi and mado already
  carried `.jj/` from 2026-10-19 (immutable alias `::bookmarks()`); `.tower/jj-probe/` holds an
  earlier probe.
- **jj study wave jj-w1** (`.ufo/waves/hyaku/jj-w1/`, 67 seats, reports committed 7d0c760):
  22 sandbox trials (21 lanes + fleet root), 21 lane git-usage audits, 12 jj doc probes, 12 fleet
  tool audits, critics and a sentinel. Every lane trial passed init/commit/push/recovery; the
  sentinel and critics found helper defects (non-fast-forward push could rewind the remote,
  branch flip, `.ufo/state` path-guard bypass, basename lock, orphaned `committed` hash after a
  recovery rebase, committer drift on rebase, remote-rewrite re-publish, deletions/renames not
  landing, phantom deletion through an empty nested `.git`, `--include-ignored` bypassing the size
  cap). Fleet root stays on git (JjAuditFleetCommit, JjAuditWatchdog, JjDocWorktrees: one
  working-copy-moving jj command poisons the next git commit; JjTrialFleetRoot dissented).
- **jj-lane.sh v2** (14df5b9): fast-forward-only pushes, remote-rewrite stop, rebase without
  `--ignore-immutable` keeping the `--as` committer, branch bound at init, canonical paths passed as
  filesets, `.ufo/state`/large-file/phantom-deletion/sweep/foreign-identity guards, deletions and
  renames land, realpath lock, one citable `landed <hash>`, `push --no-rebase` for the driver;
  `state` stays pure git and falls back to detection for lanes init never touched. Selftest 45/45
  (28 cases fail on v1). `inline.sh verify` now treats an unpushed lane as not landed.
- **Per-lane jj routing.** Each lane's next dispatch names its `JjAudit<Lane>.md` and
  `JjTrial<Lane>.md` as routed defects (tooling that reads `HEAD`/`@{u}`/the index under jj).
- **Concurrency.** Seven lanes in flight (tsukuroi r17 added for next-boot safety, below). The
  100-job cap refuses orchestrator dispatches while lane waves run; dispatches retry.
- **Session-only routing additions:** `retry.fallbackChains.m_swe` = commandcode → opencode-go
  deepseek-v4.1-flash after m_swe rate limits killed executor seats (tabi r16 6, souji r16 2,
  kaidoku r17 2, mado r17 1); replaced at directive 12 by zai glm-5.3-flash → devin
  glm-5-3-flash so no route uses the m_flash models.
- **m_flash → m_zfl (directive 12, ~13:4x -03).** scout, labrat, connector, reviewer, simplifier,
  distiller and revenger route to @m_zfl (session-only `task.agentModelOverrides`); headless probe
  `scripts/hyaku/probe-alias.sh m_zfl` → `answered-by=zai/glm-5.3-flash primary-ok=True`. Seats
  already running keep their model; new seats take m_zfl.
- **Opus 429 recovery.** KaidokuR18, TabiR17, TsukuroiR17 and MadoR18 exited on Anthropic 429
  (retry-after 11–14 min); all four were resumed under their original identities after the
  operator reported "opus is back". SoujiR17 (refused earlier by the 100-job cap) dispatched then.
- **Swarm shape.** An orchestrator edit (f4eac4e) briefly limited rounds to one 64–100 spawn wave
  plus resumes; reverted in 8a9a4d8 to build + falsify waves of 64–100 each (round ≤200) per the
  operator's heavy-swarm directives. Worktree isolation for concurrent writers and the
  `landed <hash>` citation rule stay.
- **Boot safety (tsukuroi r17, read-only, IRC to the orchestrator):** the current boot already ran
  the mkinitcpio 42.2 UKI (efivars LoaderEntrySelected = Omarchy.linux; no boot input newer than
  the 09:57:09 boot); 42.2 images ship `new_root -> sysroot`, so the btrfs-overlayfs/plymouth
  `/new_root` hooks resolve (namespace emulation passed). Its first L0 line ("snapshot boots
  degraded") was wrong and is corrected in `.ufo/l0-questions.md` (6fe9984). Remaining cautions:
  re-hash the default UKI if anything rebuilds it; pin snapshot #1 (the only 41.1 rollback); the
  LUKS header backup lives on the encrypted root.
- **More m_zfl (directive 13).** scribe (was m_haiku) and critic + sentinel (were m_opus) now route
  to @m_zfl too; executor stays @m_swe (operator: m_swe for code-heavy work), mutation-tester @m_sol,
  L1s and closures (`task`) @m_opus. Addendum wave mix now ≈80% m_zfl seats (~76 of ~96) with
  executors reserved for items that write or run code. Moving critics/sentinels off Opus also
  lowers pressure on the Anthropic account whose 429s stopped four L1s earlier.
- **Historical executor → m_flash (directive 14, 13:46 -03; later role routing changed).** Executor
  then routed to @m_flash (was @m_swe); every other seat role stayed as directive 13 left it. Probe
  at the switch: m_flash's primary (commandcode deepseek-v4.1-flash) returned 429 "5-hour usage
  limit … resets at 2026-10-20T19:47:54Z" (16:47 -03); the request was answered by
  devin/claude-opus-5-5 through fallback. That Opus fallback entry is historical, removed by
  directive 30, and not current policy. The m_swe fallback chain was then unused by any role; critic
  later returned to m_swe.
- **Scribe stays m_haiku (directive 15).** scribe reverted to @m_haiku; critic and sentinel stay on
  @m_zfl, executor @m_flash. Wave mix ≈70% m_zfl (~66 of ~96).
- **Critic + sentinel back on m_opus (directive 16).** Final seat routing (session-only): scout,
  labrat, connector, reviewer, simplifier, distiller, revenger → @m_zfl; critic, sentinel → @m_opus;
  scribe → @m_haiku; executor → @m_flash; mutation-tester → @m_sol; task (L1s, closures) → @m_opus.
  Wave mix ≈58% m_zfl (~56 of ~96); critic+sentinel capped at ≤10 per wave to limit Anthropic 429s.
- **Scout + labrat → m_flash (directive 17).** Seat routing now (session-only): scout, labrat,
  executor → @m_flash; connector, reviewer, simplifier, distiller, revenger → @m_zfl; critic,
  sentinel → @m_opus; scribe → @m_haiku; mutation-tester → @m_sol; task (L1s, closures) → @m_opus.
  Wave mix ≈40 m_flash / ≈32 m_zfl of ~96. m_flash's primary (commandcode) is at its 5-hour plan
  limit until 2026-10-20T19:47:54Z (16:47 -03); until then those seats answer through a fallback.
- **m_zfl cascade (directive 18).** Session-only `retry.fallbackChains.m_zfl` = devin
  glm-5-3-flash-1m → charm-hyper glm-5.3-flash → openai-codex gpt-6-luna:max (m_luna max, last).
  Probe of the new last hop at 14:24 -03: openai-codex gpt-6-luna answered (`stop`).
- **m_flash cascade (directive 19).** Session-only `retry.fallbackChains.m_flash` = charm-hyper
  deepseek-v4.1-flash → opencode-go deepseek-v4.1-flash → devin deepseek-v4-1-flash →
  openai-codex gpt-6-luna:max (m_luna max, last). Keyed first by the m_flash role; since 15:50 -03
  the same cascade is also keyed by its primary model `commandcode/deepseek/deepseek-v4.1-flash`,
  which outranks role chains, so m_fast/plan sessions failing on that model now walk it too.
- **Diagnosis at directive 20 (15:2x -03).** Three faults:
  1. *zai rate limit kills m_zfl seats.* Seat transcripts in this session: 3,550 × `429 Rate limit
     reached for requests (type=1302)` from zai in 90 min and 127 transcripts ending in "Retry budget
     exhausted after 10 retries" — those seats retried zai only and never walked the m_zfl cascade
     (e.g. TameshiR17.RR7-2, RR1-2). Losses: tabi r17 17, tsukuroi r17 43 of 82 wave-2 seats, souji
     r17 28+. Mitigation: `retry.maxRetries` 10 → 40 (session-only) so seats ride out bursts
     longer; more retries do not change which chain a seat walks (see the fallback entry below).
  2. *Revived L1 completions were not delivered to the orchestrator.* TabiR17 had exited on a 429,
     was messaged, and landed r17 at 14:51 (af41737), but its completion never surfaced in the
     orchestrator's job waits, so its closure sat undispatched ~35 min. Observed
     (RuntimeRevivedCompletion-2): TabiR17's job had already settled failed at 13:06 and its session
     kept working; the 13:22 message was answered `Delivered to TabiR17` (a warm turn in a live
     session), no new run appeared, and `wait` never saw the 14:52 finish. TsukuroiR17 and
     KaidokuR18 had parked; their messages were answered `Queued … (was parked; revived)`, each
     showed as a fresh run in `proc://`, and `wait` delivered both. Later, TabiR18's revival
     appeared in `wait`, but SoujiR17-3 (`was parked; revived`) and KaidokuR19 (`Delivered to`) did
     not. Practice: after each wait, for any revived L1 missing from its list, check
     `.ufo/reports/round-<N>/<lane>.md` and the child's `history://` tail.
  3. *Orchestrator routing broadcasts interrupted L1 waits.* Seven routing notes × seven L1s
     (directives 12–17) each interrupted an L1's wait; routing is by role and needs no L1 action, so
     those broadcasts stop. Concurrency fell to ~27 jobs while lanes integrated; mori r17 joins to
     restore wave pressure.
- **Fallback ownership (corrected 16:4x -03 after RuntimeFallbackOwner-2).** Chain lookup is exact
  model → provider wildcard → live role → `default` (omp://settings.md). A role-bound seat captures
  its alias cascade at spawn (`session_init` modelRole + retryFallback) and walks it: an m_flash
  scout went commandcode 429 → charm-hyper 402 → opencode-go at 13:35 -03
  (SoujiR17-3.ScoutKeepOnlySouji). The earlier note here, that role `subagent:<id>` kept alias
  cascades from ever being consulted, was wrong. Two questions stay open: why the zai seats retried
  zai ten times (~72 s apart) without switching, and why Opus 429s with ~2.5 h retry-after killed
  L1s (TabiR18, SoujiR17-3, KaidokuR19) without falling back. A provider retry-after or cooldown
  steering the retry policy fits both but is unproven; no retry-decision records persist. A seat
  keeps the chain it captured at spawn, also when revived: RR7-2 (spawned 13:49 with the two-hop
  m_zfl chain) still used it after Luna was added at 14:25 and after revivals at 15:28 and 15:47.
  Headless `omp -p --model @alias` runs on no role, so `default` owns its failures. Repair from
  15:50 -03 (session-only; reaches new spawns only): each cascade is also keyed by its primary
  model — `zai/glm-5.3-flash` = m_zfl cascade, `commandcode/deepseek/deepseek-v4.1-flash` = m_flash
  cascade, `openai-codex/gpt-6.1-sol` = m_sol cascade, `anthropic/claude-opus-5-5` = default
  cascade — so ownership no longer depends on role; role assignments and cascade order are
  unchanged. Fresh smoke seats (SmokeFlashCascade, SmokeZflCascade, SmokeOpusCascade) failed over:
  commandcode 429 → opencode-go deepseek-flash; zai 429 (type=1302) → openai-codex gpt-6-luna;
  Anthropic 429 → openai-codex gpt-6.1-sol. That proves failover for new spawns, not which key won
  (the alias chains hold the same hops) or what caused the earlier deaths.
- **m_sol briefly replaced m_opus (directive 21), reverted by directive 22; directives 23–30 (directive 30 changes fallback policy only).**
  Current routing (session-only): task (L1s, closures), planner → @m_opus; main → @m_strong;
  critic → @m_swe (exact-model fallback key `devin/swe-2` = m_swe cascade zai glm-5.3-flash →
  devin glm-5-3-flash); executor, sentinel → @m_luna (exact-model key `openai-codex/gpt-6-luna` =
  m_luna cascade devin gpt-6-luna); connector, scout, labrat, simplifier → @m_flash;
  mutation-tester → @m_sol; reviewer, revenger → @m_zfl; scribe, distiller → @m_haiku.
  Risk: Codex now carries m_luna, m_sol and the last hop of the m_zfl/m_flash cascades.
- **Connector → m_flash (directive 29, supersedes directive 27).** "change the m_grok for the the
  m_flash": connector leaves @m_grok for @m_flash, joining scout, labrat and simplifier; at that
  time no other role mapping, alias or fallback list changed. Historical, no longer routed: directive 27's
  connector → @m_grok with exact-model key `cursor/grok-4.7-fast` = m_grok cascade cursor
  grok-4.7-500k-fast → xai-oauth grok-4.7 → devin grok-4-7, and the ~16:3x -03 probe
  (`probe-alias.sh m_grok m_swe m_luna`) where all three primaries answered. The change is
  session-only and reaches only seats spawned after it: running sessions and resumed seats keep
  the chain they captured at spawn; nothing was saved globally.
- **Historical coordinator-chain correction (18:2x–18:3x -03; superseded by directive 30).** Fresh
  KaidokuR20 and ClosureTabiR18 snapshots contained the three-hop `m_opus` alias chain, without Sol,
  despite the four-hop exact-model chain above. Reported to OMP QA: this disagrees with the documented
  exact-model precedence at spawn. Existing failed coordinators retain those snapshots;
  warm resumes again failed on Anthropic ~8,727-second backoff or Devin weekly quota.
  At that time, session-only mitigation appended the configured Sol tail to `m_opus`, preserving its
  Opus primary and first three fallback hops. KagiR22's snapshot then captured all four hops, and its
  transcript shows Anthropic 429 → Codex gpt-6.1-sol serving real tool calls. This is historical
  evidence of the mitigation on fresh spawns, not a refresh of old agents.
- **Next three ten-round blocks started:** kagi r22–31, kake r22–31, kasegi r23–32.
  First rounds dispatched as KagiR22, KakeR22, KasegiR23; each must finish its named round and
  independent closure before advancing. Their initial work may proceed while the shared
  jj helper's guarded recovery is verified; no live helper commits until that check completes.
- **Routing precedence (ruling on kama r17 closure R8).** The closure found the addendum's
  role→model map contradicting the deployment `MISSION.md` buckets (connector heavy-reasoning,
  critic/sentinel economy). For phase 2 the operator's explicit per-role directives (1–30 above)
  decide each seat's route; `MISSION.md` buckets stay the deployment default outside this phase.
  The addendum quotes each directive verbatim next to the role it binds. Not a lane defect.
- **Scope ruling (integrator):** tabi owns live browser/CDP page observation including the WebMCP
  page-tool surface; kaidoku keeps CDP only as an REA provider surface (tabi r16 closure notes).
- **Directive 30 — current session-only fallback policy.** For Flash, the configured sequence after
  the Commandcode `commandcode/deepseek/deepseek-v4.1-flash` primary is
  `charm-hyper/deepseek-v4.1-flash` → `opencode-go/deepseek-v4.1-flash` →
  `devin/deepseek-v4-1-flash` → `openai-codex/gpt-6-luna:max`; `charm-hyper` is the first configured
  fallback after Commandcode. The same exact-primary-model entry covers the m_flash/m_fast/high/plan
  chains. m_zfl's configured fallbacks are devin GLM → charm-hyper GLM →
  `openai-codex/gpt-6-luna:max`; m_haiku's are devin Haiku → cursor Haiku1m → cursor Haiku →
  `openai-codex/gpt-6-luna:max`. These lists end with m_luna:max; no provider availability or
  induced-failover claim is made. The default and m_opus fallback lists are Codex Sol only
  (`openai-codex/gpt-6.1-sol`); every configured fallback entry containing Opus was removed,
  including exact-model chains, so no subagent may inherit Opus as a fallback. Explicit Opus
  primaries (task/planner and the main session where explicitly selected) remain unchanged, as do
  the other role assignments above. Previously unassigned built-in overrides `security-reviewer`,
  `sonic` and `seance` are explicitly pinned to @m_flash to prevent parent-model inheritance.
  m_luna's separate own-provider backup was not changed. These session-only settings affect fresh
  per-spawn captures only; existing sessions and resumed seats keep their captured chains and are
  not retroactively refreshed. They were not saved globally. No policy/access restrictions changed;
  KasegiR23 remains policy-paused under incident 7 and must not be retried. No provider probe or
  forced-failover test was run for this directive.

## Incidents (phase 2)

1. **Seat in the fleet root (11:19–11:20 -03).** JjAuditMado-2 ran `git commit` and
   `jj git init --colocate` in the live fleet root after a failed `cd`. It self-repaired: HEAD
   re-attached, `git reset --mixed df54adf`, `.jj` and `refs/jj/keep/*` removed. Reflog shows no
   other fleet commit in that window; `origin/master` never moved (verified 11:4x).
2. **tameshi index reset (11:57).** v1 `init` on the stale 2026-10-19 pilot `.jj` (git HEAD had
   moved; every init call used `--ignore-working-copy`) reset the git index to the stale `@-` tree
   (225 staged `D`). Repaired by backing jj out (`refs/jj/*`, `.jj`, per-repo jj config removed,
   `git reset -q`) and re-colocating fresh; git history and working tree untouched. mado's pilot
   `.jj` got the same pre-emptive replacement at its r17 closure. v2 init imports git HEAD first
   and asserts `git status` is unchanged (selftest z20).
3. **Host upgrade by an unknown actor.** `/var/log/pacman.log`: 13 runs 07:45–09:39 -03 including
   `pacman -Syu … linux-lts linux-lts-headers` at 09:15:30 (mkinitcpio 41.1→42.2) — the boot-chain
   change the update-safety gate guards. Operator-owned; tsukuroi r17 carries next-boot safety as a
   priority claim and an L0 question.
4. **Installs by lanes.** kama r16: llama.cpp b11755 (`~/.local/opt`, `~/.local/bin/llama-server`,
   L0 question). kaidoku r17 seat: Go 1.27.3 (`~/.local/opt/go-1.27.3`, not on PATH). tameshi r17
   seat: ruff 0.17.1 and vulture 2.16 (`uv tool`). mado r19 seat: pip 26.2.1 in the uv cache only
   (`uv run --with pip`, nothing on PATH).
5. **`~/.omp/agent/mcp.json` rewritten by an unidentified writer (13:35:56 -03).** The rea entry's
   `"enabled": false` (orchestrator, 10:12 -03, operator-authorized) is gone and its pin moved
   6.5.0 → 6.7.0; file size unchanged (429 B). Reported by KaidokuR19's LiveConfigPins seat; the
   lane did not touch it. A session-transcript search for `rea-agents@6.7.0` found only lane
   content about pins, no writer. In-session seats reach MCP tools through `xd://` devices (see
   provider probes below), so the 207-tool commandcode overflow hits headless runs only. Left as
   is for the operator.
6. **Mado r20 copy-summary guard failure and helper-owned recovery.** A helper-created
   commit was stranded after jj displayed `C .ufo/waves/round-20/{ => w2/IsoV3}/isolate.sh`:
   the old parser fabricated a doubled slash and rejected an allowed path. Replaced rendered
   summary parsing with NUL-delimited Git tree changes (`--no-renames`); copied destinations
   and both rename endpoints are checked, unsupported/empty/error diffs refuse.
   Added explicit `recover` with full hash, exact author/committer, direct branch parent,
   current `@` relationship, conflict/scope guards, and a non-snapshotting fast-forward push.
   First sandbox run was 44/57 (fixture failures retained); corrected fixtures yielded 57/57,
   including old-fail incident-shaped move/copy and dirty-working-copy recovery checks.
   Live recovery used the original nine-path allowlist, not current dirt:
   `landed f8576f765179f651c307f2ea120db1476efcffe8`. Before/after `@` stayed
   `33f6afbb17d5f8bb124768c211f04f0df9ce4128`, the remaining-diff SHA-256 stayed
   `fcf3017e19efe959f1b785cf44bdf031fe3fa4b72eb4c68a09944ebc23fc771e`,
   and the unrelated `w1/reports/IsolationHarness.md` edit was preserved. No raw lane Git/JJ
   write was used for recovery. Implementation JjScopeRecovery; review JjRecoverySafety;
   parent executed final checks and live recovery. No tools installed.
7. **Kasegi r23 provider policy stop.** After its unchanged 64-seat build started, KasegiR23
   ended on Codex `cyber_policy`, not a transient quota error. The lane block is policy-paused:
   preserve retained work, do not route the request through another provider or change access
   settings to bypass the refusal, and exclude it from quota-backoff wakeups. The subsequent
   `proc://` snapshot showed no running KasegiR23 descendants; nothing was respawned or killed.


## Provider probes (2026-10-20 10:0x -03)

- m_flash: headless `omp -p --model @m_flash` failed on its primary (commandcode
  deepseek-v4.1-flash, HTTP 400 "JSON node count cannot exceed 32768") because headless mode sends
  the rea MCP's 207 tools natively (41,739 JSON nodes, `~/.omp/logs/http-400-requests/`). In-session
  subagents mount MCP tools under `xd://`, and a generic `task` and a `scout` probe were both served
  by commandcode deepseek-v4.1-flash (session transcripts ProbeTaskFlash/ProbeScoutFlash). With
  `--tools=read` or rea disabled, the headless primary answered too. In that historical probe,
  charm-hyper returned 402 (out of credits); opencode-go and devin answered then. This is not current
  availability evidence.
- **Historical probe results:** m_haiku, m_swe (devin/swe-2), m_sol and m_opus primaries answered;
  at that time m_swe had no fallback chain. Historical m_opus fallback evidence: devin/claude-opus-5-5
  weekly quota exhausted. This Opus fallback entry was removed by directive 30 and is not current
  policy. google-antigravity rejects this host's tool schemas (400).

## Loop

`inline.sh dispatch <lane>` → L1 `task` (prompt `.ufo/prompts/<lane>-round-<N>.md`) →
`inline.sh verify <lane>` → `inline.sh closure <lane>` → closure `task` → `inline.sh closed <lane>`
→ `inline.sh advance <lane>` → next dispatch while the lane's block of 10 is unfinished.
Failed attempt: `inline.sh fail <lane> "<why>"` then re-dispatch (blocked after 3 attempts).

## Wrap checkpoint — developed work, not admission

Final model-run state: KagiR22 and SoujiR18 finished naturally; KamaR18's coordinator ended on
Devin weekly quota and no workers remained. Nothing was cancelled. Claims/attempts/baselines remain intact.

| Claim | Pushed checkpoint or snapshot state | Original owner / pending action |
|---|---|---|
| kama r18 | `101f3991d3570bc9350fbf9c5561f4be1185699d`; code/corpus/evidence archived, no author report | `KamaR18`; interrupted by weekly quota, unadmitted; no restart or r19 |
| souji r18 | Author lane `8be65236a4b61fffe9c0d05d30043650848c0a60`; report `856e4f6bd41ddad513bc2a77f936f82972d430c5`; landing verified | `SoujiR18` finished naturally; independent closure pending; inherited operator sweep untouched |
| kagi r22 | Author lane `254d632ed2f6174e1ffcfe636a17b5e18284212f`; report `c5c5d1d26443a5c6f753c9f2424a3e0ed4822cec`; landing verified | `KagiR22` finished naturally; independent closure pending, no r23 started |
| tameshi r18 | Author report landed; no closure verdict | `ClosureTameshiR18` pending provider recovery |
| tabi r18 | Author report landed; no closure verdict | `ClosureTabiR18` pending provider recovery |
| kaidoku r20 | `7a1e0dfa186058073e952d284778c4d6b5f36ed3` | `KaidokuR20`; interrupted, unadmitted |
| kake r22 | `26b27af3be44fec9de221f716b3cf3d2861ab146` | `KakeR22`; interrupted, unadmitted |
| mado r20 | `38d1b367276a73e28d2950a67f20fcd2cc797add` | `MadoR20`; interrupted, unadmitted |
| tsukuroi r19 | `8e5916360f2dfe7bc4eb4ba144081af555900116` | `TsukuroiR19`; interrupted, unadmitted |
| kasegi r23 | `8bf980721554d2d24bcc83e2e0996e0c27684a06` | Archival checkpoint only; policy pause remains, no model retry or code execution |
| mori r18 | No r18 work; r17 rejected at `rounds[372]` | `MoriR18`; quota-blocked before work |
| chousa r25 | No r25 work | `ChousaR25`; quota-blocked before work |

- The six interrupted-round checkpoints preserve developed code, tools, corpus edits and evidence;
  they do not certify claims or replace missing author reports. All came from helper `landed` receipts.
- Nine large generated artifacts and all 96 retained Kama paths passed redacted static secret scans.
  Files above directory tracking limits were explicitly included. All six checkpointed lanes verified
  `ahead=0 behind=0 tracked=0 untracked=0`; durability is not a claim/test verdict.
- Fleet runtime `.ufo/watchdog.log`/`.ufo/state/*`, operator sweeps and unrelated/ambiguous scratch
  were not swept into commits. Latest actual closure row is 372; a rendered closure prompt is not a verdict.
- Resume only after operator continuation: reconcile `proc://`, named histories and
  `.ufo/reports/round-N/lane.md` first; warm follow-up completions may be absent from `wait`.
- Reuse the original unfinished identities and claimed baselines; do not call `inline.sh dispatch`
  on an already-claimed round or replace dead seats. Apply/verify directives 29–30 for new captures;
  old sessions retain their captured retry policies. Kasegi's policy stop is not a quota retry.
- Same schema: landed author report → `inline.sh verify` → non-author closure → `inline.sh closed`
  → `inline.sh advance` → next dispatch. Never advance without the closure; no new dispatch during pause.
