# Checklist execution — the 16 credential-hygiene items, one verdict each

Source basis: `corpus/checklist-run.sh` (v1, round 15; 496 lines, sha256
`4a06a9f2a4e4…` at the revision read) and `corpus/checklist.tsv` (40 lines, 16
data rows: 9 `runnable` / 7 `by-hand`, sha256 `28bd238e549c…`); both files were still being edited while this entry
was written (the gate grew 452→496 lines and its selftest 28→34 cases in that
window), so the figures below are a named-revision snapshot: the landing step
re-stamps both rows (`corpus/claim-ledger.sh stamp`, a reviewed commit) and
re-runs §Reproduction;
`SKILL.md`
§Credential-hygiene checklist, 16 `- [ ]` items counted this round —
`awk '/^Evidence production:/,/^Handler operation:/' SKILL.md | grep -c '^- \[ \]'`
⇒ 8 and `awk '/^Handler operation:/,/^## Evidence-receipt patterns/' SKILL.md |
grep -c '^- \[ \]'` ⇒ 8, so `SCORECARD.md:16`'s "15-item hygiene checklist" is
stale; the four gates the items name, re-run on the live host 2026-09-28:
`SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)`
exit 0 · `DRIFT_PINS: CLEAN (files=15 symbols=20)` exit 0 ·
`OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)`
exit 0 · `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2
schema-absent=0)` exit 1 (by design); plus `corpus/knowledge/claim-ledger.md`
(Class 6, bound 26) for the declaration and self-reference rules,
`corpus/knowledge/drift-gate.md` for the `op.env` NOHASH policy, and
`corpus/knowledge/surface-census.md` for the `SKIP`/`UNVERIFIED` split this gate
inherits when it delegates.

Gates observed this round against the landed pair: `CHECKLIST_RATIO: runnable=9/16
floor=8 by_hand=7 delegated=3 direct=6` + `CHECKLIST_RUN: CLEAN (items=16
runnable=9 by_hand=7 failed=0)`, exit 0, ~2.1 s (two runs) · `--list` ⇒
`CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`, exit 0 · `--selftest` ⇒
`CHECKLIST_SELFTEST: PASS (34 cases)`, exit 0. Every other verdict string in this entry was produced by a
command in §Reproduction — each of the nine runnable rows was also run by hand
and asserted against its own `expect_exit`/`expect_last` (9/9 match), and the
defect vocabulary was exercised on scratch fixtures via `--tsv`/`--skill`. No row
reads `$CONFIG_DIR/op.env` bytes, resolves a reference, starts or stops the
handler, or invokes `corpus/claim-ledger.sh`, and the deny-list governs each
row's own command string; the one delegate that execs `op` — E5's
`op-ref-probe.sh` — does so over generated plain-value fixtures and refuses any
reference token before exec (see §Runnable vs by-hand, reason 4).

## Why this gate exists

operability scored 8 in rounds 10–14 and every round gave the same reason, in the
scorecard's own words: round 10 (`SCORECARD.md:62`) "Three runnable gates … 12
checklist items still operator judgement"; rounds 12/13/14 (`:95`, `:118`,
`:188`) "the ceilings are unchanged — nothing schedules any gate and the
checklist's judgement items remain judgement"; the ceilings list (`:162`, `:220`)
"nothing schedules the six gates; the checklist still holds …".

Nothing in those sentences was wrong. What was missing is that **no command could
say which items are judgement and which are commands**: the split was prose
(`SCORECARD.md:28`: "12 of the checklist items are still operator judgement, not
commands"), the item count was stale in the depth cell, and an item could be
added, reworded or dropped with every gate still green. The round-13 critic's
result is the shape of that hole: a declaration that *resolves* is not a
declaration that *measures* (`corpus/knowledge/claim-ledger.md` bounds 17, 25).

This gate makes the checkbox list the **source** and the TSV the **declaration**,
one row per item, and each `runnable` row a command with a verdict; the residue
that genuinely cannot be mechanised becomes an explicit `by-hand` class carrying
a reason class and a unique reason — the round-14 `Reverify: by-hand: <class> —
<reason>` pattern applied to the checklist, with the same shape rules (class from
a closed set, reason ≥24 characters, unique across the file).

## Items come from `SKILL.md`; `lead` is the bijection

The item set is not a list inside the gate. `extract_items` reads **`SKILL.md`
itself** — only the `## Credential-hygiene checklist` section, stopping at the
next `## ` heading — and takes every `- [ ] ` bullet, appending indented
continuation lines to the item they follow (three of the sixteen items are
multi-line in the prose — H6, H7 and H8).

Each row's `lead` is an ERE matched against the *item text* with newlines
collapsed and whitespace squeezed, and a leading space prepended so an
unanchored pattern still sees a boundary. The mapping must be a bijection over
the sixteen items, and every way of breaking it has its own verdict:

| break | verdict | measured |
|---|---|---|
| a row whose `lead` matches nothing | `UNMATCHED-LEAD <id> (/lead/ matches no item)` | source |
| a row whose `lead` matches several items | `DUPLICATE-LEAD R1 (/item text/ matches 6 items)` | fixture |
| two rows declaring the same item | `DUPLICATE-ITEM <j> (2 rows declare it)` | fixture |
| an item no row declares | `UNMATCHED-ITEM <j> (no row declares it)` | fixture |
| fewer rows than items | `UNDECLARED (items=7 rows=6)` | fixture |
| more rows than items | `EXTRA (items=N rows=M)` | source, selftest-pinned |

That is the design's real teeth, and it is stronger than "there are sixteen rows
in a TSV": a seventeenth checkbox added to `SKILL.md` is `UNDECLARED (items=17
rows=16)` **and** `UNMATCHED-ITEM 17`, a reworded item loses its row, and a lead
widened until it matches two items is refused. The prose list stays the source,
the TSV stays the declaration, and either one moving alone is a defect.

## Schema — `corpus/checklist.tsv`, column by column

`id <TAB> class <TAB> lead <TAB> check <TAB> expect_exit <TAB> expect_last
<TAB> reason <TAB> note`. `#` comment lines are skipped; a row that does not
carry exactly eight fields is `POLICY row <id>: N columns, want 8 (id class lead
check expect_exit expect_last reason note)`, exit 2, nothing executed.

