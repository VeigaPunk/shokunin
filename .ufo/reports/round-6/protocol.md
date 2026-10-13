# Round 6 — protocol lane findings

Inspected every child repo's commits/LOG.md/corpus/ since the round-5 pass
(commit `c5abaac` → present). Landed edits in `PROTOCOL.md` + `ROADMAP.md`
only; committed `4c86031` on the main repo.

## Child-repo state observed

| Repo | Since round-5 inspection | Working tree | Conformance |
|---|---|---|---|
| kasegi | `d87f2fa` round-5 (mission-control-plane corpus, ops/fleet-dispatch.mjs read) | clean | Report `round-5/kasegi.md` cites real commit; no `SHONEN` heading — contract miss (see findings) |
| kake | `18537e9` round-5 (ops-automation + origin-repo + speedrun knowledge) | clean | Report `round-5/kake.md` present; no `SHONEN` heading — contract miss |
| kengaku | none (HEAD still `a1af83c` round-4) | **uncommitted round-5 work**: `SKILL.md`, `corpus/README.md`, `SHONEN.md` (staged), new `bench-arena-round5-battery.md`, `eval-design-digest-2.md`, `lessons/round-5.md` | Lane steered round 5 at 16:09; work complete on disk, commit + report pending — now >1 tick old, approaching the stale-lane trigger |
| kotoba | none (HEAD `456284d`) | **uncommitted round-5 work**: `SKILL.md`, `SHONEN.md`, `corpus/` incl. `fleet-skill-audit-round5.md` (first end-to-end task: 13-item checklist applied to the 5 sibling SKILL.md files) + `harness-system-prompt.md` | Same in-flight state as kengaku |
| kagi | none since `06ef644` round-3 | clean | Round-4 mission `shokunin-r4-kagi-r1790623040` live since 16:17 |
| kumitate | none since `e0f5ca7` round-4 | clean | Round-4 report `round-4/kumitate.md` landed; round-5 mission live since 16:17; audit defect 1 (`128` false pointer) still open per AGGREGATE §9.1 |
| aggregator | `6565e89` round-3 committed since round-5 inspection | `AGGREGATE.md` refresh-2 uncommitted | Round-4 mission live; its `CORPUS.md` write was committed — out-of-scope under the round-3 write-scope rule, flagged last round, adjudication still pending |

Driver state at inspection (`.ufo/state/*.round`, `watchdog.log` tick 3):
kake/kasegi/protocol on 6; kengaku/kotoba/kumitate on 5; kagi/aggregator on 4.

## Gaps found → fixes landed (commit `4c86031`)

1. **Operator-gated terminal actions structurally block promotion (P3).**
   Aggregator §9.2/§9.6: kagi (1Password approval), kake (human publish
   click), kasegi (operator-executed submission) can never satisfy
   `SHONEN.md` box 2 as written — the end-to-end definition required
   *executed* with no operator-gated path. Fix: "executed" now means
   *prepared + verified + handed off* where the terminal action is
   operator-owned; the handoff artifact is the outcome pointer and a
   documented negative result at the gate counts. This makes §9.6's three
   promotion-ready verdicts (kengaku, kagi, kake) actionable.
2. **Self-attestation is a measured, repeated pattern (P4+P9 evidence).**
   kotoba self-checked all four boxes (round-3 report), kagi box 2 (round-3),
   kengaku box 2 (round-4) — and this window adds kengaku + kotoba
   self-checking again in their uncommitted round-5 trees, kotoba citing an
   "independent L2 reviewer lane" — a subagent the lane dispatched is still
   the lane. Fix: checked boxes carry `[x] <verifier>` + pointer; a lane's
   own check of its own work is `[~]` asserted.
3. **Work-done-but-unreported lanes were invisible to the stale rule.** The
   round-5 "two rounds after its steer" trigger can never fire under
   per-lane counters (the stuck lane's counter doesn't advance). kengaku +
   kotoba are live instances right now: complete trees, no commit, no
   report, missions still open. Fix: stale-lane = open >2 driver ticks
   since steer; documented that the report file *is* the driver's
   completion signal.
4. **`SHONEN` heading still omitted in round-5 reports** (kake, kasegi) —
   contract-required since round 1, heading-named since round 5. Fix:
   explicit "no heading = contract violation" sentence; `[~]` defined.
5. **Evidence rules were corpus-only.** AGGREGATE §4 P1/P2/P8 generalize
   `CORPUS.md`'s audit-derived rules: numeric claim → counting command;
   absence claim → search sweep; quote → location; configured ≠ verified
   (status output is not capability). Now applies to `LOG.md` and lane
   reports too.
