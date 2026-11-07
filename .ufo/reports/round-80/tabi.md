# tabi — round 80

Lane repo `/home/vgpnk/Projects/shokunin/tabi-shokunin`; base `e2e12ca58fe2cdbed4aa97af47793b6cfb5a9350`
(lane clean, `local=remote`, `ahead=0 behind=0`). Round 79 was admitted; its routed defects 1–4 are this
round's C2 spine and its named frontier legs are C1's. **Declared claims (2):** **C1** coverage (9) —
capability generation r80 of `chromium-showpicker-linux` (the r79 frontier legs); **C2** calibration
(9) — record drift (r79 routed defects 1–4) plus the self-drift leg (defect 8). Both frozen in
`.ufo/waves/round-80/claims.json`; instrument digests in `.ufo/waves/round-80/freeze.txt`, final
digests commit **D = `93172ba92d6372563f9419b3aaf81f4b6398365b`** (D1 `bf5ba377`, D2 `88808c13`,
D3 `f9ece656`, D4 `b2560829`, D5 `53ecca84`, D6 `045fccc5`, D8 `a1b14284`, D9 `211962dc` were superseded
by instrument repairs before the final scored run; every superseded run is named below and none is cited
as evidence).

## Work performed

- **C1 — capability `chromium-showpicker-linux`, generation r80.** Driver
  `scripts/chrome-cdp-showpicker-round80.mjs` (7 legs, one fresh browser per leg, a cross-origin iframe
  on a second loopback port), counter `scripts/check-showpicker-r80.mjs` (57 checks), battery
  `scripts/negatives-showpicker-r80.mjs` (102 cases), kill power `scripts/kill-power-r80.mjs`
  (80 mutants), selftest `scripts/selftest-r80-gates.mjs` (9 gates). Scored receipt
  `corpus/evidence/round80/chromium-showpicker/receipt.json` (nonce `tabi-r80-l1-93172ba92d63`):
  counter clean 57 checks, battery 102/102, kill power 80/80 with 0 survivors, selftest 9/9. The
  measured laws are in `corpus/knowledge/chromium-showpicker-runtime-round-80.md`: a `webkitdirectory`
  input and an `accept`-constrained input both open `selectSingle`; two `userGesture` calls both
  succeed and open two pickers (no already-open guard); a `setTimeout(0)` call from a trusted click's
  handler keeps the activation; a cross-origin iframe's FILE input is exempt from the SecurityError
  (S219/S220) and opens while the parent cannot reach the child document; a disabled cross-origin file
  input throws `InvalidStateError` without consuming activation; the programmatic trigger ANSWERED with
  `DOM.setFileInputFiles` on the event's `backendNodeId` delivers the exact bytes and fires trusted
  `input`+`change`.
- **C2 — record drift.** `scripts/check-record-drift-r80.mjs` (19 claims): the r79 corrections are
  append-only directional pairs and EVERY pair of the same shape must name the true value (a second
  wrong correction is a mismatch); the self-drift leg reads the scored VERDICTS (clean, 0 failed, 0
  survivors) and the numbers from the committed scored outputs. Before 17 mismatches
  (`lesson-proof/c2-before.json`), after 0. Controls (`lesson-proof/c2-controls.json`, seat R80Drift):
  reverse-correction → `sc-79-battery`; stale-removed → `log-79-cases`; truth-moved → the five self
  claims.
- **Frontier step.** `corpus/SOURCES.md` 218 → 221 rows (S219 WHATWG showPicker exemption, S220
  Chromium 155 `html_input_element.cc`, S221 CDP Page.pdl), all opened this round with located quotes
  in the lesson's Gate; census start exit 0 (218), end exit 0 (221). Five mistakes mined in
  `corpus/lessons/round-80.md` `## Mistakes`.
- **Wave w1.** One v1 wave, **12 seats, all settled, none dead** (5 executor incl. the labrat probe and
  the C2-controls seat, 2 reviewer, 1 critic, 1 mutation-tester, 1 scout, 1 scribe, 1 connector);
  attack roles 4/12 = 33 %; the L1 holds the canonical planner seat and the `labrat` probe rides an
  executor seat (the validator rejects `planner` and `labrat` as swarm roles). Spec `w1-spec.json`,
  dispatch `w1-dispatch.json`, handoff `w1.ready`, results `w1-results.json`.
