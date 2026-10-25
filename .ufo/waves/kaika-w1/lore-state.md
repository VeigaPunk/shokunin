# kaika W1 — STATE dossier · lane `lore` (fictional-world records and consistency: the world bible)

Probe: `W1StateLore` (revenger role), 2026-10-19. Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`, read-only.
Every command runs from the lane root unless it is marked **[fleet]** (cwd `/home/vgpnk/Projects/shokunin`).
`K##` IDs point to the pasteable commands in §7. Pipes stay out of tables.

- **Tools.** STATE needs no web access. No LSP was used. Every claim here is a file-existence, count, byte, or
  exit-code observation, not a claim about symbol meaning. Text sweeps are literal `grep` / `git grep`.
- **Hygiene.** Read-only. The gate replay used verify modes only (`python3 -B`, no `--self-test`, no `--freeze`).
  `git status --porcelain=v1 --ignored | sha256sum` matched before and after (K31).
- **Disclosure.** One accidental write: a shell redirect created `/tmp/kaika-lore-shonen-canon.txt` (601 B, a copy
  of fleet `PROTOCOL.md:423-436`). This probe deleted it at once. No repo file was touched.

---

## 1. Identity

| field | value | evidence |
|---|---|---|
| lane / repo | `lore` / `lore-shokunin`; `origin` → `VeigaPunk/shokunin-world-bible` | `git remote -v`; [fleet] MANIFEST roster `"id":"lore"`, `"repo":"shokunin-world-bible"` |
| domain | "fictional-world records + consistency verification" | [fleet] MANIFEST roster; PROVINCE.md:3 |
| rank | shonen; SHONEN.md has four `[~]` and zero `[x]` | MANIFEST roster `"rank":"shonen"`; SHONEN.md:5-12 |
| branch / HEAD | `main` @ `6cec83aede47575beeeda6b7dc0e4ea74927be78` (2026-10-18 11:28 -0300) | K01 |
| origin/main | `099b4bc` (r102 SCORECARD closure); local is **3 commits ahead**: f553a27, 1659a42, 6cec83a, all post-closure cleanup; standing no-push rule | K02 |
| commits | 152 | K03 |
| last round | **r102**, closed ADMITTED 2026-10-18, "FINAL ROUND OF THE OPERATOR'S LOOP" | LOG.md:3590; SCORECARD.md:665; [fleet] `.ufo/reports/round-102/lore.md:1-3`; [fleet] MANIFEST max lore round 102 (K05). All agree with the ledger hint. |
| next round | **r103**. No lore r103 artifact exists; [fleet] `.ufo/reports/round-103/` holds only `game-dev-2d.md`. | K06 |
| posture | "planned: none — the loop is closed. The lane stands at rest at round 102 unless the operator directs r103+." | SCORECARD.md:693 |
| commit identity | 145/152 `lore-shokunin`; 4 `ci`, 1 orchestrator, 1 operator, and 1 `games-engine-mechanics-shokunin` (the recorded r80 incident, LOG.md:1492) | K04 |

**Unlogged post-closure mutation.** Three commits came after the r102 closure (07:07):
- f553a27 deleted 153,283 files (K18);
- 1659a42 deleted 374 files (K18);
- 6cec83a extended `.gitignore`.

Lane LOG.md mentions none of them (0 hits, K19), and the fleet ledger does not either. Their only trace is the
`.gitignore` comment: "round-101's V04-scratch/baseline-tree re-entered history as 336 MB of nested repo copies"
(`.gitignore:5-8`). f553a27 also broke 24 cited evidence paths (D7).

---

## 2. Axes

No score has ever been assigned. SCORECARD.md:3 reads: "Owned axes: depth, coverage, calibration. Scores remain
unassigned without a quality rubric". The top axis table (SCORECARD.md:6-10) still shows `unmeasured`, with
last-change rounds r43, r39 and r83. Since r93, every closure judges six axes.

| axis | top-table score | top-table last change | improved | unchanged | harmed | r102 verdict |
|---|---|---|---|---|---|---|
| depth | unmeasured (SCORECARD.md:8) | r43 | 16 | 1 | 0 | improved (bounded) |
| coverage | unmeasured (SCORECARD.md:9) | r39 | 14 | 3 | 0 | unchanged (not harmed) |
| calibration | unmeasured (SCORECARD.md:10) | r83 | 16 | 1 | 0 rows; r89 reclassified **harmed** (SCORECARD.md:356) | improved (bounded) |
| operability | not in top table | — | 7 | 3 | 0 | unchanged (not harmed) |
| freshness | not in top table | — | 4 | 6 | 0 | improved (bounded) |
| adjacency | not in top table | — | **0** | 10 | 0 | unchanged (not harmed) |

The improved/unchanged/harmed counts come from K07.

### Lowest non-retired axis

A numeric lowest is undefined: every axis is unmeasured, and no fleet rule covers ties (K20: 0 hits for
`unmeasured|tie-break` in PROTOCOL.md). AXES.md:22-23 says: "Pick the round's axis from the trend furthest behind."

- **Owned-axis reading.** Among the owned axes (SCORECARD.md:3), **coverage** is lowest: 14 improved against 16 and
  16. It was also unchanged in r99 and r102, the latest round (SCORECARD.md:579, 679).
- **Six-axis reading.** Across all six judged axes, **adjacency** is lowest: 0 improved in 10 verdicts (r93–r102).
- Both axes belong to the **expansion** trend (coverage + adjacency, AXES.md:21), which is the trend furthest behind.
- The lane's own old tie-break, "Calibration wins the falsifiability tie-break" (SCORECARD.md:22, fleet round 1),
  has been moot since r87: every round from r87 to r102 included a calibration claim.

**Recommendation.** W2 should first state the owned-axis set (SCORECARD.md:3 is out of date — D9). Then:
- if three axes are owned, take **coverage** as the required lowest axis;
- if six are owned, take **adjacency**.

