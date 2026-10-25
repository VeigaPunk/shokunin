# Chousa ART dossier — deep-research method

**Lane:** `chousa` (`/home/vgpnk/Projects/shokunin/chousa-shokunin`)  
**Opened:** 2026-10-19  
**Research scope:** research-agent evaluations, citation/source attribution, claim verification, retrieval evaluation, and source-appraisal frameworks. Documentation and papers only; no live targets were accessed.

## Evidence handling and limits

- `web_search` was available and used; source rows below are only pages opened during this session. `SOURCES.md` is a proposed registry shape, not an existing file edited in the lane.
- No LSP device is exposed in the mounted tool inventory. I used literal grep only to discover headings/paths; it is not semantic proof. Local findings below cite the file sections actually read.
- The assignment is leaf-member/read-only. No subagents, repository edits, gate runs, or git mutations were made. Only this output artifact is written.
- **Instruction-like target text:** TREC's paper contains quoted benchmark prompt templates (Figures 2–3) including “Return only a JSON list … no extra commentary” and scoring instructions. These are experimental prompt artifacts, not directions for this dossier; treated as untrusted content and not followed. The ICLR landing page also carries the publisher boilerplate “Do not remove” in its comment form. These are recorded as instruction-like/prompt-injection content for the wave policy, not as evidence of compromise or as research claims.

## Uncovered ground and what the lane already holds

### Observed local facts

- `PROVINCE.md:3-15` owns reusable question framing, source hierarchy, citation-chain hop resolution, claim-vs-source verification, and search-strategy taxonomy. It refuses model-quality/evaluation claims to `kengaku`, external live-target research without operator approval, and orchestration work.
- `SKILL.md:8-21,33-40` already prescribes question → source hierarchy → chain → claim check; primary/secondary/aggregator/unsourced categories; anchor resolution; and explicit unresolved handling. It says to report source disagreements rather than average them.
- `SKILL.md:23-31` explicitly says the primary > secondary > aggregator > unsourced ladder is this lane's own construction, not a hierarchy inherited from another lane; rows warranted only by that table remain proposals until sourced.
- `corpus/QUALITY.md:1-7` is titled “Admission bar (probation draft)” and requires falsifiable claims or opinion labels, an evidence anchor, separation of observation/inference/unknown, append-only errata, and retained rejection reasons.
- `corpus/README.md:8-30` and filenames in `corpus/knowledge/` show extensive work on record structure, verbatim claim spans, citation-hop anchors, rejection/sweep checks, composed gate modes, reference integrity, path boundaries, and Markdown parsing. Knowledge filenames observed (no entry bodies read): `archived-export-intake.md`, `claim-verification-r2.md`, `chain-resolution-r3.md`, `anchor-boundaries-r4.md`, `sweeps-rejections-r5.md`, `verify-all-r6.md`, `reference-integrity-r7.md`, `gate-baseline-r8.md`, `archives-verified-r9.md`, `hardening-r10.md`, `audit-r11.md`, `scope-refusal-r12.md`, `gate-baseline-r12.md`, `hardlink-alias-r13.md`, `mount-alias-r14.md`, `root-slash-boundary-r15.md`, `verification-r16.md`, `fenced-heading-r17.md`, `scope-phrase-gap-r18.md`, `sweep-symlink-r19.md`, `html-comment-r20.md`, `pointer-boundary-r21.md`, `denylist-r22.md`, and `fenced-anchor-r23.md`.
- `corpus/README.md:139-159,474-476` says the local verifier checks declared record structure, byte-span identity, local source canonicalization/anchor existence, selected sweep locations, and reference tokens. It explicitly says those checks do not establish semantic support, source truth, or external-source verification; external source verification remains out of scope by design. `corpus/README.md:306-476` frames the Frontier primarily as serial gate-hardening and evidence-boundary work.

### Synthesis / inference

