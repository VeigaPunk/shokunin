# xsentinel report — wave-6 pre-wave + mid-wave census (cross-lane)

Wave: shokunin-train-20261014-w6 · Dispatch: 2026-10-14T05:01:28Z (02:01:28 -0300) · Census taken ~02:20-02:35 -0300 (wave in flight)
Scope: fleet `~/Projects/shokunin`, lanes `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, worktrees `~/Projects/prymeagnt{,/audio,/game-dev-2d,/game-dev-3d}`.
Scratch: `.ufo/waves/shokunin-train-20261014-w6/xsentinel-scratch/` (new-w6-files.txt, new-w6-textfiles.txt, cred-hits.txt).

## Verdict line

Dispatch expectations mostly hold: all four base SHAs match, zero pushes, zero stashes, zero real credentials in 3,396 new wave-6 files. **However the "g2d archives shrank to MB-scale" expectation is FALSIFIED** — `git archive HEAD` is still 644MB — and the two largest findings are the same failure class that caused the r63 incident: a 117M receipt file and ~1.4G of baseline trees sitting **unignored** on disk.

## 1. git HEADs at dispatch — PASS

| repo | HEAD at census | expected | verdict |
|---|---|---|---|
| fleet (`~/Projects/shokunin`) | `c6dea73` (child of `7e2b35c`) | `7e2b35c`+ | PASS — `c6dea73` is the wave-6 dispatch commit itself, committed exactly at dispatch 02:01:28 -0300 |
| audio-shokunin | `0df212f` | `0df212f` | PASS |
| game-dev-2d-shokunin | `2efaae2` "hygiene: untrack r63-baseline/tree" | "hygiene tip" | PASS |
| game-dev-3d-shokunin | `35a911c` | `35a911c` | PASS |
| prymeagnt root / audio / g2d / g3d worktrees | `a605f31f` / `8ec47838` / `fe4bbeaf` / `e1e863c3` | (not pinned) | clean, on `craft/*-r1` branches |

Evidence: `git -C <repo> rev-parse HEAD`; `swarm-registry.json` base_shas.

## 2. Credential-shaped scan on new wave-6 files — PASS (0 real hits)

- Enumerated `find <repo> -newermt '2026-10-14 02:01:28' -type f` → 3,396 files (audio 135, g2d 183, g3d 1,267, fleet 1,587); 3,236 text files scanned.
- Pattern set: `BEGIN *PRIVATE KEY`, `AKIA…`, `gh[pousr]_`, `github_pat_`, `glpat-`, `sk-`, `xox[baprs]-`, `AIza…`, `password|passwd|api_key|secret|token|credential` assignments.
- 80 regex hits — **all** inside vendored `three.js` under `game-dev-3d-shokunin/corpus/live/r75-baseline/frozen/corpus/fixtures/three/node_modules/three/` (XHR `credentials` docs, parser `token` locals). `grep -v 'node_modules/three/' cred-hits.txt` → **0 lines**.
- No real credentials in new wave-6 content.

## 3. Scratch-size census — PARTIAL FAIL

### g2d archive shrink: expectation falsified
- `git -C game-dev-2d-shokunin archive HEAD | wc -c` → **644,106,240 bytes (~614MiB)**, 36,912 tracked files, ~700M working-tree bytes (`git ls-files -z | du -ch --files0-from=-`).
- The hygiene commit `2efaae2` did remove the 34,522-file `r63-baseline/tree` (tracked r63-baseline files now only `battery.stdout` + `reports/round-63/r63-baseline.md`); archive fell ~1.4G → 644MB. **But "MB-scale" as expected is falsified**: remaining mass is `corpus/live/` tracked legacy — 36,170 files / 689M, dominated by **7 tracked 73.7MB `fixture.x86_64` export binaries** under `corpus/live/r25-{export-scout,export-critic,pair-reviewer}/` (~516M) plus dense historical seat-scratch dirs (r57-save-executor 1,635 files, r37-focus-executor-full 1,403, …).

### Baseline frozen/tree dirs >200M on disk — 2 flags
| dir | size | tracked? | ignored? |
|---|---|---|---|
| `g2d/corpus/live/r63-baseline/tree` | 682M | no (untracked by `2efaae2`) | yes `corpus/.gitignore:3` — but **never deleted from disk** |
| `g2d/corpus/live/r66-baseline/frozen` | 700M | no | yes `corpus/.gitignore:4` — **written this wave at 02:02 by r66-baseline seat**: the exact pattern just fixed is already recurring |
- audio (unignored — see §6): `r64-baseline/tree` 119M, `r65-baseline/frozen` 134M, `r66-baseline/frozen` 139M.
- g3d `r75-baseline/frozen` 25M incl. `node_modules/three` — under 200M, ignored via `corpus/.gitignore: live/`.
- Fleet `.ufo/waves/*` all ≤1.9M; w4/w5 `xconnector-scratch`/`xsentinel-scratch` leftovers untracked, 4–460K (cosmetic).

## 4. Commit-identity on mid-wave commits — PASS (1 commit, consistent)

- Only post-dispatch commit anywhere: fleet `c6dea73`, author **and** committer `devin-fleet <fleet@shokunin.local>` — same identity as wave-5 closeout `7e2b35c`. No lane repo has a post-dispatch commit (seats are LEAFs; parent integrates after wave).
- Observation (info): all three lanes show a coordinated author-email migration in their final pre-wave commits — `<lane>@shokunin.local` → `<lane>-shokunin@local` (audio between `30e5e32`→`014b532`, g2d `61ec1c0`→`414eb8e`, g3d `e435a01`→`fc9915e`); fleet `shokunin-fleet` → `devin-fleet` at `7e2b35c`. Uniform and timestamped before dispatch — noted for provenance, not an intrusion signal.

## 5. Pushes / stashes — PASS

- `git stash list` → 0 entries in all 8 repo views.
- Remote-ref reflogs (`git reflog show --date=iso origin/main` / `--all | grep push`): last `update by push` 2026-10-13 ~17:04–17:05 -0300 in every repo — ~9h pre-dispatch. No push, fetch, merge, rebase, or checkout evidence mid-wave. Lane branches sit ahead of origin (audio +12, g2d +13, g3d +13) — normal; push is operator-owned.

## 6. Stale artifacts / exclusion durability — FAIL (two MEDIUMs)

### F1 — MEDIUM: 117M `edge-verdicts.json` sits unignored, one blanket-add from tracked state
- `game-dev-2d-shokunin/corpus/live/r65-boundary/edge-verdicts.json` = 122,535,352 B (117M), untracked, **never committed** (`git log --all -- <path>` empty), and **not covered by any ignore rule**: `git check-ignore -v` exits 1 — `corpus/.gitignore` only has `live/*/tree/` + `live/*/frozen/` (commit `2efaae2`).
- The r65-boundary receipt was excluded *procedurally* (nobody ran `git add -A` since), not *durably*. A blanket `git add corpus/live/` or `git add -A` at r66 integration commits 117M into the repo — the exact failure the r63 hygiene commit was fixing. It is also the only file >20M sitting untracked-but-unignored across all five repos.
- Smallest remediation: append a pattern to `game-dev-2d-shokunin/corpus/.gitignore` covering boundary megareceipts (e.g. `live/*-boundary/edge-verdicts.json`, or a size-class rule like `live/*/edge-*.json`), or delete the file post-adjudication; owner: g2d parent/operator at integration.

### F2 — MEDIUM: audio lane has no exclusion for baseline `tree/`/`frozen/`; ~392M unignored
- `audio-shokunin` has **no `.gitignore` covering corpus at all** (`cat .gitignore corpus/.gitignore` → absent/empty). `git check-ignore` on `corpus/live/r64-baseline/tree/`, `r65-baseline/frozen/`, `r66-baseline/frozen/` → no match.
- Mitigating evidence: parent integrates selectively — `corpus/live/r64-baseline{,/out}` is tracked while `tree/` stayed untracked; same for r65/r66 `frozen/`. Held for 3 rounds by convention only.
- Risk: any future blanket add (or a new seat running `git add corpus/`) commits ~392M instantly; audio already tracks 161M under `corpus/live` (13,751 files) so the "commit live scratch" precedent exists. Same class as F1 — port the g2d `live/*/tree/` + `live/*/frozen/` patterns (or g3d's blanket `live/` ignore) into `audio-shokunin/.gitignore`.

### F3 — LOW: disk-side recurrence already underway
- `r66-baseline/frozen` 700M (g2d) created at 02:02 this wave; `r63-baseline/tree` 682M still on disk after untrack; audio r64–r66 tree/frozen ~392M. All ignored-or-untracked → no tracked-state exposure, but ~1.8G/wave of regenerable mass. Recommend deleting extracted trees post-untrack (r63) and having baseline seats freeze via `git archive` only (per seat rules), not `cp -a`.

### F4 — LOW: g3d baseline froze `node_modules` into snapshot
- `r75-baseline/frozen/corpus/fixtures/three/node_modules/` (25M, 1,589 files) — contrary to the "never embed node_modules" baseline guidance; harmless because `corpus/.gitignore: live/` ignores it, but it also inflates the credential-scan surface (all 80 regex hits were this tree).

### Positive notes
- g3d posture is the cleanest: `corpus/.gitignore → live/` — entire live tree durably excluded; tracked tree is 2.5M/274 files.
- audio wave-6 transport runs regenerate `corpus/artifacts/*.wav` (tracked) **byte-identically** — `git status` shows 0 modified tracked files; the "prior ledger byte-stable" constraint holds mid-wave.
- g2d hygiene commit itself is well-formed: `live/*/tree/` + `live/*/frozen/` verifiably match the on-disk dirs (`check-ignore -v` shown above).
- No cross-lane writes observed: all new files sit inside each seat's declared scratch (`corpus/live/rNN-<seat>/`) or report scope; one first report landed (`g2d reports/round-66/r66-baseline.md`, expected tracked path).

## Severity summary

| sev | finding | path |
|---|---|---|
| MEDIUM | 117M receipt unignored; exclusion procedural not durable | `game-dev-2d-shokunin/corpus/live/r65-boundary/edge-verdicts.json` |
| MEDIUM | archive still 644MB — "MB-scale" falsified; 7×73.7MB export binaries + 689M live legacy tracked | `game-dev-2d-shokunin/corpus/live/r25-*/**/fixture.x86_64` |
| MEDIUM | no corpus ignore rules; ~392M baseline mass one blanket-add from tracked | `audio-shokunin/corpus/live/r{64,65,66}-baseline/{tree,frozen}` + missing `audio-shokunin/corpus/.gitignore` |
| LOW | ~1.4G regenerable baseline trees left on disk post-untrack (r63) / re-created mid-wave (r66) | `game-dev-2d-shokunin/corpus/live/r{63,66}-baseline/{tree,frozen}` |
| LOW | node_modules embedded in frozen snapshot (ignored, wasteful) | `game-dev-3d-shokunin/corpus/live/r75-baseline/frozen/…/node_modules` |
| INFO | stale w4/w5 x-seat scratch untracked in fleet repo | `.ufo/waves/shokunin-train-20261013-w{4,5}/*-scratch/` |
| PASS | HEADs, credential scan (0 real/3,396), commit identity, zero pushes/stashes, byte-stable tracked fixtures | — |

Census limits: snapshot mid-wave (seats still writing); reflog-based push evidence is local-only (no remote contact attempted, per operator-ownership).
