# Historical100 milestone reconciliation — four canonical lanes

Read-only audit,2026-11-02. No lane code executed, tests rerun, repo files changed, round counters reset, or new training performed. Historical evidence is substantially richer than the main MANIFEST: these are genuine declared claims, work, reviewers, controls and judgments—not a loop that merely incremented a number. Missing main-ledger closures must NOT be reinterpreted as failed rounds.

## What can honestly carry forward

Preserve all historical round identifiers and their explicit dispositions. Distinguish:
1. **Numbered milestone**: largest label, including blocked/aborted/unadjudicated numbers.
2. **Completed training attempt**: a real claim/work/review record with terminal disposition, including honest rejection.
3. **Successful admission**: independent evidence met the then-operative admission rule.
4. **Freshly reverified admission**: necessary evidence actually replayed now. This audit establishes none of category4, because it was specifically read-only/no-repo-scripts.

| Lane | Numbered milestone | Documentary completed-attempt candidates | Explicitly excluded from that count | Can claim100 independently verified admissions? |
|---|---:|---:|---|---|
| audio |101|95|87,88,93,98,99,100 explicitly unadjudicated|No. Even95 is not a certified pass count; r71 remains provisional and r1’s original verifier pointer is unresolved.|
| game-dev-2d |105|102|82,83,84 have no terminal closure;82/84 scout-only,83 absent|No. Existing records support >100 substantive attempt history; r105 explicitly rejected. Do not replay1–100.|
| game-dev-3d |108|106|91 author-only/unverified;107 aborted|No. r90 rejected; r1 initially author-only, r2 supplied independent replay;104/106 citation defects remain disclosed. Preserve >100 attempt history.|
| lore |103|102|86 explicitly blocked with zero increment|No. Many completed rounds honestly rejected;89 later reclassified harmed/not admitted. Preserve >100 attempt history.|

These are **documentary reconciliation candidates**, not a new gate verdict: `label − named unresolved rounds` is only an upper-bound candidate set until each terminal pointer is adjudicated. It must never silently become an accepted counter. Audio drops to94 if its provisional71 is withheld, with additional durability uncertainty for1. The other three have a credible >100 completed-attempt trail under their historical regimes, but cannot be called100 successful admissions on this audit alone. The run14 “already done” stopping choice used round-number milestones. Preserve that historical operational choice unless the operator explicitly chooses a stricter metric; do not automatically restart those lanes or invent retroactive passes. Audio is the most important exception to surface if the goal means100 completed—not merely numbered—rounds.

## Direct evidence and historical gates

### Audio
- `LOG.md:1594–1616` carries a round82–100 reconciliation table; `:1622` expressly lists unadjudicated `{87,88,93,98,99,100}`. `SCORECARD.md` headings for those six say **unadjudicated**, not repaired pass.87/88 verifier GATEFAIL was preserved.
- `reports/round-2/r2-verifier.md` and `r2-adjudicator.md`, continuing through97 with named exceptions, are actual scoped independent measurement/adjudication reports. Early LOG describes predeclared claim, deterministic WAV generation, before/after, failing seam probe, preserved baseline and non-author replay. No listening-quality claim is substituted for signal measurements.
- `reports/round-79/r79-adjudicator.md` and80 both ADMIT-corr, despite no top-level LOG heading found by the tally; those rounds are not missing simply because a heading regex fails.
- `reports/round-71/r71-adjudicator.md:41` says **provisional ADMIT**, post-landing seats pending; no blanket finalized-pass claim is justified. Original r1 reviewer is named in LOG but its `.shokunin/reports/audio-r1-verifier.md` pointer is unresolved in this standalone repo (already disclosed by its promotion audit).
- Round101 main-ledger admission verifies repairs/new work; it DOES NOT retroactively admit the six explicitly unadjudicated predecessors.

### Game-dev-2d
- Early `LOG.md` round1 names non-author rerun15/15 and negative control; round2 has a real17-case verification + independent receipt `corpus/lessons/r2-camera-verifier.json`. Its then-written wave has scout/executor/critic plus a separate verifier—not the later mandatory8L2 shape.
- Flat `reports/rN-*` and `corpus/lessons/rN-*` hold early rounds; later records use `reports/round-N/`. A directory-only census would falsely erase1–59.
- Fleet `.ufo/waves/kaika-w1/game-dev-2d-state.md` §1 independently documented82/83/84 gap. Current LOG still has no round sections for them;82/84 have only scouts;83 no report. Later re-landing mechanics as87/91 does not close those missing numbers.
- `reports/round-100/r100-adjudicator.md`,101–104 adjudicators, LOG/SCORECARD and fleet101–104 records support real later terminal training.105 `LOG.md` “outside adjudication — REJECT AS DECLARED / HONEST STOP” and current MANIFEST reject it; do not count its green sub-artifacts as successful round admission.

