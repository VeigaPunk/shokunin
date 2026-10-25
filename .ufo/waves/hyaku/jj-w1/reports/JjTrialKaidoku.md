# JjTrialKaidoku — jj-colocation trial, lane `kaidoku`

Seat: JjTrialKaidoku-2 · Date: 2026-10-20 · jj 0.45.1 (`~/.local/bin/jj`) · helper `scripts/hyaku/jj-lane.sh` (unmodified)
Sandbox: `/fast/scratch/jj-wave/JjTrialKaidoku/` (remote.git = bare copy of live repo; lane = colocated; lane-autotrack = auto-track copy; lane-plain = plain-git control; operator = second clone). Live repo touched read-only only (clone / rsync source / `git log`).

## Findings (observed, with commands)

### Step 1 — Sandbox build
`git clone --bare <live> remote.git && git clone remote.git lane && rsync -a --exclude=.git --exclude=.jj <live>/ lane/`

- `git -C lane status --porcelain | wc -l` → **8**: 1× ` M .ufo/waves/round-17/run-carriers.sh` (live in-flight edit, faithfully mirrored), 7× `??` (`verify.py`, `w2/`, `wave2-dispatch-attempts.json`, `wave2-dispatch.json`, `wave2-registration.json`, `wave2-result.txt`, `wave2-spec.json`).
- Largest untracked/ignored files (none ignored except inside venv): `wave2-dispatch.json` 132,913 B; `wave2-spec.json` 104,851 B; `wave2-registration.json` 14,953 B; `verify.py` 9,571 B; `wave2-result.txt` 5,130 B; `w2/controls.json` **1,751,824 B** (lives inside untracked `w2/`); venv bits under `arc3-loop1-round4/tools/vyper-venv/` (<1 KiB each).
- Hazard census: **no nested .git dirs** (`find . -name .git -not -path './.git'` → empty); **no active hooks** (only samples); **no .gitattributes / no LFS usage** (git-lfs installed but nothing tracked through it). **Symlinks exist**: venv `bin/python*`, `lib64`, unicode-named `bin/𝜋thon`, `solc-prefix/node_modules/.bin/*`, two `alias-*.conf` — all inside ignored/untracked dirs. Largest tracked file ~6.2 MB (`arc3-loop1-round12/.../function-copy.json`) — over jj's default 1 MiB cap but already tracked, so auto-track doesn't touch it.
- `.gitignore` coverage: root `.gitignore` only covers `__pycache__/`+`*.pyc`; `.ufo/waves/round-17/w2/` and `.ufo/state/` (absent in lane) are **not ignored** — they rely on being merely untracked.

### Step 2 — Colocate via helper
`HYAKU_STATE=…/state jj-lane.sh init lane kaidoku`

- State line: `state branch=main local=da64646… remote=da64646… ahead=0 behind=0 head=attached tracked=1 untracked=7` — **PASS**.
- Init warnings: only the expected `The author of the working copy will stay "Joao Pedro Veiga …"` metaedit hint (cosmetic; commit path stamps identity itself). No file-tracking warnings.
- Repo config set correctly: `snapshot.auto-track="none()"`, `user.name="kaidoku-shokunin"`, `user.email="kaidoku@shokunin.local"`, `revset-aliases."trunk()"="main@origin"`.
- `git symbolic-ref -q HEAD` → `refs/heads/main` (**attached** right after init — PASS).
- `git status --porcelain` after init: **identical 8 lines**; every untracked path still `??`, no intent-to-add — PASS.
- `jj status` ×3 (EPOCHREALTIME deltas): **12.9 ms, 13.1 ms, 14.2 ms**. `git status --porcelain` for reference: 10.6–12.1 ms. jj adds ~2 ms — negligible on this lane.

### Step 3 — auto-track="all()" alternative (lane-autotrack copy)
`cp -a lane lane-autotrack; jj config set --repo snapshot.auto-track '"all()"'; jj st`

- **27 files** snapshotted into `@` as `A` entries (`jj --ignore-working-copy diff --summary -r @ | grep -c '^A '` → 27), mirroring every untracked wave-17 artifact including 13 hidden `.st-*.out` selftest outputs.
- **One `new file too large` refusal**: `.ufo/waves/round-17/w2/controls.json: 1.7MiB (1751824 bytes); the maximum size allowed is 1.0MiB`.
- Snapshot time: **11.1 ms** for `jj st` — fast even while tracking 27 files; the cost is correctness, not speed.
- Git-visible consequence: the 27 files appear as staged ` A` entries (`git status --porcelain | grep -c '^ A'` → 27). Any plain `git commit` would sweep the whole w2/ tree into a commit. PASS as measurement; confirms `none()` is mandatory.

