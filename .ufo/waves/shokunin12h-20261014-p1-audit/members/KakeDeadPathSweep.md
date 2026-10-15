# KakeDeadPathSweep

Advisory sweep only. Not a judge verdict, lane round report, receipt, or admission. No lane file was edited. No gate, build, lint, or formatter was run. No fetch. No secret or session content was read.

## Binding

- Tree swept: `/home/vgpnk/Projects/shokunin/kake-shokunin` (50 files, `.git` excluded, untracked `plans/` included).
- Worktree HEAD: `de5d7627696fd2ecb3e955997bc8bee83aea3220` (`round-19: append independent-audit erratum`).
- Named identity commit `59948314e9af5dd6ef81894fc1c422b353f10938` is an ancestor. Net diff vs that commit is two pointer rewrites plus an appended erratum in `corpus/lessons/round-19-recensus.md`. None of the live lines below sit in that diff. Line numbers of every live cite are the same at the identity commit.
- Porcelain: `?? plans/` only. `plans/wwkd-round-19-recensus.md` has zero hits.
- Token walk: 399 lines at HEAD (398 at the identity commit; the extra line is `corpus/lessons/round-19-recensus.md:44`, which says "stale webzites binaries" and is labelled, not live).

## Host absence (measured this pass)

`test -e` exit 1 (absent):

- `/home/vgpnk/projects`
- `/home/vgpnk/Projects/origin-work`
- `/home/vgpnk/Projects/webzites`
- `/home/vgpnk/Projects/ds4cc-marketplace`
- `/home/vgpnk/Projects/plazir-15-site`
- `/home/vgpnk/.bailian`
- `/home/vgpnk/archive/bench-arena`
- `/home/vgpnk/.config/the-janitor`
- `/home/vgpnk/.local/bin/the-janitor`
- `/home/vgpnk/.local/state/the-janitor`
- `/home/vgpnk/.config/opencode/agents/janitor.md`
- `/home/vgpnk/.config/systemd/user/webzites-probe.timer`
- `/home/vgpnk/.config/systemd/user/webzites-keeper.service`

`test -e` exit 0 (present, not a substitute for the deleted paths):

- `/home/vgpnk/Projects/ufo-fsd-alpha`
- `/home/vgpnk/Projects/burnerchrome` (top names only: `README.md`, `index.html`, `marketplace.html`, `adapters/`, `assets/`. Not content-compared to `~/Projects/ds4cc-marketplace/burnerchrome`.)

`command -v webzites` exit 1. `command -v the-janitor` exit 1.

`~/Projects` children listed this pass do not include `webzites`, `ds4cc-marketplace`, `plazir-15-site`, or `origin-work`.

## Rules (this sweep, not the lane's)

A hit is a line containing one of: lowercase `~/projects` or `/home/vgpnk/projects`; `origin-work`; `webzites`; `ds4cc-marketplace`; `plazir-15-site`; `bailian`; `bench-arena`; `the-janitor` / `janitor.md`. Case-variant-only matches: 0.

- **live** — standing runbook or present-tense sentence a reader would execute or treat as current, with no absence marker on that line and no dated section heading governing it.
- **marked-historical** — same line carries `r18 re-census` plus absent/gone/historical-record, naming that cite.
- **labelled** — not current-voice. Subtags below (declared-absent pin, fixture, suspend/watch, governed by a marked header/`cd`/closing line, round-record, dated section or role noun, absence word on the line).
- **unresolved** — none. Judgment gaps that are not hits are listed at the end.

A nearby `r18` comment that names a different path does not mark this line. The gate's ±2 `absent|gone|…` window is looser than this rule; that looseness is a finding, not the classifier.

## Counts

| family | token lines | in-lane |
|---|---|---|
| webzites | 282 | yes |
| ds4cc-marketplace | 48 | yes |
| plazir-15-site | 43 | yes |
| origin-work | 23 | yes |
| lowercase `~/projects` | 18 | yes |
| `~/.bailian` | 0 | no token |
| `~/archive/bench-arena` | 0 | no token |
| the-janitor host paths | 0 | no token |

| class | lines |
|---|---|
| live | 77 |
| marked-historical | 65 |
| labelled | 257 |
| unresolved | 0 |
| total | 399 |

