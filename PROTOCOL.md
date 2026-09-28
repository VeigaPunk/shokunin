# Shokunin Protocol

> 職人 — an artisan specialist that earns its domain through demonstrated craft.

A **shokunin** is a domain specialist, distinct from generic agents: it owns a
domain, accumulates hard-won knowledge, and is iterated by rounds of swarm work
until it can iterate itself.

## Lifecycle

```
mint → shonen (apprentice) → shokunin (artisan of a domain) → jin'i-ryu (self-iterating)
```

- **Shonen** — minted when a domain demand is proven: two documented
  *unplaceable* demand instances (work no existing province could absorb) or
  an explicit operator directive — the bar closure step 3 applies, stated
  once here. It starts with a scoped `SKILL.md` +
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
lossy paraphrase is exactly what the snapshot clause would void. Each
*child-lane* prompt carries, as quoted protocol text: the report path and
filename, the commit-before-report ordering, the `SHONEN` heading
requirement, the commit-hash citation rule, and the lane's write scope.
The aggregator prompt instead embeds *its* operative set verbatim: report
path, the ledger path and refresh duty, child-repo commit ownership
(aggregator commits its own files, pathspec-limited), the corpus-only
write scope, and the L2 minimum — a number this file does not own:
`MISSION.md` §L2 concurrency is its source (currently 8 subagents in one
batched call). The protocol prompt embeds its own duties: this file's
re-read requirement, the integrator-of-record closure steps, and the L2
minimum. Text that exists only in this file reaches the
lanes that re-read it and is skipped by the ones that don't — rounds 1–10
measured the gap: 45 child-lane reports filed, 41 missing a `SHONEN`-led
heading (`grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md | grep -vE
'protocol|aggregator|AGGREGATE' | wc -l` → 41 of 45, re-executed
2026-09-28 at main HEAD `0a30b44`) while 0/58 generated prompts named it —
round 9 measured 36/40 and 0/46, so the fleet-2 template narrowed nothing;
a prompt-fidelity defect named in round notes does not fix the
template — the integrator's report must also carry the exact corrected
`lane_prompt()` text required, since `scripts/` is edited by the
operator-side maintainer, not a lane.