### Step 4 — Simulated round commit
- Prepared: appended LOG.md line, created `corpus/lessons/round-999-jjtrial.md`, left `w2/scratch-jjtrial.txt` untracked.
- `jj-lane.sh commit lane --as kaidoku -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md` → `committed 0ba13fd2…` + `pushed 0ba13fd2…`, exit 0.
- Identity: `git log -1 --format` → `author=kaidoku-shokunin <kaidoku@shokunin.local>` **and** `committer=kaidoku-shokunin <kaidoku@shokunin.local>` — PASS.
- `git log -1 --format=%H -- LOG.md` = `0ba13fd2…` = pushed hash — PASS.
- `git merge-base --is-ancestor 0ba13fd2… main` → exit 0 — PASS.
- `jj-lane.sh state` → `ahead=0 behind=0 head=detached` — PASS (detachment expected post-mutation).
- Sandbox remote `git -C remote.git log -1 main` = `0ba13fd2…` — PASS.
- Scratch file: `cat w2/scratch-jjtrial.txt` → `scratch 1792505945.8111742` intact, still untracked (inside `??` `w2/`) — PASS.
- Commit content: `git show --stat 0ba13fd2` → exactly `LOG.md | 1 +` and `corpus/lessons/round-999-jjtrial.md | 2 ++` — pathspec-limited, run-carriers.sh edit excluded — PASS.
- **Operator-push collision**: second clone pushed `96c16ef operator: add considerthese note` on top of `0ba13fd2`. Helper commit of `corpus/lessons/round-999-jjtrial-2.md` then printed `committed f84fbda9` but **`pushed d898a7e8`** — the rejected push was recovered by fetch + rebase of the single unpushed commit onto the moved `main@origin`, giving it a **new hash**. Remote log: `d898a7e (kaidoku) → 96c16ef (operator) → 0ba13fd` — remote commits untouched, no force-push — PASS.
  - **Citable-hash rule confirmed essential**: anything citing the `committed` line's hash after a rebase-recovery would cite a commit that is not on the remote. Only the `pushed` line is valid.

### Step 5 — Lane's own git-touching gates (3 of 3 registry git-object checks)
Lane has no `tools/`/`scripts/` dir at root; the git-object gates live under `.ufo/waves/round-17/` per SKILL.md's registry. All three use only `git rev-parse/ls-tree/show/cat-file` on explicit revs — object reads, no index/HEAD-symbolic-ref dependence.

| Gate | Colocated lane (`lane`, HEAD detached) | Plain clone (`lane-plain`) |
|---|---|---|
| `controls.py da64646 d898a7e8` | exit 0, full JSON report | exit 0 |
| `temporal-sweep.py --rev d898a7e8 --sites-rev da64646` | exit 0, counts `{corrected:4, sites:4, unqualified:0}` | exit 0, identical counts |
| `invocation-audit.py --rev d898a7e8` | exit 0, counts `{rows:17, exercised_match:5, unlabelled_variant:12}` | exit 0, identical counts |

**Zero colocation-caused failures.** These gates are rev-pinned, so detached HEAD is a non-issue for them. Untested risk remains for any gate that does `git rev-parse --abbrev-ref HEAD`, `@{u}`, `git stash`, or relies on the index — none of the three registry git gates do.

## PASS/FAIL table (steps 2–5)

| Step | Check | Result |
|---|---|---|
| 2 | init state line ahead=0/behind=0/attached | PASS |
| 2 | repo config (auto-track none, identity, trunk alias) | PASS |
| 2 | HEAD attached after init | PASS |
| 2 | porcelain unchanged vs step 1 (8 lines, `??` preserved) | PASS |
| 2 | `jj status` latency (13–14 ms) | PASS |
| 3 | auto-track measurement (27 files staged, 1.7 MiB refusal, 11 ms) | PASS (hazard confirmed, not adopted) |
| 4 | commit prints `committed`+`pushed`, exit 0 | PASS |
| 4 | author+committer = lane identity | PASS |
| 4 | LOG.md tip == pushed hash; ancestor of main; remote has it; state ahead=0 | PASS |
| 4 | scratch file untracked + intact; commit pathspec-limited | PASS |
| 4 | moved-remote recovery via fetch+rebase, pushed≠committed, no force/rewrite | PASS |
| 5 | controls.py / temporal-sweep / invocation-audit | PASS ×3, identical to plain-clone control |

