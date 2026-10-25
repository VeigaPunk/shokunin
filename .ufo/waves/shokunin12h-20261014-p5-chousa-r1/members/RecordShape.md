# RecordShape — research-record schema the gate validates

**Member:** RecordShape (scribe)  
**Wave:** shokunin12h-20261014-p5-chousa-r1  
**Lane:** chousa-shokunin  
**Axes scored on:** coverage · depth · calibration  
**Role of this file:** advisory data for the parent / ResearchGateDesign / GateFixtureDesign. Not a judge verdict.

**Central finding (stated, not papered over):** the three survey artifacts under `research/deep-research-2026-09-28/` are ChatGPT UI chat-export transcripts. Their own outbound citations (hostnames, bare titles, `+N` counters) are **unverifiable from local material**. Any claim that rests only on those outbound hops is `unverified-locally`. The record shape below exists so a gate can force that honesty into structure.

---

## 0. Why a fixed shape

Fleet precedents already enforce claim/citation discipline elsewhere:

| Precedent | What it forces | Local anchor |
|---|---|---|
| kagi claim-ledger | every claim is a **command** with expect+exit; citations must resolve or be labelled dead; knowledge entries declare `Reverify:` | `kagi-shokunin/corpus/claim-ledger.sh` docs header (revision/claim/citation/idref/entry/cell classes); `kagi-shokunin/corpus/knowledge/claim-ledger.md:1-33` |
| kasegi anchorcheck | every `` `path:line` `` is range-checked against a declared base; LOST-RECORDED stays separate from "passed" | `kasegi-shokunin/corpus/instruments/anchorcheck.py:1-63` |
| kasegi citation-bases | one vocabulary for LANE / MIRROR / ORIGIN-WORK / LOST-TREE / LOST-BASE / BLOB-PIN | `kasegi-shokunin/corpus/knowledge/citation-bases.md:1-80` |
| chousa SKILL decision table | question → hierarchy → chain → claim check; rejected sources kept | `chousa-shokunin/SKILL.md:13-46` |
| chousa QUALITY | claim falsifiable or opinion; source pointer; obs/inf/unk separate; rejections kept | `chousa-shokunin/corpus/QUALITY.md:1-7` |

chousa's `tools/research-gate.sh` (designed by sibling ResearchGateDesign; not landed here) validates a **research record** file against the method contract. This member defines the record's required sections and shows one **filled** example built only from local surfaces.

---

## 1. Schema (normative for the gate)

A research record is a single Markdown file (or fixture directory with a root `RECORD.md`) containing **exactly these top-level sections**, in this order. Missing section ⇒ finding id (stable vocabulary; aligned with sibling FindingIds intent).

| # | Section heading | Required | Gate finding if absent/broken | Purpose |
|---|---|---|---|---|
| 1 | `## Meta` | YES | `NO_META` | identity, window mode, revision pins |
| 2 | `## Question` | YES | `NO_QUESTION` | one declared research question (not a topic blob) |
| 3 | `## Source table` | YES | `NO_SOURCE_TABLE` / `UNRANKED_SOURCE` | every source ranked primary\|secondary\|aggregator\|unsourced\|export |
| 4 | `## Chain` | YES | `NO_CHAIN` / `CHAIN_HOP_UNRESOLVED` | ordered hops; each hop `resolved` \| `unresolved` \| `blocked-no-fetch` |
| 5 | `## Claims` | YES | `NO_CLAIMS` / `CLAIM_UNPOINTED` | each claim pointed, typed, statused |
| 6 | `## Rejections` | YES (may be empty table with header) | `REJECTION_DROPPED` if prose discards a source with no row | kept refusals with reason |
| 7 | `## Unknowns` | YES (may be empty table with header) | `UNKNOWN_COLLAPSED` if unknown is stated as fact elsewhere | residual unknowns, not smuggled into claims |
| 8 | `## Sweeps` | YES when any negative claim exists | `NEGATIVE_WITHOUT_SWEEP` | commands/path globs that support absence claims |
| 9 | `## Stop` | RECOMMENDED | (informational; proposal if enforced) | why the window closed |

### 1.1 Meta fields

