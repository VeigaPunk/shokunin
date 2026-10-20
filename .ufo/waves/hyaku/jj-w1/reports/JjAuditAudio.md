# JjAuditAudio — lane `audio` git-invocation audit (read-only)

**Seat:** JjAuditAudio-2 (leaf; no subagent dispatch). **Date:** 2026-10-20.
**Target:** `/home/vgpnk/Projects/shokunin/audio-shokunin`, branch `main`, HEAD `0462a5440f23f45707ba681e2a011940e3c923dd` (= `origin/main`).
**Live state when audited:** plain git checkout; `.git/HEAD` = `ref: refs/heads/main`; no `.jj` directory; `git status --porcelain --untracked-files=no` empty; `git rev-parse HEAD` = `git rev-parse origin/main`. Colocation is prospective, not present in this lane yet.
**Read-only discipline:** no write, stage, checkout, fetch, or commit in the live repo. All jj/git mutation experiments ran against sandbox bare origins under `/fast/scratch/jj-wave/JjAuditAudio-2/`; that sandbox was deleted after the audit. The only write outside it is this report.

## 0. Bottom line

**A = 0, B = 0, C = 0.** The lane has **218 read-only (D) git invocation sites** plus **16 generic read-only wrapper definitions (W)**; no executable tooling in the lane mutates history, the index, or the working tree. The lane is not colocated yet, so nothing is broken today. The prospective jj risks are (1) `HEAD` is the detached `@-` commit, not the branch, between the helper's `jj commit` and its bookmark move/push; (2) detached HEAD breaks `@{u}`/`symbolic-ref` idioms; (3) jj's index resets and intent-to-add placeholders make `ls-files -s`/`diff --cached`/`status --untracked-files=no` gates semantically wrong.

## 1. Scope reality and method

The brief's nominal in-scope paths do not exist on this lane:

| expected | found | evidence |
|---|---|---|
| `tools/` | absent | `find . -maxdepth 1 -type d` prints `considerthese corpus ports reports` only |
| `scripts/` | absent | same |
| `verifiers/` | absent | same |
| `SKILL.md` | absent | `find . -name SKILL.md` → no result; `README.md:8-9` says it is absent on lanes still in shonen seed form |
| gates/selftests named in `SKILL.md` | n/a (no `SKILL.md`) | `SHONEN.md` is the 10-line promotion checklist and names no commands; `corpus/QUALITY.md` is Q1–Q22 admission criteria; neither contains a git command |
| root executable files | 1 `.sh`, 0 `.py/.mjs/.js/Makefile` | `generate_timings.sh`: five `gnuplot` lines, 0 git |

Because the nominal surface is empty, the sweep was expanded to every executable script under the lane (excluding `.git`): **1,213 regular `.py` files + 1 symlinked `.py` + 167 `.sh` files; 0 `.js`/`.mjs`; 0 `Makefile`.**

Method:
- Every `.py` parsed with `ast`: `subprocess.run/call/check_output/check_call/Popen` calls whose first argv element is `"git"`, plus every call to a locally defined `git(...)` wrapper. Wrapper definitions are recorded as W; their call sites are recorded with the concrete subcommand.
- Every `.sh` scanned line-wise for `git <subcommand>`, excluding comment lines and six `echo`-only label lines that print a command without executing it (`r84:40,44`, `r85:45,49`, `r86:67`, `r87:44`).
- Searched and found none: `os.system("git ...")`, `shell=True` git strings, a `GIT`/`GIT_BIN` variable holding `"git"`, GitPython/pygit2/dulwich, `.js`/`.mjs`/`Makefile` git calls.

Result by area:

| area | files | static sites | classes |
|---|---|---|---|
| `corpus/fixtures/` (11 `test_*.py` selftests + `measure_audio.py`, `build_artifacts.*`, probes) | 20 | 0 | — |
| `reports/round-1-calibration/count_checklist.py` (standing tool) | 1 | 4 | 3 D + 1 W |
| `corpus/live/**` historical round scripts | 90 | 230 | 215 D + 15 W |
| **total** | **91** | **234** | **218 D + 16 W** |

The 11 selftests named in the lane's own record (`test_audio_final_guards.py`, `test_audio_host_lock.py`, `test_ebur_r93_entry_cleanup.py`, `test_pwstream_r98_scope.py`, `test_rtp_r99_{lan_control,loopback,missing}.py`, `test_sofa_r100_witnesses.py`, `test_truepeak_r101.py`, `test_wppol_r97_guard.py`, `test_wpstate_r90_lock.py`) **contain zero git invocations**; they exercise ffmpeg/SoX/PipeWire/Pulse/ALSA binaries only.

## 2. In-scope/standing tooling: every git call

`reports/round-1-calibration/count_checklist.py` is the only git-using tool outside `corpus/live/`. Its documented invocations are `python3 reports/round-1-calibration/count_checklist.py <hash>` and `... HEAD` (`reports/round-1-calibration/measurement.md:8-9`).

| site | exact command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `reports/round-1-calibration/count_checklist.py:19-20` | `subprocess.check_output(["git","-C",str(ROOT),*args], text=True)` | **W** | Generic wrapper: runs whatever `*args` the caller supplies, in the lane root, and inherits a detached HEAD. Its three callers pass only `rev-parse`, `show`, `ls-tree`. | Keep the wrapper read-only; do not add mutating subcommands. |
| `...:49` | `git("rev-parse","--verify", sys.argv[1] + "^{commit}")` | **D** | Verified working for a full hash, `main`, and `HEAD` under detached HEAD. `@{u}` fails rc=128 (`fatal: HEAD does not point to a branch`). `HEAD` resolves to `@-`, which may lag the branch between `jj commit` and the helper's `bookmark set`/push. | Pass an explicit hash or `refs/heads/main`. For a landed check, add `git merge-base --is-ancestor <hash> refs/remotes/origin/main`. |
| `...:50` | `git("show", revision + ":SHONEN.md")` | **D** | Rev-based and index-free; works detached (verified). Requires the path at the selected rev; `SHONEN.md` exists at HEAD. | Keep; pass an explicit rev. |
| `...:51` | `git("ls-tree","-r","-z","--name-only", revision)` | **D** | Rev-based and index-free; works detached (verified). | Keep. |

`generate_timings.sh` and all 20 `corpus/fixtures/` files have no git calls.

## 3. All-site classification

