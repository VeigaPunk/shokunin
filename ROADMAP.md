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
   (`[~]`) until a named non-author verifier; kotoba has re-attributed its
   file to `[~]` itself, kagi's four bare `[x]`s count as `[~]` by rule.
   Three `SHONEN.md` files are marked/prose variants that must regenerate
   to the round-8 embedded template (kagi, kotoba, kengaku — kengaku's is
   a stale 3-box file missing the oral-context box); the untouched mint
   seeds (kasegi, kake, kumitate) are already canonical. The independent
   review itself has not been scheduled — integrator action.

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

