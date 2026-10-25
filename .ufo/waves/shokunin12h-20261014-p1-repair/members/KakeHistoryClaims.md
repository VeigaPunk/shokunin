# KakeHistoryClaims — advisory inventory

Seat: `kake/HistoryClaims`, revenger, report-only. Starting revision `b0feb30886585d8df6d4671845a2d18989ca722b` (baselines.json; `git -C kake-shokunin rev-parse HEAD` matched). Lane plan: `kake-shokunin/plans/wwkd-round-19-recensus.md`. This file is not a native judge verdict, lane round report, receipt, or admission.

No lane file, gate file, LOG, corpus note, or sibling report was edited. No test, build, lint, formatter, or `freshness-sweep` was run. No external fetch. No push. `plans/` is parent-owned and untracked; left untouched.

## Reconstructed contract

A kake history claim is one of four measured classes, not a recalled label:

- **citation-to-deleted** — a `~/` or `/home/vgpnk/` cite, or a relative cite whose only known base was a deleted tree, whose target `exists()` is false and no surviving object was identified.
- **superseded-revision** — prose or a pin presents a hash, line, count, or literal as current after a later measurement replaced it. Describe the old value as of its round. Do not copy it forward as the current pin.
- **line-drift** — the cited file still exists and the cited line no longer says what the claim says. If the file is gone, this class is not measurable. Do not re-pin the number.
- **stale `--src`** — an explicit `--src` / `UFO_SRC` that points at a bad root and is still honored. Absent in this lane.

The r18 repair already landed: missing concrete paths with an absent-word within ±2 lines of any cite of that token are `declaredAbsent`, exit-neutral. The annotation is token-OR, not sentence-level (`scripts/freshness-sweep.mjs` `scanCitations`, evidence kept from the first annotated cite). A green path section does not mean every imperative is historical. Repeating the r18 comment pass is not the remaining work.

`PROVINCE.md` (6 lines) has no path cite and no revision pin. Empty cluster.

## Evidence chain

