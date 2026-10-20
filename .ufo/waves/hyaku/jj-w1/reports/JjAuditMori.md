# JjAuditMori — git call audit of lane `mori` under planned jj colocation

Auditor: JjAuditMori-2 (read-only static audit + sandbox measurement).
Target: `/home/vgpnk/Projects/shokunin/mori-shokunin`, branch `master`.
Measured at audit time (live, read-only):

```
$ git -C . rev-parse --abbrev-ref HEAD   -> master
$ git -C . rev-parse HEAD                -> 24526ea9617cd020fee16c28fe4d4a2789dc28cb
$ git -C . rev-parse refs/heads/master   -> 24526ea9617cd020fee16c28fe4d4a2789dc28cb
$ git -C . status --porcelain=v1 -b      -> ## master...origin/master
$ ls -d .jj                              -> No such file or directory   (lane not colocated yet)
```

Sandbox for every jj command: `/fast/scratch/jj-wave/JjAuditMori/` (removed after this report; no
live repo was written, and no jj command ever ran with cwd or `-R` under `/home/vgpnk/Projects/shokunin`).
Versions: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git 2.56.0`.

## In-scope inventory

- `tools/` (8 files): `mori-census.sh`, `mori-silence-cases.sh`, `mori-round13-regressions.py`,
  `mori-round14-regressions.py`, `mori-round15-regressions.py`, `mori-round16-regressions.py`,
  `mori-round16-context-check.py`, `mori-journal-window.py`.
- `scripts/` and `verifiers/`: **absent** (`ls` rc 2). No root-level `*.sh|*.py|*.mjs|*.js|Makefile`
  (`find . -maxdepth 1 ... | wc -l` = 0). `considerthese/*.md` is prose.
- SKILL.md registers 9 gate/probe rows (lines 164–172), all backed by the files above:
  census + drift pin (`mori-census.sh`), silence oracle (`mori-silence-cases.sh`),
  r13/r14/r15/r16 regressions, r16 context check, journal window.
- `mori-journal-window.py` and `mori-round16-context-check.py` contain **zero** git calls
  (exhaustive `\bgit\b` scan: 0 lines each). Their subprocesses run journalctl and themselves only.

## Findings (observed)

### F1 — No class-A call site exists in this lane

```
$ grep -nE 'symbolic-ref|@\{u(pstream)?\}|--abbrev-ref|branch --show-current|for-each-ref' tools/*
(no matches)
```

No tool assumes an attached HEAD or an upstream. This is the main reason the cutover is cheap here.

### F2 — `jj commit` detaches HEAD and rewrites the git index; `jj st` does not

Sandbox, after `jj git init --colocate` and one commit:

```
$ git symbolic-ref -q HEAD ; echo rc=$?
rc=1
$ git rev-parse HEAD
611dfb56904b92b5a1bc5897b728d26a55c6ea73
$ git rev-parse '@{u}'
fatal: HEAD does not point to a branch          # rc 128
$ git rev-parse --abbrev-ref HEAD
HEAD                                            # not used by this lane
$ git branch --show-current                     # prints nothing, rc 0
```

`jj st` (snapshot only) left HEAD attached and left a `git add`-staged entry intact; the detach and
the index reset happen on `jj commit`. The claims hold for the mutation that matters here.

### F3 — HEAD is not the branch after `jj commit` (D-class hazard)

Same sandbox, second commit made without moving the bookmark (the helper's `bookmark set` step is a
separate command after `commit`):

```
$ git rev-parse HEAD        -> d19d559da39f8de044f8926e65cb2256c6a3535c
$ git rev-parse master      -> 611dfb56904b92b5a1bc5897b728d26a55c6ea73
$ git log -1 --format='%h %an' refs/heads/master -> 611dfb5 Joao Pedro Veiga
$ git log -1 --format='%h %an' HEAD              -> d19d559 mori-shokunin
```

In git mode `git commit` moves `refs/heads/<branch>` and HEAD atomically. Under jj, HEAD follows the
working-copy parent immediately, while the bookmark is moved by a later, separate `jj bookmark set`
(and the remote by a still-later `jj git push`). `git log`/`rev-parse HEAD` therefore observe commits
that are not on the branch and not pushed whenever that later step fails or is skipped.

### F4 — `jj commit` keeps `@`'s author; only `metaedit --update-author` stamps the lane identity

First commit made after `jj config set --repo user.name mori-shokunin`:

```
$ git log -1 --format='%h|%an <%ae>|%cn <%ce>|%s'
611dfb5|Joao Pedro Veiga <jpveigao10@gmail.com>|mori-shokunin <mori@shokunin.local>|subject work
```

The **committer** was the lane; the **author** was the ambient identity (the operator's global jj
config). Helper-shaped sequence (`jj metaedit --update-author` with per-command `--config user.name/
user.email`, then `jj commit -m ... -- <path>`):

```
$ git log -1 --format='%h|%an <%ae>|%cn <%ce>|%s'
d19d559|mori-shokunin <mori@shokunin.local>|mori-shokunin <mori@shokunin.local>|second work
```

`scripts/hyaku/jj-lane.sh` (cmd_commit, ~line 219) does run metaedit before commit, so helper commits
satisfy the lane-identity invariant. Any commit path that bypasses the helper does not.

### F5 — Index reset destroys staged state, but not dirt detection

A path staged with `git add` before a jj mutation became an intent-to-add index entry after
`jj commit` (empty blob in the index, real bytes in the worktree):

```
$ git ls-files -s staged.md
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	staged.md
$ git diff --cached --name-status      -> (empty)
$ git status --porcelain               ->  A staged.md
$ git ls-files -mo --exclude-standard  -> staged.md
```

So `diff --cached`/`ls-files -s`-style staging reads become meaningless under jj; `status --porcelain`
and `ls-files -m/-o` still report the path. This lane uses the latter two only.

### F6 — `.jj/` cannot pollute row B: jj ignores itself

`jj git init --colocate` writes `.jj/.gitignore` containing `/*`:

```
$ od -c .jj/.gitignore
0000000   /   *  \n
$ git status --porcelain --ignored=matching | grep '^!! .jj/'
!! .jj/.gitignore
!! .jj/repo/
!! .jj/working_copy/
$ git ls-files --others --exclude-standard | wc -l
0
```

No census/selftest path sees jj metadata as untracked churn.

### F7 — `ls-files -mo` still detects edits to *tracked* files under jj

After appending to a tracked file and running a jj snapshot:

```
$ git ls-files -mo --exclude-standard   -> LOG.md
$ git status --porcelain=v1 --untracked-files=all ->  M LOG.md
$ git ls-files -s LOG.md                 -> 100644 df967b96... 0  LOG.md
$ git rev-parse HEAD:LOG.md              -> df967b96...
$ git hash-object LOG.md                 -> d1cb4a6c...
```

The git index is HEAD-based, the worktree holds `@`; both modified tracked files and untracked files
are reported. This is the exact input of census row B (mori-census.sh:2180) and it survives colocation.

### F8 — r15's pinned blob is safe (pin is an ancestor of `master`)

```
$ git cat-file -e 0fa5e0de194bcc270a927a166664113e6821442b^{commit} && echo present=yes
present=yes
$ git merge-base --is-ancestor 0fa5e0de194bcc270a927a166664113e6821442b HEAD; echo rc=$?
rc=0
```

`git show <pin>:tools/mori-census.sh` reads a reachable git object; jj does not prune the git object
database for commits on the branch. No change needed beyond the existing on-disk frozen fallback.

### F9 — Hooks and attributes: none, so jj's bypass is currently a non-issue

```
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample' | wc -l        -> 0
$ git config --get core.hooksPath; echo rc=$?                           -> rc=1 (unset, merged config)
$ ls .gitattributes                                                     -> No such file
$ git ls-files | grep -i attributes; echo rc=$?                         -> rc=1
$ git config --get core.attributesfile; echo rc=$?                      -> rc=1
$ git config --get core.autocrlf; echo rc=$?                            -> rc=1
$ git config --get core.eol; echo rc=$?                                 -> rc=1
$ git config --local --get-regexp '^(filter|merge|diff)\..*'; echo rc=$? -> rc=1
$ cat .git/info/attributes                                              -> No such file
$ cat .git/info/exclude                                                 -> default comments only
```

No commit-msg/pre-commit/pre-push hook, no clean/smudge/process filter, no eol normalization, no
`.gitattributes` in the tree. `.gitignore` contains only `.ufo/interactive-sessions/`.
jj bypasses git hooks by design and does not apply git filters; with none configured there is no
behavior to lose today. If any is added later, it will silently not run on jj commits.

### F10 — Hardening gaps in two gates (not jj-caused, but jj-relevant)

- `mori-round16-regressions.py:701-703` runs `["git","-C",str(REPO)] + args` with
  `env = dict(os.environ)`: no `--no-optional-locks`, no `-c core.fsmonitor=false`, and no
  `GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE` scrub. Its `status --porcelain` can refresh/write the git
  index while jj is exporting the same index.
- `mori-round15-regressions.py:782-784` inherits `os.environ` (sets only `GIT_OPTIONAL_LOCKS=0`), so an
  inherited `GIT_DIR` can override `-C`.
- Census (2129/2180/2197/2207) explicitly unsets `GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE`,
  sets `GIT_OPTIONAL_LOCKS=0`, and disables fsmonitor on the `ls-files` call. r13/r14 replace the
  environment wholesale (`PATH`, `HOME`, `GIT_CONFIG_GLOBAL/SYSTEM`, `GIT_OPTIONAL_LOCKS`).

### F11 — Dead code and synthetic git

- `mori-silence-cases.sh:436-443` defines `git_q()`; it is never called (only definition matched).
- Census' own selftest installs a **stub** `git` dispatcher (`mori-census.sh:2846-2866`, per-verb files
  `stub/git-<verb>`); r13/r14 write synthetic `git` scripts into fixtures (`r13:1110`, `r14:857`).
  Selftests therefore never exercise the real invocations below; `--selftest` returns before the
  revision probes (`r13:3250`, `r14:~2610`, `r15:2325`, `r16:1751`).

### F12 — Output guards omit `.jj`

`r15:1418` and `r16:747` protect `REPO/tools`, `REPO/.git`, `REPO/corpus` from `--output`, but not
`REPO/.jj`. r13/r14 have no such protected-tree guard at all. An output path under `.jj` would mutate
jj metadata and be invisible to `git status` (F6). Low severity, trivial to close.

## Classified call sites

Class key: **A** attached-HEAD/upstream assumption · **B** history/index/worktree mutation ·
**C** index/staging-state read · **D** read-only, HEAD-commit based.

| # | file:line | command (exact argv) | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|---|
| 1 | tools/mori-census.sh:2100 | `env GIT_OPTIONAL_LOCKS=0 "$GIT_BIN" -C "$ROOT" cat-file -e "HEAD:$rpath"` | D | none for detached HEAD; `HEAD` may be a working-copy parent that is not on `refs/heads/*` (F3), so report-closure can be credited to a non-branch commit | none required; if branch identity matters: `cat-file -e "refs/heads/$branch:$rpath"` |
| 2 | tools/mori-census.sh:2102 | `env GIT_OPTIONAL_LOCKS=0 "$GIT_BIN" -C "$ROOT" log -1 --format=%ct -- "$rpath"` | D | same HEAD-vs-branch caveat; `%ct` is committer time, which jj rewrites on rebase (still within window) | `git log -1 --format=%ct "refs/heads/$branch" -- "$rpath"` |
| 3 | tools/mori-census.sh:2129 | `env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE GIT_OPTIONAL_LOCKS=0 "$GIT_BIN" -C "$repo" rev-parse --git-dir` | D | none; measured `.git` in a colocated repo | none (already jj-safe) |
| 4 | tools/mori-census.sh:2180 | `... -c core.fsmonitor=false -c core.quotePath=false -C "$repo" ls-files -mo --exclude-standard` | C | low: measured index is HEAD-based, tracked edits + untracked files still listed (F7); `.jj` self-ignored (F6); staged entries become intent-to-add but remain visible (F5) | keep; equivalent HEAD-relative form: `status --porcelain=v1 -z --untracked-files=all` |
| 5 | tools/mori-census.sh:2197 | `... -C "$repo" rev-parse --verify -q HEAD` | D | none for detached HEAD; presence check only | keep, or verify the branch ref and record `head_branch_mismatch` |
| 6 | tools/mori-census.sh:2207 | `... -C "$repo" log --since=@"$LA_EPOCH" --format='%ct %an <%ae>'` (default rev = HEAD; root lanes add pathspec excludes) | D | HEAD-vs-branch drift can count a non-landed commit as progress (F3); `%an` depends on the commit path stamping lane identity (F4) | `git log "refs/heads/$branch" "${lg_args[@]}"` |
| 7 | tools/mori-silence-cases.sh:449 | `git -c init.defaultBranch=main init -q "$1"` | B | none live: fixture repo under `mktemp -d /tmp/mori-silence-cases.XXXXXX`, never the fleet tree; but the fixture models only git, so jj export semantics are untested | keep for git-mode cases; add a colocated fixture arm |
| 8 | tools/mori-silence-cases.sh:480-481 | `git -c ... -C "$repo" add -- "$rel"` | B | none live (fixture); under jj an `add`-based fixture would model state jj destroys (F5) | keep for git-mode; jj arm: `jj file track --include-ignored -- "$rel"` |
| 9 | tools/mori-silence-cases.sh:488-489 | `git -c ... -C "$repo" commit -q -m "$msg"` | B | none live (fixture); jj commit detaches HEAD and keeps `@`'s author unless metaedit (F4) | keep for git-mode; jj arm: `jj --config user.name=... metaedit --update-author` then `jj commit -m ... -- <paths>` |
| 10 | tools/mori-round13-regressions.py:1245 (launcher 1229) | `git --no-optional-locks -C REPO -c core.fsmonitor=false rev-parse HEAD` | D | normal-run only (selftest returns earlier); detached HEAD works; HEAD≠branch caveat (F3) | keep; branch-anchored rev if comparing against the branch |
| 11 | tools/mori-round13-regressions.py:1251 (launcher 1229) | `git ... status --porcelain --untracked-files=all` | C | low: dirty boolean preserved under jj (F5/F7); XY codes change for staged paths; `.jj` ignored | keep; add `-z` for path safety |
| 12 | tools/mori-round14-regressions.py:432 (launcher 405) | `git -C REPO -c core.fsmonitor=false rev-parse HEAD` | D | as row 10 | as row 10 |
| 13 | tools/mori-round14-regressions.py:438 (launcher 405; `PORCELAIN_ARGS` 393-397) | `git -C REPO -c core.fsmonitor=false --no-optional-locks status --porcelain --untracked-files=all` | C | low: as row 11 | keep |
| 14 | tools/mori-round15-regressions.py:749 (launcher 787) | `git -c core.fsmonitor=false -C REPO --no-optional-locks show 0fa5e0d:tools/mori-census.sh` | D | none: pinned commit is an ancestor of `master` (F8), object reachable; existing on-disk frozen fallback | none (already jj-safe) |
| 15 | tools/mori-round15-regressions.py:806 (launcher 787) | `git ... rev-parse HEAD` | D | as row 10 | as row 10 |
| 16 | tools/mori-round15-regressions.py:807 (launcher 787) | `git ... status --porcelain=v1 -z --untracked-files=all` | C | low: as row 11 | keep |
| 17 | tools/mori-round16-regressions.py:712 (launcher 701-703) | `git -C REPO rev-parse HEAD` (inherits `os.environ`, no `--no-optional-locks`, no `core.fsmonitor=false`) | D | as row 10, plus no env/flag hardening (F10) | add `--no-optional-locks -c core.fsmonitor=false`, scrub `GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE` |
| 18 | tools/mori-round16-regressions.py:713 (launcher 701-703) | `git -C REPO status --porcelain` (default untracked mode) | C | low: as row 11; may take the git index lock while jj exports (F10); misses nothing at dir level (normal mode) | add `-z --untracked-files=all`, `--no-optional-locks`, `-c core.fsmonitor=false`, env scrub |

Not counted as git invocations: `command -v git` (silence:181, capability probe), the census stub
dispatcher (`mori-census.sh:2846/2859/2866`), the r13/r14 synthetic `git` fixtures
(`r13:1110`, `r14:857`), the unused `git_q` wrapper (silence:441 — dead, no callers), and the
documentation string at `mori-census.sh:2276`.

## Counts per class

| class | count | where |
|---|---|---|
| A (attached HEAD / upstream assumption) | **0** | — |
| B (history/index/worktree mutation) | **3** | silence-cases init/add/commit, all inside `mktemp` fixtures; 0 against a live repo |
| C (index/staging-state read) | **5** | census `ls-files -mo`; r13/r14/r15/r16 `status --porcelain*` |
| D (read-only, HEAD-based) | **10** | census cat-file/log x2/rev-parse x2; r13 rev-parse; r14 rev-parse; r15 show + rev-parse; r16 rev-parse |
| **total real invocation sites** | **18** | — |

Plus one unreachable dead wrapper (`silence:441`), which is excluded from the live count.

## Top three risks for this lane

1. **HEAD is not the branch under jj (D probes).** The census grades progress from `git log`/`HEAD`
   (`mori-census.sh:2207`, plus `2197`), and all four regression gates pin start/end revisions with
   `rev-parse HEAD` (`r13:1245`, `r14:432`, `r15:806`, `r16:712`). After `jj commit`, HEAD is `@-`
   while `refs/heads/<branch>` lags until `jj bookmark set`; measured divergence
   `HEAD=d19d559` vs `master=611dfb5`. A failed/aborted bookmark step, or a lane commit made by hand
   without moving the bookmark, makes the census credit a commit that is neither on the branch nor
   pushed — violating the "landed = committed AND pushed" spirit for any signal derived from these
   probes. Mitigation: resolve the branch (origin/HEAD → master → main, as `jj-lane.sh` does) and
   query `refs/heads/$branch` instead of `HEAD`; optionally emit `HEAD_BRANCH_MISMATCH` when
   `git merge-base --is-ancestor HEAD refs/heads/$branch` fails.

2. **Lane authorship is only correct because the helper calls `metaedit --update-author`.**
   `jj commit` preserves `@`'s author (measured: ambient `Joao Pedro Veiga <jpveigao10@gmail.com>`
   even with `--config user.name=mori-shokunin`); the committer alone gets the lane identity. The
   census's progressing verdict requires the exact author `<lane>-shokunin <lane>@shokunin.local`
   (`mori-census.sh:2231`). Any path that creates lane history outside `jj-lane.sh commit`
   (manual `jj commit`, `jj new` + describe, another automation) yields ambient-authored commits and
   silently degrades `progressing` to `progressing-weak` (`row-C`) — the census then under-reports
   work rather than naming an identity violation. Mitigation: keep the helper as the only commit
   path, and add a distinct census finding (e.g. `LANE_AUTHOR_MISMATCH`) when a post-launch commit's
   committer is the lane but its author is not, instead of folding it into `other_authored_commits`.

3. **Zero jj-colocated coverage in every gate and selftest, plus two unhardened git readers.**
   The silence oracle builds real *git* fixtures (`silence:13,433-490`); r13/r14 swap in synthetic
   `git` stubs; r15/r16 fixtures are journal packs. Nothing in this lane exercises a colocated repo,
   so risks 1 and 2 cannot be caught by any selftest, and the census's own `--selftest` answers from
   `stub/git-<verb>` rather than a real repo. At the same time `r16:701-703` and `r15:782-784` run
   git without the census's hardening (`--no-optional-locks`, `core.fsmonitor=false`, `GIT_*` scrub),
   so their `status` reads can race jj's index export. Mitigation: add one colocated fixture arm
   (git init → `jj git init --colocate` → `file track` + `metaedit --update-author` + `jj commit` →
   assert the same verdict/exit), and reuse the census argv hardening in both gates.

## Recommendations (ordered, all in `tools/`)

1. Add a small branch resolver to `mori-census.sh` (4 lines, mirroring `detect_branch`: symbolic-ref →
   `refs/remotes/origin/HEAD` → `refs/heads/master` → `refs/heads/main`) and use `refs/heads/$branch`
   in the `cat-file`/`log`/`rev-parse` probes; keep `HEAD` only where the commit itself is the subject.
   Do not introduce a shared library for this — census is deliberately standalone.
2. In `mori-census.sh`, after `has_head=1`, compute `git merge-base --is-ancestor HEAD
   "refs/heads/$branch"`; on failure emit an explicit info/drift row rather than silently grading from
   HEAD. Same check is cheap enough for the gates.
3. Keep `ls-files -mo` (it is measured safe); do not add `diff --cached`/`ls-files -s` reads, which jj
   invalidates. If a HEAD-relative form is preferred, switch to `status --porcelain=v1 -z
   --untracked-files=all` and parse NUL records.
4. Add `.jj` to the protected-output lists in `r15:1418` and `r16:747`; consider the same guard for
   `r13`/`r14`, which currently lack one entirely.
5. Harden `r16._git` to the census/r13 shape: `--no-optional-locks`, `-c core.fsmonitor=false`,
   explicit env without `GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE`; do the env scrub in `r15._git` too.
6. Add a jj-colocated case to `mori-silence-cases.sh` and to the r13/r14 selftests: a real colocated
   fixture whose commit is made by `jj file track` → `jj metaedit --update-author` → `jj commit`, then
   assert (a) row A matches the lane author, (b) row B still sees a dirty tracked file, (c) a stale
   bookmark (HEAD ahead of `refs/heads/master`) is reported rather than graded progressing.
7. Delete the unused `git_q()` (`silence:436-443`) or use it; today it is dead weight and reads as if
   all fixture git calls were centralized when only init/add/commit are.

## Invariants check for the planned cutover

- **pathspec-limited commits**: unchanged; the helper passes `-- <paths>` to `jj commit` and refuses
  `..`, absolute and glob paths (`jj-lane.sh` cmd_commit). No mori tool commits.
- **lane identity**: only guaranteed on the helper path (F4/risk 2).
- **pushed-before-cited hash**: helper prints `pushed <hash>` only after `jj git push` succeeds and
  rebases only `<branch>@origin..<branch>` on rejection; no force. Not exercised by mori tooling.
- **LOG.md append-only**: no in-scope tool writes LOG.md; no enforcement is added by jj either way.
- **`.ufo/state/` never committed**: helper rejects `.ufo/state/*` and `.ufo/watchdog.log` commit
  paths; mori tooling never commits. [INFERENCE] state lives at the fleet root, not in the lane repo.
- **hooked/attribute behavior**: none configured, so jj's bypass changes nothing today (F9).

## [INFERENCE]

- The r13/r14/r15/r16 revision probes are normal-run only; `--selftest` returns before the harness is
  constructed (`r13:3250` vs `3259`; `r14:2757` vs `2766`; `r15:2325`; `r16:1751` vs the run body).
  Therefore selftests do not validate the probes against a real repo. (Verified by call ordering, not
  by executing them.)
- Whether the fleet runs these gates from the lane checkout or a separate copy is unknown. `REPO` is
  `__file__.parent.parent`, so whenever the tools are run in place the status/HEAD probes observe the
  lane repo — the assumption behind risks 1 and 3.
- A transient read of `.git/index`/`HEAD` during jj's export is possible because git readers take no
  lock against jj; I did not stress concurrent mutation, so the probability is unmeasured. Census
  treats a nonzero rc as `unavailable` (row 1), which is non-alarming and could mask a silent lane.
- jj rebasing an unpushed commit changes its hash and committer time; the census window is
  committer-time based, so a rebased commit stays inside the window. Not measured live (no rejects
  were produced in the sandbox).

## Verification gaps (not run, therefore not passed)

- Did not run `mori-census.sh` or any gate: forbidden against live paths, and a faithful run needs the
  fleet root's roster/ledger/journal.
- Did not stress concurrent `jj` mutation vs `git status`/`ls-files` readers.
- Did not exercise the helper's push-rejection → fetch → rebase → retry path (relied on its source and
  the sandbox's successful push after `bookmark track`).
- Did not test an unborn-HEAD colocated repo (no commits); live lanes always have commits.
- The live lane has no `.jj`, so all colocated measurements are sandbox replicas, not live observations.
