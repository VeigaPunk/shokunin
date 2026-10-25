# KotobaHistoryClaims — advisory freshness re-census

Worker advisory only. Not a native judge verdict, not a lane round report, not a receipt, and not an admission. No lane file, gate file, LOG byte, corpus byte, or sibling report was edited. Starting revision matched `baselines.json`: `02302c521b933c55fc4be79193e61537e3380751`. Worktree dirty set at measurement was `?? plans/` only (parent plan; not this seat).

Axes used: freshness (current cite vs deleted/superseded), operability (append-only errata a later integrator can paste), calibration (do not re-pin a moved hash; do not treat a dated transcript as a live promise), adjacency (gate notes stay with GateRepair; quoted sibling text stays quoted).

## Method

Read-only existence, content-hash, and anchor-count measurements. Gates were not run. Credentials, oauth, `server.token`, `auth.json`, and `op.env` were not content-read.

Measured this session:

- `git -C kotoba-shokunin rev-parse HEAD` → `02302c521b933c55fc4be79193e61537e3380751`
- `test -e` on cited host paths (tables below)
- `sha256` of `~/.local/bin/omp` → `ff59fc1b484c1308a7247ad208305005627b3fac62b440737c2b1835ac32074e` (276199392 bytes, `omp/18.10.4`)
- `sha256` of `~/.opencode/bin/opencode` → `d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9` (210109920 bytes, `opencode v2.0.26`)
- omp template recovered by anchoring `Compress into one routing hint` through the next NUL → 273 bytes, sha256 `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51`, both `{{name}}` and `{{description}}` present
- opencode binary anchor counts: `disableClaudeCodePrompt` 0, `Instruction.resolve` 0, `InstructionContext.observe` 0, `system-context-builtins` 0, `CONTEXT.md` 0, `OPENCODE_DISABLE_CLAUDE_CODE` 0, `message=init count=` 0, `duplicate skill name` 0; `skills rescanned` 2, `ConfigInstructionPlugin` 8, `Instructions from:` 3, `OPENCODE_DISABLE_PROJECT_CONFIG` 2
- `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`
- moved ufo skill `~/Projects/ufo-fsd-alpha/skills/ufo/SKILL.md` exists; folded frontmatter `description` length is 605, not the historical 690. Do not adopt 605 as a new pin.
- `~/.omp/agent/agents/*.md` → 13 files, not 37
- `~/.agents/skills` → 7 directories, each with `SKILL.md` (godspeed, omarchy, reverse-engineer-anything, shokunin, swarm, tower, ufo). No `sekhmet`, `xbrd`, `wwkd`, or `bailian-*`
- `/home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md` → 8 files; `*-round-*.md` → 108 files
- `/home/vgpnk/Projects/shokunin/*-shokunin/AGENTS.md` → 12 files
- `--src` appears in kotoba `LOG.md` only, as the round-18 statement that the gates never took `--src`. No `--src` in lane `*.py` / `*.md` / `*.json` / `*.sh` outside fixtures.

`~/Projects/origin-work` is absent. `~/projects` (lowercase) is absent. `~/Projects/ufo-fsd-alpha` exists. `~/Projects/ufo-fsd-alpha/ports/xbgst-codex` is absent.

## Classification

- **live** — the cited path exists, or the pinned revision still matches the named bytes, and the sentence is allowed to stay current.
- **superseded historical** — original bytes remain, and an append-only errata already says the cite or pin is not current. Do not repeat that repair. Do not delete the original sentence.
- **unresolved** — the sentence still reads as current, measurement falsifies it, and no same-file errata discharges it. Retained as named debt. Draft text below is not applied.

PROVINCE.md is six lines, no path cite, no numeric claim. No cluster. Live empty.

Stale `--src`: no cluster. The round-18 negative still holds.

Line-drift of upstream `packages/opencode/src/skill/index.ts:321-343` (`SKILL.md:512-518`) was not measured against a local source tree. Not folded into citation-to-deleted.

## Already landed — do not repeat

Round 18 named four sites and marked them. Re-measured; the markers are still present and the path facts still hold.

