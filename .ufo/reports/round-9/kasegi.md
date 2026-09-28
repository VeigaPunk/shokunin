# kasegi-shokunin — Round 9 report

**Lane:** kasegi (bounty & security research). **Round:** 9 / 2026-09-28.
**Commit:** `c80c2a1` `round-9` in `kasegi-shokunin` (SKILL.md, LOG.md,
corpus/README.md, + corpus/knowledge/submitted-registry.md,
corpus/lessons/round-9.md; also swept in a pre-existing untracked
aggregator-mirror lessons file — left intentionally, on-topic).

## What landed

**`corpus/knowledge/submitted-registry.md`** — the consolidated
do-not-refile set for `~/Projects/bounties`, which previously existed
nowhere. Contents:

- **Verified filings (3):** H1 4002776 mozilla (closed_duplicate→3721615),
  H1 4002810 spotify (closed_duplicate→3892215), H1 4002789 airtable
  (not_established; `status.json` BLOCKED but `submission_state:SUBMITTED`
  + `submitted_url` carry truth).
- **Archive-era filings (3):** H1 4028846 (k8s-nodebound), Bugcrowd
  a169f309-… (ld-node-stream), e4f41218-6036-… (mattermost; owning mission
  claim-web1). Correction vs my L1 draft: the receipt-bearing packages are
  **not gone** — they live in the live sibling tree
  `~/Projects/origin-work/open-bug-bounties/claim-packages/`
  (`submission-review/` receipts.csv 3 rows + 6 JSONs + queue.json +
  CONTRADICTION.md).
- **Probable-unverified (3):** H1 4028904/4028953 (elastic), Bugcrowd
  4ecbaf46-9548-… (aiven) — orphan receipts conflicting with admin records;
  do not refile, do not delete.
- **VDP (1):** anthropic-plugin-dev-cmd-injection, free disclosure
  2026-09-06 (ledger DISCLOSED_FREE row at identical timestamp).
- Field-semantics traps (19 signature clusters; `submission_performed===true`
  vacuous corpus-wide; `no_submission_performed:false` polarity trap;
  `submitted_url` vs `submission_url`; structured alias fields
  `duplicate_of`/`DUPLICATE_OF_SUBMITTED` vs unused `claim.json alias_of`;
  3 stale `claim-ready/*` + 9 `claim-hold/*` tags); 15 status-less claim
  dirs (13 ingestion-seeded stubs + 2 partials); root zips = frozen
  ≤2026-09-15 snapshots.

## ⚠ Live hazard surfaced (operator attention)

**Queued claim row 4** `claims/hackerone-anthropic/plugin-dev-test-hook-
command-injection` (DONE, `claimable:true`, in `docs/claim-ready-index.md`)
is the **identical finding** already disclosed via the Anthropic VDP
(same title, commit `d7dbd9a`, file, source sha256, CWE-78). Live proof:
`node ops/claim-check.mjs` on the package → `OK` despite the VDP receipt —
the duplicate gate reads only `claims/*/*/status.json`. A `claim-hold/*`
tag exists on it yet the generated index still queues it. Filing it would
double-file the operator's own free disclosure. Second blind spot: the
whole `origin-work/open-bug-bounties/claim-packages/` corpus (~26 pkgs,
all six archive-era receipt IDs) is outside every bounties-repo scan.
**Fix ownership: bounties repo (cross-domain; reported, not fixed).**
Advisory: extend the duplicate predicate to `vdp-disclosures/*/SUBMITTED.md`
+ origin-work + archive receipts; match on commit+file+sha256+CWE.

## L2 wave (8 seats, one batched task call — per MISSION.md)

VerifyRegistry (reviewer): 6/6 claims CONFIRMED + DISCLOSED_FREE row found.
CollisionAnalysis (connector): hazard CONFIRMED with live claim-check OK;
upstream fix shape advised.
FieldSemantics (sentinel): triple detector confirmed safe-but-incomplete;
vacuous `===true` leg; polarity traps.
SweepStores (scout): origin-work receipt store, `_claimer.status.json`
submitted[]/disclosed[], `.ufo/bounty-fleet/reports/` found; zips' internal
submission records inventoried.
FieldProvenance (revenger): 19 field signatures mapped to producer waves.
Probes (executor): all 5 probes CONFIRMED; refuted `claim.json` as alias
vehicle; zips provably non-live.
CiteAudit (scribe): 43/46 cites verified; 4 discrepancies — all corrected
in the final files (aiven mis-attribution, STAGED truncation, alias-marker
inversion, 22-vs-21 audit count).
FalsifyRegistry (critic): empty yield — findings recovered from transcript
(origin-work discovery); yield-shape failure logged as telemetry.

## Status

Every named corpus gap is now closed; depth work remains (per-program
anatomy sampling) but the highest-value structural hole — "what was
already filed" — is done and it immediately produced a real hazard.
