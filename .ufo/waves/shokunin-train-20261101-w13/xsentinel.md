# XSENTINEL — fleet hygiene audit, wave-13

**Seat:** xsentinel (LEAF, report + confirmed-dead process kills only)
**Window:** 2026-10-14 ~12:51–12:56 local (-0300)
**Scope:** lane repos `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` under `~/Projects/shokunin` (parent `master@3de0575` w13 setup; lanes each own repo on `main`, excluded from parent by `.gitignore:*-shokunin/`)

**Headline:** **zero confirmed-dead trees — zero kills.** Both recounts (12:51, 12:53) show `wait_for_partner` fleet count = 0, open fifo fds = 0, and no timed-out orphans. All three rounds (audio r74, g2d r73, g3d r82) were LIVE throughout — g3d r82 seat trees run under `devin acp` (pid 3928555, alive). One bounded orphaned snapper (g2d r73-simplifier, pid 654178) reported INFO per w12 F1c convention. w12's ignore-fold recommendations **landed** (`audio@6f905c3`): `big.wav` and `measure-env/` are now covered — **zero untracked-unignored ≥20MB files fleet-wide** (w12 had 1). New largest-yet ignored tars: audio r74-baseline `head-1ba8103.tar` 344.8MB, g2d r73-baseline `HEAD-2dd108b….tar` 687.1MB. Tracked-file deltas all fit sanctioned conventions.

---

## F1 — Process census

### F1a. KILLED — none

No tree met the confirmed-dead bar (dead parent session + orphaned to init + no live reader). Two full sweeps of `/proc/*/wchan` (12:51, 12:53): the only `wait_for_partner` process is pid 1817 `uwsm aux app-daemon` — session infrastructure, not fleet. Scan of every live pid's `/proc/*/fd`: **zero open fds on any fifo** in `/tmp` or lane corpora. No orphaned `timeout`-wrapper children, no detached descendants holding pipes (only pipe-fd holders fleet-adjacent: omp session jsonl on 3984151, the snapper's own script fd, live r82-baseline's `/tmp/r82-godot-post2.log` stdout — all explained below).

w12's killed tree (3813/3808 r72-critic fifo writer) verified still absent; its residue fifo `/tmp/r72-critic-fifo2-sDv4/m.snd` remains on disk, inert, unopened.

### F1b. INFO — live seat trees (all under `devin acp` 3928555, alive, etimes ~2h10m)

| PID(s) | Tree | Lane/rung | Bound |
|---|---|---|---|
| 957585→957586→godot churn (969585→985201…) | `run_battery.py --godot … --runs r82-baseline/runs-post2 --probe-failing --probe-crash-exit --probe-stream-attribution --probe-tree-timeout` | g3d r82-baseline | seat-internal per-probe timeouts; stdout→`/tmp/r82-godot-post2.log` |
| 963039→963040(`timeout 900`)→963041→godot churn (969492→982477…) | `run_battery.py … r82-reviewer/godot-runs3` | g3d r82-reviewer | `timeout 900` |
| 961441→961442 | `sleep 120 && git log --oneline -3 && git status …` | g3d r82 | bounded poll |
| 969634→969635 | `sleep 240; ls reports/round-82/…; find r82-verifier -newermt '-4 min'` | g3d r82-verifier | bounded poll |
| 994327→994328 | `sleep 45 && git log --oneline -4 && …` | g3d r82 | bounded poll |

All PPID→3928555 (live session), all bounded or churning per rung. Godot children are headless `--script res://…` rung processes that rotate as the battery advances. INFO — do not kill.

### F1c. INFO — one orphaned bounded snapper

| PID | Tree | Lane/dir | Bound | State |
|---|---|---|---|---|
| 654178 (+transient `sleep 10` child) | `bash corpus/live/r73-simplifier/snapshot_loop.sh` | g2d r73-simplifier | `seq 1 360` × 10s ≈ 60min | live, etimes ~35min, ends ~13:18 |

