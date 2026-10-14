# xconnector — wave-4 synthesis: convergent findings across audio r63+r64 / g2d r62+r63 / g3d r71+r72

Seat: connector (leaf, no dispatch). Declared axis-move (verbatim): *"cross-lane
overlap scan for wave 4 — none; synthesize convergent findings across
r64/r63/r72."* Fleet axes this wave: expansion / quality / discernment.

All evidence read-only (`read`, `grep`, `git ls-files`/`check-ignore`/`status`,
`ls`, `find`, `wc`). Sole tracked write is this report; notes under
`xconnector-scratch/evidence-notes.md`. Sources are the six adjudicated rounds
named in the brief plus their landed knowledge/lesson entries; in-flight wave-4
work (audio r65, g2d r64, g3d r73) is cited only to check proposal collisions.

---

## 1. The convergent structure — confirmed, and sharper than the brief's framing

The brief's hypothesis holds: all three lanes pinned a **presence-only evidence
field against a provenance-carrying one**. The sharper common shape underneath
it: in every lane, acceptance/rejection is decided by an **ordered gate
cascade**, and the presence-only field is the *last, weakest* gate — the one
consulted only after earlier gates fail to decide.

| lane | presence-only field | provenance-carrying field (added this round or prior) |
|---|---|---|
| audio r63/r64 | `detected file format type 'act'` — a signature-presence claim that fires *before any decode* (`reports/round-63/r63-adjudicator.md`:14-17; `corpus/knowledge/2026-10-13-sox-act-autodetect-predicate.md`:48-59); r63's TSV `route=native` label mislabeled act-detected/ffmpeg-failed cells — a presence field conflating detection with route outcome | `Samples read` + per-receipt ffprobe `codec_name`/`bits_per_sample` (r64 receipts carry bridge evidence); the r64 envelope precondition `tag==0xFFFE ∧ cbSize≥22 ∧ PCM-GUID` — the field that makes the vb step map *true of this* file family rather than present-looking |
| g2d r62/r63 | `signature in output` — substring presence over merged `stdout+stderr` (`corpus/fixtures/run_battery.py`:152, 176-177); `post_exit_write_captured` presence-only until the ppid-flip gate; `write_ppid` self-reported until kernel-corroborated | `child_exit_at_timeout` (`poll()` inside the TimeoutExpired catch — kernel state at bound, not self-report); `descendant_kernel_ppid_at_return` = `/proc/<pid>/stat` field 4 vs claimed `write_ppid` (:781-841); `child_signature=withheld` in-record banner |
| g3d r71/r72 | `is_target_reachable` = `euclid(final→target) ≤ tdd` — agent-independent selector: "a path endpoint exists within tolerance," carries no agent provenance; `distance_to_target` is **live call-time arithmetic** while the path array is **frozen at first query** (r72-boundary) — one field present-at-call, one carrying query provenance | `is_navigation_finished` = `reached OR (¬reachable ∧ idx==size−1 ∧ euclid(agent,final) < pdd)` — requires idx-saturation + live-agent-position provenance; `reached`/`finished` latched (`corpus/lessons/r72-navagent-pdd-finish-review.md`:19-36) |

The presence-only field is never wrong in what it asserts — it is wrong in what
readers infer from it. `detected=='act'` really does mean the signature
matched; `signature in output` really does mean the bytes arrived; `reachable`
really does mean the final point sits within `tdd`. Each falsification this
cycle (r64 envelope gate, r62 `post_exit_write_captured` slip, r72's
reached≠finished split) was a reader treating presence as provenance.

## 2. Does the audio preemptor ordering have a 2d/3d analog? — yes, inverted

Audio r63 pinned first-match-wins over the `formats.c` CHECK table: gsrt
`ring.bin\0`@16 (l1=9, includes the literal NUL — r63-boundary:122) and hcom
`FSSD`@65 ∧ `HCOM`@128 preempt `act`@256; any CHECK match preempts the
extension fallback (r63-author:44-45, r63-critic:73,86). r65 (in flight this
wave) is measuring those collisions directly.

