# Kaika W1 — Current art: learning from mistakes

## Executive synthesis

**Observed:** the fleet already has a real learning loop, not a blank slate. `LEARNING.md` requires curation, candidate admission through `QUALITY.md`, understanding fed back into `SKILL.md`/`QUALITY.md`, and frontier expansion; every round's lesson records candidates admitted and rejected with reasons plus a non-author spot-check of at least one admit and one reject. `CORPUS.md` requires evidence-bearing lessons, source/verification/recheck fields for knowledge, falsifiable claims or explicit opinion, and an append-only correction discipline. `AXES.md` admits an exploratory claim only as `unprovable-but-better` with a named non-author reviewer; without that review it remains `unprovable` and honest-stop applies. `PROTOCOL.md` specifies evidence, revision-pinned audit, durable routed-defect follow-up, and the no-axis-harmed admission bar. These are good foundations, especially the rejection-as-evidence and outside-review rules.

**Research finding:** do not encode “ask the model to reflect” as a general correction method. A prompted model can identify or fix some errors under special conditions, yet ungrounded self-review is unreliable and can regress a correct result. The stronger operational pattern is: locate the failure; preserve the observable evidence; propose a corrective rule; validate it against an independent verifier or a matched before/after check; retain the lesson only if it improves without hidden regressions; and leave uncertainty explicit. For human teams, the companion pattern is a psychologically safe, reviewed postmortem whose action items are checked for closure, plus a short premortem to surface risks before work begins. Keep one failure as a case; require corroboration or a counterexample check before turning it into a general rule.

**Evidence boundary:** papers establish performance on named tasks and benchmarks, not universal agent or organizational learning. Google SRE and Klein are authoritative practice guidance, not randomized causal trials. Error-management training has a cross-study meta-analysis, but it concerns human skill training, not shokunin corpus admission. AIID documents a persistent, searchable incident archive proposed as a shared-learning mechanism; [INFERENCE] archived public reports alone do not establish prevalence or that a database by itself prevents recurrence.

## Fleet footing and scoped gap

- `LEARNING.md` §§“The learning path,” “The three trends,” and “Discernment is checked from outside” already connect a gate disagreement to a lesson and a grounded `QUALITY.md` criterion; lessons have a `## Gate` with candidates, decisions, reasons, and spot-check result.
- `CORPUS.md` §§“Rules” and “Rules added from the round-1/2 corpus audits” already require re-resolvable evidence, falsifiability or marked opinion, source/verified-at/recheck frontmatter, repro commands for corpus counts, sweeps for negative claims, and append-only corrections.
- `AXES.md` §§“Working the axes” already says that every round's claims must verify and no axis may be harmed; its exploratory route demands a named non-author reviewer and honors honest-stop.
- `PROTOCOL.md` §§“Evidence standard,” “Gate standard,” and “File contract per shokunin repo” already pin audit verdicts to a revision and preserve routed defects; `PROTOCOL-APPENDIX.md` is a durable case history of evidence, ledger, gate, and census failures.

**One scoped contract enhancement candidate [INFERENCE], not a confirmed defect:** the reviewed fleet-level learning text discusses what the gate got right or wrong, error patterns, and checklists, but does not make a causal postmortem record (observed event → contributing conditions/root-cause hypothesis → correction → independent recurrence/regression check) an explicit round-lesson criterion. This is only a finding about the named fleet files, not about all lane `QUALITY.md` files; no lane-specific quality bar was in scope. The search used to assess this wording was `grep -nEi 'root.?cause|causal|contribut|postmortem|regression|recurr|failure analysis|mistake|error pattern' PROTOCOL.md PROTOCOL-APPENDIX.md CORPUS.md LEARNING.md AXES.md`.

## Evidence map: mechanism, strength, and craft implication

