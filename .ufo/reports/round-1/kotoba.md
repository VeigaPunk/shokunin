# kotoba-shokunin — round-1 findings

**Lane:** prompt & skill craft. **Repo:** `/home/vgpnk/projects/shokunin/kotoba-shokunin`. **Commit:** `1d93182` (SKILL.md rewrite + LOG.md entry + corpus/ per CORPUS.md).

## Delivered

Rewrote `kotoba-shokunin/SKILL.md` from a 20-line shonen seed into a domain skill file covering:

- **Skill-file anatomy** — 7-organ load order (frontmatter → role → gate → decision surface → procedures → boundaries → references) with per-organ exemplars.
- **Frontmatter trigger-description rules** — 7 rules: capability-first, quoted literal triggers, implicit-intent triggers, co-located anti-triggers, sibling arbitration clauses, always-on overrides, metadata for runtime deps.
- **Decision-table criteria** — when a table vs. numbered steps vs. a sentence; every row must end in an action.
- **Compression rules** — description density > body density; depth to `reference/`/`--help`, verbatim command blocks, failure signatures inline, ~600-line module bound (largest observed: omarchy 392).
- **Trigger-fidelity checklist** — 13 statically-checkable items.
- **Anti-patterns** — 8 named smells with fix direction.
- **Refusals + Sources** — every claim cited to one of 16 surveyed production files.

## Evidence base

Surveyed: `~/.agents/skills/{wwkd,godspeed,sekhmet-l3,xbrd-ask,omarchy,bailian-cli,bailian-protocol,bailian-gen,bailian-finetune,bailian-train-deploy,bailian-model-recommend,bailian-web-search,bailian-docs-llm-wiki,bailian-managed-agent,bailian-sandbox}/SKILL.md` + `~/.config/opencode/skills/ufo/SKILL.md`. Observed line counts 18 (godspeed) → 392 (omarchy); none approach the 600-line bound, so it operates as a split trigger, not a norm.

## Key findings (domain-level)

1. **Anti-triggers belong in frontmatter.** The router only reads `description`; exclusions buried in the body still cause false activation. All surveyed families co-locate them (omarchy, bailian-*).
2. **Trigger strings come in three kinds:** literal quoted invocations (`"/wwkd"`), named triggers (`"sekhmet"`), and implicit needs (`"我想做一个XX"` — bailian-model-recommend). Mature descriptions carry all three.
3. **Fail-closed is the dominant prerequisite pattern:** "if that protocol file is missing, stop and run `bl skill init`; do not guess" (bailian family) and ufo's "fail closed — do not synthesize a replacement."
4. **Failure knowledge is only worth its lines with a signature:** error text, exit code, version constraint (zsh `status` readonly trap, deploy 404 propagation). Bare warnings are dead tokens.
5. **Soft hand-off by skill name beats path deps** — bailian family routes by name with `--help` fallback; only the shared protocol gets a hard relative path.

## Review

Independent reviewer lane (m_composer map) verified all 12 citations and scored the file against its own 13-item checklist: **SHIP**, all items pass. Two soft flags resolved: added explicit citation-drift fail-closed clause (evidence-base paragraph); checklist item 4 passed via generic boundary (no same-registry sibling exists to name — noted).

## Scope notes

Did not touch MANIFEST.json or sibling repos. `bailian-managed-agent`, `bailian-sandbox`, `bailian-docs-llm-wiki` read only via line counts + frontmatter grep (not fully surveyed in-body — noted, not cited for claims they didn't support).
