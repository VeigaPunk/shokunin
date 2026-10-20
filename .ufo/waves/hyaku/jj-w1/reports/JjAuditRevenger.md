# jj migration audit — lane `revenger` (read-only)

Date 2026-10-20 · Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` @ `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` (`main`, upstream `origin/main`) · jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` · Sandbox `/fast/scratch/jj-wave/JjAuditRevenger-2` (removed after evidence capture) · No live repo was written, staged, committed, fetched or pushed; live reads were `cat/grep/find` and `git -C <live> log|show|ls-files|rev-parse|status|diff|config`.

## Findings (observed)

### F1 — The lane's executable tooling contains zero git invocations (class A/B/C/D = 0)

Every in-scope script was read or scanned. The complete executable inventory is 30 `.py`, 6 `.js`, 0 `.sh`, 0 `.mjs`, 0 `Makefile`; three files carry the executable bit: `corpus/verify_pe_resources.py`, `reports/round-1/replay_scenarios.py`, and the ELF fixture `corpus/fixtures/checksum-r1/checksum` (`file`: "ELF 64-bit LSB pie executable … not stripped"; `strings | grep -icE 'git|commit'` = 0).

Search coverage (all run from the lane root):

```
$ grep -rnE '\bgit\b' --include='*.sh' --include='*.py' --include='*.mjs' --include='*.js' --include='Makefile' . | grep -v '^./.git/'
./reports/round-1/replay_scenarios.py:364: ... "live/runs/round-NN records; point at an isolated git-archive "
$ grep -rniE '\bgit\b' corpus --include='*.py' --include='*.js' --include='*.mjs' --include='*.sh' | wc -l
0
$ grep -rnE 'check_output|check_call|subprocess\.|os\.system|os\.popen|os\.exec|os\.spawn|shutil\.which|pty\.spawn|child_process|execFile|execSync|spawnSync|spawn\(|bash -c|sh -c' --include='*.py' --include='*.js' --include='*.mjs' --include='*.sh' .
./reports/round-1/replay_scenarios.py:90:    proc = subprocess.run(
$ grep -rnE 'GIT_' --include='*.py' --include='*.js' --include='*.mjs' --include='*.sh' .
(no output)
$ grep -rn --include='*.py' --include='*.sh' --include='*.js' --include='*.mjs' --include='Makefile' -e '\.git' -e 'GIT_' .
(no output)
$ grep -rnE 'LOG\.md|\.ufo/state|merge-base|refs/heads|symbolic-ref|@\{u\}|--abbrev-ref|show-current|rev-parse' --include='*.py' --include='*.js' --include='*.mjs' --include='*.sh' .
(no output)
```

The single spawn site is not git: `reports/round-1/replay_scenarios.py:90` runs `subprocess.run([sys.executable, "-B", script], cwd=str(cwd), capture_output=True, text=True, timeout=TIMEOUT_SECONDS)` (lines 90-96). It inherits the environment wholesale (`env` not overridden) but the invoked verifier opens no repo. The only occurrence of the token `git` in executable tooling is the help string at `reports/round-1/replay_scenarios.py:364` ("point at an isolated git-archive extraction"); it is not executed.

Consequence: no call site exists to classify — the lane's executable surface cannot assume an attached HEAD, mutate history/index/worktree, read staging state, or depend on a HEAD commit through git. None of the six protocol invariants is enforced by lane code: the two that `jj-lane.sh` can enforce (lane identity, pathspec limit) live only in that fleet-root helper, and `LOG.md` append-only plus the `.ufo/state/` exclusion have no enforcement in the lane at all.

### F2 — The assignment's named paths do not exist in this lane

```
$ ls -d tools scripts verifiers
ls: cannot access 'tools': No such file or directory
ls: cannot access 'scripts': No such file or directory
ls: cannot access 'verifiers': No such file or directory
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.js' -o -name '*.mjs' -o -name 'Makefile' \) -print
(no output)
$ find . -maxdepth 3 -name 'SKILL.md'   # run at fleet root
./kaidoku-shokunin/SKILL.md  ./game-dev-3d-shokunin/SKILL.md  ./lore-shokunin/SKILL.md  ... (sibling lanes only)
```

`revenger-shokunin` has no `SKILL.md`, so the "gates and selftests named in SKILL.md" cannot be audited as such; there are also no `tools/`, `scripts/` or `verifiers/` directories. `git ls-files | awk -F/ '{print $1}' | sort | uniq -c` gives `466 corpus / 27 .ufo / 23 reports` plus the five root docs. The lane's verifiers are the 10 `corpus/verify_*.py` files plus the runner `reports/round-1/replay_scenarios.py`; all 30 `.py` files were scanned and none invokes git — the runner's sole `git` token is the help string at line 364.

