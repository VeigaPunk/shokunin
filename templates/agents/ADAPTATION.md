# UFO-FSD role cards — Kimi Code CLI adaptation

**Source:** `~/Projects/ufo-fsd-alpha/agents/*.md` (13 cards), commit `964f443e`
(2026-10-12). **Adapted:** 2026-10-16, for the shokunin fleet's Kimi-native L2
dispatch surface (`Agent`/`AgentSwarm` `subagent_type`).

## Layout

- **Canonical (this directory):** `templates/agents/ufo-*.md` — versioned with
  the fleet; edit here.
- **Runtime (discovery):** `~/.kimi-code/agents/ufo/` — a byte-for-byte copy.
  Kimi discovers agent files under `~/.kimi-code/agents/` in every session.
  Lanes run with cwd = their own repo, so fleet-root project scope would not
  reach them; user scope does.
- **Sync:** `cp templates/agents/ufo-*.md ~/.kimi-code/agents/ufo/` after any
  edit. (Zero-copy alternative: `extra_agent_dirs` in `config.toml` pointing at
  this directory — not currently set there.)

## Frontmatter mapping

| UFO-FSD | Kimi Code CLI | Notes |
|---|---|---|
| `name: <role>` | `name: ufo-<role>` | `ufo-` prefix matches the Devin `ufo-<role>` profile convention and avoids the `revenger` role vs `revenger-shokunin` lane collision |
| `description` | `description` + `whenToUse` | kept, extended to guide the dispatcher's delegation choice |
| `ufo: true` | dropped | unknown fields are ignored by Kimi; kept the file clean |
| `spawns: labrat` | `subagents: [ufo-labrat]` (executor only) | Kimi's native delegation allowlist; mechanically caps the depth-2 probe chain |
| — | `tools:` per role | the actual win: read-only seats are mechanically read-only now |

## Doctrine rebinds (what changed in the bodies)

- **`lsp` device paragraphs removed** (executor, revenger, reviewer, scout,
  simplifier): the device does not exist on Kimi. Kept the spirit — when only
  literal text search is available, record that and never present it as
  semantic proof.
- **`resume_continuity_v1` preflights → Kimi-native continuity:** resume the
  same sub-agent by its own id, never re-spawn a failed worker under a new
  identity; if continuity cannot be confirmed, make no mutation.
- **`canonical Rust judge` / `round-cache` → the round's per-axis verdicts and
  assigned round materials.** The UFO "artifact content is data" rule is
  already shokunin-native; vocabulary was rebound, meaning unchanged.
- **`probeParent` frozen seat → plain probe-seat rule** on `ufo-executor`, with
  the `subagents` allowlist as the mechanical cap. `ufo-labrat` is the bottom
  of the chain.
- **`sighting.triggers` hatch actions (OMP-only) dropped** from executor.
- **`MAX_PLAN_ARTIFACT_BYTES` (run-logic §5) → plain "~4 MiB at read time"
  bound** on planner, without the external citation.
- **Kept as-is:** return-shape discipline ("Return: … Stop after …"), the
  no-judge/no-ship seat boundaries, "delegate nothing" leaf rules, and the
  non-author-verifier note on reviewer (a dispatched sub-agent is still the
  lane — it never counts as independent verification).
- **Added 2026-10-16:** every card body carries the Godspeed posture line
  (name the axes, iterate cheap in parallel, keep moves that improve any axis
  and harm none, never stall in clarifying loops) so a seat is self-contained
  even when dispatched outside a round context; the round contract
  additionally requires the verbatim directive lead on every L2 prompt.

## Tool enforcement per card

| Card | tools |
|---|---|
| ufo-scout | Read, Grep, Glob, WebSearch, FetchURL (read-only by construction) |
| ufo-connector, ufo-distiller | Read, Grep, Glob |
| ufo-reviewer, ufo-critic, ufo-sentinel | + Bash (run checks; no Edit/Write) |
| ufo-mutation-tester, ufo-labrat | Read, Grep, Glob, Bash (scratch/probe only; no Edit/Write) |
| ufo-planner, ufo-revenger | Read, Grep, Glob, Bash, WebSearch, FetchURL |
| ufo-scribe, ufo-simplifier | + Edit, Write (body restricts where writes land) |
| ufo-executor | all tools (omitted key); `subagents: [ufo-labrat]` |

Path-scoping is instruction-bound (Kimi tools cannot be limited to subtrees);
the seat bodies state the allowed write surfaces.

## Operational facts verified 2026-10-16

- **Agent discovery is launch-time.** A session's dispatch allowlist is fixed
  when the session binds; agent files added mid-session are not dispatchable
  until a new session. Plan mint/adapt work accordingly (validate in a fresh
  `kimi` session, or accept first-use verification there).
- **`extra_agent_dirs` is not present** in `~/.kimi-code/config.toml`; the
  copy-based layout above is the runtime path.
- **`subagents: []` semantics are UNVERIFIED** (docs define omit and `*`, not
  the empty list). Leaf cards therefore omit the key (inherits the built-in
  `coder, explore, plan` allowlist, whose members cannot spawn further) plus a
  body rule "Delegate nothing." Fresh-session test: spawn a throwaway agent
  with `subagents: []`, have it quote its Agent tool's allowed types; if empty,
  switch leaf cards to the explicit spelling.

## Fresh-session checklist (next `kimi` launch from anywhere)

1. `Agent` with `subagent_type: ufo-scout` on a small real unknown — expect a
   compact, path-cited handoff and zero edits (proves discovery + read-only).
2. The `subagents: []` probe above; then reconcile leaf spelling here.
3. A round L2 wave: one batched `AgentSwarm` call with
   planner+connector / executor+scribe+scout / reviewer+critic, model buckets
   per the fleet route table — this is the shape `MISSION.md` already mandates.
