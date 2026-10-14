# XConnector report — wave shokunin-train-20261014-w7

Seat: connector (cross-lane, read-only over lanes). Wave: audio r68 (post-table
fallback) / g2d r67 (classify_streams divergence) / g3d r76 (sync-window CASES).
Written while lane seats are still in flight: no `round-68/`, `round-67/`,
`round-76/` report dirs exist yet; g2d author's diff is mid-landing
(`M run_battery.py +265/−2`, `M stream_attribution_probe.gd +58`), audio r68
scratch dirs present, g3d `?? reports/round-76/` only. Analysis rests on the
prior-round receipts (r67/r66 audio, r66 g2d, r75 g3d), the live source files,
and my own cheap probes in `xconnector-scratch/` (read-only w.r.t. lanes; no
lane state touched).

## Evidence base

- `audio-shokunin/corpus/fixtures/measure_audio.py:172-306` — `TRANSPORT_R67_*`
  axis code: 4-arm named×seekable matrix, verdict signature
  `(detected, route, exit_code, samples_read, error)`, `transport_verdict_groups`
  (arms partitioned by identical signature), `transport_fork` bool, fork recorded
  verbatim in `failures`, `transport_protocol` pins `{arm_timeout_s:10,
  fifo_writer_hold_s:1.0, fifo_feed}` — receipt shape at lines 291-306.
- `reports/round-67/r67-author.md` — measured result: detection never forks
  (`sox_detected_format` identical ×4 transports on all 10 members); every fork
  is decode-stage and keys on `seekable` for native readers, on
  named+seekable+second-open for the act/ffmpeg bridge.
- `reports/round-66/r66-boundary.md` — CHECK-table preemptor map, rows 78-97
  fully probed (`voc(78)→smp(79)→wve(80)→gsrt(81)→amr-wb(82)→prc(83)→sph(84)→
  amr-nb(85)→txw(86)→sndt(87)→vorbis(88)→opus(89)→hcom(90)→act(93,ffmpeg)→
  wav(95/96/97)`); txw `LM8953`@0-5 and smp `SOUND SAMPLE DATA`@0-16 both
  hard-refuse pipes (`input must be a file, not a pipe`); wve decodes on pipe.
- `game-dev-2d-shokunin/corpus/fixtures/run_battery.py:160-208` —
  `classify_process` (merged `stdout+stderr`: signature anywhere; per-line
  `ERROR:` scan; whole-blob `SCRIPT ERROR:`/`Parse Error:`; 3-shape allowlist
  incl. the structured `chain incomplete` conjuncts) vs `classify_streams`
  (signature must be on **stdout**; blob clauses checked **per stream**; stderr
  scan = EVERY nonempty line must be allowlisted — strictly stronger than an
  ERROR:-scan; `line_allowed` implements only exact + `,`-prefix shapes, no
  structured shape).
- `run_battery.py` in-flight r67 diff (uncommitted, read 2026-10-14):
  `dual_classify` runs BOTH classifiers over the SAME captured streams; 7 new
  probe flags (`--stdout-error`, `--stderr-error`, `--stderr-structured`,
  `--sig-on-stderr`, `--seam-error`, `--seam-script`, `--seam-sig`) +
  `divergence_table` + `sd_discriminations` (expected-set partition check) +
  `reject_arm_diverges_non_error_stderr` (the stderr-strictness divergence via
  the pre-existing `STREAM_STDERR:` arm).
- `game-dev-3d-shokunin/corpus/fixtures/navagent3d_detour.gd:1552-1662` —
  step order `set_target → tp → mutate → wait:N×physics_frame → peek →
  _read_state` (wait=0 legal: `range(0)` skips awaits → same-tick read);
  `_apply_mutation` fixed order delete→recreate→transform/enabled/layers→link→
  agent; `_final_srv_state` folds all mutate dicts into expected server state
  and reads it back — a no-op setter fails the arm.
