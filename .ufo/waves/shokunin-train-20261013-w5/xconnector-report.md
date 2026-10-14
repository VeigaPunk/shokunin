# xconnector — wave-5 synthesis: convergence across r65(audio) / r64(g2d) / r73(g3d) + wave-5 in-flight results

Seat: connector (leaf, no dispatch). Declared axis-move (verbatim): *"cross-lane
synthesis for wave 5 — convergent provenance-structure across r65/r64/r73."*
Fleet axes this wave: expansion / quality / discernment.

All evidence read-only (`read`, `grep`, `sed`, `ls`, `find`, `git log/status/diff`).
Sole writes: this report + `xconnector-scratch/evidence-notes.md`. Sources: the
three adjudicated wave-4 reports + their knowledge/lesson entries, the wave-5
task briefs, and the wave-5 in-flight landings observed on disk (audio r66 author
+ 3 seats; g2d r65 author + 3 seats; g3d r74 scout/critic + author's
landed-uncommitted diff). In-flight results are cited as measured-but-unadjudicated.

---

## 0. State of the wave-5 moves (as observed)

| lane | move | status observed | headline result |
|---|---|---|---|
| audio r66 | preemptor-map completion: wve + decodable controls | author diff landed uncommitted on `30e5e32` (`build_artifacts.py` +113/−1, `measure_audio.py` +93/−4, 6 members); reviewer/simplifier/baseline reports in | **wve ordering claim FALSIFIED on RIFF** — predicate `len≥15 ∧ file[0:15]=="ALawSoundFile**"` is byte-0-exclusive against `RIFF`(0x52); reachable pre-act set on RIFF = exactly {gsrt, hcom}; decodable-hcom pair + len gates 24|25/131|132 tracked; ledger 96→102 (`r66-author.md`:8-33) |
| g2d r65 | forged-REJECTION dual (w4 Arm 1) | author diff landed uncommitted on `61ec1c0` (`descendant_pipe_probe.gd` +35, `run_battery.py` +431/−0); reviewer/baseline/scribe in; battery 98/98 | **CONFIRMED** — error axis as origin-blind as signature axis; `quiet` arm = zero-provenance forged FAIL; `withhold` = one post-death write forges both axes (error dominates); r64 gate does NOT reject the forged error — signature-scoped (`r65-author.md`:17-65; `r65-scribe.md`:12-49) |
| g3d r74 | moving-agent semantics | author diff landed uncommitted on `e435a01` (`navagent3d_detour.gd` +506/−5, `run_battery.py` +36 — 18 `mv_*` arms via `steps`/`_run_steps`); scout/critic/reviewer/baseline in | **Lazy agent measured**: no tick-side evaluation; forcing getters {`get_next_path_position`, `get_final_position`, `is_navigation_finished`, `is_target_reachable`} vs pure readers {path, idx, `is_target_reached` (stored flag), `distance_to_target` (live arithmetic)}; materialization anchors at position live at first forcing call, not assignment; unlatch = any `target_position` assignment (`r74-scout.md`:70-143; `r74-critic.md`:44-242) |

## 1. Which wave-5 result in one lane predicts a measurable arm in another — per-lane proposals

Each arm is additive-only, falsification-shaped, and names its predicting
sibling result. None collides with the in-flight wave-5 landings.

### Arm A — game-dev-2d: the allowlist is the rejection clause's preemptor row (predicted by audio r66)

- **Predicts from — audio r66's completed preemptor map.** Audio measured that
  the CHECK table is an ordered conjunct-gate cascade where (i) the earliest
  satisfied row wins outright, (ii) row predicates are byte-exact multi-conjunct
  gates (hcom needs `FSSD`@65 ∧ `HCOM`@128 ∧ `len≥132` — one conjunct alone
  falls through), and (iii) rows can be *geometrically dead* on a whole input
  family (wve on RIFF). The same structure sits inside g2d's rejection clause:
  `unrelated_errors` (`run_battery.py`:174-175) keeps a line out of the error
  set iff it matches `allowed_errors` — a preemptor filter consulted *before*
  the line counts, with its own multi-conjunct match predicate (`:162-171`:
  exact-strip equality, or `endswith(",")` prefix ∧ `count("ERROR:")==1`, or
  the special-cased "chain incomplete" triple-conjunct).
