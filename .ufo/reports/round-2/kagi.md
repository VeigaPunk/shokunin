# kagi-shokunin — round 2 report

**Lane:** secrets & vault ops (the-janitor flows, credential-hygiene evidence)
**Commit:** `9b3e49f` in `kagi-shokunin` — 10 files, +594/−6
**Vault access:** none. No `op` vault command, no `the-janitor request`, no
janitor tmux session started. No secret value or `op://` ref path recorded.

## Gap picked and why

Highest-value gap was double: (a) `SKILL.md` was still the 12-line seed —
zero decision content, `SHONEN.md` 0/4; (b) the seeded `corpus/README.md`
indexed 7 entries but only 1 file existed on disk — an unverifiable index is
worse than none. Both closed in one pass: corpus filled first, SKILL.md
rewritten on top of it.

## What landed

- `SKILL.md` rewritten: vault-ops decision table (intent → correct surface →
  never → expected output), exact failure-text table with exit codes,
  credential-hygiene checklist, evidence-receipt patterns (checksum/custody
  split, negative-space assertions, fixed verification vocabulary), 8
  anti-patterns. Every claim cites a file read or a live probe from today.
- `corpus/knowledge/` — 4 new entries: credential-isolation (cmd_serve env
  strip, fixed model, deny-all agent + `janitor_auth.ts`), op-env-refs
  (refs/run split, redaction direction), tac-evidence-integrity (tac-check
  semantics, O_EXCL custody, boundary vocabulary), cdp-bridge-1password
  (NMH manifest mechanics, open-popup refusal, shared-port caveat).
- `corpus/lessons/` — 2 new entries: round-1 (deferral record + 3 carry-forward
  rules) and round-1-aggregator-audit (CORPUS.md conformance verdicts).
- `corpus/README.md` reconciled: fixed wrong MANIFEST key
  (`rounds[1].deferred` → `rounds[1].lanes.kagi: "not-dispatched"`), updated
  gaps, recorded that `config.json` was read for key-shape only (values
  unrecorded by design).
- `LOG.md` — round-1 deferral backfilled, round-2 entry with evidence list.

## Evidence

Probes run: `the-janitor --help`, `the-janitor status` (state stopped),
`the-janitor cdp-bridge status` (nmh present, browser support executable,
cdp 9222 down), `op --version` (2.35.0), `tmux ls` (only `ufo_sighting`),
`stat` modes on op.env/config.json/state files. Full reads: the-janitor
(333 ln), client.py, opencode.json overlay, janitor.md agent, janitor_auth.ts,
tac-check (88 ln), handoff-status.json, MANIFEST.json rounds[1].

## Residual gaps (next round candidates)

- No end-to-end `the-janitor request` ever run — the one missing proof for
  `SHONEN.md` promotion; requires operator-side 1Password unlock/approval.
- `op` signin/account-get/service-account paths unexercised.
- Secret rotation/revocation practice: no evidence found on inspected surfaces.
- CDP 9222 lease ownership vs kake fleet — reported, not absorbed.

## Cross-domain flag

Shared musketeer chrome profile + CDP port 9222 with webzites/kimi fleet —
ownership unresolved, surfaced to integrator per PROVINCE.md.