| Area | Mechanism and primary findings | Evidence strength and boundary | Shokunin implication |
|---|---|---|---|
| **Intrinsic LLM self-correction** | Huang et al. find that asking a model to verify/revise its own reasoning without external feedback often fails and can damage performance. Tyen et al. separate error localization from repair: models struggle to find an error, but improve when given its location. Wu et al. show a task-specific counterexample: ProCo turns an answer into a masked-condition verification question and reports gains on three reasoning settings. A 2024 preprint by Liu et al. also reports intrinsic improvement under zero-temperature, carefully controlled prompts, but explicitly omits reasoning tasks. Kamoi et al.'s TACL survey finds that results depend on task, feedback, and fair evaluation; their synthesis does not support a general claim that prompting alone reliably corrects mistakes. Later ACL work reports wavering/prompt bias and cognitive bias; ACL 2026 RefineBench finds modest self-refinement and much stronger guided refinement. | **Mixed across definitions, with a consistent caution for unguided review.** Several peer-reviewed studies and a broad TACL survey find failure or regressions; other work finds narrow, prompt-structured or task-specific gains. These are not all strict replications of Huang: they differ in task, starting answer, prompt, feedback and metric. The 2024 intrinsic-correction counterpoint is an arXiv preprint and excludes reasoning. RefineBench is a recent broad open-ended benchmark; SCoRe demonstrates a separate exception via online RL training, not an innate property of an unmodified model. | In lessons, record initial correctness and post-revision correctness separately, including correct→incorrect regressions. “The model reflected” is not evidence of a fix. A factual/subjective claim without a reliable verifier stays unproven. Allow a structural verification question when the domain supplies one, but cite and test it as a bounded method, not a universal capability. |
| **Tool- and verifier-grounded correction** | CRITIC alternates an initial answer, relevant tools (e.g., search or interpreter), evidence-backed critique, and correction. Self-Debugging executes candidate code, feeds back execution/test results, and asks the model to explain its program; on tasks without tests, explanation alone is weaker evidence. The crucial distinction is between a generated critique and an observable external result. | **Moderate-to-strong for the tested tasks, not universal.** Peer-reviewed benchmark studies report gains in QA, program synthesis, and code generation; they include task-specific test/evidence conditions and older model snapshots. Tool feedback may itself be incomplete or irrelevant, and passing a finite test set is not proof of universal correctness. | Preserve tool output, failing assertion, relevant input and revision together. The lesson must name what the verifier actually established and what remains untested. Use the same baseline and post-change verifier; count regressions, not only successful repairs. A model-authored explanation is not an independent verdict. |
| **Failure-memory and error notebooks in agents** | Reflexion turns task feedback into concise verbal reflection held in an episodic memory for future attempts. ExpeL collects success/failure trajectories, extracts cross-task insights and retrieves successful examples; its study reports that adding raw reflections to insight extraction could mislead the resulting insights. ACL 2026 Mistake Notebook Learning clusters batch failures into subject-level notes and keeps a memory update only when measured batch performance improves. AgentDebug decomposes trajectories into memory/reflection/planning/action/system errors, seeks the earliest critical error, and provides targeted retry guidance. | **Moderate task-benchmark evidence, weak evidence for indefinite or organization-wide learning.** Reflexion and ExpeL show gains on selected agent tasks; MNL's recent peer-reviewed study spans reasoning, Text-to-SQL and interactive tasks and includes ablations, but itself notes judge/verifier bias, retrieval granularity and memory lifecycle risks. AgentDebug is an arXiv preprint with a small manually annotated benchmark and only moderate annotator agreement (reported κ = 0.55; S016, §2.2). None establishes that every one-off error should become a permanent general rule. | Keep the incident and its evidence even when it is singular; distinguish a case note from a generalized reusable rule. Generalize from repeated/corroborated patterns or an independently verified causal explanation. Keep the note short, scoped, retrievable, and testable; compare baseline and post-note behavior and discard/regard as unproven a note that regresses performance. Never treat an LLM judge's binary label as ground truth. |
| **Human expert teams: blameless postmortems** | Google SRE's practice records impact, response, contributing/root causes, and preventive actions; it defines triggers in advance, assumes participants acted with the information available, requires review, and stores reviewed cases for sharing. The point is to fix information, system and process conditions rather than shame individuals. | **Authoritative operating guidance and a mature practitioner case, not a controlled estimate of causal effect.** It supports what a useful process looks like and why reporting safety matters; it does not quantify the treatment effect of “blamelessness.” | Round lessons should report the observed context and contributing conditions without assigning moral blame. Distinguish direct cause, contributing conditions, hypotheses, and unknowns. End each accepted lesson with a prevention/detection action and a later check that the action landed and recurrence risk changed. Review the artifact; an unreviewed lesson is not a closed learning loop. |
| **Human teams: premortems** | Klein's premortem has participants imagine the planned project has already failed and independently generate plausible reasons before discussing them. This gives knowledgeable dissenters a low-cost opening to surface risks that ordinary prospective planning may suppress. | **Expert-origin practice proposal; evidence here is the original HBR article, not a controlled outcome trial.** Treat it as a planning aid, not a guarantee that risk prediction is complete or accurate. | Before a risky round, use a bounded “assume this round failed” prompt and record a few falsifiable risks, the signal that would detect each, and the stop/rollback condition. Do not let a premortem become a post hoc explanation or an extra score. |
| **Error-management training** | Keith and Frese's meta-analysis studies active exploration with explicit permission to make errors and learn during training. Across 24 studies (N = 2,183) they report a positive mean effect (Cohen's d = 0.44); effect is larger for post-training transfer (d = 0.56) and structurally distinct/adaptive transfer tasks (d = 0.80). They identify both active exploration and error encouragement as effective elements (S017, abstract). | **Strongest quantitative evidence in this set for human training transfer, but indirect for shokunin.** It concerns skill acquisition under training conditions, not autonomous agents, corpus admission, or mistakes in production. | Run experiments in a reversible sandbox with explicit error budgets and expected observations; then require a debrief and transfer check on a structurally different task. Never interpret error encouragement as permission to risk live data, credentials, users, or unreviewed production changes. |
| **Case libraries / AI incident databases** | AIID gives incidents persistent identities, linked reports, search and multiple purpose-specific taxonomies; its official pages invite ongoing submissions and describe an adaptive incident definition. Its 2025 editor study finds structural ambiguity and unavoidable epistemic uncertainty around cause, harm extent, severity and system details. | **Direct evidence for the repository's operation and design; no causal evidence that it alone reduces incidents.** [INFERENCE] The inspected AIID material describes public reports and voluntary submission but does not establish census coverage or exposure-adjusted incident rates. Taxonomy choices and editorial updates affect what can be counted. | Keep a searchable, append-only rejected/accepted case history with source links, dates and provenance. Preserve “unknown”/disputed fields and corrections as new records. Use cases to generate candidate checks and counterexamples, not to infer prevalence from counts or to present an incident report as a complete causal investigation. |