```
record_id:     <stable id, e.g. RR-chousa-r1-export-trust>
lane:          chousa-shokunin
window_mode:   loopback | external-approved
approval_ref:  none | path-to-approval-table-row
as_of:         ISO-8601 date or commit
operator:      <who opened the window>
```

`window_mode=external-approved` without `approval_ref` ⇒ `APPROVAL_MISSING` (hard boundary: `chousa-shokunin/SKILL.md:34-36`, `chousa-shokunin/PROVINCE.md:10-12`).

### 1.2 Question fields

- Exactly one primary question string under `## Question`.
- Optional sub-questions as a numbered list; each must be answerable or explicitly deferred to `## Unknowns`.
- A topic title with no interrogative ⇒ `NO_QUESTION` (the three exports declare long prompt blobs, not clean question records — see filled example contrast).

### 1.3 Source table columns

| column | values | notes |
|---|---|---|
| `src_id` | S1, S2, … | stable within the record |
| `path_or_token` | repo-relative path, or labelled external token | external tokens need `label` |
| `tier` | `primary` \| `secondary` \| `aggregator` \| `unsourced` \| `export` \| `fleet-gate` | `export` = chat/UI dump treated as carrier, not as authority for its outbound cites |
| `revision` | sha256 prefix and/or `wc -l`/`bytes`, or stamp row | from local measure; never invented |
| `role` | what it is used for | one line |
| `local_openable` | yes \| no | if no, must say why (no-fetch / lost-base / ephemeral) |
| `label` | optional: `historical` \| `ephemeral` \| `proposal-target` \| `unverified-outbound` | kagi marker class adapted |

Unranked row (missing `tier`) ⇒ `UNRANKED_SOURCE`.  
Citing an external URL as if primary while `window_mode=loopback` ⇒ `TIER_OVERCLAIM` (proposal enforcement until external window exists).

### 1.4 Chain hop columns

| column | values |
|---|---|
| `hop` | 1..N order |
| `from` | src_id or claim_id |
| `to_token` | the cited string as it appears |
| `status` | `resolved` \| `unresolved` \| `blocked-no-fetch` \| `labelled-dead` |
| `local_evidence` | path:line that proves the hop, or `none` |
| `note` | one line |

A hop that stops at a bare hostname (`arxiv.org`, `コトバンク`) with no local artifact ⇒ `blocked-no-fetch` in loopback, never silently `resolved`.  
Broken hop kept in the table (not deleted) — chaining discipline requires the failure to remain visible (`chousa-shokunin/SKILL.md:28-29`).

### 1.5 Claim columns

| column | values |
|---|---|
| `claim_id` | C1, C2, … |
| `text` | single falsifiable sentence (or marked `opinion:`) |
| `kind` | `observation` \| `inference` \| `negative` \| `opinion` \| `proposal` |
| `points_to` | `path:line` and/or `src_id` + span | required unless `opinion`/`proposal` |
| `status` | `verified-local` \| `unverified-locally` \| `contradicted-local` \| `open` |
| `depends_on` | hop ids or empty |
| `sweep_ref` | required when `kind=negative` | points at `## Sweeps` row |

`CLAIM_UNPOINTED` when `kind` ∈ {observation, inference, negative} and `points_to` empty.  
Mixing observation text into an inference without relabeling ⇒ calibration defect (QUALITY item 3: `chousa-shokunin/corpus/QUALITY.md:5`).

### 1.6 Rejection columns

| column | values |
|---|---|
| `rej_id` | R1, R2, … |
| `candidate` | what was considered |
| `reason` | why refused |
| `anchor` | path:line or `operator-boundary` |
| `kept` | always `yes` if row exists — presence is the keep |

Silently omitting a source the narrative discarded ⇒ `REJECTION_DROPPED`.

### 1.7 Unknown columns

| column | values |
|---|---|
| `unk_id` | U1, U2, … |
| `text` | what is not known from local material |
| `blocker` | `no-fetch` \| `missing-artifact` \| `export-truncated` \| `needs-approval` \| other |
| `would_need` | concrete next surface (still local or approval-table row) — never a live URL fetch instruction in loopback |

### 1.8 Sweep columns (negative claims)

