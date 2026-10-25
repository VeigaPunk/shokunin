# W2j jj probe — kake-shokunin

Repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (live branch `master`, HEAD `cb807bc8`).
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kake-shokunin` — deleted after probe (was 3.5M incl. 1.7M .git). Live repo verified untouched afterwards: `git status --porcelain` = 0 lines, branch `master`, no `.jj/` exists.

jj version: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj`).

## 1. Pristine baseline (scratch clone, before jj)

- `node scripts/freshness-sweep.mjs --offline` → **exit 1**. VERDICT: DRIFT — §paths 7 unannotated-miss citations (`~/Projects/webzites`… absent from FS, a pre-existing condition of the lane's docs, unrelated to jj). `--selftest` skipped: it writes hermetic fixtures under `/tmp/kake-r16/selftest` (outside scratch) per its own header. Node v24.21.0.
- `node scripts/probe-delta.mjs` → **exit 2** (`cannot read ~/Projects/webzites/state/probe-history.jsonl: ENOENT`). Correction to an earlier misread: piping to `tail` reported EXIT=0; the true code is 2, matching its contract "2 = unreadable input".

## 2. `jj git init --colocate`

- Init output: "Done importing changes from the underlying Git repo … Initialized repo". Set `trunk()` = `master@origin`; hinted `jj bookmark track master@origin` (not needed for probe).
- First `jj st`: **0.008s**. Reported empty working-copy `@` on top of `cb807bc8 master`; `jj diff --stat -r @` → 0 files changed (repo was already clean — nothing to snapshot).
- `git status` after: clean, "On branch master". `git rev-parse --abbrev-ref HEAD` → `master` (HEAD stays attached while `@` is empty; it detaches only while a jj commit is checked out — observed `HEAD detached` state transiently mid-probe, normal for colocated mode; `jj` reattaches on next `jj` operation that touches HEAD… actually: git sees HEAD detached after jj operations, and `jj` moves `master` bookmark. Git tooling that insists on a symbolic HEAD ref will read `(HEAD detached …)`.)

## 3. Gates re-run after jj init — no change

- `freshness-sweep --offline` → exit **1** (identical DRIFT verdict). `probe-delta` → exit **2** (identical ENOENT).
- Neither script invokes git at all: `grep -rnE 'rev-parse --abbrev-ref|symbolic-ref|git status|git diff --cached|git add|git stash' scripts/ SKILL.md` → no matches. No hooks installed (`.git/hooks/` contains only `*.sample`).

## 4. Lane-identity commit flow — works, but NOT via `--config` flags alone

Tested `kake-shokunin <kake@shokunin.local>`:

- `jj --config user.name=kake-shokunin --config user.email=kake@shokunin.local commit -m test <path>` → `git log -1 --format='%an <%ae> | %cn <%ce>'` = `Joao Pedro Veiga <jpveigao10@gmail.com> | kake-shokunin <kake@shokunin.local`. **Only the committer took the flags.** Root cause (observed): jj stamps the *author* when the working-copy commit is created by the previous jj command (snapshot), before `commit` runs; *committer* is stamped at `jj commit` time and honors `--config`.
- Writing `[user]` into `.jj/repo/config.toml` by hand → **ignored**: repo-scoped config for security reasons lives outside the repo (jj docs, "Configuration — repo settings"), at `jj config path --repo` → `~/.config/jj/repos/<config-id>/config.toml`. `jj config set --repo user.name/user.email` wrote it there and subsequent commits carried `kake-shokunin <kake@shokunin.local>` as **both** author and committer (`git log -1` verified).
- `JJ_USER=kake-shokunin JJ_EMAIL=kake@shokunin.local jj new && jj commit -m …` → also full lane identity both fields (docs: "Environment variable overrides").
- Retroactive fix works: `jj metaedit --update-author -r <rev>` rewrote a mis-authored commit to lane identity (rebased descendants cleanly).
- `jj bookmark set jjprobe -r @-` → `git branch --list` shows `jjprobe`; `git log -1 jjprobe` resolves to the jj-made commit. Git ↔ jj ref interop confirmed.

**Required config for lanes:** `jj config set --repo user.name '<id>-shokunin'` + `jj config set --repo user.email '<id>@shokunin.local'` once per colocated repo (or `JJ_USER`/`JJ_EMAIL` env on every jj invocation). `--config` flags alone produce wrong-author commits — a silent misattribution hazard.

## 5. Hazards

- Special files in live checkout: **none** (`find -type p -o -type s` → empty).
- Untracked files in live checkout: **0** (`git ls-files --others --exclude-standard` → empty; `git status --porcelain` → clean). No surprise snapshot payloads.
- Big ignored files: `.ufo/interactive-sessions/**` = 2.1M + 2.3M `.jsonl`, covered by `.gitignore` line `.ufo/interactive-sessions/` → jj skips them. `snapshot.max-new-file-size = "1MiB"` (jj built-in default, `jj config list --include-defaults`) only matters if a >1MiB *untracked* file appears — currently impossible to hit since untracked set is empty; hazard = future big unignored drops (session logs written outside the ignored dir would be snapshotted at ≤1MiB or error above it).
- Credential-named files: `find` for cred/secret/token/pem/key/env/password/id_rsa patterns → **no matches**.
- `.jj/` coverage: **not in `.gitignore`, but not needed** — jj ships `.jj/.gitignore` containing `/*`, so `git check-ignore .jj/*` → ignored. `git status` stays clean of jj internals automatically.
- Detached-HEAD exposure: while jj has a non-master working-copy checked out, `git rev-parse --abbrev-ref HEAD` → `HEAD` (detached). Any git tool that requires a symbolic branch would misbehave *if* run concurrently during a jj session. No such tool exists in this repo today (scripts are git-free), and `jj` keeps `master` bookmark tracking the branch, so `git checkout master` works normally.

## Verdict

**safe-with-config.** Required: per-repo `jj config set --repo user.name/user.email` for lane identity (env vars acceptable). Top hazard: relying on `--config user.*` silently produces `jpveigao10@gmail.com` authorship on every commit — must be repo config or `JJ_USER`/`JJ_EMAIL`, since jj snapshots the author into the working-copy commit *before* `jj commit` parses its flags.
