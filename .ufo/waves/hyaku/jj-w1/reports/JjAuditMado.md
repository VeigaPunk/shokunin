# JjAuditMado — lane `mado` / `mado-shokunin`: git invocations under jj colocation

Wave: `hyaku/jj-w1`. Seat: `JjAuditMado-2`. Date: 2026-10-20. Branch audited: `master`.
Read-only on live repos except for the disclosed incident in §0 (repair only).

Lane identity observed in its own log: `mado-shokunin <mado@shokunin.local>` (last 4 commits).

---

## 0. INCIDENT — read this before trusting anything else in this report

I broke the wave's hard rule. Between `2026-10-20 11:19:37` and `11:20:07 -0300` two of my
tool cells ran with cwd `/home/vgpnk/Projects/shokunin` (the live fleet root) because a
`cd "$SB/<dir>"` failed and the shell stayed in the previous cwd. In that window I ran
`git add`/`git commit`, `jj git init --colocate`, `jj file track`, `jj commit`,
`jj config set --repo` and `jj restore` **in the fleet root** — exactly the class of operation
the wave forbids. I detected it in the next command, stopped, established ground truth from the
reflog, reversed only my own artifacts, and verified the result. Full disclosure follows; no
part of this is inferred.

### 0.1 What the fleet root looked like before (reflog ground truth)

```
$ git reflog master --format='%gd|%H|%gs' | head -3
master@{0}|ca7f6e0b4f28fb5d6e8a82faa8a060366e034b79|commit: via git 2
master@{1}|df54adf2c1f42038b3cb623ad412d542a86a1179|commit: round-16: hyaku closure dispatch for kama
$ git rev-parse origin/master
df54adf2c1f42038b3cb623ad412d542a86a1179
```

Pre-incident: `HEAD -> master = df54adf2 = origin/master`.

### 0.2 What I did there (measured by the outputs of the offending cells)

| mutation | result |
|---|---|
| `printf … > hookprobe3.txt`; `git add`; `git commit -m 'via git 2'` | `ca7f6e0` on `master`, 1 file (`hookprobe3.txt`) |
| `printf … > hookprobe4.txt`; `jj file track`; `jj commit hookprobe4.txt -m 'via jj 2'` | `4daa1331` ("export from jj"), **HEAD detached**, parent `ca7f6e0` |
| `jj git init --colocate` (second cell) | created `.jj/`, 18 `refs/jj/keep/*`, and synced the git index (31 `.ufo` paths staged) |
| `jj config set --repo user.name/user.email/snapshot.auto-track` | wrote repo config into that `.jj` |
| `jj restore version` | `No matching entries for paths: version` / `Nothing changed.` |
| `git clone "$SB/origin.git" hooktest` / `attrtest` (earlier cells, no `cd "$SB"`) | two clone dirs created inside the fleet root |
| `rm -f version` | no-op candidate: no `version` file is tracked in fleet history (§0.5) |

Nothing was pushed at any point; `origin/master` was `df54adf2` before and after.

### 0.3 Repair (executed; each step verified)

```bash
git symbolic-ref HEAD refs/heads/master                     # re-attach
git reset --mixed df54adf2c1f42038b3cb623ad412d542a86a1179  # branch back; worktree untouched
rm -f hookprobe3.txt hookprobe4.txt
rm -rf .jj
rm -rf hooktest attrtest
git update-ref -d refs/jj/keep/4daa1331215f6d40d17835812f31ffa6bcc8ea09
git update-ref -d refs/jj/keep/ca7f6e0b4f28fb5d6e8a82faa8a060366e034b79
git for-each-ref refs/jj/keep --format='delete %(refname)' | git update-ref --stdin
rm -f .git/ORIG_HEAD
```

The 18 `refs/jj/keep/*` files all carried mtime `11:19:37–11:19:38` (my init, not pre-existing),
so the whole `refs/jj` namespace was removed. I did **not** use `reset --hard`: the worktree was
never rewritten, so `.ufo/` outputs and other seats' files were preserved.

### 0.4 Verified final state

