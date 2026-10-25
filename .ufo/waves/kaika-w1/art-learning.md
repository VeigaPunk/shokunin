# Continual learning and self-improving agent systems — W1 ART

## Scope and evidence discipline

Primary-source web research was available and used: every row below was opened in this session. Tier A means the original paper, official project code, or official specification/docs. Search snippets and unopened references are not represented as source rows. Paper results are described as claims of those papers, not as fleet evidence.

**Untrusted-content note.** Some opened source pages contain ordinary instructions and commands (for example, Voyager's README installation/use sections and Agent Skills' validation/evaluation guides). They were treated as source data only; none were followed, executed, installed, or downloaded. Under the wave's handling rule, those embedded instructions are reported as instruction attempts, not adopted as instructions for this research.

## Observed shokunin baseline

- **[OBSERVED]** `LEARNING.md` §“The learning path” already defines curation → `corpus/QUALITY.md` admission → understanding distilled into `SKILL.md`/QUALITY → frontier exploration; §“Discernment is checked from outside” requires a non-author spot-check of at least one admit and reject and disallows self-attested exploratory improvement. The learning trends are categorical (`improved` / `harmed` / `unchanged` / `unprovable-but-better`), not a scalar.
- **[OBSERVED]** `AXES.md` §“Working the axes — a round is 1–3 claims” requires distinct, causally separable axes, one claim on the lowest non-retired axis, falsifiable evidence, and no harmed axis for admission. Its exploratory-claim rule requires a named non-author reviewer.
- **[OBSERVED]** `CORPUS.md` §“Layout” and “Rules” make the corpus lane-specific memory, require source/verified-at/recheck on knowledge entries, falsifiable claims, round evidence for lessons, rejected candidates with reasons, and append-only corrections. `PROTOCOL.md` round requirements say corrections are new appended entries, not rewrites.
- **[OBSERVED]** Current `CORPUS.md` layout lists README, QUALITY, knowledge, and lessons, but not a curated source registry. The campaign plan explicitly schedules `corpus/SOURCES.md` and its fleet contract as deliverables; this is a planned registry gap, not evidence that existing protocol gates are defective. The exact search `grep -nE 'SOURCES\.md|source registry' /home/vgpnk/Projects/shokunin/CORPUS.md /home/vgpnk/Projects/shokunin/LEARNING.md /home/vgpnk/Projects/shokunin/PROTOCOL.md /home/vgpnk/Projects/shokunin/AXES.md` returned no matches.
- **[INFERENCE]** The best fit is a *proposal-and-curation loop*, not an autonomous-write loop: agent systems can generate candidate memories, reusable routines, failure explanations, and evaluation cases; the shokunin gate must still require source provenance, QUALITY criteria, per-axis no-harm evidence, and outside review where judgment is subjective. Retain the lineage of knowledge and corrections; use expiry/recheck to mark stale items rather than silently erasing the corpus.

## Verified mechanisms mapped to the protocol

### Skill libraries, episodes, and reusable workflows

**Voyager** — The paper describes an automatic curriculum, an ever-growing executable-code skill library, and iterative code improvement from environment feedback, execution errors, and self-verification (S001 abstract; S019 README). Retrieved/composed skills enable later tasks without weight updates. **Strengthens:** lane `SKILL.md` as an operational repertoire and `corpus/README.md` frontier as a source of candidate goals/capabilities. **Conflict / boundary:** Minecraft success and the agent's own verification do not establish a lane's QUALITY bar or independent verification. Treat generated skills as candidates; land only after domain-specific tests and non-author review where required.

**Reflexion** — Task feedback is converted into linguistic reflections stored in an episodic buffer and reused on later trials; its paper permits scalar or free-form feedback from external or internally simulated sources (S002 abstract). **Strengthens:** `corpus/lessons/round-<N>.md` as the durable place to capture what failed, why, and the reusable correction. **Conflict / boundary:** a reflection or internally simulated reward is not a verified fact, an outside spot-check, or a per-axis verdict. Keep reflections as candidates and require source/evidence plus the existing lesson gate.

