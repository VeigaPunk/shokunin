# KotobaDeadPathSweep

Advisory sweep data. Not a judge verdict, not a receipt, not an admission. No lane file was edited. Gates were not run.

Tree swept: `kotoba-shokunin` working tree at `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` (the named lane-identity commit). `git status --porcelain` → `?? plans/` only. `plans/wwkd-round-19-recensus.md` was included in the walk and has no hit in these families.

## Method

Walked 236 files under `kotoba-shokunin` (skipped `.git`). Tokens matched in file text. Host existence is `test -e` (exit 1 = absent, exit 0 = present), this session, no content read.

Classification, applied per citing line:

- **live** — this lane's own voice uses the path as a current location or a place to open, and no same-paragraph marker says historical, absent, moved, dead, or snapshot-recount.
- **marked-historical** — the same sentence or the immediately following errata says historical, absent, moved, or dead.
- **labelled** — fixture literal, frozen round-N disposition pin, trigger/name token with no filesystem path, or a sibling line quoted as observed text where this lane does not reassert existence.
- **unresolved** — replayable command, result, or existence requirement that would now fail, with no absence marker. Not a standing "open this" instruction, and not discharged.

A source date ("Sourced 2026-09-28", "Audited 2026-09-28") is not an absence marker. `SKILL.md:51-53` ("Cited line numbers are points-in-time. Verify before trusting") is a line-drift rule, not a path-absence mark; it tells the reader to re-read the file.

## Host existence

```
test -e /home/vgpnk/projects                         → exit 1 absent
test -e /home/vgpnk/Projects/origin-work             → exit 1 absent
test -e /home/vgpnk/Projects/webzites                → exit 1 absent
test -e /home/vgpnk/Projects/ds4cc-marketplace       → exit 1 absent
test -e /home/vgpnk/Projects/plazir-15-site          → exit 1 absent
test -e /home/vgpnk/.bailian                         → exit 1 absent
test -e /home/vgpnk/archive                          → exit 1 absent
test -e /home/vgpnk/archive/bench-arena              → exit 1 absent
test -e /home/vgpnk/bench-arena                      → exit 1 absent
test -e /home/vgpnk/.config/the-janitor              → exit 1 absent
test -e /home/vgpnk/.config/the-janitor/op.env       → exit 1 absent
test -e /home/vgpnk/Projects/shokunin                → exit 0 present
test -e /home/vgpnk/Projects/ufo-fsd-alpha           → exit 0 present
command -v the-janitor                               → exit 1 (not on PATH)
```

`git -C kotoba-shokunin rev-parse HEAD` → exit 0, `b0c7cb2e248bccf692cf10e4d3c394e09944e83d`.

Survivor relevant to the lowercase cites: `/home/vgpnk/Projects/shokunin` (including `kagi-shokunin`, `kake-shokunin`, `kasegi-shokunin`, `kengaku-shokunin`, `kumitate-shokunin`, `.ufo/prompts/`, `MISSION.md`). Counts under that tree were not re-pinned.

## Lane-record comparison

| Lane sentence | Match? | Counterexample |
|---|---|---|
| `LOG.md:908-914` — citations to upstream-deleted/moved files were **4**, all marked, and origin-work was the only path-class defect | mismatch as a completeness claim | 17 live lines below are outside those 4 sites. The 4 named sites that are path citations are still marked (next row). |
| `LOG.md:908-910` / `SKILL.md:35-38` / `LOG.md:469-471` / `harness-verifier-round10.md:112-114` — the origin-work ufo path, the LOG round-13 note, and the `ports/xbgst-codex` symlink root are historical | match for those three path sites | The fourth named site (`opencode-extraction-round14.md` v1 rule set) is not a hit in these eight families. This sweep does not re-judge that banner. The harness-verifier errata names the origin-work path only; it does not cover `~/.bailian/skills` on the preceding sentence (`:105`). |
| `SCORECARD.md:82` — "4 dead-path citations marked historical" | match for the marked four; mismatch if read as the population | Same 17 live lines. |
| `corpus/lessons/round-19-recensus.md:31` — lowercase `/home/vgpnk/projects/...` cites remain | match on the class | Does not name the 14 live lowercase lines, does not name owner/unblock, and does not mention webzites, `~/.bailian`, or the janitor config path. |
| `LOG.md:863-867` and `checklist-execution-round17.md:263-268` — report pointers were case-corrected off the absent lowercase base | match for that class, from the text | The repair's own words limit it to `.ufo/reports` pointers. It does not discharge SKILL or the other corpus cites. |
| Round-19 lesson / scorecard do not claim zero live citations | match | The acceptance bar (zero live, or each named with owner/unblock) is not met by the record. This file names them. |

