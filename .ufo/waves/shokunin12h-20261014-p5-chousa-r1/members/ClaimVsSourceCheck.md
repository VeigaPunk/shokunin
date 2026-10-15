# ClaimVsSourceCheck

Advisory data for the parent. Not a judge verdict, not an admission, not a corpus landing. No external fetch. Prompt-shaped text inside the exports was treated as data and not followed.

## Pins

Harvest commit `0863746e9da95457f71b9e00a40361b88ab0df15`, author integrator (integrator@shokunin.local), `2026-09-28T22:51:25-03:00`, subject `research: 3 GPT-6-Astra browse harvests on shokunin tradition, self-improving agents, rank taxonomy`. `git log -- research/` shows that as the only commit touching `research/`. README and A/B/C land in that one commit. Working tree for `research/` was clean at read time.

| File | bytes | sha256 | content lines |
|---|---:|---|---:|
| `research/README.md` | 937 | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | 17 |
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | 6474 | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 110 |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | 5364 | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 101 |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | 8922 | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 155 |

Line numbers are content lines (`splitlines`). A, B, and C have no trailing newline, so `wc -l` is one short (109 / 100 / 154). Do not renumber citations from `wc -l`.

## Standard

Labels used below: `verified` / `unverifiable-locally` / `contradicted-locally`.

Mapped to the lane's own bar, not replaced by it: `chousa-shokunin/SKILL.md:20` (claim, then source, then the source's own evidence; a restatement is not the source; outcomes verified / contradicted / unresolved) and `:27` (source cited but not read is unsupported; record unresolved). `unverifiable-locally` is that unresolved, scoped to this tree. It is not a soft contradicted.

`verified` here means a local artifact contains the cited source's own text and that text supports the claim. Same-commit chrome agreeing with the README is corroboration inside one harvest, not an independent source. Arithmetic among numerals printed in the claim is not the experiment. Parametric knowledge was not used as a source. Browser profiles and CDP were not opened (session material; shape-only).

Observation, inference, and unknown are marked as such. A negative claim carries the sweep that was actually run.

## Sweep (what was opened)

- Full read of the four harvest files.
- Fleet-repo walk of `*.md`, `*.txt`, `*.py`, `*.sh`, `*.json`, `*.tsv`, excluding `.git` and `.ufo`, for the distinctive strings named under each claim.
- Live rank gloss: `PROTOCOL.md:21`, `:35-36`, `:76-78`.
- Precedents, as evidence of what the fleet already enforces, not as a web-source gate: `kagi-shokunin/corpus/claim-ledger.sh` (`docs` at `:53-65`, `cite_class` at `:429-449`), `kasegi-shokunin/corpus/instruments/anchorcheck.py:4-20` and `:53-61`, `kasegi-shokunin/corpus/knowledge/citation-bases.md:9-80`.
- Executed, read-only: `anchorcheck.py` on A, on B, and on README; `claim-ledger.sh citations --docs` on all four harvest files. Outputs under "Gate counterexample".

Surface correction, not one of the five: the spec names `kasegi-shokunin/corpus/instruments/citation-bases.md`. That path is absent. The file is `kasegi-shokunin/corpus/knowledge/citation-bases.md`. `corpus/instruments/` holds `citation-survival.md`, not `citation-bases.md`.

Not opened: the hosts named in the exports (Kotobank, adachi-hanga.com, arxiv.org, archive.nihonkiin.or.jp, jstage.jst.go.jp, kendo.or.jp, and the JKA name with no URL). Any rule that needs those pages is `proposal`.

## CVS-1 — 職人気質 is read katagi, not kishitsu

**Claim.** `A-shokunin-tradition.md:47` and `:71`: 職人気質 is normally / conventionally read shokunin katagi; "shokunin kishitsu" occurs in English discussions, but katagi is the dictionary reading; the meaning includes pride in skill, earnestness, painstaking work, and, in another definition, apparent stubbornness and disregard of profit; it names a disposition, not a formal ethical constitution. `research/README.md:11-12` adopts this as a correction for the scheme.

**Source the claim appeals to.** `A:67-69` and `A:72`: Daijisen, Nihon Kokugo Daijiten, Kanjipedia, then the bare label コトバンク and `+3`. No URL, no headword entry, no quotation. `A:71` says another definition "explicitly includes" stubbornness and disregard of profit. "Explicitly" asserts a quotation-level match. The quotation is not in the file.

