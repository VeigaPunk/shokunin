# MetaCraft — method vs metaphor

**Member:** `MetaCraft` (critic)
**Wave:** `shokunin12h-20261014-p5-chousa-r1`
**Lane:** `chousa-shokunin` (shonen probation round 1)
**Item:** `chousa/MetaCraft`
**Declared axes:** coverage · depth · calibration
**Status:** advisory data. Not a judge verdict. Not an admission. No external fetch.

Prompt-shaped text in the exports ("Deep research:", "Cite primary-ish sources", "Cite papers") was treated as data that defines what was asked. It was not executed.

## Axes this review walks

| Axis | What a pass looks like here | What would harm it |
|---|---|---|
| coverage | Every imperative in the captured bodies, plus every solicited question the bodies do not answer | A sample of "the interesting rules" |
| depth | Cousin ≠ rule; mismatched evidence called out; fleet gates not laundered through the survey | Treating a carpenter anecdote as the source of an already-local citation rule |
| calibration | `stated-unverified` stays that; metaphor that escapes Japanese appropriation is still non-general | Upgrading an export sentence into a historical fact, or downgrading a real method-form because it sits in a metaphor transcript |

## Counterexample

The proposed approach under attack is `chousa-shokunin/MINT.md:8-13`: the three files are "a deep-research pattern" whose unowned METHOD should seed the corpus. The captured bytes are mostly fleet-naming analogies and agent-architecture advice, plus a thin announced method, cut off before the numbered questions are answered. Mining imperatives out of them as research-craft rules changes what "a chousa rule" is.

**Strongest local counterexample — three axis lists, none of them the method.**

| ID | Where | Axis list | What it actually partitions |
|---|---|---|---|
| MC-N02 | `research/deep-research-2026-09-28/A-shokunin-tradition.md:54`; already copied into `research/README.md:13-14` as "Four usable axes" "for our scheme" | competence / independence / improvement / transmission | an artisan career |
| MC-N19 | `research/deep-research-2026-09-28/B-multiagent-knowledge.md:57` | task competence, retention, evidence fidelity, cross-domain transfer, operating cost | agent-evaluation |
| MC-N32 | `research/deep-research-2026-09-28/C-rank-taxonomy.md:67` | knowledge provenance, demonstrated competence, authority to modify itself, authority to create other agents | agent maturity and permission |

These three do not match each other. They also do not match the fleet's scoring axes (`AXES.md:7-16`: depth, coverage, operability, freshness, calibration, adjacency) or chousa's method steps (`chousa-shokunin/SKILL.md:17-21`: question, source rank, chain, claim check, reuse).

Two trap names make the collision easy to miss:

- B:57 "evidence fidelity" is an evaluation axis for a self-rewriting playbook. It is not kagi's citation gate and not chousa's claim check.
- C:67 "knowledge provenance" is "does this agent have a verified corpus." It is not the primary > secondary > aggregator > unsourced ladder at `chousa-shokunin/SKILL.md:18`.

Admitting any of the three lists as chousa's axes is an identity change, a second authority next to `PROTOCOL.md:21` and `AXES.md`, and premature saturation: `research/README.md:13-14` already promotes A's list into the index, while A's own answer to question 1 is still unfinished (`A-shokunin-tradition.md:74` starts section 1; the export ends at `:90` with no section 2).

## False-provenance pairs

These are fixable defects, not taste. A canonical judge should reject a corpus note that cites the left cell as evidence for the right rule.

