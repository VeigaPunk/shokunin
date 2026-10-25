# xconnector — cross-lane seat over wave-8 moves (audio r69 / g2d r68 / g3d r77)

Seat: xconnector, wave `shokunin-train-20261014-w8`. Read-only across lanes; no
dispatches, no tracked writes. Scratch: `xconnector-scratch/` (evidence notes +
command outputs).

**Timing caveat (declared):** this seat ran while all three author lanes are
still in flight — no `reports/round-{69,68,77}/r*-author.md` exists yet;
in-flight scratch observed: audio `corpus/live/r69-{scout,boundary,reviewer,
scribe}/` (scout already probing `nm_zeros.{wav,bin,txw,f32,snd,au,raw,xyz}`),
g2d `corpus/live/r68-{baseline,boundary,reviewer,simplifier}/`, g3d
`corpus/live/r77-{baseline,reviewer,simplifier}/` (no r77-author dir yet;
g3d `git status --porcelain` = 0). Analysis below is therefore **declared-move
× committed-state** (audio r68 `6c91040`, g2d r67 `1101cb3`, g3d r76
`3ab09fd`/`8a67f71`), not post-landing. Where a transfer depends on a wave-8
result I mark it `[pending-landing]`.

## The three moves, one-line mechanisms

| lane | move | mechanism under test | receipt shape |
|---|---|---|---|
| audio r69 | ext-suffix sweep + dead-CHECK census | same no-match bytes under ≥5 names → does the fallback/detection fork on extension alone; `.snd` is the first name-gated DETECTION fork (sndr row `formats.c:247-248`, the only ext-parameterized CHECK) | per-ext verdict groups over 4 transports; `rows_hit`/`rows_dead` census |
| g2d r68 | fabrication-window offset ladder + receipt upgrades | descendant write at {0,40,80,120,160,240}ms into the 200ms signature gap (`descendant_pipe_probe.gd:129` gap_ms=200, `:159` `sleep 0.08`) → measured [lo,hi) window bound | `divergent_clause` signature {exit,signature,error_scan,blob,allowlist_shape} per divergence row + sha256(raw_stdout/stderr) same-input gates |
| g3d r77 | apply-order + map_force_update + wait-ladder verdict-groups | `_apply_mutation` fixed order delete→recreate→transform→link→agent→map_active (`navagent3d_detour.gd:1841-1873`) load-bearing or inert; force_update's edge collapse scope; window bound as partition boundary | verdict-groups receipt over the wait ladder |

## Axis 1 — pattern transfer (measured structure → untested analog)

### T1 — verdict-groups × divergent-signature receipts (three-way, already converging)

The three lanes are independently landing the same receipt idiom — a partition
of observations by identical signature — with complementary strengths:

- **audio (landed r67):** `transport_verdict_groups` partitions 4 transport
  arms by signature `(detected, route, exit, samples, error)` — but records
  groups WITHOUT naming which signature field discriminates them.
- **g2d (declared r68):** `divergent_clause` names the discriminating field
  per row {exit,signature,error_scan,blob,allowlist_shape} — but keeps the
  per-row `divergent` bool rather than a signature partition.
- **g3d (declared r77):** partition-boundary form — the window bound IS the
  boundary between adjacent groups on an ordered ladder.

Transfers (all additive, all cheap — three are pure receipt restatements):

- **T1a audio←g2d:** annotate `transport_verdict_groups` boundaries with the
  discriminating fields. On committed r67 data the field set is derivable
  without a single rerun: within-member forks never differ on `detected`
  (r67 headline: "detection itself never forks"); the gsrt 2-group split is
  discriminated by `error` alone (same route/exit/samples class), the act
  3-group split by {exit,samples,error}. The r69 `.snd` arm is where
  `detected` first becomes a discriminator — naming that field in the receipt
  is exactly what makes the r69 claim ("detection forks on name") legible
  rather than narrative. Cost: receipt-shape upgrade, zero new runs.
- **T1b g2d←audio:** partition the 9-row `divergence_table` into
  (merged,streams)-signature groups {T,T}/{T,F}/{F,T}/{F,F} — the r67 LOG's
  "4 families" is currently carried as per-row bools + prose; the group form
  is audio's committed shape verbatim. Cost: restatement of r67 payload.
- **T1c g2d←g3d `[pending-landing]`:** record the fabrication-window bound as
  a partition BOUNDARY between adjacent offset groups (lands {0..hi} vs
  misses {hi..240}), not only a per-offset table — the g3d r77 receipt idiom
  applied to the ordered ms-axis. Same for audio's unordered ext axis: bound
  is degenerate (no order), which is itself worth pinning — an unordered
  verdict-groups receipt can't express "edge", only "classes".
