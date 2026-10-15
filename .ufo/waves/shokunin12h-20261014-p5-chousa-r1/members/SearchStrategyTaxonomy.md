# SearchStrategyTaxonomy — chousa r1 advisory

**Member:** SearchStrategyTaxonomy (executor)
**Wave:** shokunin12h-20261014-p5-chousa-r1
**Lane:** chousa-shokunin (province owns search-strategy taxonomy — `chousa-shokunin/PROVINCE.md:7`)
**Axes judged on:** coverage · depth · calibration
**Class:** advisory data for parent corpus land — **not a judge verdict**

---

## 0. Central finding (must not be papered over)

The three survey artifacts are **chat-export transcripts** of GPT-6-Astra browse sessions, not Deep Research pipeline dumps (`research/README.md:6-8`). Their on-page citation chips (`コトバンク`, `arxiv.org`, `+N`, bare hostnames) are **unverified from local material alone**. Any strategy below that is *observed in the exports* is labeled **observation (export)**; it is not admitted as a fleet rule until a local hop can be resolved or an operator external window is approved.

**Observation / inference / unknown stay separate** throughout (`chousa-shokunin/corpus/QUALITY.md:5`; `chousa-shokunin/SKILL.md:45`).

---

## 1. Axes of a search move

Name these before picking a strategy. A move is scored only on axes it claims.

| Axis | Question | Local anchor |
|---|---|---|
| **Q** Question-bound | Is the search answering a declared question? | `chousa-shokunin/SKILL.md:17` — never start from a search box with no question |
| **L** Locality | Can it be answered from local durable surfaces first? | Round contract: no external fetches; approval table required (`chousa-shokunin/SKILL.md:34-36`) |
| **R** Resolvability | Does every cite resolve to path/command/blob, or is it labelled dead? | `kagi-shokunin/corpus/claim-ledger.sh:31-46`, `:429-440`; `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-19`; `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-67` |
| **H** Hierarchy | Primary > secondary > aggregator > unsourced? | `chousa-shokunin/SKILL.md:18`, `:28` |
| **N** Negatives | Does an absence claim carry its sweep command? | `CORPUS.md:38-40`; `PROTOCOL.md:336-337`; `chousa-shokunin/SKILL.md:44` |
| **K** Keep-rejects | Are rejected sources retained with reason? | `chousa-shokunin/corpus/QUALITY.md:5`; `chousa-shokunin/SKILL.md:46` |
| **C** Cost/approval | Is the next hop inside loopback, or does it need operator approval? | `chousa-shokunin/SKILL.md:34-36`; province refuses live external without approval (`chousa-shokunin/PROVINCE.md:10-12`) |

**Calibration rule:** improve any axis and harm none. A widen that gains coverage by dropping resolvability is a net loss (fleet gates fail-closed on unresolved cites — claim-ledger citations `CLEAN|BROKEN`, anchorcheck bad classes, kumitate `CITE_CHECK: CLEAN|DRIFT`).

---

## 2. Ordered taxonomy — what to try first

Strategies are numbered **S0→S9**. Status is one of:

- **admitted** — fleet or chousa local artifact cites the practice at path:line
- **observation (export)** — seen in A/B/C transcripts; citations inside the export are unverified
- **proposal** — useful method candidate with an explicit **falsification** condition

### S0 — Frame the question before any search
**Status:** admitted  
**Do first:** write the question the window will answer; refuse “search and see.”  
**Evidence:** `chousa-shokunin/SKILL.md:17` decision-table row “Research a question”; expected output is a research record with a declared question.  
**Stop if:** no question can be stated — halt; do not open a search surface.  
**Falsification (of the rule itself):** a successful research record with no declared question that still passes a future `research-gate.sh` question check — would refute S0 as gateable.

### S1 — Local inventory before remote
**Status:** admitted  
**Do first:** enumerate local durable surfaces that could answer Q:

