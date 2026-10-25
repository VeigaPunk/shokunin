# Round 14 registry-home rerun — scribe (report-input evidence)

Role: `scribe` (dispatched author-lane seat, `R14HomeScribe`). This artifact is
**evidence / gate report input** for the parent's round-14 `protocol` report and
closure record. It authors no report, claims no promotion, certifies no
conformance, and asserts nothing about a command it did not run. Only this file
was written by this seat. No build, lint, test, self-test or formatter was run.
The inherited live gate crash was **not** re-run (rerun `context.md` §Contract:
treat as known failure). No commit, push, routing, script, template, runtime or
child-repo edit was made.

Baseline of record for this batch: `.ufo/waves/round-14/registry-home-rerun/before.json`
(sha256 `6f8e73ef…db8d70f`, commit `99efc52b3a6f3648f7d8e097d78460901ad3c91c`,
`protocol_registered_closure_gates=0`, `root_SKILL_exists=False`). Live `HEAD` at
scribe time was verified as `99efc52b3a6f3648f7d8e097d78460901ad3c91c`
(`git rev-parse HEAD`).

---

## 1. Canonical four-box seed — the four exact labels

Source of truth: `PROTOCOL.md:419-431`, the canonical `SHONEN.md` seed block
(verbatim, `<name>` the only substitution). The four checklist lines are
`PROTOCOL.md:425-428`; the box semantics that grade them are `PROTOCOL.md:68-73`.

Exact labels, verbatim apart from the seed's 4-space indent and its leading
`- [ ]` box:

1. `SKILL.md contains real decision tables, error patterns, checklists, cited sources`
2. `At least one end-to-end domain task executed and logged in LOG.md`
3. `Instructions executable by an agent without oral context`
4. `No cross-domain bleed (PROVINCE.md still accurate)`

Marks rule (`PROTOCOL.md:430-431`): `[~]` asserted by the lane itself (evidence
pointer required); `[x]` only with a named non-author verifier per
**Promotion gates** (`PROTOCOL.md:67-73`). The assessment section, when the
parent files it, belongs under a `SHONEN` heading with one line per box
(`PROTOCOL.md:143-149`, `:174-183`); a report without that heading does not
satisfy the contract.

## 2. Honest box statuses (report input, none `[x]`)

The root repo has **no** `SHONEN.md`, `SKILL.md` or `PROVINCE.md`
(`ls -a` at fleet root; also `before.json` `root_SKILL_exists=False`). No
promotion file may therefore be invented, and boxes 1/3/4 have no artifact to
grade. All nine seats of this batch are dispatched author-lane workers, so no
seat here can supply the named non-author verifier box `[x]` requires.

| # | Exact label | Status | Evidence pointer for the status |
|---|---|---|---|
| 1 | `SKILL.md contains real decision tables, error patterns, checklists, cited sources` | `[ ]` | Root `SKILL.md` absent: fleet-root `ls -a` lists `PROTOCOL.md`/`PROTOCOL-APPENDIX.md` and no `SKILL.md`; `.ufo/waves/round-14/registry-home-rerun/before.json` stdout `root_SKILL_exists=False`. `PROTOCOL.md:406-410` requires `SKILL.md` as the file carrying tables/patterns/checklists — the root has none, so the box is untouched, not asserted. |
| 2 | `At least one end-to-end domain task executed and logged in LOG.md` | `[~]` | Asserted by this lane; the round's work is executed but **not yet logged or committed**. `grep -n "round-14\|round 14" LOG.md` → no output (0 matches), and the parent owns the `LOG.md` write (rerun `context.md` §Ownership). Artifact-form evidence of the executed batch exists under `.ufo/waves/round-14/registry-home-rerun/` (e.g. `dispatch.json`, `before.json`, `critic.md`) — pointer only, not a landed-log claim. Not `[x]`: box `[x]` needs a named non-author verifier. |
| 3 | `Instructions executable by an agent without oral context` | `[ ]` | No root `SKILL.md`, so the instructions artifact this box grades is absent. `PROTOCOL.md` is contract text for the fleet, not the lane skill file; this box is untouched by the batch (`PROTOCOL.md:70-72`). |
| 4 | `No cross-domain bleed (PROVINCE.md still accurate)` | `[ ]` | Root `PROVINCE.md` absent, so its accuracy is unassessable — cannot be `[x]` and cannot be `[~]` as an accuracy claim. The only cross-domain item this seat encountered is the gate defect routed in §6, which belongs to this lane's own repo (`MANIFEST.json` + `.ufo/waves/round-15/`), not to a sibling domain. |