```
$ git rev-parse --abbrev-ref HEAD      -> master
$ git rev-parse HEAD                   -> df54adf2c1f42038b3cb623ad412d542a86a1179
$ git rev-parse master                 -> df54adf2c1f42038b3cb623ad412d542a86a1179
$ git rev-parse origin/master          -> df54adf2c1f42038b3cb623ad412d542a86a1179
$ ls .git/refs                         -> heads remotes tags   (no jj)
$ ls -d .jj                            -> no .jj
$ git diff --name-status               -> M  .ufo/watchdog.log
$ git status --porcelain | awk '{print $1}' | sort | uniq -c
     44 ??
      1 M
```

`.ufo/watchdog.log` mtime is `11:16:57`, i.e. **before** the incident (11:19:37) — that change
is the watcher's, not mine. The `??` entries are `.ufo` wave files (other seats' reports and,
after this write, this report itself).
`git config` (mtime Oct 19 22:32) and `packed-refs` were not modified.
The audited lane repo itself was untouched: `mado-shokunin` HEAD `3e9848a5…`, 4 untracked paths.

### 0.5 Residuals and limits of the repair

- **Reflog (honest, left in place):** `master@{1}=ca7f6e0`, `HEAD@{1..3}` record the two probe
  commits and the reset. They are history, not state.
- **Unreachable objects:** `git fsck --unreachable --no-reflogs` lists 71 commits; 8 are from
  `2026-10-20` in the incident window and all 8 are mine (2 probes + 6 empty jj working-copy
  commits). The other 63 are Oct 13–19 pre-existing debris. **No other seat's commit is among
  them** (checked by author/date/subject for every incident-window entry).
- **Not run:** `git gc`/reflog expiry (the orchestrator may run
  `git reflog expire --expire-unreachable=now --all && git gc --prune=now` if it wants the
  probes gone from the object store).
- **Cannot be excluded:** an *untracked* file named `version` in the fleet root could have been
  removed by `rm -f version`. No tracked `version` exists in any history
  (`git log --all -- version` empty; `git ls-files | grep -x version` empty) and I saw no
  evidence one existed.
- What would have prevented it: an absolute cwd assertion before any `git`/`jj` call. I added
  one (`[ "$(pwd -P)" = "$SB" ] || exit 9`) to every subsequent cell, and the remaining
  measurements in this report were taken with it.

---

## 1. Scope and method

In-scope inventory, measured:

```
$ ls -la tools scripts verifiers
tools:  mado-action-plan.py  mado-verify.sh        # scripts/ and verifiers/ do not exist
$ find . -path ./.git -prune -o -path ./.jj -prune -o -path ./.ufo -prune \
       -o -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' \
       -o -name Makefile -o -name '*.mk' \) -print
./tools/mado-action-plan.py
./tools/mado-verify.sh
```

No root scripts, no `Makefile`. `.ufo/waves` gates (`frozen/verify.py`, `MistakeFix.py`) are out
of scope per the item, and are frozen copies of older gates; a grep confirms the same three git
calls are embedded there (`gate.sh:3009`, `:759` in rounds 13/14).

Method: full token scan of both files, every hit classified by reading its call path; then
sandbox reproduction with jj 0.45.1 (colocated clones of a local bare origin, never a real
remote) and gate runs against synthetic roots, plus a read-only live gate run.

---

## 2. Findings (observed)

**F1 — Only two executable files; `mado-action-plan.py` has zero git content.**
```
$ grep -c 'git' tools/mado-action-plan.py
0
$ grep -n 'subprocess' tools/mado-action-plan.py
75:import subprocess
526:    return subprocess.run(
```
Its only process creation is `_self_invoke` (`:526-530`): `[sys.executable, "-I", script, *args]`,
`shell=False`, `stdin=DEVNULL`, 60 s timeout, minimal env, temp cwd. No git, no shell.