1. lane corpus (`chousa-shokunin/corpus/`, sibling `*-shokunin/corpus/`)
2. fleet root docs (`CORPUS.md`, `PROTOCOL.md`, `research/`)
3. citation/instrument precedents (claim-ledger, anchorcheck, cite-check)
4. already-harvested research dumps (`research/deep-research-2026-09-28/`)

**Evidence of local-first resolvers (order is the search order):**

| Surface | Local-first order | Cite |
|---|---|---|
| kagi claim-ledger citation classes | `corpus/*` → knowledge/lessons shorthand → sibling lane → `.ufo` → root docs; session URIs are EPHEMERAL fail | `kagi-shokunin/corpus/claim-ledger.sh:434-450`, `:31-41` |
| kasegi anchorcheck bases | blob-pin → ORIGIN-WORK explicit → lane → MIRROR-ABSOLUTE → unprefixed mirror fallback; lost bases labelled, not silently rewritten | `kasegi-shokunin/corpus/instruments/anchorcheck.py:21-48`; `citation-bases.md:82-103` |
| kumitate cite-check | re-resolve path/line/symbol/pin against origin tree; hermetic selftest separate from live | `kumitate-shokunin/LOG.md:128-133`; `kumitate-shokunin/SKILL.md:664-667` |

**Widen only after** local inventory returns empty or partial **with the sweep recorded** (S5).  
**Stop if:** Q is fully answered by local primary/secondary material with resolving pointers.  
**Hard stop without approval:** any move that would fetch a live external target (`chousa-shokunin/SKILL.md:34-36`).

### S2 — Resolve the pointer before trusting the prose
**Status:** admitted  
**Do next:** for every candidate cite, run the mechanical resolve class before semantic reading.

| Verdict class | Meaning for search | Source |
|---|---|---|
| resolves / IN-RANGE(*) | may be read as evidence | anchorcheck docstring `:9-12` |
| UNRESOLVED / MISSING-FILE / PAST-EOF | hop broken — record and either label dead or stop chain | claim-ledger `:41-46`; anchorcheck `:13-14` |
| EPHEMERAL (`local://`, `artifact://`, `agent://`, `proc://`) | not a durable search hit | claim-ledger `:39-41`, `:439` |
| LOST-RECORDED / BASE-ABSENT / `[lost-tree]` / `[lost-base]` | historical absence kept, never counted as verified | citation-bases.md:47-67; anchorcheck `:17-19`, `:60-61` |
| labelled dead (`scratch|ephemeral|historical|…`) | counted, not failed — search may continue elsewhere | claim-ledger `:42-46`, `:440` |

**Fleet practice:** dead citations must be labelled where cited, not silently dropped (`claim-ledger.sh:45-46`). That is a search-record rule, not a cleanup rule.  
**Stop if:** the only supporting cites are EPHEMERAL or unlabelled-unresolved — claim stays **unresolved**, not asserted.

### S3 — Prefer primary / institution / practitioner over aggregator restatement
**Status:** admitted (hierarchy) + observation (export priority list)  
**Admitted hierarchy:** primary > secondary > aggregator > unsourced (`chousa-shokunin/SKILL.md:18`). Aggregator quoted as primary is a hierarchy violation — re-derive from primary (`:28`).  
**Observation (export A):** the Astra response *states* a priority of “practitioners, workshop accounts, craft associations, museums, and Japanese cultural institutions” (`research/deep-research-2026-09-28/A-shokunin-tradition.md:56`). That priority is **content of an unverified export**, not a fleet-admitted source ranking.  
**Search implication for chousa:** when multiple local sources exist, rank them by hierarchy before searching further; when only export prose exists, mark claims **unverifiable-locally**.  
**Falsification (proposal half):** a controlled loopback where an aggregator page is the only source and a primary later contradicts it without the record flagging hierarchy violation — would refute treating aggregator-as-primary as a detectable defect.

### S4 — Lexical / term-attestation pass before theory-building
**Status:** observation (export) → **proposal** for method  
**Observed moves:**

