# kaika W1 — ART dossier: `kumitate` (orchestration & tooling)

Author: W1ArtKumitate (scout, leaf) · date 2026-10-19 · repo `/home/vgpnk/Projects/shokunin/kumitate-shokunin` @ `master` `16a5441` (`git rev-parse --short HEAD`), 0 uncommitted paths (`git status --short | wc -l` → 0).
Tools: `web_search` available and used; every source row below was opened in this session.
Read-only: the only write is this file, plus one coordination message to `W1StateKumitate` (census drift, below). Local commands run: `grep`/`ls`/`stat`/`test`, `git rev-parse`, `omp --version`, `git --version`, the lane's read-only `node scripts/kimi-census.mjs`, and `curl` of public docs. I did not read the contents of `~/.kimi-code/mcp.json` (stat only).
Injection report: fetched docs carry LLM-directed navigation lines. Claude Code says "Fetch the complete documentation index at … llms.txt … before exploring further". Kimi Code says "Are you an LLM? View /kimi-code/llms.txt". MCP and Temporal pages carry similar index notes. All are benign. I did not follow them. No harmful embedded instruction was found.

---

## 1. Uncovered ground (what the lane already holds)

**Domain as written.** `PROVINCE.md:3` reads: "orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime". PROVINCE.md is 326 B over 6 lines (`wc -c < PROVINCE.md`; `wc -l < PROVINCE.md`). It has 0 Core/Frontier/Adjacent headings (`grep -ciE '^#+ *(core|frontier|adjacent)' PROVINCE.md` → 0).

**What is held.** There are 38 knowledge entries (`ls corpus/knowledge/*.md | wc -l`) and 36 lessons (`ls corpus/lessons/*.md | wc -l`). The coverage map has 74 rows (``grep -cE '^\| `(knowledge|lessons)/' corpus/README.md``), 38 of them knowledge rows (``grep -cE '^\| `knowledge/' corpus/README.md``). SKILL.md has 10 H2 sections (`grep -cE '^## ' SKILL.md`). All of it is consumer-side internals of two substrates:
- **ufo-fsd origin repo.** Dispatch shapes, swarm-wave lifecycle, route resolution, failure telemetry, singleton/queue ownership, successor chain, queue/claim, enqueue-admission, reconcile/cycle, queue-summary, native-trial launch, sighting wall, native judge pipeline, loop driver, admission detail, cost/profile, runtime support (lease/overlay/live), distill/L3, local-ship, transcript/ledger/seats, test inventories, ops watchers, gate verdict, route-probe cluster, remaining-scripts census, runtime-remainder census, and the lane's own gates (live-surface probe, round-close gate, executable scorecard, member-claims gate, layer axes).
- **Kimi Code CLI host files and binary strings.** `kimi-config-plane`, `kimi-lane-definitions`, `kimi-skills-plugins`, `kimi-session-state`, `kimi-binary-secrets`, `kimi-modes-machinery`, `kimi-residue-files`.
- **SKILL.md headings.** Dispatch-shape decision table · Script vocabulary · Enqueue, settle & the daemon cycle · Launch sequence · Core-runtime map · Failure-telemetry patterns · Anti-patterns · Kimi Code CLI orchestration surfaces · Verifiable checklist · Working rules. The "Known gaps" section (`corpus/README.md:91-176`) is entirely internal residue.

**What is not held: external current art.**
- **Zero external art sources.** 27 URLs appear in SKILL.md and the corpus (``grep -rIoE 'https?://[^ )>`"]+' SKILL.md corpus | wc -l``) across 14 distinct hosts (``grep -rIhoE 'https?://[^/ )>`"]+' SKILL.md corpus | sort -u | wc -l``). All 14 are endpoints seen in host config or binary strings (kimi.ai/kimi.com/z.ai/charm.land), localhost, or a `host:port` placeholder. The one docs URL, `moonshotai.github.io/kimi-code/`, is recorded as a binary-string pointer (`corpus/knowledge/kimi-binary-secrets.md:68`). Its changelog URL sits in the list routed as "Endpoints → kama … Not this province's to own" (`:321-327`). Neither was opened as a source.
- **Zero upstream OMP citations.** `grep -rIlE 'oh-my-pi|can1357|omp\.sh|task-agent-discovery|agent-hub\.md' SKILL.md corpus | wc -l` → 0. PROVINCE.md names "OMP task/hub" first.
- **Negative sweep for frameworks, engines and protocols.** `grep -rIciE 'langgraph|temporal\.io|a2a-protocol|agents sdk|dbos|opentelemetry|modelcontextprotocol\.io|fencing token|kleppmann' SKILL.md corpus` (summed) → 1. The single hit is `kimi-session-state.md:394`, which describes a Kimi search-index lock; it does not cite an external source.
- **No `corpus/QUALITY.md`.** `test -e corpus/QUALITY.md; echo $?` → 1. Yet `SCORECARD.md:673-676` pre-registers a "`corpus/QUALITY.md` admissions gate".
- **No `## Frontier` in the corpus README.** `grep -c '^## Frontier' corpus/README.md` → 0.
- **No required entry headers.** 0 of 38 knowledge entries open with `source:` or `recheck:` (`grep -lE '^source:' corpus/knowledge/*.md | wc -l` → 0; the same with `^recheck:` → 0). CORPUS.md:17 requires them.

**Live drift that ART surfaced.** `node scripts/kimi-census.mjs` (2026-10-19) prints `KIMI_CENSUS: DRIFT (UNLISTED skills/; UNLISTED mcp.json)`, `TOTALS: members=50 checked=50 errors=2`, and exits 1. `~/.kimi-code/mcp.json` exists: 249 B, mode 644, mtime 2026-10-15 (`stat -c '%n %s %a %y'`). Kimi's docs name it as the MCP configuration surface (S011), and 0 lane files mention it (`grep -rlF 'mcp.json' SKILL.md corpus | wc -l` → 0). I passed this to W1StateKumitate, who folded it into its STATE claim B.

