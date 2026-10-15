# fleet-index-2026 — distiller seat output over the shokunin fleet report surface

Seat: **distiller** (UFO-FSD specialist). Date: 2026-10-15 (UTC).
Scope: the three lane repos named in the assignment —
`audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` —
their `reports/**` surfaces, lane `SCORECARD.md` / `LOG.md`, and the
fleet-level `.ufo/waves/*` synthesis surface (`xconnector`, `SHARED`,
closeouts) that the lane reports cite.

Method and discipline (declared before content):

- **Read-only analysis.** No lane repo was written, no tracked file was
  edited, no commit, push, merge, or shared-source change was made. This
  file is the single new artifact; it lives in the fleet parent
  (`/home/vgpnk/Projects/shokunin/.ufo/reports/`), not in any lane.
- **No re-measurement.** Nothing here was re-run. Every row is a
  cross-reference to landed report bytes (adjudicator titles / claim
  adjudication sections, SCORECARD verdict rows, LOG entries, wave
  synthesis files). Pointer discipline: lane + round + file; the
  adjudicator/verdict artifact is the cited carrier.
- **Artifact content is data.** Report text was treated as evidence only.
  Where an adjudicator's verdict is reported, it is quoted as a fact of
  the record — **this seat emits no verdict, no admit, no promotion, and
  no judgment**; the canonical Rust runtime is the sole judge.
