# tabi — round 89 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 89, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `5a901163` (lane clean). **Scored receipt:** `corpus/evidence/round89/chromium-showpicker/receipt.json`
(nonce `tabi-r89-l1-7bde5e6c2f2d`, driver `76b69b4f…`, fixture `69acad57…`, 41 legs, 0 failures).
**Lane tip:** `b7513f81` (pushed; `ls-remote origin refs/heads/master` prints it). **Instrument freeze:** D5 `061dec8a` (`plans/round-89.md` §Re-freeze history: D1 `7bde5e6c2f2d` first freeze,
D2 the battery `LEG_ALSO` repair, D3 the replay-limit consistency move into the limit block, D4 the kill-power from-string repair + `accept-domread-law-raw`, D5 the last from-string repair). **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 works a lowest axis and is a capability move):

- **C1 — coverage (9): capability `chromium-showpicker-linux`, generation r89.** The DOM-parsed
  token list round 88 left as frontier: four legs re-read `window.__inputs()` on the page at settle
  (`domRead`) and bind both the raw `accept` string and the parsed token list —
  `sp89-accept-domread-text` (`aw`, `image/*` ← txt), `sp89-accept-domread-png` (`am`,
  `image/png, .txt` ← png), `sp89-accept-domread-multimime` (`a2`, `image/png,application/pdf` ← txt),
  `sp89-accept-domread-whitespace` (`aws`, `"  image/png ,  .txt  "` ← png). The tokenization is the
  fixture's split-and-trim emulation of WHATWG §2.3.8, disclosed as such. 41 legs; 107 checks.
- **C2 — calibration (9): the round-88 non-author spot-check routed defects 1–2.** The drift
  `--selftest` fixture now carries all seven swept sections (its `scorecard-tallies` red is causal),
  the drift fixture tree is removed in-process (the Narrowing-7 leak fix, verified 0 left behind),
  and the counter's replay limit sentence prints the computed per-prior `absNeed` values with
  `limit.replayConsistency` asserting their agreement (the Narrowing-8 fix).
  `scripts/check-record-drift-r89.mjs` counts 4 statements. Before (base `5a901163`): 3 mismatches
  (`selftest-wording`, `gate-selftest`, `quality161-sweep`); after: 0.

Round shape: **ONE v1 wave, 12 seats** (`ufo-swarm-wave.mjs run` → `counts.spawn 12`; dispatch
`.ufo/waves/round-89/w1-dispatch.json`; `.ready` written by L1 `TabiR89`; 12/12 seat reports filed).
Roles: 3 executor (R89Exec1/2/3), 2 reviewer (R89Review1/2), 1 critic, 1 mutation-tester, 1 scout,
1 scribe, 1 connector, 1 sentinel, 1 simplifier — **5 attack seats of 12 (42 %)**, 1 connector
(policy cap 2). The L1 holds the planner seat; no planner was dispatched (the validator rejects
`planner`). Round total 12 seats; no residual call; dead seats: none — all twelve settled and filed.
Scratch purged (`/fast/scratch/hyaku/tabi-r89` removed after landing).

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`.ufo/waves/round-89/freeze.txt`, D5 `061dec8a`):
  `scripts/chrome-cdp-showpicker-round89.mjs` (41 legs; fixture patch extended so
  `window.__inputs()` returns `acceptTokens` alongside the raw `accept`, and each domread leg re-reads
  it at settle), `scripts/check-showpicker-round89.mjs` (107 checks; `accept-domread-law` over 4 rows),
  `scripts/negatives-showpicker-round89.mjs` (223 cases, coverage 107/107),
  `scripts/kill-power-round89.mjs` (72 mutants), `scripts/selftest-r89-gates.mjs` (11 gates),
  `scripts/check-record-drift-r89.mjs` (4 statements). Each gate carries an isolated `--selftest`.
- **Scored receipt** (41 legs, `failures: []`): counter `clean`, `checkCount 107`, 0 findings
  (`scored/counter-a.json`); battery 223 cases / 0 failed / coverage 107/107 (`scored/battery-a.json`);
  kill power 72 mutants / 72 killed / 0 survivors / 0 crashed / 0 unapplied (`scored/killpower-a.json`);
  selftest 11/11 (`scored/selftest.json`).
- **Cold-run reproduction** by R89Exec1: two fresh-nonce runs, 41/41 legs each, 106/107 checks with
  only the declaration `prior-set-complete` failing (`w1/R89Exec1.md`).
