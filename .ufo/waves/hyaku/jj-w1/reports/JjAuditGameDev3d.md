# JjAuditGameDev3d — static git audit of `game-dev-3d-shokunin`

- Lane: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`
- Branch: `main`, HEAD `3118be0b18dd7351b1faf6ce99d26a34370793ec`, upstream `origin/main`
- Lane VCS today: plain git, **no `.jj`** (`ls .jj` → `No such file or directory`); 23,484 tracked files
- jj under test: `jj 0.45.1-7c41cdeb16b6c` (behaviour measured in sandbox `/fast/scratch/jj-wave/JjAuditGameDev3d-2/`, removed after the run; reproduction commands in §5)
- Mode: static read-only on the lane. Every git command run against the lane was read-only plumbing (`rev-parse`, `log`, `ls-files`, `status`, `config` queries, `submodule status`); no `add`, `commit`, `stash`, `checkout`, `reset`, `fetch`, `pull`, `push`, `merge`, `clean` or `tag`. No jj command ever ran with a working directory or `-R` under `/home/vgpnk/Projects/shokunin`. No live repo was written, staged, checked out or fetched.
- Tool installs: **none**.

## 1. Scope and enumeration

The assignment's named set does not exist at the lane root; the executable tooling lives under `corpus/`.

```
$ find . -path ./.git -prune -o -type d \( -name tools -o -name scripts -o -name verifiers -o -name tests \) -print
(no output)
$ git ls-files | awk -F/ 'NF==1' | grep -E '\.(sh|py|mjs|js)$|Makefile'
(none)
$ find . -path ./.git -prune -o -name Makefile -print
(no output)
```

In-scope files actually audited (all of them, for git tokens):

| file | git hits |
|---|---|
| `corpus/knowledge/unreal-mcp/gate/run_gate.sh` | 15 lines match `git ` |
| `corpus/artifacts/glb-r12/run_import.py` | 0 |
| `corpus/artifacts/glb-r9/validate_glb.py` | 0 |
| `corpus/artifacts/unity-r19/verify_scene.py` | 0 |
| `corpus/artifacts/unreal-r22/verify_descriptor.py` | 0 |
| `corpus/artifacts/zip-r10/verify_carrier.py` | 0 |
| `corpus/fixtures/run_battery.py` | 0 |
| `corpus/fixtures/timeout_descendant.py` | 0 |
| `corpus/live/r101-sentinel/mcp2/srv.py` | 0 |
| `corpus/knowledge/unreal-mcp/upstream/hooks/unreal-context.sh` | 0 |
| `corpus/fixtures/three/*.mjs` (9 runners) | 0 |
| all `*.gd` fixtures (`OS.execute` exists, no git token) | 0 |

`SKILL.md` names only one executable gate, `corpus/knowledge/unreal-mcp/gate/run_gate.sh` (lines 91, 114, 181), and one runner, `corpus/fixtures/run_battery.py` (line 193). No file named `*selftest*` exists anywhere in the lane (`find … -iname '*selftest*'` → empty). The gate's calibration controls are prose in `gate/README.md` plus historical scripts under `reports/round-107/mutations/` — out of the assigned scope, see §8.

Excluded per assignment and by kind: `.git`, corpus prose (`corpus/knowledge/**/*.md`), `reports/`, `corpus/live/runs/*/scratch/` (byte-copies of fixtures), vendored JS (`corpus/fixtures/r94vendor/`, `corpus/fixtures/three/node_modules/` — only GitHub URLs in comments).

## 2. Classified call-site table

All sites are in `corpus/knowledge/unreal-mcp/gate/run_gate.sh`. `SUB` = the lane subtree `corpus/knowledge/unreal-mcp`; `CLONE` = `$WORK/clone` (scratch) or `$GATE_REF`.

| file:line | exact command | class | risk under jj colocation (HEAD may be detached, jj owns the index) | jj-safe replacement |
|---|---|---|---|---|
| `run_gate.sh:32` | `for _t in git sha256sum grep find sort comm; do` | preflight, executes nothing | none | keep |
| `run_gate.sh:97` | `git -C "$SUB" rev-parse --show-toplevel` | **D** | none: read-only, no snapshot; `.git` survives colocation. If a lane were ever jj-native-only this guard goes false and `LANE_HEAD` is silently omitted | keep (optionally accept `.jj`) |
| `run_gate.sh:98` | `git -C "$SUB" rev-parse HEAD` | **D** | **git HEAD is a jj-managed pointer, not the branch.** After `jj new` it is an empty working-copy commit with no subject; after `jj commit` it is the new commit; neither is on `main` until the bookmark moves (§5, E2). Printed unqualified as `LANE_HEAD` | `git -C "$SUB" rev-parse refs/heads/main`, printed as `LANE_BRANCH=`; keep HEAD separately as `GIT_HEAD=` if wanted |
| `run_gate.sh:204` | `command -v git` | preflight | none | keep |
| `run_gate.sh:210` | `git -C "$C2_REF" rev-parse HEAD` | **D** | only proves `GATE_REF` is a git repo; passes even when HEAD is detached at `@`. The pin test is at :229, so a colocated reference survives this gate and fails later | `git -C "$C2_REF" rev-parse refs/heads/main` and/or `git -C "$C2_REF" cat-file -e "$PIN^{commit}"` |
| `run_gate.sh:224` | `timeout 180 git clone --quiet "$REPO" "$CLONE"` | **D\*** | if `REPO` is a local colocated path, the clone checks out the source's git HEAD, not the branch: observed detached at the source HEAD with `Note: switching to '<sha>'` (§5, E5). Checks 2c/2d then measure that tree while the report names `CLONE_HEAD`; a failure is attributed to the pin, not to the source HEAD | `git clone --branch main --single-branch`, or `git init` + `git fetch "$REPO" "$PIN"` + `git ls-tree -r --name-only "$PIN"` |
| `run_gate.sh:229` | `git -C "$CLONE" rev-parse HEAD` | **D** | **false FAIL 2a** for a colocated `GATE_REF`: a fresh colocated reference passes, then `jj new` alone moves HEAD to an empty commit ≠ pin while the tree is clean (§5, E7) | compare `refs/heads/<branch>`, not HEAD (same fix as :210) |
| `run_gate.sh:230` | `git -C "$CLONE" status --porcelain` | **C** | reads index + worktree. (a) A jj snapshot in `@` shows ` M a.txt` → **false FAIL 2b** on a colocated reference (E3/E7). (b) The first `git status` after a jj mutation **rewrites `.git/index`** (bytes changed; suppressed by `--no-optional-locks`, E4) — the gate mutates the "read-only" reference and races jj's index management | drop 2b for `GATE_REF`, or clone a throwaway copy; at minimum `git --no-optional-locks status --porcelain` and refuse a reference containing `.jj/` |
| `run_gate.sh:231` | `git -C "$CLONE" ls-files \| sort > "$WORK/clone-files.txt"` | **D** | index-driven; on a colocated reference the index is jj-reset/refreshed, so the path set follows index state rather than the pin tree (observed correct at `ls_files=2`, but it is not object-addressed) | `git -C "$CLONE" ls-tree -r --name-only "$PIN"` |
| `run_gate.sh:248` | `git -C "$CLONE" show "$PIN:$f" \| sha256sum` | **D** | none: object-addressed at `PIN`, independent of HEAD and index | keep (or `git cat-file blob "$PIN:$f"`) |

`D*` at :224 is read-only with respect to the audited repo; its only writes are the fresh clone under `$WORK_ROOT`.

### Counts per class

| class | count | sites |
|---|---|---|
| **A** (assumes attached HEAD / upstream) | **0** | — |
| **B** (mutates history, index or worktree) | **0** | — |
| **C** (reads index / staging state) | **1** | :230 |
| **D** (read-only) | **7** | :97, :98, :210, :224 (D\*), :229, :231, :248 |
| non-executing git references | 4 | :32, :204, :205 message, :214 message |
| prose comments containing `git ` | 3 | :43, :143, :185 |

Executed git commands: **8** (1 C + 7 D). `grep -nE 'git '` returns 15 lines in total, accounted for exactly as 8 + 4 + 3.

## 3. Hooks and attributes

```
$ find .git/hooks -type f ! -name '*.sample' -printf '%p %m\n'
(no output)                      # 14 files, every one a *.sample
$ git config --show-origin --get-all core.hooksPath ; echo rc=$?
rc=1                             # unset at system, global and local scope
$ git config --show-origin --get-regexp 'init\.templatedir'
(no output)
$ find . -path ./.git -prune -o -name '.gitattributes' -print ; git ls-files | grep -c gitattributes
(no output) / 0
$ ls .git/info/attributes
No such file or directory
$ git config --show-origin --get-regexp 'core\.(autocrlf|eol|safecrlf)$|^filter\.'
file:/home/vgpnk/.config/git/config  filter.lfs.clean    git-lfs clean -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.smudge   git-lfs smudge -- %f
file:/home/vgpnk/.config/git/config  filter.lfs.process  git-lfs filter-process
file:/home/vgpnk/.config/git/config  filter.lfs.required true
```

- **Git hooks in use: none.** No non-sample hook, no `core.hooksPath`, no init template dir.
- **Attributes / eol rules: none.** No `.gitattributes` tracked or on disk, no `info/attributes`, `core.autocrlf` and `core.eol` unset. The global git-lfs filter definitions are inert because no attribute selects `filter=lfs`.
- jj bypasses both anyway; the gate's byte check is filter-immune in the right direction (`sha256sum` of the worktree file vs `sha256sum` of `git show "$PIN:$f"`, which emits the raw blob). With no attributes today, colocation costs nothing here.
- `corpus/knowledge/unreal-mcp/upstream/hooks/unreal-context.sh` is a Claude Code `SessionStart` hook shipped inside the vendored subtree — not a git hook and not installed by git. It contains no git calls.

## 4. Top three risks

1. **`LANE_HEAD` can name a commit that is not on `main` (`run_gate.sh:98`).** Under colocation git HEAD tracks jj's working-copy pointer: `jj new` makes it an empty, subject-less commit; `jj commit` makes it the new commit; both were non-ancestors of `main` until a bookmark move (`git merge-base --is-ancestor` → false, §5 E2). The gate only prints it (`grep LANE_HEAD` → line 98 only), so the risk materialises when a report cites `LANE_HEAD` as the landed hash, violating "a cited hash stays an ancestor of the branch". Replace with `refs/heads/main`.
2. **A jj-colocated `GATE_REF` turns the standing close-out gate falsely red and mutates its own reference (`run_gate.sh:229`, `:230`).** Modelled on a fresh colocated reference at the pin: it passes; after `jj new`, HEAD ≠ pin with a clean tree → 2a fails; after snapshotting one edit, `git status` reports ` M a.txt` → 2b fails; and the first status after a jj mutation rewrites `.git/index` (bytes changed; unchanged with `--no-optional-locks`). A blocked/failed close-out is misattributed to the vendored bytes, and the "read-only" reference has been written.
3. **`git clone` of a local colocated repo compares the wrong commit (`run_gate.sh:224`).** Cloning the colocated worktree produced a detached checkout at the source git HEAD (`Note: switching to '14d6074…'`), not `main`; checks 2c/2d then describe `@`/`@-` rather than the branch tip, and 2a reports a pin mismatch whose cause is the source HEAD. Cloning the bare remote with `--branch main` produced an attached, clean `refs/heads/main` (E6), which is the safe form.

## 5. Observed evidence (sandbox, jj 0.45.1)

All commands ran under `/fast/scratch/jj-wave/JjAuditGameDev3d-2/lab/` against a sandbox bare repo; nothing touched a live path.

**E1 — live lane state (read-only).**
```
$ git rev-parse --abbrev-ref HEAD              → main
$ git symbolic-ref -q HEAD                     → refs/heads/main
$ git rev-parse HEAD                           → 3118be0b18dd7351b1faf6ce99d26a34370793ec
$ git rev-parse --abbrev-ref main@{u}          → origin/main
$ ls .jj                                       → No such file or directory
$ git ls-files | wc -l                         → 23484
```

**E2 — HEAD after jj operations, and ancestry vs `main`.**
```
$ jj new
HEAD=5765895db8ea8271ab39fd835728d9f39626ce5e  main=a5626ba728d47878c4d8956e2051396cda6cf3ee
HEAD NOT ancestor of main
$ git show -s --format=%s HEAD                 → (empty subject)
$ jj commit -m probe-empty
HEAD=24a4fbd3760dcc995ada5194d4b7fa9ee655ed61  main=a5626ba…
HEAD NOT ancestor of main                      dirty=0
```
(`git symbolic-ref -q HEAD` is `DETACHED` in these states; the same was observed after a path-limited `jj commit`: `rev-parse HEAD=14d60748`, `rev-parse main=35919d14`, `symbolic-ref` → `DETACHED`, `status=[]`.)

**E3 — a jj snapshot in `@` is visible to `git status`.**
```
$ printf 'jj-snapshot-change\n' >> a.txt ; jj status
$ git status --porcelain                       →  M a.txt
```

**E4 — `git status` rewrites the jj-managed index.**
```
after jj new:  idx 248 11:14:02.848490671   sha I1
git status:    idx 248 11:14:03.853730806   sha I2   → index bytes CHANGED by status
after jj new:  idx 248 11:14:03.860730737   sha J1
git --no-optional-locks status:  same mtime, same sha J2
                                                       → index bytes unchanged
```

**E5 — cloning a colocated worktree.**
```
$ git clone work clone-from-coloc
Note: switching to '14d6074856783931f09988804284749332065b7b'.
You are in 'detached HEAD' state.
$ git -C clone-from-coloc symbolic-ref -q HEAD   → rc 1 (detached)
```
The source's branch was `main=35919d1`; the clone landed on `@-`.

**E6 — control: plain clone of the bare remote.**
```
$ git clone -q --branch main origin.git refpin
$ git -C refpin rev-parse HEAD                   → 35919d14ce2f1d3509bcbfe8ea50c7eebd600814
$ git -C refpin symbolic-ref -q HEAD             → refs/heads/main
$ git -C refpin status --porcelain               → (empty), tracked=2
```

**E7 — gate check 2 modelled on a colocated `GATE_REF`** (`HEAD`, `rev-parse HEAD == PIN`, `status --porcelain | wc -l`):

| state of the colocated reference | HEAD == pin | dirty |
|---|---|---|
| fresh clone at pin + `jj git init --colocate` | yes | 0 |
| after `jj new` (no content change) | **no** (empty commit) | 0 |
| after snapshotting one edit (`jj status`) | no | **1** (` M a.txt`) |
| after `jj commit` of that edit | no | 0 |
| after `jj bookmark set main -r @-` | no vs original pin; HEAD == the moved `main` | 0 |

The last row is expected (the pin variable was captured before the bookmark move); it shows the only state in which HEAD tracks the branch is after an explicit bookmark move.

## 6. [INFERENCE]

- `LANE_HEAD` is consumed only by readers, not by the gate logic (`grep -n LANE_HEAD` returns line 98 alone). Risk 1 is latent until a report cites it.
- The index write in E4 could collide with a concurrent jj mutation and surface as an index-lock error. Not reproduced: no concurrency test was run.
- In the planned helper flow (`jj commit <paths>` → bookmark move → push), `@-` and the branch tip coincide, so the non-ancestor window is between a jj mutation and the bookmark move. The audit does not assume the helper always completes.
- The mado round-14 incident (a jj command in a live repo snapshotting state) is operator-reported; it was not re-verified here.

## 7. Recommendations

1. Pin the gate to the branch, not to HEAD: `git -C "$SUB" rev-parse refs/heads/main`, printed as `LANE_BRANCH=`; keep/rename the HEAD value if the diagnostic is still wanted. Editing the gate moves its sha, so update the `SKILL.md` stamp (`390a25ae…`, line 181) with the same change.
2. Make CHECK 2 HEAD- and index-free: `git cat-file -e "$PIN^{commit}"`, `git ls-tree -r --name-only "$PIN"`, `git cat-file blob "$PIN:$f"`. This removes :229, :230 and :231 from the jj surface in one cut.
3. If `GATE_REF` stays: reject a reference containing `.jj/` with a named message; otherwise require `refs/heads/<branch>` and use `git --no-optional-locks status --porcelain`. Treat `GATE_REF` as read-only in fact, not just by convention.
4. Never point `REPO` or `GATE_REF` at a colocated worktree; use the bare mirror or a plain `git clone --branch`.
5. Keep the gate's remaining git reads as they are: `rev-parse`, `show`, `ls-files` do not snapshot, so running them inside a colocated lane is safe. The hazard is **trusting HEAD**, not executing git.

## 8. Residual risk and verification gaps

- **No `tools/`, `scripts/`, `verifiers/` directory and no root-level code file exists**, so the assignment's first, third and fourth bullets are empty by enumeration, not by omission.
- **No selftest file is named in `SKILL.md`.** The gate's calibration controls (`gate/README.md` §Calibrating the gate, C1–C7/A1–A4/W0–W6) are prose plus scripts under `reports/round-107/mutations/`. Those scripts do run git (`mut-gate.sh:175` `git -C "$REF_NEW" rev-parse HEAD`, `:183` `git ls-files -z`, `:205` `git clone --quiet --bare`) and are **not audited here** because `reports/` is outside the assigned scope; if they are ever re-run as standing tooling they need the same review.
- The gate itself was not executed: it performs a network clone and the live-tree rule forbids running fleet scripts. Every finding is static reading plus isolated sandbox experiments.
- `corpus/live/runs/*/scratch/` and `reports/` were excluded as run artifacts; `r94vendor/` and `three/node_modules/` as vendored dependencies.
- jj behaviour is version-specific; measured on `0.45.1-7c41cdeb16b6c` only.
