# Kumitate — Round 57

## Work performed

Declared claims:

1. **C1 — operability, lowest non-retired axis:** acquire the `readme-map`
   capability (`kumitate-readme-map-v1`), the corpus file↔README-row bimap
   gate (`scripts/readme-map.mjs` + `.ufo/pins/readme-map.json`). It turns the
   count-only C2 proxy term into a per-file contract that names WHICH corpus
   file lacks its `corpus/README.md` map row — the defect class routed as
   R56-V3, now on its third recurrence.
2. **C2 — coverage frontier (learning, sourced):** add
   `corpus/knowledge/worker-heartbeat-liveness.md`, the durable-execution
   frontier's liveness-signal side, sourced on S117 (Temporal detecting
   activity failures), S118 (Kafka 4.3 consumer configs) and S119
   (Kubernetes liveness/readiness/startup probes), with S120 (RabbitMQ
   heartbeats) opened and rejected.

- Added `scripts/readme-map.mjs`, its 14-case hermetic suite and
  `.ufo/pins/readme-map.json` (135 covered paths). `README_MAP: CLEAN
  files=135 rows=135 covered=135`; `--selftest` 14/14 (close receipts under
  `.ufo/waves/round-57/close/selftests.txt`).
- Registered `pin.readme-map` in the separate gate-pin map of
  `scripts/proxy-check.mjs` (parent-frozen stanza keys untouched;
  `pin.proxy-check` re-pinned); strict proxy reads `PROXY: MATCH (A=90 C=27
  operability=9; C1=19/19 C2=135/135 coverage=10; …)`. New `SCORECARD.md`
  capability row and SKILL.md gate row; the verifiable checklist grows to 27
  items.
- Added the frontier entry plus S117–S120 rows: three mined-and-captured
  admissions and S120 opened-then-rejected (AMQP heartbeats are TCP
  connection liveness, not worker/task liveness). All 13 entry clauses are
  bound to distinct committed receipts under
  `.ufo/waves/round-57/build/Scout{TemporalHb,Kafka,K8s,Queue,RabbitmqHb}/`;
  `sources-check` reads
  `CLEAN (rows=120 tiers=A:99,B:13,C:8 status=queued:12,mined:88,rejected:20 entries_with_source=14 legacy=38)`.
- Routed-defect answers (append-only; filed bytes unchanged):
  - **R56-V1 — L2 floor unmet (prepared-undispatched wave).** The orchestrator
    dispatches waves between rounds, so this round prepares, validates and
    reports its wave the same way and spawns nothing (see the wave bullet
    below).
  - **R56-V2 — stale frozen A54/A55 exactly-N literals.** Chosen shape:
    append-only correction plus a frozen convention, not a re-pin of old
    counters. A57's B7 arm binds `items === 27` AND every item id→gate
    mapping (24 counter-pins, 25 source-capture, 26 source-dupes, 27
    readme-map). Future capability moves must re-express every binding, never
    only the newest. The frozen A54/A55/A56 counters stay byte-identical and
    read 9/10 at R1 on their B7 count arm only — named counter-obsolescence,
    recorded in `close/prior-probes.txt`.
  - **R56-V3 — spotcheck lesson without README map row.** The row for
    `corpus/lessons/round-56-verifier-spotcheck.md` is restored (base proxy:
    `C2_TOTAL_DRIFT declared=132 computed=133`), and the class is now gated by
    C1 (QUALITY Q48).
- Prepared **one v2 wave** under policy v2: 64 seats; executor 19, reviewer 13,
  scribe 8, scout 7, critic 6, mutation-tester 5, simplifier 2, sentinel 2,
  revenger 1, connector 1. Attack roles (reviewer+critic+mutation-tester)
  24/64 = 37.5%; planner seat held by the L1. Spec, validation, taskCall and
  registry committed at `.ufo/waves/round-57/w1-spec.json`,
  `w1-validate.json`, `w1-taskcall.json` and `w1/swarm-registry.json`.
  **Prepared-but-undispatched:** no seats spawned, returned or killed;
  returned-without-report=0, dead=0, total=64 prepared. After the lane tip, at
  2026-10-24 12:50:32Z, a non-lane writer (presumably orchestrator wave
  tooling) rewrote the working-copy `w1/swarm-registry.json` into
  `ufo-swarm-registry-v1` (64 members, `agentId: null`) and preserved the
  committed file as `swarm-registry.legacy-wave-v1.json` (byte-identical). The
  L1 left both uncommitted and untouched.