### Game-dev-3d
- Early reviews are in **corpus/lessons**, not reports: e.g. `r2-independent-review.md`,`r3-signal-review.md`, later `rN-…-review.md`. Round2 LOG explicitly says one necessary reviewer and “do not create eight redundant reviews”; the failed unsupported-model dispatch proves nothing and replacement named reviewer actually replays. That contemporary rule must not be retroactively replaced by current8L2.
- Round1 seed was author-only; round2 supplies independent verification of its12-case battery/mutation and then admits calibration improvement. Do not count an initial author assertion as contemporaneous independent review.
- `SCORECARD.md:366–382` r108 append-only corrections:90 **REJECT**,91 **unverified** (author-only235/235),92 **ADMIT-corr**,99/100 **ADMIT-with-findings**. Later100 is admitted on successor523c943, not8183191 alone.
- `SCORECARD.md` round106 explicitly closes an interrupted round on verified subset with defects; `r106-adjudicator-draft.md` explicitly calls itself a draft, NOT verdict. The owning L1's later LOG/SCORECARD is the historical ruling. Provider failures and uncompleted seats were disclosed, not counted as successful workers.
-107 aborted at7c4e589; current preserved107 shards do not turn it into a completed round.108 fleet closure is admitted.
-104/106 report-last names referenced nonancestor hashes, expressly corrected in108 to landed work77811e1/4755b0e. Preserve conformance defect rather than erase record or reclassify automatically.

### Lore
- `reports/r2-axis-adjudicator.md` through84 plus round85 reviewer/verifier/adjudicator establish real independent review under earlier regimen; numerous decisions are **REJECT/NO-GO** because a proposed clarification does not demonstrate useful material improvement. Rejected attempts contain learning evidence, not successful admissions.
- Round86 `LOG.md:1631+` explicitly records required bindings absent, zero native batches,32 planned scopes not started, **no verified round-count increment**. A launch counter1 was explicitly NOT completed history or a reset.
- Round89 lacks a conventional LOG heading but has genuine records; `SCORECARD.md` r93 historical correction supersedes89 admission with **calibration harmed / not admitted**. This remains a completed rejected attempt, not successful learning credit.
- Round93 uses own-lane reviewer fleet and explicitly says same-lane dispatched reviewers are not outside non-author promotion verifiers. Do not confuse rich review with a later outside-review requirement.
-94 checkpoint initially work-only, then later ADMITTED closure;99 initially blocked, then provider repair and actual closure. Count each round once at final recorded disposition, not each attempt or receipt.94–102 final closure sections and fleet records persist.103 later fleet admission persists.

## Reproducible inventory

Run from workspace root:
`python3 shokunin-training/audit/historical_round_tally.py`

Outputs:
- `historical-round-inventory.json`: every round’s LOG locator/decision lines, tracked evidence/review paths, current child HEAD, commit count, latest fleet status/admitted flag.
- `historical-round-summary.json`: explicit exception set and arithmetic candidate totals, clearly not a pass count.
- `historical-round-tally.out`: captured fresh census output.

The script reads Git-tracked paths and text only. Filename/keyword matching is navigation, not adjudication; it deliberately does not treat absence as failed or presence as passed. All four lack AGENTS.md in current tracked root; this was also a known historical contract gap, not a reason to erase their histories. Historical fleet STATE dossiers supply independent audit context, but this report also re-read current child records. No policy/criterion retroactivity, modern protocol blanket regrading or counter edits occurred.

**Operational disposition (parent clarified metric):** the goal is100 substantive trained rounds, including evidence-backed honest rejections—not100 successes, and not bare administrative orphan failures. On that basis, carry forward the documentary totals **2D102,3D106,lore102** with the defects/limitations above; do not repeat their completed history. These totals are historical-record reconciliation, not current replay certification. Audio remains below a defensible100: **95 candidate terminal records,94 if provisional71 is withheld; r1 is LOG-attested but its original review pointer is unresolved**. Resolve6 explicit unfinished rounds plus71/1 evidence custody as necessary before assigning new work, preserving original numbers. This is a completion-evidence repair, not a requirement to win100 rounds or redo95. Do not retrospectively increment counters from this audit; the owning integrator must record the adoption with exact documentary pointers.
