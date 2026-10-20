# JjAuditKasegi — lane `kasegi` git-invocation audit (read-only)

Lane repo: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` · branch `master` · HEAD `922a4dd`
Audit date: 2026-10-20. jj probed: `0.45.1-7c41cdeb`. No installs, no upgrades.
Sandbox: `/fast/scratch/jj-wave/JjAuditKasegi-2/` (kept — it preserves every failure cited below).

## 0. Scope reality check (measured, not assumed)

The assignment's listed surfaces **do not exist** in this lane:

| expected surface | present? | evidence |
|---|---|---|
| `tools/` | no | `ls -d tools` → no such file |
| `scripts/` | no | `ls -d scripts` → no such file |
| `verifiers/` | no | `ls -d verifiers` → no such file |
| root `*.sh`/`*.py`/`*.mjs`/`*.js`/`Makefile` | none | `ls -1 *.sh *.py *.mjs *.js Makefile` → no matches |
| JS tooling anywhere | none | `find . -name '*.mjs' -o -name '*.js'` (excl. `.git`) → empty |
| git calls in scripts | history-confirmed never existed | `git log --all --pretty=format: --name-only --diff-filter=A \| grep -E '\.(sh\|py\|mjs\|js)$\|Makefile'` → only the 4 `corpus/instruments/*.py` |

The lane's entire executable surface is `corpus/instruments/{anchorcheck,resolve,density,test_resolve}.py` (all `#!/usr/bin/env python3`, mode 755), the shell receipts embedded in `SCORECARD.md`, one runnable `recheck:` gate, and one round-plan instruction. `SKILL.md` names only `resolve.py` (`grep -c anchorcheck SKILL.md` = 0; `resolve` = 15); `SCORECARD.md` names anchorcheck/density/resolve; `corpus/instruments/README.md` names all four including the `test_resolve.py` selftest.

Exhaustive spawn search:

```
grep -rInE "(subprocess|execFile|execSync|spawnSync|spawn|Popen|system\(|check_output)" \
  --include='*.py' --include='*.sh' --include='*.mjs' --include='*.js' . --exclude-dir=.git --exclude-dir=.ufo
./corpus/instruments/anchorcheck.py:65:import re, sys, os, subprocess
./corpus/instruments/anchorcheck.py:120:    p = subprocess.run(['git', '-C', repo, 'show', f'{obj}:{path}'],
./corpus/instruments/test_resolve.py:130:        proc = subprocess.run([sys.executable, ...])   # python, not git
```

**There is exactly one git invocation in lane code**: `corpus/instruments/anchorcheck.py:120`.

## 1. Classified table

Classes: **A** attached-HEAD/upstream assumption · **B** history/index/worktree mutation · **C** index/staging read · **D** read-only, HEAD-commit-based.

| # | file:line | exact command | kind | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|---|---|
| 1 | `corpus/instruments/anchorcheck.py:120` (def `:118`, called `:157`) | `git -C <lane_root> show <obj>:<path>` where `<obj>` is a `<!-- pin: path hash -->` hash (7–40 hex) | code | **D** | Object-by-id read; works with detached HEAD (measured rc=0). Real risks are gate semantics, not mechanics: (i) no branch/push check, so a pin on an off-bookmark or rewritten commit still verifies; (ii) phantom trailing line; (iii) uncaught crash on non-UTF-8 blob or missing `git`. Dormant today: `grep -rn '<!-- *pin:'` → 0 pins. | Keep `git show <obj>:<path>`; prepend `git merge-base --is-ancestor <obj> <branch>` and compare `git rev-parse <branch>`/`origin/<branch>` before trusting a pin; use `splitlines()`, `errors='replace'`, and catch `FileNotFoundError`. |
| 2 | `SCORECARD.md:332` | `git archive 94aace2` (before-tree source) | receipt | **D** | Safe. `94aace2` is an ancestor of `master` (measured `merge-base --is-ancestor` → yes), so permanently reachable. Reproduced identically after a jj mutation. | Unchanged. If a new freeze is taken in a jj lane, archive **the branch** (`git archive master`), not `HEAD` (see finding F4). |
| 3 | `SCORECARD.md:336` | `git ls-tree --name-only 94aace2 corpus/knowledge/` | receipt | **D** | Safe (explicit commit). | Unchanged. |
| 4 | `SCORECARD.md:337` | `git ls-tree --name-only 94aace2 corpus/knowledge/` (loop feeding `bash -c "$r"`) | receipt | **D** | Safe. Note it *executes* each `recheck:` line, including #9. | Unchanged. |
| 5 | `SCORECARD.md:339` | `git ls-tree --name-only 94aace2 corpus/knowledge/` | receipt | **D** | Safe. | Unchanged. |
| 6 | `SCORECARD.md:339` | `git show 94aace2:$f` | receipt | **D** | Safe (explicit commit). | Unchanged. |
| 7 | `SCORECARD.md:340` | `git ls-tree --name-only 94aace2 corpus/knowledge/` | receipt | **D** | Safe. | Unchanged. |
| 8 | `SCORECARD.md:341` | `git ls-tree --name-only 94aace2 corpus/knowledge/` | receipt | **D** | Safe. | Unchanged. |
| 9 | `corpus/knowledge/repo-git-state.md:75` | `test -d ~/Projects/bounties/.git && git -C ~/Projects/bounties rev-parse HEAD` | gate (`recheck:` line, run by #4) | **D** | Safe and inert: target base is absent, the `test -d` short-circuits, gate fails closed. jj never touches this path. | Unchanged. |
| 10 | `plans/wwkd-round-21-authority-audit.md:33` | `git -c user.name=kasegi-shokunin -c user.email=kasegi@shokunin.local` — options-only fragment; the prose verb is "Commit actual owned paths only" | plan instruction | **B** (+ implicit **A**) | **Unsafe.** In a colocated lane `git commit` runs on jj's detached HEAD: measured commit `1ce4440` was created while `master` stayed at `906bbe6`, and jj then imported it ("Reset the working copy parent to the new Git HEAD"). The commit is outside the bookmark and outside the helper's accounting. | Delete/replace with `scripts/hyaku/jj-lane.sh commit <lane-dir> --as kasegi -m <msg> -- <paths>`. Never `git add`/`git commit` in a lane. |
| 11 | `SKILL.md:279` | `git ls-files` (census: "1.5 G, `git ls-files` → 0, mostly *not ignored*") | prose measurement | **C** | **Meaning drift.** Under jj the index is written from `@`; measured: `runtime.log` appeared in `git ls-files` while `git cat-file -e HEAD:runtime.log` → no, and `git status --short` showed ` A runtime.log`. A census of "tracked" becomes a census of "snapshotted". Target tree is the lost `~/Projects/bounties`, so not runnable today. | For committed contents: `git ls-tree -r --name-only <branch> -- <path>`. For working-copy contents: `jj --ignore-working-copy file list`. |

Additional prose-only references (commands described, not part of a runnable gate — listed for completeness, not counted): `SKILL.md:413` (`rev-parse --verify` inside the lost `ops/finalize-all.mjs`); `corpus/knowledge/repo-git-state.md:3,11-16,42,60,69,73` (`git status/branch/rev-list/merge-base/ls-files/reflog/stash list/log origin/main` against the lost tree); `corpus/knowledge/ops-invariants.md:122` (`git -C claims log --oneline -8`); `LOG.md:1066` (`git grep -niE … 94aace2`); `LOG.md:414`, `corpus/knowledge/source-tree-loss-2026-09-28.md:139`, `corpus/knowledge/triage-thresholds.md:10` (prose).

## 2. Counts per class

| scope | A | B | C | D | total |
|---|---:|---:|---:|---:|---:|
| all identified command occurrences (table rows 1–11) | 0 | 1 | 1 | 9 | 11 |
| runnable surface only (code + shell receipts + runnable `recheck:` gate) | 0 | 0 | 0 | 9 | 9 |
| lane scripts (`*.py`/`*.sh`/`*.mjs`/`*.js`/`Makefile`) | 0 | 0 | 0 | 1 | 1 |

Zero A-class call sites exist: nothing in the lane reads `symbolic-ref`, `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`, or uses HEAD as a branch name. The only A-shaped hazard is the class-B plan line, whose `git commit` *behaves* like an A-class assumption under jj.

## 3. Hooks and attributes (what jj bypasses)

| item | state in this lane |
|---|---|
| `.git/hooks/*` non-sample | **none** — 14 entries, all `*.sample` (`ls .git/hooks \| grep -v '\.sample$'` → empty) |
| `core.hooksPath` | **unset** (repo and global) |
| `.gitattributes` | **absent** at root (and nowhere tracked: `find . -name .gitattributes` → empty) |
| `.git/info/attributes` | absent |
| `core.attributesFile` | unset |
| `core.autocrlf` / `core.eol` | unset (both `git config --get` exit 1) |
| global filters | `filter.lfs.{clean,smudge,process,required}` configured globally, but **no attribute selects it**, so inert |

Measured jj bypasses (sandbox):

- **Hooks.** Installed `.git/hooks/pre-commit` that appends to a log and `exit 1`; `jj commit` succeeded and the marker file was never created: `hooklog` → `(hook did not run)`. jj does not run git hooks at all.
- **eol rules.** With `.gitattributes: *.txt text eol=lf`, jj committed a CRLF worktree file **raw**: `git cat-file -p HEAD:crlf.txt` → `c r l f \r \n s e c o n d \r \n`. No normalization, no warning.
- **clean filters.** With `*.log filter=upper` (`tr 'a-z' 'A-Z'`), jj committed `lower\n` **unfiltered**; `git add` would have stored `LOWER\n`.
- **read path.** `git show <rev>:<path>` prints the stored blob, not a smudged/textconv version (measured: uppercase blob printed uppercase; `eol=crlf` blob printed LF).

Net: nothing is bypassed *today* because the lane has no hooks and no attributes. jj also bypasses the lane's would-be normalization barrier the moment any filter/eol rule is added, and `anchorcheck` reads the raw blob, so the gate would keep grading jj's unnormalized bytes.

## 4. Findings (observed facts first)

**F1 — `anchorcheck` accepts a pin that is not on the branch.** In `kasegi-clone` (jj-colocated, remote removed), a `jj commit` produced pin commit `c1de781` while `master` stayed at `922a4dd`:

```
$ python3 corpus/instruments/anchorcheck.py probe.md
== probe.md: 3 in-range cite instances, 0 bad; 3 distinct anchors; LOST-RECORDED=0 PIN-BROKEN=0 ORIGIN=0 OUTSIDE-BASE=0 BASE-ABSENT=0
OK md:2 SKILL.md:1    [---]
OK md:3 SKILL.md:1023 [| A report cites the 2025 CWE Top 25 | ...]
OK md:4 SKILL.md:1024 []
$ echo -n "pin ancestor of master? " && (git merge-base --is-ancestor c1de781d7f812ccc9d0a120ed592314e67e883f7 master && echo YES || echo NO)
pin ancestor of master? NO
$ git rev-parse --short master; git rev-parse --short c1de781
922a4dd
c1de781
```

So `bad=0` certifies bytes that never landed on `master`. Nothing in the lane checks ancestry; the protocol invariant "a cited hash stays an ancestor of the branch" is unenforced.

**F2 — pin durability is *stronger* than expected, which hides F1.** After `jj describe` rewrite, `jj op abandon '..@-'`, `jj util gc --expire=now`, and `git gc --prune=now`, the old pin still resolved and the gate still reported `0 bad`. jj's `refs/jj/keep/*` refs protect rewritten commits:

```
$ git for-each-ref --format='%(refname)' refs/jj/keep | wc -l
10
$ git cat-file -t c1de781d7f812ccc9d0a120ed592314e67e883f7
commit
```

So "PIN-BROKEN" is not the failure mode to fear; silent success on a stale/off-branch pin is.

**F3 — phantom trailing line in the pin path.** `git_show` does `p.stdout.split('\n')`; a blob ending in `\n` yields one extra empty element:

```
$ wc -l < SKILL.md
1023
# pin on SKILL.md, cite SKILL.md:1024
OK md:4 SKILL.md:1024  []
```

The non-pin path (`sum(1 for _ in open(path))`) correctly reports `PAST-EOF md:3 notes.md:3 (file has 2 lines)` for the same shape. Only the git branch is off by one — a false OK with empty captured text.

**F4 — round receipts grade `HEAD`, which is detached under jj and can differ from the branch.** The committed receipt `.../.ufo/rounds/round-21/committed-anchorcheck.json` records a frozen-HEAD snapshot run (`cwd: .../tmp/head-instruments-i1i1m1i1`), and the plan says "committed HEAD anchorcheck". Measured in a colocated repo after `jj commit` without a bookmark move:

```
$ git rev-parse --short HEAD; git rev-parse --short master
972d385
070f934
$ git ls-tree -r --name-only HEAD     # f.md, only-in-head.md
$ git ls-tree -r --name-only master   # f.md
$ git archive HEAD | tar -t | wc -l ; git archive master | tar -t | wc -l
2
1
```

After the helper's bookmark set + push, `git rev-parse HEAD == master == origin/master == pushed` (measured `cdbe08d`), so the receipt is only correct **post-helper**; any lane that runs it between `jj commit` and `jj bookmark set` grades off-branch content.

**F5 — `git ls-files` is index-of-`@` under jj.** Fresh colocated repo, untracked file `runtime.log`:

```
$ git ls-files                    # tracked.txt
$ jj status                       # A runtime.log
$ git ls-files                    # runtime.log, tracked.txt
$ (git cat-file -e HEAD:runtime.log 2>/dev/null && echo yes || echo no)
no
$ git status --short              # " A runtime.log"
```

`git diff --cached` is non-empty before `jj commit` and empty after it (staged entries are absorbed into `@-`). Any lane gate using `git ls-files`, `git diff --cached`, `git status --porcelain` reads jj's working-copy tree, not commit contents.

**F6 — a bare `git commit` in a jj lane orphans the commit.** Following the plan instruction verbatim:

```
$ git symbolic-ref -q HEAD || echo detached      # detached
$ printf 'v3\n' > f.md && git add f.md && git -c user.name=... -c user.email=... commit -qm 'git commit under jj'
$ git log --oneline -3
1ce4440 git commit under jj
065ad33 jj commit
906bbe6 base
$ git rev-parse --short master
906bbe6
$ jj status
Reset the working copy parent to the new Git HEAD.
```

The commit never touched `master`, and jj re-parented the working copy onto it.

**F7 — the call site is not robust.** Three measured failures, all in `git_show`:
- non-UTF-8 pinned blob → uncaught `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 4` and exit 1 (the non-pin path handles the same file with `errors='replace'` and prints `�� bad byte`);
- no `git` on `PATH` → uncaught `FileNotFoundError: [Errno 2] No such file or directory: 'git'` (gate dies instead of returning a verdict);
- abbreviated pins are accepted as-is with no uniqueness/ancestry check.

**F8 — the sanctioned path is mechanically sound.** In the clone, after `jj git init --colocate` + a `jj commit` (detached HEAD), all receipt commands still returned their baseline values, and both live instruments returned baseline output:

```
ls-tree: 25   show: 69   archive: 106        # identical before/after the jj mutation
== SKILL.md: 7 in-range cite instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306 PIN-BROKEN=0 ...
mean dens 154.0
test_resolve.py: Ran 10 tests ... OK
```

`jj git push` exports the bookmark to `refs/heads/<branch>` (`git rev-parse master` == jj bookmark == pushed hash), so git-based readers keep working.

**F9 — the lane's declared `.ufo` invariant is narrower than assumed.** `.ufo/` is not untracked here: `git ls-files .ufo | wc -l` = **28** (round-21 receipts are committed deliberately). `.ufo/interactive-sessions/` is the only ignored subtree; `.ufo/state/` is absent. With the helper's `snapshot.auto-track = "none()"`, a new `.ufo/state/s.json` stayed untracked and a pathspec commit of `LOG.md` committed only `LOG.md` (measured); with default auto-track, jj snapped the untracked file into `@` (`A runtime.log`).

**F10 — immutability of pushed commits depends on `trunk()` being current.** With the helper's `revset-aliases."trunk()" = "<branch>@origin"` and a real push, the pushed tip is protected:

```
$ jj describe -r master -m 'rewrite pushed?'
Error: Commit cdbe08d4a3b1 is immutable
```

With no `origin` at all (remote removed), the same command succeeded: `Rebased 3 descendant commits.` [INFERENCE] A stale but present `master@origin` produces the same exposure for every commit past that bookmark, since `trunk()` is then outside the rewritten range. The "pushed commits are never rewritten" invariant is therefore a jj-config property (current `trunk()`), not a git property.

## 5. Top three risks for this lane

1. **The anchor gate cannot tell "landed" from "local".** `git show <pin>:<path>` resolves any object in the store — off-bookmark jj commits (F1) and rewritten commits kept alive by `refs/jj/keep` (F2) both yield `0 bad`. The lane's own `corpus/knowledge/repo-git-state.md:42` already states the rule for git claims: "single-witness git claims need `--is-ancestor`, not `log --oneline` eyeballing" — `anchorcheck.py` does not implement it, and jj makes the failure routine because `jj commit` places work outside the bookmark by default. This is the lane's only git code and the source of its frozen-tree verdicts.
2. **The surviving class-B instruction produces orphaned commits.** `plans/wwkd-round-21-authority-audit.md:33` still says to commit with `git -c user.name=… -c user.email=… commit`. Under jj's detached HEAD it creates a commit off-branch and leaves `master` untouched (F6); the next `jj` command imports it as the working-copy parent, so the error is silent. Every lane write must go through `scripts/hyaku/jj-lane.sh commit`.
3. **Index-based checks silently change meaning.** `git ls-files`, `git diff --cached`, and `git status --porcelain` now describe `@` (the snapshotted working copy), not the commit (F5). `SKILL.md:279` is the lane's instance of that method, and `.ufo/`'s 28 tracked files make any "tracked vs untracked" census load-bearing. Replace with `git ls-tree -r --name-only <branch>` for committed content and `jj file list` for working-copy content.

## 6. Residual risk and verification gaps

- **No hook/attribute exposure today**, so jj's bypass (section 3) is currently inert. Any future `.gitattributes`, `core.hooksPath`, or LFS rule is invisible to jj writes and visible to `git show` — the two would diverge with no gate noticing.
- **Abbreviated pins** (7 chars) are not uniqueness-checked; a collision would turn a good pin into `PIN-BROKEN`, and `jj` history churn increases object count. Not observed.
- **`find_lane_root` tests `.git` with `os.path.isdir`.** A non-colocated jj repo (no top-level `.git`, store under `.jj/repo/store/git`) would walk past the lane and could run `git show` in an ancestor repo. Not triggered here: the lane has root `SKILL.md`, which short-circuits the walk. The fleet plan colocates, so acceptable — but a seed lane without `SKILL.md` would break.
- **Ancestry is not push state.** Even with `merge-base --is-ancestor`, a commit can be an ancestor of local `master` and unpushed (helper exit 3 path). A landed check needs `git rev-parse <branch>` == `git rev-parse origin/<branch>` (or an explicit push receipt).
- **Not run (by design):** the helper script (read only, never executed), any lane/fleet script against a live path, and any real remote push. The only push was to a sandbox bare repo (`origin.git`).

## 7. Recommendations

1. `anchorcheck.py`: before trusting a pin, require `git merge-base --is-ancestor <obj> <branch>` and return a distinct verdict (e.g. `PIN-OFF-BRANCH`); optionally require `git rev-parse <branch>` == `origin/<branch>` for "landed". Use `p.stdout.splitlines()`, pass `errors='replace'`, and wrap `subprocess.run` to return `PIN-BROKEN` (or a new `GIT-UNAVAILABLE`) instead of raising. That is a ~10-line change in `git_show` and removes F1/F3/F7.
2. Delete the class-B step in `plans/wwkd-round-21-authority-audit.md` or rewrite it to `scripts/hyaku/jj-lane.sh commit <lane> --as kasegi -m <msg> -- <paths>`; add the same line to `AGENTS.md` so no round re-derives a `git commit`.
3. Freeze receipts from the branch, not `HEAD`: `git archive master` / `git rev-parse master` in `SCORECARD.md` and the round plan's step 4. Post-helper they coincide (measured), pre-helper they do not (F4).
4. Do not add `.gitattributes`, hooks, or LFS rules to this lane while jj performs the writes; if a filter becomes necessary, route that path's writes through git or re-verify bytes in `anchorcheck`.
5. Keep the helper's `snapshot.auto-track = "none()"` and the `.ufo/state/*` rejection — both were measured to hold (F9); `.ufo/rounds` and `.ufo/reports` stay intentionally tracked.

## 8. Sandbox

`/fast/scratch/jj-wave/JjAuditKasegi-2/` is preserved because it reproduces F1–F7 (`exp5` pin probes, `exp7` attributes, `exp11` git-commit-under-jj, `exp12`/`origin.git` immutability, `exp13` HEAD-vs-branch, `kasegi-clone`/`ufo-probe` for the real lane copy). No writes were made to the live lane (`git status --short` empty before and after).
