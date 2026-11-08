# tabi — round 86 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 86, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `57265864` (lane clean). **Freeze commit:** `9919aa52`; **lane tip:** `346b3260`
(pushed; `ls-remote origin refs/heads/master` prints it). **D:** `4bd89a80f439`
(D1 `0e7bb7e08cac` was re-frozen before any gate ran — `plans/round-86.md` §Re-freeze history).
**Nonce:** `tabi-r86-l1-4bd89a80f439`. **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 works a lowest axis and is a capability move):

- **C1 — coverage (9): capability `chromium-showpicker-linux`, generation r86.** Two of the r85 note's
  three named frontier items are measured: the `accept` token grammar as a matrix (wildcard
  `image/*`, mixed list `image/png, .txt`, and a non-matching MIME token `application/pdf`) and the
  same-origin `type=color` activated arm. 30 legs; 95 checks.
- **C2 — operability (9): the tel-only conjunct narrowings.** R85Mut1's routed defect 3 — the six
  cross-origin law conjuncts each kept for the tel leg and dropped elsewhere. Six conjunct-scoped
  counter mutations are scored against both generations' frozen batteries; six r85 families ride as
  controls. 12 battery cases are added on the search and text legs.

Round shape: **ONE v1 wave, 11 seats** (`ufo-swarm-wave.mjs run` → 11 spawn, 0 resume, 11 settled, 0
dead; dispatch `.ufo/waves/round-86/w1-dispatch.json`, `.ready` taken by the dispatcher at
05:47:10, results `.ufo/waves/round-86/w1-results.json`). The results file's `output` fields are
null — the orchestrator kernel restarted mid-wave and could not recover child handles — so the
eleven seat report files under `.ufo/waves/round-86/w1/` are the authoritative record (orchestrator
note in `w1-results.json`; no seat died). Roles: 3 executor (R86Exec1/2/3), 2 reviewer
(R86Review1/2), 1 critic, 1 mutation-tester, 1 scout, 1 scribe, 1 connector, 1 sentinel —
**4 attack seats of 11 (36 %)**, 1 connector (policy cap 2). The L1 holds the planner seat; no
planner was dispatched (the validator rejects `planner`). Round total 11 seats; no residual call.

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`.ufo/waves/round-86/freeze.txt`, sha256 `4bd89a80f439…`):
  `scripts/chrome-cdp-showpicker-round86.mjs` (30 legs; four new parent inputs `#aw`/`#am`/`#ap`/
  `#cos`, six new legs), `scripts/check-showpicker-r86.mjs` (95 checks; new laws
  `accept-grammar-law` and `same-origin-color-law`), `scripts/negatives-showpicker-r86.mjs`
  (201 cases; five accept-grammar cases, five colour cases, 12 generated `cross-{search,text}-*`
  conjunct witnesses), `scripts/kill-power-r86.mjs` (66 mutants),
  `scripts/selftest-r86-gates.mjs` (10 gates), `scripts/check-record-drift-r86.mjs` (8 record
  claims), `scripts/witness-families-r86.mjs` (12 families).
- **Scored receipt** `corpus/evidence/round86/chromium-showpicker/receipt.json`: nonce
  `tabi-r86-l1-4bd89a80f439`, 30 legs, `failures: []`, fixture `94421dc0…`, driver `5a435da6…`.
- **The accept grammar measured** (five legs, three token forms read back from the page):
  `sp86-accept-wildcard-text` (`image/*` ← `text/plain`), `sp86-accept-wildcard-png`,
  `sp86-accept-mixed-text`, `sp86-accept-mixed-png` (`image/png, .txt`), `sp86-accept-pdf-token-png`
  (`application/pdf` ← `image/png`). Each: `showPicker {ok:true, ret:'undefined'}`, one
  `Page.fileChooserOpened` (`selectSingle`), the delivered file in the input's `files` with its bytes
  and a page `read` `ret: 'hex:…'`. Law `accept-grammar-law` (counter lines 659–683).
- **The colour arm measured**: `sp86-same-origin-color-activated` — `showPicker {ok:true,
  ret:'undefined'}`, activation `{true,true}→{false,true}`, no `input`/`change`, **0**
  `Page.fileChooserOpened`. Law `same-origin-color-law` (counter lines 685–687).
