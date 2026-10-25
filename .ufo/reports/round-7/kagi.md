# kagi-shokunin — round 7 report

Commit: `kagi-shokunin@51c9d30` ("round-7", pushed). Domain: secrets & vault ops.
L2 wave: 9 lanes, one batch — ScriptVerify, AuthRepro, ClaimCheck, SiblingOverlap,
BoundaryAttack, DaemonEnvAudit, DraftDiskState, DraftTrustBoundary,
HardeningHandoff. All completed; verifier corrections folded in.

## Gap closed

**The corpus had documented every verb and every config layer, but never the
socket the handler actually listens on, and never what it writes to disk.**
Both gaps hid boundary errors: the janitor "deny ceiling" was documented as
isolation, and "process-memory-only" read as if nothing persisted.

## Findings (verified on scratch replicas, never the live daemon)

- **Port 40961 is an unauthenticated HTTP API.** `_serve` never sets
  `OPENCODE_SERVER_PASSWORD`; the server prints `server is unsecured` on
  stdout at launch. Repro: `POST /session` → 200 no creds; password set ⇒ 401
  on *every* route incl. `/global/health`, Basic `opencode:<pw>` ⇒ 200
  (`OPENCODE_SERVER_USERNAME` honored, Bearer rejected). No project-trust
  prompt, no Origin/Host validation, no per-UID check — any uid in the host
  netns can drive it; agent names are enumerable via unauth `GET /agent` /
  `GET /config`.
- **The `{"*": deny}` ceiling was never socket-scoped** — it is per-request
  agent frontmatter. Three verified escape routes: (a) `POST
  /session/{id}/shell {"agent","command"}` executes in 51 ms with **no model
  call**; (b) `agent` names any permissive loaded agent; (c) the body `tools`
  map re-enables denied tools *under `agent:"janitor"`*. Tool subprocesses
  inherit the serve env — `OP_SESSION_<domain>`/`OP_SERVICE_ACCOUNT_TOKEN`,
  plus tmux-server leftovers (`SSH_AUTH_SOCK` live agent, `XDG_RUNTIME_DIR`
  GPG sockets) and a docker-group uid. Clean-shell `op` hangs (negative
  control): the daemon env is the *sole* vault-capable context. Blast radius
  = the operator's whole user session.
- **Squat-phishing is real**: `client.py` sends no auth/pinning — a mock
  control plane answering `JANITOR_ACTION_REQUIRED` can harvest operator
  approvals; `ensure_started` detects only the no-tmux squat shape.
- **Transcripts persist at rest**: `xdg-data/opencode/opencode.db` (0600 via
  the wrapper's `umask 077`) holds plaintext request/reply text and tool
  parts — 7 sessions / 39 messages / 55 parts observed — past `stop`, which
  rm's only `session-id`. No purge verb. `opencode.log` is the durable
  diagnostic surface (endpoint `stream error` ≈58 s exponential backoff;
  `fnm-nudge.js` load failure on all 8 recorded starts — the global plugin is
  inert by *failure*, not just permission).
- **Lock/wedge topology measured**: `request` holds `client.lock` through the
  whole round-trip (default 3600 s); a hung request wedges `stop`/`start` —
  only `tmux kill-session` unblocks. Readiness texts are timeouts, not
  diagnoses (120 probes ⇒ 60–300 s; wedged server prints the
  "authorization" message).
- **tmux env passthrough trap**: a pre-existing tmux server does not inherit
  the caller's env — `OP_SERVICE_ACCOUNT_TOKEN=x the-janitor start` silently
  drops the token and falls into the interactive path. The documented
  headless path is conditional on server provenance (`set-environment -g` or
  a fresh server works).

## Landed

- `corpus/knowledge/handler-trust-boundary.md` — auth matrix, three escape
  routes, env-inheritance proof, fix recipe, `/doc`-driven repro.
- `corpus/knowledge/handler-on-disk-state.md` — XDG map, DB/log forensics,
  lock table, 8-state wedge taxonomy, isolated-tmux repro harness.
- `corpus/knowledge/control-plane-hardening.md` — operator rollout:
  password + `client.py` `Authorization` header together (else
  `server_healthy` 401s into misleading texts), transcript purge cadence,
  residual-risk statement (password ≠ isolation vs same-uid).
- Corrections: `credential-isolation.md`, `config-layering.md`,
  `janitor-lifecycle.md` — ceiling reframed as per-agent policy; transcript
  durability; `janitor_auth` = `op vault list` exit-code probe.
- `SKILL.md` — trust-boundary + disk/wedge sections, diagnose row, wedge
  failure causes, tmux env trap, checklist/anti-pattern/falsification rows.
- `corpus/lessons/round-7.md` — "the ceiling was an agent, not a socket";
  scratch-replica method notes; README coverage + two open operator gaps.

## Integrator items

- CDP 9222 (kake fleet): the documented `webzites` lease is cooperative
  serialization, **not** an ACL — the same loopback-is-not-a-boundary
  question applies to that listener; ownership ruling still open.
- Hardening is an operator decision (touches `_serve`/`client.py`); recipe
  staged in `control-plane-hardening.md`.

## Hygiene

No vault access performed; `OP_*` values used in probes were fake
placeholders; no secret values, `op://` ref paths, or account values in any
artifact; DB inspection was shape/count-only (`?immutable=1`). Real janitor
state untouched (still `state stopped`); all scratch servers killed.
