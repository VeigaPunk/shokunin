# X-Sentinel — invariant sweep, wave shokunin-train-20261013-w2

Seat: sentinel (LEAF, read-only on repos; this file is my only write).
Sweep executed: 2026-10-13 20:38:21 -0300 (`date +%s` = 1791934701).
Wave dispatch artifacts: `spec.json` mtime 20:32, `tasks/` 20:33, `dispatch.json` + `swarm-registry.json` 20:34 -0300.
**Timing caveat:** snapshot taken ~4 min after registry write — an early-wave baseline, not a pre-dispatch image. At census time all four canonical repos and all three worktrees show 0 `status --short` lines (lanes had not yet landed `.shokunin/<lane>/` writes). §6 re-verify commands close the gap at integration.

Wave shape (from `spec.json`): 26 items — 8 seats × 3 domain lanes (audio r63, game-dev-2d r62, game-dev-3d r71) + XConnector + XSentinel.

## 1. Contamination baseline — `git status --short` + HEAD

| repo | HEAD | branch→upstream | `status --short` |
|---|---|---|---|
| `~/Projects/shokunin/audio-shokunin` | `3c96a69fcf298f60d53023225d9b268e8f625410` | `main...origin/main` (ahead 2) | clean (0 lines) |
| `~/Projects/shokunin/game-dev-2d-shokunin` | `08d80dc0e7a74a6a26c7ed4d50f9fcc5341b95fd` | `main...origin/main` (ahead 2) | clean (0 lines) |
| `~/Projects/shokunin/game-dev-3d-shokunin` | `9458c183988c8428503b9287d51cd86f7a48378b` | `main...origin/main` (ahead 3) | clean (0 lines) |
| `~/Projects/shokunin` (fleet root) | `79d580b1a4cbde471f160b8f913a13db24e774f4` | `master` (no upstream; `origin/master` exists at `9bdb31b`, 4 behind) | clean (0 lines). HEAD = parent's 20:34:25 w2 spec+dispatch+registry commit |

HEADs are the parent's between-wave integration commits: audio `3c96a69` "audio r62 adjudication" (20:25:15), g2d `08d80dc` "r61 adjudication" (20:26:36), g3d `9458c18` "r70 adjudication" (20:28:10) — all pre-dispatch (20:34). Expected-shape reading: in-flight lane deltas this wave will be untracked `corpus/live/r63-*` / `r62-*` / `r71-*` scratch plus `reports/round-{63,62,71}/` paths landed through the symlinks; anything else — or any tracked-path modification — is contamination.

Worktree-side baseline (`~/Projects/prymeagnt/<lane>` — independent repos, `rev-parse --show-toplevel` = itself):

| worktree | HEAD | branch | status |
|---|---|---|---|
| `~/Projects/prymeagnt/audio` | `8ec47838a5400bac6b5e2f403b237be10ab708e9` | `craft/audio-r1` | clean (0 lines) |
| `~/Projects/prymeagnt/game-dev-2d` | `fe4bbeaf1818865f500cc851657a13643bd706db` | `craft/game-dev-2d-r1` | clean (0 lines) |
| `~/Projects/prymeagnt/game-dev-3d` | `e1e863c3f755247523d1d694216fce69d4353249` | `craft/game-dev-3d-r1` | clean (0 lines) |

Parent `~/Projects/prymeagnt` repo: HEAD `a605f31fbaa22096b84d56a43e434a1913288a4f`, clean (0 lines); lane dirs `.gitignore`d (`/audio/`, `/game-dev-2d/`, `/game-dev-3d/`, …). Fleet root `.gitignore` = `*-shokunin/` — lane repos are nested-ignored (no submodules: `git submodule status` empty), so root cleanliness does not cover lane internals; per-repo rows above do.

## 2. `.shokunin/<lane>` symlink resolution — VERIFIED