- The lane already has unusually developed *mechanical provenance* (resolvable IDs, pinned bytes, exact spans/anchors, explicit refusals). The uncovered layer is *epistemic admission*: what the claim asks, why this source is appropriate for it, whether a chain preserves the original claim, whether the source actually supports the claim, and what remains unknown.
- The current source ladder is acknowledged as provisional but still appears in the skill's decision table. Current 2025–2026 literature and authoritative source-appraisal guidance support a claim-relative gate more strongly than a universal source-type ladder. This is a recommendation inferred from the opened sources, not a claim that any one paper establishes a universal hierarchy.
- The external-evaluation papers belong in Chousa only as method evidence. Their leaderboards and model-performance claims remain out of province (`kengaku`); their useful parts are task scoping, independent constructs, traceable citation checks, calibrated judgments, and retained uncertainty.
- No opened source establishes one universally correct source ranking across every domain and claim type. The health-intervention guidance below is a useful warning against design-label pyramids, not a universal model for all research.

## Current art: method findings

1. **Deep research is multi-construct.** The ICLR 2026 DeepResearch Bench evaluates report quality separately from effective citations/citation accuracy. DeepResearch Bench II (an arXiv preprint) derives granular criteria from expert reports and separates information recall, analysis, and presentation. DRACO and DRBench use other task/domain mixes. These are complementary benchmark designs, not interchangeable measures or a universal leaderboard.
2. **Citation quality is not a URL check.** CiteEval argues that NLI-style source entailment alone is an incomplete proxy and evaluates citation quality in the context of the query, retrieval context, and generated answer. “Cited but Not Verified” separates URL accessibility, topical relevance, and factual support. TREC 2025 separately assesses document relevance, answer completeness, sentence-to-citation support, and assessor agreement. The measures answer different questions.
3. **Citation support is not the same as world truth.** DeepResearch Bench II explicitly notes that a source can support an answer while the information itself may still be false. A record therefore needs distinct states for source existence/access, relevance, claim support, and truth/verification; a supported claim can still be wrong if the source is wrong.
4. **Citation chains can transmit distortion.** Chen et al. (ACL 2025) compare claims in citing and cited papers and report a “telephone effect”: lower fidelity in one link is associated with lower fidelity in later citations. This is scholarly-citation evidence; applying it to general web chains is a cautious inference, but it directly motivates resolving intermediate hops rather than accepting a summary of a citation.
5. **More retrieval is not monotonic evidence quality.** The 2026 “Cited but Not Verified” preprint reports that factual-check performance fell as search depth increased in its tested models while surface-level link/relevance measures remained stable. Treat this as a task-specific result, not a universal law; it nevertheless refutes “more sources/search calls automatically means more verified knowledge.”
6. **Labels and judges need auditability.** DeepFact introduces versioned, revisable claim labels and an audit-then-score procedure; Cochrane's standards require independent duplicate risk-of-bias review and support for each judgment. For a Chousa gate, this generalizes as “retain judgment evidence, disagreements, and corrections,” not “automate a final truth oracle.”
7. **Source hierarchy should be conditional and question-relative.** IFCN requires best available primary evidence *where suitable*, and explanation when using secondary evidence; it also requires key claim elements to be checked against multiple named sources when available. SIFT adds source identity/agenda, better coverage, and tracing to original context. Cochrane cautions against relying on fixed study-design labels in intervention evidence and evaluates fit/risk for the actual question. Together, these support contextual appraisal rather than a universal ranking.

## Candidate knowledge entries

Each entry below is a proposal, not an admitted local fact. Quotes are from pages opened this session and are under 25 words. `QUALITY.md` criteria are referenced as Q1–Q5 in order: falsifiability, evidence anchor, observation/inference/unknown separation, append-only errata, retained rejection.

### C01 — `question-framing-and-scope.md`