| id | where | class | evidence |
|---|---|---|---|
| KTB-HC-01 | `SKILL.md:35-38` | superseded historical | origin-work ufo `SKILL.md` absent; marker says historical path, tree moved to `~/Projects/ufo-fsd-alpha`, 690-char description not re-pinned. Moved file exists. Folded description is not 690. |
| KTB-HC-01b | `LOG.md:469-471` | superseded historical | same path, same 2026-10-14 errata. LOG bytes not touched. |
| KTB-HC-02 | `corpus/knowledge/harness-verifier-round10.md:109-114` | superseded historical for the path only | `ports/xbgst-codex` absent under both trees. Marker keeps the observation as then-true. Counts around it are KTB-HC-08. |
| KTB-HC-03 | `corpus/knowledge/opencode-extraction-round14.md:3-12` | superseded historical for the v1 rule set | header says OC-1…OC-5 anchors are gone and the body is preserved verbatim. Live binary anchor counts agree. Body sha pins stay as the round-14 record. |
| KTB-HC-05 | `corpus/knowledge/instruction-surface-census-round13.md:10-23` and `:162-175` | superseded historical for the old class ids | old ids are named as not-live. § B table at `:207-209` is the v2 model. Current binary shas at `:22-23` match the binaries measured above. Those two full shas are current pins, not superseded pins. |

Template pin `c1f03c8e248eb40e…` in `SKILL.md:535-536`, `corpus/knowledge/harness-verifier-round10.md:77`, and `verifiers/baseline.json` `omp.elf.template_sha256` still matches the live omp binary. **Live. Do not describe-dont-pin it.**

`corpus/knowledge/checklist-execution-round17.md:221` and `:245` pin `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27`, which is the current sha256 of `verifiers/verify_skill_checklist.py`. **Live.**

`corpus/knowledge/independent-verification-round12.md:16` pins `a32da4a4…` and `430fe289…`, which match current `verifiers/verify_corpus_integrity.py` and `verifiers/verify_corpus_independent.py`. **Live.**

`corpus/knowledge/cold-run-round11.md:19-28` already says the round-11 content shas are not recoverable and not independently checkable. **Superseded historical.** Do not strip the transcript.

`corpus/knowledge/claim-census-round12.md` already labels the mismatched script shas FALSE at HEAD / STALE. **Superseded historical.**

`corpus/knowledge/sibling-description-rewrites-round8.md:444` quotes another lane's then-description containing `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`. Quoted meta-finding, not this lane's live path promise. **Superseded historical quote.** The file's own base path at `:5` is KTB-HC-09.

Round 17 case-corrected corpus `.ufo/reports` pointers off lowercase `/home/vgpnk/projects` (`checklist-execution-round17.md:263-268`, `LOG.md:863-867`). That repair landed for report pointers. It did not cover SKILL or the remaining corpus host cites. Do not reopen the report-pointer repair.

## Unresolved clusters

### KTB-HC-04 — extraction note still equates a superseded binary sha to the live baseline field

`opencode-extraction-round14.md:96-97` says binary sha256 `f9dab32248695e9ebd56b16a1921798fd85112cf5a69c7dfd0cabc1e17be4a11` is "equal to `verifiers/baseline.json` `measured_against.opencode_binary_sha256`". The header marks the rule set historical. That sentence is still a live cross-pin. Current `verifiers/baseline.json:7` is `d9123b9bcd…`, matching the live binary, not `f9dab322`.

Class: unresolved superseded-revision. Owner: parent append into the corpus note. Not a gate edit.

### KTB-HC-07 — SKILL still teaches the v1 opencode model and the 17-skill world as current

Round 18's SKILL errata covers only the 17→7 count (`SKILL.md:30-31`) and the origin-work path (`:35-38`). These sentences have no errata and still read as current craft:

- `:99` — opencode reads `CLAUDE.md` via `y[1]` and `~/.claude/CLAUDE.md` via `n[1]`, gated by `OPENCODE_DISABLE_CLAUDE_CODE`. Live binary: those anchors 0. `~/.claude/CLAUDE.md` absent.
- `:100` — opencode priority list `y` = AGENTS.md → CLAUDE.md → CONTEXT.md. Live binary: `CONTEXT.md` 0.
- `:101` — declared `instructions: []` fetches `https://`. Census `:175` and the anchor counts say that fetcher is gone. The v2 read-hook still emits `Instructions from:` (3 hits) for `AGENTS.md` paths, which is a different mechanism. Do not collapse those.
- `:509-511` — `message=init count=N`, latest 18, `duplicate skill name` warns. Live binary: both literals 0. `skills rescanned` is present (2).
- `:539-541` — cache "17 rows at round 9 … all 17 keys reproduce … 27/27 checks", stated as the verifier's current authority. Opening errata says the live set is 7. `verifiers/baseline.json` expects `omp.db.rows` 14, `omp.offered.skills` 7, `omp.cache.keys_reproduced` 7. Round 18 LOG says the harness gate is 28/28 after the grammar change, not 27/27. This seat did not re-run the gate.

