# Source curation and evidence grading: critique and proposed contract

**Scope.** This is an evidence-backed critique of the draft `SOURCES.md` contract, not a lane-specific corpus admission. The source rows below are dossier-local IDs; allocate fresh lane-local IDs if any source is later added to a lane registry.

**Method and local evidence.** I searched before reading and then read only the relevant `chousa-shokunin` sections. `chousa-shokunin/SKILL.md` already specifies question → hierarchy → citation chain → claim check (lines 15–21), labels its primary > secondary > aggregator > unsourced ordering as a local construction rather than an external rule (lines 23–31), and requires resolvable pointers, search sweeps for negative claims, separated observation/inference/unknown, and retained rejections with a flip-condition (lines 54–59). `corpus/QUALITY.md` already requires falsifiable claims, measured anchors, separated observation/inference/unknown, append-only errata, and retained rejections (lines 3–7). The corpus index lists existing claim, chain, sweep/rejection, and reference-integrity work (README lines 8–14); its known-gaps section explicitly says those structural checks do not prove semantic support or a source's truth (lines 141–159). Reuse these surfaces; do not invent a second research method or imply a clean structural gate proves truth.

**Semantic-tool limitation.** I attempted `read xd://lsp`; the device is not mounted. I used `grep` only to locate the exact local sections and `read` to inspect their text. No semantic LSP result is claimed.

## Evidence-led critique of the draft

D01 — **Tier scope is missing.** “A primary/authoritative” and “B strong secondary” read as global properties of a source, not a judgment scoped to a particular claim. A primary source may be primary only for its own record, methods, or institutional position; it may not warrant unrelated claims. Add a `scope` field and state that a tier is assigned for that scope.

D02 — **Source class, source reliability, claim credibility, and evidence certainty are collapsed.** The current NATO-reproducing UK doctrine rates source reliability separately from credibility of the particular report; it says, “Reliability and credibility must be evaluated separately.” (JDP 2-00, §3.39(c), p. 69.) GRADE is different again: it rates certainty in the body of evidence by outcome, not a single source row or individual study. A/B/C must not masquerade as either scale.

D03 — **Primary does not mean proven.** SIFT/lateral reading asks who is behind a source, what independent coverage says, and whether a claim reaches its original context. The original CRAAP guide itself says criteria vary with the information need. Treat CRAAP as prompts, not a point score. A comparison study found a difference on one end-of-semester paper measure but inconclusive quizzes and cautioned against generalizing from its single-course setting; it does not prove that CRAAP is universally ineffective.

D04 — **The draft can duplicate chousa's method.** `SOURCES.md` should be a curated “where to learn” registry, not a second version of the existing question → hierarchy → chain → claim-check workflow, claim-verification gate, chain gate, or integrity check. The source hierarchy is chousa's local working standard, not an imported universal law.

D05 — **A title plus live URL does not preserve the source actually read.** The draft lacks an exact edition/revision and pinpoint anchor. The Perma study distinguishes link rot (no content at the URL) from reference rot (content changed while the URL still works); an HTTP 200 can still be a redirect, soft 404, or changed page. Pew's 2024 analysis separately documents decay in sampled pages and reference links, with its own conservative status-code definition. Store the exact section/version and, when possible, a verified archive pointer and capture date.

D06 — **Workflow state is ambiguous and rejection data are underspecified.** `watch` is a recheck cadence, not a mutually exclusive mining state; `rejected` currently hides its reason in `teaches` and omits chousa's required flip-condition. Separate source teaching from rejection rationale. Make corrections append new rows with `supersedes`; let `recheck` express watch cadence.

D07 — **No selection-flow account.** PRISMA 2020 reports records from identification through selection to included studies and asks authors to cite apparently eligible studies that were excluded and explain why (items 16a/16b). A source registry is not a systematic review, so do not claim PRISMA compliance; for a bounded sweep, a compact PRISMA-inspired run record still makes identified, screened, included, and excluded-with-reasons auditable. Keep unopened leads visibly separate.

