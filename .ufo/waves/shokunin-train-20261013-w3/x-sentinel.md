# X-Sentinel — invariant sweep, wave shokunin-train-20261013-w3

Seat: sentinel (LEAF, read-only on repos; this file is my only write). Lane `f16bc01d`.
Sweep executed: 2026-10-13 21:36–21:53 -0300. Wave dispatched 2026-10-14T00:30:00Z (= 21:30:00 -0300) per `dispatch.json`/`swarm-registry.json` (26 lanes: 8 seats × audio r64 / g2d r63 / g3d r72 + XConnector + XSentinel).

**Timing caveat — live-wave census.** First status reads began ~21:36 (T+6min); lanes were already writing. During the sweep itself, `audio-shokunin` HEAD advanced `37d4c57` → `5cc0eb0` (an in-wave commit at 21:38:17 — see §4/F1). The tables below record both the earliest read (closest to pre-wave) and the final read at 21:52:43. Treat all rows as a point-in-time baseline with documented drift, not a frozen image; §6 re-verify commands close the gap at integration.

## 1. Contamination baseline — `git status --short` + HEAD

Canonical lane repos (under `~/Projects/shokunin`, nested-ignored by root `.gitignore` = `*-shokunin/`; independent repos, no submodules):

| repo | HEAD | branch vs `origin` | status @ first read (~21:37) | status @ 21:52:43 |
|---|---|---|---|---|
| `audio-shokunin` | **first read `37d4c57`**; final `5cc0eb0e2490c4d5c382511f57c2c7708cf7f75a` | `main`, ahead 6 / behind 0 | 40 lines (all `??`: `r64-reviewer/`, `r64-scout/`, 38× `corpus/live/runs/*`) | 199 lines: 4 `M` (`corpus/fixtures/build_artifacts.py`, `measure_audio.py`, + 2 tracked `__pycache__/*.pyc`), 195 `??` (185 `runs/*` dirs, r64-{author,baseline,boundary,critic,scribe,simplifier}, `corpus/live/round-64/`, `reports/round-64/*`) |
| `game-dev-2d-shokunin` | `edbd945dff303a13cec1c9134d2eedf16b8be44d` (r62 adjudication, committed 21:29:31 — 29s pre-dispatch) | `main`, ahead 4 / behind 0 | 2 lines (`?? r63-baseline/`, `?? r63-reviewer/`) | 10 lines: 2 `M` (`corpus/fixtures/descendant_pipe_probe.gd`, `run_battery.py`), `??` r63-{author,baseline,boundary,reviewer,scout,scribe,simplifier} + `reports/round-63/` |
| `game-dev-3d-shokunin` | `996ea376f1e5d7cc8be38429f7f97f1a8b7018c7` (r71 adjudication, 21:00:16) | `main`, ahead 6 / behind 0 | **0 lines** | 3 lines: `M corpus/fixtures/navagent3d_detour.gd`, `M corpus/fixtures/run_battery.py`, `?? reports/round-72/` |
| `~/Projects/shokunin` (fleet root) | `90c2d4ab57d7f39c987b9519c69092254abec1cb` (w3 spec+dispatch+registry commit, 21:34:27) | `master` vs `origin/master`, ahead 6 / behind 0 | 2 lines | 2 lines: `?? .ufo/waves/…-w2/x-connector.md`, `?? …-w2/x-sentinel.md` (w2 seat reports still awaiting integration commit) |

**Ignore-policy asymmetry (affects what "clean" means per lane):**
- `game-dev-3d-shokunin/corpus/.gitignore` = `live/` — the whole per-round scratch tree is invisible to `git status` (`check-ignore` confirms: `corpus/.gitignore:1:live/`). The r70/r71/r72 seat dirs exist on disk (r72-* created 21:35–21:46) yet produce zero status lines. **For 3d, `git status` cannot see lane writes** — contamination checks must diff `corpus/live/` by mtime/`find`, not status.
- `game-dev-2d-shokunin/corpus/live/.gitignore` = `runs/` + one historical dir — so `r63-baseline/` (incl. its **684M** `tree/` archive extract, §5/F2) shows as `??`.
- `audio-shokunin` has **no `.gitignore` anywhere** — all 185 `runs/` dirs and the 119M `r64-baseline/` accumulate as `??`.

