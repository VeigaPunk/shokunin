# kama — round 6 report (BLOCKED-WITH-DATA)

Lane round 6 of the operator goal "free-tier provider load-test" — loop 1 of
3, deepseek round 1 of 2. Date: 2026-10-18. Dispatch surface: one batched
AgentSwarm call, 64 seats, `subagent_type=coder`.

## Work performed

- Round plan + claims declared: `.ufo/round-6/plan.json` in the lane repo.
  Freshness claim: re-anchor still-live source anchors through dated corpus
  corrections (standing queue: `SCORECARD.md` Planned; `.ufo/round-5/
  continuation.md`). Operability claim: refresh the gate evidence bundle at
  round-6 HEAD under `.ufo/round-6/gates/`.
- Seat protocol + 64-seat map authored: `.ufo/round-6/SEAT-PROTOCOL.md`
  (20 audit seats on one-file-each corpus surfaces, 12 evidence/gate seats,
  32 fixed-shape TPS-probe seats; append-only edits; per-seat telemetry
  block).
- ONE batched AgentSwarm dispatched on
  `opencode-go/deepseek-v4.1-flash-free` (free variant; wire-default effort —
  the dispatch surface exposes no per-seat effort pin). Full telemetry:
  `.ufo/round-6/telemetry.json`.
- Single-seat liveness re-probe after the wave: same failure (persistence
  check).

## Landed changes (lane repo, commit f396b98945407374ee116e93453b04b0c396c200)

- `.ufo/round-6/plan.json`, `.ufo/round-6/SEAT-PROTOCOL.md`,
  `.ufo/round-6/telemetry.json` — new.
- `LOG.md` — round-6 entry appended.
- `SCORECARD.md` — move-log row + round-6 blocked section.
- No corpus, probe, registry, or gate content changed (no seat executed).
- No push: the operator goal instructs commit only, and round-5 set the
  no-push precedent. Bookkeeping for operator release.

## Before → after measurements

- Seats dispatched 64 → completed 0; failed 64, one class, verbatim:
  `400 Upstream request failed: Model is unavailable.` — repeated identically
  across all 64 seats. The alias is accepted by the host dispatch catalog;
  the failure originates at the provider gateway.
- Wave wall time 41.6 s for 64 fast-fail spawn attempts (≈0.65 s per attempt,
  queue-drained). Peak concurrency observed: 0 — no seat reached model
  execution, so seat-level self-measurement (t_start/t_end/output bytes)
  does not exist this round.
- Re-probe: 1 seat, ~2 min after the wave, 0.53 s to the identical error —
  persistent unavailability, not a transient rate-limit.
- Claim measurements (freshness re-anchor count; gate-bundle refresh): NOT
  EXECUTABLE — no seat ran. No before/after is claimed; nothing re-rolled.

## Round telemetry (dispatch level, recorded by L1)

- Window: 2026-10-18T18:32–18:35Z. Seats launched 64, completed 0, failed 64.
- Failure class: upstream model-unavailable (400), verbatim above.
- Tokens generated: 0. Inferred TPS: not measurable — inference requires
  ≥1 completing seat (methodology declared in the goal); zero completing
  seats exist this round.
- **Finding:** free-tier `opencode-go/deepseek-v4.1-flash-free` effective
  concurrency ceiling on this host at 2026-10-18T18:33Z = **0 usable seats**
  (model unavailable at the gateway, persistent across two waves).

## Cross-domain findings

None. No stale-lane exposure (round blocked at dispatch).

## Admission

BLOCKED-WITH-DATA. No admit; no axis harmed or improved — no round executed.
All axes unchanged. No scalar advanced. Round-3 report gap and round-5
blocked attempt remain named debt, untouched.

Per goal schedule: round 7 (same model — re-tests availability), then rounds
8–9 on the glm free variant.

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists — unchanged;
  pointer: `SKILL.md` §§Decision table, Error signatures, Checklist (author
  assertion; no non-author verifier this round).
- [~] End-to-end domain task executed and logged — unchanged; pointer:
  `LOG.md` rounds 1–4 (author assertion).
- [~] Instructions executable without oral context — unchanged; pointer:
  `SKILL.md` §Checklist, `corpus/knowledge/snapshot-history.md` (author
  assertion).
- [~] No cross-domain bleed — unchanged; pointer: `PROVINCE.md` §Write
  boundary (author assertion).
