# round-1 findings — kengaku-shokunin (LLM/model research & evaluation)

Date: 2026-09-28. Commits in child repo: `90a5ce8 round-1` (SKILL.md+LOG.md), `24ff62e round-1` (corpus/, per operator interjection requiring `corpus/README.md` + `corpus/knowledge/` + `corpus/lessons/` per `~/projects/shokunin/CORPUS.md`).

## Path correction (evidence)

- Prompt specified `~/wikillm/llm-wiki`. **Absent on host**: `find /home/vgpnk -maxdepth 3 -iname "*wikillm*"` returned only `~/.bailian/skills/bailian-docs-llm-wiki`; `-type d -iname "*wiki*"` found nothing matching.
- Actual working copy: `~/Projects/webzites/repos/llm-wiki` (402 files, 342 markdown). Siblings `llm-wiki-site`, `llm-wiki-public` exist in same dir.
- SKILL.md records this correction so the next round does not re-search.

## Grounding performed

Read 5 wiki pages + Home.md:

- `wiki/ai/agents-and-engineering/benchmark-shortlist-for-godspeed-research.md` — 8 public benchmarks ranked add-now/add-if-relevant, SWE-Bench Verified retirement (OpenAI 2026-02-23, contamination), "public benchmarks will miss" four signals, minimal stack.
- `wiki/ai/agents-and-engineering/godspeed-umwelt-iteration-2.md` — 125 agents, 21 experiments, 3×2 factorial; K2 clean split (0/3 control vs 3/3 godspeed found log-target, ~13% RMSE); variant multiplier 4–9×; tool calls +50%, wall-clock ~1.75×; T2 review gradient 7→9→13→17→19 findings.
- `wiki/ai/agents-and-engineering/godspeed-umwelt-iteration-3-alpha-shittycodex.md` — two-condition alpha design (CXF-C vs CXF-G), 10-field telemetry spec, Phase 0–3 gates, 36–40 run floor, judging schema, expansion rule.
- `wiki/ai/agents-and-engineering/gemini-3.1-pro-godspeed-benchmarks.md` — concrete task designs for the four signals.
- `wiki/ai/agents-and-engineering/gemini-3.1-pro-godspeed-test-battery.md` — SWE-bench public/private contamination paradox, predictive calibration example.
- `~/.bailian/skills/bailian-docs-llm-wiki/models/` — structured model index: `index.md`/`index.json`/`families.jsonl`/`models.jsonl`/`groups/*.json`, 180 families / 413 models (generated 2026-09-11); `profile` field tri-state semantics (missing=unknown, null=N/A, `profileCompleteness: structured-only` = mechanical fields only); hard specs live in top-level row fields.

## SKILL.md changes

Frontmatter updated (correct wiki path, shonen rank preserved). Body rewritten:
- Decision table mapping 11 task classes → benchmark family → measured property, each row sourced to a wiki page section.
- Minimal-stack rule from the shortlist note.
- 8 anti-patterns (contamination blindness, leaderboard-as-proof, uncontrolled sweeps, skipped calibration, frozen-harness violations, broken-telemetry scaling, accusation counting, public/private SWE-bench confound).
- Research-note structure: YAML frontmatter spec (title/branch/category/source_ids/last_compiled/related) + body conventions verified against 3 pages.
- Route-telemetry interpretation: per-run artifact set (`response.md` + `telemetry.json` + `judge.json`), 10 fields, baseline deltas (tools ~1.5×, wall-clock 1.5–2×, correctness 0→0), 6-row observation→interpretation→action table, cost-normalization rule.
- 8-step eval production checklist mirroring Phase 0–3 gates.

## L2 routing note

- No task-subagents dispatched this round — single-file rewrite with direct evidence, L2 overhead unjustified. If L2s are dispatched in later rounds: executor/scribe on m_kcode, reviewer on m_composer, planner on m_lunamax, critic/distiller/simplifier/revenger/labrat/mutation-tester on m_zfl, connector on m_antigravity, sentinel on m_grok, **scout on m_flash** (operator update mid-round; supersedes m_zfl).

## Non-goals respected

- No changes to `MANIFEST.json`, other shokunin repos, or files outside `kengaku-shokunin/` + this report.
- PROVINCE.md still accurate (domain unchanged); SHONEN.md checkboxes partially advanced — decision tables/checklists/cited sources now exist; end-to-end domain task still outstanding.

## Corpus (operator interjection)

- Created `corpus/` inside the child repo: `README.md` (index, coverage map, 4 named gaps), `knowledge/` 4 entries — `benchmark-selection.md`, `godspeed-eval-findings.md`, `telemetry-run-design.md`, `local-model-index.md` — each citing file paths or command output per CORPUS.md rules; `lessons/round-1.md` citing this round's LOG/commit/report.
- Corpus files verified free of zero-width chars (`grep -P '[\x{200B}-\x{200D}]'` clean); tree clean at commit `24ff62e`.
