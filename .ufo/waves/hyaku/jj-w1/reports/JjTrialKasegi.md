# JjTrialKasegi — empirical jj-colocation trial for lane `kasegi`

Seat: JjTrialKasegi-2. Sandbox: `/fast/scratch/jj-wave/JjTrialKasegi/` (removed after run; nothing worth preserving — all evidence inline below). jj 0.45.1 at `~/.local/bin/jj`. Live repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (branch `master`) was touched read-only only (`git status/ls-files/log`, `cat`, `find`, `grep`, `rsync -a` source side).

## Findings

### Step 1 — sandbox build (PASS)

Commands (verbatim from the brief):

```
git clone --bare /home/vgpnk/Projects/shokunin/kasegi-shokunin /fast/scratch/jj-wave/JjTrialKasegi/remote.git   # done
git clone /fast/scratch/jj-wave/JjTrialKasegi/remote.git /fast/scratch/jj-wave/JjTrialKasegi/lane            # done
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kasegi-shokunin/ …/lane/                 # done
git -C lane status --porcelain | wc -l   → 0
```

`git status --porcelain` = **0 lines**. This lane currently has **zero untracked files**: the only non-tracked payload is gitignored (`.gitignore`: `.ufo/interactive-sessions/`, `__pycache__/`). `git status --porcelain --ignored` shows exactly `!! .ufo/interactive-sessions/`.

Largest untracked-or-ignored files (`git ls-files -o -i --exclude-standard | du -b`):

| bytes | path |
|---|---|
| 2,220,658 | `.ufo/interactive-sessions/20261015T050057Z/…jsonl` |
| 1,525,852 | `.ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl` |
| 4,668 | `.ufo/interactive-sessions/…/7.eval.log` |
| 1,248 | `.ufo/interactive-sessions/…/3.bash-original.log` |

Only 4 ignored files exist (~3.6 MB total). Largest ignored file (2.2 MB) exceeds jj's default `snapshot.max-new-file-size` (1 MiB) but is gitignored, so it never reaches a snapshot. Largest tracked files are ≤100 KB (`.ufo/rounds/round-21/frozen-head-citation-survival.tsv` 100K, `SKILL.md` 84K).

### Step 2 — colocate through the helper (PASS)

Command:

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialKasegi/state scripts/hyaku/jj-lane.sh init /fast/scratch/jj-wave/JjTrialKasegi/lane kasegi
```

- State line printed: `state branch=master local=922a4dde… remote=922a4dde… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Repo config set (`jj config list --repo`):
  ```
  revset-aliases."trunk()" = "master@origin"
  snapshot.auto-track = "none()"
  user.name = "kasegi-shokunin"
  user.email = "kasegi@shokunin.local"
  ```
- Init warnings (stderr): the jj hint about tracking `master@origin` (the helper tracks it via `bookmark track`), and twice `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>"` — the known @-author wart the helper works around with `metaedit --update-author` at commit time.
- `git symbolic-ref -q HEAD` → `refs/heads/master` (**attached** right after init).
- `git status --porcelain` still **0** (unchanged vs step 1); `--ignored` adds `!! .jj/` — via `.jj/.gitignore` containing `/*` (jj self-ignores the colocated dir; `git check-ignore -v .jj/repo/config.toml` → `.jj/.gitignore:1:/*`).
- `jj status` timing ×3: **9 ms, 9 ms, 8 ms** (working copy empty; `jj status` → "The working copy has no changes.").

### Step 3 — default `auto-track = "all()"` alternative (PASS, hazard confirmed)

```
cp -a lane lane-autotrack          # warning: repo appears to have been copied … config file has also been copied
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status                          # 11 ms — snapshots 0 files (lane's only non-tracked content is all gitignored)
```

With real content present (`seat-scratch.txt` + 2 MiB `big-blob.bin` dropped in):

