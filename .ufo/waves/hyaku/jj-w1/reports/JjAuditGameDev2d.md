# JjAuditGameDev2d — static git audit of `game-dev-2d-shokunin`

- Lane: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`
- Branch: `main`, HEAD `bce53b83a21ea43ddc2bf050bfe78cb4f2b68550`, upstream `origin/main`
- Lane VCS today: plain git, **no `.jj`** (`ls .jj` → `No such file or directory`); 42,566 tracked files
- jj under test: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`; all behaviour below was measured in
  `/fast/scratch/jj-wave/JjAuditGameDev2d-2/` (removed after the run; reproduction commands in §6)
- Mode: static read-only on the lane. Every git command run against the lane was read-only plumbing
  (`rev-parse`, `log`, `ls-files`, `ls-tree`, `show`, `status`, `cat-file`, `check-ignore`, `config` queries).
  No `add`, `commit`, `stash`, `checkout`, `reset`, `fetch`, `pull`, `push`, `merge`, `clean` or `tag` was run
  against a live repo. **No `jj` command ever ran with a working directory or `-R` under
  `/home/vgpnk/Projects/shokunin`.** No live repo was written, staged, checked out or fetched by me; the only
  side effect of the allowed read-only plumbing is that `git status` can refresh `.git/index` (§6 S11).
- Tool installs: **none**.

## 1. Scope and enumeration

The assignment's named set does not exist at this lane's root. `game-dev-2d-shokunin` is one of the few lanes
with no `SKILL.md` on any branch and no top-level tooling directory.

```
$ git ls-tree --name-only HEAD
LOG.md  PROVINCE.md  README.md  SCORECARD.md  SHONEN.md  considerthese  corpus  reports
$ for d in tools scripts verifiers; do test -e "$d" && echo "$d"; done
(no output)
$ git ls-files | grep -E '^SKILL\.md$|^(tools|scripts|verifiers)/'
(no output)
$ git log --all --oneline -- SKILL.md
(no output)                       # also empty in origin/main, origin/devin/wiki-link, wt-r98, wt-r99, wt-r100
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \)
(no output)
```

So the assignment's first, third and fourth bullets are empty by enumeration, not by omission. The lane's
executable surface is the per-round harnesses under `corpus/live/` and `reports/round-*/`, plus the
standing fixture battery `corpus/fixtures/*.py`. I audited **every** executable file in the lane:

| area | `.sh`/`.py`/`.mjs`/`.js`/`Makefile` files | invoke git (files) |
|---|---|---|
| `corpus/fixtures/` (the standing battery) | 4 | **0** |
| `corpus/live/` (round harnesses, frozen copies) | 1,522 | 48 |
| `reports/` (round mutation/verifier scripts) | 292 | 19 |
| repo root | 0 | 0 |
| **total** | **1,818** | **67 files / 155 lines / 159 invocations** |

The 1,818 are 1,623 `.py` plus 195 `.sh`; there is **no `.mjs`, `.js` or `Makefile` anywhere in the lane**,
so there are no Node `execFile`/`spawn`/`child_process` call sites — only shell commands and Python
`subprocess`/wrapper calls.

- `corpus/fixtures/run_battery.py` — the lane's actual gate, the file every round executes — contains **zero**
  git calls, so jj colocation cannot break the battery itself.
- 4 lines carry two git invocations each (`r95-scribe/static_audit.py:93`, `:404`,
  `r103-crit4-order.py:43`, `r105-count.sh:11`); the table lists both calls per line, hence 159 invocations
  on 155 lines.
- Excluded per assignment and by kind: `.git`, corpus prose (`corpus/**/*.md`, `corpus/knowledge/**`),
  `.ufo/` outputs, `corpus/live/runs/*/scratch/` (byte-copies of fixtures), and `reports/**/*.md`.
- 213 code lines match the token `git` case-sensitively; 155 are invocations, the rest are comments,
  docstrings, `print` text and one unified-diff literal (`diff --git …`) — each accounted for during review.

## 2. Classified call-site table

