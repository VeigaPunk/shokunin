# JjDocHooksAttributes — git hooks, `.gitattributes`, filters and LFS under jj 0.45.1

**Verdict: none of the three Git mechanisms is honored by any jj operation on jj 0.45.1.**
jj runs no hooks, reads no `.gitattributes` rules (eol, filter, diff/binary, merge), runs no
clean/smudge filters in either direction, and Git LFS fails in all three directions (commit
stores raw bytes, checkout leaves pointer files, push uploads no LFS objects). Repos that rely
on any of them must keep those operations on the Git CLI path.

- Toolchain: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git version 2.56.0`,
  `git-lfs/3.8.0 (GitHub; linux amd64; go 1.27.0-X:nodwarf5)`.
- Docs: versioned **v0.45.1** pages (`https://docs.jj-vcs.dev/v0.45.1/...`, the version matching
  the installed binary). The site's `latest` alias currently points at **v0.46.0**
  (`https://docs.jj-vcs.dev/versions.json`: `{"version":"v0.46.0","aliases":["latest"]}`); the
  three statements quoted below are byte-identical on both pages, and the 0.46.0 CHANGELOG section
  contains no hook/attribute/LFS/eol entry. `https://jj-vcs.github.io/jj/latest/...` answers with a
  301 to `http://docs.jj-vcs.dev/latest/...` (`location:` header observed).
- All probes ran in `/fast/scratch/jj-wave/JjDocHooksAttributes/` (fresh `git init` +
  `jj git init --colocate`). No live repo was written, staged, fetched or checked out and no real
  remote was pushed: every `origin` was created with `git remote add origin <sandbox-bare>`, and
  where `git remote -v` was printed it confirmed the sandbox path (for example
  `origin /fast/scratch/jj-wave/JjDocHooksAttributes/hooks/remote.git`).
- In the transcripts, `$B` is the sandbox subdirectory named by the experiment's heading (e.g.
  `.../JjDocHooksAttributes/hooks`), and `...` marks output trimmed only where stated.

---

## F1 — Git hooks are not run: not pre-commit, not commit-msg, not pre-push

**Citation.** v0.45.1 Git compatibility → Supported features:
<https://docs.jj-vcs.dev/v0.45.1/git-compatibility/> — quote:
> **Hooks: No.** There's [#405](https://github.com/jj-vcs/jj/issues/405) specifically for providing
> the checks from <https://pre-commit.com/>.

Issue #405 `Integrate with https://pre-commit.com/` is **Open** (read from the issue page, which
shows `![Issue]Open`; the GitHub API was rate-limited with HTTP 403). The CLI agrees: `jj help`
has no hook command, `jj help git` never mentions hooks, `jj commit --help`, `jj git push --help`,
`jj git clone --help` and `jj run --help` expose no hook/verify flag, and
`jj config list --include-defaults | grep -ic hook` returns **0**. (`jj help -k` accepts only
`bookmarks`, `config`, `filesets`, `glossary`, `revsets`, `templates`, `tutorial`; none documents
hooks, and the only `hook` string in `jj help -k config` is a link to Gerrit's `commit-msg`
format documentation.) The v0.45.1 CHANGELOG contains zero lines matching `hook`.

**Experiment 1 — hooks installed, then jj mutations.**

```console
$ mkdir -p .git/hooks
$ for h in pre-commit commit-msg pre-push; do
    printf '#!/bin/sh\necho "%s $*" >> %s/hook-fired.log\nexit 0\n' "$h" "$B" > ".git/hooks/$h"
    chmod +x ".git/hooks/$h"
  done
$ echo hello > a.txt
$ jj commit -m "jj commit with hooks installed"
Done importing changes from the underlying Git repo.
Working copy  (@) now at: kqtzoqno 341eeaa2 (empty) (no description set)
Parent commit (@-)      : oumkoqkl b4f74a67 jj commit with hooks installed
$ if [ -f "$B/hook-fired.log" ]; then cat "$B/hook-fired.log"; else echo "(no hooks fired)"; fi
(no hooks fired)
$ jj describe -m "noop"; jj new
...
$ if [ -f "$B/hook-fired.log" ]; then cat "$B/hook-fired.log"; else echo "(still no hooks fired)"; fi
(still no hooks fired)
```