Ceiling, stated for the parent: registration of the gate is **not** blanket
conformance, not a live clean verdict, and not a promotion input (rerun
`context.md` §Contract; `PROTOCOL.md:382-402`, `:393-398`).

## 3. Filed marker — current identity and append-only correction constraints

Path: `.ufo/reports/round-14/protocol.md`. Live bytes verified byte-for-byte
against `HEAD`:

| Fact | Observed value | Command |
|---|---|---|
| size | `340` bytes | `wc -c .ufo/reports/round-14/protocol.md` |
| live sha256 | `d2567df3f11018ebd168918c46c7ea69119e45e41ac2f58140b1bf5634f691b4` | `sha256sum …` |
| live git blob | `7bf148bb7b502537d218625ef8746b774d622244` | `git hash-object …` |
| blob in `HEAD` | `100644 blob 7bf148bb7b502537d218625ef8746b774d622244` | `git ls-tree HEAD .ufo/reports/round-14/protocol.md` |
| worktree vs `HEAD` | empty diff | `git diff --stat HEAD -- .ufo/reports/round-14/protocol.md` |

The prefix is therefore intact and unmodified; the marker text is
`# protocol round-14 closeout (marker)` plus four prose lines, carrying no
`SHONEN` heading and 340 B < the driver's 400 B content floor (`LOG.md:692-693`,
measured driver semantics: report path + `SHONEN` heading + ≥400 bytes, no
freshness check).

Driver consequence, observed live (`.ufo/watchdog.log`, 2 occurrences):

```
2026-10-15T01:45:42-03:00 lane-round-failed protocol round=14 :: marker/contentless report; NOT advancing
2026-10-15T01:45:42-03:00 launch protocol round=14 pid=2651861
2026-10-15T01:50:57-03:00 lane-round-failed protocol round=14 :: marker/contentless report; NOT advancing
2026-10-15T01:50:57-03:00 launch protocol round=14 pid=2685253
```

(count `grep -c "lane-round-failed protocol round=14" .ufo/watchdog.log` → `2`;
also `.ufo/watchdog.log:285` `wrap protocol round=14 complete; NOT respawning
(fleet-wrap)`). This matches `PROTOCOL.md:174-183` (a contentless completion
marker closes nothing) and `:183-190` (a filed report recording no lane work is
a marker → lane-round `failed`, marker kept as a conformance defect).

**Append-only correction constraints (binding on the parent):**

- The 340 B prefix MUST remain an exact byte prefix of the file. Corrections
  land **only** as an erratum appended after the filed bytes, in a **new commit**,
  naming the text it supersedes — never a rewrite, labelled or silent
  (`PROTOCOL.md:133-136`). Append-only files take an appended correction entry
  pointing at superseded text (`PROTOCOL.md:122-124`).
- The erratum lands **after** the round's work is committed (rerun `context.md`
  §Contract). It must not be the vehicle that lands the work.
- Only a real report satisfies the path: work performed + ≥1 evidence pointer +
  changes landed and each tied to a `LOG.md` entry + a checkable commit hash +
  the `SHONEN` heading (`PROTOCOL.md:143-149`, `:174-183`). The parent's closure
  record (statuses written, or why none were writable) is required
  (`PROTOCOL.md:202-203`).

## 4. Required report sections and commit-before-report evidence

