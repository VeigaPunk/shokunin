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

A shokunin with no `LOG.md` activity across two consecutive completed rounds is
flagged **dormant** by the integrator in the round notes; dormancy is a review
trigger for the operator, never an automatic retirement.

## Promotion gates

A promotion is a decision backed by artifacts, not a vibe. Every gate names its
verifier and its evidence.

- **shonen → shokunin.** Every `SHONEN.md` box checked by a reviewer who did
  not author the round's changes (a fresh lane or integrator review — never
  self-attestation). Minimum bar:
  - `SKILL.md` contains at least one decision table, one error-pattern list,
    and one checklist, each citing a resolvable source (repo path, command
    output, or external document).
  - `LOG.md` records at least one end-to-end domain task: trigger → action →
    outcome → evidence pointer.
  - `PROVINCE.md` still matches reality: no absorbed cross-domain work.
  On promotion `SHONEN.md` is deleted, `MANIFEST.json` rank is updated, and the
  review is recorded in the promoter's lane report and the repo's `LOG.md`.
- **shokunin → jin'i-ryu.** At least one logged round in which the shokunin —
  given the round's telemetry — proposed and landed a falsifiable improvement
  to its own `SKILL.md`/`PROVINCE.md`. The delta and its falsification
  condition are recorded in `LOG.md`; the main repo aggregates only the
  promotion decision.

## Round-robin rounds

Each round, the orchestrator dispatches up to one swarm lane per rostered
shokunin (round robin). A shokunin with no dispatched lane participates in the
round only as scope available to other lanes — never as an implicit no-op.

Rounds are driven externally (a scheduler/steer names the round number); the
steer advances the round, the lane owns the work content. Round numbers are
monotonic; a lane must not claim a round other than the steered one.

Every dispatched lane writes a report at
`.ufo/reports/round-<N>/<id>.md` in the main repo, where `<id>` is the roster
id (`protocol` and `aggregator` for the two main-repo lanes). A report under
any other name does not satisfy the contract. Minimum content:

- work performed and evidence pointers (paths, commands, diffs);
- changes landed in the child repo, each tied to a `LOG.md` entry;
- cross-domain evidence encountered, with the domain it belongs to;
- a `SHONEN.md` checklist assessment for that lane's shokunin.

A round is **completed** when every dispatched lane has either reported or
been recorded failed by the integrator — a failed lane counts; a missing
report does not. After a completed round the integrator:

1. Reads every lane report.
2. Lands warranted protocol improvements in this file (a highly valuable
   feature discovered by any domain generalizes to the protocol).
3. Mints a new shonen only if evidence shows an unserved domain — minimum
   evidence: two documented demand instances or an explicit operator
   directive.
4. Appends one entry to `MANIFEST.json`'s `rounds` array and a round entry to
   each participating shokunin's `LOG.md`. Round-entry shape:
   `{round, date, type, lanes: {<id>: <status>}, promotions: [{id, from, to}], minted: [id...], notes}`
   where `<status>` is `ok | failed | not-dispatched`, plus `in-flight` only
   while the round is still open. `type`, `protocol_updates`, and other
   annotation keys are optional. An entry may be written early and corrected
   before the round closes, but no lane may be recorded `not-dispatched`
   while a dispatch or prompt for it exists.

The **aggregator** lane is a main-repo lane that reviews every child repo's
`corpus/` each round (per `CORPUS.md`) and files gaps as lessons. It is the
sole exception to lane write-scope: it may create or repair `corpus/` inside
any child repo — nothing else.

## Evidence standard

Everywhere the protocol says *evidence*, it means a resolvable pointer: a repo
path, a command and its output, a commit, or an external document — never a
naked assertion. A `LOG.md` entry without a pointer is not evidence; a claim
in a lane report that no reader can reach does not exist.

An **end-to-end domain task** is one real work item executed against the
domain's actual surfaces, logged as trigger → action → outcome → pointer.

## File contract per shokunin repo

| File | Purpose |
|---|---|
| `SKILL.md` | The specialist's craft: triggers, decision tables, error patterns, checklists, cited sources |
| `PROVINCE.md` | Domain boundary: what it owns, what it refuses, its work surfaces. Declared surfaces must resolve; when a lane finds a surface moved or absent it corrects `PROVINCE.md` to the real path and logs the correction |
| `LOG.md` | Append-only iteration log: round entries, accepted changes, falsifiable next-iterations |
| `SHONEN.md` | Promotion checklist to shokunin; deleted on promotion |
| `AGENTS.md` | Operating rules when working inside this repo |
| `corpus/` | Proprietary knowledge corpus per `CORPUS.md`: `README.md` index, `knowledge/` sourced domain notes, `lessons/` per-round training lessons; reviewed by the aggregator lane every round |

## Invariants

- Specialize, don't generalize: a shokunin's `SKILL.md` contains *cited,
  verifiable* knowledge of its domain — never generic agent advice.
- One domain per shokunin; a domain belongs to one shokunin. Contested scope —
  evidence or work that plausibly belongs to two provinces — is reported in
  the lane report; the integrator arbitrates by refining `PROVINCE.md`, and
  records the ruling in the round notes.
- Rounds are evidence-driven: every `LOG.md` entry cites the work that
  motivated it.
- `LOG.md` is append-only: entries are never rewritten or deleted; corrections
  land as new entries.
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it.
  Only the integrator writes `MANIFEST.json`, `PROTOCOL.md`, and `ROADMAP.md`;
  lanes write only inside their own child repo and their lane report.
- A meta-domain shokunin (e.g. prompt & skill craft) documents *patterns*; it
  does not own the protocol files, other provinces' files, or promotions.
- Local-first: repos live locally; publishing is operator-owned.
- `corpus/` inherits the evidence standard: every `knowledge/` entry cites a
  resolvable source; `corpus/lessons/` entries cite the round and its LOG.md
  entry or lane report.

