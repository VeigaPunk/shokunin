# kasegi — round 5

**Gap chosen:** the mission control plane — `fleets/` runtime + audit lanes
— the last major undocumented layer of the bounty domain. Claim packages
(rounds 1–3) and ledger/evidence stores (round 4) were covered; the layer
that dispatches, tracks, models-routes, and lands results was only a
one-row "ops inventory" mention.

**Landed (all inside `kasegi-shokunin/`):**

- `corpus/knowledge/mission-control.md` (new, ~9 KB):
  - `ops/fleet-dispatch.mjs` full read → dispatcher mechanics: queue-score
    weights (priority 9e12 > continue 2e12 > curated 1e12 > reward.min,
    EV ordering never a gate/AR12), 2 h `leases.json`, tmux `fleet-grid`
    pane rotation, restart-safe `reconcile()`, sole-committer P21 +
    `claim-check` P20 gating, `claim-ready/<id>/<slug>` tag with
    byte-diff proof + atomic push, UTC-3 dual-method model windows,
    strict-signature 429 detection → grok-only lane, `--sync` allowlist.
  - `fleets/missions/` = 584 generated L1 assignments (every one has a
    status file); `fleets/run/` census: 703 status files (PARKED 646 /
    DONE 27 — 13 w/ claims deliverable / SCOPING 20 / RETIRED 6 /
    BLOCKED 2 / HUNTING+WRAPPING 2) + 537 gzipped logs; `_`-prefixed
    seat statuses (`_claimer`, `_review-orchestrator`, `_b1k-*`).
  - Sibling L1 contracts: `claimer-mission.md` (operator-authed CDP
    submissions; its status records 3 H1 report URLs + Intigriti
    ID-check BLOCKED), `review-mission.md` (486-item verdict sweep).
  - Resume path: `state-snapshots/` + `docs/RUNBOOK-resume.md`.
  - Audit lanes: 21 `.ufo-mission-report-bh*.md` (all BLOCKED readiness
    audits), `.ufo-warden/` dispatch ledger, `.ufo-ingestion/` intake
    cycles + claim-ready tracker covering the *different*
    `origin-work/open-bug-bounties` tree.
- `SKILL.md`: new "Mission control plane" section + 5 cited paths.
- `corpus/README.md`: coverage-map row for mission-control.
- `LOG.md`: round-5 entry with evidence.
- `corpus/lessons/round-5.md`: closed items, friction, parked gaps.

**Commit:** `round-5` on `kasegi-shokunin` main.

**Parked / next-round candidates:** `fleets/registry.json` lane routing
(likely cross-domain), `fleets/ufo-archive-2026/` (10-subdir archive
census), `george/` (still no claim-package links).
