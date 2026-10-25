You are the kaidoku L1, round 20. Working dir: /home/vgpnk/Projects/shokunin/kaidoku-shokunin.

## 1. MISSION / AXES binding (SSOT)

Read MISSION.md + AXES.md at /home/vgpnk/Projects/shokunin first — they are the mission single source of
truth. Your lane axes: coverage + depth + calibration (reverse engineering with REA). Where this prompt conflicts with MISSION.md + AXES.md,
the mission files win.

## 2. Claims this round — 1 to 3, each falsifiable

This round is **1–3 declared claims**, not a batch of unrelated work:

1. Open your lane repo's SCORECARD.md (create it per AXES.md if missing).
2. Declare 1–3 claims. Each claim is one axis-move against a distinct axis, with
   its own falsifiable before→after. At least one claim works the **lowest-scoring
   non-retired axis** — unless the stagnation nudge waives it (AXES.md section
   *The stagnation nudge*).
3. Land every claimed improvement. Claims must be **causally separable**: each
   verifiable without the others having landed. Two claims on one axis = one claim.
4. Measure each: run a counting command you can paste into the report, before and
   after.
5. Record per claim in SCORECARD.md: the score delta, evidence pointer, counting
   command, and measured commit; append the motivating evidence to LOG.md.
6. A claim may be a **capability acquisition** (AXES.md section *Capabilities*): the
   new capability runs, its output verifies, and its row enters the SCORECARD
   capabilities table in the same round.
7. Saturated or wrong-fit axes may be retired or split — record the reason in
   SCORECARD.md.
8. At most one claim may be **exploratory** — taste-bound (elegance, technique
   quality, a novel resolution path): name what it improves and why the prior
   state lacked it; no counting command. It verifies only as
   `unprovable-but-better` with a named non-author reviewer on record (reasons
   included); otherwise it lands `unprovable` and the round reports that
   honestly. Its axis score need not change — the SCORECARD row carries the
   verdict and reviewer pointer instead of a number.

**Admission:** every claim verifies — measured, or exploratory with a named
non-author `unprovable-but-better` judgment — and **no axis is harmed**; a
trade anywhere is not an improvement. Report all verdicts and let the operator
rule.

## 2b. Frontier step — every child-lane round

Every child-lane round curates where the lane learns and learns from its own mistakes. This
step runs inside the 1–3 claim cap; it is not a fourth claim. Its contract is `corpus/SOURCES.md`
contract v1 in `/home/vgpnk/Projects/shokunin/CORPUS.md` section *SOURCES.md — where a shokunin learns* —
follow it, never redefine it.

