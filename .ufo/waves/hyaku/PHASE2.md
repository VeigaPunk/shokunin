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
  {"task":1500}; `task.maxConcurrency` 300 (was 100). `async.maxJobs` stays 100 (default; read at
  process start), so a `task` call is refused while ≥100 background jobs run — L1s retry every
  ~3 min (addendum §6.2 "Job cap").
- **rea MCP disabled** in `~/.omp/agent/mcp.json` (`"enabled": false`, 10:12 -03; pre-edit copy
  `~/.omp/agent/mcp.json.pre-disable-20261020T1015`). The running session keeps its connection
  until `/mcp reload`; kaidoku uses the `rea` CLI (`npx -y rea-agents@6.5.0`). Restore by setting
  `"enabled": true` (or copying the pre-edit file back) when the operator wants it.

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
