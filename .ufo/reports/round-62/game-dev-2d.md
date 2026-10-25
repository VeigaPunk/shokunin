# game-dev-2d round 62 — coverage move: pipe-EOF descendant-timeout classification

**Stamp.** game-dev-2d lane, round 62 (devin host, wave `shokunin-train-20261013-w2`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `81a100c`, report-last `edbd945` — identity `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`.

## Work performed

Formalized the r61-boundary finding as a tracked surface: `communicate(timeout)` is a **completion + pipe-drain deadline**, not child liveness — a clean-exiting Godot child whose spawned descendant holds the captured pipes is still TIMEOUT at the bound (`return ≈ min(bound, max(child_exit, last_fd_EOF))`), and the timeout kill is direct-child-only so the descendant orphans. Fixture `descendant_pipe_probe.gd` with `--spawn-hold` (meta-driven, hold ~7s inside a 3.0s bound — inside the misattribution window) and `--spawn-detach` (CASES control: fds detached at exec → child-exit-bound PASS while the descendant silently orphans).

## Landed changes

- `corpus/fixtures/descendant_pipe_probe.gd` (new) + `run_battery.py` **+142/−0** — CASES `descendant_pipe_detached_control` + unconditional meta `probe_descendant_pipe_eof` (7 discriminations; `poll()`-at-timeout child-death proof load-bearing). `run_process`/`classify_process`/`classify_streams`/`classify_audio_process` byte+ast identical vs r61.
- `corpus/lessons/r62-pipe-eof-timeout.md` — semantics, decision table, tracked-surface map, retained UNKNOWNs.
- `reports/round-62/` — 8 seat reports + verifier + adjudicator.
- Integration corrections on the committed state: post-exit write now **gated on kernel reparenting** (`/proc/self/stat` ppid flip — closes the critic's presence-only +0.05s forgery class; a `kill -0` first attempt deadlocked on zombie-until-bound and was corrected); detach `sleep 5`→`8` (simplifier's thin-margin gate).

## Before → after measurements

| metric | before | after |
|---|---|---|
| seven-flag battery | 92/92 (frozen `08d80dc`) | **94/94** (author + integration + verifier runs) |
| prior rows | — | **92/92 field-identical** on the 7-field tuple |
| descendant-held-pipe classification | probed scratch-only | tracked: hold arm TIMEOUT with `child_exit_at_timeout=0`; detach control PASS 0.4s |
| forgery resistance | — | 8/9 critic mutants reject; the 1 slip (pre-death write) closed at integration; kernel-side ppid-flip traced by verifier |

## SHONEN

- [x] Declared falsifiable axis-move (coverage), evidence over prose
- [x] Named non-author replay passed all old + new classifications (94/94, sha `7a4ee384…`)
- [x] No axis harmed (additive-only; 92 prior rows field-stable; classifier untouched)
- [x] Bounded claims; UNKNOWNs retained honestly (signal origin, receipt-vs-semantics, reaping)

Per-axis verdicts (Sol): coverage **improved locally**, depth **improved locally**, calibration **unchanged**. Learning trends: expansion/quality/discernment all **improved**. No promotion action.
