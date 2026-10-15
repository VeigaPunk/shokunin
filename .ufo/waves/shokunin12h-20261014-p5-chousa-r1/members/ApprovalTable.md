# Operator-approval table — future external research window

**Member:** `ApprovalTable`  
**Wave:** `shokunin12h-20261014-p5-chousa-r1` (chousa probation r1 · research-craft SURVEY)  
**Status of this file:** deliverable only. **Not** an approval, grant, or fetch authorization.  
**Every row `approval_state`:** `pending`  
**This round's network posture:** NO EXTERNAL FETCHES (contract). Rows below are a queue for a *future* operator-opened window.

---

## 0. What this table is

| Field | Meaning here |
|---|---|
| `target` | Named external surface a future fetch might hit (host, paper, institution, dictionary lemma). |
| `why` | Claim class inside the local survey corpus that is currently **unverified** without that surface. |
| `scope_limit` | Hard ceiling if approved: path/lemma/paper id only; no bounty, no model-quality scoring, no secret capture. |
| `evidence_to_capture` | Byte-stable artifacts the operator/window must land so later rounds can cite `path:line` (fleet discipline). |
| `approval_state` | Always `pending` in this deliverable. |

**Axes this table serves:** coverage (every named external cite class in A/B/C + README), depth (why + capture recipe + limit), calibration (pending-only; proposal vs admitted kept separate; hard refusals explicit).

---

## 1. Central finding (must not be papered over)

**Observation (local only):**  
`research/deep-research-2026-09-28/{A,B,C}-*.md` are **chat-export transcripts** (Chrome/ChatGPT UI chrome, “Sources / Web search”, collapsed “+N” counters), not a pinned primary corpus.

| Local anchor | Observation |
|---|---|
| `research/README.md:5-8` | Fired 2026-09-28 on burner CDP 9222; **no** Deep Research entitlement — browse-enabled GPT-6-Astra (9/8/10 web searches), not Deep Research pipeline. |
| `research/deep-research-2026-09-28/A-shokunin-tradition.md:67-69,72,83-84,90` | Host chips (`コトバンク`, `adachi-hanga.com`, `+N`) and “ChatGPT can make mistakes” footer; no stable URL, DOI, quote, or retrieved byte hash. |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md:51,71-73,81` | `arxiv.org` chip and paper name table; no arXiv ids, PDF hashes, or quote spans. |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md:44-48,82-83,90-103,121,131,135` | Search-query lines and institution chips; “10 more” collapsed; same unverified footer. |

**Inference (labeled):** Any design rule that *depends* on those external facts is at best a **proposal** until a future window captures primary bytes under operator approval.

**Unknown:** Exact URLs, retrieval timestamps, and whether the model’s paraphrases match the primary pages. This table does not invent them.

**Fleet precedent (evidence of what we already enforce locally — not an external grant):**

| Precedent | What it enforces | Local anchor |
|---|---|---|
| kagi `claim-ledger.sh` citation mode | Committed Markdown cites must resolve to durable paths; `local://` / session URIs are EPHEMERAL and fail unless the citing line labels them dead | `kagi-shokunin/corpus/claim-ledger.sh:31-46,986-994` |
| kagi `docs` entry audit | Knowledge entries declare `Reverify:` (claim rows or explicit by-hand class) + stamp pin | `kagi-shokunin/corpus/claim-ledger.sh:53-65,820-828,957-965` |
| kasegi `citation-bases.md` | Named bases (LANE/MIRROR/LOST-TREE/…); lost bases stay labeled, never silently rewritten | `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-67,82-106` |
| kasegi `anchorcheck.py` | `path:line` range-checked; BASE-ABSENT / LOST-RECORDED distinct from “looks fine” | `kasegi-shokunin/corpus/instruments/anchorcheck.py:67-74,101-104` + `…/instruments/README.md:12-14,41-46` |
| density alone is insufficient | Fabricated `path:line` scores like a real one → need resolve+anchor | `kasegi-shokunin/corpus/instruments/README.md:27-31` |

**Implication for chousa METHOD:** a future external window must land captures that can become **LANE-internal** stamped artifacts (or an explicit new base class, operator-named), so gates like citation/anchorcheck can run without network.

---

## 2. Hard refusals (never rows for approval)

These stay **out of table** even in a future window (contract hard boundary):