```
audio       -> ../../../shokunin/audio-shokunin       -> realpath /home/vgpnk/Projects/shokunin/audio-shokunin       (.git present)
game-dev-2d -> ../../../shokunin/game-dev-2d-shokunin -> realpath /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin (.git present)
game-dev-3d -> ../../../shokunin/game-dev-3d-shokunin -> realpath /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin (.git present)
```

Committed-vs-live: `git -C <worktree> show HEAD:.shokunin/<lane>` == `readlink` for all three — **MATCH ×3**. A retargeted symlink would silently redirect every `.shokunin/<lane>/**` write out of the canonical repo; worktree `status` clean + committed==live means currently intact. Re-check at integration (§6). Sibling `.shokunin/{MANIFEST.json,mints/,reports/}` are worktree-repo content, not through the symlink — consistent with prior rounds.

## 3. Credential-material sweep — in-wave lanes CLEAN; all hits benign-classified

Method (paths-only output; **no values printed anywhere**): ripgrep `files_with_matches` plus GNU `grep -rEl`/`grep -rEil` (descends hidden dirs, ignores gitignore) over each repo excluding `.git`; strict shapes: `op://`, `BEGIN * PRIVATE KEY`, `gh[pousr]_{20+}`, `github_pat_{20+}`, `AKIA…{16}`, `xox[bsp]-{10+}`, `sk-{20+}`, `AIza…{35}`, `Bearer …{20+}`; generic assignment tier: `(api_key|apikey|secret|password|passwd|passphrase|private_key|access_token|auth_token|refresh_token|client_secret|credential)\s*[:=]` (ci); plus `find` for secret-named files (`*.pem *.key *.p12 *.pfx id_rsa* *credential* .env* *.keystore .npmrc .netrc *secret* *token*`) and hidden-file inventory.

**audio-shokunin** (10,801 files): strict = 0. Generic = 1 file: `corpus/live/r63-boundary/src/sox_ng/issues/issues.sh` — vendored SoX-ng issue-tracker helper (POSIX sh, 1632 lines). Masked-context check: `password=` is CLI-param plumbing — empty default `password=` (l.197), `password="$2"` arg assignment (l.246,249), interactive `read -r password` (l.309), help prose (l.114). No literal. **Benign — upstream vendored param name.**

**game-dev-2d-shokunin** (71,016 files): strict = 13 files, all `corpus/live/**/out|export/fixture.x86_64` — `file`: ELF 64-bit stripped executables (Godot export fixtures). Each contains exactly **14 scattered PEM marker strings** (`BEGIN/END [RSA|EC|ENCRYPTED ]PRIVATE KEY`) in non-contiguous string-table order (END-before-BEGIN sequences) — TLS-library format-string constants linked into the export template, not key blobs (no contiguous BEGIN+base64+END block; identical 14-marker set across all 13). Generic = 0. **Benign — compiled-binary crypto-lib residue.**

**game-dev-3d-shokunin** (5,211 files): strict = 0, generic = 0. **Clean.**

**~/Projects/shokunin fleet root** (932 root-owned files, `*-shokunin/` excluded from this pass): all strict hits are documentation, decomposed and length-verified:
- `op://` — ~15+ files under `.ufo/reports/` (kagi round reports, AGGREGATE) and `.ufo/waves/` (scratch/seat docs incl. prior `x-sentinel.md`): prose mentions of the 1Password ref scheme.
- `github_pat_` — 14 files; `github_pat_[A-Za-z0-9_]{20,}` full-token-shape count = **0 in every file** (bare-prefix pattern mentions only).
- `gh[pousr]_[A-Za-z0-9]{20,}` — 2 files: `.ufo/waves/round-9/corpus-gate.mjs:660` is the **declared synthetic fixture** (in-file label "A synthetic sample token appears here: … never real"); `.ufo/waves/aggregator-r11/seats/sentinel.md:19` quotes it in its own adjudication. Previously adjudicated INFO — same verdict here.
- `BEGIN * PRIVATE KEY` — `.ufo/waves/round-9/seats/sentinel-scope.md` (detection-pattern table entry).
- `xox[bsp]-` — 1 bare-prefix mention in `.ufo/waves/round-12/sentinel-trust.md`; real-shape `xox[bsp]-…{10+}` count = 0.
- `AKIA`, `AIza`, `sk-{20+}`, real `Bearer …{20+}` — **zero hits fleet-wide.**