## Lane-specific colocation hazards

1. **Untracked wave scratch is large and un-ignored.** `.ufo/waves/round-17/w2/` (≈1.8 MB incl. `controls.json` at 1.7 MiB > jj's 1 MiB cap) and `wave2-*.json` are `??` but not `.gitignore`d. Under default auto-track they would enter `@` (and the git index as intent-to-add); one file refuses outright. `auto-track="none()"` is required, exactly as the helper sets.
2. **git-staged state is fragile across jj mutations** — measured: a `git add`-staged path survived `jj status` untouched (jj did *not* import it into `@` under `none()`), but the next `jj commit` reset the index and the file fell back to untracked. No data loss, but any fleet-side `git add && git commit` choreography in a lane must be retired; jj-lane.sh commit is the only safe committer.
3. **HEAD detaches after the first jj mutation** (`head=detached`, at the branch tip). `git rev-parse HEAD`, `git log`, `merge-base`, `show`, `ls-tree` all work; `@{u}`/`--abbrev-ref HEAD`/`git pull`/`git status -sb` upstream hints do not. The helper's `detect_branch` (origin/HEAD fallback) already copes.
4. **committed ≠ pushed under remote contention.** Rebasing unpushed commits rewrites their hashes. Reports must cite the `pushed` line only.
5. **Symlinks & unicode filenames exist** (venv `𝜋thon`, `node_modules/.bin`) but all inside ignored dirs; jj snapshot didn't choke on them, and `none()` keeps them out anyway. No nested .git, no LFS, no hooks, no .gitattributes.
6. **`.ufo/state/` protection is by helper path filter, not by .gitignore** — the lane has no `.ufo/state/` currently; the helper rejects `.ufo/state/*` and `.ufo/watchdog.log` by argument check regardless of ignore files.
7. **`jj git push` conflict-tree footgun** is guarded by the helper's `conflicts()` precheck (not triggered here; no conflicts produced).

## Recommended per-lane config / ignore additions

```gitignore
# kaidoku-shokunin/.gitignore — append
.ufo/state/
.ufo/waves/*/w2/
.ufo/watchdog.log
```
Rationale: belt-and-suspenders. `auto-track="none()"` already keeps scratch out of `@`, but `.gitignore` also protects against any future lane-side plain-`git add .`/`-A` accident and silences the `??` noise in `git status` that seats read for "did I leave debris". The per-round `w2/` glob covers the recurring wave-scratch convention; `.ufo/state/` defense-in-depth matches the helper's hard filter. Do **not** ignore `wave2-*.json` at round root — dispatch specs are occasionally committed deliberately (precedent: round-16 wave files are tracked); leave that to pathspec choice.

No other config changes needed: helper-set `snapshot.auto-track="none()"`, identity, and `trunk()` alias verified correct; do not raise `snapshot.max-new-file-size` (the 1 MiB refusal was protective — w2/controls.json should never be committed).

## [INFERENCE]

- jj's git-index reset happens on *mutation* (commit), not on read-only `jj status` — consistent with the helper selftest note but worth stating precisely: staged entries persist through snapshots, die at commit.
- The three registry git gates are insensitive to colocation because they pin explicit revs; the lane's real residual risk is any *unregistered* script that branches on `git symbolic-ref HEAD` or does its own `git add`. A `grep -rln 'symbolic-ref\|rev-parse --abbrev-ref\|git stash\|git add' .ufo/` sweep would be the cheap follow-up audit.
- For fleet-root repos with many seat sandboxes, auto-track all() would stage thousands of files; `none()` + explicit `jj file track` is the only viable posture, matching the helper.

## Files / artifacts

- Report only file written outside sandbox: this file.
- Sandbox `/fast/scratch/jj-wave/JjTrialKaidoku/` left in place (contains lane, lane-autotrack, lane-plain, operator, remote.git, state/) — remove on integrator confirmation; nothing in it needs preserving beyond this report.
- Installs: none. (`/usr/bin/time` and `bc` absent; used `$EPOCHREALTIME`/`awk` instead. No tool installs were needed.)
