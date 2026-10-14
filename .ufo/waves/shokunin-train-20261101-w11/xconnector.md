# xconnector — cross-lane synthesis over wave-10 landings + frontier seats

Seat: xconnector, wave `shokunin-train-20261101-w11`. LEAF, read-only across
lanes; own evidence limited to interpreter-level demos (no fixture edits, no
git mutations). Scratch: `xconnector-scratch/evidence-notes.md`.

**Timing caveat (declared):** wave-11 is in flight as this report is written.
Landed: g3d r80 (`faae4e0`, eval-event catalogue folded, 64/64). In flight:
audio r72 (scout/boundary/critic/scribe reports present, author arm
uncommitted at `c079aba`), g2d r71 (critic/simplifier reports present, author
in flight). The love-physics frontier report (`fb-lovephysics.md`) landed
*this session* (receipts `out/run-1..7.txt`, 11:18–11:20Z). In-flight findings
are cited as such — evidence, not landed truth.

## What the round-cache now establishes — the layer model

| layer | mechanism | where landed | edge semantics |
|---|---|---|---|
| spawn (POSIX fd) | descendant inherits/addresses captured fd1 → midline splice | Godot (r68/r69 midlineforge), LOVE `os.execute` + `/proc/pid/fd/1` (r70 critic F1, folded `16d003c`) | window = wall-ms, gap-relative |
| language (stdio) | writer's own buffer withholds bytes until fill/flush/exit | pygame = CPython block-buffer (fa-pygame; edge **corrected to 131072 B on 3.14** by in-flight r71-critic — the "~8KB" figure falsified) | window = **bytes**, not ms |
| engine plumbing | runner's per-tick serve / eval events own commit | Godot navserver {link:2, region:3}f + `map_off` perm; bpy {get, vl.update, dg.update, frame_set, bpy.ops} | window = phase/tick/eval count |
| decoder (content) | sniff → per-decoder accept/refuse tiers | sox CHECK+ext dispatch; ffmpeg content-only; libsndfile post-sniff raw fallback + recognized-refused tier | axis = name / seekability |

The wave-10 correction that matters most for cross-lane prediction: the
fabrication claim was relocalized **engine-general → spawn-general**
(`r70-critic.md:53-62`, adjudicator `ADMIT-with-correction`). The same
relocalization is now due one level down — see arm X1.

## Ranked wave-12 frontier arms

### X1 — "reordering fabrication": fd1-inheritance × stdio-withholding composition (g2d + g3d, shared arm)

**The two landed shared mechanisms compose, and the composition changes the
byte topology.** On a runtimes whose scripting layer block-buffers stdout
(CPython: pygame, bpy `-b -P`), a descendant write into inherited fd1 lands in
the kernel pipe while the parent's earlier `write()` sits in userspace — the
downstream reader sees descendant bytes **before** the parent's earlier bytes.
Same seam as the Godot/LOVE splice; different wound shape: **prefix/reorder
fabrication** instead of midline splice, with the window bounded by
buffer-lifetime (fill ≥131072 B on py3.14 / flush / exit), not wall-ms.

**Demonstrated this seat** on the host interpreter (no fixture needed —
`scratch/evidence-notes.md`):

```
python3  … write("HEAD "); os.system("printf INJECTED"); write(" TAIL\n") | cat -A
        → INJECTEDHEAD  TAIL$      # descendant bytes precede parent head
python3 -u …same…                  → HEAD INJECTED TAIL$   # midline splice
python3 …print("HEAD ",end="",flush=True)…same… → HEAD INJECTED TAIL$   # flush collapses window
```

Control already landed in-repo: LOVE's `io.write` head is on the wire before
the gap ends — the critic's splice cells (`corpus/live/r70-critic/splice_probe/
main.lua:26-31`, `splice_probe_fd1/`) show midline topology, so LuaJIT writes
through per-call while CPython withholds. The language layer picks the
topology; the spawn layer supplies the seam.

**Arm shape** (per Python runtime — pygame via the in-flight r71 fixture,
bpy via `blender -b -P` one-shot): HEAD (unflushed) → spawn `sh -c 'printf
… >&1'` at known offsets → TAIL → exit; cells over {buffered, `-u`,
`flush=True`} × {descendant inside vs after window} × {pure-line vs
>131072 B mid-run crossing write}. Predictions, all falsifiable:
(i) buffered → `INJECT…HEAD…` reorder; (ii) unbuffered/flushed → midline
splice identical to LOVE/Godot; (iii) a descendant write during a
crossing-write flush lands between flushed chunks — hybrid topology;
(iv) `PYTHONUNBUFFERED=1` collapses the window. **Receipt consequence to
pin now:** any future *streaming* parser of ARM lines over a pipe can see
reordered output on Python runtimes — a verdict-integrity hazard class the
post-exit battery parsers cannot observe.

