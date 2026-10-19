# kaika W2j — credential exposure under colocated jj (SENTINEL)

Verdict: **safe-with-config**. No sensitive-named file is untracked-and-unignored today. The 107 untracked-and-unignored files in 3 repos would all be snapshotted by jj on first use. None is credential-named, but their contents were not inspected (out of scope). Top hazard: `.tower/` in the fleet root is ignored only by `.git/info/exclude`, which is not versioned.

Scope: fleet root `/home/vgpnk/Projects/shokunin`, all 21 `*-shokunin` lanes, and `/home/vgpnk/Projects/kimi-shokunin` (23 repos). Read-only. No file contents were read or printed. No jj command was run inside any live repo. No scratch clone was created.

## 1. Untracked-but-not-ignored, sensitive-looking names

Command: `git -C <repo> ls-files -o --exclude-standard -z` then `stat -c '%a %s'` on each absolute path. Name regex: `\.env`, `.pem`, `.key`, `.p12`, `.pfx`, `id_rsa|ed25519|ecdsa|dsa`, `secret`, `credential`, `passw`, `.netrc`, `.npmrc`, `.pypirc`, `.service`, `shim`, `api[_-]?key`, `.kdbx`, `token`.

Result: **0 matches out of 107 files**.

| repo | files | modes (count) | total bytes | max bytes | branch |
|---|---|---|---|---|---|
| game-dev-3d-shokunin | 79 | 644:52, 755:27 | 850,589 | 38,890 | main |
| kama-shokunin | 2 | 644:2 | 6,124 | 4,413 | master |
| lore-shokunin | 26 | 644:25, 755:1 | 218,489 | 34,095 | main |
| all other 20 lanes, fleet root, kimi-shokunin | 0 | — | — | — | — |

Only these three repos have any untracked-and-unignored file. Their largest files (`reports/round-107/r107-scribe-report.md`, `.scratch/*/tools/dependency-freeze-contract.json`, `reports/round-107/mutations/gate-draft.sh`) are far below jj's 1 MiB limit, so the size limit does not exclude any of them.

Names that look like "scratch" but are not credential-named, with contents not inspected: `lore-shokunin/.scratch/v26/poll.log`, `lore-shokunin/.scratch/v26/poll.sh`, `kama-shokunin/.ufo/round-10/plan.json`, `kama-shokunin/.ufo/round-10/SEAT-PROTOCOL.md`. A log could carry tokens regardless of name. Content scanning is a follow-up that needs its own assignment.

## 2. What prevents snapshotting: jj settings in effect

- `jj config get snapshot.auto-track` → `all()` (default). Nothing excludes files from auto-track.
- `jj config get snapshot.max-new-file-size` → `1MiB` (default).
- `jj config list --user` → only `user.name`, `user.email`, `ui.default-command`, `git.auto-local-bookmark`. No `snapshot.*` key.
- No `core.excludesFile` (`git config --show-origin -l` shows no exclude/ignore entries).
- Per-repo `.git/info/exclude`: 0 rules in game-dev-3d, kama and lore. Root `.gitignore`: none in game-dev-3d, 1 rule in kama, 5 in lore.

So for the 107 files, **no rule prevents snapshotting**. The only protection is that they are not credential-named.

