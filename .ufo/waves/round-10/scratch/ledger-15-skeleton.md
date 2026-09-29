# Ledger §15 skeleton — Refresh 8 / round-10 aggregator audit (structure only; no measurements)

**Author:** `scribe` seat (round-10 wave). **Status:** skeleton. The aggregator L1 fills every `L1-FILL(<id>)` cell and
lands this as the `## 15.` section of `shokunin:.ufo/reports/AGGREGATE.md`, appended after §14.
**Model of shape:** `shokunin:.ufo/reports/AGGREGATE.md` §14 (read, not copied) — §14.1 method · §14.2 verdicts ·
§14.3–§14.8 rule/protocol analysis · §14.9 standing tables · §14.10 sweep + queue · §14.11 correction of the previous
record · §14.12 self-defects · §14.13 L0 surfacing · §14.14 re-run commands · §14.15 residuals + proposals · §14.16
routed rows · §14.17 post-mirror re-run · §14.18 addendum.
**Round-10 facts the section must serve:** `shokunin:.ufo/waves/round-10/CONTEXT.md` (host facts, seat write scope,
gate usage, exit map, declared not-evaluated checks); parts A/B/C and the falsifiers: `shokunin:SCORECARD.md`
§Planned (round 10 entry).

## Conventions for this file

