# tabi — round 88 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 88, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `f16f992d` (lane clean). **Scored receipt:** `corpus/evidence/round88/chromium-showpicker/receipt.json`
(nonce `tabi-r88-l1-86f1dcec`, driver `8c015fa4…`, fixture `8f93405128f1…`, 37 legs, 0 failures).
**Lane tip:** `0a4750e7` (pushed; `ls-remote origin refs/heads/master` prints it). **Instrument freeze:** D7 `abfd00a2` (`plans/round-88.md` §Re-freeze history: D1 `86f1dcec` first freeze,
D2 `138bb883` selftest re-pin + genuine 37-leg priors, D3 `93500a4e` the `gate-selftest` gate, D4 the
kill-power mutant from-string, D5 the runner gate's own read bug, D6 the critic-driven tally/selftest
strengthening, D7 the counter dereference guards + real selftest witnesses). **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 works a lowest axis and is a capability move):

- **C1 — coverage (9): capability `chromium-showpicker-linux`, generation r88.** The three remainder
  values round 87 named as frontier are measured, one page input each: `accept="IMAGE/PNG"` ←
  `image/png`, `accept="audio/*,video/*"` ← `text/plain`, and `accept="image/png;q=0.9"` ←
  `image/png`. Every raw attribute is read back from the page; every delivered file lands in the
  input with its bytes, trusted `input`+`change`, and page-read hex. 37 legs; 102 checks.
- **C2 — calibration (9): the round-87 non-author spot-check's routed defects D1–D4.** Restore the
  seven historical SCORECARD selftest tallies the r87 sweep rewrote; replace the r87 "10/10 at D7"
  wording with the D6 value; give every r88 gate an isolated `--selftest`; extend QUALITY 161's
  sweep to the SCORECARD tally set. `scripts/check-record-drift-r88.mjs` counts 4 statements.
  Before (base `f16f992d`): 4 mismatches; after: 0.

Round shape: **ONE v1 wave, 12 seats** (`ufo-swarm-wave.mjs run` → `counts.spawn 12`; dispatch
`.ufo/waves/round-88/w1-dispatch.json`; `.ready` taken at 11:50:56Z; 12/12 seat reports filed).
Roles: 3 executor (R88Exec1/2/3), 2 reviewer (R88Review1/2), 1 critic, 1 mutation-tester, 1 scout,
1 scribe, 1 connector, 1 sentinel, 1 simplifier — **5 attack seats of 12 (42 %)**, 1 connector
(policy cap 2). The L1 holds the planner seat; no planner was dispatched (the validator rejects
`planner`). Round total 12 seats; no residual call; dead seats: none — all twelve settled and filed.
Scratch purged (`/fast/scratch/hyaku/tabi-r88` removed after landing).

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`.ufo/waves/round-88/freeze.txt`, D7 `abfd00a2`):
  `scripts/chrome-cdp-showpicker-round88.mjs` (37 legs; new inputs `#ac`/`#au`/`#amc`),
  `scripts/check-showpicker-round88.mjs` (102 checks; `accept-grammar-law` over 12 rows),
  `scripts/negatives-showpicker-round88.mjs` (215 cases, coverage 102/102),
  `scripts/kill-power-round88.mjs` (69 mutants), `scripts/selftest-r88-gates.mjs` (11 gates),
  `scripts/check-record-drift-r88.mjs` (4 statements). Each gate carries an isolated `--selftest`.
- **Scored receipt** (37 legs, `failures: []`): counter `clean`, `checkCount 102`, 0 findings
  (`scored/counter-a.json`); battery 215 cases / 0 failed / coverage 102/102 (`scored/battery-a.json`);
  kill power 69 mutants / 69 killed / 0 survivors / 0 crashed / 0 unapplied (`scored/killpower-a.json`);
  selftest 11/11 (`scored/selftest.json`).
- **Cold-run reproduction** by R88Exec1: two fresh-nonce runs, 37/37 legs each, 101/102 checks with
  only the declaration `prior-set-complete` failing (`w1/R88Exec1.md`).
- **Leg (b) reproduction** by R88Exec2: battery byte-identical to `scored/battery-a.json`; kill power
  set-identical (69/69; only `results` order varies); selftest 11/11 at D7 (`w1/R88Exec2.md`).
