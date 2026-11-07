# tabi — round 81

Lane `tabi-shokunin` (browser & web-interaction craft), round 81, attempt 1. Base
`c27e8406e6a2dc3cafcff030c9224cf8a14e3464`; digests commit **D = `a2183a93362259cb574ef3d03b565ee6d2c26599`**,
nonce `tabi-r81-l1-a2183a933622`. Axes at round start: all six at 9 (SCORECARD r80). Claims: **C1
coverage** (capability `chromium-showpicker-linux`, generation r81 — the r80 frontier legs) and
**C2 calibration** (the ten routed defects the r80 non-author spot-check owed to r81, plus the
self-drift identity leg).

## Work performed

**C1 — coverage, capability `chromium-showpicker-linux` generation r81.** The r80 frontier is now
measured and gated: (1) a cross-origin NON-file (`type=date`) input's own script throws
`SecurityError` "showPicker() called from cross-origin iframe." and opens nothing; (2) the SAME call
on a DISABLED `type=date` input is `InvalidStateError` same-origin and `SecurityError` cross-origin —
the order discriminator (Chromium checks the origin before mutability, the spec the reverse);
(3) transient activation is per-frame-tree; (4) a DIRECTORY answered through `DOM.setFileInputFiles`
expands into the input's files with `webkitRelativePath` set and trusted `input`+`change`; (5) a
`.txt` answered into `accept=".png"` is ACCEPTED (accept is a dialog hint, S223); (6) a real click on
an input whose picker is already open opens a SECOND chooser.
- Driver `scripts/chrome-cdp-showpicker-round81.mjs` (6 legs, one fresh browser per leg, cross-origin
  iframe on a second loopback port) — pin `e35e63c1…` in `.ufo/waves/round-81/freeze.txt`.
- Counter `scripts/check-showpicker-r81.mjs` (56 checks) — scored receipt
  `corpus/evidence/round81/chromium-showpicker/receipt.json`; `scored/counter-a.json` `verdict clean`,
  `checkCount 56`, `findings []`. Independent path: the same receipt under the D-frozen prior set
  with `--prior probe2` is also clean 56 (`scored/counter-a-dfrozen.json`), so the verdict does not
  depend on the post-D prior-set repair.
- Battery `scripts/negatives-showpicker-r81.mjs` (62 cases, coverage 56/56 declared checks) —
  `scored/battery-a.json` `cases 62`, `failed 0`, `coverage {declared 56, covered 56, uncovered [],
  unknown []}`.
- Kill power `scripts/kill-power-r81.mjs` (46 semantic mutants) — `scored/killpower-a.json`
  `mutants 46`, `killed 46`, `survived 0`, `crashed 0`.
- Selftest `scripts/selftest-r81-gates.mjs` — `scored/selftest-r81-gates.out` `clean true`,
  `cases 9`, `failed []`.
- Frozen scored runner `scripts/run-scored-r81.sh` (the frozen arguments of leg (c)).
- Cold-run acceptance (leg b): four cold receipts, each `clean 56` under the frozen counter with the
  repaired prior set plus `--prior` the scored receipt — `scored/cold-runs.txt` lists
  `R81Exec1/l1-rescore-cold1.json`, `l1-rescore-cold2.json`, `R81Exec2/cold3.score.json`,
  `cold4.score.json`; zero honest refusals (R81Exec1 ledger §1–§10; R81Exec2 report, including a
  space-bearing scratch path end to end).
- No-work control: the r80 receipt under the r81 counter exits 1 with 30 findings including `schema`
  (`controls/c1/nowork.json`); the base has no r81 receipt (`git cat-file -e
  c27e8406:corpus/evidence/round81/…` → 128; the counter on an absent path exits 2
  `receipt-unreadable`, `lesson-proof/c1-base-absent.json`).
- Forgery control: probe1 with its identity rewritten to the expected values exits 1 on
  `replay-event-timeline` (`controls/c1/forgery.json`).

**C2 — calibration, record drift.** `scripts/check-record-drift-r81.mjs` counts 12 record claims: the
ten r80 routed defects (end census, D9 nonce/D sweep, the two dead pointers, the Gate quote counts,
the frozen-claim annotation, the capability typo, the control count, D10, the battery binding) plus
the r81 identity leg (final nonce/D) and the numbers leg. Before: exit 1, **12** mismatches
(`lesson-proof/c2-before.json`). After: exit 0, **0** mismatches (`lesson-proof/c2-after.json`).
- Controls (`lesson-proof/c2-controls.json`, mirror lane, base 0 mismatches): reversed correction →
  `claims-annotation`; stale removed → `capability-typo`; nonce swapped → `r81-identity`.
- The ten corrections are recorded append-only in `corpus/lessons/round-81.md` `## Corrections`; the
  r80 records are not rewritten.
