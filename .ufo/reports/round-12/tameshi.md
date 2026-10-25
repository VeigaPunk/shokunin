# Tameshi — round 12 (resumed in-session)

## Work performed

Declared claims: **C1 calibration / capability acquisition** — repeated pristine-control gate (F3); **C2 depth / axis move** — case-level declared-witness detail for the existing bash-surface-census leg (F2). Both owned axes tied at 6; C2 works the lowest depth axis. Scalar scores remain **6 → 6**: capability is not promotion credit; reanalysis is not a seventh independent gate.

Unless fleet-rooted explicitly, evidence paths below are relative to `tameshi-shokunin/`.

- Finished the inherited standalone control gate and both missing digest-pinned snapshot expectations; appended its decision table and registry to `SKILL.md:1479-1515`. Actual CLI selftest: **29 cases PASS**, exit 0; three actual pristine bash controls matched. Evidence: `.ufo/evidence/round-12/verification-final.json`, `tools/repeat-control.py`.
- Proved the repair can fail: the same changing-fixture mismatch oracle fails against a one-loop mutant (verifier 1; wrong `controls_match`) and passes with repetition restored (verifier 0; correct `controls_mismatch`). Raw fixture/mutant/output: `.ufo/evidence/round-12/oracle-repair/`; exact commands: `oracle-repair.json`.
- Completed the pinned bash study: **10 classified**, **8 on-witness / 0 accidental / 2 survived / 0 inconclusive**; **14 exercised + 2 skipped** selftest slots. Six specific hits, two generic-only (B2/B6), one B3 extra failing case. Case-label association is not assertion-level causality. Evidence: `.ufo/evidence/round-12/BashWitness/summary.json`; main `check`/`count` receipts in final verification.
- Curated six existing opened sources, no new rows; admitted sourced F3 knowledge, appended witness-source errata, and learned the previous outside box-3 disagreement in QUALITY criterion 13. Criteria 11–12 address finite controls and declaration exposure. Evidence: `corpus/knowledge/repeated-control-precondition.md`, `corpus/QUALITY.md:32-46`, `corpus/lessons/round-12.md`.
- Resolved all nine inherited dirty paths from the terminated headless attempt; retained/completed, none silently discarded. No operator/aggregator-owned file changed. W1 dispatched 32 seats but only 30 reports survived; ControlGate/BashWitness were interrupted. Decisions and durable launch/termination digest: `.ufo/evidence/round-12/inherited.json`, lesson In-session inheritance resolution.
- Main replayed the unchanged runner: **80/80 selftest PASS**, six-leg **REGRESSION PASS**, exit 0 each. Evidence: final verification. Kagi's pinned object store was read-only; no sibling/product patch or domain push.

## Landed changes

**Pushed lane HEAD: `8742f5dcebf82bb1b57da7d7d2a7dd98a0e5c32e`** (origin master). Measured content: `9df9212d33dc2dbda133e88f28ad47bb08839a5b`. Both commits carry tameshi-shokunin / tameshi@shokunin.local. Lane push completed before this report was written.

| Commit | Work | LOG linkage |
|---|---|---|
| `9df9212d33dc2dbda133e88f28ad47bb08839a5b` | Two tools, complete source/evidence records, both waves, knowledge/source corrections, frontier index, QUALITY criteria, SKILL registry | `LOG.md:655-734`, both Round 12 entries |
| `8742f5dcebf82bb1b57da7d7d2a7dd98a0e5c32e` | SCORECARD measured deltas/capability row and pinned after output | `LOG.md:736-746`; `.ufo/evidence/round-12/after-committed.json` |

Failures remain evidence. First witness declaration refused a 40-hex git revision because of a 64-hex regex. First completed sweep crashed on skip normalization; raw crashed run retained. Classifier repairs followed outcomes, with unchanged declarations. Actual rerun agreed on all ten classifications and preserved canonical summary. Witness selftest receipt: 40/40 PASS. Evidence: `.ufo/waves/round-12/w2/WitnessFinish.md`, `BashWitness/`.

Main integration caught a fixture-path bug (selftest exit 2), an ambiguous mutation anchor, and a stable fixture mistakenly supplied to a mismatch oracle. Retained: `integration-failure.txt`, `verification.json`. After the one-line selftest path fix, the main replay passed all checks except that wrongly selected oracle fixture. Only repaired oracle rows were then re-exercised; `verification-final.json` consolidates the unchanged passing checks and repaired rows. No failed attempt was relabeled green.

## Before → after measurements

Command, run from lane root:

```sh
python3 .ufo/evidence/round-12/measure.py --rev REV
```

Both runs exited 0. Before REV: `18ad5d050ef4bcd830fe513825baed878f025024`; after REV: `9df9212d33dc2dbda133e88f28ad47bb08839a5b`. Outputs: `.ufo/evidence/round-12/resumed-before.json`, `after-committed.json`.

| Claim | Before | After | Runtime evidence / lane verdict |
|---|---|---|---|
| C1 capability | repeat_control_artifact=0; one control per existing runner sweep | artifact=1 plus demonstrated CLI/snapshot behavior; capability row entered | 29-case selftest, three real controls, frozen match/mismatch, mutation-backed oracle; **improved** |
| C2 depth | bash witness summary absent; classified defects=0 | witness_classified=10; counts 8/0/2/0; unresolved=[] | `python3 tools/bash-witness-study.py check` and `count` exit 0; raw logs/rerun retained; **improved**, case-level bound |

Guardrails: recorded_cases=6 → 6; unique_recorded_gates=6 → 6; calibration_restraint_score=6 → 6, excluding box 3 per previous outside adjudication. Command C is only an 8-point mark upper bound, not an authority-checked score. No new scalar points.

