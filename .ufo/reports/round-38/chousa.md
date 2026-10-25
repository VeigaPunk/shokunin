# chousa — round 38 report

Lane tip at report: `870074e8aaf01333c8fe3bdd218eba3a0f2e9a01` (pushed; cited per claim).
Landed gate `tools/research-gate.sh` sha256 `0447ad14b6135441f39f9220d02ae2967b810f791a2f1058654ee0c800c3b85a`; selftest PASS (272 cases, 0 skipped) on those bytes.

## Work performed

Declared claims (frozen `corpus/evidence/round38/claims.md` at `504c1d2a…`, 13 errata appended):

- **C1 — operability** (lowest scored axis, 3/10): the canonical pin capture's child runs through ONE pinned absolute `env` (override absolute+GNU-reporting, refused exit 2 `ENV_PROVENANCE`), so a caller-exported `env` function cannot interpose. Routed input: the round-37 exported-env witness.
- **C2 — calibration**: every round-38 counter receipt binds gate_sha256_pre==post (changed gate refuses, no receipt), counter/expect/receipt digests; `verify-receipts.py` re-derives from committed bytes and fails closed. Routed input: the round-37 counter-strength debt (F1/F4).

Work items (evidence pointers):

- Freeze + construction: counters, expectations table, controls (base-gate-r37 reused; pre-round-38 gate `9fcac047…` committed as `base-gate-r38.sh`), before/after receipts (`504c1d2a…`).
- Wave 1 (32 seats, 30 returned): re-derived both predicates on fresh seeds (w1/ExecC1Rederive, ExecC2Rederive, ScribeKnowledgeC1/C2); replayed F1 live (w1/ExecF1Replay: r38 refuses exit 2 no receipt, r37 accepts stamped with the target hash); second delivery mechanism (w1/ExecEnvFnHarness); no-harm battery (w1/ExecNoHarm, re-run after a seat demurral); gate-mutant and counter-mutant matrices (w1/MutGateC1, MutCounterC2 — all counter mutants killed); **four verifier kill candidates** (w1/CritC2Kill: legacy laundering, identity reroute, doctored observations, vacuous receipts); cell coupling (w1/ExecDoNothingCtl: c2 on base gate 4/7); ambient `BASH_ENV` forge moving the r37 control to 7/7 (w1/RevCounterC1); do-nothing/text/errata/separability/routed-queue/frontier/overlap audits (w1/CritDoNothing [died], CritNoexec, CritTextOverreach, RevSeparability, RevRoutedQueue, ScoutFrontier, ConnOverlap, SimpCounters, SentScope/SentNoNet).
- Wave-1 integration (`1f0add70…`) closed the kills pre-wave-2 (census-tied verifier, ok re-derivation, counter_rc decoupling, BASH_ENV scrub, re-sealing doctors, shlex-quoted shim, pre/post table hashing); disclosed to in-flight seats; wave 2 re-closed the loop.
- Wave 2 (32 seats, 30 returned): all wave-1 kill fixtures refuse by name (w2/W2CritLaundering — one survivor closed as Erratum 9 strict schema; w2/W2CritVacuous, W2RevVerifyFinal); mutated-verifier catch confirmed via re-sealed doctors (w2/W2ScribeKnowledgeC2: 4/7 when the counter/expect checks are deleted); final re-derivations (w2/W2ExecC1Final/C2Final: 7/7 ×2 seeds each, controls 2/7 and 0/7); separability on final bytes (w2/W2RevSeparabilityFinal); receipt byte-audit 9/9 clean (w2/W2RevReceipts); new wave-2 classes closed/named: POSIXLY_CORRECT false-kill (gate `unset` + scrub), PYTHONPATH child channel (`-E` pin + scrub), pre-run stale receipts, type-laundering, malformed-row crash (Errata 9–13); no-harm battery final (w2/W2ExecNoHarmFinal).
- L1 probes: legacy-receipt fail-closed check; BASH_ENV forge closed + honest attack live (seeds 38501/38503); full receipt re-verification (9/9 + 2 cross-refusals).