Classes: **A** assumes an attached branch HEAD or an upstream (`symbolic-ref`, `@{u}`, `--abbrev-ref HEAD`,
`branch --show-current`, HEAD used as a branch name); **B** mutates history, index or worktree (`add`, `commit`,
`stash`, `checkout`, `reset`, `rebase`, `push`, `pull`, `merge`, `clean`, `tag`, and `apply`); **C** reads index
or staging state (`status`, `diff` with no revision, `diff --cached`, `ls-files -s`, `update-index`); **D**
read-only based on a commit (`log`, `show`, `rev-parse`, `ls-tree`, `cat-file`, `grep`, `check-ignore`,
`archive`, plain `ls-files`, `diff <rev>`).

Risk codes (state under jj colocation — HEAD may be detached, jj owns the index):

- **D-ok** — committed-object read; works with a detached HEAD; no index dependency.
- **D-lsfiles** — index-driven membership; a path that jj has `file track`ed but not committed reads as
  untracked until the commit lands.
- **C-jjindex** — reads the git index/staging column; jj resets the index on mutation and a plain `git status`
  refreshes/rewrites it (observed, §6 S11).
- **C-scratch** — same command against a scratch directory outside the lane.
- **B-dryrun** — `apply --check` on the lane; mutates nothing.
- **B-scratch** — mutation-family call against an absent `/var/tmp` scratch directory.
- **B-checkout-scratch** — same, but `git checkout --` would silently revert a jj-snapshotted edit if ever
  retargeted at a colocated repo.

`<repo>` marks a `-C` expression from the source (`str(REPO)`, `REPO`, `"$LIVE"`, `{REPO}`); `{…}` marks a
non-literal argument kept as written. Every row is one invocation; the line is the exact source line.