- Pre-score witness (QUALITY Q43/M5): both frozen counters were run against a
  scratch post-state commit in a `/tmp` clone before scoring — A57 10/10, D57
  5/5 (`witness/`). The first witness attempts found two lane-artifact
  defects, repaired before R1 with counters untouched: the entry wrapped its
  clauses across lines (E2 read 0 bound), and one receipt path was shared by
  two clauses (E2 distinct 12/13). The first mutant transcript also deleted a
  single hold call; it was replaced by the all-hold-deleted mutant the B5c arm
  specifies (`held=0/0`, exit 1).
- Misroot sweep: the lane wrote no fleet-root files besides this report.
  `.ufo/state/*` and `.ufo/watchdog.log` untouched. Two misrouted IRC messages
  about kotodama's r67 counters reached this session: an alert from
  `L1-kotodama-r67.CriticFrontier` and the resolution from `L1-kotodama-r67`.
  Neither was acted on (cross-lane) or answered (no agent messaging channel in
  this session); the kotodama orchestrator should confirm the alert reached
  its own L1.
- Tool installs/updates: none. **Stale-lane:** respawn-per-round; no other
  kumitate mission open.
- Open L0 items carried, not changed: R41-2 gate-pins ruling, R43-1/R43-5, A3e
  captured-invocation, R53-2 seat-accounting convention. No new L0 question
  filed.

## Landed changes

- `f0dc6d1160e66af65355bd353665adac22bbf4a9` — R1, freeze + integrate (the
  measured close revision): plan, frozen counters A57/D57 v1, base receipts,
  witness files, time-spaced receipts (span ≥300 s) + doctored replay control,
  wave spec/validate/taskCall/registry, `readme-map` gate + registry +
  `pin.readme-map`, SKILL row + checklist item 27, SCORECARD stanza +
  capability row + move log + round-57 section, frontier entry + S117–S120
  rows + captures + lesson + README rows + PROVINCE + QUALITY Q48,
  counter-mutant transcript, LOG.md round-57 entry, R56-V1/V2/V3 answers.
- `b3bd0633aec43ad2559f980b400e4d7077e10af3` — **concurrent writer, not this
  L1 session**: committed this session's uncommitted R1 claim receipts
  (`close/FINAL-attest57-R1.txt`, `close/FINAL-doctrine57-R1.txt`,
  `selftests.txt`, `prior-probes.txt`), re-minted receipt run-3, and rewrote
  the mutant transcript and witness outputs.
- `798d4d23743487d0c642239ca54deba421021af3` — **concurrent writer**: a second
  set of close receipts scored at `b3bd0633` (`attest57-final.txt` 10/10,
  `doctrine57-final.txt` 5/5, `prior-counters-at-close.txt`,
  `sources-census-after.txt`, `harm-battery.txt`).
- `c42afe1c189f2a1ecbe175f6e4ea4f9065c138d7` — SCORECARD measured-commit slots
  filled with R1.
- `8c6f5b017d149b18134917378cdbed3b492d8e89` — idempotence re-run at the
  bookkeeping tip (`close/IDEMPOTENCE-c42afe1c….txt`): A57 10/10, D57 5/5
  (lane tip).

(Complete r57 lane-commit list. All five carry the lane identity, but two
landed from a concurrent writer — most likely a second live session on the
same round, e.g. an `omp` process running from the fleet root since 02:11.
Both claims were independently re-measured at its tip `798d4d23`: A57 10/10,
D57 5/5. The orchestrator should confirm that only one kumitate r57 L1 was
meant to be live and reconcile any second report it files.)

## Before → after measurements

**C1 — operability / `readme-map` capability.** Frozen command:
`node .ufo/waves/round-57/probe/attest57-probe.mjs /home/vgpnk/Projects/shokunin/kumitate-shokunin <rev>`.
At base `7178bfd3643c0fac74c8eb637cd6e985faadd0cf`: `ATTEST57_UNMET held=0/10
checks=10`, exit 1 (`base/attest57-base.txt`). At R1
`f0dc6d1160e66af65355bd353665adac22bbf4a9`: `ATTEST57_HELD held=10/10
checks=10`, exit 0 (`close/FINAL-attest57-R1.txt`); idempotence at the
bookkeeping tip also 10/10. `node scripts/readme-map.mjs` reads `CLEAN
files=135 rows=135 covered=135`; selftest 14/14. Operability is 9→9
(terminal): A=87→90, C=26→27, `floor(10×(A+C)/(A+C+3))` remains 9. The command
that would show it unmoved: the same probe at base (0/10), or `readme-map` on
the base tree (gate absent).

