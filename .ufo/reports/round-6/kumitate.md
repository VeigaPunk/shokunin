# kumitate-shokunin — round 6

Commit: `eca3d14` (`round-6`) in `kumitate-shokunin/` (pushed origin/master).

## What landed

Three of the four standing named gaps closed:

1. **Fleet-dispatcher tail — fully mapped** (`corpus/knowledge/
   enqueue-admission.md` + `reconcile-and-cycle.md` + SKILL.md "Enqueue,
   settle & the daemon cycle" section). The 14,769-line file is now covered
   end-to-end: queue I/O + lock internals (seize-quarantine-verify steal,
   token-identity release, non-reentrant 30 s acquire), scope partition,
   godspeed-envelope gate, the mint + admission battery (dedupe → dep/chain
   existence → afterChains root/dead-terminal → scope overlap → result-path
   collision → capacity relief that WRITES mid-admission), batch `@N` sibling
   refs, 90-day compaction (distinct from the JSONL relief archive), the
   receipt-verdict memo (stat-keyed, `<=` age boundary, soft
   `dispatch_snapshot` rebinding, `unboundAdmission`), `reconcileQueue`'s
   full ordered rule set (head sweeps → deferred/parked re-mint scans →
   per-task mission arms → catch/finally → orphan flagging), auto-reap
   (settlement-licensed; re-derivation with total reason/cause vocabulary),
   the durable-episode latch machinery (`emitLatched`/`{kind}_closed`/
   `*_recovered`; DURABLE_TELEMETRY_KINDS = {ledger_event_drift,
   ledger_terminal_verdict_revision} only; mutation=touch vs
   deletion=persist-only asymmetry), `runCycle`'s 12-step pass, and `main()`'s
   verb surface (incl. undocumented `precheck`).

2. **`ufo-sighting-lib` internals** (`corpus/knowledge/sighting-wall.md` +
   SKILL.md wall section): manifest persistence model (revision++,
   1 MiB write / 16 MiB read asymmetry, dir-lock seize protocol), pane
   lifecycle (`spawn-pane` adoption rule, `__pane-run` self-attestation
   quadruple, `stopMission`-in-finally, `resume` successor gate
   `RESUME_SUPERSEDED`, `complete` receipt gate + `COMPLETED_CAPTURE_LINES=0`),
   steer/peek transport (`send-keys -l` single invocation, 4096-byte text
   bound, seq pin), the four-source observation model (transcript oracle,
   spark store, L0 tick, dispatcher sidecar — never pane content), and 13
   verified boundary crossings.

3. **the-tick ground-handler gap closed** — `ufo-ground-handler.mjs` serves
   FOUR ops on a one-line-JSON socket: `health`, `freshness_ping`,
   `path_ping`, `chat` (the only model touch). SKILL.md updated.

Plus three core-runtime support-family notes (`native-admission-detail.md`,
`cost-and-profile.md`, `runtime-support.md`) — seats/admission-text/rules
attribution, cost-ledger validation + lineage walk, route catalog +
FailureClass authorities, lane_overlay/lease/live.

## Corrections (playbook got truer this round)

- **"Only the dispatcher writes pending-work.json" is FALSE.** Sentinel
  falsified it: `ufo-l0-monitor.mjs` is a sanctioned heal-only second writer
  under its own dir-lock port (writes at :1419/1431/1459/1467 via its
  `writeQueue` :226-232 — `writeFileAtomic` WITHOUT `revision++` or
  `validateQueue`, so revision is non-monotonic across heals). SKILL.md
  anti-pattern 9 rewritten as the two-writer rule.
- **`permits_advance` is `execution_profile.rs:448`** — :447 is the
  `#[must_use]` attribute line; three corpus entries mis-cited it (fixed).
- **Critic falsified my reconcileQueue head-order claim** — actual order is
  `sweepGraceDeferLatch` → `sweepRowFaultLatches` → `pruneAdmissionLatch`;
  the source comment "runs at the top" contrasts vs `claimNextTask`, not the
  sweeps.
- Reviewer caught systematic L-drift in the tail map's latch citations
  (~15-45 lines low); scout rev-2 re-verified every start line against
  source.

## Cross-domain reports (reported, not owned)

1. **Judge/producer parity break — `is_format_char`.** The judge strips
   exactly `\p{Cf}` (native_admission_text.rs:52-61); the JS producer's
   `FORMAT_CHARS_RE` strips `\p{Cf} ∪ \p{Mn} ∪ 6 Zs separators`
   (ufo-credential-screen.mjs:55-75). An Mn/Zs-split credential shape (e.g.
   U+00A0/U+0301) diverges: producer re-joins and screens it, judge does not —
   `native_telemetry.rs:493-507` can refuse a producer-conformant handoff.
   Fail-closed direction; UNPINNED on both sides (all split-shape tests use
   Cf only: ufo-credential-redact.test.js:63, native_tests.rs:7210). Fix
   belongs in ufo-fsd-alpha.
2. **`l0-monitor` queue writes bypass dispatcher invariants** — no revision
   bump, no validateQueue, no credential/size bound (ufo-l0-monitor.mjs:
   226-232). Playbook-worthy warning; blast radius bounded (heal-only rows).
3. **`ufo-sighting-lib/queue.mjs` honors out-of-root queue paths** that the
   dispatcher/monitor refuse — disclosed as `queueEscapesRoot`, fixture-
   driven, documented (:167-178).

## Method

13 L2 lanes total this round (mission mandate ≥8/batched call satisfied:
10 in one call + 3 scouts first): 2 scouts split the dispatcher tail at its
own boundary, 1 mapped sighting-lib, 3 mapped Rust support families, 1
scouted the planner work-order, 1 executor drafted the SKILL.md section,
1 scribe censused every durable-telemetry callsite, 1 critic falsified
verbatim parent claims (caught A1's head-order error), 1 reviewer audited
map citations (caught the L-drift), 1 sentinel falsified the ownership
invariant. Parent verified the riskiest claims directly: reconcileQueue
+ runCycle + emitter latch + main() read line-by-line; admission relief
write, verdict machinery, `permits_advance` body, monitor writeQueue,
format-char sets, cost-ledger call sites, `correlation_group_for` order,
`live.rs` transport — all confirmed against source.

## Evidence

Origin repo `ufo-fsd-alpha`: `fleet-dispatcher.mjs` (rev sha 44a3c781…,
14,769 lines) L95-200, L5713-8645, L8680-14769; `ufo-sighting-lib/` 26 files;
`ufo-l0-monitor.mjs` :201-253/:1411-1467; `ufo-ground-handler.mjs`
:99-163/:680-760; `crates/ufo-core-runtime/src/{execution_profile,
native_admission_text,cost_ledger,native_seats,lane_overlay,lease,live,
native_admission_rules}.rs`; `ufo-credential-screen.mjs` :55-75. Full scout
maps (cited, rev-pinned): `local://kumitate-r6-dispatch-ingress.md`,
`…-dispatch-tail.md` (rev 2), `…-sighting-lib.md`, `…-native-seats.md`,
`…-cost-ledger.md`, `…-runtime-support.md`, `…-ledger-census.md`,
`…-critic.md`, `…-review.md`, `…-sentinel.md`, `…-connect.md`, `…-plan.md`.

## Remaining gaps (README updated)

- `ufo-core-runtime` remainder: `l3_swarm`, `distill.rs`, `native_ledger`,
  `native_seat_coverage`, `native_transcript`, `local_ship`/`bounded_fs`/
  `fs_durability` internals. Round-7 order drafted (`local://kumitate-r6-plan.md`).
- fleet-dispatcher `queueSummary` per-field semantics.
- Wall layout/display engine depth.
