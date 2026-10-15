# KasegiHistoryClaims — advisory re-census

Seat: `kasegi/HistoryClaims`. Lane: `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. Starting revision from `baselines.json`: `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` (round 20 plan; HEAD still that commit, message `round-19: re-census after second root loss…`). Plan read: `kasegi-shokunin/plans/wwkd-round-20-recensus.md`.

This file is an advisory inventory. It is not a native judge verdict, a lane round report, a receipt, or an admission. No lane file, gate file, LOG, SCORECARD, corpus note, or sibling report was edited. Original LOG and corpus bytes are unchanged. Errata below are drafts for the parent integrator; they are not applied.

Measurement stamp: 2026-10-14T23:37:28Z, plus same-session follow-up probes. Gates (`anchorcheck.py`, `resolve.py`, tests, lint, formatters) were not re-run. Round-19 census numbers are cited as the landed record, not re-measured here.

## Axes

- Freshness: absence of the three lost roots re-checked; the one live relocation pin re-checked against current HEAD; one worktree listing pinned beside that pin has drifted.
- Operability: the documented blob-pin command uses a deleted lowercase path. The blobs themselves still resolve on the uppercase path.
- Calibration: round-19 `[lost-base]` prefixes on `triage-thresholds.md` lost-tree line numbers assert the wrong base. A mirror path in `claim-package-contract.md` carries a past-EOF lost-tree line. Already-landed loss annotations are not re-proposed as repairs.
- Adjacency: the 681-file loss fact lives in the fleet L0 side channel, not in the cited corpus note. `.ufo/` listing drift is UFO-substrate runtime, not a kasegi gate. PROVINCE re-point stays an operator L0 question.

## Method

Read-only. Classified clusters, not every backtick.

- `live`: the claim still matches a tree that exists, or a git object that still resolves, and is not presented as a newer revision than the one measured.
- `superseded historical`: the claim was true of a past tree or revision, and the lane already describes it as history (dated stamp, `[lost-tree]` / `[lost-base]`, or a file-head errata). Do not rewrite those bytes.
- `unresolved`: the claim is still presented as openable or current, and this session falsified that reading, or the only cited record was never committed so the claim cannot be re-opened.

Describe-don't-pin means: keep the old sentence, name the revision or as-of stamp it belonged to, and do not let a reader treat that revision as the current tree.

## Presence re-check

| path | result |
|---|---|
| `~/Projects/bounties` | ABSENT |
| `~/Projects/the-bounty-hunter` | ABSENT |
| `~/Projects/origin-work` (and `…/ufo-fsd-alpha`, `…/open-bug-bounties`) | ABSENT |
| `~/Projects/ufo-fsd-alpha` | PRESENT |
| `~/projects` (lowercase) | ABSENT (`ls: cannot access`) |
| `find /home/vgpnk /home/vgpnk/Projects -maxdepth 3 -type d` for `bounties`, `the-bounty-hunter`, `open-bug-bounties`, `origin-work` | no hits |

This is a shallower probe than `root-loss-2026-10-12.md` §3 (`find ~ -maxdepth 5`). It reconfirms the canonical paths and depth-3 name hits. It does not repeat the maxdepth-5 sweep. Absence of those four directory names at depth ≤3 is measured; a deeper relocated copy remains unproven by this seat, same limit the round-19 note already carried.

`git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` = `964f443ee53df0ce06bd689af01f0dea031b01f9`. `rev-list --count 964f443e..HEAD` = 0. `merge-base --is-ancestor` exit 0. Subject: `routing: regenerate omp-seat-routing mirror from the live global config (operator: ompskills host apply)`, `2026-10-12 18:32:12 -0300`. The pin is not a superseded git revision.

Worktree is not identical to that commit. `git status --porcelain` (names only): `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs` (5 files, 195 insertions / 178 deletions). None of those paths are the files this lane re-anchored. Do not describe HEAD `964f443e` as a clean worktree. The root-loss sentence "clean of the old origin-work path" is a path-string claim, not a clean-tree claim; that reading was not falsified.

Lane blob pins still resolve in `/home/vgpnk/Projects/shokunin/kasegi-shokunin`: `fc6d398` SKILL.md 546 lines, `7483333` 590, `eb5b590` 997, `d1e6e8f` 1012. Those counts match `citation-bases.md:71-77`.

## Cluster inventory

### H1 — first loss, `~/Projects/bounties` (2026-09-28T23:51:31Z)

Class: **superseded historical**.

Evidence: still ABSENT this session. Landed record: `corpus/knowledge/source-tree-loss-2026-09-28.md:1-14`, `PROVINCE.md:5-8`, `SKILL.md:8-25`, `corpus/README.md:39-44`. Anchored lost-tree cites in SKILL + PROVINCE + `corpus/README.md` + `corpus/knowledge/*.md` this session: 159 `[lost-tree]` tokens. Past-EOF lost-tree marks that must stay `[lost-tree]` (recorded mirror EOF, not re-opened): `SKILL.md:338` `ops/shared.mjs:55` (mirror 41), `corpus/README.md:29` `ops/claim-check.mjs:96-97` (mirror 83), `citation-bases.md:52` and `source-tree-loss-2026-09-28.md:190` `ops/claim-check.mjs:174-199`.

`corpus/lessons/*.md` bare anchors (`round-14.md:33` `fleets/claimer-mission.md:29`, `round-14.md:37` `fleets/mission-template.md:20`, `round-4-aggregator-audit.md:26` `ops/shared.mjs:55`) are the rule-6 historical set (`citation-bases.md:107-116`). Class: **superseded historical**. Do not renumber or prefix them.

No new errata. Repeating the round-15/19 loss paragraph would rewrite a landed annotation.

### H2 — second loss, mirror `1cfbd86` and origin-work `1307b8b`

Class: **superseded historical** for the absence fact. The HEADs are identities of absent repos, not current checkouts.

Evidence: both trees ABSENT this session. Landed annotations already say so: `PROVINCE.md:16-22` (the present-tense "surfaces now resolve" at `PROVINCE.md:9-15` is the round-15 paragraph; the next paragraph withdraws it), `SKILL.md:19-32`, `corpus/README.md:47-58`, `citation-bases.md:20-41`, `root-loss-2026-10-12.md:10-14`, `source-tree-loss-2026-09-28.md:10-14`. `SKILL.md:813-816` "re-read this round" is labeled round 15. `SKILL.md:892-944` already dual-cites mirror vs lost-tree for `fleet-dispatch.mjs` (`:156`/`:204`, `:152`/`:200`). That is the correct describe-both form.

`source-tree-loss-2026-09-28.md:147` still says the mirror is "live-checkable" and `:157` says the mirror "can still execute". Those sentences are inside the historical body. The file-head errata already says they are not current. Do not strike them. No second errata.

Round-19 added 155 `[lost-base]` prefixes in `SKILL.md` and smaller counts in knowledge files (`git diff 7906aa10..d1e6e8f`). That repair landed. It is not re-done here. The one place it applied the prefix to lost-tree numbers is H6.

### H3 — `ufo-fsd-alpha` pin `964f443e`

Class: **live** for the git pin `964f443e` and for the two re-anchored file claims. **Unresolved** for "same repo (history intact)" and for the exclusive `.ufo/` listing pinned beside that revision as if it were current.

Live, re-measured:

- `scripts/ufo-sighting.mjs` exists, 4714 lines, worktree blob = HEAD blob `760edeafc22f006386e81302994869f977e4ec55`. `ufo-archive-2026.md:31` holds.
- Every `skills/ufo/SKILL.md` copy found (12 paths, including `skills/ufo/SKILL.md` and `.omp/skills/ufo/SKILL.md`) is 600 lines, sha256 prefix `4708d14d`, identical at HEAD and in the worktree. `ufo-workspaces.md:312` "file now 600 l" holds. The older `2d5bfd3e` / `40949973` pair in the same sentence is the round-13 fork diff, already described as not current. Do not pin `4708d14d` into that sentence; the line count is the live claim, the sha was not claimed.
- `.ufo/missions` ABSENT. `find … -maxdepth 4 -name 'hunt-*'` count 0. `ufo-workspaces.md:170-171` holds.

Falsified exclusive listing:

- `root-loss-2026-10-12.md:19-20` and `ufo-workspaces.md:172` say `.ufo/` holds only `cache scopes sighting statusline-*`.
- Measured children: `cache`, `contract-sync`, `rs-self-iter-blocked.json`, `scopes`, `sighting`, `statusline-cache.json`, `statusline-full.stamp`.
- New names `contract-sync` and `rs-self-iter-blocked.json` mtime `2026-10-14 20:16:04 -0300`, after the note's `2026-10-14T12:44Z` census. `git check-ignore -v` → `.gitignore:4:**/.ufo/`. They are ignored runtime, not a new commit. `scopes` mtime `2026-10-14 20:36:30 -0300` (directory touched; not claimed absent).

The revision did not move. The listing was a point-in-time worktree snapshot described as a property of HEAD `964f443e`. That is the describe-don't-pin failure.

`root-loss-2026-10-12.md:15` also says the relocated tree is the "same repo (history intact)". Measured on this checkout: `rev-list --count HEAD` = 3; root `72ab84a80c4033aa1182654fb3f288bb7ff446c4` (`2026-09-25 02:43:32 +0000`, `fix(sub-7): M4 r04…`); the three commits delete 0 files (`git diff --diff-filter=D --name-only 72ab84a8 HEAD` count = 0). `main` and `origin/main` are both `964f443e`. Object `5725fa7d3` exists (`2026-09-28 22:49:00 -0300`, 861 commits reachable from it) but `git merge-base HEAD 5725fa7d3` exits 1, and it is not an ancestor of HEAD. Reachable `main` history is not an intact long history. Describe `964f443e` as the current main tip, not as proof the origin-work history survived intact.

`root-loss-2026-10-12.md:29-30` cites `kumitate-shokunin/SCORECARD.md`, environmental-findings paragraph, for "50 upstream file deletions". That phrase is kasegi's paraphrase. The sibling paragraph is present at `kumitate-shokunin/SCORECARD.md:623-633`: origin tree moved; "history contains the round-16 pin `5725fa7d3`"; "3 commits since `5725fa7d3`, 50 files deleted", naming `scripts/atomic-write.mjs`, `scripts/charter-scribe/sync.test.mjs`, and `scripts/collect-omp-native-handoff-lib/refusal-line.mjs`. An earlier search for the paraphrase was a miss. The paragraph is not missing.

Those sibling claims do not describe reachable `main`. `5725fa7d3` is not an ancestor of HEAD. `rev-list --count 5725fa7d3..HEAD` = 3 because the histories do not join, not because HEAD is 3 commits after that pin. `git diff --diff-filter=D --name-only 5725fa7d3 HEAD` = 970, not 50. HEAD's own 3 commits deleted 0. The three named paths are present at `5725fa7d3` and absent at HEAD. Class: **superseded historical** as a 2026-10-13 recon sentence; **unresolved** as a current deletion count. Do not pin 50, and do not replace it with 970 inside the old sentence. Owner: kumitate for the recon; UFO substrate for the orphan main.

Cross-domain owner: UFO substrate (`~/Projects/ufo-fsd-alpha`) for the orphan history and `.ufo/` runtime; kumitate for the 2026-10-13 recon wording. Kasegi records the drift. It must not absorb router or runtime repair. Adjacent to `KasegiLiveAnchors`; this seat owns the historical-claim classification only.

### H4 — lane blob pins vs deleted command path

Class: **live** objects, **superseded historical** content (they are not current `SKILL.md`). **Unresolved** operability of the documented command.

`citation-bases.md:72-73` says resolve with `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md`. That directory is ABSENT. Uppercase `/home/vgpnk/Projects/shokunin/kasegi-shokunin` is the checkout, and `git show fc6d398:SKILL.md` there yields 546 lines, matching the prose. Fleet L0 already records the lowercase `~/projects` absorption (`../.ufo/l0-questions.md` kake round-17 row). This lane's command was not updated.

Do not rewrite the historical pin list. Append a path errata. Do not put `fc6d398:SKILL.md` in backticks (`citation-bases.md:77-79`).

### H5 — citation to a corpus note that was never committed

Class: **unresolved**.

`citation-bases.md:43-44` says the origin-work `.ufo-missions` subtree lost 681 files at `2026-09-28T22:45:06-03:00`, "recorded in `corpus/knowledge/open-bug-bounties-census.md` §loss-event".

Measured:

- `test -f corpus/knowledge/open-bug-bounties-census.md` → ABSENT.
- `git log --all -- corpus/knowledge/open-bug-bounties-census.md` empty.
- `git rev-list --all --objects` has no blob for that path.
- `git log -S open-bug-bounties-census` shows the cite arriving in `ed44a92` (round-18) inside `citation-bases.md` only.
- The 681-file fact is not in `LOG.md`. It is in the fleet side channel `../.ufo/l0-questions.md` kasegi round-16 row (681 files / 41 dirs / 14 MB, same timestamp, "NOT recoverable").

The count is single-sourced outside this corpus. Origin-work is ABSENT, so the count cannot be re-measured. The cite itself is a citation-to-never-landed, not a lost-tree path.

Named debt: `CENSUS-NOTE-NEVER-LANDED`. Cross-domain owner: fleet L0 / operator. This seat does not edit `.ufo/l0-questions.md`.

### H6 — round-19 `[lost-base]` on lost-tree `fleet-dispatch.mjs` numbers

Class: **unresolved**. This is the remaining falsified marking. It is not a gate defect.

`triage-thresholds.md:19-30` says the `ops/*.mjs` numbers below were read from the lost `~/Projects/bounties` tree, and that the mirror **diverges**: 330 lines vs 427; 3-term score at mirror `:97` vs the 5-term `:110` below; `adjusted_ev` at mirror `:152`/`:155`/`:156` vs `:200`/`:204`. `source-tree-loss-2026-09-28.md:115` is the same divergence table (`attempts()` mirror `:72-79` vs live `:78-85`; peak model mirror `:221` vs live `gpt-6-astra` — the live line this file cites is `:300`).

Parent `7906aa10` had those cites unprefixed (`fleet-dispatch.mjs:110`, `:200`, `:78-85`, …). Round-19 commit `d1e6e8f` wrapped them as `[lost-base]` (15 additions in this file). `[lost-base]` means the mirror (`citation-bases.md:59-64`). On these rows it points a restorer at the wrong bytes: mirror `:110` is not the 5-term expression; mirror `:200` is not the `adjusted_ev` read (mirror read is `:152`, which `SKILL.md:943` already cites as `[lost-base]`).

Exact mis-prefixed tokens added in `d1e6e8f` (line numbers are current):

- `triage-thresholds.md:52` `[lost-base] fleet-dispatch.mjs:88-114`
- `:65` `[lost-base] fleet-dispatch.mjs:78-85`
- `:72` `[lost-base] fleet-dispatch.mjs:56`
- `:73` `[lost-base] fleet-dispatch.mjs:182`
- `:77` `[lost-base] fleet-dispatch.mjs:110`
- `:92` `[lost-base] fleet-dispatch.mjs:113`
- `:98` `[lost-base] fleet-dispatch.mjs:110`
- `:126` `[lost-base] fleet-dispatch.mjs:98`
- `:131` `[lost-base] fleet-dispatch.mjs:90`
- `:343` `[lost-base] fleet-dispatch.mjs:200`
- `:383` `[lost-base] fleet-dispatch.mjs:107`
- `:433` `[lost-base] fleet-dispatch.mjs:110`
- `:435` `[lost-base] fleet-dispatch.mjs:10`
- `:436` `[lost-base] fleet-dispatch.mjs:200` and `[lost-base] schema.json:34-51` and `[lost-base] fleet-dispatch.mjs:11`
- `:438` `[lost-base] fleet-dispatch.mjs:300`

`schema.json` was recorded anchor-compatible (`source-tree-loss-2026-09-28.md:112`, 68 lines). A `[lost-base]` on `schema.json:34-51` is not the same defect as the `fleet-dispatch.mjs` prefixes. The header still says those numbers were read from the lost tree; describe them as lost-tree numbers that matched the mirror, not as a new mirror reading.

Header `:21-22` still says "the surviving frozen mirror". That present tense is false as of this session. It is the same second-loss fact H2 already recorded elsewhere, left unannotated in this file.

Not past recorded mirror EOF: a `[lost-base]` cite with end line greater than the §4.1 mirror length was not found in SKILL + knowledge for `ev-report.mjs` (92), `rank.mjs` (249), `park-disposition.mjs` (80), `fleet-dispatch.mjs` (330), `shared.mjs` (41), `claim-check.mjs` (83), `schema.json` (68). The defect is wrong base, not past-EOF. `anchorcheck.py` would not catch it: both prefixes are `LOST-RECORDED` and unchecked.

### H7 — mirror path carrying a lost-tree past-EOF line

Class: **unresolved**.

`claim-package-contract.md:19-22` attributes "the entire provenance gate is the :96-97 non-emptiness check" to `~/Projects/the-bounty-hunter/ops/claim-check.mjs`. Recorded mirror length is 83 (`source-tree-loss-2026-09-28.md:117`). `corpus/README.md:29` already says that range is `[lost-tree]` and the mirror file is 83 lines. The contract note was not updated. `:29` in the same paragraph may exist on the 83-line file; this seat cannot re-read the mirror, so only `:96-97` is called past-EOF.

### H8 — unmarked Source lines into absent roots

Class: **superseded historical** as claims (each is dated "Read 2026-09-28" or "Verified live 2026-09-28"), **unresolved** as openable tokens. Round-19 marked many `path:line` anchors and left these Source lines unmarked, so a resolver still treats them as current paths.

Unmarked `Source:` / equivalent openable leads:

- `claim-gates.md:3` `~/Projects/bounties/ops/claim-check.mjs`
- `claim-package-contract.md:3` `~/Projects/bounties/fleets/mission-template.md`
- `ev-model.md:3-8` mirror `ops/ev-report.mjs` at `1cfbd86`, round-15 note only (bounties gone; mirror not marked absent)
- `intake-and-finalize.md:3` `~/Projects/bounties/ops/import-board.mjs`, plus body paths at `:11`, `:14-22`, `:70`, `:84`, `:95` into the mirror and origin-work
- `mission-control.md:3` `~/Projects/bounties/ops/fleet-dispatch.mjs` (427 lines — the lost-tree length, not the 330-line mirror)
- `ops-invariants.md:3-5` and `:10` bounties plus `~/Projects/the-bounty-hunter`
- `policy-access-playbook.md:3` `~/Projects/the-bounty-hunter/fleets/mission-template.md`
- `retirement-autopsies.md:3-5` mirror source plus "live re-census"; `:43` "Verified against the surviving mirror writer"
- `operator-queue.md:3-5` `docs/claim-ready-index.md` and "live `ops/claim-check.mjs` re-run" (relative, lost tree)
- `repo-git-state.md:7` "ACTIVE hazard" and `:21` "refused **now**" about the bounties dispatcher. The repo is absent. The stall cannot be current.
- `target-checkouts.md:11` disposition `live: the cantina-pendle hunt target` for `pendle-core-v2-public/` inside the lost tree

Already marked, leave alone: `evidence-dir.md:3`, `mission-ledger.md:3`, `program-quirks.md:3`, `terminal-classes.md:3`, `ufo-archive-2026.md:3`, `vdp-disclosure-packages.md:3`, `intake-surface.md:4`.

`citation-bases.md:31` still backquotes `~/Projects/the-bounty-hunter/ops/rank.mjs:55-58` with no prefix. The same sentence says it is now `[lost-base]` and BASE-ABSENT. The example token is an openable-shaped cite to an absent file. Class: **unresolved** as a token; the sentence's historical reading is already written.

### H9 — carried debt that stays debt

Class: **unresolved**. Do not close these by corpus citation.

From `SCORECARD.md:150-165`, still true because the trees are absent:

- `RECEIPT-STORE-LOST` — `submission-review/` receipts. Unblock: restore `open-bug-bounties` or operator declares the claims permanently attested. Owner: operator.
- `MIRROR-SOURCE-LOST` — every mirror line anchor uncheckable. Unblock: restore a checkout of `1cfbd86`, or set `$KASEGI_MIRROR`. Owner: operator. Not a gate code change; instruments already derive the root.
- `ORIGIN-REPO-LOST` — historical `origin-work/ufo-fsd-alpha` quotes stay quotes. Live file claims were re-anchored and H3 re-checked them. Unblock: none for the pin. The `.ufo/` listing is separate (H3).
- PROVINCE re-point — `PROVINCE.md:13-14`, `../.ufo/l0-questions.md` kasegi round-15 row. Owner: operator. This lane must not re-scope itself.

`citation-survival.md` (round-19 generated census) is not re-interpreted here. Its INTERNAL rows for `../MISSION.md` and `./PROVINCE.md` still name files that exist (`/home/vgpnk/Projects/shokunin/MISSION.md`, lane `PROVINCE.md`).

## Draft append-only errata

Parent may append these. Do not replace the sentences they cite. Do not edit gate files. LOG and SCORECARD appends are parent work, not this seat.

### E1 — append to `corpus/knowledge/triage-thresholds.md`

```
**Round-20 errata (2026-10-14, append-only; do not edit the rows above).**
The round-19 `[lost-base]` prefixes on `fleet-dispatch.mjs` line numbers in
this file mark lost-tree numbers, not mirror numbers. The header at the
round-15 pin still says so: mirror score is 3-term at `:97`; the 5-term
expression at `:110` is the lost tree; mirror `adjusted_ev` read/log/note
are `:152`/`:155`/`:156`, not `:200`/`:204`; mirror `attempts()` is
`:72-79`, not `:78-85`. Read every `[lost-base] fleet-dispatch.mjs:…` token
in this file as `[lost-tree]` for the lost `~/Projects/bounties` tree
as-of 2026-09-28T23:32Z. Do not pin those lines to
`~/Projects/the-bounty-hunter` HEAD `1cfbd86`. The dual-cite form that
keeps both bases is `SKILL.md` triage-economics (`:152` mirror / `:200`
lost-tree). `schema.json` spans that matched the mirror at round 15 stay
anchor-compatible history, not a new reading. "The surviving frozen mirror"
in the header is the round-15 status; that tree was ABSENT at the
2026-10-14T12:44Z re-census and was still ABSENT at 2026-10-14T23:37:28Z.
```

### E2 — append to `corpus/knowledge/claim-package-contract.md`

```
**Round-20 errata (append-only).** The `:96-97` non-emptiness check named
at the round-13 boundary note is a lost-tree line. The frozen mirror
`ops/claim-check.mjs` was recorded at 83 lines
(`corpus/knowledge/source-tree-loss-2026-09-28.md` §4.1). Do not read
`~/Projects/the-bounty-hunter/ops/claim-check.mjs:96-97` as a mirror anchor.
Index correction already at `corpus/README.md:29`. Both the bounties tree
and the mirror are absent; the sentence is history, not an openable path.
```

### E3 — append to `corpus/knowledge/citation-bases.md`

```
**Round-20 errata (append-only).**
1. The example token `~/Projects/the-bounty-hunter/ops/rank.mjs:55-58` in
   the MIRROR section is the pre-loss form. It does not resolve. The
   sentence already says it is `[lost-base]` / BASE-ABSENT. Do not open it.
2. `corpus/knowledge/open-bug-bounties-census.md` was never committed
   (`git rev-list --all --objects` has no blob; cite arrived in `ed44a92`
   and points nowhere). The 681-file / 2026-09-28T22:45:06-03:00 loss is
   recorded only in the fleet L0 side channel (kasegi round-16 row), not
   in a lane note. Do not treat §loss-event as openable. The count is
   unresolved named debt `CENSUS-NOTE-NEVER-LANDED` until an operator
   accepts the L0 row as the record or restores origin-work.
3. The blob-pin command uses `/home/vgpnk/projects/shokunin/kasegi-shokunin`.
   That lowercase path is ABSENT (measured 2026-10-14T23:37:28Z). The
   objects `fc6d398` (546), `7483333` (590), and `eb5b590` (997) still
   resolve under `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. Describe
   the pins as those historical snapshots. Do not describe the lowercase
   path as the current checkout. Do not backtick a bare blob path.
```

### E4 — append to `corpus/knowledge/root-loss-2026-10-12.md`

```
**Round-20 listing errata (2026-10-14T23:37:28Z, append-only).**
HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` was still HEAD
(`rev-list --count 964f443e..HEAD` = 0). The `.ufo/` child list in the
facts section was a 12:44Z worktree snapshot, not a property of that
commit. Re-list: `cache`, `contract-sync`, `rs-self-iter-blocked.json`,
`scopes`, `sighting`, `statusline-cache.json`, `statusline-full.stamp`.
`contract-sync` and `rs-self-iter-blocked.json` mtime 2026-10-14 20:16:04
-0300; `git check-ignore` reports `.gitignore:4:**/.ufo/`. `.ufo/missions`
still absent. Do not pin the child list to the commit. Worktree dirt
unrelated to lane cites (names only): `README.md`, `config/ufo.json`,
`crates/ufo-core-runtime/bundled/config.json`,
`crates/ufo-core-runtime/bundled/omp-seat-routing.json`,
`scripts/fleet-dispatcher.test.mjs`. Canonical lost roots were still
ABSENT. Depth-3 name probe found no relocated `bounties`,
`the-bounty-hunter`, `open-bug-bounties`, or `origin-work`. The note's
maxdepth-5 sweep was not repeated.
HEAD's reachable history is 3 commits rooted at `72ab84a8`
(2026-09-25). Do not read "same repo (history intact)" as current.
`5725fa7d3` is in the object db (861 commits) and has no merge-base
with HEAD (exit 1). "50 upstream file deletions" is this note's
paraphrase of `kumitate-shokunin/SCORECARD.md:630` ("50 files deleted"),
which is present. Do not record that paragraph as missing. The count
does not reproduce: `git diff --diff-filter=D --name-only 5725fa7d3 HEAD`
= 970; HEAD's 3 commits deleted 0. The three named paths are absent at
HEAD and present at `5725fa7d3`. Do not pin 50, and do not substitute 970.
```

