# ART dossier — kengaku

**Lane:** LLM and model research and evaluation  
**Research scope:** evaluation methodology: contamination detection, LLM-as-judge bias and calibration, benchmark saturation, agentic evaluations, and statistical reporting.  
**Research date:** 2026-10-19

## Uncovered ground

### What the lane already holds

- `corpus/README.md` marks benchmark selection, search-shape mechanisms, run telemetry, evaluation theory, executed local evaluations, cross-pipeline stability, planning-horizon probes, and prior-art pricing as covered. Its benchmark-selection and evaluation-theory summaries include contamination status and an LLM-judge-versus-aggregator distinction; those are real coverage, not empty space. See `corpus/README.md` §Coverage map and `corpus/knowledge/benchmark-selection.md` / `eval-theory-notes.md`.
- `SKILL.md` already warns against stale leaderboard trust and contamination blindness, frozen-harness violations, and interpreting a multi-turn advantage as planning. It says to re-check benchmark contamination status before citing (`SKILL.md` §Benchmark anti-patterns, lines 60–100).
- The existing `eval-theory-notes.md` summarizes judge-versus-aggregator failure modes and advocates algorithmic aggregation; `eval-prior-art-calibration.md` prices local findings against fetched public literature. These are useful foundations, but they are not a current, end-to-end source-backed protocol for calibrating judge accuracy or reporting uncertainty.
- The corpus has substantial local evidence about run-to-run noise, power, paired contrasts, forecasting, and planning-horizon probes (`README.md` §Coverage map and §Open gaps; knowledge filenames include `bench-arena-round7-noise-n25.md`, `bench-arena-round11-power.md`, `bench-arena-round12-ladder.md`, `bench-arena-round8-horizon.md`, and `bench-arena-round9-replication.md`). The local planning-horizon instrument is closed as an instrument, while the claim remains explicitly open.

### Where a new source-backed frontier helps

1. **Contamination method and transparency.** The skill already flags contamination, and benchmark selection records a contamination status, but the coverage map has no dedicated row for detector families, detector blind spots, or a benchmark contamination-transparency record. Recent work shows why a detector-negative must not be translated into “clean.”
2. **Judge calibration rather than judge confidence.** Existing notes describe judges as noisy proxies and the need to separate judgment from aggregation. The uncovered step is calibration against human labels, including the judge’s sensitivity/specificity and their uncertainty, plus prompt-perturbation tests for position, rubric, and reference-answer effects.
3. **Benchmark saturation and lifecycle.** The lane warns about stale leaders and already has selection advice, but no named coverage row for a statistical saturation test or an explicit distinction between task mastery and insufficient top-model discrimination. The current evidence also cautions against treating private splits as a stand-alone longevity guarantee.
4. **Agentic task validity.** The lane has unusually deep bespoke horizon and repeated-run work. The next useful source layer is external methodology that makes task duration, human baselines, reliability level, task family, scaffold, and external-validity limits explicit. Current coding-benchmark audits make test validity and contamination separate concerns: even a replacement benchmark needs task-level quality checks.
5. **Statistical reporting recipe.** Existing local power and paired-result work is strong, but the README does not expose a general transfer checklist for uncertainty in shared-item comparisons, task-family clustering, run variability, adaptive data selection, and leaderboard multiplicity.

### Proposed corpus placement

Add coverage-map rows for **contamination detection and transparency**, **judge calibration**, **benchmark saturation/lifecycle**, and **statistical reporting**. Extend the existing agentic/planning-horizon row with externally sourced time-horizon and task-validity methodology rather than replacing the lane's local instrument. Source claims below are deliberately bounded to what the opened evidence supports.

## Current art, 2025–2026

