# verify2 — step-1 closure verification, seven lane reports (rounds terminating 19:13–19:50, 2026-09-28)

Scope: Main repo `/home/vgpnk/projects/shokunin` (branch `master`) + nested child repos.
Read-only throughout (no writes under /home/vgpnk/projects). All values re-executed at ~19:50–19:52 -03.
PROTOCOL clauses used (main repo `PROTOCOL.md`):
- L88,116: child-lane prompts carry `commit-before-report ordering`; *"A lane report lands last — written only after the lane's child-repo work is committed, and it must cite the commit hash… a report naming a hash the repo does not contain fails verification"*.
- L265–273: closure checks *"each report for the contract-required `SHONEN` heading"*; *"A report that violates the report contract (missing heading, dead or orphaned hash, report filed before its commit) … is recorded as a conformance defect"*.
- L430–437: *"paths under `tmpfs` (`/tmp`, `/dev/shm`), session-scoped `local://` artifacts … are not evidence"*.

## 0. Live repo state observed during this pass (changed mid-session)

```
$ git -C /home/vgpnk/projects/shokunin log -1 --format='%h %cI %s'
f9dcfd2 2026-09-28T19:47:54-03:00 round-11 kotoba report: … (filed late by the round-12 respawn; lane commit 4dd7753)
```
Main HEAD advanced from `9af7245` (observed at pass start) to `f9dcfd2` during the pass.
`kasegi round=13` complete line was pending at pass start and landed mid-pass:
```
$ grep -n kasegi .ufo/watchdog.log | tail -3
178:2026-09-28T19:50:42-03:00 complete kasegi round=13; respawning
179:2026-09-28T19:50:43-03:00 launch kasegi round=14 runId=shokunin-r14-kasegi-r1790635842
```
Watchdog complete lines (quoted by timestamp): kake r11 `19:13:04` · kagi r10 `19:13:05` · kumitate r9 `19:20:36` · aggregator r6 `19:35:38` · kotoba r11 `19:35:39` · kake r12 `19:43:10` · kasegi r13 `19:50:42`.

Repos probed: `/home/vgpnk/projects/shokunin` + 6 children; `/home/vgpnk/Projects/{bounties, webzites/repos/ufo-fsd-alpha, webzites/repos/llm-wiki, origin-work/ufo-fsd-alpha, origin-work/charter-ufo-fsd, ds4cc-marketplace}`. (`webzites` top level is not a git repo: `git -C /home/vgpnk/Projects/webzites rev-parse --is-inside-work-tree` → `fatal: not a git repository`.)

## 1. Seven rows