Labelled split: round-record 94, dated-or-role 71, declared-absent pin 44, governed 13, absence-stated 9, fixture 7, watch 6, non-path 10, suspend 2, watch-pin 1.

## Verdict against the lane record

**Disagree** with `corpus/lessons/round-19-recensus.md:37-38` (same sentence at the identity commit): "Stale live prose recorded, not rewritten in place: `SKILL.md:59`/`:111` still name deleted webzites binaries." Those two lines are live. They are not the set. Counterexamples are the 77 live lines below, including unmarked source-dir rows, bare `webzites` commands, `origin-work` present-tense paths, and `scripts/probe-delta.mjs:33`.

**Disagree** with `SCORECARD.md:22-23`: "The corpus' `origin-work/*` cites are all marked absent-historical." Counterexamples:

- `corpus/knowledge/keeper-timer-inert.md:91` — present tense `ExecStart=…/origin-work/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`. The `r18` comment on `:93` names `~/Projects/origin-work/charter-ufo-fsd`, a different path.
- `corpus/knowledge/publish-queue.md:167` — standing rule: any local `git pull`/`fetch` in `origin-work/*` needs explicit sanction. No absence marker.
- `corpus/knowledge/publish-queue.md:233` — `~/Projects/origin-work/open-bug-bounties/` with no `r18` marker (dated r15/r16 frame, so labelled here, still not marked-historical).
- `corpus/knowledge/freshness-pins.json:74-76` — declared-absent pin rows, not prose historical-record markers.

**Agree** that the deleted roots are gone, that PQ-2 / PQ-14 / §history are already named with an unblock (`SCORECARD.md:13-19`), and that re-pinning those watches green would hide a real absence. **Agree** that lowercase `~/projects` is described as removed (`SKILL.md:300-301`, `SCORECARD.md:31`). **Agree** this lane has zero `~/.bailian`, `~/archive/bench-arena`, and the-janitor host-path tokens.

**Agree** that many concrete `~/…` cites carry an inline `r18 re-census` marker (65 token lines at HEAD). That does not make the unmarked operational lines historical.

The appended erratum at `round-19-recensus.md:42-48` repeats the three-site stale-prose list and then discusses describe-don't-pin counts and hashes. It does not enumerate the live command/source-dir set. This sweep does not re-litigate the hash sentence; it does not depend on it.

## Live citations (77)

Each line is a current-voice cite of a path or host tool that `test -e` / `command -v` shows absent. Owner for all of these is **kake** (prose or the script default). Unblock: put an absence marker on the citing line, or stop instructing the command. Do not delete the historical measurement. Do not re-pin `pathsMissSet` to hide them — the citation gate does not see bare `webzites` commands (see calibration).

### SKILL.md — checklist, verb table, unmarked source dirs (26)

- `:59-62`, `:65`, `:71`, `:73`, `:103`, `:111`, `:115` — step 1 still says `node ~/Projects/webzites/bin/webzites.mjs probe --all`, abbreviates later commands to `webzites`, and says `webzites-probe.timer` runs and `webzites-keeper.timer` is loaded. `:111` is `node ~/Projects/webzites/scripts/kimi-surface.mjs sync-check`.
- `:159` — `webzites lease acquire`.
- `:211`, `:213-214`, `:216-217` — drift table commands (`webzites probe`, `webzites grokbot reconcile`, `node ~/Projects/webzites/scripts/kimi-surface.mjs kimi-map`, `webzites grokbot tick`, `webzites status --json`).
- `:225` — vintage evidence path `webzites/reports/keepers/grokbot-<site>.log.md`.
- `:17` — surface table source `~/Projects/plazir-15-site` with no marker (the ds4cc row above it is marked; this row is not).
- `:20` — `~/Projects/ds4cc-marketplace/burnerchrome` with no marker.
- `:24` — `~/Projects/plazir-15-site` as the recreate source, no marker.
- `:28` — `ds4cc-marketplace/apps-sdk` + `render.yaml` as the current Render source.
- `:54`, `:294-295` — present tense: `plazir-15-site/speedrun/` is a frozen copy; canonical lives in `ds4cc-marketplace/speedrun/`.
- `:154` — operator step: copy bodies into `ds4cc-marketplace/speedrun/data/`.
- `:358` — cited-paths bullet `~/Projects/plazir-15-site/` with no marker. The next bullet (`:360`) marks `origin-work`, not this path.

