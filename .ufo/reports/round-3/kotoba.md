# kotoba-shokunin — round-3 findings

**Lane:** prompt & skill craft. **Repo:** `/home/vgpnk/projects/shokunin/kotoba-shokunin`. **Commit:** `229b687` (tagged `round-3` per directive). **Round note:** no round-2 ran in this repo — numbering skipped 1→3; LOG.md records actual rounds.

## Gap selected

From `corpus/README.md` round-1 gap list: **"No corpus on AGENTS.md craft"** — PROVINCE.md claims `SKILL.md/AGENTS.md quality` but the domain knowledge was SKILL.md-only. Also carried citation debt: 3 bailian files counted but never read in-body.

## Delivered (all inside `kotoba-shokunin/`)

- **SKILL.md +46 lines:** new "Instruction surfaces" section — three-class taxonomy (opt-in SKILL.md / always-on AGENTS.md / one-shot dispatch prompts) with per-surface craft rules and dominant failure modes; dispatch-prompt stanza order documented (role → context → job → routing → report → `| godspeed`); 2 new anti-patterns (procedures-in-AGENTS.md, missing dispatch stanza); checklist scoped to routed files; Sources extended to all 16 surveyed skills + AGENTS.md/L1-prompt corpora. Description widened to `AGENTS.md / dispatch prompts / system prompts`.
- **corpus/knowledge/agents-md-and-dispatch-surfaces.md** — new: surface taxonomy, 5-line AGENTS.md template proof (md5sum-verified shape-identity), dispatch stanza order from `diff`, observation that routing policy drifts in dispatch prompts (scout `m_zfl`→`m_flash` interjection evidence).
- **corpus/lessons/round-3.md** — new: worked/weak entries incl. the `edit` anchor-drift retry pattern and round-number skip handling.
- **corpus/README.md** — coverage map updated; AGENTS.md gap and unread-bailian debt both closed; gaps refiled (no activation telemetry; taxonomy generalizes from 3 observed classes; no named sibling rival).
- **LOG.md** — round-3 entry with evidence pointers.

## Evidence base (new)

- `cat`/`md5sum` of 6 shokunin child `AGENTS.md` — identical 5-line constraint template, name-only variance.
- `diff .ufo/prompts/kagi-L1.md .ufo/prompts/kotoba-L1.md` — fixed stanza order; variable fields isolated to role/domain/job/round.
- Full reads: `bailian-docs-llm-wiki` (layered wiki/models/raw depth trees, `qualityScore<=2` fallback), `bailian-managed-agent` (plan-before-apply, secrets never in preview), `bailian-sandbox` (operational boundaries, credential redaction).
- `PROTOCOL.md` file-contract table — the meta-domain carve-out ("documents *patterns*; does not own protocol files") confirmed this work stays in-province.

## Cross-domain evidence encountered

The L1 prompt diff shows routing-policy drift lives in regenerated dispatch prompts rather than a durable surface — arguably protocol-lane territory (where to pin fleet model maps). Reported here; not absorbed.

## SHONEN.md checklist assessment

- [x] Decision tables, error patterns, checklists, cited sources — SKILL.md has 4 tables, 10 anti-patterns, 13-item checklist, 17 sources.
- [x] End-to-end domain task logged — round-1 rewrite + round-3 iteration, both logged with evidence.
- [x] Executable without oral context — self-demonstrating file; checklist is static-read applicable.
- [x] No cross-domain bleed — PROVINCE still accurate; surfaces work is inside "prompt & skill craft".
- [~] Promotion still requires a non-author reviewer per PROTOCOL.md ("never self-attestation") — the round-1 reviewer pass covered that revision only.