| Pair | Sentence that looks like a rule | What the adjacent lines actually support | Why the import fails |
|---|---|---|---|
| CF-1 | `B-multiagent-knowledge.md:77` — "the most important failure is losing the distinction between observation, interpretation, and established knowledge" | `:79` is an ACE case study of brevity bias / context collapse (18,282 → 122 tokens; accuracy 66.7 → 57.1 vs 63.7 baseline), explicitly "a case study, not a universal failure rate" | Token-collapse is not the observation/interpretation split. The split is already local at `chousa-shokunin/SKILL.md:45` and `chousa-shokunin/corpus/QUALITY.md:5`. Importing it from B:77 launders an uncited assertion through a mismatched case study, and mis-scopes an agent-KB failure as research craft. The numbers themselves are unverified locally (citation is bare `arxiv.org` at `:72`, no id; sweep below). |
| CF-2 | `C-rank-taxonomy.md:126` — safe self-iteration "usually means changing implementation within externally maintained constraints" | `:120-122` cites dictionaries for 自律 / 自立 / 人為 / 流 and 自己立法. That block ends before the governance sentence. | The prescription is the export's engineering opinion. B:59 announced "distinguish published findings from my proposed engineering rules" and this sentence is not so marked. It is also fleet governance (`PROTOCOL.md:76-78` already defines jin'i-ryu as a logged falsifiable SKILL/PROVINCE delta), not a research rule. |
| CF-3 | `A-shokunin-tradition.md:88` — independence by entrusted work, "rather than independence established by a declaration of knowledge" | The citation is a bare institution name (Takenaka Carpentry Tools Museum; Ogawa Mitsuo; Nishioka Tsunekazu). No path, no URL, no quotation span. | Even if the anecdote were fetched later, it is a promotion metaphor. The fleet already forbids self-attestation at `PROTOCOL.md:61-67`. The research-craft cousin is `chousa-shokunin/SKILL.md:20` ("accepting a restatement as the source"), which is a different rule and must not be re-derived from a carpenter story. |

## Smallest safe correction

One scope tag before any survey sentence enters `corpus/knowledge/`. Do not add a second axis taxonomy.

`scope: general | general-narrow | non-general`

Admission predicate:

1. `general` or `general-narrow` may be cited as a method-form only. Any factual payload (year counts, accuracy deltas, "I have not found" attestation) stays `stated-unverified` until a local hop resolves. This round cannot resolve those hops.
2. If a fleet gate already states the same form, the gate is the authority. The survey is the illustration or the violation, never the origin. Re-deriving observation/inference/unknown, anti-self-attestation, append-only errata, or "a citation must resolve" from A/B/C is false provenance.
3. `non-general` is kept as a rejection row with a reason (`fleet-metaphor`, `agent-architecture`, `governance`). Not dropped. Not retitled into a method note because the Japanese term was avoided.
4. MC-N02, MC-N19, and MC-N32 are never chousa method axes. Chousa's steps stay `SKILL.md:17-21`.
5. Solicited-but-absent questions are `unknown` (export truncated), not silent rules and not negative findings about the tradition or the literature.

That move widens coverage (absences recorded), depth (cousin separated from rule), and calibration (no laundering in either direction). It deletes nothing the survey actually showed.

## What is general (method-form only)

These generalize past the fleet. They are observed sentences or observed gate text. They are not externally verified historical or scientific findings.