| column | values |
|---|---|
| `sweep_id` | W1, W2, … |
| `claim_id` | the negative claim |
| `command_or_method` | exact local command, or prose method if command impossible |
| `runnable_locally` | yes \| no |
| `result_summary` | what the sweep showed |
| `as_of` | when run |

### 1.9 Machine-checkable invariants (gate contract sketch)

Aligned with `chousa-shokunin/SKILL.md:48-53`:

1. `## Question` non-empty after strip → else `NO_QUESTION`.
2. Every `src_id` referenced by claims/chains exists in source table → else `SOURCE_ID_DANGLING`.
3. Every source row has `tier` ∈ allowed set → else `UNRANKED_SOURCE`.
4. Every chain hop has `status` ∈ allowed set; if `status=resolved` then `local_evidence` matches `path:line` that opens → else `CHAIN_HOP_UNRESOLVED`.
5. Every claim with `kind` ∈ observation|inference|negative has non-empty `points_to` → else `CLAIM_UNPOINTED`.
6. Every `kind=negative` has `sweep_ref` resolving to `## Sweeps` → else `NEGATIVE_WITHOUT_SWEEP`.
7. `## Rejections` and `## Unknowns` section headers exist (tables may have only header row) → else `REJECTION_DROPPED` / `UNKNOWN_COLLAPSED`.
8. No claim `status=verified-local` may `depends_on` a hop with `status≠resolved` → else `VERIFY_OVERREACH`.
9. Secrets shape-only: no values matching session/credential patterns in any cell → `SECRECY_SHAPE` (boundary: `chousa-shokunin/SKILL.md:39`).
10. Outbound URL/hostname used as `points_to` under `window_mode=loopback` → `EXTERNAL_POINTER_IN_LOOPBACK`.

Exit map (for ResearchGateDesign): `RESEARCH_GATE: CLEAN` exit 0 · `RESEARCH_GATE: DRIFT` exit 1 · usage/setup exit 2.

---

## 2. Filled example (local material only)

The example answers a **method** question about the survey corpus itself — not a content question about Japanese craft ranks (content routes elsewhere; craft stays here).

### RECORD (example body a gate would accept as CLEAN shape; several claims correctly statused `unverified-locally`)

