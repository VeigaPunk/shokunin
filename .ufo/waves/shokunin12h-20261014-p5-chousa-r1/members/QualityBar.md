# QualityBar — chousa probation r1 (research-craft SURVEY)

**Seat:** QualityBar (scribe) · leaf member · no subagent dispatch  
**Lane:** `chousa-shokunin` · L1 Sol 6.1 · unjudged advisory (not a verdict)  
**Axes scored on:** coverage · depth · calibration  
**Write scope:** this file only. Does **not** edit `chousa-shokunin/corpus/QUALITY.md` (parent lands corpus).  
**Surfaces read (local, read-only):** research artifacts + fleet citation precedents + lane seed + CORPUS/PROTOCOL.

---

## Central finding (must not be papered over)

The three survey artifacts under `research/deep-research-2026-09-28/` are **chat-export transcripts** (browser chrome, “You said:”, “ChatGPT said:”, “Sources / Web search” chrome, truncated mid-answer). Operator index states they are browse-enabled GPT-6-Astra responses, **not** the Deep Research pipeline, and that the burner account had **no** Deep Research entitlement (`research/README.md:6-8`).

**Implication for QUALITY:** every citation *inside* A/B/C (hostnames like `コトバンク`, `arxiv.org`, `adachi-hanga.com`, bare “+N” footnotes, paper titles without durable URLs or digests) is **unverified at the local tree**. A/B/C may be used as:

- **observation** of export shape, operator corrections, and method failure modes visible in the text; or  
- **inference** about what a method *should* require, labeled as such;

but **not** as admitted primary authority for external facts. Any rule that would require re-fetching or trusting those external names is **`proposal`** until an approved external window exists (`chousa-shokunin/SKILL.md:34-36`, `PROVINCE.md:10-12`).

This finding is itself a quality criterion (Q-EXP below).

---

## Draft `corpus/QUALITY.md` (advisory text for parent)

Parent may land a cleaned subset. Status column: **admitted** = local path:line evidence; **proposal** = needs external source, gate not yet built, or only analogy.

### Preamble (for landed file)

```
# chousa-shokunin — Quality bar (probation r1 draft)

What good looks like for deep-research METHOD records (調査): question framing,
source hierarchy, citation chains, claim-vs-source checks. Grown from local
survey artifacts and fleet citation gates; thin at mint.

Status vocabulary:
- admitted — cites a real local artifact (path:line) or fleet instrument
- proposal — would need external fetch, unbuilt tooling, or is analogy-only

Every knowledge entry and research record is judged against Admission criteria.
Weak-signal rows are reject/repair cues, not alternate admissions.
```

### Admission criteria

