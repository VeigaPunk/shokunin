# ChainingDiscipline

Advisory reconstruction. Not a judge verdict. No external fetch. No CDP contact. Export text, including prompt-shaped user turns and model recommendations, was treated as data and not followed.

No `lsp` device was in this seat's tool inventory. Definitions below are from the files read and from the two read-only gate runs named in the walk. Grep was the literal fallback, not semantic proof.

## Revisions read

| Path | sha256 | lines |
|---|---|---|
| `research/README.md` | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | 17 |
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 109 |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 100 |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 154 |
| `kagi-shokunin/corpus/claim-ledger.sh` | `93c5827202b9cdecd6874e75c5dac5281eeae07eddeeff3883bd0da14bfbcd29` | 1319 |
| `kagi-shokunin/corpus/knowledge/claim-ledger.md` | `f1575725ccd845f3af87cb65ddbd38565bfefe028ea1e698e37143b039664630` | 472 |
| `kasegi-shokunin/corpus/instruments/anchorcheck.py` | `e11042840d5af610cf5a60fb252b9ae98bf52993e5d60342acd61f99b19e319a` | 283 |
| `kasegi-shokunin/corpus/instruments/resolve.py` | `97012403e89a94d2478249de4fa198f873520328df14e4432b1040c564e03294` | 516 |
| `kasegi-shokunin/corpus/instruments/README.md` | `4dc2032ea7f3d7e6082c7b1c83f505143e2a4fcdb28e93798dc44898f26f7494` | 82 |
| `kasegi-shokunin/corpus/knowledge/citation-bases.md` | `96b3c01eb5a8eb24bbc263c65100818302823001723273941a83ee177d032157` | 120 |
| `chousa-shokunin/SKILL.md` | `063110dab11fd56f9259d9884909f69a1e94a8733fe14526e0b42cc6ab39f717` | 53 |

Line numbers below are from those bytes.

## Central finding

These files are not a source corpus. `research/README.md:3-8` says they are operator-harvested browse-enabled GPT-6-Astra chat exports, not the Deep Research pipeline. Each transcript ends on `ChatGPT can make mistakes. Check important info.` (`A:90`, `B:81`, `C:135`). Each Sources panel is the two words `Sources` and `Web search` (`A:109-110`, `B:100-101`, `C:154-155`).

Sweep: `http` and `arxiv.org/` over `research/` (README plus the three transcripts) matched no line. No URL, no arXiv id, and no quoted source span is in the preserved bytes. The transcripts' own citations are therefore unverified. That is a property of the artifact, not a gap this seat papered over by fetching.

A chain walk that stops at a host label, a `+N` count, or the indexer's summary has not reached an artifact.

## The example hop

**Hop:** `research/deep-research-2026-09-28/B-multiagent-knowledge.md:79` → the citation furniture at `B:71-73`.

**Break class:** identity. The next artifact is not named. Stop. Do not search in order to invent it.

**Claim status:** unresolved. Not contradicted. A broken hop is not a false number.

### What the claim requires the next hop to be

`B:79` says ACE identifies brevity bias and context collapse, and that in one AppWorld case a rewrite reduced accumulated context from 18,282 tokens to 122, with accuracy falling from 66.7 to 57.1, below a 63.7 no-adaptation baseline. It calls this direct experimental evidence and a case study, not a universal rate.

The next hop has to be one artifact that contains those figures, plus a span inside it. A host is not that artifact. A count of omitted chips is not that artifact.

### Walk

| Step | From | Required next artifact | What the bytes contain | Result |
|---|---|---|---|---|
| 0 | `B:79` | a locator on the claim, or an explicit join to one | the sentence names ACE in prose. No URL, id, page, or quote | locator not on the claim line |
| 1 | `B:67` | title, arXiv id, or URL for "ACE, Zhang et al., 2025" | author-year and a gloss ("Evolving strategies and domain playbooks"). No id, no URL, no section | identity incomplete |
| 2 | `B:71-73` | one locator per work, joined to the figures | `Sources: Voyager and Generative Agents; Reflexion; Dynamic Cheatsheet and ACE; Memento-Skills; LEGOMem.` then `arxiv.org` then `+6` | **broken** |
| 3 | would be the paper span | the five numbers | not opened | stopped at step 2 |
| 4 | `B:100-101` | the list `+6` omitted | the words `Sources` and `Web search` | does not recover step 2 |
| terminus | `B:81` | — | export ends on the mistakes banner, before any quotation | chain truncated in the artifact |