- **Leg (b)**: counter `clean` / 95 checks; battery 201 cases / 0 failed / coverage 95/95; kill power
  66 mutants / 66 killed / 0 survivors / 0 crashed / 0 unapplied; selftest 10/10 —
  `scored/{counter-a,battery-a,killpower-a,selftest}.json`.
- **C2 before/after**: `scored/witness-a.json` — before **3** survivors
  (`narrow-tel-crossaccess`, `narrow-tel-childseq`, `narrow-tel-childact-before`), after **0** of 12;
  reproduced independently by `w1/R86Exec3.md` (hand-applied `narrow-tel-childseq`: survives the r85
  battery, dies on the r86 battery) and mechanistically confirmed by `w1/R86Critic.md` Q3.
- **Do-nothing controls**: `controls/c1/nowork-r85-under-r86.json` — the r85 scored receipt under
  the r86 counter: exit 1, 89 checks, **40 findings** including `schema` and `plan-frozen`; the first
  capture recorded 39 and predated the scored receipt, so R86Sentinel's F1 (no-reproduction) was
  acted on: re-captured with the tree state named in `controls/c1/README-controls.md`.
  `controls/c1/noreceipt.txt` — exit 2 `receipt-unreadable`.
- **Adversarial seats**: R86Review1 (two LOW findings: the accept law's weakest conjunct is the
  receipt-level `desc.accept`; `showPicker`↔`triggerResult` unbound), R86Review2 (the 12 cases are
  individually attributable; loop-leg zero-open/`length`/`isTrusted` conjuncts unwitnessed),
  R86Critic (the 12-case set is 4× minimal; before-value 3 confirmed cell-by-cell), R86Mut1
  (independent 62-mutant sweep: 12 killed, 50 survived, **29 whole-counter escapes**, 21 shadowed),
  R86Sentinel (bounds/provenance audit).
- **Sources**: the L1 re-opened S223 and S219 itself on 2026-11-08 (WHATWG input page, HTTP 200,
  687,515 B, sha256 `b0202de1c0b4…`); located quotes 18 and 21 words, recorded in the lesson Gate.
  R86Scout re-opened the same page for the accept/colour/picker sentences (`w1/R86Scout.md`).
- **Frontier step**: census start/end exit 0, 223 rows both ends; knowledge 98 → 99; three rejects
  with flip conditions in the lesson Gate; no new registry rows (carried rows re-opened).
- **Seat ledger (11 seats, all reported; role → key result):**

| seat | role | key result |
|---|---|---|
| R86Exec1 | executor | two fresh-nonce cold runs: 95 checks, 94 true / 1 false (`prior-set-complete`), every law check agrees across runs |
| R86Exec2 | executor | battery 201/0/95–95, kill power 66/66/0/0, selftest 10/10 re-measured; exact match with the scored JSONs and SCORECARD |
| R86Exec3 | executor | witness before 3 / after 0 re-run; both do-nothing controls reproduced; hand-applied `narrow-tel-childseq` survives r85 and dies on r86 |
| R86Review1 | reviewer | counting command reproduces `clean / 95`; TWO LOW findings (accept law receipt-level; `showPicker`↔`triggerResult` unbound) |
| R86Review2 | reviewer | the 12 search/text cases fire their own id by their own conjunct; loop-leg zero-open/length/isTrusted unwitnessed |
| R86Critic | critic | before-value 3 confirmed cell-by-cell; the 12-case set is 4× minimal; acceptance-vs-filtering overclaim caught and narrowed |
| R86Mut1 | mutation-tester | independent 62-mutant sweep: 12 killed, 50 survived, **29 whole-counter escapes**, 21 shadowed by named checks |
| R86Scout | scout | S223/S219/S216 re-opened from one fetch (sha256 `b0202de1…`); three laws grounded with located quotes and word counts |
| R86Scribe | scribe | independent note/lesson/registry drafts; two record corrections applied (accept headline, source accounting) |
| R86Connector | connector | 20 sibling lanes pinned; 0 contested ground on accept/colour/showPicker/cross-leg witness design |
| R86Sentinel | sentinel | bounds and provenance clean; **F1 MEDIUM**: the committed do-nothing control no longer reproduced (40 vs 39 findings) — re-captured and recorded |