### Saturation, capabilities, planned work

- **Saturation: none.** SCORECARD.md:365 says no "whole-domain saturation line is established; no saturation is
  asserted and the nudge is disabled". A stagnation window of N=3 was declared there. The `## Saturation` section
  (SCORECARD.md:85) still says it is "to be declared by the lane on its next round", a stale placeholder.
- **Capabilities: 4 rows** (K08): provenance stop-cause assessment (r88), in-world excerpt support verification
  (r89), checker-regression discrimination (r91), frozen boundary-document regression check (r93).
  - Two running gates are missing from this table: `map_obligations` (r94, 25/25 self-test) and `dependency_freeze`
    (r96, 19/19 self-test). Both replay green (K31).
  - SCORECARD.md:412 added `map_obligations` to the SKILL **registry** (now 5 rows, K09), not to the repertoire
    table that AXES.md:57-64 requires.
- **Planned: none** (SCORECARD.md:693). The `## Planned` section (SCORECARD.md:87-89) is a rollout placeholder.

**Fleet-contract tension (not a lane defect).** AXES.md:79 asks for a "score 0–10" per axis. The lane deliberately
did not invent a rubric (SCORECARD.md:365; LOG tail "no rubric was invented"), which matches the kaika essence of
"per-axis verdicts only". `templates/round-prompt.md:21` asks for a "score delta" that this lane cannot honestly
fill. W2 should record verdicts, not invent numbers.

---

## 3. Corpus

### Counts

- knowledge: **25** files (24 `.md` + 1 `.json`) — K10
- lessons: **0**; `corpus/lessons/` is absent — K14
- `QUALITY.md` criteria: **0**; the file is absent — K14
- `SOURCES.md` rows: **0**; the file is absent — K14
- fixture directories: **174** (K15). Frozen chain: 8/8 `RESULT PASS` (K31).
- real-world references: **6** rows in `knowledge/reference-ledger.md` — PROV-O, JSON Schema 2020-12, Python
  graphlib, ETCSL 1.4.1, Spence 1913, Chamberlain *Kojiki*. K16b gives 7 matches: the header plus 6 rows.

### Knowledge headers (CORPUS.md:17)

The rule is: "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`".
- Entries that open with all three in lines 1–3: **10/24** (K11). They are r94–r99 (7 notes), r100 (2) and r101.
- Field missing anywhere in the file (K12):
  - `source:` missing: **12**
  - `verified-at:` missing: **12**
  - `recheck:` missing: **13**
- The same 12 notes lack all three fields: `seed`, the three `2026-10-12-*` notes, `r74`, `r87`, `r88`, `r89`,
  `r91-c9-watch`, `r93-r8-worked-example`, `r102-freshness-sweep`, `reference-ledger`.
- `r102-push-synthesis` is the 13th `recheck:` gap: it has `source:` and `verified-at:` but no `recheck:`.
- `holder-assessment-boundary` has all three fields, but at lines 11, 39 and 50, so it does not open with them.
- `r102-debt-ledger.json` is JSON, so a header triplet does not apply. It carries `compiled_at`.

### Recheck status

- **Overdue by date: 0.** None of the 11 `recheck:` lines carries a date; all are event-triggered (K13).
- `verified-at` values: 9 dated 2026-10-17, 2 dated 2026-10-18, and 1 undated: holder-assessment-boundary says
  "RUNTIME REPLAYED … at `ca7f9ef`".
- **Fired event triggers.** Three notes cite evidence that f553a27 deleted after they were verified (D7):
  `r99-gate-blind-spot-table`, `r100-provenance-semantics-boundary`, `r100-crossing-arc-synthesis`.
  - Their own recheck clauses are therefore now due. Example: r100-crossing-arc-synthesis.md:3 says recheck
    "whenever a cited fixture, map, excerpt, source attribution, gate, pin, or receipt changes".
- The r102 freshness sweep checked hex tokens only: "every sha256-like token (`[0-9a-f]{7,64}`) extracted and
  re-verified" (r102-freshness-sweep.md:8-10). Path pointers were outside its method.

### Coverage map and frontier

- `corpus/README.md`: 0 mentions each of "coverage map", "frontier" and "gaps" (K17). Its headings are navigation
  only (corpus/README.md:12, 16, 29, 38).
- `PROVINCE.md`: 0 `Core` / `Frontier` / `Adjacent` sections (K17). It is Owns / Sources / Refuses prose
  (PROVINCE.md:3-11), short of the LEARNING.md:68 shape.
- Known gaps live elsewhere, in `r102-debt-ledger.json` (K18b): 361 entries, of which 111 are closed, 108 addressed
  and 45 carried. The carried items cluster around:
  - fixture-README replay blocks with no recorded exits: 6 recurrences, r94→r99 (e.g. `r99-NB-09`);
  - legacy-dialect scope bounds (`r95-NB-01`, `r96-NB-01`, `r97-NB-08`);
  - a consistently regenerated map still exits 0 (`r96-NB-21`, `r97-NB-09`);
  - tool and contract committed together (`r94-BR-24`);
  - an offline-irreproducible network fetch (`r94-BR-26`);
  - 35 legacy fixtures covered only by JSON receipts (`r94-BR-27`).

### Candidate coverage-map rows for W2

These come from local evidence. The lane's own scope note already names four uncovered surfaces: "The checker does
not yet check aliases, free-text semantic contradictions, source reliability, or competing in-world dating
systems." (knowledge/2026-10-12-lore-decision-table.md:17-18)

