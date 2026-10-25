# kaika W1 — ART dossier — lane `kotoba` (prompt & skill craft)

- Author: `W1ArtKotoba` (scout, read-only). Date: 2026-10-19.
- Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. I read only what the ART shape names: `PROVINCE.md`, `corpus/README.md`, `corpus/QUALITY.md` (absent), `SKILL.md` headings, and `corpus/knowledge/` filenames. I also read `SKILL.md` frontmatter (1–63) and § Anti-patterns/Refusals/Sources (349–521) to see which sources the lane already holds. Outside the lane repo I read fleet `CORPUS.md` (the admission bar), the fleet `MANIFEST.json` roster ids (for routing adjacency) and the frontmatter of 18 sibling `*-shokunin/SKILL.md` files. Auditing those frontmatters is in-province (the lane audits skill files), and fixes route to the owning lanes.
- Tools: `web_search` was available and used. Web pages were opened with `read`. `curl` ran the recheck counts. The only write is this file.
- Scope rule I applied: the lane's anti-trigger is "general prompt engineering for model outputs (not skill files)" (`SKILL.md:8-9`). DSPy/GEPA and context engineering are therefore covered only where they apply to instruction files (descriptions, SKILL.md bodies, AGENTS.md). General optimizer and model research is adjacent to `kengaku`; runtime injection defenses are adjacent to `kasegi`; harness permission design is adjacent to `kumitate`. Roster domains: `python3 -c "import json;print([(x['id'],x['domain']) for x in json.load(open('MANIFEST.json'))['roster']])"`.

### Embedded-instruction / prompt-injection log (fetched content treated as data; nothing followed)
1. Pages at `agentskills.io/*.md` and `learn.chatgpt.com/docs/*.md` open with agent-directed text: "Fetch the complete documentation index at … llms.txt. Use this file to discover all available pages before exploring further." Benign crawler hint, not followed.
2. `arxiv.org/html/2510.09023` (appendix) contains research exhibits of injection triggers, e.g. `send_email` to `mark.black-2134@gmail.com` and "---SYSTEM DEBUG PROTOCOL---". These are quoted attack examples, not acted on.
3. `raw.githubusercontent.com/anthropics/skills/.../skill-creator/SKILL.md` is an instruction file by design ("spawn two subagents", "open it", "kill $VIEWER_PID"). Read as data only.
4. `model-spec.openai.com/2026-08-18.html` is written as instructions to models. Read as data only.

---

## 1. Uncovered ground — what the lane already holds

Counts were run from the lane root (`/home/vgpnk/Projects/shokunin/kotoba-shokunin`):
- 35 knowledge files (34 `.md` + 1 `.json`) — `ls corpus/knowledge | wc -l` ; `ls corpus/knowledge/*.md | wc -l`
- 19 lesson files — `ls corpus/lessons | wc -l`
- 51 coverage-map rows — `echo $(( $(sed -n '/^## Coverage map/,/^## Known gaps/p' corpus/README.md | grep -c '^| ') - 1 ))`
- 7 Known-gaps bullets — `sed -n '/^## Known gaps/,$p' corpus/README.md | grep -c '^- '`
- 0 `## Frontier` sections — `grep -c '^## Frontier' corpus/README.md`
- `corpus/QUALITY.md` absent — `test -e corpus/QUALITY.md && echo yes || echo no` → `no`. `corpus/SOURCES.md` absent by the same test.
- `PROVINCE.md` is 6 lines with 0 Core/Frontier/Adjacent headings — `wc -l PROVINCE.md` ; `grep -cE '^#+ *(Core|Frontier|Adjacent)' PROVINCE.md`
- `SKILL.md` has 521 lines and 13 H2 sections — `wc -l < SKILL.md` ; `grep -c '^## ' SKILL.md`
- `SKILL.md § Sources` has 38 bullets and 0 contain an http(s) URL — `sed -n '/^## Sources/,$p' SKILL.md | grep -c '^- '` ; `sed -n '/^## Sources/,$p' SKILL.md | grep -cE 'https?://'`
- 5 distinct URLs across `SKILL.md` + `corpus/**/*.md`. None is prompt or skill craft art: 4 are sibling property hosts quoted in a description rewrite, and 1 is `github.com/sst/opencode`. Command: `grep -rhoE 'https?://[^ )>`|"]+' SKILL.md corpus --include='*.md' | sort -u`
- Negative claim with its sweep: 0 files mention any of these terms: agentskills, anthropic.com, progressive disclosure, context engineering, context rot, DSPy, GEPA, MIPRO, TextGrad, instruction hierarchy, prompt injection, spotlight, CaMeL, OWASP, model spec, skill-creator. Command: `for k in agentskills anthropic.com 'progressive disclosure' 'context engineering' 'context rot' DSPy GEPA MIPRO TextGrad 'instruction hierarchy' 'prompt injection' spotlight CaMeL OWASP 'model spec' skill-creator; do printf '%s %s\n' "$k" "$(grep -rilF -e "$k" SKILL.md corpus | wc -l)"; done` → every line `0`.

What is held: the corpus is deep self-measurement of two host harnesses.
- **omp/opencode router render and offer gates.** Covers the 99-char cliff, cache keys and `<available_skills>` vs `<skills>`. Files: `knowledge/render-mechanism-round7.md`, `harness-router-models-round9.md`, `opencode-offer-trace-round8.md`, `skill-activation-telemetry.md`, `trigger-miss-proxy-round6.md`.
- **Instruction-surface census (7 classes).** Files: `instruction-surface-census-round13.md`, `instruction-surface-remeasure-round13.md`, `harness-system-prompt.md`, `claude-md-surface.md`, `opencode-extraction-round14.md`.
- **Four checklists** (trigger, agent-definition, dispatch-prompt, always-on). Files: `alwayson-checklist-round7.md`, `dispatch-prompt-audit-round7.md`, `agent-def-audit-round6.md`, `fleet-skill-audit-round5.md`.
- **Executable verifiers and second witnesses.** Files: `harness-verifier-round10.md`, `corpus-integrity-round11.md`, `independent-verification-round12.md`, `harness-independent-round37.md`, `checklist-execution-round15/16/17.md`, `substrate-pin-guard-round23.md`.
- **Sibling description rewrites and citation routing.** Files: `sibling-description-rewrites-round8.md`, `sibling-citation-routing-round16/21.md`.
- **Craft rules.** `frontmatter-trigger-surface.md` and `anatomy-and-compression.md` hold 16 host files surveyed 2026-09-28 and a "~600-line module bound" (README.md:10).

What is not held: any external current art (sweep above), plus several structural pieces.
- Cross-client standard: the agentskills.io spec and client guide.
- Vendor authoring rules: 500-line body, third-person description, no XML tags, one-level references.
- Vendor trigger-eval protocols.
- Skill and context-file efficacy evidence.
- Context engineering.
- Prompt and instruction optimizers.
- Instruction hierarchy (authority of surfaces).
- Skill-borne injection.
- Structural pieces: no `QUALITY.md`, no `## Frontier`, no Core/Frontier/Adjacent split in `PROVINCE.md`, no `SOURCES.md`.