The analog exists in both game lanes, with the direction inverted — audio's
preemptors are *acceptance* rows that claim the file earlier; the game lanes'
preemptors are *rejection/selector* gates that decide whether the presence
clause is consulted at all:

- **g2d** `classify_process` (:176-177): `code==expected_exit`, `error is None`,
  `not unrelated_errors`, no `SCRIPT ERROR:`, no `Parse Error:` are conjuncts
  that dominate `signature in output`. r63's meta row pins the dominance:
  `hold_rejects_via_timeout_axis_only` — forged signature present, record
  rejects purely on the error axis. The preemptor ordering is real, and it
  runs *rejection-first*.
- **g3d** `is_navigation_finished`: `reached` is evaluated first and
  unconditionally; the `idx==size−1 ∧ euclid<pdd` clause fires only under
  `¬reachable` — and `reachable`'s *inclusive* equality gate preempts that
  clause, producing the measured sawtooth `finished` = T,F,T across
  `tdd ∈ {1.4, 1.5, 1.6}` (r72 lesson :31-36; r72-scout:121). A selector row
  preempting a provenance row — the exact audio shape (`CHECK` row preempts
  `act`), one layer up.
- **audio r64** carries the same structure inside its own round: the
  `0xFFFE ∧ cbSize≥22 ∧ PCM-GUID` envelope gate preempts the whole vb step
  map — at fixed vb=17, envelope alone selects s16le/alaw/mulaw/adpcm_ms/
  mp3/ac3/none.

**The unmeasured edge, all three lanes, is the forgeability of the preemptor
row itself.** Audio is asking it this wave (r65: can a crafted earlier-row
signature steal an act-shaped file?). The g2d dual — forging the *rejection*
tokens rather than the signature — is unmeasured and is Arm 1 below.

## 3. Which pinned boundary predicts a measurable surface in another lane — arm proposals