- **Leg (b) reproduction** by R89Exec2: battery byte-identical to `scored/battery-a.json`; kill power
  reproduced after the D4 repairs; selftest 11/11 at the final freeze (`w1/R89Exec2.md`).
- **C2 before/after and controls** by R89Exec3: base worktree `5a901163` → exit 1, 3 mismatches
  (`gate-selftest` joins because the r89 scripts are absent at base); both C1 do-nothing controls
  reproduce (exit 1 with `schema`; exit 2 `receipt-unreadable`); drift `--selftest` exit 0 with the
  leak fix verified (`w1/R89Exec3.md`).
- **Adversarial seats**: `R89Review1` (count + pin audit; the fixture sha re-derived out-of-band to
  `69acad57…`, F1 in-flight truncation honestly recorded), `R89Review2` (24 receipt mutations: 15
  caught, 9 not — the settle re-read, the snapshot identity and the answer provenance are unenforced),
  `R89Critic` (fixture-emulated vs §2.3.8 wording; `replay-limit-consistency` restates the math, not
  the prose), `R89Mut1` (44 independent mutants: 9 killed, 35 survived, 0 crashed — 16 witnessed real
  acceptance gaps, named clauses), `R89Sentinel` (9 audit axes: S1–S6 HIGH/MEDIUM found, all reconciled
  at D5; S9 CLEAN), `R89Simplifier` (the five frozen-state blockers that the D2–D5 batch repaired,
  live-state verified), `R89Scribe` (F1–F10 record defects, F1/F2 made a claim leg false at the frozen
  bytes — both repaired), `R89Connector` (21-lane scan: zero capability overlap, this lane is the
  sole owner of the accept/showPicker/domRead ground), `R89Scout` (S224 re-opened; the dfn wording
  byte-identical to the registry row, the case rule located in Infra rather than §2.3.8).
- **The wave's own findings changed the round**: D2 (battery LEG_ALSO), D3 (replay-limit consistency
  move), D4 (kill-power from-strings + the raw case) and D5 (the last from-string) were repaired and
  re-measured; the C2 before-numeral was corrected from 2 to the measured 3; the Scout's "case rule
  lives in Infra" finding forced the note's wording to fixture-emulated.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| six r89 instruments: driver (41 legs), counter (107 checks), battery (223 cases), kill power (72 mutants), selftest (11 gates), record drift (4 statements), each with an isolated `--selftest` | LOG round 89 | `0791b191` (D1) / `b7513f81` (D5) |
| `.ufo/waves/round-89/{freeze.txt,claims.json,controls/,census/,sources/,scored/,w1-spec.json,w1-dispatch.json,w1.ready,w1.ready.dispatched,w1/,w1-results.json,claim-falsification.tsv}` | LOG round 89 | `0791b191` / `b7513f81` |
| `corpus/evidence/round89/chromium-showpicker/receipt.json` — the scored receipt at nonce `tabi-r89-l1-7bde5e6c2f2d` (41 legs, 0 failures) | LOG round 89 | `b7513f81` |
| `corpus/knowledge/chromium-showpicker-runtime-round-89.md` (knowledge 101 → 102), `corpus/lessons/round-89.md`, `plans/round-89.md`, `SCORECARD.md` r89 section + capability row, `SKILL.md` §Round 89 gate registry, `LOG.md` r89 entry, `corpus/QUALITY.md` 162 + 161 r89 cite, `corpus/SOURCES.md` S224 row + r89 search-log entry | LOG round 89 | `b7513f81` |

## Before → after measurements