| Refused class | Reason |
|---|---|
| Bounty-program / live VDP / kasegi target research | Lane boundary: chousa ≠ kasegi |
| Model-quality / kengaku scoring of GPT-6-Astra or competitors | Lane boundary: chousa ≠ kengaku; export quality is process evidence only |
| Secrets, session tokens, burner-account credentials, 1Password/op material | Shape-only if ever described; no capture of secret bytes |
| Unscoped “search the web for shokunin” crawls | Must be row-scoped targets below |
| Treating this table as permission | Deliverable ≠ grant |

Rejected-with-reason (kept): any row that would require live exploitation, phishing, or unauthorized access — **not proposed**.

---

## 3. Capture contract (applies to every `pending` row if later approved)

Minimum evidence bundle per approved target (proposal for parent `tools/research-gate.sh` / METHOD corpus — **not admitted as enforced** until parent lands it):

1. **Identity:** canonical URL or stable id (DOI / arXiv id / ISBN / institution page id).  
2. **Retrieval stamp:** UTC time, tool/user-agent class, operator id.  
3. **Content address:** SHA-256 of raw response body (HTML/PDF/plain).  
4. **Excerpt pin:** quoted span(s) that support the claim, with in-document locator (page, section heading, or byte offset) — enough to re-anchor after reflow.  
5. **Claim linkage:** which local export line(s) the capture is meant to confirm, refute, or leave unknown (`research/...:line`).  
6. **Disposition:** `confirms` | `refutes` | `partial` | `not-found` | `paywalled` | `ambiguous` — never silent drop.  
7. **Base label:** future lane path under an operator-chosen root (e.g. `chousa-shokunin/corpus/external/...`) so cites become `path:line` after ingest.

Negative claims after a window still need a **sweep** (what was searched, what was not found) — fleet negative-claim rule.

---

## 4. Approval table

All `approval_state = pending`. Grouped by survey artifact. IDs are stable row keys for parent SCORECARD/LOG.

### 4.A — Tradition / terminology (from `A-shokunin-tradition.md` + README)

| id | target | why | scope_limit | evidence_to_capture | approval_state |
|---|---|---|---|---|---|
| A-01 | Kotobank lemma cluster for 見習い / 弟子 / 職人 / 極み / 職人気質 (Daijisen, Nihon Kokugo Daijiten entries as aggregated) | Export asserts lexical distinctions and **katagi** (not kishitsu) reading from these dictionaries (`A:60-72`, README corrections `research/README.md:11-12`) | **GET** only named lemma pages; JP/EN as published; no account login; no bulk dump of unrelated Kotobank graph | Raw HTML + sha256; exact reading/gloss quotes; publisher attribution on-page; map each quote → export claim row (minarai/deshi/shokunin/kiwami/katagi) | pending |
| A-02 | Japan Kanji Aptitude Testing Foundation **Kanjipedia** entries for the same kanji set | Named alongside Daijisen/NKD as lexical source (`A:67`) | Single-character / compound entries cited by export only; no scrape of test prep corpus | Entry text + url + sha256; note if paywall/login blocks | pending |
| A-03 | Primary dictionary publishers **direct** (Shōgakukan Digital Daijisen / NKD), not only Kotobank mirror | Export may be one hop from primary; Kotobank is an aggregator chip (`A:68,72`) | Resolve publisher-canonical pages for the same headwords; stop after headword set in A-01 | Canonical URL, headword, reading, definition spans, license/ToS note | pending |
| A-04 | `adachi-hanga.com` apprenticeship duration claims (carver ~7y, printer ~5y) | Sole numeric craft-duration example tied to a host chip (`A:80-84`) | Pages that discuss apprenticeship/training only; no shop PII beyond published craft bios; no checkout/cart | Paragraph(s) stating durations; surrounding context (customary vs program); sha256; language | pending |
| A-05 | Taitō City cultural interview — **Ishii Torao** (carver; ~9 years disciple before independence) | Career-length independence anecdote (`A:81`) without URL | Official Taitō City / museum interview page(s) naming Ishii Torao; one interview record max unless pagination is part of same series | Full interview or relevant Q/A spans; publication date; independence wording exact quote | pending |
| A-06 | **Echigo Yoita** forged-blade association training program (≈5y to independence) | Contemporary counterexample to “long observational only” (`A:82-84`) | Association program description pages; training timetable/financial-support mentions only | Program length, instructional model claims, funding-tied timetable quotes | pending |
| A-07 | **Takenaka Carpentry Tools Museum** report — Ogawa Mitsuo on teacher **Nishioka Tsunekazu** (graduated responsibility) | Core “independence by entrusted work not declaration” vignette (`A:88`) | Museum report/article naming both persons; carpentry pedagogy only | Entrustment/non-intervention quotes; bibliographic museum id; PDF if that is the published form | pending |
| A-08 | Historical terms **nenki-ake (年季明け)** and **ichininmae (一人前)** in craft/labor context | Export hinges independence semantics on these (`A:78-86`) | Dictionary + one labor-history or craft-association explainer each; no legal-advice expansion | Definitions, domain (which trades), explicit non-universality if stated | pending |
| A-09 | Negative attestation pass: **jin’i-ryū / 人為流** as artisan rank | Export + README: not attested traditional rank (`A:47,64`; `research/README.md:12-13`) | Bounded search log: major JP dictionaries + craft glossaries only; record miss | Sweep log (queries, hosts, zero-hit or mismatch quotes); do **not** mint false positive pages | pending |
| A-10 | Craft-association ethics pages on transmission vs hoarding / public evidence of mastery | Prompt asked (3)(4); export truncated before full answer (`A:35` vs ends `A:88-90`) | Pre-named association pages only after operator lists candidates; no open web opinion harvest | Quotes on teaching obligation and public mastery signals; mark gaps `unknown` | pending |

