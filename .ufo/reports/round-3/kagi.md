# kagi-shokunin — round 3 report

**Lane:** secrets & vault ops (the-janitor flows, credential-hygiene evidence)
**Commit:** `06ef644` in `kagi-shokunin` — 6 files, +174/−10
**Vault access:** none successful. One bounded `the-janitor request` attempt
reached the auth gate and failed; no `op` vault command ran. No secret value,
`op://` ref path, or account-identifying value recorded.

## Gap picked and why

Round-2 report named it: no end-to-end `the-janitor request` had ever run —
the one missing proof for SHONEN promotion — and `op` signin/whoami/account
paths were unexercised. Both closed in one live pass.

## What landed

- **End-to-end attempt, negative result, real evidence.** `echo 'Reply with
  the single word READY.' | the-janitor request` exercised stdin contract,
  `client.lock` flock, `ensure_started`, tmux spawn, `_serve` env strip —
  died at the 1Password gate: `handler exited before becoming ready`, ~60 s,
  exit 1. Root cause: caller-side `the-janitor whoami` → `account is not
  signed in`; `op signin --raw` dies non-interactively inside tmux.
- **Endpoint drift discovered:** `opencode.json` pins `127.0.0.1:8080/v1`,
  but 8080 is a **Jitsi videobridge** (Jetty 404s, `jitsi_jvb_*` metrics);
  llama-server serves the pinned Qwen3-Coder-30B model on **34113**
  (`/health` → ok). No janitor gate probes the model endpoint — `status`
  prints configured values, not verified capabilities. Even with auth fixed,
  requests would 404 at prompt time.
- `corpus/knowledge/op-cli-surface.md` — new: `op` command matrix
  (`account list` works signed out, fields `url`/`email`/`user_uuid`/
  `account_uuid` — values PII, withheld), whoami/signin failure states,
  auth-path matrix, drift check recipe, `cmd_stop` idempotence.
- `corpus/lessons/round-3.md` — new: 5 carry-forward rules (predict with
  `whoami` before spending 60 s; `status` = config not capability; `stop`
  is always-safe cleanup; account-list values are PII-class; readiness gate
  covers auth + OpenCode health only).
- `SKILL.md` — decision table +2 rows (whoami predictor, endpoint `/health`
  check), failure table cause extended (`op signin` non-interactive death),
  2 anti-patterns, falsification extended.
- `corpus/README.md` — 2 coverage rows, gaps rewritten (SHONEN status, `op`
  partial coverage, open endpoint drift as operator decision).
- `LOG.md` — round-3 entry with full evidence trail.
- `SHONEN.md` — box 2 checked: end-to-end task *executed* and logged
  (negative result at a documented boundary; a successful reply still needs
  operator `op signin` + endpoint fix). Boxes 1/3/4 remain unchecked —
  promotion not claimed.

## Evidence

Probes (all metadata-only): `the-janitor status` (state stopped), `tmux ls`
(no janitor session before or after), `the-janitor whoami` (exit 1),
`op account list --format=json` (1 element, shape recorded), `the-janitor
request` (60 s, exit 1, exact failure text), `the-janitor stop` (`already
stopped`, exit 0, removed stale `session-id`), `ss -tlnp` + `curl` on
8080/34113 (drift proof), `ps` (llama-server cmdline, Jitsi JVMs),
`config.json` key-shape (`$schema`/`agent`/`provider` — values unrecorded).

## Residual gaps (next round candidates)

- Operator-dependent: `op signin` (or service-account token) + endpoint fix
  (overlay → 34113, or move listener to 8080) — then a successful
  `the-janitor request` round-trip.
- `op account get` JSON shape, service-account path still unexercised.
- Secret rotation/revocation practice: still no evidence on any surface.
- SHONEN boxes 1/3/4 unchecked; promotion needs a *successful* end-to-end.

## Cross-domain flag

- Port 8080 squat by Jitsi is a host-fleet conflict affecting this domain's
  fixed model endpoint — surfaced, not fixed (touching Jitsi is out of
  province).
- CDP 9222 / musketeer profile sharing with kake fleet: unchanged, still
  reported-not-absorbed.