### Known gaps (corpus/README.md) → current art that addresses them
- **README.md:63-67 — 33/41 checklist boxes are lane-attested prose.** S004's pre-share checklist and S001/S003's machine-checkable rules can be executed: name regex, name==dir, description ≤1024 chars, no XML tags, file ≤500 lines, references one level deep. → §2 item 12, §8.
- **README.md:68-72 — command-check extraction set.** No external art found. Stays lane-internal.
- **README.md:73-75 — "Implicit-intent fidelity is still unmeasured … Needs an intent-labeling pass".** Two vendor protocols exist: S006/S007 (Anthropic) and S009 (OpenAI). → E1.
- **README.md:76-84 — MCP/plugin surface.** S008 shows plugins bundling skills with MCP connectors. S002 shows the catalog can live in a tool description. → Leads.
- **README.md:85-90 — sibling arbitration (0/5 descriptions carry an arbitration clause).** S006 asks for negatives where "this skill competes with another but should win". S008's template asks the description to say "when this skill should and should not trigger". → E1.
- **README.md:91-95 — consume-side activation (godspeed 205/399 = 51.4%).** S006 documents under-triggering and a consult-only-when-needed policy. S015 measured 56% non-invocation. → E2.
- **README.md:96-100 — render cliff; whether cached one-liners route better is unmeasured.** S008 shortens descriptions under a catalog budget. S012 shows where metadata-only routing breaks at scale. → E2.

---

## 2. Current art 2025–2026 the corpus does not hold

1. **Agent Skills is an open, cross-client standard.** The spec (S001) is normative. The client-implementation guide (S002) defines a 3-tier load, `<available_skills>` catalog XML and model-driven activation ("rather than implementing harness-side trigger matching or keyword detection", S002 § Step 4). It also defines lenient validation, a name-collision rule, trust gating and compaction protection. S005 (Anthropic) notes the open standard was "published … December 18, 2025". The same `<available_skills>` shape the lane observed in opencode is the reference catalog format (S003 `to-prompt`).
2. **Vendor authoring rules that differ from the lane's own.** The body should be under 500 lines (S001, S004), while the lane uses a ~600-line bound (README.md:10). Descriptions must be third-person, ≤1024 chars and contain no XML tags (S004 § Skill structure). Names are gerund-preferred, with reserved words "anthropic"/"claude" banned. References stay one level deep, and reference files over 100 lines get a TOC (S004). S004 also prescribes evaluation-first development: three scenarios plus a no-skill baseline.
3. **Trigger evaluation as a protocol, from two vendors.** Anthropic's executable loop: 20 labelled queries with near-miss negatives, 3 runs per query, a 60/40 held-out split, and selection by held-out score (S006); it improved triggering on 5 of 6 public skills (S007). OpenAI's CSV `id,should_trigger,prompt` covers explicit, implicit, contextual and negative-control rows, checked against `codex exec --json` traces (S009).
4. **A second router contract (Codex).** Implicit invocation by description. The initial list is budgeted at 2% of context or 8,000 chars, descriptions are shortened first, and skills may be omitted with a warning. Guidance: "Front-load the key use case and trigger words". An `allow_implicit_invocation` policy exists. `.agents/skills` is scanned from CWD up to the repo root (S008).
5. **Under-triggering is the documented default failure.** Anthropic says so in S006. A controlled vendor eval found the skill never invoked in 56% of cases, with zero lift at default (S015).
6. **Skill efficacy is measurable, and smaller is better.**
   - SkillsBench: curated skills add +16.2pp (v1) / +16.6pp (latest); focused skills with 2–3 modules beat comprehensive docs (S011).
   - ACES: paired Skill Lift; static scans and LLM-judge correlate at ρ = 0.14; process metrics such as discovery and routing are invisible to document scans (S013).
   - SkillRouter: at ~80K skills, metadata-only routing loses 37–44 points (S012).
7. **Always-on context files (AGENTS.md) have measured costs.**
   - No general gain and +20% inference cost; overviews are unhelpful (S016).
   - Tuned guidance beats static guidance (S017).
   - A compressed docs index beat on-demand skills on one suite (S015).
   - Precedence convention: the nearest file wins and explicit user prompts override (S010).
8. **Context engineering** (S018, S019): context is a finite attention budget, so use the smallest set of high-signal tokens. Pitch system prompts at the "right altitude". Prefer canonical examples over edge-case lists. Use just-in-time retrieval, compaction and notes. Context rot appears across 18 models.
9. **Self-improving contexts and skills.**
   - ACE: brevity bias and context collapse; delta-updated playbooks (S020).
   - GEPA: reflective, Pareto-frontier optimization (S021), with a DSPy textual-feedback metric (S022).
   - Self-evolving skills: sparse, validation-filtered search that needs failure feedback (S014).
   - Self-generated skills: no average lift in SkillsBench v1 (S011).
10. **Instruction hierarchy as an authority model.**
    - IH-Challenge (2026): System > developer > user > tool (S023).
    - Model Spec 2026-08-18: six levels; tool outputs and attachments carry no authority by default; implicit delegation to AGENTS/README instructions (S024).
    - ManyIH: up to 12 tiers at ~40% accuracy (S025).
11. **Skills as an injection vector.**
    - Skills are "all instructions", so detection-style defenses are invalid (S026).
    - 26.1% of 31,132 marketplace skills are vulnerable; script-bundling skills are 2.12× likelier (S027).
    - Prompting defenses give no robustness gain under adaptive attack (S028).
    - Rule of Two: at most two of {untrusted input, sensitive access, external action} per session (S029).
