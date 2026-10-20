# JjAuditKengaku — lane `kengaku` git-surface audit (jj wave 1)

Seat: `JjAuditKengaku-2` · 2026-10-20 · lane `kengaku`, branch `master`.
Audited tree: `/home/vgpnk/Projects/shokunin/kengaku-shokunin` @ `6180e4f` (attached `master`, clean, `## master...origin/master`).
Tooling: git 2.56.0; jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj`).
Mode: static, read-only audit of the live lane. jj behaviour was exercised **only** in `/fast/scratch/jj-wave/JjAuditKengaku-2` (removed after this report; no failure needed preservation). No tool installed or upgraded.

## Verdict

- **4 executable git call sites in 2 files: all class D. A = 0, B = 0, C = 0.**
- **9 documented (hand-run) git commands** in `plans/`, `SCORECARD.md`, `LOG.md`: all class D.
- No active git hooks, no `.gitattributes`, no filters, no eol rules, no submodules, one worktree.
- The lane is **not yet colocated** (`kengaku-shokunin/.jj` does not exist), so none of the drift below is live today.
- Under colocation, only two semantic drifts appear: the `HEAD` provenance label in `plans/round24_census.sh:8`, and a latent `--revision HEAD` path in the SKILL-registered `coverage-census` probe. Every cited-hash read stays valid (verified in sandbox).

## 1. Findings (observed)

### F1. The executable git surface is four command sites, all read-only

Search (repo-wide, code extensions only; `.git` excluded):

```
$ grep -rnI --exclude-dir=.git --include='*.py' --include='*.sh' \
    --include='*.mjs' --include='*.js' --include='Makefile' \
    -E '\bgit[[:space:]]+[a-z-]' .