1. Captured before receipt, not re-run: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kake-before.json`. `node scripts/freshness-sweep.mjs --offline` at `2026-10-14T23:34:59Z`, exit 0, revision `b0feb30886585d8df6d4671845a2d18989ca722b`. Verdict line: `VERDICT: OK (exit 0, partial: offline)`. Path section: `40 files · 303 occurrences · 68 unique tokens · resolve 5 · declaredAbsent 55 · drift 0 · unresolved 8`. `§history SUSPENDED` on `/home/vgpnk/Projects/webzites/state/probe-history.jsonl`. `§armed` all remote checks `skipped(offline)`, `complete=false`. Informational children: 30, with 16 `omegag-*` names added versus the pin.
2. Independent `exists()` on 2026-10-14, this seat: absent — `~/Projects/origin-work`, `~/Projects/webzites`, `~/Projects/ds4cc-marketplace`, `~/Projects/plazir-15-site`, `~/Projects/lucario`, `~/Projects/ufofsdbeta`, `~/Projects/ephemeral/wz1`, `~/DIRMAP.md`, `~/.config/systemd/user/webzites-{probe,keeper}.{timer,service}`, `~/.config/systemd/user/charter-scribe.{timer,service}`, `~/Projects/ufo-fsd-alpha/.ufo/charter-scribe/ledger.jsonl`. Present — `~/Projects/ufo-fsd-alpha`, `~/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs` (37255 bytes), `~/Projects/ufo-fsd-alpha/docs/charter-ufo-fsd/` (11 entries), `~/Projects/shokunin/.ufo/reports/round-1/web-properties-publishing.md` (3352 bytes).
3. `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9` (short `964f443e`, commit, ancestor of HEAD). `git cat-file -t` failed for `9c28d29`, `9c28d293de181d14898570264d2c4e523ce34255`, `e6bd071887bfaa87eff07ab03d323d5b92760fba`, `bd02d101f4d897df0a76e48758024ddacc2ef1c7`, `f3d2ecd`, `c814526`, `61d0ce6`, `a8f1e2b`. Those objects are not in the surviving repo.
4. `~/Projects` inode still `27238`. Directory mtime `2026-10-14T22:02:04Z`. Direct children 30, not the pinned 14 and not the r17 prose 36.
5. Marker recount over `SKILL.md` + `corpus/**/*.md`: the phrase `r18 re-census` is on 65 lines in 24 files, all containing `<!--`. `corpus/lessons/round-18.md:38` quotes the marker syntax, so path-annotation comments are 64 in 24 files. The lesson's "63 cite lines across 22 files" does not match this recount.
6. Search for `--src` and `UFO_SRC` over `kake-shokunin`: no matches. No stale `--src` surface.
7. Local `docs/charter-ufo-fsd/index.html` (53047 bytes, sha256 `43d321f91cf018dc75d6f0052a573e3f198b0c1a159e0615574f8e0eecc5296b`) contains 0 `scribe beat` literals and calls itself a historical mirror (`index.html:7`). It is not the deleted GHP repo. `9c28d29` is not in this git.
8. One in-repo line pin was re-read: `keeper-timer-inert.md:97` → `publish-queue.md:32` still contains `operator config edit`. That pin held. Webzites `src/*.mjs` and `scripts/kimi-surface.mjs` line pins have no surviving file.

Alpha worktree porcelain (not read, not this lane): `M README.md`, `M config/ufo.json`, `M crates/ufo-core-runtime/bundled/config.json`, `M crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `M scripts/fleet-dispatcher.test.mjs`. The HEAD pin is the commit, not those dirty bytes.

## Clusters

| id | class | classification | evidence | disposition |
|---|---|---|---|---|
| C1 | citation-to-deleted, W7 roots | superseded historical at token level | before receipt: 55 `declaredAbsent`, drift 0. r18 comments on the token. Lesson `round-18.md:36-42` | do not repeat the comment pass |
| C2 | same roots, still read as current procedure | live | `SKILL.md:59`, `:111`, `:303-304`, property-map rows `:17`, `:20`, `:24`, `:26-28` have no comment on that line. Token-OR hides them because another cite of the same token is annotated | named debt; errata below, not applied |
| C3 | check-id table copies r17 literals | live superseded-revision | `freshness-sweep.md:43-53` vs `freshness-pins.json` round 18 | describe-don't-pin; errata below |
| C4 | "Exit 1 is currently the EXPECTED verdict" because plazir is 5 ahead | live superseded-revision (reason falsified) | `freshness-sweep.md:85-91`. `~/Projects/plazir-15-site` absent | reason is false now. Bare exit not re-run. Named debt |
| C5 | deploy/remote hashes `9c28d29`, `e6bd071`, `bd02d10`, `f3d2ecd`, `c814526`, `61d0ce6` | unresolved live pins | pins file still holds `charterGhpDeploy`, `pq2Remote`, `plazirRemote`. `git cat-file -t` failed in the only surviving repo. No fetch this seat | do not re-pin. Named debt |
| C6 | `964f443e` as alpha HEAD | live, still true | `rev-parse HEAD` equals `964f443ee53d…` | do not mark superseded. Do not treat dirty worktree bytes as that commit |
| C7 | scribe ledger cite | superseded historical, still true | r18 comment on `keeper-timer-inert.md:114` and `publish-queue.md:246`. `ledger.jsonl` still absent. `.ufo/charter-scribe/` absent | annotation stands |
| C8 | `…/origin-work/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs` | citation-to-deleted prefix of a relocated file | `keeper-timer-inert.md:91` is not a `PATH_RE` cite (leading `…/`), so the sweep cannot see it. Script exists at `~/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`. `origin-work` absent | describe the new root; do not pin origin-work |
| C9 | `docs/charter-ufo-fsd` inside alpha | not a restoration of the deleted GHP repo | 0 scribe-beat literals; self-described historical mirror; `9c28d29` absent from alpha git | do not retarget `origin-work/charter-ufo-fsd` cites at this tree |
| C10 | `src/cli.mjs` / `src/fleet.mjs` / `src/probe.mjs` / `src/reconcile.mjs` / `scripts/kimi-surface.mjs` / `fleet.config.json` line pins | citation-to-deleted; line-drift unresolved | 82+31+6+10+16+11 pins in SKILL and corpus. Files absent. No second copy found under alpha | do not re-pin lines |
| C11 | `publish-queue.md:32` pin | line-drift not observed | `keeper-timer-inert.md:97` re-read; line 32 still says `operator config edit` | no errata for the line number |
| C12 | `projectsChildrenSet` 36 (prose) / 14 (pin) / 30 (live) | prose is superseded-revision; pin is a frozen baseline, not a world claim | `freshness-sweep.md:44`; pins file 14 names; live listing 30; before receipt printed the 16 added names as informational | do not gate on it. Do not cite 14 or 36 as current |
| C13 | 8 unresolved sweep tokens | unresolved by grammar | before receipt: `~/`, globs `webzites-*.timer`, `grokbot-*.log.md`, `rebuild-*.json`, `recreate-*.json`, `update-*.json`, placeholders `dead-slot-` and `grokbot-` | not live defects |
| C14 | `--src` / `UFO_SRC` | not present | no matches in the lane | not a stale-`--src` defect |
| C15 | marker census 63/22 | superseded count | recount 64 annotation comments / 24 files | describe-don't-pin the lesson's count |
| C16 | `~/Projects` inode `27238` | live, still true | `stat` inode `27238` | no errata |

Relative cites outside `PATH_RE` (before receipt: 384, not resolve-checked) are the carrier for C10. They are not a separate defect class.

## Proposed delta — append-only errata

Not applied. Owner: parent integration / `KakeRecordPrep`. Do not rewrite the cited bytes. Do not delete r18 comments. Do not edit `scripts/freshness-sweep.mjs` or `freshness-pins.json` from this finding.

### Append to `corpus/knowledge/freshness-sweep.md`

```
## Erratum — round 19 history re-census (2026-10-14)

The check-id table's "pinned baseline" column copies r17 literals. Those literals are not current. The pins file is `corpus/knowledge/freshness-pins.json`, `round` 18, `updated` 2026-10-14. Cite the check-id and re-read the file. Do not copy the literal into prose.

| check-id | table literal, historical only | pins file at round 18, still a snapshot |
|---|---|---|
| P2 `pathsMissSet` | 10 entries, r17 | 55 entries |
| P2b `projectsChildrenSet` | 36 entries | 14 entries. Live `~/Projects` children at 2026-10-14T22:02:04Z: 30, including 16 `omegag-*` names added since the pin. P2b is informational, never a gate |
| A1 `charterGhpPin` | `2026-09-26 scribe beat` | `2026-09-30 scribe beat` |
| A1 `charterGhpLiveSha` | `fb365e38…` | `7c243a1d81357cdee71520034a05d540bfe8f69c702a7a1c95f8a0bfa5237aba` |
| A1 `charterGhpChurnAfter` | `2026-09-29` | `2026-09-30` |
| A1 `charterGhpDeploy` | `9c28d29` | file still holds `9c28d293de181d14898570264d2c4e523ce34255`. That object does not resolve in `~/Projects/ufo-fsd-alpha` (`git cat-file -t` failed). The charter git repo is absent. Do not pin the hash as a resolvable current revision |

The r16 sentence "Exit 1 is currently the EXPECTED verdict" because `~/Projects/plazir-15-site` is 5 commits ahead described the r16 world. The directory is absent (re-census `exists()` false). Do not cite "5 commits ahead" or HEAD `c814526` / remote `bd02d10` as current. Those objects do not resolve in the surviving repo. The bare-run exit was not re-measured by this seat. The captured before receipt is `--offline` exit 0 partial, which is not a live pass.
```

### Append to `SKILL.md`

```
## Erratum — round 19 history re-census (2026-10-14)

Token-level absence for the W7 roots is already declared (r18 comments + `pathsMissSet`, 55, drift 0 on the captured `--offline` receipt). That does not make every imperative in this file historical. These sentences still read as current procedure, and their targets are absent. They are named debt, not closed claims:

- :59 `node ~/Projects/webzites/bin/webzites.mjs probe --all` — binary absent. Historical invocation only.
- :111 `node ~/Projects/webzites/scripts/kimi-surface.mjs sync-check` — script absent.
- :303-304 check `~/DIRMAP.md` before classifying lowercase ENOENT — file absent. `projectsChildrenSet` is the replacement instrument, and it is a snapshot (14 pinned, 30 live children), not a complete listing to trust.
- Property-map rows :17 (`plazir-15-site`), :20 (`ds4cc-marketplace/burnerchrome`), :24 (`plazir-15-site`), :26-28 (`lucario`, `lucario/site`, `ds4cc-marketplace/apps-sdk`) have no r18 comment on the row. Rows :16, :18, :19 do. The map header date is 2026-09-28. Treat the whole map as a historical snapshot, not a current source-directory table.
- Line pins `src/cli.mjs:*`, `src/fleet.mjs:*`, `src/probe.mjs:*`, `src/reconcile.mjs:*`, and `scripts/kimi-surface.mjs:*` are citation-to-deleted. Line-drift is not measurable: the files are gone, and no surviving copy was found. Do not re-pin the numbers.

Still true, re-measured, do not mark superseded: `~/Projects` inode `27238`; `~/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`. The pin is the commit. The alpha worktree has unrelated local modifications; those bytes are not the pin.
```

### Append to `corpus/knowledge/keeper-timer-inert.md`

```
## Erratum — round 19 history re-census (2026-10-14)

:91 `ExecStart=…/origin-work/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs` uses a deleted prefix. `~/Projects/origin-work` is absent. The script exists at `~/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs` (37255 bytes). Describe that root. Do not pin origin-work as current. User units `charter-scribe.timer` and `charter-scribe.service` are absent under `~/.config/systemd/user/`.

:92 `61d0ce6` does not resolve in `~/Projects/ufo-fsd-alpha`. The charter repo that held it is absent. Describe the 2026-09-28 beat historically. Do not pin the hash as a current object.

:97 `publish-queue.md:32` was re-read and still contains `operator config edit`. That line pin held. The same row still states config `2026-09-26 scribe beat` versus live `2026-09-28 scribe beat`. The pins file's charter pin is `2026-09-30 scribe beat`, and that literal was not re-fetched this seat. Do not treat the PQ-12 row's 09-26/09-28 pair as the current pin.
```

### Append to `corpus/lessons/round-18.md`

```
## Erratum — marker census (2026-10-14; do not rewrite the lesson)

"63 cite lines across 22 files" is the round-18 count, not a current census. Recount over `SKILL.md` + `corpus/**/*.md`: the phrase `r18 re-census` is on 65 lines in 24 files. `round-18.md:38` quotes the marker syntax, so path-annotation comments are 64 in 24 files. Do not pin 63/22 as the current marker set. The annotations themselves stand.
```

