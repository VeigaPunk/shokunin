# kaika W2j — jj colocate probe: `audio-shokunin`

Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin` (live branch `main` @ `defbe128`)
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/audio-shokunin` (deleted after probe; size 1.5 G incl. `.git` + `.jj`, measured with `du -sh .`)
jj: `jj 0.45.1-7c41cdeb` at `~/.local/bin/jj`
Probe time: 2026-10-19 ~18:30–18:45 UTC.

## Live-repo facts (read-only)

- `git status --porcelain` → **0 lines** (clean). `git rev-parse --abbrev-ref HEAD` → `main`.
- `git ls-files | wc -l` → **50,213** tracked; working tree `du -sh --exclude=.git` → **1.4 G** (≈1.28 G of it in `corpus/live`).
- Identity: no repo-local `user.name`/`user.email`; falls back to global `ci <ci@local>` (`git config user.name` in repo → `ci`).
- **Untracked-but-not-ignored files: none.** `git ls-files --others --exclude-standard` → 0 lines. (`git ls-files --others` without excludes shows only gitignored `Timing*.plot`/`Timings.html` regenerates.) → A colocated `jj st` in the live repo would snapshot **nothing new**; first-commit risk from file contents is nil.
- **Special files: 18 FIFOs** under `corpus/live/r68-scout/fifo/` (`stat` → `prw-r--r--`, size 0, e.g. `nd_noext`, `nd_riffx.wav`, `nd_zeros.*`, `noext_member`, `smp_*.wav`, `txw_*.wav`). `git check-ignore corpus/live/r68-scout/fifo/nd_noext` → exit 1 (not ignored; git simply cannot track FIFOs). No sockets, no devices (`find -type p/s/b/c` → only the 18 FIFOs).
- Credential-looking names: none that are credentials. `find` for `*credential*|*secret*|.env*|*token*|id_rsa*|*.pem|*.key` returned only corpus receipt/fixture files whose names contain "key" (e.g. `corpus/live/r88-boundary/receipts/B11-keyset.json`, `key_lines.log`) — all tracked corpus data, no secrets.
- Untracked files >1 MiB: none (untracked set is empty). Largest tracked-untracked risk class doesn't apply.
- Hooks: `.git/hooks/` contains only `*.sample` files — **no active git hooks** for jj to bypass.
- Git dependence in tooling: `grep -rn 'rev-parse\|symbolic-ref\|git status\|git diff --cached\|git add\|git stash'` over `corpus/fixtures/*.py *.sh *.c`, `generate_timings.sh` → **no hits**. The only `git` mentions are comments inside `measure_audio.py` ("`git archive` / per-seat tree copies…"), not invocations.

## Checklist 1 — pristine baseline (scratch clone)

Scratch created per protocol: `git clone --local --no-checkout <live> <scratch>` then `git -C <scratch> checkout main` (1.90 s).

Read-only gate found: the repo's self-test battery is `corpus/fixtures/test_*.py` (13 files; unittest). Four tests spawn inert children and three write tempdirs under `/tmp` — all use `tempfile.TemporaryDirectory`, self-clean, no network, no writes to the live repo. Ran the full suite:

- `cd scratch/corpus/fixtures && python3 -m unittest discover -s . -p 'test_*.py'` → **Ran 59 tests in 14.351s — OK** (exit 0).

## Checklist 2 — `jj git init --colocate`

- `jj git init --colocate` → "Done importing changes from the underlying Git repo"; set `trunk()` alias to `main@origin`; hint to `jj bookmark track main@origin`.
- First `jj st` wall time: **0.079 s** (user 0.125 s, sys 1.662 s — the 50k-file/1.4 G tree snapshots cheap; jj fingerprints rather than re-hashing unchanged content).
- `jj st` output: "The working copy has no changes." `@ = osskqwno c94d9995 (empty)`, `@- = defbe128 … main main@origin`.
- `jj diff --stat -r @` → **0 files changed** — nothing snapshotted (consistent with 0 untracked files; see FIFO result below).
- `git status` after init: **clean**. `git rev-parse --abbrev-ref HEAD` → **main** (still attached at this point).
- `.jj/` coverage: `git status --ignored` shows `!! .jj/` — jj writes `.jj` into `.git/info/exclude` automatically at init. **No `.gitignore` edit needed.**

## Checklist 3 — gates re-run after init

- Same `python3 -m unittest discover -s . -p 'test_*.py'` → **Ran 59 tests in 13.191s — OK** (exit 0). **No exit-code change; zero branch/index dependence** (matches the grep finding: no fixture invokes git at all).

## Checklist 4 — lane-identity commit flow