### Overall reading

The most defensible “continuous improvement” loop is not more self-critique; it is **evidence → localization → bounded correction → independent check → durable, reviewable lesson → recheck on later work**. A single error is enough to file a case, halt unsafe continuation, or correct a verified local defect. It is not by itself enough to claim that a broad new rule is generally true. Repeated patterns improve confidence in a general rule but still need counterexamples, appropriate scope, and the lane's own quality bar. Protect contributors from blame while remaining exacting about claims and outputs.

## Proposed round-note and quality-bar design

### Add to a round lesson's `## Mistakes` (proposal)

For each material failure, retain a compact record with:

- **Observed signal:** the exact failed check, output, mismatch or near miss; path/URL and relevant revision; no secrets or credentials.
- **Impact and scope:** what it affected and what did not; do not inflate a local defect into a fleet-wide claim.
- **Cause status:** direct observation vs. root-cause hypothesis vs. contributing condition vs. unresolved unknown. Preserve competing explanations where evidence does not distinguish them.
- **Correction and independent verification:** what changed; the reproducible command/citation, exact revision, baseline and post-change results, regression check and non-author reviewer. For subjective exploratory work, preserve the required named reviewer and reason instead of inventing a numeric score.
- **Gate decision:** admitted, rejected, or held; reason. A rejection is retained as evidence of taste, not erased as failure to curate.
- **Follow-through:** action owner/scope and next-round recheck. Carry an unresolved defect in the durable routed-defect ledger, not solely in lesson prose.

Use this as a shaping proposal, not a replacement for the existing `## Gate` contract or lane-specific format. Blameless means no person-scoring; it does not mean vague cause, unverified repair, or missing accountability for actions.

### Candidate `QUALITY.md` criteria (adapt to each lane; cite the producing lesson)

