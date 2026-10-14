# xconnector — cross-lane seat over wave-9 moves (audio r70 / g2d r69 / g3d r78)

Seat: xconnector, wave `shokunin-train-20261014-w9`. Read-only across lanes;
no dispatches, no tracked writes. Scratch: `xconnector-scratch/evidence-notes.md`.

**Timing caveat (declared):** ran while all three author lanes are in flight —
no `reports/round-{70,69,78}/` exists. Committed state: audio `939fe47` (r69
work `30bb86d`), g2d `5d66b4d` (r68 work `f754546`), g3d `71818b7` (r77 work
`35dfbe2`). In-flight scratch observed but not judged: audio
`r70-{scribe,critic}` (independent hold-ladder drivers), g2d
`r69-{scribe,simplifier}` (pre-author fixture snapshots), g3d
`r78-{scribe,boundary,critic,simplifier}` (own-geometry permanence probe
already run at {20,60,120,300}f). Wave-8's connector transfers (T2a/T2b/T2c,
g2d-F3, g3d-F1) became this wave's declared moves verbatim — this report does
not re-propose them.

## The three moves, one-line mechanisms

| lane | declared move | mechanism under test | unit |
|---|---|---|---|
| audio r70 | `fifo_writer_hold_s=1.0` laddered {0,0.05,0.2,0.5,1.0,2.0}s × `dec_act` + chunked `fifo_feed` | ffmpeg bridge open-#2 needs an attached writer; hold is an unmeasured determinism bound (r67: bare writer races open-#2 5/5, one run blocked >10s) | wall-clock seconds |
| g2d r69 | `midline_offset_ms=80` fixed, sweep `gap_ms` {50,100,200,400,800} (`descendant_pipe_probe.gd` `OS.delay_msec(200)`) + `sha256(merged)` per dual_classify | is the fabrication window gap-relative (`offset<gap`) or an absolute write-latency constant — the referent question the offset ladder cannot express | pipe-time milliseconds |
| g3d r78 | `map_off` permanence ladder {20,60,120,300}f + callsite pair arms (coroutine-resume vs `_physics_process`) | "stale forever" measured only to +15f (r76-adjudicator: "not a proof of unboundedness"); `bb_physmut` +1-tick callsite shift is scratch-level only | physics frames |

## Axis 1 — pattern transfer

### 1a. Is a shared 'laddered bound' receipt idiom worth converging? **Yes — and the lanes are already converging piecemeal; what is missing is the boundary typing.**

All three ladders emit *rung × verdict × rep-distribution* cells:

- audio r70 (declared + in-flight): `hold_ladder` cells —
  `{fifo_feed, fifo_writer_hold_s, reps[], verdict_distribution}` where the
  distribution key is the r67 signature 5-tuple `(detected, route, exit,
  samples, error)`. r70-scribe's independent driver uses the identical shape.
- g2d r68 (landed): 6 offsets × 3 reps → `measured_window
  {landed_offsets_ms, missed_offsets_ms, mixed[], lo_edge_ms, hi_edge_ms}` —
  cells are landed/missed/mixed counts.
- g3d r77 (landed): `ladder {bound, groups, sizes}` — bound = first sample
  index whose `_tuple_sig` differs, *derived from the partition*; r78's
  permanence ladder is the same shape over {20,60,120,300}f.

The parts that differ — and where the receipt idiom should be shared — are
the **boundary semantics** and the **observer disclosure**:

```
laddered_bound := {
  swept: {param, unit: wall_s|pipe_ms|frames|turns, rungs: [...]},
  cells: [{rung, reps, verdict_distribution: {signature -> count}}],
  boundary: {kind: threshold_first_stable        # audio h*
                  | window_band                  # g2d [lo,hi) + mixed
                  | first_divergent              # g3d bound=N
                  | none_through_max_rung        # g3d permanence (asymmetric)
                  | binary_on_condition,         # audio waitclose collapse
            at: rung | [lo,hi] | omitted_rungs },
  referent: <what the bound is relative to>,      # see 1c
  observer_schedule: {...}                        # see 1b
}
```

The `none_through_max_rung` kind matters: g3d's permanence ladder is
asymmetric — it can only falsify (a late flush becomes the bound) or extend
coverage. Recording it with the same "bound" vocabulary as a threshold would
be a real semantic drift (see axis 3). The `binary_on_condition` kind covers
audio's declared alternative — verdict binary on writer-attached-at-open-#2,
h* collapsing to a condition, not a constant.

### 1b. Are the three races the same observer-perturbs-edge mechanism? **Same genus, three species — and the discriminating axis is *where* the observation perturbs.**

