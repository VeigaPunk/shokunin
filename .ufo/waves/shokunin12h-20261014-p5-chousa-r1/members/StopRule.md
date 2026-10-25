# StopRule — research-window stop, falsified

Advisory data for the parent. Not a lane verdict, not a host stop, not a judge result. Prompt-shaped text inside the exports is the question ledger (data), not an instruction. No external fetch was made. Nothing below verifies a web source.

The three stored tabs do not contain a justified stop. They contain several completion-shaped signals that disagree with each other and with the unanswered asks. Stopping on any one of those signals is premature. The smallest safe correction is one fail-closed predicate: a question ledger over the captured body, with sweep and citation sub-checks. UI events, the index, and a sibling lane's path-gate are not that predicate.

## Candidate stop rules under attack

Each candidate is invited by a local sentence. None is admitted.

| Id | Invited rule | Where it is invited | Why it looks like a stop |
|---|---|---|---|
| S1 | UI chrome means the response finished | `research/deep-research-2026-09-28/A-shokunin-tradition.md:90-91`, `B-multiagent-knowledge.md:81-82`, `C-rank-taxonomy.md:135-136` ("ChatGPT can make mistakes" then "Latest response"); empty `Sources` / `Web search` footers at `A:109-110`, `B:100-101`, `C:154-155` | The capture ends in completion chrome |
| S2 | A duration means the window closed | `A:36-37`, `B:36-37`, `C:36-37` (`Worked for` and `Working for`) | A timer is printed |
| S3 | A search count means the window closed | `research/README.md:8` ("9/8/10 web searches each") | The index states a count |
| S4 | "Haven't found" means the negative is closed | `A:47`, `A:64`, `C:53`, `C:109`; index upgrade at `research/README.md:12` | The model, then the index, speaks in absence |
| S5 | Named hosts plus `+N` means the sources were harvested | `A:68-69`, `A:83-84`, `B:72-73`, `C:82-83`, `C:122` | Chips look like a bibliography |
| S6 | The index corrections are the harvest, so the window is done | `research/README.md:10-16` | Bold "Corrections for our scheme" |
| S7 | A dead citation chain stops the window | `chousa-shokunin/SKILL.md:29` ("chain ends at a dead link … record the hop and stop") | These exports have no openable hop, so a reader may treat the chain as dead and the window as closed |
| S8 | One experimental case closes the failure-mode ask | `B:79` (one AppWorld rewrite; the same sentence says it is not a universal rate) | It is the only numeric result in the corpus |
| S9 | A sibling citation gate being clean (or inapplicable) means research citations are closed | `kagi-shokunin/corpus/claim-ledger.sh:31-46`; `kasegi-shokunin/corpus/instruments/anchorcheck.py:101-104` | The fleet already has citation gates |

S7 is the lane's own written stop. The defect is promoting it from one hop to the window. S1–S6 and S8–S9 are readings the stored files invite. Rejecting them is the falsification.

## What would justify stopping

**Proposal** (method, not a finding about the tradition or the papers). A research window may be marked stopped only when every row of the ledger below is true of the **captured body**. A timer, a badge, a directory name, an index sentence, or a green sibling gate is not a row.