### 3.1 Counts

| class | static sites | meaning |
|---|---|---|
| **A** | **0** | no `symbolic-ref`, `@{u}`, `--abbrev-ref`, `show-current`, `branch --show-current`, or `HEAD`-as-branch refspec |
| **B** | **0** | no `add`, `commit`, `stash`, `checkout`, `reset`, `rebase`, `push`, `pull`, `merge`, `clean`, `tag`; no plain `git apply` |
| **C** | **0** | no `diff --cached`/`--staged`, `ls-files -s`, `update-index`, `diff-index --cached` |
| **D** | **218** | read-only: `show`, `rev-parse`, `ls-tree`, `diff`, `status`, `apply --check/--numstat`, `log`, `ls-files`, `hash-object`, `archive` |
| **W** | **16** | generic `git(*args)` wrapper definitions; every observed caller passes a D subcommand |
| **total** | **234** | |

Executable-process accounting: **218 invocations** = 83 concrete subprocess argv sites + 57 local-wrapper call sites + 78 shell command sites. The 16 W rows are wrapper definitions, not additional process launches.

### 3.2 By command family

| family | class | sites | jj risk | jj-safe replacement |
|---|---|---|---|---|
| `git show <rev>:<path>` | D | 59 | Rev-based, safe detached. `HEAD` is `@-`; may lag the branch bookmark. | Explicit hash or `refs/heads/main`; never `@{u}`. |
| `git rev-parse ...` | D | 45 | `HEAD`, `--short HEAD`, `--show-toplevel`, `<rev>:<path>` all work detached (verified). `HEAD` may lag the bookmark. | Same; for ancestry use `merge-base --is-ancestor`. |
| `git ls-tree ...` | D | 23 | Rev-based, index-free, safe. | Keep; use an explicit rev. |
| `git diff ...` | D | 21 | All are `--name-only/--numstat/--quiet/--no-index` or `<rev>` diffs. Plain `git diff` is worktree-vs-index; jj resets the index, so it behaves as worktree-vs-HEAD in practice. | Prefer `git diff HEAD -- <path>`/`--quiet HEAD`; never `--cached`. |
| `git status ...` | D | 17 | Read-only but index-sensitive. Under jj, pending `@` changes show as ` M`/`.A`; `--untracked-files=no` still shows a jj-added new file. Does not fail. | `jj status` for working-copy truth, or `git status` only as a dirty flag. |
| `git apply --check/--numstat` | D | 17 | Dry-run only; does not mutate. Plain `git apply` would be B. | Keep `--check`/`--numstat`; never drop the flags. |
| `git log ...` | D | 14 | Rev-based, safe detached. `git log <base>..HEAD` follows `HEAD`, so it can report an unpushed jj commit as "landed". | `git log <base>..refs/remotes/origin/main`. |
| `git ls-files ...` | D | 10 | Index-based. jj resets the index; new `@` files appear as empty-blob intent-to-add entries (`e69de29…`) and files modified in `@` resolve to the HEAD blob. | `git ls-tree -r --name-only <rev>` or `jj file list` for a tracked census. |
| `git hash-object ...` | D | 9 | Content-based, index-free, safe. | Keep. |
| `git archive ...` | D | 3 | Rev-based, safe detached (verified `git archive HEAD` works). | Keep; explicit rev. |

## 4. Hooks, attributes, filters, eol

Nothing is configured in this lane:

| item | result |
|---|---|
| non-sample hooks | `ls -1 .git/hooks \| grep -v '\.sample$'` → no output, rc=1. All 14 entries are `*.sample`. |
| `core.hooksPath` | unset at local, global, and system level (`git config --local/--global/--system --get core.hooksPath` → rc=1 each) |
| `.gitattributes` | none: `find . -name .gitattributes -not -path './.git/*'` → no output |
| `.git/info/attributes` | absent: `ls .git/info/attributes` → `No such file or directory` |
| `core.attributesFile` | unset (`git config --get-all core.attributesFile` → rc=1) |
| `git check-attr -a` on `corpus/fixtures/measure_audio.py`, `corpus/artifacts/ui.wav`, `SHONEN.md`, `.gitignore` | no output → no attribute applies |
| eol | `core.autocrlf`, `core.eol`, `core.safecrlf` all unset (rc=1 each) |
| `include.path` | unset (rc=1) |
| global filter config | `filter.lfs.clean/smudge/process/required` are defined in `/home/vgpnk/.config/git/config`, but no attribute selects `filter=lfs`; `git lfs ls-files` is empty |
| jj consequence | With no hooks/attributes/eol rules, jj's bypass changes nothing today. The lane's protocol invariants (lane identity, pathspec-limited commits, append-only `LOG.md`, `.ufo/state/` exclusion) are enforced only by `scripts/hyaku/jj-lane.sh` argument checks, not by a git hook or attribute filter. If a hook or LFS/eol attribute is added later, jj will bypass it. |

## 5. Top three risks for this lane

### Risk 1 — `HEAD` is `@-`, not the branch, between jj commit and bookmark push

The lane's documented instrument says `count_checklist.py HEAD` (`reports/round-1-calibration/measurement.md:9`), and the historical postcommit probes resolve `NEW = git rev-parse HEAD` (`r76-baseline/postcommit_verify.py:24`, `r77-baseline/postcommit_verify.py:25`, `r78-baseline/census.py:97`, `r89-boundary/r89b_probe.py:456`, `r88-simplifier/proofs/observations.py:67`). `r75-scribe/poll-landing.sh:19,23` also prints "LANDED" from `git log "$base"..HEAD`.

The helper's order is `jj commit` → `jj bookmark set` → `jj git push`, inside the per-lane lock `$STATE/jj-<lane>.lock`. Lane scripts do not take that lock. In the window, HEAD is the new `@-` commit while `refs/heads/main` is still the old tip. Sandbox evidence after `jj commit -m 'divergence probe' -- a.txt`:

```
$ git rev-parse HEAD; git rev-parse refs/heads/main
e873bf58b26deb862bc8ad914414fd8760bd1f2a
46fc26fc9d0abdbc0883e981a5b627ee9d61b7b0
$ git show HEAD:d.txt
fatal: path 'd.txt' exists on disk, but not in 'HEAD'
```