- **Pre-file falsification ledger**: `.ufo/waves/round-86/claim-falsification.tsv` — 11 rows, all
  six attack seats read, both claims covered; `prefile-falsification.py --lane tabi --round 86` →
  `pass claims=2 rows=11 attack_seats=6 findings=0`. Every `falsifies-wording` row names its
  narrowing in `plans/round-86.md §Narrowings`; the one `falsifies-number` row is R86Sentinel's F1,
  fixed by re-capturing the control.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `scripts/chrome-cdp-showpicker-round86.mjs` (30 legs), `scripts/check-showpicker-r86.mjs` (95 checks; `accept-grammar-law`, `same-origin-color-law`), `scripts/negatives-showpicker-r86.mjs` (201 cases), `scripts/kill-power-r86.mjs` (66 mutants), `scripts/selftest-r86-gates.mjs` (10 gates), `scripts/check-record-drift-r86.mjs`, `scripts/witness-families-r86.mjs` (12 families) | LOG round 86 | `9919aa52` |
| `.ufo/waves/round-86/{freeze.txt,claims.json,controls/,census/,sources/,scored/,w1-spec.json,w1-dispatch.json,w1.ready}` — frozen claims, pins, two prior probes, do-nothing controls, scored outputs, wave dispatch | LOG round 86 | `9919aa52` |
| `.ufo/waves/round-86/{w1/ (11 seat reports), w1-results.json, claim-falsification.tsv, controls/c1/README-controls.md}` + the re-captured control, record corrections (accept headline, source accounting, D1→D2) | LOG round 86 | `d80b2489`, count fix `346b3260` |
| `corpus/evidence/round86/chromium-showpicker/receipt.json` — the scored receipt at nonce `tabi-r86-l1-4bd89a80f439` (30 legs, 0 failures) | LOG round 86 | `9919aa52` |
| `corpus/knowledge/chromium-showpicker-runtime-round-86.md` (knowledge 98 → 99), `corpus/lessons/round-86.md`, `plans/round-86.md` (incl. §Narrowings and §Re-freeze history), `SCORECARD.md` round-86 section + two capability rows, `SKILL.md` §Round 86 gate registry, `LOG.md` round-86 entry | LOG round 86 | `9919aa52` |

## Before → after measurements

**C1 — coverage.** Counting command (frozen; the SCORECARD row carries the hardcoded fixture pin):

```
node scripts/check-showpicker-r86.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round86/chromium-showpicker/receipt.json \
  --expect-driver-sha256 5a435da6dae0d2eba1add83e51903ae954801fb67bca6186f2ad5787e94a313d \
  --expect-nonce tabi-r86-l1-4bd89a80f439 \
  --expect-fixture-sha256 94421dc0cceba84082aa3e75d501e14876b7eac6942c809f98f7fef6b774a3a1 \
  --prior-set .ufo/waves/round-86/controls/c1/prior-set.txt --json
```

- **Before** (base `57265864`): no r86 receipt → exit 2 `receipt-unreadable`
  (`controls/c1/noreceipt.txt`); the r85 scored receipt under the r86 counter → exit 1, 89 checks, 39
  findings including `schema`, `plan-frozen`, `leg-order` (`controls/c1/nowork-r85-under-r86.json`).
- **After** (D2): exit 0, `verdict clean`, **95 checks**, 0 findings; battery 201/0/coverage 95/95;
  kill power 66/66/0/0/0; selftest 10/10.
- Measured at commit `9919aa52` (the frozen instrument family and the scored receipt).
- Independent reproduction: `w1/R86Review1.md` §0 re-ran the counting command from committed bytes
  (`clean`, 95); `w1/R86Exec2.md` re-ran battery/kill-power/selftest; `w1/R86Exec1.md` cold runs agree
  on every law check.

**C2 — operability.** Counting command:

```
node scripts/witness-families-r86.mjs --lane <ABS lane> --work <ABS scratch> --json
```

- **Before** (frozen r85 battery, tel-only conjunct witnesses): **3 of 12** families survive —
  `narrow-tel-crossaccess`, `narrow-tel-childseq`, `narrow-tel-childact-before`.