Class: unresolved live claims. Owner: parent append into `SKILL.md`. Do not rewrite the table in place.

### KTB-HC-08 — harness-verifier counts still current-tense after the path marker

`harness-verifier-round10.md:93-118` and `:124-130` still say offered 17, keys 17/17, dangling pair `sekhmet`/`xbrd`, `~/.omp/agent/skills` adds skills, `~/.config/opencode/skills` and `~/.bailian/skills` are symlink trees, and `oc.log.init_count_max` 18 == 17+1. Only `:112-114` is marked historical.

Measured: `~/.agents/skills` has 7 entries and no dangling `sekhmet`/`xbrd`; `~/.omp/agent/skills` absent; `~/.config/opencode/skills` absent; `~/.bailian` absent. Baseline expects dangling 0, offered 7, `oc.log.init_count_max` 0, and has `oc.log.skills_rescan_max` expect 3 (`baseline.json:32-38`, `:80-82`, `:120-122`).

Class: unresolved superseded host-state. The path errata does not discharge the counts. Owner: parent append into the corpus note.

### KTB-HC-09 — lowercase `/home/vgpnk/projects` cites

`/home/vgpnk/projects` is absent. Surviving tree is `/home/vgpnk/Projects/shokunin`. Round 17 fixed report pointers only.

Still cited as the place to read files, with no absence marker:

| file:line | cite | surviving measured location |
|---|---|---|
| `SKILL.md:88`, `:97` | `/home/vgpnk/projects/shokunin/.ufo/prompts/` | `/home/vgpnk/Projects/shokunin/.ufo/prompts/` (116 `*.md`, 8 `*-L1.md`) |
| `SKILL.md:106`, `:482` | `/home/vgpnk/projects/shokunin/*/AGENTS.md` | capital-P `*-shokunin/AGENTS.md`, 12 files, not 6 |
| `SKILL.md:144`, `:153`, `:386`, `:484`, `:486` | same prompts tree | same surviving directory. L1 count 8 still matches. Round-file count does not: table says ~72 (`:98`), sources say 50 at round-9 recount (`:486`); measured 108 `*-round-*.md`. Do not re-pin 108. |
| `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10-11` | same lowercase globs | same |
| `corpus/knowledge/sibling-description-rewrites-round8.md:5` | `/home/vgpnk/projects/shokunin/` | capital-P tree |
| `corpus/knowledge/checklist-execution-round15.md:78` | lowercase `MISSION.md` | `/home/vgpnk/Projects/shokunin/MISSION.md` exists |
| `corpus/knowledge/checklist-execution-round16.md:88` | says three SKILL sites "now read" the lowercase prompts path | that form is the absent base |

Class: unresolved citation-to-deleted (case-moved base). Not line-drift. Owner: parent append. Describe the surviving capital-P tree; do not replace counts in place.

### KTB-HC-10 — SKILL Sources and evidence paragraphs cite vanished host trees

`SKILL.md:47-53` dates the survey 2026-09-28 and says verify before trusting. That is not an absence marker. `Sources` (`:454-497`) and the evidence paragraphs (`:107-142`) still name the files as the bibliography.

Absent, no marker:

- `~/.agents/skills/{wwkd,sekhmet-l3,xbrd-ask,bailian-protocol,bailian-cli,bailian-train-deploy,bailian-model-recommend,bailian-web-search,bailian-gen,bailian-finetune,bailian-docs-llm-wiki,bailian-managed-agent,bailian-sandbox}/SKILL.md` (`SKILL.md:454-476`)
- `~/.config/opencode/skills/ufo/SKILL.md` (`:48`, `:480`)
- `~/.agents/AGENTS.md` (`:107`, `:417`, `:482`)
- `~/.agents/godspeed-core/directive.md` (`:109`)
- `~/.config/opencode/agents/` and `~/.config/opencode/agent/ufo.md` (`:113-117`, `:490`)
- `~/.config/opencode/command/` (`:137`, `:496`)
- `~/.omp/agent/skills` as an offer-gate root (`:176`) and `~/.omp/agent/skills/ufo/SKILL.md` (cited from `render-mechanism-round7.md:64`)