| Artifact | Move | Line |
|---|---|---|
| A | correct reading 職人気質 → katagi; reject unattested jin’i-ryū as traditional rank | `A-shokunin-tradition.md:47`, `:64`, `:71` |
| C | dictionary entries for craft terms; reject invented ladder; second search on jin’i-ryū / 自己立法 | `C-rank-taxonomy.md:53`, `:81`, `:55-60`, `:107-118` |
| C | site-scoped queries before open web (`site.nihonkiin.or.jp …`, `site.kodokanjudoinstitute.org …`) | `C-rank-taxonomy.md:44-46` |

**Proposal (method):** for any proper name / rank / technical term in Q, run a **term-attestation** sub-search (dictionary / glossary / institution page) *before* synthesizing a ladder or ontology.  
**Falsification:** a term-first pass that systematically misses a well-attested technical sense available only in primary practice docs (would show term-first is necessary-but-insufficient, not wrong — tighten to “term then primary practice,” do not drop).  
**External half is proposal-only this round:** site-scoped web search requires operator approval (S8). Local surrogate: grep lane + research dumps + dictionary-shaped local fixtures when present.

### S5 — Negative claims require an explicit sweep
**Status:** admitted  
**When claiming absence** (“no attestation”, “nothing handles X”, “absent everywhere”):

1. write the **search command** (or bounded command set)
2. write the **scope** (paths, bases, date)
3. write the **result** (0 hits / only labelled-dead / BASE-ABSENT)
4. keep the sweep even if later a hit appears (errata append-only — `QUALITY.md:4`)

**Evidence:** `CORPUS.md:38-40`; `PROTOCOL.md:336-337` (“an absence claim its search sweep”); `chousa-shokunin/SKILL.md:44`.  
**Export parallel (unverified):** A and C phrase negatives (“I haven’t found evidence…”, “I found no authoritative attestation…”) at `A-shokunin-tradition.md:47,64` and `C-rank-taxonomy.md:53,109` **without** a reproducible sweep command — this is the defect class the admitted rule exists to catch.  
**Stop (honest stop):** sweep complete under declared scope with 0 resolving hits → absence claim may be stated **scoped** (“absent under sweep S”), never universal.  
**Widen:** expand scope (sibling lanes, alternate bases, synonym list) and re-run; do not upgrade “scoped absent” to “globally absent” without the wider sweep.

### S6 — Walk citation chains hop-by-hop; stop at the first broken hop
**Status:** admitted  
**Procedure:**

1. take the cite as written
2. resolve hop → artifact bytes (or label unresolved)
3. read the cited span (not a restatement)
4. if the span itself cites further, continue
5. **on dead hop:** record hop id, reason, stop that chain (`chousa-shokunin/SKILL.md:19`, `:29`)

**Do not:** stop at a summary of the citation (`SKILL.md:19` Never column); average disagreeing sources (`:30`).  
**Fleet parallel:** claim-ledger refuses ephemeral session URIs as durable cites (`claim-ledger.sh:39-41`); kasegi refuses silently rewriting lost roots to mirror (`citation-bases.md:97-100`).  
**Search widen after break:** start a **new** chain from a different seed; do not paper over the broken hop.

### S7 — Split evaluation axes; do not search for a single collapsed score
**Status:** observation (export) + weak admitted echo  
**Observation (export):** all three artifacts separate multi-axis frames rather than one ladder:

| Artifact | Axes stated | Line |
|---|---|---|
| A | competence / independence / improvement / transmission | `A-shokunin-tradition.md:54` (also `research/README.md:13-14`) |
| B | task competence / retention / evidence fidelity / cross-domain transfer / operating cost | `B-multiagent-knowledge.md:57` |
| C | knowledge provenance / demonstrated competence / authority to modify / authority to create | `C-rank-taxonomy.md:67` |