## Live — 17 lines

These are operative. A reader following the sentence opens a path `test -e` reports absent. No same-file errata discharges them.

### Lowercase `/home/vgpnk/projects` — 14 lines

Survivor is `/home/vgpnk/Projects/shokunin` (exit 0). Do not re-pin file counts while marking these.

| cite | what the sentence does |
|---|---|
| `SKILL.md:88` | "no harness loads `/home/vgpnk/projects/shokunin/.ufo/prompts/`" — names that path as the dispatch-prompt location |
| `SKILL.md:97` | same claim, surface table, spawn row |
| `SKILL.md:106` | hash claim over `/home/vgpnk/projects/shokunin/*/AGENTS.md`, "re-verified round 7" |
| `SKILL.md:144` | anatomy "from `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md`" |
| `SKILL.md:153` | diff "both under `/home/vgpnk/projects/shokunin/.ufo/prompts/`" |
| `SKILL.md:386` | "observed form: `/home/vgpnk/projects/shokunin/.ufo/prompts/`. Checkable by reading the file" |
| `SKILL.md:482` | Sources: `/home/vgpnk/projects/shokunin/*/AGENTS.md` (6 files) |
| `SKILL.md:484` | Sources: `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md` |
| `SKILL.md:486` | Sources: `/home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md` |
| `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10` | fact table, present tense, lowercase AGENTS glob |
| `corpus/knowledge/agents-md-and-dispatch-surfaces.md:11` | fact table, present tense, lowercase `*-L1.md` glob |
| `corpus/knowledge/checklist-execution-round15.md:78` | heading: floor is `/home/vgpnk/projects/shokunin/MISSION.md`. Same file `:70` uses the capital-P report path |
| `corpus/knowledge/checklist-execution-round16.md:88` | "three sites now read `/home/vgpnk/projects/shokunin/.ufo/prompts/`" as the landed named base. Those SKILL sites still contain that string (`:88`, `:97`, `:386`) |
| `corpus/knowledge/sibling-description-rewrites-round8.md:5` | five sibling `SKILL.md` files "all under `/home/vgpnk/projects/shokunin/`". The five directories exist under capital-P |

Owner: kotoba parent / record seat. Unblock: append-only mark that the lowercase base is absent and the observed tree is `/home/vgpnk/Projects/shokunin`. Do not rewrite the sentences. Do not copy a new file count into them. Not a verifier edit: absolute paths are outside `trigger.citation_resolves` (`verifiers/verify_skill_checklist.py:164-169` admits only `corpus/`, `verifiers/`, `opencode/`, `.ufo/`, `../`, and drops `~` and leading `/`).

### webzites path — 1 line

| cite | what the sentence does |
|---|---|
| `corpus/knowledge/fleet-skill-audit-round5.md:59` | own voice: "bin lives at `~/Projects/webzites/bin/webzites.mjs`". Header date 2026-09-28 only. Same line also has two bare `webzites` command-name tokens |

`test -e ~/Projects/webzites` → exit 1. Owner of the citation: kotoba parent (append that the path is absent; do not re-pin kake L46/L161). Owner of the tree: operator. kake owns the domain if the tree returns.

### `~/.bailian` — 2 lines