- `reports/round-75/r75-{author,critic,scout}.md` — the window is TWO windows:
  setter→server-sync (mutation invisible to everything same-turn — server
  getters `link_get_enabled`/`link_get_iteration_id` themselves read stale;
  flips at the first `physics_frame`) and sync→forcing-call (unbounded; pure
  readers stale indefinitely). Critic pinned "one physics frame at minimum";
  scout measured `map_set_active(false)` → NO iteration bump at all — a
  permanent-stale regime, not a window.
- My own probes (SoX_ng 14.8.0.1, `xconnector-scratch/probe-transcript.txt`,
  all exit 2, verbatim FAIL strings):

  | transport | input | last FAIL line |
  |---|---|---|
  | file | `nomatch.bin` (43 B, no magic) | `no handler for file extension 'bin'` |
  | file | `nomatch.wav` (same bytes, renamed) | `can't open input file 'nomatch.wav': RIFF header not found` |
  | fifo_path | `nfifo2.wav` (same bytes) | `can't open input file 'nfifo2.wav': RIFF header not found` |
  | stdin_pipe | `cat nomatch.wav | sox -V6 -` | `can't determine type of '-'` |
  | redirected_fd | `sox -V6 - < nomatch.wav` | `can't determine type of '-'` |

## Axis 1 — pattern transfer

**T1 (headline). The decisive transport bit flips per stage — measured before
the r68 author lands.** r67 established: detection = transport-invariant;
decode-stage forks key on `seekable`. My post-table probes measure a THIRD
stage with the OPPOSITE bit decisive: on a no-match member the fallback is
**extension-keyed**, so the verdict partition is `{file, fifo_path}` (named →
extension → handler; `.wav`→wav-reader `RIFF header not found`, `.bin`→
`no handler for file extension`) vs `{stdin_pipe, redirected_fd}` (named `-` →
`can't determine type of '-'`). `redirected_fd` is seekable yet lands in the
pipe group — seekability buys nothing without a name. **Predicted
falsification of the r68 declared claim's mechanism**: the fork is real, but
its axis is `named`, not `seekable` — the exact *opposite* grouping from the
decode-stage forks. The r67 receipt already carries both bits per arm
(`named`/`seekable`, measure_audio.py:271-273), so the attribution is
self-evident in-receipt once the member lands. Caveat: the member's *suffix*
is a live sub-axis — a `.txw`-suffixed no-match member would route fifo to the
pipe-refusing txw reader (`input must be a file, not a pipe`) and could split
the named group further. Cleaner mechanism statement for the ledger: autodetect
consumes two different resources — prefetch *bytes* (gone on pipes at
detection) and a *name* (absent on `-` at fallback).

**T2. `transport_verdict_groups` is the shared receipt idiom — two lanes
already re-invented it.** Same-subject × axis-ladder → signature-partition →
derive fork/bound as the partition boundary:
- audio r67: 10 members × 4 transports → groups + `transport_fork`.
- g2d r67 (in flight): same captured streams × 2 classifiers × allowlist
  variants → `divergence_table` + expected-set discrimination — same math,
  minus the per-group *signature tuple*. One additive delta worth landing (now
  or r68): a `divergent_clause` signature per row
  (`{exit, signature, error_scan, blob, allowlist_shape}` → which clause
  diverged) so the g2d divergence set is diffable across rounds the way
  audio's groups make r68-vs-r67 fork sets mechanically comparable.
- g3d r76: wait-ladder {0,1,2,...} × full tuple is the same shape — emitting
  the **groups** (waits partitioned by identical post-mutation tuple) instead
  of only per-arm pass/fail derives the window bound as a partition boundary;
  a wait≥1 arm landing in the pre-sync group then falsifies the bound
  mechanically, not just the one arm's pin.

**T3. Race-window constants → measured bounds; one lane per instance.**
- audio: `TRANSPORT_R67_FIFO_WRITER_HOLD_S = 1.0` is a *chosen* constant pinned
  in `transport_protocol`; the minimum deterministic linger is unmeasured
  (r67 observed bare-writer race 5/5 + one >10 s block).
- g2d: midlineforge's 80 ms write into the 200 ms signature gap is a point
  sample (descendant_pipe_probe.gd:82-88, 157-168) — the fabrication window's
  bounds are unmeasured; >120 ms scheduler stall already declared as the
  falsification surface.
