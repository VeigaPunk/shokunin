# kaika W2j — jj colocate probe: `kagi-shokunin`

**Verdict: `safe-with-config`.** Required config: repo-scoped jj identity
(`jj config set --repo user.name kagi-shokunin`, `… user.email kagi@shokunin.local`).
Top hazard: jj `commit` stamps **author** from persistent `~/.config/jj` config, so a
`--config user.name=…` CLI override produces the right committer but the *operator's*
personal name as author — lane attribution wrong until repo config or `jj metaedit --author`
fixes it. No other blocker found.

## Environment

- Probe repo: `/home/vgpnk/Projects/shokunin/kagi-shokunin`, live branch `master`,
  HEAD `aea7a43` ("kagi: dotenv byte-contract observations…").
- Live `git status --porcelain`: **empty** (clean; zero untracked files).
- jj: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` at `~/.local/bin/jj`.
- Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kagi-shokunin`,
  `git clone --local --no-checkout` + `git checkout master`; 89 tracked files, ~3.0 MB.
  Final scratch size 3.4 MB (`.git` 1.9 MB + `.jj` 256 KB); **deleted after probe**.

## 1. Pristine baseline gates (scratch, before jj)

Repo has no `tools/`/`scripts/`/`verifiers/`; gates live in `corpus/*.sh` (registry in
SKILL.md gate table). All grep-verified free of `git`/`rev-parse`/`symbolic-ref`/`git status`/
`git diff --cached`/`git add`/`git stash`/hooks references. `op-ref-probe.sh` is structurally
guarded (env-file guard refuses ref tokens → no vault contact); `surface-census.sh --verbs`
and `--deep` skipped per SKILL.md ("operator present" only). Every gate exits 0 while
printing its verdict word — verdicts below are the baseline, identical under jj:

| Gate | Verdict line (tail) | Exit |
|---|---|---|
| `bash corpus/surface-census.sh` | `SURFACE_CENSUS: DRIFT (diverged=1 gone=23 … absent=37)` | 0 |
| `bash corpus/scope-gate.sh` | `BREADTH_AUDIT: DEFECT … ADJACENCY_SCOPE: DEFECT` | 0 |
| `bash corpus/checklist-run.sh` | `CHECKLIST_RUN: BROKEN (items=16 runnable=9 failed=6)` (missing host `janitor.md`) | 0 |
| `bash corpus/claim-ledger.sh verify` | `CLAIM_LEDGER: FAIL (claims=35 failed=3 deferred=11 stale=9)` | 0 |
| `bash corpus/claim-ledger.sh docs` | `DOC_AUDIT: CLEAN (entries=21 row_linked=18)` | 0 |
| `bash corpus/drift-pins.sh` | `DRIFT_PINS: DRIFT (files_ok=0 files_bad=15 symbols_bad=20)` | 0 |
| `bash corpus/transcript-scan.sh` | `transcript-scan: db not found: …/opencode.db` | 0 |
| `bash corpus/op-ref-probe.sh` | `OP_REF_PROBE: SETUP (janitor binary not executable)` | 0 |

Baseline note: all DRIFT/DEFECT/FAIL verdicts are **host-environment** absences
(`the-janitor`, `tac/`, `opencode.db` not installed on this box), not repo defects —
an "inconclusive baseline" for green/red purposes but a valid comparator for the jj delta.

## 2. `jj git init --colocate`

```
$ jj git init --colocate
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Hint: The following remote bookmarks aren't associated with the existing local bookmarks:
  master@origin
Hint: Run `jj bookmark track master@origin` to keep local bookmarks updated on future pulls.
Initialized repo in "."
```

- First `jj st`: **5 ms** (repo is 3 MB; trivial). Output: working copy = new empty change
  `kxtzkrpy a12a5bc9` on top of `aea7a430` (`master`, `master@origin`, `kaika/round@origin`).
- `jj diff --stat -r @`: `0 files changed` — nothing snapshotted (clean worktree).
- `git status --porcelain` after init: **empty**. `git rev-parse --abbrev-ref HEAD`: `master`
  (symbolic-ref `refs/heads/master` — **no detached HEAD**, branch preserved).
- `.jj/` invisible to git: jj writes `.jj/.gitignore` containing `/*`; verified via
  `git check-ignore -v .jj/` → match on `.jj/.gitignore:1:/*`; `git status --ignored` shows
  `!! .jj/`. **No `.gitignore` coverage needed.**

## 3. Gates re-run under jj

