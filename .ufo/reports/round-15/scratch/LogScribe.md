# LogScribe — round-15 scratch (LOG.md entry draft + placeholders)

Lane: scribe. Deliverable: the round-15 `LOG.md` bullet, house style copied from
the round-13/round-14 bullets in `LOG.md:375-501` (read first). Nothing in this
file is a repo edit; L1 integrates.

## House style extracted from the two preceding entries (checklist for whoever pastes)

- one bullet, `- 2026-09-28 — round N (**<axis> X → Y**; axis-move: …)`, 2-space
  continuation indent, ~78-col wrap, no sub-bullets, no headings inside;
- order: Dispatch → **The finding** → Landed → Evidence (shipped revision) →
  Siblings unchanged → **The L2 wave** / defects found by execution → Adjacency →
  posture;
- every number quoted is either a command ⇒ verdict pair or an explicit
  before → after; pre-move evidence sits next to the post-move verdict;
- the closing sentence is the posture sentence, verbatim across rounds.

## Pre-move facts I re-measured myself (read-only): the "at `2486643`" side

`2486643` is the round-14 commit = the round-15 pre-move HEAD.

- `awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- \[ \]'` ⇒ **16** items (8 under
  `Evidence production:` at `SKILL.md:421`, 8 under `Handler operation:` at
  `SKILL.md:431`; section spans `SKILL.md:419-448`, items span 422-447). The
  section body is byte-identical at `4b8c018` (round 13) — all 16 item line
  numbers shifted by exactly +13 when round 14 added lines above it.
- Item count over every `SKILL.md`-touching commit
  (`for c in $(git log --format=%h --reverse -- SKILL.md); do git show $c:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'; done`)
  ⇒ `55d6887:0 9b3e49f:10 06ef644:10 486f584:10 244b8c1:10 5f55ba8:10 51c9d30:12
  148ae5c:13 e64e81b:14 03477c0:14 301b9ec:14 4b8c018:16 2486643:16` — items
  entered in rounds 2, 7, 8, 9 and 13; **no revision ever held 15**. At `ea77bf0`
  (the revision `SCORECARD.md:16` was measured at) the count was **13**.
- `SCORECARD.md:16` ⇒ "a 15-item hygiene checklist" (wrong by two when written,
  stale by three now). `SCORECARD.md:40`, `:62`, `:84` ⇒ "12 checklist items
  still operator judgement" (rounds 9, 10, 11 — the checklist held 14 items at
  each, so the reading implies 2 runnable against ≥3 items that already named a
  live gate). `SCORECARD.md:209` already names "the checklist item count" as the
  round-15 falsifiable target.
- `ls corpus/checklist*` ⇒ `No such file or directory` (exit 2) — nothing in the
  repo enumerated the checklist before this round.
- Lock attribution: `git show 2486643:PROVINCE.md | sed -n '12p'` ⇒ `… — HTTP
  client, lock, session-id, THE_JANITOR_REQUEST_TIMEOUT`, `git show
  2486643:corpus/surface-census.tsv | sed -n '22p'` ⇒ `… HTTP client: lock,
  session-id, request timeout`; against `grep -nic lock
  ~/.config/the-janitor/client.py` ⇒ **0** and the real flock in
  `~/.local/bin/the-janitor` (`LOCK_FILE` L12; `exec 9>"$LOCK_FILE"` + `flock 9`
  at L130-131, L139-140, L175-176). Both are committed rows: the defect is in
  history, not only in the working tree.
- Symbols the checklist names that no gate asserted before this round: `grep -c`
  over `corpus/*.sh corpus/*.tsv` ⇒ **0** for `autoupdate`,
  `target_authority_conferred`, `40961`, `OPENCODE_SERVER_PASSWORD`; the only
  `9222` hit is `corpus/stamps.tsv:1`, a sha256 containing the digit run — a
  false positive (items 8, 11, 13, 16).
- Corpus counts at `2486643`: `grep -c '^R1' corpus/claim-ledger.tsv` ⇒ 18 rows,
  `grep -c '[^[:space:]]' corpus/stamps.tsv` ⇒ 44, `grep -c '^## Round '` ⇒ 12,
  `ls corpus/knowledge/*.md | wc -l` ⇒ 17 entries.

