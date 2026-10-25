# JjAuditChousa — chousa lane: git call-site audit and jj-colocation risk

Seat: `JjAuditChousa-2` (reviewer, read-only). Date: 2026-10-20.
Live lane: `/home/vgpnk/Projects/shokunin/chousa-shokunin` — branch `master`, tip
`d730ae4c33989ad9c8535764d4cae77b4db869f6`, `git status --porcelain` empty (0 lines),
no `.jj` directory (colocation has not been applied to the live lane), one worktree.
Audited gate bytes: `tools/research-gate.sh`, mode `100755`, 5290 lines,
`sha256 752e4e382ed77c06ac5030ce2179c7ca524934f86fd2a6b25ef946ab027ac553`.
Sandbox used for all jj measurements: `/fast/scratch/jj-wave/JjAuditChousa-2`
(removed after this report; nothing was run with cwd or `-R` under the live fleet root
or any live lane). No tool installs or upgrades were performed. Live-lane reads used
`status`, `rev-parse`, `ls-files`, `diff`, `log`, `config --list`, `check-attr`,
`remote -v` and `worktree list` — all read-only; no live write, stage, fetch or push.

## Findings (observed)

### F1 — The lane's executable tooling contains **zero** git invocations

In-scope inventory (everything below `.git/`, `.jj/`, `corpus/` prose and `.ufo/waves`
excluded):

```text
$ find . -path ./.git -prune -o -path ./.ufo -prune -o -type f -perm -u+x -print
./corpus/evidence/round24-measure.sh      # out of the enumerated dirs; checked separately
./tools/research-gate.sh

$ ls -d scripts verifiers 2>/dev/null; find . -maxdepth 1 \( -name '*.sh' -o -name '*.py' \
    -o -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \) -print
(no output: no scripts/, no verifiers/, no root scripts/Makefile)
```

The only gate named in `SKILL.md` is `research-gate` (all seven table rows resolve to
`bash tools/research-gate.sh ...`). Its selftest is `--selftest` inside the same file.

Direct scans of the gate (exit status captured):

```text
$ grep -nE '(^|[^A-Za-z_])git([^A-Za-z_]|$)' tools/research-gate.sh
$ echo $?
1                                   # no match

$ grep -oE '\b(git|hg|jj|svn|fossil)\b' tools/research-gate.sh | sort | uniq -c
(empty)

$ grep -n -i 'git' tools/research-gate.sh | wc -l
8
$ grep -oE '[A-Za-z_]*git[A-Za-z_]*' tools/research-gate.sh | sort | uniq -c
      8 digit
      1 github_pat
      1 github_pat_
      2 legit
      1 legitimate
(every hit is inside a word; no command token)
```

There is also no subprocess machinery that could construct a VCS call:

```text
$ grep -nE 'subprocess|execFile|spawn|popen|system\(|sh -c|bash -c' tools/research-gate.sh
4640:    if unshare --user --map-root-user --mount --propagation private bash -c '
4653:    unshare --user --map-root-user --mount --propagation private bash -c '
```

Both hits are the selftest's namespace fixtures (cases 103–106), containing `mount`,
`printf`, `stat` and a `bash "$NS_SELF"` exec — no git. The script has no `eval`,
no `source` and no dynamic command construction
(`grep -nE '\beval\b|\bbase64\b|^[[:space:]]*source |^[[:space:]]*\. '` → only the
prose word "eval" inside `SCOPE_KENGAKU`).

Runtime trace, verify mode (strace of every exec):

```text
$ strace -f -qq -e trace=execve -o trace bash tools/research-gate.sh \
    verify corpus/fixtures/full-r6.md --root .
rc=1                      # expected: sandbox root lacks the fleet research/ tree
execve_count=359
vcs_execves=0
unique execs: /usr/bin/bash /usr/bin/date /usr/bin/dirname /usr/bin/grep
              /usr/bin/head /usr/bin/readlink /usr/bin/sed /usr/bin/tr
```

