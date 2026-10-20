# JjAuditWatchdog — shokunin-watchdog.sh under jj-colocated lanes

Scope: `/home/vgpnk/Projects/shokunin/scripts/shokunin-watchdog.sh` (414 lines, HEAD `bee791e`),
specifically `render_prompt` (L172), `report_of` (L144), `record_report_baseline` (L120),
`launch_lane` (L193), `commit_evidence`/`lane_git` (L288-300) and `advance` (L344).

Method: read-only inspection of the live fleet; every jj command ran only under
`/fast/scratch/jj-wave/JjAuditWatchdog/` (jj 0.45.1). The live root was touched only with
`cat`/`ls`/`git log|status|rev-parse|ls-files`. No tool installs were needed.

## Call inventory (the whole git surface)

```
$ grep -nE '\bgit\b' scripts/shokunin-watchdog.sh
292:  git -C "$SHOKUNIN_ROOT" -c "user.name=${1}-shokunin" -c "user.email=${1}@shokunin.local" "${@:2}"
296:  git -C "$SHOKUNIN_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 0
```

There are exactly three invocations (`lane_git add`, `lane_git commit`, `rev-parse`), all against
`$SHOKUNIN_ROOT`. `render_prompt`, `report_of` and `record_report_baseline` run **zero** git
commands. Consequently:

- Colocating a lane repo whose `LANE_REPO` is not `.` is invisible to this script.
- The only colocation that changes this script's meaning is **the fleet root itself** — which is the
  lane repo for the two `.` lanes (`shokunin.conf:20-21`: `protocol|.|`, `aggregator|.|`) and the
  target of `commit_evidence` for **every** lane, not just `.` lanes.

## Findings

### F1 — `commit_evidence` is colocation-blind (High)

`scripts/shokunin-watchdog.sh:294-300`:

```sh
commit_evidence() { # lane n
  local lane="$1" f=".ufo/prompts/$1-round-$2.md"
  git -C "$SHOKUNIN_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 0
  [ -f "$SHOKUNIN_ROOT/$f" ] || return 0
  lane_git "$lane" add -- "$f" >/dev/null 2>&1 || return 0
  lane_git "$lane" commit -q -m "round-$2: ${lane} dispatch evidence" -- "$f" >/dev/null 2>&1 || true
}
```

Observed in a jj-colocated sandbox fleet root:

```
$ git -C <colocated-repo> rev-parse --is-inside-work-tree
true
```

The probe succeeds, so the function proceeds; nothing detects `.jj`. The function also returns 0
on every early exit and discards the commit's exit status with `|| true`.

### F2 — `git add` is wiped by any jj working-copy rewrite (High)

A staged prompt is preserved by snapshot-only jj commands but destroyed by commands that rewrite `@`:

```
$ git add -- .ufo/prompts/protocol-round-4.md; git diff --cached --name-only
.ufo/prompts/protocol-round-4.md
$ jj commit -m 'protocol lane round-3 work' -- .ufo/state/protocol.round
$ git diff --cached --name-only
(empty)
```

Matrix from a clean colocated repo (each row: stage a fresh prompt, run one jj command):

```
jj st                    staged[probe-1]                -> [probe-1]          ref=master HEAD=c2e2501
jj log -r @              staged[probe-1 probe-2]        -> [probe-1 probe-2]  ref=master HEAD=c2e2501
jj commit other path     staged[probe-1 probe-2 probe-3]-> []                  ref=DETACHED HEAD=399ad2d
jj new                   staged[probe-4]                -> []                  ref=DETACHED HEAD=73ebc29
jj bookmark set          staged[probe-5]                -> []                  ref=DETACHED HEAD=73ebc29
jj git export            staged[probe-6]                -> [probe-6]           ref=DETACHED HEAD=73ebc29
```

So the hazardous interleaving is precisely the lane's own commit path (`jj-lane.sh commit` runs
`jj commit`), not every `jj status`.

### F3 — after the wipe, `git commit -- <new prompt>` fails and the failure is swallowed (Critical)

A first-time prompt path is untracked once the index entry is gone, and a pathspec commit cannot
name a path git does not know:

```
$ git diff --cached --name-only          # after jj commit of another path
(empty)
$ git -c user.name=protocol-shokunin -c user.email=protocol@shokunin.local \
    commit -q -m 'partial after reset' -- .ufo/prompts/protocol-round-5.md
error: pathspec '.ufo/prompts/protocol-round-5.md' did not match any file(s) known to git
(exit 1)
```

End-to-end through the real function (deterministic `git` shim that runs one concurrent lane
`jj commit` immediately after `lane_git add` returns):

