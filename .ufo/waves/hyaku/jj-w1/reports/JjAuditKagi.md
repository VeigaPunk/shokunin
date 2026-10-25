# JjAuditKagi — kagi lane git invocations under jj colocation

Read-only static audit, wave jj-w1. Audit revision `master @ c2cab35bc92e57e39e5489bac3386db078345b3f`
("Integrate remote documentation; preserve local round log"); worktree clean at audit start
(`git status --porcelain` → 0 lines). The lane is **not colocated yet** (`test -d .jj` → no), so every
jj-specific risk below is prospective. No live-repo write was made; all jj behavior evidence comes from
`/fast/scratch/jj-wave/JjAuditKagi-2/` with the host's `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`
(sandbox removed after the run; every command needed to reproduce is quoted).

## Findings

### F1. In-scope executable tooling contains **zero** git invocations

Enumerated exactly as scoped:

| surface | result |
|---|---|
| `tools/`, `scripts/`, `verifiers/` | all **ABSENT** (`for d in tools scripts verifiers; do test -d "$d" …`) |
| root `*.sh`, `*.py`, `*.mjs`, `*.js`, `Makefile` | **none** (`find . -maxdepth 1 … | wc -l` → `0`) |
| gates/selftests named in `SKILL.md` | the eight `corpus/*.sh`, 5,811 lines total (`wc -l corpus/*.sh`) |
| tracked non-root JS | `.ufo/round-20/route-admission.mjs` (40 lines; no `child_process`/spawn) |

Search over every in-scope file (script extensions plus the tracked `.mjs`):

```
$ grep -rniE 'git' --include='*.sh' --include='*.py' --include='*.mjs' --include='*.js' --include='Makefile' .
corpus/claim-ledger.sh:164:DENY_WORD_RE='(^|[^A-Za-z0-9_-])(op|the-janitor|git|rm|mv|cp|chmod|chown|curl|wget|sudo|ssh|scp|systemctl|tmux|kill|pkill|dd|truncate|shred|ln|rsync|tar)([^A-Za-z0-9_-]|$)'
```

That is a **policy regex, not a call site**. Targeted search for invocations and process APIs:

```
$ grep -nE '(^|[^A-Za-z0-9_-])(git|jj|subprocess|execFile|spawn|Popen|child_process)([^A-Za-z0-9_-]|$)' \
    corpus/*.sh .ufo/round-20/route-admission.mjs
corpus/claim-ledger.sh:164: … git|rm| …
$ grep -nEc 'child_process|execFile|spawn|Popen|subprocess' .ufo/round-20/route-admission.mjs
0
```

No gate shells out to a sibling gate or to `client.py` in a way that reaches a VCS; the gates read host
files/DBs, write scratch, and `python3` is used only for JSON/SQLite parsing
(`surface-census.sh:378,491,795`, `transcript-scan.sh:217,221`).

**Classified table (acceptance): no rows.** Counts per class in scope: **A=0, B=0, C=0, D=0.**
The practical consequence is positive: no file in kagi's own tooling has to change for jj colocation.
The lane's real exposure is procedural and outside the repo (F2).

### F2. The lane's actual git usage is outside the repo — classes C and B, both break under jj

The only git commands a kagi round runs **inside the lane repo** come from its generated prompt, not
from repo tooling. The current addendum already forbids them
(`scripts/hyaku/lane-addendum.md:123` helper commit; `:128` "Never `git add`, `git commit`, …"), but
the newest on-disk prompt for this lane (`$FLEET_ROOT/.ufo/prompts/kagi-round-21.md`) still carries the old text (mtime 2026-10-19 20:10, before the 2026-10-20 jj
directive):

| file:line | exact command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `$FLEET_ROOT/.ufo/prompts/kagi-round-21.md:189` | `git diff --cached \| grep -nE 'op://\|BEGIN [A-Z ]*PRIVATE KEY\|ghp_[A-Za-z0-9]{20,}\|AKIA[0-9A-Z]{16}\|xox[baprs]-'` | **C** | Index is irrelevant/empty: the prompt never stages anything, and every jj commit resets the git index. The sweep passes vacuously while the commit takes working-tree content. | `jj diff --git -- <paths> \| grep -nE '…'` before the helper commit (it snapshots, which the commit does anyway) |
| `$FLEET_ROOT/.ufo/prompts/kagi-round-21.md:191` | `git -c user.name=kagi-shokunin -c user.email=kagi@shokunin.local commit -m "round-21: <summary>" -- <paths>` | **B** | jj leaves HEAD detached; this commits on the detached head, never moves the branch bookmark, is never pushed, and the cited hash is not an ancestor of `master`. | `scripts/hyaku/jj-lane.sh commit <lane> --as kagi -m "…" -- <paths>`; cite its `pushed <hash>` |

