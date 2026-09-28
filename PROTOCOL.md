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

A shonen that records no `LOG.md` activity across two consecutive rounds it
was dispatched and reported in is flagged **dormant** by the integrator in
the round notes; rounds the lane was not dispatched do not count against it.
Dormancy is a review trigger for the operator, never an automatic
retirement.

## Promotion gates

A promotion is a decision backed by artifacts, not a vibe. Every gate names its
verifier and its evidence.

- **shonen → shokunin.** Every `SHONEN.md` box checked by a reviewer who did
  not author the round's changes (a fresh lane or integrator review — never
  self-attestation; a subagent the lane dispatched is still the lane). Each
  checked box names its reviewer — `[x] <verifier>` — and cites its evidence
  pointer. The same marks apply inside `SHONEN.md`: a lane's own assessment
  of its own work is `[~]` asserted (with its evidence pointer), and only an
  `<id>` that did not author the round's changes may write `[x]`. Any
  `[x]` in `SHONEN.md` carrying no named non-author verifier is author
  attestation and counts as `[~]` for the gate.
  Minimum bar (rendered box-for-box by the `SHONEN.md` seed below; the two
  change only in the same edit):
  - `SKILL.md` contains at least one decision table, one error-pattern
    list, and one checklist, each citing a resolvable source (repo path,
    command output, or external document).
  - `LOG.md` records at least one end-to-end domain task:
    trigger → action → outcome → evidence pointer.
  - An agent with no oral context can execute `SKILL.md`/`corpus/`
    instructions: self-contained, pointers resolvable.
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
monotonic; a lane must not claim a round other than the steered one — in
commits, `LOG.md` entries, corpus lessons, and reports alike. A round the
driver skipped produces no entry rather than a mislabeled one; several
entries for one steered round are allowed.

Round prompts are snapshots: where a prompt — or any earlier round's
instructions — conflicts with the current `PROTOCOL.md` or `CORPUS.md`, the
repo files win. A lane re-reads the protocol at the start of every steered
round; a long-lived mission does not grandfather superseded rules.

Round prompts embed the operative contract verbatim — the driver's template
is part of the contract's delivery mechanism, not a convenience summary, and
lossy paraphrase is exactly what the snapshot clause would void. Each lane
prompt carries, as quoted protocol text: the report path and filename, the
commit-before-report ordering, the `SHONEN` heading requirement, the
commit-hash citation rule, and the lane's write scope. Text that exists only
in this file reaches the lanes that re-read it and is skipped by the ones
that don't — rounds 1–8 measured the gap: 33 child-lane reports, 30 missing
a `SHONEN`-led heading (`grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md`
minus the ledger, 2026-09-28) while no driver prompt named it.

Rounds are per-lane counters, not a fleet-global clock: the driver keeps
`.ufo/state/<lane>.round` and lanes can sit on different round numbers at
the same wall-clock moment (a late-joining or respawning lane's `round-3`
is not the same event as another lane's `round-3`). `reports/round-<N>/`
collects whichever lanes ran their Nth round; the integrator closes round
`<N>` per lane, not per fleet.

A lane report **lands last** — written only after the lane's child-repo work
is committed, and it must cite the commit hash. Landed means committed:
changes that exist only in a working tree do not count for the round, and a
report naming a hash the repo does not contain fails verification.

Every dispatched lane writes a report at
`.ufo/reports/round-<N>/<id>.md` in the main repo, where `<id>` is the roster
id (`protocol` and `aggregator` for the two main-repo lanes). A report under
any other name does not satisfy the contract. For the current respawn driver
the report file's existence is also the round-completion signal: a lane that
finishes all other work but files no report keeps its round open
indefinitely (covered by the stale-lane rule below). Minimum content:

- work performed and evidence pointers (paths, commands, diffs);
- changes landed in the child repo, each tied to a `LOG.md` entry;
- cross-domain evidence encountered, with the domain it belongs to;
- a `SHONEN.md` checklist assessment for that lane's shokunin, under a
  `SHONEN` heading with one line per box (`[x]` / `[ ]` / `[~]` + pointer).
  A report without this heading does not satisfy the contract even if the
  same facts appear elsewhere in it; `[~]` means asserted-by-author, not
  skipped. Consequence, not just a label: a report missing the `SHONEN`
  heading is a conformance defect AND is disqualified as evidence in that
  lane's promotion review — the assessment must be re-filed under the
  heading in the next round's report (reports are filed once; the
  assessment, not the report, is re-filed).

A lane whose mission has terminated or been respawned without filing its
round report is recorded `failed` by the integrator; a missing report never
holds a round open. A mission still open more than two driver ticks after
its steer is a stale-lane review trigger — its working context predates
landed protocol changes, and a lane whose work is done but unreported
stalls the same way — and the integrator may record it `failed` so the
driver respawns it on a fresh prompt. A respawned mission inherits its
predecessor's working tree: uncommitted changes it finds are uncommitted
round work under the landed-means-committed rule — the new lane resolves
them (commit-under-its-entry or revert) before it files its own report.