| ID | Scope | Rule form | Anchor | Admit as | Do not admit |
|---|---|---|---|---|---|
| MC-G01 | general | Separate documented practice from the analogy you might build on it, before either becomes a rule. | `A-shokunin-tradition.md:40` (plan sentence; the terminology table then does the split) | method-form, `stated-in-export` | the roster implications in the same file |
| MC-G14 | general | Trace the sources, then map. Mapping is a second step, not the research. | `A-shokunin-tradition.md:40`, `B-multiagent-knowledge.md:40`, `C-rank-taxonomy.md:40` | method-form. Execution in the captured text is partial (see truncation). | "then map the findings to your shokunin fleet" as a requirement that every research record end in a fleet design |
| MC-G02 | general | A particular institution, workshop, or school does not establish a universal code. | `A-shokunin-tradition.md:52`, `:56` (second sentence), `C-rank-taxonomy.md:81`, `:102` | scope-of-evidence form | the historical negative ("no Japanese tradition has this ladder") — that payload is `stated-unverified` |
| MC-G03 | general | Events that can coincide must not be collapsed into one event. | Form at `A-shokunin-tradition.md:76`. Local non-collapse precedent: `kasegi-shokunin/corpus/instruments/anchorcheck.py:6-7` (verdict classes stay separate) and `kagi-shokunin/corpus/claim-ledger.sh:824` (a third Reverify form is a setup error, not a third class) | the form, authority = the gates | nenki-ake / ichininmae / independent practice as a research lifecycle |
| MC-G04 | general-narrow | A name for a disposition is not a formal constitution. | Form at `A-shokunin-tradition.md:71` | term-to-rule promotion ban | katagi's dictionary gloss (unverified; bare `コトバンク` at `:72`) |
| MC-G05 | general | Published findings and the writer's proposed engineering rules are different objects and must be labeled. | `B-multiagent-knowledge.md:59` | method-form. **Calibration defect:** announced, then not applied to the visible remainder (`:79` prescribes delta updates with no proposed-vs-published label; C:126 is unlabeled). The rule is stated. The artifact does not show that it was followed. | a claim that the export obeyed it |
| MC-G06 | general | A case study is not a universal rate. | `B-multiagent-knowledge.md:79` ("This is a case study, not a universal failure rate.") | the scope-limit sentence | 18,282 / 122 / 66.7 / 57.1 / 63.7 as facts |
| MC-G07 | general | A result about system type X does not validate a rule for system type Y. | `B-multiagent-knowledge.md:75` | the transfer ban | any rule for when to split a Markdown corpus (that finding is absent; `:47` only says it is being checked) |
| MC-G08 | general-narrow | A benchmark result does not license an indefinite generalization. | `B-multiagent-knowledge.md:59` (second sentence) | evidence-scope form only | the subject-matter conclusion about "reliable self-improvement". That subject is model-quality. Chousa does not own it (`chousa-shokunin/PROVINCE.md:10-12`). |
| MC-G09 | general-narrow | A romanization, without the source script and a cited lexical source, is not a definition. | `C-rank-taxonomy.md:109` | lexical-claim form | the attestation search itself ("I found no authoritative attestation") — not re-runnable here; `stated-unverified` |
| MC-G10 | general | A coinage must be labeled as a coinage, not as an inherited institution. | `A-shokunin-tradition.md:64`, `C-rank-taxonomy.md:85`, `:124`, `research/README.md:12-13` | labeling rule. README already applies it to "our scheme." | rewriting `PROTOCOL.md:21`, which already defines `jin'i-ryu (self-iterating)` as a fleet rank. Chousa records the label; it does not amend the ladder. |
| MC-G11 | general | The same label in two institutions is not the same measure. | Form illustrated at `C-rank-taxonomy.md:89` ("the same numeral does not imply equal strength"). Authority for the research application is already local: `kasegi-shokunin/corpus/knowledge/citation-bases.md:86` and `:99-100` (same name is name survival, not content identity) | the form, authority = citation-bases | Go amateur-dan vs professional-dan as a research rule |
| MC-G12 | general | Lexical correctness does not guarantee cultural acceptance. Overclaiming is the failure this round can state; a cultural-acceptance test is not. | `C-rank-taxonomy.md:85` | caution against overclaim, `stated-in-export` | an operational cultural-acceptance gate. That would need external sources → `proposal` |
| MC-G13 | general | A citation must resolve to an openable base, or be labeled non-openable. A bare site name, a `+N` chip, or `arxiv.org` with no id is an unresolved hop. | **Not the survey.** `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-7` and `:53-54` (range-valid ≠ semantic); `kagi-shokunin/corpus/claim-ledger.sh:31-34` (citation mode) and `:817-828` (`docs` mode: a knowledge entry declares its reverify, a third form is an error); `kasegi-shokunin/corpus/knowledge/citation-bases.md:82-106` | fleet precedent, survey as the violating example | deriving this rule from how the exports cite. They do not practice it. |