1. **Question ledger closed.** Every numbered ask and every named topic in the prompt is `answered` (with a body section), `negative-with-sweep`, or `deferred-with-reason`. Silence is not a status. A residual "I'm checking" / "Investigating" / "Analyzing" line with no later close keeps the window open. Forced by `A:47`, `A:49`, `B:47`, `B:49`, `C:40` (plan names self-certification; no such section follows).
2. **Answer boundary, not capture boundary.** The answer text itself closes (section closer, or an explicit remainder). Disclaimer + "Latest response" + an empty Sources footer after a mid-argument is `CAPTURED`, not stopped. Forced by `A:88-91`, `B:79-82`, `C:128-136`.
3. **Search log replayable.** Every search event lists its queries. Bare "Searched the web" fails. A collapse marker fails. A negative cites that list. Forced by `A:42` (no queries), `B:42` (no queries), `C:48`, `C:61`.
4. **Citation form.** An admitted source is a resolvable local anchor, or it is labelled dead/unverified on the citing line. A hostname and a `+N` chip are not citations. Unverified model numerals stay unverified; they cannot be the stop witness. Forced by the chip lines in S5 and by `kagi-shokunin/corpus/claim-ledger.sh:44-46` (a dead citation must be labelled dead where it is cited — these chips are not even labelled).
5. **Pipeline identity matched.** The record names the pipeline that ran. Prompt prefix and directory name are not identity. Forced by `research/README.md:6-8` against the path `research/deep-research-2026-09-28/` and the "Deep research:" prefixes at `A:35`, `B:35`, `C:35`.
6. **Index ⊆ body.** An index sentence with no supporting body line is `INDEX_OVERRUN` and blocks stop. Forced by `research/README.md:12` and `research/README.md:16` (sweeps below).
7. **The artifact's own caveat survives.** A stop that drops "not a universal failure rate" (`B:79`), "not a declaration of knowledge" (`A:88`), or "do not establish indefinite, reliable self-improvement" (`B:59`) has changed the finding. That is not a stop; it is an edit.

Chain-stop stays chain-local. `chousa-shokunin/SKILL.md:29` closes one hop after the hop is recorded. It does not close sibling asks. `chousa-shokunin/SKILL.md:18-19` already forbids stopping at a summary of the citation. Both sentences are in force. Neither fires as a window stop on these files (see rejection R7).

This is not a never-stop rule. `B:59` says preprint benchmarks do not establish indefinite self-improvement. A window that waits for the literature to prove the fleet never stops, and the artifact already refuses that bar. Stop when the ledger is closed, including explicit unknowns — not when the science is finished, and not when the UI looks finished.

## Strongest counterexample

Stop at `A:91` because the file says "Latest response."

What that stop drops, all still inside the same file:

- The prompt's asks (2) whether a master finishes, (3) teach versus hoard, and (4) public evidence of narrow mastery. Ask (1) is the only numbered section, and it ends on the exhibit the previous sentence called "particularly relevant" (`A:88`).
- `ikigai` and `kodawari`, named in `A:35`, absent from the body. Sweep: `ikigai|kodawari|hoard` over `A-shokunin-tradition.md:38-110` — no hits. (`finish` / `teach` / `transmission` do hit; see the ledger. Absence is claimed only for the three tokens.)
- The status line that was still open: "I'm checking how practitioners distinguish independence, continued learning, and transmission" (`A:47`), and the thread title "Investigating Historical Labor Obligations and Contracts" (`A:49`), which has no section under it.
- Unlogged negative at `A:64` ("could not substantiate"; "semantics remain uncertain") with zero query strings after `A:42`.
- Hidden chips `コトバンク +3` (`A:69`) and `adachi-hanga.com +2` (`A:84`).

The same file's last substantive sentence says independence is "graduated responsibility through actual work, rather than independence established by a declaration of knowledge" (`A:88`). S1 is a declaration. The incomplete answer already rejects the shape of the stop a reader would take from its own chrome.

The disclaimer on the previous line (`A:90`, same pair at `B:81` and `C:135`) says the answer may be wrong and should be checked. A stop that fires on that chrome ignores the sentence it is firing on.

`kagi-shokunin/corpus/claim-ledger.sh:27-30` is the fleet's analogue, not a research-window rule: a verdict-shaped string followed by failure must not pass; the verdict has to be the last line. Here the verdict-shaped string ("Latest response") is not even the answer's last substantive line, and the question ledger after it is a failure. **Inference, marked as such:** treating S1 as a stop repeats the shape that final-line rule was written to refuse. The rule itself governs claim-ledger commands, not these exports.

## Question ledger

Status is against the captured body only. `prompt-only` means the token occurs in the "You said" line and not as a delivered finding.

