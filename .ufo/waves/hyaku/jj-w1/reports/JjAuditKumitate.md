# JjAuditKumitate — lane `kumitate` git-invocation audit for jj colocation

- Lane: `/home/vgpnk/Projects/shokunin/kumitate-shokunin`, branch `master`, tip `1770305fae20826b39905a8251ddeca6b4957ac4`, HEAD **attached**, `@{u}=origin/master`, ahead/behind `0 0`, work tree clean, **no `.jj` yet** (checked at audit start with `git rev-parse --abbrev-ref HEAD`, `git rev-parse '@{u}'`, `git status --porcelain`, `[ -d .jj ]`).
- Toolchain: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` at `~/.local/bin/jj`; git is the backend.
- Method: read-only static census of the lane repo, plus isolated jj probes in `/fast/scratch/jj-wave/JjAuditKumitate-2` (bare `origin.git` remotes under that path; `git remote -v` confirmed before every push/fetch). **No `jj` command ran with cwd or `-R` inside the live fleet root or any live lane.** No live repo was written, staged, checked out, fetched or committed to. No tool was installed or upgraded.
- Sandbox: removed after the audit; no cited result depends on it surviving.

## 0. Scope census (what exists, and what does not)

```
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name Makefile \) -print
[end]                                  # NO root-level executable tooling
$ ls -d tools verifiers 2>/dev/null
[end]                                  # tools/ ABSENT, verifiers/ ABSENT
$ ls scripts/
cite-check.mjs  claims-check.mjs  kimi-census.mjs  proxy-check.mjs  round-gate.mjs  sources-check.mjs  surface-probe.mjs
```

`grep -c 'git' scripts/*.mjs` — raw token counts, not call sites:

```
cite-check.mjs 30 · round-gate.mjs 29 · proxy-check.mjs 9 · claims-check.mjs 1
kimi-census.mjs 0 · sources-check.mjs 0 · surface-probe.mjs 0
```

The 9 `proxy-check` hits are all `.git`-tree pruning (`if (e.name === '.git') continue;` at line 499 and fixture prose); the single `claims-check` hit is `PRUNE_DIRS = new Set(['.git', …])` at line 157. Neither executes git. `kimi-census`, `sources-check`, `surface-probe` never name a git subcommand.

Only **two** of the seven SKILL.md gates execute git: **round-gate** (9 production call sites) and **cite-check** (2). All git execution goes through `spawnSync('git', [argv…])` with `shell:false` — no shell interpolation, no `git` in a `bash -c` string of either gate.

## 1. Findings (observed, each with the command run and its output)

### F1 — `round-gate --close` is permanently fail-closed after the first jj commit (class A, 2 sites)

Reproduced end-to-end with the real gate script against a sandbox lane + sandbox main repo, both with bare `origin` remotes:

```
# plain git, before jj:
$ UFO_SRC=/nonexistent/ufo node kumitate-shokunin/scripts/round-gate.mjs --round 2 --lane kumitate \
    --repo <sb>/gate/lane --reports-dir <sb>/gate/main/.ufo/reports --main-repo <sb>/gate/main \
    --origin /nonexistent/ufo --close --json
"verdict": "CLEAN", "errors": 0 ... exit=0

# after: jj git init --colocate + one helper-shaped commit (file track → metaedit --update-author →
# commit -m 'round 2 close note' -- LOG.md → bookmark set master -r @- → git push --bookmark master)
$ (same command)
"findings": [ { "severity": "error", "kind": "UPSTREAM_MISSING",
  "detail": "--repo /fast/scratch/jj-wave/JjAuditKumitate-2/gate/lane: exit 128
              fatal: HEAD does not point to a branch" } ]
exit=2
```

The cause is `scripts/round-gate.mjs:456` (`git rev-list --count '@{u}..HEAD'`). Measured directly in the colocated lane:

```
$ git symbolic-ref -q --short HEAD || echo DETACHED
DETACHED
$ git rev-parse HEAD
195c9ace6fe792cc8244aab8f651282e73af7452        # == refs/heads/master here
$ git rev-list --count '@{u}..HEAD'
fatal: HEAD does not point to a branch
exit=128
$ git log '@{u}..HEAD' --name-only
fatal: HEAD does not point to a branch
exit=128
```

Line 456 maps *any* non-zero exit to `UPSTREAM_MISSING` (round-gate header, line 120-123), so the close-only trio can never be evaluated. `--tracked` is unaffected (exit 0, `ROUND_GATE: CLEAN`) because it only touches `--main-repo`, which remains git-managed.

Detachment trigger, isolated: init alone keeps HEAD attached (`symref=master`); `jj status` (snapshot) keeps it attached; the first commit-graph mutation (`jj commit`, `jj new`) detaches it — `symref=DETACHED head=6ddd48c master=9735bae`.

### F2 — Under jj, HEAD is a detached commit, not the branch: three gates can certify work that never landed

A plain `jj commit -- <path>` does **not** move the bookmark (only the helper's explicit `bookmark set` does). In that state:

```
$ jj commit -m 'unbookmarked commit' -- A.txt
Parent commit (@-) : wnlwzuql ea8e0d54 unbookmarked commit
$ git rev-parse --short master   -> 9735bae        # branch did NOT move
$ git rev-parse --short HEAD     -> ea8e0d5        # detached HEAD moved (== @-)
$ git status --porcelain         -> (empty) exit=0 # TREE_DIRTY says clean
$ git merge-base --is-ancestor ea8e0d54 HEAD          -> exit 0   # citation accepted
$ git merge-base --is-ancestor ea8e0d54 refs/heads/master -> exit 1  # NOT on the branch
$ git log --format=%B -1          -> "unbookmarked commit"   # COMMIT_MISSING would match it
$ git rev-list --count --branches --not --remotes -> 0   # branch/remote queries cannot see it
```

So `COMMIT_CITED_NOT_ANCESTOR` (line 373), `TREE_DIRTY` (line 449) and `COMMIT_MISSING` (line 434) all read detached `HEAD`; the upstream-vs-remote probe that would normally catch this is the one broken in F1. The protocol invariant is "a cited hash stays an ancestor of the **branch**", and SKILL.md:739-740 states the gate checks "ancestors of lane `HEAD`" — under jj that is no longer the same object.

### F3 — jj resets the git index on every graph mutation; `git add` staging is destroyed

```
$ printf 'B2\n' >> B.txt; git add B.txt
$ git diff --cached --name-only
B.txt
$ jj new            # any graph mutation, incl. `jj commit -- paths`
$ git diff --cached --name-only
(empty)             # exit=0, staged entry gone
$ git status --porcelain
 M B.txt            # now an *unstaged* change
```

`jj --ignore-working-copy <read>` leaves the index alone (`git status` unchanged); `jj status` alone also left a staged entry intact in the `auto-track="none()"` case tested. The reset happens on commit/graph mutation. No in-scope production tool stages anything, so the lane's own gates are not broken by this today — but any future `git add`-then-commit path silently loses its work.

### F4 — jj runs no git hooks and applies no `.gitattributes` clean filters

Sandbox repo with `.gitattributes` `*.txt filter=up` and `filter.up.clean = tr a-z A-Z`, plus an executable `.git/hooks/pre-commit` writing a marker:

```
git commit:  g.txt blob = "HELLO"   hook marker = YES
jj commit:   j.txt blob = "world"   hook marker = NO
```

jj writes the commit directly (no hook) and stores worktree bytes (no clean filter). No eol test is cited: `text eol=crlf` leaves the blob LF under git too, so that probe does not discriminate.

### F5 — cite-check is jj-safe at both production sites, with one cosmetic HEAD caveat

```
$ git -C <jj lane> rev-parse --verify --quiet 195c9ace…^{commit}
195c9ace6fe792cc8244aab8f651282e73af7452   exit=0
$ git -C <jj lane> rev-parse --verify --quiet deadbeef1^{commit}
(empty)                                     exit=1   # REV_UNKNOWN path still works
$ git -C <jj lane> rev-list --count 195c9ace…~1..HEAD
1                                            exit=0
```

Pin resolution and the `.ufo`/`--src` scans never depend on a branch. `gitBehindCount` (`<hex>..HEAD`, cite-check:1153-1157) is only a message suffix ("N commits behind HEAD") and drifts when detached `HEAD` ≠ branch tip; it cannot fail the gate.

### F6 — `surface-probe --checklists` transitively runs round-gate, but never with `--close`

`scripts/surface-probe.mjs:858` executes each SKILL.md checklist line via `spawnSync('bash', ['-c', item.command], { cwd: opts.self })`. The checklist (SKILL.md:618-630) includes `node scripts/round-gate.mjs` and `node scripts/round-gate.mjs --tracked`; neither uses `--close`, so the F1 break is not reachable through the checklist. `--close` is documented only in prose (SKILL.md:743, 752) and in round-gate's own usage.

### F7 — hooks / attributes / eol inventory: nothing active

```
$ ls .git/hooks            -> only *.sample files (14 samples, zero live hooks)
$ git config --get-regexp '^(hook\.|core\.hooksPath|core\.fsmonitor|core\.sshCommand)'
(no output, exit=1)
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample'
(none)
$ git ls-files | grep -i 'gitattributes\|gitmodules'
(none, exit=1)             # no .gitattributes anywhere in the lane
$ [ -f .git/info/attributes ] -> no
$ cat .git/info/exclude    -> comment lines only
$ git config --get core.autocrlf / core.eol -> unset / unset
$ git check-attr -a -- SKILL.md -> (no attributes)
```

Global `~/.config/git/config` carries `filter.lfs.{clean,smudge,process,required}` and a `gh` credential helper; with **no `.gitattributes` referencing `filter=lfs`**, the LFS filter is inert. `.jj/` does not pollute `git status`: jj writes `.jj/.gitignore` (`git status --ignored` shows `!! .jj/`), so `TREE_DIRTY` is not permanently red just from colocation.

## 2. Classified table

`<repo>` = `--repo` (lane), `<mainRepo>` = `--main-repo` (fleet root), `<fixture>` = mkdtemp fixture. All calls are argv-only (`shell:false`).

| # | file:line | exact command | class | risk under jj (HEAD may be detached; jj owns the index) | jj-safe replacement |
|---|---|---|---|---|---|
| 1 | `scripts/round-gate.mjs:219` | `git -C <repo> rev-parse --is-inside-work-tree` | D | none (verified `true` under colocation) | keep |
| 2 | `scripts/round-gate.mjs:361` | `git -C <dir> cat-file -e <token>^{commit}` | D | none for exported commits (`HEAD`, `@-`, bookmark tips all resolve); a hash jj never exported cannot be verified [INFERENCE] | keep; contract already requires citing *pushed* hashes |
| 3 | `scripts/round-gate.mjs:373` | `git -C <repo> merge-base --is-ancestor <token> HEAD` | D (HEAD-as-rev) | **real**: passes for a commit on detached HEAD that is not on the branch (F2) | `git -C <repo> merge-base --is-ancestor <token> refs/heads/<branch>`, branch resolved once via `git symbolic-ref -q --short HEAD` → `git symbolic-ref refs/remotes/origin/HEAD` → `master`/`main` (same ladder as `jj-lane.sh:detect_branch`) |
| 4 | `scripts/round-gate.mjs:434` | `git -C <repo> log --format=%B%x00 -n 1000` | D | **real**: reads detached HEAD, so a `round-N` marker on an unlanded commit satisfies `COMMIT_MISSING` (F2) | `git -C <repo> log --format=%B%x00 -n 1000 refs/heads/<branch>` (or `--branches`) |
| 5 | `scripts/round-gate.mjs:449` | `git -C <repo> --no-optional-locks status --porcelain` | C (index+worktree) | **real**: false-clean when work exists only in detached HEAD (F2); jj's index reset (F3) also erases any staged intent before the check | keep `git status`, and under `.jj` add: `jj --ignore-working-copy diff --summary -r @` empty **and** `git rev-list --count HEAD --not refs/heads/<branch>` = 0 |
| 6 | `scripts/round-gate.mjs:456` | `git -C <repo> rev-list --count '@{u}..HEAD'` | **A** | **hard break**: exit 128 `fatal: HEAD does not point to a branch` → `UPSTREAM_MISSING` fail-closed on every round after the first jj commit (F1) | `git -C <repo> rev-list --count refs/remotes/origin/<branch>..refs/heads/<branch>` (verified exit 0 under detached HEAD); optionally `..HEAD` as a second, separate `HEAD_NOT_ON_BRANCH` finding |
| 7 | `scripts/round-gate.mjs:479` | `git -C <mainRepo> ls-files --error-unmatch -- <rel>` | D | low: reads the index, which jj keeps in sync for tracked files; ITA entries make a jj-tracked-uncommitted file look tracked. `--main-repo` is the git-managed fleet root today | keep; if the main repo is ever colocated, pair with the pushed check below |
| 8 | `scripts/round-gate.mjs:483` | `git -C <mainRepo> log '@{u}..HEAD' --name-only` | **A** | same fatal if the **main repo** is ever colocated (not planned; fleet root stays `fleet-commit.sh`) | `git -C <mainRepo> log refs/remotes/origin/<branch>..refs/heads/<branch> --name-only` |
| 9 | `scripts/round-gate.mjs:550` | `git -C <mainRepo> ls-files --error-unmatch -- <rel>` | D | none (main repo is git; index-only read) | keep |
| 10 | `scripts/round-gate.mjs:717` | `git -c user.name=t -c user.email=t@t -c commit.gpgsign=false -C <fixture> <args>` — 36 invocations: `init`, `remote add`, `push -u origin main`, `add -A`, `commit`, `checkout -b/-q`, `rev-parse HEAD` (lines 738-1367) | **B** | none: every fixture is under `mkdtempSync(join(tmpdir(), 'kumitate-round-gate-selftest-'))` (line 690), `GIT_CONFIG_GLOBAL=/dev/null`, no jj | keep; **add** a jj-colocated fixture so `--selftest` covers the detached state |
| 11 | `scripts/round-gate.mjs:719` | `git <FIXTURE_CONFIG> init --bare --quiet -b main <path>` (called at 737) | **B** | none (temp path) | keep |
| 12 | `scripts/cite-check.mjs:1138→1147` | `git -C <repo> rev-parse --verify --quiet <hex>^{commit}` | D | none (verified on a jj lane; detached HEAD irrelevant) | keep |
| 13 | `scripts/cite-check.mjs:1138→1155` | `git -C <repo> rev-list --count <hex>..HEAD` | D | cosmetic: "N commits behind HEAD" drifts when detached HEAD ≠ branch tip; cannot fail the gate | `<hex>..refs/heads/<branch>` or `<hex>..--branches` if the suffix must be exact |
| 14 | `scripts/cite-check.mjs:1674` | `git <args>` cwd=`srcRoot`, 4 invocations: `init -q`, `add -A`, `commit -qm fixture`, `rev-parse HEAD` (1675-1678) | **B** | none (fixture under `mkdtempSync(join(tmpdir(), 'kumitate-cite-selftest-'))`, line 1842) | keep |
| 15 | `scripts/cite-check.mjs:1866` | `git -C <srcRoot> rev-parse HEAD` | D | none (fixture repo) | keep |

## 3. Counts per class

| class | rows | production call sites | fixture call sites | fixture git invocations |
|---|---|---|---|---|
| A (attached HEAD / upstream assumed) | **2** | 2 (lines 456, 483) | 0 | 0 |
| B (mutates history/index/worktree) | **3** | 0 | 3 (717, 719, 1674) | 41 (36 + 1 + 4) |
| C (reads index/staging) | **1** | 1 (line 449) | 0 | 0 |
| D (read-only, HEAD-based) | **9** | 8 (219, 361, 373, 434, 479, 550, 1147, 1155) | 1 (1866) | 1 |
| **total** | **15 rows / 53 invocations** | **11** | 4 | **42** |

Production surface: 11 git invocations in the two gates (round-gate 9, cite-check 2). The other five SKILL.md gates execute no git at all.

## 4. This lane's top three risks

1. **`round-gate --close` cannot return CLEAN under jj** (F1). Two `@{u}..HEAD` sites (456, 483) turn the documented round-close audit into `exit 2 / UPSTREAM_MISSING` after the first jj commit. Measured: CLEAN/exit 0 → FAIL-CLOSED/exit 2 across nothing but `jj init` + one commit. The close-time invariant the fleet relies on ("everything committed is pushed") is currently evaluated by the one check jj breaks first.
2. **Detached HEAD is trusted as the branch** (F2). `merge-base --is-ancestor … HEAD`, `git status --porcelain`, and `git log` all read detached HEAD. A commit that exists only on detached HEAD (bookmark set failed, or any seat runs plain `jj commit`) passes the citation-ancestor check, passes TREE_DIRTY, and can satisfy the round marker — while `refs/heads/master` lacks it. Branch-relative queries (`--branches --not --remotes`) return 0 in that state, so a naive "use the branch ref" fix for F1 would not close this hole; it needs a separate `HEAD --not refs/heads/<branch>` probe.
3. **jj owns the index and bypasses git hooks/filters** (F3/F4). `git add` staging is wiped by the next graph mutation; `jj commit` runs no `pre-commit` hook and applies no `.gitattributes` clean filter (measured: `HELLO` via git vs `world` via jj). Today the lane has zero hooks, zero attributes and no staging tooling, so the blast radius is zero — but the absence of those three things is now load-bearing, and any future addition silently stops enforcing.

## 5. Inference (not directly observed)

- **[INFERENCE]** The reachable trigger for F2 is the helper's own failure path: `jj-lane.sh` runs `commit`, then `bookmark set … || exit 1`. A failed bookmark set leaves `@-` ahead of the branch with an empty `git status`, i.e. exactly the measured F2 state; the helper's `push` would then push the branch (not the new commit) and exit 0, so a later `--close` would see a "clean, pushed" branch while the new commit is detached. The helper seat should confirm this against `jj-lane.sh` directly.
- **[INFERENCE]** jj's git export covers commits reachable from `HEAD` and bookmarks (verified: `cat-file -e` resolves both `@` and `@-`); abandoned or otherwise unreachable jj commits are not tested here and may be absent from the git object DB. Consequence: `COMMIT_CITED_UNRESOLVED` can only ever verify hashes jj exported; citing a pushed hash (the protocol rule) keeps this safe.
- **[INFERENCE]** `round-gate --selftest` will stay green through all of F1/F2 because every fixture is plain git with an attached `main` (lines 737-1369); grep finds no `detach`/`DETACHED` case and the only upstream case is the plain-git `UPSTREAM_MISSING` assertion at line 1211. The suite therefore cannot regress-detect this class of break.

## 6. Recommendations

1. **round-gate, branch resolver + upstream probe (fixes F1).** Resolve the lane branch once (reuse the `detect_branch` ladder from `scripts/hyaku/jj-lane.sh`: `git symbolic-ref -q --short HEAD` → `git symbolic-ref -q refs/remotes/origin/HEAD` → `master`/`main` → first local branch). Replace line 456 with `git rev-list --count refs/remotes/origin/<branch>..refs/heads/<branch>` and line 483 with the `refs/…` form. Both were measured exit 0 under detached HEAD.
2. **round-gate, new finding `HEAD_NOT_ON_BRANCH` (fixes the F2 blind spot).** Add `git rev-list --count HEAD --not refs/heads/<branch>` (measured 1 in the unbookmarked state, 0 in normal helper state) with a fresh finding id, so detached work can never be reported as clean. Keep it separate from `UNPUSHED` so the detail line names the real defect.
3. **round-gate, jj-aware close trio.** Under `.jj`, gate `TREE_DIRTY` on `jj --ignore-working-copy diff --summary -r @` being empty in addition to `git status --porcelain`; point the citation-ancestor check (line 373) at `refs/heads/<branch>` and the marker scan (line 434) at the branch ref. Cite `refs/heads/<branch>`, never bare `HEAD`, in all three.
4. **round-gate, selftest coverage.** Add one jj-colocated fixture: clone → `jj git init --colocate` → helper-shaped commit → assert `--close` is CLEAN and that a bookmarked-lag fixture trips `HEAD_NOT_ON_BRANCH`. Without it the fix is unverifiable by the suite that owns it.
5. **cite-check.** Replace `<hex>..HEAD` (line 1155) with `<hex>..refs/heads/<branch>` (or `--branches`) so the "behind HEAD" suffix is branch-true; keep `rev-parse --verify` as-is.
6. **Unchanged:** `--tracked` (lines 479/483/550 target the git-managed main repo), `rev-parse --is-inside-work-tree`, `cat-file -e`, both `ls-files --error-unmatch` sites, and all fixture git in both suites.
7. **Hooks/attributes:** nothing to migrate (none exist). Do not add `.gitattributes` filters or git hooks to a jj-colocated lane expecting them to run — F4 shows both are bypassed; put such enforcement in the gate scripts instead.

## 7. Residual risk and verification gaps

- **Not run** (main agent owns verification): the live gates (`round-gate --selftest`, `--close`, `--tracked`, `cite-check --selftest`) were not executed against the live lane; every measurement above comes from sandbox replicas.
- The F1 result is specific to jj 0.45.1's export/detach behavior; a jj upgrade that re-attaches HEAD would flip line 456 back to green and re-open the F2 hole with no signal.
- jj's export boundary for unreachable commits is inferred, not measured.
- `git status --porcelain` under jj was measured with `snapshot.auto-track="none()"` and a single working copy; concurrent seats in the same lane working copy (the six live rounds) may interleave jj operations and change which state a gate samples.
- No package, binary or config was installed or modified for this audit; the sandbox `/fast/scratch/jj-wave/JjAuditKumitate-2` was removed.
