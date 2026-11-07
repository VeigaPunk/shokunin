# tabi — round 75 report

L1 `TabiR75`, attempt 1 (`.ufo/watchdog.log`: `launch tabi round=75 … attempt=1`, no earlier attempt; nothing
inherited). Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, base `c19a520fdfa574a5c082b09130b7dbfcdd1e99eb`,
final lane hash **`a92837d05dde6ea5a5cc9053c5bb83599c84f62f`** (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims: **one** — **C1, coverage (capability acquisition) `chromium-drag-intercept-linux`**: CDP
`Input.setInterceptDrags` + `Input.dispatchDragEvent` + the `Input.dragIntercepted` event on Chromium
155.0.8059.84 headless, frozen predicate `C1-DRAGINTERCEPT-R75` (`.ufo/waves/round-75/claims.json`). All six axes
stood at 9; C1 works a lowest axis. Sourced claim: S196–S200, opened this round. **Verdict: verified on the
frozen predicate (legs a–d hold)**, with two frozen non-predicate sentences corrected on record (see SCORECARD
`## Round 75`).

- Fresh-start reading: the r72–r74 non-author spot-checks were read before the claim; the four r74 routed
  defects were applied to this generation's instruments or carried with reasons (`corpus/lessons/round-75.md:9-33`).
- Surface probe (raw CDP, no lane script): interception replaces the native drag session; a dispatched drop is
  dragover-then-drop; `dragCancel` fires nothing; `dragLeave` refused (scratch probe; findings carried into the
  driver legs and the note).
- Instruments (pre-freeze commit `d71951a7`): driver `scripts/chrome-cdp-dragdrop-round75.mjs` (15 legs, CDP event
  capture, 3 degenerate producers), counter `scripts/check-dragdrop-r75.mjs` (146 checks; event-multiset and
  ≥ 50 ms gap-multiset replay test; `priorSet` in its output; 8 sourced laws), battery
  `scripts/negatives-dragdrop-r75.mjs` (254 cases; requires its 3 laundered receipts), kill power
  `.ufo/waves/round-75/controls/c1/kill-power-r75.mjs` (146 force-true + 40 semantic; crash ≠ kill), selftest
  `scripts/selftest-r75-gates.mjs`.
- Pre-freeze evidence: 4 probes + 9 cold smokes + 3 degenerates; `controls/c1/prefreeze-summary.json` allOk 9/9
  (counter clean 146, battery 254/254, kill power holds, 0 crashed, on every smoke); `controls/c1/controls-summary.json`
  allOk (do-nothing, replay, whole-shift 0.1 ms / 100 ms — the r74 declared limit, now refused — probe relabel,
  degenerates, limit witness); honest-pair replay margin `lesson-proof/timeline-honest-pairs.json` (156 pairs,
  0 refused).
- Freeze `b1ddabc5` (claims + prior-set enumeration at the freeze parent), digests commit D `57f28cf1`
  (`freeze.txt`, 7 digests), scored run `8204c176` (`run-scored.sh`: driver 0, counter 0, battery 0, kill power 0).
- Wave w1 (dispatch `061b10d0`; results `.ufo/waves/round-75/w1-results.json`): leg (b) by R75Exec1 (counter exit 0
  clean 146, 17 priors, `w1/R75Exec1/counter.json`); legs (c) re-run independently (254/254 ×2, kill power holds).
- Integration `a92837d0`: capability row, note corrections, S201, QUALITY 141–142, SKILL `## Round 75 gate registry`,
  selftest `scored/selftest-r75-gates.out` (`clean=true cases=12`, exit 0), lesson, LOG, README coverage row.
- Round shape: ONE v1 wave of **11 seats** (policy `ufo-wave-policy.json`, band 8–16), no residual call; round
  total **11**. Role mix: executor 2, reviewer 3, critic 1, mutation-tester 1, scout 1, connector 1, scribe 1,
  revenger 1; attack seats 5/11 (45 %). Planner seat = the L1 (validator refuses `planner`). Dead seats: **0**
  (all 11 settled; 11 report files under `w1/`: 3 HOLDS, 1 CONFIRMED, 7 FINDINGS). Seat routes: per
  `task.agentModelOverrides` at spawn (not passed by the L1).

## Landed changes

| Commit (lane, `jj-lane.sh` `landed`) | What | LOG |
|---|---|---|
| `d71951a78f5fa1a6672359c815e85a7f297bc8db` | pre-freeze instruments, probes, smokes, degenerates, controls, prefreeze 9/9, S196–S200, note, lesson draft | `LOG.md` `## Round 75` bullets 2–4 |
| `b1ddabc5f3eda9fa4c780c41c51a574ae1edf4d8` | FREEZE `claims.json` + prior-set enumeration (raw 25 / top-level 16) | bullet 4 |
| `57f28cf128e69dc40604f3201eab6a843c8e4142` | digests commit D (`freeze.txt`) | bullet 4 |
| `8204c1762192d23529ebe1df5d7577e2d351f979` | scored run, leg (a)/(c) outputs, scored receipt | bullet 5 |
| `061b10d08b3e295dffdf5624e9422082bf7a99e8` | wave w1 spec and validated dispatch (11 seats) | bullet 7 |
| `a92837d05dde6ea5a5cc9053c5bb83599c84f62f` | wave evidence, capability row, SCORECARD correction, S201, QUALITY 141–142, registry, selftest, lesson, LOG, README | bullets 5–7 |

## Before → after measurements

- **C1** (base `c19a520f` → lane tip `a92837d0`; scored receipt landed at `8204c176`, measured against frozen pins in
  `57f28cf1:.ufo/waves/round-75/freeze.txt`).
  - Counting command: `node scripts/check-dragdrop-r75.mjs --receipt corpus/evidence/round75/chromium-drag-intercept/receipt.json --expect-driver-sha256 d604552e408ed6998f32ead68e9732ba87b2ecfd7483d671ca95f63cf3228105 --expect-nonce tabi-r75-l1-57f28cf128e6 <16 --prior, one per line of .ufo/waves/round-75/controls/c1/prior-set.txt> --json`
    — before: no receipt → exit 2 `receipt-unreadable`; the r74 IME receipt → exit 1 (`schema`, `nonce-shape`,
    `nonce-expected`, `driver-pin`, `drag-call-count`, `intercept-event`, …) (`controls/c1/controls-summary.json`);
    after: exit 0, `clean`, 146 checks, 16 priors (`scored/c1-counter-a.json`).
  - Leg (b): R75Exec1 counter exit 0 clean 146, 17 priors (`w1/R75Exec1/counter.json`).
  - Leg (c): battery exit 0, 254/254, allOk (`scored/c1-negatives-a.json`); kill power exit 0, holds, 146/146 +
    40/40, crashed [] (`scored/c1-kill-power-a.json`).
  - Leg (d): `git show <rev>:SCORECARD.md | grep -c '^| \`chromium-drag-intercept-linux\` |'` → 0 → 1;
    `git grep -lE 'dispatchDragEvent|setInterceptDrags' <rev> -- corpus/knowledge | wc -l` → 0 → 1; the note's
    `source:` line cites S196–S200.
  - Do-nothing control beaten: the cheapest no-work inputs (no receipt, the newest committed capability receipt,
    a byte-identical or relabelled PRE replay, a whole-timeline shift) all fail as declared (`controls-summary.json`
    allOk, committed in the pre-freeze commit).

## Sources & frontier

- Census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
  start exit **0**, 195 rows, 27 W04 (`.ufo/waves/round-75/census/start.txt`); end exit **0**, 201 rows, 29 W04
  (`census/end.txt`). Row count command: `grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md` → 195 → 201.
- Rows added by tier: **6 × tier A** (`code`): S196–S200 before the freeze (Input.pdl drag scope, input_handler.cc
  drag scope, web_frame_widget_impl.cc, drag_controller.cc, data_transfer.cc), S201 after (event_handler.cc,
  located by R75Scout, re-opened by the L1). Each has a ≤25-word located quote in `corpus/lessons/round-75.md`
  `## Gate` / `## Sources — opened after the freeze`.
- Rows touched old→new: none of the earlier rows; in-round anchor corrections on this round's own rows S196
  (`53-91` → `53-94`) and S197 (`1578-1624` → `1578-1619`), logged in the lesson.
- Frontier advanced: the note's open mechanism (why `drag@src` precedes some dragovers) moved from measured-only to
  sourced (S201). New frontier: file/link/HTML items, modifiers.
- Sourced claim: C1 rests on S196–S200 (claims.json `sourced`; note `source:` line).
- Mined mistakes: 5 rows in `corpus/lessons/round-75.md` `## Mistakes` (control expectation from belief; a
  battery case rounded back onto the honest grid + three unexercised conjuncts; a replay threshold chosen before
  the honest distribution; QUALITY 140's literal grep over-matching counter outputs; r74 F4/F5 misfiled) —
  QUALITY 141–142.
- Assimilation: none (`merge/tabi/` adoption stays closed pending L0 `tabi | round-57`). `considerthese/`: no
  such directory in this lane.

## Trend verdicts

- **expansion: improved.** Capability `chromium-drag-intercept-linux` admitted to the table (row 0 → 1);
  knowledge 87 → 88 on ground the coverage map did not hold (`git ls-tree -r --name-only <rev> corpus/knowledge | wc -l`);
  registry 195 → 201.
- **quality: improved, contested in part.** The r74 declared limit (whole-quantum timeline shift) is refused by
  the new generation (control `replay-forged-whole-shift-0.1ms`), the prior set is enumerated against the
  repository, and kill power no longer scores a crashed battery as a kill. Against that: R75Critic shows the frozen
  limit sentence is imprecise (0.1 ms grid, 9 of 17 events, battery/kill power also receipt readers) and
  R75Revenger shows r74 F4/F5 open and misfiled in the frozen `priorRound` sentence; both are corrected on record,
  not deleted. Closure to rule.
- **discernment: improved.** Five mistakes mined with fail-able proofs (QUALITY 141–142); the Gate carries one
  admit and three rejects for spot-check; attack-seat findings are routed, not argued away.
- Per-axis: coverage improved (C1). Calibration: no claim; **contested** — the L1 reads it unchanged (both false
  or imprecise sentences are marked in SCORECARD, lesson and note in-round), R75Revenger counted 2 self-assessment
  mismatches before correction. Depth, freshness, operability, adjacency unchanged (R75Connector: overlap none,
  verdict adjacent).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Pointer: `SKILL.md`
  `## Round 75 gate registry`, plus prior pointers in `SHONEN.md:5-6`. R75Revenger checked the pointers resolve
  (6/6); a lane seat is not a non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md: `LOG.md` `## Round 75` (drag interception,
  4 probes + 9 smokes + 1 scored + 1 + 3 cold seat runs).
- [~] Instructions executable by an agent without oral context: R75Exec1/R75Exec2 ran the driver, counter and
  battery from the spec alone (`w1/R75Exec1/report.md`, `w1/R75Exec2/report.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate): `PROVINCE.md` untouched; R75Connector overlap none
  (`w1/R75Connector/report.md`).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (RULES.md read; pacman untouched). No seat reported an install.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → untracked `trail-ids.txt` (Nov 6 20:36,
before this round's launch; not a tabi r75 file) and `.scratch/` (orchestrator-owned); no misroot from this round.
Open L0 questions: none new; `tabi | round-57` (register correction) stays open.