| file:line | command | class | risk | jj-safe replacement |
|---|---|---|---|---|
| `corpus/live/r66-scribe/drive_surface.py:66` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r67-boundary/drive_boundary.py:55` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r67-boundary/drive_boundary.py:58` | `git status --porcelain corpus/fixtures/` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r67-boundary/drive_boundary.py:61` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r67-reviewer/reparent_gate_argv_check.py:2` | `git show cb84d0a^:corpus/fixtures/descendant_pipe_probe.gd` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r67-reviewer/reparent_gate_argv_check.py:3` | `git show HEAD:corpus/fixtures/descendant_pipe_probe.gd` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r67-scribe/drive_streams.py:43` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r68-reviewer/drive_divergence.py:36` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r68-reviewer/drive_divergence.py:238` | `git -C <repo> rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r71-scribe/watch.sh:4` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r71-scribe/watch.sh:9` | `git status --porcelain -- corpus/fixtures reports/round-71 corpus/live` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r71-scribe/watch.sh:10` | `git log -1 --format=%h` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r71-simplifier/wait_for_landing.sh:3` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r71-simplifier/watch.sh:3` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r71-simplifier/watch.sh:8` | `git status --porcelain -- corpus/fixtures reports/round-71` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r72-reviewer/watch.sh:3` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-reviewer/watch.sh:8` | `git status --porcelain -- corpus/fixtures reports/round-72 corpus/live` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r72-reviewer/watch.sh:9` | `git log -1 --format=%h` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-scribe/watch.sh:4` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-scribe/watch.sh:9` | `git status --porcelain -- corpus/fixtures reports/round-72 corpus/live` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r72-scribe/watch.sh:10` | `git log -1 --format=%h` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-simplifier/snapshot_loop.sh:3` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-simplifier/wait_for_landing.sh:4` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-simplifier/wait_for_landing.sh:8` | `git log -1 --format=%h` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-simplifier/watch.sh:4` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r72-simplifier/watch.sh:9` | `git status --porcelain -- corpus/fixtures reports/round-72 corpus/live` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r72-simplifier/watch.sh:10` | `git log -1 --format=%h` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r88-baseline/run-reps.sh:12` | `git -C "$LIVE" rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r88-baseline/run-reps.sh:22` | `git -C "$LIVE" rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r89-baseline/run-reps.sh:12` | `git -C "$LIVE" rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r89-baseline/run-reps.sh:22` | `git -C "$LIVE" rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r89-verify2/scripts/cases_compare.py:32` | `git -C <repo> show 8cea888:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r89-verify2/scripts/cases_compare.py:37` | `git -C <repo> show ee20575:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r90-reviewer/verify_fresh.py:11` | `git show ee20575:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r91-critic/scripts/static_audit.py:169` | `git -C <repo> show --numstat 77d2f7e -- corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-critic/scripts/audit.py:23` | `git show {COMMIT}:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-critic/scripts/audit.py:28` | `git show --numstat --format= COMMIT` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-critic/scripts/audit.py:41` | `git rev-parse COMMIT + "^"` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-critic/scripts/audit.py:43` | `git show {COMMIT}^:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-critic/scripts/audit.py:48` | `git show {COMMIT}^:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/compare_runs.py:17` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/fixedfps_probe.py:21` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/forge_nullts.py:22` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/forge_rows_landed.py:17` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/nav_envelope.py:21` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/recompute_claims.py:23` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/static_folds.py:34` | `git show HEAD:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r92-scribe/audit/summarize_runs.py:9` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-reviewer/tools/static_audit.py:39` | `git show d9edb72:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/compare_runs.py:15` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/receipts_census.py:20` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/recompute.py:25` | `git -C <repo> show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/static_audit.py:51` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/static_audit.py:131` | `git diff --numstat HEAD~1 HEAD -- corpus/fixtures/` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/static_audit.py:133` | `git show HEAD~1:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/static_audit.py:174` | `git show spec` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-scribe/audit/static_audit.py:199` | `git show --name-only --format= HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r93-verifier/probes/provenance.py:50` | `git -C <repo> show --name-only --format= HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/classifier_properties.py:23` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/floor_gate.py:27` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/receipts_census.py:21` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/recompute.py:26` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:47` | `git show HEAD:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:75` | `git show --numstat --format=%H%n%P%n%s HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:76` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:77` | `git log -1 --format=%s` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:78` | `git log -1 --format=%P` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:82` | `git show HEAD~1:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r94-scribe/audit/static_audit.py:216` | `git ls-files corpus/live/{lane}` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r94-scribe/audit/static_audit.py:295` | `git status --porcelain -uno` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r94-scribe/audit/static_audit.py:297` | `git diff --numstat corpus/fixtures/run_battery.py` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r95-critic/scripts/hygiene.py:24` | `git show {rev}:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-reviewer/tools/audit_static.py:31` | `git show {rev}:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-reviewer/tools/author_runs.py:23` | `git show 9cd47507:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-reviewer/tools/author_runs.py:28` | `git ls-files corpus/live/runs` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r95-reviewer/tools/cross_session.py:36` | `git show 9cd47507:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/floor_gate.py:24` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/fresh_arms.py:55` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/receipts_census.py:23` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/recompute.py:24` | `git show HEAD:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:26` | `git show {AUDITED}:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:48` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:49` | `git rev-parse {AUDITED}~1` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:51` | `git status --porcelain -uno` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r95-scribe/audit/static_audit.py:59` | `git show --numstat --format=%H AUDITED` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:64` | `git show {AUDITED}~1:corpus/fixtures/run_battery.py` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:93` | `git cat-file -e HEAD:<p>` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:93` | `git show HEAD:{p}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:94` | `git ls-files --error-unmatch p` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r95-scribe/audit/static_audit.py:328` | `git ls-files corpus/live/{lane}` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r95-scribe/audit/static_audit.py:389` | `git ls-files --error-unmatch reports/round-95/r95-scout.md` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r95-scribe/audit/static_audit.py:395` | `git ls-files --error-unmatch reports/round-95/r95-boundary.md` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `corpus/live/r95-scribe/audit/static_audit.py:402` | `git diff --name-status AUDITED head` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:404` | `git show {AUDITED}:{p}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-scribe/audit/static_audit.py:404` | `git show {head}:{p}` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-simplifier/head_check.py:39` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-simplifier/head_check.py:43` | `git log -1 --format=%s LANDING` | D | D-ok | keep; cite an explicit sha/ref |
| `corpus/live/r95-simplifier/head_check.py:45` | `git status --porcelain --untracked-files=no` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `corpus/live/r95-simplifier/head_check.py:50` | `git -C <repo> show "%s:%s" % (LANDING, rel)` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-101/mutations/run-all-mutations.sh:6` | `git rev-parse --show-toplevel` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_s4_residual_gate.sh:35` | `git -C "$REPO" show "$REV:SCORECARD.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_s4_residual_gate.sh:36` | `git -C "$REPO" show "$REV:PROVINCE.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_s4_residual_gate.sh:105` | `git -C "$REPO" show "$REV:SCORECARD.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_s4_residual_gate.sh:115` | `git -C "$REPO" show "$REV:corpus/lessons/r10-export-launch.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:26` | `git -C "$REPO" status --porcelain corpus/lessons corpus/knowledge` | C | C-jjindex | `git diff --numstat HEAD -- <paths>` + `ls-files --others` |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:31` | `git -C "$REPO" show "$REV:$f"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:82` | `git -C "$REPO" show "$REV:SCORECARD.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:89` | `git -C "$REPO" show "$REV:corpus/lessons/r10-export-launch.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:97` | `git -C "$REPO" show "$REV:README.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:102` | `git -C "$REPO" show "$REV:README.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/mut07.py:91` | `git -C <repo> rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/r102-S3-inventory.py:76` | `git apply --check str(tmp)` | B | B-dryrun | none (`--check` mutates nothing) |
| `reports/round-102/mutations/r102-ver9-run.py:68` | `git apply str(WORK / "patches" / p)` | B | B-scratch | none (scratch target) |
| `reports/round-102/mutations/r102-ver9-scene_io.py:71` | `git apply str(WORK / "patches" / p)` | B | B-scratch | none (scratch target) |
| `reports/round-102/mutations/r102-w3-census.py:149` | `git -C {REPO} archive HEAD corpus/fixtures` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/r102-w3-census.py:198` | `git show HEAD:{rel}` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/r102-w3-census.py:209` | `git -C <repo> grep -I -o -F .shokunin/game-dev-2d/corpus/ HEAD -- corpus/lessons` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/r102-w3-census.py:216` | `git show HEAD:SCORECARD.md` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-102/mutations/r102-w3-census.py:220` | `git show HEAD:PROVINCE.md` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/mut06.py:721` | `git -C <repo> rev-parse --short HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/mut08.py:94` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/r103-S0-build_candidates.py:24` | `git -C <repo> show HEAD:{path}` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/r103-crit4-order.py:27` | `git checkout -- REL` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-103/mutations/r103-crit4-order.py:30` | `git apply -v str(p)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-order.py:43` | `git rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/r103-crit4-order.py:43` | `git status --porcelain` | C | C-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-order.py:47` | `git checkout -- REL` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-103/mutations/r103-crit4-order.py:48` | `git status --porcelain` | C | C-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:20` | `git -C <repo> show {HEAD}:{REL}` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-103/mutations/r103-crit4-proof.py:80` | `git checkout -- REL` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-103/mutations/r103-crit4-proof.py:81` | `git apply --check -v str(CAND)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:84` | `git status --porcelain` | C | C-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:86` | `git apply -v str(W5)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:88` | `git status --porcelain` | C | C-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:89` | `git apply --check -v str(CAND)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:92` | `git apply -v str(CAND)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:97` | `git checkout -- REL` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-103/mutations/r103-crit4-proof.py:98` | `git apply -v str(CAND)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:100` | `git apply --check -v str(W5)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:103` | `git apply -v str(W5)` | B | B-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-crit4-proof.py:109` | `git checkout -- REL` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-103/mutations/r103-crit4-proof.py:110` | `git status --porcelain` | C | C-scratch | none (scratch target) |
| `reports/round-103/mutations/r103-ver5-fold.py:315` | `git -C <repo> rev-parse HEAD` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-104/mutations/r104-C5-exposure-census.py:37` | `git ls-files` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `reports/round-104/mutations/r104-C5-exposure-census.py:42` | `git ls-files` | D | D-lsfiles | `git ls-tree -r --name-only <rev>` / `jj file list` |
| `reports/round-104/mutations/r104-C5-exposure-census.py:51` | `git cat-file -e "HEAD:" + p` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-104/mutations/r104-C5-exposure-census.py:56` | `git check-ignore -v probe` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-104/mutations/r104-W10-per-variant-reconcile.py:25` | `git -C <repo> checkout -q -- corpus/fixtures/run_battery.py` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-104/mutations/r104-W10-per-variant-reconcile.py:30` | `git -C <repo> apply str(M / p)` | B | B-scratch | none (scratch target) |
| `reports/round-104/mutations/r104-W10-variant-matrix.py:33` | `git -C <repo> checkout -q -- corpus/fixtures/run_battery.py` | B | B-checkout-scratch | none while `/var/tmp`; else `jj restore <path>` |
| `reports/round-104/mutations/r104-W10-variant-matrix.py:38` | `git -C <repo> apply str(M / p)` | B | B-scratch | none (scratch target) |
| `reports/round-105/r105-count.sh:4` | `git rev-parse --short "$R"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-count.sh:6` | `git show "$R:corpus/fixtures/run_battery.py"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-count.sh:10` | `git ls-tree --name-only "$R" corpus/knowledge/` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-count.sh:11` | `git ls-tree --name-only "$R" corpus/knowledge/` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-count.sh:11` | `git show "$R:$f"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-count.sh:12` | `git show "$R:corpus/SOURCES.md"` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-mapped-criteria.py:50` | `git rev-parse --verify {sys.argv[1]}^{{commit}}` | D | D-ok | keep; cite an explicit sha/ref |
| `reports/round-105/r105-mapped-criteria.py:60` | `git show {revision}:{path}` | D | D-ok | keep; cite an explicit sha/ref |