A report that cites the HEAD-derived hash (or the `log base..HEAD` "landed" line) in that window violates the protocol invariant "a cited hash stays an ancestor of the branch" and lane bar Q12 ("A cited commit is reachable from the published branch, or its evidence is explicitly marked `branch-scoped`"). The lane has **no executable ancestry check**: zero `merge-base`, `is-ancestor`, `branch --contains`, or `rev-list origin/main` sites. Mitigation: cite the helper's `pushed <hash>` output; resolve from `refs/heads/main`/`refs/remotes/origin/main`; add `git merge-base --is-ancestor <hash> refs/remotes/origin/main` to any landed gate.

### Risk 2 — detached HEAD silently breaks attached-ref idioms

After any jj mutation `.git/HEAD` is a raw hash. Sandbox evidence:

```
$ git symbolic-ref -q --short HEAD; echo rc=$?
rc=1
$ git rev-parse --abbrev-ref HEAD
HEAD
$ git rev-parse '@{u}'
fatal: HEAD does not point to a branch
rc=128
$ git branch -vv
* (no branch) e873bf5 divergence probe
  main        46fc26f [origin/main] add checklist
```

Zero current lane sites use these idioms (the sweep found no `symbolic-ref`, `@{u}`, `--abbrev-ref`, or `show-current`), so nothing fails today. The risk is a new "landed/pushed" gate written in the natural git style: `@{u}` exits 128, `--abbrev-ref HEAD` returns the literal string `HEAD`, and a `status -sb` parser sees `## HEAD (no branch)`. Mitigation: always use explicit refs or `jj bookmark list <branch>`; never infer a branch name from HEAD.

### Risk 3 — jj's index resets and intent-to-add placeholders invalidate index-based gates

`git add` staging is destroyed by the next jj mutation. Sandbox evidence in `exp1`:

```
$ git add f.txt
$ git diff --cached --name-only
f.txt
$ jj describe -m wip
$ git diff --cached --name-only
                      # empty
$ git ls-files -s f.txt
100644 814f4a42... 0  f.txt     # HEAD blob, not the working-copy content (4cb29ea3...)
```

After a path-limited `jj commit -- a.txt` leaves a new file `d.txt` in `@`, `d.txt` is in the index as an **empty-blob intent-to-add placeholder**:

```
$ git hash-object d.txt
6f1852975b9306ae5d8dfdf0d4cb1f5cb36ac229
$ git rev-parse :d.txt
e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
$ git ls-files -s d.txt
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0 d.txt
$ git diff --cached --name-only
                      # empty
$ git diff-index --name-status HEAD
M  a.txt
A  d.txt
$ git status --porcelain --untracked-files=no
 A d.txt
```

The lane has zero class-C sites today, but 10 `ls-files` and 17 `status` sites (family R2) exist in historical censuses; re-running them under jj can change counts or report an empty content hash for a non-empty file. Mitigation: `git ls-tree -r --name-only <rev>`/`jj file list` for censuses; `git hash-object <file>` for content identity; `git diff HEAD -- <path>`/`git diff --quiet HEAD` for dirty state; never stage.

## 6. Residual risk, [INFERENCE], recommendations

- **[INFERENCE]** Because `corpus/live/**` scripts are frozen round artifacts, the practical jj surface is the 4 sites in `count_checklist.py` plus any new lane tooling. The historical scripts are still re-runnable and are the reason classes A/B/C are not structurally impossible in this repo.
- **[INFERENCE]** The helper's push-recovery path rebases unpushed commits (`jj rebase -b <tip> -d <branch>@origin`), so a `committed <hash>` printed on exit 3 can be rewritten on retry. Only the helper's `pushed <hash>` is cite-safe; this matches the helper's own header contract.
- **Recommendation 1:** in `count_checklist.py`, accept only `HEAD`/hash/`refs/*`; reject `@{u}` and any revset with `@` or `..` before calling git, so a detached-HEAD failure is a clear usage error, not a `CalledProcessError` traceback.
- **Recommendation 2:** add a read-only ancestry gate to the lane (e.g. `git merge-base --is-ancestor "$hash" refs/remotes/origin/main`) and run it before any report cites a hash. This closes Q12's current zero-executable-check gap.
- **Recommendation 3:** do not add git hooks, `.gitattributes` filters, or eol rules as a jj-era enforcement layer; they will be bypassed. Put the invariants in the helper or in a pre-report gate that reads jj/git refs explicitly.
- **Recommendation 4:** if a lane census must count tracked files, switch `git ls-files` to `git ls-tree -r --name-only <rev>`; if it must detect dirty state, use `git diff --quiet HEAD -- <paths>` instead of `git diff --quiet`/`status --porcelain --untracked-files=no`.

## Appendix A — every static git site (234)

Legend: **R1** = rev-based read (safe detached; `HEAD` may lag the bookmark); **R2** = index/worktree read (jj index-reset caveat); **R3** = content hash (safe, index-free); **R4** = dry-run apply (safe; keep `--check`/`--numstat`); **R5** = generic wrapper (subcommand from caller; observed callers R1–R3).