- **Falsifiable claim:** A research record is not ready to search until it declares an answerable user question, scope/temporal bounds where relevant, and a coverage plan whose independent subquestions can be checked in the final report.
- **Evidence:** Cochrane Handbook, Chapter 2, §2.1: “The first and most important decision in preparing a systematic review is to determine its focus.” TREC 2025 RAG Track, §2 and §3.1, decomposes multi-faceted narratives into sub-narratives before relevance and coverage assessment. DeepResearch Bench II, §3.1.2, requires temporal scope for time-sensitive tasks.
- **Coverage row filled:** Add a method row under `corpus/README.md` `## Frontier` for question declaration, scope, and subquestion coverage. Existing material describes record/gate behavior but the named filenames do not identify a learned question-framing method.
- **Recheck:** Re-open S024 §2.1–2.3 and S017 §2–3.1; test records for a declared question, scope, and separately checkable coverage obligations.
- **QUALITY:** Q1–Q3: presence and completeness can be checked; each criterion has a source anchor; domain transfer beyond review/benchmark settings must be labelled inference.

### C02 — `contextual-source-admission.md`

- **Falsifiable claim:** Source priority must be justified for the particular claim: provenance, source role, method/fit, recency, interests, independence, and availability determine whether primary evidence is suitable; a secondary source must be identified and its use explained. Do not treat “primary” as automatically correct or as a universal rank.
- **Evidence:** IFCN Code, Principle #2 “Standards and Transparency of Sources”: “The applicant uses the best available primary, not secondary, sources of evidence wherever suitable primary sources are available.” Cochrane Handbook, Chapter 24, §24.2.1.3, cautions against existing evidence hierarchies when study-design labels do not fit the actual question. SIFT, “Investigate the source” and “Find better coverage,” asks readers to account for expertise, agenda, and alternative coverage.
- **Coverage row filled:** Grounds the currently provisional hierarchy in `SKILL.md:17-30`; add a source-admission procedure to the Frontier without broadening the lane into bounty, model-quality, or orchestration work.
- **Recheck:** Re-open S022 Principle #2, S027 §24.2.1.3, and S023 “Investigate the source”; compare decisions across unlike claim types and record counterexamples.
- **QUALITY:** Q1–Q3: require an explicit suitability reason, cite the relevant source location, and mark healthcare-specific criteria as analogy rather than universal rule.

### C03 — `citation-chain-fidelity.md`

- **Falsifiable claim:** A resolved chain anchor establishes that a locator exists, not that a later paraphrase preserves the original claim; a “faithful” disposition must compare each hop's proposition and qualifications against the source at that hop, or remain unresolved.
- **Evidence:** Chen et al., ACL 2025, Abstract: “citations can vary in their fidelity”; the same abstract describes a “telephone effect” in which low-fidelity citation links are followed by lower-fidelity later citations. `corpus/README.md:151-155` already records that local CLEAN does not prove semantic support or agreement.
- **Coverage row filled:** Extend the existing chain-resolution/anchor-boundary topic in the coverage map with a separate semantic-fidelity method; do not relabel `verify-chain` anchor existence as a semantic truth check.
- **Recheck:** Re-open S014 Abstract and compare one hop at a time from claim → cited source → cited source's source; record an exact anchor and any lost scope/uncertainty.
- **QUALITY:** Q1–Q3 and Q5: use positive, altered, and unresolved examples; cite each source hop; keep a rejection with its reason when a chain stops.

### C04 — `claim-source-truth-boundaries.md`

- **Falsifiable claim:** An accessible, topically relevant citation is not sufficient for a supported claim; source access, relevance, claim support, and the source's own truth are distinct observations. A result that collapses these states must fail a fixture where the page loads and is topical but does not support the claim.
- **Evidence:** “Cited but Not Verified,” §3.3: “Link Works verifies URL accessibility, Relevant Content measures topical alignment, and Fact Check validates factual accuracy against source content.” DeepResearch Bench II, §2.1, warns that citation support alone does not confirm information correctness. The lane's local known-gaps section says its gate does not prove semantic support or source truth.
- **Coverage row filled:** Add the external claim/source semantic boundary to the existing local-only claim-verification topic. This is a manual/documentation method under current boundaries, not authorization to fetch outside sources or change the gate's scope.
- **Recheck:** Re-open S010 §3.3 and S002 §2.1; construct or review a cited claim whose source is accessible and topical but contradictory/insufficient, and retain separate outcomes.
- **QUALITY:** Q1–Q3 and Q5: enumerate the distinct states, attach a location to each judgment, preserve “unresolved,” and retain the counterexample.