Worktree supplement (`~/Projects/prymeagnt/<lane>`, the `.shokunin/<lane>` writers' cwd — independent repos):
`audio` `8ec47838`, `game-dev-2d` `fe4bbeaf`, `game-dev-3d` `e1e863c3` — all clean (0 lines), HEADs unchanged since 17:04 bootstrap; parent `~/Projects/prymeagnt` `a605f31f`, clean.

## 2. `.shokunin/<lane>` symlink resolution — VERIFIED ×3

```
prymeagnt/audio       .shokunin/audio       -> ../../../shokunin/audio-shokunin       -> realpath OK, .git present
prymeagnt/game-dev-2d .shokunin/game-dev-2d -> ../../../shokunin/game-dev-2d-shokunin -> realpath OK, .git present
prymeagnt/game-dev-3d .shokunin/game-dev-3d -> ../../../shokunin/game-dev-3d-shokunin -> realpath OK, .git present
```

Committed-vs-live: `git show HEAD:.shokunin/<lane>` == `readlink` for all three — **MATCH ×3** (a retargeted link would redirect every `.shokunin/<lane>/**` lane write out of the canonical repo). Sibling `.shokunin/{MANIFEST.json,mints/,reports/}` are real worktree content, not links — consistent.

Other symlinks fleet-wide (all resolve): 8× `.ufo/waves/round-12/mutants/m*/.ufo` → fleet `.ufo`; 1× `round-15/mutants-wave2/fixtures` → `../fixtures`. No dangling links, no links escaping `~/Projects/shokunin`.

**Inside the lane repos themselves there are no `.shokunin` symlinks.** What exists instead: 4 **committed directory copies** at `corpus/live/r35-baseline-reviewer/.shokunin/game-dev-2d/` and `…/r36-baseline-reviewer/.shokunin/game-dev-2d/` in g2d (HEAD stores them as `040000` trees, not mode-120000 links), plus their nested duplicates inside the new `r63-baseline/tree/` snapshot. They are dereferenced point-in-time copies of the lane's own `corpus/` (fixtures + lessons) — now diverged from canonical (canonical `corpus/fixtures/` has gained 7 files the embeds lack; `button_group_selection.gd` and `run_battery.py` differ in content). Harmless dead data, but every `git archive HEAD` baseline re-copies them (recursion: r63-baseline's tree contains the r35/r36 items' own `.shokunin` embeds). See F2.

## 3. Credential-material sweep — CLEAN; all hits benign-classified (no values printed)

Method: GNU `grep -rEl` (binary-inclusive; ripgrep `-l` provably misses ELF-contained markers — method note F6) over each repo excluding `.git`, plus a secret-shaped filename `find` (`*.pem *.key *.p12 *.pfx id_rsa* id_ed25519* .env* .netrc .npmrc *credential* *secret* *.keystore`) and git-config key audit. Strict shapes: `op://`, `PRIVATE KEY`/`BEGIN `, `gh[pousr]_*`, `github_pat_*`, `AKIA/ASIA`, `xox[baprs]-`, `glpat-`, `AIza*`, `sk-*{16,}`, `Bearer *{16,}`, `ssh-rsa`, `passphrase`, `Authorization:`; generic assignment tier `(password|passwd|secret|api_?key|token|credential)\s*[:=]` (ci). Git history `-G` scan of the same strict set: hits are all report/spec/docs commits (detection-pattern tables), zero payload.

| repo | strict hits | classification |
|---|---|---|
| `audio-shokunin` | `gh[pousr]_` bare prefix in `reports/round-62/r62-verifier.md` (+ copy nested in `r64-baseline/tree/`) | doc mention; real-token-shape count `gh*_…{20,}` = **0**. Generic tier: `r63-simplifier.md` only (prose). |
| `game-dev-2d-shokunin` | `PRIVATE KEY`/`BEGIN ` in **14 identical-class `fixture.x86_64` ELF exports** — 7 canonical under `corpus/live/r25-*/…out|export/` + 7 nested duplicates inside `r63-baseline/tree/`; plus `reports/round-61/r61-verifier.md` | ELF hits = TLS-library PEM *format-string constants* linked into Godot export templates (scattered BEGIN/END markers, no contiguous key blob) — same class adjudicated benign at w2; the +7 are snapshot duplication, not new material. `gh[pousr]_`/`glpat-`/`ssh-rsa` hits: the verifier doc's detection tables, real-shape count 0. Generic: the ELFs + `r62-boundary/drive_port_recon.py` (param names). |
| `game-dev-3d-shokunin` | `AKIA[0-9A-Z]{8,}` in 8 minified vendored `three` files (`draco_decoder.js`, `zstddec.module.js` + nested baseline copies); `gh[pousr]_` in r70/r71 verifier docs | exact AWS shape `AKIA[0-9A-Z]{16}` count = **0** — incidental uppercase runs in minified JS. Docs: bare-prefix mentions only. Generic tier: vendored `node_modules` parser identifiers. |
| `~/Projects/shokunin` root (excluding `*-shokunin/`) | `op://` prose ~67 files (`.ufo/reports`, wave docs); `github_pat_`/`gh_` bare prefixes; `PRIVATE KEY` in sentinel docs + declared synthetic fixture `.ufo/waves/round-9/corpus-gate.mjs`; `xox` bare prefix; one `sk-…{16,}` in `.ufo/waves/round-15/reviewer-final.md` | All documentation/fixtures. The `sk-` hit resolves to a 21-char run **inside a `task-…` identifier string** (context verified masked; len=21, sha-prefix `36fe82fe`). Full-token-shape `github_pat_`/`gh[pousr]_…{20,}` count = 0 everywhere. |

**Zero live credential values found in any scanned working tree.** Zero secret-shaped filenames. `prymeagnt` worktree `.shokunin/` non-symlink content: zero strict hits; no dotfile creds. Git config audit (all 4 repos): remote URLs are clean `https://github.com/VeigaPunk/*` (no `user:pass@`); **no `credential.helper`, no `http.*extraheader`** keys; no non-sample hooks in any `.git/hooks`.

## 4. Lane git identities + remote-push verification

**Identity chain.** No repo sets local `user.name`/`user.email`; effective identity falls back to global `ci`/`ci@local`. Lane commits arrive under per-invocation identities (`audio-shokunin <audio@shokunin.local>`, `game-dev-2d-shokunin <game-dev-2d@…>`, `game-dev-3d-shokunin <game-dev-3d@…>`, root `shokunin-fleet <fleet@…>` etc.) — i.e., env/`-c` overrides, not config. History confirms the fallback leaks through: `ci <ci@local>` authored 4–5 bootstrap commits in each lane and 13 at root. Root history also carries 55 pre-fleet commits under a personal identity (`…@gmail.com`) — already on the public GitHub remote; noted for provenance completeness, not actionable.

**No push during the wave — verified three ways** (remotes all reachable):
- Remote-tracking reflog tails (`logs/refs/remotes/origin/*`): last `update by push` entries at 17:04:50 / 17:04:52 / 17:04:53 / 17:05:20 -0300 (fleet bootstrap pushes ~4.5h pre-wave). Nothing after.
- Live `git ls-remote --heads origin` heads == local tracking refs exactly: root `9bdb31b`, audio `1c52c7d`, g2d `3ee05ff`, g3d `e054cfe`. If any in-wave commit had been pushed, the remote head would be a descendant of it — it is not.
- Direction check per repo: remote head is an ancestor of local HEAD; `ahead` = 4–6 unpushed local commits, `behind` = 0, no divergence. Unpushed local commits are the standing pattern (integration commits accumulate between bootstrap pushes).

## 5. Findings

| # | sev | finding | exploit/failure path | smallest remediation |
|---|---|---|---|---|
| F1 | LOW | **In-wave commit on a canonical lane repo**: `audio-shokunin` `5cc0eb0` "audio r64 interim: land reviewer+scout reports; correct r63 tarball-citation nit", 21:38:17, authored+committed `audio-shokunin`. Diff includes a **tracked knowledge file edit** (`corpus/knowledge/2026-10-13-sox-act-autodetect-predicate.md`) that r64 seats are dispatched to read. | Any pre/in-wave census (this one included) silently anchors to a moving HEAD; a lane citing the knowledge file may reference either revision → provenance ambiguity in evidence claims. Consistent with the fleet's own durability doctrine (root history commits in-flight bytes deliberately), so not a discipline breach — but it invalidates "frozen baseline" assumptions. | Integrator re-runs `rev-parse HEAD` + `status --short` at integration time rather than diffing against any earlier census; prefer post-settle edits to files named in live lane prompts. |
| F2 | LOW | **Unignored bulk snapshots**: g2d `corpus/live/r63-baseline/` = **684M** untracked (whole-repo `git archive` extract incl. nested `corpus/live/r2x/` binaries and the committed `.shokunin/game-dev-2d` embed copies); audio `r64-baseline/` = 119M untracked; audio also has 185 untracked `runs/` dirs. Prior convention committed baseline dirs selectively (g2d `r61-baseline` tracked = 1 file; g2d `.git` total = 36M). | A blind `git add -A`/`git add corpus/live` at integration lands ~800M+ into g2d history (~20× .git bloat), permanently duplicating ELF exports and fixture copies — and each future baseline re-nests them (observed: r63 tree already contains the r35/r36 embeds). | Integrate via explicit pathspecs excluding `*/tree/` and `runs/`; or add `*/tree/` (+ `runs/` for audio) to the lane's `corpus/live/.gitignore` — matching 3d's `live/` posture if bulk-scratch exclusion is the intent. |
| F3 | LOW | **Lane commit identity unpinned** — no `user.*` in any repo config; provenance relies on the invoker setting env identity every time. | A lane or script committing without the override lands as `ci <ci@local>` (already happened: 4–5 per lane) — attribution ambiguity between parent-integration and stray/leaf commits; history can't distinguish them by author field. | `git config user.name "<lane>-shokunin" / user.email "<lane>@shokunin.local"` per repo (fleet-local identities); or have the parent sign integration commits under a distinct `integrator` identity. |
| F4 | INFO | `audio-shokunin` tracks 4 `__pycache__/*.pyc` files; every python run in the wave flips them `M`. | Bytecode churn adds deterministic noise to `git status`, masking real contamination signals in the lane with the highest status volume (199 lines). | `git rm --cached corpus/fixtures/__pycache__` + ignore rule (as 3d already does). |
| F5 | INFO | w2 seat reports (`x-connector.md`, `x-sentinel.md`) remain untracked at root 22 min post-dispatch; w1's equivalents were committed in a later sweep (`ad1065b`). | Same D-129-class durability gap the fleet has documented against itself — uncommitted `.ufo/waves` bytes are lost on host failure until the integration sweep lands them. | None new — parent integration already sweeps these; noted so the gap isn't mistaken for missing seat output. |
| F6 | INFO | **Method defect worth recording**: `rg -l` missed all 14 ELF `PRIVATE KEY` marker hits (binary suppression); GNU `grep -rEl` caught them. A sentinel scanning binaries with rg alone would false-negative. | Credential material embedded in compiled artifacts (the realistic hiding spot) evades rg-only sweeps. | Keep `grep -rEl` (or `rg --binary`/`--text`) in the strict pass for any corpus containing binaries. |
| F7 | INFO | 3d's wholesale `live/` ignore means `git status` is structurally blind to in-lane scratch there — "clean at census" ≠ "nothing written" (r72 seat dirs appeared 21:35–21:46 while status stayed 0–3 lines). | Contamination/loss detection for 3d must use `find corpus/live -newer <marker>` or size diffs, not status. | Per-lane census note; no change required. |

**Positive confirmations:** `.shokunin/<lane>` targets verified committed==live ×3; no symlinks escape the fleet root; zero live secrets / secret-shaped files / creds-in-URL / credential helpers / non-sample hooks; remotes resolve and no push occurred in the wave window; root↔lane repo boundary intact (`*-shokunin/` ignore holds, no submodule confusion).

## 6. Integration-time re-verify (closes the T+6min→drift gap)

```sh
for d in . audio-shokunin game-dev-2d-shokunin game-dev-3d-shokunin; do
  echo "== $d"; git -C ~/Projects/shokunin/$d rev-parse HEAD
  git -C ~/Projects/shokunin/$d status --short | wc -l
done
# 3d scratch is invisible to status — census by mtime instead:
find ~/Projects/shokunin/game-dev-3d-shokunin/corpus/live -maxdepth 1 -newermt '2026-10-13 21:30' | sort
# link integrity (worktree side):
for d in audio game-dev-2d game-dev-3d; do
  readlink ~/Projects/prymeagnt/$d/.shokunin/$d
  git -C ~/Projects/prymeagnt/$d show HEAD:.shokunin/$d
done
# push-parity (must stay equal at integration):
git -C ~/Projects/shokunin/audio-shokunin ls-remote --heads origin
tail -1 ~/Projects/shokunin/audio-shokunin/.git/logs/refs/remotes/origin/main   # last 'update by push' should predate 21:30
# integration bulk guard:
git -C ~/Projects/shokunin/game-dev-2d-shokunin status --short | grep -c 'r63-baseline'   # if staged, verify tree/ excluded
```

End of assigned surface. — sentinel `f16bc01d`, wave shokunin-train-20261013-w3