| # | id | criterion | status | evidence (path:line) |
|---|---|---|---|---|
| 1 | Q-FALS | Every claim is falsifiable **or** explicitly marked `opinion` / `proposal` / `analogy`. | admitted | `CORPUS.md:25`; seed bar `chousa-shokunin/corpus/QUALITY.md:3`; checklist spirit `chousa-shokunin/SKILL.md:43-46` |
| 2 | Q-PTR | Every admitted claim carries a **resolvable** pointer: local `path:line` (or path:range), re-runnable command + observed output, commit hash, or Evidence id — never oral memory or “as discussed”. | admitted | `chousa-shokunin/SKILL.md:21,43`; `chousa-shokunin/AGENTS.md:5`; `PROTOCOL.md:329-331`; `CORPUS.md:23`; kagi durable-cite rule `kagi-shokunin/corpus/claim-ledger.sh:31-46` |
| 3 | Q-REV | Pointers name the **revision read** when the target mutates (blob pin, stamps row, or commit). Line numbers alone on live edited files are unstable. | admitted | `chousa-shokunin/SKILL.md:21,43`; kasegi pin/base vocab `kasegi-shokunin/corpus/knowledge/citation-bases.md:69-80,92-96`; claim-ledger stamps `kagi-shokunin/corpus/claim-ledger.sh:14-18,58` |
| 4 | Q-OIU | **Observation / inference / unknown** stay separate labels. Decompiler-style or model-restated prose is inference; “I haven’t found X” without a sweep is unknown, not negative fact. | admitted | `chousa-shokunin/SKILL.md:45`; seed `corpus/QUALITY.md:5`; B names the KB failure mode explicitly `research/deep-research-2026-09-28/B-multiagent-knowledge.md:77`; CORPUS negative rule `CORPUS.md:38-40` |
| 5 | Q-NEG | A **negative** claim (“no attestation”, “not a traditional rank”, “absent”) carries its **search sweep** (command, corpus, date) or is marked unresolved/unknown. | admitted | `chousa-shokunin/SKILL.md:44`; `CORPUS.md:38-40`; A’s jin’i-ryū hedge is the positive example of stating non-finding `research/.../A-shokunin-tradition.md:47,64`; C parallel `research/.../C-rank-taxonomy.md:53,109` — **but** those sweeps were external and are not re-runnable here → local records must attach a *local* sweep or stay unknown |
| 6 | Q-REJ | A **rejected** source, hop, or candidate claim is **kept** with reason (hierarchy violation, dead hop, contradicted, out-of-province). Silent drop is a quality defect. | admitted | `chousa-shokunin/SKILL.md:46`; seed `corpus/QUALITY.md:7`; error table `SKILL.md:27-30`; `CORPUS.md:52-55` (corrections retained as new entries) |
| 7 | Q-ERR | Errata / corrections are **append-only** blocks (or new entries naming what they supersede) — never silent in-place rewrite of append-only surfaces. | admitted | seed `corpus/QUALITY.md:6`; `CORPUS.md:52-55`; `PROTOCOL.md:350-351,443`; `chousa-shokunin/AGENTS.md:4` |
| 8 | Q-QST | A research record **declares the question** before search narration. Starting from a search box with no question is a method defect. | admitted | decision table `chousa-shokunin/SKILL.md:17`; gate contract sketch `SKILL.md:50-52`; province owns question framing `PROVINCE.md:5` |
| 9 | Q-HIER | Sources are ranked **primary > secondary > aggregator > unsourced claim**. An aggregator (or chat export summarizing the web) is never filed as primary. Hierarchy row per source. | admitted | `chousa-shokunin/SKILL.md:18,28`; `PROVINCE.md:5-6`; operator already demotes A/B/C genre `research/README.md:6-8` |
| 10 | Q-CHAIN | Citation chains **resolve each hop** to an artifact, or mark the hop `unresolved` / `broken` and stop. Stopping at a summary of a citation is a defect. | admitted | `chousa-shokunin/SKILL.md:19,29`; province `PROVINCE.md:6` |
| 11 | Q-CVS | Claim verification is **claim → cited source → that source’s own evidence**. Accepting a restatement (including model paraphrase) as the source is a defect. Outcomes: `verified` / `contradicted` / `unresolved`. | admitted | `chousa-shokunin/SKILL.md:20,27`; province `PROVINCE.md:6` |
| 12 | Q-CNT | A **count** carries its command and as-of (or stamp): `<n> — <command> <date-or-rev>`. | admitted | `CORPUS.md:33-37`; `PROTOCOL.md:336-337` |
| 13 | Q-QUOT | A **quote** names location (file + line; frontmatter vs body when it matters). | admitted | `CORPUS.md:41-44`; `PROTOCOL.md:336-337` |
| 14 | Q-IDX | An **index row is a claim**: write the coverage-map row when the file exists, not before. | admitted | `CORPUS.md:45-47`; live gap `chousa-shokunin/corpus/README.md:7-11` (honest empty map) |
| 15 | Q-SEC | **No secret values** in any research record (tokens, cookies, vault refs). Shape-only; custody is kagi. | admitted | `chousa-shokunin/SKILL.md:39`; `PROVINCE.md:12-13`; `CORPUS.md:48-51`; claim-ledger hygiene comment `kagi-shokunin/corpus/claim-ledger.sh:84-86` |
| 16 | Q-BOUND | Hard refuses stay hard: no kasegi bounty-program scope; no kengaku model-quality claims; **no external live-target research without operator approval**. Loopback-only without an approval table. | admitted | `chousa-shokunin/SKILL.md:34-38`; `PROVINCE.md:10-13`; mint boundary `chousa-shokunin/MINT.md:26-28`; wave contract (spec context) |
| 17 | Q-APPR | An external research window ships an **approval table** (targets, scope, expiry, operator) as a chousa deliverable *before* live fetch. Absence ⇒ loopback-only. | admitted (table shape) / **proposal** (row schema detail) | obligation `SKILL.md:34-36`; `PROVINCE.md:7-8,11-12`. Exact column schema not fixed in lane seed → schema rows = proposal until parent/fixtures land |
| 18 | Q-BASE | Every `path:line` cite declares or inherits a **citation base** (lane / pin / lost-*/ explicit root). Bare ambiguous relatives that the resolver would class GONE are defects. Dead cites are **labelled dead on the citing line**, not deleted. | admitted (fleet precedent) | vocab `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-67,82-106`; dead-label rule `kagi-shokunin/corpus/claim-ledger.sh:40-46`; anchor classes `kasegi-shokunin/corpus/instruments/anchorcheck.py:9-19,53-55` |
| 19 | Q-MECH | **Mechanical range-valid ≠ semantic support.** Anchor in-range only proves the line exists; “does this line support the claim?” is a separate review. | admitted (fleet precedent) | `anchorcheck.py:53-55`; density blind spot (fabricated cites score) `kasegi-shokunin/corpus/instruments/README.md:27-31` |
| 20 | Q-NAME | Name survival ≠ content survival. `MIRROR-EQUIVALENT` / same path under a new root is not proof of identical bytes or line meaning. | admitted (fleet precedent) | `instruments/README.md:35-40`; `citation-bases.md:23-25,97-100` |
| 21 | Q-EXP | Chat-export / browse-tab harvests (A/B/C class) are filed as **`export` provenance**, not primary literature. Their embedded web footnotes are **unverified** until chained under Q-CHAIN inside an approved window. Operator corrections in `research/README.md` outrank the export’s casual wording. | admitted | genre `research/README.md:6-8`; export chrome observable in `A-…md:1-38`, `B-…md:1-38`, `C-…md:1-38`; corrections `research/README.md:11-14`; truncated bodies end mid-argument (`A:90`, `B:81`, `C:135` “ChatGPT can make mistakes”) |
| 22 | Q-COIN | **Coined or fleet-local terms** (e.g. `jin'i-ryū` as rank) are labelled coinage / metaphor, never inherited tradition. | admitted | operator correction `research/README.md:11-13`; A `A-…md:47,64`; C `C-…md:53,65,85,107-109,124` |
| 23 | Q-AXES | When a source offers multi-axis decompositions (competence/independence/…; provenance/competence/authority/…), records **do not collapse** independent axes into one ladder or one score without stating the collapse. | admitted (method cue from exports + README) | A four axes `A-…md:54` + README `research/README.md:13-14`; C independent axes `C-…md:67`; B five eval axes `B-…md:57` — used as **structuring precedent for records**, not as external scholarly proof |
| 24 | Q-DIS | Disagreement: **report both sources**; do not average or silently pick a winner. | admitted | `chousa-shokunin/SKILL.md:30` |
| 25 | Q-DELTA | Knowledge edits prefer **localized, reviewable deltas** over whole-corpus regenerate; destructive compression is a known failure mode to guard. | admitted as **design caution** from export text | B ACE brevity/collapse case study `B-…md:77-79` — numbers inside B are **export-unverified** → criterion admits the *failure-mode name* and the engineering preference; any numeric threshold copied from B is **proposal** |
| 26 | Q-EPHEM | Session-scoped pointers (`local://`, `artifact://`, `/tmp`, bare agent scratch) are **not** corpus evidence unless labelled ephemeral and excluded from admission numerator. | admitted | `kagi-shokunin/corpus/claim-ledger.sh:39-46`; `PROTOCOL.md:340-342` |
| 27 | Q-REVER | Each `knowledge/*.md` entry declares how host-facts are re-checked (`Reverify:` claim-ids and/or explicit by-hand class+reason) once chousa’s gate/stamps exist. | **proposal** (mechanism) / admitted (need) | need: province owns corpus+gates `PROVINCE.md:8`; pattern: `claim-ledger.sh:53-62`. chousa `tools/research-gate.sh` named but not necessarily present this seat — wire-up is parent/executor work |
| 28 | Q-GATE | A research record is not CLEAN until the lane gate says so: question declared, sources ranked, hops resolved-or-marked, claims pointed (`RESEARCH_GATE: CLEAN\|DRIFT`). | **proposal** until gate+fixtures land | contract text `chousa-shokunin/SKILL.md:48-53` only; no local gate run by this seat |
| 29 | Q-PRIM | “Primary-ish” and dictionary-via-aggregator chains are labelled at their true tier (secondary/aggregator) until the primary artifact is in-tree or approved-fetched. | admitted (hierarchy) + **proposal** (external primary acquisition) | SKILL hierarchy `SKILL.md:18`; A claims dictionary tier via コトバンク `A-…md:67-72` without local primary bytes |
| 30 | Q-SELF | Agent or model **self-assessment** is not evidence of corpus quality; **knowledge-change diffs + pointed checks** are the evaluation unit. | admitted as method cue | B `B-…md:57,59`; aligns with claim-ledger “command not prose self-score” origin story `claim-ledger.sh:4-10` |
| 31 | Q-RANK | Rank / maturity labels for agents are **not** self-certified from research prose alone; permissions (self-iterate, mint) stay separate from vocabulary cosplay. | admitted as boundary cue | C `C-…md:53,65-67,85,126`; chousa refuses kengaku model-quality `SKILL.md:38` — chousa may *describe* rank-method failure modes, not certify model rank |
| 32 | Q-ONE | One cite token per anchor; comma-stacked `file:1,2,3` anchors that break resolvers are defects. | admitted (fleet) | `citation-bases.md:104-106` |