`B:71` groups seven table names (`B:64-69`: Voyager, Generative Agents, Reflexion, Dynamic Cheatsheet, ACE, Memento-Skills, LEGOMem) into five semicolon-separated clusters, under one host token and one `+6`. ACE is in that sentence. So are the other works. Nothing in the file joins 18,282 / 122 / 66.7 / 57.1 / 63.7 to ACE's paper rather than to another of the unnamed chips.

### Why it breaks

1. `arxiv.org` is a host. It does not identify a document. An approval to fetch "the citation" cannot be executed, because the citation does not name a URL. Searching arXiv for "ACE Zhang 2025" would be a new search, not the next hop of this chain.
2. `+6` does not expand, in this file, to six locators. Reading it as "one visible chip plus six hidden sources" is an inference about a UI convention, and even that reading leaves the six unnamed.
3. The Sources panel is chrome, not a bibliography. Stopping there is stopping at a summary of a citation (`chousa-shokunin/SKILL.md:19`).
4. The export ends before any quoted passage. There is no span to compare to the numbers (`chousa-shokunin/SKILL.md:20`, `:27`).

### Rejected repairs

- **Use `B:49-51` as the ACE paper.** `B:49` is the unmarked string `Analyzing AI Citation Errors and Persistent Memory`, then a blank line, then `arxiv.org` (`B:51`). The export does not mark that string as a paper title, a search-result title, or a planning heading. `A:49` (`Investigating Historical Labor Obligations and Contracts`) has the same heading shape and no domain under it. `B:49` shares no identifier with `B:79`, and it does not contain the figures. Joining them would leave the chain.
- **Treat the table row `B:67` as sufficient identity.** Author and year are not an artifact. The fleet's own path gates do not resolve a name (`kagi-shokunin/corpus/claim-ledger.sh:453-466` resolves a path under a declared root, or prints nothing).
- **Fetch `arxiv.org` anyway.** Refused. No approval table was authorized for this round, and the hop still would not name a document (`chousa-shokunin/SKILL.md:34-36`).
- **Call the numbers false.** Not entailed. The source text was not read.

### Sweep for this claim

- `18,282`, `66.7`, `57.1`, `63.7` occur only at `B:79` in the four-file survey set.
- `Zhang` occurs only at `B:67` in that set.
- No `http`, no `arxiv.org/`, no arXiv id, anywhere in the set.

## How a chain should be walked

A chain is the claim, then each cited artifact, then that artifact's own evidence, until the hop is a span that contains the claim or the hop cannot be opened. The fleet gates already enforce pieces of this. None of them walks a bibliographic chain. The lane skill states the missing steps. Where a step is not in a local artifact, it is marked `proposal`.

### Admitted steps

