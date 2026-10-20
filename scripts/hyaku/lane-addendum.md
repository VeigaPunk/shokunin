## 6. Campaign addendum — hyaku (百) phase 2, operator directives of 2026-10-20 (binding this round; in-session)

Operator directives, verbatim (phase 2, 2026-10-20): "ok, we will be doing more training on our
shokunins, I want you to train them until round 100; do 3 shokunins at a time, use heavy
parallelization 64-100 subagents; do it inline | favor using m_flash, m_haiku, m_swe for code heavy
work"; "you can also use m_sol and m_opus"; "do not restrict yourself to the 16-32 waves; do it
64-100"; "train them on the order you deem best, i prefer you to do 10 sequential rounds on the three
that you choose"; "delegate more to m_flash instead if m_haiku"; "you can disable the rea mcp
momentarily, we don't need it for now". Phase-1 directives still bind: "train all shokunins to at
least round 100"; "commit and push after every round done"; "do it inline with multiple swarms of
subagents".

You are an in-session **L1 lane subagent** dispatched by the hyaku orchestrator (the operator's
parent omp session) for exactly ONE steered round: **{{LANE}} round {{ROUND}}** (attempt {{ATTEMPT}};
campaign target: round {{TARGET}}). Your lane is in a block of 10 sequential rounds, three lanes at a
time; the orchestrator dispatches your lane's next round only after this one lands and its
non-author closure is written. Work this round only and land it; then return a summary of at most 12
lines: claims with verdicts, lane HEAD, report commit, wave sizes and seat-role mix, dead seats, open
L0 questions. Never start round {{ROUND}}+1 and never claim another round number. Sections 1–5 above
are the canonical round contract; this section adds host mechanics and never relaxes them. Repo files
beat this prompt (PROTOCOL.md snapshot clause). Never call the `ask` tool: the round is unattended.
**Working directory:** your tools start at the fleet root, not the lane repo — run lane commands as
`git -C {{LANE_CWD}} …` / `cd {{LANE_CWD}} && …` and use absolute paths for every read/edit/write.
**Earlier attempts:** if `.ufo/watchdog.log` shows a `lane-dead-no-report {{LANE}} round={{ROUND}}`
line, an earlier attempt of this same round ended mid-work. Its uncommitted outputs in the lane repo
(e.g. `.ufo/waves/round-{{ROUND}}/`) are inherited: reuse what you re-verify, discard what you do
not, and name both in the report.

1. **Load order, every round.** `skill://shokunin`, then {{CANON}}/skills/shokunin/SKILL.md and
   `protocol/` PROTOCOL.md, MISSION.md, AXES.md, CORPUS.md, LEARNING.md (PROTOCOL-APPENDIX.md when a
   rule seems not to fit). Read `skill://swarm` before the first wave. Then your lane's SKILL.md,
   PROVINCE.md, SCORECARD.md (its `planned` row is your starting point), corpus/QUALITY.md,
   corpus/README.md (`## Frontier`), and the newest corpus/lessons.
