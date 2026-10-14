# xsentinel report — wave shokunin-train-20261013-w5

**Seat:** xsentinel (cross-lane, r0). **Declared axis-move:** pre-wave-5 + mid-wave census across all three lanes (HEADs, secrets, scratch sizes, commit identities, pushes/stashes, w4 leakage).
**Census window:** dispatch declared `2026-10-14T02:30Z` (spec commit `f86e464` at 02:23:38Z). Measurements taken ~04:05–04:56Z. **The wave settled during the census:** lane integration commits landed 04:36–04:49Z while measuring (audio `014b532`, g2d `414eb8e`/`44b6d2b`/`b8a5a04`, g3d `fc9915e`); verifier/scratch writes were still in flight at 04:55Z (`corpus/live/r66-verifier/`, runs `20261014T0445*`). Both at-dispatch and current values are reported below.

**Path resolution note (load-bearing):** the brief's `~/Projects/prymeagnt/<lane>` roots are *wrapper* worktrees (`.git/worktrees/*`, heads `8ec4783`/`fe4bbea`/`e1e863c`) — the expected dispatch SHAs **do not exist in those object stores** (`git cat-file -t 30e5e32` → `Not a valid object name`). Canonical lane repos are `~/Projects/shokunin/{audio-shokunin,game-dev-2d-shokunin,game-dev-3d-shokunin}`, reached via `<wrapper>/.shokunin/<lane>` symlinks. All canonical values below are from the shokunin repos. Evidence dumps: `xsentinel-scratch/{census-evidence.txt,secrets-scan.txt,baseline-recursion.txt}` (+ two files pre-existing from an earlier partial xsentinel run at 02:32Z — `new-w5-files.txt`, `cred-hits.txt`; superseded by this pass).

## Verdict summary

| # | Item | Severity | Result |
|---|------|----------|--------|
| 1 | HEADs at dispatch | informational | audio `30e5e32` ✓, g2d `61ec1c0` ✓, g3d `e435a01` ✓ (canonical repos, exact); fleet `f86e464` = expected `c5b89ea`+1 (the w5 spec commit itself, pre-dispatch) |
| 2 | Credential-shaped scan, wave-5 files | clean | zero high-signal hits, zero key/token assignments; loose-keyword hits all benign prose/test tokens |
| 3 | Scratch-size census / baseline recursion | **HIGH — flag for integration (repeat of the w4 1.4G lesson)** | g2d `corpus/live/r65-baseline` = **1.4 GB**, embeds **12 nested `r*-baseline` dirs** incl. double-nesting under `r63-baseline/tree/`; 14× 71 MB `fixture.x86_64`. Audio `r66-baseline` 141M compliant (explicit excludes honored). g3d `r74-baseline` 26M, disclosed `npm ci` node_modules provisioning |
| 4 | Mid-wave commit identity | clean | 5 post-dispatch commits, all authored by correct lane identities (`audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin`); consistent with parent-integration model |
| 5 | Pushes/stashes | clean | zero stashes everywhere; zero remote-tracking ref writes after dispatch — no push/fetch during the wave |
| 6 | w4 stale artifacts in tracked state | **MEDIUM (root cause of item 3)** | g2d tracks **34,523 files** of `corpus/live/r63-baseline` (committed at r63, w3 era, foreign identity) + w4 stray `corpus/live/r64-baseline/battery.stdout`; audio tracks r62–r64 + now r65-baseline receipt sets (~200 files each, convention); tracked `*.pyc` still live (audio 8, g2d 15) |

One HIGH finding (non-blocking to wave correctness, compounding at integration), one MEDIUM, rest clean/informational.

---

## 1. git HEADs at dispatch vs expected