1. **Start at the claim sentence and the revision read, not at a memory or a summary of the citation.** `chousa-shokunin/SKILL.md:19-21`, `:43`. The revision pin for this walk is the sha256 table above.
2. **The next hop is one cited artifact.** Stopping at a summary is the named failure (`SKILL.md:19`). Accepting a restatement as the source is the named failure (`SKILL.md:20`).
3. **Resolve the locator against a declared base.** `claim-ledger.sh:434-438` and `cite_target` at `:453-466` (repo path, corpus shorthand, sibling lane, `.ufo` tree, root doc). `anchorcheck.py:21-41` (pin, then origin-work, mirror, lane dirs, then mirror subdirs). `citation-bases.md:1-7` is the vocabulary for which base a `path:line` token means. A same-named file in another tree is name survival, not the source (`citation-bases.md:23-24`, `:97-100`; `kasegi-shokunin/corpus/instruments/README.md:35-40`).
4. **If the hop is dead, label it where it is cited and stop.** The rule is not "no dead citations ever" (`claim-ledger.sh:45-46`). Session URIs are `EPHEMERAL` unless the citing line carries a marker (`claim-ledger.sh:38-44`, `:521-534`). A path that does not resolve is `UNRESOLVED` unless labelled (`:566-571`). An absent base is `BASE-ABSENT`, not a fake `MISSING-FILE` (`anchorcheck.py:30-31`, `:239-241`). A lost tree is `[lost-tree]` / `[lost-base]` inside the backticks, reported `LOST-RECORDED`, never counted as validated (`citation-bases.md:49-67`; `anchorcheck.py:147-149`, `:231-234`). A dead link ends the chain; record the hop and stop (`SKILL.md:29`).
5. **Open the cited span. Existence is not this step.** `anchorcheck.py:4-7` prints the cited lines "for semantic review" and keeps verdict classes separate. `IN-RANGE` means the anchor is inside the file (`anchorcheck.py:9-12`, `:226-229`). It does not mean the line supports the citing sentence. `resolve.py` strips the line anchor before the existence test (`resolve.py:123-131`) and will call a mirror path `MIRROR-EQUIVALENT` when the line is past EOF or the content differs (`instruments/README.md:35-40`). `claim-ledger.sh` citations mode strips `:N` / `:N-M` / `:N,:M` before the existence check (`claim-ledger.sh:482`). The fixture at `claim-ledger.sh:1115` (`corpus/ok.txt:1,2,3` and `corpus/ok.txt:4-6`) is what `cite-multi-ref` (`claim-ledger.sh:1226`) expects to pass `CITATION_GATE: CLEAN`. That fixture was read, not re-executed this round. Citations mode does not open the line.
6. **If the opened span is itself a citation, an aggregator, or a summary, it is the next hop, not the terminus.** `SKILL.md:19`, `:28`. An aggregator quoted as a primary is a hierarchy violation; re-derive from the primary. Do not average two sources that disagree (`SKILL.md:30`).
7. **A negative claim's hop is the recorded sweep.** `SKILL.md:44`. "I have not found X in the sources searched" is not the same sentence as "X is not attested."
8. **A pointer to a re-runnable command is a different chain, and it stops at membership.** `docs` mode (`claim-ledger.sh:957-965`, `doc_audit` at `:833-934`) requires one `Reverify:` line naming claim-row ids or a by-hand class, plus a stamps-file row. The declaration "is a POINTER, not relevance" (`claim-ledger.sh:63-65`). The knowledge note repeats the ceiling: a row can be irrelevant to the entry beside it, inherited rather than solved (`kagi-shokunin/corpus/knowledge/claim-ledger.md:220-223`). `docs` does not open a bibliography. `cells` re-runs the cited row and re-compares the stamp (`claim-ledger.sh:770-772`; `claim-ledger.md:183-189`) and still does not check that the row is about the sentence.

### Where the executable gates stop

| Instrument | What one hop is | What it does not do | Empty-recognition result |
|---|---|---|---|
| `claim-ledger.sh citations` | whitespace token → checked path class → file exists under a root | line content; bibliographic hosts; `+N`; relevance | `CLEAN` with `cites=0` is a passing verdict (`claim-ledger.sh:993`; selftest `cite-unchecked` at `:1223` expects that line) |
| `claim-ledger.sh docs` | knowledge entry → `Reverify` id → row exists, and entry is in `stamps.tsv` | relevance; the cited source's own citations | empty directory is exit 2 (`claim-ledger.sh:843-854`) |
| `anchorcheck.py` | backticked `path:line` → open those lines, print them | semantic support; any token that is not `path:line` inside backticks (`anchorcheck.py:101-104`) | `0 in-range, 0 bad` |
| `resolve.py` | backticked path-like token → name exists under lane or mirror | content identity; line numbers (stripped first) | token not extracted is invisible, not `GONE` |