```markdown
# RR-chousa-r1-export-as-record

## Meta
- record_id: RR-chousa-r1-export-as-record
- lane: chousa-shokunin
- window_mode: loopback
- approval_ref: none
- as_of: 2026-10-14 (wave shokunin12h-20261014-p5-chousa-r1)
- operator: chousa probation r1 / RecordShape member
- scope_note: method audit of local research/ exports; refuses kasegi bounty scope and kengaku model-quality claims

## Question
What kind of research *records* are the three files under
`research/deep-research-2026-09-28/`, and which of their load-bearing
statements can be verified from local material alone?

Sub-questions:
1. What does each file declare as its originating prompt/question?
2. What citation *forms* appear, and which hops resolve locally?
3. What corrections does the fleet's own README already assert about terminology?
4. What does the fleet already enforce for citations that these exports lack?

## Source table

| src_id | path_or_token | tier | revision | role | local_openable | label |
|---|---|---|---|---|---|---|
| S1 | research/README.md | secondary | sha256 5199b23b4be6… ; 17 lines ; 937 bytes | operator index of the three tabs; states corrections | yes | |
| S2 | research/deep-research-2026-09-28/A-shokunin-tradition.md | export | sha256 9033857d4625… ; 109 lines ; 6474 bytes | chat-export carrier for tradition prompt/response | yes | unverified-outbound |
| S3 | research/deep-research-2026-09-28/B-multiagent-knowledge.md | export | sha256 6d8dbddd3e2d… ; 100 lines ; 5364 bytes | chat-export carrier for multi-agent KB prompt/response | yes | unverified-outbound |
| S4 | research/deep-research-2026-09-28/C-rank-taxonomy.md | export | sha256 e48fe70ff920… ; 154 lines ; 8922 bytes | chat-export carrier for rank-taxonomy prompt/response | yes | unverified-outbound |
| S5 | chousa-shokunin/SKILL.md | fleet-gate | sha256 063110dab11f… ; 53 lines ; 2886 bytes | method contract this record implements | yes | |
| S6 | chousa-shokunin/corpus/QUALITY.md | fleet-gate | 7 lines ; 300 bytes | admission bar | yes | |
| S7 | kagi-shokunin/corpus/claim-ledger.sh | fleet-gate | 1319 lines ; 79301 bytes | claim+citation durability gate (docs mode) | yes | |
| S8 | kagi-shokunin/corpus/knowledge/claim-ledger.md | secondary | (lane knowledge) | explains why claims need commands | yes | |
| S9 | kasegi-shokunin/corpus/instruments/anchorcheck.py | fleet-gate | 283 lines ; 14390 bytes | path:line anchor gate | yes | |
| S10 | kasegi-shokunin/corpus/knowledge/citation-bases.md | secondary | 120 lines ; 7773 bytes | citation base vocabulary | yes | |
| S11 | コトバンク | aggregator | n/a | outbound hostname inside exports | no | unverified-outbound ; blocked-no-fetch |
| S12 | arxiv.org | aggregator | n/a | outbound hostname inside B | no | unverified-outbound ; blocked-no-fetch |
| S13 | adachi-hanga.com | unsourced | n/a | outbound hostname inside A | no | unverified-outbound ; blocked-no-fetch |
| S14 | archive.nihonkiin.or.jp / nihonkiin.or.jp | unsourced | n/a | outbound hostnames inside C | no | unverified-outbound ; blocked-no-fetch |

Tier notes:
- `export` is below `secondary` for authority over *external* facts, but is
  `primary` for facts *about the export text itself* (what string appears on
  which line). Claims about export text point at S2–S4 with status
  verified-local. Claims about the world those exports describe that need
  S11–S14 stay unverified-locally.
- Hierarchy rule source: chousa-shokunin/SKILL.md:18
  (`primary > secondary > aggregator > unsourced claim`).

## Chain

| hop | from | to_token | status | local_evidence | note |
|---|---|---|---|---|---|
| H1 | question | S1 research/README.md | resolved | research/README.md:5-16 | index describes the three tabs and pipeline caveat |
| H2 | S1 | S2 A-shokunin-tradition.md | resolved | research/README.md:10-14 → file openable | README lists A; bytes match measured revision |
| H3 | S1 | S3 B-multiagent-knowledge.md | resolved | research/README.md:15 | same |
| H4 | S1 | S4 C-rank-taxonomy.md | resolved | research/README.md:16 | same |
| H5 | S2:67-72 | コトバンク | blocked-no-fetch | none | export cites Kotobank; no local snapshot |
| H6 | S2:83 | adachi-hanga.com | blocked-no-fetch | none | apprenticeship-years claim rests here |
| H7 | S3:71-73 | arxiv.org (+6) | blocked-no-fetch | none | paper list has no local PDF/arXiv ids as files |
| H8 | S4:82 | コトバンク | blocked-no-fetch | none | dictionary authority not local |
| H9 | S4:90 | archive.nihonkiin.or.jp | blocked-no-fetch | none | Go rank claim outbound |
| H10 | S4:109 | (negative: no attestation of jin'i-ryū) | unresolved | S4:109 text only | absence claim inside export; export's own sweep not recorded as commands |
| H11 | method | S5–S10 fleet gates | resolved | paths open; see source table | precedents for what a disciplined record contains |

Broken-hop example retained: **H5–H9** are the class of failure ChainingDiscipline targets — narrative authority stops at a hostname with no local artifact.

## Claims

| claim_id | text | kind | points_to | status | depends_on | sweep_ref |
|---|---|---|---|---|---|---|
| C1 | research/README.md states the three files are browse-enabled GPT-6-Astra responses (not Deep Research pipeline), harvested 2026-09-28. | observation | research/README.md:6-8 | verified-local | H1 | |
| C2 | Each of A/B/C is a ChatGPT UI export: chrome lines include "Skip to content", "ChatGPT said:", "Sources", "Web search". | observation | A:1-8,38-45 ; B:1-8,38-45 ; C:1-8,38-50 | verified-local | H2,H3,H4 | |
| C3 | A's user prompt asks about minarai/deshi/shokunin/jin'i-ryu/kiwami and four prescription questions. | observation | research/deep-research-2026-09-28/A-shokunin-tradition.md:34-35 | verified-local | H2 | |
| C4 | A asserts there is no universal ladder minarai→deshi→shokunin→jin'i-ryū→kiwami. | observation | A:52 | verified-local (as export text) | H2 | |
| C5 | A asserts 職人気質 is read shokunin katagi (not kishitsu). | observation | A:47,71 ; research/README.md:11-12 | verified-local (export+README agree on the string) | H1,H2 | |
| C6 | The world-fact "katagi is the dictionary reading" is true in Japanese lexicography. | inference | would need S11 or local dictionary dump | unverified-locally | H5 | |
| C7 | A cites Adachi apprenticeship durations (~7y carvers / ~5y printers). | observation | A:80-83 | verified-local (as export text) | H2 | |
| C8 | Those durations match Adachi's site. | inference | adachi-hanga.com | unverified-locally | H6 | |
| C9 | B lists Voyager, Generative Agents, Reflexion, Dynamic Cheatsheet, ACE, Memento-Skills, LEGOMem as related work. | observation | B:63-71 | verified-local (as export text) | H3 | |
| C10 | Those papers exist on arXiv with the attributed findings (e.g. ACE brevity bias numbers). | inference | arxiv.org | unverified-locally | H7 | |
| C11 | C asserts no authoritative attestation that jin'i-ryū means "self-legislating school". | observation | C:53,107-109 | verified-local (as export text) | H4 | |
| C12 | No local fleet file outside these exports defines jin'i-ryū as an attested historical rank. | negative | see W1 | verified-local | H1–H4,H11 | W1 |
| C13 | README already labels jin'i-ryu as a coined term for the scheme, not attested artisan rank. | observation | research/README.md:12-13 | verified-local | H1 | |
| C14 | The exports do not carry resolvable path:line citations of the form kasegi anchorcheck checks. | negative | see W2 | verified-local | H11 | W2 |
| C15 | The exports do not carry claim rows with re-runnable commands of the form kagi claim-ledger requires. | negative | see W3 | verified-local | H11 | W3 |
| C16 | A research record that stopped at these exports and marked C6/C8/C10 verified would over-claim. | inference | S5:19-20,43-46 ; this record's status column | verified-local | H11 | |
| C17 | opinion: four axes (competence/independence/improvement/transmission) are a useful roster design split. | opinion | A:54 ; README:13-14 | open (design preference, not fact) | | |

Epistemic split enforced: C4/C5/C7/C9/C11 = what the **export says**; C6/C8/C10 = what the **world is**; only the first class is verified-local without fetch.

## Rejections

| rej_id | candidate | reason | anchor | kept |
|---|---|---|---|---|
| R1 | Treat コトバンク / arxiv.org hostnames as resolved primaries | window_mode=loopback; no local snapshot; NO EXTERNAL FETCHES | wave contract; chousa-shokunin/SKILL.md:34-36 | yes |
| R2 | Accept export "Sources: … arxiv.org +6" as a citation chain end | chain must reach an artifact or mark unresolved | chousa-shokunin/SKILL.md:19,28-29 | yes |
| R3 | Fold kasegi bounty-program research into this record | province refuse → kasegi | chousa-shokunin/PROVINCE.md:10-12 | yes |
| R4 | Fold model-quality evaluation of GPT-6-Astra into this record | province refuse → kengaku | chousa-shokunin/PROVINCE.md:10-11 ; README:6-8 names model only as provenance | yes |
| R5 | Live-fetch Kotobank/Adachi/Nihon Ki-in to upgrade C6/C8 | needs operator approval table row; not granted this window | chousa-shokunin/SKILL.md:34-36 | yes |
| R6 | Delete H5–H9 because they failed | rejections/broken hops are kept | chousa-shokunin/corpus/QUALITY.md:7 | yes |
| R7 | Use session URIs (local://, agent://) as durable claim pointers | kagi citation class EPHEMERAL | kagi-shokunin/corpus/knowledge/claim-ledger.md:22-27,122-133 | yes |

## Unknowns

| unk_id | text | blocker | would_need |
|---|---|---|---|
| U1 | Whether Kotobank/Daijisen entries at export-time actually support the katagi gloss | no-fetch | approval-table row + captured dictionary snapshot filed under research/ |
| U2 | Whether ACE AppWorld 18282→122 token case numbers are accurate | no-fetch | local PDF or pinned arXiv source under research/ |
| U3 | Full untruncated model response beyond the export's "Latest response" UI clip | export-truncated | original session archive if operator retains one (shape-only; no secrets) |
| U4 | Exact CDP/burner account session identifiers for the 2026-09-28 harvest | needs-approval / secrecy | not required for method audit; provenance beyond README:6-8 is unknown |
| U5 | Whether a future external window should prefer primary craft associations over dictionary aggregators for independence-duration claims | needs-approval | ApprovalTable deliverable (sibling); decision not made here |

## Sweeps

| sweep_id | claim_id | command_or_method | runnable_locally | result_summary | as_of |
|---|---|---|---|---|---|
| W1 | C12 | `rg -n "jin'i-ry[uū]|jin’i-ry|自立法|jiri-tsu-ry" research/ chousa-shokunin/ kagi-shokunin/corpus/knowledge/ kasegi-shokunin/corpus/knowledge/ 2>/dev/null` plus README read | yes | hits concentrate in research/README.md and the three exports; no outside attestation of historical rank | 2026-10-14 |
| W2 | C14 | `rg -n '\`[a-zA-Z0-9_./-]+\.(md|py|sh|tsv):[0-9]+' research/deep-research-2026-09-28/` | yes | no path:line backtick cites in the three exports; cites are hostnames/titles | 2026-10-14 |
| W3 | C15 | compare export structure to claim-ledger row shape (`id TAB command TAB expect…`) documented in kagi-shokunin/corpus/knowledge/claim-ledger.md:64-68; `rg -n 'R[0-9]+-[0-9]+' research/deep-research-2026-09-28/` | yes | no claim-id rows; no command column; narrative only | 2026-10-14 |

## Stop
Stop conditions met for this loopback window:
- Question answered at the method layer (exports are carriers; outbound hops blocked).
- Every load-bearing local claim pointed at path:line.
- Residual world-facts parked in Unknowns with blockers, not promoted to verified-local.
- Further progress on C6/C8/C10 requires ApprovalTable + captured sources (out of this record's window).
Premature if: we had claimed C6/C8/C10 verified, or dropped R1–R6.
```

