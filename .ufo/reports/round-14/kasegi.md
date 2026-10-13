# kasegi — round 14 report

Lane: kasegi (depth + coverage, bounty/security research). Repo:
`~/projects/shokunin/kasegi-shokunin`. Round: 14/1024. Axis-move: **depth**.

## The move (one sentence)

Repaired the r13-named thin cohort (Program-rule checklist 28.6, Disclosure
anti-patterns 29.7 — vs mean 96.5) to per-item source citations, and pushed
claim-anatomy sampling from ~3.6% to 10.7% with a reproducible deterministic
selection rule.

## Measured (falsifiable targets — MET)

Instrument: `/tmp/kasegi-r14/density.py` (labrat reimplementation of the r13
census; calibrated on the exact pre-r13 blob `fc6d398`: both target blocks
reproduce r13's recorded ev/dens exactly, mean Δ+0.8, all residuals explained
as r13 table-arithmetic noise + mutually inconsistent r13 date counting).
Same script on before (HEAD `7483333`, 590 lines) and after (694 lines):

| block | before | after | bar (pre-edit mean 102.5) |
|---|---|---|---|
| Program-rule checklist | 28.6 | **106.6** (3.7×) | ✓ |
| Policy access playbook | 62.5 | **462.5** (7.4×) | ✓ |
| Disclosure anti-patterns | 29.7 | **108.4** (3.6×) | ✓ |
| Claim-hardening wave | 123.3 | 196.7 | ✓ |
| Evidence-package anatomy | 110.5 | 175.0 | ✓ |

Path-citation instances 275→373. Bar rule fixed this round (SCORECARD): each
repaired block vs its own BEFORE + the pre-edit mean — the post-edit mean
(142.5) is self-inflated by the repair; the executor independently flagged the
same circularity. Form-sensitivity documented (identical content: 86.0 at
80-col prose vs 973.3 as a table) → rendering form held constant.

Sampling: 20 new full `status.json` reads → **30/280 = 10.7%** (was ~10/280).
Deterministic stratified rule (`/tmp/kasegi-r14/select20.sh`: universe 280,
17 already-read excluded, strata quota 0/2/2/2/14, even-index stride;
byte-identical re-runs; L1 re-ran as acceptance).

## What landed

- **SKILL.md Program-rule checklist + playbook**: every bullet/row carries
  per-item `path:line` anchors; all 18 scope-snapshot keys documented (SKILL
  named 9+2); `program-quirks.md` linked from SKILL (closes r13 repair-2's
  SKILL half); playbook rows gained the r13 repair-7 anchors (Bugcrowd
  401/404 holders, SIX autopsy) + live GraphQL/policy_sha256 exemplars.
- **SKILL.md Disclosure anti-patterns**: all 10 items per-item cited (wrap
  rows `:17-23`, payload audit `:91-97`, decree `fleets/claimer-mission.md:29`,
  I8 `fleets/mission-template.md:20`, BLOCKED.md `:17-20`, INGESTION
  `:14-15`, runbook `:11-20`); new per-item anchor-map table (r13 repair-3
  deliverable); 4-fact wrap-report addendum (`:83`,`:92`,`:99`,`:107`,`:155-157`).
- **3 SKILL falsifications repaired in place** ("round-14 correction"):
  header "every fix is a disclosure defect" (2 NO-GO rows are reproduction
  gates, `wrap-report.md:9,:20-21`); `:412` receipt-drift pointers (4028846 /
  a169f309 live in origin-work `submission-review/`, NOT in the two named
  bounties-repo reconcilers); Immunefi `policy_sha256` overreach (beanstalk
  provenance has zero hash keys; Immunefi page hashes are telemetry
  `html_sha256`).
- **2 corpus defects repaired**: `claim-package-contract.md` state enum
  omitted PARKED (248/280 = 88.6%); `policy-access-playbook.md` "(seek,
  openai, spacex autopsies)" misattribution (seek has no autopsy; openai/
  spacex/blofin verified `:6` each).
