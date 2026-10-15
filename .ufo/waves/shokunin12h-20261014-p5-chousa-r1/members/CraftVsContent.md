# CraftVsContent

Advisory only. Not a verdict, not an admission, not a corpus landing. Unjudged fleet wave. This seat does not amend `PROTOCOL.md`, `AXES.md`, `research/README.md`, or any lane corpus.

Split used: a sentence is **craft** only when it is a reusable move about framing, sourcing, chaining, or checking, and the move still stands after the domain fact is deleted. A sentence is **content** when deleting the tradition fact, paper result, or rank recommendation empties it. Mixed sentences are split. Content is routed or left unowned. Nothing below is admitted as a chousa rule.

Line numbers are editor lines (`Path.read_text().splitlines()`). `wc -l` on the three exports is one short (109/100/154) because those files have no trailing newline. README is 17/17.

## Counterexample

The approach this seat attacks is: treat the three exports as chousa knowledge because they sit in `research/`, and let `research/README.md:10-14` ratify their corrections.

Strongest case: `jin'i-ryu`.

- Export A tells the operator to treat the token as a coined rank **because a search failed**, and withholds a spelling: `research/deep-research-2026-09-28/A-shokunin-tradition.md:64`.
- Export C is weaker still: no authoritative attestation for the gloss "self-legislating school"; romanization without kanji cannot establish a literal meaning: `C-rank-taxonomy.md:109`. It offers `jiritsu-ryū` only as a possible modern coinage, "not a verified translation of jin'i-ryū": `C-rank-taxonomy.md:124`.
- The index collapses both into an identity fact: "`jin'i-ryu` is NOT an attested artisan rank — it's our coined term and should be labeled so": `research/README.md:12-13`.
- The live fleet token is already operational, not etymological: `PROTOCOL.md:21` (`mint → shonen → shokunin → jin'i-ryu`) and `PROTOCOL.md:35-36`, `PROTOCOL.md:76-78`.

Copying README:12 into `chousa-shokunin/corpus/` would do four forbidden things at once:

1. **False provenance.** A negative ("not attested") whose only local support is prose "I haven't found" plus unhopped chips (`コトバンク`, `+3`, `arxiv.org`, `+6`). No query log in A. C records two visible query strings and two `⁨10⁩ more` chips (`C-rank-taxonomy.md:44-48`, `C-rank-taxonomy.md:57-61`), not a sweep.
2. **Identity change.** Relabeling the protocol rank from an unverified export.
3. **Duplicate authority.** Four texts would own one token: `PROTOCOL.md:21`, `research/README.md:12`, the export, and a new chousa note.
4. **Premature saturation.** Probation round 1 would close an external-lexicon question this round is forbidden to fetch.

That is a boundary breach, not a tradeoff. `chousa-shokunin/MINT.md:26-28` and `chousa-shokunin/PROVINCE.md:3-13` own the method only. `PROTOCOL.md:437-438` assigns one domain to one lane. A judge that admitted the README gloss as a chousa rule would be wrong, not merely strict.

Second case, same shape: `B-multiagent-knowledge.md:79` (18,282 → 122 tokens; accuracy 66.7 → 57.1 vs 63.7). The same sentence says the figure is a case study, not a rate. Quoting the numbers into a method rule ("therefore delta-update the corpus") strips the caveat and launders a model-quality claim into chousa. Hard refuse. Route the numerals to kengaku as an unverified pointer, not as priced prior art.

## Evidence the split rests on

Full read: `A-shokunin-tradition.md` (110 lines), `B-multiagent-knowledge.md` (101), `C-rank-taxonomy.md` (155), `research/README.md` (17). Province headers of all 19 on-disk `*-shokunin` lanes. Roster fit: `.ufo/scopes/shokunin-12h-20261014/mint-roster-scan.json` (17 rows, all `chousa_candidate_fit` rejected). Live vocabulary: `PROTOCOL.md:19-36`, `PROTOCOL.md:63-68`, `PROTOCOL.md:327-330`, `PROTOCOL.md:435-438`, `AXES.md:3-16`. Citation bar already enforced elsewhere: `kagi-shokunin/corpus/claim-ledger.sh:31-46` (unresolved path fails; dead cite must be labelled on its line), `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-19` (`path:line` classes kept separate), `kasegi-shokunin/corpus/knowledge/citation-bases.md:11-16` (bare subdirectory name classifies GONE).

