# kaika W3 — non-author verification: souji round 12

Reviewer: W3ReviewSouji (fresh orchestrator-dispatched reviewer; not a lane seat).
Lane: souji-shokunin, branch `kaika/round`, base `dcc8b9e83`, round commits `d7266c5` (work) and `de9187e` (records measured commit). Reviewed read-only; scratch was under `/tmp/kaika-verify/souji/` and is deleted after this file.

## Recommendation

**HOLD. Do not record round 12 as verified.** Three blockers:

1. `sources-census.sh validate` exits **1** (E09 on S030), not 0. Contract v1 says recheck is an ISO date or cadence; S030 has `—`.
2. K5 (`quarantine-same-filesystem-rename.md`) is admitted under Q15, and Q15's only lesson pointer is the K5 admission row itself. LEARNING.md names that pattern as a harm.
3. The K5 Gate row says "the pasteable recheck line is the committed fixture." No committed K5 fixture exists, and the K5 body says "scratch-only script, not committed."

What reproduces: provenance, credential sweep, C1 counts, C2 counts, C3 gate, and the K1–K4 rechecks. The K5 behaviour reproduces, but the admission basis does not hold.

Suggested disposition: admit K1, K3, K4 (K2 after its recheck is fixed); hold K5; fix S030's recheck cell; ground or drop Q15; record C1 as a count, not a calibration gain; record C2's census as failing until the validator exits 0.

## 1. Provenance — PASS

Command: `git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' dcc8b9e83..de9187eed`

```
de9187e souji-shokunin <souji@shokunin.local> | souji-shokunin <souji@shokunin.local> | round-12: record measured commit d7266c5 ...
d7266c5 souji-shokunin <souji@shokunin.local> | souji-shokunin <souji@shokunin.local> | round-12: QUALITY bar + mistakes ledger (C1), ...
```

Both commits have the lane identity as author and committer. The lane has no upstream (`git rev-parse --abbrev-ref @{u}` → "no upstream configured"), which is consistent with "No push."

## 2. Append-only — PASS for the named scope; out-of-scope in-place edits found

Command: `git diff dcc8b9e83..de9187eed -- LOG.md corpus/lessons corpus/QUALITY.md | grep -cE '^-[^-]'` → **0**.

- `LOG.md`: one hunk, `@@ -451,0 +452,50 @@`, pure insertion at EOF (base line 451 is the last line).
- `corpus/lessons/round-12.md`, `corpus/QUALITY.md`, `corpus/SOURCES.md`, and `corpus/knowledge/*` are new files (`git cat-file -e dcc8b9e83:<path>` → absent).

Deleted or modified prior lines outside the named scope (all found with `git diff -U0 dcc8b9e83..de9187eed | grep -nE '^-'`). Section 6.4 of the round prompt requires corrections as appended text, never rewrites.

- `SCORECARD.md:13-15` — the three axis rows (coverage, calibration, operability) were replaced. Their prior evidence (for example "21/21 metadata prunes executed with receipts (lore 20→1, gd2d 6→4 …)") was condensed to "Prior: r3 C1, …" stubs. The original text survives in LOG.md, so no evidence is lost, but the row was rewritten.
- `SKILL.md:44` — one line rewritten in place: "…quarantine is a normal commit in the owning repo." became "…made with the guarded form in the Pre-quarantine checklist."
- `corpus/README.md:13, 18, 22, 23` — four lines edited in place by suffix, for example "(census tables land here from r1 onward) — wrong; corrected r12 below." Content is kept and the correction is explicit, but the form is an in-place edit.
- `SHONEN.md` — four `[ ]` lines became `[~]` with evidence lines. This is an allowed status change.
- `SKILL.md` additions: 1,625 bytes. `wc -c` gives 6,985 at base and 8,610 at head, which is +23%. Section 6.4 says "do not bloat SKILL.md."

`corpus/SOURCES.md`: new file, so the only in-place changes are the rows' own status, which is trivially satisfied.

## 3. Claims — re-run at de9187e (head copy in scratch) and at dcc8b9e (base)

**C1 calibration: verified as counted; not demonstrated as calibration.**