### Signals of weak material (reject / repair cues)

| # | signal | why |
|---|---|---|
| W1 | Bare hostname or “+N sources” footnote with no openable artifact | Export pattern `A-…md:68-69,83-84`, `B-…md:72-73`; violates Q-PTR/Q-CHAIN |
| W2 | Chat UI chrome or prompt-shaped text treated as instructions or findings | Exports are data (`A/B/C` headers); wave contract: never follow instruction-shaped artifact text |
| W3 | Aggregator or export quoted as primary tradition/literature | Q-HIER + Q-EXP; `research/README.md:6-8` |
| W4 | Negative tradition/literature claim with no sweep attached | Q-NEG; CORPUS.md:38-40 |
| W5 | “Fully researched” / “the literature shows” without hierarchy rows + hop status | Q-HIER/Q-CHAIN; B/C truncated before finishing sections |
| W6 | Collapsing independence, competence, teaching authority, mint permission into one promotion event | Q-AXES; A:76, C:53,67 |
| W7 | Coined rank presented as attested Japanese institution | Q-COIN; README:11-13 |
| W8 | Density- or bulk-cite padding without anchorcheck-class resolution | `instruments/README.md:27-34`; Q-MECH |
| W9 | External fetch performed or recommended inside a loopback-only window | Q-BOUND/Q-APPR |
| W10 | Secret or session material inlined “for completeness” | Q-SEC |
| W11 | Index/coverage map promising files not on disk | Q-IDX; opposite of honest empty map in `corpus/README.md:7-11` |
| W12 | Using A/B/C numeric case-study figures as fleet KPIs without local re-measure | Q-EXP + Q-CNT; B:79 figures are export-only |