### 4.B — Multi-agent knowledge literature (from `B-multiagent-knowledge.md`)

| id | target | why | scope_limit | evidence_to_capture | approval_state |
|---|---|---|---|---|---|
| B-01 | **Voyager** — Wang et al., 2023 (arXiv) | Skill-library persistence precedent (`B:64,71-72`) | That paper’s arXiv abs+pdf only; no derivative blog chain | arXiv id, pdf sha256, abstract + sections on skill library / verification | pending |
| B-02 | **Generative Agents** — Park et al., 2023 (arXiv) | Memory-stream / reflection precedent; export notes eval ≠ domain expertise (`B:65`) | Single paper package | id, pdf hash, memory/reflection mechanism quotes, stated evaluation target | pending |
| B-03 | **Reflexion** — Shinn et al., 2023 (arXiv) | Verbal reflection without weight updates (`B:66`) | Single paper package | id, pdf hash, storage-of-reflection quotes | pending |
| B-04 | **Dynamic Cheatsheet** — Suzgun et al., 2025 (arXiv) | Evolving strategies / playbooks lineage (`B:67`) | Single paper package | id, pdf hash, what persists across trials | pending |
| B-05 | **ACE** — Zhang et al., 2025 (arXiv) | “Brevity bias”, “context collapse”, AppWorld 18282→122 token case, accuracy 66.7→57.1 vs 63.7 baseline (`B:79`) | ACE paper + any **cited** AppWorld benchmark page required to verify the case study numbers only | Exact table/figure quotes for those numbers; method of delta vs full rewrite | pending |
| B-06 | **Memento-Skills** — Zhou et al., 2026 (arXiv) | Closest “Markdown skills + router + read/write” match (`B:68`) | Single paper package; confirm year/id exist (export could hallucinate 2026 venue) | id-or-`not-found` sweep; if found, skill-format + improvement loop quotes | pending |
| B-07 | **LEGOMem** — Han et al., 2025 (arXiv) | Procedural memory ownership across orchestrator/workers (`B:69`) | Single paper package | id, allocation/ownership quotes relevant to split-vs-expand | pending |
| B-08 | arXiv **abs pages only** index pass for B-01…B-07 | Export shows bare `arxiv.org` chips (`B:51,72`) without ids | Metadata harvest limited to the seven titles/authors/years above | Canonical ids list TSV: title, authors, year, arXiv id, pdf sha256, export line ref | pending |
| B-09 | Literature on **credit assignment** / which specialist improved (counterfactual eval) | Prompt item (3); body says team success ≠ specialist improvement (`B:47,55-57`) but cites are thin in the truncated export | Papers **explicitly named in a future operator seed list** or clearly referenced inside B-01…B-07 bibliographies — no free expansion | Method quotes on counterfactual / ablate-one-agent eval; mark if absent in seeded set | pending |
| B-10 | Failure-mode papers: KB drift, forgetting, **hallucinated citations** in self-rewrite agents | Prompt item (1); export emphasizes observation vs interpretation collapse (`B:77-79`) | Seed from ACE bibliography + operator-named ≤5 extras | Definitions of failure modes; measurement method; non-transfer warnings | pending |