### Other standing runbooks (50)

- `corpus/README.md:58` — `webzites-probe.timer` nominally provides 6h coverage.
- `corpus/README.md:73` — invoke `node ~/Projects/webzites/bin/webzites.mjs`.
- `corpus/knowledge/fleet-registry.md:47` — source `~/Projects/ds4cc-marketplace/burnerchrome`, status cell "live", no marker (adjacent rows are marked).
- `corpus/knowledge/fleet-registry.md:53-54` — source `~/Projects/plazir-15-site`, no marker.
- `corpus/knowledge/fleet-registry.md:62` — source `~/Projects/ds4cc-marketplace/burnerchrome`, no marker.
- `corpus/knowledge/free-read-verbs.md:12-13` — "Invocation is always the absolute node path"; names `bin/webzites.mjs`.
- `corpus/knowledge/free-read-verbs.md:112`, `:161`, `:404` — current exit-contract pins into `bin/webzites.mjs`.
- `corpus/knowledge/free-read-verbs.md:455` — the 6h `webzites-probe.timer` sweep self-heals the snapshot.
- `corpus/knowledge/freshness-sweep.md:87` — present tense: `~/Projects/plazir-15-site` is 5 commits ahead of `origin/main`.
- `corpus/knowledge/ghp-subpath-spotcheck.md:11-12` — current verb table `webzites probe` / `webzites grokbot reconcile`.
- `corpus/knowledge/keeper-timer-inert.md:1` — title: `webzites-keeper.timer` loaded, disabled, never fired. The unit file is absent, not loaded-disabled.
- `corpus/knowledge/keeper-timer-inert.md:78` — `webzites-probe.timer` covers the probe leg (present tense).
- `corpus/knowledge/keeper-timer-inert.md:91` — live origin-work ExecStart path (see disagree).
- `corpus/knowledge/keeper-timer-inert.md:106` — "What still works": `webzites-probe.timer` enabled, active, 6h.
- `corpus/knowledge/keeper-timer-inert.md:139`, `:141-142` — operator recipe `webzites install --timer --enable` and `systemctl --user enable --now webzites-keeper.timer`.
- `corpus/knowledge/kimi-subpath-audit.md:77` — heading "Procedure (re-run recipe)" greps `ds4cc-marketplace/sitemap.xml`.
- `corpus/knowledge/mirror-pitfalls.md:31-32` — present tense `plazir-15-site/speedrun/` and `ds4cc-marketplace/speedrun/`. File has no `r18` marker at all.
- `corpus/knowledge/mirror-pitfalls.md:36` — `webzites lease acquire`.
- `corpus/knowledge/ops-automation.md:13-14` — unit table still the watching fabric (`webzites probe --all --quiet`, `webzites grokbot tick --quiet`). Sources paragraph `:3-4` is marked; this table is not.
- `corpus/knowledge/ops-automation.md:16`, `:19` — `webzites install` and `webzites status`.
- `corpus/knowledge/ops-automation.md:68` — CLI surface heading cites `bin/webzites.mjs --help` as the verbatim source.
- `corpus/knowledge/origin-repos.md:30-31`, `:33`, `:35` — standing name-trap: edit `ds4cc-marketplace` / `plazir-15-site`. `:34` says "Edit the right repo for the right URL."
- `corpus/knowledge/origin-repos.md:64` — `burnerchrome-kimi.sourceDir` → vendored `ds4cc-marketplace/burnerchrome`.
- `corpus/knowledge/probe-delta-alerting.md:77-78` — "Invoke both from any cwd" with `node ~/Projects/webzites/bin/webzites.mjs` and `node ~/Projects/webzites/scripts/kimi-surface.mjs`. (`:18` marks the history file, not these binaries.)
- `corpus/knowledge/publish-channels.md:5`, `:10`, `:22` — present tense workflow paths `ds4cc-marketplace/.github/workflows/pages.yml`, `plazir-15-site/.github/workflows/pages.yml`, `ds4cc-marketplace/render.yaml`.
- `corpus/knowledge/publish-channels.md:30` — "Verified verbs in `~/Projects/webzites/scripts/kimi-surface.mjs`". (`:49` marks a different file.)
- `corpus/knowledge/publish-queue.md:34` — standing PQ-14 recipe: `git rev-list` in `~/Projects/plazir-15-site`.
- `corpus/knowledge/publish-queue.md:41` — unpushed `ds4cc-marketplace` commits advance both surfaces.
- `corpus/knowledge/publish-queue.md:156` — if health suspect, `systemctl --user list-timers webzites-probe.timer`.
- `corpus/knowledge/publish-queue.md:167` — live origin-work fetch rule (see disagree).
- `corpus/knowledge/speedrun-pipeline.md:15`, `:21`, `:23`, `:40` — stage list `webzites speedrun record|report|prep|post`. `:11` marks the keeper root absent; these command lines do not.
- `scripts/probe-delta.mjs:33` — `DEFAULT_HISTORY` is `Projects/webzites/state/probe-history.jsonl`. A bare `node scripts/probe-delta.mjs` reads that path and exits 2 if missing (`probe-delta.mjs:74-80`). No suspend pin. The citation gate does not scan `scripts/`.