- g3d: the r76 move ladders `wait` (0/1/2) — the only lane currently
  converting a race constant into a measured bound. The transfer is
  bidirectional: audio's `transport_protocol` shows how to pin the protocol
  inside the receipt (g3d could record `{wait_ladder, order_of_ops}` per
  CASES row the same way), and g3d's ladder shape is the next-order move for
  the other two lanes' constants (see Axis 2).

**T4. Readback-gate (`_final_srv_state`) → audio + g2d.** g3d arms assert their
own precondition (a no-op setter fails the arm; navagent3d_detour.gd:344-358,
1618-1662). The audio r68 analogs: pin `sox_detected_format is None` on all
four legs of the no-match member (precondition = true table miss — a member
that secretly matches a row would "fork" on the wrong mechanism) and
`sox_detected_format == 'txw'|'smp'` on the refusal member (covers the critic's
"shadowed by earlier CHECK row" attack mechanically). The g2d r67 analog:
`dual_classify` feeds identical bytes by construction but the record carries
no same-input proof — recording `sha256(raw_stdout)`/`sha256(raw_stderr)` per
dual verdict makes same-input a gated fact rather than a convention.

**T5. Dead-clause census → dead-CHECK-row census (audio, coverage axis).**
g2d r66 censused allowlist entries (0 dead) and blob clauses
(`SCRIPT ERROR:`/`Parse Error:` dead in-run) as a first-class receipt field.
Audio's analog is unprobed: the CHECK table runs to ~row 97 (r66-boundary map)
while the tracked member family exercises only {wav, act, gsrt, hcom} —
+txw/smp this wave. A scratch-only census (grep `sox_detected_format` across
committed receipts vs the row inventory) measures which table rows have EVER
been first-match — the coverage frontier of the autodetect axis, and the
natural companion to r68's post-table move (the no-match member is the input
for which the WHOLE table is dead).

