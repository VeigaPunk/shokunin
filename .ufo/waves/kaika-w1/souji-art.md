# kaika W1 — ART dossier — souji-shokunin (掃除: repo and workspace hygiene)

author: W1ArtSouji (scout, read-only) · date: 2026-10-19 · lane HEAD `dcc8b9e` (`git --no-optional-locks -C souji-shokunin log -1 --format=%h`) · host git 2.55.0 (`git --version`), git-filter-repo 2.47.0-3, shellcheck 0.11.0 (`pacman -Q git git-filter-repo shellcheck`)

- **Tools:** `web_search` was available and used. Every SOURCES row below was opened in this session: a web page, raw source at a tag, or an installed man page.
- **Read-only:** I kept to read-only work, with one exception, disclosed here. I wrote a scratch copy of git-filter-repo.txt to `/tmp/.souji-art-gfr.txt` and deleted it in the same session (`ls` → "No such file"). I touched no lane file, git state, or install.
- **Injection check:** none of the fetched pages contained instructions aimed at the reader. I found no prompt-injection attempt.
- **Method caveat:** in this agent harness, `find`/`rm`/`mv`/`grep`/`wc`/`ls` are harness builtins: `type -a find` prints "find is a shell builtin", and `find --version` prints 0.8.0. A child `bash` uses the GNU tools instead: `bash -c 'find --version'` prints GNU findutils 4.11.0, and `rm` is GNU coreutils 9.11. I re-ran every lane and man-page count below under `bash -c`, and the results matched. Wave 2 should run its pasteable counts the same way.

---

## 1. Uncovered ground

### What the lane already holds

- **SKILL.md** covers:
  - the receipt taxonomy: pushed / moved-to-obsidian / stale, plus `metadata-prune` and fail-closed refusals (:12-26)
  - the classify table (:30-38)
  - the removal flow: dry run → approval → `git mv` into `.ufo-quarantine/<utc-date>/` → hold (≥450 s, 24 h preferred) → second check → delete (:40-47)
  - the Never list (:49-58)
  - 4 false-SAFE error patterns (:60-76)
  - checklists (:78-90) and known surfaces (:92-106)
- **PROVINCE.md headings** (`grep -nE '^## ' PROVINCE.md`): Owns :6, Work surfaces :19, Refuses :26, Adjacency :38. There is no Core/Frontier/Adjacent split, which LEARNING.md:68-70 calls for.
  - Owns includes "duplicate configs" and dead worktree *metadata* (:11-12).
