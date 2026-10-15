# Kake historical marking — describe-don't-pin

Lane: `kake-shokunin`. Audited commit: `59948314e9af5dd6ef81894fc1c422b353f10938` (nested repo HEAD; parent odb does not contain the object). Identity `kake-shokunin <kake@shokunin.local>`, subject `round-19: OMP-era freshness re-census (measured gates; records + scoped repair)`. Worktree dirty only as untracked `plans/` (outside the commit; not a pin source). Read-only. No lane file edited. No gate run. No external fetch. Remote body hashes were not re-measured.

Rule applied: a superseded count, hash, pid, or line number may stay if the sentence is marked historical / describe-don't-pin. A content hash of a missing file must not be stated as that file's current identity. A row in `freshness-pins.json` is a drift baseline, not a presence claim, only when prose does not also say the absent tree currently is that hash or that count.

## Verdict on the lane's own record

| Claim | Verdict | Why |
|---|---|---|
| `corpus/lessons/round-19-recensus.md:37-40` `SKILL.md:59` / `:111` still name deleted webzites binaries; not rewritten | **agree** | `:59` is `node ~/Projects/webzites/bin/webzites.mjs probe --all`. `:111` is `node ~/Projects/webzites/scripts/kimi-surface.mjs sync-check`. Both trees absent. These are current-voice procedure cites, not hash pins. Dead-path seat owns the path class. |
| same lesson: `freshness-sweep.md:43-53` copies pre-r18 pin literals | **agree** | Table column is "pinned baseline". Literals disagree with `freshness-pins.json` (round 18) and, for children, with the live directory. Detail below. |
| same lesson: `SCORECARD.md:20` says 14 `~/Projects` children; receipt measures 30 | **agree** | Pin set length 14. Live listing 30 (2026-10-14, this seat). The 14 names are a subset; 16 `omegag*` names are added; none of the 14 are gone. |
| lesson does not claim the rule is satisfied; stale prose "recorded, not rewritten" | **agree** | The three named sites are real. They are not the whole set. |
| `SCORECARD.md:22-23` `origin-work/*` cites are all marked absent-historical | **disagree if read as covering revision pins** | Path comments exist. Standing ledger rows still state missing-repo HEAD/remote hashes and "5 commits ahead" / "live `2026-09-28`" as the current queue. |
| `SCORECARD.md:22` / round-18 lesson: alpha HEAD `964f443e` | **agree** | `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` = `964f443ee53df0ce06bd689af01f0dea031b01f9`. Not a superseded pin. |
| round-19 lesson `:23` selftest region marks `B19,B1083,E1139,B1298,E1300,B1318,E1320` | **agree on the line pins** | Those script lines contain the `SELFTEST-WRITES-*` markers the recorder scans. Selftest was not re-run here. |
| round-18 lesson `:38` / `LOG.md:413` / `SCORECARD.md:43` "63 cite lines in 22 files" now carry the erratum | **disagree as a current census** | Measured 64 lines matching `<!-- r18 re-census` in 24 files, after dropping the prose mention of the opener at `round-18.md:38`. |

## Commands (this slice)

Lane identity, from `kake-shokunin/`:

```text
git rev-parse HEAD
→ 59948314e9af5dd6ef81894fc1c422b353f10938
git status --short
→ ?? plans/
git merge-base --is-ancestor 59948314e9af5dd6ef81894fc1c422b353f10938 HEAD
→ exit 0
```

Parent repo, `/home/vgpnk/Projects/shokunin`:

```text
git rev-parse HEAD
→ 5ec4b43280e5cad3698a7e71b7b301e5ccdb0883
git cat-file -t 59948314e9af5dd6ef81894fc1c422b353f10938
→ exit 128, bad object
```

Host facts (no content read of credentials; no fetch):