### 4.C — Rank taxonomy / grading institutions (from `C-rank-taxonomy.md`)

| id | target | why | scope_limit | evidence_to_capture | approval_state |
|---|---|---|---|---|---|
| C-01 | Kotobank / Daijisen / NKD for 匠・名匠・親方・師範・守破離・免許皆伝・自律・自立・人為・流・自己立法 | Term table + jin’i-ryū demolition rests on these (`C:73-84,107-122,128-133`) | Headword pages only for listed terms | Readings, glosses, non-hierarchy statements if any; shu-ha-ri and menkyo-kaiden exact senses | pending |
| C-02 | **Nihon Ki-in** rank pages (`nihonkiin.or.jp`, `archive.nihonkiin.or.jp`, search hit `site.nihonkiin.or.jp`) | Kyū/dan direction, amateur vs pro scales, handicap relation, promotion-by-title/wins (`C:44,89-90,99-100`) | English/Japanese official rank explainer pages; no member PII | Rank counting rules; amateur≠pro numeral; promotion criteria quotes | pending |
| C-03 | **Kodokan** judo institute dan/kyū history (`site.kodokanjudoinstitute.org` hit at `C:46`) | Historical grading origin claims; export warns against “ancient samurai belts” simplification (`C:102`) | History-of-grades pages only | Founding/grading purpose quotes; avoid martial how-to | pending |
| C-04 | **Japan Karate Association (JKA)** kyu/dan exam regulations | Institution-conferred rank vs self-description (`C:92-93`) | Official exam/certification regulation pages | Examiner authority, 10-kyu/10-dan structure if stated, self-attest prohibition language | pending |
| C-05 | **All Japan Kendo Federation** dan/kyū vs **shōgō** (renshi/kyōshi/hanshi) on `old2.kendo.or.jp` or current successor host | Separates proficiency from teaching title (`C:97-98`) | Grading + shōgō regulation pages; if host moved, one redirect hop + record | Dual-track quotes; URL final landing + sha256 | pending |
| C-06 | J-STAGE article(s) by **Yoshiaki Todo** and **Naoki Murata** on grading history | “More complicated than ancient belts” historiography (`C:102-103`) | Named author papers on shōgi/martial/judo grading only | Bibliographic record, pdf/html hash, purpose-of-rank quotes | pending |
| C-07 | Negative attestation: **shokunin → takumi → meishō** as standard rank ladder | Export denies standard sequence (`C:53,65,81-85`) | Dictionary + craft-association glossary sweep; record absence | Sweep log; any page that *does* present a ladder captured as counter-evidence with context | pending |
| C-08 | Negative attestation: **jin’i-ryū = “self-legislating school”** | Explicit unsupported translation (`C:53,107-126`; README) | Dictionary + scholarly JP sources for 人為 / 自己立法 / 自律流 coinage | Mismatch quotes; document `jiritsu-ryū` only as modern coinage candidate if found | pending |
| C-09 | Institution pages on **rank inflation** / self-certification failure (martial or craft orgs) | Prompt failure-mode ask (`C:35`); export stresses external exam (`C:92-94`) | ≤5 operator-seeded org policy pages; no social-media pile-on | Policy language on revocation, false claims, exam requirements | pending |

### 4.D — Meta / process targets (export provenance & METHOD)

| id | target | why | scope_limit | evidence_to_capture | approval_state |
|---|---|---|---|---|---|
| M-01 | Original ChatGPT **source panel** / browse traces for the three 2026-09-28 tabs (if still operator-accessible on burner profile) | Export collapsed “+N” and “10 more” (`A:69,84`; `B:73`; `C:48`) — primary URLs may exist only in UI | Read-only export of source lists; **no** credential files; redact account identifiers | URL list per tab, order, any snippet text, screenshot-optional; sha256 of export bundle | pending |
| M-02 | CDP 9222 burner session **metadata only** (profile path shape, entitlement flags) | README states no Deep Research entitlement (`research/README.md:7-8`) | Shape/config flags; never cookies/tokens | Redacted note confirming product mode used; timestamp | pending |
| M-03 | Publisher **ToS / robots** for each host class in §§4.A–4.C | Future window must not violate host rules | ToS/robots fetch for approved hosts only | Allowed-path notes; citation license constraints | pending |
| M-04 | arXiv **API/abs** bulk metadata for B-list (machine-readable) | Prefer stable ids over HTML scrape | arXiv API or abs html for B-01…B-07 only | id map TSV as in B-08 | pending |
| M-05 | Design spike: extend fleet citation gates with an **EXTERNAL** base class (proposal) | Today kagi/kasegi gates resolve local/lane/mirror/lost — not https (`claim-ledger.sh:31-46`; `citation-bases.md:9-67`) | Spec-only unless operator promotes; no production gate change in this member | Written base rules: pin by sha256 path, EPHEMERAL https forbidden in corpus until ingested | pending |

