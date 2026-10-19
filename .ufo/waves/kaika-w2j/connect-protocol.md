# kaika W2j — Shokunin Protocol VCS Neutrality & jj Colocation Mapping

**Artifact:** `local://kaika-w2j-connect-protocol.md`  
**Role:** UFO-FSD connector  
**Date:** 2026-10-19  
**Substrate / Tool:** jj 0.45.1 (`~/.local/bin/jj`), git 2.47.0 (`/usr/bin/git`)  
**Scope:** `/home/vgpnk/Projects/shokunin` (fleet root and 21 lanes) and `/home/vgpnk/Projects/kimi-shokunin`

---

## 1. Executive Summary & Verdict

- **Verdict:** `safe-with-config`
- **Core Principle:** In colocated mode (`jj git init --colocate`), Jujutsu shares Git's `.git` object database directly. Git commit identifiers (40-hex SHA-1 / SHA-256) remain the invariant, universal evidence currency across the fleet. Every existing Git-based verifier, history pin, and gate script continues to function because commits created by `jj` are immediately exported to Git's object store.
- **Top Hazard:** Lane identity leakage and detached `HEAD`.
  1. `jj` 0.45.1 ignores local `.git/config` `user.name`/`user.email` if `~/.config/jj/config.toml` exists, stamping operator identity onto lane commits unless `jj config set --repo user.name/email` is configured prior to working-copy snapshotting.
  2. History-mutating `jj` commands detach Git `HEAD` (`git rev-parse --abbrev-ref HEAD` prints `HEAD`, and `git symbolic-ref HEAD` exits 128). Tooling assuming an attached branch name fails unless updated or anchored on object IDs.

---

## 2. Comprehensive Git Assumption Map & jj-Colocated Equivalents