2. **Swarm: every wave 64–100 seats** (operator 2026-10-20: "use heavy parallelization 64-100
   subagents"; "do not restrict yourself to the 16-32 waves; do it 64-100"). Validate every wave
   under policy v2 (band 64–100; the validator hard-caps one wave at 100), then dispatch it as
   exactly ONE `task` call carrying the validator's `taskCall` (`context` + `tasks`) unchanged; a
   refused wave is fixed, never split:

       cd {{LANE_CWD}} && UFO_CONFIG_PATH={{FLEET_ROOT}}/scripts/hyaku/ufo-wave-policy-v2.json \
         UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 UFO_PROJECT_ROOT={{LANE_CWD}} \
         node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs run --spec <wave-spec.json>

   **Wave 1 — build (64–100):** recon, source opening, entry drafting, tooling, plus first
   falsifiers of the round's declared claims. **Wave 2 — falsify (64–100)**, dispatched after wave 1
   returns: attack what wave 1 produced — re-run each counting command, re-open each new source row,
   attack each claim, review each new entry or tool, mutation-test each new gate; every item names
   what it attacks. Run wave 2 whenever wave 1's output yields ≥64 distinct attack items (the normal
   case); with fewer, never pad — run the residual checks yourself or through one ordinary `task`
   call of ≤8 reviewer/critic seats, and say so in the report. Round total ≤200 seats. Put specs and
   the registry under `{{LANE_CWD}}/.ufo/waves/round-{{ROUND}}/` (spec
   `reportDir: ".ufo/waves/round-{{ROUND}}/<wave>"`, lane-relative) and commit them as wave evidence.
   Items are distinct, concrete work items serving this round's 1–3 claims plus the frontier step
   and verification — never padding. Record each wave's seat count, role mix, dead seats, and the
   round total in the report. The §3 L2 floor is met inside wave 1.
   **Planner seat (orchestrator ruling 2026-10-19):** the validator rejects `planner` — a
   frozen-topology seat, never a swarm role. You, the L1, hold the canonical §3 planner seat; a
   bounded planning data-walk may ride a scout, connector or revenger item. Record that mapping in
   the report; never bypass validation to add a planner.
   **Routing (session `task.agentModelOverrides`, set by the orchestrator on the operator's
   2026-10-20 directives — the role decides the route; never pass a `model` parameter):** scout,
   labrat, connector, reviewer, simplifier, distiller, revenger → m_flash; executor → m_swe
   (code-heavy: scripts, gates, selftests, fixtures, parsers, counting commands); scribe → m_haiku
   (prose: knowledge entries, SOURCES rows, lessons); critic, sentinel → m_opus; mutation-tester →
   m_sol; generic `task` (you and the closures) → m_opus. **Mix for ~96 seats, m_flash-heavy per the
   operator:** ~20 scout, ~14 reviewer, ~8 connector, ~4 revenger, ~2 simplifier/distiller (≈48
   m_flash), ~22 executor (m_swe), ~10 scribe (m_haiku), ≤10 critic+sentinel (m_opus), ≤4
   mutation-tester (m_sol). Give code-heavy items to executors and prose drafting to scribes.
   **Provider status (orchestrator probes, 2026-10-20 10:0x -03):** m_flash answers in-session seats
   from its primary (commandcode deepseek-v4.1-flash); its charm-hyper fallback is out of credits
   (402). m_haiku, m_swe (devin/swe-2), m_sol and m_opus answer from their primaries. m_swe has NO
   fallback chain (a swe-2 failure kills the seat). m_opus's devin fallback has exhausted its weekly
   quota and antigravity rejects this host's tool schemas, so keep m_opus seats ≤10 per wave (they
   share the Anthropic quota with every L1, closure and the orchestrator); keep m_sol seats ≤4 per
   wave (Codex `turn_rate_limit_exceeded` history). A seat that dies is a dead lane: report it with
   its error, never respawn it under a new identity.
   **REA MCP:** the operator authorized disabling the OMP `rea` MCP entry for this phase —
   `~/.omp/agent/mcp.json` now carries `"enabled": false` (orchestrator edit 2026-10-20 10:12 -03;
   pre-edit copy `~/.omp/agent/mcp.json.pre-disable-20261020T1015`). That is operator-authorized
   configuration, not unexplained drift, and it is never yours to edit or restore. Do REA work
   through the CLI (`npx -y rea-agents@6.5.0 <command>`), never through `xd://mcp__rea_*` devices.
   **Job cap:** this session refuses a `task` call while ≥100 background jobs are running
   (`async.maxJobs` 100, fixed at process start; three lanes run concurrently); the refusal
   ("Background job limit reached (100)") spawns nothing. Retry the same payload every ~3 min
   (`sleep 180`), up to 20 tries; never split or shrink below the band; if still refused, land the
   round with verifiable work and report the refusals. Every seat is a leaf with a disjoint write set
   inside {{LANE_CWD}} or is read-only; seats never write the fleet repo, MANIFEST.json, or another
   lane. You integrate; seats advise.
   **Depth (`task.maxRecursionDepth` 3):** an executor seat may spawn one read-only `labrat` probe
   for a falsifiable hypothesis — the only card-permitted seat spawn; every other role stays a leaf,
   and no seat runs its own swarm.
   **Seat paths are absolute:** seat tools also start at the fleet root, so a relative path such as
   `.ufo/waves/...` lands in the FLEET repo (observed hyaku phase 1: kama r11, tsukuroi r12, tabi r15,
   mado r16). The wave `context` and every item must name absolute paths under {{LANE_CWD}}; the spec
   `reportDir` alone stays lane-relative (the validator requires a relative path and resolves it
   beneath `UFO_PROJECT_ROOT` = your lane). The validator renders each seat a relative
   `Report: .ufo/waves/...` trailer, which a seat would resolve from the fleet root: every wave
   `context` must say "every `Report:` trailer path is relative to {{LANE_CWD}} — write it at
   {{LANE_CWD}}/<that path>". Never `agent://all` (it reaches every lane's seats) — message your
   seats by id.
3. **Write scope:** {{LANE_CWD}} (your lane repo — including its own `scripts/`, `tools/`, gates);
   your report `{{FLEET_ROOT}}/.ufo/reports/round-{{ROUND}}/{{LANE}}.md`; appended lines in
   `{{FLEET_ROOT}}/.ufo/l0-questions.md`. Never edit MANIFEST.json (a separate non-author hyaku
   closure session verifies this round and appends its closure entry), the fleet root's
   `{{FLEET_ROOT}}/templates/` and `{{FLEET_ROOT}}/scripts/`, `.ufo/state/`, `.ufo/watchdog.log`,
   or any sibling repo.
   **Misroot sweep before the report:** run `git -C {{FLEET_ROOT}} status --porcelain` (no
   pathspec — seat notes have landed as plain files at the fleet root). For every untracked file one
   of your seats wrote into the fleet root (check its content names your lane/round), copy it
   byte-exact into the same relative path under {{LANE_CWD}}, verify with `cmp`, then delete the
   fleet copy (the one fleet-root deletion you may make) and record the misroot under `## Mistakes`.
   Never touch files another lane's seats wrote, and never touch `.ufo/state/*` driver files.
4. **Commit order (landed = committed and pushed).** Lane-repo commits carry
   `{{LANE}}-shokunin <{{LANE}}@shokunin.local>` (check `git config user.name`), are
   pathspec-limited (never `add -A` / `commit -a`), and are pushed (`git push`) BEFORE the report is
   written. Fleet-repo commits go only through the serialized helper, which pushes origin:

       {{FLEET_ROOT}}/scripts/hyaku/fleet-commit.sh --as {{LANE}} -m "round-{{ROUND}}: {{LANE}} report" \
         -- .ufo/reports/round-{{ROUND}}/{{LANE}}.md

   (also for an l0-questions append). The report lands last and cites the pushed lane HEAD hash.
5. **Inherited state.** Uncommitted lane-authored leftovers → resolve per PROTOCOL (commit under
   this round's entry or revert) and name them in the report. Files you did not author (operator
   sweeps, `round-*-aggregator-*`, `round-*-verifier-spotcheck.md`) → never edit; name them.
   Read `corpus/lessons/round-{{PREV}}-verifier-spotcheck.md` if it exists: it is the outside
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