Docs (jj 0.45 docs, via search index: https://docs.jj-vcs.dev/latest/working-copy/ and https://docs.jj-vcs.dev/latest/config/): auto-track `all()` default; `.gitignore` honored in every directory, plus `$XDG_CONFIG_HOME/git/ignore` and `$GIT_DIR/info/exclude`; files over `snapshot.max-new-file-size` skipped; `jj file track --include-ignored` overrides ignore rules (CLI reference / changelog 0.35.0).

## 3. Sensitive-named files that ARE ignored, and the rule that protects each

Command: `git -C <repo> ls-files -o -i --exclude-standard`, filtered by the same regex, then `git check-ignore -v --stdin`.

| repo | count | ignore rule (file:line → pattern) | examples (names only) |
|---|---|---|---|
| fleet root `shokunin` | 8 | `.git/info/exclude:8` → `.tower/` | `.tower/comms/findings/*-r18-*shim*…md` (8 files, names include "live-api-keys-sit-in-plaintext", "legorder-vuln-…credentials-are-plaintext-defaults-in-shim") |
| fleet root `shokunin` | 4 | `.gitignore` → `.ufo/waves/*/*-scratch/` | `.ufo/waves/shokunin-train-2026101{3,4}-w{5,8,9}/xsentinel-scratch/secrets-scan.txt`, `secrets-tracked.txt`, `secrets-untracked.txt`, `secrets.txt` |
| `kotodama-shokunin` | 43 | `.gitignore` → `.scratch/` | includes `.scratch/.ufo/waves/.../xsentinel-scratch/secrets-*.txt` (nested copy), `.scratch/*/outside-secret.txt` (8 bytes each, test fixtures), `.scratch/x03/fixtures/*_tokens.json` |
| `kaidoku-shokunin` | 35 | `.ufo/waves/arc3-loop1-round4/tools/vyper-venv/.gitignore` → `*` | all inside the venv; false positives (`Crypto/Protocol/SecretSharing.py`, `asttokens`) |
| `souji-shokunin` | 2 | `tests/vault/vadv-49/.gitignore:2` → `shims/` | `tests/vault/vadv-49/shims/electron43`, `shims/obsidian` (mode 755, 100 bytes each) |

Mode/size of the `secrets-*.txt` files in shokunin: 644; 157 B, 1,125 B, 1,400 B, 6,617 B. These are world-readable but ignored, so jj will not snapshot them. The `.gitignore` glob `.ufo/waves/*/*-scratch/` only protects files in directories whose name ends in `-scratch`.

## 4. Tracked sensitive-named files (outside the untracked scope, noted for completeness)

These are already in git history. jj does not change their exposure, but they should be reviewed by the repo owner:
- `souji-shokunin/tests/fixtures/case-F10/app.env` — TRACKED, mode 600, 138 B
- `souji-shokunin/tests/fixtures/case-F10/creds.pem` — TRACKED, mode 600, 132 B

Many other tracked hits matched `token` (LLM and Solidity terms) or `1password` in doc names. These are false positives and not listed.

## 5. Hazards

1. **Auto-track is unconditional for the 107 files.** The first `jj` command in game-dev-3d, kama or lore snapshots all 107 into the working-copy commit. Owners should commit, ignore, or remove them before adoption. [INFERENCE]: they are only pushed if a bookmark points at that commit, so `jj git push` of bookmarks does not send them unless one is set.
2. **`.tower/` protection is unversioned.** It lives only in `.git/info/exclude`. A fresh clone or `git init` of the fleet root drops the rule. `.tower/comms/findings/` holds plaintext-credential findings. Fix: move the rule into a versioned `.gitignore`. Do not rely on `.git/info/exclude` alone.
3. **`jj file track --include-ignored` bypasses ignore rules.** It is a manual override, but any operator or script using it on the fleet root would expose the ignored `.tower/` and `secrets-*.txt` files.
4. **World-readable secrets-named scratch files** (mode 644) under `*-scratch/` directories. Not a jj issue; a local-permission issue.

## 6. Required config (recommendations, not applied)

- Keep `snapshot.auto-track` at default `all()` only after the 107 files are dispositioned.
- Optional repo-level exclusion, if needed: `jj config set --repo snapshot.auto-track 'all() & ~glob:"**/secret*"'` [INFERENCE: pattern syntax not validated here; per docs pksunkara example uses `all() & ~foo.txt`]. Test in a scratch clone first.
- Move `.tower/` into a versioned `.gitignore` in the fleet root.

## 7. Not done / residual

- Contents of any file were not read. Name-based screening cannot prove the 107 untracked files are free of secrets.
- No scratch clone was created and no gates were run; that is outside this read-only assignment.
- My temporary files in `/tmp` (`kaika-w2j-*`) were deleted after use.