| repo | brief-expected | HEAD at dispatch | observed now | verdict |
|------|----------------|------------------|--------------|---------|
| `audio-shokunin` (main) | `30e5e32` | `30e5e32` ("audio r65 adjudication: ADMIT…", 02:09Z) | `014b532` (+1 integration commit, 04:36Z) | **exact match** |
| `game-dev-2d-shokunin` (main) | `61ec1c0` | `61ec1c0` ("g2d r64 adjudication: ADMIT…", 02:21Z) | `b8a5a04` (+3 commits, 04:38–04:49Z) | **exact match** |
| `game-dev-3d-shokunin` (main) | `e435a01` | `e435a01` ("g3d r73 adjudication: ADMIT…", 02:19Z) | `fc9915e` (+1, 04:38Z) | **exact match** |
| `~/Projects/shokunin` fleet (master) | `c5b89ea` | `f86e464` | `f86e464` | **stale expectation, not anomaly**: `f86e464` is the w5 spec/tasks/registry commit (02:23:38Z, 7 min pre-dispatch); its parent is `c5b89ea`. Identical off-by-one pattern to w4. |
| `~/Projects/prymeagnt` + wrappers | — | `a605f31` / `8ec4783`,`fe4bbea`,`e1e863c` | unchanged | quiet; the stale-shell trap from the w4 report is still armed (extraction-shell histories end at the `.shokunin` symlink commits) |

Commands: `git -C <repo> rev-parse --short=7 HEAD`, `git log --format='%h %an %aI %s'`.

## 2. Credential-shaped scan — wave-5 files

Scanned all wave-created surfaces: `tasks/*.txt` + wave `*.json` + wave scratch dirs; audio `corpus/live/{r66-*,round-66,runs/20261014T02*}`; g2d `corpus/live/r65-*` + `reports/round-65/`; g3d `corpus/live/r74-*` + `reports/round-74/` — including all `frozen/` payloads (full output: `xsentinel-scratch/secrets-scan.txt`).

- High-signal pass (`BEGIN.*PRIVATE`, `AKIA`, `ghp_`, `github_pat_`, `glpat-`, `xox[baprs]-`, `sk-`, `AIza`, `aws_secret`, OpenSSH/RSA/EC blocks): **0 hits**.
- Assignment pass (`api_key|secret|password|token|bearer` followed by `[:=]` + quoted value): **0 hits**.
- Loose-keyword hits are all benign: probe witness fields (`"cmdline token absent"` in `r62-boundary/port-recon-verdicts.json`, embedded via frozen), an `identity_token = "--out-dir=…"` variable in `drive_port_recon.py`, forged-marker test tokens in `r65-boundary/drive_edges.py` (`FORGED split-token diagnostic`), and report prose.

**Result: CLEAN** — same profile as w4; vendored blobs inside frozen trees carry no credential material.

## 3. Scratch-size census — the 1.4G recursion repeated

| tree | size | verdict |
|------|------|---------|
| `g2d/corpus/live/r65-baseline` | **1.4 GB** | **VIOLATION — >200M flag and nested-embedding prohibition** |
| `audio/corpus/live/r66-baseline` | 141M | compliant — `archive-manifest.txt` + `archive-excluded.txt` (693 members dropped: every tracked `r*-baseline` + `node_modules`); `find frozen -type d -name '*baseline*'` → **0** |
| `g3d/corpus/live/r74-baseline` | 26M | size OK; `frozen/corpus/fixtures/three/node_modules` (23M) present — see below |
| stale on disk | g2d `r64-baseline` 1.4G (flagged w4, still present), audio `r64-baseline/tree` 119M + `r65-baseline` 135M | operator cleanup pending |

**g2d r65-baseline anatomy.** `frozen/` contains 12 `r*-baseline` dirs — top level `r57-parent/r58-process/r59-audio/r61/r62/r63/r64-baseline`, plus a second nesting under `r63-baseline/tree/corpus/live/r5{7,8,9}/r6{1,2}-baseline` (`baseline-recursion.txt`). Fourteen 71,680,000-byte `fixture.x86_64` Godot export binaries, i.e. the same mass flagged in the w4 report.