| CM | surface | governed now | local evidence |
|---|---|---|---|
| CM-a | aliases, name variants, homonyms | **uncovered** | decision-table:17; checklist row "name collisions … unmeasured" (2026-10-12-lore-consistency-checklist.md:8); SCORECARD.md:13 "no active name check or alias coverage"; l0-questions.md:1, open since r4 |
| CM-b | free-text semantic contradictions | partial: R10 is a manual gate (SKILL.md:26); no mechanical check | decision-table:17 |
| CM-c | competing in-world dating systems / calendars / uncertain or relative time | **uncovered**; ticks are integer-only (knowledge/r91-c9-watch.md) | decision-table:18; r57 (LOG.md:987); r71 tick-order harm (LOG.md:1271); 0 substantive hits for interval/calendar/relative-date terms (K21) |
| CM-d | reliability of in-world sources | **uncovered** in-world (real-world method belongs to chousa, SKILL.md:7-9) | decision-table:18 |
| CM-e | canon tiers, retcons, supersession of in-world records | **uncovered** | 0 hits for `retcon`, `canon tier` or `canon status` (K21); PROVINCE.md:9 only refuses uncited canon |
| CM-f | reveal (narrative) order vs chronology | **uncovered** | 0 hits for spoiler/reveal order/narrative order/fabula/syuzhet (K21) |
| CM-g | intake of generated content (kotodama handoff packets) | **uncovered** in lore records | lore has no acknowledgement record (K30); kotodama L0 asks lore to confirm packet consumability ([fleet] `.ufo/l0-questions.md:44`) |

Already-governed rows that seed the map:
- entity schema and references (`check_bible`)
- relations and reciprocity
- timeline ticks / `depends_on` / inversion / double-booking
- in-cluster contradictions ledger
- source-ID resolution
- provenance chains (`knowledge/r87-…`, `holder-assessment-boundary`)
- R8 sourced inspiration
- R9 claim→excerpt support (`support_check`, `map_obligations`)
- R10 cross-cluster comparison, manual (`knowledge/r101-…`)
- dependency-edge freeze
- boundary-document certification
- real-world reference ledger, with rights and training permission kept separate

### Leads (unopened)

These are cited in lane or sibling records but were not opened by this probe. W2 must open each in-round before it
becomes a `SOURCES.md` row:
- W3C PROV-O §2 — https://www.w3.org/TR/prov-o/
- W3C PROV-DM (REC-prov-dm-20130430) — https://www.w3.org/TR/prov-dm/, cited at
  `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md:31`
- JSON Schema Validation 2020-12 §6.5 — https://json-schema.org/draft/2020-12/json-schema-validation
- Python `graphlib.TopologicalSorter` — https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter
- ETCSL 1.4.1, lines 122–163 — https://etcsl.orinst.ox.ac.uk/section1/tr141.htm
- Spence 1913 — https://www.gutenberg.org/ebooks/53080
- Chamberlain *Kojiki* 1882 (via Terebess) — https://terebess.hu/english/kojiki.html

---

## 4. Mistakes (mined from the lane's own record)

Base record:
- **32** rejected-closure headings (K22): r4, r14, r38, r42, r44–47, r49, r51–58, r63–65, r68–71, r75–82.
- **2** blocked attempts (K22): r86 at LOG.md:1631, r99 at LOG.md:3267.
- 1 round admitted and later reclassified **harmed**: r89 (SCORECARD.md:356).
- r16 "reject as submitted", then corrected (LOG.md:231).
- Errata recorded in r93–r102.

**Capture status.** No `QUALITY.md` criterion captures any of these classes, because the file is absent (K14). SKILL.md
was swept with one pattern per class (K23); counts are below.

