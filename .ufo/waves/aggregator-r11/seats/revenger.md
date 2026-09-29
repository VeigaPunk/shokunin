# Revenger — intent reconstruction for ambiguous fleet events

Seat: aggregator r11, round-11 fleet ledger refresh. All commands runnable verbatim from `/home/vgpnk/Projects/shokunin`. Volatile state stamped `2026-09-29T03:26Z` (`date -u`).

## Q1 — Was the wrap a mission pause, config reload, or lane-model migration? Does it explain counter heterogeneity?

**Evidence**

- `git show f5d8507` — integrator commit `2026-09-28T23:41:38-03:00`. Two files: `.ufo/reports/round-10/aggregator.md` (+4 lines: *"Fleet wrap: lane completed by operator directive before its report landed. In-flight work survives in the main repo working tree. Not respawning."*) and `scripts/shokunin-watchdog.sh` (+13/-4), which inserts a sentinel branch into the tick loop:

  ```bash
  elif report_of "$lane" "$n"; then
    if [ -f "$SK/.ufo/fleet-wrap" ]; then
      "$UFO" complete --mission "$mid" --note "fleet wrap: round $n landed, not respawning" ...
      echo "... wrap ${lane} round=${n} complete; NOT respawning (fleet-wrap)" >> watchdog.log
    elif [ "$n" -lt "$MAX_ROUNDS" ]; then ... launch_lane "$lane" $((n+1))
  ```

- `sed -n '260,320p' .ufo/watchdog.log` — drain is per-lane as each in-flight round lands: kasegi r17 23:39:54, kengaku r13 23:39:55, kumitate r16 23:39:55, kotoba r16 23:39:56, kama r1 23:39:57; aggregator r10 23:47:27; protocol r14 last at 23:54:59. Sentinel must have existed in the working tree ~2min before f5d8507 was committed. NOTE: lanes re-emit `wrap … NOT respawning` every tick until relaunch (e.g. kasegi logged 3×) — after `ufo complete` the mission still greps `live=1` and `.round` doesn't advance, so the wrap branch re-fires. Only each lane's FIRST wrap line marks real completion.
- `git show 17c1fad -- scripts/shokunin-watchdog.sh` — relaunch commit `00:19:02-03:00`: `SK` path changed `projects/` → `Projects/`, and `LANE_MODEL` rewritten from `m_lunamax`/`m_z53`/`m_flash` mix → all nine lanes `@m_swe`; prompt L0 path and route-map text updated in kind.
- `git log -1 --format='%ci %s' f5d8507` — subject literally reads "respawn-per-round halted at current round **per lane**". `git log --oneline --all -- .ufo/fleet-wrap` → empty; `ls .ufo/fleet-wrap` → No such file. Sentinel was never committed and was deleted at relaunch.
- `sed -n '296,312p' .ufo/watchdog.log` — at 00:19:29–34 all nine lanes log `complete <lane> round=N; respawning` + `launch <lane> round=N+1` in one tick (the new driver observed live=1 missions whose reports existed — sentinel gone → normal complete+respawn path).

**Interpretation**

Not a pause and not a config reload — a **controlled fleet drain + driver restart for a lane-model migration** (with repo relocation and kama onboarding folded into the same window). The sentinel made each lane finish its in-flight round, log `wrap`, and NOT respawn; the operator then moved the repo path, rewrote `LANE_MODEL` to `@m_swe`, deleted the sentinel, and started a fresh watchdog, which cleanly completed the lingering missions and launched everyone at `N+1`. **Counter heterogeneity is fully explained**: counters are per-lane files (`ls .ufo/state/` → one `<lane>.round` per lane; f5d8507's subject states "halted at current round **per lane**"), so aggregator froze at 10 and relaunched 11 while protocol froze at 14 and relaunched 15. Aggregator is simply a slower lane (10 rounds completed in the whole 15:44–23:39 window vs kasegi's 17). There is no fleet-global round number — MANIFEST/`rounds[]` mint-gap reasoning should not assume one.

**Confidence: high** (mechanism read from the script diff itself; timeline consistent across log, commits, and live processes).

## Q2 — 8afbc8f 'untrack embedded kama-shokunin repo': was kama first committed AS a gitlink then untracked?

**Evidence**

- `git show 8afbc8f` — deletes file mode `160000` `kama-shokunin`, `Subproject commit c6199a2542440db77d69918599e5a378ee116337` (= kama-shokunin HEAD, matching context). Timestamp `00:19:15-03:00`, author Joao Pedro Veiga.
- `git log --diff-filter=A --oneline -- kama-shokunin` → **17c1fad** — the gitlink was ADDED inside the relaunch commit itself (its `--stat` lists `kama-shokunin | 1 +`), then removed 13 seconds later by 8afbc8f.
- `cat .gitignore` → contains the six original lane dirs (`kasegi-shokunin/` … `kagi-shokunin/`) but NOT `kama-shokunin/`; `git check-ignore -v kama-shokunin` → NOT IGNORED. Verified at stamp: `git status --porcelain` shows `?? kama-shokunin/` — still unignored, still stageable as a gitlink by any `git add -A`.
- `git log -1 --format='%ci %h' cd2d343` → `2026-09-28 23:20:47` — kama r1's fleet-hygiene filing ("a main-repo 'git add -A' would stage it as a gitlink … proposed one-line fix on the L0 channel") **predates** the accidental staging at 00:19:02 by ~58 min.

**Interpretation**

