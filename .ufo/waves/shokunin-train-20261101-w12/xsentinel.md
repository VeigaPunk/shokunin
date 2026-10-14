# XSENTINEL — fleet hygiene audit, wave-12

**Seat:** xsentinel (LEAF, report + confirmed-dead process kills only)
**Window:** 2026-10-14 ~11:52–12:07 local (-0300)
**Scope:** lane repos `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin` under `~/Projects/shokunin` (parent `master@d41a9f5`; lanes each own repo on `main`, excluded from parent by `.gitignore:*-shokunin/`)

**Headline:** one confirmed-dead fifo tree killed (audio r72-critic, 2 pids). Unlike w11's 75-orphan standing leak, this wave's r73 fifo probes **self-reap**: ffmpeg/pw-cat/mpv children churn under live seats and clear to zero when each rung ends. All three rounds (audio r73, g2d r72, g3d r81) were LIVE throughout the audit — seat-owned processes reported INFO, not killed. Only other mutation: none. `git status` shows only convention-sanctioned tracked deltas.

---

## F1 — Process census

### F1a. KILLED — audio r72-critic dead fifo-writer tree

| PID | Cmdline | Evidence of death |
|---|---|---|
| 3813 | `bash -c` async subshell: `… && mkfifo "$tmp/m.snd" && cat corpus/live/round-69/extsuffix_nomatch.snd > "$tmp/m.snd"` | `wchan=wait_for_partner` blocked in `open(O_WRONLY)` on `/tmp/r72-critic-fifo2-sDv4/m.snd` for **~37 min** (etimes 2001s at kill). **No reader can ever exist:** `$tmp` was assigned *inside* the `&`-backgrounded AND-list, so the foreground `timeout -s KILL 6 sndfile-info "$tmp/m.snd"` expanded to literal `/m.snd` → ENOENT → exited instantly ~35 min prior. The mktemp path was known to no other process. |
| 3808 | parent `bash -c` of the same probe | `do_wait` on 3813 forever; its own `timeout` and `rm -rf` cleanup both dead. Reparented to PPID 1573 (systemd --user) — launching seat exited. |

- **Action:** `kill -9 3813 3808` at ~11:58. Verified gone (`ps -p` empty). SIGKILL chosen per r73 measurement that fifo-blocked opens ignore SIGTERM.
- **Residue (not removed — file cleanup out of kill scope):** fifo `/tmp/r72-critic-fifo2-sDv4/m.snd` on disk, inert.
- **Bug class:** the same `cmd && cmd & cmd` precedence trap as w11's watcher launchers (async list swallows the variable assignment), plus an unbounded fifo writer with no `timeout`/reap — the w11-F1a leak mechanism in miniature.
- **Severity:** was LOW-MEDIUM (self-contained, one fifo, /tmp-only). Now CLOSED.

### F1b. INFO — r73 fifo-probe churn is live-seat-owned and self-reaping

- **Observed (11:52–12:00):** steady ~2 `ffmpeg -loglevel quiet -nostdin -i /tmp/fifo-hold-r70-*/pair_dec_act.wav -f au -` per snapshot, each PPID→1573 within seconds (orphaned per rung), blocked `wait_for_partner`; transient `mpv --ao=null … -` children of `measure_audio.py --probe-consumers-r73`; 1 transient `pw-cat`; ~2 `[sox] <defunct>` zombies under `measure_audio.py` parents (reap lag, self-clearing).
- **Difference vs w11:** orphans do **not accumulate** — each rung's `/tmp/fifo-hold-r70-*/` dir is removed and its ffmpeg disappears within tens of seconds; final 60 s recount = **0 ffmpeg, 0 mpv, 0 pw-cat, 0 strace**. Parents are live harnesses under seat session `devin acp` (pid 3928555), wrapped `timeout 280`, outputs in-scope (`corpus/live/r73-reviewer/ladder-run3.out`, `r73-author/ledger-r73.tsv` via `run_ledger.py`, fd 3 held open on the active rung's fifo — paired ends confirmed via `/proc/*/fd`).
- **Residual risk (unchanged mechanism):** if a seat session dies mid-rung, the orphaned reader persists forever (fifo unlinked, `wait_for_partner`, SIGTERM-immune — needs SIGKILL). Not a leak today; remains the w11 root cause.
- **Severity:** INFO.

### F1c. INFO — bounded watcher/poller residuals (orphaned launchers, in-scope writes)