| id | mistake class | evidence (rounds → LOG/SCORECARD lines) | SKILL.md sweep (K23) | proposed `QUALITY.md` criterion |
|---|---|---|---|---|
| M1 | **Unsupported hard rule.** A structural predicate is enforced as an error without a convention that makes the property mandatory, causing false positives or suppressed findings. | r4 LOG.md:52 (homonyms got VIOLATION/exit 1; calibration harm); r44 :750; r45 :767; r63 :1114; r69 :1226; r75 :1379 | 0 hits for homonym/duplicate-name/uniqueness. Held only in SCORECARD.md:14 `retired:`, knowledge/2026-10-12-lore-decision-table.md:52 and l0-questions.md:1. | A predicate fails a bible only when a declared in-world or schema convention makes the property obligatory; otherwise it warns (exit 0) or becomes an L0 question. |
| M2 | **Self-authentication.** New authored text restates or justifies its own premise; a label is treated as provenance. | r14 :203 ("circularly auth…"); r76 :1397 ("registry label cannot authenticate independent provenance"); r79 :1470 (rationale co-invented in the same passage); r80 :1497 | 0 hits for `circular`, `restat`, `self-justif`, `co-invented` (3 knowledge files mention it) | New fiction is admitted only for a consequence not already encoded and not justified by its own premise. IDs, labels and registry rows never confer provenance. |
| M3 | **Report upgraded to fact.** A reported observation, allegation or non-finding is treated as a receipt, an identity, custody, or absence. | r47 :801; r49 :839 (allegation → `provenance.to_holder`); r53 :911; r54 :932; r55 :949 (placement ≠ continued presence); r58 :1004 | R10 (SKILL.md:26) requires referent + field + occasion only across clusters; 0 hits for `non-finding` or `not objective` | Encode reports as attributed claims. Identity, occasion, custody and absence each need their own in-world source. |
| M4 | **Encoding overreach.** A field (tick, place, dependency) asserts more than its excerpt supports. | r16 :231 (description asserted a known place for `place_id: unlisted`; calibration harmed); r71 :1271 (tick 4 encodes unsupported succession; trade rejected) | 0 hits for tick ordering/precedence/succession; only the generic SKILL.md:22 "Accept only the checked structural result" | Every encoded value must be supported by the mapped excerpt. Editorial encodings are labelled editorial in the map and README. |
| M5 | **Prior-art failure.** The candidate repeats an exercised branch or applies an already-admitted distinction. | r38 :632 (r7 already exercised it); r42 :712 (r3 already did); r46 :784 (r41 already admitted the distinction); r51 :877 (r48/r50 already corrected it); r57 :987 (inversion already reports cycles) | 0 hits for `prior art`, `already exercised` (knowledge: 0) | Before declaring, sweep LOG.md and reports for the same branch or rule. A repeat is not a gain; cite the sweep. |
| M6 | **No decision delta.** A diagnostic or table adds output, but no non-author makes a different repair or editorial choice. | r52 :894; r56 :970 (rolled back); r64 :1132; r65 :1150; r68 :1208; r70 :1248; r77 :1420; r78 :1444; r81 :1515; r82 :1537 (a sealed baseline reader chose the same actions) | 2 hits for `materia`, both about R8 inspiration (SKILL.md:24, 40), not diagnostics | Admit a new diagnostic, row or note only if a sealed baseline-vs-proposal comparison by a non-author shows a different action, or it catches a seeded defect the baseline misses. |
| M7 | **Hedging a definite finding.** Over-qualification is itself a calibration harm. | r89 admitted, then harmed: null-chain/tick findings "wrongly qualified at `e97613c`" (SCORECARD.md:356); r90 repaired it forward-only | Only the two repaired lines are pinned, via `discriminate_check` (SKILL.md:59-68) and the C9 watch. SKILL's 2 `qualif` hits are about R10 source-ID qualification, not hedging. | Definite structural findings stay definite. Qualify only where the checker cannot decide, and name the undecidable input. |
| M8 | **Accounting and process errata.** | roster declared ≠ dispatched ×3 (SCORECARD.md:600, 634, 667); "completed" ≠ a usable report (r94 W20, SCORECARD.md:383); phantom "r100 V33" citation ([fleet] r102 report:27); counting-basis drift (push-synthesis:184-187; SCORECARD.md:359); SHONEN prose said `[~]` while the file said `[ ]` (SCORECARD.md:357); wrong git identity plus an unauthorized push (LOG.md:1492); a verifier's `--freeze` probe wrote a foreign `c3red` pin (SCORECARD.md:480); blocked r86 and r99 | 0 hits for roster / declared-vs-dispatched | Compute closure counts from the dispatch receipt, never type them. Every cited seat or report ID must resolve to a file before closure. Verifiers never write to pinned surfaces. |
| M9 | **Evidence durability.** Pointers into transient or parent-repo paths. | r102 F1: dangling commit pin `b6ca1e90…` (r102-freshness-sweep.md:67-77). This probe: 24 cited `*-scratch` paths deleted after admission (D7); 87 runnable `.shokunin/lore/` commands (D8); the r102 sweep checked digests only (r102-freshness-sweep.md:8-10). | 3 hits for `scratch` (SKILL.md:87, 98, 99), all about self-test scratch location or the `c3red` pin; none about citation durability | Durable corpus cites only tracked, non-transient, lane-root-relative paths, never `*-scratch/` or `.shokunin/<lane>/`. Every freshness claim runs a path-existence sweep alongside the digest sweep. |

### Where outside checks disagreed with the gate

These are discernment evidence for `lessons/round-103.md ## Gate`:
- **r16:** the first adjudicator rejected the round as submitted (LOG.md:231); a corrected re-adjudication followed.
- **r89:** the closure gate admitted it; the r93 replay found harm (SCORECARD.md:356).
- **r45:** the verifier first replayed only two controls, then widened scope (LOG.md:767).
- **r53:** the verifier used fixtures-cwd argv and miscounted "496" (LOG.md:911).
- **r55:** the scribe gave a conditional GO against seven no-gos (LOG.md:949).
- **r94:** F15 bounded, F39 superseded, F40 not credited (SCORECARD.md:407-409).
- **r96:** V23's FAIL was discharged by removing the `c3red` pin (SCORECARD.md:480).
- **r97:** V46's FAIL was discharged at r98 (SCORECARD.md:544).
- **r99:** eleven standing FAILs, none re-rolled (SCORECARD.md:582).
- **r100:** V15, V18 and V20 FAILs were discharged or bounded (SCORECARD.md:616).

---

## 5. Contract defects

Severity: **H** blocks D2 conformance; **M** is a conformance or truth defect; **L** is hygiene.