Required sections, in order, from the committed round-14 prompt
`.ufo/prompts/protocol-round-14.md` §4 (tracked blob `5a80dce65ca641b8ba4d4c700f012c3cf0bd9b7c`,
3433 B; report path named there as `.ufo/reports/round-14/protocol.md`):

1. **Work performed** — one bullet per item, each with an evidence pointer
   (path:line, command output, or commit hash).
2. **Landed changes** — every change tied to a `LOG.md` entry **and** to the
   commit hash carrying it.
3. **Before → after measurements** — one per claim, each with its counting
   command and the commit it was measured against.
4. **SHONEN** — one line per box: `[x]` only with a named non-author verifier,
   `[~]` with a resolvable pointer, `[ ]` if untouched.

This is the same contract as `PROTOCOL.md:143-149` (minimum content) and the
five child-lane prompt items `PROTOCOL.md:99-100` (report path/filename,
commit-before-report ordering, `SHONEN` heading, commit-hash citation rule, lane
write scope).

Commit-before-report evidence already established, and what is still missing:

| Item | State at scribe time | Source |
|---|---|---|
| Lane report path | `.ufo/reports/round-14/protocol.md` exists but is a marker | `PROTOCOL.md:137-139`; §3 above |
| Commit-then-push ordering | not yet performed for this round's work | prompt §5 (`.ufo/prompts/protocol-round-14.md`); `MISSION.md:74` (`Commit inside the owning repo then git push. Reports: .ufo/reports/round-<N>/<lane>.md on the main repo, commit + push.`) |
| Report cites a commit hash that is an ancestor of `HEAD` | impossible yet — no lane commit exists; `HEAD` is `99efc52b3a6f3648f7d8e097d78460901ad3c91c` | `PROTOCOL.md:116-120` (`git merge-base --is-ancestor <hash> HEAD` is the closure check) |
| Report filed before its commit | would be a conformance defect | step 1, `PROTOCOL.md:214-220` |
| Uncommitted round work in the owning repo at closure | clean cutover required. At scribe time `git status --porcelain` showed 3 modified tracked paths — `.ufo/watchdog.log` and `.ufo/l0-questions.md` (driver/operator surfaces) and `LOG.md` (a **sibling** lane's in-flight append, `aggregator` round-10 relaunch, `git diff --stat LOG.md` → `27 +++`), none of which this seat owns or touched — plus untracked wave dirs | `git status --porcelain`; `git diff --stat LOG.md` |

So the parent's order is: commit the round's lane work (which includes this
rerun directory and the integrated `PROTOCOL.md`/`SCORECARD.md` edits) → then
append the erratum after the marker bytes → then the report's cited hash
resolves as an ancestor of `HEAD`.

## 5. Known live gate crash — no closure verdict; routed owner

This is **inherited** evidence (`.ufo/waves/round-14/registry-home/live-closure.json`,
sha256 `541d08fbf1fd6e69e4292fadf8dd75eed32a8f8e9a9698cdf2b44f3766cef879`,
captured `2026-10-15T04:49:38.672179+00:00` at measured commit
`e163d15bb1b080ae567ada3b86441455e9808f9b`). It is **not** re-run here, per
rerun `context.md` §Contract.

| Fact | Value |
|---|---|
| command | `python3 .ufo/waves/round-15/closure-check.py --repo . --json --no-citations` |
| returncode | `1` |
| stdout | empty |
| classification | `unhandled-exception; no closure verdict emitted; no ledger statuses derived` |
| exception | `TypeError: '<' not supported between instances of 'NoneType' and 'int'` |
| traceback site | `.ufo/waves/round-15/closure-check.py:1143` in `do_live` → `analyze` |
| trigger corpus (inherited) | `MANIFEST.json` `rounds[138]`, `round: null`, `type: "closure"` (`.ufo/waves/round-14/registry-home/protected-before.json`) |

Static confirmation performed by this seat (read-only, grouping only, no gate
execution): line 1143 is the `for row in sorted(all_rows, key=lambda x:
(lane_sort(x["lane"]), x["round"], x["entry"])):` call, whose tuple key mixes
`x["round"]` (`None`) with `x["entry"]` (`int`) — consistent with the inherited
traceback. Independently verified live: `MANIFEST.json` `rounds` has 142 entries
and `rounds[138]` is the sole `round: null` entry.

**Report wording the parent MUST use (and MUST NOT upgrade):**

- registered; live evaluation crashed; **no closure verdict and no closure
  statuses** were derived. The gate redness (`rc=1`) is **not** an adjudicated
  `failed`/debt verdict — `PROTOCOL.md:364-368` defines the outer verdict
  interface and `PROTOCOL.md:393-398` makes gate redness status-neutral. A
  crash produces no verdict at all: `[INFERENCE]` from `PROTOCOL.md:364-368`, an
  unhandled exception is not a declared code→class mapping, so it must be
  reported as could-not-evaluate / unadjudicated rather than folded into the
  declared `1 → failed` class.
- do not call this `clean`, a debt verdict, or closure completion.

**Routed owner (one routing line owed in the parent's round notes):** `protocol`
lane — owner of `.ufo/waves/round-15/closure-check.py` (its committed gate; the
implementation defect is a self-defect of this lane's own repo) and of the
append-only `MANIFEST.json` `rounds[]` array whose malformed `rounds[138]` row
triggers it (integrator-of-record scope, `PROTOCOL.md:195-201`, `:236-237`).
Routing is integrator work that must exist in an artifact
(`PROTOCOL.md:224-228`); the aggregator mirrors the row into the owning repo's
`corpus/lessons/` and keeps it open in the ledger until the correction lands.
Within **this** move the gate must not be changed and the historical ledger must
not be altered (rerun `context.md` §Contract).

## 6. Inherited artifacts catalogued for preservation (not this batch's dispatch)

`.ufo/waves/round-14/registry-home/` is read-only inherited evidence. Its own
`dispatch.json` records the **previous** nine-seat batch; it must **not** be
counted as this batch's L2 roster (rerun `dispatch.json`
`inherited_dispatch: ".ufo/waves/round-14/registry-home/dispatch.json is
preserved but not counted as this batch."`). Catalog for preservation:

| Path (inherited, untracked) | Bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-14/registry-home/before.json` | 771 | `d2fdb423bd312b8dbdd3103ccb6032eadca71a13734e695dff0a72505899380e` |
| `.ufo/waves/round-14/registry-home/context.md` | 2802 | `5caeb97a3f90804b8d73b1c3eabb2304e480f36f26150a3ee4f306675768c5ac` |
| `.ufo/waves/round-14/registry-home/critic.md` | 9095 | `7560e3779af06de9a934fff8ad071c7d74c8ac02572818f2b58ece07de34a6b1` |
| `.ufo/waves/round-14/registry-home/dispatch.json` | 1493 | `9518ea01c9a5ce1744c08f739d9e8080b9f9e7f830816124c78b451b0b6005b1` |
| `.ufo/waves/round-14/registry-home/live-closure.json` | 1229 | `541d08fbf1fd6e69e4292fadf8dd75eed32a8f8e9a9698cdf2b44f3766cef879` |
| `.ufo/waves/round-14/registry-home/planner.md` | 9533 | `90c917e426c85dfb97c57d205ed49fdeb76298e4b30203ee85d95386a5282766` |
| `.ufo/waves/round-14/registry-home/protected-before.json` | 866 | `5c12062ef9048c41244fdf9283f6112a25063808c96d2d0a6a390bd826bf9f19` |

Preserved surfaces that must keep their recorded bytes (digests verified live by
this seat against `registry-home-rerun/before.json` `protected_sha256`):

| Surface | sha256 (verified) |
|---|---|
| `.ufo/waves/round-15/closure-check.py` | `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` |
| `.ufo/waves/round-15/frozen/r15-pre-003400/expected.json` | `19d6935b7d84e84ef3946db3d3f3537c615f122f14fbe197aad31023db2ddea9` |
| `.ufo/waves/round-15/frozen/r15-post-012710/expected.json` | `ba78759bc4652f6d73802dda10aafe04cdb48fdd351e803092fc849fda602315` |
| `.ufo/history-pin.json` | `b161cd4106c928472c1eca8395262beb7624e23349743fcd2880e2b416e7f81b` |
| `SCORECARD.md` §`## Aggregator lane` onwards | `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf` |

Qualified frozen names resolve and are digest-pinned as declared: `r15-pre-003400`
(`exit 1`, 17 pinned debt entries, 6 pinned input digests) and `r15-post-012710`
(`exit 0`, 0 debt, 6 inputs) — both under `.ufo/waves/round-15/frozen/`, which
is the same qualified form `PROTOCOL.md:385-387` requires (a bare name matching
more than one root fails closed).

This batch's own roster is `.ufo/waves/round-14/registry-home-rerun/dispatch.json`
(sha256 `a4ca52bcf1d814fa7b11fe9d40c3b5a7185f4d43df74a96d0fd30b4bf9818a9f`), one
native `functions.task` batch, nine seats (planner, connector, 3× executor,
scribe, scout, reviewer, critic), routing authority
`task.agentModelOverrides` only. All nine remain author-lane workers.

## 7. Gate / report inputs the parent still owes (uncommitted at scribe time)

This is what the scribe can see as outstanding; it is not a status verdict.

1. Round's lane work committed, then run the registered commands once
   (`--selftest`, `--frozen round-15/r15-pre-003400`,
   `--frozen round-15/r15-post-012710`) — the last of these must be reported
   with actual output, and must **not** be pre-claimed as clean.
2. `SCORECARD.md` protocol-soundness before→after row with its counting command
   and measured commit (`before.json` command is the baseline counter:
   `protocol_registered_closure_gates=0`, `root_SKILL_exists=False`).
3. `LOG.md` appended round-14 entry (currently 0 matches for round-14) tied to
   the commit that carries the work.
4. Erratum appended after the 340 B marker bytes in a new commit, naming the
   superseded marker text; marker prefix byte-identical (§3).
5. Report at `.ufo/reports/round-14/protocol.md` carrying the four sections of
   §4, the `SHONEN` heading with §2 statuses, the closure record
   (`PROTOCOL.md:202-203`), the §5 crash wording plus its one routing line, and
   a cited commit hash that satisfies
   `git merge-base --is-ancestor <hash> HEAD`.
6. `MANIFEST.json` `rounds` closure entry for round 14 (`closed_at` required if
   it carries any `not-dispatched` row), append-only, plus mirroring/routing of
   the gate defect (§5).

Also for the parent's step-1 fidelity check: the committed round-14 prompt
`.ufo/prompts/protocol-round-14.md` carries the mission/axes binding, the axis
move, the L2 floor, the report contract with all required sections, commit/push
ordering, push scope and the L0 side channel (`PROTOCOL.md:93-100`). It is the
driver's generic template text, so the **rerun** contract of
`.ufo/waves/round-14/registry-home-rerun/context.md` is the operative one for
this batch.

## 8. Out of scope / not done by this seat

- No build/lint/test/self-test/formatter invocation of any kind.
- No gate execution, and specifically no re-run of the inherited crash.
- No edit to `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `SCORECARD.md`, `LOG.md`,
  `MANIFEST.json`, `.ufo/watchdog.log`, `.ufo/history-pin.json`, `.ufo/prompts/`,
  `scripts/`, `templates/`, routing config, or any child/sibling repo.
- No edit to the filed marker or to any inherited artifact.
- No commit, push, publication, deployment, or judge/runtime invocation.
- No report authored, no promotion claimed, no worker treated as a non-author
  verifier, no `[x]` written.

Artifact path: `.ufo/waves/round-14/registry-home-rerun/scribe.md`.