**Local sweep.** 職人気質, Daijisen, Kanjipedia, and `shokunin katagi` occur only in this harvest (A, and the README restatement). No dictionary text elsewhere in the walked tree. The string `kishitsu` in `A:35` is the user's question, not a source. `README.md:11-12` restates A. A restatement is not a second source (`SKILL.md:20`).

**Verdict: unverifiable-locally.**

Nothing local says the reading is kishitsu, so this is not contradicted. Absence of a contradicting dictionary is not confirmation. Do not admit `README.md:11-12` as a scheme correction on the strength of `A:71`.

**Proposal, not admitted.** A local copy of the cited entry, with the headword and the reading, would be the source's own evidence. That copy is not in this tree. Fetching it needs an approved external window.

## CVS-2 — jin'i-ryu is not an attested artisan rank, and it is our coinage

Two claims are glued together in `README.md:12`. They do not share a verdict-bearing source, and neither verifies.

**Claim (a), historical negative.** `A:47`: no evidence found that jin'i-ryu is a traditional artisan rank. `A:64`: the spelling could not be substantiated as an established artisan rank "in the Japanese or English sources searched"; without an attested Japanese spelling and source, the semantics remain uncertain; treat it as the system's coined rank, not inherited Japanese terminology. `C:53` and `C:109`: no support, and "no authoritative attestation", for translating jin'i-ryu as "self-legislating school." `C:118` offers 人為 as a gloss (human action, not self-legislation). `C:124` offers 自律流 / jiritsu-ryu as a possible different coinage, "not an established school name or a verified translation of jin'i-ryu."

**Claim (b), authorship.** `README.md:12`: "it's our coined term and should be labeled so."

**Source (a) appeals to.** A's "sources searched", with no query list. A has one `Searched the web` label (`A:42`) and no queries. C's visible queries are for the translation question, not for an artisan-rank attestation: `C:57` `"自己立法" "自律"`, `C:59` `"jin'i-ryu"`, `C:61` a collapsed `10 more` (codepoints under the provenance rider). No result rows, no hit counts, no dictionary quotation. `C:120` says the dictionaries support the 自律 / 自立 / 人為 / 流 distinctions, then コトバンク and `+4`. No entry text. A negative with no recorded sweep in A, and a partial query list with no results in C. The lane requires a negative claim to carry its sweep (`SKILL.md:44`).

**Source (b) appeals to.** No coinage record. `PROTOCOL.md:21` glosses `jin'i-ryu (self-iterating)`. `:35-36` and `:76-78` define an operational gate. The live protocol does not say "coined", does not give kanji, and does not claim a Japanese attestation. Walk for `coined` outside `.git` and `.ufo`: `README.md`, A, and a later append in `chousa-shokunin/MINT.md`. Usage is not authorship. The later append is a restatement of these exports, not a coinage act.

A and C do not contradict each other. Both refuse an inherited-rank / literal-translation reading. `C:124` is a different romanization, and it says so.

**Verdict: unverifiable-locally** for (a) and for (b).

(a) is a search report whose results are not in the file. (b) is an authorship claim with no local act of coinage. "PROTOCOL does not call it traditional" does not prove this fleet coined it, and does not prove the historical negative.

**Smallest safe correction.** Do not copy `README.md:12` into a corpus fact. Do not relabel `PROTOCOL.md:21` from this check. The operational token can remain an operational token without a tradition claim — that is already what `:21` says. Adding a "coined" label would assert (b), which this check did not verify. Mark both `proposal`.

**Local mis-anchor, do not copy.** `chousa-shokunin/MINT.md:39-42` attributes to `C:109` the claim that jiritsu-ryu is not a verified translation. `C:109` does not say that. It is about jin'i-ryu as "self-legislating school." The line about 自律流 is `C:124`, and it says that coinage is not a verified translation of jin'i-ryu. `C:109` is the wrong anchor for the jiritsu sentence.

`C:118`'s 人為 gloss is a separate positive lexical claim with the same defect as CVS-1 (name-drop, no entry). Not verified. Not a contradiction of (a).

## CVS-3 — Adachi: about seven years for carvers, five for printers

**Claim.** `A:80`: Adachi's own account gives customary apprenticeship periods of approximately seven years for carvers and five for printers. Cast with it, and used for the conclusion: `A:81` Ishii Torao, nine years as a disciple before independent establishment; `A:82` Echigo Yoita, a program aiming for independence within five years. Conclusion `A:86`: there is no universal sacred number of years or common final examination.

