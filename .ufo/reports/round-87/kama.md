# kama — round 87 report (attempt 1)
Lane HEAD at report time: `95ad1dbb2cfd0fee99b9f0cd7238755dbf5ff546` (= `origin/master`, `git ls-remote` verified).
Freeze commit `94e8fe7b911a5e6f8d1e1a07bff110d3ff6cb659`. Base `362b0d4a241520c9bc79b204c042d9fcefbb06ea`.
Plan `plans/round-87-claims.md` (with amendment A1). Lesson `corpus/lessons/round-87.md`.
Fresh-start round (operator run-15 amendment 27); the three last rejected closures (rounds 84, 85, 86, all
`rejected-honest-stop`) were read before any declaration.
Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tools installed or upgraded: none (no L1 install; seat reports record none).

## Work performed

Declared claims (2, both frozen before any measurement; distinct axes):

- **C1 — calibration (lowest assigned axis, 7): the rendered-cell selector repaired and the live self-assessment
  cell made true.** Outcome: **honest stop, not admitted.** The successor candidate passes the frozen probe battery
  but changes the gate coupling and population, which the frozen population rule R4 forbids.
- **C2 — operability (8): the round-86 instrument trio composed as pre-report-gate arm 14 `round86-instruments`,
  with a fault harness.** Outcome: **verified on its frozen predicates.**

Work items (evidence pointers):

