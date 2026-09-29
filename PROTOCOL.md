# Shokunin Protocol

> 職人 — an artisan specialist that earns its domain through demonstrated craft.

A **shokunin** is a domain specialist, distinct from generic agents: it owns a domain, accumulates
hard-won knowledge, and is iterated by rounds of swarm work until it can iterate itself.

## Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan of a domain) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted when a domain demand is proven: two documented *unplaceable* demand instances
  (work no existing province could absorb) or an explicit operator directive — the mint bar, stated
  once here; closure step 3 applies it. It starts with a scoped `SKILL.md` + `PROVINCE.md`, an empty
  `LOG.md`, and a domain record in `MANIFEST.json`.
- **Shokunin** — promoted when it demonstrably performs domain work end-to-end, per the gate below:
  its `LOG.md` shows completed rounds and a reviewer can execute the written instructions without
  oral hand-holding.
- **Jin'i-ryu** — promoted per the gate below when it can iterate on itself, with the main repo
  aggregating only promotion/mint decisions.

A shonen that records no `LOG.md` activity across two consecutive rounds it was dispatched and
reported in is flagged **dormant** by the integrator in the round notes; rounds the lane was not
dispatched do not count against it. Dormancy is a review trigger for the operator, never an
automatic retirement.

## Promotion gates

A promotion is a decision backed by artifacts, not a vibe. Every gate names its verifier and its
evidence.

- **shonen → shokunin.** Every `SHONEN.md` box checked by a reviewer who did not author the round's
  changes — a fresh lane or integrator review, never self-attestation;
  a subagent the lane dispatched is still the lane. Each checked box names its reviewer (`[x] <verifier>`)
  and cites its evidence pointer. The same marks apply inside `SHONEN.md`: the lane's own assessment is `[~]`
  asserted (with its evidence pointer); only a non-author `<id>` may write `[x]`. Any `[x]` carrying no named
  non-author verifier is author attestation and counts as `[~]` for the gate. Minimum bar (rendered box-for-box
  by the `SHONEN.md` seed below; the two change only in the same edit):
  - `SKILL.md` contains at least one decision table, one error-pattern list, and one checklist, each
    citing a resolvable source (repo path, command output, or external document) — real craft, not
    generic advice.
  - `LOG.md` records at least one end-to-end domain task: trigger → action → outcome → evidence
    pointer.
  - An agent with no oral context can execute `SKILL.md`/`corpus/` instructions: self-contained,
    pointers resolvable.
  - `PROVINCE.md` still matches reality: no absorbed cross-domain work.
  On promotion `SHONEN.md` is deleted, `MANIFEST.json` rank is updated, and the review is recorded
  in the promoter's lane report and the repo's `LOG.md`.
- **shokunin → jin'i-ryu.** At least one logged round in which the shokunin — given the round's
  telemetry — proposed and landed a falsifiable improvement to its own `SKILL.md`/`PROVINCE.md`. The delta and its
  falsification condition are recorded in `LOG.md`.

## Round-robin rounds

Each round, the orchestrator dispatches up to one swarm lane per rostered shokunin (round robin). A
shokunin with no dispatched lane participates in the round only as scope available to other lanes —
never as an implicit no-op.

Rounds are driven externally (a scheduler/steer names the round number); the steer advances the
round, the lane owns the work content. Round numbers are monotonic; a lane must not claim a round
other than the steered one — in commits, `LOG.md` entries, corpus lessons, and reports alike. A
round the driver skipped produces no entry rather than a mislabeled one; several entries for one
steered round are allowed.

Round prompts are snapshots: where a prompt — or any earlier round's instructions — conflicts with
the current `PROTOCOL.md` or `CORPUS.md`, the repo files win. A lane re-reads the protocol at the
start of every steered round; a long-lived mission does not grandfather superseded rules.

Round prompts embed the operative contract verbatim — the driver's template is part of the
contract's delivery mechanism, not a convenience summary, and lossy paraphrase is what the snapshot
clause would void. Each *child-lane* prompt carries, as quoted protocol text: the report path and
filename, the commit-before-report ordering, the `SHONEN` heading requirement, the commit-hash
citation rule, and the lane's write scope. The aggregator prompt instead embeds *its* operative set
verbatim: report path, the ledger path and refresh duty, child-repo commit ownership (its own files,
pathspec-limited), the corpus-only write scope, and the L2 minimum — a number this file does not own:
`MISSION.md` §L2 concurrency is its source. The protocol prompt embeds its own duties: this
file's re-read requirement, the integrator-of-record closure steps, and the L2 minimum. Text only in this file
reaches the lanes that re-read it and is skipped by the ones that don't (§Appendix, "Prompt embeds contract"): a
prompt-fidelity defect named in round notes does not fix the template — the integrator's report must also carry the
exact corrected `lane_prompt()` text required, since `scripts/` is operator-side.

Rounds are per-lane counters, not a fleet-global clock: the driver keeps `.ufo/state/<lane>.round`
and lanes can sit on different round numbers at the same wall-clock moment (a late-joining or
respawning lane's `round-3` is not the same event as another lane's). `reports/round-<N>/` collects
whichever lanes ran their Nth round; the integrator closes round `<N>` per lane, not per fleet.