D08 — **Counting rows is not validating a registry.** The draft's commands are useful for total/tier counts, but do not detect duplicate or skipped IDs, malformed rows, unresolved `used-by`/`supersedes` references, or whether an anchor supports a claim. Fix field positions to a stable schema and describe these as counts only—not a quality or semantic-validity verdict. Chousa's existing integrity gate itself resolves references but expressly does not establish semantic support.

## Source findings that shape the contract

- **NATO/Admiralty grading.** The directly readable UK MOD JDP 2-00, fourth edition (August 2023), calls the reproduced framework the NATO Intelligence Grading System/Admiralty Code. It pairs A–F source reliability with 1–6 information credibility, permits mismatched combinations (for example, its B5 and E1 examples), and says to review the grades as more information arrives. This is a useful two-axis lesson, not a numeric tier system for shokunin sources. Both direct official AJP-2.1 PDF routes attempted in this session returned 403; the UK doctrine is the opened primary governmental source for the table reproduced there, while exact NATO-publication wording/version remains unverified.
- **GRADE certainty.** The GRADE Working Group handbook describes outcome-centric certainty across a body of evidence and explicitly says this is not a rating of each study as a single unit (§5). The handbook marks some sections as being replaced by the GRADE Book. CDC's 2024 ACIP GRADE handbook gives a currently readable application: high/moderate/low/very low certainty, downgrade/upgrade considerations, and overall certainty across critical outcomes. Use GRADE only where its evidence-synthesis context fits; never map it to A/B/C.
- **SIFT, lateral reading, and CRAAP.** Caulfield's SIFT article is primary for the author's method: stop, investigate the source, find better coverage, and trace to original context. Wineburg and McGrew's original web-task study observed professional fact-checkers leaving the target site and checking other sources, reaching more warranted conclusions in less time than the historian/student groups in those tasks; its sample and task setting limit generalization. CSU Chico's original CRAAP handout says its criteria can vary in importance by situation. Caulfield's critique is useful expert argument, while the 2021 CRAAP-versus-six-question study is primary empirical evidence with mixed outcomes; neither warrants a universal pass/fail rubric.
- **PRISMA and citation chaining.** PRISMA 2020 is a systematic-review reporting guideline, not a source-grade scale. Its official flow page and statement support tracking identification/selection/inclusion and exclusion reasons. Cochrane's current Chapter 4 describes citation indexes and requires checking reference lists of included studies and relevant reviews for intervention reviews. The opened CoCites validation study distinguishes backward references from forward citing papers and reports that its citation-based method did not retrieve the full included set in its tested reviews. Thus, citation chaining is a reproducible supplementary path, not proof of exhaustive coverage.
- **Link/reference rot and citation archives.** Zittrain, Albert, and Lessig's original Perma paper defines both kinds of rot and shows why link status alone cannot establish that the cited passage remains. Pew's 2024 report and methodology give a broader, sample-bounded view and disclose their operational definition. Perma's own user guide says to verify the capture and publish its Perma link; the guide notes WARC and screenshot formats and that some records can be private. An archive improves recoverability of a version; it does not independently establish that version's truth or authorship.
- **W3C PROV.** The W3C PROV-DM Recommendation is a domain-agnostic provenance model for entities, activities, and responsible agents; the PROV overview says provenance can help assess quality, reliability, and trustworthiness. Borrow the traceability idea (source/version, research/capture activity, responsible author/curator, derived knowledge), not a requirement to implement RDF or claim PROV conformance.

## How lane QUALITY.md should reference tiers

Add a short cross-reference, not a second tier taxonomy: “Use `corpus/SOURCES.md` for the lane's A/B/C source-tier definitions and recheck policy. A/B is a source-role label scoped to a claim, not proof. Admit a claim only when its exact anchor and citation chain support that claim under this `QUALITY.md`; C is a discovery lead and is never sole support for admitted knowledge. Keep observation, inference, and unknown separate; retain rejected sources with reason and flip-condition. Apply GRADE only to an appropriate body of evidence by outcome, not to a source row.” Keep the reusable workflow in `chousa-shokunin/SKILL.md`; do not duplicate it in every `QUALITY.md`.

