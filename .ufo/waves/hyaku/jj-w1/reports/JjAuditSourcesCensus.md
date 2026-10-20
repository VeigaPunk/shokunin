# JjAuditSourcesCensus — `scripts/sources-census.sh` in jj-colocated lanes

Target: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`, 806 lines.
Modes audited: `census`, `validate`, `overdue`, `shared`. Environment: jj 0.45.1
(`~/.local/bin/jj`), git 2.56.0. No installs or upgrades were needed. No subagents were used.

All jj execution was confined to `/fast/scratch/jj-wave/JjAuditSourcesCensus-2/`; live repos were
only read (`git -C … log|show|ls-files|rev-parse|status|diff`, `cat`, `grep`). No live repo was
written, staged, fetched, or pushed; no fleet or lane script was executed against live paths. The
helper's push-recovery was replicated by hand (`jj git fetch` + `jj --ignore-immutable rebase -b …
-d main@origin`) inside sandbox repos whose `origin` is a sandbox bare repo.

## Verdict in one line

The script contains **no git and no jj invocation** (proved two ways below), so none of its calls
break on jj's detached HEAD, index reset, or bookmark moves. What does change is the meaning of the
bytes it reads: a jj-conflicted `corpus/SOURCES.md` materialises one side as `%%%%%%%` diff lines that
the row parser ignores, so all four modes treat the file as ordinary input — `census`/`overdue`/
`shared` under-count its rows and `validate` can print `ok` with exit 0 where the equivalent git
merge conflict produces `E03`/`E04` and exit 1.

## Findings

### F1 — No VCS call exists in the script; the four modes are filesystem-only (no break, verified)

```
$ grep -in git scripts/sources-census.sh   # no output, exit 1
$ grep -in jj  scripts/sources-census.sh   # no output, exit 1
```

(Excerpts below abbreviate unchanged row cells with `…`; marker lines, ids and URLs are verbatim.
Conflict-marker lines carry one leading space so this report itself does not register as a merge
conflict.)

Process-level proof, one trace per mode:

```
$ for m in census validate overdue shared; do
    strace -f -e trace=execve -o "exec-$m.log" ./sources-census.sh "$m" --root ./fleet --today 2026-10-20 >/dev/null 2>&1
    printf '%s: ' "$m"; grep -qE 'execve\("[^"]*(/git|/jj)' "exec-$m.log" && echo VCS_FOUND || echo no-vcs
  done