- Before: `census/round-12/mistakes.md` does not exist at dcc8b9e (it was added in d7266c5). The only before-state is the scribe table at de9187e. Command: `sed 's/\\|/%7C/g' <file> | awk -F'|' '/^\| M[0-9]+ \| (defect|process|honest-stop|caught) \|/{n++; if ($6 !~ /^[[:space:]]*none/) c++} END{print c"/"n}'` gives **28/52** (matches).
- After: same command on `corpus/lessons/round-12.md` at de9187e gives **51/53** (matches). Rows with `none`: M27 and M39 (matches).
- Dangling `QUALITY.md Q<n>` pointers: none (command from the Gate section; prints nothing).
- Concern: the AFTER column is the lane's own captured-by mapping. The lesson Gate says "the L1 changed the captured-by cell of 22 of the 24 rows that were `none`." The mapping was written after the criteria were. Two examples of mapping without capture: M43 → Q8, and `grep -c timeout tools/souji-quarantine.sh` → **0** at de9187e. The Q8 test (`grep -nE 'timeout [0-9]+[smh]? .*(mv\|sha256sum)'`) therefore cannot pass. M32 is also mapped only partially, per its own cell.

**C2 coverage + sources capability: counts verified; the "census runs clean" capability row is not verified.**

- Knowledge entries with three headers: `for f in corpus/knowledge/*.md; do head -3 "$f" | grep -cE '^(source|verified-at|recheck):'; done | grep -c '^3$'` → **5** (base: 0 files). Matches.
- Frontier rows holding an entry: `grep -cE '^\| F[0-9] .*\| frontier, entr' corpus/README.md` → **3** (base: no README coverage map). Matches.
- SOURCES rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **33** (base: file absent). Tiers A=29 B=3 C=1; status mined=18 queued=13 rejected=2. Matches.
- Contract census commands (rows, malformed NF≠13, duplicates, enum, tier inflation, mined used-by): all silent or as stated. The contract's command set is clean.
- Registered validator: `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate <lane>` → **exit 1**, output `souji-shokunin	E09	S030 recheck=—`. Reproduced at the live worktree and at the de9187e archive. See §4.

**C3 operability: verified.**

- Gate registered: `tests/fixtures/r12-maintenance-guard.sh` absent at dcc8b9e, present at de9187e.
- `bash tests/fixtures/r12-maintenance-guard.sh --selftest; echo $?` → `selftest=PASS ids=6/6`, exit **0**. Run in my check: 6 of 6 `verdict=PASS` lines, exit 0. Expected before/after per case match the header.
- Guard rows: `grep -cE 'maintenance\.auto=false|rev-parse --show-toplevel|worktree lock --reason' SKILL.md` → **0** (base) → **3** (head). Matches.
- Q4 test on the fixture: `grep -c 'TMPDIR:-/tmp'` → 0; `grep -c '/var/tmp'` → 3; `trap` count 4. Write scope is `mktemp -d /var/tmp/souji-r12-maintenance.XXXXXX` (fixture line 68).
- `shellcheck -S warning tests/fixtures/r12-maintenance-guard.sh; echo $?` → **0**.

## 4. SOURCES — validate fails; rows re-opened

**Command:** `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/souji-shokunin; echo $?`

```
souji-shokunin	E09	S030 recheck=—
1
```

Tool state: `fleet-census/scripts/sources-census.sh` is **untracked** (`git status`: `?? scripts/sources-census.sh`). Its sha256 is `7ce0d9bb…2c5d2`. Its mtime is 2026-10-19 19:30:43 -0300. My first validate run, about 25 minutes earlier, exited **0** with `ok` and gawk "backslash not last character" warnings on stderr. The tool was rewritten between my runs (by a sibling, per the roster), so the exit-0 version cannot be pinned. The **current** tool is the one I score. The current tool's E09 rule is `recheck !~ /^[0-9]+d$/ && !symbolic(recheck)`, which is consistent with the frozen contract. Frozen contract, Registry field `recheck`: "ISO date or cadence (`90d`, `180d`, `on-release`)." S030 has `—`, so it is non-conforming under either reading.

Rows re-opened (URL, anchor, quote):

