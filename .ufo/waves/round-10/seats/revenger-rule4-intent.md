# Rule 4 intent: command-bearing counts, not number-shaped prose

## Defect class and boundary

**One-sentence defect class:** Rule 4 catches a corpus entry that presents a factual, re-derivable measurement as a count while withholding the command (and, in the stronger formulation, its unit and date), so a reader cannot reproduce what was counted.

The faithful boundary is:

* **(a) Real defect — measured count with no command.** A number asserts an observed inventory/result (rows, files, lines, packages, occurrences, etc.); absent the counting command/date (and, per proposal P-u, unit), the claim is not re-derivable.
* **(b) Entity designation — not a measurement.** A number embedded in a name, task identifier, round label, lane number, “box 3”, or a compound noun naming an entity is not a count claim merely because it contains digits.
* **(c) Inline design arithmetic — not a measurement.** A plan or protocol computes a planned sample (`12 tasks × 2 conditions = 24 runs`) rather than reporting what happened. It should be judged as design text, not Rule 4.
* **(d) Falsified number quoted inside a correction — not a new count claim.** If an append-only correction quotes the old number in order to refute it, Rule 9 requires preserving that quotation; Rule 4 must not demand a command for the *quoted falsehood*. The collision is structural: Rule 4 sees digits, while Rule 9 deliberately preserves the historical text. The ledger explicitly calls this D-141 and says “a quoted-and-refuted number is not a count claim” (shokunin:.ufo/reports/AGGREGATE.md:1692-1696; D-141 at :1900).

## What round 1 actually found

The primary audits describe four different facts, not four identical “bad numbers”:

1. **kasegi — `275 claim packages`: (d) in a later correction, but its original defect was (a) plus store/unit ambiguity.** The audit re-ran three `claims/` counts: 274 program directories, 295 package directories, and 281 `status.json` files, and said “No counting rule yields 275” (kasegi-shokunin:corpus/lessons/round-1-aggregator-audit.md:43-49). The later ledger found the number itself was real in a *different store*: `find ~/Projects/bounties/evidence -maxdepth 2 -name status.json | wc -l` returned 275, while `claims/` had the three other populations (shokunin:.ufo/reports/AGGREGATE.md:348-360). Thus the motivating defect was a count with no command/store/unit, not invention. When a correction quotes “275” to explain and falsify it, that occurrence is class (d), not a second violation.
2. **kake — `20-row registry`: (a), a wrong measured count, not merely missing provenance.** The audit parsed `len(...fleet.config.json["sites"])` and observed 21 rows, with the denominator affecting “14 of 20” (kake-shokunin:corpus/lessons/round-1-aggregator-audit.md:42-50). This is a registry-row measurement and should carry the parse command/date/unit; it is not inline arithmetic.
3. **kake — `~40 clones`: (a), stale/wrong measured count.** `ls -1 ~/Projects/webzites/repos | wc -l` observed 50, versus the corpus’s “~40” (kake-shokunin:corpus/lessons/round-1-aggregator-audit.md:51-52). The defect is an unreproducible inventory measurement, not the tilde itself.
4. **kumitate — `scripts/ 74 entries`: (a), stale measured count, with a separate unit problem.** `ls scripts | wc -l` observed 82 (78 files + 4 dirs), and `find scripts/ufo-sighting-lib -type f | wc -l` observed 26 rather than 25 (kumitate-shokunin:corpus/lessons/round-1-aggregator-audit.md:51-54). “Entries” leaves file-vs-directory semantics unclear; the number also drifted. The audit separately records 93 src `.rs` files versus 102 in the whole crate and calls the src-only/whole-crate convention undocumented (kumitate-shokunin:corpus/lessons/round-1-aggregator-audit.md:58-60): that is the unit axis, not a command-only failure.

The round-2 aggregate confirms the three stale kake counts and the kumitate inventory count as reproduced defects, and records kasegi’s 275 as a cross-store conflation (shokunin:.ufo/reports/AGGREGATE.md:300-308, 348-360). The ledger’s §1–§10 framing matters: it records the command-reproduction method, distinguishes false pointers (F), wrong/unreproducible numbers (N), unverifiable claims (U), and scope defects, and later names r4’s false-positive classes explicitly (shokunin:.ufo/reports/AGGREGATE.md:106-135, 1691-1696).

