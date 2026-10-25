# JjAuditKama — lane `kama` git-invocation audit for jj colocation

- Lane: `/home/vgpnk/Projects/shokunin/kama-shokunin`, branch `master`, tip at audit start `726f737a942f1606d66e032f1efbcbb6f689ccf1` (attached, `master...origin/master` in sync, dirty only in `.ufo/waves/round-16/...`, concurrent rounds).
- Toolchain: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, git as backend.
- Method: read-only static census + isolated jj probes in `/fast/scratch/jj-wave/JjAuditKama-2` (removed after the audit; no citation depends on it surviving).
- No `jj` command was run with cwd or `-R` inside the live fleet root or any live lane. No live repo was written, staged, fetched or checked out.

## 0. Scope census (what exists, and what does not)

```
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name Makefile \) -print
[end]                       # no root-level executable tooling
scripts:   ABSENT
verifiers: ABSENT
tools:     yes              # kama-probe.sh, test-snapshot.sh, kama-llamacpp-live.py, kama-ollama-evidence.py
tests:     yes              # ollama-corpus-guard/check.py, probe-verdicts/check.py, llamacpp-live/check-receipt.py
```

`grep -cE '\bgit\b'` over every in-scope executable file:

```
tools/kama-probe.sh                      0
tools/test-snapshot.sh                   0
tools/kama-llamacpp-live.py              0
tools/kama-ollama-evidence.py            0
tests/llamacpp-live/check-receipt.py     0
tests/ollama-corpus-guard/check.py       0
tests/probe-verdicts/check.py            0
```

**The lane's own executable tooling contains zero git invocations** (no shell `git `, no `subprocess`/`execFile`/`spawn` argv containing `git`, no `GIT_*` env use). The only git calls reachable from this lane's SKILL.md-named gates live in the gate implementations under `.ufo/waves/`, which SKILL.md rows name as the gates themselves (rows 396, 430, 534) — treated in scope here, distinguished from `.ufo/waves` *outputs*.

## 1. Findings (observed, each with the command run and its output)

### F1 — No class A, no lane-mutating class B, no class C anywhere in the lane
Every git site found is a read against the object database (`cat-file`, `show`, `rev-parse`) plus two `git init` calls that target throwaway temp directories. There is no `symbolic-ref *` write, `@{u}`, `--abbrev-ref`, `--show-current`, `add`, `commit`, `stash`, `checkout`, `reset`, `rebase`, `push`, `pull`, `merge`, `clean`, `tag`, `diff --cached`, `ls-files -s`, or `update-index`.

### F2 — The detached-HEAD failure matrix, measured (jj 0.45.1, colocated repo)

Detached HEAD, after `jj commit`:

| command | exit | output |
|---|---|---|
| `git rev-parse HEAD` | 0 | commit id |
| `git cat-file blob HEAD:corpus/SOURCES.md` | 0 | committed bytes |
| `git show HEAD:tools/kama-probe.sh` | 0 | committed bytes |
| `git rev-parse master` | 0 | branch tip |
| `git rev-parse --show-toplevel` | 0 | path |
| `git rev-parse --abbrev-ref HEAD` | **0** | **`HEAD`** (silent literal — no error) |
| `git branch --show-current` | **0** | **(empty)** (silent empty string) |
| `git symbolic-ref -q --short HEAD` | 1 | — |
| `git rev-parse '@{u}'` | **128** | `fatal: ...` |

Unborn HEAD (fresh `jj git init --colocate`, no commits):

| command | exit |
|---|---|
| `git rev-parse HEAD` | **128** |
| `git rev-parse --verify HEAD` | **128** |
| `git rev-parse '@{u}'` | **128** |
| `git branch --show-current` | 0, prints `master` |
| `git rev-parse --show-toplevel` | 0 |

The lane uses only shapes from the safe rows. `--abbrev-ref`/`--show-current` are the dangerous ones (exit 0 with a junk/empty answer) and **are not used in kama**.

### F3 — `jj commit <paths>` silently commits nothing for untracked files when `snapshot.auto-track="none()"`

```
$ jj config set --repo snapshot.auto-track 'none()'
$ printf 'new\n' > tools/newfile.sh
$ jj commit -m try -- tools/newfile.sh
Warning: The given paths do not match any file: tools/newfile.sh
Working copy  (@) now at: vnrmwnqm a388213b (no description set)
Parent commit (@-)      : ylrupvoy cd195908 (empty) try
commit exit=0
tracked in @? 0
```