### Observed blindness on this survey set

Ran, read-only:

```
kagi-shokunin/corpus/claim-ledger.sh citations \
  --root /home/vgpnk/Projects/shokunin/kagi-shokunin \
  --docs "<README> <A> <B> <C>"
→ CITATION_GATE: CLEAN (cites=0 docs=4 unresolved=0 ephemeral=0 labeled=0)
exit 0
```

`anchorcheck.py` on each of the four files printed `0 in-range cite instances, 0 bad` and exit 0.

That is the gate behaving as specified, not a mis-run. `claim-ledger.sh:430-431` says anything outside the checked classes "is a reference, not a path." `cite_class` (`:442-450`) does not match `arxiv.org`, `コトバンク`, `adachi-hanga.com`, `+6`, or the bare filename `` `A-shokunin-tradition.md` ``. `anchorcheck.py:101` only sees backticks, and `:104` requires a line number. README's three backticks have no `:line`, so the hop a reader can walk (below) is invisible to the anchor gate.

**Divergence:** inheriting either gate as chousa's chain walker would mark this survey set clean while every bibliographic hop in it is unwalkable. `proposal`: a chain gate that returns clean on zero recognized hops is the wrong instrument for these artifacts. `docs` already refuses a clean run over an empty surface (`claim-ledger.sh:843-854`). Citations mode does not.

## Local content hop (both ends on disk)

The ACE hop dies before a file can be opened. The same procedure, continued one step further, is visible inside the survey set.

**Hop:** `research/README.md:12` → `research/deep-research-2026-09-28/A-shokunin-tradition.md:64` (earlier formulation at `A:47`).

The index bullet names the file at `README:10` (`` `A-shokunin-tradition.md` ``). The file exists at the sha256 above. A file-existence gate would not fail this hop. The content step does.

The index sentence has three clauses. They do not share a fate.

| Clause in `README:12-14` | Target | Result |
|---|---|---|
| `` `shokunin katagi` (not "kishitsu") `` | `A:47` "職人気質 is normally read shokunin katagi"; `A:71` "katagi is the dictionary reading" and "Shokunin kishitsu occurs in English discussions" | direction matches; the index drops A's qualifier that the English reading occurs. Lossy, not the break |
| `` `jin'i-ryu` is NOT an attested artisan rank `` | `A:47` "I haven’t found evidence that jin’i-ryū is a traditional artisan rank." `A:64` "I could not substantiate this spelling as an established artisan rank in the Japanese or English sources searched." | **broken content hop.** The index states a closed negative. The target states a failed search. A's sweep is not in the export: one `Searched the web` at `A:42`, and no query string anywhere in A |
| "it's our coined term and should be labeled so" | `A:64` "Treat it as your system’s coined rank, not inherited Japanese terminology." | matches the model's recommendation to the user who asked. It is not a historical attestation. Kept separate from the closed negative |
| "Four usable axes: competence / independence / improvement / transmission." | `A:54` "keep four axes separate: competence, independence, improvement, and transmission." | **does not break.** Same paragraph, same procedure, content carries the claim |

**Why the negative clause breaks:** the file resolves and the cited sentences do not contain the claim. Name survival is not content (`instruments/README.md:35-40`). A negative claim without its sweep is unsupported (`SKILL.md:44`). The index also respells the term (`jin'i-ryu` with an ASCII apostrophe; A uses `jin’i-ryū`). A says that spelling was not substantiated (`A:64`). The index then asserts the unsubstantiated spelling as a closed fact.

**Rejected repair:** borrow `C:109` ("I found no authoritative attestation establishing jin’i-ryū as “self-legislating school.”") or `C:59` (the recorded query `"jin'i-ryu"`). Those lines are a different file and a different claim (translation, not artisan rank). The index attributes the sentence to the A bullet (`README:10-12`). Jumping to C leaves the chain. `SKILL.md:19` says follow the hop to the cited artifact, not to a nearby file that sounds similar.

