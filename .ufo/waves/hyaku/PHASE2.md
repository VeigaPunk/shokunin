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

## Continuation — 2026-10-21

- The prior session ended on SIGHUP after the operator selected **Allow recovery
  coordinators**: new identities only for failed checkpointed coordinators, with
  original rounds/baselines preserved, recovery recorded, completed work reused,
  and no respawn of dead worker seats. This supersedes the original-identity-only
  hold above for those failed coordinators; Kasegi's separate policy stop remains.
- The operator resumed sequential training and reiterated: "swwwarm heavy,
  64-100 concurrent parallelization" and "64-100 swarm subagents please".
- Recovered completions: souji r18 admitted at `rounds[373]`, kagi r22 admitted
  at `rounds[374]`. Both claims were advanced only after `inline.sh closed`
  returned `1 admitted`; SoujiR19 and KagiR23 now own their next named rounds.
- `inline.sh verify` observed landed kengaku r25 (`c163a04`, lane `9d8a00d2a`)
  and kumitate r35 (`00b0344`, lane `4c9e40759`). Fresh independent closures
  `CloseKengaku25` and `CloseKumitate35` are pending; neither round is admitted.
- Retained tameshi r18 and tabi r18 also verified landed (`a85e4d8`/`4b7c6823a`
  and `bd330f8`/`df51a0724`). Their earlier closure coordinators failed before
  writing spot-checks; `RecoverTameshi18Closure` and `RecoverTabi18Closure`
  are the explicitly authorized recovery coordinators. No author work is rerun.
- Actual concurrency proof: one validated `kagi-r23-parent-build` task call
  spawned **66** agents: 43 existing command-ledger obligations and 23 existing
  source rows, with 45 scouts, 6 critics, 4 connectors and 11 reviewers.
  `proc://` observed all 66 running alongside the lane coordinators/closures.
  Spec, dispatch and assigned-ID registry live under
  `kagi-shokunin/.ufo/waves/round-23/parent-build*`. This is KagiR23's build
  wave, not an extra round or an admission verdict. Reports have disjoint
  absolute paths; seats do not edit production or execute live credential gates.
  KagiR23 remains the sole production integrator. Souji's next build dispatch
  waits for capacity while it prepares independently; no quota-padding tasks.
- *Superseded (next bullets):* at first the continuation ran on the global role map; directives 29–30
  were not yet restored. Helper log labels such as `model=@m_opus` are configured labels, not
  evidence of the answering model.
- Verification so far: real dispatch, assigned registry and observed running
  jobs; landed-report checks above. These do not certify the new rounds'
  behavior. Each new round still requires actual changed-path execution,
  committed evidence, report landing and independent non-author closure.
- No tools installed or updated by this continuation's orchestrator.

### Continuation directives and corrections (2026-10-21, later)

34. "swwwarm heavy, 64-100 concurrent parallelization" (twice) / "64-100 swarm subagents please"
35. "use m_zfl on revenger"

- **Opus fallback observed, routing restored.** Under the global map, m_flash seats fell through
  `commandcode` (429 weekly limit, resets 2026-10-27T09:47:39Z) → `charm-hyper` (402 out of
  credits) → `anthropic/claude-opus-5-5`: 25 m_flash parent-build seats answered on Opus (transcript
  scan, e.g. `ClaimR11X02` model_change 03:46:43Z). That violates directive 30, so the exact
  directive-29/30 session values were replayed from the prior transcript and re-applied
  (session-only, NOT saved): `retry.fallbackChains` with no Opus entry and m_zfl/m_flash/m_fast/
  m_haiku tails `openai-codex/gpt-6-luna:max`; `task.agentModelOverrides` task/planner @m_opus,
  critic @m_swe, executor/sentinel @m_luna, mutation-tester @m_sol, scribe/distiller @m_haiku,
  scout/labrat/connector/simplifier @m_flash, reviewer/revenger @m_zfl (directive 35 satisfied).
  Agents spawned before the restore keep their captured chains. Devin also reports weekly quota
  exhausted; these are provider observations, not availability proof.