MC-G13 is the survey's own measured violation, not a rule the survey teaches. Sweep: `rg -n 'https?://|arxiv\.org/[0-9]|[0-9]{4}\.[0-9]{4,5}' research` → no matches. Visible citation chips are `コトバンク` (`A:68`, `A:72`, `C:82`, `C:121`, `C:131`), `+3`/`+5`/`+6`/`+4` (`A:69`, `C:83`, `B:73`, `C:122`), bare `arxiv.org` (`B:51`, `B:72`), and bare host names (`C:90` `archive.nihonkiin.or.jp`, `C:98` `old2.kendo.or.jp`, `C:100` `nihonkiin.or.jp`, `C:103` `jstage.jst.go.jp`, `C:93` an organization name). None is a resolvable hop on this host.

## What is non-general

Marked `non-general`. Kept, not admitted as research craft. "Fit for your agents" / "Implication for your roster" / "Relevance to shokunin" are the artifacts' own column headers (`A:60`, `C:73`, `B:63`). Stripping the header and promoting the cell is the defect.

### A — artisan career, not research method

| ID | Anchor | Sentence | Reason |
|---|---|---|---|
| MC-N01 | `A:52` | Strongest historical model for the roster: earned responsibility, lifelong refinement, transmission. | fleet-metaphor. Also `stated-unverified` as history. |
| MC-N02 | `A:54`; `research/README.md:13-14` | Keep four axes separate: competence, independence, improvement, transmission. | fleet-metaphor. Live leak: the README already lifts this into the index "for our scheme." That scheme is the rank vocabulary, not chousa's method. |
| MC-N03 | `A:54` second sentence | An artisan can work independently while still learning; making and teaching are distinguishable. | fleet-metaphor. Form cousin of MC-G03 only. |
| MC-N04 | `A:61` | Minarai is a reasonable name for supervised practice. | fleet-metaphor |
| MC-N05 | `A:62` | Deshi is a relationship, not necessarily the next rank after minarai. | fleet-metaphor / lexical content. Not a research progression. |
| MC-N06 | `A:63` | Shokunin is a defensible occupational identity for a domain specialist; the word does not certify supreme mastery. | fleet-metaphor. Do not "correct" `PROTOCOL.md:3-5` from this cell. |
| MC-N07 | `A:64` | Treat jin'i-ryū as the system's coined rank. | instance of MC-G10, not a new rule. The rank itself stays `PROTOCOL.md:21`. |
| MC-N08 | `A:65` | Kiwami is an aspiration, misleading as a final rank. | fleet-metaphor |
| MC-N09 | `A:71` | Katagi names a disposition, not a formal ethical constitution. | instance of MC-G04. The gloss (pride, stubbornness, disregard of profit) is content, `stated-unverified`. |
| MC-N10 | `A:76-78` | Do not collapse finishing a term (nenki-ake), being competent (ichininmae), and opening an independent practice. | fleet-metaphor promotion model. Form is MC-G03. |
| MC-N11 | `A:80-82` | Seven years, five years, nine years, five years, depending on trade and on the length of financial support. | content. Non-general if used as a promotion threshold. `stated-unverified`. |
| MC-N12 | `A:86` | No universal sacred number of years or common final examination. | as a promotion rule: non-general. as a scope-limit: already MC-G02. |
| MC-N13 | `A:88` | Graduated responsibility through actual work, not a declaration of knowledge. | fleet-metaphor. See CF-3. Cousin of `PROTOCOL.md:61-67`, not its source. |
| MC-N14 | `A:56` first sentence | Prioritize practitioners, workshop accounts, craft associations, museums, and Japanese cultural institutions. | not the chousa hierarchy. Craft-history source preference, `proposal` (the listed sources are not locally openable). Cousin of `SKILL.md:18` must not be re-derived from this list. |

