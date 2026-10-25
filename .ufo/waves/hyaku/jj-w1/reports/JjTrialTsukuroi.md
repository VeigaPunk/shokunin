# JjTrialTsukuroi — jj colocation trial, lane `tsukuroi`

Seat: `JjTrialTsukuroi-2` · 2026-10-20 · jj 0.45.1 (`/home/vgpnk/.local/bin/jj`) · git 2.56.0
Sandbox: `/fast/scratch/jj-wave/JjTrialTsukuroi/` (remote = `remote.git`, bare clone of the live repo; live repo was never mutated — only `cat`/`git log`/`ls-files`/`status` reads and `git clone --bare`/`rsync -a` out of it).

## Findings (observed)

### Step 1 — sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/tsukuroi-shokunin /fast/scratch/jj-wave/JjTrialTsukuroi/remote.git
git clone .../remote.git .../lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/tsukuroi-shokunin/ .../lane/
git -C .../lane status --porcelain | wc -l        → 0
```

The live lane is **fully committed and clean**: `git status --porcelain` in the live repo = 0 lines, `git ls-files` = 461 tracked files. Only ignored content exists:

```
git status --porcelain --ignored → !! .ufo/interactive-sessions/
git ls-files -o -i --exclude-standard | wc -l → 3
```

Largest untracked/ignored files (bytes, `du -b`):
| bytes | path |
|---|---|
| 1 886 589 | `.ufo/interactive-sessions/20261015T050057Z/…01a13df2….jsonl` |
| 913 039 | same dir `__advisor.jsonl` |
| 2 010 | same dir `11.bash-original.log` |

The largest ignored file (1.8 MiB) exceeds jj's default `snapshot.max-new-file-size` (1 MiB) — relevant to step 3/hazards.

### Step 2 — helper `init`

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialTsukuroi/state \
  /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh init /fast/scratch/jj-wave/JjTrialTsukuroi/lane tsukuroi
```

Output (verbatim, abridged):
```
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Initialized repo in "."
Warning: This setting will only impact future commits.
The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".
To change the working copy author, use "jj metaedit --update-author".   (×2, name+email)
state branch=master local=6923fe0b…bbe remote=6923fe0b…bbe ahead=0 behind=0 head=attached tracked=0 untracked=0
exit=0
```

Repo config readback (`jj --ignore-working-copy config list --repo`):
```
revset-aliases."trunk()" = "master@origin"
snapshot.auto-track = "none()"
user.name = "tsukuroi-shokunin"
user.email = "tsukuroi@shokunin.local"
```

