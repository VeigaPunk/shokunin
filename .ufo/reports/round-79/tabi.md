# tabi — round 79

Lane repo `/home/vgpnk/Projects/shokunin/tabi-shokunin`; base `24c821895f31f9dcb66ac2f357bc947818b0408c`
(lane clean, `local=remote`, `ahead=0 behind=0`). Round 78 was admitted; its routed defects 1–6 are
this round's spine. **Declared claims (2):** **C1** coverage (9) — capability acquisition
`chromium-showpicker-linux` (the programmatic picker trigger path and its gesture law); **C2**
calibration (9) — record drift, the round-78 spot-check's routed defect 1/2/6, counted by a committed
instrument. Both frozen in `.ufo/waves/round-79/claims.json` before any post-D run; instrument digests
in `.ufo/waves/round-79/freeze.txt`, final digests commit **D = `f154beeff14e349b84fa0d236461132295b7c017`**
(two earlier D commits, `8e966a40` and `80830674`/`3a1209c0`, were superseded by wave findings before
the final scored run; every superseded run is named below and none is cited as evidence).

## Work performed

- **C1 — capability `chromium-showpicker-linux` (new).** Driver
  `scripts/chrome-cdp-showpicker-round79.mjs` (10 legs, one fresh browser per leg, because
  `navigator.userActivation.hasBeenActive` is per-window state), counter
  `scripts/check-showpicker-r79.mjs` (56 checks), battery `scripts/negatives-showpicker-r79.mjs`
  (90 cases), `scripts/kill-power-r79.mjs` (64 semantic mutants), `scripts/selftest-r79-gates.mjs`
  (9 gates), and four honest pre-freeze receipts under `.ufo/waves/round-79/controls/c1/probes/`.
  Evidence: `corpus/evidence/round79/chromium-showpicker/receipt.json` (nonce
  `tabi-r79-l1-f154beeff14e`), `.ufo/waves/round-79/scored/c1-counter-a.json` (clean, 56/56),
  `c1-negatives-a.json` (90/90, `coverage.uncovered []`, `coverage.unknown []`),
  `c1-killpower-a.json` (64/64 killed, 0 survivors, 0 crashed), `selftest-r79-gates.out` (9/9).
- **C2 — record drift.** `scripts/check-record-drift-r79.mjs` (20 record claims over the r78
  SCORECARD row, SKILL registry, LOG entry, filed report, `claims.json` leg (b) path and the
  `nodeReport` sentence; each checked for *stale-present* + a **directional** correction pair
  `<stale> → <truth>` + truth re-derived from the committed bytes). Before
  `lesson-proof/c2-before.json` (exit 1, 7 mismatches), after `lesson-proof/c2-after.json` (exit 0,
  0 mismatches); controls `lesson-proof/c2-controls.json` (reversed → 2 mismatches; stale removed →
  2; truth moved → 1).
- **Frontier step.** `corpus/SOURCES.md` 215 → 218 rows (S216 WHATWG `showPicker()` steps, S217 MDN
  `showPicker()`, S218 Chromium 155 `html_input_element.cc`), all opened 2026-11-07 with located
  quotes in the lesson's Gate; census start exit 0 (215), end exit 0 (218). Four mistakes mined in
  the lesson's `## Mistakes`, each with its red state under `lesson-proof/`.