- `jj commit -m test jj-probe-scratch.txt` with `--config user.name=audio-shokunin --config user.email=audio@shokunin.local` produced a commit whose `git log` shows:
  - `audio-shokunin <audio@shokunin.local> | audio-shokunin <audio@shokunin.local> | test` — **but only after fixing the author** (see pitfall). Raw `--config` run produced `Joao Pedro Veiga <jpveigao10@gmail.com>` (global jj `user.name`) as **author** and `audio-shokunin` as **committer**.
- **Pitfall (verified):** the commit author is stamped when the working-copy change is *first snapshotted* (first `jj st`), not at `jj commit` time. `--config` on the commit command only affects the committer. Fix that works: `jj config set --repo user.name 'audio-shokunin' && jj config set --repo user.email 'audio@shokunin.local'` **before the first `jj` command in the repo** — or repair after the fact with `jj metaedit -r <change> --update-author` (verified: flipped author to `audio-shokunin <audio@shokunin.local>`; committer already correct).
- After repo-level config was set, a second commit (`echo probe2 > probe2.txt; jj commit -m 'lane test commit' probe2.txt`) showed `git log -1 --format='%an <%ae> | %cn <%ce>'` → `audio-shokunin <audio@shokunin.local> | audio-shokunin <audio@shokunin.local>` ✓
- Bookmark → git branch: `jj bookmark create lane-audio-probe -r @-` → `git branch --list` shows `lane-audio-probe` ✓ (`main` also intact at `defbe128`).
- `git checkout lane-audio-probe` works; next `jj st` logs op `import git head` and resets the working-copy parent to the new HEAD — bidirectional interop confirmed; `jj undo` then cleanly undid the import.

## Checklist 5 — hazards

1. **FIFOs — benign.** Recreated `corpus/live/r68-scout/fifo/nd_noext` with `mkfifo` in scratch: every `jj` command (`st`, `commit`, `new`, `undo`) completed in <1 s; `jj file list` reports no such path; `jj diff --stat` → 0 files. jj **silently skips** non-file/non-symlink/non-dir entries — no block-on-open, no error, no warning. (Matches jj's fileset docs: only regular files, symlinks and directories participate; https://jj-vcs.github.io/jj/latest/filesets/.)
2. **`snapshot.max-new-file-size` trips on `__pycache__`.** Running the fixture suite creates `corpus/fixtures/__pycache__/measure_audio.cpython-314.pyc` = **2.9 MiB** (> default 1.0 MiB). Every subsequent jj command prints "Refused to snapshot some files" (warning, not error — the file stays untracked). `.gitignore` currently does NOT cover `__pycache__`. → Add `__pycache__/` to `.gitignore`, or live with the warning.
3. **HEAD goes permanently detached.** After any jj working-copy change, `git rev-parse --abbrev-ref HEAD` → `HEAD` and `git symbolic-ref HEAD` → fatal "ref HEAD is not a symbolic ref" — even after `jj new main`. Documented behavior: "jj commands will usually put the Git repo in a 'detached HEAD' state" (https://jj-vcs.github.io/jj/latest/git-compatibility/, "Colocated Jujutsu/Git repos"). Any tool parsing `--abbrev-ref` for the branch name breaks; none exists in this lane today, but lane scripts elsewhere may assume it.
4. **jj stages untracked files in the git index.** Once jj snapshots a new file, `git status` shows it as `A` (staged add); modifications to tracked files stay ` M`. Docs: staging area "will be ignored" by jj — but git tools see jj's snapshot staged. A stray `git commit -a` in a colocated repo would commit exactly what jj snapshotted.
5. **Author ≠ configured identity on first snapshot** (checklist 4). Mitigation is repo-level `jj config set --repo user.*` as part of init, before anything else runs jj.
6. No credentials, no >1 MiB untracked files, no active hooks in the live checkout.

## Verdict

**safe-with-config.**

Required config at adoption time:
```sh
jj git init --colocate
jj config set --repo user.name 'audio-shokunin'
jj config set --repo user.email 'audio@shokunin.local'
```
plus one `.gitignore` line `__pycache__/` (repo-root `.gitignore`) to silence the 2.9 MiB `snapshot.max-new-file-size` refusal.

Top hazard: **permanently detached git HEAD in colocated mode** — `git rev-parse --abbrev-ref HEAD` returns `HEAD`, so any future lane tooling that reads the branch name that way will break. Runner-up: commit *author* silently falls back to global `user.name` if identity isn't repo-configured before the first snapshot (committer alone honors `jj commit --config`).

Restoration: scratch clone deleted after recording path/size; live repo untouched (only read-only `git status`/`ls-files`/`check-ignore`/`find`/`stat` were run against it).