### Describe-don't-pin markings (wording only, not new pins)

- `964f443e` — still HEAD. Say "HEAD at the 2026-10-14 re-census", not "the current bytes" (worktree dirty).
- `9c28d293de181d14898570264d2c4e523ce34255`, `e6bd071887bfaa87eff07ab03d323d5b92760fba`, `bd02d101f4d897df0a76e48758024ddacc2ef1c7`, `f3d2ecd`, `c814526`, `61d0ce6` — deleted-repo objects. Say "as recorded at round N; not resolvable in `~/Projects/ufo-fsd-alpha`". Do not add them to a new pin.
- `src/cli.mjs:361`, `:389`, `:393`, `:78`, `:1087`, `src/fleet.mjs:39-52`, `src/probe.mjs:55`, `src/reconcile.mjs:200-212`, `scripts/kimi-surface.mjs:206-208`, `fleet.config.json:256` — say "line as read in the webzites tree before the 2026-10-12 prune". Do not emit a replacement line number.
- `projectsChildrenSet` — say "r18 snapshot, 14 names; live children were 30 at 2026-10-14T22:02:04Z". Do not re-pin the set in this seat.
- First existing scribe script: `~/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`. The origin-work candidate does not exist. There is no `--src` flag to fail closed; the cite is prose.