- Protocol load (read): MISSION.md, AXES.md, SCORECARD.md (§Axes, §Planned, §Capabilities), SHONEN.md, `shokunin.conf`, plans/round-86-claims.md, the round-84/85/86 closures (`corpus/lessons/round-86-verifier-spotcheck.md:76` verdict `rejected-honest-stop`), `skill://swarm`, the round-86 wave spec and dispatch shape, and the prompt sections 1–7. Not re-read this round: PROTOCOL.md, LEARNING.md, CORPUS.md, corpus/QUALITY.md (the frontier step followed the prompt's §2b text).
- Do-nothing controls executed before freeze (committed in `94e8fe7b`): `.ufo/waves/round-87/controls/c1-live-before.out`
  (`RENDERED_CELLS facts=3 mismatches=2 …`, exit 1); `controls/c1-probes-before.out` (`C1_PROBES probes=3 escapes=3
  control=red`, exit 1); `controls/c2-gate-before.out` (`PRE_REPORT round=87 arms=13 failed=4`; `round86-instruments`
  count 0). Probe battery `controls/c1-probes.py` (P-A list-marker closer, P-B first-word disposition, P-C second revision).
- Round-86 R86V1 resolved: its three untracked lane-authored files committed in `94e8fe7b` (not rewritten).
- Wave 1 (one v1 wave, 12 seats; `w1-spec.json`, `w1-dispatch.json`, `w1.ready` → `w1.ready.dispatched`,
  `w1-results.json`; WAVE-DONE `w1` received). Seat reports: `.ufo/waves/round-87/w1/<Seat>.md`; evidence `w1/out/<Seat>/`.
  - EX01SelectorRepair (executor, C1): successor candidate `w1/out/EX01SelectorRepair/round87-rendered-cells.py`,
    `selector.diff`; its gate-coupling and population docstring rewrite is at `selector.diff` hunks `gate_fact`/`Population`.
  - EX02GateArmWire (executor, C2): `w1/out/EX02GateArmWire/pre-report-gate.py`, `gate.diff` (arm 14 in the round-83 pattern).
  - EX03FaultHarness (executor, C2): `w1/out/EX03FaultHarness/round87-gate-arm-faults.py`, `test-arm-present.out`, `test-arm-absent.out`.
  - MT01SelectorBattery (mutation-tester, C1): `w1/out/MT01SelectorBattery/battery.py`; on round-86 selector
    `battery-run-round86.out`: `SELECTOR_MUTANTS mutants=9 killed=3 escaped=6` (escapes M1, M2, M5, M6, M7; M9 cne).
  - MT02GateArmBattery (mutation-tester, C2): `w1/out/MT02GateArmBattery/battery.py`; on master gate
    `master-run.stdout.txt`: `GATE_ARM_MUTANTS mutants=7 killed=0 escaped=7`; on a synthetic correct arm
    `synth-selftest.stdout.txt`: `7/7`. Integrated-gate run: see Limits.
  - RV01PlanFreezeReview (reviewer): verdict `ok` with two fixes (R1 arm-delta in the counting command; R2 population diff); R2's "§4.6" citation refuted by `w1/out/SC01SourceOpen/fetched-4.5.txt:4`. Both fixes landed as plan amendment A1.
  - CR01NoWorkShortcuts (critic): `w1/out/CR01NoWorkShortcuts/receipts/`: a hard-coded literal selector passes predicates 1–2 as written (residual, disclosed; routed to round 88).
  - SC01SourceOpen (scout): `w1/out/SC01SourceOpen/quotes.md`: S580 (CommonMark 0.31.2 §5.2) and S578 re-open (§4.5).
  - SC02ConsiderTheseMine (scout): `w1/out/SC02ConsiderTheseMine/mine.md`: `considerthese/2026-10-26.md` proposal 2 → KQ141 (lesson item).
  - SC03MistakeSweep (scout): `w1/out/SC03MistakeSweep/sweep.md`: fleet-root sweep (below), R86V1 captured-by analysis.
  - SB01LessonDraft (scribe): `w1/out/SB01LessonDraft/lesson-round-87.md` (integrated and extended as `corpus/lessons/round-87.md`).
  - CN01OverlapScan (connector): `w1/out/CN01OverlapScan/overlap.md`: no name collision; no sibling duplicate of C1/C2.
- Integration (L1 only committer): `tools/pre-report-gate.py` ← EX02 candidate; `tools/round87-gate-arm-faults.py` ← EX03;
  `tools/round87-rendered-cells.py` **not** placed in `tools/` (candidate kept as wave evidence, claim not admitted).
  SCORECARD calibration row corrected to the round-86 closure's observed disposition (numeric score unchanged); its
  pre-round text kept as history below it (append-only), see Limits.
- Plan amendment A1 (pre-data, before the L1's successor measurement; committed in `24d1895d`): R5 (all revisions),
  R1/R4 citation check, C2 harm-rule arm delta.

## Landed changes

| Commit | Change | LOG/SCORECARD link |
|---|---|---|
| `94e8fe7b` | freeze: plan, do-nothing controls, probe battery, R86V1 strays | LOG round 87 |
| `3ad2b9e6` | gate arm 14 `round86-instruments`, fault harness, lesson `corpus/lessons/round-87.md`, S580 row, SCORECARD planned round 88, capability `gate-round86-instruments` (first working 87), LOG entry | LOG round 87; SCORECARD §Capabilities |
| `c6b5cf3f`, `fe78ca4f` | calibration row corrected to the round-86 closure (first attempt used a capitalised pointer; the selfdesc/newest-closure arms fixed it); round-85 history row restored byte-for-byte below it | SCORECARD §Axes row 18–19 |
| `24d1895d` | measured receipts (`measured/`) and plan amendment A1 | LOG round 87 |
| `a5f0ede9` | MT02 battery receipt on the integrated gate | — |
| `95ad1dbb` | wave-1 settlement record and MT02 seat report | — |

## Before → after measurements

**C1 (calibration).** Counting commands (exit codes in brackets).
- Before (`362b0d4a`): `python3 tools/round86-rendered-cells.py --repo . --rev 362b0d4a…` → `RENDERED_CELLS facts=3 mismatches=2 gate=1 closure=0 disposition=0 newest_gate=86 newest_closure=86` [1]; probe battery `python3 .ufo/waves/round-87/controls/c1-probes.py tools/round86-rendered-cells.py` → `C1_PROBES probes=3 escapes=3 control=red` [1]. Receipts `controls/c1-live-before.out`, `controls/c1-probes-before.out`.
- After (`fe78ca4f`, receipts `measured/`):
  - successor live predicate: `python3 .ufo/waves/round-87/w1/out/EX01SelectorRepair/round87-rendered-cells.py --repo . --rev fe78ca4f…` → `RENDERED_CELLS facts=3 mismatches=0 gate=1 closure=1 disposition=1 newest_gate=86 newest_closure=86` [0] (`measured/c1-successor-tip.out`).
  - successor probe predicate: `C1_PROBES probes=3 escapes=0 control=red` [0] (`measured/c1-probes-successor-tip.out`).
  - population predicate (A1 R4): `diff` of the `Population` block against round 86 → 17 lines (`measured/c1-r4-population-diff.out`). **Non-empty: the population changed.**
  - round-86 counter at tip: `mismatches=1` [1] (`measured/c1-round86-counter-tip.out`): its disposition oracle still reads `rejected-harmed` from the closure body (P-B, unrepaired in the frozen counter).
- Verdict: successor predicates 1 and 2 hold; the population predicate fails; **C1 not admitted (honest stop).** Axis score unchanged (7).

**C2 (operability).**
- Before (`362b0d4a`): `PRE_REPORT round=87 arms=13 failed=4 uncommitted=0`; `round86-instruments` count 0 (`controls/c2-gate-before.out`).
- After: `PRE_REPORT_ARM round86-instruments exit=0 ok RENDERED_CELLS_SELFTEST pass=17 fail=0 | DEBT_MUTANT_OWNERS_SELFTEST pass=13 fail=0 | PIN_ORIGIN_SELFTEST …` and `PRE_REPORT round=87 arms=14` (`measured/gate-tip.out`, measured at `fe78ca4f`) [1 overall; see below].
- Fault predicate: `python3 tools/round87-gate-arm-faults.py --repo . --work <scratch>` → `ARM14_FAULTS faults=3 killed=3 escaped=0` [0] (`c2-faults.out`); arm-absent control `CONTROL_RED`, `killed=0 escaped=3` [1] (`w1/out/EX03FaultHarness/test-arm-absent.out`).
- Harm rule (base-ok arms still ok): `comm` of `PRE_REPORT_ARM … exit=0 ok` names, base vs `measured/gate-tip.out` → `round-clean` only (`measured/c2-harm-base-ok-now-red.out`). That red was transient: the round-87 measured receipts were uncommitted when measured; they are committed in `24d1895d`, and `round-clean` only reads the round-87 wave directory.
- Verdict: **C2 verified on its frozen predicates** (arm present and ok, `arms=14`, `3/3` seeded faults killed, control red without the arm).

Full-gate verdict at `fe78ca4f` (the gate is a conformance probe, not the claim): `failed=4`: `selfdesc` (see Limits), `round75-instruments` (APPEND_DEBT, see Limits), `round-scope` and `round-clean` (measured-time receipts, transient; now committed). Base had `failed=4`.

## Sources & frontier

- `corpus/SOURCES.md` before (round start, `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`): exit 0; `census --file corpus/SOURCES.md`: rows 319, tier A 304 / B 11 / C 4, mined 286, queued 8, rejected 25, invalid 0, missing 0.
- After (`95ad1dbb`): `validate` exit 0; rows 320, tier A 305 / B 11 / C 4, mined 287, queued 8, rejected 25, invalid 0, missing 0.
- Rows added by tier: A +1 (S580, CommonMark 0.31.2 §5.2 list items, status mined, opened 2026-11-05, `used-by corpus/lessons/round-87.md`, quote "A list item may contain any kind of block:", verbatim-checked `quotes.md`).
- Rows touched old→new: none. S578 re-opened this round (§4.5 quote still matches live page, SC01 freshness check); its row is unchanged and the re-open is recorded in the lesson `## Gate`.
- Frontier rows advanced: S580 (C1 rule R1, container rule for fence markers).
- Considerthese: `considerthese/2026-10-26.md` proposal 2 mined → KQ141 (lesson item, not implemented); the file's header line says "proposals only; I am not acting on any of them".
- Assimilation: none (`merge/kama/` not adopted this round).

## Trend verdicts

- **expansion: unchanged** — one source row and one capability (`gate-round86-instruments`) entered; no new knowledge entry; the capability is demonstrated by `ARM14_FAULTS faults=3 killed=3 escaped=0`.
- **quality: improved** — the gate now runs the round-86 instrument selftests fail-closed (arm 14, 3/3 seeded faults killed), and the lane's own calibration cell matches the newest closure's disposition (round-86 `rejected-honest-stop`) instead of round 85.
- **discernment: unchanged** — the reviewer and critic seats falsified the plan's citations and found shortcuts, but no non-author judgment on an admitted claim exists this round; C1 is not admitted, and no exploratory claim was declared.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → author assertion: `SKILL.md`; unchanged this round; no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → author assertion: `LOG.md` round 1–3 and round 16–17; this round's gate arm runs are instrument receipts, not a new domain task.
- [~] Instructions executable by an agent without oral context → author assertion: `SKILL.md` §Checklist; unchanged.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → author assertion: `PROVINCE.md`; CN01 (`w1/out/CN01OverlapScan/overlap.md`) found no sibling overlap.

## Limits and open items

- **C1 honest stop.** The successor's population changes (R4 diff 17 lines). R5 (all-revisions) is part of A1, but the candidate does not implement it; the candidate is kept as evidence, not in `tools/`. Round 88 must freeze a population-preserving rule before data.
- **Residual, C1:** CR01 showed a selector hard-coding the three fixture texts satisfies predicates 1–2 as written. Routed to round 88 as an unseen probe family frozen before the first scored candidate.
- **Battery defect (MT02, integrated gate).** `measured/mt02-battery-integrated-gate.out` prints `GATE_ARM_MUTANTS mutants=7 killed=7 escaped=0`, but its own pristine self-check reports `not-ok` on the default tools copy (the battery's scratch tools were contaminated by fault stubs in that run). The 7/7 is **not** accepted as kill evidence; C2's admission rests on the harness predicate above. Routed to round 88.
- **`selfdesc` red (structural).** The arm reads every `| calibration |` row of SCORECARD §Axes; the round-85 history row kept beneath the corrected row (kept to avoid an append-only deletion event) keeps it red. L0 question appended.
- **`round75-instruments` red (APPEND_DEBT).** At `fe78ca4f`: `round=87 base=362b0d4a2415 events=90 accepted=53 late=26 pending=0 unaccepted=11 bad_rows=19`. The arm could not evaluate at base (no round-87 plan), so this red surfaces now; cause not yet investigated. L0 question appended.
- **R86V1 residue:** round-86 w3 seat reports `EX02GateCensus.md` and `CN01OverlapScan.md` were never written to disk (recorded, not reconstructed; `sweep.md`).
- **Seat answering models:** the wave results do not record the answering model per seat; routes are `task.agentModelOverrides` as configured. No seat's claim depends on a specific model.

## Round shape and seats

- Shape: ONE v1 wave, `w1`, 12 seats (policy `ufo-wave-policy.json`, band 8–16). Roles: executor 3, scout 3, mutation-tester 2, reviewer 1, critic 1, scribe 1, connector 1. Attack seats (mutation-tester, reviewer, critic) 4 of 12 = 33 %; connector 1 of 2 max. The L1 holds the planner seat (validator rejects planner).
- Residual call: none. Second wave: none.
- Dead seats: none (12 of 12 wrote output and a report; `w1-results.json`).
- Round total: 12 seats.
- Misroot sweep (before this report): `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `M .scratch/run15-state.json` (orchestrator-owned; not touched). No kama seat file at the fleet root. Recorded in `w1/out/SC03MistakeSweep/sweep.md`.
- Scratch: `/fast/scratch/hyaku/kama-r87/` removed after landing.

## Mistakes (lesson `corpus/lessons/round-87.md` `## Mistakes`)

- M1 R86V1 — round-86 leftovers untracked (captured-by: none; fixed `94e8fe7b`).
- M2 R86V2 — C1 false greens (captured-by: none in round 86; fix: frozen probe battery).
- M3 successor passes its own probes while changing the frozen population (captured-by: the R4 rule; no arm yet).
- M4 calibration cell stale at round start (captured-by: `selfdesc`/`newest-closure` arms, only when run).

## L0 questions appended

- kama | round-87 | APPEND_DEBT (`round75-instruments`) red at lane tip — operator ruling and round-88 investigation.
- kama | round-87 | `selfdesc` reads every `| calibration |` row — ruling between option A and option B.

## Verification gate

- Lane pushed: `git -C /home/vgpnk/Projects/shokunin/kama-shokunin ls-remote origin refs/heads/master` → `95ad1dbb2cfd0fee99b9f0cd7238755dbf5ff546`.
- Round end census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0.
- `## SHONEN` count: 1 (see above).