A no-op commit is created and **exit status is 0**. `jj file track` first, then the same command commits the file (`try2` → `8c82f4f`). The helper `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh` does run `jj file track` (lines 209-214), so this is a hazard only for hand-run `jj commit`, not for helper-routed commits.

### F4 — Index behaviour is command-dependent
```
index-before-commit: [corpus/SOURCES.md]      # after git add -A
index-after-jj-commit: []                     # jj commit cleared the index
```
`jj status` alone did **not** clear a `git add`-staged entry in this run; `jj commit` and `jj new` did. No kama gate reads the index (zero class C), so this is informational only.

### F5 — jj does not run git hooks
```
jj commit      -> hook marker exists? NO
git commit     -> hook marker exists? YES
```
(with an executable `.git/hooks/pre-commit` writing a marker)

### F6 — jj ignores `.gitattributes` text/eol normalization
Same CRLF worktree bytes, `.gitattributes` = `*.txt text eol=crlf`:
```
git index blob (normalized):  x \n y \n
jj-committed blob:           x \r \n y \r \n
eol attr now: a.txt: text: set / a.txt: eol: crlf
```
git normalizes to LF in the recorded blob; jj records the raw worktree bytes. The lane has no attributes today (see §4), so this is latent.

## 2. Classified call-site table

Class A = assumes attached HEAD/upstream; B = mutates history/index/worktree; C = reads index; D = read-only, rev-addressed. "Named gate" = implementation of a SKILL.md gate row.

### 2a. Named gates (in scope)

| file:line | exact command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `.ufo/waves/round-12/fidelity.py:115` | `git --no-pager --no-replace-objects -C <repo> rev-parse --show-toplevel` | D | none — topology only, identical in a colocated repo | keep |
| `.ufo/waves/round-12/fidelity.py:261` | `git --no-pager --no-replace-objects -C <repo> rev-parse --verify 2f7303c242319c1dc96c6bcf7702ac18b3ca1aad:corpus/SOURCES.md` | D | none — rev pinned by constant, HEAD not consulted | keep |
| `.ufo/waves/round-12/fidelity.py:271` | `git ... cat-file blob 2f7303c…:corpus/SOURCES.md` | D | none — object is immutable and reachable from `master` | keep |
| `.ufo/waves/round-12/fidelity.py:441` | `git --no-pager --no-replace-objects init --quiet <mkdtemp>/empty-repo` | B | none — temp dir only, never the lane | keep |
| `.ufo/waves/round-12/fidelity.py:442` | `git ... cat-file blob 2f7303c…:corpus/SOURCES.md` (selftest) | D | none | keep |
| `.ufo/waves/round-12/fidelity.py:449` | `git ... rev-parse HEAD` (selftest, result consumed at :539 as a fixture revision) | D, **HEAD-existence** | detached is fine (exit 0); **unborn HEAD → exit 128**, selftest aborts `cannot read repository HEAD` | `git rev-parse --verify -q HEAD` with a skip, or read `refs/heads/master` |
| `.ufo/waves/round-13/measure.py:295` | `git ... rev-parse HEAD` (live mode, required) | D, **HEAD-existence** | detached fine; unborn → `GateError` → exit 3 `probe_error` (honest, not clean) | keep HEAD, or `git rev-parse --verify refs/heads/master` for branch-tip semantics |
| `.ufo/waves/round-13/measure.py:309` | `git ... rev-parse --verify --end-of-options <rev>^{commit}` | D | none | keep |
| `.ufo/waves/round-13/measure.py:318` | `git ... cat-file blob <resolved-before-oid>:corpus/QUALITY.md` | D | none | keep |
| `.ufo/waves/round-13/measure.py:385` | `git ... cat-file blob <HEAD>:corpus/QUALITY.md` | D, **HEAD-relative semantics** | reads `@-`, not `@`. Combined with `worktree_matches_head = final == head_quality` (:397) and the `clean` conjunction (:443-451), any uncommitted QUALITY.md edit yields exit 1 `documentation_mismatch` — a *failed* gate, not could-not-evaluate | run the helper `commit` before the gate, or compare against the branch-tip ref once the bookmark has moved; gate the HEAD-vs-worktree divergence as its own finding |
| `.ufo/waves/round-16/measure.py:116` | `git -C <lane> cat-file blob 20e392ea683a36bc223eb7cb45897acfb45456a3:tools/kama-probe.sh` | D | none — pinned commit. Separate latent defect: no `--no-replace-objects` and no GIT_* scrub, unlike the other two gates | keep, add the two guards for parity |

