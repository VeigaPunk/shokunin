# tabi — round 87 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 87, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `24765dd9` (lane clean). **Freeze commit:** `79b5cd13`; **lane tip:** `a53b01a1`
(pushed; `ls-remote origin refs/heads/master` prints it). **D:** the scored receipt is D3
`3dd4b0802d67`; D4 `b1d06cf8db57` re-froze only the selftest runner (path fix), D5 `c921658c6046` the drift gate (R87Critic C2-3/C2-4), D6 `6d4a63d29e0c` a tenth selftest gate
(R87Sentinel F3), and D7 `c858c91ec04d` the drift gate's item-heading and directional-scope repairs
(R87Mut1 D07/D09) — `plans/round-87.md` §Re-freeze history. **Nonce:** `tabi-r87-l1-3dd4b0802d67`. **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 works a lowest axis and is a capability move):

- **C1 — coverage (9): capability `chromium-showpicker-linux`, generation r87.** The four remaining
  `accept` token forms the r86 note named as frontier are measured, one page input each:
  `audio/*` ← `image/png`, `video/*` ← `text/plain`, a multi-MIME list `image/png,application/pdf`
  ← `text/plain`, and the whitespace variant `"  image/png ,  .txt  "` ← `image/png`. Every raw
  attribute is read back from the page; every delivered file lands in the input with its bytes,
  trusted `input`+`change`, and page-read hex. 34 legs; 99 checks.
- **C2 — calibration (9): the five lane-owned record defects of the round-86 non-author spot-check.**
  `scripts/check-record-drift-r87.mjs` counts five record statements against repo state
  (accept-headline sweep, the two round-86 `## Mistakes` evidence pointers, the round-86 SOURCES
  search-log entry, the round-86 ledger pointer, and this round's r86-report corrections). Before
  (base worktree) 5 mismatches; after 0.

Round shape: **ONE v1 wave, 11 seats** (`ufo-swarm-wave.mjs run` → `counts.spawn 11`; dispatch
`.ufo/waves/round-87/w1-dispatch.json`; `.ready` taken by the dispatcher at 07:13:59; results
`.ufo/waves/round-87/w1-results.json`). Roles: 3 executor (R87Exec1/2/3), 2 reviewer
(R87Review1/2), 1 critic, 1 mutation-tester, 1 scout, 1 scribe, 1 connector, 1 sentinel —
**5 attack seats of 11 (45 %)**, 1 connector (policy cap 2). The L1 holds the planner seat; no
planner was dispatched (the validator rejects `planner`). Round total 11 seats; no residual call;
dead seats: none — all 11 seats settled and filed (R87Scribe, the last handle, stayed live-but-unfiled for ~20 min after the other ten settled and filed before the wave was settled).

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`.ufo/waves/round-87/freeze.txt`, D7 `c858c91ec04d`):
  `scripts/chrome-cdp-showpicker-round87.mjs` (34 legs; four new parent inputs `#aa`/`#av`/`#a2`/
  `#aws`, four new `sp87-accept-*` legs), `scripts/check-showpicker-r87.mjs` (99 checks; the
  `accept-grammar-law` table extended to seven matrix forms over eight raw strings),
  `scripts/negatives-showpicker-r87.mjs` (209 cases, coverage 99/99),
  `scripts/kill-power-r87.mjs` (66 mutants), `scripts/selftest-r87-gates.mjs` (10 gates),
  `scripts/check-record-drift-r87.mjs` (5 statements).
- **Scored receipt** `corpus/evidence/round87/chromium-showpicker/receipt.json`: nonce
  `tabi-r87-l1-3dd4b0802d67`, 34 legs, `failures: []`, fixture `10e444f7…`, driver `7c54e786…`.
- **The four new legs measured** (receipt; reproduced in two cold runs by `w1/R87Exec1.md` §3):
  `sp87-accept-audio-png` (`aa`, `audio/*` ← `tabi-r87-b.png`), `sp87-accept-video-text` (`av`,
  `video/*` ← `tabi-r87-a.txt`), `sp87-accept-multimime-text` (`a2`, `image/png,application/pdf` ←
  `tabi-r87-a.txt`), `sp87-accept-whitespace-png` (`aws`, `"  image/png ,  .txt  "` ←
  `tabi-r87-b.png`). Each: `showPicker {ok:true, ret:'undefined'}`, one `Page.fileChooserOpened`
  (`selectSingle`), trusted `input`+`change`, page `read` hex of the delivered bytes, and the
  input's `files` list carrying the file.