`jj describe` and `jj new` did not fire anything either. No hook side effect was observed for any
jj command.

**Experiment 2 — the same hooks fire under Git in the same sandbox.** This proves the hook files
were valid and executable, so the silence above is jj's behavior, not a bad test:

```console
$ git commit --allow-empty -m control
[detached HEAD d0aa80c] control
pre-commit
commit-msg .git/COMMIT_EDITMSG
$ git push <sandbox-bare> HEAD:refs/heads/fromgit
To .../hooks2/remote2.git
 * [new branch]      HEAD -> fromgit
pre-push .../hooks2/remote2.git .../hooks2/remote2.git
```

**Experiment 3 — pre-push specifically, with a verified successful jj push.**

```console
$ jj git push -b main
Changes to push to origin:
  bookmark: main [add to 82753d2914a8]
push_exit=0
$ git --git-dir="$B/remote.git" for-each-ref
82753d2914a8139782cdeff96c86556e2aa11cbc commit	refs/heads/main
$ if [ -f "$B/hooklog" ]; then cat "$B/hooklog"; else echo "(pre-push not fired by jj push)"; fi
(pre-push not fired by jj push)
```

**Mechanism — jj hides `git push` from the hook with `--no-verify`.** A wrapper installed as
`git.executable-path` logged the exact argv:

```console
$ jj --config git.executable-path="$B/gitwrap" git push -b main
Changes to push to origin:
  bookmark: main [add to dbed15dcd3be]
$ cat "$B/argv.log"
GIT-ARGV: [-c] [core.fsmonitor=false] [-c] [submodule.recurse=false] [--git-dir]
 [.../repo/.git] [push] [--porcelain] [--no-verify] [--force-with-lease=refs/heads/main:]
 [--] [origin] [dbed15dcd3be3dfd7171b019c075b83283e7f0d8:refs/heads/main]
```

`git help push` (local documentation) defines the flag:

> --verify, --no-verify
>     Toggle the pre-push hook (see githooks(5)). ... With --no-verify, the hook is bypassed
>     completely.

A control in a clean sandbox confirms the flag is what suppresses it:

```console
$ git push -q "$B/remote.git" HEAD:refs/heads/plain; cat "$B/hooklog"
fired .../nverify/remote.git .../nverify/remote.git
$ : > "$B/hooklog"; git push -q --no-verify "$B/remote.git" HEAD:refs/heads/nv
$ cat "$B/hooklog"                                   # empty
(hooklog empty: --no-verify suppressed pre-push)
```

For completeness, the wrapper also shows `jj git fetch` and `jj git clone` call plain
`git fetch --porcelain --prune --no-write-fetch-head --no-tags ...` (no hooks exist for fetch,
so nothing is bypassed there). `jj git clone` is `git fetch` + `git remote show` + jj's own
checkout — not `git clone`:

```console
GIT-ARGV: [...] [fetch] [--porcelain] [--prune] [--no-write-fetch-head] [--no-tags] [--]
 [origin] [+refs/heads/*:refs/remotes/origin/*] [+refs/tags/*:refs/jj/remote-tags/origin/*]
GIT-ARGV: [...] [remote] [show] [--] [origin]
```

`git commit --no-verify` means "Bypass the pre-commit and commit-msg hooks" (`git help commit`).
jj does not go through `git commit` at all: wrapping `git.executable-path` and running
`jj commit -m c1`, `jj describe -m desc`, `jj new` produced an empty argv log:

```console
$ jj --config git.executable-path="$B/gitwrap" commit -m "c1"
$ jj --config git.executable-path="$B/gitwrap" describe -m "desc"
$ jj --config git.executable-path="$B/gitwrap" new
$ cat "$B/argv.log"
(no git invocation at all)
```

Commit-side hooks therefore cannot run, regardless of `--no-verify`.

---

## F2 — `.gitattributes` is ignored entirely; eol rules do not apply in either direction

**Citation.** v0.45.1 Git compatibility → Supported features:
<https://docs.jj-vcs.dev/v0.45.1/git-compatibility/> — quote:
> **.gitattributes: No.** There's [#53](https://github.com/jj-vcs/jj/issues/53) about adding support
> for at least the `eol` attribute.

