# PrimarySourceHierarchy — chousa r1 survey (advisory)

Member: `PrimarySourceHierarchy` · role: executor · axes: coverage, depth, calibration  
Surfaces: `research/**`, fleet citation gates (read-only). No external fetch.  
This file is data for the parent, not a judge verdict.

## Axes (named)

| Axis | How this report serves it |
| --- | --- |
| coverage | Four tiers (primary → secondary → aggregator → unsourced) each get a definition, admit test, local anchor, and artifact/gate mapping. |
| depth | Decision table + downgrade rules + form→tier map over the three exports and two fleet gates. |
| calibration | Observation / inference / unknown kept separate; chat-export citations treated as **unverified shape**, never as resolved authority; empty tiers marked `proposal`. |

## Central finding (observation)

The three survey artifacts are **ChatGPT UI export transcripts**, not source packs:

- Operator index: `research/README.md:6-8` — burner Chrome tabs, browse-enabled GPT-6-Astra, **not** Deep Research entitlement; 9/8/10 web searches each.
- Each body ends with the product disclaimer and chrome (`A-shokunin-tradition.md:90`, `B-multiagent-knowledge.md:81`, `C-rank-taxonomy.md:135`).
- In-export “citations” are host labels, `+N` footers, bare site names, or paper title lists — **none** are `path:line` to bytes on this host, and none were re-fetched this round.

**Observation:** a claim inside A/B/C that names an external authority is at best a **narrated pointer**, not a verified primary.  
**Inference:** any METHOD rule that treats those pointers as admitted sources without a local pin would re-encode the failure mode the fleet already gates against (unresolvable / ephemeral cites).  
**Unknown (this round):** whether any named external page still contains the quoted fact — blocked by NO EXTERNAL FETCHES.

That gap is the hierarchy’s load-bearing reason for existing.

---

## Tier definitions (normative vocabulary for chousa METHOD)

Order is strict: **primary > secondary > aggregator > unsourced**.  
When classifying a claim’s support, take the **highest tier actually present and re-openable**. A lower-tier garnish does not raise the tier. A broken higher-tier pointer **downgrades** (see Decision rules).

| Tier | What it is | Admit when (local test) | Reject / downgrade when |
| --- | --- | --- | --- |
| **primary** | First-hand durable record of the fact: original text, measurement, instrument output, operator-attested local artifact bytes. | A reader on this host can open the cited object and read the supporting span without trusting a narrator. | Narrator-only paraphrase; session URI; absent base; “Sources: Web search” chrome with no payload. |
| **secondary** | Authored account **about** primaries (paper, interview write-up, museum report, craft-association program text) with a stable identity. | Named work/author/venue sufficient to request later; ideally pinned local copy or blob. | Title-only name-drop with no venue/id; chat summary of a paper with no local abstract/body. |
| **aggregator** | Index, portal, search UI, multi-hit footer, or multi-source digest that **points at** many items without being any one of them. | Useful as a **discovery trail**, never as sole warrant for a load-bearing claim. | Using `コトバンク +N` / `arxiv.org +N` as if it were the dictionary/paper. |
| **unsourced** | Assertion, recommendation, or negative claim with no recoverable pointer. | Admissible only as `proposal`, voice, or explicitly scoped negative with a recorded sweep. | Promoting to fleet knowledge without a pin or `proposal` mark. |

---

## Decision table (classify one claim)

Use top-down; stop at first matching row.

| # | Question | If yes → | Local calibration anchor |
| --- | --- | --- | --- |
| 1 | Does the cite resolve to **openable local bytes** whose span states the fact (lane `path:line`, stamp-pinned file, blob-pin show)? | **primary** (fleet-grade) | `kasegi-shokunin/corpus/knowledge/citation-bases.md:11-18` (**LANE** = re-openable internal path); mechanical twin: `IN-RANGE(LANE)` / `IN-RANGE(PIN)` in `kasegi-shokunin/corpus/instruments/anchorcheck.py:9-12`. |
| 2 | Is the support a **named authored work** (paper with authors+year, dated interview, institutional report) even if only summarized here? | **secondary** (identity may be admitted as a *future pin target*; **body not verified** this round) | `A-shokunin-tradition.md:80-88` — Adachi apprenticeship durations; Ishii Torao disciple years; Echigo Yoita program; Takenaka / Ogawa on Nishioka. Named secondary *forms*; export holds paraphrase only. |
| 3 | Is the support a **portal, search hit list, host label, or `+N` multi-source footer**? | **aggregator** | `A-shokunin-tradition.md:67-69` (`コトバンク` / `+3`); `B-multiagent-knowledge.md:71-73` (`arxiv.org` / `+6`); `C-rank-taxonomy.md:44-48` (site-scoped search lines). |
| 4 | Is there **no pointer**, only model voice, product UI, or bare “I haven’t found”? | **unsourced** | `C-rank-taxonomy.md:69` (Initiate→…Agentwright recommendation, no cite); `A-shokunin-tradition.md:47` (jin’i-ryū non-attestation without sweep log); `B-multiagent-knowledge.md:59` (explicit split: published vs **proposed engineering rules**). |
| 5 | Would confirming the fact require **network or live target**? | mark rule **`proposal`**; log in external-window table — do **not** admit | Contract: wave spec / this round’s NO EXTERNAL FETCHES; parallel fleet refusal of unresolved cites: `kagi-shokunin/corpus/claim-ledger.sh:31-46`. |