**Admitted echo:** fleet scorecards already separate axes and demand per-cell pointers (`kagi-shokunin/corpus/claim-ledger.sh:66-74` cells mode; `PROTOCOL.md` scorecard as claims).  
**Search implication:** when Q mixes “is it true?” with “may it act?”, run **separate searches** per axis; a hit on competence is not a hit on minting authority.  
**Proposal:** encode axis-split as a mandatory pre-search checklist row.  
**Falsification:** a domain where one calibrated external contest collapses all axes (e.g. pure strength rating) and axis-split adds only noise — mark that domain as single-axis exception with evidence.

### S8 — External / live-target widen only under an approval table
**Status:** admitted (boundary) · **proposal** (window procedure)  
**Admitted boundary:** no external live-target research without operator approval; without an approval table the window is **loopback-only** (`chousa-shokunin/SKILL.md:34-36`; `PROVINCE.md:10-12`).  
**Observation (export):** A/B/C each show “Searched the web” (`A:42`, `B:42`, `C:42,55`) and C shows site-scoped strings (`C:44-46`) — operator-burner session, **not** a chousa-approved window, and **not** Deep Research (`research/README.md:6-8`).  
**Proposal — widen ladder for an *approved* external window:**

| Step | Move | Stop/advance |
|---|---|---|
| E0 | restate Q + local exhaustion proof (S1+S5) | no local exhaustion → refuse external |
| E1 | institution / primary-domain sites (site: filters) | hit with resolvable capture → prefer over open web |
| E2 | dictionary / standards bodies | term attestation |
| E3 | open web / arXiv / general search | only if E1–E2 incomplete |
| E4 | capture: URL, retrieved span, retrieval time, content hash if available | missing capture → claim unverifiable |
| E5 | chain-walk any fresh cites (S6) under the same approval scope | hop outside scope → new approval row or stop |

**Falsification of E-ladder:** an approved window where E3 open-web finds a primary that E1 site-scope systematically misses *and* E1 was scoped to the correct institutions — would force “open web in parallel with site-scope,” not “open web first.”  
**This round’s external approval table is a sibling deliverable (ApprovalTable member), all rows `pending` — not permission.**

### S9 — Knowledge-change unit and anti-collapse (content caution, method proposal)
**Status:** observation (export B) → **proposal** (search-record hygiene)  
**Observation (export B):** iterative full rewrite can destroy useful detail (“brevity bias” / “context collapse”); prefer localized delta updates (`B-multiagent-knowledge.md:77-79`). Paper cites in the export are **unverifiable locally**.  
**Proposal for chousa records:** search findings land as **append-only deltas** (new claim rows, new rejection rows, errata blocks) — never a silent whole-record regenerate that drops prior sweeps or rejections (`QUALITY.md:4-5`).  
**Falsification:** a measured case where delta-only records accumulate contradictions that a curated full rewrite would have resolved *and* the rewrite preserves every prior sweep id — would justify a governed full-rewrite path with mandatory sweep retention, not free rewrite.

---

## 3. How to widen (decision table)

| Trigger | Widen move | Do not | Status |
|---|---|---|---|
| Local 0 hits on exact string | synonym / kanji / alternate romanization list; re-sweep | jump to live web | admitted pattern via S5; synonym list **proposal** until codified |
| Local hits are only aggregators | seek primary named by aggregator (chain S6) | quote aggregator as primary | admitted `SKILL.md:28` |
| Chain hop unresolved | label hop; seed new chain; check LOST/BASE-ABSENT vocabulary | rewrite path to a different base silently | admitted `citation-bases.md:97-100` |
| Term sense disputed | S4 term-attestation; keep both senses with sources | pick the sense that fits the roster metaphor | observation→proposal |
| Two sources disagree | report both; dual claims | average / silently prefer newer | admitted `SKILL.md:30` |
| Negative claim needs more force | broaden sweep scope + record commands | upgrade wording without new sweep | admitted `CORPUS.md:38-40` |
| Local exhausted, Q open | draft approval-table row (target, why, scope limit, evidence to capture) | fetch anyway | admitted boundary `SKILL.md:34-36` |
| Approval granted | E1→E5 ladder (S8) | start at open web | proposal |
| Axis collision (competence vs authority) | split Q; separate searches (S7) | one blended query | observation→proposal |