| Proposed criterion | Admission test | Research grounding |
|---|---|---|
| **Observed facts precede causal interpretation.** | An entry distinguishes source-observed facts from inference, names the conditions needed to reproduce the failure, and labels unknowns. No unsupported “root cause.” | Google SRE postmortems; AIID editor uncertainty; AgentDebug root-cause localization. |
| **A correction is not admitted because a model says it worked.** | A resolvable independent verifier or non-author review checks the before/after result at a pinned revision; record regressions and test limits. Unsupported outcomes remain unproven. | Huang; Kamoi; CRITIC; Self-Debugging; RefineBench. |
| **A general rule needs generalization evidence.** | A one-off incident may be admitted as a scoped case; a reusable principle names its scope and is supported by repeat cases, counterexamples or a distinct-task transfer check. | ExpeL; MNL; error-management training. |
| **Memory updates must be reversible and non-regressive.** | Show the previous and proposed note, the retrieval/use context, and matched post-update result. Reject or quarantine a note when an independent check is absent or a regression appears. | MNL accept-if-improves; ExpeL's failure/reflection ablation; protocol no-harm rule. |
| **Every admitted lesson yields a checkable prevention/detection action.** | State what future command, audit or task will detect recurrence, and when the check is due. A lesson without a verified action may remain a useful case, but not a claimed prevention. | Google SRE postmortem action/review loop; `LEARNING.md`'s lesson-to-quality feedback. |
| **Case counts represent the archive, not the world.** | A count carries its exact command and snapshot/date; coverage/selection limits are named; disputed classifications remain visible. | AIID snapshots and 2025 editor study; existing `CORPUS.md` count/negative-claim rules. |

A gate should preserve rejections and the criterion that rejected them. If an outside reviewer disagrees, the next change is a lesson and a grounded criterion, not quiet rewriting of the old decision. This is already aligned with `LEARNING.md` and append-only corpus rules.

## Honest-stop and audit-round implications

### Honest-stop

- If the only “evidence” that an answer changed correctly is the same model's unaided self-review, stop the *claim of correction*: record the attempt and say what verifier or human evidence is missing. Do not falsely call it a failure if the outcome is unknown; do not promote it as an improvement.
- If a causal explanation is plausible but not separated from alternative causes, label it as a hypothesis and scope the lesson to the observed case. Do not make a universal rule from unlocated errors or an unrepresentative incident archive.
- If the needed checker, comparator, baseline, or independent reviewer is unavailable, mark the affected criterion `unprovable`/`could-not-evaluate` as the existing protocol requires and route the missing evidence. For exploratory claims, preserve the existing named-non-author gate; no author self-attestation can substitute.
- If corrective work creates a real trade, report each axis verdict and stop admission under the current no-harm rule. The learnings below do not justify suppressing a harmed axis or turning failure into an aggregate scalar score.

This is calibrated stopping, not a ban on exploration: use reversible safe experiments, report the unknown precisely, and make the next probe falsifiable.

### Audit rounds

1. **Before work:** when risk warrants, run the Klein-style premortem. Keep it short; for each risk name a leading indicator and a safe stop/rollback. Recheck that the round's proposed claim and verifier can actually distinguish success from a plausible failure.
2. **After the attempt:** review the evidence and the candidate gate decision, not the author's confidence. The current outside spot-check (one admit and one reject at minimum) is a valuable guard; retain a reasoned `agree`/`disagree` for each.
3. **At closure:** verify citations and commands against the revision they describe, inspect the committed output and check for regression. Keep gate capability/self-test separate from measurement, per the current gate standard.
4. **At the next audit:** recheck action closure and recurrence using the same criterion where possible, plus a counterexample/transfer sample when the lesson claims a general principle. Re-flag unresolved routed defects; do not let a missing report or a prose-only action item disappear.
5. **Across the corpus:** audit rejected entries and stale sources as deliberately as admitted entries. Use an incident database to find candidate counterexamples, not prevalence estimates. Preserve reviewer disagreement as a calibration lesson.

This adds causal depth to current protocol audits; it does not replace the existing append-only ledger, version pins, outside review, status rules, or per-axis verdicts.

## Mistakes mined from research and fleet evidence

These are recurring patterns, not a count of individual incidents:

- **M1 — “Reflect again” can worsen a correct answer.** Intrinsic revision without a trustworthy signal has documented regressions; score error→correct and correct→error separately. Sources: S001, S004, S007, S009.
- **M2 — Repair depends on finding the right error.** Supplying the error location can change repair success; root-cause localization and surface-error counting are not equivalent. Sources: S002, S016.
- **M3 — A reflection can itself be a hallucinated memory.** ExpeL reports an ablation where adding raw reflections to insight construction is disadvantageous; do not make reflection text an admitted fact without checking it against the trajectory. Source: S014.
- **M4 — Memory growth can overfit or regress.** MNL's batch guard, clustering ablation and stated verifier limits motivate evaluation before retaining a generalized note. Sources: S015, S014.
- **M5 — An incident archive is epistemically incomplete.** Cause, harm and system facts can be ambiguous; [INFERENCE] the public case archive should not be treated as a random sample. Keep unknowns and provenance rather than turning case frequencies into risk rates. Sources: S020–S024.
- **M6 — A postmortem that is unreviewed or not durable does not close the loop.** Google SRE says to review postmortems; the fleet appendix itself records routed defects lost in report prose and evidence pointers that no longer resolve. Sources: S018, S029.

