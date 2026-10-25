# JjAuditKaidoku — lane `kaidoku` git-invocation audit (read-only)

- Seat: JjAuditKaidoku-2, wave `hyaku/jj-w1` (study-and-falsify for jj 0.45.1 colocation).
- Lane: `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`.
- Baseline at audit time: HEAD `da64646adcb19c1ede7537b799b8c7d283fe43da`, attached (`git rev-parse --abbrev-ref HEAD` → `main`), 8 dirty entries, **no `.jj` yet** (`ls -d .jj` → exit 2). So every risk below is prospective, not an incident.
- Toolchain observed: `git version 2.56.0`, `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`.
- Sandbox: `/fast/scratch/jj-wave/JjAuditKaidoku-2/` (kept; it preserves the HEAD/branch divergence cited below; `REPRO.txt` there records the setup). No live repo was written, staged, committed or fetched; jj ran only with cwd inside that sandbox.

## 1. Scope and method

In-scope executable files (28; root has **0** `*.sh`/`*.py`/`*.mjs`/`*.js`/`Makefile`). The lane has **no** top-level `tools/`, `scripts/` or `verifiers/` directory (`test -d` → absent for all three); the executable surface named by SKILL.md lives under `.ufo/` and is enumerated below:

- `.ufo/gates/`: `c1-census-v10.py`, `citation-drift/citation-drift-probe.py`, `custody-pair/custody-pair.py`
- `.ufo/rounds/interactive-r1/verify-recovery.py`
- `.ufo/waves/round-14/`: `measure.py`, `tools/quote-fidelity.py`
- `.ufo/waves/round-15/`: `measure.py`, `snapshot-inventory.py`
- `.ufo/waves/round-16/`: `controls.py`, `measure.py`, `selection.py`, `selfcheck.py`
- `.ufo/waves/round-17/`: `controls.py`, `measure.py`, `run-carriers.sh`, `verify.py`, `w2/receipt-forge.py`, `tools/*.py` (11)

Git argv appears in **11** of those 28 files; the other 17 contain none (notably `verify-recovery.py`, `c1-census-v10.py`, `quote-fidelity.py`, `snapshot-inventory.py`, `selection.py`, `selfcheck.py`, `run-carriers.sh`, and 9 of the 11 `round-17/tools/*.py`, including `carrier-run.py`, `pins.py`, `compare.py`, `receipt-validate.py`).

Method: static `read` of every call site in context, plus `grep` sweeps for `["git"` argv literals, for class-A patterns (`symbolic-ref|@\{u\}|abbrev-ref|show-current`), for `shell=True|os.system|os.popen` (none), and for `.git/` path literals (none). The lane's scripts were **not executed** (no gate run, no selftest run against the lane). The exact git commands were replicated by hand in the sandbox against a jj-colocated copy, per the wave rules.

Sweep for class-A patterns over the in-scope dirs:

```
$ grep -rn -E 'symbolic-ref|@\{u\}|abbrev-ref|show-current' .ufo/gates .ufo/rounds \
    .ufo/waves/round-14 .ufo/waves/round-15 .ufo/waves/round-16 .ufo/waves/round-17 \
    --include='*.py' --include='*.sh'
(no output; exit 1)
```