## Shipped-revision facts (L1's live evidence block + my read-only re-runs, 22:36-22:41)

Confirmed green and identical at the 22:41:28 revision as well
(`checklist-run.sh` 22:41:18, `checklist.tsv` 22:41:28): `CHECKLIST_RATIO:
runnable=9/16 floor=8 by_hand=7` + `CHECKLIST_RUN: CLEAN (items=16 runnable=9
by_hand=7 failed=0)` exit 0, `CHECKLIST_SELFTEST: PASS (28 cases)`,
`CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`. Between the two green revisions
the tree went transiently red twice (22:40) and both were fixed — see the
mid-edit clause in the entry.

- `bash corpus/checklist-run.sh` ⇒ `CHECKLIST_RATIO: runnable=9/16 floor=8
  by_hand=7` then `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)`
  exit 0 (~2.3 s); `--selftest` ⇒ `CHECKLIST_SELFTEST: PASS (28 cases)` exit 0;
  `--list` ⇒ `CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`; `--only E1` ⇒ the two
  summary lines, exit 0; `--only E2` ⇒ `BY-HAND E2 (manual-change: --pin runs
  once after an intentional host edit, and which REPIN/MOVED lines are acceptable
  is an authoring call)`, exit 0.
- `corpus/checklist.tsv` is **8** columns — `id class lead check expect_exit
  expect_last reason note` — with `lead` an ERE matched against the item text, so
  the row↔item mapping is a **bijection** enforced in both directions
  (`UNMATCHED-LEAD`/`DUPLICATE-LEAD`/`UNMATCHED-ITEM`/**`DUPLICATE-ITEM`**/`UNDECLARED`/`EXTRA`).
  Row ids are `E1..E8` then `H1..H8`.