12. **Applied finding — fleet `SKILL.md` frontmatter vs current art** (new measurement, read-only):

    ```
    cd /home/vgpnk/Projects/shokunin && ruby -ryaml -e '
    puts "dir | yaml | name==dir | name_ok | desc_chars | desc<=1024 | xml_tag_in_desc | lines | lines<=500"
    rows = Dir.glob("*-shokunin/SKILL.md").sort.map do |p|
      t = File.read(p); d = File.basename(File.dirname(p)); lines = t.count("\n"); m = t.match(/\A---\n(.*?)\n---\n/m)
      begin
        fm = m ? (YAML.safe_load(m[1]) || {}) : {}; ok = m ? "ok" : "NO_FRONTMATTER"
      rescue Psych::SyntaxError => e
        fm = {}; ok = "INVALID(" + e.message[/line \d+ column \d+/].to_s + ")"
      end
      name = fm["name"].to_s; desc = fm["description"].to_s
      r = [d, ok, name == d, !!(name =~ /\A[a-z0-9]+(-[a-z0-9]+)*\z/) && name.size <= 64, desc.size, desc.size <= 1024, !!(desc =~ /<[A-Za-z_\/][^>]*>/), lines, lines <= 500]
      puts r.join(" | "); r
    end
    puts "files #{rows.size} | yaml_invalid #{rows.count{|r| r[1] != "ok"}} | desc>1024 #{rows.count{|r| r[1]=="ok" && !r[5]}} | xml_tag #{rows.count{|r| r[6]}} | >500 lines #{rows.count{|r| !r[8]}} | name!=dir(valid yaml) #{rows.count{|r| r[1]=="ok" && !r[2]}}"'
    ```

    Result on 2026-10-19: `files 18 | yaml_invalid 12 | desc>1024 0 | xml_tag 1 | >500 lines 10 | name!=dir(valid yaml) 2`.
    - **YAML-invalid (12):** game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kumitate, mado, tabi, tameshi, tsukuroi. The cause is a plain-scalar `description:` containing `": "`. Examples: `kake-shokunin/SKILL.md:3` "… Pages deploys. Rank: shonen."; `mado-shokunin/SKILL.md:3` "… compositor craft. Rank: shonen (probation)." This is exactly S002 § "Handling malformed YAML" ("Technically invalid YAML — the colon breaks parsing").
    - **No `name:` field (2):** `lore-shokunin` and `souji-shokunin` frontmatter carry only `description`. S001 marks `name` "Required: Yes".
    - **XML tag in description (1):** `kotoba-shokunin` itself carries `` `<skills>` `` in the description (`sed -n '1,16p' SKILL.md | grep -c '<skills>'` → 1, line 14). S004 says the description "Cannot contain XML tags". That is an Anthropic rule; the agentskills.io spec has no such rule.
    - **Over 500 lines (10):** kagi 663, kasegi 1012, kengaku 640, kotoba 521, kotodama 732, kumitate 782, mado 1580, tabi 1595, tameshi 1476, tsukuroi 1636.
    - **Peer-supplied, not opened by me:** `W1StateKotoba` reports that `verifiers/verify_skill_checklist.py:67-76,472-533` "frontmatter parses" is a lenient structural parse with no XML-tag rule. The lane's own gate cannot see either defect class (see `local://kaika-w1-kotoba-state.md`).
    - **Scope caveat:** the shokunin files are not in an omp discovery root (`SKILL.md:12-15`), so these defects break portability to agentskills-compatible clients, not routing on this host today.

---

