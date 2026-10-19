# kaika W2j — jj colocate probe: kumitate-shokunin

Repo: `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (live branch `master`, HEAD `16a5441a3347a10ac5ed169abcd5a17ba6f3f185`).
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kumitate-shokunin` (deleted after probe; 5.4 MiB total, `.jj/` 228 KiB, `.git` 3.0 MiB).
jj: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`jj --version`). Node `v24.21.0`.
Live repo untouched: post-probe `git -C <live> status --porcelain | wc -l` → `0`, `rev-parse --abbrev-ref HEAD` → `master`.

## 1. Pristine baseline (in scratch clone)

`git clone --local --no-checkout <live> <scratch>` + `git checkout master` → clean worktree, `git status --porcelain | wc -l` = 0.

Live-repo facts (read-only): `status --porcelain` empty (clean); `git ls-files | wc -l` = 110; checkout 7.7 MiB, `.git` 3.0 MiB. No `tools/`/`verifiers/` dirs; gates live in `scripts/` (`cite-check`, `claims-check`, `kimi-census`, `proxy-check`, `round-gate`, `surface-probe` .mjs). The SKILL.md "Verifiable checklist" (SKILL.md:587–602) is the gate registry; `node scripts/surface-probe.mjs --checklists` executes all 11 items with exit codes (surface-probe.mjs:797–881 runs each item via `bash -c` in the repo).

Baseline detector — `node scripts/surface-probe.mjs --checklists`, wall 10.08 s, `CHECKLIST_EXIT=1`, 6/11 pass:

| SKILL.md | item | baseline |
|---|---|---|
| 592 | cite-check | PASS (exit 1 = allowed DRIFT) |
| 593 | cite-check --selftest | PASS exit 0 |
| 594 | surface-probe (live conformance) | FAIL exit 1 — `SURFACE_PROBE: DRIFT`: DIGEST_CONCAT/PIN_DIGEST digest drift vs origin manifest + dispatcher `STATUS_REACH` (surface unreachable; the live dispatcher isn't running) |
| 595 | surface-probe --selftest | PASS exit 0 |
| 596 | round-gate --selftest | PASS exit 0 |
| 597 | round-gate (audit) | FAIL exit 2 — `REPORTS_DIR_MISSING: --reports-dir /home/vgpnk/Projects/shokunin/.tower/jj-probe/.ufo/reports is absent`. Location-dependent: `--reports-dir` defaults to `<fleet-parent>/.ufo/reports`; exists at live fleet root, absent beside scratch clones. Path-derived, not git-derived — identical under jj. |
| 598 | round-gate --tracked | FAIL exit 2 — same `REPORTS_DIR_MISSING` |
| 599 | proxy-check | FAIL exit 1 — `PROXY: DRIFT` (K_MEMBERS_DRIFT 49→50, coverage_kimi 10→9) — live `~/.kimi-code` drift, unrelated to the repo |
| 600 | proxy-check --selftest | PASS exit 0 |
| 601 | claims-check | PASS exit 0 `CLAIMS: MATCH` |
| 602 | kimi-census | FAIL exit 1 — `KIMI_CENSUS: DRIFT (UNLISTED skills/; UNLISTED mcp.json)` — live root drift, unrelated to the repo |

Baseline FAILs are **environment drift, not git dependence**: 597/598 are path-derived, 599/602 are the live `~/.kimi-code` tree, 594 is origin-tree digest drift + a stopped live service. Mutation-tester verdict: the baseline is a mixed detector — 6 items are valid detectors, 5 are inconclusive-by-environment.

## 2. `jj git init --colocate`

- `jj git init --colocate` → `INIT_EXIT=0`, "Done importing changes from the underlying Git repo. Setting the revset alias `trunk()` to `master@origin`. … Initialized repo in `.`". Hint printed: untracked remote bookmark `master@origin`.
- First `jj st`: **6 ms** (real 0m0.006s). "The working copy has no changes." `@` = `oowwskst b29caa0e (empty)`, parent `pyrknktu 16a5441a` with bookmarks `kaika/round@origin master master@origin`.
- `jj diff --stat -r @` → `0 files changed, 0 insertions, 0 deletions` — nothing snapshotted beyond HEAD (the `.gitignore` already covers `.ufo/interactive-sessions/`; jj honors it).
- `git status --porcelain` after init → empty; `git status --ignored --porcelain` → `!! .jj/` only. `git rev-parse --abbrev-ref HEAD` → `master` (still attached).
- **`.gitignore` coverage for `.jj/`**: needed = none. `jj git init` writes `.jj/.gitignore` containing `/*` — `git check-ignore -v .jj/repo/store/git` → `.jj/.gitignore:1:/*`. `.git/info/exclude` untouched (default template). `.jj` is self-ignoring; no repo `.gitignore` edit required.
- jj store: `.jj/repo/store/git_target` → pointer to the real `.git` (13-byte file); `.jj` holds ops/index only (228 KiB on a 110-file repo).

## 3. Re-run gates under jj

`node scripts/surface-probe.mjs --checklists` (wall 10.82 s): **byte-identical verdict table** — same 6 PASS / 5 FAIL, same exit codes, `VERDICT: FAIL`, `CHECKLIST: 6/11 pass`. Zero exit-code changes attributable to jj. Grep of tools for git calls (`grep -nE "rev-parse|symbolic-ref|git status|git diff|git add|git stash"` over `scripts/*.mjs`): only `rev-parse --is-inside-work-tree`, `rev-parse HEAD`, `rev-parse --verify`, `git status --porcelain`, `git ls-files` — **none call `rev-parse --abbrev-ref HEAD`, `symbolic-ref`, `git diff --cached`, `git add`, or `git stash`**; all work under detached HEAD. No git hooks in the repo.

## 4. Lane-identity commit flow

- `echo "probe change" > SCRATCH-PROBE.md; jj st` → `A SCRATCH-PROBE.md` (working-copy-as-commit; `git status` showed the same file untracked). `git rev-parse --abbrev-ref HEAD` still `master` at this point.
- `jj --config user.name=kumitate-shokunin --config user.email=kumitate@shokunin.local commit -m test SCRATCH-PROBE.md` → committed `9421b1f4d1013e70b0f6c206d217a9f851688d8b`.
- `git log -1 --format='%an <%ae> | %cn <%ce>'` → **`Joao Pedro Veiga <jpveigao10@gmail.com> | kumitate-shokunin <kumitate@shokunin.local`** — **FINDING: `--config user.name/user.email` set the committer but NOT the author; the author came from `~/.config/jj/config.toml` (`jj config list` → `user.name = "Joao Pedro Veiga"`, `user.email = "jpveigao10@gmail.com"` — a persistent per-user jj config distinct from git's `ci <ci@local>`).** Command-line `--config` did not override it for the author slot; a persisted config at higher precedence (or env `JJ_USER`/`JJ_EMAIL`) is required. Second commit `c2692d00` (`--config` again) → `kumitate-shokunin <kumitate@shokunin.local> | kumitate-shokunin <kumitate@shokunin.local>` — author DID apply on the second run; the first commit's stale author is explained by jj resolving author identity at repo-init/snapshot time (`user.name` read when `@`'s parent op ran). Reproduced once; treat `--config user.name` as unreliable for author on the first post-init commit and verify `git log` author after adopting.
- **Branch/HEAD behavior**: after `jj commit`, `git rev-parse --abbrev-ref HEAD` → `HEAD` (detached); `git symbolic-ref HEAD` → `fatal: ref HEAD is not a symbolic ref` (exit 128); `master` stayed at the old commit (`git branch -v` → `master 16a5441a`, detached HEAD `9421b1f`). Colocated jj creates the commit but does NOT advance the checked-out branch — expected per jj's working-copy model (docs: https://jj-vcs.github.io/jj/latest/git-compatibility/ — "the Git HEAD is detached when the working-copy commit isn't on a branch"). `jj bookmark set master -r 'parents(@)'` → "Moved 1 bookmarks to oowwskst 9421b1f4 master" and `git branch -v` showed `master 9421b1f [ahead 1]` while HEAD stayed detached; `git checkout master` reattached (`Switched to branch 'master'`). A subsequent `jj st` re-snapshotted and detached HEAD again.
- `jj op log --limit 5` shows full op history (snapshot/commit/bookmark ops, 1–3 ms each) — `jj undo`/`jj op restore` work over these ops.

## 5. Hazards

- Special files in live checkout: `find <live> -path '*/.git' -prune -o \( -type p -o -type s \) -print` → **none**; `-type l` → **none** (no FIFOs, sockets, symlinks).
- Untracked files: `git -C <live> status --porcelain` clean; `ls-files --others --exclude-standard` → **zero untracked-not-ignored files** → first jj command snapshots nothing unexpected.
- Files > 1 MiB: only ignored `.ufo/interactive-sessions/20261015T050057Z/…jsonl` (1.8 MiB) — ignored by `.gitignore`, so `snapshot.max-new-file-size` never sees it. No untracked >1 MiB.
- Credential-looking names: only `corpus/knowledge/kimi-binary-secrets.md` (a tracked doc about secrets policy, not a secret). Live `.ufo/` content is a session transcript, ignored.
- Git-side config untouched by init: `git config --local --list` after init showed only clone defaults (no `core.excludesfile`, no jj keys injected).

## Verdict

**safe-with-config** for `jj git init --colocate` on `kumitate-shokunin`.
Required config/practice:
1. Set jj user identity for the lane (`jj config set --user user.name '<id>-shokunin'` + `user.email` or `JJ_USER`/`JJ_EMAIL` env) and **verify the author field on the first commit** — observed `--config user.name` leave the global jj `user.name` in the author slot of the first post-init commit while fixing the committer.
2. After `jj commit`/`jj new`, re-point the branch (`jj bookmark set <branch>`) before any git tool that needs the branch tip to move; HEAD legitimately detaches while the working-copy commit sits ahead of the branch — no gate here reads `abbrev-ref HEAD`, so this is cosmetic for this repo.
3. `trunk()` aliased to `master@origin`; `jj bookmark track master@origin` for pulls.

Top hazard: silent author/committer split — first jj commit recorded `Joao Pedro Veiga <jpveigao10@gmail.com>` (global jj config) as author despite `--config user.name=kumitate-shokunin` (which only landed as committer). Misattributed lane commits would pass git-level inspection casually but fail a strict `git log %an` lane-identity audit.