### E5 — append to `corpus/knowledge/ufo-workspaces.md` after the hunt-* paragraph

```
**Round-20 errata (append-only).** The 2026-10-14 re-verify that
`~/Projects/ufo-fsd-alpha` @ `964f443e` has no `.ufo/missions/` and no
`hunt-*` at depth ≤4 still held at 2026-10-14T23:37:28Z (hunt count 0).
The parenthetical "`.ufo/` holds only `cache scopes sighting statusline-*`"
did not. Ignored children `contract-sync` and `rs-self-iter-blocked.json`
were present (mtime 2026-10-14 20:16:04 -0300). Describe that list as the
12:44Z snapshot. Do not pin it to HEAD `964f443e`. The 600-line ufo
`SKILL.md` claim still matched HEAD and worktree (sha256 prefix
`4708d14d`); do not add that prefix to the round-13 fork-diff sentence.
```

### E6 — one header stamp for the unmarked Source cluster

Append the same paragraph, unchanged, to each of: `claim-gates.md`, `claim-package-contract.md`, `ev-model.md`, `intake-and-finalize.md`, `mission-control.md`, `ops-invariants.md`, `policy-access-playbook.md`, `retirement-autopsies.md`, `operator-queue.md`, `repo-git-state.md`, `target-checkouts.md`.