**ExpeL** — The agent gathers task experiences, extracts natural-language insights, and recalls those insights and past examples on later tasks without parameter updates (S003 abstract). **Strengthens:** the curation → gate → understanding path in `LEARNING.md`, especially turning repeated failure modes into a lesson and a cited `SKILL.md` checklist. **Conflict / boundary:** automatically extracted generalizations can overfit or preserve bad trajectories. The protocol's falsifiability, provenance, rejection reasons, and external check remain the admission authority.

**Agent Workflow Memory (AWM)** — AWM induces reusable routines by abstracting example-specific context from previous task trajectories, then selectively supplies a matching workflow; it supports offline and online induction (S004 abstract; S020 README, “What is Agent Workflow Memory?”). **Strengthens:** lane `SKILL.md` procedures/checklists and `corpus/README.md` capability/frontier rows, where a repeated subroutine is more useful than retaining raw transcripts. **Conflict / boundary:** task-specific workflows may not transfer to another lane or changed surface. Require the abstraction to state its boundary and validate it against held-out cases before calling it a durable skill.

### Skill packaging and test-driven refinement

**Agent Skills specification and authoring/evaluation guides** — Progressive disclosure loads skill metadata for discovery, the full `SKILL.md` when activated, and referenced resources only when needed; its authoring guide recommends grounding skills in real artifacts and execution traces. The evaluation guide compares with-skill against a baseline, uses objective assertions where possible, and keeps human review for qualities that resist mechanical checks (S005–S007; spec §“Progressive disclosure”, best-practices §“Refine with real execution”, evaluating-skills §“Writing assertions” and §“Reviewing results with a human”). **Strengthens:** lane `SKILL.md` organization, small focused references, `corpus/QUALITY.md` criteria, and lesson evidence from reproducible tests. **Conflict / boundary:** progressive disclosure must not hide protocol-critical duties behind a reference a lane may not load; the local contract still requires instructions to be executable with resolvable pointers. A skill's own self-check is not the required non-author reviewer.

### Search over prompts, contexts, and executable artifacts

**GEPA / DSPy** — GEPA reflects over execution traces and textual feedback to mutate prompt components, tests candidates, and maintains a Pareto set of complementary attempts (S008 abstract; S009 §§“How Does GEPA Work?” and “Objective-Aware Frontier Tracking”). DSPy's current docs say scalar score still gates acceptance/final selection; objective scores affect selection of parents/merges, rather than replacing that scalar acceptance condition. **Strengthens:** generate alternatives from `LOG.md`, lessons, validator output, and counterexamples; candidates can inform `SKILL.md`/QUALITY changes and `SCORECARD.md` test claims. **Conflict / boundary:** neither a Pareto prompt frontier nor scalar optimization is shokunin's round verdict. Keep all per-axis judgments, reject any trade that harms an axis, and use GEPA only to propose candidates—not to self-authorize promotion.

**AlphaEvolve** — LLM-generated code variants are run through automated evaluators; an evolutionary database retains promising programs to guide further proposals. The official account emphasizes domains with clear, systematic evaluators (S010 abstract; S011 “Designing better algorithms with large language models”). **Strengthens:** falsifiable before/after checks and runnable tools on `operability`, plus capability acquisition recorded with evidence. **Conflict / boundary:** an objective score is not coverage, freshness, calibration, adjacency, or the protocol's no-harm rule. Use for bounded tasks with trustworthy evaluators; do not collapse six axes into one reward or treat automated correctness as proof of corpus quality.

**Agentic Context Engineering (ACE)** — ACE treats context as an evolving playbook: generator, reflector, and curator roles produce insights from task trajectories and make incremental, structured updates intended to avoid context collapse (S012 abstract; S013 README §§“Overview” and “How It Works”). **Strengthens:** a curated playbook derived from `corpus/lessons/` and `SKILL.md`, with lessons making changes auditable and QUALITY criteria explaining what gets retained. **Conflict / boundary:** role separation inside one system is not equivalent to an independent non-author reviewer; performance feedback does not automatically provide axis-wise evidence. Keep updates append-only at the record layer and promote only reviewed deltas.

