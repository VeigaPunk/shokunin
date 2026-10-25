# x-connector — sibling-overlap scan (wave shokunin-train-20261013-w2)

Seat: connector (leaf). Judged axes: expansion, quality, discernment.
Scan executed 2026-10-13 while the wave was in flight; all evidence is read-only
(`git log`/`git show`/`git status`/`git diff`, file reads). Sole write is this file.

Lanes in scope (worktree cwd → canonical repo via `.shokunin/<lane>` symlink):
- audio r63-in-flight (axis: depth — SoX `act` autodetect byte predicate; task `AudioR63*`)
- game-dev-2d r62-in-flight (axis: coverage — track the r61-probed pipe-EOF
  misattribution as a classification surface; task `G2dR62*`)
- game-dev-3d r71-in-flight (axis: depth — `path_postprocessing` invariance of the
  r70-proven Euclidean `distance_to_target`; task `G3dR71*`)

In-flight state observed at scan time:
- 3d: `git status` shows ` M corpus/fixtures/navagent3d_detour.gd` (+45),
  ` M corpus/fixtures/run_battery.py` (+4 — two CASES rows
  `navagent3d_detour_post_edgecentered`/`_post_none`, claiming `distance=3.605551`
  invariant with changed `next`/`pathlen`), `?? reports/round-71/r71-baseline.md`.
  Runner is HEAD 709 lines → WT 713; `def probe_tree_timeout` moved HEAD:423 → WT:427.
- 2d: `?? reports/round-62/r62-baseline.md` only — frozen HEAD `08d80dc`, runner
  sha256 `d705bca719fc…` (byte-identical to WT), seven-flag battery 92/92 replayed
  (`corpus/live/r62-baseline/runs/20261013T233453788036Z/`). No tracked r62 edits yet.
- audio: `?? reports/round-63/r63-scout.md` — predicate already pinned:
  `len>256 && bytes[0..3]=="RIFF" && bytes[256]==0x84` (RIFF-magic conjunct newly
  stated). Baseline sweep runs under `corpus/live/runs/*ui-extensible*`.

---

## (a) The 3d→2d tree-timeout port — concrete diff sketch

### a.0 What 3d's mechanism is (three committed components)