| row | tier | check | result |
|---|---|---|---|
| S001 git-maintenance(1) | A | installed `zcat /usr/share/man/man1/git-maintenance.1.gz`, line 591 | "removes worktrees that cannot be located anymore" — matches; line 595 "This is the default strategy for manual maintenance" — matches |
| S009 git/git v2.55.0 builtin/gc.c | A | `curl raw.githubusercontent.com/git/git/v2.55.0/builtin/gc.c`, lines 1970–1975 | `strategy = geometric_strategy;` and `type = MAINTENANCE_TYPE_MANUAL;` — match (gate quote is 1974–1975) |
| S009 worktree.c | A | v2.55.0 worktree.c, lines 954–956, 1001–1008 | `if (file_exists(file.buf)) { goto done;` (locked skip) and `if (stat(file.buf, &st) || st.st_mtime <= expire) {` — match |
| S009 commit.c | A | v2.55.0 commit.c:1965 | `run_auto_maintenance(the_repository, quiet);` — match |
| S010 RelNotes | A | raw v2.54.0 `Documentation/RelNotes/2.54.0.adoc` line 58 | `* "git maintenance" starts using the "geometric" strategy by default.` — match |
| S022 FreeDesktop Trash 1.0 | A | live spec (fetched 2026-10-19) | "Publication Date: 2014-01-02, Version: 1.0" — match; "MUST check that this directory is not a symbolic link" (§5) — match; "must not overwrite a previous copy" (§6) — match |
| S025 coreutils mv | A | live gnu.org **timed out**; offline `info coreutils` | "‘mv’ falls back on copying as if by ‘cp -a’, then" — match (offline; live fetch not possible) |
| S005 git-repo(1) | A | installed `git-repo.1.gz` line 44 | "THIS COMMAND IS EXPERIMENTAL" — match |
| S016 rmlint 1.rst | A | live master | "WILL NOT DELETE ANY FILES" — count 1 — match |
| S030 OneNine (rejected) | C | live page (fetched) | "running `git gc --aggressive --prune=now` on a monthly basis" — match; filter-branch offered for simpler tasks — match. **Anchor wrong**: the page is dated "January 5, 2025" but the row says "(no date stamp)" |
| S032 git-filter-branch (rejected) | A | installed man line 46 | "has a plethora of pitfalls … its use is not recommended" — match |
| S031 own-work | A | `tests/results/r12-maintenance-guard.txt` lines 2, 4, 11–16, 31–40 | content matches; **timestamp** wrong: row says "generated 2026-10-19T21:53:39Z", file header says `# generated: 2026-10-19T22:22:41Z` |

## 5. Discernment spot-check (LEARNING.md)

| item | gate verdict | my verdict | reason |
|---|---|---|---|
| K1 `git-auto-maintenance-prunes-worktrees` | admit | **agree** | v2.55.0 source lines match (§4). `grep -cE 'strategy = geometric_strategy;\|"3\.months\.ago"'` on v2.55.0 gc.c → **2**. Fixture reproduces 2→1. The failure case is seat-reported and tagged [INFERENCE] in the entry; Q3's literal test passes. |
| K5 `quarantine-same-filesystem-rename` | admit (Q15) | **disagree (hold)** | Behaviour reproduces (below). But the admission rests on Q15, which has no mined lesson (§6). The Gate says the recheck line "is the committed fixture," which is false (§6). |
| ART C3 size census `size-census-git-repo-structure` | reject (defer) | **agree** | `zcat git-repo.1.gz` line 44: "THIS COMMAND IS EXPERIMENTAL", and the open question (does `repo structure` take locks or write?) was not tested. The lane's "premise stale" note does not change the reject. |
| S030 OneNine | reject (row) | **agree on the verdict, disagree on the anchor** | The live page does recommend `git gc --aggressive --prune=now` monthly, and it offers filter-branch. The row's "no date stamp" is wrong: the page is dated January 5, 2025. |

Two admits and two rejects were sampled, which meets the ≥1 admit / ≥1 reject rule. The K5 K-admit reproduction, with the scratch commands in §6, is the behaviour evidence for the disagreement.

## 6. New knowledge entries — headers and rechecks

Headers: all five have `source:`, `verified-at:`, `recheck:` (`head -3 … | grep -cE` → 3 each).