Yes — committed as a gitlink at 17c1fad, untracked at 8afbc8f 13s later. The kama r1 debt wasn't stale: it was a **correct prediction that the operator then triggered live** while landing the big 218-file relaunch commit (the `git add -A` it warned about). The untrack commit was a surgical correction, not a fix — the root cause (missing `.gitignore` line) remains open at stamp time, so the same accident can recur on the next `add -A`. Proposed routed-row text: "kama r1 .gitignore gap remains open after 8afbc8f's untrack — add `kama-shokunin/` to .gitignore" (no key assigned per contract).

**Confidence: high** (diff-filter log is unambiguous; .gitignore state re-verified live).

## Q3 — `.ufo/watchdog-driver.log`: what is the driver vs the watchdog? Does it explain dirty state files?

**Evidence**

- `wc -l .ufo/watchdog-driver.log` → `0`; `ls -la` → 0 bytes, created `Sep 29 00:19`; `git status --porcelain` → `?? .ufo/watchdog-driver.log` (untracked).
- `sed -n '88,116p' scripts/shokunin-watchdog.sh` — `scripts/shokunin-watchdog.sh` **is** the fleet driver (header line 2: "respawn-per-round fleet driver"). All its diagnostics go to `.ufo/watchdog.log` via explicit `echo >>`; nothing inside writes driver-log. The file is plainly the shell script's own stdout/stderr redirect (`bash scripts/shokunin-watchdog.sh > .ufo/watchdog-driver.log` or tmux equivalent) created when the new driver instance spawned at 00:19 — empty because the script produces no incidental stdout.
- `ps aux` — PID 2991361 `bash scripts/shokunin-watchdog.sh`, started 00:19, alive at stamp.
- `git status --porcelain | grep -c '^ M'` → **19** (not 16): 9 lanes × `.ufo/state/<lane>.{mission,round}` + `.ufo/watchdog.log`. `git diff .ufo/state/kasegi.round` shows `17` → `18`; `.mission` shows old runId → `shokunin-r18-kasegi-r1790651970`.
- `sed -n '64,86p' scripts/shokunin-watchdog.sh` — `launch_lane` writes the runId to `.mission` and N to `.round` on every launch — both are **git-tracked** files, so every launch dirties two tracked files per lane.

**Interpretation**

Driver = watchdog: one process, two logs. `.ufo/watchdog.log` is the structured event log the script appends to; `.ufo/watchdog-driver.log` is the driver's captured stdout/stderr for this instance (empty = healthy, `set -u` clean, no launch-fail output leaked). Dirty state is mechanical: the mass relaunch rewrote all 18 tracked state files plus appended the log — counted 19 ` M`, not the 16 the prompt cited (likely counted before aggregator/protocol/kama launches landed or before a later tick). Implication for the ledger: `.ufo/state/*` churns every launch while staying tracked — per-round commits would need to either track it (noise) or the prompts' "commit+push" already swallows it.

**Confidence: high** on mechanism; **medium** that 16-vs-19 is purely a timing artifact (no second writer found).

## Q4 — Round-counter semantics: N = in-flight round or last completed?

**Evidence**

- `sed -n '80,81p' scripts/shokunin-watchdog.sh`: `echo "$n" > .ufo/state/$lane.round` executes inside `launch_lane` **at launch time**, before the round runs.
- `cat .ufo/state/kasegi.round .ufo/state/kama.round .ufo/state/aggregator.round` → `18 / 2 / 11`.
- `cat .ufo/state/kake.round .ufo/state/kagi.round .ufo/state/protocol.round` → `17 / 17 / 15`.
- Cross-check report files (`ls .ufo/reports/round-17/ .ufo/reports/round-18/`): `round-17/` holds only `kasegi.md`; `round-18/` is empty (dir auto-created by `lane_prompt` via `mkdir -p` at launch — explains empty `round-11`, `round-18` dirs). `ls .ufo/reports/round-16/` → `kagi kake kasegi kotoba kumitate` — kagi/kake last filed r16.
- Log pairing: `launch kasegi round=18` at 00:19:30 with `wrap kasegi round=17 complete` 23:39:54 — report for the counter's own number (18) does not exist; last filed is 17. Same pattern: kake counter 17, last report round-16/kake.md; kagi counter 17, last report round-16/kagi.md. Protocol counter 15; no `round-15/protocol.md` exists (round-15 dir has `kagi kake kasegi kotoba kumitate scratch` only).

**Interpretation**

**`.ufo/state/<lane>.round` N = the current in-flight round** (set at launch), NOT last completed. Ledger rule: "last completed round" for a lane = `N − 1` when the lane is mid-round, or `N` only when a `round-<N>/<lane>.md` file exists AND the watchdog has logged `complete`/`wrap` for it. For dormancy pairs: kasegi's reported-completed frontier is 17 (filed), 18 is live and must not count as a completed-or-dispatched round for dormancy until its report lands.

**Confidence: high** (code path + three-lane file/log cross-check agree).

## Summary for the L1

| Event | Reconstruction | Confidence |
|---|---|---|
| f5d8507 wrap | Sentinel-file drain + driver restart enabling @m_swe lane-model migration + repo move + kama onboarding; per-lane counters explain 11-vs-15 | high |
| 8afbc8f untrack | kama gitlink added inside 17c1fad, removed 13s later; r1's .gitignore-gap prediction fired live, debt still open | high |
| watchdog-driver.log | Driver's stdout/stderr capture for the 00:19 instance; 0 bytes = clean; state dirtiness is tracked `.ufo/state/*` rewrites per launch (19 M observed, not 16) | high (mechanism) / med (count delta) |
| Counter semantics | N = in-flight round, written at launch; completed frontier = N−1 while mid-round | high |