## Proposed final `SOURCES.md` contract

# SOURCES.md contract
- Purpose: append-only “where to learn” registry; `corpus/knowledge/` stores admitted facts/claims.
- Reuse `chousa-shokunin/SKILL.md`: question → hierarchy → chain → claim check; do not fork its research method.
- Keep exactly one append-only source registry table; optional search-run notes are prose, not another registry table.
| id | source | kind | tier | scope | revision | anchor | teaches | status | opened | recheck | used-by | capture | supersedes | reason/flip |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
- IDs are the next unused `S###`; never reuse. One row per opened source; no `|` inside cells.
- `source` is title plus canonical URL/DOI; `kind` is spec/docs/paper/code/tool/dataset/talk/book/community/own-work.
- `tier A` = primary or authoritative for this row's exact scope; `tier B` = strong secondary synthesis; `tier C` = unverified lead only, never sole support for admitted knowledge.
- Tier is curation, not truth or certainty. Do not assign NATO A–F/1–6 or GRADE labels to registry rows.
- `scope` names the claim/topic for which the tier applies; the same source may earn a different tier outside that scope.
- `revision` pins edition/commit/publication or page version; `anchor` gives exact section/page/heading/line, not just a homepage.
- `teaches` is one grounded learner benefit. A quote is at most 25 words and names its exact location.
- `status` is `queued` (opened, worth mining), `mined` (cited by knowledge/lesson), or `rejected`; `watch` is expressed by `recheck`.
- A rejected row keeps its reason and flip-condition in `reason/flip`; a correction is a new row with `supersedes` set.
- `opened` is the author's ISO date; `recheck` is a date/cadence such as `90d` or `on-release`.
- `used-by` lists exact knowledge/lesson paths or `—`; `capture` gives a verified archive URL, capture date, and digest, or `—`.
- Unopened sources go under `## Leads (unopened)`, never into the registry table; a lead is not evidence.
- For each bounded search, append a prose run note with question/query, searched sources, date, identified/screened/included/excluded counts, exclusion reasons, deduplication, iterations, and stop rationale. Call this PRISMA-inspired tracking, not PRISMA compliance.
- A negative claim carries its search sweep; a citation chain records each hop's anchor as verified or unresolved; counts never imply exhaustiveness.
- Use CRAAP only as context-dependent prompts and SIFT/lateral reading to investigate source identity, better coverage, and original context—not as a score.
- Keep source reliability separate from the specific claim's credibility; if GRADE fits, rate the body of evidence by outcome, not individual registry rows.
- Count rows: `grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md`
- Count tiers: `grep -E '^\| S[0-9]{3} \|' corpus/SOURCES.md | awk -F'|' '{gsub(/[[:space:]]/,"",$5); print $5}' | sort | uniq -c`
- Count statuses: `grep -E '^\| S[0-9]{3} \|' corpus/SOURCES.md | awk -F'|' '{gsub(/[[:space:]]/,"",$10); print $10}' | sort | uniq -c`

## Opened source registry for this review