### Downgrade rules (observation → rule candidates)

| Condition | Forced tier | Gate precedent (local) |
| --- | --- | --- |
| Cite shape is `local://`, `artifact://`, `agent://`, `proc://` | unsourced / ephemeral (must label or fail) | `claim-ledger.sh:39-46`, `EPHEM_RE` at `claim-ledger.sh:439` |
| Path token does not resolve under declared bases | cannot be primary; treat as broken → unsourced unless labelled dead | `claim-ledger.sh:41-46`; anchorcheck `MISSING-FILE` / `BASE-ABSENT` (`anchorcheck.py:13-19`, `73-74`) |
| Historical absent tree kept as evidence | recorded loss, **not** validated primary | `[lost-tree]` / `[lost-base]` → `LOST-RECORDED` (`citation-bases.md:47-65`; `anchorcheck.py:17-19`) |
| Range check passes but line may not support claim | mechanical primary **candidate** only; semantic check still open | `anchorcheck.py:53-55` (range-valid ≠ semantic validity) |
| Export lists paper titles + `arxiv.org` footer only | aggregator (discovery), not secondary body | `B-multiagent-knowledge.md:63-73` |
| Negative claim (“no attestation”) without sweep artifact | unsourced negative; keep with reason, do not treat as primary absence-proof | `C-rank-taxonomy.md:107-109`; `A-shokunin-tradition.md:64` |

---

## Tier anchors (concrete local examples)

### 1. Primary — **has local examples (fleet gates + operator index)**

| Example | Path:line | Why it is primary *in-fleet* |
| --- | --- | --- |
| LANE base vocabulary | `kasegi-shokunin/corpus/knowledge/citation-bases.md:11-18` | Defines the only base where a relative `path:line` is expected to open under the lane root; bare subdir cites classified GONE if wrong shape (`:14-16`). |
| Mechanical range verdicts | `kasegi-shokunin/corpus/instruments/anchorcheck.py:9-12`, `:53-55` | `IN-RANGE(LANE|PIN|…)` prints cited lines for review; separates mechanical vs semantic. |
| Durable cite classes | `kagi-shokunin/corpus/claim-ledger.sh:31-46`, `:434-437` | Citations must resolve under corpus/knowledge/lessons/sibling-lane/ufo shapes; ephemeral URIs fail unless line-labelled. |
| Revision pin of cited artifact | `kagi-shokunin/corpus/claim-ledger.sh:14-17` | `stamps.tsv` sha256/lines/bytes — which bytes were read. |
| Operator production note | `research/README.md:6-8` | First-hand operator surface fact about how A/B/C were harvested (entitlement, date, tool). |

**Observation:** A/B/C contain **no** embedded primary payloads of Daijisen entries, arXiv HTML/PDF, Adachi pages, or JKA exam regs.  
**Inference:** for *external* tradition/ML claims, **primary is empty in the survey corpus** this round.  
**External primary admission** (fetch + pin dictionary/paper/interview bytes) = **`proposal`** → external-window table below.

### 2. Secondary — **form present in artifacts; bodies absent locally**