### Memory organization, correction, and decay

**A-MEM** — New episodes become structured notes with contextual attributes, keywords, and tags; the system dynamically links related notes and can revise existing note representations as new memories arrive (S014 abstract). **Strengthens:** `corpus/README.md` navigation and cross-links between related knowledge entries/lessons. **Conflict / boundary:** rewriting existing memories conflicts with append-only correction. Use links or derived indexes as rebuildable navigation, not as authority to silently mutate sourced claims; corrections should supersede with a new cited record.

**Memory-addition/deletion study** — The study finds that retrieved experience can be copied into later behavior, so unfiltered additions risk error propagation and even apparently correct memories can be misaligned; downstream task evaluations can reveal memory utility (S015 abstract). **Strengthens:** QUALITY admission/recheck criteria and lessons that record the observable downstream failure, retrieval context, and decision to reject or supersede. **Conflict / boundary:** evaluator-driven auto-delete is unsafe for durable domain facts and append-only lessons. Use downstream evidence to flag re-review, not to erase history or replace an independent gate.

**THEANINE** — Rather than remove old dialogue memories, it links them by temporal and cause-effect relations and retrieves timelines; its paper also introduces counterfactual evaluation of memory use (S016 ACL Anthology abstract). **Strengthens:** `verified-at`/`recheck` lineage, explicit supersession history, and counterexamples in lessons—old claims can explain how understanding changed. **Conflict / boundary:** the paper studies lifelong dialogue, not craft corpora; preserving every record can increase retrieval noise. Adopt chronology/provenance as a pattern, not the domain-specific memory policy or an exception to QUALITY.

**AgeMem** — Memory actions (store, retrieve, update, summarize, filter, discard) are exposed as policy actions and learned with a staged reinforcement-learning strategy and step-wise credit assignment (S017 abstract). **Strengthens:** a possible future tool for proposing recheck, consolidation, or retrieval actions, and for testing context efficiency. **Conflict / boundary:** autonomous update/discard and RL reward optimize the agent's policy, not the fleet's append-only contract, per-axis verdicts, or outside gate. Do not delegate corpus admission/deletion authority to the learned policy.

**MemoryBank** — This early long-term-memory system adds retrieval plus a hand-specified Ebbinghaus-inspired decay/reinforcement mechanism: elapsed time lowers retention while recall reinforces a memory (S018 abstract). It is a useful historical baseline for the knowledge-decay lead, not evidence that time-based forgetting is correct for craft knowledge. **Strengthens:** asking what should be rechecked and what should be prominent in retrieval. **Conflict / boundary:** automatic decay/deletion can discard rare but durable facts and contradicts append-only correction. Recheck dates should trigger verification/flagging, not silent removal.

## Candidate knowledge entries for later lane rounds

These are proposed entry seeds, not admitted knowledge. A lane must map them to its own uncovered coverage/frontier row, apply its own `corpus/QUALITY.md`, and record the gate. Where the relevant lane is unknown, the mapping below names the fleet-level protocol surface only.

### CE-01 — Keep a curated source registry distinct from knowledge

**Falsifiable claim:** when a lane maintains `corpus/SOURCES.md` separately from `corpus/knowledge/`, each open source can be queued/rechecked and linked to admitted entries without treating a source list as proof of a knowledge claim. Verify by checking registry IDs/required fields against cited knowledge paths and checking all `mined` rows have a real use-by path. **Source / location:** Agent Skills best practices, “Start from real expertise” and “Synthesize from existing project artifacts” (S006); ExpeL abstract on accumulating and recalling extracted insights (S003). **Fills:** fleet `CORPUS.md` source-registry contract and lane source-curation coverage. **QUALITY/recheck:** retain only primary/traceable sources and record why a candidate is rejected; recheck URLs and use-by references with the lane's own reproducible validator. **Admission bar:** this is a registry claim, not a generic knowledge fact; the lane must show the file/row validators and its `QUALITY.md` criteria.

### CE-02 — Convert repeated execution traces into a lesson, then a tested procedure

