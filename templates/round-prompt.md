You are the {{LANE}} L1, round {{ROUND}}. Working dir: {{FLEET_ROOT}}/<{{LANE}}-repo>.

## 1. MISSION / AXES binding (SSOT)

Read MISSION.md + AXES.md at {{FLEET_ROOT}} first — they are the mission single source of
truth. Your lane axes: {{AXES}}. Where this prompt conflicts with MISSION.md + AXES.md,
the mission files win.

## 2. Claims this round — 1 to 3, each falsifiable

This round is **1–3 declared claims**, not a batch of unrelated work:

1. Open your lane repo's SCORECARD.md (create it per AXES.md if missing).
2. Declare 1–3 claims. Each claim is one axis-move against a distinct axis, with
   its own falsifiable before→after. At least one claim works the **lowest-scoring
   non-retired axis** — unless the stagnation nudge waives it (AXES.md §The stagnation nudge).
3. Land every claimed improvement. Claims must be **causally separable**: each
   verifiable without the others having landed. Two claims on one axis = one claim.
4. Measure each: run a counting command you can paste into the report, before and
   after.
5. Record per claim in SCORECARD.md: the score delta, evidence pointer, counting
   command, and measured commit; append the motivating evidence to LOG.md.
6. A claim may be a **capability acquisition** (AXES.md §Capabilities): the new
   capability runs, its output verifies, and its row enters the SCORECARD
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

## 3. L2 floor — one batched swarm

Dispatch **at least 8 L2 subagents in ONE batched AgentSwarm call** this round (Kimi
surface: a single batched swarm dispatch, not serial one-at-a-time spawns). Minimum role
split:

- 1× planner, 1× connector (sibling-overlap scan)
- 3× executor, 1× scribe, 1× scout (per-surface reconnaissance)
- 1× reviewer, 1× critic (falsifies the claims the others assert)

Add sentinel / revenger / labrat / mutation-tester / simplifier / distiller as the axis
demands. Route every role through the **host route table** — the fleet operator's
role→model assignments for this substrate. Never hardcode model aliases in the lane repo;
the route table, not this prompt, decides which model serves which role.

**Godspeed lead:** every L2 lane prompt leads with `/skill:godspeed` followed by the
verbatim directive bytes from `~/.agents/skills/godspeed/directive.md` — do not
paraphrase. Resumes and nudges never re-carry it.

## 4. Report contract

Write the round report at `{{FLEET_ROOT}}/.ufo/reports/round-{{ROUND}}/{{LANE}}.md` on the
fleet repo. Required sections, in order:

- **Work performed** — opens by naming the round's declared claims (1–3) and their
  target axes or capability; then one bullet per work item, each carrying an
  evidence pointer (path:line, command output, or commit hash).
- **Landed changes** — every change tied to a LOG.md entry and to the commit hash that
  carries it.
- **Before → after measurements** — one per claim, each with the counting command and the
  commit it was measured against.
- **SHONEN** — one line per box of your SHONEN.md checklist: `[x]` only with a named
  non-author verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched.

**Marker rule:** a contentless report (placeholder text, missing required sections, no
evidence pointers) counts as the round **failed** — the driver relaunches the same round. A
report that names real committed work but skips the required sections is `ok` plus a
minimum-content conformance defect, logged as one.

## 5. Commit, push scope, L0 side channel

- Round end: commit (`round-{{ROUND}}`) inside your lane repo, then push. Also commit and
  push the report on the fleet repo.
- **Push scope:** only the fleet repo remote and your own {{LANE}} lane remote. Domain
  source trees are **read-only** — upstream work is documented in the report, never
  pushed.
- **L0 side channel:** if you need an operator decision, append
  `<lane> | round-<N> | <question>` to `{{FLEET_ROOT}}/.ufo/l0-questions.md`. Do not block
  the round on an answer; note the open question in the report and route around it.

 | godspeed