| entry | recheck run (command) | result | claim vs source |
|---|---|---|---|
| K1 | `curl …/v2.55.0/builtin/gc.c \| grep -cE 'strategy = geometric_strategy;\|"3\.months\.ago"'` | **2** (expect 2) | matches §4 |
| K2 | `man git-gc \| grep -nE '2.weeks\|3.months\|90 days\|30 days\|60 days\|15 days'` | **defect**: "90 days" is wrapped as "90  days" (double space) and never matches (man line 223). The 90-day default is correct; the recheck is blind to it. | 2 weeks (line 205), 3 months (215), 30 (230), 60 (274), 15 (279) — match |
| K3 | `curl fclones v0.35.0 dedupe.rs/main.rs` + `rmlint master` greps | **1 1 1** (expect 1 1 1) | dedupe.rs:843–847 "Bail out as well if any file has been modified…" — match (I read lines 814–847 at v0.35.0); main.rs:184–185 — match |
| K4 | spec-text grep script (fetched live) | all six lines **1** | matches §4 |
| K5 | GNU mv 9.11 in scratch: `renameat2 … = 0` count 1; `EXDEV` count 2; `mv --no-copy` exit **1** with "Invalid cross-device link"; `rm --help` flag count 2 | all as expected | the behaviour is correct. Its committed-fixture claim is not (§6, below). |

Scratch for K5 used `/tmp/kaika-verify/souji/k5/…` (device 57) and `/dev/shm/souji-k5-…` (device 33). Both were removed by trap, and no residue is left (`ls /var/tmp/souji-k5-* /dev/shm/souji-k5-*` → 0).

**Q15 lesson pointer.** QUALITY.md Q15 cites "corpus/lessons/round-12.md `## Gate` (K5 row: written when K5 needed a second device; flagged for the non-author spot-check)." That pointer is the admission itself, not a mined class from `## Mistakes`. LEARNING.md's quality rule: a criterion "is added with no lesson behind it" is a harm. Q15 is the only criterion whose lesson pointer is a knowledge admission.

**Committed-fixture claim.** The Gate row for ART C6 → K5 says: "the pasteable recheck line is the committed fixture." K5's own body says: "FIXTURE (scratch-only script, not committed; `recheck:` is its self-contained equivalent)." Command: `git -C <lane> grep -n -e 'souji-k5' -e '/dev/shm' de9187e -- tests` → no output. The only committed fixture is `tests/fixtures/r12-maintenance-guard.sh`.

## 7. Credentials — PASS

Command: `git -C <lane> diff dcc8b9e83..de9187eed | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1).

## 8. Report — conformant with template §4; findings

Report path: `fleet-ledger/.ufo/reports/round-12/souji.md`. Sections present: Work performed, Landed changes, Before → after, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. Cites `d7266c5` and `de9187e`. `[x]` count: `grep -c '\[x\]' souji.md` → **0**. SHONEN boxes are `[~]` with pointers that resolve: `SKILL.md:28` (Decision tables), `:60` (Error patterns), `:85` (Checklists), `LOG.md:362` (operator sweep entry).

Report-content defects:

- The report's "Before → after" C2 line says "contract census clean"; the registered validator exits 1 (§4). The capability row in SCORECARD says "contract v1 census runs clean." Both should name the E09 finding until fixed.
- "Expansion … uncovered ground": F1/F3/F4 were created in this round (PROVINCE.md:47 onward and README coverage map), so "uncovered" is true at base by construction. The narrow sibling sweep I ran (grep for 9 F1/F3/F4 terms across `*-shokunin/PROVINCE.md` and `SKILL.md`) found only the souji lane itself. That supports "uncontested" but is not the full connector sweep.
- Integrator note on the fleet root is **stale**: `git -C /home/vgpnk/Projects/shokunin reflog -8` shows the top entry "reset: moving to 31baf5c"; `git status --short` at the fleet root shows only ` M LOG.md`; no untracked strays are listed. The four throwaway commits and the stray files appear already repaired (commits recoverable from reflog until expiry). The `M LOG.md` at the fleet root is not from this lane's commits and is not mine to judge.

## 9. Trend verdicts (LEARNING.md)

- **Expansion: improved (conditional).** Evidence: K1–K4 are admitted entries on F1/F3/F4 (base: zero entries and no coverage map; §3 C2 counts). Condition: K5 is held. Without K5, four entries.
- **Quality: unchanged (strict reading).** LEARNING's improved condition needs a weaker entry superseded or a stale entry re-verified. This round has no prior entries to supersede. K1–K4 rechecks run and reproduce (K2's recheck is blind to one claim). No admitted entry is false. The bar was created, but it has not yet been tested against a counterexample.
- **Discernment: harmed, pending fix.** The Q15 criterion has no mined lesson behind it, and K5 was admitted under it. LEARNING names this as harm. The sampled admits and rejects otherwise agree (§5). The S030 anchor error is a record-accuracy defect, not a gate error.

## 10. Per-axis recommendations (lane axes: calibration, operability, coverage)

- **calibration (7):** verdict "improved" is supported only as a mapped-criteria count (28/52 → 51/53, §3). Recommend: score stays 7. Record as "count verified; no demonstrated catch." M43 (mapped to an unenforced Q8) and M32 (partial) should not count as captured.
- **operability (8):** verified. Gate exit 0; selftest 6/6; shellcheck 0; SKILL guard rows 0 → 3. Score stays 8 with delta 0, as the lane writes. The "improved" label with delta 0 needs an operator ruling under AXES.md.
- **coverage (8):** counts verified; capability row not verified until `validate` exits 0. Recommend: hold the coverage "improved" verdict until S030's recheck is fixed and K5 is resolved.

## Defects, by severity

**Blocking**
1. `sources-census.sh validate` → exit 1, E09 on S030 (`recheck=—`), against frozen contract v1 Registry `recheck`. Fix: set S030 `recheck` to a conforming cadence (for example `365d` or `on-release`). Evidence: §4.
2. K5 is admitted under Q15, and Q15's lesson pointer is the K5 admission itself. LEARNING harm: "a criterion is added with no lesson behind it." Fix: ground Q15 in a mined class in `## Mistakes`, or drop it and hold K5. Evidence: §6.
3. K5 Gate: "the pasteable recheck line is the committed fixture" is false; no committed K5 fixture exists. Fix: correct the Gate sentence or commit the fixture (under `/var/tmp` plus the Q15 second device). Evidence: §6.