| | g3d mark-vs-phase | audio writer-attach | g2d write-position |
|---|---|---|---|
| edge measured | serve boundary w1-vs-w2 (sync publish) | open-#2 resolution (blocked vs au-magic vs decode) | arrival order vs tail_flush |
| observer perturbs | SUT's internal scheduling state — forcing read marks map dirty, next phase publishes early | SUT's external precondition — open-#2 blocks unless a writer is attached | the stimulus channel — ~2.5ms spawn latency shifts nominal→effective; ~1ms stochastic band |
| perturbation site | **SUT-state** | **external precondition** | **stimulus channel** |
| de-perturbable? | no — the read IS the perturbation; only the protocol can be pinned | yes — a waitclose writer makes the verdict condition-pinned, not timed | partially — shift calibratable, band remains |

Evidence: g3d r77-adjudicator ("read-history perturbs the measured edge
under force"; jitter rate context-dependent ~63% arm vs 4% probe — a phase
artifact, not a constant); audio r67-author ("the linger is what makes the
arm deterministic"; 5/5 race, one >10s block); g2d r68-adjudicator (strict
bound on write-position; nominal edge = gap − spawn overhead; transition
band ~1ms).

**Not the same mechanism.** The honest commonality is one level up: each
measured edge is an ordering between the SUT's phase clock and the harness's
event schedule — so the receipt must pin *both* clocks. The three lanes'
second axes are complementary halves of that disclosure: audio's
`fifo_feed` variant and g3d's read-cadence sweep the *observer-side*
schedule; g2d's gap sweep and g3d's callsite pair sweep the *SUT-side*
schedule (which timed flush / which drain the event enters).

A fresh in-flight corroboration: g3d r78-scribe's own probe ran a `:force`
arm under mapoff at every rung — `map_iter` stays frozen (`iter_delta=0`),
served tuple stays STALE. Forcing reads under an *inactive* map are inert:
the mark-vs-phase channel has no scheduled phase to advance once the map
leaves the sync iteration. This refines the mechanism — the race needs the
map *in* the iteration — and turns "permanence" into "the perturbation
channel itself is switched off", a stronger statement than a bounded wait.

### 1c. The referent question transfers before it is asked

g2d r69 is the only lane explicitly testing what its bound is *relative to*
(gap-relative vs absolute). The same question already applies to the other
two, and both briefs half-ask it:

- **audio:** if the r70 ladder finds the verdict binary on
  writer-attached-at-open-#2, then `hold_s` was never the referent — it is a
  wall-time proxy for attach-state. The `waitclose` feed (already in
  r70-scribe's driver, labeled "h*=0 semantics") is exactly the referent
  arm. If instead a plateau h* < 1.0s exists, the referent is real time —
  and the next-order question becomes the plateau's width and shape.
- **g3d:** the callsite pair tests whether the *referent clock* is
  await-count (coroutine turns) or tick-index (physics drain) — the r76
  +1-tick shift says the serve edge is counted in different units depending
  on which clock the write entered. That is the gap-relative-vs-absolute
  question in physics-frame units.

## Axis 2 — next-order frontier proposals (per lane; concrete, falsifiable, cheap)

**audio (post-r70):**

- **A1 race-band shape below the plateau** *(g2d's transition-band semantics
  transplanted)*: if a plateau h* exists, dense rungs {0,10,25,50,100}ms ×
  N≥15 on `dec_act` — does P(stable-verdict) rise monotonically with hold
  (band = scheduling-latency width) or step sharply (binary-on-attach at
  coarse resolution)? Falsifiable either way; one member; scratch-then-flag.
- **A2 orphan-receipt field**: r70-{scribe,critic} both noticed that a
  timed-out fifo arm can leave a blocked `ffmpeg -i` grandchild —
  `subprocess.run(timeout)` kills only the sox parent. Pin
  `orphans_after_cell` (pgrep count) in the ladder receipt so a `blocked:`
  verdict also discloses what it leaked. Receipt-only addition; zero new
  physics.
- **A3 `arm_timeout_s` ladder** (w8-T2d residual): the one remaining point
  constant in `transport_protocol` — is `blocked:` at 10s a verdict or an
  artifact of the bound? Two rungs {10, 30}s on the h=0 oneshot cell answer
  it. Cheapest possible ladder; mostly bookkeeping.

**g2d (post-r69):**

- **G1 the dead corner of the (offset, gap) plane**: gap < spawn latency
  (~2.5ms) ⇒ no nonnegative offset can land inside — fabrication becomes
  impossible at *any* offset. Rungs gap ∈ {1,5,10}ms × offset {0,50}ms
  predict all-miss cells; a single fabrication there falsifies the
  write-position model itself. Extends the declared crossed ladder into the
  region where the referent question has a sharp answer.
- **G2 digest discriminating-power negative control**: `sha256(merged)` is
  asserted to catch concat-order drift — demonstrate it once on scratch: a
  consumer concatenating stderr+stdout (the r66 caveat order) must yield a
  different digest on identical channels. One run; converts the field from
  declared-gate to measured-gate. Caveat to carry: digests bind *decoded
  text* (r68's b"\xff"≡b"\xfe" collision) — raw-byte drift that decodes
  identically stays invisible.
- **G3 straddle as a first-class cell outcome**: the ~0.1ms H-E-T-E2
  regime is currently narrative; a dense-offset cell band near the edge
  (e.g. 197–199ms at 0.25ms steps × more reps) either resolves it into
  landed/missed or pins it as a named third verdict — three-valued cell
  semantics the shared idiom can already carry.

**g3d (post-r78):**

- **D1 reactivation edge × inactive-window read-cadence**: in-flight scratch
  already shows force-under-mapoff inert (iter frozen); the next-order arm
  is `mut_map_cycle` with srv_get/force calls interleaved *during* the
  inactive span — falsifiable claim: the post-reactivation +2f clamp is
  read-history-invariant (predicted by "an out-of-iteration map cannot be
  marked"). One arm; reuses declared machinery.
- **D2 jittered cell as a pinned distribution** *(g2d's mixed-cell semantics
  transplanted)*: r77 *skipped* the jittered w1 serve cell and pins w0/w3.
  With per-cell `verdict_distribution` (audio's r70 shape), w1 becomes
  pinnable as a distribution with a disclosed protocol — turning a skipped
  rung into measured data. Receipt + arm-level only.
- **D3 third callsite**: if r78 confirms the {coroutine, physics} pair,
  complete the context ladder with a deferred-signal (`call_deferred` /
  `await`-on-signal) callsite — prediction: −1 tick relative to coroutine,
  same as `_physics_process` if both drain in the same phase.

## Axis 3 — drift bookkeeping between lanes' conventions

- **Mixed-cell policy — the real divergence this wave.** Three answers to a
  nondeterministic cell: g2d records `mixed` inside a declared transition
  band (landed); g3d r77 *skipped* the jittered w1 rung and pins only stable
  cells (landed, disclosed); audio r70 records per-cell verdict
  *distributions* (declared + in-flight). Consequence: the same physical
  fact — a jittered edge — lands as "band", "omitted rung", or
  "distribution" depending on lane. The shared idiom's `boundary.kind`
  makes all three expressible, but without it a cross-lane census cannot
  compare edges.
- **"Bound" referent drift**: audio's swept unit (wall-s) may be a proxy for
  a boolean attach-state; g2d's swept unit (nominal ms) is a proxy for
  write-position after a ~2.5ms channel shift; g3d's unit (frames) is
  callsite-dependent (−1 tick from `_physics_process`). All three pin the
  proxy; only g2d's r69 crossed ladder tests the referent. If audio's h*
  collapses to binary-on-attach, the lanes will have one bound of each kind
  — duration, position, condition — under the same word.
- **Boundary-kind vocabulary**: g3d `bound=N` (partition-derived first
  divergence), g2d `measured_window{lo,hi,mixed}` (threshold band), audio
  `hold_ladder` (sufficiency threshold). Same word family, three semantics.
- **Timeout disclosure asymmetry persists** (w8-T2d, still open): audio pins
  `arm_timeout_s` in-receipt and its `blocked:` verdict is *defined* by it;
  g2d `timeout_seconds` and g3d arm timeouts live in runners only. New this
  wave: audio's h=0 cells produce `blocked:` verdicts *and* can leak ffmpeg
  orphans — timeout is load-bearing for the verdict and has a side-effect
  neither sibling lane's convention would catch.
- **sha256(merged) inherits the decoded-text limit**: r68's digests bind
  post-decode text (boundary-measured collision b"\xff"≡b"\xfe"); r69's
  merged digest gates concat-order of decoded text, not raw bytes. Not a
  regression — a named limit to carry in the receipt's doc.
- **Flag-naming drift widens**: audio's `--probe-fifo-hold-ladder-r70` is
  round-suffixed (119→ growing flag set); g2d's declared
  `--probe-midlineforge-gapladder` is mechanism-named with no round; g3d
  stays `mut_*` CASES rows. Audio keeps provenance grep-trivial at the cost
  of flag growth — the drift is in where provenance lives.
- **Verdict-distribution convergence without coordination** (positive):
  audio r70-scribe's independent runner emits `verdict_distribution` cells
  identical in shape to the declared `hold_ladder`; the idiom is converging
  organically — naming it makes it durable.
- **Convergent (no drift):** report path shape, scratch scope, sha256-pinned
  receipts, `git archive HEAD` baseline freeze, LEAF + evidence binding,
  newest-first additive arms, prior-rows-byte-stability invariant (three
  implementations, one claim — unchanged from w8).

## Proposed move (one bounded)

**Converge the three lanes on the typed `laddered_bound` receipt idiom —
cells = rung × verdict-distribution; `boundary.kind` ∈ {threshold_first_stable,
window_band, first_divergent, none_through_max_rung, binary_on_condition};
mandatory `referent` and `observer_schedule` fields — and spend each lane's
next frontier on another lane's axis question (audio A1 race-band shape;
g2d G1 dead-corner / G2 digest negative control; g3d D1 read-cadence ×
reactivation, D2 distribution-pinned jitter).**

This is a compatible synthesis: it adopts what all three declared moves
already emit, adds two fields that are pure disclosure (what the harness did
and what the bound is relative to), and types the boundary so the g3d
asymmetric ladder and a possible audio binary collapse stop masquerading as
the same object.

## Affected axes (this round's declared set: expansion / quality / discernment)

- **discernment ↑**: referents and boundary-kinds become explicit — the
  three "races" stop being conflated, and each bound names the clock it is
  measured against.
- **expansion ↑**: three concrete next-round frontiers per lane, each
  falsifiable, each already reachable by existing machinery (no new harness
  classes).
- **quality ↑**: mixed-cell policy becomes a typed field instead of a
  per-lane habit; the orphan/timeout side-effect class gets a receipt field.
- No axis regresses: all additions are additive receipt fields + opt-in
  probes; the idiom renames nothing already landed.

## Risks

- **Convention drift risk**: the idiom is a shared habit, not a contract —
  lanes adopt it only if next wave's briefs name the fields. Cheap fallback:
  even field-name parity on `verdict_distribution` + `boundary` alone
  captures most of the value.
- **Audio outcome dependence**: if h* collapses to binary-on-attach, the
  "ladder" degenerates to a condition pin — the idiom still fits
  (`binary_on_condition`) but the frontier A1 dissolves into a
  simplifier-grade move (constant → protocol). Either way it lands.
- **Distribution-pinning costs reps**: a jittered cell needs N≥3 (r68 needed
  3 for mixed-cell semantics; r70-scribe uses 15/25). Bounded but nonzero —
  lane authors should size reps to the edge's jitter width, not globally.
- **Referent tests can return "neither"**: g2d's dead-corner could show a
  third regime (e.g. channel saturation); that is still measured signal, but
  it lengthens the frontier. Disclosed, not smoothed.
- **In-flight evidence is pre-adjudication**: the g3d force-under-mapoff
  inertness and the ladder scripts are sibling scratch — data for the
  parent, not landed truth.

## Verification

- Committed refs spot-checked: `measure_audio.py:197,278-295,319-320`;
  `descendant_pipe_probe.gd:164-181`; `run_battery.py:2529-2531,2776-2778`;
  `navagent3d_detour.gd:1527-1600` (`mut_map_off` +15f arm, `mut_map_cycle`
  +2f reactivation), `:209-227` (r77 force/ladder header).
- Prior reports: audio `r67-author` (:71-80 race evidence), `r69-adjudicator`
  (ADMIT); g2d `r66-author`:215-216 (concat-order caveat), `r68-author` +
  `r68-adjudicator` (write-position bound, band, decoded-text digest limit);
  g3d `r76-adjudicator` (+15f bound, callsite qualifier), `r77-adjudicator`
  (mark-vs-phase, w1 skip, jitter-rate context-dependence).
- In-flight scratch: audio `r70-scribe/run_hold_ladder.py` (waitclose feed,
  killpg runner, verdict_distribution), `r70-critic/ladder.py` (orphans());
  g3d `r78-scribe/runs/perm_w{20,60,120,300}` (all STALE, force-inert,
  iter_delta=0); g2d `r69-simplifier/*.pre-author.*` snapshots.
- Wave-9 briefs: `tasks/{audio,g2d,g3d}-author.txt` (declared moves verbatim);
  wave-8 `xconnector-report.md` (prior transfers, now landed as these moves).
- No re-execution of lane probes; no verdicts on in-flight work; the baseline/
  corpus-hygiene observations stay with xsentinel's scope.

## Limits

- Post-landing re-resolution: A1–A3/G1–G3/D1–D3 assume the declared moves
  land roughly as measured so far; a falsified declared claim reorders the
  frontier, not the idiom.
- Mechanism taxonomy is report-verbatim + file:line checks — no probe runs
  (read-only seat).
- The `laddered_bound` schema is a proposal for lane conventions; nothing
  here modifies contract, axes, or judgment.