The same page limits Git config interop to remotes and `core.excludesFile`:
> The only configuration from Git (e.g. in `~/.gitconfig`) that's respected is the following.

so `core.autocrlf`, `core.eol` and `filter.*` are out of scope by documentation as well. Issue #53
`Add support for .gitattributes` is **Open**. The local CLI documents exactly one native eol knob,
repo-wide and off by default (`jj help -k config`):

> This setting serves the same purpose as the [`core.autocrlf`] Git config.

and, for `input-output`:

> Apply EOL conversion on both file check-in to and file check-out from the
> backend store, so you have CRLF line endings in your working directory

```console
$ jj config list --include-defaults | grep -n 'working-copy.eol-conversion'
16:working-copy.eol-conversion = "none"
```

**Experiment 1 — identical input committed by Git and by jj.** Same `.gitattributes`
(`*.txt text eol=lf`), same CRLF bytes, same filter config:

```console
$ printf '*.txt text eol=lf\n*.up filter=upper\n' > .gitattributes
$ printf 'one\r\ntwo\r\n' > t.txt; printf 'lower\n' > f.up
# git path: git add .gitattributes t.txt f.up; git commit -m "committed by git"
== git path ==
t.txt blob: 00000000: 6f6e 650a 7477 6f0a                      one.two.
f.up  blob: LOWER
commit: 4f66a87 committed by git
# jj path: jj git init --colocate; jj commit -m "committed by jj"
== jj path ==
t.txt blob: 00000000: 6f6e 650d 0a74 776f 0d0a                 one..two.
f.up  blob: lower
commit: bd3c83b committed by jj
```

`t.txt` under `text eol=lf`: Git normalizes CRLF→LF in the blob; jj preserves the CRLF bytes
(`0d 0a`). The CRLF bytes were committed verbatim.

**Experiment 2 — `core.autocrlf` is not consulted.**

```console
$ git config core.autocrlf input
$ printf 'x\r\ny\r\n' > auto.txt
$ jj commit -m "crlf under core.autocrlf=input"
$ git cat-file blob HEAD:auto.txt | xxd
00000000: 780d 0a79 0d0a                           x..y..
```

**Experiment 3 — no checkout conversion for `eol=crlf`.** Stored LF, attribute asks for CRLF:

```console
$ printf '*.txt text eol=crlf\n' > .gitattributes
$ printf 'p\nq\n' > out.txt; jj commit -m "lf content, attribute asks crlf"; jj new
worktree out.txt:
00000000: 700a 710a                                p.q.
```

**Experiment 4 — jj's own `working-copy.eol-conversion` does work, repo-wide.** `input` normalizes
on check-in; `input-output` writes CRLF on checkout and re-normalizes on snapshot:

```console
$ jj config set --repo working-copy.eol-conversion input
$ printf 'a\r\nb\r\n' > in.txt; jj commit -m "eol input"
$ git cat-file blob HEAD:in.txt | xxd
00000000: 610a 620a                                a.b.
$ jj config set --repo working-copy.eol-conversion input-output
$ printf 'm\nn\n' > io.txt; jj commit -m "io mode"
$ rm io.txt; jj restore io.txt
Working copy  (@) now at: ...
...
$ xxd io.txt
00000000: 6d0d 0a6e 0d0a                           m..n.        # worktree CRLF
$ printf 'm\r\nn\r\n' > io.txt; jj status | head -1
The working copy has no changes.                              # snapshot normalized it back
```

**Experiment 5 — other attributes are ignored too (binary/diff).** `.gitattributes`
`*.dat binary` (macro for `-diff -merge -text`); jj still treats the file as text:

```console
$ git diff -- a.dat            # pure git
Binary files i/a.dat and w/a.dat differ
$ jj diff -r @                 # jj
Modified regular file a.dat:
   1     : one
        1: two
```

The reason is documented in `jj help -k config`:
> To detect if a file is binary, Jujutsu currently checks if there is a NULL byte in the file,
> which is different from the algorithm of gitoxide or Git.