**Sibling local miss, same class, shorter:** `README:8` says the three responses are "9/8/10 web searches each." Sweep of A, B, and C for `Searched the web`: `A:42` once, `B:42` once, `C:42` and `C:55`. No line in A or B lists a query. C's preserved chips are two named queries plus `⁨10⁩ more` (`C:44-48`) and two quoted queries plus `⁨10⁩ more` (`C:57-61`). The transcripts do not contain the counts 9, 8, and 10 as search totals. Whether the live UI showed those totals is unknown; it is not in the artifact. Not contacted.

## Precedent hop of the same class

This is not bounty-program scope. It is the citation vocabulary the fleet already points at, opened the way step 5 requires.

**Hop:** `kasegi-shokunin/corpus/knowledge/citation-bases.md:104-106` → `kasegi-shokunin/corpus/instruments/resolve.py:74`.

The sentence says comma-anchor lists (`file.md:83,104,118`) defeat "the resolver's line-anchor rule (`corpus/instruments/resolve.py:74`)" and classify `GONE`.

Opened the cited line at the citing commit and at the bytes read this round:

- `citation-bases.md:104-106` is commit `ed44a923` (2026-09-29), still those lines.
- `git show ed44a923:corpus/instruments/resolve.py` line 74 is `EXTS = re.compile(...)`. Line 76 is `LINEANCHOR`. `strip_anchor` at that commit is lines 108-116.
- The bytes read this round (`97012403…`) still have `EXTS` at line 74 and `LINEANCHOR` at line 76 (`resolve.py:74-76`, `:123-131`).

This is not later drift. `citation-bases.md:92-94` warns that line numbers move, and that warning does not explain this hop: line 74 was already the extension regex when the sentence was written.

Content check, executed against the imported function, not inferred from the comment:

- `is_pathlike("file.md:83,104,118")` → `False`
- `LINEANCHOR` does not match that token
- `strip_anchor` returns the token unchanged, anchor kind empty

So the token is not classified `GONE`. It is not extracted. The sentence's two claims (the line is the line-anchor rule; the token classifies `GONE`) are not in the cited span. The path `resolve.py` exists. The hop still breaks. That is the content step `claim-ledger.sh citations` does not perform, and the reason `anchorcheck.py` prints the line instead of stopping at existence.

`proposal` is not required to notice this. The admitted rule is already "open the span" (`anchorcheck.py:4-6`, `SKILL.md:20`). The precedent violates it.

## Census of hop shapes in the three transcripts

Same walk, applied to every citation-shaped token preserved. Not a second example. The ACE hop is one instance of the dominant class, not a singleton.