### C05 — `adjudication-and-revision.md`

- **Falsifiable claim:** When a claim-support or source-admission judgment is disputed, retain the submitted evidence, an independent review/adjudication, and an append-only revision; do not treat one unreviewed human or model label as an immutable oracle.
- **Evidence:** DeepFact, Abstract: “labels and rationales remain revisable.” Cochrane MECIR C53–C55 requires independent duplicate review, a pre-defined disagreement process, and the source supporting each judgment.
- **Coverage row filled:** Adds an epistemic review/correction method beside the existing append-only records and mechanical verification modes; does not absorb model-evaluation ownership.
- **Recheck:** Re-open S013 Abstract and S026 standards C53–C55; for a disagreement, check that the evidence, adjudicator, prior label, and new disposition are all recorded.
- **QUALITY:** Q1–Q5: define what would overturn a decision, keep the evidence pointer, separate observation from judgment, append the correction, and preserve rejected alternatives with reasons.

## Study paths

- **Question to evidence audit — S024 → S017 → S018 → S001 → S002:** start with an answerable scoped question; see narrative decomposition and manual/automated support assessment; isolate retrieval metrics; then compare report-level rubric designs. This sequence teaches task construction, not a Chousa model leaderboard.
- **Source hierarchy and chain — S023 → S022 → S027 → S014 → S009 → S010:** investigate origin/context; apply conditional primary-source transparency; avoid fixed design-label ladders; trace citation fidelity; then learn citation-context and deployed-report checks.
- **Claims and adjudication — S015 → S020 → S026 → S013:** inspect evidence-backed claim verdicts and insufficient-evidence behavior; see annotated grounding; require supported duplicate judgments; then study revisable factuality labels.

## Failure modes mined from current literature

|id|failure mined|evidence and location|method response|
|---|---|---|---|
|M01|A real citation can be misattributed or fail to support the attached claim.|S010 §3.3 separates access, topical relevance, and factual support.|Keep separate per-citation outcomes; do not pass a claim on link existence or topic match alone.|
|M02|A citation chain can transmit progressively altered meaning.|S014 Abstract reports citation-fidelity variation and the “telephone effect.”|Resolve the original source and compare claims/qualifications at each hop; otherwise mark unresolved.|
|M03|More search depth can leave factual synthesis worse, even where links and topical relevance look sound.|S010 §4.3; result is limited to the study's evaluated models/tasks.|Do not admit source-count or tool-call count as quality; ask whether evidence supports the exact claim.|
|M04|A one-pass benchmark label can be mistaken; expert judgments may need evidence-led revision.|S013 Abstract describes audited, revisable labels; S026 C53–C55 supports independent review.|Retain disagreement, rationale, adjudication, and append-only label history.|
|M05|A source-type ladder can overstate authority when detached from the claim and method.|S022 Principle #2 says primary evidence is preferred where suitable; S027 §24.2.1.3 warns against fixed hierarchies for intervention questions.|Use a conditional, question-relative source appraisal; keep domain boundaries explicit.|

## Rejected candidates, retained as evidence of taste

- **Reject:** “Primary > secondary > aggregator > unsourced” as a universal admission theorem. The opened authorities support conditional preference for suitable primary sources and warn that fixed evidence hierarchies can mislead. Retain the current lane ladder as a proposal until a question-relative rule has evidence and counterexamples.
- **Reject:** “More sources, citations, or search calls means better research.” S010 §4.3 reports non-monotonic factual checking under increased search depth; S008 also separates coverage and citation quality. Source quantity is not a substitute for claim-level support.
- **Reject:** “Working URL + on-topic page = verified claim.” S010's three dimensions and S017's support evaluation separate these checks; such a rule would silently over-admit unsupported statements.
- **Reject:** “A single automated judge or frozen expert label is ground truth.” S013 makes labels revisable and S026 requires duplicate, supported judgments. Use automation as an aid, keep unresolved cases, and permit evidence-backed correction.
- **Reject/defer to `kengaku`:** Importing benchmark scores or model rankings into Chousa's source-admission corpus. The benchmark metrics are useful to learn evaluation design, but the lane boundary expressly refuses model-quality claims.