A lane report **lands last** — written only after the lane's child-repo work is committed, and it
must cite that commit's hash. Landed means committed: changes that exist only in a working tree do
not count for the round. The cited hash is the lane repo's `HEAD` when the report is written — a
report naming a hash the repo does not contain fails verification, and a cited hash that is not an
ancestor of `HEAD` at closure is a conformance defect (`git merge-base --is-ancestor <hash> HEAD` is
the check). Corrections land as new commits, never by amending a cited one — amending or rewriting
orphans the record — and append-only files (`LOG.md`) take an appended correction entry pointing at
the superseded text, never an in-place rewrite. Landed also means landed *by the lane*: the commit
that adds `.ufo/reports/round-<N>/<id>.md` carries the lane identity, because the driver completes
the mission the instant the file reaches disk and any later fleet-level commit can sweep it
(§Appendix, "Lands last"). A swept report is still landed — history is never rewritten to fix
attribution — but the integrator records the attribution defect in the round notes, and a lane whose
report is still uncommitted when its mission completes has not satisfied this clause. An orphaned
report is resolved in order: the lane's own respawn inherits and lands it; the integrator sweeps it
for durability only if that successor mission also terminates without landing it, and records the
attribution defect — a sweep is the last resort because it freezes the on-disk bytes, unfilled
placeholders and all, into a permanent object (§Appendix, "Orphaned report"). A filed report is a
record: a correction lands in the correcting round's own report or as an appended erratum naming
the superseded text, never as a silent in-place rewrite.

Every dispatched lane writes a report at `.ufo/reports/round-<N>/<id>.md` in the main repo, where
`<id>` is the roster id (`protocol` and `aggregator` for the two main-repo lanes). A report under
any other name does not satisfy the contract. For the current respawn driver the report file's
existence is also the round-completion signal: a lane that finishes all other work but files no
report keeps the *driver's* mission open until the stale-lane rule below fires, while a missing
report never holds a round open in the *integrator's ledger* — there the lane-round is recorded
`failed` at closure. Minimum content:

- work performed and evidence pointers (paths, commands, diffs);
- changes landed in the child repo, each tied to a `LOG.md` entry;
- cross-domain evidence encountered, with the domain it belongs to;
- a `SHONEN.md` checklist assessment for that lane's shokunin, under a `SHONEN` heading with one
  line per box (`[x]` / `[ ]` / `[~]` + pointer). A report without this heading does not satisfy the
  contract even if the same facts appear elsewhere in it; `[~]` means asserted-by-author, not
  skipped. Consequence: a report missing the `SHONEN` heading is a conformance defect AND disqualified as evidence
  in that lane's promotion review — the assessment (reports are filed once; the assessment is not) must be re-filed
  under the heading in the next round's report.

A lane whose mission has terminated or been respawned without filing its round report is recorded
`failed` by the integrator. `failed` covers every lane-round that was prompted or dispatched and has
no report by closure, including a prompt left behind by a failed launch (dispatch evidence and
orphan prompts: step 4). A mission still open more than two driver ticks after its steer is a
stale-lane review trigger — its working context predates landed protocol changes, and a lane whose
work is done but unreported stalls the same way — and the integrator may record it `failed` so the
driver respawns it on a fresh prompt. The trigger needs an actuator: every dispatched lane's report
must list any mission open longer than two driver ticks — age computed from the launch timestamp,
not the tick counter, which resets when the driver restarts — and must say whether it is
*progressing* or *silent*. Progressing means observable activity in the lane's write scope since its launch —
a commit authored by the lane, or files modified under its repo
(`find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*'`); silent means neither. A commit
authored by *another* lane is not the subject lane's activity — the aggregator writes into every
child repo — so where the only newer files are a sibling's, the row says so and grades the lane on
its own signals. Commit sparsity is
normal in this
fleet (§Appendix, "Stale-lane actuator"), so the absence of a commit is not silence and must not
trigger `failed`. The integrator-of-record records `failed` only for silent missions and flags
progressing ones in the round notes — and recording `failed` is a ledger act, not a kill: the
driver's respawn path is unreachable while its daemon is up (step 4), so nothing in this section
terminates live work.

A respawned mission inherits its predecessor's working tree: uncommitted *lane-authored* changes it
finds are uncommitted round work under the landed-means-committed rule — the new lane resolves them
(commit-under-its-entry or revert) before it files its own report. Uncommitted **aggregator-owned**
files (`corpus/lessons/round-*-aggregator-*`) are not the lane's to commit: the lane records them in
its report and leaves them for the aggregator to resolve.

A file at the report path is not automatically a report. The driver's completion signal is that
path's existence (`report_of()` in `scripts/shokunin-watchdog.sh`), so a contentless **completion
marker** can close a lane-round with no work behind it (§Appendix, "Marker vs report"). A filed
report that records no lane work — no changes, no evidence pointer, no resolvable commit — is a
marker, not a report: the integrator records that lane-round `failed`, keeps the marker file as a
conformance defect, and names the counter advancement in the round notes. A short report that names
a real committed round-work hash is a *defective* report, not a marker: status `ok`, minimum-content
defect recorded. A marker that names nothing checkable is `failed` whatever the lane actually did —
real work sitting unattributed in child repos does not rescue it. This does not relax step 1:
contract violations inside a real report stay status-neutral defects.