## Why the citation gate does not clear these

Read from `scripts/freshness-sweep.mjs`, not re-run.

- `scanCitations` reads `SKILL.md` and `corpus/**/*.md` only (`:342-347`). `scripts/probe-delta.mjs`, `LOG.md`, and `SCORECARD.md` are outside it.
- `PATH_RE` (`:121`) matches `~/` or `/home/vgpnk/` only. Bare `webzites probe`, `webzites-probe.timer`, and `ds4cc-marketplace/speedrun/` are not path cites to that gate.
- A token is `declaredAbsent` if any cite is within ±2 lines of `absent|gone|vanished|emptied|no longer|dangling|no such file|never published|missing` (`:116-118`, `:310-333`), even when that word names a different path. `SKILL.md:358` (`~/Projects/plazir-15-site/`) falls in the window of `:360`'s `absent`.
- `pathsMissSet` membership suppresses `newMissing` for a path already pinned (`:461-469`). An unannotated repeat of `~/Projects/webzites/bin/webzites.mjs` (pin row `freshness-pins.json:82`) does not flip the gate.
- So a red bare run (PQ-2 / PQ-14 ANOMALY, §history SUSPENDED) can coexist with these 77 live lines. That red is not evidence the prose is clean.

## Labelled and marked-historical — every other hit

Subtags are still class **labelled** or **marked-historical**. Ranges are inclusive.

### marked-historical (65)

Same-line `r18 re-census` absent/historical-record comment.

- `SCORECARD.md:43`
- `SKILL.md:16, 18-19, 30, 157, 273, 324, 333, 355, 360`
- `corpus/README.md:70`
- `corpus/handoffs/cmdProbe-merge-fix.md:5, 60`
- `corpus/knowledge/drift-detection.md:4, 7`
- `corpus/knowledge/fleet-registry.md:3, 45-46, 56, 60`
- `corpus/knowledge/free-read-verbs.md:5, 33`
- `corpus/knowledge/freshness-sweep.md:96, 116`
- `corpus/knowledge/ghp-subpath-spotcheck.md:4`
- `corpus/knowledge/keeper-timer-inert.md:11, 14, 21, 48, 93, 114, 159`
- `corpus/knowledge/ops-automation.md:3-4`
- `corpus/knowledge/origin-repos.md:3, 5, 7, 15, 66`
- `corpus/knowledge/probe-delta-alerting.md:18`
- `corpus/knowledge/publish-channels.md:49`
- `corpus/knowledge/publish-queue.md:3, 188, 246`
- `corpus/knowledge/speedrun-pipeline.md:3-4, 9, 11`
- `corpus/lessons/round-1-aggregator-audit.md:4, 29-30, 54`
- `corpus/lessons/round-17.md:45`
- `corpus/lessons/round-18.md:16`
- `corpus/lessons/round-4-aggregator-audit.md:11, 35, 37`
- `corpus/lessons/round-5-aggregator-audit.md:75`
- `corpus/lessons/round-5.md:7`
- `corpus/lessons/round-6-aggregator-audit.md:40, 81, 140`
- `corpus/lessons/round-6.md:5`
- `corpus/lessons/round-9.md:4`

`keeper-timer-inert.md:93` is marked for `~/Projects/origin-work/charter-ufo-fsd` only. The word `webzites` on that line is the start of "no webzites code writes…", not a second marked path.

