# XSENTINEL — fleet hygiene audit, wave-11

**Seat:** xsentinel (LEAF, report-only, no mutations)
**Window:** 2026-10-14 ~11:18–11:26 local (-0300)
**Scope:** `~/Projects/shokunin` (parent, `master@f6e28b1`→`42e8c23`) + lane repos `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` (each own git repo, `main`, excluded from parent by `.gitignore:*-shokunin/`)

**Headline event:** the ~60-process orphan standing-followup was measured at **75 ffmpeg + 3 strace trees at 11:18–11:22**, then an **external sweep killed all of them mid-audit** (zero media-tool processes at 11:24:44). This seat made no mutations; the kill was not mine. Both observations are reported.

---

## F1 — Stray process census

### F1a. 75 orphaned ffmpeg, FIFO-blocked (SEEN 11:18–11:22, GONE 11:24)

- **Command:** `ps -eo pid,ppid,etimes,stat,comm` / `ps -eo etimes,args | grep '[f]fmpeg '`
- **Evidence:** 75 `ffmpeg` processes, all PPID=1573 (`/usr/lib/systemd/systemd --user` → reparented orphans; launching seats exited). All STAT=`S`, wchan=`wait_for_partner` — blocked in FIFO open/read. Age histogram (etimes): 24× ~9h, 2× ~4h, 9× ~3h, 38× ~2h, 1× ~1h, 1× <1h.
- **Source attribution (argv `-i` paths):**
  - r67-era ≈ 21: `corpus/live/r67-boundary/probes/.fifo_probe` ×10, `.race_fifo` ×5, `r67test.wav`, `/tmp/r67b.wav`, `/tmp/r67c.wav`, `/tmp/f_act` ×2, `r67-author/fifo/pair_preempt_act.wav` ×2
  - r69: `/tmp/r69-starve-*/{st,lz}.{dts,aptx}` ×8
  - r70: `/tmp/r70simp-*/pair_dec_act.wav` ×28, `/tmp/holdladder-oneshot-*` ×10, `/tmp/open2-hold-0-*` ×3, `/tmp/fifo-hold-r70-*` ×1
  - r71: `/tmp/r71-scout-fifo-zlcngrf_/txw_piperefuse.wav` ×1 (`-f null -`), `/tmp/tmp.xPz0KacFg4/m.aptx` ×1
  - misc: `probes/.fifo_act.wav` ×2 (relative-path argv)
- **Mechanism:** probes spawn `ffmpeg -i <fifo|wav> -f au -` readers with `-nostdin` and no timeout/reap; when the harness exits, the reader stays blocked forever on the FIFO (or on a dead pipe with SIGPIPE disposition). Matches "pre-existing ffmpeg orphans ~60 from r67–r70 seats" in w10 `closeout.json:standing_followups` — r71 added ~13 more before the sweep.
- **State now:** `pgrep -xc ffmpeg` → **0** at 11:24:44. Dead: also all `ffprobe/sox/pw-cat/love` (a transient `love` and 2 `blender` seen in-window were live r80-verifier/g2d seat work with live parents — not orphans).
- **Impact:** resolved externally; residue remains (F1c). Root cause unaddressed — next fifo probe round re-leaks.
- **Severity:** was HIGH (81 stuck procs); now residual LOW until next probe round.

### F1b. `timeout strace sox` deadlock trees (SEEN, GONE)

- PIDs 1965371+1965372 (`timeout 10 strace … sox /tmp/r67c.wav -n stat`, etimes 33079s), 1970028+1970029 (`timeout 6 strace … /tmp/f_act`, 33047s), 3097763 (`strace … /tmp/tmp.xPz0KacFg4/m.aptx`, 12205s).
- `timeout` sat in `sigsuspend`, `strace` in `do_wait` — **elapsed 9.2h / 9.2h / 3.4h vs. declared 10s/6s timeouts**: the deadline mechanism itself deadlocked (ptraced/tracee-child wait is not interruptible by the timer path used here). Any harness relying on `timeout N strace … <fifo-blocked-cmd>` does not bound.
- All three gone by 11:24. Strace outputs persist: `/tmp/r67fifo.strace`, `/tmp/strace_act.txt`, `runs/strace-aptx-fifo.txt` (relative).

### F1c. Residual leaks still live at close

| PID(s) | What | State | Bound? |
|---|---|---|---|
| 4145249 | `bash -c` frontier-pipewire probe (`pw-cat`/`cat > fifo3`) | `wait_for_partner`, 811s, **0 children** — stuck past its own `timeout -s KILL 8` wrappers | Unbounded |
| 1073+1075 | g2d r71-scribe `watch.sh` launcher + loop | `do_wait`, 348s | Bounded (~1h, `seq 1 240`×15s) |
| 3917474+3917477 | audio r71-simplifier `watch.sh` tree | `do_wait`, 2934s | Bounded (~1.3h) |
| 4193461+4193464 | g2d r71-simplifier `watch.sh` tree | `do_wait`, 378s | Bounded (~50min) |

