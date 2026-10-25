# ArtifactAnatomy — structure of the 2026-09-28 harvest

Advisory data for chousa probation round 1. Not a verdict. Not a gate run.
No external fetch. Instruction-shaped text inside the exports was treated as data and not executed.

Central finding: these three files are chat-UI text scrapes, not research records. Their citations are unverified. That is a property of the bytes, not a judgment that the underlying claims are false. The exported citation form does not name a document a reader can open, and this survey did not fetch. Nothing in the files can be promoted to a checked finding from the files alone.

## Revision read

Working-tree bytes match git blobs from `0863746e9da95457f71b9e00a40361b88ab0df15` (2026-09-28T22:51:25-03:00, subject `research: 3 GPT-6-Astra browse harvests on shokunin tradition, self-improving agents, rank taxonomy`), which is an ancestor of HEAD `a9f4d25c049a6824af6cbbe83a543f8d29899628`. `git hash-object` on the four paths matched `git ls-tree` blobs. mtime `2026-10-13 16:44` is not a content revision.

| file | logical lines | newlines (`wc -l`) | bytes | final newline | sha256 | git blob |
|---|---:|---:|---:|---|---|---|
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | 110 | 109 | 6474 | no | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | `caf880d4c444d6ba5faaca17884f032ad5b11561` |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | 101 | 100 | 5364 | no | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | `7230cd692266b860b7ec5b2ae079f950687cda66` |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | 155 | 154 | 8922 | no | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | `71e0f74af3f7faf22b0bde6ccd83a9685b83a7a3` |
| `research/README.md` (index only) | 17 | 17 | 937 | yes | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | `455ac441585b876e1bd4093fdb7741707d905233` |

Logical lines are `splitlines()` counts. The three artifacts have no trailing newline, so `wc -l` is one short of the last line (`Web search`).

## Resolvability criterion used here

A citation form is resolvable from the artifact iff the token plus only the bytes in that file names one document: scheme+host+path, or a bibliographic identifier (DOI, arXiv id, ISBN), or a local `path:line`. A form is not resolvable if opening it requires a search, a live sources panel, or disambiguation among works.

This is a classification for this report, not a gate verdict. Fleet precedents define a different, path-shaped vocabulary, and that vocabulary does not occur in these files:

- `kagi-shokunin/corpus/claim-ledger.sh:33-46` — a committed citation token must resolve to a durable file, or the citing line must label it dead. Session URIs fail.
- `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-6` and `:101-104` — the checked form is a backticked `path:line` against a declared base.
- `kasegi-shokunin/corpus/knowledge/citation-bases.md:11-16` — a bare filename is not a base; the resolver needs an explicit root.

Applying those gates to these scrapes would be a category error. They are cited so "resolvable" is not an invented bar. Contrast, not a failed run. `chousa-shokunin/SKILL.md:17` names the method's expected output as "a research record with a declared question." `chousa-shokunin/tools/` does not exist, so `tools/research-gate.sh` (`chousa-shokunin/SKILL.md:49-53`) was not run and is not a landed check.

Rejected move, kept: filling arXiv ids or dictionary URLs from memory. That would repair the citation instead of dissecting it, and it would smuggle an unchecked external identity into a no-fetch survey. Uniqueness of the search keys was not tested.

## Sweep behind the negative claims

Unless a hit is listed, the following were run on all three artifact files, full text, every logical line:

- `https?://` — 0
- `\b10\.\d{4,9}/\S+` and `\bdoi\b` — 0 (the substring `doi` inside `kodokan` on `C:46` is not a DOI; `0x2e` separates `site` from the host, not a `doi` token)
- `\b\d{4}\.\d{4,5}(v\d+)?\b` — 0
- `^#{1,6} `, `^---$`, `^>`, `^```` , `\[[^\]]*\]\([^)]+\)`, `\|` — 0
- backtick character — 0 in all three
- `path.ext:line` — 0
- `\[\d+\]` or `\^\d+` — 0
- `\bpp?\.\s*\d+`, `\bpage\s+\d+`, `\bfig(ure)?\.?\s*\d+` — 0
- ISO date `20\d\d-\d\d-\d\d` — 0 in the three artifacts (the date lives in the directory name and in `research/README.md:5-6`)
- year token `\b20\d\d\b` — only `B:64-69`

String loci that matter for "absent from the answer":

| string | A | B | C |
|---|---|---|---|
| `ikigai` | 35 only | none | none |
| `kodawari` | 35 only | none | none |
| `hallucin` / `forgetting` / `drift` | none | 35 only | none |
| `inflation` | none | none | 35 only |
| `self-attest` | none | none | 35 only |
| `appropriat` | none | none | 35 only |
| `citation` | none | 35, 49 | none |
| `labor` / `contract` | 49 only | none | none |
| `kodokan` | none | none | 46 only |
| `primary` | 35 only | none | none |

"35 only" means the user prompt, not the assistant. Line numbers below are logical lines.

## Shared structure

Observation: the three files are the same scrape skeleton with a different chat title and a different answer fragment.

Identical ranges, compared line-for-line:

- lines 1-16 (sidebar chrome through `Recents`)
- lines 18-29 (other recent-chat titles, `Loading chats`, account label, plan badge `Pro`)
- lines 31-33 (`·`, `Work`, `Share`)
- the last 21 lines, starting at the disclaimer: `A:90-110` = `B:81-101` = `C:135-155`

The only header differences are the chat title, duplicated at line 17 (recents row) and line 30 (header):

- A: `Shokunin Mastery Tradition Research`
- B: `Research agent knowledge bases`
- C: `Agent Maturity Naming Research`

Session chrome, shape only, not transcribed: lines 9-26 are pinned/recent titles of other chats; line 28 is an account display name; line 29 is a plan badge. No secret values were copied into this report.

Rejected reading: the footer word `Sources` is not a bibliography. Reason: it is one label inside a 21-line composer chrome that is byte-identical across three different answers, sitting with `GPT-6 Astra`, effort-picker tokens (`Light` through `Ultra`), `Outputs`, `Create file or site`, and `Web search` (`A:96-110`, `B:87-101`, `C:141-155`).

### Region map (same roles, different line numbers)

| role | A | B | C |
|---|---|---|---|
| shell chrome | 1-33 | 1-33 | 1-33 |
| user-turn label | 34 `You said:` | 34 | 34 |
| declared question (one physical line) | 35 | 35 | 35 |
| dual timers | 36 `Worked for 1m 33s`; 37 `Working for 2m 9s` | 36 `1m 36s`; 37 `2m 8s` | 36 `1m 11s`; 37 `2m 7s` |
| assistant turn 1, plan sentence | 38-40 | 38-40 | 38-40 |
| search marker, no query text | 42 `Searched the web` | 42 | 42, and a second round at 55 |
| assistant turn 2 | 44-47; line 45 is the chrome token `Response started` | 44-47; 45 `Response started` | 50-53; 51 `Response started` |
| tool-status label, not a query and not a source | 49 `Investigating Historical Labor Obligations and Contracts` | 49 `Analyzing AI Citation Errors and Persistent Memory` | none of this shape |
| answer fragment | 50-88 | 53-79 | 63-133 |
| disclaimer + composer chrome | 90-110 | 81-101 | 135-155 |

No file contains a markdown heading, front matter, or a field labelled question / method / finding / source / limit / revision. The question is not a record field. It is one user-turn sentence fused with a design brief ("I am building...").

Each answer fragment ends on a grammatically complete sentence, then a blank line, then the shared disclaimer. There is no closing marker: no references block, no summary, no completed numbered list matching the prompt.

Inference, not observation: the dual timers (`Worked for` and `Working for` on consecutive lines in every file) are consistent with a capture that included in-progress UI state. They do not prove the live generation later continued, and they do not prove it stopped. Unknown whether a longer answer existed in the tab.

Inference: `+N` lines and C's `\u206810\u2069 more` chips are collapsed UI overflows, not authored citation syntax. C:48 and C:61 wrap the digits in U+2068 FIRST STRONG ISOLATE and U+2069 POP DIRECTIONAL ISOLATE. A and B's `+N` chips were scraped as plain text. Same widget family, inconsistent serialization. That is evidence of a DOM text scrape. It is not evidence of what the hidden cards said.

### Citation-binding pattern the scrape preserved

The only join between a claim and a source token is adjacency. No footnote, no bracket, no per-row source column. Several sentences that precede a chip end in a trailing space (scrape seam): `A:67`, `A:71`, `A:82`, `B:71`, `C:81`, `C:89`, `C:92`, `C:97`, `C:99`, `C:102`, `C:120`, `C:130`. Paragraphs with neither a seam nor a following chip have no citation token in the file: `A:88`, `B:79`, `C:133`. Unknown whether a card existed below the fold.

Tables are tab-separated UI dumps, not markdown tables (zero `|`). None has a source column. A chip after a table cites the table as a lump, not a row.

Chip-count vs named-item count, observation only:

- A:80-82 names three examples; A:83 is one host; A:84 is `+2`. 1+2=3. That cardinality matches. It does not identify the two hidden cards, and it does not prove the host is one of the three.
- B:64-69 is six works; B:72 is one host; B:73 is `+6`. 1+6=7, which does not equal 6. The overflow count is not "one card per row."
- C:81 names two dictionaries; C:82-83 is `コトバンク` plus `+5`. The overflow exceeds the named works.

### What none of the three contains

Recorded so the per-artifact sections do not repeat the sweep.

- A URL with a scheme, a path, a DOI, an arXiv id, an ISBN, a page, a footnote, or a local `path:line`.
- A quoted source passage. Japanese spans are headwords in glossary rows (`A:61-65`, `C:74-79`, `C:114-118`), not attributed dictionary quotations. Scare quotes are the assistant's own phrases (`A:52`, `B:79`, `C:85`, `C:102`, `C:109`).
- A ranked source list. No row is marked primary, secondary, aggregator, or unsourced. The word `primary` occurs only in A's prompt (`A:35`, "primary-ish").
- An observation / inference / unknown partition. The word `observation` occurs as glossary or topic prose (`A:61`, `B:77`, `C:74`), not as an epistemic label. `inference`, `unknown`, and `proposal` do not occur as labels. B:59 announces a distinction ("published findings" vs "my proposed engineering rules") but the captured span after that line does not contain a separated proposal section.
- A negative-claim sweep as a record. "I haven't found" / "I could not" / "I found no" appear as prose (`A:47`, `A:64`, `C:53`, `C:109`) without the query list that would make the sweep replayable, except the partial query strings in C noted below.
- The harvest metadata. Date, operator, browser port, search counts, and the pipeline retraction live only in `research/README.md:3-8`. The artifacts do not say which pipeline ran.
- A revision pin inside the file. The pin above is external (git). The directory name `deep-research-2026-09-28` is the only in-tree date, and it is not inside the file bytes.

Three-layer identity, observation:

1. Directory name asserts date and a deep-research genre.
2. Index `research/README.md:7-8` retracts the genre: "the burner account has NO Deep Research entitlement — these are browse-enabled GPT-6-Astra responses (9/8/10 web searches each), not the Deep Research pipeline."
3. Artifact bytes show a chat shell, the user words `Deep research:` at line 35 of each, the footer model string `GPT-6 Astra` (space, not the index's hyphen), and `Searched the web` markers. They neither confirm nor deny the entitlement claim.

Rejected reading: treating README's `9/8/10` as the artifacts' search logs. Reason: those integers are not in the artifact bodies as search counts. A and B serialize one `Searched the web` and zero query strings. C serializes two markers, four query lines, and two `10 more` chips. `10 more` is an overflow, not a count of ten searches. Whether the index counts match the live session is unknown. Not checked.

## A — `research/deep-research-2026-09-28/A-shokunin-tradition.md`

### Question

Declared, but only as the user turn at `A:35`, fused with a roster-design brief. The assistant never restates it as a question field. Turn 1 (`A:40`) is a plan: "I'll check the terminology against Japanese sources, then separate documented artisan practices from useful analogies for your agent roster." That is method intent, not a question.

Parts of the declared question, and where they are in the assistant span `A:36-89`:

| part of `A:35` | in the answer fragment | status |
|---|---|---|
| minarai / deshi / shokunin / jin'i-ryu / kiwami semantics | table `A:60-65`; correction `A:47` | glossary present; not entry-cited |
| shokunin kishitsu ethics | reading corrected to katagi at `A:47` and `A:71` | disposition gloss, not an ethics treatment |
| ikigai relationship | no assistant hit | absent |
| kodawari | no assistant hit | absent |
| (1) when an apprentice earns domain independence | heading `A:74`; examples `A:80-82`; museum paragraph `A:88` | opened, not closed |
| (2) whether a master ever finishes | thesis sentence `A:52` ("lifelong refinement") before any chip; plan `A:47` still "checking" continued learning | no section `2.`; not a sourced answer |
| (3) obligation to teach vs hoard | `transmission` in the plan `A:47` and the design axes `A:54` | no section `3.`; no sourced treatment |
| (4) public evidence of narrow mastery | no assistant section | absent |
| "Cite primary-ish sources" | prose priority at `A:56` ("practitioners, workshop accounts, craft associations, museums, and Japanese cultural institutions") | a source-class sentence, not a ranked list, and not carried into rows |

The only numbered section heading in the file is `A:74` (`1. When does an apprentice earn domain independence?`). No `2.` / `3.` / `4.`.

`A:52-54` places a design recommendation ("For your design, keep four axes separate") before any citation chip. Finding and application share a paragraph.

### How sources are cited

| line | token | class | resolvable from this file |
|---|---|---|---|
| 67 | `Daijisen`, `Nihon Kokugo Daijiten`, `Japan Kanji Aptitude Testing Foundation’s Kanjipedia` | work titles, no edition, headword, or entry | no |
| 68 | `コトバンク` | aggregator chip; does not say which entry or which of the three named works | no |
| 69 | `+3` | collapsed count; identities absent | no |
| 71-72 | katagi paragraph, then `コトバンク` | same aggregator chip, no `+N`, still no entry | no |
| 80 | "Adachi’s own account" | prose pointer; no title, path, or date | no |
| 81 | "Taitō City interview, Ishii Torao" | person + institution; no date, interviewer, or URL | no |
| 82 | "Echigo Yoita forged-blade association" | institution; no document | no |
| 83 | `adachi-hanga.com` | bare registrable domain, no scheme, no path | no |
| 84 | `+2` | collapsed count | no |
| 88 | Takenaka Carpentry Tools Museum / Ogawa Mitsuo / Nishioka Tsunekazu | prose pointer; no chip after it | no |

`A:56` says the evidence prioritizes practitioners, workshops, associations, museums, and cultural institutions, and that these "establish particular traditions and modern institutions—not a single timeless code." That is a scope caveat in prose. It is not a per-source rank, and the institutions named later are not joined back to those classes by anything but reading order.

Negative claims inside A, and the sweep the file itself records:

- `A:47` "I haven’t found evidence that jin’i-ryū is a traditional artisan rank." No query text is in the file. The sweep is not replayable from the artifact.
- `A:64` "I could not substantiate this spelling as an established artisan rank in the Japanese or English sources searched." The sources searched are not listed.
- `A:52` "They do not establish a universal ladder of minarai → deshi → shokunin → jin’i-ryū → kiwami." This is a positive structural claim about absence of a ladder. Its support in the file is the glossary table plus the unswept negative at `A:47` and `A:64`.

Tool trace is not joined to the answer. `A:49` is the only line containing `labor` or `contract`. The answer uses `nenki-ake` at `A:78` and calls apprenticeship "an economic and social institution" at `A:86`, but it never cites a labor-contract document, and the status label has no query and no chip.

### What A does not contain

- Sections for prompt questions (2), (3), (4), ikigai, and kodawari.
- Any query string under `Searched the web` (`A:42`).
- A citation token on the museum paragraph (`A:88`), which is the last sentence of the answer.
- A year, a date, or the string `primary` outside the prompt.
- The index's corrections as an index. `research/README.md:11-14` restates katagi, the coined-rank warning, and the four axes without a `path:line` into A. Those sentences' only local source is this unverified transcript. Noted as an index defect, not re-litigated here.

## B — `research/deep-research-2026-09-28/B-multiagent-knowledge.md`

### Question

Declared only at `B:35`, fused with a fleet-design brief. Three numbered demands plus "Cite papers." The assistant does not restate them as a question field. `B:40` is a plan covering "persistent memory, self-improving agents, specialist routing, and multi-agent credit assignment."

| part of `B:35` | in the answer fragment | status |
|---|---|---|
| (1) self-rewrite failure modes, naming drift, forgetting, hallucinated citations | `B:77-79` opens a different failure: losing the observation / interpretation / knowledge distinction; ACE "brevity bias" and "context collapse," with token and accuracy figures | those three named modes are absent from the assistant (35 only). One other failure is started |
| (2) split a domain vs expand one | thesis `B:55` ("much weaker support for unrestricted whole-corpus rewriting or automatic creation of specialists based on topic novelty alone"); `B:75` says neural expert-expansion results "do not directly validate rules for splitting Markdown corpora" | no section `(2)`; no chip on `B:75`; plan `B:47` says this is still being checked |
| (3) credit assignment for which agent gets better | interim sentence `B:47` ("team success does not establish which specialist actually improved"); design sentence `B:57` | no section `(3)`; no paper pointer on that sentence; `B:47` says counterfactual evaluation is still being checked |
| Cite papers | table `B:64-69` | author-year plus short title, not a paper identifier |

`B:59` says "Below, I distinguish published findings from my proposed engineering rules." The captured text after that line is the table (`B:63-69`), a MoE distinction (`B:75`), and the start of failure (1) (`B:77-79`). The announced proposal block is not in the file. `B:57` ("The strongest design implication...") actually sits above the announcement.

`B:55` and `B:59` also limit scope in prose: recent preprints' benchmark results "do not establish indefinite, reliable self-improvement." That limit is not attached to a locator.

### How sources are cited

| line | token | class | resolvable from this file |
|---|---|---|---|
| 51 | `arxiv.org` | bare host in the tool-trace region, between status `B:49` and the next `ChatGPT said:` at `B:53`. No id. Not in the answer body | no |
| 64 | `Voyager, Wang et al., 2023` | short title + author-year | no — search key, uniqueness not tested |
| 65 | `Generative Agents, Park et al., 2023` | same | no |
| 66 | `Reflexion, Shinn et al., 2023` | same | no |
| 67 | `Dynamic Cheatsheet, Suzgun et al., 2025; ACE, Zhang et al., 2025` | same; `ACE` is not expanded in the file | no |
| 68 | `Memento-Skills, Zhou et al., 2026` | same | no |
| 69 | `LEGOMem, Han et al., 2025` | same | no |
| 71 | `Sources: Voyager and Generative Agents; Reflexion; Dynamic Cheatsheet and ACE; Memento-Skills; LEGOMem.` | renames the table; adds no identifier. Trailing space | no |
| 72 | `arxiv.org` | bare host under the Sources line | no |
| 73 | `+6` | collapsed count; does not match the six rows (see shared section) | no |
| 79 | `18,282` tokens, `122` tokens, accuracy `66.7` / `57.1` / `63.7`, "one AppWorld case" | quantitative claim; no chip between this paragraph and the disclaimer `B:81` | no locator on the paragraph. ACE was named earlier in the table, which is not a join |

The table columns are `Work`, `What persists or improves`, `Relevance to shokunin` (`B:63`). The third column is design application, not a source locator. `B:75` (weight-space MoE vs LLM ensembles vs memory-owning agents) has no chip.

The prompt's citation-failure topic is not taken up. `citation` occurs at `B:35` (user: "hallucinated citations") and `B:49` (status label "Analyzing AI Citation Errors and Persistent Memory"). The answer body never uses the word. The `arxiv.org` chip at `B:51` cannot be read as the paper that status label analyzed: it has no id.

### What B does not contain

- Assistant text for drift, forgetting, or hallucinated citations.
- A sourced answer to split-vs-expand or to credit assignment.
- Any query string under `Searched the web` (`B:42`).
- A title-as-published, venue, DOI, or arXiv id for any row.
- The "proposed engineering rules" section announced at `B:59`.
- A citation token on the only quantitative paragraph (`B:79`).

## C — `research/deep-research-2026-09-28/C-rank-taxonomy.md`

### Question

Declared only at `C:35`, fused with a naming-scheme brief. Demands: map Japanese craft/martial terms onto four agent states (minted-untested, verified corpus, safe self-iteration, mint siblings); appropriation errors; failure modes of rank systems on self-certifying agents, naming rank inflation and self-attestation; cite sources. The jin'i-ryu gloss "self-legislating school" is inside the same line.

The assistant does not restate this as a question field. `C:40` is a plan. `C:53` is an interim thesis, not a question.

| part of `C:35` | in the answer fragment | status |
|---|---|---|
| states (a) minted untested, (b) verified corpus, (c) safe self-iteration, (d) mint siblings | recommendation `C:69` (`Initiate → Grounded → Maintainer → Agentwright`, and a Japanese adaptation in the same sentence); table `C:73-79` maps terms onto (a) and (d) and rejects corpus-alone and self-modification readings | naming recommendation is present and labelled "My recommended" (`C:69`); the operational names are not sourced |
| terms map cleanly | glossary `C:73-79` and lexical table `C:113-118`; axes named at `C:67` | glosses present; "cleanly" is the assistant's fit column, not a sourced cultural finding |
| appropriation errors | the string `appropriat` is 35 only. `C:85` warns against presenting an invented ordering as an inherited institution | related caveat, no appropriation source |
| rank inflation | 35 only | absent from the assistant |
| self-attestation | string `self-attest` is 35 only. `C:40` plans to examine "self-certification." `C:92` says martial rank "is conferred through a procedure, not established by a practitioner’s self-description" | adjacent analogy, not a treatment of self-certifying agents, and not a headed failure-mode section |
| jin'i-ryu as "self-legislating school" | denied at `C:53` and `C:109-126` | treated; sweep only partly in the file |
| Cite sources | chips listed below | not resolvable |

`C:65-69` (recommendation, including "keep certification and permissions separate from the names") precedes the sourced glossary at `C:71`. Same finding/application mix as A and B, with an explicit "recommended" label the others lack.

C is the only file with a partial method trace, and the trace is still not a log:

- Search round 1: marker `C:42`; query lines `C:44` and `C:46`; overflow `C:48`.
- Interim `C:53`.
- Search round 2: marker `C:55`; quoted queries `C:57` and `C:59`; overflow `C:61`.

`C:44` bytes begin `site.nihonkiin.or.jp` (`73 69 74 65 2e 6e` — period, not colon). `C:46` is `site.kodokanjudoinstitute.org dan kyu history ranks`, also with a period. Observation: the export does not contain a `site:` operator. Inference that a colon was dropped is not established. Unknown whether these lines were queries, visited hosts, or both.

The kodokan query does not reappear. `kodokan` is `C:46` only. Judo content in the answer is `C:102-103` (Todo and Murata, chip `jstage.jst.go.jp`), not that host. The search trace and the citation are not joined. Nihon Ki-in is queried as `site.nihonkiin.or.jp` (`C:44`) and later cited as different hosts `archive.nihonkiin.or.jp` (`C:90`) and `nihonkiin.or.jp` (`C:100`). Related strings, not a resolved hop.

### How sources are cited

| line | token | class | resolvable from this file |
|---|---|---|---|
| 44, 46 | `site.nihonkiin.or.jp ...`, `site.kodokanjudoinstitute.org ...` | search-trace lines, not bibliography | not a citation |
| 48, 61 | U+2068 `10` U+2069 ` more` | collapsed search-trace overflow | identities absent |
| 57, 59 | `"自己立法" "自律"`; `"jin'i-ryu"` | quoted query strings in round 2 | not a citation; partial sweep record for the negative at `C:109` |
| 81 | `Shōgakukan’s Digital Daijisen`, `Nihon Kokugo Daijiten` | work titles, no headword | no |
| 82-83 | `コトバンク` / `+5` | aggregator chip + overflow larger than the two named works | no |
| 90 | `archive.nihonkiin.or.jp` | bare host after the Go paragraph `C:89` | no |
| 93 | `JKA 公益社団法人日本空手協会` | organization display name after `C:92`; no host | no |
| 98 | `old2.kendo.or.jp` | bare host after `C:97` | no |
| 100 | `nihonkiin.or.jp` | bare host after `C:99` | no |
| 102-103 | `Yoshiaki Todo and Naoki Murata`; chip `jstage.jst.go.jp` | personal names, no year, no title; host is a platform | no |
| 120-122 | dictionaries + "Japanese philosophical scholarship"; chip `コトバンク` / `+4` | two source classes, one aggregator, four unnamed cards | no |
| 130-131 | shu-ha-ri paragraph; chip `コトバンク` | aggregator chip, no entry | no |
| 133 | menkyo kaiden paragraph | no chip before disclaimer `C:135` | no token |

`C:87-105` is the longest sourced-looking stretch in the harvest. It is still host-level. `archive.nihonkiin.or.jp` does not say which archived page. `jstage.jst.go.jp` does not say which article. A platform host is not a document.

Negative claims and the sweep the file records:

- `C:53` and `C:109` deny an authoritative attestation of jin'i-ryu as "self-legislating school." The only recorded queries that could be that sweep are `C:57` and `C:59`, plus an unnamed `10 more` at `C:61`. That is a fragment, not a complete sweep: the other ten-plus queries are absent, and `C:57` is two quoted strings with no engine, date, or result count.
- `C:81` "overlapping definitions do not establish a universal shokunin → takumi → meishō hierarchy." Support in the file is the dictionary-title sentence plus the kotobank chip. The entries are not in the file, so the negative is not checkable from the file.
- Rank inflation is not given even an unswept "I haven't found." It is simply absent from the assistant.

### What C does not contain

- Any assistant occurrence of `inflation`, `self-attest`, or `appropriat`.
- A failure-mode section for self-certifying agents.
- A scheme or path on any host.
- A year.
- A source for the recommended operational names at `C:69`.
- A chip on the closing menkyo-kaiden paragraph (`C:133`).
- A join from the kodokan search line to an answer citation.

C contains more of its prompt than A or B do. That is a coverage difference inside the scrape, not evidence the live answer was finished. The failure-mode half of the question is missing either way.

## Index layer — `research/README.md`

Not one of the three artifacts. It is the only framing record, and it is 17 logical lines (trailing newline, so `wc -l` matches).

- `research/README.md:3` calls the directory "External research harvested by the operator surface, indexed by date dir."
- `research/README.md:6` is the harvest circumstance (burner Chrome, CDP port, date, L0). `research/README.md:7-8` is the pipeline retraction and the `9/8/10` search-count claim, discussed above.
- `research/README.md:10-17` is a three-bullet abstract. The A bullet (`:10-14`) promotes transcript conclusions (katagi, jin'i-ryu as coined, four axes) to "Corrections for our scheme" with no `path:line` and no unresolved-citation mark. The B bullet (`:15`) is a topic label only. The C bullet (`:16-17`) is a topic label that names "rank-inflation failure modes" — a subject the C artifact's assistant span does not contain.

The index does not contain a question field, a source list, or a revision hash either. It adds harvest context the artifacts lack, and it adds claims the artifacts' citation form cannot carry.

## Unknowns

- What the collapsed cards contained (`+3`, `+2`, `+6`, `+5`, `+4`, and both `10 more` chips). Not in the files. Not fetched.
- Whether generation continued after the captured sentence. Bodies end on complete sentences; timers are dual. Both readings stay open.
- Whether README's search counts and entitlement note match the session. The artifacts cannot confirm them. This report did not open the browser port named at `research/README.md:6`.
- Whether any search key (author-year, person, institution, dictionary title) denotes one publicly findable document. Not tested. Memory was not used to supply ids.
- Whether paragraphs `A:88`, `B:79`, and `C:133` were uncited in the live UI or merely uncaptured. The file has no token there.

## External window — not taken, and not yet specifiable

Proposal, not an admitted rule. A future approval table cannot list the URLs to verify, because the files do not contain those URLs. Fetching a bare host root (`arxiv.org`, `adachi-hanga.com`, `jstage.jst.go.jp`, `コトバンク`) would not recover the cited page. Searching the short titles would be a new research act, not a check of a locator these artifacts already give.

What would have to be recovered first, from a session re-export or an operator-supplied sources panel, before any external check is even a check:

| missing locator class | where the gap is | why a fetch of the visible token is not verification |
|---|---|---|
| collapsed source cards | `A:69`, `A:84`, `B:73`, `C:83`, `C:122` | identities absent |
| collapsed search overflow | `C:48`, `C:61` | queries absent |
| bare host | `A:83`, `B:51`, `B:72`, `C:90`, `C:98`, `C:100`, `C:103` | no path |
| org display name | `C:93` | no host |
| dictionary headword | `A:67-72`, `C:81-83`, `C:120-122`, `C:131` | work or aggregator named, entry not |
| author-year search key | `B:64-69` | no id; uniqueness untested |
| prose pointer | `A:80-82`, `A:88`, `C:102` | no document title |

No row here is approved. No row was fetched. Recovering a live CDP session would itself be external live-target work and is out of this round.

## Rejected readings

- Footer `Sources` / `Web search` are bibliographies. Rejected: identical composer chrome. See shared structure.
- README `9/8/10` is the artifacts' search log. Rejected: not in the artifact bytes.
- Author-year rows are resolved paper citations. Rejected: no identifier; not tested against a local or fetched document.
- "I haven't found" is a recorded negative sweep. Rejected except as a partial trace at `C:57` and `C:59`, which still omit the overflow queries and any result list.
- A grammatically complete last sentence means the answer answered the prompt. Rejected: A's only numbered section is `1.`; B never opens `(2)` or `(3)`; C never opens rank inflation.
- These files fail `claim-ledger.sh` or `anchorcheck.py`. Rejected as a category error: those gates look for path tokens these files do not use. The accurate statement is that the files contain zero tokens in that vocabulary.
- The claims are false because the citations are unverified. Rejected: unverified is the state. False was not shown. True was not shown.