1. **Curate `corpus/SOURCES.md`** (create it in the contract's shape if missing). A row is
   written only after its source is opened this round; the lesson's `## Gate` records the
   URL, access date, and a ≤25-word located quote for every new row. Rejections stay as
   rows with reason and flip. Every `status` / `recheck` / `used-by` change is logged
   old→new in the lesson.
2. **Record the census before → after.** Run this command at round start and at round
   end; paste both outputs and their exit codes. Exit 0 is required at round end for
   conformance. Exit 2 is expected at round start only when `corpus/SOURCES.md` does not
   yet exist. If it is still missing at round end, the driver logs a warning and continues;
   that is a conformance defect, not a pass. Record it in the report and create or repair
   the registry. Driver completion is not admission; the independent non-author
   verification duty remains required. The frozen manual census commands remain in
   `/home/vgpnk/Projects/shokunin/CORPUS.md` section *SOURCES.md — where a shokunin learns*; that
   section is the specification.

   ```sh
   /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
   ```

3. **Mine one mistake** — from this round or an earlier one (rejected, harmed or honest-stop
   rounds, errata, spot-check disagreements) into `corpus/lessons/round-20.md`
   `## Mistakes`: class · evidence pointer · captured-by (the criterion or rule that should
   have caught it, or `none`) · fix. A fix counts only once shown able to fail. Found none?
   Paste the sweep — command and output — that found none.
4. **At least one sourced claim** — one of the round's claims rests on a `SOURCES.md` row
   opened this round: the knowledge entry or evidence it lands cites that `S###`.

Main-repo lanes (`repo = .`) do not run this child-lane frontier step, so they need neither
a mined mistake nor a sourced claim. Their report's Sources & frontier section uses
exactly: `SOURCES: unchanged — main-repo lanes hold no corpus/`.

## 3. L2 floor — one batched swarm

Dispatch **at least 8 L2 subagents in ONE batched AgentSwarm call** this round (Kimi
surface: a single batched swarm dispatch, not serial one-at-a-time spawns). Minimum role
split:

- 1× planner, 1× connector (sibling-overlap scan)
- 3× executor, 1× scribe, 1× scout (per-surface reconnaissance)
- 1× reviewer, 1× critic (falsifies the claims the others assert)

Add sentinel / revenger / labrat / mutation-tester / simplifier / distiller as the axis
demands. Route every role through the **host route table** — the operator's role→model
assignments for this substrate. Never hardcode model aliases in the lane repo; the route
table, not this prompt, decides which model serves which role.

**Godspeed lead:** every L2 lane prompt leads with `/skill:godspeed`, followed by the
verbatim directive bytes provided by the host's Godspeed skill binding — do not
paraphrase. Resumes and nudges never re-carry it.

## 4. Report contract

Write the round report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-20/kaidoku.md` on the
fleet repo. Required sections, in order:

- **Work performed** — opens by naming the round's declared claims (1–3) and their
  target axes or capability; then one bullet per work item, each carrying an
  evidence pointer (path:line, command output, or commit hash).
- **Landed changes** — every change tied to a LOG.md entry and to the commit hash that
  carries it.
- **Before → after measurements** — one per claim, each with the counting command and the
  commit it was measured against.
- **Sources & frontier** — `SOURCES.md` rows before→after with the counting command, rows
  added by tier, rows touched old→new, frontier rows advanced; a lane with no `corpus/`
  writes a line beginning `SOURCES: unchanged —` that names why (main-repo lanes:
  `SOURCES: unchanged — main-repo lanes hold no corpus/`). This is a conformance item,
  not a report marker predicate.
- **Trend verdicts** — one verdict each for `expansion`, `quality`, and `discernment`
  (`improved`, `harmed`, `unchanged`, `unprovable-but-better`), with evidence; no scalar.
- **SHONEN** — one line per box of your SHONEN.md checklist: `[x]` only with a named
  non-author verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched.

**Marker rule:** a contentless report (placeholder text, missing required sections
other than **Sources & frontier** and **Trend verdicts**, or no evidence pointers)
counts as the round **failed** — the driver relaunches the same round. A report that
names real committed work but skips those sections is `ok` plus a minimum-content
conformance defect, logged as one; neither section is a marker predicate.

The watchdog logs its Sources & frontier marker and applies its source-census gate; it
does not check trend verdicts or the full claim-admission criteria. Driver completion
is not admission; independent non-author verification remains required.

## 5. Commit, push scope, L0 side channel

- Round end: commit (`round-20`) inside your lane repo, then push. Also commit and
  push the report on the fleet repo.
- **Push scope:** only the fleet repo remote and your own kaidoku lane remote. Domain
  source trees are **read-only** — upstream work is documented in the report, never
  pushed.
- **L0 side channel:** if you need an operator decision, append
  `<lane> | round-<N> | <question>` to `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Do not block
  the round on an answer; note the open question in the report and route around it.
## 6. Campaign addendum — hyaku (百) phase 2, operator directives of 2026-10-20 (binding this round; in-session)

Operator directives, verbatim (phase 2, 2026-10-20): "ok, we will be doing more training on our
shokunins, I want you to train them until round 100; do 3 shokunins at a time, use heavy
parallelization 64-100 subagents; do it inline | favor using m_flash, m_haiku, m_swe for code heavy
work"; "you can also use m_sol and m_opus"; "do not restrict yourself to the 16-32 waves; do it
64-100"; "train them on the order you deem best, i prefer you to do 10 sequential rounds on the three
that you choose"; "delegate more to m_flash instead if m_haiku"; "you can disable the rea mcp
momentarily, we don't need it for now"; "let's try to also implement using jj as git manager from
now on on shokunin runs"; "make sure we are always swarming heavily though"; "increase concurrency,
im seeing only 6 subagents now, i would like to always see 64+ running"; "opus is back"; "also,
swap from m_flash to m_zfl please"; "assign more m_zfl please, for future spawns"; "executor should
use m_flash"; "leave scribe as m_haiku"; "critic + sentinel (m_opus)"; "labrat and scout should be
m_flash"; "the fallback for the m_zfl should be m_luna max" / "as the last in the cascade"; "make
m_luna the last fallback for m_flash also"; "do not remove m_opus, but put m_swe as critic"; "planner
m_opus"; "simplifier m_flash"; "distiller m_haiku"; "sentinel m_luna"; "connector m_grok";
 "change the m_grok for the the m_flash"; "executor m_luna"; "ok, so, hyper has to be a secondary provider, after commandcode on deepseek v4.1 flash (m_flash) | aside from this, no subagent can inherit m_opus as the fallback; for m_zfl, mflash, m_fast, m_haiku, the last cascade fallback has to be m_luna".
Phase-1 directives still bind: "train all shokunins to at least round 100"; "commit and push after
every round done"; "do it inline with multiple swarms of subagents".

You are an in-session **L1 lane subagent** dispatched by the hyaku orchestrator (the operator's
parent omp session) for exactly ONE steered round: **kaidoku round 20** (attempt 3;
campaign target: round 100). Your lane is in a block of 10 sequential rounds, six lanes at a
time; the orchestrator dispatches your lane's next round only after this one lands and its
non-author closure is written. Work this round only and land it; then return a summary of at most 12
lines: claims with verdicts, lane HEAD, report commit, wave sizes and seat-role mix, dead seats, open
L0 questions. Never start round 20+1 and never claim another round number. Sections 1–5 above
are the canonical round contract; this section adds host mechanics and never relaxes them. Repo files
beat this prompt (PROTOCOL.md snapshot clause). Never call the `ask` tool: the round is unattended.
**Working directory:** your tools start at the fleet root, not the lane repo — run lane commands as
`git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin …` / `cd /home/vgpnk/Projects/shokunin/kaidoku-shokunin && …` and use absolute paths for every read/edit/write.
**Earlier attempts:** if `.ufo/watchdog.log` shows a `lane-dead-no-report kaidoku round=20`
line, an earlier attempt of this same round ended mid-work. Its uncommitted outputs in the lane repo
(e.g. `.ufo/waves/round-20/`) are inherited: reuse what you re-verify, discard what you do
not, and name both in the report.

1. **Load order, every round.** `skill://shokunin`, then /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/SKILL.md and
   `protocol/` PROTOCOL.md, MISSION.md, AXES.md, CORPUS.md, LEARNING.md (PROTOCOL-APPENDIX.md when a
   rule seems not to fit). Read `skill://swarm` before the first wave. Then your lane's SKILL.md,
   PROVINCE.md, SCORECARD.md (its `planned` row is your starting point), corpus/QUALITY.md,
   corpus/README.md (`## Frontier`), and the newest corpus/lessons.
2. **Swarm: every wave 64–100 seats** (operator 2026-10-20: "use heavy parallelization 64-100
   subagents"; "do not restrict yourself to the 16-32 waves; do it 64-100"). Validate every wave
   under policy v2 (band 64–100; the validator hard-caps one wave at 100), then dispatch it as
   exactly ONE `task` call carrying the validator's `taskCall` (`context` + `tasks`) unchanged; a
   refused wave is fixed, never split:

       cd /home/vgpnk/Projects/shokunin/kaidoku-shokunin && UFO_CONFIG_PATH=/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json \
         UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 UFO_PROJECT_ROOT=/home/vgpnk/Projects/shokunin/kaidoku-shokunin \
         node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs run --spec <wave-spec.json>

   **Wave 1 — build (64–100):** recon, source opening, entry drafting, tooling, plus first
   falsifiers of the round's declared claims. **Wave 2 — falsify (64–100)**, dispatched after wave 1
   returns: fresh reviewer/critic/mutation-tester/scout seats attack what wave 1 produced — re-run
   each counting command, re-open each new source row, attack each claim, review each new entry or
   tool, mutation-test each new gate; every item names what it attacks. Run wave 2 whenever wave 1's
   output yields ≥64 distinct attack items (the normal case); with fewer, never pad — run the
   residual checks yourself or through one ordinary `task` call of ≤8 reviewer/critic seats, and say
   so. Round total ≤200 seats: the operator's directives ("swarm rounds of 64-128", "64-100",
   "make sure we are always swarming heavily", "always see 64+ running") supersede the swarm skill's
   default 100-member round budget; the validator's 100-seat cap per wave still binds. Never replace
   a dead seat. Put specs and registries under `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/.ufo/waves/round-20/` (spec
   `reportDir: ".ufo/waves/round-20/<wave>"`, lane-relative) and commit them as wave evidence.
   Items are distinct, concrete work items serving the round's 1–3 claims plus the frontier step
   and verification — never padding. Record each wave's seat count, role mix, dead seats, and the
   round total in the report. The §3 L2 floor is met inside wave 1.
   **Planner seat (orchestrator ruling 2026-10-19):** the validator rejects `planner` — a
   frozen-topology seat, never a swarm role. You, the L1, hold the canonical §3 planner seat; a
   bounded planning data-walk may ride a scout, connector or revenger item. Record that mapping in
   the report; never bypass validation to add a planner.
   **Routing (session `task.agentModelOverrides`, set by the orchestrator on the operator's
   2026-10-20 directives — the role decides the route; never pass a `model` parameter):**
   connector, scout, labrat, simplifier → m_flash (operator: directive 27 "connector m_grok"
   superseded by directive 29 "change the m_grok for the the m_flash"; "labrat and scout should be
   m_flash"; "simplifier m_flash"); reviewer, revenger → m_zfl (operator 2026-10-20: "swap from
   m_flash to m_zfl"; "assign more m_zfl please, for future spawns"); executor, sentinel → m_luna
   (operator: "executor m_luna"; "sentinel m_luna"; executors only for code-heavy items: scripts,
   gates, selftests, fixtures, parsers, counting commands); critic → m_swe (operator: "do not
   remove m_opus, but put m_swe as critic"); mutation-tester → m_sol; scribe, distiller → m_haiku
   (operator: "leave scribe as m_haiku"; "distiller m_haiku"; prose: knowledge entries, SOURCES
   rows, lessons); planner (the L1-held frozen seat) and generic `task` (you and the closures) →
   m_opus (operator: "planner m_opus"). Explicit Opus primaries remain unchanged; no subagent may
   inherit Opus as a fallback. Directives 29–30 affect fresh captures only: running sessions and
   resumed seats keep the chain captured at spawn; the settings are session-only, not saved globally.
   **Mix for ~96 seats:** ~24 scout + ~2 simplifier + ~8 connector (≈34 m_flash), ~18 reviewer, ~4
   revenger (≈22 m_zfl), ~16 executor + ≤2 sentinel (≈18 m_luna), ~10 scribe (m_haiku), ~8 critic
   (m_swe), ≤4 mutation-tester (m_sol); distiller stays m_haiku if used, planner and `task` (L1s,
   closures) m_opus. Codex now hosts m_luna, m_sol and the last hop of the configured m_zfl/m_flash/
   m_fast/m_haiku cascades: if executors start failing on Codex rate limits, say so in the report
   with the error text. Give an item to an executor only when it writes or runs code; prose drafting goes to
   scribes, attacks to reviewers/critics/scouts.
   **Historical provider observations (2026-10-20 probes):** m_zfl answered from its primary
   (zai glm-5.3-flash) at the swap (~13:4x -03); its observed cascade was devin glm-5-3-flash →
   charm-hyper glm-5.3-flash (out of credits, 402) → m_luna max (openai-codex gpt-6-luna:max,
   answered a probe at 14:24 -03) last. Executors moved from m_swe to m_flash at 13:46 -03; the
   probe then showed m_flash's primary (commandcode deepseek-v4.1-flash) at its 5-hour plan limit
   (429, reset 2026-10-20T19:47:54Z = 16:47 -03). Its observed cascade was charm-hyper deepseek-flash
   (402) → opencode-go deepseek-flash → devin deepseek-flash → m_luna max
   (openai-codex gpt-6-luna:max) last. Record a seat's actual answering model when a claim depends
   on it; these observations are not current availability proof.
   **Historical zai rate-limit evidence (observed 14:00–15:25 -03):** with several lanes in waves at
   once, zai answered m_zfl seats with `429 Rate limit reached for requests (type=1302)`; ~130 seats
   died with "Retry budget exhausted after 10 retries" after retrying zai alone (~72 s apart). Why
   they never switched is unresolved: role-bound seats do capture and walk their alias cascade, and
   a provider retry-after or cooldown fits but is unproven.
   **Historical cascade-keying and smoke outcomes (since 15:50 -03):** the then-configured cascades
   were also keyed by their primary models (`zai/glm-5.3-flash`,
   `commandcode/deepseek/deepseek-v4.1-flash`, `openai-codex/gpt-6.1-sol`,
   `anthropic/claude-opus-5-5`, `devin/swe-2`, `openai-codex/gpt-6-luna`, `cursor/grok-4.7-fast`;
   the m_grok key stayed configured, unused by any role since directive 29). Fresh smoke seats
   (SmokeFlashCascade, SmokeZflCascade, SmokeOpusCascade) then failed over: commandcode 429 →
   opencode-go deepseek-flash; zai 429 (type=1302) → gpt-6-luna; Anthropic 429 → gpt-6.1-sol. Those
   observations showed failover for those fresh spawns, not which key won (the alias chains held the
   same hops) or what caused the earlier deaths. A seat keeps the chain it captured at spawn, also
   when resumed; only fresh captures receive changed settings. `retry.maxRetries` is 40. Report any
   seat that dies, with its last error text.
   **Historical Opus coordinator backoff:** coordinators received 429s with 13–14-minute
   retry-after values earlier today ("opus is back" since); respect any backoff and resume the same
   identity, never restart a duplicate writer. Historical availability is not current capacity
   proof. A dead seat stays dead in the evidence.
   **Directive 30 — current session-only fallback policy:** for the shared Commandcode
   `commandcode/deepseek/deepseek-v4.1-flash` primary (m_flash/m_fast/high/plan), the configured
   fallback sequence is `charm-hyper/deepseek-v4.1-flash` → `opencode-go/deepseek-v4.1-flash` →
   `devin/deepseek-v4-1-flash` → `openai-codex/gpt-6-luna:max`; `charm-hyper` is the first configured
   fallback after Commandcode. The exact-primary-model key mirrors the role chains. m_zfl's
   configured fallbacks are devin GLM → charm-hyper GLM → `openai-codex/gpt-6-luna:max`; m_haiku's
   are devin Haiku → cursor Haiku1m → cursor Haiku → `openai-codex/gpt-6-luna:max`. Each of these
   configured lists ends with m_luna:max; no provider availability or induced-failover claim is made.
   The default and m_opus fallback lists now contain only Codex Sol (`openai-codex/gpt-6.1-sol`);
   every configured fallback entry containing Opus was removed, including exact-model chains. No
   subagent may inherit Opus as a fallback; explicit Opus primaries and all other role assignments
   are unchanged. Previously unassigned built-in overrides security-reviewer, sonic and seance are
   explicitly pinned to m_flash to prevent parent-model inheritance. m_luna's separate own-provider
   backup was not changed. These settings affect fresh per-spawn captures only; already-running or
   resumed sessions keep their captured chain and are not retroactively refreshed. They are
   session-only, not saved globally. No policy/access restrictions changed; KasegiR23 remains
   policy-paused under PHASE2.md §Incidents and must not be retried.
   **REA MCP:** the operator authorized disabling the OMP `rea` MCP entry for this phase; the
   orchestrator set `"enabled": false` in `~/.omp/agent/mcp.json` at 10:12 -03 (pre-edit copy
   `~/.omp/agent/mcp.json.pre-disable-20261020T1015`). An unidentified writer rewrote that file at
   13:35:56 -03: the rea pin is now `rea-agents@6.7.0` and `enabled: false` is gone (reported by
   kaidoku r19; left for the operator to decide). The file is operator-owned either way: never edit
   or restore it. Do REA work through the CLI (`npx -y rea-agents@6.5.0 <command>`), never through
   `xd://mcp__rea_*` devices.
   **Job cap:** this session refuses a `task` call while ≥100 background jobs are running
   (`async.maxJobs` 100, fixed at process start; three lanes run concurrently); the refusal
   ("Background job limit reached (100)") spawns nothing. Retry the same payload every ~3 min
   (`sleep 180`), up to 20 tries; never split or shrink below the band; if still refused, land the
   round with verifiable work and report the refusals. Every concurrent writer needs an actual
   separate worktree, unique branch/path and observed base; bind its absolute paths there and
   keep one integration owner. Read-only seats return findings without production edits. Never
   run concurrent writers on one checkout. Seats never mutate the fleet repo, sibling lanes,
   lane jj state or lane Git index; put those bounds in every wave context.
   **Depth (`task.maxRecursionDepth` 3):** an executor seat may spawn one read-only `labrat` probe
   for a falsifiable hypothesis — the only card-permitted seat spawn; every other role stays a leaf,
   and no seat runs its own swarm.
   **Seat paths are absolute:** seat tools also start at the fleet root, so a relative path such as
   `.ufo/waves/...` lands in the FLEET repo (observed hyaku phase 1: kama r11, tsukuroi r12, tabi r15,
   mado r16). The wave `context` and every item must name absolute paths under /home/vgpnk/Projects/shokunin/kaidoku-shokunin; the spec
   `reportDir` alone stays lane-relative (the validator requires a relative path and resolves it
   beneath `UFO_PROJECT_ROOT` = your lane). The validator renders each seat a relative
   `Report: .ufo/waves/...` trailer, which a seat would resolve from the fleet root: every wave
   `context` must say "every `Report:` trailer path is relative to /home/vgpnk/Projects/shokunin/kaidoku-shokunin — write it at
   /home/vgpnk/Projects/shokunin/kaidoku-shokunin/<that path>". Never `agent://all` (it reaches every lane's seats) — message your
   seats by id.
3. **Write scope:** /home/vgpnk/Projects/shokunin/kaidoku-shokunin (your lane repo — including its own `scripts/`, `tools/`, gates);
   your report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-20/kaidoku.md`; appended lines in
   `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Never edit MANIFEST.json (a separate non-author hyaku
   closure session verifies this round and appends its closure entry), the fleet root's
   `/home/vgpnk/Projects/shokunin/templates/` and `/home/vgpnk/Projects/shokunin/scripts/`, `.ufo/state/`, `.ufo/watchdog.log`,
   or any sibling repo.
   **Misroot sweep before the report:** run `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no
   pathspec — seat notes have landed as plain files at the fleet root). For every untracked file one
   of your seats wrote into the fleet root (check its content names your lane/round), copy it
   byte-exact into the same relative path under /home/vgpnk/Projects/shokunin/kaidoku-shokunin, verify with `cmp`, then delete the
   fleet copy (the one fleet-root deletion you may make) and record the misroot under `## Mistakes`.
   Never touch files another lane's seats wrote, and never touch `.ufo/state/*` driver files.
4. **Commit order (landed = committed and pushed) — jj lane VCS** (operator 2026-10-20: "let's try
   to also implement using jj as git manager from now on on shokunin runs"). Your lane repo is
   jj-colocated (jj 0.45.1; git stays the backend and the GitHub remote). Commit ONLY through the
   lane helper, which tracks exactly the listed paths, commits them under
   `kaidoku-shokunin <kaidoku@shokunin.local>`, moves the branch bookmark and pushes (recovering
   from an operator push by fetch + rebase of your unpushed commits only):

       /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit /home/vgpnk/Projects/shokunin/kaidoku-shokunin --as kaidoku \
         -m "round-20: <what>" -- <repo-relative path>...

   Cite ONLY the helper's final `landed <hash>` line after successful remote verification.
   `rewritten <old> -> <new>` is diagnostic, never a citable landed hash. For an ordinary
   `commit`, exit 3 retains a local commit but proves no push: resolve the cause, then retry
   the helper push; never force.
   The post-commit scope/deletion guard reads NUL-delimited `git diff-tree
   --name-status -z --no-renames` records, not human brace summaries: a rename
   is checked as a deletion plus an addition, and an unchanged copy source is
   not treated as a changed path.
   If a specific helper-stranded candidate must be recovered, supply its
   reviewed full hash and the original requested paths explicitly:

       /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh recover /home/vgpnk/Projects/shokunin/kaidoku-shokunin --as kaidoku \
         --revision <full-commit-hash> -- <original repo-relative path>...

   Recovery is never automatic: the candidate must be a single direct child of
   the current lane branch tip, current `@` must be its direct child, both
   author and committer must match the lane/protocol identity, it must be
   conflict-free with a nonempty tree diff, and every changed path must pass
   the same scope, runtime and phantom-deletion guards. Its local mutation
   advances only the named branch bookmark; it does not snapshot or rewrite
   the remainder of `@`, and refuses stale-remote rebasing.
   Exit 3 means no landed-hash proof; never cite a candidate unless the helper
   prints `landed <hash>` after remote verification. Do not retry ordinary `push`
   while unrelated edits remain in `@`.
   `nothing to commit` lands nothing. Explicit files above 10 MiB require `--allow-large`. A named
   directory commits like `git add <dir>` (ignored content stays out; new files over 1 MiB inside it
   are skipped with a warning — name them as files). **Never** `git add`, `git commit`, `git stash`,
   `git checkout`, `git switch`, `git reset`, `git pull` or `git push` in the lane, and never run a
   mutating jj command yourself (`commit`, `new`, `describe`, `squash`, `rebase`, `abandon`,
   `bookmark`, `undo`, `op restore`/`revert`, `git push`/`fetch`): the helper is the only writer, jj
   resets the git index on every mutation, and a stray jj commit would be swept into your next push.
   Read-only git (log, show, diff, status, ls-files, rev-parse, merge-base) stays fine, but git HEAD
   is detached after the first helper commit: read the lane tip with
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kaidoku-shokunin` (`local=`, `ahead=`) or
   `git rev-parse <branch>`, never `@{u}`, `--abbrev-ref HEAD` or `branch --show-current`; record
   measured/pinned revisions as the branch tip, never bare `HEAD`. Read-only jj only with
   `--ignore-working-copy`. Revert a tracked file by rewriting it from the branch
   (`git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin show <branch>:<path> > /home/vgpnk/Projects/shokunin/kaidoku-shokunin/<path>`). A lane gate or selftest that
   runs git writes must run on a sandbox clone, never in the lane.
   Fleet-repo commits stay on git, only through the serialized helper, which pushes origin:

       /home/vgpnk/Projects/shokunin/scripts/hyaku/fleet-commit.sh --as kaidoku -m "round-20: kaidoku report" \
         -- .ufo/reports/round-20/kaidoku.md

   (also for an l0-questions append). The report lands last and cites the pushed lane hash.
5. **Inherited state.** Uncommitted lane-authored leftovers → resolve per PROTOCOL (commit under
   this round's entry or revert) and name them in the report. Files you did not author (operator
   sweeps, `round-*-aggregator-*`, `round-*-verifier-spotcheck.md`) → never edit; name them.
   Read `corpus/lessons/round-19-verifier-spotcheck.md` if it exists: it is the outside
   discernment check of your previous round — turn every disagreement or routed defect into a
   lesson-backed `QUALITY.md` criterion or fix, or say in the report why not. Also honor any
   `corpus/lessons/operator-*.md` teaching not yet reflected.
6. **Report extras:** the canonical **Trend verdicts** section; a `Stale-lane` line (respawn-per-
   round driver; no other mission of this lane is open); and any tool installs.
7. **Tooling authorization (operator, 2026-10-19):** you and every seat may install or upgrade
   tools that help the task — read `/home/vgpnk/.omp/agent/RULES.md` first (official channels,
   update-safety gate, record tool/version/channel/reason in the report). Put that sentence in
   each wave's `context`. **pacman guard (orchestrator ruling 2026-10-20, after the mado r15
   libinput incident):** **all pacman transactions are PAUSED host-wide** until the operator
   resolves the host-recovery L0 question — install via `uv tool`/`npx`/an official binary in
   `~/.local/bin`, or file an L0 question. When the pause lifts, the dry-run rule applies: the
   host's sync DB is ~413 packages ahead of the installed system, so installing or naming an
   already-installed package is a forbidden partial upgrade; before any `pacman -S`, run
   `pacman -Sp --print-format '%n %v' <pkgs>` and proceed only if every listed package is not
   installed yet. Never `-Sy`, `-Syu`, `-U`, `-R`, downgrade, or restart a host service. Put this
   guard in each wave's `context` too.
8. **Honesty.** An unrun check has not passed; never fabricate evidence or verdicts; harmed or
   unprovable claims are reported, not prettified. Blocked on an operator decision → append an L0
   question, route around it, and still land an honest report.