- Runnable rows (9): E1 (`bash corpus/surface-census.sh >/dev/null && bash
  corpus/drift-pins.sh`, pinned last line drift's verdict), E4 (`REF_PATH_SCAN:
  hits=0`), E5 (`op-ref-probe.sh`), E8 (jq over `~/.local/state/tac/handoff-status.json`
  → `HANDOFF_STATUS: OK`), H1 (`CLIENT_LOCK: flock=N declared=1 mode=600|absent`),
  H3 (jq over both config layers → `CONFIG_OVERLAY: OK`), H4 (`JANITOR_PERMS: OK
  (entries=2 steps=4)`), H7 (`transcript-scan.sh`, `expect_exit 0|1`, pinned
  `HITS=2` line), H8 (`CONTROL_PLANE: password_refs=0 listeners=N established=0`).
- By-hand rows (7): `authoring-duty` ×4 (E3, E6, E7, H6), `runtime-behavior` ×1
  (H2), `manual-change` ×1 (E2), `cross-lane` ×1 (H5) — `operator-scope` is the one
  class of the closed five no row needed.
- Verdicts (landed wording): `CHECKLIST_RUN: CLEAN|BROKEN (items=N runnable=K
  by_hand=M failed=f)` — no `skipped` field; `CHECKLIST_RATIO: runnable=K/N
  floor=F by_hand=M`; exit-1 `ITEM-FAIL <id> (exit a want b)` / `ITEM-LASTLINE
  <id> (got …)` / `… TIMEOUT`; exit-2 `POLICY` (row out of policy, nothing run) /
  `SETUP`; `CHECKLIST_LIST`; `CHECKLIST_SELFTEST: PASS|FAIL (N cases)`.
- Recorded ceiling (L1 names it as the class's weak point, verified by me): E4's
  declared exclusion is a **vault-name allowlist** — `grep -vE
  'op://(FakeVault|wal|vault)/'` — and `op://vault/` is the default 1Password
  vault name, so a synthetic `op://vault/<item>/<key>` line is dropped before the
  count (`… | grep -vE … | wc -l` ⇒ 0 while the raw shape pattern matches it ⇒ 1).
  The sweep proves the placeholder form is absent, not that any live ref is.
- Defects found by execution during the round, each fixed and re-verified
  (L1-owned; two repros came from these read-only runs): (i) `uniq -d` exits 1 on
  an empty result, and under `set -euo pipefail` that made `verify` exit 1 with
  **zero bytes** of output at the `dup_ids`/`dup_reasons` sites — the `dup_ids`
  site survived only because its enclosing function is called in a condition
  context; both guarded, and last-line extraction moved to `awk 'NF{l=$0} END{print l}'`
  so empty row output no longer kills the run. (ii) H4's front-matter capture
  `re.search(r'^---\n(.*?)\n---\n', …)` returns a body whose last line has no
  trailing newline, so `(?:[ \t]+.*\n)+` consumed only the first permission entry
  and the row reported `JANITOR_PERMS: DEFECT (entries=1 steps=4)` against a
  correct host file (fixed with `fm = m.group(1) + "\n"`). (iii) E4's first run
  was `ITEM-FAIL E4 (exit 1 want 0) | REF_PATH_SCAN: hits=3` — three undeclared
  ref-shaped literals in artifacts (`corpus/knowledge/op-env-refs.md:14`,
  `corpus/lessons/round-5-aggregator-audit.md:19`,
  `corpus/transcript-scan.sh:202`, all the documented placeholder form), which
  forced the declaration above and the `vault` name into the allowlist; the
  `DENY_CHECK` policy also grew to refuse `the-janitor run` and
  `claim-ledger.sh` in a row's check.

Peer evidence transcribed (not re-run): `ItemsScout.md` (ground-truth census,
F1-F7), `EntryDraftExecutor.md` (row plan + delegation map + bounds),
`CheckPlanner.md` (stricter reading: `runnable=3 by_hand=13` on the
duty-versus-premise rule), `SiblingConnector.md` (sibling sweep), `HostScout.md`,
`ReportDraftExecutor.md`, `TsvMutator.md` (plan-only at the time of writing),
`ItemReviewer.md` (see relay below).

## Lane relay — [CONFLICTS_UNRESOLVED: 1] (for L1; not for the LOG bullet as executed evidence)

`ItemReviewer.md` (22:38, read as of 22:39) has a usable first half and a broken
second half. Usable: its executed table records the last line of all nine
runnable rows, and the values match what the shipped gate prints
(`HANDOFF_STATUS: OK (boundaries=5 receipt=present sha=present)`, `CLIENT_LOCK:
flock=3 declared=1 mode=600`, `CONFIG_OVERLAY: OK (providers=1 share=disabled
autoupdate=False global=parsed global_providers=absent)`, `CONTROL_PLANE:
password_refs=0 listeners=0 established=0`, `REF_PATH_SCAN: hits=0`, `JANITOR_PERMS:
OK (entries=2 steps=4)`). Broken, and therefore **not to be pasted into the LOG
entry as executed evidence**:

- its contested verdict `E1 — SHOULD-BE-BY-HAND in the shipped form`, whose
  supporting block is a console transcript invoking binaries that do not exist on
  this host (`node-drop-drytree`, `node-drop-dry-tree-left`, `net soi`, `itsu`,
  `net-sol`, `t_purt_iterator.inc`), after which the report's prose is corrupted
  mid-sentence; the argument itself (item 1's duty is *sequence plus both gates
  green*, the row registers the two exits) is readable, but nothing in the lane
  demonstrates a state where the row passes and the duty is broken — no executed
  counterexample, so the claim stays unverified and I record it as a conflict, not
  as a finding;
- its provenance sentence "Gate and TSV are **byte-identical to repo HEAD
  `baec94f…`**" contradicts the tree (`git status --short` shows both untracked
  new files, and `corpus/checklist.tsv` was edited at 22:36); do not repeat it in
  the entry or the report;
