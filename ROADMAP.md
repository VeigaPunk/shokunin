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

1. **Round-robin development** — lanes are dispatched by the external round
   driver (typically up to one per shokunin, plus the aggregator); exit: a
   completed round per `PROTOCOL.md` (every dispatched lane reported or
   recorded failed).
2. **Protocol aggregation** — after each completed round, land improvements
   into `PROTOCOL.md`; mint new shonen only on evidence (≥2 documented
   *unplaceable* demand instances — work no existing province could absorb —
   or explicit operator directive); exit: `MANIFEST.json` `rounds`
   entry appended with every lane's terminal status.
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
   (`[~]`) until a named non-author verifier. Round-9 state: **no report
   filed since refresh-3 carries a conforming `SHONEN` heading** (36/40
   child reports missing) — every assessment since is author-asserted and
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

## Operator-side integrator debt (round 9)

Items the protocol lane can name but not execute (`scripts/` and prompt
template are operator-side integrator files):

- `scripts/shokunin-watchdog.sh` `lane_prompt()` still generates prompts
  with **zero** of the five embedded contract items and the **stale L2
  route map** (`m_composer`/`m_antigravity` — outside the MISSION.md
  bucket). Required template correction is specified in
  `.ufo/reports/round-9/protocol.md` verbatim.
- `.ufo/prompts/` files accumulate untracked; decide whether prompts are
  committed evidence (recommended: yes — they are what the fidelity check
  audits) or ignored.
- Contested rulings still open: CDP-9222 lease (kagi r3+r7),
  `fleets/registry.json` scope, aggregator commit `6565e89` touching
  `.ufo/prompts/*` unadjudicated, `AGGREGATE.md` relocation to canonical
  `.ufo/reports/AGGREGATE.md`.
- kotoba `3b029b8` committed under the operator's personal git identity —
  fix `user.name/email` in `kotoba-shokunin` (lane may self-fix per the
  new lane-identity invariant).