- `node scripts/check-capability-status.mjs --json` → exit 0, `mismatches 0`, `provisional 1`
  (selftest gate).

**Frontier step.** S222 (CDP `DOM.setFileInputFiles` parameters, 6-word quote at line 684) and S223
(WHATWG `accept` is a hint, 20-word quote) opened this round; S219/S220 re-opened and their `used-by`
gained the r81 note. Census start exit 0 (221 rows), end exit 0 (223 rows). Mistakes mined in
`corpus/lessons/round-81.md` `## Mistakes` (the `fl()` non-file crash, the click-while-open no-op
index, the prior-set-as-JSON read, the mirror stray-receipt collision). The sourced claim is C1
(S222/S223/S219/S220).

**Wave w1.** One v1 wave, 11 seats: executor ×4 (Exec1, Exec2, Exec3, Drift), reviewer ×2, critic ×1,
mutation-tester ×1, scout ×1, scribe ×1, connector ×1. Attack roles 3/11 = 27 % (≥25 %). No residual
call. Spec/dispatch/ready/results under `.ufo/waves/round-81/`; seat outputs under
`.ufo/waves/round-81-seats/`. The L1 held the planner seat (the validator rejects `planner`; a
bounded planning data-walk rode the scout/connector items).

**Wave w1 findings (integrated).**
- **R81Exec1.** Two cold runs clean (56/56, findings []); its M1–M6 matrix measured the prior-set
  states and forced the amendment ruling (the committed one-line set contradicted `claims.json`'s
  "probes 1-2"); the D-frozen set + `--prior probe2` path is also clean.
- **R81Exec2.** cold3/cold4 clean, one under a space-bearing scratch path; the directory answer
  carries `webkitRelativePath` through the space path; teardown swept to zero.
- **R81Review1.** Six receipt-level forgeries pass clean 56 (child sha/patch unbound, `window.__r3`
  eval swappable, chooser event duplicable with a rewritten `afterSendId`, `/tmp` answer path,
  `childState` unread, the two cross-origin legs transplantable from probe1 — they carry 0 page
  events, so replay gives them no protection). Routed to r82; disclosed in Limits.
- **R81Review2.** F1 kill power has no baseline guard; F2 eleven independent clause-level weakenings
  survive the frozen battery; F3 `coverage.unknown` 4 (fixed by repair 2); F4 the D freeze bytes are
  superseded (disclosed, both repairs named); F5–F10 diagnostics/coverage/`alsoAllowed` defects. The
  four extra cases are not redundant (each is the sole killer of a distinct mutant).
- **R81Critic.** Leg (c) was false as written twice — `coverage.unknown []` (fixed by repair 2) and
  the named `scripts/run-scored-r81.sh` (now exists); the limit sentence is off by one (moving
  `absNeed` is refused, `absNeed+1` escapes — corrected in the record, frozen text not edited); the
  four presence-bound C2 claims (disclosed, routed).
- **R81Connector.** 20 sibling lanes scanned, 0 contested rows, 11 adjacent, 9 none; no sibling holds
  a browser-interaction capability (mado's matches are the XDG desktop portal, kake's static HTML).
- **R81Scribe.** Drafted the note, the SOURCES rows and the lesson; its independent quote counts
  cross-checked the Gate (S222 6 words, S223 20 words after correction).
- **R81Scout.** Re-opened the four sources independently (WHATWG input page, Chromium
  `html_input_element.cc`, `DOM.pdl`, `Page.pdl`) and saved the fetched bytes with sha256.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| C1 instruments frozen (driver, counter, battery, kill power, selftest, drift counter), probes 1–2, no-work and forgery controls, claims.json, freeze.txt | LOG r81 items 1–2 | `a2183a93` |
| Digests commit D and nonce recorded | LOG r81 item 1 | `5233f510` |
| Instrument repair 1 (prior set probes 1–2, battery mirror path) + C1/C2 records, note, SOURCES 222–223, QUALITY 159, the ten r80 corrections, SCORECARD/LOG/SKILL/README/PROVINCE | LOG r81 items 1–6 | `86cd811a` |
| Scored selftest 9/9 and the cold-run index (leg b) | LOG r81 item 1 | `2f4b03ed` |
| Instrument repair 2 (battery coverage bookkeeping, `run-scored-r81.sh`) + re-scored battery/kill power/selftest + limit corrections | LOG r81 items 1–6 | `97d42fad` |
| Wave evidence (spec, dispatch, ready, seat outputs), scored receipt, census end | LOG r81 item 4 | `7416159a` |

## Before → after measurements