### X2 — "fork axis = re-access channel" (audio; also predicts pw-cat/mpv)

The four measured decoder/consumer stacks now make the mechanism visible:
a transport fork lives exactly where the consumer **re-accesses the input**
after the first stream pass, and the fork axis is the channel that pass uses.

| stack | re-access | fork axis measured |
|---|---|---|
| sox | re-open by name (act→ffmpeg bridge, open #2) + ext dispatch | {named×seekable}; writer-linger band (r70) exists **because** open #2 needs an attached writer |
| ffmpeg/ffprobe | none — `pipe:` single pass, fd0 never `lseek`'d (r71-boundary probe-C, strace) | none — 9/9 members transport-invariant |
| libsndfile `sf_open` | name consulted at open (post-sniff fallback) | {named}/{anonymous} on `.snd` only |
| libsndfile `sf_open_fd` | none | none |
| mpv | lavf refresh-seek (optional pass 2) | {seekable} — **inverted**: EPERM on seekable file, plays on fifo (fb-pipewire:c) |
| pw-cat | single open → playback-paced drain | none (fb-pipewire:b) |

Predictive corollaries, each a cheap cell:
- **Tool-layer inheritance**: pw-cat's decode is libsndfile (`sndfile:` error
  prefix). If pw-cat calls `sf_open(path)`, a **fifo named `*.snd`** carrying
  no-magic bytes opens `RAW|U-Law`; if it virtualizes fd IO, it rejects —
  either answer localizes where the name axis enters the stack. Same cell on
  `sndfile-convert <fifo.snd>`. (fb-pipewire tested `fifo1`/`fifo3` names —
  the discriminating name was never carried on the fifo.)
- **mpv second polarity**: the observed fork is refresh-seek EPERM on a
  seekable *file*. `--start=N` makes the seek mandatory → predicted fork on
  {seekable} with normal polarity (file seeks, fifo refuses or degrades).
  Both polarities on one axis would pin "mpv forks on the seek channel in
  whichever direction the demuxer's seek support allows".
- The name-axis verdict is three-valued across decoders {dispatch (sox) /
  fallback (sndfile) / absent (ffmpeg)} — and per in-flight r72 evidence the
  fallback even **consumes the 12-byte sniff probe** (ULAW reads 500 of 512
  frames; r72-boundary headline). Reframe: no "second decoder has a name
  axis" boolean; record *which channel* each pass touches.

### X3 — "interior writes at the commit boundary" (g2d love.physics ↔ g3d bpy ↔ Godot callsite)

The landed edge vocabulary has two classes — immediate (edge 0) and deferred
(edge ≥1). The frontier receipts reveal a **third class: the in-commit
observer**, and an open question it forces — what happens to a *write issued
inside* the commit boundary.

Measured observers inside a commit: LOVE `setCallbacks` all fire
`in_step=true` inside `world:update` (fb-lovephysics:c) and **the channel
picks the snapshot** — narrowphase BC/preSolve see exactly `y_pre/vy_pre`,
postSolve sees `y_post/vy_post`, and TOI-path BC sees a *third* mid-step
state (post-gravity, pre-impulse: `vy = vy_pre + g·dt`). bpy mirrors the
channel-split one level up: `depsgraph_update_post` does **not** witness
frame-path evals (fa-bpy-evalcat §2; `frame_set` fires `frame_change_*`
only). Godot: `_physics_process` callsite shifts navserver writes +1 tick
but PhysicsServer 0 (fb-physserver).

**Arm (g2d):** inside `preSolve`/`postSolve` attempt `body:setPosition`,
`love.physics.newBody`, fixture/body destroy, nested `world:update`.
Box2D canonically asserts the world is locked mid-step → predicted outcomes
{refused / deferred-to-step-end / fatal}, per class. Whatever the answer, it
pins the third edge class on LOVE.
**Arm (g3d, pairing):** an RNA write inside a `depsgraph_update_post`
handler — re-entrant tag? deferred? error? unprobed in evalcat.
**Shared claim to falsify:** *commit boundaries gate writes issued from
inside them; the gate class is per-subsystem, not per-runtime* — predicted
from the same per-subsystem split already measured as {navserver:queued} vs
{physserver:inline} inside one engine and {RNA:queued} vs {bpy.ops:inline}
inside another.

### X4 — "second tier inside one server" (g3d Godot PhysicsServer completion)

