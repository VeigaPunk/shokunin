# X-Sentinel — invariant sweep, wave shokunin-train-20261013

Seat: sentinel (LEAF, read-only on repos; this file is my only write).
Sweep executed: 2026-10-13 19:01:12 -0300 (22:01:12 UTC), `date -u +%s` = 1791928936.
Wave dispatch `dispatch.json` mtime 2026-10-13 18:55:50.712 -0300; `swarm-registry.json` 18:58:58.691 -0300.
**Timing caveat:** lanes were already working when this snapshot was taken (~6 min after dispatch). This is an early-wave baseline, not a literal pre-dispatch image; the contamination deltas below are the declared scratch dirs observed in flight. The integration-time re-verify commands in §6 close the gap.

## 1. Contamination baseline — `git status --short` + HEAD

| repo | HEAD | branch→upstream | `status --short` |
|---|---|---|---|
| `~/Projects/shokunin/audio-shokunin` | `1c52c7d074ed693f9d4ea98e5f9fea4cc204c8cd` | `main...origin/main` | `?? corpus/live/r62-boundary/` (1 line) |
| `~/Projects/shokunin/game-dev-2d-shokunin` | `3ee05ff5f47f6d1716b7012fc44b711d24387592` | `main...origin/main` | `?? corpus/live/r61-baseline/` + `?? corpus/live/r61-reviewer/` (2 lines) |
| `~/Projects/shokunin/game-dev-3d-shokunin` | `e054cfee74dea96cfd21cfbbfc9fdd4ac74a426b` | `main...origin/main` | clean (0 lines; `reports/round-70/` exists but is empty — invisible until it holds files) |
| `~/Projects/shokunin` | `3478bb7b7deea0a9f50aa3ef26d2bdd6babcf0c1` | `master` (no upstream configured; `origin/master` exists) | clean (0 lines). HEAD itself is the parent's 18:58:58 wave-registry commit: "wave shokunin-train-20261013: 26-lane training wave spec+dispatch+registry (audio r62 / g2d r61 / g3d r70)" |

Expected-shape reading: the only in-flight deltas are untracked dirs matching declared lane scratch (`r62-*` audio, `r61-*` g2d) under each repo's own `corpus/live/`. At integration, anything else under a lane repo — or any tracked-path modification — is contamination.

Worktree-side baseline (`~/Projects/prymeagnt/<lane>` — each is an independent repo; `rev-parse --show-toplevel` = itself):

| worktree | HEAD | branch | status |
|---|---|---|---|
| `~/Projects/prymeagnt/audio` | `8ec47838a5400bac6b5e2f403b237be10ab708e9` | `craft/audio-r1` | clean (0 lines) |
| `~/Projects/prymeagnt/game-dev-2d` | `fe4bbeaf1818865f500cc851657a13643bd706db` | `craft/game-dev-2d-r1` | clean (0 lines) |
| `~/Projects/prymeagnt/game-dev-3d` | `e1e863c3f755247523d1d694216fce69d4353249` | `craft/game-dev-3d-r1` | clean (0 lines) |

Parent `~/Projects/prymeagnt` repo is also clean (0 lines); lane dirs are `.gitignore`d nested repos (`/audio/`, `/game-dev-2d/`, `/game-dev-3d/` in `~/Projects/prymeagnt/.gitignore`). Same pattern at fleet root: `~/Projects/shokunin/.gitignore` = `*-shokunin/` — lane repos are nested-ignored, so root `status` cleanliness does not cover lane internals; per-repo checks above do.

## 2. `.shokunin/<lane>` symlink resolution — VERIFIED

```
audio       -> /home/vgpnk/Projects/shokunin/audio-shokunin       (realpath match YES)
game-dev-2d -> /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin (realpath match YES)
game-dev-3d -> /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin (realpath match YES)
```

Each `.shokunin/<lane>` is a **tracked** gitlink-free symlink (mode `120000`) inside its worktree repo. `git show HEAD:.shokunin/<lane>` == live `readlink` for all three (`../../../shokunin/<lane>-shokunin`, MATCH ×3). A lane retargeting this symlink would redirect every `.shokunin/<lane>/**` write; worktree `status` clean ⇒ currently unmodified. Re-check at integration with the same one-liner.

Sibling files `.shokunin/{MANIFEST.json,mints/,reports/round-*/<lane>.md}` (64/62/71 tracked paths) live in the worktree repo, not through the symlink — consistent with history: `reports/round-N/<lane>.md` are the tracked per-round lane reports in prymeagnt-land.