- Launcher parses as `{ …; nohup bash watch.sh … } & echo` — the `&&`-chain including `nohup bash watch.sh` went to background, so the `bash -c` wrapper `do_wait`s on the watcher for its full lifetime (2 procs per watcher instead of 1 detached). Cosmetic doubling, but watchers also **outlive their seats** writing `watch.log` (in-scope path, dead-author process).
- Zombies (session noise, not fleet): `uwsm-app` ×4, `xdg-terminal-ex` ×1.
- **/tmp litter:** ~209–214 files matching `r6*`/`r7*`/`holdladder|open2|fifo-hold|starve|simp` remain under `/tmp` (incl. FIFOs `/tmp/f_act`, `/tmp/r67rev_fifo`); the `/tmp/r70simp-*`/`r69-starve-*`/`holdladder-*`/`open2-hold-*` dirs are gone. On-disk FIFO `corpus/live/frontier-pipewire/fifo3` remains (the stuck bash is attached).

**Smallest remediation:** probe harnesses should `timeout -k` every fifo-reader spawn **and** reap (or `exec` readers under a supervised group + `kill -- -$pgid` on exit); delete `watch.sh` respawn pattern or write it single-process (`exec nohup …`); one-line `/tmp/r6*|r7*` litter sweep in the next hygiene pass.

---

## F2 — Oversized tracked files & ignore gaps

**Method:** per repo — `git ls-files -z | xargs -0 stat -c '%s %n'` (tracked ≥50MB), `git rev-list --objects --all | git cat-file --batch-check` (history blobs ≥50MB), `find -size +50M` classified TRACKED / IGNORED(check-ignore) / UNTRACKED-NOT-IGNORED, then re-run at ≥10MB.

| Repo | Tracked files ≥50MB (worktree) | History blobs ≥50MB | `.git/objects` |
|---|---|---|---|
| parent | 0 | 0 | 3.8M |
| audio | 0 | 0 | 32M |
| g2d | **7** | **1 unique** (`73,703,800 B`) | 35M |
| g3d | 0 | 0 | 1.6M |

### F2a. TRACKED ≥50MB — g2d `fixture.x86_64` ×7 paths, one shared blob
`corpus/live/r25-{export-critic,export-scout×4,pair-reviewer×2}/…/out/fixture.x86_64` — 73.7MB each, identical blob. Already in history (push-safe at <100MB but permanent ~35MB pack weight for a regenerable build artifact). **Severity: MEDIUM** — also the seed of the 35 ignored re-extractions below.

### F2b. Resident giants, ignored — 6.2GB fleet disk
- g2d 5.5GB: `r68–r70-baseline/frozen/HEAD-*.tar` 656–667MB ×4; `r65-boundary/edge-verdicts.json` 122MB; 35× 73.7MB `fixture.x86_64` re-extractions under `r{63,66,67,69,70}-baseline/{tree,frozen,frozen-extract}` (ignored by `corpus/.gitignore: live/**/*tree*/`, `*extract*/`, `frozen/`).
- audio 701MB: `r70-simplifier/head.tar` + `r70-baseline/frozen/head-939fe47.tar` = **278,548,480 B each (the 265MB pusher-bouncer — two copies, ignored via `.gitignore:2 corpus/live/*/*.tar` and `corpus/.gitignore:5 live/*/frozen/`)**; `r69 head-7b8d423.tar` 169MB.
- g3d: 0 bytes. Parent view: all under ignored `*-shokunin/` lanes.
- **Gap class:** UNTRACKED-NOT-IGNORED ≥10MB = **0 fleet-wide** — ignore lattice currently tight. head.tar can no longer bounce a push; it survives only as disk cost + re-ingestion bait if rules regress. **Severity: MEDIUM** (disk), LOW (git risk).