Fleet examples mined from `PROTOCOL-APPENDIX.md` include unresolvable evidence pointers, defects stranded in prose instead of the durable ledger, gate results changing with the revision/snapshot, and census blind mass. Those are not evidence that the relevant lanes acted badly; they are evidence that precise, revision-bound and durable process checks matter.

## Candidate knowledge entries for the fleet corpus

These are candidates, not admitted entries. Each quote is short and names its exact location; each recheck is citation-based or explicitly requires a runnable verifier once a lane applies the lesson. Targets refer to the existing fleet contract surface, not to an inspected lane's private `QUALITY.md`.

### `intrinsic-revision-is-not-proof`

- **Claim:** A prompted revision without new evidence can regress; admit an accuracy improvement only when the before/after result passes an independent, revision-pinned check and the regression direction is measured.
- **Source and quote:** S001, Huang et al., ICLR abstract: “at times, their performance even degrades after self-correction.” (URL + `Abstract`). S009 provides the broader recent open-ended refinement benchmark (URL + `Abstract`).
- **Coverage target:** `LEARNING.md` §Quality gating and `CORPUS.md` §Rules; adds explicit correction/regression evidence to the existing admission loop.
- **Recheck:** Compare the initial and revised outputs on the same recorded task set with the cited independent evaluator; review S001 and S009 abstracts on each source refresh. Do not count the claim from reflection text alone.
- **QUALITY fit:** Falsifiable; cites primary benchmark papers and requires a reproducible local verifier. Keep benchmark-scope caveat in the entry.

### `localize-before-generalizing-a-failure`

- **Claim:** An actionable error lesson names the earliest supported failure point and separates it from downstream symptoms; a single event is a case, not by itself a universal rule.
- **Source and quote:** S002, Tyen et al., abstract: “this boosts downstream task performance across our 5 reasoning tasks”; the same abstract conditions repair on supplied error location. S016, AgentDebug, §2 and §3, tests root-cause localization and targeted retry.
- **Coverage target:** `corpus/lessons/round-<N>.md` `## Mistakes` and `## Gate`; extends the existing round lesson with causal status and scope.
- **Recheck:** Revisit the named trajectory and its observed signal; for a general rule, test a repeated or distinct-task case and a counterexample. Cite S002/S016 at their abstracts/method sections; a specific lane entry must supply the exact domain command.
- **QUALITY fit:** Separate observation, hypothesis and outcome; preserve unknowns. Does not require many incidents before logging a high-risk one-off.

### `reviewed-postmortem-needs-verified-action`

- **Claim:** A failure lesson is not closed by an explanation alone; it needs review and a preventive/detection action whose completion and effect are rechecked.
- **Source and quote:** S018, Google SRE, §“Best Practice: No Postmortem Left Unreviewed”: “An unreviewed postmortem might as well never have existed.”
- **Coverage target:** `LEARNING.md` §The learning path and `PROTOCOL.md` audit/defect routing; makes follow-up to a failure lesson visible.
- **Recheck:** At next audit, cite the action's commit or tracked artifact and rerun its named test; retain the postmortem citation for the process rule.
- **QUALITY fit:** The lesson needs resolvable cause/evidence, an executable follow-up, and a non-author review; no individual blame.

### `premortem-makes-risk-speakable-before-the-round`

- **Claim:** A brief failure-imagining prompt before risky work can surface a falsifiable risk and stop condition that ordinary plan review missed; treat it as hypothesis generation, not risk proof.
- **Source and quote:** S019, Klein, HBR article, `Summary`: “assume that the project they are planning has just failed”.
- **Coverage target:** `PROTOCOL.md` round planning / `.ufo` prompts; supplements, rather than replaces, the actual verifier and round contract.
- **Recheck:** Compare each predicted risk with the round's observed outcome and keep misses as well as hits; re-read the original HBR summary and method description on refresh.
- **QUALITY fit:** Candidate is explicitly a practice hypothesis with low causal-evidence strength; admit only if the fleet's round review observes value without adding unbounded ceremony.