Named-gate count: **A 0 · B 1 · C 0 · D 9** (the one B is the temp-dir `init`).

### 2b. Adjacent code under `.ufo/waves` (not named by SKILL.md — listed for completeness)

| file:line | exact command | class | risk |
|---|---|---|---|
| `.ufo/waves/round-11/reproduce.py:89` | `git -C <root> rev-parse HEAD` | D, HEAD-existence | same unborn-HEAD hazard; `check=True` → traceback |
| `.ufo/waves/round-12/reproduce.py:55` | `git("rev-parse","HEAD")` via `git()` at :50 | D, HEAD-existence | same |
| `.ufo/waves/round-12/reproduce.py:79` | `git("rev-parse","--verify",SPEC)` | D | none |
| `.ufo/waves/round-12/reproduce.py:80` | `git("cat-file","blob",SPEC)` | D | none |
| `.ufo/waves/round-12/reproduce.py:184` | `git("rev-parse","HEAD")` | D, HEAD-existence | same |
| `.ufo/waves/round-12/reproduce.py:177` | `git --no-replace-objects -C <tmp>/empty init -q` | B | temp dir only |
| `.ufo/waves/round-16/stale-statements.py:58` | `git -C <lane> show <rev>:<path>` | D | none — pinned rev + immutable objects |

Adjacent count: **A 0 · B 1 · C 0 · D 6**.

### 2c. Argv constructors (not commands, counted separately)
`.ufo/waves/round-12/fidelity.py:95` and `:387` (`['git','--no-pager','--no-replace-objects']`), `.ufo/waves/round-13/measure.py:278` (adds `-C LANE`), `.ufo/waves/round-12/reproduce.py:50` (adds `-C ROOT`). All additive prefixes; no command semantics.

### 2d. Counts per class

| class | lane in-scope (tools/, tests/, root) | named gates | adjacent | **total** |
|---|---|---|---|---|
| A (attached HEAD / upstream assumed) | 0 | 0 | 0 | **0** |
| B (history/index/worktree mutation) | 0 | 1 | 1 | **2** (both temp-dir `git init`) |
| C (index/staging read) | 0 | 0 | 0 | **0** |
| D (read-only, rev-addressed) | 0 | 9 | 6 | **15** |

## 3. Top three risks for this lane

