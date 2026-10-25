# JjAuditTameshi — every git invocation in lane `tameshi`'s tooling, classified for jj colocation

Seat: JjAuditTameshi-2 · 2026-10-20 · branch `master` · read-only audit.
Sandbox for every jj command: `/fast/scratch/jj-wave/JjAuditTameshi-2/` (kept: it preserves the
three reproductions cited below). No `jj` command ran with cwd or `-R` inside
`/home/vgpnk/Projects/shokunin` or any lane repo.

Tools used: jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, git `2.56.0`. No installs.

## 0. Scope actually found

| Requested scope | Present? | Files audited |
|---|---|---|
| `tools/` | yes, 7 files | `mutate-and-run.sh`, `bash-witness-study.py`, `context-capture.py`, `evidence-disposition.py`, `pin-disposition.py`, `repeat-control.py`, `witness-metadata.py` |
| `scripts/` | **absent** | — |
| `verifiers/` | **absent** | — |
| root `*.sh *.py *.mjs *.js Makefile` | **absent** | — |
| gates/selftests named in SKILL.md | yes | `tools/*.py` above; `.ufo/evidence/round-14/capture-context.py` (historical, "do not run", SKILL.md:1602/1623); `.ufo/evidence/round-16/measure.py`, `.../coldread/assemble.py`, `.../attribution/reattribute.py`; `.../round-gate/survivor-probes/probes.mjs` (named at SKILL.md:1790) |
| adjacent verifier in a named gate dir | yes | `.ufo/evidence/round-16/coldread/anchor-check.py` (not named in SKILL.md) |
| `corpus/` | 39 `.md`, no scripts | — |

`assemble.py` and `reattribute.py` contain **zero** git invocations (`grep -c -i git` = 0), as do
`evidence-disposition.py`, `repeat-control.py`, `witness-metadata.py`.

Live repo state at start (11:09Z-ish): `HEAD=c699c8c36d6e…` on attached `refs/heads/master`,
`.jj/repo/store/git_target` = `../../../.git`, `.jj/repo/store/type` = `git` (colocated),
`git for-each-ref refs/jj` = 7 `refs/jj/keep/*` commits. The lane is live: at 14:18Z `HEAD` was
`05a224754db3…` (round-16 wave-2 landed while this audit ran). Observations are timestamped where
they can drift.

## 1. Classification of every git call site

Class legend (from the assignment):
**A** = assumes an attached branch HEAD/upstream · **B** = mutates history/index/worktree ·
**C** = reads index/staging state · **D** = read-only, revision-addressed.
"Risk under jj colocation" is the observed behaviour, not a guess; every claim marked *[obs]* has a
command + output excerpt in §2.

### 1.1 `tools/mutate-and-run.sh` (the ledger engine)

