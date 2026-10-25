# KasegiHistoricalMarking — advisory re-measure

Seat: `kasegi/audit/HistoricalMarking`. Lane: `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. Lane identity commit `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` (`round-20: OMP-era freshness re-census…`, `kasegi-shokunin <kasegi@shokunin.local>`). Parent fleet HEAD is a different repo and does not contain this object.

This file is an advisory inventory. It is not a native judge verdict, a lane round report, a receipt, or an admission. No lane file was edited. `resolve.py` was not run: it writes `citation-survival.md` / `.tsv`.

Describe-don't-pin, as applied here: a count, hash, pid, or line number may stay in the sentence that measured it, if that sentence is dated or stamped as the revision it belonged to, and a reader cannot treat it as the current identity of a file that is missing or that has moved. A content hash of a missing file asserted as what the file is now is a failure even when the hash was once true.

## Commands (this seat)

| command | exit | last / decisive line |
|---|---:|---|
| `python3 corpus/instruments/anchorcheck.py SKILL.md` (cwd = lane) | 0 | `== SKILL.md: 7 in-range cite instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306 PIN-BROKEN=0 ORIGIN=0 OUTSIDE-BASE=0 BASE-ABSENT=0` |
| `python3 corpus/instruments/density.py SKILL.md --label audit` | 0 | `Total path-citation instances: 645 across 18 blocks.` Mean dens **154.0**. |
| `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` | 0 | `964f443ee53df0ce06bd689af01f0dea031b01f9` |
| `git -C ~/Projects/ufo-fsd-alpha merge-base HEAD 5725fa7d3` | 1 | empty; not an ancestor (`merge-base --is-ancestor` exit 1) |
| `git -C ~/Projects/ufo-fsd-alpha diff --diff-filter=D --name-only 5725fa7d3 HEAD \| wc -l` | 0 | `970` |
| `git -C ~/Projects/ufo-fsd-alpha diff --diff-filter=D --name-only 72ab84a8 HEAD \| wc -l` | 0 | `0` |
| `git -C ~/Projects/ufo-fsd-alpha rev-list --count HEAD` | 0 | `3` (root `72ab84a80c4033aa1182654fb3f288bb7ff446c4`) |
| `git -C ~/Projects/ufo-fsd-alpha rev-list --count 5725fa7d3` | 0 | `861` |
| `ls` of `~/Projects/ufo-fsd-alpha/.ufo` | 0 | `cache contract-sync rs-self-iter-blocked.json scopes sighting statusline-cache.json statusline-full.stamp` |
| `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md` | 128 | `cannot change to '/home/vgpnk/projects/shokunin/kasegi-shokunin': No such file or directory` |
| `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md \| wc -l` | 0 | `546` |
| canonical lost roots `test -d` | — | ABSENT: `~/Projects/bounties`, `~/Projects/the-bounty-hunter`, `~/Projects/origin-work` (and `…/ufo-fsd-alpha`, `…/open-bug-bounties`), `~/projects`. PRESENT: `~/Projects/ufo-fsd-alpha`, uppercase lane checkout. |
| `test -f corpus/knowledge/open-bug-bounties-census.md` | 1 | ABSENT. `git log --all --` that path: empty. Pickaxe `open-bug-bounties-census` hits only `ed44a92` (the cite). |

`find ~ -maxdepth 5` from the round-19 note was not repeated. Absence of the canonical paths is measured. A deeper relocated copy is not re-proven here.

Round-20 diff (`git show --stat HEAD`): `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-20-recensus.md` only. Knowledge notes, `SKILL.md`, and instruments were not touched. `git status --porcelain`: `?? plans/` only (untracked plan; not a pin).

## Claim-by-claim vs `corpus/lessons/round-20-recensus.md`

| lesson claim | verdict | evidence |
|---|---|---|
| anchorcheck `7 in-range / 0 bad / LOST-RECORDED=306 / PIN-BROKEN=0 / OUTSIDE-BASE=0 / BASE-ABSENT=0` | **agree** on every field the lesson states | re-run above. The tool also prints `ORIGIN=0`, which the lesson omits. Not a contradiction. |
| density `645` path-citation instances, exit 0 | **agree** | re-run above. Mean 154.0. |
| instruments already derive `$KASEGI_MIRROR` / `$KASEGI_ORIGIN_ROOT`; no gate change | **agree** | `anchorcheck.py:70-97` derives those two. Round-20 diff does not touch instruments. |
| `$UFO_SRC` is not a real consumer; the anchor regex does not match `~/Projects/ufo-fsd-alpha/` | **agree** with the lesson; **disagree** that the living notes already say this | `UFO_SRC` occurs in `LOG.md:802`, `SCORECARD.md:164`, `root-loss-2026-10-12.md:55`, and the lesson. It does not occur in `anchorcheck.py` or `resolve.py`. |
| named debts left unrepaired | **agree** | each token below is still in the living file; round 20 did not edit those files |
| 50-file-deletion sentence does not reproduce; do not adopt 50 | **agree** | cross-history delete count is 970, not 50; HEAD's own 3 commits deleted 0; `5725fa7d3` has no merge-base with HEAD. Do not substitute 970 into the old sentence. |
| scorecard `116/1142`, `132/1469` do not match census `116/1144`, `132/1471` | **agree**, with a sharper stamp | the mismatch is inside `d1e6e8f`, not a later regeneration. `git show d1e6e8f:corpus/instruments/citation-survival.md` already has `116/1144` and `132/1471`. The same commit's `SCORECARD.md:134` and `LOG.md:812` say `116/1142` and `132/1469`. Round 20 did not rewrite either number. |

Suffix-join "left unlanded": the commit did not land it. This seat did not assess whether it was the only available root change.

## What still holds (do not re-pin)

- Git pin `964f443ee53df0ce06bd689af01f0dea031b01f9` is still HEAD (`rev-list --count 964f443e..HEAD` = 0). Subject and date match `root-loss-2026-10-12.md:15-17`. Not a superseded git revision.
- `~/Projects/ufo-fsd-alpha/skills/ufo/SKILL.md` is 600 lines. Worktree blob = HEAD blob `1e56471673ba93f78b6047ef08239c8af616345d`. `ufo-workspaces.md:312` "file now 600 l" holds. The `2d5bfd3e` / `40949973` pair in the same sentence is already marked as the recorded fork diff, not current bytes. Do not add `4708d14d` to that sentence.
- `scripts/ufo-sighting.mjs` is 4714 lines. Worktree blob = HEAD blob `760edeafc22f006386e81302994869f977e4ec55`.
- Worktree dirt on that repo (names only): `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs`. None of those are the re-anchored files. `root-loss-2026-10-12.md:18` "clean of the old origin-work path" is a path-string claim, not a clean-tree claim. Do not read a clean worktree into it.
- Blob pins `fc6d398` (546-line `SKILL.md`), and the objects named beside it, still resolve on the uppercase checkout. They are historical snapshots, not current `SKILL.md` (`sha256sum` now `d4383dc435359aca…`, not the round-18 log pin `62582f91…`).
- Receipt-store hashes in `LOG.md:734-738` (`3ed3e695…`, `1fa7cb8b…`, `49525f86…`) are withdrawn as current by `root-loss-2026-10-12.md:62-64` ("descriptions of evidence that can no longer be re-measured, preserved verbatim"). That marking holds. Do not delete the hashes. Do not treat `LOG.md:734` "current-byte" as the file now.
- `source-tree-loss-2026-09-28.md:10-14` already says the body's "live-checkable" / "can still execute" sentences (`:147`, `:157`) are historical. Do not strike them.
- `PROVINCE.md:9-15` present tense is withdrawn by `:16-22`. Do not rewrite the round-15 paragraph.
- Operator-queue captured-source sha256 `ded642e811b4…` (`operator-queue.md:29`) is a disclosure fingerprint of captured bytes, not a claim that a path on disk now hashes to that value. Not a current-identity pin.
- No numeric pid is pinned anywhere in the lane. The only hit is the command text `pgrep` at `ops-invariants.md:126`. Vacuous pass on pids.
- Pre-r16 lesson anchors stay under `citation-bases.md` rule 6. Not re-flagged.

## Counterexamples (path:line)

Round 20 named several of these and did not mark the source sentences. The sentences below are still present-tense or still the latest numeric claim a reader of the living file will take as current.

### C1 — census counts, living scorecard vs the file it cites

`SCORECARD.md:134` and `LOG.md:812` state corpus `116/1142 = 10.16 %` and lane `132/1469 = 8.99 %` as the round-19 regenerated census.

Committed census, same commit `d1e6e8f` and still at HEAD:

- `corpus/instruments/citation-survival.md:13` corpus distinct = **1144**
- `:32` `116/1144 = 10.14%`
- `:33` `132/1471 = 8.97%`
- `:11` distinct total **1471**

The lesson agrees the rates do not match. The scorecard row is not marked stale. A reader of `SCORECARD.md` still takes `116/1142` as the last measured rate. `LOG.md:812` is a dated round-19 entry; the scorecard row is the living one.

Related, not named by the lesson: `corpus/instruments/README.md:16-17` says `citation-survival.md` / `.tsv` are the **current census of record, regenerated in round 18**. That file was regenerated in `d1e6e8f` (round 19). Round-18 log pins of that generation (`LOG.md:756-759`, md `4d387470…`, tsv `95c6a232…`) do not match current bytes (`483c1411…`, `d12387cf…`). The README sentence is a superseded regeneration presented as the current census identity. Round 19 touched this README (`git log` last touch `d1e6e8f`) and left the sentence.

### C2 — `$UFO_SRC` asserted as an instrument root

Lesson is right that the code does not consume it. These living sentences still say it does:

- `corpus/knowledge/root-loss-2026-10-12.md:55` — instruments derive `$KASEGI_MIRROR` / `$KASEGI_ORIGIN_ROOT` / `$UFO_SRC`
- `SCORECARD.md:164` — "derived `$UFO_SRC` candidates list the new path first"
- `LOG.md:802` — "`$UFO_SRC`/`ufo-fsd-alpha` candidates in anchorcheck" (dated round-19 entry; the two files above are the current-facing copies)

`grep UFO_SRC` over the lane hits only those prose sites plus the lesson. Not in `anchorcheck.py` or `resolve.py`.

### C3 — `resolve.py` line numbers, superseded and one standing mis-pin

`citation-bases.md` cites current instrument lines. `citation-survival.md:147-150` reports them INTERNAL and in range (file is 516 lines). Range is not the rule.

At `ed44a92` (round 18), `classify()` other-root return was `:163-165` and the relative fallback was `:166-174`. Round 19 inserted the derived-root block and moved `classify()` down. Current text:

- other-root rule is `resolve.py:178-180`
- relative lane-then-mirror fallback is `resolve.py:181-189`
- `LINEANCHOR` is `resolve.py:76`
- `resolve.py:74` is `EXTS`, and was already `EXTS` at `ed44a92`

Sentences that still point at the old or wrong lines:

- `citation-bases.md:16` and `:29` — `resolve.py:164-172` as the relative-path GONE / MIRROR-EQUIVALENT fallback. Current `:164-172` is the start of bounty-domain `classify()`, not that fallback.
- `citation-bases.md:41` — `resolve.py:161-163` as the other-root RESOLVES rule. Current `:161-163` is inside `exists_any` (glob return).
- `citation-bases.md:105` — `resolve.py:74` as the line-anchor rule. That line is `EXTS`. This pin was already wrong at round 18; it is a standing mis-pin, not a round-19 drift.

`citation-bases.md:18` `resolve.py:31-48` still lands in the module docstring that states INTERNAL (`:37-38`). Not the same defect. The implementation of that branch is now `:182-184`.

### C4 — HEAD `964f443e` carrying a drifted worktree listing and an intact-history claim

`root-loss-2026-10-12.md:15` — "same repo (history intact)". Measured: reachable `main` is 3 commits rooted at `72ab84a8` (2026-09-25). Object `5725fa7d3` exists (861 commits) and `merge-base` with HEAD exits 1. Describe `964f443e` as the current main tip, not as proof the origin-work history survived.

`root-loss-2026-10-12.md:19-20` and `ufo-workspaces.md:171-172` — `.ufo/` holds only `cache scopes sighting statusline-*`. Measured children also include `contract-sync` and `rs-self-iter-blocked.json` (mtime `2026-10-14 20:16:04 -0300`, after the note's `2026-10-14T12:44Z` census). `git check-ignore -v` → `.gitignore:4:**/.ufo/`. `scopes` directory mtime `2026-10-14 21:16:36 -0300`. The revision did not move. The exclusive list was a 12:44Z snapshot written as a property of HEAD `964f443e`.

`root-loss-2026-10-12.md:29-30` — "measured 50 upstream file deletions", citing `kumitate-shokunin/SCORECARD.md` environmental-findings paragraph. That paragraph is present at `kumitate-shokunin/SCORECARD.md:623-633` ("3 commits since `5725fa7d3`, 50 files deleted"). It does not describe reachable `main`. Named paths `scripts/atomic-write.mjs`, `scripts/charter-scribe/sync.test.mjs`, `scripts/collect-omp-native-handoff-lib/refusal-line.mjs` are PRESENT at `5725fa7d3` and ABSENT at HEAD. Delete count `5725fa7d3` vs HEAD is 970, not 50. HEAD's 3 commits deleted 0. `rev-list --count 5725fa7d3..HEAD` = 3 because the histories do not join, not because HEAD is 3 commits after that pin.

### C5 — blob-pin command uses a missing checkout path

`citation-bases.md:72-73` and `triage-thresholds.md:12` tell the reader to resolve pins with `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin` (lowercase `projects`). That directory is ABSENT (command exit 128, above). Uppercase `/home/vgpnk/Projects/shokunin/kasegi-shokunin` is the checkout, and `fc6d398:SKILL.md` there is 546 lines, matching the prose. The objects are live. The documented command is not.

### C6 — count whose only cited record was never committed

`citation-bases.md:43-44` — origin-work `.ufo-missions` lost 681 files at `2026-09-28T22:45:06-03:00`, "recorded in `corpus/knowledge/open-bug-bounties-census.md` §loss-event". That file was never committed. Origin-work is ABSENT, so the count cannot be re-measured. The cite is not a lost-tree path; it is a citation to a note that does not exist.

### C7 — `[lost-base]` on lost-tree `fleet-dispatch.mjs` numbers

`triage-thresholds.md:19-30` says the `ops/*.mjs` numbers below were read from the lost `~/Projects/bounties` tree, and that the mirror diverges (330 lines vs 427; 3-term score at mirror `:97` vs 5-term `:110`; `adjusted_ev` at mirror `:152`/`:155`/`:156` vs `:200`/`:204`). The tokens were then prefixed `[lost-base]`, which means the mirror (`citation-bases.md:59-64`). A restorer who trusts the prefix reads the wrong bytes. `anchorcheck.py` will not catch it: both prefixes are `LOST-RECORDED` and unchecked. This seat did not re-open the absent mirror; the divergence table is the recorded mirror length, not a new reading.

Still prefixed `[lost-base]` on those lost-tree numbers:

- `triage-thresholds.md:52` `:88-114`
- `:65` `:78-85`
- `:72` `:56`
- `:73` `:182`
- `:77` `:110`
- `:92` `:113`
- `:98` `:110`
- `:126` `:98`
- `:131` `:90`
- `:343` `:200`
- `:383` `:107`
- `:433` `:110`
- `:435` `:10`
- `:436` `:200`, and `:11` in the same cell
- `:438` `:300`

`:436` also prefixes `[lost-base] schema.json:34-51`. `source-tree-loss-2026-09-28.md:112` recorded `schema.json` as anchor-compatible (68 lines). That prefix is not the same defect. The header still says those numbers were read from the lost tree.

`triage-thresholds.md:21` "the surviving frozen mirror" is present tense. That tree is ABSENT (`test -d` fails).

### C8 — mirror path carrying a lost-tree past-EOF line

`claim-package-contract.md:19-22` attributes "the entire provenance gate is the :96-97 non-emptiness check" to `~/Projects/the-bounty-hunter/ops/claim-check.mjs`. Recorded mirror length is 83 (`source-tree-loss-2026-09-28.md:117`). `corpus/README.md:29` already calls that range `[lost-tree]`. The contract note was not updated. Both trees are absent. The sentence is history written as a mirror anchor. `:29` in the same paragraph may exist on an 83-line file; this seat cannot re-read the mirror, so only `:96-97` is called past recorded EOF.

### C9 — content hashes of missing files asserted as current identity

The hard rule fails on these. The hashes may have been true of a named past tree. They are written as what the file is.

- `corpus/knowledge/submitted-registry.md:108-109` — "the surviving mirror's 83-line `ops/claim-check.mjs` (sha256 `93679ea1d29b`)". "Surviving" is present tense. `~/Projects/the-bounty-hunter` is ABSENT. A grep for `Round-19|Round-20|ABSENT` in that file hits only this sentence; there is no absence stamp.
- `SKILL.md:321` — `ops/shared.mjs` (mirror: 41 lines, sha256 `2497578a44e5`) **owns** the constants. Present tense. File absent. The skill header (`SKILL.md:25-31`) says the roots are gone; this sentence does not say the hash is not current identity.
- `SKILL.md:477` — `ops/park-disposition.mjs` (mirror: 80 lines, sha256 `868057c96cc8`) in the same present-tense shape.
- `SKILL.md:816-820` — mirror `ops/ev-report.mjs` sha256 `ba5485ed6a5d` "resolves", `ops/rank.mjs` `e724186c1330` "matches". Labeled "Anchor base (round 15)" and HEAD `1cfbd86`, which is the right revision stamp, but the paragraph does not say that tree is now absent. Present tense.
- `corpus/knowledge/ev-model.md:8-10` — same `ba5485ed6a5d`, "resolves at 0 offset", revision named (`1cfbd86`), absence not marked in the file. Weaker than "surviving", same class.

Not in this class: the receipt hashes withdrawn at `root-loss-2026-10-12.md:62-64`; the provenance table under the `source-tree-loss` file-head errata; the fork-diff prefixes at `ufo-workspaces.md:310-313`.

### C10 — present-tense counts of an absent repo

`corpus/knowledge/repo-git-state.md` has no round-19/20 absence stamp (`grep` Round-19|ABSENT: no matches). Header `:3` says "Verified live 2026-09-28", which is a date, then the section title and the consequence override it:

- `:7` "ACTIVE hazard"
- `:15` dirty tree **903 entries** (breakdown of a missing worktree)
- `:21` dispatcher `commitClaims`/`finalizePush`/`periodicSync` is refused **now**

`~/Projects/bounties` is ABSENT. Those counts cannot be current. The date in the header is not enough while the section says ACTIVE and now.

Unmarked `Source:` leads into absent roots (claim-gates, mission-control's 427-line lost-tree length, target-checkouts "live", retirement-autopsies "surviving mirror writer", and the rest of that cluster) are the same second-loss fact. Dead-path sweep owns the openable-token list. This seat flags them only where they pin a count, hash, or "now".

## Named debt

| id | where | class | owner | unblock |
|---|---|---|---|---|
| `CENSUS-RATE-STALE` | `SCORECARD.md:134`, `LOG.md:812` vs `citation-survival.md:32-33` | superseded count, still the last scorecard rate | kasegi record / parent append | mark the scorecard row as not the census file; do not edit the round-19 sentence in place; do not re-pin 1142 to 1144 inside the old sentence without saying the file already said 1144 at `d1e6e8f` |
| `CENSUS-README-ROUND18` | `corpus/instruments/README.md:16-17` | superseded regeneration presented as current census identity | kasegi record | append that the current file is the round-19 regeneration (`116/1144`, `132/1471`), not the round-18 run |
| `UFO-SRC-NOT-A-CONSUMER` | `root-loss-2026-10-12.md:55`, `SCORECARD.md:164`; dated copy `LOG.md:802` | false current instrument claim; lesson states the fact and does not point at these lines | kasegi record | append that `$UFO_SRC` is not read by `anchorcheck.py` or `resolve.py`. Do not add a consumer to make the sentence true |
| `RESOLVE-LINE-DRIFT` | `citation-bases.md:16`, `:29`, `:41`, `:105` | superseded (and one standing) line numbers; range-check passes | kasegi knowledge | append current spans (`:178-180`, `:181-189`, `:76`). Do not backtick a bare blob. Re-derive after any further edit to `resolve.py` |
| `UFO-HISTORY-NOT-INTACT` | `root-loss-2026-10-12.md:15` | superseded history claim presented as current | UFO substrate for the orphan `main`; kasegi records only | append. Do not rewrite the sentence. Do not treat `964f443e` as false — the pin is live |
| `UFO-DOT-LISTING-DRIFT` | `root-loss-2026-10-12.md:19-20`, `ufo-workspaces.md:171-172` | point-in-time listing pinned to a commit | UFO substrate (ignored runtime); kasegi records | append the 12:44Z stamp. Do not pin the child list to HEAD. Do not delete the old list |
| `FIFTY-NOT-REPRODUCIBLE` | `root-loss-2026-10-12.md:29-30`; source paraphrase at `kumitate-shokunin/SCORECARD.md:630` | superseded count | kumitate for the 2026-10-13 recon wording; UFO substrate for the orphan history; kasegi must not absorb either | do not adopt 50. Do not substitute 970. The sibling paragraph is present; do not record it as missing |
| `BLOB-PIN-LOWERCASE-PATH` | `citation-bases.md:72-73`, `triage-thresholds.md:12` | current command path ABSENT; objects live on the uppercase path | kasegi citation-bases | append the uppercase checkout. Do not rewrite the historical pin list. Do not backtick `fc6d398:SKILL.md` |
| `CENSUS-NOTE-NEVER-LANDED` | `citation-bases.md:43-44` | count cited to a file that was never committed | fleet L0 / operator | accept the L0 row as the record or restore origin-work. Do not invent the missing note |
| `TRIAGE-LOST-BASE-MISPREFIX` | `triage-thresholds.md:21` and the `:52`–`:438` list above | wrong base on lost-tree line numbers; "surviving mirror" present tense | kasegi knowledge | append: read those `[lost-base] fleet-dispatch.mjs` tokens as `[lost-tree]` as-of 2026-09-28T23:32Z. Do not pin them to HEAD `1cfbd86` |
| `CLAIM-CHECK-96-MIRROR-MISBASE` | `claim-package-contract.md:19-22` | lost-tree line written as a mirror anchor | kasegi knowledge | append. Index correction already at `corpus/README.md:29`. Both trees absent |
| `MIRROR-HASH-AS-CURRENT` | `submitted-registry.md:108-109`; `SKILL.md:321`, `:477`, `:816-820`; `ev-model.md:8-10` | content hash of a missing file as current / surviving identity | kasegi knowledge; operator if the mirror is restored | append describe-don't-pin. Do not delete the hashes. Restoring a checkout of `1cfbd86` would make them re-checkable; it does not make the present-tense sentences true today |
| `REPO-STATE-NOW` | `repo-git-state.md:7`, `:15`, `:21` | counts and "now" of an absent repo | kasegi knowledge | append that `~/Projects/bounties` is absent; the 903 / 171 figures are the 2026-09-28 census |
| `RECEIPT-STORE-LOST` | `SCORECARD.md:151-155`, hashes kept at `LOG.md:734-738` | already marked describe-don't-pin | operator | restore `open-bug-bounties` or declare the claims permanently attested. Do not re-pin the hashes |
| `MIRROR-SOURCE-LOST` | `SCORECARD.md:156-160` | every mirror line anchor uncheckable | operator | restore a checkout of `1cfbd86`, or set `$KASEGI_MIRROR`. Not a gate-code change |
| `ORIGIN-REPO-LOST` | `SCORECARD.md:161-165` | historical origin-work quotes; live file claims re-checked above | none for the `964f443e` pin | the `.ufo/` listing and the intact-history sentence are separate rows |

## Axes

- Freshness: the git pin `964f443e` is current; the listing and the intact-history sentence pinned beside it are not. Census rates in the scorecard were already stale at the commit that wrote them.
- Operability: the documented blob-pin command does not run. `$UFO_SRC` is documented as a root and is not read. `anchorcheck.py` `bad=0` does not see wrong-base prefixes or drifted instrument line numbers.
- Calibration: round 20's lesson agrees with the re-measure on the debts it names, and does not mark the source sentences. One additional current-identity class (`MIRROR-HASH-AS-CURRENT`, `CENSUS-README-ROUND18`, `UFO-SRC-NOT-A-CONSUMER`, `RESOLVE-LINE-DRIFT`) is not in the lesson's debt list.
- Adjacency: 50-file wording is kumitate's recon; the orphan `main` and `.ufo/` runtime are the UFO substrate. Kasegi records the drift. It must not absorb either repair. Unmarked openable `Source:` paths are the dead-path seat's list; this seat kept only the pins.
