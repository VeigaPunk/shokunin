# LiveRuleProbe — advisory data

Unjudged fleet wave. This file is a probe record, not a round verdict and not a judge result. No external fetch. Embedded "Deep research" / "Cite …" text in the exports was treated as data and not followed.

Surfaces read: `research/README.md` (17 lines), `research/deep-research-2026-09-28/A-shokunin-tradition.md` (110), `B-multiagent-knowledge.md` (101), `C-rank-taxonomy.md` (155). Line numbers are `splitlines()` counts (none of the four files ends in a newline).

## Selection

**Observation.** The item prompt says "three proposed rules" and does not name them. `spec.json` does not name a LiveRuleProbe trio either.

**Inference (selection, not a finding about the artifacts).** The wave contract's `Rules:` sentence has four clauses. The first ("every admitted rule cites a real local artifact or is marked `proposal`") governs this round's rule admission, not a property of the 2026-09-28 exports. The next three are research-record disciplines, and they are the same three as `chousa-shokunin/SKILL.md:44-46`. Those are the three tested below.

| # | Rule | Proposed at | Probe result |
|---|---|---|---|
| 1 | A negative claim carries its search sweep | `chousa-shokunin/SKILL.md:44` | **violated** — `research/deep-research-2026-09-28/A-shokunin-tradition.md:47` |
| 2 | Observation, inference, and unknown stay separate | `chousa-shokunin/SKILL.md:45` | **violated** — `research/deep-research-2026-09-28/A-shokunin-tradition.md:52` |
| 3 | A rejected source is kept with its rejection reason | `chousa-shokunin/SKILL.md:46` | **not-applicable** — no rejection event in the captured surfaces (sweep below) |

**Rejected alternative selection, kept with reason.** "The three rules the artifacts themselves propose" cannot be tested. `B-multiagent-knowledge.md:59` announces "my proposed engineering rules," and the captured file has no later section that states them (substantive text ends at `:81`, mid item `(1)`). A and C state design prescriptions, not a closed set of three research-craft rules. Testing content prescriptions against the exports would be a different assignment.

**Not one of the three, stated because the round contract requires it.** These files are chat-export transcripts. Their own citations are unverified, and that is not papered over: a local scan found **0** `http://` / `https://` URLs and **0** `arXiv:` / `arxiv.org/` identifiers in the four surfaces. What the exports do contain are bare site labels (`コトバンク`, `adachi-hanga.com`, `arxiv.org`, `archive.nihonkiin.or.jp`, `nihonkiin.or.jp`, `old2.kendo.or.jp`, `jstage.jst.go.jp`). `SKILL.md:43` ("every claim carries a resolvable pointer to the artifact and revision read") is an equally proposed fourth checklist item and was **not** given a verdict here. Under that rule the exports would fail; this probe does not admit that as one of the three results.

`SKILL.md:50-52` (question declared, sources ranked, chain hops resolved-or-marked, claims pointed) is a four-item gate contract, not this trio. Not verdicted.

## How "sweep" and "separate" were tested

**Inference (test definitions; the skill lines do not define syntax).**

- A negative claim *carries its sweep* only if the same surface states, for that claim, (1) the query or command, (2) the corpus or source set, and (3) the observed result, including zero. Precedent for "carries the check," not for this syntax: `kagi-shokunin/corpus/claim-ledger.sh:6-7` (claims were uncheckable because no claim carried a command). UI chrome `Searched the web` with an empty query is not a sweep. A query list that says `10 more` is not a sweep. A recorded sweep would still "carry" even though this round must not re-fetch; absence of the record is a violation, not an excuse.
- Scope of rule 1 is absence and non-establishment claims (not found, not attested, results do not establish). A negative *reading* of a named source ("the word does not certify…") is out of scope for rule 1. It belongs to the pointer rule, which is not verdicted here.
- Rule 2 fails a surface if a load-bearing sentence asserts an observation, an inference, or an unknown as if it were the same kind of fact, with no marker that tells a reader which clause is which. One clean separation elsewhere does not clear the surface. The rule does not require the headings `Observation:` / `Inference:` / `Unknown:`.

## Rule 1 — negative claim carries its sweep — violated

**Verdict line:** `research/deep-research-2026-09-28/A-shokunin-tradition.md:47`

