# JjTrialGameDev3d — jj-colocation trial for lane `game-dev-3d`

Sandbox: `/fast/scratch/jj-wave/JjTrialGameDev3d/` (`remote.git` bare, `lane` colocated clone,
`lane-autotrack` copy for the `all()` measurement, `lane-plain` non-jj baseline, `operator`
second clone, `probe` scratch repo). jj 0.45.1 at `~/.local/bin/jj`. Live repo never touched
except read-only `git status`/`ls`/`cat`.

## Findings (observed)

### Step 1 — sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin .../remote.git
git clone .../remote.git .../lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin/ .../lane/
git -C .../lane status --porcelain | wc -l   → 1
git -C .../lane status --porcelain           → ?? reports/round-107/
```
10 largest untracked/ignored files (`find` over `reports/round-107`, `node_modules`, `corpus/live`):
all 10 are copies of `corpus/live/runs/20261018T*/scratch/r95vendor/pybullet.cpython-314-x86_64-linux-gnu.so`,
7,063,864 bytes each. File counts: `reports/round-107/` = 79 files; `corpus/fixtures/three/node_modules/` = 1,264;
`corpus/live/` = **120,686**. Ignore sources: `corpus/.gitignore:1 live/` and
`corpus/fixtures/three/.gitignore:1 node_modules/`. `git status --porcelain --ignored` shows
`!! corpus/fixtures/three/node_modules/` and `!! corpus/live/` — git-side ignore works.

### Step 2 — helper init

```
HYAKU_STATE=.../state jj-lane.sh init .../lane game-dev-3d   → rc 0
```
Output included `Setting the revset alias trunk() to main@origin`,
two warnings `The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>"`,
and the state line:
```
state branch=main local=3118be0b…ec remote=3118be0b…ec ahead=0 behind=0 head=attached tracked=0 untracked=1
```
Repo config confirmed:
```
revset-aliases."trunk()" = "main@origin"
snapshot.auto-track = "none()"
user.name = "game-dev-3d-shokunin"
user.email = "game-dev-3d@shokunin.local"
```
`git symbolic-ref -q HEAD` → `refs/heads/main` (attached, as predicted right after init).
`git status --porcelain` unchanged: still exactly `?? reports/round-107/` (1 line).

`jj status` timing (date-based; `/usr/bin/time` absent):
run1 0.016 s, run2 0.016 s, run3 0.017 s, each rc=0. Output lists `? reports/round-107/` under
"Untracked paths" — listed but not tracked under `none()`.

### Step 3 — default `all()` auto-track alternative

`cp -a lane lane-autotrack`, then `jj config set --repo snapshot.auto-track '"all()"'`, then `jj status`:
- **79 files** snapshotted into the working-copy commit — every file under the untracked
  `reports/round-107/` (`jj diff --summary -r @` → 79 × `A`).
- Ignored trees (`corpus/live/` 120k files, `node_modules/` 1.2k) were **not** tracked
  (grep count 0): default auto-track respects gitignore.
- First `jj status` (the snapshotting run): **82 ms**; warm run 14 ms. No `new file too large`
  refusal — the 7 MiB `.so` files live under gitignored `corpus/live`, so the 1 MiB cap never met them.
- Side effect observed in git: `git status --porcelain` now shows 79 lines as ` A` (intent-to-add),
  i.e. the jj-tracked set leaks into `git status` as staged-intent entries.
- Extra probe: plain `jj file track scratch-big.bin` (2 MiB file) → warning
  `Refused to snapshot some files: scratch-big.bin: 2.0MiB; the maximum size allowed is 1.0MiB`.
  `jj file track --include-ignored scratch-big.bin` → rc 0 and `A scratch-big.bin` in `@`.
  So `--include-ignored` (used by the helper for named files) **also bypasses the 1 MiB cap** —
  any seat naming a `corpus/live/**` `.so` as a commit path WILL commit it.

### Step 4 — round commit through the helper

