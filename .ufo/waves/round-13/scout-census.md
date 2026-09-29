# scout — round-13 census extension

Lane seat: `ScoutCensus` (scout, round-13 `protocol` wave). Artifact: `.ufo/waves/round-13/scout-census.md`.
Companion artifact: `.ufo/waves/round-13/obligation-census-r13.tsv` (the deliverable; 170 lines = header + 169 rows: 93 legacy + 76 new — 63 from the first pass and 13 pinning the Sibling-mint bullet that landed while this artifact was being written, §Revision B).

**Scope.** Extend `.ufo/waves/round-11/obligation-census.tsv` (93 rows) so that the round-13
compaction of `PROTOCOL.md` can be verified against the *gate standard* and the *seven round-12
pins*, not just the round-11 obligations. Nothing outside `.ufo/waves/round-13/` was written;
`PROTOCOL.md` and `.ufo/waves/round-11/` are untouched (byte compared below).

**Method.** Rows are appended, never edited: `cat round-11/obligation-census.tsv <new rows>` is the
only construction step, so the first 94 lines are byte-identical by construction and by `diff`.
Each new row was derived by reading the rule in `PROTOCOL.md`, then choosing the **longest
single-line span of that rule's operative words** that `grep -E` can match. Every predicate was
executed against the live file and required to match **exactly one line, inside the body**
(`< 502` on the live revision; the `## Appendix` heading is at line 502 today — it was 487 before the
revision-B insert), so no new row leans on the appendix digest.

**Id convention.** Prefixes continue each section's existing family: `G*` = `## Gate standard`
(previously uncovered), `P*` = the round-robin pins (live in `## Round-robin rounds` and its step-4
semantics), `V*` continues `## Fleet-2 conventions` (`V1`–`V5` are the legacy rows). The `P` series
starts at `P11` as the round-13 brief specifies; no id collides with a legacy row. `R52` continues the
legacy `R` family (whose last row is `R51`) and pins the integrator's write-scope count — it exists
because legacy row `R31` describes a superseded count (see §Legacy rows). `L8`–`L20` continue the
`Lifecycle` family (`L1`–`L7` are legacy rows) and pin the lane-initiated **Sibling mint** bullet that
`2d19a64` added — the one rule in the live file that was census-blind until then (§Revision B).

| Round-12 pin (`.ufo/reports/round-12/protocol.md` §Protocol amendments) | rows |
|---|---|
| Row identity / `lane_rounds` never re-keys / `unadjudicable` legacy rows | P11, P12, P13, P14 |
| Orphaned-report resolution order + re-grade-to-`failed` condition + aggregator-`corpus/` exclusion | P15, P16, P17, P18, P19 |
| Filed-report correction form = erratum appended after the filed bytes, never a rewrite | P20, P21, P29 |
| `progressing-weak` as a third stale-lane grade | P22, P23 |
| L0 append-only + integrator durability owner + cite-by-lane-and-round | V6, V7, V8, V9, V10, V11 |
| `in-flight` ended only by a *landed* report | P24, P25 |
| `supersedes.entry` disambiguator + ambiguous-triple rule | P26, P27, P28 |

`## Gate standard` (lines 361–400 on the live revision; 346–384 at revision A) is covered by
**G1–G37**: G1–G26 are the clause rows (drawn from the brief's twelve required items, split where a
single line cannot carry two duties), G27–G37 are the audit-driven closures named in §Weak-predicate
self-audit.

**Measurement block** — two revisions, because `PROTOCOL.md` moved while this artifact was being
written (`2d19a64`, the Sibling-mint insert; see §Revision B). All row tables below quote the **live
(revision B)** line numbers.

| quantity | command | revision A (`e275d4a`) | revision B (live, `2d19a64`) |
|---|---|---|---|
| target length | `wc -l -c PROTOCOL.md` | `526 49269` | `541 50603` |
| target digest | `sha256sum PROTOCOL.md` | `22cb61ce89ce6af42dfb7b753d952ca0cbc7a22532c5a01b0c9aca72b8ac4638` | `e1797e2b01539c4b1b60015f005c37352256d3cecbbfec1021fd3b22a7005fe6` |
| target digest (md5, the label peers quote) | `md5sum PROTOCOL.md` | `63de15a37a42ce57decb951a7e8aa2f0` | `444667c4a69f5998f9abb957a68a4343` |
| body inline round refs (budget: unchanged) | `awk 'NR<PL' PROTOCOL.md \| grep -o 'round-[0-9][0-9.]*' \| wc -l` | `4` (`NR<487`) | `4` (`NR<502`) |
| appendix heading | `grep -n '^## Appendix' PROTOCOL.md` | line `487` | line `502` |
| census size | `wc -l -c .ufo/waves/round-13/obligation-census-r13.tsv` | `157 18606` (156 rows) | `170 20274` (169 rows) |
| census digest | `sha256sum .ufo/waves/round-13/obligation-census-r13.tsv` | `b74416e40d87428292ba2e128a00cccd429a37746bd1b4bf52142fed2cb33549` | `ce6d0ef44ab5ed66391e708b7d8aa5a0ead599f312ed880fda05ad4a5c4c2d99` |

The legacy census is unchanged in both revisions:
`sha256sum .ufo/waves/round-11/obligation-census.tsv` →
`ad70706665fcc7ed9e6473a1db1830db0ea1c05e00d42fe5d3b9ba0f01b222f8` (94 lines, `9706` B).

## Revision B — `PROTOCOL.md` moved while this artifact was being written

At 22:5x the file changed under this seat: `2d19a64` added a **Sibling mint** bullet at lines 23–37
(15 lines, `## Lifecycle`), so every line from 23 on shifted `+15`, the appendix heading moved
`487 → 502`, and the file grew `526 → 541` lines / `49269 → 50603` B. Measured re-measurement on the
new revision, not assumption:

| check | command | observed |
|---|---|---|
| both censuses still pass | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md [census]` | extended `169/169`, legacy `93/93`, both exit 0 |
| every new row still lands on exactly one body line | per-row match sweep over the live file | 76 of 76 rows, one match each, none `>= 502` |
| the new bullet was census-blind before this pass | delete lines 23–37, re-run | `156/156` extended and `93/93` legacy — the whole bullet could be deleted with the census green |
| the new bullet is now guarded | same deletion, after `L8`–`L20` | `156/169`, **13 MISSING** (`L8`–`L20`), exit 1 |

`L8`–`L14` are the clause rows for the bullet (mint bar; roster-scan record; `MINT.md` and its
required content; ≥3 verified rounds; probation `not as a roster row`; the write/roster screen);
`L15`–`L20` are the audit-driven closures that stop the wrapped halves of the same bullet from being
deletable (the *no existing province owns* bar, the scan-record-as-evidence clause, the
operator-adds-rows-only-afterwards clause, the write-screen's object, and the probation clause's
subject and location). Nothing else in the artifact changed with the revision: the same 63 rows,
re-measured, still match one body line each.

## New rows (76)

Every row below was checked the same way: the predicate matches one body line, never an appendix
line. Obligation text is the rule as `PROTOCOL.md` states it today.

| id | section | obligation | predicate | PROTOCOL.md line matched (revision B, `2d19a64`) |
|---|---|---|---|---|
| G1 | Gate standard | A gate is a committed, re-runnable verdict script a lane owns | `is a committed, re-runnable verdict script a lane owns` | 363: A **gate** is a committed, re-runnable verdict script a lane owns: it reads surfaces, compa… |
| G2 | Gate standard | A gate reads surfaces and compares them against expected values persisted in its own repo | `expected values persisted in its own repo` | 364: against expected values persisted in its own repo, and returns a verdict. A tool that canno… |
| G3 | Gate standard | A tool that cannot fail is a probe | `A tool that cannot fail is` | 364: against expected values persisted in its own repo, and returns a verdict. A tool that canno… |
| G4 | Gate standard | A tool that cannot fail is registered as a probe | `probe.., and is registered as one` | 365: a **probe**, and is registered as one. |
| G5 | Gate standard | Verdict map: 0 = clean and 1 = failed fleet-wide | `= .clean. and .1. = .failed. fleet-wide` | 367: - **Verdict.** `0` = `clean` and `1` = `failed` fleet-wide; every other code a gate exits (… |
| G6 | Gate standard | Every other exit code is declared in the registry entry and mapped onto clean\|failed\|could-not-evaluate | `is declared in its registry entry and mapped onto .clean \| failed \| could-not-evaluate.` | 368: `64`, …) is declared in its registry entry and mapped onto `clean \| failed \| could-not-eval… |
| G7 | Gate standard | An undeclared nonzero code reads as could-not-evaluate | `undeclared nonzero code reads as .could-not-evaluate.` | 369: and an undeclared nonzero code reads as `could-not-evaluate`. Nothing else is pinned: a gat… |
| G8 | Gate standard | Nothing else is pinned: a gate's own vocabulary stays lane-owned; the section governs the outer interface only | `stays lane-owned, and this section` | 370: vocabulary — WARN vs HIT, a missing baseline, finding kinds — stays lane-owned, and this se… |
| G9 | Gate standard | Self-test runs over isolated fixtures, no live-tree write, asserting both the exit code and a stable expected finding-id | `no live-tree write\) asserting both the exit code and a stable expected finding-id` | 373: network, no live-tree write) asserting both the exit code and a stable expected finding-id,… |
| G10 | Gate standard | Self-test expected values are committed in the owning repo and independent of the recomputation | `committed in the owning repo and independent of the recomputation` | 374: the expected values committed in the owning repo and independent of the recomputation. The … |
| G11 | Gate standard | The self-test flag spelling is the lane's | `spelling is the lane's` | 375: spelling is the lane's (`--selftest`, `--self-test`, `run_selftest()`) and the registry rec… |
| G12 | Gate standard | A helper-only or model-only self-check does not satisfy the self-test clause | `helper-only or model-only self-check does not satisfy` | 376: a helper-only or model-only self-check does not satisfy this clause. |
| G13 | Gate standard | Self-test green is capability, not a measurement | `Self-test green is capability, not a measurement` | 377: - **Two evidences.** Self-test green is capability, not a measurement (§Evidence standard).… |
| G14 | Gate standard | A gate over a mutable fleet artifact also ships a run over a committed input snapshot with its committed expected verdict | `also ships a run over a committed input snapshot` | 378: whose verdict depends on a mutable fleet artifact also ships a run over a committed input s… |
| G15 | Gate standard | A verdict names the revision it was measured against | `A verdict names the revision it was measured against` | 380: run. A verdict names the revision it was measured against: a gate grades the tree it runs o… |
| G16 | Gate standard | Registry rows live in each lane's SKILL.md, with the fields name, gate\|probe, entry command, verdict map, self-test command and spelling, pinned-value path, write scope, owner | `the rows live in each lane's .SKILL.md.: name,` | 382: - **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name, |
| G17 | Gate standard | The aggregator ledger stays the routed-defect queue, not a second inventory; a fleet index is pointers to lane rows, never copied expected values | `fleet index is pointers to lane rows, never copied expected values` | 385: second inventory; a fleet index is pointers to lane rows, never copied expected values. |
| G18 | Gate standard | Scope: read-only over surfaces it does not own, and it never acts on an external surface | `Read-only over surfaces it does not own, and it never acts on an external surface` | 386: - **Scope.** Read-only over surfaces it does not own, and it never acts on an external surf… |
| G19 | Gate standard | A verdict is lane-local evidence and never stands in for the native judge | `never stands in for the native judge` | 389: (`loop_stop`/`mission_goal`) and never stands in for the native judge. |
| G20 | Gate standard | A verdict never defines the host runtime's stop conditions | `never defines the host runtime's stop conditions` | 388: local-first). A verdict is lane-local evidence: it never defines the host runtime's stop co… |
| G21 | Gate standard | A red gate is a conformance defect recorded in the round notes and routed to its owner; status-neutral unless the round's rules already prescribe failed | `status-neutral unless the round's rules already prescribe .failed.` | 391: to its owner — status-neutral unless the round's rules already prescribe `failed`; gate red… |
| G22 | Gate standard | Gate redness is never the marker predicate | `never the marker predicate` | 392: never the marker predicate, since step 1 grades marker-versus-real-report first and only a … |
| G23 | Gate standard | The integrator verifies a gate's committed evidence | `The integrator verifies a gate's .committed evidence.` | 393: invokes `failed`. The integrator verifies a gate's *committed evidence* (self-test tally, |
| G24 | Gate standard | The integrator does not execute a sibling's gate | `it does not execute a sibling's gate` | 394: frozen-run verdict, the revision measured); it does not execute a sibling's gate, whose |
| G25 | Gate standard | Delivery is the re-read duty, not the driver's prompt template; the integrator names the exact lane_prompt() addition | `the integrator names the exact .lane_prompt\(\)` | 397: template (one of five child-lane items): the integrator names the exact `lane_prompt()` add… |
| G26 | Gate standard | Closure grades no gate conformant until its registry row exists in the lane's own SKILL.md | `grades no gate conformant until its registry row exists` | 398: in its round report, and closure grades no gate conformant until its registry row exists in… |
| G27 | Gate standard | Nothing else is pinned: a gate's own vocabulary is the only thing left lane-owned; no gate breaks on adoption | `Nothing else is pinned` | 369: and an undeclared nonzero code reads as `could-not-evaluate`. Nothing else is pinned: a gat… |
| G28 | Gate standard | A gate reads surfaces and compares them against expected values | `it reads surfaces, compares them` | 363: A **gate** is a committed, re-runnable verdict script a lane owns: it reads surfaces, compa… |
| G29 | Gate standard | Self-test runs over isolated fixtures (temp trees) | `over isolated fixtures .temp trees` | 372: - **Self-test.** Every gate exposes a self-invocation mode over isolated fixtures (temp tre… |
| G30 | Gate standard | The registry records the self-test flag spelling | `and the registry records it` | 375: spelling is the lane's (`--selftest`, `--self-test`, `run_selftest()`) and the registry rec… |
| G31 | Gate standard | The frozen run carries its committed expected verdict | `with its committed expected verdict` | 379: with its committed expected verdict, so a later hand-edit of that artifact contradicts the … |
| G32 | Gate standard | The registry schema is this section's | `The schema is this section's` | 382: - **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name, |
| G33 | Gate standard | The aggregator ledger stays the routed-defect queue, not a second inventory | `The aggregator ledger stays the routed-defect queue` | 384: pinned-value path, write scope, owner. The aggregator ledger stays the routed-defect queue,… |
| G34 | Gate standard | A verdict is lane-local evidence | `A verdict is lane-local evidence` | 388: local-first). A verdict is lane-local evidence: it never defines the host runtime's stop co… |
| G35 | Gate standard | Gate redness is the subject of the never-the-marker-predicate ban | `gate redness is` | 391: to its owner — status-neutral unless the round's rules already prescribe `failed`; gate red… |
| G36 | Gate standard | The integrator's evidence check is the self-test tally | `self-test tally` | 393: invokes `failed`. The integrator verifies a gate's *committed evidence* (self-test tally, |
| G37 | Gate standard | The aggregator ledger is not a second inventory; the fleet index carries pointers, never copied expected values | `second inventory; a fleet index is pointers` | 385: second inventory; a fleet index is pointers to lane rows, never copied expected values. |
| L8 | Lifecycle | Any lane may mint a sibling when it finds a domain demand no existing province owns | `any lane may mint a sibling when it finds a domain demand` | 23: - **Sibling mint (lane-initiated)** — any lane may mint a sibling when it finds a domain de… |
| L9 | Lifecycle | The minting lane's roster-map scan record is part of the mint evidence | `records the roster map it decided against` | 25: `PROVINCE.md` and records the roster map it decided against — that scan record is part of t… |
| L10 | Lifecycle | The sibling seed includes a MINT.md stating the reasoning, cause, demand instances, rejected roster fit and domain boundary | `plus a .MINT.md. stating the` | 28: SHONEN.md from the canonical template, AGENTS.md, LOG.md) plus a `MINT.md` stating the |
| L11 | Lifecycle | MINT.md records the demand instances with evidence pointers | `demand instances with evidence pointers` | 29: reasoning, cause, demand instances with evidence pointers, the rejected roster fit, and the |
| L12 | Lifecycle | The sibling self-iterates through at least three verified rounds before roster rows exist | `self-iterates through at least three verified rounds` | 32: lacks the route map) and self-iterates through at least three verified rounds building |
| L13 | Lifecycle | Probation state is recorded in rounds[].notes meanwhile, not as a roster row | `not as a roster row` | 35: `rounds[].notes` meanwhile, not as a roster row. The minting lane never writes outside its … |
| L14 | Lifecycle | The minting lane never edits MANIFEST.json roster or a sibling's post-seed content | `it never edits .MANIFEST.json. roster or a sibling's` | 36: repo + the new sibling's seed files; it never edits `MANIFEST.json` roster or a sibling's |
| L15 | Lifecycle | The mint bar is a domain demand no existing province owns (the object of the scan) | `existing province owns` | 24: existing province owns. Steps, in order: (a) the minting lane scans `MANIFEST.json` + every |
| L16 | Lifecycle | The roster-map scan record is itself mint evidence | `mint evidence` | 26: mint evidence; (b) it creates the sibling's own repo dir `{id}-shokunin/` on this host and … |
| L17 | Lifecycle | Only after those rounds land does the operator add the MANIFEST.json roster row and ROADMAP.md table row | `only after those rounds land does the operator add` | 33: `corpus/` + `PROVINCE.md`; (d) only after those rounds land does the operator add the |
| L18 | Lifecycle | The minting lane never writes outside its own repo plus the new sibling's seed files | `repo \+ the new sibling's seed files` | 36: repo + the new sibling's seed files; it never edits `MANIFEST.json` roster or a sibling's |
| L19 | Lifecycle | Probation state is recorded in rounds[].notes | `probation state is recorded in` | 34: `MANIFEST.json` roster row and `ROADMAP.md` table row — probation state is recorded in |
| L20 | Lifecycle | The probation record's location is rounds[].notes | `rounds\[\].notes. meanwhile` | 35: `rounds[].notes` meanwhile, not as a roster row. The minting lane never writes outside its … |
| P11 | Step4 | Row identity: the row names the lane-round it describes, lane-round (<id>, round) | `The row describes lane-round` | 282: what makes such a row falsifiable. The row describes lane-round `(<id>, round)`: `lane_roun… |
| P12 | Step4 | lane_rounds annotates the row and never re-keys it | `never re-keys it` | 283: annotates it and never re-keys it, so last-wins is computed over `(id, entry.round)`; readi… |
| P13 | Step4 | Last-wins is computed over (id, entry.round), not over lane_rounds | `last-wins is computed over .\(id, entry.round\).` | 283: annotates it and never re-keys it, so last-wins is computed over `(id, entry.round)`; readi… |
| P14 | Step4 | Pre-fleet-2 fleet-keyed entries carry no lane_rounds and are unadjudicable as lane-rounds | `carry no .lane_rounds. and are .unadjudicable. as lane-rounds` | 285: fleet-keyed entries, which carry no `lane_rounds` and are `unadjudicable` as lane-rounds |
| P15 | Step4 | An orphaned report is resolved in order: the lane's own respawn inherits and lands it first | `is resolved in order: the lane's own respawn inherits and lands it` | 117: report is resolved in order: the lane's own respawn inherits and lands it; the integrator s… |
| P16 | Step4 | The integrator sweeps an orphaned report only after a successor mission also terminates without landing it | `the integrator sweeps it` | 117: report is resolved in order: the lane's own respawn inherits and lands it; the integrator s… |
| P17 | Step4 | The orphaned-report resolution order never reaches aggregator-owned corpus/ files | `never reaches aggregator-owned` | 120: placeholders and all, into a permanent object, and the order never reaches aggregator-owned |
| P18 | Step4 | A terminated lane-round with an unlanded report is recorded on its termination evidence with the durability debt named | `recorded on its termination evidence with the durability debt named` | 122: but is unlanded is recorded on its termination evidence with the durability debt named, and… |
| P19 | Step4 | That lane-round is re-graded failed for want of a landed report if the successor never lands it | `re-grades it .failed. for want of a landed report if the successor never lands it` | 123: pass re-grades it `failed` for want of a landed report if the successor never lands it. A f… |
| P20 | Step4 | A filed-report correction lands as an erratum appended after the filed bytes in a new commit and naming the text it supersedes | `appended after the filed bytes in a new commit and naming the text it supersedes` | 125: appended after the filed bytes in a new commit and naming the text it supersedes — never a … |
| P21 | Step4 | A filed report is never rewritten — labelled or silent | `never a rewrite` | 125: appended after the filed bytes in a new commit and naming the text it supersedes — never a … |
| P22 | Step4 | Sibling-authored activity alone is a third grade, progressing-weak: named as such in the row | `sibling-authored activity alone is a third grade, .progressing-weak.: named as such` | 159: child repo — so sibling-authored activity alone is a third grade, `progressing-weak`: named… |
| P23 | Step4 | progressing-weak is never called progressing, and never silent or failed on its own | `never called progressing, and never silent or .failed. on its own` | 160: in the row, never called progressing, and never silent or `failed` on its own. Commit spars… |
| P24 | Step4 | in-flight is decided from the absence of both a complete line and a landed report | `the absence of both a .complete <lane> round=N. line and a .landed. report` | 261: from the absence of both a `complete <lane> round=N` line and a *landed* report — an |
| P25 | Step4 | An uncommitted file at the report path does not end in-flight | `uncommitted file at the report path does not end .in-flight.` | 262: uncommitted file at the report path does not end `in-flight`, however it fires the driver's |
| P26 | Step4 | Two corrections sharing round+type+date name no unique row | `share round\+type\+date that triple names no unique row` | 298: Where two corrections share round+type+date that triple names no unique row, so `supersedes` |
| P27 | Step4 | supersedes MAY also carry entry (the array index) as the disambiguator | `MAY also carry .entry.` | 299: MAY also carry `entry` — the array index, stable precisely because the array is append-only… |
| P28 | Step4 | A gate treats a correction that needs the disambiguator and omits it as ambiguous | `needs the disambiguator and omits it as ambiguous` | 300: and a gate treats a correction that needs the disambiguator and omits it as ambiguous |
| P29 | Step4 | The no-rewrite ban covers the filed bytes — labelled or silent | `of the filed bytes, labelled or silent` | 126: of the filed bytes, labelled or silent. |
| R52 | Step4 | The integrator's main-repo writes expand by exactly five (the count is normative, and the legacy R31 description still says three) | `expand by exactly five` | 188: `PROTOCOL.md`/`ROADMAP.md`/`SCORECARD.md`/`LOG.md`/its own report, and expand by exactly fi… |
| V6 | Fleet-2 | L0 file is append-only in the LOG.md sense: a restatement or correction appends a new line naming the superseded one | `appends a new line naming the superseded one` | 496: appends a new line naming the superseded one and never rewrites a filed line, and the opera… |
| V7 | Fleet-2 | L0 filed lines are never rewritten; the operator's in-place answers are never a lane write | `never rewrites a filed line` | 496: appends a new line naming the superseded one and never rewrites a filed line, and the opera… |
| V8 | Fleet-2 | Cite an L0 question by lane + round + its opening words | `by lane \+ round \+ its opening words` | 497: in-place answers are never a lane write. Cite a question by lane + round + its opening word… |
| V9 | Fleet-2 | L0 questions are never cited by line number, which moves as the queue grows | `never by line number` | 498: never by line number: the queue grows, so every line number moves. Its durability owner is … |
| V10 | Fleet-2 | L0 durability owner is the integrator, which commits it with the round's integration commit | `integrator, which commits it with the round's integration commit` | 499: integrator, which commits it with the round's integration commit — a lane's appended questi… |
| V11 | Fleet-2 | The L0 durability owner framing: its owner is an integrator, not a lane | `Its durability owner is the` | 498: never by line number: the queue grows, so every line number moves. Its durability owner is … |

## Verification

Both runs are the round-11 verifier, unmodified, against the live `PROTOCOL.md`
(`2d19a64`: sha256 `e1797e2b…`, md5 `444667c4…`, 541 lines). The revision-A runs (526 lines,
sha256 `22cb61ce…`) returned the same verdicts on the then-current file — 156/156 and 93/93 — and the
revision-B numbers below are the ones this artifact's tables describe.

Run 1 — extended census (tail; the 164 preceding lines are `PASS <id>`):

```
$ sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md .ufo/waves/round-13/obligation-census-r13.tsv | awk 'NR>=165'
PASS V7
PASS V8
PASS V9
PASS V10
PASS V11

169/169 obligations found; 0 MISSING
$ echo $?
0
```

Observed: `grep -c '^PASS'` → `169`; `grep -c '^MISS'` → `0`; summary line
`169/169 obligations found; 0 MISSING`; **exit 0** (the verifier's last statement is
`[ "$miss" -eq 0 ]`).

Run 2 — the untouched 93 legacy rows, default census path:

```
$ sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md | awk 'NR>=90'
PASS V2
PASS V3
PASS V4
PASS V5

93/93 obligations found; 0 MISSING
$ echo $?
0
```

Run 3 — legacy prefix of the new file, byte-compared to the round-11 file:

```
$ diff <(sed -n '1,94p' .ufo/waves/round-13/obligation-census-r13.tsv) .ufo/waves/round-11/obligation-census.tsv
$ echo $?
0
```

Empty output, exit 0: the 93 legacy rows are unmodified and in order (they are a `cat` prefix, and
the diff proves it). Supporting checks, same session:

```
$ awk -F'\t' 'NF!=4{print "BADFIELDS",NR}' .ufo/waves/round-13/obligation-census-r13.tsv   # no output
$ awk -F'\t' 'NR>1{print $1}' … | sort | uniq -d                                            # no output (no duplicate ids)
```

Run 4 — appendix hygiene for the 76 new rows: for each new predicate, the set of matching lines was
computed; every row had **exactly one** match and all of them `< 502` (the appendix heading is at
line 502 on the live revision), so no new predicate is satisfied by the incident digest instead of
the rule.

Run 5 — live-revision and view runs (all after the revision-B insert, same session):

```
$ sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md                                  # legacy, live file
93/93 obligations found; 0 MISSING
$ sh .ufo/waves/round-11/verify-census.sh /tmp/unwrapped-proto.md <r13 census>          # §Re-wrap tolerance
169/169 obligations found; 0 MISSING
$ sh .ufo/waves/round-11/verify-census.sh /tmp/unwrapped-proto.md                       # legacy, unwrapped view
93/93 obligations found; 0 MISSING
```

## Weak-predicate self-audit

Weak predicates are the census's real failure mode: a row that still matches after the rule is gone
is a green light over a hole, and it is invisible in the `PASS` stream. So each of the 76 new rows
was attacked.

**Standard.** A row is **weak** iff a plausible one-line edit of `PROTOCOL.md` deletes part of the
obligation while some line still matches the predicate. Every claimed witness was *executed*, not
imagined: the edit was applied to the file text in memory, all 169 predicates were re-run against the
mutated text, and the rows that MISS were recorded. "none found" means the predicate's span contains
the clause's operative words, so removing the clause removes the match.

**Result.** 23 of 76 rows are weak alone; 21 of those are caught by a sibling row (so the census as a
whole still fails on the mutation), one (`G26`) is not a hole at all, and one (`P17`) is an
**uncaught standing hole**, named in §Residual holes. Seventeen of the 21 catches are *audit-driven
closure rows* — G27–G32, G34–G37, L15, L16, L18–L20, P29, V11 — added after the audit found the hole
they close; each one's witness was re-run against it and now MISSes. (G33 and L17 split a clause and
carry no witness; the other four catches are batch-A rows G4, P16, P18 and the batch-B core row L11.)
The 53 non-weak rows — marked "none found", four of them carrying a positive control and one (`R52`)
an audit-driven counter-fix — hold their clause's operative words inside a single line.