- **C2 before/after and controls** by R88Exec3: base worktree `f16f992d` → exit 1, 4 mismatches;
  live lane → exit 0, 0; both C1 do-nothing controls reproduce (exit 1 with `schema`; exit 2
  `receipt-unreadable`); drift `--selftest` exit 0 (`w1/R88Exec3.md`).
- **Adversarial seats**: `R88Review1` (count + pin audit, forged-prior refusal; F1–F8),
  `R88Review2` (20 receipt mutations; 8 caught, 12 not — per-leg accept mirrors and `upload*`
  unenforced), `R88Critic` (C1-A/B/C scope attacks; C2-A tally escape and C2-B text-only
  `gate-selftest` — both repaired at D6), `R88Mut1` (43 independent mutants: 23 killed, 20 survived,
  0 crashed; survivors are witness holes, not law failures), `R88Sentinel` (6 audit axes, 4 PASS;
  F-1 the C2 leg (b) numeral, F-2 the missing drift receipts — both fixed), `R88Simplifier`
  (H1–H3: the battery/kill selftests were vacuous, two counter dereferences aborted without a
  verdict, the drift fixture was inert — all repaired at D7), `R88Scribe` (F1–F7 record defects,
  including the note's inherited r87 `recheck:` line — all fixed), `R88Connector` (21-lane scan:
  zero overlap, this lane is the sole owner of the accept/showPicker ground), `R88Scout`
  (S223/S219 re-opened; located the spec's five-token list and showed `image/png;q=0.9` is
  **out of grammar** — the wording was narrowed).
- **The wave's own findings changed the round**: D6 (critic: tally escape, text-only gate) and D7
  (simplifier: vacuous selftests, counter aborts) were repaired and re-measured; scribe F1–F7 and
  sentinel F-1/F-2 were fixed as record edits; the `image/png;q=0.9` out-of-grammar fact forced
  narrowings 1–3 and the "nine in-grammar" wording everywhere the law is stated.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| six r88 instruments: driver (37 legs), counter (102 checks), battery (215 cases), kill power (69 mutants), selftest (11 gates), record drift (4 statements), each with an isolated `--selftest` | LOG round 88 | `86f1dcec` (D1) / `db032725` (D7) |
| `.ufo/waves/round-88/{freeze.txt,claims.json,controls/,census/,sources/,scored/,w1-spec.json,w1-dispatch.json,w1.ready,w1.ready.dispatched,w1/}` | LOG round 88 | `82d0c2b8` / `db032725` |
| `corpus/evidence/round88/chromium-showpicker/receipt.json` — the scored receipt at nonce `tabi-r88-l1-86f1dcec` (37 legs, 0 failures) | LOG round 88 | `82d0c2b8` |
| `corpus/knowledge/chromium-showpicker-runtime-round-88.md` (knowledge 100 → 101), `corpus/lessons/round-88.md`, `plans/round-88.md`, `SCORECARD.md` r88 section + capability row + the seven restored tallies, `SKILL.md` §Round 88 gate registry, `LOG.md` r88 entry, `corpus/QUALITY.md` 161 extension, `corpus/SOURCES.md` r88 search-log entry | LOG round 88 | `355508db` / `db032725` |

## Before → after measurements

