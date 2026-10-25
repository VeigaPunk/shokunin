# xconnector — wave-6 synthesis: convergent gate/preemptor structure across r67(audio) / r66(g2d) / r75(g3d)

Seat: connector (leaf, no dispatch). Declared axis-move (verbatim): *"cross-lane
synthesis for wave 6 — convergent gate/preemptor structure across r66/r65/r74."*
Fleet axes this wave: expansion / quality / discernment.

All evidence read-only (`read`, `grep`, `ls`, `find`, `git log/status`,
`python3` on spec JSON). Sole writes: this report +
`xconnector-scratch/evidence-notes.md`. Sources: the three adjudicated wave-5
reports + their knowledge/lesson entries, the wave-5 xconnector report, the
wave-6 task briefs and swarm-registry, and wave-6 **in-flight** landings
observed on disk (audio r67 author's probe design + critic's measured
transport matrix; g2d r66 baseline/reviewer replays only — no author arms yet;
g3d r75 simplifier's arm-variant prep only). In-flight results are cited as
measured-but-unadjudicated.

Structural note for this wave: **all three wave-6 moves are the wave-5
connector's Arms A/B/C adopted verbatim** (w5 report §1/§3 → swarm-registry
`moves`). The round's declared claim for each lane is therefore a proposal
this seat previously scored as measurable; the arms below are the *next
order* — what the wave-6 results themselves predict, not the adopted moves.

---

## 0. State of the wave-6 moves (as observed)

| lane | move | status observed | headline in-flight result |
|---|---|---|---|
| audio r67 | transport as first-class ledger axis (file/pipe/fd/fifo per member) | author `probe_transports.py` design landed (2×2 {named×seekable} over 10 tracked members + ui.wav); **critic matrix.tsv measured** — 10 members × 5 transports; boundary probes staged | **Detection is transport-invariant on all 10 members; reader verdict forks on 4.** act members decode only on regular/seekable fds (file+devstdin ok; pipe/devstdin-pipe die `can't find Sun/NeXT`; redir `premature EOF` — the ffmpeg bridge is a regular-file-only row); gsrt members exit 2 everywhere but error-string forks (seekable→`premature EOF`, pipe→`invalid format`); `pair_dec_hcom` invariant-ok (the never-seek control, confirmed); **fifo anomaly: `pair_preempt_both` fifo-path-1w → detected `-` + 124 samples exit 0** — the `sox`-assumption raw path on gsrt-shaped bytes every other transport detects (`r67-critic/matrix.tsv:1-51`, `fifo.tsv:5`, `transport_matrix.sh`) |
| g2d r66 | rejection-clause surface map (allowlist preemptor, split evasion, splice fabrication, dead-entry census) | baseline + reviewer battery replays only (`r66-{baseline,reviewer}/runs/…/verdicts.json`); no author arms, no surface-map arms landed yet | nothing measured in-flight beyond the 87-row replay; the move's substrate is host-verified in the committed classifier (`run_battery.py:160-208` below) |
| g3d r75 | server-side map/link mutation under committed path — zombie waypoint | baseline dir + simplifier `chain_{link,pop,motion_*}.txt` consolidation hunks + `cons/navagent3d_detour.gd`; no tracked mutation arms yet | nothing measured in-flight; the r74 critic's `fw_mapedit`/`mapedit_lazy` (lazy invalidation → EMPTY path + `final=(0,0,0)` at next forcing call, `r74-critic.md:97-118`) is the adjudicated prior the move will pin as CASES |

## 1. Which wave-6 results in one lane predict a measurable arm in another — per-lane proposals

Each arm is additive-only, falsification-shaped, and names its predicting
sibling wave-6 result. None collides with the in-flight wave-6 landings.

### Arm A — game-dev-2d: channel-absorption — the split classifier makes the whole allowlist dead on stdout (predicted by audio r67)

- **Predicts from — audio r67's measured transport axis.** The r67 matrix
  shows the *same bytes* producing different verdicts depending on which fd
  carried them, with no receipt field recording the carrier. g2d has the
  identical shape one level up, and wave-6's surface map is drawing the
  clause-level half of it while the **classifier-level half sits committed
  and unmeasured**: `classify_streams` (`run_battery.py:179-208`) requires the
  signature on stdout (`:183`), scans *both* streams for `SCRIPT ERROR:`/
  `Parse Error:` (`:185-188`), and rejects on any unexpected **stderr** line
  (`:200-207`) — but stdout has **no generic `ERROR:` scan at all**. A plain
  `ERROR:` line on stdout is verdict-inert there; the same line on stderr
  rejects. Under `classify_process` (`:160-177`) both reject — the merged
  concat erases the channel. So the allowlist — the r66 preemptor row under
  measurement — is never even *consulted* on the stdout channel: a
  **channel-absorption** strictly stronger than clause-absorption, dead on
  arrival without matching any entry.