| file:line | exact command | cls | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `tools/mutate-and-run.sh:1000` | `git -C "$repo" rev-parse --verify --quiet "${rev}^{commit}"` | D | none for the rev itself; *[obs]* rev-addressed reads work detached. **But** `-C` has no repo-identity guard, so a lane without `.git` silently resolves in the fleet super-repo (§2.2). | keep command; prepend `repo_identity` guard (`rev-parse --show-toplevel` realpath == repo realpath) as `pin-disposition.py:235-265` already does. |
| `tools/mutate-and-run.sh:1004` | `git -C "$repo" cat-file -e "${rev}:${path}"` | D | same super-repo fallback; object read itself is filter-free. | same guard; or `jj --repository "$repo" file show -r "$rev" "$path"`. |
| `tools/mutate-and-run.sh:1009` | `git -C "$repo" show "${rev}:${path}" >"$dst"` | D | safe detached; raw blob (no eol/filter applied). | keep; guard. `cat-file blob` is equivalent and narrower. |
| `tools/mutate-and-run.sh:1018` | `git -C "$repo" ls-tree "$rev" -- "$path" \| awk '{print $1}'` | D | safe; tree read by rev, independent of HEAD and index. | keep; guard. |
| `tools/mutate-and-run.sh:1533` | `grev=$(git -C "$grepo" rev-parse HEAD)` | D | fixture repo under `mktemp -d /tmp` (no `.jj`) → attached; no risk. If reused on a lane after a jj commit it returns `@-`, not the bookmark. | fixture: keep. Lane: `git rev-parse --verify --quiet "refs/heads/$branch^{commit}"`. |
| `tools/mutate-and-run.sh:1592` | `grev_exec=$(git -C "$grepo" rev-parse HEAD)` | D | as above (fixture). | as above. |
| `tools/mutate-and-run.sh:1593` | `git -C "$grepo" show "$grev_exec:exec.sh"` | D | fixture; safe. | keep. |
| `tools/mutate-and-run.sh:1627` | `grev_noexec=$(git -C "$grepo" rev-parse HEAD)` | D | fixture; safe. | keep. |
| `tools/mutate-and-run.sh:1628` | `git -C "$grepo" show "$grev_noexec:noexec.sh"` | D | fixture; safe. | keep. |
| `tools/mutate-and-run.sh:1529` | `git -C "$grepo" init -q` | B | fixture only (`$root/fleet/fakerepo`, `$root=$(mktemp -d /tmp/tameshi-r4-2-selftest.XXXXXX)`, :1262). No `.jj` ancestor. | keep; optionally `-c init.templateDir=`/`core.hooksPath=` to neutralise host hooks. |
| `tools/mutate-and-run.sh:1530` | `git -C "$grepo" add -A` | B | fixture only; index writes are local to the fixture. | keep. |
| `tools/mutate-and-run.sh:1531` | `git -C "$grepo" -c user.name=… -c user.email=… -c commit.gpgsign=false commit -q -m selftest-fixture` | B | fixture only. | keep. |
| `tools/mutate-and-run.sh:1588` | `git -C "$grepo" add exec.sh` | B | fixture only. | keep. |
| `tools/mutate-and-run.sh:1589` | `git -C "$grepo" -c … commit -q -m selftest-fixture-exec` | B | fixture only. | keep. |
| `tools/mutate-and-run.sh:1623` | `git -C "$grepo" add noexec.sh` | B | fixture only. | keep. |
| `tools/mutate-and-run.sh:1624` | `git -C "$grepo" -c … commit -q -m selftest-fixture-noexec` | B | fixture only. | keep. |

Non-call git references here: `command -v git` at `:996` and `:1159` (capability probes, not
invocations); `GIT_CONFIG_NOSYSTEM=1` / `GIT_CEILING_DIRECTORIES="$h"` in the round-gate suite
string at `:1222` (defensive env for the mutant, not a git call).

### 1.2 `tools/pin-disposition.py` (six-leg content disposition)

| file:line | exact command | cls | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `tools/pin-disposition.py:255` | `git_run(repo_real, ["rev-parse","--show-toplevel"])` | D | safe; repo discovery is HEAD-independent. This is the **only** tool with a super-repo guard (`repo_identity`, :235-265). | keep (it is the model for the fix in §1.1). |
| `tools/pin-disposition.py:278` | `git -C repo rev-parse --verify --quiet --end-of-options <commit>^{commit}` | D | safe detached; explicit 40-hex. | keep; (optional) `jj --ignore-working-copy log -r <commit>`. |
| `tools/pin-disposition.py:288` | `git -C repo cat-file -t <commit>:<path>` | D | safe. | keep. |
| `tools/pin-disposition.py:296` | `git -C repo cat-file blob <commit>:<path>` | D | safe; raw bytes, no attributes. | keep. |
| `tools/pin-disposition.py:317` | `git -C repo rev-parse --verify --quiet --end-of-options HEAD^{commit}` | D | **semantic drift.** HEAD is `@-`, which after `jj new`/an in-progress change is a jj working-copy snapshot commit that is not the branch bookmark; *[obs]* `master..HEAD` = 1 and `HEAD:file.txt` carried an unpushed `dirty` line (§2.3). The row's `head`/"current" classification can therefore call unpushed snapshot bytes current. | resolve the branch: `git rev-parse --verify --quiet --end-of-options "refs/heads/master^{commit}"` (or `<branch>@origin`); add `git merge-base --is-ancestor "$rev" refs/heads/master`. |
| `tools/pin-disposition.py:329` | `git -C repo cat-file -t <head>:<path>` | D | inherits the `:317` commit choice only. | use the same bookmarked commit. |
| `tools/pin-disposition.py:341` | `git -C repo cat-file blob <head>:<path>` | D | inherits the `:317` commit choice only. | as above. |
| `tools/pin-disposition.py:702,704,705,710,711,715,716,723,726,727,731,732` | selftest fixture helper `git()` (`:667-695`, neutralises `core.hooksPath`, `init.templateDir`, global config) → `init`, `add`, `commit`, `add`, `commit --allow-empty`, `add`, `commit`, `init`, `add`, `commit`, `add -A`, `commit` | B | fixtures only, under `tempfile.mkdtemp(prefix="tameshi-r13-pin-disposition-selftest.", dir="/tmp")` (:604). Host hooks/templates already neutralised. | keep. |
| `tools/pin-disposition.py:706,712,717,728,733` | `git(fleet/kumitate/kagi, ["rev-parse","HEAD"])` | D | fixture repos, attached; safe. | keep. |