**Structural caveat (applies to every row, tested as W19).** A `grep -E` substring cannot see an
added *permission*: `expected values persisted in its own repo` still matches after the text becomes
`expected values persisted in its own repo or supplied by a flag`, and the rule is then no longer
binding. The census detects *deletion*, never *widening*. A future round that wants that guarantee
needs a two-sided predicate (`must match` + `must not match`) or the census moved into the closure
checker; it is out of reach of the round-11 verifier's `grep -qE` contract, which was kept unchanged.

| id | one-line mutation that removes the obligation while the predicate still matches |
|---|---|
| G1 | none found |
| G2 | **weak alone** — W13: delete `it reads surfaces, compares them` (l.364) → G2 still matches; the comparison act vanishes. **Caught** by G28. |
| G3 | **weak alone** — W1: replace `a **probe**, and is registered as one.` (l.364) → G3 still matches; the classification `probe` vanishes. **Caught** by G4. |
| G4 | none found (positive control: W1 deletes its own phrase and G4 MISSes). |
| G5 | none found |
| G6 | none found |
| G7 | none found |
| G8 | **weak alone** — W2: delete `Nothing else is pinned: a gate's own` (l.370) → G8 still matches; the no-other-pinning guarantee vanishes. **Caught** by G27. |
| G9 | **weak alone** — W3: delete `over isolated fixtures (temp trees, no` (l.373) → G9 still matches; hermetic fixture isolation vanishes. **Caught** by G29. |
| G10 | none found |
| G11 | **weak alone** — W17: delete `and the registry records it;` (l.375) → G11 still matches; the registry-record duty vanishes. **Caught** by G30. |
| G12 | none found |
| G13 | none found |
| G14 | **weak alone** — W18: delete `with its committed expected verdict` (l.378) → G14 still matches; the frozen run's expected value vanishes. **Caught** by G31. |
| G15 | none found |
| G16 | **weak alone** — W16: delete `The schema is this section's; ` (l.382) → G16 still matches; schema ownership vanishes. **Caught** by G32. |
| G17 | **weak alone** — W14: replace `not a` + line break + `second inventory;` with `not a queue;` (l.385) → G17 still matches; the not-an-inventory rule vanishes. **Caught** by G37. |
| G18 | none found |
| G19 | **weak alone** — W4: delete `A verdict is lane-local evidence: ` (l.389) → G19 still matches; the lane-local framing vanishes. **Caught** by G34. |
| G20 | none found |
| G21 | none found |
| G22 | **weak alone** — W11: delete `; gate redness is` (l.392) → G22 still matches; the ban's subject vanishes. **Caught** by G35. |
| G23 | **weak alone** — W5: delete the parenthetical `(self-test tally,` + line break + `frozen-run verdict, the revision measured)` (l.393) → G23 still matches; which evidence counts vanishes. **Caught** by G36. |
| G24 | none found |
| G25 | none found |
| G26 | **weak alone** — W6: replace ``lane's own `SKILL.md`.`` with `the lane's repo.` → G26 still matches and **no row MISSes**; **not a hole**: the location duty is still stated in the Registry bullet and pinned by G16, so nothing is lost document-wide. |
| G27 | none found |
| G28 | none found |
| G29 | none found |
| G30 | none found |
| G31 | none found |
| G32 | none found |
| G33 | none found |
| G34 | none found |
| G35 | none found |
| G36 | none found |
| G37 | none found |
| L8 | **weak alone** — W20: delete the wrapped object `demand no / existing province owns.` (l.23) → L8 still matches; the *no existing province owns* bar vanishes. **Caught** by L15. |
| L9 | **weak alone** — W21: delete `mint evidence; ` from the wrapped continuation (l.25) → L9 still matches; the scan-record-is-evidence duty vanishes. **Caught** by L16. |
| L10 | **weak alone** — W22: delete `reasoning, cause, demand instances with evidence pointers, the rejected roster fit, and the` (l.28) → L10 still matches; MINT.md's required content vanishes. **Caught** by L11. |
| L11 | none found |
| L12 | none found |
| L13 | **weak alone** — W23: delete `probation state is recorded in` (l.35) → L13 still matches; the probation clause loses its subject. **Caught** by L19. |
| L14 | **weak alone** — W24: delete `repo + the new sibling's seed files;` (l.36) → L14 still matches; the write-screen's object vanishes. **Caught** by L18. |
| L15 | none found |
| L16 | none found |
| L17 | none found |
| L18 | none found |
| L19 | **weak alone** — W25: delete the wrapped location `` `rounds[].notes` `` (l.34) → L19 still matches; the probation record's location vanishes. **Caught** by L20. |
| L20 | none found |
| P11 | none found |
| P12 | none found |
| P13 | none found |
| P14 | none found |
| P15 | **weak alone** — W10: delete `; the integrator sweeps it` (l.117) → P15 still matches; the integrator-sweep step of the order vanishes. **Caught** by P16. |
| P16 | none found (positive control: W10 deletes its own phrase and P16 MISSes). |
| P17 | **weak alone, and UNCAUGHT** — W7: delete the wrapped object `` `corpus/` files `` → P17 still matches and **no row MISSes**; the order's exclusion of aggregator-owned `corpus/` files can be deleted with the census green. Standing hole — see §Residual holes. |
| P18 | none found (positive control: W12 deletes its own phrase and P18 MISSes). |
| P19 | **weak alone** — W12: replace `is recorded on its termination evidence with the durability debt named, and the next` (l.123) → P19 still matches; the termination-evidence + durability-debt duty vanishes. **Caught** by P18. |
| P20 | none found |
| P21 | **weak alone** — W8: delete `of the filed bytes, labelled or silent.` (l.125) → P21 still matches; the object of the no-rewrite ban vanishes. **Caught** by P29. |
| P22 | none found |
| P23 | none found |
| P24 | none found (positive control: W9 deletes its own phrase and P24 MISSes). |
| P25 | none found |
| P26 | none found |
| P27 | none found |
| P28 | none found |
| P29 | none found |
| R52 | none found — the predicate pins the numeral itself, so a count change (`five` → `six`) MISSes. This row is the counter-fix for the legacy R31 description, whose predicate `expand by exactly` is count-blind (see §Legacy rows). |
| V6 | none found |
| V7 | none found |
| V8 | none found |
| V9 | none found |
| V10 | **weak alone** — W15: replace `Its durability owner is the` with `The committer is the` (l.499) → V10 still matches; the durability-owner framing vanishes. **Caught** by V11. |
| V11 | none found |