- **Assimilation: none** (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
  `considerthese/`: no such directory in this lane.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Instruments, frozen claims and digests D1, pre-freeze probes and prior set, C2 before state, census start | round-80 bullets 1–3 | `bf5ba377` |
| Digests D2 — the battery exempts the committed scored receipt by content; kill power runs in parallel with a counter timeout | round-80 bullet 1 | `88808c13` |
| Digests D3 — battery 103 cases with the threshold brackets and the survivor-isolating cases; kill power 81/81 on the scored receipt | round-80 bullet 1 | `f9ece656` |
| Digests D4 — the drift counter reads the filed reports from the fleet repo and checks claims.json in its frozen phrasing | round-80 bullet 2 | `b2560829` |
| Digests D5 — the replay bracket breaks every gap and targets the exact matched count | round-80 bullet 1 | `53ecca84` |
| Digests D6 — the replay rule is pair-based; the gap side is reported, not a refusal | round-80 bullets 1–2 | `045fccc5` |
| Digests D8 — an unparsable receipt must be a `.json` file or start with `{`; a prose report quoting the schema is not a receipt | round-80 bullet 1 | `a1b14284` |
| Digests D9 — probe4 joins the prior set so the mirror-lane cases see every walked probe as a prior | round-80 bullets 1–3 | `211962dc` |
| Scored evidence under D10 (counter 57, battery 102/102, kill power 80/80, selftest 9/9), the prefreeze summary, the C2 controls, the r79 corrections, the knowledge note, S219–S221, QUALITY 157–158, the lesson, SCORECARD/LOG/SKILL/PROVINCE/README records, wave w1 spec/results/reports | round-80 bullets 1–4 | `66937f20` |
| The r79 lesson's append-only corrections (battery 90 cases, kill power 64/64, the withdrawn kp-run1 pointer, the Gate quote counts) | round-80 bullet 2 | `70784d27` |

## Before → after measurements

| Claim | Counting command | Before | After | Measured at |
|---|---|---|---|---|
| C1 coverage (9), `chromium-showpicker-linux` generation r80 | `node scripts/check-showpicker-r80.mjs --lane <ABS lane> --receipt corpus/evidence/round80/chromium-showpicker/receipt.json --expect-driver-sha256 cb93935c…19cc --expect-nonce tabi-r80-l1-93172ba92d63 --expect-fixture-sha256 <receipt fixture sha> --prior-set .ufo/waves/round-80/controls/c1/prior-set.txt --json` | base: no r80 receipt → exit 2 `receipt-unreadable`; the r79 showpicker receipt under the r80 counter → exit 1, findings incl. `schema` and every `leg-*` (`lesson-proof/c1-nowork.json`) | exit 0 `clean`, **57 checks**; battery **102/102**; kill power **80/80**, 0 survivors; selftest 9/9 | `93172ba9` |
| C2 calibration (9), record drift + self-drift | `node scripts/check-record-drift-r80.mjs --lane <ABS lane> --json` | exit 1, **17 mismatches** (`lesson-proof/c2-before.json`) | exit 0, **0 mismatches** (`lesson-proof/c2-after.json`); `check-capability-status.mjs --json` exit 0, `mismatches 0`, `provisional 1` | `93172ba9` |

The C1 limit (frozen, printed in the counter's `limit` block): the replay rule is pair-based — a forger
who rewrites the identity fields and moves at least `ceil(0.5 * prior events)` event times escapes it;
the gap side is REPORTED, never a refusal, because this driver's fixed waits reproduce gap durations
across honest runs (measured: an honest receipt matched a prior's single gap within 0.05 ms). A forger
who shifts EVERY event by a constant offset escapes the pair rule; that is the stated limit.

## Sources & frontier

- `corpus/SOURCES.md` rows: **218 → 221** — `grep -cE '^\| S[0-9]{3,}' corpus/SOURCES.md` (218 at base,
  221 after). Added by tier: **A = 3** (S219 spec, S220 code, S221 code), B = 0, C = 0. Rows touched
  old→new: none. Census start `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
  **exit 0** (`.ufo/waves/round-80/census/start.txt`), end **exit 0**
  (`.ufo/waves/round-80/census/end.txt`), W04 duplicate-URL warnings only.
- Frontier rows advanced: the r79 note's named frontier (webkitdirectory/accept inputs, the deferred
  trigger, the cross-origin frame, the trigger-then-answer combination) is now core. The r80 note's
  Frontier names what stays open: a `type=date` cross-origin leg (the SecurityError the spec and
  Chromium keep for non-file, non-color inputs), a `webkitdirectory` answer leg (measured by R80Exec3's
  probe, not in the capability), an `accept`-filtered answer, and a real click while a picker is open.
- Mined mistakes: 5 rows in `corpus/lessons/round-80.md` `## Mistakes`; QUALITY 157–158 added.
- Sourced claim: C1 rests on S219–S221, opened this round with located quotes in the lesson's Gate.
  R80Scout re-opened all four items and corrected two locators (`core/html/forms/`,
  `devtools_protocol/domains/` at this tag).
- **Correction — the SecurityError reachability (R80Scout HIGH).** The frozen claims' C1 limit said
  page script cannot construct the SecurityError case. False: the child origin's own script reaches it
  on a NON-file input (`type=text` → SecurityError "showPicker() called from cross-origin iframe."),
  and S219/S220 both exempt File/Color inputs, which is why the r80 file-input leg succeeds. The
  measured law is the EXEMPTION; the SecurityError is r81's first leg. The seat's discriminating table
  (`.ufo/waves/round-80-seats/R80Scout/probes/discriminating-orders.json`, cases A–E) also MEASURES the
  order disagreement: a cross-origin DISABLED `type=text` throws `SecurityError` (Chromium checks
  cross-origin before mutability) while the same call same-origin throws `InvalidStateError` (the spec
  orders mutability first). The note's law 6b carries it. The frozen claims.json is not edited; this
  entry and the lesson carry the correction.
- Assimilation: none (`merge/tabi/` closed pending the open L0 `tabi | round-57`); `considerthese/`
  absent in this lane.

## Trend verdicts

- **expansion — improved.** A new knowledge note on ground the coverage map did not hold
  (`corpus/README.md` `## Round 80 coverage`), registry 218 → 221 (all three rows `mined` and cited),
  and the capability's generation r80 adds six measured surface elements (the two input classes, the
  double-open boundary, the deferred trigger, the cross-origin exemption, the answered trigger).
- **quality — improved, with disclosed limits.** The scored gate generation is green (57 checks,
  battery 102/102, kill power 80/80, selftest 9/9) and the r79 record drift is corrected on the record
  (17 → 0, directional, with three controls). Two limits are disclosed: the replay rule is pair-based
  (a uniform shift escapes it), and the wave's independent mutation seat (R80Mut1, 123 conjunct-level
  mutants) found 95 survivors of the frozen battery, 84 with an executed witness — the battery has one
  isolating case per CHECK, not per conjunct. Routed to r81; no admitted corpus entry was found false.
- **discernment — improved.** The wave falsified the claim four times and each became a correction: the
  critic's gap trilemma (the gap side refused honest runs), the scout's SecurityError refutation, the
  reviewer's fixture/answer limits, and the mutation seat's survivor census. The round's own controls
  caught five instrument defects before the freeze (the arm-before-click ordering, the chooser
  baseline, the content exemption, the unparsable-prose walk, the gap rule).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Round 80 gate registry with the entry command, verdict map, self-test and pinned path; the law table
  in `corpus/knowledge/chromium-showpicker-runtime-round-80.md` cites S219–S221. No non-author verifier
  has checked this round's additions yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 7-leg runtime measurement
  and its counter, logged in `LOG.md` round-80 bullet 1.
- [~] Instructions executable by an agent without oral context — the driver/counter/battery entry
  commands are in `SKILL.md` §Round 80 gate registry and the note's `recheck:` line; the pre-freeze
  probes reproduce from them.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` gains the cross-origin frame
  and the answer path and keeps the refusal routes; the wave's connector scanned 20 sibling lanes and
  found no contested row.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. This round's mission began
2026-11-07T19:03:13-03:00 (`.ufo/watchdog.log` `launch tabi round=80 pgid=2294340`) and is
**progressing** (commits `bf5ba377` … `70784d27`; lane tip `70784d27e3a8e54ce060dfb8fd3f3a3c793deea0`, remote equal).

## Tool installs

None this round (no package, binary or tool was installed or upgraded; the round used the host's
`/usr/bin/chromium` 155.0.8059.84 and node v24.21.0).

## Wave w1 — results

12 seats, all settled, **none dead** (`w1-results.json`: 12 results, 12 seats). Results `.ufo/waves/round-80/w1-results.json`; per-seat reports
in `.ufo/waves/round-80/w1/` and evidence in `.ufo/waves/round-80-seats/`.

| Seat | Role | Outcome |
|---|---|---|
| R80Exec1 | executor | Leg (b): cold1 + cold2, driver exit 0, 7/7 legs, zero honest refusals, clean 57/57 under both counter versions. F1/F2: the counter changed under it mid-round and the scored nonce moved with D — both recorded as routed instrument defects. |
| R80Exec2 | executor | Leg (b): cold3 + cold4 plus a scratch path containing a space; all clean, no defects. |
| R80Exec3 | executor | Frontier probe: a `webkitdirectory` input answered with a DIRECTORY path delivers one FileList entry per file with `webkitRelativePath`; an `accept=".png"` input answered with a `.txt` is accepted; a real click while a chooser is pending — evidence for r81, not capability legs. |
| R80Review1 | reviewer | Attack on C1: the instrument/identity churn (B1–B4), the unpinned fixture (H1), `answer-law` as a consistency check rather than a delivery proof (H2), the unbound cross-origin child result (H3), the unbound scored outputs (H4). All routed to r81; none falsifies the scored legs as measured. |
| R80Review2 | reviewer | Battery/kill-power attack: the frozen bracket did not bracket (F1), the gap side refused an honest run (F2), the D6 repair removes the gap rule and both its tests (F3), counts amended mid-wave (F4), the deleted mutant receipt-dependent (F5), 29 `alsoAllowed` entries never fire (F6), diagnostics (F7), `bracketNeed` (F8), prose poisoning fixed at D8 (F9). |
| R80Critic | critic | The gap trilemma, the frozen nonce, the C2 self-drift weaknesses (counts only; the wrong-correction clause unenforced) and the capability-row wording — all integrated (the self-drift leg reads verdicts, every correction pair must name the truth, the row states first-working round 79). |
| R80Mut1 | mutation-tester | 123 independent conjunct-level mutants on the D9 counter: 22 killed by refusal cases, 2 by the honest case, 95 survivors of which 84 have an executed witness — the battery is per-check, not per-conjunct. Routed to r81. |
| R80Scout | scout | All four sources opened and quoted; the HIGH SecurityError-reachability refutation and two locator corrections (integrated). |
| R80Scribe | scribe | Drafted the note, the SOURCES rows and the lesson; the L1 admitted the note after the scout's correction. |
| R80Connector | connector | 20 sibling lanes scanned; no contested row; the desktop XDG-portal boundary (mado) vs headless CDP interception (tabi) named as the adjacency boundary. |
| R80Probe | executor (labrat probe) | Hypothesis CONFIRMED: transient activation is per-frame-tree — the child's click sets the parent's `isActive`/`hasBeenActive`, and the child's successful `showPicker()` consumes it tree-wide; the failed call does not. |
| R80Drift | executor | C2 controls in a scratch mirror: reverse-correction → `sc-79-battery`, stale-removed → `log-79-cases`, truth-moved → the five self claims. |

Routed defects for r81 (from the wave): the fixture is unpinned (H1); `answer-law` proves consistency,
not delivery (H2); the cross-origin child result is unbound (H3); the scored outputs are unbound (H4);
the battery is per-check, not per-conjunct (R80Mut1's 84 witnessed survivors); 29 `alsoAllowed`
entries never fire (F6); the driver header's order-discrimination sentence is false as built (R80Scout);
a `type=date` cross-origin leg, a `webkitdirectory` answer leg and a click-while-pending leg are the
frontier.
