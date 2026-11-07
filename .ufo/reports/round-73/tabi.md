# tabi — round 73 report

L1 `TabiR73`, attempt 1. Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`, base
`d7ff9f190260d91a1e675f474b7abf79960cdfd4`, final lane hash `8c081aa3d96df73e19f41b9920b8b48cebd1637f`
(`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state`: `ahead=0 behind=0 tracked=0 untracked=0`).

## Work performed

Declared claims (1): **C1 coverage** — capability acquisition `chromium-synth-pinch-gesture-linux`
on instrument generation r73 (sourced: S180–S183, opened this round). Frozen predicate
`C1-SYNTHPINCH-R73` (a)–(d) in `.ufo/waves/round-73/claims.json` (freeze `d7387fb3`, digests commit
D `3409ab53`). **Verdict: all four legs hold on the frozen predicate.** The frozen `limit` sentence
was falsified by R73Critic and is corrected in SCORECARD (below); no instrument, predicate or kill
rule was amended. No exploratory claim.

- Fresh-start reading (r72 rejected; Run15 tabi r63 prerequisites): r60/r61/r62/r71/r72 spot-checks
  read before the freeze; M5 producer-verdict AND→OR kept as a source-location semantic mutant and
  10 polarity cases; contradictory duplicate / fabricated-label cases kept
  (`scripts/negatives-synthpinch-r73.mjs`); final instrument bytes digested before any scored run
  (`.ufo/waves/round-73/freeze.txt`). R73Revenger: none of the eight r60–r72 root failures repeated
  (`.ufo/waves/round-73/w1/R73Revenger/report.md` §1).
- Generation r73 (routed defects 1–2 of the r72 closure): `scripts/chrome-cdp-synthpinch-round73.mjs`
  (r72 driver, 15 changed lines: schema, nonce prefix, title, header); `scripts/check-synthpinch-r73.mjs`
  (98 checks: + `nonce-expected`, `replay-launch-token`, `replay-devtools-url`,
  `replay-event-timeline` against `--prior` receipts; pin, nonce and ≥1 prior required);
  `scripts/negatives-synthpinch-r73.mjs` (228 cases; absolute anchor cases replace the relative
  `in-wheel-anchor-2px`; replay cases; must-accept prior with all identifiers different);
  `.ufo/waves/round-73/controls/c1/kill-power-r73.mjs` (98 force-true + 19 semantic mutants).
- Pre-freeze executed controls (`ae2628af`): 9 cold repetitions; counter, battery AND kill power on
  every one, 9/9 (`controls/c1/prefreeze-summary.json`, fail-closed); do-nothing / replay / limit
  controls with expected verdicts declared in the script, allOk (`controls/c1/controls-summary.json`:
  no receipt exit 2; r72 receipt exit 1; no flags exit 2; byte-identical replay and nonce+stamps
  rewrite exit 1 with the replay ids; full-identifier rewrite exit 0 = declared limit witness);
  three degenerate drivers exit 1.
- Leg (a): L1 post-D run, nonce `tabi-r73-l1-3409ab53b905`, driver exit 0, counter exit 0 clean, 98
  checks (`.ufo/waves/round-73/scored/c1-counter-a.json`; receipt
  `corpus/evidence/round73/chromium-synth-pinch-gesture/receipt.json` sha256 `a3b9070b…3ea8`), landed `c44fcf6f`.
- Leg (b): R73Exec1 cold run, nonce `tabi-r73-exec1-3409ab53b905`, counter exit 0 clean, 98
  (`.ufo/waves/round-73/w1/R73Exec1/counter.json`); L1 re-run agrees (`scored/c1-counter-b-L1rerun.json`, exit 0).
- Leg (c): battery exit 0, 228/228, coverage gap 0 (`scored/c1-negatives-a.json`); kill power
  holds, 98/98 force-true, 19/19 semantic (`scored/c1-kill-power-a.json`); reproduced by R73Exec1
  (`w1/R73Exec1/kill-power-a.json`) and R73Critic.
- Leg (d): capability row added (`SCORECARD.md` `## Round 73`, grep count 0 → 1); note
  `corpus/knowledge/chromium-synth-pinch-gesture-runtime-round-73.md` cites S180–S183.