### Witness table (executed, not imagined)

Each witness is one edit; "defeats" is the row that still matches afterwards (the weak row),
"MISS" the rows that fail in the mutated text (the catch).

| witness | mutation applied to `PROTOCOL.md` | row it defeats | rows that MISS |
|---|---|---|---|
| W1 | `a **probe**, and is registered as one.` → `registered per the lane's registry.` | G3 | G4 |
| W2 | `Nothing else is pinned: a gate's own` → `A gate's own` | G8 | G27 |
| W3 | `over isolated fixtures (temp trees, no` → `over fixtures, no` | G9 | G29 |
| W4 | `local-first). A verdict is lane-local evidence: it never defines` → `local-first). A verdict never defines` | G19, G20 | G34 |
| W5 | `*committed evidence* (self-test tally,` + line break + `frozen-run verdict, the revision measured)` → `*committed evidence*` | G23 | G36 |
| W6 | ``lane's own `SKILL.md`.`` (l.399) → `the lane's repo.` | G26 | none — not a hole (see below) |
| W7 | `` `corpus/` files `` deleted from l.121 | P17 | **none — standing hole** |
| W8 | `of the filed bytes, labelled or silent.` → `labelled or silent.` | P21 | P29 |
| W9 | `and a *landed* report — an` → `— an` | — (positive control) | P24 |
| W10 | `; the integrator sweeps it` → `.` | P15 | P16 |
| W11 | `` `failed`; gate redness is `` → `` `failed`; `` | G22 | G35 |
| W12 | `is recorded on its termination evidence with the durability debt named, and the next` → `is recorded in the round notes, and the next` | P19 | P18 |
| W13 | `it reads surfaces, compares them` → `it reads surfaces` | G2 | G28 |
| W14 | `not a` + line break + `second inventory;` → `not a queue;` | G17 | G37 |
| W15 | `Its durability owner is the` → `The committer is the` | V10 | V11 |
| W16 | `The schema is this section's; ` deleted | G16 | G32 |
| W17 | `and the registry records it;` deleted | G11 | G30 |
| W18 | `with its committed expected verdict` deleted | G14 | G31 |
| W19 | `expected values persisted in its own repo` → `… or supplied by a flag` | G2, and in principle every substring row | none — the additive class (see caveat) |
| W20 | `demand no` + line break + `existing province owns.` deleted from the mint bullet | L8 | L15 |
| W21 | `mint evidence; ` deleted from the mint bullet's wrapped continuation | L9 | L16 |
| W22 | `reasoning, cause, demand instances with evidence pointers, the rejected roster fit, and the` deleted | L10 | L11 |
| W23 | `probation state is recorded in` deleted | L13 | L19 |
| W24 | `repo + the new sibling's seed files; ` deleted | L14 | L18 |
| W25 | the wrapped location `` `rounds[].notes` `` deleted | L19 | L20 |

