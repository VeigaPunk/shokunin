# Kaika publication record

Operator directives: commit and push; repositories public; merge to main. Each target below is the repository's GitHub default branch (`main` or `master`); all 25 were verified public with the default branch matching the push target.

| id | GitHub repository | default branch | pushed range | visibility |
|---|---|---|---|---|
| fleet | `VeigaPunk/shokunin` | `master` | `31baf5cb..` this commit | public → public |
| audio | `VeigaPunk/shokunin-game-audio` | `main` | `e2187f6a..0462a544` | public → public |
| chousa | `VeigaPunk/chousa-shokunin` | `master` | `ab19cff..d730ae4c` | public → public |
| game-dev-2d | `VeigaPunk/shokunin-godot-2d` | `main` | `5f87de7d..bce53b83` | public → public |
| game-dev-3d | `VeigaPunk/shokunin-3d-engines` | `main` | `7c4e589..3118be0b` | public → public |
| kagi | `VeigaPunk/kagi-shokunin` | `master` | `c03e12c..c2cab35b` | public → public |
| kaidoku | `VeigaPunk/shokunin-reverse-engineering` | `main` | `de77d75..767adafb` | public → public |
| kake | `VeigaPunk/kake-shokunin` | `master` | `7c9f28f..5009ecaa` | public → public |
| kama | `VeigaPunk/kama-shokunin` | `master` | `893e3c5..2f7303c2` | public → public |
| kasegi | `VeigaPunk/kasegi-shokunin` | `master` | `3bd13fa..922a4dde` | public → public |
| kengaku | `VeigaPunk/kengaku-shokunin` | `master` | `dc0e594..6180e4fb` | public → public |
| kotoba | `VeigaPunk/kotoba-shokunin` | `master` | `78ee57e..c61a973b` | public → public |
| kotodama | `VeigaPunk/kotodama-shokunin` | `main` | `c42d675..4ad26836` | public → public |
| kumitate | `VeigaPunk/kumitate-shokunin` | `master` | `72d9ccd..1770305f` | public → public |
| lore | `VeigaPunk/shokunin-world-bible` | `main` | `dbdd5fa..01306d51` | public → public |
| mado | `VeigaPunk/mado-shokunin` | `master` | `8e0c9b2..7dcb785b` | public → public |
| mori | `VeigaPunk/mori-shokunin` | `master` | `b2e1ca2..6531ac60` | public → public |
| revenger | `VeigaPunk/shokunin-binary-forensics` | `main` | `8bbcb4e..cf024192` | public → public |
| souji | `VeigaPunk/shokunin-repo-hygiene` | `master` | `dcc8b9e..31984f47` | private → public |
| tabi | `VeigaPunk/tabi-shokunin` | `master` | `25f6483..f032f2dc` | public → public |
| tameshi | `VeigaPunk/tameshi-shokunin` | `master` | `3fb55ac..18ad5d05` | public → public |
| tsukuroi | `VeigaPunk/tsukuroi-shokunin` | `master` | `8148201..b76b5c37` | public → public |
| canonical | `VeigaPunk/kimi-shokunin` | `main` | `b3ca98f..e737d2ea` | private → public |
| omp-binding | `VeigaPunk/ompskills` | `main` | `344e1cb..b8c699c0` | private → public |
| retired-kimi-mirror | `VeigaPunk/myskills` | `main` | `fd9ed8c..1c5e0a55` | public → public |

## Preflight

- Destinations: 25 distinct `github.com/VeigaPunk/*` targets, no duplicates and no credentials in remote URLs (`publish-inventory.md`).
- Remote advances: 14 repositories had README/wiki-link, LOG and daily-reflection commits not present locally. Each was fetched and merged with a normal two-parent merge. Local LOG bytes stayed an exact prefix, and the remote-only suffix was appended verbatim. Corpus, skill, scorecard and runtime blobs were unchanged (`remote-doc-integrations.json`). No force push or history rewrite.
- Secrets: the 21 child change ranges contained 0 credentials (gitleaks 8.30.1 plus typed patterns, `publish-lane-security.md`). The fleet/canonical/binding/mirror ranges had 0 credential blockers (`publish-core-security.md`). Flagged kasegi engagement identifiers were already public at the remote base.
- Visibility changes: `kimi-shokunin`, `shokunin-repo-hygiene` and `ompskills` were private. Their complete reachable histories were mirrored and scanned (`public-history-scan.json`): canonical had 0 findings. The other two had 6 `generic-api-key` matches, classified as prose labels, a local directory name, a probe id and a deliberate synthetic canary — no credential (`public-history-triage.md`). Only then were the three repositories made public.

## Limits

Scans are rule/pattern based, not a certification. Already-public history contains operator local paths and an email address. Unrelated untracked or staged user work was left uncommitted (game-dev-3d, lore, kama, ompskills, myskills). The fleet-root row is published by pushing the commit that carries this file.