## Named debt (retained, not closed)

| debt | why unresolved | unblock | owner |
|---|---|---|---|
| KAKE-DEBT-PQ2 | `~/Projects/ds4cc-marketplace` absent. Round-18 already recorded gate `ANOMALY`. Not re-run here | restore the repo, or declare PQ-2 dead in an append-only note | operator; parent records |
| KAKE-DEBT-PQ14 | `~/Projects/plazir-15-site` absent. "5 ahead" reason is falsified; current bare verdict not re-measured | restore the repo, or declare PQ-14 dead | operator; parent records |
| KAKE-DEBT-HISTORY | `probe-history.jsonl` absent; `probeHistoryAbsent: true` suspends the section | restore webzites `state/`, or point `KAKE_PROBE_HISTORY` at a surviving copy | operator |
| KAKE-DEBT-DEPLOY-HASH | `charterGhpDeploy` / `pq2Remote` / `plazirRemote` do not resolve locally. Live remotes not fetched | a later seat with an allowed fetch, or a restored clone. Do not invent a new hash | `KakeLiveAnchors` if a fetch is in scope; else operator |
| KAKE-DEBT-LINEPINS | webzites line pins have no file to diff | a surviving `webzites` tree. Until then the numbers are historical | this seat's errata; no gate edit |
| KAKE-DEBT-BARE-VERDICT | before receipt is `--offline` exit 0 partial. Round-18 bare exit 1 was not re-measured | parent gate after integration. Do not read the offline OK as a live pass | parent |
| KAKE-DEBT-DIRMAP-PROCEDURE | `SKILL.md:303-304` still instructs a check of a deleted file | append the SKILL errata above. Do not delete the W6 paragraph | `KakeRecordPrep` |
| KAKE-DEBT-CHILDREN | pin 14 vs live 30 is informational by P2b. SCORECARD "now holds 14 children" is outside this seat's files and is stale if read as current | RecordPrep may append a SCORECARD note. Do not re-pin from this seat | `KakeRecordPrep` |