### 1.3 Remaining tooling

| file:line | exact command | cls | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `tools/bash-witness-study.py:338` | `git -C <kagi> show --end-of-options <rev>:corpus/surface-census.sh` | D | safe; explicit rev, `.git` or `.jj` presence checked at :335. | keep; `cat-file blob` if filters were ever a concern (they are not for `show`). |
| `tools/context-capture.py:1447` | `control_argv = ["/usr/bin/git","-C",lane,"rev-parse","--git-dir"]` | **literal, not executed** by this tool (fixture receipt data only) | none; the actual control ran in round-14 `capture-context.py`. | none needed. |
| `tools/repeat-control.py`, `tools/evidence-disposition.py`, `tools/witness-metadata.py` | — | — | no git invocations | — |

### 1.4 Gates named in SKILL.md (`.ufo/evidence/…`)

| file:line | exact command | cls | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `.ufo/evidence/round-14/capture-context.py:400` (executed twice at `:402-403`) | `[git_path, "-C", LANE_ROOT, "rev-parse", "--git-dir"]` (positive control, baseline + injected env) | D | safe; repo discovery, no HEAD/branch assumption. Works because colocation keeps `.git`. | keep. |
| `.ufo/evidence/round-16/measure.py:79→:85` | `subprocess.run(['git','-C',repo,'show','<rev>:<path>'])` via `blob()` | D | safe; default `--repo` is the live lane, but every read is rev-addressed. | keep; optionally guard identity (default repo is the lane itself, so low risk). |
| `.ufo/evidence/round-16/measure.py:612` | `git -C <repo> rev-parse --verify --quiet <rev>^{commit}` | D | safe. | keep. |
| `.ufo/evidence/round-16/measure.py:418,419,429` | selftest `git_in(repo,'add','-A' / 'commit' / 'init')` under `tmp` with `HOME=tmp` | B | fixture only. | keep. |
| `.ufo/evidence/round-16/coldread/anchor-check.py:41` | `subprocess.run(["git","-C",REPO,"show",f"{rev}:{path}"], check=True)` with fixed revs `c699c8c…`, `e69b488` | D | safe while the objects exist; both were resolvable during the audit (`c699c8c` was `master` at start, and `refs/jj/keep` protects jj-known commits). | keep; if the rev is ever rewritten, re-pin. |
| `.ufo/evidence/round-16/round-gate/survivor-probes/probes.mjs:24` | `spawnSync('git', ['-C', cwd, ...args])` wrapper | D | wrapper only. | — |
| `probes.mjs:28` | `git(dir,['init','-q','-b','main'])` | B | fixture under `ROOT` default `/tmp/tameshi-r16-survivorprep/fx`; **`FXROOT` env override** + `rmSync(...,{recursive:true,force:true})` in `fresh()` (`:31`) means pointing `FXROOT` at a live tree deletes it. | keep default; refuse `FXROOT` paths under the fleet root. |
| `probes.mjs:30` | `git(dir,['add','-A'])`, `git(dir,['commit','-q','-m',msg])`, `git(dir,['rev-parse','HEAD'])` | B (D read) | fixture only. | keep. |
| `probes.mjs:144` | `git(lane,['reset','--hard','HEAD~1'])` | B | fixture only (`lane` under `base`/`fresh`). | keep; same `FXROOT` guard. |
| `probes.mjs:145` | `spawnSync('git',['-C',lane,'cat-file','-e',`${shaB}^{commit}`])` | D | fixture; safe. | keep. |
| `probes.mjs:187,189,190` | `git init --bare -q -b main <bare>`, `git remote add origin <bare>`, `git push --quiet -u origin main` | B | fixture bare remote under `/tmp`; no real remote. | keep. |
| `probes.mjs:322,324,325` | same init/remote/push trio for the second probe | B | fixture. | keep. |
| `probes.mjs:400` | `git(main,['add','-A'])`, `git(main,['commit','-q','-m','filed reports'])` | B | fixture. | keep. |

