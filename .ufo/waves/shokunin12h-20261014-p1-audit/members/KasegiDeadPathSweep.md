# KasegiDeadPathSweep

Advisory measurement only. Not a native judge verdict, lane round report, receipt, or admission. No lane file was edited. No gate, build, lint, test, or formatter was run. No commit.

Axes walked: freshness (landed tree, not the lane's own census), operability (would a follower open the path), calibration (live vs labelled vs dated log), adjacency (deleted-path classes that are not this lane's, and case-wrong pointers to files that do exist).

Lane tree swept: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` at `git rev-parse HEAD` = `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` (exit 0). That is the assigned round-20 identity commit. Porcelain was not audited (identity seat).

## Classification rule (applied here, not taken from the lane)

- **live** — the sentence is a current how-to or a present-tense liveness claim, and neither the sentence nor an immediately following withdrawal marks the path lost. A follower who obeys it looks up a deleted path.
- **labelled** — the same sentence, or the census/instrument row, carries an explicit loss marker: `[lost-base]`, `[lost-tree]`, `ABSENT`, `GONE`, `BASE-ABSENT`, or the instrument comment that the candidate exists only so absence is named.
- **marked-historical** — dated log or lesson, past-tense quote ("lived at", "recorded as", "at census time"), or a body the file-head errata already declares historical. Not a current how-to.
- **unresolved** — unmarked token whose file elsewhere withdraws the class, or a generator example that names the deleted path beside a RESOLVES count. Not silent, not cleanly live.

A dated LOG/lesson line that said "lives under" on 2026-09-28 is marked-historical, not live. The same wording in an undated knowledge how-to is live.

## Commands

| command | exit | observation |
|---|---:|---|
| `[ -e /home/vgpnk/projects ]` and `[ -e /home/vgpnk/projects/shokunin ]` | n/a (test false) | ABSENT |
| `[ -d /home/vgpnk/Projects/origin-work ]` and `…/open-bug-bounties`, `…/the-bounty-hunter`, `…/ufo-fsd-alpha` | n/a | NODIR |
| `[ -d /home/vgpnk/Projects/open-bug-bounties ]`, `…/the-bounty-hunter`, `…/bounties` | n/a | NODIR (adjacency; not the assigned class list, except origin-work) |
| `[ -d /home/vgpnk/Projects/ufo-fsd-alpha ]` | n/a | DIR (relocated tree; not a deleted-path hit) |
| `[ -e ]` on `/home/vgpnk/Projects/webzites`, `…/ds4cc-marketplace`, `…/plazir-15-site`, `/home/vgpnk/.bailian`, `/home/vgpnk/archive/bench-arena`, `/home/vgpnk/.config/the-janitor`, `/home/vgpnk/.local/bin/the-janitor`, `/home/vgpnk/.local/state/the-janitor`, `/home/vgpnk/.config/opencode/agents/janitor.md` | n/a | all ABSENT |
| `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin rev-parse --is-inside-work-tree` | **128** | `fatal: cannot change to '/home/vgpnk/projects/shokunin/kasegi-shokunin': No such file or directory` |
| in-process walk of every file under the lane (skip `.git`) for the eight classes | n/a | 163 hits in 2 classes; 0 hits in the other 6. 137 files walked. |

Capital-P counterparts of the lowercase lesson pointers exist: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-{1,3,4,5,6,7,8,9}/kasegi.md` and `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log`. The lowercase forms do not.

`citation-survival.tsv` RESOLVES rows (not deleted paths): `/`, `/home`, `/home/vgpnk`, `/tmp`, `~`, `~/Projects`, `~/Projects/**`, `~/Projects/ufo-fsd-alpha`, `~/Projects/ufo-fsd-alpha/scripts/ufo-sighting.mjs`. Zero deleted-path tokens classify RESOLVES.

## Totals

| class | hits | live | labelled | marked-historical | unresolved |
|---|---:|---:|---:|---:|---:|
| `~/Projects/origin-work` (substring `origin-work`) | 137 | 20 | 65 | 40 | 12 |
| lowercase `~/projects` or `/home/vgpnk/projects` | 26 | 2 | 11 | 10 | 3 |
| `webzites` | 0 | 0 | 0 | 0 | 0 |
| `ds4cc-marketplace` | 0 | 0 | 0 | 0 | 0 |
| `plazir-15-site` | 0 | 0 | 0 | 0 | 0 |
| `~/.bailian` / `bailian` | 0 | 0 | 0 | 0 | 0 |
| `~/archive/bench-arena` / `bench-arena` | 0 | 0 | 0 | 0 | 0 |
| the-janitor host paths (`janitor`, case-insensitive) | 0 | 0 | 0 | 0 | 0 |
| **total** | **163** | **22** | **76** | **50** | **15** |