| Example | Path:line | Classification note |
| --- | --- | --- |
| Lexical authorities named | `A-shokunin-tradition.md:67` (Daijisen, Nihon Kokugo Daijiten, Kanjipedia); `C-rank-taxonomy.md:81` (Digital Daijisen, NKD) | Secondary *identities*; export shows aggregator footers, not entry text. |
| Workshop / museum accounts | `A-shokunin-tradition.md:80-88` | Secondary narrative forms (Adachi, Ishii, Yoita, Takenaka/Ogawa). |
| Paper lineage table | `B-multiagent-knowledge.md:63-69` (Voyager, Generative Agents, Reflexion, ACE, …) | Secondary *candidates* by title/author/year; no local PDF/HTML. |
| ACE case numbers | `B-multiagent-knowledge.md:79` (18282→122 tokens; 66.7→57.1 vs 63.7) | Load-bearing quantitative claim; **unverifiable-locally** without paper bytes. |
| Kyū/dan institutional pages named | `C-rank-taxonomy.md:89-100` (Nihon Ki-in, JKA, AJKF) | Secondary institutional targets; hosts only as bare labels. |

**Fleet secondary analogue:** a knowledge entry that cites another stamped lane doc (still primary-to-fleet, secondary-to-world) — pattern required by `claim-ledger.sh:53-65` (`Reverify:` row or by-hand class).

**Rejection kept:** treating “Sources: Voyager and Generative Agents… arxiv.org +6” (`B-multiagent-knowledge.md:71-73`) as secondary **bodies** — reason: footer is an aggregator collapse, not six openable works.

### 3. Aggregator — **abundant local examples in all three exports + README**

| Example | Path:line | Shape |
| --- | --- | --- |
| Kotobank multi-hit footers | `A-shokunin-tradition.md:68-69`, `:72-73`; `C-rank-taxonomy.md:82-83`, `:121-122`, `:131` | Portal brand + `+N` |
| arXiv multi-hit footer | `B-multiagent-knowledge.md:51-52`, `:72-73` | Host + `+6` |
| Site-scoped search chrome | `C-rank-taxonomy.md:44-48` | `site.nihonkiin.or.jp…`, `site.kodokanjudoinstitute.org…`, `10 more` |
| Bare hosts without scheme | `A-shokunin-tradition.md:83` (`adachi-hanga.com`); `C-rank-taxonomy.md:90-103` | Discovery residue, not URLs |
| Tab index digest | `research/README.md:10-17` | Operator aggregator over A/B/C (meta-secondary to the exports) |

**Fleet aggregator analogue:** citation **census** / multi-doc scan summaries (e.g. `claim-ledger` citations mode counting cites across docs — `claim-ledger.sh:511-579`) — counts and class labels, not the underlying fact.

**Rule candidate:** an aggregator hit may justify **opening a fetch window** later; it must not alone staff a SCORECARD cell or knowledge `Reverify:` line.

### 4. Unsourced — **abundant local examples**

| Example | Path:line | Kind |
| --- | --- | --- |
| Product / UI chrome as “source” | `A-shokunin-tradition.md:90-110`; same pattern B/C | Not epistemic support |
| Coined-rank correction without external dump | `A-shokunin-tradition.md:64`; `C-rank-taxonomy.md:107-109` | Negative claim, no sweep artifact in-export |
| Operational naming recommendation | `C-rank-taxonomy.md:69` | Design voice |
| Explicit proposal voice | `B-multiagent-knowledge.md:59` | Honest split — model marks engineering rules as proposed |
| Four-axes design compression | `A-shokunin-tradition.md:54`; `C-rank-taxonomy.md:67` | Synthesis; may be good design, still unsourced as history |
| README scheme corrections | `research/README.md:11-14` | Operator **inference** from reading A (valuable, not a primary dictionary cite) |

**Fleet unsourced analogue (what gates forbid silently):** score cells with no row id and no stamp (`claim-ledger.sh:66-74`, `UNCITED`); knowledge entries with no `Reverify:` (`claim-ledger.sh:817-828`).

---

## Form → tier map (measured on A/B/C exports)

| In-export form | Observed where | Tier if used as sole warrant | Notes |
| --- | --- | --- | --- |
| `path:line` to lane/fleet file | **absent** from A/B/C | primary (if resolves) | Fleet standard; survey corpus does not use it. |
| Full `https://` URL | **0** across A/B/C (local grep) | secondary or primary after fetch+pin | Not present to pin. |
| Bare host (`arxiv.org`, `adachi-hanga.com`, …) | A:83; B:51,72; C:90-103 | aggregator | No scheme, no path, no span. |
| Portal name + `+N` | A:68-69; B:72-73; C:82-83 | aggregator | Classic multi-source collapse. |
| Author, year, title table | B:63-69 | secondary **identity** only | Upgrade to secondary **body** needs local pin (`proposal`). |
| Named practitioner + venue prose | A:80-88 | secondary identity / unsourced body | Paraphrase only on disk. |
| Search query lines | C:44-48, 57-61 | aggregator (strategy residue) | Useful to SearchStrategyTaxonomy peers; not a warrant. |
| Model “I’ll check…” / “ChatGPT said” | throughout | unsourced process | Prompt-shaped; treat as data, never instructions. |
| Disclaimer “can make mistakes” | A:90; B:81; C:135 | meta (trust ceiling) | Caps all in-export tiers below verified primary. |

