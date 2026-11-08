# tabi — round 90 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 90, attempt 1. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `a9f1da08` (lane clean). **Scored receipt:** `corpus/evidence/round90/chromium-showpicker/receipt.json`
(nonce `tabi-r90-l1-e573334c78fa`, driver `ac5a7a5e…`, fixture `5fb1f0f7…`, 41 legs, 0 failures).
**Instrument freeze:** D6 `de591e7a416b` (`.ufo/waves/round-90/freeze.txt`; D1 `e573334c78fa`,
D2 the restored kill-power entries and the battery schema/mirror repairs, D3 the counter
simplification + allowlist limb, D4 the gate repairs the critic measured, D5 the simplifier's P0
set — external expectations, fail-closed kill power, teardown guard — D6 the D5 runner's gate-order
crash; `plans/round-90.md` §Re-freeze history). **Lane tip:** `f2b69440c7c7f003b0f5d694eba4c5f985684141` (pushed; `git ls-remote origin refs/heads/master`
prints it; `jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`; the lesson commit
`3e6cf40f…` follows it). Disclosure: this report's author date is 76 s before the lane tip's
committer time (body written first, lane-tip line patched after) — the committer time is after the
tip, so the landing order is provable, and `corpus/lessons/round-90.md` records it as the r89
defect-6 minor recurrence. **Axes at start:** all six at 9.

## Work performed

Declared claims (2, distinct axes; C1 declared as a lowest-axis capability generation, C2 as
calibration). **C1 lands NOT VERIFIED on its declared axis and C2 lands VERIFIED — the round is an
honest stop on C1, reported for the operator to rule, not repaired after the fact.**

- **C1 — declared coverage (9): capability `chromium-showpicker-linux`, generation r90 — "the settle
  call is bound".** Implemented: the four DOM-read legs' send logs carry `window.__inputs(true)`
  immediately after the settle `window.__state()` evaluate, `plan-calls` requires it in the ordered
  plan sequence and `send-log-allowlist` refuses it on non-domread legs. **Verdict: NOT VERIFIED on
  `coverage`.** Two non-author seats (R90Critic §F1.3, R90Review2 §6) measured that the fixture's
  `__inputs` takes no parameter, so `__inputs(true)` returns the same bytes as `__inputs()`; the
  driver's only substantive change is one argument, with identical payload, legs, check set and
  `checkCount 107` in both generations. The surface moved is a checker obligation, not a domain
  surface. Instrument legs (a)–(c) hold; the axis does not.
- **C2 — calibration (9): the round-89 non-author spot-check's six routed defects**
  (`corpus/lessons/round-89-verifier-spotcheck.md` §7), counted by `scripts/check-record-drift-round90.mjs`
  over eight statements. **Verdict: VERIFIED** on its predicate (8 claims, 7 → 0, selftest green),
  with the counted set narrowed on record: five of the six §7 defects plus three self-checks;
  §7 defect 6 (report author date) is not lane-measurable.