### labelled/declared-absent (44)

`corpus/knowledge/freshness-pins.json:58-61, 66-69, 74-77, 81-112` — `pathsMissSet` rows. They assert expected absence. That is correct for the absent paths. It is not a prose historical-record marker, and it does not cover the live lines.

### labelled/watch-pin (1)

`corpus/knowledge/freshness-pins.json:38` — `plazirSourceDir` `/home/vgpnk/Projects/plazir-15-site`. `checkPlazir` (`freshness-sweep.mjs:688-702`) turns a missing dir into `ANOMALY` / `plazir-gate-anomaly`. Already named PQ-14. Not an existence claim.

### labelled/suspend (2)

`scripts/freshness-sweep.mjs:110` — canonical history default, suspended when `pins.probeHistoryAbsent` and the path is missing (`:99-102`, `:566-567`). `:999` is the comment that says the source is absent.

### labelled/watch (6)

`scripts/freshness-sweep.mjs:81` — `pq2Dir` `/home/vgpnk/Projects/ds4cc-marketplace`; missing dir becomes `ANOMALY` (`:850`). Already named PQ-2.

`scripts/freshness-sweep.mjs:544, 549-550, 554` — `nextFire` queries `webzites-probe.timer` and is documented informational, never a drift predicate (`:543-546`). No timer line returns `next: null` (`:551`).

`scripts/freshness-sweep.mjs:772` — fleet.config default. `readFileSync` failure is caught (`:782`) and PQ-12 falls back to `pins.charterGhpPin`. `SCORECARD.md:27-28` already says the file is gone.

### labelled/fixture (7)

`scripts/freshness-sweep.mjs:1090, 1110, 1117, 1131, 1133-1134, 1185` — selftest strings `~/Projects/webzites/selftest-*.md`, explicitly fixtures, not host paths.

### labelled/governed (13)

Marker is on the fence header, the `cd` line, or the closing line of the same citation, not on these lines.

- `SKILL.md:334` — child of the marked `~/Projects/webzites/` bullet at `:324` (systemd marker also on `:333`).
- `corpus/handoffs/cmdProbe-merge-fix.md:62, 64-65` — `node bin/webzites.mjs` under `cd ~/Projects/webzites` marked at `:60`. Copy-paste residual; not counted live because the cwd line is marked.
- `corpus/knowledge/drift-detection.md:3` — brace cite closed by the `r18` comment on `:4`.
- `corpus/knowledge/drift-detection.md:10-11, 14` — fence under `:7` "Commands (all under `~/Projects/webzites/`)" marked absent. (`:12` has no `webzites` token.)
- `corpus/knowledge/free-read-verbs.md:6` — continuation of the Sources line marked at `:5`; `:7` dates the read 2026-09-28.
- `corpus/knowledge/ops-automation.md:6` — `bin/webzites.mjs --help` inside the Sources paragraph marked at `:3-4`.
- `corpus/knowledge/origin-repos.md:67` — continuation of the `:66` marked `~/Projects/ds4cc-marketplace` bullet.
- `corpus/knowledge/speedrun-pipeline.md:5, 8` — `:5` continues the marked sources at `:3-4`; `:8`'s path is the one `:9` marks.

### labelled/absence-stated (9)

The line itself says gone/removed/absent/deleted, without the `r18` formula.

- `SCORECARD.md:9, 16, 31, 44` — W6/W7 narrative: lowercase `~/projects` removed; plazir "gone".
- `SCORECARD.md:8` — false friend: the matched word is "corrupt/deleted snapshot", not a webzites absence mark. Still not live (score cell about r11/r12 proofs; "webzites owner" is a role).
- `SKILL.md:301` — "removed `~/projects`".
- `corpus/knowledge/freshness-sweep.md:44` — W6 `~/projects` was caught via a descendant.
- `corpus/knowledge/publish-queue.md:22` — PQ-2 cell; "absent" in that cell is about sitemap paths, not an `r18` marker. Not an instruction to open the deleted repo.
- `scripts/freshness-sweep.mjs:480` — comment: `~/projects` vanished.

### labelled/round-record (94)

Dated LOG bullets and `corpus/lessons/round-*.md` narrative. Past observation, not a current instruction. Not `r18`-marked unless listed above.

