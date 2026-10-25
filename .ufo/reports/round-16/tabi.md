# tabi — round 16 report (hyaku phase 2, attempt 1)

Lane HEAD `1205d261776a349af99a5a205c7c2467fbabae16` (pushed, `origin/master`, ahead 0, clean).
Baseline `e38d2599a922cb729186353830fff8e159b4fef0`. Measured revision
`3254740c694e4fc7851ca9d88b39230db3042ba6`.

## Work performed

Declared claims (2):
- **C1 — operability 8 (lowest non-retired tie with depth/freshness/adjacency):** enforced
  measurement-binding contracts 0→1. Fixes the round-15 outside routed defects 1 and 2
  (`tabi-shokunin/corpus/lessons/round-15-verifier-spotcheck.md:120-121`).
- **C2 — coverage 9 + capability acquisition `webmcp-cdp-observation`, sourced:** native-WebMCP
  held entries 0→1 on Chromium 154.0.8037.97 (flags, loopback). It rests on S020 (re-opened) and
  S030–S037, all opened this round.

Work items:
- Wrote the L1 plan (L1 holds the canonical §3 planner seat; the validator rejects `planner`;
  bounded data-walks rode scout/reviewer items): `tabi-shokunin/.ufo/waves/round-16/PLAN.md`.
- Built the gate `scripts/check-measurement-binding.mjs` with modes `--check/--at/--reproduce`,
  `--legacy` and `--self-test`, plus a 59-case child-CLI selftest
  `scripts/selftest-measurement-binding.mjs` (`8f7feb3`, hardened at `3254740`).
- Made `--legacy` on the real round-15 file exit 1 with C1
  `counter_digest_unrecorded/counted_inputs_undeclared/counter_changed_since_measurement` and C2
  `counter_digest_mismatch/counted_inputs_undeclared`: `corpus/evidence/round-16/binding/legacy-r15.json`.
- Added the counter `.ufo/waves/round-16/measure.mjs`, authored by L1 after the seat that owned it
  died. It reruns the revision's own selftest. It then runs two probes of its own: a stub gate that
  always reports clean, against which the selftest must fail, and three variations of the round-15
  file whose expected findings differ. The probes were added after wave 2 falsified the first
  version, and three wave-2 liar commits now count 0
  (`corpus/evidence/round-16/measure/c1-liar-probes.json`).
- Added the WebMCP harness `scripts/webmcp-loopback-round16.mjs` with fixtures. The receipt
  `corpus/evidence/round-16/webmcp/receipt.json` shows 11/11 cases passing, including the
  flag-off and domain-disabled controls, a real browser pid and argv, and the permissions-policy
  and `data:` divergence. The pre-commit 8/11 receipt is kept as `receipt-first-run-failed.json`.
- Wrote the knowledge note `corpus/knowledge/webmcp-chromium-loopback-round-16.md`. It has a
  spec-versus-build table, a decision table and a corrections record. Also appended the README map
  row and supersession text, a SKILL round-16 section with its wave-2 corrections, and QUALITY 22–25.
- Wrote the lesson `corpus/lessons/round-16.md`: Gate with per-row URL, date and quote; registry
  transitions; 10 mined mistakes; routed-defect disposition.
- Ran the frontier step. SOURCES went from 29 to 40 rows. S039's rejection was found unsound for a
  dated source and is superseded append-only by S040, and a drafted Fastly rejection was withdrawn
  (chromestatus gives 149→156, extended to 162).

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `8f7feb3` | Gate, selftest, harness, fixtures, receipts, note, SOURCES rows S030–S039 + S020 re-open, README/SKILL/QUALITY appends, wave-1 evidence | `tabi-shokunin/LOG.md` "2026-10-20 — round-16" |
| `b444ca8` | C2 counter consumer repair; the failing first C2 measurement is kept | same entry ("History kept") |
| `3254740` | Wave-2 repairs to gate, selftest, counter and harness; receipt regenerated; note, README and SOURCES corrections (S037 mined, S040); wave-2 evidence | same entry ("Wave 2 falsified and L1 repaired") |
| `6c8e0ff` | `measurements.json`, binding manifest, lesson, LOG/SCORECARD/QUALITY/SKILL records, liar-probe receipt | same entry |
| `1205d26` | `binding/check.json` (`--check --reproduce` clean, claims=2 bound=2) | same entry (binding) |

