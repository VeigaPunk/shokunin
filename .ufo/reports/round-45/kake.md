# kake — round 45 report

Lane tip (pushed): `dc7f03e7c8ba45878e0f4eb1ea87543c9466d67b` (jj-lane helper, `landed` lines:
freeze `3b4c430a`, wave-1 evidence `7ed93784`, instruments `4c538444`, measurements `290b570d`,
wave-2 spec `74c9b3cf` + registry `e545525`, final `dc7f03e7`). Base: `35b35f41ba8782872bec42a4df77407c76e7926e` (r44 tip).

## Work performed

Declared claims (2, both measured, zero exploratory):

- **C1 — operability: witness-gate audit driver v2 (receipt-integrity hardening)**, routed from
  round-44 w2 `ReviewCounterContract.md` defects 1a/1b/1c. The frozen v1 driver
  (`.ufo/waves/round-44/c44_audit.py`, sha `8ee2c8bf…`) accepts counter-error receipts,
  tool-absent receipts and stale planted receipts as witnesses (re-derived by
  `w1/ReviewV1Defects.md`, all six probes fire). Driver v2 `.ufo/waves/round-45/c45_audit.py`
  (final sha `9b824d95…`) refuses all three with named classes and re-certifies the honest
  round-44 cohort unchanged.
- **C2 — freshness: gate standing-claim re-verification and repair**, routed from
  `MutClassGate.md` (selftest coverage caveat), `CriticHarmGuard.md` (v4 receipt text) and
  `CriticC1Predicate.md` (mixed-witness caveat).

Work items (evidence pointers):

- Two v1 waves, both 32 seats, one task call each, validated under `ufo-wave-policy.json`
  (w1 `w1-spec.json`/`w1-taskcall.json`, w2 `w2-spec.json`/`w2-taskcall.json`); 64/64 seats
  returned, 0 dead; every counting command re-run and every new gate mutation-tested in wave 2
  (32 attack seats: 12 reviewer, 6 critic, 6 mutation-tester, 5 executor, 2 scout, 1 sentinel).
- L1 integration from wave-1 findings: driver v2 hardening (build-leg cohort selftest, `-O`
  guard, toolSha256 receipt→control binding, receipt-predicate summary stamping, driverSha256
  field), counter v6 docstring/alias fixes, matrix runner per-leg gating + honest-leg identity
  binding (manifest + on-disk build receipts), freshness runner falsifiability rewrite, fixture
  shape corrections + READMEs, stray `.ufo/.ufo` path-bug output removed.
- Claim-identity discovery: the frozen C2(c) tuple `22/1/4` belongs to the pre-G6 receipt
  `verification/claim/after-v5.json` (23 witnessed, `ok=false`), while the named claim receipt
  `after-final/after-v5.json` (27 witnessed) re-derives 26 class-only + 1 mixed + 0 met — found
  independently by four wave-1 seats and confirmed by a 2,384-file exclusivity scan
  (`w2/RederiveSplit.md`).
- Pycache drift remediated twice; committed frozen bytes byte-identical (git-clean; guard
  excludes gitignored `__pycache__`, `w2/SentinelFinal.md` PASS modulo that exclusion).
- Misroot sweep: zero kake-r45 files at the fleet root (all seat reports landed under the lane).

## Landed changes (all in `dc7f03e7`, ancestors as listed)

- `3b4c430a` — SCORECARD round-45 declarations (frozen before data), LOG entry, lesson skeleton.
- `7ed93784` — wave-1 spec/plan/taskCall. `4c538444` — instruments, fixtures, verification
  receipts. `290b570d` — measurements, corpus, wave-1 reports. `74c9b3cf`/`e5455253` — wave-2
  spec/taskCall/registry. `dc7f03e7` — wave-2 corrections, final receipts, corpus, SCORECARD/LOG.
- Corpus: `corpus/SOURCES.md` +S133 (Python subprocess docs, tier A, mined) +S134 (SO answer,
  rejected); `corpus/knowledge/receipt-integrity.md` (new, cites S133);
  `corpus/knowledge/claim-count-derivation.md` S130→S132 correction (append-only);
  `corpus/lessons/round-45.md` Gate (1 admit, 1 reject, 1 candidate-only) + Mistakes 14–15.

## Before → after measurements

**C1** — `python3 -B .ufo/waves/round-45/c45_matrix.py --stage before|after`
(`verification/matrix/{before,after}.json`):
- before: invalid_accepted=3 (frozen v1 certifies all three invalid fixture classes; honest
  27/27 + build 3/3 also certified, so the before is not degenerate).
- after: invalid_accepted=0, rejections_named=3 with per-leg classes (counter_error /
  tool_absent / stale_receipt — stale refused by the mtime branch at a valid exit 1),
  honest_witnessed=27, honest_build_met=3 with manifest + build-receipt identity binding.
