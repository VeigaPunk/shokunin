# kasegi-shokunin — round 10 report

**Gap closed:** the 12-row operator queue (`docs/claim-ready-index.md`) had
never been audited as a set; round 9 flagged row 4 without verifying it.

**Landed:** `corpus/knowledge/operator-queue.md` + SKILL.md "Operator queue —
live audit" section + README coverage/gap closure + `lessons/round-10.md` +
LOG.md entry. Commit `04f9527` on kasegi-shokunin master.

## Verified findings (all live, 2026-09-28)

- All 12 queued rows pass `ops/claim-check.mjs` on current bytes.
- **Systemic:** `ops/claim-index.mjs:13` only consumes `claim-ready/*` tags —
  `claim-hold/*` is inert metadata. Three held packages (anthropic,
  wordpress, intel) are queued regardless. Reported, not fixed (cross-domain).
- **Systemic:** duplicate scan reads `claims/` only. Row 4
  `hackerone-anthropic/plugin-dev-test-hook-command-injection` is
  byte-identical to `vdp-disclosures/anthropic-plugin-dev-cmd-injection/`
  (commit `d7dbd9a0…`, same file, captured sha256 `ded642e8…`, CWE-78) — a
  duplicate of the operator's own 2026-09-06 free disclosure that returns
  `claim-check: OK`. Do not file.
- **Field trap:** `submitted_url` on 9/12 queued rows is a route URL
  (landing/`reports/new`), never a `/reports/<id>` receipt — queue
  membership = never submitted.
- **Per-row residual gates** extracted from each `claim_checklist.md`:
  personio takeover proof REQUIRED by program OOS; spacex same class
  "recommended"; intel `submit/BLOCKED-2026-09-11.md` still live (no authed
  Intigriti session); wordpress channel-block = historical no-H1-session
  note; 8x8 asset `eligible_for_bounty=false`; mutable-precondition re-verify
  gates on spacex/amazonvrp/x/beanstalk/yahoo.

## Evidence trail

`node ops/claim-check.mjs` ×12 → all `OK`. `git tag -l 'claim-hold/*'` → 9
tags, 3 colliding with queued rows. `claim-index.mjs` full read → no hold
consumption. VDP↔claim fingerprint grep → identical commit/file/sha256/CWE.

## Frontier

Named known-gaps in README are all closed or parked (`george/` parked round 4,
`fleets/registry.json` routing possibly cross-domain). Next rounds should
either deepen per-package dossiers (e.g. severity/portal-field conformance
per platform for the 9 fileable rows) or mine `docs/` uncited files
(`plan-round0.md` already covered; `continuation-notes.md` classes covered).