**Integrator of record.** The integrator this protocol assigns work to is the round's `protocol`
lane — a role, not a separate rostered lane; where a generated driver prompt conflicts (e.g. "never
MANIFEST.json"), this file wins per the snapshot clause. Its main-repo writes are
`PROTOCOL.md`/`ROADMAP.md`/`SCORECARD.md`/`LOG.md`/its own report, and expand by exactly five:
appending `MANIFEST.json` `rounds` entries, the conformance/routing record inside its own report
(the round notes), committing already-generated `.ufo/prompts/*.md` so dispatch evidence is
durable, committing `.ufo/l0-questions.md` so the operator queue is durable, and committing the
round's closure-gate artifacts under `.ufo/waves/round-<N>/` — it never edits a prompt or the
script, and `scripts/` plus `.ufo/state/` remain operator-side (§Invariants); required template
corrections are named in its report. The integrator's
closure artifact is its own round report: a protocol-lane report carrying no closure record — the
statuses it wrote, or a statement of why none was writable — is an incomplete report whatever else
it contains. That is the only guaranteed delivery channel: generated protocol prompts name none of steps 1–4
(§Appendix, "No closure channel"), so the duty reaches the lane solely through this file's re-read.
The closure record is a gate, not prose: steps 1 and 4 run through a committed checker whose frozen
re-run reproduces every status the entry carries (§Gate standard, "Two evidences"), so a closure
record no reader can re-execute is an opinion.

A round is **completed** when every dispatched lane has either reported or been recorded failed by
the integrator — a failed lane counts; a missing report does not. Under the respawn driver lanes
hold different counters at the same instant, so fleet-wide completion is never observable, and
waiting for it is what left rounds 2–11 without a closure entry (§Appendix, "Closure entries").
Closure is therefore per lane-round: each protocol round the integrator closes every lane-round that
terminated since its last pass plus any older one still carrying an unresolved row (step 4). After
closing, the integrator:

1. Reads every lane report and verifies each cited child-repo commit exists *and is an ancestor of
   the lane repo's `HEAD`*; verifies no participating repo is left with uncommitted round work
   (uncommitted aggregator-owned files are reported, not lane debt); checks each report for the
   contract-required `SHONEN` heading; checks the round's dispatched `.ufo/prompts/*.md` carried the
   five contract items verbatim per the embed clause above **and that any L2 route map quoted in the
   prompt matches the current `MISSION.md` bucket**. A report that violates the report contract
   (missing heading, dead or orphaned hash, report filed before its commit) or a prompt missing
   embedded items is recorded as a conformance defect in the round notes — this does not change the
   lane's status unless the round's rules already prescribe `failed`.
2. Lands warranted protocol improvements in this file (a highly valuable feature discovered by any
   domain generalizes to the protocol); routes cross-domain defects a lane report filed against a
   sibling's files to the owning lane — and the integrator's report carries one routing line per
   defect **including defects a lane owes its own repo** (self-defects ride the same durable queue;
   routing is integrator work and must exist in an artifact). The aggregator mirrors each routed
   defect into the owning repo's `corpus/lessons/` (aggregator-owned naming) and keeps an **open
   routed-defects row** in its ledger (canonical path and fallback queue: the aggregator-lane
   paragraph below) until the owning lane's `corpus/lessons/` or `SKILL.md` correction lands;
   unresolved rows are re-flagged each audited round, and on its first audited round after any
   absence the aggregator sweeps intervening lane reports and round notes and reconciles ledger rows
   before new audits. The ledger row — not round notes alone — is the durable queue, since defects
   outlive the round that routed them.
3. Mints a new shonen only if evidence shows an unserved domain — minimum evidence per **Lifecycle**
   (the mint bar stated once there). `ROADMAP.md` restates the bar; where a restatement drifts, this
   file wins and the drift is a round-notes defect.
4. Appends one entry to `MANIFEST.json`'s `rounds` array (integrator-of-record scope; each lane's
   own `LOG.md` entry remains lane work, not integrator work — lanes write inside their own repos).
   Round-entry shape:
   `{round, date, type, lanes: {<id>: <status>}, promotions: [{id, from, to}], minted: [id...], notes}`
   where `<status>` is `ok | failed | not-dispatched | in-flight`. `type`, `closed_at`,
   `protocol_updates`, and other annotation keys are optional. Semantics under a per-lane-counter
   driver:
   - **Partial entries are the norm.** Write the entry for round `N` as soon as one lane's Nth
     lane-round terminates: a terminal status for every `N` lane-round that has terminated,
     `in-flight` for lanes dispatched and still open, `not-dispatched` for lanes with no dispatch
     evidence **as of `closed_at`** — so `closed_at` is required on any entry carrying a
     `not-dispatched` row. Waiting for all eight counters to reach `N` waits forever; that is what
     left rounds 2–11 unclosed.
   - **Dispatch evidence** is the `.ufo/watchdog.log` dispatch line — `launch <lane> round=N`
     (respawn driver, written only after a successful launch) or `steer <lane> -> round N`
     (steer-era driver; the earliest rounds had no prompt files at all, so a prompt-only test
     misreads real lane-rounds as undispatched — §Appendix, "Dispatch evidence"). The committed
     `.ufo/prompts/<lane>-round-N.md` corroborates mission *content* and must be committed to be
     durable, but `lane_prompt()` writes it before the launch is attempted — a prompt with no
     dispatch line is an attempted dispatch and records `failed`. **Completion evidence** is a
     `.ufo/reports/round-N/<lane>.md` that satisfies the report contract; a completion marker is not
     a report (see above) and makes the lane-round `failed`. **Termination evidence** is a `complete
     <lane> round=N` line or the lane's counter passing `N`. Liveness probes are not evidence of an
     open mission: `ufo-sighting status --lite` still lists a mission after the driver `complete`d
     it (§Appendix, "Liveness probes"), so the driver's `live` test can never fail while its daemon
     is up and its `lane-dead-no-report` retry path is unreachable. `in-flight` is therefore decided
     from the absence of both a `complete <lane> round=N` line and a *landed* report — an
     uncommitted file at the report path does not end `in-flight`, however it fires the driver's
     existence signal (§Appendix, "Unlanded report") — and never from a status
     probe. `.ufo/watchdog.log` is mutable and the driver appends to it concurrently, so its line
     numbers drift: the round notes carry a committed digest (timestamp + text) of every
     dispatch/complete line a status rests on, and that digest — not the live log — is the pointer
     that resolves at closure.
   - **`in-flight` is debt, not a resting status.** Every `in-flight` row is answered by the next protocol
     round — resolved to a terminal status or re-confirmed with evidence — which appends `{"round": N,
     "type": "closure-correction", "closed_at": …, "lanes": {<id>: <status>}}` — never an in-place
     edit. A lane dispatched for its Nth
     round *after* round `N` closed rides the next closure-correction for `N` — never dropped, never
     folded into `N+1`. An `in-flight` row whose mission is still live at the next pass is
     re-confirmed by a closure-correction carrying `in-flight` plus the launch pointer, and stays
     debt until the mission terminates.
   - No lane may be recorded `not-dispatched` while dispatch evidence for that lane-round exists,
     and no lane may be recorded `in-flight` unless its mission was live at `closed_at`. A row
     contradicting evidence is a conformance defect of the entry (§Appendix, "Closure entries").
   - **A row names the lane-round it describes.** `lanes` values stay status strings; the optional
     `lane_rounds: {<id>: <n>}` map records a lane's own counter where it differs from the entry's
     `round` and is required on every `not-dispatched` row — the counter the lane actually held is
     what makes such a row falsifiable. The row describes lane-round `(<id>, round)`: `lane_rounds`
     annotates it and never re-keys it, so last-wins is computed over `(id, entry.round)`; reading
     the map as the key erases in-flight debt and manufactures rows out of the pre-fleet-2
     fleet-keyed entries, which carry no `lane_rounds` and are `unadjudicable` as lane-rounds
     (§Appendix, "Row identity"). An `ok` row needs no pointer:
     `.ufo/reports/round-<n>/<id>.md` is derivable, and its absence falsifies the row. `failed`,
     `in-flight`, and `not-dispatched` rows carry their pointer in `notes`.
   - **Retroactive closure is typed, and is not a pass.** Entries for lane-rounds that terminated
     before the integrator role existed carry `type: "retroactive-closure"` and notes stating that
     the statuses are presence-of-evidence only, that step-1 verification (hash ancestry, `SHONEN`
     heading, prompt fidelity) did not run at the time, and — for rounds before fleet-2 (`609ecb6`)
     — that no axis-move duty existed. Promotion and axis reviews must never read a retroactive row
     as a contemporaneous pass.
   - **`rounds` is append-only after closure.** Corrections are appended entries carrying `type:
     "closure-correction"` and `supersedes: {round, type, date}` naming the row they replace — never
     in-place edits, never prepends, because index citations into the array must keep resolving
     (§Appendix, "Append-only `rounds`"). Consumers read the array in order; `rounds[].round` is not
     unique and the last row for a lane wins.