## 3. Counts per class

| class | invocations | where |
|---|---|---|
| **A** (attached HEAD / upstream assumed) | **0** | — |
| **B** (mutates history, index or worktree) | **20** | 13 × `git apply` (12 scratch, 1 live `--check`), 7 × `git checkout --` (all scratch) |
| **C** (reads index / staging state) | **16** | 15 × `git status --porcelain` (10 lane, 5 scratch), 1 × no-revision `git diff --numstat` (lane) |
| **D** (read-only, commit-based) | **123** | 115 object reads, 8 × `git ls-files` |

Per risk code: `D-ok` 115 · `D-lsfiles` 8 · `C-jjindex` 11 · `C-scratch` 5 · `B-scratch` 12 · `B-checkout-scratch` 7
· `B-dryrun` 1. Per verb: `show` 71, `rev-parse` 27, `status` 15, `apply` 13, `log` 8, `ls-files` 8,
`checkout` 7, `diff` 3, `ls-tree` 2, `cat-file` 2, `grep` 1, `check-ignore` 1, `archive` 1.

**No lane script invokes `git add`, `commit`, `push`, `fetch`, `pull`, `merge`, `rebase`, `stash`, `reset`,
`clean`, `tag`, `switch`, `restore`, `rm`, `mv`, `update-ref` or `worktree`** (exhaustive grep, §1 method).
`scripts/hyaku/jj-lane.sh` is therefore the sole writer to this lane repo — a clean cutover, with no competing
git commit path to retire.

