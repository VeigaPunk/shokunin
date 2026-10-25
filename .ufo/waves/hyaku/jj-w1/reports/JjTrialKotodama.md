# JjTrialKotodama — empirical jj-colocation trial for lane `kotodama`

Seat: JjTrialKotodama-2 (leaf). Date: 2026-10-20.
Target: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (branch `main`, remote `https://github.com/VeigaPunk/kotodama-shokunin.git`, HEAD `4ad2683`).
Sandbox: `/fast/scratch/jj-wave/JjTrialKotodama/` (`remote.git` = sandbox bare remote, `lane` = colocated trial, `lane-plain` = non-jj control, `lane-autotrack` = auto-track "all()" variant, `operator` = second clone for the concurrent-push case).
Tools: jj 0.45.1 (`~/.local/bin/jj`), git 2.56.0. No installs needed or performed.
The live repo was only ever read (status/ls-files/du/find); every jj command ran with cwd inside the sandbox; the sandbox remote was verified with `git remote -v` → `/fast/scratch/jj-wave/JjTrialKotodama/remote.git` before any push.

## Step 1 — sandbox build

Commands run verbatim from the assignment. Results:

- `git clone --bare … remote.git` and `git clone … lane` both clean.
- After the rsync overlay: `git -C lane status --porcelain | wc -l` → **0** (live tree was already clean; nothing untracked, nothing modified).
- `git status --porcelain --ignored | wc -l` → **41**, all `!!`.
- 10 largest untracked-or-ignored files (all ignored, all under `reports/supplement-opencode-1/scratch/`):

  | bytes | path (suffix) |
  |---|---|
  | 135,327,186 | …/round5-06/b35683971-Gamble_R.pdf |
  | 58,797,092 | …/round8-f11/oip92.pdf |
  | 26,916,873 | …/round5-06/Oidtmann_gsas.harvard_0084L_11276.pdf |
  | 22,580,333 | …/round6-03/ritner-saoc54-4th.pdf |
  | 16,426,644 | …/round5-13/aura-korean-thesis.pdf |
  | 15,004,361 | …/src-09-slavs/primary_chronicle.pdf |
  | 15,004,361 | …/round5-04/a011458.pdf |
  | 8,098,353 | …/source-recheck-orality/gummere_djvu.xml |
  | 7,717,930 | …/round6-04/aegean_textiles_ats18.pdf |
  | 5,958,870 | …/22-label-representation/hj1903_djvu.txt |

  ≈ 311 MB of ignored payload in one ignored tree; largest tracked file is `reports/round-23/…/tie-break-check-receipt.json` at 1,037,171 bytes (just under jj's 1 MiB default max-new-file-size — borderline, see hazards).
- `.gitignore` (live, verbatim): `.ufo/state/`, `.ufo/watchdog.log`, `*.log`, `__pycache__/`, `/reports/supplement-opencode-1/scratch/`, `.scratch/`.

## Step 2 — colocate through the helper

`HYAKU_STATE=/fast/scratch/jj-wave/JjTrialKotodama/state jj-lane.sh init lane kotodama` → exit 0.

- State line: `state branch=main local=4ad26836… remote=4ad26836… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Init warnings (stderr, verbatim):
  - `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>". To change the working copy author, use "jj metaedit --update-author".` (×2 — one per `user.name`/`user.email` `config set`). Cosmetic only: the working-copy commit @ stays empty under auto-track=none and the helper's commit path runs `metaedit --update-author` under the lane identity before every commit (verified in step 4).
  - No `@ already tracks N added path(s)` warning — @ was empty.
- Repo config confirmed via `jj config list --repo`: `snapshot.auto-track = "none()"`, `user.name = "kotodama-shokunin"`, `user.email = "kotodama@shokunin.local"`, `revset-aliases."trunk()" = "main@origin"`. (`jj git init --colocate` prints `Initialized repo in "."` and hints to `jj bookmark track main@origin`; the helper's `bookmark track` already handles it — `main@origin` was tracked and `jj git push` worked without further setup.)
- `git symbolic-ref -q HEAD` → `refs/heads/main` — **HEAD attached** right after init. ✔
- `git status --porcelain | wc -l` → still **0**; `--ignored` count went 41 → 42, the sole new entry being `!! .jj/` (jj drops `.jj/.gitignore` containing `/*`; verified `git check-ignore -v .jj` → `.jj/.gitignore:1:/* .jj/`). No tracked or untracked path changed state. ✔
- `jj status` timing (3 runs, `date +%s%N` deltas, warm): **10 ms / 9 ms / 10 ms** — trivially cheap on this lane even with the 488 MB working tree, because snapshotting with auto-track=none only has to stat, not ingest.

## Step 3 — default auto-track "all()" alternative

`cp -a lane lane-autotrack` (jj warns `Your repo appears to have been copied …` — worth knowing for replication), then `jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'`.

- On the pristine tree: `jj status` → `The working copy has no changes.` — **0 files snapshotted**, snapshot+status **12 ms**. Reason: every big payload file in this lane is *ignored*, and auto-track never admits ignored files. On this lane, all() alone would have been harmless **by luck** — the lane happened to be clean at init time.
- Probed with `echo hi > scratch-untracked.txt` + 2 MiB `big-new.bin`:
  - `jj status` → `Working copy changes: A scratch-untracked.txt`; `git status --porcelain` → ` A scratch-untracked.txt` (**intent-to-add**, polluting git status and any `git diff --cached` consumer); snapshot+status **20 ms**.
  - `big-new.bin` → **new file too large refusal**, verbatim: `Warning: Refused to snapshot some files: big-new.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)`. It stays `? big-new.bin` in jj / `??` in git — refused files are left untracked, not committed.
- Conclusion matches the helper's design note: on kotodama the default all() would silently intent-to-add any seat scratch that isn't ignored; none() is required.

## Step 4 — simulated round commit via the helper

Prepared: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-jjtrial.txt` untracked.

`jj-lane.sh commit lane --as kotodama -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md` →

```
committed d3a7044d0a971a9bf22cd686894d8061999c9bba
pushed   d3a7044d0a971a9bf22cd686894d8061999c9bba   exit 0
```

Verifications (all in the sandbox lane):

- `git show -s --format='%an <%ae>%n%cn <%ce>' d3a7044d` → `kotodama-shokunin <kotodama@shokunin.local>` for **both author and committer**. The lane identity is enforced per command; operator `jpveigao10@gmail.com` never leaked. ✔
- `git log -1 --format=%H -- LOG.md` → `d3a7044d…` = pushed hash. ✔
- `git merge-base --is-ancestor d3a7044d… main` → exit 0. ✔
- `jj-lane.sh state lane` → `ahead=0 behind=0 head=detached tracked=0 untracked=1`. ✔
- `git -C remote.git log -1 --format=%H main` → `d3a7044d…` — remote has it. ✔
- `scratch-jjtrial.txt` still `??` with intact content. ✔
- Side observation: after the commit `git symbolic-ref -q HEAD` fails — HEAD is **detached at d3a7044d** (the `@-` export), and `git log @{u}..HEAD` now fails `fatal: HEAD does not point to a branch`. Matches the wave brief; `detect_branch` covers it via `origin/HEAD`.

**Operator-push collision:** cloned `remote.git` → `operator`, committed `considerthese/round-999-operator.md` (`5a82548`), pushed to `main`. Then a second helper commit of `corpus/lessons/round-999-jjtrial-2.md`:

```
committed 874727ba43a5326cca906d5ddbc4a3242e42a9cd
pushed   bf7e9b1b2af90116b922db781e562703e5fd7e05   exit 0   (~1.2 s)
```

The pushed hash differs from the committed hash — the helper's fetch+rebase path ran: remote `main` = `bf7e9b1 → 5a82548 (operator) → d3a7044 → 4ad2683`. Both my commits sit on top of the operator tip; the operator commit was **not** rewritten (`5a82548` still in place, non-force push), `git merge-base --is-ancestor bf7e9b1… main` → 0, `state` → `ahead=0`. This is exactly the promised semantics, but note it for the protocol: **the hash printed as `committed` is not citeable — only `pushed <hash>` is** (helper already prints the right one).

## Step 5 — lane's own git-touching gates

`grep 'git '` on `SKILL.md` hits only prose citations; the actual subprocess-git callers in the lane are `tools/harness/receipt_guard.py` (`rev-parse`, `symbolic-ref`, `show-ref`, `ls-files`), `tools/harness/claims-freshness.py` (`ls-tree -r -z`, `cat-file --batch`, `rev-parse`), and `tools/check-readme-revisions.py` (`git -C LANE show <base>:corpus/README.md`). Ran each `--selftest` with 300 s timeout, colocated vs plain control clone:

| Selftest (cwd = repo root) | colocated lane | plain clone | verdict |
|---|---|---|---|
| `python3 tools/harness/receipt_guard.py --selftest` | exit 0, 45/45 controls | exit 0 | identical — no colocation failure |
| `python3 tools/harness/claims-freshness.py --selftest` | exit 0, registry 43/43 + seam 19/19 | exit 0 | identical — no colocation failure |
| `python3 tools/check-readme-revisions.py --selftest` | exit 0, all controls + `selftest: all checks passed` | exit 0 | identical — no colocation failure |

No colocation-caused failure observed. Note these selftests build disposable fixture repos and use only read-only git verbs that don't depend on HEAD attachment; `receipt_guard.py` does probe `symbolic-ref HEAD` but tolerates a detached HEAD (its `rev-parse HEAD^{commit}` path succeeds first, and `_head_commit` handles returncode 1).

## Additional probes (seat-initiated)

- **Index destruction confirmed:** `git add scratch-jjtrial.txt` → `A  scratch-jjtrial.txt`; ran one helper commit of another path; afterwards `git status` → `?? scratch-jjtrial.txt`. Any jj mutation resets the git index — **`git add`-staged entries silently revert to untracked**. Fleet tooling that stages before calling the helper will lose the stage (but not the file).
- **`jj file track --include-ignored` bypasses the size cap:** in lane-autotrack, tracking the 135 MB `b35683971-Gamble_R.pdf` by file path succeeded (exit 0; `.git` grew 25 M → 155 M). Helper commit applies `--include-ignored` to every named **file**, so `jj-lane.sh commit … -- reports/supplement-opencode-1/scratch/round5-06/b35683971-Gamble_R.pdf` would push a 135 MB blob. Named **directories** don't get the flag, so the ignored scratch dir as a whole is safe — the hazard is only explicitly-named ignored files.
- **`git fsck`:** only dangling objects (jj's historical @ commits etc.) — expected colocation noise, no corruption.
- **LOG.md append-only:** respected — the commit contained only the appended line; nothing rewrote history after push (`d3a7044d` and `bf7e9b1` remain ancestors of `main`; the rebase ran *before* the second push).

## PASS/FAIL table

| Step | Check | Result |
|---|---|---|
| 2 | helper init exit, repo config set, HEAD attached, porcelain unchanged (0), `??` semantics preserved | **PASS** |
| 2 | `jj status` latency | 9–10 ms — **PASS** |
| 3 | all() measurement (0 files snapshotted on real tree; intent-to-add + 1 MiB refusal on synthetic files; 12–20 ms) | **PASS** (measured) |
| 4 | `committed`/`pushed` lines, lane identity on author+committer, `git log` == pushed hash, ancestor of main, state ahead=0, remote updated, scratch file intact+untracked | **PASS** |
| 4 | operator-push recovery (fetch+rebase, remote commit preserved, push not forced) | **PASS** |
| 5 | receipt_guard / claims-freshness / check-readme-revisions selftests vs plain clone | **PASS** — 3/3 identical exit 0 |

## Colocation hazards specific to this lane

1. **311 MB of ignored PDFs** under `reports/supplement-opencode-1/scratch/` — safe under auto-track=none and under dir-path commits, but **one explicitly-named ignored file committed through the helper lands in git history unbounded** (measured: 135 MB tracked, exit 0). Recommend a helper-side size guard (e.g. refuse `-s >64 MB` files) or lane discipline; also the 1,037,171-byte tracked `tie-break-check-receipt.json` shows this lane rides within ~17 KB of jj's 1 MiB default for new files.
2. **Detached HEAD after any jj mutation** — `@{u}` revsets break; all lanes' git reads must use `main`/`origin/main` names (helper's `detect_branch` handles it; ad-hoc `git` in lane prompts must not assume `@{u}`).
3. **git index reset on every jj mutation** — never `git add` and then call the helper.
4. **Untracked-file race with default all()** — measured intent-to-add pollution; none() mandatory on this lane.
5. **Symlinks in ignored scratch** (`round7-15/` has out-of-repo targets, ignored): harmless today; if that dir were ever committed jj/git would store the link itself — consistent with git semantics, no extra hazard.
6. **`cp -a` of a colocated repo copies the .jj store** — jj detects and warns; harmless for trials, but don't `rsync -a` a colocated lane as a backup method without excluding `.jj`.
7. No nested `.git` dirs (the `kotodama-shokunin/` subdir is a plain dir containing `reports/`), no `.gitattributes`/LFS, no custom `.git/hooks` — clean on those axes.
8. `.ufo/state/` is gitignored already; helper additionally refuses `.ufo/state/*` and `.ufo/watchdog.log` pathspecs (checked in helper source lines 182–183).

## Recommended per-lane config / ignore additions

- Repo config (helper already sets; all confirmed working here):
  - `snapshot.auto-track = "none()"` — **required** on this lane.
  - `user.name`/`user.email` = lane identity — set, enforced per command anyway.
  - `revset-aliases."trunk()" = "main@origin"` — set.
- Optional belt: `snapshot.max-new-file-size` stay at the default **1 MiB** (raising it would only legitimise PDFs entering history); instead add a helper-level byte-size refusal for `--include-ignored` file args. [INFERENCE: worth a fleet-wide default, not just kotodama.]
- `.gitignore`: current set is adequate (covers the entire 311 MB scratch tree and `.ufo/state/`). No additions strictly needed. Optional hardening: `.jj/` is already excluded via jj's own `.jj/.gitignore`; nothing to add.
- Lane-practice note (docs, not config): cite only the `pushed` hash in reports; never `git add` before helper calls; treat `git status --porcelain` as the cross-tool contract (it matched jj state exactly in every observation above).

## Files changed / artifacts

- Report only: `.ufo/waves/hyaku/jj-w1/reports/JjTrialKotodama.md`.
- All mutations confined to `/fast/scratch/jj-wave/JjTrialKotodama/` (removed on completion; the sandbox bare remote received only throwaway `round-999`/`considerthese` commits — nothing pushed outside the sandbox).
- No installs; jj 0.45.1 and git 2.56.0 already present.