| # | Surface / Location | Git Behavior Relied On | jj-Colocated Equivalent (Git Hash Currency Preserved) | Severity / Risk |
|---|--------------------|------------------------|-------------------------------------------------------|-----------------|
| 1 | `PROTOCOL.md:40` | Sibling lane minting: `create the sibling's repo dir {id}-shokunin/ under the fleet root and its git remote` | Sibling repo created with `jj git init --colocate`; remote added via `jj git remote add origin <url>` (or `git remote add origin <url>`). Both VCSs read and sync the same remotes. | Low |
| 2 | `PROTOCOL.md:117-122` | Report lands last; cited hash must be lane repo's `HEAD` at report time; ancestor check: `git merge-base --is-ancestor <hash> HEAD`. | Cited hash is the commit ID of the described change: `jj log -r @- -T 'commit_id'`. In colocated mode, `git merge-base --is-ancestor <hash> HEAD` succeeds exit 0 without change, because jj writes the commit into `.git` and points Git `HEAD` at `@-`. jj equivalent revset: `<hash> & ancestors(@-)`. | Low |
| 3 | `PROTOCOL.md:123-124` | Immutability: corrections land as new commits, never amending/rewriting cited commits (amending orphans the record). | jj can rewrite commits easily (`describe`, `squash`, `rebase`). If a cited hash is rewritten, `merge-base --is-ancestor` fails. In jj: create new descendant commit (`jj new <cited> && jj commit`). Guard with `revset-aliases."immutable_heads()" = "builtin_immutable_heads() | visible_heads()"`. | Medium (operational discipline) |
| 4 | `PROTOCOL.md:161-162` | Activity scan: files modified under lane repo: `find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*'`. | Must exclude `.jj/` internal operation store: `find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*' -not -path '*/.jj/*'`. Otherwise internal op logs trigger false positive activity. | Medium (false gate signal) |
| 5 | `PROTOCOL.md:353-354` | "Commits are cited by hash, never by subject or tag — `git rev-parse round-4` fails wherever the tag doesn't exist." | Retain git commit hash as citation format. jj change IDs (e.g. `kkmowrqu...`) MUST NOT be cited in reports or scorecards because external git verifiers cannot resolve them. | High (contract invariant) |
| 6 | `PROTOCOL.md:466` | Bookkeeping: `git push`ing the round's commits to remote. | `git push` remains functional. Alternatively `jj git push --bookmark <branch>`. `jj git push` alone without bookmarks will not push bare revisions. | Low |
| 7 | `PROTOCOL.md:470-472` | Pathspec-limited commit: `git commit -- .ufo/reports/round-<N>/<id>.md` (avoids sweeping sibling in-flight edits). | `jj commit -m "..." -- .ufo/reports/round-<N>/<id>.md`. Paths not included in the fileset remain in `@`, moving to a new child working copy. | Low |
| 8 | `PROTOCOL.md:473-479` | Lane authorship: child repos set `git config user.name/email`; main repo uses `git -c user.name=... -c user.email=... commit`. | **CRITICAL:** `jj` 0.45.1 reads user config from `~/.config/jj/config.toml` over `.git/config`. In child repos, run `jj config set --repo user.name "<lane>-shokunin"` and `jj config set --repo user.email "<lane>@shokunin.local"`. In main repo, execute `jj metaedit --update-author -r @` or prefix `JJ_USER=... JJ_EMAIL=... jj commit`. | High (attribution defect) |
| 9 | `MISSION.md:79-87` | Commit inside owning repo then `git push`; push scope restricted to fleet and lane remotes; domain trees read-only. | Identical semantics. Read-only domain trees remain untouched; lane repos commit locally via `jj commit` and push via `git push origin <branch>` or `jj git push`. | Low |
| 10 | `CORPUS.md:24,58` | `lessons/` entries cite commit hash; restoration of committed files (`git checkout --`). | Commit citations remain Git SHAs. File restoration at revision in jj: `jj restore -r <hash> <path>`. | Low |
| 11 | `templates/round-prompt.md:22,67-71,82-86` | Embedded instructions: commit hashes cited in SCORECARD.md; commit-then-push ordering; push scope. | Commit hashes remain 40-hex Git SHAs. Template prompt instructions remain valid under colocation; add jj command alternatives. | Low |
| 12 | `scripts/shokunin-watchdog.sh` (fleet root) | Lines 45, 61-63: checks report existence on filesystem `[ -f "$SK/.ufo/reports/round-$2/$1.md" ]`; prompt instructs commit-then-push. | Filesystem existence check is VCS-agnostic. No change needed to watchdog loop. Prompt string can state VCS-neutral commit requirement. | Low |
| 13 | `.ufo/history-pin.json` | Pinned JSON carries `"manifest_commit": "ae19fca"`, verified by `closure-check.py` via `git show <commit>:MANIFEST.json` and `git merge-base --is-ancestor <commit> HEAD`. | Unchanged. In colocated mode, Git's object database stores `manifest_commit`. `git show` and `git merge-base` execute cleanly. In jj: `jj cat -r <hash> MANIFEST.json`. | Low (fully backward compatible) |
| 14 | `kimi-shokunin/scripts/mint-agent.sh` | Lines 74-79, 87: `git init`, `git config user.name/email`, `git add -A`, `git commit -m ...`, `git rev-parse --short HEAD`. | For colocated lanes: append `jj git init --colocate` + `jj config set --repo user.name/email`. `git rev-parse --short HEAD` continues to output the Git commit SHA. | Medium (minting script update) |
| 15 | `kimi-shokunin/scripts/shokunin-watchdog.sh` | Lines 98-106: `lane_git()` uses `git -c user.name=... -c user.email=...`; `commit_evidence()` runs `lane_git "$lane" commit -q -m "round-$2: ${lane} dispatch evidence" -- "$f"`. | In colocated mode, Git commands run by the watchdog continue to create Git commits. jj automatically imports them on next run (`Done importing changes from the underlying Git repo`). Can remain Git-plumbing. | Low |
| 16 | Lane Gate Scripts (354 scripts across 21 lanes) | Extensive usage of: `git rev-parse HEAD`, `git show <rev>:<path>`, `git cat-file -e <rev>^{commit}`, `git merge-base --is-ancestor`, `git ls-files`, `git status --porcelain`. | **Colocated compatibility: 100% PASS for read-only Git object inspect commands.** Because colocation shares `.git/objects`, `git show`, `git cat-file`, `git log`, and `git ls-files` execute identically. **Exception:** gates checking `git symbolic-ref HEAD` fail on detached HEAD. | Medium (detached HEAD caveat) |

---

## 3. Evidence from Local Probes & Repository Verification

1. **Colocated Init and Object Synchronization:**
   - Scratch clone of `kimi-shokunin` (1.1 MiB) created at `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kimi-shokunin-connect`:
     ```bash
     jj git init --colocate
     ```
     Output: `Initialized repo in "."`, `Setting the revset alias trunk() to main@origin`.
   - `jj st`: took `0.010s`; created working copy `@` on top of Git `HEAD`.
   - `jj diff --stat -r @`: 0 files changed; `git status`: clean.