| id | sev | defect | evidence |
|---|---|---|---|
| D1 | H | `corpus/QUALITY.md` is missing, and with it the whole quality-gating step. | CORPUS.md:12; LEARNING.md:12-13, 54-56 ("every criterion cites the lesson that produced it"); K14 |
| D2 | H | `corpus/lessons/` is missing: 0 lessons and no `## Gate` anywhere. | CORPUS.md:14, 18; PROTOCOL.md:419; K14 |
| D3 | M | `AGENTS.md` is missing. | PROTOCOL.md:418. [fleet] Lore and audio are the only lanes missing AGENTS, QUALITY and lessons (K27). |
| D4 | M | `corpus/README.md` has no coverage map, known gaps or frontier (0/0/0). | CORPUS.md:11; K17 |
| D5 | M | `PROVINCE.md` has no Core / Frontier / Adjacent sections. Its sources line is stale: "in-world documents under corpus/ (world bible, once rounds produce it)" (PROVINCE.md:6), yet 174 fixture directories exist. The refusal names `art-east-asian-design` (PROVINCE.md:9), a lane absent from the fleet. | LEARNING.md:68; K17; K15; [fleet] MANIFEST mentions of `art-east-asian` = 0 (K29) |
| D6 | M | Knowledge header non-conformance: 10/24 open with the triplet; 12 lack `source:`, 12 lack `verified-at:`, 13 lack `recheck:`. | CORPUS.md:17; K11, K12 |
| D7 | **H** | **24 dead evidence pointers.** Unique `.ufo/waves/round-{99,100}/seats/*-scratch/…` paths cited from 4 durable surfaces existed at r102 closure `099b4bc` and were deleted by f553a27 (2026-10-18 11:26, "reports and receipts retained"). They are recoverable with `git show 099b4bc:<path>`. Citing files: tools/README.md:331-333, 407, 410; r100-crossing-arc-synthesis.md:72, 111; r100-provenance-semantics-boundary.md:40, 43, 51; r99-gate-blind-spot-table.md:33-39, 93, 242, 270, 274, 287-345. | K16, K17x; deletion attribution in K18c |
| D8 | M | **Path-root drift.** The first run instruction, "From the repo root, run:" `python3 .shokunin/lore/corpus/fixtures/check_bible.py …` (corpus/fixtures/README.md:3-6), exits **2** as written; the lane-relative twin exits 0. There are 87 runnable `python3 .shokunin/lore/` lines, and 95 `.shokunin/lore/` lines across 5 tracked surfaces (fixtures README 86, r74 3, malformed-error-patterns 3, SCORECARD 2, r102-freshness-sweep 1). `.shokunin/` does not exist at the lane root. | K24, K25 |
| D9 | M | **SCORECARD drift.** The title still says "round 83"; SCORECARD.md:3 lists 3 owned axes while 6 are judged; the top table's last-change rounds (r43, r39, r83) and `.shokunin/lore/` commands are stale; `## Saturation` and `## Planned` are rollout placeholders that contradict SCORECARD.md:365 and :693; `## Capabilities` has 4 rows while 6 gates run. | SCORECARD.md:1, 3, 8-10, 72-89, 365, 412; K08, K09, K31 |
| D10 | M | The README index promises files that do not exist: "`lessons/` (per-round), `QUALITY.md` (the admission bar)". | README.md:15-16; K14 |
| D11 | L | SKILL.md frontmatter has no `name:`. [fleet] 16 of 18 lane SKILL.md files have one; lore and souji do not (K28). 13 SKILL lines exceed 500 chars, max 1,155 at SKILL.md:24 (the R8 decision row). Long lines: decision rows 24–26, error signatures 31–32, registry rows 55–56, 87, 89, 98–100 and 103; the registry rows carry dated supersession prose inline. | SKILL.md:1-12, 24-32, 55-103; K26 |
| D12 | M | **Gate conformance debt.** 3 of 6 gates have no self-test: `check_bible`, `discriminate_check`, `support_check`. `check_bible.py`, the lane's core checker, has no SKILL registry row; it is the "sixth gate" only in push-synthesis:76-78. | SKILL.md:46, 65, 76; push-synthesis:83-86; K09 |
| D13 | L | **Bloat.** LOG.md is 803,535 B / 3,634 lines / 383 headings, the largest LOG in the fleet (audio is next at 466,689; K26b). SCORECARD 83,297 B; fixtures README 85,211 B / 1,309 lines; tools README 49,402 B. `reports/` holds 991 flat entries. 6,336 tracked files, 3,468 of them under `.ufo`. `.git` is 28M. | K26, K26b |
| D14 | L | **Stray artifacts** (do not touch; operator decision). `.scratch/` is **the one uncommitted change**: untracked, 26 files, scratch roots `V02` and `v26` (2026-10-18 00:03–00:16) holding a byte-identical freeze tool and contract plus a **mutated** `r100-docket-review/timeline.json`. [INFERENCE] They are r101 verifier seats: the mtimes fall inside r101's declaration-to-freeze window (2026-10-17 23:59 → 2026-10-18 06:12), and the names match r101's V-seat IDs. Also `v05-self-test-scratch/` (126 files, 948K; it matches the `*-self-test-*/` ignore but is a seat probe kit from 2026-10-17 20:27, not a tool temp dir) and `.ufo/interactive-sessions/` (ignored; 3 files, 3.7M). | K04, K32 |
| D15 | L | In `reference-ledger.md`, rows 13–14 (Spence, Chamberlain) follow prose lines 10–12 with no table header, so Markdown does not render them as table rows. An index row is a claim. | reference-ledger.md:3-14 |
| D16 | M | **Adjacency debt.** The kotodama contract `kotodama-lore-adjacency` now hashes `5f4c02bf…` (last changed by kotodama e1694ba, 2026-10-17 17:44), which matches neither digest lore recorded (`e834f503…` at r89, `50c4c2f2…` at r93; l0-questions.md:5-7). Contract §1: "a changed revision/digest requires both lanes to re-read and acknowledge before importing under it." Lore holds 0 acknowledgement records in corpus, SKILL or PROVINCE; its 17 tracked mentions are 16 wave files (r89–r93) plus `l0-questions.md`. The kotodama handoff packet sample (67,699 B) appears in lore only in 2 r93 wave files. | K30 |
| D17 | L | The 3 local commits are unpushed. This matches the standing no-push rule and is informational only. | K02 |
| D18 | L | [debatable] All 4 SHONEN evidence lines end with the extra sentence "Lane assertion, not external promotion verification." PROTOCOL.md:417 allows "one indented evidence line per box … with a resolvable pointer; no other prose". | SHONEN.md:6, 8, 10, 12; K35 |

Confirmed not to be defects:
- SHONEN.md matches the canonical seed byte-for-byte apart from the marks (K33), and its 10 evidence pointers resolve (K35).
  Cleanup f553a27 removed only `.ufo/waves/round-93/deepseek/F17-scratch/` (39 files) from round 93, which no
  durable surface cites.
- All 18 of SKILL.md's line-range anchors resolve (K34).
- The r102 phantom `V30-debt` pointer was already corrected by addendum D1 (push-synthesis:181-183).
- `cross-cluster-contradictions.md`, `r89-hypothetical-moon-basin/`, `r88-myth-cluster2/`, `r88-norse-cluster/` and
  `measure_holder_disclosure.py` are intentionally absent, as stated in the citing text (e.g. r89-…:14, r88-…:131-132,
  holder-…:60-64).

**Operability baseline.** Every documented gate is green on HEAD (K31): `check_bible` CLEAN 0; `support_check` r87
22/22 PASS; `map_obligations` r100 22/22 PASS; `dependency_freeze` 8/8 PASS; discriminator HELD 0; `boundary_doc`
CERTIFIED 0.

---

