# Report skeleton — `shokunin:.ufo/reports/round-10/aggregator.md` (structure only; no measurements)

**Author:** `scribe` seat (round-10 wave). **Status:** skeleton. The aggregator L1 fills every `L1-FILL(<id>)` cell and
lands the result at the contract path `shokunin:.ufo/reports/round-10/aggregator.md` (main repo; the fleet's
`respawn-per-round` completion signal is that file).
**Model of shape:** `shokunin:.ufo/reports/round-9/aggregator.md` (read, not copied) — stamp · the move · verdicts ·
measurements · what the round falsified · L2 wave digest · routed findings · L0 surfacing · `SHONEN` · compliance ·
next. This skeleton reorganises that shape around round 10's parts (A registry home, B `r4` adjudication, C
per-rule movement) and keeps every standing duty.
**Facts the report must serve:** `shokunin:.ufo/waves/round-10/CONTEXT.md` (host facts, seat write scope, gate usage —
`--selftest`, `--all`, `--snapshot`, `--registry` — exit map, implemented checks `r2 r4 r7 r8 r10 shonen`, declared
not-evaluated checks) and `shokunin:SCORECARD.md` §Planned (round 10 entry: parts A/B/C and the falsifiers).
**Companion skeleton:** `shokunin:.ufo/waves/round-10/scratch/ledger-15-skeleton.md` holds the ledger §15 shape; every
report cell below should resolve to a ledger cell of the same id suffix plus the report's own summary prose.

## Conventions for this file

- **Path convention** (D-128 forward fix): bare paths are main-repo-relative; a main-repo path may also be written
  `shokunin:<path>`; a child-repo path is always written `<repo-dir>-shokunin:<path>`.
- **Numeric policy.** No digit in this file is a claim. Every score, revision, hash, count, tally, exit code, age or
  verdict carrying a number is an `L1-FILL(<id>)` cell. Digits survive only as identifiers: section refs (`§14.2`),
  round tags (`round-9`, `round-10`), defect keys (`D-127`, `D-141`), proposals (`P-v`), rule tags (`r4`, `r10`,
  `box-3`), lane/seat names, and paths.
- **Tables.** Every content table below is header-only; the `**Cells:**` line under each table names the `L1-FILL` id
  that owns each column and the row axis. The single exception is the index table immediately below, whose rows are
  `L1-FILL` ids (identifiers), not data.
- **Mandatory contract items.** The report carries the `## SHONEN` heading (`PROTOCOL.md` report contract: a report
  without the heading does not satisfy the contract) and cites the commit it was built on. It names every L2 seat with
  its deliverable path, and it states push scope explicitly.
- **Order.** All work is committed and pushed **before** this report is written; the report's own write + commit +
  push is the round's last action (the driver completes a mission on file existence).
- **Roster scope.** Where a row axis says "per child repo", it means the roster the table states: the repos rostered at
  the round-10 cutoff plus any lane minted while the wave ran (see `## Mid-round scope change`). A table grading a
  different set says so in its own Cells line; never write "all repos" without naming the roster.
- **Attribution.** A file under this lane's wave directory is this lane's evidence even when another author committed
  it. Record the adding author per wave file, and decide any published claim about who committed what with the two
  commands the ledger names, rather than repeating the claim.
- **Proof that zero remain:** `grep -c 'L1-FILL' <this file>` before filling and after; record both counts in
  `R-ZERO-FILL`. A cell that cannot be measured gets `could-not-evaluate` plus the reason — never a silent blank.

## L1-FILL index — every id used in this file