A round is **completed** when every dispatched lane has either reported or
been recorded failed by the integrator — a failed lane counts; a missing
report does not. After a completed round the integrator:


1. Reads every lane report and verifies each cited child-repo commit exists
   and that no participating repo is left with uncommitted round work; checks
   each report for the contract-required `SHONEN` heading; checks the round's
   dispatched `.ufo/prompts/*.md` carried the five contract items verbatim
   per the embed clause above. A report that violates the report contract
   (missing heading, dead hash, report filed before its commit) or a prompt
   missing embedded items is recorded as a conformance defect in the round
   notes — this does not change the lane's status unless the round's rules
   already prescribe `failed`.
2. Lands warranted protocol improvements in this file (a highly valuable
   feature discovered by any domain generalizes to the protocol); routes
   cross-domain defects a lane report filed against a sibling's files to the
   owning lane — the integrator's round notes carry one routing line per
   defect (routing is integrator work and must exist in an artifact), the
   aggregator mirrors each routed defect into the owning repo's
   `corpus/lessons/` (aggregator-owned naming) and keeps an **open
   routed-defects row** in its `AGGREGATE.md` ledger until the owning lane's
   `corpus/lessons/` or `SKILL.md` correction lands; unresolved rows are
   re-flagged in the ledger each audited round. On its first audited round
   after any absence the aggregator sweeps intervening lane reports and
   round notes and reconciles ledger rows before new audits. The ledger row
   — not round notes alone — is the durable queue, since defects outlive
   the round that routed them.
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
`corpus/` each round (per `CORPUS.md`), files gaps as lessons inside the
child repos, and files its own round report at
`.ufo/reports/round-<N>/aggregator.md` covering per-repo corpus verdicts and
cross-lane learnings. It is the sole exception to lane write-scope: it may
create or repair `corpus/` inside any child repo — nothing else: no main-repo
files outside its own report. Alongside the per-round report it maintains one
rolling audit ledger (`AGGREGATE.md` under `.ufo/reports/`); the ledger is
append-only in the same sense as `LOG.md` — refresh sections supersede
earlier rows explicitly rather than rewriting them.

## Evidence standard

Everywhere the protocol says *evidence*, it means a resolvable pointer: a repo
path, a command and its output, a commit, or an external document — never a
naked assertion. A `LOG.md` entry without a pointer is not evidence; a claim
in a lane report that no reader can reach does not exist.

An **end-to-end domain task** is one real work item executed against the
domain's actual surfaces, logged as trigger → action → outcome → pointer.
Where the domain's terminal action is operator-owned (vault approval,
publish click, claim submission), executed means *prepared + verified +
handed off*: the handoff artifact — the staged payload, the probe verdict,
the request reaching its gate — is the outcome pointer, and a documented
negative result at that gate still counts.

A numeric claim carries its counting command, an absence claim its search
sweep, and a quote its location (frontmatter/body, file, line) — the
`CORPUS.md` rules apply to `LOG.md` entries and lane reports too, not only
to `corpus/`. A status command printing configured values is not evidence of
capability: endpoint/ability claims need a probe against the real surface.

Sharpened by the round-4 audit (111 re-executed citations):

- **Claimed ≠ re-executed.** A command offered as evidence is a re-run
  performed at write time with its observed output — never an output quoted
  from memory or a prior session.
- **Corrections sweep every mention.** Before a round's commit, grep every
  file the lane touches (`corpus/README.md`, `SKILL.md`, `knowledge/`) for
  the superseded claim — a corrected fact left standing in a sibling file is
  still a defect.
- **A falsified claim in an append-only file gets a named correction entry
  in the lane's next round** — appended, never rewritten; it stays on the
  routed-defect queue until it lands.
- **Commits are cited by hash, never by subject or tag** — `git rev-parse
  round-4` fails wherever the tag doesn't exist.
- **Drift pins.** A corpus that cites host files by line/content may carry a
  pin mechanism (e.g. `kagi-shokunin/corpus/drift-pins.sh`) — but a pin only
  counts if its expected values are **persisted inside the repo** (a
  recorded sha/mode/lines baseline, or a committed expected-output file the
  script diffs against). A fingerprint *printer* with no stored baseline
  cannot detect drift: round-8 audit found kagi's pins verifiable for only
  2 of 13 files. Recommended where the surface drifts outside lane control.

## File contract per shokunin repo