./corpus/evidence/round11-fleet/mutate_r11.sh:8:git status --porcelain > "$BASE_STATUS"
./corpus/evidence/round11-fleet/mutate_r11.sh:137:git status --porcelain > "$W/status.after"
./plans/round24_census.sh:6:# with: mkdir -p /tmp/k24base && git archive 99cf615 | tar -x -C /tmp/k24base, then
./plans/round24_census.sh:8:echo "HEAD $(git rev-parse --short HEAD 2>/dev/null || echo n/a)"
```

The only Python spawn of git is the shared helper in the registry probe:

```
$ grep -rnI --exclude-dir=.git --include='*.py' -E '["'"'"']git["'"'"']' .
./corpus/evidence/round13-coverage/coverage_census.py:45: p = subprocess.run(("git", "-C", str(repo)) + tuple(args),
```

`grader.py` (5737 lines) contains **no** git call: its only `subprocess.run` is `[sys.executable, os.path.abspath(__file__), ...]` at `grader.py:5540` (selftest re-entry). A case-insensitive grep for `git` in `grader.py` returns only `_LOGIT_EPS` / `_logit` false positives. `plans/attrib_probe.py` likewise has one `subprocess.run` at `:886` whose argv is `["journalctl", ...]` (constructed at `:885`), not git.

Absent from the lane: `tools/`, `scripts/`, `verifiers/`, any `Makefile`, any `*.mjs`/`*.js` (`find . -path ./.git -prune -o \( -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \) -print` → empty). Root-level executables: `grader.py` only.

The two `mutate_r11.sh` hits are corpus evidence artifacts, not registry entries; they are outside the stated in-scope dirs (`.corpus` skip) and are listed here only for completeness. `git status --porcelain` would be the class-C-adjacent call if it were in scope; under jj it reports jj's exported working-copy state, so it is not a safe staged-state oracle either.

### F2. `plans/round24_census.sh:8` is the only executable HEAD read, and its label is the lane's real jj exposure

```
plans/round24_census.sh:
  6  # with: mkdir -p /tmp/k24base && git archive 99cf615 | tar -x -C /tmp/k24base, then
  8  echo "HEAD $(git rev-parse --short HEAD 2>/dev/null || echo n/a)"
```

The captured outputs show what the line is used for:

```
$ grep -n '^HEAD' corpus/evidence/round24-census/*.txt
corpus/evidence/round24-census/after.txt:3:HEAD 94da19e
corpus/evidence/round24-census/base-99cf615.txt:1:HEAD n/a
$ head -1 corpus/evidence/round24-census/after.txt
# round-24 after-census, run 2026-10-19T19:23:02-03:00 with commit 94da19eea7b9d95f803b68d252f39bee4d33d19d checked out (clean tree)
```

So `HEAD` here is a **provenance label** ("which commit does this working tree correspond to"), not a gate input. That equivalence is true only while HEAD is attached to a clean branch. It is false once jj drives the checkout (F5, F6).

### F3. The SKILL-registered `coverage-census` probe has three git reads, all commit-pinned — one interface hole

`SKILL.md` §Gate/probe registry declares `coverage-census | probe | python3 corpus/evidence/round13-coverage/coverage_census.py [--revision REV]`. Its git layer (`REPO = HERE.parents[3]` = lane root) is:

```
coverage_census.py:
 43  def git(repo, args):
 45      p = subprocess.run(("git", "-C", str(repo)) + tuple(args), capture_output=True)
 65      rc, out, err = git(REPO, ("rev-parse", "--verify", "--quiet",
 66                                 revision + "^{commit}"))
 79      rc, out, err = git(REPO, ("ls-tree", "-z", "%s:%s" % (self.label, rel)))
110      rc, out, err = git(REPO, ("show", "%s:%s" % (self.label, rel)))
```

Default mode (`--revision` omitted) is pure working-tree `open()/iterdir()`: zero git. With `--revision`, the argument is resolved to a **full 40-hex commit** and then every subsequent read uses `commit:path`. That is jj-safe because jj exports committed objects into the git object database (F6). The only hole is the literal input `HEAD`: it resolves successfully to the detached jj commit and the census then reports that id as `revision`, with no check that the id is reachable from `master`.

### F4. Zero lane-side history mutation, staging, or push

No `git add|commit|stash|checkout|reset|rebase|push|pull|merge|clean|tag` appears in any in-scope file (F1 search). The lane's own protocol explicitly forbids lane commits:

```
plans/probe-battery-TEMPLATE.md:70: ... no git commits (parent integrates) |
plans/probe-battery-r19.md:87:7. **No git commits.** The parent integrates under the kengaku lane identity.
```

The lane's only recorded history-mutating habit is the postmortem of a manual `git add`:

```
considerthese/2026-10-19.md:62: ... an r20 evidence backfill caused by a `git add` pathspec error.
```

That is a class-B *mention*, not a call site; it is the one place where jj's staging semantics (F5) would bite a seat that follows old text.

### F5. Sandbox: HEAD detaches, upstream dies, and the index is cleared on working-copy updates (not on a bare snapshot)

Sandbox: local bare `origin.git` + colocated clone, initialized with the helper's exact config sequence (`snapshot.auto-track="none()"`, lane identity, `trunk()=master@origin`, `bookmark track master@origin`); `git remote -v` confirmed the local bare path before any push.

After init, before any mutation — HEAD still attached:

```
$ git symbolic-ref -q --short HEAD          -> master
$ git rev-parse --short HEAD                -> ae2598f
$ git rev-parse --short master              -> ae2598f
$ jj log -r 'master|@' -T ...               -> @ 32ea3160, master ae2598f
```

After `jj commit -m 'lane: census touch' -- LOG.md`:

```
$ git symbolic-ref -q --short HEAD || echo 'HEAD DETACHED'
HEAD DETACHED
$ echo "git HEAD short: $(git rev-parse --short HEAD)"
git HEAD short: 9924aff
$ echo "master: $(git rev-parse --short master)"
master: ae2598f
$ jj log -r 'master|@|@-'
b817c4726479 bm= @          # empty working copy
9924affd0836 bm=            # HEAD is here, on no bookmark
ae2598f62028 bm=master      # branch tip did not move
```

With an uncommitted change in `@`, HEAD stays at `@-` and the tree bytes are not represented by the printed commit:

```
$ printf 'uncommitted line\n' >> LOG.md ; jj --ignore-working-copy st
$ git symbolic-ref -q --short HEAD || echo 'HEAD DETACHED'   -> HEAD DETACHED
$ git rev-parse --short HEAD                                 -> 9924aff
$ git rev-parse --short master                               -> ae2598f
$ git status --porcelain                                     ->  M LOG.md
$ git rev-parse --abbrev-ref HEAD                            -> HEAD
$ git rev-parse --verify 'HEAD@{u}'                          -> fatal: HEAD does not point to a branch
```

Index behaviour (the wave premise says "jj resets the git index on every mutation" — that is **overbroad**):

```
after git add, cached: LOG.md
after jj st,   cached: [LOG.md ]        # bare snapshot did NOT clear the staged entry; status `M  LOG.md`
after jj new:  cached=[] status=[]      # working-copy update DID clear it
after git add + jj commit: cached=[] status=[]
```

So the index is reset by working-copy **updates** (`new`, `commit`, and by extension `edit`/`checkout`/`abandon`), not by a snapshot-only command. `git add` staging in a colocated lane is silently destroyed by the next update — no error, no warning.

Commit-pinned reads survive colocation, including for commits created before colocation:

```
$ git archive ae2598f LOG.md | tar -t        -> LOG.md
$ git diff --stat ae2598f -- LOG.md          -> 1 file changed, 2 insertions(+)
$ git ls-tree -r ae2598f --name-only         -> LOG.md
$ git show ae2598f:LOG.md                    -> seed
```

Bookmarks are exported back to git refs immediately (this is what makes a branch-pinned replacement valid):

```
$ jj --ignore-working-copy bookmark set master -r @-
$ git rev-parse --short refs/heads/master    -> 1d72f7e   (== HEAD)
```

### F6. Live lane state: not colocated, clean, correct identity

```
$ ls -d .jj                                   -> No such file or directory
$ git rev-parse --abbrev-ref HEAD             -> master
$ git rev-parse --short HEAD                  -> 6180e4f
$ git status --porcelain --branch             -> ## master...origin/master
$ git config user.name / user.email           -> kengaku-shokunin / kengaku@shokunin.local
$ git remote -v                               -> https://github.com/VeigaPunk/kengaku-shokunin.git
$ git worktree list                           -> single worktree
$ git log -1 --format='%an <%ae>'             -> protocol-shokunin <protocol@shokunin.local>
```

The local identity already matches the lane invariant `<id>-shokunin <<id>@shokunin.local>`. The last commit is an integration commit authored by `protocol-shokunin`, which is consistent with "the parent integrates" — no lane-produced commit is in question here.

### F7. Hooks, attributes, filters, eol: nothing to bypass today

```
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample' -printf '%f\n'   -> (empty)
$ ls .git/hooks | wc -l                                                  -> 14   (all *.sample)
$ git config --get core.hooksPath                                        -> rc=1 (unset)
$ find . -path ./.git -prune -o -name '.gitattributes' -print            -> (empty)
$ ls .git/info/                                                          -> exclude only (default comments)
$ git check-attr -a -- LOG.md grader.py                                  -> (no output, exit 0)
$ git config --global --get core.autocrlf ; ... core.eol                 -> (unset)
$ git config --global --get-regexp 'filter\.'                            -> filter.lfs.clean/smudge/process/required
$ ls .gitmodules ; git config --get-regexp '^submodule'                  -> absent / none
```

`filter.lfs.*` is configured globally but **no path assigns `filter=lfs`**, and `check-attr` confirms no attribute applies, so no clean/smudge runs today. `core.hooksPath` is unset and the hooks directory is 100% samples. jj bypasses hooks and attributes; in this lane that bypass currently discards nothing.

`.gitignore` is `.ufo/interactive-sessions/` and `__pycache__/`. There is no `.ufo/state/` directory in this lane (`ls -d .ufo/state` → absent), so the "`.ufo/state` never committed" invariant has no bytes at risk here; it is also enforced independently by `jj-lane.sh` path rejection.

## 2. Classified table — executable call sites

| # | file:line | exact command | class | risk under jj colocation (HEAD may be detached; jj owns the index) | jj-safe replacement |
|---|---|---|---|---|---|
| G1 | `plans/round24_census.sh:8` | `git rev-parse --short HEAD 2>/dev/null \|\| echo n/a` | **D** | **MEDIUM (semantic).** Resolves, but names `@-`: after a jj commit that is a commit on no bookmark (sandbox: `HEAD 9924aff` vs `master ae2598f`); with a dirty `@` it names a commit that does **not** contain the bytes being counted. The `\|\| echo n/a` fallback covers "not a repo", never "detached". Captured `after.txt` already leans on this line as a provenance claim (`HEAD 94da19e`). | `echo "HEAD $(git rev-parse --short refs/heads/master \|\| echo n/a)"` (bookmark→git ref export verified) plus a working-copy marker, e.g. `echo "WC $(jj --ignore-working-copy log -r @ --no-graph -T 'commit_id.short()' 2>/dev/null \|\| echo n/a)"`. |
| G2 | `corpus/evidence/round13-coverage/coverage_census.py:65-66` | `git -C <lane> rev-parse --verify --quiet <REV>^{commit}` | **D** | **LOW–MEDIUM (latent).** Explicit 40-hex hashes (the recorded `99cf615`) are unaffected. `--revision HEAD` resolves to the detached jj commit / `@-` and is then reported as the census `revision` with no branch-reachability check. | Resolve a bookmark explicitly (`--revision master`), or reject the literal `HEAD` with a message naming `master`/`@`; or accept `@` and map it through `jj log -r @ -T commit_id`. |
| G3 | `corpus/evidence/round13-coverage/coverage_census.py:79` | `git -C <lane> ls-tree -z <commit>:<rel>` | **D** | **NONE.** Commit-pinned tree read; jj exports commit objects to git (sandbox: `ls-tree -r ae2598f` works post-colocation). No index or HEAD dependency. | None. Keep `<commit>` fully resolved (as today via :65). |
| G4 | `corpus/evidence/round13-coverage/coverage_census.py:110` | `git -C <lane> show <commit>:<rel>` | **D** | **NONE.** Same as G3 (sandbox: `show ae2598f:LOG.md` → `seed`). | None. |

Spawn primitive: `coverage_census.py:45` (`subprocess.run(("git", "-C", repo) + args)`) is the single transport for G2–G4; it is not an extra command site.

## 3. Counts per class

Executable call sites (total 4):

| class | count | sites |
|---|---|---|
| A — attached HEAD / upstream assumed | **0** | — |
| B — history / index / tree mutation | **0** | — |
| C — index / staging read | **0** | — |
| D — read-only, HEAD-commit based | **4** | G1 (census.sh) + G2–G4 (coverage_census.py) |

Documented, hand-run commands (total 9): A 0 · B 0 · C 0 · **D 9** (table §4). Historical prose mention of `git add` (§F4) is not a command invocation and is not counted.

## 4. Documented (non-executable) commands

| # | file:line | command | class | jj risk | jj-safe replacement |
|---|---|---|---|---|---|
| D1 | `plans/round24_census.sh:6` (comment) | `git archive 99cf615 \| tar -x -C /tmp/k24base` | D | None — commit object exists in a colocated repo; archive verified in sandbox. | None. |
| D2 | `plans/round-24-claims.md:91` | `git diff --diff-filter=D --name-only 99cf615 -- corpus/knowledge` | D | None — hash-pinned diff. | None. |
| D3 | `plans/round-24-claims.md:105` | `git archive 99cf615` | D | None. | None. |
| D4 | `SCORECARD.md:40` | `git show --stat` (round-9 commit) | D | LOW — no rev pinned; under jj it shows `HEAD` (= `@-`). Historical prose, not a rerun procedure. | Pin the hash if ever re-run: `git show --stat <round9-sha>`. |
| D5 | `SCORECARD.md:61` | `git ls-tree -r f147a27 --name-only \| grep -c SCORECARD` | D | None — hash-pinned. | None. |
| D6 | `SCORECARD.md:64` | `git ls-tree -r f147a27 --name-only \| grep -cE '\.(py\|sh)$'` | D | None. | None. |
| D7 | `SCORECARD.md:90` | `git ls-tree -r 2575be6 --name-only \| grep -cE ...` | D | None. | None. |
| D8 | `SCORECARD.md:287` | `git ls-tree -r f147a27 --name-only \| grep -c evidence` | D | None. | None. |
| D9 | `LOG.md:120` | `git -C ../ log --oneline` | D | LOW — shows the jj-exported graph including `@`/`@-` commits; used as historical merge evidence only. | `git -C ../ log --oneline --branches` if a branch-only view is wanted. |

## 5. This lane's top three risks

1. **`HEAD` as a provenance label (`plans/round24_census.sh:8`) — active on the next colocated run.** The census prints a commit id that, under jj, can be a commit reachable from no bookmark and can exclude the working-copy bytes it just measured. The captured `after.txt` already treats the line as "the commit this tree corresponds to"; one `jj commit`/`jj new` breaks that equivalence silently, because the `2>/dev/null || echo n/a` fallback only triggers outside a repo. Sandbox proof: `HEAD 9924aff` / `master ae2598f` / ` M LOG.md`.
2. **`--revision HEAD` on the registry-declared `coverage-census` interface.** The probe accepts any rev, resolves it, and stamps it as the census `revision`. Under jj, `HEAD` resolves to the detached `@-` or `@`, so a future seat typing the obvious `--revision HEAD` records a revision that no bookmark contains. All recorded evidence uses `99cf615`, so nothing stored is wrong today; this is a latent interface trap, not a current defect.
3. **Silent loss of `git add` staging.** This is the lane's one documented history-mutating habit (`considerthese/2026-10-19.md:62`: an r20 backfill broken by a `git add` pathspec). In a colocated repo the staged entry survives a bare `jj st` but is cleared by the next working-copy update (`jj new`, `jj commit`), with no error. A seat following old text would believe a path was staged when it is not; kengaku has no in-repo staging checks, so nothing would catch it.

Residual (not top three): jj bypasses hooks and attributes. Today the lane has zero active hooks, zero attributes and no active filters (F7), so the bypass costs nothing; if a commit-msg hook or LFS attribute is ever added to this lane, jj commits would silently skip it.

## 6. Invariant check against the wave's protocol list

| invariant | lane evidence | status |
|---|---|---|
| landed = committed AND pushed before a report cites the hash | no push/commit call in any in-scope file; lane protocol defers integration to the parent (`probe-battery-TEMPLATE.md:70`) | [INFERENCE] holds by absence: the lane cannot claim a hash it pushed itself; enforcement lives in the fleet helper, out of this seat's scope |
| cited hash stays an ancestor (no amend/rewrite) | no `rebase`/`commit --amend`/`reset` anywhere; all 13 sites are reads | holds |
| lane identity `<id>-shokunin <<id>@shokunin.local>` | repo-local `user.name=kengaku-shokunin`, `user.email=kengaku@shokunin.local`; helper sets the same pair | holds today |
| commits pathspec-limited | no commit invocation in lane tooling | N/A (helper's job) |
| `LOG.md` append-only | census and grader read `LOG.md`; no write path in scope | holds |
| `.ufo/state/` never committed | `.ufo/state` absent; `.gitignore` does not list it, but helper rejects `.ufo/state/*` paths and `auto-track="none()"` means no implicit tracking | holds, with a documentation gap (the lane's own `.gitignore` would not stop a hand `git add .ufo/state`) |

## 7. [INFERENCE]

- `git diff --diff-filter=D 99cf615 -- corpus/knowledge` and the `ls-tree` sites remain valid under colocation because jj preserves the imported commit objects and exports new commits on every operation; only sandbox equivalents (`diff`, `ls-tree`, `show`, `archive` against `ae2598f`) were executed, and no live-repo jj command was run.
- The helper's bookmark move + push (out of scope) would leave `refs/heads/master` equal to the pushed tip; I verified only that `jj bookmark set` exports to `refs/heads/master` immediately, not the push path.
- If the lane is colocated with `snapshot.auto-track="none()"`, untracked scratch under the lane cannot enter `@`; if init is ever skipped or a lane is colocated by hand with defaults, the helper's own init comment records that every untracked file gets tracked. Not exercised here.

## 8. Recommendations

1. Replace `plans/round24_census.sh:8` with a branch-pinned label plus an explicit working-copy marker (G1). One line; keeps `n/a` for non-repo trees.
2. In `plans/round-24-claims.md` and the probe-battery text, state that `coverage_census.py --revision` takes a 40-hex commit or `master`, never `HEAD`; optionally harden the probe to reject `HEAD`. No change is needed for the stored `99cf615` evidence.
3. Do not introduce `git add` into any lane workflow after colocation. If a staging assertion is ever needed, assert `jj diff -r @ --summary`, not `git diff --cached`.
4. Before colocating this lane, confirm `.ufo/state/` is absent (it is) and keep the helper's `auto-track="none()"` init; if the lane ever grows a hook or `.gitattributes`, treat it as a jj bypass and enforce the same rule in the helper.
5. The two grep hits in `corpus/evidence/round11-fleet/mutate_r11.sh` (`git status --porcelain`) are out of scope and are not gate entries; if that artifact is ever re-run under colocation, its before/after status comparison is not a staged-state oracle.

## 9. Verification gaps

- No live-repo jj command was run (prohibited); all jj behaviour above is sandbox evidence at jj 0.45.1, git 2.56.0.
- The helper's commit/push/retry logic is another seat's scope; this audit covers only call sites reachable from kengaku's own files and from the two SKILL-registered entries.
- `corpus/evidence/*.sh|*.py` outside `round13-coverage/` were sampled only by the repo-wide grep (two `git status` hits in `mutate_r11.sh`); they are excluded by the task's corpus skip.
- No hook/attribute runtime was exercised because none exists in this lane (`check-attr` empty; hooks all samples).

## 10. Sandbox reproduction

```
mkdir -p /fast/scratch/jj-wave/<seat> && cd /fast/scratch/jj-wave/<seat>
git init -q --bare origin.git && git clone -q origin.git work && cd work
git config user.name kengaku-shokunin && git config user.email kengaku@shokunin.local
echo seed > LOG.md && git add LOG.md && git commit -qm seed && git push -q origin master
git remote -v                                  # confirm local bare before any push
jj --config 'snapshot.auto-track="none()"' git init --colocate .
jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
jj --ignore-working-copy config set --repo user.name  kengaku-shokunin
jj --ignore-working-copy config set --repo user.email kengaku@shokunin.local
jj --ignore-working-copy config set --repo 'revset-aliases."trunk()"' '"master@origin"'
jj --ignore-working-copy bookmark track master@origin
printf 'x\n' >> LOG.md && jj commit -m c1 -- LOG.md
git symbolic-ref -q --short HEAD || echo DETACHED   # DETACHED
git rev-parse --short HEAD; git rev-parse --short master
```

Sandbox removed after writing this report; every excerpt above is quoted verbatim from its run.