| Tree | Lane/seat dir | Bound | State |
|---|---|---|---|
| 218833+218836 g2d `r72-reviewer/watch.sh` | r72 | 200×10s | **exited on bound** during audit |
| 221465+221469 g2d `r72-simplifier/watch.sh` | r72 | 240×10s (~40 min) | live, ends ~12:15 |
| 405623+405627 g2d `r72-simplifier/snapshot_loop.sh` | r72 | 300×10s (~50 min) | live, ends ~12:25 |
| 287861+287883 g3d `r81-simplifier` watch loop | r81 | 120×15s | exited ~12:07 |
| 326833+326835 g3d `r81-critic` fixture-delta watcher | r81 | 120×10s | exited ~11:57 |

Same cosmetic doubling as w11 (`bash -c` wrapper `do_wait`s on its own `nohup`ped watcher). Launchers reparented to 1573 but children write only own-scope `watch.log`/`snapshots/` and self-terminate. Not killed: r72/r81 dirs show seat mtimes within the last minutes — the rounds are in-flight and these logs feed live seats.
**Also live (seat-owned, do not kill):** audio `r73-author/run_ledger.py` → `measure_audio.py --probe-consumers-r73` (511189 tree); `r73-baseline` rerun tail-sleeper (419142); g2d `r72-reviewer` `pygame_battery.py --runs` loops (514746 tree); g3d r81 author-poll loops (436138, 504090).

### F1d. Out-of-scope lanes (INFO only)

Other shokunin lanes have live seats under a `kimi` session (pid 295525): `/tmp/tameshi-r3-3-work/poll.sh` (321900/321902), `/tmp/tsukuroi-r3-4-poll/poll.sh` (332220) + in-repo poll loop (486051), `mado-shokunin` file-watch poll (503969). Not in audit scope; reported for census completeness.
**Session noise (not fleet):** `uwsm-app` ×4, `xdg-terminal-ex` ×1 zombies.

### F1e. On-disk fifos & /tmp litter

