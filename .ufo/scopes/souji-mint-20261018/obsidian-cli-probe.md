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

## Round-4 findings (2026-10-18) — for the operator's later CLI work

The r4 recon swarm (63 seats) established, with bounded live probes:

- **No invocable CLI entry point exists on this host.** `obsidian-cli-inspector`
  (pacman 1.0.3-1) is a third-party stats tool — its `hash` column is
  `size:mtime`, not a content digest. The official CLI is not a separate
  binary: it is the app acting as a second-instance **socket client** to
  `$XDG_RUNTIME_DIR/.obsidian-cli.sock` (JSON line `{argv,tty,cwd}`), with
  73 handlers (`search`, `daily`, `sync`, `workspaces`, …) decoded from the
  asar.
- **Registration is structurally refused under this packaging**: the
  installer copies `<execDir>/obsidian-cli` to `~/.local/bin/obsidian` only
  when `basename(argv0)` contains "obsidian" — the pacman wrapper's argv0
  is `electron`, so the check never passes, and `/usr/lib/obsidian` ships
  no `obsidian-cli` file to copy.
- **Live socket probe returned 0 bytes** in 4 bounded attempts (8–92s
  windows) while a harness-spawned app instance held the socket — the reply
  path never produced output. Verdict: CLI = socket-client model, unusable
  headless today.
- **Usable today**: the lane shipped `tools/souji-vault-verify.sh` — pure
  ledger+sha256 verification, vault read-only, no Obsidian process needed.
  When the operator lands a working CLI invocation later, only the
  `--cli` probe path needs a real entry point.
