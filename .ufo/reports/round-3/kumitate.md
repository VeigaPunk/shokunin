# kumitate-shokunin — round 3 report

**Gap selected:** fleet-dispatcher settle/successor internals — the largest
unmapped high-risk surface in corpus (why iterate chains live or die).
Round-2 carryover (route-resolution note + SKILL section) was committed
separately as `round-2` before this round's work.

## Deliverables (child repo, commit `round-3`)

- `corpus/knowledge/successor-chain.md` — full map of
  `maybeEnqueueIterationSuccessor` (~L6743-7150 in
  `scripts/fleet-dispatcher.mjs`).
- SKILL.md `fleet-dispatcher` section expanded with the iterate chain.
- `corpus/lessons/round-3.md`, corpus README index/gap refresh, LOG.md
  round-3 entry.

## Findings

1. **Decision gate is receipt-bound and fail-closed.** Only
   `iteration.decision:"continue"` mints a successor; missing block →
   `decision_missing`; round cap → `budget_halt` (overrides even
   `continue`); a decision on a non-iterate row is logged
   `queue_continuation_skipped` rather than silently dropped.
2. **Defer-not-die is the doctrine.** Scope occupancy and queue capacity
   park as `continue`+`deferred`, re-minting onto the deterministic
   successor key when the condition drains — successor identity is a pure
   function of `(parent, round, priorReceiptSha256)`.
3. **Outcome vocabulary (7 kinds):** `continue | stop | blocked |
   budget_halt | decision_missing | successor_error |
   successor_superseded`. afterChains: `stop|budget_halt|decision_missing|
   successor_superseded` satisfy waiters; `blocked|successor_error`
   starve; unknown kinds fail closed.
4. **Park epochs (r43):** `iterationOutcome.at` is the park epoch, never
   re-stamped on re-evaluation; `lastEvalAt` carries evaluation. Consuming
   code that reads `at` as freshness will misread parked entries.
5. **Admission counting is latch-based, not log-based:**
   `admission-latch.json` pairs each `receipt_snapshot_binding_accepted`
   with exactly one `receipt_snapshot_binding_retracted` per completion
   demotion; admissions − retractions = live count. Display settles do not
   retract by contract (r40).
6. **Typed collisions:** `result_path_occupied` names the queue occupant;
   `result_path_artifact_exists` refuses to attribute an owner from a
   filename alone (fail-closed evidence).

## Remaining gaps

`ufo-core-runtime` loop-driver + native admission internals (next
candidate), native-trial launch sequence, the-tick ops, dispatcher
claim/dispatch front half.