### F3 — No git hooks, hook path, attributes, filters or eol rules are in use

```
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample' | wc -l
0
$ git config --get core.hooksPath ; echo rc=$?          # local, then global, then system
rc=1  (global rc=1; `git config --system --list | grep -Ei 'hooks'` empty)
$ find . -path ./.git -prune -o -name '.gitattributes' -print
(no output)                         # also absent: .git/info/attributes, core.attributesfile (rc=1)
$ git check-attr text eol filter ident -- corpus/README.md corpus/verify_pe_resources.py SCORECARD.md reports/round-1/replay_scenarios.py
corpus/README.md: text: unspecified        ... eol: unspecified ... filter: unspecified ... ident: unspecified
(repeated "unspecified" for all four attributes on all four paths)
$ git config --get core.autocrlf ; echo rc=$?           # rc=1
$ git config --get core.eol ; echo rc=$?                # rc=1
$ git grep -I -l 'git-lfs' -- . | wc -l
0
```

The **only** filter configuration in effect is global, in `~/.config/git/config`: `filter.lfs.clean=git-lfs clean -- %f`, `filter.lfs.smudge=git-lfs smudge -- %f`, `filter.lfs.process=git-lfs filter-process`, `filter.lfs.required=true`. No lane `.gitattributes` binds any path to `filter=lfs`, and no blob is an LFS pointer, so the configuration is inert. There is no `.gitmodules`, no sparse-checkout, no `core.fsmonitor`, no `core.untrackedCache`; one worktree (`git worktree list` → `.../revenger-shokunin cf02419 [main]`); index entries 522; `git diff --cached --name-only | wc -l` = 0. `.gitignore` contains only `.ufo/interactive-sessions/`.

The hook/attribute bypass jj performs is therefore currently **inert for this lane** — there is nothing to bypass. (The sandbox demonstrates what would happen if either were added; see F5.)

### F4 — The documented gate commands are class D with explicit revisions, plus two class-A HEAD idioms and class-C status/diff checks

These are committed prose/JSON gate procedures, not executable code. Exact occurrences were counted with `grep -oF` over `SCORECARD.md LOG.md reports/round-1/*.json reports/round-1/*.md`:

| Location | Exact command | Class | Risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `SCORECARD.md:27` | `git archive --format=tar <measured-commit> corpus` | D | Low. Rev-addressed and index-free; independent of HEAD. Requires the hash to stay reachable (pushed, never rewritten). | Keep. Feed `<measured-commit>` from `jj-lane.sh push`'s `pushed <hash>`, never from `HEAD` or the pre-push `committed <hash>`. |
| `SCORECARD.md:126`, `:133` | `git archive`; `git show` (base `a7acc20`) | D | Low, same as above; explicit base hash is safe while reachable. | Keep; prefer full 40-hex hashes. |
| `reports/round-1/counting-commands.json:7` | `git archive --format=tar <commit> corpus` (revision protocol) | D | Low. | Keep; cite only pushed hashes. |
| `reports/round-1/measured-before.json:4` | `git archive --format=tar <commit> corpus` | D | Low. | Keep. |
| `reports/round-1/measurements.json:12,18,27,33` | "isolated git archive of `<hash>` corpus" (provenance) | D | Low; provenance is hash-addressed. | Keep; verify hash is ancestor of `refs/heads/main` or `refs/remotes/origin/main`. |
| `reports/round-1/input-preservation.json:71` | `git show <baseline>:<path>` == `git show <work>:<path>` | D | Low. Explicit revs; independent of index/HEAD. | Keep; full hashes. |
| `reports/round-1/scenarios.md:24` | `git archive 286033c5… corpus \| tar -x -C /tmp/baseline-r1` | D | Low. | Keep. |
| `reports/round-1/scout.md:9`, `:231` | `git show 286033c5:corpus/…`; `git diff --stat 286033c5 -- corpus/` | D | Low; explicit rev. | Keep. |
| `reports/round-1/scribe.md:333` | `git log/status` (read-only inspection idiom) | D (log) | Low for `log` with an explicit rev; **not** low if `log` defaults to `HEAD` — HEAD is `@-`, which may be an unbookmarked commit (F5). | `git log <explicit-rev>` or `jj --ignore-working-copy log -r 'heads(bookmarks(main))'`. |
| `reports/round-1/input-ledger.json:18` | "git status of corpus/ was clean before and after the census" | C | Medium. Under jj, `git status` compares worktree/index against `HEAD` = `@-`; the index is jj-managed and may hold intent-to-add entries. Clean status does **not** prove the branch contains the work (F5). | `jj --ignore-working-copy status` + `jj --ignore-working-copy diff --summary -r @`; if git is required, `git status --porcelain` plus explicit `git rev-parse refs/heads/main`. |
| `reports/round-1/scribe.md:100,273,283,312`; `connector.md:47`; `input-ledger.md:9`; `reviewer.md:4` | `git status` (cleanliness claims) | C | Medium, same mechanism: index reset on jj mutations and intent-to-add for jj-tracked working-copy paths. Historical claims were true under git; re-running them post-colocation has different semantics. | As above. |
| `reports/round-1/scribe.md:275` | `git diff --stat` (no rev) | C | Medium: reads index/worktree; jj resets the index and registers jj-tracked uncommitted paths as intent-to-add. | `jj --ignore-working-copy diff --stat` or `git diff --stat <explicit-rev>`. |
| `reports/round-1/scribe.md:42` | `git merge-base --is-ancestor <hash> HEAD` (closure conformance) | **A** | **High.** `HEAD` is not the branch under jj: after `jj commit` HEAD detaches to `@-`; after an unbookmarked `jj commit`, an ancestry test against HEAD passes for a commit that is **not** on `main` (observed F5). Also fails/refuses when the cited hash was rewritten by a push-retry rebase. | `git merge-base --is-ancestor <hash> refs/heads/main` (or `refs/remotes/origin/main`) after `git cat-file -e <hash>^{commit}`; jj form: `jj --ignore-working-copy log -r '::<hash> & heads(bookmarks(main))'`. |
| `LOG.md:318` | `git cat-file -e HEAD:.shokunin/revenger/corpus/verify_pe_resources.py` | **A** | **High if reused.** Assumes HEAD is the lane tip; under jj HEAD = `@-`, and an unbookmarked `jj commit` makes HEAD a commit the branch does not contain (observed). | `git cat-file -e refs/heads/main:<path>` or `jj --ignore-working-copy file show -r 'heads(bookmarks(main))' <path>`. |

Other `git` mentions in `reports/round-1/*.md` are descriptive (`git toplevel`, `origin https://…`, "did not inspect git state") and contain no command. Two hashes referenced by the lane are **not** in this repo: `5b471e4` (cited in a skipped `.ufo` scribe audit against the fleet-ledger worktree) and `f27b5f1…` (no such object in this repository). Every hash the lane's committed reports use as a base/work commit resolves and is an ancestor of `main` today: `286033c5`, `7c3ce19`, `8bbcb4`, `35b2e8b`, `a7acc20`, `cf02419` (`git rev-parse --verify <h>^{commit}` + `git merge-base --is-ancestor <h> main` → `ancestor`).

### F5 — Colocated sandbox probe (jj 0.45.1): detached HEAD, jj-managed index, hook and eol bypass, HEAD ≠ branch after an unbookmarked commit

Setup (sandbox only; live repo cloned read-only, `origin` re-pointed to a sandbox bare repo and confirmed before any push/fetch):

```
$ git clone --bare /home/vgpnk/Projects/shokunin/revenger-shokunin origin.git
$ git clone origin.git lane
$ git -C lane remote -v
origin  /fast/scratch/jj-wave/JjAuditRevenger-2/origin.git (fetch)
origin  /fast/scratch/jj-wave/JjAuditRevenger-2/origin.git (push)
$ cd lane && jj --config 'snapshot.auto-track="none()"' git init --colocate .
$ jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
$ jj --ignore-working-copy config set --repo user.name  revenger-shokunin
$ jj --ignore-working-copy config set --repo user.email revenger@shokunin.local
$ jj --ignore-working-copy config set --repo 'revset-aliases."trunk()"' '"main@origin"'
$ jj --ignore-working-copy bookmark track main@origin
```

**Init.** HEAD remains attached, so class-A commands happen to work immediately:

```
$ git rev-parse --abbrev-ref HEAD   -> main
$ git symbolic-ref -q HEAD          -> refs/heads/main   (rc 0)
$ git rev-parse --abbrev-ref --symbolic-full-name '@{u}' -> origin/main
$ git rev-parse HEAD main origin/main -> cf02419… cf02419… cf02419…
$ git status --porcelain | wc -l    -> 0
```