- **Claim (falsifiable).** On the r65 errforge family the verdict forks on
  `{fd × classifier}`: a post-death forged `ERROR:` emitted on **stdout** is
  absorbed by `classify_streams` (record PASS) while the identical line on
  **stderr** rejects — and both reject under `classify_process`. Four cells,
  three rejects, one absorb; the absorb cell is decided by *which pipe* the
  descendant inherited, not by bytes — the audio-r67 fork shape on g2d's
  substrate. This also answers, with measurement, the r65 lesson's retained
  UNKNOWN ("the error scan there is per-stream; untested", lesson
  `r65-forged-rejection-dual.md:186-188`).
- **Discriminating measurement.** Extend the errforge meta with per-fd
  emission: `--spawn-errforge-stream-{out,err}` — the ppid-gated descendant
  echoes the byte-identical marker post-death on stdout-only vs stderr-only
  (the fixture's `>&2` redirect pattern already exists — r65 `split_errforge_run`
  stream arms). Each bounded-Popen record is scored through *both* classifiers
  on the same captured bytes. Discriminations:
  `streams_absorbs_stdout_forge`, `streams_rejects_stderr_forge`,
  `merged_rejects_both_fds`, `allowlist_not_consulted_on_stdout` (a stdout
  forge matching *no* allowlist entry still passes streams — absorption
  without allowance), plus the genuine `push_error` control per fd.
  Falsification path: if `classify_streams` rejects the stdout forge (a scan
  exists that `:179-208` doesn't show), or stderr-forge absorbs, the
  channel model is wrong — record the actual cells.
- **Axes:** g2d depth (the rejection clause's preemptor map gains the row
  above the allowlist — *classifier selection itself* is a preemptor whose
  reachability is fd-topology; the surface map is incomplete without it);
  coverage +2-3 meta arms; prior 87 rows + 29 discriminations stable.
- **Risks:** (i) `classify_streams` is probe-scoped (used only in the
  stream-attribution probe `:1719`; CASES verdicts route through
  `classify_process`/`classify_audio_process` `:446`) — the arm documents a
  *probe-classifier divergence*, a surface-map fact, and must not be scored
  as a CASES-row vulnerability; (ii) the absorption direction is near-certain
  from the code — the measured value is the full 2×2 cell matrix and the
  allowlist-non-consultation pin, not the direction.

### Arm B — game-dev-3d: the latched zombie — does `finished` gate the map-mutation invalidation row (predicted by g2d r66 + audio r67)

- **Predicts from — g2d r66's dead-entry census and audio r67's
  transport-gated row reachability.** The r66 census asks which clause rows
  no reachable input can trip; the r67 matrix shows row *sets* themselves
  fork on transport state (ext rows exist only on named transports — §2).
  g3d holds the same composition open between two adjudicated facts that
  wave-6 is about to sharpen: (i) the `finished` latch early-returns the
  whole update — pop loop AND pmd re-query both freeze (r74 lesson `:32`);
  (ii) map edits lazily invalidate the stored path — next forcing call
  yields EMPTY + `final=(0,0,0)` (r74 critic `fw_mapedit`/`mapedit_lazy`
  `:97-118`, measured-but-not-CASES-pinned). Wave-6 declares the
  link-mutation half. **The composition — mutation delivered while latched —
  is unmeasured in both directions.**
- **Claim (three-way falsifiable fork; every outcome lands a pair).** With
  `finished` latched, a server-side link/region/layers mutation leaves the
  pure-reader `path` snapshot byte-equal to the pre-mutation array (the
  freeze conjunct holds on *reads*), and then exactly one of: **(a) queued**
  — the first forcing call after unlatch (`target_position` re-assignment)
  re-materializes a mutation-aware path: invalidation was latched, not lost;
  **(b) pushed** — a forcing call *while still latched* already shows a
  changed array: mutation reaches the committed path under the freeze —
  falsifies the whole-update-latch claim for this field; **(c) dropped** —
  the post-unlatch re-query re-materializes the **dead hop**: the
  invalidation row is state-gated dead under the latch — a resurrected
  zombie, strictly worse than r75's plain zombie. (b) is the falsifier of an
  adjudicated claim; (c) is the g2d-dead-row shape inside g3d's update
  cascade.
- **Discriminating measurement.** `steps` presets `mv_latchmut_{link,region,
  layers}` riding the author's prescribed `{mutate:{...}}` step kind (r75
  author brief): settle → forcing call commits the link-inclusive path →
  scripted walk to `finished` (latch) → `mutate` → pure-read tuple
  (`path`/`idx`/flags — must equal pre-mutation: the freeze conjunct) →
  forcing read (array moves here ⇒ push-model) → same-value `set_target`
  unlatch → forcing read (mutation-aware path ⇒ queued; pre-mutation
  geometry incl. dead hop ⇒ dropped) → a 30-frame no-forcing wait sub-arm
  (anything moves without a forcing call ⇒ laziness itself falsified).
  Companion `link_get_enabled` read-back pins that the mutation landed.