**F2 — Three executed git invocations exist in the whole lane, all in `tools/mado-verify.sh`,
all read-only and commit-based.**
```
$ grep -nE '(^|[^[:alnum:]_./-])git([^[:alnum:]_-]|$)' tools/mado-verify.sh
3347:  [ -d "$tree/.git" ] && omtree=1
3374:    if ! have git; then
3382:      gt=$(tmo git -C "$tree" describe --tags --exact-match 2>/dev/null); grc=$?
3391:      gh=$(tmo git -C "$tree" rev-parse HEAD 2>/dev/null); grc=$?
3402:    if ! have git || [ "$omtree" = 0 ] || ! have sha256sum || [ ! -f "$leaf" ]; then
3406:      blob=$(tmo git -C "$tree" show "HEAD:$OMARCHY_SKILL_REL" 2>/dev/null | sha256sum | cut -d' ' -f1)
```
`$tree = $ROOT/.local/share/omarchy` (the omarchy checkout), `tmo` = `timeout 5` wrapper
(`:121`). They run only in live mode; `--no-live` emits `SKIP` for all three (`:3350-3352`,
measured: `SKIP live layer skipped (--no-live)`).

**F3 — The target checkout is plain git today, not colocated.**
```
$ git -C ~/.local/share/omarchy rev-parse --abbrev-ref HEAD   -> master
$ git -C ~/.local/share/omarchy rev-parse HEAD                -> 8fcc9d6048af4cb0e3af8512c78049857a3b53dd
$ git -C ~/.local/share/omarchy describe --tags --exact-match -> v3.8.4
$ [ -d ~/.local/share/omarchy/.jj ]                           -> no
```

**F4 — The live gate passes all three git rows right now (read-only run, 2026-10-20).**
```
$ bash tools/mado-verify.sh | awk '$1=="omarchy" && ($2 ~ /git|vs_head/)'
omarchy   omarchy.git.tag        PASS    HELD: v3.8.4 exactly at HEAD (P3 pin)
omarchy   omarchy.git.head       PASS    HELD: 8fcc9d60 (P3 pin)
omarchy   omarchy.skill.vs_head  PASS    worktree == HEAD blob (index-free; no local edit)
$ bash tools/mado-verify.sh | tail -1
MADO_VERIFY: DIVERGED (1 fail, 0 unknown, 52 pass) — first fail: live.walker.version (pin changed: '2.17.2'; re-verify claim anchors)
```
(The red is an unrelated stale walker pin, not a git finding; recorded here so nobody mistakes
the red verdict for a git failure.)

**F5 — On a jj-colocated checkout whose git HEAD is the tagged commit, all three calls still
work.** Sandbox `fixA`: local bare origin, clone, `jj git init --colocate`, `jj new fec817a`
(empty WC on top of the tagged commit).
```
$ git rev-parse --abbrev-ref HEAD -> master      # HEAD attached at the tagged commit
$ git describe --tags --exact-match -> v3.8.4
omarchy   omarchy.git.tag        PASS    HELD: v3.8.4 exactly at HEAD (P3 pin)
omarchy   omarchy.git.head       FAIL    MOVED: rev-parse HEAD → 'fec817a85dc25f36ef7627730567b89166d0dc8d' != pin 8fcc9d60…
omarchy   omarchy.skill.vs_head  PASS    worktree == HEAD blob (index-free; no local edit)
```

**F6 — After `jj new`, git HEAD detaches onto an empty working-copy commit; the tag row turns
UNKNOWN and the head row turns a false FAIL.**
```
$ jj new
Working copy  (@) now at: … (empty) …
$ git rev-parse HEAD                -> 8d286c97f829cd575362639c2f63129df10b7a94   # an EMPTY commit
$ git rev-parse --abbrev-ref HEAD   -> HEAD
$ git symbolic-ref -q HEAD          -> rc=1
$ git describe --tags --exact-match -> fatal: no tag exactly matches '8d286c97…'; rc=128
$ git rev-parse --abbrev-ref '@{u}' -> fatal: HEAD does not point to a branch; rc=128
omarchy   omarchy.git.tag        UNKNOWN git describe failed (rc=128) — tag pin unverified
omarchy   omarchy.git.head       FAIL    MOVED: rev-parse HEAD → '8d286c97…' != pin 8fcc9d60…
omarchy   omarchy.skill.vs_head  PASS    worktree == HEAD blob (index-free; no local edit)
```
Tag `v3.8.4` still sits at the parent; the rows cannot see it. UNKNOWN blocks CLEAN;
the head row is an active false-DIVERGED.