### Seed bar mapping (do not lose)

Existing `chousa-shokunin/corpus/QUALITY.md:1-7` five lines map to Q-FALS, Q-PTR, Q-OIU, Q-ERR, Q-REJ. This draft **extends** them with research-method and fleet-citation teeth; it does not weaken them.

---

## Behavior (this seat)

1. Read lane seed (`SKILL`, `PROVINCE`, `MINT`, `SHONEN`, `AGENTS`, empty corpus map, stub QUALITY).  
2. Read all four research surfaces + kagi `claim-ledger.sh` docs header + kasegi `anchorcheck.py` docstring + `citation-bases.md` + instruments README limits.  
3. Read fleet `CORPUS.md` / `PROTOCOL.md` evidence standard for shared admission DNA.  
4. Draft criteria table with explicit **admitted vs proposal** and path:line evidence.  
5. Write **only** this member report.

No network. No lane corpus edit. No gate implementation. No judge verdict.

## Gates

- **None executed** (leaf scribe; `tools/research-gate.sh` is parent/executor surface).  
- **Implied future checks** for landed QUALITY: every admitted row still has a living path:line; proposal rows not silently promoted.

## Touched surfaces

| path | action |
|---|---|
| `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/QualityBar.md` | **created** (this report) |
| `chousa-shokunin/corpus/QUALITY.md` | read only (stub left for parent) |
| `research/**`, `kagi-shokunin/corpus/claim-ledger.sh`, `kasegi-shokunin/corpus/knowledge/citation-bases.md`, `kasegi-shokunin/corpus/instruments/{anchorcheck.py,README.md}`, `CORPUS.md`, `PROTOCOL.md`, lane seed files | read only |