**After a helper-shaped commit + push** (`jj file track --include-ignored -- <file>`; `jj metaedit --update-author`; `jj commit -m … -- <file>`; `jj bookmark set main -r @-`; `jj git push --remote origin --bookmark main`), author and committer were both `revenger-shokunin <revenger@shokunin.local>` and the push reported `bookmark: main [move forward from cf02419276e5 to 3b2a998db2e2]`. Class-A commands then break silently or loudly:

```
$ git rev-parse --abbrev-ref HEAD   -> HEAD          (rc 0 — a "branch name" that is not a branch)
$ git branch --show-current         -> (empty)       (rc 0)
$ git symbolic-ref -q HEAD          -> (no output)   (rc 1)
$ git rev-parse --abbrev-ref --symbolic-full-name '@{u}'
fatal: HEAD does not point to a branch                (rc 128)
$ git rev-parse HEAD main origin/main -> 3b2a998d… 3b2a998d… 3b2a998d…
$ git status --porcelain | wc -l    -> 0
```

**Class D still works** (explicit revs or HEAD as a commit):

```
$ git archive --format=tar HEAD corpus | tar -t | head -3   -> corpus/ corpus/QUALITY.md corpus/README.md (rc 0)
$ git archive --format=tar main corpus | tar -t | head -3   -> (same)
$ git show HEAD:corpus/README.md | head -2                  -> # corpus — revenger index (rc 0)
$ git show cf02419:corpus/README.md | head -2               -> (same)
$ git diff --stat cf02419                                   -> corpus/replay-sandbox-test.md | 1 + (rc 0)
```

**Index is jj-managed (class C).** Staged entries survive a mere `jj status` but are wiped by a state-changing jj command:

```
# after `git add corpus/README.md corpus/index-probe.txt`
$ git diff --cached --name-only      -> corpus/README.md corpus/index-probe.txt
$ jj status                          -> (snapshot; staged entries still present)
$ git diff --cached --name-only      -> corpus/README.md corpus/index-probe.txt
$ jj new -m 'mutation probe'
$ git diff --cached --name-only      -> (empty)
$ git ls-files corpus/index-probe.txt -> (empty)      # and `git status` shows "?? corpus/index-probe.txt"
```

A path that jj tracks but that is not yet committed appears in the index as **intent-to-add** after a snapshot:

```
$ git status --porcelain=v2 -- corpus/tracked-probe.txt
1 .A N... 000000 000000 100644 0000000000000000000000000000000000000000 0000000000000000000000000000000000000000 corpus/tracked-probe.txt
$ git ls-files -s -- corpus/tracked-probe.txt
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	corpus/tracked-probe.txt   # empty blob
$ git diff --cached --name-only -- corpus/tracked-probe.txt | wc -l -> 0
```

**HEAD is not the branch after a jj commit that does not move the bookmark.** `jj commit` advanced HEAD to `997e954…` while `main`/`origin/main` stayed at `3b2a998…`:

```
$ git rev-parse HEAD main origin/main -> 997e954b… 3b2a998… 3b2a998…
$ git status --porcelain | wc -l      -> 0                      # clean, yet main is behind
$ git cat-file -e HEAD:corpus/unbookmarked-probe.txt -> yes
$ git cat-file -e main:corpus/unbookmarked-probe.txt -> no
$ git archive --format=tar HEAD | tar -t | grep -c unbookmarked -> 1
$ git archive --format=tar main | tar -t | grep -c unbookmarked -> 0
$ git log --oneline -1                -> 997e954 unbookmarked probe   # default rev is HEAD, not main
```

**Hooks are bypassed.** With an executable `.git/hooks/pre-commit` writing a marker:

```
$ git hook run pre-commit            -> rc 0; marker = "hook ran"     # hook works under git
$ (make a new jj commit)             -> marker remains absent          # jj never ran it
```

**eol rules are bypassed on jj writes and reintroduced by git touches.** With `.gitattributes` = `*.probe text eol=crlf`:

```
jj commit (LF file)                  -> worktree/index bytes remain LF (`od`: "... o n e \n ...")
$ git ls-files --eol corpus/eol-probe.probe -> i/lf  w/lf  attr/text eol=crlf
# plain git repo, same attribute:
$ rm f.probe && git checkout -- f.probe -> worktree bytes now CRLF (`\r\n`)
# colocated repo, same git checkout:
$ git checkout -- corpus/eol-probe.probe -> worktree bytes CRLF; jj status -> "M corpus/eol-probe.probe"
```