| cite | what the sentence does |
|---|---|
| `corpus/knowledge/harness-verifier-round10.md:105` | "`~/.config/opencode/skills` and `~/.claude/skills` are symlink trees into `~/.bailian/skills`". The 2026-10-14 errata at `:112-114` says "that path" about the fenced origin-work symlink root, not this sentence |
| `corpus/knowledge/sibling-description-rewrites-round8.md:377` | quotes kengaku L303 `~/.bailian/skills/bailian-docs-llm-wiki/models/index.md`, then this lane's gloss "(Bailian model data lives there)" |

`test -e ~/.bailian` → exit 1. Owner: kotoba parent. Unblock: append that `~/.bailian` is absent and that the origin-work marker does not cover `:105` or the `:377` gloss. Do not rewrite the round-10 census or the quoted cell. Restoration: operator.

## Unresolved — 11 lines

Not standing craft instructions. Not marked absent. Re-running the command, or treating the quoted requirement as current, hits an absent path.

| cite | family | why unresolved |
|---|---|---|
| `corpus/knowledge/checklist-execution-round15.md:186` | lowercase `~/projects` | recorded `find -L ~/projects ~/Projects …` → 123. Operand, not an open-this pointer. No absence mark. Re-run would not see the lowercase root |
| `corpus/knowledge/claim-census-round12.md:40` | `/home/vgpnk/projects` | census row, command `test -f /home/vgpnk/projects/shokunin/.ufo/reports/round-$n/kotoba.md`, result `OK ×9`, verdict AGREES. Header says rows keep that round's values. No absence mark on this path |
| `corpus/knowledge/claim-census-round12.md:80` | `/home/vgpnk/projects` | census row, `for f in /home/vgpnk/projects/shokunin/*-shokunin/SKILL.md`, verdict AGREES |
| `corpus/knowledge/cold-run-round11.md:58` | `/home/vgpnk/projects` | fenced cold-run command; three occurrences of the lowercase repo path on one line. Reachability qualifier at `:19-28` covers content shas, not this path |
| `corpus/knowledge/cold-run-round11.md:59` | `/home/vgpnk/projects` | command output echoing that path |
| `corpus/knowledge/cold-run-round11.md:200` | `/home/vgpnk/projects` | reproduction snippet `R = "/home/vgpnk/projects/shokunin/kotoba-shokunin"` |
| `corpus/knowledge/corpus-integrity-round11.md:110` | `/home/vgpnk/projects` and `~/projects` | fenced `git grep` comment; two tokens on one line. Prose at `:122` (no path token) still says the host-absolute and tilde forms were "all resolving" |
| `corpus/knowledge/corpus-integrity-round11.md:131` | `/home/vgpnk/projects` | fenced `test -f` loop, comment `# → OK ×9` |
| `corpus/lessons/round-10.md:95` | `/home/vgpnk/projects` | evidence cell `ls /home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md \| wc -l` → 53 |
| `verifiers/baseline.json:126` | `~/Projects/origin-work` | current notes field: "round 13: a ufo copy under `~/Projects/origin-work/ufo-fsd-alpha`". Dated example, not an open-this instruction. SKILL/LOG errata are other files and do not mark this note. `evaluate()` does not read `notes` |
| `corpus/knowledge/sibling-description-rewrites-round8.md:151` | `~/.config/the-janitor/op.env` | Observed-text cell quoting kagi L28 "needs `~/.config/the-janitor/op.env` present". This lane does not reassert it. The quoted requirement is an existence claim, the directory is absent (exit 1), and this file has no absence mark |

Owner for the nine transcript lines plus the baseline note: kotoba parent. Unblock: append "do not replay; path absent" on each file. Do not delete the printed commands or the AGREES cells. Do not re-pin 53, 123, or OK ×9. Do not change `baseline.json` check expects to fit the note.

Owner for the janitor quote: kotoba parent for the mark; operator or kagi if `~/.config/the-janitor` is restored. Do not rewrite the observed-text cell.

## Marked-historical — 9 lines