---

## 3. Mapping: schema field → gate finding → local warrant

| Schema must-hold | Finding id | Warrant in fleet/local material |
|---|---|---|
| Question declared | `NO_QUESTION` | `chousa-shokunin/SKILL.md:17` expected output "research record with a declared question" |
| Sources ranked | `UNRANKED_SOURCE` | `chousa-shokunin/SKILL.md:18` |
| Chain hop resolved or marked | `CHAIN_HOP_UNRESOLVED` | `chousa-shokunin/SKILL.md:19,28-29` |
| Claim pointed | `CLAIM_UNPOINTED` | `chousa-shokunin/SKILL.md:43` ; QUALITY.md:4 ; kagi claim-without-command failure class `claim-ledger.md:19-22` |
| Rejection kept | `REJECTION_DROPPED` | `chousa-shokunin/SKILL.md:46` ; QUALITY.md:7 |
| Unknown not smuggled | `UNKNOWN_COLLAPSED` | QUALITY.md:5 ; SKILL.md:45 |
| Negative has sweep | `NEGATIVE_WITHOUT_SWEEP` | SKILL.md:44 |
| verified-local ≰ blocked hop | `VERIFY_OVERREACH` | SKILL.md:20 ; calibration lesson in claim-ledger.md:16-22 |
| Loopback ≰ live URL pointer | `EXTERNAL_POINTER_IN_LOOPBACK` | wave contract NO EXTERNAL FETCHES ; SKILL.md:34-36 |
| path:line openable when claimed | (anchorcheck class) | `anchorcheck.py:3-20` IN-RANGE vs PAST-EOF/MISSING-FILE |
| Dead cite labelled | (kagi citations class) | claim-ledger.sh docs: labelled stale tokens |