`.jj` needs no `.gitignore` entry: jj writes `.jj/.gitignore` (contents self-ignore the directory), so `git status --porcelain` stays empty while `git status --ignored=matching` shows `!! .jj/.gitignore`, `!! .jj/repo/`, `!! .jj/working_copy/`.

## Classified table — executable tooling

No rows. Search space: 30 `.py` + 6 `.js` + 0 `.sh` + 0 `.mjs` + 0 `Makefile` (all scanned above), plus the 3 executable-bit files. The single spawn site (`replay_scenarios.py:90`) executes `sys.executable` only; no shell, no `git`. No `.git` path, `GIT_*` environment variable, branch/upstream query, or history/index mutation exists in executable tooling.

## Counts per class

| Basis | A | B | C | D | Total |
|---|---:|---:|---:|---:|---:|
| Executable tooling call sites (30 py, 6 js, 0 sh/mjs/Makefile) | 0 | 0 | 0 | 0 | **0** |
| Committed gate docs (`SCORECARD.md`, `LOG.md`, `reports/round-1/*.json`, `reports/round-1/*.md`) | 2 | 0 | 9 | 20 | **31** |

Documented counts, by exact string: `git archive` ×13 (D), `git show` ×4 (D), `git diff --stat <rev>` ×2 (D), `git log` ×1 (D; `scribe.md:333` is the slash-joined `git log/status`, counted once here), `git status` ×8 (C), `git diff --stat` bare ×1 (C), `git cat-file … HEAD` ×1 (A), `git merge-base … HEAD` ×1 (A). `git rev-parse`, `git ls-tree`, `git checkout`, `git add`, `git commit`, `git push`: 0 occurrences in those gate docs. The two class-A occurrences are the highest-risk documented idioms; the class-C status/diff checks and any default-rev `git log`/`git status` also change semantics (risks 2-3 below). Neither class-A command is executable.

## Hooks and attributes inventory (current)

- Hooks: **none**. `.git/hooks` holds only the 14 `*.sample` files (`applypatch-msg`, `commit-msg`, `fsmonitor-watchman`, `post-update`, `pre-applypatch`, `pre-commit`, `pre-merge-commit`, `prepare-commit-msg`, `pre-push`, `pre-rebase`, `pre-receive`, `push-to-checkout`, `sendemail-validate`, `update`); `find .git/hooks -maxdepth 1 -type f ! -name '*.sample'` = 0.
- `core.hooksPath`: unset at repo, global and system levels.
- Attributes: no `.gitattributes` in the tree, no `.git/info/attributes`, `core.attributesfile` unset; `git check-attr text eol filter ident` → `unspecified` on representative paths.
- eol: `core.autocrlf` and `core.eol` unset.
- Filters: global `filter.lfs.*` (clean/smudge/process/required) only; inert (0 LFS pointer blobs, no binding attribute).
- `.gitignore`: `.ufo/interactive-sessions/` only. `.jj` is not listed but jj self-ignores it (observed).
- `extensions.worktreeConfig`/sparse: absent; one worktree; 522 index entries; 0 staged.

## Top three risks for this lane under jj colocation

1. **The "landed == pushed and ancestor of the branch" invariant has no executable check in the lane, and the one documented check uses `HEAD`.** `reports/round-1/scribe.md:42` prescribes `git merge-base --is-ancestor <hash> HEAD`; under jj, `HEAD` is `@-` (verified) and can be an unbookmarked commit that `main` does not contain (verified: `HEAD` 997e954 vs `main` 3b2a998, clean `git status`). A cited hash can therefore pass the check while never landing on the branch; worse, a push-retry rebase in `jj-lane.sh` can rewrite an unpushed commit so a previously printed `committed <hash>` no longer reaches `main` at all. Nothing in the lane executes the check or distinguishes the helper's `committed` from `pushed` hash.
2. **Latent class-A breakage for future or out-of-lane gates.** Today there are zero git calls, so colocation is a no-op for executable tooling — but the idioms the lane's records use (`git rev-parse --abbrev-ref HEAD`, `git branch --show-current`, `git symbolic-ref`, `@{u}`) fail or lie after the first jj mutation: `--abbrev-ref HEAD` returns the literal string `HEAD` with rc 0, `branch --show-current` returns empty rc 0, and `@{u}` exits 128 (`fatal: HEAD does not point to a branch`). A future script copied from those patterns would silently measure `@-` instead of the branch.
3. **Index- and status-based cleanliness evidence is not reproducible post-colocation.** Eight `git status` occurrences and one bare `git diff --stat` in committed gate docs read an index that jj resets on every state-changing command (`jj new`/`jj commit` wiped staged entries; `git diff --cached` empty) and populates with intent-to-add entries for jj-tracked working-copy paths (` A`, empty-blob index entry). `git status` clean can coexist with `main` being behind (`HEAD` advanced by an unbookmarked jj commit), so a cleanliness check is neither necessary nor sufficient for "landed". The lane's own tooling never reads the index, so this risk is in the documented re-verification procedure, not in the code.

