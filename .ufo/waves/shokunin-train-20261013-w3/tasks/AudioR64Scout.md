/skill:godspeed

Lane: audio (audio-shokunin) — training round 64; the lane's one declared axis-move is coverage: map the valid-bits-to-codec reclassification sweep under the ffmpeg bridge that r62 disclosed and r63 made deterministic. Established: with `act` routing forced (RIFF + byte[256]==0x84), ffmpeg's riffdec maps wValidBitsPerSample through `ff_get_pcm_codec_id` — valid17 -> pcm_s24le (3-byte samples, packet-residue count 3,839), valid24 -> pcm_s24le, valid32 -> pcm_s32le (4-byte, count 2,880); the count law is floor(per-packet bytes/width) summed over packets. Declared claim: the reclassification is a step map over valid-bits values — sweep wValidBitsPerSample through a controlled range (e.g. {1..16, 17..24, 25..32, 33..48} boundary values) under the SAME act-forced route, record per-value the ffmpeg-negotiated codec/sample-width and SoX decode sample count, and pin the boundary values where width steps. Land a tracked boundary-family pair iff a step boundary is established; else bounded UNKNOWN with eliminated hypotheses

Work from the lane worktree root ~/Projects/prymeagnt/audio. Paths below use the `.shokunin/audio/` prefix, which resolves into ~/Projects/shokunin/audio-shokunin.

Your seat: scout (role scout).

Recon only. Map the r62/r63-established routing surface for this round's sweep: read `corpus/knowledge/2026-10-13-sox-act-autodetect-predicate.md` + the r62 packet-residue knowledge entry + `reports/round-63/` seat reports. Locate how wValidBitsPerSample is authored into a WAV fixture in `corpus/fixtures/build_artifacts.py` (find the pair_valid_17/24/32 builders and how valid-bits lands at byte 38 / fmt chunk). Verify by `ffprobe` which pcm codec ffmpeg negotiates for each existing pair (s16le/s24le/s32le). Report file:line pointers for the builder entry point an extended sweep needs, plus the packetization evidence (r62: packets 8192+3328 bytes; per-packet floor(bytes/width) sum).

Write scope — ONLY: your report `.shokunin/audio/reports/round-64/r64-scout.md` plus scratch/receipts under `.shokunin/audio/corpus/live/r64-scout/` (pass `--runs .shokunin/audio/corpus/live/r64-scout/runs` to runners that accept it). Create the reports dir if missing. Nothing else.

Lane bounds: leaf member — no subagent dispatch.
Judged on: expansion, quality, discernment
Milestone: audio r64 + game-dev-2d r63 + game-dev-3d r72 (one axis-move per lane)

| godspeed