- **Contamination is tiered and detectors are conditional evidence.** The 2026 systematic review distinguishes exact, syntactic, semantic, and task-level contamination; compares string matching, likelihood, membership inference, model-prompted detection, and benchmark audits; and concludes that no detection family is reliable across all tiers, access settings, and training stages. A separate reasoning-model study reports that post-training can conceal signals used by contamination detectors. Operational consequence: report what a detector had access to, what contamination tier it tests, and what a negative result cannot rule out. Do not turn “not detected” into “uncontaminated.” (S001–S002)
- **A judge’s score is not an unbiased accuracy estimate by default.** Current work measures scoring-prompt effects such as rubric order, score IDs, and reference-answer score, while rubric-based judging has model-specific position and criterion-order effects. A 2026 ICML paper provides a direct correction-and-interval approach using a human-labeled calibration set, carrying uncertainty from both the test sample and the calibration sample. Treat prompt robustness and calibration as different checks: permutation can reduce a positional effect, but does not establish human accuracy. (S009–S011)
- **Saturation is a measurement-resolution problem, not simply a high score.** A 2026 systematic study defines it around loss of reliable discrimination among top systems together with proximity to an empirical ceiling, and proposes an uncertainty-aware index. This gives a useful lifecycle signal, not a universal verdict: check the study’s model-relative assumptions and small private-benchmark subset before claiming that privacy has no value. Pair saturation checks with construct validity and task-quality review. (S007–S008)
- **Agentic results depend on the task and its grader.** METR defines time horizon using human completion time and a chosen AI success probability; its live data page reports 50% and 80% estimates, describes human baselines and repeated independent runs, and warns that the suite is domain-limited and estimates above its stated range are unreliable. The measure is task difficulty, not the time an agent spends working or general job automation. Separately, OpenAI’s 2026 SWE-bench Verified notice reports both contamination and tests rejecting functionally correct work; its later SWE-bench Pro self-audit retracts its earlier recommendation after finding task-quality problems. Treat both notices as primary lab disclosures, not independent replications, and do not assume a new benchmark is automatically sound. (S005–S006, S013–S014)
- **Statistical reporting must match the sampling design.** Recent work calls for paired item-level comparisons and a minimum-detectable-effect/resolution interpretation rather than ranking from raw score gaps; explicitly handling clustering and multiplicity; and resampling across data and model variation for multitask/multilingual settings. Error bars on a single score, repeat-to-repeat uncertainty, and uncertainty in a model-to-model difference are distinct quantities. When benchmark items are adaptively selected, use an inference method whose coverage is valid for that adaptive design. (S015–S019)

## Candidate knowledge entries

Each item is a proposed future `corpus/knowledge/` entry, not an admitted fact. `corpus/QUALITY.md` was absent in this checkout, so none can honestly be certified against the lane's admission bar yet.

### Candidate: `contamination-detection-and-transparency.md`

- **Falsifiable claim:** A negative result from one detector family does not establish that a model is uncontaminated across other contamination tiers, training stages, or access regimes; an evaluation should state detector access and scope and preserve a transparency record.
- **Source and location:** S001, ACL Anthology, Abstract; corroborating adversarial result in S002, §Abstract. Quote: “no detection method is consistently reliable across contamination tiers, model-access settings, and training stages.”
- **Coverage row filled:** New `Contamination detection and transparency` row; complements, rather than duplicates, the existing benchmark-selection contamination status and `SKILL.md` anti-pattern.
- **Recheck:** Re-read the current ACL Anthology version and its detector-family comparison at `https://aclanthology.org/2026.gem-main.50/`; check for post-training detector evaluations before each new model-family claim.
- **QUALITY gate:** Cannot certify without `corpus/QUALITY.md`. The proposed claim is narrow, tied to a peer-reviewed primary review and an explicit evidence boundary; actual admission remains unresolved.

### Candidate: `llm-judge-calibration.md`

- **Falsifiable claim:** For binary human-judged outcomes, an uncorrected LLM-judge pass fraction can be biased when sensitivity and specificity are imperfect; a calibrated estimate should carry uncertainty from both test cases and human-labeled calibration cases. Separately audit prompt-order sensitivity before using rubric scores to select or rank outputs.
- **Source and location:** S011, PMLR 306, Abstract; S010, §Abstract. Quote: “imperfect sensitivity and specificity of the LLM judges induce bias in naive evaluation scores.”
- **Coverage row filled:** New `Judge calibration` row; extends `eval-theory-notes.md`’s judge-versus-aggregator discussion and `eval-prior-art-calibration.md`’s prior-art pricing with a measured calibration protocol.
- **Recheck:** Compare the PMLR method and released implementation at `https://proceedings.mlr.press/v306/lee26bl.html` with the rubric perturbation experiments at `https://arxiv.org/html/2602.02219`; recheck when calibration labels or judge family change.
- **QUALITY gate:** Cannot certify without `corpus/QUALITY.md`. Primary proceedings and explicit calibration and prompt-perturbation scopes make the candidate auditable; admission remains unresolved.