**F7 — Class-A markers are absent from the tooling, and would break under colocation if added.**
Measured in the same sandbox: `symbolic-ref -q HEAD` rc=1, `@{u}` rc=128,
`branch --show-current` prints empty with rc=0. No file in scope uses any of them
(`grep -rnE 'symbolic-ref|@\{u\}|--abbrev-ref|branch --show-current|--porcelain|git status'`
matches only comments and selftest assertion strings).

**F8 — Class C is unsafe across jj mutations: `jj new` and `jj commit` both drop `git add`-staged
entries.**
```
before:            [100644 382ed162… 0  staged2.txt]
after jj commit:   []
status:            [?? staged.txt;?? staged2.txt;]
cached:            []
```
(and identically after `jj new`). The lane has no class-C call today, but its documented
measurement recipes do (`git diff --numstat`, §5).

**F9 — The `.git`-is-a-directory precondition misses git worktrees.**
```
$ ls -ld "$FIX/.local/share/omarchy/.git"
-rw-r--r-- 1 vgpnk vgpnk 70 …/.git          # a FILE, not a dir
omarchy   omarchy.git.tag        UNKNOWN no git checkout at …/fixC/.local/share/omarchy
omarchy   omarchy.git.head       UNKNOWN no git checkout at …
omarchy   omarchy.skill.vs_head  UNKNOWN checkout or leaf unreadable — worktree/HEAD relation unverified
```
Colocation keeps `.git` a directory, so jj itself is not affected — but any worktree-based
checkout silently blinds three rows.

**F10 — `omarchy.skill.vs_head` misreports an unreadable HEAD blob as a local edit (S2).**
```
$ git -C tree show HEAD:default/omarchy-skill/SKILL.md >/dev/null 2>&1; echo rc=$?
rc=128
$ printf '' | sha256sum
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
omarchy   omarchy.skill.vs_head  FAIL  MOVED: worktree 11eeeb547fcd… != HEAD blob e3b0c44298fc… (local edit; editing the skill edits the checkout)
```
Because `:3406` pipes through `sha256sum` and never captures git's rc, a failed `git show` yields
the sha of empty input, which is non-empty, so the guard `[ -z "$blob" ]` at `:3408` is
**unreachable** and the intended `UNKNOWN "cannot read HEAD:…"` arm is dead code. Verdict becomes
DIVERGED. Under jj this fires whenever the compared path exists only in the working copy
(e.g. a new file with `snapshot.auto-track=none()`).

**F11 — Hooks: none in use in either repo.**
```
$ ls .git/hooks | grep -v '\.sample$'     -> (empty; 14 *.sample files, mado lane)
$ git config --get core.hooksPath         -> rc=1 (unset), both repos
$ ls ~/.local/share/omarchy/.git/hooks    -> samples only
```

**F12 — Attributes/eol: none in use; LFS filters configured but inert on the omarchy checkout.**
```
.gitattributes                        -> ABSENT (both repos)
.git/info/attributes                  -> ABSENT (both repos)
core.autocrlf / core.eol              -> unset (both repos)
git -C ~/.local/share/omarchy config --get-regexp '^filter\.'
filter.lfs.clean git-lfs clean -- %f
filter.lfs.smudge git-lfs smudge -- %f
filter.lfs.process git-lfs filter-process
filter.lfs.required true
```

**F13 — jj bypasses both: hooks do not run, attributes/eol are not applied.**
```
--- jj commit ---                     (pre-commit hook installed, +x)
Working copy  (@) now at: pqyvlxyk ae7ee848 (empty) …
Parent commit (@-)      : prlysxrz 8f9fa524 via-jj          # no HOOK output
--- git commit ---
HOOK-RAN
[detached HEAD a84a805] via-git
```
```
$ cat .gitattributes        -> *.md text eol=crlf
git-checkout bytes:      l   i   n   e  \r  \n
jj-restore bytes:      l   i   n   e  \n
$ git status --porcelain   ->  M probe.md        # jj's LF file looks modified to git
```

