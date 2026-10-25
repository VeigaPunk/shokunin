# x-connector — sibling-overlap scan (wave shokunin-train-20261013-w3)

Seat: connector (leaf). Declared axes this wave: audio r64 **coverage**,
game-dev-2d r63 **depth**, game-dev-3d r72 **depth**.
Scan executed 2026-10-14 while the wave was in flight; all evidence is
read-only (`git log`/`git status`/`git show`, file reads, grep). Sole write is
this file. No subagents dispatched; leaf bound honored.

Lanes in scope (worktree cwd → canonical repo via `.shokunin/<lane>` symlink):

- **audio r64** — axis coverage: pin the `wValidBitsPerSample`→codec
  reclassification step map under the `act`/ffmpeg bridge (74-variant sweep,
  task `AudioR64*`).
- **game-dev-2d r63** — axis depth: land the merged-stream signature-spoof
  boundary as tracked rows (`descendant_pipe_forged_signature_release` CASES
  row + `probe_descendant_signature_spoof` meta row — the r62 critic's
  isolated measurement promoted to committed evidence; task `G2dR63*`).
- **game-dev-3d r72** — axis depth: pin `path_desired_distance` waypoint-pop
  semantics and the two-mode `is_navigation_finished` with equality-edge arms
  (+22 CASES rows; task `G3dR72*`).

In-flight state observed at scan time (`git status --porcelain`):

| repo | observed | attribution |
|---|---|---|
| audio-shokunin | ` M corpus/fixtures/{build_artifacts.py,measure_audio.py}`, `M` two `.pyc`, `?? corpus/live/r64-*/`, `?? corpus/live/runs/20261014T*` | r64 author's declared tracked edits + leaf scratch — not this seat |
| game-dev-2d-shokunin | ` M corpus/fixtures/{descendant_pipe_probe.gd,run_battery.py}`, `?? corpus/live/r63-*/`, `?? reports/round-63/` | r63 author's landed tracked rows + leaf scratch — not this seat |
| game-dev-3d-shokunin | `?? reports/round-72/`; by final capture also ` M corpus/fixtures/{navagent3d_detour.gd,run_battery.py}` | leaf reports, then r72 author's declared +297/−1 fixture / +44/−0 runner landing mid-scan — not this seat |