## 3. SOURCES.md rows (contract draft; all opened 2026-10-19)

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | Agent Skills — Specification — https://agentskills.io/specification (repo pin agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379) | spec | A | Normative SKILL.md format: name 1–64 lowercase-hyphen chars matching the directory; description 1–1024 chars saying what and when; optional license/compatibility/metadata/allowed-tools; 3-tier disclosure (~100-token metadata, under 5000-token body, resources on demand); main file under 500 lines; references one level deep | watch | 2026-10-19 | on-release | — |
| S002 | Agent Skills — How to add skills support to your agent — https://agentskills.io/client-implementation/adding-skills-support | docs | A | Client contract: catalog of name+description(+location) at ~50–100 tokens per skill; `<available_skills>` XML example; model-driven activation with no harness keyword matching; lenient validation (name/dir mismatch warns and loads, missing description skips); project-over-user collisions with a warning; trust-gate project skills; exempt skill content from compaction | watch | 2026-10-19 | 90d | — |
| S003 | skills-ref — Agent Skills reference library README — https://github.com/agentskills/agentskills/tree/main/skills-ref | tool | A | Reference CLI: `validate` (frontmatter + naming), `read-properties` (JSON), `to-prompt` (emits the `<available_skills>` block "recommended for Anthropic's models"). Marked demonstration-only, so use it as an independent second witness, not as a production gate | watch | 2026-10-19 | on-release | — |
| S004 | Skill authoring best practices — Claude Docs — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | docs | A | Anthropic authoring rules: third-person description stating what and when, ≤1024 chars, no XML tags; no reserved words in name; body under 500 lines; references one level deep with a TOC past 100 lines; build three evals and a no-skill baseline first; Claude A authors while Claude B tests; pre-share checklist | watch | 2026-10-19 | 90d | — |
| S005 | Equipping agents for the real world with Agent Skills — Anthropic Engineering — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | docs | A | Origin of the 3-level progressive-disclosure model (2025-10-16; open-standard note dated 2025-12-18); name+description pre-loaded into the system prompt; start with evaluation; have Claude capture successes and mistakes into the skill; audit less-trusted skills before use | queued | 2026-10-19 | 180d | — |
| S006 | anthropics/skills — skill-creator/SKILL.md @dbd4588 — https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md | code | A | Executable trigger-optimization protocol: 20 queries (8–10 should-trigger, 8–10 near-miss should-not), each run 3x, 60/40 train/held-out, up to 5 iterations, best description chosen by held-out score; documents under-triggering and that Claude consults skills only for tasks it cannot easily do alone | watch | 2026-10-19 | on-commit (main moves) | — |
| S007 | Improving skill-creator: Test, measure, and refine Agent Skills — Claude blog (2026-03-03) — https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills | docs | A | Vendor eval framing: capability-uplift vs encoded-preference skills; regression and model-outgrew-skill signals; parallel clean-context eval agents; blind comparator A/B; description tuning against false positives and negatives (improved triggering on 5 of 6 public skills) | queued | 2026-10-19 | 180d | — |
| S008 | Build skills — ChatGPT/Codex docs — https://learn.chatgpt.com/docs/build-skills (redirected from developers.openai.com/codex/skills) | docs | A | Second router contract: implicit invocation by description; initial list budget of 2% of context or 8000 chars; descriptions shortened first and skills may be omitted with a warning; front-load trigger words; `.agents/skills` scanned from CWD to repo root; same-name skills not merged; `allow_implicit_invocation` policy | watch | 2026-10-19 | on-release | — |
| S009 | Testing Agent Skills Systematically with Evals — OpenAI Developers blog — https://developers.openai.com/blog/eval-skills | docs | A | Skill-eval recipe: outcome, process, style and efficiency goals; a 10–20 prompt CSV with should_trigger covering explicit, implicit, contextual and negative-control rows; deterministic checks over `codex exec --json` JSONL traces, then rubric grading with an output schema | queued | 2026-10-19 | 180d | — |
| S010 | AGENTS.md — open format site — https://agents.md/ | spec | A | Always-on context-file convention (60k+ repos; stewarded by the Agentic AI Foundation under the Linux Foundation): plain Markdown with no required fields; nested files where the closest to the edited file wins; explicit user chat prompts override everything | watch | 2026-10-19 | 90d | — |
| S011 | SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks — arXiv 2602.12670 — https://arxiv.org/abs/2602.12670 | paper | A | Paired with/without-skill evaluation: curated skills add +16.2pp (v1, 7 configs) or +16.6pp (latest, 18 configs); focused 2–3-module skills beat comprehensive docs. v1 says self-generated skills give no average benefit, but that condition is absent from the latest abstract, so cite by version | watch | 2026-10-19 | on-new-version | — |
| S012 | SkillRouter: Skill Routing for LLM Agents at Scale — arXiv 2603.22455 — https://arxiv.org/abs/2603.22455 | paper | A | With ~80K overlapping skills, hiding the body (metadata-only routing) costs 37–44 points of routing accuracy; body-distilled descriptions recover part. Scale-bound evidence for where name+description routing stops working | queued | 2026-10-19 | 180d | — |
| S013 | Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills (ACES) — arXiv 2608.20614 — https://arxiv.org/abs/2608.20614 | paper | A | Skill Lift from paired live trials with and without a skill; structural scans and LLM-judge correlate at Spearman ρ 0.14; composite lift is positive in 72.8% of 947 paired cases; process signals (discovery, routing) are invisible to document scans | queued | 2026-10-19 | 180d | — |
| S014 | Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds — arXiv 2608.02636 — https://arxiv.org/abs/2608.02636 | paper | A | Controlled study of iterative skill revision: only 55 of 388 candidates set a validation best; all 11 selected evolutions used feedback that included failed trajectories; self-evolution is sparse, validation-filtered search, not a steady per-round gain | queued | 2026-10-19 | 180d | — |
| S015 | AGENTS.md outperforms skills in our agent evals — Vercel blog (2026-01-27) — https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | docs | B | Single-vendor Next.js 16 eval: the skill was never invoked in 56% of cases (default skill 53% = baseline 53%); explicit instructions reached 79% but were wording-fragile; a compressed 8KB AGENTS.md docs index reached 100%. Tier B because the suite is unpublished and covers one framework | queued | 2026-10-19 | 365d | — |
| S016 | Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? — arXiv 2602.11988 — https://arxiv.org/abs/2602.11988 | paper | A | Context files (LLM-generated and developer-committed) do not generally raise task success and add over 20% inference cost; their instructions are followed, but repository overviews do not help | queued | 2026-10-19 | 180d | — |
| S017 | Probe-and-Refine Tuning of Repository Guidance for Coding Agents — arXiv 2606.20512 — https://arxiv.org/abs/2606.20512 | paper | A | How guidance is produced is the decisive variable: synthetic bug-fix probes iteratively patch the guidance file; 33.0% vs 28.3% (static KB) vs 25.5% (unguided) on SWE-bench Verified; the gain is coverage (reaching the right file), not per-patch precision | queued | 2026-10-19 | 180d | — |
| S018 | Effective context engineering for AI agents — Anthropic Engineering (2025-09-29) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | docs | A | Context is a finite attention budget, so use the smallest high-signal token set; pitch system prompts at the right altitude (between brittle if-else and vague); curate canonical examples rather than edge-case lists; just-in-time retrieval; compaction, note-taking and sub-agents | queued | 2026-10-19 | 365d | — |
| S019 | Context Rot: How Increasing Input Tokens Impacts LLM Performance — Chroma tech report (2025-07-14) — https://www.trychroma.com/research/context-rot | paper | A | All 18 models degrade as input grows, even on simple tasks; low needle-question similarity and distractors make it worse; no notable variation across 11 needle positions for its NIAH task (contradicting secondary claims of an edge-position advantage); code released | queued | 2026-10-19 | 365d | — |
| S020 | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ACE) — arXiv 2510.04618 — https://arxiv.org/abs/2510.04618 | paper | A | Names two failure modes of iterative rewriting, brevity bias and context collapse; counters them with itemized playbooks updated by incremental deltas (generate, reflect, curate); +10.6% on agents and +8.6% on finance | queued | 2026-10-19 | 180d | — |
| S021 | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning — arXiv 2507.19457 — https://arxiv.org/abs/2507.19457 | paper | A | Reflective optimizer: samples trajectories, diagnoses failures in natural language, proposes and tests prompt edits, keeps a Pareto frontier of complementary candidates; beats GRPO by 6% on average with up to 35x fewer rollouts, and MIPROv2 by over 10% | queued | 2026-10-19 | 180d | — |
| S022 | dspy.GEPA: Reflective Prompt Optimizer — DSPy docs — https://dspy.ai/current/api/optimizers/GEPA/overview/ | docs | A | Operational interface: the metric may return a score plus textual feedback per predictor (pred_name, pred_trace); compile(trainset, valset); detailed_results expose Pareto candidates and per-instance bests; gepa installs only below Python 3.15 | watch | 2026-10-19 | on-release | — |
| S023 | Improving instruction hierarchy in frontier LLMs (IH-Challenge) — OpenAI (2026-03-10) — https://openai.com/index/instruction-hierarchy-challenge/ | docs | A | Operative ordering System > developer > user > tool; training tasks are instruction-following-simple, script-gradable and shortcut-free; IH training improved prompt-injection robustness without collapsing into over-refusal; dataset released | queued | 2026-10-19 | 365d | — |
| S024 | OpenAI Model Spec (2026-08-18) — https://model-spec.openai.com/2026-08-18.html | spec | A | Six authority levels (Root, System, Developer, User, Guideline, No Authority); quoted text, file attachments and tool outputs carry no authority by default; users may implicitly delegate to AGENTS/README instructions; provenance-weighted trust example (AGENTS.md vs stuff.txt) | watch | 2026-10-19 | on-release (dated versions) | — |
| S025 | Many-Tier Instruction Hierarchy in LLM Agents (ManyIH) — arXiv 2604.09443 — https://arxiv.org/abs/2604.09443 | paper | A | Real agents face more privilege tiers than the usual fewer-than-five; ManyIH-Bench has up to 12 conflicting levels over 853 tasks; frontier models reach about 40% accuracy when conflicts scale | queued | 2026-10-19 | 180d | — |
| S026 | Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections — arXiv 2510.26328 — https://arxiv.org/abs/2510.26328 | paper | A | Skill files are an injection channel: every line reads as an instruction, so instruction-detection defenses are invalid by definition; hidden instructions in long skills or scripts exfiltrate data; "Don't ask again" approvals carry over; LLM skill-scanners inherit their own jailbreak surface | queued | 2026-10-19 | 180d | — |
| S027 | Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale — arXiv 2601.10338 — https://arxiv.org/abs/2601.10338 | paper | A | 31,132 marketplace skills scanned: 26.1% carry at least one vulnerability across 14 patterns (prompt injection, exfiltration, privilege escalation, supply chain); 5.2% high-severity; script-bundling skills are 2.12x likelier to be vulnerable | queued | 2026-10-19 | 180d | — |
| S028 | The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections — arXiv 2510.09023 — https://arxiv.org/abs/2510.09023 | paper | A | Defense claims need adaptive attackers: 12 defenses bypassed, most above 90% ASR; prompting defenses (Spotlighting, Prompt Sandwiching) exceed 95% ASR and add no robustness over undefended models; plan-then-execute defenses were skipped because their control flow is data-independent | queued | 2026-10-19 | 365d | — |
| S029 | Agents Rule of Two: A Practical Approach to AI Agent Security — Meta AI (2025-10-31) — https://ai.meta.com/blog/practical-ai-agent-security/ | docs | A | Auditable predicate: within one session an agent should satisfy at most two of [A] untrusted inputs, [B] sensitive data or systems, [C] state change or external communication; needing all three requires human-in-the-loop; a supplement to least privilege, not a substitute | queued | 2026-10-19 | 365d | — |
| S030 | How Do You Build Your First Agent Skill? — Agentman blog (2026-06-09) — https://agentman.ai/blog/build-your-first-agent-skill-skillmd-anatomy | community | C | Rejected: claims a name/folder mismatch means the skill will not load, but the client guide (S002) says warn and load anyway; credits an angle-bracket rule to the agentskills.io spec, which has 0 mentions of it; token-saving figures cite unnamed secondary analyses; vendor marketing | rejected | 2026-10-19 | none | — |

