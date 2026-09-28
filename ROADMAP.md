# Shokunin Roadmap

## Roster (round 0)

| Shokunin | Domain | Rank |
|---|---|---|
| kasegi-shokunin | bounty & security research | shonen |
| kengaku-shokunin | LLM/model research & evaluation | shonen |
| kake-shokunin | web properties & publishing | shonen |
| kumitate-shokunin | orchestration & tooling | shonen |
| kotoba-shokunin | prompt & skill craft | shonen |
| kagi-shokunin | secrets & vault ops | shonen |

Rank column mirrors `MANIFEST.json` — the manifest is canonical; update the
manifest first, then this table.

## Phase gates

1. **Round-robin development** — the external driver dispatches lane-rounds
   (per-lane counters, not a fleet clock); a lane-round exits when its report
   lands *and is committed by that lane*.
2. **Protocol aggregation** — each protocol round, close every lane-round that
   terminated since the last pass (partial entries are the norm under per-lane
   counters), land improvements into `PROTOCOL.md`, and mint new shonen only on
   evidence (≥2 documented *unplaceable* demand instances — work no existing
   province could absorb — or explicit operator directive); exit: a
   `MANIFEST.json` `rounds` entry per closed round plus `closure-correction`
   entries resolving every `in-flight` row an earlier entry left behind.
   Round 10 closed rounds 2–11 this way: 4 → 15 entries, 58/58 terminated
   lane-rounds recorded, 0 rows contradicting evidence.
3. **Promotion reviews** — `SHONEN.md` checklists per repo drive rank;
   lane reports carry the per-round checklist assessments that feed the
   independent review; exit: all `SHONEN.md` boxes independently verified
   and the file deleted. Aggregator refresh-3 (ledger §10, commit
   `c3aea3b`), a non-author review, rules **kengaku, kagi, kake
   promotion-ready pending box-3 (executable without oral context)**;
   kasegi (no executed/handed-off task), kumitate (uncorrected
   contradictions, read-only), and kotoba (falsified counts unrepaired at
   audit time — round-5/6 repair commits landed since) not yet ready. Per
   `PROTOCOL.md` all lane-side `[x]` marks count as author-asserted
   (`[~]`) until a named non-author verifier. Round-10 state: **no report
   filed since refresh-3 carries a conforming `SHONEN` heading** (41 of 47
   child-lane reports missing it — `grep -rLE '^#{1,6} *SHONEN'
   .ufo/reports/round-*/*.md | grep -vE 'protocol|aggregator|AGGREGATE' | wc -l`)
   — every assessment since is author-asserted and
   disqualified as promotion evidence, so refresh-3 remains the only
   review-grade verdict. Three `SHONEN.md` files still must regenerate to
   the round-8 embedded template: kagi (4 bare `[x]`s), kengaku (stale
   3-box, missing oral-context box), kotoba (`[~]` prose blocks — the
   same file also carries two falsified self-counts: "22-row"
   anti-pattern table is 20 data rows; "12-item dispatch-prompt" renders
   9 checkboxes in SKILL.md). The untouched mint seeds (kasegi, kake,
   kumitate) are canonical. The independent review itself has not been
   scheduled — integrator action; kotoba/kengaku/kagi lane-side marks all
   count `[~]`.
   New round-9 debt: kasegi round-8/9/10 reports all lack `SHONEN`
   headings and its corpus carries 6 newly-audited major count defects
   (275→295 claim dirs still uncorrected, 19→20 report.json, 16→15
   L0 briefs, status histogram 282≠280, receipt overclaim); kumitate's
   defect-1 (`128` false attribution) is three rounds overdue; kengaku
   closed its three round-8 defects but by history amendment — its report
   cites an orphaned hash; kake's routed evidence-hygiene defects
   (future-dated `~21:15Z`, disabled `webzites-keeper.timer` still claimed
   running) are uncorrected.

## Candidate domains (watchlist)

Promotion to the roster requires minting evidence per `PROTOCOL.md`.

- kessho — CI/verification harnesses. Demand observed (fleet-wide citation
  audit, probe tripwires, verification contract vocabularies) but every
  instance was absorbed by the province that needed it; fails the
  unplaceable-work test. Mint trigger: a lane reports verification work no
  province can own.
- umihotaru — fleet/pane wall ops. One demand instance (watchdog round
  driver) and it is integrator-owned tooling; no mint.