- `git symbolic-ref -q HEAD` → `refs/heads/master` (rc=0): HEAD **attached** after init.
- `git status --porcelain | wc -l` → **0**, identical to step 1 (all untracked paths still `??`/`!!`, none promoted to ` A`).
- Init warnings: only the two author-of-working-copy notices (expected; `@` keeps operator identity until the first `metaedit --update-author`, which the helper's `commit` performs). No `already tracks N added paths` warning.
- `jj status` from the lane dir, 3 runs: **6 ms, 6 ms, 6 ms** (`date +%s%N` deltas; repo is small).
- `.jj/` is hidden from git by `.jj/.gitignore:1 /*` (its own ignore file), not by repo `.gitignore`.

### Step 3 — default auto-track `all()` in a copy

```
cp -a lane lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status          # snapshot: 9 ms, 0 files added (all untracked content is gitignored)
echo > scratch-untracked.txt ; dd if=/dev/urandom of=big-untracked.bin bs=1M count=2
jj status          # snapshot: 16 ms
```

Output:
```
Warning: Refused to snapshot some files:
  big-untracked.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)
Working copy changes:
A scratch-untracked.txt
Untracked paths:
? big-untracked.bin
```

- Files jj would snapshot into @: **1** of the 2 test files (`scratch-untracked.txt`); the 2 MiB file was refused (warning, not fatal — snapshot proceeds without it). With zero non-ignored untracked files (the lane's real steady state), `all()` snapshots **0** files.
- Side effect confirmed in git: `git status --porcelain` showed ` A scratch-untracked.txt` — auto-tracked files appear as **intent-to-add** entries in the git index. `none()` avoids this entirely.
- Copy warning: `jj` prints `Your repo appears to have been copied from …lane/.jj/repo …` — informational only.

### Step 4 — round commit via helper, then operator-push race

Prepared: appended 1 line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `seat-scratch.txt` untracked.

```
HYAKU_STATE=… jj-lane.sh commit . --as tsukuroi -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 2901e235b648191b529a919092d33bec0dc4f9fd
→ pushed    2901e235b648191b529a919092d33bec0dc4f9fd    exit=0
```

Verifications:
- `git log -1 --format` → `author=tsukuroi-shokunin <tsukuroi@shokunin.local>`, `committer=` identical (both stamped correctly).
- `git log -1 --format=%H -- LOG.md` → `2901e235…` = pushed hash.
- `git merge-base --is-ancestor 2901e235 master` → rc=0.
- `jj-lane.sh state .` → `state branch=master local=2901e235… remote=2901e235… ahead=0 behind=0 head=detached tracked=0 untracked=1`.
- `git -C remote.git log -1 master` → `2901e235 round-999: jj trial` — remote has it.
- `cat seat-scratch.txt` → intact; `git status` → `?? seat-scratch.txt` (still untracked).
- HEAD is now **detached** (`head=detached`), matching the known post-mutation behavior; `git rev-parse master` still resolves to `b905bb8…` after step 5's push.

Operator-push race: second clone `operator-clone` committed `considerthese/2026-10-20-daily.md` (identity `Joao Pedro Veiga`) and pushed `a37d912` to sandbox `origin/master` while the lane repo was still at `2901e235`. Then:

```
jj-lane.sh commit . --as tsukuroi -m "round-999: jj trial 2 (post-operator-push)" -- LOG.md
→ committed e6671a1c7b373c11f06d1b5bce97ef0721ccdebb
→ pushed    b905bb869716d1203b94ea8031ffb4086a40a17f   exit=0   (1.18 s wall)
```

`jj-push.err` recorded `Changes to push to origin: bookmark: master [move forward from a37d91235679 to b905bb869716]` — the rejected first push fetched, rebased only the unpushed commit onto `master@origin`, and retried. Final history (`git -C remote.git log master`):
```
b905bb8 round-999: jj trial 2 (post-operator-push)   tsukuroi@shokunin.local
a37d912 considerthese: 2026-10-20 daily reflection   jpveigao10@gmail.com
2901e23 round-999: jj trial                          tsukuroi@shokunin.local
```
**The pushed hash (b905bb8) ≠ the pre-rebase committed hash (e6671a1)** — the helper's printed `pushed` line is the only citeable hash; both invariants (committed-then-pushed, hash-ancestor-of-branch) hold because `pushed` is read back from `heads(master@origin)` after push.

### Step 5 — lane git-touching checks

`tools/` ships 6 files; 5 invoke git read-only plumbing (`git --no-pager -C <root> show|rev-parse`), 1 (`tsukuroi-census.sh`) does not use git but is the lane's headline selftest and was included as a smoke check. Ran against the **colocated** `lane` and a **plain** `lane-plain` clone (no `.jj`), timeout 300 s each:

| Check | jj lane rc | plain clone rc | identical? |
|---|---|---|---|
| `check-section-citations.py --selftest` | 0 (43/43 PASS) | 0 (43/43) | yes |
| `check-section-citations.py --revision HEAD` | 0 `status: PASS` | 0 `status: PASS` | yes — same resolved rev `b905bb8…` |
| `check-root-dac-correction.py --selftest` | 0 (13/13) | — | — |
| `check-root-dac-correction.py --revision HEAD` | 0 `PASS findings=0` | 0 `PASS` | yes |
| `measure-update-recheck.py --revision HEAD` | 0 `status: COUNTED` | 0 `status: COUNTED` | yes — byte-identical `snapshot_sha256` |
| `tsukuroi-census.sh --selftest` | 0 (97/97 PASS, 15.7 s) | — | — |

No colocation-caused failure observed. Every check resolves `HEAD`/`master` through `git rev-parse --verify`, which works under a detached HEAD because `HEAD` points at the branch-tip commit object.

Extra probe — jj mutation resets the git index:
```
git add staged-via-git.txt        → 'A  staged-via-git.txt'
jj describe -m "index-reset probe" → '?? staged-via-git.txt'; git ls-files --stage → 0
```
Confirmed: any `jj` snapshot rewrites `.git/index`; `git add`-staged entries are silently unstaged.

Post-commit upstream state: `git symbolic-ref -q HEAD` rc=1 (detached), `git rev-parse @{u}` → `fatal: HEAD does not point to a branch`, `git status -sb` → `## HEAD (no branch)`. `.jj` dir = 460 K vs `.git` = 9.2 M.

## PASS/FAIL table

| Step | Result | Evidence |
|---|---|---|
| 2 init: colocates, sets 4 repo config keys, HEAD attached, porcelain unchanged | **PASS** | config readback; `symbolic-ref` rc=0; porcelain 0→0 |
| 2 `jj status` ×3 | PASS | 6 ms each |
| 3 auto-track `all()` snapshot | PASS (as documented hazard) | 1 file tracked, 2 MiB refused w/ warning, 16 ms; intent-to-add leak into git index observed |
| 4 helper commit: identity, pathspec limit, pushed hash = `git log -1 -- LOG.md`, ancestor, ahead=0, remote has it, scratch intact | **PASS** | all six checks in step 4 |
| 4 operator-push recovery | PASS | push rejected → fetch+rebase of unpushed commit only → `pushed b905bb8`; remote history linear, operator commit preserved |
| 5 git-touching checks in colocated repo | PASS | 6 runs, all rc=0, identical to plain clone |

## Colocation hazards specific to this lane

1. **Oversized ignored file**: `.ufo/interactive-sessions/**.jsonl` ≈1.8 MiB > jj's 1 MiB `snapshot.max-new-file-size`. Harmless while it stays `.gitignore`d and unnamed — but the helper's `jj file track --include-ignored` **will** admit such a file into a commit if a seat ever names it explicitly. No other large or untracked content exists in this lane.
2. **Intent-to-add leak (killed by config)**: with default `all()`, any non-ignored untracked file silently becomes ` A` in the git index. The helper's `none()` prevents it; verified that `config set` itself uses `--ignore-working-copy` so the fix can't re-pollute.
3. **Detached HEAD / `@{u}`**: after the first helper commit, `@{u}` and `git status -sb` branch line break. Mitigated: the helper's `detect_branch` falls back to `origin/HEAD`→`master`, and all 5 lane tools take explicit `--revision` revs that resolve fine.
4. **Index reset**: every jj mutation unstages `git add` entries. Only matters if a seat mixes `git add` with jj — lanes shouldn't.
5. **Author-of-@**: `jj config set user.*` warns it won't change @'s author; the helper's `metaedit --update-author` before `commit` covers it (verified: author AND committer = `tsukuroi-shokunin <tsukuroi@shokunin.local>`).
6. **Lock naming [INFERENCE]**: `take_lock` keys the flock on `basename "$dir"`; invoking `commit . ` produced lock file `jj-..lock` while `init` with an absolute path produced `jj-lane.lock`. Two spellings of the same repo → two different locks → no mutual exclusion. Orchestrators should always pass the same (absolute) path.
7. Non-hazards verified absent: no symlinks, no nested `.git`, no `.gitattributes`/LFS, no non-sample hooks, no generated build dirs. Remote carries several `cursor/*` branches — untouched by lane pushes (helper pushes only the lane bookmark).

## Recommendations

- Adopt `jj-lane.sh` as-is for `tsukuroi` lane commits; no lane-specific config or `.gitignore` changes needed. Current `.gitignore` (`.ufo/interactive-sessions/`) already covers the only ignored surface, and `.ufo/state/` never exists here.
- Optional hardening [INFERENCE]: add `.ufo/interactive-sessions/` to the helper's never-commit pathspec denylist alongside `.ufo/state/`/`.ufo/watchdog.log`, since `--include-ignored` defeats the `.gitignore` guard for explicitly-named files over 1 MiB.
- Always cite the `pushed` line, never `committed`, when a rebase retry may have occurred (observed: e6671a1 → b905bb8).
- Pass one canonical absolute lane path to the helper so the flock basename is stable.
- Fleet-root commit path unchanged; nothing in this trial argues for or against jj at fleet root.

## Tooling installs

None. `jj 0.45.1` already present at `~/.local/bin/jj`; `bc` and `/usr/bin/time` absent — used `date +%s%N` arithmetic instead (no install needed).