### Candidate: `benchmark-saturation-and-retirement.md`

- **Falsifiable claim:** A benchmark is saturated only when top-model performance is both near its empirical ceiling and not reliably distinguishable under the evaluation uncertainty; a high score alone is insufficient. Report the model set, leaderboard snapshot, uncertainty assumptions, and whether the conclusion is saturation or merely stagnation.
- **Source and location:** S007, §2.1, “Definition and Scope.” Quote: “benchmark saturation as the loss of reliable discriminative power among top-performing models.”
- **Coverage row filled:** New `Benchmark saturation and lifecycle` row; updates existing stale-benchmark and selection rules with an explicit, uncertainty-aware construct.
- **Recheck:** Recompute from the paper’s public data/code at `https://arxiv.org/html/2602.16763` against a dated leaderboard snapshot; report sensitivity to the paper’s model-count and effective-sample assumptions.
- **QUALITY gate:** Cannot certify without `corpus/QUALITY.md`. The entry would label its index as one study’s operationalization, not a ground-truth quality score; admission remains unresolved.

### Candidate: `agent-time-horizon-and-task-validity.md`

- **Falsifiable claim:** A METR-style time horizon is a human-duration estimate for a specified task distribution and a specified predicted success probability; it is not agent wall-clock time or an unrestricted claim about general work. Coding-benchmark scores also require task contamination and grader-validity checks.
- **Source and location:** S014, METR, “Methodological Details.” Quote: “the task duration where the fitted curve intersects with 50% (or 80%) success probability.” S005, article body, “Why we no longer evaluate” supports the need to audit task leakage and tests.
- **Coverage row filled:** Extends the existing `Multi-turn state tracking / planning horizon` row, which README marks as an open claim, with external task-duration and task-validity methodology.
- **Recheck:** Use the dated METR data and methodology at `https://metr.org/time-horizons/`; check its displayed last-updated notice and range limitation before reusing estimates. Recheck each benchmark's task/test release notes before calling it a clean transfer set.
- **QUALITY gate:** Cannot certify without `corpus/QUALITY.md`. Keep the METR measure scoped to its task suite and keep lab self-audits attributed to their authors; admission remains unresolved.

### Candidate: `paired-eval-uncertainty-reporting.md`

- **Falsifiable claim:** For models evaluated on shared items, uncertainty in the paired item-level difference can differ materially from independent-score uncertainty; leaderboard claims should state the paired design, interval or resolution target, and any task-family clustering and multiplicity treatment.
- **Source and location:** S018, §1 and §3; S017, ACL Anthology, Abstract; S015, §2.2 and §4.2. Quote: “the assertion that A is meaningfully better than B is a statistical claim about the gap, not the gap itself.”
- **Coverage row filled:** New `Statistical reporting` row; complements the lane’s local powered paired work with an explicit reusable external reporting recipe.
- **Recheck:** Recompute a selected binary comparison using the paired diagnostic and released data/code at `https://arxiv.org/html/2605.30315`; recheck clustered/bootstrap guidance against the target benchmark’s actual task-family structure.
- **QUALITY gate:** Cannot certify without `corpus/QUALITY.md`. The claim is design-conditional and the cited papers name estimands and assumptions; admission remains unresolved.

## Paths

- **Contamination audit:** S001 → S002 → S005 → S006 — learn the taxonomy and detector limits, stress-test reasoning-model assumptions, then compare benchmark contamination with task/test validity failures.
- **Judge calibration:** S012 → S009 → S010 → S011 — start with the canonical judge failure modes, add current score/rubric perturbations, then use human calibration and uncertainty correction.
- **Agentic evidence and inference:** S013 → S014 → S005 → S006 → S018 → S017 — read the task-horizon method and current data first, scrutinize real coding-benchmark validity next, then learn paired-resolution and resampling treatment.

## Rejected candidates and mistakes mined

### Rejected candidate: use a contamination-risk factor as a general score correction

S003’s DCR paper proposes multiplying raw accuracy by a fuzzy contamination factor. Reject this as a generally valid “decontaminated accuracy” claim: the authors describe the adjusted value as risk-aware rather than an accuracy recovered after removing contamination, and list frontier-scale models and generative tasks as unvalidated. The useful salvage is to study a transparent risk checklist, not import the correction formula as a universal metric. Source: S003, §2.4.2 and §Limitations.

### Rejected candidate: treat SWE-bench Verified or Pro as an uncontested current capability meter