## Current r4 ground truth (round-10 gate run)

Command run: `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json`; live worktrees at the gate’s printed revisions and dirty counts: kasegi `b021dc9`, dirty 1; kengaku `e171cdf`, dirty 4; kake `4214101`, dirty 6; kumitate `637d181`, dirty 7; kotoba `0f658ff`, dirty 11; kagi `2486643`, dirty 12. The command emitted 264 r4 findings in its JSON line (the run also reports 310 total findings); the examples below are adjudicated against the quoted source text, not accepted merely because the heuristic emitted them.

### Over-fire examples (not Rule-4 defects)

1. `kengaku-shokunin:corpus/knowledge/telemetry-run-design.md:27` — “**Phase 1 smoke**: 2 tasks × 2 conditions = 4 runs”. **(c)** planned design arithmetic.
2. `kengaku-shokunin:corpus/knowledge/telemetry-run-design.md:28` — “**Phase 2 core**: 12 tasks × 2 conditions = 24 runs”. **(c)** planned design arithmetic.
3. `kengaku-shokunin:corpus/knowledge/telemetry-run-design.md:29` — “**Phase 3 transfer**: 8–12 runs public slices only after mechanism visible.” **(c)** design range, not an observed census.
4. `kengaku-shokunin:corpus/knowledge/telemetry-run-design.md:30` — “**Floor**: 36–40 runs total.” **(c)** protocol floor.
5. `kotoba-shokunin:corpus/knowledge/anatomy-and-compression.md:28` — “wwkd principle 8 states `"~600 lines per module"`”. **(b)** the number is part of a named principle/design threshold, quoted as guidance, not a survey count; the actual survey source command is separately stated at :24.
6. `kotoba-shokunin:corpus/knowledge/anatomy-and-compression.md:29` — “No surveyed file exceeds 392.” **(a)** would be a real measured negative/count, but in context the gate’s number-shaped match is not a bare count defect: it is a conclusion immediately backed by the explicit survey command at :24 and is not the missing-command class.
7. `kake-shokunin:corpus/knowledge/ghp-subpath-spotcheck.md:37` — “~30 lines of python”. **(c)** implementation-size estimate for a proposed procedure, not measured corpus inventory.
8. `kumitate-shokunin:corpus/knowledge/remaining-scripts-census.md:1` — “Remaining scripts census — S8 (60 members)”. **(b)** S8 is an entity/registry designation.
9. `kumitate-shokunin:corpus/knowledge/remaining-scripts-census.md:4` — “S7 (`remaining scripts`, 69 members …)”. **(b)** historical registry-family designation; the line names what S7 means rather than silently asserting a fresh count.
10. `kumitate-shokunin:corpus/knowledge/remaining-scripts-census.md:13` — “The 69 count is unchanged: it is now 9 + 60.” **(c)** explicit partition arithmetic explaining a registry split; not an uncommanded inventory claim.

These are genuine current r4 findings from the gate JSON’s `CR-<repo>-r4-*` records, but a human adjudicator should not label them violations under the intent above. (The gate’s own report names compound nouns and design arithmetic as declared false-positive classes: shokunin:.ufo/reports/AGGREGATE.md:1691-1696.)

### Clear defects