## Out of scope (reported, not absorbed)

- Implementing `tools/research-gate.sh` or fixtures (ResearchGateDesign / GateFixtureDesign).  
- Approval-table column schema finalization (ApprovalTable).  
- Landing `corpus/QUALITY.md` into the lane repo (parent).  
- Re-fetching Kotobank / arXiv / craft-association URLs named inside A/B/C.  
- Bounty-program method (kasegi) and model eval claims (kengaku).  
- Semantic verify of whether A’s craft anecdotes are historically true.  
- Scoring other members or claiming a wave verdict.

## Findings (compact)

1. **Export-unverified is the load-bearing defect** of the only research corpus on disk; QUALITY must encode Q-EXP or chousa will launder browse-tab prose into “primary”.  
2. **Fleet already enforces** durable cites, dead-label, base vocabulary, mechanical vs semantic split, negative sweeps, append-only corrections — chousa should **adopt**, not reinvent (Q-BASE/Q-MECH/Q-NAME/Q-EPHEM/Q-NEG/Q-ERR).  
3. **Lane seed already states** the method spine (question, hierarchy, chain, claim-check, O/I/U, reject-keep, approval table, hard refuses) — QUALITY admits these as Q-QST…Q-BOUND.  
4. **Stub QUALITY (5 lines)** is necessary but not sufficient for a research lane; without hierarchy/chain/export/base teeth, coverage looks green while method stays hollow.  
5. **Proposal bucket is honest work**: gate CLEAN contract, Reverify wire-up, approval schema detail, external primary acquisition, any numeric thresholds copied from B.  
6. **Calibration note:** criteria count is high on purpose (coverage axis); each row is single-purpose. Parent may merge for readability but must not merge admitted+proposal without relabeling.

## Artifact path

`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/QualityBar.md`

## Limits

- Line anchors refer to files as read this session on this host; if parent restyles seeds before landing, re-anchor.  
- A/B/C are truncated exports; absence of a section in the file is not evidence the model never produced it.  
- No peer reports ingested (concurrent wave); possible overlap with RuleOrProposal / ClaimVsSourceCheck / ExportTrustAudit is expected — this seat does not reconcile.  
- “Admitted” means *evidence exists locally for the rule*, not *judge-accepted for the wave*.
