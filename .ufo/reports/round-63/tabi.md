# tabi — round 63 (attempt 1, Linux host)

**Declared claims (2, frozen before the wave and before any scored data):**

- **C1 — coverage, capability acquisition `chromium-wheel-scroll-domain-linux`**
  (**final verdict UNPROVABLE** — its frozen predicate is met, but the target is
  reachable by a hand-written receipt, so the round's do-nothing standard fails;
  see the measurements and the wave findings):
  the Linux Chromium wheel/scroll domain on a loopback fixture (delta
  passthrough, exact scroll arithmetic, a page-cancelled leg with its released
  positive control) measured by a counter that refuses ten declared negatives
  and kills eight exact-line source mutants through the production CLI. The
  stagnation nudge is ACTIVE (saturation 8; every axis ≥ 8; no capability row
  since r58), so the lowest-axis obligation is waived and this is the round's
  frontier/capability move.
- **C2 — calibration**: the lane's own frozen self-assessment gate
  (`scripts/check-selfassessment.mjs`) counts its self-assessment against
  observed repo state; mismatches 2 → 0 and `clean` false → true at the landing
  revision with a clean worktree, gate bytes and its 45/45 selftest unchanged.

Baseline `f098bcf8843c8a5a723a83995352180f897a6ff9`; instrument/controls freeze
`816592612dd2a8073437c595d3fe3c477125cf3c`; wave spec + validated dispatch
`e5325ad8805df86cb0109373d2ac695f558c2a1f`.

## Work performed

- **Read before declaring.** The four rejected closures r59–r62 and the r62
  non-author spot-check (`corpus/lessons/round-62-verifier-spotcheck.md`,
  R1 durability artifact, R2 producer-verdict polarity negatives, R3
  contradictory-duplicate/fabricated-label refusal, R4 unanswered
  topology/overlap limits) were read first; every routed defect has a
  corresponding control in this round or an explicit non-claim in the lesson.
- **Pre-freeze probe (design data, not the scored pass).** Three cold
  `mouseWheel` probes on Chromium 155.0.8059.84 measured the determinism that
  sized the predicate: `.ufo/waves/round-63/probe/wheel-probe.mjs` and
  `probe1.json`–`probe3-smooth.json` (scroll 0→120→240→120→120, swallowed leg
  unchanged, clean teardown; identical with and without `--disable-smooth-scrolling`).
- **Instruments built and frozen.** `scripts/chrome-cdp-loopback-round63.mjs`
  (driver: launch/profile/sweep/teardown machinery retained from r62, new
  fixture and five-leg wheel journey),
  `.ufo/waves/round-63/counters/chromium-wheel-r63.mjs` (counter + 22-case
  selftest), `counters/make-negatives-r63.mjs` (ten one-field falsifications),
  `counters/mutate-r63.mjs` + `counters/mutants-r63.json` (exact line/column
  mutants run through the production CLI), `counters/compare-stability-r63.mjs`,
  `counters/old-generation-r63.mjs` (red-before). Eight digests frozen in
  `claims.json`.
- **Failing-before controls executed and committed BEFORE the freeze**
  (`claims.json:controlsCommittedBeforeFreeze`):
  `.ufo/waves/round-63/controls/no-work/` (no-args exit 2, missing receipt exit 2,
  r62 receipt through the r63 counter exit 1 with 20 findings, driver-pin mismatch
  exit 2; positives: smoke receipt exit 0, r62 live receipt exit 0 under its own
  frozen counter);
  `.ufo/waves/round-63/controls/negatives/` (ten controls, each exit 1 with its
  expected finding);
  `.ufo/waves/round-63/controls/mutation/matrix.json` (pristine accepts live,
  refuses all ten; 8/8 mutants distinguished, 0 survived);
  `.ufo/waves/round-63/controls/old-generation/result.json` (frozen r62 counter
  exit 1 on a lying receipt, exact-line producer mutant exit 0 — the class this
  generation closes, demonstrated on this host with the mutant bytes committed
  at `controls/old-generation/r62-producer-mutant.mjs`).
- **Scored data (post-freeze).** Two independent cold runs of the frozen driver
  wrote `corpus/evidence/round63/chromium-wheel-scroll/receipt.json` (+4 PNGs)
  and `stability/receipt-run2.json` (+4 PNGs), 15 files including a
  `sha256sum -c`-verifying `MANIFEST.txt`; nonces `tabi-r63-data-one` /
  `tabi-r63-data-two`, ports 19511/19512 and 19513/19514. Counter exit 0 on both
  (`controls/counter-data-run1.command.json`, `…run2…`); stability `STABLE`
  (`controls/stability-data.json`, 4/4 PNG sha256 identical); the matrix over
  the scored receipt is 8/8 killed (`controls/mutation/matrix-data.json`).
