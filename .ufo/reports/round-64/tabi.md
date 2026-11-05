# tabi — round 64 (attempt 1, resumed) — report

Lane: `tabi-shokunin` (browser and web-interaction craft). Round 64, hyaku run 15.
Claims: **C1** coverage — capability `chromium-wheel-scroll-domain-linux`,
generation 2 (a run-bound receipt plus a live re-run as the demonstration);
**C2** calibration — the lane's control receipts are re-derivable from committed
bytes (receipt-provenance gate). L1: `TabiR64`. Lane tip after this round:
`5dd531afad331aa0440b7b39790e302d272aadde`.

This round was launched three times before this attempt and each earlier L1 died
on provider failure (`lane-dead-no-report tabi round=64` at 22:32:15, 22:32:54,
22:33:31; attempt 1 had spawned the 12-seat wave at 21:53:15 and committed the
claims freeze, the pinned instruments, the pre-freeze controls and the wave
dispatch). This attempt inherited those bytes and re-verified all ten pins
before scoring: 10/10 sha256 match `claims.json` (`pins` map, re-hashed
2026-11-04), so the frozen instruments were reused unchanged and nothing was
re-frozen or narrowed.

## Work performed

Claim C1 (coverage / capability `chromium-wheel-scroll-domain-linux`) and claim
C2 (calibration / receipt provenance). Work items, each with its evidence:

- **Resumed and validated the inherited freeze.** `claims.json` pins re-hashed
  10/10 (`.ufo/waves/round-64/claims.json` `pins`; commands in the section
  below). Freeze `0fc68043` adds only `claims.json` to its parent `32726b8d`
  (pre-freeze controls), so the "controls before data" ordering holds.
- **Produced the SCORED evidence run.** The inherited evidence file was the
  pre-freeze design smoke (nonce `tabi-r64-smoke-design`), i.e. not a
  post-freeze pass. Replaced by a fresh run of the frozen driver at nonce
  `tabi-r64-scored-20261104`: `corpus/evidence/round64/chromium-wheel-scroll/`
  (`receipt.json` sha256 `4e3a95c1834fbaf19ccbb58267d413a81d1d947df90c0bfcea48041d0af0a86f`,
  six PNGs, `MANIFEST.txt` re-generated and `sha256sum -c` 7/7 OK). Byte-identical
  copy at `.ufo/waves/round-64/controls/scored/smoke/` is the control base.
- **Ran the C1 after-command.** `scripts/verify-live-r64.mjs` (frozen) re-ran the
  frozen driver twice cold and compared both runs with the evidence receipt:
  `predicate true, findings [], runs a/b exit 0 with counterExit 0/0,
  agreement.crossRun true, agreement.evidence true, driverSha256 ==
  1ff560cc7f34c709a6ec8847fec9b4b6a1b55bb4818b550ae41d1dcee2b92db5`
  (`.ufo/waves/round-64/controls/scored/live-verify.stdout`,
  `live-verify.command.json`).
- **Ran the frozen counter on the scored receipt.** `predicate true,
  findingCount 0, checks 29` (`controls/scored/counter-smoke.stdout`), and the
  counter selftest `TABI_R64_COUNTER_SELFTEST verdict=clean cases=31 passed=31`.
- **Re-ran the whole control battery at the scored data revision** `e3f52156`
  (`controls/run-controls-r64.mjs --rev e3f52156`, frozen): 12/12 controls pass;
  negatives `29 declared / 29 refused / forgedGreen 0`; mutants
  `16 applied / 16 killed / 0 surviving / 0 redundant`; red-before
  `r63-receipt exit 1 (14 findings), one-by-one exit 1, borrowed-shots exit 1,
  no-shots exit 1`, and the disclosed `synthetic-rendering` control unchanged
  at exit 0 (`controls/scored/{negatives,mutants}/matrix.json`,
  `controls/scored/summary.json`).
- **Ran the C2 after-command at the data revision**:
  `checked 15, matrices 0, failures 0, byCheck {}, requireCommitted true,
  ok true` (`controls/scored/gate-after.stdout`), exit 0. Before-state
  reproduced exactly from committed bytes: `checked 11, failures 34`
  (schema 11, stdout-bound 11, inputs-bound 11, argv-real 1) at `6c19979f`
  (`controls/gate-before.stdout`).
- **Integrated the wave's falsification.** Wave w1's ten reports were read in
  full; their findings are routed below and, where they are defects of the
  frozen bytes, folded into `corpus/QUALITY.md` 118 and the lesson's Mistakes.
  Two findings change the round's disposition: the verifier does not pin the
  driver it runs (H1), and C2's target is reachable without work (H5).