bpy's r80 closure claim (eval-event set enumerable-and-closed,
`violations=0` on 45+ classes at `faae4e0`) has a direct structural
transfer: bpy found **some event classes bind only on the periodic path**
(`keyframe_insert` inert through tagged evals, binds at `frame_set`). The
PhysicsServer lattice is currently flat `{*:0}` — but the frontier seat
explicitly left the step's *own outputs* unprobed: contact-pair generation,
`intersect_shape`/`cast_motion`/`body_test_motion`, area overlap
(fb-physserver caveats). **Prediction transferred from bpy:** queries stay
edge-0 same-turn while generated events (contacts, motion-test results)
bind at the physics tick — a two-tier lattice inside one server, isomorphic
to {RNA-write:1, keyframe:frame_set} inside one object model. Companion arm:
`physics/3d/run_on_separate_thread=true` — predicted to convert mid-step
writes from inline to locked/deferred (the one regime change that could
break the flat `{*:0}`). Jolt engine = second-build control.

### X5 — "statement-stream dead surfaces" census (cross-lane, cheap)

A runtime class is emerging: **no host pump → no notifier surface.** Measured
dead under `-b -P`: msgbus (renamed API subscribes but never fires),
`undo_post`, `bpy.app.timers` (registered, never fired — r79-critic cell).
pygame headless: no spontaneous QUIT, no pump needed; pw-cat `--target 0`:
unlinked stream **hangs forever** — subscription without a link never drains
(fb-pipewire:a). Arm: pin a per-runtime {live / dead-headless / pump-gated}
verdict table over {bpy `--python` interactive vs `-P`, `bpy.app.timers`,
pygame `mixer` endevents + `time.set_timer` under dummy, `love.thread`
channels, pw-cat sink-less}. This is a fixture-portability law: any battery
arm whose witness is a notifier callback is dead weight on statement-stream
runtimes — the evalcat "do NOT pin msgbus/undo_post rows" note generalized.

## Contradictions stated (not smoothed)

- **"Fabrication = spawn-layer on both engines" is true of the seam, not the
  signature.** Godot/LOVE splice *midline* because their writers flush
  through; Python runtimes are demonstrated (this seat) to **reorder**. A
  wave-12 battery that looks only for the r68 line-shape on a Python runtime
  will MISS the fabrication it causes — verdict shape is language-layer
  dependent. Same mechanism, different detection predicate.
- **"Seekable helps" is dead as a law.** sox txw needs seekable; mpv's hcom
  member plays *because* the fifo is non-seekable (file arm: refresh-seek
  EPERM → rc=2). Same axis, opposite polarities, both real. The mechanism
  that survives is re-access-channel (X2), not direction.
- **Edge constants are per-subsystem, not per-runtime.** Godot contains both
  navserver {2,3}f and PhysicsServer {0}; bpy contains RNA {1 eval} and
  bpy.ops {0}. Any wave-12 claim of the form "runtime R has edge E" is
  malformed at birth — the unit is (runtime, subsystem, mutation class).
- **Withholding bound: "~8 KB" is falsified** (in-flight r71-critic F1):
  `io.DEFAULT_BUFFER_SIZE = 131072` on CPython 3.14 (verified this seat:
  `io.DEFAULT_BUFFER_SIZE` → 131072), 8192 B on ≤3.13 — the constant is
  interpreter-version-dependent, and a withheld line releases early on a
  crossing write (255.7 ms measured, not at exit). X1 cells must carry the
  referent `default_buffer_size` per receipt, not a hardcoded edge.
- **libsndfile's name axis is not sox's.** Same {named}/{anonymous}
  partition shape on `.snd`, different mechanism (post-sniff raw-family
  fallback vs ext-gated CHECK row + dispatch), different member coverage
  (r72 in-flight: the "sndfile-only" class is empty on the tracked 9 —
  `.snd`-named is sox∩sndfile; the true sndfile-only exemplar is `.au`,
  outside the corpus). Same verdict, different machine — the receipt must
  name the mechanism or the two columns conflate.
- **Determinism**: love.physics trajectories are byte-identical ×7 runs
  (PHYS-DETERM sha256 stable, `fb-lovephysics.md` (b)) — but only the
  trajectory block; ACC legs are wall-clock by design. Byte-stability claims
  must scope the block.
- **In-flight status asymmetry**: g3d r80 landed; audio r72 and g2d r71
  landings absent at snapshot — all r72/r71 findings above are seat-level
  evidence, pre-adjudication.

## Proposed move (one bounded)

**Dispatch the ranked frontier set as five wave-12 pre-measurement arms, with
X1+X2 as the payload: (X1) pin "reordering fabrication" on both Python
runtimes — predicted from two landed mechanisms, mechanism demonstrated on
the host interpreter this seat; (X2) pin "fork axis = re-access channel" on
the audio consumers — pw-cat/sndfile-convert `*.snd`-fifo inheritance cell +
mpv mandatory-seek cell; (X3) interior-write gating at commit boundaries on
love.physics + bpy handler; (X4) PhysicsServer two-tier completion +
separate-thread arm; (X5) dead-surface census.**