- **corpus/knowledge/** holds 1 file, `obsidian-ledger.tsv` (`ls corpus/knowledge | wc -l` → 1).
- **corpus/lessons/** holds 11 files (`ls corpus/lessons | wc -l` → 11).
- **corpus/QUALITY.md** is absent (`test -e corpus/QUALITY.md; echo $?` → 1).
- **corpus/README.md** has no coverage map and no `## Frontier` (`grep -c '^## Frontier' corpus/README.md PROVINCE.md` → 0 and 0).
- **Held in tools but not in the corpus:** all 4 installed tools set `GIT_OPTIONAL_LOCKS` (`grep -lE 'GIT_OPTIONAL_LOCKS|no-optional-locks' tools/souji-{verify,vault-verify,quarantine,census}.sh | wc -l` → 4). SKILL.md never mentions it (`grep -cE 'GIT_OPTIONAL_LOCKS|no-optional-locks' SKILL.md` → 0).

### What the lane does not hold

Each count below is a sweep over the whole lane tree. Command: `bash -c "grep -rIlE '<pattern>' --exclude-dir=.git . | wc -l"`, with cwd `souji-shokunin`.

- **Git's own deletion machinery** — 1 file. Pattern: `git maintenance|maintenance\.(strategy|auto)|gc\.worktreePruneExpire|gc\.pruneExpire|gc\.reflogExpire`. The single hit is `tools/souji-census.impl-46.sh:111` (`-c maintenance.auto=false`), a draft that was never installed.
- **Size census** — 0 files. Pattern: `git-sizer|git repo structure|count-objects|rev-list --disk-usage|filter-repo --analyze`.
- **Duplicate finders** — 0 files. Pattern: `rmlint|jdupes|fdupes|fclones|czkawka|rdfind`. This is despite PROVINCE.md:12 owning "duplicate configs".
- **Object-level holds** — 0 files. Pattern: `expire-to|cruft pack|gc\.pruneExpire`.
- **Restorable-removal formats** — 0 files. Pattern: `trashinfo|trash-put|freedesktop|Trash spec`. This is despite LOG.md:447-449 recording that `~/.local/share/Trash` was emptied.
- **Rewrite tools named in the Never list** — 0 in each file. Pattern: `filter-repo|BFG|git replay|git history (reword|split|fixup|drop)|filter-branch`, checked with `grep -cE` over SKILL.md, PROVINCE.md and AGENTS.md (0/0/0).
  - SKILL.md:51 names only `reset --hard`, rebase and amend.
  - The frontmatter phrase "NEVER git history rewrite" (SKILL.md:2) now reads the same as the experimental `git history` command (2.54+).
- **SKILL rules with zero hits** (`bash -c "grep -cE '<p>' SKILL.md"` → 0 for each):
  - `nested`
  - `NUL|-z\b`
  - `add -A|pathspec`
  - `descendant`
  - `same file ?system|one-file-system|rename\(`
  - `lock --reason|worktree lock`
  - `maintenance`

---

## 2. Current art (2025–2026) the corpus does not hold

1. **Git maintenance now deletes by default** (S009, S010, S001).
   - 2.50.0 (2025-06-16) added a reflog-expire task (RelNotes 2.50.0:34). It also exposed gc's clean-up tasks to `git maintenance` (:65-66). In 2.55.0 these are `worktree-prune` and `rerere-gc`; each appears 5 times in the man page (`zcat /usr/share/man/man1/git-maintenance.1.gz | grep -cE 'worktree(\\)?-prune'` → 5; same with `'rerere(\\)?-gc'` → 5).
   - 2.52.0 (2025-11-17) added the geometric strategy (RelNotes 2.52.0:73-75).
   - **2.54.0 (2026-04-20) made geometric the default** (RelNotes 2.54.0:58). The code confirms it:
     - v2.53.0 `builtin/gc.c:1983` uses `strategy = gc_strategy;`
     - v2.54.0 `:1973` and v2.55.0 `:1974` use `strategy = geometric_strategy;` for unscheduled runs.
     - The geometric strategy includes `worktree-prune` and `reflog-expire` as MANUAL-type tasks (gc.c:1894-1921).
     - `--auto` runs count as unscheduled. `git commit`, `fetch`, `merge`, `am` and `rebase` each contain one `run_auto_maintenance` call (`curl -fsSL https://raw.githubusercontent.com/git/git/v2.55.0/builtin/<f>.c | grep -c run_auto_maintenance` → 1 each).
   - 2.55.0 fixed the background-maintenance lockfile (RelNotes 2.55.0:327-330).
   - 2.56.0 (2026-09-28) made housekeeping pluggable (:370-373) and changed when rerere-gc triggers (:545-547).
2. **Native size census** (S005, S010, S014, S013).
   - 2.52 added `git repo`, 2.53 added size information to `git repo structure` (RelNotes 2.53.0:34-35), and 2.54 added maximum values (2.54.0:88-89). The command is marked EXPERIMENTAL.
   - Its stated intent is to replace git-sizer, whose last release is v1.5.0 (2021-11-16).
3. **Git deletes only what it can recover** (S004).
   - 2.56 adds `git repack --drop-filtered [--dry-run]`. It drops promisor blobs only when they can be re-fetched. It refuses to run mid-operation and refuses blobs the index references.
   - The host's 2.55.0 does not have it (`zcat /usr/share/man/man1/git-repack.1.gz | grep -cE 'drop(\\)?-filtered'` → 0).
   - `--expire-to` (copy pruned objects elsewhere) is present: `zcat /usr/share/man/man1/git-repack.1.gz | grep -cE 'expire(\\)?-to'` → 1, and the same on `git-gc.1.gz` → 2.
4. **Built-in history rewriting** (S010). Experimental `git history` gained `reword`/`split` (2.54.0:10-11), `fixup` (2.55.0:28) and `drop` (2.56.0:38-40). The Never list does not name it (section 1).
5. **Git 3.0** (no release date; S011) will default to reftable refs, `safe.bareRepository=explicit` and sha256. Each changes an assumption a file- or ref-based census makes.
6. **Duplicate-finder releases.** GitHub dates come from `curl -fsSL https://github.com/<repo>/releases/tag/<tag> | grep -oE 'datetime="[^"]+"' | head -1`. The jdupes date comes from `curl -fsSL 'https://codeberg.org/api/v1/repos/jbruchon/jdupes/releases?limit=1' | jq -r '.[0] | [.tag_name, .published_at] | @tsv'`.

   | tool | version | release date | note |
   |---|---|---|---|
   | jdupes | v1.31.2 | 2026-09-02 | Codeberg; `curl -fsSI https://github.com/jbruchon/jdupes/releases/latest` → 404 |
   | czkawka | 12.0.2 | 2026-09-09 | |
   | rdfind | 1.8.0 | 2026-02-22 | |
   | fdupes | v2.4.0 | 2025-03-30 | |
   | rmlint | v2.10.3 | 2025-03-22 | |
   | fclones | v0.35.0 | 2025-03-03 | |

   None is installed on the host (`for t in rmlint jdupes fdupes fclones czkawka_cli rdfind; do command -v $t; done` → all absent).
7. **Safe-removal tooling** (S022, S023).
   - trash-cli 0.26.9.29 was released 2026-09-29.
   - The FreeDesktop Trash spec moved to `/trash/latest/`; the old `/trash-spec/latest/` returns 404 (`curl -fsS -o /dev/null -w '%{http_code}' <url>`).
   - On the host, `gio` is present and `trash-put` is absent (`command -v`).
8. **History-rewrite tooling** (S012). git-filter-repo v2.47.0 (2024-12-04) is the current release, and it matches the host's 2.47.0-3. It now has `--sensitive-data-removal` (`zcat /usr/share/man/man1/git-filter-repo.1.gz | grep -cE 'sensitive(\\)?-data(\\)?-removal'` → 8).

---

## 3. SOURCES.md rows (contract draft)

Rows use `| S0NN |` with spaces, because the contract's counting regex needs them (defect D6 in section 8). Count rows with `grep -cE '^\| S[0-9]{3} ' kaika-w1-souji-art.md`, and tiers with `grep -E '^\| S[0-9]{3} ' kaika-w1-souji-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`.

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | git-maintenance(1) § TASKS + § CONFIGURATION (maintenance.strategy, maintenance.auto) — https://git-scm.com/docs/git-maintenance | docs | A | Tasks include reflog-expire, rerere-gc, worktree-prune and geometric-repack; geometric is the default for manual maintenance and removes worktrees that cannot be located; maintenance.auto gates the auto runs that porcelain commands trigger | queued | 2026-10-19 | on-release | — |
| S002 | git-gc(1) § OPTIONS, § CONFIGURATION, § NOTES — https://git-scm.com/docs/git-gc | docs | A | Git's own deletions wait out grace periods: pruneExpire 2 weeks, reflog 90 days (30 if unreachable), worktreePruneExpire 3 months, rerere 60/15 days; --prune=now raises corruption risk under concurrent writers; --expire-to | queued | 2026-10-19 | on-release | — |
| S003 | git-worktree(1) § COMMANDS lock/prune, § OPTIONS, § Porcelain Format — https://git-scm.com/docs/git-worktree | docs | A | prune -n -v --expire; lock --reason writes worktrees/<id>/locked and blocks prune, move and remove; list --porcelain -z gives NUL-safe locked/prunable attributes | queued | 2026-10-19 | on-release | — |
| S004 | git-repack(1) --cruft, --expire-to, --drop-filtered, --dry-run — https://git-scm.com/docs/git-repack | docs | A | --expire-to keeps pruned objects in a separate directory as a backup; 2.56 --drop-filtered deletes only promisor blobs that can be re-fetched, refuses mid-operation or for index-referenced blobs, and has a --dry-run | queued | 2026-10-19 | on-release | — |
| S005 | git-repo(1) § COMMANDS structure — https://git-scm.com/docs/git-repo | docs | A | EXPERIMENTAL; reports ref counts, reachable object counts, inflated and disk sizes, and largest objects; lines/nul/-z formats are for parsing, table is not | watch | 2026-10-19 | on-release | — |
| S006 | git(1) § ENVIRONMENT GIT_OPTIONAL_LOCKS and --no-optional-locks — https://git-scm.com/docs/git (installed /usr/share/man/man1/git.1.gz 2.55.0) | docs | A | With GIT_OPTIONAL_LOCKS=0, git status stops refreshing and rewriting the index as a side effect; the doc basis for a read-only census (cf. git-status § BACKGROUND REFRESH) | queued | 2026-10-19 | on-release | — |
| S007 | git-clean(1) -n/--dry-run, clean.requireForce — https://git-scm.com/docs/git-clean | docs | A | Git's own deleter refuses to run without -f and supports dry run; untracked nested repositories need a second -f, so nested repos are a separate safety class | queued | 2026-10-19 | on-release | — |
| S008 | git-last-modified(1) — https://git-scm.com/docs/git-last-modified | docs | A | EXPERIMENTAL (2.52+); shows which commit last modified each path, an age signal for tracked files that does not rely on mtime | queued | 2026-10-19 | on-release | — |
| S009 | git/git source at v2.55.0: builtin/gc.c, worktree.c, run-command.c — https://github.com/git/git/blob/v2.55.0/builtin/gc.c | code | A | Ground truth: unscheduled maintenance defaults to geometric (gc.c:1974); worktree-prune runs worktree prune --expire 3.months.ago (gc.c:162, 379-388); locked registrations are skipped (worktree.c:954-956); porcelain spawns maintenance run --auto (run-command.c:1980) | queued | 2026-10-19 | on-release | — |
| S010 | Git release notes 2.50.0 to 2.56.0 — https://github.com/git/git/tree/master/Documentation/RelNotes | docs | A | Dated record of changes: gc clean-up tasks join maintenance (2.50); git repo and geometric strategy (2.52); structure sizes (2.53); geometric becomes default and git history arrives (2.54); history fixup (2.55); repack --drop-filtered (2.56) | watch | 2026-10-19 | on-release | — |
| S011 | Git BreakingChanges § Git 3.0 — https://git-scm.com/docs/BreakingChanges | docs | A | Planned defaults: sha256, reftable refs (tombstones and geometric compaction), main as default branch, safe.bareRepository explicit; each changes an assumption a ref- or file-based receipt makes | watch | 2026-10-19 | 90d | — |
| S012 | git-filter-repo(1): --analyze, --sensitive-data-removal, § FRESH CLONE SAFETY CHECK — https://github.com/newren/git-filter-repo/blob/main/Documentation/git-filter-repo.txt | docs | A | --analyze does not modify the repo yet writes reports under .git/filter-repo/; refuses clones that are not fresh; warns against a --force habit; history rewriting stays operator-owned | queued | 2026-10-19 | on-release | — |
| S013 | git-sizer README (last release v1.5.0, 2021-11-16) — https://github.com/github/git-sizer | docs | A | Size metrics with a level-of-concern scale and --json; the vocabulary git repo structure aims to replace; stale release cadence | watch | 2026-10-19 | on-release | — |
| S014 | GitLab blog, What's new in Git 2.53.0 § git-repo-structure — https://about.gitlab.com/blog/whats-new-in-git-2-53-0/ | community | B | Git contributors state that git repo structure should eventually become a native replacement for git-sizer | queued | 2026-10-19 | 180d | — |
| S015 | GitHub Docs, Removing sensitive data from a repository — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository | docs | A | Adjacent (kagi): revoke or rotate a leaked secret first; filter-repo rewrites have side effects and need coordination; souji routes this work and never does it | watch | 2026-10-19 | 180d | — |
| S016 | rmlint(1) manual, docs/rmlint.1.rst — https://github.com/sahib/rmlint/blob/master/docs/rmlint.1.rst | docs | A | rmlint never deletes files itself: it writes a reviewable rmlint.sh and json; // tags original paths; -k keeps tagged; -m requires a tagged match; -p compares byte by byte; handlers remove/reflink/hardlink | queued | 2026-10-19 | on-release | — |
| S017 | rmlint docs, Cautions (why it's hard to write a dupefinder) — https://rmlint.readthedocs.io/en/latest/cautions.html | docs | A | Tool-independent failure list with reproducible demos: the same path reached twice or via symlinks, hardlink false positives, hash collisions, odd filenames; advises moving duplicates to a holding area instead of deleting | queued | 2026-10-19 | 365d | — |
| S018 | jdupes README (v1.31.2, 2026-09-02) — https://codeberg.org/jbruchon/jdupes | docs | A | Chooses careful over aggressive; -Q skips byte-for-byte verification (WARNING); -T must be given twice; -t turns off pre-action change checks and is named a TOCTTOU vulnerability; guards against traversing the same path twice | queued | 2026-10-19 | on-release | — |
| S019 | fdupes(1) man page (v2.4.0, 2025-03-30) — https://github.com/adrianlopezroche/fdupes/blob/master/fdupes.1 | docs | A | --log records deletion choices; --deferconfirmation byte-checks just before deleting; --immediate implies --noprompt; CAVEATS cover the symlink trap and a directory given twice | queued | 2026-10-19 | on-release | — |
| S020 | fclones README (v0.35.0, 2025-03-03) — https://github.com/pkolaczk/fclones/blob/main/fclones/README.md | docs | A | Finding (group) is separate from acting (remove, move or link read the saved report); --dry-run prints the exact commands; move target_dir is a built-in holding area; keep-path and keep-name guards | queued | 2026-10-19 | on-release | — |
| S021 | fclones source src/dedupe.rs at main — https://github.com/pkolaczk/fclones/blob/main/fclones/src/dedupe.rs | code | A | Rechecks at act time: skips non-regular files and files whose length changed, and aborts a group if any file changed after the report (dedupe.rs:815-849) | queued | 2026-10-19 | on-release | — |
| S022 | FreeDesktop.org Trash Specification 1.0 (2014-01-02) — https://specifications.freedesktop.org/trash/latest/ | spec | A | Restorable layout: files/ plus info/<name>.trashinfo with Path and DeletionDate; info written first with O_EXCL; earlier trashings never overwritten; shared .Trash must not be a symlink | queued | 2026-10-19 | 365d | — |
| S023 | trash-cli README (0.26.9.29, 2026-09-29) — https://github.com/andreafrancia/trash-cli | docs | A | Spec-compliant CLI: trash-put, trash-list, trash-restore, trash-rm; trash-empty <days> purges by age; FAQ advises against aliasing rm to trash-put | queued | 2026-10-19 | on-release | — |
| S024 | GNU coreutils manual, rm invocation — https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html | docs | A | --one-file-system skips other mounts during recursive removal; --preserve-root=all rejects arguments on a different file system from their parent; -I prompts once | queued | 2026-10-19 | on-release | — |
| S025 | GNU coreutils manual, mv invocation — https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html | docs | A | mv is a rename within one file system; across file systems it copies and then removes, and a failed multi-directory move can be left split between file systems | queued | 2026-10-19 | on-release | — |
| S026 | find(1) ACTIONS -delete, GNU findutils 4.11.0 — installed man page via man find (web manual html_mono/find.html returned 404 on 2026-10-19) | docs | A | -delete turns on -depth, so -prune stops working; putting -delete first deletes everything under the start points; test with -print first | queued | 2026-10-19 | on-release | — |
| S027 | ShellCheck wiki SC2115 — https://github.com/koalaman/shellcheck/wiki/SC2115 | docs | A | rm -rf "$VAR/"* deletes from / when VAR is empty; use ${VAR:?}; SC2115 is warning severity, so a -S error gate cannot see it (checked locally with shellcheck 0.11.0) | queued | 2026-10-19 | 365d | — |
| S028 | GitLab, Postmortem of database outage of January 31 (2017-02-10) — https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/ | docs | A | Still the reference case for deleting on the wrong target: a data-directory wipe meant for the secondary ran on the primary; about 300 GB gone; the pg_dump backups were missing | queued | 2026-10-19 | 365d | — |
| S029 | Google SRE book ch. 26, Data Integrity — https://sre.google/sre-book/data-integrity/ | book | B | Soft deletion is the first defense layer, with lazy deletion behind it; usual delays are 15 to 60 days; what matters is recovery, not backups | queued | 2026-10-19 | 365d | — |
| S030 | OneNine, How to Reduce Git Repository Size Safely — https://onenine.com/how-to-reduce-git-repository-size-safely/ | community | C | REJECTED: recommends a monthly git gc --aggressive --prune=now and offers filter-branch, contradicting S002 and the filter-branch WARNING | rejected | 2026-10-19 | — | — |

Tally: A 27, B 2 (S014, S029), C 1 (S030); total 30. Statuses: queued 24, watch 5, rejected 1, mined 0 — no knowledge entry cites any row yet.

Why older sources are kept:
- S022 (2014) is still the current spec version (1.0).
- S028 (2017) is still the reference case for deleting on the wrong target and for backups that were never tested.
- S029 (2016) is still the standard text on soft deletion.

## Leads (unopened)

- **Git and repository analysis**
  - Git mailing list, "[PATCH 0/8] builtin/maintenance: use "geometric" strategy by default" — https://ratatoskr.run/git/2026/02/8029429/t
  - Taylor Blau, "New techniques in repacking monorepos" (Git Merge 2025) — https://ttaylorr.com/presentations/git-merge-2025.pdf
  - gitrepository-layout(5), worktrees/<id>/{gitdir,locked,index} — https://git-scm.com/docs/gitrepository-layout
  - git-cherry(1), patch-equivalence for commits rebased and then pushed; a source of false negatives for the pushed receipt — https://git-scm.com/docs/git-cherry
  - git-rev-list(1) `--disk-usage`; git-count-objects(1) `-vH` — https://git-scm.com/docs/git-rev-list, https://git-scm.com/docs/git-count-objects
  - Scalar maintenance registration — https://git-scm.com/docs/scalar
  - GitLab docs, Repository size — https://docs.gitlab.com/user/project/repository/repository_size/
  - GitHub Blog, Highlights from Git 2.55 / 2.56 — https://github.blog/open-source/git/highlights-from-git-2-56/
  - git-annex `unused`/`dropunused` and numcopies, deletion gated on verified copies — https://git-annex.branchable.com/
- **Duplicates and safe removal**
  - duperemove and dupd, both referenced by S017 — https://github.com/markfasheh/duperemove, https://github.com/jvirkki/dupd
  - Bumblebee `rm -rf /usr` space-in-path issue #123, linked from S017 — https://github.com/MrMEEE/bumblebee-Old-and-abbandoned/issues/123
  - safe-rm, a wrapper that blocks deletion of protected paths — https://launchpad.net/safe-rm

---

## 4. Candidate knowledge entries (6)

The lane has no `corpus/QUALITY.md` (section 1), so "clears the bar" means two things here:
- the fleet floor: CORPUS.md:23-25 (sourced, falsifiable) and :33-47 (a count carries its command, a negative carries its sweep, a quote names its location, an index row is a claim);
- the proposed seed criteria Q1–Q4 in section 7.

### C1 `git-auto-maintenance-prunes-worktrees`

- **Claim.** On git ≥2.54 (host: 2.55.0), these steps follow from a single `git commit`:
  1. `commit` (and likewise `fetch`, `merge`, `am`, `rebase`) spawns `git maintenance run --auto`.
  2. Unscheduled runs use the geometric strategy.
  3. That strategy's `worktree-prune` task runs `git worktree prune --expire <gc.worktreePruneExpire, default 3.months.ago>` once at least 1 registration is prunable.
  4. Registrations with a `locked` file are skipped.
  5. Registrations whose gitdir file is missing or unreadable are prunable at any age.
  6. A missing working tree becomes prunable once `worktrees/<id>/index` is older than the expiry.

  So souji's own quarantine commit can prune worktree metadata with no souji receipt. SKILL.md:44 says "quarantine is a normal commit in the owning repo", and the commit is only protected if run as `git -c maintenance.auto=false commit` or if the registration is locked.
- **Sources** (S009, S010, S001):
  - `builtin/gc.c`@v2.55.0: `:1974` (`strategy = geometric_strategy;`), `:162` (`3.months.ago`), `:379-388` (task), `:391-420` (condition, `maintenance.worktree-prune.auto` limit 1), `:1894-1921` (geometric task table)
  - `worktree.c`@v2.55.0: `:954-956` (locked), `:949-953` and `:958-993` (invalid admin dir or broken gitdir file), `:1001-1008` (index mtime ≤ expire)
  - `run-command.c`@v2.55.0: `:1980`
  - Quote, RelNotes 2.54.0:58: "\"git maintenance\" starts using the \"geometric\" strategy by default."
  - Quote, S001 § CONFIGURATION › maintenance.auto: "controls whether some commands run git maintenance run --auto after doing their normal work. Defaults to true."
- **Lane evidence.**
  - Installed tools guard against this 0 times (`grep -lE 'maintenance\.auto|gc\.auto' tools/souji-{verify,vault-verify,quarantine,census}.sh | wc -l` → 0).
  - `souji-quarantine.sh` runs `git mv` (:529) but no commit. The commit step is manual (e.g. e20f4fa, LOG.md:379-380).
  - SKILL.md mentions worktree lock 0 times (section 1).
- **Fills:** F1 (proposed): git-native housekeeping vs receipts.
- **Recheck:** `v=$(git --version | awk '{print $3}'); curl -fsSL https://raw.githubusercontent.com/git/git/v$v/builtin/gc.c | grep -c 'strategy = geometric_strategy;'` → 1.
- **Falsifying fixture** (wave 2, under `/var/tmp`, never a live path):
  1. Set up the fixture: `git init`, then an empty commit.
  2. Add a detached worktree: `git worktree add --detach ../wt`.
  3. Remove its directory: `rm -rf ../wt`.
  4. Age its index: `touch -d '100 days ago' .git/worktrees/wt/index`.
  5. Commit: `git -c maintenance.autoDetach=false commit --allow-empty -m x`.
  6. Expect `git worktree list | wc -l` to drop from 2 to 1.
  7. Repeat with `-c maintenance.auto=false`, and again after `git worktree lock`. Both should stay at 2.
- **[INFERENCE, not fixture-run]** Pruning a detached registration deletes that worktree's HEAD. Commits reachable only from it then lose that root; S002 NOTES lists refs/*, index and reflogs as what keeps objects alive. If so, git itself can trigger the SKILL.md:75-76 "Worktree-with-unique-commits" hazard.
- **Quality bar:** fleet floor; Q1 (version-pinned: the default changed between 2.53 and 2.54), Q2 (code at a tag over prose), Q4 (fixture-falsifiable).

### C2 `git-grace-periods-and-expire-to`

- **Claim.** Git's own deletions wait out grace periods by default:
  - unreachable objects are pruned only once older than `gc.pruneExpire` (2.weeks.ago);
  - reflog entries expire after 90 days, or 30 days if unreachable;
  - worktree admin files are pruned after 3.months.ago;
  - rerere records are kept for 60 days (resolved) or 15 days (unresolved).

  `--prune=now` gives this up. `--cruft --expire-to=<dir>` (`git gc` or `git repack -d`) keeps the pruned objects in a separate directory. For comparison, souji's hold is ≥450 s, with 24 h preferred for anything not pushed (SKILL.md:45).
- **Sources:**
  - S002 § CONFIGURATION (gc.pruneExpire, gc.reflogExpire, gc.reflogExpireUnreachable, gc.worktreePruneExpire, gc.rerereResolved/Unresolved)
  - Quote, S002 § OPTIONS: "--prune=now prunes loose objects regardless of their age and increases the risk of corruption if another process is writing to the repository concurrently"
  - Quote, S004 --expire-to: "useful for keeping a copy of any pruned objects in a separate directory as a backup"
  - Quote, S029 § First Layer: Soft Deletion: "Common choices of soft deletion delays are 15, 30, 45, or 60 days."
- **Fills:** F1 and F4.
- **Recheck:** `man git-gc | grep -nE '2.weeks|3.months|90 days|30 days|60 days|15 days'` and `git config --get gc.pruneExpire || echo unset`.
- **Quality bar:** fleet floor and Q1. The entry holds facts only. Changing the hold period is a SKILL decision for wave 2.

### C3 `size-census-git-repo-structure`

- **Claim.** Git ≥2.53 ships `git repo structure`, marked EXPERIMENTAL. It reports:
  - ref counts;
  - reachable object counts;
  - inflated and disk sizes by type;
  - the largest objects (from 2.54).

  Only `lines`/`nul`/`-z` output is meant for parsing; `table` "may change and is not intended for machine parsing". Git contributors intend it to replace git-sizer, whose last release was v1.5.0 (2021-11-16).

  `git filter-repo --analyze` does not modify history, but it does write reports under `.git/filter-repo/`. A read-only census should therefore run it only on a `--no-local` clone, never on a live lane repo.
- **Sources:**
  - S005 § COMMANDS `structure`
  - S010 RelNotes 2.53.0:34-35 and 2.54.0:88-89
  - Quote, S014: "eventually become a native replacement for tools such as git-sizer(1)"
  - S012 § OPTIONS --analyze: "Will not modify your repo."
  - Quote, S012 Documentation line 418: "Every time filter-repo is run, files are created in the `.git/filter-repo/`"
- **Fills:** F2 (proposed): repository size census. The lane currently holds 0 size-census commands (section 1).
- **Recheck:** `git help repo | grep -c 'THIS COMMAND IS EXPERIMENTAL'`, then `git repo structure --format=lines | cut -d= -f1 | sort -u` on a clone.
- **Open question:** does `git repo structure` take optional locks or write anything? Not verified. Wave 2 can test this by running it with `GIT_OPTIONAL_LOCKS=0` on a clone and diffing `find .git -newer <stamp>`.
- **Quality bar:** fleet floor, Q1, Q4.

### C4 `dupe-finders-detect-then-act`

- **Claim.** Maintained duplicate finders keep detection and deletion separate, and recheck at act time:
  - rmlint never deletes; it writes a reviewable script.
  - fclones `group` writes a report that `remove`/`move`/`link` consume. `--dry-run` prints the commands. At act time it skips files whose length changed, and aborts a group if any file changed after the report.
  - fdupes `--log` records the deletion choices.
  - jdupes calls turning off its pre-action change checks (`-t`) a TOCTTOU vulnerability, and warns that hash-only `-Q` risks data loss.

  A souji duplicate verdict therefore needs three things:
  1. byte comparison (`cmp`);
  2. a designated original (rmlint `//` with `-k`);
  3. a recheck at act time.

  The receipt taxonomy (SKILL.md:19-23) holds none of these, yet PROVINCE.md:12 owns "duplicate configs".
- **Sources and quotes:**
  - S016 rmlint.1.rst:28: "rmlint itself WILL NOT DELETE ANY FILES."
  - S021 dedupe.rs:843: "Bail out as well if any file has been modified after `config.modified_before`."
  - S018 README:249-251: "disables file change checks during/after scanning. This opens a security vulnerability that is called a TOCTTOU"
  - S018 :323-324: "Do not use it on ANY data set for which any amount of data loss is unacceptable."
  - S019 fdupes.1:131-132: "Log file deletion choices to LOGFILE."
- **Fills:** F3 (proposed): duplicate verdicts.
- **Recheck:**
  - `curl -fsSL https://raw.githubusercontent.com/pkolaczk/fclones/main/fclones/src/dedupe.rs | grep -c modified_before`
  - `curl -fsSL https://raw.githubusercontent.com/sahib/rmlint/master/docs/rmlint.1.rst | grep -c 'WILL NOT DELETE'`
- **Quality bar:** fleet floor; Q3 (paired with documented failure cases from S017 and S018).
- **Decision for the operator:** a `duplicate` receipt class would change the taxonomy and the tools. That needs operator approval; this entry holds facts only.

### C5 `trash-spec-restorable-quarantine`

- **Claim.** Trash spec 1.0 defines a layout from which removed items can be restored:
  - the payload lives in `$trash/files/`;
  - each item has one `$trash/info/<name>.trashinfo` with `Path=` and `DeletionDate=`;
  - the info file is created first, atomically, with O_EXCL;
  - a repeat trashing of the same path must not overwrite the earlier copy;
  - a payload without its info file is an "emergency case";
  - a shared `$topdir/.Trash` must be checked not to be a symlink.

  souji's r10 containment defect is a case of that last rule: a symlinked `.ufo-quarantine` was followed outside the repo (census/round-10/S06-cluster-C-member2.md:53-63).
- **Sources and quotes:**
  - S022 § 5: "The implementation also MUST check that this directory is not a symbolic link."
  - S022 § 6: "When trashing a file or directory, the implementation MUST create the corresponding file in $trash/info first."
- **Fills:** F4 (proposed): restorable quarantine format.
- **Recheck:** `curl -fsSL https://specifications.freedesktop.org/trash/latest/ | grep -c 'not a symbolic link'` (≥1), and check that the page still says "Version: 1.0".
- **Quality bar:** fleet floor, Q3.

### C6 `quarantine-same-filesystem-rename`

- **Claim.** GNU `mv` behaves differently across file systems:
  - normally, `mv` just renames;
  - across file systems, it copies as `cp -a` and then removes the original;
  - a failed multi-directory move can be left split between the two file systems.

  GNU `rm` has two flags that limit deletion to one file system:
  - `--one-file-system` skips other mounts during recursive removal;
  - `--preserve-root=all` rejects any argument that is on a different file system from its parent.

  So quarantine staging is an atomic rename only when the quarantine root is on the same device as the target (`stat -c %d`). Deleting from quarantine can also be fenced to one file system.
- **Sources and quotes:**
  - S025: "mv falls back on copying as if by cp -a, then (assuming the copy succeeded) it removes the original."
  - S024: "When 'all' is specified, reject any command line argument that is not on the same file system as its parent."
- **Fills:** F4.
- **Lane link [INFERENCE, unverified]:** during the operator sweep, the staging loop hung and 2 files were missing after the timeout (LOG.md:373-378). Whether those moves crossed file systems is not known.
- **Recheck:** `stat -c '%d %n' <target> <quarantine-root>` (equal device numbers mean the rename path), and `/usr/bin/rm --help | grep -c one-file-system` (GNU coreutils 9.11: `/usr/bin/rm --version | head -1`).
- **Quality bar:** fleet floor, Q4.

---

## 5. Paths

Study orders, one per proposed frontier row:

- **F1, git-native housekeeping:** S002 → S001 → S009 → S003 → S004 → S010 → S011. The docs give intent and defaults; the tagged source shows what actually runs on `--auto`; worktree gives the lock and porcelain controls; repack gives object-level holds; release notes and BreakingChanges track drift.
- **F3, duplicate verdicts:** S017 → S016 → S019 → S018 → S020 → S021. Start with the failure list before any tool. Then rmlint's model for tagging originals, then the fdupes/jdupes caveats. End with fclones' split between report and action, and the code that rechecks at act time.
- **F4/F5, safe removal:** S029 → S022 → S023 → S025 → S024 → S026 → S027 → S028. Why soft deletion and how long to wait; a restorable format; a compliant CLI; what staging and deletion do at the file-system level; shell-level hazards; the reference wrong-target incident.

## 6. Rejected candidates

1. **git filter-branch and BFG as cleanup techniques.** History rewriting is refused (PROVINCE.md:28). Git's own docs warn against filter-branch (opened; git-filter-branch(1) § WARNING): "has a plethora of pitfalls". BFG was not opened.
2. **Monthly `git gc --aggressive --prune=now`** (S030, opened). S002 contradicts it: `--prune=now` risks corruption, and `--aggressive` is "probably not worth it ... without running tailored performance benchmarks".
3. **Aliasing `rm` to `trash-put`.** The S023 FAQ says "You can but you shouldn't", because the semantics differ: trash-put removes directories without needing `-R`.
4. **Hash-only duplicate matching as a souji receipt** (jdupes `-Q`; rmlint with MD5 and without paranoid mode). S018 and S017 show the risk of collisions and data loss.
5. **czkawka's similarity finders** (README opened; it matches similar images, videos and music). Similarity is not identity, so it cannot back a receipt.
6. **shred, secure erase, NIST SP 800-88.** These do the opposite of quarantine: they make removal irreversible. S024 notes that content removed with `rm` is "usually possible to recover". Erasing credential-bearing data is kagi's domain. NIST was not opened.
7. **GitHub Engineering, "Scaling Git's garbage collection"** (cruft packs; opened). Redundant with S002 NOTES at the current depth. Revisit only if object pruning ever enters scope; it does not today.
8. **GitHub Blog, "Highlights from Git 2.54"** (opened). Redundant with S010, and B tier.
9. **rdfind README** (opened). At this depth it adds no safety mechanism beyond the self-deletion trap S017 already demonstrates.
10. **Toy Story 2 `rm -rf` anecdote.** Not opened. Only C-tier retellings exist, with no primary record.

---

## 7. Mistakes mined (external failures mapped to lane classes) and proposed criteria

**M1 — Symlink traversal**
- External failure: fdupes deletes through a symlinked directory (S017 § Symlinks). Trash spec says .Trash must not be a symlink (S022 § 5).
- Lane analogue: r5 symlink false-SAFE (lessons/round-5.md:9-13). r10 C2-Q1, the symlinked quarantine root (census/round-10/S06-cluster-C-member2.md:53-63).
- Already captured? Partly. SKILL.md has `symlink-present` for digest scopes only (`grep -cE 'quarantine-root|symlink' SKILL.md` → 2: lines 17, 22). Quarantine-root containment lives only in the tools.
- Proposed rule: every path component a removal writes through gets an lstat check, not just digest scopes.

**M2 — Time of check to time of use (TOCTTOU)**
- External failure: jdupes `-t` (S018); fclones `modified_before` (S021).
- Lane analogue: r10 G2, a fresh child inside an aged container was DELETED (census/round-10/S13-fragment.md:66-73). r9 delete-after-revoke (lessons/round-9.md:10).
- Already captured? Partly. SKILL.md:46 re-runs the receipt. There is no rule at descendant level (`grep -c descendant SKILL.md` → 0).
- Proposed rule: at staging, the second check pins each descendant's length, mtime and digest, and aborts if any drifts.

**M3 — Odd filename bytes**
- External failure: rmlint Cautions § Unusual Characters (S017). Git provides NUL-delimited formats (S003 `-z`, S005 `-z`).
- Lane analogue: r9 rows spliced with tabs read as SAFE; authorization forged through NUL bytes in a list (lessons/round-9.md:10-12).
- Already captured? No in SKILL.md (`grep -cE 'NUL|-z\b' SKILL.md` → 0). Captured in the tools since r10.
- Proposed rule: paths travel NUL-delimited end to end; human-readable output formats are never parsed.

**M4 — Nested repositories**
- External failure: `git clean` needs a second `-f` for nested repos (S007).
- Lane analogue: r9, nested dirty or unpushed repos deleted on the strength of an ancestor's receipt (lessons/round-9.md:12-13).
- Already captured? No (`grep -c nested SKILL.md` → 0).
- Proposed rule: a nested `.git` under a target is its own receipt scope and never inherits the ancestor's receipt.

**M5 — Hidden writes during read-only checks**
- External failure: `git status` refreshes the index (S006); `filter-repo --analyze` writes `.git/filter-repo/` (S012).
- Lane analogue: r9 read-only contract violation, index rewrites (lessons/round-9.md:15-16).
- Already captured? In the tools (4/4), not in SKILL.md (0; section 1).
- Proposed rule: read-only checks run with `GIT_OPTIONAL_LOCKS=0`; history analyzers run only on `--no-local` clones.

**M6 — An empty variable expands to /**
- External failure: Steam #3671, documented in SC2115 (S027). The Bumblebee `/usr` case is SC2114.
- Lane analogue: the lane's recorded shellcheck gates use `-S error` in 8 of 10 invocations (`bash -c "grep -rhoE 'shellcheck( -[a-zA-Z]+( [a-z]+)?)*' --include='*.md' --include='*.json' . | sort | uniq -c"`; e.g. census/round-10/S02-cluster-A.md:19). Both SC2115 and SC2114 are warnings, so `-S error` hides them: `printf '#!/bin/bash\nrm -rf "$X/"*\n' | shellcheck -S error -` exits 0 with no findings, and the default severity reports `warning … [SC2115]`.
- Already captured? No.
- Proposed rule: removal scripts pass at least `shellcheck -S warning -i SC2115,SC2114` (or the full warning set).

**M7 — Wrong target or over-broad scope**
- External failure: GitLab ran the wipe on the primary (S028). filter-repo's fresh-clone check catches running in the wrong directory (S012 § FRESH CLONE).
- Lane analogue: in the operator sweep, `git add -A` pulled 10 live `.scratch` outputs and the in-flight r11 report into e20f4fa, which then took two corrective commits (LOG.md:380-382).
- Already captured? No (`grep -cE 'add -A|pathspec' SKILL.md` → 0).
- Proposed rule: quarantine commits stage exactly the approved pathspec list (`git commit -- <paths>` or `--pathspec-from-file`), never `-A`.

**M8 — Git maintenance as a deleter with no receipt**
- External failure: S001 and S009 (C1).
- Lane analogue: latent. The quarantine commit runs `git commit` (SKILL.md:44).
- Already captured? No. Installed tools have 0 guards. Only the draft `souji-census.impl-46.sh:111` had `-c maintenance.auto=false`.
- Proposed rule: hygiene commits run with `-c maintenance.auto=false`, and pinned registrations carry `git worktree lock --reason`.

**Proposed seed criteria for `corpus/QUALITY.md`.** Per LEARNING.md:54-58, each criterion must cite the lesson behind it.

- **Q1 — Version-pinned.** A claim about tool behavior names the version it was verified on and the host's version. Lesson: "linked-worktree HEADs making unique=0 wrong on git 2.55" (lessons/round-9.md:14). Precedent: the maintenance default changed between 2.53 and 2.54 (S009).
- **Q2 — Code at a tag beats prose.** Where docs are silent about what actually runs, cite tagged source. Lesson: "installed behavior wins over this prose; r6 reconciliation" (SKILL.md:14-15).
- **Q3 — Paired with a failure.** An entry on a deletion mechanism cites at least one documented failure case. Lesson: the r5 symlink false-SAFE (lessons/round-5.md:9-13).
- **Q4 — Fixture-falsifiable.** The recheck is a fixture command under `/var/tmp`, never a live fleet path. Lessons: the /tmp quota corrupted fixture runs (lessons/round-8.md:24-25); the r10 fixture policy (census/round-10/S06-cluster-C-member2.md:3-4).

**Proposed frontier rows** for `corpus/README.md ## Frontier` and the PROVINCE Frontier. These rows do not exist yet; an index row is a claim, so each should be created together with its first admitted entry.

- **F1** — git-native housekeeping vs receipts (C1, C2)
- **F2** — repository size census (C3)
- **F3** — duplicate verdicts (C4)
- **F4** — restorable quarantine format and file-system semantics (C5, C6, C2)
- **F5** — deletion-safety engineering (M6, M7)

## 8. Defects observed in passing (for the STATE peer; nothing touched)

- **D1** — `corpus/QUALITY.md` is missing (`test -e` → rc 1). CORPUS.md:12 requires it.
- **D2** — `corpus/README.md` has no coverage map and no `## Frontier` (0). Its Known gaps are stale: :22 says "No census data yet (r1)" and :23 says "No gate tool yet (r2)", while 11 lessons exist.
- **D3** — PROVINCE.md uses Owns/Work surfaces/Refuses/Adjacency (:6, :19, :26, :38) rather than Core/Frontier/Adjacent (LEARNING.md:68-70).
- **D4** — Root strays: `err4.nl2` and `err4.z2` (67 B each) and `.ufo-reports-placeholder` (0 B) (`stat -c '%n %s' err4.nl2 err4.z2 .ufo-reports-placeholder`).
- **D5** — `tools/` holds 120 files, 61 of them `cand-*` and 47 `*impl*` (`ls tools | wc -l`; `ls tools | grep -c '^cand-'`; `ls tools | grep -c impl`). The hygiene lane carries its own debris from earlier candidate rounds.
- **D6** — Defect in the fleet's draft SOURCES.md contract: the example row `|S001|…` has no spaces, but the counting regex `^\| S[0-9]{3} ` needs one, so the example counts as 0:
  - `printf '|S001|x|docs|A|t|queued|2026-10-19|90d|—|\n' | grep -cE '^\| S[0-9]{3} '` → 0
  - the spaced form → 1

  Wave 2 should either standardize on `| S001 |` or change the regex to `^\| ?S[0-9]{3} ?\|`.
- **D7** — The gd2d worktree lock state is ambiguous. SKILL.md:99-101 says "PINNED (locks held …)"; LOG.md:134-136 says "locked … pruned … unlocked". Unlocked registrations are exposed to C1. The STATE peer could check with `git -C game-dev-2d-shokunin worktree list --porcelain | grep -c '^locked'`; I did not run it, as it is outside my read scope.

## 9. Remaining unknowns

- **C1, end to end.** It has not been run as a fixture; it is source-derived. The commit-loss consequence for detached registrations is [INFERENCE].
- **C3.** Whether `git repo structure` takes locks or writes anything is not verified.
- **C6.** The cross-file-system link to the hang during the operator sweep is unverified.
- **Lane shellcheck coverage.** I did not run `shellcheck -S warning` on the installed tools, as they are outside the ART read scope. The STATE peer should count SC2115/SC2114 hits there.
- **Version history.** I did not trace the exact release that added `worktree-prune`/`rerere-gc` beyond RelNotes 2.50.0:65-66, which says gc clean-up tasks were made available to maintenance.