**C1** — counting command (frozen):
`node scripts/check-showpicker-r81.mjs --lane <ABS lane> --receipt corpus/evidence/round81/chromium-showpicker/receipt.json --expect-driver-sha256 e35e63c1… --expect-nonce tabi-r81-l1-a2183a933622 --expect-fixture-sha256 <receipt fixture sha256> --prior-set .ufo/waves/round-81/controls/c1/prior-set.txt --json`
- before (base `c27e8406`): no r81 receipt → exit 2 `receipt-unreadable`; the r80 receipt under the
  r81 counter → exit 1, 30 findings including `schema`.
- after (measured against `97d42fad`): exit 0, `verdict clean`, `checkCount 56`, `findings []`;
  battery 62/62 with `coverage.unknown []`; kill power 46/46; selftest 9/9; four cold runs clean.

**C2** — counting command (frozen): `node scripts/check-record-drift-r81.mjs --lane <ABS lane> --json`
- before (base): exit 1, **12** mismatches (`lesson-proof/c2-before.json`).
- after (measured against `97d42fad`): exit 0, **0** mismatches (`lesson-proof/c2-after.json`).

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
— start exit 0 (221 rows, `census/start.txt`), end exit 0 (223 rows, `census/end.txt`), W04
duplicate-URL warnings only.

- Rows before → after: **221 → 223** (`grep -c '^| S[0-9]' corpus/SOURCES.md` → 223).
- Rows added by tier: **A=2** (S222 CDP `DOM.setFileInputFiles`; S223 WHATWG `accept` attribute),
  B=0, C=0. Both `mined`, both opened 2026-11-07.
- Rows touched old→new: **S219** `used-by` `chromium-showpicker-runtime-round-80.md` →
  `…round-80.md, …round-81.md`; **S220** the same change. Logged in `corpus/lessons/round-81.md`
  `## Gate`.
- Frontier rows advanced: the four r80 frontier items (the non-file SecurityError, the
  `webkitdirectory` answer, the `accept`-filtered answer, the click-while-open) moved to core
  (`corpus/README.md` `## Round 81 coverage`, `PROVINCE.md` `## Round 81`); the remaining frontier is
  answering the second chooser, `type=color`/`type=month` cross-origin legs, nested `webkitdirectory`
  answers, and the `accept` token grammar.
- Assimilation: none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
  `considerthese/`: no such directory in this lane.

## Trend verdicts

- **expansion — improved.** Knowledge 93 → 94 (`corpus/knowledge/chromium-showpicker-runtime-round-81.md`,
  net new, cites S219/S220/S222/S223, all `mined`); registry 221 → 223; the capability generation adds
  six measured surface elements and the coverage map gains `## Round 81 coverage`.
- **quality — improved, with disclosed limits.** The scored gate generation is green (56 checks,
  battery 62/62 with `coverage.unknown []`, kill power 46/46, selftest 9/9); the ten r80 record
  defects are corrected on the record (12 → 0, directional, three controls); no admitted domain entry
  was found false. Disclosed limits: the replay rule is pair-based (a uniform shift escapes); the
  counter's limit sentence is off by one (corrected in the record); six receipt-level forgeries pass
  clean 56 (routed to r82); eleven clause-level weakenings survive the frozen battery (routed); the
  frozen kill power is the battery's own kill set.
- **discernment — improved.** The wave falsified the claims and the round's own controls caught four
  instrument defects before the freeze plus two named repairs; the critic's leg-(c) falsification was
  fixed by repair 2, not argued. The r80 outside spot-check agreed with every sampled admit/reject
  and its routed defects are this round's C2 subject. Disclosed limit: four C2 claims are
  presence-bound (routed to r82).

## Limits and routed defects (r82)

1. Six receipt-level forgeries pass clean 56 (R81Review1): bind the fixture child sha/patch, the
   `window.__r3` eval, the chooser event's `afterSendId`, the answer path's location, `childState`,
   and give the cross-origin legs at least one page event or a leg-specific binding.
2. Eleven independent clause-level weakenings survive the frozen battery (R81Review2 F2); the kill
   power has no baseline guard (F1).
3. The C2 counter's four presence-bound claims (`gate-quote-counts`, `capability-typo`,
   `control-count`, `landed-d10`) pass with a reversed correction (R81Critic).
4. The frozen limit sentence's first clause is off by one; the record states the corrected sentence.
5. The frozen `claims.json` pins the pre-repair battery (`6964de6f`) and the one-line prior set; both
   repairs are named in `corpus/lessons/round-81.md` and `freeze.txt`, and the D-frozen + `--prior`
   path is also verified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Round 81 gate registry, §Approval table, §Evidence ladder; prior `[x]` named lane-dispatched seats, not non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-81 entry, `corpus/evidence/round81/chromium-showpicker/receipt.json` (6 legs, 56-check counter).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/chromium-showpicker-runtime-round-81.md` + the gate registry entry command; the executor seats ran the driver and counter from the written commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` `## Round 81`; refusal routes unchanged (loopback only, no credential content).

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none this
round (no package, binary or npx install was needed; pacman stayed paused).