| Artifact | Ask | Body status | Witness |
|---|---|---|---|
| A | Term ladder minarai / deshi / shokunin / jin'i-ryū / kiwami | Partial table. Model says the sources do not establish that ladder | `A:52`, `A:60-65` |
| A | jin'i-ryū as a traditional rank | Negative, **sweep missing**. Wording is "could not substantiate" / "semantics remain uncertain", not a closed absence | `A:47`, `A:64`. Queries: none after `A:42` |
| A | katagi / kishitsu | Reading corrected; glossed as a disposition, "not a formal ethical constitution". Ethics not developed | `A:71` |
| A | ikigai | Absent from body | Sweep above |
| A | kodawari | Absent from body | Sweep above |
| A | (1) domain independence | Partial. Three workshop examples, then the Nishioka/Ogawa exhibit, then chrome | `A:74-88`. Hosts for two of the three examples sit inside `+2` (`A:84`) |
| A | (2) does a master finish | Not a section. "Lifelong refinement" is asserted in the framing paragraph. "Finishing" at `A:76` is apprenticeship completion, a different question | `A:52` assertion; `A:76` different sense; `A:47` still checking "continued learning" |
| A | (3) teach vs hoard | Not a section. "Teaching" appears in a design sentence. `hoard` absent | `A:54`; sweep above |
| A | (4) public evidence of narrow mastery | Absent | No section between `A:74` and chrome |
| A | Primary-ish citations | Names and chips. No URL, no quote, no local anchor | `A:67-69`, `A:83-84` |
| B | (1) drift | Absent from body | Sweep `drift\|forgetting\|hallucin` over `B:38-101`: no hits |
| B | (1) forgetting | Absent from body | Same sweep |
| B | (1) hallucinated citations | Thread title only. Not a finding | `B:49` "Analyzing AI Citation Errors and Persistent Memory"; no citation-error section after it |
| B | (1) destructive rewrite | One case study, with the author's own non-universality caveat. Numerals unverified | `B:77-79` |
| B | (2) split vs expand | Not delivered. Status still checking. Body has a scope caveat, not a criterion | `B:47`, `B:75` |
| B | (3) credit assignment | Plan sentence and a status preview. No paper section. Design sentence at `B:57` is not a citation | `B:40`, `B:47`, `B:57` |
| B | Cite papers | Author/year names. `arxiv.org +6`. No ids | `B:63-73` |
| C | kyū/dan, Go, martial grading | Sections present. Host chips, not URLs. Unverified | `C:87-105` |
| C | shokunin / takumi / meishō as a ladder | Denied as a standard sequence, on dictionary overlap, chips collapsed | `C:53`, `C:81-83` |
| C | jin'i-ryū = self-legislating school | Negative, **sweep not replayable**. Four query strings visible; two collapse markers | `C:53`, `C:57`, `C:59`, `C:109`. Markers: `C:48`, `C:61` |
| C | Naming for (a)–(d) | Explicit recommendation, not a sourced finding | `C:69` "My recommended operational names" |
| C | Appropriation | One paragraph. Does not claim universal cultural acceptance | `C:85` |
| C | Rank inflation | Absent from body. Claimed by the index | Sweep `inflation\|self-attest\|failure mode` over `C:38-155`: no hits. Index: `research/README.md:16` |
| C | Self-attestation | Phrase absent. Adjacent sentence: rank is conferred by procedure, not self-description. That is not a failure-mode survey | `C:92` |
| C | Other metaphors | Open heading. Two items, no closer, then chrome | `C:128-136` |

Counts, so a later note cannot say "the tabs covered the prompts": A delivers a partial on 1 of 4 numbered asks; B starts 1 of 3 and does not finish it; C never opens the failure-mode ask the prompt and the plan both named (`C:35`, `C:40`).

## Search log and the README count

