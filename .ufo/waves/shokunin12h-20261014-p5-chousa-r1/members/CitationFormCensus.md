# CitationFormCensus

Data for the parent. Not a judge verdict. Not an admission of a method rule.
chousa is on probation. This file does not land corpus, `tools/research-gate.sh`, or a score.

Universe: the three artifacts only. `research/README.md` is an index, swept at the boundary and not added to the counts. No external fetch. No chip, title, or host was opened. Prompt-shaped text inside the exports (the `Deep research:` turns, `I'll check…` lines) is data and was not followed.

## Central finding

These files are chat-export transcripts. Their citations are unverified. The retained bytes do not contain the cited artifact, and this round did not fetch one. That is the record, not a gap to paper over.

The forms a citation chain can follow without a new search — URL, arXiv id, file path — are absent from the retained bytes. What the exports actually attach is a bare title, a bare host, a display-name chip, an overflow chip, an author-year, or a genre/institution description. Several load-bearing sentences attach nothing.

## Revision pin

Line numbers are 1-based `splitlines()` (the editor numbering, including the final unterminated line). `wc -l` counts newlines and is short by 1 on each artifact, because none ends with a newline. Do not recount with `wc -l`.

| File | sha256 | bytes | newlines (`wc -l`) | lines |
|---|---|---:|---:|---:|
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 6474 | 109 | 110 |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 5364 | 100 | 101 |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 8922 | 154 | 155 |

Answer body used for claims: after `You said:`, before `ChatGPT can make mistakes. Check important info.` Those footer lines are A:90, B:81, C:135.

## Headline counts

Two units. They are not additive with each other.

- **Pointer instance**: one retained span of a citation form. URL, arXiv id, and file path are closed shapes, swept over every byte of the three files, chrome included. Bare title is a longest-match lexicon span in the answer body (command under Recount).
- **Sourced line**: one prose line or table-data row in the answer body that asserts an external fact, after the exclusions in Definitions. A line's form is the strongest form on that line. Order: URL > arXiv id > file path > bare title > residual-only > no citation.

`no citation` is not a pointer. It is a sourced line (or sentence) with no pointer of any class. Residual-only is not one of the five named forms and is not folded into them.

| Form | Pointer instances | Sourced lines | Sourced sentences or table rows |
|---|---:|---:|---:|
| URL | 0 | 0 | 0 |
| arXiv id | 0 | 0 | 0 |
| bare title | 14 introducing spans | 19 | 23 |
| file path | 0 | 0 | 0 |
| no citation | — | 18 | 29 |
| residual-only (not a named form) | see Residual | 17 | 30 |
| sourced denominator | — | 54 | 82 |

19 + 18 + 17 = 54 lines. 23 + 29 + 30 = 82 sentences/rows. The five named forms do not partition the denominator. The missing piece is residual-only.

Per file, sourced lines:

| File | sourced lines | URL | arXiv id | bare title | file path | no citation | residual-only |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 18 | 0 | 0 | 5 | 0 | 8 | 5 |
| B | 12 | 0 | 0 | 7 | 0 | 5 | 0 |
| C | 24 | 0 | 0 | 7 | 0 | 5 | 12 |
| total | 54 | 0 | 0 | 19 | 0 | 18 | 17 |

Per file, sourced sentences or table rows:

| File | n | bare title | no citation | residual-only |
|---|---:|---:|---:|---:|
| A | 27 | 5 | 12 | 10 |
| B | 18 | 10 | 8 | 0 |
| C | 37 | 8 | 9 | 20 |
| total | 82 | 23 | 29 | 30 |

Hop-ready locators (URL or arXiv id or file path) that a later reader can open without a new search: **0** pointer instances, **0** sourced lines. That is the chaining baseline.

Bare-title spans are not 19. Fourteen introducing spans sit on 9 lines. Ten further bare-title lines are table rows that do not contain a title string; they inherit the next attribution sentence. 9 + 10 = 19. See Inheritance.

## Definitions

**URL.** A scheme-bearing `http://` or `https://` token, a markdown `](…)` target, an HTML `href`, or a `www.` token. A bare hostname is not a URL. Rejected promotion: `adachi-hanga.com` and `arxiv.org` have no scheme and no path.