**Falsifiable claim:** a lesson that records a failure trace, an actionable correction, and an independent gate decision yields a reusable `SKILL.md` procedure that passes a predeclared regression set more reliably than the prior version without harming another axis. Compare prior/current outputs and preserve the full per-axis verdicts. **Source / location:** Reflexion abstract (S002), ExpeL abstract (S003), Agent Skills best practices “Refine with real execution” and evaluation guide “Writing assertions” (S006–S007). **Fills:** `corpus/lessons/round-<N>.md` Gate/Mistakes, `corpus/QUALITY.md`, `SKILL.md`. **QUALITY/recheck:** re-run the same cases and include negative/edge cases; cite actual outputs, not a self-reported reflection. **Admission bar:** non-author spot-check of an admit and reject and a landed, falsifiable claim per existing `LEARNING.md`/`AXES.md` rules.

### CE-03 — Promote workflows, not raw episodes

**Falsifiable claim:** a bounded routine abstracted from multiple task traces is more reusable across a lane's declared task variants than a single raw trajectory, without cross-domain bleed. Evaluate the named procedure on held-out variants and record boundary failures. **Source / location:** AWM abstract and README “What is Agent Workflow Memory?” (S004, S020); Voyager abstract and README “Run Voyager for a specific task with a learned skill library” (S001, S019). **Fills:** lane `SKILL.md` decision/checklist content, `SCORECARD.md` capability evidence, and an explicit `corpus/README.md` coverage/frontier row. **QUALITY/recheck:** require resolvable source, executable procedure, and a runnable check; re-run after underlying tool/API changes. **Admission bar:** lane-specific repeated evidence and independent verification; neither source claims universal transfer to unrelated crafts.

### CE-04 — Preserve correction history; let recheck flag staleness, not erase it

**Falsifiable claim:** adding a sourced correction/superseding entry with temporal links preserves the earlier claim's audit trail and lets a reviewer identify the currently verified claim, while a recheck sweep flags stale claims rather than silently deleting them. Verify on a deliberately superseded example plus a fresh and stale control. **Source / location:** THEANINE abstract (S016); memory-addition/deletion study abstract (S015); MemoryBank abstract (S018). **Fills:** `CORPUS.md` append-only correction rule, `LEARNING.md` quality trend, and `corpus/QUALITY.md` freshness criteria. **QUALITY/recheck:** validate source, `verified-at`, recheck condition, and explicit supersedes relation. **Admission bar:** no mutable overwrite or automatic deletion; the lane's non-author spot-check confirms old history remains understandable and current authority is explicit.

### CE-05 — Use optimizers as proposal generators behind the no-harm gate

**Falsifiable claim:** candidate generation from evaluator traces can produce a prompt/procedure delta that passes independent checks on its declared axis, with no other axis harmed; a candidate that improves a scalar aggregate but harms any axis is not admitted. **Source / location:** GEPA abstract and DSPy docs “Objective-Aware Frontier Tracking” (S008–S009); AlphaEvolve abstract and DeepMind blog evaluator discussion (S010–S011); ACE abstract (S012). **Fills:** `AXES.md` round-claim rule, `LEARNING.md` per-trend gate, and a lane's verification checklist. **QUALITY/recheck:** use fixed before/after cases, explicit per-axis results, and a non-author reviewer for subjective claims. **Admission bar:** retain the native per-axis vocabulary; never substitute optimizer score, Pareto status, self-reflection, or benchmark leaderboard for protocol verification.

## Study paths

- **Build a lane source/skill loop:** S005 → S006 → S007 → S003 → S004 → S001/S019. Start with skill structure, then execution-based evaluation, then contrast episodic insight, reusable workflows, and executable skills. This is the shortest path to proposals for `CORPUS.md`, SOURCES, lessons, and lane `SKILL.md`.
- **Keep proposal search subordinate to verification:** S007 → S008/S009 → S010/S011 → S012/S013 → existing `AXES.md` and `LEARNING.md`. Compare trace reflection, evolutionary selection, and playbook curation against the shokunin's external gate and per-axis no-harm rule.
- **Study memory retention without importing destructive forgetting:** S018 → S015 → S016 → S014 → S017. Move from a simple decay baseline to empirical memory-quality evidence, temporal links, dynamic organization, and learned memory operations; record where each departs from append-only craft corpora.