**Mechanism — tracked-state embedding, not untracked copy.** The seat did use `git archive HEAD` (verified: untracked paths `corpus/live/r64-baseline/frozen`, `corpus/live/runs` are absent inside `frozen/`). The embedded trees are *tracked*: HEAD `61ec1c0` contains **36,122 members matching `r*-baseline`** — dominated by `corpus/live/r63-baseline` (34,523 files, a full `tree/` repo-copy committed at w3-era `de78edb`/`a7e0cb1`, authored by `games-engine-mechanics-shokunin`). The seat's verification grepped `git ls-tree -r HEAD --name-only | grep -E 'frozen|node_modules'` → 0 (literally true — nothing is *named* `frozen`), but the standing seat rule and this wave's g2d brief both prohibit "prior `r*-baseline`/frozen trees … exclude them explicitly". `reports/round-65/r65-baseline.md` therefore reports "no nested prior frozen trees" — technically worded, materially falsified: nested prior *baseline* trees are embedded. **Exploit/defect path:** the exclusion check matched on directory-name vocabulary instead of the prohibited set; every future `git archive` freeze re-embeds the committed `r63-baseline` until it is untracked — g2d `corpus/live` is now **4.2G** (was 2.8G at w4 census; ~1.3G+/wave trajectory), and each new baseline's frozen tree re-adds ~1.4G of worktree mass plus the same mass again to any commit that lands it.

**g3d deviation (low):** `frozen/…/node_modules` is gitignored → it did not come from `git archive`; the seat's own report discloses provisioning it via `npm ci` inside the frozen tree (lockfile three@0.186.1) so the battery can run. Bounded and disclosed, but the seat rule's literal "NEVER … node_modules" text needs either an explicit provisioning exception or a deps-outside-frozen layout.

**Smallest remediation:** (a) `git rm -r --cached corpus/live/r*-baseline` + ignore `corpus/live/**` in g2d (and the r62–r65 receipt sets in audio if receipt-commit convention is not intended for baselines), cutting 36K tracked members; (b) baseline freeze command becomes `git archive HEAD | tar -x --exclude='corpus/live/r*-baseline' --exclude='*/frozen/*' --exclude='node_modules'` — audio's manifest+exclude pattern is the working template, adopt it fleet-wide; (c) operator delete of `r64-baseline/` (1.4G) and `r65-baseline/frozen/` (1.4G) after adjudication receipts are secured.

## 4. Mid-wave commit identity

`git log --all --since=2026-10-14T02:30:00Z` across all 5 repos at 04:15Z → 0 commits; re-measured 04:52Z → 5 commits, all post-settle integration (leaf-seat rule held while seats were active):

| commit | repo | author | time (Z) | content |
|--------|------|--------|----------|---------|
| `014b532` | audio | `audio-shokunin <audio-shokunin@local>` | 04:36 | r66 landing — 5,166 files; commits r66 seat dirs + r66-baseline *receipts* (207 files: manifest/ledger/`out/`; **0 `frozen/` members**) and w4-era `r65-baseline` receipts (194 files) |
| `414eb8e` | g2d | `game-dev-2d-shokunin <game-dev-2d-shokunin@local>` | 04:38 | r65 move — 723 files incl. `r65-author/{fault,pretree}-runs/` scratch trees (`.godot/` caches, `*.uid`, `__pycache__` committed wholesale — convention) + stray `corpus/live/r65-baseline/battery.stdout` |
| `44b6d2b` | g2d | same | 04:45 | adjudication+lesson+verifier (5 files, clean) |
| `b8a5a04` | g2d | same | 04:49 | boundary-seat landing (98 files, 0 baseline/frozen) |
| `fc9915e` | g3d | `game-dev-3d-shokunin` | 04:38 | r74 landing (9 files, clean) |

**Identities: PASS** — every mid-wave commit carries the expected per-lane identity. Two nits: (i) email convention drift — current-era commits use `<lane>-shokunin@local` vs historical `<lane>@shokunin.local` (same display name); (ii) pre-existing foreign-identity history persists: g2d r60–r63 commits (incl. `de78edb`, which committed the `r63-baseline` tree behind item 3/6) are authored `games-engine-mechanics-shokunin`, and all three wrapper-worktree tips carry that identity — flagged in w4, unchanged, informational.