---

## 4. When to stop

Stopping is a **positive** act with evidence, not fatigue.

### 4.1 Hard stops (admitted)

| Condition | Action | Cite |
|---|---|---|
| No declared question | do not search | `SKILL.md:17` |
| No operator approval and next hop is live external | stay loopback-only; record need in approval table | `SKILL.md:34-36` |
| Citation chain dead hop | record hop + reason; stop that chain | `SKILL.md:29` |
| Only EPHEMERAL or unlabelled-unresolved supports the claim | claim = unresolved; stop asserting | claim-ledger `:39-46` |
| Secret/session material in path | shape-only; never content-read as “source” | `SKILL.md:39`; `CORPUS.md:48` region; province → kagi custody |
| Scope is kasegi (bounty) or kengaku (model quality) | refuse; route out of province | `PROVINCE.md:10-11`; `SKILL.md:37-38` |

### 4.2 Soft stops (satisfied window)

Stop the window as **complete enough** when all hold:

1. **Q answered or explicitly unknown** — unknowns named (`QUALITY.md:5`)
2. **Every positive claim** has a resolvable pointer to artifact + revision (`SKILL.md:43`)
3. **Every negative claim** carries its sweep (`SKILL.md:44`; `CORPUS.md:38-40`)
4. **Every rejection kept** with reason (`SKILL.md:46`)
5. **Hierarchy assigned** per source (`SKILL.md:18`)
6. **No unapproved external residual** — any remaining external need is a pending approval row, not an implicit todo

### 4.3 Premature-stop falsifiers (calibration)

A stop is **premature** if any of:

| Defect | How detected | Local example class |
|---|---|---|
| Declared universal absence without sweep | missing command | export negatives A/C (no command) |
| Stopped at citation summary | chain hop not opened | `SKILL.md:19` Never column |
| Aggregator treated as primary and primary unattempted | hierarchy row | `SKILL.md:28` |
| Local inventory not run | no S1 sweep in record | contract surfaces list |
| Broken hop dropped | rejection/hop absent | `QUALITY.md:5` |
| Axes collapsed into one unearned rank | single label for multi-axis Q | export C warning on self-certifying ranks `C-rank-taxonomy.md:53-67` (content; method: keep axes split) |

**Proposal — stop metric:** `stop_ok = claims_pointed ∧ negatives_swept ∧ rejects_kept ∧ (external_pending_only_via_table)`.  
**Falsification:** a record scoring stop_ok that a later local primary contradicts on a claim marked verified — would require a “primary-not-searched” finding id, not abandonment of stop_ok.

### 4.4 Export incompleteness as stop teacher

The three artifacts themselves are incomplete research records under chousa’s checklist:

| Checklist item | A/B/C export status (local observation) |
|---|---|
| Resolvable pointer per claim | **violated** — chips like `コトバンク`, `arxiv.org`, `+N` do not resolve to local bytes (`A:68-69,72-73`; `B:72-73`; `C:82-83,90-93`) |
| Negative claim sweep command | **violated** — prose absence without command (`A:47,64`; `C:53,109`) |
| Question declared | **partial** — user prompt states multi-part Q (`A:35`; `B:35`; `C:35`) but record shape is chat UI, not research record |
| Rejections kept | **partial** — jin’i-ryū / invented ladders rejected in prose; no structured rejection table |

**Inference (marked):** a correct stop rule would have marked these windows **incomplete / unverifiable-locally**, not “done.”  
**Unknown:** whether the live Astra session held deeper source panels not captured in the export.

---

## 5. Worked micro-example (local-only)

**Q:** Is `jin'i-ryū` an attested traditional artisan rank?

