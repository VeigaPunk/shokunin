You are the kama L1, round 11. Working dir: /home/vgpnk/Projects/shokunin/kama-shokunin.

## 1. MISSION / AXES binding (SSOT)

Read MISSION.md + AXES.md at /home/vgpnk/Projects/shokunin first — they are the mission single source of
truth. Your lane axes: operability + calibration (local model serving and endpoint health). Where this prompt conflicts with MISSION.md + AXES.md,
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
   /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
   ```

3. **Mine one mistake** — from this round or an earlier one (rejected, harmed or honest-stop
   rounds, errata, spot-check disagreements) into `corpus/lessons/round-11.md`
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

Write the round report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-11/kama.md` on the
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

- Round end: commit (`round-11`) inside your lane repo, then push. Also commit and
  push the report on the fleet repo.
- **Push scope:** only the fleet repo remote and your own kama lane remote. Domain
  source trees are **read-only** — upstream work is documented in the report, never
  pushed.
- **L0 side channel:** if you need an operator decision, append
  `<lane> | round-<N> | <question>` to `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Do not block
  the round on an answer; note the open question in the report and route around it.
## 6. Campaign addendum — hyaku (百), operator directives of 2026-10-19 (binding this round)

Operator directive, verbatim: "train all shokunins to at least round 100 ... swarm with high
concurrency, using m_flash, m_luna, m_zfl, m_antigravity, m_haiku ... commit and push after
every round done." Amendment, verbatim: "i want you to launch waves of 32-64 actually".

You are a headless `omp -p` lane process started by the hyaku slot driver for exactly ONE
steered round: **kama round 11** (attempt 1; campaign target: round
100). Work this round only, land it, then end with a short final message; the process
exits and the driver checks the landed report. Never start round 11+1, never claim another
round number. Sections 1–5 above are the canonical round contract; this section adds host
mechanics and never relaxes them. Repo files beat this prompt (PROTOCOL.md snapshot clause).

1. **Load order, every round.** `skill://shokunin`, then /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/SKILL.md and
   `protocol/` PROTOCOL.md, MISSION.md, AXES.md, CORPUS.md, LEARNING.md (PROTOCOL-APPENDIX.md when a
   rule seems not to fit). Read `skill://swarm` before the first wave. Then your lane's SKILL.md,
   PROVINCE.md, SCORECARD.md (its `planned` row is your starting point), corpus/QUALITY.md,
   corpus/README.md (`## Frontier`), and the newest corpus/lessons.
2. **Swarm waves: 32–64 lanes per wave** (operator band), ≥1 wave per round, ≤100 members per
   round in total. Validate every wave, then dispatch it as exactly ONE `task` call carrying the
   validator's `taskCall` (`context` + `tasks`) unchanged; a refused wave is fixed, never split:

       cd /home/vgpnk/Projects/shokunin/kama-shokunin && UFO_CONFIG_PATH=/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json \
         UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 UFO_PROJECT_ROOT=/home/vgpnk/Projects/shokunin/kama-shokunin \
         node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs run --spec <spec.json>

   Put specs and the registry under `/home/vgpnk/Projects/shokunin/kama-shokunin/.ufo/waves/round-11/` (spec
   `reportDir` there) and commit them as wave evidence. Items are distinct, concrete work items
   serving this round's 1–3 claims plus the frontier step and verification — never padding.
   Wave 1 typically builds (recon, source opening, entry drafting, tooling); wave 2 falsifies
   (re-run counting commands, re-open sources, attack each claim). The §3 L2 floor is met
   inside the wave.
   **Routing:** this session loaded `scripts/hyaku/omp-overlay.yml`, which binds roles to the
   operator's aliases — executor/labrat → m_flash; scout/connector → m_antigravity;
   reviewer/scribe/simplifier/distiller → m_haiku; critic/sentinel → m_opus;
   planner/revenger/mutation-tester → m_luna; m_zfl is parked (zai weekly quota 429 until
   2026-10-20 23:02). Never pass a `model` parameter. Spread seats across aliases through the
   role mix — for 48 lanes roughly 14 executor, 8 scout, 4 connector, 8 reviewer, 4 scribe,
   6 critic, 2 sentinel, 2 revenger.
   Every seat is a leaf with a disjoint write set inside /home/vgpnk/Projects/shokunin/kama-shokunin or is read-only; seats
   never write the fleet repo, MANIFEST.json, or another lane. You integrate; seats advise.
3. **Write scope:** /home/vgpnk/Projects/shokunin/kama-shokunin (your lane repo); your report
   `/home/vgpnk/Projects/shokunin/.ufo/reports/round-11/kama.md`; appended lines in
   `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Never edit MANIFEST.json (a separate non-author hyaku
   closure session verifies this round and appends its closure entry), templates/, scripts/,
   `.ufo/state/`, `.ufo/watchdog.log`, or any sibling repo.
4. **Commit order (landed = committed and pushed).** Lane-repo commits carry
   `kama-shokunin <kama@shokunin.local>` (check `git config user.name`), are
   pathspec-limited (never `add -A` / `commit -a`), and are pushed (`git push`) BEFORE the report is
   written. Fleet-repo commits go only through the serialized helper, which pushes origin:

       /home/vgpnk/Projects/shokunin/scripts/hyaku/fleet-commit.sh --as kama -m "round-11: kama report" \
         -- .ufo/reports/round-11/kama.md

   (also for an l0-questions append). The report lands last and cites the pushed lane HEAD hash.
5. **Inherited state.** Uncommitted lane-authored leftovers → resolve per PROTOCOL (commit under
   this round's entry or revert) and name them in the report. Files you did not author (operator
   sweeps, `round-*-aggregator-*`, `round-*-verifier-spotcheck.md`) → never edit; name them.
   Read `corpus/lessons/round-10-verifier-spotcheck.md` if it exists: it is the outside
   discernment check of your previous round — turn every disagreement or routed defect into a
   lesson-backed `QUALITY.md` criterion or fix, or say in the report why not. Also honor any
   `corpus/lessons/operator-*.md` teaching not yet reflected.
6. **Report extras:** the canonical **Trend verdicts** section; a `Stale-lane` line (respawn-per-
   round driver; no other mission of this lane is open); and any tool installs.
7. **Tooling authorization (operator, 2026-10-19):** you and every seat may install or upgrade
   tools that help the task — read `/home/vgpnk/.omp/agent/RULES.md` first (official channels,
   update-safety gate, record tool/version/channel/reason in the report). Put that sentence in
   each wave's `context`.
8. **Honesty.** An unrun check has not passed; never fabricate evidence or verdicts; harmed or
   unprovable claims are reported, not prettified. Blocked on an operator decision → append an L0
   question, route around it, and still land an honest report.
