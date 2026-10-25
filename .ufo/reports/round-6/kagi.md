# kagi-shokunin — round 6 report

Commit: `kagi-shokunin@5f55ba8` ("round-6"). Domain: secrets & vault ops.

## Gap closed

**Config layering was asserted, never resolved.** Prior rounds described
`~/.config/the-janitor/config.json` as a "second overlay, shape known" and
called `opencode.json` the isolation boundary. Both were unproven — and one
was wrong.

## Method

`opencode debug agent janitor` + `opencode debug config` (opencode 1.18.31)
run under the *exact* `_serve` environment (cwd `$CONFIG_DIR`,
`OPENCODE_CONFIG` set, XDG dirs redirected to `/tmp/oj-dbg` — janitor state
untouched, no model call, no vault). Cross-checked against the embedded
`customize-opencode` doc extracted from the binary.

## Findings (resolved, not inferred)

- `OPENCODE_CONFIG` is **additive**: global `~/.config/opencode/opencode.json`
  merges underneath the janitor overlay. 9 provider defs load
  (`enabled_providers` gates to `qwen-local` post-merge); 23 fleet agents and
  global plugin `fnm-nudge.js` load into the handler process; 56 merged
  permission rules evaluate last-match-wins with janitor's
  `{"*": deny, janitor_auth: allow}` as the ceiling — resolved `tools` map
  shows only `janitor_auth: true`.
- `config.json` is **inert**: not an opencode-discovered filename, zero
  references in the launcher; resolved `steps: 4` (janitor.md frontmatter
  wins) vs its `steps: 8`. A decoy — editing it does nothing.
- Isolation corrected: the walls are `enabled_providers` + permission
  ceiling + `_serve`'s 18-var credential unset — **not** the config boundary.
  Global-config edits / new global plugins are a live drift & attack surface
  on janitor (recorded as open operator decision with hardening knobs).
- Project-config discovery from `$CONFIG_DIR` is live but unused
  (`OPENCODE_DISABLE_PROJECT_CONFIG` unset).
- Endpoint drift persists: resolved `baseURL` still `127.0.0.1:8080/v1`
  (Jitsi on 8080; model on 34113) — unchanged operator decision.

## Landed

- `corpus/knowledge/config-layering.md` — layer table, leak inventory,
  `steps` precedence, decoy proof, reproduction block.
- `corpus/drift-pins.sh` — sha256/mode/lines of all 13 cited host files;
  cheap staleness gate before trusting line refs. Smoke-run OK.
- `corpus/lessons/round-6.md` — "trust the resolver, not the files".
- `SKILL.md` — new Config layering section; corrected isolation checklist
  item; 2 new anti-patterns (dead `config.json`, false `OPENCODE_CONFIG`
  isolation); round-6 falsification row.
- `corpus/README.md` — 3 coverage rows; `config.json` gap resolved to inert;
  new open gap: global-layer leak.

Hygiene held: no vault access, no secret values, no `op://` ref paths, no
account PII in any artifact.