Prepared: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left
`operator-scratch.txt` untracked.
```
jj-lane.sh commit .../lane --as game-dev-3d -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 267ef0011a7fc039d56a49630eb1ffe21e82e374
  pushed    267ef0011a7fc039d56a49630eb1ffe21e82e374      rc=0
```
Verifications, all pass:
- `git show -s` → `author=game-dev-3d-shokunin <game-dev-3d@shokunin.local>`,
  committer identical. (metaedit `--update-author` works.)
- `git log -1 --format=%H -- LOG.md` → `267ef001…` = pushed hash.
- `git merge-base --is-ancestor 267ef001… main` → rc 0.
- `jj-lane.sh state` → `ahead=0 behind=0 head=detached tracked=0 untracked=2`.
  (HEAD detached to the tip after the jj mutation, exactly as predicted; `@{u}` is gone.)
- Sandbox remote: `git -C remote.git log -1 main` → `267ef001… round-999: jj trial`.
- `operator-scratch.txt` still `??` with content `do not commit me` intact.

Operator-push recovery: from `.../operator` (second clone), committed `considerthese/jj-notes.md`,
pushed `b5015dc9…` to `main`. Then in the lane appended a line to `SCORECARD.md` and reran the helper:
```
→ committed 160b94aaf918a1c87e508963ad150d96aa543923
  pushed    a34d3523e8ea0db235b2a2963fdc094f2fc6ec15   rc=0
```
The pushed hash differs from the committed hash — the helper fetched, rebased the unpushed commit
onto moved `main@origin`, moved the bookmark, and repushed. Remote history:
`a34d3523 → b5015dc (operator) → 267ef001 → 3118be0b`; `git merge-base --is-ancestor b5015dc main` → rc 0;
`state` → `ahead=0`. Recovery path confirmed end-to-end.

### Step 5 — lane's git-touching checks

The lane has exactly **one** git-invoking tool outside `reports/`:
`corpus/knowledge/unreal-mcp/gate/run_gate.sh` (CHECK 2 does `git clone` of the pinned upstream
into `GATE_WORKDIR` scratch, `git ls-files`, `git show <pin>:<f>`, `git status --porcelain`,
and `git -C "$SUB" rev-parse HEAD` for its `LANE_HEAD=` banner). The verify_*.py/run_import.py
selftests and `run_battery.py` never invoke git.

- Colocated lane run: `GATE_WORKDIR=.../gatework timeout 300 bash corpus/knowledge/unreal-mcp/gate/run_gate.sh`
  → `GATE RESULT: PASS (checks failed: 0)`, rc 0. CHECK 2 printed
  `CLONE_HEAD=a6aa73ad… CLONE_DIRTY=0 CLONE_TRACKED=12 PATH_EXTRA=0 PATH_MISSING=0 BLOB_DIFFS=0`.
  Note: CHECK 2's dirty probe runs against its *fresh clone* of the upstream pin repo, not the lane
  repo, so lane detached-HEAD state cannot reach it; `LANE_HEAD=` still resolved under detached HEAD
  (`rev-parse HEAD` works fine detached).
- Plain-clone baseline (`lane-plain`, same content, no `.jj`): `GATE RESULT: PASS (checks failed: 0)`, rc 0.
  Identical result → no colocation-induced gate failure.

### Extra probes (scratch repo, not the lane)

In `.../probe` (fresh git repo + `jj git init --colocate`):
- `git add staged.txt` then `jj new -m probe` → jj folded the index-staged file into a jj commit
  (`19c74b45`, empty description in git log) and reset the git index; `git status` went from `A  staged.txt`
  to empty with the file committed. **git's index is absorbed by jj, not preserved.**
- Raw `git commit` on the detached HEAD succeeds but stays off `main` (`git rev-parse main` ≠ HEAD);
  next `jj status` printed `Reset the working copy parent to the new Git HEAD` — jj adopts it into
  its own history while `main` never moves. A raw `git push origin main` then pushes the *old* tip,
  and `git pull` fails (`There is no tracking information for the current branch`).

## PASS/FAIL table