Still present, leave live:

- `~/.agents/skills/godspeed/SKILL.md`, `~/.agents/skills/omarchy/SKILL.md`
- `~/.local/bin/omp`, `~/.opencode/bin/opencode`, `~/.omp/agent/skill-descriptions.db`, `~/.omp/agent/sessions`, `~/.local/share/opencode/opencode.db`, `~/.local/share/opencode/log/opencode.log`
- `~/.claude/skills` exists and contains only `omarchy`

Measured survivors, describe only, do not retarget the old cite by rewriting it:

- `wwkd` skill file exists at `~/Projects/ufo-fsd-alpha/skills/wwkd/SKILL.md`
- godspeed directive exists at `~/Projects/godspeed-core/directive.md` and `~/.agents/skills/godspeed/directive.md`

`~/wikillm` and `~/.xbgst` at `SKILL.md:598` are already named dead. Live negative. Do not errata them again.

Class: unresolved citation-to-deleted on the standing bibliography. Owner: parent append into `SKILL.md`.

### KTB-HC-11 — render-mechanism dangling-symlink claim

`corpus/knowledge/render-mechanism-round7.md:64-67` says `~/.omp/agent/skills/ufo/SKILL.md` wins over `~/.config/opencode/skills/ufo/`, and `~/.agents/skills/{sekhmet,xbrd}` are dangling symlinks into ufo-fsd-alpha. No errata. All four paths are absent. The directories are gone, not dangling. Round 18 LOG says the dangling pair is gone; this note was not marked.

Class: unresolved citation-to-deleted. Owner: parent append into that note.

### KTB-HC-12 — agents-md fact table

`corpus/knowledge/agents-md-and-dispatch-surfaces.md:3` says sourced 2026-09-28. `:9-11` and `:26` still state as fact: 16 skills under `~/.agents/skills/` plus `~/.config/opencode/skills/`, lowercase AGENTS glob, and a ~60-line `~/.agents/AGENTS.md`. Measured: 7 skill dirs, opencode skills dir absent, host AGENTS.md absent, lowercase glob absent.

Class: unresolved. A source date is not an absence marker. Owner: parent append.

### KTB-HC-13 — corpus index still describes the superseded model as the current row

`corpus/README.md` FILE-column paths resolve (before-receipt `missing=0`; not re-run here). The Basis column is outside that gate and still describes superseded revisions as the standing summary:

- `:34` — harness verifier "27 checks" and "17/17 reproduction" plus init-count == root union. Baseline and round 18 LOG say otherwise.
- `:38` — opencode's 9 classes "are now reproduced" by OC-1…OC-6 including `instruction-context`. Extraction header and census `:175` say those ids are historical.
- `:39` — opencode model "quoted from its shipped JS" as priority list AGENTS.md→CLAUDE.md→CONTEXT.md plus `~/.claude/CLAUDE.md` and fetched `https://` entries. Census § B was rewritten; this index row was not.
- `:31` — offer trace keyed on `message=init count=N`. Literal absent from the live binary.

Class: unresolved superseded-revision in the standing index. Owner: parent append to `corpus/README.md`. Do not rewrite the rows.

### KTB-HC-14 — round-13 remeasure has no errata

`corpus/knowledge/instruction-surface-remeasure-round13.md` has no 2026-10-14 marker. `:23-25` records agreement that opencode loads `CLAUDE.md` via `y[1]` / `n[1]`, walks AGENTS→CLAUDE→CONTEXT, and fetches `https://` instructions. Those anchors are 0 in the live binary. The note is a round-13 witness, but nothing in the file says the agreement is not the current model. Census § B now contradicts it.

Class: unresolved superseded-revision. Owner: parent append. Do not delete the agreement table.

### KTB-HC-15 — "37 files live" omp agent roster

`SKILL.md:120` and `instruction-surface-census-round13.md:222` say `~/.omp/agent/agents/*.md` → 37 files live. The directory exists. Measured `*.md` count is 13. The census errata says § A stays live and does not discharge this exclusion-row count.

Class: unresolved superseded count. Path is live. Do not re-pin 13 into the original sentence. Owner: parent append.

### KTB-HC-16 — verifier content shas with no not-current marker