```
$ commit_evidence protocol 1; echo "commit_evidence rc=$?"
commit_evidence rc=0
after: ref=DETACHED HEAD=a529056 master=906e10f
evidence commit present anywhere? []            # git log --all --grep 'round-1: protocol dispatch evidence'
staged: []
prompt status: ?? .ufo/prompts/protocol-round-1.md
```

`commit_evidence` reported success and produced no commit. `advance` never checks its status
(`advance` L346 is a bare call; `set -u` only, no `set -e`), then logs
`complete <lane> round=N; advancing to round=N+1` (L360).

Natural-rate control (12 rounds, background lane doing `jj commit` in a loop): all 12 evidence
commits were created — but none on master (F4):

```
missing evidence commits: 0 / 12
master contains any dispatch evidence: 0
master=906e10f HEAD=df6aab8 ref=DETACHED
```

### F4 — with detached HEAD, the evidence commit never lands on the branch (High)

jj leaves git HEAD detached at `@-` after every working-copy rewrite (observed; the live fleet
root's own reflog shows the same mechanism, see L1). Then `git commit` moves HEAD only:

```
$ echo "HEAD=$(git rev-parse --short HEAD) master=$(git rev-parse --short master) ref=$(git symbolic-ref -q --short HEAD || echo DETACHED)"
HEAD=f7aa7f7 master=5aa8527 ref=DETACHED
$ git branch --contains HEAD --format='%(refname:short)'
(no branch)
$ git log --oneline master..HEAD
f7aa7f7 round-3: protocol dispatch evidence
```

jj then adopts the detached commit as `@-` on its next run, so it can become an ancestor of the
lane's next commit and reach master only when the helper moves the bookmark:

```
$ git log --graph --oneline --all
* 515f2e2 (HEAD) protocol lane round-3 work
* f7aa7f7 round-3: protocol dispatch evidence
* 5aa8527 (master) protocol lane round-2 work
```

After a helper-shaped `bookmark set master -r @-`, those commits did become ancestors of master
("dispatch-evidence commits reachable from master: 12"). But that is the lane's later jj write, not
`advance`; `commit_evidence` on its own no longer satisfies "dispatch evidence is on the branch
when the round is marked complete". If the lane never runs jj again (e.g. a `.` lane told to use
`fleet-commit.sh` for the fleet repo), the commit stays off-branch, reachable only via HEAD and
`refs/jj/keep/*`:

```
$ git for-each-ref --contains f7aa7f7 --format='%(refname)' | head
refs/jj/keep/...
```

Note the inverse case works: if HEAD is still attached (no lane jj mutation yet), the commit lands
on master and jj imports/updates the bookmark on its next run (`master` subject became
`round-1: protocol dispatch evidence`, and `jj` log showed `master*` at it). The breakage starts at
the lane's first `jj commit`/`jj new`.

### F5 — the complete path commits while the lane still runs (High)

`advance` (L344-376):

```
346  commit_evidence "$lane" "$n"
349    if [ -n "$mid" ] && ! kill_mission "$lane" "$mid" ...
356      if [ -n "$mid" ] && ! kill_mission "$lane" "$mid" ...
371    if [ -n "$mid" ] && ! kill_mission "$lane" "$mid" ...
```

The evidence commit happens **before** `kill_mission`, so while a `.` lane is still alive its cwd
is the fleet root and it can be running `jj commit` in the same repo — exactly the deterministic
failure in F3. The window is not hypothetical: the report just landed, so the lane is likely in its
final commit/push phase.

### F6 — driver runtime writes become jj working-copy input (Medium)

The live fleet root tracks 64 `.ufo/state` files (`git ls-files .ufo/state | wc -l` → 64:
`.gitkeep` plus 21 `.out`, 21 `.round`, 21 `.mission`; during the L1 probe below, 9
`.report-baseline` files were additionally in the index as intent-to-add). `launch_lane`
appends to `.ufo/state/<lane>.out` (L217) and writes `.mission`/`.round` (L219-220); `report_of`
and `record_report_baseline` read/write `.ufo/state`. In a colocated fleet root a snapshot sweeps
the tracked ones into the working-copy commit:

```
$ jj --ignore-working-copy diff --summary -r @
M .ufo/state/protocol.out
M .ufo/state/protocol.round
```

Prompts are also tracked (225 files under `.ufo/prompts`) and `render_prompt` writes them
non-atomically (`printf '%s\n' "$t" > "$out"`, L184). Rewriting a tracked prompt shows up as `M` in
`@`:

```
$ jj --ignore-working-copy diff --summary -r @
M .ufo/prompts/protocol-round-2.md
```