**Class A count in lane tooling is zero.** `git symbolic-ref`, `@{u}`, `--abbrev-ref`, `branch --show-current` and HEAD-as-a-branch-name do not occur. (The helper `scripts/hyaku/jj-lane.sh` does call `git symbolic-ref -q --short HEAD`, but it handles the empty result and falls back to `origin/HEAD`/`master`/`main`; it is fleet-level and out of this lane's scope.)

## 2. Findings (observed facts, with the exact probe and output)

### F1. Right after colocation HEAD is attached; after a jj mutation it is detached at `@-`

Sandbox, after `jj git init --colocate` + the helper's repo config:

```
$ git symbolic-ref -q HEAD          -> refs/heads/main
$ git rev-parse HEAD                -> 322f789d2ae0...   (== main)
$ git rev-parse '@{u}'              -> 322f789d2ae0...   (exit 0)
```

After one `jj commit` + `jj --ignore-working-copy bookmark set main -r <hash>`:

```
$ git symbolic-ref -q HEAD          -> (no output; exit 1)
$ git rev-parse HEAD                -> dfc77ec34efe...
$ git rev-parse main                -> dfc77ec34efe...
$ git rev-parse --abbrev-ref HEAD   -> HEAD
$ git branch --show-current         -> (empty, exit 0)
$ git rev-parse '@{u}'              -> fatal: HEAD does not point to a branch   (exit 128)
```

So a detached HEAD breaks `@{u}`, `--abbrev-ref` and `--show-current`, while `rev-parse <branch>`, `rev-parse HEAD`, `show`, `ls-tree` keep working. This matches the plan's note; the lane's tooling is already on the safe side of that line.

### F2. HEAD can be a commit that is not on `main` and not pushed

Sandbox, one `jj commit` performed **without** the helper's bookmark move (the shape any seat can produce with `jj new`, `jj split`, or a direct `jj commit`):

```
$ git rev-parse HEAD                          -> f87053c4e46c155379f799418e65b72b767e76fa
$ git rev-parse main                          -> 4c63e87394b661c1daf968abbd4f79742ef0751e
$ git rev-parse origin/main                   -> 4c63e87394b661c1daf968abbd4f79742ef0751e
$ git symbolic-ref -q HEAD                    -> exit 1  (detached)
$ git merge-base --is-ancestor HEAD main      -> exit 1  (HEAD is NOT an ancestor of main)
$ git rev-parse '@{u}'                        -> fatal: HEAD does not point to a branch
$ git show HEAD:corpus/QUALITY.md             -> succeeds (prints the unpushed line)
```

Every class-D read in this lane therefore still *returns data* when HEAD is off-branch — it just returns the wrong tree. That is the failure mode behind risks 1–3 below. In the helper's normal path (`jj commit` → `bookmark set` → push) HEAD landed on the pushed hash (`HEAD == main == origin/main == 4c63e873…` after `jj git push`), so the divergence is a window/edge, not the steady state.

### F3. The git index is reset by working-copy-changing jj operations

Staged with `git add`, then one jj command, then read back:

```
before:  $ git status --porcelain     -> "M  LOG.md"
         $ git diff --cached --name-only -> LOG.md
after `jj describe -m d4`             -> git diff --cached: (empty); status: " M LOG.md"
after `jj commit -m c3 -- LOG.md`     -> git diff --cached: (empty); status: (clean)
after `jj new`                        -> git diff --cached: (empty); tree checked out
after `jj --ignore-working-copy bookmark set main -r <same hash>`
                                      -> git diff --cached: (empty); status: " M LOG.md"
preserved by: `jj st`, `jj --ignore-working-copy log`, `jj file track`, `jj metaedit --update-author`
```

The plan's stronger phrasing ("jj resets the index on every mutation") is not what this version does; the observed rule is: jj operations that rewrite/check out the working-copy commit or export refs reset the index, snapshot-only and metaedit-style commands do not. Either way, **`git add` staging is not durable in a lane repo**, so class-C reads must not be trusted across a jj call.

### F4. Revision-scoped reads against jj-exported refs are sound

Against the jj-colocated sandbox repo:

```
$ git show main:corpus/QUALITY.md     -> file body
$ git ls-tree -r --name-only main     -> LOG.md  SKILL.md  corpus/QUALITY.md
$ git cat-file -e main:LOG.md         -> exit 0
$ git rev-parse --git-dir             -> .git
$ git rev-parse 'main^{commit}'       -> dfc77ec34efe...
$ git rev-parse 'main^{tree}'         -> e9938ded8095...
$ git rev-list --max-parents=0 main   -> 322f789d2ae0...
$ git -C .ufo/gates/citation-drift rev-parse --git-dir
                                      -> /…/lane/.git     (walk-up works; the probe only tests exit)
```

`git rev-parse main@origin` fails (`ambiguous argument`): `@origin` is jj revset syntax, not git syntax. No lane tool uses it — the helper uses `jj … -r "heads(main@origin)"`. Worth knowing if a new tool is written from the helper's vocabulary.

### F5. Hooks: none in use

```
$ ls .git/hooks | wc -l            -> 14
$ ls .git/hooks | grep -vc sample  -> 0
$ git config --local  --get core.hooksPath ; echo $?  -> (unset) 1
$ git config --global --get core.hooksPath ; echo $?  -> (unset) 1
$ git config --system --get core.hooksPath ; echo $?  -> (unset) 1
```

All 14 entries are `*.sample`. jj bypasses `.git/hooks` entirely, so there is nothing to bypass today; the cost materialises only if a fleet hook (secret scan, commit message policy) is added later.

### F6. Attributes / filters / eol: none in force

```
$ find . -name .gitattributes -not -path './.git/*'   -> (no output)
$ cat .git/info/attributes                           -> absent (exit 1)
$ git config --global --get core.attributesFile ; echo $?   -> (unset) 1
$ git config --local  --get core.autocrlf ; echo $?         -> (unset) 1
$ git config --global --list | grep -E 'autocrlf|core\.eol|filter\.|attributesfile'
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
```

git-lfs filters are configured globally but never assigned by any `.gitattributes` in the lane, so no lane path goes through them and `git add`/`commit` cannot be rewritten by a filter. `jj` does not apply git attributes at all; with none present the bypass is currently a no-op. `.gitignore` is `__pycache__/` and `*.pyc`; jj adds `.jj/.gitignore` containing `/*`, so `.jj` never appears in `git status` (observed: `!! .jj/`, `git ls-files | grep -c '^\.jj'` → 0), and `jj git init --colocate` injected **no** keys into `.git/config` (no `core.hooksPath`, no `jj` section).

### F7. Live-lane context that changes what "landed" means for these tools

`git -C . status --porcelain` at audit time:

```
 M .ufo/waves/round-17/run-carriers.sh
?? .ufo/waves/round-17/verify.py
?? .ufo/waves/round-17/w2/
?? .ufo/waves/round-17/wave2-dispatch-attempts.json
?? .ufo/waves/round-17/wave2-dispatch.json
?? .ufo/waves/round-17/wave2-registration.json
?? .ufo/waves/round-17/wave2-result.txt
?? .ufo/waves/round-17/wave2-spec.json
```

`verify.py` (the only lane tool that *always* derives its gate revision from HEAD) is **untracked** at HEAD, and `.ufo/waves/round-17/verification.json` + `verify/` do not exist (the round-17 verification pass has not run). With `snapshot.auto-track="none()"`, untracked files stay untracked until `jj file track`, and the helper commits only the paths named after `--`; a `verification.json` written by an untracked `verify.py` would not become landed unless both are named. The SKILL.md registry row for `citation-drift` cites `.ufo/waves/round-17/verification.json` as an exercised-argv artifact; that artifact is absent (round-16's exists, with `source_revision: 27b8fc13…`).

## 3. Classified table

Legend: **A** attached-branch/upstream assumption · **B** history/index/worktree mutation · **C** index/staging read · **D** read-only, HEAD-commit based. "live" = runs against the lane repo; "fixture" = runs against a `tempfile.mkdtemp()` repo created by the same script's selftest.

### 3.1 Live-lane call sites (32)

| file:line | command (exact argv) | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `.ufo/gates/citation-drift/citation-drift-probe.py:102` | `["git","-C",root,"show",f"{rev}:{path}"]` | D | Low by itself: works on detached HEAD (F4). Becomes medium when `--rev` is omitted, because the default is `HEAD` (L477) and HEAD may be off-branch/unpushed (F2) — the probe then attests a tree that never landed. | Keep the read; require an explicit `--rev`, or resolve `HEAD`→`refs/heads/<branch>` and refuse if not an ancestor. jj form: `jj file show -r <rev> <path>`. |
| `…/citation-drift-probe.py:265` | `["git","-C",root,"rev-parse","--git-dir"]` | D | None. Works from any subdir and on detached HEAD (verified). | Keep. |
| `…/citation-drift-probe.py:273-275` | `["git","-C",root,"rev-parse","--verify","--quiet","%s^{commit}"%rev]` | D | None for explicit revs; same `--rev HEAD` default caveat as L102. | Keep; add `git merge-base --is-ancestor <rev> refs/heads/<branch>` when `rev` came from HEAD. |
| `.ufo/gates/custody-pair/custody-pair.py:327` (used at L349 as `repo_head(Path.cwd())`) | `["git","rev-parse","HEAD"]`, `cwd=str(cwd)` | D | **High for a custody artifact.** Under jj this is `@-`: equal to the branch tip only immediately after the helper's `bookmark set`; otherwise it records an unbookmarked, unpushed commit (F2). It is also cwd-dependent, so a manual capture outside the lane records the wrong repo or `(none)`. | Record the branch identity too: `rev-parse --verify refs/heads/<branch>` (or `jj --ignore-working-copy log --no-graph -r 'trunk()' -T 'commit_id'`), add a dirty flag, and take the repo path as an argument instead of `Path.cwd()`. |
| `.ufo/waves/round-14/measure.py:10` | `["git","-C",ROOT,"rev-parse",sys.argv[1]]` | D | Low. Branch names resolve in colocation (verified). No `--verify`, so an ambiguous name can resolve to a tag instead of the commit. | `git rev-parse --verify <arg>^{commit}` (as rounds 15–17 already do). |
| `…/round-14/measure.py:13` | `["git","-C",ROOT,"show",f"{revision}:{path}"]` | D | None. | Keep. |
| `…/round-14/measure.py:15` | `["git","-C",ROOT,"ls-tree","-r","--name-only",revision]` | D | None. | Keep. |
| `.ufo/waves/round-15/measure.py:46-48` | wrapper `["git","-C",str(ROOT),*args]` + `rev-parse --verify f"{arg}^{commit}"` | D | None. | Keep. |
| `…/round-15/measure.py:54` | `git("show", f"{revision}:{path}")` | D | None. | Keep. |
| `…/round-15/measure.py:58` | `git("ls-tree","-r","--name-only",revision)` | D | None. | Keep. |
| `.ufo/waves/round-16/measure.py:59-61` | wrapper `L44-47` + `rev-parse --verify …^{commit}` | D | None. | Keep. |
| `…/round-16/measure.py:67` | `git("show", …)` | D | None. | Keep. |
| `…/round-16/measure.py:71` | `git("ls-tree","-r","--name-only",rev)` | D | None. | Keep. |
| `.ufo/waves/round-16/controls.py:62` | wrapper `L48-52` + `rev-parse --verify …^{commit}` | D | None. | Keep. |
| `…/round-16/controls.py:71` | `git("ls-tree","-r","-z",rev)` | D | None. | Keep. |
| `…/round-16/controls.py:95-97` | `git("show", f"{rev}:{path}", text=False)` | D | None. | Keep. |
| `.ufo/waves/round-17/measure.py:70` | wrapper `L57-60` + `rev-parse --verify …^{commit}` | D | None. | Keep. |
| `…/round-17/measure.py:80` | `git(root,"show", f"{rev}:{path}")` | D | None. | Keep. |
| `…/round-17/measure.py:85` | `git(root,"ls-tree","-r","--name-only",rev)` | D | None. | Keep. |
| `.ufo/waves/round-17/controls.py:82` | wrapper `L68-72` + `rev-parse --verify …^{commit}` | D | None. | Keep. |
| `…/round-17/controls.py:92` | `git(root,"ls-tree","-r","-z",rev)` | D | None. | Keep. |
| `…/round-17/controls.py:116-118` | `git(root,"show", f"{rev}:{path}", text=False)` | D | None. | Keep. |
| `.ufo/waves/round-17/verify.py:58` | `git("rev-parse","--verify",sys.argv[1]+"^{commit}")` | D | Low: the caller supplies the rev; nothing asserts it is on the branch. | Add the ancestry assertion below to both `base` and `source`. |
| `.ufo/waves/round-17/verify.py:59` | `git("rev-parse","HEAD")` | D | **Highest risk in the lane.** `source_revision` becomes the revision that `citation-strict --strict`, `controls.py`, `measure.py` and `temporal-sweep.py` all evaluate. Under jj it is `@-`, with no assertion that it is the branch or the pushed tip; F2 shows an unbookmarked commit being silently returned. The verification record would then cite an unpushed tree while `--strict` passes against it. | `source=$(git rev-parse --verify refs/heads/main^{commit})` (or `jj --ignore-working-copy log --no-graph -r 'trunk()' -T 'commit_id'`), then `git merge-base --is-ancestor "$source" refs/heads/main` and `[ refs/heads/main = refs/remotes/origin/main ]`; exit 2 on mismatch, before any command runs. |
| `.ufo/waves/round-17/verify.py:60` | `git("status","--porcelain")` | C | Low–medium: the index is jj-managed and reset by describe/commit/new/bookmark-set (F3), so staged vs unstaged is not representable; after a helper commit it is empty even though `@` is a distinct (empty) commit. As a *dirty-content* record it matched `jj diff --summary` exactly in the sandbox (`M LOG.md`, `M SKILL.md`). | `jj --ignore-working-copy diff --summary` (or `jj st`); keep `status` only as a cross-check. |
| `.ufo/waves/round-17/tools/temporal-sweep.py:68` | `["git","-C",root,"show",f"{rev}:{path}"]` | D | None. | Keep; `jj file show -r <rev> <path>` is an option. |
| `…/temporal-sweep.py:73` | `["git","-C",root,"cat-file","-e",f"{rev}:{path}"]` | D | None. | Keep. |
| `…/temporal-sweep.py:94` | `["git","-C",root,"rev-parse","--verify",f"{rev}^{commit}"]` | D | None. | Keep. |
| `…/temporal-sweep.py:106` | `["git","-C",root,"ls-tree","-r","--name-only",rev,"--"] + SITE_DIRS` | D | None. | Keep. |
| `.ufo/waves/round-17/tools/invocation-audit.py:73` | `_git(root,["rev-parse","--verify",f"{rev}^{commit}"])` (wrapper `L59-63`) | D | None. | Keep. |
| `…/invocation-audit.py:77` | `_git(root,["ls-tree","-r","--name-only",rev,"--",".ufo/"])` | D | Low: with `auto-track="none()"` a receipt written but never tracked is invisible at `rev`, so the audit's unreadable/absent accounting depends on the committer naming paths. | Keep; document that the audit is revision-scoped, or add a worktree-vs-rev delta note. |
| `…/invocation-audit.py:82` | `_git(root,["show",f"{rev}:{path}"],decode=False)` | D | None. | Keep. |

### 3.2 Selftest / fixture call sites (30)

All targets are `tempfile.mkdtemp()` directories (or `workdir = mkdtemp(); repo = workdir/"lane"`) with their own `git init`; jj never manages them.

| file:line | command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `.ufo/gates/citation-drift/citation-drift-probe.py:350` | `["git","init","-q",d]` (`d=mkdtemp`) | B | None. Separate non-colocated repo. Caveat: `mkdtemp` honours `TMPDIR`; if `TMPDIR` pointed inside the lane the fixture would be nested inside the jj working copy (still a separate repo, but its files would be visible to jj snapshots). | Keep; ensure `TMPDIR` is outside the lane, or create fixtures with an explicit `--git-dir`. |
| `…/citation-drift-probe.py:365` | `["git","-C",d,"add","-A"]` | B | None (fixture). | Keep. |
| `…/citation-drift-probe.py:366-367` | `["git","-C",d,"-c","user.email=e@x","-c","user.name=e","commit","-qm",case]` | B | None (fixture). `-c` identity avoids global-config dependence. | Keep. |
| `.ufo/waves/round-17/measure.py:215` | `run("init","-q")` (via L208-214) | B | None (fixture). | Keep. |
| `…/round-17/measure.py:220` | `run("add","-A")` | B | None (fixture). | Keep. |
| `…/round-17/measure.py:221` | `run("commit","-q","-m","fixture")` | B | None (fixture). | Keep. |
| `…/round-17/measure.py:222` | `run("rev-parse","HEAD")` | D | None (fixture HEAD is the just-made commit). | Keep. |
| `.ufo/waves/round-17/controls.py:434` | `git(root,"add","-A")` | B | None (fixture). | Keep. |
| `…/round-17/controls.py:435-441` | `git(root,"-c","user.email=…","-c","user.name=…","commit","-qm",message)` | B | None (fixture). | Keep. |
| `…/round-17/controls.py:442` | `git(root,"rev-parse","HEAD")` | D | None (fixture). | Keep. |
| `…/round-17/controls.py:451` | `git(root,"init","-q")` | B | None (fixture). | Keep. |
| `.ufo/waves/round-17/tools/temporal-sweep.py:234` | `git_in(repo,"init","--quiet")` (wrapper L209-217 adds `-c user.name=… -c user.email=…`) | B | None (fixture). | Keep. |
| `…/temporal-sweep.py:251` / `279` / `298` | `git_in(repo,"add","-A")` (three commits) | B | None (fixture). | Keep. |
| `…/temporal-sweep.py:252` / `280` / `299` | `git_in(repo,"commit","--quiet","-m","rev1"/"rev2"/"rev3")` | B | None (fixture). | Keep. |
| `…/temporal-sweep.py:254` / `282` / `301` | `["git","-C",repo,"rev-parse","HEAD"]` | D | None (fixture). | Keep. |
| `…/temporal-sweep.py:315` | `["git","-C",repo,"rev-list","--max-parents=0","HEAD"]` | D | None (fixture). | Keep. |
| `…/temporal-sweep.py:321` | `["git","-C",repo,"rev-parse",f"{rev0}^{{tree}}"]` | D | None (fixture). | Keep. |
| `.ufo/waves/round-17/tools/invocation-audit.py:367` | `_git(root,["init","-q"])` | B | None (fixture). | Keep. |
| `…/invocation-audit.py:368-370` | `_git(root,["config","user.email"/"user.name"/"commit.gpgsign", …])` | B | None (fixture). | Keep. |
| `…/invocation-audit.py:415` | `_git(root,["add","-A"])` | B | None (fixture). | Keep. |
| `…/invocation-audit.py:416` | `_git(root,["commit","-q","-m","fixture"])` | B | None (fixture). | Keep. |
| `…/invocation-audit.py:417` | `_git(root,["rev-parse","HEAD"])` | D | None (fixture). | Keep. |

## 4. Counts per class

| class | live | fixture | total |
|---|---|---|---|
| A (attached branch / upstream assumed) | 0 | 0 | **0** |
| B (mutates history/index/worktree) | 0 | 22 | **22** |
| C (reads index/staging) | 1 | 0 | **1** |
| D (read-only, HEAD-commit based) | 31 | 8 | **39** |
| **total** | **32** | **30** | **62** |

Per file: `citation-drift-probe.py` 6 (3 D live, 3 B fixture) · `custody-pair.py` 1 D live · `round-14/measure.py` 3 D · `round-15/measure.py` 3 D · `round-16/measure.py` 3 D · `round-16/controls.py` 3 D · `round-17/measure.py` 7 (3 D live, 3 B, 1 D fixture) · `round-17/controls.py` 7 (3 D live, 3 B, 1 D fixture) · `round-17/verify.py` 3 (2 D, 1 C live) · `temporal-sweep.py` 16 (4 D live, 7 B, 5 D fixture) · `invocation-audit.py` 10 (3 D live, 6 B, 1 D fixture).

Of the 17 instruments registered in SKILL.md, **6** make git calls: `citation-drift`, `custody-pair`, `round16-structural-controls`, `round17-structural-controls`, `temporal-sweep`, `invocation-audit`. The other 11 (`interactive-r1-recovery`, `quote-fidelity`, `go-snapshot-inventory`, `go-selection-preview`, `go-carrier-run`, `go-log-extract`, `go-route-predict`, `go-route-compare`, `receipt-validate`, `pins`, `go-buildinfo-probe`) make none and are unaffected.

## 5. Top three risks for this lane

**R1 — `verify.py:59` turns HEAD into the gate revision.** `source_revision = git rev-parse HEAD` is then used as the revision for `temporal-sweep.py` (`--rev source`, L127-128), `controls.py` (L131), `measure.py` (L133), `citation-strict --strict` (L135-139, `--rev source` at L136) and is recorded as `source_revision` (L165). The custody capture that follows (L141-143) runs with cwd=LANE. Under jj, HEAD is `@-` and nothing asserts it is `main` or `origin/main`. Observed divergence: `HEAD=f87053c4…`, `main=origin/main=4c63e873…`, `git merge-base --is-ancestor HEAD main` → exit 1, while `git show HEAD:corpus/QUALITY.md` still succeeds. Result: a verification record and a strict citation gate can attest an unpushed tree — violating "landed = committed AND pushed before a report cites the hash" and "a cited hash stays an ancestor of the branch". `verify.py` is untracked right now, so the fix is free before it is ever committed.

**R2 — `citation-drift-probe.py` default `--rev HEAD` (L477, used by L102/L274).** The registered argv passes `--rev <REV>`, but any default/manual run evaluates `@-`'s tree. Two concrete effects under jj: (a) the probe can pass/fail against a tree that is not on `main`; (b) with `snapshot.auto-track="none()"`, a file written but not tracked/committed is absent at `rev`, so the probe reports `citation_file_absent` for a file that exists in the working copy — a false red that looks like citation drift. Fix: require `--rev`, or resolve it to `refs/heads/<branch>` and refuse when HEAD is not an ancestor.

**R3 — `custody-pair.py:327` records `repo-HEAD` as `@-`.** The custody receipt's identity pin is supposed to tie a content snapshot to a landed commit. Under jj it is the working-copy parent, which equals the branch tip only at the moment the helper returns; after any unbookmarked jj commit it records an unpushed hash (F2). It is additionally computed from `Path.cwd()`, so a capture started outside the lane records a different repo or `(none)` while the rest of the receipt remains internally consistent. Fix: record `repo-branch` + `repo-branch-HEAD` (`refs/heads/<branch>` or `trunk()`) and the dirty flag alongside `repo-HEAD`, and take the repo root explicitly.

The one class-C site (`verify.py:60`, `status --porcelain`) is deliberately ranked below these: it is a record-only field, and in the sandbox it matched `jj diff --summary` exactly. No live class-A and no live class-B site exists, so the lane's git surface is already close to jj-safe; the exposure is concentrated in the three HEAD-keyed reads above.

## 6. [INFERENCE]

- [INFERENCE] The orchestrator/closure will treat `verification.json`'s `source_revision` as the attested tree. I found no round-17 verification record to confirm the citation practice (the file is absent), so the consequence chain is inferred from the field name and from how round-16's record is consumed, not observed.
- [INFERENCE] Had any lane tool used `git diff --cached` / `git add` on the lane, its effect would silently vanish across a jj call (F3). No such live site exists today; the concern is future tools and seat habits ("stage then review"), which jj makes misleading.
- [INFERENCE] `git status --porcelain` is a faithful *content* dirty check under jj only while the index has been reset by the last jj op; if a seat stages files after the last jj op, `git status` will show `M ` entries that `jj diff` cannot distinguish from ` M`. Both orders were observed; the equivalence claim is scoped to the jj-managed state.
- [INFERENCE] jj 0.45.1 exports bookmark moves to git refs synchronously (observed immediately after `bookmark set` and `git push`), so ref staleness is not a risk at this version. A future jj that defers export would turn every class-D read into a stale-read risk.
- [INFERENCE] The ~100 one-off scripts under `.ufo/waves/arc3-loop1-*/claims/**` that also contain `["git", …]` argv (e.g. `…/claims/c1/RV-2/rule-citation-audit.py`, `…/claims/c2/SC-4/scratch/**` probe copies) are wave outputs, excluded per the assignment. They are historical evidence scripts, not instruments re-run by the lane's gates; if any is ever re-run on a colocated lane it inherits the same HEAD-default hazard.

## 7. Recommendations

1. **Pin the branch, not HEAD, in `verify.py`** (R1): `source=$(git rev-parse --verify refs/heads/main^{commit})` or `jj --ignore-working-copy log --no-graph -r 'trunk()' -T 'commit_id'`; then require `git merge-base --is-ancestor "$source" refs/heads/main` **and** `refs/heads/main == refs/remotes/origin/main` before running any gate, exiting 2 with a named finding otherwise. Apply the same to `base`.
2. **Make citation-drift's revision explicit** (R2): make `--rev` required (or reject the literal `HEAD`), and add the ancestry assertion. Document that untracked/uncommitted files are absent by construction under `auto-track="none()"`.
3. **Widen the custody receipt** (R3): add `repo-branch`, `repo-branch-HEAD`, `repo-dirty`, and accept the repo root as an argument; keep `repo-HEAD` for backward comparison.
4. Add a cheap static lint over lane tooling that fails on `"git"` argv containing `HEAD`-as-revision, `@{u}`, `symbolic-ref`, `--abbrev-ref`, or `branch --show-current` outside the known-safe allowlist; run it in the same pass as the existing selftests.
5. Keep class B out of the lane: selftest fixtures must stay under `tempfile.mkdtemp()` (all do), and the lane should not export `TMPDIR` into its own tree. No `git add -A`/`git commit` may ever run with cwd = lane root.
6. If the fleet adds hooks or `.gitattributes` filters (e.g. secret scan, LFS), add a jj-side equivalent: jj does not run `.git/hooks` and does not apply git attributes, so such a control would be silently bypassed in a colocated lane. Today nothing is lost (0 active hooks, 0 attributes).

## 8. Residual risk and verification gaps

- Static audit: no lane gate or selftest was executed (read-only assignment), so exit-code/behavior claims about the gates themselves are out of scope; only the git commands were replicated, in the sandbox.
- The helper's rejected-push → fetch → rebase path was not exercised (helper out of scope; its git calls are `git -C <lane> symbolic-ref/show-ref/for-each-ref/rev-parse/rev-list/status/ls-files`, all read-only, and its own `detect_branch` already handles detached HEAD).
- `.ufo/waves/arc3-loop1-*/claims/**` (≈100 files with git argv) not audited — wave outputs.
- `jj` version tested: 0.45.1 only.
- The live lane has no `.jj` yet, so no finding is an observed live failure; F1–F4 are sandbox observations against a faithful replica of the helper's init/commit/push sequence.

## 9. Compliance notes

- Live repos were read only with `cat`/`ls`/`grep`/`find` and `git -C <live> log|show|ls-files|rev-parse|status|config --list/--get`; nothing was written, staged, committed, fetched or pushed. The lane still shows exactly the 8 pre-existing dirty entries and no `.jj`.
- One process error, disclosed: `jj --version` was run once with cwd = `kaidoku-shokunin` (inside the live tree), before the sandbox existed. `jj --version` exits before repo discovery, printed only the version, and the lane has no `.jj` (verified after); no repo state was read or written. All other jj commands ran with cwd under `/fast/scratch/jj-wave/JjAuditKaidoku-2/`. `jj help` was never run.
- Sandbox kept: `/fast/scratch/jj-wave/JjAuditKaidoku-2/` (with `REPRO.txt`), because it preserves the cited HEAD/branch divergence (`HEAD=f87053c4…` vs `main=4c63e873…`, `merge-base --is-ancestor` exit 1). It can be deleted once this report is integrated.
- No tools were installed or upgraded for this audit.