| id | source | kind | tier | scope | revision | anchor | teaches | status | opened | recheck | used-by | capture | supersedes | reason/flip |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S001 | UK MOD JDP 2-00 — https://assets.publishing.service.gov.uk/media/653a4b0780884d0013f71bb0/JDP_2_00_Ed_4_web.pdf | docs | A | UK exposition of NATO grading | Ed. 4, Aug 2023 | ch. 3 §§3.39–3.40, Table 3.1, pp. 68–70 | Separates source reliability from specific-report credibility; grades can diverge and be revisited. | queued | 2026-10-19 | on-release | — | — | — | — |
| S002 | GRADE Handbook — https://gdt.gradepro.org/app/handbook/handbook.html | book | A | GRADE Working Group overview | Updated Oct 2013; site notes replacement by GRADE Book | About the Handbook; §§1 and 5 | Defines certainty as outcome-centric body-of-evidence assessment; identifies updates replacing older sections. | queued | 2026-10-19 | on-release | — | — | — | — |
| S003 | CDC ACIP GRADE Handbook, ch. 7 — https://www.cdc.gov/acip-grade-handbook/hcp/chapter-7-grade-criteria-determining-certainty-of-evidence/index.html | docs | A | ACIP's application of GRADE | Reviewed Apr 22, 2024 | Summary; Table 4 | Gives certainty categories and outcome-level downgrade/upgrade considerations for ACIP. | queued | 2026-10-19 | on-update | — | — | — | — |
| S004 | CDC ACIP GRADE Handbook, ch. 10 — https://www.cdc.gov/acip-grade-handbook/hcp/chapter-10-overall-certainty-of-evidence/index.html | docs | A | ACIP overall certainty | Reviewed Apr 22, 2024 | Summary | Explains that overall certainty is generally bounded by the lowest-rated critical outcome. | queued | 2026-10-19 | on-update | — | — | — | — |
| S005 | Meriam Library, Evaluating Information — Applying the CRAAP Test — https://library.csuchico.edu/sites/default/files/craap-test.pdf | docs | A | Originator's CRAAP guide | Guide dated 2010-09-17 | p. 1, introduction and criteria | Presents CRAAP questions and says criteria importance depends on the situation or need. | queued | 2026-10-19 | on-use | — | — | — | — |
| S006 | Lowe et al., Questioning CRAAP — https://files.eric.ed.gov/fulltext/EJ1329588.pdf | paper | A | This study's first-year course comparison only | Journal article, 2021 | Results; Discussion; Conclusion | Reports a 6QW paper-rubric advantage but inconclusive quizzes and study limitations; not a universal verdict. | queued | 2026-10-19 | on-use | — | — | — | — |
| S007 | Caulfield, A Short History of CRAAP — https://hapgood.us/2018/09/14/a-short-history-of-craap/ | own-work | B | Author's critique of online checklists | Published 2018-09-14 | “We brought a can opener to a gunfight”; linked history | Argues that static checklists can miss external context; use as expert argument and follow its citations. | queued | 2026-10-19 | on-use | — | — | — | — |
| S008 | Caulfield, SIFT (The Four Moves) — https://hapgood.us/2019/06/19/sift-the-four-moves/ | own-work | A | SIFT as defined by its author | Published 2019-06-19 | “The four moves”; each move heading | Defines the author's source investigation, better-coverage, and original-context moves. | queued | 2026-10-19 | on-use | — | — | — | — |
| S009 | Wineburg & McGrew, Lateral Reading — https://www.hendrix.edu/uploadedFiles/Academics/Faculty_Resources/Teaching_and_Learning/EvaluatingDigitalInformation.pdf | paper | A | Original study's web-evaluation tasks | Stanford SHEG working paper, 2017-09 | Abstract; Methods; Results | Reports fact-checkers' lateral source checks and more warranted conclusions in less time in the studied tasks. | queued | 2026-10-19 | on-use | — | — | — | — |
| S010 | Page et al., PRISMA 2020 statement — https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/ | paper | A | PRISMA systematic-review reporting | BMJ article, 2021 | Table 1, items 16a/16b; Fig. 1 | Requires reporting records-to-included-study selection and excluded studies with reasons. | queued | 2026-10-19 | on-release | — | — | — | — |
| S011 | PRISMA 2020 flow diagram — https://www.prisma-statement.org/prisma-2020-flow-diagram | docs | A | Official PRISMA flow templates | Current site page, opened 2026-10-19 | “PRISMA flow diagram” | Provides templates by review type and source; maps identified, included, excluded, and reasons. | queued | 2026-10-19 | on-release | — | — | — | — |
| S012 | Cochrane Handbook, ch. 4 — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04 | docs | A | Cochrane intervention-review searching | Ch. 4 last updated Mar 2025 | §§4.3.1.4, 4.3.5; MECIR C30 | Describes citation indexes and recommends checking included-study and relevant-review reference lists. | queued | 2026-10-19 | on-release | — | — | — | — |
| S013 | Janssens et al., Novel citation-based search method — https://pmc.ncbi.nlm.nih.gov/articles/PMC7006380/ | paper | A | Citation-search validation in the tested reviews | BMC Med Res Methodol, 2020 | Abstract; Background; Methods; Results | Defines backward/forward citation relations and reports that its tested citation method did not retrieve every included article. | queued | 2026-10-19 | on-use | — | — | — | — |
| S014 | Zittrain, Albert & Lessig, Perma — https://harvardlawreview.org/wp-content/uploads/2014/03/forvol127_zittrain.pdf | paper | A | Original legal-citation samples and proposed Perma workflow | Harvard Law Review Forum, 2014 | Introduction; “Our Work”; “Detailed Methodology” | Defines link and reference rot; shows a successful HTTP status can still fail to preserve cited material. | queued | 2026-10-19 | on-use | — | — | — | — |
| S015 | Pew, When Online Content Disappears — https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | paper | A | Pew's sampled historical pages and linked pages | Report, 2024-05-17 | “How we did this”; findings | Supplies a recent, sample-bounded measure of page and link disappearance, not a universal web rate. | queued | 2026-10-19 | 90d | — | — | — | — |
| S016 | Pew, Link Rot Methodology — https://www.pewresearch.org/data-labs/2024/05/17/methodology-link-rot/ | docs | A | Pew's operational sample and dead-link definition | Report methodology, 2024-05-17 | “Evaluating the status of pages and links” | Discloses samples, status-code thresholds, retries, and ambiguous cases counted as accessible. | queued | 2026-10-19 | 90d | — | — | — | — |
| S017 | Perma.cc user guide — https://perma.cc/docs/perma-link-creation | docs | A | Perma's own capture/citation workflow | Live guide, opened 2026-10-19 | “Preservation Methods”; “Citing Perma Links”; “Preservation formats” | Describes capture verification, public archive links, WARC/screenshot formats, and private-record limits. | queued | 2026-10-19 | 90d | — | — | — | — |
| S018 | W3C PROV-DM Recommendation — https://www.w3.org/TR/2013/REC-prov-dm-20130430/ | spec | A | W3C provenance data model | W3C Recommendation, 2013-04-30 | Abstract | Defines a domain-agnostic model for entities, people, and processes involved in producing data or things. | queued | 2026-10-19 | on-release | — | — | — | — |
| S019 | W3C PROV-Overview — https://www.w3.org/TR/2013/NOTE-prov-overview-20130430/ | spec | A | W3C PROV family overview | W3C Working Group Note, 2013-04-30 | Abstract | Explains provenance as a basis for assessing quality, reliability, and trustworthiness. | queued | 2026-10-19 | on-release | — | — | — | — |