- Supplementary (not a predicate leg): both scored receipts stay clean against PRE plus all 87
  committed r71/r72 receipts as priors (`scored/c1-counter-{a,b}-crossgen.json`, exit 0), so neither
  is a relabel of a committed earlier receipt; the (a) nonce appears in no file before D (R73Review3 §3).
- R73Critic FALSIFIED the frozen limit sentence: relabelling four identity fields of the r72 scored
  receipt / r72 smoke1 passes the frozen counting command (F4/F5,
  `.ufo/waves/round-73/lesson-proof/forge-*.pre-only.json`, exit 0); refused with cross-generation
  priors (`*.crossgen.json`, exit 1). Recorded as a correction (SCORECARD `## Round 73`), Mistakes
  row 2, QUALITY 138. R73Review1 §1.4 sharpens it further (one 1e-12 `ts` change defeats the timeline check).
- Gate registry: SKILL.md `## Round 73 gate registry`; `node scripts/selftest-r73-gates.mjs --selftest`
  12/12, exit 0 (`scored/selftest-r73-gates.out`).
- Planner seat: held by the L1 (validator rejects `planner`); no planning data-walk seat.

## Landed changes

All via `jj-lane.sh`, each printed `landed <hash>`; LOG.md entry `## Round 73`.

| commit | content |
|---|---|
| `ae2628afdfb2d8bfcffa9dd0c247f3868d67d757` | pre-freeze r73 driver/counter/battery, kill-power-r73, 9 smokes + 3 degenerates, pf evaluation (9/9), controls, S180–S183 staged sources + rows, r73 note, census start, lesson-proof (QUALITY 137 red state) |
| `d7387fb30b513fec0cf61193f275484aed750b45` | frozen claim C1 (`claims.json`) |
| `3409ab53b905d12d0866c6c93373e1c9887eda10` | D: `freeze.txt` digests, before any scored run |
| `c44fcf6f11fe549e8585e073e1cfad66dc2e2cbb` | scored run (a), leg (c) battery + kill power, scored receipt |
| `8c081aa3d96df73e19f41b9920b8b48cebd1637f` | leg (b) L1 re-run, capability row (d), wave w1 evidence (11 seats, spec, dispatch, results), S184–S186, note F1–F5, QUALITY 137–138, SKILL r73 registry + selftest, lesson, SCORECARD block + correction, LOG, crossgen controls, census end |

## Before → after measurements

**C1** — counting command (measured against `c44fcf6f` and tip `8c081aa3`):
`node scripts/check-synthpinch-r73.mjs --receipt corpus/evidence/round73/chromium-synth-pinch-gesture/receipt.json --expect-driver-sha256 3f0ffe24c8436400589dd856cff8503af150cccbcf338e7b895fb9c4ce5559c4 --expect-nonce tabi-r73-l1-3409ab53b905 --prior .ufo/waves/round-73/controls/c1/smoke{1..9}.receipt.json --prior .ufo/waves/round-73/controls/c1/degenerate-{dispatch-wheel,set-scale,skip-touch}.receipt.json --json`

| leg | before (base `d7ff9f19`) | after |
|---|---|---|
| (a) counter | no r73 receipt → exit 2 `receipt-unreadable`; r72 scored receipt → exit 1 | exit 0 clean, 98 checks |
| (b) independent run | — | R73Exec1 exit 0 clean, 98 |
| (c) battery + kill power | — | 228/228 exit 0; holds (98/98, 19/19) |
| (d) `grep -c '^| \`chromium-synth-pinch-gesture-linux\` |' SCORECARD.md` | 0 | 1 |

Do-nothing control (no r73 work) scores exit 2 / exit 1 and row count 0 (`controls-summary.json`), so
the target is not reachable without the round's work. Caveat (R73Critic, corrected limit): legs
(a)/(b) read receipts; a relabelled r72 receipt meets them under the frozen prior set.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  Start exit 0, 179 rows, 25 W04 (`.ufo/waves/round-73/census/start.txt`). End exit 0, 186 rows, 25 W04
  (`census/end.txt`). Row count: `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md` 179 → 186.