- **Path convention** (D-128 forward fix, so a sibling's citation gate can resolve every pointer): bare paths are
  main-repo-relative; a main-repo path may also be written `shokunin:<path>`; a child-repo path is always written
  `<repo-dir>-shokunin:<path>`.
- **Numeric policy.** No digit in this file is a claim. Every revision, hash, count, tally, exit code, age or verdict
  that carries a number is an `L1-FILL(<id>)` cell. Digits survive only as identifiers: section refs (`§14.2`, `§15.7`),
  round tags (`round-9`, `round-10`), defect keys (`D-127`), proposals (`P-v`), rule tags (`r4`, `r10`, `box-3`),
  seat/lane names, and paths.
- **Tables.** Every content table below is header-only, by design — the L1 writes the data rows. The `**Cells:**` line
  under each table names the `L1-FILL` id that owns each column and states the row axis, so no cell is ambiguous. The
  single exception is the index table immediately below, whose rows are `L1-FILL` ids (identifiers), not data.
- **Angle-bracket tokens** inside command columns are usage metavariables, written the way
  `shokunin:.ufo/waves/round-10/CONTEXT.md` writes them (`--snapshot <repo-dir> <commit>`). They are not placeholders:
  the L1 substitutes the value its own command produced.
- **Roster scope.** Where a row axis says "per child repo", it means the roster scope stated in §15.22: the repos
  rostered at the round-10 cutoff (`shokunin:.ufo/waves/round-10/CONTEXT.md`) plus any lane minted while the wave ran.
  A table grading a different set says so in its own Cells line. Never write "all repos" without naming the roster.
- **Attribution.** A file under this lane's wave directory is this lane's evidence even when another author committed
  it; record the committing author per wave file (§15.22), and cite the two commands that decide any published claim
  about who wrote what.
- **Proof that none remain:** run `grep -c 'L1-FILL' <this file>` before filling and after; the before and after counts
  are the zero-remain evidence the round-10 report quotes in its `## Next` section.

## L1-FILL index — every id used in this file

| id | surface | what the L1 measures | command to run |
|---|---|---|---|
| L-STAMP-MAIN | §15 stamp, §15.1 | main-repo HEAD, and the clock time of each reading | `date -u +%Y-%m-%dT%H:%M:%SZ; git rev-parse --short HEAD` |
| L-STAMP-CHILD | §15.1, §15.22 | live HEAD and dirty-file count per repo in the stated roster scope, per reading — the loop names the cutoff roster plus `kama`, the lane minted mid-wave | `for d in kasegi kengaku kake kumitate kotoba kagi kama; do printf '%s %s dirty=%s\n' $d "$(git -C $d-shokunin rev-parse --short HEAD)" "$(git -C $d-shokunin status --porcelain \| wc -l)"; done` |
| L-ROSTER-SCOPE | §15.1, §15.22 | the roster each table grades: the roster as declared in `MANIFEST.json` at read time, versus the cutoff roster this audit's baseline used | `python3 -c "import json;print(json.load(open('MANIFEST.json')).get('roster'))"; git log --format='%h %aI %an %s' -2 -- MANIFEST.json` |
| L-KAMA-MINT | §15.22 | a lane minted mid-wave: its mint commit and author, its HEAD and dirty count, its tracked-file count, its gate run (exit, findings, provisional flag), and whether its corpus is tracked at that HEAD (re-derivability) | `git log --format='%h %aI %an %s' -1 -- kama-shokunin; git -C kama-shokunin rev-parse --short HEAD; git -C kama-shokunin status --porcelain \| wc -l; git ls-files kama-shokunin \| wc -l; node .ufo/waves/round-9/corpus-gate.mjs --repo kama-shokunin --round 10; echo exit=$?; git -C kama-shokunin ls-files corpus/ \| wc -l` |
| L-WAVE-OWNERSHIP | §15.22 | per file under this lane's wave directory: the commit and author that added it — the check for a sibling having committed this lane's in-flight evidence | `git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-10/CONTEXT.md; git log --diff-filter=A --format='%h %an' --name-only -- .ufo/waves/round-10/` |
| L-SIBLING-CLAIM | §15.22 | whether a sibling's published claim that a previous wave was uncommitted is true, decided by the two commands below | `git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-9/corpus-gate.mjs; git ls-tree -r <cutoff-rev> --name-only .ufo/waves/round-9 \| wc -l` |
| L-ANCESTRY | §15.1, §15.5 | whether each before-revision is a commit and an ancestor of HEAD, and its distance from HEAD | `git -C <repo-dir>-shokunin cat-file -e <rev>^{commit}; git -C <repo-dir>-shokunin merge-base --is-ancestor <rev> HEAD; echo exit=$?; git -C <repo-dir>-shokunin rev-list --count <rev>..HEAD` |
| L-GATE-SHA | §15.1 | sha256 of the gate script and of its expected-values file | `sha256sum .ufo/waves/round-9/corpus-gate.mjs .ufo/waves/round-9/corpus-gate.expected.json` |
| L-GATE-SELFTEST | §15.1, §15.7 | self-test tally and exit code (capability evidence) | `node .ufo/waves/round-9/corpus-gate.mjs --selftest; echo exit=$?` |
| L-GATE-REGISTRY | §15.2, §15.6 | the gate's own registry: verdict map, implemented checks, declared not-evaluated checks with reasons | `node .ufo/waves/round-9/corpus-gate.mjs --registry` |
| L-A-HOME | §15.2 | the location a legal registry home would be, or the sweep that proves none exists | `ls SKILL.md 2>&1; ls .ufo/waves/round-10/; grep -n 'registry' PROTOCOL.md` |
| L-A-AUTHORITY | §15.2 | the authority text the home decision rests on (a protocol ruling, or the clause as written) | `grep -n -B2 -A30 'Gate standard' PROTOCOL.md` |
| L-A-ROW | §15.2 | the row's fields per the registry clause (each required field a column) | same clause text; field names read from it verbatim |
| L-A-CALL | §15.2 | the call itself: row landed **or** reasoned rejection — and the conformant-vs-unregistrable check | derived from L-A-HOME + L-A-ROW; the round-10 falsifier text is in `shokunin:.ufo/waves/round-10/CONTEXT.md` |
| L-B-R4-TOTAL | §15.3 | `r4` findings before and after the declared classes are closed | `node .ufo/waves/round-9/corpus-gate.mjs --all \| grep -c '(r4)'` |
| L-B-R4-CLASSES | §15.3 | findings per declared false-positive class, before → after | `grep -n 'declared\|not-evaluated\|FP' .ufo/waves/round-9/corpus-gate.mjs` + the adjudicating seat's class table |
| L-B-R4-COLLISION | §15.3 | the rule-4/rule-9 collision (`D-141`) sub-count inside the class set | derived from L-B-R4-CLASSES |
| L-B-R4-KEPT | §15.3 | the residue defensible as violations once the classes close | derived from L-B-R4-CLASSES |
| L-B-R4-DISPOSITION | §15.3 | per class: kept / reclassified / withdrawn / could-not-evaluate, with the by-construction argument | `shokunin:.ufo/waves/round-10/seats/revenger-rule4-intent.md` (seat evidence) |
| L-C-REV-BEFORE | §15.4 | the revision each repo was graded at in refresh 7 (before state) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 9` |
| L-C-REV-AFTER | §15.4 | each lane's next landed revision (after state), with its timestamp and subject | `git -C <repo-dir>-shokunin log -1 --format='%h %aI %s'` |
| L-C-PERRULE | §15.4 | per-rule finding count at the before revision and at the after revision | the gate at both revisions; per-repo `# summary` lines + the finding-id tally |
| L-C-MOVEMENT | §15.4 | movement direction per rule per repo: cleared / added / unchanged / contested | derived from L-C-PERRULE |
| L-GATE-ROUNDSEL | §15.4 | the `--round 9` versus `--round 10` fleet tallies | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 9; node .ufo/waves/round-9/corpus-gate.mjs --all --round 10` |
| L-GATE-ALL | §15.4, §15.20 | per-repo `# summary` lines (revision, dirty, exit, findings, rules) and the fleet exit code | `node .ufo/waves/round-9/corpus-gate.mjs --all; echo exit=$?` |
| L-GATE-FINDINGS | §15.20 | the finding-id tally per rule across the fleet (the before/after totals the post-mirror table compares) | `node .ufo/waves/round-9/corpus-gate.mjs --all \| grep -oE '^CR-[a-z]+-shokunin-(r[0-9]+\|shonen)' \| awk -F- '{print $NF}' \| sort \| uniq -c` |
| L-VERDICT | §15.5 | per repo: measured revision, verdict, failed rules, movement, seat evidence | the gate at the measured revision + the round-10 per-repo verdict seat files under `.ufo/waves/round-10/seats/` |
| L-VERDICT-TALLY | §15.5 | the tally over the verdict set, and which rule fails fleet-wide | derived from L-VERDICT |
| L-RULE8 | §15.6 | rule-8 literal occurrences per repo at its revision, with hit-file authorship | the `op://` scanner in `shokunin:.ufo/waves/round-9/l1-baseline.md` §1 |
| L-RULE7 | §15.6 | rule 7 on both readings: phantom rows (gate `r7`) and under-coverage | gate `r7` findings + index-row versus tracked-file counts |
| L-SHONEN-CENSUS | §15.6 | `SHONEN.md` canonical-form census: marks per box, evidence lines per box, deviations, verifier-id presence | the checker in `shokunin:.ufo/waves/round-9/l1-baseline.md` §2 + the gate's `shonen` findings |
| L-GATESTD | §15.6 | §Gate standard adoption census, one column per clause, one row per sibling verdict tool | the round-10 connector seat file under `.ufo/waves/round-10/seats/` + per-repo `SKILL.md` registry rows |
| L-BOX3 | §15.10 | box-3 currency re-run at each lane's landed revision | the per-repo gate commands named in that lane's own report |
| L-GATE-SNAPSHOT | §15.7 | each pinned revision's frozen run and its MATCH/MISMATCH verdict, plus the exit code | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <repo-dir>-shokunin <commit>; echo exit=$?` |
| L-STANDING-DORMANCY | §15.8 | per lane: counter, last dispatch, last landed report, last `LOG.md` round entry, last commit age, dormancy verdict | bounded `LOG.md` token scan (the §12.1 correction-3 bound) + `.ufo/watchdog.log` scan |
| L-STANDING-MINT | §15.8 | per candidate: demand instances, owning-province test, bar verdict, status, re-run pointer | `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` + the window sweep |
| L-STANDING-MARKS | §15.8 | marker grading of the window's reports; mints executed over the `rounds` entries | `python3 -c "import json;print([r.get('minted') for r in json.load(open('MANIFEST.json'))['rounds']])"` |
| L-KAMA-BYTES | §15.9 | byte-identity of the kama L0 line against the pinned blob | `git show <pin>:.ufo/l0-questions.md \| md5sum; md5sum .ufo/l0-questions.md` |
| L-KAMA-BAR | §15.9 | whether the kama demand instances still resolve, and the owning-province test | `git -C <repo-dir>-shokunin merge-base --is-ancestor <h> HEAD; echo exit=$?; grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` |
| L-KAMA-DRIFT | §15.9 | the endpoint-drift probes re-run, GET only, plus the config lines that still pin the stale base URL | the probe block in `shokunin:.ufo/reports/AGGREGATE.md` §12.2, re-executed read-only |
| L-SWEEP-REPORTS | §15.11 | window: reports landed, markers, reports missing the `SHONEN` heading, untracked prompts and reports | `git ls-files -o --exclude-standard .ufo/prompts .ufo/reports` + the heading grep (`^#{1,6} *SHONEN`) |
| L-SWEEP-MANIFEST | §15.11 | `rounds` entries, last-wins status tally, rows stale at read time | the last-wins script committed in `shokunin:.ufo/waves/round-9/seats/sweep-window.md` §2.2 |
| L-SWEEP-QUEUE | §15.11 | queue keys: definition rows, distinct keys, max key, next free, collisions, folds, open rows by owner | `python3 -c "import re;t=open('.ufo/reports/AGGREGATE.md').read();r=re.findall(r'^\| (D-\d+)',t,re.M);print('rows',len(r),'distinct',len(set(r)),'max',max(r,key=lambda x:int(x[2:])))"` |
| L-FALSIFIER | §15.11 | whether refresh 7's own written falsifier triggered, with the consuming evidence | the falsifier text in `shokunin:.ufo/reports/round-9/aggregator.md` §Next + the lanes' citations of the refresh-7 verdicts |
| L-CORRECT-CELLS | §15.12 | non-author re-execution of §14's published cells: pass / stale / fail | `shokunin:.ufo/waves/round-10/seats/reviewer-citations.md` (seat) + the L1's own re-runs |
| L-CORRECT-X | §15.12 | per corrected cell: published value, re-executed value, cause | derived from L-CORRECT-CELLS |
| L-SELFDEFECTS | §15.13 | the self-defect rows filed at refresh 8, numbering continuing §14.12 | the §15.13 table itself |
| L-CONTESTED | §15.14 | per standing contested-scope item: owner pair, ruling, deadline, evidence | `grep -n 'contested' .ufo/reports/AGGREGATE.md SCORECARD.md` + the integrator's recorded ruling |
| L-L0-BLOBS | §15.15 | blob forensics over `.ufo/l0-questions.md`: blob list, sha256, clean-versus-HEAD | `git log --format='%h' -- .ufo/l0-questions.md; sha256sum .ufo/l0-questions.md; git status --porcelain .ufo/l0-questions.md` |
| L-L0-ROWS | §15.15 | per entry: lane, round, opening words, classification at this refresh; operator answers | the classification table in §15.15 |
| L-L0-APPEND | §15.15 | the line(s) appended this round, and the pre-append clean check | `git diff --numstat .ufo/l0-questions.md` |
| L-MIRROR-COMMITS | §15.16 | the child-repo lesson commits and the single-file verification of each | `git -C <repo-dir>-shokunin show --stat HEAD` |
| L-MIRROR-CITES | §15.16 | unqualified cross-repo citations in the lesson drafts, before → after the path-convention line | the citation scanner in `shokunin:.ufo/waves/round-9/l1-baseline.md` |
| L-DURABLE | §15.16, §15.18 | round-10 wave artifacts committed, with nothing left untracked at the wave paths | `git ls-files .ufo/waves/round-10/ \| wc -l; git ls-files -o --exclude-standard .ufo/waves/round-10/` |
| L-POSTMIRROR | §15.20 | the gate re-run after the mirror: per-repo summaries, and whether `r10` cleared | `node .ufo/waves/round-9/corpus-gate.mjs --all` after the child commits |
| L-ROUTED-KEYS | §15.19 | routed rows added: key, owner, severity, defect, evidence — plus the collision check | the key script committed in `shokunin:.ufo/waves/round-9/seats/distiller-queue.md`-class seat + `shokunin:.ufo/waves/round-10/seats/distiller-queue.md` |
| L-PROPOSALS | §15.18 | proposals routed: id, target file, clause, status | derived from the proposals this round produced |
| L-ADDENDUM | §15.21 | rows filed while composing the report, after the main commit | `ls -l .ufo/waves/round-10/seats/; stat -c '%y %n' .ufo/waves/round-10/seats/*` |
| L-SCOPE-CHANGE | §15.22 | facts that changed the round's scope while the wave ran: the roster, the wave-file authorship, the sibling claim re-tested, and the read-time state of the untracked paths | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"; git status --porcelain \| grep -c '^??'` |

---

## 15. Refresh 8 — round-10 aggregator audit (registry home, r4 adjudication, per-rule movement)

Paste everything from this heading down. The L1 writes the stamp paragraph (readings, wave shape, the seats dispatched
and their deliverable paths) as prose, then fills the tables in order.

### 15.1 Method — every cell names its revision (P-s held), and parts A/B/C are stated as falsifiable claims

Purpose: §14.1 demoted the single cutoff stamp to a *reading time* and made the revision the identity of an audit cell.
This refresh inherits that rule unchanged; the child repos move while the fleet runs, so a cell that does not name its
revision is not comparable to the one it is compared against.

Restate the round's parts (A/B/C) and their falsifiers in this lane's own words (from
`shokunin:.ufo/waves/round-10/CONTEXT.md`): **A** a legal registry home for `corpus-gate.mjs` or a reasoned rejection;
**B** the `r4` heuristic's declared false-positive classes closed until the count is defensible as violations;
**C** the gate re-run at each lane's next landed revision, movement reported per rule. The falsifiers are named in the
same place and must be answered as yes/no in §15.18.

**Roster scope.** State here which repo set this section's tables grade, and say it once: the roster at the round-10
cutoff, plus any lane minted while the wave ran (§15.22). The declared roster at read time and the cutoff roster are
both measured (L1-FILL(L-ROSTER-SCOPE)); a table whose scope differs says so in its own Cells line.

**Reading stamps.** One row per reading. The table exists because §14.1's rule makes the reading time part of the cell.

| Reading | Time (UTC) | Main-repo HEAD | Per-repo HEAD and dirty count | What was read at this stamp |
|---|---|---|---|---|

**Cells:** rows = one per reading the L1 actually made (prose row axis, no id); `Time` and `Main-repo HEAD` =
L1-FILL(L-STAMP-MAIN); `Per-child HEAD and dirty count` = L1-FILL(L-STAMP-CHILD); `What was read` = prose the L1
writes (which sections/tables were read at that stamp).

**Gate identity.** The gate is fixed input this refresh; its hash is what makes "the same gate produced both runs"
checkable.

| Artifact | sha256 | Self-test tally | Self-test exit | Declared not-evaluated checks |
|---|---|---|---|---|

**Cells:** rows = the gate script and its expected-values file; `sha256` = L1-FILL(L-GATE-SHA); `Self-test tally` and
`Self-test exit` = L1-FILL(L-GATE-SELFTEST); `Declared not-evaluated checks` = L1-FILL(L-GATE-REGISTRY).

**Before-state ancestry.** Required whenever a before/after pair is asserted: the before revision must be a commit and
an ancestor of what the after run graded, or the movement claim is vacuous.

| Repo | Before revision | Live HEAD | Distance (commits) | Ancestor? (exit) |
|---|---|---|---|---|

**Cells:** one row per child repo; `Before revision`, `Live HEAD`, `Distance (commits)`, `Ancestor? (exit)` =
L1-FILL(L-ANCESTRY); the before revisions are also L1-FILL(L-C-REV-BEFORE).

### 15.2 Part A — `corpus-gate.mjs` registry home: the row, or the reasoned rejection (`D-127` / `P-v`)

Purpose: `PROTOCOL.md` §Gate standard places registry rows in each lane's `SKILL.md`; the main repo has none, so the
clause as written leaves a main-repo gate unregistrable. This subsection either lands the row at a home the clause (or
a ruling) allows, or records the rejection with its reason. **Falsifier:** the gate may not be called conformant while
unregistrable — the call in `L-A-CALL` must say which it is.

| Check | Finding | Authority (file:line) | Home decided | Row landed? |
|---|---|---|---|---|

**Cells:** rows = the candidate homes the sweep actually checked (main-repo root, the lane's own wave directory, an
integrator-owned registry if one exists — the L1 names what it swept); `Finding` and `Home decided` = L1-FILL(L-A-HOME);
`Authority (file:line)` = L1-FILL(L-A-AUTHORITY); `Row landed?` = L1-FILL(L-A-CALL).

**The row's fields.** One row per field the registry clause names; the field list is read from the clause, not invented.

| Field | Value | Source of the value |
|---|---|---|

**Cells:** rows = the clause's required fields (L1 reads them from L-A-AUTHORITY); `Value` and `Source` =
L1-FILL(L-A-ROW); if the call is a rejection, write the rejection's rationale in this table's `Source` column and say
so in the heading line above.

### 15.3 Part B — the `r4` heuristic's declared false-positive classes, closed

Purpose: refresh 7 declared false-positive classes for the `r4` heuristic (including the rule-4/rule-9 collision `D-141`; `CORPUS.md`
rule 4 requiring a command for every count while rule 9 requires a falsified count to be quoted inside a correction
entry). This subsection measures the classes, states each one's disposition, and reports the residue that survives as
violations. **Falsifier:** the `r4` cell may not be restated without its classes — the class table is mandatory, not
optional.

**Class census.**

| Class | Rule pair | Findings before | Findings after | Disposition | By-construction argument |
|---|---|---|---|---|---|

**Cells:** rows = the declared classes plus any class the adjudicating seat adds (name them; do not renumber
`D-141`); `Findings before` and `Findings after` = L1-FILL(L-B-R4-CLASSES); `Disposition` and `By-construction
argument` = L1-FILL(L-B-R4-DISPOSITION); the collision row's sub-count is also L1-FILL(L-B-R4-COLLISION).

**Residue.**

| Cell | Before | After | Defensible as violations | Command |
|---|---|---|---|---|

**Cells:** rows = the `r4` total and its collision sub-count, never folded into one row; `Before` = L1-FILL(L-B-R4-TOTAL);
`After` and `Defensible as violations` = L1-FILL(L-B-R4-KEPT); `Command` = the gate invocation actually used, quoted.

### 15.4 Part C — per-rule movement at each lane's next landed revision

Purpose: the currency half of the rule-10 duty is whether a verdict names a landed revision; the movement half is
whether any rule moves between revisions. Both are reported per rule, not per repo, because a repo-level verdict hides
a rule that cleared behind one that appeared. **Falsifier:** a verdict that does not name its revision.

**Revisions.**

| Repo | Before revision (refresh 7) | After revision (next landed) | After commit timestamp | After commit subject |
|---|---|---|---|---|

**Cells:** one row per child repo; `Before revision` = L1-FILL(L-C-REV-BEFORE); `After revision`, `timestamp`,
`subject` = L1-FILL(L-C-REV-AFTER).

**Per-rule movement.**

| Repo | Rule | Before | After | Movement | Seat evidence |
|---|---|---|---|---|---|

**Cells:** rows = one per (repo × rule) pair present in either run — state the pairing rule the L1 used (union of
both runs' rule sets) so a rule that appears or disappears is not silently dropped; `Before`, `After`, `Movement` =
L1-FILL(L-C-PERRULE) and L1-FILL(L-C-MOVEMENT); `Seat evidence` = the round-10 seat file path under
`.ufo/waves/round-10/seats/`.

**Fleet totals and the round selector.**

| Selector | Exit | Findings | Rule breakdown |
|---|---|---|---|

**Cells:** rows = the live `--all` run at the after revisions and the round selector (`--round 9` versus `--round 10`)
the CONTEXT baseline was measured with; `Exit`, `Findings`, `Rule breakdown` = L1-FILL(L-GATE-ALL) and
L1-FILL(L-GATE-ROUNDSEL).

### 15.5 Round-10 corpus verdicts (`CORPUS.md` rule 10) — re-emitted at named revisions

Purpose: rule 10 requires a verdict per repo each round, and §14.1 requires the verdict to name the revision it graded.
Carry forward the critic amendment §14.2 absorbed: `could-not-evaluate` is a **cell** grade, never a repo verdict.

| Repo | Measured revision | Verdict | Failed rules | Movement versus refresh 7 | Seat evidence |
|---|---|---|---|---|---|

**Cells:** one row per repo in the stated roster scope (a lane minted mid-wave is its own row, §15.22); all measurement
columns = L1-FILL(L-VERDICT); `Seat evidence` = the round-10
per-repo verdict seat path. Beneath the table, one prose line: the tally (`L1-FILL(L-VERDICT-TALLY)`) and which rule
fails fleet-wide (refresh 7's answer was rule 8-literal; re-measure it rather than inherit it).

### 15.6 Standing rule/protocol analysis carried forward from refresh 7

Purpose: the §14 rule/protocol analyses are still live. Re-run them at this
refresh's revisions; if one did not move, say so with its command rather than dropping it.

**Rule 8 on its literal text.** Refresh 7 graded every child corpus FAIL-literal and found the literal hits mostly in this
lane's own mirrored lessons (`CORPUS.md` says "including this one's examples"). Re-measure; if the fix is forward-only,
the count moves only where a lesson landed.

| Repo | Revision | corpus files | lines | occurrences (unit) | files with hits | hit-file owner |
|---|---|---|---|---|---|---|

**Cells:** one row per child repo; the counts = L1-FILL(L-RULE8). The **unit** is a column, not prose — refresh 7's
`P-u` lesson (lines versus occurrences versus files produced several "correct" answers inside one wave).

**Rule 7, both readings.**

| Reading | Repo | Count | What it measures | Command |
|---|---|---|---|---|

**Cells:** rows = one per (reading × repo); the readings are the literal one (gate `r7`: an index row naming an absent
file) and the interpretation one (indexed paths versus tracked corpus files). All three measurement columns =
L1-FILL(L-RULE7). Name the reading in the row, since refresh 7's `D-142` shows they disagree.

**`SHONEN.md` canonical-form census.**

| Repo | Marks per box | Evidence lines per box | Deviations | Verifier-id present? | Canonical? |
|---|---|---|---|---|---|

**Cells:** one row per child repo; all columns = L1-FILL(L-SHONEN-CENSUS). The verifier-id column is the one a
promotion review reads: a mark without one is author attestation.

**§Gate standard adoption census.**

| Tool | Lane | Verdict map | Self-test asserts exit and finding-id | Committed pinned values | Frozen run over a snapshot | Registry row complete | Classification |
|---|---|---|---|---|---|---|---|

**Cells:** one row per sibling verdict tool; all columns = L1-FILL(L-GATESTD). Classification vocabulary is the one
the clause uses (gate / probe), so a re-reader can check the row against the clause text.

### 15.7 Frozen snapshots re-run — the gate's own regression evidence

Purpose: a gate that only runs over a live worktree is not re-runnable evidence (§14.8's two-evidences clause).
Each pinned revision gets its own run and its own verdict; the snapshot set is the one named in
`shokunin:.ufo/waves/round-9/CONTEXT.md`'s frozen keys plus any revision this round pinned.

| Pinned revision | Repo | Exit | Frozen verdict | Live-head relationship |
|---|---|---|---|---|

**Cells:** one row per pinned (repo × revision) pair; `Exit`, `Frozen verdict`, `Live-head relationship` =
L1-FILL(L-GATE-SNAPSHOT). A repo whose corpus is untracked at the graded revision has **no** re-runnable snapshot: write
`could-not-evaluate` and the reason (which repo, and why) rather than a verdict — the same discipline §15.22 applies to
a freshly minted lane. The self-test tally belongs to this subsection too: L1-FILL(L-GATE-SELFTEST) — capability
(exit code and ordered finding-ids) and the measurement run are distinct evidences, never one.

### 15.8 Standing tables re-run — rows are claims stamped to a revision

Purpose: the standing duty. Every rostered lance row and every mint/watchlist row is re-run against the live tree, and
each row's cell carries its revision. Refresh 7's result (every row moved inside the hour) is the reason this is a duty
and not a table.

**Dormancy.** One row per rostered lane; the rule is `PROTOCOL.md`'s dormancy rule, quoted verbatim in §12.1 rather
than paraphrased.

| Lane | Counter | Last dispatched | Last report landed (marker grading) | Last `LOG.md` round entry | Last commit age | Dormancy verdict |
|---|---|---|---|---|---|---|

**Cells:** one row per lane in the stated roster scope (including this lane and any lane minted mid-wave — a new lane's
dormancy row is normally "not yet dispatched twice", which is a result, not an omission); all measurement columns =
L1-FILL(L-STANDING-DORMANCY).
State the marker-grading rule applied (a report with no lane work is a marker with a failed grade; a short report
naming a real commit is `ok` with a minimum-content defect).

**Mint / watchlist.** One row per candidate; the bar is the protocol's own wording, quoted.

| Candidate | Demand instances (dated pointers) | Owning-province test | Bar verdict | Status | Re-run pointer |
|---|---|---|---|---|---|

**Cells:** one row per candidate carried in §12.2 plus any candidate this window surfaced; all measurement columns =
L1-FILL(L-STANDING-MINT). A re-test that fired must say so explicitly, as §12.3 began doing.

**Marker ledger and mints executed.**

| Measure | Value | Command |
|---|---|---|

**Cells:** rows = mints executed over the `rounds` entries, and the marker grading of this window's reports;
`Value` = L1-FILL(L-STANDING-MARKS); `Command` = the invocation quoted.

### 15.9 kama byte-identity and its bar re-test

Purpose: kama is `blocked-external`; the byte-identity test is what distinguishes "still unanswered" from "new". Never
re-flag it as new. Re-run the test, the bar test, and the drift probes.

| Check | Value | Command | Reading |
|---|---|---|---|

**Cells:** rows = the L0 line's byte-identity (L1-FILL(L-KAMA-BYTES)), the demand-instance ancestry plus
owning-province test (L1-FILL(L-KAMA-BAR)), and the endpoint-drift probes (L1-FILL(L-KAMA-DRIFT)). One prose line states
whether the L0 line is still byte-identical to the pinned blob, which is the only honest basis for "not an answer".

### 15.10 Box-3 currency re-run at the lanes' landed revisions

Purpose: §14.6 re-ran three provisional box-3 verdicts and one broke. This subsection is the recurring half of that
duty: re-run the whole box-3 set at the lanes' landed revisions, and re-test the specific mark a sibling's own gates
contradict.

| Repo | Prior grade | Re-run at revision | Result | Decisive evidence (command and output tail) |
|---|---|---|---|---|

**Cells:** one row per repo; all measurement columns = L1-FILL(L-BOX3). `stays provisional` is a legal third outcome
when the decisive text is worktree-only or untracked at the landed revision (§14.6's critic amendment A3).

### 15.11 Corpus sweep + queue movement since the refresh-7 cutoff

Purpose: the sweep proves the window was enumerated, not sampled. Every absence claim in the report carries this sweep.

| Sweep target | Count | What was enumerated (not sampled) | Command |
|---|---|---|---|

**Cells:** rows = reports landed in the window, markers, reports missing the `SHONEN` heading, untracked prompts,
untracked reports at contract paths, untracked driver-state paths (`.ufo/state/**`, and the dispatch prompt of any lane
minted mid-wave), the main-repo untracked-path count, the declared **roster** and the `MANIFEST.json` `rounds` entries
(both are read at a named time, because a mid-wave mint appends to each), stale rows, queue key counts, collisions and
folds;
the counts = L1-FILL(L-SWEEP-REPORTS), L1-FILL(L-SWEEP-MANIFEST), L1-FILL(L-SWEEP-QUEUE) as the row requires;
`Command` = the invocation quoted.

**Previous refresh's falsifier.**

| Falsifier (verbatim from refresh 7) | Triggered? | Consuming evidence |
|---|---|---|

**Cells:** rows = the falsifier statements refresh 7 wrote in its `§Next`; `Triggered?` and `Consuming evidence` =
L1-FILL(L-FALSIFIER). A falsifier that did not trigger is reported as *not* triggered — an unfired falsifier is a
result.

**Queue movement this window.** Bullets only: rows that moved status, rows newly opened, rows closed, and any row whose
re-test condition fired. Each bullet carries its key and its evidence pointer; the key census itself is the
L1-FILL(L-SWEEP-QUEUE) cell above.

### 15.12 The refresh-7 record corrected (non-author re-execution)

Purpose: the `P-q` duty — a non-author seat re-executes this lane's own published cells every refresh. This subsection
publishes the pass/stale/fail split and absorbs every FAIL as a correction row, in the append-only style rule 9
requires.

| Cell (ledger §14) | Published value | Re-executed value | Verdict | Cause |
|---|---|---|---|---|

**Cells:** one row per re-executed cell; all four measurement columns = L1-FILL(L-CORRECT-CELLS) and
L1-FILL(L-CORRECT-X); the seat file is `shokunin:.ufo/waves/round-10/seats/reviewer-citations.md`. Cells that pass are
as important as cells that fail: publish the split.

### 15.13 Aggregator self-defects filed at refresh 8

Purpose: §14.12's series continues. A defect in this lane's own published record is filed here, not routed away.

| # | Defect | Evidence |
|---|---|---|

**Cells:** one row per defect; `#` continues §14.12's numbering (L1-FILL(L-SELFDEFECTS) for the new range and the
cumulative count); `Evidence` = file:line, command, or output tail. If there are none, write the sentence that says so
and keep the table header — an empty defect table is a claim.

### 15.14 Contested scope — standing items and their rulings

Purpose: `PROTOCOL.md` requires contested-scope rulings to be recorded with a deadline; refresh 7's §14.15 named the
items and this lane cannot rule them. Publish the item, the owner pair, the ruling state, and who owes the ruling.

| Item | Owner pair | Ruling (or open) | Deadline / trigger | Evidence |
|---|---|---|---|---|

**Cells:** one row per standing contested item (the model-routing ownership contest and the fleet model-map pinning are
the two carried from §14.15; the L1 adds any new one the window surfaced); all four columns = L1-FILL(L-CONTESTED).

### 15.15 L0 surfacing (MISSION.md: the aggregator surfaces entries each round)

Purpose: the side channel is append-mostly and operator-answered by in-place edit. Forensics over every blob is what
makes "operator answers: none" a measurement rather than a guess. Cite entries by lane + round + opening words, never by
line number.

| Filed by | Question (opening words) | Classification at this refresh | Evidence |
|---|---|---|---|

**Cells:** one row per entry in the file; `Classification` = L1-FILL(L-L0-ROWS); the blob list, sha256 and clean check
= L1-FILL(L-L0-BLOBS); the append this round = L1-FILL(L-L0-APPEND). Classifications must be reused from §14.13's
vocabulary (answered by ruling / superseded / blocked-external / open, operator-only) so a re-reader can compare.

### 15.16 Mirror — the child-repo lesson commits, and their citation hygiene

Purpose: the lessons are how a sibling inherits this refresh's verdicts. Each is committed pathspec-limited under the
aggregator identity, verified single-file, and swept for unqualified cross-repo citations before it lands.

| Repo | Lesson file | Commit | Files changed | Unqualified citations before → after |
|---|---|---|---|---|

**Cells:** one row per repo in the stated roster scope that received a lesson (a lane minted mid-wave may legitimately
receive none before its first dispatched round — say so rather than omitting the row); `Commit`, `Files changed` =
L1-FILL(L-MIRROR-COMMITS); `Unqualified citations
before → after` = L1-FILL(L-MIRROR-CITES); the durability check for the wave as a whole = L1-FILL(L-DURABLE). The
push-scope ruling goes in prose here: this lane has no sibling remote.

### 15.17 Re-run commands (copy-paste runnable from the main repo root)

Write the blocks in the order they were run, deduplicated against §14.14 and against the index table above. Blocks
should include, at minimum: the revision stamps; the gate's registry/self-test/`--all`/`--snapshot` invocations; the
per-rule finding tally; the verdict re-run at a measured revision; the frozen-snapshot loop; the queue-key census; the
L0 byte-identity pair; and any scanner this refresh added (state where its source lives, so a non-author can re-run it
without this session). Each block is preceded by the cell it produces, as `# -> <cell id>`.

### 15.18 Residual gaps kept honest, and proposals routed

Two blocks, both mandatory:

- **Residuals** — bullets, each one a gap this refresh did not close, with its command or pointer. Include: what the
  gate still declares `not-evaluated` and why that is honest rather than a pass; any repo whose verdict rests on a
  worktree-only artifact; the dormancy rule's missing positive test case if it still has none; and this lane's own
  artifacts as a defect source (`L1-FILL(L-SELFDEFECTS)`).
- **Proposals routed** (integrator lands; this lane cannot) — one row or bullet per proposal: id, target file, clause,
  status. Carry forward the unlanded ones from refresh 7 rather than dropping them, and add any new one.

| Proposal | Target file | Clause / change | Status | Evidence |
|---|---|---|---|---|

**Cells:** one row per proposal; all columns = L1-FILL(L-PROPOSALS).

**Falsifier answer.** One line per round-10 falsifier, answered yes/no with the cell that answers it. This is the cell
a reader checks first.

### 15.19 Routed-defect rows added at refresh 8 (keys continue; no collisions)

| Key | Owner | Severity | Defect | Evidence / command |
|---|---|---|---|---|

**Cells:** one row per routed defect; `Key` continues the ledger's series without collision (checked via
L1-FILL(L-ROUTED-KEYS)); `Severity` uses the ledger's own scale; `Defect` is one sentence stating the failure, not the
symptom; `Evidence / command` = file:line or a quoted invocation. State the key census check in one line above the
table (rows, distinct, max, next free) so a reader can see the collision test ran. A **cross-lane attribution incident**
— a sibling having committed this lane's in-flight wave files (§15.22), with the offending commit and the affected file
list — is routed here rather than absorbed as this lane's own defect, unless the bytes committed were this lane's.

### 15.20 Post-mirror re-run — did the gate's own findings clear?

Purpose: the gate's teeth, demonstrated the only way that counts — a finding appears while an obligation is unmet and
disappears when the artifact lands, with no edit to the gate.

| Repo | Summary line (verbatim) | Exit | `r10` in the rule set? |
|---|---|---|---|

**Cells:** one row per child repo; all columns = L1-FILL(L-POSTMIRROR); the before/after totals come from
L1-FILL(L-GATE-FINDINGS) — the finding tally. Disclose any revision that moved underneath the run rather than
pinning the table to a revision that no longer exists.

### 15.21 Post-write addendum

Purpose: rows that become visible only *after* the commit, because a seat was still live or a sibling landed while the
report was composing. The addendum carries the late evidence with its own commit and its own seat file, and states the
blast radius the late evidence measures.

Write it last; if nothing landed late, write the sentence that says so (`L1-FILL(L-ADDENDUM)` for the seat-directory
state at composition).

### 15.22 Mid-round scope-change log — facts that moved the round's ground

Purpose: this wave ran long enough for the ground to move under it. Each entry states the fact, the command that
measured it, the read time, and which earlier table of this section it invalidates or rescopes. The entries below were
already observed before §15.1–§15.21 were written, so this log is not an addendum: it is part of the section.

| Change | Measured fact | Command | Read time | Tables rescoped |
|---|---|---|---|---|

**Cells:** rows = the scope changes actually observed (see the list below — replace with the L1's own); `Measured
fact` = L1-ROSTER-SCOPE, L1-KAMA-MINT, L1-WAVE-OWNERSHIP, L1-SIBLING-CLAIM and L1-SCOPE-CHANGE as the row requires;
`Read time` = the same stamp form as §15.1.

The changes to check, in the order they reached this lane:

- **The roster grew.** A lane was minted main-repo-side (`MANIFEST.json` `roster`, a `kama-shokunin/` directory with its
  own remote) while refresh 8 was running, so every "per child repo" table is scoped to the roster at its own read time,
  and the minted lane's verdict is its own row — with its gate exit, its finding breakdown, and one explicit line on
  whether its corpus is **tracked** at the revision graded (a verdict that cannot be re-derived from a commit is
  `provisional`, not conformant). L1-FILL(L-KAMA-MINT).
- **The new lane's directory is a nested repo in the main tree.** Test whether the main repo's ignore list covers it
  and what the main-repo file count for it is, because an untracked nested repo is invisible to every main-repo sweep in
  §15.11 and to a `git clean`-class hazard analysis. L1-FILL(L-SCOPE-CHANGE).
- **A sibling committed files of this lane's in-flight wave directory.** The wave directory is this lane's evidence; the
  author who *added* each file is a recorded fact, and a sibling's commit of this lane's files is a routed incident with
  a blast radius (which files, which commit, whether the content is this lane's own bytes). L1-FILL(L-WAVE-OWNERSHIP).
- **A sibling's published claim about a previous wave is testable.** Where a sibling's commit message asserts that a
  prior wave was never committed, decide it with the two commands rather than accepting or repeating the claim: the
  introducing commit of a file in that wave, and the tree listing of that wave at the cutoff revision.
  L1-FILL(L-SIBLING-CLAIM).

Add rows for any further change the wave produced (an axis switch, a superseded §Planned entry, a sibling gate that
moved), and route the incidents that are not this lane's to fix through §15.19.