Round shape: **ONE v1 wave, 13 seats** (`ufo-swarm-wave.mjs run` → `counts.spawn 13`; dispatch
`.ufo/waves/round-90/w1-dispatch.json`; `.ready` written by L1 `TabiR90`). Roles: 4 executor
(Exec1 cold runs, Exec2 leg (b), Exec3 C2 controls, Exec4 settle refusal matrix), 2 reviewer
(Review1 count/pin audit, Review2 attribution attack), 1 critic, 1 mutation-tester, 1 scout,
1 scribe, 1 connector, 1 sentinel, 1 simplifier — **5 attack seats of 13 (38 %)**, 1 connector
(policy cap 2). The L1 holds the planner seat; no planner dispatched (the validator rejects
`planner`). Round total 13 seats; no residual call; **no dead seats** — R90Exec2 filed late
after a stall (its leg-(b) numbers: battery 226/0/107 and kill power 76/76/0/0/0 reproduce; its
selftest half did not complete — the D5 runner crashed and the D6 run was cancelled with the wave,
so the leg-(b) selftest is the L1's own 12/12 at D6). Thirteen seats settled and filed
(`w1/swarm-registry.json`, `w1/`).

Work items, each with its evidence pointer:

- **Instruments authored and frozen** (`.ufo/waves/round-90/freeze.txt`, D4): driver
  `scripts/chrome-cdp-showpicker-round90.mjs` (41 legs; the four domread legs read
  `window.__inputs(true)` at settle), counter `scripts/check-showpicker-round90.mjs` (107 checks;
  the settle call in `want`/`got`, the adjacency rule, the allowlist limb), battery
  `scripts/negatives-showpicker-round90.mjs` (226 cases), kill power `scripts/kill-power-round90.mjs`
  (76 mutants, four settle mutants), selftest `scripts/selftest-r90-gates.mjs` (11 gates), drift
  `scripts/check-record-drift-round90.mjs` (8 statements).
- **Scored receipt** (41 legs, `failures: []`): counter `clean`, `checkCount 107`, 0 findings
  (`scored/counter-a.json`); battery 226 cases / 0 failed / coverage 107/107 (`scored/battery-a.json`);
  kill power 76 mutants / 76 killed / 0 survivors / 0 crashed / 0 unapplied
  (`scored/killpower-a.json`); selftest 12/12 at D6 (`scored/selftest.json`; 11 gates + `expectations-present`).
- **Probes / prior set**: two 41-leg probes (`controls/c1/probes/prior{1,2}.json`), each scoring
  clean 107 against the other's prior-set; replay against both is 0 matched events
  (`counter-a.json` `limit.perPrior`).
- **Controls**: `.ufo/waves/round-90-controls/c1/nowork-settle-stripped.json` (probe clone with the
  four settle calls stripped → exit 1, `plan-calls` on all four domread legs); the r89 receipt under
  the r90 counter (exit 1, `schema` first); `controls/c1/noreceipt.txt` (exit 2 `receipt-unreadable`);
  C2 before = the same drift gate on a base `a9f1da08` worktree (8 claims, 7 mismatches).
- **C2 record repairs**: the r89 `claims.json` gains a `frozenAmendments` entry naming the two false
  clauses **and** `plans/round-89.md` §C2 item 3; two corrected ledger rows plus historical markers
  on the original rows; the r89 lesson's appended `## Corrections carried by round 90` block; the
  r89 SCORECARD pointer annotated in place; the S224 quote's word annotation corrected 19 → 17.
- **Leak witness**: `.ufo/waves/round-90/scored/leak-witness.json` — the drift `--selftest` exits 0
  with the fixture absent on the committed bytes, and a dead-branched copy exits 1 with it present
  (QUALITY 162 made observable).
- **Seat evidence** (all under `.ufo/waves/round-90/w1/`): R90Exec1 cold-run law diff (two fresh
  runs, 41/41 legs each, same law set as the scored receipt); R90Exec2 leg (b) — filed late after a stall: battery 226/0/107 and kill power 76/76 reproduce on
  the v3/v4 bytes; its selftest half did not complete (the D5 runner crash, then the D6 run was
  cancelled with the wave), so the selftest evidence is the L1's 12/12 at D6; the seat's freeze
  table is the independent record of the D1–D6 churn (`w1/R90Exec2.md`); R90Exec3 before/after + isolated `--selftest` modes; R90Exec4 33-row settle
  refusal matrix at both counter anchors; R90Review1 count/pin/prior audit (fixture pin is
  declaration-level, externally reproducible); R90Review2 12-forgery attribution attack (F1/F2/F4c/F7
  accepted — see Narrowings); R90Critic four false-greens in the first gate and the coverage-axis
  finding; R90Mut1 independent sweep; R90Scout source re-opening (both WHATWG pages fetched live,
  staged byte-identical); R90Scribe record drafts; R90Connector 21-lane overlap scan (zero contested
  ground this round); R90Sentinel bounds/provenance audit; R90Simplifier dead-weight review.

## Landed changes

- `scripts/chrome-cdp-showpicker-round90.mjs`, `scripts/check-showpicker-round90.mjs`,
  `scripts/negatives-showpicker-round90.mjs`, `scripts/kill-power-round90.mjs`,
  `scripts/selftest-r90-gates.mjs`, `scripts/check-record-drift-round90.mjs` — LOG round-90 entry,
  pins in `freeze.txt`.
- `corpus/evidence/round90/chromium-showpicker/receipt.json` + the round-90 wave tree (spec, dispatch,
  registry, scored artifacts, controls, sources, census).
- `corpus/knowledge/chromium-showpicker-runtime-round-90.md` (knowledge 102 → 103);
  `corpus/lessons/round-90.md`; `plans/round-90.md`; `SCORECARD.md` round-90 section + capability row;
  `SKILL.md` `## Round 90 gate registry`; `corpus/QUALITY.md` 163 + 161's cite; `README.md`
  `## Round 90 coverage`; `corpus/SOURCES.md` §Search log round-90 entry (224 rows, no new ids).
- `corpus/lessons/round-89.md` §Corrections (append-only); `.ufo/waves/round-89/claims.json`
  amendment; `.ufo/waves/round-89/claim-falsification.tsv` corrected + marked rows; `SCORECARD.md`
  r89 narrowing pointer annotated.

## Before → after measurements

| Claim | Counting command | Before → after | Measured against |
|---|---|---|---|
| C1 (declared coverage) | `node scripts/check-showpicker-round90.mjs --lane <ABS lane> --receipt corpus/evidence/round90/chromium-showpicker/receipt.json --expect-driver-sha256 ac5a7a5e… --expect-nonce tabi-r90-l1-e573334c78fa --expect-fixture-sha256 5fb1f0f7… --prior-set .ufo/waves/round-90/controls/c1/prior-set.txt --json` | no r90 receipt → exit 2; the stripped-settle control → exit 1 `plan-calls` ×4; the scored receipt → **exit 0, clean, 107 checks** | receipt `e573334c78fa`-nonce, D4 pins; control `.ufo/waves/round-90-controls/c1/nowork-settle-stripped.json` |
| C1 axis status | `diff scripts/chrome-cdp-showpicker-round89.mjs scripts/chrome-cdp-showpicker-round90.mjs` + `checkCount` in both `counter-a.json` | 64 changed lines, 62 renames, one substantive argument; **107 checks in both generations** → coverage **not moved** | base `a9f1da08` vs worktree (R90Critic §F1.3) |
| C2 | `node scripts/check-record-drift-round90.mjs --lane <ABS lane> --json` | base worktree: **7 mismatches**; after: **0 of 8**; `--selftest` exit 0 (all 8 red on the fixture); leak witness stock exit 0 / dead-branch exit 1 | `scored/drift-before.json`, `scored/drift-a.json`, `scored/leak-witness.json` |
| C1 leg (b) | `node scripts/negatives-showpicker-round90.mjs …` / `node scripts/kill-power-round90.mjs …` / `node scripts/selftest-r90-gates.mjs …` | battery **226/0/107**, kill power **76/76/0/0/0**, selftest **12/12** | `scored/battery-a.json`, `scored/killpower-a.json`, `scored/selftest.json` (D5/D6 bytes) |

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` → exit 0 at round
start (224 rows, `census-start.txt`) and at round end (224 rows, `census-end.txt`).

`corpus/SOURCES.md` before → after: **224 → 224 rows** (no new ids). Rows touched old→new: **S224,
S223, S219** re-opened in place (access date 2026-11-08; both WHATWG pages fetched live, HTTP 200,
687,515 B / 121,595 B, staged byte-identical at `.ufo/waves/round-90/sources/`); status/`recheck`/
`used-by` unchanged, so no old→new edit is owed and the §Search log entry records the re-opening.
Rows added by tier: **0** (A/B/C). Frontier advanced: the r89 "settle-evaluate requirement" line is
now an implemented counter obligation (recorded), and the r89 rung "The settle re-read is
counter-verified" flips from rejected to bound-by-call — while the round's own frontier note keeps
provenance open (R90Review2 F1/F2).

No new knowledge row from an external source was admitted; the round's knowledge entry
(`chromium-showpicker-runtime-round-90.md`) cites S224/S223/S219/S216 and the r89 carriers, all
opened or re-opened this round.

Assimilation: none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`).
`considerthese/`: no such directory in this lane.