Row and tier counts (run on this file; the same commands apply to `corpus/SOURCES.md`):
- 30 rows — `grep -cE '^\| S[0-9]{3} ' <file>`
- tiers: A 28 · B 1 · C 1 — `grep -E '^\| S[0-9]{3} ' <file> | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`
- status: watch 10 · queued 19 · rejected 1 · mined 0 (no lane knowledge entry cites them yet; wave 2 flips rows to `mined` as entries land) — `grep -E '^\| S[0-9]{3} ' <file> | awk -F'|' '{gsub(/ /,"",$7); print $7}' | sort | uniq -c`

Opened in this session but held back (30-row budget). Each is eligible as a row in a later wave:
- **The Instruction Hierarchy (Wallace et al., arXiv 2404.13208, 2024).** The canonical origin of IH: system prompts and untrusted text were treated at the same priority, so it teaches models to ignore lower-privileged instructions. The operative 2026 form is S023/S024.
- **Agent READMEs (arXiv 2511.12884).** 2,303 context files from 1,925 repos evolve like configuration code. Security (14.8%) and performance (14.5%) instructions are rare.
- **"Do Not Mention This to the User" (arXiv 2602.06547).** 98,380 registry skills; 157 confirmed malicious, with 632 vulnerabilities across 13 techniques. Concealment is embedded in documentation.
- **MIPROv2 (arXiv 2406.11695).** Instruction + demonstration optimization for multi-stage LM programs, up to 13% gains. It is the lineage that GEPA (S021) supersedes for this lane's use.

## Leads (unopened)
- **Skill routing:**
  - SkillRet (arXiv 2605.05726)
  - The Router Within / GAVEL (2609.15982)
  - Skill Is Not Document (2606.03565)
  - Compositional Skill Routing (2606.18051)
  - Representation Affects Retrieval (2608.20389)
  - Skill2Query (2608.16071)
- **Skill quality and evaluation:**
  - SkillEval (2608.06891)
  - SkillJuror (2606.11543)
  - Agent Skill Evaluation and Evolution survey (2606.11435)
  - SkillGenBench (2605.18693)
  - SkillCorpus (2607.15557)
  - NVIDIA SkillEvaluator (ACES implementation)
- **Self-evolution:**
  - Trace2Skill (2603.25158)
  - SkillEvolver (2605.10500)
  - EvoSkills (2604.01687)
  - SkillLearnBench (2604.20087)
  - Constrained exploration-exploitation self-evolution (2607.26643)
  - https://github.com/HKUST-KnowComp/rethinkskill
  - https://github.com/ace-agent/ace
  - https://github.com/gepa-ai/gepa
- **Skill security (adjacent to kasegi; the lane needs only audit-relevant parts):**
  - SkillJect (2602.14211)
  - SkillAttack (2604.04989)
  - SkillSecurer (2609.14079)
  - Detecting Malicious Agent Skills using Attention (2606.23416)
  - Emerging Threats of the Agent Skill Ecosystem (2605.28588)
  - Agent Skill Security survey (2607.13987)
  - Skills Are Not Islands (2607.01136)
  - SkillVetBench (2606.15899)
  - SkillProbe (2603.21019)
  - Context Matters, repo-aware skill security (2603.16572)
  - Towards Secure Agent Skills (2604.02837)
  - Agent Skills for LLMs: Architecture, Acquisition, Security (2602.12430)
  - https://github.com/aisa-group/promptinject-agent-skills
- **Context files:**
  - Do Context Files Help Coding Agents? Two-agent ablation (2607.27250)
  - LOCA-bench (2602.07962)
  - Classifier Context Rot (2605.12366)
- **Instruction hierarchy:**
  - IH-Challenge paper https://arxiv.org/abs/2603.10521 and dataset https://huggingface.co/datasets/openai/ih-challenge
  - Model Spec 2025-12-18 (linked from S023)
  - Anthropic's Claude constitution (principal hierarchy)
- **Injection architecture (kasegi adjacency):**
  - Can CaMeLs Talk? (2610.05640)
  - CaMeLoT (2609.18674)
  - Plan-then-Execute guide (2509.08646)
  - Operationalizing CaMeL (2505.22852)
  - OWASP LLM01:2025 https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **Anthropic engineering posts:** "Demystifying evals for AI agents" (2026-01), "Writing effective tools for agents", "Effective harnesses for long-running agents"; Manus "Context Engineering for AI Agents: Lessons from Building Manus".
- **Vendor code to pin next:**
  - https://github.com/openai/skills (`.system/skill-creator`)
  - `anthropics/skills` `skill-creator/scripts/run_loop.py` + `run_eval.py`
  - https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator
- **Could not open:** https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655 (HTTP 403).

---

## 4. Candidate knowledge entries (6)

The lane has no `corpus/QUALITY.md` (`test -e corpus/QUALITY.md` → absent), so every candidate is held to the fleet bar instead:
- `CORPUS.md:17` — the entry opens with `source:` / `verified-at:` / `recheck:`.
- `CORPUS.md:23` — URL source.
- `CORPUS.md:25` — falsifiable.
- `CORPUS.md:33-37` — counts carry commands.
- `CORPUS.md:38-40` — negative claims carry their sweep.
- `CORPUS.md:41-44` — quotes name their location.
- `SKILL.md:360-361` — "claims need a file, a command output, or a cited source".
- Draft criterion for wave 2's QUALITY.md: every admitted external claim has tier-A support, cites a version (arXiv vN, dated spec, or commit) and carries a pasteable recheck.

All six clear that draft: each has tier-A support, and the one B-tier source (S015) is never sole support. All recheck commands below were run on 2026-10-19 with the stated results.

### E1 — `knowledge/trigger-eval-protocol.md`
- **Claim (falsifiable):** Two vendors that ship description-routed skills specify trigger fidelity the same way: as a labelled should/should-not-trigger prompt set whose negatives are near-misses. Anthropic's executable loop adds the parameters: 20 queries, 3 runs per query, a 60/40 train/held-out split, at most 5 iterations, and the description chosen by held-out score. The claim is false if the pinned files lack these parameters.
- **Sources and quotes:**
  - S006 § "Description Optimization → Step 1": "Create 20 eval queries — a mix of should-trigger and should-not-trigger."
  - S006 § Step 1: "the most valuable ones are the near-misses — queries that share keywords or concepts with the skill but actually need something different"
  - S006 § Step 1: "cases where this skill competes with another but should win."
  - S006 § Step 3: "selected by test score rather than train score to avoid overfitting"
  - S009 § "4. Use a small, targeted prompt set": "Including at least one should_trigger=false case helps catch false positives, where Codex selects the skill too eagerly"
  - S007 § "Getting skills to trigger at the right time": "improved triggering on 5 out of 6 public skills."
- **Fills:**
  - Known gap README.md:73-75: implicit-intent fidelity is unmeasured and needs an intent-labeling pass.
  - Known gap README.md:85-90: arbitration, via negatives that compete with siblings.
  - Coverage row "Trigger-miss proxy (round-6)" (README.md:17), whose literal-trigger proxy only covers prompts that name a skill.
