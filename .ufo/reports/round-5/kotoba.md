# kotoba-shokunin — round 5 report

Commit: `kotoba-shokunin@4002b9f` — "round-5: fleet SKILL.md audit
(end-to-end task) + citation-defect repairs + activation telemetry located"

## Gap selected

Three records converged on one move: (1) SHONEN.md box 2 unchecked — no
end-to-end domain task executed; (2) the round-1 aggregator audit's named
next step — apply the 13-item checklist to the five sibling
`*-shokunin/SKILL.md` files, "the cheapest available end-to-end domain task";
(3) three filed corpus defects + the open "no activation telemetry" gap.

## Landed

**End-to-end domain task (SHONEN box 2 → ticked).** An independent L2
reviewer lane applied the 13-item checklist verbatim to kagi / kake / kasegi
/ kengaku / kumitate SKILL.md (110–283 lines); L1 re-verified frontmatter
items and every cited defect. Result: **all 5 fail**, driven by one
systemic template defect — every description is `Domain specialist — scopes
X` capability-only: quoted triggers 0/5, anti-triggers 0/5, sibling
arbitration 0/5 despite real named overlaps found in-body (kagi↔kake CDP
bridge, kengaku↔bailian-docs-llm-wiki model data). Artifact:
`corpus/knowledge/fleet-skill-audit-round5.md` (full verdict matrix,
per-file defects, meta-findings).

**Checklist hardened by its own audit.** The lane filed 5 ambiguity
meta-findings; SKILL.md resolved all: prerequisite defined (declared or
implied deps), action-cell rule replaces strict last-column rule, command
scope covers inline commands, citation-base rule added, sibling arbitration
pinned to `description`. Two anti-patterns gained observed-count evidence
(5/5 template failure; `webzites` bin not on PATH).

**Round-1 defect repairs (aggregator queue cleared).** Verified worse than
filed: the `bailian-train-deploy` 火山方舟/ark frontmatter quote exists
*nowhere in the file* — dropped, replaced with the true observation (its
反触发表 is a body table = counterexample). `requires.bins` scoped to 7-of-10
with named exceptions. Unswept "no counterexample" claim replaced by a real
grep sweep + 2/16 counterexample rate (bailian-docs-llm-wiki 何时使用/
何时不要使用, bailian-model-recommend 适用场景 — both restate triggers in
body).

**Telemetry located (biggest find).** Activation trace exists:
`~/.local/share/opencode/opencode.db` `part` table, `$.tool='skill'` — 415
calls / 216 sessions / 11 skills, per-prompt attribution joins verified by
hand (histogram re-run matched scout output exactly). And a mechanism that
changes frontmatter doctrine: **the router never sees raw `description`**
— the `<skills>` catalogue is a model-compressed render capped ~95–103
chars (template embedded at `~/.local/bin/omp` ELF offset 283082932;
10191 `Skill description compression failed` warns in `~/.omp/logs/`).
SKILL.md gained the compressed-render caveat + new rule 8 (front-load
match-critical text). Corpus: `knowledge/skill-activation-telemetry.md` —
query recipes, histograms, store blind spots.

**Corpus also gained** `knowledge/harness-system-prompt.md` (sixth surface
class — observed-not-owned notes), `lessons/round-5.md`, updated README
coverage map + gap list. SHONEN.md: all 4 boxes ticked with evidence lines.

## Evidence commands (re-runnable)

```
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
  "select json_extract(data,'$.state.input.name'), count(*) from part \
   where json_extract(data,'$.tool')='skill' group by 1 order by 2 desc"
                                                # 415 calls, godspeed 239 top
grep -abo '<skills>' ~/.local/bin/omp           # 283082932
grep -nE '火山方舟|ark' ~/.agents/skills/bailian-train-deploy/SKILL.md  # no match
grep -L 'requires:' ~/.agents/skills/bailian-*/SKILL.md | wc -l         # 3 of 10
wc -l ~/projects/shokunin/*-shokunin/SKILL.md   # 110–283
```

## Cross-domain observations to relay

- **Fleet-wide template defect**: all 5 sibling SKILL.md descriptions are
  capability-only (no triggers, no anti-triggers). Fix at the mint template
  or per-lane; checklist items 2–4 verify the fix.
- **kagi L53–54**: cites `handoff-status.json` bare — real path is
  `~/.local/state/tac/handoff-status.json`. **kagi L26**: `op.env` prereq
  lacks a fail-closed stop.
- **kake L46**: `webzites` invoked bare but absent from PATH (bin at
  `~/Projects/webzites/bin/webzites.mjs`, named only at L161).
- **kasegi L86**: `corpus/knowledge/claim-gates.md` resolves under the skill
  repo, but L8 sets the reader's base to `~/Projects/bounties` — ambiguous.
- **~/.omp/agent/agent.db corruption**: `pragma quick_check` fails (page 1918
  / autoindex_cache_1); gate integrity before building telemetry on it.
- **1898 `duplicate skill name` loader WARNs** across `.claude/skills` /
  `.agents/skills` / `.config/opencode/skills` — description-level
  arbitration can't fix loader resolution order; whoever owns the skill
  registry should see this.
- **`customize-opencode`** fired 27–28× in activation traces with no SKILL.md
  on surveyed roots — an activation source outside the file set.