- **Job cap.** The process refuses `task` spawns at 100 running background jobs, process-wide,
  nested seats and coordinators included ("Background job limit reached (100)"), although
  `async.maxJobs` reads 1000. A 100-seat wave can never start from an L1; waves stay ≤88.
- **Gate failure and fix.** A Main-held GRANT protocol stalled while Main's eval kernel blocked
  600 s on a config write: SoujiR19 landed r19 with 0 seats and TsukuroiR19Recovery landed r19
  without its prepared falsify wave (both disclosed in their reports). Main revived both to run
  their validated waves through the new self-service gate `scripts/hyaku/wave-slot.sh` (acquire/
  release; live-agent transcript proxy + recent grants ≤ CAP 92, 8 slots reserved for
  coordinators; sandbox smoke: grant, timeout, release-regrant) and to append report errata after
  the filed bytes. Tsukuroi's 100-seat falsify spec must be re-validated ≤88.
- **Closures since resume:** `rounds[375]` kumitate r35 admitted; `[376]` kengaku r25
  rejected-honest-stop (expansion harmed at first landing; operator may rule the tip-corrected
  reading admissible); `[377]` tameshi r18 admitted; `[378]` tabi r18 admitted. All four advanced;
  kengaku r26 is repair-first.
- **Live now:** KumitateR36 (96-seat build wave dispatched), KamaR18Recovery (integration, ≤8
  residual seats), SoujiR19 and TsukuroiR19Recovery (gated post-hoc waves), TameshiR19-2, TabiR19-2,
  KengakuR26-2 (fresh rounds, restored routing), CloseKagi23 (kagi r23 landed `8a4ecbbd`, wave
  evidence `46fac5a2`, report `00cfe25d`; disclosed L1 deviation: a real-tree `cells` run executed
  host-private R18-01, uncredited, M23-5). Remaining interrupted claims (kaidoku r20, kake r22,
  mado r20, mori r18, chousa r25) wait for coordinator capacity; kasegi r23 stays policy-paused.

36. "more concurrency, i want 64-100"
37. "use more m_zfl please"

- **Routing saved globally (operator chose "Save globally").** `retry.fallbackChains` and
  `task.agentModelOverrides` are persisted in `~/.omp/agent/config.yml`. Directive 37 moved scout,
  labrat, connector and simplifier from @m_flash to @m_zfl (reviewer/revenger already @m_zfl),
  session and global; executor/sentinel @m_luna, critic @m_swe, mutation-tester @m_sol,
  scribe/distiller @m_haiku, task/planner @m_opus unchanged. Coordinators spawned earlier keep
  their captured map.
- **Gate measure corrected.** `wave-slot.sh` now counts running agents as subagent transcripts
  without a non-empty `<id>.md` output (+3 revived allowance), CAP 98; the transcript-recency proxy
  overcounted (live 44 vs 26 jobs) and starved a 68-seat wave. Sandbox smoke: 20 running + 70 granted,
  then 64 refused (timeout) with 70 pending.
- **Recovery coordinators dispatched (attempt 2 each, `inline.sh fail` + `dispatch` recorded):**
  KaidokuR20Recovery (w1 registry records 0 assigned; lane determines real spend), KakeR22Recovery
  (128 spent → ≤72 left), MadoR20Recovery (163 spent → no new wave), MoriR18Recovery (repair-first
  after `rounds[372]` rejected-harmed), ChousaR25Recovery (0 spent). kasegi r23 stays policy-paused.
- **Band at dispatch:** `wave-slot.sh status` → running 92, tameshi r19-w1 64 granted.

38. "i want more concurrency" / "just increase it, ive seen it running 175 concurrently"
39. "run more m_zfl subagents, also" / "and some more m_luna"
40. "for simplifier, use m_composer"