Discharged for the path they name. Listed so a later reader does not re-open them.

| cite | family | marker |
|---|---|---|
| `LOG.md:864` | `/home/vgpnk/projects` | "absent lowercase"; scope is the report-pointer repair, not the live SKILL cites |
| `corpus/knowledge/checklist-execution-round17.md:263` | `/home/vgpnk/projects/.../.ufo/reports` | "Every dead pointer used" that base |
| `corpus/knowledge/checklist-execution-round17.md:264` | `/home/vgpnk/projects` | "is absent on this host" |
| `verifiers/corpus-baseline.json:10` | `/home/vgpnk/projects` | "now-absent"; same report-pointer scope |
| `SKILL.md:35` | `~/Projects/origin-work/ufo-fsd-alpha/skills/ufo/SKILL.md` | same sentence: "2026-10-14 errata: historical path; the tree moved" |
| `LOG.md:469` | same origin-work ufo path | same-sentence 2026-10-14 errata |
| `LOG.md:894` | `~/Projects/origin-work/ufo-fsd-alpha` | relocation arrow to `~/Projects/ufo-fsd-alpha` |
| `LOG.md:909` | origin-work | "dead origin-work path" |
| `corpus/knowledge/harness-verifier-round10.md:109` | `~/Projects/origin-work/.../ports/xbgst-codex/skills` | next paragraph `:112-114`: "that path is historical" |

`LOG.md:906` ("The origin-work citations were the only path-class defect") is a class-name, not a path pointer. Classified labelled below. The completeness claim is the mismatch in the record table, not a live path cite.

## Labelled — not operative pointers

### Lowercase, fixture or debt label or frozen pin — 18 lines

| cite | why labelled |
|---|---|
| `corpus/lessons/round-19-recensus.md:31` | debt label: "cites remain". Does not tell the reader to open the path. Does not discharge the 14 live lines |
| `verifiers/checklist-baseline.json:208` | `alwayson.01` disposition, "at round 15 … under ~/projects". Frozen pin text, not a path the checklist resolves |
| `verifiers/checklist-baseline.json:214` | `alwayson.02`, same disposition string |
| `verifiers/checklist-baseline.json:220` | `alwayson.03`, same |
| `verifiers/checklist-baseline.json:226` | `alwayson.04`, same |
| `verifiers/checklist-baseline.json:232` | `alwayson.05`, same |
| `verifiers/checklist-baseline.json:238` | `alwayson.06`, same |
| `verifiers/checklist-baseline.json:244` | `alwayson.07`, same |
| `verifiers/checklist-baseline.json:250` | `alwayson.08`, same |
| `verifiers/verify_corpus_integrity.py:624` | `FIXTURE_POINTER_SHAPES` hosted example |
| `verifiers/verify_corpus_integrity.py:625` | fixture tilde example |
| `verifiers/verify_corpus_integrity.py:770` | self-test input string |
| `verifiers/verify_corpus_integrity.py:771` | self-test expected string |
| `verifiers/verify_corpus_integrity.py:775` | self-test input string |
| `verifiers/verify_corpus_integrity.py:776` | self-test expected string |
| `verifiers/verify_corpus_integrity.py:797` | `pointer_shape` fixture |
| `verifiers/verify_corpus_integrity.py:806` | expected site string inside `self_test` |
| `verifiers/verify_corpus_integrity.py:807` | expected site string inside `self_test` |

The fixture strings are not a live resolver default. `self_test` says a failure means the script or the fixture is wrong, never that the host is wrong (`verify_corpus_integrity.py:630-634`).

### origin-work, non-pointer — 2 lines

| cite | why labelled |
|---|---|
| `LOG.md:906` | class-name "origin-work citations", not a path. Completeness claim is separately a record mismatch |
| `corpus/knowledge/sibling-description-rewrites-round8.md:444` | observed-text quote of kumitate L9 `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`. This lane uses it as evidence of an ownership split, not as a path to open |

### webzites — 15 path lines labelled, plus 6 bare-name lines

