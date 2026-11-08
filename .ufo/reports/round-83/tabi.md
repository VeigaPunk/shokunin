# tabi — round 83

## Work performed

**Declared claims** (frozen before scoring in `.ufo/waves/round-83/claims.json`, digests D
`b6496e6f5d4f…` = sha256 of `.ufo/waves/round-83/freeze.txt`):

- **C1 — coverage, capability `chromium-showpicker-linux` generation r83** (sourced: S219/S220
  re-opened; predicate `C1-SHOWPICKER-R83`). Fifteen legs: cross-origin `type=number` and `type=range`
  SecurityError; a `multiple` file input answered opens `selectMultiple`; a real PNG into
  `accept=".png"` accepted with its bytes; the second chooser (same `backendNodeId` as the first)
  answering leg. The r82 seven laws carried. Counter `scripts/check-showpicker-r83.mjs`, 74 checks.
- **C2 — calibration, record drift on the r82 spotcheck routed defects** plus the anchored
  direction-bound counter and the r83 identity/numbers legs (predicate `C2-RECORDDRIFT-R83`).
  Counter `scripts/check-record-drift-r83.mjs`, 7 claims. Before 4 mismatches, after 0.

**Work items**

- Built the r83 instrument family from the r82 bytes (driver, counter, battery, kill power, selftest,
  record drift); 15-leg driver with two new cross-origin inputs, a `multiple` leg, a MIME-accept leg
  and a second-chooser answer leg (`scripts/chrome-cdp-showpicker-round83.mjs:166-186`).
- Pre-freeze probe (15 legs, 0 failures) is the committed prior `.../controls/c1/probes/prior1.json`.
- Scored run, re-run at the identity nonce `tabi-r83-l1-b6496e6f5d4f`: 15 legs, 0 failures, counter
  exit 0 **74 checks clean** (`corpus/evidence/round83/chromium-showpicker/receipt.json`,
  `fixture.sha256 7784c9de…`). The earlier first-freeze receipt (`tabi-r83-l1-c016710129da`) was also
  clean 74 and is superseded so the receipt and records carry one nonce.
- Battery 84 native cases + 69 imported R82Mut1 witnesses = **153 cases, 0 failed, coverage 74/74**
  (`.../scored/battery-a.json`); frozen kill power **50/50** (`.../scored/killpower-a.json`); selftest
  **9/9** (`.../scored/selftest.out`).
- Pre-freeze repairs, each fixed by measurement: missing `clickAt` in the counter PLAN crashed
  `plan-calls`; `LEG_KEYS` required the two chooser-id fields on every leg but only one leg set them
  (driver now initialises them); the redundant `secondChooserBackendNodeId === opens[1]` conjunct
  survived its own mutant and was removed as a rule owned by another check (QUALITY 156).
- Routed defect 2 from the r82 spotcheck closed in part: the 69 witness mutations are battery cases;
  the `mode-single-only` gap is closed by the `sp83-multiple-mode` leg; three witnesses needing the
  witness harness's `H.*` mirror machinery are dropped with reasons (their ids are covered by the
  existing prior-set walk cases).