## Candidate knowledge entries

These add method guidance rather than duplicate chousa's existing structural gates; all are candidates, not admitted knowledge.

CE01 — `source-tier-is-scope-not-verdict` — Claim: A/B/C describes a source's role for a named scope and does not prove that a claim is true. Evidence: S001 §3.39(c), Table 3.1; S005 introduction. Quote: “Reliability and credibility must be evaluated separately.” (JDP 2-00, §3.39(c), p. 69.) Fills the currently unlisted source-tier/claim-grade distinction in `corpus/knowledge/`.

CE02 — `grade-certainty-is-outcome-level` — Claim: GRADE certainty is assigned to a body of evidence for an outcome, not to one registry source. Evidence: S002 §5; S003 Summary; S004 Summary. Quote: “This does not mean rating each study as a single unit.” (GRADE Handbook, §5.) Fills evidence-grading methodology without turning the source registry into a health guideline.

CE03 — `web-source-checking-needs-context` — Claim: online source appraisal should include source investigation, independent coverage, and original context; CRAAP criteria are not equal-weight universal scores. Evidence: S005 introduction; S007 “We brought a can opener to a gunfight”; S008 “The four moves”; S009 Abstract/Results. Quote: “Different criteria will be more or less important depending on your situation or need.” (Meriam Library CRAAP guide, p. 1.) Fills web-source appraisal, not a verdict about every checklist.