- **Axes:** g3d depth (the invalidation event's *bind instant* — push vs
  pull vs drop — completes the update cascade's row ordering relative to the
  latch row); coverage +3-4 presets; prior 145 rows + 4 probes + Node 31/31
  stable (additive presets only).
- **Risks:** (i) depends on the r75 author's `{mutate}` mechanism landing —
  line positions re-verify post-integration; (ii) if r75 shows link mutation
  is inert entirely (no invalidation even unlatched), the arm reduces to
  "latch preserves the zombie across unlatch" — weaker but still
  discriminating; (iii) the no-force wait arm may expose tick-side work the
  lazy model excludes — that *is* the falsifier design, not a defect.

### Arm C — audio: the fallback cascade is transport-gated, and detection's bind-instant may fork on live-pipe delivery (predicted by g2d r66 + g3d r75)

- **Predicts from — g2d r66's dead-entry census + the r75 mutation-under-
  commit question.** The r66 census formalizes "rows no reachable input can
  trip"; the r75 question is "does a committed artifact observe post-commit
  mutation". Both land on audio's detection layer, where wave-6 is mapping
  transport but only inside the CHECK table. **Below the table sits a second
  cascade whose rows are transport-gated, not byte-gated** (`formats.c:911-931`,
  r64-reviewer verified copy): on autodetect NULL → `io_type==lsx_io_pipe`
  forces `filetype="sox"` (raw assumption, `:921-923`); else
  `lsx_find_file_extension(path)` routes by name (`:925-930`); `-t` overrides
  above all. And *inside* the table, rows for headerless formats are
  declared extension-dependent (`:169` aptx, `:181` dfpwm comments).
- **Claim (i), falsifiable.** The row *set* itself is a function of
  transport: identical undetectable bytes route `sox`-raw on pipe, the
  ext-handler on a named sibling, `can't determine type` with no usable
  extension — and a **fifo named `x.wav` still hits the pipe-assumption**,
  because the `io_type` check precedes the ext lookup: the extension row is
  *dead-by-transport* even when a filename exists — the g2d dead-entry shape
  with a state (not fixture) gate. Discriminating: one magic-free 600-B blob
  × {`file.bin`, `file.wav`, `pipe`, fifo `x.wav`, fifo no-ext, `-t wav` on
  pipe} — record routed handler + exit + samples. Falsifier: fifo `x.wav`
  opening the wav reader shows ext beats `io_type` — record the actual
  order.
- **Claim (ii), falsifiable — the detection bind-instant.** r67-critic's
  `fifo-path-1w` leg on `pair_preempt_both` measured `detected=-` + 124
  samples exit 0 (`fifo.tsv:5`) — the `sox`-assumption raw path on bytes
  that detect `gsrt` on every other transport (`matrix.tsv:7-11`).
  Consistent explanation: on a live fifo the autodetect read bound before
  the magic was delivered — detection's 257-B window is a **delivery-
  boundary artifact**, the newline-split-evasion analog inside the byte
  domain (g2d r66: a conjunct split across the scan's unit boundary evades
  the row). Claim: a fifo writer delivering <25 B, sleeping, then the rest
  can evade the gsrt row and force `sox`-assume — write-chunking forks
  *detection*, not just decode. Discriminating: controlled fifo writer
  {single write} vs {write 20 B → sleep {10,100,500} ms → write remainder}
  on `pair_preempt_gsrt`-shaped bytes, N≈20 reps each; detection-miss rate
  vs delay lands the bind model — first-read/short-fill (misses) vs
  blocking-fill-to-EOF (never misses ⇒ claim falsified; the fifo anomaly
  then needs its own cause pinned, e.g. open-order race).