1. `kake-shokunin:corpus/knowledge/fleet-registry.md:5` — “`len(sites)` = **21 rows** — status: 12 live / 3 pruned / 3 broken / 3 queued”. **(a)** This is an observed registry census. It names `len(sites)` textually but does not give the executable command/date required by Rule 4; the round-1 audit’s command is the missing re-derivation boundary.
2. `kasegi-shokunin:corpus/README.md:42-44` — “DATA-half censuses (**1088 records, 280 packages, 592 evidence dirs, 7227 telemetry lines, 31 autopsies**…)”. **(a)** multiple asserted current measurements with no command beside them. Each has a unit, but no command/date; this is exactly the real r4 class.
3. `kake-shokunin:corpus/lessons/round-1-aggregator-audit.md:61` — “Reconcile every doc to **21 rows**”. **(d)** when read as a correction/lesson quoting the already adjudicated count, it is not a new census; the actual defect is the source claim at `kake-shokunin:corpus/knowledge/fleet-registry.md:8` (“20 rows”). This illustrates why a literal regex over correction prose over-fires.
4. `kumitate-shokunin:corpus/lessons/round-1-aggregator-audit.md:51-54` — “`scripts/` **74 entries**… Observed: `ls scripts | wc -l` = **82**…”. **(d)** the first number is quoted inside an append-only correction that supplies the command and falsifies it; Rule 9 requires retaining it. The original lane-report claim was (a), but this correction occurrence is D-141-like.
5. `kake-shokunin:corpus/knowledge/fleet-registry.md:7-9` — “Audit correction: round-1 said **‘20 rows’** — the registry has **21**”. **(d)** quoted-and-refuted historical count plus corrected result; a regex sees two numbers, but Rule 9’s correction entry is structurally required and should not itself be failed.
6. `kumitate-shokunin:corpus/lessons/round-1-aggregator-audit.md:55-60` — “`~80% of SKILL.md content` — no counting method given”. **(a)** measured proportion with no measurement command/method; it is not a task identifier or design arithmetic.

The current gate’s concrete revisions/dirty stamps above are the measurement identity. No claim here substitutes the round-9 frozen revision: the run was explicitly against round-10 selector live worktrees.

## Unit-before-command warning

Ledger proposal P-u says a count must name its **unit** as well as its command: lines, occurrences, and files produced four different “correct” kagi numbers in one wave (shokunin:.ufo/reports/AGGREGATE.md:1869-1874). A command alone cannot decide whether `wc -l` means physical lines, matching occurrences, or files containing a match. The kumitate 74/82 example has the same issue: “entries” could mean directory entries (82), files (78), or recursive files (and `ufo-sighting-lib`’s 25/26 depends on tree and file predicate). Unit ambiguity is therefore a separate (a)-adjacent defect, not permission to classify every number-shaped phrase as Rule 4.

## Recommended deciding tests

* **Class (a), measured count:** violation only when prose asserts an observed inventory/result (`N files`, `N rows`, `N occurrences`, `N lines`, `N packages`, percentages/count ratios presented as measured) and no nearby executable command/date (and no explicit unit). Faithful signal: a result claim whose evidence cannot be re-run. Regex artefact: any numeral followed by a count noun, especially inside a citation correction, table arithmetic, or quoted historical claim.
* **Class (b), entity designation:** exempt identifiers and names (`task 27`, `S8`, round 12, box 3, `r4`, “principle 8”). Faithful signal: the number labels a stable object/section/registry key rather than quantifying a population. Regex artefact: digit + noun alone without checking syntactic role.
* **Class (c), inline design arithmetic:** exempt planned equations, ranges, budgets, and sample plans (`12 tasks × 2 conditions = 24 runs`, `36–40 runs floor`). Faithful signal: future/modal/design markers (`phase`, `plan`, `floor`, `after`, `will`, `proposed`) or explicit arithmetic operators. Regex artefact: treating every `N × M = K` or range as an observed count.
* **Class (d), quoted correction:** exempt a number inside an append-only correction when nearby prose marks it as old/quoted/wrong and supplies the correction/evidence. Faithful signal: `said`, `earlier`, `correction`, `observed`, `wrong`, `not X`, `instead`, or a lesson’s correction section, plus Rule 9’s new-entry context. Regex artefact: flagging the historical number while ignoring the correction’s command; this is the D-141 structural collision.

For any surviving (a) finding, the adjudicator should demand the complete tuple `<number> — <unit> — <command> <date>` and retain the lane revision/tree and dirty count alongside the run, as required by the round-10 evidence contract (shokunin:.ufo/waves/round-10/CONTEXT.md:71-81).