**Major**
4. C1 AFTER count is self-assigned: the L1 changed 22 of 24 `none` cells, and M43 is mapped to Q8 whose tool test fails (`grep -c timeout tools/souji-quarantine.sh` → 0). Record as "count verified, not calibration." Evidence: §3 C1.
5. Append-only form violated outside the named scope: `SCORECARD.md:13-15` (three axis rows replaced, prior evidence condensed); `SKILL.md:44` (line rewritten); `corpus/README.md:13,18,22,23` (lines edited in place). Fix: restore as appended corrections, or record as an accepted exception. Evidence: §2.

**Minor**
6. S030 anchor says "(no date stamp)"; the live page is dated January 5, 2025.
7. S031 timestamp: row says `21:53:39Z`, file says `22:22:41Z`.
8. K2 recheck is blind to the 90-day reflog default because man wraps "90  days" with a double space. Fix: `grep -E '90 +days'`.
9. SKILL.md grew 6,985 → 8,610 bytes (+23%). Section 6.4 says "do not bloat SKILL.md." The new error-pattern paragraph restates K1's facts; fold only the durable row plus a pointer.
10. SCORECARD capability row "contract v1 census runs clean": true for the contract's command set, false for the registered validator (E09). Name the finding.

**Integrator (not the lane)**
11. `fleet-census/scripts/sources-census.sh` is untracked and was rewritten during this review (sha256 `7ce0d9bb…2c5d2`, mtime 2026-10-19 19:30:43 -0300). Commit it or pin its sha256 before anyone else relies on `validate`. The earlier exit-0 run used a version I cannot reproduce, and the earlier run also printed a gawk warning on stderr.
12. S025 live fetch (gnu.org) timed out during this review. The quote was checked offline (`info coreutils`) instead.

## Admit / reject recommendation (per item)

| item | recommendation |
|---|---|
| K1 | admit |
| K2 | admit after recheck fix (defect 8) |
| K3 | admit |
| K4 | admit |
| K5 | **hold** (blockers 2, 3) |
| Q15 | **reject as written** unless grounded in a mined class |
| C3 size-census reject | stands |
| S030 reject row | keep rejected; fix recheck (blocker 1) and anchor (defect 6) |
| S032 reject row | keep rejected |
| C1 | record as counted |
| C2 | hold until `validate` exits 0 |
| C3 | verified |

## Verification gaps

- The census validator is untracked and changed during the review. My results are for the current version (sha256 `7ce0d9bb…2c5d2`) only.
- The lane's internal re-derivation seats (R12PostReviewer, R12PostCritic, the labrat) are the lane, and I did not re-run their outputs.
- The connector sweep for F1/F3/F4 was only partly re-run (narrow grep; §8).
- Live gnu.org fetch for S025 timed out; the quote was checked offline.
- Scratch was used only under `/tmp/kaika-verify/souji/`. The K5 recheck used the `/tmp` and `/dev/shm` device pair, and both were removed by trap.
