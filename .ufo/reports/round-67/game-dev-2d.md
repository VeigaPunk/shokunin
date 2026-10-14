# game-dev-2d round 67 — depth/coverage move: classify_streams ↔ merged per-channel divergence map

**Stamp.** 2D lane, round 67 (devin host, wave `shokunin-train-20261014-w7`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `d44ba86`, load-bearing fix `9e946c9`, report-last `1101cb3` — identity `game-dev-2d-shokunin <g2d@shokunin.local>`.

## Work performed

Mapped `classify_streams`' per-channel divergence from merged `classify_process` as a measured axis — opt-in probe only, default path untouched. `run_battery.py` +~265 (`streamdiv_*` meta inside `--probe-stream-attribution`: 7 real-Godot arms + 6 allowlist reclasses + pair dual, 20 discriminations, 9-row `divergence_table`); `stream_attribution_probe.gd` +58 (`--{stdout,stderr}-error`, `--stderr-structured`, `--sig-on-stderr`, `--seam-{error,script,sig}`).

**Measured: 12/27 arms divergent**, rep-stable, four families — ABSORB (stdout `ERROR:` invisible to streams: stdout examined only for signature + 2 blob tokens); STRICT (every non-empty stderr line must match `allowed_stderr`; signature channel-pinned to stdout; seam-fabricated signature; allowlist+noise; `ERR\nOR:` evasion; merged-only structured entry); SEAM×ALLOWLIST (exempted stderr fragment completes phantom `ERROR:`/`SCRIPT ERROR:` line existing only in the concat); AGREE (stderr `ERROR:` both-reject; allowlisted stderr both-absorb; blob tokens both-reject; exit/error short-circuit first). **The shipped reject arm itself diverges** (`g_stream_reject` T/F — latent since r19, un-named until now). Boundary: seam is stdout-tail|stderr-head **only** — reverse order unfabricatable.

Critic falsified "exactly the stream-attribution axis" — the corrected claim is the enumerated four-family map. Simplifier found `sd_sig_head` dead → integration made it load-bearing (`raw_stdout.endswith(sd_sig_head)` seam-tail pin, `9e946c9`).

## Landed changes

- `corpus/lessons/r67-stream-classifier-divergence.md`; `reports/round-67/` all 9 seat reports + adjudicator.
- Scribe: 54 real-pipe records via own extraction driver (sha-convergent, rep-stable); verified author 9-row table row-for-row.

## Before → after measurements

| metric | before | after |
|---|---|---|
| stream-classifier divergence | observed-adjacent (r19 latent, r65 re-pinged) | enumerated 4-family map, 12/27 arms, clause-level mechanism each |
| battery (flagless) | 88/88 | 88/88 (unchanged — opt-in flag) |
| battery (flagged) | — | **89/89**, discriminations 20/20, table 9/9 |
| shipped reject arm | assumed consistent | measured divergent (T/F) — production behavior since r19 |

## SHONEN

- [x] Declared falsifiable axis-move (depth/coverage); wording falsification absorbed (enumeration over "exactly")
- [x] Named non-author replay — **verifier AGREE 5/5** on `9e946c9` (88/88 + 89/89 + 34/34 + 20/20 + 9/9 rows)
- [x] No axis harmed — prior 88 rows stable, classifiers byte-identical (3 seats, AST+sha), opt-in flag only
- [x] Bounded claims (classifier-level verdicts; 4.7.2 headless; POSIX pipes; latent in default battery); real captured pipe bytes throughout