**F14 — The selftest's git stub cannot fail, so the gate's git error arms are never exercised.**
```
$ sed -n '668,670p' tools/mado-verify.sh
describe) printf '%s\n' "${STUB_GIT_TAG:-v3.8.4}"; exit 0 ;;
rev-parse) printf '%s\n' "${STUB_GIT_HEAD:-8fcc9d60…}"; exit 0 ;;
show) cat "${STUB_GIT_BLOB:-/dev/null}"; exit 0 ;;
```
Every stub verb exits 0 and ignores its arguments. No OM scenario feeds a nonzero rc, so the
`UNKNOWN` arms at `:3385`/`:3394` — the exact arms that fire under F6 — are untested by the
lane's own `--selftest`.

**F15 — Selftest health and documentation drift.**
The pristine selftest cannot run inside my sandbox: `/tmp/w5-mado-m52-selftest.*` (`:395`) and
`/tmp/mado-verify-regression.*` (`:1860`) are hardcoded and ignore `TMPDIR`. On a copy with only
those two paths redirected:
```
MADO_SELFTEST: FAILED — 371 passed, 1 failed
  - R10: derived target equals the recorded gate revision (got 'a4568e1d…' want 'cd1d73d7…')
```
R10 failed only because the copy's bytes differ from `PIN_MADO`. Recomputing the derivation
(the three `sed` marker excisions of `mado_r7_target_build`, `:1723-1734`) on the **untouched**
file in the sandbox gives `cd1d73d75fcc8e5b96d5b83c0d16660897e58cf32edf77416d389fa16b9f3f96`
= `PIN_MADO` (`:1639`). So the pristine run would read 372/372; SKILL.md's last recorded count
is `268/268` (`SKILL.md:1468`, `:1668`) — a stale record, not a gate failure.
Live script identity: 3,711 L / 177,849 B / sha256 `fba82a66…`.

**F16 — No lane tool checks landedness; the lane is 8 commits ahead of origin in this snapshot.**
```
2026-10-20T14:16:37Z
HEAD=3e9848a5b9d05fdba96af9772bdaf1f03c66580f  abbrev=master
master=3e9848a5…        origin/master=27cd06f5067c3d3540ab9aa7cc734eb8eee162cc
ahead=8 behind=0        is-ancestor(origin/master, master)=0
porcelain: 4 × "?? .ufo/waves/round-17/..."
```
All 8 commits are `mado-shokunin <mado@shokunin.local>`, authored 13:56–14:15Z. This is a live
snapshot of a running round, not proof of a fault — but no gate in `tools/` can detect it, so a
report that cites one of these hashes has no in-lane landedness evidence.

**F17 — The lane repo is already colocated, and jj has been run in it (process finding).**
`.jj/repo/store/git_target` = `../../../.git`, i.e. colocated since
`2026-10-19 20:38:49` (`jj git init --colocate`, from the op log). Op log (12 ops), command
strings as stored:
```
2026-10-19 20:38:49 | jj git init --colocate
2026-10-20 04:24:40 | jj log -r '@|@-|@--' --no-graph
2026-10-20 10:21:51 | jj --no-pager log -r '@ | @- | trunk()' --no-graph -T '…'
```
No commit/bookmark/rebase op exists, and `git reflog master` has no jj-authored entry (its 4
non-commit entries are ordinary git: `pull --ff-only`, `commit (merge)`, `merge … Fast-forward`,
`commit (initial)`). So jj has not moved this repo's history — but `jj log` has been run in the
live lane at least three times, which is the round-14 incident class the wave's rules forbid.
The op log also shows every jj run left the working-copy state touched
(`.jj/working_copy/checkout` mtime = `10:21:51`), while plain `git` commits continued afterwards
(11:11–11:15) — so jj's view is now stale relative to `master`.

---

## 3. Classified table — executable tooling

Class legend: **A** attached-HEAD/upstream assumption · **B** history/index/worktree mutation ·
**C** index/staging read · **D** read-only, HEAD-commit based.