These are round transcripts or artifact tables. They were true of that round. They are not the current file identity, and the file does not say so.

| file:line | pinned sha256 prefix | current file sha256 prefix |
|---|---|---|
| `checklist-execution-round15.md:212` | `f169f247` `verify_skill_checklist.py` | `02ccf1b3` |
| `checklist-execution-round15.md:213` | `6bccc6b2` `checklist-baseline.json` | `68831bb3` |
| `checklist-execution-round15.md:214` | `200f38dd` `checklist-command-vocabulary.json` | `76d16a9c` |
| `checklist-execution-round16.md:119-120` | `70f8b38e` `verify_skill_checklist.py` | `02ccf1b3` |
| `harness-verifier-round10.md:34` | `55016ef5…` as the omp region under discussion, dated 2026-09-28, no not-current marker | live omp is `ff59fc1b…` |

Class: unresolved describe-dont-pin. Keep the original pins. Mark them as the revision they describe. Owner: parent append. Historical shas stay in the note; they must not be read as the current pin. Do not move them into LOG by deleting them here.

### KTB-HC-17 — gate-note residue (not edited)

`verifiers/baseline.json` checks were re-recorded in round 18. Three notes still describe the old world:

- `:126` `omp.db.rows` still cites `~/Projects/origin-work/ufo-fsd-alpha` as the project-scoped copy example
- `:127` `omp.offered.dangling` still says recorded dangling entries are `sekhmet`, `xbrd`, while `checks.omp.offered.dangling.expect` is 0
- `:129` `oc.log.init_count_max` still says the check is max of `message=init count=N`, while that literal is absent and the new check is `oc.log.skills_rescan_max`

Class: unresolved, gate file. Owner: KotobaGateRepair. This seat did not edit it. Not a reason to re-pin check expects.

### KTB-HC-18 — round-18 completeness sentence

`LOG.md:908-914` says citations to upstream-deleted/moved files were 4, all marked, and genuine lane defects were 0. That sentence is true of the four sites it names. It is false as a completeness claim against the clusters above. Do not rewrite it. A later append must name it.

Class: unresolved completeness claim in an append-only log. Owner: parent / record seat, append only.

## Proposed append-only errata

Paste targets only. Original sentences stay. No sha of a superseded revision is introduced as a current pin. Current binary shas already pinned in the census are not repeated here.

### Append to `SKILL.md`

```
## Errata — 2026-10-14 re-census (append-only; do not treat as a new pin set)

The 2026-10-14 markers at the truncator-key example stay. They do not cover the rows below. Each cited path was existence-tested against this host. Absent means absent. A surviving location is described, not substituted into the original sentence.

- `/home/vgpnk/projects/shokunin` is absent. The observed tree is `/home/vgpnk/Projects/shokunin`. Dispatch-prompt and AGENTS cites that use the lowercase base (`:88`, `:97`, `:106`, `:144`, `:153`, `:386`, `:482`, `:484`, `:486`) are historical citations. `*-L1.md` still numbers 8 under the capital-P tree. The "~72" / "50" round-file counts are not re-pinned; re-derive before citing.
- Host bibliography paths that do not exist, and are not already marked dead: `~/.agents/skills/{wwkd,sekhmet-l3,xbrd-ask,bailian-*}/SKILL.md`, `~/.config/opencode/skills/ufo/SKILL.md`, `~/.config/opencode/agents/`, `~/.config/opencode/agent/ufo.md`, `~/.config/opencode/command/`, `~/.agents/AGENTS.md`, `~/.agents/godspeed-core/directive.md`, `~/.omp/agent/skills`. `wwkd` is present only as `~/Projects/ufo-fsd-alpha/skills/wwkd/SKILL.md`. The godspeed directive is present as `~/Projects/godspeed-core/directive.md` and `~/.agents/skills/godspeed/directive.md`. Do not retarget the old cites by editing them.
- Opencode craft rows `:99-101` and the log recipe `:509-511` describe the 2026-09-28 binary. In `opencode` v2.0.26 those anchors are absent (`CONTEXT.md`, `OPENCODE_DISABLE_CLAUDE_CODE`, `Instruction.resolve`, `message=init count=`, `duplicate skill name`). The current model is the round-18 § B in `corpus/knowledge/instruction-surface-census-round13.md`, not these rows. `Instructions from:` still occurs, as the read-hook path, not as the old remote fetcher.
- Sources `:539-541` (17 rows, 17/17, 27/27) is the round-9/10 recording. The live-set errata at `:30-31` governs. Do not read 27/27 as the current check count.
- `~/.omp/agent/agents` exists. The "37 files" count at `:120` is not current. Re-derive; do not adopt a replacement count from this errata.
```