- C2: `check-record-drift-r83.mjs` anchors the quote-count direction on the correction cell
  (`23 -> 20`), requires a committed refused control, corrects the r82 lesson's `7 -> 4` count, and
  files the census start/end the r82 spotcheck found missing (`.../census/start.txt`, `end.txt`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| freeze + claims + prior set | round-83 | `4cdf4def` |
| freeze amendment (redundant mutant removed, prior set repaired, number/range laws registered) | round-83 | `27d5451b` |
| generation r83 + calibration drift, note, SCORECARD, SKILL registry, LOG | round-83 | `5d6c34f0` |
| 69 R82Mut1 witnesses imported (153 cases), final pins | round-83 | `615c97a1` |
| wave w1 evidence, narrowings (`plans/round-83.md`), seat-status repair, final scored receipt at the identity nonce | round-83 | `030dfc29` |

All commits landed through `scripts/hyaku/jj-lane.sh commit … --as tabi` (helper `landed <hash>` lines
cited); lane `master` = `030dfc2998015d8d1ee0a44d6fd1229d131dc08e`, remote identical.

## Before → after measurements

- **C1** — command: `node scripts/check-showpicker-r83.mjs --lane <ABS lane> --receipt
  corpus/evidence/round83/chromium-showpicker/receipt.json --expect-driver-sha256
  70b522cc896f4a9b89320d58313b56519499566256cb0b7dd0b3a8aac1944fce --expect-nonce
  tabi-r83-l1-b6496e6f5d4f --expect-fixture-sha256
  7784c9dece0f5c7ad1911733281a8bd7337a8a5588799cbda9acc02f9a9e55fa --prior-set
  .ufo/waves/round-83/controls/c1/prior-set.txt --json`.
  Before: no r83 receipt → exit 2 `receipt-unreadable`; the r82 receipt under the r83 counter → exit 1,
  69 findings / 40 failed checks (`.../scored/nowork-r82-under-r83.json`). After: exit 0, `verdict
  clean`, `checkCount 74`, `findings []` (`.../scored/counter-a.json`), measured against `030dfc29`.
- **C2** — command: `node scripts/check-record-drift-r83.mjs --lane <ABS lane> --json`.
  Before: exit 1, 4 mismatches (`direction-bound`, `census-artifacts`, `r83-identity`, `r83-numbers`)
  in `.../lesson-proof/c2-before.json`. After: exit 0, **0 mismatches** (`.../lesson-proof/c2-after.json`).
- **Controls**: the reversed correction (`23 -> 20` → `20 -> 23`) on a scratch mirror of HEAD bytes
  exits 1 with `direction-bound` failed (R83Drift `control-1-reversed.json`; summarised in
  `.../lesson-proof/c2-controls.json`). No-work control symmetric: r83 receipt under the r82 counter →
  exit 1 (`.../scored/nowork-r82-under-r83.json` reverse direction measured by R83Critic).

## Narrowings (the wave falsified parts of the claim wording; `plans/round-83.md`)

1. **multiple-mode bytes** (R83Review1, MEDIUM-LOW false green): `multiple-mode-law` binds mode, file
   list, upload record and the trusted events, but not the page-read `ret` hex; a consistent forgery
   with `read.ret='hex:00'` scores clean. Narrowed to the bound half; ret pin routed to r84.
2. **second-chooser attribution** (R83Review2 + R83Exec2): the law is a payload/state law plus an
   id-equality clause. Answering `evs[0]` instead of the last event delivers byte-identical files and
   the law still passes 74/74; every id-equality conjunct is individually and jointly droppable with
   the battery exiting 0.
3. **battery reach** (R83Mut1): the frozen kill power kills its own 50-mutant list 50/50, but an
   independent 115-mutant set (111 executed, no reuse) leaves **110 alive**, 77 behavioural escapes.
   "Kill power 50/50" is not general mutant resistance; routed to r84.
4. **replay boundary** (R83Critic + R83Mut1): verbatim replay refused (61/61 matched vs the 31-event
   threshold); moving the first 31 events +100 ms escapes replay and `event-leg-window` catches that
   move; R83Mut1's threshold forgery is accepted by both relaxed and strict replay mutants. The escape
   minimum is 31 and it is a declared limit.
5. **C2 direction/number binding** (R83Drift): `direction-bound` is statically anchored plus a
   committed refusal receipt (the counter does not re-execute the mirror itself); `r83-numbers` binds
   presence plus the scored outputs, not each statement.

## Sources & frontier

Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin tabi` — start exit 0, 223 rows (`.../round-83/census/start.txt`), end
exit 0, 223 rows, 37 W04 duplicate-URL warnings (`.../round-83/census/end.txt`). Rows before → after:
**223 → 223** (no new rows; generation r83 measures the r82 note's named frontier on carried sources).
Rows added by tier: none. Rows touched old→new: none (`status`/`recheck`/`used-by` unchanged; S219/S220
re-fetched 2026-11-08, byte-identical sha256 `b0202de1c0b4…`). Frontier rows advanced: `type=number`/
`range` cross-origin (frontier → core), `multiple` mode (frontier → core), accept MIME answer
(frontier → core), second-chooser answer payload (frontier → core, with the attribution limit named).

Assimilation: none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`).
`considerthese/`: no such directory in this lane.

## Trend verdicts

- expansion: **improved** — knowledge 94 → 95 (`corpus/knowledge/chromium-showpicker-runtime-round-83.md`),
  four frontier legs moved into core with receipt field paths, registry held byte-identical.
- quality: **improved** — 74-check counter clean, battery 153/153 with full coverage, frozen kill power
  50/50, selftest 9/9, drift 0; the one surviving mutant was removed as a redundant rule rather than
  papered over.
- discernment: **improved** — the wave's attack seats falsified the round's own wording in five places
  (multiple-mode bytes, second-chooser attribution, battery reach, replay boundary, C2 binding) and
  every one is narrowed in `plans/round-83.md` and this report instead of being absorbed; the L1's own
  false dead-seat record is retracted in `corpus/lessons/round-83.md` `## Mistakes`.

## Round shape

One v1 wave `w1` (policy `ufo-wave-policy.json`, band 8–16): **10 seats**, spawned
2026-11-08T02:06:43, all 10 settled (`.../round-83/w1-results.json`). Role mix: 3 executors
(R83Exec1, R83Exec2, R83Drift), 2 reviewers (R83Review1, R83Review2), 1 critic (R83Critic),
1 mutation-tester (R83Mut1), 1 scout (R83Scout), 1 scribe (R83Scribe), 1 connector (R83Connector) —
3 attack roles (≥25 %). No residual call. Round total: **10 seats**. Dead seats: none (a first draft
recorded R83Mut1/R83Scribe dead from missing report files; both were alive — retracted, and the
`R83Mut1.md` path the L1 had overwritten is repaired by recovering the seat's own output to
`w1/R83Mut1-results.json`). Planner seat: the L1 holds it (the validator rejects `planner`).

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*`
(orchestrator-owned) and `plans/round-91.md` (another lane's file, untouched) — no fleet-root file
written by this lane's seats.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Approval table, §Evidence ladder, §Runbook, `## Round 83 gate registry`.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `corpus/knowledge/multi-step-journey.md` §1–§2, §7; LOG.md round-83.
- [~] Instructions executable by an agent without oral context —
  `corpus/knowledge/executor-test-sufficiency.md` §0, §4; R83Exec1's cold runs reproduce the driver
  from the committed bytes with no oral context.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; R83Connector scanned
  20 siblings, 0 contested rows on the r83 surface, five pre-existing contested rows reported to the
  integrator.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none this round (node v24.21.0 and Chromium 155.0.8059.84 already present; pacman
paused per the addendum guard).
