# kagi-shokunin — round 5 report

## Gap chosen

`corpus/README.md` known gaps named one last open hole: "no entry on
secret-rotation or revocation practice: no evidence of either was found in the
inspected surfaces." Competing candidate — re-verifying endpoint drift — was
rejected: it's already narrowed to one JSON field and is an operator decision,
so re-probing adds nothing.

## What landed (commit `244b8c1` in kagi-shokunin)

- `corpus/knowledge/janitor-lifecycle.md` — the four state objects
  (`client.lock`, `session-id`, `OP_SESSION_<domain>`, `OP_SERVICE_ACCOUNT_TOKEN`)
  with lifetime + kill semantics; per-class rotation table; revocation evidence
  trail; verification probes; anti-claims.
- `corpus/lessons/round-5.md` — rules extracted.
- `SKILL.md` — "Rotation & revocation" section (per-class rotate-at-source ×
  restart-required matrix), 2 anti-patterns (`session-id` is not a credential;
  vault revocation is lazy not eager), falsification row.
- `corpus/README.md` — 2 coverage rows; the named gap is now marked resolved.
- `LOG.md` — round-5 entry with evidence.
- `SHONEN.md` — boxes 1/3/4 checked (cited decision/failure tables present;
  SKILL.md self-contained; PROVINCE scope held, no cross-domain absorption).
  Box 2 was already checked in round 3.

## Key findings (evidence-backed)

1. **No rotate/revoke verb exists by design.** Authorization is
   `process_memory_only`; `the-janitor stop` (tmux kill + `rm session-id`,
   L173–184) is the entire revocation surface for every secret the handler
   holds — `OP_SESSION_*` and `OP_SERVICE_ACCOUNT_TOKEN` die with the daemon.
2. **Rotation is rotate-at-source, and restart-required is per class:**
   `op://` refs rotate in the vault (no restart — `op run` re-resolves per
   call); raw `op.env` values rotate by edit (no restart);
   `OP_SERVICE_ACCOUNT_TOKEN` and `OP_SESSION_*` require `stop` + restart —
   they're materialized once in `_serve`'s env at daemon start (L194–210).
3. **`session-id` is a conversation id, not a credential** — `client.py`
   `get_session_id` (L49–64) self-heals via `POST /session` when missing or
   stale (`session_exists` GET check, L41–46). Deleting it only forks context.
   Still kept out of artifacts — habit hygiene, zero benefit.
4. **Vault-side revocation is lazy.** `janitor_auth` is a spawned
   `op vault list` exit-code probe that only runs inside a model request;
   `op signout`/item delete/SA-token kill surface only as `AUTH_REQUIRED` at
   the next request. No watch/hook exists anywhere in the surface.

## Drift re-check (live, 2026-09-28)

- `status`: `state stopped`; `whoami`: `account is not signed in` (exit 1);
  state dir holds no `session-id` — all consistent with round-4.
- 34113 `/health`: `{"status":"ok"}`; 8080: 404 — endpoint drift unchanged,
  fix still `opencode.json` `baseURL` (operator decision, recorded round 4).
- tmux: only `ufo_sighting` — no janitor session running.

## Compliance

No vault access, no secret values, no `op://` ref paths, no
account-identifying values in any artifact. No `request` attempted —
`whoami` exit 1 predicts the readiness death; no model-path work was needed
for this gap. Remaining open items are all operator decisions or deliberate
non-mapping (endpoint `baseURL`, `op signin`, vault structure).