- **After** (frozen r86 battery): **0 of 12** survive, 12 killed, 0 crashed, 0 unapplied
  (`scored/witness-a.json`, measured at `9919aa52`).

## Sources & frontier

- **Census** (frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
  start exit 0 (`census/start.txt`, 223 rows), end exit 0 (`census/end.txt`, 223 rows).
- **Rows before → after:** 223 → 223. Rows added by tier: none. Rows touched old→new: none by
  status/recheck/`used-by` — S223, S219, S216, S221, S222 were **re-opened** (each source opened this
  round, the lesson Gate carries URL, access date 2026-11-08 and located quotes of 18 and 21 words).
- **Frontier rows advanced:** the r85 note's `accept`-grammar item moved from frontier to measured
  core for three token forms; the `type=color` same-origin item moved from frontier to measured core;
  the same-element origin comparison stays frontier (not constructible in the loopback fixture).
- **Assimilation:** none — `merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`;
  no `considerthese/` directory exists in this lane.
- **Sourced claim:** C1 rests on S223 (the `accept` attribute as a hint) and S219 (the colour
  exemption), both opened this round; the knowledge note cites them and the lesson Gate records the
  located quotes.

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | **improved** | knowledge 98 → 99 (`ls corpus/knowledge/*.md \| wc -l`); two frontier items moved to measured core (`accept` grammar ×3 token forms, same-origin colour arm); two new capability rows in SCORECARD |
| quality | **improved** | 12 search/text conjunct witnesses close the tel-only gap (3 → 0); three battery cases added for the kill-power reach gap (66/66); no admitted entry fails re-check (counter, battery, kill power and selftest re-run from committed bytes) |
| discernment | **improved** | the wave falsified the accept law's weakest conjunct, the `showPicker`↔`triggerResult` binding, the 12-case minimality and the conjunct-completeness; all eight narrowings recorded in `plans/round-86.md §Narrowings` before filing; R86Mut1's 29 escapes routed as the round's principal limit |

## Trend verdict details (one line each, for the closure)

- **expansion improved** — `ls corpus/knowledge/*.md | wc -l` → 99; SCORECARD round-86 capability rows:
  `chromium-showpicker-linux` (generation r86) and `battery-leg-witnesses`.
- **quality improved** — `scored/battery-a.json` `cases 201, failed 0, coverage 95/95`;
  `scored/witness-a.json` before 3 / after 0; `scored/killpower-a.json` `66/66/0/0`.
- **discernment improved** — `prefile-falsification` ledger + `plans/round-86.md §Narrowings` items 1–8;
  no claim sentence survives that a wave artifact falsified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Round 86 gate registry registers all seven r86 instruments with commands and measured numbers;
  §Approval table and the evidence ladder unchanged and re-read this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 30-leg generation run
  (one fresh browser per leg, real CDP against a loopback fixture) is logged in the LOG round-86
  entry and scored in `scored/counter-a.json`.
- [~] Instructions executable by an agent without oral context — the registry block gives each
  instrument's full command; `w1/R86Exec1.md` and `w1/R86Exec2.md` executed them from the block
  alone (both lane-dispatched seats).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R86Connector's
  20-sibling scan found no contested ground on the accept/colour/showPicker surfaces
  (`w1/R86Connector.md` §8).

## Round extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (node v24.21.0, python3, curl and git were already present; every seat
  reported no installs). Tools used as-is: `node`, `python3`, `curl`, `git`, `jj-lane.sh`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no
  lane-written stray at the fleet root. The two untracked fleet paths present are not this lane's
  (`.scratch/closure-tabi-r83-entry.json` is orchestrator state, `.ufo/reports/round-89/chousa.md`
  is another lane's). `git -C tabi-shokunin status --porcelain` is empty at `346b3260`; every round
  file sits under the lane tree or the sanctioned report path.
- **Scratch:** the L1 scratch tree `/fast/scratch/hyaku/tabi-r86/` is purged at close (probe, scored,
  battery, kill-power, selftest and per-seat dirs); receipts are copied into the wave dir, never left
  in `/tmp` or the scratch root.
- **L0:** no new operator question; the standing `tabi | round-57` assimilation question is
  unchanged and was routed around (Assimilation: none).