Adjacent, **not** named in SKILL.md and not counted: `.../survivor-probes/c1059-probe.sh` (init/add/
commit at :63, :77, :78-81 — all inside `SCRATCH=$(mktemp -d /tmp/tameshi-r16w2-c1059-XXXXXX)`,
:27, with `trap rm -rf`), and the ~80 other `.ufo/evidence/**` scripts (evidence copies, out of the
named-gate scope).

## 2. Observed evidence for the risk column

All commands below ran in `/fast/scratch/jj-wave/JjAuditTameshi-2/`; `exp1` = colocated clone,
`exp2` = super-repo discovery, `exp3` = hooks/filters/index.

### 2.1 jj mutates detach HEAD; read-only jj commands do not

```
after init: refs/heads/master
after jj log: refs/heads/master
after jj st: refs/heads/master
after jj commit: DETACHED
after git commit on detached: DETACHED head=22bf2dd4… master=3d0138ca…
after git checkout master: refs/heads/master head=3d0138ca… master=3d0138ca…
```

Post-`jj commit` probes: `git symbolic-ref -q HEAD` → exit 1; `git rev-parse --abbrev-ref HEAD` →
`HEAD`; `git rev-parse '@{u}'` → `fatal: HEAD does not point to a branch`; `git rev-parse HEAD`
still returns the commit; `git rev-parse master` returns the bookmark. The live lane is currently
attached; the only jj command string retained in its op store is a read-only `jj log`
(`.jj/repo/op_store/operations/d0521bb3…`), and §2.1 shows read-only jj commands do not detach.
[INFERENCE] No mutating jj command has yet run in the live lane; the first `jj commit`/`jj new`
will detach it.

### 2.2 A lane without `.git` is read from the fleet super-repo (no guard in mutate-and-run.sh)

`exp2/super` is a git repo; `exp2/super/lane` has no `.git`:

```
$ git -C lane rev-parse --show-toplevel
/fast/scratch/jj-wave/JjAuditTameshi-2/exp2/super
$ git -C lane show e591be15…:lane/file.txt
super-bytes
$ [ guard: realpath(toplevel) == realpath(lane) ] → GUARD-REFUSES (foreign)
```

`pin-disposition.py:235-265` implements exactly that guard; `mutate-and-run.sh:1000-1035` does not.
If any sibling lane moves to a non-colocated jj store (`.git` removed), the seven-leg ledger reads
the super-repo instead — `cat-file -e` fails as SETUP at best, or a same-named rev:path resolves
from the wrong store at worst.

### 2.3 HEAD can be a jj working-copy snapshot commit that is not on the branch

`exp1/work` after `jj new` + an edit:

```
master..HEAD count=1
HEAD tree file.txt=v3|dirty|
master tree file.txt=v3|
HEAD descends from master
```

So `git show HEAD:<path>` / `rev-parse HEAD^{commit}` return bytes/identity one commit ahead of
`master`, never pushed. `SKILL.md:1033`'s `current = git show HEAD:<path>` row and
`pin-disposition.py:317`'s `head_observation` inherit this.

### 2.4 Pinned object reads survive both GCs; the already-colocated sibling proves it in production

Sandbox: explicit-rev reads survived `git gc --prune=now` and
`jj util gc --expire=now`; `git for-each-ref refs/jj` stayed at 6 in `exp1`.

Live sibling `mado-shokunin` (already colocated: `.jj` and `.git` both present):
```
$ git -C mado-shokunin rev-parse --verify --quiet 'eead56b2…d0e13^{commit}'   → eead56b2…  (exit 0)
$ git -C mado-shokunin show eead56b2…:tools/mado-verify.sh | sha256sum
d7edaab4bf108625d213393b77432d7c0104daaa487c801fbc8bba16e32d0e13  -
```
That equals `PIN_MADO` (`tools/mutate-and-run.sh:557`), so the D-class path is empirically intact
under colocation today. `kagi`'s pinned leg likewise re-hashes to `PIN_BASH` (`275d8294…`).

### 2.5 Hooks and attribute filters: jj bypasses both

`exp3/repo` (colocated), `.git/hooks/pre-commit` writing `hook-ran.txt`:

```
jj commit -m 'via jj'   → hook NOT run under jj
git commit -qam 'via git' → hook ran under git: ran
```

`.gitattributes` `* filter=upper`, `filter.upper.clean = tr a-z A-Z`:

```
git blob: VIA-GIT
jj blob: via-jj
```

Raw `jj` bytes go into the git object store without the clean filter. `git show`/`cat-file` of a
pinned rev are unaffected either way (they never consult attributes).

### 2.6 jj resets the git index on commit-boundary mutations, not on reads

```
before jj new:   cached=[a.txt b.txt]
after jj new:    cached=[]
before jj commit:cached=[a.txt]
after jj commit: cached=[]
```

`jj st` alone did **not** clear a staged entry. No in-scope call site reads or writes the index, so
this is contextual only.

### 2.7 The live lane's jj repo config has no `snapshot.auto-track`

jj 0.45 stores repo-level config **outside the repo**, per repo path:
`jj config path --repo` → `/home/vgpnk/.config/jj/repos/86a634125f04a8756fc6/config.toml`
(metadata: `/home/vgpnk/Projects/shokunin/tameshi-shokunin/.jj/repo`, mtime
`2026-10-19 20:39:15 -0300`). Its full content:

```toml
[revset-aliases]
"trunk()" = "master@origin"
"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"

[user]
name = "tameshi-shokunin"
email = "tameshi@shokunin.local"
```

`grep -c auto-track` = **0**. `mado-shokunin`'s live config (`b7d9811b…`) is the same shape, also
without the key. The helper's `cmd_init` sets it (`jj --ignore-working-copy config set --repo
snapshot.auto-track '"none()"'`, helper `:152`), but `cmd_commit` only checks `-d "$dir/.jj"`
(helper `:186`) — so a commit before `init` runs uses jj's default auto-track. This is the
round-14 mado incident shape; at 14:18Z the lane had 2 untracked paths (earlier in the round it
had 20+).

Aside: my sandbox `jj config set --repo` wrote one such external config dir; I removed it
(`~/.config/jj/repos/9bf392363315a585a38d`) after recording the path semantics. That accidental
residue is itself the durability finding: repo config does not travel with the repo.

## 3. Counts per class

Static call sites (one row per line; a line with two git calls counts once per line):

| Class | `tools/` | named gates | named harness `probes.mjs` | adjacent `anchor-check.py` | **Total** |
|---|---|---|---|---|---|
| **A** attached-HEAD/upstream assumptions | 0 | 0 | 0 | 0 | **0** |
| **B** history/index/worktree mutations | 19 | 3 | 10 | 0 | **32** |
| **C** index/staging reads | 0 | 0 | 0 | 0 | **0** |
| **D** read-only, revision-addressed | 22 | 3 | 1 | 1 | **27** |
| literal, not executed | 1 (`context-capture.py:1447`) | — | — | — | **1** |

Executed call sites: **59** (A0 · B32 · C0 · D27). Of the 32 B sites, **0** run against a live
repo: 19 are in `tools/` selftests under `mktemp -d /tmp` (7 in `mutate-and-run.sh`, 12 in
`pin-disposition.py`), 3 in `measure.py`'s `mkdtemp`, 10 in `probes.mjs` under its `/tmp` fixture
root. Primary tooling alone (`tools/` + named gates, no
harness/adjacent): **47** sites — A0 · B22 · C0 · D25.

## 4. Git hooks and attributes in use

Lane repo `/home/vgpnk/Projects/shokunin/tameshi-shokunin`:

| Mechanism | State | Evidence |
|---|---|---|
| `.git/hooks/*` | **only `*.sample`** (13 files, all `.sample`); zero active hooks | `ls -la .git/hooks/` |
| `core.hooksPath` | unset in every scope | `git config --get core.hooksPath` → exit 1 |
| `.gitattributes` (repo tree) | **none anywhere** | `find . -name .gitattributes -not -path './.git/*'` → empty |
| `.git/info/attributes` | absent | `ls .git/info/` → `exclude`, `refs` |
| `core.attributesFile` | unset | `git config --get core.attributesFile` → exit 1 |
| `git check-attr -a -- tools/mutate-and-run.sh` | no attributes | empty output, exit 0 |
| global config filters | `filter.lfs.clean/smudge/process` + `filter.lfs.required=true` exist in `~/.config/git/config`, but **no `.gitattributes` binds `filter=lfs` to any path** | `git config --list --show-origin \| grep -i filter` |
| eol rules (`core.autocrlf`, `core.eol`, `text=`) | none set, no attributes | same config listing |

Fleet root `/home/vgpnk/Projects/shokunin`: `.git` present, `.jj` absent. Siblings: `mado` is
already colocated (`.jj`+`.git`); `kagi`, `kumitate`, `tsukuroi` are git-only. None of the four has
a non-sample hook, `hooksPath`, or a repo-local `.gitattributes` (checked with `find`/`grep` on
`.git/config`; no git write verbs run there).

Because both mechanisms are empty today, the jj bypass demonstrated in §2.5 has **zero current
behavioural effect** in this lane. It becomes live the moment a commit hook, an LFS/text/eol
attribute, or a `core.hooksPath` is introduced: git-path commits would run them, jj-path commits
would not, silently.

## 5. This lane's top three risks

**R1 — `mutate-and-run.sh` reads `git -C "$repo"` with no repo-identity guard; a lane without
`.git` is silently read from the fleet super-repo.** (Class D defect, high blast radius: 7 ledger
legs across 6 sibling repos.) `pin-disposition.py:235-265` already shows the fix. Evidence §2.2. Until
every sibling is colocated and stays colocated, a `.git` disappearance converts a pin mismatch into
either a false SETUP or a read from the wrong object store. Replacement: port `repo_identity`
before `:1000`–`:1035`, or export `GIT_CEILING_DIRECTORIES="$FLEET_ROOT"` and fail when the
toplevel != `$repo`.

**R2 — HEAD is `@-`, not the branch bookmark, after any jj mutation, and can be an unpushed
working-copy snapshot commit.** (`pin-disposition.py:317`; SKILL.md:1033's
`current = git show HEAD:<path>`.) Evidence §2.3: `master..HEAD=1` with an extra `dirty` line in
`HEAD:file.txt`. A content gate will classify unpushed snapshot bytes as "current"; anything that
cites a HEAD-derived hash can cite a commit that is not an ancestor of `master`, breaking the
wave's cited-hash invariant. Replacement: resolve `refs/heads/master` (and `master@origin`)
explicitly, and assert `git merge-base --is-ancestor "$rev" refs/heads/master` before citing.
Detached HEAD also breaks `@{u}`/`--abbrev-ref HEAD` (observed fatal); no in-scope call site uses
them today (class A = 0), but the helper's `detect_branch()` is the pattern to copy if one appears.

**R3 — the live lane's repo-level jj config lacks `snapshot.auto-track="none()"`, and that config
is external to the repo.** (Boundary finding, immediate likelihood.) Evidence §2.7. The helper
fixes it only via `init`, while `commit` gates on `.jj` existence alone; the first helper commit
without `init` runs with default auto-track over the lane's untracked paths. Because the config
lives at `~/.config/jj/repos/<path-hash>/config.toml`, it does not survive a path change, a
different operator/machine, or `jj config gc`. Replacement: run `jj-lane.sh init tameshi-shokunin
tameshi` before the first commit, and make `commit` fail closed unless
`jj --ignore-working-copy config get --repo snapshot.auto-track` returns `none()`.

Fourth, inert today: the hooks/attribute-filter bypass (§2.5) and the index reset (§2.6). No class-C
call site exists, and the lane has no hooks or attributes, so neither can change a verdict now.

## 6. Residual risk and unrun checks

- I did **not** execute any in-scope tool's `--selftest`/`--regression` (read-only brief; selftests
  write under `/tmp`). The classification is static plus jj/git semantics reproduced in the sandbox;
  a selftest pass would not have exercised a colocated repo anyway (`--regression` reads sibling
  repos, and those selftests `git init` under `/tmp`).
- I did **not** run `jj` in the live lane or any lane repo, so `jj config list --repo`, `jj st`, and
  `jj log` behaviour against the live op log is inferred from the external config file + op-store
  contents, not from a live call.
- The lane moved during the audit (`c699c8c` → `05a2247`); all live-state citations carry their
  observation context, and the dirty-path count quoted in R3 was sampled before the round landed.
- `assemble.py` / `reattribute.py` / `evidence-disposition.py` / `repeat-control.py` /
  `witness-metadata.py`: zero git invocations by literal grep; not classified further.
- Sandbox kept for reproduction: `/fast/scratch/jj-wave/JjAuditTameshi-2/` (`exp1` §2.1/§2.3,
  `exp2` §2.2, `exp3` §2.5/§2.6). Outside that sandbox, the only surviving write is this report;
  the one accidental external jj repo-config file (§2.7) was removed after it was recorded.