Launcher reparented to 1573 (dead parent — same cosmetic orphan shape as w11/w12 watchers). Loop hashes `corpus/fixtures/{pygame_probe,pygame_battery,love_battery}.py` every 10s and snapshots on change — **reads tracked fixtures, writes only own-scope `r73-simplifier/snapshots/`** (log.txt shows fresh entries through 15:51 UTC ≈ 12:51 local — actively doing its job while the r73 round is in flight: r73-reviewer dir mtime 12:48, r73-simplifier 12:47). Not killed: bounded + in-scope + the round it monitors is live. Residual risk identical to w12 note: if its writes outlived the round it would still self-terminate at bound.

### F1d. Out-of-scope lanes (INFO only)

w12's other-lane pollers are **all gone** — `tameshi` poll.sh (321900/321902), `tsukuroi` poll.sh (332220/486051), `mado` watch (503969) absent; their rounds ended. `kimi` session itself (295525) still alive at 12:53 but holds no shokunin-lane children. Session noise unchanged: `uwsm-app` ×4 + `xdg-terminal-ex` ×1 zombies, uwsm aux daemon fifo-block.

### F1e. On-disk fifos & /tmp litter

- **Corpus fifos (all inert, zero openers — verified via `/proc/*/fd` sweep):** audio `r68-scout/fifo/` ×16, `frontier-pipewire/fifo{1,2,3}`, `r73-author/scratch/fifo{A,P,S.snd,Act.wav}`, `r73-verifier/{n,p}fifo`, `r73-boundary/logs/f{2,3}.fifo` = **27 fifos** (identical set to w12 — the r73 items belong to completed round dirs now). g2d/g3d: **zero** corpus fifos.
- **/tmp fifos ×32** (all inert): `r72-critic-fifo2-sDv4/m.snd` (w12 kill residue), `sanity-r70-*/`, `straceleg-r70-*` ×4, `tmp*/cz_nomatch.{wav,f32,txw,snd}` ×16 (fifo-typed files inside dead mktemp dirs), `tmp.xPz0KacFg4/m.aptx`, `r68c-GP0A/m.wav`, `f_act`, `f_act2`, `r67{rev_fifo,fifo-eqilxdsp/,test.wav,b.wav}`, `r65fifo.wav`.
- **/tmp census:** ~**829** fleet-pattern entries at depth 1 (broad pattern incl. `tmp*`; w12 counted ~364 with a narrower tag set — growth is real regardless: rounds r10→r82 residue accumulates, nothing sweeps). `tmp*` dirs: **75** at depth 1, churning minute-fresh from live seats. Fresh-seat files: `r82-godot-post{,2}.log`, `r82critic-timing{,2}`, `r74v2.out`, `r74fold.out`. Dead residue classes unchanged (fifo dirs above + w9–w12-era `r*`-tagged files). Sweep still recommended; size trivial but count growing ~2×/wave.

---

## F2 — Oversized artifacts (≥20MB, classified)

Method: `find -size +20M` per lane → `git ls-files --error-unmatch` / `git check-ignore` per file.

