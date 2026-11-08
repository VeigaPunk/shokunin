# tabi — round 85 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 85, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `c574d593` (lane clean, `jj-lane.sh state` ahead=0 behind=0). **Freeze commit:** `5c19615`
(D1 `dbecb1a18905`). **Lane tip:** `e6b53ec9` (pushed; `ls-remote origin refs/heads/master` prints it). **D2:** `620623a43f74`, nonce **`tabi-r85-l1-620623a43f74`** (re-freeze before any
record was scored; `plans/round-85.md` §Re-freeze history). **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 works a lowest axis and is a capability move):

- **C1 — coverage (9): capability `chromium-showpicker-linux`, generation r85.** The r84 note's named
  frontier — "a same-origin `type=tel`/`search`/`text` trigger (error or silent no-op) for contrast with
  the cross-origin path" — is now measured twice: three same-origin legs with no transient activation
  and three after a real trusted click on the neutral `#pad`. 24 legs; 87 checks.
- **C2 — operability (9): the r84 survivor-family witnesses.** Six single-conjunct weakenings of the
  cross-origin law block that R84Mut1's independent sweep routed to r85, re-applied to the r84 and the
  r85 counters and scored with each generation's frozen battery.

Round shape: **ONE v1 wave, 10 seats** (`ufo-swarm-wave.mjs run` → 10 spawn, 0 resume; dispatch
`.ufo/waves/round-85/w1-dispatch.json`, `.ready` written, results `.ufo/waves/round-85/w1-results.json`).
Roles: 3 executor (R85Exec1/2/3), 2 reviewer (R85Review1/2), 1 critic, 1 mutation-tester, 1 scout,
1 scribe, 1 connector — **4 attack seats of 10 (40 %)**, 1 connector. The L1 holds the planner seat;
no planner was dispatched (validator rejects `planner`). Round total 10 seats; no residual call.
No seat died.

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`5c19615`, pins in `.ufo/waves/round-85/freeze.txt`, sha256
  `620623a43f74…`): `scripts/chrome-cdp-showpicker-round85.mjs` (24 legs; six new legs at lines
  191–196; parent inputs `#tes`/`#ses`/`#txs` at left 100/300/500, top 750), `scripts/check-showpicker-r85.mjs`
  (87 checks; `NO_PICKER` set line 146, `same-origin-no-picker-law` line 654), battery (175 cases),
  kill power (58 mutants), selftest, `scripts/witness-families-r85.mjs`, `scripts/check-record-drift-r85.mjs`.
- **Scored receipt** `corpus/evidence/round85/chromium-showpicker/receipt.json`: nonce
  `tabi-r85-l1-620623a43f74`, 24 legs, `failures: []`, fixture `0b012937…`, child fixture `cf492566…`
  (driver `1690c63d…`); scored at the D2 nonce after the re-freeze.
- **Six new legs measured**: `sp85-same-origin-{tel,search,text}` → `{ok:false,name:'NotAllowedError'}`
  with activation `{false,false}→{false,false}`, 0 choosers; `-activated` → `{ok:true,ret:'undefined'}`
  with `{true,true}→{false,true}`, 0 choosers. `w1/R85Exec1.md` (two cold runs, all six records
  identical across runs), `w1/R85Exec2.md`.
- **Leg (b)**: battery 175/0/coverage 87/87, kill power 58/58/0/0/0, selftest 9/9 —
  `scored/{battery-a,killpower-a,selftest}.json`; independently re-run by R85Exec2 (`w1/R85Exec2.md`).
- **C2 before/after**: `scored/witness-a.json` — before 3 survivors (`cross-access-dropped`,
  `cross-childseq-dropped`, `cross-childact-before-dropped`), after 0; reproduced by R85Exec3's
  hand-edit path (`w1/R85Exec3.md` §2) and causally by R85Review2 (battery minus the six → the same
  three survive, `w1/R85Review2.md` §3).
- **Do-nothing control** (before the score): `controls/c1/nowork-r84-under-r85.json` — the r84 scored
  receipt under the r85 counter: exit 1, 81 checks, 21 findings.
- **Adversarial seats**: R85Review1 (four MEDIUM + two LOW findings; false-green table, §2),
  R85Review2 (per-case ids and the causal test), R85Critic (confound, limit escape reproduction,
  C2 accounting), R85Mut1 (independent mutant sweep, `w1/R85Mut1.md`).
