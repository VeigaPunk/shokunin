/skill:godspeed

Lane: audio (audio-shokunin) — training round 64; the lane's one declared axis-move is coverage: map the valid-bits-to-codec reclassification sweep under the ffmpeg bridge that r62 disclosed and r63 made deterministic. Established: with `act` routing forced (RIFF + byte[256]==0x84), ffmpeg's riffdec maps wValidBitsPerSample through `ff_get_pcm_codec_id` — valid17 -> pcm_s24le (3-byte samples, packet-residue count 3,839), valid24 -> pcm_s24le, valid32 -> pcm_s32le (4-byte, count 2,880); the count law is floor(per-packet bytes/width) summed over packets. Declared claim: the reclassification is a step map over valid-bits values — sweep wValidBitsPerSample through a controlled range (e.g. {1..16, 17..24, 25..32, 33..48} boundary values) under the SAME act-forced route, record per-value the ffmpeg-negotiated codec/sample-width and SoX decode sample count, and pin the boundary values where width steps. Land a tracked boundary-family pair iff a step boundary is established; else bounded UNKNOWN with eliminated hypotheses

Work from the lane worktree root ~/Projects/prymeagnt/audio. Paths below use the `.shokunin/audio/` prefix, which resolves into ~/Projects/shokunin/audio-shokunin.

Your seat: reviewer (role reviewer).

Non-author audit of round 63. Re-execute pivotal r63 evidence fresh: the 86-command ledger in `reports/round-63/r63-verifier.md` (or adjudicator) — replay serially; verify 43 exit0 / 43 exit1 shape; verify pair_route_84 routes `act`/(ffmpeg) with count 3,839 and pair_route_00 routes native `wav` fatal exit 2; verify the formats.c citation claims (AUTO_DETECT_SIZE 257, CHECK rows for act/wav ordering — if the extracted source tree is pruned, use the retained tarball); verify commits `1a97b0e`/`37d4c57` resolve and are ancestors of HEAD. Record agree/disagree per checked claim.

Write scope — ONLY: your report `.shokunin/audio/reports/round-64/r64-reviewer.md` plus scratch/receipts under `.shokunin/audio/corpus/live/r64-reviewer/` (pass `--runs .shokunin/audio/corpus/live/r64-reviewer/runs` to runners that accept it). Create the reports dir if missing. Nothing else.

Lane bounds: leaf member — no subagent dispatch.
Judged on: expansion, quality, discernment
Milestone: audio r64 + game-dev-2d r63 + game-dev-3d r72 (one axis-move per lane)

| godspeed
