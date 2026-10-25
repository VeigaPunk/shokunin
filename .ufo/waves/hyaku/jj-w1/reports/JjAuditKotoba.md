# JjAuditKotoba — static git-call audit of lane `kotoba`

- Seat: `JjAuditKotoba-2` · wave `hyaku/jj-w1` · 2026-10-20
- Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`,
  live HEAD `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, **`.jj` absent** (lane not yet colocated).
- Mode: read-only static audit of the lane's executable tooling + sandbox reproduction of jj
  behaviour on jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`. No lane file, index, ref
  or hook was written; no live-repo script was executed. Every live inspection used
  `git -C <live> log|show|ls-files|rev-parse|status|diff` or plain `cat/find/grep`.
- Sandbox: `/fast/scratch/jj-wave/JjAuditKotoba-2` (removed after the run; repro recipe in §11).
- Tool installs: none needed (git and jj 0.45.1 already present).

## 0. Scope actually present

The ticket names `tools/` and `scripts/`; **neither directory exists in this lane** and there is
no `Makefile`, `*.mjs` or `*.js` at the root. The audited set is therefore:

| in scope | files |
|---|---|
| `verifiers/` | 9 `*.py` + `fault_injection_corpus.sh` (the rest are fixtures/baselines/JSON) |
| root | 7 `*.md`, `.gitignore` — no executable |
| SKILL.md gates/selftests | `verify_harness_claims.py`, `verify_skill_checklist.py`, `check_substrate_pins.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `fault_injection_corpus.sh`, `check_assertion_floors.py`, `compare_harness_independent.py`, `verify_surfaces.py`, `verify_harness_independent.py` |
| skipped | `.git/`, `.ufo/` (incl. `waves/` and round evidence scripts), corpus prose |

Command used:

```
find . -path ./.git -prune -o -path ./.ufo -prune -o -type f \
  \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \) -print | sort
find . -path ./.git -prune -o -path ./.ufo -prune -o -type d \( -name tools -o -name scripts -o -name bin \) -print
```

Second command: **no output** — no `tools/`, `scripts/` or `bin/` anywhere in the lane.

## 1. Findings (observed, not inferred)

### F1 — Class A is empty: no lane tool assumes an attached HEAD or an upstream

Sweep for every class-A idiom over all in-scope executables:

```
grep -rn -E '@\{u\}|@\{upstream\}|symbolic-ref|--abbrev-ref|branch --show-current|merge-base' \
  verifiers/ *.py *.sh
```