- **Sources**: the L1 re-opened S219 itself (WHATWG input page, HTTP 200, 687,515 B, sha256
  `b0202de1c0b4…`, 19-word located quote in the lesson Gate); R85Scout re-opened S219/S220/S218 and
  located the `showPicker()` chain (`w1/R85Scout.md`).
- **Frontier step**: census start/end exit 0, 223 rows both ends; knowledge 97 → 98; three rejects
  with flips in the lesson Gate; no new registry rows (carried rows re-opened).
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no lane-written stray
  at the fleet root (see Round extras).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `scripts/chrome-cdp-showpicker-round85.mjs` (24 legs; six same-origin arms), `scripts/check-showpicker-r85.mjs` (87 checks; `NO_PICKER`, `same-origin-no-picker-law`), `scripts/negatives-showpicker-r85.mjs` (175 cases incl. the six `cross-tel-*` family cases), `scripts/kill-power-r85.mjs` (58 mutants), `scripts/selftest-r85-gates.mjs`, `scripts/check-record-drift-r85.mjs`, `scripts/witness-families-r85.mjs` | LOG round 85 | freeze `5c19615` (D1) → re-freeze commit carries D2 `620623a43f74` |
| `.ufo/waves/round-85/{freeze.txt,claims.json,controls/,census/start.txt}` — frozen claims, pins, prior set, pre-freeze probe, do-nothing controls | LOG round 85 | `5c19615` |
| `corpus/evidence/round85/chromium-showpicker/receipt.json` — the scored receipt at nonce `tabi-r85-l1-620623a43f74` (24 legs, 0 failures) | LOG round 85 | round commit |
| `.ufo/waves/round-85/{w1-spec.json,w1-dispatch.json,w1.ready,w1/,scored/,claim-falsification.tsv,census/end.txt}` — wave evidence and scored outputs | LOG round 85 | round commit |
| `corpus/knowledge/chromium-showpicker-runtime-round-85.md` (knowledge 97 → 98), `corpus/lessons/round-85.md`, `plans/round-85.md`, `SCORECARD.md` round-85 section + two capability rows, `SKILL.md` §Round 85 gate registry, `LOG.md` round-85 entry | LOG round 85 | round commit |

## Before → after measurements

**C1 — coverage.** Counting command (frozen; SCORECARD row carries the hardcoded fixture pin):

```
node scripts/check-showpicker-r85.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round85/chromium-showpicker/receipt.json \
  --expect-driver-sha256 1690c63d14447a08ea9fe915a49d317e2953c5fb08e064e8f160a100089ab8ee \
  --expect-nonce tabi-r85-l1-620623a43f74 \
  --expect-fixture-sha256 0b0129377711954ddae722a7ad6db8f00f5eb94759ef45786f21b6eede3d252a \
  --prior-set .ufo/waves/round-85/controls/c1/prior-set.txt --json
```

- before: no r85 receipt → exit 2 `receipt-unreadable` (`controls/c1/noreceipt.txt`); the r84 scored
  receipt under the r85 counter → exit 1, **81** checks, **22** findings
  (`controls/c1/nowork-r84-under-r85.json`).
- after: exit 0, `verdict: clean`, **checkCount 87**, 0 findings (`scored/counter-a.json`), measured
  against the round-85 commit. Leg (b): battery **175 cases / 0 failed / coverage 87/87**
  (`scored/battery-a.json`), kill power **58 mutants / 58 killed / 0 survivors / 0 crashed / 0
  unapplied** (`scored/killpower-a.json`), selftest **9/9** (`scored/selftest.json`).

**C2 — operability.** Counting command:

```
node scripts/witness-families-r85.mjs --lane <ABS lane> --work <ABS scratch> --json
```

- before (frozen r84 D battery, `scripts/negatives-showpicker-r84.mjs` + `check-showpicker-r84.mjs`
  + the r84 scored receipt): **3 of 6 families survive** — `cross-access-dropped`,
  `cross-childseq-dropped`, `cross-childact-before-dropped`.
- after (frozen r85 battery + counter): **0 of 6 survive**, 6 killed, 0 crashed, 0 unapplied
  (`scored/witness-a.json`), measured against the round-85 commit. Reproduced independently by
  R85Exec3's hand-edit path (`w1/R85Exec3.md` §2) and causally by R85Review2 (`w1/R85Review2.md` §3:
  battery minus the six cases → the same three survive).

## Sources & frontier