### B — agent architecture and evaluation, not research method

| ID | Anchor | Sentence | Reason |
|---|---|---|---|
| MC-N15 | `B:47` | Rewriting the entire knowledge base can erase useful detail. | agent-architecture. Cousin "don't compress a source into a summary that drops the cited detail" is a different rule and is `proposal` if anyone wants it; it is not this sentence. |
| MC-N16 | `B:47` | Team success does not establish which specialist improved. | agent-evaluation. Tease only — no procedure in the captured text. |
| MC-N17 | `B:55` | The literature supports persistent specialists with external memory, reusable procedures, and evaluated revisions. | agent-architecture content. `stated-unverified`. Out of province if it becomes a model-quality claim. |
| MC-N18 | `B:55` | Weaker support for unrestricted whole-corpus rewriting, or for creating specialists from topic novelty alone. | agent-architecture. Not a domain-split criterion (that answer is absent). |
| MC-N19 | `B:57` | Unit of evaluation is the knowledge change, not the self-assessment. Five axes: task competence, retention, evidence fidelity, cross-domain transfer, operating cost. | agent-evaluation. "Evidence fidelity" must not be aliased to citation discipline. |
| MC-N20 | `B:63-69` | Voyager / Generative Agents / Reflexion / Dynamic Cheatsheet / ACE / Memento-Skills / LEGOMem are precedents for the fleet's SKILL files. | analogy column ("Relevance to shokunin"). Not research method. Paper identities are bare titles plus `arxiv.org` — unresolved. |
| MC-N21 | `B:64` | Voyager's verified code library "differs substantially from freely rewritten factual prose." | agent-architecture comparison. Not "prefer executable evidence over prose" as a chousa rule. |
| MC-N22 | `B:65` | Generative Agents evaluates believable behavior, not increasing domain expertise. | agent-evaluation content. kengaku-adjacent subject. |
| MC-N23 | `B:75` fleet half | Neural expert-expansion results "do not directly validate rules for splitting Markdown corpora." | the transfer ban is MC-G07. The fleet application is non-general, and no split rule is supplied. |
| MC-N24 | `B:77` | Most important KB failure is losing observation / interpretation / established knowledge. | agent-architecture assertion. See CF-1. Do not import. The distinction's local authority is `SKILL.md:45` and `QUALITY.md:5`. |
| MC-N25 | `B:79` prescription | Prefer localized delta updates and structured curation over regenerating the whole playbook. | agent-architecture. Cousin of `QUALITY.md:6` (errata are append-only) must not be derived from ACE. |
| MC-N26 | `B:79` numbers | 18,282 → 122 tokens; 66.7 → 57.1 vs 63.7 baseline. | unverified payload, not a rule. Attached citation does not resolve. |

### C — naming and permission, not research method

Escaping a bad Japanese mapping does not make the replacement a general method. `C:69`'s "Initiate → Grounded → Maintainer → Agentwright" is still a fleet naming scheme.