**C2 — coverage frontier / `worker-heartbeat-liveness.md`.** Frozen command:
`node .ufo/waves/round-57/probe/doctrine57-probe.mjs /home/vgpnk/Projects/shokunin/kumitate-shokunin <rev>`.
At base: `DOCTRINE57_UNMET held=2/5 checks=5`, exit 1
(`base/doctrine57-base.txt`). At R1: `DOCTRINE57_HELD held=5/5 checks=5`,
exit 0 (`close/FINAL-doctrine57-R1.txt`); idempotence also 5/5. The retired
coverage aggregate stays 10 after the R56-V3 repair restores C2/C2_total to
135/135; the frontier advance is the sourced entry, not a claimed scalar
increase.

## Sources & frontier

Frozen census command (run at round start and round end):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`.
Before — exit 0 with the four pinned W04 duplicate-URL warnings (S034, S068,
S084, S095); after — exit 0 with the same four warnings (`close/harm-battery.txt`,
standalone re-run section; the earlier `census_exit` line there is `tail`'s
exit and is superseded).

Row count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 116 before / 120 after. Tier histogram → A=96 B=12 C=8 before / A=99 B=13
C=8 after. New rows: S117/S118/S119 A admitted; S120 B rejected. Existing
status/recheck/used-by cells touched: none. Frontier advanced: durable-execution
and multi-agent failure research via its seventh sourced entry; it remains
Frontier, not Core.

- **S117 — admitted, tier A.** Temporal, Detecting Activity Failures,
  https://docs.temporal.io/encyclopedia/detecting-activity-failures; opened
  2026-10-24; "An Activity Heartbeat is a ping from the Worker that is
  executing the Activity to the Temporal Service."
- **S118 — admitted, tier A.** Apache Kafka 4.3 consumer configs,
  https://kafka.apache.org/43/configuration/consumer-configs; opened
  2026-10-24; `session.timeout.ms`: "The client sends periodic heartbeats to
  indicate its liveness to the broker."
- **S119 — admitted, tier A.** Kubernetes, Configure Liveness, Readiness and
  Startup Probes,
  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/;
  opened 2026-10-24; "Kubernetes provides liveness probes to detect and remedy
  such situations."
- **S120 — rejected, tier B.** RabbitMQ Heartbeats,
  https://www.rabbitmq.com/docs/heartbeats; opened 2026-10-24; AMQP
  heartbeats detect dead TCP connections at connection scope — transport
  keepalive, not worker/task liveness. Flip condition recorded in the row;
  reject receipt `build/ScoutRabbitmqHb/`.

Captured bodies + sha256 for S117–S120 are pinned in
`.ufo/pins/source-captures.json` (`SOURCE_CAPTURE: CLEAN captures=13
exemptions=107`); `SOURCE_DUPES: CLEAN groups=4 known=4` (no new duplicate).

## Trend verdicts

- **Expansion — improved.** One sourced entry advances the durable-execution
  frontier band (S117/S118/S119), S120 is kept as an explicit scope rejection,
  and `readme-map` enters the repertoire. Evidence: `corpus/README.md`,
  `corpus/SOURCES.md`, `SCORECARD.md` capabilities, D57 at R1.
- **Quality — improved.** A recurring coverage-map defect class (r52, r55,
  r56) is now mechanically gated with a 14/14 hermetic suite; all ten gate
  selftests, strict proxy, and the source gates read clean at close; the
  R56-V2 supersession convention is frozen into a scored arm instead of
  re-pinning old counters; QUALITY Q48 codifies the rule. Prior counters'
  item-count misses are named obsolescence, not hidden.
- **Discernment — unchanged pending outside review.** The lane records the
  S117–S119 admissions and S120 rejection but does not self-grade that taste;
  the independent non-author source-decision review is pending
  (`corpus/lessons/round-57.md` Spot-check line).

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited
  sources — `SKILL.md` §Gate registry / §Verifiable checklist (27 items);
  `SCORECARD.md` `readme-map` row.
- [~] At least one end-to-end domain task executed and logged — `readme-map`
  run/selftest; `LOG.md` round 57; measured R1
  `f0dc6d1160e66af65355bd353665adac22bbf4a9`.
- [~] Instructions executable without oral context —
  `node scripts/readme-map.mjs [--registry <path>] [--readme <path>] [--corpus <dirs>]`,
  the 14-case selftest, and the saved plan/counter contract.
- [~] No cross-domain bleed; PROVINCE remains accurate — `PROVINCE.md`
  frontier update stays in orchestration/tooling; sibling broker/workflow
  families remain open; the misrouted kotodama alert was not absorbed.
