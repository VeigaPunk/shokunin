# kotoba-shokunin — round 4 report

Commit: `kotoba-shokunin@397b29c` — "round-4: agent-def/command surfaces +
round-N dispatch mode — taxonomy 3→5 classes"

## Gap selected

Corpus README (round-3) filed: "No corpus on CLAUDE.md / system-prompt /
AGENTS.md-in-harness variants beyond this host's files; the surface taxonomy
generalizes from 3 observed classes only." The host had exactly two unsurveyed
instruction surfaces plus an unnoticed second dispatch-prompt mode inside the
already-surveyed `.ufo/prompts/` directory.

## Landed

**SKILL.md** (270 lines, +~40 vs round-3):

- Instruction-surfaces table 3 → 5 rows: added **agent definition**
  (`~/.config/opencode/agents/*.md`) and **command file**
  (`~/.config/opencode/command/*.md`); split dispatch prompt into **spawn**
  and **round** modes.
- New evidence paragraphs: agent-definition frontmatter keys
  (`subagents`, `cascade`, `permission_mode`, `whenToUse`), the
  `NOT general-purpose. NOT explore.` negative-routing convention (7/18
  files), byte-identical godspeed preamble in 13/18 files — and
  `mutation-tester.md` carrying it **twice** in-file (merge artifact, found
  via `grep -c`); command-file pointer-then-rules idiom vs inline protocol.
- Craft-asymmetry paragraph now names all five optimization targets:
  match precision / constraint survival / delegation precision /
  one-shot completeness / delta-only weight.
- 6 new anti-patterns (copy-pasted posture blocks, per-task text in agent
  bodies, dated frontmatter notes, command files restating procedures,
  spawn/round mode confusion in both directions).
- 3 new source entries.

**Corpus**: `knowledge/agent-defs-commands-and-round-prompts.md` (all facts
with commands and counts), `lessons/round-4.md`, README coverage map + gap
list updated (5-class coverage; harness system prompts, CLAUDE.md, MCP tool
descriptions, plugin manifests remain open).

Also committed: `corpus/lessons/round-1-aggregator-audit.md` — a legitimate
aggregator-produced audit artifact that was staged-but-uncommitted on the
worktree; it files 2 citation defects + 1 unfalsifiable negative in round-1
knowledge entries, which are now queued gaps for round-5.

## Evidence commands (re-runnable)

```
wc -l ~/.config/opencode/agents/*.md | sort -n        # 14–197 lines, 18 files
for f in ~/.config/opencode/agents/*.md; do sed -n \
  '/Godspeed-enabled/,/tool calls/p' "$f" | md5sum; done | sort | uniq -c
                                                      # 13 identical, 4 none, 1 doubled
grep -c 'Godspeed-enabled' agents/mutation-tester.md  # 2 — merge artifact
grep -L 'requires:' ~/.agents/skills/bailian-*/SKILL.md | wc -l   # 3 of 10
diff .ufo/prompts/kake-round-4.md .ufo/prompts/kasegi-round-4.md  # name+path only
```

## Cross-domain observations to relay

- `~/.config/opencode/agents/mutation-tester.md` has the godspeed preamble
  duplicated in-file — worth a fix by whoever owns the fleet's agent roster
  (not kotoba's province).
- `~/.config/opencode/agents/ufo.md` `cascade_note` references a provider
  parking deadline (`until 2026-08-29`) already past — stale routing metadata.
- Round-5 candidate (highest-value remaining gap): fix the 2 citation defects
  + 1 unfalsifiable negative the aggregator audit filed against round-1
  knowledge entries, or measure trigger fidelity if activation logs exist.
