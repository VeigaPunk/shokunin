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
   into `PROTOCOL.md`; mint new shonen only on evidence (≥2 documented demand
   instances or explicit operator directive); exit: `MANIFEST.json` `rounds`
   entry appended with every lane's terminal status.
3. **Promotion reviews** — `SHONEN.md` checklists per repo drive rank;
   lane reports carry the per-round checklist assessments that feed the
   independent review; exit: all `SHONEN.md` boxes independently verified
   and the file deleted.

## Candidate domains (watchlist)

Promotion to the roster requires minting evidence per `PROTOCOL.md`.

- kessho — CI/verification harnesses
- umihotaru — fleet/pane wall ops
- kagemusha — substrate adapters & mirrors