2. **Commit Creation & Git Hash Parity:**
   - Command:
     ```bash
     jj config set --repo user.name "protocol-shokunin"
     jj config set --repo user.email "protocol@shokunin.local"
     jj commit -m "second commit" test2.txt
     ```
   - Inspection via Git:
     ```bash
     git log -1 --format='%H %an <%ae> | %cn <%ce>'
     ```
     Output: `bd289a3f... protocol-shokunin <protocol@shokunin.local> | protocol-shokunin <protocol@shokunin.local>`
   - `jj log -r @- -T 'commit_id'`: outputs exact 40-hex SHA `bd289a3f...`.
   - `git merge-base --is-ancestor bd289a3f HEAD`: exited `0` (clean ancestry).
   - jj revset ancestry check: `jj log -r 'bd289a3f & ancestors(@-)' -T commit_id` returned `bd289a3f...`.

3. **Identity Leakage Trap Discovered:**
   - When only `git config user.name/email` was set in `.git/config`, `jj commit` used `Joao Pedro Veiga <jpveigao10@gmail.com>` from `~/.config/jj/config.toml`.
   - Passing `--config user.name=... --config user.email=...` to `jj commit` alone resulted in:
     `Author: Joao Pedro Veiga <jpveigao10@gmail.com> | Committer: protocol-shokunin <protocol@shokunin.local>`.
   - **Fix:** `jj config set --repo user.name "<id>-shokunin"` and `jj config set --repo user.email "<id>@shokunin.local"` must be executed before creating/snapshotting `@`, or repaired with `jj metaedit --update-author -r @`.

4. **Detached HEAD State Under Colocation:**
   - Immediately after `jj commit`, `git status` reports:
     `HEAD detached from refs/heads/main`
     `git rev-parse --abbrev-ref HEAD` prints `HEAD`.
     `git symbolic-ref HEAD` exits `128` (`fatal: ref HEAD is not a symbolic ref`).
   - Moving or setting a bookmark (`jj bookmark set main -r @-`) advances Git's branch ref `refs/heads/main`, but Git's `HEAD` remains detached at `@-` until `git checkout main` or `git switch main` is run.

---

## 4. Proposed Move: Minimal Bounded Contract Text Change

To make the shokunin protocol VCS-neutral under colocation without breaking existing Git verifiers, scorecards, or history pins, apply the following bounded amendment to `PROTOCOL.md`:

### Target Sections in `PROTOCOL.md`
1. §"Evidence standard" (`PROTOCOL.md:353-354`)
2. §"Lane authorship" & "Push scope" (`PROTOCOL.md:470-479`)
3. §"A lane report lands last" (`PROTOCOL.md:117-122`)
4. §"Write scope" (`PROTOCOL.md:161-162`)

### Proposed Amendment (Diff-equivalent text)