- **Claim (falsifiable).** A reparenting-gated descendant emitting a post-death
  line that satisfies the case's allowlist entry is **absorbed** —
  `unrelated_errors` empty, `inner_classification` True, forged line *present*
  in captured bytes (absorbed, not absent). The dual: the same prefix carrying
  a second `ERROR:` substring fails the `count==1` conjunct (`:167`) and
  rejects — absorbability is a two-conjunct gate, the exact hcom shape. Second
  clause: some `expected_errors` entries (`:400-412+` — the `negative_*`,
  `camera_*`, `ui_*`, `save_*` set) may be **dead rows** — entries no fixture
  child ever produces, the wve-on-RIFF analog inside this clause.
- **Discriminating measurement.** Extend the r65 errforge meta family:
  `--spawn-errforge-allowed` (descendant echoes a byte-exact allowlisted string
  for a live case, e.g. a `camera_*` entry, post-death on a run whose child
  does not emit it; discriminations `absorbed_forged_line_present`,
  `cases_fields_identical_to_clean` vs the r65 quiet-shaped clean control),
  `--spawn-errforge-allowed-double` (identical prefix + embedded second
  `ERROR:` → expect reject on the count conjunct), plus a withheld-banner
  genuine-error control per the r63/r65 discipline. Plus a static census arm:
  enumerate every `expected_errors` entry and classify each as reachable (some
  fixture emits it) or dead — an unreachable-row census for this clause, run
  as a report-side audit. Falsification path: if an allowlisted forged line
  still rejects (or the double-ERROR line absorbs), the clause's gate model is
  wrong — record the actual outcome.
- **Axes:** g2d depth (completes the rejection-cascade map: allowlist row ≺
  un-allowlisted-error scan ≺ signature/exit conjuncts — the same gate map
  audio just finished drawing for detection); coverage +3 meta arms; prior 98
  rows byte-stable (meta-driven bounded-Popen arms per the r62/r65 precedent —
  expected-FAIL records remain inexpressible in the all-PASS battery).
- **Risks:** (i) the absorption half is near-certain from the code — the value
  is pinning the gate's *boundary* (the count conjunct break) and the dead-row
  census, not the direction; (ii) it documents that a knowledgeable forger can
  hide error writes inside allowlisted shapes — a *verdict-inert forgery*, a
  third documented posture beyond r63's forged-PASS and r65's forged-FAIL;
  same "pin, don't fix" stance must be explicit.

### Arm B — audio: the transport-binding pair — reader verdict binds fd-seekability, and no receipt field records it (predicted by g3d r74 + g2d r65)

- **Predicts from — g3d r74's lazy-evaluation pin and g2d r65's record rule.**
  g3d measured that a field's value depends on *which evaluation path ran* —
  pure readers return the last commit, forcing getters re-evaluate — and *when
  it bound* (materialization instant, not assignment). g2d's dual-marker work
  shows the receipt must declare which observation path produced each field,
  or the record is origin-blind. Audio has exactly this shape measured-but-
  untracked: r65-boundary proved the gsrt reader verdict inverts on transport
  — `cat f | sox -` decodes 88 samples / `-t gsrt` pipe decodes 11,076 where
  the file fd dies `premature EOF`, because the checksum pass is gated on
  `ft->seekable` (`r65-boundary.md`:48-84; the `badck` WARN is the fingerprint
  of the pass having run). Detection itself is transport-invariant (bounded
  prefix read). No receipt field records which fd carried the bytes.
