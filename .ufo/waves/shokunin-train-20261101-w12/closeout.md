# Wave-12 closeout — composed mechanisms (fd1-inheritance x block-buffering)

Wave: `shokunin-train-20261101-w12`. Registry: `registry.json`. Closed 2026-10-14 ~15:15Z.

## Results

| lane | round | verdict | commits | headline |
|---|---|---|---|---|
| audio | r73 | ADMIT-corr | `febf34b` + `3b4c3b7` | consumer class joined: 2 member-local forks, different drivers — mpv x dec_hcom inverted-seek (lavf-synthetic EPERM, 0 failing syscalls) + pw-cat x .snd name-axis (inherits libsndfile fallback); ops surface pinned (daemon gate, writerless-fifo KILL, playback-pacing 4.03s/4s, trickle->EOF); class-polarity claim falsified corpus-wide |
| g2d | r72 | ADMIT | `fee5563` + `2dd108b` | reorder fabrication CONFIRMED — fd1-OWNER's buffering mode is the variable (buffered->prefix_reorder, -u/flush/env->midline_splice, late->append); mechanism libc/CPython-general, not engine-specific; PYTHONUNBUFFERED ambient leak fixed (env=CHILD_ENV + strip) |
| g3d | r81 | ADMIT | `65b2f26` + `fd75567` + `31cf56a` | bpy reorder CONFIRMED with parse-survival contract (gluevictim dropped, physical last-wins); PYTHONUNBUFFERED inert on bpy (needs --python-use-system-env); evalcat bare catalogue 8->14 under falsifier |

## Model-mix accounting

deepseek-v4-1-flash-max carried scout/critic/scribe/simplifier/reviewer seats via `-ds` profiles; SWE-2 on authors/baselines/verifiers. Rate-limit wave killed: audio r73 author+verifier v1, xsentinel v1, xconnector v1 — author substituted by operator (disclosed), verifier+sentinel respawned on -ds, connector respawned on subagent_explore. flashseat skill: dead end (no skill tool in subagents); `-ds` profiles remain the only deepseek path.

## Fleet hygiene (xsentinel)

w11's 75-orphan ffmpeg class CLOSED — r73 probes self-reap; one dead r72-critic fifo tree killed (scoping-bug writer, ~37min); `r71-critic/big.wav` 52.9MB = only unignored >=20MB offender; measure-env/ ignore gap standing (MEDIUM).

## Wave-13 frontier bank (xconnector pending)

love.physics in-step contact lattice; PhysicsServer3D edge-0 + Jolt; pw-cat zero-sink/--target-0 hang classes; dead-surface census (bpy msgbus/QUIT, love callbacks, link-gated sinks); infix topology (paced mid-chunk interleave); detach-child EOF-hold; non-Python fd1-owner test (is reorder libc-general?); lavf demuxer breadth (wv/aifc seek-gated siblings of hcom).