- **Axes:** audio depth (the detection layer's row table extended below the
  CHECK rows — fallback cascade + bind instant — the two things r66's
  preemptor map provably does *not* cover); coverage +~10 legs; additive
  member + scratch-driven transports; 102-command ledger stable.
- **Risks:** (i) the anomaly may be a scheduling flake with a different
  cause — the delayed-writer arm exists to discriminate causes, and a clean
  blocking-fill result falsifies (ii) honestly while (i) stands on the
  source order alone; (ii) chunk-forking is timing-probabilistic — the arm
  must report a distribution, not a boolean (a new receipt shape for this
  lane); (iii) `io_type` classification of fifo-by-path is itself part of
  what's measured — the claim names its own falsifier.

## 2. Convergence audit — the preemptor-row formalism is real as a table shape, divergent as a mechanism

**Verdict: yes for a fleet convention, bounded to the row-table declaration —
and the three lanes' rows are NOT the same mechanism.** The brief's chain
(audio CHECK rows ≺ g2d allowlist entries ≺ g3d gate conjuncts) is an
analogy ladder, not an order relation; what survives audit is a shared
*structure* plus three honest divergences.

The shared structure, now host-verified in all three lanes:

| facet | audio CHECK row (`formats.c:71-72`) | g2d allowlist entry (`run_battery.py:162-175`) | g3d update conjunct (r74 lesson) |
|---|---|---|---|
| row shape | conjunction of atomic predicates: `len ≥ p1+l1 ∧ memcmp@p1 ∧ memcmp@p2` | conjunction of atomic predicates: exact-strip ∨ (prefix `endswith(",")` ∧ `count==1`) ∨ 4-conjunct chain-incomplete | conjunction of atomic predicates: `euclid(agent,path[idx]) < pmd` strict; `reached`/`finished` latch flags |
| order | source-table position, first match returns | per-line consult inside the error scan, before the line counts | temporal evaluation order inside one forcing call: latch ≺ dirty/target ≺ pmd ≺ sequential pop ≺ flags |
| dead rows | **geometric**: wve on RIFF (byte-0 exclusion — provable); all non-offset-0 rows dead on RIFF family | **empirical**: `expected_errors` entries no fixture emits — census in-flight this round | **state-gated**: pmd/pop rows dead under `finished` latch — dynamic, not geometric; pure readers are dead *getters* for liveness |
| transport/state-gated reachability | **new this wave**: ext rows + ext fallback exist only on named transports; pipe collapses to the `sox`-assume row (`:921-930`) | allowlist reachability itself fd-gated under `classify_streams` (Arm A — dead on stdout) | invalidation rows reach a latched agent only via the Arm-B channel (queued/push/drop — open) |
| effect | **route**: picks a winner (handler) | **absorb**: suppresses a veto — an anti-row, can never win anything | **gate**: decides whether update work happens at all |

A convention worth declaring: **every tracked gate map ships a row table**
— per row: `{id, order, conjuncts, effect ∈ {route, absorb, gate},
reachability ∈ {geometric, empirical-census, state-gated, transport-gated},
deadness-proof ref}`. All three lanes independently spent rounds discovering
dead rows (wve-on-RIFF in r66; the in-flight `expected_errors` census;
latch-gated conjuncts in r74): the convention turns the *next* dead-row
question into a documentation check instead of a discovery round. It
composes with the w5 `{bind, via, attr}` field convention — rows vs fields,
orthogonal surfaces, same ledger.

**Contradictions, stated not smoothed:**

1. **Effect classes diverge fundamentally.** Audio rows *route* (first match
   wins a handler); g2d allowlist entries can only *suppress* — they are
   anti-rows that preempt a veto, i.e. second-order preemptors; g3d conjuncts
   *gate evaluation*. Calling all three "preemptor rows" is precise only at
   the level "a row consulted before the clause's default action that can
   cancel or redirect it" — anything stronger overstates the analogy.
2. **Deadness has three proof classes.** Geometric (audio — byte-exclusion,
   provable from the predicate alone), empirical (g2d — a census over
   observed outputs, permanently falsifiable), state-gated (g3d — deadness
   is a function of runtime state; a dead row can resurrect). A fleet
   convention must carry the proof class, not just a dead/alive flag.
3. **Order semantics differ.** Audio order is a static table position; g2d's
   entries are consulted per-line with intra-entry conjuncts ordered but no
   meaningful inter-entry order; g3d's order is temporal and state-fed back
   (the latch *changes* the row set mid-flight). There is no shared "≺"
   across lanes — the brief's ordering is analog, not mechanism.