| Command | Exit | Result |
|---|---|---|
| `stat -c '%i %n' /home/vgpnk/Projects` | 0 | inode `27238` |
| `stat` `/home/vgpnk/projects` | 2 | absent |
| directory listing of `~/Projects` (non-dot names) | 0 | **30** children |
| `test -e` webzites, ds4cc-marketplace, plazir-15-site, lucario, origin-work, `~/DIRMAP.md` | 1 each | absent |
| `test -e` the four `webzites-{probe,keeper}.{service,timer}` units | 1 each | absent |
| `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` | 0 | `964f443ee53df0ce06bd689af01f0dea031b01f9` |
| `test -e` `…/ufo-fsd-alpha/.ufo/charter-scribe/ledger.jsonl` | 1 | absent |
| `systemctl --user list-unit-files 'webzites-*' 'charter-scribe*'` | 0 | empty |
| `systemctl --user list-timers --all` | 0 | only `ai-usage.timer` |
| `git cat-file -t` in alpha and in kake for `9c28d293…`, `e6bd0718…`, `bd02d101…`, `61d0ce6`, `c814526`, `f3d2ecd`, `a8f1e2b` | n/a | all `MISSING` |

Pin-file lengths, parsed from `corpus/knowledge/freshness-pins.json` (`round` 18): `pathsMissSet` 55, `projectsChildrenSet` 14, `pathsFiles` 40.

## Counterexamples (presented as current)

### Counts and hashes in the living check-id table

`corpus/knowledge/freshness-sweep.md:40-53` is the standing instrument contract ("pinned baseline"), not a dated run transcript. `:68-70` says never copy a pinned literal into prose. The table does, and the copies are pre-r18.

| Line | Prose, as current pin | Measured |
|---|---|---|
| `:43` | `pathsMissSet` (10 entries, r17) | pins file **55** |
| `:44` | `projectsChildrenSet` (36 entries) | pins file **14**; live directory **30** |
| `:45` | `pathsFiles` (39-entry list, "now the real list") | pins file **40** |
| `:49` | A1 `2026-09-26 scribe beat`, live sha `fb365e38…`, churnAfter `2026-09-29` | pins file pin `2026-09-30 scribe beat`, sha `7c243a1d81357cdee71520034a05d540bfe8f69c702a7a1c95f8a0bfa5237aba`, churnAfter `2026-09-30` |
| `:51` | `pq2Remote` `e6bd071` / 20 unpushed | `~/Projects/ds4cc-marketplace` absent; object does not resolve locally |
| `:53` | `plazirRemote` `bd02d10` / 5 unpushed / locs 8 vs 7 | `~/Projects/plazir-15-site` absent; object does not resolve locally |

`:49` is a superseded content hash stated as the current armed pin. It is a remote-body hash, not the sha256 of a missing local file. The loaded pin is `7c243a1d…`. Do not re-fetch to "fix" it from this seat.

`corpus/knowledge/freshness-sweep.md:85-87` — "**Exit 1 is currently the EXPECTED verdict**" because `~/Projects/plazir-15-site` is 5 commits ahead. The directory is absent. Round-18/19 records say the bare drift is PQ-2 + PQ-14 `ANOMALY`, not that lead. The lesson names `:43-53` and does not name `:85-87`.

### Standing score and planned section

- `SCORECARD.md:20` — "`~/Projects` now holds 14 children". Live count 30. Lane already records this. Confirmed.
- `SCORECARD.md:9` — current freshness evidence cell, not a move-log row. Prefixed `r17 HOLD 10`, then present tense: "Live exit 1 **remains** solely expected PQ-14 `plazir-live-source-gap`"; `--selftest` **10/10**; `projectsChildrenSet` 36; `pathsFiles` 39-entry. Round-19 lesson records selftest **13/13**. The `r17` prefix dates the paragraph and does not mark the "remains" clause historical.

### Missing-checkout hashes stated as the current queue

These objects do not resolve in kake or in `~/Projects/ufo-fsd-alpha`. No fetch was made. They are commit hashes of missing trees, not file-content hashes.