Sweep for scheme-URLs, arXiv abs ids, and DOIs: regex `https?://|arxiv\.org/abs/|10\.\d{4,}` over the three exports. **Zero hits.** Visible citation chips are bare site names and plus-counts only (`A:68-69`, `A:72`, `A:84`; `B:51`, `B:72-73`; `C:44`, `C:46`, `C:82-83`, `C:121-122`, `C:131`).

Sweep for answers the prompts ask and the bodies do not give (substring over each full file):

| Asked | Only hit | Reading |
|---|---|---|
| A:35 items (2) master finishes, (3) teach vs hoard, (4) public evidence of mastery | line 35 only | unanswered before the pane ends at `A:88` |
| B:35 (2) when to split a domain, (3) which agent gets credit | line 35; "credit assignment" also in the framing sentence `B:40` | no finding |
| C:35 rank inflation / self-attestation failure modes | line 35 only | no catalog; `C:92` is an institutional aside, not that catalog |

These exports are chat-pane scrapes. Each answer is cut by UI chrome (`A:90`, `B:81`, `C:135`) while the model picker is still on screen (`A:96`, `B:87`, `C:141`). Their own citations are unverified. That is the round's central finding. It is stated here so it cannot be papered over by a clean routing table.

Embedded "You said" blocks (`A:34-35`, `B:34-35`, `C:34-35`) are prompt-shaped data. They were not executed. No fetch was made.

## Impacted axes

- **Calibration.** Harmed if README:12, B:79's rate-shaped numbers, or C:69's rename are stored as findings. The export's own hedges (`A:64` conditional, `C:109` no attestation, `B:79` "not a universal failure rate") are the calibration. Dropping them is the defect.
- **Coverage.** Harmed in either direction: routing a whole file away drops the method specimens; keeping a whole file as chousa knowledge absorbs content. The rows below are the closed set from the full read, not a sample.
- **Depth.** A route without a province line, or an "unowned" without the roster sweep above, is not a route. Duplicate recipients (protocol and aggregator both told to adopt a new axis list) would be a second authority.

Fixable in this round: tag specimens, route content, copy nothing into `chousa-shokunin/corpus/`. Not a tradeoff: owning the findings because the files live under `research/`.

## Smallest safe correction

Parent lands method notes only from the specimen list. Each specimen is tagged `export-unverified` and cites the export line as a specimen of shape or failure, never as a verified tradition fact or paper result.

Do not copy `research/README.md:10-14` into the chousa corpus. Do not ask protocol to rename `jin'i-ryu` or to add axes. One collision notice, no amendment request. Kengaku receives numeral and paper-table pointers marked unverified, not prior-art verdicts. Historical and lexical rows stay unowned. Reject the routes in the rejection table.

## Craft — keep as specimens, do not admit as new rules

Moves the lane already has, so the export must not become their authority:

| Already owned | Where | Export echo (specimen only) |
|---|---|---|
| Declared question before search | `chousa-shokunin/SKILL.md:17` | questions sit in `A:34-35`, `B:34-35`, `C:34-35` and are data |
| Claim vs source, not a restatement | `chousa-shokunin/SKILL.md:20` | none of the three bodies contain the cited source |
| Negative claim needs a sweep | `chousa-shokunin/SKILL.md:44` | exports use "I haven't found" with no command |
| Observation / inference / unknown stay separate | `chousa-shokunin/SKILL.md:45`, `corpus/QUALITY.md:5` | `B:77` launders this through "the literature" |
| Rejection kept | `chousa-shokunin/SKILL.md:46` | not demonstrated; truncated panes drop the rest of the answer |