**Source the claim appeals to.** `A:83-84`: the bare domain `adachi-hanga.com` and `+2`. No URL path, no quote, no date. The `+2` companions are unnamed. Ishii and Echigo have no pointer at all. Zero `http` in A.

**Local sweep.** `adachi-hanga`, `Adachi`, `Ishii Torao`, and `Echigo Yoita` each occur in exactly one walked file: A. No page text.

**Inference, not a second verdict.** `A:76` says finishing an apprenticeship, becoming a competent artisan, and establishing an independent practice should not be collapsed into one event. `A:80` is a term length. `A:81` is years before independent establishment. `A:82` says the timetable also reflects the duration of financial support. On the file's own distinctions, the three numerals are not one measurement. They do not establish `A:86`. They also do not contradict `A:86`: no local source asserts a universal term either. Non-probative is not contradicted.

**Verdict: unverifiable-locally** for `A:80`, and **unverifiable-locally** for `A:86`.

Same citation shape, not separately scored: `A:88` (Takenaka Carpentry Tools Museum, Ogawa Mitsuo, Nishioka Tsunekazu) has no URL and no quotation.

**Unknown, not a negative about the tradition.** The user asked four questions (`A:35`). The saved response answers (1) only in part and stops at `A:88`, then the disclaimer (`A:90`) and `Latest response` (`A:91`). `hoard`, `ikigai`, `kodawari`, and `public` occur only in `A:35`. `finish` in the body is `A:76` "finishing an apprenticeship", which is not question (2), whether a master ever finishes. Whether the live tab continued past this cut is unknown. Absence in this cut is not a finding that the tradition is silent on (2), (3), or (4).

## CVS-4 — ACE AppWorld rewrite: 18,282 tokens to 122; accuracy 66.7 to 57.1 vs 63.7

**Claim.** `B:79`: in one AppWorld case, a rewrite reduced accumulated context from 18,282 tokens to 122; accuracy fell from 66.7 to 57.1, below the 63.7 no-adaptation baseline. The same sentence hedges: this is a case study, not a universal failure rate.

**Source the claim appeals to.** `B:67` "ACE, Zhang et al., 2025" with no title. `B:71-73` names ACE among sources, then `arxiv.org` and `+6`. `B:51` `arxiv.org` sits in the progress chrome between narration blocks; it is not a paper link. Zero `http`, zero `doi`, zero arxiv id in B.

**Local sweep.** Punctuated `18,282` occurs once in the walked tree: `B:79`. `context collapse` once: `B:79`. Unpunctuated `18282` occurs in game-dev telemetry files; those files are not this case (no ACE, no AppWorld). `66.7` is a common numeral in lane telemetry; those hits were not treated as corroboration and were not chased as a paper.

**Observation, not an upgrade.** 57.1 is less than 63.7, which is less than 66.7. The inequality among the printed numerals holds. That does not verify the experiment.

**Adjacent claim, separately unverifiable.** `B:77` says the most important self-rewrite failure is losing the distinction between observation, interpretation, and established knowledge. `B:79` does not say the ACE case is evidence for that distinction. The citation does not transfer across the paragraph break. Do not hang `B:77` on `B:79`.

**Province, if a later window ever verifies the numerals.** The figures are benchmark-shaped. This lane refuses model-quality claims (`chousa-shokunin/SKILL.md:38`, `PROVINCE.md:10-11`). Admitting 66.7 / 57.1 / 63.7 as a finding about a model would be out of province even after a source check. The only method residue the file itself allows is the hedge already in `B:79`: one case of destructive compression, not a universal rate. That residue is still unverified here. `B:59` (benchmark results do not establish indefinite, reliable self-improvement) is the model's own limit statement, not a sourced result.

**Verdict: unverifiable-locally.**

Not separately scored, same class: the author-year rows at `B:64-69` (Voyager, Generative Agents, Reflexion, Dynamic Cheatsheet, ACE, Memento-Skills, LEGOMem) have no ids, no URLs, and no paper text. `B:64`'s claim that Voyager's verified code library differs substantially from freely rewritten factual prose is unverifiable-locally on this tree.