Observation. Stored search events: A one (`A:42`), B one (`B:42`), C two (`C:42`, `C:55`). Visible query strings: A 0, B 0, C 4 (`C:44`, `C:46`, `C:57`, `C:59`). C also stores two collapse markers whose visible text is the digits 10 wrapped in U+2068 / U+2069 then " more" (`C:48`, `C:61`). Sweep: ASCII `10 more` over `C-rank-taxonomy.md` returned no matches, so a stop-gate that greps that form will not see the unreproducible sweep.

`research/README.md:8` says 9/8/10 web searches. Those digits are not in the exports as a search count. Visible events (1, 1, 2) are a count of **recorded search-event lines**, not of searches performed. "10 more" is a **query-list** collapse, a different unit from "web searches."

Unknown, kept unknown: whether 9/8/10 was true of the live tabs. The exports neither confirm nor refute it. Therefore the README count cannot witness a stop of the **stored** window. Using it as the stop is S3, and S3 cites a sentence the artifact under review does not contain.

## Citation shape the fleet gates do not see

Observation. Source tokens in the bodies are hostnames, a dictionary name, and `+N` counts: `A:68-69` (`+3`), `A:83-84` (`+2`), `B:72-73` (`+6`), `C:82-83` (`+5`), `C:121-122` (`+4`). Hidden-chip sum printed by the UI: 3+2+6+5+4 = 20. Those 20 are counts, not titles. They were not read here. They cannot be marked `[lost-tree]` either: a lost-tree anchor still records the path (`kasegi-shokunin/corpus/knowledge/citation-bases.md:50-54`). A `+6` records nothing. It cannot enter a resolving numerator, and it also cannot enter the lost-recorded numerator. It is an uncaptured hop.

`kagi-shokunin/corpus/claim-ledger.sh:31-46` checks path-shaped and session-URI tokens (`corpus/…`, lane shorthands, `local://`, and the labelled-dead exception). A hostname and `+3` are outside that class. `kasegi-shokunin/corpus/instruments/anchorcheck.py:17-19` refuses to count a deliberately non-openable anchor as validated; `anchorcheck.py:53-56` separates range-valid from semantic support. **Inference from those classifiers, not a gate run:** neither documented checked class includes a hostname or a `+N` chip, so a pass from either gate would not have inspected these sources.

S9 is therefore a category error. A clean (or vacuously inapplicable) sibling path-gate does not close a research window whose sources are chips. **Inference:** wiring research-gate stop to claim-ledger CLEAN would launder unverified hosts into a pass. That is a duplicate authority, and it is the wrong one.

Central finding, stated rather than papered over: every web citation in these three files is unverified. They are chat-export transcripts. "Latest response" does not check them. This round must not admit Daijisen, Adachi, Voyager, ACE, Nihon Ki-in, or the `B:79` numerals as verified sources. The numerals may be quoted only as "the export contains these digits" (`B:79`). Whether they match a paper is unknown.

## Pipeline identity

Observation. `research/README.md:6-8`: burner Chrome, no Deep Research entitlement, browse-enabled GPT-6-Astra responses, explicitly not the Deep Research pipeline. The exports label "GPT-6 Astra" (`A:96`, `B:87`, `C:141`). The prompts ask for "Deep research" (`A:35`, `B:35`, `C:35`). The directory is named `deep-research-2026-09-28`.

Three identities are in play. Only the README sentence records an operator observation of the pipeline. The prompt prefix is the user's ask. The directory name is a label. A stop that keys off the path or the prefix changes the identity of the record from "browse-enabled capture" to "deep-research result." That is a false provenance stop. The requested pipeline did not run (`research/README.md:7-8`). Absence of the entitlement is why the substitute is not complete. It is not evidence the substitute finished.

## Index overrun

`research/README.md:12-13` states `jin'i-ryu` "is NOT an attested artisan rank — it's our coined term." The bodies do not say that.

