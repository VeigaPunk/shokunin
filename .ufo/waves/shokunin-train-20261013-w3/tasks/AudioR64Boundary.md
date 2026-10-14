/skill:godspeed

Lane: audio (audio-shokunin) — training round 64; the lane's one declared axis-move is coverage: map the valid-bits-to-codec reclassification sweep under the ffmpeg bridge that r62 disclosed and r63 made deterministic. Established: with `act` routing forced (RIFF + byte[256]==0x84), ffmpeg's riffdec maps wValidBitsPerSample through `ff_get_pcm_codec_id` — valid17 -> pcm_s24le (3-byte samples, packet-residue count 3,839), valid24 -> pcm_s24le, valid32 -> pcm_s32le (4-byte, count 2,880); the count law is floor(per-packet bytes/width) summed over packets. Declared claim: the reclassification is a step map over valid-bits values — sweep wValidBitsPerSample through a controlled range (e.g. {1..16, 17..24, 25..32, 33..48} boundary values) under the SAME act-forced route, record per-value the ffmpeg-negotiated codec/sample-width and SoX decode sample count, and pin the boundary values where width steps. Land a tracked boundary-family pair iff a step boundary is established; else bounded UNKNOWN with eliminated hypotheses

Work from the lane worktree root ~/Projects/prymeagnt/audio. Paths below use the `.shokunin/audio/` prefix, which resolves into ~/Projects/shokunin/audio-shokunin.

Your seat: boundary (role revenger).

Scratch-only recon for the NEXT disclosed surface: the non-USING_FFMPEG build behavior and the stdin autodetect path retained UNKNOWNs from r63. Probe: (a) does SoX read stdin into the same 257-byte detection buffer (pipe the pair_route_84.wav through `cat | sox - -n stat`) — same act predicate or a different code path? (b) the `goto error` no-fallback claim — construct an act-triggered file whose bytes past offset 256 are parseable by NEITHER ffmpeg nor au and observe the exact terminal error ordering; (c) can an act-routed file carry a SECOND autodetect (e.g. au magic) such that the au reader on the ffmpeg pipe re-claims it? Report mechanism evidence with commands/outputs.

Write scope — ONLY: your report `.shokunin/audio/reports/round-64/r64-boundary.md` plus scratch/receipts under `.shokunin/audio/corpus/live/r64-boundary/` (pass `--runs .shokunin/audio/corpus/live/r64-boundary/runs` to runners that accept it). Create the reports dir if missing. Nothing else.

Lane bounds: leaf member — no subagent dispatch.
Judged on: expansion, quality, discernment
Milestone: audio r64 + game-dev-2d r63 + game-dev-3d r72 (one axis-move per lane)

| godspeed
