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
   and the file deleted. Aggregator audit (`AGGREGATE.md` ledger, §9.6)
   finds kengaku, kagi, and kake promotion-ready under non-author review;
   kengaku's box 2 is strengthened by its authored round-5 full-battery
   run (`kengaku-shokunin@782dd2d`). Round-5 additions: kagi and kotoba
   self-checked every remaining box; per `PROTOCOL.md` all lane-side
   `[x]` marks are author-asserted (`[~]`) until a non-author verifier
   names itself. The independent review itself has not been scheduled —
   integrator action.

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
  Operator decision pending: `qwen-local` repoint 8080→34113 + `op signin`.
  Configuration-fault discovery is not yet recurring demand; hold.

