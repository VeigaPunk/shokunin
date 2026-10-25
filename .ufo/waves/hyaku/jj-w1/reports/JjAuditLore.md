# JjAuditLore — lane `lore` git invocations under jj colocation

Seat: `JjAuditLore-2` · repo `/home/vgpnk/Projects/shokunin/lore-shokunin` · branch `main` ·
HEAD `01306d51252f837909af5252c398ee4e31259f9b` · jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` ·
lane currently has **no `.jj`** (`ls -d .jj` → absent), so this is the pre-colocation code surface audited
against sandbox replicas. Read-only against the lane: `cat/grep/find`, `git log|show|ls-files|rev-parse|status|diff|cat-file|merge-base|check-attr|check-ignore`,
`git clone`. No `jj` ever ran in the live repo (hard rule). All jj probes ran in
`/fast/scratch/jj-wave/JjAuditLore-2/` with `origin` a sandbox bare repo.

## Scope actually present (the assignment's layout does not exist in this lane)

`tools/`, `scripts/` and `verifiers/` **do not exist** in `lore-shokunin`; there is no root-level
`*.sh/*.py/*.mjs/*.js/Makefile` either:

```
$ for d in tools scripts verifiers; do ls -la "$d"; done
== tools ==   MISSING
== scripts == MISSING
== verifiers == MISSING
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \) -print
(no output)
$ find . -path ./.git -prune -o -type f \( -name '*.mjs' -o -name '*.js' -o -name 'Makefile' -o -name '*.mk' \) -print
(no output)
```

The lane's real executable tooling, audited here as the equivalent surface:

| Surface | Tracked? | Notes |
|---|---|---|
| `corpus/tools/{boundary_doc_check,dependency_freeze,discriminate_check,map_obligations,support_check}.py` | yes | all five SKILL.md gates |
| `corpus/fixtures/check_bible.py` | yes | gate named in SKILL.md decision table; **zero** git/subprocess calls |
| `reports/round-1/measure_preservation.py` | yes | measurement script, not a gate |
| `v05-self-test-scratch/*.sh`, `*/corpus/tools/dependency_freeze.py` | no — ignored by `.gitignore:4 *-self-test-*/` | root-adjacent selftest harnesses |
| `.scratch/{V02,v26}/**` | no — untracked (`git status` → `?? .scratch/`) | copied baselines |

Enumeration was exhaustive, not sampled:

```
grep -rn -E '(["\x27]git["\x27]|(^|[ ;|&(])git +[a-z-])' --include='*.py' --include='*.sh' \
  --include='*.mjs' --include='*.js' --include='Makefile' . --exclude-dir=.git --exclude-dir=.ufo
```

That returns **23** call sites; the same sweep found **zero** `shell=True`, `os.system`, `os.popen`,
`GIT_*` environment plumbing, and zero `execFile/spawn` JS/Node callers. `git` is never invoked through a shell
string, so every site is a literal argv list and cannot be redirected by an alias or `GIT_DIR`.

## Findings (observed; command + excerpt)

### F1. The live, tracked surface is seven git calls, all class D — no A, B, or C

| file:line | exact command | class | risk under jj (HEAD may be detached; jj owns the index) | jj-safe replacement |
|---|---|---|---|---|
| `corpus/tools/boundary_doc_check.py:416` | `git show <legacy_baseline_revision>:corpus/fixtures/check_bible.py` (cwd=repo root) | **D** | none observed. Reads a git object by full 40-hex SHA (`5eb9451b…`); detached HEAD irrelevant. | keep; optionally pre-resolve `git rev-parse --verify <rev>^{commit}` once and reuse the SHA |
| `corpus/tools/boundary_doc_check.py:495` | `git show <revision>:<path>` | **D** | none observed; callers pass contract revisions (full SHAs) and self-test fixture paths. | keep |
| `corpus/tools/boundary_doc_check.py:527` | `git ls-tree -r --name-only <revision> -- <fixture_paths>` | **D** | none observed; explicit revision, object read. | keep |
| `corpus/tools/dependency_freeze.py:429` | `git rev-parse HEAD` | **D** (rev only) | **medium, semantic**: after jj snapshots, `HEAD` names `@-` (the working-copy parent), not the bytes being digested. `--freeze` therefore writes a revision label that does not contain the pinned content (F5). | record `HEAD` only when the pinned bytes equal `HEAD:<path>` (see Recommendations), else `unversioned`/`dirty@<sha>`; or add an explicit `--revision` input |
| `corpus/tools/discriminate_check.py:47` | `git show e97613cc…:corpus/fixtures/check_bible.py` | **D** | none observed; constant full SHA, object read. | keep |
| `reports/round-1/measure_preservation.py:16` | `git rev-parse --verify <arg>^{commit}` | **D** | low: caller-supplied revision. `HEAD` now resolves to `@-`; a jj change id (e.g. `usmrvsov`) is not a git object and would raise `CalledProcessError` (`check=True`). | document "pass a git SHA or bookmark name"; resolve and validate before use |
| `reports/round-1/measure_preservation.py:20` | `git archive <commit> corpus` | **D** | none observed for exported/committed revisions; `git rev-parse` above already normalized the input. | keep |

`dependency_freeze.py:429` sits inside `freeze()` only; the gate's normal **verify** mode (the SKILL.md entry
command) makes **no git call at all** — it is a digest comparison. `map_obligations.py` and `support_check.py`
have no git calls (their subprocess use is `sys.executable` self-test re-entry and `grep -nF`).

### F2. The scratch surface adds sixteen more D sites, all copies of the same two calls

| file:line | exact command | class | risk under jj | jj-safe replacement |
|---|---|---|---|---|
| `v05-self-test-scratch/c1probe.sh:17` | `git -C /home/…/lore-shokunin show 9a3d648:corpus/tools/dependency_freeze.py` | D | none (object read by SHA) | keep |
| `v05-self-test-scratch/c1probe.sh:18` | `git -C … show 9a3d648:corpus/tools/dependency-freeze-contract.json` | D | none | keep |
| `v05-self-test-scratch/c1probe2.sh:17,18` | same two commands (`9a3d648`) | D | none | keep |
| `v05-self-test-scratch/poll.sh:18` | `git diff --quiet 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` | D | low: diffs the named commit against the working tree, which under jj is `@`; still reports "diff" while the edit is uncommitted, so the poll's meaning is unchanged | keep; compare against `refs/heads/main` if the intent ever becomes "committed?" |
| `v05-self-test-scratch/{c1probe,c1probe2}/{legacypin-now,selfneutral-now}/corpus/tools/dependency_freeze.py:379` (4 files) | `git rev-parse HEAD` | D | medium (same label defect as F1), but each runs in a non-git mirror root, where git exits 128 and `freeze()` degrades to `"unversioned"` | if ever promoted, apply the F1 clean-tree guard |
| `v05-self-test-scratch/{c1probe,c1probe2}/{legacypin-9a3d648,selfneutral-9a3d648}/corpus/tools/dependency_freeze.py:365` (4 files) | `git rev-parse HEAD` | D | same as above | same |
| `v05-self-test-scratch/redemo/corpus/tools/dependency_freeze.py:379` | `git rev-parse HEAD` | D | same as above | same |
| `.scratch/V02/scratch-root/corpus/tools/dependency_freeze.py:429` | `git rev-parse HEAD` | D | same as above | same |
| `.scratch/v26/scratch-root/corpus/tools/dependency_freeze.py:429` | `git rev-parse HEAD` | D | same as above | same |

These are stale copies (sha256 `b06275f3…` for the `9a3d648` baselines, `03d04365…` for the older `now`
copies, `60a78bc3…` for the current copies; the live tool is `60a78bc3…`). They are not shipped. Their only
bearing on the jj move is that the mirrored roots are **not git repos**, so `git rev-parse HEAD` exits 128,
`freeze()` catches it (`if result.returncode == 0`) and records `"unversioned"` — i.e. the mirrors never
exercise the HEAD path, and the only live exercise of it is the real lane repo.

### F3. Under colocation, HEAD is `@-` and detaches at the first `jj commit`; the branch bookmark is a separate ref

Measured in `/fast/scratch/jj-wave/JjAuditLore-2/probe2.sh` (fresh repo, sandbox `origin`, helper-equivalent
init: `jj --config 'snapshot.auto-track="none()"' git init --colocate .` + repo configs + `bookmark track main@origin`):

```
-- T1 after jj colocate      symbolic-ref: refs/heads/main  HEAD: 471306ce…  main: 471306ce…
-- T3 after jj st (snapshot) symbolic-ref: refs/heads/main  HEAD: 471306ce…  (HEAD = @-, the unchanged branch tip)
-- T5 after jj commit        symbolic-ref: detached         HEAD: f29aab7e…  main: 471306ce…
-- T6 after jj bookmark set  symbolic-ref: detached         HEAD: f29aab7e…  main: f29aab7e…
-- T7 after jj git push      symbolic-ref: detached         HEAD: f29aab7e…  main: f29aab7e…
```

Before the first commit, `git rev-parse HEAD` equals the branch tip and `git rev-parse main` succeeds. After the
helper's `jj commit`, `symbolic-ref -q HEAD` fails, `git rev-parse --abbrev-ref HEAD` prints `HEAD`, and
`git rev-parse HEAD` = `@-` = the pushed hash; `refs/heads/main` is the same commit only after `bookmark set`.
Consequences for this lane: every D call reads objects by SHA and is unaffected; **no in-scope code uses
`symbolic-ref`, `@{u}`, `--abbrev-ref HEAD` or `branch --show-current`** (grep below), so class A is not just
survived, it is absent.

```
$ grep -rn -E 'symbolic-ref|@\{u\}|--abbrev-ref|show-current|rev-parse +HEAD' \
    --include='*.py' --include='*.sh' --include='*.mjs' --include='*.js' --include='Makefile' \
    . --exclude-dir=.git --exclude-dir=.ufo
(no output)          # rev-parse HEAD is matched by the wider literal-git sweep, classed D in F1
```

The one place `HEAD` is *named* (not used as a branch) is `dependency_freeze.py:429`, classed D by the
assignment's taxonomy.

### F4. jj does clear the git index — but only for some operations, and this lane has no class C caller

`.git/index` is not read by any in-scope file (`grep -rn -E 'diff --cached|ls-files -[sS]|update-index'` over
`*.py/*.sh` → no output), so this is latent risk only. The per-operation matrix from
`/fast/scratch/jj-wave/JjAuditLore-2/probe3.sh` (each row: stage `a.txt`, run one op, read `git diff --cached`):

```
jj st                              staged[a.txt ]->[a.txt ] head[refs/heads/main]->[refs/heads/main]
jj log --ignore-wc                 staged[a.txt ]->[a.txt ] head[refs/heads/main]->[refs/heads/main]
jj describe -m                     staged[a.txt ]->[]       head[refs/heads/main]->[refs/heads/main]
jj metaedit --update-author        staged[a.txt ]->[]       head[refs/heads/main]->[refs/heads/main]
jj commit -- a.txt                 staged[a.txt ]->[]       head[refs/heads/main]->[detached]
jj bookmark set                    staged[a.txt ]->[]       head[refs/heads/main]->[detached]
jj new                             staged[a.txt ]->[]       head[refs/heads/main]->[detached]
jj git export                      staged[a.txt ]->[a.txt ] head[refs/heads/main]->[refs/heads/main]
```

`jj st`, `--ignore-working-copy` reads, and `jj git export` preserved staged entries; `describe`, `metaedit`,
`commit`, `bookmark set`, `new` cleared them. The workable rule for future tooling: **the git index is not
durable in a colocated repo; never stage and expect a later jj command to leave it staged.**

The related snapshot pathology is real and is already handled by the helper's init: with jj's default
auto-track, an untracked file becomes an intent-to-add entry in git's index at the next snapshot; with
`snapshot.auto-track="none()"` it stays untracked. Observed in the same probe:

```
== auto-track none: untracked file behavior ==
-- status: M  corpus/a.txt|?? corpus/c.txt|
== default auto-track (control): untracked file behavior ==
-- status:  A corpus/c.txt|
-- ls-files -s corpus/c.txt: 100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	corpus/c.txt
```

(`e69de29…` is the empty blob, i.e. an intent-to-add index entry that git would render as ` A`.)

### F5. `dependency_freeze --freeze` writes a revision label that can name bytes other than the pin

`freeze()` at `corpus/tools/dependency_freeze.py:427-451` sets both `pins[<name>]["revision"]` and the top-level
`contract["revision"]` from `git rev-parse HEAD`. In a colocated repo `HEAD` is `@-`, while the digests come from
the working tree. Reproduced on a sandbox clone (`/fast/scratch/jj-wave/JjAuditLore-2/probe4.sh` section E:
one line appended to `corpus/fixtures/r99-window-lapse/README.md`, no commit):

```
worktree README sha: 42b793f116932c25141ba6ac2aa9cdd85006cc208760e7a2021acff7a0dcfbcd
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 84f051be02bb2a30a85d0795901a246a3b33dc353d5022aee06ee89157df96a2
RESULT PASS
pin.revision = 85ae25cb536f71d90366bdfada1102c2f4b15aef
pin.files README sha = 42b793f116932c25141ba6ac2aa9cdd85006cc208760e7a2021acff7a0dcfbcd
contract.revision = 85ae25cb536f71d90366bdfada1102c2f4b15aef
git rev-parse HEAD = 85ae25cb536f71d90366bdfada1102c2f4b15aef
pin revision blob  = b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049
git rev-parse main = 85ae25cb536f71d90366bdfada1102c2f4b15aef
```

The pin's `README.md` digest is `42b793…` (dirty worktree) while `git show <pin.revision>:…README.md` is
`b93209…`. The gate still verifies (it compares bytes and digests, never the label): nothing in the file reads
`pin["revision"]` back — `grep -n revision corpus/tools/dependency_freeze.py` shows writes at 427/431/440/451
and no read — so the defect is a provenance-record defect, not a verdict defect. It is worth noting this is
identical in plain git with a dirty tree; what jj adds is that *every uncommitted round edit* is in this state
(the working copy commit `@` exists and is not `HEAD`), so a `--freeze` run at integration time will
systematically record the previous commit.

When the tree is clean, the label is correct: after the helper-style commit, `git status --porcelain` is empty
and `git show HEAD:a.txt` equals the worktree content (probe2 T6/T7); `git diff --quiet HEAD -- a.txt` returns 0.

### F6. All named gates still evaluate in a colocated clone — before and after HEAD detaches

Sandbox clone of this lane (`git clone --no-hardlinks`, `origin` re-pointed at a sandbox bare:
`origin /fast/scratch/jj-wave/JjAuditLore-2/origin-mirror.git`), helper-equivalent colocation, then the exact
SKILL.md entry commands:

| gate | plain git | after colocation, HEAD attached | after helper-style commit, HEAD **detached** |
|---|---|---|---|
| `boundary_doc_check.py` | exit 0, `CERTIFIED` | exit 0, `CERTIFIED` | exit 0, `CERTIFIED` |
| `discriminate_check.py` | exit 0, `DISCRIMINATION HELD` | exit 0, `DISCRIMINATION HELD` | exit 0, `DISCRIMINATION HELD` |
| `dependency_freeze.py r97-crossing-acknowledgment` | exit 0, `RESULT PASS` | exit 0, `RESULT PASS` | exit 2 `DIGEST-MISMATCH` — **only because the probe edited a pinned README**, expected gate behavior, not a git defect |

```
=== C. same gates, colocated, HEAD attached ===
boundary exit=0        CERTIFIED (bounded: …)
discriminate exit=0    RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
dependency exit=0      RESULT PASS
=== D. helper-style commit detaches HEAD, then gates again ===
symbolic-ref: detached
HEAD:         85ae25cb536f71d90366bdfada1102c2f4b15aef
main:         85ae25cb536f71d90366bdfada1102c2f4b15aef
boundary exit=0        CERTIFIED (bounded: …)
discriminate exit=0    RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
```

The `boundary_doc_check` default path is the only gate that touches git on every run (site 416, the legacy
baseline `git show`); its `--self-test` adds sites 495 (`git show` of the committed document/checker/fixtures)
and 527 (`git ls-tree`). It is unaffected by detachment because every revision comes from
`corpus/tools/boundary-doc-contract.json` as a full SHA.

### F7. Every revision these gates pin is a reachable ancestor of `main` (so jj export/GC cannot strand them)

```
$ for r in 65838f86… 5eb9451b… 337f0fa5… b5fe4729… ebec6bbd… e97613cc… 9a3d648; do
    git merge-base --is-ancestor "$r" main && echo "$r yes"; done
65838f867d6ece8e7b8bdcc4ffc667a08a1b785e yes   # boundary document + checker pin
5eb9451baff217c19d5786405f9b2aa500b7c1b7 yes   # legacy checker pin
337f0fa52b02626b7687eedbb2d99fab30446fe4 yes   # dependency pins r88/r94/r95/r96/r97/r98
b5fe472957ab1e4e9c90f5613acc14cd24a288ae yes   # r99
ebec6bbdeb1d919c9eb19e7fdd5b9c6dd14db026 yes   # r100
e97613cc276f5fa9cac49ff1900798cf6863c020 yes   # discriminate BASELINE
9a3d648                                   yes  # scratch selftest baseline
```

A jj-created commit is written into `.git/objects` immediately even before any export — observed
`git cat-file -t 883a510751b0…` (`@` right after `jj st`) → `commit` — so a pin taken from `@` would resolve
locally but would be absent on a fresh clone/peer until the bookmark is pushed. Current pins are all on `main`,
so this is a forward hazard, not a present one.

### F8. Hooks and attributes: nothing is in use, so jj's bypass costs nothing today

```
$ ls .git/hooks | grep -v '\.sample$' | wc -l
0                                   # 14 files, all *.sample
$ git config --get core.hooksPath
(unset)                             # also unset in ~/.gitconfig
$ find . -path ./.git -prune -o -name .gitattributes -print
(no output)
$ cat .git/info/attributes
absent
$ git config --global --get core.attributesFile ; git config --global --get core.autocrlf ; git config --global --get core.eol
(unset) (unset) (unset)
$ ls ~/.config/git/attributes
no ~/.config/git/attributes
$ git check-attr -a -- corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment/README.md
(no output)
```

- **Hooks:** no active hook and no `core.hooksPath`. jj never runs git hooks, so the only lost control would be
  hypothetical future hooks; today none exist. The lane's actual write path is the helper's own
  commit→bookmark→push sequence, not hooks, so "landed = committed and pushed" is unaffected.
- **Attributes/filters/eol:** no `.gitattributes` anywhere, no info attributes, no global attributes file, no
  `core.autocrlf/eol`. `~/.gitconfig` *defines* `filter "lfs"` (`clean`/`smudge`/`process`, `required = true`),
  but no attribute references it, so it never fires. If a future `.gitattributes` adds `filter=lfs` or
  `eol=crlf`, jj will not run those filters — that is the one standing hazard in this section.
- Also git-only in the global config and therefore ignored by jj: `pull.rebase=true`, `push.autoSetupRemote=true`,
  `rerere.enabled=true`/`autoupdate=true`. No in-scope code pulls, merges or pushes, so no effect.

## Counts per class

| class | live tracked tooling (7 sites) | root scratch + copies (16 sites) | total |
|---|---|---|---|
| **A** — attached HEAD / upstream (`symbolic-ref`, `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`, HEAD-as-branch) | 0 | 0 | **0** |
| **B** — history/index/worktree mutation (`add`, `commit`, `stash`, `checkout`, `reset`, `rebase`, `push`, `pull`, `merge`, `clean`, `tag`) | 0 | 0 | **0** |
| **C** — index/staging read (`diff --cached`, `ls-files -s`, `update-index`) | 0 | 0 | **0** |
| **D** — read-only, HEAD-commit based (`log`, `show`, `rev-parse HEAD`, `diff <rev>`, plain `ls-files`) | 7 | 16 | **23** |

Breakdown of the 23: `git show` ×7 (2 boundary + 1 discriminate live, 4 in the two scratch selftest shell
scripts), `git ls-tree` ×1, `git rev-parse` ×13 (2 live: `dependency_freeze` HEAD and `measure_preservation`
`--verify`; 9 stale copies under `v05-self-test-scratch`, 2 under `.scratch`), `git archive` ×1, and
`git diff --quiet <sha>` ×1 (scratch poll).

## Top three risks for this lane

1. **The freeze label lies as a matter of course (`corpus/tools/dependency_freeze.py:429`).** Under jj, after the
   first helper commit, `HEAD` is `@-` forever; any edit made after that lives in `@` while the gate digests the
   working tree. `--freeze` will therefore record the *previous* commit alongside bytes that are not in it
   (observed: pin revision `85ae25cb`, README digest `42b793…`, `git show 85ae25cb:…README.md` → `b93209…`).
   No gate reads the field, so verdicts stay correct; but any report or hand-off that cites the pin revision as
   "the commit these pins were taken at" is wrong. Plain git has the same dirty-tree gap, but there a commit
   moves `HEAD` onto the bytes; under jj `HEAD` stays at `@-` through every edit window, and the commit that
   holds the edits is `@`, which `HEAD` never names without the helper's bookmark move.
2. **The class-A/class-C immunity is a property of today's code, not an enforced invariant.** Detached HEAD at
   `@-` and the index-clearing matrix (F4) will silently break the first future convenience edit that adds
   `git symbolic-ref`, `@{u}`, `git diff --cached` or `git add`. Nothing in the lane tests for that; the gate
   suite only exercises the current literal argv lists. A one-line guard in the existing self-tests (scan
   `corpus/tools/*.py` for those tokens and fail) would keep the property from being lost by accident.
3. **A pin taken from a jj working-copy commit is locally valid and remotely absent.** jj writes `@` into
   `.git/objects` immediately (`git cat-file -t <@>` → `commit`), so `git show <@>:path` works in the lane and
   would make a self-test pass — but a fresh clone, a peer seat or a CI checkout will not have that object until
   the bookmark is pushed. Today all seven pinned revisions are ancestors of `main` (verified above), so the
   invariant holds by luck of process, not by check. Enforce `git merge-base --is-ancestor <pin> main` (or
   `git branch -r --contains <pin>`) wherever a revision is written into a contract.

## [INFERENCE]

- `[INFERENCE]` jj's GC (`jj util gc`, and any git `gc --prune` after the 90-day/default grace) can only strand
  revisions that are unreachable; since all current pins are ancestors of `main`, none is at risk. The forward
  risk in F7/Top-3 #3 is about *unpushed* `@` commits, not about exported history.
- `[INFERENCE]` `git rev-parse HEAD` in `freeze()` would return the correct commit if `--freeze` were run only
  after the helper committed and with a clean `@`. I did not isolate that positive case through `--freeze`; the
  equivalent clean-tree state was verified at the git level (probe2 T6/T7: `git status --porcelain` empty,
  `git diff --quiet HEAD -- a.txt` rc=0, `git show HEAD:a.txt` = worktree).
- `[INFERENCE]` The `measure_preservation.py` failure mode for non-git revisions is an uncaught
  `CalledProcessError` (`check=True`), i.e. a traceback rather than a usage error; callers must pass git SHAs or
  bookmark names (`main` survives because jj exports bookmarks; `@` does not mean anything to git unless the
  helper has committed it).
- `[INFERENCE]` Because every in-scope git call is a literal argv list with no shell and no `GIT_*` env, jj's
  takeover of commits cannot change *which* command runs; only the repository state those commands observe
  changes (F3–F5).

## Recommendations (advisory — no lane file was edited)

1. In `dependency_freeze.freeze()` (`corpus/tools/dependency_freeze.py:427-451`): after building
   `observed["files"]`, record `HEAD` only if, for every pinned file, `git cat-file blob HEAD:<path>` matches the
   bytes just digested; otherwise write `"unversioned"` (or `dirty@<short>`). This is jj-agnostic, keeps the
   contract honest with a dirty tree in plain git too, and works with detached HEAD.
2. Add a cheap guard to an existing self-test: fail if any `corpus/tools/*.py` or `reports/**/*.py` contains
   `symbolic-ref`, `@{u}`, `--abbrev-ref`, `branch --show-current`, `diff --cached`, `ls-files -s`,
   `update-index`, or a git verb from class B. It encodes the current safe shape before jj makes the first
   accidental addition fail in the field.
3. Wherever a contract revision is written (`dependency_doc_check` pins, `dependency_freeze --freeze`), assert
   `git merge-base --is-ancestor <rev> <branch>` before persisting; reject a revision that is only in the local
   object store. This makes "a cited hash is reproducible from the remote" mechanical.
4. Document for future lane tooling: in a colocated repo `HEAD` = `@-`, `refs/heads/<branch>` is the exported
   bookmark, and the git index is not durable. Prefer explicit `git rev-parse --verify <rev>^{commit}` and
   object reads (`show`/`ls-tree`/`archive`); never stage.
5. If the fleet ever adds `.gitattributes` (LFS, eol) or hooks to lane repos, treat them as *not* enforced under
   jj; move any invariant they encode into the helper or the gates, where it runs on both paths.

## Verification gaps (unrun checks have not passed)

- The live lane repo was not executed: `dependency_freeze.py --self-test` and `map_obligations.py --self-test`
  create their scratch dir at the repository root (`tempfile.TemporaryDirectory(..., dir=ROOT)`), which would be
  a write in a live repo. I did not run them there; I ran the read-only gate paths in a sandbox clone instead.
- `boundary_doc_check.py --self-test` was not run at all (its self-test reads `git_blob` from the repo and
  writes only to the system temp dir; I verified the mechanism statically and ran the default path instead).
- The helper's push-rejected / rebase-retry arm was not exercised (out of scope for lane tooling; the helper was
  read, not executed, per the hard rules).
- I did not test `git worktree`, `GIT_DIR` redirection, or a repo where `main` does not exist as a local bookmark —
  `detect_branch`'s fallback chain was read but only the `main`/`origin/HEAD` path was exercised.
- jj 0.45.1 on this host only; other versions may change which operations clear the index or detach HEAD.

## Sandbox

`/fast/scratch/jj-wave/JjAuditLore-2/` is preserved because it holds the F5 failure reproduction and the gate
runs cited above: `probe.sh`, `probe2.sh`, `probe3.sh`, `probe4.sh`, `clone/` (sandbox `origin` re-pointed at
`origin-mirror.git`, so no live remote can be pushed), and the per-operation `probe3/case_*` repos. No live repo
was written; `git status` in `lore-shokunin` remains `?? .scratch/` only.