| # | Report | exists/size | mtime | `grep -cE '^#{1,6} *SHONEN'` | hex tokens | marker-vs-report verdict | main-repo file status | /tmp–local:// evidence pointers | report mtime vs cited/own commit |
|---|---|---|---|---|---|---|---|---|---|
| 1 | round-11/kake.md | yes / 5504 B | 19:11:16.046 | **0 (MISSING)** | 440e3cba,5a80ee93,abf822c7,8c5bb8ca — all sha256 content pins (non-commit) | names real changes ✓; **no commit-hash citation** (says "Commit `round-11`") | tracked, added by `78bd39b` | `/tmp/kake-r11/scout-verbs.md`, `/tmp/kake-r11/` | report 19:11:16 **< own lane commit 0262681 19:11:24 (−8 s)** ⇒ filed before its commit |
| 2 | round-10/kagi.md | yes / 7178 B | 19:09:01.961 | **0 (MISSING)** | 2586de87081a,f8114ee44b15,c84939050de8,8d57f3cd — sha256 pins (non-commit); first 3 verified exact | real changes ✓; evidence pins verified; **no hash citation** ("Branch/commit: `round-10`") | tracked, added by `ade32e4` | none | report 19:09:01 **< own lane commit 03477c0 19:09:31 (−30 s)** ⇒ filed before its commit |
| 3 | round-9/kumitate.md | yes / 10464 B | 19:15:14.990 | **0 (MISSING)** | 0ac2272,31f09cd,d65aa24,ee907f1cf (commits, ancestors ✓); 86bdcd9a,8ed7ef0a, + two 64-hex sha256 pins (non-commit) | ✓ real changes + resolvable cited hash `d65aa24` | **untracked** | `/tmp/kumitate-r9/spec.md` | report 19:15:14 > cited commit d65aa24 19:10:11 ⇒ ordering OK (commit-before-report) |
| 4 | round-6/aggregator.md | yes / 15931 B | 19:30:11.182 | 1 (`## SHONEN`) | 19 commits all resolve & are ancestors of HEAD (main/kake/kagi/kumitate/kotoba/kengaku/kasegi + ufo-fsd-alpha); non-commits: 1790629072 (runId), deadbeef0000 & a318e719a04b (synthetic drift-pin digest pair) | ✓ real changes + resolvable hash `e333e7c` | **untracked** | none | report 19:30:11 > cited commit e333e7c 19:28:15 ⇒ ordering OK |
| 5 | round-11/kotoba.md | yes / 12397 B | 19:47:11.283 | 1 (`## SHONEN`, supplied late) | 3b029b8,4dd7753,abef8aa,d49dfa5,7a4c9a0,ea77bf0 (commits, ancestors ✓); 143fe473(md5),2f07179c & 631569277d(sha256 prefixes) | ✓ real changes + resolvable hash `4dd7753` | tracked, added by `f9dcfd2` | `/tmp/before-clone-r11`, `/tmp/round11`, `/tmp/notgit` (all reproducible, report says so) | report 19:47:11 > cited commit 4dd7753 19:45:58 ⇒ ordering OK |
| 6 | round-12/kake.md | yes / 15348 B | 19:42:18.923 | **0 (MISSING)** | 0262681,61d0ce6 (commits, ancestors ✓); 8c5bb8ca (sha256 prefix) | real changes ✓; **no commit-hash citation** ("hash in the round-end section below" — section gives no hash) | tracked, added by `9af7245` | `/tmp/kake-r12/{critic.md,scout-verbs3.md,revenger-patch.md,revenger-replica/,live/status-json.out,/}`, `/tmp/kake-r11/scout-verbs.md` | report 19:42:18 **< own lane commit a642f93 19:46:14 (−3 m 56 s)** ⇒ filed before its commit |
| 7 | round-13/kasegi.md | yes / 9964 B | 19:44:05.526 | **0 (MISSING)** | fc6d398,5309290 (commits, ancestors ✓); 3d28a716 (commit; ancestor of bounties `main` but **NOT** of HEAD, exit 1); **d7dbd9a UNRESOLVABLE**; ded642e8 (sha256 prefix) | real changes ✓; one cited hash **unresolvable**, one not-ancestor | tracked, added by `0933e84` | `/tmp/kasegi-r13/connector.md`, `/tmp/kasegi-r13/classify{2..5}.py`, `/tmp/kasegi-r13/` | report 19:44:05 **< own lane commit 7483333 19:44:20 (−15 s)** ⇒ filed before its commit |

## 2. Per-hash evidence (step 3)

Method: `/tmp/shokunin-r11/verify2/hexcheck.sh <tokens…>` → for each token, `git -C <repo> cat-file -t <tok>` then `merge-base --is-ancestor <tok> HEAD; echo exit=$?` across 13 repos. Tokens extracted with `grep -oE '[0-9a-f]{7,40}'` (64-hex sha256 pins surface as two fragments ≤40; recombined below).