Runtime trace, the SKILL-named selftest, from the clone's own root:

```text
$ strace -f -qq -e trace=execve -o trace bash tools/research-gate.sh --selftest
rc=0
RESEARCH_GATE_SELFTEST: PASS (136 cases, 0 skipped)
execve_count=25553
vcs_execves=0
```

Unique executables in the selftest trace: bash, basename, cat, chmod, cp, cut, date,
dirname, env, grep, head, id, ln, mkdir, mktemp, mount, mv, od, python3, readlink,
realpath, rm, sed, sha256sum, sort, stat, tail, tr, unshare, wc. Zero `git`, `jj`,
`hg`, `svn`. `python3` is used only for JSON parsing inside the selftest
(`command -v python3` guarded, lines 4032–4033 and 5173–5174).

Adjacent executable, outside the enumerated scope but checked because it is executable:
`corpus/evidence/round24-measure.sh` has exactly one git token, in the usage comment
(`git archive ab19cff`); it contains no git execution — its only subprocess is
`["bash","tools/research-gate.sh","verify",...]` (line 27).

### F2 — No git hooks are in use

```text
$ ls .git/hooks
applypatch-msg.sample  commit-msg.sample  fsmonitor-watchman.sample  post-update.sample
pre-applypatch.sample  pre-commit.sample  pre-merge-commit.sample    pre-push.sample
pre-rebase.sample      pre-receive.sample prepare-commit-msg.sample  push-to-checkout.sample
sendemail-validate.sample               update.sample        # 14 files, all *.sample

$ find .git/hooks -type f ! -name '*.sample' -print
(empty)

$ git config --show-origin --get-all core.hooksPath
(no output, rc=1)          # unset in local, global and system scopes

$ ls .git/config.worktree 2>/dev/null; git config --get-regexp '^submodule\.'
(absent; no submodule config)
```

Active hooks: none. `core.hooksPath` is unset at every scope, so git's default
`.git/hooks` applies and contains only the stock samples. Nothing for jj to bypass
in this lane today. (If a hook or `core.hooksPath` is added later, `jj` will not run it:
the helper commits with `jj`, not `git commit` — forward risk, see Recommendations 5.)

### F3 — No attributes, filters or eol rules in effect

```text
$ find . -name .gitattributes -print                  # (empty)
$ cat .git/info/attributes                            # none
$ git config --show-origin --get-all core.attributesFile
(no output, rc=1)
$ ls /home/vgpnk/.config/git/attributes /etc/gitattributes
no user attributes / no system attributes
$ git ls-files -z | xargs -0 git check-attr -a -- | grep -c .
0                                                     # across all 249 tracked files
$ git config --show-origin --list | grep -Ei 'autocrlf|eol|safecrl|filter'
file:/home/vgpnk/.config/git/config  filter.lfs.clean=git-lfs clean -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.smudge=git-lfs smudge -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.process=git-lfs filter-process
file:/home/vgpnk/.config/git/config  filter.lfs.required=true
```

The global git-lfs filter is declared but **no path assigns `filter=lfs`** (0 attribute
lines over the whole index), so it is inert for this lane. `core.autocrlf`, `core.eol`
and `core.safecrlf` are unset; there are no `text=`/`eol=`/`ident=` rules. jj bypasses
nothing here because there is nothing defined.

### F4 — Five git mentions exist, all documentation-only and read-only

No mention is executed by lane tooling. Full set (repo-wide search excluding
`.git` and `.ufo`; `corpus` was searched for shell/python entry points and only the
executable measurement script below mentions git):