**arXiv id.** `arXiv:` plus `YYYY.NNNNN`, `arxiv.org/abs|pdf|html/` plus that id, an old-style archive id (`hep-th/9901001` and the sibling archives), or a bare `YYYY.NNNNN` / `vN` token. The string `arxiv.org` alone is not an id. A year (`2023`) is not an id.

**File path.** A backtick span, a `path:line` token, a `corpus/` or `research/` or `./` relative path, a fleet URI (`local://`, `artifact://`, `agent://`, `proc://`, `skill://`), or a token ending in `.md` / `.py` / `.sh` / `.tsv` / `.json` / `.mjs`. A hostname is not a path. This is the shape `kagi-shokunin/corpus/claim-ledger.sh:31-46` and `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-7` already know how to check. It does not occur in the three artifacts.

**Bare title.** A work, paper, or dictionary name with no URL, arXiv id, or file path on that span. Locked lexicon, longest match first, so `Shōgakukan’s Digital Daijisen` is not also counted as `Daijisen`, and `Japan Kanji Aptitude Testing Foundation’s Kanjipedia` is not also counted as `Kanjipedia`. Apostrophes are U+2019 as stored. A `Sources:` line that repeats the table's titles is a restatement, counted separately, not added to the 14.

**No citation.** A sourced line whose block contains none of: URL, arXiv id, file path, bare title, bare host, display-name chip, overflow chip, author-year, bare attribution, or anaphora (`The dictionaries`). Forward inheritance is not applied. A later paragraph that names ACE does not cite an earlier sentence that does not.

**Residual-only.** A sourced line whose only pointers are outside the five named forms. Reported beside them. Folding it into `no citation` is rejected: a pointer is present, and calling it absent would hide the broken hop. Folding a bare host into URL is rejected: the file does not contain a URL.

**Sourced line, included.** A prose sentence, or one table-data row, in the answer body, that asserts a tradition, a wording, a number, a paper result, or an absence. Table unit is the row, not each cell. The relevance column of B's table is not split into extra no-citation claims: it is the assistant's mapping, not a second sourced finding. Reason kept: splitting it would manufacture no-citation counts from a column the export does not present as a cited result.

**Excluded from the denominator** (kept, not dropped):

| Kind | n | Lines |
|---|---:|---|
| process narration | 5 | A:40, A:47 (`I’m checking…`), B:40, B:47 (`I’m checking…`), C:40 |
| meta | 5 | A:56 first sentence, A:58, B:59 first sentence, B:61, C:53 first sentence |
| recommendation | 20 | A:52 first, A:54 first, B:57 both, C:65 first, C:67 both, C:69 both, C:85 first two, C:99 last, C:102 last, C:105 both, C:124 both, C:126 both, C:130 last |
| commentary on an adjacent pointer | 5 | A:86 first, A:88 last, B:79 `This is a case study…`, C:89 last, C:97 last |
| restatement label | 1 | B:71 `Sources: …` |

Headings and the prompt-question line are not claims. They are labels. Two of them assert a fact that the next prose restates, so the assertion is not lost: C:87 is restated by C:89; C:107 is restated by C:109. Other headings: A:49, B:49 (process-step titles), A:74 (question), C:71, C:95, C:111, C:128.

**Block attachment.** Chips and titles in a blank-delimited block apply to every sourced sentence in that block. Exception: a table row that says the assistant `could not substantiate` / `haven’t found` / `found no` does not inherit a following positive attribution. A:64 is that row.

**Table inheritance.** If the next block's prose says `come from` or `The dictionaries support`, gloss rows inherit that block's form. Donors: A:67, C:81, C:120. This is textual, not a guess: A:67 says the lexical distinctions come from the named dictionaries; C:81 says these meanings come from the named dictionaries; C:120 says the dictionaries support those distinctions. The negative row A:64 does not inherit.

## Closed-shape sweep

Command, run from the fleet root against `research/deep-research-2026-09-28` only. `rg` exits 1 when there is no match; empty output below is the zero, not a skipped sweep.