4. **Transport/state can kill a whole row set, not just satisfy it.** The
   wave-6 additions to the formalism: pipe transport deletes audio's ext
   rows and substitutes the `sox`-assume row; the `finished` latch deletes
   g3d's invalidation/pop rows; `classify_streams` deletes g2d's entire
   stdout error scan. Deadness is a property of {row × carrier-state}, not
   of the row — a row table that omits the carrier column will mislabel.

## 3. The one bounded move (seat-card proposal)

**Land Arm B — the g3d latched-zombie pair.** It is the only arm whose
outcome is a genuine three-way fork (queued / pushed / dropped) with an
adjudicated claim on the line: outcome (b) falsifies r74's whole-update
latch, outcome (c) lands the g2d dead-row shape inside g3d's own cascade —
the wave's convergence made measurable rather than asserted. It composes
both siblings' wave-6 results at once (dead-entry census + transport-gated
reachability) and is the direct second half of the declared zombie move the
author is already building the `{mutate}` step kind for. Improves g3d depth
(invalidation bind-instant + row ordering vs the latch) and coverage (+3-4
presets); no axis harmed: additive presets, 145 rows stable.
Fleet-level companion: the §2 row-table convention — a per-gate-map
declaration of `{order, conjuncts, effect, reachability, deadness-proof}`,
scoped to maps already under measurement (no retrofit debt), alongside the
w5 `{bind, via, attr}` field convention.

## 4. Highest-value unexplored boundary after wave 6 — one sentence per lane

- **audio:** the hint/override layer *above* the CHECK table — `-t` forced
  type, the in-table extension-dependent rows (aptx/dfpwm `formats.c:169-181`),
  and the transport-gated post-table fallback — is the only place routing is
  decided by name and carrier rather than bytes, which r67 just proved is a
  live fork axis and which no preemptor-map work has touched.
- **game-dev-2d:** the interleave model — whether `communicate()`'s cross-fd
  drain order is schedulable decides whether splice-fabrication and split-
  evasion are deterministic verdicts or probability distributions, i.e.
  whether the surface map's rows have transport-dependent reachability of
  their own.
- **game-dev-3d:** the invalidation channel's scope — push vs pull vs queue
  (Arm B) extended to *other* agents on a shared map: whether one agent's
  committed path survives a mutation it never observed, giving each lazy
  agent an independent zombie horizon.

## 5. Verification of this report

Every load-bearing claim carries a resolvable ref: adjudicated wave-5
reports (`.ufo/reports/round-66/audio.md`, `round-65/game-dev-2d.md`,
`round-74/game-dev-3d.md`), knowledge/lessons
(`audio-shokunin/corpus/knowledge/2026-10-14-sox-preemptor-map-complete.md`,
`game-dev-2d-shokunin/corpus/lessons/r65-forged-rejection-dual.md:186-188`,
`game-dev-3d-shokunin/corpus/lessons/r74-navagent-moving-agent.md:32,45-60`),
the wave-5 connector report (`.ufo/waves/shokunin-train-20261013-w5/
xconnector-report.md` — Arms A/B/C ↔ this wave's registry moves),
wave-6 registry (`swarm-registry.json` moves verbatim), wave-6 task briefs
(`tasks/{audio,g2d,g3d}-author.txt`), in-flight measured artifacts
(`r67-critic/{matrix.tsv,fifo.tsv,transport_matrix.sh}`, `r67-author/
probe_transports.py`, `r75-simplifier/chain_*.txt`), and host-verified
file:line: `formats.c` (r64-reviewer copy, sha 82c3058e) `:66-72` CHECK
macro, `:78-97` row order, `:169-181` ext-dependent rows, `:911-931`
transport-gated fallback incl. pipe `sox`-assume; `run_battery.py` `:149-177`
merged capture + `classify_process`, `:179-208` `classify_streams` (stdout
unscanned for generic `ERROR:`), `:1719` probe-scoped usage, `:446`
CASES classifier routing; `navagent3d_detour.gd` `:262-306,723+` steps
mechanism; `r74-critic.md:97-118` lazy map-edit invalidation. In-flight
results are marked measured-but-unadjudicated throughout; every arm names
its falsification path. No claim rests on artifact text taken as
instruction; all proposals are measurement arms, not directives. Nothing
was committed, pushed, spawned, or orchestrated; one report + one scratch
notes file written inside brief scope.