- **Verdict: NOT MET as declared** — the frozen predicate sentence's causal clause ("over the
  invoked counter bytes") is unfalsifiable by mtime + self-reported sha (`w1/CriticC1Predicate.md`,
  model-demonstrated; disposition judged sound by `w2/AttackC1Sentence.md`). The bounded repair
  verifies; the trust boundary is routed to the operator.

**C2** — `python3 -B .ufo/waves/round-45/c45_freshness.py`
(`verification/freshness/freshness.json`):
- leg (a) selftest kills 2/4 → 4/4 (same m1–m4 mutations, v1 vs v2 shipped selftests;
  `verification/selftest-coverage/{before,after}/`).
- leg (b) v4 receipt names class runs: true (committed r44 v4 receipt) → false (fresh counter-v6
  v4 receipt, `verification/v6v4/counter-v4.json`; v5→v6 diff = 3 allowed hunks).
- leg (c) witness split: FALSIFIED as declared — the named claim receipt re-derives
  26 class-only + 1 mixed + 0 met, not the frozen 22/1/4; correction filed with both receipt
  sha256s.
- **Verdict: NOT MET as declared** (conjunctive MET fails on leg (c)); legs (a)/(b) verify.

No owned axis harmed: ledger gate green at tip (`w2/ReRunLedgerGate.md`, 3 figures 0 mismatches);
census exit 0; frozen-set guard clean modulo the pycache exclusion.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`
- Before (round start): exit 0, 132 rows, 12 pre-existing W04 duplicate-url warnings.
- After (round end): exit 0, 134 rows, same 12 W04 warnings, no E-class rows.
- Rows added: S133 (docs, tier A, mined, opened 2026-10-24), S134 (community, tier C, rejected,
  opened 2026-10-24); retained bytes at `.ufo/waves/round-45/sources/`. Touched old→new: no other
  row's cells changed. Frontier rows advanced: S133/S134 re-opened live in wave 2 (quotes still
  verbatim; S133's raw sha is a build-timestamp snapshot — visible-text hash is the stable pin,
  as for S095). Mistakes mined: lesson entries 14 (receipt-trust) and 15 (receipt-identity
  attribution). Sourced claim: C1's knowledge entry cites S133.

## Trend verdicts

- **expansion: improved** — SOURCES 132 → 134 with a logged reject; new knowledge entry on
  uncovered receipt-integrity ground; two Mistakes rows; new instruments (driver v2, counter v6,
  matrix, freshness runner) extend the operability surface.
- **quality: improved** — three HIGH latent gate defects closed with named-class refusals and an
  unchanged honest-cohort verdict; v4 receipts are mode-accurate; the witness-split figure now
  re-derives from the receipt it names; every new gate is mutation-tested able-to-fail.
- **discernment: improved** — the lane's own frozen claims were falsified twice by its own
  instruments (C1 sentence overreach, C2(c) receipt identity) and reported as falsified, not
  narrowed; four wave-1 seats independently caught the receipt identity; the mixed-witness
  caveat is now a measured, filed split.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — untouched this round (no diff at tip vs base).
- [~] At least one end-to-end domain task executed and logged in LOG.md — C1/C2 logged in LOG.md round-45 entries, measured at `dc7f03e7`.
- [ ] Instructions executable by an agent without oral context — unchanged this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched; connector scan (`w1/ConnectorSiblingOverlap.md`) found no contested scope.

## Round shape and waves

- Shape: default two v1 waves (policy v1 band 32–64; 64 total ≤ 128). §3 L2 floor met in both
  waves (connector/executor/scribe/scout/reviewer/critic present; planner seat is the L1 per the
  frozen-topology ruling; no planner/distiller seats).
- Wave 1 (build, 32 seats): 9 executor, 4 scout, 5 critic, 4 reviewer, 4 scribe, 2
  mutation-tester, 1 connector, 1 revenger, 1 sentinel, 1 simplifier. Dead: 0.
- Wave 2 (falsify, 32 seats): dispatched only after wave 1 returned ≥32 distinct attack items
  (re-runs, re-derivations, claim/predicate attacks, gate mutations, source re-opens); 12
  reviewer, 6 critic, 6 mutation-tester, 5 executor, 2 scout, 1 sentinel; attack roles 27/32.
  Dead: 0. Residual calls: none.
- Seat routing: host route table only (`task.agentModelOverrides`); no model aliases passed or
  written to the lane.

## Stale-lane, installs, L0

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused host-wide; seats and L1 used pre-existing python3/jq/strace).
- L0 questions: one appended (fleet commit `03a0f94c`) — C1 trust-boundary disposition
  (bounded trusted-local-counter reading vs required causal provenance with counter-side
  cooperation). Routed, not blocking.
- Orchestrator steer acknowledged: round 46+ switches to one v2 wave of exactly 64 seats
  (policy v2); round 45 kept its committed two-wave v1 shape.