Criterion 2 ("zero LIVE citations to deleted paths, or each named with its owner/unblock") is **not met**. Twenty-two live hits. The lane named two debt classes that cover some of them and missed the line-level rest.

## Claim-by-claim vs the lane record

1. **Round-20 lesson: instruments derive roots; both domain roots still lost.** Agree. `corpus/instruments/anchorcheck.py:67-98` and `corpus/instruments/resolve.py:81-96` derive `$KASEGI_MIRROR` / `$KASEGI_ORIGIN_ROOT`, else first existing candidate, else the canonical absent path. Those candidate strings are labelled, not live binds: `ORIGIN_ABSENT` is the absence branch. Measured NODIR on every candidate except `~/Projects/ufo-fsd-alpha`, which this lane's deriver does not select.

2. **SCORECARD round-19: live ufo-fsd citations re-anchored; `UFO_ROOT=` kept as a quote.** Agree for the sites this sweep opened: `corpus/knowledge/ufo-archive-2026.md:31`, `corpus/knowledge/ufo-workspaces.md:98`, `:169`, `:311`. Disagree if that sentence is read as "every origin-work liveness claim was re-anchored." The open-bug-bounties how-tos below are still present tense and unmarked.

3. **SCORECARD: 202 SKILL + 39 corpus anchors marked `[lost-base]`.** Not re-counted. Agree that many `path:line` anchors carry the prefix (example `SKILL.md:695`). Disagree that the count means the prose class is closed. Unmarked present-tense paths remain; they are the live set.

4. **`RECEIPT-STORE-LOST` (SCORECARD.md:151-155): receipts are corpus-attested only; unblock = operator restores `open-bug-bounties` or declares the claims permanently attested.** Agree the store loss is named, with an operator unblock. Disagree that this names the live sentences. The debt row has no file:line. `submitted-registry.md` still says the tree "is a LIVE, separate claim corpus" with no in-file errata.

5. **`BLOB-PIN-LOWERCASE-PATH` (round-20 lesson; repair note E3 cites `citation-bases.md:72-73`; owner there = parent integrator).** Agree `citation-bases.md:72` is a live command and the lowercase path is absent (git exit 128). Disagree that the class is fully named: `corpus/knowledge/triage-thresholds.md:12` is a second runnable `git -C ~/projects/shokunin/kasegi-shokunin show` and is not in that errata. The lesson names the debt and does not state owner/unblock.

6. **`ORIGIN-REPO-LOST`: `origin-work/ufo-fsd-alpha` quotes stay quotes; unblock none for lane gates.** Agree for the quote sites (LOG.md:541-542, claim-anatomy-sample.md:96, ufo-workspaces.md:98). Disagree that this covers `open-bug-bounties` how-tos. Those are a different path under the same deleted root, and they are not quotes.

7. **Generated census parenthetical "domain other: origin-work, /tmp, ~/projects" next to RESOLVES=9 (`citation-survival.md:24`, printed by `resolve.py:339-340`).** Disagree with reading this as a claim that those paths resolve. The nine RESOLVES rows are the absolute roots and `~/Projects/ufo-fsd-alpha` listed above. The parenthetical is a stale example in the generator. Class unresolved, not a false RESOLVES.

8. **Round-20 lesson does not claim zero live citations.** Agree. The failure is against the audit criterion, not against a sentence the lane wrote.

## Live hits (22) — counterexamples

Follower-openable or present-tense liveness. None carries `[lost-base]` / ABSENT on the sentence.

### lowercase `~/projects` (2)

- `corpus/knowledge/citation-bases.md:72` — "commands resolve a pin with the shell command git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show". Measured exit 128.
- `corpus/knowledge/triage-thresholds.md:12` — "Resolve with `git -C ~/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md`". Same absent directory. Not named in the E3 errata.

### `~/Projects/origin-work` (20)

`corpus/knowledge/submitted-registry.md` — no loss marker anywhere on these lines; file has no origin-work errata:

- `:9` "the live sibling tree `~/Projects/origin-work/open-bug-bounties/`"
- `:10` continuation, `claim-packages/` as "the true home"
- `:24` "`~/Projects/origin-work/open-bug-bounties/claim-packages/` is a"
- `:26` path inside the LIVE-corpus sentence
- `:27` "`…/submission-receipts.csv` (verified live)"
- `:42` "no bounties-repo tool reads `~/Projects/origin-work/` at all" — present tense, corpus asserted outside every scan
- `:63` `…/receipts/CONTRADICTION.md` "is the additive warning file"
- `:66` `…/queue.json` `submitted:false` as a current admin record
- `:67` `…/run.json` `external_submissions:0` as a current admin record
- `:123` "the entire `~/Projects/origin-work/open-bug-bounties/claim-packages/` corpus … is outside every bounties-repo scan"
- `:125` `…/queue.json` in that same present-tense gap
- `:127` "A re-staged finding from the origin-work tree collides with nothing the checker reads"

`corpus/knowledge/intake-and-finalize.md` — current procedure, header dated 2026-09-28, no later withdrawal:

- `:14` "Feeds `~/Projects/origin-work/open-bug-bounties/data/` into `bounty-map/programs/`"
- `:18` binding inputs `…/independent_programs.json` and `…/platform_programs.json`
- `:19` `…/web3_programs.json` "expose `.records[]`"
- `:22` `…/refresh_evidence.json` "needs `run_id` + `evidence_id`"

`corpus/knowledge/ops-invariants.md`:

- `:99` "board defaults to `/home/vgpnk/Projects/origin-work/open-bug-bounties`"
- `:100` "Requires `~/Projects/origin-work/open-bug-bounties/data/refresh_evidence.json`"