| id | section | what the L1 measures | command to run |
|---|---|---|---|
| R-STAMP | preamble | round, runId, launch time, reading stamps, the commit chain that landed before this report, and this report's own push range | `date -u +%Y-%m-%dT%H:%M:%SZ; git rev-parse --short HEAD; git log --author=aggregator-shokunin -3 --format='%h %aI %s'; git status --porcelain \| wc -l` |
| R-AXIS-SCORE | The move | the chosen axis's score before → after, and the axis that was lowest | `grep -n 'corpus review' SCORECARD.md` |
| R-AXIS-DEBT | The move | which debt the move pays (the queued residual it inherits or re-decides) | `git show HEAD:SCORECARD.md \| sed -n '/### Planned/,/### Retired/p'` |
| R-AXIS-LANDED | The move | one sentence: what landed, in artifacts a non-author can run | the artifacts themselves (ledger §15 cells) |
| R-METHOD-STAMPS | Method | main-repo and per-repo revision + dirty count for every reading this report's cells rely on, over the roster each table states | `for d in kasegi kengaku kake kumitate kotoba kagi kama; do printf '%s %s dirty=%s\n' $d "$(git -C $d-shokunin rev-parse --short HEAD)" "$(git -C $d-shokunin status --porcelain \| wc -l)"; done` |
| R-ROSTER-SCOPE | Method / Mid-round scope change | the roster each table grades, as declared in `MANIFEST.json` at read time versus the cutoff roster, and the read time of each | `python3 -c "import json;print(json.load(open('MANIFEST.json')).get('roster'))"; git log --format='%h %aI %an %s' -2 -- MANIFEST.json` |
| R-KAMA-MINT | Mid-round scope change | the mid-wave mint: mint commit and author, the new repo's HEAD and dirty count, its tracked-file count, its gate run (exit, finding breakdown, provisional flag) and whether its corpus is tracked at the graded revision | `git log --format='%h %aI %an %s' -1 -- kama-shokunin; git -C kama-shokunin rev-parse --short HEAD; git ls-files kama-shokunin \| wc -l; node .ufo/waves/round-9/corpus-gate.mjs --repo kama-shokunin --round 10; echo exit=$?; git -C kama-shokunin ls-files corpus/ \| wc -l` |
| R-WAVE-OWNERSHIP | Mid-round scope change / Push-scope compliance | per file of this lane's wave directory, the commit and author that added it | `git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-10/CONTEXT.md; git log --diff-filter=A --format='%h %an' --name-only -- .ufo/waves/round-10/` |
| R-SIBLING-CLAIM | Mid-round scope change | whether a sibling's published claim about a prior wave being uncommitted holds, decided by the two commands | `git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-9/corpus-gate.mjs; git ls-tree -r <cutoff-rev> --name-only .ufo/waves/round-9 \| wc -l` |
| R-SCOPE-CHANGE | Mid-round scope change | the read-time state of the paths a scope change touches: `rounds` length, untracked main-repo paths, and whether the new lane's directory is a nested untracked repo | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"; git status --porcelain \| grep -c '^??'` |
| R-A-GATE-HOME | Part A | where a legal registry home was found, or the sweep proving none exists | `ls SKILL.md 2>&1; node .ufo/waves/round-9/corpus-gate.mjs --registry` |
| R-A-GATE-ROW | Part A | the row's required fields and their values (or the rejection's rationale) | `grep -n -A30 'Gate standard' PROTOCOL.md` |
| R-A-GATE-CALL | Part A | the call: row landed **or** reasoned rejection — never "conformant" while unregistrable | derived from R-A-GATE-HOME + R-A-GATE-ROW |
| R-B-TOTAL | Part B | `r4` findings before → after class closure | `node .ufo/waves/round-9/corpus-gate.mjs --all \| grep -c '(r4)'` |
| R-B-CLASSES | Part B | findings per declared false-positive class, before → after | `grep -n 'declared\|not-evaluated\|FP' .ufo/waves/round-9/corpus-gate.mjs` + the adjudicating seat's table |
| R-B-COLLISION | Part B | the rule-4/rule-9 collision sub-count (`D-141`) | derived from R-B-CLASSES |
| R-B-KEPT | Part B | the residue defensible as violations rather than as a heuristic | derived from R-B-CLASSES |
| R-B-DISPOSITION | Part B | per class: kept / reclassified / withdrawn / could-not-evaluate, with its by-construction argument | `shokunin:.ufo/waves/round-10/seats/revenger-rule4-intent.md` (seat evidence) |
| R-C-BEFORE | Part C | the revision each repo was graded at in refresh 7 (before state) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 9` |
| R-C-AFTER | Part C | each lane's next landed revision (after state) with timestamp and subject | `git -C <repo-dir>-shokunin log -1 --format='%h %aI %s'` |
| R-C-PERRULE | Part C | per-rule finding count at the before revision and at the after revision, per repo | the gate at both revisions; per-repo `# summary` lines + the finding-id tally |
| R-C-VERDICTS | Part C | per repo: measured revision, verdict, failed rules, movement, seat evidence | the gate at the measured revision + the round-10 verdict seat files under `.ufo/waves/round-10/seats/` |
| R-C-TALLY | Part C | the verdict tally over the repo set and which rule fails fleet-wide | derived from R-C-VERDICTS |
| R-STAND-ROWS | Standing duties | dormancy rows and mint/watchlist rows re-run, with the movement each row shows | bounded `LOG.md` token scan + `.ufo/watchdog.log` scan + `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` |
| R-STAND-FROZEN | Standing duties | the frozen-snapshot runs' verdicts and the gate's sha256 (capability and measurement, two evidences) | `node .ufo/waves/round-9/corpus-gate.mjs --selftest; node .ufo/waves/round-9/corpus-gate.mjs --snapshot <repo-dir>-shokunin <commit>; sha256sum .ufo/waves/round-9/corpus-gate.mjs` |
| R-STAND-KAMA | Standing duties | kama's L0 line byte-identity, its bar re-test, and the endpoint-drift probes | `git show <pin>:.ufo/l0-questions.md \| md5sum; md5sum .ufo/l0-questions.md` + the §12.2 probe block re-run |
| R-STAND-MARKS | Standing duties | marker grading of the window's reports; mints executed over the `rounds` entries | `python3 -c "import json;print([r.get('minted') for r in json.load(open('MANIFEST.json'))['rounds']])"` |
| R-OWED | Standing duties / owed | the carried obligations re-tested: the refresh-7 corrections landed in place, the flagged box-3 contradiction at its lane's next landed revision, and the dormancy rule's still-missing positive test | the owed list in `shokunin:.ufo/reports/round-9/aggregator.md` §Next + the per-repo gates |
| R-SWEEP-WINDOW | Sweep + queue | window enumeration: reports landed, markers, reports missing the `SHONEN` heading, untracked prompts and reports | `git ls-files -o --exclude-standard .ufo/prompts .ufo/reports` + the `^#{1,6} *SHONEN` grep |
| R-SWEEP-MANIFEST | Sweep + queue | `rounds` entries, last-wins status tally, rows stale at read time | the last-wins script committed in `shokunin:.ufo/waves/round-9/seats/sweep-window.md` §2.2 |
| R-SWEEP-QUEUE | Sweep + queue | queue keys: rows, distinct, max, next free, collisions, folds, open rows by owner; and the rows that moved this window | `python3 -c "import re;t=open('.ufo/reports/AGGREGATE.md').read();r=re.findall(r'^\| (D-\d+)',t,re.M);print('rows',len(r),'distinct',len(set(r)),'max',max(r,key=lambda x:int(x[2:])))"` + `shokunin:.ufo/waves/round-10/seats/distiller-queue.md` |
| R-SWEEP-FALSIFIER | Sweep + queue | whether refresh 7's written falsifier triggered, with the consuming evidence | the falsifier text in `shokunin:.ufo/reports/round-9/aggregator.md` §Next + the lanes' citations of the refresh-7 verdicts |
| R-SELF-DEFECTS | Self-defects filed | the rows filed against this lane this refresh, and the cumulative count, with per-row evidence | the rows themselves + ledger §15.13 |
| R-CONTESTED | Contested scope | per standing contested item: owner pair, ruling state, who owes the ruling, deadline/trigger | `grep -n 'contested' .ufo/reports/AGGREGATE.md SCORECARD.md` + the integrator's recorded ruling |
| R-L0 | L0 surfacing | entries by lane + round + opening words, their classification, the operator-answer count, and the lines appended this round | `git log --format='%h' -- .ufo/l0-questions.md; sha256sum .ufo/l0-questions.md; git diff --numstat .ufo/l0-questions.md` |
| R-DISPATCH-SEATS | Dispatch digest | the seats actually dispatched, their roles, and the count against `MISSION.md`'s L2 floor | `MISSION.md` L2-concurrency clause + the L1's own batched dispatch record + `ls .ufo/waves/round-10/seats/` |
| R-DISPATCH-PATHS | Dispatch digest | each seat's deliverable path under the wave directory | `git ls-files .ufo/waves/round-10/ \| sort` |
| R-DISPATCH-LIVE | Dispatch digest | which seats were still live at composition, and how their evidence landed afterwards | `ls -l .ufo/waves/round-10/seats/; stat -c '%y %n' .ufo/waves/round-10/seats/*` |
| R-SHONEN-BOXES | SHONEN | the box assessment per subject, with the verifier id and the evidence pointer each box line needs | per-file reads of the subjects' `SHONEN.md` files |
| R-SHONEN-FORM | SHONEN | canonical-form census: marks, evidence lines per box, deviations, and whether a `[x]` carries a named non-author verifier | the checker in `shokunin:.ufo/waves/round-9/l1-baseline.md` §2 + the gate's `shonen` findings |
| R-WRITESCOPE | Push-scope compliance | write-scope audit: allowed paths written, forbidden paths untouched | `git show --stat <commit>; git status --porcelain` + the wave's sentinel seat file |
| R-PUSH | Push-scope compliance | the main-repo push range, and the pushed state of every child-repo commit this lane made | `git log --oneline <range>; git -C <repo-dir>-shokunin log -1 --format='%h %s'` |
| R-NEXT | Next (round 11) | next round's axis-move, its parts, and the artifact each part lands | derived from `shokunin:SCORECARD.md` §Planned |
| R-FALSIFIERS | Next (round 11) | next round's falsifiers, each written so a re-reader can decide it yes/no | prose the L1 writes (each falsifier names the cell that decides it) |
| R-ZERO-FILL | Next (round 11) | the `grep -c 'L1-FILL'` counts for the ledger-section skeleton and for this report's own fill pass, before → after | `grep -c 'L1-FILL' .ufo/waves/round-10/scratch/ledger-15-skeleton.md; grep -c 'L1-FILL' .ufo/reports/round-10/aggregator.md` |