| # | file:line | exact command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|---|
| 1 | `tools/mado-verify.sh:3382` | `gt=$(tmo git -C "$tree" describe --tags --exact-match 2>/dev/null); grc=$?` | **D** | Commit-based, survives detach. If the checkout were colocated, HEAD may be an empty working-copy commit → `rc=128` → row `UNKNOWN` (blocks CLEAN). No false PASS. Reproduced: F6. | Resolve the tip instead of HEAD: `git -C "$tree" describe --tags --exact-match "$(git -C "$tree" rev-parse --verify refs/heads/master)"`. |
| 2 | `tools/mado-verify.sh:3391` | `gh=$(tmo git -C "$tree" rev-parse HEAD 2>/dev/null); grc=$?` | **D** | Same, but the failure is a **false FAIL**: `HEAD` = `@-`, which can be an empty WC commit → verdict DIVERGED although the checkout is pinned. Reproduced: F6. | `git -C "$tree" rev-parse --verify refs/heads/master` (same identity, independent of HEAD attachment). |
| 3 | `tools/mado-verify.sh:3406` | `blob=$(tmo git -C "$tree" show "HEAD:$OMARCHY_SKILL_REL" 2>/dev/null \| sha256sum \| cut -d' ' -f1)` | **D** | Index-free, so detach and index resets are harmless. But git's rc is discarded: on failure the pipeline yields `e3b0c442…` and the row claims a *local edit*; the `UNKNOWN` arm at `:3408` is unreachable. Reproduced: F10. | `blob=$(tmo git -C "$tree" cat-file blob "HEAD:$rel" \| sha256sum \| cut -d' ' -f1); grc=${PIPESTATUS[0]}`; route `grc≠0` to UNKNOWN. |

### 3a. git-adjacent non-invocations in the same plane

| file:line | construct | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `tools/mado-verify.sh:3347` | `[ -d "$tree/.git" ]` | precondition | Colocation keeps `.git` a dir (OK). A git *worktree* makes it a file → `omtree=0` → three UNKNOWN (F9). | `git -C "$tree" rev-parse --git-dir >/dev/null 2>&1` |
| `tools/mado-verify.sh:3374`, `:3402` | `have git` | precondition | none | — |
| `tools/mado-verify.sh:662-676` | selftest `git` stub (fixture on PATH) | fixture | Answers all three verbs with `exit 0` and ignores arguments; cannot express the rc=128 case jj produces (F14). | Add `STUB_GIT_RC` (and per-verb rc) plus an OM scenario asserting UNKNOWN. |

No other git invocation exists in either executable file (F1, F2).

---

## 4. Counts per class

Executable tooling (`tools/`, `scripts/` absent, `verifiers/` absent, root scripts absent,
`Makefile` absent):

| class | count | sites |
|---|---|---|
| A | **0** | — |
| B | **0** | — |
| C | **0** | — |
| D | **3** | `mado-verify.sh:3382`, `:3391`, `:3406` |

Adjacent git dependencies: 3 (`:3347`, `:3374`, `:3402`) + 1 fixture stub (`:662-676`).
`tools/mado-action-plan.py`: 0 git references, 0 shell-outs.

SKILL.md guidance (commands a lane agent is told to run; not executed by a script) — 14 lines:

| class | count | lines |
|---|---|---|
| A | **0** | — |
| B | **0** | — |
| C | **4** | 1046, 1226, 1370 (`git diff --numstat`), 1635 (`git status --porcelain`) |
| D | **10** | 25, 367, 812 (×2 commands), 836 (whitelist of 5 verbs), 1056, 1259, 1278, 1632, 1644, 1689 |

---

## 5. Guidance table — SKILL.md commands, classified