- **Job cap, corrected.** The earlier "process-wide 100" note was wrong. After the gate target went
  to 200 (`~/.local/state/shokunin-hyaku/wave-cap`, re-read on every acquire), MoriR18Recovery
  started 68/68 seats and KagiR24 67 while other waves ran: `proc://` and the transcript census
  showed ~160 concurrent agents (the operator's 175 observation stands). Main's own spawns were
  still refused with "Background job limit reached (100)" (KamaR19 and CloseKumitate36), so while
  waves run Main reuses idle agents by message instead of spawning: KamaR18Recovery became the
  kama r19 L1, CloseKagi23 (never touched kumitate) the kumitate r36 closure.
- **Routing (session + saved globally):** critic @m_swe → @m_luna (critic/executor/sentinel on
  m_luna), simplifier → @m_composer (`xai-oauth/grok-composer-2.5-fast`, fallback
  `cursor/composer-2.5-fast`); scout/labrat/connector/reviewer/revenger @m_zfl unchanged.
  Session-only, not saved: `task.maxConcurrency` 100 → 200, `retry.maxRetries` 10 → 40 (the
  directive-era value; fresh spawns only).
- **Provider saturation (transcripts modified in the last 15 min, 2026-10-21 ~03:5x -03):**
  461 Codex `gpt-6-luna` "at capacity" errors and 31 seats dead after the 10-retry budget; 202 zai
  `glm-5.3-flash` 429s; devin weekly quota (33), charm-hyper out of credits (37), commandcode weekly
  limit (19). Answering-model census of the new Mori/Kagi seats: m_zfl 24 on zai, 19 failed over to
  Codex Luna, 54 not yet answered; m_luna 19 on Codex Luna; m_haiku 17 on Anthropic Haiku. Every
  m_zfl/m_luna fallback path ends on the saturated Codex, so more seats there mostly add retries
  and deaths; dead seats are recorded, never respawned.
- **Memory.** One reading showed 29/30 GB used, 0 available, 22 GB swap, PSI `full avg10=19.95`;
  a minute later MemAvailable was 25 GB and swap 3.3 GB (omp RSS 1.9 GB): a transient seat
  workload spike, not agent count. `wave-slot.sh` now also waits while MemAvailable is below
  `HYAKU_WAVE_MIN_AVAIL_MB` (default 6144); sandbox smoke: floor met → granted, floor unmet →
  timeout exit 3.
- **Closures since:** `rounds[379]` kagi r23 admitted (r24 running), `rounds[380]` kama r18
  admitted (r19 assigned). kumitate r36 landed (lane `91da27c6`, erratum `ba523308`; author keeps
  C1 unadmitted) and awaits its closure.
- **Operator rulings (ask, 2026-10-21):** "Save both globally" → `task.maxConcurrency` 200 and
  `retry.maxRetries` 40 saved; "Add Haiku hop" → `retry.fallbackChains` m_zfl and
  `zai/glm-5.3-flash`: devin GLM → charm-hyper GLM → `anthropic/claude-haiku-5-5` →
  `openai-codex/gpt-6-luna:max` (Luna stays last, directive 30); m_luna and
  `openai-codex/gpt-6-luna`: devin Luna → `anthropic/claude-haiku-5-5`. No Opus entry anywhere.
  Session and global; fresh spawns only. Wave target raised to 240 (state file) with the Haiku
  overflow in place; memory floor unchanged.
- **Job-cap mechanism (scout LiveConcurrencyControl, read against omp 18.12.3 docs + binary):** the
  admission ceiling is `Math.min(100, async.maxJobs)` per spawning session's AsyncJobManager, read
  live; `async.maxJobs` 1000 is inert above 100; completed jobs hold no slot. Observed effect: L1
  sessions dispatch full waves while Main's own spawns can still be refused, so Main reuses idle
  agents by message (KumitateR36 → kumitate r37 repair-first).
- **Closure:** `rounds[381]` kumitate r36 **rejected-harmed** (123 anchors shifted one symbol off at
  the pin, `FIDELITY nonok=0` a false green; C1 operability unprovable, coverage:script-layer
  harmed, runtime-layer improved). Advanced to r37 repair-first.
- **Closures (continued):** `rounds[382]` kake r22 admitted (recovery attempt 2; KakeR22Recovery
  reused for kake r23). `rounds[383]` kumitate r37 **rejected-harmed**: the four notes were reset to
  `0614092` text (131 anchors fixed, 62 previously true anchors broken: S8 27, S7 6, S4 8,
  native-trial 21, by the closure's independent parser at pin `31c465f1`); the fidelity ratchet
  ceilings sum exactly to the current error count, so `FIDELITY: CLEAN` cannot fail; r37 LOG entry
  edited in place. Kumitate now has two consecutive rejections (a third blocks the lane);
  r38 repair-first is assigned to CloseKumitate37, the r37 verifier that holds the independent parser
  and the repair list. kama r19 landed (lane `3389513f`, report `ac9859f4`; KamaR18Recovery reused
  as its author) and its closure went to CloseKake22 (never touched kama).
- **Seat losses observed by lanes:** Mori r18 w1 lost 15/68 seats to Codex `turn_rate_limit_exceeded`;
  kake r22 attempt 1 lost 25 (4 Haiku 429 at startup, 21 when its coordinator died); several
  closures had their ≤8 review seats refused by the job cap and did every check themselves.
- **Latest closures:** kama r19 admitted at `rounds[384]` (spot-check `37bd4c5b`; author
  KamaR18Recovery, verifier CloseKake22); kama r20 is now assigned to CloseKama18 as its author.
  tameshi r19 admitted at `rounds[385]` (spot-check `c144dcd8`; same-ruler 0/5 → 5/5 verified,
  QUALITY20 editing violation disclosed and bounded). Its first r20 author wake failed before
  producing an answer: Anthropic 429, `retry-after-ms=8247000`. No worker wave ran in that wake.
  Parent recorded fail+dispatch as r20 attempt 2, preserving the original baseline. Fresh
  TameshiR20Recovery spawn was refused by Main's job cap; idle CloseKumitate35 is now its
  recovery author. No retry of the failed wake or provider-capacity probe was made.
- **Outstanding coordinator failure:** KaidokuR20Recovery ended on Devin weekly quota before a
  final handoff. Retained round-20 work remains unadmitted. RecoverClaims is reconciling its
  report/checkpoints/actual spent seats and surviving descendants before another writer starts;
  the existing quota error is accepted without a new provider probe.
- **kumitate r38:** the author reports a validated 90-seat build (89 reports) and disclosed its
  mismatch with the narrower 64–88 dispatch context. The operator's 64–100 wave band admits 90;
  no wave was undone or replaced. Independent falsification still must verify the frozen
  811-anchor population, explicit unchecked/debt members, and zero true→nontrue regressions
  against the fixed pairing rule before closure. Author-side numbers are not admission.

41. "make the global default for retry to be 5, not 40" / "on omp, when a model fails"

- **Current retry limit:** `retry.maxRetries=5`, set for this session and saved globally.
  Readback reports `5`, source `global config`, "Maximum retry attempts on API errors".
  This supersedes all earlier retry-40 instructions in this campaign record and old prompt
  snapshots. Fallback chains, routing, concurrency targets and running workers were not changed.
  Already-created child sessions may retain their captured settings; no worker was restarted.
- **Further closures:** mori r18 admitted at `rounds[386]` (spot-check `b3602869`); its r19
  first author wake failed before any answer on Anthropic 429/backoff. Parent recorded failure,
  preserved the baseline and dispatched attempt 2 as fresh MoriR19Recovery; no old worker seat
  was revived or replaced.
- **mado r20 closure:** Main performed the non-author integration after a proposed reviewer's
  wake failed before an answer and a fresh coordinator spawn was refused. RecoverReadyLanes
  independently recounted receipts and reopened sources read-only. Main's immutable `got==want`
  recount confirmed 29/175 → 172/175, unchanged case names/order/expectations; C2's 30-prime
  shares C1 evidence. Unresolved committed recall/precision/resource counterexamples and the
  knowledge entry's current overclaims mean `rejected-harmed`, `rounds[387]`, fleet `eeba593d`.
  Spot-check `794aaeb2` is remote-confirmed. mado r21 is now assigned to fresh MadoR21; a third
  consecutive rejected closure would block the lane.
- **tsukuroi r19:** the held falsify wave finally ran (72 seats, 66 reports, six provider-dead,
  no replacements; total 140), seven repair classes landed. Author tip `e1865d17`, measured
  `1f35705a`, fleet erratum `d70ce422`; fresh CloseTsukuroi19 owns its non-author closure.
  Boot readiness is not certified: the author retains plymouth/hook rechecks as INCONCLUSIVE.
- **souji r19:** its parked follow-up reported a successful 68-seat wave with zero dead, tip
  `49b64584`, errata through `9764dc55`; late reports were still uncommitted. Parent requested
  their helper-only landing before closure, preserving the unrelated operator sweep.
- **kaidoku r20:** failed recovery attempt 2 left pushed tip `5c0b46c4` plus dirty authored
  evidence, no report and no surviving writers. Actual seats spent: 100 + 71 = 171, with two
  missing first-wave reports. Parent recorded fail+dispatch attempt 3; idle generic coordinator
  RecoverTameshi18Closure now owns integration only, no new 64-seat wave or dead-seat replacement.

---

## Session 2 continuation (2026-10-21, session 01a15c83; parent resumed from 01a15963)

42. "swarms should be 64-100" / "high parallelize" / "let's make it so the last fallback for
    [m_zfl, m_flash, m_luna] ; m_auto"
43. "and also for m_haiku ; assign the last fallback to m_auto"
44. "use m_swe as the default model"

- **Routing, saved globally.** `retry.fallbackChains` gained `@m_auto` (cursor/default) as the
  LAST hop on role keys m_zfl, m_flash, m_luna, m_haiku AND on their winning exact-model keys
  (`zai/glm-5.3-flash`, `commandcode/deepseek/deepseek-v4.1-flash`, `openai-codex/gpt-6-luna`,
  `anthropic/claude-haiku-5-5`) — model keys beat role keys, so role-only edits would never
  fire for the primaries. m_luna's own cascade now ends …haiku → @m_auto. `modelRoles.default`
  = `@m_swe` and `m_swe` itself = `devin/swe-2:max` (preserves the prior default's :max effort).
  `task.agentModelOverrides` unchanged. Fresh spawns capture the new chains; running/resumed
  seats keep what they captured at spawn.
- **Wave band:** every new wave remains 64–100 seats per spec (policy v2 + operator 42); the
  validator's per-wave 100 cap and the ≤200/round total still bind.
- **Process census (scout ContinuationLifecycle, read-only):** only two live omp processes —
  this session (2967303) and an unrelated /tmp session (620991) holding ZERO fleet handles.
  No external writer; all parked agent IDs belong to this session and are messageable.
- **Claims reconciled against state (not transcript):** 13 live claims — tameshi 20, tabi 19,
  kengaku 26, souji 20, kagi 24, chousa 25 (attempt 2), kaidoku 21, kake 23, mado 21, mori 19
  (attempt 2), tsukuroi 20, kama 20, kasegi 23 (policy-paused, NOT retried). kumitate stays
  blocked (3 consecutive rejections through r38). No `inline.sh dispatch` on already-claimed
  rounds — that path double-writes.
- **Resumption actions:** fresh `task` coordinators spawned under held claims — SoujiR20-2,
  KagiR24-2, ChousaR25, KaidokuR21-2, KakeR23, MadoR21-2, TabiR19, KengakuR26 (dead-session
  coordinators are unresumable; their waves' seats count as dead seats against ≤200). Parked
  in-session coordinators woken for held claims: TsukuroiR19Recovery→r20, KamaR18Recovery→r20
  queued; TameshiR19-2 (tameshi r20) and MoriR18Recovery (mori r19) wakes FAILED on
  Anthropic Opus 429, retry-after ~73 min — they re-parked; re-wake after backoff, never
  spawn a duplicate writer while a claim-holding identity exists.
- **Seat telemetry:** KaidokuR21-2's fresh r21 wave validated + dispatched 64 unchanged;
  3 executors + 6 critics + 1 sentinel died on Codex `turn_rate_limit_exceeded` (5-retry
  budget) and 6 scribes on Haiku 429 (retry-after ~71 min) — recorded as dead, not replaced.
  SoujiR20-2's inherited 64 W1 seats are dead-session orphans (not in registry, not
  resumable); treated as 64 dead seats, r21 budget reduced accordingly. KagiR24-2 found r24's
  prior attempt had landed lane c5ef9e9 + report WITHOUT the falsify wave — it runs a fresh
  64-seat falsification over frozen r24 artifacts and appends errata (never overwrites filed
  bytes); falsification failure = honest rejection evidence, never a closure write.
- **Gate counter landed:** `wave-live.py` + `wave-slot.sh` + 45-case selftest committed as
  `108a0cd` and pushed. Fixes the earlier phantom/missed-revival count: bounded 256 KiB
  reverse-tail scan; session_exit and assistant error/aborted close a run, later activity
  reopens it, terminal `stop` frees a seat only with a newer non-empty `<id>.md`. Ledger
  `pending` window 120 s self-cleans; observed pending=0 at resumption.
- **Next:** re-wake TameshiR19-2 + MoriR18Recovery after the Opus window; collect reports,
  run non-author closures, then `dispatch` the next unclaimed rounds.

## Session 2 continuation, later directives (2026-10-21, session 01a15c83)

- **Operator ruling (ask):** mado block → "Authorize r22 recovery". `blocked/mado` removed, an
  `operator-unblock` event appended to `events.log`, mado r22 dispatched (MadoR22, attempt 1). The
  r19–r21 rejection history stays on record; the recovery round still needs a non-author closure.

45. "continue"
46. "use m_flash for the scout and connector"
47. "commit and push current progres and developments to the repos"
48. "i want you to add m_inc as the fallback before m_luna for m_zfl, m_flash, m_haiku" /
    `modelRoles: m_inc: inception/mercury-3:max`
49. "m_zfl as executor"

- **Routing, saved globally.** `task.agentModelOverrides`: scout and connector `@m_auto` →
  `@m_flash`; executor `@m_luna` → `@m_zfl` (sentinel stays `@m_luna`, critic `@m_auto`).
  `retry.fallbackChains`: `@m_inc` (`inception/mercury-3:max`, already in `modelRoles`) inserted
  immediately before the final `openai-codex/gpt-6-luna:max` hop on role keys m_zfl, m_flash,
  m_haiku AND on their exact-model keys `zai/glm-5.3-flash`,
  `commandcode/deepseek/deepseek-v4.1-flash`, `anthropic/claude-haiku-5-5` (model keys apply
  whenever that model is active, so a role-only edit never fires for the primaries). Fresh
  spawns only.
- **Checkpoint (directive 47).** Fleet `0db5068` (report baselines + watchdog) pushed. Seven jj
  lanes (kagi, kama, kengaku, mado, mori, souji, tabi) got `jj describe` + `jj new` wip snapshots;
  the snapshot-plus-empty-child topology blocked tabi's and kagi's landing helpers ("non-tip
  dirty base"), so the parent moved each lane's `master` bookmark onto its checkpoint and pushed
  (remote == local verified for all seven; kagi folded its own via `jj-lane.sh recover`).
  game-dev-3d (`89dd182`) and lore (`380ef3a`) were rebased onto their remotes and pushed.
  Lesson: a parent snapshot inside an active jj lane must advance the bookmark in the same step.
- **Coordinator deaths.** MoriR22 (Devin weekly quota, 27 m) and ChousaR27 (Devin quota, 15 m 50 s)
  were revived by message. SoujiR22 (27 m 49 s) and TameshiR23 (34 m) died on Codex `cyber_policy`
  while on the Opus → `gpt-6.1-sol` fallback, as ChousaR26R did earlier. Rule: one fresh
  coordinator per lane with stop-on-refusal; never rephrase, reroute or retry refused work; a
  repeat parks the lane for the operator. MoriR22R, SoujiR22R and CloseKama22 died instantly on
  Opus 429 before doing any work; SoujiR22R and CloseKama22 were later revived. A ChousaR27R2
  replacement overlapped the revived original for ~6 min (parent-caused). It stood down without
  commits and handed its uncommitted lane edits to ChousaR27.
- **Closures this stretch.** `rounds[413]` tameshi r22 admitted; `[414]` chousa r26
  rejected-harmed (selftest FAIL 3/187, streak 1); `[415]` kaidoku r22 admitted (C1 1/6, explicitly
  incomplete, not unprovable); `[416]` tsukuroi r21 rejected-honest-stop (C3 unprovable; 13 Bash
  starts across 9 NO-EXEC seats + 6 fetches = conformance debt; streak 1); `[417]` tabi r21
  admitted; `[418]` kama r22 admitted.
- **Dispatched since.** tameshi r23, kaidoku r23, chousa r27, tsukuroi r22, tabi r22, kama r23.
  Running `dispatch` on tsukuroi and kaidoku while their landed rounds were still unclosed
  re-claimed the same rounds as attempt 2. The closures covered the landed attempt-1 work and
  cleared those claims.
- **Job cap.** Main's spawns are refused at 100 again, so idle agents are reused by message:
  CloseTabi21 → kagi r26 closure; CloseTameshi22 → tameshi r23 recovery author (inherits TameshiR23's
  wave, no re-dispatch); CloseKama22 → kama r23 author.
- **agent.db corruption #3 (12:08:43; operator: "agent.db jsut broke, fix please").** omp
  quarantined the malformed store as `agent.db.corrupt-1792595323977-…` and started a blank one
  (0 credentials), so fresh omp processes were unauthenticated; this session ran on in-memory
  credentials. Fix, following the 10-20 procedure: `sqlite3 .recover` of the quarantined copy
  in a 0700 tmp dir. With and without freelist pages it gave identical rows: integrity ok, 27
  credentials across 14 providers, 10 credential blocks, newest token updates minutes before the
  crash. It was restored at 12:26:14 through the SQLite backup API (`.restore`, WAL preserved,
  page size 4096 = 4096). Snapshots: `agent.db.pre-restore-20261021T122614` and
  `agent.db.recovered-20261021T122614`, both 0600; the tmp copies were deleted. Smoke test: fresh
  `probe-alias.sh` processes, m_inc → inception/mercury-3, m_haiku → anthropic/claude-haiku-5-5,
  m_zfl → zai/glm-5.3-flash, all primary-ok. Lost: ~18 min of blank-store telemetry (kept in
  the pre-restore snapshot). Root cause still unknown. This is the third corruption (10-20 02:40,
  10-21 05:05, 12:08), all under heavy campaign load. The store sits on btrfs (`/@home`,
  zstd) and is opened per operation by several processes (this session, the 5-minute
  `ai-usage.timer`, `omp -p` probes); no process holds it open between operations.
- **Wave gate 240 → 320 (state file, events.log `operator-policy`).** Queued waves were refused at
  live 183 + kotoba 92 / revenger 68 / souji 64 > 240, while MemAvailable was 14.3 GB (floor 6 GB)
  and memory PSI was 0. Raised under directives 36–38 (more concurrency); the memory floor still
  guards the host. The gate admitted a 64-seat reservation at once (live 156).
- **Three-strike rule fix (`inline.sh advance`).** The streak loop counted only outcome files
  equal to `rejected`, but closures write the protocol's whole verdict set (`rejected-harmed`,
  `rejected-honest-stop`), so those never counted toward the block (flagged by CloseTsukuroi21).
  It now matches `rejected*`. Throwaway check: harmed + honest-stop + rejected → 3; mixed with an
  admit → 2; all admitted → 0. Re-audit under the corrected rule: only kumitate (already
  blocked) and mado (r19–r21, operator-authorized r22 recovery) reach 3, so no state changed.
- **Closures since.** `rounds[419]` kagi r26 admitted; `[420]` kake r25 admitted (streak reset);
  `[421]` tameshi r23 admitted. Dispatched: kagi r27 (KagiR26), kake r26 (KakeR25), tameshi r24
  (CloseTameshi22), and first hyaku rounds kotoba r47 (MoriR22R), kotodama r50 (ChousaR27R2)
  and revenger r61 (CloseChousa26), all reused idle agents while Main stays job-capped.