`SOURCES.md` rows before → after: **223 → 223** (no new rows). Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
— start exit 0, end exit 0 (`census/start.txt`, `census/end.txt`), 223 rows both ends. Rows touched
old→new: none (no `status`/`recheck`/`used-by` change this round; rows are append-only and none
needed a status move). Rows added by tier: A 0, B 0, C 0. Carried rows **re-opened this round**: S219
(the L1 itself: HTTP 200, 687,515 B, sha256 `b0202de1c0b4…`, `showPicker()` steps located, 19-word
quote in the lesson Gate), S220/S218 (`html_input_element.cc` at tag 155.0.8059.84, R85Scout), S221/S222
(CDP Page/DOM domains). Frontier rows advanced: **one** — the r84 note's "same-origin tel/search/text
trigger for contrast" moved from frontier to measured core (six legs, one new law); the `accept`
MIME-token / `image/*` grammar stays frontier with flips (lesson Gate rejects).

`Assimilation: none` — `merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`;
`considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion: improved** — knowledge 97 → 98, and the six new legs move the r84 note's named frontier
  into measured core with a new gated law (`same-origin-no-picker-law`); C2 adds a capability row
  (`battery-survivor-witnesses`). Evidence: `scored/counter-a.json` (87 checks),
  `corpus/knowledge/chromium-showpicker-runtime-round-85.md`.
- **quality: improved** — three real trigger classes added to the battery (access/childseq/childact),
  three routed r84 defects closed (contrast leg, family witnesses, limit-sentence control re-derived),
  and the counter/battery/kill-power family re-frozen as one generation. Evidence:
  `scored/battery-a.json`, `scored/killpower-a.json`, `w1/R85Review2.md` §3.
- **discernment: improved** — the round's own wave falsified C1's wording twice (no-picker inference;
  origin-determination needs `given activation`) and C2's novelty claim (three of six cases duplicate
  pre-existing triggers), and both narrowings are recorded in `plans/round-85.md` **before** filing;
  the D1→D2 re-freeze is recorded with its cause rather than hidden. Evidence: `w1/R85Critic.md` §1,
  `w1/R85Review1.md` §1, `plans/round-85.md` §Narrowings.

| axis | verdict |
|---|---|
| coverage | improved |
| calibration | improved |
| depth | unchanged |
| operability | improved |
| freshness | unchanged |
| adjacency | unchanged |

**Wave w1 seat ledger** (`w1-results.json`: 10 seats, 0 dead): R85Exec1 (executor — two cold runs,
all six new records identical), R85Exec2 (executor — battery/kill power/selftest, green at D1; its
`record-drift` gate red is the mid-wave re-freeze, narrowing 5), R85Exec3 (executor — witness
before/after and the forgery controls), R85Review1 (reviewer — four MEDIUM + two LOW), R85Review2
(reviewer — per-case ids and the causal test), R85Critic (critic — confound, limit escape, C2
accounting), R85Mut1 (mutation-tester — 73 independent mutants: 22 killed, 31 case-level survivors),
R85Scout (scout — spec/Chromium quotes, TYPE-vs-early-return answer), R85Scribe (scribe — drafts plus
two record-drift findings), R85Connector (connector — 20 sibling heads pinned, no contested row).
Attack seats 4/10 (40 %); connector seats 1; no residual call.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `scripts/chrome-cdp-showpicker-round85.mjs` (24 legs; six same-origin arms), `scripts/check-showpicker-r85.mjs` (87 checks; `NO_PICKER`, `same-origin-no-picker-law`), `scripts/negatives-showpicker-r85.mjs` (175 cases incl. six `cross-tel-*` family cases), `scripts/kill-power-r85.mjs` (58 mutants), `scripts/selftest-r85-gates.mjs`, `scripts/check-record-drift-r85.mjs`, `scripts/witness-families-r85.mjs` | LOG round 85 | freeze `5c19615` (D1) → re-freeze + round work `c8876299`, closing commit **`e6b53ec9`** (D2 `620623a43f74`); lane tip = remote tip |
| `.ufo/waves/round-85/{freeze.txt,claims.json,controls/,census/start.txt}` — frozen claims, pins, prior set, pre-freeze probe, do-nothing controls | LOG round 85 | `5c19615` |
| `corpus/evidence/round85/chromium-showpicker/receipt.json` — scored receipt, nonce `tabi-r85-l1-620623a43f74`, 24 legs, 0 failures | LOG round 85 | `c8876299` (final tip `e6b53ec9`) |
| `.ufo/waves/round-85/{w1-spec.json,w1-dispatch.json,w1.ready,w1/,scored/,census/end.txt,claim-falsification.tsv}` — wave evidence, scored outputs, ledger | LOG round 85 | `e6b53ec9` |
| `corpus/knowledge/chromium-showpicker-runtime-round-85.md` (knowledge 97 → 98), `corpus/lessons/round-85.md`, `plans/round-85.md`, `SCORECARD.md` round-85 section + two capability rows, `SKILL.md` §Round 85 gate registry, `LOG.md` entry | LOG round 85 | `e6b53ec9` |

## Before → after measurements

**C1 — coverage.** Frozen counting command (SCORECARD row hardcodes the fixture pin):

```
node scripts/check-showpicker-r85.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round85/chromium-showpicker/receipt.json \
  --expect-driver-sha256 1690c63d14447a08ea9fe915a49d317e2953c5fb08e064e8f160a100089ab8ee \
  --expect-nonce tabi-r85-l1-620623a43f74 \
  --expect-fixture-sha256 0b0129377711954ddae722a7ad6db8f00f5eb94759ef45786f21b6eede3d252a \
  --prior-set .ufo/waves/round-85/controls/c1/prior-set.txt --json