HEADs at scan: audio `37d4c57` (WT carries r64 work), 2d `edbd945` (WT carries
r63 work, runner sha256 `b6f3d5c2…` vs HEAD `0c4c9bee…`), 3d `996ea37` (WT
runner `4e9ead37…` = r72 author's landed +44/−0). Third consecutive wave in
which sibling seats' tracked diffs land mid-scan — every line cite below is
pinned to a named sha or WT position.

---

## (a) Does the 3d runner share the 2d signature-spoof seam?

### a.1 The seam as 2d pinned it (tracked, this round)

2d `run_battery.py` (WT `b6f3d5c2…`): `run_process` :149-152 returns
`proc.stdout + proc.stderr` — **streams merged at capture**. `classify_process`
:160-177 gates on `signature in output` — **substring presence over the merged
string**, plus unrelated-`ERROR:` filtering. The r63 landing records the
measured boundary (`descendant_pipe_probe.gd` `--spawn-forge-*` arms, runner
comment :103 "forged signature accepted"):

| arm | driver | exit | error | sig present | classify |
|---|---|---|---|---|---|
| `forge_release` @8s | `run_process` verbatim | 0 | None | yes (**forged, post-death**) | **True** — tracked PASS |
| `forge_hold` @3.0s | bounded Popen | None | `TIMEOUT after 3.0 seconds` | yes (forged) | **False** — via timeout fields only |

The forged writes are provably post-death (ppid reparented to subreaper 1573,
`write_ppid ≠ godot_pid`; `child_exit_at_timeout=0`). Rejection in the hold
arm rides entirely on `timed_out`/`error`/`actual_exit=None` — the signature
axis is satisfied and overridden; `classify_if_error_none=True` isolates that
exactly (r63-author receipt `spoof-verdicts.json` sha `f24b10b9…`).

### a.2 3d's seam shape — narrower, same family

3d `run_battery.py` (WT `4e9ead37…`): `run_process` :319-322 returns
`(proc.stdout, proc.stderr, proc.returncode, None)` — **streams never merged
on the accept path**. `classify` :334-360 requires the marker as an **exact
stripped line of stdout** (`marker not in lines`, :346); *any* nonempty stderr
line rejects (:348-350); SCRIPT ERROR/Parse Error reject per-stream
(:351-355); a merged `stdout + stderr` scan exists but **only on the reject
axis** (:356-360 — `ERROR:`/leak warnings poison, never satisfy).

So: **3d stream handling is NOT merged the same way.** The injection surface
narrows twice: the forged bytes must arrive on **fd1** (an fd2 write cannot
satisfy the marker check — it is rejected), and they must form a **complete
line** (a seam-straddling fragment cannot match exact-line membership).

### a.3 Same forgery family applies — measured, not inferred

The forgery class is *acceptance gated on captured-byte presence without
writer attribution*. 3d's exact-line-on-stdout gate narrows the syntax the
forgery must produce but changes nothing about authorship: a descendant
inheriting fd1 and writing the exact marker line **post-death** produces a
record identical to a genuine PASS (`exit 0`, `error None`, clean stderr,
marker line present). The lane's own sibling already measured precisely this:

- 2d r63-scout (:56-60, :175, :246): a forged descendant write on inherited
  **fd1** lands on stdout → `classify_streams` (2d's stream-separated
  classifier — the 3d CASES shape: signature-on-stdout + strict stderr
  rejection, WT :179-202) returns **True** on the forged write.
  *"'signature on stdout' ≠ 'signature from the child' — any future port to
  stream-separated CASES classification does not close this boundary."*
- 3d's own `probe_stream_attribution` (:447) proves the runner enforces
  *stream* attribution (the `--emit-stderr` reject arm) — but stream
  attribution is not *process* attribution. The probe instruments which fd
  carried a byte, never which pid wrote it.
- The r63-boundary depth sweep generalizes the breach: `d2_spoof` — a
  doubly-orphaned **grandchild** writing the signature after *both* ancestors'
  deaths — classifies **True** at 1.451s. "EOF releases only when the LAST
  fd-carrier of any generation dies. **Depth is never the variable — fd
  carriage is.**" The mechanism is POSIX fd inheritance; nothing in it is
  lane-local — 3d's `subprocess.run(capture_output=True)` pipes inherit
  identically, and no 3d CASES fixture currently exercises the seam (the
  only spawning fixture, `timeout_tree3d.gd`, is probe-only).

What 3d adds that 2d lacks on CASES records: `elapsed_seconds`
(corroborating a hold-shape — elapsed ≈ bound — but not discriminating it)
and an `error`-field timeout path identical in shape (`TIMEOUT after 20
seconds`, `actual_exit=None` → `classify` False via `code is None` + `error`
reasons :337-341). As in 2d, only the **release shape** can produce a forged
PASS; the hold shape is quarantined by the error axis in both lanes.

3d's probe path already owns the closing apparatus the CASES path lacks:
`probe_crash_exit` reads `marker_observed_while_live` (marker must be seen
while `process.poll() is None` — a liveness-gated marker read), and
`probe_tree_timeout` verifies witness identity via `/proc` ppid/pgid/
starttime/cmdline before cleanup. Neither mechanism reaches `classify`.

### a.4 A 3d-only asymmetry worth naming

Because 3d's reject axis scans the merged `stdout + stderr` for `ERROR:`
(:356-360), a descendant can also *sabotage*: one `ERROR:` line on either
inherited fd poisons a genuine child's acceptance. That is a denial vector,
not an acceptance vector — symmetric origin-blindness, opposite direction.
2d's allowlist shape (`expected_errors`) partially bounds its equivalent.

---

## (b) Audio's per-packet floor vs game-lane fixture evidence conventions

### b.1 The law, precisely (r62 established, r64 measured exhaustively)

Under the `act`→ffmpeg bridge (route pinned r63: `len≥257 ∧ "RIFF"@0 ∧
file[256]==0x84`, no runtime fallback — one handler chosen at autodetect),
decode count = **Σᵢ floor(pktᵢ/w)·ch** where `w=(V+7)>>3` and the packet
boundaries are themselves width-derived (bitrate-scaled). r64's 74-variant
sweep measured six steps: 1–8→`pcm_u8` [4096,4096,3328]→11,520; 9–16→s16le
[8192,3328]→5,760; 17–24→s24le→**3,839**; 25–32→s32le [11520]→2,880;
33–56→codec-NONE (exit 2 `premature EOF`); 57–64→**s64le** [11520]→1,440
(a step the sketched range did not predict); ≥65→NONE.

The r64 critic's refinements bound the law honestly: the 1-D map is a slice
of a multi-input function (declared `block_align` moves 3839↔3840 at fixed
valid=17; the missing `×ch` factor; the LAST `data` chunk *replaces* the
stream; `data_size∈{0,0xFFFFFFFF}` reads rest-of-file; a named-codec
empty-AU class exits 0 with 0 samples — distinguishable from codec-NONE's
exit 2). Sub-frame packets drop whole: `[8192,1]`→+0. The load-bearing
content is the same: **residue at each unit boundary is discarded per unit
and no whole-stream correction recovers it** — `floor(11520/3)=3840 ≠ 3839`.

### b.2 The structural isomorphism in the game lanes' evidence conventions

The audio law is a statement about *counting in units*: an aggregate over a
partition is not the aggregate over the merged stream; unit boundaries are
load-bearing. The game lanes' evidence conventions instantiate the same
accounting invariant on different units — some correctly, one not:

| unit boundary | where | consequence |
|---|---|---|
| **per-line** | 3d `marker not in stdout.splitlines()` (:346) | a marker fragmented across lines never reassembles — `floor` per line unit |
| **per-stream** | 3d separate accept path vs 2d merged `stdout+stderr` | a signature straddling the concat seam (fd1 tail + fd2 head) exists in **neither** stream yet satisfies 2d's `signature in output` — the merged read *harvests boundary residue*, exactly the counting error the packet law forbids |
| **per-case** | both runners `all(verdict=="PASS")` | no battery-level sum can launder a failed row's residue into credit |
| **per-timeout-residue** | `exc.stdout`/`exc.stderr` drained partials | recorded as evidence, never counted toward acceptance — `error` set ⇒ always False |
| **per-process** | **absent in both** | the pipe is used as the unit; a descendant's bytes enter the parent's account — the 2d tracked forged PASS is precisely *counting bytes by delivery chunk instead of by authored unit* |

### b.3 Where the analogy must stop (discernment bound)

This is a **convention-level isomorphism, not a mechanism equivalence**.
The audio law is decoder semantics — deterministic, implemented in
libavcodec. The game-lane units are acceptance-policy choices. What transfers
is the *accounting* truth: post-merge analysis cannot recover per-unit
residue. Merged output is to the game classifier what a whole-file floor is
to the packetized decoder: the information needed for attribution was
discarded at the boundary and no downstream check regenerates it. Audio's
own mirror-image instance makes the point in-domain: SoX reads only the AU
pipe — "a missing decoder, a demux failure, and a missing binary are
indistinguishable" (r63-boundary): the child ffmpeg's stderr/exit are
invisible through the byte contract, exactly as a descendant's writes are
indistinguishable inside the parent's captured pipe.

The missing unit in both game lanes is the **process**: audio counts per
packet; the game runners count per pipe. The correct unit for *provenance*
is the writer — and that floor exists nowhere on either CASES accept path.

---

## (c) Contested or overlapping surfaces this round

**c.1 — The shared mechanism surface (the round's true overlap; not
contested scope).** Both game lanes probe complementary edges of one POSIX
mechanism on the same `/usr/bin/godot` 4.7.2 binary: fd inheritance, pipe-EOF
vs liveness, reparenting to the subreaper (pid 1573 on this host).
2d instruments the **byte edge** (what a descendant can forge into captured
output — r63's tracked acceptance boundary, extended this round to depth ≥2:
"depth is never the variable — fd carriage is"). 3d instruments the
**identity edge** (`probe_tree_timeout` verifies witness ppid/pgid/starttime/
cmdline via `/proc` before targeted cleanup; `bounded_claim`: *"One
identified detached Godot-spawned witness… not arbitrary process-tree
cleanup"*). Neither duplicates the other; each lane's finding is predictive
for the other's runner. This is evidence-plumbing overlap — product
ownership (audio signal analysis / 2d engine fixtures / 3d navigation+spatial
fixtures) remains disjoint and uncontested.

**c.2 — "Harness/evidence auditing" refusal tension (enduring, not new).**
Both game provinces refuse *harness/evidence auditing* (harness-integrity,
gate-evidence, rlm-dispatch — all named as other owners). Yet this wave's
moves — and r62's before them — are self-instrumentation boundary work:
2d pins its own classifier's acceptance seam; 3d maintains probes that audit
its own runner's attribution. The de facto boundary observed this wave:
**each lane audits only its own measurement instrument** — the runner is
part of the lane's owned executable corpus — while no lane touches shared
gates or a sibling's verdicts. The refused targets are absent owners in
this wave; the tension is jurisdictional, not behavioral. Named, not
adjudicated.

**c.3 — audio↔2d engine-audio seam (carried from w1, still unbound).**
2d's CASES retains `audio_playback`/`audio_no_play` with
`classify_audio_process` (ObjectDB leak-warning allowlist) — engine-runtime
playback through `AudioStreamPlayer`, a different layer from audio's
file-level decode/measurement (no duration/loudness/spectral claims on it,
consistent with the w1 finding: claimed by 2d occupation and audio domain,
verified by neither in the joint sense). No artifact-level bind this wave:
audio r64 never touches Godot; 2d r63 never touches WAV semantics.

**c.4 — Receipt-persistence divergence across lanes.** Audio *tracks* its
receipts (`corpus/live/runs/` committed — 86-command ledger replayed
43/43 exit-identical, byte-identical receipts; shared timestamp namespace
because `measure_audio.py` has no `--runs` flag — sibling seats interleave
and attribute by before/after census). Both game lanes **gitignore**
`corpus/live/` — every game-lane verifier carries the "on-disk only" caveat
(r72-reviewer §residual). Same path shape, opposite persistence semantics —
a real convention split, currently uncoordination-requiring because no
consumer crosses lanes.

**c.5 — Mid-flight drift as a standing hazard (third consecutive wave).**
3d r71's `seeds_unchanged=false` incident; this wave: 2d r63-boundary
recorded the sibling author diff landing mid-probe (third round running)
and re-verified classifiers byte-identical HEAD↔WT via `ast` extraction;
audio's committed-receipt surface makes the same drift visible via SHA
rather than silent. The convergent defense observed in all three lanes:
frozen `git archive HEAD` baseline replay + byte-level receipts + sha-pinned
citations. Asymmetric capability note: 3d's runner carries `seed_digests()`/
`seeds_unchanged` (it *detected* the r71 incident); 2d's runner has no
equivalent and relies on mtime/`git status` forensics.

**c.6 — Shared substrate: canonical-repo/worktree duality.** All three lanes
resolve `.shokunin/<lane>` into canonical `*-shokunin` repos; commit SHAs
resolve only canonically (flagged this wave by both the audio r64 reviewer
and the 3d r72 reviewer). Integration-relevant property, not a conflict.

**c.7 — Connector↔sentinel split.** XSentinel reads the same three repos
read-only for contamination/credential/route census; disjoint concern,
disjoint output (`x-sentinel.md`). No surface shared but reads.

---

## (d) Lane-repo write attestation

Every operation this seat performed was read-only: file reads, `grep`,
`git status`/`git show`/`git log`/`git diff`, `ls`, `head`, `sha256sum`,
`find`. The `git status` captures in the header table are **pre-existing
sibling state** (r63/r64 author tracked diffs in flight, leaf scratch dirs);
none of it was produced here. This seat's only filesystem write is:

`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin-train-20261013-w3/x-connector.md`

— inside the fleet wave root (its own repo, HEAD `90c2d4a`), which is the
dispatch-sanctioned connector write scope. No tracked content in
`audio-shokunin`, `game-dev-2d-shokunin`, or `game-dev-3d-shokunin` was
created or modified; no fixture, runner, CASES row, report, receipt, LOG,
SCORECARD, lesson, or manifest was touched; no commit/checkout/stash/push;
no subagent dispatched.

---

## The one bounded move (seat-card proposal)

**Name and land the per-writer floor — the closing mechanism already exists,
on the wrong path.** The round's three declared moves synthesize to one
non-obvious move none of the lanes declared:

- **Audio supplies the invariant**: evidence is only valid counted in whole
  units on its natural boundary; merged aggregates can't recover boundary
  residue (b.2). The natural unit for *provenance* is the writing process,
  not the pipe.
- **2d supplies the measured breach**: the tracked forged-PASS row —
  presence without authorship, depth-agnostic (b.2 last row; a.1).
- **3d supplies the unused apparatus**: `probe_crash_exit`'s
  `marker_observed_while_live` (liveness-gated marker read) and
  `probe_tree_timeout`'s `/proc` identity verification — built, committed,
  exercised on the opt-in path, and absent from `classify`.

The cheapest honest landing is in 2d, where the fixture already exists:
a `descendant_pipe_probe.gd` `--spawn-forge-release` arm under a
bounded-Popen meta arm (the vehicle the r63 hold arm already uses) that
reads the marker **while the direct child is live** and records
`marker_observed_while_live`/`marker_first_seen_at`. On the post-death
forgery that gate flips the verdict while a genuine child marker still
passes — one discriminating pair, additive-only, no CASES schema change
(CASES can't hold a reject-shape record; the meta row is the vehicle, per
the w2 finding). It improves the **depth** axis (closes the only open arm
of a now-tracked boundary) with no axis harmed: no tracked CASES semantic
changes, no verdict reshaping, no sibling scope absorbed — the port
direction is mechanism-to-mechanism, and 3d's PROVINCE licenses mechanism
inheritance ("shared fixture patterns are inherited").

This complements the w2 connector's sketch (3d→2d tree-timeout port) by
reversing the valuable direction: w2 ported 3d's *cleanup*; the r63 finding
says the scarce asset is 3d's *liveness-gated acceptance gate*, not its
killpg. For 3d, the same synthesis is available but cheaper to defer: its
CASES accept path is currently unexercised by any spawning fixture, so its
per-writer floor is a latent gap, not a tracked boundary.

### Risks of the proposed move (stated, not smoothed)

- `while-live` narrows the forgery class to *post-death* writes only. A
  descendant writing the marker **during** the parent's life still passes —
  the gate floors per-liveness-window, not per-writer. Full per-writer
  accounting (per-fd separation or reader-side pid tagging) is a different,
  larger move; this proposal must claim only "post-death writes excluded."
- Marker timing becomes evidence: `marker_first_seen_at` vs child-exit
  ordering is timing-dependent; on a loaded host a genuine late flush could
  be misclassified. Needs a margin (deadline between child exit and drain,
  or a flag the fixture writes before spawning).
- The arm is Linux/`/proc`-coupled in the same way as every existing probe;
  keep the typed-error guard (`os.name != "posix" or not /proc`).

### Contradictions left explicit (not scored)

1. Both game provinces refuse "harness/evidence auditing" while both lanes'
  wave moves *are* harness-boundary evidence work (c.2). Resolution observed
  is jurisdictional convention; nothing in the provinces' text settles it.
2. 3d's runner is simultaneously stricter (exact-line, stderr-reject) and
  equally origin-blind (no writer attribution) — "narrower seam" and "same
  family" are both true; they are different claims about different axes.
3. Audio's receipt convention (tracked, census-attributed) and the game
  lanes' (gitignored, on-disk) can't both be the fleet-evidence ideal;
  no consumer currently requires reconciling them.
4. The 2d forgery boundary is *tracked as accepting* — a PASS row encoding
  a known-false provenance claim. `verdict==PASS` there means "the runner
  accepted," not "the evidence is sound" — the two readings coexist in one
  field.

## Verification

All claims resolve to resolvable artifacts: 2d runner WT sha `b6f3d5c2…`
(`run_process` :149-152 merged capture; `classify_process` :160-177
`signature in output`; `classify_streams` :179-202 stdout+strict-stderr —
the 3d-shaped variant, measured accepting the forged fd1 write per
`r63-scout.md` §:56-60/:175/:246; CASES comment :103); HEAD-pre-edit sha
`0c4c9bee…` = `edbd945`. 3d runner WT sha `4e9ead37…` (`run_process`
:319-322 separate; `classify` :334-360 — exact-line :346, stderr-reject
:348-350, reject-side merged `ERROR:` scan :356-360; `probe_stream_attribution`
:447). 2d r63: `spoof-verdicts.json` sha `f24b10b9…`; `r63-author.md`
arms table; `r63-boundary.md` depth table (`d2_spoof` forged PASS 1.451s,
`d3_hold` ggc-only holder; "depth is never the variable — fd carriage is").
3d r72: `r72-author.md` semantics block (pop strict `<` live-position
Euclidean; reachable INCLUSIVE `<=`; finished two-mode `reached OR
(¬reachable ∧ idx==size−1 ∧ euclid→final<pdd)`, non-monotone in tdd T,F,T;
latched); `r72-reviewer.md` AGREE×10, 90/90+4probes, `seeds_unchanged=true`,
Node 31/31. Audio r64: `r64-author.md` 74-variant sweep + step-map table;
`r64-critic.md` refinements (multi-input function, `×ch` factor,
sub-frame drop `[8192,1]`→+0, no codec fallback ever, empty-AU exit-0
class, last-`data`-rebase); `r64-reviewer.md` AGREE, 86-cmd 43/43 replay.
Audio mechanism bounds: SoX_ng 14.8.0.1 `formats.c:93` `CHECK(act,0,4,
"RIFF",256,1,"\x84")` preceding `CHECK(wav,…)` — content- and version-
dependent; `act`→`(ffmpeg)` pseudo-handler (AU intermediary; no native act
decoder, no post-failure retry — byte-edit reroutes ≠ fallback).
Province refs: all three `PROVINCE.md` files (ownership/refusal lists).
Prior wave refs: w1 `x-connector.md` §a.1 (engine-audio seam);
w2 `x-connector.md` §a (tree-timeout port sketch, I1-I12 flags; the
CASES-cannot-reject finding; 3d probe line map).

Host-bound caveats carried: Godot `4.7.2.stable.arch_linux.ed1daf0bf`
stationary-agent L-corridor only for all navigation claims; Linux `/proc`/
subreaper semantics for all process claims; SoX_ng 14.8.0.1 / ffmpeg n9.0.1
for all codec claims; Python 3.14.7 for `subprocess.run` timeout semantics.
No claim here extends past its measured build.

| godspeed