Generic tier in root: prose/doc mentions (`.ufo/waves/kaidoku-r4/06-1password-asar.md` — a 1Password-asar audit doc; prior sentinel reports describing this very sweep). No live secret assignment observed.

**Non-wave lane repos** (inside root, not dispatched this wave — swept for completeness): strict hits are **exclusively `op://`** in secrets-tooling knowledge/lessons/tooling files — kagi-shokunin ×30 files (`corpus/knowledge/op-*`, `op-ref-probe.sh`, `transcript-scan.sh`, `surface-census.sh`, aggregator-audit lessons), kasegi ×4, kotoba ×4, kake ×3, kengaku ×2, kumitate ×2; kaidoku/kama/lore/revenger ×0. Generic hits likewise doc/config-shape (kumitate `api_key = ""` empty literal in `kimi-config-plane.md`, `secret: true` flags in `kimi-census.mjs`, `user:pass@127.0.0.1` local fixture in `kama-shokunin/tools/test-snapshot.sh:80`). Same classes the prior sentinel's F2 adjudicated INFO — no new shapes.

**Secret-named files: none in any swept tree.** Hidden files are all `.gitignore`/`.gdignore`/`.gitkeep`/`.package-lock.json` markers.

**Verdict: no credential-shaped material anywhere that is a real secret.** Every strict hit resolves to (a) pattern documentation, (b) the declared-synthetic corpus-gate fixture, or (c) TLS constant strings in compiled fixtures.

## 4. Identity, remotes, push evidence

- **Effective identity** (all 4 canonical repos): `user.name=ci`, `user.email=ci@local` — from **global** config (`git config --local` empty everywhere; `--global user.name=ci`). HEAD-commit authorship is per-identity and attributable: `audio-shokunin <audio@shokunin.local>`, `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`, `game-dev-3d-shokunin <game-dev-3d@shokunin.local>`, `shokunin-fleet <fleet@shokunin.local>` (author==committer on all four HEADs). No `credential.helper` configured (local or global).
- **Remotes:** lane repos `origin` → `https://github.com/VeigaPunk/shokunin-{game-audio,godot-2d,3d-engines}.git`; root → `shokunin.git`. HTTPS, no userinfo. Each prymeagnt worktree repo additionally carries **all 13 `prymeagnt-*` remote definitions** (push-capable addressing to every sibling lane remote + `origin`→prymeagnt.git) — persists from last wave.
- **Push during wave: NONE — two independent lines of evidence.**
  1. Reflog: `update by push` entry counts identical to last wave's census — **4 per lane repo** (`logs/refs/remotes/origin/main`), **8 for root** (`origin/master`). Newest push epochs: lanes 1791921890/892/893 (17:04:50–53 -0300), root 1791921920 (17:05:20) — all pre-wave (dispatch 20:34).
  2. Live remote state (`git ls-remote`, 10s probe, all reachable): remote tips equal local remote-tracking refs exactly — audio `1c52c7d`=`origin/main`, g2d `3ee05ff`=`origin/main`, g3d `e054cfe`=`origin/main`, root `9bdb31b`=`origin/master`. Any in-wave push would have advanced both.
- **Unpushed local work (operator-owned, consistent):** lanes ahead of `origin/main` by 2/2/3 commits (prior wave's work+adjudication, committed locally 20:25–20:28), root ahead of `origin/master` by 4 (prior integration + this wave's spec commit). No `FETCH_HEAD` in lane repos (never fetched); root `FETCH_HEAD` mtime 16:42 (pre-wave). Remote tips lag local by exactly these parent-integration commits — flag for operator, not a violation.

## 5. Findings (severity / path / evidence / remediation)