| column | values | meaning |
|---|---|---|
| `id` | `<letter><digits>` | the row's name in every verdict line; must match `^[A-Z][0-9]+$`; duplicate ids are `POLICY duplicate row id: …`. The landed set is `E1–E8` (`Evidence production:`) and `H1–H8` (`Handler operation:`), in `SKILL.md` order |
| `class` | `runnable` / `by-hand` | the only column that changes what the row means. Anything else is `POLICY row <id>: class "…" is not runnable\|by-hand` |
| `lead` | ERE | matched against the item text; the bijection above |
| `check` | command string / `-` | `runnable`: run as `bash -c` with cwd = repo root under `timeout $CHECKLIST_TIMEOUT` (default 240 s). `by-hand`: the literal `-`, i.e. the row asserts no command shape exists |
| `expect_exit` | `N` or `A\|B\|C…` / `-` | `runnable`: accepted exit code(s), matched as `^[0-9]+(\|[0-9]+)*$`. `by-hand`: `-`. A bad value is `POLICY row <id>: expect_exit "…" is not N or A\|B\|…` |
| `expect_last` | ERE / `-` | `runnable`: matched with `grep -qE` against the **last non-blank stdout+stderr line**. `by-hand`: `-` |
| `reason` | `-` / `<class>: <text>` | `runnable` rows must carry `-` (`POLICY … runnable row must carry reason \`-\``). `by-hand`: class from the closed five, text ≥24 chars, matched as `^(authoring-duty\|runtime-behavior\|cross-lane\|manual-change\|operator-scope): .{24,}$` |
| `note` | free text, no tabs | `runnable`: what the row verifies. `by-hand`: why it cannot be mechanised and what would mechanise it. Both classes need a non-`-` note, so no row is a bare command |

The closed classes are `authoring-duty`, `runtime-behavior`, `cross-lane`,
`manual-change`, `operator-scope`; duplicate reasons are
`DUPLICATE-REASON (…)` (exit 1) — the uniqueness rule `docs` applies to entry
declarations (`corpus/knowledge/claim-ledger.md` Class 6), and the same closed-set
discipline that keeps the by-hand escape from becoming a free-text excuse.

## Runnable vs by-hand, and why the split is the point

A row is `runnable` when the item's claim reduces to **a premise that is true of
this host now** — a declared surface still has its declared mode, the overlay
still carries its containment keys, the port still has no established socket. A
row is `by-hand` when the item is an **operator duty** — a rule about what a
person does next (`--pin` once after an intentional change, quote only
metadata-only output, one request at a time) or about behaviour that only exists
while the handler runs. No command observes a duty; the class is where that is
said out loud instead of living in prose.

The split matters for four reasons, each one a failure earlier rounds recorded:

1. **Silence was indistinguishable from satisfaction.** Before this gate the
   checkbox list enforced nothing: an item naming a real gate and an item naming
   a judgement call sat in the same list with the same formatting.
2. **The unverifiable set is countable.** `CHECKLIST_RATIO` prints
   `runnable=K/N floor=F by_hand=M delegated=D direct=K-D` and `runnable*2 >= N`
   (floor `ceil(N/2)`, here 8 of 16) keeps the by-hand class from swallowing the
   checklist — the shape rule `DOC_AUDIT_RATIO` uses one level up. The
   `delegated` half matters as much: a row whose `check` starts
   `bash corpus/<gate>.sh` (`^bash[[:space:]]+corpus/`) is an item that *already
   had a gate*, and counting it as a new measurement would overstate the round.
   The landed pair is `delegated=3 direct=6` — three gates named by items
   (`surface-census`+`drift-pins` under E1, `op-ref-probe` under E5,
   `transcript-scan` under H7), six assertions this file introduces.
3. **A duty escalated to a command becomes a false clean.** Encoded as a `grep`,
   "never widen `janitor` permissions" would go green on a host where the ceiling
   *file* is correct and the live agent was widened through the global config:
   the premise holds, the duty is broken. That is what the class column prevents,
   and why H4's row asserts the file and says so in its `note`.
