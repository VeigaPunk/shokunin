# Gate correction — round 14 · `R14ExecGate`

**Scope reviewed (round-14 candidate only, read-only):** `PROTOCOL.md` (working tree, 464 lines /
40,079 B) against the committed baseline `HEAD` (`PROTOCOL.md` = 541 lines / 50,603 B; `md5
444667c4a69f5998f9abb957a68a4343`) + `PROTOCOL-APPENDIX.md` (untracked, 47 lines / 11,977 B) →
§Evidence standard, §Gate standard, §File contract per shokunin repo, §Invariants, §Fleet-2
conventions (adopted).
No source file was edited; no test, build, formatter or gate was run; the candidate was not mutated.
All commands below are read-only. `[observed]` = tool output quoted verbatim; `[inference]` = derived.

**Baseline correction (affects the round-14 measurement, not my five sections):** `[observed]`
`git diff 310967c HEAD -- PROTOCOL.md` → 0 lines, so `PROTOCOL.md` is byte-identical at `310967c` and
at current `HEAD` (`4d518fe`); the round-14 data-walk's `f3cbdcf` (526 lines / 49,269 B) is an *earlier*
source snapshot, 15 lines behind because of `2d19a64` ("sibling-mint allowance + kama probation
entry"). The P4-length before/after for this move is therefore **541 → 464 lines / 50,603 → 40,079 B**,
not 526 → 464, and `f3cbdcf`-based line numbers in earlier round-14 notes are 15 lines low below
`2d19a64`'s insertion point.

## Verdict

1. **Material defect, introduced by this candidate (fix before landing):** §Invariants dropped
   `CORPUS.md` from the main-repo write enumeration — present at `HEAD:PROTOCOL.md:440`, absent from
   the worktree (`git diff HEAD -- PROTOCOL.md`, deletion hunk `@@ -439,30 +403,26 @@`) → main-repo
   **`CORPUS.md` now has no named writer** anywhere in the pair. Exact old/new text and reason in
   **Finding 1**.
2. **Material defect, carried (NOT this candidate's — do not count it twice):** §Gate standard
   Registry clause (rows live in "each lane's `SKILL.md`") stays unsatisfiable for the two main-repo
   lanes. It predates this candidate, is already filed and open as ledger row **D-127**
   (owner protocol/integrator), and its text is frozen by a committed anchor. Text in **Finding 2**;
   land it as a routed-defect closure, not as part of the compaction move.
3. **Gate-integrity fact this proves:** the round-13 preservation gate reports `clean` on this
   candidate, and neither Finding 1's clause nor Finding 2's clause is reachable by its census or
   anchors. The honest round-14 claim is "every obligation **in the census** preserved", not
   "no obligation lost" (**§Blind spot**).

---

## Finding 1 — `CORPUS.md` write-ownership clause dropped by the compaction (new, material)

**Location.** `PROTOCOL.md:403-404`, §Invariants, first bullet (`[observed]`
`grep -n 'Only integrator roles' PROTOCOL.md` → `403`).

**Old text (candidate, verbatim):**

```
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it. Only integrator roles
  write main-repo files: `MISSION.md`, `AXES.md`, and `scripts/` are operator-side integrator files,
```

**New/old baseline text that was dropped** — present at `HEAD:PROTOCOL.md:439-441` (hunk
`@@ -439,30 +403,26 @@` of `git diff HEAD -- PROTOCOL.md`; byte-identical at `310967c:PROTOCOL.md:439-441`
and at `f3cbdcf:PROTOCOL.md:424-425`):

```
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it. Only integrator roles
  write main-repo files — `MANIFEST.json`, `PROTOCOL.md`, `ROADMAP.md`, `CORPUS.md`, `MISSION.md`,
  `AXES.md`, `scripts/`, `.ufo/` state and prompts.
```

So the loss is **candidate-only**: `git diff HEAD -- PROTOCOL.md` shows the `CORPUS.md` line as a
deletion, and no earlier round removed it.

**Reason it is a material defect, not a length win.** `CORPUS.md` is missing from *every* writer class
the candidate enumerates, and those enumerations are closed:

- lanes: "Lanes write only inside their own child repo and their lane report" (`PROTOCOL.md:407`);
- aggregator: "no main-repo files outside its own report and ledger" (`PROTOCOL.md:274-275`);
- protocol lane: "Its main-repo writes are … those expand by exactly six" (`PROTOCOL.md:154-163`) —
  `CORPUS.md` is not among them;
- operator-side list: `MISSION.md`, `AXES.md`, `scripts/` (`PROTOCOL.md:404`) — `CORPUS.md` absent.

So after compaction a main-repo file that the pair still binds is unowned. `[observed]` the file is
live and tracked (`git ls-files CORPUS.md` → `CORPUS.md`; `ls -la CORPUS.md` → `2926 B`), and the
candidate names it four times (`PROTOCOL.md:69` snapshot clause, `:272` aggregator duty, `:297` "the
`CORPUS.md` rules bind `LOG.md` entries and lane reports too", `:374` the `corpus/` file-contract
row). The fleet's own record treats editing it as a lane defect and expects integrator-only writes:
ledger `.ufo/reports/AGGREGATE.md` §10 — "The round-3 aggregator's `CORPUS.md` write (commit
`6565e89`) remains a flagged write-scope violation with adjudication pending … Recommendation:
**ratify the content** … but confirm `CORPUS.md` is integrator-only going forward —
aggregator-proposed CORPUS rules route through the report"; and `.ufo/l0-questions.md:12` files the
pending CORPUS.md amendment set as "all operator-side text (this lane publishes the measurements and
does not edit the file)". `[inference, grounded on those two records]` the correct label is
operator-side integrator, i.e. the pre-compaction sentence's file set.