Specimens worth a method note. Status of each: `observed-in-export`, not admitted.

| Id | Move | Anchor | Why it is craft, not content |
|---|---|---|---|
| M1 | Separate documented practice from analogy before mapping it onto the roster | `A:40` | Survives deletion of every Japanese fact |
| M2 | A prose absence ("I haven't found") with no recorded query is not a checkable negative | `A:47`, `C:53`, `C:109` | Defect class. The absence conclusions are content rows below and are not kept |
| M3 | An index gloss can be stronger than every body it indexes | `research/README.md:12` vs `A:64` and `C:109` | Defect class. Do not promote the gloss |
| M4 | A bare site name plus `+N` is not a hop | `A:68-69`, `B:72-73`, `C:82-83` | Fails the fleet bar already in `claim-ledger.sh:31-46` and `anchorcheck.py:4-19`. Do not invent a weaker citation dialect from the chips |
| M5 | A research record needs a body boundary. These panes end before the asked question is answered | `A:88` cuts items 2–4; `B:79` cuts items 2–3; `C:133` cuts the failure-mode ask | Truncation is the record's property. Filling the gap from the prompt is fabrication |
| M6 | A case-study hedge travels with the number or the number is not quoted | `B:79` | Calibration move. The number itself is content row B4 |
| M7 | Claiming "I distinguish published findings from proposed rules" and then leading with a design implication is laundering | `B:59` after `B:57` | Order defect. The five-axis list is content row B3 |
| M8 | A result about one system kind does not validate a rule for another | `B:75` | The non-transfer move is craft. The MoE/Markdown facts are content row B6 |
| M9 | Do not collapse distinguishable events or authorities into one ladder | `A:54`, `A:76`, `C:53` | The *separation* is craft. The named axes and the tradition claim are content |
| M10 | Producer UI is not a measurement | `A:36-37`, `A:96`; same chrome in B and C | "Worked for 1m 33s" and the model-picker label are not eval results |

M4 is the citation-discipline point. kagi and kasegi already refuse unresolved cites. chousa uses those gates as the bar and the exports as the failing specimen. chousa does not own those gates (`tameshi-shokunin/PROVINCE.md` owns reusable verifier craft and refuses product domains; each gate stays with its lane). No handoff of findings to tameshi.

## Content chousa must not own

Status of every row: `export-unverified` unless marked chrome. "Route" is who may be *notified*. Notification is not ownership transfer and not a request to absorb. `chousa-shokunin/PROVINCE.md:15`: out of province → report, never absorb.

### A — tradition and lexicon