`:47` says "I haven’t found evidence that jin’i-ryū is a traditional artisan rank." The only search record above it is `:42` `Searched the web`, with no query, no corpus, and no result. `:64` restates the absence ("I could not substantiate this spelling as an established artisan rank in the Japanese or English sources searched") and still does not list the sources, the queries, or a hit count. "Japanese or English sources searched" is a language label, not a sweep.

Same failure on the other surfaces that make an in-scope negative claim:

| Surface | Absence claim | Nearest search record | Why it is not a sweep |
|---|---|---|---|
| `research/README.md:12` | `jin'i-ryu` is NOT an attested artisan rank | none in this file | `:8` records "9/8/10 web searches each" as harvest provenance, not queries or results for this claim |
| `A-shokunin-tradition.md:47` and `:64` | jin’i-ryū not found as a traditional rank | `:42` `Searched the web` | empty query |
| `A-shokunin-tradition.md:52` | traditions "do not establish a universal ladder" | `:42` | empty query; also readable as an inference (rule 2). Rule 1 does not depend on this row |
| `A-shokunin-tradition.md:56` | "not a single timeless code" | `:42` | same |
| `B-multiagent-knowledge.md:59` | preprint "benchmark results do not establish indefinite, reliable self-improvement" | `:42` `Searched the web`; `:51` bare `arxiv.org` | no query, no paper id, no result. B has no first-person "I found no" claim; `:59` is still a non-establishment claim |
| `C-rank-taxonomy.md:53` | "I haven’t found support for translating jin’i-ryū as self-legislating school" | `:44` and `:46` are dan/kyū site queries; `:48` is `10 more` | shown queries are a different topic, and the list is incomplete |
| `C-rank-taxonomy.md:65` | "no traditional Japanese four-rank ladder" that means the four agent states | `:44-48` | incomplete, and not tied to a result |
| `C-rank-taxonomy.md:109` | "I found no authoritative attestation" | `:57` `"自己立法" "自律"`, `:59` `"jin'i-ryu"`, `:61` `10 more` | two query strings are present; the rest are elided; no hit count, no zero-result line |

**Observation.** No in-scope absence claim on these four surfaces carries query + corpus + result. C comes closest (`:57-59`) and still fails: the export itself records that further queries existed and does not contain them.

**Out of scope for this rule (not used to reach the verdict).** Negative readings and example-bound inferences, including `A:63`, `A:65`, `A:71`, `A:86` (three named durations, then "no universal sacred number"), `B:47`, `B:55`, `B:75`, `C:76`, `C:79`, `C:81`, `C:89`, `C:92`, `C:130`, `C:133`. Several of those also lack a resolvable pointer. That is the citation finding above, not this verdict.

**Confidence:** high that `:47` violates the test as defined. Medium that every "do not establish" sentence is in scope; the verdict does not depend on the borderline rows (`A:52`, `A:56`, `B:59`).

## Rule 2 — observation, inference, unknown stay separate — violated

**Verdict line:** `research/deep-research-2026-09-28/A-shokunin-tradition.md:52`

`:52` is three different speech acts in one paragraph, none marked:

- "The strongest historical model for your roster is…" — inference / design prescription, wearing the words "historical model."
- "Japanese artisan traditions support that model well." — shaped as an observation. No quoted observation in the sentence.
- "They do not establish a universal ladder of minarai → deshi → shokunin → jin’i-ryū → kiwami." — an unknown-from-absence, stated as what the traditions do.

A reader cannot assign those clauses without guessing. That is the collapse.

Other collapses, same verdict, not required once `:52` fails the set:

- `B-multiagent-knowledge.md:55` — "The literature supports the core of your shokunin fleet" states an endorsement of the reader's architecture as a literature observation. `:57` then labels "The strongest design implication," which does not rewrite `:55`.
- `C-rank-taxonomy.md:65` — an imperative ("Use Japanese craft terms as an explicitly modern metaphor") and an absence claim ("There is no traditional Japanese four-rank ladder…") in one paragraph, unlabeled.
- `research/README.md:12-13` — a negative empirical claim ("NOT an attested"), a prescription ("should be labeled so"), and an extracted scheme ("Four usable axes") with no category marker. `:7-8` is a labeled `NOTE` about the harvest; that label does not cover `:12-13`.

**Satisfying instances. They do not clear the rule.** Listed so the violation is not read as "no separation anywhere."