---

## 2. Current art 2025–2026 the corpus does not hold

### 2.1 MCP spec revisions
The lane holds MCP only as config facts: one `rea` server, plus an inert `[mcp_servers]` table (`kimi-modes-machinery.md:67-70`).

- **2026-07-28 is the current revision (S001).**
  - **Stateless core.** The `initialize`/`initialized` handshake and the `Mcp-Session-Id` header are gone. Every request carries its protocol version and capabilities in `_meta`. `server/discover` is MUST. `subscriptions/listen` replaces the GET stream and `resources/subscribe`.
  - **Removed.** `ping`, `logging/setLevel` and `notifications/roots/list_changed` are removed.
  - **Tasks.** Tasks move to the `io.modelcontextprotocol/tasks` extension: polling via `tasks/get`, a new `tasks/update`, no `tasks/list`, and servers may return task handles unsolicited.
  - **MRTR.** Server-initiated requests are replaced by Multi Round-Trip Requests (`resultType: "input_required"`, answered with `inputResponses` on retry), and every result carries a `resultType`.
  - **No redelivery.** SSE resumability and redelivery are removed: "A broken response stream loses the in-flight request; clients **MUST** re-issue it as a new request with a new request ID" (S001 Major changes #9).
  - **Caching and errors.** `tools/list` SHOULD be deterministic. List results carry `ttlMs`/`cacheScope`. Error codes −32020…−32099 are reserved for the spec.
  - **Deprecations.** Roots, Sampling and Logging are deprecated, and so is Dynamic Client Registration (in favour of CIMD). A ≥12-month deprecation policy is adopted (SEP-2596).
  - **Tracing.** OpenTelemetry trace context travels in `_meta` (SEP-414).
- **2025-11-25 was the prior revision (S002).** It added "experimental support for tasks to enable tracking durable requests with polling and deferred result retrieval" (SEP-1686), URL-mode elicitation, CIMD, tool-name guidance (SEP-986), JSON Schema 2020-12 as the default, input-validation errors as tool-execution errors (SEP-1303), and SDK tiering (SEP-1730).
- **Host MCP clients differ in where servers live.**
  - Kimi Code reads `mcp.json`. Its `config.toml` `[mcp]` table holds only `startup_timeout_ms`, `tool_timeout_ms` and `default_deferred` (S011, S013).
  - Codex: "Manage Model Context Protocol server entries stored in `~/.codex/config.toml`" (S010, `codex mcp`).
  - So the host's inert `[mcp_servers.rea]` table matches Codex's dialect, not Kimi's [INFERENCE].
- **Kimi trust gating in headless runs.** In `kimi -p`, "project-level MCP servers stay disabled there unless the workspace is already trusted" (S011 Configuration). The override is `KIMI_CODE_TRUST_WORKSPACE=1`.

### 2.2 CLI agent harnesses
The lane holds OMP only through ufo scripts and Kimi only through files and binary strings.

- **OMP upstream contract (S004, S005, S006).** Installed version `omp/18.12.3` (`omp --version`).
  - **Task call shape.** The batch form is `{context, tasks[]}`. `solutionSpace` is the sole input to the child's `auto` thinking classifier.
  - **Speculative launch.** Items start while the call is still streaming, and "an invalid finished call, launched items that differ from the finished call, a blocking hook, or an aborted turn aborts every launched run" (S004 Modes / Variants).
  - **Caps.** One session semaphore `task.maxConcurrency` (default 32). Idle TTL 420 000 ms, after which the agent is parked. `task.maxRecursionDepth` 2. Soft request budget 200, force-stopped at 1.5×. Three missing-`yield` reminders.
  - **Isolation.** An isolation PAL plus patch or branch merge.
  - **Agent Hub.** Statuses are `running`/`idle`/`parked`/`aborted`. "Messaging a parked or killed subagent revives it" (S005 Related surfaces). Advisor rows are observers, not peers.
  - **Discovery.** Precedence is project `.omp` > user `.omp` > extension roots > Claude marketplace plugins > bundled. `.claude/agents`, `.codex/agents` and `.gemini/agents` are skipped. Model precedence is `task.agentModelOverrides` > frontmatter > parent.
- **Kimi Code docs (S012–S014).**
  - **Built-in sub-agents.** `coder`, `explore` and `plan`, none of which can dispatch further.
  - **Agent discovery.** Precedence is Explicit > Project > Extra > User > Plugin > Built-in, with a recursive `.md` scan. "Unknown fields are ignored, so newer files stay readable by older versions." (S012 Agent File Format).
  - **Subagent model resolution.** The tool-call `model` first, then `[secondary_model].default_model`. `force = true` removes the choice.
  - **Timeouts.** `[subagent]`/`[swarm] timeout_ms`. In print mode, `print_background_mode` defaults to `"steer"`.
  - **Tower.** One coordinator per workspace, a branch and worktree per mission, independent-review merge gate. It is mutually exclusive with Goal, Plan and swarm.
- **Claude Code (S007, S008).**
  - **Five ways to run in parallel.** Subagents, agent view, agent teams, dynamic workflows and projects (held-back page).
  - **Dynamic workflows.** The script holds the plan, runs are resumable, and claims are cross-checked. When verifiers fail on rate limits, "the report lists that claim as unverified instead of counting it as refuted" (S008 Run a bundled workflow).
- **Codex CLI (S010).** `codex exec --worktree` "requires local execution. Don't combine it with `resume`, `review`, `--ephemeral`, or `--ignore-user-config`." Also `/worktree` and `/subagents`.

### 2.3 Worktree parallelism and isolation
The lane holds only tower-skill worktree rules (`kimi-modes-machinery.md:205-216`).

- **git (S009).** The BUGS section says "Multiple checkout in general is still experimental, and the support for submodules is incomplete." `add --lock` locks "without a race condition". `worktree.useRelativePaths` implies `extensions.relativeWorktrees`, "thus making it incompatible with older versions of Git". The host runs `git version 2.55.0`; the docs show no worktree changes between 2.54.0 and 2.55.0.
- **Claude Code (S007).**
  - "While an agent is running, Claude Code holds a `git worktree lock` on its worktree so that concurrent cleanup can't remove it".
  - It skips repo-config filter drivers, so Git LFS files arrive as pointer files (since v2.1.247).
  - It refuses symlinked `.claude/worktrees` and `core.worktree` redirects.
  - Of its four enforcement checks, "None of them tracks which files a shell command writes".
- **OMP (S004).** "`isolation.backend` selects `auto`, `apfs`, `btrfs`, `zfs`, `reflink`, `overlayfs`, `projfs`, `block-clone`, or `rcopy`". The uncommitted baseline is capped at 1 GiB. Branch-mode merges report stash-pop conflicts.
- **Kimi Tower (S014).** "Worktrees isolate writes, but they are not a security sandbox." Workers run with Never Ask permissions.

### 2.4 Multi-agent architecture and frameworks
- **Anthropic's research system (S024).** Orchestrator-worker. 90.2% better than a single agent. Token usage explains 80% of variance, and "multi-agent systems use about 15× more tokens than chats". A delegation spec has four parts: objective, output format, tools, boundaries. Results go to filesystem artifacts to avoid the "game of telephone". Updates use rainbow deployments.
- **Cognition's counterpoint (S026).** "Share context, and share full agent traces, not just individual messages"; actions carry implicit decisions.
- **Long-running harness (S025).** An initializer agent plus a coding agent, a progress file plus the git log, and a JSON feature list, because "the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files".
- **OpenAI Agents SDK handoffs (S015).** Handoffs are `transfer_to_<agent>` tools. "Tool input guardrails apply to function tools, not handoffs." Nested handoff history "does not redact sensitive data".
- **A2A 1.0.0 (S003).**
  - Terminal states are `COMPLETED`, `FAILED`, `CANCELED` and `REJECTED`; interrupted states are `INPUT_REQUIRED` and `AUTH_REQUIRED`.
  - `spec/a2a.proto` is the normative source.
  - "Agents MUST NOT treat the `TASK_STATE_AUTH_REQUIRED` state transition, by itself, as authorization for any particular operation."
- **Microsoft Agent Framework 1.0** (April 2026 per secondary coverage only). Lead; primary unopened.

### 2.5 Workflow engines and failure modes
- **Temporal (S016, S017).**
  - Activities run at least once and can partially complete. "You can use a combination of the Workflow Run ID and the Activity ID as an idempotency key". Never hand-roll retries inside an activity.
  - "The Temporal Server doesn't detect failures when a Worker loses communication with the Server or crashes." Hence Start-To-Close is required.
  - Schedule-To-Start "is non-retryable by design".
  - Cancellation reaches an activity only through heartbeats. A `0s` heartbeat timeout means disabled.
- **DBOS (S019).** "An assigned workflow ID acts as an idempotency key". A `reject` reuse policy is available. Nondeterminism raises `DBOSStepNondeterminismError`. Timeouts are durable and start-to-completion.
- **LangGraph (S018).** Durability modes are `exit`, `async` and `sync`. With `async`, "there is a small risk that LangGraph does not write checkpoints if the process crashes during execution". Replay re-triggers LLM and API calls.
- **AWS (S027).** Retries are "selfish". "If each layer retries independently, the load on the database will increase 243x". Use single-layer retries, token-bucket retry budgets and jitter.
- **Kleppmann (S028).** Distinguish efficiency locks from correctness locks. A lease needs a fencing token that the resource itself checks.
- **Stop Means Stop (S023, 2026-07 preprint).** Approval, cancel and timeout primitives lack barrier semantics: "This contract holds on none of six widely used open-source frameworks." The failure modes are sibling leak, replay double-execution, cancellation orphans and timeout zombies.

### 2.6 Failure research and telemetry
- **MAST (S021).** "14 unique modes, clustered into 3 categories", from 1600+ traces, κ = 0.88.
- **Who&When (S022).** "The best method achieves 53.5% accuracy in identifying failure-responsible agents but only 14.2% in pinpointing failure steps".
- **OTel GenAI (S020).** Operation names include `invoke_agent`, `invoke_workflow`, `execute_tool` and `plan`. "the corresponding span SHOULD cover the duration of the logical operation with all retries". Status: Development.

---

## 3. `SOURCES.md` rows (30; contract columns; all opened 2026-10-19)

Wave-2 note on `kind`: the enum has no `article` value. First-party engineering posts are filed as `docs` and independent expert essays as `community` (see defect C1).

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | MCP spec Key Changes 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28/changelog | spec | A | Stateless MCP core: no handshake or sessions, server/discover, MRTR, tasks as extension, no SSE redelivery, cacheable lists, deprecations with 12-month window | queued | 2026-10-19 | on-release | — |
| S002 | MCP spec Key Changes 2025-11-25 — https://modelcontextprotocol.io/specification/2025-11-25/changelog | spec | A | Prior revision: experimental tasks (SEP-1686), URL elicitation, CIMD, tool-name guidance, JSON Schema 2020-12, input errors as tool errors | queued | 2026-10-19 | 365d | — |
| S003 | A2A Protocol Specification (latest = 1.0.0) — https://a2a-protocol.org/latest/specification/ | spec | A | A2A task lifecycle (terminal COMPLETED/FAILED/CANCELED/REJECTED; interrupted INPUT/AUTH_REQUIRED), proto-normative schema, AUTH_REQUIRED is not authorization | watch | 2026-10-19 | on-release | — |
| S004 | oh-my-pi docs/tools/task.md — https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md | docs | A | OMP task contract: batch shape, solutionSpace, speculative launch, semaphore 32, idle TTL 7 min, depth 2, budgets, yield retries, isolation PAL, merge modes | queued | 2026-10-19 | on-release | — |
| S005 | oh-my-pi docs/agent-hub.md — https://github.com/can1357/oh-my-pi/blob/main/docs/agent-hub.md | docs | A | Agent Hub: running/idle/parked/aborted, revive-on-message, kill tombstones, agent:// vs history://, advisors are observers not peers | queued | 2026-10-19 | on-release | — |
| S006 | oh-my-pi docs/task-agent-discovery.md — https://github.com/can1357/oh-my-pi/blob/main/docs/task-agent-discovery.md | docs | A | Task agent discovery: source precedence, first-wins by exact name, model/schema/tier/account-pool precedence, before_subagent_spawn hook | queued | 2026-10-19 | on-release | — |
| S007 | Claude Code: Run parallel sessions with worktrees — https://code.claude.com/docs/en/worktrees | docs | A | Worktree isolation contract and failure modes: locks, sweep, LFS filter-driver skip, symlink and core.worktree refusals, four enforcement checks | queued | 2026-10-19 | 30d | — |
| S008 | Claude Code: Orchestrate subagents at scale with dynamic workflows — https://code.claude.com/docs/en/workflows | docs | A | Script-held orchestration: who holds the plan, resumable runs, cross-checked claims, unverified-not-refuted on rate limits, ultracode gating | watch | 2026-10-19 | 30d | — |
| S009 | git-worktree documentation (2.56.0 page) — https://git-scm.com/docs/git-worktree | docs | A | Linked worktrees: lock/prune/repair/move semantics, --lock race-free, relative-path extension, BUGS: multi-checkout experimental, submodules incomplete | queued | 2026-10-19 | on-release | — |
| S010 | Codex CLI Developer commands — https://learn.chatgpt.com/docs/developer-commands?surface=cli | docs | A | Codex CLI: exec/fork --worktree constraints, /worktree and /subagents, codex mcp stores servers in ~/.codex/config.toml | queued | 2026-10-19 | 30d | — |
| S011 | Kimi Code CLI Docs: Model Context Protocol — https://moonshotai.github.io/kimi-code/en/customization/mcp.html | docs | A | Kimi MCP client: mcp.json user/project levels, trust gating in headless runs, deferred tool loading, mcp__server__tool permissions | queued | 2026-10-19 | on-release | — |
| S012 | Kimi Code CLI Docs: Agents and Sub-Agents — https://moonshotai.github.io/kimi-code/en/customization/agents.html | docs | A | Kimi sub-agents: built-ins, depth allowlist, discovery precedence, recursive scan, frontmatter fields, unknown fields ignored, wire.jsonl storage | queued | 2026-10-19 | on-release | — |
| S013 | Kimi Code CLI Docs: Configuration files — https://moonshotai.github.io/kimi-code/en/configuration/config-files.html | docs | A | Kimi config.toml reference: secondary_model resolution and force, subagent/swarm timeouts, print-mode background steering, mcp timeouts | queued | 2026-10-19 | on-release | — |
| S014 | Kimi Code CLI Docs: Tower multi-agent collaboration — https://moonshotai.github.io/kimi-code/en/guides/tower.html | docs | A | Kimi Tower: one coordinator per workspace, branch and worktree per mission, independent review merge gate, mode exclusivity, not a sandbox | queued | 2026-10-19 | on-release | — |
| S015 | OpenAI Agents SDK: Handoffs — https://openai.github.io/openai-agents-python/handoffs/ | docs | A | Handoffs as transfer_to tools; guardrail scope; input filters; nested history does not redact; no filters on server-managed conversations | watch | 2026-10-19 | 90d | — |
| S016 | Temporal: Activity Definition (Idempotency) — https://docs.temporal.io/activity-definition | docs | A | At-least-once activities, partial completion, idempotency keys from Run ID plus Activity ID, never hand-roll retries inside activities | queued | 2026-10-19 | 180d | — |
| S017 | Temporal: Detecting Activity failures — https://docs.temporal.io/encyclopedia/detecting-activity-failures | docs | A | Timeout taxonomy: Start-To-Close detects worker crash, Schedule-To-Start non-retryable, heartbeats carry progress and cancellation | queued | 2026-10-19 | 180d | — |
| S018 | LangGraph: Checkpointers (durability modes) — https://docs.langchain.com/oss/python/langgraph/checkpointers | docs | A | Checkpoint durability modes exit/async/sync and their crash windows; pending writes; replay re-triggers LLM and API calls | watch | 2026-10-19 | 90d | — |
| S019 | DBOS: Workflows tutorial — https://docs.dbos.dev/python/tutorials/workflow-tutorial | docs | A | Workflow ID as idempotency key with reject reuse policy; determinism rule and nondeterminism error; durable timeouts; step guarantees | watch | 2026-10-19 | 90d | — |
| S020 | OpenTelemetry semconv: generative client AI spans — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md | spec | A | GenAI span conventions: operation names incl. invoke_agent/execute_tool/plan, spans cover all retries, error.type; Development status | watch | 2026-10-19 | on-release | — |
| S021 | Cemri et al., Why Do Multi-Agent LLM Systems Fail? (MAST) — https://arxiv.org/abs/2503.13657 | paper | A | MAST: 14 multi-agent failure modes in 3 categories from 1600+ traces, kappa 0.88, LLM-judge annotator | queued | 2026-10-19 | 365d | — |
| S022 | Zhang et al., Which Agent Causes Task Failures and When? (Who&When) — https://arxiv.org/abs/2505.00212 | paper | A | Automated failure attribution; best method 53.5% agent-level and 14.2% step-level accuracy | queued | 2026-10-19 | 365d | — |
| S023 | Khan, Stop Means Stop: the enforcement gap in agent-framework control primitives — https://arxiv.org/abs/2607.14166 | paper | A | Approval gates, cancellation and timeouts lack barrier semantics in 6 of 6 frameworks: sibling leak, replay double-exec, orphans, zombies (2026 preprint) | watch | 2026-10-19 | 90d | — |
| S024 | Anthropic: How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system | docs | A | Orchestrator-worker research system: token usage explains 80% of variance, about 15x tokens, delegation spec, filesystem artifacts, rainbow deploys | queued | 2026-10-19 | 365d | — |
| S025 | Anthropic: Effective harnesses for long-running agents — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | docs | A | Long-running harness: initializer plus coding agent, progress file plus git log, JSON feature list, premature-victory failure modes | queued | 2026-10-19 | 365d | — |
| S026 | Cognition: Don't Build Multi-Agents (Walden Yan) — https://cognition.com/blog/dont-build-multi-agents | community | B | Counterpoint: share full traces; actions carry implicit decisions; parallel writers produce conflicting work | queued | 2026-10-19 | 365d | — |
| S027 | AWS Builders' Library: Timeouts, retries, and backoff with jitter — https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter | docs | B | Retries are selfish: capped backoff, jitter, single-layer retries (243x amplification), token-bucket retry budgets, idempotent APIs | queued | 2026-10-19 | 365d | — |
| S028 | Kleppmann: How to do distributed locking — https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html | community | B | Efficiency vs correctness locks; leases need fencing tokens checked by the resource; timing assumptions break lock safety (2016, still canonical) | queued | 2026-10-19 | 365d | — |
| S029 | MCP Security Best Practices (2026-07-28 docs) — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices | docs | A | REJECTED for this lane: OAuth confused deputy, token passthrough and session hijacking are security-province work; report to kasegi/kagi, do not absorb | rejected | 2026-10-19 | 365d | — |
| S030 | LangGraph: Persistence overview — https://docs.langchain.com/oss/python/langgraph/persistence | docs | A | REJECTED: locator drift; the durable-execution URL now redirects to this overview, which omits the durability semantics; cite S018 instead | rejected | 2026-10-19 | 365d | — |

Counts:
- Rows → 30: `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md`.
- Tiers → A 27, B 3, C 0 (A includes the 2 rejected rows): the contract's `awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`.
- Status → queued 21, watch 7, rejected 2: `grep -E '^\| S[0-9]{3} ' corpus/SOURCES.md | awk -F'|' '{gsub(/ /,"",$7); print $7}' | sort | uniq -c` (checked against this dossier's table on 2026-10-19).

**Opened but held back.** These are row-ready next round; I left them out to respect the 30-row cap:
- OMP README (31 tools, `pi-iso` backends, `mcp.enableProjectConfig` overlay): https://github.com/can1357/oh-my-pi
- Claude Code "Run agents in parallel": https://code.claude.com/docs/en/agents
- MCP 2026-07-28 release post (maintainer rationale for server-minted handles): https://blog.modelcontextprotocol.io/posts/2026-07-28/
- "MCP joins the Agentic AI Foundation": https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/
- Temporal OpenAI Agents SDK integration (TS: "model calls are executed as Activities, so they retry durably and are not repeated during Workflow replay"): https://docs.temporal.io/develop/typescript/integrations/openai-agents
- Anthropic "Building effective agents" (2024-12-19, canonical workflows-vs-agents vocabulary; the page now says its tooling landscape has changed): https://www.anthropic.com/engineering/building-effective-agents
- AGENTS.md: https://agents.md/

## Leads (unopened)
- **OMP docs.** I opened the directory index; these files are not yet read: `mcp-protocol-transports.md`, `mcp-runtime-lifecycle.md`, `mcp-config.md`, `collab.md`, `advisor-watchdog.md`, `non-compaction-retry-policy.md`, `handoff-generation-pipeline.md`, `natives-rust-task-cancellation.md`. All live under https://github.com/can1357/oh-my-pi/tree/main/docs.
- **`omp://` harness docs on this host.** They match the installed `omp/18.12.3`; the GitHub docs above track `main`. Harness policy says avoid unless asked, so this needs an explicit ask.
- **MCP.** The tasks extension spec, the MRTR page (https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr), the feature-lifecycle policy (https://modelcontextprotocol.io/community/feature-lifecycle) and the deprecated-features registry (https://modelcontextprotocol.io/specification/2026-07-28/deprecated).
- **Microsoft Agent Framework primary docs.** learn.microsoft.com/agent-framework and github.com/microsoft/agent-framework. Search surfaced only secondary coverage of the 1.0 release on 2026-04-03.
- **Google ADK docs.**
- **Restate and Inngest (AgentKit)** durable-execution docs.
- **Temporal.** Workflow versioning/patching docs (the deploy-during-run failure mode, cf. S024's rainbow deploys). Temporal blog "Idempotency and durable execution": https://temporal.io/blog/idempotency-and-durable-execution
- **Claude Code.** Sub-agents (concurrent subagent limit): https://code.claude.com/docs/en/sub-agents. Agent teams: https://code.claude.com/docs/en/agent-teams. Hooks reference (`WorktreeCreate`/`WorktreeRemove`).
- **Anthropic.** "Effective context engineering for AI agents" (2025-09), "Writing effective tools for agents" (2025-09), "Code execution with MCP" (2025-11), "Harness design for long-running application development" (2026-03). The last is named, per a search snippet, in https://github.com/anthropics/cwc-long-running-agents.
- **Kimi Code docs.** Hooks, env-vars (`KIMI_CODE_TRUST_WORKSPACE`, `KIMI_SUBAGENT_TIMEOUT_MS`), plugins, and the `/tower` slash-command reference.
- **OTel GenAI agent-spans doc.** The sibling of S020, likely `docs/gen-ai/gen-ai-agent-spans.md`; path unverified.
- **Papers.** arXiv 2606.31498 "Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express". ACL 2026 "Seeing the Whole Elephant" failure-attribution benchmark: https://aclanthology.org/2026.acl-long.912.pdf
- **Datasets and code.** MAST: https://github.com/multi-agent-systems-failure-taxonomy/MAST. Who&When: https://github.com/mingyin1/Agents_Failure_Attribution
- **Platform docs.** Linux kernel overlayfs docs (semantics behind OMP's isolation backend). git 2.48 release notes (relative worktrees).

---

## 4. Candidate knowledge entries (6)

Bar used. The lane has no `corpus/QUALITY.md`, so each entry is measured against the fleet bar:
- **Header (CORPUS.md:17; LEARNING.md:61-62).** The entry opens with `source:`, `verified-at:` and `recheck:`, where `recheck:` is "the command or citation that re-verifies it".
- **Citation (CORPUS.md:23).** It cites a source.
- **Falsifiability (CORPUS.md:25).** It is "falsifiable or marked opinion".
- **House rule (`corpus/README.md:178`).** "All entries are falsifiable and cite file+symbol." For external sources I map this to URL + section heading + ≤25-word quote + pinned version or fetch date.

Every candidate below fills ground the coverage map does not hold, which matches LEARNING.md:30 (expansion: "net new admitted entries on uncovered ground, each citing its coverage-map row").

**K1 — `omp-task-hub-contract`** (fills: new coverage-map row "OMP task/hub upstream contract"; first scope in `PROVINCE.md:3`; upstream-citation sweep → 0)
- **Claim (falsifiable).**
  - On `main` docs at fetch time, OMP bounds every spawn with one session semaphore `task.maxConcurrency` (default 32), parks idle agents after `task.agentIdleTtlMs` (default 420 000 ms) and caps `task.maxRecursionDepth` at 2.
  - Registry statuses are exactly `running`/`idle`/`parked`/`aborted`, and messaging a parked or killed agent revives it.
- **Cross-checks against the lane.** These can fail independently, which is what makes them useful.
  - `SKILL.md:20` gives `concurrencyCeiling` 32 (`CONCURRENCY_CEILING`), equal to OMP's default. [INFERENCE] The ufo ceiling mirrors the harness default, so an upstream change would desync them silently.
  - `SKILL.md:487-489` (AP4, resume = `write agent://<id>` revives the parked agent) is consistent with S005.
  - New hazard for AP2/AP3: speculative launch starts batch items before the call finishes streaming, and an invalid finished call then aborts them.
- **Sources and quotes.**
  - S004, "Limits & Caps": "Idle TTL: `task.agentIdleTtlMs`, default `420_000` ms (7 min); `<= 0` disables parking and keeps idle sessions live until exit."
  - S004, "Modes / Variants": "an invalid finished call, launched items that differ from the finished call, a blocking hook, or an aborted turn aborts every launched run".
  - S005, "Roster and inspector": "status (`running`, `idle`, `parked`, or `aborted`), agent identity, parent, and unread IRC count"
  - S005, "Related surfaces": "Messaging a parked or killed subagent revives it."
- **Recheck.** `curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/tools/task.md | grep -cE 'agentIdleTtlMs|maxConcurrency|maxRecursionDepth'` → 5 (2026-10-19). Pin `omp --version` → `omp/18.12.3`. Version skew between docs on `main` and the installed binary remains a named gap; the `omp://` lead would close it.
- **Bar.** Tier-A upstream docs with section anchors. Defaults are numeric and falsifiable. `verified-at:` = 2026-10-19 + `omp/18.12.3`.

**K2 — `kimi-mcp-plane`** (fills: coverage-map K1 config-plane row, new member `mcp.json`; `SCORECARD.md:137` lists only config.toml, tui.toml and the .bak chain)
- **Claim.**
  - Kimi Code reads MCP servers only from `mcp.json`: user `~/.kimi-code/mcp.json` and project `.kimi-code/mcp.json`, with the project entry winning on a shared name.
  - The `config.toml` `[mcp]` table documents only `startup_timeout_ms`, `tool_timeout_ms` and `default_deferred`, and no `mcp_servers` section is documented. That grounds the `kimi doctor` line at `kimi-modes-machinery.md:67-70` ("Unknown top-level key ignored by the v2 engine: mcp_servers").
  - [INFERENCE] The inert `[mcp_servers.rea]` table follows the Codex dialect.
  - Headless `kimi -p` keeps project-level servers off unless the workspace is trusted.
- **Sources and quotes.**
  - S011, "Configuration": "MCP server configuration is written in `mcp.json`, at two levels". Same section: "project-level MCP servers stay disabled there unless the workspace is already trusted".
  - S013, "`mcp`": the three-key table.
  - S010, "`codex mcp`": "Manage Model Context Protocol server entries stored in `~/.codex/config.toml`."
- **Recheck.**
  - `curl -fsSL https://moonshotai.github.io/kimi-code/en/customization/mcp.md | grep -c 'mcp.json'` → 7.
  - `node scripts/kimi-census.mjs` → `UNLISTED mcp.json` today.
  - `grep -rlF 'mcp.json' SKILL.md corpus | wc -l` → 0 → ≥1 once admitted.
- **Bar.** Tier-A docs plus a host observation; the inference is labelled. Secrecy: S011 lists `env`, `headers` and `bearerTokenEnvVar` fields, so the file must be treated as shape-only (stat, never read), like the census's secret members.

**K3 — `kimi-subagent-model-resolution`** (fills: coverage-map K2 delegate-plane row; closes the UNKNOWN at `kimi-lane-definitions.md:227-231`, "file vs registry precedence … unverified")
- **Claim.**
  - Kimi resolves a subagent's model as (1) the explicit tool-call `model`, then (2) `[secondary_model].default_model`. `force = true` pins every spawn and rejects an explicit `model`.
  - Agent files have no model field, and unknown frontmatter fields are ignored. So the "ALWAYS spawn with model …" pin inside each `description:` (`kimi-lane-definitions.md:34-37`) is advisory prose to the dispatching agent, not a binding. `kimi-lane-definitions.md:7` ("pinning one provider/model") over-claims; see mistake M1.
  - Tower workers take `default_model`, while reviewers stay on the primary model unless `force = true`.
  - `~/.kimi-code/agents/` is scanned recursively, so `agents/secondary/*.md` load as user-scope agents.
- **Sources and quotes.**
  - S013, "Subagent model pool": "A spawn resolves the subagent's model in this order: 1. An explicit `model` passed in the tool call 2. `default_model`"
  - S012, "Agent File Format": "Unknown fields are ignored, so newer files stay readable by older versions."
  - S014, "Mode exclusivity and secondary model": "`TowerSpawn` currently does not support selecting a model for an individual mission or spawn."
- **Recheck.** `curl -fsSL https://moonshotai.github.io/kimi-code/en/configuration/config-files.md | grep -n "resolves the subagent's model"` → line 240 (2026-10-19). Host behaviour is unverified: the docs track current Kimi, while the host binary is the sha-pinned v2.1.1 per `kimi-binary-secrets.md`. A spawn probe would falsify it.
- **Bar.** Tier-A docs. The entry turns a recorded UNKNOWN into a documented, falsifiable rule and labels the remaining host-version gap.

**K4 — `lock-classes-and-fencing`** (fills: Frontier row "distributed-systems grounding for lock/lease/idempotency machinery"; the framework sweep returned only 1 incidental hit)
- **Claim.** Kleppmann asks whether a lock exists for efficiency or for correctness, and that splits the lane's two lock families:
  - `acquireSingletonLock` (pid + starttime + bootId; `SKILL.md:513-518`) prevents duplicate daemons, i.e. double-fired ladders. That is an efficiency/ladder guard.
  - The `lease.rs` writer lease is a correctness lock. Its `epoch` is a monotone fencing token (`runtime-support.md:113`), but the writer checks it by re-reading the lease around the write (`guarded_write`, `runtime-support.md:134-137`); the resource itself never checks it. Kleppmann's safety condition is unmet by design.
  - The lane's own line "the closure may already have committed" (`runtime-support.md:137`) is therefore the expected residual: the lease detects a stale write, it does not prevent one.
  - Falsifier: a resource-side epoch check in a `publish_guarded` consumer.
- **Source and quote.** S028, "Making the lock safe with fencing": "Note this requires the storage server to take an active role in checking tokens, and rejecting any writes on which the token has gone backwards."
- **Recheck.** The source is canonical (2016), so 365d. Internal: `grep -n 'closure may already have committed' corpus/knowledge/runtime-support.md` → 137. `node scripts/cite-check.mjs` must stay CLEAN on the new note.
- **Bar.** A B-tier canonical source joined to A-tier internal anchors. The entry is marked analysis, falsifiable by the named counter-evidence.

**K5 — `mcp-2026-07-28-delta`** (fills: Frontier row "MCP spec revisions"; the lane holds only config facts)
- **Claim.**
  - Relative to 2025-11-25, revision 2026-07-28 removes the handshake, sessions, `ping` and `logging/setLevel`. It removes SSE resumability, so lost in-flight requests are re-issued under new IDs. It moves tasks to an extension (`tasks/get` polling, `tasks/update`, no `tasks/list`), introduces MRTR and a required `resultType`, deprecates Roots/Sampling/Logging with a ≥12-month window, and reserves −32020…−32099.
  - [INFERENCE] For orchestrators, tool-call retries after a stream loss become fresh requests, so server-side tool idempotency (S016's discipline) moves from nice-to-have to required.
- **Source and quote.** S001, Major changes #9: "A broken response stream loses the in-flight request; clients **MUST** re-issue it as a new request with a new request ID".
- **Recheck.** `curl -fsSL https://modelcontextprotocol.io/specification/2026-07-28/changelog.md | grep -oE 'SEP-[0-9]+' | sort -u | wc -l` → 14 (2026-10-19). Re-run on the next revision.
- **Bar.** Spec-primary and enumerable. The inference is labelled.

**K6 — `isolation-substrates`** (fills: Frontier row "isolation substrates"; the lane holds only tower-skill worktree rules, `kimi-modes-machinery.md:205-216`)
- **Claim.** The four substrates the fleet touches guarantee different things:
  - git linked worktrees share `.git`, multi-checkout is still experimental, and submodule support is incomplete.
  - Claude Code holds `git worktree lock` while an agent runs and skips repo filter drivers (LFS arrives as pointer files).
  - OMP `isolated` tasks are not git-worktree-only: they use a PAL with 9 backend values plus patch or branch merge.
  - Kimi Tower worktrees "are not a security sandbox".
  - Falsifiers: OMP isolation that requires git worktrees; git dropping the BUGS caveat.
- **Sources and quotes.**
  - S009, "BUGS": "Multiple checkout in general is still experimental, and the support for submodules is incomplete."
  - S004, "Modes / Variants": "`isolation.backend` selects `auto`, `apfs`, `btrfs`, `zfs`, `reflink`, `overlayfs`, `projfs`, `block-clone`, or `rcopy`".
  - S007, "Clean up subagent and background-session worktrees": "While an agent is running, Claude Code holds a `git worktree lock` on its worktree so that concurrent cleanup can't remove it".
  - S014, "Safety and resource cost": "Worktrees isolate writes, but they are not a security sandbox."
- **Recheck.**
  - `curl -fsSL https://git-scm.com/docs/git-worktree/2.54.0 | grep -c 'Multiple checkout in general is still experimental'` → 1. The host runs `git 2.55.0`, and the docs show no worktree change in 2.55.
  - `curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/tools/task.md | grep -c 'isolation.backend'` → 3.
- **Bar.** Four tier-A docs, each claim tied to its own falsifier.

---

## 5. `## Paths`
- **MCP revision literacy.** S002 → S001 → S011 → S013 → S010. Learn the revision delta first, then how the host's two documented MCP clients consume servers. That makes the inert `[mcp_servers]` table explainable rather than just observed.
- **Durable orchestration failure modes.** S027 → S016 → S017 → S019 → S018 → S028 → S023. Start with generic retry and idempotency economics, move through engine contracts (Temporal, DBOS, LangGraph), then lock safety, and end at the agent-specific enforcement gap. Each step names a failure class that the lane's queue, lease and watchdog code already handles or misses.
- **Multi-agent architecture judgment.** S024 → S026 → S025 → S021 → S022 → S008 → S004 → S005. Start with the design debate, then long-running harness practice, then measured failure taxonomies. End at the concrete harness contracts the fleet actually runs.

---

## 6. Rejected candidates (with reasons)
1. **S029, MCP Security Best Practices (opened).** Its content (OAuth proxies, token passthrough) belongs to the security province (kasegi/kagi). One domain per shokunin: report it, do not absorb it.
2. **S030, LangGraph Persistence page (opened).** The old durable-execution locator now redirects here, and the page omits the semantics. Keep the rejection as evidence of locator hygiene and cite S018.
3. **Secondary write-ups of S024** (ZenML LLMOps DB, Simon Willison, ByteByteGo, ai.plainenglish). Seen only in search results; never opened. They are secondary to an opened primary, so tier C at best and never sole support.
4. **Microsoft Agent Framework via secondary coverage** (Visual Studio Magazine, personal blogs). Not admitted until the primary docs are opened; kept as a lead.
5. **Tertiary MCP timelines** (hidekazu-konishi, the WorkOS explainers). Seen in search; the spec changelogs S001 and S002 are primary. Rejected unopened.
6. **A2ABreak (arXiv 2609.10871) and OWASP agentic top-10.** Security analyses, so adjacency (kasegi). Unopened.
7. **Airflow, Dagster, Prefect.** Rejected by scope. These batch DAG schedulers fail through scheduler latency and DAG parsing, which does not model long-lived agent missions; Temporal, DBOS and LangGraph cover durable agent state.
8. **Entry idea: "framework comparison matrix".** Rejected because it is not falsifiable against the lane's substrate: it describes frameworks the fleet does not run. Prefer contracts of the harnesses on the host (K1–K3).
9. **Entry idea: "adopt A2A for fleet messaging".** Rejected because the fleet has no A2A endpoint. This would be design speculation, not knowledge.

---

## 7. Defects and mistakes surfaced (for STATE and wave 2)

**Lane defects (D):**
- **D1.** No `corpus/QUALITY.md` (`test -e corpus/QUALITY.md; echo $?` → 1), although `SCORECARD.md:673-676` pre-registers a QUALITY.md admissions gate.
- **D2.** PROVINCE.md is 326 B with 0 Core/Frontier/Adjacent headings, against LEARNING.md:68-70.
- **D3.** `corpus/README.md` has 0 `## Frontier` headings, against LEARNING.md:59-60.
- **D4.** 0 of 38 knowledge entries carry `source:`/`recheck:` headers, against CORPUS.md:17.
- **D5.** The census reports DRIFT: `UNLISTED mcp.json` and `UNLISTED skills/` (6 children, 5 declared).

**Mistakes mined (M):** lane claims the external art contradicts or leaves ungrounded.
- **M1.** `kimi-lane-definitions.md:7` says "pinning one provider/model". Per S012 and S013 the description pin is advisory; only the tool-call `model` or `[secondary_model]`/`force` binds.
- **M2.** The UNKNOWN at `kimi-lane-definitions.md:227-231` stayed open while a tier-A doc answered it. The curation step of the learning path was skipped.
- **M3.** The province's first scope ("OMP task/hub") has 0 upstream citations. All 38 entries were learned from the consumer side only.
- **M4.** The census's frozen K1–K5 set omits the documented MCP surface. It measured the files the author knew, not the surfaces the product documents.
- **M5. Category error: URL as endpoint vs URL as source.** The Kimi docs site, which documents the lane's own round-18 orchestration surfaces (S011–S014), appeared only as a binary-string pointer. Its changelog was routed to kama as an "Endpoint" (`kimi-binary-secrets.md:321-327`) instead of being mined as the tier-A source for `kimi-*.md`. Proposed QUALITY criterion: "a vendor docs URL found in a binary is a source lead first, an endpoint second".

**Contract and external (C):**
- **C1.** The `SOURCES.md` `kind` enum lacks `article`/`post`. Engineering posts get shoehorned into `docs` or `community`. This needs a decision from the D3 owner.
- **C2.** Kimi's config doc contradicts itself on timeouts. The `[subagent]`/`[swarm]` `timeout_ms` table default is `7200000` (2 hours), while the print-mode paragraph says "subagents run without a timeout (`[subagent] timeout_ms` and `[swarm] timeout_ms` both default to `0` unless explicitly set)" (S013). The host pins `7200000` explicitly (`kimi-config-plane.md:252-253`; generation 3→4 changed `0 → 7200000` at `:340`). The fleet's headless Kimi lanes are safe only while that pin holds.

**Hand-off to wave 2 (scope, not a claim).**
- **ART work alone cannot carry the lowest axis.** The lowest non-retired axis is operability at 8 (`SCORECARD.md:306`), and the next integer needs A+C ≥ 27 from 17.
- **One gate is not enough.** A single offline `SOURCES.md` row-grammar gate plus its checklist item gives 19/22 ≈ 0.864, still 8.
- **Where ART fits.** The expansion, quality and discernment axes already appear as `unchanged` rows at `SCORECARD.md:1555-1557`, or a new coverage row family. The STATE dossier owns the round design.