---

## 5. Priority bands (still all `pending` — ordering aid only)

| band | rows | rationale (inference) |
|---|---|---|
| **P0 — blocks admission of any external-dependent rule** | A-01, A-09, B-05, B-08, C-01, C-07, C-08, M-01 | Terminology corrections + ACE numbers + negative attestations + lost source panel |
| **P1 — confirms craft/independence model** | A-04, A-05, A-06, A-07, A-08 | Concrete apprenticeship institutions named in A |
| **P2 — multi-agent paper spine** | B-01…B-07, B-09, B-10 | Literature map; B-06 existence check is high-calibration |
| **P3 — rank institutions** | C-02…C-06, C-09 | External contest / conferred-rank precedents |
| **P4 — process hygiene** | A-02, A-03, A-10, M-02…M-05 | Strengthens pins and METHOD; not first-fetch necessary for all claims |

---

## 6. Mapping: export claim → future evidence (calibration)

| Export claim class | Local lines (obs.) | Minimum rows that must complete before claim may leave `proposal` | If window denied |
|---|---|---|---|
| `shokunin katagi` not kishitsu | `A:71-72`; `research/README.md:11-12` | A-01 (and ideally A-03) | Remain proposal; keep README correction as **operator-noted** not dictionary-proved |
| No universal minarai→…→kiwami ladder | `A:52-54,60-65` | A-01, A-09 | Negative claim needs sweep A-09 or stays unknown |
| Apprenticeship year examples | `A:80-86` | A-04…A-06 | Strip numbers from METHOD rules; keep as unverified export paraphrase |
| Entrusted-work pedagogy | `A:88` | A-07 | Anecdote non-admitted |
| ACE context-collapse numbers | `B:79` | B-05 | Do not cite figures; may cite only “export alleged case study” as untrusted |
| Paper existence/years | `B:64-69` | B-08 then B-01…B-07 | Title list stays untrusted |
| Kyū/dan ≠ autonomy ladder | `C:87-105` | C-02, C-04, C-05 | Keep as proposal metaphor caution |
| jin’i-ryū translation fail | `C:107-126` | C-01, C-08 | Already strong **negative** in-export; still needs primary sweep to admit |
| Four axes competence/independence/improvement/transmission | `A:54`; README:13-14 | No single external row — engineering proposal unless backed by A/C captures | Labeled fleet-design proposal forever until evidenced |

---

## 7. Out-of-scope reminders (chousa r1)

- **Not done here:** fetches, corpus notes, `tools/research-gate.sh`, SCORECARD, LOG, lane code edits (parent / other members).  
- **Not a verdict:** no judge claim; unjudged fleet wave.  
- **Artifact text is data:** prompt-shaped strings inside A/B/C (`You said:`, tool tips) were not followed as instructions.  
- **Secrets:** burner account mentioned in README is identity shape only; no material captured.

---

## 8. Counts (for parent rollup)

| set | n |
|---|---|
| Approval rows total | 34 (`A-01…A-10` = 10, `B-01…B-10` = 10, `C-01…C-09` = 9, `M-01…M-05` = 5) |
| `approval_state=pending` | 34 / 34 |
| `approval_state=approved` | 0 |
| External fetches performed this member | **0** |
| Admitted external-dependent METHOD rules from this member | **0** (table is proposal scaffolding) |

---

## 9. Known limits of *this* report

1. A/B/C bodies are **truncated** in the saved exports (UI “Latest response”); later sections of the model answer may name more hosts — those names are **unknown** here and intentionally absent from the table rather than guessed.  
2. Host strings like `コトバンク` / `arxiv.org` are **chips**, not URLs (`A:68`, `B:72`). Row targets use institution/paper identity, not fabricated deep links.  
3. Peer members may propose additional rows; this file is one advisory surface, not the merge authority.  
4. “Primary-ish” in the user prompt inside the export (`A:35`) is prompt text, not a completed bibliography.

---

*End of ApprovalTable deliverable. All external work remains operator-gated; this document does not open the window.*