| ID | Anchor | Sentence | Reason |
|---|---|---|---|
| MC-N27 | `C:53` | Skill, teaching authority, and permission to act are distinct; traditions do not collapse them into one ladder. | governance / fleet-metaphor |
| MC-N28 | `C:53`, `C:81` | "Shokunin → takumi → meishō" is not a standard rank sequence. | lexical content, `stated-unverified`. Keep as a rejection of the prompt's ladder. Not a research rule. |
| MC-N29 | `C:53`, `C:109` | No support found for jin'i-ryū as "self-legislating school." | content negative, `stated-unverified`. Form of the lexical caution is MC-G09. |
| MC-N30 | `C:65` | Use the craft terms as an explicitly modern metaphor; keep certification and permissions separate from the names. | fleet-metaphor / governance. The first clause is an instance of MC-G10. The permission split is not research craft. |
| MC-N31 | `C:65` | No traditional four-rank ladder means created → corpus-verified → safely self-improving → agent-producing. | content negative, `stated-unverified`. Non-general as a maturity model. |
| MC-N32 | `C:67` | Axes: knowledge provenance, demonstrated competence, authority to modify itself, authority to create other agents. | governance. "Knowledge provenance" must not be aliased to source hierarchy. |
| MC-N33 | `C:69` | Recommended names: Initiate → Grounded → Maintainer → Agentwright. | fleet-metaphor. Non-general even though it avoids Japanese terms. |
| MC-N34 | `C:69` | Alternative: Minarai → Shokunin → Shokunin with a self-iteration license → Oyakata with a minting license. | fleet-metaphor |
| MC-N35 | `C:73-79` | Term-fit table (minarai, shokunin, takumi, meishō, oyakata, shihan), including "merely cloning a configuration does not merit oyakata" (`:78`) and "verified corpus alone is insufficient" for the competence shokunin implies (`:75`). | fleet-metaphor by the column header "Fit for your agents." `:75` is not a definition of research completion. |
| MC-N36 | `C:87` | Kyū/dan is a grading structure, not an autonomy ladder. | fleet-metaphor |
| MC-N37 | `C:89` | Go ranks have a performance domain and an external contest that the proposed agent ranks lack. | fleet-design constraint. The commensurate-label form is MC-G11; this application is non-general. |
| MC-N38 | `C:92` | Rank is conferred by a procedure, not by self-description. | governance. Cousin of `PROTOCOL.md:63-67`. Not its source. Not the phrase "self-attestation" (that phrase is prompt-only; see MC-X12). |
| MC-N39 | `C:97` | Dan is not teaching authority (kendo dan/kyū vs shōgō). | governance metaphor |
| MC-N40 | `C:99` | An enduring achievement badge should be separate from current deployment authorization. | governance. Not a research-record rule. |
| MC-N41 | `C:102` | Avoid claiming a single timeless Japanese rank tradition. | historical caution, `stated-unverified`. Form is MC-G02. |
| MC-N42 | `C:105` | Arbitrary "3-kyū, 1-kyū, 1-dan, 2-dan" adds apparent precision without a calibrated scale. Use kyū/dan only with domain examinations and a published grading standard. | fleet-naming. Cousin "don't use a precision-implying citation form you did not resolve" is MC-G13, authority = the gates, not this sentence. |
| MC-N43 | `C:113-118` | 自律 / 自立 / 自己立法 / 流 / 人為 glosses. | lexical content, `stated-unverified`. Keep as a rejection of the prompt's translation. Not research rules. |
| MC-N44 | `C:124` | Jiritsu-ryū 自律流, if used, is a modern coinage and must be labeled as one. | instance of MC-G10 |
| MC-N45 | `C:126` | "Self-legislating" promises rule-rewriting; safe self-iteration means changing implementation inside externally maintained constraints. | governance. See CF-2. Out of chousa province. |
| MC-N46 | `C:130` | Shu–ha–ri has three stages, does not describe minting, does not confer replication authority. "Ri" should never mean a capable agent has outgrown safety constraints. | fleet-metaphor plus a safety policy. **Not a research stopping rule.** A stop-rule note that cites this line has imported the metaphor. |
| MC-N47 | `C:133` | Menkyo kaiden is not "has downloaded the entire corpus" and is not a license to create peers. | fleet-metaphor |

`A:60-65` "Implication for your roster" cells are the same class as MC-N04–N08. No cell in that table is a general research-craft rule.

### Lane files that are already mixed, and should stay split

