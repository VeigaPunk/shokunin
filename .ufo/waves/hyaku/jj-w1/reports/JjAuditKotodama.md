# JjAuditKotodama — kotodama lane git invocations under jj colocation

Read-only static audit, wave jj-w1. Audit target: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
at `main @ 4ad26836552462d28a946ca3b067cab0b5ce3532` ("round-49 verifier spot-check (integrator,
kaika): non-author admit/reject sample + adjudication"), worktree clean (`git status --porcelain |
wc -l` → `0`), lane **not yet colocated** (`test -d .jj` → absent), so every jj risk below is
prospective. `jj` was never run in the lane or fleet root; all jj evidence comes from
`/fast/scratch/jj-wave/JjAuditKotodama-2/` with the host's
`jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` and `git 2.56.0`. No tool was installed or
upgraded; no live repo was written.

## Scope and method

| surface | result |
|---|---|
| `tools/` | 35 tool files (`.py`; excluding `tools/gates/expected/` and `tools/gates/frozen/` fixture trees), **3** invoke git |
| `scripts/` | **ABSENT** (`ls: cannot access 'scripts'`) |
| `verifiers/` | **ABSENT** (`ls: cannot access 'verifiers'`) |
| root `*.sh`, `*.py`, `*.mjs`, `*.js`, `Makefile` | **none** (`ls` → no such file); no root executable file (`find . -maxdepth 1 -type f -perm -u+x` → empty) |
| gates/selftests named in `SKILL.md` | 29 `tools/...` paths; every existing one is under `tools/` and covered above. `tools/gates/typed-pipelines.js` is named in `SKILL.md` but does not exist (`ls` → no such file) |
| `tools/gates/expected/`, `tools/gates/frozen/` | fixture inputs/expected outputs, not executed by lane tooling: `grep -rn '"git"'` → `0`; their 47 `git` tokens are prose in `freeze.txt`/`expected.json`/markdown |
| `tools/harness/receipt_guard_adoption.py`, `r8_checks.py`, `packet_links.py`, `packet_uncertainty.py` | no git execution (`\bgit\b` hits are path filters and limit prose) |

Search set: every file type under `tools/` (not just by extension), plus `git`-token, `subprocess`,
`os.system`, `execFile`, `spawn`, `GIT_*` sweeps. `receipt_guard.py:54` and `claims-freshness.py:128`
are single dispatchers (`["git", "--literal-pathspecs", "-C", str(root), *args]`); every call below
goes through them, with `GIT_*` scrubbed from the environment and `GIT_OPTIONAL_LOCKS=0`,
`GIT_NO_REPLACE_OBJECTS=1` set. The dispatchers are not counted as call sites.

Class definitions as assigned: **A** attached-branch/upstream assumption; **B** history/index/worktree
mutation; **C** index/staging read; **D** read-only HEAD-commit read.

## Classified table

Legend: RG = `tools/harness/receipt_guard.py`, CF = `tools/harness/claims-freshness.py`,
CR = `tools/check-readme-revisions.py`.

| file:line | exact command (after dispatcher) | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `RG:69` | `git --literal-pathspecs -C <root> rev-parse --verify --quiet HEAD^{commit}` | **D** | Resolves jj's `@-`, which is the newest *local* commit, often an empty jj working-copy-parent commit that is not on the branch/remote (observed: `HEAD f0e826a8…` = 1 commit ahead of `origin/main 4ad26836…`, same tree). Tree content is right; the identity is not landed evidence. | Keep as the tree probe only. Resolve `refs/heads/main` / `refs/remotes/origin/main` when a sha will be cited. |
| `RG:73` | `git … symbolic-ref --quiet HEAD` | **A** | Reachable only when `HEAD^{commit}` exits 1 (unborn HEAD). Under jj, detached HEAD never reaches here because `rev-parse` succeeds; a fresh colocated repo is attached+unborn and this succeeds, then the branch is used only for `show-ref` existence. Detached + failing `rev-parse` falls through to a fail-closed error, so no silent pass. | No change needed; if hardening, replace the pair with a direct `rev-parse --verify refs/heads/<branch>`. |
| `RG:76` | `git … show-ref --verify --quiet <branch>` | **A** | Branch ref name came from `HEAD`; jj exports bookmarks to `refs/heads/*` on push/import, so a pushed lane branch exists. Unborn branch → rc 1 → `_head_commit` returns `None` (allow), which is the intended pre-commit behaviour. | No change needed. |
| `RG:92` | `git … rev-parse --show-toplevel` | **D** | None: repo discovery, independent of HEAD attachment. Works in a colocated repo (observed `…/case2/lane`). | Keep. |
| `RG:129` | `git … ls-tree -z --full-tree <head> -- <relative>` | **D** | **Head-only receipt detection.** Correct only while HEAD is the branch tip. With the working copy anchored below the tip, a receipt committed on `main`/`origin/main` is invisible and the guard allows the overwrite (reproduced, R2). | Probe **all** of HEAD, `refs/heads/main`, `refs/remotes/origin/main`; refuse if the path exists in any. |
| `RG:216` | `git … rev-parse HEAD:validation.json` | **D** | Selftest fixture only; fixture HEAD is attached (`refs/heads/control`). No lane exposure. | Keep. |
| `RG:247` | `git … add -- validation.json` | **B** | Selftest fixture only. Any jj mutation resets the index (observed), but the fixture is a plain nested `.git` and no `jj` runs there. | Keep (fixture); do not lift into the lane. |
| `RG:252` | `git … add -- validation.json` | **B** | Same. | Keep (fixture). |
| `RG:260` | `git … add -- new.json` | **B** | Same. | Keep (fixture). |
| `RG:299` | `git … worktree add --detach --no-checkout <linked>` | **B** | Selftest fixture only. `git worktree add` against a jj-colocated repo was not exercised and should not be introduced into lane tooling. | Keep (fixture). |
| `CF:150` | `git … rev-parse --show-toplevel` | **D** | None. | Keep. |
| `CF:181` | `git … rev-parse --verify <rev>^{commit}` | **D** | Resolves the declared baseline (live round-49 input is a short sha `78f77a6`). Branch names also resolve; jj keeps `refs/heads/*` current on import/push. No `@{u}`/`symbolic-ref`. | Keep; pin shas, not branch names. |
| `CF:182` | `git … cat-file -t <resolved>` | **D** | None. | Keep. |
| `CF:455` | `git … rev-parse --verify <sha>^{tree}` | **D** | None (explicit commit). | Keep. |
| `CF:466` | `git … ls-tree -r -z --full-tree <commit>` | **D** | None (explicit commit). | Keep. |
| `CF:510` | `git … cat-file --batch` | **D** | None (explicit commit). | Keep. |
| `CF:2487` | `git … rev-parse HEAD` | **D** | Selftest only; under jj this is the local `@-` commit (observed 1 ahead of `origin/main`). It is stored as the fixture's `baseline_sha`, never as landed evidence. | Keep for the selftest; do not reuse this read for landings. |
| `CR:306` | `git -C <LANE> show <BASE_COMMIT>:corpus/README.md` | **D** | Explicit pin, `BASE_COMMIT = "c42d675be96b6b3957e6e5c00ab192080cb70083"` (`CR:67`). Resolves in the live repo and in the sandbox clone. Risk is object survival, not HEAD: a missing object silently SKIPs the control (R3). | Assert `git cat-file -e <sha>^{commit}` and fail (not skip) when absent. |

Counts per class (executed call sites): **A = 2, B = 4, C = 0, D = 12 — total 18**, in 3 files.
Two dispatchers make the exact command depend on arguments; the table above is exhaustive over their
callers. **No class C site exists**: nothing in lane tooling reads the index, which is why jj's
index reset does not currently break anything.

Non-executing `git` references (not rows): `receipt_guard_adoption.py:63,85,1263` (path filters and
protocol prose); `claims-freshness.py:935` (regex that classifies evidence text as destructive),
`:1312,:1487,:1503,:1506,:2522,:2589` (`evidence_command` strings stored as JSON data, never
executed — `grep` for `evidence_command` + `run/exec/subprocess/popen` → rc 1);
`receipt_guard.py:267-268,296-297,331,334,341` (env controls and synthetic fixture writes, not git
invocations).

## Top three risks

### R1 (high) — `receipt_guard` cites a jj-local commit as "committed"

Evidence, colocated clone of the live lane (`jj git init --colocate`, then `jj new`):

```
$ git rev-parse HEAD                          # f0e826a84c6cc1a7490a52d440c23be8429b8556
$ git rev-parse origin/main                   # 4ad26836552462d28a946ca3b067cab0b5ce3532
$ git rev-parse refs/heads/main               # 4ad26836552462d28a946ca3b067cab0b5ce3532
$ git rev-list --count origin/main..HEAD      # 1
$ git log -1 --format='%s|%an|%ae' HEAD       # "|JJ_EMPTY_STRING|JJ_EMPTY_STRING"
                                              #  empty local commit; jj wrote its empty-identity
                                              #  sentinel because the clone set no jj user config
$ python3 tools/harness/receipt_guard.py reports/round-49/validation.json
receipt_guard: refusing overwrite path=reports/round-49/validation.json
  committed_sha=f0e826a84c6cc1a7490a52d440c23be8429b8556
  committed_blob=bd762a89068b7f798865f37f3de1f6de22e912fd; … [RECEIPT-GUARD-COMMITTED]
```

The guard still refuses the overwrite (the tree is the same), but `committed_sha` names a commit that
is **not** on `main` or `origin/main` — under the git flow that string was the branch tip. Any receipt,
telemetry row, or report that copies this sha as "landed" violates the wave invariant *landed =
committed AND pushed before a report cites the hash*. The sha is printed on every refusal (and on
the `REFRESH_RECEIPTS=1` permit), so it is directly available to be copied into evidence; the risk is
the value's meaning. The same HEAD-based identity is used in `round_runner_main`'s two-phase recheck.

State-dependence (observed): immediately after `jj-lane.sh commit`, `git rev-parse HEAD` equals the
**pushed** tip (sandbox: `HEAD` = `origin/main` = `5c527a60771a…`), so the guard's identity is correct
in that steady state. It diverges in the state receipts are actually written in — before the helper
commit, or after any seat-run `jj new`/`jj edit` — where HEAD is a local empty commit such as
`f0e826a8…` above.

### R2 (high) — HEAD-only receipt detection has a reproduced false negative

A receipt committed and pushed on `main` is invisible when the jj working copy is anchored below the
tip. Reproduced end-to-end in the sandbox (`case6`, preserved at
`/fast/scratch/jj-wave/JjAuditKotodama-2/case6`):

```
$ git rev-parse origin/main                                   # 8020198fb233ee846ce20513f2cb6ac778f93fc0 (C2, has receipt)
$ git cat-file -e origin/main:reports/validation.json          # rc 0
$ jj new 20c3eec0eaa84f389605dc3b9d8af80fcc8473a7              # C1, pre-receipt
$ git rev-parse HEAD                                           # 20c3eec0eaa84f389605dc3b9d8af80fcc8473a7
$ python3 tools/harness/receipt_guard.py reports/validation.json \
      --repo-root /fast/scratch/jj-wave/JjAuditKotodama-2/case6/lane
$ echo $?                                                      # 0   ← allowed, no REFRESH_RECEIPTS
```

`RG:129` reads `ls-tree HEAD -- reports/validation.json`; at C1 the path is absent, so the guard
returns success and a fresh receipt may overwrite a path whose blob is already committed on the
pushed branch. Under the pre-jj flow HEAD was `main`, and the same command exits 3. The assumption
HEAD == branch tip was always implicit in the guard, but git kept it true by construction; jj makes
it routinely false (`jj new <older-change>`, `jj edit`, or an in-flight rebase before the bookmark
moves). [INFERENCE] The helper's rejected-push path rebases only unpushed commits onto the fetched
remote tip (observed in the helper run below), so its rewritten receipt tree still reports as
committed; the durable hazard is any seat anchoring work below the receipt-bearing tip.

### R3 (medium) — pinned objects fail asymmetrically: one control skips, one fails closed

`CR:306` depends on `c42d675…` resolving forever. In the sandbox, jj rewrite + `jj op abandon ..` +
`jj util gc --expire now` left the rewritten commit readable (`git cat-file -t <old>` → `commit`;
`git show <old>:pinned.txt` → `pin`), and jj writes `refs/jj/keep/<sha>` for local commits
(`git show-ref`), so the pin is durable in practice. But nothing asserts it: if the object ever goes
missing, `check-readme-revisions` prints `SKIP control: base c42d675 README flagged (r49 defect)
(base object unreachable)` and still exits 0 — `skip()` (`CR:233`) does not clear `ok`, and only
`PASS`/`FAIL` controls gate the exit. `claims-freshness` on the same condition raises `GateInputError`
and exits 2. The r49 duplicate/stub regression check is therefore the one gate that can silently
become a pass.

Related latent constraint (not a today-risk): class C is empty, and jj resets the index on every
mutation — `git diff --cached --name-only` went from `a.txt,b.txt` to empty across one `jj new`.
Any future gate that reads staged state will pass vacuously under jj.

## Hooks and `.gitattributes`

Observed in the live lane (read-only):

```
$ ls .git/hooks | grep -vc '\.sample$'                          # 0
$ find .git/hooks -type f ! -name '*.sample' -perm -u+x         # (no output)
$ git config --show-origin --get-all core.hooksPath             # rc 1 — unset at every scope
$ find . -name .gitattributes                                   # (no output)
$ cat .git/info/attributes                                      # No such file
$ git config --get core.autocrlf; git config --get core.eol     # rc 1; rc 1 — unset
$ git check-attr -a -- corpus/README.md tools/harness/receipt_guard.py   # (no output)
```

`.git/hooks` holds exactly the 14 stock `.sample` files. Global `~/.config/git/config` defines
`filter.lfs.clean/smudge/process` and `filter.lfs.required=true`, but no attribute binds any file to
`lfs`, so no filter or eol rule is in force today.

jj bypasses both mechanisms if they are ever added — sandbox probe (`case5`, `.gitattributes`
`*.dat filter=up`, `*.txt text eol=crlf`):

```
# clean filter "tr a-z A-Z"
git  commit → git cat-file -p HEAD:b.dat   → SECRET
jj   commit → git cat-file -p HEAD:b.dat   → secret
# eol rule text eol=crlf
git  checkout -- a.txt                     → 6c "line\r\n"
jj   restore a.txt                         → 5c "line\n"
```

So a future `.gitattributes` filter or eol rule would be silently bypassed by jj lane commits; a
hook-based control (e.g. a pre-commit scanner) would be silently bypassed as well, since jj does not
run git hooks.

## Selftests under colocated jj (observed)

Run in the sandbox clone, after `jj git init --colocate` and `jj new` (detached HEAD), with the
in-scope tools copied verbatim from the live lane:

| command | exit | result excerpt |
|---|---|---|
| `python3 tools/harness/receipt_guard.py --selftest` | 0 | `"controls_passed": 45, "controls_total": 45, "selftest_passed": true` |
| `python3 tools/harness/claims-freshness.py --selftest` | 0 | `SELFTEST OK: registry 43/43 + seam 19/19 controls` |
| `python3 tools/check-readme-revisions.py --selftest` | 0 | `PASS control: base c42d675 README flagged (r49 defect) …`; `selftest skips: 0` |

Also observed: `jj git init --colocate` on an existing clone leaves HEAD **attached** to
`refs/heads/main`; the first jj mutation detaches it and points it at `@-` (after `jj new`: HEAD =
`f0e826a8…` = `@-`, `git symbolic-ref -q HEAD` rc 1, `git branch --show-current` prints empty,
`git rev-parse --abbrev-ref '@{u}'` → `fatal: HEAD does not point to a branch`). The helper's commit
flow (`jj commit -- <paths>`) again leaves HEAD at `@-`. No in-scope tool uses `@{u}`,
`--abbrev-ref HEAD`, `branch --show-current`, or HEAD as a branch name.

## Boundary observations (outside lane tooling; relevant to the wave plan)

- `jj commit -m … -- <paths>` with paths that carry no changes prints `Warning: The given paths do not
  match any file: …` and still creates an **empty commit** (observed in the helper-like sandbox flow).
  A helper retry or an already-committed pathspec can therefore push an empty commit and cite its
  hash. [INFERENCE] `scripts/hyaku/jj-lane.sh` should refuse when `jj log -r @` reports no paths.
- In the **rejected-push retry** the helper prints two hashes: `committed 9cdd73c2…` (the pre-rebase
  local commit) and `pushed 285ba5f0…` (the rebased commit actually sent). Observed:
  `git merge-base --is-ancestor 9cdd73c2 origin/main` → rc 1 (not an ancestor), while the pushed
  commit's parent is the fetched remote tip and the remote commit is preserved. The lane contract is
  "cite the pushed hash", but a consumer that scrapes the first `committed` line records an unpushed
  rewrite. `jj-lane.sh` should print a single citable hash, or label both unambiguously.
- `detect_branch` prefers the attached local branch over `origin/HEAD`. In a sandbox bare repo whose
  default was `master` while the payload branch was `main`, `init` selected `master` and later
  committed/pushed `origin master`, leaving `origin/main` untouched (observed). The live lane is
  unaffected (`branch.main.remote=origin` in `.git/config`); [INFERENCE] any newly created lane must
  be cloned so its checked-out local branch is the remote default, or the branch must be passed
  explicitly.
- A jj working-copy commit created before `jj config set --repo user.name/email` keeps the empty
  author (`JJ_EMPTY_STRING`, `jj` warns it "can't be pushed to remotes"); this matches the plan's
  `jj metaedit --update-author` requirement. The lane-identity invariant
  `<id>-shokunin <<id>@shokunin.local>` is not enforced by any in-scope gate.

## Recommendations (priority order)

1. Change `receipt_guard`'s committed probe from HEAD to the branch refs: read `HEAD` (tree) plus
   `refs/heads/main` and `refs/remotes/origin/main`; refuse if any contains the receipt, and print the
   `origin` commit as `committed_sha` (or a separate `landed_sha`) so cited hashes are pushed ones.
2. Treat the class-A fallback as documentation-only: it is dormant under detached HEAD and fails
   closed. No rewrite needed before cutover.
3. Make `check-readme-revisions` fail (not skip) when `BASE_COMMIT` is unresolvable, and assert
   `git cat-file -e <sha>^{commit}` before `git show`.
4. Keep the class-B selftest fixture git-only: it already lives under the gitignored `.scratch/`, and
   jj's snapshot did not pick up an untracked file or an ignored directory in the auto-track probes
   (with `snapshot.auto-track none()` and with the default). Do not point `git worktree add` at a
   colocated lane.
5. If a `.gitattributes` filter/eol rule or a git hook is ever added, do not rely on it for lane
   commits: jj bypasses both (evidence above). Enforce such rules in a tool surfaced by a lane gate.

## Helper exercise (sandbox copy) and remaining gaps

`scripts/hyaku/jj-lane.sh` was copied verbatim into the sandbox and run against a sandbox bare origin
(`HYAKU_STATE` redirected into the sandbox, `JJ_BIN` the host's jj), never against a live path:

| step | observed |
|---|---|
| `init <lane> kotodama` | `state branch=main local=ffc079bc… remote=ffc079bc… ahead=0 behind=0 head=attached`; `trunk()` set to `main@origin` |
| `commit --as kotodama -m "round test" -- a.txt b.txt` | `committed 78f28987…` / `pushed 78f28987…`; `HEAD` = `origin/main` = `78f28987…`; author and committer both `kotodama-shokunin <kotodama@shokunin.local>`; untracked `c.txt` absent from the commit |
| forced rejected push (remote moved out of band) | `committed 9cdd73c2…` then `pushed 285ba5f0…`; pushed parent = fetched remote tip `dfff8b0`; `origin/main` gained exactly one commit; the remote commit is preserved |
| `receipt_guard.py reports/validation.json --repo-root <lane>` after a helper commit | exit 3, `committed_sha=5c527a60…` = `HEAD` = `origin/main` (the correct steady state) |
| `state` | `state branch=main local=285ba5f0… remote=285ba5f0… ahead=0 behind=0 head=detached tracked=0 untracked=1` |

Remaining unrun checks: (a) the helper on a lane with a custom `immutable_heads()` alias (the source
mentions tameshi/mado) and `jj-lane.sh push`'s no-op path; (b) a rejection served by GitHub rather
than a local bare remote. Both are outside this lane's tooling.

Sandbox: `/fast/scratch/jj-wave/JjAuditKotodama-2/` — cases 1–5 and 7 removed (7 was the branch-name
setup artifact); `case6` (R2's false negative) and `case8` (helper init/commit/retry/guard) are kept
because they preserve cited reproductions.