| site | command | class | replacement |
|---|---|---|---|
| `corpus/live/r65-reviewer/collision_scan.py:17` | `git ls-files` | D | R2 |
| `corpus/live/r67-baseline/compare.py:44` | `git -C str(ROOT) show f"HEAD:{relpath}"` | D | R1 |
| `corpus/live/r68-baseline/compare.py:45` | `git -C str(ROOT) show f"{COMMIT}:{relpath}"` | D | R1 |
| `corpus/live/r69-author/census_check_rows.py:28` | `git -C str(ROOT) ls-files corpus/live/runs` | D | R2 |
| `corpus/live/r69-baseline/compare.py:46` | `git -C str(ROOT) show f"{COMMIT}:{rel}"` | D | R1 |
| `corpus/live/r69-scribe/census_checkrows.py:121` | `git ls-files` | D | R2 |
| `corpus/live/r69-verifier/census_v.py:73` | `git -C str(ROOT) ls-tree -r --name-only commit corpus/live/runs` | D | R1 |
| `corpus/live/r69-verifier/census_v.py:79` | `git -C str(ROOT) ls-files corpus/live/runs` | D | R2 |
| `corpus/live/r70-baseline/compare.py:46` | `git -C str(ROOT) show f"{COMMIT}:{rel}"` | D | R1 |
| `corpus/live/r71-boundary/edge_probes.py:318` | `git -C str(REPO) rev-parse HEAD` | D | R1 |
| `corpus/live/r71-boundary/edge_probes.py:321` | `git -C str(REPO) diff --name-only corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r71-simplifier/watch.sh:4` | `cd "$(git rev-parse --show-toplevel)"` | D | R1 |
| `corpus/live/r71-simplifier/watch.sh:8` | `cur="$cur $(ls -d corpus/live/r71-author corpus/artifacts/ffprobe_ledger_r71.json 2>/dev/null \| tr '\n' ',') $(git status --porcelain -- corpus/fixtures corpus/artifacts corpus/…` | D | R2 |
| `corpus/live/r72-verifier/extract_lattice.py:46` | `git ls-files f"corpus/live/runs/*{suffix}/measurements.json"` | D | R2 |
| `corpus/live/r73-baseline/compare.py:26` | `git show f"HEAD:{path}"` | D | R1 |
| `corpus/live/r73-baseline/compare.py:41` | `git show HEAD:corpus/live/r70-author/ledger-r71.tsv` | D | R1 |
| `corpus/live/r73-baseline/compare.py:63` | `git ls-files corpus/live/runs` | D | R2 |
| `corpus/live/r74-baseline/build_env.py:20` | `git *args` | W | R5 |
| `corpus/live/r74-baseline/build_env.py:25` | `git ls-files corpus/artifacts corpus/fixtures corpus/live/round-*` | D | R2 |
| `corpus/live/r74-baseline/build_env.py:30` | `git show f"HEAD:{rel}"` | D | R1 |
| `corpus/live/r74-baseline/compare.py:26` | `git show f"HEAD:{path}"` | D | R1 |
| `corpus/live/r74-baseline/compare.py:41` | `git show HEAD:corpus/live/r70-author/ledger-r71.tsv` | D | R1 |
| `corpus/live/r74-baseline/compare.py:63` | `git ls-files corpus/live/runs` | D | R2 |
| `corpus/live/r74-baseline/semantic_compare.py:99` | `git show HEAD:corpus/live/r70-author/ledger-r71.tsv` | D | R1 |
| `corpus/live/r74-baseline/semantic_compare.py:116` | `git show f"HEAD:{crel}"` | D | R1 |
| `corpus/live/r74-scribe/parser_audit.py:37` | `git hash-object str(FIX)` | D | R3 |
| `corpus/live/r74-scribe/watch.sh:8` | `echo "HEAD: $(git log --oneline -1)"` | D | R1 |
| `corpus/live/r74-scribe/watch.sh:9` | `echo "worktree tracked-modified: $(git status --porcelain --untracked-files=no \| wc -l)"` | D | R2 |
| `corpus/live/r74-scribe/watch.sh:10` | `echo "fixture blob: $(git hash-object corpus/fixtures/measure_audio.py)"` | D | R3 |
| `corpus/live/r74-simplifier/watch-landing.sh:9` | `head=$(git rev-parse --short HEAD)` | D | R1 |
| `corpus/live/r74-simplifier/watch-landing.sh:10` | `dirty=$(git status --porcelain 2>/dev/null \| grep -vc '^??')` | D | R2 |
| `corpus/live/r74-simplifier/watch-landing2.sh:8` | `head=$(git rev-parse --short HEAD)` | D | R1 |
| `corpus/live/r74-simplifier/watch-landing2.sh:9` | `src=$(git diff --name-only HEAD -- corpus/fixtures/measure_audio.py corpus/fixtures/build_artifacts.py \| wc -l)` | D | R1 |
| `corpus/live/r74-simplifier/watch-landing3.sh:8` | `head=$(git rev-parse --short HEAD)` | D | R1 |
| `corpus/live/r74-simplifier/watch-landing3.sh:9` | `src=$(git diff --name-only HEAD -- corpus/fixtures/measure_audio.py corpus/fixtures/build_artifacts.py \| wc -l)` | D | R1 |
| `corpus/live/r75-baseline/build_env.py:27` | `git *args` | W | R5 |
| `corpus/live/r75-baseline/build_env.py:32` | `git ls-tree -r --name-only FROZEN` | D | R1 |
| `corpus/live/r75-baseline/build_env.py:38` | `git show f"{FROZEN}:{rel}"` | D | R1 |
| `corpus/live/r75-baseline/compare.py:28` | `git show f"{ANCHOR}:{path}"` | D | R1 |
| `corpus/live/r75-baseline/compare.py:43` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r75-baseline/compare.py:65` | `git ls-tree -r --name-only ANCHOR corpus/live/runs` | D | R1 |
| `corpus/live/r75-baseline/semantic_compare.py:103` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r75-baseline/semantic_compare.py:120` | `git show f"{ANCHOR}:{crel}"` | D | R1 |
| `corpus/live/r75-scribe/newparser_audit.py:34` | `git hash-object str(FIX)` | D | R3 |
| `corpus/live/r75-scribe/poll-landing.sh:9` | `head1=$(git log --oneline -1 \| cut -c1-7)` | D | R1 |
| `corpus/live/r75-scribe/poll-landing.sh:10` | `fblob=$(git hash-object corpus/fixtures/measure_audio.py \| cut -c1-12)` | D | R3 |
| `corpus/live/r75-scribe/poll-landing.sh:19` | `newcommits=$(git log --oneline "$base"..HEAD 2>/dev/null \| wc -l)` | D | R1 |
| `corpus/live/r75-scribe/poll-landing.sh:23` | `echo "$ts LANDED: $(git log --oneline "$base"..HEAD \| head -5)" >> "$LOG"` | D | R1 |
| `corpus/live/r75-scribe/watch.sh:7` | `head1=$(git log --oneline -1 \| cut -c1-7)` | D | R1 |
| `corpus/live/r75-scribe/watch.sh:8` | `fblob=$(git hash-object corpus/fixtures/measure_audio.py \| cut -c1-12)` | D | R3 |
| `corpus/live/r75-scribe/watch.sh:17` | `dirty=$(git status --porcelain --untracked-files=no \| wc -l)` | D | R2 |
| `corpus/live/r75-scribe/watch.sh:18` | `r74dirty=$(git status --porcelain --untracked-files=no \| grep -c 'r74' )` | D | R2 |
| `corpus/live/r75-simplifier/watch-landing.sh:11` | `head=$(git rev-parse --short HEAD)` | D | R1 |
| `corpus/live/r75-simplifier/watch-landing.sh:12` | `fixture=$(git status --porcelain -- corpus/fixtures/measure_audio.py 2>/dev/null \| wc -l)` | D | R2 |
| `corpus/live/r75-simplifier/watch-revisions.sh:16` | `git diff -- corpus/fixtures/measure_audio.py > "$S/landing-snapshot$n.diff"` | D | R1 |
| `corpus/live/r75-simplifier/watch-revisions.sh:17` | `lines=$(git diff --stat -- corpus/fixtures/measure_audio.py \| tail -1)` | D | R1 |
| `corpus/live/r76-baseline/build_env.py:27` | `git *args` | W | R5 |
| `corpus/live/r76-baseline/build_env.py:32` | `git ls-tree -r --name-only FROZEN` | D | R1 |
| `corpus/live/r76-baseline/build_env.py:38` | `git show f"{FROZEN}:{rel}"` | D | R1 |
| `corpus/live/r76-baseline/compare.py:28` | `git show f"{ANCHOR}:{path}"` | D | R1 |
| `corpus/live/r76-baseline/compare.py:43` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r76-baseline/compare.py:65` | `git ls-tree -r --name-only ANCHOR corpus/live/runs` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:24` | `git rev-parse HEAD` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:29` | `git *a` | W | R5 |
| `corpus/live/r76-baseline/postcommit_verify.py:36` | `git log -1 --format=%s NEW` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:39` | `git rev-parse f"{ref}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:40` | `git show f"{ref}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:43` | `git ls-tree -r OLD corpus/live/runs` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:44` | `git ls-tree -r NEW corpus/live/runs` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:51` | `git diff --name-only OLD NEW` | D | R1 |
| `corpus/live/r76-baseline/postcommit_verify.py:56` | `git diff OLD NEW -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r76-baseline/semantic_compare.py:103` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r76-baseline/semantic_compare.py:120` | `git show f"{ANCHOR}:{crel}"` | D | R1 |
| `corpus/live/r76-boundary/probe_boundary_r76.py:764` | `git -C str(ROOT) rev-parse HEAD` | D | R1 |
| `corpus/live/r77-baseline/build_env.py:25` | `git *args` | W | R5 |
| `corpus/live/r77-baseline/build_env.py:30` | `git ls-tree -r --name-only FROZEN` | D | R1 |
| `corpus/live/r77-baseline/build_env.py:36` | `git show f"{FROZEN}:{rel}"` | D | R1 |
| `corpus/live/r77-baseline/build_env_post.py:26` | `git *args` | W | R5 |
| `corpus/live/r77-baseline/build_env_post.py:31` | `git ls-tree -r --name-only PIN` | D | R1 |
| `corpus/live/r77-baseline/build_env_post.py:36` | `git show f"{PIN}:{rel}"` | D | R1 |
| `corpus/live/r77-baseline/commit_watch.py:22` | `git *a` | W | R5 |
| `corpus/live/r77-baseline/commit_watch.py:34` | `git rev-parse HEAD` | D | R1 |
| `corpus/live/r77-baseline/commit_watch.py:37` | `git log -1 --format=%s head` | D | R1 |
| `corpus/live/r77-baseline/commit_watch.py:38` | `git diff --name-only FROZEN head` | D | R1 |
| `corpus/live/r77-baseline/compare.py:29` | `git show f"{ANCHOR}:{path}"` | D | R1 |
| `corpus/live/r77-baseline/compare.py:44` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r77-baseline/compare.py:66` | `git ls-tree -r --name-only ANCHOR corpus/live/runs` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:25` | `git rev-parse HEAD` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:30` | `git *a` | W | R5 |
| `corpus/live/r77-baseline/postcommit_verify.py:37` | `git log -1 --format=%s NEW` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:40` | `git rev-parse f"{ref}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:41` | `git show f"{ref}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:44` | `git ls-tree -r OLD corpus/live/runs` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:45` | `git ls-tree -r NEW corpus/live/runs` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:52` | `git diff --name-only OLD NEW` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:53` | `git diff --shortstat OLD NEW` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:58` | `git diff OLD NEW -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r77-baseline/postcommit_verify.py:78` | `git rev-parse f'{ref}:corpus/fixtures/measure_audio.py'` | D | R1 |
| `corpus/live/r77-baseline/postreplay_check.py:32` | `git *a` | W | R5 |
| `corpus/live/r77-baseline/postreplay_check.py:41` | `git show f"{FROZEN}:corpus/{rel}"` | D | R1 |
| `corpus/live/r77-baseline/postreplay_check.py:60` | `git rev-parse f"HEAD:{lr}"` | D | R1 |
| `corpus/live/r77-baseline/postreplay_check.py:61` | `git rev-parse f"{FROZEN}:{lr}"` | D | R1 |
| `corpus/live/r77-baseline/postreplay_check.py:62` | `git show f"{FROZEN}:{lr}"` | D | R1 |
| `corpus/live/r77-baseline/semantic_compare.py:104` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r77-baseline/semantic_compare.py:121` | `git show f"{ANCHOR}:{crel}"` | D | R1 |
| `corpus/live/r78-baseline/build_env.py:25` | `git *args` | W | R5 |
| `corpus/live/r78-baseline/build_env.py:30` | `git ls-tree -r --name-only FROZEN` | D | R1 |
| `corpus/live/r78-baseline/build_env.py:36` | `git show f"{FROZEN}:{rel}"` | D | R1 |
| `corpus/live/r78-baseline/build_env_post.py:25` | `git *args` | W | R5 |
| `corpus/live/r78-baseline/build_env_post.py:33` | `git ls-tree -r -z --name-only anchor` | D | R1 |
| `corpus/live/r78-baseline/build_env_post.py:38` | `git show f"{anchor}:{rel}"` | D | R1 |
| `corpus/live/r78-baseline/census.py:30` | `git *a` | W | R5 |
| `corpus/live/r78-baseline/census.py:47` | `git ls-tree -r --name-only FROZEN corpus/live/runs/` | D | R1 |
| `corpus/live/r78-baseline/census.py:51` | `git ls-tree -r --name-only HEAD corpus/live/runs/` | D | R1 |
| `corpus/live/r78-baseline/census.py:79` | `git ls-tree -r -z --name-only FROZEN` | D | R1 |
| `corpus/live/r78-baseline/census.py:93` | `git rev-parse f"{ref}:{led}"` | D | R1 |
| `corpus/live/r78-baseline/census.py:97` | `git rev-parse HEAD` | D | R1 |
| `corpus/live/r78-baseline/census.py:99` | `git status --porcelain --untracked-files=no` | D | R2 |
| `corpus/live/r78-baseline/census.py:112` | `git ls-files corpus/artifacts` | D | R2 |
| `corpus/live/r78-baseline/census.py:115` | `git show f"{FROZEN}:{rel}"` | D | R1 |
| `corpus/live/r78-baseline/commit_watch.py:22` | `git *a` | W | R5 |
| `corpus/live/r78-baseline/commit_watch.py:34` | `git rev-parse HEAD` | D | R1 |
| `corpus/live/r78-baseline/commit_watch.py:37` | `git log -1 --format=%s head` | D | R1 |
| `corpus/live/r78-baseline/commit_watch.py:38` | `git diff --name-only FROZEN head` | D | R1 |
| `corpus/live/r78-baseline/compare.py:27` | `git show f"{ANCHOR}:{path}"` | D | R1 |
| `corpus/live/r78-baseline/compare.py:42` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r78-baseline/compare.py:93` | `git ls-tree -r --name-only ANCHOR corpus/live/runs/` | D | R1 |
| `corpus/live/r78-baseline/semantic_compare.py:103` | `git show f"{ANCHOR}:corpus/live/r70-author/ledger-r71.tsv"` | D | R1 |
| `corpus/live/r78-baseline/semantic_compare.py:127` | `git show f"{ANCHOR}:{crel}"` | D | R1 |
| `corpus/live/r78-simplifier/build_env.py:24` | `git *args` | W | R5 |
| `corpus/live/r78-simplifier/build_env.py:28` | `git ls-tree -r -z --name-only ANCHOR` | D | R1 |
| `corpus/live/r78-simplifier/build_env.py:32` | `git show f"{ANCHOR}:{rel}"` | D | R1 |
| `corpus/live/r80-baseline/archive-tree.sh:8` | `HEAD=$(git rev-parse HEAD)` | D | R1 |
| `corpus/live/r80-baseline/archive-tree.sh:10` | `git archive --format=tar "$HEAD" > /tmp/r80-baseline-work/head-${HEAD:0:7}.tar` | D | R1 |
| `corpus/live/r80-baseline/archive-tree.sh:23` | `git ls-tree -r -z --name-only "$HEAD" \| tr '\0' '\n' \| LC_ALL=C sort > /tmp/r80-baseline-work/ls-tree.txt` | D | R1 |
| `corpus/live/r80-baseline/battery.sh:13` | `"$1" "$(git rev-parse --short HEAD)" "$(sha256sum "$FIX" \| cut -d' ' -f1)"` | D | R1 |
| `corpus/live/r80-baseline/env.sh:10` | `echo "HEAD: $(git rev-parse HEAD)"` | D | R1 |
| `corpus/live/r80-baseline/env.sh:11` | `echo "HEAD_subject: $(git log --oneline -1)"` | D | R1 |
| `corpus/live/r80-baseline/env.sh:14` | `echo "fixture_dirty_vs_HEAD: '$(git status --porcelain -- corpus/fixtures/measure_audio.py)'"` | D | R2 |
| `corpus/live/r80-baseline/watch.sh:11` | `"$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r80-baseline/watch.sh:13` | `"$(git status --porcelain \| wc -l)" >> "$OUT"` | D | R2 |
| `corpus/live/r81-author/battery.sh:15` | `"$1" "$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r81-baseline/archive-tree.sh:8` | `HEAD=$(git rev-parse HEAD)` | D | R1 |
| `corpus/live/r81-baseline/archive-tree.sh:10` | `git archive --format=tar "$HEAD" > /tmp/r81-baseline-work/head-${HEAD:0:7}.tar` | D | R1 |
| `corpus/live/r81-baseline/archive-tree.sh:23` | `git ls-tree -r -z --name-only "$HEAD" \| tr '\0' '\n' \| LC_ALL=C sort > /tmp/r81-baseline-work/ls-tree.txt` | D | R1 |
| `corpus/live/r81-baseline/battery.sh:24` | `"$1" "$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r81-baseline/env.sh:10` | `echo "HEAD: $(git rev-parse HEAD)"` | D | R1 |
| `corpus/live/r81-baseline/env.sh:11` | `echo "HEAD_subject: $(git log --oneline -1)"` | D | R1 |
| `corpus/live/r81-baseline/env.sh:14` | `echo "fixture_git_blob: $(git rev-parse HEAD:corpus/fixtures/measure_audio.py)"` | D | R1 |
| `corpus/live/r81-baseline/env.sh:15` | `echo "fixture_dirty_vs_HEAD: '$(git status --porcelain -- corpus/fixtures/measure_audio.py)'"` | D | R2 |
| `corpus/live/r81-baseline/watch.sh:11` | `"$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r81-baseline/watch.sh:13` | `"$(git status --porcelain -- corpus/fixtures/measure_audio.py \| tr -d '\n')" \` | D | R2 |
| `corpus/live/r81-verifier2/battery.sh:16` | `"$1" "$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r82-author/battery.sh:17` | `"$1" "$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r82-baseline/archive-tree.sh:8` | `HEAD=$(git rev-parse HEAD)` | D | R1 |
| `corpus/live/r82-baseline/archive-tree.sh:10` | `git archive --format=tar "$HEAD" > /tmp/r82-baseline-work/head-${HEAD:0:7}.tar` | D | R1 |
| `corpus/live/r82-baseline/archive-tree.sh:23` | `git ls-tree -r -z --name-only "$HEAD" \| tr '\0' '\n' \| LC_ALL=C sort > /tmp/r82-baseline-work/ls-tree.txt` | D | R1 |
| `corpus/live/r82-baseline/archive-tree.sh:32` | `echo "tree_fixture_git_blob: $(git rev-parse "$HEAD:corpus/fixtures/measure_audio.py")"` | D | R1 |
| `corpus/live/r82-baseline/battery.sh:22` | `"$1" "$(git rev-parse --short HEAD)" \` | D | R1 |
| `corpus/live/r82-baseline/env.sh:10` | `echo "HEAD: $(git rev-parse HEAD)"` | D | R1 |
| `corpus/live/r82-baseline/env.sh:11` | `echo "HEAD_subject: $(git log --oneline -1)"` | D | R1 |
| `corpus/live/r82-baseline/env.sh:14` | `echo "fixture_git_blob: $(git rev-parse HEAD:corpus/fixtures/measure_audio.py)"` | D | R1 |
| `corpus/live/r82-baseline/env.sh:15` | `echo "fixture_dirty_vs_HEAD: '$(git status --porcelain -- corpus/fixtures/measure_audio.py)'"` | D | R2 |
| `corpus/live/r82-baseline/env.sh:46` | `echo "HEAD: $(git rev-parse HEAD)"` | D | R1 |
| `corpus/live/r82-baseline/post-state.sh:8` | `echo "HEAD: $(git rev-parse HEAD)"` | D | R1 |
| `corpus/live/r82-baseline/post-state.sh:9` | `echo "HEAD_subject: $(git log --oneline -1)"` | D | R1 |
| `corpus/live/r82-baseline/post-state.sh:12` | `echo "worktree_tracked_dirty: '$(git status --porcelain --untracked-files=no \| tr '\n' ';')'"` | D | R2 |
| `corpus/live/r82-baseline/watch.sh:15` | `head=$(git rev-parse --short HEAD)` | D | R1 |
| `corpus/live/r84-simplifier/run-all.sh:36` | `REPO="$(git -C . rev-parse --show-toplevel)"` | D | R1 |
| `corpus/live/r84-simplifier/run-all.sh:41` | `git -C "$REPO" apply --check corpus/live/r84-simplifier/r84-simplifier.patch \` | D | R4 |
| `corpus/live/r84-simplifier/run-all.sh:45` | `git -C "$REPO" apply --numstat corpus/live/r84-simplifier/r84-simplifier.patch` | D | R4 |
| `corpus/live/r85-critic/arm-replay-gaps.py:30` | `git show f"{COMMIT}:corpus/fixtures/measure_audio.py"` | D | R1 |
| `corpus/live/r85-critic/arm-replay.py:26` | `git show f"{COMMIT}:corpus/fixtures/measure_audio.py"` | D | R1 |
| `corpus/live/r85-simplifier/run-all.sh:41` | `REPO="$(git -C . rev-parse --show-toplevel)"` | D | R1 |
| `corpus/live/r85-simplifier/run-all.sh:46` | `git -C "$REPO" apply --check corpus/live/r85-simplifier/r85-simplifier.patch \` | D | R4 |
| `corpus/live/r85-simplifier/run-all.sh:50` | `git -C "$REPO" apply --numstat corpus/live/r85-simplifier/r85-simplifier.patch` | D | R4 |
| `corpus/live/r86-critic/arm-replay.py:21` | `git -C str(REPO) show fa5994a0:corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r86-critic/locktest_child.py:20` | `git -C REPO show fa5994a0:corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r86-simplifier/proofs/run-all.sh:7` | `REPO="$(git rev-parse --show-toplevel)"` | D | R1 |
| `corpus/live/r86-simplifier/proofs/run-all.sh:12` | `git -C "$REPO" show "$PIN:corpus/fixtures/measure_audio.py" \` | D | R1 |
| `corpus/live/r86-simplifier/proofs/run-all.sh:15` | `git -C "$REPO" show "$PIN" -- corpus/fixtures/measure_audio.py \` | D | R1 |
| `corpus/live/r86-simplifier/proofs/run-all.sh:68` | `git -C "$REPO" apply --check --numstat "$PWD/../r86-simplifier.patch"` | D | R4 |
| `corpus/live/r87-critic/arm-replay-gaps.py:22` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r87-critic/arm-replay.py:29` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r87-critic/locktest.py:42` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:22` | `git -C str(REPO) *args` | W | R5 |
| `corpus/live/r87-reviewer/r87r_pin.py:27` | `git show f"{rev}:{path}"` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:33` | `git rev-parse COMMIT` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:34` | `git log -1 --format=%s COMMIT` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:35` | `git diff --numstat PARENT COMMIT` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:39` | `git show f"{COMMIT}:corpus/fixtures/measure_audio.py"` | D | R1 |
| `corpus/live/r87-reviewer/r87r_pin.py:43` | `git hash-object -t blob --stdin --path=corpus/fixtures/measure_audio.py` | D | R3 |
| `corpus/live/r87-reviewer/r87r_pin.py:45` | `git -C str(REPO) hash-object -t blob --stdin` | D | R3 |
| `corpus/live/r87-scribe/build-receipts.py:147` | `git ls-files --error-unmatch str(p.relative_to(LANE))` | D | R2 |
| `corpus/live/r87-simplifier/proofs/run-all.sh:24` | `git show d1e687b9 -- corpus/fixtures/measure_audio.py > "$HERE/r87-diff.patch"` | D | R1 |
| `corpus/live/r87-simplifier/proofs/run-all.sh:49` | `{ git apply --check "$SEAT/r87-simplifier.patch" && echo "git apply --check CLEAN"` | D | R4 |
| `corpus/live/r87-simplifier/proofs/run-all.sh:50` | `git apply --numstat "$SEAT/r87-simplifier.patch"` | D | R4 |
| `corpus/live/r88-simplifier/proofs/fold-r88-simplifier.py:127` | `git diff --no-index --no-color -- base-measure_audio.py folded/measure_audio.py` | D | R1 |
| `corpus/live/r88-simplifier/proofs/fold-r88-simplifier.py:148` | `git apply --numstat fold.diff` | D | R4 |
| `corpus/live/r88-simplifier/proofs/observations.py:57` | `git status --short -- corpus/fixtures/__pycache__/` | D | R2 |
| `corpus/live/r88-simplifier/proofs/observations.py:67` | `git rev-parse --short HEAD` | D | R1 |
| `corpus/live/r88-simplifier/proofs/observations.py:70` | `git show HEAD:corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r88-simplifier/proofs/observations.py:71` | `git diff --numstat HEAD -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r88-simplifier/proofs/run-all.sh:43` | `echo "-- numstat:"; git -C "$TREE" apply --numstat "$HERE/fold.diff"` | D | R4 |
| `corpus/live/r88-simplifier/proofs/run-all.sh:44` | `echo "-- check:"; git -C "$TREE" apply --check "$HERE/fold.diff" && echo "clean"` | D | R4 |
| `corpus/live/r88-simplifier/proofs/run-all.sh:57` | `git -C "$TREE" status --short -- corpus/fixtures/measure_audio.py \` | D | R2 |
| `corpus/live/r88-simplifier/proofs/static-proofs.py:46` | `git diff c19bec96^ c19bec96 -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r88-simplifier/proofs/static-proofs.py:236` | `git apply --numstat DIFF` | D | R4 |
| `corpus/live/r88-simplifier/proofs/static-proofs.py:240` | `git apply --check DIFF` | D | R4 |
| `corpus/live/r88-simplifier/proofs/static-proofs.py:260` | `git diff --numstat HEAD -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r89-boundary/r89b_probe.py:456` | `git rev-parse --short HEAD` | D | R1 |
| `corpus/live/r89-boundary/r89b_probe.py:459` | `git status --short` | D | R2 |
| `corpus/live/r89-boundary/r89b_probe.py:927` | `git status --short` | D | R2 |
| `corpus/live/r89-critic/locktest.py:32` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r89-critic/mutate.py:32` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r89-critic/nested_sweep.py:24` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r89-critic/replay.py:28` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r89-critic/sweep.py:23` | `git show f"{COMMIT}:{FIXTURE}"` | D | R1 |
| `corpus/live/r89-simplifier/proofs/fold-r89-simplifier.py:146` | `git diff --no-index --no-color -- base-measure_audio.py folded/measure_audio.py` | D | R1 |
| `corpus/live/r89-simplifier/proofs/fold-r89-simplifier.py:150` | `git hash-object BASE` | D | R3 |
| `corpus/live/r89-simplifier/proofs/fold-r89-simplifier.py:152` | `git hash-object OUT` | D | R3 |
| `corpus/live/r89-simplifier/proofs/fold-r89-simplifier.py:168` | `git apply --numstat os.path.join(HERE, "fold.diff")` | D | R4 |
| `corpus/live/r89-simplifier/proofs/run-all.sh:21` | `git -C "$TREE" apply --check "$PROOFDIR/fold.diff" \` | D | R4 |
| `corpus/live/r89-simplifier/proofs/run-all.sh:23` | `git -C "$TREE" apply --numstat "$PROOFDIR/fold.diff"` | D | R4 |
| `corpus/live/r89-simplifier/proofs/run-all.sh:49` | `git -C "$TREE" diff --quiet HEAD -- corpus/fixtures/measure_audio.py \` | D | R1 |
| `corpus/live/r89-simplifier/proofs/static-proofs.py:46` | `git diff 0d732989^ 0d732989 -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r89-simplifier/proofs/static-proofs.py:276` | `git apply --numstat DIFF` | D | R4 |
| `corpus/live/r89-simplifier/proofs/static-proofs.py:281` | `git apply --check DIFF` | D | R4 |
| `corpus/live/r89-simplifier/proofs/static-proofs.py:330` | `git diff --quiet HEAD -- corpus/fixtures/measure_audio.py` | D | R1 |
| `corpus/live/r91-simplifier/landcheck.py:28` | `git show f"{spec}:corpus/fixtures/" "measure_audio.py"` | D | R1 |
| `reports/round-1-calibration/count_checklist.py:20` | `git -C str(ROOT) *args` | W | R5 |
| `reports/round-1-calibration/count_checklist.py:49` | `git rev-parse --verify sys.argv[1] + "^{commit}"` | D | R1 |
| `reports/round-1-calibration/count_checklist.py:50` | `git show revision + ":SHONEN.md"` | D | R1 |
| `reports/round-1-calibration/count_checklist.py:51` | `git ls-tree -r -z --name-only revision` | D | R1 |

## Appendix B — read-only commands used

```
# live state (read-only)
cd /home/vgpnk/Projects/shokunin/audio-shokunin
cat .git/HEAD
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD; git rev-parse origin/main
git status --porcelain --untracked-files=no
git worktree list
ls -1 .git/hooks
git config --local/--global/--system --get core.hooksPath
git config --get-all core.attributesFile
git config --get core.autocrlf; git config --get core.eol; git config --get core.safecrlf
git check-attr -a -- corpus/fixtures/measure_audio.py corpus/artifacts/ui.wav SHONEN.md .gitignore
find . -name .gitattributes -not -path './.git/*'
git lfs ls-files
# scan
find . -path ./.git -prune -o -type f -name '*.py' -print | wc -l   # 1213
find . -path ./.git -prune -o -type f -name '*.sh' -print | wc -l   # 167
```

Rebuild the static-site dataset with the AST scanner described in §1 (subprocess `["git", ...]` first element plus local `git(...)` wrappers), then classify the first subcommand token. The 234-row result is Appendix A; counts are in §3.1.

## Appendix C — sandbox experiments (jj 0.45.1, git 2.56.0)

All experiments were run in `/fast/scratch/jj-wave/JjAuditAudio-2/exp1` and `exp2`, each with a sandbox `git init --bare -b main origin.git`, a clone, and `jj git init --colocate`; the repo config mirrored the helper (`snapshot.auto-track="none()"`, `trunk()="main@origin"`, `bookmark track main@origin`). No live repo was contacted and no real remote was pushed to.

Observed:
- after `jj git init --colocate`: HEAD attached (`ref: refs/heads/main`), `@{u}` works;
- after the first `jj commit`: `.git/HEAD` is a raw hash, `symbolic-ref` rc=1, `--abbrev-ref HEAD` → `HEAD`, `@{u}` rc=128, `branch -vv` → `* (no branch)`;
- `git rev-parse HEAD`, `git show HEAD:<path>`, `git ls-tree`, `git log`, `git archive HEAD`, `git hash-object`, `git rev-parse --show-toplevel` all still work detached;
- `git add` staging survives `jj file track`, is wiped by `jj describe`/`jj commit`; `git diff --cached` then empty;
- after `jj commit -- a.txt`, HEAD != `refs/heads/main` until `jj bookmark set`; a new file left in @ appears as empty-blob intent-to-add in `git ls-files -s`/`git rev-parse :path`, while `git hash-object` returns the real content hash; `status --porcelain --untracked-files=no` still shows it;
- after `jj bookmark set main -r @-` + `jj git push -b main`, HEAD == `refs/heads/main` == `refs/remotes/origin/main` (detached), and `git merge-base --is-ancestor HEAD main` rc=0.

The sandbox was removed after the audit; no failure state was preserved.
