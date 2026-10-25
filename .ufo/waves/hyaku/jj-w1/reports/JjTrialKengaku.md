# JjTrialKengaku — jj-colocation empirical trial for lane `kengaku`

Seat: `JjTrialKengaku-2` · Date: 2026-10-20 · Lane: `/home/vgpnk/Projects/shokunin/kengaku-shokunin` (branch `master`)
Sandbox: `/fast/scratch/jj-wave/JjTrialKengaku/` · jj 0.45.1 (`~/.local/bin/jj`)
No commands were run inside the live repo except read-only `git status|ls-files|rev-parse|config`, `find`, `cat`, `grep`. No real remote was touched; `origin` in the sandbox = `/fast/scratch/jj-wave/JjTrialKengaku/remote.git`.

## Findings (observed facts, each with its command)

### Step 1 — sandbox build: PASS

```
git clone --bare /home/vgpnk/Projects/shokunin/kengaku-shokunin /fast/scratch/jj-wave/JjTrialKengaku/remote.git
git clone /fast/scratch/jj-wave/JjTrialKengaku/remote.git /fast/scratch/jj-wave/JjTrialKengaku/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kengaku-shokunin/ /fast/scratch/jj-wave/JjTrialKengaku/lane/
git -C .../lane remote -v        → origin /fast/scratch/jj-wave/JjTrialKengaku/remote.git (fetch/push)   [sandbox remote confirmed]
git -C .../lane symbolic-ref -q HEAD → refs/heads/master        (HEAD attached)
git -C .../lane status --porcelain | wc -l        → 0
git -C .../lane status --porcelain --ignored | wc -l → 1   (!! .ufo/interactive-sessions/)
```

The lane ships essentially zero untracked/ignored content: **3 files, all ignored** under `.ufo/interactive-sessions/` (ignored by `.gitignore:1`). Largest untracked/ignored (`git ls-files -o -i --exclude-standard | xargs du -b | sort -rn | head`):

| bytes | path |
|---|---|
| 1,697,078 | `.ufo/interactive-sessions/20261015T050057Z/…01a13df2….jsonl` |
| 790,777 | `…/01a13df2…/__advisor.jsonl` |
| 7,533 | `…/01a13df2…/3.eval.log` |

(Only 3 such files exist.) Largest *tracked*: `corpus/evidence/round12-ladder/results-r12.jsonl` 1,427,319 B — above jj's 1 MiB default, but already tracked so `snapshot.max-new-file-size` does not apply to it.

### Step 2 — colocate through the helper: PASS

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialKengaku/state \
  /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh init /fast/scratch/jj-wave/JjTrialKengaku/lane kengaku
```

- Helper state line: `state branch=master local=6180e4fb… remote=6180e4fb… ahead=0 behind=0 head=attached tracked=0 untracked=0` — exit 0.
- Init warnings (stderr): none from `jj git init --colocate` itself beyond the standard hints; `config set` printed twice:
  `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>". To change the working copy author, use "jj metaedit --update-author".`
  Harmless here — `commit` runs `metaedit --update-author` itself. **No** "working-copy commit @ already tracks N added path(s)" warning (that warning only fires on pre-existing `.jj`).
- Repo config after init (`jj config list --repo`):
  `snapshot.auto-track = "none()"`, `user.name = "kengaku-shokunin"`, `user.email = "kengaku@shokunin.local"`, `revset-aliases."trunk()" = "master@origin"`. Bookmark `master@origin` tracked (init output shows the track hint then tracking).
- `git symbolic-ref -q HEAD` → `refs/heads/master` — **HEAD attached right after init** (matches the known observation that detachment only happens after a jj mutation).
- Porcelain comparison: step1 = 0 entries; step2 = **0 entries** (`--ignored`: 1→2, the second being `!! .jj/` — ignored via `.jj/.gitignore:1:/*`, verified by `git check-ignore -v .jj/`). No untracked path changed state.
- `jj status` timing (3 runs, from the lane dir): **13 ms, 9 ms, 10 ms**. Output: `The working copy has no changes.` `@` = empty commit on top of `master` (`vxrsvklq 6180e4fb`).

### Step 3 — default auto-track `all()` alternative: FAIL (as designed) — confirms why the helper disables it

```
cp -a lane lane-autotrack && cd lane-autotrack
# prepared: appended line to LOG.md, created corpus/lessons/round-999-jjtrial.md,
#           scratch-jjtrial.txt, big-scratch.bin (2 MiB, /dev/urandom)
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status        → snapshot in 19 ms
```

