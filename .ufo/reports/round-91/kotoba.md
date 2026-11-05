# kotoba — round 91 (attempt 2, KotobaR91a2) — report

Lane: `kotoba-shokunin` (branch `master`). Base (freeze): `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`.
Landing: commit A `c6631ca44435f0d9cbe6b9d5a6fb57788cbe258a` (integration, corpus, instruments, wave evidence);
commit B `43d373b6739179d11594e4ae80e668e696f1716f` (LOG, SCORECARD, lesson settlement, landing receipts).
Final lane hash (remote): `43d373b6739179d11594e4ae80e668e696f1716f`. Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims (frozen in `plans/round-91.md`, freeze commit `9af1a7af`; two claims):

- **C1 — depth** (capability deepening; the lane's lowest owned axis, depth 9 < consistency 10): the mutation battery's own guard surface. Three kill rows (`mb-m2` G1 commit-check skip, `mb-m15` G1 clean-tree guard off, `mb-m16` restore read-back dropped) become killable through three new guard self-test arms. Predicate: `killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, exit 0, G1–G3 PASS, self-test ≥ 22.
- **C2 — freshness** (advisory; tied-lowest 8 under the all-axes reading): two legs. Leg A: the floors guard's nested self-test cap calibrated to a measured duration (`SELF_TEST_TIMEOUT_S` 120 → 360) and the instrument-pin admission for `check_assertion_floors.py`. Leg B: the freeze-gate exit-ladder repair for a non-UTF-8 plan.

Work items, with evidence:

- **Frozen plan and pre-data controls.** `plans/round-91.md`, `plans/round-91-controls.md` at `9af1a7af`; controls held at the freeze base: `freeze gate: 4 control(s) held`, rc 0 (`.ufo/waves/round-91/receipts/freeze-gate-r91.txt`).
- **Inherited state (attempt 1, KotobaR91).** Reused: the freeze commit, the base receipts, the wave `r91-w1` outputs (patches, READY files, seat reports under `.ufo/waves/round-91/w1/`), and the scout's quote receipts. Re-verified, not trusted: every patch re-checked with `git apply --check` and applied in the lane (`.ufo/waves/round-91/w1/*/…patch`); every self-test and predicate re-run at the landing revision (below). Discarded: nothing. Uncommitted at attempt 2's start: the wave directory and `r91-w1` READY files (committed in A).
- **Wave `r91-w1` (one v1 wave, 13 seats, band 8–16).** Ready file taken by attempt 1 (`.ufo/waves/round-91/r91-w1.ready.dispatched`, 2026-11-05T12:06:18-03:00). Seat roles as dispatched: executor 3, scout 1, scribe 1, connector 1, reviewer 2, critic 1, mutation-tester 2, revenger 1, sentinel 1. Outputs on disk for 12 of 13 seats; `ReviewerRepairs` produced no output and no result record. See § Dead seats and § Open items for the WAVE-DONE gap. The plan's § Wave shape named `LabratLadder`; the dispatched spec carries `RevengerLadder` (revenger), which is what ran.
- **Wave-1 readings (evidence, not verdicts).** ExecBatteryArms (`w1/ExecBatteryArms.md`, patch `w1/ExecBatteryArms/ExecBatteryArms.patch`); ExecFloorsCap (`w1/ExecFloorsCap.md`, patch `w1/ExecFloorsCap/ExecFloorsCap.patch`); ExecLadder (`w1/ExecLadder.md`, verdict REPAIRABLE, patch `w1/ExecLadder/ExecLadder.patch`); ScoutSources (`w1/ScoutSources.md`, S262/S263/S264 located quotes); ScribeCorpus (`w1/ScribeCorpus.md`, patch `w1/ScribeCorpus/ScribeCorpus.patch`); ConnectorOverlap (`w1/ConnectorOverlap.md`, no sibling copies of the six surfaces); ReviewerBattery (`w1/ReviewerBattery.md`, C1 guard arms, all PASS); MutTesterBattery (`w1/MutTesterBattery.md`, 7 mutants, 6 killed, 1 survived — the dropped-row `m6`); MutTesterRepairs (`w1/MutTesterRepairs.md`, 10 mutants on the C2 patches, 10 killed; F1 registry-floor coverage gap; F2 behavioural-constant coverage gap); CriticClaims (`w1/CriticClaims.md`, control defects and shortcut checks); RevengerLadder (`w1/RevengerLadder.md`, rung probe: base FAILS on the non-UTF-8 rung, repaired on the candidate); SentinelScope (`w1/SentinelScope/sentinel.md`, scope PASS; F1 floors-registry touch-list widening; F2 census 189-vs-190).
- **Addendum (`plans/round-91-addendum-1.md`, A1–A6).** Recorded after the wave's candidate readings and before the landing commit; none changes a predicate, counter, manifest row, PROBES entry or control byte. A1: the `freeze_gate` floor coupling (30 → 31) is a required touch-list amendment (observed red without it). A2: census expectation corrected to 190 (plan said 189; the rejected row counts). A3: leg B identity disposition — bound to the non-UTF-8 rung, re-derived from base bytes; identity with the routed pointer left open. A4: the plan's C1 no-work pointer corrected to the round-90 transcript. A5: two frozen controls defective, recorded and routed. A6: index and PROVINCE touch-list notes.
- **Integration (landing commit A `c6631ca4`).** The four builder patches applied in order; corpus files (`knowledge/mutation-battery-arms-round91.md`, `knowledge/timeout-calibration-round91.md`, `lessons/round-91.md`); `corpus/SOURCES.md` S262, S263, S264; `corpus/README.md` index rows (three round-91 files plus the round-90 spot-check, which was unindexed); `PROVINCE.md` § Core (the mutation battery joins the executable-instruments bullet, round-90 routed defect 3); `verifiers/check_mutation_battery.py`, `verifiers/fixtures/mutation-battery/manifest.tsv` (+3 kill rows), `verifiers/check_assertion_floors.py`, `verifiers/floors-registry.json`, `verifiers/check_tip_battery.py` (`INSTRUMENT_PINS` append), `verifiers/check_freeze_gate.py`; `plans/round-91-addendum-1.md`; `.ufo/waves/round-91/` (wave evidence, `receipts/ladder-defect.md`). Self-tests before the commit: battery 25, freeze gate 31, floors 176, tip battery 74, gate registry 74 of 74 — all rc 0.
- **Landing measurements at `c6631ca` (receipts in `.ufo/waves/round-91/receipts/landing/`, committed in B).** See § Before → after measurements.
- **Frontier step (§ 2b).** S262 and S263 opened this round by the scout seat (located quotes in `w1/ScoutSources/quote-receipts.txt`; quote grounding re-checked at landing against the saved HTML: all three S262 and both S263 quotes located, after tag stripping). One rejection row (S264). One mined mistake class per the lesson's `## Mistakes` (`landing`, `number-drift`, `vacuous`). Sourced claims: C1 cites S262 (`knowledge/mutation-battery-arms-round91.md`); C2 cites S263 (`knowledge/timeout-calibration-round91.md`).
- **Pre-data controls re-run at landing** (`freeze-gate-controls-landing.txt`): `REFUSED control ctl-c2-capline-only` — declared exit 1, observed exit 0 on the cap-only world. Expected by construction (addendum A5); a frozen-declaration defect, routed to round 92, not repaired into frozen bytes.
- **Corpus/no-harm instruments at landing:** § Trend verdicts and § Before → after measurements.
- **Lesson and LOG.** `corpus/lessons/round-91.md` (Gate, Mistakes, Considerthese, Sources, Settlement); `LOG.md` § Round 91 (freeze and landing entry); `SCORECARD.md` round-91 annotations and round-92 intentions (append-only).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| C1 guard arms, 3 kill rows, third PROBES target, fixture stub (`check_mutation_battery.py`, `manifest.tsv`) | LOG.md § Round 91, "Landing commit A" and "C1 measured" bullets | `c6631ca4` (A) |
| C2 leg A: cap 360, measured constant, arms, `freeze_gate` floor coupling (`check_assertion_floors.py`, `floors-registry.json`) | LOG.md § Round 91, "C2 leg A measured" | `c6631ca4` (A) |
| C2 leg B: non-UTF-8 plan rung repair plus self-test arm (`check_freeze_gate.py`) | LOG.md § Round 91, "C2 leg B measured" | `c6631ca4` (A) |
| Instrument-pin admission for `check_assertion_floors.py` (`check_tip_battery.py`, `INSTRUMENT_PINS` append) | LOG.md § Round 91, "C2 leg A measured" | `c6631ca4` (A) |
| SOURCES rows S262 (tier A, mined), S263 (tier A, mined), S264 (tier C, rejected) | LOG.md § Round 91, "Sources" | `c6631ca4` (A) |
| Knowledge entries (2), lesson (`corpus/lessons/round-91.md`), index rows and PROVINCE § Core line | LOG.md § Round 91 | `c6631ca4` (A) (settlement text in B) |
| Addendum A1–A6 (`plans/round-91-addendum-1.md`) | LOG.md § Round 91, "Attempt-2 addendum" | `c6631ca4` (A) |
| Wave evidence `.ufo/waves/round-91/` and `receipts/ladder-defect.md` | LOG.md § Round 91, "Wave" | `c6631ca4` (A) |
| Lesson settlement (seat record, claim readings, frontier step) | LOG.md § Round 91 | `43d373b6` (B) |
| SCORECARD round-91 annotations; round-92 intentions | SCORECARD.md, appended after the round-90 block | `43d373b6` (B) |
| Landing receipts `receipts/landing/` | LOG.md § Round 91, measurement bullets | `43d373b6` (B) |

## Before → after measurements

Every measurement names the revision it ran at. Base instrument readings were taken by running each base instrument from its own clone at the freeze base (`9af1a7af`), because `--rev` selects the tree and the running script's own bytes are what execute.

- **C1 predicate** — before: `grep -cP '\tkill\t' verifiers/fixtures/mutation-battery/manifest.tsv` at `9af1a7af` → 14; `python3 -B verifiers/check_mutation_battery.py --rev 9af1a7af… --work <scratch>` run in a base clone → `mutation battery killed 14 of 14 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0 (`.ufo/waves/round-91/receipts/landing/c1-predicate-base-clone.txt`). After at `c6631ca`: same grep → 17; the same command → `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0, G1/G2/G3 PASS (`c1-predicate-landing.txt`).
- **C1 self-test** — `python3 -B verifiers/check_mutation_battery.py --self-test`: before 19 assertions (`c1-selftest-base.txt`, base clone) → after `0 failure(s) over 25 assertions`, rc 0 (`c1-selftest-landing.txt`). The three guard mutants: SURVIVED at base (round-90 transcript, `.ufo/waves/round-90/w1/MutTesterBattery/transcripts/harness-run.log` lines 9, 22, 23) → `killed [bat-self-test exit 0->1]` at landing (`c1-predicate-landing.txt`).
- **C1 bound** — MutTesterBattery `m6` (one kill row dropped from a committed clone) keeps the self-test green and prints `killed 16 of 16`, exit 0; only the exact predicate line distinguishes it. Stated, not repaired (routed to round 92).
- **C2 leg A (cap)** — `grep -n '^SELF_TEST_TIMEOUT_S = ' verifiers/check_assertion_floors.py`: before 120 (`9af1a7af`) → after 360 (`c6631ca`, line 208); `MEASURED_SELFTEST_S = 161` (line 214). Measured duration receipt `.ufo/waves/round-91/receipts/harness-selftest-duration.txt` (160.2 s, at `9264baaa`, round base).
- **C2 leg A (floors self-test)** — `python3 -B verifiers/check_assertion_floors.py --self-test`: before 165 assertions (base tree archive at `9af1a7af`, rc 0) → after `0 failure(s) over 176 assertions`, rc 0 (`floors-selftest-landing.txt`).
- **C2 leg A (pin, tip battery)** — `git rev-parse c6631ca:verifiers/check_assertion_floors.py` = `6f2c52fb2e09e817dff3360b97400a5d6e53626c`, one `INSTRUMENT_PINS` entry. `python3 -B verifiers/check_tip_battery.py --rev <rev>`: before `guards 4 of 5; tip battery exit 0: 3 of 6`, rc 1 (round-start receipt `tipbattery-before.txt` at `9264baaa`) → after `guards 5 of 5; tip battery exit 0: 3 of 6`, rc 1 (`tipbattery-landing.txt` at `c6631ca`). The rc 1 is the three carried red gates (checklist, corpus integrity, corpus independent).
- **C2 leg A (bare floors walk)** — `python3 -B verifiers/check_assertion_floors.py` at `c6631ca`: 19 of 19 PASS, `PASS floors_guard observed=176 floor=176`, `PASS freeze_gate observed=31 floor=31`, rc 0 (`floors-live-landing.txt`, load 1.90 → 2.12).
- **C2 leg B (freeze gate)** — `python3 -B verifiers/check_freeze_gate.py --self-test`: before 30 assertions (base clone, rc 0, `c2-freezegate-selftest-base.txt`) → after `0 failure(s) over 31 assertions`, rc 0 (`c2-freezegate-selftest-landing.txt`). Able-to-fail: the repaired line reverted in a scratch world → `FAIL arm plan-not-utf8 could-not-evaluate` (`ExecLadder/able-to-fail.txt`, a candidate measure); MutTesterRepairs m7 KILLED. Re-derived defect at base: a non-UTF-8 plan exits 1 with `UnicodeDecodeError` where the docstring ladder assigns rung 2 (`ladder-defect.md`).
- **C2 leg B (ladder rows in C1's run)** — `fg-m3-ladder-refusal-to-2` and `fg-m3b-ladder-eval-to-1` both `killed` at landing (`c1-predicate-landing.txt`).
- **Census (SOURCES rows)** — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: before 187 (`receipts/census-before.txt`) → after 190 (`receipts/landing/census-after-A.txt`); `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0 both times.

Harm readings (base → landing, same commands):
- `verify_corpus_integrity.py --json`: `corpus.index.unindexed` 1 → 0; DRIFT set 5 → 4 (`tracked_files`, `report_total`, `commit_total`, `commit_unresolvable` carried; `corpus-integrity-landing.json`).
- `check_r86_routed_repairs_v3.py --base-receipt .ufo/waves/round-89/receipts/d5v3-base-receipt.json` (lane): round-start `closed 4 of 5, instance drift 4` (`base-d5v3.txt`) → landing `closed 4 of 5, instance drift 3` (`d5v3-landing.txt`); `d5ii` FAIL → PASS; `d5iii` growth lists tracked_files 185 → 188 (the three new corpus files, counted by design). The base-clone run of the same gate (`d5v3-base-clone.txt`) is not comparable: rc 2, location class.
- `check_gate_registry.py --rev`: `gate registry rows conformant 74 of 74; phantom 0`, rc 0 at both base and landing.
- `check_sibling_census.py … --province PROVINCE.md`: `province rows 20 matched 4`, rc 1 — identical to base (`sibling-census-landing.txt`).
- `verify_skill_checklist.py --json`: one non-pass, `governance.citation_resolves` — identical to base.
- `check_province_core.py --rev` (`province-core-landing.txt`, `province-core-base-clone.txt`): `province core rows 0 of 2`, rc 1 at base and at landing; its BASE pin `a5f7459` is stale and its Frontier check was already red at the freeze base. Not touched.
- `SKILL.md`: 600 lines / 92,672 B, unchanged (`base-skill-size.txt`).
- `check_freeze_gate.py --plan plans/round-91-controls.md`: `REFUSED control ctl-c2-capline-only` at landing (see § Work performed; not repaired).

## Sources & frontier

- **SOURCES rows before → after:** 187 → 190 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; census validate rc 0 at both points).
- **Rows added by tier:** A: 2 (S262 PIT "Basic concepts", S263 Python `subprocess`, both `mined`); B: 0; C: 1 (S264 Wikipedia "Mutation testing", `rejected`, with its flip condition in the row).
- **Rows touched old → new:** none. `git diff 9af1a7af c6631ca -- corpus/SOURCES.md | grep -c '^-[^-]'` → 0 (append-only); the frozen contract's append-only rule holds for this range.
- **Frontier rows advanced:** none in `corpus/README.md` § Frontier, which this round did not edit (§ Frontier is pinned by `check_province_core`; the frontier moved into two knowledge entries instead: the mutation-testing equivalent-mutant notion and the subprocess kill-and-wait contract).
- **Assimilation:** none. The `merge/kotoba/` package stays unadopted (L0 `kotoba | round-88` open; the id-collision census of the registry is recorded in the round-90 closure).
- **Considerthese:** no proposal implemented. Proposal 3 (description self-audit) carried; it needs a SKILL.md description rewrite that the 600-line ceiling cannot absorb (`base-skill-size.txt`).
- **Lane registry rows touched by this round's corpus:** knowledge entries cite S262 and S263; `used-by` lists are exactly the citing files.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries (`corpus/knowledge/mutation-battery-arms-round91.md` citing S262; `corpus/knowledge/timeout-calibration-round91.md` citing S263), each `source:` citing a `mined` row, on the battery guard surface and the subprocess-timeout contract, neither of which the lane held as knowledge before. Bound: S262 overlaps S260's killed/survived vocabulary; its scope cell says so.
- **quality: improved.** Corpus `unindexed` 1 → 0; the tip battery's `instrument-pin` guard FAIL → PASS (guards 4 of 5 → 5 of 5); freeze-gate exit-ladder defect repaired on its re-derived instance (self-test 30 → 31, able-to-fail shown); D5 v3 instance drift 4 → 3; no admitted entry failing its recheck (the recheck commands are in each entry's `recheck:` line).
- **discernment: unchanged.** The Gate admits S262 and S263 and rejects S264, but the non-author spot-check is pending (`corpus/lessons/round-91.md` § Gate). The pre-data control `ctl-c2-capline-only` did not refuse the shortcut it names; that is a gate miss, recorded as a Mistake with a routed fix, not a verdict on discernment. No non-author verdict is on record this round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` 600 lines / 92,672 B, unchanged this round (`.ufo/waves/round-91/receipts/base-skill-size.txt`; `.ufo/waves/round-91/receipts/landing/gate-registry-landing.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the landing run of the round's instruments at `c6631ca` (predicate, self-tests, bare floors walk, tip battery, controls) logged in `LOG.md` § Round 91 with receipts in `.ufo/waves/round-91/receipts/landing/`.
- [~] Instructions executable by an agent without oral context — evidence: `verifiers/check_mutation_battery.py --rev c6631ca…` ran cold from the committed tree and printed the predicate line (`.ufo/waves/round-91/receipts/landing/c1-predicate-landing.txt`); the knowledge entries carry `recheck:` commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` § Core gains the battery line; the sibling census stays red as before (`province rows 20 matched 4`, `.ufo/waves/round-91/receipts/landing/sibling-census-landing.txt`). Not `[x]`: the box needs a non-author verifier.

## Dead seats and round shape

- **Round shape:** one v1 wave `r91-w1`, 13 seats (band 8–16). Attack seats (reviewer, critic, mutation-tester): 4 of 13 landed (31 %, ≥ 25 %). Connector 1 (≤ 2). Planner excluded by the validator; the L1 holds the § 3 planner seat (standing deviation). Residual calls: none. Second wave: none (the wave's attack items were all in wave 1). Round total: 13 seats.
- **Dead or unlanded seats:** `ReviewerRepairs` (reviewer). No output file or directory under `.ufo/waves/round-91/w1/`; the registry row has `agentId: null`; no last error text is available to report.
- **Attempt-1 L1 (`KotobaR91`):** ended without a landed report (watchdog `lane-dead-no-report kotoba round=91`, 2026-11-05T13:34:09-03:00). Its wave registry was never settled.

## Open items

- **WAVE-DONE for `r91-w1` not received by this attempt.** The ready file names `KotobaR91` (attempt 1) as `l1`, so the handoff addressed the dead attempt. `swarm-registry.json` has no agent ids and no `r91-w1-results.json` exists. Requested: the orchestrator settle `r91-w1` from its seat outputs, or confirm none is due. I did not re-dispatch (taken ready file; double-spawn risk).
- **Fleet-root L0 not appended.** `.ufo/l0-questions.md` has uncommitted lines from other writers; committing it would sweep their lines under this lane's identity. The open question above is recorded here instead.
- **Frozen controls defective (routed, round 92):** `ctl-c2-capline-only` reads MET on the cap-only world; `ctl-c1-manifest-only` never reads its appended rows (addendum A5).
- **Leg B identity:** whether the re-derived non-UTF-8 rung is the routed round-90 pointer is a judgement left open (addendum A3).
- **Bounds:** battery `m6` (self-test blind to a dropped kill row; only the exact predicate line catches it); unrepaired ladder findings `--work` under a regular file (`NotADirectoryError`), duplicate control names read as held, declared `exit 127` never compared.
- **Carried, unchanged:** L0 `kotoba | round-88` (assimilation renumber-or-retire), `kotoba | round-73` (gate-registry home), `kotoba | round-50` (sibling precedence).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time: ` M .scratch/run15-state.json`, ` M .ufo/l0-questions.md`, `?? .ufo/closure-kaidoku-r92.json`. None is a kotoba seat's file (orchestrator-owned, another writer's L0 lines, another lane's closure); nothing was copied or deleted. The wave's seats wrote into the lane (`w1/`), with no fleet-root misroot.

## Tooling

No installs, upgrades or host changes. No pacman, sysctl or `/proc/sys` write. Scratch used under `/fast/scratch/hyaku/kotoba-r91/L1` and removed at the end of the round.

## Verdict basis

Claims are proposed as: C1 measured (predicate met on committed evidence at `c6631ca`); C2 measured on legs A and B, with leg B's identity with the routed pointer open. No axis value is changed by this report; the non-author closure rules verdicts and axis scores.

## Erratum — wave settlement (appended 2026-11-05 after first filing)

The sections **Dead seats and round shape** and **Open items** above state that no
`r91-w1-results.json` existed and that no WAVE-DONE was received. Both statements are superseded:
after this report was filed, the orchestrator delivered `WAVE-DONE kotoba r91 r91-w1` and wrote
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-91/r91-w1-results.json`
(13 records with keys `name`, `agent`, `output`, `note`; no per-seat status field). Twelve records
carry full seat outputs. The `ReviewerRepairs` record reads
`output unavailable: FileNotFoundError('Output not found: ReviewerRepairs-6')` — the harness holds
no output object for that seat, which confirms the dead-seat disposition and supplies the last
error text this report said was unavailable. No seat wrote into the wave dir after the report's
misroot sweep. No claim reading, measurement, verdict or axis value changes; this erratum
supersedes only the two statements named above and the "no last error text" clause of
§ Dead seats. The results file is committed as wave evidence in lane commit C (named in LOG.md
§ Round 91, "Wave settlement").