**T6. Timing precondition, both directions (brief's named pair).**
g3d's same-turn window and g2d's capture-before-pipe-EOF are the same shape:
a write/mutation lands before vs after a consume/sync boundary. Two
corollaries the lanes' own briefs half-see:
- g2d boundary item 5 ("does `communicate()` drain-order change which seam
  fabricates") is **predicted null on content**: `subprocess.run(
  capture_output=True)` captures per-fd and the merged text is a fixed
  post-hoc `stdout + stderr` concat — drain scheduling cannot alter per-stream
  bytes; it only interacts with TIMEOUT truncation. Cheap falsifier: rerun a
  seam arm under reversed read order; predicted byte-identical.
- The symmetric g3d structure: `_apply_mutation`'s fixed order
  (delete→recreate→transform→link→agent) is the analog of g2d's fixed concat
  order — a composed same-tick mutation (`region_delete`+`region_recreate`)
  is g3d's "seam": an emergent state neither setter alone produces, enabled by
  pinned ordering. The boundary's "two setters same tick" probe is this
  question; a bypass probe that hand-orders the same setters differently
  (transform-then-delete vs delete-then-transform) tests whether apply-order
  changes the synced state — same falsification class as the seam-order test.

**T7. Strictness asymmetry is now pinned on both sides — but note the surviving
cell.** The in-flight g2d diff covers the non-ERROR stderr strictness via
`reject_arm_diverges_non_error_stderr` (streams rejects / merged accepts on a
plain `STREAM_STDERR:` line) and seam-immunity both directions. The one cell
with no arm: a *benign* stderr line (`printerr("note: ...")`, no `ERROR:`, no
signature bytes) — same clause as the signature-on-stderr case, so
mechanism-covered, but it is the divergence most likely to matter in real
Godot output (engine warnings/progress on stderr). One `printerr` flag if a
future round wants the cell explicit.

## Axis 2 — next-order frontier proposals (concrete, falsifiable, cheap)

**audio (r69+):**
1. Extension-suffix sweep on the r68 no-match member — same bytes renamed
   `.wav` / `.bin` / `.txw` through the 4 transports: predicts the named arm
   splits {wav-reader-fail | no-handler | txw-reader} → a 3–4-group partition
   pinning the extension sub-axis. Cost: scratch probe only, ~12 sox runs.
2. Ledger input-digest pinning — `run_ledger.py` is per-seat scratch (zero
   tracked cost): record sha256+mtime of each `corpus/artifacts/` input per
   row. Converts the r67-observed mid-write flakes (2 UNPARSED rows from
   sibling rebuilds) into detected drift vs real verdict change. Transfers
   g2d/g3d's isolation convention as *detection* where isolation isn't
   available (artifacts are tracked AND regenerated by every seat).
3. `fifo_writer_hold_s` ladder {0, 0.5, 1.0, 2.0} → minimum deterministic
   linger bound; also decides whether the 1.0 s is slack or load-bearing.
4. Dead-CHECK-row census (T5) — coverage bookkeeping over existing receipts.

**g2d (r68+):**
1. Descendant-write offset ladder on midlineforge ({0,40,80,120,160,240} ms
   vs the 200 ms gap) → measured fabrication-window bound — the exact r76
   move shape applied to the lane's own timing constant.
2. `divergent_clause` signature column in `divergence_table` (T2) — additive
   receipt field; makes the divergence set mechanically diffable next round.
3. Same-input gate: sha256 of fed streams inside each `dual_classify` record
   (T4) — kills the "same captured bytes" objection class permanently.
4. (Marginal) benign-stderr arm (T7) — same clause as existing cells; only if
   a round wants the cell explicit.

**g3d (r77+, or strengthen r76 receipt):**
1. Emit wait-ladder verdict-groups (T2) — derive the frame bound as partition
   boundary; declared claim says "stable measured constant" and this makes
   constant-vs-distribution a receipt-level question, not a per-arm pin.
2. `map_set_active(false)` expected value is **permanent-stale, not a window
   bound** — scout r75 measured no iteration bump at all; the arm should pin
   "stale served at ALL waits" or it will read a correct inert result as a
   failed window measurement.
3. Mutation apply-order bypass probe (T6) — hand-ordered setters vs
   `_apply_mutation`'s fixed order; tests whether the ORDER is load-bearing.

## Axis 3 — drift bookkeeping between lanes

- **Report paths** uniform: `reports/round-<N>/r<N>-<seat>.md` inside each lane
  repo; x-seats write to the wave dir (`xconnector-report.md`,
  `xsentinel-report.md`) — outside all three repos, so no lane LOG/history will
  carry this report unless a scribe imports it. Deliberate asymmetry; noted.
- **Scratch** uniform: `corpus/live/r<N>-<seat>/`; x-seats
  `xconnector-scratch/`, `xsentinel-scratch/` at wave root.
- **Tracked-scratch norms differ three ways:** audio tracks selected live
  evidence (15,291 files under `corpus/live` committed; `corpus/.gitignore`
  covers only `live/*/tree|frozen|*tree*`, extended w7 after the 42 MB
  `head-tree/` miss); g2d tracks more (37,751 files) with the same ignore
  family + `edge-verdicts.json`; g3d ignores `live/` WHOLESALE
  (`git ls-files corpus/live` = 0) plus `__pycache__/`/`*.pyc`. Same path,
  three policies — a cross-lane reader must not assume a `corpus/live/` receipt
  is committed in g3d.
- **`__pycache__` split:** audio TRACKS
  `corpus/fixtures/__pycache__/measure_audio.cpython-314.pyc` (drifts every
  round, disclosed "parent decides" since r62); g2d leaves it untracked
  (`?? corpus/fixtures/__pycache__/`); g3d ignores `*.pyc` globally.
  Recommend audio follow the g3d pattern next hygiene pass (precedent:
  f4621f9).
- **Commit identities drift:** two emails per lane repo with no observable
  rule — audio `{audio-shokunin@local, audio@shokunin.local}` (r67 work used
  the first, r67 report-last the second; r66 report-last the first), g2d
  `{game-dev-2d-shokunin@local, g2d@shokunin.local}`, g3d likewise. Any
  author-based history grep splits each lane's log. Low harm, real drift.
- **LOG declaration convention split:** audio carries a separate PRE-declared
  round entry since r63 ("Round N declared … claim and wave spec"); g2d/g3d
  record the claim retroactively inside the integration entry ("Declared
  (author dispatch brief; retroactive record)"). Reviewer seats auditing
  declared-vs-measured should know which shape their lane uses.
- **Converged, no drift:** `git archive HEAD` freeze + no-recursive-embedding
  norm identical in all 18 lane briefs; "ABSOLUTE `--runs`" propagated into
  this wave's g2d AND g3d baseline/reviewer briefs (the r75 trap → docstring
  `cefc821` → brief convention); report-last/verifier/adjudicator ordering
  identical across lanes.
- **Shared-state exposure asymmetry:** audio's `corpus/artifacts/` is tracked
  AND regenerated by `build_artifacts.py` under every seat → mid-write flake
  exposure (r67: 2 UNPARSED rows, disclosed, mtime-evidenced). g2d/g3d isolate
  per-seat via `--path`/scratch. No convention breach; remedy is frontier
  proposal audio#2.

## Proposed move (bounded)

The wave's one non-obvious move is the **stage-aware verdict-partition
synthesis**: (a) hand the audio lane the measured prediction that r68's
post-table fork partitions on `named` (+extension), not `seekable` — the
opposite axis from r67's decode forks — so the author lands the arms expecting
the correct partition and the report can state the three-stage axis map
(detection: neither bit; fallback: named; decode: seekable); (b) promote the
`transport_verdict_groups` idiom into g3d's r76 window arms as
wait-partition-derived bounds, and into g2d's landed divergence table as a
`divergent_clause` signature column. Improves **discernment** (corrected
mechanism claim for audio; bound-as-derivation for g3d) and **expansion**
(the receipt idiom generalizes to any axis-ladder) at zero cost to
**quality** — all additions are additive receipt fields or scratch probes;
nothing tracked regresses, no green battery count moves.

## Risks

- My fallback probes ran on MY bytes, not the author's member — the member's
  suffix chooses the named-arm reader; predicted partition assumes `.wav` or
  unknown-extension naming. If the author names it `.txw` the fifo arm routes
  to the pipe-refusing txw reader (3-group partition — still namedness-keyed,
  different signature).
- `redirected_fd` probe used a regular-file fd; SoX may behave differently on
  other seekable fds (`/proc/self/fd` plumbing is the r68 boundary seat's
  territory — my result is the `-`-named lower bound).
- The r67 fifo arm needs the 1.0 s linger only because the ffmpeg bridge
  re-opens by name; post-table fallback to a NATIVE reader (wav) needs no
  linger — but if the extension maps to an ffmpeg-handled type (e.g. a suffix
  routed to act), the fifo arm re-enters the contended-fifo regime. Unprobed
  on this host.
- g3d "stable constant" claim: critic's r75 evidence says ≥1 frame; whether
  the bound is exactly 1 vs a small distribution under load is precisely what
  the r76 ladder measures — my report treats the bound as open.
- Probes used a plain one-shot fifo writer (no linger) — adequate for the
  native-reader fallback measured; not adequate if a named arm ever routes to
  the bridge (same caveat).

## Verification

- Probe transcript + inputs: `xconnector-scratch/probe-transcript.txt`,
  `nomatch.{bin,wav}`, `fifo.out` — commands verbatim above; all four
  transports exit 2 with the quoted FAIL strings, `sox -V6` on SoX_ng
  14.8.0.1, host plazir27.
- Source refs resolvable on this host: `measure_audio.py:177-306`,
  `run_battery.py:160-217, 2199-2514+`, `navagent3d_detour.gd:1552-1662`,
  `descendant_pipe_probe.gd:82-168`; reports `round-67/r67-author.md`,
  `round-66/r66-boundary.md`, `round-66/r66-author.md`,
  `round-75/r75-{author,critic,scout}.md`.
- In-flight g2d diff read via `git diff` on uncommitted worktree state —
  content may shift before landing; the discrimination names quoted exist at
  read time.
- No lane file, tracked content, or shared state modified; only
  `xconnector-report.md` + `xconnector-scratch/` written. No commits, no
  dispatch.