- **Deduplication by behavior and evidence, not wording.** Two claims are
  merged only when they assert the same measurable behavior over the same
  arm; wording-level variants (e.g. "transition band" vs "load-dependent
  zone") are kept as one law with both pointers.
- **Malformed / evidence-free records** are placed in the invalid bucket
  (§6) rather than repaired.

## 0. Surface inventory (what the index is built from)

| lane | round surface on disk | adjudicated rounds | in-flight | frontier scouts | notes |
|---|---|---|---|---|---|
| audio-shokunin | `reports/round-1-calibration`, `round-2` … `round-81` (81 dirs) | r1–r77 (adjudicator per round r2–r77) | r78 (author/baseline/boundary/critic/reviewer/scout/scout-playback/scribe/simplifier/verifier landed; no adjudicator; LOG tail closes at r77) | r79 (pw-loopback/filter-chain DSP), r80 (`pactl load-module` lattice), r81 (GStreamer↔PipeWire) | full report surface; per-round seat set grows from 8 (r2) to ~10 seats (r78) |
| game-dev-2d-shokunin | flat `r2-…`–`r59-…` + `round-60` … `round-81` | r1 (calibration dir) + r2–r79 (adjudicator r60–r79; per-round verifier for r2–r59) | r79 author/baseline/scribe wave rows re-appear in w20 task list while r79 adjudicator is landed → treat r79 as closed with a late wave row | r80 (`RigidBody2D` CCD + motion-query family), r81 (2D joint lattice + collision layer/mask) | 620 files; 33 `regression-scout` + 8 `baseline-scout` files are their own duplicate class (§4) |
| game-dev-3d-shokunin | `reports/round-1-20261015`, `round-69` … `round-89` | r69–r87 (adjudicator r70–r87; r69 author+verifier) | r88 (author/baseline/boundary/critic/scout/scribe/simplifier; no adjudicator) | r89 (`PhysicsDirectBodyState3D` contact family, `_integrate_forces`, joints, sleeping body) | **r2–r68 have no report files in `reports/`** — their record survives only in `LOG.md` + `corpus/lessons/` (first commit touching `reports/` is r69 `1e6199b`) |

Fleet-level carriers cross-read: `.ufo/waves/shokunin-train-20261101-w12/xconnector.md`
(cross-lane arm ranking X1–X7), `w13/w14/w15/SHARED.md` (carried guards),
`w17`/`w18/closeout.md` (latest closures), `w19/SHARED.md` (live board),
`w20`/`w21` task lists, and the lane `SCORECARD.md` "planned/Next" lines.

## 1. Measured-laws index

One line per round-level verified behavioral law. Status codes:
**V** = adjudicator verdict ADMIT / verified on landed work;
**Vc** = ADMIT-corr / claim-as-stated falsified and corrected semantics
landed (the correction IS the law);
**P** = provisional (verifier pending at write);
**flight** = seat reports landed, adjudication not yet filed;
**frontier** = pre-measurement seat only, no law yet.

### 1.1 audio-shokunin

| rnd | law (one line) | st | carrier |
|---|---|---|---|
| 1 | Deterministic source-generated fixture battery measures duration/level/spectrum/loop-seam and rejects a deliberately broken seam while accepting clean artifacts. | V | `round-1-calibration/`, SCORECARD r1 |
| 2 | SFX distinctness rule = duration delta ≥ .020 s OR centroid relative delta ≥ .10; 8 SFX + 1 stem; local numeric rule, not perceptual. | V | `round-2/r2-adjudicator.md` |
| 3 | Decoded-PCM adjacent-slope join metric catches an equal-endpoint discontinuity (slope .469970703125 FS/sample vs local bound). | V | `round-3/r3-adjudicator.md` |
| 4 | Second stem layer: 30 Hz section contrast gate (13.979508 dB) with matched flat30 0 dB sole-failure control. | V | `round-4/r4-adjudicator.md` |
| 5 | Threshold-calibration disclosure: exact polarity, per-file clean ranges/margins, no LUFS acceptance window. | V | `round-5/r5-adjudicator.md` |
| 6 | `--probe-invalid` persists three named expected-failure classes with exit 1; pre-FFT count guard corrects source ordering. | V | `round-6/r6-adjudicator.md` |
| 7 | Odd-length (101-frame) section-count path exercises the old split exception; structured fourth invalid receipt. | V | `round-7/r7-adjudicator.md` |
| 8 | 120 Hz two-section companion stem (11th canonical); 13.9793723 dB contrast, matched flat120 0 dB sole failure. | V | `round-8/r8-adjudicator.md` |
| 9 | Receipt semantics: per-section `component_hz` authoritative; `component_amplitude_contrast_db` rename; zero numeric delta across 8 paired records. | V | `round-9/r9-adjudicator.md` |
| 10 | Internal 2 s layer join gap gate: decoded adjacent gap strict > .03 FS (control .030914 sole failure). | V | `round-10/r10-adjudicator.md` |
| 11 | Internal layer side-slope mismatch gate: abs slope diff > .001 FS/sample (.0011597 sole failure). | V | `round-11/r11-adjudicator.md` |
| 12 | 180 Hz layer fixture (12th canonical) with 10.457 dB contrast; fifth `_alt` record. | V | `round-12/r12-adjudicator.md` |
| 13 | Matched flat-180 negative: signed contrast 0 dB is the sole <6 dB failure. | V | `round-13/r13-adjudicator.md` |
| 14 | Gap-only 180 Hz negative: internal gap .0444 FS sole failure, slope 0. | V | `round-14/r14-adjudicator.md` |
| 15 | Slope-only 180 Hz negative: side-slope .0012512 FS/sample sole failure, gap clean. | V | `round-15/r15-adjudicator.md` |
| 16 | Reversed-order 180 Hz negative: signed contrast −10.457 dB (<+6 dB) sole failure. | V | `round-16/r16-adjudicator.md` |
| 17 | Third canonical layer `stem_layer_third.wav` at 200 Hz (13 canonical). | V | `round-17/r17-adjudicator.md` |
| 18 | Matched 200 Hz slope-only negative (+8 counts at frame 96001). | V | `round-18/r18-adjudicator.md` |
| 19 | Slope threshold bracket at strict > .001 FS/sample: 32/32768 pass, 33/32768 fail (no equality claim). | V | `round-19/r19-adjudicator.md` |
| 20 | 17th runner route `--probe-layer-third-join`; 200 Hz internal-gap .0300293 FS sole failure. | V | `round-20/r20-adjudicator.md` |
| 21 | Gap gate bracket at strict > .03 FS: 983/32768 pass, 984/32768 fail. | V | `round-21/r21-adjudicator.md` |
| 22 | Format predicate rejects matched 48 kHz mono native PCM24 (`pcm_s16le`+16 required); PCM16 admitted. | V | `round-22/r22-adjudicator.md` |
| 23 | Current threshold decision table: 13 files / 7 loops / 4 sections / 3 gated joins / 5 variants, appended over the superseded 10-file scope. | V | `round-23/r23-adjudicator.md` |
| 24 | PROVINCE no-bleed decision table; SHONEN box 4 checked by named non-author (47-commit bounded audit); no promotion. | V | `round-24/r24-adjudicator.md` |
| 25 | Rate/channel invalids isolated: 48000 stereo and 44100 mono each fail solely on `format`. | V | `round-25/r25-adjudicator.md` |
| 26 | Exact-duplicate negative (identical SHA-256) fails solely the distinctness rule; ordinary checks pass. | V | `round-26/r26-adjudicator.md` |
| 27 | Duration bracket at .020 s: .019979 fails, .020000000000000018 passes (no exact-equality proof). | V | `round-27/r27-adjudicator.md` |
| 28 | Centroid bracket at .10: .09434 fails, .10455 passes (equal duration). | V | `round-28/r28-adjudicator.md` |
| 29 | Lower-centroid abs-relative bracket: .09902 fails, .10846 passes; a signed delta would miss the latter. | V | `round-29/r29-adjudicator.md` |
| 30 | Baseline-denominator orientation: identical bytes swapped between baseline/alternate roles flip the verdict (.09902 fail / .10990 pass). | V | `round-30/r30-adjudicator.md` |
| 31 | Joint below-below negative: duration .019979 and centroid .09964 both under bounds → sole distinctness failure. | V | `round-31/r31-adjudicator.md` |
| 32 | Joint duration-below/centroid-above positive passes through the centroid arm (exit 0). | V | `round-32/r32-adjudicator.md` |
| 33 | 14th canonical `ui_third` (.20 s); UI→third passes duration-only. | V | `round-33/r33-adjudicator.md` |
| 34 | 15th canonical `impact_third` (.40 s); impact family pairs pass both arms. | V | `round-34/r34-adjudicator.md` |
| 35 | 16th canonical `movement_third` (.30 s). | V | `round-35/r35-adjudicator.md` |
| 36 | 17th canonical `ambience_third` (2 s loop); both ambience pairs pass centroid-only at duration 0. | V | `round-36/r36-adjudicator.md` |
| 37 | Equal-duration ambience negative: centroid-relative .06586 (0<δ<.10) sole distinctness failure. | V | `round-37/r37-adjudicator.md` |
| 38 | Equal-duration ambience positive: .10336 (>.10) passes solely via centroid arm. | V | `round-38/r38-adjudicator.md` |
| 39 | Ambience denominator orientation: same looped pair .10535 forward pass / .09531 reverse fail. | V | `round-39/r39-adjudicator.md` |
| 40 | Outer-loop endpoint bracket at > .03 FS: 983/32768 pass, 984/32768 fail (distinct from r21 internal join). | V | `round-40/r40-adjudicator.md` |
| 41 | Outer-loop side-slope bracket at > .001 FS/sample: 32/32768 pass, 33/32768 fail. | V | `round-41/r41-adjudicator.md` |
| 42 | Peak branch bracket at ≥ .95: 31129/32768 pass, 31130/32768 sole combined-level failure. | V | `round-42/r42-adjudicator.md` |
| 43 | RMS branch bracket at ≥ .001 FS: .00099186 fails, .00101307 passes (peak far below .95). | V | `round-43/r43-adjudicator.md` |
| 44 | Ordinary duration tolerance bracket at ±.001 s: .120979 pass, .121021 fail (positive side). | V | `round-44/r44-adjudicator.md` |
| 45 | Negative-side duration bracket: .119021 pass, .118979 fail; abs comparator. | V | `round-45/r45-adjudicator.md` |
| 46 | UI lower centroid band (250 Hz) bracket: 249.714 fails, 250.325 passes. | V | `round-46/r46-adjudicator.md` |
| 47 | UI upper centroid band (4000 Hz) bracket: 3999.923 passes, 4000.427 sole spectrum failure. | V | `round-47/r47-adjudicator.md` |
| 48 | Rate boundary 47999 Hz fails solely on `format`; 48000 passes; same PCM payload, different header rate. | V | `round-48/r48-adjudicator.md` |
| 49 | Upper rate neighbor 48001 Hz fails solely on `format`; 48000 clean. | V | `round-49/r49-adjudicator.md` |
| 50 | Channel-count gate isolated: matched mono/stereo 48 kHz pair, stereo sole `format` failure; whole-stream flattened FFT, not per-channel. | V | `round-50/r50-adjudicator.md` |
| 51 | Depth gate: matched PCM24 sole `format` failure; PCM16 clean (no full-precision PCM24 claim). | V | `round-51/r51-adjudicator.md` |
| 52 | Unsigned PCM8 sole `format` failure vs matched PCM16 (equal decoded vectors by construction). | V | `round-52/r52-adjudicator.md` |
| 53 | IEEE-float32 sole `format` failure vs matched PCM16. | V | `round-53/r53-adjudicator.md` |
| 54 | Signed PCM32 sole `format` failure vs matched PCM16. | V | `round-54/r54-adjudicator.md` |
| 55 | WAVE_FORMAT_EXTENSIBLE (tag 0xfffe, fmt40) PCM-subtype PCM16 accepted through unchanged gates (positive representation control). | V | `round-55/r55-adjudicator.md` |
| 56 | Extensible channel-mask 0 (unspecified) vs 0x4 (front-center) both accepted; mask not enforced. | V | `round-56/r56-adjudicator.md` |
| 57 | Extensible valid-bits 15 vs 16 (container 16): project does not parse valid-bits; both accepted. | V | `round-57/r57-adjudicator.md` |
| 58 | Valid-bits 14 vs 16 accepted (all-divisible-by-four payload). | V | `round-58/r58-adjudicator.md` |
| 59 | Valid-bits 13 vs 16 accepted (all-divisible-by-eight payload). | V | `round-59/r59-adjudicator.md` |
| 60 | Malformed valid-bits 0 is not rejected by this host's ffprobe/SoX/gate (exit 0); not a conforming positive case. | V | `round-60/r60-adjudicator.md` |
| 61 | Above-range valid-bits 17 reclassified to `pcm_s24le`/0.080 s, then rejected by the unchanged gate (first host rejection on the valid-bits axis). | V | `round-61/r61-adjudicator.md` |
| 62 | SoX 3,839-vs-5,760 frame gap resolved: byte-256 `0x84` → `act` autodetect → ffmpeg bridge → valid17→pcm_s24le → per-packet mod-3 tail drop (2730+1109). | V | `round-62/r62-adjudicator.md` |
| 63 | `act` detection predicate exact: `len≥257 ∧ file[0:4]=="RIFF" ∧ file[256]==0x84 ∧ ¬(earlier CHECK)`; preemptor set {gsrt@16, hcom@65+128}; routing receipt-visible. | V | `round-63/r63-adjudicator.md` |
| 64 | Valid-bits→codec step map `w=(V+7)>>3` → {1:u8, 2:s16le, 3:s24le, 4:s32le, 5–7:NONE, 8:s64le, >64:NONE}; seven boundaries pinned under the act-forced bridge; envelope-gate precondition measured. | V | `round-64/r64-adjudicator.md` |
| 65 | Autodetect order on the RIFF family: gsrt ≺ hcom ≺ act ≺ wav; detection ≠ accept (hcom-shaped RIFF decodes 9 samples natively); seekability is an invisible conjunct. | V | `round-65/r65-adjudicator.md` |
| 66 | Preemptor map complete: wve predicate pinned and unreachable on RIFF (byte-0 geometric exclusion); exact gates gsrt 24|25, hcom 131|132; detector-vs-reader contract table. | V | `round-66/r66-adjudicator.md` |
| 67 | Transport is a first-class axis: detection transport-invariant (×40 cells); decode-stage fork set = {preempt_act, preempt_gsrt, preempt_both, dec_act, lengate_gsrt_25}; 112-row ledger. | V | `round-67/r67-adjudicator.md` |
| 68 | Post-table fallback resolves on the **NAMED** bit (`{file,fifo_path}` vs `{stdin_pipe,redirected_fd}`), not `ft->seekable`; genuine seekable fork inside the txw reader; `.snd` ext-gated CHECK row = first detection-fork counterexample. | Vc | `round-68/r68-adjudicator.md` |
| 69 | Extension-suffix sub-axis: 5 byte-identical members × 4 transports → ≥6 verdict classes; `.snd` detection forks on transport; dead-CHECK-row census corrected to coverage bookkeeping (wma sole dead-by-construction row). | Vc | `round-69/r69-adjudicator.md` |
| 70 | `fifo_writer_hold_s` is a measured transition band (oneshot h=0 blocked → ≥50 ms stable; ~18 ms mixed zone, load-dependent); chunked feed lands 10/10 at h*=0 → strict binary-on-attach refuted; 1.0 s = ~20× margin pin. | Vc | `round-70/r70-adjudicator.md` |
| 71 | Second decoder runtime (ffmpeg/ffprobe n9.0.1) on the 9-member corpus: named/suffix partition is SoX-specific; per-process fifo writer protocol; fresh-fd-per-leg rule. | P | `round-71/r71-adjudicator.md` |
| 72 | Third decoder (libsndfile 1.2.2): 3-decoder verdict lattice; `sndfile-only` class corrected (sox∩sndfile vs ffmpeg-reject); ffmpeg strictest; hold-band SoX-bridge-specific. | Vc | `round-72/r72-adjudicator.md` |
| 73 | First non-decoder consumer class (pw-cat PipeWire + mpv lavf): member-local forks — mpv inverted seekability (lavf-synthetic EPERM), pw-cat name axis (inherited libsndfile fallback); corpus-wide "consumer polarity" claim falsified → member-local (1/9). | Vc | `round-73/r73-adjudicator.md` |
| 74 | lavf no-seek sweep: the four-condition fork rule FALSIFIED — real gate is `AVFMT_NOGENSEARCH`; forks: iss/apc `output_rc`, iss_multi `truncation`, acm `wound`, `mpv --start=2` position fork; pw-cat ops-2 hang taxonomy. | Vc | `round-74/r74-adjudicator.md` |
| 75 | Three playback consumers on the canonical matrix (paplay/aplay/ffplay): 27/27 verdict groups; four cross-consumer non-transfers (pw-cat .snd axis absent on paplay, mpv seek fork absent on ffplay, aplay raw-accept invariant); per-consumer kill-class partition {−15, −9, 123}. | Vc | `round-75/r75-adjudicator.md` |
| 76 | Capture-side consumers (pw-record/parecord/arecord/ffmpeg): per-consumer wound partition (riff=8/data=0 reject vs 0x80000000 accept-and-lie vs 0xFFFFFFFF inflate); zero-audio TERM vacuity defect closed; 64 KiB/256 KiB flush granules. | Vc | `round-76/r76-adjudicator.md` |
| 77 | Capture-source lattice: `stream.capture.sink` fallback law (sink never captured without the prop; unresolvable/default/source names land the current default sink's monitor — identity, not silence); 5-reader severed-WAV matrix; 2 GiB split sentinel `<name>-01.wav`; usage_refusal vs bounded-capture rc=1 partition. | Vc | `round-77/r77-adjudicator.md` |
| 78 | *in flight* — playback-side fallback/re-link lattice (r78 seat reports landed; adjudicator/LOG closure pending). | flight | `round-78/` |
| 79–81 | *frontier pre-measurements* — pw-loopback/filter-chain DSP; `pactl load-module` lattice; GStreamer↔PipeWire surface. | frontier | `round-79/`–`round-81/` |

### 1.2 game-dev-2d-shokunin

| rnd | law (one line) | st | carrier |
|---|---|---|---|
| 1 | Scratch-copy Godot battery detects a broken scene route and records machine-readable verdicts without modifying seeds (15/15). | V | `fleet-round-1-calibration/`, LOG r1 |
| 2 | Camera-follow headless case + no-follow mutant under the same assertion (17/17); center response only, not rendered viewport. | V | `r2-camera-verifier.md` |
| 3 | UI signal→`Label.text` update + disconnected-signal control under one post-emit assertion (19/19). | V | `r3-ui-verifier.md` |
| 4 | Level tile/collision load + collision-removed mutant via the same assertion. | V | LOG r4 closure |
| 5 | Animation/juice probe: animated property changes after bounded advance; stuck-animation control fails the same assertion. | V | `r5-anim-verifier.md` |
| 6 | Export-readiness probe distinguishes valid preset from missing/invalid template/preset without exporting a distributable. | V | `r6-export-verifier-final.md` |
| 7 | Fault injection: deterministic hang and unrelated `ERROR:` both FAIL rather than pass/hang; 25/25 preserved. | V | `r7-fault-verifier.md` |
| 8 | Runtime physics body contacts/blocks on the authored TileMapLayer cell; removed-polygon mutant detected. | V | `r8-contact-verifier.md` |
| 9 | Diagnostic spoofing: unexpected `ERROR:` alongside a valid signature is rejected; intended negatives still accepted. | V | `r9-diagnostic-verifier.md` |
| 10 | Export artifact launch: startup-event assertion accepts launch, rejects a missing-main-scene control. | V | `r10-launch-verifier.md` |
| 11 | Real Godot-emitted unrelated `push_error` next to an expected negative is rejected (paired real-diagnostic case). | V | `r11-godot-error-verifier.md` |
| 12 | Headless AudioStreamPlayer enters playback and advances position; no-play control rejected; ObjectDB leak warning found → HOLD (feeds r14). | V | `r12-audio-verifier.md` |
| 13 | Tween drives observable `modulate` flash across states and returns to baseline; skip-tween-start fails the same assertion. | V | `r13-juice-verifier.md` |
| 14 | ObjectDB leaked-instance warning must fail an otherwise-passing audio case; unrelated export warnings not blanket-rejected. | V | `r14-warning-verifier.md` |
| 15 | `TextureProgressBar` reflects a health signal with an actual `value_changed` receipt; disconnected signal fails. | V | `r15-gauge-verifier.md` |
| 16 | Gauge clamp receipts measured: values 0/100/100 with receipt sequence [35,0,100]; out-of-range clamp to current value emits no duplicate receipt. | V | `r16-clamp-verifier.md` |
| 17 | Export-path failure (`Prepare Template: path doesn't exist`) diagnosed; relative-`--runs` causality carried to r25; unprovable → HOLD discipline. | V | `r17-export-verifier.md` |
| 18 | `Camera2D` limit clamps the active screen center beyond the authored right boundary; disabled-limit control follows target. | V | `r18-limit-verifier.md` |
| 19 | Stream attribution: same exit-0 with stdout marker vs unrelated `printerr` discriminates accept/reject; classification-identical fields. | V | `r19-stream-verifier.md` |
| 20 | Top-edge camera limit pair; the spoken camera-first claim for r20 was invalid and superseded before dispatch (claim correction, not a measurement). | V | `r20-top-verifier.md` |
| 21 | Real Godot signal-termination classification: same emitted signature, externally signalled process must classify false; bounded lifetime proven. | V | `r21-crash-verifier.md` |
| 22 | Real Godot timeout: pre-timeout success signature is insufficient — timed-out process classifies false (`code=None`), no surviving direct child. | V | `r22-timeout-verifier.md` |
| 23 | Left-edge limit pair: active center = boundary ± half-width (64 px viewport → −968); far-left control fails the intended assertion. | V | `r23-left-verifier.md` |
| 24 | Bottom-edge limit pair with dynamic half-height (→968); far-bottom control follows target. | V | `r24-bottom-verifier.md` |
| 25 | Relative `--runs` export-path failure causally reproduced; both fixture export targets normalized. | V | `r25-export-verifier.md`, SCORECARD |
| 26 | Startup timeout bound: process must not pass on a stale signature before the timeout. | V | `r26-timeout-verifier.md` |
| 27 | Button press semantics measured at HEAD (39 vs 41 case counts reconciled); bounded calibration. | V | `r27-button-verifier.md` |
| 28 | `ui_accept` repeat timing pinned. | V | `r28-repeat-verifier.md` |
| 29 | Button focus dependence measured (focus-absent vs focused press). | V | `r29-focus-verifier.md` |
| 30 | Edge class: press-only vs release observation. | V | `r30-edge-verifier.md` |
| 31 | Focus loss during hold changes the observed press count (bounded). | V | `r31-focus-loss-verifier.md` |
| 32 | CheckBox stateful toggle semantics. | V | `r32-checkbox-verifier.md` |
| 33 | CheckBox edge behavior under repeated presses. | V | `r33-checkbox-edge-verifier.md` |
| 34 | Radio/`ButtonGroup` selection semantics. | V | `r34-button-group-verifier.md` |
| 35 | `ButtonGroup` absence control: without a group, no mutual exclusion. | V | `r35-group-absence-verifier.md` |
| 36 | HSlider input semantics measured (grabber/value path). | V | `r36-slider-verifier.md` |
| 37 | Focus-absence control for HSlider/Button sequence. | V | `r37-focus-verifier.md` |
| 38 | UI edge cell re-measured under real Godot. | V | `r38-edge-verifier.md` |
| 39 | Repeat measurement replicated. | V | `r39-repeat-verifier.md` |
| 40 | Repeat + focus-absence combined cell. | V | `r40-repeat-focus-verifier.md` |
| 41 | Focus handoff mid-sequence measured. | V | `r41-focus-handoff-verifier.md` |
| 42 | Focus restoration returns the same press behavior (bounded). | V | `r42-focus-restore-verifier.md` |
| 43 | Second focus loss before the final press measured. | V | `r43-second-loss-verifier.md` |
| 44 | Second restoration measured. | V | `r44-second-restore-verifier.md` |
| 45 | Double restore + disconnect: bounded calibration supported. | V | `r45-double-restore-disconnect-verifier.md` |
| 46 | Mid-run signal disconnect: bounded calibration supported. | V | `r46-mid-disconnect-verifier.md` |
| 47 | Reconnect after first press: callback path restored. | V | `r47-reconnect-verifier.md` |
| 48 | Late reconnect after final adjustment. | V | `r48-late-reconnect-verifier.md` |
| 49 | Fresh press after late reconnect: focused edge9 left press 4→3, receipts [6,3]/Value3; 64 prior tuples unchanged. | V | `r49-fresh-after-reconnect-verifier.md`, SCORECARD |
| 50 | Release after the late-reconnected press measured. | V | `r50-release-verifier.md` |
| 51 | Parsed-release observer provenance (corrected scratch). | V | `r51-provenance-verifier.md` |
| 52 | `root.push_input` route contrast vs direct callback. | V | `r52-route-verifier.md` |
| 53 | Composite route measured (bounded). | V | `r53-composite-verifier.md` |
| 54 | Order semantics measured. | V | `r54-order-verifier.md` |
| 55 | Omit-await ineffective → **no frame-necessity claim** (negative result recorded). | V | `r55-frame-verifier.md`, SCORECARD |
| 56 | Push+frame: observer 3→4 with action true; direct clear+next frame leaves observer 4/action false; 71 prior tuples stable. | V | `r56-pushframe-verifier.md` |
| 57 | Save/load boundary measured. | V | `r57-save-verifier.md` |
| 58 | Process baseline measured. | V | `r58-process-verifier.md` |
| 59 | Audio boundary measured (export caveat retained). | V | `r59-audio-verifier.md` |
| 60 | Spontaneous-signal classification from returncode alone is unprovable (self vs external SIGKILL indistinguishable; UNKNOWN retained); crash `-6` classifiable only with the crash's own `ERROR:` marker allowlisted; self `-9` classifies false. | V | `round-60/r60-adjudicator.md` |
| 61 | Tracked crash rows: `crash_spontaneous_sigabrt` (−6 + exact ERROR-marker allowlist) + `crash_self_sigkill` (−9); meta row's four mismatch discriminations + marker-presence clause all reject. | V | `round-61/r61-adjudicator.md`, SCORECARD |
| 62 | Descendant-held-pipe TIMEOUT misattribution pinned: hold arm `child_exit_at_timeout=0` + `post_exit_write_captured` gated on kernel reparenting (ppid flip); detach control child-exit-bound; 7 discriminations. | V | `round-62/r62-adjudicator.md` |
| 63 | Merged-stream presence-only signature clause = tracked known-accepting forgery boundary (release arm PASS on post-death descendant signature; hold arm rejects via error axis only); 10 discriminations incl. kernel-corroborated write_ppid; fabricated-ppid slip closed. | V | `round-63/r63-adjudicator.md` |
| 64 | While-live marker gate: `poll()`-gated read rejects forged post-death markers (release×3 + hold, ~32 ms post-death) while accepting genuine/detach (+66–71 ms margin); `kill(pid,0)` false-accepts through the zombie window (2.35–2.42 s drain vs 1–4 ms gate); live-window forge defeats the gate by construction (6/6 verifier, 29/29 critic). | Vc | `round-64/r64-adjudicator.md` |
| 65 | Forged-REJECTION dual: reparent-gated descendant's post-death un-allowlisted `ERROR:` flips a clean exit-0/signature-present record to FAIL on classification-identical fields; counterfactual strip = sole cause; 29 discriminations; 87/87 committed replay, 97 prior rows 0-mismatch. | V | `round-65/r65-adjudicator.md` |
| 66 | Rejection-clause surface: clause inventory (line-scan + 2 allowlist-immune blob conjuncts), allowlist preemptor bound, evasion boundary set, seam-fabrication geometry, dead-entry census (0/40 in-run; 6 static dead surfaces); forgery works in three directions incl. denial-of-verdict (`\xff`→`UnicodeDecodeError`). | V | `round-66/r66-adjudicator.md` |
| 67 | `classify_streams` ↔ `classify_process` divergence mapped as a four-family table (12/27 divergent, rep-stable); signature channel-pin + seam-position bound (stdout-tail|stderr-head only); shipped reject arm itself diverges (T/F, latent since r19). | V | `round-67/r67-adjudicator.md` |
| 68 | Fabrication-window bound measured strictly: write-position space [0,gap), nominal offsets {0–198} fabricate / transition 198.05–198.35 / ≥198.5 never; three regimes (miss / in-window fused line + destroyed sig / straddle H-E-T-E2); spawn-latency floor + ppid crossover ~250–260 ms; declared-grid claim falsified as written (~80× resolution overstated). | Vc | `round-68/r68-adjudicator.md` |
| 69 | Fabrication-window referent pinned **gap-relative**: splice iff write pos ∈ [0,gap); r68's ~198 ms edge shown to be `gap − spawn_overhead`, not a constant; crossed cells refute any absolute edge <~602 ms; edge re-located ~295–300 at gap=300. | V | `round-69/r69-adjudicator.md` |
| 70 | LOVE 11.5 headless first contact: viability positive; `love.update` uncapped (~960 Hz); **fabrication window is Godot-runner plumbing, NOT engine-general** (no fabrication window at LOVE's io layer); os.execute splice = POSIX fd1 inheritance (spawn-general). | Vc | `round-70/r70-adjudicator.md` |
| 71 | pygame 2.6.1/SDL 2.32.72 headless: withholding is a CPython stdio language-layer window; constant = `io.DEFAULT_BUFFER_SIZE` **131072** (GH-118144; ≤3.13 = 8192) — the frontier's ~8 KB bound falsified; compound two-layer window (textio 8192 + BufferedWriter 131072) = 139263 B invisible, 139264th surfaces it. | Vc | `round-71/r71-adjudicator.md` |
| 72 | Reorder fabrication confirmed and correctly attributed: variable = **fd1-OWNER's stdio mode** (brief's "buffered child" wrong); topology family {prefix, infix, midline, append}; window = buffer lifetime not wall-time; mechanism libc/CPython-general (byte-equal on bare python3 and in-pygame). | Vc | `round-72/r72-adjudicator.md` |
| 73 | Topology set closed {prefix, infix, midline, append} + fd2-merge inversion; Node.js v24.21.0 = 4th owner runtime (3rd withholding layer: libuv event-loop queue); infix = flush-epoch constant, not a band; detach-EOF harness-integrity cell. | V | `round-73/r73-adjudicator.md` |
| 74 | LOVE physics interior-write lattice: Box2D callback surface pinned {refused, deferred, fatal, applied} + endContact; fatal partitioned fatal(lua) vs SIGABRT-died; re-entrancy defeats IsLocked; destroy drain inside the update epilogue; carried fifo-SIGTERM-immune guard falsified for LOVE (EINTR). | Vc | `round-74/r74-adjudicator.md` |
| 75 | Deferred/uncontained partition confirmed at byte level: new classes `refused_abort` (step abort + transient lock + collateral refusal) and `ignored` (return value unconsumed, impulse measured landing); F2 gate defect corrected (presence→value). | Vc | `round-75/r75-adjudicator.md` |
| 76 | New class `deferred_abort` (accepted write + abort; drain catches up one step late); world:destroy deferral + next-access death; drain bounded inside step-73 epilogue (`jwlive→jdrain`); retfalse inertness refuted/proven at 3-granularity control. | Vc | `round-76/r76-adjudicator.md` |
| 77 | Release/callback-swap/drain-EC lattice: 26 cells / 6 classes; critic D2/D3 gate defects folded; simplifier P3 67-pin dedup byte-identical. | Vc | `round-77/r77-adjudicator.md` |
| 78 | Nested `world:update` damage surface: 17 new cells; `e_locked` cleared by inner epilogue; inner-drain ownership; Memoizer dispatch escape; body-drain-EC nested SIGSEGV; zombie-contact silent UAF; livelock/`drain_converge`; drain provenance required (own/own_n). | Vc | `round-78/r78-adjudicator.md` |
| 79 | Godot-4 2D contact/event battery (`phys2d_events`): interior-window cell table + motion-query family; record corrections P1/P2 (colliders snapshot not invariant; deferred writes durable, reframed as same-frame visibility). | Vc | `round-79/r79-adjudicator.md` |
| 80–81 | *frontier scouts* — `RigidBody2D` CCD + motion-query family; 2D joint lattice + collision layer/mask lattice. | frontier | `round-80/`, `round-81/` |

### 1.3 game-dev-3d-shokunin

Rounds 2–68 survive as LOG entries + `corpus/lessons/` (no report files —
see §3.4); laws below are from `LOG.md` round sections. Rounds 69+ carry
full report dirs.

| rnd | law (one line) | st | carrier |
|---|---|---|---|
| 1 | Headless Godot 4.7.2 3D battery exists and discriminates causal positives from intended negatives across six mechanic classes (12 cases; exit/marker contract). | V | LOG r1 |
| 2 | Independent r1 replay (non-author) reproduces battery + mutation receipts; no unsupported claim found. | V | LOG r2 |
| 3 | Direct-child crash-exit classification: same marker, externally signalled process must reject. | V | LOG r3 |
| 4 | stdout/stderr attribution: unexpected non-error stderr diagnostic tolerance tested on a real 3D fixture. | V | LOG r4 |
| 5 | Bounded process-tree timeout with descendant-spawning fixture + process-group termination receipt. | V | LOG r5 |
| 6 | three.js scene-graph math executes headlessly (no GL context claimed). | V | LOG r6 |
| 7 | Camera3D near/far frustum gates incl. rotated camera. | V | LOG r7 |
| 8 | Near-plane rejection for positive depth < near. | V | LOG r8 |
| 9 | Self-authored GLB static inspection (REA) + one-byte length-defect rejection. | V | LOG r9 |
| 10 | REA ZIP inventory of the GLB carrier (generic members only). | V | LOG r10 |
| 11 | Godot headless GLB import/load and instancing. | V | LOG r11 |
| 12 | Discriminating GLB import rejection (invalid total-length header accepted by importer → negative control established). | V | LOG r12 |
| 13 | Headless 3D navigation path query (NavigationServer3D/Region3D/NavMesh). | V | LOG r13 |
| 14 | Grounded-floor contact (`is_on_floor()`) vs airborne control. | V | LOG r14 |
| 15 | Slope floor-angle classification (floor/wall booleans at 30°/60°). | V | LOG r15 |
| 16 | Slope telemetry readback: configured `floor_max_angle` read back; hardcoded markers shown to lie under mutation. | V | LOG r16 |
| 17 | PackedScene instance-local 3D transforms (two instances, distinct child transforms). | V | LOG r17 |
| 18 | Persisted `.tscn` save/load round-trip of authored child transforms. | V | LOG r18 |
| 19 | Unity-style text-scene references (static format vocabulary only; Unity absent). | V | LOG r19 |
| 20 | Mesh-resource instance isolation under PackedScene (mutable BoxMesh sharing). | V | LOG r20 |
| 21 | `resource_local_to_scene` locality survives scratch `.tscn` save/load. | V | LOG r21 |
| 22 | Unreal `.uplugin` descriptor static module-type check (format vocabulary only). | V | LOG r22 |
| 23 | Orthographic Camera3D depth-invariant projection. | V | LOG r23 |
| 24 | Orthographic near-plane gate (positive-forward pre-near point rejected). | V | LOG r24 |
| 25 | Orthographic far-plane gate. | V | LOG r25 |
| 26 | Gravity-driven jump/landing sequence with displaced floor. | V | LOG r26 |
| 27 | Sampled initial grounded state before impulse (geometry alone insufficient). | V | LOG r27 |
| 28 | Gravity-driven downhill travel vs level control. | V | LOG r28 |
| 29 | Downstream slope assertion sensitivity (mutated angle rejected independently of the rotation guard). | V | LOG r29 |
| 30 | Keyframed 3D transform evaluation at sought timestamps. | V | LOG r30 |
| 31 | Frame-advanced animation playback updates a 3D node without further `seek`. | V | LOG r31 |
| 32 | 3D position cross-fade between two live animations. | V | LOG r32 |
| 33 | Procedural `ArrayMesh` from explicit vertices; surface arrays/bounds readback. | V | LOG r33 |
| 34 | Indexed procedural mesh topology (shared vertices across triangles). | V | LOG r34 |
| 35 | Mesh-derived physics collision (one-face triangle collider, `face_index=0`). | V | LOG r35 |
| 36 | Two-face indexed mesh collision routing (distinct hit faces on interior rays). | V | LOG r36 |
| 37 | `MultiMesh` per-instance transform readback (CPU data only). | V | LOG r37 |
| 38 | `Skeleton3D` rest/pose readback under headless runtime. | V | LOG r38 |
| 39 | Child-bone rotation composes in the pose hierarchy. | V | LOG r39 |
| 40 | `BoneAttachment3D` live child node follows the bone. | V | LOG r40 |
| 41 | `ShapeCast3D` swept-shape query (collider/contact/safe fraction). | V | LOG r41 |
| 42 | Finite-radius grazing cast vs ray miss (radius is load-bearing). | V | LOG r42 |
| 43 | `Curve3D` baked spatial path. | V | LOG r43 |
| 44 | `PathFollow3D` scene-tree transform along a baked curve. | V | LOG r44 |
| 45 | Frame-paced `PathFollow3D` progress. | V | LOG r45 |
| 46 | Callback-driven `PathFollow3D` progress. | V | LOG r46 |
| 47 | `RemoteTransform3D` live target propagation. | V | LOG r47 |
| 48 | `RemoteTransform3D` rotation-propagation attribution. | V | LOG r48 |
| 49 | Live `NavigationAgent3D` next-path query. | V | LOG r49 |
| 50 | Callback-driven actor follows the navigation next point. | V | LOG r50 |
| 51 | Live retarget during callback-driven following. | V | LOG r51 |
| 52 | Independent attribution of the r51 final actor endpoint. | V | LOG r52 |
| 53 | Current-battery reproduction contract (freeze + replay discipline). | V | LOG r53 |
| 54 | Orthographic near-plane adjacent pair. | V | LOG r54 |
| 55 | Orthographic far-plane adjacent pair. | V | LOG r55 |
| 56 | Orthographic exact near-plane sample. | V | LOG r56 |
| 57 | Orthographic exact far-plane sample. | V | LOG r57 |
| 58 | Node three.js perspective frustum math. | V | LOG r58 |
| 59 | three.js near-plane exclusion at a shared projected ray. | V | LOG r59 |
| 60 | three.js orthographic depth-invariant projection/frustum. | V | LOG r60 |
| 61 | Strict Node stream bytes: `expectedLine + "\n"`, other stream empty (private copied-source `\n\n` accepted by old runners, rejected by revised). | V | SCORECARD calibration row, `corpus/lessons/r61-stream-review.md` |
| 62 | three.js orthographic near-plane exclusion. | V | LOG r62 |
| 63 | three.js Raycaster triangle hit/miss. | V | LOG r63 |
| 64 | Raycast front/back face discrimination. | V | LOG r64 |
| 65 | Raycaster ordered two-mesh intersections. | V | LOG r65 |
| 66 | Raycaster near/far distance clipping. | V | LOG r66 |
| 67 | Sampled inclusive Raycaster range boundaries. | V | LOG r67 |
| 68 | Raycaster layer-mask selection: mask1 near, mask2 far, mask3 both ordered; far-layer mutation with ray mask2 exits 1 on zero actual hits (CPU mask selection, not rendered visibility). | V | SCORECARD coverage row, `corpus/lessons/r68-ray-layers-review.md` |
| 69 | NavAgent3D distance/reachability probe family; `distance_to_target`=2.828427 on convex polygon where Euclidean and path-sum coincide → UNKNOWN retained. | V | LOG r69 |
| 70 | `distance_to_target` = Euclidean to the **raw authored** `target_position` (detour 3.605551 vs path 4.130649); reach gates key off `euclid(final, target) ≤ tdd` (through-wall with no path). | V | `round-70/r70-adjudicator.md` |
| 71 | Postprocessing invariance: Euclidean-to-raw target under corridorfunnel/edgecentered/none while pathlen changes; `final` postprocessing-invariant (claim's "final changes" clause measured false and narrowed). | Vc | `round-71/r71-adjudicator.md` |
| 72 | pdd pop law: `idx` advances while `idx<size−1 ∧ euclid(agent, path[idx])<pdd` — strict, sequential, live-position keyed, saturates at `size−1`; `reached` = strict `euclid(agent, raw target) < tdd`, through-wall, latched; `reachable` = inclusive `euclid(final→target) ≤ tdd`; `finished` = `reached OR (¬reachable ∧ idx==size−1 ∧ euclid(agent, final) < pdd)` (critic's idx-conjunct counterexample absorbed as claim wording). | Vc | `round-72/r72-adjudicator.md` |
| 73 | Off-mesh link traversal gate system: LINK-type metadata at hop-start under `path_metadata_flags` per-bit control (opt-OUT, default 7 on 4.7.2); layers-bitmask / bidirectional-exit-side / enabled=false each independently drop the link to byte-identical no-link tuples; `enter_cost` structurally inert vs `travel_cost` live (crossover ~1.12); pop-through symmetric; `vertices.append_array` post-assignment non-write-through. | V | `round-73/r73-adjudicator.md` |
| 74 | Lazy-update model: forcing-getter set vs pure readers; stored path frozen strictly under pmd (5.000000==pmd re-queries); pop = live-pos sequential strict `<`; latch survives all motion, released by ANY `target_position` assignment (same-value too); lazy materialization anchored at first forcing call. | V | `round-74/r74-adjudicator.md` |
| 75 | Two-stage mutation gate: setter→server-sync (~2–3 frames) + sync→first-forcing-call; same-turn pre-sync serving is a bounded zombie window; pure readers serve stale indefinitely; `navigation_layers` = synchronous exception; **finished-latch zombie** (dead route served through region move AND delete until target re-assign); header "never SERVED" overclaim corrected to post-sync scope. | Vc | `round-75/r75-adjudicator.md` |
| 76 | Per-class serve edges as strict constants: link 2, region 3, `map_off` never, agent 0; `map_off` permanent-stale regime distinguished from the latch; inside-window zombie serves; same-value suppression on every probed setter (target_position carve-out); "wait≥1" falsified per-class; callsite qualifier (physics-callback write one tick shallower — later corrected, see r78). | Vc | `round-76/r76-adjudicator.md` |
| 77 | Apply-order is load-bearing only through RID lifecycle (doomed-RID voiding, masking witness); `map_force_update` reach split — getter edge collapses same-turn, serve edge = mark-vs-phase race (link jitter {1,2} ~15–20%, region −1f deterministic); "emergent seam" corrected to dead-write voiding. | Vc | `round-77/r77-adjudicator.md` |
| 78 | `map_set_active(false)` permanence = measured +1200f regime with in-fixture falsifier (map_iter/link_iter pins, iter_watch canary); reactivation edge on+2 wait-independent; callsite pair resolved to sample-base semantics (kills the r76 "−1 tick" misreading). | Vc | `round-78/r78-adjudicator.md` |
| 79 | bpy (Blender 5.2.1 headless) two-layer lattice: write-through vs evaluation-gated split (NOT RNA-vs-depsgraph); held-handle staleness unbounded (map_off analogue); drain absent; shared-graph flush; membership edge; non-signal quirk. | P | `round-79/r79-adjudicator.md` |
| 80 | bpy eval-event catalogue folded: `bpy.ops`-call auto-eval (new class), driver edge=1, keyframe binds only at `frame_set`, handler timing split (dup vs fc), msgbus/undo_post dead headless; bounded closure ~100 probed mutation classes, 0 falsifiers across 4 sweeps; mechanical falsifier armed (`closed|violations`). | V | `round-80/r80-adjudicator.md` |
| 81 | X1 reorder fabrication confirmed on a SECOND Python runtime (bpy `-b -P`): child bytes prefix the parent's buffered rows (child < pre_spawn); parse-survival contract pinned (gluevictim dropped, physical last-wins); **`PYTHONUNBUFFERED` inert on bpy** (X1 prediction (iv) falsified); evalcat 8→14. | Vc | `round-81/r81-adjudicator.md` |
| 82 | evalcat residual fold 14→20 (update_tag witness, custom setter, libraries, instance, batch_remove, evalget stale/freed/refused edges); forge-last masking measured reachable (74/74 silent) → independent genuine-cell invariant armed; `batch_remove` stale-ref SIGSEGV boundary mapped; parser-hazard contract pinned both directions. | V | `round-82/r82-adjudicator.md` |
| 83 | PhysicsServer3D two-tier lattice: queries edge-0, generated events tick-bound, sync-callback once/tick; write-phase dependency (delta=1|2); ST refusal = deterministic context gate; `static_nopair` inversion between GodotPhysics3D and Jolt recorded. | Vc | `round-83/r83-adjudicator.md` |
| 84 | Jolt backend pinned as an in-battery probed arm (jolt_edge child re-exec, 7-key verdict map); `phase_delta` first-class cell (proc=2 / phys=1, identical across both backends). | Vc | `round-84/r84-adjudicator.md` |
| 85 | Jolt × `run_on_separate_thread` cross-product confirmed (191/191); threading invariance at map+constant level; backend-determinism under another real backend; mutation matrix 6/6 load-bearing; forged child.log rejected. | Vc | `round-85/r85-adjudicator.md` |
| 86 | `script_size_gate` stochastic band (~475–575, verified), `deferred_hang` class, `backend_tier`, `dummy_floor` zero-vs-positive; 195/195 with 191 prior rows byte-identical; parked nav cell record corrected (scout `safe_n=10` vs author `safe_n=0` both reproduced — missing `project.godot` harness artifact, NOT a scout falsehood). | Vc | `round-86/r86-adjudicator.md` |
| 87 | Body-tier direct-state lattice: 201/201 folded battery, 195/195 prior rows; `freed_space` crash-line + GP crash-site + refusal-count corrections folded; `ss_fired` bucketed pin; author correctly refused the scout's nav cell (replication gave the falsifier). | Vc | `round-87/r87-adjudicator.md` |
| 88 | *in flight* — `PhysicsDirectSpaceState3D` read family + `PhysicsDirectBodyState3D` inertia getters. | flight | `round-88/` |
| 89 | *frontier scout* — `PhysicsDirectBodyState3D` contact family, `_integrate_forces` interior rules, joint family, cross-space handles, sleeping body. | frontier | `round-89/r89-scout.md` |

### 1.4 Cross-lane laws (same behavior measured in ≥2 lanes)

| law | lanes/rounds | notes |
|---|---|---|
| Child-stdout fabrication/splice window = POSIX fd1 inheritance × the fd1-owner's buffering mode (spawn-general, not engine-general) | 2d r70/r72/r73; 3d r81/r82; audio — n/a | 2d r70 refuted engine-generality; 2d r72 fixed the referent to fd1-OWNER; 3d r81 extended to bpy; xconnector w12 lists the C-stdio cell as already measured. |
| Withholding window bounded by the runtime's buffer constant, not a universal 8 KB | 2d r71 (CPython 131072), 2d r73 (libuv event-loop layer), 3d r81 (bpy: PYTHONUNBUFFERED inert) | the ~8 KB frontier assumption falsified once, then re-scoped per runtime. |
| Descendant-held-pipe TIMEOUT misattribution (tree-timeout is a pipe-EOF wait, not child liveness) | 2d r62 (ported from 3d r5); 3d r5 | 2d r62-boundary explicitly ports 3d's mechanism; 3d r72 verifier's relative-`--runs` trap re-recorded in 2d. |
| Liveness-gated acceptance of a marker read (while-live gate defeats forged post-death markers) | 3d r72 proposal → 2d r64 landed; 2d r63 boundary | XConnector-flagged cross-lane import; live-window forge remains open by construction in both. |
| Write-visibility windows on a deferred/server-synced physics surface (setter→sync→reader) | 3d r74–r78 (Godot navserver); 2d r74–r78 (LOVE Box2D callbacks) | same *shape* of law (deferred write + drain epoch) measured on two engines; 3d edges are strict frame constants, 2d classes are refused/deferred/fatal/applied. |
| Verdict-string/stream parsing hazards under captured output | 2d r61–r69 (Godot runner); 3d r61 (Node strict stream bytes), 3d r81/r82 (bpy parse-survival) | parser survival ≠ parser safety; forged-last masking documented in 3d r82. |
| Rate/format gate behavior on odd headers (valid-bits / extensible / codec reclassification) | audio r57–r64 only | single-lane; recorded here to prevent future cross-lane re-derivation. |

## 2. Contradiction ledger

Claims that conflicted with a later measurement, and which survived.
Resolution column names the surviving behavior; "survivor" is the record's
own corrected wording, not this seat's judgment.

| # | earlier claim (pointer) | later conflicting claim (pointer) | resolution / survivor |
|---|---|---|---|
| C1 | audio r67-boundary: residual margin "~0.5–1.0 s" for the fifo writer hold. | audio r70 scout + r70 ladder: h* ≈ O(10–50 ms); r67's own `-tt` trace shows open #2 at +30 ms. | Survivor: transition band (oneshot {0 blocked → ≥50 ms stable}, ~18 ms mixed), load-dependent; 1.0 s is a margin-of-safety pin, never a measured edge. |
| C2 | audio r70 pre-claim: the fifo verdict is strictly binary on writer-attached-at-open-#2. | audio r70 chunked-feed control: normal verdict lands at h*=0 when delivery spans open #2. | Survivor: outcome space = attach × close-before-deadline; the third outcome (attach-through-delivery) refutes strict binary-on-attach. |
| C3 | audio r67: decode-stage fork is on the seekable bit (named × seekable proxy). | audio r68 four-seat convergence: fork resolves on NAMED-resolvability; `ft->seekable` never read on the post-table path; prefetch bytes are pending-buffer-replayed. | Survivor: named-axis mechanism; genuine seekable fork exists only inside the txw reader (`{file,redirected_fd}` decode vs pipes refuse). |
| C4 | audio r72 pre-claim: a "sndfile-only" `.snd`-named class. | audio r72 adjudication: sox also accepts `{file,fifo}` (sndr/504) — class is sox∩sndfile vs ffmpeg-reject. | Survivor: corrected class partition; the sndfile-unique exemplar is `.au`-named identical bytes (frontier, untracked). |
| C5 | audio r73 pre-claim: corpus-wide "consumer polarity" (opposite of the decoder axis). | audio r73 adjudication: member-local (1/9), name-independent; pw-cat's real fork is the inherited libsndfile fallback. | Survivor: member-local forks; corpus-wide polarity falsified as worded. |
| C6 | xconnector w12: four-condition lavf fork rule predicting `acm` forks. | audio r74: `acm` satisfies all four yet does not fork at the output level (rc=0, identical 868 B PCM); real gate is `AVFMT_NOGENSEARCH`. | Survivor: NOGENSEARCH-gated fallback; `acm` = `wound` class only; `fork_kind` lattice landed. |
| C7 | audio r76 row: arecord TERM behavior stated universally. | audio r77 scout falsified the r76 row's universality. | Survivor: r77 records the corrected, receipt-backed sever/gate classes; r76 row scope narrowed. |
| C8 | 2d r68 declared grid: fabrication edge ~200 ms at ~80× grid resolution. | 2d r68 critic: bound is on write-position, grid resolves only (160,240]; edge stochastic ~198.3–198.5 ms; lo unreachable. | Survivor: write-lands-between-flushes bound; the ~80× grid claim recorded as falsified-as-written. |
| C9 | 2d r68: ~198 ms is an absolute edge constant. | 2d r69: crossed cells (300,400)/(300,800)/(600,800) refute any absolute edge <~602 ms; edge re-locates with gap. | Survivor: gap-relative referent — splice iff write pos ∈ [0,gap); r68's number = `gap − spawn_overhead`. |
| C10 | 2d r66–r69 model implied an engine-general fabrication window. | 2d r70 LOVE first contact: no fabrication window at LOVE's io layer; the Godot bound is runner plumbing. | Survivor: spawn-general (POSIX fd1 inheritance); engine-general scope refuted at the engine layer. |
| C11 | 2d frontier assumption: withholding window ≈ 8 KB. | 2d r71: bound = `io.DEFAULT_BUFFER_SIZE` 131072 on CPython 3.14.7 (GH-118144); compound 139263 B window. | Survivor: 131072 constant, build-specific; the 8 KB figure was a stale-artifact assumption. |
| C12 | 2d r72 brief: "buffered child" is the reorder variable. | 2d r72 critic F1: variable = fd1-OWNER's stdio mode; topology family {prefix,infix,midline,append}. | Survivor: owner-mode referent; carried as a wave guard (w13–w15 SHARED). |
| C13 | 2d r63/r64 carried guard: fifo-open blocks are SIGTERM-immune (general). | 2d r74: guard falsified for LOVE (EINTR); later narrowed again in wave guards ("ONE-TERM survival only" — aplay dies to TERM₂). | Survivor: per-consumer signal partition; `timeout -s KILL` is the kill bound; no general immunity claim. |
| C14 | 2d r19-era assumption: `classify_streams` and `classify_process` agree on the shipped reject arm. | 2d r67: 12/27 divergent; the shipped `--probe-stream-attribution` reject arm itself diverges (T/F, latent since r19). | Survivor: divergence table + channel-pin bound; latent defect recorded, default path untouched. |
| C15 | 2d r64: `kill(pid,0)` suffices as a liveness witness. | 2d r64/r65: false-accepts through the 2.35–2.42 s zombie window; kernel ppid corroboration required. | Survivor: `poll()`-gated while-live read + kernel-corroborated witnesses; primitive load-bearing (13/13 critic, 29/29 scribe). |
| C16 | 2d r76 "callsite write is one tick shallower". | 2d r78: callsite pair = sample-base shift (same sync drain); r76 reading killed. | Survivor: sample-base semantics; bound=2 (resume) vs bound=1 (…) per r78. |
| C17 | 3d r71 declared clause: `get_final_position` changes under postprocessing. | 3d r71 critic's 12-arm attack incl. off-edge clamp bait: `final` invariant. | Survivor: narrowed claim — distance Euclidean-invariant; `final` invariance is the measured fact; false clause preserved as a green negative. |
| C18 | 3d r71-boundary: finished-gate unreachable clause is `≤ ~pdd`. | 3d r72 critic counterexample `u_gap_pdd2.3` (euclid(final)=2.0616 < pdd=2.3 yet finished=false, pop blocked at idx=1). | Survivor: strict `<` + conjunctive `idx==size−1`; defect was claim wording — landed artifact already encoded the corrected model. |
| C19 | 3d r75 header: pre-sync state is "never SERVED". | 3d r75 critic: same-turn zombie window serves pre-sync; global per-agent dirty (not per-edge). | Survivor: post-sync scope wording; ≥1-frame zombie window pinned. |
| C20 | 3d r76: "wait ≥ 1 frame suffices" / "physics-callback writes are one tick shallower". | 3d r76 scout (wait≥1 falsified per-class) and r78 (callsite corrected to sample-base). | Survivor: per-class edges {link:2, region:3, agent:0, map_off:never}; sample-base callsite. |
| C21 | 3d r77 fixture comment: serve edge does not collapse under `map_force_update`; "emergent seam". | 3d r77 critic: region serve edge deterministic 3f→2f (9/9); mechanism = dead-write voiding, not emergence; mut_force_link flakes ~15–20% inside the official battery → jittered cell skipped, not pinned. | Survivor: RID-lifecycle voiding mechanism; deterministic region sample pinned, jittered link sample honestly skipped. |
| C22 | 3d r84 boundary/reviewer premise: `delta_pf=1`. | 3d r84 critic F1: premise refuted (process-context delta=2 / physics=1); reviewer F3 premise partially refuted. | Survivor: `phase_delta` proc=2 / phys=1 first-class cell; refuted premises recorded, pins keyed by measured value. |
| C23 | 3d r86 record: parked nav cell = scout falsehood. | 3d r86 reviewer F1 + verifier: scout `safe_n=10` byte-identical whenever `project.godot` exists (17/17 incl. empty file); author `safe_n=0` only in project-less harness (11/11). | Survivor: harness-artifact explanation — NOT a scout falsehood; record corrected. |
| C24 | xconnector w12 X1 prediction (iv): `PYTHONUNBUFFERED` will control bpy buffering. | 3d r81: PYTHONUNBUFFERED inert on bpy without `--python-use-system-env`. | Survivor: per-runtime falsifier working as designed; bpy requires the flag pair. |
| C25 | 2d r79 scout reading P1: `cb1_colliders=1` is a count invariant; P2 deferred writes are window-scoped reverts. | 2d r79 adjudication: P1 = dispatch-order snapshot (`colliders_2=2` measured); P2 = deferred writes land durably (same-frame visibility, not revert). | Survivor: value-stable cells with corrected interpretation notes. |
| C26 | 2d r20 spoken camera-first claim ("round 1 is branch tip"). | 2d r20 LOG: HEAD already closed r19; camera has r2/r18 coverage. | Survivor: spoken claim superseded before dispatch; no edit or admission rested on it. |

Unresolved / open contradictions (no resolving measurement on the
report surface as of this pass):

- 2d r64 live-window forge "defeats the gate by construction" vs the
  gate's claimed discrimination envelope — both are recorded; the
  post-death-origin vs authorship distinction remains open by design.
- 3d r82 `batch_remove` stale-ref SIGSEGV boundary vs r79's "absent
  drain" lattice — the boundary is mapped but the drain/refcount
  interaction is not closed.
- audio r76→r77 sink-topology drift: r76 regression failures classified
  host-state (pre-fold HEAD repro + named 18.6% contention class); the
  host-state attribution is bounded, not independently reproducible on a
  differently-loaded host.
- 3d r77 "truth digests = open frontier" — non-serve state is hidden by
  verdict groups; no measurement closes it yet.

## 3. Coverage map

### 3.1 Measured surfaces (by lane, current)

- **audio**: SoX_ng 14.8.0.1 transport/autodetect surface (9-member × 4
  transports, 119-row ledger and descendants), valid-bits→codec step
  map, preemptor ordering, capture-side consumers (pw-record/parecord/
  arecord/ffmpeg), capture-source lattice + fallback law, playback
  consumers (pw-cat/mpv/paplay/aplay/ffplay), ffmpeg/ffprobe and
  libsndfile decoder matrices, PipeWire sever/wound partitions.
- **2d**: Godot 4.7.2 headless UI/input surface (Button/CheckBox/HSlider
  focus/edge/repeat/reconnect sequences r27–r56), runner classifier
  surface (crash/signal/timeout/stream-attribution r19–r69), forgery
  boundary family (r63–r69), three runtimes (Godot, LOVE 11.5, pygame
  2.6.1/SDL 2.32.72) + Node.js owner runtime, LOVE physics callback
  classes r74–r78, Godot-4 `phys2d_events` battery r79.
- **3d**: Godot 4.7.2 headless 3D mechanics (r1–r68 across six mechanic
  classes, navigation, resources, animation, physics), navserver
  mutation semantics r69–r78, Blender 5.2.1 bpy lattice r79–r82,
  PhysicsServer3D two-tier + Jolt backend pair r83–r86, body-tier
  direct-state r87; Node three.js math suites (31/31) throughout.

### 3.2 Named-but-unmeasured / queued coverage gaps

| lane | surface named, not measured | queue origin |
|---|---|---|
| audio | non-`USING_FFMPEG` SoX build (source-only, unreachable) | SCORECARD `planned` line |
| audio | stdin + ffmpeg-bridge dead combination (disclosed, unexercised by design) | r64/r66 adjudicators |
| audio | `.mp3`/`.aptx`/`.dts` fifo hazards (disclosed) | r69 adjudicator bounds |
| audio | playback-side fallback/re-link lattice | r78 in flight; r78-scout-playback |
| audio | pw-loopback/filter-chain DSP; `pactl load-module` topology lifecycle; GStreamer↔PipeWire | r79–r81 frontier scouts |
| 2d | production-project launch; GUI/rendering; platforms beyond this host | SCORECARD coverage row |
| 2d | stall-knee margins; kill(0)-trap lint | SCORECARD `planned` (r64-era) |
| 2d | transitive-depth forgery; startup-knee stochastic band; zombie persistence | SCORECARD `planned` |
| 2d | `RigidBody2D` CCD + motion-query family; 2D joint lattice; collision layer/mask lattice | r80–r81 frontier scouts |
| 2d | immediate `free()` in-cb refused member (queued future arm) | r79 record correction P3 |
| 3d | rendering/GPU behavior; navigation-mesh baking; multiplayer/replication; orthographic precision beyond the sampled points; general slope sliding/friction; untouched grounded-flag/jump-controller; other resource types/solver regimes | SCORECARD `planned` |
| 3d | Unity/Unreal runtimes (not installed; static samples only); production-project launch; broad PackedScene serialization/compatibility; GUI/viewport embedding; 3D export templates; other platforms | SCORECARD `planned` |
| 3d | moving-agent locomotion dynamics beyond teleport-only motion; multi-agent/node-link; latch-release under motion | r74/r75 bounds |
| 3d | truth digests for non-serve state; jittered link force-update cell | r77 bounds (honestly skipped) |
| 3d | `PhysicsDirectSpaceState3D` read family + inertia getters; contact family, `_integrate_forces`, joints, sleeping body | r88 in flight; r89 scout |

### 3.3 Queues that were closed during the observed window

xconnector w12 ranked arms X1–X7 all landed: X1 owner census → 2d r73
(Node.js, 4th runtime); X2 lavf no-seek sweep → audio r74; X3 pw-cat
ops-2 → audio r74; X4 reorder topology depth → 2d r73; X5 physics
interior writes → 2d r74–r78 + 3d r83–r86; X6/X7 → 3d r82. Frontier
pre-measurements all folded: audio fa-sndfile → r72; 2d fa-pygame → r71
and fb-lovephysics → r74; 3d fa-bpy-evalcat → r80 and fb-physserver →
r83. This is a healthy closed-loop signal: the fleet's queued surfaces
are being consumed faster than new ones are named.

### 3.4 Structural coverage gaps (report surface, not domain)

- **3d r2–r68 report durability**: no `reports/round-N/` files exist for
  rounds 2–68 (first `reports/` commit is r69). Their evidence survives
  only in `LOG.md` entries and `corpus/lessons/`. Cross-lane readers
  (like this seat) can law-index those rounds only from LOG text; any
  future audit requiring per-seat reports for r2–r68 will fail to find
  them. Named, not repaired (repair is a lane/operator action).
- **audio r78 and 3d r88 lack adjudicators** on disk at this pass; their
  laws are recorded as in-flight rather than verified.
- **2d r79 late wave rows**: r79 adjudicator is landed while w20 task
  list still carries r79 author/baseline/scribe rows — a bookkeeping
  overlap, not a missing report; noted so the next closure pass does not
  double-count the round.
- **Sibling-lane host contention** appears repeatedly in 2d/3d receipts
  (r62–r68 2d baselines; r73–r76 3d baselines) as named confounds. It is
  documented, bounded, and does not change verdicts, but it is the
  single most frequent receipt caveat in the corpus.

## 4. Duplicate scout targets (waste signal for future dispatch)

Duplicate = two or more scout seats dispatched to measure the same arm.
In-round parallel scouts with disjoint surfaces are excluded; the
classes below are same-arm repeats across rounds.

| # | class | instances | arm measured | waste assessment |
|---|---|---|---|---|
| D1 | 2d `regression-scout` | 33 files, r19–r53 (every round) | prior battery + opt-in flags regression audit | **Largest single class.** Same map re-derived each round; recommend one standing regression map + delta-only audits on rounds that touch the runner. |
| D2 | 2d `baseline-scout` | 8 files, r20–r29 | immutable HEAD baseline | Same target (freeze identity) each round; mergeable into the standing regression map. |
| D3 | 2d Button/focus/edge/repeat family | r27,r28,r29,r30,r31,r37,r38,r39,r40,r41,r42,r43,r44 (13 rounds) | Button focus / press-edge / repeat semantics under one assertion | Successive rounds re-measure the same widget arms with fresh scouts; a single pinned focus/edge/repeat table with delta audits would carry the same evidence. |
| D4 | 2d Camera2D limits | r2 (follow), r18 (right), r20 (top), r23 (left), r24 (bottom) | camera edge limits | Each edge is a distinct arm; the *scout* target (limit semantics) is identical — one scout could have mapped all four edges in one dispatch. |
| D5 | audio layer join/gap/slope scouts | r8–r19 (12 rounds) | 120/180/200 Hz internal join, gap, slope gates | Iterative by design (each round adds a matched negative), but the scout re-maps the same fixture/geometry each time; a single geometry map + per-round negative spec would cut 10+ scout dispatches. |
| D6 | audio comparator-arm scouts | r40–r47 (8 rounds) | one comparator arm per round (endpoint, slope, peak, RMS, duration ±, centroid band) | Same *method* (find a bracketing pair) applied to sibling arms; batchable into one scout mapping all arms of the gate. |
| D7 | 3d nav-agent distance family | r70, r71, r72 (+ r69 UNKNOWN) | `distance_to_target` semantics / pop / finished | Sequential resolution of one question; each round's scout re-derives overlapping context. |
| D8 | 3d mutation-window family | r74–r78 (5 rounds) + frontier fb-physserver | setter→sync→reader windows | Deliberate depth ladder; scouts repeat the same lattice scaffolding (mutation classes × wait ladders). |
| D9 | Same-round parallel scouts | audio r77 (`r77-scout` + `gst-scout`, both capture/playback), audio r78 (`r78-scout` + `r78-scout-playback`), 2d r77 (`r77-scout` + `gd-scout`), 3d r86 (`r86-scout` + `nas-scout` + `bpx-scout`), 2d r19 (hash/regression/stream) | overlapping frontier inventory | Mostly complementary halves; audio r77 and 2d r77 show genuine overlap (same round, same surface family, two seats). Cap parallel scouts per surface at one. |
| D10 | Cross-lane re-derivation | X1 reorder measured in 2d r72/r73 and 3d r81/r82; tree-timeout in 3d r5 and 2d r62; while-live gate proposed 3d r72 → landed 2d r64; relative-`--runs` trap 3d r72 → recorded 2d r72 | same mechanism, different runtime | Deliberate generalization (each runtime is a new arm) — **not waste**, but the xconnector/SHARED surface is what keeps it deliberate; without it these look like duplicates. Keep the cross-lane carrier. |
| D11 | Same-arm double measurement inside one round | audio r70 (scout map + baseline's independent 10-rep ladder); 2d r62 (verifier + boundary port); 3d r86 (verifier re-derived every arm with its own children) | independent reproduction | By-design verification redundancy, not waste; do not dedupe. |

## 5. Composed compatible-set candidate (composition evidence only)

The compatible survivor set below is the subset of §1 laws that the
corpus cross-reference shows to be mutually consistent (no surviving
contradiction in §2, no shared arm with conflicting values, each
non-author reproduced where the lane's rules require it). Composition was
**rescored by cross-reference only** — no new measurement, no verdict.

Composition axes carried (the lanes' declared axes): depth, coverage,
calibration.

**C1 — "Host plumbing is not engine semantics" (cross-lane, 3 laws).**
2d r70 (fabrication window = runner plumbing), 2d r72 (referent =
fd1-owner mode), 3d r81 (bpy X1 reorder confirmed, PYTHONUNBUFFERED
inert). Composes with the guard set carried in w13–w15 SHARED. Depth and
calibration consistent; coverage is per-runtime.

**C2 — "Buffer/withholding constants are per-build" (3 laws).**
2d r71 (131072 on CPython 3.14.7), 2d r73 (libuv third layer), 3d r81
(bpy flag pair). Composes; no conflicting constants remain after C11.

**C3 — "Gate behavior is a measured bracket, never an equality" (audio
r19–r49 family + 2d/3d strict/inclusive edge pins).** Audio's ~20
comparator brackets, 2d's classification boundaries, and 3d's strict
`<` / inclusive `≤` gate table are the same epistemic shape: measured
adjacent points, no equality claim. Composes across all three lanes.

**C4 — "Forgery/verdict-string surfaces must be pinned in both
directions" (2d r63–r69 + 3d r82).** Forged PASS, forged FAIL, forged
TIMEOUT, denial-of-verdict, forged `violations=0`, glue-victim drops.
Composes: each lane names its own accepting boundary rather than
claiming safety.

**C5 — "Deferred-write windows are engine- and phase-scoped" (3d
r74–r78 + 2d r74–r79).** Godot navserver edges are strict frame
constants with a sample-base callsite qualifier; LOVE Box2D classes are
refused/deferred/fatal/applied with a drain epoch. Composes as the same
law shape over two engines; no shared constant is asserted.

**C6 — "Transport/runtime breadth is a measured axis" (audio r67–r77 +
2d r70/r71/r73 + 3d r79–r87).** Each new runtime (decoder, consumer,
engine) is measured against a frozen prior ledger with byte-identity
checks. Composes; the only cross-lane constants are per-build names.

Excluded from the compatible set (survivor set only):

- any claim still carrying an unresolved contradiction (§2 open list);
- in-flight rounds (audio r78, 3d r88) and frontier scouts (audio
  r79–r81, 2d r80–r81, 3d r89) — no adjudicated law yet;
- r71 audio and r79 3d are marked **P** (provisional, verifier pending
  at write) and are carried as depth-only composition members with that
  caveat attached, not as fully verified rows.

## 6. Invalid bucket (records that could not be admitted as evidence)

Records that are malformed or evidence-free *as carriers for this index*
— never repaired here:

1. **audio r78 / 3d r88**: no adjudicator report on disk. Seat reports
   exist; the round-level law is not yet filed. Treated as in-flight,
   not as a law. (No inference drawn from seat text alone.)
2. **2d `r79` w20 task rows** (author/baseline/scribe) vs landed r79
   adjudicator: bookkeeping overlap; not double-counted.
3. **2d r20 spoken claim** ("round 1 is branch tip"): already superseded
   by the lane's own LOG correction; excluded as evidence, retained as
   a contradiction-ledger row (C26).
4. **audio r23/r24 (early)**: commit pins that resolve only in the
   pre-extraction origin repo (noted in the lane's own append-only
   correction) — hash citations are not resolvable in this checkout;
   the numeric content is retained, the hash is not treated as evidence.
5. **3d r2–r68 report files**: absent (not malformed). LOG-derived law
   rows are admitted with a `LOG` carrier marker; any downstream use
   requiring per-seat report evidence for those rounds must treat them
   as unverifiable from the report surface (§3.4).
6. **Frontier seats generally** (audio r79–r81, 2d r80–r81, 3d r89):
   pre-measurement reports, no adjudication — admitted only as queue
   entries (§3.2), never as laws.

## 7. Handoff notes

- This index is a cross-reference, not a re-derivation: every row points
  at the lane artifact that owns it. If a lane's correction lands later,
  the row here is stale by construction — re-run this seat after the
  next wave closeout rather than editing this file in place (the file is
  an artifact, corrections belong in the correcting round's own record).
- Highest-value next moves the surface itself names: close audio r78 and
  3d r88 adjudications; fold the r79–r81 / r80–r81 / r89 frontier
  scouts; collapse D1/D2/D3 duplicate scout classes into standing maps;
  and decide whether 3d r2–r68 evidence needs a durability pass (only
  the operator/lane can land that).
- No verdict, admit, promotion, edit, or runtime invocation was made by
  this seat. Stop before judgment.