**Experiment 6 — ignored attributes leave the Git view permanently dirty.** After a jj commit of
CRLF bytes under `eol=lf`, `git status` reports a modification that `git checkout` cannot clear;
same for the filter case:

```console
== git status right after jj commit (eol=lf, blob CRLF) ==
 M t.txt
== git diff --stat ==
warning: in the working copy of 't.txt', CRLF will be replaced by LF the next time Git touches it
 t.txt | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
== git checkout -- t.txt then status ==
00000000: 6f6e 650d 0a74 776f 0d0a                 one..two.
 M t.txt                                              # still modified
== git status right after jj commit (filter=upper, blob lowercase) ==
 M f.up
== git diff ==
-lower
+LOWER
```

`jj status` itself is clean in both repos; the disagreement is between jj's bytes and Git's
attribute-filtered view of the same commit.

No jj command printed any warning that attributes or filters were being ignored.

---

## F3 — Filters (clean/smudge) never run

**Citation.** Same v0.45.1 page: `**.gitattributes: No.**` and the configuration limitation quoted
in F2 ("The only configuration from Git ... that's respected is the following", i.e. remotes and
`core.excludesFile`). There is no `filter.*` support to configure.

**Experiment 1 — clean filter ignored at commit.** `filter.upper.clean = "tr a-z A-Z"`,
`filter.upper.smudge = cat`, `.gitattributes` `*.up filter=upper`, content `hello filter`:

```console
== pure git: staged blob with filter=upper clean ==
HELLO FILTER
== jj: committed blob with filter=upper clean ==
hello filter
```

(`f.up` in the divergence table above: Git `LOWER` vs jj `lower`.)

**Experiment 2 — smudge filter ignored at checkout.** Same driver, smudge
`sed s/^/S:/`, stored blob `HELLO`:

```console
$ rm f.up; git checkout -- f.up; cat f.up
S:HELLO
$ rm f.up; jj restore f.up
Working copy  (@) now at: ...
...
$ cat f.up
HELLO                     # jj writes the stored blob, unfiltered
$ jj status | head -1
The working copy has no changes.
```

`ident` is ignored as well: `.gitattributes` `*.id ident` with `cid=$Id$` committed by jj stays
literally `cid=$Id$`.

---

## F4 — Git LFS is unusable under jj: raw blobs, pointer worktrees, no uploads