## 4. Top three risks

1. **The lane's "is the tree clean / what changed" evidence is `git status`, and jj owns that index (11 lane
   sites).** Ten `status --porcelain` calls (`r67-boundary/drive_boundary.py:58`, the five `corpus/live/r71-*`
   and `r72-*` watchers, `r94-scribe/audit/static_audit.py:295`, `r95-scribe/audit/static_audit.py:51`,
   `r95-simplifier/head_check.py:45`, `reports/round-102/mutations/mut06_stale_cite_resurrection.sh:26`) plus
   one no-revision `git diff --numstat` (`r94-scribe/audit/static_audit.py:297`) are the lane's only
   worktree-state instrument; r94 calls the result `foreign_worktree_modification`. Two observed effects:
   (a) the first `git status` after a jj mutation **rewrites `.git/index`** (S11: inode and sha changed), i.e.
   a supposedly read-only audit writes the index jj manages; (b) the same bytes produce different porcelain
   strings before and after a jj mutation (`M ` staged → ` M` unstaged, S3/S7), so a watcher that hashes
   status output can change state with no file change, and a foreign edit staged with `git add` is invisible
   to `git diff` (worktree-vs-index). Replace with `git diff --numstat HEAD -- <paths>` plus
   `git ls-files --others --exclude-standard` (both index-independent), or `jj --ignore-working-copy diff`.
2. **`git ls-files` is used as "tracked", but jj's `file track` is invisible to git until the commit lands
   (8 sites).** `r104-C5-exposure-census.py:37,42` derives "tracked files total" and per-class censuses from
   `git ls-files`; `r94-scribe/audit/static_audit.py:216` and `r95-reviewer/tools/author_runs.py:28` count lane
   inventories; `r95-scribe/audit/static_audit.py:94,328,389,395` decide `"tracked": true/false` with
   `git ls-files --error-unmatch`. Observed (S4): after `jj file track corpus/fixtures/new_probe.gd`,
   `git ls-files` returns nothing, `ls-files --error-unmatch` exits 1 and `cat-file -e HEAD:…` exits 128; after
   the commit the path appears. A report written mid-round — the normal moment, before the closure commit —
   undercounts exactly the files the lane is about to land, and `"tracked": false` means "not committed",
   not "not tracked by jj". Use `git ls-tree -r --name-only <rev>` for the committed set and `jj file list`
   for the jj-tracked set, and print which set is meant.
