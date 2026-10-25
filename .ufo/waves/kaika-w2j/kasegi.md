# jj colocate probe — kasegi-shokunin

**Verdict: `safe-with-config`.** Required config: `git config user.name/user.email` lane values in-repo so `jj` uses them without per-command flags (jj falls back to `JJ_USER`/`JJ_EMAIL`/`user.name` config; author of `@` is fixed at commit creation — use `jj metaedit --update-author` if @ was created before identity is set). Top hazard: **git HEAD detaches** (`git rev-parse --abbrev-ref HEAD` → `HEAD`) as soon as jj moves `@` to any fresh commit — including `jj new master` where @- carries the `master` bookmark — and never reattaches. Any tool reading branch identity (watchdog, `git branch --show-current`) sees "detached", not "master".

- Live repo: `/home/vgpnk/Projects/shokunin/kasegi-shokunin`, branch `master` @ `94aace220d45bc75bb728dc2a01a94d9fc85cdbe`.
- Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kasegi-shokunin` (`git clone --local --no-checkout` + `git checkout master`), 2.8 MiB at creation; deleted after probe. Live repo never touched by jj.

## 0. Live-repo pre-flight (read-only)

- `git status --porcelain` → **0 lines** (clean; nothing untracked-but-not-ignored).
- `git ls-files` → 94 files; worktree 4.8 MiB (`du -sh --exclude=.git`); largest tracked `.ufo/rounds/round-21/frozen-head-citation-survival.tsv` 102 KiB.
- `find . ! -type f ! -type d` (excluding `.git`) → **no FIFOs/sockets/special files**; no symlinks.
- `git status --porcelain --ignored` → 1 ignored entry: `.ufo/interactive-sessions/` (`.gitignore` lines: `.ufo/interactive-sessions/`, `__pycache__/`). It holds one 1.5 MiB session file — ignored, so jj will not snapshot it.
- `git ls-files --others --exclude-standard` → empty → **no untracked files to sweep into a snapshot; `snapshot.max-new-file-size` non-issue**.
- Credential-like names (`*cred*`, `*secret*`, `*.pem`, `*.key`, `*token*`, `.env*`, `id_rsa*`) → **none**.
- `.git/hooks/` → no non-sample hooks. `git stash list` → 0.

## 1. Pristine baseline (scratch, pre-jj)

Gates found in `corpus/instruments/` (SKILL.md gate registry = instruments/README.md):

| gate | cmd | exit | key output |
|---|---|---|---|
| anchorcheck | `python3 -B corpus/instruments/anchorcheck.py SKILL.md` | 0 | `7 in-range, 0 bad; LOST-RECORDED=306 PIN-BROKEN=0 ORIGIN=0 OUTSIDE-BASE=0 BASE-ABSENT=0` |
| density | `python3 -B corpus/instruments/density.py SKILL.md` | 0 | mean dens **154.0**, 645 cites / 18 blocks |
| resolve | `python3 -B corpus/instruments/resolve.py .` | 0 | `skill=33/506 corpus=143/1212 all=159/1539` (writes committed `citation-survival.{md,tsv}` → `git restore`ed after) |
| regressions | `python3 -B corpus/instruments/test_resolve.py` | 0 | `Ran 10 tests … OK` |

No gate writes outside the repo (resolve writes `citation-survival.*` in-tree; test_resolve's `dir=HERE` fixture is repo-local). No network/credentials needed.

## 2. `jj git init --colocate`

- Init: `real 0m0.020s`, "Done importing changes from the underlying Git repo"; alias `trunk()` → `master@origin`; hint to `jj bookmark track master@origin`.
- First `jj st`: `real 0m0.006s` — "working copy has no changes", `@` empty on top of `94aace22` (`master master@origin kaika/round@origin` — note: an extra remote-tracking bookmark `kaika/round` exists at origin HEAD; `jj` displays it on the same commit).
- `jj diff --stat -r @` → `0 files changed` → **nothing snapshotted** (tree was clean).
- `git status` after init: still "On branch master, nothing to commit". `git rev-parse --abbrev-ref HEAD` → **`master`** (HEAD attached at this point).
- `.jj/` dir: 260 KiB. jj writes `.jj/.gitignore` containing `/*` → `.jj` invisible to git (`git status` stays clean, `git add -A` can't embed it). **No tracked-`.gitignore` change needed** (self-ignored; the context's "`.gitignore` coverage needed for `.jj/`" concern does not apply).

## 3. Gates re-run after jj init

Identical exits and identical summary lines for all four gates (anchorcheck `7/0/306/0/0/0/0` exit 0; density 154.0 exit 0; test_resolve `Ran 10 … OK` exit 0; resolve exit 0). Branch-dependence grep over repo sources: only `corpus/instruments/anchorcheck.py:120` shells out to git — `git -C <repo> show <obj>:<path>` for PIN cites — object-store-only, works under detached HEAD (proven: ran post-detach, exit 0). **No in-repo tool uses `rev-parse --abbrev-ref`, `symbolic-ref`, `git status`, `diff --cached`, `git add`, or `git stash`.**

## 4. Lane-identity commit flow

- `echo > .jj-probe-marker.txt` then (per W2jScribe correction — `--config user.name/email` sets committer only; `@`'s author is fixed at creation): `JJ_USER=kasegi-shokunin JJ_EMAIL=kasegi@shokunin.local jj metaedit --update-author -r @` then `jj --config user.name=kasegi-shokunin --config user.email=kasegi@shokunin.local commit -m test .jj-probe-marker.txt` → commit `d70d40f3`.
- `git log -1 --format='%an <%ae> | %cn <%ce>'` → **`kasegi-shokunin <kasegi@shokunin.local> | kasegi-shokunin <kasegi@shokunin.local>`** — author AND committer correct (requires the `metaedit --update-author` step; without it author = `vgpnk@plazir27` machine default, which is exactly why `--config` alone is insufficient).
- `jj bookmark set probe-test -r @-` → `git branch --list` shows **`probe-test` → `d70d40f3`**. jj bookmarks map 1:1 to git branches. ✅

## 5. Hazards

1. **Detached git HEAD (the real finding).** After `jj commit`, `git rev-parse --abbrev-ref HEAD` → `HEAD` ("detached from refs/heads/master"). `jj new master` — whose @- *carries* the `master` bookmark — still leaves HEAD detached ("detached at refs/heads/master"). jj 0.45.1 colocated never reattaches HEAD once it detaches (docs: https://jj-vcs.github.io/jj/latest/git-compatibility/ "The HEAD pointer in colocated repos is updated to point to the parent of the working-copy commit" — detached unless @- is a branch tip; observed behavior detaches even then). Impact: any external tool reading branch name sees `HEAD`. kasegi's own gates are unaffected (proven), but fleet-level tools (`scripts/shokunin-watchdog.sh`, driver commit flows) must be audited before fleet adoption.
2. **Untracked → committed.** `echo > untracked-demo.txt && jj st` → `A untracked-demo.txt` in `@` — any future unignored junk file in the live lane will be silently committed by the next jj command. Live repo currently has zero untracked files (see §0), so adoption-time risk is nil; `.gitignore` hygiene must be kept.
3. **`.ufo/interactive-sessions/` is ignored** → excluded from jj snapshots; a 1.5 MiB ignored file present costs nothing. `__pycache__/` ignored. No untracked >1 MiB → `snapshot.max-new-file-size` irrelevant here.
4. Special files: none. Credential-like names: none. Hooks: none (no hook migration needed — but note jj does not run git hooks; `commit.template`/pre-commit gates in other repos would be bypassed — not applicable here).

## 6. jj value demonstrated

`jj op log` shows every mutation (snapshot/bookmark-point/new/commit with args); `jj undo` restored the pre-`jj st` op and **deleted the untracked file back out of the tree** ("removed 1 files"), `git status` stayed clean. Working-copy-as-commit + undo work end-to-end in this repo.

## 7. Cleanup

Scratch `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kasegi-shokunin` (2.8 MiB → ~3.1 MiB with `.jj`) deleted post-probe. Live repo untouched: all jj commands ran inside the scratch clone; the `probe-test`/`probe-test2`/`test` commits exist only in the deleted clone (objects shared via `--local` clone hardlinks are in the clone's own .git — `--local` uses hardlinks, so `d70d40f3`/`54ad586a`/`88fe6c85` objects are *reachable only from the scratch* and disappear with it; verify live repo has no `probe-test*` refs: refs were never written to the live `.git`).