**Citation.** v0.45.1 Git compatibility:
<https://docs.jj-vcs.dev/v0.45.1/git-compatibility/> — quote:
> **Git LFS: No.** ([#80](https://github.com/jj-vcs/jj/issues/80))

Issue #80 `Add support for Git LFS` is **Open**.

**Experiment 1 — jj commit of an LFS-tracked path stores the raw file, not a pointer.**
`git lfs install --local`, `git lfs track "*.bin"` generates
`*.bin filter=lfs diff=lfs merge=lfs -text`; `data.bin` contains `raw-payload`:

```console
== jj: committed blob for LFS-tracked data.bin ==
raw-payload
== jj: local lfs object store ==
(count: 0)
$ jj status
The working copy has no changes.
```

Git's own clean path on the same content produces a pointer (control repository):

```console
== control: git-committed blob under filter=lfs ==
version https://git-lfs.github.com/spec/v1
oid sha256:0ee268c331a1e8b08215997976068718357b8250e92faf8935d1c7fc02faa41f
size 12
$ git config --local --get-regexp '^filter\.lfs\.'
filter.lfs.clean git-lfs clean -- %f
filter.lfs.smudge git-lfs smudge -- %f
filter.lfs.process git-lfs filter-process
filter.lfs.required true
```

**Experiment 2 — jj checkout leaves pointer files instead of content.** `jj git clone` of a Git
LFS repo whose blob is a pointer (control `git clone` smudged correctly):

```console
$ git clone lfsctl gitclone; head -c 60 gitclone/data.bin | xxd
00000000: 7261 772d 7061 796c 6f61 640a            raw-payload.
$ jj git clone lfsctl jjclone
Working copy  (@) now at: oorynpzo e47031a3 (empty) (no description set)
Parent commit (@-)      : uzvoolsk a0a5bcc8 master | lfs commit by git
$ head -c 200 jjclone/data.bin | xxd | head -4
00000000: 7665 7273 696f 6e20 6874 7470 733a 2f2f  version https://
00000010: 6769 742d 6c66 732e 6769 7468 7562 2e63  git-lfs.github.c
00000020: 6f6d 2f73 7065 632f 7631 0a6f 6964 2073  om/spec/v1.oid s
00000030: 6861 3235 363a 3065 6532 3638 6333 3331  ha256:0ee268c331
$ jj status
The working copy has no changes.
```

The working copy contains the pointer text and matches HEAD, because jj materializes the tree
itself (see the `git fetch` argv in F1) and never runs the smudge filter.

**Experiment 3 — jj push ships pointers but no LFS objects, and skips the LFS pre-push hook.**
A pointer commit (made by Git) pushed with `jj git push` to a fresh sandbox bare remote:

```console
$ jj git push -b master
Changes to push to origin:
  bookmark: master [add to e4d79e81a375]
push_exit=0
$ git --git-dir="$B/remote.git" for-each-ref
e4d79e81a3755fcb33a464b2b5b79a8c29a9ffc7 commit	refs/heads/master
$ git --git-dir="$B/remote.git" cat-file blob master:d.bin
version https://git-lfs.github.com/spec/v1
oid sha256:0ee268c331a1e8b08215997976068718357b8250e92faf8935d1c7fc02faa41f
size 12
$ find "$B/remote.git/lfs" -type f 2>/dev/null | wc -l
0
$ if [ -f "$B/hooklog" ]; then cat "$B/hooklog"; else echo "(pre-push not fired by jj push)"; fi
(pre-push not fired by jj push)                      # marker pre-push never ran
```

`git lfs install --local` had installed its `pre-push` hook in `.git/hooks` (listed next to
`post-checkout`, `post-commit`, `post-merge`); jj's `--no-verify` (F1) means it never ran, so no
objects were transferred.

**Experiment 4 — the pushed remote is broken for Git users.**

```console
$ git clone remote.git verifyclone; echo "clone_exit=$?"
Downloading d.bin (12 B)
Error downloading object: d.bin (0ee268c): Smudge error: ... remote missing object 0ee268c...
error: external filter 'git-lfs filter-process' failed
fatal: d.bin: smudge filter lfs failed
warning: Clone succeeded, but checkout failed.
clone_exit=128
```

---

## F5 — What jj does invoke, and what it never does

Across `jj git push`, `jj git fetch` and `jj git clone`, the complete set of git invocations
observed through `git.executable-path` was `git push --no-verify`,
`git fetch --prune --no-write-fetch-head --no-tags`, and `git remote show`. `jj commit`,
`jj describe` and `jj new` invoked **no git process at all** under the same wrapper (empty argv
log). No hook process and no filter subprocess was ever observed. `jj`'s own checkout writes the
stored blob bytes; its push delegates object transfer to `git push`.

---

## Consequence for the planned shokunin integration

### Present-state census (read-only, no jj invocation)

```console
$ for d in /home/vgpnk/Projects/shokunin/*-shokunin; do
    ga=$(git -C "$d" ls-files | grep -ci gitattributes || true)
    hooks=$(ls "$d/.git/hooks" 2>/dev/null | grep -v sample | tr '\n' ',' || true)
    cfg=$(git -C "$d" config --local --get-regexp '^(filter\.|core\.hooksPath|core\.autocrlf|core\.eol)' | tr '\n' ';' || true)
    lfs=$(test -d "$d/.git/lfs" && echo yes || echo no)
    printf '%-24s gitattributes=%s hooks=[%s] lfsdir=%s cfg=[%s]\n' "$(basename "$d")" "$ga" "$hooks" "$lfs" "$cfg"
  done
audio-shokunin           gitattributes=0 hooks=[] lfsdir=no cfg=[]
...
tsukuroi-shokunin        gitattributes=0 hooks=[] lfsdir=no cfg=[]
# all 21 output lines identical: gitattributes=0 hooks=[] lfsdir=no cfg=[]
$ git -C /home/vgpnk/Projects/shokunin ls-files | grep -i gitattributes
(none tracked)
$ git -C /home/vgpnk/Projects/shokunin config --show-origin --get-regexp '^(filter\.lfs|core\.hooksPath|core\.autocrlf|core\.eol)'
file:/home/vgpnk/.config/git/config	filter.lfs.clean git-lfs clean -- %f
file:/home/vgpnk/.config/git/config	filter.lfs.smudge git-lfs smudge -- %f
file:/home/vgpnk/.config/git/config	filter.lfs.process git-lfs filter-process
file:/home/vgpnk/.config/git/config	filter.lfs.required true
```

- No lane repo tracks a `.gitattributes`, has a non-sample hook, a repo-local filter/hooksPath/
  autocrlf/eol setting, or an LFS store. `core.hooksPath` is unset everywhere.
- The Git LFS *filters* are installed only in the user-level config; no repo has a
  `filter=lfs` attribute, so they never engage today.
- Fleet root: same picture, plus **8 tracked CRLF files** under
  `research/round-18-kimi-model-routing/...` (for example `.../battery/raw/telemetry.csv`). With
  no `.gitattributes` and no `core.autocrlf`/`core.eol`, Git stores and checks them out
  byte-exact, so nothing relies on eol conversion.

**Conclusion: the planned cutover breaks no *present* hook/attribute/filter/LFS dependency.**
The danger is latent, and it is asymmetric:

1. **Two commit paths now behave differently.** `scripts/hyaku/jj-lane.sh` commits with
   `jj commit -m "$msg" -- "${existing[@]}"` (line 230) and pushes with
   `jj git push --remote origin --bookmark "$BRANCH"` (line 109) → no hooks, no attributes, and
   `--no-verify` on push. `scripts/hyaku/fleet-commit.sh` commits with
   `g add` (line 49) / `g commit -q -m "$msg"` (line 53) and pushes with
   `git push -q "$REMOTE" "HEAD:$BRANCH"` (line 63) → **hooks and attributes apply**. A
   pre-commit/pre-push/commit-msg check installed in a lane `.git/hooks` would silently skip
   every lane commit made through the helper but still run for fleet-root commits; a lane's
   pre-push secret scan would never see a `jj git push`.
2. **`.gitattributes` adoption would corrupt lane hygiene signals.** If a lane ever adds eol or
   filter rules, jj commits raw bytes (F2/F3), and any Git-side view then shows a permanent
   ` M <file>` (Experiments 6). `jj-lane.sh state` derives its `tracked=`/`untracked=` counts
   from `git status --porcelain` (`print_state`), so it would report a dirty lane after a clean
   commit. `fleet-commit.sh`'s `git add` would then normalize/rewrite the same file, producing a
   second, different commit.
3. **LFS must be banned, not merely unsupported.** `git lfs` is installed and its filters are
   global, so a single `git lfs track "*.bin"` in a lane would make `jj-lane.sh` commit the raw
   binary (no pointer), `jj git clone`/`jj edit` leave pointer files on disk, and
   `jj git push` publish a remote whose pointers have no objects — a fresh `git clone` fails with
   exit 128 (F4.3/F4.4). Game-dev/audio lanes are the likely places to reach for binary assets.
4. **The six protocol invariants are untouched.** Landed = committed AND pushed (helper reads the
   remote tip after push), cited hash stays an ancestor (the helper's retry rebases only unpushed
   commits onto `<branch>@origin` and never amends pushed ones), lane identity is set by
   `metaedit --update-author` (line 227), commits stay pathspec-limited (`jj commit ... -- paths`),
   `LOG.md` append-only and `.ufo/state/` exclusion are path-policy guards in the helper. None of
   them uses hooks, attributes or LFS, so this finding does not invalidate the design — it
   constrains what may be added later.
5. **Server-side is unaffected.** `--no-verify` only suppresses the client hook; GitHub-side
   hooks, branch protection and CI still run. If enforcement matters, it belongs in CI or in an
   explicit check inside the helper.

### Recommendations

- **Do not use `.git/hooks` as the enforcement layer for lane commits or pushes.** If a check is
  required, invoke it explicitly inside `jj-lane.sh commit`/`do_push` before `jj commit` /
  `jj git push`, or in CI. A `.git/hooks/pre-push` will never fire on `jj git push` (proof: F1
  argv log with `--no-verify`).
- **Keep `working-copy.eol-conversion` at its default `none`.** It is repo-wide, not per-path,
  and jj's binary detection is NUL-based rather than attribute-based; setting it in lanes would
  change snapshot bytes for every file to solve a problem no repo currently has.
- **Ban `.gitattributes` eol/text/filter rules and `core.autocrlf`/`core.eol` in lane repos.**
  If a specific file ever needs attribute-driven handling, commit it through the Git path
  (`fleet-commit.sh`-style `git add`/`git commit`) and verify `git status --porcelain` is empty
  afterwards, rather than committing it from a jj workspace.
- **Ban Git LFS in lane repos (and anywhere jj commits land).** Treat `filter=lfs` in
  `.gitattributes`, a `.git/lfs/` directory, or `git lfs track` as a stop condition; do not run
  `jj git push` in such a repo. LFS requires the Git CLI end to end until #80 lands.
- **Add a cheap preflight guard outside jj** (jj cannot enforce it): fail lane init/commit when
  `git ls-files | git check-attr --stdin filter eol text` yields anything other than
  `unspecified`, when `.gitattributes` exists, when
  `git config --local --get-regexp '^filter\.'` is non-empty, or when `.git/lfs` exists. This is
  one `git` call and needs no jj invocation.
- **Fleet root stays safe today**: its 8 CRLF CSVs are byte-exact and all its writes go through
  `fleet-commit.sh` (Git), which honors attributes; do not add eol attributes to the fleet root
  while any path is committed through jj.

---

## Open uncertainties

- **Transports.** Every push/clone used a local sandbox bare repo (no real remote push allowed).
  The `--no-verify` flag is unconditional in the argv jj constructs, so hook bypass should be
  transport-independent [INFERENCE], but SSH/HTTPS behavior (including LFS `lfs.url`/auth) was
  not exercised.
- **`jj git clone` over HTTPS.** The local-path clone was `git fetch` + `git remote show` + jj
  checkout; I assume the HTTPS path is the same [INFERENCE], which is what leaves LFS pointers
  on disk. Not separately measured.
- **Version coverage.** Only jj 0.45.1 was executed. The v0.46.0 docs still say `No` for all
  three features and the 0.46.0 CHANGELOG section has no hook/attribute/LFS/eol entry, but no
  0.46 binary was tested.
- **Hook set.** `pre-commit`, `commit-msg` and `pre-push` were probed directly; the docs say
  "Hooks: No" generically and no hook side effect was seen for the other types
  (`prepare-commit-msg`, `post-commit`, `post-checkout`, `post-merge`,
  `reference-transaction`), which were not individually instrumented.
- **Attribute drivers.** `eol`, `filter`, `ident`, `binary` (`-diff -merge -text`) were probed.
  A custom `merge=` driver was not exercised directly; jj's conflict engine is jj-native, so an
  attribute-selected merge driver cannot apply [INFERENCE from the docs plus the `binary` test].
- **Issue states** (#53, #80, #405: all Open) came from the HTML issue pages; the GitHub API was
  rate-limited (HTTP 403) for this host.
- **Census limits.** The live audit counted tracked `.gitattributes` and non-sample hooks; an
  ignored/untracked `.gitattributes` in some working directory was not enumerated (same
  limitation recorded in `.ufo/waves/kaika-w2j/docs-compat.md`, which reached the same
  doc-level conclusions without runtime tests — this report supplies the missing experiments).
- **`git lfs` version.** Measured with git-lfs 3.8.0 using `filter.lfs.process` and
  `filter.lfs.required=true`; jj ignores all filter config regardless, but older LFS versions
  install a slightly different hook set.

## Installs / cleanup

No tool was installed or upgraded; `jj 0.45.1`, `git 2.56.0` and `git-lfs 3.8.0` were already
present. The sandbox `/fast/scratch/jj-wave/JjDocHooksAttributes/` was removed after the
experiments; every output cited above is pasted verbatim. No live repository was written, staged,
fetched, checked out or pushed to a real remote.