3. **The 20 mutation-family calls are almost entirely dead scratch code, and the one live call checks the
   wrong tree (r102-S3-inventory.py:76).** Nineteen of twenty target `/var/tmp/r103c-C4/wt` or
   `/var/tmp/r104-W10/realtest`, or a copied tree under `/var/tmp/r102-ver9`; all three `/var/tmp` roots are
   absent now (`ls -d /var/tmp/r102* /var/tmp/r103c-C4 /var/tmp/r104-W10` → `No such file or directory`); they
   cannot touch the lane. The single live call, `git apply --check` at the lane
   root, is non-mutating and worked against a jj working copy (S6), but its docstring claims it checks "at
   HEAD" while `git apply --check` checks the **worktree**, which under jj is `@` and may hold uncommitted
   changes — a PASS/FAIL is reported for a tree the tool does not name. Latent hazard behind the scratch
   `checkout` calls: `git checkout -- <path>` restores from the git index jj resets, not from `@`; observed
   (S5) the worktree edit vanished while `jj diff -r @` still showed it, and the next `jj commit` snapshotted
   the reverted bytes (S7). If any of those 7 checkout sites is ever pointed at the lane, use `jj restore
   <path>`.

## 5. Hooks and attributes

```
$ find .git/hooks -maxdepth 1 -type f | wc -l                      → 14
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample' | wc -l   → 0
$ find .git/hooks -maxdepth 1 -type f -perm -u+x ! -name '*.sample' | wc -l → 0
$ git config --show-origin --get-all core.hooksPath ; echo rc=$?   → rc=1 (unset)
$ git config --show-origin --get-all init.templatedir ; echo rc=$? → rc=1 (unset)
$ git config --show-origin --get-all core.attributesfile ; echo rc=$? → rc=1 (unset)
$ git config --show-origin --get-all core.autocrlf ; echo rc=$?    → rc=1 (unset)
$ git config --show-origin --get-all core.eol ; echo rc=$?         → rc=1 (unset)
$ git ls-files | grep -c gitattributes                             → 0
$ find . -path ./.git -prune -o -name '.gitattributes' -print      → (no output)
$ ls .git/info/attributes                                          → No such file or directory
$ git config --show-origin --get-regexp '^filter\.'
file:/home/vgpnk/.config/git/config  filter.lfs.clean    git-lfs clean -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.smudge   git-lfs smudge -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.process  git-lfs filter-process
file:/home/vgpnk/.config/git/config  filter.lfs.required true
```

- **Git hooks in use: none.** All 14 `.git/hooks` entries are `*.sample` (mode 755, but git only runs a
  hook whose name lacks `.sample`); no `core.hooksPath`, no init template dir.
- **Attributes / eol rules: none.** No `.gitattributes` tracked or on disk, no `info/attributes`,
  `core.autocrlf` and `core.eol` unset. The global git-lfs filter definitions are inert because no attribute
  selects `filter=lfs`; the one `lfs` string in `git ls-files` is a filename
  (`corpus/live/r61-critic/critic_landed_selfsigkill.stdout`), not a pointer.
- `.gitignore` exists only at `corpus/.gitignore` and `corpus/live/.gitignore` (regenerable-tree and cache
  rules). It affects `git status`'s untracked display and jj's auto-track; the helper pins
  `snapshot.auto-track="none()"`, so it is not a filter/eol surface.
- **jj bypasses both, measured (0.45.1):** `jj commit` did not execute an executable `.git/hooks/pre-commit`
  (marker file absent), while `git commit -qam` did (S9); and an `eol=crlf` attribute left jj's worktree bytes
  LF where `git checkout --` wrote CRLF (S10). With no hooks or attributes today, colocation changes nothing
  here — but a future gate added to `.git/hooks` or `.gitattributes` would silently not run on jj commits.

## 6. Observed evidence (sandbox, jj 0.45.1)