Residual (low, migration-level): `.gitignore` does not cover `.ufo/state/` (`git check-ignore .ufo/state/x` rc 1), and the helper rejects only literal `.ufo/state/*` arguments; a wholesale `-- .ufo` directory argument to `jj-lane.sh commit` would admit state files if they ever appear. The lane has no `.ufo/state/` directory today and no code that commits, so this is a caller-discipline gap, not an active defect. Hooks/attributes are absent now; if added, jj bypasses hooks entirely and does not apply eol on its own writes, while a `git checkout` in the same repo does apply eol and creates jj-visible churn (observed CRLF then `M`).

## [INFERENCE]

- [INFERENCE] Because zero executable git calls exist, initializing this lane with `jj-lane.sh init` changes no lane gate's behavior; the migration risk is concentrated in the documented verification steps and future scripts, not in the present tooling.
- [INFERENCE] Immediately after a helper `commit`+`push` (bookmark moved), `HEAD`, `main` and `origin/main` coincide (observed), so unmodified historical gate commands that use `HEAD` will pass in that window; they diverge as soon as a jj mutation lands without a bookmark move or a push-retry rebase rewrites the unpushed tip.
- [INFERENCE] The helper's push-retry path (fetch + rebase of only unpushed commits) can change the hash printed by `committed <hash>` before `pushed <hash>` is printed; only the latter is cite-safe. This path was read, not exercised (requires a concurrent remote writer).
- [INFERENCE] `.jj` self-ignores via `.jj/.gitignore` (contents: `/*`); no lane `.gitignore` change is required for colocation.

## Recommendations

1. If any executable gate is added, verify the contract with explicit refs: `git cat-file -e <cited>^{commit}` and `git merge-base --is-ancestor <cited> refs/heads/main` (or `refs/remotes/origin/main`). Never use `HEAD`, `@{u}`, `symbolic-ref HEAD` or `--abbrev-ref HEAD` in a colocated lane. Replace the documented `scribe.md:42` idiom before colocation.
2. Cite only the helper's `pushed <hash>` output; do not parse `committed <hash>`, and treat exit 3 (committed, push failed) as not landed.
3. For cleanliness checks use `jj --ignore-working-copy status` and `jj --ignore-working-copy diff --summary -r @`; if git is required, compare against explicit `refs/heads/<branch>` and do not trust `git diff --cached`/`git ls-files -s`/`git status` alone in a colocated repo.
4. Keep this lane free of `.gitattributes`, eol rules and active hooks, or validate them against jj 0.45.1 first; jj writes raw bytes and skips hooks, and a later git checkout/restore reintroduces converted bytes as jj modifications.
5. Do not pass directory arguments (especially `.ufo`) to `jj-lane.sh commit`; commit explicit paths so `.ufo/state/` can never enter, and consider adding `.ufo/state/` to the lane `.gitignore` as defence in depth.
6. Colocation itself is safe for this lane now: no git calls, no hooks, no attributes, `.jj` self-ignores, and `git archive`/`git show`/`git diff <rev>` continue to work with detached HEAD.

## Verification gaps

- Static audit only; the lane's verifier matrix (SCORECARD commands C and F) was not executed — no gate run was required and no code changed.
- The helper's push-retry rebase and conflict-refusal branches were read, not exercised; no multi-writer sandbox remote race was staged.
- Live repos were not fetched; `origin` in the sandbox was a local bare clone and was confirmed with `git remote -v` before the one test push.
- `.ufo/waves/*` outputs (including historical reports containing `git -C … show 5b471e4`) were skipped per the assignment's scope; those references are outside this lane's repository and do not affect the counts above.
- `tools/`, `scripts/`, `verifiers/` and `SKILL.md` do not exist in this lane, so the corresponding portions of the requested scope had no artifacts to audit; this report covers the actual inventory (all `.py`/`.js` tooling, gate docs, hooks/attributes config).