- **round-11/kake.md** — `440e3cba`, `5a80ee93`, `abf822c7`: report: *"`liveSha256` nondeterministic per fetch (abf822c7→440e3cba→5a80ee93 — never alert on sha deltas)"* → content-hash samples, no object in any repo. `8c5bb8ca`: sentinel state sha *"sha `8c5bb8ca…` before==after"*. All 4 = non-commit content pins (correctly framed). Actual lane commit = `0262681` (not cited).
- **round-10/kagi.md** — `sha256sum` re-run: `2586de87081a…`=corpus/surface-census.sh ✓, `f8114ee44b15…`=corpus/surface-census.tsv ✓, `c84939050de8…`=corpus/state-shape.tsv ✓ (all three claimed prefixes match exactly). `8d57f3cd…` = custody record sha (on-disk artifact not present here → unverified prefix). All 4 = non-commits.
- **round-9/kumitate.md** — `0ac2272` ✗kumitate commit, ancestor exit=0; `31f09cd` ditto; `d65aa24` ✗kumitate commit = repo HEAD, ancestor exit=0; `ee907f1cf` ✗`/home/vgpnk/Projects/origin-work/ufo-fsd-alpha` ancestor exit=0. sha256 pins: `86bdcd9a…`=scripts/surface-probe.mjs ✓ (sha re-verified), `8ed7ef0a…`=md5(manifest stdout), full pins `de50bca59b159cbd77029bf6e26d1bf26762c9849fc6b89fa2fba572995fc099` and `0e98c908bb8dc52353716852b5451605ad5889c98b7bc620fceebd7797725567`. Non-commits.
- **round-6/aggregator.md** — resolvable commits (all `merge-base --is-ancestor` exit=0): main `0a30b44`,`640a4c5`,`8ec7a56`,`ade32e4`,`e333e7c`; kake `ab8c9e2`,`dd4eabf`; kagi `ad694a2`,`e64e81b`; kumitate `7a4c9a0`,`a6f9456`; kotoba `778310d`,`8e22a41`; kengaku `3175e69`,`1bd17ec`,`f147a27`; kasegi `d341b48`,`fb9ac8e`; ufo-fsd-alpha `ee907f1cf`. Non-commits: `1790629072` (runId `shokunin-r6-aggregator-r1790629072`), `deadbeef0000` + `a318e719a04b` (the falsified drift-pin test digest pair *"`DRIFT … deadbeef0000->a318e719a04b`"*).
- **round-11/kotoba.md** — `3b029b8`,`4dd7753`,`abef8aa`,`d49dfa5` ✗kotoba commits ancestor=0 (`4dd7753` = own r11 landing); `7a4c9a0` ✗kumitate = *"authored `shokunin <shokunin@local>`"* ✓ report claim; `ea77bf0` ✗kagi *"authored `shokunin <shokunin@local>`"* ✓ report claim. Non-commits: `143fe473` (md5), `2f07179c`,`631569277d` (sha256 prefixes).
- **round-12/kake.md** — `0262681` ✗kake commit (pre-land HEAD), ancestor=0; `61d0ce6` ✗`origin-work/charter-ufo-fsd` *"charter: scribe beat 2026-09-28"*, ancestor=0; `8c5bb8ca` sha256 prefix.
- **round-13/kasegi.md** — `fc6d398` ✗kasegi commit *"round-12 (late commit)…"*, ancestor=0; `5309290` ✗main commit *"kasegi round-12 report (late commit)"*, ancestor=0; `3d28a716` ✗bounties commit `3d28a71676166007ccec78fa52ad76a287501962` *"chore(fleet): periodic mission-work sync [auto]"* 2026-09-06T05:42:43-03:00 — `cat-file -t`=commit, `merge-base --is-ancestor 3d28a716 HEAD`=**1**, `… main`=0 (bounties is `* (no branch, rebasing main)`; `main` tip = 3d28a716; detached HEAD = `58acb6d8` which does not contain it); `ded642e8` sha256 prefix; **`d7dbd9a` → `fatal: Not a valid object name` in every probed repo**.

### 2a. The unresolvable hash (kasegi `d7dbd9a`) — confirmed defect