The **aggregator** lane is a main-repo lane that reviews every child repo's `corpus/` each round
(per `CORPUS.md`), files gaps as lessons inside the child repos, and files its own round report at
`.ufo/reports/round-<N>/aggregator.md` covering per-repo corpus verdicts and cross-lane learnings.
It is the sole exception to lane write-scope: it may create or repair `corpus/` inside any child
repo — nothing else: no main-repo files outside its own report and ledger. Every file it creates
inside a child repo is **committed by the aggregator itself at creation time**, pathspec-limited to
its own files, under its own subject (`corpus: round-<N> aggregator …`) — never left uncommitted for
a lane's round commit to sweep, and a lane never commits an aggregator-owned file. Alongside the
per-round report it maintains one rolling audit ledger — canonically `.ufo/reports/AGGREGATE.md`,
and no third path counts; a superseded snapshot elsewhere (e.g. `round-2/AGGREGATE.md`) is relocated
there by its next refresh and remains readable evidence — superseded, not voided. While the
canonical ledger is absent or unrefreshed, the integrator's round notes are the queue of record
(§Appendix, "Ledger"). The ledger is append-only in the same sense as `LOG.md` — refresh sections
supersede earlier rows explicitly rather than rewriting them. An aggregator round report is
incomplete unless the ledger was refreshed or the report names why no row changed — and a round
filed without the ledger duty keeps the routed-defect queue empty by construction.

## Evidence standard

Everywhere the protocol says *evidence*, it means a resolvable pointer: a repo path, a command and
its output, a commit, or an external document — never a naked assertion. A `LOG.md` entry without a
pointer is not evidence; a claim in a lane report that no reader can reach does not exist.

An **end-to-end domain task** is one real work item executed against the domain's actual surfaces,
logged as trigger → action → outcome → pointer. Where the domain's terminal action is operator-owned
(§Invariants, local-first), executed means *prepared + verified + handed off*: the handoff artifact
— the staged payload, the probe verdict, the request reaching its gate — is the outcome pointer, and
a documented negative result at that gate still counts.

A numeric claim carries its counting command, an absence claim its search sweep, and a quote its
location (frontmatter/body, file, line) — the `CORPUS.md` rules apply to `LOG.md` entries and lane
reports too, not only to `corpus/`. A status command printing configured values is not evidence of capability:
endpoint/ability claims need a probe against the real surface.