---

# aggregator round 10 — corpus-review axis-move: gate registry home, `r4` false-positive adjudication, per-rule movement at landed revisions

Paste everything from the `#` title down. The stamp paragraph is prose, written last, and cites the commit chain that
landed before this report.

**Stamp.** Aggregator lane, round 10 of the lane's round cap (`.ufo/state/aggregator.round` = L1-FILL(R-STAMP)). This refresh
does not stamp its cells to one cutoff: every cell names the revision it measured (the `P-s` rule refresh 7
established). Reading stamps, the wave's shape (seats dispatched, one batched call), the artifacts committed before
this report, and this report's own push range: L1-FILL(R-STAMP).

## The move — axis and score

Purpose: one axis, one verifiable improvement, measured. Round 10's axis is **corpus review**; the move is to make the
`CORPUS.md` rule-10 verdicts non-author re-derivable end to end, in parts A/B/C.

| Axis | Score before | Score after | Counting command | Evidence pointer |
|---|---|---|---|---|

**Cells:** one row per aggregator axis scored (corpus review, plus any axis the round touched); `Score before`,
`Score after` = L1-FILL(R-AXIS-SCORE); `Counting command` = the command quoted in `SCORECARD.md`; `Evidence pointer` =
the ledger cell the score rests on. Then prose lines: the debt this move pays (L1-FILL(R-AXIS-DEBT)) and what
landed, in one sentence (L1-FILL(R-AXIS-LANDED)). If the round's axis differs from `SCORECARD.md` §Planned, say so
explicitly and record it as a defect, as refresh 7 did.