## Cross-domain

- `KakeGateRepair`: no remaining falsified gate defect from this inventory. Missing history is already `SUSPENDED` (`probeHistoryAbsent`). Missing plazir/ds4cc dirs already throw into `ANOMALY` on the non-offline git path (`checkPlazir` catch, `freshness-sweep.mjs:680`). There is no `--src` to repair. Do not add a `UFO_SRC` resolver to make a deleted root resolve. Explicit absence must stay absence.
- `KakeLiveAnchors`: live URL, beat literal, and sitemap claims were not fetched here. C5 stays unresolved until a fetch or a restored clone.
- `KakeRecordPrep`: the four errata blocks above are the proposed append. Do not rewrite LOG or the r18 lesson body.
- ufo-fsd-alpha checkout (not this lane): `scripts/charter-scribe/systemd/charter-scribe.service:10-11` still sets `WorkingDirectory` and `ExecStart` under `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`, which does not exist. The script itself is at the new root. Source checkout is read-only for this wave.
- kasegi / L0: `SKILL.md:307-308` still records the shared 2026-09-28 `bounties` loss. `~/Projects/bounties` is in `pathsMissSet` and was `declaredAbsent` on the before receipt (`publish-queue.md:214`). Not re-opened.

## Axes (advisory, not scores)

- Freshness: the r18 token repair holds (drift 0 on the captured receipt). The remaining freshness defect is prose that still presents r17 pin literals and deleted-repo hashes as current (C3, C4, C5).
- Operability: checklist steps at `SKILL.md:59` and `:111` are not runnable. That is carried debt, not a new script defect.
- Calibration: token-OR annotation plus a green offline path section can be read as "every cite is historical". It is not. The 63/22 census sentence is itself a stale count.
- Adjacency: scribe unit path and the in-tree charter mirror belong to the alpha checkout. Live beats belong to `KakeLiveAnchors`. Gate behavior is already fail-closed; no implementation change from this seat.

## Divergences from the round-18 lesson

- "63 / 22" does not match the recount (64 annotation comments / 24 files).
- HEAD `964f443e` was not superseded.
- `sync.mjs` was relocated, not deleted. The lesson did not claim the script was deleted; the `:91` cite was outside `PATH_RE` and was not annotated.
- `docs/charter-ufo-fsd` inside alpha is a different artifact from the deleted GHP repo. Do not treat the prune as a move of that repo.
- `~/Projects` children are 30, not 14. The pin is a baseline. The world moved after it (directory mtime 2026-10-14T22:02:04Z).

## Confidence

High on absence of the W7 roots, on HEAD equality, on the check-id table contradicting the pins file, on `61d0ce6` / `9c28d29` / `e6bd071` / `bd02d10` not resolving in alpha, and on the scribe script's new path. Unresolved, and left unresolved, on live HTTP state and on the current bare-run exit code. No gate change is justified from this seat.