- **C2 repair.** Before state reproduced in a sandbox clone at baseline with the
  one inherited round-62 artifact restored (`controls/selfassessment-before.json`:
  exit 1, mismatches 2). Append-only correction of the `SCORECARD.md:3427` tally
  attribution (one line, so the gate's per-line association can bind it) and the
  round-62 `R62Scout` directory committed with `MANIFEST.txt` (8 files,
  1,388,366 B `commands.json` included).
- **Frontier step.** S166 (MDN WheelEvent, B/docs) and S167 (CSSOM View, A/spec)
  opened and quoted this round; census before/after both exit 0; lesson Gate has
  one admit and one reject per source plus two rejected candidates with flip
  conditions; `QUALITY.md` criterion 115 landed; knowledge note
  `corpus/knowledge/chromium-wheel-scroll-round-63.md` (notes 74 → 75); README
  coverage row; `SKILL.md` §Wheel/scroll domain.
- **Wave.** ONE v1 wave `w1` of 12 seats, dispatched through the inline ready
  handoff after the freeze commit (`w1.ready` at 16:02, orchestrator
  `w1.ready.dispatched` at 16:03; registry 12 names). Roles: scout 1, executor 3,
  scribe 1, connector 1, reviewer 1, critic 1, mutation-tester 2, sentinel 1,
  revenger 1; attack seats reviewer+critic+2×mutation-tester+sentinel+revenger
  = 6/12 (50 %); one connector (≤2). The L1 holds the canonical planner seat.
  **All 12 seats settled** with reports in `w1/` (scout 1, executor 3, scribe 1,
  connector 1, reviewer 1, critic 1, mutation-tester 2, sentinel 1, revenger 1);
  every seat's output is nonempty and no dead-seat/provider-error note appears
  in `w1-results.json`. The L1 integrated their findings into the round lesson
  (`## Wave findings`, W1–W15). Headline findings: the frozen counter is
  a consistency checker, not an execution oracle (a hand-written receipt with
  four 1×1 PNGs, and a coherent driver-side fabrication, both exit 0); the
  stability comparator is not in the pin set and compares only one side's
  declared hashes; sixteen of the counter's 25 checks have no declared negative;
  the page-side `scrollEvents` contradiction is admitted. The sentinel measured
  Chromium's own background traffic to four non-loopback IPv6 peers in both of
  its runs (fixture server logged only `/` and `/favicon.ico` from 127.0.0.1),
  a lexical-only scratch guard, and partial XDG redirection. All are disclosed
  as C1's limits or routed to the next declared generation; none is a
  frozen-rule fire, and none is repaired after scoring.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows orchestrator `.scratch/*`, `.ufo/l0-questions.md`, another lane's
  `round-84/kama.md`, and one stray `after` file dated 2026-11-03 20:05 (content
  `== SCORECARD diff base-`, no lane/round attribution) — not tabi r63 work, left
  untouched. No tabi seat wrote into the fleet root.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| r63 instruments, frozen claims, pre-freeze controls, staged sources | Round 63 (C1/C2) | `81659261` (lane) |
| wave w1 spec, validated 12-seat dispatch, ready handoff | Round 63 (wave line) | `e5325ad8` (lane) |
| driver/counter/harness + controls + sources (freeze) | Round 63 | `81659261` (lane) |
| scored evidence, data controls, docs, knowledge, lesson, SCORECARD/LOG/QUALITY/README/SKILL, round-62 artifact MANIFEST | Round 63 | `54170404496c8d0385ded985c33ea7657aaab6b6` (lane) |
| C2 gate after-receipt | Round 63 | `5b7029ebd9ad96282e662a1225cb4762aa074cf1` (lane) |
| this report | — | filed after lane tip `5b7029ebd9ad96282e662a1225cb4762aa074cf1` (fleet `fleet-commit.sh --as tabi`) |

## Before → after measurements

**C1** — counting command (frozen; also the claim's `afterCommand`):

```
node .ufo/waves/round-63/counters/chromium-wheel-r63.mjs corpus/evidence/round63/chromium-wheel-scroll/receipt.json --driver scripts/chrome-cdp-loopback-round63.mjs --expect-driver-sha256 b00efd59ac10fd047014b76b2a5d16cc8b0acaab0730e8c6029a0b53a0d6c040 --shot corpus/evidence/round63/chromium-wheel-scroll --json
```

- **before** (freeze commit `81659261`): no r63 driver/counter/evidence exists;
  the frozen r62 generation's exact-line producer mutant accepts its lying
  receipt while the pristine bytes refuse it (exit 1 / exit 0,
  `controls/old-generation/result.json`, line 45 col 9 of the r62 counter).
- **after** (data at `54170404496c8d0385ded985c33ea7657aaab6b6`): counter exit 0, `predicate: true`,
  `findingCount: 0`; selftest `verdict=clean cases=22 passed=22`; ten declared
  negatives each exit 1 (`forgedGreen 0`); eight exact-line mutants each accept
  the live receipt and false-green exactly their declared negative
  (`mutantsSurviving 0`); cold-run stability STABLE with 4/4 identical PNG
  sha256; evidence dir 0 → 15 files.
- **stability, re-derived directly** (no reliance on the unpinned comparator):
  each receipt's four recorded sha256 equal its own PNG bytes (4/4 and 4/4) and
  the two runs' PNGs are byte-identical per step (4/4) —
  `controls/stability-direct.json`, verdict `STABLE-DIRECT`.
- **evidential limit (disclosed, from the wave):** the counter certifies
  internal consistency against the pinned driver bytes; it does not witness
  execution. `R63Reviewer` hand-wrote a receipt with four 1×1 PNGs
  (`w1/R63Reviewer/receipts/attacks/v12-fully-forged.json`, exit 0) and
  `R63MutDriver` produced a driver-side coherent fabrication (fake
  `window.scrollY` over an `overflow:hidden` page, exit 0) — both inside the
  claim's unauthenticated-receipt boundary, which this report widens from
  "changes the driver and passes the new pin" to "can hand-write a consistent
  receipt with the pinned driver". No capability row is recorded; the real-run artifacts (4+ independent driver invocations with
  real 14 KB PNGs, exact arithmetic, closure) are the demonstration, not the
  counter's green alone.
- **disposition:** the frozen predicate, kill rules and declared negatives all
  pass, but the cheapest do-nothing control (a hand-authored receipt with four
  1×1 PNGs) **meets the target**, so §9's pre-freeze standard is not met by the
  generation as declared. C1 is therefore reported **UNPROVABLE**, not admitted,
  no capability row enters, and the real runs plus the repair plan are kept for
  the next declared generation.
- score: coverage 9 held; delta 0.

**C2** — counting command:

```
node scripts/check-selfassessment.mjs --rev <LANDED_REV> --json
```

- **before** (sandbox clone at `f098bcf8` with the one round-62 artifact
  restored): exit 1, `mismatches: 2` — `m1-selftest-tally SCORECARD.md:3427
  claimed 44 observed 9`; `m3-unlanded-paths` (the gate labels it round 43 via
  its heading regex) claimed "landed" observed 1;
  `clean: false`. Receipt `controls/selfassessment-before.json`.
- **after** (lane at `5b7029ebd9ad96282e662a1225cb4762aa074cf1` with a clean worktree; first clean run at `54170404`, receipt
  `controls/selfassessment-after[-receipt]`): exit 0,
  `mismatches: 0`, `clean: true`; 142 could-not-evaluate and 59 superseded
  findings disclosed and not counted; gate bytes and selftest 45/45 unchanged.
- score: calibration 9 held (already above the saturation line; no rubric
  authorizes a numeric move on a gate repair); delta 0.

## Sources & frontier

`SOURCES.md` registry: **165 → 167 rows** (`node scripts/check-sources.mjs` →
`SOURCES_GATE verdict=clean rows=167 tiers=A:149,B:9,C:9
status=queued:15,mined:142,rejected:10 findings=0`).

- Rows added by tier: **B: +1** (S166 MDN WheelEvent — scoped delta-property
  semantics), **A: +1** (S167 CSSOM View — `scrollTop` getter definition);
  C: 0. Both opened 2026-11-04, quoted ≤25 words in the lesson Gate, status
  `mined`, `used-by` the new knowledge note and the round lesson.
- Rows touched old→new: **none** — no existing row's status, recheck or used-by
  changed this round.
- Census (contract command):
  - before — `scripts/sources-census.sh validate /fast/scratch/hyaku/tabi-r63/before-clone`
    (baseline bytes read from a sandbox clone; the lane no longer holds them
    untouched) → exit **0**, rows 165 (A 148 / B 8 / C 9), output
    `.ufo/waves/round-63/controls/census-start.txt`.
  - after — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
    → exit **0**, rows 167 (A 149 / B 9 / C 9), output
    `.ufo/waves/round-63/controls/census-end.txt`.
  - Both carry the 22 pre-existing W04 duplicate-URL warnings; no new E codes.
- Frontier rows advanced: the **wheel/scroll domain** is measured on the Linux
  Chromium surface and admitted as a knowledge note (74 → 75); it is **not** a
  repertoire move this round (C1 unprovable, no capability row). The domain's
  declared residuals stay frontier (horizontal scroll, `scrollend`, trackpad
  phases, ctrl+wheel zoom, cross-browser deltas).
- **Assimilation: none** — the round-57 quarantine register shift still blocks
  package adoption and the 38 hand-checks already stand committed (round-62
  lesson); `considerthese/` is absent for this lane, so one line says so and no
  proposal is mined. No keyup-value, kaidoku-overlap or planner-topology ruling
  is inferred.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | **improved** | knowledge notes 74 → 75 on ground the coverage map did not hold (the wheel/scroll domain), with two new mined source rows. **No capability row enters** — C1 is unprovable under the do-nothing standard; the expansion is the admitted knowledge entry and registry ground, not a repertoire move. |
| quality | **unchanged** | no admitted knowledge entry was re-verified, superseded or found stale this round; the new entry is an expansion move and the gate repair is calibration. No admitted entry failed a re-check. |
| discernment | **improved** | the fresh non-author r62 spot-check's three routed defects are answered by construction in this round — both producer polarities (R2), contradictory-duplicate and fabricated-label refusals (R3), and the artifact durability resolution (R1) — and its limits are retained, not rewritten (R4). The round-63 outside sample itself is still pending (a dispatched seat is still the lane). |

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Approval table, §Evidence ladder, §Runbook, §Wheel/scroll domain (round-63 section, pin `4c54e0c91de1`); prior non-author verification of the whole sufficiency claim is not claimed.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — round-63 wheel/scroll run (`corpus/evidence/round63/chromium-wheel-scroll/receipt.json`, two cold runs, closure proven); also `corpus/knowledge/multi-step-journey.md` §1–§2, §7 for the earlier journey.
- `[~]` Instructions executable by an agent without oral context — the round-63 §Wheel/scroll decision table plus `corpus/knowledge/chromium-wheel-scroll-round-63.md` §7 carry the copy-paste command and the negative/positive control rule; the earlier executor test (`executor-test-sufficiency.md` §0, §4) was a lane-dispatched seat, not non-author.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` scope check this round: the wheel/scroll interaction domain is browser craft and stays in province; no sibling surface is absorbed (connector scan reported in the wave dir); refusal routes unchanged.

## Routed defects / next-round obligations

1. **Bind the receipt to the run.** Render the invocation nonce into the page
   (pixels and/or DOM) and require a per-leg pixel signature; read
   `host.chromium`; bind `fixture.origin` to a server-log request count/status.
   Until then the counter's green is consistency evidence only (W1, W7).
2. **Pin every instrument before the freeze.** The stability comparator was
   authored after the pin list and left unlisted; it also compares only the a
   side's declared hashes (W2). The next freeze pins it and compares both sides.
3. **Declare a negative for every check named.** Sixteen checks have no negative
   (incl. `deltaMode === 0`, `isTrusted`, `scrollYAtDispatch`, `target-binding`,
   `page-final-state`, `driver-binding`, `schema`, `shot-records`), so
   `mutantsSurviving: 0` is scoped to the eight declared mutants (W5).
4. **Pin the page-side cross-checks.** `scrollEvents` must equal the count of
   non-prevented wheel events derived from the log and the legs (W3); `ts` order
   and modifier flags should be constrained (W5/W7).
5. **Fail closed on `ps` error** in the driver's sweep so closure fields cannot
   be vacuous (W6).
6. **Claims-file wording.** The C2 m3 finding's `round` field is 43 (the gate's
   heading regex), the m1 pair is a cross-instrument mis-association, and the C2
   kill rule's gate pin is not in `pins` (the blob `005bd45a…` is equal at
   baseline, freeze and wave commits). Frozen text stands; the reading is
   corrected here and in the lesson (W8).

## Round shape, extras, open questions

- **Shape:** ONE v1 wave of 12 seats (band 8–16), 6/12 attack seats (≥25 %),
  1 connector (≤2); residual ordinary calls: none. **Dead seats: 0**
  (12/12 settled, all outputs nonempty). Wave results:
  `.ufo/waves/round-63/w1-results.json`.
- **Round verdict:** **rejected-honest-stop** (C1 unprovable, C2 verified); no
  axis harmed; every score held (adjacency 8, coverage 9, depth 9, operability 9,
  freshness 9, calibration 9); knowledge 74 → 75, registry 165 → 167, no
  capability row.
- **Lane tip:** `5b7029ebd9ad96282e662a1225cb4762aa074cf1` (remote `refs/heads/master` verified by
  `git ls-remote`; `jj-lane.sh state` local=remote, ahead=0, behind=0, untracked=0).
- **L1 planner mapping:** the L1 held the canonical planner seat; the validator
  rejects a `planner` seat (recorded mapping, not bypassed).
- **Tool installs:** none.
- **Stale-lane:** respawn-per-round driver; this report closes round 63 and no
  other mission of this lane is open.
- **Open L0 questions (unchanged, unruled):** `tabi | round-44`/`round-61`
  planner/topology, `tabi | round-59` keyup-`cancelable` value rule, `tabi |
  round-59` kaidoku overlap ruling, plus the round-60 wide-hit adjudication.
  None is treated as answered; no routing change is inferred.