| step | check | result |
|---|---|---|
| 2 | init rc, state line clean, config keys set | PASS |
| 2 | git HEAD attached after init | PASS (`refs/heads/main`) |
| 2 | `git status` unchanged after init | PASS (1 line, identical) |
| 2 | `jj status` 3× warm ≈ 16 ms | PASS |
| 3 | `all()` snapshot count = 79, ignored dirs untouched | PASS (measured; hazard confirmed) |
| 4 | commit prints `committed`+`pushed`, identity = lane id | PASS |
| 4 | pushed hash ancestor of main, LOG.md log matches, remote updated | PASS |
| 4 | scratch file untracked and intact | PASS |
| 4 | rejected-push recovery via fetch+rebase | PASS (`a34d3523` on remote, `ahead=0`) |
| 5 | run_gate.sh in colocated lane | PASS (rc 0) |
| 5 | run_gate.sh in plain clone | PASS (rc 0) — no colocation regression |

## Lane-specific colocation hazards

1. **`corpus/live/` — 120,686 files incl. ≥10 identical 7 MiB `pybullet.*.so` binaries** (gitignored).
   Under `auto-track="none()"` harmless; under default `all()` still ignored. The live risk is the
   helper's `jj file track --include-ignored <named file>`: a commit pathspec naming a `corpus/live/**`
   file commits it with **no 1 MiB cap** (measured, step 3).
2. **`reports/round-107/` — 79 files of in-flight round output, untracked in the live repo too.**
   With default `all()` auto-track they are swept into `@` and surface in `git status` as 79
   intent-to-add ` A` entries — polluting every git-side status check in the lane. This is the
   strongest lane-specific argument for keeping `none()`.
3. **`corpus/fixtures/three/node_modules/`** — 1,264 ignored files; same ignore-respecting behavior.
4. **Symlink**: one, `corpus/live/r101-sentinel/probes/sym/Link.uproject` → missing target; inside
   ignored `corpus/live`, never exercised by a commit path.
5. **No `.gitattributes`/LFS, no `.git/hooks` beyond samples, no nested `.git`, no `.ufo/`** in this
   lane — those hazards don't apply here.
6. **Detached HEAD is normal** once jj mutates: `@{u}` and `git pull` break; any lane script doing
   raw `git push`/`git pull`/`git commit` will silently misbehave (probe section). This lane's only
   git-touching artifact (`run_gate.sh`) is read-only w.r.t. the lane repo and unaffected.
7. **git index is not durable**: jj absorbs `git add`-staged entries into jj commits — seats must not
   stage via `git add` expecting it to persist.

## Recommended per-lane config / ignore additions

The helper's init already sets the correct repo config; no additions are strictly required for
this lane. Recommendations (optional hardening):

- **Keep `snapshot.auto-track = "none()"`** — the measured `all()` alternative pollutes `git status`
  with the lane's in-flight round directories.
- **[INFERENCE]** Consider adding `reports/round-*/` scratch subdirs (e.g. `reports/round-104/gate/scratch/`,
  currently tracked in-repo history) to review — not needed for jj; noting only that round scratch
  committed historically is a lane convention, not a jj hazard.
- **[INFERENCE]** Document for lane seats: never name `corpus/live/**` files in a helper commit
  pathspec — `--include-ignored` will ship the 7 MiB `.so` binaries with no size guard. If a belt is
  wanted, a lane-side preflight could reject `corpus/live/` pathspecs; that is a helper/change-request
  decision, not config.
- **[INFERENCE]** `reports/round-107/` in the live repo is uncommitted in-flight work; whoever owns
  the round should commit it before cutover so the first post-jj snapshot isn't ambiguous.

## Recommendation

jj colocation through `scripts/hyaku/jj-lane.sh` is **safe for `game-dev-3d`**: the helper's
commit/push/state contract (pathspec-limited, lane identity, pushed-hash citation, fetch+rebase
recovery, append-only LOG.md honored) held under real lane content including a 120k-file ignored
tree; the lane's single git-touching gate passes identically colocated and non-colocated.
Residual risks are process-level (raw git mutations on detached HEAD; `--include-ignored` size
bypass), not config.

## Installs

None. `/usr/bin/time` and `bc` were absent; timing was done via `date +%s%N` / Python instead.
No pacman/uv/npm transactions performed.