Path lines that are snapshot pins or quoted sibling text, not this lane saying "go here" or "lives at":

| cite | why labelled |
|---|---|
| `corpus/knowledge/claude-md-surface.md:27` | `~/Projects/webzites/repos/llm-wiki/CLAUDE.md` inside the inventory table. `:20-23` labels that table "the round-6 snapshot; recount before citing" |
| `corpus/knowledge/sibling-description-rewrites-round8.md:222` | observed text of kake L30/L46; two path tokens (`fleet/fleet.config.json`, `bin/webzites.mjs`) |
| `corpus/knowledge/sibling-description-rewrites-round8.md:247` | quote of the sibling's new command `node ~/Projects/webzites/bin/webzites.mjs` |
| `corpus/knowledge/sibling-description-rewrites-round8.md:337` | quoted kengaku description containing `~/Projects/webzites/repos/llm-wiki` |
| `corpus/knowledge/sibling-description-rewrites-round8.md:366` | observed text, same llm-wiki path |
| `corpus/knowledge/sibling-description-rewrites-round8.md:387` | truncator analysis of that quoted string; not offered as a current location |
| `verifiers/checklist-baseline.json:100` | `agentdef.01` disposition, "at round 15 … snapshot under ~/Projects/webzites/.../state" |
| `verifiers/checklist-baseline.json:106` | `agentdef.02`, same |
| `verifiers/checklist-baseline.json:112` | `agentdef.03`, same |
| `verifiers/checklist-baseline.json:118` | `agentdef.04`, same |
| `verifiers/checklist-baseline.json:124` | `agentdef.05`, same |
| `verifiers/checklist-baseline.json:130` | `agentdef.06`, same |
| `verifiers/checklist-baseline.json:136` | `agentdef.07`, same |
| `verifiers/checklist-baseline.json:142` | `agentdef.08`, same |
| `verifiers/checklist-baseline.json:148` | `agentdef.09`, same |

Bare `webzites` with no filesystem path (name or smell token only):

| cite | why labelled |
|---|---|
| `corpus/knowledge/fail-closed-and-anti-patterns.md:82` | anti-pattern example "kake: `webzites` on no PATH". No directory path |
| `corpus/knowledge/sibling-description-rewrites-round8.md:198` | proposed description noun |
| `corpus/knowledge/sibling-description-rewrites-round8.md:200` | trigger string `"webzites"` |
| `corpus/knowledge/sibling-description-rewrites-round8.md:214` | sentence-1 render analysis |
| `corpus/knowledge/sibling-description-rewrites-round8.md:243` | proposed render line |
| `corpus/knowledge/sibling-description-rewrites-round8.md:246` | noun in a render comparison |

`fleet-skill-audit-round5.md:59` is not in this table; it is live.

### bench-arena — named family has 0 path hits

`~/archive/bench-arena` and `/home/vgpnk/archive/bench-arena`: **0 hits**.

Related, not that spelling:

| cite | class | note |
|---|---|---|
| `corpus/knowledge/sibling-description-rewrites-round8.md:353` | labelled | name token "bench-arena batteries". No path |
| `corpus/knowledge/sibling-description-rewrites-round8.md:365` | labelled | observed text quoting kengaku L150 `~/bench-arena/telemetry-qwenlocal-v2.csv`. Predecessor path, also absent (`test -e ~/bench-arena` exit 1). This lane does not reassert it |

### the-janitor command names — not host paths

18 lines contain the string `the-janitor`. Only `sibling-description-rewrites-round8.md:151` is a filesystem path (unresolved, above). The other 17 are command or trigger mentions, excluded from the path census:

`SKILL.md:109`, `SKILL.md:359`, `corpus/knowledge/agent-def-audit-round6.md:51`, `corpus/knowledge/agents-md-and-dispatch-surfaces.md:43`, `corpus/knowledge/alwayson-checklist-round7.md:30`, `corpus/knowledge/sibling-description-rewrites-round8.md:119`, `:126`, `:127`, `:141`, `:146`, `:147`, `:154`, `:160`, `:169`, `:171`, `:174`, `:180`.