**C1 — coverage.** Counting command (frozen; the fixture value is the scored receipt's own):

```
node scripts/check-showpicker-round88.mjs --lane <ABS lane> \
  --receipt corpus/evidence/round88/chromium-showpicker/receipt.json \
  --expect-driver-sha256 8c015fa4ea541c25cf1e0c5ba35b28ee94c11dcb4aaa8bf1baf191ecbe49b9b4 \
  --expect-nonce tabi-r88-l1-86f1dcec \
  --expect-fixture-sha256 8f93405128f1b0286549c470ff2e849e861af2a79b3d3cccea32dd9f27231a35 \
  --prior-set .ufo/waves/round-88/controls/c1/prior-set.txt --json
```

- **Before** (base `f16f992d`): no r88 receipt → exit 2 `receipt-unreadable`
  (`controls/c1/noreceipt.txt`); the r87 scored receipt under the r88 counter → exit 1,
  findings incl. `schema`, `plan-frozen`, every `leg-*` (`controls/c1/nowork-r87-under-r88.json`).
- **After** (D7 instruments): exit 0, `verdict clean`, **102 checks**, 0 findings;
  battery 215/0/coverage 102/102; kill power 69/69/0/0/0; selftest 11/11. Measured at
  `db032725` (first scored landing `82d0c2b8`).
- Independent reproduction: `w1/R88Exec1.md` (two cold runs, 37/37 legs, 101/102 each, only the
  declaration `prior-set-complete`), `w1/R88Exec2.md` (battery byte-identical; kill power
  set-identical; selftest 11/11), `w1/R88Review1.md` F1 (counting command `clean`/102).
- **Narrowed**: acceptance is not filtering (the dialog is unmeasured); ten attribute-string values,
  **nine in-grammar** — `image/png;q=0.9` is out of the spec's `accept` grammar (`w1/R88Scout.md`)
  and is measured as a non-conforming value; attribution rides on the top-level `fixtureInputs`
  snapshot + `stateAfter`/`answer`/`read.ret`, never on the per-leg mirrors or `upload*`
  (`w1/R88Review2.md`); the byte contents stay the inherited r83 marker under r88 names
  (`plans/round-88.md` §Narrowings 1–3).

**C2 — calibration.** Counting command:

```
node scripts/check-record-drift-r88.mjs --lane <ABS lane> --json
```

- **Before** (base `f16f992d` worktree): exit 1, claims 4, **4 mismatches** — `scorecard-tallies`,
  `selftest-wording`, `gate-selftest`, `quality161-sweep` (`scored/drift-before.json`; reproduces
  `w1/R88Exec3.md`). The frozen claim text first said 3; the numeral was corrected to the measured 4
  post-scoring and is disclosed in `claims.json` `frozenAmendments` and `plans/round-88.md`
  §Frozen-amendment note.
- **After**: exit 0, **0 mismatches**, claims 4 (`scored/drift-a.json`), measured at `db032725`.
- The drift gate's own `--selftest` exits 0 on an isolated fixture lane whose `scorecard-tallies`
  and `selftest-wording` statements are red for their intended reasons (asserted `bad=["round-44-has-10"]`,
  `staleHolds=true`); the runner gate `gate-selftest` executes all four isolated modes.
- **Narrowed**: the drift selftest's swept-tally witness is overdetermined, its own assertion strength
  is unwitnessed, the battery has witness holes on carried legs, and the counter's replay limit block
  can be made self-contradictory without a red (`plans/round-88.md` §Narrowings 4–7, R88Mut1).

## Sources & frontier

- **Census** (frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
  start exit 0 (`census/start.txt`, 223 rows); end exit 0 (`census/end.txt`, 223 rows).
- **Rows before → after:** 223 → 223. Rows added by tier: none. Rows touched old→new: none by
  status/recheck/`used-by` — **S223** and **S219** were re-opened in place (access date 2026-11-08,
  687,515 B, sha256 `b0202de1c0b4…`, located quotes in the lesson Gate); **S221/S222** were carried,
  not re-opened (no `.pdl` fetched). The round-88 bounded re-opening is recorded at
  `corpus/SOURCES.md` §Search log.
- **Frontier rows advanced:** the three remainder `accept` values moved from frontier to measured
  core; R88Scout's located spec sentence ("A valid MIME type string with no parameters") moved one of
  them **out** of the grammar, and the law's wording was narrowed to that fact. Knowledge 100 → 101.
- **Assimilation:** none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
  `considerthese/` — no such directory in this lane.
- **Frontier step:** the lesson Gate records one admit (`corpus/knowledge/chromium-showpicker-runtime-round-88.md`)
  and two rejects with flip conditions (full grammar enumeration; dialog filtering); one mistake class
  mined into `corpus/lessons/round-88.md` §Mistakes.

## Trend verdicts

- **expansion: improved** — knowledge 100 → 101 (`git ls-tree -r --name-only <rev> corpus/knowledge/ | wc -l`);
  three named frontier values move to measured core; one capability row enters SCORECARD.
- **quality: improved** — the frozen family re-derives 102/102 checks, battery 215/0, kill power 69/69,
  selftest 11/11; the r87 blanket sweep's seven false tallies are restored; the round's own attack
  seats forced three instrument repairs (D6, D7) that each re-ran green.
- **discernment: improved** — the r87 spot-check's four lane-owned defects are closed against observed
  state; the wave falsified four sentences (the grammar count, per-leg attribution, the `gate-selftest`
  reach, the C2 before numeral) and each was narrowed or corrected with its artifact cited.

## Corrections the wave forced

`plans/round-88.md` §Narrowings 1–8 and §Frozen-amendment note: the grammar count (nine in-grammar of
ten values); per-leg attribution; `upload*`/patch-body non-binding; the drift fixture's
overdetermination; selftest assertion strength; battery witness holes; the drift selftest's leaked
fixture directory (14 trees cleaned by hand); the replay limit-block defect; and the C2
before-numeral correction (3 → 4, disclosed).

## Seat ledger (12 seats, all filed; `w1-results.json` = 12 results)

| seat | role | key result |
|---|---|---|
| R88Exec1 | executor | two fresh-nonce cold runs: 37/37 legs, 0 failures, 101/102 checks each; only the declaration `prior-set-complete`; the three `sp88-accept-*` legs identical in both. |
| R88Exec2 | executor | battery byte-identical to `scored/battery-a.json` (215/0/102/102); kill power set-identical (69/69, only `results` order varies); selftest 11/11 at D7. |
| R88Exec3 | executor | C2 BEFORE on base `f16f992d`: exit 1, **4** mismatches; both C1 controls reproduce (exit 1 with `schema`; exit 2 `receipt-unreadable`); drift `--selftest` exit 0. |
| R88Review1 | reviewer | counting command `clean`/102 from committed bytes; 8/8 freeze pins; forged prior refused (exit 1); F3 stale pin/prose (fixed). |
| R88Review2 | reviewer | 20 receipt mutations: 8 caught, 12 not — per-leg `fixtureInputs`, `upload*` and the embedded patch body are unenforced; attribution narrowed. |
| R88Critic | critic | C1 scope attacks (case/parameter legs cannot prove tokenisation); C2-A tally escape (stub/duplicate heading, ungated off-set 10/10) and C2-B text-only `gate-selftest` — both repaired at D6. |
| R88Mut1 | mutation-tester | 43 independent mutants: 23 killed, 20 survived, 0 crashed; survivors are battery-witness holes, selftest assertion strength and the replay limit-block wording — routed, not hidden. |
| R88Scout | scout | S223/S219 re-opened byte-identically; located the spec's five-token list and showed `image/png;q=0.9` is out of grammar — the claim wording was narrowed. |
| R88Scribe | scribe | independent records; F1–F7 record defects (incl. the note's inherited r87 `recheck:` line) — six fixed before filing, F3's residual fixed after. |
| R88Connector | connector | 21-lane / ~1,800-file scan: zero capability overlap on accept/showPicker/setFileInputFiles; this lane is the sole owner. |
| R88Sentinel | sentinel | 6 audit axes: 4 PASS; F-1 the C2 before numeral and F-2 the missing drift receipts — both fixed. |
| R88Simplifier | simplifier | H1–H3: vacuous battery/kill selftests, two counter dereferences aborting without a verdict, inert drift fixture — all repaired at D7. |

## Pre-file falsification ledger

`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 88` →
`PREFILE-FALSIFICATION: pass claims=2 rows=15 attack_seats=6 findings=0` (exit 0). The ledger
`.ufo/waves/round-88/claim-falsification.tsv` carries 15 rows over both claims; all six attack
seats (Review1, Review2, Critic, Mut1, Sentinel, Connector) are read; each `falsifies-wording`
row points at the narrowing or the D6/D7 repair that answers it, and the two `falsifies-number`
rows point at the disclosed numeral correction.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — §Round 88 gate registry + the r88 instruments; verifier: none new this round (the r87 spot-check's `[~]` stands).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the scored receipt + `w1/R88Exec1.md` cold runs; LOG round 88.
- [~] Instructions executable by an agent without oral context — `w1/R88Exec_{1,2,3}.md` executed the frozen commands from the prompt alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/R88Connector.md` sibling scan: zero overlap, this lane the sole owner; nothing absorbed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Lane branch `master`.

## Tooling

No tool was installed or upgraded this round. `pacman` stayed paused; every seat used the host's
existing node v24.21.0 and python3. R88Scout noted `/home/vgpn/.omp/agent/RULES.md` is absent on this
host (the operator file is at `/home/vgpnk/.omp/agent/RULES.md`), so no update-safety gate applied.