Rounds are per-lane counters, not a fleet-global clock: the driver keeps
`.ufo/state/<lane>.round` and lanes can sit on different round numbers at
the same wall-clock moment (a late-joining or respawning lane's `round-3`
is not the same event as another lane's `round-3`). `reports/round-<N>/`
collects whichever lanes ran their Nth round; the integrator closes round
`<N>` per lane, not per fleet.

A lane report **lands last** — written only after the lane's child-repo work
is committed, and it must cite the commit hash. Landed means committed:
changes that exist only in a working tree do not count for the round. The
cited hash is the lane repo's `HEAD` at the moment the report is written —
a report naming a hash the repo does not contain fails verification, and a
cited hash that is not an ancestor of `HEAD` at closure is a conformance
defect (amending or rewriting a commit a report already cited orphans the
record; `git merge-base --is-ancestor <hash> HEAD` is the check). Corrections
land as new commits, never by amending a cited one — and append-only files
(`LOG.md`) take an appended correction entry pointing at the superseded
text, never an in-place rewrite (round-9: kengaku `85b22e3`→`f147a27`
orphaned its own report; `LOG.md:9` round-5 entry rewritten in place).
Landed also means landed *by the lane*: the commit that adds
`.ufo/reports/round-<N>/<id>.md` carries the lane identity, because the
driver completes the mission the instant the file reaches disk and any
later fleet-level commit can sweep it (round-10 measurement: 21 reports
were added by `6565e89`, 21 by `609ecb6`, 4 by `0a30b44` — 46 of 60 swept
into three commits authored by identities that are not the filing lane's;
`609ecb6` at 17:38:25 added `round-10/kasegi.md`, whose lane-round had
completed at 17:32:47). A swept report is still landed — history is never
rewritten to fix attribution — but the integrator records the attribution
defect in the round notes, and a lane whose report is still uncommitted
when its mission completes has not satisfied this clause.

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
holds a round open in the integrator's ledger — though it does hold the
*driver* open, since `report_of()` is the driver's completion signal and the
mission stays live until the stale-lane rule below fires. `failed` covers
every lane-round that was prompted or dispatched and has no report by
closure, including a prompt left behind by a launch that failed
(`lane_prompt()` runs before `ufo-sighting launch`, so a `launch-fail` line
leaves an orphan prompt on disk — 0 observed as of round 10, structural).
A mission still open more than two driver ticks after
its steer is a stale-lane review trigger — its working context predates
landed protocol changes, and a lane whose work is done but unreported
stalls the same way — and the integrator may record it `failed` so the
driver respawns it on a fresh prompt. The trigger needs an actuator: every
dispatched lane's report must list any mission open longer than two driver
ticks — age computed from the launch timestamp, not the tick counter, which
resets when the driver restarts (round-10: `tick=13` at 17:32:48 then
`tick=1` at 17:50:21, `.ufo/watchdog.log:117,126`) — and must say whether
it is *progressing* (a commit authored by that lane after its launch) or
*silent*; the integrator-of-record records `failed` from that listing for
silent missions without further review and flags progressing ones in the
round notes rather than killing live work. A respawned
mission inherits its predecessor's working tree: uncommitted
*lane-authored* changes it finds are uncommitted round work under the
landed-means-committed rule — the new lane resolves them
(commit-under-its-entry or revert) before it files its own report.
Uncommitted **aggregator-owned** files (`corpus/lessons/round-*-aggregator-*`)
are not the lane's to commit: the lane records them in its report and
leaves them for the aggregator to resolve (round-9: aggregator mirrors sat
uncommitted in kake/kumitate/kagi; kasegi swept one into `c80c2a1`, an
unlogged misattribution).

A file at the report path is not automatically a report. The driver's
completion signal is that path's existence (`report_of()` in
`scripts/shokunin-watchdog.sh`), so a contentless **completion marker**
closes a lane-round with no work behind it: the round-10 audit found
`.ufo/reports/round-8/kengaku.md` (101 B, "work pushed") advanced kengaku
8→9 while `kengaku-shokunin` HEAD stayed `f147a27` "round-7" — no round-8
commit, no round-8 `LOG.md` entry, so the marker's claim is false. A filed
report that records no lane work (no changes, no evidence pointer, no
resolvable commit) is a marker, not a report: the integrator records that
lane-round `failed`, keeps the marker file as a conformance defect, and
names the counter advancement in the round notes. A short report that
names a real committed round-work hash is a *defective* report, not a
marker (round-10: kotoba `8c300ad`, kumitate `7a4c9a0`) — status `ok`,
minimum-content defect recorded. A marker that names nothing checkable is
`failed` whatever the lane actually did: the round-5 aggregator marker
cites no commit, so that lane-round is `failed` even though aggregator
mirror commits (`1395393`, `a50bbda`, `294cbf1`) sit unattributed in three
child repos. This does not relax step 1: contract violations inside a real
report stay status-neutral defects.