### `incident-cases-preserve-uncertainty-and-provenance`

- **Claim:** [INFERENCE] A searchable incident collection helps teams find earlier failure cases, but public reports and taxonomy labels alone do not establish true incident rates or complete causal stories.
- **Source and quote:** S022, AIID About, `Why AI Incidents?`: “The database is a constantly evolving data product and collection of applications.” S021, Paeth et al., AAAI abstract, reports unavoidable epistemic uncertainty in causes, harm extent, severity and system details.
- **Coverage target:** proposed fleet `corpus/SOURCES.md` and `corpus/lessons/round-<N>.md` case provenance; complements the append-only lesson and rejected-candidate history.
- **Recheck:** Use a dated snapshot and record its date for any count (S024, `Database Snapshots`); follow the individual incident source citations and retain unknown/disputed classifications.
- **QUALITY fit:** Require source provenance, event date vs report date where available, scope/uncertainty, and no prevalence claim from raw counts.

### `safe-error-management-is-a-training-condition`

- **Claim:** Structured active exploration plus permission to make and learn from errors can improve human skill transfer; apply it to reversible practice and verify transfer rather than tolerating production harm.
- **Source and quote:** S017, Keith & Frese, abstract: “both active exploration and error encouragement were identified as effective elements in EMT.”
- **Coverage target:** `LEARNING.md` §Curation and §Expanding perspective; provides a human-training rationale for safe exploratory rounds.
- **Recheck:** Re-read S017's abstract and moderator results; any lane applying it must define a sandbox, maximum impact, and a transfer task before counting the claim.
- **QUALITY fit:** Keeps the empirical boundary explicit (human training, not agent corpus); admission requires a safe, executable trial and an observable transfer result.

## Study paths

- **LLM correction: limits → diagnosis → verifier → current benchmark:** S001 → S002 → S004 → S003 → S011/S012 → S009 → S010. First separate “can correct when located” from “can detect its own error”; then study external evidence and the latest refinement/training boundaries.
- **Human/team learning: surface risk → learn safely → review → preserve cases:** S019 → S017 → S018 → S020 → S021. Begin with ex-ante dissent, move through safe error-management practice, then compare postmortem review with an incident library that preserves uncertainty.

## Rejected candidates and reasons

- **Rejected: “An LLM's confident self-critique proves the repair.”** The self-review signal is not independent; Huang and RefineBench report weak or regressive intrinsic refinement, while the survey distinguishes reliable task feedback from prompted self-feedback. (S001, S004, S009.)
- **Rejected: “Every single failure should become a permanent general rule.”** A one-off case should be preserved, but generalization without scope, repeated evidence or a distinct-task check risks overfitting; MNL uses batch abstraction and its own paper acknowledges verifier/memory limits. (S014–S016.)
- **Rejected: “Count incidents to compare who is worst.”** [INFERENCE] AIID's public case records cannot be assumed complete or exposure-adjusted; SRE's blameless rationale is to expose systemic conditions rather than punish the person who surfaced them. (S018, S020–S024.)
- **Rejected: “A pre-mortem predicts failure, so its risk list is a verified finding.”** Klein's article is a planning intervention, not an oracle or outcome guarantee; keep predictions as hypotheses and measure hits and misses. (S019.)

## Leads (unopened)

- AIID's contributed taxonomy directory (`https://incidentdatabase.ai/taxonomies/`) — inspect definitions and annotation guidelines before adopting any incident categories in a fleet-wide case schema.
- Agentic Context Engineering and Memento, cited in S015's related work — inspect their primary papers/code before comparing their memory-update and retention policies to a shokunin corpus.
- Error-management training's broader meta-analysis trail and newer replications — S017 is foundational and quantitative, but it is older and human-training-specific.

## Fleet-level SOURCES registry candidates

