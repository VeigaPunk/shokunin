# KengakuDeadPathSweep

Advisory data. Not a judge verdict, not a lane round report, not a receipt, not an admission. No lane file was edited. No gate was run. No secret or session content was read.

## Identity

- Lane HEAD `7153e671b1581a4b705583656883b6af158257df` (`round-16: OMP-era freshness re-census (measured gates; records + scoped repair)`, 2026-10-14 21:15:36 -0300). `merge-base --is-ancestor` of that hash against HEAD exits 0; they are the same commit.
- Porcelain: `?? plans/` only. `plans/` has no deleted-path hits. Round-16 diff is `LOG.md` +7, `SCORECARD.md` +6, `corpus/lessons/round-16-recensus.md` +30. It did not edit `SKILL.md`, `PROVINCE.md`, `SHONEN.md`, `corpus/README.md`, or any knowledge source line.
- Walk: 187 decoded files under `kengaku-shokunin`, `.git` excluded, no NUL binaries. Inventory is literal text, not LSP (no server was used).

## Existence (this session)

`test -e` / `test -d` equivalent. No file contents read.

| Path | Result |
|---|---|
| `/home/vgpnk/projects` and `/home/vgpnk/projects/shokunin` | ABSENT |
| `/home/vgpnk/Projects/shokunin` | EXISTS (dir). `CORPUS.md` there EXISTS |
| `/home/vgpnk/Projects/origin-work` and `…/ufo-fsd-alpha` | ABSENT |
| `/home/vgpnk/Projects/ufo-fsd-alpha` | EXISTS (dir). Not a deleted path. |
| `/home/vgpnk/Projects/webzites` and `…/repos/llm-wiki` | ABSENT |
| `/home/vgpnk/Projects/ds4cc-marketplace` | ABSENT |
| `/home/vgpnk/Projects/plazir-15-site` | ABSENT |
| `/home/vgpnk/.bailian` | ABSENT |
| `/home/vgpnk/archive` and `/home/vgpnk/archive/bench-arena` | ABSENT |
| `/home/vgpnk/bench-arena` | ABSENT |
| `~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.local/state/the-janitor` | ABSENT |
| `~/.config/opencode/agents/janitor.md` | ABSENT |

Name search, not a full-disk proof: `find /home/vgpnk /scratch /tmp /mnt /opt /srv -maxdepth 4` for `webzites`, `bench-arena`, `bailian`, `origin-work`, `ds4cc-marketplace`, `plazir-15-site`, `the-janitor`, `llm-wiki` printed no hits. Do not invent a replacement path.

`~/bench-arena` is not in the parenthetical list as its own item. It is the pre-relocation name of the listed `~/archive/bench-arena` tree, and it is also absent. Citations to it are in scope. In-repo filenames `bench-arena-*.md` are not host-path citations: 231 `bench-arena` lines have no host path and are excluded. 136 lines do name a host path.

## Rubric

A hit is one deleted-path token on one line. One line can carry two classes.

- **live** — a current contract (`SKILL.md`, `PROVINCE.md`, `SHONEN.md`, `corpus/README.md`, `corpus/knowledge/*` source or reproduction command), the latest census sentence that still says the path resolves, or an executable default that opens the path. No same-line or in-file ABSENT/historical marker retires that token.
- **marked-historical** — dated past-round capture, or the line itself says ABSENT / gone / historical / No such file for that token.
- **labelled** — the line partially retires the token (relocated-from, then-located, frozen, stored-vs-current) but does not say ABSENT, or it is a debt note that names the path in order to say it is gone. The replacement path, where named, is also absent, so the label is not a successful retarget.
- **unresolved** — no rule could class the token. None.

A `read 2026-09-28` stamp is a verification date, not a retirement. Round-16's lesson naming the debt does not convert the unedited `SKILL.md` / `PROVINCE.md` line into marked-historical.

## Agreement with the lane record

Lane record measured: `corpus/lessons/round-16-recensus.md`, `LOG.md:24-28`, `SCORECARD.md:364`, plus the still-standing round-15 census at `SCORECARD.md:184-225` and `LOG.md:22`.