| file:line | exact text | class | risk under jj colocation | jj-safe equivalent |
|---|---|---|---|---|
| `LOG.md:100` | `` `git -C .. log -1 --format='%H %aI' -- research` `` | D | none — read-only log; from the lane root `..` is the fleet root, which stays on git. Also works in a colocated lane (git reads exported refs). | same command, with the repo named explicitly: `git -C <fleet-root> log -1 ...` |
| `LOG.md:111` | `` `git remote -v` `` | D (read-only; not HEAD-derived) | none — reads `.git/config`; jj colocation keeps git remotes unchanged. | same |
| `LOG.md:123` | `` `git -C .. log` `` | D | none — same as line 100. | same |
| `SKILL.md:359` | `` `git clone` `` (historical: clone of the committed r7 gate run for comparison) | D (read-only setup; not HEAD-derived) | none — clones commits, never the checked-out lane. | same |
| `corpus/evidence/round24-measure.sh:4` | `` `git archive ab19cff` `` (usage comment for producing a before-state tree) | D (read-only; not HEAD-derived) | none — archives a commit; comment only, not executed. | same |

`LOG.md:111–112` also records the fleet origin URL
(`https://github.com/VeigaPunk/shokunin.git`). The live lane's own `.git/config`
currently has `remote.origin.url = https://github.com/VeigaPunk/chousa-shokunin.git`
and `git remote -v` returns both fetch and push rows (the LOG entry predates that
configuration). No lane command touches either remote.

### F5 — Measured jj state transitions (sandbox clone of the same commit)

Colocated with the helper's documented init shape
(`jj --config 'snapshot.auto-track="none()"' git init --colocate .`, then
`jj --ignore-working-copy config set --repo ...` for `snapshot.auto-track`,
`user.name`, `user.email`, `revset-aliases."trunk()" = "master@origin"`,
`jj bookmark track master@origin`). All commands below ran in the sandbox only.

| step | `git symbolic-ref -q --short HEAD` | `git rev-parse --abbrev-ref HEAD` | `git rev-parse @{u}` | `git diff --cached` |
|---|---|---|---|---|
| before jj init | `master` | `master` | `d730ae4c…` | n/a |
| after jj init (no mutation) | `master` | `master` | `d730ae4c…` | n/a |
| after a gate `--json` append (no jj yet) | `master` | `master` | `d730ae4c…` | empty (file modified in worktree) |
| after `jj status` (snapshot only) | `master` | `master` | `d730ae4c…` | **preserved** (staged entry survived) |
| after `jj describe -m …` | `master` | `master` | `d730ae4c…` | **reset** (staged became unstaged) |
| after `jj new` | *(empty → detached)* | `HEAD` | `fatal: HEAD does not point to a branch` | reset |
| after helper flow: `metaedit --update-author` → `commit -m … -- README.md` → `bookmark set master -r @-` | *(empty → detached)* | `HEAD` | `fatal: HEAD does not point to a branch` | reset |

Excerpts:

```text
$ git symbolic-ref -q --short HEAD || echo '(detached)'
(detached)
$ git rev-parse --abbrev-ref HEAD
HEAD
$ git rev-parse @{u}
fatal: HEAD does not point to a branch
$ git rev-parse master        # still works
229ab3b13b66a1c49309f858de89cd47390bb1f2
$ git log -1 --format='%an <%ae> committer=%cn <%ce>' master
chousa-shokunin <chousa@shokunin.local> committer=chousa-shokunin <chousa@shokunin.local>
```

Identity caveat, confirmed: `jj config set --repo user.*` after the fact prints
`Warning: ... The author of the working copy will stay "Joao Pedro Veiga
<jpveigao10@gmail.com>". To change the working copy author, use
'jj metaedit --update-author'.` — the helper's `metaedit --update-author` step is what
makes the measured commit carry `<id>-shokunin`, not the config calls alone.

Push, sandbox bare remote only (`git remote -v` confirmed the sandbox bare before any
fetch/push):

```text
$ jj git push --remote origin --bookmark master
bookmark: master@origin [updated] tracked
Bookmark master@origin already matches master
Nothing changed.                       # bare was pre-seeded at the same hash
$ git --git-dir=<sandbox>/bare rev-parse master
229ab3b13b66a1c49309f858de89cd47390bb1f2
$ git rev-parse master
229ab3b13b66a1c49309f858de89cd47390bb1f2
```