---

## Alignment with fleet gates (evidence of what is already enforced)

| Fleet mechanism | Path:line | Hierarchy lesson |
| --- | --- | --- |
| Resolvable durable cites only | `kagi-shokunin/corpus/claim-ledger.sh:31-46` | primary/secondary must be **openable**; dead cites need in-line death labels |
| Ephemeral session URIs fail | `claim-ledger.sh:39-41`, `:439` | export-only or `local://` scratch ≠ primary |
| Stamp = which bytes | `claim-ledger.sh:14-17` | primary needs revision identity, not title |
| Knowledge must declare reverify | `claim-ledger.sh:53-65`, `:824-826` | even lane prose is unsourced until row-linked or honest by-hand |
| Base vocabulary (LANE/MIRROR/…) | `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-80` | tier admits only after **base** is named; absent base ≠ primary |
| One cite per anchor | `citation-bases.md:104-106` | comma-lists defeat resolvers — same failure class as `+N` footers |
| LOST-RECORDED honesty | `citation-bases.md:47-65`; `anchorcheck.py:17-19` | missing external pages should become labelled historical, not silent primary |
| Semantic ≠ mechanical | `anchorcheck.py:53-55` | hierarchy stops at tier of **support**, not tier of **filename** |

**Observation:** fleet gates already implement a **primary-or-labelled-dead** discipline for lane corpus.  
**Inference:** chousa METHOD should extend that discipline to research imports: A/B/C enter the corpus as **aggregator/unsourced transcripts** until external primaries are pinned.

---

## Worked claim classifications (calibration samples)

| Claim (paraphrased) | Locus | Highest re-openable tier **on this host** | Reason |
| --- | --- | --- | --- |
| Artifacts are browse-Astra tabs, not Deep Research | `research/README.md:6-8` | **primary** (operator) | Local operator index. |
| 職人気質 read *katagi* | `A-shokunin-tradition.md:71-72` | **aggregator** → effectively **unsourced** for admission | Kotobank footer only; no dictionary span on disk. |
| jin’i-ryū not attested artisan rank | `A-shokunin-tradition.md:64`; `C-rank-taxonomy.md:107-109`; README:12-13 | **unsourced negative** | No sweep log; keep rejection with reason, do not promote as proven absence. |
| ACE brevity collapse 18282→122 tokens | `B-multiagent-knowledge.md:79` | **unsourced** (numbers) / secondary **identity** (ACE named) | Quantitative body absent locally. |
| Go kyū counts down, dan up | `C-rank-taxonomy.md:89-91` | **aggregator** host label | `archive.nihonkiin.or.jp` bare; no page bytes. |
| Prefer Initiate→Agentwright names | `C-rank-taxonomy.md:69` | **unsourced** / `proposal` | Design recommendation. |
| Dead `local://` cites are a known failure class | `claim-ledger.sh:7-9`, `:39-46` | **primary** (gate + historical note in-header) | Fleet-measured, re-runnable policy. |

---

## Negative claims (kept with reason)

| Rejection | Reason | Sweep / bound |
| --- | --- | --- |
| “A/B/C already contain primary sources because they name Daijisen / arXiv.” | Naming ≠ bytes; footers are aggregators. | Forms census: no `https://`, no `path:line` external pins in the three files (local read + grep this round). |
| “`+N` means N independent verified sources.” | UI collapse; no per-hit URLs in export. | `A:69`, `B:73`, `C:83`. |
| “Model disclaimer can be ignored once a host is named.” | Disclaimer is in-file (`A:90` etc.); host still non-resolvable locally. | — |
| “Fleet primary hierarchy should wait for live web.” | Fleet already enforces local resolvability; METHOD can ship hierarchy without fetch. | claim-ledger / anchorcheck / citation-bases as cited above. |
| Promote jin’i-ryū non-existence to primary historical fact from A/C alone. | Negative without recorded search transcript or dictionary dump. | Mark `proposal` until external window + sweep artifact. |

