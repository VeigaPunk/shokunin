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

## Decisions

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
- **Session-only routing addition:** `retry.fallbackChains.m_swe` = commandcode → opencode-go
  deepseek-v4.1-flash, after m_swe rate limits killed executor seats (tabi r16 6, souji r16 2,
  kaidoku r17 2, mado r17 1).
- **Scope ruling (integrator):** tabi owns live browser/CDP page observation including the WebMCP
  page-tool surface; kaidoku keeps CDP only as an REA provider surface (tabi r16 closure notes).

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
   L0 question). kaidoku r17 seat: Go 1.27.3 (`~/.local/opt/go-1.27.3`, not on PATH).


## Provider probes (2026-10-20 10:0x -03)

- m_flash: headless `omp -p --model @m_flash` failed on its primary (commandcode
  deepseek-v4.1-flash, HTTP 400 "JSON node count cannot exceed 32768") because headless mode sends
  the rea MCP's 207 tools natively (41,739 JSON nodes, `~/.omp/logs/http-400-requests/`). In-session
  subagents mount MCP tools under `xd://`, and a generic `task` and a `scout` probe were both served
  by commandcode deepseek-v4.1-flash (session transcripts ProbeTaskFlash/ProbeScoutFlash). With
  `--tools=read` or rea disabled, the headless primary answers too. charm-hyper fallback: 402 out of
  credits; opencode-go and devin deepseek-v4.1-flash answer.
- m_haiku, m_swe (devin/swe-2), m_sol, m_opus: primary answered. m_swe has no fallback chain.
  devin/claude-opus-5-5 (an m_opus fallback): weekly quota exhausted. google-antigravity rejects
  this host's tool schemas (400).

## Loop

`inline.sh dispatch <lane>` → L1 `task` (prompt `.ufo/prompts/<lane>-round-<N>.md`) →
`inline.sh verify <lane>` → `inline.sh closure <lane>` → closure `task` → `inline.sh closed <lane>`
→ `inline.sh advance <lane>` → next dispatch while the lane's block of 10 is unfinished.
Failed attempt: `inline.sh fail <lane> "<why>"` then re-dispatch (blocked after 3 attempts).