| Lane claim | This sweep |
|---|---|
| `grader.py` has no `--src` and no origin-tree path | **Agree.** `grader.py` has 0 hits for every token in this sweep. |
| Round-16 lesson: wiki, `~/archive/bench-arena`, `~/bench-arena`, `~/.bailian` still written as current in `SKILL.md` / `PROVINCE.md` | **Agree**, and the lesson under-lists. The same claims are also live in `SHONEN.md:12`, `corpus/README.md`, `SCORECARD.md:3` and `:218`, `LOG.md:22` (`Resolving:`), and 17 knowledge source/command lines (5 wiki, 10 old-battery, 2 bailian). |
| Round-15 `origin-work` mentions marked historical | **Agree** for `SCORECARD.md:196`, `:205`, `:206`, `:222`, `:223` and the origin-work half of `LOG.md:22` (same line says gone). **Disagree** that `:186` is marked on its own line: the ABSENT marker is `:205`. Class labelled. |
| Round-15 (b) citation-to-deleted = 0 | **Disagree** if read as a host-surface census. True only of the ufo-fsd deleted-file class this sweep did not re-count. Host-path live citations are not zero. |
| Round-15 `~/archive/bench-arena` and wiki **resolves** (`SCORECARD.md:218`, `LOG.md:22`) | **Disagree** as a current fact. Both parents are absent. The sentences were not struck. Class **live**. Whether they were true at the 09:41 -0300 round-15 commit is **unresolved**: no transcript is in the commit. That does not retire the citation. |
| Round-14 "living pointers were corrected" to the archive path | **Disagree** as current. The archive path is absent, and ten knowledge lines still name `~/bench-arena` (six of them reproduction commands, plus `local-bench-arena.md:3`). |
| Zero citations to `ds4cc-marketplace`, `plazir-15-site`, and the-janitor install paths | **Agree.** 0 hits. |

## Counts

Token-hits: **369**. live **61**, labelled **14**, marked-historical **294**, unresolved **0**.

| Token | Hits | Live |
|---|---|---|
| `old-bench-arena` | 113 | 10 |
| `webzites-path` | 86 | 22 |
| `lowercase-projects` | 70 | 9 |
| `bailian` | 43 | 7 |
| `archive-bench-arena` | 38 | 12 |
| `origin-work` | 9 | 0 |
| `webzites-name` | 7 | 1 |
| `janitor-md` | 3 | 0 |

Zero-hit tokens: `ds4cc-marketplace`, `plazir-15-site`, `the-janitor-tree` (`the-janitor`, `~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.local/state/the-janitor`).

## Live citations

These fail "zero LIVE citations to deleted paths." Not suppressed. Not fixed.

### Wiki (`~/Projects/webzites`) — owner: operator restore or retire; kengaku record appends the marker

Unblock: restore `~/Projects/webzites/repos/llm-wiki`, or append an ABSENT erratum on the lines below. Do not retarget. Depth-4 name search found no copy.