## Proposed `corpus/SOURCES.md` rows

All entries below were opened in this session. `queued` means opened and worth mining next; `used-by` stays `—` because no corpus knowledge entry was authored. `S011` is tier B because it is a synthesis survey; all other rows are original papers, official standards, authoritative documentation, or official first-party proceedings/data (tier A). Several standards predate 2025; they are retained because they remain the primary/authoritative method source for their stated scope, not because they are current-art studies.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents — https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html|paper|A|Separates reference-based report assessment from citation count and citation accuracy in open-ended research tasks.|queued|2026-10-19|90d|—|
|S002|DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports — https://arxiv.org/html/2601.08536v3|paper|A|An arXiv preprint with expert-derived fine-grained rubrics across recall, analysis, and presentation; useful for construct separation, not as a universal score.|queued|2026-10-19|90d|—|
|S003|DRBench: A Realistic Benchmark for Enterprise Deep Research — https://arxiv.org/abs/2510.00172|paper|A|Enterprise tasks mix web and private knowledge, and score insight recall, factual accuracy, and report coherence.|queued|2026-10-19|90d|—|
|S004|Deep Research Bench: Evaluating AI Web Research Agents — https://arxiv.org/html/2506.06287v1|paper|A|Uses multi-step research tasks and frozen RetroSearch for repeatable comparisons; includes original-source and claim-validation task types.|queued|2026-10-19|90d|—|
|S005|ResearcherBench: Evaluating Deep AI Research Systems on the Frontiers of Scientific Inquiry — https://arxiv.org/abs/2507.16280|paper|A|Pairs rubric assessment of insight with factual assessment of citation faithfulness and coverage; domain is frontier AI research.|queued|2026-10-19|90d|—|
|S006|ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks — https://arxiv.org/abs/2508.15804|paper|A|Separates cited-literature relevance, source faithfulness, and verification of uncited factual statements.|queued|2026-10-19|90d|—|
|S007|DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity — https://arxiv.org/abs/2602.11685|paper|A|Uses task-specific rubrics to keep factual accuracy, breadth/depth, presentation/objectivity, and citation quality distinct.|queued|2026-10-19|90d|—|
|S008|Synthesizing scientific literature with retrieval-augmented language models — https://www.nature.com/articles/s41586-025-10072-4|paper|A|ScholarQABench combines citation measures with human rubrics for coverage, coherence, writing, and factual correctness in long-form synthesis.|queued|2026-10-19|90d|—|
|S009|CiteEval: Principle-Driven Citation Evaluation for Source Attribution — https://aclanthology.org/2025.acl-long.1574/|paper|A|Citation quality is evaluated in query, retrieval, and answer context rather than only as entailment from a cited passage.|queued|2026-10-19|90d|—|
|S010|Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents — https://arxiv.org/html/2605.06635v1|paper|A|A reproducible report parser supports separate URL-access, relevance, and claim-support checks; results are a preprint's particular evaluation.|queued|2026-10-19|90d|—|
|S011|Attribution, Citation, and Quotation: A Survey of Evidence-based Text Generation with Large Language Models — https://aclanthology.org/2026.acl-long.1430/|paper|B|Maps terminology and evaluation approaches for evidence-based generation; useful for finding primary sources, not as sole support for a claim.|queued|2026-10-19|90d|—|
|S012|CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation — https://aclanthology.org/2026.acl-long.282/|paper|A|Frames citation checking as retrieval-aware attribution alignment and recognizes alternative valid sources.|queued|2026-10-19|90d|—|
|S013|DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality — https://aclanthology.org/2026.acl-long.1586/|paper|A|A claim-level benchmark keeps rationales and labels revisable through evidence submission and adjudication.|queued|2026-10-19|90d|—|
|S014|The Noisy Path from Source to Citation: Measuring How Scholars Engage with Past Research — https://aclanthology.org/2025.acl-long.1534/|paper|A|Measures sentence-level citation fidelity and shows that information can be distorted as claims are relayed through later citations.|queued|2026-10-19|90d|—|
|S015|The 2nd Automated Verification of Textual Claims AVeriTeC Shared Task — https://aclanthology.org/2025.fever-1.15/|paper|A|Real-world claim verification requires evidence retrieved with the verdict; highlights reproducibility and efficiency constraints in the shared task.|queued|2026-10-19|90d|—|
|S016|Proceedings of the Eighth Fact Extraction and VERification Workshop — https://aclanthology.org/volumes/2025.fever-1|paper|A|Official proceedings index exposes 2025 work on evidence retrieval, claim decomposition, nuanced verdicts, and verifier bias; follow each paper before admission.|queued|2026-10-19|90d|—|
|S017|Overview of the TREC 2025 Retrieval Augmented Generation Track — https://trec.nist.gov/pubs/trec34/papers/Overview_rag.pdf|paper|A|Separates retrieval relevance, answer coverage/completeness, sentence-level citation support, and assessor agreement.|queued|2026-10-19|90d|—|
|S018|TREC 2025 RAG Retrieval-Only Task Results — https://trec.nist.gov/pubs/trec34/appendices/trec2025-rag-retrieval.html|dataset|A|Reports nDCG and recall for retrieval runs; retrieval ranking is not a factuality or claim-support verdict.|queued|2026-10-19|90d|—|
|S019|MIRAGE: A Metric-Intensive Benchmark for Retrieval-Augmented Generation Evaluation — https://aclanthology.org/2025.findings-naacl.157/|paper|A|Separates retrieval and generation and tests robustness to noisy or misleading context.|queued|2026-10-19|90d|—|
|S020|GaRAGe: A Benchmark with Grounding Annotations for RAG Evaluation — https://aclanthology.org/2025.findings-acl.875/|paper|A|Passage-level grounding annotations test relevant support and whether a system deflects when evidence is insufficient.|queued|2026-10-19|90d|—|
|S021|BrowseComp-Plus: A Fair and Disentangled Evaluation Benchmark for Deep Search Agents — https://aclanthology.org/2026.acl-long.1023/|paper|A|A fixed human-verified corpus improves reproducibility and separates retriever effects from end-to-end search-agent performance.|queued|2026-10-19|90d|—|
|S022|IFCN Code of Principles — Standards and Transparency of Sources — https://ifcncodeofprinciples.poynter.org/the-commitments|spec|A|Requires conditional use of suitable primary evidence, explanation for secondary sources, multiple named sources where available, and disclosed interests.|queued|2026-10-19|on-revision|—|
|S023|SIFT (The Four Moves) — https://hapgood.us/2019/06/19/sift-the-four-moves/|docs|A|The method investigates source identity and agenda, seeks better coverage, traces claims to original context, and periodically stops to refocus.|queued|2026-10-19|365d|—|
|S024|Cochrane Handbook Chapter 2: Determining the scope of the review and the questions it will address — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-02|docs|A|Authoritative health-review guidance on answerable questions, scope, user relevance, and PICO; transfer beyond that domain is an analogy.|queued|2026-10-19|on-release|—|
|S025|Cochrane Handbook Chapter 14: Completing Summary of findings tables and grading certainty — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14|docs|A|Grades certainty for each outcome using risk of bias, inconsistency, indirectness, imprecision, and publication bias.|queued|2026-10-19|on-release|—|
|S026|Cochrane MECIR C52-C60: Assessing risk of bias in included studies — https://www.cochrane.org/authors/handbooks-and-manuals/mecir-manual/standards-conduct-new-cochrane-intervention-reviews-c1-c75/performing-review-c24-c75/assessing-risk-bias-included-studies-c52-c60|spec|A|Requires independent duplicate judgments, a defined disagreement process, and evidence supporting each risk-of-bias judgment.|queued|2026-10-19|on-revision|—|
|S027|Cochrane Handbook Chapter 24: Including non-randomized studies on intervention effects — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-24|docs|A|The current Handbook chapter cautions against fixed study-label hierarchies and recommends appraisal of design features relative to the question.|queued|2026-10-19|on-release|—|