4. **A delegated row inherits its delegate's policy, not this gate's.** The
   deny-list governs a row's *own* `check` string; E5 delegates to
   `op-ref-probe.sh`, which is the one delegate that execs `op run` — over
   generated plain-value fixtures, refusing any reference token before exec (the
   probe's own `POLICY`, `corpus/knowledge/op-ref-consumption.md`). A reader who
   takes "no row execs `op`" as an absolute property of this gate is wrong in one
   direction and right in the one that matters: no row resolves a reference.

**Contested split, recorded not resolved (round 15).** The shipped criterion is
"is there a command whose verdict is a defect signal for this item, with the
`note` naming the duty left to the operator"; under it 9 rows are runnable. The
row set itself records the nearest competing reading, on E5's `note`: classifying
a *delegating* row as by-hand (the check is another gate's, so the item's command
is not this file's evidence) makes the split **8 runnable / 8 by-hand — exactly
the floor, with no slack**. A stricter duty-only reading was argued further still
(3 runnable / 13 by-hand, reported by the planner lane via the integrator and not
re-measured here), at which point `RATIO` fires and the gate fails itself. All
three readings agree on the verdicts and disagree about what a "premise" is, so
the criterion — not the gate — is the binding design decision. Recorded because a
reader who applies either stricter rule will read the ratio line as inflated, and
that reading is not wrong, only different.

## Verdicts and exit codes

| verdict / mode | exit | what a reader does |
|---|---|---|
| `CHECKLIST_RATIO: runnable=K/N floor=F by_hand=M delegated=D direct=K-D` | — | the shape line, printed before every verdict: how much of the checklist answers with a command, and how much of *that* was already a gate. Landed pair ⇒ `runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6` |
| `CHECKLIST_RUN: CLEAN (items=N runnable=K by_hand=M failed=0)` | 0 | every runnable row matched its exit code **and** its last-line ERE, and the declaration is a clean bijection |
| `CHECKLIST_RUN: BROKEN (items=N runnable=K by_hand=M failed=F)` | 1 | at least one defect line above; `F` counts only rows that ran and failed, so a declaration defect prints `BROKEN … failed=0` (measured on fixtures) |
| `ITEM-FAIL <id> (exit a want b)` `[ TIMEOUT]` | 1 | the row ran, its exit code was not accepted (`a` = actual, `b` = declared, or the `A\|B` set). `TIMEOUT` is appended when `a` is 124. Six lines of the row's output follow, indented `    \| ` |
| `ITEM-LASTLINE <id> (want /ERE/ got "…")` | 1 | the exit code was accepted but the last non-blank line is not the declared ERE — a delegated gate that degraded while still exiting 0 lands here |
| `UNDECLARED` / `EXTRA` / `UNMATCHED-ITEM` / `DUPLICATE-ITEM` / `UNMATCHED-LEAD` / `DUPLICATE-LEAD` / `DUPLICATE-REASON` / `RATIO` | 1 | a declaration defect (table above plus `RATIO (runnable=K floor=F items=N)`); the run continues and reports all of them |
| `POLICY …` | 2 | a row is out of policy — a forbidden surface in `check`, a missing/`-` field, a class outside the two, a bad or duplicate id, a short/unclassed reason. Nothing is executed |
| `SETUP …` | 2 | the TSV or `SKILL.md` cannot be read, the section is missing, or `--only` names an unknown id. Nothing is executed |
| `--list` | 0 | `ROW <id> runnable lead=/…/ exit=… last=/…/ :: <check>` or `ROW <id> by-hand lead=/…/ <class>: <text>`, then `CHECKLIST_LIST: rows=N runnable=K by_hand=M`. Runs nothing |
| `--ratio` | 0 / 1 / 2 | audits the **declaration** (bijection, reason uniqueness, floor) and prints only `CHECKLIST_RATIO: …`; no row runs. A broken *row* is invisible here — measured: a `--tsv` copy with `expect_exit` set to `9` still prints the identical ratio line and exits 0, while the full run reports `ITEM-FAIL` + `BROKEN`. A broken *declaration* exits 1 (`RATIO`) or 2 (`POLICY`/`SETUP`) as usual |
| `--only <id>` | 0 / row / 2 | a `by-hand` row prints `BY-HAND <id> (<class>: <text>)`; a `runnable` row re-runs `verify` with only that row executed (the declaration audit still runs); an unknown id is `SETUP --only <id>: no such row id` |
| `--selftest` | 0/1 | scratch `SKILL.md` + TSV pairs rebuilt per case: `CHECKLIST_SELFTEST: PASS (34 cases)` or `FAIL (f/N cases)` |

`ITEM-FAIL` and `ITEM-LASTLINE` are deliberately two questions: *did the premise
change* versus *is the evidence still the evidence*. That is the split the ledger
draws between `STALE` and `STALE-POINTER`, and it is what keeps a delegated gate
honest — `transcript-scan.sh` exits 1 on a healthy host (`SKILL.md` says exit 1
is a finding), so H7 accepts `0|1|2` with two pinned last lines and pins the
count-bearing summary.

## The sixteen rows — delegation map and direct assertions

The checklist is mostly a *map of existing gates*. Where an item already names a
gate, the row delegates: it runs that gate and matches its verdict line rather
than re-implementing the check. Every row below was run by hand on 2026-09-28
(cwd = repo root, the same command the gate forms) and asserted against its own
`expect_exit`/`expect_last`: 9/9 matched.

| id | item (`SKILL.md` order) | class | the row runs / asserts | measured |
|---|---|---|---|---|
| E1 | Record mechanism and metadata | runnable | `bash corpus/surface-census.sh >/dev/null && bash corpus/drift-pins.sh` — **two** gates: `&&` carries the census exit status (its verdict line is discarded by the redirect), the pinned last line is drift's | exit 0, `DRIFT_PINS: CLEAN (files=15 symbols=20)` |
| E2 | After any intentional host-file change | by-hand | `manual-change:` the `--pin` decision and which `REPIN`/`MOVED` lines are acceptable is an authoring call; the drift gate itself is E1 | — |
| E3 | Quote command output only when it is metadata-only | by-hand | `authoring-duty:` separating a metadata block from pasted output is a writing judgement; `note` records the mechanisation nobody has built (a declared allow-list of quotable command shapes) | — |
| E4 | `refs` output: key names OK … ref paths stay out of artifacts | runnable | a scan for reference-shaped literals over `*.md`/`*.tsv`/`*.sh`, allowing three declared placeholder vault names (`vault` — the documented example shape, three lines — plus the `FakeVault`/`wal` fixtures); prints `REF_PATH_SCAN: hits=N excluded=E raw=R` and **counts only**, pinning both the post-allowlist count and the raw count so the allowlist cannot remove a hit silently | exit 0, `REF_PATH_SCAN: hits=0 excluded=5 raw=5` (before the exclusion fix: `hits=3`, see the landing table) |
| E5 | Before relying on a key inventory … `op-ref-probe.sh` | runnable | `bash corpus/op-ref-probe.sh` — the one **delegated** row whose delegate execs `op` (over generated plain-value fixtures, refusing any reference token before exec), so the deny-list on the row's own string does not cover it: the delegate's policy does, and E5's `note` says so | exit 0, `OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)` |
| E6 | Never paste `the-janitor run` output | by-hand | `authoring-duty:` no command can tell whether a value's class was checked before quoting; the masking contract itself is E5's probe (`corpus/knowledge/op-ref-consumption.md`) | — |
| E7 | Receipts/checksums bind *bytes*: state scope explicitly | by-hand | `authoring-duty:` the scope sentence is a writing duty; byte-binding is `tac-check`'s own offline gate (`corpus/knowledge/tac-evidence-integrity.md`) | — |
| E8 | Handoffs carry context + receipt *path*; `boundaries` is the vocabulary | runnable | `python3` over `~/.local/state/tac/handoff-status.json`: `credentials_in_evidence is False`, `target_authority_conferred is False`, `access_receipt` and `receipt_sha256` present — key names and booleans only | exit 0, `HANDOFF_STATUS: OK (boundaries=5 receipt=present sha=present)` |
| H1 | One request at a time — `client.lock` flock serializes machine-wide | runnable | the serialization **premise**: `flock 9` sites, the `exec 9>"$LOCK_FILE"` that opens the lock, and the `LOCK_FILE=` declaration in `~/.local/bin/the-janitor`, plus `client.lock`'s mode when it exists (absent tolerated — `prepare_state` recreates it, `corpus/knowledge/janitor-lifecycle.md`) | exit 0, `CLIENT_LOCK: flock=3 exec=3 declared=1 mode=600` |
| H2 | After `stop`, expect `AUTH_REQUIRED` … | by-hand | `runtime-behavior:` needs a stop + next-request cycle against a live handler; start/stop is operator scope and outside this gate | — |
| H3 | Keep `config_overlay` intact … the global config also reaches the handler | runnable | overlay keys (`enabled_providers`, `share`, `autoupdate`, `default_agent`) **and** that the global `~/.config/opencode/opencode.json` still parses with `agent`/`provider` | exit 0, `CONFIG_OVERLAY: OK (providers=1 share=disabled autoupdate=False global=parsed global_providers=absent)` |
| H4 | Never widen `janitor` agent permissions | runnable | the front-matter `permission:` block must be exactly `["*": deny, janitor_auth: allow]`, and `steps: 4` | exit 0, `JANITOR_PERMS: OK (entries=2 steps=4)` (before the parse fix: `DEFECT (entries=1 steps=4)`) |
| H5 | CDP port 9222 + musketeer profile shared with the kake fleet | by-hand | `cross-lane:` the lease is kake's surface, reported never adjudicated (`SCORECARD.md:180`) | — |
| H6 | Never put secret-adjacent text into a request | by-hand | `authoring-duty:` the durable consequence is E8/H7's territory and `transcript-scan.sh`; the duty is what a person types | — |
| H7 | Run `corpus/transcript-scan.sh` after any request … | runnable | `bash corpus/transcript-scan.sh`; `expect_exit` `0\|1\|2` and two accepted last lines, because exit 1 is `SKILL.md`-declared by design and after a legitimate `stop` + `rm -rf xdg-data` the DB is gone (surface-census classes `opencode.db*` `runtime`), where the scan exits 2 with `db not found`. Any *other* exit-2 cause still fails the row | exit 1, `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0) db=…` |
| H8 | Treat `127.0.0.1:40961` as unauthenticated handler access | runnable | `OPENCODE_SERVER_PASSWORD` occurrences in the CLI + client must be 0, no established socket may point at 40961, and a listener that is *not* on loopback fails the row while a loopback listener is reported (legitimate while the handler runs — the row's `note` says so) | exit 0, `CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0 established=0` |

Seven rows are by-hand, nine runnable — and of the nine, `delegated=3` and
`direct=6`. The delegated gates are `surface-census.sh` and `drift-pins.sh` (both
under E1, one row), `op-ref-probe.sh` (E5) and `transcript-scan.sh` (H7). The
other six runnable rows are assertions this file introduces, and every runnable
row was measured independently before this entry was written (values above).

## Round-15 landing table (same defects, measured both ways)

Six defects were found by running the gate against its own repository (and by
reading it against the brief), and all six are fixed at the revision this entry
quotes. The before column is measured on the first landed pair — the two *gate*
rows at `checklist-run.sh` `ead9f7308bbb`, the two *row* rows at
`checklist.tsv` `3a5f422595b5`, which is the order they were fixed in: the script
first, and the run then printed `ITEM-FAIL E4 (exit 1 want 0)` +
`ITEM-FAIL H4 (exit 1 want 0)` + `CHECKLIST_RUN: BROKEN (items=16 runnable=9
by_hand=7 failed=2)`, exit 1. The after column is `4a06a9f2a4e4` /
`28bd238e549c`. The gate's own repository is its first fixture, and it was red
until the last of these:

| defect | before | after |
|---|---|---|
| by-hand reason uniqueness built its input with `for …; do [[ class == by-hand ]] && printf …; done \| sort \| uniq -d` under `set -o pipefail` | the for-loop's last test returning 1 killed the script on the assignment: `bash corpus/checklist-run.sh` ⇒ **exit 1, no output at all** whenever the last TSV row was `runnable` (H8 was) | guarded (`… \| uniq -d) \|\| true` over a collected list) ⇒ `CHECKLIST_RATIO` + `CHECKLIST_RUN: CLEAN … failed=0`, exit 0 |
| last-line extraction `printf … \| grep -v '^[[:space:]]*$' \| tail -n 1` | `grep -v` exits 1 on empty output ⇒ the same silent death for any row whose check printed nothing | `awk 'NF { l = $0 } END { print l }'` ⇒ a silent row is `ITEM-LASTLINE R1 (want /^A1: OK$/ got '')`, exit 1 |
| H4 captured the front matter with `re.search(r'^---\n(.*?)\n---\n', t, re.S)`, whose group has no trailing newline | its block pattern could not match the final entry ⇒ `JANITOR_PERMS: DEFECT (entries=1 steps=4)`, exit 1, on a correct host file | `fm=(m.group(1)+'\n')` ⇒ `JANITOR_PERMS: OK (entries=2 steps=4)`, exit 0 |
| E4's reference-shaped sweep excluded only `op://FakeVault/` and `op://wal/` | `REF_PATH_SCAN: hits=3` — the three hits are the documented placeholder form `op://vault/<item>` at `corpus/knowledge/op-env-refs.md:14`, `corpus/lessons/round-5-aggregator-audit.md:19`, `corpus/transcript-scan.sh:202`, i.e. a real item reading red on a repository that leaks nothing | the allowlist is the three placeholder vault names (`vault\|FakeVault\|wal`) and the row now prints `hits=`, `excluded=` **and** `raw=` with both counts pinned (so a future shrink of the example set is a reviewed re-pin, not a silent pass) ⇒ `REF_PATH_SCAN: hits=0 excluded=5 raw=5`, exit 0 |
| `DENY_CHECK` was `op\.env\|op run\|op read\|op inject\|the-janitor start\|the-janitor stop` | the regex carried no `the-janitor run` and no `claim-ledger\.sh` alternative, so a row naming either passed the guard — and `ITEM-FAIL` echoes the failing row's output | now `…\|the-janitor run\|claim-ledger\.sh` ⇒ `POLICY row R1: check touches a denied surface (/…/)`, exit 2 (measured, both) |
| the bijection closed one direction only | two rows declaring one item produced `UNMATCHED-ITEM` for the orphaned item but nothing about the duplication | `DUPLICATE-ITEM <j> (2 rows declare it)` added ⇒ both directions report |

## §Bounds — what this gate does not do

1. **A runnable row verifies a premise, not the operator's duty.** `janitor.md`
   carrying `{"*": deny, janitor_auth: allow}` is not "you never widened
   `janitor`"; `flock 9` appearing in the CLI is not "one request at a time" was
   honoured; the overlay's keys are not "the handler loaded them". This is the
   round-13 relevance ceiling in checklist form, inherited from
   `corpus/knowledge/claim-ledger.md` bounds 17 and 25, not re-solved here. Each
   row's `note` names its premise so the reader can see how far the verdict
   reaches — and the §Contested-split paragraph above records that the boundary
   between premise and duty is a judgement, not a measurement.
2. **Nothing schedules the gate.** It is manual, like every other gate in this
   corpus (`SCORECARD.md:162`, `:220` "nothing schedules the six gates"); an item
   can stop holding while nobody looks. Round 15 changes *what a run can say*,
   not *when a run happens*.
3. **`transcript-scan.sh` exits 1 by design**, so H7 accepts `0|1|2` and pins
   **two** last lines: the count-bearing summary, and `transcript-scan: db not
   found: …` — the state `SKILL.md`'s own purge recipe (`stop` + `rm -rf
   xdg-data`) produces, where the scan exits 2 and the census classes
   `opencode.db*` as `runtime/absent`. A changed hit count is `ITEM-LASTLINE`, so
   the row asserts the verdict *and* the baseline; any other exit-2 cause fails.
   A row demanding exit 0 would paint a healthy host red — the round-8
   false-positive class the census records for `SKIP` too.
4. **No row may re-invoke `corpus/claim-ledger.sh`**, and the deny-list refuses
   one (`POLICY`, exit 2, measured). The ledger re-runs the rows a scorecard cites
   and skips only rows that re-invoke it (`corpus/knowledge/claim-ledger.md`
   bound 26, `SKIP-SELF`; a nested `verify` is refused outright), so a checklist
   row calling the ledger would make the two gates mutually re-entrant. The
   dependence is one-way and that is what `Reverify: R15-01` rests on: the
   *ledger* may carry a row that runs `bash corpus/checklist-run.sh` (this
   checklist never calls the ledger, so nothing recurses), while the checklist may
   not carry the ledger inside itself.
5. **`$CONFIG_DIR/op.env` bytes are never read, by any row.** The corpus rule
   that makes this true elsewhere holds here: `op.env` is pinned by mode, line
   count and dotenv *shape* with the hash withheld by policy
   (`corpus/knowledge/drift-gate.md`: "`op.env` is the only file where NOHASH is
   …"), `corpus/surface-census.tsv` records the note "env-ref file; values never
   read into an artifact", and the gate refuses a `check` naming `op.env`. A row
   wanting "the contract still holds" asks `op-ref-probe.sh` (E5), which reads a
   scratch fixture or a shape.
6. **The deny-list is a text guard, not a sandbox — and it only guards a row's
   own `check` string.** It is one regex over that string (`op\.env`,
   `op run|read|inject`, `the-janitor start|stop|run`, `claim-ledger\.sh`). It
   cannot see a path assembled at runtime, a differently spelled `op` invocation,
   or a row that reads some other secret file; and a *delegating* row is covered
   by its delegate's policy instead, which is why E5 can hand off to
   `op-ref-probe.sh` (the delegate execs `op run` over generated values and
   refuses any reference token before exec). The control is that the TSV is a
   reviewed, committed file — the bound the ledger states for its own allowlist
   (`corpus/knowledge/claim-ledger.md` bound 2).
7. **A failing row's output is echoed** (six lines, `tail -n 6`, prefixed
   `    | `). A row whose command prints a value therefore leaks it into the run
   log *when it fails* — which is why E4's scan prints counts only, and why "a
   check must print a verdict line and nothing secret" is written into the TSV
   header rather than left implicit. The echo is the diagnostic the reader needs
   and the leak surface the reader must respect.
8. **The bijection is a shape rule, not a relevance rule.** Swapping two rows'
   `lead`s keeps every count exact and turns the run green while each check now
   measures the other item — measured on a fixture: leads swapped ⇒
   `CHECKLIST_RUN: CLEAN (items=6 runnable=4 by_hand=2 failed=0)`, exit 0. The
   `note` column is the only place the premise is stated, and nothing reads it.
9. **The `by-hand` class is an explicit unverifiable set, not evidence of
   effort.** A class from a closed five, a ≥24-character reason and a uniqueness
   check reject the cheapest rubber stamp; they cannot reject a
   thoughtful-looking reason attached to a measurement nobody ever ran
   (`corpus/knowledge/claim-ledger.md` bounds 18, 21, 23).
10. **The ratio floor is coverage, not evidence.** The landed pair is 9 runnable
    of 16 with floor 8, so exactly **one** conversion of a runnable row to
    `by-hand` still satisfies the rule (8·2 ≥ 16) and a second fires `RATIO
    (runnable=7 floor=8 items=16)`. Which rows are runnable is a design choice the
    floor cannot audit (see the contested split).
11. **E1 discards the census's verdict.** The row redirects `surface-census.sh`
    to `/dev/null`, so only its exit status survives and the pinned last line is
    drift's. A census that failed while drift stayed clean is `ITEM-FAIL` with
    drift's clean summary printed beside it, plus six lines of (empty) output —
    evidence that names the wrong gate unless the reader knows the row.
12. **Delegated verdicts inherit delegated bounds.** `SURFACE_CENSUS: CLEAN`
    carries the census's exit-neutral `SKIP` (a locked database) and its
    enumeration limits; a green checklist row is green *to that depth*
    (`corpus/knowledge/surface-census.md` §Bounds). Same for the probe's
    fixture-only scope and the transcript scan's DB existence requirement.
13. **Rows are host-state claims.** H8's listener count is true of a stopped
    handler; a live session moves the DB floors and the transcript counts; H1
    tolerates an absent `client.lock` by design. Like `R11-06`, a row whose
    subject is host state needs re-baselining when the host legitimately changes,
    not a "regression" label (`corpus/knowledge/claim-ledger.md` bound 1).
14. **`expect_exit` widening is real.** The grammar is `N` or `A|B|C…`
    (`^[0-9]+(\|[0-9]+)*$`), so H7's `0|1|2` lets both a transcript scan that
    returns `CLEAN` and a post-purge `db not found` pass the exit half — the ERE
    carries the baseline, and the second accepted state is only safe because the
    row pins the *shape* of the missing-DB line too. A future row accepting more
    codes narrows the exit half further, and only review notices; the ledger's
    `R11-06` is the precedent for recording a firing gate's exit code instead of
    forcing 0.
15. **`--only` and `--ratio` narrow the question, and both can look clean over a
    failing checklist.** `--only` skips every row but the named one (the
    declaration audit still runs): on a fixture whose `R1` fails, the full run is
    `BROKEN (items=2 runnable=2 by_hand=0 failed=1)` exit 1 while `--only R2` is
    `CLEAN … failed=0` exit 0. `--ratio` runs *no* row at all: a copy with
    `expect_exit` mutated to `9` prints the identical
    `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6` line
    and exits 0 (measured), because the ratio line is the same line a clean and a
    broken run both print first. Neither is ever the verdict.
16. **Item text is not the item's meaning.** `extract_items` collapses each item
    into one line; a `lead` matches that collapsed text, so rewording an item
    across a line break can move a row from matched to `UNMATCHED-ITEM` with no
    semantic change. The prose stays the source of truth, which is the point —
    and also the fragility.
17. **The row timeout is a single TERM.** The runner is `timeout "$ROW_TIMEOUT"
    bash -c "${R_CHECK[$i]}"` — no `-k`, unlike `corpus/claim-ledger.sh`'s
    `timeout -k 5`. A check that traps and ignores TERM can hold the run past its
    declared bound; measured as `ITEM-FAIL R1 (exit 124 want 0) TIMEOUT` with
    `CHECKLIST_TIMEOUT=1` against a `sleep 5` row, which is the well-behaved case.
18. **`--selftest` proves the paths, not the repository.** The 34 cases rebuild
    scratch `SKILL.md`/TSV pairs (no sed-on-fixture), so they exercise the
    verdict vocabulary; the default wiring — the real `SKILL.md` section, the real
    TSV, the four delegated gates — is proven only by running the gate, which is
    why the landing table above is measured on the repo pair rather than on a
    fixture.

## Falsifiers (ranked: cheapest lie first)

Each was run on a scratch pair (`--tsv`/`--skill`) unless marked otherwise; the
observed verdict is quoted.

1. **Widen an `expect_last` ERE until a degraded summary still matches** — e.g.
   `^A1: ` instead of `^A1: OK$` against a check that prints `A1: DEGRADED` ⇒
   `CHECKLIST_RUN: CLEAN (items=6 runnable=4 by_hand=2 failed=0)`, exit **0**.
   Measured: the ERE is the row's whole oracle. The `lead` column is protected
   against exactly this (`DUPLICATE-LEAD`), `expect_last` is not.
2. **Swap two rows' `lead`s** (each check now measures the other item) ⇒ CLEAN,
   exit 0. Measured: relevance is not checked, only shape.
3. **Add a seventeenth `- [ ]` item to a scratch `SKILL.md`** ⇒ `UNDECLARED
   (items=7 rows=6)` + `UNMATCHED-ITEM 7 (no row declares it)` + `RATIO`-
   independent `CHECKLIST_RATIO: runnable=4/7 floor=4 by_hand=2 delegated=0 direct=4` ⇒ `BROKEN`,
   exit 1. Measured. This is the falsifier that makes "sixteen rows" mean "the
   prose list", not "a TSV someone wrote".
4. **Widen a `lead` until it matches several items** (`item text` in a six-item
   fixture) ⇒ `DUPLICATE-LEAD R1 (/item text/ matches 6 items)` + five
   `DUPLICATE-ITEM` lines ⇒ exit 1. Measured.
5. **Point two rows at one item** ⇒ `DUPLICATE-ITEM 1 (2 rows declare it)` +
   `UNMATCHED-ITEM 2 (no row declares it)` ⇒ exit 1, `failed=0` in the summary
   (a declaration defect is not a row failure). Measured.
6. **Set a runnable row's `expect_exit` to a value the check never returns** ⇒
   `ITEM-FAIL R1 (exit 0 want 3)` with the output tail ⇒ `BROKEN … failed=1`,
   exit 1. Measured. `exit 127` (a renamed delegated gate) gives
   `ITEM-FAIL R1 (exit 127 want 0)` with `bash: line 1: …: command not found`.
7. **Make a row print nothing** (`check` = `true`) ⇒ `ITEM-LASTLINE R1 (want
   /^A1: OK$/ got '')`, exit 1. Measured — and this is the case that killed the
   run silently before the fix (landing table).
8. **Put a secret-reading command in a check** (`cat op.env`) ⇒ `POLICY row R1:
   check touches a denied surface (/op\.env|op run|op read|op inject|the-janitor
   start|the-janitor stop|the-janitor run|claim-ledger\.sh/)`, exit 2, nothing
   executed. **Same line** for `bash corpus/claim-ledger.sh verify` (the recursion
   rule). Both measured.
9. **Convert runnable rows to `by-hand` until the floor breaks** — in a six-item
   fixture two runnable of six ⇒ `RATIO (runnable=2 floor=3 items=6)`, exit 1
   (that fixture also lost a row, so it printed `UNDECLARED (items=6 rows=5)`
   beside it; three of six still passes: `runnable=3/6 floor=3`, measured). On the
   repo pair the same arithmetic allows one conversion (8/16) and fires on the
   second.
10. **Duplicate a by-hand reason** ⇒ `DUPLICATE-REASON (authoring-duty: …|)`,
    exit 1. Measured. Shortening a reason below 24 characters or dropping its
    class is `POLICY … reason … is not \`<class>: <>=24 chars>\``, exit 2.
11. **Give a row a command that never exits** (`sleep 5` with
    `CHECKLIST_TIMEOUT=1`) ⇒ `ITEM-FAIL R1 (exit 124 want 0) TIMEOUT`, exit 1.
    Measured — see bound 17 for the single-TERM caveat.
12. **Narrow with `--only` and call it the verdict** ⇒ `--only R2` prints
    `CHECKLIST_RUN: CLEAN (items=2 … failed=0)`, exit 0, on the same fixture whose
    full run is `BROKEN … failed=1`. Measured: the cheapest way to make the gate
    *look* clean without changing anything it measures.
13. **Quote `--ratio` (or grep the ratio line) as the whole answer** ⇒ the line is
    byte-identical whether the rows hold or not: on a `--tsv` copy with
    `expect_exit` mutated to `9`, `--ratio` prints
    `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6` and
    exits 0, while the full run prints the same line *followed by* `ITEM-FAIL` and
    `BROKEN`. Measured: the shape line survived as the summary of a run that never
    happened.

## Reproduction (2026-09-28)

```bash
cd ~/projects/shokunin/kagi-shokunin
bash corpus/checklist-run.sh          # CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6
                                      # CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0), exit 0, ~2.1 s
bash corpus/checklist-run.sh --list   # CHECKLIST_LIST: rows=16 runnable=9 by_hand=7, exit 0
bash corpus/checklist-run.sh --ratio  # CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6, exit 0 — declaration only, no row runs
bash corpus/checklist-run.sh --selftest   # CHECKLIST_SELFTEST: PASS (34 cases), exit 0
bash corpus/checklist-run.sh --only H1    # one runnable row; BY-HAND <id> for a by-hand row; SETUP for an unknown id
bash corpus/checklist-run.sh --only E3    # BY-HAND E3 (authoring-duty: …), exit 0

# read one row's own command and run it the way the gate does (cwd = repo root):
row(){ awk -F'\t' -v id="$1" '$1==id{print $4}' corpus/checklist.tsv; }
bash -c "$(row E1)"   # DRIFT_PINS: CLEAN (files=15 symbols=20), exit 0
bash -c "$(row E4)"   # REF_PATH_SCAN: hits=0 excluded=5 raw=5, exit 0
bash -c "$(row H1)"   # CLIENT_LOCK: flock=3 declared=1 mode=600, exit 0
bash -c "$(row H4)"   # JANITOR_PERMS: OK (entries=2 steps=4), exit 0
bash -c "$(row H8)"   # CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0 established=0, exit 0
bash -c "$(row H7)"   # TRANSCRIPT_SCAN: HITS=2 (…), exit 1 by design (two accepted last lines: the HIT summary, or `db not found` after a purge)

# the fixture paths (what §Falsifiers measured): build a scratch pair, then mutate one field
d=$(mktemp -d)
{ printf '## Credential-hygiene checklist\n\nEvidence production:\n'
  printf -- '- [ ] alpha item\n- [ ] beta item\n- [ ] gamma item\n- [ ] delta item\n- [ ] epsilon item\n- [ ] zeta item\n'
  printf '\n## Next section\n'; } > "$d/SKILL.md"
printf 'R1\trunnable\talpha\tprintf "A1: OK\\n"\t0\t^A1: OK$\t-\talpha premise\nR2\trunnable\tbeta\tprintf "A2: OK\\n"\t0\t^A2: OK$\t-\tbeta premise\nR3\trunnable\tgamma\tprintf "A3: OK\\n"\t0\t^A3: OK$\t-\tgamma premise\nR4\trunnable\tdelta\tprintf "A4: OK\\n"\t0\t^A4: OK$\t-\tdelta premise\nR5\tby-hand\tepsilon\t-\t-\t-\tauthoring-duty: epsilon is a writing decision with no command shape\tepsilon reason\nR6\tby-hand\tzeta\t-\t-\t-\tcross-lane: zeta is owned elsewhere and only reported, never adjudicated\tzeta reason\n' > "$d/checklist.tsv"
bash corpus/checklist-run.sh --tsv "$d/checklist.tsv" --skill "$d/SKILL.md"
# → CHECKLIST_RATIO: runnable=4/6 floor=3 by_hand=2 delegated=0 direct=4 · CHECKLIST_RUN: CLEAN (items=6 runnable=4 by_hand=2 failed=0), exit 0
m(){ awk -F'\t' -v OFS='\t' "$1" "$d/checklist.tsv" > "$d/m.tsv"; bash corpus/checklist-run.sh --tsv "$d/m.tsv" --skill "$d/SKILL.md"; }
m 'NR==1{$4="true"}1'              # ITEM-LASTLINE R1 (want /^A1: OK$/ got ''), BROKEN failed=1
m 'NR==1{$5="3"}1'                 # ITEM-FAIL R1 (exit 0 want 3), BROKEN failed=1
m 'NR==1{$4="cat op.env"}1'        # POLICY row R1: check touches a denied surface (/…/), exit 2
m 'NR==1{$4="printf \"A1: DEGRADED\\n\"";$6="^A1: "}1'   # CLEAN — the ERE is the whole oracle
m 'NR==1{$3="beta"} NR==2{$3="alpha"}1'                  # CLEAN — leads swapped, relevance unchecked
CHECKLIST_TIMEOUT=1 m 'NR==1{$4="sleep 5"}1'             # ITEM-FAIL R1 (exit 124 want 0) TIMEOUT
m 'NR==1{$5="7"}1' >/dev/null   # this fixture's full run is BROKEN … failed=1, exit 1
bash corpus/checklist-run.sh --tsv "$d/m.tsv" --skill "$d/SKILL.md" --only R2   # CLEAN … failed=0, exit 0 — narrowed, not the verdict

# the delegated gates themselves
bash corpus/surface-census.sh      # SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0), exit 0
bash corpus/drift-pins.sh          # DRIFT_PINS: CLEAN (files=15 symbols=20), exit 0
bash corpus/op-ref-probe.sh        # OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6), exit 0
bash corpus/transcript-scan.sh     # TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0), exit 1 (by design)
```

Reverify: R15-01