- **Recheck (2026-10-19 results):**
  - `curl -sL https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md | grep -cE '20 eval queries|60% train|3 times|test score rather than train'` → `2` (lines 345 and 400)
  - `curl -sL https://developers.openai.com/blog/eval-skills.md | grep -c 'should_trigger'` → `2`
  - Cadence: on commit to `anthropics/skills` main, and 180d for S009.
- **Admission:** tier-A sole support (S006 code, S009 vendor docs); counts carry commands; quotes are located.
- **Round use:**
  - Countable artifact: one labelled `evals/trigger/<skill>.json` per audited skill, holding 20 queries with ≥8 near-miss negatives. Count with `ls … | wc -l` and `jq '[.[]|select(.should_trigger==false)]|length'`.
  - Measuring trigger rates needs harness runs. That costs money and is lane-internal; route harness hooks to `kumitate`.

### E2 — `knowledge/activation-economics.md`
- **Claim (falsifiable):** Description-routed skills mostly fail by not firing.
  - Anthropic documents under-triggering and a policy of consulting skills only for tasks the model cannot easily do alone.
  - A controlled vendor eval measured 56% non-invocation and zero lift at default.
  - Codex's catalog budget (2% of context or 8,000 chars) shortens descriptions first, so trigger words must sit in the opening clause.
  - The claim is false if the pinned sources stop saying this, or if a lane measurement on this host shows over-triggering dominates.
- **Sources and quotes:**
  - S006 § "Write the SKILL.md": "currently Claude has a tendency to "undertrigger" skills -- to not use them when they'd be useful."
  - S006 § "How skill triggering works": "Claude only consults skills for tasks it can't easily handle on its own"
  - S015 § "Skills weren't being triggered reliably": "In 56% of eval cases, the skill was never invoked."
  - S008 § "How ChatGPT and Codex use skills": "Front-load the key use case and trigger words so a host can still match the skill if descriptions are shortened."
  - S008 intro: "If many skills are installed, Codex shortens skill descriptions first."
- **Fills:**
  - Known gap README.md:91-95 (godspeed offered 387/387, activated 205/399 = 51.4%, a consume-side gap). S006's consult policy supplies a mechanism hypothesis. [INFERENCE] A posture skill like godspeed rarely matches "tasks it can't easily handle", so sub-100% activation would be expected even with a perfect description. Test it with E1's protocol.
  - Known gap README.md:96-100 (render cliff).
  - Coverage rows "Render mechanism & trigger survival" (README.md:20) and "Harness router models (round-9)" (README.md:33). This is cross-harness generalization: omp's `slice(0,99)` cliff and Codex's budget shortening both reward front-loaded triggers, which matches the lane's "keep 55–96" chars finding.
- **Recheck (2026-10-19 results):**
  - `curl -sL https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md | grep -cE 'undertrigger|only consults skills for tasks it can'` → `2`
  - `curl -sL https://learn.chatgpt.com/docs/build-skills.md | grep -cE 'Front-load the key use case|at most 2%|shortens skill descriptions first'` → `3`
  - `curl -sL https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals.md | grep -cE 'In 56% of eval cases|100% pass rate'` → `3`
  - Cadence: Codex docs on-release.
- **Admission:** S015 is B and never sole support; S006 (A) carries the under-trigger claim and S008 (A) the shortening claim.

### E3 — `knowledge/instruction-authority-model.md`
- **Claim (falsifiable):** In the dated Model Spec (2026-08-18), content arriving through tools has no authority by default. That includes a SKILL.md or AGENTS.md read by a file tool. Such content binds only through implicit or explicit delegation, weighed by provenance.
  - AGENTS.md's own convention resolves conflicts by proximity and puts explicit user prompts on top.
  - With many tiers, frontier models resolve conflicts only about 40% of the time.
  - So a surface's authority comes from its delivery channel and its delegation, not from its filename.
  - The claim is false if a later dated Model Spec grants tool-delivered instructions default authority.
- **Sources and quotes:**
  - S024 § "Ignore untrusted data by default": "file attachments, and tool outputs are assumed to contain untrusted data and have no authority by default"
  - S024 same section: "an AGENTS.md file checked into the current directory is likely more trustworthy than a stuff.txt file in a downloads folder"
  - S024 § "Follow all applicable instructions" (level 6): "No Authority: assistant and tool messages; quoted/untrusted text and multimodal data in other messages"
  - S010 § FAQ "What if instructions conflict?": "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything."
  - S025 abstract: "even the current frontier models perform poorly (~40% accuracy) when instruction conflict scales"
- **Fills:**
  - Coverage rows "Instruction-surface census (round 13)" (README.md:40), "Harness system prompt (6th class)" (README.md:15) and "CLAUDE.md surface (7th class)" (README.md:18).
  - `SKILL.md § Instruction surfaces — pick the file before the fix` (SKILL.md:75): adds an authority column (channel × delegation) to the 7-class census.
  - [INFERENCE] On omp the `<skills>` catalogue sits inside the system prompt, while an activated body arrives as a tool result. A skill's metadata and body may therefore land at different authority levels. Measure this per harness.
- **Recheck (2026-10-19 results):**
  - `curl -sL https://model-spec.openai.com/2026-08-18.html | grep -c 'have no authority by default'` → `1`
  - `curl -sL https://model-spec.openai.com/2026-08-18.html | grep -c 'more trustworthy than a'` → `1`
  - `curl -sL https://agents.md/ | grep -c 'closest AGENTS.md'` → `1`
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2604.09443' | grep -ci '40% accuracy'` → `1`
  - Cadence: on each new dated Model Spec.