**F1 — MEDIUM, RECURRING (latent capability, still no evidence of use).** `gh auth status`: `Logged in to github.com account VeigaPunk (keyring)`, token `gho_…` (masked), scopes `'gist','read','org','repo','workflow'`, protocol https. Any lane shell that can exec `gh` holds repo+workflow authority over every `VeigaPunk/*` remote — `gh auth token`, `gh api` mutate — while the no-push rule is policy-only. Persists from last wave's F1 unchanged; `op` at `/usr/bin/op`; `SSH_AUTH_SOCK=/run/user/1000/ssh-agent.socket` live (remotes are HTTPS — not directly git-usable). No credential.helper, so bare `git push` still needs interactive auth — `gh` does not. Empirical check this wave: remote tips == remote-tracking refs (§4) — capability unexercised so far. Smallest remediation (unchanged): launch lanes with `GH_CONFIG_DIR` pointed at an empty dir / `gh` off lane PATH / `SSH_AUTH_SOCK=` unset, or keep the declared-fact posture and re-run §6 at integration.

**F2 — INFO (recurring, previously adjudicated).** Committed `op://<seg>/<seg>/<seg>` refs persist and grew: kagi-shokunin corpus now 30 files (was ×17 refs/6 files last wave) plus kasegi/kotoba/kake/kengaku/kumitate corpus knowledge+lessons. All are secrets-mechanism docs/probe vectors in the lanes whose province is that mechanism; no values involved. Smallest remediation (unchanged): record the kagi-province exemption explicitly or redact path segments. Sentinel does not adjudicate.

**F3 — INFO (recurring hygiene).** Fleet root `master` still has no upstream (`branch -vv` bare; `origin/master` at `9bdb31b`, 4 behind). `status -sb` never shows ahead/behind for root. Fix: `git -C ~/Projects/shokunin branch --set-upstream-to=origin/master master` (operator-owned).

**F4 — INFO (new this wave, integration-relevant).** Remote tips lag local: lanes `origin/main..HEAD` = 2/2/3, root `origin/master..HEAD` = 4 — all parent integration commits (prior-wave adjudications + w2 spec). Push remains operator-owned and pending; integration receipts should record local-only state, not assume pushed parity.

**F5 — INFO (verified-holding).** `.shokunin/<lane>` symlinks committed==live ×3 (§2); 13-remote push-capable addressing in each worktree (§4) — capability, no use evidence (worktrees clean, lane reflogs unchanged).

## 6. Integration-time re-verify (parent, cheap)

```bash
for r in audio-shokunin game-dev-2d-shokunin game-dev-3d-shokunin; do
  git -C ~/Projects/shokunin/$r status --short                        # only corpus/live/r{63,62,71}-* + reports/round-* declared shapes
  git -C ~/Projects/shokunin/$r rev-parse HEAD                        # compare §1 baseline HEADs
  wc -l < ~/Projects/shokunin/$r/.git/logs/refs/remotes/origin/main   # must stay 4
  git -C ~/Projects/prymeagnt/${r%-shokunin} status --short           # clean ⇒ worktree tracked files + symlink intact
  git -C ~/Projects/prymeagnt/${r%-shokunin} show HEAD:.shokunin/${r%-shokunin}  # must equal live readlink
done
git -C ~/Projects/shokunin status --short                             # root: only .ufo/waves/shokunin-train-20261013-w2 artifacts
timeout 10 git -C ~/Projects/shokunin/audio-shokunin ls-remote origin refs/heads/main  # tip must still equal origin/main
```

## 7. Limits

Point-in-time read at 20:38 -0300 (~4 min post-registry) while lanes run; post-sweep mutation needs §6 re-checks. Remote reachability probed read-only via `ls-remote` (all 4 answered within 10s). Sweep is shape-based — high-entropy values matching no pattern are not detectable by grep; `grep -r` covered hidden+gitignored paths but not `.git` internals beyond reflog/config reads. Env observed in my own shell only (no `GH_TOKEN`/`GIT_ASKPASS`/`GIT_CONFIG_*`/`AWS_*`/`OPENAI*`/`ANTHROPIC*` set); lane-process environments may differ.