census: no-vcs
validate: no-vcs
overdue: no-vcs
shared: no-vcs
$ grep -hoE 'execve\("[^"]+"' exec-*.log | sed 's/execve("//;s/"$//' | sort -u
/usr/bin/bash
/usr/bin/cat
/usr/bin/gawk
/usr/bin/grep
/usr/bin/sed
/usr/bin/sort
./sources-census.sh
```

Consequences tested in the sandbox jj lane (`fleet/census-shokunin`):

* HEAD detachment: `git symbolic-ref -q --short HEAD` returned `main` before, then after
  `jj new` returned nothing (`DETACHED`). `census` printed `FLEET rows 3` both times and
  `validate` still printed `census ok …` / exit 0.
* The known breakage is real but unused by the census: in a detached jj lane
  `git rev-parse @{u}` → `fatal: HEAD does not point to a branch` (exit 128), while
  `git rev-parse main` works. The census has no `@{u}`, `HEAD`, index, or ref usage.
* Index inertness: after `git add corpus/knowledge/staged.md`, running all four modes left
  `git diff --cached --name-only` printing `corpus/knowledge/staged.md`. (jj itself resets the
  index on its own mutations; the census never invokes jj, so it cannot do that.)
* jj op-head inertness: `.jj/repo/op_heads/heads/bce56b…` had mtime `1792505586` before and after
  all four modes; `git status --porcelain` was empty before and after.
* `selftest`: 96 `killed`, 0 `SURVIVED`, `selftest ok`, exit 0 (fixtures copied to the sandbox so
  the run cannot touch the fleet).

Call inventory (all reads are plain filesystem reads):

| mode | file reads | VCS commands |
|---|---|---|
| `census` | `$ROOT/*-shokunin` dirs (line 472), `shokunin.conf` via `sed` (line 470), `corpus/SOURCES.md` via `gawk` (`row_pass`, line 574) | none |
| `validate` | same as census + `usedby_findings` `[ -e "$dir/$path" ]` (line 566) | none |
| `overdue` | `row_pass` only | none |
| `shared` | `row_pass` output aggregated in gawk | none |

### F2 — HIGH: jj conflict materialisation hides one side's rows from every mode; `validate` returns `ok`

`row_pass` only accepts lines matching `^ {0,3}\|` (line 615). jj materialises a text conflict as one
full side under `+++++++` plus the other side as `%%%%%%%` diff lines prefixed `+|` / `-|`; those
prefixed lines are not table rows. There is no conflict-marker detection anywhere in the script.

Same-line conflict, lane side hidden (`fleet2/conflict-shokunin`, conflict produced by the helper's
own recovery command):

```
 <<<<<<< conflict 1 of 1
+++++++ oprznsmz cf1fa164 "lane lesson commit" (rebase destination)
| S001 | One — https://a.example/x | docs | B | s1 | §1 | first evidence row UPSTREAM | queued | 2026-01-01 | 30d | — |
%%%%%%% diff from: oprznsmz accd9c41 "lane lesson commit" (parents of rebased revision)
\\\\\\\        to: olmsmnqn 932f5d65 (rebased revision)
-| S001 | One — https://a.example/x | docs | B | s1 | §1 | first evidence row | queued | 2026-01-01 | 30d | — |
+| S001 | One — https://a.example/x | docs | B | s1 | §1 | first evidence row LANE | queued | 2026-01-01 | 30d | — |
 >>>>>>> conflict 1 of 1 ends

$ ./sources-census.sh validate --root ./fleet2 --today 2026-10-20
conflict	W04	S003 duplicate url a.example/x across scopes
conflict	ok	./fleet2/conflict-shokunin/corpus/SOURCES.md
exit 0
```

The identical conflict under a plain git merge (same base content, lane edits S001, upstream edits
S001):

```
 <<<<<<< HEAD
| S001 | … first evidence row UPSTREAM … |
 =======
| S001 | … first evidence row LANE … |
 >>>>>>> lane

$ ./sources-census.sh validate --root ./fleetgit2 --today 2026-10-20
gitconf	E03	S001 duplicate id
gitconf	E04	S001 duplicate url a.example/x within scope s1
exit 1
```

Adding rows at the same position loses the row entirely (`fleet3/addgate-shokunin`, lane appends S005,
upstream appends S004):

```
 <<<<<<< conflict 1 of 1
+++++++ ztmtrlrm a68dd1d0 "lane commit" (rebase destination)
| S004 | Upstream new — https://up.example/new | … |
%%%%%%% diff from: ztmtrlrm e1c2aceb "lane commit" (parents of rebased revision)
\\\\\\\        to: ykqrqkuo e5a93ac9 (rebased revision)
+| S005 | Lane new — https://lane.example/new | … |
 >>>>>>> conflict 1 of 1 ends

$ ./sources-census.sh census --root ./fleet3 --today 2026-10-20
addgate	rows	4          # control with both rows materialised: 5
FLEET	rows	4
exit 0
$ ./sources-census.sh validate --root ./fleet3 --today 2026-10-20
addgate	ok	…/corpus/SOURCES.md
exit 0
$ ./sources-census.sh shared --root ./fleet3
(no output, exit 0)         # control: lane.example/new	shared	addgate,other
```

`overdue` loses a due row the same way (`fleet10/gate-shokunin`, lane row S010 opened 2025-01-01,
recheck 30d, hidden in the `+|` line):

```
$ ./sources-census.sh overdue --root ./fleet10 --today 2026-10-20   # genuine jj conflict
gate	cadence	S001 …
gate	cadence	S020 …
gate	cadence	S011 …
gate	overdue	S001 262d recheck=30d opened=2026-01-01
(no S010 line)
$ # control: lift the +| lane row into the table
gate	overdue	S010 627d recheck=30d opened=2025-01-01
```

The hidden side is not always the lane's: in `fleet12/gate-shokunin` the same rebase shape produced
`+| S011` hidden and the lane row S010 in the visible `+++++++` side, so `shared`/`overdue` saw S010
and missed upstream S011 instead. Both directions were observed on jj 0.45.1; [INFERENCE] the
selection is not content-deterministic (it varies with the merge/hash), so "the visible side is the
lane's content" is not a safe assumption.

Caller impact: `scripts/shokunin-watchdog.sh:323` `sources_gate` only branches on the census exit
code (0 pass, 1 block, else warn), and `scripts/hyaku/closure-prompt.md:43` tells closures to run
`validate` directly. A conflicted registry therefore passes the gate with rc 0 and the closure sees
`ok`; only a later `jj-lane.sh` push would refuse the conflicted tree.

### F3 — MEDIUM: all modes read the working copy, never the pushed commit

`row_pass` is handed `$f` on disk (line 717); there is no `--rev`/`--landed` path. `--file` reads the
file via `realpath` (line 502) and can be pointed anywhere. In a jj lane with
`snapshot.auto-track="none()"`, tracked-file edits stay in `@` and path-limited commits leave them
there.

Clean sandbox fixture (`fleet8/drift-shokunin`: base 2 rows; worktree adds S006; only
`corpus/lessons/l.md` is committed, bookmark `main` moved to that commit and pushed):

```
$ git rev-parse main
55b53b652a5ccd5b358809e925c498b1bdcf7472
$ git show main:corpus/SOURCES.md | grep -cE '^\| S[0-9]+'
2
$ grep -cE '^\| S[0-9]+' corpus/SOURCES.md
3
$ git show main:corpus/SOURCES.md | grep -q S006 && echo PRESENT || echo ABSENT
ABSENT
$ ./sources-census.sh census --root ./fleet8 --today 2026-10-20 | grep 'FLEET	rows'
FLEET	rows	3
$ ./sources-census.sh validate --root ./fleet8 --today 2026-10-20
drift	ok	./fleet8/drift-shokunin/corpus/SOURCES.md
exit 0
```

So `validate` can certify a registry row that is not in the cited pushed hash. [INFERENCE] This gap
pre-exists in git when changes are left unstaged; jj widens it because new files stay untracked under
`auto-track="none()"` (F4).

### F4 — MEDIUM: a new `SOURCES.md` can be absent from a `jj commit` that exits 0

With `snapshot.auto-track="none()"`, a newly created registry is untracked. A plain jj commit of that
path warns and still succeeds with an empty commit:

```
$ jj commit -m 'untracked new registry' -- corpus/NEW.md
Warning: The given paths do not match any file: corpus/NEW.md
Working copy  (@) now at: vrvtqktt f9284525 (empty) (no description set)
Parent commit (@-)      : omwvwvmr c7b33dfe (empty) untracked new registry
commit rc=0
$ jj --ignore-working-copy file list -r @- | grep -F corpus/NEW.md || echo ABSENT_FROM_COMMIT
ABSENT_FROM_COMMIT
$ jj file track -- corpus/NEW.md && jj commit … -- corpus/NEW.md
$ jj --ignore-working-copy file list -r @- | grep -F corpus/NEW.md
corpus/NEW.md
```

The git equivalent refuses: `error: pathspec 'NEW.md' did not match any file(s) known to git`
(exit 1). `jj-lane.sh` already mitigates this with `jj file track --include-ignored -- <file>` before
`jj commit` (line 210 of the helper), but a lane path that commits an untracked new registry
directly with `jj commit` cannot include it (observed above), so it can lose the file while
`validate` stays green.

### F5 — MEDIUM/LOW: `E11` is existence-only and passes on conflicted artifacts

`usedby_findings` tests only `[ ! -e "$dir/$path" ]` (line 566). jj leaves a conflicted used-by file
in place, so a marker-filled artifact passes:

* `fleet7/e11-shokunin` (upstream deletes `corpus/knowledge/two.md`, lane modifies it):
  `jj st` → `A corpus/knowledge/two.md`, `Warning: There are unresolved conflicts at these paths:
  corpus/knowledge/two.md 2-sided conflict including 1 deletion`; the file is 280 bytes of
  `<<<<<<< conflict 1 of 1 …`; `validate` → `e11 ok`, exit 0.
* `f14/fleet/b-shokunin` (binary content conflict): `corpus/knowledge/data.bin` is 379 bytes of
  textual conflict block (`<<<<<<< conflict 1 of 1 …`); `validate` → `b ok`, exit 0.
* `f16/fleet/b-shokunin` (invalid UTF-8 bytes, NULs included): same in-place materialisation
  (`data.bin`, 379 bytes, `2-sided conflict`); `validate` → `b ok`, exit 0. No `.jjconflict-*`
  sidecars appeared in any conflict produced here.

The helper's `do_push` refuses to push a conflicted bookmark (exit 3), so the two instruments can
disagree: `validate` says clean, the lane cannot land. See `scripts/hyaku/jj-lane.sh:112-116`.

### F6 — LOW: roster/conf parsing is unaffected by colocation (verified)

`build_roster` still globs `"$ROOT"/*-shokunin` (line 472) and parses `shokunin.conf` with `sed`
(line 470); `.jj` is hidden and does not match, and no `git` metadata is consulted. A jj *workspace*
lane (`.jj` present, no `.git` at all) also works [INFERENCE: a tool that requires `.git` would not
open that directory; the census does not require it]:

```
$ test -e wsroot/ws-lane-shokunin/.git && echo YES || echo NO   → NO
$ ./sources-census.sh census --root ./wsroot --today 2026-10-20
ws	rows	1
FLEET	rows	1
$ ./sources-census.sh validate --root ./wsroot --today 2026-10-20
ws	ok	./wsroot/ws-lane-shokunin/corpus/SOURCES.md
exit 0
```

## Inference

* [INFERENCE] The production path that creates these conflicts is `jj-lane.sh`'s push-rejection
  recovery: `do_push` runs `jj git fetch` then
  `jj --ignore-immutable rebase -b <tip> -d <branch>@origin`, and `@` is a descendant of `<tip>`, so
  the dirty working-copy commit is rebased too. If `corpus/SOURCES.md` was edited but not part of the
  commit being pushed, its rows can conflict with an operator push even though the commit under test
  touched a different path. I read `do_push` in the helper (line 121 is the rebase) and reproduced
  the resulting conflict by hand; I did not execute the helper.
* [INFERENCE] Because `sources_gate` treats rc 0 as pass, F2 lets a round advance on a conflicted
  registry; the failure surfaces only if the lane later asks the helper to push the conflicted tree,
  or if a human reads the file.
* [INFERENCE] Which conflict side is materialised as full content and which as `%%%%%%%` diff varies
  by rebase/merge shape (observed both directions), so the census cannot be made correct by assuming
  the lane's side survives; only marker detection is reliable.
* [INFERENCE] F3 is pre-existing in the git era (unstaged working-tree edits are also read by the
  census), but jj's `auto-track="none()"` and the rc-0 empty commit in F4 make "green validate, no
  landed counterpart" substantially easier to reach for new registries.

## Recommendations

1. **Add a conflict check to the census; do not let it report `ok` on a conflicted registry.**
   Before the table parse in `row_pass` (line 574) — and once per file in `usedby_findings` — scan
   the file for the jj materialisation markers:
   `^<<<<<<< conflict `, `^%%%%%%% diff from:`, `^>>>>>>> conflict .* ends$`, and refuse any
   `*.jjconflict-*` sibling. Emit a new `E13` (error, exit 1) with lane + path + first marker line.
   A registry row can never legitimately start with those tokens (rows start with `|`), so the check
   is false-positive-safe and needs no VCS invocation. This preserves the script's read-only,
   no-git contract and covers the same shape for a plain git conflict if it is ever read directly.
2. **Optionally add a read-only jj guard outside the census** (watchdog `sources_gate`, which already
   owns lane-level policy): `jj --ignore-working-copy log -r 'heads(bookmarks(<branch>)) & conflicts()'`
   and `jj --ignore-working-copy diff --summary -r @ -- corpus/SOURCES.md`. Both use
   `--ignore-working-copy`, so they cannot snapshot or rewrite a live lane; plain `jj` must not be
   used from a reader.
3. **Add a landed/rev mode for evidence citation.** `validate` (and `census`) should accept
   `--rev <rev>`/`--landed` and read `git show <rev>:corpus/SOURCES.md` instead of the worktree, or
   the closure step should assert equality before citing a hash
   (`cmp <(git show <hash>:corpus/SOURCES.md) corpus/SOURCES.md`). The `--file` path can stay as-is.
4. **Keep `jj-lane.sh` mandatory for lane commits and document the untracked trap.** The helper's
   `jj file track` already covers new files; add one line to the lane prompt that
   `jj commit -- <path>` returns 0 with an empty commit for untracked paths under
   `auto-track="none()"`, so direct jj commits are forbidden.
5. **Make `sources_gate` block on conflict state.** Feed it the new `E13` (rc 1) rather than relying
   on rc 2 warnings, and run the gate after the helper push, when the working copy for committed
   paths is clean.
6. **Tighten `E11` slightly** (cheap): treat a used-by path as valid only if it is a non-empty regular
   file that does not contain conflict markers; execution of F2's marker check can be shared.

## Verification gaps / residual risk

* No live lane was read beyond `git`/`cat`/`grep` per the wave's hard rules; all fixtures are
  sandbox repos with sandbox bare origins. The helper was not executed; its recovery command was
  replicated by hand.
* jj 0.45.1 conflict formatting is assumed stable; a future jj that changes marker wording would need
  the `E13` patterns revisited. The patterns above are the exact strings observed.
* The `shared` loss is demonstrated in `fleet3` (conflict run produced no output; the control with
  S005 materialised produced `lane.example/new	shared	addgate,other`). In `fleet10` the shared map
  did not lose the URL because a visible sibling row carried the same URL; that is consistent with the
  mechanism but means `shared` loss is only as broad as the hidden rows' unique URLs.
* F3 is a pre-existing worktree-vs-commit property of the script, not a jj regression; it is reported
  because the wave's "landed = committed AND pushed before a report cites the hash" invariant makes it
  material.
* There is no canonical-runtime, same-identity rerouting, or saturation surface in this target;
  nothing of that kind was verified here.

Sandbox preserved (contains the failure fixtures cited above, `exec-*.log`, `selftest.out`):
`/fast/scratch/jj-wave/JjAuditSourcesCensus-2/` — subdirs `fleet`, `fleet2`, `fleet3`, `fleet7`,
`fleet8`, `fleet9`, `fleet10`, `fleet12`, `f14`, `f16`, `wsroot`, `gitcmp2`, `fleetgit2`.