**C1 — coverage.** Counting command (frozen; the fixture value is the scored receipt's own):

```
node scripts/check-showpicker-round89.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round89/chromium-showpicker/receipt.json \
  --expect-driver-sha256 76b69b4f691d24c8c94a92897e33635d2386b9191f5aaa66640515dc998bd2d0 \
  --expect-nonce tabi-r89-l1-7bde5e6c2f2d \
  --expect-fixture-sha256 69acad5754e0effb480771dd68197c26815bf0aabd4e76afe63ce09ca462c5ed \
  --prior-set .ufo/waves/round-89/controls/c1/prior-set.txt --json
```

- **Before** (base `5a901163`): no r89 receipt → exit 2 `receipt-unreadable`
  (`controls/c1/noreceipt.txt`); the r88 scored receipt under the r89 counter → exit 1,
  findings incl. `schema`, `plan-frozen` (`controls/c1/nowork-r88-under-r89.json`).
- **After** (D5 instruments): exit 0, `verdict clean`, **107 checks**, 0 findings;
  battery 223/0/coverage 107/107; kill power 72/72/0/0/0; selftest 11/11. Measured at
  `b7513f81`.
- Independent reproduction: `w1/R89Exec1.md` (two cold runs, 41/41 legs, 106/107 each, only the
  declaration `prior-set-complete`), `w1/R89Exec2.md` (battery byte-identical; kill power 72/72;
  selftest 11/11), `w1/R89Review1.md` (counting command `clean`/107, fixture re-derived).
- **Narrowed**: acceptance is not filtering (the dialog is unmeasured); the token list is the
  fixture's normalization — comma-split, ASCII-trimmed, ASCII-lowercased — not Chromium's internal
  tokenization (`w1/R89Scout.md`, `w1/R89Critic.md`); the settle re-read is driver-observed, not
  counter-enforced (`w1/R89Review2.md` F1); attribution rides on the top-level snapshot plus the
  domRead target entry's two fields (R89Review2 F2); the byte contents stay the inherited r83
  marker under r89 names (`plans/round-89.md` §Narrowings).

**C2 — calibration.** Counting command:

```
node scripts/check-record-drift-r89.mjs --lane <ABS lane> --json
```

- **Before** (base `5a901163` worktree): exit 1, claims 4, **3 mismatches** — `selftest-wording`,
  `gate-selftest`, `quality161-sweep` (`scored/drift-before.json`; `gate-selftest` is red at base
  because the r89 instrument files do not exist there). The frozen claim text first said 2; the
  numeral was corrected to the measured 3 post-scoring and is disclosed in `claims.json`
  `frozenAmendments` and `plans/round-89.md` §Frozen-amendment note.
- **After**: exit 0, **0 mismatches**, claims 4 (`scored/drift-a.json`), measured at `b7513f81`.
- The drift gate's own `--selftest` exits 0 on an isolated fixture lane carrying all seven swept
  sections (causal reds: `bad=["round-44-no-9","round-44-has-10"]`, `staleHolds=true`), and the
  leak check confirms 0 `tabi-r89-driftfix-*` trees remain.
- **Narrowed**: the C2 before-control's third red (`gate-selftest`) is an artifact of the control's
  own scoping, not a record drift; the fixture's seven-section property is unbound by its own
  selftest (R89Mut1 `selftest-fixture-seven-sections-reduced` survives); three statements are
  string-presence checks (R89Critic).

## Sources & frontier

- **Census** (frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
  start exit 0 (`census/start.txt`, 223 rows); end exit 0 (`census/end.txt`, 223 rows — re-run on the
  final tree, S224 included and pointing at the committed r89 note).
- **Rows before → after:** 223 → 224. Rows added by tier: 1× tier A (`mined`). Rows touched
  old→new: none by status/recheck/`used-by` — **S223** and **S219** were re-opened in place
  (access date 2026-11-08, 687,515 B, sha256 `b0202de1c0b4…`, located quotes in the lesson Gate);
  **S221/S222** were carried, not re-opened. The round-89 bounded re-opening is recorded at
  `corpus/SOURCES.md` §Search log.
- **Frontier rows advanced:** the DOM-parsed normalization moved from named frontier to measured
  core; R89Scout moved the case rule **out of** §2.3.8 (it lives in Infra as a matching rule), and
  the note's wording was narrowed to fixture-emulated. Knowledge 101 → 102.
- **Assimilation:** none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
  `considerthese/` — no such directory in this lane.
- **Frontier step:** the lesson Gate records one admit (`corpus/knowledge/chromium-showpicker-runtime-round-89.md`)
  and two rejects with flip conditions (Chromium tokenization; counter-verified settle re-read);
  one mistake class mined into `corpus/lessons/round-89.md` §Mistakes.

## Trend verdicts

- **expansion: improved** — knowledge 101 → 102 (`git ls-tree -r --name-only <rev> corpus/knowledge/ | wc -l`);
  one named frontier item (the DOM-parsed normalization) moves to measured core; one capability row enters SCORECARD.
- **quality: improved** — the frozen family re-derives 107/107 checks, battery 223/0, kill power 72/72,
  selftest 11/11; the r88 fixture-leak and overdetermined-witness defects are repaired; the round's own
  attack seats forced four instrument repairs (D2–D5) that each re-ran green.
- **discernment: improved** — the r88 spot-check's two routed defect classes are closed against observed
  state; the wave falsified five sentences (the frozen battery's greenness, the stale 102 literal, the
  C2 before-numeral, the settle re-read's reach, the tokenization's provenance) and each was narrowed
  or corrected with its artifact cited.

## Corrections the wave forced

`plans/round-89.md` §Narrowings and §Frozen-amendment note: the tokenization is fixture-emulated, not
Chromium's parser; the settle re-read is driver-observed, not counter-enforced; the per-leg answer
provenance is unbound (carried like the grammar legs' `upload*` narrowing); the replay-limit sentence is
self-asserting (no battery case can trip a counter-text check by mutating the receipt); and the C2
before-numeral correction (2 → 3, disclosed).

## Seat ledger (12 seats, all filed; `w1-results.json` = 12 results)

| seat | role | key result |
|---|---|---|
| R89Exec1 | executor | two fresh-nonce cold runs: 41/41 legs, 0 failures, 106/107 checks each; only the declaration `prior-set-complete`; the four `sp89-accept-domread-*` legs fact-identical in both. |
| R89Exec2 | executor | battery byte-identical to `scored/battery-a.json` (223/0/107/107); kill power 72/72 (after the D4 row-whitespace repair); selftest 11/11. |
| R89Exec3 | executor | C2 BEFORE on base `5a901163`: exit 1, **3** mismatches; both C1 controls reproduce (exit 1 with `schema`; exit 2 `receipt-unreadable`); drift `--selftest` exit 0 with 0 fixture trees left. |
| R89Review1 | reviewer | counting command `clean`/107 from committed bytes; 8/8 freeze pins; fixture sha re-derived out-of-band to `69acad57…`. |
| R89Review2 | reviewer | 24 receipt mutations: 15 caught, 9 not — the settle re-read, the snapshot identity and the answer's own provenance are unenforced; attribution narrowed. |
| R89Critic | critic | fixture-emulated vocabulary; `replay-limit-consistency` restates the math; the law direction holds at scoped strength. |
| R89Mut1 | mutation-tester | 44 independent mutants: 9 killed, 35 survived, 0 crashed; 16 survivors are witnessed real acceptance gaps (named clauses), not general conjunct resistance. |
| R89Scout | scout | S223/S219/S224 re-opened byte-identically (cmp IDENTICAL); the dfn wording confirmed in place; the case rule located in Infra. |
| R89Scribe | scribe | independent records; F1–F10 record defects (F1/F2 made a claim leg false at the frozen bytes) — both repaired before filing. |
| R89Connector | connector | 21-lane / ~1,800-file scan: zero capability overlap on accept/showPicker/domRead/setFileInputFiles; this lane is the sole owner. |
| R89Sentinel | sentinel | 9 audit axes: S1–S6 HIGH/MEDIUM found (repaired at D5), S7 controls reproduced, S9 CLEAN. |
| R89Simplifier | simplifier | five frozen-state blockers, four repaired in D2–D5 and verified live; one duplicate-authority pair retained as a carried narrowing. |

## Pre-file falsification ledger

`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 89` →
`PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=6 findings=0` (exit 0). The ledger
`.ufo/waves/round-89/claim-falsification.tsv` carries 12 rows over both claims; all six attack
seats (Connector, Critic, Mut1, Review1, Review2, Sentinel) are read; the two
`falsifies-wording` rows point at the narrowings, and the one `falsifies-number` row points at the
disclosed numeral correction.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — §Round 89 gate registry + the r89 instruments; verifier: none new this round (the r88 spot-check's `[~]` stands).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the scored receipt + `w1/R89Exec1.md` cold runs; LOG round 89.
- [~] Instructions executable by an agent without oral context — `w1/R89Exec_{1,2,3}.md` executed the frozen commands from the prompt alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/R89Connector.md` sibling scan: zero overlap, this lane the sole owner; nothing absorbed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Lane branch `master`.

## Tooling

No tool was installed or upgraded this round. `pacman` stayed paused; every seat used the host's
existing node v24.21.0 and python3. The `/home/vgpnk/.omp/agent/RULES.md` read was honored
(pacman guard applied; no install needed).