```
jj status → "Warning: Refused to snapshot some files: big-blob.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB"
            "Working copy changes: A seat-scratch.txt"    snapshot: 15 ms
jj diff --summary -r @ → A seat-scratch.txt
git status --porcelain  → " A seat-scratch.txt"   "?? big-blob.bin"
```

Observed: `all()` tracked 1 file into @ in 15 ms; the 2 MiB file hit the `new file too large` refusal and stayed `??`. The critical leak: the jj-tracked file appears to git as ` A` (intent-to-add) — exactly the index pollution the helper's `none()` prevents. Under `none()` in the real sandbox lane, the same 2 MiB file stayed `?`-untracked in jj and `??` in git with no refusal warning.

### Step 4 — round commit via the real helper (PASS)

Prepared: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `lane-scratch.txt` untracked. Then:

```
HYAKU_STATE=… scripts/hyaku/jj-lane.sh commit lane --as kasegi -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 0cc89564250c0cf3e5d10f7f5b14aabc6d589390
→ pushed    0cc89564250c0cf3e5d10f7f5b14aabc6d589390   (exit 0)
```

Verifications (all in sandbox):

- `git log -1 --format='author=%an <%ae> committer=%cn <%ce>' 0cc8956…` → `kasegi-shokunin <kasegi@shokunin.local>` for **both** author and committer.
- `git log -1 --format=%H -- LOG.md` → `0cc89564…` (equals pushed hash).
- `git merge-base --is-ancestor 0cc8956… master` → exit 0.
- `jj-lane.sh state lane` → `ahead=0 behind=0 head=detached tracked=0 untracked=1`.
- `git -C remote.git log -1 --format='%H %s' master` → `0cc8956… round-999: jj trial`.
- `lane-scratch.txt` still `??`, content `leave me untracked` intact. Pathspec limiting works: only the two named paths were committed.
- After the commit, `git symbolic-ref -q HEAD` fails → HEAD is now **detached** (expected colocation behavior).

**Competing-push recovery:** cloned `remote.git` → `operator`, committed `considerthese/operator-note.md` as a different user, pushed (`0cc8956..d5f7ac7`). Then a second helper commit of `plans/jj-trial-second.md`:

```
committed 3db8dd09a446e623c11516cecf195e8ea689e7f1
pushed    05e1772fde37cd0d726833db04ff817c9dfc4457     # rebased — committed ≠ pushed hash
```

Remote log after: `05e1772 (kasegi) → d5f7ac7 (operator) → 0cc8956 (kasegi) → 922a4dd` — linear, no force-push, unpushed commit rebased onto the moved remote tip. `state` → `ahead=0`. **Lesson:** cite the `pushed` hash, never the `committed` one, when the push recovered through rebase.

### Step 5 — lane git-touching checks (PASS)

Lane tools live in `corpus/instruments/` (`anchorcheck.py`, `density.py`, `resolve.py`, `test_resolve.py`). Grep shows `anchorcheck.py` is the **only** instrument invoking git (`git show <hash>:<path>` for pin verification, `anchorcheck.py:120`). `density.py`/`resolve.py`/`test_resolve.py` never touch git (`test_resolve.py` runs `resolve.py` in a subprocess on a fixture; no git calls). Ran three checks, colocated lane vs plain `lane-plain` clone, 300 s timeouts:

| check | colocated lane | plain clone | delta |
|---|---|---|---|
| `python3 corpus/instruments/anchorcheck.py corpus/knowledge/citation-bases.md` | exit 0 — `10 in-range, 0 bad; LOST-RECORDED=1 PIN-BROKEN=0 BASE-ABSENT=1` | exit 0 — identical | none |
| `python3 corpus/instruments/anchorcheck.py SKILL.md` | exit 0 — `7 in-range, 0 bad; LOST-RECORDED=306` | exit 0 — identical | none |
| `python3 corpus/instruments/test_resolve.py` | exit 0 — `Ran 10 tests … OK` | exit 0 — `Ran 10 tests … OK` | none |