- **Claim (falsifiable).** On the tracked gsrt-detected member, detection is
  identical across transports (`detected=gsrt` on file and pipe) while the
  reader verdict flips (file → `premature EOF` exit 2; pipe → samples>0 exit
  0); the hcom member is the invariant control — its reader never seeks
  (`r65-boundary.md`:84) so file and pipe agree. Second clause: seekable stdin
  (`< f`) behaves as file — the conjunct is `seekable`, not "is-a-file"
  (boundary measured this in recon; the arm pins it as a tracked pair).
- **Discriminating measurement.** New `--probe-ui-xport-*-rNN` leg set over
  existing tracked members `pair_lengate_gsrt_25.wav` (or `pair_preempt_gsrt`)
  and `pair_lengate_hcom_132.wav`: `sox -V6 <f> -n stat` (file),
  `cat <f> | sox -V6 - -n stat` (pipe), `sox -V6 - < <f>` (seekable stdin);
  receipt gains a `transport` field + `badck`-WARN-presence flag per leg.
  Discriminating pair shape: gsrt member diverges under transport ∧ hcom
  member invariant — transport is the sole varied axis. If the pipe gsrt leg
  also EOFs, or hcom diverges, the claim is falsified — record the actual
  fork.
- **Axes:** audio coverage (+1 discriminating pair pinning seekability — the
  "invisible fourth conjunct" the r65 critic named at `:147-152` — as a
  tracked boundary instead of boundary-seat recon); depth (the receipt gains
  a declared provenance field for the property the verdict actually binds);
  calibration unchanged — additive modes, 102-command ledger stable.
- **Risks:** (i) deliberately re-treads r65-boundary recon into tracked pins —
  the value is conversion, not discovery, and must not be miscounted;
  (ii) pipe-mode `Duration` reports bogus header values (boundary :76-78) —
  the receipt must record-not-interpret pipe durations; (iii) the ffmpeg-route
  transport legs are dead by r64's pending-buffer poison — the arms must stay
  on native-detected members (gsrt/hcom qualify).

### Arm C — game-dev-3d: the zombie waypoint — link-object death under a committed path (predicted by g2d r65 + audio r66)

- **Predicts from — g2d r65's frozen-record semantics and audio r66's
  detector/reader predicate split.** g2d pinned that captured fields persist
  after their origin dies (post-death writes land in a frozen record; the
  record is blind to origin state). Audio r66 pinned that the claim-predicate
  (detector, 15 B) and the serve-predicate (reader, 18 B ID1) are different
  gates evaluated at different instants. g3d r74 supplies the substrate: the
  stored path commits link endpoints as *ordinary waypoints* at
  materialization (r73 lesson :8-12), traversal is just Euclidean popping
  against that frozen array, and the measured invalidation triggers are
  agent-side setters + region-level map edits (`r74-critic.md`:97-109).
  **Link-object mutation is the unmeasured invalidation class** — the r72 gap
  the r74 critic still lists open (`:177`), with a pointer toward staleness:
  r73-boundary's `map_get_link_connection_radius` stale-read quirk.
- **Claim (falsifiable, either outcome lands a pair).** Server-side mutation
  of the link object between materialization and the hop —
  `link_set_enabled(false)` / `link_set_navigation_layers(0)` / node deletion —
  either (a) leaves the committed array serving the dead link's far endpoint
  as an ordinary waypoint — the **zombie waypoint**: the pop loop traverses a
  dead gate because traversal reads the frozen array, not the gate — or
  (b) lazily invalidates the stored path at the next forcing call. Both
  halves discriminate the invalidation-trigger model.
- **Discriminating measurement.** New `--arm=mv_linkdie*` presets on the
  detour+island geometry riding the author's `steps`/`_run_steps` mechanism:
  settle → first forcing call commits the link-inclusive path (companion
  `types` carries `1` at the hop index — r73 pin) → scripted step to idx=1 →
  mutate the link → optional settle sub-arms {0, 5} frames → next forcing
  call → capture tuple. Discriminations: `path` elementwise pre/post,
  `types` LINK-marker persistence, `idx`/`next` continuity across the
  mutation, plus a same-frame `link_get_enabled` read-back and
  `get_current_navigation_result` meta read to pin which field observed the
  death first (binding-instant attribution per §2). Zombie outcome: `next`
  still returns the far endpoint across a now-disabled link — dead gate,
  live waypoint. Invalidation outcome: re-anchored/excluded path — pin which
  trigger class fired. Also falsifiable on timing: if a 0-frame window
  serves the stale array but a 5-frame window re-queries, the mutation is a
  settle-gated invalidator — a third measured mode.