| Step | Strategy | Action (local) | Result |
|---|---|---|---|
| 1 | S0 | declare Q | done |
| 2 | S1 | read `research/README.md:11-12`, A, C | README already flags coined term |
| 3 | S2 | attempt to resolve export cites for jin’i-ryū | no local primary; chips unverified |
| 4 | S5 | sweep: `rg -n "jin.?i.?ry[uū]|人為|自己立法" research/ chousa-shokunin/ kagi-shokunin/corpus/ kasegi-shokunin/corpus/knowledge/` (illustrative) | hits are the exports + fleet notes about the coinage — **no independent primary** |
| 5 | S6 | chain from C’s dictionary discussion | stops at unverified コトバンク chip |
| 6 | Stop | claim: **unverifiable as traditional rank from local material**; treat as system coinage per `research/README.md:11-12`; external dictionary confirmation = pending approval row | hard stop without approval |

This is the template: local exhaustion → scoped negative/unknown → approval row if still needed.

---

## 6. Status census (calibration)

| ID | Strategy | Status | Falsification / residual |
|---|---|---|---|
| S0 | Question before search | admitted | gateable; refute if questionless record passes gate |
| S1 | Local inventory first | admitted | refute if external-first systematically beats documented local exhaustion |
| S2 | Resolve pointer before trust | admitted | fleet gates already enforce |
| S3 | Hierarchy prefer primary | admitted + export obs | proposal half: aggregator-trap fixture |
| S4 | Term-attestation first | observation → proposal | miss of practice-only sense |
| S5 | Negative = sweep | admitted | — |
| S6 | Chain hop walk / stop on break | admitted | — |
| S7 | Axis split | observation → proposal | single-axis domains |
| S8 | External only under approval + E-ladder | boundary admitted; E-ladder proposal | site-scope miss of primary |
| S9 | Delta records / anti-collapse | observation → proposal | governed full-rewrite counterexample |

**Counts:** admitted cores **7** (S0–S3 hierarchy core, S5, S6, S8 boundary) · proposals **4** (S4, S7, S8 E-ladder, S9) · pure observations called out inside S3/S4/S7/S9.

No strategy above claims an external page was read in this round.

---

## 7. Risks and blockers

| Risk | Notes |
|---|---|
| Treating A/B/C search theater as method authority | exports are data; their “Searched the web” lines are not chousa procedure |
| Importing B’s paper findings as chousa content | multi-agent KB failure modes are **content** (route to relevant domain lane); only the *craft* pattern (delta vs rewrite, evaluate changes not self-score) is method-adjacent and still proposal |
| Silent base rewrite when roots are absent | forbidden by kasegi citation-bases; chousa must reuse LOST-*/label pattern, not invent “close enough” paths |
| Premature universal negatives | largest calibration failure mode visible in the survey material |
| Blocker for deeper S4/S8 | operator external window not approved this round — correctly leaves E-ladder untested |

---

## 8. Evidence index (paths touched)

- `research/README.md:6-14`
- `research/deep-research-2026-09-28/A-shokunin-tradition.md:35,42,47,54,56,64,71`
- `research/deep-research-2026-09-28/B-multiagent-knowledge.md:35,42,57,77-79`
- `research/deep-research-2026-09-28/C-rank-taxonomy.md:35,42-46,53-60,67,81-83,107-118`
- `chousa-shokunin/SKILL.md:17-19,28-30,34-39,43-46`
- `chousa-shokunin/PROVINCE.md:5-13`
- `chousa-shokunin/corpus/QUALITY.md:3-5`
- `CORPUS.md:33-40`
- `PROTOCOL.md:336-337`
- `kagi-shokunin/corpus/claim-ledger.sh:31-46,66-74,429-450`
- `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-61`
- `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-67,82-103`
- `kumitate-shokunin/LOG.md:128-133`
- `kumitate-shokunin/SKILL.md:664-667`

---

## 9. Hand-off

Parent may land a `corpus/knowledge/search-strategy-taxonomy.md` from this advisory: keep **admitted** rows as rules with path:line; keep **proposal** rows with falsification; state the export-unverified central finding in the corpus note’s header. Companion members: ApprovalTable (S8 rows), StopRule, NegativeClaimSweep, PrimarySourceHierarchy, CrossLanePrecedent.