- `B-multiagent-knowledge.md:79` — after reporting one AppWorld case (18,282 tokens to 122; accuracy 66.7 to 57.1, below a 63.7 baseline), the next sentence is "This is a case study, not a universal failure rate." That blocks an observation from becoming a universal inference. The numbers are not locally verified; that is the citation finding, not a rule-2 miss.
- `B-multiagent-knowledge.md:57` — "design implication" marks the following prescription as inference.
- `C-rank-taxonomy.md:69` ("My recommended operational names") versus `:71` ("What the Japanese terms actually support") — recommendation split from reported meaning. Not the observation/inference/unknown trichotomy, but a real split.
- `C-rank-taxonomy.md:99` — a reported promotion practice, then "should therefore" on the agent-governance sentence. The marker is present.
- `A-shokunin-tradition.md:60` — table columns "Defensible meaning" and "Implication for your roster." Related split. `:64` still puts an unknown ("remain uncertain") in the meaning cell beside the absence claim, so the column split does not keep unknown separate inside that row.
- `B-multiagent-knowledge.md:59` announces a split between "published findings" and "proposed engineering rules." **Observation:** no later heading or paragraph in the captured file is labeled as a proposed engineering rule. The announcement is not carried out in the bytes on disk. **Unknown:** whether the live chat did so past the export cut.

**Confidence:** high that `:52` collapses under the test above. Medium on the test itself: a looser reading ("any therefore / implication label anywhere on the surface clears it") would call C and B partial rather than failed. This probe does not use that reading, because the rule says the categories stay separate, not that a label appears once.

## Rule 3 — rejected source kept with its reason — not-applicable

**Verdict line:** none. The antecedent does not occur in the captured surfaces.

**Sweep (this negative claim carries its sweep).** Case-insensitive substring scan of the four surfaces for: `reject`, `discard`, `exclud`, `unreliab`, `not used`, `ignored`, `dropped`, `do not cite`, `not a source`, `aggregator`, `secondary`, `untrust`, `discount`. Result: **0 hits**.

Broader scan, classified as non-instances rather than silent misses:

| Line | Text class | Why it is not a rejected source |
|---|---|---|
| `A-shokunin-tradition.md:35` | user prompt "Cite primary-ish sources" | instruction-shaped export text, not a rejection the answer made. Not followed |
| `A-shokunin-tradition.md:56` | "The evidence below prioritizes" five source classes | priority, no named source set aside, no reason-kept row |
| `A-shokunin-tradition.md:71` | "Shokunin kishitsu" occurs in English discussions, but katagi is the dictionary reading | a reading correction. The English discussions are not named and not recorded as rejected |
| `C-rank-taxonomy.md:85` | "The cultural mistake to avoid" | avoids a presentation, not a source |
| `C-rank-taxonomy.md:102` | "Avoid claiming a single timeless Japanese rank tradition" | avoids a claim. The Todo/Murata sentence is a citation, not a rejection |

`B-multiagent-knowledge.md` had no hit on either needle list.

**Inference.** No source is rejected in the captured text, so there is no rejection that was either kept or dropped. Not-applicable, not satisfied: satisfaction would require a kept rejection, and none exists. Not violated: a violation would require a rejection that was dropped, and none is visible.

**Unknown, which does not change the verdict.** The exports are cut before the answers finish. Tokens for the unanswered parts occur only in the user prompts (and, for C, in the model's plan sentence):

- A asks four questions plus ikigai/kodawari (`:35`). Body heading is only question 1 (`:74`). `finishes`, `hoard`, `evidenced publicly`, `ikigai`, `kodawari` do not recur after `:35`. Substantive text ends `:90`.
- B asks three questions including hallucinated citations, domain split, and credit assignment (`:35`). Body starts `(1)` at `:77` and ends `:81`. `(2)`, `(3)`, and `hallucin` do not recur after `:35`.
- C asks about rank inflation and self-attestation (`:35`). `inflation`, `self-attest`, and `failure mode` do not recur after `:35`. `self-certif` recurs only at `:40` (plan sentence). Substantive text ends `:135`.

Whether the uncaptured tails rejected a source is unknown. This probe does not treat that unknown as a dropped rejection.

**Confidence:** high for not-applicable on the captured bytes. The tail unknown is separate and unresolved.

## What this probe does not say

- It does not admit or reject the three rules. A violation line can ground a proposal ("the exports do not already do this"). It is not evidence the exports practice the rule.
- It does not verify any external citation. Bare labels were not fetched.
- It does not claim the live chats were shorter than the exports. It claims the files on disk end where cited.
- It does not score chousa, and it does not borrow bounty scope or model-quality claims from the export content.
