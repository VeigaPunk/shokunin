# audio round 71 — coverage/runtime-breadth: second decoder (ffmpeg/ffprobe) on the transport corpus

**Stamp.** Audio lane, round 71 (devin host, wave `shokunin-train-20261101-w10`; massacre conditions — 25/26 seats died to the free-model pool; operator-substituted author + post-landing v2 seats). Lane commit: work `7b9e75d`.

## Work performed

`--probe-ffprobe-transport-r71`: 9 tracked members (5 identical-byte extsuffix + posttable/txw + dec_act/dec_hcom) × 4 transports under `ffprobe` detection + `ffmpeg -v error -i -f null -` decode. New receipt family `ffprobe_*_r71_probe`; insertion-only — prior 120-mode ledger untouched.

## Measured

**Claim CONFIRMED**: ffmpeg content-probes on every transport; suffix plays no role — all 7 no-match members reject "Invalid data" on all 4 transports where SoX split them 5 ways by name. dec_act→`wav`, dec_hcom→`hcom` transport-invariant incl. fifo. The r68/r69 named/suffix partition is SoX-specific — honest scope narrowing.

**Fixture mechanics learned the hard way:** (a) a consumer chain (ffprobe then ffmpeg on the same fifo) needs a fresh fifo+writer PER process — the second process opens after the first writer exits (the r67 open-#2 phenomenon, generalized); (b) `pipe:` over a seekable redirected fd must get a FRESH fd per leg — shared-offset made a phantom detect-ok/decode-fail fork (operator self-caught pre-land); (c) `pipe:` over a seekable fd == over a true pipe on n9.0.1 — redirected_fd is not a distinct ffmpeg transport class. probe_score field absent on n9.0.1 (recorded null).

## Remaining

Verifier/critic/boundary v2 seats dispatched post-landing; 121-mode byte-identity ledger in flight. Prior ledger rows byte-stable by insertion-only construction.