## Leads (unopened)

These are search leads only; none is a SOURCES row because its page was not opened.

- Oxford CEBM, “Levels of Evidence: An introduction” — https://www.cebm.ox.ac.uk/resources/levels-of-evidence/levels-of-evidence-introductory-document — compare with the Cochrane warning on question-specific design appraisal.
- Original AVeriTeC shared-task paper — https://arxiv.org/html/2410.23850v1 — inspect original dataset construction and evidence-verdict schema before any future corpus admission.
- TREC RAG track website — https://trec-rag.github.io/ — track task data, qrels, and versioning details not covered by the opened overview/appendix.
- Check, Please! Starter Course linked from the SIFT author page — https://www.notion.so/Check-Please-Starter-Course-ae34d043575e42828dc2964437ea4eed — inspect as an applied learner path, not as primary evidence for source truth.

## Contract defect found

|id|defect|evidence|reproduction|
|---|---|---|---|
|D01|The README coverage inventory is stale/incomplete: `corpus/README.md:50` declares 20 entries (ten knowledge notes and ten lessons), while the current `corpus/knowledge/` directory has 24 Markdown files and the README maps 23 knowledge paths; `audit-r11.md` is in the directory but not in the map.|`corpus/README.md:7-30,50`; complete `corpus/knowledge/` filename listing from glob.|24 files — `printf '%s\n' corpus/knowledge/*.md | wc -l`; 23 listed knowledge rows — `grep -c '^| \`knowledge/' corpus/README.md`; locate declared count — `grep -n '^Count:' corpus/README.md`; check omitted audit note — `grep -F -c 'audit-r11.md' corpus/README.md`|