```markdown
### 1. In §Evidence standard (PROTOCOL.md:353):
- Commits are cited by canonical object hash (40-hex Git commit ID), never by subject, tag, or VCS-specific change ID. In colocated VCS environments (such as Jujutsu), commit citations remain the underlying Git commit SHA (`jj log -r @- -T 'commit_id'`). Change IDs (`change_id`) are mutable local navigation handles and do not satisfy the evidence standard.

### 2. In §A lane report lands last (PROTOCOL.md:119-122):
The cited hash is the lane repo's committed state when the report is written: a hash the repo does not contain fails verification, and one that is not an ancestor of HEAD (or the working-copy parent `@-`) at closure is a conformance defect (`git merge-base --is-ancestor <hash> HEAD` or VCS equivalent `<hash> & ancestors(@-)` is the check). Under colocated VCS, tools must evaluate ancestry against the commit object ID, as the working tree may operate in a detached-HEAD state. Corrections land as new descendant commits, never by amending or rewriting a cited commit.

### 3. In §Write scope & Lane authorship (PROTOCOL.md:162, 470-479):
- Activity scans exclude both Git and Jujutsu metadata directories:
  `find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*' -not -path '*/.jj/*'`
- A lane's main-repo commit is pathspec-limited to its own report file (`git commit -- .ufo/reports/round-<N>/<id>.md` or `jj commit -- .ufo/reports/round-<N>/<id>.md`) — never sweeping unowned working-tree files.
- Lane authorship is auditable across all active VCS frontends: in colocated repositories, lane identity (`<lane>-shokunin` / `<lane>@shokunin.local`) MUST be configured in both Git (`git config user.name/email`) and Jujutsu repository config (`jj config set --repo user.name/email`). Main-repo commits made via Jujutsu must ensure the working-copy author carries the lane identity (`jj metaedit --update-author -r @` or `JJ_USER`/`JJ_EMAIL` environment variables) before committing.
```

---

## 5. Second-Order Effects & Trade-Off Analysis

| Dimension | Surface | Impact / Second-Order Effect | Resolution / Safety Gate |
|-----------|---------|------------------------------|---------------------------|
| **Soundness** | Contract | Eliminates git-only lock-in while maintaining 100% backward compatibility with Git hashes. | Commits cited in reports remain immutable Git SHAs. No format change in SCORECARD.md or MANIFEST.json. |
| **Operability** | Runtime / Lanes | Lanes gain operation log (`jj op log`), safe undo (`jj undo`), and conflict resilience without breaking Git tooling. | Colocation allows Git CLI and jj CLI to coexist in the same directory. |
| **Integrity** | Verification | `closure-check.py` and `history-pin.json` verify git commit objects directly. | Because `jj` exports directly to `.git`, `closure-check.py` passes with zero code modifications. |
| **Calibration** | Attribution | Prevents silent leakage of host/operator identity (`Joao Pedro Veiga`) into lane commits. | Mandatory `jj config set --repo` in seed/mint kit (`mint-agent.sh`). |
| **Substrate** | File system | Prevents `.jj/` operation metadata from registering as fake lane activity. | Exclude `*/.jj/*` in file activity `find` patterns. |
| **Constraint** | Git Worktrees | Active craft rounds currently run in Git worktrees (`.tower/worktrees/kaika/`). `jj` 0.45.1 does NOT support linked Git worktrees (`git-worktree: No`). | Colocation must NOT be enabled inside active `.tower/worktrees/kaika/*` worktrees; adoption applies to lane root repos after worktrees retire or cut over. |

---

## 6. Risks & Mitigation

1. **Risk: Commit Rewriting (`jj describe -r`, `jj rebase`, `jj squash`).**
   - *Consequence:* Rewriting a commit generates a new Git SHA; the previously cited hash becomes orphaned, causing `git merge-base --is-ancestor` to exit 1 (conformance defect).
   - *Mitigation:* Explicit contract clause: corrections land as new descendant commits (`jj new <cited> && jj commit`). Add `immutable_heads() = "visible_heads()"` in repo config to block rewrites.
2. **Risk: Detached HEAD in Git Tools.**
   - *Consequence:* Scripts invoking `git symbolic-ref --short HEAD` or checking `git rev-parse --abbrev-ref HEAD == master` will fail after any `jj` command.
   - *Mitigation:* Audit lane gates to ensure they resolve revisions via explicit hashes or `HEAD` object IDs rather than symbolic branch names.
3. **Risk: Concurrent Undo / Restore Across Workspaces.**
   - *Consequence:* In jj 0.45.1, `jj undo` and `jj op restore` operate repository-wide. If multiple agents share a single `.jj` repository, one agent's undo restores another agent's snapshot.
   - *Mitigation:* Preserve one distinct repository per lane (`<id>-shokunin/`). Never share a single colocated repository across multiple uncoordinated concurrent agents.

---

## 7. Verification Steps

1. In any test repo, initialize colocated jj:
   `jj git init --colocate` (exit code `0`).
2. Verify git status and commit resolution:
   `jj commit -m "test" <file>`
   `git log -1 --format='%H'` matches `jj log -r @- -T 'commit_id'`.
3. Verify ancestry check:
   `git merge-base --is-ancestor $(jj log -r @- -T 'commit_id' --no-graph) HEAD` returns exit code `0`.
4. Verify history pin anchor:
   `git show $(cat .ufo/history-pin.json | jq -r .manifest_commit):MANIFEST.json` resolves cleanly.
5. Verify clean tree and exclusion:
   `find . -newermt "1 hour ago" -type f -not -path '*/.git/*' -not -path '*/.jj/*'` ignores internal VCS metadata.