Observed facts (each command run in the sandbox):

1. **The sweep cannot see what a pathspec commit takes** — true even on plain git, because
   `git commit -- <paths>` ignores the index and nothing stages:

   ```
   $ git diff --cached | grep -nE 'op://|…'      # after writing op://vault/secret into a tracked file
     rc=1 out=''
   $ git commit -q -m round -- f.txt              # rc=0
   $ git show HEAD:f.txt
     clean\nop://vault/secret
   $ git diff HEAD~1 HEAD -- f.txt | grep -nE 'op://'
     7:+op://vault/secret
   ```

2. **jj clears the index on the commit mutation** (the helper runs `metaedit` + `commit`). `jj st`
   alone left the staged entry intact; `jj commit` did not:

   ```
   $ git add f.txt; git diff --cached --stat
     f.txt | 1 +
   $ jj st
   $ git diff --cached --stat
     f.txt | 1 +
   $ jj commit -m jj-c3 -- f.txt
   $ git diff --cached --stat
     (empty)
   ```

3. **`git commit` on jj's detached HEAD produces a hash off the branch**:

   ```
   $ git symbolic-ref -q HEAD                     rc=1
   $ git rev-parse --abbrev-ref HEAD              HEAD
   $ git rev-parse --abbrev-ref --symbolic-full-name '@{u}'
     fatal: HEAD does not point to a branch
   $ git commit -q -m detached-commit -- f.txt    rc=0
   $ git rev-parse --short HEAD                   18425aa
   $ git rev-parse --short master                 b4a5d19
   $ git merge-base --is-ancestor HEAD master     rc=1
   ```

   That is exactly the broken invariant "a cited hash stays an ancestor of the branch".

4. **Even purely jj-managed state has `HEAD` ≠ bookmark**: after `jj commit`, `git rev-parse HEAD`
   returned the last exported commit `19a523a`, while `@` had moved to `b2728d9e` and `master` was
   `c863684`; `merge-base --is-ancestor HEAD master` exited `1`. So class **D**'s `rev-parse HEAD` is
   non-mutating but **not safe for citing the landed commit** — a classification caveat for the
   jj-era table, not a defect of kagi's files.

5. The prompt's final response asks for the "lane commit hash"; with no command named, an L1 reading
   it under jj can reach for `git rev-parse HEAD` (stale/exported commit, or `@-`) or `@{u}` (fatal).
   The canonical sources are the helper's `pushed <hash>` and `jj-lane.sh state` (`local=`, `ahead=`),
   or `git rev-parse master`.

### F3. Hooks and attributes: none in use — and jj bypasses both when added

Current state of the lane:

| item | observed |
|---|---|
| active hooks | **none** — `.git/hooks` has 14 files, all `*.sample`; `find .git/hooks -type f ! -name '*.sample'` → 0 |
| `core.hooksPath` | unset repo-wide and globally (`git config --get` rc=1; `--show-origin --get-all` empty; `--global` rc=1) |
| `.gitattributes` | absent |
| `.git/info/attributes` | absent |
| `core.attributesfile` | unset (no `~/.config/git/attributes`) |
| eol rules | none — `core.autocrlf` and `core.eol` unset |
| `.gitignore` | only `.ufo/interactive-sessions/`; `.git/info/exclude` is the default comment block |

Sandbox proof that a newly added hook/filter would **not** apply to `jj commit`:

```
$ # .git/hooks/pre-commit creates .git/HOOK_RAN
$ jj commit -m jj-c1 -- f.txt
HOOK_RAN exists: False
$ git commit -q -m git-c2 -- f.txt
HOOK_RAN exists: True
```

```
$ git config filter.upper.clean 'tr a-z A-Z' ; echo '*.filt filter=upper' > .gitattributes
$ echo lower > x.filt ; git add -f x.filt ; git show :x.filt
  LOWER          # clean filter ran
$ jj file track -- x.filt ; jj commit -m jj-filt -- x.filt ; git show HEAD:x.filt
  lower          # filter skipped
```

So today kagi has nothing for jj to bypass; if a content filter, eol rule or hook is added later,
`jj-lane.sh commit` will silently skip it. Enforce such checks in the helper or a gate, not in
`.gitattributes`/hooks.

### F4. Claim-ledger policy names `git` but not `jj`

`corpus/claim-ledger.sh:157-184` (executor at `:408` runs `bash -o pipefail -c "$cmd"`). The first-token
allowlist is `^(bash|grep|sha256sum|wc|test)$`; `DENY_WORD_RE` at `:164` lists `git` and **not** `jj`.
Verbatim replica in the sandbox:

```
REFUSE | git status | first-token:git
REFUSE | jj status | first-token:jj
ALLOW  | bash corpus/helper.sh
ALLOW  | bash corpus/jj-helper.sh
ALLOW  | bash corpus/git-helper.sh      # '-' is in the word class, so the regex misses it
REFUSE | bash corpus/git.sh | denied-verb:git
ALLOW  | bash corpus/jj.sh
REFUSE | grep git corpus/SKILL.md | denied-verb:git
ALLOW  | grep jj corpus/SKILL.md
```

[INFERENCE] After colocation a claim row can still run any `bash` helper; the deny list no longer
names the VCS the lane actually uses, so a helper that mutates via `jj` is not flagged by name.
This is a policy-label gap, not a sandbox escape (the same gap already exists for any wrapped
command), and no such jj-wrapping helper exists in the lane today.

## Counts per class

| scope | A | B | C | D |
|---|---|---|---|---|
| in-repo executable tooling (8 gates + 1 tracked `.mjs`) | 0 | 0 | 0 | 0 |
| adjacent, documented in the prompt (not repo tooling) | 0 | 1 | 1 | 0 (HEAD citation is D-shaped but unsafe for citation) |

For completeness, `scripts/hyaku/fleet-commit.sh` — fleet-root, not the lane — was read and not counted:
it uses `git ls-files --error-unmatch`, `git diff --cached --quiet`, `git rev-list --count`,
`git rev-parse HEAD`, `git add`, `git commit`, `git push`. It never runs in the lane repo and stays the
fleet-root path.

## Top three risks for kagi

1. **The credential sweep cannot see what gets committed.** `git diff --cached` is empty because the
   prompt never stages, and `git commit -- <paths>` commits working-tree content for tracked paths
   anyway (observed: sweep rc=1/no output, then the commit contained `op://vault/secret`). Under jj the
   index is additionally cleared on every commit. A secret-shaped line in `LOG.md`/corpus prose can
   land unswept.
2. **Detached-HEAD `git commit` breaks the landed invariant.** Observed hash `18425aa` while
   `master=b4a5d19`, `merge-base --is-ancestor` rc=1: cited but unreachable from the branch and
   unpushed. While HEAD was still attached, jj reset `@`'s parent to the new Git HEAD (`metaedit`
   printed "Reset the working copy parent to the new Git HEAD"); after detachment the commit stayed
   off-branch (`merge-base --is-ancestor` rc=1). I did not test whether jj later imports a detached
   git commit; the hash is unpushed either way. Replacement is the helper, whose output is the
   pushed hash.
3. **HEAD/upstream reads are unusable for citations.** `symbolic-ref -q HEAD` rc=1,
   `--abbrev-ref HEAD` = `HEAD`, `@{u}` → `fatal: HEAD does not point to a branch`, and
   `rev-parse HEAD` can name a lagging exported commit instead of the bookmark. Cite
   `jj-lane.sh commit|state` (`pushed <hash>`, `local=`) or `git rev-parse master`.

## Residual risk and verification gaps

- Static audit: no lane script, gate or selftest was executed (per the hard safety rules); no live
  repo was written or fetched. Every behavioral claim was reproduced in the sandbox with the same
  jj 0.45.1 as the host.
- The lane has no `.jj` yet; all jj risk is prospective until `jj-lane.sh init kagi-shokunin kagi`.
- Excluded by instruction: `.git`, `.jj`, corpus prose, `.ufo/waves`. The lane repo has no
  `.ufo/waves`; the fleet root's `.ufo/waves/*.mjs` (cross-lane-gate, corpus-gate, r4-adjudicate)
  do spawn git read-only and are outside this lane.
- Outside the lane and unverified here: host janitor `client.py`/`$CONFIG_DIR` tooling, and the
  fleet-root helpers beyond reading them.
- `.ufo/state/` invariant: the lane has no `.ufo/state/` and no `.gitignore` rule for it;
  `jj-lane.sh` rejects `.ufo/state/*` path arguments and `snapshot.auto-track="none()"` leaves
  untracked files out, but the helper was not executed.
- No tool installs or upgrades were made.

## Recommendations (advisory — no lane files edited)

1. Replace the prompt's sweep with `jj diff --git -- <paths> | grep -nE '…'` run before the helper
   commit; keep `git diff HEAD -- <paths>` only as a tracked-file approximation.
2. Delete the prompt's `git commit` step; the addendum's `jj-lane.sh commit` is the only lane commit.
   Cite `pushed <hash>` / `state local=`, never `@{u}` or `--abbrev-ref HEAD`.
3. Add `jj` to `DENY_WORD_RE` in `corpus/claim-ledger.sh` and re-run `--selftest`; if claim rows may
   wrap helpers, also pin the helper path to a read-only allowlist.
4. Do not add `.gitattributes` filters/eol rules or git hooks expecting them to affect lane commits;
   enforce those checks in `jj-lane.sh` or in a gate.