### F2c. Ignore-rule gaps
- `.devin/` (substrate skill dir) at parent root: untracked, **not ignored** → permanent `git status` noise in parent. Cosmetic.
- audio `corpus/live/r71-critic/` w10 scratch (test.*, big.mp3 ~1.4MB ×2, *.bin/*.wav ×16) — untracked-unignored, in-scope residue awaiting cleanup; same for `r72-*` dirs (w11, in-flight).

---

## F3 — Tracked-scratch policy drift

`git ls-files | grep -cE 'scratch|/runs/'`:

| Repo | Tracked scratch/runs files | Hotspots |
|---|---|---|
| parent | 18 | `.ufo/reports/round-15/scratch/` ×14, `.ufo/waves/round-{10,14}/scratch/` ×2 — `scratch/` (no hyphen) **not covered** by `.gitignore:3 .ufo/waves/*/*-scratch/` |
| audio | **9,817** | `r6{5..9},r70-{boundary,scout,scribe}/runs/logs/` (1183 in r66-boundary alone), `r6{2,3}-*/scratch/` |
| g2d | **23,836** | `r69-{simplifier,scribe}/{runs-landed,runs-preland,del-measure}/*/scratch` + `missing-preset-scratch` (~60 files/run-dir), `r20-*-scratch/` Godot projects |
| g3d | 0 | `corpus/.gitignore` = `live/` — whole live tree untracked |

- **Tracked `.pyc`** (w10 followup F8): parent 3 (`.ufo/waves/round-1{2,3}/__pycache__`), audio 36, g2d 40, g3d 0. On-disk `__pycache__/` dirs: parent **273**, audio 83, g2d 184, g3d 3 — unignored bytecode regenerates noise every run.
- audio `corpus/live/runs/` is a **tracked shared ledger**: 5,282 tracked `measurements.json`; 5 new w11 dirs (11:20–11:21) untracked-unignored — every `measure_audio.py`/`build_artifacts.py` invocation appends there by design.
- **Severity: MEDIUM** — 33k+ transient files committed contradicts the "scratch is transient" rule (`/.gitignore:2` comment); lane policy is internally inconsistent (g3d tracks nothing under live/, audio/g2d track everything incl. scratch).

---

## F4 — Seat write-scope check, wave-10/11

- **Wave dirs clean.** `w10/`: spec/dispatch/swarm-registry/closeout + `tasks/` + empty `xsentinel-scratch/` (ignored, `.gitignore:3`). `w11/`: `spec.json` + `tasks/` only — committed by operator `42e8c23`. No stray seat files in either wave dir.
- **Declared scope pattern** (w11 tasks): `reports/round-<N>/r<N>-<seat>.md` + `corpus/live/r<N>-<seat>/` **ONLY**.
- **Live in-scope work observed:** g3d r80-verifier `blender -b -P bpy_evalcat_probe.py` (child of live bash); g2d frontier-lovephysics seat (`run-2..7.{txt,err}`, `phys_off/`, `reports/frontier/fb-lovephysics.md` @11:21) — inside frontier scope.
- **F4a. Directive-vs-scope contradiction (systemic, not a seat fault):** `g3d-author.txt` orders "implement the move in the tracked fixture(s)" while the boilerplate says "write ONLY inside … report file + scratch dir". Observed: `M corpus/fixtures/bpy_sync_probe.py` (+619, r80 evalcat arm) and `M corpus/fixtures/bpy_battery.py` (+114), dirty-uncommitted, mtimes 11:22–11:23 — author landing by directive. Same pattern sanctioned by convention for runs/ ledger writes (audio) and fixture regeneration mtimes fleet-wide (`measure_audio.py`, `build_artifacts.py`, `corpus/artifacts/*.wav`, `corpus/live/round-*/​*_probe.wav` touched in-window, content-identical → status clean). **Impact:** scope audits can't distinguish sanctioned shared-surface writes from violations without reading task text per seat. **Smallest remediation:** amend the scope line to "+ shared fixture/ledger surfaces when directive requires" or move fixture edits to operator-side landing. **Severity: LOW-MEDIUM (ambiguity), not a breach.**
- **F4b. Tracked-file mutation inside scratch:** g2d `M corpus/live/frontier-lovephysics/out/run-1.txt` (464-line rewrite) + `M phys_probe/main.lua` (+120) — inside the frontier seat's own dir; allowed by scope letter, but mutating *tracked* prior evidence rather than appending new scratch. Note only.
- **F4c. Watchers:** seat-launched `watch.sh` loops (F1c) write only inside their own `r71-{scribe,simplifier}/` — in-scope path, out-of-lifetime process.
- No cross-lane writes found; no writes into other waves' dirs; parent tree untouched except `.devin/` (substrate).

---

## Severity roll-up

| # | Finding | Severity | Status |
|---|---|---|---|
| F1a | 75 orphaned ffmpeg, FIFO-blocked, r67–r71 | HIGH→resolved | externally swept 11:22–11:24; root cause live |
| F1b | `timeout strace` deadline deadlock ×3 | MEDIUM | swept; mechanism unaddressed |
| F1c | stuck pw-cat probe bash, 3 watcher trees, /tmp litter ~209 | LOW–MEDIUM | live |
| F2a | tracked 73.7MB blob ×7 paths (g2d) | MEDIUM | standing |
| F2b | 6.2GB ignored giants resident (g2d 5.5G, audio 701M) | MEDIUM | standing |
| F2c | `.devin/` unignored; zero untracked-unignored ≥10MB | LOW | standing |
| F3 | 33,671 tracked scratch/runs files + 79 tracked .pyc | MEDIUM | standing drift |
| F4a | fixture/ledger writes vs "scratch ONLY" scope line | LOW–MEDIUM | policy tension |
| F4b/c | tracked mutation inside scratch; watchers outlive seats | LOW | note |

**Census receipts:** all `ps` snapshots, `git` classifications, and `find` inventories above were captured live this session; w10 `closeout.json:standing_followups` cross-referenced (ffmpeg-orphan followup confirmed & now stale-positive; `.pyc` F8 answered: 79 tracked).