Hits: only the docstring at `verify_corpus_integrity.py:46` ("record `git status` in the
baseline") and a *quoted example* at `verify_corpus_integrity.py:729` (`git rev-parse --verify
round-5`, inside a test fixture string). No executable `symbolic-ref`, `@{u}`, `--abbrev-ref
HEAD`, `branch --show-current`, or HEAD-as-branch-name call exists in the lane. This is the
single best result of the audit: **nothing in kotoba's tooling has to be rewritten just because
HEAD detaches.**

The only `.git`-shaped assumption outside actual git calls is
`verify_skill_checklist.py:395` (`(cand / ".git").exists()` for repo-root discovery), which
colocation preserves unchanged.

### F2 — `git rev-parse --short HEAD` silently changes referent under jj

Both `head` producers call exactly this:

- `verifiers/compare_harness_independent.py:2399-2404`
  `subprocess.run(["git", "-C", str(cwd), "rev-parse", "--short", "HEAD"], ...)`
- `verifiers/verify_corpus_independent.py:456`
  `head = _git(repo, "rev-parse", "--short", "HEAD").stdout.strip()`

Sandbox measurement (helper's exact sequence: `jj git init --colocate`, repo config
`snapshot.auto-track="none()"`, `jj file track`, `jj commit -- <path>`, `jj bookmark set`):

```
after jj init          : head=master          HEAD=310cad2 master=310cad2
after jj commit+bookmark: head=DETACHED       HEAD=f5d9b77 master=f5d9b77
                          git rev-parse --abbrev-ref '@{u}'
                          -> fatal: HEAD does not point to a branch
after jj new -m 'x'    : head=DETACHED        HEAD=9f5162e master=f5d9b77
later                  : HEAD=7abd7c7 master=f5d9b77
                          git merge-base --is-ancestor HEAD master   (exit 1)
                          -> HEAD IS NOT an ancestor of master
git branch --show-current -> '' (empty)
```

So HEAD is detached at `@-`, the *parent of jj's working-copy commit*. Immediately after a
helper-style commit it coincides with the branch tip; after any `jj new` / `jj edit` /
`jj squash` / rebase it can name an ephemeral commit that is on no bookmark, has never been
pushed, and is not an ancestor of `master`. Both readers are display/receipt-only (see §7), so
nothing fails — the hash is simply recorded as if it identified the audited tree.

### F3 — jj resets the git index on mutation; `git add` state is destroyed

```
$ git add corpus/knowledge/staged.md
after git add:            ls-files=5  cached=corpus/knowledge/staged.md
$ jj new -m 'noop split'
after jj new:             ls-files=4  cached=
                          git status --porcelain -> "?? corpus/knowledge/staged.md"
```

The staged entry is gone from the index and back to untracked. Corollary: any lane procedure
that relies on `git add` as durable state (the corpus baseline literally records
`"git_status": "round-17 staged working tree; new corpus file is tracked in the index"`) has no
equivalent under jj. The only durable "tracked" state is a jj commit.

### F4 — `git ls-files` is jj-owned state, and the reading depends on `snapshot.auto-track`

With the helper's pin (`snapshot.auto-track="none()"`) a brand-new uncommitted file stays
invisible to git, exactly like an unstaged git file:

```
after jj file track new.md alone : ls-files=3 ; status "?? corpus/knowledge/new.md"
after jj commit new.md           : ls-files=4 (README, a.md, new.md, x.py) ; status clean
```

With jj's **default** auto-track (no helper pin — e.g. init skipped, config lost, or a seat
running jj in a repo the helper never initialised) a single snapshot stages every untracked
file into the git index:

```
$ jj st            # default auto-track, new file corpus/knowledge/auto-new.md
ls-files=4         # includes corpus/knowledge/auto-new.md
git status --porcelain
  A corpus/knowledge/auto-new.md
```

`--ignore-working-copy` does **not** snapshot (`auto-2.md` stayed absent after
`jj --ignore-working-copy log -r @`), so read-only helper commands are safe; the hazard is any
snapshotting jj command run outside the helper's config.

### F5 — uncommitted deletion stays in `git ls-files`, so the corpus gates can exit 2

In a helper-configured lane, delete a committed corpus file and do not commit:

```
$ rm corpus/knowledge/new.md
$ git ls-files corpus
corpus/README.md
corpus/knowledge/a.md
corpus/knowledge/new.md      <- listed, but the file is gone
$ git status --porcelain corpus
 D corpus/knowledge/new.md
```

Both corpus instruments turn that list into reads:
`verify_corpus_integrity.py:598-600` (`target.read_text` -> `Inconclusive`, exit 2) and
`verify_corpus_independent.py:68-78` (`_open_text` -> `EnvError`, exit 2). Under git the author
could `git add -A` the deletion away; under jj only a commit updates the index. The gate then
reports *"environment unreadable: cannot read tracked file corpus/...: No such file"*, which
reads as repo breakage, not as "you have an uncommitted deletion".

The deletion **can** be committed through jj pathspec commits (measured: `jj file track` on the
deleted path exits 0, `jj diff --summary` shows `D`, `jj commit -- <path>` exits 0, `git
ls-files corpus` drops to the remaining 2 files), so this is an ordering constraint, not a
dead end.

### F6 — `git clone` of a colocated, detached-HEAD lane works and carries no `.jj`

`fault_injection_corpus.sh:76-79` clones the live repo once per fault world. Measured against a
colocated lane whose HEAD was detached:

```
$ git clone --quiet --no-hardlinks "file://$SB/lane" world   -> exit 0, empty stderr
world .jj? no
world head=master  HEAD=f5d9b77   ls-files=4   git status: clean
$ git -C world checkout --quiet --detach HEAD                 -> exit 0, DETACHED
```

The world is pure git (no `.jj`), so `git add`/`checkout` in the worlds never meet jj. Clone
sees refs only: a jj commit made but not yet moved onto the branch bookmark (helper exits 1
between `jj commit` and `bookmark set`) would be invisible and the worlds would silently test
an older corpus. The harness already copies the *instruments* from the live tree, but not the
corpus content, so the branch-tip assertion below matters.

### F7 — `cat-file -e` resolves jj-authored commits

```
$ git cat-file -e f5d9b777200a4f5b407485593917003d40eea2f3^{commit}   -> OK
```

jj exports commits to the git object database at commit time, and the helper moves the bookmark
in the same run, so the citation checks (`commit_unresolvable`, `commit_nonhash`) keep working.
`git ls-files -s corpus` after a helper-style commit showed every path at stage 0 (no
intent-to-add rows).

### F8 — hooks and attributes: nothing to bypass today

```
$ find .git/hooks -type f ! -name '*.sample' -print      -> (empty; 14 files, all *.sample)
$ git config --get core.hooksPath                        -> (no output)
$ git config --show-origin --get-regexp '^(core\.(autocrlf|eol|hookspath|fsmonitor|sparsecheckout|ignorecase|symlinks)|extensions\.|filter\.)'
file:/home/vgpnk/.config/git/config  filter.lfs.clean=git-lfs clean -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.smudge=git-lfs smudge -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.process=git-lfs filter-process
file:/home/vgpnk/.config/git/config  filter.lfs.required=true
$ find . -name .gitattributes -not -path './.git/*' -print   -> (empty; no .git/info/attributes)
```

There is **no active hook, no `core.hooksPath`, no `.gitattributes` anywhere in the lane, no
`.git/info/attributes`, and `core.autocrlf`/`core.eol` are unset.** The global LFS filter is
defined but unbound (no attribute selects `filter=lfs`), so it is inert. jj bypassing hooks and
filters therefore costs nothing *today*; the exposure is entirely forward-looking (§8).

## 2. Classified table

Class legend: **A** attached-HEAD/upstream assumption · **B** history/index/worktree mutation ·
**C** staging-state read · **D** read-only, HEAD-commit based. "Target" says what the call
actually touches: `lane` (the audited repo), `world` (`fault_injection` throwaway clone),
`tmp` (selftest tempdir).

| # | file:line | exact command | class | target | risk under jj colocation (HEAD may be detached, jj owns the index) | jj-safe replacement |
|---|---|---|---|---|---|---|
| 1 | `verifiers/compare_harness_independent.py:2400` | `git -C <cwd> rev-parse --short HEAD` | D | lane | HEAD is `@-`, detached, possibly on no bookmark and not on the branch; receipt field `head` becomes an unpushed ephemeral hash. Never errors. | Resolve branch first (`b=$(git symbolic-ref -q --short HEAD \|\| git rev-parse --abbrev-ref origin/HEAD)`) then `git rev-parse --short "refs/heads/${b#origin/}"`; or `jj --ignore-working-copy log -r 'trunk()' -T commit_id`. |
| 2 | `verifiers/verify_corpus_integrity.py:549` (argv at `526-527`) | `git -C <repo> ls-files corpus/` | D | lane | Index is jj-owned. With `snapshot.auto-track="none()"` it equals the committed corpus (good); with default auto-track one snapshot adds every uncommitted file as `A`, inflating `tracked_files` and clearing UNINDEXED/STALE. | Count committed population: `git ls-tree -r --name-only refs/heads/<branch> -- corpus/`. If index semantics are really wanted, pin auto-track in repo config and assert `git diff --cached --name-only` is empty. |
| 3 | `verifiers/verify_corpus_integrity.py:560` | `git -C <repo> rev-parse --git-dir` | D | lane | None: colocation keeps `.git` (repository discovery unchanged). | Keep. |
| 4 | `verifiers/verify_corpus_integrity.py:607` (argv at `541-542`) | `git -C <repo> cat-file -e <hex>^{commit}` | D | lane | None observed: jj exports commits to git objects; helper moves the bookmark in the same run. | Keep; optional cross-check with `jj --ignore-working-copy log -r <rev> -T commit_id`. |
| 5 | `verifiers/verify_corpus_independent.py:83` (argv at `63-64`) | `git -C <repo> ls-files -- corpus/` | D | lane | Same index hazard as #2; drives UNINDEXED/MISSING/STALE in the second witness. | `git ls-tree -r --name-only refs/heads/<branch> -- corpus/` (committed set) or the same pin + `diff --cached` assertion. |
| 6 | `verifiers/verify_corpus_independent.py:449` | `git -C <repo> rev-parse --git-dir` | D | lane | None. | Keep. |
| 7 | `verifiers/verify_corpus_independent.py:456` | `git -C <repo> rev-parse --short HEAD` | D | lane | Same as #1; printed in text (`HEAD <sha>`) and JSON (`"head"`), never compared. | Same branch-resolution replacement. |
| 8 | `verifiers/verify_corpus_independent.py:425` | `git -C <repo> cat-file -e <token>^{commit}` | D | lane | None observed. | Keep. |
| 9 | `verifiers/verify_corpus_independent.py:573` | `git -C <tmp> init -q` | B | tmp | None: tempdir has no `.jj`; only reachable via `--self-test`. | Keep; add `[ ! -d "$root/.jj" ]` guard if TMPDIR could point inside a colocated tree. |
| 10 | `verifiers/verify_corpus_independent.py:574` | `git -C <tmp> add -A` | B | tmp | None (plain-git fixture). | Keep. |
| 11 | `verifiers/verify_corpus_independent.py:576-577` | `git -C <tmp> -c user.email=a@b -c user.name=t commit -q -m init` | B | tmp | None (plain-git fixture; author/committer pinned per-command, so no jj identity leak). | Keep. |
| 12 | `verifiers/verify_corpus_independent.py:662` | `git -C <tmp> rev-parse HEAD` | D | tmp | None (fixture repo is plain git, HEAD attached). | Keep. |
| 13 | `verifiers/verify_corpus_independent.py:676` | `git -C <tmp> add -A` | B | tmp | None. | Keep. |
| 14 | `verifiers/fault_injection_corpus.sh:61` | `git -C "$REPO" rev-parse --git-dir` | D | lane | None. | Keep. |
| 15 | `verifiers/fault_injection_corpus.sh:66` | `git -C "$REPO" rev-parse --short=7 HEAD` | D | lane | Same HEAD referent shift as #1; `REPO_HEAD` is banner-only (`:419`). | Resolve `<branch>` as in #1, then `git rev-parse --short=7 "refs/heads/<branch>"`. |
| 16 | `verifiers/fault_injection_corpus.sh:76` | `git clone --quiet --no-hardlinks "file://$REPO" "$w"` | D (lane read; world write) | lane→world | Works at detached HEAD (measured exit 0); world gets no `.jj`; visibility limited to refs, so a jj commit not yet on the bookmark is invisible and the world silently tests older corpus content. | After clone, assert `git -C "$w" rev-parse refs/heads/<branch>` equals `git -C "$REPO" rev-parse refs/heads/<branch>`; on mismatch print `env unreadable: world not at lane branch tip` and return 2. |
| 17 | `verifiers/fault_injection_corpus.sh:77` | `git clone --quiet --no-hardlinks "$REPO" "$w"` (fallback) | D (lane read; world write) | lane→world | Same as #16. | Same tip assertion. |
| 18 | `verifiers/fault_injection_corpus.sh:79` | `git -C "$w" checkout --quiet --detach HEAD` | B | world | None: the world is a plain-git clone with no `.jj`, so jj's index reset cannot reach it. | Keep; optionally guard `[ ! -d "$w/.jj" ]` to keep it that way. |
| 19 | `verifiers/fault_injection_corpus.sh:195` | `git -C "$1" cat-file -e 'deadbee^{commit}'` | D | world | None. | Keep. |
| 20 | `verifiers/fault_injection_corpus.sh:212` | `git -C "$1" ls-files corpus` (piped to `grep -q`) | D | world | None (plain-git world). | Keep. |
| 21 | `verifiers/fault_injection_corpus.sh:219` | `git -C "$1" add corpus/knowledge/fault-injected-note.md` | B | world | None in the current design (world has no `.jj`). If a world were ever colocated, the next jj snapshot would drop this staged row and `plant_e` would stop being visible to the instrument. | Keep; guard `[ ! -d "$1/.jj" ]` and fail the plant if violated. |
| 22 | `verifiers/fault_injection_corpus.sh:220` | `git -C "$1" ls-files corpus` (piped to `grep -q`) | D | world | None. | Keep. |

Helper/wrapper definitions counted once each, not as sites: `verify_corpus_independent.py:62-65`
(`_git`), `verify_corpus_integrity.py:523-536` (`git`), `:539-544` (`git_ok`),
`compare_harness_independent.py:2397-2409` (`git_head`).

## 3. Counts per class

| class | count | sites |
|---|---|---|
| A (attached HEAD / upstream) | **0** | — |
| B (history/index/worktree mutation) | **6** | independent `573`, `574`, `576-577`, `676`; fault `79`, `219` |
| C (staging-state read) | **0** | no `diff --cached`, `ls-files -s`, `update-index` anywhere |
| D (read-only, HEAD-commit based) | **16** | compare `2400`; independent `83`, `425`, `449`, `456`, `662`; integrity `549`, `560`, `607`; fault `61`, `66`, `76`, `77`, `195`, `212`, `220` |
| **total** | **22** | |

Split by blast radius:

- **Lane-touching: 11** (rows 1-7, 14-17) — these read the audited repo and see jj's refs/index.
- **World-only: 5** (rows 18-22) plus the clone destination side of rows 16-17; **tempdir-only:
  5** (rows 9-13) — plain git, no `.jj`, cannot be reached by jj's index reset.
- **All 6 B calls are non-lane mutations**: 4 in tempdir fixtures and 2 in plain-git clones that
  provably carry no `.jj`.

## 4. Top three risks for this lane

### R1 — `git ls-files` is no longer author-controlled state (false-PASS vector) — **critical if the auto-track pin is ever absent**

`verify_corpus_integrity.py:549` and `verify_corpus_independent.py:83` define "tracked corpus
file" as `git ls-files corpus/`. Under jj that is the *index jj writes*, not what the author
staged. With the helper's `snapshot.auto-track="none()"` the reading is sound and equals the
committed tree. Without it (init never run, repo config lost, `.jj` created by another actor, a
seat running plain `jj st` under default config) a single snapshot stages every untracked corpus
file as `A`, and both corpus gates then certify uncommitted files as tracked:
`tracked_files` rises, `unindexed` falls, `stale_patterns` clears, and a README row naming a
never-committed file passes. That is a **false PASS in the exact instrument that polices the
corpus**, and it leaves no trace in the verdict. Evidence: F4 (default auto-track: `ls-files=4`
with `A corpus/knowledge/auto-new.md` after one `jj st`).

### R2 — `HEAD <sha>` receipts become unpushed, ephemeral provenance — **high, silent**

`compare_harness_independent.py:2400` and `verify_corpus_independent.py:456` record
`--short HEAD`. Under jj HEAD is detached at `@-`; measured `HEAD=7abd7c7 master=f5d9b77` with
`git merge-base --is-ancestor HEAD master` failing. A comparison report can therefore say
"HEAD scanned: `7abd7c7`" for a commit that is on no bookmark, was never pushed, and may be
abandoned by the next jj operation (and eventually collected). Nothing errors, so a later reader
cannot distinguish a faithful receipt from an unreproducible one. Evidence: F2.

### R3 — gate ordering: uncommitted deletion or new corpus file breaks the gate before jj commits it — **medium**

`git ls-files` lists a deleted-but-uncommitted path (F5), so both corpus verifiers try to read a
file that is gone and exit 2 with an "environment unreadable" message. A new-but-uncommitted
file is invisible to `ls-files`, so a README row naming it is classified `stale_patterns`
(DRIFT) until the file is committed. Under the git workflow the author could `git add` the
deletion/new file and gate the staged tree; under jj only a commit moves the index, so the lane
must **commit before gating**. This is a workflow contract change, not a defect in the
verifiers, but it will present as a red gate at exactly the wrong moment unless the lane is told.

## 5. Hooks, filters, eol

- **Active git hooks: none.** `.git/hooks` holds 14 files, all `*.sample`;
  `find .git/hooks -type f ! -name '*.sample'` is empty; `git config --get core.hooksPath`
  returns nothing (local and global).
- **`.gitattributes`: none** anywhere in the working tree, and no `.git/info/attributes`.
- **eol rules: none.** `core.autocrlf` and `core.eol` are unset in local and global config.
- **LFS filter: defined globally, unbound here.** `filter.lfs.{clean,smudge,process}` and
  `filter.lfs.required=true` exist in `~/.config/git/config`, but with no `filter=lfs`
  attribute in the lane the filter never runs. jj's known blindness to git filters and
  `.gitattributes` is therefore a **zero-cost bypass today** — the only forward hazard is
  re-introducing a hook or an LFS/eol rule and assuming jj will honour it.

## 6. Non-invocations (checked, clean)

These in-scope tools were read and contain **no git invocation**: `verify_harness_claims.py`,
`verify_harness_independent.py`, `verify_surfaces.py` (uses `strings` via `subprocess` only),
`check_assertion_floors.py` (re-runs verifiers with `sys.executable` only), `check_substrate_pins.py`
(hashes bytes, never execs), and `verify_skill_checklist.py` (resolves declared command heads with
`shutil.which`; it *does not execute* the commands in SKILL.md, so the `git status` fixtures under
`verifiers/fixtures/checklist/` are data, not call sites). `checklist-command-vocabulary.json`
declares `git` as a resolvable head — that is a PATH probe, not a git call.

## 7. Why the HEAD and `head` findings are provenance-only (source proof)

- `compare_harness_independent.py`: `head` is set at `2495`, rendered at `1295`
  (`- HEAD scanned: ...`) and `1379` (`render_json["head"]`), and copied into the freeze receipt
  at `1695`. No equality, ancestry or branch test consumes it anywhere in the file.
- `verify_corpus_independent.py`: `head` is stored at `456`, returned at `462`, and used only at
  `512` (text banner) and `509` (JSON). No check reads it.
- Therefore under jj these calls **cannot cause a DRIFT/FAIL**; they can only mislabel a receipt.

## 8. Inference

- [INFERENCE] The helper's `snapshot.auto-track="none()"` pin, not the `ls-files` call itself,
  is what keeps the corpus gates honest under jj. Any lane that colocated before that pin
  existed, or that loses the repo-local config, inherits R1 even though it never edits the
  verifiers.
- [INFERENCE] A future fleet-wide `commit-msg`/`pre-commit` hook (e.g. for LOG.md append-only
  enforcement) would be silently skipped under jj colocation; nothing in this lane's tooling
  currently depends on hooks, so the review gate for that change should be "does this need to
  fire on jj commits too?".
- [INFERENCE] If the lane ever adopts Git LFS, jj would commit the pointer/raw mismatch that
  jj's filter blindness implies; `filter.lfs.required=true` would not protect, because jj never
  consults the filter. Keep lane binaries and fixtures out of LFS or keep jj off those paths.
- [INFERENCE] The fault-injection clone is a **snapshot of refs**, not of the working copy. Once
  jj authors commits, the only durable handoff point is "bookmark moved and pushed"; the helper
  enforces that ordering, but the harness has no assertion that the live branch tip it cloned is
  the commit the lane thinks it is (row 16/17 mitigation).

## 9. Recommendations (priority order)

1. **Replace index-derived "tracked" with commit-derived "tracked"** in both corpus
   instruments (`git ls-tree -r --name-only refs/heads/<branch> -- corpus/`), or in the
   alternative keep `ls-files` but add a hard precondition: repo-local
   `snapshot.auto-track="none()"` present, and `git diff --cached --name-only` empty. This
   closes R1 at the source and makes the gate independent of whether a jj snapshot happened.
2. **Stop using `HEAD` as provenance.** Resolve the lane branch first and record
   `refs/heads/<branch>` (or `trunk()` from jj) in `compare_harness_independent.py` and
   `verify_corpus_independent.py`. If the intent is truly "the working tree scanned", record the
   branch tip plus a dirty marker, not `HEAD`.
3. **Write the gate-ordering contract into the lane docs**: corpus files must be jj-committed
   before `verify_corpus_integrity.py` / `verify_corpus_independent.py` run; an uncommitted
   deletion makes them exit 2 by design, and the message is "commit first", not "repo broken".
4. **Add the clone-tip assertion** in `new_world()` (row 16): world tip must equal lane branch
   tip, else exit 2 — otherwise the fault harness silently grades an older corpus after any
   interrupted helper run.
5. **Keep `[ ! -d "$w/.jj" ]` guards** on every world mutation (`checkout`, `add`) so a future
   change to how worlds are built cannot quietly hand a world back to jj.
6. No change needed to the class-C/A surface (there is none), to `cat-file`, `rev-parse
   --git-dir`, or the selftest fixtures; they are already jj-compatible.

## 10. Verification gaps / residual risk

- I did **not execute** any lane verifier or fleet script (read-only mandate). The exit-2
  prediction in F5/R3 follows from source (`read_text`/`_open_text` -> `Inconclusive`/`EnvError`)
  plus the measured `ls-files` output; it was not run end-to-end.
- I replicated the helper's jj sequence by hand in the sandbox; I did not run
  `scripts/hyaku/jj-lane.sh` itself, so its flock, push-retry and conflict-refusal paths are
  untested here (out of lane scope).
- jj garbage collection of abandoned `@` commits was not exercised; a receipt hash from R2 may
  remain resolvable for an unknown period before `jj util gc`, then stop resolving.
- `git clone` while jj holds an operation lock was not tested; the harness already falls back to
  a second clone form and exits 2 on failure.
- A `TMPDIR` set *inside* the colocated lane would put the selftest `git init` fixtures under
  jj's snapshot root; with `auto-track="none()"` they would stay untracked, but this combination
  was not measured.
- Not tested: `git ls-files` behaviour when a lane commit is made with `jj` but the bookmark is
  never moved (the clone-side visibility gap in row 16) — the mechanism is clear from refs, but
  I did not stage an interrupted-helper repro.

## 11. Repro recipe (sandbox only; never run in the live repo)

```
SB=/fast/scratch/jj-wave/JjAuditKotoba-2; mkdir -p "$SB"; cd "$SB"
git init -q --bare remote.git
git init -q -b master lane && cd lane
# seed commit + push to sandbox remote, then:
jj --config 'snapshot.auto-track="none()"' git init --colocate .
jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
jj --ignore-working-copy config set --repo user.name  kotoba-shokunin
jj --ignore-working-copy config set --repo user.email kotoba@shokunin.local
jj --ignore-working-copy config set --repo 'revset-aliases."trunk()"' '"master@origin"'
jj --ignore-working-copy bookmark track master@origin
# observe: git symbolic-ref -q --short HEAD | git rev-parse --short HEAD | git ls-files
```

Each measurement in §1 was produced by adding one step to that base (commit via
`jj file track` + `jj metaedit --update-author` + `jj commit -- <path>` + `jj bookmark set`, then
`jj new`, a default-auto-track clone, a `git clone` of the colocated repo, and an uncommitted
`rm`). The sandbox was removed after the run; the recipe reproduces every excerpt above.