## Method

Purpose: state the shape of the wave and the stamps its cells were read at, so a non-author can re-run any cell
without this session.

| Reading | Time (UTC) | Main-repo HEAD | Per-repo HEAD and dirty count | What was read |
|---|---|---|---|---|

**Cells:** rows = one per reading this report's cells depend on; `Time`, `Main-repo HEAD`, `Per-repo HEAD and dirty
count` = L1-FILL(R-METHOD-STAMPS); `What was read` = prose naming the sections, seats and files read at that stamp.
One prose line follows: the gate's identity (sha256, self-test tally, exit, declared not-evaluated checks) — the
capability and measurement evidences the §Gate standard clause requires; the numbers live in `R-STAND-FROZEN` and the
ledger's `L-GATE-*` cells. One further line states the **roster scope** this report's tables grade
(L1-FILL(R-ROSTER-SCOPE)): the cutoff roster plus any lane minted while the wave ran, each table naming its own set.

## Part A — `corpus-gate.mjs` gains a legal registry home, or a reasoned rejection (`D-127` / `P-v`)

Purpose: `PROTOCOL.md` §Gate standard places registry rows in each lane's `SKILL.md`, and the main repo has none, so as
written the clause leaves a main-repo gate unregistrable. **Falsifier:** the gate may not be called conformant while
unregistrable.

| Measure | Before | After | Command |
|---|---|---|---|

**Cells:** rows = the measures that define this part (rows registered for the gate; candidate homes swept; the
conformant-versus-unregistrable call); `Before`, `After` = L1-FILL(R-A-GATE-HOME) and L1-FILL(R-A-GATE-CALL);
`Command` = the invocation quoted. A one-row table is acceptable if the part reduces to one measure, but the
conformant/unregistrable call is always its own row.

| Field (from the registry clause) | Value | Source |
|---|---|---|

**Cells:** rows = the clause's required fields, read from the clause and not invented; `Value`, `Source` =
L1-FILL(R-A-GATE-ROW). If the outcome is a rejection, replace this table's rows with the rejection's numbered reasons
and say in the prose above that the row was not landed.

## Part B — the `r4` heuristic's declared false-positive classes, closed

Purpose: refresh 7 declared false-positive classes for an `r4` heuristic whose raw count mixed real violations with
by-construction artifacts (notably the rule-4/rule-9 collision `D-141`). **Falsifier:** the `r4` cell may not be
restated without its classes.

| Class | Rule pair | Before | After | Disposition | By-construction argument |
|---|---|---|---|---|---|

**Cells:** rows = the declared classes plus any the adjudicating seat added (name them; never renumber a key);
`Before`, `After` = L1-FILL(R-B-CLASSES); `Disposition`, `By-construction argument` = L1-FILL(R-B-DISPOSITION); the
collision row's sub-count is also L1-FILL(R-B-COLLISION).

| Measure | Before | After | Command |
|---|---|---|---|

**Cells:** rows = the `r4` total and the residue defensible as violations, never folded into one row; `Before` =
L1-FILL(R-B-TOTAL); `After`, plus the defensible-residue row = L1-FILL(R-B-KEPT); `Command` = the invocation quoted.
Then one prose line stating which finding-id class the gate itself would need to change, or why the gate is left
untouched.

## Part C — per-rule movement at each lane's next landed revision

Purpose: part C is the currency half of the duty — re-run the gate at each lane's **next landed** revision and report
what moved per rule. **Falsifier:** a verdict that does not name its revision.

| Repo | Before revision | After revision | After commit time | After commit subject |
|---|---|---|---|---|

**Cells:** one row per repo in the stated roster scope (a lane minted mid-wave is its own row — its verdict names
whether its corpus is tracked at that revision, since an untracked corpus makes the verdict provisional); `Before
revision` = L1-FILL(R-C-BEFORE); `After revision`, `After commit time`, `After commit subject` = L1-FILL(R-C-AFTER).

| Repo | Rule | Before | After | Movement | Seat evidence |
|---|---|---|---|---|---|

**Cells:** rows = one per (repo × rule) pair in the union of the two runs' rule sets (state the pairing rule in one
line above the table, so a rule that appeared or vanished is visible rather than dropped); `Before`, `After`,
`Movement` = L1-FILL(R-C-PERRULE); `Seat evidence` = the round-10 seat file path.

| Repo | Measured revision | Verdict | Failed rules | Movement versus refresh 7 | Seat evidence |
|---|---|---|---|---|---|

**Cells:** one row per repo in the stated roster scope; every measurement column = L1-FILL(R-C-VERDICTS). Beneath the
table: one line
with the tally and the rule that fails fleet-wide (L1-FILL(R-C-TALLY)), and one line restating that
`could-not-evaluate` is a cell grade, never a repo verdict.

## Standing duties

Purpose: the per-refresh duty. Rows are revision-stamped claims, not facts; a row that did not move says so with its
command.

| Duty table | Row identity | Movement observed | Command |
|---|---|---|---|

**Cells:** rows = one per standing row actually re-run (the dormancy rows for every lane in the stated roster scope,
including any lane minted mid-wave and this lane itself; the mint/watchlist candidate rows, one of which may have just
been consumed by a mint; the frozen-snapshot rows; the marker/mint cells) — name each row; `Movement observed` =
L1-FILL(R-STAND-ROWS), L1-FILL(R-STAND-FROZEN) and L1-FILL(R-STAND-MARKS) as the row requires; `Command` = the
invocation quoted.

**kama.** One prose line plus a small table row: byte-identity of the L0 line against the pinned blob, the bar
re-test, and the drift probes — all L1-FILL(R-STAND-KAMA). State explicitly that kama is **not re-flagged**; the
byte-identity test is what distinguishes unanswered from new. If a lane was minted mid-wave, its own `kama`-class entry
is a separate row and is **not** covered by the carried L0 line — say which line belongs to which (R-STAND-KAMA).

### Owed from refresh 7 (do not let it age)

One bullet per carried obligation, each with the revision it was re-tested at and the cell that decides it:
L1-FILL(R-OWED). A carried obligation that is still open is reported open, not quietly dropped.

## Sweep + queue movement

| Sweep target | Count | What was enumerated | Command |
|---|---|---|---|

**Cells:** rows = window reports landed, markers, reports missing the `SHONEN` heading, untracked prompts, untracked
reports at contract paths, untracked driver-state paths (including the mission/round state and dispatch prompt of any
lane minted mid-wave), the main-repo untracked-path count, the declared roster, `rounds` entries, stale `rounds` rows,
queue key census, and the falsifier check; the
counts = L1-FILL(R-SWEEP-WINDOW), L1-FILL(R-SWEEP-MANIFEST), L1-FILL(R-SWEEP-QUEUE), L1-FILL(R-SWEEP-FALSIFIER) as the
row requires; `Command` = the invocation quoted. The roster and the `rounds` length are read at a named time: a
mid-wave mint appends to both.

Then bullets for queue movement: rows that moved status, rows newly opened, rows closed, and any re-test condition that
fired — each with its key and its evidence pointer.

## Self-defects filed

| # | Defect | Evidence |
|---|---|---|

**Cells:** one row per defect filed against this lane this refresh; `#` = L1-FILL(R-SELF-DEFECTS) (numbering continues
the ledger's series); `Evidence` = file:line or a quoted command and output. Also state where the refresh-7 record was
corrected and whether any earlier defect closed. A **cross-lane attribution incident** (a sibling having committed this
lane's in-flight wave files) is reported here with the offending commit and the affected file list, and routed — see
`## Mid-round scope change`; defects a sibling caused are not absorbed as this lane's own.

## Contested scope

| Item | Owner pair | Ruling (or open) | Deadline / trigger | Evidence |
|---|---|---|---|---|

**Cells:** one row per standing contested item plus any new one the window surfaced; every measurement column =
L1-FILL(R-CONTESTED). Items this lane cannot rule are published with the owner who owes the ruling — never resolved
here.

## L0 surfacing

Purpose: every entry in `.ufo/l0-questions.md`, classified, with the operator-answer count stated as a measurement.

| Filed by | Question (opening words) | Classification | Evidence |
|---|---|---|---|

**Cells:** one row per entry (cited by lane + round + opening words, never by line number); `Classification` =
L1-FILL(R-L0); the operator-answer count, the blob forensics, and the line(s) appended this round are also
L1-FILL(R-L0). Classifications reuse the established vocabulary (answered by ruling / superseded / blocked-external /
open, operator-only) so a re-reader can compare refreshes.

## Dispatch digest — every L2 seat and its deliverable

Purpose: name every seat and the file it produced, so a non-author can reach the evidence rather than this lane's
summary of it.

| Seat | Role (route bucket) | Deliverable path | Outcome |
|---|---|---|---|

**Cells:** rows = every dispatched seat (L1-FILL(R-DISPATCH-PATHS) for the paths; the seat count against `MISSION.md`'s
L2 floor is L1-FILL(R-DISPATCH-SEATS)); `Outcome` = the one-line result and its evidence file; seats still live at
composition are L1-FILL(R-DISPATCH-LIVE) and must be reported as still live rather than as complete. If a seat's
deliverable did not land, write that — an unlanded seat is a result.

Seats observed in this seat's roster at composition (the L1 replaces this list with its own dispatch record): LabratProbes
(`labrat`), ScoutGateMovement (`scout`), ScoutSweepWindow (`scout`), ExecVerdictLessons (`executor`), ExecR4Adjudicator
(`executor`), SentinelScope (`sentinel`), DistillerQueue (`distiller`), RevengerRule4Intent (`revenger`),
ReviewerCitations (`reviewer`), ConnectorOverlap (`connector`), ScribeSkeletons (`scribe`). Deliverables landed in
`.ufo/waves/round-10/seats/` at composition: `distiller-queue.md`, `revenger-rule4-intent.md`,
`reviewer-citations.md`, `sentinel.md` — the path convention is `.ufo/waves/round-10/seats/<seat-file>.md`.

## SHONEN

Purpose: the contract item (`PROTOCOL.md` report contract). The main repo carries no `SHONEN.md` — fleet-meta has no
minted shonen and the aggregator lane is a role — so this section carries the interpreted form this lane has used since
round 4 plus the fleet-wide assessment it owes: one line per box per subject, the verifier id each mark needs, and the
canonical-form census.

| Subject | Box 1 | Box 2 | Box 3 | Box 4 | Ruling | Evidence pointer |
|---|---|---|---|---|---|---|

**Cells:** one row per subject in the stated roster scope (this lane, under the interpreted form, plus every child
shokunin, including any lane whose mint landed while the wave ran — a freshly minted lane's `SHONEN.md` is untested and
that is the finding); all box columns and `Ruling` = L1-FILL(R-SHONEN-BOXES); `Evidence pointer` = a resolvable file
pointer, not a paraphrase. One prose line states the non-author rule applied: a subagent this lane dispatched is still
this lane, so its seats are not non-author verifiers.

| Repo | Marks per box | Evidence lines per box | `<verifier-id>` named | Canonical form |
|---|---|---|---|---|

**Cells:** one row per repo in the stated roster scope; all columns = L1-FILL(R-SHONEN-FORM). The `<verifier-id>` column
is the one a promotion review reads — a `[x]` carrying no named non-author verifier is author attestation and counts as
`[~]`.

## Push-scope compliance

| Surface | Action | Scope ruling | Evidence |
|---|---|---|---|

**Cells:** rows = the main-repo push (range and result = L1-FILL(R-PUSH)), the child-repo commits this lane made and
their pushed state (L1-FILL(R-PUSH)), the write-scope audit of allowed versus forbidden paths
(L1-FILL(R-WRITESCOPE)), the authorship of each file in this lane's wave directory (L1-FILL(R-WAVE-OWNERSHIP) — this
lane's evidence, whoever committed it), and the main-repo tracking state of a lane directory added mid-wave
(L1-FILL(R-SCOPE-CHANGE)); `Scope ruling` = the clause quoted (`MISSION.md` push scope; `PROTOCOL.md` invariants). The
report states plainly which commits were pushed, which were committed-not-pushed by ruling, which forbidden paths were
never touched, and which paths a sibling's commit touched on this lane's behalf.

## Mid-round scope change

Purpose: the facts that moved the round's ground while the wave ran — a roster mint, a sibling committing this
lane's in-flight wave files, a sibling claim about a prior wave that is testable, and the read-time state of the paths
those touch. Fold them in; the ledger's `§15.22` carries the same rows.

| Change | Measured fact | Command | Read time | Tables rescoped |
|---|---|---|---|---|

**Cells:** rows = the scope changes observed (replace with the L1's own list); `Measured fact` = L1-FILL(R-KAMA-MINT),
L1-FILL(R-WAVE-OWNERSHIP), L1-FILL(R-SIBLING-CLAIM), L1-FILL(R-SCOPE-CHANGE) as the row requires; `Read time` = the
stamp form used in `## Method`. One line states the roster scope each affected table now grades
(L1-FILL(R-ROSTER-SCOPE)), and one line states whether the sibling's claim about the prior wave holds — decided by the
two commands, never repeated from the commit message.

## Next (round 11, falsifiable)

Purpose: the hand-off. Name the move, its parts, the artifact each part lands, and the falsifiers — written so a
re-reader can decide each one yes/no from a named cell.

- **Move:** L1-FILL(R-NEXT) — the axis and the improvement, with the debt it pays.
- **Roster scope carried forward:** the next round's tables state the roster they grade, which now includes the lane
  minted during this wave (L1-FILL(R-ROSTER-SCOPE)); a table that silently returns to the older roster is a defect.
- **Parts:** bullets, one per part, each naming its artifact path.
- **Falsifiers:** bullets, one per falsifier (L1-FILL(R-FALSIFIERS)), each naming the cell that decides it.
- **Zero-remain proof:** the `grep -c 'L1-FILL'` pair for the ledger skeleton and for this report's own fill pass,
  before → after (L1-FILL(R-ZERO-FILL)).