# W2j jj-colocate probe — tameshi-shokunin

Repo: `/home/vgpnk/Projects/shokunin/tameshi-shokunin` (live branch `master`, 73 tracked files, 5.6 M checkout).
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/tameshi-shokunin` (3.2 M, `git clone --local --no-checkout` + `git checkout master`; **deleted** after probe). jj 0.45.1-7c41cdeb.
Live repo untouched: `git -C <live> status --porcelain` → 0 lines, `rev-parse --abbrev-ref HEAD` → `master` (before and after).

## Verdict: **safe** (with one lane-identity workflow note; no config required)

## 1. Pristine baseline

Gate: `tools/mutate-and-run.sh --selftest` (the only tool in the repo; hermetic — builds fixtures under `mkdtemp`, cleans in `finally`, per SKILL.md gate registry).
- `TMPDIR=<probe tmp> ./tools/mutate-and-run.sh --selftest` → `MUTATE_SELFTEST: 80/80 pass`, `VERDICT: PASS`, exit 0, 5.2 s.
- `--regression` mode **cannot run in any clone**: `FLEET_ROOT=$(dirname³($SELF))` hard-resolves sibling lane repos (`$FLEET_ROOT/kimi-shokunin` etc. for `regression_case_git` legs). In scratch, FLEET_ROOT = `.tower/jj-probe` → legs would hit `revision not found` SETUP failures. Same in live: it only works when the tool sits at `<fleet>/<lane>/tools/`. Pre-existing coupling, not a jj issue.

## 2. `jj git init --colocate`

- `jj git init --colocate` → 0.024 s, "Done importing changes", `trunk()` → `master@origin`, hint to `jj bookmark track master@origin`.
- First `jj st` → **0.007 s**: `@ = ruozrszz 3341f31d (empty)`, parent `4eb4cf31 master master@origin`. Snapshotted nothing: `jj diff --stat -r @` → 0 files.
- `git status --porcelain` after → 0 lines; `git rev-parse --abbrev-ref HEAD` → `master` (still attached).
- `.jj/` self-ignores: `jj git init` writes `.jj/.gitignore` = `/*` → `git status` shows `!! .jj/` only under `--ignored`; `git status -uall` clean. **No repo `.gitignore` change needed.**

## 3. Gates re-run after colocate

- `./tools/mutate-and-run.sh --selftest` → 80/80 PASS, exit 0. No change.
- Index/branch-dependence grep of `mutate-and-run.sh`: **zero** hits for `rev-parse --abbrev-ref`, `symbolic-ref`, `git status`, `git stash`, `update-index`, `diff --cached`, or `git add`/`commit` outside `mkdtemp` fixture repos (`$grepo`). Live-repo git use is read-only object-store access: `rev-parse --verify`, `cat-file -e`, `show <rev>:<path>`, `ls-tree`. Colocation never disturbs these.

## 4. Lane-identity commit flow

- `jj --config user.name=tameshi-shokunin --config user.email=tameshi@shokunin.local commit -m test jj-probe-scratch.txt` → commit `54767fea`, but `git log -1` showed **committer** = lane, **author** = `Joao Pedro Veiga <jpveigao10@gmail.com>` (machine default baked when `@` was created). `--config` on `commit` sets committer only.
- Fix (peer-verified): `JJ_USER=tameshi-shokunin JJ_EMAIL=tameshi@shokunin.local jj metaedit --update-author -r @-` → `fd259183`, `git log -1 --format='%an <%ae> | %cn <%ce>'` → `tameshi-shokunin <tameshi@shokunin.local> | tameshi-shokunin <tameshi@shokunin.local>`.
- `jj bookmark set master -r @-` → git `master` advanced to `fd25918` (`git branch --list -v`: `master fd25918 [ahead 1] test`). Git branch can point at a jj commit. ✔
- Caveat: `--update-author` rewrote the committer too; to preserve distinct committer pass `--config user.name/email` explicitly. For lane identity both-match is intended, so this is fine.

## 5. Hazards

- **Detached HEAD**: after `jj commit`, `git status` → `HEAD detached from refs/heads/master` (jj pins git HEAD to `@`'s parent, not the branch tip). `git switch master` reattaches cleanly; `jj st` stays consistent. Tools that shell `git rev-parse --abbrev-ref HEAD` would read `HEAD` instead of `master` — none in this repo, but fleet-wide greps must allow for it.
- Special files: `find -type p -o -type s` → none.
- Untracked >1 MiB: none. Only ignored path is `.ufo/interactive-sessions/` (per-repo `.gitignore`: `.ufo/interactive-sessions/`); largest member `…24ad.jsonl` = 1.8 M > `snapshot.max-new-file-size` (1 MiB) but jj honors `.gitignore` — `jj st` snapshotted 0 files.
- Credential names: `find -iname '*cred*|*secret*|*.key|*.pem|*token*|.env*|id_rsa*'` → no hits.
- `git fsck` post-jj: only expected dangling objects (rewritten commit ancestors).

## Commands rerun verbatim for reproducibility

`jj git init --colocate`; `jj st`; `jj diff --stat -r @`; `jj --config user.name=… commit -m test <path>`; `JJ_USER=… JJ_EMAIL=… jj metaedit --update-author -r @-`; `jj bookmark set master -r @-`; `git switch master`; `./tools/mutate-and-run.sh --selftest` (pre/post jj).