(A first attempt against an empty bare failed with `references unexpectedly moved on
the remote ... (reason: stale info)`; that is a sandbox seeding artifact — the bare had
no `master` while jj's tracking state expected one. Re-seeded, the push path completed.)

### F6 — The gate's only write surfaces, and their jj interaction

Non-temporary writes in the gate (everything else writes under mktemp dirs):

| file:line | write | trigger |
|---|---|---|
| `tools/research-gate.sh:2504` | `printf '%s\n' "$line" >>"$JSON_ARG"` | `verify-all ... --json PATH` (append-only, validated at 2368–2376) |
| `tools/research-gate.sh:2792` | `printf '%s' "$text" >"$path"` | `--pin PATH` |
| `tools/research-gate.sh:2862–2866` etc. | mktemp under `$TMPDIR` | `--selftest` and the canonical pin capture (gate removes them) |

Measured interaction with jj (sandbox): run the gate with
`--json corpus/evidence/verify-all-manifest.jsonl` (a tracked file), which changed it
8 → 9 → 10 lines, then commit a *directory* that contains it:

```text
$ bash tools/research-gate.sh verify-all corpus/fixtures/integrity-r7.md \
    --json corpus/evidence/verify-all-manifest.jsonl --root .
# (sandbox root lacks the fleet research/ tree, so the verdict is DRIFT;
#  the section under test, integrity, reported verdict=CLEAN)
$ wc -l < corpus/evidence/verify-all-manifest.jsonl
9
$ git diff --cached --name-only
(empty)
$ jj commit -m 'directory pathspec probe' -- corpus/evidence
$ git show --stat --format='%h %s' <new commit>
9f71122 directory pathspec probe
 corpus/evidence/verify-all-manifest.jsonl | 2 ++
```

With an empty git index, a directory pathspec still committed both appended receipt
lines. Under git the same result would require `git add`. A file pathspec excludes it:

```text
$ git add LOG.md ; echo 'fourth probe' >> README.md
$ jj commit -m 'pathspec probe' -- README.md
$ git show --stat --format='%h %s' <commit>
cdf9bc9 pathspec probe
 README.md | 1 +
$ git status --porcelain
 M LOG.md
 M corpus/evidence/verify-all-manifest.jsonl
```

`LOG.md` had been staged with `git add`; after `jj commit` its content was in `@` but its
index entry was gone (status ` M`, not `M `). `jj commit` itself is pathspec-faithful.

## Classified table — executable call sites

| # | file:line | exact command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|---|
| — | — | *(none: the lane has no executable git call site)* | — | — | — |

Counts, executable tooling:

| class | count |
|---|---|
| A (attached HEAD / upstream assumed) | **0** |
| B (mutates history, index or worktree) | **0** |
| C (reads index or staging state) | **0** |
| D (read-only, HEAD-commit based) | **0** |
| total | **0** |

Counts, documentation-only mentions (F4, not executed by lane tooling):

| class | count |
|---|---|
| A | 0 |
| B | 0 |
| C | 0 |
| D (read-only; two rows are not HEAD-derived, marked in F4) | 5 |
| total | 5 |

## Top three risks for this lane

**R1 — Detached HEAD makes every future class-A call fail, and the lane's docs are the
only git recipes left.** Measured post-helper state: `git rev-parse @{u}` →
`fatal: HEAD does not point to a branch`, `git rev-parse --abbrev-ref HEAD` → `HEAD`,
while `git rev-parse master` and `git log master` still work. No lane code calls these
today, so the risk is a regression by future edits or replayed recipes. Any state check
added later must resolve the branch (`refs/heads/<branch>` or `refs/remotes/origin/<branch>`)
and must not use `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`, or `symbolic-ref HEAD`
as a branch source.

**R2 — Gate receipts are swept by directory pathspecs because jj commits from `@`, not
from the git index.** The gate's `--json` append (line 2504) and `--pin` write (line 2792)
land as ordinary working-copy writes. Measured: with `git diff --cached` empty,
`jj commit -- corpus/evidence` committed two appended manifest lines. The helper accepts
directories (it even splits files/dirs for `jj file track`), so a lane that commits a
receipt directory includes whatever the gate appended, staged or not. Prefer file-only
pathspecs for receipts, or keep manifests outside the directories a lane commits.

**R3 — The git index is not a staging gate under jj.** Measured: a staged `LOG.md`
(`git add`) lost its index entry across `jj commit` and reappeared as an unstaged
worktree change; the content survived only inside `@`. No lane tooling stages today
(good), but any operator or future script that relies on `git add` … later `git commit`
is silently unsafe in a colocated lane. Treat `@` as the staging area; commit with
explicit file paths through the helper.

## [INFERENCE]

- The helper's `state` subcommand is pure-git and read-only (its `print_state` uses
  `rev-parse`, `rev-list`, `symbolic-ref`, `status`), so it is jj-safe; its
  `branch=`/`head=` fields correctly report the detached state. Its `tracked=` count
  compares the worktree to git `HEAD`; in the measured post-commit state `HEAD` is
  `@-` (the branch tip), so pending `@` changes still surface as worktree
  modifications and are counted — no reporting defect observed. That is fleet
  tooling, outside this lane's scope; noted for the orchestrator.