`corpus/knowledge/operator-queue.md:90` — "`~/Projects/origin-work/open-bug-bounties/claim-packages/` receipt tree — row 4 is a verified duplicate that returns `claim-check: OK`". Present-tense blind spot. Not in the HistoryClaims H8 origin-work list (that note named the file's bounties Source lines, not this path).

`SCORECARD.md:174` — Planned section, after the round-19 ABSENT annotation, still says "whose surviving origin-work package materially differs." Present-tense survival after the file has recorded the tree gone.

## Unresolved (15)

File or later section withdraws the class, or the token is an example, but the line itself is unmarked. Not counted as live. Still not clean.

- `SCORECARD.md:16` — lead "read this first" still says two roots "survive", including `~/Projects/origin-work/open-bug-bounties`. Withdrawn only at `:124-125`.
- `SKILL.md:206` — dead watcher "scans the origin-work claim-packages tree". Header `:25-30` says the root is gone; this sentence is not marked.
- `SKILL.md:273` — "claim-ready tracker over the separate `origin-work/open-bug-bounties` tree". Same header coverage, sentence unmarked.
- `corpus/README.md:24` — index row still calls `submitted-registry.md` a "live census" and names `origin-work/…/submission-review/` as the real receipt store. `:51-58` later says every such path is historical.
- `corpus/README.md:87` — closed-gap blurb "3 archive-era live in origin-work tree".
- `corpus/README.md:88` — "origin-work corpus outside every scan" in that same blurb.
- `corpus/README.md:159` — round-14 note "4028846/a169f309 live in origin-work `submission-review/`".
- `corpus/instruments/README.md:14` — current format rule: ORIGIN-WORK citations "must use" `~/Projects/origin-work/open-bug-bounties/`. Does not claim the directory exists. A writer following it emits new cites into the deleted prefix.
- `corpus/instruments/citation-survival.md:24` — "Of the 9 RESOLVES, 9 are non-lane roots (domain `other`: origin-work, /tmp, ~/projects …)". Example list, not the RESOLVES set. See claim 7.
- `corpus/instruments/resolve.py:339` — the generator line that prints that parenthetical (the `origin-work` token).
- `corpus/instruments/resolve.py:340` — the `~/projects` token in the same template.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:50` — evidence cell `~/projects/shokunin/.ufo/watchdog.log`. File-head errata covers mirror and origin-work, not this class. Capital-P `watchdog.log` exists; this locator does not.
- `corpus/knowledge/intake-surface.md:106` — watcher target `~/Projects/origin-work/open-bug-bounties/claim-packages/`. `:114` says the tracker is dead; the path is not marked absent.
- `corpus/knowledge/mission-control.md:162` — tracker "tracking `origin-work/open-bug-bounties/claim-packages/`". No loss marker.

## Labelled (76)

Loss marker on the sentence, or GONE/BASE-ABSENT machinery. Not live.

### origin-work (65)

- `LOG.md:792` — round-19 entry: the whole `~/Projects/origin-work` tree "are ABSENT".
- `PROVINCE.md:18` — "the whole `~/Projects/origin-work` tree disappeared".
- `SCORECARD.md:125` — surviving roots "are ABSENT".
- `SCORECARD.md:161` — `ORIGIN-REPO-LOST` debt: quotes stay quotes.
- `SKILL.md:21` — root named, same paragraph "**also ABSENT since 2026-10-12**".
- `SKILL.md:27` — "no relocated copy"; citations "now marked `[lost-base]`".
- `SKILL.md:396` — "then-surviving root" `/home/vgpnk/Projects/origin-work/open-bug-bounties`; "root ABSENT since 2026-10-12"; anchor is `[lost-base]`.
- `SKILL.md:695` — receipt anchors prefixed `[lost-base] ~/Projects/origin-work/open-bug-bounties/…`.
- `SKILL.md:729` — "they lived in" the sibling tree; continuing sentence "that tree is ABSENT since 2026-10-12".
- `corpus/README.md:34` — index title "mirror + origin-work absent".
- `corpus/README.md:49` — path named; sentence completes "both now ABSENT".
- `corpus/README.md:51` — "`~/Projects/origin-work` are also GONE".
- `corpus/README.md:54` — every `origin-work` path "is now a historical record".
- `corpus/instruments/anchorcheck.py:27` — accepted prefix; absent base is BASE-ABSENT (`:30`).
- `corpus/instruments/anchorcheck.py:29` — candidate `~/Projects/origin-work/open-bug-bounties`.
- `corpus/instruments/anchorcheck.py:39` — candidate `~/Projects/origin-work/the-bounty-hunter`.
- `corpus/instruments/anchorcheck.py:69` — comment: this event removed the whole tree.
- `corpus/instruments/anchorcheck.py:77` — `_MIRROR_CANDIDATES` entry.
- `corpus/instruments/anchorcheck.py:80` — `_ORIGIN_CANDIDATES` entry.
- `corpus/instruments/anchorcheck.py:96` — `ORIGIN_CITE_PREFIX`.
- `corpus/instruments/anchorcheck.py:104` — `CITE` regex includes the prefix; `[lost-base]` strips before check (`:103`).
- `corpus/instruments/resolve.py:86` — mirror candidate; `:81-84` says absent cites classify GONE.
- `corpus/knowledge/citation-bases.md:35` — "live repo while it stood"; next line ABSENT.
- `corpus/knowledge/citation-bases.md:36` — "the entire `origin-work` tree is ABSENT since 2026-10-12".
- `corpus/knowledge/citation-bases.md:39` — example path; same paragraph "now GONE; use `[lost-base]`".
- `corpus/knowledge/root-loss-2026-10-12.md:14` — table cell **ABSENT**.
- `corpus/knowledge/root-loss-2026-10-12.md:38` — detection loop listing `~/Projects/origin-work` and `…/ufo-fsd-alpha`; documented result only `~/Projects/ufo-fsd-alpha` PRESENT.
- `corpus/knowledge/root-loss-2026-10-12.md:39` — `~/Projects/origin-work/open-bug-bounties` in that loop.
- `corpus/knowledge/root-loss-2026-10-12.md:45` — `ls ~/Projects` "no origin-work".
- `corpus/knowledge/root-loss-2026-10-12.md:50` — anchors "are now `[lost-base]`".
- `corpus/knowledge/source-tree-loss-2026-09-28.md:11` — round-19 errata: origin-work "ABSENT since ~2026-10-12".
- `corpus/instruments/citation-survival.tsv` GONE rows (34): `:59`, `:87`, `:88`, `:131`, `:143`, `:161`, `:249`, `:279`, `:280`, `:281`, `:282`, `:283`, `:424`, `:589`, `:590`, `:591`, `:592`, `:593`, `:1147`, `:1148`, `:1149`, `:1150`, `:1151`, `:1152`, `:1153`, `:1314`, `:1315`, `:1316`, `:1317`, `:1318`, `:1319`, `:1320`, `:1321`, `:1322`. Outcome column is GONE. `:589-593` also carry `[lost-base]` inside the token.

### lowercase `~/projects` (11)

`corpus/instruments/citation-survival.tsv` GONE rows: `:358`, `:359`, `:360`, `:361`, `:362`, `:363`, `:364`, `:365`, `:1334`, `:1335`, `:1336`.

## Marked-historical (50)

Dated record or past-tense quote. Not a current how-to. Opening them still fails; that is operability of the archive, not a live citation.

### origin-work (40)

- `LOG.md:71` — 2026-09-28 round 5, "tracker over the origin-work tree".
- `LOG.md:180` — 2026-09-28 round 9, "receipt tree lives under `~/Projects/origin-work/open-bug-bounties/`". Then-true. Withdrawn by `:792`.
- `LOG.md:231` — round narrative, "also scans origin-work claim-packages".
- `LOG.md:442` — round narrative, "store is origin-work `submission-review/`".
- `LOG.md:541` — disappearance-window quote `origin-work/ufo-fsd-alpha`.
- `LOG.md:542` — `origin-work/tmp`, `origin-work/open-bug-bounties/.git`.
- `LOG.md:581` — round-15 inventory of `~/Projects/origin-work/open-bug-bounties` as a then-surviving root.
- `LOG.md:718` — "absent from lane, mirror, origin-work".
- `LOG.md:723` — "origin-work reconciliation are different artifacts".
- `PROVINCE.md:12` — round-15 "surfaces now resolve" paragraph. Immediately withdrawn by `:16-22`.
- `SCORECARD.md:67` — round-15 coverage cell, inventory-only measurement.
- `SCORECARD.md:103` — round-18 cell, "Four exact origin-work receipt anchors now open" (then).
- `SCORECARD.md:108` — round-18 narrative "origin-work; review also resolved".
- `SKILL.md:976` — cited-paths preamble: round-19 clause says the origin-work exception is historical and "there are no live exceptions left".
- `SKILL.md:996` — cited-paths bullet under that preamble ("for the origin-work claim tree").
- `SKILL.md:1003` — cited-paths bullet "over claims/ AND origin-work claim-packages", same preamble.
- `corpus/instruments/resolve.py:30` — docstring example of the other-root rule (`exists? RESOLVES : GONE`).
- `corpus/knowledge/claim-anatomy-sample.md:96` — quoted lost-tree field value `origin-work/ufo-fsd-alpha/.ufo/missions/…`.
- `corpus/knowledge/root-loss-2026-10-12.md:15` — "lived at `origin-work/ufo-fsd-alpha`".
- `corpus/knowledge/root-loss-2026-10-12.md:18` — "clean of the old origin-work path".
- `corpus/knowledge/root-loss-2026-10-12.md:31` — whether the trees "vanished in the same maintenance".
- `corpus/knowledge/source-tree-loss-2026-09-28.md:53` — concurrent-activity cell; file-head errata says this body is the historical record.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:129` — section title for the then-inventory.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:132` — inventory path.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:133` — inventory paths.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:135` — `submission-review/` inventory.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:136` — `data/` inventory.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:137` — dataset byte sizes.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:138` — dataset byte sizes continued.
- `corpus/knowledge/source-tree-loss-2026-09-28.md:149` — anchor-base rule "(c) origin-work", under the same errata.
- `corpus/knowledge/ufo-archive-2026.md:31` — "recorded as `origin-work/ufo-fsd-alpha` at census time; the tree relocated".
- `corpus/knowledge/ufo-workspaces.md:98` — `UFO_ROOT=~/Projects/origin-work/ufo-fsd-alpha` "as recorded in the lost launch script".
- `corpus/knowledge/ufo-workspaces.md:169` — old location, re-verified against `~/Projects/ufo-fsd-alpha`.
- `corpus/knowledge/ufo-workspaces.md:311` — "relocated from `origin-work/`".
- `corpus/lessons/round-5.md:19` — 2026-09-28 lesson, tracker for the separate tree.
- `corpus/lessons/round-9.md:17` — lesson "lives in the live sibling tree". Dated round record, not a how-to. The knowledge file it points at (`submitted-registry.md`) is the live counterexample, not this lesson line.
- `corpus/lessons/round-9.md:27` — "origin-work, and archive receipts are all outside".
- `corpus/lessons/round-9.md:57` — "origin-work blind spot reported upstream".
- `corpus/lessons/round-9.md:59` — "archive-receipt index + origin-work corpus".
- `corpus/lessons/round-9.md:62` — "origin-work discovery".

### lowercase `~/projects` (10)

Lesson evidence locators and one friction note. Capital-P report files exist; these spellings do not. Append-only lessons; not current commands.

- `corpus/lessons/round-1-aggregator-audit.md:13`
- `corpus/lessons/round-1.md:4`
- `corpus/lessons/round-1.md:25` — names the prompt's `~/projects` convention as the thing that was wrong.
- `corpus/lessons/round-3.md:4`
- `corpus/lessons/round-4.md:4`
- `corpus/lessons/round-5.md:4`
- `corpus/lessons/round-6.md:4`
- `corpus/lessons/round-7.md:4`
- `corpus/lessons/round-8.md:4`
- `corpus/lessons/round-9.md:4`

## Zero-hit classes

Searched the lane tree, case-insensitive, for `webzites`, `ds4cc-marketplace`, `plazir-15-site`, `plazir15`, `bailian`, `bench-arena`, `bench_arena`, `janitor`. No matches. Those deleted paths are not cited here, live or otherwise. the-janitor host paths (`~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.local/state/the-janitor`, `agents/janitor.md`) are absent on disk and uncited in this lane.

## Named debt (this sweep; not repaired)

| id | live or unresolved lines | owner | unblock |
|---|---|---|---|
| `BLOB-PIN-LOWERCASE-PATH` | live `citation-bases.md:72`, live `triage-thresholds.md:12` (second site unnamed by the lane) | kasegi record; parent appends. Objects `fc6d398` still resolve under `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (not re-shown here). | Point both shell commands at the capital-P checkout. Do not backtick a bare blob path. Do not treat the lesson report spellings as the same defect. |
| `RECEIPT-STORE-LIVE-PROSE` | live `submitted-registry.md:9,10,24,26,27,42,63,66,67,123,125,127` | kasegi record for the wording; operator for the bytes | In-file errata that the tree is ABSENT since 2026-10-12. Scorecard `RECEIPT-STORE-LOST` already names the store and the operator unblock (restore `open-bug-bounties`, or declare the claims permanently attested). It does not name these lines. |
| `INTAKE-HOWTO-ORIGIN` | live `intake-and-finalize.md:14,18,19,22` | kasegi record | Append errata: those feeds are `[lost-base]`. Do not run `import-board` against that root. Not in round-20 named debt. |
| `FRESHNESS-DEFAULT-ORIGIN` | live `ops-invariants.md:99-100` | kasegi record | Same. The SKILL retelling at `:396` is already labelled; this how-to is not. |
| `QUEUE-BLINDSPOT-ORIGIN` | live `operator-queue.md:90` | kasegi record | Mark the receipt-tree path `[lost-base]`. The claim-check gap is also a lost-tree fact; do not describe the scan as a current miss against a present tree. |
| `SCORECARD-SURVIVING-PACKAGE` | live `SCORECARD.md:174` | kasegi record | The Planned sentence post-dates the ABSENT annotation and still says the package is surviving. Mark it historical or delete the survival claim. Do not look for the package. |
| `RESOLVES-EXAMPLE-STALE` | unresolved `citation-survival.md:24`, `resolve.py:339-340` | kasegi instruments | The example list is not the RESOLVES set. Regenerating the census without editing the template reprints the misread. Not a false GONE/RESOLVES row. |
| `LEAD-SURVIVE` | unresolved `SCORECARD.md:16`, `corpus/README.md:24,87,88,159`, `SKILL.md:206,273`, `intake-surface.md:106`, `mission-control.md:162`, `instruments/README.md:14`, `source-tree-loss-2026-09-28.md:50` | kasegi record | File banners exist for some of these and not for the sentence. Append a one-line withdrawal on the sentence, or stop prescribing the deleted prefix as the citation form. Lowercase watchdog cell: the file is at `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log`. |

Standing lane debts this sweep does not close and does not contradict: `RECEIPT-STORE-LOST`, `MIRROR-SOURCE-LOST`, `ORIGIN-REPO-LOST` (quote half only). Unblock for the store remains the operator. Unblock for the live wording is a kasegi record append, which this seat did not make.

## Adjacency (not absorbed)

- `~/Projects/bounties` and `~/Projects/the-bounty-hunter` are also NODIR. They are outside this sweep's class list. Lines were classified only when they also contained `origin-work` or lowercase `projects`.
- `~/Projects/open-bug-bounties` is an `anchorcheck.py` fallback candidate and is NODIR. It is not a separate live citation; it is part of the labelled absence walk.
- Lesson lowercase report paths are case-wrong pointers to files that exist under `/home/vgpnk/Projects/shokunin/.ufo/reports/`. Left marked-historical. Do not rewrite the lessons.

## What this seat did not do

Did not run `anchorcheck.py`, `density.py`, or `resolve.py` (gate seat). Did not re-count the 202/39 `[lost-base]` prefix claim. Did not read session or credential files. Did not edit the lane. Did not treat repair-wave prose as evidence; presence, git exit 128, and the line text were re-measured.