- **Frontier step.** Registry 167 → 169 (S168/S169, build-scoped Chromium
  155.0.8059.84 PDL rows opened and quoted this round; S153 re-opened in place,
  never duplicated); knowledge note re-pointed to the scored revision; a mistake
  mined per class (seven rows in `corpus/lessons/round-64.md` ## Mistakes); the
  duplication-URL guard proven (the `@master` row append was refused by the
  census and the row was re-opened instead); census before/after below.
- **Corrected two carried defects.** r63 spot-check D2 (SCORECARD:3465 printed
  194/58 where the receipts say 142/59) is corrected on the record in the round
  64 block; D1 was already closed in `SKILL.md` (`d376dc70…` true digest).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` →
  `M .scratch/run15-state.json` (orchestrator-owned, untouched) and an empty
  `mo.tip` (created 23:58 by another lane's seat; its content does not name this
  lane or round, so it was left in place and is reported, not moved).

## Landed changes

Every change is one commit; the round's `LOG.md` entry is the narrative.

| Commit | What it carries | LOG.md |
|---|---|---|
| `32726b8d` (inherited, re-verified) | frozen instruments + all failing-before controls, committed BEFORE the freeze | round 64 entry |
| `0fc68043` (inherited, re-verified) | `claims.json`: two claims, ten pins, kill rules, targets | round 64 entry |
| `70f52f6a` (inherited, re-verified) | w1 spec, validated 12-seat dispatch, ready handoff | round 64 entry |
| `e3f52156` | scored wheel/scroll evidence (fresh run, new nonce), scored control base, QUALITY 118 | round 64 entry |
| `382e83b1` | scored control receipts at `e3f52156`, knowledge note re-pointed, SOURCES 169, README r64 row under its own heading, SKILL round-64 pin decision row, lesson (Gate/Mistakes/wave), SCORECARD round-64 block, census end | round 64 entry |
| `5dd531af` | LOG.md round-64 entry | — |

Lane pushed: `git ls-remote origin refs/heads/master` →
`5dd531afad331aa0440b7b39790e302d272aadde` (pre-report gate, printed by the
command below).

## Before → after measurements

**C1 — coverage, capability `chromium-wheel-scroll-domain-linux`.**
Counting command (the claim's frozen `afterCommand`):

```
node scripts/verify-live-r64.mjs --scratch <ABS> \
  --driver scripts/chrome-cdp-loopback-round64.mjs \
  --counter .ufo/waves/round-64/counters/chromium-wheel-r64.mjs \
  --evidence corpus/evidence/round64/chromium-wheel-scroll/receipt.json \
  --evidence-shots corpus/evidence/round64/chromium-wheel-scroll --json
```

- before (baseline `6c19979f`): no r64 driver, counter, verifier or evidence
  (`git cat-file -e 6c19979f:scripts/chrome-cdp-loopback-round64.mjs` → absent;
  `git ls-tree -r --name-only 6c19979f -- corpus/evidence/round64/ | wc -l` → 0).
  The r63 generation's failure class re-derived this round: the committed r63
  receipt through the r64 counter exits 1 with 14 findings
  (`controls/scored/red-r63-receipt.command.json` exit 1).
- after, measured against `e3f52156` (receipt bytes landed there; the control
  receipts are committed at `382e83b1` and all name `e3f52156`):
  `predicate true`, `findings []`, two runs exit 0 with counterExit 0/0,
  `crossRun true`, `evidence true`, `driverSha256 1ff560cc…b92db5` (the pin).
  Counter `predicate true / findings 0 / checks 29`; negatives 29/29 refused
  with `forgedGreen 0`; mutants 16/16 killed, 0 surviving; selftest 31/31;
  four red-before classes refused. Verdict: **VERIFIED on its frozen predicate**.
  Limits disclosed: the counter is not an execution oracle (a synthesized
  rendering passes — `red-synthetic-rendering` exit 0), and the verifier does not
  check the driver digest against the pin (see routed defects).

**C2 — calibration, receipt provenance.**
Counting command (the claim's frozen `afterCommand`):

```
node scripts/check-receipt-provenance.mjs --dir .ufo/waves/round-64/controls/scored \
  --repo . --rev e3f5215615f68490230bd0c6db94f7d84f0fc084 \
  --require-committed --min-receipts 12 --json
```

- before (r63 controls at `6c19979f`): exit 1, `checked 11, failures 34`
  (schema 11, stdout-bound 11, inputs-bound 11, argv-real 1).
- after (scored population at `e3f52156`): exit 0, `checked 15, matrices 0,
  failures 0, byCheck {}, ok true`.
- Verdict: **measured, NOT admitted**. The after-state is real and re-derived,
  but the same target is reached by a population of never-executed receipts with
  invented stdout and matching digests (`w1/R64Reviewer` H5:
  `checked=14 matrices=2 failures=0 ok=true` on the frozen gate bytes), and this
  round froze no pre-freeze skip-the-work control for C2 — so §9's
  no-work standard is not met. Coverage/capability work is real; the calibration
  claim is an honest miss and is routed.

## Sources & frontier

Census command (round start and round end):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

- before: exit 0, rows 167 (A 149 / B 9 / C 9), output
  `.ufo/waves/round-64/controls/census-start.txt` (recorded at round start by the
  first attempt, unchanged since).
- after: exit 0, rows 169, output `.ufo/waves/round-64/controls/census-end.txt`;
  the only findings are the 22 pre-existing W04 duplicate-URL warnings (S123,
  S148, S156 among them).
- rows added by tier: **S168, S169** — both tier A, kind `code`, status `mined`,
  recheck `on-release`, build-scoped to Chromium tag `155.0.8059.84`
  (commit `5869fe313571d75152b77813cf0a4ee26a4e6df0`). Staged bytes:
  `.ufo/waves/round-64/w1/R64Scribe/sources/s170-chromium155-Input.pdl`
  (14,431 B, sha256 `5bbc6e23…c66e3d`, quote "Y delta in CSS pixels for mouse
  wheel event (default: 0)." at line 202) and
  `…/s171-chromium155-Browser.pdl` (12,079 B, sha256 `5e1faf7d…70da`, the
  `getVersion` response fields at lines 208–219). Both quotes were located by the
  L1 in the committed bytes this round.
- rows touched old→new: **S153** (re-opened in place at round start: `scope`
  gained the `Input.dispatchMouseEvent` delta-unit and `captureBeyondViewport`
  extension; `anchor` gained the 2026-11-04 re-fetch 1,423,215 B / sha256
  `cb4b0a40…` with two located quotes; `used-by` gained the r64 note and lesson;
  `status`/`opened`/`recheck` unchanged). A second row for the same URL was
  refused by the census (`W04` duplicate URL + `E05 kind=protocol`) and the row
  was re-opened instead.
- frontier rows advanced: `wheel-scroll` path extended by
  `wheel-scroll-build-scoped` (S168 → S169); the round-64 knowledge note enters
  `corpus/README.md` under its own round heading (the inherited row sat under the
  round-63 heading and was moved).
- Assimilation: **none** — the round-57 quarantine register shift still blocks
  package adoption and the 38 hand-checked rows stand committed (round-62
  lesson). `considerthese/` does not exist for this lane.
- Sourced claim: C1's method entry cites S168 (delta unit) and S169 (identity
  fields), both opened this round; the claim's evidence lands at the same commit.
- Frontier (declared, not held): horizontal scroll, `scrollend`,
  trackpad/momentum phases, ctrl+wheel zoom, cross-browser deltas, scroll
  snapping, third-party sites.

## Trend verdicts

- **expansion — improved.** A capability row entered `SCORECARD.md`
  (`chromium-wheel-scroll-domain-linux`, first-working round 64) with a
  re-runnable demonstration; knowledge 75 → 76 notes; registry 167 → 169 rows,
  both cited by the new note and the lesson. Evidence: the capability table row,
  `corpus/knowledge/chromium-wheel-scroll-round-64.md`,
  `.ufo/waves/round-64/controls/census-end.txt`.
- **quality — improved.** The round replaces r63's unprovable generation with
  instruments that re-run and that refuse the r63 failure class: 4 red-before
  classes refused (r63 receipt 14 findings, 1×1 PNGs, borrowed shots, no shots),
  counter selftest 31/31, 29/29 declared negatives, 16/16 frozen mutants killed.
  Evidence: `controls/scored/*.command.json` + matrices; the scoped limit (18 of
  30 independent counter loosenings survive) is routed, so this is a measured
  improvement with a named ceiling, not a claim of completeness.
- **discernment — unchanged.** C2's no-work standard failed and the round reports
  it as `measured, not admitted`; calibration stays 9. The round's own defect
  (evidence receipt was the pre-freeze design smoke) was found and corrected
  before the after-pass; two enforcement gaps were found by seats and routed.
  No score moves on this axis, so the verdict is `unchanged` rather than a claim
  of improvement.

## Round shape, seats and settlement

- Shape: **ONE v1 wave (`w1`) of 12 seats**, policy
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16), spec/dispatch `70f52f6a`,
  spawned 21:53:15 and adopted by the orchestrator (`w1.ready.dispatched`).
- Role mix: scout 1, executor 3, scribe 1, connector 1, reviewer 1, critic 1,
  mutation-tester 2, sentinel 1, revenger 1. Attack seats 6/12 = **50 %**
  (≥25 % floor). The canonical planner role is held by the L1 (the validator
  forbids `planner`); the connector seat carried the sibling-overlap scan.
- Dead seats: **R64Sentinel** (left no report and no receipts) and
  **R64MutDriver** (stopped after `instruments/`, no report). Ten seats left a
  report plus receipts; no seat was replaced and nothing was resent.
- Settlement: `w1-results.json` was never written — the L1 died at 22:32 before
  the dispatcher's handoff, so no `WAVE-DONE` reached this attempt. The
  settlement was reconstructed from `.ufo/waves/round-64/w1/swarm-registry.json`
  and the seat files, and is recorded above rather than implied.
- Residual call: **none**. The residual path (≤4 seats in one ordinary `task`
  call) is unavailable on this substrate: the validator's wave floor is 8, and
  the inline handoff forbids an L1 `task` call. Round total: **12 seats**.
- Seats never commit; the L1 integrated and scored. All wave findings are in
  `.ufo/waves/round-64/w1/*.md`.

## Routed defects (next round)

1. **Driver pin unenforced** (w1 `R64Reviewer` H1, `R64ExecDriver` findings 1–3):
   `verify-live-r64.mjs` hashes whatever `--driver` it is given and hands that
   hash to the counter, so a substitute driver exits 0 with zero browser
   executions (561 ms). Repair: compare against the claim's pin and refuse a
   mismatch, with its own control. Criterion: `corpus/QUALITY.md` 118.
2. **C2 no-work reachability** (w1 `R64Reviewer` H5): a fabricated population of
   12 receipts scores 0 failures; freeze a skip-the-work control before data.
   Also the gate's `^matrix` pattern never matches the battery's
   `negatives-matrix.json` aliases, so the scored run reports `matrices 0`.
3. **Counter conjunct coverage** (w1 `R64MutCounter`): 26 of 30 independent
   single-line loosenings survive the declared negatives; 18 accept a targeted
   forgery. The frozen 16 are all killed, so this is coverage debt, not a
   regression.
4. **Recorder timeout** (w1 `R64Critic` F24 + this round): the battery caps a
   command at 600 s while the verifier's own retry budget can need 960 s under
   fleet load; `live-verify` recorded exit -1 twice this round while the same
   frozen argv run directly took 11.8 s (attempts `[0,0]`).
5. **Verifier evidence agreement is shape-only** (w1 `R64Reviewer` H3.4): the
   evidence receipt's nonce never needs to match a live run; disclosed in the
   claim's limits, routed as a hardening item.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — `SKILL.md` §Wheel/scroll domain generation 2 (`:3071`), instrument
  table + decision rows including the new driver-pin row; all four boxes remain
  author-asserted (`SHONEN.md`), no named non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  round-64 entry + `corpus/knowledge/chromium-wheel-scroll-round-64.md`; the run
  is re-executable by the verifier, but the non-author judgment is the closure's.
- [~] Instructions executable by an agent without oral context —
  `SKILL.md` run commands for driver/counter/verifier/gate; executed this round
  by the L1 and by w1 seats from the same text.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — connector seat's
  sibling scan: 0 same-surface lines across 20 lanes, 0 registry collisions,
  119 adjacent boundaries explicitly not absorbed (`w1/R64Connector.md`).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Wave evidence and inherited state

- Inherited from the died attempts and reused after re-verification: the claims
  freeze, the pinned instruments, the pre-freeze control battery, the w1 spec/
  dispatch and all eleven existing seat artifact trees.
- Replaced after re-verification: the evidence receipt (design smoke → scored
  run at `tabi-r64-scored-20261104`), the `scored/smoke` control base, and the
  red-before/negatives/mutants outputs (re-derived at the data revision).
- Discarded: nothing of the seats' work; the design-phase `smoke-live` receipt
  was moved to `.ufo/waves/round-64/controls/design/` (not deleted) so the
  scored population contains only revision-bound receipts. Every counted receipt
  is listed by the gate run above (`checked 15`).
- Tool installs: **none** (node v24.21.0, Chromium 155.0.8059.84 already
  present; pacman stays paused). No new L0 question filed; the existing
  keyup/overlap/topology L0s remain open and unruled.