Repo built with the helper's exact init recipe (`jj --config 'snapshot.auto-track="none()"' git init --colocate`,
then the four `jj config set --repo` keys and `jj bookmark track main@origin`), a sandbox bare `origin`, two
tracked files. All commands under `/fast/scratch/jj-wave/JjAuditGameDev2d-2/`; no live path touched.

**S1 — right after colocation: HEAD is still attached.**
```
$ git symbolic-ref -q HEAD        → refs/heads/main
$ git rev-parse --abbrev-ref HEAD → main
$ git rev-parse main@{u}          → f09014f0234b7f93d06bad58b62514625a4346bc
```

**S2 — a jj snapshot of a tracked edit is visible to git, and `HEAD:` still holds the pre-edit bytes.**
```
$ git status --porcelain                            →  M corpus/fixtures/run_battery.py
$ git diff --stat  → 1 file changed, 1 insertion(+), 1 deletion(-)
$ git show HEAD:corpus/fixtures/run_battery.py       → CASES = [("base", "x.gd", [], 0, "sig")]
```

**S3 — a `git add`-staged entry survives a read-only `jj status`, then is dropped by `jj commit`.**
```
[before jj]  $ git diff --cached --stat → SCORECARD.md | 1 +
$ jj status                             → staged entry still present
[after jj commit] $ git status --porcelain → " M SCORECARD.md"   (column 2, no longer staged)
                  $ git diff --cached --stat → (empty)
```

**S4 — `jj file track` is invisible to `git ls-files` until the commit lands.**
```
$ jj file track corpus/fixtures/new_probe.gd
$ git ls-files corpus/fixtures/new_probe.gd         → (empty)
$ git ls-files --error-unmatch corpus/fixtures/new_probe.gd
  error: pathspec '…' did not match any file(s) known to git        rc=1
$ git cat-file -e HEAD:corpus/fixtures/new_probe.gd
  fatal: path '…' exists on disk, but not in 'HEAD'                 rc=128
[after jj commit] $ git ls-files corpus/fixtures/new_probe.gd → listed
```

**S5 — `git checkout --` silently reverts a jj-snapshotted edit (worktree and `@` diverge).**
```
$ git checkout -- corpus/fixtures/run_battery.py
$ git status --porcelain                      → battery no longer listed
$ jj --ignore-working-copy diff --stat -r @   → corpus/fixtures/run_battery.py | 2 +-
```
The next `jj commit -- corpus/fixtures/run_battery.py` snapshotted the reverted bytes, and the commit did not
contain the edit.

**S6 — `git apply --check` works against the jj working copy (no mutation).**
```
$ git apply --check --verbose probe.patch → Checking patch SCORECARD.md...   rc=0
```

**S7 — after `jj commit`: HEAD is the committed commit and is detached.**
```
$ jj commit -m 'sandbox: jj commit' -- corpus/fixtures/run_battery.py corpus/fixtures/new_probe.gd
$ git rev-parse HEAD               → b8fcaf9d626ebce7ab316003a9a173737fbe87ab
$ git rev-parse main               → b8fcaf9d626ebce7ab316003a9a173737fbe87ab
$ git rev-parse --abbrev-ref HEAD  → HEAD
$ git symbolic-ref -q HEAD         → rc=1 (detached)
$ git rev-parse '@{u}'             → fatal: HEAD does not point to a branch
$ git show HEAD:corpus/fixtures/new_probe.gd → new file
$ git log -1 --format=%h           → b8fcaf9
$ git status --porcelain           →  M SCORECARD.md
```

**S8 — the pushed ref is addressable in git; `main@origin` is not.**
```
$ git rev-parse origin/main                        → b8fcaf9d626ebce7ab316003a9a173737fbe87ab
$ git merge-base --is-ancestor main origin/main; echo rc=$? → rc=0
$ git rev-parse main@origin  → fatal: ambiguous argument 'main@origin'   (that is a jj revset)
```

**S9 — jj does not run git hooks.**
```
# executable .git/hooks/pre-commit writes hook.log
$ jj commit -m 'hook probe' -- SCORECARD.md   → hook.log absent
$ git commit -qam 'hook probe git'            → hook.log contains "hook-fired"
```

**S10 — jj does not apply `eol` attributes.**
```
.gitattributes: *.txt text eol=crlf ; probe.txt contains "lf-only\n"
$ jj commit … -- probe.txt …                  → worktree bytes: l f - o n l y \n
$ git checkout -- probe.txt (plain git repo)  → worktree bytes: l f - o n l y \r \n
```