## Landed changes

Lane commits: freeze `504c1d2a…`; integration `1f0add70…` (wave-1 closures); `8e93bc91…` (SentScope closures); final `870074e8…` (wave-2 closures + frontier). All tied to the LOG.md round-38 entry:

- `tools/research-gate.sh` — env pin machinery + capture `"$ENV_BIN"` + selftest cases 268–272 + `unset POSIXLY_CORRECT` (`870074e8…`).
- `corpus/evidence/round38/` — counters, verifier, frozen expectations, claims + Errata 1–13, 9 receipts (all `VERIFY: ok`; c1 base receipts refuse the landed gate), controls.
- `corpus/knowledge/env-pin-capture-r38.md` (S072) and `receipt-binding-r38.md` (S073); `corpus/lessons/round-38.md` (7 mistakes); `corpus/QUALITY.md` 55; `corpus/SOURCES.md` S072/S073; README rows + frontier; SCORECARD r38 + planned-39; SKILL.md gates table (272, r38 row); r37 knowledge L1 repair.
- `.ufo/waves/round-38/` — wave specs, dispatches, 30+30 seat reports.

## Before → after measurements

- C1: `ENV_PIN_CAPTURE_MATCH` **2/7 → 7/7**. Command (lane root): `python3 corpus/evidence/round38/c1-count.py --gate tools/research-gate.sh --seed N --receipt F`. Before: `receipts/c1-base-s38001.json` + `c1-base2-s38003.json` (both base gates; measured at `504c1d2a…`). After: committed receipts on seeds 38001/38011/38351 + wave-1 38211/38231/38251 (reports) + wave-2 38411/38431 (`w2/W2ExecC1Final.md`), every receipt `gate_sha256=0447ad14…` on the final bytes. **Met under the Erratum-6/13 narrowed reading** (function-export interposition + missing/non-GNU override refusals; the PATH half, relative-override refusal, positive override witness: named, demonstrated by mutants, pre-registered r39).
- C2: `RECEIPT_BINDING_MATCH` **0/7 → 7/7**. Same command shape with `c2-count.py`. Before: `receipts/c2-base-s38101.json` (the r37-counter pipeline). After: committed 38101/38111/38371 + wave-1 38221/38241 + wave-2 38421/38441; separability 7/7 on the unfixed base gate; the four wave-1 kill fixtures refuse by name in wave 2. **Met under the Erratum-2/10/11 narrowed reading** (integrity + self-consistency, NOT authorship; the verifier-mutant pass-through class named with `verifier_sha256` carried).
- No-harm (final bytes): selftest PASS 272; claims 17/17 CLEAN; chain 17/22 CLEAN; broken control DRIFT (2 sections); archives 3/3 (`w2/W2ExecNoHarmFinal.md`).

## Sources & frontier