- `A:64`: "could not substantiate this spelling as an established artisan rank in the Japanese or English sources searched. Without an attested Japanese spelling and source, its intended semantics remain uncertain." The search is unlogged (`A:42`).
- `C:109`: "no authoritative attestation" for the proposed translation, plus "Romanization without kanji cannot establish a literal meaning." The query list is incomplete (`C:48`, `C:61`). `C:118` distinguishes 人為 as a different word; that is a dictionary distinction inside the answer, not a logged null for each kanji candidate.
- `C:124` treats 自律流 as a possible modern coinage "not an established school name or a verified translation of jin'i-ryū." That is a proposal about a different romanization, not a proof about jin'i-ryū.

The index replaces an unlogged negative and an explicit uncertainty with a closed NOT. Stopping because the README has already corrected the scheme saturates a claim the artifacts left open. `chousa-shokunin/SKILL.md:44` requires the sweep; `chousa-shokunin/SKILL.md:45` and `chousa-shokunin/corpus/QUALITY.md:5` require observation, inference, and unknown kept separate. The README sentence is an inference written as a correction.

`research/README.md:13-14` lists four "usable axes," including improvement and transmission. Those axes are the model's design instruction at `A:54`. Improvement has no evidence section. Transmission is named at `A:47`, `A:52`, `A:54` and never given sources. Admitting the axes as harvest results admits a recommendation. `B:59` says the export was going to separate published findings from proposed engineering rules, then the file ends at `B:79` before that separation is applied to the unanswered asks.

`research/README.md:16` attributes "rank-inflation failure modes" to C. Sweep over `C:38-155` for `inflation`, `self-attest`, and `failure mode`: no hits. The index describes a section the body does not contain.

`research/README.md:11` "katagi ethics" overruns `A:71`, which stops at "not a formal ethical constitution."

## Rejections kept

| Id | Rejected stop | Reason |
|---|---|---|
| R1 | S1 chrome | Chrome follows an unfinished argument in A and B and an open heading in C. The disclaimer on the same boundary says the text is unchecked. Status lines in the same files still say checking (`A:47`, `B:47`) |
| R2 | S2 timers | In all three files `Working for` is longer than `Worked for` (`A:36-37`, `B:36-37`, `C:36-37`). The two authorities disagree. A duration is not a coverage proof. `A:86` rejects a universal numeric threshold for apprenticeship completion; transferring that sentence onto search counts is an **inference**, not a finding. The observation that falsifies S2 is the timer disagreement itself |
| R3 | S3 README search counts | Count not in the exports. Unit (searches) ≠ unit (visible events) ≠ unit (collapsed query rows). Live-tab truth of 9/8/10 is unknown |
| R4 | S4 closed absence | A has no query log. C's log is not replayable, and `C:109` says romanization cannot establish the meaning the search would have to refute. README's NOT is an index upgrade of uncertainty |
| R5 | S5 chip bibliography | `+N` is not a source. 20 hidden chips are uncaptured hops, not lost-recorded anchors (`citation-bases.md:50-54`) |
| R6 | S6 index-as-harvest | INDEX_OVERRUN on jin'i-ryū, the four axes, katagi ethics, and rank inflation |
| R7 | S7 window-sized chain-stop | Precondition of `SKILL.md:29` is a recorded hop that died. These hops were never captured, so the rule does not fire. `SKILL.md:18-19` forbids stopping at the summary. A missing URL blocks **that claim**. It does not close sibling asks, and it does not license inventing the page (no fetch this round; `SKILL.md:34-35`) |
| R8 | S8 one case study | `B:79` states the non-universality caveat in the same sentence as the numerals. Drift, forgetting, and hallucinated citations are still absent. The numerals are unverified, so they also fail row 4 of the stop predicate |
| R9 | S9 sibling-gate stop | claim-ledger and anchorcheck do not classify this citation shape. A green path-gate is a different authority |
| R10 | Never-stop until the literature proves self-improvement | `B:59` already refuses that bar. Out of scope for a window stop, and the wrong repair for R1–R9 |