- its proposed North-Star ("the maximum P such that every runnable row survives
  every broadcast clause") is a criterion change, which is L1's call and not the
  scribe's; if it is adopted, the entry's `9 runnable / 7 by-hand` sentence needs
  the criterion the repo states, not the lane's.

Still silent at 22:39 (no scratch artifact): mutation-tester (re-ran? its file is
still plan-only), labrat, sentinel, critic, simplifier, distiller. `{{WAVE_OTHER}}`
is where their one-clause results go; if a lane lands nothing executable, write
that it found nothing executable.

---

## Entry (draft — paste as one bullet after the round-14 bullet)

- 2026-09-28 — round 15 (**operability 8 → 9**; axis-move: the last large prose
  surface in this repo becomes executable — each of the 16 credential-hygiene
  checklist items is now a row in a data file, mapped back to its item text by a
  gate-enforced bijection, and every mechanisable one prints a verdict from one
  command). Dispatch: 14 L2 lanes in one batched call (planner, connector, 2
  scouts, scribe, 2 executors, reviewer, critic, sentinel, labrat,
  mutation-tester, simplifier, distiller). **The finding**: no count of the
  checklist on disk was ever right — section-scoped, `awk '/^## Credential-hygiene
  checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- \[ \]'` ⇒ **16**
  today, and the same command over every `SKILL.md`-touching commit ⇒ 10, 12, 13,
  14, 16 (items entered in rounds 2, 7, 8, 9 and 13), so **no revision ever held
  15** while `SCORECARD.md:16` called it "a 15-item hygiene checklist" — wrong by
  two at `ea77bf0`, where the count was 13, and stale by three now ({{STALE_CELL}}); the three
  "12 of the checklist items are still operator judgement" cells
  (`SCORECARD.md:40/62/84`) were wrong at every revision they appear in, because
  items 1/5/15 already named live gates and items 12/14 are pinned today
  (`drift-pins.sh` on `janitor.md`'s `"*": deny` front matter, `transcript-scan.sh`
  on the persisted-DB verdict) — the runnable/judgement split was asserted once
  and never recomputed, so an item could gain or lose a command and the sentence
  kept reading as truth; and `SCORECARD.md:209` had already named "the checklist
  item count" as the round-15 falsifiable target, so this round closes the round-13
  self-named gap rather than inventing one. Three host facts fell out of the same
  census as defects in committed rows rather than prose slips: `PROVINCE.md:12`
  and `corpus/surface-census.tsv:22` both file the lock under `client.py`, but
  `grep -nic lock ~/.config/the-janitor/client.py` ⇒ **0** and the flock is
  `~/.local/bin/the-janitor`'s (`LOCK_FILE` L12, `exec 9>"$LOCK_FILE"` + `flock 9`
  at L130-131, L139-140, L175-176) — item 9's serialization mechanism was
  documented in a file that does not contain it; four symbols the checklist names
  were asserted by nothing (`grep -c` over `corpus/*.sh corpus/*.tsv` ⇒ 0 for
  `autoupdate`, `target_authority_conferred`, `40961`,
  `OPENCODE_SERVER_PASSWORD`, the sole `9222` hit being a sha256 digit run at
  `corpus/stamps.tsv:1`), so items 8, 11, 13 and 16 read as covered while being
  covered by nothing; and the item that forbids ref paths in artifacts was
  inverted by what the repo proved — `corpus/surface-census.sh:516-528` asserts
  `ref-verbatim yes` / `plain-redacted yes`, i.e. `the-janitor refs` prints the
  ref path and redacts the plain value, the reverse of the intuition the item is
  written on. Landed: `corpus/checklist.tsv` — **16** rows
  (`id class lead check expect_exit expect_last reason note`), `lead` an ERE that
  must match the item's own text, so the mapping is a bijection over the 16 items
  in both directions (`UNMATCHED-LEAD`/`DUPLICATE-LEAD`/`UNMATCHED-ITEM`/
  `DUPLICATE-ITEM`/`UNDECLARED`/`EXTRA`), i.e. a deleted item, a drifted row or
  two rows claiming one item cannot pass silently; `corpus/checklist-run.sh` —
  default verify runs each `runnable` row at repo root under a 240 s timeout and
  matches its exit code **and** its last non-blank stdout line, printing
  `CHECKLIST_RATIO: …` then `CHECKLIST_RUN: …`, with
  `ITEM-FAIL`/`ITEM-LASTLINE`/`TIMEOUT` as exit-1 defects and `POLICY`/`SETUP` as
  exit-2 shape/policy errors that execute nothing, plus `--list`, `--only <id>`,
  `--selftest`; the by-hand rows carry a reason of the form `<class>: <text ≥24
  chars>` with the class from the closed 5-set {authoring-duty, runtime-behavior,
  cross-lane, manual-change, operator-scope} — the round-14 `Reverify:` pattern
  (`bash corpus/claim-ledger.sh docs`) applied to the checklist — so
  "un-mechanisable" is a labelled, counted set under a ratio floor instead of a
  residue, and the split reads **9 runnable / 7 by-hand** (4 authoring-duty, 1
  each runtime-behavior, manual-change, cross-lane; `operator-scope` is the one
  class no row needed) rather than an un-recomputed sentence. Three of the
  runnable rows delegate to a sibling gate by matching its verdict line instead
  of re-implementing it (E1 `surface-census.sh`+`drift-pins.sh`, E5
  `op-ref-probe.sh`, H7 `transcript-scan.sh` with `expect_exit 0|1` and the
  declared `HITS=2` baseline pinned as teeth), and the other six assert a premise
  directly on the host with `jq`/`grep` over non-secret files (handoff boundaries,
  both config layers, the agent front-matter permission block, the flock sites and
  lock mode, the 40961 control-plane containment); the gate never reads `op.env`,
  resolves a reference, execs `op`, starts/stops the handler or prints a value —
  a check that touches a denied surface (including `the-janitor run` and
  `claim-ledger.sh`) is `POLICY` exit 2, and no row may invoke
  `corpus/claim-ledger.sh` (the ledger's `cells` mode skips self-audit rows).
  Item 1's row is deliberately **narrower** than its item text — the item also
  names `claim-ledger.sh verify` (recursion) and `--pin` (mutating), both banned
  by the row contract — and the row's `note` says so rather than the gate
  silently dropping half of it. Docs: `SKILL.md` gains a decision-table row
  (`SKILL.md:40`, verb, exact verdicts and exits, and the trap "trusting a
  by-hand row as verified — it is a declared gap") plus an executable header on
  the checklist itself (`SKILL.md:421-425`: "**Executable since round 15.** Every
  item below is one row of `corpus/checklist.tsv`, run by `bash
  corpus/checklist-run.sh`: 9 items carry a runnable check (expected exit +
  expected last output line), 7 declare a `by-hand` class with a unique reason
  because no command shape exists"), `corpus/knowledge/checklist-execution.md`
  records the row grammar, the class set, the verdict vocabulary, the ratio floor
  and the bounds, and declares its own re-verification set —
  `Reverify: R15-01, R15-02, R15-03, R15-04` — the two lock mis-attributions are
  corrected in place (`PROVINCE.md:12` now `… HTTP client: session-id,
  THE_JANITOR_REQUEST_TIMEOUT (the client.lock flock lives in the CLI, not here —
  measured round 15: grep -nic lock client.py ⇒ 0, flock at the-janitor
  L130/139/175-176)`; `corpus/surface-census.tsv:22` now `… HTTP client:
  session-id, request timeout (the flock is in the CLI)`), and
  `corpus/lessons/round-15.md` records the wave. Ledger: rows `R15-01..R15-04`
  pin the gate's own summary and the declarations above
  ({{R15_EXTRA_ROWS}}), plus re-pinned count rows (`{{REPINNED_ROWS}}`); `SCORECARD.md` gains the
  round-15 pre/post tables and the operability cell cites the row that re-runs the
  checklist (`{{SCORECARD_CELLS}}`). Evidence (shipped revision):
  `bash corpus/checklist-run.sh` ⇒ `CHECKLIST_RUN: CLEAN (items=16 runnable=9
  by_hand=7 failed=0)` exit 0 with `CHECKLIST_RATIO: runnable=9/16 floor=8
  by_hand=7` (~2.3 s); `--selftest` ⇒ `CHECKLIST_SELFTEST: PASS (28 cases)`;
  `--list` ⇒
  `CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`; `--only E1` ⇒ the two summary
  lines exit 0 and `--only E2` ⇒ `BY-HAND E2 (manual-change: --pin runs once
  after an intentional host edit, and which REPIN/MOVED lines are acceptable is
  an authoring call)`; pre-move, same tree: `bash corpus/checklist-run.sh` ⇒
  `No such file or directory`, exit 127, and the only count on disk was the stale
  `SCORECARD.md:16` "15-item". Siblings unchanged: `DRIFT_PINS: CLEAN
  (files={{PIN_FILES}} symbols={{PIN_SYMBOLS}})` + 13 cases; `SURFACE_CENSUS:
  CLEAN (assets={{SC_ASSETS}} runtime=15 scanned=4 ok={{SC_OK}} absent=2
  skipped={{SC_SKIPPED}})` + `--verbs CLEAN (pass=7 skip=3)` + 16 cases;
  `TRANSCRIPT_SCAN: HITS=2` exit 1 by design; `OP_REF_PROBE: CLEAN (checks=44
  oprun=12 refs=7 divergent=5 edge=10 sig=6)` + 29 cases; `claim-ledger.sh verify`
  ⇒ `CLAIM_LEDGER: CLEAN (claims={{CLAIMS}} stamped={{STAMPED}} ids={{IDS}} …)`
  and `cells` ⇒ `CELL_AUDIT: CLEAN (cells={{CELLS}} row_pointed={{ROW_POINTED}}
  … self_skipped={{SELF_SKIPPED}} …)` — the `R15-*` rows are `bash
  corpus/checklist-run.sh` invocations run through the ledger's claims machinery,
  and the gate itself runs no claim row, so there is no recursion and the round's
  no-op-execution rule held for every lane. **The L2 wave**: the scout's
  ground-truth census is what made the finding measurable — it re-counted the
  checklist at every `SKILL.md` revision (never 15), mapped all 16 items onto the
  gates that already covered them (5 runnable across 4 sibling gates at the
  pre-state), produced the unpinned-symbol and `9222`-false-positive results
  quoted above, and refuted one of my own starting assumptions by reading the gate
  source rather than the prose (`corpus/surface-census.sh:516-528`), which is what
  turned item 4 from a predicted by-hand row into the round's one new sweep
  (`REF_PATH_SCAN: hits=0`, count-only). **Defects found by execution, each fixed
  and re-verified**: `verify` first exited 1 with zero bytes of output because
  `uniq -d` exits 1 on an empty result and `set -euo pipefail` applied at the
  `dup_reasons` site (the `dup_ids` site survived only because its enclosing
  function is called in a condition context) — both guarded, and last-line
  extraction moved to `awk 'NF{l=$0} END{print l}'` so empty row output no longer
  kills the run; H4's `re.search(r'^---\n(.*?)\n---\n', …)` returns a body whose
  last line has no trailing newline, so `(?:[ \t]+.*\n)+` read only the first
  permission entry and the row reported `JANITOR_PERMS: DEFECT (entries=1
  steps=4)` against a correct host file; and E4's first run was `ITEM-FAIL E4
  (exit 1 want 0) | REF_PATH_SCAN: hits=3` — three undeclared ref-shaped literals
  in artifacts (`corpus/knowledge/op-env-refs.md:14`,
  `corpus/lessons/round-5-aggregator-audit.md:19`,
  `corpus/transcript-scan.sh:202`, all the documented placeholder form), which is
  what forced the declared exclusion below; and two later mid-edit revisions were
  caught before shipping — E4's rewrite swallowed its own verdict line into the
  `n=$(…)` capture so the row printed nothing while exiting 0, and H7's widened
  `expect_exit 0\|1\|2` tripped `POLICY row H7: expect_exit 0|1|2 is not N or
  A|B`, exit 2, with nothing executed — both fixed in the next revision, which
  re-run green with the same three numbers. One lane's stricter reading was
  refused with its reason rather than smoothed: the planner's duty-versus-premise
  rule scored the same 16 items `runnable=3 by_hand=13`, and the shipped criterion
  is narrower — "is there a command whose verdict is a defect signal for this
  item", with the row's `note` naming the duty that remains the operator's.
  **Recorded ceiling** (named, not hidden): E4's exclusion is a vault-*name*
  allowlist (`op://(FakeVault|wal|vault)/`), and `vault` is the default 1Password
  vault name, so a synthetic `op://vault/<item>/<key>` literal is dropped before
  the count while the shape pattern matches it — the sweep proves the placeholder
  form is absent, not that any live ref is. {{WAVE_OTHER}} Adjacency (reported,
  not absorbed): the connector lane's source-level sweep found that **no** sibling
  lead implements the unit this round shipped — checklist item → runnable command
  → per-item verdict — kotoba
  `verifiers/verify_skill_checklist.py:671-725,847-873,1195-1209` maps
  hash-pinned boxes to dispositions and resolves command heads without executing
  a box's command, kumitate `scripts/proxy-check.mjs:277-294` counts
  checklist-box lines as a proxy term in a composite score, kumitate
  `round-gate.mjs:303-478` gates round artifacts, kasegi
  `corpus/instruments/anchorcheck.py` resolves Markdown `path:line` anchors (and
  prints `MISSING-FILE`/`PAST-EOF` findings while still exiting 0 — relayed, not
  adjudicated), kengaku `grader.py` replays committed experiment evidence, and
  kake's only located script (`scripts/probe-delta.mjs`) is a history report — so
  the gate is *adjacent*, not duplicative, and the one shared shape worth naming
  (a stable-ID outcome ledger) stays with the integrator. No vault access, no
  handler start/stop, no Chrome launch, no secret value in any artifact, all L2
  execution scratch-only.

---

## Placeholders

Resolved from L1's live evidence block at 22:36 (and confirmed by my own
read-only re-runs at 22:37): the `CHECKLIST_RUN`/`CHECKLIST_RATIO`/`CHECKLIST_LIST`/
`CHECKLIST_SELFTEST`/`--only` strings are now real numbers in the bullet above.
What remains unresolved, with where each comes from:

1. `{{SKILL_POINTER}}` — **resolved**: the landed text is quoted in the bullet
   (`SKILL.md:40` decision-table row and the `SKILL.md:421-425` header). If L1
   edits either before shipping, re-quote both; do not paraphrase.
1b. `{{STALE_CELL}}` — `SCORECARD.md:16` still reads "a 15-item hygiene checklist"
   at 22:38 (verified again: `sed -n '16p' SCORECARD.md`). Either the cell is
   corrected (paste the new text and say which round corrected it — round 13 did
   exactly this for a historical number) or the placeholder becomes the sentence
   that the stale cell **stands**, with the reason (it is the round-9 record). Do
   not ship the bullet with a dangling `{{}}` and do not silently drop the
   finding: this string is one of the three the round exists to remove.
2. `{{KNOWLEDGE_ENTRY}}` — **resolved**: `corpus/knowledge/checklist-execution.md`
   (untracked at 22:39, `Reverify: R15-01, R15-02, R15-03, R15-04` at its line 11)
   is quoted in the bullet. It must be stamped and its four rows must exist in
   `corpus/claim-ledger.tsv` before shipping (round-14 rule, `bash
   corpus/claim-ledger.sh docs`); if the entry is dropped, delete the clause.
3. `{{LOCK_FIX_LINES}}` — **resolved**: both rows were corrected in place at the
   same line numbers (`PROVINCE.md:12`, `corpus/surface-census.tsv:22`) and the
   new text is quoted in the bullet; re-read both if L1 edits either file again,
   since the quoted text is verbatim.
4. `{{R15_EXTRA_ROWS}}` — the entry says `R15-01..R15-04` because
   `corpus/knowledge/checklist-execution.md` declares exactly that set as its
   `Reverify:` line; `corpus/claim-ledger.tsv` still held 18 rows at 22:39. When
   the rows land, replace the parenthetical with what each one actually pins, or
   trim the range to the rows that shipped.
5. `{{REPINNED_ROWS}}` — the count rows re-pinned with `old → new` (expected
   candidates: `R13-02` ledger rows 18 → N where N = post-landing
   `grep -c '^R1' corpus/claim-ledger.tsv`; `R12-03` stamps 44 → N; `R11-09`
   selftest cases 94 → N). List only the rows actually re-pinned.
6. `{{SCORECARD_CELLS}}` — the cell pointers added/changed in the round-15 tables
   (row ids), mirroring round 14's "five score-card cells now cite the rows that
   re-run the commands their own Evidence already quoted". The operability cell's
   ceiling sentence must keep the two that remain (nothing schedules any gate; and
   a runnable row verifies a premise, not the operator's duty).
7. `{{PIN_FILES}}` / `{{PIN_SYMBOLS}}` — `DRIFT_PINS` counts (15/20 before this
   round). They move if the round pinned new files or added pins for the symbols
   the checklist now asserts; the TSV/gate are repo files, so expect 15/20 unless
   L1 pinned something else — say which.
8. `{{SC_ASSETS}}` / `{{SC_OK}}` / `{{SC_SKIPPED}}` — `SURFACE_CENSUS` counts
   (20 / 34 / 0 before this round). A new census row for the gate or the TSV moves
   `assets`/`ok`; quote the verdict line, and if `skipped` changed, say why
   (round-13 lesson: never quote a sibling verdict as a constant).
9. `{{CLAIMS}}` / `{{STAMPED}}` / `{{IDS}}` — `verify` summary fields; `stamped`
   moves if the new gate or TSV is stamped.
10. `{{CELLS}}` / `{{ROW_POINTED}}` / `{{SELF_SKIPPED}}` — `cells` summary fields.
    `row_pointed` rises by the number of new cells citing `R15-*`. `self_skipped`
    changes **only** if a new row re-invokes `claim-ledger.sh`, which the checklist
    contract (and now `DENY_CHECK`) forbids — if it moved, the contract was
    violated and the entry must say so rather than absorb it.
11. `{{WAVE_OTHER}}` — the lanes L1 reported as still open at 22:36
    (mutation-tester, labrat, reviewer, critic, sentinel, simplifier, distiller):
    one clause each with the id or command that shows it — the mutation-tester's
    `FAILS-CLOSED`/`FALSE-CLEAN` verdict per mutation, the labrat's live run, the
    reviewer's citation check, the critic's executed counterexample and the fix it
    forced, the sentinel's verdict on the allowed-print surface, the simplifier's
    deletion, the distiller's synthesis or its honest "no artifacts". If a lane
    reported nothing executable, write that it found nothing executable rather
    than inflating it.
12. Dispatch line — confirm "14 L2 lanes in one batched call" and the role list
    against the spawn record. Round 13 was 12 lanes in two calls, round 14 was 14
    in one; this number must not be copied forward if the roster differed.
13. `Siblings unchanged` — if any sibling gate is not green at the shipped
    revision, do **not** write "unchanged": quote the non-green verdict inside the
    same bullet (rounds 13/14 never smoothed this).
14. Posture sentence — the last sentence is fixed by the round contract: "no vault
    access, no handler start/stop, no Chrome launch, no secret value in any
    artifact, all L2 execution scratch-only". If any lane started/stopped the
    handler or read `$CONFIG_DIR/op.env`, replace it with that lane's actual scope
    and name the deviation — the sentence is a measurement, not boilerplate.
15. `ITEM-FAIL`/`ITEM-LASTLINE` gloss — the bullet quotes the landed names; if the
    gate's `--help` header and its code disagree, believe the code and say so.
16. E4 ceiling — written out concretely in the bullet, **no placeholder**: it
    quotes `op://(FakeVault|wal|vault)/` and the demonstration (`… | grep -vE … |
    wc -l` ⇒ 0 while the raw shape pattern matches ⇒ 1). If L1 narrows the
    exclusion before shipping (a marker-permitted form, or rewriting the three
    examples to an ellipsis), edit the clause in place and delete the ceiling —
    do not leave a ceiling the gate no longer has.
17. Pre-move probe — `bash corpus/checklist-run.sh` at `2486643` ⇒ `No such file
    or directory` exit 127 is a *path* check, not a gate verdict. If a reviewer
    objects to it as pre-move evidence, replace it with the item-count command and
    the stale `SCORECARD.md:16` string, which are the real before-side.
18. Criterion sentence — written out in the bullet, **no placeholder**: the
    planner-lane split (`runnable=3 by_hand=13` under duty-versus-premise) is
    quoted as *refused with its reason*. Confirm the shipped criterion's wording
    against the landed `corpus/knowledge/*` entry (or the gate header) before
    citing it; do not paraphrase a criterion the repo does not state.
19. Revision pin on the Evidence block — the quoted trio is the revision L1
    confirmed at 22:36 (`CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7
    failed=0)`, `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7`,
    `CHECKLIST_SELFTEST: PASS (28 cases)`). The TSV kept moving after that
    (22:40 revisions made E4's check print nothing and H7's widened exit trip
    `POLICY row H7: expect_exit 0|1|2 is not N or A|B`, exit 2; both reported).
    A LOG bullet must quote **one** revision: take the final trio from the shipped
    commit's own run and, if any number differs from the three above, replace them
    in the bullet and say in the same sentence which revision the entry pins.