| File | Purpose |
|---|---|
| `SKILL.md` | The specialist's craft: triggers, decision tables, error patterns, checklists, cited sources. Its frontmatter `description` carries quoted trigger strings, an anti-trigger, and a sibling-arbitration note — capability-and-scope-only descriptions misroute |
| `PROVINCE.md` | Domain boundary: what it owns, what it refuses, its work surfaces. Declared surfaces must resolve; when a lane finds a surface moved or absent it corrects `PROVINCE.md` to the real path and logs the correction |
| `LOG.md` | Append-only iteration log: round entries, accepted changes, falsifiable next-iterations |
| `SHONEN.md` | Promotion checklist to shokunin; generated at mint by copying the canonical template (below) verbatim and deleted on promotion. Gates evolve — when they change, the owning lane regenerates `SHONEN.md` verbatim from the template on its next steered round (the lane is the only allowed writer inside its repo). Verification is mechanical: the seed block (indented lines below) must diff byte-identical modulo `<name>` = the repo's directory name, and marks are confined to the box character plus one indented evidence line per box — `[x] <verifier-id>` or `[~]` with a resolvable pointer; no other prose, added boxes, or removed boxes. Round-8 audit found three repos carrying prose/mark variants outside this form (kagi 4 bare `[x]`, kotoba per-box prose blocks, kengaku a stale 3-box file); the untouched mint seeds (kasegi, kake, kumitate) already conform |
| `AGENTS.md` | Operating rules when working inside this repo |
| `corpus/` | Proprietary knowledge corpus per `CORPUS.md`: `README.md` index, `knowledge/` sourced domain notes, `lessons/` per-round training lessons; reviewed by the aggregator lane every round |

The canonical `SHONEN.md` seed (verbatim — `<name>` is the only substitution):

    # <name> — Promotion checklist

    Promotion to shokunin requires all of:

    - [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources
    - [ ] At least one end-to-end domain task executed and logged in LOG.md
    - [ ] Instructions executable by an agent without oral context
    - [ ] No cross-domain bleed (PROVINCE.md still accurate)

Marks: `[~]` asserted by the lane itself (evidence pointer required),
`[x]` only with a named non-author verifier per **Promotion gates**.

## Invariants

- Specialize, don't generalize: a shokunin's `SKILL.md` contains *cited,
  verifiable* knowledge of its domain — never generic agent advice.
- One domain per shokunin; a domain belongs to one shokunin. Contested scope —
  evidence or work that plausibly belongs to two provinces — is reported in
  the lane report; the integrator arbitrates by refining `PROVINCE.md`, and
  records the ruling in the round notes. A contested-scope report left
  unruled by the next completed round is re-flagged in the lane report, the
  round notes, and an open row in the aggregator ledger; silence is not a
  ruling and must never default scope to whichever lane wrote first.
- Rounds are evidence-driven: every `LOG.md` entry cites the work that
  motivated it.
- `LOG.md` is append-only: entries are never rewritten or deleted; corrections
  land as new entries.
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it.
  Only the integrator writes main-repo files — `MANIFEST.json`,
  `PROTOCOL.md`, `ROADMAP.md`, `CORPUS.md`, `scripts/`, `.ufo/` state and
  prompts. Lanes write only inside their own child repo and their lane
  report at `.ufo/reports/round-<N>/<id>.md`. `.ufo/reports/` and
  `.ufo/waves/` are the round's written evidence and are committed with the
  round's integration commit; `.ufo/state/` and `.ufo/watchdog.log` are
  driver runtime and stay untracked.
- A meta-domain shokunin (e.g. prompt & skill craft) documents *patterns*; it
  does not own the protocol files, other provinces' files, or promotions.
- Local-first: repos live locally; **domain-facing actions are
  operator-owned** (publishing, vault approval, claim submission). Repo
  bookkeeping — committing and `git push`ing the round's commits — is
  ordinary lane work, not publishing, when the driver instructs it.
  Exception: operator-gated artifacts (staged payloads, publish candidates,
  vault request material, evidence under embargo) are committed locally but
  not pushed until the operator releases the gate — bookkeeping never
  front-runs an operator decision. A lane's main-repo commit is
  pathspec-limited to its own report file
  (`git commit -- .ufo/reports/round-<N>/<id>.md`) — never `commit -a` /
  `add -A`, which sweeps up sibling in-flight edits and integrator
  working-tree changes.
- `corpus/` inherits the evidence standard: every `knowledge/` entry cites a
  resolvable source; `corpus/lessons/` entries cite the round and its LOG.md
  entry or lane report.
  Corpus corrections are new entries, never in-place rewrites — in both
  directions: no lane edits another lane's or the aggregator's corpus
  files; `round-<N>-aggregator-*.md` are aggregator-owned.


## Fleet-2 conventions (adopted)

- Expertise axes live in `AXES.md`; each lane owns a named subset and works one
  axis-move per round, measured in `SCORECARD.md` (per child repo).
- `MISSION.md` is the mission SSOT: fleet shape, model map, concurrency floor,
  push rule, L0 side channel. Watchdog prompts bind to it.
- L0 side channel: lanes append `.ufo/l0-questions.md`; aggregator surfaces.
