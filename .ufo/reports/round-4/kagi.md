# kagi-shokunin — round 4 report

## Gap chosen

The corpus's "known gaps" named two open items: `op account get` JSON shape and
the **service-account path**. Both were scattered across `cmd_serve`'s auth
chain and never documented as a surface — the script's env-var contract had no
inventory anywhere (`usage()` lists zero knobs).

## What landed (commit `486f584` in kagi-shokunin)

- `corpus/knowledge/janitor-env-contract.md` — complete env-var table:
  path/port overrides (`THE_JANITOR_*`, `MUSKETEER_*`, `ONEPASSWORD_BROWSER_SUPPORT`),
  auth selectors (`OP_SERVICE_ACCOUNT_TOKEN` skips the whole
  `account get`/`signin`/`whoami` chain at `cmd_serve` L194 — the real headless
  path; `OP_ACCOUNT` → `--account` passthrough L196), and proof that the model
  endpoint is **not** a knob.
- `corpus/lessons/round-4.md` — rules extracted.
- `SKILL.md` — 2 decision-table rows (headless run, account selection), new
  env-contract section, 3 anti-patterns, falsification update.
- `corpus/README.md` — coverage map + resolved/open gaps reconciled.
- `LOG.md` — round-4 entry with evidence.

## Key findings (evidence-backed)

1. **`OP_SERVICE_ACCOUNT_TOKEN` is the unattended route** — present in `_serve`'s
   env ⇒ zero interactive `op` calls. Operator-gated (token must exist in vault),
   but the mechanism is already implemented and was undocumented.
2. **Endpoint truth = `provider.qwen-local.options.baseURL` in `opencode.json`**.
   `MODEL_ENDPOINT` (script L17) is a hardcoded literal feeding only `status`'s
   cosmetic `endpoint` line — the drift fix is one JSON field, and `status` will
   still print the stale literal afterward.
3. **`op account get` works signed out** — field shape recorded
   (`url`,`email`,`user_uuid`,`account_uuid`,`domain`,`type`,`state`); `.domain`
   builds `OP_SESSION_<domain>`. Values are account-identifying PII — withheld
   everywhere.
4. **`op.env` is not all `op://` refs** — live `refs` shows 2 of 10 keys hold raw
   identifier-class values (`XAI_TEAM_ID`, `TOKEN_PLAN_INFNET_IDENT`); convention
   unenforced.
5. **Credential strip asymmetry**: `_serve` unsets ~19 model creds but leaves
   `OP_SESSION_*`/`OP_ACCOUNT`/`OP_SERVICE_ACCOUNT_TOKEN` — stray caller-side
   `OP_SESSION_<other>` would reach the handler env.

## Drift re-check (live, 2026-09-28)

- `the-janitor status`: `state stopped`; `whoami`: `account is not signed in`
  (exit 1) — round-3 auth state persists.
- Port 8080: Jetty 404 (still Jitsi); 34113 `/health`: `{"status":"ok"}` —
  endpoint drift unresolved, fix identified (overlay `baseURL`).
- CDP 9222 down; tracked files sha256-verified unchanged since round-2 reads.

## Compliance

No vault access, no secret values, no `op://` ref paths, no account-identifying
values in any artifact. `the-janitor request` was not re-run — `whoami` exit 1
already predicts its readiness death; the drift fix and signin are operator
decisions, as recorded.