`record_report_baseline` itself is atomic (`tmp` + `mv -fT`, L127-136) and its file is untracked, so
`snapshot.auto-track="none()"` keeps it out of jj until something explicitly tracks it (see F7).

### F7 — the helper's `.ufo/state/*` guard does not match the directory (High, adjacent)

Because it directly exposes what `record_report_baseline` writes, observed in the sandbox:

```
$ jj-lane.sh commit <dir> --as protocol -m 'lane hygiene sweep' -- .ufo/state
committed 9cfafdfc51ed5b1e2f2382e38d88adc2cc2586e6
$ git show --pretty='' --name-only HEAD
.ufo/state/protocol.report-baseline
```

Pattern test:

```
.ufo/state                   state-guard=NOMATCH
.ufo/state/                  state-guard=MATCH
.ufo/state/protocol.round    state-guard=MATCH
./.ufo/state                 state-guard=NOMATCH
./.ufo/watchdog.log          state-guard=NOMATCH
```

The rule ".ufo/state/ is never committed" can therefore be broken by a lane that names the
directory (or the `./` form) instead of a file. `jj file track .ufo/state` also explicitly tracks
the otherwise-untracked `.report-baseline`.

### F8 — fleet-repo evidence commits are unserialized (Medium, pre-existing, worsened)

`commit_evidence` performs bare `git add`/`git commit` on the fleet repo with no flock. Fleet-repo
writers otherwise serialize on `scripts/hyaku/fleet-commit.sh`'s 1200 s lock. With the fleet root
colocated, a second writer (jj) resets the same index; with it git-only, the driver still races
lane report commits. The jj change adds a writer that mutates `.git/index` and `HEAD` on every
working-copy rewrite.

## L1 — live incident observed during this audit (Critical; reported, not caused here)

While inspecting the live root read-only, the fleet root itself was jj-colocated and rolled back:

```
$ ls -la .jj
drwxr-xr-x .jj   2026-10-20 11:19:37
$ git symbolic-ref -q --short HEAD || echo DETACHED
DETACHED
$ git rev-parse --short HEAD; git rev-parse --short master
4daa133
ca7f6e0
$ git reflog --date=iso
df54adf HEAD@{2026-10-20 11:20:46 -0300}: reset: moving to df54adf2c1f...
ca7f6e0 HEAD@{2026-10-20 11:20:46 -0300}:
4daa133 HEAD@{2026-10-20 11:19:38 -0300}: export from jj
ca7f6e0 HEAD@{2026-10-20 11:19:37 -0300}: commit: via git 2
```

- `4daa133` subject `via jj 2`, author `Joao Pedro Veiga <jpveigao10@gmail.com>`.
- `ca7f6e0` subject `via git 2`, author `t <t@x>`; its jj repo config
  (`~/.config/jj/repos/6b028a4ba80daddce168/config.toml`) reads
  `user.name="t"`, `user.email="t@x"`, `snapshot.auto-track="none()"`,
  `trunk()="master@origin"` — a probe identity, not a lane identity.
- While `.jj` existed, the index carried 28 intent-to-add entries (` A`): 9
  `.ufo/state/*.report-baseline` and 19 `.ufo/waves/hyaku/jj-w1/reports/*`; `.ufo/watchdog.log`
  showed ` M`.
- At 11:20:46 the branch was reset to `df54adf` and `.jj` removed. Final state:
  `symbolic-ref=master`, `HEAD=master=origin/master=df54adf`, `A entries: 0`, `ca7f6e0`/`4daa133`
  unreachable, `.jj` absent. `origin/master` never moved, so nothing was pushed.

I ran no jj command in the live root. [INFERENCE] The `via git 2` / `via jj 2` messages and the
probe identity indicate a deliberate A/B probe rather than a lane round; the practical damage
window (11:19:38–11:20:46) had no driver tick (`.ufo/watchdog.log` last entry 11:16:57), so
`commit_evidence` did not fire during it. Had it fired, F3/F4 are the exact result.

## What still holds (non-findings)

- No `@{u}`, `branch --show-current`, `rev-parse HEAD`-as-branch, or upstream reads anywhere in this
  script. Unlike `inline.sh verify`, the watchdog itself has no attached-HEAD assumption except the
  implicit one in `git commit` (F4).
- `sources_gate` runs `scripts/sources-census.sh`, which contains no `git` call
  (`grep -n 'git ' scripts/sources-census.sh` → empty), so the closure gate is jj-neutral.
- `report_of` is a byte/digest check (`sha256sum` + `wc -c` + `grep`); jj colocation does not change
  report acceptance.
- `record_report_baseline`'s file is untracked and atomically replaced; with `auto-track="none()"`
  it stays out of jj by default.