- `LOG.md:4-7, 13, 15, 17, 19, 26, 74, 138, 169, 213, 248, 273, 319-320, 338, 358, 403, 411-412, 422`
- `corpus/lessons/round-1-aggregator-audit.md:10, 28, 31-32, 48-49, 53, 67`
- `corpus/lessons/round-1.md:20`
- `corpus/lessons/round-10.md:7, 33, 41`
- `corpus/lessons/round-12.md:19, 27, 45`
- `corpus/lessons/round-17.md:9, 14, 20-21`
- `corpus/lessons/round-18.md:12-14, 33, 54, 56, 59`
- `corpus/lessons/round-19-recensus.md:35, 38, 44` — `:35` says `origin-work` absent; `:38` names the two SKILL lines as deleted binaries; `:44` is the post-identity erratum ("stale webzites binaries").
- `corpus/lessons/round-3.md:4, 9`
- `corpus/lessons/round-4-aggregator-audit.md:31`
- `corpus/lessons/round-4.md:4-5`
- `corpus/lessons/round-5-aggregator-audit.md:14, 17-18, 21-22`
- `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:6, 9, 11, 13, 24-25`
- `corpus/lessons/round-5.md:5, 20, 44, 46-47`
- `corpus/lessons/round-6-aggregator-audit.md:48, 50, 62, 65-68, 129`
- `corpus/lessons/round-8-aggregator-box3-coldrun.md:12, 15-17, 19, 34-35, 37, 55, 100`
- `corpus/lessons/round-9.md:42-43, 45`

`LOG.md:338` cites `origin-work/ufo-fsd-alpha/.ufo/charter-scribe/ledger.jsonl` as a past verified locus. Round-record, not marked-historical. Another hole in the SCORECARD "all marked" sentence.

### labelled/dated-or-role (71)

Dated section, provenance table, role noun ("webzites owner"), schema id, UA string, or remote URL path. Not executed as a current host path under the rule above. A reader who ignores the section date can still misuse them; they are not upgraded to live.

- `SCORECARD.md:14, 22, 28, 63` — `:14` names PQ-2's path as debt (gone is on `:16`); `:22` is the false "all marked" claim; `:28` says the webzites tree is gone; `:63` is a future re-audit trigger.
- `SKILL.md:179, 258, 299, 353` — role noun; URL path `/plazir-15-site/snake` dated 2026-09-28; r16 inode sentence (removal is on `:301`); "no webzites code writes".
- `corpus/README.md:31, 63, 74` — "webzites owner".
- `corpus/handoffs/cmdProbe-merge-fix.md:1, 3, 22` — owner / archaeology role.
- `corpus/knowledge/drift-detection.md:48, 65, 73, 77` — `:48` dated 18:51Z; `:65` under "Fresh probe — 2026-09-28"; `:73` under "r16 re-verification (2026-09-29)"; `:77` is a URL path in that table.
- `corpus/knowledge/fire-journal-codes.md:3-4` — Source paths, "grep'd 2026-09-28". No `r18` marker in this file. Dated source, not a re-run order.
- `corpus/knowledge/fleet-registry.md:4` — schema id `webzites-fleet-v1`.
- `corpus/knowledge/free-read-verbs.md:27, 124, 134, 262, 317-320, 378, 444-445` — schema id; dated 2026-09-28 run; UA `webzites-reconcile/1.0`; role; round-11 provenance table (`:313` heading); quoted stderr; "webzites source owner".
- `corpus/knowledge/freshness-sweep.md:103` — r17 "BEFORE the fix" narrative.
- `corpus/knowledge/ghp-subpath-spotcheck.md:56, 60, 68, 71` — "at baseline time" / "verified 2026-09-28" / "currently serves" under that dated verification.
- `corpus/knowledge/keeper-timer-inert.md:19-20, 24, 26-27, 33-35, 37, 41, 45-47, 124, 127, 135` — verbatim block dated 2026-09-28T22:18Z (`:16` heading); `:41` "same minute"; `:45` "read 2026-09-28"; `:124` and `:127` quote the superseded r5 text (`:129` says historical); `:135` quotes an L0 question.
- `corpus/knowledge/ops-automation.md:98` — under "r13 re-verification (2026-09-28)".
- `corpus/knowledge/origin-repos.md:19, 62` — `:19` is the r5–r8 byte-verified table (`repos/plazir-15-site`, URL "live 200", not re-fetched); `:62` is "webzites keeper".
- `corpus/knowledge/probe-delta-alerting.md:6, 69` — owner role; `:69` is under "Companion CLI facts (operability audit, 2026-09-28)". The imperative invoke lines `:77-78` are live, above.
- `corpus/knowledge/publish-channels.md:11` — URL `veigapunk.github.io/plazir-15-site/`, not a local path.
- `corpus/knowledge/publish-queue.md:5, 32, 224-225, 233, 236, 262` — schema id; "no webzites code"; r15 section including "Domain roots … all alive" (`:225`, false if read as current, dated by `:181`); r16 count of origin-work bounties (`:233`); r16 "are distinct dirs" (`:236`); r16 "NEW — PQ-14" (`:262`, under `:239`).
- `corpus/knowledge/sitemap-orphan-audit.md:22-24, 76, 92` — workflow paths closed by "read 2026-09-28" on `:24`; `:76` under "r16 re-read (2026-09-29)"; role noun.