W9, W10, W12 and W20–W25 are **positive controls** as run: each deletes a pinned clause (or its
object), so the row that pins it MISSes and the census fails. They are listed because they also prove
the *sibling* row in each pair passes the same mutation — which is why the pairs below must be read as
one obligation. W20–W25 are additionally the evidence that the Sibling-mint bullet, which no row
covered before this pass, is now deletable only clause-by-clause against a red census.

### Pairs (each half alone is deletable)

| pair | one obligation, two lines of the file | witness |
|---|---|---|
| G3 + G4 | "cannot fail is a probe" (l.364) / "registered as one" (l.365) | W1 |
| P15 + P16 | respawn-first (l.117) / integrator-sweep-last (l.117) | W10 |
| P18 + P19 | termination evidence + durability debt named (l.122) / re-graded `failed` (l.123) | W12 |
| P20 + P21 + P29 | erratum form (l.125) / never-a-rewrite (l.125) / its object (l.126) | W8 |
| P24 + P25 | what decides `in-flight` (l.261) / what does not end it (l.262) | W9 |
| L8 + L15 | "may mint a sibling when it finds a domain demand" (l.23) / the *no existing province owns* bar (l.24) | W20 |
| L9 + L16 | "records the roster map it decided against" (l.25) / "mint evidence" (l.26) | W21 |
| L10 + L11 | `MINT.md` exists (l.28) / its required content (l.29) | W22 |
| L13 + L19 + L20 | the probation outcome (l.35) / its subject (l.34) / its location (l.35) | W23, W25 |
| L14 + L18 | "never edits `MANIFEST.json` roster or a sibling's" (l.36) / the write-screen's object (l.36) | W24 |