## 5. Pushes/stashes

- `git stash list` → empty in all 8 repos (3 wrappers, fleet, 3 lanes, prymeagnt root).
- Zero remote activity during the wave: all `logs/refs/remotes/**` files have mtime ≤ `2026-10-13 17:05 -03` (= 20:05Z, ~6.4h pre-dispatch); `find .git/logs/refs/remotes -newermt 02:30Z` → empty everywhere; `FETCH_HEAD` mtimes pre-dispatch.
- Unpushed accumulation (operator-owned): lanes ahead of `origin/main` — audio +11, g2d +12, g3d +13 (`git rev-list --count origin/main..main`); fleet `master` ahead of `origin/master` by 11; prymeagnt `main` == `origin/main`.

**Push/stash policy holding.**

## 6. Stale wave-4 artifacts → tracked state

- **g2d `corpus/live/r64-baseline/battery.stdout`** — the w4 baseline stray, committed in `a32920b` (w4 era). Confirmed still tracked; pattern repeated: `r65-baseline/battery.stdout` was committed in w5's `414eb8e` (same single-file leak shape).
- **g2d `corpus/live/r63-baseline`** — 34,523 tracked files (w3-era, foreign-identity commits `de78edb`/`a7e0cb1`); this committed frozen `tree/` is the root cause making every `git archive` baseline recursive (item 3).
- **audio `corpus/live/r{62,63,64,65}-baseline` receipt sets** tracked (181/254/256/194 members) — audio commits baseline receipts each wave; the w4-round `r65-baseline` set landed inside w5's `014b532`. Consistent convention, but it is what grows the exclusion list every wave (693 members this wave).
- **Tracked `*.pyc`** still live: audio 8, g2d 15 (`__pycache__/*.pyc` show `M` again this wave — bytecode noise in diffs; g3d properly ignores them via `corpus/.gitignore`).
- Fleet w4 tracked set is clean (dispatch/spec/tasks/x-reports only — the 3 grep hits were the `*-baseline.txt` task briefs, not scratch). Untracked stale on disk: `w3/x-connector.md`, w4 x-seat scratch dirs, w5 `xconnector-report.md` now landed untracked (awaiting adjudication commit).

## Additional boundary observations (informational)

- **Scope containment held.** Post-dispatch writes outside declared scratch/report paths: audio author edits `corpus/fixtures/{build_artifacts.py,measure_audio.py}` + `corpus/artifacts/*.wav` (17 tracked wavs) + ~200 tracked `corpus/live/round-*/` probe wavs — all **byte-identical rebuilds** (`git status` shows no `M` for them; only mtimes moved), which corroborates the "96-command ledger byte-stable" claim rather than violating scope. g2d: 0 files outside `r65-*`/`round-65`. g3d: only the two tracked fixtures in flight (`navagent3d_detour.gd`, `run_battery.py`).
- **Wrapper-shell trap (persists from w4):** `~/Projects/prymeagnt/{audio,game-dev-2d,game-dev-3d}` remain live worktrees with disjoint heads; a seat resolving the brief's literal "worktree/repo root" would inspect a stale history. Observed traffic correctly resolves through `.shokunin/<lane>` symlinks. Remediation unchanged: delete or pointer-ify the nested `.git`s after verifying no unique objects.
- **Timing note:** g2d/g3d baseline trees were created 02:24–02:28Z, i.e. minutes *before* the declared 02:30Z dispatch stamp — consistent with the spec commit landing 02:23Z and the stamp being rounded; not an anomaly.
- **g2d `corpus/live` = 4.2G** and grows ~1.3G/wave while baseline trees remain tracked — disk-exhaustion trajectory for the host; highest-leverage single fix in this report.

**Scope:** leaf census only — read-only git commands (`rev-parse`, `log`, `ls-tree`, `ls-files`, `status`, `stash list`, `check-ignore`), `du`/`find`/`rg` scans. No commits, no mutations to any repo or another lane's state; scratch confined to `xsentinel-scratch/`; no domain-facing actions attempted.