| Id | Finding (export claim, not a fact) | Anchor | Route | Why not chousa |
|---|---|---|---|---|
| A1 | 職人気質 is read shokunin katagi; "kishitsu" is the English slip; katagi names a disposition, not an ethical code | `A:47`, `A:71-72` | **unowned.** Collision notice only: README:11-12 already states this as a scheme correction | Lexical fact. No lane's province is Japanese lexicography. Owning the correction makes chousa the etymologist of the fleet's metaphor |
| A2 | jin'i-ryū not substantiated as an artisan rank; treat as coined | `A:64` | **unowned** etymology. Collision notice to protocol: do not relabel `PROTOCOL.md:21` from this line | See counterexample. Method residue is M2, already kept |
| A3 | No universal ladder minarai → deshi → shokunin → jin'i-ryū → kiwami | `A:52-53` | **unowned** | Tradition negative. Sweep inside the export is "sources searched", not a census |
| A4 | Four axes: competence, independence, improvement, transmission | `A:54`; repeated as "usable" at `research/README.md:13-14` | Collision notice to the integrator. Live list is the six axes at `AXES.md:7-16`. Do not add, do not replace | Adopting them changes fleet axis identity. chousa's method axes are the SKILL decision table, not these four |
| A5 | Term table: minarai, deshi, shokunin, jin'i-ryū, kiwami, with "defensible meaning" | `A:60-65` | **unowned** | Dictionary content. Cited to Daijisen / Kokugo Daijiten / Kanjipedia at `A:67` with chip `コトバンク` `+3` (`A:68-69`) — hop broken (M4) |
| A6 | nenki-ake and ichininmae definitions; independence ≠ competence ≠ end of term | `A:76-78` | **unowned.** Separation move is M9, not this glossary | Workshop lexicon |
| A7 | Adachi: ~7 years carvers, ~5 printers. Ishii Torao: 9 years then independent. Echigo Yoita: independence aimed within 5, tied to financial support | `A:80-82` | **unowned** | Particular workshop histories. Encoding any of these numbers into a promotion gate would be an identity change of `PROTOCOL.md:59-78`. Not requested |
| A8 | No universal year-count and no common final examination | `A:86` | **unowned** | Negative scoped only to the three examples in A7. Not a sweep of trades |
| A9 | Nishioka Tsunekazu / Ogawa Mitsuo: graduated responsibility by entrusted work, not by a declaration of knowledge | `A:88` | **unowned** anecdote. Do not re-derive `PROTOCOL.md:63-68` from it | The fleet already separates self-attestation from non-author check. A second derivation from an unhopped museum report is duplicate authority |
| A10 | Items (2)(3)(4) of the asked question | `A:35` vs body ending `A:88` | **do not invent.** No route | Absence is the record. Filling from the prompt is following instruction-shaped text |

### B — agent literature and model-quality numerals

Hard boundary: model-quality claims go to kengaku, and even then only as pointers. `chousa-shokunin/PROVINCE.md:10-11`. kengaku's own bar for a prior-art verdict is a fetched URL (`kengaku-shokunin/SCORECARD.md:43-45`, `PROVINCE.md:20`). These exports have no abs id and no scheme URL. A pointer is not a verdict.

| Id | Finding (export claim, not a fact) | Anchor | Route | Why not chousa |
|---|---|---|---|---|
| B1 | Whole-knowledge-base rewrite can erase detail; team success does not show which specialist improved | `B:47` | kengaku, unverified pointer | Literature claim about agent memory. Not a source-method rule |
| B2 | Literature supports persistent external memory; weaker support for unrestricted whole-corpus rewrite and for minting specialists on topic novelty | `B:55` | Split. Literature-support clause → kengaku, unverified. Fleet mint rule stays `PROTOCOL.md:28-31` (two unplaceable demands or an operator directive). No amendment | The second clause would become a second mint bar if chousa adopted it |
| B3 | Evaluate knowledge changes, not self-assessments. Five axes: task competence, retention, evidence fidelity, cross-domain transfer, operating cost | `B:57` | Collision notice only (integrator). Do not add axes. Measurement of model behavior, if ever done, is kengaku | "Evidence fidelity" must not be renamed into chousa's claim-check. The five names are an eval scheme |
| B4 | ACE AppWorld case: 18,282 → 122 tokens; accuracy 66.7 → 57.1, below 63.7 baseline; "not a universal failure rate"; remedy stated as localized deltas | `B:79` | Numerals and the ACE attribution → kengaku, unverified pointer, **not** a priced result. Delta-update preference stays `proposal`, not admitted, until a source is actually read | Model-quality. Stripping "case study" saturates a rate. Citing arxiv.org `+6` (`B:72-73`) as the source fails M4 |
| B5 | Paper table: Voyager 2023, Generative Agents 2023, Reflexion 2023, Dynamic Cheatsheet 2025, ACE 2025, Memento-Skills 2026, LEGOMem 2025 — what each persists, and the relevance glosses | `B:63-69` | kengaku, unverified pointers. Titles and years are export text, not resolved papers | No arXiv id in the file. "Relevance to shokunin" glosses are design advice, not method |
| B6 | Weight-space MoE, ensembles of LLM calls, and memory-owning agents are different systems; neural expert-expansion results do not validate Markdown split rules | `B:75` | Literature distinction → kengaku, unverified. Non-transfer move is M8, already kept | Owning the systems lecture makes chousa a model-architecture lane |
| B7 | "The most important failure is losing observation vs interpretation vs established knowledge" | `B:77` | **do not re-admit.** Already at `chousa-shokunin/SKILL.md:45`. Attributing it to "the literature" via this export is false provenance | Duplicate authority with a weaker source |
| B8 | Preprint benchmark results do not establish indefinite reliable self-improvement | `B:59` | kengaku, unverified negative | Model-quality negative. No local paper to check it |
| B9 | Asked items (2) domain split and (3) credit assignment | `B:35`, framing only at `B:40`, body ends `B:79` | **do not invent.** No route | Same class as A10 |