## 6. Proposed round r103 (1–3 claims, distinct axes)

Common rules for all claims:
- Record per-axis verdicts only; invent no rubric (SCORECARD.md:365).
- Append-only: corrections are dated addenda.
- Verification is non-author.
- No push; `.scratch/` is left for an operator ruling.

### C1 — coverage

Why coverage: it is the required lowest axis on the owned-axis reading (§2), and it was unchanged in r99 and r102.
The claim: establish the coverage map and frontier, then move at least 3 uncovered rows to covered with current-art
knowledge entries.

**Before:** 0 rows from
- `grep -cE '^\| CM-[a-z0-9]+ ' corpus/README.md`
- `grep -c '^## Frontier' corpus/README.md`
- `grep -lE '^coverage-row: CM-' corpus/knowledge/*.md | wc -l`

**After:**
- a coverage map of ≥15 rows (the 12 governed rows from §3 plus CM-a…CM-g, each naming its governing artifact or
  `uncovered`);
- `## Frontier` with ≥3 rows;
- ≥3 new knowledge entries on CM-a, CM-c, CM-e or CM-f. Each entry must:
  - open with `source:` / `verified-at:` / `recheck:`;
  - cite its CM row;
  - cite ≥1 tier-A or tier-B `SOURCES.md` row opened in-round;
  - pass `QUALITY.md` (C2).

Counting command: the three greps above, run before and after.
**Falsifier:** an entry citing a CM row that was already governed, or citing a tier-C source as its sole support.
**Served by:** `corpus/SOURCES.md` (D1 deliverable; the §3 Leads become rows once opened) and the ART dossier's
current art. The decision-table quote at :17-18 is the lane's own warrant for CM-a…CM-d.

### C2 — calibration (the discernment trend)

The claim: an admission bar mined from the lane's own mistakes, and a gated lesson.

**Before:** `test -f corpus/QUALITY.md; echo $?` → 1. `ls corpus/lessons 2>/dev/null | wc -l` → 0.

**After:**
- `QUALITY.md` with ≥7 criterion rows (`grep -cE '^\| Q[0-9]{2} ' corpus/QUALITY.md`), taken from M1–M9. Each row
  cites `corpus/lessons/round-103.md#mistakes` and ≥1 LOG.md or SCORECARD.md line, and each cited line must be a
  reject / harm / erratum / NO-GO / BLOCKED record. Check with
  `sed -n '<n>p' LOG.md | grep -ciE 'reject|harm|errat|no-go|blocked'` → 1.
- `corpus/lessons/round-103.md` with `## Gate` (candidates / admitted / rejected with reasons / spot-check) and
  `## Mistakes`.

**Falsifiers:**
- a criterion with no lesson behind it (LEARNING.md:32);
- a non-author spot-check that disagrees with the gate and the disagreement is not learned;
- a C1 entry admitted that fails any Q row.

### C3 — choose one axis; both satisfy "distinct axes"

**C3-freshness.** No durable pointer dangles silently.
- **Before:** `24` from K16; K24 as-written exit `2`; `87` from K25.
- **After:**
  - dated addenda in the 4 citing surfaces map each deleted path to `git show 099b4bc:<path>`. Measure with K16u
    (missing paths with no `099b4bc:<path>` addendum anywhere in `corpus/`): **24 → 0**;
  - one dated lane-root note in `corpus/fixtures/README.md` maps the historical `.shokunin/lore/` commands to their
    lane-relative twins, with the twin replay at exit 0;
  - the path sweep is added to the freshness method.
- **Falsifier:** any K16 path without an addendum, or a twin command that does not reproduce its documented exit.

**C3-adjacency.** Take this instead if six axes are declared owned; adjacency is then the lowest axis.
- **Before:** `git grep -l 'kotodama-lore-adjacency' -- corpus SKILL.md PROVINCE.md | wc -l` → 0. Contract digest
  `5f4c02bf…` is unacknowledged.
- **After:**
  - 1 acknowledgement record carrying the contract §1 fields `lane, contract_id, revision, file_sha256, reader,
    read_at, evidence_pointer`, at the current digest;
  - a PROVINCE `Adjacent` section naming chousa, kotodama and game-dev-2d with resolvable sibling paths;
  - the dangling `art-east-asian-design` refusal annotated (dated, not deleted);
  - kotodama's L0 packet-consumability question answered or routed.
- **Falsifier:** the recorded digest ≠ `sha256sum` of the contract at verification time.

Non-claimed conformance work that W2 should still land, since axis work does not displace the file contract
(PROTOCOL.md:497-498):
- `AGENTS.md` (D3);
- README index truth (D10);
- SCORECARD owned-axes, saturation and capabilities sections, via a dated section (D9);
- knowledge header addenda for the 12 legacy notes (D6).

---

## 7. Command appendix

All commands run from the lane root unless marked [fleet]. Each line shows the observed value.