**R1 — `round-13` live gate conflates "working copy ahead of HEAD" with a documentation failure.** `clean` requires `worktree_matches_head` (`measure.py:397,443-451`). Under jj, `@` is perpetually ahead of `HEAD` until the helper commits and moves the bookmark, so a gate run between "edit QUALITY.md" and "helper commit" returns **exit 1 `documentation_mismatch`** with observation `worktree_not_at_measured_revision`. SKILL.md reads exit 1 as a failed gate, so the lane would publish a false failure. Mitigation is ordering: helper `commit` before the gate. A stricter fix would separate the divergence into its own finding (code change, out of this audit's write scope).

**R2 — Unborn HEAD on a freshly colocated lane.** `git rev-parse HEAD` exits 128 in a colocated repo with no commits. That aborts the round-12 selftest (`fidelity.py:449`) and returns exit 3 `probe_error` in round-13 live (`:295`). Detached HEAD is *not* the hazard — every argv shape the nine named-gate read sites use was replayed against a detached HEAD and exited 0 (`rev-parse --show-toplevel`, `rev-parse --verify <rev>:path`, `rev-parse --verify --end-of-options <rev>^{commit}`, `cat-file blob <rev>:path`, `show <rev>:path`, `rev-parse HEAD`). Only the pre-first-commit window matters; it disappears once the helper has pushed any commit.

**R3 — Silent empty commits when a path is untracked and `snapshot.auto-track="none()"` is set.** `jj commit -m … -- <untracked>` prints a warning, creates an empty commit, and **exits 0** (F3). If an L1 or critic runs `jj commit` by hand instead of through `jj-lane.sh`, it can cite a hash that contains none of its work while every exit-status check passes. This is the lane's largest "landed" integrity hazard in the jj model, and it is invisible to git-based verification because the hash exists and is pushed. The helper is defensively written against both halves of it: it `jj file track`s each existing path (lines 209-214), exits 0 with `nothing to commit (no such paths)` when the pathspec matches nothing (line 199), short-circuits on an empty `jj diff --summary` with `nothing to commit` (line 218), and prints a hash only on a real commit (line 235). The hazard is therefore confined to hand-run `jj commit`.

## 4. Hooks, attributes, filters and eol rules

- **Hooks:** `.git/hooks` contains only `*.sample` files; `git config --get core.hooksPath` exits 1 at every scope. **No active hooks.** (jj also does not execute git hooks — F5.)
- **Attributes:** no `.gitattributes` is tracked or present anywhere (`find . -name .gitattributes -not -path './.git/*'` → empty); `core.attributesfile` unset; `.git/info/attributes` absent; `git check-attr -a` over `corpus/SOURCES.md`, `tools/kama-probe.sh`, `SKILL.md`, `LOG.md`, `registry/history/latest.tsv` → empty.
- **Filters:** global config defines `filter.lfs.{clean,smudge,process,required}`, but no attribute binds `filter=lfs`, so LFS is **inert**. jj would bypass it anyway (F6).
- **EOL:** `git ls-files --eol` → `635  i/lf w/lf`, `1  i/none w/none` (`.ufo/waves/round-16/build/dispatch.stderr`, binary). No `core.autocrlf` and no `core.eol` at any scope. Nothing to bypass today.
- Incidental: `.git/info/refs` exists (193 bytes, branch + `origin/*` lines) — a `git update-server-info` leftover; inert.
- `.gitignore` contains only `.ufo/interactive-sessions/`. No tracked path under `.ufo/state` (`git ls-files .ufo/state` → empty), so the never-commit-state invariant holds now.

## 5. [INFERENCE]

- Because `tools/` and `tests/` contain zero git calls, colocating `kama` changes **no executable gate behaviour**; the residual risk is procedural (R1, R3) and bootstrap-only (R2).
- All 15 class-D reads stay correct indefinitely: jj never rewrites existing git objects, and every pin (`2f7303c…`, `20e392e…`, `SOURCE_BLOB_OID`) is reachable from `master`, so a `jj git gc` that prunes only unreachable objects cannot remove them. Not tested against an actual `jj git gc`.
- `jj commit <paths>` splitting `@` means HEAD at any instant is the last *helper-committed* tree, which is exactly what round-13's `worktree_matches_head` assumes only when the gate runs after a helper commit.
- If the helper's bookmark move fails after `jj commit`, HEAD still advances (detached commit existed before the bookmark move), so a gate could read a commit that is not yet pushed. That would violate the "landed = committed and pushed" invariant while exit codes stay clean; SKILL.md's citation rule, not any gate here, is the only guard. [INFERENCE from the helper's ordering at lines 229-239 (`commit` → `hash=@-` → `bookmark set` → push); not exercised.]

## 6. Recommendations

1. **Leave the nine named-gate git reads as they are.** They are jj-safe; changing them adds risk without reducing any.
2. **Enforce gate ordering in the lane's round procedure:** helper `commit` → then round-13 live. Do not run round-13 live against an uncommitted QUALITY.md and call exit 1 a documentation failure.
3. **Treat detaching as expected:** anything new that needs a branch name must use `refs/heads/master` (as `jj-lane.sh:59,71` already does), never `HEAD`, `@{u}`, `--abbrev-ref` or `--show-current` — the latter two fail *silently* (exit 0) under detachment.
4. **Never add `.gitattributes` filters or eol rules to this lane**, and never add git hooks expecting them to fire. jj ignores both (F5, F6).
5. **Require `jj file track` for every new path** before `jj commit`, and prefer the helper so R3 cannot fire; a post-commit check that the new commit is non-empty (`jj diff --summary -r <hash>` non-empty) would close R3 at the source.
6. **Parity fix in `round-16/measure.py:116`:** add `--no-replace-objects` and the GIT_* environment scrub the other gates use. This is a robustness fix, not a jj-compatibility fix.

## 7. Verification gaps (honest)

- The live gates were **not executed** against the live lane (read-only mandate); their jj behaviour is established by isolating the exact argv shapes and reproducing each under a colocated repo in the sandbox.
- HEAD/branch values drift while sibling rounds run; `726f737` is a timestamped snapshot, not a pin.
- `jj git gc` object retention, and `jj git fetch`'s treatment of the pinned commits, were not exercised.
- The helper was grepped in full (268 lines) and read in detail for `cmd_commit` (lines 199-246), `cmd_init` (134-165) and the branch resolver (50-78); it was never executed, so R3's consequence for the helper is derived from its ordering, not from a run.

## 8. Tool installs

None. No package, binary or config was installed or modified for this audit. The sandbox `/fast/scratch/jj-wave/JjAuditKama-2` was removed; no cited failure depends on its preservation.