- For lanes with `LANE_REPO != "."`, the whole watchdog is jj-neutral: every call is fleet-root
  scoped, and `.gitignore:1` (`*-shokunin/`) keeps lane repos out of the fleet-root work tree.

## [INFERENCE]

1. `git commit` can also lose the race on `.git/index.lock` while jj holds the index during a
   working-copy update; not reproduced deterministically (F3 uses the deterministic post-add reset
   instead).
2. `render_prompt`'s truncate-then-write can be snapshotted mid-write by a lane jj command; the
   final content converges on the next snapshot, but a torn prompt could be committed if the driver
   crashes between. Timing not forced.
3. `.ufo/state/*.out` append-only growth will increase jj snapshot cost and op-log churn
   proportionally; not measured.
4. The live probe's author/config identity (`t <t@x>`) and commit names are a manual A/B test, not
   an inline.sh dispatch (inline.sh passes the lane id to `jj-lane.sh init`, which would have
   written `protocol-shokunin`).
5. `refs/jj/keep/*` keeps off-branch driver commits alive, but they are invisible to any tool that
   reads `refs/heads/master`/`origin/master` only.

## Cross-scope (other seats own these; recorded here because they meet the watchdog)

- `scripts/hyaku/inline.sh` is the live driver per `.ufo/watchdog.log` (`driver=hyaku-inline`).
  `inline.sh:38-40` colocated every lane at dispatch, including `.` lanes whose `LANE_CWD` is the
  fleet root (`lane_vcs_init "$lane" "${LANE_CWD[$lane]}"`); its dispatch commits the prompt via
  `fleet-commit.sh` (git, flock) rather than `commit_evidence`. See JjAuditInlineSh /
  JjAuditFleetCommit.
- `fleet-commit.sh` pushes `HEAD:$BRANCH`; with detached HEAD that pushes jj's `@-` chain and can
  move master independently of jj's bookmark. Sandbox-observed related fact: `jj git push` refuses
  a bookmark whose ancestry contains an undescribed commit ("Won't push commit ac7904524102 since
  it has no description"); the driver's evidence commits carry a description, so they do not
  themselves block a push.
- `jj-lane.sh:149-152` guard (F7) is the helper owner's file.

## Recommendations (proposal only; nothing edited)

1. **Keep the fleet root git and enforce it.** At startup, `die` (or log `fleet-jj-refused`) when
   `$SHOKUNIN_ROOT/.jj` exists and any `LANE_REPO` is `.`; add `[ ! -e "$SHOKUNIN_ROOT/.jj" ]` to
   `commit_evidence` with a `evidence-skip` log line so the failure is visible instead of silent.
2. **One writer per repo on the complete path.** For a `.` lane, replace `commit_evidence`'s bare
   `git add`/`commit` with a call to `fleet-commit.sh --as <lane> -m "round-N: <lane> dispatch
   evidence" -- .ufo/prompts/<lane>-round-N.md` (it holds the 1200 s flock), or with a jj writer if
   the fleet root is ever colocated. In both cases assert the path is in a commit on the branch:
   `git log -1 --format=%H refs/heads/master -- "$f"`, never via HEAD.
3. **Commit after the lane is dead.** Move `commit_evidence` below `kill_mission` in `advance`
   (L346 → after L349/L356/L371). It does not need the live process; this removes the concurrent
   jj/git window entirely.
4. **Stop swallowing the result.** Capture and log `commit_evidence`'s rc (`advance` currently
   ignores it) and log `evidence-commit-fail <lane> round=N` with git's stderr; treat a missing
   commit as `advance-blocked`, not `complete`.
5. **Make `render_prompt` atomic** (`$out.tmp.$$` + `mv -fT`), matching
   `record_report_baseline`, so a concurrent jj snapshot never sees a truncated prompt.
6. **Keep driver runtime out of jj** if the fleet root is ever colocated: stop tracking
   `.ufo/state/*.round|.mission|.out` (21 each today) or `jj file untrack` them, and keep
   `.ufo/state` out of any commit path.
7. **Harden the helper guard** (owner: helper): treat `.ufo/state` and `./.ufo/state` as
   `.ufo/state/*`, and `./.ufo/watchdog.log` as the log path, before any `jj file track`.
8. **Template/launch wording:** a `.` lane's "inside your lane repo" is the fleet root; until the
   driver is jj-aware, such lanes must not run jj at all. Route their commits through one writer.

## Sandbox

Preserved at `/fast/scratch/jj-wave/JjAuditWatchdog/` (`fleet` = git-only control, colocated
scenarios; `fleet2` = detached-HEAD, index-wipe, interleaving, helper guard; `fleet3` =
attached-HEAD then jj import). It contains the reproductions cited above.