**Unknown, not a negative about the literature.** Last `ChatGPT said:` is `B:53`. The delivered body stops at `B:79`, then the disclaimer (`B:81`). Prompt questions (2) split-vs-expand and (3) credit assignment are not answered there. `B:47`, in the progress block before `B:53`, states that team success does not establish which specialist actually improved, and that domain-splitting evidence is still being checked. That is a claim-shaped sentence in progress chrome, with no paper attached. It is not a delivered, sourced answer. `hallucin` occurs only in the prompt (`B:35`): the named failure mode "hallucinated citations" is not in the answer. Whether the live tab continued is unknown.

## CVS-5 — README says C contains rank-inflation failure modes

**Claim.** `research/README.md:16-17`: `C-rank-taxonomy.md` is craft rank vocabularies plus rank-inflation failure modes for self-certifying agents.

Class I: the source is the named file. The README indexes the files (`README.md:3`, indexed by date dir), so the bullet is a claim about the saved artifact, not about an unsaved continuation.

**Sweep of C, all 155 content lines.** `rank inflation`, `inflation`, `self-attestation`, and `failure modes` occur once each, all inside the user prompt `C:35`. The delivered response, after the last `ChatGPT said:` at `C:63`, contains no `inflation`.

Closest delivered sentences, which are not that catalog:

- `C:93`: rank is conferred through a procedure, not established by a practitioner's self-description. A self-attestation fragment. Its own cite is the JKA name at `C:93` with no URL and no quotation, so that JKA sentence is itself unverifiable-locally. It is not a rank-inflation analysis.
- `C:105`: arbitrary kyu/dan labels would add apparent precision without a calibrated skill scale. False precision, not inflation.
- `C:126` and `C:130`: engineering cautions about "self-legislating" and about reading ri as outgrowing safety constraints. Not a rank-inflation catalog.

The file ends inside "Other tempting metaphors" (`C:128-133`), then the disclaimer (`C:135`) and `Latest response` (`C:136`). The Sources panel (`C:153-154`) is the labels `Sources` and `Web search` only.

**Vocabulary half, scoped.** The term table and the sections after it are in the file (`C:73-79` and following). As a claim that the saved file contains craft-rank vocabulary, that half is **verified** (Class I, presence only). It does not verify the dictionary meanings: `C:81-83` names Daijisen and Nihon Kokugo Daijiten, then コトバンク and `+5`, with no entry text. Those meanings stay unverifiable-locally, same defect as CVS-1.

**Verdict: contradicted-locally** for the rank-inflation constituent of `README.md:16-17`.

Counting `C:93` or `C:105` as the catalog would be a false verification. They are different claims, and one of them is itself unsourced.

**Unknown, not a world-negative.** Whether the live tab continued past this cut is unknown. This verdict does not say the literature lacks rank-inflation failure modes. It says the saved file, which the README indexes, does not contain that analysis.

## Not one of the five — recorded so they are not laundered

### README provenance (`README.md:6-8`)

Asserts: burner Chrome, CDP 9222, fired 2026-09-28 by L0, no Deep Research entitlement, browse-enabled GPT-6-Astra responses, 9/8/10 web searches each, not the Deep Research pipeline.

What the dumps contain, and do not:

- The chrome line `GPT-6 Astra` is at `A:96`, `B:87`, `C:141`. UI words consistent with a ChatGPT web capture (`ChatGPT`, `jpveiga`, `Pro`, `Work`) are in the headers. Observation: the saved chrome says that. It is not an independent provider record.
- A, B, and C contain no `9222`, no `entitlement`, no `L0`, no `9/8/10`, and no date.
- `Deep research:` at `A:35`, `B:35`, `C:35` is the user's request prefix, not a pipeline badge.
- Captured `Searched the web` labels: `A:42` once, `B:42` once, `C:42` and `C:55`. That is 1, 1, and 2 event labels in the cut. It is not a recorded search total.
- `C:48` and `C:61` are U+2068, `10`, U+2069, space, `more`. Measured codepoints, not inferred. A bidi-isolated collapsed-list widget, present twice. Reading it as confirmation of "10 web searches" is a false verification.
- Dual timers in every file: `A:36` `Worked for 1m 33s` and `A:37` `Working for 2m 9s`; `B:36-37` 1m 36s and 2m 8s; `C:36-37` 1m 11s and 2m 7s. The chrome is not a clean measurement log.