CE04 — `search-flow-and-citation-chains-are-auditable` — Claim: bounded review searches should expose identification, screening, inclusion/exclusion reasons, and the citation-search path; citation networks are not guaranteed exhaustive. Evidence: S010 Table 1 items 16a/16b; S012 §4.3.5/C30; S013 Background/Results. Quote: “Cite studies that might appear to meet the inclusion criteria, but which were excluded, and explain why they were excluded.” (PRISMA 2020, item 16b.) Fills search transparency without claiming every lane performs a systematic review.

CE05 — `citation-time-capture-preserves-a-version` — Claim: cite a checked archive snapshot alongside the live source when appropriate, but do not treat preservation as proof of source truth. Evidence: S014 Introduction/“Our Work”; S015 report; S016 methods; S017 “Citing Perma Links”; S018–S019 abstracts. Quote: “If you don't publish the Perma Link, your readers won't be able to find the record.” (Perma user guide, “Citing Perma Links.”) Fills external web-citation durability, distinct from chousa's local archived-export intake.

## Mistakes mined

M01 — Treating A/primary as a claim-verdict transfers source authority to the proposition; the JDP separates those judgments, and GRADE is outcome-level (S001–S004).

M02 — Turning CRAAP into equal-weight points erases its originator's situation-dependent instruction and overstates a mixed comparison study (S005–S007).

M03 — Treating HTTP 200 or a live URL as proof that a citation still contains the referenced passage misses reference rot (S014–S016).

M04 — Treating a resolved anchor/reference or clean structural gate as semantic support overclaims what chousa's own known-gaps section says its checks establish (README lines 141–159).

## Leads (unopened / access-limited)

- NATO, AJP-2.1 official PDF routes on COI and JADL returned HTTP 403 in this session. JDP 2-00 is the opened UK doctrine source for the NATO grading table it reproduces; exact AJP-2.1 wording/version remains unresolved.
- TARCiS statement full text and correction on BMJ returned HTTP 403. The PubMed record exposed bibliographic metadata and an erratum reference but not the statement's recommendations, so it is not a source row. Cochrane's opened handbook and the opened citation-search validation study support the claims made here.
- Current GRADE Book chapter pages returned an empty shell in the reader. The GRADE handbook itself notes that its overview and certainty section are being replaced; CDC's 2024 ACIP handbook was readable, but the exact current GRADE Book wording remains to be checked.
- Library of Congress WARC format page returned HTTP 403. Perma's opened user guide is the direct source for its own WARC/screenshot capture and citation workflow.

## Counts and commands

- Opened source rows: 19 — `grep -cE '^\| S[0-9]{3} \|' local://kaika-w1-art-curation.md`
- Tier rows: A=18, B=1, C=0 — `grep -E '^\| S[0-9]{3} \|' local://kaika-w1-art-curation.md | awk -F'|' '{gsub(/[[:space:]]/,"",$5); print $5}' | sort | uniq -c`
- Candidate entries: 5 — `grep -cE '^CE[0-9]{2} —' local://kaika-w1-art-curation.md`
- Mistakes mined: 4 — `grep -cE '^M[0-9]{2} —' local://kaika-w1-art-curation.md`
- Draft defects found: 8 — `grep -cE '^D[0-9]{2} —' local://kaika-w1-art-curation.md`

## Recommendations

1. Preserve the draft's useful purpose and append-only registry, but add scope, exact revision/anchor, capture metadata, and explicit rejection reason/flip-condition.
2. Keep A/B/C as local, claim-scoped curation tiers; keep source reliability, report credibility, claim support, and GRADE certainty as distinct judgments.
3. Reuse chousa's research method and gates; add a lightweight, PRISMA-inspired search log for bounded sweeps and a `QUALITY.md` cross-reference instead of duplicating method or pretending a count proves truth.