```
$ grep -n 'd7dbd9a' .ufo/reports/round-13/kasegi.md
83:  `ded642e8…`, commit d7dbd9a, CWE-78) and still returns `claim-check: OK`.
$ grep -rn 'd7dbd9a' kasegi-shokunin --include=*.md | head
kasegi-shokunin/LOG.md:197: same commit `d7dbd9a09f59775726ed14bbea8fc9dfdff62f7b`, same file
kasegi-shokunin/SKILL.md:501: `d7dbd9a`, file, sha256 `ded642e8`, CWE-78) …
$ for r in bounties the-bounty-hunter ds4cc-marketplace kasegi-shokunin; do git -C $r cat-file -t d7dbd9a09f59775726ed14bbea8fc9dfdff62f7b; done
fatal: … Not a valid object name d7dbd9a          (7-char form, each repo)
fatal: … could not get object info                 (full 40-char form, each repo)
# exhaustive: every .git under /home/vgpnk (maxdepth 4) → hits=0
```
Verdict: `d7dbd9a` / `d7dbd9a09f59775726ed14bbea8fc9dfdff62f7b` does not exist in any local object database (bounties is mid-rebase, so it may live only in the un-fetched origin). Cited as evidence ⇒ "dead or orphaned hash" conformance defect (PROTOCOL L273).

## 3. Marker-vs-report verdicts, with deciding lines