The commit message restates "GPT-6-Astra browse harvests" and the commit timestamp is 2026-09-28. Author is integrator, not a recorded L0. Same-commit corroboration of a harvest date and a model label. No conversation id, no provider model id, no entitlement record in the tree. Browser profile not opened.

**Verdict: unverifiable-locally** for `README.md:6-8` as production facts.

**Rejected upgrade to contradicted.** 1, 1, and 2 captured event labels do not disprove a live-UI count that was not saved, and the query lists are collapsed. They also do not verify 9/8/10. Both upgrades are refused.

### Three axis lists, not one

Delivered bodies, all present as sentences, none verified against a source:

- `A:54` competence / independence / improvement / transmission
- `B:57` task competence / retention / evidence fidelity / cross-domain transfer / operating cost
- `C:67` knowledge provenance / demonstrated competence / authority to modify itself / authority to create other agents

`README.md:13-14` lifts only A's list and calls them "usable axes." Presence of the sentence `A:54` is verified as Class I presence. `A:52-54` is the model's design split. `A:56` says the evidence establishes particular traditions, not a single timeless code. Presence of `A:54` does not verify a tradition, and it does not make A's list the harvest's only list. Do not collapse the three lists into one method.

## Gate counterexample

The fleet's existing citation gates false-clean this harvest. A research gate that only shells out to them will admit name-drops.

Executed:

- `python3 kasegi-shokunin/corpus/instruments/anchorcheck.py` on A, on B, and on `research/README.md`: each printed `0 in-range cite instances, 0 bad; 0 distinct anchors` and exited 0.
- `bash kagi-shokunin/corpus/claim-ledger.sh citations --root kagi-shokunin --docs` the four harvest files: `CITATION_GATE: CLEAN (cites=0 docs=4 unresolved=0 ephemeral=0 labeled=0)`, exit 0.

Why that is not a pass:

- `anchorcheck.py:4-7` and `:53-61` only see backtick path:line tokens. Range-valid is mechanical; semantic support is a separate review. Here there is no token to review. Exit 0 with zero cites is a vacuous pass.
- `claim-ledger.sh:430`: anything outside the checked path shapes is "a reference, not a path." `cite_class` (`:442-449`) returns failure for every other token, and `citations` then skips it. Bare コトバンク, `arxiv.org`, `adachi-hanga.com`, `archive.nihonkiin.or.jp` are invisible. `cites=0` means the gate saw nothing it knows how to check.
- `docs` mode (`claim-ledger.sh:53-65`) allows exactly four by-hand classes: `control-plane-scratch`, `opencode-internal`, `interactive-only`, `vault-refusal`. None names "cited external source is not in the tree." Filing CVS-1..4 under one of those four would be a false classification. The round's mark for that case is `proposal`.
- `citation-bases.md:9-80` defines LANE, MIRROR, ORIGIN-WORK, LOST-TREE, LOST-BASE, BLOB-PIN. A web domain is not a base in that vocabulary. Those bases are also the wrong tool for this harvest: MIRROR and ORIGIN-WORK are recorded absent (`citation-bases.md:20-41`). Absence of a bounty mirror does not answer whether Kotobank says what A claims.

## Correction

Do not admit CVS-1, CVS-2, CVS-3, CVS-4, `README.md:6-8`, or the dictionary rows in C as corpus facts. Mark them `proposal`.

Admit only the Class I observations this check actually made: the four files are one truncated ChatGPT UI harvest in commit `0863746`; their Sources panels are labels with no URLs; their citations are name-drops (domain, `+N`, author-year, no quotation); `anchorcheck` and `claim-ledger.sh citations` both false-clean them; `README.md:16-17` overclaims C on rank inflation; `A:54` is a sentence in A, not a verified tradition, and not the only axis list in the harvest.

A research gate has to fail closed when a claim's cited source text is absent, including a bare domain, a `+N`, and an author-year with no local copy. A zero-cite CLEAN must not be a pass. Forcing these rows through `docs` by-hand classes would hide the gap the gate does not name.

## Unknowns kept unknown

- Whether any live tab continued past the cut (A ends at the Nishioka anecdote, B at the ACE case, C inside "Other tempting metaphors").
- Provider model id behind the chrome string `GPT-6 Astra`, entitlement, conversation id, and who fired the tabs. The commit records integrator on 2026-09-28. That is not those facts.
- Which kanji, if any, this fleet intended for `jin'i-ryu`. The tree does not say. `C:118` guessing 人為 is not a fleet record.