---

## 4. Contrast: raw export vs shaped record

| Dimension | Raw export (A/B/C) | Shaped record (this example) |
|---|---|---|
| Question | Long prompt embedded under "You said:" (A:35, B:35, C:35) | Single interrogative + numbered sub-questions |
| Sources | Hostname footers, `+N` counters, bare titles | Ranked table with revision pins and openable flag |
| Chain | Implicit "Searched the web" UI chrome | Explicit hops; blocked-no-fetch retained |
| Claims | Prose paragraphs mixing fact and design advice | Rows with kind/status/points_to |
| Rejections | Partially present as narrative caveats (A:64 jin'i-ryū unsubstantiated) | Table rows with keep=yes |
| Unknowns | UI disclaimer "ChatGPT can make mistakes" (A:90) | Structured unknowns with blockers |
| Negative evidence | "I haven't found…" without sweep commands (A:47, C:109) | Sweeps W1–W3 with runnable local commands |
| Citation durability | Fails kagi ephemeral/unresolved classes if treated as corpus | Labels outbound as unverified-outbound |
| Anchor form | No `path:line` | All verified-local claims use path:line |

This contrast **is** the round's method finding: the harvest is useful as a **source inventory and prompt archive**, not as an admitted claim ledger.

---

## 5. Minimal skeleton (empty CLEAN template)

For GateFixtureDesign PASS fixture:

```markdown
# RR-<id>
## Meta
- record_id: RR-<id>
- lane: chousa-shokunin
- window_mode: loopback
- approval_ref: none
- as_of: <date>
## Question
<one interrogative sentence>
## Source table
| src_id | path_or_token | tier | revision | role | local_openable | label |
| S1 | <path> | primary | <sha or wc> | <role> | yes | |
## Chain
| hop | from | to_token | status | local_evidence | note |
| H1 | question | S1 | resolved | <path:line> | |
## Claims
| claim_id | text | kind | points_to | status | depends_on | sweep_ref |
| C1 | <sentence> | observation | <path:line> | verified-local | H1 | |
## Rejections
| rej_id | candidate | reason | anchor | kept |
| (header only if none) |
## Unknowns
| unk_id | text | blocker | would_need |
| (header only if none) |
## Sweeps
| sweep_id | claim_id | command_or_method | runnable_locally | result_summary | as_of |
| (header only if no negative claims) |
## Stop
<why closed>
```

Defect fixtures (one per finding id) omit or break exactly one invariant — owned by GateFixtureDesign / ChainHopFixture siblings; not duplicated here.

---

## 6. Out of scope (this member)

- Implementing `tools/research-gate.sh` (ResearchGateDesign).
- Finding-id final enum freeze (FindingIds) — names above are advisory alignments.
- Approval table contents (ApprovalTable) — only referenced as blocker class.
- Judging content truth of shokunin/multi-agent/rank claims beyond export-text observation.
- Network fetch of any outbound hostname.

---

## 7. Calibration notes (how this report should be read)

- **Coverage:** schema sections Meta → Stop; six required gate surfaces (question, sources, chain, claims, rejections, unknowns) plus sweeps/stop; filled example exercises every column; fleet precedents cited with paths.
- **Depth:** epistemic split export-text vs world-fact; hop table with real blocked hosts from A/B/C; negative sweeps given as concrete local commands; rejection table keeps boundary refusals.
- **Calibration:** does not upgrade C6/C8/C10 to verified; states export citations unverified; marks opinion C17; unknowns named rather than filled with inference; no external fetch performed; no judge verdict claimed.

---

## 8. Provenance of measurements used above

```
# local only — recorded 2026-10-14 during this member run
wc -l -c research/README.md research/deep-research-2026-09-28/*.md \
  chousa-shokunin/SKILL.md chousa-shokunin/corpus/QUALITY.md \
  kagi-shokunin/corpus/claim-ledger.sh \
  kasegi-shokunin/corpus/knowledge/citation-bases.md \
  kasegi-shokunin/corpus/instruments/anchorcheck.py
sha256sum research/README.md research/deep-research-2026-09-28/*.md \
  chousa-shokunin/SKILL.md
```

Line anchors quoted in the filled example were read directly from those paths in this session. Outbound hosts listed are strings present in the export files, not fetched targets.