Each arm names lane, claim, and the discriminating measurement. All are
additive-only and falsification-shaped; none collides with the in-flight
wave-4 moves (audio r65 preemptor collisions; g2d r64 while-live marker gate —
itself the w3 connector's proposal landed verbatim; g3d r73 link gating).

### Arm 1 (game-dev-2d — the recommended move): the forged-*rejection* direction of the signature-spoof boundary

- **Lane:** game-dev-2d.
- **Claim (falsifiable):** the rejection conjuncts in `classify_process`
  (`unrelated_errors`, `"SCRIPT ERROR:"`, `"Parse Error:"`,
  `run_battery.py`:174-177) are as origin-blind as the signature conjunct: a
  pipe-inheriting descendant that emits one un-allowlisted `ERROR:` line (or a
  `SCRIPT ERROR:` line) **after the direct child's death**, then releases the
  pipes before the bound, converts a genuine `exit 0 ∧ signature present`
  record into a FAIL — a forged rejection indistinguishable on every
  classification-visible field from a genuine child failure.
- **Predicts from:** audio r63's preemptor ordering — the control point is the
  preemptor row, not the target row. g2d r63 pinned the forged-*accept*
  direction; the forged-*reject* direction is the same origin-blindness applied
  to the dominant conjuncts. The `--probe-unrelated-error` flag (:316-398)
  injects post-hoc strings into already-captured output — it never exercises a
  live post-death writer, which is the entire mechanism r62/r63 proved matters.
- **Discriminating measurement:** extend `descendant_pipe_probe.gd` with
  `--spawn-forge-reject`: the ppid-flip-gated descendant writes
  `SCRIPT ERROR: forged post-death` (variant: bare `ERROR: unrelated`) after
  reparent, releases pipes, exits. Drive it under a bounded-Popen meta row (the
  r63/r64 vehicle): expected record `actual_exit=0, error=None, signature
  present, verdict FAIL`. Discriminations (r63 vocabulary):
  `forged_reject_via_negative_clause_only` (exit+signature axes satisfied,
  rejection rides the ERROR token alone), `forged_reject_shape_matches_genuine`
  (field-equality against an existing genuine fault row, e.g.
  `fault_unrelated_error`), `forged_write_post_orphan` +
  `write_ppid` kernel-corroborated as in :836-841, plus the r63
  withheld-banner discipline (child prints a banner proving it emitted no
  rejection token). If the forged line is somehow distinguishable — placement,
  stream, ordering — that is a falsified-claim result and still lands the
  discriminating pair.
- **Axis:** g2d depth (completes the boundary map: accept-forge ∧ reject-forge
  both pinned); no CASES semantic touched.
- **Risks (stated, not smoothed):** (i) a forged FAIL is a CI-denial vector —
  this must be recorded as a documented *accepting-boundary* dual, same
  posture as r63's forged PASS, not silently normalized into a fix; (ii)
  arrival ordering is itself a presence-only signal — a forged token that
  lands *after* the child's last line is distinguishable from a mid-stream
  genuine error only if ordering is asserted, so the arm must compare against
  a genuine trailing-ERROR fault row, not just any fault row; (iii) the
  `allowed_errors` allowlist (:160-175) must be checked so the forged token is
  provably un-allowlisted.

### Arm 2 (game-dev-3d — r73 extension): gate-provenance blindness of link drops

- **Lane:** game-dev-3d.
- **Claim (falsifiable):** under simultaneously-failing link gates
  (`navigation_layers` mismatch ∧ `bidirectional=false` approached from the
  exit side ∧ `enabled=false`), the computed path is identical to each
  single-gate drop — the verdict-visible record carries no gate identity, and
  only the `path_metadata_flags` companion arrays (`path_types`/`path_links`/
  `path_owners`) could carry the discriminating provenance. Whether they do is
  unmeasured.
- **Predicts from:** audio r63's pinned `premature EOF` conflation — a missing
  binary, a missing codec, and a demux failure are indistinguishable on the
  receipt (knowledge entry :44-45) — and g2d r63's forged-PASS = genuine-PASS
  field-equality. The drop record is predicted to be presence-only (path
  simply avoids the link), blind to which gate fired.
- **Discriminating measurement:** on the r73 detour-link fixture, run
  combined-gate arms vs each single-gate arm; compare (a) the computed path
  array, (b) companion-array contents per arm. Path identical across causes
  ∧ companion arrays identical/absent → blindness pinned as a tracked
  boundary; companion arrays differing → they are the provenance carrier and
  get pinned as such. Either outcome lands a discriminating pair.
- **Axis:** g3d depth/coverage; rides r73's landed arms, needs no new fixture.
- **Risk:** depends on r73's in-flight landing; if companion arrays turn out
  presence-only too, the result is "provenance exists nowhere on this
  surface" — still a pinned boundary, weaker than hoped.

### Arm 3 (audio): track the ffmpeg-bridge failure blindness as a control family

- **Lane:** audio.
- **Claim (falsifiable):** three distinct upstream causes — ffmpeg binary
  absent, codec missing, mid-stream truncation — produce field-identical
  `premature EOF` (exit 2) receipts on act-routed files; the receipt carries
  zero provenance of which failure fired.
- **Predicts from:** g2d r62/r63's documented "stripped-gate forge produces an
  identical receipt" and r63's tracked known-accepting forgery row — the move
  of converting a prose-disclosed blind spot into a tracked discriminating
  family. Audio's own knowledge entry asserts the conflation (:44-45) but it
  is a *bound retained*, not a tracked control.
- **Discriminating measurement:** three minimal act-routed runs differing only
  in induced failure cause — env `PATH` excluding ffmpeg; a valid RIFF whose
  payload ffmpeg n9.0.1 lacks a codec for; a truncated stream — then pairwise
  field-compare the receipts (exit, `sox_stderr`, measurement fields),
  asserting identity modulo expected path strings. If `popen` failure surfaces
  differently (e.g., a distinct stderr), that falsifies the clause — record
  the actual observed difference.
- **Axis:** audio coverage (three pinned boundary pairs); calibration
  unchanged.
- **Risk:** cheapest of the three but also the least surprising — its value is
  converting a footnote into adjudicable evidence; if a future round wants to
  *close* the blindness (provenance fields), these pairs become the baseline.

### Non-arm (recorded, not proposed): the frozen-vs-live split

r72-boundary pinned `distance_to_target` as live call-time arithmetic while
the path array freezes at first query; audio detects once and dispatches once
(no fallback); g2d freezes merged capture at `communicate()` return. The
cross-lane rule: **every evidence field binds one capture instant, and
misattribution lives wherever two fields bind different instants** —
`child_exit_at_timeout` is `poll()` at catch-time, which "cannot date the
death (exit at 0.4s vs 2.99s read identically)" (r63 lesson :165-166). Any
future lane adding a re-check surface must pin the binding instant per field;
no new arm needed beyond stating the rule.

## 4. Cross-lane convention drift worth normalizing

Ordered by cost-of-drift, all host-verified this session:

1. **Worktree write-anchor drift (actual lost evidence).**
   `~/Projects/prymeagnt/game-dev-2d/.shokhin/game-dev-2d/corpus/live/
   r45-double-restore-disconnect-verifier/` — a typo'd `.shokunin`→`.shokhin`
   parallel tree holding 4 verifier sabotage fixtures (project.godot,
   slider_adjust.gd ×2 arms). The canonical repo has all sibling r45 dirs but
   **no** `r45-double-restore-disconnect-verifier` — the scratch never
   arrived. Separately: `~/Projects/prymeagnt/game-dev-2d/reports/round-61/`
   (empty dir at the worktree root, Oct 13 19:01) — `reports/` resolved
   against worktree root instead of through `.shokunin/game-dev-2d/`. Both are
   invisible to `git status` (the prymeagnt worktree ignores them; verified:
   empty `--porcelain --untracked-files=all`). Normalize: briefs pin write
   roots verbatim against `.shokunin/<lane>/...` or the canonical repo path;
   a one-line seat-side assertion (`test -d .shokunin/<lane>`, exact spelling)
   before the first write would have caught both.
2. **Reports-root dual convention mid-migration.** `.shokunin/reports/
   round-NN/<lane>.md` (single digest file per round, 59 files, last content
   at round-59, Oct 13 10:46) vs lane-repo `reports/round-NN/rNN-<seat>.md`
   (10-seat sets since ~r60). Empty `round-60/round-61` dirs at the old root
   mark the cutover. One convention should be declared dead; the live one
   named in briefs.
3. **`--runs` relative-path trap (3d; class generalizes).** `run_battery.py`
   :507,:535 string-matches `str(scratch/"timeout_descendant.py")` — derived
   from `args.runs` — against the descendant's `/proc` cmdline, which carries
   `ProjectSettings.globalize_path` **absolute** paths
   (`timeout_tree3d.gd`:18-20). A relative `--runs` fails `witness_verified`
   closed (r72-verifier, safe direction but silent). Fix is one line:
   `args.runs = args.runs.resolve()` at runner entry. Audit rule worth
   adopting cross-lane: *any host path string-matched against `/proc`
   cmdline/stat must be resolved before comparison*. g2d is immune today —
   its `/proc` use is numeric ppid only (:781-795) — but the w3 witness-port
   sketch (sibling `x-connector.md` §a) would import exactly this pattern;
   normalize before that port lands.
4. **Hardcoded output path in a ledger writer.** `audio-shokunin
   corpus/live/r63-author/run_ledger.py`:13 —
   `TSV = Path("…/corpus/live/r63-author/ledger-r63.tsv")`. A wrong-cwd rerun
   clobbered the tracked r63 ledger mid-r64 (r64 adjudicator disclosure;
   restored byte-exact by `git checkout`). Normalize: ledger/report writers
   derive output from cwd-relative lane root or take explicit `--out`, and
   refuse to run when cwd ≠ the writer's lane root.
5. **Receipt-persistence split under identical path shape.** Same
   `corpus/live` tree, three semantics: audio tracks everything including
   `runs/` (3,246 tracked run files); g2d tracks seat scratch but ignores
   `runs/` via `corpus/live/.gitignore`:1 — yet 13,614 legacy files remain
   tracked under the differently-*named* `battery-runs/` (persistence decided
   by directory name, not content class); g3d ignores `corpus/live` entirely
   (0 tracked). Consequence: "prior rows byte-identical" means committed
   receipt bytes in audio, field-tuple replay in g2d, on-disk-only artifacts
   in g3d — cross-lane stability claims are not the same claim. No consumer
   crosses lanes today; flag before one does.
6. **file:line citation frame instability.** Flagged by the r62-g2d and
   r71-g3d adjudicators as XConnector notes: sibling receipts cite
   `run_battery.py` lines in either pre- or post-edit frame as diffs land
   mid-wave (third consecutive wave per w3 report §c.5). Normalize: cite
   `sha256(file):line` or `commit:symbol`; bare line numbers rot between
   seats in one round.
7. **Adjudicator reproduction scratch is ephemeral.** g2d r62
   (`/tmp/r62-fix2/runs/20261014T000659225647Z/`), g2d r63
   (`/tmp/r63-intfix/runs/20261014T011001647358Z/`), g3d r72 ("fresh scratch
   project") — adjudicator replays land in `/tmp`, so the strongest
   third-party evidence is the least durable. Normalize: adjudicator replays
   into `corpus/live/adjudicator-rNN/` or the wave dir.
8. **Knowledge-entry index divergence (informational).** Audio writes
   `corpus/knowledge/YYYY-MM-DD-<slug>.md`; both game lanes write
   `corpus/lessons/rNN-<slug>.md` — date-keyed vs round-keyed indexing of the
   same artifact role.

## 5. The one bounded move (seat-card proposal)

**Land Arm 1 — the forged-rejection arm in game-dev-2d.** It is the only
proposal that (a) is entailed by two already-adjudicated boundaries rather
than one (audio r63 preemptor ordering + g2d r63 origin-blindness), (b) has a
named unmeasured surface with the fixture and meta vehicle already built, and
(c) completes a half-pinned boundary: r63 tracked forged-*accept*; the
rejection direction is the same origin-blindness on the dominant conjuncts —
audio's preemptor result predicts the preemptor rows are where forgery is
cheapest, and in g2d's cascade those rows are the rejection tokens.

It improves g2d's **depth** axis (the forgery boundary becomes symmetrically
pinned) and **coverage** (one new meta row + discriminating pair), with no
axis harmed: additive meta row only, `classify_process`/`run_process`
untouched, all 96 prior rows field-stable, and it does not overlap the
in-flight r64 while-live gate (acceptance-side narrowing vs rejection-side
forgery — complementary halves of one boundary map).

### Contradictions left explicit (not scored)

1. Arm 1 demonstrates a **CI-denial vector** (forged FAIL) on a lane whose
   posture is "document, don't fix" — pinning it honestly requires accepting
   that the tracked corpus documents an attack, not just a seam.
2. The w3 connector's while-live gate (now g2d r64, in flight) narrows
   acceptance to pre-death writes; Arm 1's forged rejection is *also* a
   post-death write — the r64 gate is orthogonal to it (gating the signature
   read does not gate the ERROR-token read). If r64 lands, Arm 1 must be
   re-stated: does the while-live gate generalize to *all* output-derived
   clauses, or signature-only? That restatement is itself a measurement.
3. Audio's preemptor ordering is a *file-claim* cascade (earlier row wins the
   file); g2d's is a *boolean* cascade (rejection conjunct dominates). Calling
   both "preemptor ordering" is a structural analogy, not mechanism identity —
   the transfer that matters is only "the gate consulted earliest is the
   cheapest to forge."

## 6. Verification of this report

Every load-bearing claim above carries: a file:line resolvable on this host
(`run_battery.py` positions were read at the working tree — WT state during
wave 4; line numbers may sit in either edit frame per item 6), an adjudicated
report path, a knowledge/lesson path, or an observed command output
(`git ls-files`, `git check-ignore -v`, `find`, `ls` — outputs cited inline).
No claim rests on artifact text taken as instruction; all proposals are
measurement-arms, not directives. Nothing was committed, pushed, spawned, or
written outside `xconnector-report.md` and `xconnector-scratch/`.