- **Assimilation: none** (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
  `considerthese/`: no such directory in this lane.
- **Wave w1.** One v1 wave, **12 seats, all settled, none dead** (4 executor, 2 reviewer, 1 critic,
  1 mutation-tester, 1 scout, 1 scribe, 1 connector, 1 probe-executor); attack roles 4/12 = 33 %;
  the L1 holds the canonical planner seat and the `labrat` probe rides an executor seat (the
  validator rejects `planner` and `labrat` as swarm roles). Spec `w1-spec.json`, dispatch
  `w1-dispatch.json`, handoff `w1.ready`, results `w1-results.json`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Instruments, pre-freeze receipts and prior set, frozen claims and digests, knowledge note, lesson, S216–S218, QUALITY 155–156, README coverage, SCORECARD/SKILL/LOG with the round-78 corrections | round-79 bullets 1–3 | `8e966a40` (superseded D) |
| Digests commit D — the battery exempts the committed scored receipt by content; the driver stdout leaves the walked tree | round-79 bullet 1 | `80830674` (superseded D) |
| Scored evidence under that D | round-79 bullet 1 | `0e51e0c6` |
| Wave spec, validated dispatch, ready handoff | round-79 bullet 4 | `be533cb2` |
| Selftest 9/9 on the committed bytes | round-79 bullet 1 | `c7118747` |
| Digests commit D — a `--prior` receipt in a walked tree is a prior (wave finding F1) | round-79 bullet 1 | `3a1209c0` (superseded D) |
| Digests commit D (final) — C2 binds corrections directionally; the claims/SKILL/lesson statements corrected to the measured counts; PROVINCE carries the showPicker surface; the pre-freeze summary and C2 controls committed | round-79 bullets 2–3 | `f154beee` |
| Wave w1 results (12/12), the scored evidence under D (counter 56, battery 90/90, kill power 64/64, drift 0, selftest 9/9), and R79Exec4's routed-defect-3a battery `scripts/negatives-filechooser-r79.mjs` | round-79 bullet 4 | `4c3ae268` |
| Wave findings integrated: the note's source-order correction and the lesson's wave section | round-79 bullet 4 | `074bd9c5` |

## Before → after measurements

| Claim | Counting command | Before | After | Measured at |
|---|---|---|---|---|
| C1 coverage (9), `chromium-showpicker-linux` | `node scripts/check-showpicker-r79.mjs --lane <ABS lane> --receipt corpus/evidence/round79/chromium-showpicker/receipt.json --expect-driver-sha256 e9c87159e5d5212237437eb7a80a2d26fcd8086603dae1e37db64ce1aaf94933 --expect-nonce tabi-r79-l1-f154beeff14e --expect-fixture-sha256 69de1a78dc3ad40f7ce6e04896e22fe1729c0a789f01276f8f53e9e55b6393df --prior-set .ufo/waves/round-79/controls/c1/prior-set.txt --json` | base: no r79 receipt → exit 2 `receipt-unreadable`; the r78 file-chooser receipt under the r79 counter → exit 1, **52 findings** (`lesson-proof/c1-nowork.json`) | exit 0 `clean`, **56/56 checks**; battery **90/90**; kill power **64/64**, 0 survivors; selftest **9/9** | `f154beee` |
| C2 calibration (9), record drift | `node scripts/check-record-drift-r79.mjs --lane <ABS lane> --json` | exit 1, **7 mismatches** (`lesson-proof/c2-before.json`) | exit 0, **0 mismatches** (`lesson-proof/c2-after.json`); `check-capability-status.mjs --json` exit 0, `mismatches 0`, `provisional 1` | `f154beee` |

The C1 escape minimum is printed beside the threshold in the counter's `limit` block: per prior,
`escapeEvents = priorEvents - absNeed + 1` and `escapeGaps = priorGaps - gapNeed + 1` — for the four
37-event priors, **19 page-event times moved and 1 gap broken** (the wave's critic re-measured the
boundary and found it reachable at exactly that point). The counter's header sentence said "moves at
least `absNeed` events", which understates the boundary by one for a prior whose `absNeed` is not
`N_p - absNeed + 1`; the printed block is correct and the prose is corrected here (wave M1).

## Sources & frontier

- `corpus/SOURCES.md` rows: **215 → 218** — `grep -cE '^\| S[0-9]{3,}' corpus/SOURCES.md` (215 at
  base, 218 after). Added by tier: **A = 3** (S216 spec, S217 docs, S218 code), B = 0, C = 0. Rows
  touched old→new: none. Census start `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin tabi` **exit 0** (`.ufo/waves/round-79/census/start.txt`), end
  **exit 0** (`.ufo/waves/round-79/census/end.txt`), W04 duplicate-URL warnings only.
- Frontier rows advanced: `showPicker()` under interception (the r78 README's named frontier) is now
  core; the note's Frontier section names what stays open (webkitdirectory/accept inputs, the
  cross-origin `SecurityError`, the trigger-then-answer combination).
- Mined mistakes: 4 rows in `corpus/lessons/round-79.md` `## Mistakes`; QUALITY 155–156 added.
- Sourced claim: C1 rests on S216–S218, opened this round with located quotes in the lesson's Gate.
  The wave's scout re-fetched every source twice (byte-identical) and corrected one synthesis
  sentence in the note (the spec and Chromium transpose the first two checks); S219 does not exist —
  there is no `Runtime.pdl` at tag 155.0.8059.84, and the claim's "S216-S219" is corrected to
  "S216-S218".
- Assimilation: none (`merge/tabi/` closed pending the open L0 `tabi | round-57`); `considerthese/`
  absent in this lane.

## Trend verdicts

- **expansion — improved.** A new capability row (`chromium-showpicker-linux`, first-working round 79)
  and a new knowledge note on ground the coverage map did not hold (`corpus/README.md`
  `## Round 79 coverage`); registry 215 → 218, all three rows `mined` and cited by the note.
- **quality — improved, with a disclosed limit.** The r78 record drift is corrected on the record
  (7 → 0) and the new instrument's frozen kill power is complete (64/64, 0 survivors) after three
  rounds of fixing what the first runs exposed (30 → 3 → 1 → 0 survivors). The wave's independent
  mutation seat (R79Mut1, 76 conjunct-level mutants) then found **56 weakenings the battery does not
  kill**: the battery has one isolating case per *check*, and a multi-conjunct check is bracketed on
  one conjunct only. The counter holds the rule; the battery is blind to the other conjuncts. This is
  routed to r80 and is not claimed closed; no admitted corpus entry was found false and left unmarked.
- **discernment — improved.** The wave falsified the claim twice (the critic's reversed-correction
  control, the scout's source-order flag) and both became corrections with red states; the round's
  own controls caught four instrument defects before the freeze (the crash on a foreign receipt, the
  mirror-lane prior-set path, the walked `driver.out`, the `--prior` walk exclusion). The non-author
  spot-check of this round is the outside check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Round 79 gate registry with the entry command, verdict map, self-test and pinned path; the law table in `corpus/knowledge/chromium-showpicker-runtime-round-79.md` §"The law, as measured" cites S216–S218. No non-author verifier has checked this round's additions yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 10-leg runtime measurement and its counter, logged in `LOG.md` round-79 bullet 1.
- [~] Instructions executable by an agent without oral context — the driver/counter/battery entry commands are in `SKILL.md` §Round 79 gate registry and the note's `recheck:` line; the pre-freeze receipts reproduce from them.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` gains the showPicker surface and keeps the refusal routes; the wave's connector scanned 20 sibling lanes, 0 contested rows.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. This round's mission began
2026-11-07T17:25:37-03:00 (`.ufo/watchdog.log` `launch tabi round=79 pgid=558011`) and is
**progressing** (commits `8e966a40` … `074bd9c5`).

## Tool installs

None this round (no package, binary or tool was installed or upgraded; the round used the host's
`/usr/bin/chromium` 155.0.8059.84 and node v24.21.0).

## Wave w1 — results

12 seats, all settled, **none dead**. Results `.ufo/waves/round-79/w1-results.json`; per-seat reports
in `.ufo/waves/round-79/w1/<seat>.md` and evidence in `.ufo/waves/round-79-seats/<seat>/`.

| Seat | Role | Outcome |
|---|---|---|
| R79Exec1 | executor | Leg (b): cold1 + cold2, driver exit 0, 10/10 legs, **zero honest refusals**; both score clean 56/56. Its finding F1 (a `--prior` receipt in a walked tree was reported `prior-set-complete`) was **fixed at the instrument** (D `3a1209c0`, carried into `f154beee`) and re-verified by the seat. |
| R79Exec2 | executor | Two more cold runs plus a scratch path containing a space: all clean, no refusals. |
| R79Exec3 | executor | Frontier probe: showPicker on `webkitdirectory`/`accept` inputs and the double-call boundary (frontier evidence for r80, not a capability leg). |
| R79Exec4 | executor | Routed defect 3a: `scripts/negatives-filechooser-r79.mjs`, one witness per R78Mut1 survivor against the frozen r78 counter, r78 bytes untouched. |
| R79Review1 | reviewer | Forged receipts against the counter; the surviving forgeries are named with their construction. |
| R79Review2 | reviewer | Re-ran battery (90/90) and kill power (64/64); its F1/F2 (the 87-case claims drift and the absent control file) are **fixed** in D `f154beee`. |
| R79Critic | critic | H1 (C2 counted substrings — a reversed correction passed) **fixed** by the directional binding; H2–H5 (record drift, absent evidence) **fixed**; M1 (limit prose) corrected here; M2 (PROVINCE) **fixed**. C1's boundary confirmed and reachable at 19 events + 1 gap. |
| R79Mut1 | mutation-tester | 76 independent conjunct-level mutants: 56 survive the frozen battery (routed to r80), 17 subsumed, 1 unreachable, 2 inert. The counter holds the rule; the battery's coverage is per-check, not per-conjunct. |
| R79Scout | scout | Every source re-fetched twice, byte-identical; S218's path confirmed; **no `Runtime.pdl` exists at the tag** (S219 dropped); two claims flagged — the note's "same order" sentence **corrected**, the `userGesture`-vs-`isActive` sentence kept as measured. |
| R79Scribe | scribe | Drafted the note, the SOURCES rows and the lesson; the L1 admitted the note after the scout's correction. |
| R79Connector | connector | 20 sibling lanes scanned, **0 contested rows**; the showPicker surface appears in no sibling's capability table or corpus. |
| R79Probe | executor (labrat probe) | Hypothesis REFUTED: mutability is checked before the gesture (a disabled input with no activation throws `InvalidStateError`), matching S218's order. |