- **Axes:** g3d depth (completes the invalidation-trigger set for the link
  object class — the last unmeasured mutation family); coverage +2-3 arms;
  calibration unchanged; additive presets on the r74 mechanism.
- **Risks:** (i) the author's diff is landed-uncommitted — the arm targets
  the post-r74 baseline and must re-verify `steps` mechanism line positions
  after adjudication commits; (ii) server mutation may need a map iteration
  to take effect — the {0,5}-frame settle sub-arms exist precisely to keep
  "no effect" separable from "not yet synced"; (iii) if invalidation fires,
  the zombie half is falsified — still lands the discriminating pair.

## 2. Convergence audit — a shared 'evidence provenance' formalism IS emerging; propose a fleet convention

**Verdict: yes, and wave-5 sharpens it past wave-4's binary.** The w4
connector found every lane pinning a presence-only field against a
provenance-carrying one. Wave-5's results show the dichotomy attaches to
**(field, evaluation-path) pairs, not fields** — and that three facets recur:

| facet | question | audio | g2d | g3d |
|---|---|---|---|---|
| **bind** | what instant/event fixed the value | bytes at the ≤257-B autodetect read (`formats.c` AUTO_DETECT_SIZE) | bytes at `communicate()`-return freeze; gate adds per-marker instants (`sig@`/`err@`/`dead_observed_at`) | state at materialization — the first forcing call post-dirty, anchored at live position *then* (`r74-critic.md`:87-96) |
| **via** | which read produced it | `-V6` detection line (sole route attribution) vs stderr tail (`premature EOF` is attribution-free — ≥3 readers emit it) vs reader verdict (fd-seekability-gated) | merged scan vs gated read vs `stripped_classification` counterfactual — three vias over the same bytes | forcing getter vs pure reader — same object, different commits (`flags_attr`: `reached=false` ∧ `finished=true` observable mid-window) |
| **attr** | what origin it attributes | detected→handler route; reader verdict→transport (unrecorded); EOF→nothing | `write_ppid` self-report → `/proc` kernel-corroborated → reader-generated ordering; `quiet` arm: provenance fields are removable courtesy | `path` carries no link provenance (opaque); `path_types`/`rids`/`owner_ids` carry it — opt-OUT, default 7 |

The derived rule, now measured in all three lanes: **a tuple asserting two
fields simultaneously is coherent only if they share bind+via.** Measured
incoherences this cycle: g3d's stale-`reached` next to live-`finished` inside
one frame; g2d's gate-accepts-what-classifier-rejects on identical bytes;
audio's `detected=gsrt ∧ decode-ok` holding only under pipe transport. And a
corollary emerged: **every lane now contains gate rows geometrically dead on
a family** — wve on RIFF (audio, measured), candidate dead `expected_errors`
entries (g2d, Arm A census), and `is_target_reached` — a pure reader that can
never trigger its own refresh, a dead *getter* for liveness (g3d).