## 3. Credential-material sweep — lane corpora CLEAN; root hits all benign-classified

Method (paths-only output; no values printed anywhere): `rg --hidden --no-ignore -l --glob '!.git/**'` per repo, tier-1 shapes (`op://`, `BEGIN * PRIVATE KEY`, `AKIA…`, `gh[psour]_…`, `github_pat_…`, `sk-…20+`, `xox[bspra]-…`, `AIza…`, JWT `eyJ…`) and tier-2 assignments (`(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token|bearer|private[_-]?key)\s*[:=]`, case-insensitive), plus `find` for credential-named files (`*.pem *.key id_rsa* id_ed25519* .env* .netrc .npmrc .pypirc *credential* *secret* *.keystore`).

- **audio-shokunin, game-dev-2d-shokunin, game-dev-3d-shokunin: ZERO hits on all three sweeps.** Clean, including the in-flight `corpus/live/r6*/` untracked dirs (covered by `--no-ignore`).
- **~/Projects/shokunin (fleet root):** hits decompose into three classes, all evidence-checked with values masked:
  - (a) **Detection tooling / self-referential meta** — sentinel reports, corpus-gate scripts, wave specs and my own task file quoting the very patterns swept (e.g. `.ufo/waves/shokunin-train-20261013/{dispatch.json,spec.json,tasks/XSentinel.txt}` each `op://`×1 — the sweep brief itself).
  - (b) **Documented synthetic fixtures** — `ghp_` at `.ufo/waves/round-9/corpus-gate.mjs:660` is labeled "never real" in-file and is already disclosed by `.ufo/waves/aggregator-r11/seats/sentinel.md:19` (along with `Bearer jt-test-pw` test literal); `PRIVATE KEY` at `.ufo/waves/round-9/seats/sentinel-scope.md:20` is a detection-regex literal in a pattern table.
  - (c) **kagi-lane mechanism documentation** — kagi's province is the secrets-tooling surface; `op://` strings there are probe vectors and redaction-policy documentation (see Finding B).

Tier-2 hits in root are all prose/config-shape mentions: `OPENCODE_SERVER_PASSWORD=` empty-set semantics docs, `api_key = ""` **empty** literals in `kumitate-shokunin/corpus/knowledge/kimi-config-plane.md`, `secret: true` metadata flags in `kumitate-shokunin/scripts/kimi-census.mjs`, `http://user:pass@127.0.0.1` local fixture in `kama-shokunin/tools/test-snapshot.sh:80`. No live secret assignment observed. Credential-named files: only `kumitate-shokunin/corpus/knowledge/kimi-binary-secrets.md` and `kagi-shokunin/corpus/knowledge/credential-isolation.md` — knowledge docs by name, not secret files.

**No secret values found in any swept tree.** Commands and hit inventories are reproducible from §3 method; masked line evidence retained above for the three token-shape hits.

## 4. Identity, remotes, push evidence