1. **kake r11** — REAL. Quote: *"Closed the r10 residual … all executed live on the real repo … Commit `round-11` in `kake-shokunin/`. 13 read-only L2 probes in ONE batch … → `/tmp/kake-r11/`"* and *"kake-shokunin: commit `round-11` + push. Main repo: this report committed + pushed."* Files named (corpus/knowledge/free-read-verbs.md, SKILL.md, SCORECARD.md, LOG.md) all present. **No resolvable commit hash cited**; report predates its own commit `0262681`. **Conformance defects: missing SHONEN heading; no hash citation; report-before-commit; /tmp evidence pointer (L430).**
2. **kagi r10** — REAL. *"Landed `corpus/surface-census.sh` v1 (868 lines) + `corpus/surface-census.tsv` (35 rows…) + `corpus/state-shape.tsv` (22 rows)…"* — all present, 868/54/48 lines, three sha256 pins verified exact. **No hash citation** (`Branch/commit: round-10`), report predates `03477c0` by 30 s. **Defects: missing SHONEN; no hash citation; report-before-commit.**
3. **kumitate r9** — REAL + ordering clean. *"**Repo commit:** `d65aa24` (`round-9`), pushed to github.com/VeigaPunk/kumitate-shokunin (`31f09cd..d65aa24`)"* — `d65aa24` resolves and is HEAD; report mtime > commit. Minor: claims surface-probe.mjs *"1438 L"*; actual `wc -l` = 1435 (worktree and the `d65aa24` blob), though `sha256` prefix `86bdcd9a…` matches. **Defects: missing SHONEN heading; untracked in main repo; /tmp evidence pointer.** (Note: aggregator r6's own report lists `round-9/kumitate.md` as a lane report left untracked — corroborated.)
4. **aggregator r6** — REAL + ordering clean. *"before-state measured at `0a30b44`, this round's work shipped in **`e333e7c`**"*; AGGREGATE.md committed blob re-checked: `git show e333e7c:… | wc -l` → 821 lines, `grep -cE '^\| D-'` → 79 — exactly the claimed *"557 → 821 lines"* / *"79 rows"*. SHONEN section present (`## SHONEN`, explains aggregator has no SHONEN.md). **Defects: untracked in main repo** (AGGREGATE.md is also currently dirty vs e333e7c, post-report edits by another writer). No /tmp pointers.
5. **kotoba r11** — REAL. *"Commit: `4dd7753` (landed by the round-12 respawn…) in `kotoba-shokunin`"* — resolves, and the report's own cross-domain identity claim re-verified (`kumitate 7a4c9a0` / `kagi ea77bf0`, both `shokunin <shokunin@local>` ✓). SHONEN supplied at filing time. **Defect: /tmp evidence pointers (self-flagged: *"Scratch state is not evidence"*); report filed 11 m 32 s after its round's `complete` line (19:35:39 → mtime 19:47:11, re-filed by the r12 respawn).** Ordering vs its cited commit OK.
6. **kake r12** — REAL but hash-less. Central finding re-verified live: `systemctl --user status webzites-keeper.timer` → *"Loaded: … disabled; preset: enabled / Active: inactive (dead) / Trigger: n/a"*, and `fleet.config.json:256` = *"marker": "2026-09-26 scribe beat"* ✓; `61d0ce6` resolves in origin-work/charter-ufo-fsd. **No commit-hash citation** (round-end section gives none); report predates its own commit `a642f93` by 3 m 56 s; 8-entry `/tmp/kake-r12/` evidence index is all tmpfs. **Defects: missing SHONEN; no hash citation; report-before-commit; /tmp evidence.**
7. **kasegi r13** — REAL but two bad pointers. Re-verified live in bounties: `ops/fleet-dispatch.mjs:200` = *"`const ev = rec.ev_inputs?.adjusted_ev;`"* ✓, `:10` comment ✓, `:107` *"`const curated = rec.ev_inputs && Object.keys(rec.ev_inputs).length > 0;`"* ✓; `ledger/telemetry.jsonl` = 7225 lines with **markers=3** ✓; `check-freshness.mjs:61` appends telemetry ✓; `triage-thresholds.md` 455 lines ✓; `fc6d398`/`5309290` resolve. **Defects: missing SHONEN heading; no hash citation for own commit (report predates `7483333` by 15 s); unresolvable hash `d7dbd9a`; `3d28a716` not an ancestor of HEAD; /tmp evidence pointers.**

## 4. Commit status in main repo (step 5)

```
$ git -C /home/vgpnk/projects/shokunin ls-files --error-unmatch <path>   # tracked / untracked
```
(Reminder: an earlier pass using a repo-root-relative pathspec while cwd=.ufo/reports produced a false "untracked"; corrected below.)

| Report | status | added by | author | add-commit cI | diff |
|---|---|---|---|---|---|
| round-11/kake.md | tracked | `78bd39b` | Joao Pedro Veiga <jpveigao10@gmail.com> | 19:11:54 | 1 file, +96 |
| round-10/kagi.md | tracked | `ade32e4` | kagi <kagi@shokunin.local> | 19:10:10 | +115 (+ `.ufo/l0-questions.md` +1, `{round-2 => }/AGGREGATE.md` rename) |
| round-9/kumitate.md | **untracked** | — | — | — | `git ls-files --others --exclude-standard` lists it |
| round-6/aggregator.md | **untracked** | — | — | — | listed by `ls-files --others …` |
| round-11/kotoba.md | tracked | `f9dcfd2` | kotoba-shokunin <kotoba@shokunin.local> | 19:47:54 | 1 file, +219 (== current main HEAD) |
| round-12/kake.md | tracked | `9af7245` | Joao Pedro Veiga <jpveigao10@gmail.com> | 19:46:14 | 1 file, +245 |
| round-13/kasegi.md | tracked | `0933e84` | Joao Pedro Veiga <jpveigao10@gmail.com> | 19:44:22 | 1 file, +158 |

Untracked set in `.ufo/reports` = {`round-10/kotoba.md`, `round-6/aggregator.md`, `round-9/kumitate.md`} — corroborates aggregator r6's claim *"Two untracked lane reports sit in the working tree and are not this lane's to commit: `.ufo/reports/round-10/kotoba.md`, `.ufo/reports/round-9/kumitate.md`"* (and adds aggregator's own).

### Answer to "which commit added kake r11 / kasegi r13, under what identity"
- `.ufo/reports/round-11/kake.md` ← **`78bd39b`** ("round-11 kake report: …"), author **Joao Pedro Veiga <jpveigao10@gmail.com>**, 2026-09-28T19:11:54-03:00 (1 file, +96).
- `.ufo/reports/round-13/kasegi.md` ← **`0933e84`** ("kasegi round-13 report: …"), author **Joao Pedro Veiga <jpveigao10@gmail.com>**, 2026-09-28T19:44:22-03:00 (1 file, +158).
Both "appear tracked" ✓ — they are, and both carry the **human/operator git identity**, not a lane identity.

## 5. Ordering (step 7) — filed-before-commit violations

| Report | mtime (epoch) | own lane commit | lane commit cI (epoch) | Δ (report − commit) | verdict |
|---|---|---|---|---|---|
| kake r11 | 19:11:16 (1790633476) | kake 0262681 | 19:11:24 (…484) | −8 s | **violation** (and no hash cited) |
| kagi r10 | 19:09:01 (1790633341) | kagi 03477c0 | 19:09:31 (…371) | −30 s | **violation** (no hash cited) |
| kumitate r9 | 19:15:14 (1790633714) | kumitate d65aa24 | 19:10:11 (…411) | +5 m 3 s | OK (cites d65aa24) |
| aggregator r6 | 19:30:11 (1790634611) | main e333e7c | 19:28:15 (1790634495) | +1 m 56 s | OK (cites e333e7c) |
| kotoba r11 | 19:47:11 (1790635631) | kotoba 4dd7753 | 19:45:58 (…558) | +1 m 13 s | OK (cites 4dd7753) |
| kake r12 | 19:42:18 (1790635338) | kake a642f93 | 19:46:14 (…574) | −3 m 56 s | **violation** (no hash cited) |
| kasegi r13 | 19:44:05 (1790635445) | kasegi 7483333 | 19:44:20 (…460) | −15 s | **violation** (no hash cited) |

All other cited child hashes predate the report mtime (e.g. kasegi's `fc6d398` 18:35:14, `5309290` 18:35:15; kake r12's `0262681` 19:11:24, `61d0ce6`). The four "violation" rows are exactly the reports that cite no commit hash at all — they each name their round ("commit `round-12`") and defer/omit the hash.

## 6. Cross-cutting observations

1. **Identity mix (corroborates kotoba r11's "fleet commit-identity class"):** child-lane commits authored `Joao Pedro Veiga <jpveigao10@gmail.com>` (kake r11/r12, kasegi r11–r13, kumitate r9) vs lane-scoped `kagi/kotoba/kengaku@shokunin.local` vs legacy `shokunin <shokunin@local>` (kotoba-reported `kumitate 7a4c9a0`, `kagi ea77bf0`). Aggregator commits use `aggregator-shokunin <aggregator@shokunin.local>`. Main-repo report commits 1/3/6/7 use the human identity; 2 and 5 use lane identities.
2. **`ade32e4` (kagi r10 report) also carried the staged `AGGREGATE.md` rename + an `.ufo/l0-questions.md` line** — directly corroborating aggregator r6's D-83: *"The rename was staged by this lane and then swept into the kagi lane's bare `git commit` `ade32e4`"* (diff stat shows `{round-2 => }/AGGREGATE.md`).
3. **`3d28a716` ancestry** is explained by the bounties repo being mid-rebase (`* (no branch, rebasing main)`; `main` tip = 3d28a716 ≤ HEAD-checkout `58acb6d8` which does not contain it) — matching kasegi r13's own *"Stalled mid-rebase state (r12 L0 question) still unresolved"*.
4. **Artifact re-checks:** kagi sha256 pins exact (3/3); kumitate sha256 prefix exact; AGGREGATE.md committed line/row counts exact (821/79); kotoba verifiers present; kasegi `triage-thresholds.md` 455 lines ✓; six `corpus/lessons/round-6-aggregator-audit.md` present in all six child repos; telegram-marker count in bounties `ledger/telemetry.jsonl` = 3 ✓ and 7225 lines ✓.

## 7. Reproduce

```
bash /tmp/shokunin-r11/verify2/hexcheck.sh <hash…>            # cat-file -t + is-ancestor across 13 repos
git -C /home/vgpnk/projects/shokunin ls-files --error-unmatch .ufo/reports/round-13/kasegi.md
git -C /home/vgpnk/projects/shokunin log --diff-filter=A --format='%h %an <%ae> %ad' --date=iso -- .ufo/reports/round-13/kasegi.md
grep -cE '^#{1,6} *SHONEN' .ufo/reports/round-13/kasegi.md
git -C /home/vgpnk/projects/shokunin show e333e7c:.ufo/reports/AGGREGATE.md | wc -l   # → 821
sha256sum kagi-shokunin/corpus/surface-census.sh | cut -c1-12                         # → 2586de87081a
```