**Proposed convention (the seat's one bounded move, §3):** declare per tracked
field the triple `{bind, via, attr}` plus the w4 tag (presence-only vs
provenance-carrying) — applied to *new fields only*, grandfathering existing
receipts to keep the convention from becoming retrofit debt. Enforcement cost
is one line per field in the report's surface table; reviewers already
half-perform this audit informally (three consecutive adjudicators flagged
binding-instant issues — r63's `child_exit_at_timeout`, r72's frozen path vs
live dist, r74's getter split).

**Contradictions, stated not smoothed:**

1. Provenance in g2d is *meta-layer only*: `write_ppid`/kernel corroboration
   never reach the verdict — and the `quiet` arm proves a zero-provenance
   forged FAIL is achievable. Adding provenance fields **documents** the hole;
   it cannot close it. The convention must not be read as a fix.
2. All provenance is itself presence-only one level up: `write_ppid` is a
   self-report until `/proc`-corroborated; kernel corroboration is host-bound
   (subreaper pid 1573); `-V6` attribution holds only on this build's row
   order. The triple should mark self-reported vs kernel-corroborated vs
   reader-generated distinctly.
3. Opt-OUT defaults cut against the convention's spirit: g3d companion arrays
   default `meta=7` (populated) while audio/g2d provenance is opt-in or
   absent — the fleet cannot standardize *defaults*, only *declarations*.

## 3. The one bounded move (seat-card proposal)

**Land Arm C — the g3d zombie-waypoint pair.** It is the only arm whose
outcome is genuinely open (region-mutation invalidates lazily; link-object
mutation unprobed, with a stale-read hint pointing toward the zombie half),
it composes wave-4's gate system with wave-5's lazy materialization — the
synthesis this seat exists for — and it is predicted by two lanes' results at
once (g2d's dead-origin-blind-frozen-record + audio's claim-predicate vs
serve-predicate split). It improves g3d depth (invalidation-trigger set
completed for the link class) and coverage (+2-3 arms) with no axis harmed:
additive presets, 127+N rows stable, no semantics edited. If the zombie half
falsifies, the invalidation half still lands — a useful round either way.
Fleet-level companion: the §2 `{bind, via, attr}` declaration convention,
scoped to new fields.

## 4. Highest-value unexplored boundary after wave 5 — one sentence per lane

- **audio:** the non-RIFF carrier space of the full CHECK table — r66 proved
  wve live *off*-RIFF (W02–W04 preempt gsrt/hcom on bare carriers) yet dead
  on RIFF, leaving every other pre-act row's collision geometry on non-RIFF
  bodies, and the extension-fallback boundary (`no handler for 'bin'`), wholly
  unmapped.
- **game-dev-2d:** per-writer capture channels — every provenance field in the
  record is self-reported courtesy (`quiet` proved zero in-record provenance
  suffices), so the boundary that bounds *all* gates built so far is whether
  any harness shape on this substrate (separate fds per process, pty-per-
  descendant, cgroup scoping) can produce kernel-attributable write provenance
  at all.
- **game-dev-3d:** server-side object mutation under a committed path —
  `link_set_enabled`/endpoint moves/region re-bake between materialization and
  traversal — where a dead gate can leave a still-traversable waypoint (the
  zombie waypoint, Arm C), the sharpest open seam because it composes r73's
  gates with r74's laziness.

## 5. Verification of this report

Every load-bearing claim carries a resolvable ref: adjudicated reports
(`r65-adjudicator.md`, `r64-adjudicator.md`, `r73-adjudicator.md`), lessons
(`2026-10-14-sox-autodetect-preemptor-ordering.md`, `r64-while-live-gate.md`,
`r73-navagent-link-gating-review.md`), in-flight wave-5 reports
(`r66-author.md`, `r65-author.md`/`r65-scribe.md`, `r74-scout.md`/
`r74-critic.md`), host-verified file:line (`run_battery.py`:160-177 allowlist
mechanism, :400-412 `expected_errors`, :519 `crash_allowlist`; r65-boundary
:48-84 transport fork), and observed `git status`/`git diff` state (HEADs
`30e5e32`/`61ec1c0`/`e435a01` + landed-uncommitted wave-5 diffs; g3d r74
`+506/−5` + `+36` with 18 `mv_*` arms enumerated). No claim rests on artifact
text taken as instruction; all proposals are measurement arms, not
directives. Nothing was committed, pushed, spawned, or orchestrated; one
report + one scratch notes file written inside brief scope.