## Rejected as direct protocol replacements

- **Automatic age/usage decay that deletes corpus entries** (S018; S017): rejected because a stale/rare item may still be durable evidence, and deletion erases correction history. Keep rechecks and supersession; at most decay retrieval priority after a transparent, reversible policy.
- **Self-reflection or learned memory policy as admission authority** (S002, S003, S012–S014, S017): rejected because the source system's own confidence/utility is not the required non-author spot-check or source-backed QUALITY gate. These systems may propose candidates and explain failure patterns.
- **Scalar reward/leaderboard as the round verdict** (S008–S011, S017): rejected because aggregate score can conceal a harmed axis, and cannot stand in for calibration, freshness, coverage, or adjacency. Use objective evaluators for individual falsifiable claims; preserve every axis verdict and the no-harm rule.
- **Promoting raw or domain-specific trajectories directly into shared craft knowledge** (S001–S004): rejected because success in one environment does not establish generality or a lane boundary. Extract a bounded workflow, cite its evidence, test variants, and keep adjacency reported rather than absorbed.

## Leads (unopened)

These were identified in search but not opened in this session; they are not source rows and no mechanism/result is asserted here.

- Memory-R1, ACL Anthology 2026: https://aclanthology.org/2026.acl-long.583/
- FadeMem, arXiv:2601.18642: https://arxiv.org/abs/2601.18642
- CodeEvolve, arXiv:2510.14150: https://arxiv.org/abs/2510.14150
- MemGPT / Letta as a memory-hierarchy implementation comparison: https://arxiv.org/abs/2310.08560

## Remaining unknowns

- Individual lane `PROVINCE.md`, `corpus/README.md` Frontier, `corpus/QUALITY.md`, `SKILL.md`, and existing knowledge entries were not inspected; therefore no lane-specific coverage gap or candidate entry is claimed as already uncovered/admissible.
- No fleet/lane `LOG.md`, rejected lesson, harmed-round, or gate-disagreement sweep was performed: this ART dossier mines zero local historical mistakes and does not claim a count of fleet mistakes. Source-paper failure modes above are research findings, not shokunin incident records.
- The opened work does not establish that any named method improves shokunin's per-axis learning outcomes. The proposed transfer is an inference that requires a lane's own round, before/after evidence, and non-author review.