- If hooks or `.gitattributes` are added to this lane later, the helper's `jj` commits
  will bypass them, because `jj` runs neither git hooks nor smudge/clean filters.
  Today there are none, so colocation changes nothing.
- The live lane has an origin URL but no `.jj`; the orchestrator's `init` will run on a
  repo whose `@` is the imported `master` tip, with the pre-existing HEAD author
  (`protocol-shokunin`) — the helper's `metaedit --update-author` is required for the
  identity invariant, as measured.

## Residual risk and verification gaps

- Out-of-lane landing tooling was not audited: `scripts/hyaku/jj-lane.sh` itself,
  `scripts/hyaku/fleet-commit.sh`, lane-close scripts, and the fleet root's own git
  usage. This report clears the lane's bytes only; the actual commit/push path lives
  there.
- The live lane was not colocated or mutated (safety rules); all jj measurements come
  from a clean `git clone` of the live lane at `d730ae4c` (same tracked tree, same gate
  bytes; the live worktree was clean, so clone == HEAD == audited bytes).
- The gate's two sandbox `verify-all` runs exited DRIFT because the sandbox root lacks
  the fleet `research/` tree; only the execve inventory (F1) and the append behavior
  (F6) are used from those runs, not the verdicts. The SKILL-named selftest passed
  136/136 in the clone.
- The static scans cannot prove the absence of a dynamically constructed VCS call in
  future revisions; they do prove it for the audited bytes pinned above. Runtime traces
  (verify and selftest) independently show zero VCS execs.
- The first sandbox push failed against an empty bare remote; this was a sandbox setup
  artifact, not a helper or jj defect, and the re-run after seeding succeeded.

## Recommendations

1. Keep lane tooling git-free. Add a cheap guard to the lane's round checklist or a
   future gate lint:
   `find tools scripts -type f 2>/dev/null | xargs -r grep -nE '(^|[^A-Za-z_])git([^A-Za-z_]|$)' || true`
   must print nothing (it prints nothing at the audited bytes).
2. If a lane ever needs VCS state, use `git rev-parse <branch>` /
   `git rev-parse refs/remotes/origin/<branch>` (measured to work detached) or the
   helper's `state`; never `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`, or
   `symbolic-ref HEAD`.
3. Commit gate receipts with file paths, never directory pathspecs; or keep
   `--json`/`--pin` outputs outside committed directories. This preserves the
   "commits are pathspec-limited" invariant in the sense of naming exactly the bytes.
4. Do not introduce `git add`/`stash`/`checkout` into lane workflows; the index is reset
   by jj. If one is ever needed, route it through the helper instead.
5. Revisit this audit if hooks, `.gitattributes`, or a lane-local git wrapper appear —
   each would change the jj-bypass delta from "nothing defined" to "defined and skipped".