### Append to `corpus/knowledge/harness-verifier-round10.md`

```
(2026-10-14 errata, append-only.) The path marker at the `ports/xbgst-codex` quote stays. It does not cover the counts. Offered-17, keys 17/17, dangling `sekhmet`/`xbrd`, `~/.omp/agent/skills`, `~/.config/opencode/skills`, `~/.bailian/skills`, and `init count` 18 == 17+1 describe the 2026-09-28 host. Those directories are absent or no longer match that census. The omp region sha `55016ef5…` (mtime 2026-09-28) is the binary that section was read from, not the current binary. The 273-byte template sha `c1f03c8e248eb40e…` still matches the live omp binary and stays a current pin. Do not re-pin catalogue counts here; the gate baseline is the live record.
```

### Append to `corpus/knowledge/opencode-extraction-round14.md`

```
(2026-10-14 errata, residual.) The header already makes OC-1…OC-6 / the v1 subsystems historical. One sentence is still a live cross-pin: the falsifier block's claim that `f9dab322…` equals `verifiers/baseline.json` `measured_against.opencode_binary_sha256`. That equality was true of the round-14 baseline. The field has since moved. Do not read `f9dab322…` or dump sha `a7db3095…` as the current binary or the current baseline field. Leave both hashes in the transcript.
```

### Append to `corpus/knowledge/render-mechanism-round7.md`

```
(2026-10-14 errata, append-only.) The `ufo` duplicate-id paths and the `sekhmet`/`xbrd` dangling-symlink sentence describe the 2026-09 host. `~/.omp/agent/skills/ufo/SKILL.md`, `~/.config/opencode/skills/ufo/`, and `~/.agents/skills/{sekhmet,xbrd}` are absent, not dangling. Observation kept. Not a current offer map.
```

### Append to `corpus/knowledge/agents-md-and-dispatch-surfaces.md`