An evidence pointer must resolve at *closure* time, not only at write time: paths under `tmpfs`
(`/tmp`, `/dev/shm`), session-scoped `local://` artifacts, and any pointer a fresh session cannot
reach are not evidence — commit the artifact or cite a reproducible command. A timestamp on evidence
must be at or before the commit that ships it — future-dated evidence is a conformance defect
(§Appendix, "Evidence standard").

Sharpened by the round-4 audit (§Appendix, "Evidence standard"):

- **Claimed ≠ re-executed.** A command offered as evidence is a re-run performed at write time with
  its observed output — never an output quoted from memory or a prior session.
- **Corrections sweep every mention.** Before a round's commit, grep every file the lane touches
  (`corpus/README.md`, `SKILL.md`, `knowledge/`) for the superseded claim — a corrected fact left
  standing in a sibling file is still a defect.
- **A falsified claim in an append-only file gets a named correction entry in the lane's next
  round** — appended, never rewritten; it stays on the routed-defect queue until it lands.
- **Commits are cited by hash, never by subject or tag** — `git rev-parse round-4` fails wherever
  the tag doesn't exist.
- **Drift pins.** A corpus that cites host files by line/content may carry a pin mechanism — but
  a pin only counts if its expected values are **persisted inside the repo** (a recorded
  sha/mode/lines baseline, or a committed expected-output file the script diffs against). A
  fingerprint *printer* with no stored baseline cannot detect drift. Recommended where the surface
  drifts outside lane control.

## Gate standard

A **gate** is a committed, re-runnable verdict script a lane owns: it reads surfaces, compares them
against expected values persisted in its own repo, and returns a verdict. A tool that cannot fail is
a **probe**, and is registered as one.

- **Verdict.** `0` = `clean` and `1` = `failed` fleet-wide; every other code a gate exits (`2`, `3`,
  `64`, …) is declared in its registry entry and mapped onto `clean | failed | could-not-evaluate`,
  and an undeclared nonzero code reads as `could-not-evaluate`. Nothing else is pinned: a gate's own
  vocabulary — WARN vs HIT, a missing baseline, finding kinds — stays lane-owned, and this section
  governs the outer interface only, so no working gate breaks on adoption.
- **Self-test.** Every gate exposes a self-invocation mode over isolated fixtures (temp trees, no
  network, no live-tree write) asserting both the exit code and a stable expected finding-id, with
  the expected values committed in the owning repo and independent of the recomputation. The flag
  spelling is the lane's (`--selftest`, `--self-test`, `run_selftest()`) and the registry records it;
  a helper-only or model-only self-check does not satisfy this clause.
- **Two evidences.** Self-test green is capability, not a measurement (§Evidence standard). A gate
  whose verdict depends on a mutable fleet artifact also ships a run over a committed input snapshot
  with its committed expected verdict, so a later hand-edit of that artifact contradicts the frozen
  run. A verdict names the revision it was measured against: a gate grades the tree it runs on, so a
  run over a moving worktree is not comparable to one over the cited commit.
- **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name,
  `gate|probe`, entry command, verdict map (code → class), self-test command and spelling,
  pinned-value path, write scope, owner. The aggregator ledger stays the routed-defect queue, not a
  second inventory; a fleet index is pointers to lane rows, never copied expected values.
- **Scope.** Read-only over surfaces it does not own, and it never acts on an external surface —
  publishing, vault approval, claim submission and driver mutation stay operator-owned (§Invariants,
  local-first). A verdict is lane-local evidence: it never defines the host runtime's stop conditions
  (`loop_stop`/`mission_goal`) and never stands in for the native judge.
- **Closure consequence.** A red gate is a conformance defect recorded in the round notes and routed
  to its owner — status-neutral unless the round's rules already prescribe `failed` (closure step 1).
  The integrator verifies a gate's *committed evidence* (self-test tally, frozen-run verdict, the
  measured revision); it does not execute a sibling's gate, whose dependencies and write scope are
  the lane's.

## File contract per shokunin repo

| File | Purpose |
|---|---|
| `SKILL.md` | The specialist's craft: triggers, decision tables, error patterns, checklists, cited sources. Its frontmatter `description` carries quoted trigger strings, an anti-trigger, and a sibling-arbitration note — capability-and-scope-only descriptions misroute |
| `PROVINCE.md` | Domain boundary: what it owns, what it refuses, its work surfaces. Declared surfaces must resolve; when a lane finds a surface moved or absent it corrects `PROVINCE.md` to the real path and logs the correction |
| `LOG.md` | Append-only iteration log: round entries, accepted changes, falsifiable next-iterations |
| `SHONEN.md` | Promotion checklist to shokunin; generated at mint by copying the canonical template (below) verbatim and deleted on promotion. Gates evolve — when they change, the owning lane regenerates `SHONEN.md` verbatim from the template on its next steered round (the lane is the only allowed writer inside its repo). Verification is mechanical: the seed block (indented lines below) must diff byte-identical modulo `<name>` = the repo's directory name, and marks are confined to the box character plus one indented evidence line per box — `[x] <verifier-id>` or `[~]` with a resolvable pointer; no other prose, added boxes, or removed boxes (§Appendix, "Canonical form") |
| `AGENTS.md` | Operating rules when working inside this repo |
| `corpus/` | Proprietary knowledge corpus per `CORPUS.md`: `README.md` index, `knowledge/` sourced domain notes, `lessons/` per-round training lessons; reviewed by the aggregator lane every round |
| `SCORECARD.md` | Axis scores per `AXES.md`: owned axes → score 0–10 → evidence pointer → last-change round, plus `planned` and `retired`. Every score is a claim: it carries the counting command that produced it and the commit it was measured against, so a reader can re-derive it |

