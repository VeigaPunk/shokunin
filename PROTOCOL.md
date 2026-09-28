# Shokunin Protocol

> 職人 — an artisan specialist that earns its domain through demonstrated craft.

A **shokunin** is a domain specialist, distinct from generic agents: it owns a
domain, accumulates hard-won knowledge, and is iterated by rounds of swarm work
until it can iterate itself.

## Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan of a domain) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted when a domain demand is proven (repeated operator need or
  a demonstrated knowledge gap). It starts with a scoped `SKILL.md` +
  `PROVINCE.md`, an empty `LOG.md`, and a domain record in `MANIFEST.json`.
- **Shokunin** — promoted when it demonstrably performs domain work end-to-end:
  its skill file carries real decision tables, error patterns, checklists, and
  cited sources — not generic advice; its `LOG.md` shows completed rounds; and
  a reviewer can execute the written instructions without oral hand-holding.
- **Jin'i-ryu** — promoted when it can iterate on itself: given a round's
  telemetry it proposes and lands its own improvements (falsifiable deltas in
  `LOG.md`), with the main repo aggregating only promotion/mint decisions.

## Round-robin rounds

Each round, the orchestrator dispatches one swarm lane per shokunin (round
robin across the roster). After a full round the integrator:

1. Reads every lane report.
2. Lands warranted protocol improvements in this file (a highly valuable
   feature discovered by any domain generalizes to the protocol).
3. Mints a new shonen only if evidence shows an unserved domain.
4. Records the round in `MANIFEST.json` (`rounds` array) and each shokunin's
   `LOG.md`.

## File contract per shokunin repo

| File | Purpose |
|---|---|
| `SKILL.md` | The specialist's craft: triggers, decision tables, error patterns, checklists, cited sources |
| `PROVINCE.md` | Domain boundary: what it owns, what it refuses, its work surfaces |
| `LOG.md` | Iteration log: round entries, accepted changes, falsifiable next-iterations |
| `SHONEN.md` | Promotion checklist to shokunin; deleted on promotion |
| `AGENTS.md` | Operating rules when working inside this repo |

## Invariants

- Specialize, don't generalize: a shokunin's `SKILL.md` contains *cited,
  verifiable* knowledge of its domain — never generic agent advice.
- One domain per shokunin; a domain belongs to one shokunin.
- Rounds are evidence-driven: every `LOG.md` entry cites the work that motivated it.
- Local-first: repos live locally; publishing is operator-owned.