No colocation-caused failures. `git show <hash>:<path>` resolves objects regardless of HEAD state, and `find_lane_root` only needs `.git` to exist.

## PASS/FAIL table

| step | result |
|---|---|
| 1 sandbox build | PASS (porcelain 0; only ignored content overlaid) |
| 2 helper init + config + timing | PASS (attached HEAD, 0 porcelain delta, `jj status` ~9 ms) |
| 3 `all()` alternative measured | PASS (1 auto-tracked file → git ` A` leak; 2 MiB refusal; 15 ms) |
| 4 helper commit + push + rebase recovery | PASS (identities correct, ancestry ok, scratch preserved, fetch+rebase recovered) |
| 5 lane git checks in sandbox | PASS (3/3 identical to plain clone; zero colocation-caused failures) |

## Colocation hazards specific to this lane

- **Detached HEAD after every jj mutation** (observed): `git rev-parse '@{u}'` → `fatal: HEAD does not point to a branch` while detached; `git rev-parse master` still works. Any lane tool using `@{u}`/HEAD-as-branch breaks; none found in this lane.
- **Git index reset by jj mutations** (selftest-known; my probe confirmed the inverse risk is real): `git add`-staged entries are `AD` after the file is removed — and under `all()` auto-track, jj-tracked files surface to git as intent-to-add ` A`. Mixed `git add` + `jj commit` workflows are unsafe; the lane must route all writes through the helper.
- **`snapshot.max-new-file-size` = 1 MiB** (observed refusal at 2.0 MiB): irrelevant today (all >1 MiB payload is gitignored `.ufo/interactive-sessions/`), but any future multi-MB corpus artifact needs either `git file track` isn't a thing — it needs the helper's `jj file track --include-ignored` path (helper already handles named files) or a `.gitignore` decision.
- **`.ufo/` bulk**: `.ufo/rounds/` is **tracked** in this lane (100K TSV committed), while `.ufo/interactive-sessions/` and `.ufo/state/` are ignored/protected. The helper already refuses `.ufo/state/*` pathspecs — that rule is load-bearing here.
- **Copied `.jj` dirs**: `cp -a`/`rsync` of a colocated lane copies `.jj/repo` + config and jj warns "repo appears to have been copied". Fleet tooling that rsyncs lane dirs should `--exclude=.jj`.
- **Not present in this lane** (checked, absent): nested `.git` dirs (0 found), symlinks (0), `.gitattributes`/LFS (no file, no `filter` attrs), custom git hooks (only `*.sample`), `__pycache__` (ignored pattern exists but no files).

## Recommendations

1. **Keep `snapshot.auto-track = "none()"`** exactly as the helper sets it; never raise `snapshot.max-new-file-size` per-repo — let explicit `jj file track` handle big paths.
2. **`.gitignore` addition (defense-in-depth, not load-bearing):** add `.ufo/state/` and `.ufo/watchdog.log` to the lane `.gitignore` even though the helper refuses those pathspecs — it makes `git status` truthful for every tool that reads it (state currently shows `untracked=1` noise only because my probe file; real `.ufo/state/` would appear identically).
3. **Fleet rsync/copy rules**: exclude `.jj/` whenever lane directories are copied (the copied-repo warning above), and never copy `.jj` between lanes — per-lane config carries that lane's identity.
4. **No lane-side code changes needed**: the sole git-invoking gate (`anchorcheck.py`) is HEAD-agnostic and passed identically colocated vs plain. `detect_branch` in the helper already prefers `origin/HEAD` over symbolic HEAD, which is what makes `state` correct while detached.
5. **Cite `pushed <hash>` only**: the recovery run demonstrated `committed` (3db8dd09) ≠ `pushed` (05e1772) after rebase; reports citing the committed hash would cite a hash that never reached the remote.

## Installs

None — jj 0.45.1 already present at `~/.local/bin/jj`; no installs or upgrades performed.
