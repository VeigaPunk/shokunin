# KasegiLiveAnchors

Advisory measurement only. Not a native judge verdict, lane round report, receipt, or admission. No lane file was edited. No gate, build, lint, test, or formatter was run.

Axes walked: freshness (pins vs current bytes), operability (can a reader open the claimed source), calibration (count/hash vs command), adjacency (sibling citation, not adopted as this lane's count).

## Revisions measured

| surface | command | output |
|---|---|---|
| kasegi HEAD | `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin rev-parse HEAD` | `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` (matches `baselines.json` kasegi.head). Porcelain: `?? plans/` only. |
| ufo-fsd-alpha HEAD | `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD` and `git log -1 --format='%H%n%s%n%an <%ae>%n%aI'` | `964f443ee53df0ce06bd689af01f0dea031b01f9`; subject `routing: regenerate omp-seat-routing mirror from the live global config (operator: ompskills host apply)`; author `ci <ci@local>`; author/commit date `2026-10-12T18:32:12-03:00`. `git rev-list --count 964f443ee53df0ce06bd689af01f0dea031b01f9..HEAD` = `0`. Toplevel `/home/vgpnk/Projects/ufo-fsd-alpha`. |
| source-root candidates | `[ -d … ]` | PRESENT `/home/vgpnk/Projects/ufo-fsd-alpha`. ABSENT `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`, `/home/vgpnk/Projects/origin-work`, `/home/vgpnk/Projects/origin-work/open-bug-bounties`, `/home/vgpnk/Projects/the-bounty-hunter`, `/home/vgpnk/Projects/bounties`, `/home/vgpnk/Projects/open-bug-bounties`. `find /home/vgpnk -maxdepth 4 -type d` for those five names printed only `/home/vgpnk/Projects/ufo-fsd-alpha`. |

Worktree note, not a kasegi claim: `git -C /home/vgpnk/Projects/ufo-fsd-alpha status --porcelain --untracked-files=no` shows `M` on `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs`. Skill and sighting paths below were clean (worktree bytes = HEAD blob). Diffs of the dirty files were not read.

## Claim inventory

Currently live OMP-derived claims are the present-tense pins in `SKILL.md:28-29`, `SCORECARD.md:128`, `SCORECARD.md:161-165`, `LOG.md:795-802`, `corpus/README.md:34`, `corpus/README.md:56-57`, `corpus/knowledge/root-loss-2026-10-12.md:15-22`, `corpus/knowledge/root-loss-2026-10-12.md:27-30`, `corpus/knowledge/root-loss-2026-10-12.md:54-56`, `corpus/knowledge/ufo-archive-2026.md:31`, and `corpus/knowledge/ufo-workspaces.md:169-173` plus `:309-314`. Lost-tree / lost-base / quoted `UFO_ROOT=` text was not re-anchored. No live `` `path:line` `` token into `ufo-fsd-alpha` exists in this lane (search for `scripts/…:digits` and `crates/…:digits` returned no matches).

### Holds

1. **HEAD hash, subject, timestamp.** Claimed at `root-loss-2026-10-12.md:15` and `:17`, and repeated as current at `SKILL.md:28-29`, `SCORECARD.md:128`, `corpus/README.md:34` and `:57`, `LOG.md:796`, `ufo-archive-2026.md:31`, `ufo-workspaces.md:171` and `:312`. Measured output matches the full hash, the subject prefix `routing: regenerate omp-seat-routing mirror…`, and `2026-10-12T18:32:12-03:00`. Not line-drift. Proposed anchor: keep `964f443ee53df0ce06bd689af01f0dea031b01f9`. Precision only: `root-loss-2026-10-12.md:27` says the commit is timestamped "by ompskills host apply"; that phrase is inside the subject (`operator: ompskills host apply`). Git author is `ci <ci@local>`. Do not rewrite the subject quote.

2. **Named tree presence.** `root-loss-2026-10-12.md:12-15` and the detection loop at `:38-42`. Same PRESENT/ABSENT result as the table above. First existing `$UFO_SRC` candidate, if a deriver existed, would be `/home/vgpnk/Projects/ufo-fsd-alpha`. The origin-work candidate is absent, so this is not a stale `--src` selection. Proposed anchor: unchanged paths.

3. **`scripts/ufo-sighting.mjs` survives at that HEAD.** `ufo-archive-2026.md:31`. Command: `test -f` plus `git show HEAD:scripts/ufo-sighting.mjs` hashed in-process. File present. Worktree = HEAD. `wc` newlines = `4714`. SHA-256 `5e8ea127e5244b1edec4d35b40a201d4fb4057dc316506582a8e5e9e2f09d19e`. Identity symbol, not previously line-pinned: `command === "launch"` at `scripts/ufo-sighting.mjs:4555`; `async function launchMission` at `:2372`. Not line-drift. Proposed anchor if a line is added later: `:4555` at this revision, not a remembered kumitate line.

4. **Canonical skill is 600 lines at this HEAD, and current bytes differ from the recorded 626-line hash.** `ufo-workspaces.md:310-313`. Command: SHA-256 and newline count of worktree and `git cat-file -p HEAD:<path>` for `skills/ufo/SKILL.md`, `.omp/skills/ufo/SKILL.md`, `.cursor/skills/ufo/SKILL.md`. All three identical. `600` newlines, trailing newline, SHA-256 `4708d14d99fcb5184f72eb386d9e9efeefcafe96a4874d0314eb54f773fe7ef2`. Header identity: `skills/ufo/SKILL.md:2` `name: ufo`. Not line-drift. Proposed current anchor: `skills/ufo/SKILL.md:1-600` at `964f443ee53df0ce06bd689af01f0dea031b01f9`, hash prefix `4708d14d`.

5. **Historical 626 / `40949973…` is a real blob, not the current file.** Same sentence, marked "when measured" / "round-13 evidence". It is absent from HEAD's followed history of `skills/ufo/SKILL.md` (`git log --follow` = 1 commit, one blob, the 600-line hash above). It is present at `remotes/cursor/clean/clean-siblings:skills/ufo/SKILL.md`: `626` newlines, SHA-256 `40949973e6476bcab87f3693ce60e78670a483113d2c1b5c40f421b3b506a184`. Classification: historical hash holds; not a current pin; not line-drift. Do not retarget the round-13 prefix onto `:1-600`.

6. **`hunt-*` dangling claim still holds.** `ufo-workspaces.md:169-173` and `root-loss-2026-10-12.md:20-22`. Commands: `find /home/vgpnk/Projects/ufo-fsd-alpha -maxdepth 4 -name 'hunt-*' | wc -l` = `0`; `find … -maxdepth 4 -type d -name missions` printed nothing; `[ -e .ufo/missions ]` = ABSENT. Not line-drift. Proposed anchor: keep the absence claim; do not attach it to the exclusive child list in item 8.

7. **Kumitate paragraph pointer lands.** `root-loss-2026-10-12.md:28-30` names `kumitate-shokunin/SCORECARD.md`, environmental-findings paragraph. The prose lead-in is `SCORECARD.md:623` `**Environmental findings (2026-10-13 recon, recorded — not absorbed).**` through `:633`. Not a line-numbered cite, so not line-drift. The exact string `50 upstream file deletions` is kasegi's paraphrase and is absent from that file; the sibling sentence is `:630` `50 files deleted`. An exact `git log -S` or grep for kasegi's phrase against kumitate misses the hit. The number was not adopted as this measurement (item 9). Re-read after a peer absence claim: `:630` still present.

### Genuine defect (not line-drift)

8. **Exclusive `.ufo/` child list is false as a current inventory.** Claimed at `root-loss-2026-10-12.md:19-20` and `ufo-workspaces.md:172`: only `cache scopes sighting statusline-cache.json statusline-full.stamp`. Command: `ls -1A /home/vgpnk/Projects/ufo-fsd-alpha/.ufo`. Measured names: `cache`, `contract-sync`, `rs-self-iter-blocked.json`, `scopes`, `sighting`, `statusline-cache.json`, `statusline-full.stamp`. Extra names are gitignored (`.gitignore:4` `**/.ufo/`). Their directory mtimes are `2026-10-14 20:16:04 -0300` (`stat` on `contract-sync` and `rs-self-iter-blocked.json`). Contents were not read. This is runtime inventory drift on an untracked tree, not a moved line and not a superseded git pin (HEAD has not moved). The dangling conclusion in item 6 still holds. Proposed delta: date the six-name list as the 2026-10-14 re-census snapshot and record the seven current names; do not invent a `hunt-*` restoration. Owner: parent / RecordPrep for the note. Not a gate file.

9. **Repeated "50 upstream file deletions" does not reproduce.** `root-loss-2026-10-12.md:28-29` states that kumitate measured 50. Independent commands against the pin that paragraph uses (`5725fa7d3`, full `5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70`):
   - `git merge-base HEAD 5725fa7d3` exit 1, empty (no common ancestor).
   - `git rev-list --left-right --count 5725fa7d3...HEAD` = `861 3`.
   - `git rev-list --count HEAD` = `3`. Roots: `72ab84a80c4033aa1182654fb3f288bb7ff446c4`. Exclusive commits `72ab84a8`, `5ace2559`, `964f443e` each have `git diff-tree --diff-filter=D --name-only -r` count `0`.
   - `git diff --diff-filter=D --name-only 5725fa7d3 HEAD | wc -l` = `970` (scripts 41, tests 115, reports 735, other non-reports 79). No natural slice of that command was 50; the count was not fitted.
   - The three script names in the kumitate paragraph are absent from the HEAD tree and are inside the 970-name cross-history diff: `scripts/atomic-write.mjs`, `scripts/charter-scribe/sync.test.mjs`, `scripts/collect-omp-native-handoff-lib/refusal-line.mjs`.
   Classification: genuine count defect, not line-drift. The citation that kumitate wrote "50" holds (item 7); the source fact does not. Proposed correct anchor: do not pin 50. Say HEAD's own history deleted 0 files in 3 commits, and a cross-history name-diff against `5725fa7d3` is 970 because that pin is not an ancestor. Owner: kumitate for their recorded count; parent / RecordPrep if kasegi repeats it. Not a gate file.

10. **`$UFO_SRC` derivation is claimed and absent.** `LOG.md:801-802`, `SCORECARD.md:164-165`, `root-loss-2026-10-12.md:54-56` say `anchorcheck.py` and `resolve.py` derive `$UFO_SRC` / `ufo-fsd-alpha` as first existing candidate, new path first. Code: `corpus/instruments/anchorcheck.py:75-97` derives only `KASEGI_MIRROR` and `KASEGI_ORIGIN_ROOT`. `CITE` at `anchorcheck.py:104` does not accept `~/Projects/ufo-fsd-alpha/…:line`. `resolve.py:85-95` derives only the mirror. Absolute `~/Projects/ufo-fsd-alpha/scripts/ufo-sighting.mjs` still classifies RESOLVES by literal existence (`corpus/instruments/citation-survival.tsv:1472`). No current `path:line` cite into that tree is being skipped. Classification: genuine defect of the prose self-claim, not line-drift, not a stale `--src`, and not a root-default runtime miss (literal expansion already opens the live path; r19 mirror/origin derivation is the gate that exists). `KasegiGateRepair` measured the same gap and decided no instrument edit (MEASURED UNCHANGED). Do not add unused `$UFO_SRC`/`CITE` surface to make the sentence true. Proposed delta: append-only errata that the deriver was not landed. Owner of the draft: KasegiHistoryClaims. Landing: parent. Not this seat.

11. **"History intact" overclaims ancestry.** `root-loss-2026-10-12.md:15` says the relocated tree is the same repo with history intact. Object presence holds: `5725fa7d3` resolves, and `git branch -a --contains 5725fa7d3` lists `remotes/cursor/clean/clean-siblings` (also `remotes/cursor/clean/clean-audit`, `remotes/cursor/selfrefine/shokunin`, `remotes/cursor/selfrefine/kernel`). The 626-line skill blob in item 5 is on that remote. Checked-out HEAD does not descend from that line (item 9). Classification: genuine defect of the ancestry reading; not line-drift; not citation-to-deleted. Proposed correct anchor: HEAD ancestry is the 3-commit orphan chain rooted at `72ab84a80c4033aa1182654fb3f288bb7ff446c4`; pre-relocation history is present as those remote refs, not as parents of `964f443e`. Owner: parent / RecordPrep for an append-only errata. Do not rewrite the original sentence in place.

### Dated, not a live invariant

12. **`.git` mtime `2026-10-14 09:40:50 -0300`.** `root-loss-2026-10-12.md:18`, inside a note dated `2026-10-14T12:44Z`. Current `stat -c '%y' .git` = `2026-10-14 20:38:29.147422745 -0300`. The old instant cannot be re-proved. Not a defect of that dated sentence. Do not re-pin it as current.

### Unremeasurable, not classified as a live defect

13. **Fork `304 l / 2d5bfd3e…` and "cites `scripts/{sync-ufo-contracts,…}` that don't exist in bounties".** `ufo-workspaces.md:309-315`. Grammatical subject is the lost `.omp/skills/ufo/SKILL.md` fork. `~/Projects/bounties` is absent, so the fork hash and the bounties-side absence cannot be remeasured. Current canonical skill has 0 matches for `sync-ufo-contracts` (grep of `skills/ufo/SKILL.md`). The script does exist in the OMP tree at `scripts/sync-ufo-contracts.mjs` (`2273` newlines, SHA-256 `fb9d3137f2dbe1c4e83c1e6461197e213548abc638ac4287e66ccff76fb1d22a`); the sentence does not deny that. Leave the fork clause historical. Do not retarget it onto the canonical skill.

14. **Quoted `UFO_ROOT=~/Projects/origin-work/ufo-fsd-alpha`.** `ufo-workspaces.md:98-99` already marks this as a quote of the lost launch script. Correctly not a live env pin. History-claims seat, not repaired here.

## Proposed delta (report only)

No implementation change from this seat. Parent should not treat a clean HEAD-hash re-check as proof that every live OMP sentence still holds.

- Keep items 1-7 as current anchors.
- Errata, append-only, for items 8, 9, and 11. Do not delete the original sentences.
- Item 10 is not a gate edit. `KasegiGateRepair` decided MEASURED UNCHANGED. The false sentence at `LOG.md:802`, `SCORECARD.md:164`, and `root-loss-2026-10-12.md:55` remains named debt for an append-only errata (HistoryClaims drafts; parent lands). Do not invent `$UFO_SRC` wiring to erase it.

## Unresolved debt

- Past `.git` mtime and the past exclusive `.ufo/` listing cannot be reconstructed; only current names and mtimes were measured.
- Fork hash `2d5bfd3e…` remains unprovable while `~/Projects/bounties` is absent.
- What command produced kumitate's 50 was not recovered. This measurement did not search their scripts or assume the number. Unblock: kumitate publishes the exact `git diff` argv, or kasegi stops repeating 50.
- Dirty ufo-fsd worktree files listed above were not hashed. No kasegi live claim pins them. Unblock only if a later cite treats those paths as HEAD bytes.
- `find ~ -maxdepth 5 -iname '*bount*'` from the note was not re-run. The named directory test and the maxdepth-4 name search above were.

## Cross-domain owner

| finding | owner |
|---|---|
| Items 8, 9, 11 prose errata | parent / KasegiRecordPrep (notes, SCORECARD, LOG). Not this seat. |
| Item 9 source count | kumitate (their SCORECARD paragraph). Kasegi must not adopt it. |
| Item 10 prose, not instruments | KasegiHistoryClaims drafts the errata; parent lands it. KasegiGateRepair: no edit. |
| Item 6 dangling `hunt-*` vs lost bounty transcripts | stays kasegi corpus; no OMP file to repair. |
| Historical lost-base line cites | KasegiHistoryClaims. Not re-inventoried here. |