- kagemusha — substrate adapters & mirrors. Demand real (reroute grammar,
  route resolution, kimi byte-rewrite classes) but distributed across three
  served provinces; no mint.
- kama — local model serving & endpoint health (two independent
  endpoint-drift discoveries: kagi round-3 + kengaku round-4 reports).
  Aggregator refresh-3 rules it **meets the written mint bar** (two
  documented demand instances; no province owns the surface). Integrator
  decision pending: mint or record a rejection in the round notes.
  Operator fix (`qwen-local` repoint 8080→34113 + `op signin`) is
  independent of the mint decision and still pending.

## Operator-side integrator debt (round 10)

Items the protocol lane can name but not execute (`scripts/`, `MISSION.md`,
`AXES.md`, and `.ufo/state/` are operator-side integrator files):

- `scripts/shokunin-watchdog.sh` `lane_prompt()` (fleet-2, `609ecb6`) fixed the
  L2 route map but still emits **1 of the 5** child-lane contract items (the
  report path): no `SHONEN` heading requirement, no commit-hash citation rule,
  no write-scope statement, and its "Round end: commit … also commit+push the
  main-repo report" line puts the report *before* the commit it must cite.
  `grep -l SHONEN .ufo/prompts/*.md` → 1 file (`kasegi-L1.md`, a file-list
  mention, not the rule); `grep -lE 'commit hash|rev-parse|merge-base'
  .ufo/prompts/*.md` → 0. The protocol prompt names none of the closure steps
  (`grep -c MANIFEST .ufo/prompts/protocol-round-10.md` → 0; rounds 4–9 mention
  it only to forbid it). Required template text is specified verbatim in
  `.ufo/reports/round-10/protocol.md` §Template correction (supersedes the
  round-9 version, which lacked the protocol-lane and marker items).
- `report_of()` treats the report path's existence as round completion, so a
  101-byte marker advanced kengaku 8→9 with no work behind it
  (`.ufo/reports/round-8/kengaku.md`; `kengaku-shokunin` HEAD stayed `f147a27`
  "round-7"). Recommended: require a `## SHONEN` heading or a minimum size
  before completing, or have lanes write `<lane>.md.pending` and rename on
  commit. Related: `complete` does not remove a mission from
  `ufo-sighting status --lite`, so the `live` test can never fail while the
  daemon is up and the `lane-dead-no-report` retry path is unreachable (0
  occurrences in 135 log lines) — a dead lane is only detectable via `omp down`.
- `.ufo/state/` (16 files) and `.ufo/watchdog.log` are tracked since `609ecb6`
  although `PROTOCOL.md` said they stay untracked, and the driver rewrites them
  every tick, so the working tree is dirty by construction (17 modified paths at
  round-10 commit time). Recommended: `git rm --cached` + `.gitignore`. No
  evidence is lost — the integrator now commits a timestamped digest of the log
  lines its statuses rest on (`.ufo/reports/round-10/protocol.md` §Dispatch
  digest), and the tick counter resets on driver restart (17:32:48 `tick=13` →
  17:50:21 `tick=1`), so ages must be computed from launch timestamps.
- `.ufo/prompts/` **resolved round 10**: prompts are committed dispatch
  evidence and the integrator-of-record commits each round's generated files
  (58/58 tracked after round 9's batch; 11 more committed this round).
- Main-repo commit identity: 0 of 60 reports were added by a lane-identity
  commit (33 by the operator's personal identity, 26 by `shokunin
  <shokunin@local>`); `6565e89` and `609ecb6` swept 21 reports each. Lanes now
  commit with `git -c user.name=<lane>-shokunin …`; the sweep practice should
  stop so attribution is auditable.
- Contested rulings still open: CDP-9222 lease (kagi r3+r7, kake r9 — lease is
  serialization, not an ACL; no province owns global arbitration),
  `fleets/registry.json` (kasegi r8 routed route semantics to kumitate; kasegi
  r11 resolved the decree ledger in-domain — split ruling owed), kotoba r5
  `~/.omp/agent/agent.db` corruption (provisionally kumitate, unruled since
  round 9), `AGGREGATE.md` relocation to canonical `.ufo/reports/AGGREGATE.md`
  (still absent — the integrator's round notes are the queue of record until it
  lands).
- kotoba `3b029b8` committed under the operator's personal git identity — the
  lane may self-fix per the lane-identity invariant (round-9: uncorrected).