| Anchor | What it is | Scope |
|---|---|---|
| `chousa-shokunin/SKILL.md:13-21` | question, hierarchy, chain, claim check, reuse | general method. Does not import the rank ladder. Leave it. |
| `chousa-shokunin/SKILL.md:3` | `Rank: shonen` in frontmatter | fleet-metaphor metadata. Not a research rule. |
| `chousa-shokunin/SHONEN.md:3-8` | promotion checklist | fleet rank gate (`PROTOCOL.md:63-73` is the authority). Box 1's "cited sources" overlaps citation discipline; the overlap is not a reason to derive the citation rule from the rank checklist. |
| `chousa-shokunin/PROVINCE.md:3-12` | owns the method; refuses bounty scope, model-quality claims, unapproved live targets | boundary, not metaphor. Holds. |
| `chousa-shokunin/MINT.md:8-13` | artifacts are the unowned method pattern | the claim under attack. The unowned province is real. These files are not that province's content. |
| `PROTOCOL.md:21` | `mint → shonen → shokunin → jin'i-ryu` | fleet-metaphor lifecycle. Chousa does not validate it and does not correct it. |
| `research/README.md:6-8` | not the Deep Research pipeline; "9/8/10 web searches each" | instrument label is partly observed (export says `GPT-6 Astra` at `A:96`, `B:87`, `C:141`, and shows a web-search UI). The entitlement denial and the 9/8/10 counts are operator assertions. See unknowns. |

Vendor boilerplate `ChatGPT can make mistakes. Check important info.` (`A:90`, `B:81`, `C:135`) is a product disclaimer, not a research rule and not a substitute for `SKILL.md:20`.

## Absent — solicited, not in the response body

Unknown, not negative findings. The tails are not in the local artifacts. A later external window might recover them; this round must not invent them.

Sweep: `rg -n 'ikigai|kodawari|hoard|hallucin|inflation|self-attest|forgetting' research/deep-research-2026-09-28` hits only the `You said:` lines (`A:35`, `B:35`, `C:35`).

Sweep: `rg -n '^[0-9]\. |^\([0-9]\)' research/deep-research-2026-09-28` hits only `A:74` (section 1) and `B:77` (`(1)`). No section 2 or 3 heading exists before either cutoff (`A:90`, `B:81`).

| ID | Asked at | Not present after the `ChatGPT said:` body starts | Status |
|---|---|---|---|
| MC-X01 | `A:35` question (2) | whether a master ever finishes | unknown (truncated) |
| MC-X02 | `A:35` question (3) | obligation to teach vs hoard | unknown (truncated) |
| MC-X03 | `A:35` question (4) | how narrow mastery is evidenced publicly | unknown (truncated) |
| MC-X04 | `A:35` | ikigai | unknown (truncated or never answered; not distinguishable locally) |
| MC-X05 | `A:35` | kodawari | same as MC-X04 |
| MC-X06 | `B:35` question (1) third failure mode | hallucinated citations, as a finding | unknown. UI chrome `B:49` says "Analyzing AI Citation Errors and Persistent Memory" — that is a status label, not a finding. |
| MC-X07 | `B:35` | forgetting, as a finding | unknown |
| MC-X08 | `B:35` | drift, as a finding | unknown. The word does not occur in B's body. |
| MC-X09 | `B:35` question (2); teased at `B:47` | when to split a domain vs expand one | unknown. `:47` says the check is in progress. No criterion follows. |
| MC-X10 | `B:35` question (3); teased at `B:40` and `B:47` | a credit-assignment procedure | unknown. MC-N16 is a one-sentence tease, not the procedure. |
| MC-X11 | `C:35` | "rank inflation" as a named failure mode | absent as a name. Do not equate MC-N42 (false precision) or MC-N37 (no external contest) with a finding that inflation was demonstrated. |
| MC-X12 | `C:35` | "self-attestation" as a named failure mode | absent as a name. Body has "self-description" at `C:92` (MC-N38). Related, not the same phrase, not a completed failure-mode survey. |

C is less truncated than A or B: the naming question and several permission distinctions are in the body. That does not make C a method artifact. It makes C a completed-enough metaphor correction.