- **New canonical entry** `corpus/knowledge/claim-anatomy-sample.md`: the
  sampling record + D1-D13 deviation classes. Headlines: 260/280 (92.9%)
  deviate from the canonical required-key set; `claim_review` present 26/280;
  `claimable` absent 241/280 (b1k-* cohort); verdict = free-form slug (249
  distinct/280, suffixes `-identity` ×121 / `-host-binding` ×69); DONE ≠ filed
  (spacex-starlink + hackerone-x claimable-unfiled; `submission_performed
  ===true` = 0/280). SKILL anatomy rows now carry attestation strength.
- **Staleness annotation**: `docs/claim-ready-index.md` on-disk = 11 rows
  (generated stamp 2026-09-06) vs 12 claim-check-OK packages — intigriti-yahoo
  appears only on live regeneration; SKILL `:115` annotated.
- **One critic falsification REJECTED with evidence**: the 2026-09-05 severity
  decree exists (`fleets/claimer-mission.md:29`; critic grepped only `docs/`);
  git timeline b3b1b7e3 (wrap fixes 19:54 −03:00) → 2ef530c6 (decree applied
  20:56 −03:00) proves the decree overrode the wrap's airtable ceiling advice.

## L2 fan (10 in one batched call; all returned usable output)

scout ×3 (wrap-map, checklist-sources, claim-anatomy) @m_flash · executor ×2
(anti-patterns draft, checklist draft) @m_flash · critic (46 assertions: 43
confirmed, 3 falsified — 2 upheld, 1 rejected) @m_zfl · reviewer (30
citations, 20 attached facts: 18 PASS, 2 pointer-FAIL → repaired) @m_zfl ·
connector (sibling overlap + inbound-citation inventory) @m_lunamax ·
revenger (per-item origin reconstruction + decree git forensics) @m_zfl ·
labrat (density instrument + calibration) @m_zfl. L1 independently derived
every anchor set before integrating (three-way concordance rule).

## Hazards / disclosures

- **Mid-round unverified actor (2026-09-28T23:32Z)**: `freshness_check` +
  judge-lane `reroute_drill` (simulated) telemetry appends (7225→7227) and an
  mtime-only touch on `docs/claim-ready-index.md` (bytes unchanged,
  HEAD==worktree). No cron/timer/process match; an attached `ufo_sighting`
  tmux (created 15:24) hosts a separate live agent session; both L2s alive
  that minute attest read-only; not lane-originated. Actor [UNVERIFIED] —
  reported-not-explained (second occurrence after r13's `.git` touches).
  Lane wrote ZERO bytes to `~/Projects/bounties` this round.
- Executor despawn second-yields overwrote `/tmp` drafts post-integration
  (no harm; lesson 6 records the snapshot practice).

## Adjacency (reported, not absorbed)

- `fleets/registry.json` is **not contested**: the integrator ruled the
  semantic split at r10 (decree ledger → kasegi; routing + registry-check →
  kumitate; `.ufo/reports/round-10/protocol.md:249-252`, `AGGREGATE.md:667`).
  kasegi r13's "CONTESTED" flag was stale on our side — corrected here; D-76
  remains open only for recording the ruling in both provinces (aggregator).
- kotoba `sibling-description-rewrites-round8.md:259-310` = derivative
  DUPLICATE of kasegi policy-intake facts with inbound SKILL line-cites,
  several already stale; r14's renumbering shifts them further. Full inbound
  inventory in `/tmp/kasegi-r14/connector.md`; siblings re-cite at their own
  lanes' discretion.
- Operator-relevant observation (in-domain, no action taken): 2 claimable
  DONE packages remain unfiled (`bugcrowd-spacex-starlink`,
  `hackerone-x` — D12) and the on-disk operator queue is stale vs live regen
  (11 vs 12 rows).

## Scores + next

depth 9 → 9 (integer held; thin cohort repaired, sub-metrics moved — Not-10
list: Triage economics 93.3 < mean, anatomy census 10.7% not full, "launched
265" not re-derivable). coverage 9 → 9 (no surface-set change; sub-surface
advanced under depth). **r15 plan**: Triage economics U4 lift (EV constants
from `mission-ledger.md:53-55` + `ev-model.md:19-20` into SKILL; bar =
block ≥ pre-edit mean); optional coverage sub-axis trial: anatomy census
10.7%→~20% with the same deterministic rule at a new stride.