### labelled/non-path (10)

- `corpus/knowledge/freshness-pins.json:39-40` — `https://veigapunk.github.io/plazir-15-site/` URLs. Not fetched.
- `scripts/freshness-sweep.mjs:60, 676, 839, 950, 953, 1223` — comments and a section label, not a path open.
- `scripts/probe-delta.mjs:4, 8` — why-comment and "webzites owner". The default path is `:33`, which is live.

## Named debt

| id | class | where | owner | unblock |
|---|---|---|---|---|
| KAKE-LIVE-PROSE | live | 76 prose lines listed above (everything live except the script default) | kake | Absence marker on each citing line, or stop the instruction. Do not delete the dated measurement. Do not treat `pathsMissSet` as covering bare commands. |
| KAKE-LIVE-PROBE-DELTA | live | `scripts/probe-delta.mjs:32-34` | kake | Require `--history`, or suspend the canonical default the way `freshness-sweep.mjs:566-567` does. A bare run currently exits 2 on the deleted file. |
| KAKE-SCORECARD-ORIGIN | false claim | `SCORECARD.md:22-23` | kake | Correct the "all marked" sentence. Counterexamples `:91` and `publish-queue.md:167` at minimum. |
| KAKE-PQ2-PQ14-HISTORY | labelled watch, already named | `SCORECARD.md:13-19`; pins `freshness-pins.json:38`, `pq2Dir`, `probeHistoryAbsent` | operator to restore the trees or declare the watches dead; kake must not re-pin them green | Unchanged from the lane record. Agree. |
| KAKE-DATED-SOURCE-UNMARKED | labelled, not live | `fire-journal-codes.md:3-4` (no `r18` anywhere in that file); `free-read-verbs.md:6`; dated sections listed above | kake, historical-marking, not this seat | Append the same absent comment if those Source lines should not be re-opened. This sweep did not upgrade them to live because the sentence or section date binds them. |
| KAKE-BURNERCHROME-CHILD | not retargeted | live rows `SKILL.md:20`, `fleet-registry.md:47`, `:62`, `origin-repos.md:64` name `ds4cc-marketplace/burnerchrome` | kake, only if a content identity is later proven | `~/Projects/burnerchrome` exists. This sweep did not compare it to the deleted child. Do not retarget the cite onto it from directory names alone. |

Zero-hit families need no owner: `~/.bailian`, `~/archive/bench-arena`, `~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.local/state/the-janitor`, `janitor.md`. Absent on the host and absent from this lane.

## Judgment gaps (not unresolved hits)

- Remote URL liveness for `veigapunk.github.io/plazir-15-site/` was not tested. Fetch is forbidden. Those lines are labelled/non-path, not host-path cites.
- Whether `~/Projects/burnerchrome` is the old vendored child is unresolved. It does not make `~/Projects/ds4cc-marketplace/burnerchrome` exist (`test -e` exit 1).
- The dated-vs-live cut is a reading rule, stated above. Moving a dated section into live would enlarge the defect set; it would not shrink it.
- This seat did not re-run `scripts/freshness-sweep.mjs`. Scanner behavior is from the source lines cited. Gate exit codes belong to the gate seat.