## Search-count claim

`research/README.md:8` says the three responses are "9/8/10 web searches each."

Sweep: `rg -n '9/8/10|Searched the web' research` → the numeral string is only at `README.md:8`. Visible `Searched the web` markers: `A:42` (1), `B:42` (1), `C:42` and `C:55` (2). C also shows collapsed chips (`C:48` "10 more"), which are not a count of ten searches.

**Observation:** the export bodies do not contain 9/8/10.
**Unknown:** whether the live session did that many searches. The chips may have collapsed them. Not contradicted. Not verified. Do not cite README:8 as a measured search census.

## Observation / inference / unknown

**Observation.** The three exports are ChatGPT UI transcripts. Response bodies end at `A:90`, `B:81`, `C:135` and continue as UI chrome. Citation forms in those bodies do not include a URL or an arXiv id (sweep above). The analogy columns are self-labeled. chousa's decision table does not currently contain the rank ladder. The fleet already enforces resolvable citations, separate verdict classes, and a named reverify declaration (anchors in MC-G13).

**Inference.** A corpus note that copies README:13-14, B:57, or C:67 into `knowledge/` under a method heading would change chousa's identity and collide with `AXES.md` and `PROTOCOL.md:21`. Labeled inference, not a landed defect: the knowledge directory is still empty (`chousa-shokunin/corpus/README.md:7`).

**Unknown.** External attestation of every "I haven't found" sentence. Whether truncated tails exist in a session this tree does not hold. Whether the operator's 9/8/10 count is true of the live tabs. Semantic support of any bare `コトバンク` / `arxiv.org` chip. This review did not fetch, so those stay unknown rather than false.

## Rejections kept

| Rejected move | Reason |
|---|---|
| Admit MC-N02 / MC-N19 / MC-N32 as chousa axes | identity change; three lists disagree with each other and with `SKILL.md:17-21` |
| Re-derive `SKILL.md:45` from B:77 | CF-1, mismatched evidence, wrong scope |
| Re-derive `PROTOCOL.md:63-67` from A:88 or C:92 | CF-3; cousin, not source |
| Re-derive `QUALITY.md:6` from B:79 | ACE playbook curation is not append-only errata |
| Treat C:69's English ladder as the general method because it avoids Japanese terms | leaving the metaphor's vocabulary does not leave the metaphor's job |
| Use C:130 "Ri never means outgrown constraints" as the research stop rule | safety policy wearing a learning-stage metaphor |
| Treat MC-X01–MC-X12 as either admitted rules or as negative findings | truncation is not a sweep of the tradition or the literature |
| Amend `PROTOCOL.md:21` from A:64 / C:109 | labeling rule (MC-G10) is chousa's; the ladder is not |

## Impacted axes

| Axis | Before this tag | After the tag |
|---|---|---|
| coverage | A method note mined from imperatives would record three axis lists and miss twelve solicited questions that are not in the bodies. | General forms, non-general rows, and absences are separate lists. Empty `knowledge/` is not filled with the wrong objects. |
| depth | B:77, C:126, and A:88 look like evidence-backed rules if the next sentence is not read. | Each is paired with the lines that do not support it, and with the local rule it must not replace. |
| calibration | README:13-14 can be reread as a research result. C:69 can be reread as "we escaped metaphor, so this is method." README:8 can be reread as a measured search census. | Scheme axes stay scheme axes. English renames stay non-general. 9/8/10 stays an operator assertion. Export sentences stay `stated-unverified` where the hop is bare. |

## Not done

No judge verdict. No corpus edit. No gate run. No external fetch. Sibling slices (content routing, injection census, citation-form counts, the approval table) were not repeated; the only cross-slice constraint stated here is the one that is this slice's defect: do not import MC-N46 into a stopping rule, MC-N24 into the quality bar, or MC-N14 into the source hierarchy.