The canonical `SHONEN.md` seed (verbatim — `<name>` is the only substitution):

    # <name> — Promotion checklist

    Promotion to shokunin requires all of:

    - [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources
    - [ ] At least one end-to-end domain task executed and logged in LOG.md
    - [ ] Instructions executable by an agent without oral context
    - [ ] No cross-domain bleed (PROVINCE.md still accurate)

Marks: `[~]` asserted by the lane itself (evidence pointer required), `[x]` only with a named
non-author verifier per **Promotion gates**.

## Invariants

- Specialize, don't generalize: a shokunin's `SKILL.md` contains *cited, verifiable* knowledge of
  its domain — never generic agent advice.
- One domain per shokunin; a domain belongs to one shokunin. Contested scope — evidence or work that
  plausibly belongs to two provinces — is reported in the lane report; the integrator arbitrates by
  refining `PROVINCE.md` and records the ruling in the round notes. A contested-scope report left
  unruled by the next completed round is re-flagged in the lane report, the round notes, and an open
  row in the aggregator ledger; silence is not a ruling and must never default scope to whichever
  lane wrote first.
- Rounds are evidence-driven: every `LOG.md` entry cites the work that motivated it.
- `LOG.md` is append-only: entries are never rewritten or deleted; corrections land as new entries.
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it. Only integrator roles
  write main-repo files — `MANIFEST.json`, `PROTOCOL.md`, `ROADMAP.md`, `CORPUS.md`, `MISSION.md`,
  `AXES.md`, `scripts/`, `.ufo/` state and prompts. `MISSION.md`, `AXES.md`, and `scripts/` are
  operator-side integrator files: the protocol lane names the corrections they need in its round
  notes and does not edit them. The protocol lane holds the protocol/roadmap/report writes and, as
  integrator-of-record, `MANIFEST.json` `rounds` appends; `MANIFEST.json` edits *outside* `rounds`
  (roster, rank, minting) remain operator-side integrator work. Lanes write only inside their own
  child repo and their lane report at `.ufo/reports/round-<N>/<id>.md`; the two main-repo lanes
  (`protocol`, `aggregator`) additionally keep `SCORECARD.md` and `LOG.md` at the main-repo root,
  because their axes are fleet-level and the `AXES.md` per-repo contract applies to them there.
  `.ufo/reports/` and `.ufo/waves/` are the round's written evidence, committed with the round's
  integration commit, as are that round's generated `.ufo/prompts/*.md` — an untracked prompt is
  non-durable dispatch evidence. `.ufo/state/` and `.ufo/watchdog.log` are driver runtime that
  churns every tick: they have been tracked since `609ecb6` although this clause once said they stay
  untracked (§Appendix, "Tracked runtime"), so no lane commit may include them —
  pathspec-limited commits are the enforcement; untracking them is operator-side work named in the round notes.
- A meta-domain shokunin (e.g. prompt & skill craft) documents *patterns*; it does not own the protocol files,
  other provinces' files, or promotions.
- Local-first: repos live locally; **domain-facing actions are operator-owned** (publishing, vault
  approval, claim submission). Push scope is owned by `MISSION.md` §Push scope — hard rule (operator
  rule, landed in `235b414` 2026-09-28): lanes push only to the main repo and their own `<lane>-shokunin`
  remote; domain source trees are read-only and upstream-bound work is carried in the round report.
  Repo bookkeeping — committing and `git push`ing the round's commits — is ordinary lane work, not
  publishing, when the driver instructs it. Exception: operator-gated artifacts (staged payloads,
  publish candidates, vault request material, evidence under embargo) are committed locally but not
  pushed until the operator releases the gate — bookkeeping never front-runs an operator decision. A
  lane's main-repo commit is pathspec-limited to its own report file (`git commit --
  .ufo/reports/round-<N>/<id>.md`) — never `commit -a` / `add -A`, which sweeps up sibling in-flight
  edits and integrator working-tree changes.
- Lane authorship is auditable: each child repo is configured at mint so round commits carry the
  lane identity (`<lane>-shokunin` / `<lane>@shokunin.local`). A lane finding its repo unconfigured
  sets `git config user.name/email` once and notes it in `LOG.md`; commits under the operator
  identity made by lane rounds are a conformance defect (§Appendix, "Lane identity"). Main-repo
  commits follow the same rule and cannot rely on `git config`, because the shared main-repo
  identity is the operator's personal one: a main-repo lane commits with
  `git -c user.name=<lane>-shokunin -c user.email=<lane>@shokunin.local commit …`.
- `corpus/` inherits the evidence standard: every `knowledge/` entry cites a resolvable source;
  `corpus/lessons/` entries cite the round and its LOG.md entry or lane report. Corpus corrections
  are new entries, never in-place rewrites — in both directions: no lane edits another lane's or the
  aggregator's corpus files; `round-<N>-aggregator-*.md` are aggregator-owned.

## Fleet-2 conventions (adopted)

- Expertise axes live in `AXES.md`; each lane owns a named subset and works one axis-move per round,
  measured in `SCORECARD.md`. An axis-move inherits the evidence standard: before and after numbers
  each carry the counting command and the commit they were measured against, and a score no reader
  can re-derive is an opinion, not a measurement. Axis work does not displace the file contract — a
  round that moves an axis while `corpus/`, `LOG.md`, or `SHONEN.md` drift are a conformance defect
  like any other.
- `MISSION.md` is the mission SSOT: fleet shape, model map, concurrency floor (the L2 minimum's
  source), push rule, L0 side channel. Watchdog prompts bind to it. Precedence between the two
  SSOTs: `PROTOCOL.md` owns process, evidence, and gates; where they conflict on process —
  `MISSION.md`'s unconditional "commit then push" against this file's operator-gated hold, for
  instance — `PROTOCOL.md` wins and the conflict is named in the round notes; neither file is edited
  by a lane.
- L0 side channel: lanes append `.ufo/l0-questions.md`; the aggregator surfaces it. The file is
  append-only in the same sense as `LOG.md` — a lane restating or correcting its own question
  appends a new line naming the superseded one and never rewrites a filed line, and the operator's
  in-place answers are never a lane write. Cite a question by lane + round + its opening words,
  never by line number: the queue grows, so every line number moves. Its durability owner is the
  integrator, which commits it with the round's integration commit — a lane's appended question is
  non-durable until committed and no lane owns the path (§Appendix, "L0 durability").

## Appendix — incident digest (why these rules exist)

One line per dated incident or measurement motivating a rule above; figures verbatim from the round record, pinned
to their measurement round, never live values. `rN` = `.ufo/reports/round-N/protocol.md`; rounds 1–8 incidents
aggregate in r10 §Closure/§Conformance (the integrator role did not exist before round 9).

| Rule | Round | Incident / measurement | Pointer |
|---|---|---|---|
| Lands last | 9 | kengaku `85b22e3`→`f147a27` orphaned its own report; `LOG.md:9` round-5 entry rewritten in place; aggregator mirrors uncommitted in kake/kumitate/kagi, kasegi swept one into `c80c2a1` (unlogged misattribution) | r10 D-12/D-13, §Conformance 7 |
| Lands last | 10 | 46 of 60 reports swept into `6565e89`/`609ecb6`/`0a30b44` (21/21/4); `609ecb6` 17:38:25 added round-10/kasegi.md, lane-round completed 17:32:47. Lane identity: r10 recorded "0 of 62 reports committed under a lane identity" (33 operator, 26 `shokunin <shokunin@local>`, a third identity) — falsified on round-11 re-execution already at write time (kumitate `9a2e9fb` 18:37:14 predates the r10 report); corrected census in the round-11 report | r10 §Conformance 4 |
| Stale-lane actuator | 10 | tick counter resets on driver restart (`tick=13` 17:32:48 → `tick=1` 17:50:21) — age from launch timestamps; commit sparsity normal (kumitate 39 min, kake 34 min, protocol 47 min to first commit) | r10 §Stale-lane |
| Stale-lane actuator | 10 | first-draft wording would have marked live lanes `failed` for commit sparsity; corrected in `43342dd` | r10 D-49 |
| Failed covers orphan prompts | 10 | 0 `launch-fail` orphan prompts observed; structural (`lane_prompt()` precedes launch) | r10 step-4 text |
| Marker vs report | 10 | round-8/kengaku.md (101 B, "work pushed") advanced kengaku 8→9 while HEAD stayed `f147a27` "round-7" — no round-8 commit or LOG entry; kotoba `8c300ad` + kumitate `7a4c9a0` named real work → `ok` + minimum-content defect, not markers | r10 §Conformance 1 |
| Marker vs report | 5 | aggregator r5 marker cites no commit → `failed` despite unattributed mirrors `1395393`/`a50bbda`/`294cbf1` in three child repos | r10 §Conformance 1 |
| Prompt embeds contract | 1–10 | 41 of 45 child reports missing a `SHONEN` heading (`grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l`, at `0a30b44`) while 0/58 prompts named it; round 9 measured 36/40 and 0/46 — the fleet-2 template narrowed nothing; at round 10 it carried 1 of 5 child-lane items; round-9 prompts quoted the pre-`c8f9f57` route map (`m_composer`/`m_antigravity` not in the allowed three) | r10 M6/M7, §Conformance 9; r9 |
| Closure entries | 10 | rounds 2–11 unclosed: `rounds` held `[0, 1, 1.5, 9]` at `0a30b44` while 66 lane-rounds dispatched, 58 terminated; one lane's round 9 dispatched 17:57, an hour after another's closed 16:47 — fleet-wide completion unobservable | r10 §Closure |
| Closure entries | 9 | entry's 6 of 8 rows contradicted evidence when written (kake `in-flight` vs report committed 17:44:34 in `4c81066`; kumitate `ok` with no derivable report; counters that never reached 9) | r10 §Conformance 2 |
| Closure entries | 1 | kagi `not-dispatched` against `launch kagi round=1` (15:50:56); aggregator `in-flight` steered onward 15:52:38 with no report | r10 §Conformance 3 |
| No closure channel | 2–10 | rounds 2–9 had no lane instantiated as integrator; rounds 2–8 produced no closure artifact at all, rounds 5–9 report prose instead of `rounds` entries; generated protocol prompts name none of steps 1–4 (`grep -c MANIFEST .ufo/prompts/protocol-round-10.md` → 0; rounds 4–9 mention it only to forbid it — "never MANIFEST.json") | r10 §Integrator, §Closure |
| Dispatch evidence | 1–3 | steer-era rounds dispatched with no prompt files; a prompt-only test misreads 8 real lane-rounds as undispatched | r10 §Dispatch digest |
| Liveness probes | 10 | 18:31 probe: `status --lite` still listed kasegi r12/kagi r9/kake r10 (all completed 18:27:55-58); `lane-dead-no-report` 0 in 135 log lines — only `omp down` removes a mission | r10 §Conformance 5 |
| Append-only `rounds` | 10 | `rounds[1]` cited 13× across `kagi-shokunin/` at round 10 (`grep -rn 'rounds\[' *-shokunin \| wc -l` → 13; the count drifts as files churn — index citations must keep resolving) | r10 §Closure |
| Retroactive typing | 10 | rounds 2–8 predate fleet-2 (`609ecb6`, no axis-move duty) and the integrator role (`4c81066`, round 9) — retroactive rows are not passes | r10 §Closure |
| Ledger | 10 | round-10 audit found `.ufo/reports/AGGREGATE.md` absent — every defect routed since round 5 lived only in report prose; rounds 5–8 routed zero defects to disk despite open routing lines | r10 D-33 |
| Aggregator write scope | 3 | `6565e89` touched `CORPUS.md` + nine `.ufo/prompts/*.md` outside corpus-only scope; adjudicated a historical defect, no rewrite | r10 D-41 |
| Evidence standard | 9, 4 | unresolvable pointers: kake `/tmp/kimi_audit.py`, kumitate `local://kumitate-r6-*`, kengaku `/tmp/bench-r7/`; kake's `~21:15Z` label preceded the clock by ~46 min (future-dated); round-4 audit re-executed 111 citations; `git rev-parse round-4` fails wherever the tag doesn't exist | r9 §Evidence; r4 audit |
| Drift pins | 6, 9 | kagi's pins verifiable for only 2 of 13 files — a fingerprint printer with no stored baseline (the body text formerly pinned this to a "round-8 audit"; the figure is recorded in the round-6 aggregator audit and the round-9 kagi report) | r6/aggregator.md; r9/kagi.md |
| Canonical form | 8 | three repos carried `SHONEN.md` variants (kagi 4 bare `[x]`, kotoba per-box prose, kengaku stale 3-box) | r8 §Audit |
| Prompts committed | 10 | 8 of 58 prompt files untracked at `0a30b44`, including all four dispatches of that round | r10 M5 |
| Tracked runtime | 10 | `.ufo/state` (16 files) + `watchdog.log` tracked since `609ecb6` although the clause said "stay untracked" | r10 §Conformance 6 |
| Lane identity | 9 | kotoba `3b029b8` authored under the operator's personal identity blurs the `[x]` non-author line | r10 D-30 |
| Protocol self-defect | 10 | `PROTOCOL.md` grew 387→583 lines with ~29 inline incident references and 17 duplicated rule pairs → round-11 compaction | r10 D-48 |
| Gate standard | 10, 12 | 14 committed verdict scripts across the six child lanes, 13 already declaring a `0/1` map; reserved codes diverge (kotoba `3` no-baseline in two scripts — and inconsistently, its `--json` path returns `0` where its text path returns `3`; kumitate `64` usage in three) and `kake-shokunin/scripts/probe-delta.mjs` self-declares "a report, not a gate"; self-test depth splits four ways (exit+expected-id: kagi drift-pins, kengaku `run_selftest()`, kumitate; exit-only: transcript-scan; model-only: kotoba `--self-test`; fixture/model: verify_corpus_independent) | l0 kengaku r10; r12 |
| Gate standard | 12 | three gates red at the round-12 reading, none attributable to a closed lane-round: kengaku's grades the tree it runs against (worktree `CHECKS n=280 mismatches=1` FAIL vs the same gate over its cited commit `06cdc98` at `n=149 mismatches=0` PASS), kagi `TRANSCRIPT_SCAN: HITS=2` and kotoba `25/27` (`omp.db.rows` 18 vs 17) read host surfaces outside lane control; all five hermetic self-tests pass run as a non-owner from the main repo in ≈8.4 s — kumitate `57/57`, so the `49/49` in the l0 question is stale | r12 |
| Row identity | 12 | keying `rounds[]` by `lane_rounds` instead of by `entry.round` yields 66 ok / 3 failed / 13 not-dispatched / 1 in-flight over 83 rows, erasing 3 of the 4 carried `in-flight` rows and manufacturing a phantom `(aggregator, 9)` out of pre-fleet-2 `rounds[3]`; entry-keyed last-wins reproduces the round-11 record exactly (73 / 4 / 23 / 4 over 104 rows) | r12 |
| Orphaned report | 12 | aggregator r7's report was uncommitted when its mission completed (20:13:17) and its r8 respawn self-landed it 19 min 17 s later (`6d27283`, lane identity); kotoba r12's stayed untracked carrying the literal placeholder `LANE_HASH` at line 224 where its round-work hash `633859f` belongs, so an integrator durability sweep would have frozen an unfilled placeholder into a permanent object | r12 |
| L0 durability | 12 | `.ufo/l0-questions.md` had no committer: the kengaku-r10 and kumitate-r10 questions sat uncommitted across two rounds until a lane sweep carried them (`46e9ec3`, kumitate r11, operator identity, +5/-1 outside its own report path), and a kake r14 in-place rewrite of its own filed line went unrecorded | r12 |
| Stale-lane actuator | 12 | the progressing test's "files modified under its repo" half attributes a sibling's work to the lane: kotoba r13 graded progressing on three `aggregator-shokunin` commits (`683d147`/`7163c81`/`ed5c261`) with no kotoba-authored commit since its launch | r12 |
| Unlanded report | 12 | kagi r12 wrote 13620 B to its contract path at 21:02 while its mission was still live: untracked, `SHONEN`=0, its only cited hashes (`4391b3b`/`7c3377c`/`e0a04d8`) are `aggregator-shokunin` box-3 commits, its own r12 work uncommitted, no `complete` line, counter still 12 — a draft at the contract path that the driver's existence signal will nonetheless complete on | r12 |