- **Corpus fifos, no openers:** `audio corpus/live/r68-scout/fifo/` ×16, `frontier-pipewire/fifo{1,2,3}` (w11's stuck pw-cat bash 4145249 is gone), `r73-author/scratch/fifo{A,P,S.snd,Act.wav}`, `r73-verifier/{n,p}fifo`, `r73-boundary/logs/f{2,3}.fifo` — inert; the r73 set belongs to live seats.
- **/tmp:** ~364 fleet-tagged entries (w11: ~209). Live working dirs churn (`fifo-hold-r70-*`); dead residue: `r72-critic-fifo2-sDv4/` (from F1a), `straceleg-r70-*`/`sanity-r70-*`/`tmp*/cz_nomatch.*` fifo dirs, plus w9–w11-era `r6*`/`r7*` files. Growing; sweep recommended next hygiene pass.

---

## F2 — Oversized artifacts (≥20MB, classified)

Method: `find -size +20M` per lane → `git ls-files --error-unmatch` / `git check-ignore` per file.

| File | Size (B) | Class | Verdict |
|---|---|---|---|
| audio `corpus/live/r73-baseline/frozen/head-f5d7faf.tar` | **344,576,000** | IGNORED | **NEW** — largest-yet head.tar (+64MB over w11's 278.5MB pair). Disk cost only; cannot bounce a push. |
| audio `corpus/live/r71-critic/big.wav` | **52,920,078** | **UNTRACKED-NOT-IGNORED** | **NEW** — mtime 11:29:56 (post-w11). The **only** ≥20MB untracked-unignored file fleet-wide. In-scope r71-critic residue (26-file scratch, all unignored). |
| g2d `r72-baseline/frozen/HEAD-44127af….tar` | 683,438,080 | IGNORED | new instance of known frozen-tar class |
| g2d `r72-baseline/frozen-extract/…/fixture.x86_64` ×7 | 73,703,800 ea | IGNORED | new instance of known re-extraction class |
| g2d tracked `r25-*/fixture.x86_64` ×7 | 73,703,800 ea | TRACKED | standing (one shared blob, w11 F2a) |
| g2d r{63,66,67,69,70} fixture re-extractions ×35, r65 `edge-verdicts.json` 122MB, r{68,69,70} tars ×4 | — | IGNORED | standing |
| audio `r70-simplifier/head.tar`, `r70-baseline/frozen/head-939fe47.tar` 278.5MB ×2, `r69 head-7b8d423.tar` 169MB | — | IGNORED | standing |
| g3d | 0 files ≥20MB | — | clean |

**Disk:** g2d 8.4GB, audio 2.9GB, g3d 483MB resident (g2d +~1.2GB this wave via r72-baseline). **Tracked ≥20MB:** unchanged — only the 7 known `fixture.x86_64` paths; **zero new tracked giants**. Untracked-unignored ≥1MB besides big.wav: **none**.
**Severity:** MEDIUM disk (cumulative ~12GB); LOW git-risk; big.wav LOW (in-scope residue, but it is a rule-evading >20M file).

---

## F3 — Ignore-gap shapes

- **`measure-env/` — established shape, still uncovered, now the largest gap.** `audio corpus/live/r73-baseline/measure-env/` = **783 untracked-unignored files, 46MB** (a nested repo clone: `corpus/live/round-*/executor`, `corpus/artifacts`, `corpus/live/runs/` ledger copies); `r72-baseline/measure-env/` 2.9MB. Neither audio nor g2d ignores it (`live/*/tree|frozen|*tree*|head|snapshot|base|*extract*` lattice doesn't match). **Drift risk is real, not hypothetical:** r69/r70 `measure-env/` content is already partially TRACKED (their `__pycache__/*.pyc` sit in the index — see F4) — a baseline seat *did* commit its env clone once. If r73's lands, ~800 transient files + a fixture clone enter history. Smallest remediation: add `live/*/measure-env/` (or `live/*/*env*/`) to `audio corpus/.gitignore`; mirror to g2d defensively.
- **`runs/` at seat depth (audio):** `r73-boundary/runs/` ×4, `r73-scout/runs/` ×5 untracked-unignored — distinct from the sanctioned tracked ledger `corpus/live/runs/` (which gained new w12 entries normally). Small emerging shape; g2d's `runs-*`/`runs2`/`godot-runs` analogues are tracked by convention there.
- `replica/tree/`, `frozen-extract/` — covered: audio `live/**/*tree*/`, both lanes `live/*/*extract*/` verified matching new instances (g2d r72-baseline/frozen-extract → IGNORED).
- g2d untracked-unignored = **3 files total** (round-71 reports awaiting operator commit). g3d = **8 report files** (`live/` wholesale-ignored lattice holds). Parent: `.devin/` w11 cosmetic gap **resolved** — `.devin/skills/flashseat/SKILL.md` now tracked (wave-12 setup commit `d41a9f5`), `mcp_config.local.json` in `info/exclude`.
- **Severity:** MEDIUM for measure-env (precedented commit-drift); LOW for seat `runs/`.

---

## F4 — Tracked `.pyc` drift

| Repo | w11 | w12 | Delta | New locations |
|---|---|---|---|---|
| parent | 3 | 3 | 0 | — |
| audio | 36 | **40** | **+4** | `r72-boundary/` ×1, `r72-reviewer/` ×2, `r72-reviewer/ldstub/` ×1 |
| g2d | 40 | **43** | **+3** | `r71-baseline/godot-runs/*/{missing-preset-scratch,scratch}` ×2, `r72-baseline/` ×1 |
| g3d | 0 | 0 | 0 | — |

On-disk `__pycache__/` dirs: parent 273→**332** (+59), audio 83→86, g2d 184→**239** (+55), g3d 3→4. Drift continues at the established rate — each wave commits another handful of bytecode via seat scratch. **Severity:** LOW-MEDIUM (standing drift, not a new breach).

---

## F5 — Tracked-file mutations by seat scratch (`git status` per lane)

| Lane | Head | Tracked deltas | Attribution |
|---|---|---|---|
| parent | `master@d41a9f5` | 0 | clean; `?? .ufo/reports/round-{72,73}/*.md` operator reports pending |
| audio | `main@febf34b` | `M LOG.md` (+19), `M SCORECARD.md` (+12), `M corpus/live/r72-baseline/measure-env/corpus/fixtures/measure_audio.py` (+264) | LOG/SCORECARD = sanctioned ledger convention (mtimes 11:58, live bookkeeping). The measure_audio.py edit is the r72 sndfile leg developed **inside the baseline seat's measure-env clone** of the fixture — real `corpus/fixtures/measure_audio.py` clean. In-scope dir but tracked-surface edit inside a scratch-shaped tree (w11 F4a tension). |
| g2d | `main@2dd108b` | `M corpus/live/r72-simplifier/watch.log` (+2) | the live watcher (F1c) appending to a **tracked** log — process-level mutation of tracked file in own-scope dir (w11 F4b note). |
| g3d | `main@ae89c13` | `M corpus/fixtures/bpy_battery.py` (+109), `M corpus/fixtures/bpy_sync_probe.py` (+225) | r81-author directive-driven fixture landing, mtimes 11:55–11:56 — matches the r81-simplifier/r81-critic watchers' monitored paths (w11 F4a convention). |

No cross-lane writes, no writes into other waves' dirs, w12 wave dir contains only `spec.json`/`registry.json`/`tasks/`. **Severity:** LOW — all deltas fit declared-convention patterns; the F4a scope-line ambiguity flagged in w11 remains the systemic note.

---

## Kill log (only mutations this seat performed)

| Time | PIDs | Signal | What | Proof of death |
|---|---|---|---|---|
| ~11:58 | 3813, 3808 | KILL | audio r72-critic `bash -c` fifo2 writer tree (F1a) | Orphaned to 1573; writer blocked `wait_for_partner` on `/tmp/r72-critic-fifo2-sDv4/m.snd` ~37 min with zero possible readers (`$tmp` scoping bug → reader never saw the path; `timeout -s KILL 6` and `rm -rf` both dead). `ps -p` post-kill: empty. |

**Live-seat-owned processes reported but deliberately not killed:** all F1b probe churn (devin acp session children), all F1c watchers (bounded, in-scope), all F1d other-lane pollers.

---

## Severity roll-up

| # | Finding | Severity | Status |
|---|---|---|---|
| F1a | r72-critic dead fifo-writer tree (2 pids, ~37min) | LOW-MEDIUM | **killed & verified** |
| F1b | r73 ffmpeg/mpv/pw-cat fifo churn | INFO | live-seat, self-reaping; w11 root cause latent |
| F1c | 5 watcher/poller trees, orphaned launchers | LOW | bounded, in-scope, 3 exited on bound |
| F1d | other-lane seat pollers (tameshi/tsukuroi/mado) | INFO | out of scope |
| F1e | ~364 /tmp fleet files; 26 inert corpus fifos; `r72-critic-fifo2-sDv4` residue | LOW | growing litter class |
| F2 | NEW 329MB `head-f5d7faf.tar` (ignored) + NEW 50.5MB `big.wav` (**untracked-unignored**) | MEDIUM / LOW | resident; ignore lattice held elsewhere |
| F3 | `measure-env/` unignored, 783 files @46MB in r73-baseline alone, prior instances partially tracked | MEDIUM | recommend `live/*/measure-env/` rule |
| F4 | tracked `.pyc` 79→**86** (+7); on-disk `__pycache__` 543→**664** dirs | LOW-MEDIUM | standing drift rate |
| F5 | tracked mutations: ledgers (sanctioned), fixture landings (F4a convention), tracked watch.log append, env-clone fixture edit | LOW | no breach; policy ambiguity stands |

**Census receipts:** all `ps`/`/proc` wchan+fd scans, `git check-ignore`/`ls-files` classifications, `find -size +20M` inventories, and `git status` outputs captured live this session (12:00–12:07 final recounts: ffmpeg=0, wait_for_partner fleet=0, dead tree verified absent). w11 `xsentinel.md` standing items re-measured: F2a/F2b persist +r72 instances, F2c `.devin/` resolved, F3 `.pyc` count updated, F1a orphan class = 0 standing at close.

---

## Addendum — independent recount 12:04–12:08 (same seat, second pass)

Re-swept all five scope items after the report was written; every finding corroborated, none invalidated:

- **F1 recount @12:08:** `ffmpeg=0 mpv=0 pw-cat=0 sox=0 strace=0` — F1b self-reap claim held. Only fleet residuals: 221465+221469 (`r72-simplifier/watch.sh`, etimes 1973s, bound ends ~12:15) and 405623+405627 (`snapshot_loop.sh`, etimes 1382s, ends ~12:25) — orphaned launchers (PPID→1573), in-scope writes only, still per F1c. `find /proc/*/fd` over all live pids: **zero open fds on any corpus or /tmp fifo** — no blocked opens anywhere. w11's stuck pw-cat bash (4145249) confirmed absent.
- **F5 update:** g3d's `M bpy_battery.py`/`M bpy_sync_probe.py` deltas **landed** in `65b2f26` (12:03) and `fd75567` (12:05) — r81 seats committing fixture work by directive; `git status` now shows only `M LOG.md`/`M SCORECARD.md` (ledger convention). Live r81-reviewer `run_battery.py`→godot tree (614092→626389, parent `devin acp` 3928555) still in-flight — INFO, not touched.
- **F2/F3 spot-rechecks:** `big.wav` still the only ≥20MB untracked-unignored file fleet-wide; `head-f5d7faf.tar` → IGNORED (`corpus/.gitignore:5`); `measure-env/` still unignored in both lanes; audio untracked-unignored ≥1MB = `big.wav` alone.
- **Mutations by this pass:** none. No kills — the only dead tree (F1a) was already closed at ~11:58; watchers bounded/in-scope; all other processes live-seat-owned.