Per-axis lane verdicts: **depth improved (detail), calibration improved (capability); coverage, operability, freshness, adjacency unchanged**. No axis harm observed within exercised scope. C1/C2 commands are independent; C2 does not invoke C1. Admission remains **pending separate non-author closure**, not a lane-declared pass.

## Sources & frontier

Start/end census command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

Start output (resumed start; original attempt receipt also retained):

```text
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
exit=0
```

End output:

```text
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
exit=0
```

Receipts: `sources-before.txt`, `resumed-sources-before.txt`, `sources-after.txt` under round-12 evidence. The measurement command above produced **rows 44 → 44**, malformed **0 → 0**, tiers **A37/B5/C2 unchanged**, statuses **mined12/queued29/rejected3 → mined15/queued26/rejected3**. Added by tier: **A0/B0/C0**.

Opened existing S004/S006/S011/S026/S028/S040. URLs, dates and located quotes: lesson Gate and source-review addendum. S026 article-body access supersedes the initial reader omission; old opened dates/anchors were not rewritten. Mutable ledger:

- S004 used-by adds repeated-control knowledge; mined/recheck unchanged.
- S006 used-by adds round-12 lesson; mined/recheck unchanged.
- S011 queued→mined; used-by —→round-12 lesson; recheck unchanged.
- S026 queued→mined; used-by —→repeated-control knowledge; recheck unchanged.
- S028 queued→mined; used-by —→round-12 lesson; recheck unchanged.
- S040 remains queued, mutable fields unchanged. No tier changes.

F3 advanced from an unimplemented repeated-control next move to sourced knowledge and demonstrated finite-sample capability. F2 gained bash case-level detail but remains partly held broadly: exposed declarations, generic-only hits and no selector/assertion-level equivalence. No province Core takeover. F1 interop, legacy provenance headers, stale successor ledger and full-page box-3 sufficiency remain prior debts, not silently solved or re-scoped.

Mistake mined: one-control blind spot, with a failing one-control mutant under the same oracle. Reject samples for outside review: “three matches prove determinism”, “bash reanalysis is a seventh gate”, and “lane-dispatched review is independent authority”. A fresh outside reviewer must sample ≥1 admit and ≥1 reject; none of this lane's seats satisfies that duty.

## Trend verdicts

- **expansion: improved** — sourced F3 knowledge on previously open ground, indexed in corpus README, demonstrated capability in SCORECARD. Evidence: new repeated-control entry, mined S004/S026 links, final verification.
- **quality: improved** — historical source semantics corrected by append-only E2/E3; runtime/evidence failures repaired with retained red-before proof. Evidence: witness note, `oracle-repair.json`, final verification. No newly falsified admitted claim is knowingly left unmarked.
- **discernment: improved** — previous independent box-3 disagreement became grounded criterion 13. This uses the disagreement-learning branch, not a claim that round-12 outside sampling occurred. Evidence: `corpus/lessons/round-1-verifier-spotcheck.md:17`, `corpus/QUALITY.md:43-46`.

## SHONEN

- [~] Decision tables, error patterns, checklists, cited sources — `SHONEN.md:5-6`, `reports/round-1-calibration.md:71-103`, new SKILL registry. Lane assertion; no independent promotion verifier.
- [~] End-to-end task executed/logged — `SHONEN.md:7-8`, `LOG.md:705-746`, retained runtime experiment. Lane assertion.
- [~] Executable without oral context — `SHONEN.md:9-10`, earlier scope-limited Appendix A/B cold-read. Full-page box-3 sufficiency **unearned/unscored**; appended registry has no new full-page cold-read.
- [~] No cross-domain bleed — `SHONEN.md:11-12`, `PROVINCE.md:22-48`, read-only pinned kagi experiment. Lane assertion; no promotion.

### Host mechanics, conformance and handoff

- Waves: inherited **32** (30 reports; two interrupted tool seats), resumed **32**, total **64**. Exact mixes: `.ufo/waves/round-12/wave-summary.json`. W1: executor3/reviewer8/connector3/scout7/revenger1/critic3/sentinel1/scribe4/simplifier1/mutation-tester1. W2: executor3/reviewer8/connector3/scout6/critic4/scribe4/sentinel2/mutation-tester1/revenger1.
- One validator-approved unchanged taskCall per wave; no model parameter. L1 held canonical planner; W2 IntentDataWalk (revenger) supplied permitted data walk. W1's reviewer-carried planner-function exercise is disclosed, not falsely attributed to MistakeMining. Session role routing unchanged.
- Conformance defects: several seats initially wrote relative fleet-root report paths; authors moved their reports to the lane and removed stray copies. An accidentally fleet-wide reminder was corrected through Main; subsequent messages named owned seats only. These write-scope mistakes are documented, not claimed domain work.
- Instrument bounds: repeat-control has no supervisor/timeout; history-anchored snapshot metadata cannot defeat coordinated rewrite; witness mapping is exposed/case-level. Nested declaration.kind is null although top-level kind/disclosure are explicit. Known residuals: implementation-seat reports. No fabricated check or independent verdict.
- **Stale-lane:** respawn-per-round; this round progressed through inherited completion, lane commits and push. No other mission of this lane is open. No round 13 started.
- **Tool installs/updates:** none.
- **Open L0:** no new decision required. Prior planner-routing question answered by host addendum. Orchestrator action: fresh non-author claim replay and ≥1 admit/≥1 reject spot-check, then closure/ledger admission. No promotion claimed.
