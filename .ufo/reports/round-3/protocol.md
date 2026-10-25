# Round 3 — protocol lane findings

Inspected all child-repo commits/LOG.md since round 1 (covers round-2 interval;
no round-2 steer reached this lane). Landed edits in commit `68294b4`
(PROTOCOL.md + ROADMAP.md only).

## Child-repo state observed

| Repo | New commits since seed | LOG.md round entries | Notes |
|---|---|---|---|
| kasegi | 2× round-1 | 1 round-1 entry (rich evidence) | Uncommitted round-2 work in progress: `SKILL.md`, `corpus/README.md` modified, `corpus/knowledge/claim-gates.md` untracked |
| kengaku | 2× round-1 | 2 round-1 entries | PROVINCE.md still declares absent `~/wikillm/llm-wiki` — lane grounded on real path but did not correct the surface |
| kake | 1× round-1 | 1 round-1 entry | — |
| kumitate | 1× round-1 | 1 round-1 entry | — |
| kotoba | 1× round-1 | 1 round-1 entry | reviewer lane returned SHIP |
| kagi | none | none | `corpus/` exists (aggregator-seeded, uncommitted); kagi-L1 prompt landed 15:50 after MANIFEST already recorded `not-dispatched` |

## Gaps found → fixes landed

1. **Aggregator lane invisible to protocol.** `aggregator-L1.md` writes
   `corpus/` into every child repo — would have violated my round-1
   write-scope invariant. Fix: aggregator defined as a main-repo lane; it is
   the *sole* exception to write-scope, corpus-only.
2. **Report naming drift.** Round-1 produced `kengaku-shokunin.md`,
   `web-properties-publishing.md` alongside conforming `<id>.md` names —
   fragile for aggregation. Fix: report path codified as
   `.ufo/reports/round-<N>/<id>.md` where `<id>` is the roster id.
3. **Rounds-entry schema divergence.** Integrator used `lanes` as a map with
   `in-flight`, `type`, `protocol_updates`, `minted` — my round-1 schema said
   array + `mints`. Fix: schema aligned to integrator's landed shape; `status`
   extended with `in-flight` while the round is open; early-write-and-correct
   allowed, but **no lane may be recorded `not-dispatched` while a dispatch or
   prompt for it exists** (kagi case).
4. **External round drivers unacknowledged.** `shokunin-watchdog.sh` steers
   each lane per round at 450s ticks. Fix: rounds are externally driven; steer
   names the round number, lane owns content, round numbers monotonic.
5. **PROVINCE drift uncorrected.** kengaku's surface `~/wikillm/llm-wiki`
   absent; lane worked on `~/Projects/webzites/repos/llm-wiki` without fixing
   PROVINCE.md. Fix: PROVINCE.md contract now requires declared surfaces to
   resolve; finding a moved/absent surface obligates a logged correction.
6. **Corpus contract orphaned.** Integrator added the `corpus/` contract row
   (commit e183bc1); corpus rules lacked protocol-level evidence binding.
   Fix: invariant — every `knowledge/` entry cites a resolvable source;
   `lessons/` entries cite round + LOG/report.

## ROADMAP.md changes

Phase gate 1 now includes the aggregator lane; gate 2 exit requires terminal
statuses in the `rounds` entry.

## Open risks / next-round watch items

- kagi's `corpus/` is uncommitted and untracked — aggregator's write-scope
  exception covers it, but kagi's own lane must claim/commit it inside its
  repo or it stalls in limbo.
- MANIFEST round-1 entry is already written with `kagi: not-dispatched`;
  protocol now obligates the integrator to correct it when kagi reports.
- SHONEN.md checklists remain fixed text seeded at mint; if gates evolve they
  drift — consider deriving at mint time (integrator-owned).
- Two lanes (kasegi, kengaku) did 2 commits in round 1 vs 1 elsewhere — no
  problem, but watch that "one lane per round" doesn't become "one commit per
  round" in lanes' mental model.

## Scope compliance

- Edited: `PROTOCOL.md`, `ROADMAP.md` only. Commit `68294b4`.
- Not touched: `MANIFEST.json`, child repos (read-only), `.ufo/` steering files.