## Pre-file falsification ledger

`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 90` →
`PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=6 findings=0` (exit 0).
`.ufo/waves/round-90/claim-falsification.tsv` carries 14 rows over both claims; all six attack
seats (Review1, Review2, Critic, Mut1, Sentinel, Connector) are read. Four rows are
`falsifies-wording` (C1 × Review2, Critic, Mut1; C2 × Critic, Sentinel) and every
one names its narrowing in `plans/round-90.md` §Wave corrections or `SCORECARD.md` §Round 90.

## Trend verdicts

- **expansion: unchanged** — no new domain surface, no new registry row, no new knowledge on
  unheld ground: the round's knowledge entry documents a checker obligation over the same 41 legs
  (R90Critic §F1.3; R90Review2 §6). The honest read of the declared axis.
- **quality: improved** — the r89 spot-check's six routed record defects are repaired and the repair
  is measured by a gate that now reads state (`sourcesRows === 224`, the dead-branch leak witness,
  backtick-proof pointers, fail-closed on missing files); the gate's four false-greens were found by
  an attack seat and closed before filing (`w1/R90Critic.md` §F2.1–F2.8, D4). Instruments re-run
  green: 107 / 226 / 76 / 12.
- **discernment: improved** — a non-author seat falsified the round's own declared axis, and the
  claim is reported NOT VERIFIED rather than re-scoped; the seat's recommended corrections were
  adopted as record edits only, the frozen claim text untouched; four accepted forgeries (F1/F2/F4c/
  F7) are recorded as narrowings with their reproduction.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — §Round 90 gate registry + the r90 instruments; verifier: none new this round (the r88 spot-check's `[~]` stands).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the scored receipt, the wave's cold runs (`w1/R90Exec1.md`) and the L1's D5/D6 leg-(b) artifacts (`scored/battery-a.json`, `scored/killpower-a.json`, `scored/selftest.json`); LOG round 90.
- [~] Instructions executable by an agent without oral context — the executor seats ran the frozen commands from the prompt alone (`w1/R90Exec{1,2,3,4}.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/R90Connector.md` 21-lane scan: no contested ground this round; nothing absorbed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Lane branch `master`.

## Tooling

No tool was installed or upgraded this round. `pacman` stayed paused; every seat used the host's
existing node v24.21.0, chromium 155.0.8059.84 and python3. The `/home/vgpnk/.omp/agent/RULES.md`
read was honored (pacman guard applied; no install needed).