- Census before → after: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0 both ends. Before: 71 rows (A 65/B 1/C 5; mined 48/queued 19/rejected 4). After: 73 rows (A 67/B 1/C 5; mined 50/queued 19/rejected 4), malformed 0; standing W04 ×2 (S051/S053) + the expected S070/S073 shared-URL warning.
- Rows added: 2 — S072 (tier A, `bash.info` exported-functions statement, opened locally 2026-10-24, no network; anchor corrected to 1461–1464 per the wave's re-open) and S073 (tier A, `supersedes S070 —` the `-c, --check` anchor-label correction).
- Rows touched old→new: none (S070 stays mined; its used-by citations remain valid — the supersede is a new row per contract rule 2; logged in the lesson ## Gate).
- Frontier rows advanced: S072/S073 enter `mined` at creation (used-by the two new knowledge entries, same commit); no recheck changes.
- Sourced claim: **C1** rests on S072 (opened this round; `env-pin-capture-r38.md` cites it for the export-delivery statement). Mistakes mined: 7 (lesson ## Mistakes, each class/evidence/captured-by/fix, fixes shown able to fail by the wave kills). Rejected candidates recorded in the lesson Gate.

## Trend verdicts

- **expansion: improved** — two knowledge entries on new measured ground (capture env pin; receipt binding), README index + frontier updated, S072/S073 opened+mined, a second pre-round control committed.
- **quality: improved** — both fixes measured 2/7→7/7 and 0/7→7/7 across construction, wave-1, and wave-2 seeds with three independent runner classes; selftest 267→272; and the waves did real falsification: four verifier kills, a cell-coupling defect, a live harness forge, and two fresh wave-2 classes were each demonstrated, closed, and frozen as errata — not absorbed.
- **discernment: improved** — the lane's first in-round kills of its own frozen claims (both C-claims' general wordings falsified beyond their counters' cells), honestly frozen as Errata 1–13 with predicates' standing receipts distinguished; QUALITY 55 captures the verifier class; SHONEN unchanged (all `[~]`, promotion holds for a non-author review).

## SHONEN

- [~] SKILL.md decision tables/error patterns/cited sources — `SKILL.md` Gates table (selftest 272, r38 counter row); `corpus/knowledge/env-pin-capture-r38.md` (lane assertion; no non-author verifier)
- [~] End-to-end domain task executed and logged — LOG.md rounds 9/25/37/38 batteries (lane assertion)
- [~] Instructions executable without oral context — `bash tools/research-gate.sh --selftest` (272 cases PASS at `870074e8…`)
- [~] No cross-domain bleed, PROVINCE.md accurate — PROVINCE.md unchanged; zero network (strace, both waves); w1/w2 ConnOverlap scans confirm in-province (lane assertion)

## Wave shape, seats, residual

- Shape: **v1, two waves of 32** (validated under policy v1, band 32–64; each dispatched as exactly ONE task call carrying the validator's taskCall; planner seat held by the L1, its data-walk riding the ScoutCounters/RevClaims-class seats per the orchestrator ruling). No residual call: wave 1 produced ~40 distinct attack items (≥32), so wave 2 ran at full 32.
- Wave 1: 32 seats — executor 6, scout 3, scribe 3, reviewer 6, critic 5, mutation-tester 3, sentinel 2, revenger 2, connector 1, simplifier 1; §3 floor met inside it. **30 returned, 2 dead**: CritDoNothing + ScoutCounters, provider `cyber_policy` refusal (last error text: "This content was flagged for possible cybersecurity risk… (code=cyber_policy)"); the L1 covered both seats' material (predicate attacks; counter recon).
- Wave 2: 32 seats — executor 4, reviewer 7, critic 6, mutation-tester 3, scribe 3, scout 4, sentinel 2, revenger 1, simplifier 1, connector 1. **30 returned, 2 dead**: W2CritEnvFinal + W2LabEnvScrub, same provider refusal; the L1 ran both probes (forge closed at 2/7, honest attack live).
- Round total: **64 seats** (≤128). Routing via the host route table; no per-seat model pins; answering models not individually recorded (no claim depends on one). One mid-wave integration per wave was disclosed to in-flight seats as it landed (same pattern each time; who/when named here: the L1, at the wave-1 and wave-2 integration points).

## Report extras

- **Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no seat installed anything; strace 7.2 already present; all sources opened from installed man/info pages).
- **Inherited state:** none (attempt 1; no `.ufo/waves/round-38/` existed at launch, lane clean).
- **Misroot sweep:** `git status --porcelain` at the fleet root shows no chousa-round-38 files outside the lane (only driver/operator files and other lanes' artifacts, untouched).
- **Operator ruling requested:** the admission is ADMIT-with-errata — both frozen predicates verify on every committed receipt and no axis is harmed (every falsified clause names a pre-existing or out-of-surface defect, each demonstrated and dispositioned), but the claims as first written do not stand un-narrowed; §Errata 1–13 freeze the narrowings and the r39 fix directions.
- **L0 questions:** none.