```

- before: no r85 receipt → exit 2 `receipt-unreadable` (`controls/c1/noreceipt.txt`); the r84 scored
  receipt under the r85 counter → exit 1, **81** checks, 22 findings
  (`controls/c1/nowork-r84-under-r85.json`).
- after: exit 0, `verdict: clean`, **checkCount 87**, 0 findings (`scored/counter-a.json`), against the
  round-85 commit. Leg (b): battery **175 cases / 0 failed / coverage 87/87**
  (`scored/battery-a.json`), kill power **58 mutants / 58 killed / 0 survivors / 0 crashed / 0
  unapplied** (`scored/killpower-a.json`), selftest **9/9** (`scored/selftest.json`).

**C2 — operability.**

```
node scripts/witness-families-r85.mjs --lane <ABS lane> --work <ABS scratch> --json
```

- before (frozen r84 D battery `42fcfedc…` + r84 counter `e88e9fc7…` + the r84 scored receipt):
  **3 of 6 families survive** — `cross-access-dropped`, `cross-childseq-dropped`,
  `cross-childact-before-dropped`.
- after (frozen r85 battery + counter): **0 of 6 survive**, 6 killed, 0 crashed, 0 unapplied
  (`scored/witness-a.json`), against the round-85 commit. Reproduced by R85Exec3's hand-edit path
  (§2) and causally by R85Review2 (§3: battery minus the six cases → the same three survive).

## Sources & frontier

`SOURCES.md` rows before → after: **223 → 223**, no new rows. Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
— start exit 0, end exit 0 (`census/start.txt`, `census/end.txt`), 223 rows both ends. Rows touched
old→new: none. Rows added by tier: A 0 / B 0 / C 0. Carried rows **re-opened this round**: S219 (the
L1 itself: HTTP 200, 687,515 B, sha256 `b0202de1c0b4…`, `showPicker()` steps, 19-word quote in the
lesson Gate), S220/S218 (`html_input_element.cc` at 155.0.8059.84, R85Scout, `w1/R85Scout.md` §0),
S221/S222 (CDP Page/DOM domains). Frontier rows advanced: **one** — "same-origin tel/search/text
trigger for contrast" moved frontier → measured core (six legs, one new law); the `accept` MIME-token /
`image/*` grammar stays frontier with flips (lesson Gate).

`Assimilation: none` — `merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`;
`considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion: improved** — knowledge 97 → 98; six new legs move the r84 note's named frontier into
  measured core with a new gated law; a new capability row (`battery-survivor-witnesses`). Evidence:
  `scored/counter-a.json`, `corpus/knowledge/chromium-showpicker-runtime-round-85.md`.
- **quality: improved** — three genuinely new trigger classes in the battery (access/childseq/
  childact-before), three routed r84 defects closed, and the counter/battery/kill-power family frozen
  as one generation. Evidence: `scored/{battery-a,killpower-a}.json`, `w1/R85Review2.md` §3.
- **discernment: improved** — the wave falsified C1's wording twice (no-picker inference;
  origin-determination needs `given activation`), C1's kill-power reach, and C2's novelty claim; all
  five narrowings are recorded in `plans/round-85.md` **before** filing, plus two record-drift fixes
  the Scribe and Review1 measured. Evidence: `w1/R85Critic.md` §1, `w1/R85Review1.md` §1,
  `w1/R85Mut1.md`, `w1/R85Scribe.md`, `plans/round-85.md` §Narrowings.

| axis | verdict |
|---|---|
| coverage | improved |
| calibration | improved |
| depth | unchanged |
| operability | improved |
| freshness | unchanged |
| adjacency | unchanged |

## Pre-file falsification ledger

```
$ python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tabi --round 85
PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=5 findings=0     (exit 0)
```

The ledger `.ufo/waves/round-85/claim-falsification.tsv` covers C1 and C2 and reads every attack seat
(R85Review1, R85Review2, R85Critic, R85Mut1, R85Connector) plus the exec/scout/scribe seats. Six
`falsifies-wording` rows point at the amendments in `plans/round-85.md` §Narrowings; the rest are
`neutral` with what they attacked named.

## Narrowings recorded before filing (detail in `plans/round-85.md` §Narrowings)

1. C1's origin-determination is narrowed to **given activation, for these types, type attribute held
   constant** — 3-cell design, different elements (Critic, Review1).
2. "These types have no picker" is an **inference** from `undefined` + zero choosers (Review1,
   Scribe).
3. `fixture.child.sha256` is shape-checked only; `claims.json`'s command carries the fixture pin as a
   template slot (Review1).
4. C2's **novelty is three trigger classes**, not six (Review2, Exec3).
5. The scored receipt was **re-executed mid-wave** (D1→D2): Exec2's `record-drift` red and Review2's
   scratch recovery are consequences, not defects; the L1's post-freeze selftest is 9/9 at D2.
6. Cold runs cannot be `clean` while the in-tree scored receipt is undeclared (`prior-set-complete`);
   Exec1's runs pass every law.
7. **Kill-power reach**: the frozen 58-mutant list is killed; R85Mut1's independent 73-mutant sweep
   leaves 31 case-level survivors (new-leg law members, `NotAllowedError` name/message on the six
   legs, `sp85-*` per-leg shape fields). Routed to r86.
8. **C2's witnesses are tel-only** — a law narrowed to the tel leg survives the battery (Mut1).
9. **The zero-chooser metric is a FILE-chooser metric** — tel/search/text still issue a datalist
   request in Chromium, so "no popup of any kind" is not measured (Scout).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` §Round 85 gate registry (seven instruments with entry commands and verdict maps) plus
  the carried §Approval table; no non-author verdict is claimed for this box.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 24-leg generation r85
  run (one fresh browser per leg, real CDP clicks, a cross-origin iframe) scored clean at 87 checks;
  `LOG.md` round-85 entry, `corpus/evidence/round85/chromium-showpicker/receipt.json`.
- [~] Instructions executable by an agent without oral context — the ten seat prompts carry every
  absolute path, pin and command; R85Exec1/R85Exec2/R85Exec3/R85Scribe reproduced the measurements
  from them alone (`w1/R85Exec{1,2,3}.md`, `w1/R85Scribe.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round adds loopback-only CDP ground;
  R85Connector's 20-head sibling table (`w1/sibling-heads-r85.tsv`) finds no contested row on these
  findings, and the refusal routes are unchanged.

## Round extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (pacman paused host-wide per the addendum; no `uv`/`npx`/binary install was
  needed). Nothing to record.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator
  state (`.scratch/run15-*`, `.ufo/l0-questions.md`) and an unrelated `.ufo/reports/round-100/mado.md`;
  no seat wrote a lane/round-named file at the fleet root, so nothing was copied back or deleted.
- **Seat notes:** the freeze commit `5c19615` carries the pre-freeze probe receipt at the scored path;
  the round commit replaces it with the D2 scored receipt at the same path (the prior-set walk refuses
  a second in-tree receipt, so replacement — not addition — is the cutover; R85Review1 MEDIUM-1 flagged
  this mid-round). R85Exec2 and R85Scribe read the lane during the D1→D2 window; their D1 figures are
  recorded as pre-amendment evidence.
- **L0 side channel:** no new question this round; the standing `tabi | round-57` (assimilation) and
  `tabi | round-44` (L2 floor) questions stay open and were routed around, not answered.