**Minimal replacement text (one insertion; no new semantics).**

old (`PROTOCOL.md:404`):

```
  write main-repo files: `MISSION.md`, `AXES.md`, and `scripts/` are operator-side integrator files,
```

new (`PROTOCOL.md:404`):

```
  write main-repo files: `MISSION.md`, `AXES.md`, `CORPUS.md`, and `scripts/` are operator-side integrator files,
```

Conservative alternative if the L1 prefers byte-for-byte restoration of the dropped sentence: replace
`PROTOCOL.md:403-404` with the two baseline lines quoted above and keep the following operator-side
clause verbatim. Either form restores exactly the dropped rule; neither adds a rule.

**Gate impact of the fix.** `[observed]` no expected value pins it:
`grep -n -iE 'integrator roles|CORPUS\.md|write main-repo|operator-side'
.ufo/waves/round-13/obligation-census-r13.tsv` returns only `F5` (`corpus/ per CORPUS.md` — the
*child-repo* corpus row) and `I5`; `grep -n -i 'operator-side\|integrator roles\|CORPUS'
.ufo/waves/round-13/anchor-phrases.txt` returns only that file's own comment line 22
(`# --- pin 2: … aggregator-corpus exclusion`), so **no anchored phrase covers the main-repo write
set**. The insertion adds at most one line (cap has six lines of headroom: 464 lines today vs
`--max-lines 470`). Optional hardening, not scope: one census row `I14 | Invariants | Main-repo write
set integrator-only incl. CORPUS.md | CORPUS.md` would make this class visible next time.

---

## Finding 2 — §Gate standard registry home unsatisfiable for main-repo lanes (carried; D-127)

