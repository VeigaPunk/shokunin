# Obsidian CLI probe — evidence for the deferred integration task

Probe date: 2026-10-18 (mint session, orchestrator). Deferred per operator:
the Obsidian integration is a later task **within** the shokunin training
(goal), not mint-time work. This file is its evidence base.

## What the official CLI is

Obsidian's official CLI ships bundled with the desktop app since v1.12
(2026-02-10); no separate download. It is agent-oriented ("anything you can
do in Obsidian you can do from the command line") and bypasses the REST API,
talking to vaults via subprocess calls that respect indexing and sync.
Enablement is operator-side: Settings → General → Advanced → "Command line
interface" → Register.

Sources:
- [Obsidian CLI Tutorial (2026): Every Command, TUI Mode & Claude Code](https://frankanaya.com/obsidian-cli/)
- [Obsidian + Claude Code: Q2 2026 Update](https://mostlycopyandpaste.com/articles/2026/05/obsidian-claude-code-q2-2026-update/)
- [Productivity App Updates March 2026](https://themodernobserver.com/tech/productivity-app-updates-march-2026)

## Host probe results (measured)

- App version: **1.14.4** (`~/.config/obsidian/obsidian-1.14.4.asar`,
  update check reported up-to-date at probe time).
- CLI flag: **enabled** — `~/.config/obsidian/obsidian.json` =
  `{"vaults":{"357200b26f64b4e9":{"path":"/home/vgpnk/Documents/shokoknowledge","ts":1791912393905,"open":true}},"cli":true}`.
- Vault registry: one vault, `/home/vgpnk/Documents/shokoknowledge`
  (lane-named folders visible at top level: atlas, kagi, kaidoku, kake,
  kama, kasegi, kengaku, kotoba, kumitate, lore, protocol, revenger,
  sources, game-dev-2d, game-dev-3d, audio).
- `/usr/bin/obsidian` is the **GUI launcher** (bash wrapper →
  `electron43 /usr/lib/obsidian/obsidian.asar`), not the CLI shim.
  `obsidian --version` launches the app (probe process had to be killed —
  do not use it as a CLI probe).
- `obsidian-cli-inspector` is present in PATH (unprobed — probe in the
  integration task).
- No shim found in `~/.local/bin` or `/usr/local/bin` at probe time —
  locating the registered CLI entry point is the integration task's first
  claim; until then, vault verification falls back to direct filesystem
  hash comparison under the vault path (read-only).

## Integration task contract (for the assigned round)

Capability claim: ledger-backed `moved-to-obsidian` verification assisted
by the official CLI — confirm a ledger row's vault-side hash against the
vault via CLI (fallback: `sha256sum` under the vault path), keep
`corpus/knowledge/obsidian-ledger.tsv` as the receipt of record, never
write to the vault from souji (read-only probe), and record the CLI entry
point + a `--selftest`-style fixture run in the SCORECARD capabilities
table. Vault writes stay operator-owned.