- `PROVINCE.md:3` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `PROVINCE.md:12` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `PROVINCE.md:55` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:3` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:8` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:11` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:556` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:557` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:558` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:559` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:560` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:561` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:563` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:566` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `SKILL.md:571` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `corpus/knowledge/benchmark-selection.md:3` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `corpus/knowledge/eval-design-digest-2.md:7` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `corpus/knowledge/eval-theory-notes.md:6` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `corpus/knowledge/godspeed-eval-findings.md:3` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent
- `corpus/knowledge/telemetry-run-design.md:3` — current contract scopes or cites the wiki tree; ~/Projects/webzites is absent

`PROVINCE.md:55` is name-only (`webzites/llm-wiki` … are read-only). It presupposes the tree. Weaker than a path bullet; still live.

`SCORECARD.md:3` and `:218`, `LOG.md:22` are in the resolves cluster below.

### Archive battery (`~/archive/bench-arena`) — owner: operator restore or retire

Unblock: restore `~/archive/bench-arena`, or append ABSENT. Do not tell a reader the old path's replacement resolves.

- `PROVINCE.md:13` — \| Local benchmark battery \| `~/archive/bench-arena/` — relocated intact from `~/bench-arena/` during round 14; `tasks/`, `grade.sh`, `loop…
- `SHONEN.md:12` —   `PROVINCE.md` surfaces re-verified round 14: endpoint/process pin EXACT_MATCH; route telemetry remains ABSENT; benchmark tree relocated in…
- `SKILL.md:237` — 2. **Eval battery**: `~/archive/bench-arena/telemetry-qwenlocal-v2.csv` (33
- `SKILL.md:330` —    identically: `BENCH_ROOT=<scratch> bash ~/archive/bench-arena/grade.sh <label>`
- `SKILL.md:565` — - `~/archive/bench-arena/` (relocated intact from `~/bench-arena/` in round 14; `tasks/`, `report-grok45.csv`, `report-qwenlocal-v2.v2.csv`,…
- `SKILL.md:568` — - `127.0.0.1:34113` llama-server + `~/archive/bench-arena/grade.sh` — authored 4-task slice, 1/4 PASS vs predicted 2/4, `03` flip PASS→FAIL …
- `SKILL.md:570` — - `~/archive/bench-arena/` round-5 battery (then located at `~/bench-arena/`) — full 33-task direct-API re-run: 20/33 PASS, 8 status deltas …
- `corpus/README.md:16` — \| `knowledge/local-bench-arena.md` \| On-host 33-task battery: schema, two-model results, complementarity split \| `~/archive/bench-arena/`…
- `corpus/README.md:18` — \| `knowledge/bench-arena-fresh-run.md` \| Round-4 authored run: endpoint drift finding, 4-task reproduction slice, prediction error \| `~/a…
- `corpus/README.md:117` — - **Bench-arena path drift** (round 14): live tree relocated from `~/bench-arena` to `~/archive/bench-arena` with content hashes unchanged a…

### Old battery (`~/bench-arena`) still used as a source or command — owner: kengaku record

Unblock: append an absence erratum on these knowledge lines. Do not rewrite the round body. Do not point them at `~/archive/bench-arena` while that path is also absent.

- `corpus/knowledge/bench-arena-fresh-run.md:4` — `~/bench-arena/` tasks. Not an analysis of prior artifacts — an authored run.
- `corpus/knowledge/bench-arena-fresh-run.md:8` — - `~/bench-arena/loop.sh` runs `opencode run --agent raw --model "$MODEL"` per
- `corpus/knowledge/bench-arena-fresh-run.md:65` — mkdir -p /tmp/X/tasks && for t in <tasks>; do ln -s ~/bench-arena/tasks/$t /tmp/X/tasks/$t; done
- `corpus/knowledge/bench-arena-fresh-run.md:67` — cd ~/bench-arena && BENCH_ROOT=/tmp/X bash grade.sh <label>
- `corpus/knowledge/bench-arena-round5-battery.md:104` — for t in ~/bench-arena/tasks/*/; do ln -s "$t" /tmp/X/tasks/; done
- `corpus/knowledge/bench-arena-round5-battery.md:107` — cd ~/bench-arena && BENCH_ROOT=/tmp/X bash grade.sh <label>
- `corpus/knowledge/bench-arena-round6-stability.md:99` — BENCH_ROOT=/tmp/bench-r6 bash ~/bench-arena/grade.sh kq-r6-rep{1,2,3}
- `corpus/knowledge/bench-arena-round7-scaffold-ablation.md:130` — BENCH_ROOT=/tmp/bench-r7 bash ~/bench-arena/grade.sh kq-r7-E{0..4}[-r{1..3}]
- `corpus/knowledge/bench-arena-task27-timeout-anatomy.md:84` — `~/bench-arena/tasks/27-rwlock-writer-pref/test.sh`.
- `corpus/knowledge/local-bench-arena.md:3` — Source: `~/bench-arena/` — files verified by `ls`, `csv.DictReader` on

### `~/.bailian` — owner: operator restore or retire

Shape only. The directory is absent; contents were not read.

- `PROVINCE.md:16` — \| Client CLI telemetry \| `~/.bailian/telemetry.jsonl`, `~/.bailian/wiki-sync-state.json` \| quota-vs-auth failure split, poll-verb rule \|
- `PROVINCE.md:17` — \| Model catalogs \| `~/.bailian/skills/bailian-docs-llm-wiki/models/{index.md,models.jsonl}`, `https://huggingface.co/api/models`, `https:/…
- `SKILL.md:562` — - `~/.bailian/skills/bailian-docs-llm-wiki/models/index.md` + `models/models.jsonl` — 180 families / 413 models structured index; `contextWi…
- `corpus/README.md:15` — \| `knowledge/local-model-index.md` \| Bailian structured model index layout and field semantics \| `~/.bailian/skills/bailian-docs-llm-wiki…
- `corpus/README.md:21` — \| `knowledge/bailian-cli-telemetry.md` \| Client-side CLI telemetry: 4,274 records, quota-vs-auth failure split, poll-verb rule \| `~/.bail…
- `corpus/knowledge/bailian-cli-telemetry.md:3` — Source: `~/.bailian/telemetry.jsonl` — 4,274 JSONL records, span
- `corpus/knowledge/local-model-index.md:3` — Source: `~/.bailian/skills/bailian-docs-llm-wiki/models/` — `index.md` header states: 180 model families, 413 backbone models, generated 202…

### Lowercase `~/projects` — owner: kengaku record, not an operator restore

`/home/vgpnk/Projects/shokunin/CORPUS.md` exists. The lowercase directory does not.

- `corpus/README.md:4` — `` `~/projects/shokunin/CORPUS.md` `` as the corpus contract pointer. **Live.**

Eight executable defaults, same deleted root. Not `grader.py`. A stranger running them without an override fails closed on a missing directory. Class live because the default is what the file executes, not because they are the current gate.

- `corpus/evidence/round10-fleet/mutate_test.sh:9` — #   REPO_ROOT defaults to /home/vgpnk/projects/shokunin/kengaku-shokunin
- `corpus/evidence/round10-fleet/mutate_test.sh:31` — REPO="${1:-/home/vgpnk/projects/shokunin/kengaku-shokunin}"
- `corpus/evidence/round10-fleet/recompute_r8.py:5` — P = "/home/vgpnk/projects/shokunin/kengaku-shokunin/corpus/evidence/round8-horizon/results.jsonl"
- `corpus/evidence/round10-fleet/recompute_r9.py:5` — P = "/home/vgpnk/projects/shokunin/kengaku-shokunin/corpus/evidence/round9-replication/results-r9.jsonl"
- `corpus/evidence/round10-fleet/schema_probe.py:13` — REPO = "/home/vgpnk/projects/shokunin/kengaku-shokunin"
- `corpus/evidence/round9-fleet/analyze.py:5` — REPO = "/home/vgpnk/projects/shokunin/kengaku-shokunin/corpus/evidence/round8-horizon"
- `corpus/evidence/round9-fleet/test_harness.py:23` — R8  = "/home/vgpnk/projects/shokunin/kengaku-shokunin/corpus/evidence/round8-horizon/results.jsonl"
- `corpus/evidence/round9-fleet/test_harness.py:24` — SRC = "/home/vgpnk/projects/shokunin/kengaku-shokunin/corpus/evidence/round8-horizon/horizon.py"

### Resolves sentences the round-16 lesson did not strike — owner: kengaku record

Unblock: append that these sentences are not current. Do not re-pin. Do not delete the round-15 bytes.

- `SCORECARD.md:3` — domain header still scopes `` `~/Projects/webzites/repos/llm-wiki` ``.
- `SCORECARD.md:218` — `` `~/archive/bench-arena` — resolves; `~/Projects/webzites/repos/llm-wiki` — `` (the word `resolves` for the wiki continues on `:219`). Both trees absent.
- `LOG.md:22` — `Resolving: ~/Projects/ufo-fsd-alpha, ~/archive/bench-arena, ~/Projects/webzites/repos/llm-wiki`. The ufo-fsd-alpha half still exists. The other two do not. The origin-work tokens on this same line are marked-historical (the line also says gone).

## Labelled

Partial retirement. Not a clean historical mark, and not a successful retarget.

- `PROVINCE.md:13` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `SCORECARD.md:169` `lowercase-projects` — contrasts stored lowercase path with current capital-P; does not assert lowercase resolves
- `SCORECARD.md:186` `origin-work` — relocation from-clause; ABSENT marker is :205, not this line
- `SKILL.md:565` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `SKILL.md:570` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `corpus/README.md:16` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `corpus/README.md:18` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `corpus/README.md:117` `old-bench-arena` — old path named as relocated-from / then-located / frozen; not an ABSENT marker, and the replacement path is also absent
- `corpus/knowledge/bench-arena-round12-ladder.md:199` `lowercase-projects` — quotes the stored generator path; next line records absence
- `corpus/lessons/round-4-aggregator-audit.md:65` `janitor-md` — present-tense in dated round-4 lesson; host file absent; not the current contract
- `corpus/lessons/round-16-recensus.md:23` `webzites-path` — round-16 debt note: path named absent and still written as current; not a use instruction
- `corpus/lessons/round-16-recensus.md:23` `archive-bench-arena` — round-16 debt note: path named absent and still written as current; not a use instruction
- `corpus/lessons/round-16-recensus.md:24` `old-bench-arena` — round-16 debt note: path named absent and still written as current; not a use instruction
- `corpus/lessons/round-16-recensus.md:24` `bailian` — round-16 debt note: path named absent and still written as current; not a use instruction

`corpus/lessons/round-16-recensus.md:23-24` is the lane's own debt label. Agree with the absence claim. It does not retire the live lines above.

## Unresolved

No token was left unclassified.

One fact is unresolved and is not a citation class: whether `SCORECARD.md:218` / `LOG.md:22` "resolves" was true at the round-15 commit (2026-10-14 09:41 -0300). The commit stores no `test -e` transcript. The round-16 lesson says the same. Current disk is the ground truth for this audit, and it is negative. That does not make the citation historical.

## Marked-historical

294 token-hits. Dated captures, or a line that itself says ABSENT / gone / historical / No such file. Not current use instructions. Full `path:line` list is the appendix.

Origin-work retirement that holds, re-measured absent:

- `SCORECARD.md:196` historical record
- `SCORECARD.md:205` **ABSENT**
- `SCORECARD.md:206` historical pointers
- `SCORECARD.md:222` erratum names the path
- `SCORECARD.md:223` directory is now gone
- `LOG.md:22` origin-work half (gone / now historical)

`corpus/evidence/round14-fleet/r14-scout-surfaces.md` still contains the verbatim `origin-work` lines. The scorecard erratum covers them. Class marked-historical, not live.

`corpus/knowledge/bench-arena-round12-ladder.md:200` records `ls -ld /home/vgpnk/projects` → No such file. That absence still holds. The quote on `:199` is labelled, not live.

## Janitor host paths

Literal `the-janitor`, `~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.local/state/the-janitor`: **0 hits**.

`~/.config/opencode/agents/janitor.md` is absent. Three hits, none in the current surface table:

- `corpus/evidence/round9-fleet/review.md:37` — marked-historical (round-9 EXISTS row)
- `corpus/evidence/round9-fleet/sweep.tsv:130` — marked-historical (round-9 EXISTS row)
- `corpus/lessons/round-4-aggregator-audit.md:65` — labelled (present tense "still references 8080" in a round-4 gap; not a current contract)

Owner of the missing agent file: operator / kagi substrate. Kengaku does not restore it. Not a live kengaku use instruction.

## Named debt

| ID | What | Owner | Unblock |
|---|---|---|---|
| KENG-DEAD-WIKI | 23 live wiki citations (22 path + 1 name), including `SCORECARD.md:3`, `:218`, and `LOG.md:22`; tree absent; no relocation at depth 4 | operator to restore or retire; kengaku record to append ABSENT | do not invent a new SSOT path |
| KENG-DEAD-ARCHIVE | live archive-path claims in PROVINCE, SKILL, SHONEN, README, SCORECARD:218, LOG:22 | operator to restore `~/archive/bench-arena` or retire it | do not re-pin content hashes from memory |
| KENG-DEAD-OLDBENCH | 10 knowledge lines still source or run `~/bench-arena` | kengaku record | append erratum; do not retarget at the also-absent archive |
| KENG-DEAD-BAILIAN | 7 live `~/.bailian` citations; directory absent | operator | restore or retire; shape only, never content-read |
| KENG-DEAD-CASE | `corpus/README.md:4` lowercase fleet root | kengaku record | point at `~/Projects/shokunin/CORPUS.md`, which exists |
| KENG-DEAD-SCRIPTS | 8 evidence-script defaults under `/home/vgpnk/projects/...` | kengaku record if those scripts are ever re-run | not the gate; override or make script-relative. Do not treat as current tooling |
| KENG-DEAD-RESOLVES | `SCORECARD.md:218` and `LOG.md:22` still say wiki and archive resolve | kengaku record | append that current truth is negative; do not re-pin; morning-of-round-15 accuracy stays unresolved |
| KENG-DEAD-ORIGIN | `SCORECARD.md:186` from-clause not marked on that line | none required for the gate | optional append that :205 covers :186. Path remains absent |
| KENG-DEAD-JANITOR-MD | 3 historical/labelled `janitor.md` hits; file absent | operator / kagi | not this lane's surface to restore |

Out of this sweep, not counted: `:34113`, pid 1299, `qwen-coder.service`, and `~/Projects/bounties/ledger/telemetry.jsonl`. The bounty row in `PROVINCE.md:15` is already marked ABSENT. Serving-plane liveness is kama's, not a deleted-path citation in this list.

## Appendix — every hit

`class` `file:line` `token`

- live `PROVINCE.md:3` `webzites-path`
- live `PROVINCE.md:12` `webzites-path`
- live `PROVINCE.md:13` `archive-bench-arena`
- labelled `PROVINCE.md:13` `old-bench-arena`
- live `PROVINCE.md:16` `bailian`
- live `PROVINCE.md:17` `bailian`
- live `PROVINCE.md:55` `webzites-name`
- live `SCORECARD.md:3` `webzites-path`
- marked-historical `SCORECARD.md:60` `old-bench-arena`
- marked-historical `SCORECARD.md:162` `archive-bench-arena`
- marked-historical `SCORECARD.md:162` `old-bench-arena`
- labelled `SCORECARD.md:169` `lowercase-projects`
- labelled `SCORECARD.md:186` `origin-work`
- marked-historical `SCORECARD.md:196` `origin-work`
- marked-historical `SCORECARD.md:205` `origin-work`
- marked-historical `SCORECARD.md:206` `origin-work`
- live `SCORECARD.md:218` `webzites-path`
- live `SCORECARD.md:218` `archive-bench-arena`
- marked-historical `SCORECARD.md:222` `origin-work`
- marked-historical `SCORECARD.md:223` `origin-work`
- live `SHONEN.md:12` `archive-bench-arena`
- live `SKILL.md:3` `webzites-path`
- live `SKILL.md:8` `webzites-path`
- live `SKILL.md:11` `webzites-path`
- live `SKILL.md:237` `archive-bench-arena`
- live `SKILL.md:330` `archive-bench-arena`
- live `SKILL.md:556` `webzites-path`
- live `SKILL.md:557` `webzites-path`
- live `SKILL.md:558` `webzites-path`
- live `SKILL.md:559` `webzites-path`
- live `SKILL.md:560` `webzites-path`
- live `SKILL.md:561` `webzites-path`
- live `SKILL.md:562` `bailian`
- live `SKILL.md:563` `webzites-path`
- live `SKILL.md:565` `archive-bench-arena`
- labelled `SKILL.md:565` `old-bench-arena`
- live `SKILL.md:566` `webzites-path`
- live `SKILL.md:568` `archive-bench-arena`
- live `SKILL.md:570` `archive-bench-arena`
- labelled `SKILL.md:570` `old-bench-arena`
- live `SKILL.md:571` `webzites-path`
- marked-historical `LOG.md:4` `webzites-path`
- marked-historical `LOG.md:4` `bailian`
- marked-historical `LOG.md:5` `lowercase-projects`
- marked-historical `LOG.md:6` `old-bench-arena`
- marked-historical `LOG.md:8` `webzites-path`
- marked-historical `LOG.md:8` `bailian`
- marked-historical `LOG.md:17` `old-bench-arena`
- marked-historical `LOG.md:17` `webzites-name`
- marked-historical `LOG.md:21` `archive-bench-arena`
- marked-historical `LOG.md:21` `old-bench-arena`
- marked-historical `LOG.md:22` `origin-work`
- live `LOG.md:22` `webzites-path`
- live `LOG.md:22` `archive-bench-arena`
- live `corpus/README.md:4` `lowercase-projects`
- live `corpus/README.md:15` `bailian`
- live `corpus/README.md:16` `archive-bench-arena`
- labelled `corpus/README.md:16` `old-bench-arena`
- live `corpus/README.md:18` `archive-bench-arena`
- labelled `corpus/README.md:18` `old-bench-arena`
- live `corpus/README.md:21` `bailian`
- live `corpus/README.md:117` `archive-bench-arena`
- labelled `corpus/README.md:117` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/INTEGRATOR-NOTES.md:72` `webzites-name`
- marked-historical `corpus/evidence/round10-fleet/INTEGRATOR-NOTES.md:75` `old-bench-arena`
- live `corpus/evidence/round10-fleet/mutate_test.sh:9` `lowercase-projects`
- live `corpus/evidence/round10-fleet/mutate_test.sh:31` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:26` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:27` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:28` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:29` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:31` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:32` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-connector.md:34` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-critic.md:6` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-critic.md:44` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-mutation-sh.md:38` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-mutation-sh.md:60` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-mutation-sh.md:268` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-report-draft.md:25` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:3` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:20` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:25` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:26` `bailian`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:29` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:31` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:32` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:33` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:34` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:35` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:36` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:42` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:44` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:67` `bailian`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:68` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:84` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-review-cites.md:85` `bailian`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:3` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:9` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:13` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:16` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:17` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:18` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:29` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:38` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:43` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:59` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:92` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:119` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:121` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:145` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:148` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-bench.md:156` `old-bench-arena`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-wiki.md:4` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-wiki.md:4` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-wiki.md:31` `webzites-path`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-wiki.md:55` `lowercase-projects`
- marked-historical `corpus/evidence/round10-fleet/r10-scout-wiki.md:55` `webzites-path`
- live `corpus/evidence/round10-fleet/recompute_r8.py:5` `lowercase-projects`
- live `corpus/evidence/round10-fleet/recompute_r9.py:5` `lowercase-projects`
- live `corpus/evidence/round10-fleet/schema_probe.py:13` `lowercase-projects`
- marked-historical `corpus/evidence/round11-fleet/r11-connector.md:15` `lowercase-projects`
- marked-historical `corpus/evidence/round11-fleet/r11-connector.md:25` `webzites-name`
- marked-historical `corpus/evidence/round11-fleet/r11-connector.md:47` `lowercase-projects`
- marked-historical `corpus/evidence/round11-fleet/r11-critic-design.md:7` `lowercase-projects`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:66` `old-bench-arena`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:80` `webzites-path`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:80` `old-bench-arena`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:80` `bailian`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:81` `webzites-path`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:84` `old-bench-arena`
- marked-historical `corpus/evidence/round11-fleet/r11-review-baseline.md:89` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:10` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:22` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:48` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:57` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:67` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-connector.md:85` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:6` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:11` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:515` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:516` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:517` `bailian`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:523` `bailian`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:523` `webzites-name`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:545` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:545` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:550` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:571` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:581` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:582` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:583` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:584` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:596` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:597` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:598` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:603` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:618` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:619` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:637` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:708` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-endpoint-freshness.md:709` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-report-draft.md:6` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-draft.md:16` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-draft.md:52` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-draft.md:286` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-final.md:7` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-final.md:231` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-report-final.md:244` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-review-baseline.md:51` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-review-baseline.md:54` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-review-baseline.md:69` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-review-baseline.md:72` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-review-baseline.md:77` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-review-citations.md:375` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-review-citations.md:377` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:38` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:48` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:49` `lowercase-projects`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:59` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:62` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:69` `webzites-path`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:69` `old-bench-arena`
- marked-historical `corpus/evidence/round12-fleet/r12-scope-audit.md:114` `webzites-name`
- marked-historical `corpus/evidence/round12-ladder/analysis_r12.md:66` `lowercase-projects`
- marked-historical `corpus/evidence/round12-ladder/recompute-run.log:1` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/INTEGRATOR-NOTES.md:68` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/INTEGRATOR-NOTES.md:69` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-connector.md:46` `webzites-name`
- marked-historical `corpus/evidence/round14-fleet/r14-critic-landed.md:118` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/r14-landing-gate.md:88` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:5` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:5` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:5` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:12` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:14` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:35` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:36` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:37` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:38` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:39` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:40` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:41` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:137` `origin-work`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:148` `origin-work`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:165` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:165` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:170` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:173` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:175` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:178` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:180` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:181` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:190` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:192` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:199` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:199` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:208` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:208` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:213` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:214` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:215` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:216` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:217` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:218` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:233` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:239` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:243` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:244` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:246` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:247` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:249` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:249` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:258` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:274` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:276` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:284` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:289` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:331` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:332` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:332` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:333` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:333` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:337` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:338` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:344` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:382` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:384` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:385` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:385` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:386` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:388` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:389` `webzites-path`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:391` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:392` `bailian`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:403` `old-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scout-surfaces.md:404` `archive-bench-arena`
- marked-historical `corpus/evidence/round14-fleet/r14-scribe-drafts.md:59` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/r14-scribe-drafts.md:277` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/drafts/lessons-round-12.md:77` `lowercase-projects`
- marked-historical `corpus/evidence/round14-fleet/drafts/lessons-round-14.md:43` `lowercase-projects`
- live `corpus/evidence/round9-fleet/analyze.py:5` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/prior-art.md:90` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/review.md:14` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/review.md:16` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/review.md:31` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/review.md:33` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/review.md:34` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/review.md:35` `bailian`
- marked-historical `corpus/evidence/round9-fleet/review.md:36` `bailian`
- marked-historical `corpus/evidence/round9-fleet/review.md:37` `janitor-md`
- marked-historical `corpus/evidence/round9-fleet/review.md:38` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/review.md:45` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sibling-overlap.md:5` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sibling-overlap.md:27` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:1` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:5` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:12` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:13` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:14` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:15` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:16` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:17` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:18` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:19` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:20` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:24` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:28` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:30` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:31` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:32` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:35` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:43` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:45` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:46` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:53` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:67` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:69` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:70` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:97` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:98` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:99` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:104` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:105` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:107` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:108` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:109` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:111` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:113` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:116` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:117` `bailian`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:118` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:120` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:121` `lowercase-projects`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:123` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:125` `old-bench-arena`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:127` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:129` `webzites-path`
- marked-historical `corpus/evidence/round9-fleet/sweep.tsv:130` `janitor-md`
- live `corpus/evidence/round9-fleet/test_harness.py:23` `lowercase-projects`
- live `corpus/evidence/round9-fleet/test_harness.py:24` `lowercase-projects`
- marked-historical `corpus/evidence/round9-replication/replication.md:71` `lowercase-projects`
- live `corpus/knowledge/bailian-cli-telemetry.md:3` `bailian`
- live `corpus/knowledge/bench-arena-fresh-run.md:4` `old-bench-arena`
- live `corpus/knowledge/bench-arena-fresh-run.md:8` `old-bench-arena`
- live `corpus/knowledge/bench-arena-fresh-run.md:65` `old-bench-arena`
- live `corpus/knowledge/bench-arena-fresh-run.md:67` `old-bench-arena`
- labelled `corpus/knowledge/bench-arena-round12-ladder.md:199` `lowercase-projects`
- marked-historical `corpus/knowledge/bench-arena-round12-ladder.md:200` `lowercase-projects`
- live `corpus/knowledge/bench-arena-round5-battery.md:104` `old-bench-arena`
- live `corpus/knowledge/bench-arena-round5-battery.md:107` `old-bench-arena`
- live `corpus/knowledge/bench-arena-round6-stability.md:99` `old-bench-arena`
- live `corpus/knowledge/bench-arena-round7-scaffold-ablation.md:130` `old-bench-arena`
- live `corpus/knowledge/bench-arena-task27-timeout-anatomy.md:84` `old-bench-arena`
- live `corpus/knowledge/benchmark-selection.md:3` `webzites-path`
- live `corpus/knowledge/eval-design-digest-2.md:7` `webzites-path`
- live `corpus/knowledge/eval-theory-notes.md:6` `webzites-path`
- live `corpus/knowledge/godspeed-eval-findings.md:3` `webzites-path`
- live `corpus/knowledge/local-bench-arena.md:3` `old-bench-arena`
- live `corpus/knowledge/local-model-index.md:3` `bailian`
- live `corpus/knowledge/telemetry-run-design.md:3` `webzites-path`
- marked-historical `corpus/lessons/round-1-aggregator-audit.md:5` `webzites-path`
- marked-historical `corpus/lessons/round-1-aggregator-audit.md:6` `bailian`
- marked-historical `corpus/lessons/round-1-aggregator-audit.md:12` `lowercase-projects`
- marked-historical `corpus/lessons/round-1-aggregator-audit.md:59` `webzites-path`
- marked-historical `corpus/lessons/round-1-aggregator-audit.md:71` `bailian`
- marked-historical `corpus/lessons/round-1.md:4` `lowercase-projects`
- marked-historical `corpus/lessons/round-1.md:9` `webzites-path`
- marked-historical `corpus/lessons/round-3.md:4` `lowercase-projects`
- marked-historical `corpus/lessons/round-3.md:12` `old-bench-arena`
- marked-historical `corpus/lessons/round-4-aggregator-audit.md:25` `old-bench-arena`
- marked-historical `corpus/lessons/round-4-aggregator-audit.md:27` `bailian`
- marked-historical `corpus/lessons/round-4-aggregator-audit.md:36` `webzites-path`
- marked-historical `corpus/lessons/round-4-aggregator-audit.md:49` `webzites-path`
- labelled `corpus/lessons/round-4-aggregator-audit.md:65` `janitor-md`
- marked-historical `corpus/lessons/round-6-aggregator-audit.md:36` `bailian`
- marked-historical `corpus/lessons/round-6-aggregator-audit.md:157` `lowercase-projects`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:12` `webzites-path`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:13` `bailian`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:15` `old-bench-arena`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:36` `old-bench-arena`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:37` `old-bench-arena`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:43` `bailian`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:71` `old-bench-arena`
- marked-historical `corpus/lessons/round-8-aggregator-box3-coldrun.md:102` `bailian`
- labelled `corpus/lessons/round-16-recensus.md:23` `webzites-path`
- labelled `corpus/lessons/round-16-recensus.md:23` `archive-bench-arena`
- labelled `corpus/lessons/round-16-recensus.md:24` `old-bench-arena`
- labelled `corpus/lessons/round-16-recensus.md:24` `bailian`

Appendix rows: 369. live 61, labelled 14, marked-historical 294, unresolved 0.