```
rg -n --pcre2 -e 'https?://' -e '\]\([^)]+\)' -e 'href\s*=' -e '\bwww\.' research/deep-research-2026-09-28
rg -n --pcre2 -e 'ar[Xx]iv:\s*[0-9]{4}\.[0-9]{4,5}' -e 'arxiv\.org/(abs|pdf|html)/' -e '(?<![0-9])[0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?(?![0-9])' research/deep-research-2026-09-28
rg -n --pcre2 -e '10\.[0-9]{4,9}/' research/deep-research-2026-09-28
rg -n --pcre2 -e '`[^`]+`' -e '[A-Za-z0-9_./-]+\.(md|py|sh|tsv|json|mjs):[0-9]+' -e '(local|artifact|agent|proc|skill)://' research/deep-research-2026-09-28
```

Observed output: no lines. Counts: URL 0, arXiv id 0, bare `YYYY.NNNNN` 0, DOI 0, backtick span 0, `path:line` 0, fleet URI 0.

Same sweep also found the residual shapes that the five-form patterns correctly did not match:

```
rg -n --pcre2 -e '^[a-z0-9][a-z0-9.-]*\.[a-z]{2,}$' research/deep-research-2026-09-28
```

7 host lines: A:83 `adachi-hanga.com`, B:51 `arxiv.org`, B:72 `arxiv.org`, C:90 `archive.nihonkiin.or.jp`, C:98 `old2.kendo.or.jp`, C:100 `nihonkiin.or.jp`, C:103 `jstage.jst.go.jp`.

```
rg -n --pcre2 -e '^\+[0-9]+$' research/deep-research-2026-09-28
```

5 overflow lines: A:69 `+3`, A:84 `+2`, B:73 `+6`, C:83 `+5`, C:122 `+4`. Sum of the integers is 20. That sum is chip text, not a count of sources. The omitted targets are not in the file.

```
rg -n 'コトバンク' research/deep-research-2026-09-28
```

5 display-name lines: A:68, A:72, C:82, C:121, C:131. A sixth display chip is not that string: C:93 `JKA 公益社団法人日本空手協会`.

```
rg -n 'et al\.' research/deep-research-2026-09-28
```

6 lines, 7 instances. B:67 contains two (`Suzgun et al., 2025` and `Zhang et al., 2025`). The other five are B:64, B:65, B:66, B:68, B:69. A word-boundary false friend, `retrieved` at B:65, is the verb in `reflections retrieved for planning`, not a citation. Not counted.

## Bare-title pointer ledger

Introducing spans (the 14). Restatements on B:71 are listed after and are not in the 14.

| Span | Title |
|---|---|
| A:67 | Daijisen |
| A:67 | Nihon Kokugo Daijiten |
| A:67 | Japan Kanji Aptitude Testing Foundation’s Kanjipedia |
| B:64 | Voyager |
| B:65 | Generative Agents |
| B:66 | Reflexion |
| B:67 | Dynamic Cheatsheet |
| B:67 | ACE |
| B:68 | Memento-Skills |
| B:69 | LEGOMem |
| B:79 | ACE |
| B:79 | ACE |
| C:81 | Shōgakukan’s Digital Daijisen |
| C:81 | Nihon Kokugo Daijiten |

Distinct matched strings: 11. Short aliases `Digital Daijisen` and `Kanjipedia` did not fire as extra spans; the longer phrase consumed them. `Daijisen` (A:67) and `Shōgakukan’s Digital Daijisen` (C:81) are not collapsed. Whether they are the same work is unknown.

B:71 restates all seven work names (`Voyager`, `Generative Agents`, `Reflexion`, `Dynamic Cheatsheet`, `ACE`, `Memento-Skills`, `LEGOMem`). Seven spans, flag `restatement`. Excluded from the 14 because they repeat the table they sit under, and the chips B:72–73 sit on that label rather than introducing a new work. Reason kept: adding them would double-count one cluster.

## Claim-line ledger

54 sourced lines. `how` is where the form came from. Inherited rows do not themselves contain the title string.

### bare title (19)

| Line | How |
|---|---|
| A:61 | inherit A:67 |
| A:62 | inherit A:67 |
| A:63 | inherit A:67 |
| A:65 | inherit A:67 |
| A:67 | in line: three dictionary titles, plus display chip A:68 and overflow A:69. Bare title wins over the chip. |
| B:64 | in row: Voyager, Wang et al., 2023 |
| B:65 | in row: Generative Agents, Park et al., 2023 |
| B:66 | in row: Reflexion, Shinn et al., 2023 |
| B:67 | in row: Dynamic Cheatsheet; ACE. Two titles, two author-years. One line. |
| B:68 | in row: Memento-Skills, Zhou et al., 2026 |
| B:69 | in row: LEGOMem, Han et al., 2025 |
| B:79 | in line: ACE twice. Four sourced sentences on the line inherit that title. The case-study caveat on the same line is commentary and is excluded. |
| C:74 | inherit C:81 |
| C:75 | inherit C:81 |
| C:76 | inherit C:81 |
| C:77 | inherit C:81 |
| C:78 | inherit C:81 |
| C:79 | inherit C:81 |
| C:81 | in line: two dictionary titles, plus display chip C:82 and overflow C:83. Bare title wins. |

### no citation (18)

| Line | What is asserted, and what is absent |
|---|---|
| A:47 | Craft-specific systems rather than a universal ladder; katagi reading; no evidence found that jin’i-ryū is a traditional rank. No title, no chip. `The sources` does not resolve: the search block A:42–43 retains no query. |
| A:52 | Japanese artisan traditions support the offered model; they do not establish minarai → deshi → shokunin → jin’i-ryū → kiwami. No pointer. The first sentence of the line is a recommendation and is excluded. |
| A:54 | An artisan can work independently while still learning. No pointer. The `For your design` sentence is excluded. |
| A:56 | The (unretained) evidence establishes particular traditions, not a timeless code. No pointer. The `evidence below` sentence is meta and is excluded. |
| A:64 | Could not substantiate jin’i-ryū as an artisan rank. Inheritance from A:67 refused. The search that would be the sweep is not in the file. |
| A:76 | Finishing an apprenticeship, becoming competent, and independent practice are distinct events. No pointer. |
| A:78 | Defines nenki-ake and ichininmae; duration depends on the trade. No pointer. The dictionary cite at A:67 is an earlier block and is not inherited forward. |
| A:86 | No universal number of years or common final examination. No pointer. The preceding examples have residual pointers; this sentence does not. The first sentence of the line is commentary and is excluded. |
| B:47 | `Newer work` erases detail when the whole base is rewritten; team success does not show which specialist improved. No title in the paragraph. ACE at B:79 is not inherited forward. |
| B:55 | `The literature supports` the fleet's core and gives weaker support to unrestricted rewriting. No title. |
| B:59 | Recent preprints' benchmark results do not establish indefinite self-improvement. No title. The `Below, I distinguish` sentence is meta and is excluded. |
| B:75 | Weight-space mixture-of-experts, LLM ensembles, and memory-owning agents are different systems; neural-expert results do not validate Markdown-splitting rules. No pointer. |
| B:77 | The important failure is losing observation vs interpretation vs established knowledge. No pointer. The next paragraph names ACE. Not inherited forward. |
| C:53 | Japanese traditions do not collapse skill, teaching authority, and permission into one ladder; shokunin → takumi → meishō is not a standard sequence; no support found for the proposed jin’i-ryū translation. No pointer. The framing sentence is meta and is excluded. |
| C:65 | No traditional four-rank ladder means created → corpus-verified → safely self-improving → agent-producing. No pointer. |
| C:85 | Dictionary accuracy cannot guarantee cultural acceptance. No pointer. The two recommendation sentences on the line are excluded. |
| C:109 | No authoritative attestation that jin’i-ryū means self-legislating school; romanization without kanji cannot establish a literal meaning. No chip. The preceding search block (C:55–62) is query residue, not a citation, and two of its queries are unretained (`10 more`). |
| C:133 | Menkyo kaiden definition and the two negative glosses. No chip after the paragraph. The answer ends at the next line. |

### residual-only (17)

| Line | Pointer that is not one of the five |
|---|---|
| A:71 | display chip A:72 `コトバンク` only. The dictionary titles are in A:67, not here. |
| A:80 | bare attribution `Adachi’s own account`, in a shared trailing cluster with A:83 `adachi-hanga.com` and A:84 `+2`. Which sentence the host belongs to is not stated. Name-match of Adachi to that host is inference and is not used to change the form. |
| A:81 | bare attribution `Taitō City interview`. Same shared cluster. The host does not name this interview. |
| A:82 | bare attribution `Echigo Yoita forged-blade association`. Same shared cluster. |
| A:88 | bare attribution `Takenaka Carpentry Tools Museum’s report`. No chip. The answer stops here. |
| C:89 | bare host C:90 `archive.nihonkiin.or.jp`. |
| C:92 | display chip C:93 `JKA 公益社団法人日本空手協会`. Not a URL. |
| C:97 | bare host C:98 `old2.kendo.or.jp`. Interleaved with C:99–100. Order-attachment (chip follows its sentence) pairs this host with this line. That pairing is layout, labeled inference. Five-form does not change either way: both lines are residual-only. |
| C:99 | bare host C:100 `nihonkiin.or.jp`. Same interleaved block. |
| C:102 | bare attribution `Research by Yoshiaki Todo and Naoki Murata` (names, no year, no title) and bare host C:103 `jstage.jst.go.jp`. |
| C:114 | inherit C:120. Anaphora `The dictionaries`, not a title string. |
| C:115 | inherit C:120 |
| C:116 | inherit C:120. The donor's second clause names `Japanese philosophical scholarship`, a genre, not a work title, for 自己立法. |
| C:117 | inherit C:120 |
| C:118 | inherit C:120 |
| C:120 | anaphora `The dictionaries`; genre `Japanese philosophical scholarship`; display chip C:121; overflow C:122 `+4`. No title string. |
| C:130 | display chip C:131 `コトバンク`. Shu–ha–ri is the term being glossed, not a work title. |

## Residual pointer instances

Not added to the five-form pointer counts.

| Class | n | Where |
|---|---:|---|
| bare host | 7 | A:83, B:51, B:72, C:90, C:98, C:100, C:103 |
| display name | 6 | `コトバンク` ×5 (A:68, A:72, C:82, C:121, C:131); JKA at C:93 |
| overflow chip | 5 | A:69 `+3`, A:84 `+2`, B:73 `+6`, C:83 `+5`, C:122 `+4`. Integer sum 20, not a source count. |
| author-year | 7 | B:64–69, two of them on B:67. Each co-occurs with a bare title, so the line's five-form is bare title. Author-year is not itself a title. |
| bare attribution | 6 | A:80 account, A:81 interview, A:82 association, A:88 report, C:102 `Research by Yoshiaki Todo and Naoki Murata`, C:120 `Japanese philosophical scholarship` |

Orphan and non-claim pointers, so they do not appear in the 54:

- B:51 `arxiv.org` follows the process heading B:49 (`Analyzing AI Citation Errors and Persistent Memory`) and is separated from the next prose by `ChatGPT said:`. It cites no sourced line. It is still a bare host, not an arXiv id.
- B:72 `arxiv.org` and B:73 `+6` sit on the excluded restatement B:71. They do not upgrade B:64–69 to an arXiv id. The table's form stays bare title.

## Rejections

Kept, with the reason. None of these were folded into the headline.

| Rejected move | Reason |
|---|---|
| Call `arxiv.org` an arXiv id | The id pattern requires `arXiv:` or `/abs|pdf|html/` plus `YYYY.NNNNN`, or a bare id token. B:51 and B:72 match none of those. Closed-shape sweep: 0. |
| Call a bare host a URL | No scheme, no path. URL sweep: 0. Guessing `https://` would manufacture a locator the file does not contain. |
| Call `Adachi’s own account`, a city interview, an association, or a museum `report` a bare title | The proper name is a person or institution. `account` / `interview` / `association` / `report` is a genre word, not a document title. No title string is in the file. |
| Call author-year a bare title | `Wang et al., 2023` names no work. It co-occurs with a title and is counted as a residual co-pointer. |
| Call `The dictionaries` a bare title | Anaphora. The titles are in C:81, a different block. Not resolved across blocks. |
| Count `+N` as N sources | The integer is chip text. The targets are not retained. Sum 20 is recorded as text, not as a census of sources. |
| Count search echoes as citations | C:44, C:46, C:57, C:59 are query lines inside `Searched the web` blocks. C:48 and C:61 are `10 more` inside those blocks (Unicode FSI/PDI around `10`), not source-overflow chips. `site.nihonkiin.or.jp` in C:44 is a search operator, not a host chip and not a URL. A:42 and B:42 retain the marker and no query. |
| Count footer `Sources` / `Web search` as a citation | A:109–110, B:100–101, C:154–155 are an unexpanded drawer label. No source list follows. |
| Add `research/README.md` backtick paths to the file-path count | Out of universe. Boundary sweep: 5 backtick spans, of which 3 are index filenames (`A-shokunin-tradition.md` at README:10, `B-multiagent-knowledge.md` at README:15, `C-rank-taxonomy.md` at README:16) and 2 are terms (`shokunin katagi` README:11, `jin'i-ryu` README:12). Not citations in the three artifacts. |
| Forward-inherit ACE from B:79 onto B:47 or B:77 | The earlier sentences do not name ACE. The export does not say they are the same finding. |
| Inherit A:67's dictionaries onto A:71 or A:78 | Different blocks. A:71 has its own chip and does not repeat the titles. |
| Split B's relevance column into no-citation claims | The column is the assistant's mapping. Splitting it would invent uncited claims the export does not separate from the bibliographic row. |
| Treat the sidebar, model picker, or `ChatGPT can make mistakes` line as a citation | Chrome. Outside the answer body. The mistakes lines are A:90, B:81, C:135. |

## Sensitivity

Measured, not hidden.

Dropping table inheritance (titles and chips count only inside the row or sentence that contains them, chips still attaching to the block they sit in) moves:

- A:61, A:62, A:63, A:65 from bare title to no citation (4 lines)
- C:74–C:79 from bare title to no citation (6 lines)
- C:114–C:118 from residual-only to no citation (5 lines)

Headline without inheritance would be bare title 19 − 10 = 9 lines, no citation 18 + 15 = 33 lines, residual-only 17 − 5 = 12 lines. The headline keeps inheritance because the donor sentence explicitly covers the table. The without-inheritance figure is the cost of refusing that reading, not a second baseline.

Sentence vs line: no sourced line mixes no citation with a cited form under block attachment. The sentence counts (29 / 23 / 30) are the same labels split across multi-sentence lines. They do not reveal uncited sentences hiding inside cited lines. One sentence-level disagreement exists and does not move the line unit: C:102's framing sentence (`ancient samurai belts`) has no pointer of its own; the host and the `Research by` phrase are on the rest of the block. Last-sentence attachment would mark that one sentence no citation. The line stays residual-only either way. Headline unit is the line.

## Observation, inference, unknown

**Observation.**

- The three files contain no URL, no arXiv id, no DOI, no file path, no fleet URI, and no backtick span. Sweep above.
- They do contain 14 introducing bare-title spans, 7 restatement spans, 7 bare hosts, 6 display chips, 5 overflow chips, 7 author-years, and 6 bare attributions, at the lines above.
- Of 54 sourced lines, 0 have a hop-ready form, 19 have a bare title as their strongest named form, 18 have no pointer of any class, 17 have only a residual pointer.
- The exports are truncated relative to their own prompts. A's prompt (A:35) asks four questions; the retained answer stops at A:88, inside question 1. B's retained answer stops at B:79, inside the first failure-mode section. C's retained answer runs through C:133 and then the mistakes footer. The Sources drawer is a label only (A:109, B:100, C:154).
- `research/README.md:3-8` describes these as browse-enabled GPT-6-Astra responses, not the Deep Research pipeline, and says 9/8/10 web searches. Retained query lines are A: 0, B: 0, C: 4 explicit plus two `10 more` chips. Those two descriptions of the same events do not match in the retained text.
- The fleet's existing citation gates check path-shaped tokens and `path:NN` anchors (`kagi-shokunin/corpus/claim-ledger.sh:31-46`, `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-7`, `kasegi-shokunin/corpus/knowledge/citation-bases.md:3-4`). Those shapes are absent here. The gates were not executed against these files in this census.

**Inference.** Labeled as such.

- A path-shaped gate run on these three files would have nothing of its checked shape to fail. That would be a vacuous pass, not a walked chain. Not executed; follows from the shape lists, not from a gate log.
- `chousa-shokunin/SKILL.md:19` says a chain follows each hop to the cited artifact and does not stop at a summary of the citation. A bare title, a bare host, and a display chip are summaries. They are not hops. `chousa-shokunin/SKILL.md:43` asks for a resolvable pointer to the artifact and the revision read. None of the 54 sourced lines has one in the retained bytes.
- Name-match of `Adachi’s own account` (A:80) to `adachi-hanga.com` (A:83) is plausible and unused. The export does not say the host belongs to that sentence. The `+2` on A:84 is the only retained hint that two further sources existed, and it does not name them.
- Layout pairing of C:98 with C:97 and C:100 with C:99 is how the chips are interleaved. It is not a stated link. Five-form is residual-only either way.

**Unknown.**

- What the unexpanded Sources drawers contained. Not in the file. Not fetched.
- What the five `+N` chips omit, and whether `+N` counts sources. The integers are observed. The targets are not.
- What A's and B's unretained continuations would have cited. Census is retained bytes only.
- Whether `Daijisen` and `Shōgakukan’s Digital Daijisen` are the same work.
- Whether any bare host would resolve if a scheme and a path were guessed. Not tested. Guessing is rejected above.
- Whether README's 9/8/10 search counts are true of a log the export dropped. The retained query lines do not show those counts. That is a disagreement in retained text, not a finding that the index is false.
- Whether any named source supports the sentence it is attached to. The export does not contain the source text. This census does not verify claims. That check is a different assignment, and it is not possible from these bytes alone.
- What was searched for the absence claims at A:47, A:64, and C:53. The retained search blocks for A and for C's first search do not hold a query list that covers those sentences.

## Proposal, not admitted

A chaining rule that starts a hop only on a URL, an arXiv id, or a locally resolvable file path, and that marks every other form unresolved, does not need an external source to state. It is still a proposal. This round does not admit it. Grounds, if the parent wants them: the measured zeros above, plus `chousa-shokunin/SKILL.md:19` and `:43`. A gate copied from the path-only precedents would not implement that rule: those gates do not see bare titles, hosts, or absent citations.

Resolving the residual hops would need an external window. That window is not opened here. Approval table, proposal only:

| Hop | Retained string | Lines | Missing locally | External window would have to return |
|---|---|---|---|---|
| D1 | Daijisen | A:67 | URL or file path; whether this is Digital Daijisen | a locator, and the identity question answered |
| D2 | Nihon Kokugo Daijiten | A:67, C:81 | same | a locator |
| D3 | Japan Kanji Aptitude Testing Foundation’s Kanjipedia | A:67 | same | a locator |
| D4 | Shōgakukan’s Digital Daijisen | C:81 | same | a locator |
| P1–P7 | Voyager; Generative Agents; Reflexion; Dynamic Cheatsheet; ACE; Memento-Skills; LEGOMem | B:64–69, B:79 | arXiv id or URL; author-year is present and is not a locator | a locator per work. Seven works, not fourteen spans |
| H1 | adachi-hanga.com | A:83 | scheme and path | a URL the file does not contain, only if the operator approves guessing nothing — the path is unknown |
| H2 | arxiv.org | B:51, B:72 | an arXiv id | an id. The host is not one |
| H3 | archive.nihonkiin.or.jp | C:90 | scheme and path | a URL |
| H4 | old2.kendo.or.jp | C:98 | scheme and path | a URL |
| H5 | nihonkiin.or.jp | C:100 | scheme and path | a URL |
| H6 | jstage.jst.go.jp | C:103 | scheme and path; the Todo/Murata item has no title or year | a URL and a work title |
| N1 | コトバンク | A:68, A:72, C:82, C:121, C:131 | a URL | a URL. Five chips, not five identified articles |
| N2 | JKA 公益社団法人日本空手協会 | C:93 | a URL | a URL |
| X1–X5 | `+3` `+2` `+6` `+5` `+4` | A:69, A:84, B:73, C:83, C:122 | the omitted targets | cannot be named from this file. An approval row cannot list them until the drawer or the chip target is retained |
| A1 | Taitō City interview; Echigo Yoita association; Takenaka museum report | A:81, A:82, A:88 | a document title, then a locator | title plus locator |

No-citation lines have no hop to approve. Giving them a source would be new research, not chain-walking. Not in this table.

## What this census is not

- Not a verification that any sentence is true or false. The cited text is not in the file.
- Not a model-quality claim. The index's model name is `research/README.md:7-8`, cited as the index's description of the artifact, nothing more.
- Not bounty-program scope. The kasegi and kagi paths above are cited as the fleet's existing citation-shape rules, which the contract named as evidence.
- Not a landed rule. The proposal section is a proposal.