### Residual holes and limits

1. **P17 — the one uncaught hole.** `PROTOCOL.md:120-121` wraps the rule as
   `and the order never reaches aggregator-owned` / `` `corpus/` files (§Appendix, "Orphaned
   report"). `` Deleting the object on l.121 leaves P17 matching and no other row MISSes, so the
   sweep order's exclusion of aggregator-owned `corpus/` files can be deleted with the census green.
   No single-line predicate fixes this without pinning the `§Appendix` pointer text itself (e.g.
   ``corpus/. files ..Appendix, "Orphaned report"..``), which would raise the odds of a false MISS
   when the compaction merges appendix references. Left open, named here, and routed in the seat
   report: the fix belongs to whoever can accept that trade-off.
2. **W6 is not a hole.** Replacing the second mention of the location (l.399) with a vague phrase
   leaves G26 matching and nothing MISSes, but the duty is still stated at l.382 and pinned by G16, so
   no obligation leaves the file. Recorded as a weak *row* only.
3. **Additive widening is invisible** (W19). Every row in this census — the 93 legacy rows as much as
   the 76 new ones — detects deletion, never an added permission after the pinned phrase. The
   round-11 verifier's `grep -qE` contract cannot express the difference.
4. **Wrapped objects.** `PROTOCOL.md` wraps at ~100 columns, so a clause's grammatical object can sit
   on the next line; P17 is the one case where that leaves a duty unpinned. Rows were deliberately
   built to keep the object on the same line where possible (G4, P13, P14, P19, P20, P22, P23, P26,
   P28, V10 all include their object).
5. **Revision-B rows are as stable as the rule that carries them.** `L8`–`L20` pin a bullet that
   landed during round 13 (`2d19a64`); if the minting lane rewrites that bullet, those rows will MISS
   and must be re-derived — the census is a frozen expectation set, not an authority over the rule.
6. **Presence, not truth.** As with the 93 legacy rows, a predicate proves a phrase is still in the
   file, not that the file is self-consistent (that is `closure-check.py`'s job) nor that no second
   rule contradicts it.
7. **A MISS is not automatically a loss.** Three measured false-MISS classes — line-break splits (45
   extended / 10 legacy on a pure re-wrap), rewords of a pinned span, and emphasis markup added or
   dropped inside one — are all documented with witnesses in §Re-wrap tolerance. The lane that grades
   a compaction should classify a MISS before acting on it, and should not weaken a row because of
   one.

### Re-wrap tolerance — why a MISS can be false

The verifier is `grep -qE` per line, so every predicate is **line-bounded**: a cut that re-wraps a
paragraph (moves line breaks, changes no word) breaks the match even though every obligation is still
in the file. Measured, not argued:

| target | text | extended census | legacy census |
|---|---|---|---|
| `PROTOCOL.md` | original | `169/169`, exit 0 | `93/93`, exit 0 |
| `/tmp/rwB.md` | pure re-wrap at 72 columns — **whitespace-normalized text identical to the original** (`textwrap.wrap(..., break_long_words=False, break_on_hyphens=False)` over prose blocks) | `124/169`, **45 MISSING**, exit 1 | `83/93`, **10 MISSING**, exit 1 |
| `/tmp/unwrappedB.md` | the same re-wrapped text, paragraph-unwrapped | `169/169`, exit 0 | `93/93`, exit 0 |
| `/tmp/rwB-masked.md` | the same re-wrap with every census-matched span held unbreakable | `169/169`, exit 0 | `93/93`, exit 0 |

Because the re-wrapped file is textually identical, all 45 (and all 10 legacy) MISSes are line-break
artifacts — no obligation was removed. `ScoutCompaction` hit the same class independently (their
plain-wrap draft scored `143/156`; `.ufo/waves/round-13/scout-compaction.md` §6 R8), and the legacy
93-row census is fragile in exactly the same way: 10 of its rows depend on where a line breaks. The
counts are implementation-dependent (width, which blocks are wrapped, which rows are pinned): what
matters is the unwrapped view agreeing, never the MISS count being small.

**Remedy — verify the unwrapped view.** Unwrapping joins the lines of each blank-line-separated block
with single spaces, so a predicate is tested against the paragraph rather than one of its wrapped
lines:

```
awk 'BEGIN{RS=""; ORS="\n\n"} {gsub(/\n[ \t]*/," "); gsub(/[ \t]+/," "); print}' PROTOCOL.md > /tmp/unwrapped.md
sh .ufo/waves/round-11/verify-census.sh /tmp/unwrapped.md .ufo/waves/round-13/obligation-census-r13.tsv
sh .ufo/waves/round-11/verify-census.sh /tmp/unwrapped.md
```

Observed on the re-wrapped text: `169/169 obligations found; 0 MISSING` and `93/93 obligations found;
0 MISSING`, both exit 0 — the remedy removes the whole class. **Reading rule for the compaction lane:
a MISS on the unwrapped view is a real obligation loss; a MISS on the line-bounded view of a file that
passes the unwrapped view is a re-wrap artifact.** A MISS is therefore classified before it is graded:
(i) a **wrap split**, which the unwrapped view settles; (ii) a **reword**, which survives the unwrapped
view and is only visible in the pinned span; (iii) **emphasis markup** added or dropped inside the
span (next paragraph). Unwrapping is marginally *more* permissive (it can
join two clauses that were never adjacent), so all 25 witnesses were re-run against it: 22 of the 25
deletions still MISS (the line-bounded view catches the same 22), with `W6`, `W7` and `W19` unchanged
— no witness loses its detection, so the remedy costs no demonstrated catch.

**Usage guard — never stream the view.** `verify-census.sh` runs one `grep` per row and `grep` drains
its input, so passing the view as `/dev/stdin` leaves the first rows matched and the rest starved:

```
$ sh .ufo/waves/round-11/verify-census.sh /dev/stdin .ufo/waves/round-13/obligation-census-r13.tsv < /tmp/unwrappedB.md
161/169 obligations found; 8 MISSING            # exit 1 — a streaming artifact, not a loss
$ sh .ufo/waves/round-11/verify-census.sh /tmp/unwrappedB.md .ufo/waves/round-13/obligation-census-r13.tsv
169/169 obligations found; 0 MISSING            # exit 0
```

Write the view to a real file first. (`ScoutCompaction` reported the same class at the earlier census
size — `150/156` from the same invocation — before this seat re-measured it as `161/169`.)

**Third false-MISS class — emphasis markup inside a pinned span.** The predicates match raw markdown,
so adding or dropping `**` or a backtick *inside* a matched span breaks the row while the rule stands.
Measured on the live file (each edit applied alone, whole census re-run):

| edit | row that MISSes | obligation intact? |
|---|---|---|
| `snapshot` → `**snapshot**` inside G14's span | `G14` | yes |
| `a **probe**, and is registered as one.` → `a probe, …` | `G4` | yes |
| `never the marker predicate` → `never the **marker** predicate` | `G22` | yes |
| `at least three verified rounds` → `at least **three** …` | `L12` | yes |

24 of the 169 matched spans already contain `*` or a backtick, so the class is not exotic;
`ExecCompact` hit it in practice (reported through `ScoutCompaction`). The unwrapped view does not
settle it — the repair is either to keep the pinned span's markup untouched while editing, or to
accept the MISS and re-derive the row after the edit.

**Masking option — keep phrases unbreakable while wrapping.** A compactor that keeps every census-matched phrase
unbreakable while re-wrapping gets a line-bounded-green file with the same words in it. Tested here:
protect the union of all 169 predicate-match spans inside each paragraph (spaces inside a span become
non-breaking), wrap at 72 columns, restore. Observed: whitespace-normalized text identical to
`PROTOCOL.md`, `661` lines against the plain re-wrap's `650` (+11, the cost of whole phrases),
line-bounded `169/169` **and** `93/93`, exit 0. Caveat: the masker must protect the **merged union** of
match spans — a first pass that kept only the longest of overlapping matches split row `G37`
(`second inventory; a fleet index is pointers`, which overlaps `G17`) and scored `155/156`. So
masking is a viable alternative to unwrapping when a lane wants a line-bounded-green artifact; it is
not free (it lengthens lines) and it needs a span-union masker. `ScoutCompaction`'s variant of the
same option reports `486` masked / `484` plain lines with both views green (their §8 V8).

### How round 13 should use this

The compaction lane must verify against `.ufo/waves/round-13/obligation-census-r13.tsv`
(`169/169`), not the round-11 default (`93/93`), because the gate standard, the seven round-12 pins
and the Sibling-mint bullet are only in the extended file. Both numbers must be green against the
compacted `PROTOCOL.md`, and the body inline round-incident budget (`NR<502`, i.e. the pre-appendix
body, `grep -o 'round-[0-9][0-9.]*'` → `4`) must not rise; all three are unchanged by this artifact
(it writes only under `.ufo/waves/round-13/`). Run the census against the **unwrapped view** of the
compacted file (§Re-wrap tolerance): a compacted, re-wrapped `PROTOCOL.md` fails the line-bounded run
for line-break reasons alone, and would read as a false obligation loss.

### Handoff to the compaction lane

The extended census is ready and green against the live `PROTOCOL.md`
(`2d19a64`: `541 50603`, md5 `444667c4…`): `169/169 obligations found; 0 MISSING`, exit 0, with the
legacy default at `93/93`. At 22:23 the compact draft under this wave
(`.ufo/waves/round-13/PROTOCOL.compact.md`) was still byte-identical to the *revision-A* file
(`sha256sum` equal, `526 49269`), so it was measured against a file that has since been superseded:
re-run it against revision B before trusting any number about it. The compaction's acceptance test is
therefore a **three-part** run against the compacted file: legacy
`sh .ufo/waves/round-11/verify-census.sh <file>` → `93/93`, extended
`sh .ufo/waves/round-11/verify-census.sh <file> .ufo/waves/round-13/obligation-census-r13.tsv`
→ `169/169`, and the body round-reference budget (`awk 'NR<PRE_APPENDIX' <file> | grep -o
'round-[0-9][0-9.]*' | wc -l` → `4`, unchanged; `PRE_APPENDIX` is 502 today and moves with the cut).
Note the bound itself moves with the compaction: what must stay `4` is the count over the pre-appendix
body, whatever its new length. Because a compaction re-wraps, run all three against the **unwrapped
view** (§Re-wrap tolerance) as well: on a pure re-wrap the line-bounded run reports 45 false MISSes
(and the legacy run 10), while the unwrapped view of the same text is `169/169` / `93/93`.

### Legacy rows — the bound on what a green census proves

The 93 legacy rows are byte-identical to the round-11 file (the round-13 contract forbids editing
anything under `.ufo/waves/round-11/`; the empty `diff` above is the proof). That fixes two
properties of this artifact, both measured here rather than assumed.

**Coverage is phrase-presence, not line coverage.**

| quantity | command | observed (live revision B) |
|---|---|---|
| lines matched by a legacy predicate | `awk -F'\t' 'NR>1{print $4}' .ufo/waves/round-11/obligation-census.tsv \| while read -r p; do grep -nE "$p" PROTOCOL.md; done \| cut -d: -f1 \| sort -un \| wc -l` | `136` |
| lines matched by any row of this census | same loop over `.ufo/waves/round-13/obligation-census-r13.tsv` | `186` |
| non-blank lines in `PROTOCOL.md` | `grep -c '[^[:space:]]' PROTOCOL.md` | `492`; pre-appendix (`awk 'NR<502'`) `454`, of which the union covers `177` |

So 356 of 492 non-blank lines match no legacy predicate, and 306 match no predicate at all: a green
`PASS` stream proves that the pinned phrases survive, not that every rule is pinned. This reproduces
independently the figure `ScoutCompaction` reports (`.ufo/waves/round-13/scout-compaction.md` §7: 134
of 526 lines matched at the revision they measured, 343 non-blank lines unmatched) — two seats, one
number, on two revisions of the file.

**One legacy row is green and stale.** 29 of the 93 legacy predicates are a single literal word
(`unplaceable`, `dormant`, `monotonic`, `supersedes`, …), so several are blind to their rule's
content by construction; the concrete case: legacy row `R31` states that the integrator's main-repo
writes "expand by exactly **three**", while `PROTOCOL.md:188` says **five** (l.173 at revision A). Its predicate,
`expand by exactly`, matches either numeral, so the row passes while describing a superseded count —
and a reader could take `R31`'s `three` as normative. Because the legacy rows may not be edited, this
artifact pins the live value instead: new row **`R52`** (`expand by exactly five`), which MISSes if
the numeral changes. Read `R31` as stale-by-construction and `R52` as the live count; the same
reconciliation should be done for the rest of the single-word predicates at the next census pass that
is allowed to touch the legacy block.