**Location.** `PROTOCOL.md:341-343` (Registry bullet) and its conformance echo at
`PROTOCOL.md:360-361` ("closure grades no gate conformant until its registry row exists in the lane's
own `SKILL.md`").

**Old text (candidate, verbatim start of the bullet and the echo):**

```
- **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name,
  `gate|probe`, entry command, verdict map (code → class), self-test command and spelling,
  pinned-value path, write scope, owner. …
  … in its round report, and closure grades no gate conformant until its registry row exists in the
  lane's own `SKILL.md`.
```

**Why it is material.** `[observed]` `ls SKILL.md` → `No such file or directory`;
`find . -maxdepth 2 -name 'SKILL.md' -not -path './.git/*'` → 7 hits, all under `*-shokunin/`. The
main repo hosts the `protocol` and `aggregator` lanes, both of which own committed gates (protocol:
`closure-check.py` mandated by §Round-robin step 4, `verify-protocol.sh`; aggregator:
`corpus-gate.mjs`), so the §Gate standard conformance condition can never be met for the gates this
file itself requires. **Pre-existing and already routed:** `[observed]`
`.ufo/reports/AGGREGATE.md:1886` — "`D-127 | protocol/integrator | 3 | §Gate standard puts registry
rows in 'each lane's `SKILL.md`'; the two main-repo lanes have none (`ls SKILL.md` → absent), so a
main-repo gate is unregistrable as written — the D-120 class repeating | §14.8; critic A4"`; the same
file's gate table reads "**unsatisfiable as written**". `[observed]` `git diff f3cbdcf -- PROTOCOL.md`
carries the Registry bullet's `SKILL.md` clause and the Delivery echo as unchanged context lines, i.e.
the compaction did not introduce them — **report it as carried debt, never as this round's finding or
as a gate-integrity regression**. (Caveat: the round-12 commit SCORECARD names for this clause,
`dddb4ec`, does not resolve in this repo — `git show ddb4ec` → `fatal: ambiguous argument` — so the
landing commit for the clause is not verifiable from here; the round-12 text itself is.)

**Minimal replacement text (proposed; the home choice is the L1's ruling).** Insert one clause after
`owner`, using a home the round-13 gate already populates:

old (`PROTOCOL.md:343`):

```
  pinned-value path, write scope, owner. The aggregator ledger stays the routed-defect queue, not a
```

new (`PROTOCOL.md:343`):

```
  pinned-value path, write scope, owner — a lane whose repo has no `SKILL.md` (the two main-repo
  lanes) declares the same fields in the committed header block of the gate script and names that
  path in its round notes. The aggregator ledger stays the routed-defect queue, not a
```

`[observed]` that home already exists in practice: `.ufo/waves/round-13/exec-verifier.md` §1 records
`Owner`, `Type: gate`, `Pinned values`, `Entry command`, `Self-test spelling`, `Verdict map`,
`Revision measured` in the script header — the Registry schema's fields verbatim.

**Required companion edits if this lands (else the gate goes red):** `[observed]`
`.ufo/waves/round-13/anchor-phrases.txt:65` pins the literal phrase "the rows live in each lane's
\`SKILL.md\`"; census rows `G16` ("Registry rows live in each lane's SKILL.md, with the fields …") and
`G26` ("Closure grades no gate conformant until its registry row exists in the lane's own SKILL.md")
pin the two clauses. Anchor and census updates must ship in the same committed act.

---

## Blind spot — why the round-13 gate's `clean` does not cover Findings 1–2

`[observed]` census row `I5` is *identical* in the baseline-derived and candidate census:
`I5 | Invariants | Operator-side integrator files (MISSION/AXES/scripts) named, never lane-edited |
operator-side integrator` (`.ufo/waves/round-11/obligation-census.tsv:81`,
`.ufo/waves/round-13/obligation-census-r13.tsv:81`). The predicate tests the *second* sentence's
three-file list; the *first* sentence's main-repo write set (the sentence that carried `CORPUS.md`
from round 11 onward) has never had a row. `[observed]` `verify-census.sh:12` matches with
`grep -qE "$pred"` — presence-only, so a dropped sibling clause passes. Finding 2's clause is pinned,
but *as the defective text*, so its own anchor guarantees the gate keeps reporting `clean` on a clause
the ledger has already graded unsatisfiable. Net: the round-13 verifier proves obligation **presence**
over its 169-row census, 61 anchors and per-section modal floors; it is not a semantic-equivalence
proof, and length reduction must not be scored as a protocol-soundness gain on this evidence alone.

## Cleared — inspected, no defect found

- **§Evidence standard** (lines 287-306): closure-time resolvability, claimed≠re-executed, corrections
  sweep, hash-not-tag citation and drift-pin persistence all survive with unchanged modal force.
  One *advisory* sentence was dropped (baseline: "Recommended where the surface drifts outside lane
  control."); no modal token, no census row, no anchor — recorded as an observed non-normative drop,
  no repair proposed.
- **§Gate standard** (lines 318-363): Verdict map, Self-test, Two evidences (incl. the new
  `expected.json` digest pinning and `unpinned (legacy)`), Scope, Closure consequence and Delivery
  agree with the round-13 `verify-protocol.sh` declarations (exit map `0/1/2/3`, `--selftest`,
  committed expected values, frozen roots). Clarity note only: the Delivery parenthetical "(one of
  five child-lane items)" can be misread as claiming §Gate standard is one of the five items
  enumerated at `PROTOCOL.md:71-74` (report path, commit-before-report, `SHONEN` heading, hash
  citation, write scope); the following sentence makes the intent unambiguous, and the phrase is
  unanchored, so no repair is proposed.
- **§File contract** (lines 365-390): all rows accurate; the new `PROTOCOL-APPENDIX.md` row correctly
  declares "Main repo, protocol-lane owned" inside a table headed "per shokunin repo". The strain is
  self-disclosed by the row, and the heading is pinned by the verifier's `structure` check (`[observed]`
  `SECTION_KEYS_BODY=…'## File contract per shokunin repo'…`), so no fix.
- **§Invariants** other bullets (contested scope + re-flag, append-only `LOG.md`, `.ufo/state` /
  `watchdog.log` churn, lane identity incl. the main-repo `-c user.name` form, corpus corrections
  two-way rule): unchanged in force.
- **§Fleet-2 conventions** (lines 440-462): the `novelty`/`consistency` → six-axis mapping clause
  agrees with `MISSION.md`'s lane table and `AXES.md`'s six axes; SSOT precedence and the L0
  append-only + integrator-durability bullet agree with the candidate's own app-mode text.

## Method (all read-only)

`git log --oneline -8`; `git status --porcelain`; `wc -l -c PROTOCOL.md PROTOCOL-APPENDIX.md`;
`git rev-parse HEAD` → `4d518fe`; `git show HEAD:PROTOCOL.md | wc -l -c` → `541 50603`;
`git diff 310967c HEAD -- PROTOCOL.md | wc -l` → `0`; `git diff --numstat HEAD -- PROTOCOL.md`
→ `239 316`; `git diff HEAD -U1 -- PROTOCOL.md` (31 hunks, read in full) and the same for
`f3cbdcf` (31 hunks, for the r12→r13/r14 separation);
`git show 6bd4f38:PROTOCOL.md | grep -n 'Only integrator roles' -A4`;
`grep -n 'CORPUS' PROTOCOL.md` (4 hits, none an ownership rule); `ls SKILL.md`;
`find . -maxdepth 2 -name 'SKILL.md'`; `git ls-files CORPUS.md`; `grep -n -i …` over
`.ufo/waves/round-13/obligation-census-r13.tsv`, `.ufo/waves/round-11/obligation-census.tsv`,
`.ufo/waves/round-13/anchor-phrases.txt`, `.ufo/waves/round-11/verify-census.sh`,
`.ufo/reports/AGGREGATE.md`, `.ufo/l0-questions.md`, `.ufo/waves/round-13/exec-verifier.md`.
Baseline `f3cbdcf` and cited commits `235b414`, `609ecb6`, `4c81066`, `c8f9f57` all resolve
(`git cat-file -t` → `commit`); the commit the SCORECARD names for §Gate standard, `ddb4ec`, does
**not** resolve in this repo.

## Adjacent observation (outside the five sections; not a defect of the candidate)

`[observed]` `.ufo/prompts/protocol-round-14.md:7` quotes the L2 route map as
"executor/scribe/scout/reviewer/critic/sentinel/revenger/labrat/mutation-tester/simplifier/distiller
@m_flash", while the route SSOT `MISSION.md:41-43` reads `executor, scribe, scout → @m_flash` and
`reviewer, critic, sentinel, revenger, labrat, mutation-tester, simplifier, distiller → @m_zfl`
(fallback `@m_swe`). §Round-robin step 1 requires the integrator to check "that any L2 route map
quoted in the prompt matches the current `MISSION.md` bucket", so this is a step-1 prompt-fidelity
conformance defect for the round notes (and a `lane_prompt()` correction for the operator, since
`scripts/` is operator-side). Provider identity itself is unverified — the `task` API exposes role
selection only — so no provider claim should be made from either bucket. Not a finding against
`PROTOCOL.md`/`PROTOCOL-APPENDIX.md`; recorded here only because step 1 grades it.

## Status

Advisory to the protocol L1. **Finding 1 is the only defect this candidate introduces**; Finding 2 is
carried debt (D-127) and must not be counted as a round-14 gate-integrity move. Both are drafted as
minimal text only; nothing outside this scratch file was written.