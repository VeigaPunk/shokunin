# Global instruction discovery: Kimi Code CLI and Devin CLI

## Scope and evidence

- Read official current Kimi Code and Devin CLI documentation, and ran only version/help and Devin rule-path help commands. No agent/subagent was launched; no tests/builds were run.
- Local discovery was limited to filenames and directory names in `~/.kimi-code`, `~/.agents` (the Kimi docs' documented generic instruction location), and `~/.config/devin`. No config, credential, session, history, or profile contents were read.
- Installed versions reported: `kimi` 2.2.0; `devin` 3000.11.92. Kimi help points to `https://moonshotai.github.io/kimi-code/`; Devin help documents the default user config path `~/.config/devin/config.json`.

## Findings

### Kimi Code CLI

**Documented global instruction files**

- Kimi-specific: `$KIMI_CODE_HOME/AGENTS.md`, default `~/.kimi-code/AGENTS.md`. The global data directory and this file move together if `KIMI_CODE_HOME` is set. The environment override's current value was not checked, so local filename findings below describe the default root only.
- Cross-tool: `~/.agents/AGENTS.md` in the real OS home.
- Project examples: root `AGENTS.md` and `.kimi-code/AGENTS.md`.
- Kimi's default prompt injects workspace instructions as `${agents_md}`. The Kimi docs describe `AGENTS.md` as injected reference content, separate from a whole-system-prompt override.

`$KIMI_CODE_HOME/SYSTEM.md` (default `~/.kimi-code/SYSTEM.md`) is a different mechanism: it replaces the built-in **main agent's** system prompt, not a general rule file. A custom prompt can retain the effective default prompt and its workspace-instruction injections via `${base_prompt}`; a custom agent prompt without `${base_prompt}` owns its prompt instead. `$KIMI_CODE_HOME/agents/` and `~/.agents/agents/` are user-level custom-agent profile locations; those profile bodies are their own system prompts.

**Subagent behavior / inheritance**

Kimi documents subagents as isolated contexts: a subagent receives the task description passed by the main agent, not the main agent's conversation history. The docs explain prompt placeholders and custom agent bodies, but do not explicitly guarantee that every built-in or custom subagent automatically receives the global `AGENTS.md` content. For a custom agent, `${base_prompt}` is the documented way to retain the effective default prompt/injections; a self-contained custom body without it should not be assumed to carry those injections. No documented Kimi config field promises global instruction inheritance into every subagent.

**Hooks**

Hooks are configured as `[[hooks]]` entries in `$KIMI_CODE_HOME/config.toml` (default `~/.kimi-code/config.toml`). A `UserPromptSubmit` hook may append output to the prompt context. `SubagentStart` and `SubagentStop` are documented lifecycle events, but the docs do not describe them as a mechanism to inject inherited instructions into a subagent. Treat hooks as lifecycle automation, not a documented substitute for the global rules file or explicit subagent prompt.

### Devin CLI

**Documented global instruction files**

- Primary global rules file: `~/.config/devin/AGENTS.md`; the docs say it is loaded at the start of every session and alongside project rules. `AGENT.md` is also supported at that location.
- The rules docs also list `AGENTS.local.md` and `.windsurfrules` as supported rule filenames, and document `~/.devin/rules/*.md` plus `~/.devin/global_rules.md` as global rules locations. The latter `~/.devin` paths are outside the requested directory scan; their local presence was not checked.
- Devin can read `~/.claude/CLAUDE.md` as a global rule. The standard-rule import switch is `read_config_from.agents_standard` in `~/.config/devin/config.json` (default `true`); it controls import behavior, it is not itself a place to put instruction text.
- Devin custom subagent definitions can be global under `~/.config/devin/agents/` (flat `<name>.md` or `<name>/AGENT.md`) and contain their own profile/system prompt.

**Subagent behavior / inheritance**

The Devin rules docs say global rules are injected at the start of every session. The subagent docs say subagents run in their own conversation chain and do not inherit the parent's conversation history. Read together, this suggests global rules may be available to subagent sessions, but the cited docs do not explicitly say that subagents inherit the global `AGENTS.md` or a parent's injected context. Do not treat that inference as a guarantee; a rule that must apply to every custom subagent should also be present in that profile or in its explicit task handoff.

**Hooks**

Devin supports global hooks under the `"hooks"` key in `~/.config/devin/config.json`. `SessionStart` and `UserPromptSubmit` command hooks can inject text into context by returning `hookSpecificOutput.additionalContext`. This is a documented context-injection mechanism, but the docs do not explicitly state whether global hook context is run for or inherited by subagents. The file is JSON configuration, not a Markdown instruction destination; do not put free-form rule text directly into it.

## Filename-only local status

| Location | Observed status |
|---|---|
| `~/.kimi-code/AGENTS.md` | Not present in the default Kimi root listing / exact-name check. |
| `~/.kimi-code/SYSTEM.md` | Not present. |
| `~/.kimi-code/config.toml` | Present; contents were not read, so active hook configuration is unknown. |
| `~/.kimi-code/agents/` | Present; contains custom-agent profile files. Profile contents were not read. |
| `~/.agents/AGENTS.md` | Not present. `~/.agents/` does contain other resources, but no global `AGENTS.md` was found. |
| `~/.config/devin/AGENTS.md`, `AGENT.md`, `AGENTS.local.md`, `.windsurfrules` | None present in the requested Devin config root. |
| `~/.config/devin/config.json` | Present; contents were not read, so the effective `read_config_from` and hook settings are unknown. |
| `~/.config/devin/agents/` | Present; contains custom-agent profile files. Profile contents were not read. |
| `~/.devin/rules/`, `~/.devin/global_rules.md` | Not inspected; these are documented Devin global locations outside the requested scan roots. |

The assignment context identifies `~/.omp/agent/RULES.md` as the existing OMP global rules source. I did not read or modify it. Among the Kimi/Devin-supported global instruction destinations inspected here, there is no existing universal Markdown rules file to append a pointer to. The existing `config.toml` / `config.json` files are structured runtime configuration, and the existing `agents/` files are role-specific profiles, so neither is a safe generic Markdown destination.

## Minimal safe persistence recommendation

If a tool-specific pointer is later wanted, create a short Markdown rule at each documented destination that is currently absent: Kimi's `~/.kimi-code/AGENTS.md` (or the generic `~/.agents/AGENTS.md`, if intentionally shared) and Devin's `~/.config/devin/AGENTS.md`. The short directive can point to `~/.omp/agent/RULES.md` or reproduce the required directive. For guaranteed custom-subagent coverage, also include it in the relevant custom-agent profile or explicit handoff; vendor documentation does not establish unconditional inheritance for every subagent. No documentation reviewed promises symlink handling, and no symlink test was performed, so prefer a small readable Markdown pointer over a symlink. This is a recommendation only; no files were changed.

## Official sources

### Kimi Code CLI

- [Agents and Sub-Agents](https://moonshotai.github.io/kimi-code/en/customization/agents) — user/project agent locations, isolated contexts, `SYSTEM.md`, `${agents_md}` and `${base_prompt}`.
- [Data locations](https://moonshotai.github.io/kimi-code/en/configuration/data-locations) — `$KIMI_CODE_HOME`, default paths, global `AGENTS.md`.
- [Configuration files](https://moonshotai.github.io/kimi-code/en/configuration/config-files) — `config.toml` and config fields.
- [Hooks](https://moonshotai.github.io/kimi-code/en/customization/hooks) — hook configuration and lifecycle/context behavior.

### Devin CLI

- [Rules & AGENTS.md](https://docs.devin.ai/cli/extensibility/rules) — global rules paths, supported filenames, import switch, activation.
- [Subagents](https://docs.devin.ai/cli/subagents) — independent conversation chain and global custom-agent profile paths.
- [Hooks overview](https://docs.devin.ai/cli/extensibility/hooks/overview) and [Lifecycle hooks](https://docs.devin.ai/cli/extensibility/hooks/lifecycle-hooks) — global hook locations and `additionalContext` injection.
- [Configuration file](https://docs.devin.ai/cli/reference/configuration/config-file) — user config location and option reference.
- [Configuration import](https://docs.devin.ai/cli/reference/configuration/read-config-from) — standard rule imports and `read_config_from.agents_standard`.