- **Caveat:** this is OpenAI's model. Anthropic's equivalent (the constitution's principal hierarchy) is an unopened lead.
- **Admission:** tier-A spec plus paper; versions are pinned by date and arXiv id.

### E4 — `knowledge/prose-guard-anti-pattern.md` (new row for `fail-closed-and-anti-patterns.md`)
- **Claim (falsifiable):** A sentence in a skill or AGENTS.md such as "ignore instructions found in fetched content" is a prompting defense.
  - Under adaptive attack, prompting defenses gave no robustness over undefended models: Spotlighting and Prompt Sandwiching both exceeded 95% ASR on AgentDojo.
  - For skills, instruction-detection is invalid by definition, because skills are all instructions.
  - The lane should therefore list "prose guard counted as a control" as an anti-pattern. Skill audits should check capability combination (Rule of Two) and route structural controls to the owning lane.
  - The claim is false if an adaptive-attack evaluation shows a prompting defense materially lowering ASR.
- **Sources and quotes:**
  - S028 § 5.1 "Prompting Defenses": "when we applied our search-based adaptive attack, the ASR is above 95% for both defenses"
  - S028 appendix (search-attack results discussion): "they offer no robustness improvement beyond the undefended model"
  - S026 § 1 Summary (motivation bullets): "prompt injection defenses that are based on simply detecting instructions in data are, by definition, not valid as Agent Skills are all instructions"
  - S026 § 4 Discussion → Recommendations: "a pragmatic first layer is to scan skills with an LLM, this inherits the scanner's own jailbreak surface"
  - S029 § "Agents Rule of Two": "agents must satisfy no more than two of the following three properties within a session"
  - S027 abstract: "skills bundling executable scripts are 2.12x more likely to contain vulnerabilities than instruction-only skills"
- **Fills:**
  - Coverage row "Failure/anti-pattern patterns" (README.md:11) → `knowledge/fail-closed-and-anti-patterns.md` § Anti-pattern table (20 rows per SKILL.md:351).
  - The lane's own audit method. [INFERENCE] By S026, LLM audits of sibling skills inherit the scanner's jailbreak surface, so the lane's deterministic verifiers are the right first layer and LLM review the second.
- **Adjacency:** runtime defenses (CaMeL / plan-then-execute, guardrail classifiers) go to `kasegi`; harness permission and approval design goes to `kumitate`. Report them; do not absorb them.
- **Recheck (2026-10-19 results):**
  - `curl -sL https://arxiv.org/html/2510.09023 | grep -c 'no robustness improvement beyond the undefended'` → `1`
  - `curl -sL https://arxiv.org/html/2510.26328v1 | grep -cE 'are all instructions'` → `1`
  - Cadence: 365d, or when a new adaptive-attack study lands.
- **Admission:** tier-A papers (three) plus vendor docs.

### E5 — `knowledge/context-file-evidence.md`
- **Claim (falsifiable):** Always-on context files are neither free nor reliably helpful.
  - Across agents and models they did not generally raise success, and they cost over 20% more inference; repository overviews were unhelpful.
  - Guidance tuned by probe-and-refine did raise the resolve rate: 33.0%, against 28.3% for a static KB and 25.5% with none.
  - On one vendor suite, a compressed docs index outperformed an on-demand skill.
  - The claim is false if a replication shows overview-style context files improve success at equal cost.
- **Sources and quotes:**
  - S016 abstract: "providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average"
  - S016 abstract: "repository overviews, although popular and recommended by model providers, are not helpful"
  - S017 abstract: "we show that how the guidance is produced is the decisive variable"
  - S017 abstract: "33.0% mean resolve rate vs. 28.3% for the static knowledge base used to initialize it and 25.5% for an unguided baseline"
  - S015 intro: "A compressed 8KB docs index embedded directly in AGENTS.md achieved a 100% pass rate"
- **Fills:**
  - Coverage rows "AGENTS.md & dispatch prompts" (README.md:12) and "Always-on checklist + self-audit" (README.md:22).
  - `SKILL.md § Always-on constraint-file checklist`, box "Size justified per line" (SKILL.md:346), gains a measured external basis.
  - Proposed new box: "no repository-overview prose; every line is non-discoverable from the tree".
- **Recheck (2026-10-19 results):**
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2602.11988' | grep -ci 'over 20%'` → `1`
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2606.20512' | grep -c '33.0%'` (abstract carries the figure)
  - Cadence: 180d.
- **Admission:** two tier-A papers carry the claim; S015 (B) supplies only magnitude.

### E6 — `knowledge/skill-evolution-dynamics.md` (seed for a `## Frontier`)
- **Claim (falsifiable):** Iterative self-revision of skill and instruction files is sparse, validation-filtered search that depends on failure evidence.
  - In a controlled study only 55 of 388 candidates set a validation best, and all 11 selected evolutions came from feedback that included failed trajectories.
  - Unvetted self-authored skills gave no average lift (SkillsBench v1).
  - Wholesale rewriting causes brevity bias and context collapse; itemized delta updates counter both.
  - This corroborates the shokunin gate from outside: admit only verified, non-harming moves; keep rejections; stay append-only.
  - The claim is false if a controlled study shows success-only feedback or unvalidated rewrites producing steady gains.
- **Sources and quotes:**
  - S014 abstract: "Evolution is sparse: only 55 of 388 candidates establish byte-distinct validation bests."
  - S014 abstract: "All 11 selections come from feedback conditions that include failed trajectories"
  - S014 abstract: "persistent skill self-evolution is better understood as sparse, validation-filtered search with model- and benchmark-dependent returns"
  - S011 **v1** abstract: "Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming." This condition is absent from the latest abstract; cite v1 explicitly.
  - S020 abstract: "brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time"
  - S021 abstract: "combine complementary lessons from the Pareto frontier of its own attempts"
- **Fills:**
  - There is no `## Frontier` (`grep -c '^## Frontier' corpus/README.md` → 0). Seed the Frontier row "self-improving skill files under a verification gate".
  - Relates to the `## Gate` practice in `lessons/round-<N>.md` (CORPUS.md:18-19).
  - Adjacency: general optimizer research belongs to `kengaku`; the lane keeps only its application to instruction files.
- **Recheck (2026-10-19 results):**
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2608.02636' | grep -c '55 of 388'` → `1`
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2602.12670v1' | grep -ci 'self-generated'` → `1`
  - `curl -sL 'http://export.arxiv.org/api/query?id_list=2602.12670' | grep -ci 'self-generated'` → `0` (version drift, recorded deliberately)
  - Cadence: on new arXiv version.
- **Admission:** tier-A papers; version-pinned citation is mandatory because of the drift above.

---

## 5. Paths (study sequences for the lane's frontier)

- **Trigger fidelity, measured — S001 → S002 → S008 → S006 → S009 → S015 → S012.**
  - Spec: what a description must carry.
  - Two client router contracts: render, budget, model-driven activation.
  - The executable optimization loop, then a second vendor's eval CSV with negative controls.
  - Evidence of the failure being measured: non-invocation.
  - Finally the scale limit, where metadata-only routing breaks.
  - Ends at E1/E2.
- **Self-improving instruction files without collapse — S020 → S021 → S022 → S014 → S011 → S013 → S016 → S017.**
  - Failure modes of rewriting come first, so the optimizer is not misused.
  - Then reflective Pareto search and its feedback-metric interface.
  - Then the empirical limits of skill self-evolution and self-authoring.
  - Then how to measure lift (paired trials; scans ≠ lift).
  - Last, the same dynamics on AGENTS.md: negative evidence, then tuned guidance.
  - Ends at E5/E6.
- **Authority and adversaries for instruction surfaces — S023 → S024 → S010 → S025 → S026 → S027 → S028 → S029.**
  - Simple ordering, then the operative spec (no authority by default; delegation; provenance).
  - Then the file-convention precedence, and where hierarchies break (many tiers).
  - Then the adversarial reality for skills (all instructions; 26.1% vulnerable).
  - Then why prose guards do not count, ending at an auditable predicate.
  - Ends at E3/E4.

---

## 6. Rejected candidates (with reasons)

1. **S030 Agentman blog (row, C).** Rejected for three reasons:
   - It contradicts the client guide. It says the skill "will not load" on a name/folder mismatch (`curl -sL https://agentman.ai/blog/build-your-first-agent-skill-skillmd-anatomy | grep -ciE 'skill will not load'` → 2). S002 says "warn, load anyway" (`curl -sL https://agentskills.io/client-implementation/adding-skills-support.md | grep -ciE 'warn, load anyway'` → 2).
   - It credits an angle-bracket rule to the agentskills.io spec, which has none (`curl -sL https://agentskills.io/specification.md | grep -ciE 'angle bracket'` → 0).
   - Its quantitative claims cite unnamed secondary analyses.
2. **Design Patterns for Securing LLM Agents (arXiv 2506.08837) and CaMeL (arXiv 2503.18813).** Both opened; not rowed. They are runtime agent architecture (control/data-flow separation). That is `kasegi`/`kumitate` province, so report it rather than absorb it. The lane needs only the consequence for audits: E4's "prose guard ≠ control" plus the Rule of Two predicate (S029).
3. **The lethal trifecta (Simon Willison, 2025-06-16).** Opened; B tier; not rowed. For audit use it is subsumed by S029, which cites it and states the auditable predicate. Adjacent to `kasegi`.
4. **Claim: "LLMs perform better when relevant information is at the beginning or end", attributed to Chroma's context-rot report.** It surfaced in a `web_search` synthesis citing a Medium summary, and that page returned HTTP 403. Rejected because the primary report says "Testing across 11 needle positions, we find no notable variation in performance for this specific NIAH task" (S019 § Needle-Question Similarity → Results; `curl -sL https://www.trychroma.com/research/context-rot | grep -ci 'no notable variation'` → 2).
5. **`web_search` synthesized answers as sources (tier C, AI summary).** In this session they conflated two SkillsBench versions: v1 has 86 tasks, 11 domains, 7 configs and the self-generated condition; the latest has 87 tasks, 8 domains, 18 configs. They also gave SkillRouter's drop as "31–44" where the abstract says 37–44. Never cite a synthesis; open the primary and pin its version.
6. **Candidate rule: "Do not hide skill bodies — description-only routing loses 37–44 points" (from S012).** Rejected as a design rule for this host. S012 measures a ~80K-skill registry with heavy overlap, while this host's catalogues hold 7–18 skills (README.md:16 and :20). That is a scale mismatch, so it stays a frontier question, not a rule.
7. **Candidate rule: "Progressive disclosure cuts tokens ~40% and raises accuracy 15–20%" (from S030).** Rejected: unsourced secondary estimate in a C-tier page.
8. **MIPROv2 (arXiv 2406.11695) as a working source.** Opened; superseded for this lane's purpose by GEPA, which reports beating it by over 10% (S021). Kept as a lineage note only.

---

## 7. Mistakes mined and defects found

### Mistakes mined (7: 4 external, 3 my own; "learn by making mistakes")
- **M1.** A secondary summary misattributes an edge-position advantage to Chroma; the primary says the opposite (§6 item 4).
- **M2.** Search synthesis conflated paper versions (SkillsBench v1/latest; SkillRouter 31–44 vs 37–44). Lesson: cite `arXiv:<id>v<N>`.
- **M3.** A vendor tutorial (S030) contradicts the standard's client guide and misattributes a rule to the spec.
- **M4.** SkillsBench's headline v1 claim (self-generated skills give no benefit) is absent from its latest abstract. Claims drift across versions, so pin the version (E6 recheck shows 1 → 0).
- **M5 (own).** My first coverage-map count used `grep -c '^| [^-A]'` and got 44. That drops data rows starting `| A…` (AGENTS.md, Aggregator, Agent-def…). The correct count is 51: `echo $(( $(sed -n '/^## Coverage map/,/^## Known gaps/p' corpus/README.md | grep -c '^| ') - 1 ))`. This is the same class as the lane's recorded counting traps (README.md:53, "three counting traps").
- **M6 (own).** My first fleet YAML sweep aborted on the first invalid file (an uncaught `Psych::SyntaxError`), which under-reports. A sweep must fail soft per file. The rerun with `rescue` found 12/18.
- **M7 (own).** My first keyword sweep put `--` before the pattern, so `--include='*.md'` was parsed as a path and errored. Re-run with `-e "$k"`; the per-file counts were 0 either way.

### Defects found (10)
- **Lane, 7.** Three overlap the STATE dossier and one is peer-supplied.
  - **D1** — no `corpus/QUALITY.md` (`test -e corpus/QUALITY.md` → absent) [also STATE].
  - **D2** — no `## Frontier` (`grep -c '^## Frontier' corpus/README.md` → 0) [also STATE].
  - **D3** — `PROVINCE.md` has no Core/Frontier/Adjacent (`grep -cE '^#+ *(Core|Frontier|Adjacent)' PROVINCE.md` → 0) [also STATE].
  - **D4** — zero external current-art sources: 0/38 Sources bullets carry a URL, 5 URLs exist corpus-wide and none is craft art, and the 16-keyword sweep finds 0 files (§1).
  - **D5** — the lane's own description contains `` `<skills>` `` (SKILL.md:14), which violates S004's "Cannot contain XML tags".
  - **D6** — SKILL.md has 521 lines, over the 500-line recommendation in both S001 and S004. The lane's own bound (~600, README.md:10) is looser than both vendor rules.
  - **D7 (peer-supplied by `W1StateKotoba`, not opened by me)** — the `verify_skill_checklist.py` "frontmatter parses" box is a lenient structural parse with no XML-tag rule, so D5 and D8 are invisible to the lane's own gate.
- **Fleet, 3.** Route to the owning lanes; do not fix from kotoba.
  - **D8** — 12/18 sibling `SKILL.md` frontmatters fail strict YAML because a plain-scalar description contains `": "` (§2 item 12).
  - **D9** — `lore-shokunin` and `souji-shokunin` have no required `name:` field.
  - **D10** — 10/18 SKILL.md files exceed 500 lines (max 1636, `tsukuroi-shokunin`).

---

## 8. Recommendations for wave 2

1. **Seed the missing corpus contract pieces.**
   - Create `corpus/SOURCES.md` from §3 (30 rows).
   - Create `corpus/QUALITY.md` with an external-source criterion: tier-A sole support, a version-pinned citation (arXiv vN, dated spec or commit) and a pasteable recheck. This is M2/M4 turned into a rule.
   - Add `## Frontier` to `corpus/README.md`, seeded by E6 and by E2's open question (routing of cached one-liners vs full descriptions).
2. **Make trigger fidelity measurable (the lane's oldest open gap).**
   - Admit E1 and E2.
   - Build labelled trigger-eval sets (20 queries, ≥8 near-miss negatives that include sibling-competition cases) for kotoba and its siblings.
   - Counting command: `jq '[.[]|select(.should_trigger==false)]|length' evals/trigger/*.json`.
   - The live trigger-rate run is a later round, with harness hooks via `kumitate`.
3. **Harden the lane's own instrument and route the fleet findings.**
   - Add strict-YAML parse, required-`name`, no-XML-tag-in-description and ≤500-line checks to `verifiers/verify_skill_checklist.py`, each with a fail-closed fixture. That would be a before → after count of executed boxes.
   - Optionally run S003 `skills-ref validate` as an independent second witness (it is demo-only, so not a gate).
   - Route D8/D9/D10 to the owning lanes as audit reports.
   - Admit E4 as a new anti-pattern row and E3 as an authority column in the instruction-surface census.
4. **Fleet-level (for the contract and canonical-sync writers).**
   - The Ruby sweep in §2 item 12 is a pasteable fleet conformance probe against agentskills.io. It could become a fleet tool check so the shokunin skills stay portable to any agentskills client.
   - SOURCES.md recheck cadences should key to versions ("on-new-version"), not only to days.
