# mado round 39 — attempt 1 (partial, honest stop)

## Work performed

Declared claims: **C1 calibration** (re-register the repaired round-38 discrimination pair); **C2 operability** (acquire the static config-option table capability); **C3 coverage** (admit sourced config-option knowledge). This attempt completed the C1 freeze and evidence only; C2/C3 remain unlanded and are **unprovable**, so no admission is claimed.

- Read and followed the lane protocol, mission/axes, corpus contract, learning path, lane skill/province/scorecard/quality and round-38 outside spot-check. The round-38 closure routed the C1 re-registration, three uncommitted reports, an eventq privacy correction, and the round-38 report erratum (`mado-shokunin/corpus/lessons/round-38-verifier-spotcheck.md:17,20,82-88`).
- Re-derived the starting axes at base `08be4eb7fd13358ed29b096e8924005d46ac409c`: `quality/check-axis-scores.py --repo . --rev master` → navigation 55/55, calibration 50/50, operability 12/12; mismatches 0 (`mado-shokunin/.ufo/waves/round-39/receipts/axis-base.txt`).
- Replayed the old C1 pair: `python3 -I quality/check-r38-discrimination.py … --manifest .ufo/waves/round-39/receipts/manifest-frozen-r38.json --rev 08be4eb…` → 18/19, `TARGET_MISSED`, exit 1; sole failing control `c1-duprow` (`mado-shokunin/.ufo/waves/round-39/receipts/c1-redbefore.txt`).
- Froze the round registration, repaired manifest copy, baseline receipts and the three inherited round-38 seat reports in lane commit `457d1b125932c1e0d797061a2156b917bcd7edaa` (lane helper output `landed …`). The manifest is byte-identical to the repaired round-38 manifest: SHA-256 `96965518dc8ad98b52b28b406d66841758c80fd75610f9b94e0239b8adf838c8`; C1 after at freeze and current tip both reads 19/19 `TARGET_MET`, exit 0 (`mado-shokunin/.ufo/waves/round-39/w1/ExecC1After.md:15-33`).
- Validated and queued one v2 swarm wave of 64 seats; the shared dispatcher spawned 64/64 by 16:10:59, then the run continued with seats still active at last observation (`/fast/scratch/hyaku-run7/dispatcher.log`, 16:10:59–16:12:59). This report is not a substitute for the required wave integration.
- Round-start selftest: `bash tools/mado-verify.sh --selftest` → 460/460, exit 0 (`mado-shokunin/.ufo/waves/round-39/receipts/selftest-base.txt`). Round-start source census → exit 0 (`mado-shokunin/.ufo/waves/round-39/receipts/census-before.txt`).

## Landed changes

- C1 registration/freeze and inherited round-38 reports: lane commit `457d1b125932c1e0d797061a2156b917bcd7edaa`. No data claim is admitted solely from the freeze. The change has no corresponding appended round-39 LOG entry yet; this report records the in-progress state, not a completed round.

## Before → after measurements

- **C1 calibration.** Command: `python3 -I quality/check-r38-discrimination.py --c1 quality/counters/c1-r38-event-ground.py --c2 quality/counters/c2-r38-eventq.py --manifest <manifest> --rev <revision>`. Before at base with round-38 frozen manifest: `controls=19 correct=18/19 verdict=TARGET_MISSED`, exit 1. After at freeze commit `457d1b125932c1e0d797061a2156b917bcd7edaa` with re-registered manifest: `controls=19 correct=19/19 verdict=TARGET_MET`, exit 0 (`w1/ExecC1After.md`). Claim is measured, but independent non-author closure remains outstanding.
- **C2 operability.** Registered target: `quality/counters/c3-r39-options.py --repo . --rev <rev>` → fixture pass, tool present, `TARGET_MET`. No C2 data commit / completed counter measurement is present at report time. **Unproven.**
- **C3 coverage.** Registered target: `quality/counters/c4-r39-options-entry.py --repo . --rev <rev>` → admitted 1/1. No C3 entry/registry/counter data commit or completed measurement is present at report time. **Unproven.**

## Sources & frontier

Round-start census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` — exit 0; seven W04 duplicate-URL warnings and W01 S277 tier-C warning (`receipts/census-before.txt`). The separate round-end seat census also recorded exit 0 while the wave was active (`w1/ExecCensusAfter.md:6-20`); no SOURCES rows were integrated in a data commit, so final row-count delta is **0 verified**. Candidate S218/S220 source receipts and S219 work were still being integrated/reviewed; S220 overlaps held row S196, so it must not be double-counted without resolving the duplicate URL. No frontier advancement is claimed. Assimilation was started (dispatcher amendment draft), not landed. `considerthese` proposal 4 informed the C2 plan; proposal 3 informed C1.

## Trend verdicts

- **expansion — unchanged:** no verified new knowledge entry/coverage ground landed in a data commit.
- **quality — unprovable-but-better:** C1's repaired discriminator is newly frozen and passes at 19/19, but no completed non-author adjudication or data round closure exists.
- **discernment — unprovable-but-better:** the C1 red/green pair is evidenced; the required round-level admit/reject spot-check and final lesson gate are not closed.

## SHONEN

[~] SKILL.md tables, error patterns and checklists — `mado-shokunin/SHONEN.md:5-6`; no new independent verifier.
[~] End-to-end domain task — `mado-shokunin/SHONEN.md:7-8`; no new independent verifier.
[~] Executable instructions — `mado-shokunin/SHONEN.md:9-10`; no new independent verifier.
[~] Province accuracy / no cross-domain bleed — `mado-shokunin/SHONEN.md:11-12`; no new independent verifier.

Stale-lane: round 39 attempt 1 is incomplete; no later round was started. Tools installed/updated: none. No L0 question filed.