The synthesis claim for the fleet: edge/fork structure is predicted by
*which channel a second access pass uses* (name, seek, buffer, phase,
callback) — not by which runtime hosts it. The frontier corpus needed is
already in place on every arm; nothing here requires new corpus classes.

## Affected axes

- **coverage/expansion ↑**: five concrete, falsifiable, cheap frontier arms;
  each reuses measured machinery (fifo+writer protocol, ctypes sf_open,
  phase-machine probes, in-callback writes).
- **discernment/depth ↑**: converts three per-lane phenomenologies (splice,
  withhold, transport fork) into mechanism-level rules that predict
  unmeasured runtimes — and explicitly retires two wrong generalizations
  (engine-general, seekable-helps).
- **quality/verdict-integrity ↑**: names a live hazard (ARM-line reordering
  on buffered-stdio runtimes for any streaming consumer) and a pin-honesty
  rule (carry `default_buffer_size`, not a hardcoded edge).
- No axis regresses: all arms are additive scratch-level pre-measurements;
  prior-row byte-stability is untouched.

## Risks

- **X1's window may be narrower than billed on bpy**: Blender's `-b -P`
  print path may differ from bare CPython (its own stdout wrapping);
  predicted same, falsifier built-in (the `-u`/flush control cells collapse
  the prediction either way).
- **X2 inheritance cell could be decided by tool code, not library**: if
  pw-cat/sndfile-convert flatten the name axis, the cell still yields the
  structural fact (which layer binds the name) — either polarity is signal.
- **X3's predicted refusal may land as a crash** (Box2D `b2Assert` under a
  debug build vs silent defer under release): the arm must record which —
  a crash cell is still a measured edge class, but it kills the probe early;
  order interior-write cells last.
- **In-flight dependence**: X1's 131072 B edge and X2's `.au` exemplar cite
  pre-landing seats; if wave-11 adjudication reverses them the arms survive
  on re-derived constants (the mechanism claims don't depend on the exact
  numbers).
- **Cost**: X1 ~30-line probes per runtime; X2 three cells; X3/X5 one probe
  each; X4 the largest (~14-arm shape by physserver precedent). Total is
  well under one lane-round of wall time on this host.

## Verification

Commands run this seat (no writes outside stated scope):

```
python3 -c 'import io,sys; print("DEFAULT_BUFFER_SIZE", io.DEFAULT_BUFFER_SIZE)'
  → 131072 (CPython 3.14.7)
python3  -c 'import sys,os; sys.stdout.write("HEAD "); os.system("printf INJECTED"); sys.stdout.write(" TAIL\n")' | cat -A
  → INJECTEDHEAD  TAIL$
python3 -u -c '<same>' | cat -A                                        → HEAD INJECTED TAIL$
python3  -c 'print("HEAD ",end="",flush=True); os.system("printf INJECTED"); sys.stdout.write(" TAIL\n")' | cat -A
  → HEAD INJECTED TAIL$
grep -E 'PHYS-(DET|EVT|STEP|COUNTS|DETERM)' out/run-{1,6}.txt | md5sum   → identical across reps
diff run-1.txt run-3.txt → only PHYS-PERF/PHYS-ACC (wall-clock) lines differ
```

File:line anchors checked: `r70-critic.md:12-72` (fd1 seam), LOVE splice
probe `corpus/live/r70-critic/splice_probe/main.lua:26-31` (`io.write` head
write-through), `fa-pygame.md:76-84` (withholding), `r71-critic.md` F1
(131072 B edge, bufferedio.c:2104 rule), `fa-sndfile.md` (fallback set,
sf_open vs sf_open_fd partition), `fb-pipewire.md` §a-c (daemon-first check,
single open, mpv inverted fork), `fb-lovephysics.md` §c (in_step=true,
per-callback snapshots), `fa-bpy-evalcat.md` §1-2 (ops auto-eval, handler
split, dead msgbus/timers), `fb-physserver.md` (edge-0 table, flush_queries
absent, unprobed list), `r79-scout.md` §1 (shared graph, no drain),
`r80-author.md` (closure falsifier armed, violations=0),
`r71-boundary.md` probe-C (`pipe:` never lseeks fd0), `r72-boundary.md` /
`r72-critic.md` (lattice re-check, `.au` exemplar, 12-byte sniff consumed).
Wave briefs: `.ufo/waves/shokunin-train-20261101-w{10,11}/tasks/*`.

## Limits

- Two lanes' wave-11 landings are absent at snapshot; in-flight findings are
  cited as seat evidence, and arms are stated against mechanisms rather than
  the specific constants those seats measured.
- The X1 reordering demo is interpreter-level (plain `python3`), not yet run
  inside a pygame/bpy process — that is the arm's job.
- No probe of tracked fixtures; no verdicts on in-flight landings; corpus
  hygiene stays with xsentinel's scope.