Reject the inference that a rising public score alone establishes coding capability progress. OpenAI’s own notices report leakage and grader/task defects for Verified, then retract their prior Pro recommendation after a separate self-audit. This does not prove that every benchmark instance is invalid; it means each release needs independent task-level validity and contamination evidence. Sources: S005, article body; S006, “Discussion.”

### Rejected candidate: private test items alone guarantee benchmark longevity

Reject the rule that secrecy prevents saturation. S007 reports no meaningful public-versus-private saturation difference in its study, but the private subset is small; the defensible lesson is to measure resolution and exposure, not to declare private data useless. Source: S007, §4.1 and study limitations.

### Rejected candidate: temperature zero plus a fixed seed makes evaluation deterministic

Reject this as a universal reproducibility claim. S016 reports nondeterminism despite those settings and recommends documenting model/API/version/parameters and uncertainty. Also preserve the target inference behavior: changing temperature solely to suppress variance can change the estimand. Source: S016, Abstract, §5, and §6.

## Leads (unopened)

- Scale’s SWE-Bench Pro primary documentation and task-level audit trail: useful counterparty material when assessing the competing creator/lab claims; not opened in this session.
- The official Terminal-Bench 2.0 and Toolathlon papers, task specifications, and scoring implementations: follow-up sources for agentic coding and multi-application tool use; not opened in this session.
- Current benchmark-maintainer releases on hidden-test governance, contamination transparency cards, and secure refresh/retirement protocols: follow-up needed before turning the contamination recommendations into an implementation checklist; not opened in this session.

## Contract defects

### DEFECT 1 — required quality gate is absent

The targeted search reported `/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/QUALITY.md` as missing. Consequently, this dossier cannot assess or claim that proposed knowledge entries pass the lane’s quality bar.

`0 — test -e /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/QUALITY.md && echo present || echo absent`

### DEFECT 2 — README has no explicit Frontier section

The README search found `## Coverage map` and `## Open gaps`, but no `## Frontier` heading, despite the lane dossier contract naming a Frontier map. Candidate coverage rows above are recommendations, not existing lane Frontier rows.

`0 — grep -cE '^## Frontier$' /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/README.md`

## Counts and reproducible counting commands

- **19 source rows** — `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-kengaku-art.md`
- **19 tier A, 0 tier B, 0 tier C** — `grep -E '^\| S[0-9]{3} ' local://kaika-w1-kengaku-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c` (only nonzero tiers are printed).
- **15 queued, 3 watch, 1 rejected** — `grep -E '^\| S[0-9]{3} ' local://kaika-w1-kengaku-art.md | awk -F'|' '{gsub(/ /,"",$7); print $7}' | sort | uniq -c`
- **5 candidate knowledge entries** — `grep -c '^### Candidate:' local://kaika-w1-kengaku-art.md`
- **4 mistakes mined and retained as rejected candidates** — `grep -c '^### Rejected candidate:' local://kaika-w1-kengaku-art.md`
- **2 contract defects found** — `grep -c '^### DEFECT ' local://kaika-w1-kengaku-art.md`

## SOURCES.md draft rows