- **T1d all three:** converge on one receipt idiom — `verdict_groups`
  (signature→members) + `divergent_fields` (minimal discriminating set) +
  `boundary` (ordered axes only). Each lane's next round can adopt additively;
  a shared shape is what makes x-lane census tooling (axis-2 F5) possible.

### T2 — timing-constant bound ladders (the family the brief names)

| lane | constant | status |
|---|---|---|
| g2d | descendant write offset vs 200ms gap | **r68 laddering** {0,40,80,120,160,240}ms → [lo,hi) |
| g3d | post-mutation wait (physics frames) | **landed r76**: per-class edges {link:2, region:3, agent:0, map_off:∞(to +15f)}; r77 receipts as verdict-groups |
| audio | `fifo_writer_hold_s=1.0`, `arm_timeout_s=10` | **point constants, never laddered** — the untested analog |

- **T2a audio (the gap):** `fifo_writer_hold_s=1.0` was chosen because a bare
  one-shot writer races the bridge's second open (r67-author: 5/5 shell runs
  → exit 2 au-magic; one python run blocked >10s) — i.e. the hold sits
  *somewhere* above a determinism bound nobody measured. Ladder it:
  {0, 0.05, 0.2, 0.5, 1.0, 2.0}s × the `dec-act` member (the arm that needs
  open-#2), plus one chunked-feed variant on `fifo_feed`. Falsifiable:
  a minimum hold h* < 1.0s exists and is stable; or the verdict is binary on
  writer-attached-at-open-#2 (h*=0 with a blocking writer). Scratch-level
  probe, no tracked edits needed for the measurement.
- **T2b g2d (crossed ladder):** the offset ladder alone cannot distinguish
  *gap-relative* from *absolute-time* bounds. Hold offset=80ms, sweep the gap
  {50,100,200,400,800}ms — if the window follows `offset<gap` it's relative;
  if it follows absolute write latency it's not. Cheap: one fixture constant
  becomes a parameter (gap_ms already a constant at `:129`).
- **T2c g3d:** bound the "∞". `map_off` permanent-stale is measured only to
  +15f/forcing-call coverage (r76-adjudicator bound note: "not a proof of
  unboundedness"). Observation ladder {20,60,120,300}f — one arm, four waits;
  either deepens the bound or finds the flush. Same family as the g2d gap
  ladder: extend the axis, not the claim.
- **T2d all three:** the give-up constants are all unladdered point values —
  audio `arm_timeout_s=10` (pinned in `transport_protocol`), g2d
  `timeout_seconds=60|8` (`run_battery.py:298`), g3d `timeout 30` arm
  invocations. Audio already records its timeout in-receipt; g2d/g3d record
  it only in the runner. Cheap receipt parity: pin the timeout per arm, the
  way audio does — a blocked/blocked-verdict bound is only auditable if the
  receipt names it.

### T3 — ext-gated CHECK ↔ allowlist preemptor ↔ apply-order (ordered-clause tables)

All three lanes test whether position/gating inside an ORDERED clause table
is load-bearing:

- **audio:** CHECK table is first-match; exactly one row is name-parameterized
  (`sndr`, ext=="snd" ∧ \0\0@0). r69 measures the ext-gate's verdict effect.
- **g2d (landed r66):** the allowlist is a preemptor INSIDE clause-1 only;
  blob clauses (SCRIPT ERROR:, Parse Error:, ObjectDB) are allowlist-immune
  and preempt it — clause order measured live (r66-critic CE-1a).
- **g3d (declared r77):** `_apply_mutation` dict order — same "does order
  matter" question, one level down (setters, not classifiers).

Transfers:

- **T3a audio←g2d:** preemptor-ordering probe on the CHECK table — craft a
  `.snd` member whose bytes satisfy BOTH the sndr row (\0\0@0) AND another
  row's magic (e.g. a `de`/`dec`-family header). Does the ext-gate reorder
  first-match, or does row position still win? This is g2d's
  blob-vs-allowlist method transplanted to detection. Cheap: byte-edit of an
  existing member shape; scratch probe first.
- **T3b g2d←audio (dead-gate census):** audio's r69 census asks which CHECK
  rows ever matched. g2d's analog: r66's census found dead CLAUSES (SCRIPT
  ERROR:/Parse Error: 0 lines in-run) but never asked which allowlist
  ENTRIES are dead *because their row can't emit matching output* — a
  reachability census over the 39 `expected_errors` rows. The
  `{exit,signature,error_scan,blob,allowlist_shape}` signature (r68) already
  names the clause; applying it to the census is a receipt upgrade, not a run.
- **T3c g3d (already absorbing g2d's method):** the r77 apply-order arm IS
  the clause-order probe — worth recording that the map_active-last comment
  (`navagent3d_detour.gd:1869-1871`) is audio's ext-gate in disguise: a
  position-gated row whose semantics depend on evaluation order. If r77 finds
  order inert everywhere EXCEPT map_active-last, the three lanes converge:
  order is load-bearing exactly at gate-valued rows.

## Axis 2 — next-order frontier proposals (per lane; concrete, falsifiable, cheap)

**audio (post-r69):**

- **F1 hold-ladder** (T2a): measured determinism bound for
  `fifo_writer_hold_s`. Falsified if verdicts don't stabilize on a clean
  [h*,∞) plateau — itself a measured result.
- **F2 ext-gate order probe** (T3a): `.snd` bytes colliding with a second
  row's magic. Falsifiable both directions; one member + 4 transports.
- **F3 death-cause partition:** r69 lands `rows_dead`; the next order
  partitions dead rows by cause {ext-gated, byte-gated, handler-absent-in-
  build}. Receipt-only upgrade over committed data — zero runs.
- **F4 `|cmd` popen arm:** the only `lsx_io_pipe` transport, noted unprobed
  since r68. Claim: post-table `|cmd` input gets `filetype="sox"` → a verdict
  class outside all 4 tracked arms. One additive transport arm.
- **F5 `--magic`/`use_magic` arm:** explicitly flagged unexercised in
  r68-author limits; same shape as F4.

**g2d (post-r68):**

- **F1 gap-duration ladder** (T2b): distinguishes gap-relative vs absolute
  window — the question the offset ladder can't answer alone.
- **F2 allowlist×blob in-run preemptor pin:** forge a line matching an
  allowlist entry AND a blob clause (`SCRIPT ERROR:` allowlisted) — makes
  r66-critic's static order claim a live CASES row. One arm.
- **F3 sha256(merged) gate:** extend the r68 same-input hashes to the merged
  concat — catches concat-order drift (the stderr+stdout consumer caveat
  carried since r66). Receipt upgrade only.
- **F4 cross-row forgery:** allowforge with a DIFFERENT row's real entry
  ("each is a per-case preemptor" — r66-author noted untested cross-row).
  Reuses the r66 chassis; one arm.
- **F5 divergent-clause census** (T3b): signature-extend the dead-clause
  census; receipt upgrade over existing captures.

**g3d (post-r77):**

- **F1 callsite ladder:** r76-critic's `_physics_process` +1-tick shift
  (`bb_physmut`) is a scratch finding, not a CASES row — pin the same
  mutation from {deferred, physics-callsite} contexts. Two arms.
- **F2 map_off bound ladder** (T2c): {20,60,120,300}f — deepens or breaks
  the permanent-stale claim. One arm.
- **F3 order×window interaction `[pending-landing]`:** if any r77 order-pair
  diverges, bisect whether the divergence is a serve-edge shift or a state
  difference — connects the r77 order axis to the r76 window axis. If all
  converge, the falsifiable next-order is a 3-setter hand-ordered sequence.
- **F4 serve-edge census:** remaining mutation keys without pinned edges —
  `link_layers`, `region_layers`, `region_delete` (r76-author residual,
  `r76-author.md` "open edge"). One wait-ladder arm per key; the audio
  dead-CHECK census pattern applied to mutation coverage.
- **F5 force_update×wait bisect `[pending-landing]`:** if r77 shows the
  serve edge survives `map_force_update`, does forcing shift it 2f→1f?
  Bisect {0,1,2} under forced getter — completes the two-stage model.

## Axis 3 — drift bookkeeping between lanes' conventions

(Overlaps xsentinel's w7-F3/security scope only where noted; this is
convention drift, not the adversarial audit.)

- **Receipt tracking — three different answers.** audio TRACKS seat scratch +
  shared receipts: 16,404 files under `corpus/live/` including `runs/` (4,670
  receipt files — `git ls-files`), `r66-boundary` (2,054), even
  `r62-author/scratch/bisect/*.wav` binaries. g2d tracks `live/` minus
  `runs/` + `edge-verdicts.json` (`corpus/.gitignore`,
  `corpus/live/.gitignore`) — 38,543 files, mostly legacy round-era mass.
  g3d ignores ALL of `live/` (`corpus/.gitignore` line 1) — 0 tracked, clean
  status. Consequence: audio's r69 dead-CHECK census greps "all committed
  receipts" — possible only where receipts are committed. The same census in
  g3d must replay the battery or mine CASES expectations; in g2d it's split
  (seat scratch committed, shared `runs/` not).
- **Baseline compliance observation [xsentinel-owned]:** g2d r68-baseline is
  archive-only (`frozen/HEAD-<sha>.tar` — compliant with the no-extraction
  brief); g3d r77-baseline `frozen/` contains an EXTRACTED tree (LOG.md,
  corpus/, …). Data point recorded here; the compliance verdict belongs to
  xsentinel (its brief explicitly covers baseline archive-only behavior).
- **Commit identities.** Consistent current state: report-last = `ci
  <ci@local>` in all three lanes; work commits = lane identity
  `<lane>-shokunin <short>@shokunin.local` (audio `<audio@…>`, g2d `<g2d@…>`,
  g3d `<g3d@…>`); older history used `<lane>-shokunin@local` — all three
  migrated email convention mid-history (w7-F3 territory). Residual: g3d's
  hygiene commit `8a67f71` landed under `ci` while audio `f4621f9` / g2d
  `3a53258` hygiene used lane identity.
- **Receipt layout.** audio shared `corpus/live/runs/<stamp>-<mode-suffix>/
  measurements.json` + per-seat `ledger-rNN.tsv` + `compare_receipts.py`;
  g2d per-seat `corpus/live/rNN-<seat>/runs/<stamp>/verdicts.json` (+ pretree
  materialization via `git archive HEAD`); g3d per-seat
  `runs/battery/<stamp>/verdicts.json`. One scanner can't serve all three —
  relevant if an x-lane census tool is ever wanted.
- **Flag/row naming.** audio `--probe-transport-<member>-rNN` —
  round-suffixed, newest-first arm blocks, monotonically growing flag set
  (114 flags and counting); g2d `--spawn-<mechanism>`/`--probe-<mechanism>`;
  g3d CASES rows `mut_*`/`mv_*` — mechanism-named, no round. Audio's
  convention makes flag-provenance grep-trivial at the cost of flag growth;
  g2d/g3d provenance lives only in reports.
- **Prior-row-stability mechanism.** Same invariant, three implementations:
  audio `compare_receipts.py` vs committed receipt files; g2d pretree
  materialization + 7-field row diff; g3d "all N prior rows re-ran → 0
  mismatches" inside one battery. All report the same "prior rows
  byte-stable" claim — no drift in the claim, drift in the evidence path.
- **Bounded-spike interpretation.** audio + g2d dispatch one read-only
  `ufo-labrat` subagent; g3d r76-author read the same allowance as a scratch
  probe script run directly. Same budget, different mechanism — worth a line
  in the next wave's briefs if uniformity is wanted.
- **Report headers.** `# R68 author —` / `# Round 67 author report —` /
  `# r76 author —` — cosmetic; LOG.md entry shape is convergent.
- **Consistent across all three (no drift):** report path shape
  `reports/round-N/rN-<seat>.md`; scratch `corpus/live/rN-<seat>/`;
  sha256-pinned receipt files; `git archive HEAD` baseline freeze mandate;
  LEAF + evidence-or-it-didn't-happen binding.

## Evidence index

Scratch `xconnector-scratch/evidence-notes.md` carries the command log. Key
refs: audio `reports/round-67/r67-author.md` (:99-107 receipt shape, :71-80
hold mechanism), `reports/round-68/r68-author.md` (:46-51 sndr row, :77-81
seekable-vs-name split); g2d `reports/round-66/r66-author.md` (:25-70 four
surfaces), `reports/round-67/r67-author.md` (:65-82 divergence table),
`descendant_pipe_probe.gd:129,159`, `run_battery.py:168-207,298`; g3d
`reports/round-76/r76-{author,critic,adjudicator}.md`,
`navagent3d_detour.gd:1841-1873`; wave briefs under
`.ufo/waves/shokunin-train-20261014-w8/tasks/`. Git facts: `git ls-files`,
`git check-ignore -v`, `git log --format` — outputs in scratch.

## Limits

- Wave-8 author landings pending — all `[pending-landing]` items re-resolve
  once reports exist; proposals don't depend on them landing favorably.
- Mechanism readings are report-verbatim + spot file:line checks
  (`_apply_mutation` body, midlineforge constants, .gitignore sources,
  ls-files counts) — no re-execution of any lane's probes (read-only seat).
- No verdicts on sibling seats' in-flight work; the census/baseline
  observations are data for xsentinel + the parent, not audit findings.