All rows below were opened during this research session. `queued`/`watch` is intentional: none is yet used by an admitted `knowledge/` entry, so `mined` would overstate status. Rows include opened date and a recheck cadence/citation; `used-by` is `—` until a real entry cites the source. Tiers follow the draft registry contract: primary/authoritative sources are A; Kamoi et al.'s critical survey is B secondary synthesis.

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | Large Language Models Cannot Self-Correct Reasoning Yet — https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html | paper | A | Intrinsic self-correction in reasoning can fail or regress without external feedback. | queued | 2026-10-19 | 180d | — |
| S002 | LLMs cannot find reasoning errors, but can correct them given the error location — https://arxiv.org/abs/2311.08516 | paper | A | Separates error localization from repair and shows correction improves when error location is supplied. | queued | 2026-10-19 | 180d | — |
| S003 | Large Language Models Can Self-Correct with Key Condition Verification — https://aclanthology.org/2024.emnlp-main.714/ | paper | A | ProCo uses masked-condition verification and reports task-specific intrinsic self-correction gains. | queued | 2026-10-19 | 180d | — |
| S004 | When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey — https://aclanthology.org/2024.tacl-1.78/ | paper | B | Synthesizes when prompting, external feedback and fine-tuning support correction; flags evaluation confounds. | queued | 2026-10-19 | 180d | — |
| S005 | Large Language Models Have Intrinsic Self-Correction Ability — https://arxiv.org/abs/2406.15673 | paper | A | Reports an intrinsic-correction counterpoint under zero-temperature and fair-prompt conditions; reasoning is out of scope. | queued | 2026-10-19 | 180d | — |
| S006 | Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot — https://arxiv.org/abs/2507.02778 | paper | A | A preprint finds error attribution/framing changes whether models activate correction; track it separately from knowledge. | watch | 2026-10-19 | on-release | — |
| S007 | Understanding the Dark Side of LLMs’ Intrinsic Self-Correction — https://aclanthology.org/2025.acl-long.1314/ | paper | A | Reports instability, prompt bias and cognitive bias in intrinsic revision across studied tasks. | watch | 2026-10-19 | 180d | — |
| S008 | Moral Self-correction is Not An Innate Capability in Language Models — https://aclanthology.org/2025.findings-ijcnlp.39/ | paper | A | Studies moral sensitivity and feedback incorporation; do not generalize correction capability across domains. | watch | 2026-10-19 | 180d | — |
| S009 | RefineBench: Evaluating Refinement Capability of Language Models via Checklists — https://proceedings.iclr.cc/paper_files/paper/2026/hash/835b6c04ca2daaa1a682c2eaad4a70ea-Abstract-Conference.html | paper | A | A broad open-ended benchmark finds self-refinement modest and guided refinement much stronger. | watch | 2026-10-19 | on-release | — |
| S010 | Training Language Models to Self-Correct via Reinforcement Learning — https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf | paper | A | SCoRe reports trained intrinsic correction using on-policy multi-turn RL and shaped progress reward. | watch | 2026-10-19 | on-release | — |
| S011 | CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing — https://arxiv.org/html/2305.11738v4 | paper | A | Tool-produced evidence supports iterative correction in the studied QA, code and toxicity tasks. | queued | 2026-10-19 | 180d | — |
| S012 | Teaching Large Language Models to Self-Debug — https://arxiv.org/html/2304.05128 | paper | A | Execution and test results plus explanation guide code repair; task evidence varies with test availability. | queued | 2026-10-19 | 180d | — |
| S013 | Reflexion: Language Agents with Verbal Reinforcement Learning — https://arxiv.org/html/2303.11366 | paper | A | Agents store task-feedback-derived reflections in episodic memory for later trials. | queued | 2026-10-19 | 180d | — |
| S014 | ExpeL: LLM Agents Are Experiential Learners — https://ojs.aaai.org/index.php/AAAI/article/view/29936 | paper | A | Agents abstract cross-task insights from successes and failures and retrieve useful examples. | queued | 2026-10-19 | 180d | — |
| S015 | Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation — https://aclanthology.org/2026.findings-acl.719/ | paper | A | Clusters related failures into reusable notes and retains memory updates only after measured improvement. | watch | 2026-10-19 | on-release | — |
| S016 | Where LLM Agents Fail and How They Can Learn From Failures — https://arxiv.org/html/2509.25370 | paper | A | A preprint classifies agent failure modules, traces cascades and tests targeted root-cause debugging. | watch | 2026-10-19 | on-release | — |
| S017 | Effectiveness of Error Management Training: A Meta-Analysis — https://pubmed.ncbi.nlm.nih.gov/18211135/ | paper | A | Meta-analysis finds positive transfer from active exploration and error encouragement in human skill training. | queued | 2026-10-19 | 180d | — |
| S018 | Google SRE Book, Chapter 15: Postmortem Culture — https://sre.google/sre-book/postmortem-culture/ | book | A | Blameless, reviewed postmortems preserve causes and preventive actions for shared learning. | queued | 2026-10-19 | 365d | — |
| S019 | Performing a Project Premortem — https://hbr.org/2007/09/performing-a-project-premortem | paper | A | Klein's prospective-hindsight method invites early risk disclosure before a project fails. | queued | 2026-10-19 | 365d | — |
| S020 | Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database — https://ojs.aaai.org/index.php/AAAI/article/view/17817 | paper | A | A persistent, searchable incident archive supports cross-organization learning and avoidance. | queued | 2026-10-19 | 365d | — |
| S021 | Lessons for Editors of AI Incidents from the AI Incident Database — https://ojs.aaai.org/index.php/AAAI/article/view/35163 | paper | A | Incident editors face structural ambiguity and unavoidable uncertainty about causes and harm details. | watch | 2026-10-19 | 365d | — |
| S022 | AI Incident Database About — https://incidentdatabase.ai/about/ | docs | A | AIID is an evolving public case collection with shared discovery and contribution surfaces. | watch | 2026-10-19 | 90d | — |
| S023 | Defining an AI Incident — https://incidentdatabase.ai/research/1-criteria/ | docs | A | AIID uses adaptive acceptance criteria because incident boundaries are not universally settled. | watch | 2026-10-19 | 90d | — |
| S024 | AIID Database Snapshots — https://incidentdatabase.ai/research/snapshots/ | dataset | A | Weekly point-in-time dumps support reproducible incident analyses and date-bound counts. | watch | 2026-10-19 | 90d | — |
| S025 | Shokunin Learning Path — `LEARNING.md` | own-work | A | The fleet already requires evidence-based curation, admission, lessons and external spot-checking. | queued | 2026-10-19 | on-protocol-change | — |
| S026 | Shokunin Corpus Contract — `CORPUS.md` | own-work | A | The fleet requires source/recheck metadata, falsifiability, count commands and append-only correction. | queued | 2026-10-19 | on-protocol-change | — |
| S027 | Fleet Protocol — `PROTOCOL.md` | own-work | A | The protocol pins evidence, audit revisions, gates, file contracts and durable defect routing. | queued | 2026-10-19 | on-protocol-change | — |
| S028 | Shokunin Axes — `AXES.md` | own-work | A | Exploratory improvement uses named outside review, per-axis verdicts and honest-stop. | queued | 2026-10-19 | on-protocol-change | — |
| S029 | Protocol Incident Appendix — `PROTOCOL-APPENDIX.md` | own-work | A | Fleet incidents document the failure modes that motivate evidence, ledger, gate and census controls. | queued | 2026-10-19 | on-protocol-change | — |