All rows below were opened in this session. Tier A means primary research, official proceedings, official lab disclosures, or current maintainer data; the 2023 judge paper and 2024 statistical paper are retained as canonical methods, not mistaken for current art. No source is marked mined because none is yet cited by an admitted lane knowledge entry.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Are LLM Benchmarks Already Contaminated? A Systematic Review of Contamination Detection Methods — https://aclanthology.org/2026.gem-main.50/ | paper | A | Taxonomy of contamination tiers, detector families, access assumptions, failure modes, and transparency cards; concludes detector reliability is not universal. | queued | 2026-10-19 | 90d | — |
| S002 | On The Fragility of Benchmark Contamination Detection in Reasoning Models — https://arxiv.org/html/2510.02386v1 | paper | A | Controlled reasoning-model study of contamination inflation and detector signals being concealed after reinforcement-learning updates. | queued | 2026-10-19 | 90d | — |
| S003 | DCR: Quantifying Data Contamination in LLMs Evaluation — https://arxiv.org/html/2507.11405 | paper | A | Proposes a fuzzy contamination-risk factor and adjusted accuracy; narrow experiments and explicit limitations make it a rejected general score-correction candidate. | rejected | 2026-10-19 | 90d | — |
| S004 | LLM Benchmark Datasets Should Be Contamination-Resistant — https://arxiv.org/abs/2605.19999 | paper | A | Proposes benchmark construction that resists learning during training while remaining useful at inference. | queued | 2026-10-19 | 90d | — |
| S005 | Why SWE-bench Verified no longer measures frontier coding capabilities — https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | docs | A | OpenAI’s primary disclosure of contamination concerns and test cases rejecting functionally correct work; recommends retiring Verified as its primary coding signal. | watch | 2026-10-19 | on-release | — |
| S006 | Separating signal from noise in coding evaluations — https://openai.com/index/separating-signal-from-noise-coding-evaluations/ | docs | A | OpenAI’s follow-up Pro task audit reports task-quality problems and retracts its previous recommendation; a lab self-audit, not independent replication. | watch | 2026-10-19 | on-release | — |
| S007 | When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation — https://arxiv.org/html/2602.16763 | paper | A | Defines saturation through top-model discrimination and evaluation uncertainty; studies benchmark properties and lifecycle implications. | queued | 2026-10-19 | 90d | — |
| S008 | Measuring what Matters: Construct Validity in Large Language Model Benchmarks — https://arxiv.org/abs/2511.04703 | paper | A | Systematic review of benchmark construct validity and actionable guidance for aligning claims, tasks, and metrics. | queued | 2026-10-19 | 90d | — |
| S009 | Evaluating Scoring Bias in LLM-as-a-Judge — https://arxiv.org/html/2506.22316 | paper | A | Measures scoring-prompt bias from rubric order, score identifiers, and reference-answer scores with stability and human-alignment metrics. | queued | 2026-10-19 | 90d | — |
| S010 | Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge — https://arxiv.org/html/2602.02219 | paper | A | Finds model-specific score-position and criterion-order bias; compares balanced and random rubric permutations and their effects on rankings. | queued | 2026-10-19 | 90d | — |
| S011 | How to Correctly Report LLM-as-a-Judge Evaluations — https://proceedings.mlr.press/v306/lee26bl.html | paper | A | ICML method for correcting judge sensitivity/specificity bias and constructing confidence intervals with both test and human-calibration uncertainty. | queued | 2026-10-19 | 90d | — |
| S012 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena — https://arxiv.org/html/2306.05685v4 | paper | A | Canonical judge study documents position, verbosity, and self-enhancement concerns and compares judgments with human preferences. | queued | 2026-10-19 | 90d | — |
| S013 | Measuring AI Ability to Complete Long Software Tasks — https://arxiv.org/html/2503.14499 | paper | A | Defines human-duration task horizons, task-suite baselines, repeated attempts, hierarchical uncertainty, and external-validity limitations. | queued | 2026-10-19 | 90d | — |
| S014 | Task-Completion Time Horizons of Frontier AI Models — https://metr.org/time-horizons/ | dataset | A | Current METR horizon data and methodology, with 50% and 80% reliability views, human-time anchors, suite limitations, and a page update notice. | watch | 2026-10-19 | 90d | — |
| S015 | Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations — https://arxiv.org/html/2411.00640 | paper | A | Canonical recommendations for paired comparisons, clustered uncertainty, power analysis, and reporting question counts and standard errors. | queued | 2026-10-19 | 90d | — |
| S016 | Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores — https://arxiv.org/html/2410.03492 | paper | A | Repeated-run uncertainty study; documents residual nondeterminism and recommends recording model, API, version, settings, and uncertainty method. | queued | 2026-10-19 | 90d | — |
| S017 | Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation — https://aclanthology.org/2025.ijcnlp-long.125/ | paper | A | Resampling method for model and data variation in multilingual/multitask results, including leaderboard ranks and pairwise differences. | queued | 2026-10-19 | 90d | — |
| S018 | Resolution Diagnostics for Paired LLM Evaluation — https://arxiv.org/html/2605.30315 | paper | A | Paired-test resolution, minimum detectable effects, required sample sizes, and sensitivity to clustering, multiplicity, and sequential stopping. | queued | 2026-10-19 | 90d | — |
| S019 | Efficient Evaluation of LLM Performance with Statistical Guarantees — https://arxiv.org/html/2601.20251 | paper | A | Adaptive query selection with finite-bank frequentist confidence coverage; clarifies that adaptive sampling needs design-valid inference. | queued | 2026-10-19 | 90d | — |
