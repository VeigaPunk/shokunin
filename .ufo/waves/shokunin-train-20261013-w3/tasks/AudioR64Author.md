/skill:godspeed

Lane: audio (audio-shokunin) — training round 64; the lane's one declared axis-move is coverage: map the valid-bits-to-codec reclassification sweep under the ffmpeg bridge that r62 disclosed and r63 made deterministic. Established: with `act` routing forced (RIFF + byte[256]==0x84), ffmpeg's riffdec maps wValidBitsPerSample through `ff_get_pcm_codec_id` — valid17 -> pcm_s24le (3-byte samples, packet-residue count 3,839), valid24 -> pcm_s24le, valid32 -> pcm_s32le (4-byte, count 2,880); the count law is floor(per-packet bytes/width) summed over packets. Declared claim: the reclassification is a step map over valid-bits values — sweep wValidBitsPerSample through a controlled range (e.g. {1..16, 17..24, 25..32, 33..48} boundary values) under the SAME act-forced route, record per-value the ffmpeg-negotiated codec/sample-width and SoX decode sample count, and pin the boundary values where width steps. Land a tracked boundary-family pair iff a step boundary is established; else bounded UNKNOWN with eliminated hypotheses

Work from the lane worktree root ~/Projects/prymeagnt/audio. Paths below use the `.shokunin/audio/` prefix, which resolves into ~/Projects/shokunin/audio-shokunin.

Your seat: author (role executor).

You are the lane's ONLY tracked-file writer this round. First do causal scratch: extend the act-forced sweep over wValidBitsPerSample — for each candidate value in a boundary set (e.g. {1,7,8,9,15,16,17,20,23,24,25,31,32,33,40,48,64}), construct a RIFF file with that valid-bits value and byte[256]==0x84, then record (a) ffprobe's negotiated codec (bits_per_sample / codec_name pcm_s16le/s24le/s32le/u8/alaw/etc or error), (b) `sox <f> -n stat`-style sample count via the ffmpeg bridge, (c) compare vs a native `-t wav` forced decode (rejection or count). Find every step boundary in the range. THEN iff a step map is established, add minimal additive tracked changes in `.shokunin/audio/corpus/fixtures/` pinning 2-3 discriminating boundary pairs (e.g. the values straddling each width step) as a sweep control — never alter format_failures, thresholds, or prior modes; additive flags only. Verify: run the full 86-command ledger + new modes; report exact commands/exits/receipts.

Write scope — ONLY: your report `.shokunin/audio/reports/round-64/r64-author.md` plus scratch/receipts under `.shokunin/audio/corpus/live/r64-author/` (pass `--runs .shokunin/audio/corpus/live/r64-author/runs` to runners that accept it). Create the reports dir if missing. Nothing else.

Lane bounds: leaf member — no subagent dispatch except your single labrat.
Judged on: expansion, quality, discernment
Milestone: audio r64 + game-dev-2d r63 + game-dev-3d r72 (one axis-move per lane)

| godspeed