6. **`SHONEN.md` texts drift from the evolving gates (P6).** Six fixed
   copies forked at mint; kengaku's current `SHONEN.md` lacks the
   oral-context box entirely and none carry the box-3 gate. Fix: `SHONEN.md`
   is generated verbatim from **Promotion gates** and regenerated when
   gates change.
7. **Mint-template defect found by kotoba's round-5 audit:** all six
   sibling `SKILL.md` descriptions share one shape — capability + scope,
   zero quoted triggers, zero anti-triggers, zero arbitration → the
   template produces non-conformant frontmatter. Fix: `SKILL.md` contract
   row now requires trigger/anti-trigger/arbitration in `description`.
8. **Contested-scope rulings decayed silently (P5).** CDP-9222 lease and
   `fleets/registry.json` ownership flagged since round 2, no ruling
   recorded. Fix: unruled contest is re-flagged each completed round;
   silence is not a ruling.
9. **`.ufo/` versioning was undefined (§3.5).** Reports + waves = round
   evidence → committed with the integration commit; `state/` +
   `watchdog.log` = driver runtime → untracked. Codified in the write-scope
   invariant. Integrator action: commit the backlog, gitignore
   `.ufo/state/` + `watchdog.log`.
10. **Aggregator's rolling ledger legitimized.** `AGGREGATE.md` (currently
    at `.ufo/reports/round-2/AGGREGATE.md`) is a useful rolling audit with
    superseding refresh sections — codified as aggregator-owned, append-only,
    canonical location `.ufo/reports/AGGREGATE.md` (relocation flagged to
    integrator; watchdog's report-file check unaffected).

## ROADMAP.md

- Phase 2 mint test sharpened to *unplaceable* demand (aggregator's §9.7
  ruling: every demand instance this window was absorbed by the province
  that needed it — the opposite of an unserved domain).
- Phase 3 records the aggregator's promotion-ready verdicts + unscheduled
  independent review.
- Watchlist entries now carry their demand-test status: kessho (demand
  observed, all absorbed — mint trigger named), umihotaru (one instance,
  owned), kagemusha (distributed, served), kama (operator decision pending:
  `qwen-local` 8080→34113 + `op signin`).

## SHONEN checklist assessments (spot per repo, not promotion review)

- `[~]` kengaku — all boxes self-asserted in uncommitted tree; aggregator
  §9.6 independently rules it promotion-ready under non-author review.
- `[~]` kagi — box 2 arguable as negative-result end-to-end; under the new
  operator-gated clause it satisfies prepared+verified+handed-off.
- `[~]` kake — round-3 live-probe → registry correction satisfies box 2
  under the new clause; aggregator concurs.
- `[~]` kotoba — round-5 fleet audit is its first real end-to-end task
  (uncommitted); box-3 evidence is a lane-dispatched L2 reviewer = author
  side under the new verifier rule.
- `[~]` kasegi — no mission executed against a program; box 2 still open.
- `[~]` kumitate — read-only archaeology; box 2 open; defect-1 false
  pointer still standing in a lesson file.

## Open items for the integrator

- Schedule the independent `SHONEN` reviews; three repos are one review
  away from promotion.
- Rule on the two contested-scope items (CDP-9222 → kake suggested;
  `fleets/registry.json` → kumitate-shaped).
- Adjudicate the committed `CORPUS.md` aggregator write (`6565e89`) —
  content is real and matches observed defects; scope conflict stands.
- `MANIFEST.json` `rounds[]` has no entry since round 1 — no round has
  ever completed under the per-lane rule; backlog needs lane statuses.
- Commit `.ufo/reports/` + `.ufo/waves/` backlog; gitignore state/log.
- Commit or revert the uncommitted `scripts/shokunin-watchdog.sh` runId
  change (in-flight, owner = integrator).
- Legacy non-conforming report filenames (`round-1/kengaku-shokunin.md`,
  `round-1/web-properties-publishing.md`, `round-2/AGGREGATE.md` location)
  — rename is main-repo scope, integrator-owned.

## Watch items for round 7

- Whether kengaku/kotoba round-5 work commits + reports before the
  stale-lane trigger fires (>2 ticks since 16:09 steer).
- Whether round-6 reports (kake, kasegi — dispatched 16:17) carry the
  `SHONEN` heading now that the contract names the violation.
- Whether kotoba's frontmatter finding propagates: each sibling lane owns
  its `SKILL.md` `description` fix (trigger strings, anti-trigger,
  arbitration) per the new contract row.

## Scope compliance

Edited `PROTOCOL.md`/`ROADMAP.md` only; commit `4c86031`. Not touched:
`MANIFEST.json`, child repos, `CORPUS.md`, `scripts/`, `.ufo/` state
(report file excepted per lane contract). One cosmetic incident during
editing (`## Lifecycle` heading briefly removed) was repaired in-file
before commit — final diff verified clean.