- **Leg (b)**: counter `clean` / 99 checks; battery 209 cases / 0 failed / coverage 99/99; kill
  power 66 mutants / 66 killed / 0 survivors / 0 crashed / 0 unapplied; selftest 10/10 at D7 over the
  D3 receipt — `scored/{counter-a,battery-a,killpower-a,selftest}.json`.
- **C2 record fixes** (defects 3/4/5/7 closed; 1–2 carried into this round's records):
  `SKILL.md` and `plans/round-86.md` restated to "not a validator on a programmatic answer"
  (+ `QUALITY.md` 161); the two round-86 `## Mistakes` rows repointed to
  `.ufo/waves/round-86/lesson-proof/README.md` (states the transcript was not retained); the
  round-86 `## Search log` entry added at `corpus/SOURCES.md:300`; `plans/round-86.md` §Narrowings
  item 9 added and the round-86 ledger's Scribe row repointed to it; the round-86 report's 39→40
  count and S221/S222 carried-not-reopened corrections recorded in `corpus/lessons/round-87.md`.
  `scored/drift-a.json` → 5 claims, 0 mismatches; `scored/drift-before.json` → 5 mismatches on the
  base worktree.
- **Do-nothing controls**: `controls/c1/nowork-r86-under-r87.json` — the r86 scored receipt under
  the r87 counter: exit 1, 95 checks, 47 findings including `schema`, `plan-frozen`, leg records
  (reproduced byte-identically by `w1/R87Exec3.md` §3); `controls/c1/noreceipt.txt` — exit 2
  `receipt-unreadable`.
- **Cold-run reproduction**: `w1/R87Exec1.md` — two fresh-nonce runs (34/34 legs, 0 failures), each
  98/99 true with only the declaration finding `prior-set-complete`.
- **Adversarial seats**: `R87Review1` (count reproduction, pin audit, `F1–F4`), `R87Review2`
  (62-variant new-leg attribution attack, `F1–F7`), `R87Critic` (13 attack verdicts; C1-2/C1-3/
  C2-3/C2-4 falsified the record wording and were repaired or narrowed), `R87Mut1`, `R87Sentinel`,
  `R87Connector` (21-lane scan: zero overlap, uncontested) — under `.ufo/waves/round-87/w1/`.
- **Sources**: the L1 re-opened S223/S219 on 2026-11-08 (WHATWG input page, HTTP 200, 687,515 B,
  sha256 `b0202de1c0b4…`, staged `.ufo/waves/round-87/sources/whatwg-input.html`); R87Scout
  re-fetched it byte-identically and opened three further parse-semantics pages (excluded as
  registry rows; `w1/R87Scout.md` §3).
- **Frontier step**: census start/end exit 0, 223 rows both ends; knowledge 99 → 100; two rejects
  with flip conditions in the lesson Gate; no new registry rows.
- **Corrections the wave forced** (`corpus/lessons/round-87.md` §Corrections): the C1 counting
  command's superseded nonce; the "selftest green" leg measured at the final freeze (D7) rather than the D3 pin;
  the round-86 ledger pointer repointed to item 9; the drift gate's directional 39→40 check; and
  the narrowing of the page-read/pin/provenance clauses (plans §Narrowings 6–11).
- **Seat ledger (11 seats, all filed):**

| seat | role | key result |
|---|---|---|
| R87Exec1 | executor | two fresh-nonce cold runs: 34/34 legs, 0 failures, 98/99 checks each; only the declaration finding `prior-set-complete`; the four new legs' facts reproduced identically. |
| R87Exec2 | executor | leg (b) reproduced: battery 209/0/coverage 99/99, kill power 66/66/0/0/0, selftest 9/9 at D4; only the kill-power `results` array order varies across runs. |
| R87Exec3 | executor | C2 BEFORE 5 mismatches on a clean base worktree, AFTER 0; both do-nothing C1 controls reproduced (exit 1 / 47 findings; exit 2 `receipt-unreadable`); caught the stale counting-command nonce and the controls-ordering wording. |
| R87Review1 | reviewer | counting command `clean` / 99 from committed bytes; six pins match; F1 pin echoes, F2 per-leg descriptors unwitnessed, F3 read `isTrusted` fixture-authored, F4 stale nonce (fixed). |
| R87Review2 | reviewer | 62 receipt variants: 30/30 law-or-send-log moves refused, 30/30 unbound leaf fields clean; F1 page-read act optional, F2 `fixture.patch.*` unbound, F3 per-leg copies dead data, F4/F5 source inventory/path, F6 child sha shape-only. |
| R87Critic | critic | 13 attack verdicts: C1-2 (counting-command nonce), C1-3 (selftest at the D3 pin), C2-3 (ledger pointer item 1), C2-4 (directionless 39/40) — each repaired or narrowed; the law itself uncontradicted. |
| R87Mut1 | mutation-tester | C1: 25 mutants, 19 killed / 5 survived / 1 crashed; four whole-counter escapes narrowed (item 14). C2: 13 mutants; D07 (item heading) and D09 (count direction) passed the D5 gate — repaired at D7 with fail-able proofs. |
| R87Scout | scout | staged page byte-identical to live (cmp exit 0); 18/20/16/12/21/21/19/10-word located quotes; the whitespace-normalization rule is off-page, so the law stays acceptance-only. |
| R87Scribe | scribe | independent note/lesson/SCORECARD/LOG drafts; five divergences (note limits section, S219 quote form, D-digest list, 9-vs-10 gate wording, `digestsCommit`), all reconciled in the final records. |
| R87Connector | connector | 21-lane / 1,816-file scan: zero capability overlap on accept/showPicker/setFileInputFiles; the four token forms are uncontested. |
| R87Sentinel | sentinel | five surfaces PASS on the final snapshot (pins, receipt identity incl. independently re-derived fixture/child hashes, census, no out-of-lane writes, controls); F1 pins-in-no-commit (fixed by `79b5cd13`), F3 exit-2 control ungated (fixed by D6), F6 selftest identity self-reference (narrowing 15). |

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `scripts/chrome-cdp-showpicker-round87.mjs` (34 legs), `scripts/check-showpicker-r87.mjs` (99 checks), `scripts/negatives-showpicker-r87.mjs` (209 cases), `scripts/kill-power-r87.mjs` (66 mutants), `scripts/selftest-r87-gates.mjs` (10 gates), `scripts/check-record-drift-r87.mjs` (5 statements) | LOG round 87 | `79b5cd13` |
| `.ufo/waves/round-87/{freeze.txt,claims.json,controls/,census/,sources/,scored/,w1-spec.json,w1-dispatch.json,w1.ready,w1/,w1-results.json,claim-falsification.tsv}` | LOG round 87 | `79b5cd13`/`a53b01a1` |
| `corpus/evidence/round87/chromium-showpicker/receipt.json` — the scored receipt at nonce `tabi-r87-l1-3dd4b0802d67` (34 legs, 0 failures) | LOG round 87 | `79b5cd13` |
| `corpus/knowledge/chromium-showpicker-runtime-round-87.md` (knowledge 99 → 100), `corpus/lessons/round-87.md`, `plans/round-87.md`, `SCORECARD.md` round-87 section + capability row, `SKILL.md` §Round 87 gate registry, `LOG.md` round-87 entry | LOG round 87 | `a53b01a1` |
| the r86 routed record fixes: `SKILL.md`, `plans/round-86.md`, `corpus/lessons/round-86.md`, `corpus/SOURCES.md`, `corpus/QUALITY.md` 161, `.ufo/waves/round-86/lesson-proof/README.md`, `.ufo/waves/round-86/claim-falsification.tsv` | LOG round 87 | `a53b01a1` |

## Before → after measurements

**C1 — coverage.** Counting command (frozen; the fixture value is the scored receipt's own, as the
sealed command names it):

```
node scripts/check-showpicker-r87.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round87/chromium-showpicker/receipt.json \
  --expect-driver-sha256 7c54e786d78d455b955e822deb4bf0419b85c4859c5287c27380d6b568389e5f \
  --expect-nonce tabi-r87-l1-3dd4b0802d67 \
  --expect-fixture-sha256 10e444f7fb840b6e132b4570794d3a0ed6f5db0781ca490a986685505e8d94c4 \
  --prior-set .ufo/waves/round-87/controls/c1/prior-set.txt --json
```

- **Before** (base `24765dd9`): no r87 receipt → exit 2 `receipt-unreadable`
  (`controls/c1/noreceipt.txt`); the r86 scored receipt under the r87 counter → exit 1, 95 checks,
  47 findings including `schema`, `plan-frozen`, `leg-order`, leg records
  (`controls/c1/nowork-r86-under-r87.json`).
- **After** (D3 receipt; D7 instrument set): exit 0, `verdict clean`, **99 checks**, 0 findings;
  battery 209/0/coverage 99/99; kill power 66/66/0/0/0; selftest 10/10. Measured at commit
  `79b5cd13`.
- Independent reproduction: `w1/R87Exec2.md` re-ran battery/kill-power/selftest; `w1/R87Review1.md`
  re-ran the counting command from committed bytes (`clean`, 99); `w1/R87Exec1.md` cold runs agree
  on every law check (98/99 each, only the declaration `prior-set-complete`).
- **Narrowed** (the wave's F-rows): the driver/fixture pins are declaration-level (Review1 F1),
  the page-read act is not required and `fixture.patch.*` is unbound (Review2 F1/F2), and per-leg
  descriptor copies are dead data (Review2 F3/Review1 F2) — `plans/round-87.md` §Narrowings 6–11.
  R87Sentinel independently re-derived the fixture and child hashes from the pinned driver +
  template + nonce/child port (`10e444f7…` / `bbb22189…`), so the fixture pin is verifiable even
  though the counter does not check it.

**C2 — calibration.** Counting command:

```
node scripts/check-record-drift-r87.mjs --lane <ABS lane> --json
```

- **Before** (base `24765dd9` worktree): exit 1, claims 5, **5 mismatches** — `accept-headline`,
  `mistake-evidence`, `sources-searchlog`, `ledger-pointer`, `report-corrections`
  (`scored/drift-before.json`; independently reproduced by `w1/R87Exec3.md` §1).
- **After**: exit 0, **0 mismatches** (`scored/drift-a.json`), measured at `79b5cd13`.
- **Narrowed**: the ledger-pointer statement is enforced as "the row names §Narrowings item 9 and
  the section carries the headline item" (R87Critic C2-3), and the 39→40 statement is a directional
  regex (C2-4); the before-value counts the complete record fix, including the two files introduced
  this round (R87Exec3 §1).

## Sources & frontier

- **Census** (frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
  start exit 0 (`census/start.txt`, 223 rows), end exit 0 (`census/end.txt`, 223 rows).
- **Rows before → after:** 223 → 223. Rows added by tier: none. Rows touched old→new: none by
  status/recheck/`used-by` — S223 and S219 were **re-opened** (access date 2026-11-08, located
  quotes in the lesson Gate) and S221/S222 were **carried, not re-opened** (no `.pdl` fetched).
  The round-86 bounded re-opening is recorded at `corpus/SOURCES.md:300` (spot-check defect 5).
- **Frontier rows advanced:** the r86 note's remaining `accept` token forms (audio, video,
  multi-MIME, whitespace) moved from frontier to measured core; the two rejects (full grammar, and
  dialog filtering) carry flip conditions in `corpus/lessons/round-87.md` §Gate.
- **Assimilation:** none (`merge/tabi/` adoption stays closed pending the open L0
  `tabi | round-57`); `considerthese/` — no such directory in this lane.

## Trend verdicts

- **expansion: improved** — knowledge 99 → 100 (`git ls-tree -r --name-only <rev> corpus/knowledge/ | wc -l`);
  four named frontier token forms move to measured core; one capability row enters SCORECARD.
- **quality: improved** — the frozen family re-derives 99/99 checks with battery 209/0 and kill
  power 66/66; the selftest 10/10; the five record statements go 5 → 0 mismatches.
- **discernment: improved** — the round-86 non-author spot-check's five lane-owned record defects
  are closed against observed state (not restated); the wave's attack seats falsified four record
  sentences (C1-2, C1-3, C2-3, C2-4), each repaired or narrowed with its artifact cited.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — §Round 87 gate registry + the r87 instruments; verifier: none new this round (the r86 spot-check's `[~]` stands).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the scored receipt + `w1/R87Exec1.md` cold runs; LOG round 87.
- [~] Instructions executable by an agent without oral context — `w1/R87Exec_{1,2,3}.md` executed the frozen commands from the prompt alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/R87Connector.md` sibling scan: zero overlap, uncontested; nothing absorbed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Lane HEAD `a53b01a1`, branch
`master`, `ahead=0 behind=0`.

## Tooling

No tool install or upgrade this round (Node v24.21.0, Chromium 155.0.8059.84, git/jj present).

## Pre-file falsification

`PREFILE-FALSIFICATION: pass claims=2 rows=13 attack_seats=6 findings=0` (exit 0). The
ledger `.ufo/waves/round-87/claim-falsification.tsv` carries 13 rows; every `falsifies-wording`
row names its narrowing in `plans/round-87.md` §Narrowings (items 3, 6–7, 9, 13–15), and the six
attack seats (Review1, Review2, Critic, Mut1, Sentinel, Connector) each appear in the artifact
column.
