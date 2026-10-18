# kama — round 7 report (BLOCKED-WITH-DATA)

Lane round 7 of the operator goal "free-tier provider load-test" — loop 1 of
3, deepseek round 2 of 2: the availability re-test. Date: 2026-10-18.
Dispatch surface: one batched AgentSwarm call, 64 seats,
`subagent_type=coder`, model `opencode-go/deepseek-v4.1-flash-free`.

## Work performed

- Round plan + claims declared: `.ufo/round-7/plan.json` (same standing-queue
  pair as round 6: freshness citation re-anchoring; operability gate-bundle
  refresh — round 6 executed neither, so the queue stands unchanged).
- Seat protocol carried from round 6 verbatim modulo round number:
  `.ufo/round-7/SEAT-PROTOCOL.md` (20 audit / 12 evidence / 32 TPS-probe).
- ONE batched 64-seat AgentSwarm dispatched. Full telemetry:
  `.ufo/round-7/telemetry.json`.

## Landed changes (lane repo, commit 4bcae65a23f58186c826ef2f793b029f3f9f8405)

- `.ufo/round-7/plan.json`, `.ufo/round-7/SEAT-PROTOCOL.md`,
  `.ufo/round-7/telemetry.json` — new.
- `LOG.md` — round-7 entry appended; `SCORECARD.md` — move-log row + section.
- No corpus, probe, registry, or gate content changed. No push.

## Before → after measurements

- Seats dispatched 64 → completed 0; failed 64, identical verbatim class:
  `400 Upstream request failed: Model is unavailable.` — same as round 6.
- Wave wall 41.5 s for 64 fast-fail spawn attempts; peak concurrency 0 (no
  seat reached model execution; no seat-level self-measurements exist).
- **Persistence established:** three probes of this model within ~25 min —
  round-6 wave (18:32Z), round-6 single-seat re-probe (18:33Z), round-7 wave
  (18:37Z) — three identical gateway failures. This is sustained provider
  unavailability of the free wire id, not a transient rate limit.
- Claim measurements: NOT EXECUTABLE (no seat ran); nothing re-rolled.

## Round telemetry (dispatch level, recorded by L1)

- Window 2026-10-18T18:36–18:38Z. Launched 64, completed 0, failed 64,
  class upstream model-unavailable (400). Tokens generated 0; inferred TPS
  not measurable (zero completing seats).
- **Finding:** loop-1 deepseek free-tier effective concurrency ceiling at
  2026-10-18T18:37Z = **0 usable seats**, persistent across three probes.

## Cross-domain findings

None.

## Admission

BLOCKED-WITH-DATA. No admit; all axes unchanged; no scalar advanced.
Named debt unchanged (round-3 report gap, round-5 blocked attempt).
Next per goal schedule: rounds 8–9 on `opencode-go/glm-5.3-flash-free`.

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
