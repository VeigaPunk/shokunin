# kasegi-shokunin — round 8 report

Commit: `round-8` (`585fec8`) in `kasegi-shokunin`. 5 files, +~190.

## Gap closed: `fleets/ufo-archive-2026/` (last named known-gap)

The pre-consolidation fleet snapshot (2026-09-06→14) held the richest
unread artifact class in the domain: 19 `missions/claim-*/report.json`
files — structured L1 self-reports from the claim-hardening wave over real
`claims/` packages, each with per-package before/after defect lists. All 19
extracted plus every sibling dir walked → `corpus/knowledge/ufo-archive-2026.md`:

- **22-class defect taxonomy** — the empirical superset of
  `claim-check.mjs`. Gate-visible: custodian `head_sha256` absent or bound
  to `event_sha256` instead of `decision_sha256`, stale
  `expected_head_sha256`, missing/orphan same-digest redaction receipts
  (wordpress: 22/27 artifacts unreceipted while 12 reusable receipts sat
  uncopied in `evidence/`), status.json field absence, submit-payload drift
  (hash mismatch, duplicate+absolute-path attachments).
  Checker-invisible: **missing in-package `submission-draft.md` was the
  dominant defect** (nearly every claim-ready package); stale
  `submission-review/packets/` drafts — one materially wrong, concluding
  dev-trunk-only while the vulnerable stable endpoint shipped (web1
  buddypress); receipt-drift duplicate-submission hazards (H1 #4028846,
  Bugcrowd a169f309 → `RECEIPT EXISTS` banners); "verified"-never-executed
  vectors (coinbase 3-4); citation drift; alias/canonical status
  confusion; proven-but-not-claimable (gamma-deposit: published audit
  finding + deployed fix verified first-hand via blockscout);
  falsified-by-execution (elastic EPR-STOR-1 → exclusion-notice draft).
- **Outcome vocabulary**: REFINED→DONE, HOLD with named blockers,
  NOT-SUBMITTABLE, reconcile-only (verified prior submission),
  stop-frontier-saturated. `no_submission_performed` is the norm — no
  mission submitted anything.
- **b1k-NNN provenance resolved** (dangling since round 4):
  `bounty-keeper/keeper.mjs` — 16-pane wall, LAUNCH_CAP 384, 12 h night
  budget, launched 265, halted `night_budget` 2026-09-11 — produced the
  run_ids `ledger/candidates.jsonl` and `evidence/*/b1k-NNN/` reference.
- **Naming drift**: archive `claim-packages/<slug>` paths are the
  pre-rename tree; verified live that those packages now live at
  `claims/<platform>-<program>/<slug>/` (hackerone-coinbase/metamask/
  mongodb exist; `claim-packages/` gone).
- **Reconciliation evidence chain** recorded from claim-spotify-oauth:
  `ledger/missions.jsonl` SUBMITTED →
  `fleets/run/portal-reconciliation-2026-09-11.json` (authenticated portal
  read) → `.ufo/claim-recovery/final-audit.json` →
  `ledger/candidates.jsonl` do-not-re-hunt → git commits. All paths
  verified present today.
- Old per-program evidence shape (`programs/<id>/` authority/custodian/
  scope-snapshots/state-ledger), `inquiries/` L0 mission briefs (original
  full-loop charter + 2026-09-06 L2 route decree), `bounty-whipper`
  nudge tracker, schema-v1 `sighting/handoffs`, and the bountyA0912
  read-only control-plane study (`non_execution` manifest) all
  characterized.

`SKILL.md` gained the "Claim-hardening wave" section (10-class defect
table + fix patterns + cited path); `corpus/README.md` coverage-map row +
gap marked closed; `LOG.md` + `corpus/lessons/round-8.md` recorded.

## Verification

- All cited paths re-verified live: `fleets/run/portal-reconciliation-
  2026-09-11.json`, `.ufo/claim-recovery/final-audit.json`,
  `.ufo/bounty-fleet/` present.
- `claims/hackerone-{coinbase,metamask,mongodb}` exist; `claim-packages/`
  absent — the rename claim is observed, not inferred.
- `git log` → `585fec8 round-8`.

## Domain state

Every named gap in `corpus/README.md` is now closed except
`fleets/registry.json` route semantics (flagged cross-domain — kumitate's
surface; the permanently-red `@role` checker bug was reported round 7 and
is unchanged) and `george/` (parked — no claim package references it).
Remaining depth is per-program claim anatomy (~274 dirs, ~10 sampled);
diminishing returns until a new defect class appears. Corpus now covers:
pipeline, gates, policy playbook, triage/EV, terminal classes, VDP format,
ledger, evidence store, control plane, retirement lane, ops invariants,
intake/finalize — and now the hardening-wave defect layer above the gates.