**Integrator of record.** The integrator this protocol assigns work to is
the round's `protocol` lane — a role, not a separate rostered lane; where a
generated driver prompt conflicts (e.g. "never MANIFEST.json"), this file
wins per the snapshot clause. Rounds 2–11 produced no closure artifact:
`MANIFEST.json` `rounds` held `[0, 1, 1.5, 9]` while 66 lane-rounds had
been dispatched and 58 had terminated (`.ufo/watchdog.log` launch/steer
lines vs `.ufo/reports/round-*/`, round-10 audit). Two causes, both
addressed here: no lane was instantiated as integrator (rounds 2–9), and
once one was, the entry shape had no semantics for a per-lane-counter
driver, so no entry could be written without inventing statuses for lanes
sitting on other counters (round 9's entry: six of its eight rows
contradicted the evidence available when it was written and three still
do — see step 4). Its main-repo writes expand by exactly
three: appending `MANIFEST.json` `rounds` entries, the conformance/routing
record inside its own report (the round notes), and committing
already-generated `.ufo/prompts/*.md` so dispatch evidence is durable — it
never edits a prompt or the script. Everything else stays
`PROTOCOL.md`/`ROADMAP.md`/`SCORECARD.md`/`LOG.md`/its report; `scripts/`
and `.ufo/state/` remain operator-side — the protocol lane names required
template corrections in its report but never edits the script.
The integrator's closure artifact is its own round report: a protocol-lane
report carrying no closure record — the statuses it wrote, or a statement
of why none was writable — is an incomplete report whatever else it
contains. That is the only delivery channel the current driver guarantees:
the generated protocol prompts name none of steps 1–4
(`grep -c MANIFEST .ufo/prompts/protocol-round-10.md` → 0; rounds 4–9
mention it once each, only to forbid it — `protocol-round-9.md:3` "never
MANIFEST.json"), so the duty reaches the lane solely through this file's
re-read. That is why rounds 2–8 produced no closure artifact at all and
rounds 5–9 produced report prose instead of `rounds` entries.

A round is **completed** when every dispatched lane has either reported or
been recorded failed by the integrator — a failed lane counts; a missing
report does not. Under the respawn driver lanes hold different counters at
the same instant (one lane's round 9 was dispatched 17:57, an hour after
another lane's round 9 closed at 16:47 — `.ufo/watchdog.log:88,130`), so
fleet-wide completion is never observable, and waiting for it is what left
rounds 2–11 without a closure entry. Closure is therefore per lane-round:
each protocol round the integrator closes every lane-round that terminated
since its last pass plus any older one still carrying an unresolved row
(step 4). After closing, the integrator:


1. Reads every lane report and verifies each cited child-repo commit exists
   *and is an ancestor of the lane repo's `HEAD`*; verifies no participating
   repo is left with uncommitted round work (uncommitted aggregator-owned
   files are reported, not lane debt); checks each report for the
   contract-required `SHONEN` heading; checks the round's dispatched
   `.ufo/prompts/*.md` carried the five contract items verbatim per the
   embed clause above **and that any L2 route map quoted in the prompt
   matches the current `MISSION.md` bucket** (round-9: generated prompts
   still quote the pre-`c8f9f57` map — `m_composer`/`m_antigravity` are not
   in the allowed three). A report that violates the report contract
   (missing heading, dead or orphaned hash, report filed before its
   commit) or a prompt missing embedded items is recorded as a conformance
   defect in the round notes — this does not change the lane's status
   unless the round's rules already prescribe `failed`.
2. Lands warranted protocol improvements in this file (a highly valuable
   feature discovered by any domain generalizes to the protocol); routes
   cross-domain defects a lane report filed against a sibling's files to
   the owning lane — and the integrator's report carries one routing line
   per defect **including defects a lane owes its own repo** (self-defects
   ride the same durable queue; routing is integrator work and must exist
   in an artifact). The aggregator mirrors each routed defect into the
   owning repo's `corpus/lessons/` (aggregator-owned naming) and keeps an
   **open routed-defects row** in its `AGGREGATE.md` ledger until the
   owning lane's `corpus/lessons/` or `SKILL.md` correction lands;
   unresolved rows are re-flagged in the ledger each audited round. On its
   first audited round after any absence the aggregator sweeps intervening
   lane reports and round notes and reconciles ledger rows before new
   audits. The ledger row — not round notes alone — is the durable queue,
   since defects outlive the round that routed them; while the aggregator
   is absent the integrator's report itself is the fallback record.
3. Mints a new shonen only if evidence shows an unserved domain — minimum
   evidence per **Lifecycle**: two documented *unplaceable* demand instances
   or an explicit operator directive. `ROADMAP.md` restates the bar; where a
   restatement drifts, this file wins and the drift is a round-notes defect.
4. Appends one entry to `MANIFEST.json`'s `rounds` array (integrator-of-record
   scope; each lane's own `LOG.md` entry remains lane work, not integrator
   work — lanes write inside their own repos). Round-entry shape:
   `{round, date, type, lanes: {<id>: <status>}, promotions: [{id, from, to}], minted: [id...], notes}`
   where `<status>` is `ok | failed | not-dispatched | in-flight`. `type`,
   `closed_at`, `protocol_updates`, and other annotation keys are optional.
   Semantics under a per-lane-counter driver:
   - **Partial entries are the norm.** Write the entry for round `N` as soon
     as one lane's Nth lane-round terminates: a terminal status for every
     `N` lane-round that has terminated, `in-flight` for lanes dispatched
     and still open, `not-dispatched` for lanes with no dispatch evidence
     **as of `closed_at`** — so `closed_at` is required on any entry
     carrying a `not-dispatched` row. Waiting for all eight counters to
     reach `N` waits forever; that is what left rounds 2–11 unclosed.
   - **Dispatch evidence** is the `.ufo/watchdog.log` dispatch line —
     `launch <lane> round=N` (respawn driver, written only after a
     successful launch) or `steer <lane> -> round N` (steer-era driver:
     rounds 1–3 were dispatched with no prompt files at all, so a
     prompt-only test misreads 8 real lane-rounds as undispatched). The
     committed `.ufo/prompts/<lane>-round-N.md` corroborates mission
     *content* and must be committed to be durable, but `lane_prompt()`
     writes it before the launch is attempted — a prompt with no dispatch
     line is an attempted dispatch and records `failed`. **Completion
     evidence** is a `.ufo/reports/round-N/<lane>.md` that satisfies the
     report contract; a completion marker is not a report (see above) and
     makes the lane-round `failed`. **Termination evidence** is a
     `complete <lane> round=N` line or the lane's counter passing `N`.
     Liveness probes are not evidence of an open mission: `ufo-sighting
     status --lite` still lists a mission after the driver `complete`d it
     (round-10 probe at 18:31: the run-ids of kasegi r12, kagi r9 and kake
     r10 — all completed 18:27:55-58 — each still match once in the status
     output, as do the eight live ones; only `omp down` removes a mission),
     so the driver's `live` test can never fail while its daemon is up and
     its `lane-dead-no-report` retry path is unreachable (0 occurrences in
     135 log lines). `in-flight` is therefore decided from the absence of
     both a `complete <lane> round=N` line and a report — never from a
     status probe.
     `.ufo/watchdog.log` is mutable and the driver appends to it
     concurrently, so its line numbers drift: the round notes carry a
     committed digest (timestamp + text) of every dispatch/complete line a
     status rests on, and that digest — not the live log — is the pointer
     that resolves at closure.
   - **`in-flight` is debt, not a resting status.** Every `in-flight` row is
     resolved by the next protocol round, which appends
     `{"round": N, "type": "closure-correction", "closed_at": …, "lanes":
     {<id>: <terminal status>}}` — never an in-place edit, same discipline
     as `LOG.md`. `rounds[].round` is therefore not unique: consumers read
     the array in order and the last row for a lane wins. A lane dispatched
     for its Nth round *after* round `N` closed rides the next
     closure-correction for `N` — never dropped, never folded into `N+1`.
   - No lane may be recorded `not-dispatched` while dispatch evidence for
     that lane-round exists, and no lane may be recorded `in-flight` unless
     its mission was live at `closed_at`. A row contradicting evidence is a
     conformance defect of the entry: round 9's recorded kake `in-flight`
     against a report committed 17:44:34 (two minutes before the entry,
     `4c81066`), kumitate `ok` and aggregator `in-flight` against counters
     that never reached 9 (`.ufo/state/` 8 and 6), and kengaku/kotoba/kagi
     `in-flight` before their 17:50–17:57 dispatches; round 1's recorded
     kagi `not-dispatched` against `launch kagi round=1`
     (`.ufo/watchdog.log:3`) and aggregator `in-flight` for a mission
     steered onward at `:17` with no report.
   - **A row names the lane-round it describes.** `lanes` values stay status
     strings; the optional `lane_rounds: {<id>: <n>}` map records a lane's
     own counter where it differs from the entry's `round` and is required
     on every `not-dispatched` row — the counter the lane actually held is
     what makes such a row falsifiable. An `ok` row needs no pointer:
     `.ufo/reports/round-<n>/<id>.md` is derivable, and its absence
     falsifies the row (that is how round 9's kumitate `ok` is provably
     wrong). `failed`, `in-flight`, and `not-dispatched` rows carry their
     pointer in `notes`.
   - **Retroactive closure is typed, and is not a pass.** Entries for
     lane-rounds that terminated before the integrator role existed carry
     `type: "retroactive-closure"` and notes stating that the statuses are
     presence-of-evidence only, that step-1 verification (hash ancestry,
     `SHONEN` heading, prompt fidelity) did not run at the time, and — for
     rounds before fleet-2 (`609ecb6`) — that no axis-move duty existed.
     Promotion and axis reviews must never read a retroactive row as a
     contemporaneous pass.
   - **`rounds` is append-only after closure.** Corrections are appended
     entries carrying `type: "closure-correction"` and
     `supersedes: {round, type, date}` naming the row they replace — never
     in-place edits, never prepends, because index citations into the array
     must keep resolving (`rounds[1]` is cited 13 times across
     `kagi-shokunin/`, e.g. `LOG.md:4`, `corpus/README.md:6`,
     `corpus/lessons/round-1.md:3`; `grep -rn 'rounds\[' *-shokunin | wc -l`
     → 13). Consumers read the array in order; the last row for a lane wins.

The **aggregator** lane is a main-repo lane that reviews every child repo's
`corpus/` each round (per `CORPUS.md`), files gaps as lessons inside the
child repos, and files its own round report at
`.ufo/reports/round-<N>/aggregator.md` covering per-repo corpus verdicts and
cross-lane learnings. It is the sole exception to lane write-scope: it may
create or repair `corpus/` inside any child repo — nothing else: no
main-repo files outside its own report and ledger. Every file it creates
inside a child repo is **committed by the aggregator itself at creation
time**, pathspec-limited to its own files, under its own subject
(`corpus: round-<N> aggregator …`) — never left uncommitted for a lane's
round commit to sweep, and a lane never commits an aggregator-owned file.
Alongside the per-round report it maintains one rolling audit ledger —
canonically `.ufo/reports/AGGREGATE.md` (the `round-2/AGGREGATE.md`
snapshot is relocated there by its next refresh; until then it remains
readable evidence — superseded, not voided — and no third path counts).
While the canonical ledger does not exist, the integrator's round notes are
the queue of record: the round-10 audit found `.ufo/reports/AGGREGATE.md`
absent (`ls .ufo/reports/AGGREGATE.md` → no such file), so every defect
routed since round 5 lived only in report prose with no durable row.
The ledger is append-only in the same sense as `LOG.md` — refresh sections
supersede earlier rows explicitly rather than rewriting them. An
aggregator round report is incomplete unless the ledger was refreshed or
the report names why no row changed — and a round filed without the ledger
duty keeps the routed-defect queue empty by construction (rounds 5–8
routed zero defects to disk despite open routing lines).

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

An evidence pointer must resolve at *closure* time, not only at write time:
paths under `tmpfs` (`/tmp`, `/dev/shm`), session-scoped `local://`
artifacts, and any pointer a fresh session cannot reach are not evidence —
commit the artifact or cite a reproducible command (round-9: kake
`/tmp/kimi_audit.py`, kumitate `local://kumitate-r6-*` maps, kengaku
`/tmp/bench-r7/` workdir all unresolvable outside the producing session).
A timestamp on evidence must be at or before the commit that ships it —
future-dated evidence is a conformance defect (round-9: kake's `~21:15Z`
label preceded the clock by ~46 min).

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
| `SCORECARD.md` | Axis scores per `AXES.md`: owned axes → score 0–10 → evidence pointer → last-change round, plus `planned` and `retired`. Every score is a claim: it carries the counting command that produced it and the commit it was measured against, so a reader can re-derive it. Main-repo lanes keep theirs at the main-repo root |

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
  Only integrator roles write main-repo files — `MANIFEST.json`,
  `PROTOCOL.md`, `ROADMAP.md`, `CORPUS.md`, `MISSION.md`, `AXES.md`,
  `scripts/`, `.ufo/` state and prompts. `MISSION.md`, `AXES.md`, and
  `scripts/` are operator-side integrator files: the protocol lane names
  the corrections they need in its round notes and does not edit them. The
  protocol lane holds the protocol/roadmap/report writes and,
  as integrator-of-record, `MANIFEST.json` `rounds` appends; `MANIFEST.json`
  edits *outside* `rounds` (roster, rank, minting) remain operator-side
  integrator work. Lanes write only inside their own child repo and their
  lane report at `.ufo/reports/round-<N>/<id>.md`; the two main-repo lanes
  (`protocol`, `aggregator`) additionally keep `SCORECARD.md` and `LOG.md`
  at the main-repo root, because their axes are fleet-level and the
  `AXES.md` per-repo contract applies to them there. `.ufo/reports/` and
  `.ufo/waves/` are the round's written evidence and are committed with the
  round's integration commit, as are that round's generated
  `.ufo/prompts/*.md` — an untracked prompt is non-durable dispatch
  evidence (round-10: 8 of 58 prompt files untracked, including all four
  dispatches of that round). `.ufo/state/` and `.ufo/watchdog.log` are
  driver runtime that churns every tick: they have been tracked since
  `609ecb6` (16 state files + the log) although this clause said they stay
  untracked, so no lane commit may include them — pathspec-limited commits
  are the enforcement; untracking them is operator-side work named in the
  round notes.
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
- Lane authorship is auditable: each child repo is configured at mint so
  round commits carry the lane identity (`<lane>-shokunin` /
  `<lane>@shokunin.local` — kagi/kake/kumitate/kengaku already do; kotoba's
  `3b029b8` committed under the operator's personal identity blurs the
  author/non-author line the `[x]` verifier rule depends on). A lane
  finding its repo unconfigured sets `git config user.name/email` once and
  notes it in `LOG.md`; commits under the operator identity made by lane
  rounds are a conformance defect.
  Main-repo commits follow the same rule and cannot rely on `git config`,
  because the shared main-repo identity is the operator's personal one: a
  main-repo lane commits with
  `git -c user.name=<lane>-shokunin -c user.email=<lane>@shokunin.local commit …`.
  Round-10 measurement: 0 of 60 reports were added by a lane-identity
  commit — 33 by the operator's identity and 26 by `shokunin
  <shokunin@local>`, a third identity that is neither operator nor lane.
- `corpus/` inherits the evidence standard: every `knowledge/` entry cites a
  resolvable source; `corpus/lessons/` entries cite the round and its LOG.md
  entry or lane report.
  Corpus corrections are new entries, never in-place rewrites — in both
  directions: no lane edits another lane's or the aggregator's corpus
  files; `round-<N>-aggregator-*.md` are aggregator-owned.


## Fleet-2 conventions (adopted)

- Expertise axes live in `AXES.md`; each lane owns a named subset and works one
  axis-move per round, measured in `SCORECARD.md` (per child repo; the two
  main-repo lanes keep theirs at the main-repo root). An axis-move inherits the
  evidence standard: before and after numbers each carry the counting command
  and the commit they were measured against, and a score no reader can
  re-derive is an opinion, not a measurement. Axis work does not displace the
  file contract — a round that moves an axis while `corpus/`, `LOG.md`, or
  `SHONEN.md` drift is a conformance defect like any other.
- `MISSION.md` is the mission SSOT: fleet shape, model map, concurrency floor,
  push rule, L0 side channel. Watchdog prompts bind to it.
- Precedence between the two SSOTs: `MISSION.md` owns fleet shape, the model
  map, the concurrency floor, the push rule, and the L0 channel;
  `PROTOCOL.md` owns process, evidence, and gates. Where they conflict on
  process — `MISSION.md`'s unconditional "commit then push" against this
  file's operator-gated hold, for instance — `PROTOCOL.md` wins and the
  conflict is named in the round notes; neither file is edited by a lane.
- L0 side channel: lanes append `.ufo/l0-questions.md`; aggregator surfaces.