This is one index-consistency defect, not a claim that the gate itself is unsound. The intentional external/semantic verification boundary is a remaining method gap, not counted as a defect.

## Counts

- Source rows: 27 — `grep -cE '^[|] S[0-9]{3} [|]' local://kaika-w1-chousa-art.md`
- Tier A: 26 — `grep -cE '^[|] S[0-9]{3} [|].*[|] A [|]' local://kaika-w1-chousa-art.md`
- Tier B: 1 — `grep -cE '^[|] S[0-9]{3} [|].*[|] B [|]' local://kaika-w1-chousa-art.md`
- Tier C: 0 — `grep -cE '^[|] S[0-9]{3} [|].*[|] C [|]' local://kaika-w1-chousa-art.md`
- Candidate knowledge entries: 5 — `grep -cE '^### C[0-9]{2} ' local://kaika-w1-chousa-art.md`
- Failure modes mined: 5 — `grep -cE '^[|] M[0-9]{2} [|]' local://kaika-w1-chousa-art.md`
- Contract defects found: 1 — `grep -cE '^[|] D[0-9]{2} [|]' local://kaika-w1-chousa-art.md`
- Current knowledge files: 24 — `printf '%s\n' corpus/knowledge/*.md | wc -l`

## Top recommendations

1. Ground or qualify the provisional source ladder with a claim-relative admission record: source role, original provenance, method/fit, recency, conflicts/interests, independent corroboration, and why a primary source is suitable; explain secondary use.
2. Keep structural/verbatim verification distinct from semantic claim support and source truth. Preserve the current no-external-fetch boundary; use explicit approval and a human evidence-backed method where external source comparison is required.
3. Track question coverage, retrieval/relevance, citation attribution, factual support, completeness, and adjudication as separate observations. Trace chains to original context, retain disagreements/rejections, and do not turn benchmark metrics or source counts into a scalar Chousa verdict.