- `corpus/knowledge/publish-queue.md:32` — standing PQ-12 row: config `2026-09-26 scribe beat` vs live `2026-09-28 scribe beat`, deploy-current `a8f1e2b`, `fleet.config.json:256`. Loaded pin and `SCORECARD.md:25-26` say the beat pin is `2026-09-30` / `7c243a1d…`. No r18 marker on the row. Dated parenthetical `(verified r7 + r12 + r13)` does not retract the row as the current fix.
- `corpus/knowledge/publish-queue.md:34` — "**source is 5 commits ahead**" HEAD `c814526`, remote `bd02d10`. Source directory absent.
- `corpus/knowledge/drift-detection.md:42` — under "Observed drift state (2026-09-26)", the r16 correction is still present tense: "source **is** 5 commits ahead of `origin/main`". r18 markers are at `:4` and `:7`, outside ±2. Heading date mitigates; the correction is the sentence a reader would use as the standing falsification, and the source is now absent, not 5 ahead.
- `corpus/knowledge/drift-detection.md:79-80` — `HEAD c814526`, remote `bd02d10`, count 5. Section heading is "Fresh probe — 2026-09-28". Treated as a dated transcript, not a current-identity claim. Listed so the dated block is not silently folded into `:42`.

`SKILL.md:71-75` still says `webzites-probe.timer` runs `probe --all` every 6h and `webzites-keeper.timer` is loaded + disabled + inactive. Units are absent; `list-timers` shows only `ai-usage.timer`. `SKILL.md:353` says the scribe push-gate is "**currently** failing". Ledger path absent; no `charter-scribe` unit. Current-voice host state, not a file-content hash.

### Line numbers

Missing-file coordinates in the living checklist, no historical marker on the line. `~/Projects/webzites` is absent, so the numbers are not re-derivable. Do not re-pin them.

- `SKILL.md:88` `src/cli.mjs:78`
- `SKILL.md:90` `src/fleet.mjs:39-52`
- `SKILL.md:93` `src/fleet.mjs:30-37`
- `SKILL.md:102-103` `src/fleet.mjs:39-52`, `src/cli.mjs:78`
- `SKILL.md:105` `src/cli.mjs:99`
- `SKILL.md:107` `:94-97` (continuation of `src/cli.mjs`)
- `SKILL.md:171` `src/probe.mjs:55`
- `SKILL.md:211-213` decision-table pins into `src/cli.mjs`, `src/reconcile.mjs`, `scripts/kimi-surface.mjs`

Same class, broader living index (`SKILL.md`, `SCORECARD.md`, `corpus/README.md`, `corpus/knowledge/*.md`), unmarked pins to files that are not in this repo and whose host trees are absent: `src/cli.mjs` 72, `src/fleet.mjs` 26, `scripts/kimi-surface.mjs` 16, `src/reconcile.mjs` 10, `src/probe.mjs` 6, `bin/webzites.mjs` 4, `fleet.config.json` 10. Many sit under round-11/12 dates inside `free-read-verbs.md`. README still indexes that file as the verb contract. Not 144 separate defects; one class.

Missing-file line pin in the current trap section:

- `SKILL.md:302` cites `~/DIRMAP.md:1,7,27`. File absent. No r18 marker on `:302-304`. `SCORECARD.md:31-32` says DIRMAP is marked historical; this cite is not.

In-repo line drift (target exists, cited range no longer holds the sentence):

- `corpus/knowledge/free-read-verbs.md:13` pins `SKILL.md:56-58` for "bare `webzites` is not on PATH". `:56` is blank, `:57` is the checklist heading, the PATH sentence is `:59-61`.
- `corpus/knowledge/free-read-verbs.md:110` pins `SKILL.md:100-105` for "read stdout, never gate on the exit code". That sentence is `:107-108`. `:100-105` is the phantom-diff warning and the start of the status exit-1 claim.

Held, not counterexamples: `keeper-timer-inert.md:97` → `publish-queue.md:32` still contains `operator config edit`. `keeper-timer-inert.md:128-129` correctly marks old `SKILL.md:58-61` historical; `:68-75` still overlaps the keeper-disabled paragraph (`:71-75`). `ops-automation.md:13` still matches the probe-timer row cited from `keeper-timer-inert.md:49` (r18 comments were appended, not inserted as new lines).

### Content hash of a missing file as current identity

**No unmarked sentence asserts a sha256 of a missing local file as that file's current byte identity.**

Marked or dated, not violations of this clause:

- `corpus/knowledge/origin-repos.md:15` — live index sha `b6f65899…` "also == `~/Projects/ds4cc-marketplace`" with a same-line r18 comment, under "r5–r8". Path is absent. Hash is retained as a historical receipt, not a current file identity.
- `origin-repos.md:16` — `20805500…` for `repos/VeigaPunk.github.io`. Same dated section. No same-line marker. Verdict word "byte-verified" is present tense; the heading dates the table. Not counted as a current-identity assertion.
- `corpus/knowledge/free-read-verbs.md:93` and `:323-324` — `probe-latest.json` / `probe-history.jsonl` sha256 `8c5bb8ca…` / `31b8be9f…` are the r11 21:30Z experiment receipt. Files absent. Dated, not current identity.
- `publish-queue.md:261` — `b6f65899… == origin/main:index.html` sits in the r16 dated section. Historical transcript.
- `freshness-pins.json` `charterGhpLiveSha` / `pq5Sha` / `vaultSha` are remote-body baselines. `charterGhpDeploy` / `pq2Remote` / `plazirRemote` are commit baselines of trees that are absent. The file comment says baselines and drift predicates. Not "the missing file's bytes are this hash." Not re-measured against the network.
- `scripts/freshness-sweep.mjs:92-96` labels `R15_LIVE_SHA` (`fb365e38…`) as the r15 snapshot hash. `:823-824` skips a missing `/tmp/kake-r15/charter-live.html` instead of treating it as current identity. `:73` still embeds that same hash in `DEFAULT_PINS`. `loadPins` prefers the pins file when it exists, so this is a latent fallback, not the loaded pin.

## Not counterexamples

- Dated LOG entries and `corpus/lessons/round-N.md` narrating what was true at that round, including old shas and "5 ahead" inside a round heading. Genre is historical. Exception: a later standing sentence that says the round's count is what the tree **now** carries (`63/22`).
- `SKILL.md:299` inode `27238`. Still true (`stat`). Lowercase inode `101125103` is in the same "at r16" sentence; the directory is absent. Not a false current pid/inode.
- No process-id revision pin. `scripts/freshness-sweep.mjs:1099` `process.pid` is a runtime selftest directory name, not a claim.
- Alpha HEAD `964f443e`. Still true.

## Named debt

| Id | What | Owner / unblock |
|---|---|---|
| KAKE-DEBT-CHECKID | `freshness-sweep.md:43-53` and `:85-87` state pre-r18 literals and a falsified "currently expected" exit reason | kake prose. Append a describe-don't-pin pointer at `freshness-pins.json`. Do not copy a new literal into the table. Do not delete the r16/r17 transcript. |
| KAKE-DEBT-CHILDREN | `SCORECARD.md:20` "now holds 14" vs live 30. Pin 14 is an r18 snapshot, informational under P2b | kake record. Append the live count as a measurement, not a re-pin. Do not gate on children. |
| KAKE-DEBT-SCORE-CELL | `SCORECARD.md:9` "remains solely expected PQ-14" and selftest 10/10 | kake record. Append that bare drift is the r18/r19 ANOMALY pair and that round-19 records selftest 13/13. Do not rewrite the r17 cell in place. |
| KAKE-DEBT-QUEUE-HASH | `publish-queue.md:32`, `:34`; `drift-detection.md:42` | kake. Append a historical banner. Do not invent a replacement hash. Objects do not resolve locally; fetch was out of scope. |
| KAKE-DEBT-LINEPINS | SKILL checklist pins listed above; `SKILL.md:302` DIRMAP lines; the knowledge-file class | kake. Unblock is a restored tree, or an append-only "coordinates of a deleted tree; do not re-pin." |
| KAKE-DEBT-LINE-DRIFT | `free-read-verbs.md:13` (`SKILL.md:56-58` → `:59-61`); `:110` (`:100-105` → `:107-108`) | kake. Append the current range. Do not rewrite the round-11 sentence. |
| KAKE-DEBT-CENSUS | 63/22 vs measured 64 `<!-- r18 re-census` lines in 24 files | kake record. Describe the recount. Do not delete comments to match 63. |
| KAKE-DEBT-FALLBACK-SHA | `freshness-sweep.mjs:73` fallback `fb365e38…` | kake instrument, latent while the pins file loads. Not a live identity claim. Do not treat as a reason to re-pin. |