All five commits are authored `tabi-shokunin <tabi@shokunin.local>`, use pathspec-limited adds, and were pushed before this report.

## Before → after measurements

| Claim | Counting command (lane root) | Before @ `e38d259` | After @ `3254740` |
|---|---|---|---|
| C1 | `node .ufo/waves/round-16/measure.mjs REV --claim C1` | exit 0, `c1_binding_contracts:0` ("gate or selftest absent") | exit 0, `c1_binding_contracts:1`, `failures:[]`; selftest 59/59 clean; stub-gate selftest `verdict=failed`; 3 legacy variations exact |
| C2 | `node .ufo/waves/round-16/measure.mjs REV --claim C2` | exit 0, `c2_webmcp_held:0` | exit 0, `c2_webmcp_held:1`, `failures:[]` |

- Both rows used the counter blob sha256 `c8b4100a9f60dcd530ae752074e04d05074b4938cc05c6f19214add05e2594cb`
  at the measured revision. Raw argv, stdout and exit codes are in `corpus/evidence/round-16/measurements.json`.
- Delivered-HEAD binding: `node scripts/check-measurement-binding.mjs --check
  corpus/evidence/round-16/measurement-binding.json --at HEAD --reproduce` gives
  `MEASUREMENT_BINDING verdict=clean claims=2 bound=2`, exit 0, at `6c8e0ff` (receipt
  `binding/check.json`) and again at `1205d26`. The commits after `3254740` touch no counted input.
- History, not this measurement: C2 counted 0 at `8f7feb3` with that commit's counter blob
  (`4eb82895…`, label-as-path defect). C1 already counted 1 at `8f7feb3`/`b444ca8` with the
  pre-wave-2 counter, which wave 2 showed liars could also satisfy.
- No-harm checks at the delivered HEAD:
  - `check-round-contract` clean (10 rounds)
  - `check-user-round-contract` exit 1 `Found 6 user rounds, expected 10` (pre-existing, unchanged)
  - `check-freshness --worktree` clean 34/34
  - `check-sources` clean, rows=40
  - aria-metadata corrected check clean (wave-2 AttackHarmGates)
- No scalar moves.

## Sources & frontier

- Rows 29→40. Counting command:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  It exited 0 `tabi ok` at start and at end. `census` went from A23/B4/C2, mined24/queued3/rejected2
  to A31/B4/C5, mined33/queued2/rejected5.
- Added by tier: A 8 (S030–S037), C 3 (S038–S040 rejected).
- Touched old→new:
  - S020: status queued→mined; used-by —→ note. The anchor is kept at `f14762e6`; the live
    revisions `cb3d1696` and `51ed7565` are logged.
  - S037: added queued, then queued→mined once the note cited it.
  - S039: superseded by S040.
  - S021: re-opened, unchanged.
- Frontier advanced: "Native WebMCP in chromium 152 — unprobed (census U3)" is held for
  Chromium 154 only. Chromium 152, real-site WebMCP, agent-side consumption and invocation as
  evidence stay open.
- Mistake mined: 10 rows in `corpus/lessons/round-16.md` `## Mistakes`, each with a fix shown able
  to fail. Sourced claim: C2 (note `source:` S020, S030–S037).

## Trend verdicts

- **expansion: improved.** Knowledge notes went 32→33 with one note on frontier ground that was
  previously unprobed. It cites only mined A-tier rows opened this round, and capability
  `webmcp-cdp-observation` enters. The source-row count is not what is credited.