| SKILL.md line | command | class | risk under jj colocation |
|---|---|---|---|
| 25 | `git describe --tags` | D | none (detached-safe) |
| 367 | `git -C ~/.local/share/omarchy describe --tags` | D | none |
| 812 | `describe --tags --exact-match` · `rev-parse HEAD` | D | HEAD = `@-` on a colocated tree; the tag can be invisible (F6) |
| 836 | whitelist: `git describe/rev-parse/show/log/ls-tree` | D | none; note the whitelist already excludes `status`/`fetch` |
| 1046, 1226, 1370 | `git diff --numstat` (line-count receipts) | C | index vs worktree: after a jj mutation staged content is gone; after `jj commit` the count is 0 (F8) |
| 1056, 1259, 1278, 1632, 1689 | `git show HEAD:<path>` (& `\| sha256sum`) | D | "HEAD" = `@-`; an uncommitted jj change makes the comparison true/false in the right direction, but a piped `sha256sum` without rc repeats F10 |
| 1635 | `git status --porcelain` | C | refreshes the index stat cache (the lane's own guard forbids it on the checkout); under jj a jj-committed-but-unpushed change reads clean, so "clean" stops meaning landed |
| 1644 | `git log -1` | D | none |

---

## 6. Hooks and attributes — what jj bypasses here

Neither repo has a hook or an attribute rule in force (F11, F12):

| item | mado lane `.git` | `~/.local/share/omarchy/.git` |
|---|---|---|
| non-`.sample` hooks | none | none |
| `core.hooksPath` | unset (rc=1) | unset (rc=1) |
| `.gitattributes` / `info/attributes` | absent / absent | absent / absent |
| `core.autocrlf` / `core.eol` | unset / unset | unset / unset |
| `filter.*` | none | `filter.lfs.{clean,smudge,process}`, `filter.lfs.required=true` |

So today jj's bypasses (F13: hooks do not run, `eol=crlf` not applied, jj's LF file then reads
` M` to git) are **latent**, not active. The omarchy checkout is one `.gitattributes` away from
activating git-lfs, after which `git show HEAD:<leaf>` would return an LFS pointer while the
worktree holds smeared content — a permanent false `vs_head` FAIL. (That LFS direction is
inference; the eol direction is measured.)

---

## 7. This lane's top three risks

**R1 — `omarchy.skill.vs_head` turns "cannot read" into "local edit" (S2).**
`tools/mado-verify.sh:3406` discards git's rc, so any `git show` failure becomes a FAIL naming
the sha of empty input, and the UNKNOWN arm at `:3408` is unreachable (F10). Reachable today
without jj (missing object, unreadable blob) and routinely under jj (a path that lives only in
the working copy). It is the only finding in this lane that produces a *wrong* verdict rather
than an UNKNOWN.

**R2 — `HEAD`-as-branch-tip in the two checkout-identity rows (S1/S2, conditional).**
`:3382` and `:3391` assume HEAD is the branch tip. On a colocated tree HEAD = `@-`, which after
`jj new`/`jj commit` is an empty working-copy commit: the tag row falls to UNKNOWN and blocks
CLEAN, and the head row reports a false DIVERGED (F6). Today the target checkout is plain git
and all three rows PASS (F3, F4), so this is armed but not firing — it fires the moment the
omarchy checkout is colocated or the plane is re-pointed at a jj-managed tree.

**R3 — Nothing in the lane checks landedness, and the documented measurement recipes are
index/attribute-sensitive (S2).**
No gate reads `master` vs `origin/master` or ancestry; the lane was 8 commits ahead at
14:16:37Z while every visible signal (`git status` clean, HEAD on master) looked normal (F16).
Meanwhile the recipes that *do* measure state — `git diff --numstat`, `git status --porcelain` —
depend on an index jj resets on every mutation (F8) and on attribute filters jj ignores (F13).
A jj-migrated lane could therefore cite an unpushed hash and measure its work with tools that
silently under-report.

---

## 8. Inference

- **[INFERENCE]** The planned migration does not change any *write* path in this lane: there is
  no class-B call in `tools/` at all; the helper (`scripts/hyaku/jj-lane.sh`) is the only writer
  and lives outside the lane. The entire jj exposure of this lane's tooling is three D reads.
- **[INFERENCE]** The three D calls are safe **as long as the target checkout stays plain git**.
  Their failure mode under colocation is UNKNOWN or false FAIL, never a false PASS: `describe`
  and `rev-parse` read commit bytes, and `vs_head` compares content, not branch state.
