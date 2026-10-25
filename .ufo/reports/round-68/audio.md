# audio round 68 — depth move: post-table fallback fork + pipe-refusal member

**Stamp.** Audio lane, round 68 (devin host, wave `shokunin-train-20261014-w7`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `6c91040`, report-last `7b8d423` — identity `audio-shokunin <audio@shokunin.local>`.

## Work performed

Pinned what SoX_ng does when autodetect's CHECK table misses entirely, per transport — plus the first tracked pipe-refusal member. `build_artifacts.py` +46/−1 (`build_ui_posttable_r68_probe` builds `posttable_nomatch.wav` — no CHECK row — and `txw_piperefuse.wav` — detected `txw`, reader refuses pipes); `measure_audio.py` +34/−3 (members + `--probe-transport-posttable-nomatch-r68` / `--probe-transport-txw-piperefuse-r68`). Ledger 112→114 rows (49 exit-0 / 65 exit-1), prior-112 byte-identical.

**Declared claim FALSIFIED-as-stated** (four-seat convergence: scout 13×8, critic 6×4+strace, boundary 19-arm 229-leg, scribe own-matrix): post-table verdicts partition on the **named** axis `{file,fifo_path}` vs `{stdin_pipe,redirected_fd}` via extension dispatch — `ft->seekable` is never read post-table; the redirected-fd rewind succeeds and buys nothing (no second classification pass); prefetch bytes are pending-buffer-replayed, not consumed. The predicted seekable partition is real but lives inside the txw reader: `{file,redirected_fd}` decode 64 samples vs `{stdin_pipe,fifo_path}` `input must be a file, not a pipe` — a reader-level `!seekable` gate.

Beyond the claim: `.snd`-named members arm an ext-gated CHECK row → **detection itself forks on namedness** — the first counterexample to r67's detection-invariance (now bounded to non-ext-gated members). 5 post-table verdict classes enumerated.

## Landed changes

- Members: `corpus/live/round-68/posttable_nomatch.wav` (512B), `txw_piperefuse.wav` (128B) — both byte-identical to verifier's verbatim rebuild.
- `corpus/knowledge/2026-10-14-sox-posttable-fallback.md`; `reports/round-68/` all 9 seat reports + adjudicator.
- Simplifier: 9/9 deletion candidates load-bearing (`.wav` extension proven load-bearing — mkdtemp-nonce nondeterminism without it); no extraction warranted.

## Before → after measurements

| metric | before | after |
|---|---|---|
| post-table fallback | unmeasured | name-resolved extension dispatch; 5 verdict classes; `seekable` never consulted |
| seekable fork locus | decode-stage only (r67) | + reader-level `!seekable` gate (txw/smp) |
| detection invariance | universal over 10 members (r67) | bounded — `.snd` ext-gated row forks detection on name |
| ledger | 112 rows | **114 rows**, prior-112 byte-identical |

## SHONEN

- [x] Declared falsifiable axis-move (depth); falsification recorded honestly — corrected mechanism is what landed
- [x] Named non-author replay — **verifier AGREE 5/5** on `6c91040` (independent 114-cmd replay byte-identical; probes deterministic ×5)
- [x] No axis harmed — prior-112 receipts byte-identical (verifier-confirmed), additive flags
- [x] Bounded claims; UNKNOWNs retained (serial-execution stability; starved-fifo protocol artifact; ext-gate bound to measured row; no production inference)