All eight gates re-run in the colocated scratch: **every verdict line and exit code
byte-identical to baseline** (same table above; `claim-ledger verify` still FAIL with
identical counts, `docs` still CLEAN, etc.). Combined with zero `git` references in the
scripts: **no branch- or index-dependence**. No hooks configured
(`ls .git/hooks | grep -v sample` → empty; `core.hooksPath` unset).

## 4. Lane-identity commit flow

Command as specified:

```
$ jj --config user.name=kagi-shokunin --config user.email=kagi@shokunin.local \
    commit -m test plans/jj-probe-scratch.txt
$ git log -1 --format='%an <%ae> | %cn <%ce>'
Joao Pedro Veiga <jpveigao10@gmail.com> | kagi-shokunin <kagi@shokunin.local>
```

**Finding (top hazard):** `jj commit` finalizes the *change created by the earlier
snapshot*, whose author was stamped from persistent jj config
(`jj config list user` → `user.name = "Joao Pedro Veiga"`, global `~/.config/jj`).
The `--config` flag set only the **committer** on the new commit — author stayed the
operator's personal identity. In a secrets/vault lane this leaks operator identity into
authored commits and breaks lane attribution. jj 0.45.1 `describe` has **no**
`--reset-author`/`--author` flag; the retroactive fix is `jj metaedit`:

```
$ jj metaedit @- --author 'kagi-shokunin <kagi@shokunin.local>'
$ git log -1 --format='%h %an <%ae> | %cn <%ce>'
e72112e kagi-shokunin <kagi@shokunin.local> | Joao Pedro Veiga <jpveigao10@gmail.com>
```

(metaedit updates author only; committer keeps whatever produced the rewrite.)

**Required config (fixes both fields for all future changes):**

```
$ jj config set --repo user.name kagi-shokunin
$ jj config set --repo user.email kagi@shokunin.local
```

Written to `~/.config/jj/repos/<repo-id>/config.toml` (repo-scoped, not in-tree — the
`.jj/repo/` dir is internal state). Verified: subsequent `jj commit -m test2` produced
`1f6b551 kagi-shokunin <kagi@shokunin.local> | kagi-shokunin <kagi@shokunin.local>` —
both fields correct with no per-command flags.

Bookmark→branch cutover verified:

```
$ jj bookmark set kagi-test -r @-   →  git branch --list kagi-test → kagi-test
$ git log -1 kagi-test → 1f6b551 test2          # same commit, real refs/heads/kagi-test
$ jj undo                                        # removed the bookmark (op log works)
```

`jj op log` records every operation (`commit`, `bookmark`, `undo` shown with args and
millisecond durations) — the adoption-value claims hold on this repo.

## 5. Hazards

- **Special files (FIFOs/sockets/devices/symlinks):** `find . -path ./.git -prune -o
  ! -type f ! -type d -print` over the live checkout → **none**.
- **Untracked >1 MiB:** none — `git status --porcelain` is empty; zero untracked files.
  (Default `snapshot.max-new-file-size = "1MiB"`, confirmed via
  `jj config list --include-defaults snapshot`, would hard-fail every jj command if a
  >1 MiB untracked file ever appears unignored — note for future lane hygiene, not a
  current blocker.)
- **Credential-looking untracked names (secrets/vault lane audit):** none. `git status
  --porcelain` empty; union of tracked + ignored paths grep'd against
  `secret|cred|token|vault|password|passwd|\.pem$|\.key$|\.env|private|\.p12|id_rsa`
  yields only documentation: `corpus/knowledge/cdp-bridge-1password.md`,
  `corpus/knowledge/credential-isolation.md` (already tracked). Ignored-dir file names
  in `.ufo/interactive-sessions/` (3 files, 2.8 MB total — transcripts/logs) match no
  credential pattern. **Nothing an auto-snapshot would commit.**
- **`.gitignore` coverage for `.jj/`:** not needed — self-ignoring (§2).
- **Residual note:** `snapshot.auto-track` defaults to `all()` in 0.45.1, so any future
  unignored file dropped into the tree is auto-committed into the working-copy change —
  more aggressive than git. For a secrets lane, the existing ignore discipline
  (`.ufo/interactive-sessions/` already ignored) must stay current; alternatively set
  `snapshot.auto-track = "none()"` repo-scoped to require explicit `jj file track`.

## Commands index

All `jj` commands ran inside the scratch clone only; live repo touched read-only
(`git status`, `git ls-files`, `find`, `du`). Live repo after cleanup: `master` @
`aea7a43`, `git status` empty — untouched. Scratch clone deleted.