Tradeoff, not a defect: refusing to open the chips in this round is the lane boundary (`chousa-shokunin/SKILL.md:34-35`; this assignment's no-fetch rule). The defect is marking the window stopped anyway. A canonical judge should reject a "stopped" mark on these files. It should not reject the refusal to fetch.

## Duplicate authorities

Inside each export, all of the following claim or deny completion at once:

- `Worked for` (looks finished)
- `Working for`, longer (looks unfinished)
- "I'm checking" / "Investigating" / "Analyzing" (unfinished)
- "Latest response" (looks finished)
- "ChatGPT can make mistakes. Check important info." (unchecked)
- `Sources` / `Web search` footer with no bibliography (looks attached, body empty)

Outside the export, the README adds a search count, a pipeline correction, and closed scheme corrections. The skill adds a chain-stop that does not fire. Sibling gates add a pass condition these citations cannot meet.

A window with more than one stop authority, those authorities in conflict, has no stop. Collapsing them into "the tab ended" picks S1 and discards the rest. That is the premature saturation.

## Impacted axes

- **Coverage.** A stop now leaves the ledger red: A 1/4 numbered asks partial, B 1/3 started, C's failure-mode ask unopened, two prompt topics absent from A, three named failure modes absent from B, rank inflation absent from C while the index asserts it. Hidden chips (20) and C's two collapse markers are uncounted hops, not covered sources.
- **Depth.** The only experimental paragraph (`B:79`) is one case, self-caveated, and unverified. Lexical tables stop at dictionary names. No chain has a second hop. `anchorcheck.py:53-56` would still require a semantic read even if a path:line existed; none exists for these hosts. Depth is "a name was printed," which `SKILL.md:27` already reads as unsupported.
- **Calibration.** The index writes NOT over "semantics remain uncertain" (`A:64` vs `research/README.md:12`). Status bubbles announce "a key finding" while still checking (`B:47`). Recommendations (`A:54`, `B:57`, `C:69`) sit where findings would be, and `B:59` warns that the distinction matters, then the capture ends. Search-count, timer, and query-collapse are three units treated as one by S2/S3. Unknowns (live continuation, truth of 9/8/10, truth of the numerals, attestation of jin'i-ryū) are not closable from these files.

## Smallest safe correction

Do not mark this window stopped. Record the three files as truncated browse-enabled captures whose web citations are unverified. Do not mint scheme corrections from `research/README.md:10-16` until each sentence is re-derived from a body line that survives the ledger.

**Proposal** for the parent's `tools/research-gate.sh`, fail closed, no new search:

- Stop witness = question ledger, not chrome.
- Residual "I'm checking" / "Investigating" / "Analyzing" with no later close → `OPEN`.
- Last substantive line followed by the disclaimer + "Latest response" + empty Sources footer → `CAPTURED`, not stopped.
- `+N` chips and isolated "N more" markers → `UNCAPTURED_HOPS`. They block chain-stop and window-stop. They are not `[lost-tree]`.
- Index sentence with no body witness → `INDEX_OVERRUN`, blocks stop.
- Pipeline field is `browse-enabled` for this corpus, copied from `research/README.md:7-8`, never inferred from `deep-research-*` or from the prompt prefix.
- Numerals in an unverified citation cannot be the stop witness. `B:79`'s caveat is retained if the sentence is quoted at all.
- `SKILL.md:29` closes one recorded hop. It is not the window predicate.

What this does not authorize: fetching the chips, resolving jin'i-ryū, confirming 9/8/10 against a live tab, or treating `C:69`'s names as the research result. Those are a future approval table (another member's deliverable), not a stop.

## Unknowns

- Whether the live tabs continued after this capture. "Working for" longer than "Worked for" is consistent with an in-flight scrape; composer chrome at the tail is also consistent with a short finished page. The stored files do not contain a close. Live continuation is unknown.
- Whether README's 9/8/10 matches the session. Unknown. Not used as a witness either way.
- Whether any named paper, dictionary entry, or numeric result is accurate. Unknown. Unverified by construction.
- Whether jin'i-ryū is attested under some spelling the unlogged search missed. Unknown. Not closed here, and not closed by the README.