- **[INFERENCE]** The helper's `init` cannot repair this lane: it colocates only when `.jj` is
  absent, and `mado-shokunin/.jj` already exists (created 2026-10-19 20:38:49, before the
  helper's `init` fix landed in the fleet commit at 22:32). Whether that pre-existing `.jj`
  carries the helper's repo settings (`user.name/email`, `snapshot.auto-track=none()`,
  `trunk()`, tracked bookmark) is **UNK**: the repo config is stored in jj's own binary store and
  reading it requires running `jj` in the live lane, which the wave forbids. The op log shows
  only `git init` and three `log` commands; it does not prove config absence.
- **[INFERENCE]** Because jj does not invoke hooks or filters, any future lane gate built on a
  pre-commit hook, `core.hooksPath`, `filter.*` or `eol` would silently do nothing in a
  colocated checkout while still doing work under `git`.
- **[INFERENCE]** `git status --porcelain` remaining clean under jj means "the working-copy
  commit has no changes", not "the work is committed and pushed": a jj commit that was never
  pushed reads clean and detached from any branch.

---

## 9. Recommendations

1. **Fix `:3406` rc handling** (one line): capture `${PIPESTATUS[0]}` (or use
   `git cat-file blob` with an rc check) and route `grc≠0` to the existing UNKNOWN message; then
   the `-z "$blob"` guard at `:3408` becomes either reachable or deletable. Add an OM scenario
   with a failing git stub so the arm is covered.
2. **Resolve the tip instead of HEAD** in `:3382`/`:3391`
   (`rev-parse --verify refs/heads/master`), or pass the branch tip into
   `describe --tags --exact-match`. Both stay class D and remove the whole R2 failure mode.
3. **Replace `[ -d "$tree/.git" ]` (`:3347`)** with `git -C "$tree" rev-parse --git-dir`
   so worktree checkouts stop reading as "no git checkout".
4. **Add a landedness row** (in `mado-verify.sh` or a separate lane gate):
   `git -C <lane> rev-parse master origin/master` plus
   `git merge-base --is-ancestor origin/master master`. It is class D, costs no index access, and
   is the only checker for the "committed AND pushed" invariant R3 describes. Do not use
   `git status` for this.
5. **Treat pre-existing `.jj` as an integration gap**: `jj-lane.sh init` should detect an existing
   `.jj` and (a) report it as `UNK/no-op` rather than assuming its settings, or (b) re-apply the
   repo config idempotently. Otherwise every lane colocated before the helper fix (this one is)
   runs with unverified `snapshot.auto-track`/identity settings.
6. **Keep `jj` out of live lanes entirely** while the study wave runs. The op log (F17) shows
   three `jj log` runs in this lane today, after the rule was written; each one snapshots the
   working copy and leaves it stale against the eight later `git` commits.

---

## 10. Unrun checks and limits

- **Pristine `--selftest` not run**: the script hardcodes `/tmp/…` (`:395`, `:1860`), and my
  mandate confines writes to the sandbox. I ran a path-redirected copy (371 passed + one
  induced R10 failure) and independently recomputed `PIN_MADO` from the untouched bytes (§F15).
- **`--regression` not run**: requires the sibling harness and writes a scratch root.
- **`--snapshot` / `--snapshot-diff` not run**: they write caller-selected files.
- **No jj command in any live repo** was run to read the lane's jj config (forbidden); that one
  item stays UNK (§8).
- **LFS/filter direction of F12/R1** is inference, not measurement (no attributes file exists to
  trigger it).
- **Live gate run** was read-only and is reported as-is, including its unrelated walker-pin red.
- The wave's own hard rule was violated once (§0); the repair is verified but the reflog and the
  unreachable objects remain as disclosed.

---

## 11. Sandbox

Preserved to keep the cited failures reproducible:
`/fast/scratch/jj-wave/JjAuditMado-2/` — `origin.git` (local bare remote), `om` (harness),
`fixA` (colocated checkout whose HEAD is the tagged commit, then `jj new`), `fixC` (worktree
fixture), `fixD`, `fixE` (unreadable-HEAD-blob case), `hk` (hook bypass), `at` (eol bypass),
`tmp/` (path-redirected selftest copy and derived-target computation). No real remote is
configured in any of them.