- **quality: improved.** Counts are now digest-bound and checkable at the delivered HEAD (round-15
  routed defects 1/2 closed). Wave 2 falsified 20+ items and each was repaired or disclosed, with
  failing history kept: the 8/11 run, C2's 0 at `8f7feb3`, and the liar probes.
- **discernment: improved (author-side).** QUALITY 22–25 are lesson-backed. Two source rejections
  were corrected: S039 was dated-unsound and was superseded; the Fastly rejection was withdrawn. The
  census `navigator.modelContext` guess was traced as a stale-premise mistake. Outside admit/reject
  agreement remains external.

## SHONEN

- [~] Decision tables, error patterns, checklists with cited sources — `tabi-shokunin/SKILL.md` round-16 decision table; `corpus/knowledge/webmcp-chromium-loopback-round-16.md` decision table (no non-author verifier)
- [~] End-to-end domain task executed and logged — `corpus/evidence/round-16/webmcp/receipt.json` 11/11, `LOG.md` round-16 entry (no non-author verifier)
- [~] Instructions executable without oral context — note §Recheck procedure; SKILL gate registry row (no non-author verifier)
- [~] No cross-domain bleed, PROVINCE accurate — `PROVINCE.md:3-19`; kaidoku CDP overlap reported as contested, not absorbed (note §Adjacency)

## Round mechanics and extras

- **Waves:**
  - **Wave 1: 84 seats.** Scout 21, executor 19, reviewer 14, scribe 10, connector 8, critic 5,
    revenger 4, sentinel 2, simplifier 1. It was refused 4× by the 100-job cap and spawned on
    attempt 5 (`.ufo/waves/round-16/w1/dispatch-attempts.json`).
  - **Wave 1 dead seats:** 6 executors died on the m_swe free-tier rate limit (BindCore,
    MeasureCounters, WebmcpHarness, WebmcpProbeDeclarative, WebmcpProbeLifecycle,
    WebmcpProbeFrames). They were not respawned; L1 integrated their partial files.
  - **Wave 2: 73 seats.** Reviewer 42, scout 14, critic 7, mutation-tester 4, sentinel 3,
    connector 2, revenger 1. Dispatched on the first attempt; 0 dead.
  - **Round total:** 157 seats. Seat IDs carried a `-5` suffix in wave 1 after the refused
    attempts, and the seats were told by message.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  `.ufo/state/*`, `watchdog.log` and orchestrator `scripts/hyaku/jj-lane*.sh.new`. None of it is
  tabi's, so nothing was moved.
- **Contested scope (adjacency):** kaidoku's Core "Runtime observation (CDP)" row
  (`kaidoku-shokunin/PROVINCE.md:53`) overlaps the C2 CDP harness. This needs an integrator ruling.
- **Inherited state:** the lane was clean at dispatch, with no earlier attempt
  (`lane-dead-no-report` absent). Outside verifier files were read, not edited.
- **Carried debt:** the protocol step-1/step-4 closure-checker certification; USER 6/10; r07
  replay; user-record freezing; IPv6; Git env; validator pin.
- **Disclosed limits:**
  - the counter runs revision code unsandboxed;
  - confinement is page-level only (WebRTC, WebTransport and SharedWorker traffic is not confined);
  - the protocol-capture profile leaks one temp dir per run;
  - the producer of the 8/11 pre-commit run was not retained.
- **L0 questions:** none appended. The two earlier tabi questions remain open
  (`l0-questions.md:25`, `:34`).
- **Stale-lane:** respawn-per-round driver. This tabi round-16 mission was launched
  2026-10-20T10:51:16-03:00 and is progressing (5 lane commits). No other tabi mission is open.
- **Tools installed/updated:** none by L1. Seat RevCountCmds installed Node 22.23.3 and 20.20.2 via
  fnm; seat AttackC1Before used `npx -y node@22` (22.23.3). No pacman transaction.