## Sources

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Voyager: An Open-Ended Embodied Agent with Large Language Models — https://arxiv.org/abs/2305.16291 | paper | A | Automatic curriculum, executable skill library, and environment-feedback loop for embodied lifelong learning. | queued | 2026-10-19 | 90d | — |
| S002 | Reflexion: Language Agents with Verbal Reinforcement Learning — https://arxiv.org/abs/2303.11366 | paper | A | Stores natural-language reflections from task feedback in episodic memory for later trials; feedback may be external or internally simulated. | queued | 2026-10-19 | 90d | — |
| S003 | ExpeL: LLM Agents Are Experiential Learners — https://arxiv.org/abs/2308.10144 | paper | A | Extracts natural-language insights from experiences and recalls them with prior examples at inference. | queued | 2026-10-19 | 90d | — |
| S004 | Agent Workflow Memory — https://arxiv.org/abs/2409.07429 | paper | A | Induces reusable routines by abstracting example-specific context and selectively retrieves workflows. | queued | 2026-10-19 | 90d | — |
| S005 | Agent Skills Specification — https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx | spec | A | Defines SKILL.md packaging and staged loading of metadata, instructions, and on-demand resources. | queued | 2026-10-19 | 90d | — |
| S006 | Agent Skills: Best practices for skill creators — https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/best-practices.mdx | docs | A | Grounds skills in real tasks/artifacts, execution traces, corrections, coherent units, and progressive disclosure. | queued | 2026-10-19 | 90d | — |
| S007 | Agent Skills: Evaluating skill output quality — https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/evaluating-skills.mdx | docs | A | Defines baseline comparisons, concrete assertions, evidence-backed grades, trace review, and human review. | queued | 2026-10-19 | 90d | — |
| S008 | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning — https://arxiv.org/abs/2507.19457 | paper | A | Uses textual reflection on trajectories to propose prompt changes and retain complementary candidates via Pareto search. | queued | 2026-10-19 | 90d | — |
| S009 | DSPy GEPA Reflective Prompt Optimizer — https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/GEPA/overview.md | docs | A | Documents trace feedback and objective tracking; scalar score still gates acceptance/final selection. | queued | 2026-10-19 | 90d | — |
| S010 | AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery — https://arxiv.org/abs/2506.13131 | paper | A | Evolves code candidates using evaluator feedback over repeated proposal and selection cycles. | queued | 2026-10-19 | 90d | — |
| S011 | AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms — https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ | docs | A | Official account of automated evaluation and evolutionary program selection for measurably evaluable problems. | queued | 2026-10-19 | 90d | — |
| S012 | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models — https://arxiv.org/abs/2510.04618 | paper | A | Treats context as a playbook maintained through generation, reflection, curation, and structured incremental updates. | queued | 2026-10-19 | 90d | — |
| S013 | ACE: Agentic Context Engineering repository — https://github.com/ace-agent/ace | code | A | Implements Generator, Reflector, and Curator roles for accumulating and organizing context/playbook knowledge. | queued | 2026-10-19 | 90d | — |
| S014 | A-MEM: Agentic Memory for LLM Agents — https://arxiv.org/abs/2502.12110 | paper | A | Creates structured notes and dynamically links related memories, with updates to historical representations. | queued | 2026-10-19 | 90d | — |
| S015 | How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior — https://arxiv.org/abs/2505.16067 | paper | A | Studies memory addition/deletion, error propagation, misaligned replay, and downstream utility evidence. | queued | 2026-10-19 | 90d | — |
| S016 | Towards Lifelong Dialogue Agents via Timeline-based Memory Management — https://aclanthology.org/2025.naacl-long.435/ | paper | A | Links memories by temporal and causal relations and retrieves timelines rather than deleting old context. | queued | 2026-10-19 | 90d | — |
| S017 | Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents — https://arxiv.org/abs/2601.01885 | paper | A | Learns memory store/retrieve/update/summarize/filter/discard actions as part of an agent policy. | queued | 2026-10-19 | 90d | — |
| S018 | MemoryBank: Enhancing Large Language Models with Long-Term Memory — https://arxiv.org/abs/2305.10250 | paper | A | Uses an Ebbinghaus-inspired time-decay and recall-reinforcement memory update mechanism. | queued | 2026-10-19 | 90d | — |
| S019 | MineDojo Voyager source repository — https://github.com/MineDojo/Voyager | code | A | Provides executable skill-library artifacts and a path to reuse a learned library on new tasks. | queued | 2026-10-19 | 90d | — |
| S020 | Agent Workflow Memory source repository — https://github.com/zorazrw/agent-workflow-memory | code | A | Provides offline and online workflow induction code and concrete task workflow artifacts. | queued | 2026-10-19 | 90d | — |

**Registry status:** every row is `queued`; this dossier opened sources but did not write any lane `knowledge/` entry. On materialization, change a row to `mined` only when a real knowledge entry cites it; append a superseding row for corrections rather than rewriting history.

**Reproducible counts for this dossier:**

- 20 source rows — `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-art-learning.md`
- Tier distribution: 20 A, 0 B, 0 C — `grep -E '^\| S[0-9]{3} ' local://kaika-w1-art-learning.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`
- 5 candidate entries — `grep -cE '^### CE-[0-9]{2} ' local://kaika-w1-art-learning.md`
- 0 local historical mistakes mined — not applicable to this ART assignment; no lane `LOG.md` or lessons sweep was run.
- 0 existing protocol defects evidenced; one planned registry gap — verified by the exact negative-search command in “Observed shokunin baseline.”