- Files snapshotted into `@` (`jj diff --summary -r @`): `M LOG.md`, `A corpus/lessons/round-999-jjtrial.md`, `A scratch-jjtrial.txt` — **2 new files added, 1 modified**. Git then shows them as staged intent-to-add:
  `git status --porcelain` → ` M LOG.md`, ` A corpus/lessons/round-999-jjtrial.md`, ` A scratch-jjtrial.txt`, `?? big-scratch.bin` — i.e. **auto-track corrupts the git view of the lane: seat scratch becomes "added" in `git status`**.
- Size refusal observed (stderr):
  `Warning: Refused to snapshot some files: big-scratch.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB`
- One extra warning: `Your repo appears to have been copied from …/lane/.jj/repo to …/lane-autotrack/.jj/repo` — cosmetic; note for future trials that `cp -a` of a `.jj` dir is detected.
- The 1.7 MB ignored `.jsonl` did **not** trigger a refusal even under `all()` — auto-track respects `.gitignore`.

### Step 4 — round-commit simulation through the helper: PASS

Prepare (in sandbox lane): appended one line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-jjtrial.txt` (`scratch-content-12345`) untracked.

```
HYAKU_STATE=… jj-lane.sh commit …/lane --as kengaku -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 3003e44c119c8cd9e23afbeb7ff80d86d11d6337
→ pushed    3003e44c119c8cd9e23afbeb7ff80d86d11d6337   (rc=0)
```

Verification:
- `git log -1 --format='author=%an <%ae>%ncommitter=%cn <%ce>' 3003e44c` →
  `author=kengaku-shokunin <kengaku@shokunin.local>` / `committer=kengaku-shokunin <kengaku@shokunin.local>` — lane identity on both.
- `git log -1 --format=%H -- LOG.md` → `3003e44c…` = pushed hash.
- `git merge-base --is-ancestor 3003e44c master` → rc 0.
- `jj-lane.sh state` → `ahead=0 behind=0 head=detached tracked=0 untracked=1`.
- `git -C remote.git rev-parse master` → `3003e44c…` — remote has the commit.
- `scratch-jjtrial.txt` still `??`, content `scratch-content-12345` intact — pathspec limit held.

**Operator-push recovery:**
```
# second clone 'op': committed considerthese/2026-10-20-op.md, pushed → remote master 8df7e85
jj-lane.sh commit …/lane --as kengaku -m "round-999: jj trial part 2" -- corpus/lessons/round-999-jjtrial-2.md
→ committed f6f126bcf698…        (local commit on stale base)
→ pushed    d0a5ac4c71db…        (REBASED hash — the citable one)  rc=0
```
`state/jj-push.err` recorded the rejected push (`bookmark: master [move forward from 8df7e85… to d0a5ac4…]` — the retry line after fetch+rebase). Verified on remote: `master = d0a5ac4`; `8df7e85` (operator) and `3003e44c` (trial-1) are both ancestors (`merge-base --is-ancestor` rc 0 for each); `git show d0a5ac4:corpus/lessons/round-999-jjtrial-2.md` returns the file; the pre-rebase `f6f126bc` is **absent on the remote** (`cat-file` fatal) — the protocol invariant "a cited hash is the pushed hash" held exactly because the helper prints the post-rebase hash.

### Step 5 — lane's own git-touching checks in the sandbox: PASS

SKILL.md's gate registry (`§Gate/probe registry`) has exactly one gate: `hermetic-grader` (`python3 grader.py`; selftest `python3 grader.py --selftest`, S0–S7). `grader.py` contains **no git calls** (the `git ` grep hits are the substring "digit"). The lane's only git-invoking scripts:

| Check | git usage | jj lane rc | plain-clone rc | verdict |
|---|---|---|---|---|
| `sh plans/round24_census.sh` (from repo root) | `git rev-parse --short HEAD` | 0 | 0 | identical output, `HEAD d0a5ac4` — detached HEAD still resolves to a hash |
| `sh corpus/evidence/round11-fleet/mutate_r11.sh` (self-contained; ROOT = `dirname/../../..`; writes only `/tmp/r11-mut` + transient fixed-path mutations restored w/ md5 check) | `git status --porcelain` before/after | 0 | 0 | byte-identical summary lines; `status.before == status.after` (`?? scratch-jjtrial.txt` only in jj lane); all md5s identical |
| `git archive 99cf615 \| tar -x -C /tmp/k24base-jj` (reproducibility recipe for the census baseline, per script header) | `git archive` on pinned historical commit | 0 | n/a | extracted full tree; `plans/round24_census.sh` runs inside it |

All three ran against the sandbox only, all under the 300 s timeout (~5.3 s for mutate_r11). **Zero colocation-caused failures.** mutate_r11's before/after `git status` was identical in the jj lane — the transient tracked-file mutations it performs and restores never reach jj because jj only snapshots on command entry, and no jj command ran mid-script.

## PASS/FAIL table

| Step | Result |
|---|---|
| 1 sandbox build | PASS |
| 2 helper init (config set, HEAD attached, porcelain unchanged, `jj status` 9–13 ms) | PASS |
| 3 `all()` auto-track alternative | CONFIRMED UNSAFE (expected): pollutes `git status` with ` A` intent-to-add; refuses files >1 MiB |
| 4 helper commit+push, identity, ancestor, recovery by fetch+rebase | PASS |
| 5 lane git-touching checks (census, mutate_r11, git archive) | PASS — identical to plain git |

## Colocation hazards specific to the `kengaku` lane

1. **Near-limit tracked files**: `corpus/evidence/round12-ladder/results-r12.jsonl` is 1.4 MB — already tracked so it snapshots fine, but any **new** evidence file >1 MiB (the lane's evidence dirs grow per round) would hit `snapshot.max-new-file-size`. The helper's `jj file track --include-ignored` on named files bypasses the size cap for explicitly committed paths, so lane workflow is safe — but ad-hoc `jj` commands in the lane would refuse.
2. **Ignored session dumps**: `.ufo/interactive-sessions/` (1.7 MB jsonl) is gitignored — invisible to auto-track and to `file track` on directories. Safe as-is.
3. **No `.gitattributes`, no LFS use** — but global `filter.lfs.*` config exists and `filter.lfs.required=true`. If a future round adds `.gitattributes` with `filter=lfs`, **jj does not run clean/smudge filters**; jj-tracked blobs would store smudged working-tree bytes, breaking LFS semantics. [INFERENCE — no `.gitattributes` exists today to test against.]
4. **No nested `.git` dirs, no symlinks, no hooks** in the lane. `find . -type l` empty; `.git/hooks/` samples only. Note: `jj git push` **bypasses git hooks entirely** (pre-push/applypatch hooks would never run) — irrelevant today since none are installed.
5. **`.ufo/` state**: `.ufo/state/` does not exist in this lane (only `rounds/`, `round-17/`, `reports/`, `interactive-sessions/`); the helper's `.ufo/state/*` refusal rule covers the fleet convention anyway. `.jj/` self-ignores via `.jj/.gitignore`.
6. **Detached HEAD**: after any helper commit, `git symbolic-ref HEAD` fails; `git rev-parse HEAD` still resolves (to `@-` = branch tip when `@` is empty). Verified: `round24_census.sh`'s `git rev-parse --short HEAD` printed `d0a5ac4` correctly. Any lane tooling using `git branch --show-current` or `@{u}` would break — none found in this lane.
7. **`git rebase`/`git commit` in the lane would fight jj**: not exercised, but with `auto-track=none()` a manual `git commit` creates a commit jj sees only at next command entry; bookmark/HEAD divergence would then confuse `detect_branch` (which falls back to origin/HEAD). [INFERENCE]

## Recommendations — per-lane config/ignore additions

None strictly required — `kengaku` is the cleanest possible colocation profile (293 tracked files, no symlinks, no LFS attributes, no hooks, all scratch gitignored).

- **No `.gitignore` changes needed.** `.jj/` self-ignores; `.ufo/interactive-sessions/` and `__pycache__/` already covered.
- **Optional belt**: add `*.bin` or a lane-specific scratch pattern (e.g. `scratch-*`, `big-*`) to `.gitignore` so accidental operator scratch can't be `jj file track`ed into a commit; today only named-path tracking protects it.
- **Guard for the future**: if any round introduces `.gitattributes`/LFS or git hooks, flag it — jj bypasses hooks and LFS filters; that is the only realistic break vector for this lane.
- **Fleet note**: keep `snapshot.auto-track="none()"` exactly as init sets it (step 3 shows `all()` pollutes `git status` with intent-to-add entries, which would corrupt any `git status --porcelain`-based fleet accounting — `mutate_r11.sh` itself diffs before/after status and would flag phantom changes).

## Installs
None (jj 0.45.1 pre-existing at `~/.local/bin/jj`; pacman channel paused per operator directive — not needed anyway).