```sh
# K01 — HEAD
git rev-parse HEAD                                   # 6cec83aede47575beeeda6b7dc0e4ea74927be78
# K02 — ahead of origin
git rev-list --count origin/main..HEAD               # 3
# K03 — commit count
git rev-list --count HEAD                            # 152
# K04 — authors and worktree status
git log --format='%an' | sort | uniq -c              # 145 lore-shokunin, 4 ci, 1 orchestrator, 1 operator, 1 games-engine-mechanics-shokunin
git status --porcelain=v1 | wc -l                    # 1 (?? .scratch/)
git status --porcelain=v1 -uall | grep -c '^?? .scratch/'   # 26
# K05 [fleet] — max lore round in MANIFEST
jq -r '.rounds[] | select((.notes|tostring)|test("^lore r[0-9]+ ")) | .round' MANIFEST.json | sort -n | tail -n 1   # 102
# K06 [fleet] — round-103 reports
ls .ufo/reports/round-103/                           # game-dev-2d.md
# K07 — per-axis verdict counts
for a in depth coverage calibration operability freshness adjacency; do printf '%s %s %s %s\n' $a "$(grep -cE "^\| *$a *\| *improved" SCORECARD.md)" "$(grep -cE "^\| *$a *\| *unchanged" SCORECARD.md)" "$(grep -cE "^\| *$a *\| *harmed" SCORECARD.md)"; done
#   depth 16 1 0 · coverage 14 3 0 · calibration 16 1 0 · operability 7 3 0 · freshness 4 6 0 · adjacency 0 10 0
# K08 — capabilities table rows
awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\| [a-z]/' SCORECARD.md | wc -l   # 4
# K09 — SKILL registry rows
grep -c '^- \*\*name:\*\*' SKILL.md                  # 5
# K10 — knowledge files
ls corpus/knowledge | wc -l; ls corpus/knowledge/*.md | wc -l    # 25; 24
# K11 — entries opening with the full triplet
for f in corpus/knowledge/*.md; do head -n 3 "$f" | grep -cE '^(source|verified-at|recheck):'; done | grep -c '^3$'   # 10
# K12 — entries missing each field
grep -LE '^source:' corpus/knowledge/*.md | wc -l    # 12
grep -LE '^verified-at:' corpus/knowledge/*.md | wc -l   # 12
grep -LE '^recheck:' corpus/knowledge/*.md | wc -l   # 13
# K13 — dated rechecks
grep -hE '^recheck:' corpus/knowledge/*.md | grep -cE '20[0-9]{2}-[0-9]{2}-[0-9]{2}'   # 0
# K14 — lessons, QUALITY, SOURCES
ls corpus/lessons 2>/dev/null | wc -l                # 0
test -f corpus/QUALITY.md; echo $?                   # 1
test -f corpus/SOURCES.md; echo $?                   # 1
# K15 — fixture census
echo $(( $(find corpus/fixtures -maxdepth 1 -type d | wc -l) - 1 ))   # 174
# K16 — dead seat-scratch pointers in durable surfaces
git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[A-Za-z0-9_./-]+' -- corpus/knowledge corpus/tools/README.md corpus/README.md corpus/fixtures/README.md SKILL.md | sed -E 's/[.,;:)]+$//' | sort -u | while read -r p; do [ -e "$p" ] || echo "$p"; done | wc -l   # 24
# K16b — reference-ledger rows (header + 6)
grep -cE '^\| [A-Z][^-]' corpus/knowledge/reference-ledger.md   # 7
# K17 — coverage map, frontier, gaps, province sections
grep -ciE 'coverage map' corpus/README.md            # 0
grep -ciE 'frontier' corpus/README.md                # 0
grep -ciE 'gaps' corpus/README.md                    # 0
grep -cE '^(#+ )?(Core|Frontier|Adjacent)' PROVINCE.md   # 0
# K17x — of K16, paths that existed at r102 closure
git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[A-Za-z0-9_./-]+' -- corpus/knowledge corpus/tools/README.md corpus/README.md corpus/fixtures/README.md SKILL.md | sed -E 's/[.,;:)]+$//' | sort -u | while read -r p; do [ -e "$p" ] || { git cat-file -e "099b4bc:${p%/}" 2>/dev/null && echo "$p"; }; done | wc -l   # 24
# K18 — deletions per cleanup commit
git show --diff-filter=D --name-only --format= f553a27 | wc -l   # 153283
git show --diff-filter=D --name-only --format= 1659a42 | wc -l   # 374
# K18b — debt-ledger dispositions
jq -c '.totals' corpus/knowledge/r102-debt-ledger.json   # items 264, carry_records 97, source_entries 361, closed 111 / addressed 108 / carried 45
# K18c — which commit deleted the cited scratch
git log --diff-filter=D --format='%h %ad' -1 -- .ufo/waves/round-100/seats/T4-scratch/replay.py   # f553a27 2026-10-18 11:26 (same for T1-, S2-, S5-scratch)
# K19 — cleanup commits in LOG.md
grep -cE 'f553a27|1659a42|6cec83a' LOG.md            # 0
# K20 [fleet] — tie rule in PROTOCOL.md
grep -ciE 'unmeasured|tie-break' PROTOCOL.md         # 0
# K21 — uncovered-surface sweeps (files)
grep -rliE 'retcon|canon tier|canon-tier|canon status' corpus/knowledge SKILL.md PROVINCE.md corpus/README.md | wc -l   # 0
grep -rliE 'spoiler|reveal order|narrative order|discourse order|fabula|syuzhet|reading order' corpus/knowledge SKILL.md PROVINCE.md corpus/README.md | wc -l   # 0
grep -rliE 'allen|interval algebra|calendar|relative date|uncertain date|fuzzy date' corpus/knowledge SKILL.md PROVINCE.md corpus/README.md | wc -l   # 1 (r91-c9-watch.md:211, incidental)
# K22 — rejected / admitted / blocked closure headings
grep -cE '^## Round [0-9]+ — (closure|closed)[^A-Za-z]*.*([Rr]eject|REJECT)' LOG.md   # 32
grep -cE '^## Round [0-9]+ — .*(ADMITTED|admitted)' LOG.md   # 45 — NOT an admission count, for three reasons:
#   it includes r4 "implementation not admitted" (LOG.md:52), leaving 44 genuine headings;
#   the r87–r93 admissions are not worded "admitted" in their headings, and r89 has no heading of its own;
#   the LOG self-reports "43 admitted rounds" (LOG.md:3630), which is unreconciled.
# Do not add 32 + 45: r4 sits in both lists. Closure/closed headings overall:
grep -cE '^## Round [0-9]+ — .*([Cc]losure|[Cc]losed)' LOG.md   # 95 headings, 91 distinct rounds
grep -cE '^## Round [0-9]+ — .*(BLOCKED|blocked)' LOG.md     # 2
# K23 — SKILL.md rule sweeps for the mistake classes
for t in 'homonym|duplicate (display )?name|uniqueness' 'circular|restat|self-justif|co-invented' 'not (objective|authenticated)|non-finding' 'tick.*(order|succession|precedence)|ordering' 'prior[- ]art|already (exercised|admitted)' 'materia' 'hedg|qualif|definite' 'roster|declared .* dispatched' 'scratch'; do printf '%s\t%s\n' "$t" "$(grep -ciE "$t" SKILL.md)"; done
#   0 · 0 · 0 · 0 · 0 · 2 (R8 only) · 2 (R10 source-ID qualification) · 0 · 3 (self-test scratch / c3red)
# K24 — the as-written entry command fails; its lane-relative twin passes
python3 -B .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent; echo $?   # 2 (Errno 2)
python3 -B corpus/fixtures/check_bible.py corpus/fixtures/consistent; echo $?                                 # 0 CLEAN
# K25 — parent-prefix lines
git grep -h 'python3 \.shokunin/lore/' -- corpus/knowledge corpus/README.md corpus/fixtures/README.md corpus/tools/README.md SKILL.md | wc -l   # 87
git grep -h '\.shokunin/lore/' -- SKILL.md SCORECARD.md SHONEN.md PROVINCE.md corpus/README.md corpus/knowledge corpus/tools/README.md corpus/fixtures/README.md | wc -l   # 95
# K26 — sizes and long SKILL lines
wc -c LOG.md SCORECARD.md SKILL.md corpus/fixtures/README.md corpus/tools/README.md   # 803535 83297 18840 85211 49402
awk 'length($0)>500' SKILL.md | wc -l                # 13
git ls-files | wc -l; git ls-files .ufo | wc -l; ls reports | wc -l   # 6336; 3468; 991
# K26b [fleet] — largest lane LOGs
wc -c */LOG.md 2>/dev/null | sort -rn | sed -n '2,3p'   # 803535 lore; 466689 audio
# K27 [fleet] — lane file parity
for d in *-shokunin; do printf '%s %s %s %s\n' $d "$(test -f $d/AGENTS.md && echo A)" "$(test -f $d/corpus/QUALITY.md && echo Q)" "$(test -d $d/corpus/lessons && echo L)"; done   # lore and audio: none of A/Q/L
# K28 [fleet] — SKILL frontmatter without name:
for f in */SKILL.md; do head -n 5 "$f" | grep -q '^name:' || echo "$f"; done   # lore-shokunin/SKILL.md, souji-shokunin/SKILL.md (16/18 have it)
# K29 [fleet] — art-east-asian mentions in MANIFEST
grep -c 'art-east-asian' MANIFEST.json               # 0
# K30 [fleet] — kotodama contract digest and lore acknowledgements
sha256sum kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md   # 5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069
git -C lore-shokunin grep -l 'kotodama-lore-adjacency' -- corpus SKILL.md PROVINCE.md | wc -l   # 0
git -C lore-shokunin grep -l 'kotodama-lore-adjacency' | wc -l   # 17
# K31 — read-only gate replay; worktree status hash unchanged before and after
python3 -B corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review            # CLEAN … 0 violations, exit 0
python3 -B corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster               # TOTAL-ROWS 22/22, RESULT PASS, exit 0
python3 -B corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review           # OBLIGATIONS raw=22 mapped=22, RESULT PASS, exit 0
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing r99-window-lapse r100-docket-review; do python3 -B corpus/tools/dependency_freeze.py corpus/fixtures/$f | grep '^RESULT'; done   # 8x RESULT PASS
python3 -B corpus/tools/discriminate_check.py | tail -n 1                               # DISCRIMINATION HELD, exit 0
python3 -B corpus/tools/boundary_doc_check.py | tail -n 1                               # CERTIFIED (bounded …), exit 0
# K32 — strays
find v05-self-test-scratch -type f | wc -l           # 126
du -sh .scratch v05-self-test-scratch .ufo/interactive-sessions   # 272K 948K 3.7M
# K33 — SHONEN seed identity (marks normalised)
grep -vE '^  ' SHONEN.md | sed 's/\[~\]/[ ]/; s/\[x\]/[ ]/'   # diff against PROTOCOL.md:425-432 with <name>=lore-shokunin: identical
# K34 — SKILL.md path:line anchors resolve (python sweep over `path:N-M` tokens)   # 18/18 resolve
# K16u — dead seat-scratch pointers with no `099b4bc:<path>` addendum (C3-freshness before/after)
git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[A-Za-z0-9_./-]+' -- corpus/knowledge corpus/tools/README.md corpus/README.md corpus/fixtures/README.md SKILL.md | sed -E 's/[.,;:)]+$//' | sort -u | while read -r p; do [ -e "$p" ] || git grep -qF "099b4bc:$p" -- corpus || echo "$p"; done | wc -l   # 24 today
# K35 — SHONEN evidence pointers and the extra disclaimer
for p in .ufo/waves/round-93/recovery/R08-skill-check.py .ufo/waves/round-93/deepseek/F21.md .ufo/waves/round-93/deepseek/F29.md reports/round-1/baseline-probes.json .ufo/waves/round-93/deepseek/F01.md .ufo/waves/round-93/deepseek/F25-replay.py .ufo/waves/round-93/deepseek/F31.md .ufo/waves/round-93/deepseek/F14-postrepair-check.py .ufo/waves/round-93/deepseek/F03.md .ufo/waves/round-93/deepseek/F24.md; do test -e "$p" && echo OK; done | wc -l   # 10
grep -c 'Lane assertion, not external promotion verification' SHONEN.md   # 4
```

## Out-of-lane observations (not investigated further)

- [fleet] A directory literally named `bash: ` (with a trailing space) sits in the fleet root, mtime 2026-10-18
  14:01. It looks like a shell-error artifact.
- [fleet] audio is the other lane missing AGENTS.md, QUALITY.md and lessons (K27). souji is the other SKILL.md
  without `name:` (K28).