`command -v the-janitor` → exit 1. That is a binary absence, not a host-path hit. `SKILL.md:359` ("only `the-janitor` is a real `the-` binary on this host") is current-tense about a binary and is outside this sweep's path families. Not classified here.

## Zero-hit families

| family | hits |
|---|---|
| `ds4cc-marketplace` | 0 |
| `plazir-15-site` / `plazir15` | 0 |
| `~/archive/bench-arena` | 0 |

`ds4cc.com` and `ds4cc` appear in `sibling-description-rewrites-round8.md` as hostnames and trigger strings (`:191`, `:198`, `:199`, `:214`, `:219`, `:220`, `:230`, `:241`, `:243`, `:246`, `:253`). Those are not the deleted repo path. Not hits.

No hit in `PROVINCE.md`, `SHONEN.md`, `AGENTS.md`, `SCORECARD.md`, or `plans/`.

`LOG.md:872` says the fault harness's `plant_f` anchor "carried the same lowercase host base" and was corrected. No path token on that line. Not a hit. `verifiers/fault_injection_corpus.sh` has no lowercase `/home/vgpnk/projects` token.

## Why a green corpus gate would not see the live set

Source, not a run. `verify_corpus_integrity.py:16-21` and `:35-37` check `.ufo/reports/round-N/*.md` pointers inside tracked `corpus/*.md` only. The live lowercase cites are globs under `.ufo/prompts` and `AGENTS.md`, a `MISSION.md` heading, and a sibling-repo base. They are outside that class. `SKILL.md` is not scanned by that verifier (`:65-66`).

`verify_skill_checklist.py:164-169` drops absolute and `~` citations. `governance.citation_resolves` (`:179-185`) reads `LOG.md` and `SCORECARD.md` only, and only repo-root tokens. `LOG.md:864` is marked absent and is not a `corpus/` or `.ufo/` subject anyway.

A later green `verify_corpus_integrity.py` does not contradict the 17 live lines.

## Named debt

| id | class | sites | owner | unblock |
|---|---|---|---|---|
| KTB-DP-LIVE-CASE | live | 14 lowercase lines in the live table | kotoba parent | append absence; describe capital-P tree; do not re-pin counts; do not edit the verifier to swallow absolute paths |
| KTB-DP-LIVE-WEBZITES | live | `fleet-skill-audit-round5.md:59` | kotoba parent for the mark; operator for the tree | append that `~/Projects/webzites` is absent; do not re-pin kake line numbers |
| KTB-DP-LIVE-BAILIAN | live | `harness-verifier-round10.md:105`, `sibling-description-rewrites-round8.md:377` | kotoba parent; operator if the tree returns | append that `~/.bailian` is absent; the `:112-114` marker does not cover these |
| KTB-DP-UNRES-TRANSCRIPT | unresolved | 9 transcript lines (round15:186, census:40 and :80, cold-run:58, :59, :200, corpus-integrity:110 and :131, round-10:95) | kotoba parent | append do-not-replay; keep the printed commands |
| KTB-DP-UNRES-BASELINE-NOTE | unresolved | `verifiers/baseline.json:126` | kotoba parent | append that the round-13 origin-work example is absent; do not move check expects |
| KTB-DP-UNRES-JANITOR | unresolved | `sibling-description-rewrites-round8.md:151` | kotoba parent for the mark; operator or kagi for the directory | append that `~/.config/the-janitor` is absent; leave the observed-text cell |
| KTB-DP-RECORD | record mismatch | `LOG.md:906-914`, `SCORECARD.md:82` | kotoba parent / record seat | append that the four-site list is not the population. Do not rewrite round 18. Round-19 lesson already names the lowercase class and still omits webzites, bailian, and the janitor path |

Not debt: the 9 marked-historical lines, the fixture and disposition pins, the zero-hit families, and the quoted sibling strings that this lane does not reassert.