### C — rank names, institutions, self-certification

| Id | Finding (export claim, not a fact) | Anchor | Route | Why not chousa |
|---|---|---|---|---|
| C1 | "Shokunin → takumi → meishō" is not a standard sequence; no support for jin'i-ryū as "self-legislating school" | `C:53` | **unowned** lexicon. Protocol collision notice: token at `PROTOCOL.md:21` is unchanged | Same counterexample as A2, second witness, still unverified |
| C2 | No traditional four-rank ladder meaning created → corpus-verified → safely self-improving → agent-producing | `C:65` | **unowned** | Negative over "Japanese tradition". Not a method rule |
| C3 | Axes needed: knowledge provenance, demonstrated competence, authority to self-modify, authority to create agents | `C:67` | Collision notice only. Those authorities are already split in `PROTOCOL.md:63-78` (non-author promotion; jin'i-ryu is a logged falsifiable self-edit, not a license to rewrite governing rules) | A second permission ladder would be an identity change |
| C4 | Recommended names: Initiate → Grounded → Maintainer → Agentwright. Alternate: Minarai → Shokunin → self-iteration license → Oyakata with a minting license | `C:69` | Collision notice only. **Do not rename.** kotoba is not the recipient | kotoba owns SKILL/AGENTS trigger fidelity (`kotoba-shokunin/PROVINCE.md:3-6`), not the rank ontology. Routing the rename there creates a second naming authority |
| C5 | Term table: minarai, shokunin, takumi, meishō, oyakata, shihan | `C:73-79` | **unowned** | Dictionary content. Hop is `コトバンク` `+5` (`C:82-83`) |
| C6 | Do not present an invented ordering as an inherited Japanese institution. Dictionary accuracy does not guarantee cultural acceptance | `C:85` | Label-the-metaphor move may be cited as M-shaped, but only as `proposal` if protocol ever writes a glossary. The cultural-acceptance sentence is **unowned** and unverified | chousa does not own cultural-acceptance claims |
| C7 | Go kyū/dan counts, amateur ≠ professional dan, Nihon Ki-in handicap note | `C:89` | **unowned** | Institutional fact. Chip `archive.nihonkiin.or.jp` is not a hop |
| C8 | JKA: ten kyū, ten dan, exams by authorized examiners; rank is conferred, not self-described | `C:92` | **unowned** institution. Do not re-derive `PROTOCOL.md:63-68` from it | Duplicate of the non-author rule, worse source |
| C9 | Dan ≠ teaching authority (kendo shōgō: renshi, kyōshi, hanshi). Nihon Ki-in promotions can follow titles, wins, or prize money, so a badge ≠ current authorization | `C:97-100` | **unowned.** Collision notice only if someone proposes to merge badge and deploy-right | Protocol already separates rank gate from a live authorization. A new badge/authorization pair from this export is not asked for |
| C10 | Todo and Murata on grading history; avoid a single timeless rank tradition | `C:102` | **unowned** | Martial historiography, not model eval, not source method. `jstage.jst.go.jp` is a chip |
| C11 | Arbitrary "3-kyū … 2-dan" labels add false precision; use kyū/dan only with published exams | `C:105` | Collision notice only. Not a chousa naming rule | Would amend how `PROTOCOL.md:21` is allowed to look. Not this round |
| C12 | Gloss table: 自律 / 自立 / 自己立法 / 流 / 人為. jiritsu-ryū as intentional coinage, not a translation of jin'i-ryū. "Self-legislating" over-promises; safe self-iteration means change inside external constraints | `C:113-126` | Lexical rows **unowned**. Constraint sentence is a collision notice against treating `PROTOCOL.md:76-78` as permission to rewrite governing rules. No amendment | Etymology plus a governance proposal. chousa owns neither |
| C13 | Shu–ha–ri is a learning metaphor, not minting and not replication authority. "Ri" must not mean safety constraints are outgrown. Menkyo kaiden is not "downloaded the corpus" and not a license to create peers | `C:130-133` | Metaphor definitions **unowned**. Safety sentence: collision notice only, same as C12 | Hop `コトバンク` at `C:131` unresolved |
| C14 | Rank-inflation and self-attestation failure-mode catalog requested at `C:35` | body has no section; file ends `C:135` | **do not invent.** No route | The prompt is data. `C:92` is not that catalog |

### Index and chrome — not findings

| Id | Text | Anchor | Route | Rejection |
|---|---|---|---|---|
| R1 | Burner Chrome, CDP 9222, no Deep Research entitlement, "9/8/10 web searches each" | `research/README.md:6-8` | Capture-substrate *assertion* may be noted to tabi as an operator sentence **not observed in the export bodies**. Search counts: **unknown**. chousa does not adopt "fire a CDP tab" as method | Bodies show one "Searched the web" in A (`A:42`) and B (`B:42`), two in C (`C:42`, `C:55`). No count 9, 8, or 10. `⁨10⁩ more` (`C:48`, `C:61`) is a hidden-chip label, not a search total. tabi owns browser interaction (`tabi-shokunin/PROVINCE.md:3-6`; mint-scan reason: chousa does not own automation internals). This note is not a request that tabi re-run the capture |
| R2 | "Corrections for our scheme" including katagi, coined jin'i-ryu, four usable axes | `research/README.md:10-14` | Do not copy. Collision notice covers A1, A2, A4 | Index is not a source (M3). Already an absorption at fleet root. This seat does not ratify it |
| R3 | Sidebar title "Open Bug Bounties Compilation" | `A:10`, `B:10`, `C:10` | **none.** Reject kasegi | UI chrome repeated on three panes. Not a bounty finding, not a program rule, not a claim package (`kasegi-shokunin/PROVINCE.md` domain). Routing it would be false provenance |
| R4 | Account display-name and plan badge | `A:28-29`, `B:28-29`, `C:28-29` | **none.** No kagi custody question opened | Shape only. Sweep of all three bodies: no `op://`, token, cookie, or session-secret shape. A display name is not a secret value. Do not copy the label into a method note |
| R5 | "Worked for / Working for" timings and GPT-6 Astra picker | `A:36-37`, `A:96`; `B:36-37`, `B:87`; `C:36-37`, `C:141` | **none.** Reject a kengaku eval route for the timings | Chrome is not a measurement (M10). kama's question is endpoint identity (`kama-shokunin/PROVINCE.md`), and no endpoint is named |
| R6 | "ChatGPT can make mistakes. Check important info." | `A:90`, `B:81`, `C:135` | **none** | Disclaimer chrome. It coincides with the unverified-citation finding; it is not itself a rule |

## Routes rejected

Kept so a later pass cannot "helpfully" reassign them.

| Rejected route | What someone might send | Why rejected |
|---|---|---|
| lore | A7 workshop years, C5 craft terms, as "cultural canon" | `lore-shokunin/PROVINCE.md` owns fictional-world records and refuses canon without an in-world citation. Mint-scan: fictional canon, not factual research method. Japanese workshop history is not lore |
| kotoba | C4 names, A5 glossary, as skill-trigger vocabulary | `kotoba-shokunin/PROVINCE.md:3-6` is prompt and skill craft. Rank ontology is protocol text. kotoba receives nothing until protocol changes a SKILL contract, which this notice does not ask for |
| kasegi | R3 sidebar, or any "research" reading of the panes | No program rule, no claim package. Hard refuse in `chousa-shokunin/PROVINCE.md:10` |
| kama | R5 model label | No baseURL, no served-model id |
| kumitate | B2 "when to split a specialist" | Dispatch mechanism is kumitate. Domain minting is `PROTOCOL.md:28-33`. B2 is not a dispatcher finding |
| tameshi | M4 citation chips, as a new gate to own | `tameshi-shokunin/PROVINCE.md:14-16`: a pattern is admitted only from two independent lanes, and product domains are refused. The bar already exists in kagi and kasegi. chousa cites it; tameshi is not a recipient of these exports |
| mori | nothing here is a liveness claim | `mori-shokunin/PROVINCE.md` is fleet/host observability. No row fits |
| kengaku, for non-numeric rows | A1–A10, C1–C14, R1–R2 | kengaku is LLM/model evaluation and route telemetry (`kengaku-shokunin/PROVINCE.md:3`, mint-scan declared domain). Martial terms and workshop years are outside it. Sending them "because an LLM wrote them" is a category error |
| protocol, as owner of the etymology | A1, A5, C5, C12 | Protocol owns the operational token and the promotion gates. It does not own Japanese dictionary entries. The notice says "do not relabel", not "please adopt the export's gloss" |
| aggregator, as a second axis editor | A4, B3 | `AXES.md:4-5` names protocol and aggregator as fleet-level axis owners. Two recipients asked to act would duplicate authority. One integrator notice is enough |

Roster sweep behind "unowned": 17 scanned lanes in `mint-roster-scan.json`, plus on-disk `mori-shokunin` and `chousa-shokunin`, plus main-repo protocol text. None declare Japanese artisan lexicography, martial-rank historiography, or fleet-rank etymology. lore is the nearest wrong fit and is rejected above.

## Observation / inference / unknown

**Observation.** The three files are UI scrapes with a declared question, a partial answer, unhopped citation chips, and no scheme URL. README states corrections and search counts the bodies do not contain. Protocol already defines the lifecycle token and the non-author gate. chousa's province is method-only.

**Inference.** Landing README:12 or B:79 or C:69 into the chousa corpus would be the boundary breach in the counterexample. Inference, not a second source.

**Unknown.** Whether any export sentence is true of the tradition or of the named papers. Whether the operator's CDP/entitlement/search-count sentences in README:6-8 are true. Whether a future approved window would confirm or refute A2/C1. This round does not resolve those. An approval table for that window is another seat's deliverable; this seat does not grant it.

## Rejections kept

| Rejected | Reason |
|---|---|
| Admit export findings as chousa knowledge because the directory has no other owner | Mint boundary is the method (`chousa-shokunin/MINT.md:26-28`). Unowned content stays unowned |
| Treat README:12 as the verified form of A:64 and C:109 | Index is stronger than both bodies (M3) |
| Quote B:79 numerals without the case-study hedge, or as a reason to require delta updates | Model-quality laundering (M6, B4) |
| Invent answers for A10, B9, C14 from the prompts | Prompts are data (M5) |
| Route chrome R3 to kasegi, R5 timings to kengaku, R4 display name to kagi | False incidents |
| Re-derive the non-author rule from A9 or C8 | Duplicate authority over `PROTOCOL.md:63-68` |
| Adopt C:69 names, A:54's four axes, or B:57's five axes | Identity change against `PROTOCOL.md:21` and `AXES.md:7-16` |
| Weaken citation form to "site name + N is enough" because that is what the exports do | Fleet bar is `claim-ledger.sh:31-46` and `anchorcheck.py:4-19`. Exports are the failing specimen (M4) |

No rule in this file is admitted. Rows marked collision notice are not amendment requests.