All at `~/Projects/shokunin/game-dev-3d-shokunin/corpus/fixtures/`, HEAD positions
(r71's in-flight +4 CASES rows shift WT positions +4 below line ~57):

1. **Fixture `timeout_tree3d.gd`** (35 lines, sha `403a2e3e…`): `extends SceneTree`;
   Node3D setup-sanity arm (`:9-16`); on `--hold-open`,
   `OS.create_process("/usr/bin/python3", [helper, pidfile], false)` (`:20`) — on this
   host the spawned process lands in its **own** process group (pgid = witness pid,
   per the r5 lesson and the runner's `pgid == witness_pid` gate); waits ≤2 s for the
   pidfile (`:25-31`); prints marker `TREE_TIMEOUT_3D: spatial node ready`; holds 30 s.
2. **Witness `timeout_descendant.py`** (11 lines, sha `c3a52834…`): writes
   `{pid, pgid, ppid}` JSON to `argv[1]`, sleeps 30 s. Being Godot-spawned it
   **inherits the capture pipes** — that inheritance is the entire hazard.
3. **`probe_tree_timeout(godot, scratch, run_dir)`** (`run_battery.py:423-543`):
   - normal arm `run_process(cmd, 8)` → classify expected 0 + marker;
   - hold-open arm `Popen(..., start_new_session=True)` (`:466-467`) — makes the Godot
     child a group leader so `os.killpg(process.pid, …)` is a legal, scoped group kill;
   - `communicate(timeout=3)` → expected `TimeoutExpired` (`:469-477`);
   - reads `scratch/timeout-descendant.json` → `proc_identity(pid)` parses
     `/proc/<pid>/cmdline`+`stat` → `{state, ppid, pgid, starttime}` (`:443-453`);
     `witness_verified` requires live, `ppid == godot pid`, `pgid == witness pid`,
     cmdline contains helper path AND pidfile path (`:484-488`);
     `same_live_witness()` adds `starttime` equality = PID-reuse guard (`:455-460`);
   - cleanup order (`:489-508`): `os.killpg(process.pid, SIGKILL)` → SIGTERM to
     verified witness → 3 s grace → SIGKILL escalation → **then**
     `communicate(timeout=3)` for `cleanup_exit` — the r5 ordering fix (drain AFTER
     the pipe-holding witness dies, else the drain itself blocks);
   - verdict requires `normal_ok and timed_out and actual_exit is None
     and cleanup_exit is not None and marker_observed and classified is False
     and witness_verified and witness_gone
     and witness_cleanup == "SIGTERM to verified detached witness"` (`:533-537`);
   - receipt `tree-timeout-verdicts.json`, bounded_claim: *"One identified detached
     Godot-spawned witness terminated after direct-child timeout; not arbitrary
     process-tree cleanup."* (`:538-540`)
   - `finally` (`:516-526`): killpg-if-live + communicate(3); forced final SIGKILL
     gated on `witness_verified and same_live_witness()` — the r5 review's
     PPID/PGID ownership gate.
   - Plumbing: flag `--probe-tree-timeout` (`:562-563`), dispatch `:620-622`,
     `tree_probe_ok` folded into `verdict` (`:692`) and payload (`:701`).
   - Verified live: r70 full battery 88/88 with `tree_probe_ok=true`
     (`corpus/live/r70-author/runs/20261013T221041493928Z/verdicts.json`).

### a.1 Where it lands in 2d's runner

2d's `run_battery.py` (1012 lines, sha `d705bca719fc…`, == frozen r62 baseline) is
a single-`main()` file: CASES table `:18-98`; probe flags `:103-111`; helpers nested
in main: `run_process` `:142-151` (merged `proc.stdout + proc.stderr`),
`classify_process` `:153-170` (substring `signature in output` + unrelated-ERROR
filter + allowlist `expected_errors` `:393`); CASES loop `:454-455`; meta rows
appended at `:505` (`probe_save_independent_process`), `:539`
(`probe_spontaneous_crash_classification`); probe blocks `if args.probe_crash_exit:`
`:796-911`, `if args.probe_timeout:` `:913-1001` (`bounded_run` `:921-968`, three arms
`:970-972`); final `payload`/`verdicts.json` `:1003-1006`; PASS iff
`all(r["verdict"]=="PASS")` `:1005`. Scratch staging `:117-125` copies every
non-hidden fixture file → a `.py` witness lands in scratch automatically.

**Landing map (additive-only, ~+130 lines over three hunks):**

| hunk | position | content |
|---|---|---|
| fixture | `corpus/fixtures/timeout_tree2d.gd` NEW (~30 lines) | port of `timeout_tree3d.gd`; Node2D sanity arm (2d convention), marker `TREE_TIMEOUT_2D: 2d node ready`, same `--hold-open` arm spawning `OS.create_process("/usr/bin/python3", [helper, pidfile], false)` |
| witness | `corpus/fixtures/timeout_descendant.py` NEW | **verbatim 11-line copy** of 3d's helper — keep it byte-identical so the `/proc` cmdline identity check `str(scratch/"timeout_descendant.py") in cmdline` ports unmodified |
| flag | after `:110` | `parser.add_argument("--probe-tree-timeout", action="store_true", help="time out a Godot child and explicitly clean one identified detached witness")` |
| probe block | after `:1001`, before `payload =` (`:1003`) | `if args.probe_tree_timeout:` block ~100 lines: accept arm via `run_process(cmd, 8)` + `classify_process(..., 0, marker_text)`; hold arm via its OWN `Popen(..., start_new_session=True, text=True, bufsize=1)`; port `proc_identity`/`same_live_witness` verbatim; keep the killpg→SIGTERM-witness→grace→drain order verbatim; record fields in `bounded_run` shape (`raw_stdout`/`raw_stderr`, `timed_out`, `process_was_running`, `direct_child_alive_after_cleanup`, `cleanup_exit_code`); `inner_classification = classify_process(actual_exit, error, raw_stdout+raw_stderr, 0, marker_text)`; append `{"case": "probe_tree_timeout", "verdict": ..., "artifact": ...}`; write `tree-timeout-verdicts.json` |

Sketch (abridged to the parts that differ from a verbatim copy):

```python
# after line 1001 — inside main(), matching probe_* block convention
if args.probe_tree_timeout:
    marker_text = "TREE_TIMEOUT_2D: 2d node ready"
    script_path = "res://timeout_tree2d.gd"
    hold_command = [args.godot, "--headless", "--path", str(scratch),
                    "--script", script_path, "--", "--hold-open"]
    accept_out, accept_code, accept_err = run_process(hold_command[:-2], 8)
    accept_ok = classify_process(accept_code, accept_err, accept_out, 0, marker_text)
    witness_path = scratch / "timeout-descendant.json"
    witness_pid = witness_start = None
    def proc_identity(pid):      # VERBATIM from 3d run_battery.py:443-453
        ...
    def same_live_witness():     # VERBATIM from :455-460
        ...
    hold = {…record skeleton like bounded_run :924-928…}
    process = None
    try:
        if os.name != "posix" or not Path("/proc/self/stat").exists():
            hold["error"] = "Linux /proc and POSIX signals required"
        else:
            process = subprocess.Popen(hold_command, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True, bufsize=1,
                                       start_new_session=True)          # (I1)
            try:
                out, err = process.communicate(timeout=3.0)
            except subprocess.TimeoutExpired:
                hold["timed_out"] = True
                # marker gate, pidfile read, proc_identity gates — verbatim (:477-488)
                if process.poll() is None:
                    os.killpg(process.pid, signal.SIGKILL)               # group kill
                if hold["witness_verified"] and same_live_witness():
                    os.kill(witness_pid, signal.SIGTERM)                 # (I2) BEFORE drain
                    …3 s grace → SIGKILL escalation, verbatim :494-502…
                out, err = process.communicate(timeout=cleanup_seconds)  # pipes now free
    finally:
        …verbatim :517-526, incl. the PPID/PGID-gated forced SIGKILL…   # (I8)
    hold["inner_classification"] = classify_process(
        hold["actual_exit"], hold["error"],
        hold["raw_stdout"] + hold["raw_stderr"], 0, marker_text)         # (I3)
    verdict = (accept_ok and hold["timed_out"] and hold["actual_exit"] is None
               and hold["cleanup_exit_code"] is not None and hold["marker_observed"]
               and not hold["inner_classification"] and hold["witness_verified"]
               and hold["witness_gone"]
               and hold["witness_cleanup"] == "SIGTERM to verified detached witness")
    artifact = run_dir / "tree-timeout-verdicts.json"; …
    results.append({"case": "probe_tree_timeout", "verdict": …, "artifact": str(artifact)})
```

### a.2 2d-specific incompatibilities — the flags that decide the port

**I1 — `killpg` is illegal without `start_new_session`; never retrofit shared paths.**
Today every 2d Godot child runs in the harness's own process group (r61 boundary
mechanism read: `run_process` has "No `start_new_session`/`process_group`").
`os.killpg(process.pid)` on such a child raises `ProcessLookupError` (pid ≠ pgid);
the naive fix `os.killpg(os.getpgid(pid))` would **SIGKILL the harness's own group —
the runner and every sibling seat shell sharing it**. The `start_new_session=True` +
`killpg(process.pid)` pair must live ONLY inside the new probe's own `Popen`.
Retrofitting it into `run_process` (`:142`) or `bounded_run` (`:921`) re-groups all
92 rows' children and falsifies the process-semantics rows r62 is pinning right now.

**I2 — witness-before-drain ordering is load-bearing.** 3d's first author-run failed
exactly this way: witness holds inherited pipes → `communicate` drains block →
"cleanup exceeded 3s" → FAIL (`corpus/lessons/r5-identified-witness-timeout.md:10`).
Kill Godot's group, SIGTERM the *verified* witness, wait for `witness_gone`, THEN
`communicate`. Reordering ports the bug, not the mechanism.

**I3 — stream/marker convention must be translated, and it weakens one check.**
3d keeps stdout/stderr split and requires the marker as an **exact stdout line**
(`classify` `:297-298`, `splitlines().count(marker)==1` `:528`). 2d merges streams in
`run_process` (`:145`) and `classify_process` is substring (`signature in output`
`:169`). Port into 2d convention (`raw_stdout`/`raw_stderr` fields like
probe_crash_exit; classify on the merge) — consistent, but a `TREE_TIMEOUT_2D:`
substring admits marker-prefix false-positives the exact-line check rejects. If the
boundary seat's scratch shows that matters, the row can pin an exact-line check
locally in the block instead — still additive.

**I4 — text vs bytes records.** 3d's probe is bytes (`marker.encode() in
raw_out.splitlines()`). 2d probes use `text=True` + str. Mechanical; just don't mix
(decode gates at `:940-941` show 2d already normalizes `exc.stdout` bytes|str).

**I5 — 3d's bounded_claim does NOT survive translation; add the arm 3d lacks.**
3d's claim "after direct-child timeout" is true only because `timeout_tree3d.gd`
holds Godot open 30 s — the timeout there really is child-liveness. On 2d's runner,
r61 proved the *same* `communicate` TimeoutExpired fires with the child already dead
(hold arm: `godot_alive_at_return=false`, elapsed 3.003 s, `error="TIMEOUT after
3.0 seconds"` — `reports/round-61/r61-boundary.md:59-67`). A faithful 2d port
therefore needs a **second arm 3d doesn't have** — `--clean-exit-witness`: fixture
quits ~0.5 s while the witness holds pipes — producing `timed_out=True,
process_was_running=False` (the discriminating pair `bounded_run` already records:
`timed_out`+`process_was_running` is precisely the misattribution witness). Expected
post-cleanup `cleanup_exit_code == 0`: the child exited 0 yet the row timed out.
Without this arm the ported probe would silently re-import 3d's claim shape onto a
runner whose r62 rows simultaneously assert the opposite — the port complements r62
only if it names that split: **the mechanism owns descendant cleanup; it does not
make the timeout bound child-liveness-aware.**

**I6 — flag-surface drift: eight-flag vs unconditional meta.** A new
`--probe-tree-timeout` flag changes the canonical invocation everywhere it is cited
verbatim: SCORECARD counting commands (`SCORECARD.md` depth/coverage rows), every
seat brief's "full seven-flag battery" wording, prior reports' command strings. The
alternative is an unconditional meta row appended like `:505`/`:539` — but this
probe cannot re-use captured outputs (it needs live process control), so
unconditional costs ~6-9 s + two Godot launches on EVERY battery invocation.
Flag-gated is the cheaper honest landing; the invocation-string updates ride the
same round's bookkeeping.

**I7 — no `seed_digests()` in this move.** 3d's seed-immutability map
(`seed_digests` `:262-268`, `seeds_unchanged` verdict field) is a separate
capability; adding it would introduce a new `verdicts.json` top-level field — schema
change with unknown consumers (the audio-lane r9 precedent). Excluded from this
sketch deliberately; if wanted it is its own declared round.

**I8 — the forced-final-SIGKILL gate ports verbatim or not at all.**
`finally` `:523-526` only SIGKILLs when `witness_verified and same_live_witness()`
— PPID/PGID/starttime/cmdline ownership proven at that instant. Simplifying to an
ungated `os.kill(witness_pid)` reintroduces the PID-reuse hazard the r5 reviewer
removed. `same_live_witness`'s starttime check is the anti-reuse guard; keep it.

**I9 — staging is compatible as-is.** 2d's copy loop (`:119-125`) stages
`timeout_descendant.py` into scratch; `ProjectSettings.globalize_path("res://…")`
resolves identically. The witness writes `timeout-descendant.json` into scratch —
the runner reads it from the same `scratch` var. Single-witness-per-run design: if
the port grows a second spawning arm (the I5 clean-exit arm), delete or rotate the
pidfile between arms; the starttime/cmdline gates still discriminate, but a stale
pidfile is a cheap false-verified.

**I10 — host coupling already proven.** `/usr/bin/python3` exists (→ python3.14);
`OS.create_process` detached-group behavior measured on this exact host (3d
`:486` gate passes every full battery; r61 2d boundary measured descendant orphans
reparented to `systemd --user` pid 1573). Linux-only claim — keep 3d's
`os.name != "posix" or not /proc` typed-error guard.

**I11 — pick the driver; the two candidate drivers produce different records.**
Under `run_process` (`subprocess.run`): timeout → kill+wait, no second drain →
`error="TIMEOUT after 3.0 seconds"`, elapsed ≈ bound (the r61-measured shape).
Under `bounded_run` (`:934-950`): first `communicate` TimeoutExpired → `kill()` →
second `communicate(timeout=3)` **still blocks on held pipes** → a second
TimeoutExpired at `:951` rewrites `error` to `"launch/read/cleanup error: …"` and
can append `"; direct-child cleanup timed out"` (`:957-958`). Both honest, but the
pinned record differs — match the row's expected fields to the chosen driver.
For the *port* (with cleanup) the drain unblocks after witness death, so
`cleanup_exit_code` distinguishes cleanly: `0` under the clean-exit arm (child's
real exit), `-9` under the hold arm (group kill).

**I12 — the port and r62's declared move are complementary only as separate
surfaces.** r62's tracked rows pin: pipe-EOF wait misattributed to liveness, and
*descendants orphan* (no group kill). The port changes the **leak** outcome
(`witness_gone=True` vs orphan under pid 1573) — it cannot change the timeout
verdict, which is decided before cleanup starts. Landed as its own
`--probe-tree-timeout` block, they coexist: r62 documents the seeded path's
semantics, the probe demonstrates the owned-cleanup alternative. Merged into
`run_process`/`bounded_run`, the port would falsify the very expectations r62 is
landing this round. Sequencing: r62 first; the port is a next-round opt-in move,
gated on G2dR62Boundary's scratch measurement of what group-kill changes on the
pipe-holding mutant.

### a.3 Relation to r62's actual declared move this wave

r62 is *not* the port — it formalizes the misattribution as tracked truth. Per
`G2dR62Author.txt`, the landing is a `descendant_pipe_probe.gd`-style fixture +
meta row. Note: **the pipe-holding arm cannot be a CASES row** — every CASES row
must classify True (`:1005`), and this arm necessarily produces `error` set +
`actual_exit=None` → False → battery FAIL. Honest vehicles: a new meta row
(precedent `:539`, zero extra Godot if it re-classifies captured outputs — but this
surface needs live processes, so new launches are required), or new arms inside the
existing `if args.probe_timeout:` block (`:913-1001`) — smallest diff, but the
payload's `bounded_claim` (`:994` "direct child cleanup only") must then be
restated to cover the descendant arms. The discriminating control is free:
`bounded_run` already emits the `timed_out=True, process_was_running=False` pair
that proves misattribution without any new field.

---

## (b) Contested scope between lanes this round

**b.1 — engine-audio seam (carried from w1): structural, no live bind.**
audio r63 is byte-level WAV/SoX predicate work (`act` trigger pinned at
`len>256 && "RIFF"@0 && byte[256]==0x84` per in-flight `r63-scout.md`) — entirely
file-level, inside audio's province. 2d r62 is harness process-semantics
classification; 3d r71 is NavigationAgent3D API semantics. Zero artifact-level
overlap. The audio↔2d engine-audio contest documented in the w1 report stands
unresolved but unbound this wave — no lane is claiming engine-side audio evidence.

**b.2 — two port-diff sketches in one wave (the real coordination point).**
`G2dR62Boundary.txt` explicitly tasks its seat: *"aligned with XConnector's r61
finding"* — measure in scratch what porting 3d's mechanism changes on the pipe-EOF
surface, and *"report receipts + a concrete port-diff sketch"*. That is the same
deliverable as section (a) here, by design: mine is the committed-code static
sketch (this file); theirs is in-lane scratch execution. Complementary, not
duplicative — but the parent should diff the two sketches rather than treat them
as independent discoveries. No file contest: my only write is this wave file;
theirs is `reports/round-62/r62-boundary.md` + `corpus/live/r62-boundary/`.

**b.3 — classification-claim jurisdiction across the sibling runners.**
2d r62's rows pin misattribution for **its own** `run_process`. 3d's runner ships
demonstrably different semantics (`start_new_session` + `killpg` + verified-witness
cleanup). If r62's bounded_claim reads "the harness misattributes timeout to
liveness" unqualified, it overreaches into 3d's lane — where the same fixture shape
is cleaned, not orphaned. The claim must stay lane-local ("this runner's seeded
path"), exactly as 3d's probe claims "one identified witness … not arbitrary
process-tree cleanup". Contested surface = claim scope, not files.

**b.4 — in-flight drift inside the measured sibling (fresh this wave).**
G2dR62Boundary's port measurement cites `game-dev-3d-shokunin/corpus/fixtures/
run_battery.py` — which the r71 author is editing **right now** (+4 CASES lines
staged at ~`:57`, WT sha `b4b31499…` vs HEAD; `probe_tree_timeout` sits at WT:427,
not HEAD:423). Line-cited evidence taken mid-edit can cite post-shift positions
against pre-shift assumptions. Any scratch port test must pin a sha (HEAD
`9458c18` or the WT sha it actually read) — the probe *body* is unchanged, but
receipts claiming file:line provenance drift by 4.

**b.5 — port direction is province-clean.**
3d's PROVINCE.md licenses the direction: "shared fixture patterns are inherited,
2D product surfaces are not" — the port imports a harness *mechanism*, not a 2D
product surface. 2d's PROVINCE.md is silent on harness imports; nothing refused.
The seed.md "ported by analogy … requires this lane's own non-author verification"
rule already governs: the port is evidence only after 2d's own named replay.

---

## (c) Lane-repo write attestation

`git status --porcelain` captured during the scan (before this write):

| repo | observed | attribution |
|---|---|---|
| audio-shokunin | `?? corpus/live/r63-{baseline,boundary,critic,reviewer,scout,simplifier}/`, `?? corpus/live/runs/20261013T2336*-ui-extensible-*` | in-flight r63 leaf scratch — not this seat |
| game-dev-2d-shokunin | `?? corpus/live/r62-{baseline,reviewer,simplifier}/`, `?? reports/round-62/` | in-flight r62 leaf scratch/reports — not this seat |
| game-dev-3d-shokunin | ` M corpus/fixtures/{navagent3d_detour.gd,run_battery.py}`, `?? reports/round-71/` | r71 author's declared tracked edits + leaf reports — not this seat |

This seat's only filesystem write is:
`/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin-train-20261013-w2/x-connector.md`.
No tracked content in any lane repo was created or modified by this seat; no
fixture, runner, CASES row, LOG, SCORECARD, or shared state was touched. (The
3d `M` rows and `??` rows belong to the lanes' own seats and were observed, not
produced, here.)

---

## Recommendation to the parent (one bounded sequence)

1. Let r62 land as declared: pipe-EOF misattribution classification surface via
   fixture + meta row (CASES cannot hold a reject arm — see a.3).
2. Read G2dR62Boundary's scratch verdict against this sketch: if group-kill
   changes the pipe-holding mutant's record as I1/I11 predict (kills the leak,
   not the timeout), the port is a next-round opt-in `--probe-tree-timeout`
   landing per a.1 — with the I5 clean-exit arm added and the I6 flag cost named.
3. If the boundary seat instead shows group-kill *does* alter the timeout record
   (e.g., drain unblocks → different error string), the pinned r62 expectations
   need re-checking against the observed record before adjudication.

## Risks / limits of this scan

- Static + git evidence only; I executed neither battery this round. Runner
  behavior claims cite committed code (`:423-543`, `:913-1001`), committed
  lessons (`r5-identified-witness-timeout.md`), the r61 boundary's measured
  scratch receipts (`tree-probe-verdicts.json` sha `cf328d66…`), and the r62
  frozen-baseline replay — not fresh runs.
- The 3d runner changed under the scan (r71 in-flight +4): HEAD line numbers are
  cited; WT positions are +4 below `:57`. The probe function *body* is unchanged —
  the port sketch is unaffected, but boundary-seat receipts may cite either frame.
- `/proc`-based identity is Linux-only; the ported claim stays host-local, matching
  every existing bound in both lanes.
- The I5 arm is my addition, not 3d's mechanism — it exists because 2d's runner
  proved a case 3d's probe never exercised. If the parent prefers a byte-faithful
  port, the bounded_claim must still be rewritten (the verbatim claim is false on
  this runner).

## Verification

Every claim resolves to a resolvable artifact: 3d `run_battery.py` HEAD positions
(`git show HEAD:` — probe `:423-543`, flag `:558-563`, dispatch `:620-622`,
verdict fold `:692`, payload `:701`), WT sha `b4b31499…` (HEAD 709 lines, WT 713);
2d `run_battery.py` sha `d705bca719fc…` == frozen r62 baseline (`run_process`
`:142-151`, `classify_process` `:153-170`, `bounded_run` `:921-968`, probe block
`:913-1001`, meta precedents `:505`/`:539`, verdict gate `:1005`); fixture shas
`403a2e3e…`/`c3a52834…`/`49948932…`; `reports/round-61/r61-boundary.md` (hold arm
`godot_alive_at_return=false`, elapsed 3.003 s; detach arm clean 0.396 s orphan
ppid 1573); `corpus/lessons/r5-identified-witness-timeout.md` (drain-order fix);
`reports/round-70/r70-author.md` (88/88, `tree_probe_ok=true`); task briefs
`G2dR62{Author,Boundary,Scout,Baseline}.txt`, `G3dR71*.txt`, `AudioR63*.txt`,
`XSentinel.txt` under `.ufo/waves/shokunin-train-20261013-w2/tasks/`; in-flight
`reports/round-63/r63-scout.md` predicate pin.

| godspeed