**S11 — a plain `git status` rewrites the jj-managed index.**
```
before:                           inode 1745254769  sha 4c1fb6230a98…bad67c7
after `git status --porcelain`:   inode 1745159888  sha 670d1ca6a7dc…088a7
after `git --no-optional-locks status`: unchanged (670d1ca6…)
```

**Live lane state (read-only).**
```
$ git rev-parse --abbrev-ref HEAD → main
$ git rev-parse --abbrev-ref --symbolic-full-name @{u} → origin/main
$ git rev-parse HEAD → bce53b83a21ea43ddc2bf050bfe78cb4f2b68550
$ ls -d .jj → No such file or directory
$ git ls-files | wc -l → 42566
```

## 7. [INFERENCE]

- The index-lock collision between a lane's `git status` and a concurrent `jj` mutation (both write
  `.git/index`) is inferred from S11; no concurrency test was run.
- Whether `/var/tmp/r103c-C4/wt` and `/var/tmp/r104-W10/realtest` were linked worktrees of the lane or plain
  copies cannot be determined from the tree: neither exists now and no setup script is committed. The risk
  codes assume "scratch, non-colocated" for those files.
- The `ls-files` undercount (S4) is bounded by the helper's `file track → commit` span. A seat that tracks
  early and commits late widens it; a seat that never tracks before `jj commit -- <paths>` has no window.
- The 71 `git show` invocations (with the 27 `rev-parse` and 8 `log` reads) are safe **as committed-object
  reads**: they resolve a rev and read the object, independent of HEAD attachment and the index. They are not
  evidence of the working copy (`@`); reports that describe them as "the worktree" would be wrong, and none do.
- jj behaviour is version-specific; every statement above was measured on `0.45.1-7c41cdeb16b6` only.

## 8. Recommendations

1. Replace the 11 lane-facing index reads (10 `status`, 1 no-rev `diff`) with
   `git diff --numstat HEAD -- <paths>` plus `git ls-files --others --exclude-standard`; keep `status` only
   for untracked detection, and add `--no-optional-locks` if it stays. This removes the only lane writes in
   the audit surface and removes the staged-column ambiguity.
2. Replace `git ls-files` / `--error-unmatch` in the four verifier tools with
   `git ls-tree -r --name-only <rev>` (committed set) or `jj file list` (jj-tracked set), and print which set
   the census means. Keep `cat-file -e HEAD:<p>` for committed membership — it is honest as written.
3. Delete or gate the 19 dead `/var/tmp` mutation calls; if the patch-order work is revived, retarget it at a
   throwaway copy and use `jj restore` / `jj file track` for revert/track. Keep `git apply --check` but name
   the tree it checks (`HEAD` via `--cached`-free object comparison, or the worktree explicitly).
4. Do not add git hooks or `.gitattributes` to this lane expecting jj commits to honour them (S9/S10). If a
   pre-commit gate is wanted, put it in `jj-lane.sh` or the lane protocol.
5. Any external gate over this lane must name `refs/heads/main` / `refs/remotes/origin/main`, never `@{u}` or
   `--abbrev-ref HEAD`; class A is empty inside the lane, and the only known HEAD-dependent code is the fleet
   helper's `detect_branch`, which is out of this scope.

## 9. Residual risk and verification gaps

- **No `tools/`, `scripts/`, `verifiers/` directory, no root-level code file, and no `SKILL.md` on any branch
  exists**, so the assignment's named surfaces are empty by enumeration. The report instead covers every
  executable file in the lane.
- Prose and history were not audited: `corpus/**/*.md`, `reports/**/*.md`, `LOG.md`, `SCORECARD.md` contain
  many `git …` citations; they are not executable and were excluded as "corpus prose".
- No lane script and no battery run was executed against the lane (no Godot runs); all findings are static
  reading plus the isolated sandbox experiments in §6.
- The live lane has no `.jj` at audit time; the first closure will colocate it. §6 models the post-`init`
  state, not a mid-round live lane.
- `corpus/live/**` and `reports/round-*/mutations/**` are per-round artifacts; some are dead (their
  `/var/tmp` targets are gone). They remain in scope because they are committed executable tooling.
- Sandbox `/fast/scratch/jj-wave/JjAuditGameDev2d-2/` was removed after the report was written.