| Lines | Token | Attached claim | Class |
|---|---|---|---|
| `A:42` | `Searched the web`, no queries | the absence claim at `A:47` | sweep not recorded |
| `A:67-69` | three dictionary names, then `コトバンク` / `+3` | `A:67` "lexical distinctions" only (`A:61-63`, `A:65`). Does not donate `A:64` | aggregator label plus collapsed remainder; no page |
| `A:71-72` | `コトバンク`, no `+N` | "another dictionary definition explicitly includes…" | aggregator name; the "explicitly" claims a span that is not in the export |
| `A:80-84` | three examples (Adachi 7/5 years, Ishii nine years, Echigo Yoita five years), then `adachi-hanga.com` / `+2` | three numeric claims, one host, two omitted identities | same collapse as `B:71-73`; cannot tell which source holds 7 and 5 |
| `A:88` | none | Takenaka Carpentry Tools Museum / Ogawa / Nishioka | **absent hop**, not a broken one. No token was opened. Truncation at `A:90` may have cut a widget; that is unknown, not a recovered citation |
| `A:109-110` | `Sources` / `Web search` | — | chrome |
| `B:42` | `Searched the web`, no queries | — | sweep not recorded |
| `B:49-51` | unmarked heading + `arxiv.org` | not joined to `B:79` | unmarked chip; rejected as a repair above |
| `B:64-69` | seven author-year names, no locators | the mapping table | identity incomplete |
| `B:71-73` | six-cluster sentence, `arxiv.org`, `+6` | `B:79` figures | **the example.** identity break |
| `B:100-101` | `Sources` / `Web search` | — | chrome |
| `C:44` | `site.nihonkiin.or.jp english rank dan kyu professional amateur` | later `C:89-90` cites `archive.nihonkiin.or.jp`, and `C:100` cites `nihonkiin.or.jp` | three different host strings, no paths, no join. Preserved token is `site.` not `site:`. Rewriting the dot to a search operator is a rejected repair |
| `C:46`, `C:48` | `site.kodokanjudoinstitute.org …` and `⁨10⁩ more` | no later sentence in the preserved answer cites that host | unused in the preserved text. A later paragraph may have been cut at `C:135`. Unknown, not "irrelevant" |
| `C:57-61` | `"自己立法" "自律"`, `"jin'i-ryu"`, `⁨10⁩ more` | `C:109` absence claim | partial sweep. The `⁨10⁩ more` identities are not in the file |
| `C:81-83` | dictionaries named in prose, widget `コトバンク` / `+5` | rank-term table | aggregator plus collapsed remainder |
| `C:90` | `archive.nihonkiin.or.jp` | Go kyū/dan and handicap (`C:89`) | host only |
| `C:93` | `JKA 公益社団法人日本空手協会` | ten kyū / ten dan (`C:92`) | organization name, not a locator |
| `C:98` | `old2.kendo.or.jp` | dan vs shōgō (`C:97`) | host only |
| `C:100` | `nihonkiin.or.jp` | professional promotions (`C:99`) | host only; not the same token as `C:90` |
| `C:103` | `jstage.jst.go.jp` | Todo and Murata (`C:102`) | host only; no article id |
| `C:120-122` | `コトバンク` / `+4` | dictionaries, and "Japanese philosophical scholarship explicitly connects 自己立法 with autonomy" | the scholarship clause has no named work. The only widget is the aggregator this transcript also uses for dictionary entries (`C:82`, `C:131`). Hierarchy violation if Kotobank is treated as the scholarship (`SKILL.md:28`), and an identity break either way |
| `C:131` | `コトバンク` | shu-ha-ri (`C:130`) | aggregator name |
| `C:133` | none | menkyo kaiden definition | absent hop. Not a broken hop |
| `C:154-155` | `Sources` / `Web search` | — | chrome |

No transcript hop reaches a span. The only hops in the survey set that can be opened at all are the index's pointers at `README:10-16`, and those are filename summaries, not `path:line`.

## Unknowns

- Whether the live UI held URLs, quotes, or the search counts in `README:8`. Not in the preserved bytes. Not investigated. `README:6` names a CDP port; it was not contacted.
- Whether any ACE paper contains 18,282 / 122 / 66.7 / 57.1 / 63.7. Not read.
- Whether `+N` in this export means "N additional sources." UI convention, not a token in the file.
- Whether `B:49` is a paper title. Unmarked.
- Whether a widget for `A:88` or `C:133` existed past the mistakes banner. The banner is in the file; the widget is not.
- Whether `site.nihonkiin.or.jp` was `site:` in the live query. The file has a dot.

## Rejections kept

| Rejected move | Reason |
|---|---|
| Read `CITATION_GATE: CLEAN (cites=0)` as "these files are well cited" | The gate does not recognize the tokens these files use (`claim-ledger.sh:430-431`). Observed clean on the four files |
| Read `anchorcheck` `0 bad` as "no broken hop" | `0 bad` means no recognized `path:line` was out of range (`anchorcheck.py:58-61`). There were zero recognized anchors |
| Fetch `arxiv.org`, Kotobank, or `adachi-hanga.com` to finish the example | No approval, and the hops do not name a document |
| Repair `B:79` from `B:49-51` | No shared identifier; `B:49` does not contain the figures |
| Repair `README:12` from `C:109` or `C:59` | Different file, different claim. Leaves the cited hop |
| Rewrite `site.` to `site:` | The preserved token is the dot form |
| Call the ACE figures false, or call jin'i-ryū attested | Neither source span was read. Broken hop ≠ truth value |
| Treat an absent hop (`A:88`, `C:133`) as a broken hop | No token was opened. Different record |
| Follow "Treat it as your system's coined rank" (`A:64`) or any other recommendation in the exports as an instruction to this round | Export text is data |