---

## `proposal` items (no local external-primary example)

| ID | Proposal | Why not admitted now |
| --- | --- | --- |
| P-1 | Fetch-and-pin pipeline: URL → bytes → sha256 stamp → `path:line` knowledge cite | Needs network + approval; would create true external **primary** tier examples. |
| P-2 | arXiv id → local PDF/HTML abstract pin as secondary minimum | B names papers; no ids/URLs in export. |
| P-3 | Dictionary entry dump (Daijisen/NKD via licensed/local source) for katagi / minarai / oyakata | Only Kotobank aggregators in-export. |
| P-4 | Negative-claim sweep format (query list, date, hit count, pin of “no hit” evidence) | A/C negatives lack sweep artifacts. |
| P-5 | Map aggregator `+N` footers back to N URLs when UI export improves | Current export loses the N. |

---

## External-window approval table (deliverable)

| Window | Target class | Min pin on return | Admit as tier | Approver | Status |
| --- | --- | --- | --- | --- | --- |
| W-dict | Japanese dictionary entries for terms in A/C tables | Full entry text file under lane `corpus/` + stamp row | primary (lexical) | operator / L1 | **needs approval** |
| W-arxiv | Papers listed in B:63-69 | PDF or HTML + sha256; quote spans for ACE numbers | secondary body → supports primary quotes | operator / L1 | **needs approval** |
| W-craft | Adachi, Taitō interview, Yoita association, Takenaka report | Saved HTML/PDF + date | secondary | operator / L1 | **needs approval** |
| W-rank | Nihon Ki-in, JKA, AJKF pages cited in C | Saved HTML + date | secondary | operator / L1 | **needs approval** |
| W-portal | Kotobank only as index | Optional; never sole warrant | aggregator only | n/a | **discouraged as admit path** |

No window was opened this round (contract).

---

## Decision cheat-sheet (for research-gate / corpus notes)

```
claim support
  ├─ openable local span? ──────────────► PRIMARY
  ├─ named work, body pinned later? ────► SECONDARY (identity now / body after W-*)
  ├─ portal, host, +N, search chrome? ──► AGGREGATOR (discovery only)
  └─ voice, bare negative, UI chrome? ──► UNSOURCED (proposal or labelled)
network required to improve tier? ──────► proposal + approval table row
fleet path cite unresolved/ephemeral? ─► fail or label (existing gates)
```

---

## Observation / inference / unknown (summary)

| Class | Content |
| --- | --- |
| **Observation** | A/B/C are chat exports; citation forms are hosts, portals, `+N`, title lists; zero local external primary bytes; fleet gates already require resolvable durable cites and labelled dead ones. |
| **Inference** | METHOD hierarchy should grade research imports **below** fleet primary until pins exist; aggregator footers are the dominant false-authority pattern in this harvest. |
| **Unknown** | Live correctness of any external fact narrated in A/B/C; true hit-count behind each `+N`; whether jin’i-ryū appears under other spellings in sources not on disk. |

---

## Files read (exclusive evidence set)

- `research/README.md`
- `research/deep-research-2026-09-28/A-shokunin-tradition.md`
- `research/deep-research-2026-09-28/B-multiagent-knowledge.md`
- `research/deep-research-2026-09-28/C-rank-taxonomy.md`
- `kagi-shokunin/corpus/claim-ledger.sh` (header + citation/docs modes)
- `kasegi-shokunin/corpus/instruments/anchorcheck.py` (header + verdict classes)
- `kasegi-shokunin/corpus/knowledge/citation-bases.md`
- Wave `spec.json` item `PrimarySourceHierarchy`

## Risks / blockers

- **Risk:** peer reports may quote A/B/C host labels as if verified — hierarchy says downgrade.  
- **Risk:** README corrections (`katagi`, coined jin’i-ryū) are strong operator inferences; still not dictionary primary.  
- **Blocker:** no external primary examples in-corpus; P-1…P-4 and W-* remain approval-gated.  
- **Non-blocker:** unsourced and aggregator tiers are fully exemplifiable from local artifacts alone.

## End state

Decision table delivered: **primary > secondary > aggregator > unsourced**, each tier anchored to concrete local paths. External primary admission paths marked `proposal` with an approval table. Central finding stated: export citations are unverified shapes, not admitted primaries.
