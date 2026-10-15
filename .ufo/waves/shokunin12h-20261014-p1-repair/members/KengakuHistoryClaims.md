# KengakuHistoryClaims — advisory (wave shokunin12h-20261014-p1-repair)

Seat: `KengakuHistoryClaims` (revenger / L2 leaf). Lane: `kengaku-shokunin`.
Steered round: **16**. Starting HEAD (`baselines.json`): `d84e48d525d6af6b1d137d608aea8c726f8bead4`.
Before receipt: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kengaku-before.json` (`python3 grader.py`, exit 0, `CHECKS n=733 mismatches=0 errata_pinned=1`). This seat did not re-run the gate.

**Not a native judge verdict, lane-round report, receipt, or admission.** No stage, commit, or push. No gate edit. No LOG, SCORECARD, SKILL, PROVINCE, or corpus byte was rewritten. Original history stays. The blocks under "Proposed append-only errata" are drafts for the parent, not applied text.

## Reconstructed contract

Living notes (SKILL, PROVINCE, `corpus/README.md`, `corpus/knowledge/`, `corpus/lessons/`) may keep a citation only as a dated snapshot once the target is gone or the revision it pins is no longer the thing a reader should open. A current-tense pin of a missing path is citation-to-deleted. A current-tense pin of an old hash, line number, pid, or count is a superseded revision and must be described, not re-pinned. Append an erratum. Do not edit the original sentence. Evidence trees under `corpus/evidence/` are frozen capture records; they are classified here only when a living note still sends a reader to them as current.

## Measurement (this session, after the before receipt)

Commands and observed results. Paths were existence-tested, not content-read when they sit next to credential or session material.

| Check | Command / method | Observed |
|---|---|---|
| Lane HEAD | `git -C kengaku-shokunin rev-parse HEAD` | `d84e48d525d6af6b1d137d608aea8c726f8bead4` (commit `2026-10-14 09:41:08 -0300`, subject round-15; diff stat is `LOG.md` +1 and `SCORECARD.md` +50 only) |
| UFO checkout | `test -d ~/Projects/ufo-fsd-alpha`; `git rev-parse HEAD` | present; `964f443ee53df0ce06bd689af01f0dea031b01f9` (`2026-10-12 18:32:12 -0300`) |
| Old UFO checkout | `test -d ~/Projects/origin-work` and `.../origin-work/ufo-fsd-alpha` | both absent |
| Upstream deletions | `git -C ~/Projects/ufo-fsd-alpha diff --name-status --diff-filter=D 5725fa7d3 HEAD` | **970** `D` lines; `rev-list --count 5725fa7d3..HEAD` = 3. The recalled "~50" figure was not used |
| Note intersection | those 970 paths and distinctive basenames vs SKILL, PROVINCE, `corpus/README.md`, `corpus/knowledge/*.md`, `corpus/lessons/*.md` | full-path hits **0**; basename hits **0**; `atomic-write.mjs`, `refusal-line.mjs`, `sync.test.mjs`, `native_epoch.rs`, `charter-scribe` absent from that note set |
| Gate `--src` | `grep` of `grader.py` for `--src` / `UFO_SRC` | no matches. GateRepair's separate report agrees; this seat did not edit `grader.py` |
| Host name search | walk `/home/vgpnk` depth 6 and `/home/vgpnk/Projects` depth 5 for `llm-wiki`, `bench-arena`, `webzites`, `bounties`, `bailian-docs-llm-wiki` | **0** directory hits outside this lane's own note filenames |
| `~/Projects` children | directory listing | 30 entries; no `webzites`, `bounties`, `the-bounty-hunter`, or `origin-work`. Parent mtime `2026-10-14T22:02:04Z` matches new `omegag-ds-*` children, not a deletion receipt |
| Deleted or absent host paths | `Path.exists` | `~/Projects/webzites/repos/llm-wiki`, `~/wikillm/llm-wiki`, `~/archive`, `~/archive/bench-arena`, `~/bench-arena`, `~/Projects/bounties`, `~/Projects/the-bounty-hunter`, `~/.bailian` (whole tree), `~/.config/llama`, `~/.config/systemd/user/qwen-coder.service`, `/proc/1299`, `~/projects` (lowercase), `/scratch` |
| Endpoint | `urlopen http://127.0.0.1:34113/health` timeout 5s | `URLError` `[Errno 111] Connection refused`. No body read |
| Case-variant fleet path | `test -e` | `~/projects/shokunin/CORPUS.md` absent; `~/Projects/shokunin/CORPUS.md` present. Round-1 and round-3 reports exist only under `~/Projects/shokunin/.ufo/reports/` |
| `/tmp/bench-*` | glob | 0 directories |
| In-repo pins | md5 / sha256 / line count of committed evidence | prefixes still match: `horizon.py` `1c157e2a` and 349 lines; r8 `results.jsonl` `df154cb5`; r8 `run.log` `fc3b232f`; r11 `results-r11.jsonl` `c42fe3d1`, `run.log` `281cb530`, `analysis_r11.md` `14663359`; r12 `results-r12.jsonl` `9dd8aa2b`, `run.log` `700d1ddd`, `analysis_r12.md` `029c3bcd`; `predictions-r9.md` sha256 starts `2a4f62ef`. Not restated as new pins |
| `opencode.json` | size only | exists, 95 bytes. **Content not read** (secret-adjacent). `~/.config/opencode/agents/janitor.md` absent |

`~/Projects` mtime does not prove when `webzites` disappeared. Round 15's "resolves" sentences have no saved `test -e` transcript in commit `d84e48d`.

## Clusters

Status is one of **live** (a reader is still told the target or revision is current), **superseded historical** (already framed as a dated snapshot or an erratum already demotes it), or **unresolved** (measurement cannot separate deletion from line-drift, or content was not read).

### HC-1 — llm-wiki SSOT — citation-to-deleted — **live**

Current-tense source of truth, not a dated digest marker.

- `SKILL.md:8-12` — "Source of truth: `~/Projects/webzites/repos/llm-wiki`". The `~/wikillm/llm-wiki` absence note on `:9-10` is still true and is not this defect.
- `SKILL.md:556-561`, `:563`, `:566`, `:571` — cited-source bullets still name that tree as the place to read.
- `PROVINCE.md:3` and surface row `PROVINCE.md:12` — listed as a live surface. No ABSENT mark.
- `corpus/README.md:12-14`, `:19-20`, `:27`, `:29` — index rows point at `llm-wiki/...` paths with no absence mark.
- Knowledge `Source:` lines still name the tree: `corpus/knowledge/benchmark-selection.md:3`, `godspeed-eval-findings.md:3`, `telemetry-run-design.md:3`, `gemini-benchmark-suite.md:3`. `eval-design-digest-2.md` and `eval-design-digest-3.md` cite `wiki/ai/...` and `wiki/karpathy/...` line anchors.

No relocation found. Round-15 `SCORECARD.md:218-219` says this path "resolves". That sentence is prose in a commit that saved no command output. **Unresolved** whether it was true at `2026-10-14 12:41Z`. **Live** as a citation now.

Wiki `:line` anchors (`eval-design-digest-2.md:13` `gpt-3-nonfiction.md:19,23-27`, and the other file:line cites in that digest) are **unresolved** line-drift. The files are absent, so new line numbers must not be invented.

### HC-2 — bench-arena living path — citation-to-deleted — **live**

Round 14 moved the living pointer from `~/bench-arena` to `~/archive/bench-arena` and said old-path commands were frozen evidence (`PROVINCE.md:13`, `corpus/README.md:117`). Both paths are now absent, and `~/archive` itself is absent. `/tmp/bench-*` is also gone.

Still written as the place to run or read:

- `SKILL.md:237-241`, `:330`, `:565`, `:568`, `:570` — `~/archive/bench-arena` as the current battery.
- `PROVINCE.md:13` — "all resolve at the archive path".
- `corpus/README.md:16`, `:18`, `:117` — archive path is the living pointer.
- Knowledge openings and reproduce fences still name `~/bench-arena` with no in-file absence erratum: `corpus/knowledge/local-bench-arena.md:3-6`, `bench-arena-fresh-run.md:4`, `:8`, `:65-67`, `bench-arena-round5-battery.md:104-107`, `bench-arena-round6-stability.md:98-99`, `bench-arena-round7-scaffold-ablation.md:130`, `bench-arena-task27-timeout-anatomy.md:84`.

`/tmp/bench-rN` citations that the notes already call ephemeral (`SKILL.md:569`, `corpus/README.md:22`) are **superseded historical**. The `~/bench-arena` reproduce fences are not; a reader can still run them.

`bench-arena-fresh-run.md:82` cites `loop.sh:32` and `:63`. The file is absent at both the old path and the archive path. Line-drift vs deletion is **unresolved**. Do not re-pin those line numbers. The field-count bug text stays a historical description.

Round-15 `SCORECARD.md:218` "`~/archive/bench-arena` — resolves" has the same missing-transcript problem as HC-1. Current `test -e` is false.

### HC-3 — bounty ledger — mixed

Already marked absent, so those sentences are **superseded historical**:

- `PROVINCE.md:15` — path ABSENT, "never treat the path as live".
- `SKILL.md:564` — "Path ABSENT as of round 11"; counts called historical.
- `corpus/README.md:17` — "(7,218 lines; now absent)".

Still present-tense, so **live**:

- `SKILL.md:222-236` — "Two distinct corpora exist" and "`~/Projects/bounties/ledger/telemetry.jsonl` (7,218 lines)" with no absence mark in that section. The cited-source bullet on `:564` contradicts the body.
- `corpus/knowledge/ledger-route-telemetry.md:3-7` — "the host's live lane-routing corpus".
- Same file `:59-65` — round-9 erratum still calls it "a live, growing surface" and tells the reader to re-run `wc -l < ~/Projects/bounties/ledger/telemetry.jsonl`. That command cannot run. The 7,224 figure is a superseded count, not a current total. Do not replace 7,218 or 7,224 with a new number.

`corpus/lessons/round-3.md:11-12` states the ledger "is a live lane-routing corpus" and `~/bench-arena/` "is a completed two-model battery". That file is a round-3 lesson, so the sentences are **superseded historical** narrative, but they are unmarked. Describe-don't-pin; do not rewrite them.

`PROVINCE.md:79-80` — "`~/Projects/the-bounty-hunter/` exists but carries no `ledger/telemetry.jsonl`". The directory is absent now. That existence claim is **live** citation-to-deleted of the negative-control path.

### HC-4 — Bailian client surfaces — citation-to-deleted — **live**

`~/.bailian` does not exist. No ABSENT mark on the province rows.

- `PROVINCE.md:16-17` — `~/.bailian/telemetry.jsonl`, `wiki-sync-state.json`, and `models/{index.md,models.jsonl}` listed as current surfaces.
- `SKILL.md:562` — models index "verified 2026-09-28".
- `corpus/README.md:15`, `:21`.
- `corpus/knowledge/local-model-index.md:3` — Source line, including `wiki-sync-state.json`.
- `corpus/knowledge/bailian-cli-telemetry.md:3` — "4,274 JSONL records".

The 4,274 / 180 / 413 figures are dated snapshots. They must not be re-counted or replaced. Content was not read (tree absent; would be shape-only if restored).

### HC-5 — process pin and `:34113` — superseded revision + citation-to-deleted — **live** in SKILL/PROVINCE

`SCORECARD.md:208-216` already records the endpoint absent and names the debt. That scorecard paragraph is **superseded historical** marking. SKILL and PROVINCE were not updated, and this seat did not update them.

Still written as the current stack:

- `PROVINCE.md:14` — process-level pin, pid 1299, unit file, q4_0 KV, jinja path.
- `SKILL.md:320-323` — live llama-server is `127.0.0.1:34113` via `qwen-coder.service`.
- `SKILL.md:450-457` — "process-pinned as of round 10 (pid 1299; `/proc/<pid>/cmdline` == `~/.config/systemd/user/qwen-coder.service` ExecStart, 41 tokens, EXACT_MATCH)".
- `corpus/knowledge/bench-arena-round12-ladder.md:218-219` — "server pid **1299**" inside a caveat a reader can take as current.

Measured now: port connection refused; `/proc/1299` absent; unit file absent; `~/.config/llama/qwen-coder-godspeed.jinja` absent; `~/.config/llama` absent. Do not re-pin pid, argv length, or the unit path as current. The round-10 EXACT_MATCH sentence stays a capture-time fact.

### HC-6 — Janitor consumer file — citation-to-deleted — **live**; baseURL **unresolved**

- `corpus/lessons/round-4-aggregator-audit.md:65` — "`~/.config/opencode/agents/janitor.md` still references 8080". The file is absent. Aggregator-owned lesson; do not rewrite it.
- `~/.config/opencode/opencode.json` exists (95 bytes). `SKILL.md:321-322` and `bench-arena-fresh-run.md:13-16` say `qwen-local` still points at `localhost:8080`. **Unresolved**: content not read. Not classified as deleted, and not confirmed still true.

### HC-7 — lowercase `~/projects/shokunin` — citation-to-deleted of a case path — **live** as a contract pointer

Linux path check: `/home/vgpnk/projects` absent; `/home/vgpnk/Projects/shokunin` present.

- `corpus/README.md:4` — "Per `~/projects/shokunin/CORPUS.md`" as the current contract. **Live**.
- Lesson evidence lines name the lowercase report path: `corpus/lessons/round-1.md:4`, `round-1-aggregator-audit.md:12`, `round-3.md:4`. The reports exist at the capital-P path (`round-1/kengaku-shokunin.md`, `round-3/kengaku.md`). Those lesson lines are **superseded historical** spellings. Do not rewrite them. Describe the surviving path; do not pin a commit hash onto it.

### HC-8 — ufo-fsd deleted files and `origin-work` — **superseded historical** (measured negative)

No living note cites a file from the 970-path deletion set. `PROVINCE.md:55` names `ufo-fsd-alpha` only as a read-only domain repo, not as a file pin. `origin-work` appears in `corpus/evidence/round14-fleet/r14-scout-surfaces.md:137` and `:148` as a neighbour observation. `SCORECARD.md:221-225` already appends the erratum that the directory is gone. Re-measured: still absent. No second erratum, and no in-place edit.

The round-15 hash prefix `964f443e` still matches `git rev-parse HEAD`. That is not a superseded pin. Do not copy it into SKILL or corpus as a new "current HEAD" sentence. Describe the observation; the scorecard already holds the prefix.

`grader.py` has no `--src` and no `UFO_SRC`. Stale-default repair is not a history-claim defect. GateRepair owns that file; this seat found nothing to hand it.

### HC-9 — in-repo evidence hashes and the 733-check line — **live and consistent**

The md5/sha256 prefixes listed above still match the committed bytes at `d84e48d`. The before receipt's `CHECKS n=733 mismatches=0 errata_pinned=1` matches the living pin in `SKILL.md` / `PROVINCE.md:19` / `corpus/README.md:76`. Not a superseded revision. Not re-pinned here. Not re-executed.

Historical grader line counts (936, 1709, 1711) appear in evidence drafts and lessons as an already-adjudicated defect class (`bench-arena-round12-ladder.md:214` cites the class, not a current `wc -l`). Current `grader.py` is 5737 lines. That count is **not** a freshness pin and must not be written as one.

### HC-10 — `~/wikillm/llm-wiki` — **superseded historical**

`SKILL.md:9-10` and `PROVINCE.md:12` already say the path does not exist. Re-measured absent. No new erratum.

## Divergences from the round-15 census

Round 15 (`SCORECARD.md:198-200`) recorded stale `--src` 0, citation to an upstream-deleted file 0, line-drift 0, genuine lane defect 0, and said substrate drift did not reach the lane.

What still holds, by this session's measurement:

- No `--src` in the gate.
- No citation in SKILL, PROVINCE, or corpus notes to a file in the 970-line upstream deletion diff.
- `origin-work` remains a historical neighbour mention, already errata'd.
- In-repo probe hashes and the 733-check line are not drifted.

What round 15 did not close, or no longer matches:

- Host surfaces the scorecard called resolving (`llm-wiki`, `~/archive/bench-arena`) are absent now. Whether they resolved at commit time is **unresolved** (no transcript).
- SKILL body and `ledger-route-telemetry.md` still call the bounty ledger live after the cited-source bullet marked it absent.
- Bailian, the unit file, the jinja path, pid 1299, and `the-bounty-hunter` are absent and still described as current in SKILL or PROVINCE.
- Those are citation and revision defects in the notes, not a grader defect. They do not authorize a `grader.py` edit.

## Proposed append-only errata

Parent appends. Do not patch the quoted sentences in place. Do not re-pin hashes, line numbers, pids, or counts. Each block names the text it supersedes.

### A. Append to `SKILL.md` (after the cited-source list)

```markdown
## Errata (appended round 16 re-census, 2026-10-14; not an in-place edit)

Supersedes the current-tense path and process pins below. Original sentences stay. Counts and hashes already in those sentences are capture-time descriptions, not new pins.

- **HC-1.** `:8-12` and cited-source bullets `:556-561`, `:563`, `:566`, `:571` name `~/Projects/webzites/repos/llm-wiki` as the source of truth. `test -e` on that path is false in this re-census. A depth-6 name search under `/home/vgpnk` found no `llm-wiki` or `webzites` directory. Digests in `corpus/knowledge/` remain the in-repo record of what was read on 2026-09-28. Do not open the wiki path as current, and do not invent replacement line numbers for wiki `:line` cites. The `~/wikillm/llm-wiki` absence note on `:9-10` is unchanged and still matches `test -e`.
- **HC-2.** `:237-241`, `:330`, `:565`, `:568`, `:570` name `~/archive/bench-arena` as the living battery. `test -e ~/archive/bench-arena`, `test -e ~/bench-arena`, and `test -e ~/archive` are all false. Reproduce commands that `cd` to either path are frozen recipes, not current instructions. CSV-derived numbers in `corpus/knowledge/local-bench-arena.md` stay snapshot text; they were not re-derived.
- **HC-3.** `:222-236` still says the lane-routing corpus exists at `~/Projects/bounties/ledger/telemetry.jsonl` with 7,218 lines. That contradicts `:564`, which already marks the path ABSENT. The `:564` marking stands. The 7,218 and the later 7,224/7,226 recounts are historical. Do not replace them with a new total. `wc -l` on that path cannot be run.
- **HC-4.** `:562` cites `~/.bailian/skills/bailian-docs-llm-wiki/models/index.md` and `models/models.jsonl` as verified. `test -e ~/.bailian` is false. The 180/413 figures stay the 2026-09-11/2026-09-28 snapshot. Do not re-count.
- **HC-5.** `:320-323` and `:450-457` describe pid 1299, `qwen-coder.service`, and `127.0.0.1:34113` as the live stack. This re-census: `urlopen` of `http://127.0.0.1:34113/health` raised `URLError` errno 111; `/proc/1299` absent; `~/.config/systemd/user/qwen-coder.service` absent; `~/.config/llama/qwen-coder-godspeed.jinja` absent. The round-10 EXACT_MATCH sentence is a capture-time description. Do not re-pin pid, token count, or argv.
```

### B. Append to `PROVINCE.md` (after the round-12/14 report-outs)

```markdown
## Round-16 re-census erratum (appended; surfaces table not rewritten)

Observed 2026-10-14 by existence tests, not by rewriting the table above.

- Research-notes row (`:12`): `~/Projects/webzites/repos/llm-wiki` is absent. No `webzites` or `llm-wiki` directory was found under `/home/vgpnk` to depth 6. The row is not a live surface until an operator restores or renames a checkout. `~/wikillm/llm-wiki` remains absent, as the row already says.
- Benchmark row (`:13`): `~/archive/bench-arena` is absent, and so is `~/bench-arena`. "All resolve at the archive path" is not a current instruction. Historical commands that use the old path stay frozen; they also do not resolve.
- Served-model row (`:14`): not a current process pin. `:34113/health` connection refused (errno 111); pid 1299, the user unit, and the jinja path are absent. Flag-change authority stays unowned. Do not re-pin the round-10 argv.
- Route-telemetry row (`:15`): absence reconfirmed. No change to the ABSENT marking.
- Client-CLI and model-catalog rows (`:16-17`): `~/.bailian` is absent, including `telemetry.jsonl`, `wiki-sync-state.json`, and `models/{index.md,models.jsonl}`. Those paths are not live surfaces. Public catalog URLs were not re-fetched.
- Round-11 report-out (`:79-80`): `~/Projects/the-bounty-hunter/` is absent. The sentence that it exists is a capture-time negative control, not a current path.
- `:55` names `ufo-fsd-alpha` as a read-only domain repo. That checkout is present at `~/Projects/ufo-fsd-alpha`. This lane's notes do not cite a file from `git diff --diff-filter=D 5725fa7d3 HEAD` (970 deletions). No file pin is added here.
```

### C. Append to `corpus/knowledge/ledger-route-telemetry.md`

```markdown
## Errata (appended round 16 re-census; supersedes the liveness assumption in the round-9 erratum)

The round-9 block above (`:59-65`) told readers to re-run `wc -l < ~/Projects/bounties/ledger/telemetry.jsonl` because the file was a live, growing surface. That command is not runnable: `test -e ~/Projects/bounties/ledger/telemetry.jsonl` is false, and `test -d ~/Projects/bounties` is false. No relocation was found in the depth-6 name search. The 7,218-line profile and the 7,224 recount stay snapshot text. Do not replace either number. Taxonomy and routing counts in this file are not re-derived. Mission-state semantics remain kasegi's; this lane does not absorb the missing tree.
```

### D. Append to `corpus/knowledge/local-bench-arena.md`

```markdown
## Errata (appended round 16 re-census)

`:3-6` cites `~/bench-arena/` as the source verified by `ls` on 2026-09-28. That path is absent. The round-14 living replacement `~/archive/bench-arena/` is also absent (`test -e` false; `~/archive` itself is absent). Numbers in this file are the 2026-09-28 snapshot. They were not recomputed from CSVs in this re-census. Do not treat the reproduce path as current.
```

### E. Append to `corpus/knowledge/local-model-index.md` and `corpus/knowledge/bailian-cli-telemetry.md`

```markdown
## Errata (appended round 16 re-census)

The Source path under `~/.bailian/` is absent (`test -e ~/.bailian` false; no relocation found). Figures in this file (index date, family/model counts, record count, date span) are the 2026-09-28 snapshot. Do not re-count. Do not read the tree for content if it reappears without a shape-only plan; credential and session material stays out of this corpus.
```

### F. Append to `corpus/README.md` (new gap bullet; do not edit `:4` or the index rows in place)

```markdown
- **Round-16 citation erratum (appended; index rows not rewritten).** `~/projects/shokunin/CORPUS.md` (`:4`) does not exist. The contract file is at the fleet root; on this host that is `~/Projects/shokunin/CORPUS.md` (`test -e` true). Do not pin the lowercase spelling as current. Living pointers to `~/Projects/webzites/repos/llm-wiki`, `~/archive/bench-arena`, and `~/.bailian` fail `test -e` and are not current surfaces; the knowledge entries remain the in-repo snapshots. The bounty-ledger index cell already says absent; that marking stands. In-repo evidence hash prefixes checked in this re-census still match the committed bytes; they are not restated as new pins.
```

### G. Parent-owned SCORECARD / LOG append (this seat does not write those files)

```markdown
## Round 16 — erratum to the round-15 "resolves" sentences (appended; round-15 text not rewritten)

Supersedes `SCORECARD.md:218-219` as a current-reader instruction. Those sentences said `~/archive/bench-arena` and `~/Projects/webzites/repos/llm-wiki` resolve. This re-census `test -e` is false for both, and a depth-6 name search found neither tree. The round-15 commit (`d84e48d`, 2026-10-14 09:41:08 -0300) saved no `test -e` transcript, so whether the sentences were true at commit time is unresolved. They are not current.

Unchanged from round 15, re-measured: `~/Projects/ufo-fsd-alpha` present; `git rev-parse HEAD` still matches the recorded prefix `964f443e` (full hash observed, not copied into SKILL). `~/Projects/origin-work` still absent. `~/Projects/bounties/ledger/telemetry.jsonl` still absent. No kengaku SKILL, PROVINCE, or corpus-note citation hits the 970 paths deleted in `git diff --diff-filter=D 5725fa7d3 HEAD`. The recalled "~50" count was not used.

`:34113` debt from round 15 stands: health connection refused (errno 111). Additional absent paths in the same stack: `/proc/1299`, `~/.config/systemd/user/qwen-coder.service`, `~/.config/llama/qwen-coder-godspeed.jinja`. Not re-pinned.

No gate change. `python3 grader.py` was not re-run; the before receipt remains the check line.
```

## Describe-don't-pin markings

Use these instead of new current pins:

- UFO checkout: "present at `~/Projects/ufo-fsd-alpha`; `git rev-parse HEAD` in this session matched the prefix already recorded in the round-15 scorecard. Not a new pin. Notes do not cite a deleted upstream file."
- Evidence hashes: "prefixes still match committed bytes at lane HEAD `d84e48d`. Not restated."
- Ledger counts: "7,218 is the 2026-09-28 profile; 7,224 and 7,226 are later recounts from when the file existed. No current total."
- Process pin: "round-10 capture described pid 1299 and a 41-token argv. That process and unit file are absent. Do not re-pin."
- Wiki and `loop.sh` line numbers: "unresolvable while the files are absent. Do not substitute new line numbers."
- Grader size: "line count is not a freshness pin. The registered verdict line is the check summary in the before receipt, not `wc -l`."
- Fleet contract path: "cite `$SHOKUNIN_ROOT/CORPUS.md` or `../CORPUS.md`. The lowercase `~/projects/shokunin` spelling does not exist here. The capital-P path does. Do not pin a commit onto that spelling correction."

## Named debt (retained)

| ID | Debt | Unblock | Owner |
|---|---|---|---|
| HC-1 | llm-wiki tree absent; SKILL/PROVINCE still call it the SSOT; wiki line cites unmeasurable | Operator restores or designates a checkout. Until then the append-only erratum is the current-reader mark. Do not guess lines | Operator for the tree. Kengaku for the note mark. Not a grader change |
| HC-2 | Both bench-arena paths absent; reproduce fences still name them; `loop.sh:32`/`:63` unmeasurable | Operator restores `~/archive/bench-arena` or records a new location with a fresh `ls`. Do not re-derive CSV numbers from memory | Operator for the tree. Kengaku for the note mark. Kumitate already has the `telemetry_source=journal` report-out (`PROVINCE.md:49-54`); no new taxonomy transfer |
| HC-3 | Ledger absence is marked in three places and contradicted in `SKILL.md:222-236` and the ledger note. `the-bounty-hunter` existence claim is false. Counting command dead | Append the errata above. Do not invent a line count. Kasegi owns ledger semantics if the tree returns | Operator for the tree. Kasegi for mission-state. Kengaku keeps model×lane inference as historical only |
| HC-4 | `~/.bailian` absent; province rows still live | Operator restores the tree or accepts historical-only catalog notes. Shape only if it returns | Operator. Kagi if credential material is in the restored tree. Kengaku does not read it |
| HC-5 | Serving plane absent; SKILL/PROVINCE still current-tense. Scorecard debt already named | Operator restores `qwen-coder.service` and llama-server. Do not re-pin pid 1299 | Unowned serving plane / kama for endpoint health. Kengaku does not take flag-change authority |
| HC-6 | `janitor.md` absent. `opencode.json` baseURL claim not re-read | Kagi may shape-check the consumer config. This seat did not read the 95-byte file | Kagi for Janitor consumer config. Kama if the question is which process listens |
| HC-7 | `corpus/README.md:4` cites a missing lowercase path | Append the gap bullet. Surviving file is `~/Projects/shokunin/CORPUS.md`. No restore required | Kengaku note mark. Protocol only if a fleet-wide case rule is wanted |
| HC-11/12 | `loop.sh` and wiki `:line` anchors | Blocked on HC-1 and HC-2 restore. Unresolved, not repaired by a new pin | Kengaku note mark |

No debt in this inventory authorizes editing `grader.py`, expected check counts, or in-repo evidence bytes.

## Cross-domain

- **Operator:** missing host trees (`webzites`/`llm-wiki`, `archive`/`bench-arena`, `bounties`, `the-bounty-hunter`, `.bailian`, `qwen-coder.service`, `/scratch`).
- **Kasegi:** bounty-ledger mission state, if the tree returns. This lane does not absorb it.
- **Kama / unowned serving plane:** `:34113` and the unit file. Already refused by `PROVINCE.md:24-25`.
- **Kagi:** `janitor.md` deletion and any `opencode.json` baseURL check. Content not read here.
- **Kumitate:** ufo-fsd deletion census is their gate's problem. This lane cites none of those 970 paths. The `loop.sh` telemetry-source report-out is already filed.
- **Protocol / parent:** append the SCORECARD/LOG erratum; do not rewrite round-15 bytes. Lowercase `~/projects` vs `$SHOKUNIN_ROOT` is a spelling defect, not a protocol amendment from this seat.

## Confidence

- High: current absence of the host paths, the empty upstream-file intersection, the in-repo hash matches, the endpoint refusal, and the lack of `--src` in `grader.py`.
- Medium: round-15 "resolves" historical accuracy. The commit contains the claim and no command transcript. Not treated as a measurement.
- Not claimed: a new grader verdict, a new line count for deleted files, or that the recalled "~50 upstream files" is the deletion set. The command that was run returned 970 `D` lines.