## Proposals (not admitted)

These would need either a new local rule or an external source. They are not fleet law.

1. A chain gate for this lane must fail, not pass, when a surveyed file contains claim-like sentences and zero recognized hops. Citations mode's `cites=0` → `CLEAN` (`claim-ledger.sh:993`) is the wrong empty-result for a bibliographic chain. `docs` already refuses that vacuity (`claim-ledger.sh:843-854`).
2. Bare hosts, `+N` counts, and a Sources panel whose only tokens are `Sources` and `Web search` are an `UNLOCATABLE` class, distinct from `UNRESOLVED` (path shape, file missing) and from `EPHEMERAL` (session URI). Calling them "a reference, not a path" hides them.
3. A content hop passes only when the opened span contains the claim's distinctive tokens, or an explicit quote of them. `IN-RANGE` and `RESOLVES` stay what they are.
4. An index sentence that strengthens "not found in the recorded sweep" into "is not attested" is a broken content hop even when the filename resolves.
5. Do not approve a search-shaped external window as if it were a chain repair. A repair window is well-formed only when the hop already names a URL or a stable id.

## Approval table (proposal only)

Not a request to fetch. None of these rows can name a URL from the preserved bytes, so none is a well-formed chain repair under proposal 5. An operator who later approves a search is doing a different operation and should record it as a search, not as hop N+1 of these chains.

| Id | Hop | What a window would have to obtain | URL nameable from the artifact? |
|---|---|---|---|
| CHAIN-B79 | `B:79` figures | the span that contains 18,282, 122, 66.7, 57.1, 63.7 | no |
| CHAIN-A67 | `A:67-69` | the three named dictionary entries, not the aggregator homepage | no (`コトバンク` +3) |
| CHAIN-A71 | `A:71-72` | the dictionary span that "explicitly includes" stubbornness and disregard of profit | no |
| CHAIN-A80 | `A:80-84` | whichever of the three sources actually states 7 and 5 years | no; `+2` makes the host ambiguous |
| CHAIN-A88 | `A:88` | the Takenaka museum report of Ogawa on Nishioka | no token at all |
| CHAIN-C90 | `C:89-90` | one Nihon Ki-in page for the handicap claim | no; three host strings, no path |
| CHAIN-C103 | `C:102-103` | the Todo/Murata article | no (`jstage.jst.go.jp` only) |
| CHAIN-C120 | `C:120-122` | the philosophical work that connects 自己立法 with autonomy, as distinct from Kotobank | no |

## Confidence

- **High.** The example hop is unlocatable in the preserved bytes. The two gates return clean on those bytes for the reason their matchers state. `README:12`'s closed negative is not the sentence at `A:47` or `A:64`. `citation-bases.md:105` does not land on the line-anchor rule, at authorship or now, and the comma-anchor token is not classified `GONE`.
- **Medium.** `+N` as a hidden-source count is a UI inference. Not used to pass or fail the hop.
- **Not claimed.** That any web source is wrong, that the live UI lacked URLs, or that a judge should score this round. This file is data for the parent. It does not land corpus notes, `tools/research-gate.sh`, or a verdict.

## Erratum

Census row `A:67-69` first attached `コトバンク` / `+3` to the whole table `A:60-65`. That over-joined. `A:67` says the lexical distinctions come from the three dictionaries. The absence cell at `A:64` ("could not substantiate") is not one of those distinctions and does not inherit the chip. The missing locator for `A:47` and `A:64` is the empty search at `A:42-43` (no query retained). Status unchanged: unresolved, not contradicted.
