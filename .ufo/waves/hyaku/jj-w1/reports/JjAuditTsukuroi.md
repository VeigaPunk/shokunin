# JjAuditTsukuroi — static git audit, lane `tsukuroi`

Status: complete. Read-only audit; no write in any live repo; no `jj` command run in
`/home/vgpnk/Projects/shokunin` or any path under it. All jj evidence comes from
`/fast/scratch/jj-wave/JjAuditTsukuroi/` (jj 0.45.1, git 2.56.0), now removed; every cited
output is inlined below.

## Scope and method

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`.

- Baseline (read-only): `HEAD` is attached to `refs/heads/master`;
  `HEAD = master = origin/master = 6923fe0bd3add04fc90f3bc3522895b27cf44bbe`; worktree clean,
  0 untracked; single worktree; full clone (`is-shallow-repository=false`, no promisor).
- Searched every `*.sh`, `*.py`, `*.mjs`, `*.js`, `Makefile` under `tools/`, `scripts/`,
  `verifiers/` and the repo root. Results: `tools/` contains 6 files
  (`tsukuroi-census.sh`, 5 Python gates); `scripts/`, `verifiers/`, `Makefile` do not exist;
  root has no executable files (only `.md`, `.gitignore`).
- Search: `grep -nE '\bgit\b' tools/*` → 31 textual hits in 5 files; 15 are executable sites
  (5 `subprocess.run(["git", …])` wrappers, 5 `show`, 5 `rev-parse`). All other hits are
  comments/error strings.
- `tools/tsukuroi-census.sh` (2679 lines, the round-2 gate named in SKILL.md) contains
  **zero** git tokens; it is a host-probe gate. Its `--selftest` is a `/tmp` fixture tree.
- Gates named in SKILL.md that carry git: `check-locator-clarification.py`,
  `check-root-dac-correction.py`, `check-section-citations.py`,
  `check-source-scope-correction.py`, `measure-update-recheck.py` (SKILL.md:1737, 1778, 1818,
  1819, 1857). The census gate (SKILL.md:240-259) has none.

## Counts per class

| Class | Executable sites | Breakdown |
|---|---|---|
| A — assumes attached HEAD / upstream | **0** | no `symbolic-ref`, `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`; HEAD never used as a branch name |
| B — mutates history/index/worktree | **0** | no add/commit/stash/checkout/reset/rebase/push/pull/merge/clean/tag |
| C — reads index/staging | **0** | no `diff --cached`, `ls-files -s`, `update-index` |
| D — read-only, commit-addressed | **15** | 5 exec wrappers + 5 `git show` + 5 `git rev-parse` |

Non-git file readers (not counted): 5 `read_tree` helpers in 4 tools read lane files directly
(the worktree path); `measure-update-recheck.py:453` requires a regular file.

## Classified call sites

`ROOT` / `repo` is `Path(__file__).resolve().parents[1]`, i.e. the lane root. Every wrapper
strips `GIT_*` from the environment, sets `GIT_OPTIONAL_LOCKS=0`, `GIT_PAGER=cat`, `LC_ALL=C`
and (except `check-root-dac-correction.py`) a 30 s timeout.

| File:line | Exact command | Class | Risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `tools/check-locator-clarification.py:443` | `git --no-pager -C <ROOT> <args>` | D | none: object reads only, no index/lock; detached HEAD irrelevant | none |
| `tools/check-locator-clarification.py:452` | `git show <commit>:<path>` | D | none: reads the committed blob at `commit`, never `@` | keep; always pass an explicit SHA |
| `tools/check-locator-clarification.py:465` | `git rev-parse --verify --quiet "<rev>^{commit}"` | D | **medium**: `rev` may be `HEAD`; under jj `HEAD` = `@-`, not the working copy and not necessarily the branch tip | require hex; resolve + `git merge-base --is-ancestor <sha> <branch>` before use; drop/deprecate `HEAD` |
| `tools/check-root-dac-correction.py:229` | `git --no-pager -C <repo> <args>` (no timeout) | D | none for reads; a wedged git blocks this gate indefinitely | add the 30 s timeout for parity |
| `tools/check-root-dac-correction.py:232` | `git show <commit>:<path>` | D | none | keep; explicit SHA |
| `tools/check-root-dac-correction.py:243` | `git rev-parse --verify --quiet "<rev>^{commit}"` | D | same `HEAD` semantic risk | same |
| `tools/check-section-citations.py:399` | `git --no-pager -C <ROOT> <args>` | D | none | none |
| `tools/check-section-citations.py:408` | `git show <commit>:<path>` | D | none | keep |
| `tools/check-section-citations.py:421` | `git rev-parse --verify --quiet "<rev>^{commit}"` | D | same `HEAD` semantic risk; also resolves `BASE` | same |
| `tools/check-section-citations.py:758` | `resolve(BASE)` → `git rev-parse --verify --quiet "db68e62065885b3f7463eb0a436c41f0dc3bcde5^{commit}"` | D | none today: verified `BASE` resolves and `merge-base --is-ancestor BASE HEAD` = true in the live repo; after a history rewrite it would still resolve as a dangling object (see R2) | add `--is-ancestor BASE <branch>` before the history comparison |
| `tools/check-source-scope-correction.py:355` | `git --no-pager -C <repo> <args>` | D | none | none |
| `tools/check-source-scope-correction.py:364` | `git show <commit>:<path>` | D | none | keep |
| `tools/check-source-scope-correction.py:377` | `git rev-parse --verify --quiet "<rev>^{commit}"` | D | same `HEAD` semantic risk | same |
| `tools/measure-update-recheck.py:426` | `git --no-pager -C <repo> <args>` | D | none | none |
| `tools/measure-update-recheck.py:437` | `git rev-parse --verify --quiet "<rev>^{commit}"` | D | same `HEAD` semantic risk | same |
| `tools/measure-update-recheck.py:444` | `git show <commit>:<path>` | D | none | keep |

Note: the table lists the 15 executable lines. `read_git`/`resolve` call sites all forward to
these; the only variable element is the revision string.

### HEAD admission points (the risk carrier, not a git call)

| File:line | Content |
|---|---|
| `tools/check-locator-clarification.py:30` | `REV = re.compile(r"^(?:HEAD|[0-9a-fA-F]{4,64})$")` |
| `tools/check-locator-clarification.py:475` | help: `HEAD or a 4-64 hex commit` |
| `tools/check-root-dac-correction.py:27` | `VALID_REV` same pattern |
| `tools/check-root-dac-correction.py:352` | help: `HEAD or a 4-64 hex commit` |
| `tools/check-section-citations.py:55` | `REV` same pattern |
| `tools/check-section-citations.py:433` | help: `required: HEAD or a 4-64 hex commit; reads immutable objects only` |
| `tools/check-source-scope-correction.py:26` | `REV` same pattern |
| `tools/check-source-scope-correction.py:506` | help: `HEAD or a 4-64 hex commit` |
| `tools/measure-update-recheck.py:38` | `REV` same pattern |
| `tools/measure-update-recheck.py:477` | help: `HEAD or a 4-64 hex commit; default worktree` |
| `SKILL.md:1818,1819,1857` | gate tables document `REV = HEAD or 4–64 hex` |

## Hooks and attributes actually in use

- Lane `.git/hooks`: 14 files, **all `*.sample`**, 0 active hooks.
- `core.hooksPath`: unset in system, global and lane-local config. Fleet root
  (`/home/vgpnk/Projects/shokunin`) is the same: no non-sample hook, `core.hooksPath` unset.
- `.gitattributes`: **absent** in the lane; `.git/info/attributes` absent;
  `core.attributesFile` unset; `core.autocrlf`, `core.eol`, `core.safecrlf` unset.
  `git check-attr -a -- tools/tsukuroi-census.sh corpus/… SKILL.md` prints nothing.
- Global config defines `filter.lfs.{clean,smudge,process}` with `filter.lfs.required=true`,
  but no attribute assigns `filter=lfs`, so LFS filtering is dormant.
- jj behavior (sandbox, verified): git hooks never run for jj commits or jj pushes (E3), and
  attribute clean filters / eol conversion are not applied (E4). Today this lane has nothing
  to bypass; the gap is latent.

## Top three risks for this lane

### R1 — `--revision HEAD` certifies `@-` (the previous commit), not the working copy; it can print PASS on content that violates the gate

Evidence, sandbox lane with a byte-identical copy of `check-locator-clarification.py` and the
real four corpus files, committed through jj (`jj commit`, bookmark moved, tracked push):

```
--- gate --revision HEAD on clean commit ---
{"correction_count": 2, "findings": [], "revision": "72fa3e90dbe8559f4ee8934e9d27f9e03700fcde", "status": "PASS"}
rc=0
worktree QUALITY heading present: False           # required heading deleted in the worktree
--- gate --revision HEAD after worktree mutation ---
{"correction_count": 2, "findings": [], "revision": "72fa3e90dbe8559f4ee8934e9d27f9e03700fcde", "status": "PASS"}
rc=0
--- gate worktree mode after mutation ---
{"correction_count": 0, "findings": [{"detail": "named headings absent", "id": "R15-MD-HEADING", …}, {"detail": "QUALITY check absent or empty", "id": "R15-MD-QUALITY", …}], "revision": "worktree", "status": "FAIL"}
rc=1
```

The two runs differ only in how the bytes are selected (`git show HEAD:path` vs `read_tree`):
`git show HEAD:md15` still contains the heading (`grep -c` = 1) while the worktree has 0.

HEAD/`@-` mechanics measured under jj 0.45.1:

```
-- after jj git init --colocate --   symbolic-ref: refs/heads/master ; HEAD = master = origin/master
-- after jj new --                   symbolic-ref: DETACHED ; HEAD=eb0d13ac… master=8256502…
-- after jj commit --                symbolic-ref: DETACHED ; HEAD=9335ac4… master=8256502…
-- after jj bookmark move master --to @- -- HEAD=master=9335ac4…
cat a.txt = edited ; git show HEAD:a.txt = one
```

After `jj edit <mutable commit>` the divergence is three-way — HEAD is the edited commit's
parent, the branch tip is a different commit, and the worktree is the edit:

```
jj edit: Working copy  (@) now at: qysuvnwq dad2afb9 c1
jj edit: Parent commit (@-)      : qxrlpwty f7ff280c (empty)
HEAD:   f7ff280ce02e…   master: 780c3704…   c1: dad2afb9…
cat f.txt -> two-edited ; git show HEAD:f.txt -> base ; git show c1:f.txt -> one
```

Danger window: everything between the first edit and `jj commit`, plus any `jj edit`
inspection. Severity high because SKILL.md documents `HEAD` as an accepted revision and the
gates are cited as proof of clean state.

### R2 — no gate binds a revision to the branch or to the remote; abandoned, unpushed and working-copy objects all verify

`git rev-parse --verify --quiet <hash>^{commit}` accepts any commit object in the odb; the tools
never call `merge-base --is-ancestor`, `rev-list`, `show-ref` or `ls-remote`
(`grep -nE 'merge-base|is-ancestor|rev-list|for-each-ref|show-ref|ls-remote' tools/*` → none).

Measured:

```
# rewritten local commit
old object still readable: YES          # git show OLD:a.txt -> one-modified
old is ancestor of master: NO
new is ancestor of master: YES

# working-copy commit @
working-copy commit id: c79748a1…      # git has it: `git cat-file -e` -> YES
@ is ancestor of master: NO (rc=1)     # `git rev-parse --verify --quiet @^{commit}` succeeds
```

And the E6b run above verified HEAD while the push had failed and origin lagged:

```
HEAD=72fa3e90…  master=72fa3e90…  origin/master=c2a86aaf…
jj git push --bookmark master --remote origin
Error: Non-tracking remote bookmark master@origin exists
… gate --revision HEAD → PASS rc=0 …
# after `jj bookmark track master@origin` the same push moves origin/master to 72fa3e9
```

So the two protocol invariants "landed = committed AND pushed before a report cites the hash"
and "a cited hash stays an ancestor of the branch" have no executable check here. The only
protection is jj config: default `immutable_heads() = builtin_immutable_heads()`
(`trunk() | tags() | untracked_remote_bookmarks() | untracked_remote_tags()`), so
`jj edit` of `master@origin` is rejected ("Commit bb60998… is immutable") — but that is a
configuration guard, not a verifier, and it does not cover local bookmarks (an unpushed
`jj describe -r @-` rewrote a commit a local bookmark pointed at, and the bookmark followed).

### R3 — jj bypasses git hooks and attribute filters/eol; the lane has none today, so any future one lands asymmetrically between the two commit paths

Sandbox evidence (`.git/hooks/pre-commit` and `pre-push` each write a marker and `exit 1`):

```
--- jj commit with failing pre-commit hook ---
pre-commit marker: ABSENT
--- git commit control (same hook) ---
pre-commit marker after git commit: ran
--- jj git push with failing pre-push hook ---
pre-push marker: ABSENT            # and the push to the sandbox origin succeeded
```

Attribute evidence (`.gitattributes`: `*.dat filter=upper`, `*.txt text eol=crlf`;
`filter.upper.clean = tr a-z A-Z`, `required=true`):

```
=== git control ===     blob f.dat:  H E L L O \n
=== jj colocated ===    blob f.dat:  h e l l o \n
git checkout -- f.txt -> l i n e \r \n
jj restore    f.txt   -> l i n e \n
```

Today this lane has zero active hooks and zero attributes, so no current commit is
misrepresented. The risk is governance: lanes commit through jj while the fleet root still
commits through `scripts/hyaku/fleet-commit.sh` (git), so any hook/attribute added later will
apply on one path and silently not the other, and repo-local `filter.lfs.*` is already defined
(though unassigned) in global config.

## Secondary observations

1. **Conflicted jj commits are invisible to git, so gates report CANNOT (loud, not silent).**
   A rebased conflict commit showed id `c97515dc…` in `jj log`; `git cat-file -e` = NO,
   `git rev-parse --verify --quiet c97515dc…^{commit}` = empty → `E-REVISION-INVALID`.
   A gate run mid-conflict cannot certify anything; the helper's refusal to push conflicted
   trees remains the barrier.
2. **`--revision master` is rejected by design.** The regex admits only `HEAD` or 4–64 hex;
   `--revision master` → `E-REVISION-INVALID` rc=2. The branch tip can only be named by hash,
   which makes it easy to reach for `HEAD` instead (see R1).
3. **Staging is destroyed by `jj commit`, not by `jj st`.** `git add a.txt` → `git diff --cached`
   shows `a.txt`; after `jj commit` the cached diff is empty. `jj st` alone left the staged
   entry intact. Irrelevant to this lane (class C = 0), but a future index-reading check would
   break under the jj commit path.
4. **The `@` commit is a real git object but a moving one.** It is readable
   (`git show <@>:path`), not an ancestor of the branch, and its commit id changes on the next
   snapshot. Never cite an `@` hash; cite `@-` via `jj log -r @- -T commit_id` or the helper's
   printed push hash.
5. **Missing-path semantics differ per tool.** `git show <commit>:path` for a path that exists
   on disk but not in the commit returns `fatal: path '…' exists on disk, but not in 'HEAD'`,
   which `read_git` maps to `None`. Locator, section-citations, source-scope and root-dac turn
   `None` into FAIL findings (`*-MISSING`), while `measure-update-recheck.py` turns both-None
   into `ABSENT` with exit 0. So an uncommitted new record is loud in four gates and a
   successful exit in the probe.
6. **`check-root-dac-correction.py:229` has no timeout**; the other four wrappers use 30 s.
7. **`git show` is `-C ROOT` against `.git`.** If a lane were ever initialized non-colocated
   (`jj git init` without `--colocate`), `.git` at the root disappears and all five tools fail
   with "not a git repository" instead of reading `.jj/repo/store/git`.

## jj-safe replacement set (recommendation only)

1. Resolve the revision, then require `git merge-base --is-ancestor <commit> <branch>` and
   `… origin/<branch>` before treating it as landed; emit a distinct finding id (e.g.
   `E-REVISION-NOT-LANDED`) instead of PASS/CANNOT ambiguity.
2. Drop `HEAD` from the accepted `REV` grammar, or make it explicit that it means `@-`
   (the parent of the working copy). Pre-commit checks should use worktree mode; post-commit
   checks should use the explicit SHA printed by the helper.
3. Keep `git show <sha>:<path>` unchanged — it is the jj-safe primitive (commit-addressed,
   no index contact, detached-HEAD independent).
4. If hooks or attributes are ever introduced in a jj lane, enforce them in the helper:
   jj runs no git hooks and applies no attribute filters/eol rules.
5. Any future staging-dependent check must read jj revsets (`jj diff -r @`), not `.git/index`.

## Residual risk and verification gaps

- I did not run jj in any live path (fleet root or lane) and did not execute the lane tools in
  the live repo; the end-to-end gate evidence uses a byte-identical copy plus corpus copies in
  `/fast/scratch`.
- Only the locator gate was exercised end-to-end under jj; the other four share the identical
  three-call git surface (`wrapper`/`rev-parse`/`show`), so the mechanism transfers, but their
  fixtures were not run.
- Not tested: jj gc/prune racing a `git show`, concurrent load, non-colocated init, partial
  clone (none configured), tag/ambiguous 4-hex prefixes (git errors loudly → CANNOT).
- SKILL.md's identity recheck at line 1592 uses `git show af8adf1:tools/tsukuroi-census.sh`
  (D, jj-safe), while lines 624/863 use worktree `md5sum` (reads `@`); under jj those two
  checks can disagree after an uncommitted edit. Documentation-level, not tooling.
- Report directory: this file is the only write outside the sandbox. Sandbox
  `/fast/scratch/jj-wave/JjAuditTsukuroi` was removed after the run.
