# kaika W1 — fleet-wide mistake mining (learning by making mistakes)

**Seat:** scribe, leaf. **Date:** 2026-10-19. **Scope:** local evidence only; no web
research was assigned to this probe and none was used. Read-only except this artifact.

**Question:** what has the fleet actually gotten wrong, which failures were captured by a
lesson / `QUALITY.md` / protocol rule, and which ones recurred *after* capture?

**Method.** Three passes, then a hand-labelled ledger:

1. `MANIFEST.json` `rounds[]` — shape inventory first (`jq keys`), then rejected /
   non-admitted / corrected / failed rows.
2. Lane memory — every `LOG.md`, `SCORECARD.md`, `corpus/lessons/`, `corpus/QUALITY.md`.
3. Fleet review — `.ufo/reports/AGGREGATE.md` (§2 citation table, §3 process, §9.5,
   §11.7, §13.5), `PROTOCOL.md` + `PROTOCOL-APPENDIX.md` (the fleet's own incident digest),
   `.ufo/l0-questions.md`, the round report surface.

A row enters the ledger only if I opened the pointer and the failure is stated there. Raw
regex sweeps are reported separately as *mentions*; they over-count (e.g. “negative control
rejected” matches “rejected”). Counts are ledger rows unless a command is shown.

---

## 1. Surface inventory — the shapes vary, so no single query finds a rejection

| Surface | Count — command |
|---|---|
| `rounds[]` entries | 294 — `jq '.rounds\|length' MANIFEST.json` |
| rows flagged as non-admitted or rejected | **22** — `jq '[.rounds[] \| select(.admitted==false or .verdict=="rejected-honest-stop" or ((.notes//.note//"") \| test("REJECTED")))] \| length' MANIFEST.json` |
| `admitted:false` alone | 17 — `jq '[.rounds[]\|select(.admitted==false)]\|length' MANIFEST.json` |
| typed `verdict:"rejected-honest-stop"` | 3 — `jq '[.rounds[]\|select(.verdict=="rejected-honest-stop")]\|length' MANIFEST.json` |
| `lanes.<id>:"failed"` rows | 22 — `jq '[.rounds[].lanes//{} \| to_entries[] \| select(.value=="failed")]\|length' MANIFEST.json` |
| lane status vocabulary | ok 204 · in-flight 46 · not-dispatched 45 · **closed 24** · failed 22 — `jq -r '.rounds[].lanes//{} \| .[]' MANIFEST.json \| sort \| uniq -c` |
| closure-corrections | 56 — `jq '[.rounds[]\|select(.type=="closure-correction")]\|length' MANIFEST.json` |
| corrections that correct a correction | 20 — `jq '[.rounds[]\|select(.supersedes.type=="closure-correction")]\|length' MANIFEST.json` |
| corrections by date | 30 on 09-28, 20 on 09-29, 6 on 10-17 — `jq -r '.rounds[]\|select(.type=="closure-correction")\|.date' MANIFEST.json \| sort \| uniq -c` |
| notes mentioning provider/quota/abort | 54 — `jq '[.rounds[]\|select(((.notes//.note//"") \| test("429\|403\|exhaust\|dry\|interrupted\|quota\|provider";"i")))]\|length' MANIFEST.json` |
| `minted` entries | 10, **all at `round:0`** — `jq -r '.rounds[]\|select(.type=="mint")\|.round' MANIFEST.json` |

Twenty-two rows are flagged non-admitted by that filter, and they are four different
shapes: **16 explicit `REJECTED` claim rounds** (kotodama 5, souji 5, kotoba 6), **3 typed
honest stops** (kotodama, `admitted:false` + `verdict:"rejected-honest-stop"`), and **3
non-rejection variants** — one `Operator-skipped` (kotodama r13: two interrupted attempts,
zero worker output), one explicit “honest data not a failed round” (kotoba r41), and one
withdrawal of a prior admission (lore r89). The classification is not derivable from
`admitted` alone: souji's five rejections are stored as `lanes.souji:"failed"` with
prose in `notes`, kotodama's honest stops use a `note` key (not `notes`), and lore's
withdrawal is a `closure-correction` that flips an earlier `admitted`. **A reader counting
rejections with one `jq` field gets a different number than a reader counting headings in the
lane `LOG.md`s**. A loose heading sweep finds **68** round headings with reject/blocked
language across 14 lanes; a tight lore-only pattern finds **32 rejected-closure headings and
2 blocked attempts**:

```bash
grep -cEi '^#{1,3} .*(round|r[0-9]+)[^|]{0,120}(reject|blocked)' */LOG.md   # 68 across 14 files
cd lore-shokunin
grep -cE '^## Round [0-9]+ — (closure|closed)[^A-Za-z]*.*([Rr]eject|REJECT)' LOG.md   # 32
grep -cE '^## Round [0-9]+ — .*(BLOCKED|blocked)' LOG.md                             # 2
```

The fleet ledger holds only lore r87–r102 plus the r89 withdrawal, so **32 of the lore
lane's 32 rejected closures never entered any fleet row**. The 16 explicit rejections counted
above are the ledger-visible subset, not the fleet's rejection history. This is the defect
recorded as **C11/M081** in the taxonomy below: the ledger cannot represent “rejected”.
MANIFEST r89 says it plainly: “lanes.lore ok means a substantive report-bearing attempt is
closed, not successful admission.”

---

## 2. Taxonomy — 13 classes, 95 ledger rows

Rows are unique incidents (primary class only); ID M045 is unused because that incident
(kengaku's absent PROVINCE path) is counted once under C03/M024. “Mentions” is a capture
sweep over `*/corpus/lessons/**/*.md` + `*/corpus/QUALITY.md` (550 files), not an incident
count.

| # | Class | Rows | Lanes (ledger) | Mentions |
|---|---|---:|---|---:|
| C01 | Reference drift — quote/pointer does not say what is claimed | 11 | kumitate, kotoba, kengaku, kasegi, kake, kagi, kaidoku | 31 |
| C02 | Number drift — unreproducible, stale or wrong count | 10 | kake, kasegi, kumitate, kotoba, kotodama, tameshi | 68 |
| C03 | Scope overreach — universal/“generalizes” without a sweep | 5 | kotoba, kumitate, kengaku, mori | 47 |
| C04 | Vacuous or inert verification — check/fix cannot fail | 9 | kotoba, souji, tameshi | 208 |
| C05 | Independence leak — author or own subagent counts as verifier | 4 | kotoba, kagi, kengaku, lore | 32 |
| C06 | Stale premise — claim built on superseded state | 8 | kotodama, kumitate, kotoba | 121 |
| C07 | Unbounded closure — class declared closed, survivor found | 7 | kotoba, souji | 52 |
| C08 | Fix-induced regression / correction error | 7 | kotoba, lore, kumitate, audio, souji, game-dev-2d | 81 |
| C09 | Evidence landing — marker, missing SHONEN, placeholder, overwrite | 7 | kotoba, kengaku, kasegi, kagi, aggregator | 5 |
| C10 | Write-scope / attribution violation | 8 | kotodama, lore, kotoba, kagi, aggregator, kama | 28 |
| C11 | Ledger / queue abandonment and shape drift | 5 | fleet-wide | 134 |
| C12 | Contract surface absence | 9 | 11 lanes + roster | 36 |
| C13 | Operational abort — provider/quota/interrupt | 5 | kotodama, souji, kotoba | 109 |

Capture legend: **P** = `PROTOCOL.md` rule + `PROTOCOL-APPENDIX.md` incident row; **C** =
`CORPUS.md` rule; **Q** = a `QUALITY.md` criterion; **L** = a corpus lesson; **—** = none
found.

---

## 3. Class detail and exemplars

### C01 — Reference drift (11 rows)

The fleet's aggregate review named this failure mode itself: “the failure mode this fleet
has is **attribution drift**, not invention” (`.ufo/reports/AGGREGATE.md` §2). Every early
false pointer pointed at a real file that said something slightly different.

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M001 | 09-28 | kumitate | `128` lane cap attributed to installed ufo skill; sweep returned 0 hits | AGGREGATE §2 row 1 |
| M002 | 09-28 | kotoba | Anti-trigger quoted as frontmatter; it lives in the body table | AGGREGATE §2 row 2 |
| M003 | 09-28 | kengaku | Three filenames attributed to the wrong note | AGGREGATE §2 row 3 |
| M004 | 09-28 | kasegi | Pendle package presented as hard-gate exemplar; gates were in another exemplar | AGGREGATE §2 row 4 |
| M005 | 09-28 | kake | Claimed `status:pruned` was inert; `probe.mjs` has no `pruned` handling | AGGREGATE §2 row 5 |
| M006 | 09-28 | kengaku | README gap example paths both absent | AGGREGATE §2 row 14 |
| M007 | 09-28 | kasegi | Assigned reviewer fabricated “108 modules” totals; rejected, audit redone deterministically | `kasegi-shokunin/LOG.md:301-304` |
| M008 | 10-13 | kumitate | First-pass admission “was wrong”; citation gate rejected the wave with 80 citation-form errors | `kumitate-shokunin/LOG.md:1001` |
| M009 | 09-28 | kagi | “every cited host file” while 4 cited files were unpinned | `kagi-shokunin/LOG.md:170` |
| M010 | 10-13 | kaidoku | Round-1 “evidence_id-bearing output” overclaimed; errata landed next round | `kaidoku-shokunin/LOG.md:25-26` |
| M011 | 09-28 | kake | “byte-frozen” metric wrong; raw sha varies via Cloudflare cfemail re-encoding | `kake-shokunin/LOG.md:42` |

Capture: **C** (“A quote names its location”), kotoba **L** (citation-base rule, r5).
Recurrence after capture: **yes** — M008 and M010 are after the 09-28 rules; M009 and M011
are same-day audit findings, so their capture *is* that audit.

### C02 — Number drift (10 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M012 | 09-28 | kake | Registry 20 rows claimed in five files; live count 21 | AGGREGATE §2 row 6 |
| M013 | 09-28 | kake | “~40 clones”; observed 50 | AGGREGATE §2 row 7 |
| M014 | 09-28 | kasegi | “275 claim packages”; no rule yields 275 (274/295/281) | AGGREGATE §2 row 8 |
| M015 | 09-28 | kasegi | 30 autopsies; observed 31 | AGGREGATE §2 row 9 |
| M016 | 09-28 | kumitate | scripts 74 vs 82; ufo-sighting-lib 25 vs 26 | AGGREGATE §2 row 10 |
| M017 | 09-28 | kotoba | `requires.bins` “all 10”; 7 carry it | AGGREGATE §2 row 11 |
| M018 | 10-14 | kotoba | Draft report claimed `verify_corpus_integrity` 9/9; actual 8/9 at `29c17be` | `kotoba-shokunin/LOG.md:574` |
| M019 | 10-19 | kotodama | Count claimed 27/224; observed 26/223 (C01/C04 lithic collision) | `MANIFEST.json` r42 note |
| M020 | 10-19 | kotoba | “items array 29 (prose said 32 — the count class, corrected)” | `kotoba-shokunin/LOG.md:1351` |
| M021 | 10-14 | tameshi | Kagi claim-ledger pin taken from an uncommitted dirty tree (79294 vs 79301 B) | `tameshi-shokunin/LOG.md:96` |

Capture: **C** (“A count carries its command”), enforced again by the 10-16 prompt
amendment. Recurrence: **yes, repeatedly** — M018 four days after the rule, M019/M020 on the
last day of evidence. The rule exists; the gate does not.

### C03 — Scope overreach (5 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M022 | 09-28 | kotoba | “counterexample none found” with no search command | AGGREGATE §2 row 12 |
| M023 | 09-28 | kumitate | “~80% of SKILL.md content” with no measure named | AGGREGATE §2 row 13 |
| M024 | 09-28 | kengaku | `PROVINCE.md` declared an absent path; unfixed at r3 and r4, so a failed obligation | AGGREGATE §2 row 15 |
| M025 | 09-28 | kengaku | Predicted the fee gate “likely generalizes”; its own five-sample test refuted it | AGGREGATE §1 |
| M026 | 10-15 | mori | Erratum's `w5`–`w11` generalization superseded by measurement | `mori-shokunin/LOG.md:49` |

Capture: **C** (“A negative claim carries its sweep”). Recurrence: **yes** (M026).

### C04 — Vacuous or inert verification (9 rows)

This is the fleet's most-instrumented failure class (208 lesson files mention it) and still
its most productive mistake generator.

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M027 | 10-18 | kotoba | r29 fix was dead code; “all 11 corruptions still exit 0” pre- and post-fix | `kotoba-shokunin/LOG.md:1344` |
| M028 | 10-18 | kotoba | r30: “the filed fix proven inert”; a control-world clone was needed | `kotoba-shokunin/LOG.md:1299` |
| M029 | 10-19 | kotoba | r36: first spot-probe forgot to write the mutated JSON and read green | `kotoba-shokunin/LOG.md:1352` |
| M030 | 10-18 | souji | Certifier `unsafe=3`, one class: `census --compare` accepts empty/near-empty prior | `souji-shokunin/LOG.md:341-342` |
| M031 | 10-17 | kotoba | r32 two-sided box-map shrink passed; absolute floor added at r33 | root `SCORECARD.md` r33 row |
| M032 | 10-19 | kotoba | r33 index fence blindness shared by both instruments | `kotoba-shokunin/LOG.md:1346` |
| M033 | 10-14 | tameshi | E1: author's survivor expectation was wrong; kept as calibration miss | `tameshi-shokunin/LOG.md:90` |
| M034 | 10-14 | tameshi | Survivors D2/D10 were “reported-but-unasserted surfaces” (max findings 2 vs cap 6) | `tameshi-shokunin/LOG.md:85` |
| M035 | 10-14 | kotoba | Frontmatter parser rejected valid nested `metadata:` blocks — a false negative on 37/138 files | `kotoba-shokunin/LOG.md:595` |

Capture: **P** §Gate standard (self-test, two evidences, frozen digests, revision named),
**L** tameshi's mutation bar. Recurrence: **yes, five recorded instances after the rule**
(M027–M030, M032), across three lanes. The rule changed the vocabulary, not the outcome.

### C05 — Independence leak (4 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M036 | 09-28 | kotoba | Round 3 self-checked all four SHONEN boxes | AGGREGATE §9.5 |
| M037 | 09-28 | kagi | Round 3 checked box 2 itself | AGGREGATE §9.5 |
| M038 | 09-28 | kengaku | Round 4 checked box 2 itself | AGGREGATE §9.5 |
| M039 | 10-17 | lore | r92 SCORECARD repeated box-3 `[~]` while canonical SHONEN stayed `[ ]` | `MANIFEST.json` r92 correction |

Capture: **P** promotion gate (“a subagent the lane dispatched is still the lane”),
**Q** kake (“a self-dispatched reviewer treated as independent promotion authority” is a
reject condition). Recurrence: **partly** — the early self-checking stopped (P worked);
the surviving form is assertion/artifact mismatch (M039), not self-promotion.

### C06 — Stale premise (8 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M040 | 10-19 | kotodama | r36 rejected: register-form domain already closed by r26/r27 | `MANIFEST.json` r36 note |
| M041 | 10-19 | kotodama | r43 O+C declared on “stale premises (durable green resolver; owned lithic slot)” | `MANIFEST.json` r43 `note` |
| M042 | 10-19 | kotodama | r44 C blocked: only drafted candidate was a carried topic | `MANIFEST.json` r44 `note` |
| M043 | 10-19 | kotodama | r47 C blocked: 790-line entry vs 221 max plus 9 blocking defects | `MANIFEST.json` r47 `note` |
| M044 | 10-19 | kotodama | r42 C01/C04 lithic collision; C04 lands, C01 routed as spare | `MANIFEST.json` r42 note |
| M046 | 10-13 | kumitate | Gates' default `--src` left stale after upstream relocation | `kumitate-shokunin/LOG.md:990-1001` |
| M047 | 10-19 | kotoba | SCORECARD stale-floors debt carried for many rounds (`S5`) | `kotoba-shokunin/LOG.md:1346` |
| M048 | 10-19 | kotoba | Dispatch brief's floor list stale (82/51 vs live 87/62) | `kotoba-shokunin/LOG.md:1364` |

Capture: no fleet rule requires a premise re-read; the freshness axis is a score, not a
gate. **Q** kama KQ3 covers historical/stale surfaces in one lane only. Recurrence:
**yes, ongoing** — the four most recent kotodama rounds and two kotoba debts.

### C07 — Unbounded closure (7 rows)

The costliest class measured here: seven non-admitted rounds in one lane chasing a class
that kept surviving on a new channel.

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M049 | 10-19 | kotoba | r37 C1 fails: source-blind re-derivation; comparator 23/28 | `MANIFEST.json` r37 note |
| M050 | 10-19 | kotoba | r39 F-2: same laundering class via the value channel | `kotoba-shokunin/LOG.md:1384` |
| M051 | 10-19 | kotoba | r40: payloads close but class “survives on new channels” (F-3′ cwd, F-4) | `kotoba-shokunin/LOG.md:1391-1402` |
| M052 | 10-19 | kotoba | r43: expected-only record+map composition door survives | `MANIFEST.json` r43 note |
| M053 | 10-19 | kotoba | r45: doors “not demonstrably bounded”; census 14/25 closed, 11 open | `MANIFEST.json` r45 note |
| M054 | 10-19 | kotoba | r41 verification round landed a 46-arm census but stayed INCOMPLETE | `MANIFEST.json` r41 note |
| M055 | 10-18 | souji | r9 red-team found 23 defect classes; r10 closed to 1 open class | `souji-shokunin/LOG.md:341` |

Quote: “the class the round meant to close survives in a second channel”
(`kotoba-shokunin/LOG.md:1384`). Capture: **C** negative-sweep rule is the closest text,
but no rule distinguishes *enumerated payloads closed* from *class bounded*. Recurrence:
**yes, six consecutive kotoba rounds** — the rule did not teach the lesson.

### C08 — Fix-induced regression / correction error (7 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M056 | 10-14 | kotoba | r15 first correction (`git rm --cached`) was “a second, worse error than the one it claimed to fix” | `kotoba-shokunin/LOG.md:679` |
| M057 | 10-19 | kotoba | r38 C2 “FAILS AS DECLARED (harm introduced)”: `pins` path=None now crashes | `.ufo/reports/round-38/kotoba.md:35` |
| M058 | 10-17 | lore | r89 admitted then WITHDRAWN: null-chain/tick findings, “lost definiteness is real harm” | `MANIFEST.json` r89 correction |
| M059 | 10-13 | kumitate | r18 first-pass admission wrong; 80 citation-form errors found after | `kumitate-shokunin/LOG.md:1001` |
| M060 | 10-13 | audio | Named verifier draft recycled historical receipts while claiming 44 fresh runs | `audio-shokunin/LOG.md:704` |
| M061 | 10-18 | souji | r11 certifiers “compromised evidence”; certification not granted | `souji-shokunin/LOG.md:353` |
| M062 | 10-13 | game-dev-2d | Work commit `a32920b` omitted the runner diff; verifier caught it, fix `5265da6` | `game-dev-2d-shokunin/LOG.md:614` |

Capture: **P** no-axis-harmed + self-test; no rule requires a fix to prove it can change
the verdict, and no rule covers correction-of-correction. Recurrence: **yes** — M056,
M057, M058 all after the gate standard.

### C09 — Evidence landing (7 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M063 | 10-13 | kotoba | Landed r15 report overwritten 14,715 B → 273 B marker at its canonical path | AGGREGATE D-153; `wc -c .ufo/reports/round-15/kotoba.md` → 273 |
| M064 | 09-28 | kotoba | r12 report carried literal `LANE_HASH` where its commit hash belongs | `.ufo/reports/round-12/kotoba.md:224` |
| M065 | current | fleet | 96 of 224 child reports carry no `SHONEN` heading; 14 post-r20 are audio/game-dev only | `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE '/(protocol\|aggregator)\.md$\|AGGREGATE' \| wc -l` |
| M066 | current | fleet | 15 reports under 1,200 B; 6 self-label `(marker)` | `find .ufo/reports -path '*/round-*/*.md' -size -1200c \| wc -l` |
| M067 | 10-17 | lore | r91 report lacked the required SHONEN heading; defective, not a marker | `MANIFEST.json` r91 correction |
| M068 | 09-28 | aggregator | Mirror lessons left uncommitted; kumitate `a6f9456` swept 72 lines into a lane commit | AGGREGATE §11.7 self-defect 1 |
| M069 | 09-28 | kagi | r12 draft at the contract path while its work was untracked and hashes pointed at aggregator commits | PROTOCOL-APPENDIX “Unlanded report” |

Capture: **P** report contract + marker-vs-report rule. Recurrence: **yes**, but the shape
changed — pre-rule markers/placeholders are largely historical; post-r20 residue is confined
to the three Devin-owned lanes (14 reports). This is the one class where the rule mostly
worked; the exceptions are exempted lanes, not ignorance.

<small>Reproduction caveat, and a meta-instance of C02: kotoba r36 recorded that the
then-current claim “18/35 reports missing SHONEN” did not reproduce — a re-sweep measured
“9/17 fleet-path, 0/17 lane-repo” (`kotoba-shokunin/LOG.md:1364`). My count (96/224 all-time,
14/91 post-r20) is a third scope. The class holds; any single number about it is
scope-dependent and must name its file set.</small>

### C10 — Write-scope / attribution (8 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M070 | 10-19 | kotodama | Commit `31baf5c` (author `kotodama-shokunin`) replaced root `LOG.md` (845→1,356 lines) and `SCORECARD.md` (438→208 lines) with **kotoba lane copies**, deleting the protocol gate-registry and Aggregator-lane sections | `git show 31baf5c -- SCORECARD.md` |
| M071 | 10-12 | lore | Operator question committed at `.shokunin/l0-questions.md`, outside the standing write scope; relocated by `8c4c0a2` | `lore-shokunin/LOG.md:58` |
| M072 | 10-14 | kotoba | `corpus/` pathspec swept a sibling's aggregator-owned lesson into the lane commit | `kotoba-shokunin/LOG.md:679` |
| M073 | 09-29 | kagi | r15 report commit `3485880` carried `.ufo/history-pin.json`, a main-repo integrator file | PROTOCOL-APPENDIX “Lane write scope” |
| M074 | 09-28 | aggregator | `6565e89` touched `CORPUS.md` + nine prompts outside corpus-only scope | AGGREGATE §11.7 self-defect 7 |
| M075 | 09-28 | aggregator | Staged ledger rename consumed by a kagi commit (`ade32e4`) | AGGREGATE §11.7 self-defect 8 |
| M076 | 10-17 | lore | r87/r88 fleet commits combined report + MANIFEST append under lore identity | `MANIFEST.json` r87/r88 corrections |
| M077 | 09-29 | kama | `.gitignore` omitted `kama-shokunin/`; embedded-gitlink accident at `17c1fad`, reverted | AGGREGATE D-152 |

<small>Note: M070 is the most destructive single incident found in this probe. The old
registry home (`## Gate registry — protocol lane registry home`, old `SCORECARD.md:147`)
and `## Aggregator lane` (old `:199`) do not exist at HEAD, so the closure gate's registry
obligation in §Gate standard currently has no artifact to grade.</small>

Capture: **P** pathspec-limited commits, lane identity, “landed means committed”.
Recurrence: **yes, and it got worse** — M072/M076 after the rule, M070 after all of them,
by a lane that was not writing to its own repo. The rule is stated but not gated.

### C11 — Ledger / queue abandonment and shape drift (5 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M078 | 09-29→now | aggregator | Canonical ledger last refreshed at round 11; ~280 later rounds produced no refresh | `grep -E '^## [0-9]+\. Refresh' .ufo/reports/AGGREGATE.md \| tail -1` → “Refresh 8 — round-11” |
| M079 | 10-17 | kotodama, lore | Rejections live only in lane LOGs: kotodama r2 is recorded `failed` for landing with the rejected claim omitted; lore's 32 pre-r87 rejected closures have no fleet row at all | `MANIFEST.json` r2 note vs `kotodama-shokunin/LOG.md:1433-1447`; `grep -c` lore sweep in §1 |
| M080 | current | fleet | 24 lane rows use status `closed`, outside the declared `ok\|failed\|not-dispatched\|in-flight` vocabulary | command in §1 |
| M081 | current | fleet | Rejection shapes are not reconcilable: `admitted:false` 17, typed verdict 3, explicit `REJECTED` in notes 5; the five note-only rows are also `lanes.souji:"failed"` | §1 commands |
| M082 | current | fleet | 10 mint entries all use `round:0`; 8 minted lane repos have no roster row | `jq -r '.rounds[]\|select(.type=="mint")\|.round' MANIFEST.json`; §6 |

Capture: **P** Ledger clause (“a round filed without the ledger duty keeps the routed-defect
queue empty by construction”). Recurrence: **yes, entirely** — the clause predicted exactly
what happened, and the queue has been empty for roughly 280 rounds.

### C12 — Contract surface absence (9 rows)

| ID | Surface | Count — command |
|---|---|---|
| M083 | lane repos missing `corpus/QUALITY.md` | 11 of 21 — loop over `*/corpus/QUALITY.md`; missing: audio, game-dev-2d, game-dev-3d, kagi, kasegi, kengaku, kotoba, kumitate, lore, revenger, souji |
| M084 | lane repos missing `SKILL.md` | 3 of 21 — audio, game-dev-2d, revenger; `git log --all -- SKILL.md` empty in all three |
| M085 | lane repos missing `corpus/lessons/` | 2 — audio, lore |
| M086 | lane repos absent from roster | 8 — chousa, kotodama, mado, mori, souji, tabi, tameshi, tsukuroi |
| M087 | roster `repo` field disagrees with directory | 6 — audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku |
| M088 | knowledge entries lacking any `source:`/`verified-at:`/`recheck:` key | 251 of 683 — `find */corpus/knowledge -type f -name '*.md' 2>/dev/null \| wc -l`; key sweep in §8 |
| M089 | lessons files with a `## Gate` section | 98 of 436; 6 lanes have zero |
| M090 | axis vocabulary split `AXES.md` vs `MISSION.md` | open L0 row aggregator r6 (D-78); `grep -n 'novelty\|consistency' AXES.md` → no match |
| M091 | two provinces claim shipped-artifact RE | `kaidoku-shokunin/PROVINCE.md:1-5` vs `revenger-shokunin/PROVINCE.md:1-5`; tsukuroi L0 asks arbitration |

Capture: **P** file contract. Recurrence: **standing, not historical** — these are current
tree facts, not past events. The contract has no gate that walks the lane set.

### C13 — Operational abort (5 rows)

| ID | Date | Lane | Incident | Pointer |
|---|---|---|---|---|
| M092 | 10-17 | kotodama | r13 operator-skipped: two interrupted attempts, zero worker output, tree clean | `MANIFEST.json` r13 note |
| M093 | 10-18 | souji | r6 96/128 seats completed; judges 15/17 NOT-MET | `souji-shokunin/LOG.md:219-225` |
| M094 | 10-18 | souji | r7 24/24 seats; receipts denied every candidate; lane remote 404 | `souji-shokunin/LOG.md:229-240` |
| M095 | 10-19 | kotoba | token-plan keys 1/2/3 429; provider switched to devin | `MANIFEST.json` r38 note |
| M096 | 10-18 | kotodama | 18/32 seats failed on `reasoning_content` API error | `MANIFEST.json` r44 `note` |

Plus 54 ledger notes mention provider/quota/abort. Capture: none fleet-level; the round
prompt's “named deviation” convention is the only record. Recurrence: constant background.

---

## 3.5 Cross-check with the lane-internal taxonomy (lore probe)

The lore STATE probe (`local://kaika-w1-lore-state.md` §4) mined the same lane's 32 rejected
closures into 9 classes (M1–M9). I re-executed its rejection counts (32 rejected, 2 blocked;
§1 above) but did not independently re-verify every class claim; treat its rows as
peer-verified, not as my observations.

**Counting caveat (peer-corrected, and itself a C02/C11 instance).** An earlier “77 closure
headings” figure was 32 rejected + 45 `admitted`-matching headings, which is not a partition:
r4 matches both regexes (`implementation not admitted`), the admitted pattern misses the
r87–r93 wording, and r89 has no heading of its own. The LOG self-reports “43 admitted rounds”
(`lore-shokunin/LOG.md:3630`), unreconciled. A neutral count is **95 `closure|closed`
headings over 91 distinct rounds** — `grep -cE '^## Round [0-9]+ — .*([Cc]losure|[Cc]losed)'
LOG.md` → 95; distinct rounds `… | sed -E 's/^## Round ([0-9]+).*/\1/' | sort -u | wc -l` → 91.
This is exactly the number-drift class the artifact records; use the neutral count, not the
admitted partition.

The mapping to this fleet taxonomy is:

| lore class | maps to | note |
|---|---|---|
| M1 unsupported hard rule | C08 (harm-by-fix) | false-positive predicate admitted as a hard error |
| M2 self-authentication | C01/C07 | label or authored text treated as provenance |
| M3 report upgraded to fact | C01 | attribution drift at the semantic level |
| M4 encoding overreach | C03 | field asserts more than its excerpt |
| M5 prior-art failure | **none** | repeated work already exercised; invisible to fleet checks |
| M6 no decision delta | **none** | diagnostic produced no different action |
| M7 hedging a definite finding | C02/C05 | over-qualification as calibration harm |
| M8 accounting and process errata | C02/C09 | counts, IDs, identity, unauthorized writes |
| M9 evidence durability | C09 | transient or parent-repo pointers |

The two unmapped classes matter for wave 2: **prior-art failure** and **no decision delta**
are “effort without gain” failures that no fleet-level counter observes. A round can verify
all its claims, harm no axis, and still repeat a settled branch or ship a diagnostic nobody
acts on. Neither class appears in the 95-row ledger because the ledger only records
admissions and defects, not wasted-but-clean rounds. If wave 2 wants a fleet criterion for
them, the lore dossier's M5/M6 rows are the only worked examples I found.

---

## 4. The unlearned repeats (ranked by cost × recurrence)

1. **C07 unbounded closure — 7 non-admitted rounds in kotoba alone (r37–r45).**
   Each round closed the *declared payloads*; each round a new channel survived. The
   fleet has a rule for negative claims but none for “class bounded”. Cost: ~7 rounds at
   17–24 seats each, plus a whole lane's regimen stalled on one claim.
2. **C04 vacuous verification — 9 recorded incidents across 3 lanes, most after the Gate
   standard.** The canonical failure is a fix that cannot change the verdict (M027), then a
   probe that does not apply its own mutation (M029), then a census that accepts an empty
   prior (M030). The Gate standard taught the vocabulary; it did not produce a mutation
   obligation for *fixes*.
3. **C10 write-scope — 8 incidents, escalating to the root-doc overwrite (M070).**
   Every rule was in place; the commit happened anyway, by a lane acting on a "bookkeeping"
   sweep. This is the only incident in the probe that destroyed another lane's artifact at
   HEAD (recoverable only from git history).
4. **C06 stale premise — 8 incidents, the four most recent rounds of one lane.** No lane
   `QUALITY.md` has a premise-freshness criterion; the freshness axis rewards re-measuring
   the *surface*, not re-checking the *claim's premise*.
5. **C01/C02 evidence drift — 21 incidents, 6 of them after the corpus rules.** The rules
   live in `CORPUS.md`; lane reports and `LOG.md` are said to bind, but nothing checks them.
6. **C11 ledger abandonment — the queue of record stopped at round 11, and the ledger never
   saw most rejections.** Six later corrections (r87–r92) had to be filed as one-off
   integrator notes; lore's 32 pre-r87 rejected closures never entered a fleet row at all.

Classes where capture **worked**: C05 self-attestation (early pattern stopped), C09 marker
reports (confined to exempted Devin lanes), C08's no-harm rule (lore r4 and r89 were
correctly rejected/withdrawn rather than averaged). Those three are evidence that a written
gate with a named verifier changes behaviour; the failures that persist are the ones whose
rule has no executable check.

---

## 5. Classes most worth a fleet-level lesson (proposals for wave 2)

Each proposal is a `QUALITY.md` criterion (one table row) plus a gate-shaped check, because
the evidence says prose-only rules did not hold (C01/C02/C07/C10 all recurred).

**L1 — “A fix must be shown able to fail.”** (C04, C08)
Admission bar: every claimed repair ships one red-before state in which the *same* command
exits non-clean for the *named* reason, and the fix is the only delta. Reject a “fix” whose
before/after trees split identically (M027), a probe that mutates nothing (M029), and a
comparison that accepts an empty prior (M030). Gate: mutation or negative-control arm, with
the observed failure text committed.

**L2 — “A closure claim needs a bound, not a payload list.”** (C07)
Admission bar: a claim that says a channel class is closed either (a) names the enumeration
rule and proves it total over a defined carrier, or (b) declares the residual open set with
counts. “All declared payloads fail closed” is not closure while a new door is untested;
M050/M051 are the exemplars. Gate: a surviving-channel census with a stated denominator and
an explicit `open` list, re-run each round.

**L3 — “Re-check the premise, not just the surface.”** (C06)
Admission bar: before writing a claim, re-read the artifact that makes it non-vacuous
(the prior round's closure record, the current file, the current counter) and cite the
reading. Reject a claim whose premise is already closed (M040) or whose scope was moved by
another lane (M044). Gate: a premise pointer with a date and a one-line observed state.

**L4 — “One writer, one path, append-only.”** (C09/C10)
Admission bar: a lane commits only its repo + its report path; a fleet-level sweep must not
replace a root file, and any report at a contract path must be substantive or explicitly
rated a marker. M070 is the cautionary case: a “bookkeeping catch-up” commit replaced the
fleet scorecard with a lane copy and erased the gate registry. Gate: `git show --stat` on
every commit touching root paths must name the owning lane; the closure walker re-derives
the registry sections.

**L5 — “Rejections are typed rows, not prose.”** (C11)
Admission bar: every round-level rejection lands as `{round, lane, status:"rejected",
claims:{…}, reason_class}` in the ledger, with the lane LOG pointer; `ok` never means
“report landed”. M079 (kotodama r2) and r89's withdrawal show the current ledger loses the
fact. Gate: a query that returns all rejections from one field, reconciled against lane LOG
headers each round.

Suggested class vocabulary for `corpus/lessons/` Gate sections (retrofittable): `vacuous`,
`survivor`, `stale-premise`, `reference-drift`, `number-drift`, `scope`, `attribution`,
`landing`, `provider`. The existing lessons use prose; six lanes have no Gate section at all
(M089), so there is nowhere for a rejection to be kept.

---

## 6. Standing contract damage (not historical mistakes — fix before wave 2 writes rules)

1. **Root docs are a lane's docs.** `LOG.md` and `SCORECARD.md` at HEAD are kotoba-shokunin
   files (identity line 1), not the main-repo protocol/aggregator surfaces. The previous
   versions existed at `31baf5c^` and contained the gate registry + Aggregator-lane sections.
   The overwrite is commit `31baf5c`, author `kotodama-shokunin`, subject “fleet backlog
   commit … bookkeeping catch-up”. A reader following §Gate standard's registry-home clause
   finds nothing. Recover in a later commit; do not rewrite `31baf5c`.
2. **No roster for 8 live lanes.** 21 lane repos, 13 roster rows, 10 mint entries at
   `round:0`. `MANIFEST.json` is declared canonical for rank and roster; it cannot be.
3. **Half the fleet has no admission bar.** 11/21 lanes lack `QUALITY.md`; of the 10 that
   have one, 6 carry the same generic 5-line probation draft (“Admission bar (probation
   draft)”), and only kake and kama carry structured, domain-specific criterion tables
   (6 rows each). The learning path's second step is thinnest exactly where the most
   failures occurred (kotoba, kumitate, kasegi, kagi have none).
4. **Corpus provenance is not machine-checkable.** 251/683 knowledge entries carry none of
   `source:` / `verified-at:` / `recheck:` in the contract shape; only 312 carry a
   `recheck:`. Lanes encode provenance in prose or HTML comments (kaidoku), which a freshness
   sweep cannot read. This is why “overdue recheck” cannot be answered fleet-wide.
5. **Ledger queue dead since round 11.** 7 refresh sections total; last names round 11.
   Routed defects after that live only in round notes.
6. **Report-contract residue in exempted lanes.** 14 post-r20 reports without SHONEN
   (audio 4, game-dev-2d 6, game-dev-3d 4). Either the contract binds them or the exemption
   must be written; today it is neither.
7. **Round namespace collisions.** 14/51 L0 lines mention a relaunch, 12 a namespace; per-lane
   counters reset to 1 while `reports/round-1/` already held history.
   `MANIFEST.json` has 10 `round:0` entries and `round:1.5`. Readers cannot resolve
   `round-N` to one lane-round without the `lane_rounds` map, which is present on only 149
   of 294 entries.
8. **Stray artifact.** `.ufo/round-44/drafts/e1/probe.py` was committed by the same sweep
   commit into a path outside the report/wave surfaces. Report the path; don't touch it.

---

## 7. Discarded candidates and limits

- **“10 placeholder reports”** — false. Only one real placeholder exists
  (`.ufo/reports/round-12/kotoba.md:224` `LANE_HASH`); the other regex hits are prose about
  placeholders. Reported as 1.
- **“96/224 reports violate the SHONEN rule”** — true but misleading as a recurrence claim.
  Era split: rounds ≥20 missing = 14/91, all in the three Devin-owned lanes. The rule worked
  for the six original lanes after it landed. Reported with the split.
- **“Affirmative axis harm”** — regex over lane LOGs is unusable (most hits are “none
  harmed” wrapped across lines). I kept only the adjudicated cases with explicit verdicts:
  lore r4 (calibration harmed), lore r89 (withdrawn), kotoba r38 (operability harmed-by-fix).
- **“Exploratory claims drive rejections”** — no evidence either way; 3 typed honest stops
  are scope/carryover blocks, not failed exploratory judgments. Not claimed.
- **Lane-internal taxonomies are cross-referenced, not merged.** The lore probe's 9 classes
  (`local://kaika-w1-lore-state.md` §4) are mapped in §3.5 but their incidents are not added
  to the 95-row ledger; counting them here would double-count the one lore round (r89) my
  ledger already holds and would import peer observations I did not re-execute.
- **Web research** — not assigned to this probe; all rows are local. External current art
  belongs to the ART scouts and must not be inferred from this file.
- **In-flight debt** — I did not audit the 46 `in-flight` rows individually; the protocol's
  debt rule says the next pass answers them, and that pass has not happened for the old era.
  Counted as shape evidence, not as incidents.

---

## 8. Command appendix (pasteable from the fleet root)

```bash
# ledgers
jq '.rounds|length' MANIFEST.json
jq '[.rounds[]|select(.admitted==false)]|length' MANIFEST.json
jq '[.rounds[]|select(.verdict=="rejected-honest-stop")]|length' MANIFEST.json
jq '[.rounds[].lanes//{}|to_entries[]|select(.value=="failed")]|length' MANIFEST.json
jq -r '.rounds[].lanes//{}|.[]' MANIFEST.json | sort | uniq -c
jq '[.rounds[]|select(.type=="closure-correction")]|length' MANIFEST.json
jq '[.rounds[]|select(.supersedes.type=="closure-correction")]|length' MANIFEST.json
jq -r '.rounds[]|select(.type=="closure-correction")|.date' MANIFEST.json | sort | uniq -c
jq '[.rounds[]|select(.admitted==false or .verdict=="rejected-honest-stop" or ((.notes//.note//"")|test("REJECTED")))]|length' MANIFEST.json
jq -r '.rounds[]|select(.type=="mint")|.round' MANIFEST.json

# ledger freshness
grep -cE '^## [0-9]+\. Refresh' .ufo/reports/AGGREGATE.md
grep -E '^## [0-9]+\. Refresh' .ufo/reports/AGGREGATE.md | tail -1

# lane-log rejections the ledger cannot see
grep -cEi '^#{1,3} .*(round|r[0-9]+)[^|]{0,120}(reject|blocked)' */LOG.md
(cd lore-shokunin && grep -cE '^## Round [0-9]+ — (closure|closed)[^A-Za-z]*.*([Rr]eject|REJECT)' LOG.md)
(cd lore-shokunin && grep -cE '^## Round [0-9]+ — .*(BLOCKED|blocked)' LOG.md)

# report surface
ls .ufo/reports/round-*/*.md | wc -l
grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \
  | grep -vE '/(protocol|aggregator)\.md$|AGGREGATE' | wc -l
find .ufo/reports -path '*/round-*/*.md' -size -1200c | wc -l
grep -rl 'LANE_HASH' .ufo/reports/round-*/*.md

# lane contract
for d in */; do [ -d "$d/corpus" ] || continue; [ -f "$d/corpus/QUALITY.md" ] || echo "$d"; done
for d in */; do [ -f "$d/LOG.md" ] || continue; [ -f "$d/SKILL.md" ] || echo "no SKILL: $d"; done

# corpus provenance
find */corpus/knowledge -type f -name '*.md' 2>/dev/null | wc -l
grep -rlE '^[-* ]*source *:' --include='*.md' */corpus/knowledge | wc -l
grep -rlE '^[-* ]*recheck *:' --include='*.md' */corpus/knowledge | wc -l
grep -rlE '^[-* ]*verified[-_ ]at *:' --include='*.md' */corpus/knowledge | wc -l
grep -rlE '^##+ *Gate' */corpus/lessons/*.md | wc -l

# root-doc overwrite
git show --stat 31baf5c
git show 31baf5c^:SCORECARD.md | grep -nE '^## (Gate registry|Aggregator lane)'
```

Mention sweeps behind the taxonomy's “Mentions” column (same 550-file surface: every
`*/corpus/lessons/**/*.md` plus `*/corpus/QUALITY.md`; each line is
`grep -rlE '<pattern>' <surface> | wc -l`):

```bash
C01 '(citation|quote)[^.\n]{0,40}(resolve|location|wrong|dead|fabricat)|misattribut'
C02 '(count|number|tally)[^.\n]{0,40}(command|reproduc|wrong|stale)'
C03 '(overclaim|over-claim|universal quantif|every cited|generaliz)'
C04 '(vacuous|tautolog|cannot fail|inert|negative control|mutation)'
C05 '(self[- ]attest|non-author verifier|author attestation|independent reviewer)'
C06 '(stale prem|stale claim|re-verif|supersed)'
C07 '(survivor|exhaustiv|bounded claim|enumeration)'
C08 '(harm(ed)?[- ]by[- ]fix|regression|fix[- ]introduced)'
C09 '(SHONEN heading|report.last|lands last|marker report)'
C10 '(write scope|pathspec|attribution defect)'
C11 '(routed.defect|ledger row|queue)'
C12 '(QUALITY\.md|file contract|SKILL\.md missing)'
C13 '(quota|429|403|provider (dead|exhaust))'
```

---

## 9. Handoff

- **For wave 2 lesson writers:** L1–L4 are ready to become one criterion row + one gate
  each. L5 needs a ledger shape decision (it edits `MANIFEST` semantics, so it is a
  protocol-lane change, not a lane change).
- **For the protocol lane:** the root-doc recovery (M070) must precede any rule that cites
  the registry home; §Gate standard's delivery clause is currently ungradeable.
- **For the aggregator:** the durable queue is dead (M078). Rebuild from the six post-r11
  correction notes plus this ledger; do not re-derive from 294 rows by hand.
- **Do not** treat the counts here as a score. They are counts of *recorded* failures; the
  fleet's unrecorded failures are, by construction, outside this probe.