## Unresolved limits

- The 2025 and 2026 agent-memory/correction literature is moving quickly; new benchmark papers are not evidence of long-term retention or team-level recurrence reduction.
- Some highly relevant papers were available as abstracts or preprints; detailed experimental protocol matters before adopting a numerical result as a local prediction.
- Human-team practice sources do not yield a universal “best postmortem template”; adapt fields to each domain while keeping evidence and follow-through.
- No lane-specific `QUALITY.md` or actual candidate source entry was inspected, so criteria above are proposals for wave-2 adaptation, not findings that a particular lane fails its own bar.
- None of the sources establishes that agent-written error notes are safe by default. Keep sensitive traces, secrets and personally identifying incident content out of the corpus; store minimal reproductions and permission-appropriate citations.

## Counts and commands

- Source rows: 29 — `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-art-mistakes.md`
- Tier rows: 28 A, 1 B — `grep -E '^\| S[0-9]{3} ' local://kaika-w1-art-mistakes.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`
- Candidate knowledge entries: 6 — `grep -c '^### `' local://kaika-w1-art-mistakes.md`
- Research-derived mistake patterns mined: 6 — `grep -c '^\- \*\*M[0-9] ' local://kaika-w1-art-mistakes.md`
- Confirmed defects found: 0; one scoped enhancement candidate is marked `[INFERENCE]` — `grep -c '^\*\*Confirmed defect:' local://kaika-w1-art-mistakes.md`