- **Identity:** all four canonical repos — effective `user.name=ci`, `user.email=ci@local` (no repo-local override; inherited). `~/Projects/prymeagnt` local override: `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`. Lane worktrees inherit prymeagnt-local or global `ci` per repo — uniform, attributable.
- **Remotes:** lane repos each carry `origin` → `https://github.com/VeigaPunk/shokunin-{game-audio,godot-2d,3d-engines}.git`; root → `shokunin.git`. No userinfo in any URL (verified via `remote -v` with userinfo-redacting sed — nothing to redact). Each prymeagnt worktree repo carries **all 13** `prymeagnt-*` remotes (lane-local config lists every sibling's URL — push-capable addressing, not just own-lane).
- **Push during wave: NONE.** `grep -rn 'update by push' <lane>/.git/logs/` — all four entries per lane repo are pre-wave: `1791920493–1791921893` epoch = 16:41:33–17:04:53 -0300; wave dispatch 18:55:50. `git rev-list --count origin/main..HEAD` = **0** for all three lanes (`origin/main` == HEAD). No `FETCH_HEAD` in lane repos (never fetched). Root: `update by push` reflog ends 17:05:20 (pre-wave); `FETCH_HEAD` mtime 16:42; `origin/master..HEAD` = **1** — the parent's own wave-registry commit `3478bb7`, unpushed (push is operator-owned; consistent).
- **Pre-wave pushes existed and were operator actions:** `ci` pushed each lane tip at 16:41–17:05 — consistent with root commit `9bdb31b` "canon lanes public". Historical, not wave activity.

## 5. Findings (severity / path / evidence / impact / smallest remediation)

**F1 — MEDIUM (latent capability, no evidence of use).** `gh` CLI is authenticated host-wide: `gh auth status` → `Logged in to github.com account VeigaPunk (keyring)`, token `gho_…` (masked), scopes `'gist','read:org','repo','workflow'`, protocol https. Any lane shell that can exec `gh` holds full repo+workflow authority over every `VeigaPunk/*` remote — `gh auth token` prints it, `gh api` mutates — regardless of the lane's no-push/no-domain-action instruction, which is policy-only. Additionally `SSH_AUTH_SOCK` is set in this env (agent socket live; remotes are HTTPS so it is not directly git-usable) and `op` is installed at `/usr/bin/op`. No `credential.helper` is configured (local or global), so bare `git push` over HTTPS would still need interactive auth — but `gh` doesn't need the helper. Impact if exercised: unauthorized push/merge/Actions dispatch attributable to the operator account — the exact "domain-facing actions" the brief reserves to the operator. Smallest remediation: launch lanes with `GH_CONFIG_DIR` pointed at an empty dir (or `gh` off the lane PATH) and `SSH_AUTH_SOCK=` unset; or treat gh-presence as a declared lane-environment fact and re-check `update by push`/remote refs at integration (commands in §6).

**F2 — LOW/INFO (contract-text tension, previously adjudicated).** Non-placeholder-shaped `op://<seg>/<seg>/<seg>` refs persist in committed corpus: `kagi-shokunin/corpus/` ×17 across 6 files (`op-ref-probe.sh` ×9, `knowledge/op-ref-consumption.md` ×3, `knowledge/op-env-refs.md` ×1, `transcript-scan.sh` ×2, `surface-census.sh` ×1, `lessons/round-5-aggregator-audit.md` ×1) and ~30 more under `.ufo/reports/round-15/scratch/` and `.ufo/waves/round-9/` (non-corpus). Context-sampled masked: they are `op run` reference-resolution mechanism docs and probe vectors (e.g. `K=op://…` rows in resolution-behavior tables; `op-env-refs.md` documents refs vs raw-value redaction). CORPUS.md literally bars "vault ref paths (`op://…`)… out of every corpus"; kagi corpus names real ref paths because its province is that mechanism. Prior aggregator audits (round-5/9 verdicts) reviewed and left them. No secret values involved — ref paths are metadata. Smallest remediation: parent/aggregator either records the kagi-province exemption explicitly or redacts path segments to `op://<v>/<i>/<f>` in the 17 corpus instances. Sentinel does not adjudicate.

**F3 — INFO (hygiene).** Fleet root `master` has no upstream configured (`status -sb` → `## master`, bare, while `refs/remotes/origin/master` exists at `9bdb31b`, 1 commit behind HEAD). `git status -sb` therefore never shows ahead/behind for root; drift detection relies on explicit `rev-list origin/master..HEAD`. Smallest remediation: `git -C ~/Projects/shokunin branch --set-upstream-to=origin/master master`.

**F4 — INFO (structure, verified-holding).** The `.shokunin/<lane>` symlink is tracked in each worktree repo and currently equals its committed target (§2). A retargeted symlink would route all lane writes out of the canonical repo while `git status` stays clean *inside* the lane repo — the worktree-side status is the detector, and it is clean for all three. Re-verify at integration (§6).

## 6. Integration-time re-verify (parent, cheap)

```bash
for r in audio-shokunin game-dev-2d-shokunin game-dev-3d-shokunin; do
  git -C ~/Projects/shokunin/$r status --short          # only declared corpus/live/r6* scratch + reports/round-*
  git -C ~/Projects/shokunin/$r rev-list --count origin/main..HEAD   # must be 0 before parent commit
  grep -c 'update by push' ~/Projects/shokunin/$r/.git/logs/refs/remotes/origin/main  # must stay 4
done
for d in audio game-dev-2d game-dev-3d; do
  git -C ~/Projects/prymeagnt/$d status --short         # clean ⇒ no tracked worktree mutation, symlink intact
done
```

## 7. Limits

Sweep is a point-in-time read at 19:01 local while lanes run; post-sweep mutations need §6 re-checks. Lane-process environments may carry env I cannot see from this shell (I verified my own env: no `GH_TOKEN`/`GIT_ASKPASS`/`GIT_CONFIG_*`, `SSH_AUTH_SOCK` present). `origin` reachability was not probed (fetch is read but network-touching; out of leaf scope). Credential sweep is shape-based — high-entropy values that match no pattern are not detectable by grep.