| File | Size (B) | Class | Verdict |
|---|---|---|---|
| g2d `r73-baseline/frozen/HEAD-2dd108b….tar` | **687,124,480** | IGNORED | **NEW** — largest-yet frozen tar (+3.7MB over r72's) |
| audio `r74-baseline/frozen/head-1ba8103.tar` | **344,842,240** | IGNORED | **NEW** — largest-yet audio head.tar |
| audio `r73-baseline/frozen/head-f5d7faf.tar` | 344,576,000 | IGNORED | standing (w12) |
| audio `r70-{simplifier,baseline}` head tars ×2 | 278,548,480 ea | IGNORED | standing |
| audio `r69-baseline/frozen/head-7b8d423.tar` | 177,244,160 | IGNORED | standing |
| audio `r71-critic/big.wav` | 52,920,078 | **IGNORED** (was UNTRACKED-NOT-IGNORED) | **flipped by w12-fold rule `corpus/.gitignore:18`** — zero unignored ≥20MB files fleet-wide |
| g2d r{63,66,67,69,70,72,73} fixture re-extractions | 73,703,800 ea ×49 | IGNORED | standing + r73 instance ×7 |
| g2d `r65-boundary/edge-verdicts.json` | 122,535,352 | IGNORED | standing |
| g2d tracked `r25-*/fixture.x86_64` ×7 | 73,703,800 ea | TRACKED | standing (one shared blob) |
| g2d r{68,69,70,72,73}-baseline frozen tars | 655–687MB ×6 | IGNORED | standing + r73 |
| g3d | 0 files ≥20MB | — | clean (4th wave running) |

**Untracked-unignored ≥20MB: ZERO** (audio also has zero ≥1MB unignored; the only audio unignored stray is 0-byte `pwcat_tmp.err`, mtime 11:40 — trivial probe residue). **Tracked ≥20MB:** unchanged — only the 7 known `fixture.x86_64` blobs.
**Disk:** g2d **9.8GB** (+1.4), audio **3.3GB** (+0.4), g3d **532MB** (+49M) resident vs w12. **Severity:** MEDIUM disk (cumulative ~13.6GB across lanes); LOW git-risk — ignore lattice held on every new instance.

---

## F3 — Ignore-gap shapes

- **`measure-env/` — GAP CLOSED for new instances.** w12 fold commit `6f905c3` added `live/*/measure-env/` (`corpus/.gitignore:19`): r73-baseline (779 files) and r74-baseline (780) instances now IGNORED with **0 tracked** — the drift path w12 flagged is shut. **Legacy standing:** `r69-baseline` (766), `r69-verifier` (777), `r70-baseline` (776), `r72-baseline` (29) measure-env trees are **fully committed env clones — 2,348 tracked files total** (w12 noted only `__pycache__` spill; recount shows the clones landed wholesale). History-only now; the rule prevents recurrence. Optional remediation if operators want index hygiene: `git rm -r --cached` the four legacy trees (they'd stay ignored).
- **`runs/` at seat depth (audio) — shape persists and grew:** unignored seat-local `runs/` dirs at `r73-boundary`×4, `r73-scout`×5, `r73-verifier`×2, **`r74-boundary`×29, `r74-scout`×7, `r74-verifier`×2** (49 files, all small). Distinct from the sanctioned tracked ledger `corpus/live/runs/` (which gained normal w13 entries). Still LOW; if it keeps growing a `live/*/runs/` — careful, that name collides with the sanctioned ledger — better `live/r*/{boundary,scout,verifier}/runs/` or per-seat convention.
- `frozen/`, `frozen-extract/`, `*tree*/` lattices: verified matching every new instance this wave (g2d r73 tar+extracts, audio r74 tar → IGNORED).
- g2d untracked-unignored = **17 entries**, all convention (r73 seat dirs, r72 snapshot dirs, r71 reports). g3d = **1** (`reports/round-82/`). Parent = **3** (`.ufo/reports/round-{72,73}` + w12 xsentinel.md pending operator commit). `pwcat_tmp.err` noted above.
- **Severity:** LOW — the w12 MEDIUM (measure-env) is resolved; legacy tracked clones are history, not live drift.

---

## F4 — Tracked `.pyc` drift

| Repo | w12 | w13 | Delta |
|---|---|---|---|
| parent | 3 | 3 | 0 |
| audio | 40 | 40 | 0 |
| g2d | 43 | 43 | 0 |
| g3d | 0 | 0 | 0 |

On-disk `__pycache__/` dirs: parent 332→**393** (+61), audio 86→89 (+3), g2d 239→**296** (+57), g3d 4→5 (+1). **Zero new tracked `.pyc` this wave** — first zero-delta wave; index drift paused while on-disk bytecode churn continues at the established rate. One tracked pyc was recompiled in place: `audio corpus/fixtures/__pycache__/measure_audio.cpython-314.pyc` shows `M` (probe imports rewrote it — bytecode churn on an already-tracked file, not a new commit). **Severity:** LOW.

---

## F5 — Tracked-file mutations (`git status` per lane)

| Lane | Head | Tracked deltas | Attribution |
|---|---|---|---|
| parent | `master@3de0575` | 0 | clean; 3 untracked `.ufo/` report files pending |
| audio | `main@6f905c3` | `M corpus/fixtures/__pycache__/measure_audio.cpython-314.pyc` | tracked-pyc recompile (F4). No LOG/SCORECARD delta this window (r74 bookkeeping landed in `49747ba`+ earlier). w12's flagged measure-env fixture edit was committed inside the r72 fold — in-scope convention held. |
| g2d | `main@1275746` | `M r72-simplifier/snapshots/log.txt` (+5), `M r72-simplifier/watch.log` (+2) | **stale uncommitted appends** from w12-era bounded watchers (last lines 15:35:26Z = 12:35 local; both files static since — no live writer, verified by fd sweep). Residue, not active mutation. |
| g3d | `main@e79e004` | `M LOG.md` (+19), `M SCORECARD.md` (+10) | sanctioned ledger convention during live r82. w12's flagged `M bpy_battery.py`/`bpy_sync_probe.py` deltas landed in `65b2f26`/`fd75567` — now committed, clean. |

No cross-lane writes, no writes into other waves' dirs, w13 wave dir untouched by lanes. **Severity:** LOW — every delta fits declared conventions; the only novelty is the w12 `.gitignore` fold commit itself (sanctioned ops action closing F2/F3).

---

## Kill log (only mutations this seat may perform)

**Zero kills, zero mutations this wave.** No tree met confirmed-dead criteria at either recount: fifo-blocked fleet = 0, open fifo fds = 0, orphaned-to-init fleet = 1 (654178 — bounded, in-scope, live round, INFO not kill), timed-out orphans = 0.

**Live processes reported but deliberately not killed:** all F1b g3d r82 seat trees (children of live `devin acp` 3928555), F1c snapper 654178, kimi session (out of scope).

---

## Severity roll-up

| # | Finding | Severity | Status |
|---|---|---|---|
| F1a | confirmed-dead trees | — | **none; 0 kills** |
| F1b | g3d r82 seat trees under live devin acp | INFO | live, bounded, in-scope |
| F1c | orphaned g2d r73 snapper 654178 (bounded, in-scope) | LOW | self-terminates ~13:18 |
| F1d | w12 other-lane pollers | INFO | all exited; kimi idle |
| F1e | ~829 /tmp entries, 32 /tmp fifos, 27 inert corpus fifos (audio only) | LOW | litter class keeps growing; sweep recommended |
| F2 | NEW largest tars (g2d 687MB, audio 345MB) all IGNORED; **untracked-unignored ≥20MB = 0** | MEDIUM disk / LOW git | big.wav gap closed by w12 fold |
| F3 | `measure-env/` rule landed; legacy 2,348 tracked clone files; seat `runs/` unignored (49 files, growing) | LOW | new-instance drift shut |
| F4 | tracked `.pyc`: **zero delta** (86 standing); on-disk `__pycache__` +122 dirs | LOW | drift paused |
| F5 | tracked deltas: ledger (g3d), stale watcher residue (g2d), pyc recompile (audio) | LOW | all convention |

**Census receipts:** two `/proc` wchan+fd sweeps (12:51, 12:53), per-lane `find -size +20M` + `git check-ignore -v` classification, `git ls-files` measure-env counts, `git status`/`diff` per repo, `du -sh` disk figures — all captured live this session. w12 standing items re-measured: kill-residue fifo persists inert; every w12 watcher confirmed exited; w12 F3 MEDIUM closed; F4 delta zero.

*godspeed.*