```
**Round-20 source stamp (append-only).** Every `~/Projects/bounties`,
`~/Projects/the-bounty-hunter`, and `~/Projects/origin-work` path in this
note is a historical source as-of the date in the header (2026-09-28
unless a later sentence gives its own stamp). Those trees were ABSENT at
2026-10-14T23:37:28Z. "Live", "now", "surviving", and "ACTIVE" in the body
mean that census, not the current host. Do not prefix-rewrite the body.
Openable form, when a path:line is added later, is `[lost-tree]` for
bounties and `[lost-base]` for the mirror and origin-work.
```

Do not apply E6 to files that already carry a round-19 absence stamp (`citation-bases.md` gets E3 instead; `source-tree-loss-2026-09-28.md`, `root-loss-2026-10-12.md`, `evidence-dir.md`, `mission-ledger.md`, `program-quirks.md`, `terminal-classes.md`, `ufo-archive-2026.md`, `vdp-disclosure-packages.md`). `triage-thresholds.md` gets E1, not a second copy of E6.

## Named debt retained

| id | class | unblock | owner |
|---|---|---|---|
| `RECEIPT-STORE-LOST` | unresolved | restore `open-bug-bounties` or operator declares receipts permanently attested | operator |
| `MIRROR-SOURCE-LOST` | unresolved | restore HEAD `1cfbd86` or set `$KASEGI_MIRROR` | operator |
| `ORIGIN-REPO-LOST` | superseded historical for quotes; live pin re-checked | none for the git pin | lane record |
| `PROVINCE-REPOINT` | unresolved | operator answers kasegi round-15 L0 row; lane must not re-scope | operator |
| `CENSUS-NOTE-NEVER-LANDED` | unresolved | accept L0 round-16 row as the 681-file record, or restore origin-work; do not invent the missing note | operator / fleet L0 |
| `TRIAGE-LOST-BASE-MISPREFIX` | unresolved until E1 is appended | append E1; do not in-place swap prefixes (that rewrites round-19 bytes) | parent integrator |
| `CLAIM-CHECK-96-MIRROR-MISBASE` | unresolved until E2 is appended | append E2 | parent integrator |
| `BLOB-PIN-LOWERCASE-PATH` | unresolved until E3 is appended | append E3; command works only on the uppercase path | parent integrator |
| `UFO-DOT-LISTING-DRIFT` | unresolved as a current-listing claim; git pin live | append E4 and E5; do not treat ignored `.ufo/` children as a kasegi code defect | UFO substrate owner; kasegi records only |
| `UFO-HISTORY-NOT-INTACT` | unresolved | describe HEAD `964f443e` as a 3-commit main tip rooted at `72ab84a8`; do not claim origin-work history survived intact | UFO substrate owner; kasegi records only |
| `KUMITATE-50-COUNT` | unresolved as a current count; cite live at `kumitate-shokunin/SCORECARD.md:623-633` | paraphrase, not a missing paragraph; 50 does not reproduce (cross-history `--diff-filter=D` name count 970; HEAD's 3 commits deleted 0); do not rewrite the 2026-10-13 sentence | kumitate for the recon; UFO substrate for the history |

No gate implementation change is justified from this seat. Instruments already derive `$KASEGI_MIRROR` / `$KASEGI_ORIGIN_ROOT` / `$UFO_SRC`. Explicit bad `--src` stays bad. That is GateRepair's file set; this seat did not open those files for edit.

## Proposed delta

Append E1–E6 only. Preserve every existing LOG line, corpus sentence, and lesson anchor. Do not stage, commit, or push from this seat.

If the parent applies nothing, the lane stays honest only if readers are pointed at this inventory: the round-19 loss stamps hold, and the unresolved rows in the debt table are the remaining freshness/calibration debt.
