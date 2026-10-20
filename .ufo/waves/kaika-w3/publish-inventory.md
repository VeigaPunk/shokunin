# Kaika Publish Inventory — 25 repos (read-only, 2026-10-19)

Method: `git ls-remote --heads <push-url> refs/heads/<dest>` per repo (concurrency 8, normal git auth helper). No fetch, no push, no repo file changes. URLs sanitized to host/owner/repo; verified no userinfo/tokens in any configured URL; no `url.*.insteadOf` rewrites in any repo. Machine-readable detail: `local://kaika-publish-inventory.json`.

## Global findings
- **Push remote**: all 25 resolve `origin` via `upstream_remote` fallback; no `branch.<name>.pushRemote`, no `remote.pushDefault` configured anywhere. No absent/ambiguous push remotes.
- **Destination branch**: from `branch.<name>.merge`; equals local branch name in all 25. No detached HEADs. Every upstream configured, every destination branch present on remote live.
- **All remotes in context**: every sanitized destination is `github.com/VeigaPunk/<repo>`. No remote outside owner/contextVeigaPunk. No credential values printed (helpers present, values withheld).
- **Duplicate push destinations**: none — 25 distinct repo:branch destinations.
- **ls-remote errors**: none.

## Table
| id | branch | HEAD | destination (github.com/VeigaPunk/) | live remote OID | vs live | vs tracking (a/b) | relation |
|---|---|---|---|---|---|---|---|
| fleet | master | 54a20d39c | shokunin:master | 31baf5cb0 | ahead 69 | 69/0 | remote ancestor → FF |
| audio | main | 63593ded4 | shokunin-game-audio:main | e2187f6ab | **UNVERIF** | 10/0 (stale) | live OID absent locally |
| chousa | master | d730ae4c3 | chousa-shokunin:master | ab19cff53 | ahead 3 | 3/0 | remote ancestor → FF |
| game-dev-2d | main | 7461a0868 | shokunin-godot-2d:main | 5f87de7df | **UNVERIF** | 7/0 (stale) | live OID absent locally |
| game-dev-3d | main | 3118be0b1 | shokunin-3d-engines:main | 7c4e5897d | ahead 4 | 4/0 | remote ancestor → FF |
| kagi | master | 1e9e67ff3 | kagi-shokunin:master | c03e12c06 | **UNVERIF** | 3/0 (stale) | live OID absent locally |
| kaidoku | main | 767adafb9 | shokunin-reverse-engineering:main | de77d7545 | ahead 7 | 7/0 | remote ancestor → FF |
| kake | master | 7e17c663b | kake-shokunin:master | 7c9f28fce | **UNVERIF** | 3/0 (stale) | live OID absent locally |
| kama | master | 03b5f0e8b | kama-shokunin:master | 893e3c5d4 | **UNVERIF** | 7/0 (stale) | live OID absent locally |
| kasegi | master | 13a519200 | kasegi-shokunin:master | 3bd13fa41 | **UNVERIF** | 2/0 (stale) | live OID absent locally |
| kengaku | master | a42bb40c1 | kengaku-shokunin:master | dc0e59441 | **UNVERIF** | 4/0 (stale) | live OID absent locally |
| kotoba | master | c61a973b2 | kotoba-shokunin:master | 78ee57e5e | ahead 3 | 3/0 | remote ancestor → FF |
| kotodama | main | 4ad268365 | kotodama-shokunin:main | c42d675be | ahead 6 | 6/0 | remote ancestor → FF |
| kumitate | master | a5683a96c | kumitate-shokunin:master | 72d9ccda9 | **UNVERIF** | 6/0 (stale) | live OID absent locally |
| lore | main | 6e804e2e5 | shokunin-world-bible:main | dbdd5facb | **UNVERIF** | 7/0 (stale) | live OID absent locally |
| mado | master | e3e6a8e6c | mado-shokunin:master | 8e0c9b264 | **UNVERIF** | 10/0 (stale) | live OID absent locally |
| mori | master | bf7cdc478 | mori-shokunin:master | b2e1ca2dd | **UNVERIF** | 3/0 (stale) | live OID absent locally |
| revenger | main | cf0241927 | shokunin-binary-forensics:main | 8bbcb4e32 | ahead 5 | 5/0 | remote ancestor → FF |
| souji | master | 31984f473 | shokunin-repo-hygiene:master | dcc8b9e83 | ahead 4 | 4/0 | remote ancestor → FF |
| tabi | master | 9bc89bfe7 | tabi-shokunin:master | 25f64835a | **UNVERIF** | 5/0 (stale) | live OID absent locally |
| tameshi | master | a21e91047 | tameshi-shokunin:master | 3fb55acd1 | **UNVERIF** | 4/0 (stale) | live OID absent locally |
| tsukuroi | master | d8ec15d5e | tsukuroi-shokunin:master | 8148201b2 | **UNVERIF** | 5/0 (stale) | live OID absent locally |
| canonical | main | e737d2ea9 | kimi-shokunin:main | b3ca98f93 | ahead 1 | 4/0 (stale) | remote ancestor → FF |
| omp-binding | main | b8c699c08 | ompskills:main | 344e1cb26 | ahead 2 | 2/0 | remote ancestor → FF |
| retired-kimi-mirror | main | 1c5e0a552 | myskills:main | fd9ed8c48 | ahead 1 | 1/0 | remote ancestor → FF |

## Push-readiness classes
- **FF-verified vs live (11)**: fleet, chousa, game-dev-3d, kaidoku, kotoba, kotodama, revenger, souji, canonical, omp-binding, retired-kimi-mirror — live remote OID is an ancestor of local HEAD; plain push fast-forwards.
- **UNVERIF (14)**: audio, game-dev-2d, kagi, kake, kama, kasegi, kengaku, kumitate, lore, mado, mori, tabi, tameshi, tsukuroi — live remote OID is **not present in the local object store** and local tracking refs are stale (live ≠ tracking). These remotes advanced with commits the local clones never fetched. Ahead/behind vs live cannot be computed without a fetch; a plain push is expected to be rejected non-fast-forward, and `--force-with-lease` is unsafe against stale local tracking refs (lease would compare to the stale value). Parent must refresh (fetch) these 14 before pushing. `git ls-remote` alone cannot rule out divergence.

## Notes for parent
- Initial HEADs above are cutoff metadata; scope `base` equals the live remote OID in 9 repos (fleet, chousa, game-dev-3d, kaidoku, kotoba, kotodama, revenger, souji, retired-kimi-mirror); canonical and omp-binding live OIDs advanced past their recorded base; the other 14 have live OIDs absent locally so base-vs-live equality is false-but-unverifiable.
- Worktrees with uncommitted/untracked entries (not modified): game-dev-3d (79), lore (26), omp-binding (5), retired-kimi-mirror (3), kama (2).
- canonical: HEAD e737d2ea9 matches context "canonical main e737d2e"; omp-binding b8c699c08 and retired-kimi-mirror 1c5e0a552 match recorded host-binding/retired-mirror commits. audio: HEAD is 10 ahead of its stale local tracking ref; exact ahead/behind vs live e2187f6ab is uncomputable without a fetch.