```
(2026-10-14 errata, append-only.) "Sourced 2026-09-28" is the survey date, not an absence marker. The fact table's `~/.config/opencode/skills/`, `/home/vgpnk/projects/shokunin/*/AGENTS.md`, `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md`, and `~/.agents/AGENTS.md` do not resolve. The capital-P shokunin tree is the observed survivor. The "16 skills" and "~60 line" host AGENTS claims are not current. Do not re-pin a replacement count in this note.
```

### Append to `corpus/knowledge/instruction-surface-remeasure-round13.md`

```
(2026-10-14 errata, append-only.) The agreement table is the round-13 witness of the 2026-09-28 opencode binary. It is not the current model. `y[1]`, `n[1]`, `OPENCODE_DISABLE_CLAUDE_CODE`, the AGENTS→CLAUDE→CONTEXT walk, and the remote `https://` instruction fetch are absent from opencode v2.0.26. Current derivation is census § B as rewritten 2026-10-14. This table stays as the witness.
```

### Append to `corpus/knowledge/instruction-surface-census-round13.md`

```
(2026-10-14 errata, residual.) § B's old class ids are already marked historical, and the binary shas in the round-18 block match the binaries they name. Not discharged: exclusion row `omp:unknown/subagent-roster` still says `~/.omp/agent/agents` "(37 files live)". The directory exists; 37 is not the current file count. Re-derive before citing. Do not replace 37 in the row.
```

### Append to `corpus/knowledge/checklist-execution-round15.md` and `checklist-execution-round16.md`

```
(2026-10-14 errata, describe-don't-pin.) Content shas in this note identify the verifier bytes of this round, not HEAD. `verify_skill_checklist.py` and the checklist baseline/vocab files have moved since. Do not delete the printed shas. Do not read them as the current pin. The current checklist-verifier pin, if one is required, is the round-17 recording, re-derived with `sha256sum`, not copied from this errata.
```

### Append to `corpus/README.md`

```
(2026-10-14 errata, append-only.) Index FILE-column paths are unchanged. These Basis summaries are historical and must not be read as the current model: round-8 offer trace keyed on `message=init count=N`; round-10 harness verifier "27 checks" / "17/17"; round-14 "9 instruction classes are now reproduced" by the v1 OC set including `instruction-context`; round-13 census row describing opencode as AGENTS.md→CLAUDE.md→CONTEXT.md plus `~/.claude/CLAUDE.md` and fetched `https://` entries. Current opencode model is census § B after the 2026-10-14 rewrite. Current harness counts live in `verifiers/baseline.json`, not in those Basis cells.
```

### Append to `LOG.md` (parent / record seat only; this seat did not append)

```
## Round 19 — citation re-census residual (append-only; round-18 classification not rewritten)

Round 18's four-site list (`SKILL.md` origin-work path, `LOG.md` round-13 note, `harness-verifier-round10.md` xbgst root, `opencode-extraction-round14.md` v1 rule set) remains marked and is not reopened. It is not a complete census. Unresolved clusters, measured not recalled, are named in `.ufo/waves/shokunin12h-20261014-p1-repair/members/KotobaHistoryClaims.md`: KTB-HC-04, KTB-HC-07, KTB-HC-08, KTB-HC-09, KTB-HC-10, KTB-HC-11, KTB-HC-12, KTB-HC-13, KTB-HC-14, KTB-HC-15, KTB-HC-16. Gate-note residue KTB-HC-17 belongs to GateRepair. No claim was deleted. No superseded sha was re-pinned as current. The live template sha `c1f03c8e…` still matches and is not part of this residual.
```

## Named debt

| id | class | unblock | owner |
|---|---|---|---|
| KTB-HC-04 | unresolved superseded-revision | append the residual equality errata; do not edit the printed sha | parent, corpus note |
| KTB-HC-07 | unresolved live craft claims | append the SKILL errata; do not rewrite `:99-101` in place | parent, `SKILL.md` |
| KTB-HC-08 | unresolved superseded host-state | append the harness-verifier errata; leave the path marker | parent, corpus note |
| KTB-HC-09 | unresolved citation-to-deleted | append lowercase-base errata; describe capital-P tree; do not re-pin 108 or 12 | parent |
| KTB-HC-10 | unresolved citation-to-deleted | append Sources absence list; do not retarget cites | parent, `SKILL.md` |
| KTB-HC-11 | unresolved citation-to-deleted | append render-mechanism errata | parent |
| KTB-HC-12 | unresolved citation-to-deleted | append agents-md errata | parent |
| KTB-HC-13 | unresolved superseded-revision | append README Basis errata; do not rewrite rows | parent |
| KTB-HC-14 | unresolved superseded-revision | append remeasure errata; keep the agreement table | parent |
| KTB-HC-15 | unresolved superseded count | append census/SKILL count errata; re-derive before any new count | parent |
| KTB-HC-16 | unresolved describe-dont-pin | append not-current markers; keep printed shas | parent |
| KTB-HC-17 | unresolved gate-note residue | notes vs expects in `verifiers/baseline.json`; do not fit expects to the notes | KotobaGateRepair |
| KTB-HC-18 | unresolved completeness claim | append a LOG residual; do not rewrite round 18 | parent / record seat |

No code change is proposed. No falsified gate check was reproduced by running a gate, so this seat does not authorize a verifier edit.

## Cross-domain

- KotobaGateRepair: `verifiers/baseline.json` notes at `:126`, `:127`, `:129` (KTB-HC-17). Checks were already re-recorded. Notes were not.
- Sibling lanes: `sibling-description-rewrites-round8.md:444` is a quotation of kumitate's then-description. Not absorbed. Not retargeted.
- Parent integrator: every append above, then the LOG residual, after integration. This seat does not commit.

## Axis reading (not a score, not a judgment)

- Freshness: round-18 markers still match the four paths they name. The standing SKILL craft table, Sources list, harness-verifier counts, and README Basis cells were not brought forward with them.
- Operability: the drafts are append-only and name the surviving path only where existence was measured. No procedure was added that depends on a deleted tree.
- Calibration: current pins that still match (`c1f03c8e…`, `ff59fc1b…`, `d9123b9b…`, `02ccf1b3…`, `a32da4a4…`, `430fe289…`) are left live. Superseded shas are described, not replaced. The moved ufo description length was used only to confirm it is not 690.
- Adjacency: no gate edit, no LOG edit, no corpus edit, no sibling-report write. Gate-note residue is named and left.
