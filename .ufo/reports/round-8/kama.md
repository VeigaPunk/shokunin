# kama — round 8 report (BLOCKED-WITH-DATA)

Lane round 8 of the operator goal "free-tier provider load-test" — loop 1 of
3, glm round 1 of 2. Date: 2026-10-18. Planned dispatch: one batched
AgentSwarm call, 64 seats, model `opencode-go/glm-5.3-flash-free`.

## Work performed

- Round plan + claims declared: `.ufo/round-8/plan.json` (same
  standing-queue pair: freshness citation re-anchoring; operability
  gate-bundle refresh — the queue stands unchanged since no seat has yet
  executed in rounds 6–8).
- Seat protocol carried forward: `.ufo/round-8/SEAT-PROTOCOL.md`.
- Dispatch attempted; rejected by the host runtime's model-catalog
  validation before any seat was created. Full verbatim error and complete
  host catalog: `.ufo/round-8/telemetry.json`.
- L0 side channel used per protocol: question appended to fleet
  `.ufo/l0-questions.md` (kama | round-8).

## Landed changes (lane repo, commit d0f5a2d2b2e5cbfd9674e57fd3d90970df92ab92)

- `.ufo/round-8/plan.json`, `.ufo/round-8/SEAT-PROTOCOL.md`,
  `.ufo/round-8/telemetry.json` — new.
- `LOG.md` — round-8 entry appended; `SCORECARD.md` — move-log row + section.
- No corpus, probe, registry, or gate content changed. No push.

## Before → after measurements

- Seats dispatched: **0** — the AgentSwarm call failed local validation in
  0.0 s; no spawn attempts, no upstream contact. This is a distinct failure
  class from rounds 6-7 (64 catalog-valid spawns each, rejected upstream
  with `400 Model is unavailable`).
- Verbatim error: `Invalid model "opencode-go/glm-5.3-flash-free".
  Available models: …` — full 29-alias catalog captured in
  `.ufo/round-8/telemetry.json`.
- Claim measurements: NOT EXECUTABLE (no seat ran); nothing re-rolled.

## Round telemetry (dispatch level, recorded by L1)

- Window: 2026-10-18T18:39–18:40Z. Launched 0, completed 0, failed 0
  (rejected pre-spawn). Tokens generated 0; inferred TPS not measurable.
- **Finding:** the goal's glm wire id is **not dispatchable on this host** —
  no opencode-go glm variant (free or paid) exists in the catalog.
  glm-5.3-flash is available only as `zai-coding-plan/glm-5.3-flash[-low]`
  (zai lane) and `devin/glm-5-3-flash-{low,high,max}` (devin lane) —
  different providers, not the opencode-go free tier under test.
- **Loop-1 score so far:** deepseek-free 0/128 seats (upstream outage,
  persistent 18:32–18:37Z); glm-free 0 seats (host catalog gap, local
  rejection). Neither provider produced a token in loop 1.

## Cross-domain findings

None. Out-of-province by construction: host model-catalog configuration is
operator/kumitate-owned — reported via L0, not acted on.

## Admission

BLOCKED-WITH-DATA. No admit; all axes unchanged; no scalar advanced.
**Operator decision required for the glm arm** (rounds 9, 12, 13, 16, 17):
add the opencode-go free glm variant to the host catalog, or authorize a
substitute wire id in writing. Per the goal's stop rule, no substitution was
made. Deepseek re-tests continue per schedule (rounds 10–11, 14–15).

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists — unchanged;
  pointer: `SKILL.md` §§Decision table, Error signatures, Checklist (author
  assertion; no non-author verifier this round).
- [~] End-to-end domain task executed and logged — unchanged; pointer:
  `LOG.md` rounds 1–4 (author assertion).
- [~] Instructions executable without oral context — unchanged; pointer:
  `SKILL.md` §Checklist (author assertion).
- [~] No cross-domain bleed — unchanged; pointer: `PROVINCE.md` §Write
  boundary (author assertion).