- Rows added by tier: A +7 — S180 `web_mouse_wheel_event.cc`, S181 `wheel_event.cc`, S182
  `web_input_event_conversion.cc`, S183 `local_frame_view.cc` (opened 21:23 before the freeze; C1's
  sourced rows); S184 `dev_tools_emulator.cc`, S185 `emulation_handler.cc`, S186
  `chrome_client_impl.cc` (located by R73Scout, re-opened by the L1 22:46). All Chromium 155.0.8059.84,
  `code`, `mined`, recheck `on-release`; quotes in `corpus/lessons/round-73.md` `## Gate`.
- Rows touched old → new: S182 anchor lines `56-65 … 127-134` → `57-65 … 128-135` (same round, R73Scribe F2).
- Frontier advanced: the r72 note's inference "deltaY divided by page scale" is now sourced (S180–S183),
  and the emulation factor = 1 is sourced (S184–S186).
- Sourced claim: C1 cites S180–S183 (opened this round).
- Mistakes mined (`corpus/lessons/round-73.md` `## Mistakes`): (1) a lost background evaluation
  stream → QUALITY 137 + fail-closed summary, shown able to fail
  (`lesson-proof/prefreeze-summary-streamA-lost.exit` = 1) and green after re-run; (2) current-generation-only
  prior set → QUALITY 138, red (`forge-*.pre-only.json` exit 0) and green (`*.crossgen.json` exit 1);
  (3) a control script's lane-root path one level short (failed loudly).
- Assimilation: none (`merge/tabi/` adoption closed pending L0 `tabi | round-57`). `considerthese/`:
  no such directory in this lane.

## Trend verdicts

- **expansion: improved** — knowledge 85 → 86 on ground the lane did not hold (the Blink half of the
  pinch wheel law and the emulation factor), registry 179 → 186, capability row 0 → 1.
- **quality: improved** — the r72 battery's receipt-relative anchor case is replaced by absolute cases
  shown on 9/9 receipts; the r72 replay hole is closed for same-generation replays; R73Scribe's F1–F5
  corrections applied to the note; transport copies restored (QUALITY 67).
- **discernment: unchanged** — the round's own limit sentence was refuted by a lane-dispatched seat and
  corrected; the admit/reject decisions await the non-author spot-check.

## Round shape and seats

- Shape: ONE v1 wave `w1`, 11 seats (`ufo-wave-policy.json`, band 8–16), validated exit 0
  (`.ufo/waves/round-73/w1-dispatch.json`, `w1-run.stderr`). Roles: executor 2, reviewer 3, critic 1,
  mutation-tester 1, scout 1, connector 1, scribe 1, revenger 1. Attack seats 5/11 (45 %). No
  residual call. Round total 11 seats. Dead seats: 0 (all 11 wrote reports; `w1-results.json` notes
  the orchestrator kernel restarted mid-wave and delivered outputs after restart).
- Routing per `task.agentModelOverrides` (no `model` passed); answering models not recorded (no claim
  depends on them).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1); seats report none.
- L0 questions: none new; open `tabi | round-57` unchanged.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `.scratch/*` (orchestrator-owned)
  and `trail-ids.txt` (present since r72, not this lane's round). No seat of this round wrote into the
  fleet root. Scratch `/fast/scratch/hyaku/tabi-r73` removed after landing.
- Routed to r74: cross-generation prior set (QUALITY 138), R73Mut1's 21 witnessed survivors,
  R73Review1 FG2–FG12 and §1.4, r71 R2 verifier hardening, R72Scout R3 rows, R4/R5.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 73 gate registry`; note tied to S180–S186. Lane-authored, not verified by a non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md — live `Input.synthesizePinchGesture` journey on Chromium 155 (`corpus/evidence/round73/chromium-synth-pinch-gesture/receipt.json`; independent run `.ufo/waves/round-73/w1/R73Exec1/receipt.json`); `LOG.md` `## Round 73`.
- [~] Instructions executable by an agent without oral context — R73Exec1 and R73Exec2 ran the pinned driver and counter cold (4 runs, all clean). Lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — R73Connector: overlap none on the r73 ground, verdict adjacent (`.ufo/waves/round-73/w1/R73Connector/report.md`); `PROVINCE.md` unchanged.
