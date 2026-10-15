# KotobaHistoricalMarking — advisory

Advisory data only. Not a native judge verdict, not a lane round report, not a receipt, and not an admission. No lane file was edited by this seat. No gate was run. Session JSONL, logs, credentials, oauth, and `server.token` were not content-read.

Audit subject is the landed commit `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` (`kotoba-shokunin <kotoba@shokunin.local>`, 2026-10-14 21:15:36 -0300). Round 19's committed delta is `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-19-recensus.md`, and a two-line comparator change in `verifiers/verify_harness_claims.py`. It did not append the historical-marking errata the repair inventory drafted.

Measurement caveat: at first status the worktree was `?? plans/` only. Before this report was written, uncommitted hunks appeared in `LOG.md`, `corpus/README.md`, `corpus/lessons/round-19-recensus.md`, and `verifiers/corpus-baseline.json` (path-prefix fixes, a round-19 index row, baseline-note deletion). Those hunks are not this seat's and are not the landed record. Cited lines below are in `b0c7cb2e`. The README insert is after line 51, so lines 31–39 are unchanged. The LOG and lesson hunks do not touch the lines cited here.

## Rule applied

Describe-don't-pin: a superseded revision is described, not pinned as current identity. A content hash of a missing file must not be asserted as that file's current identity. A dated round transcript may keep a printed sha if the same file says the sha is not current. A source date, a round heading, or a path-only errata does not discharge a later present-tense count, equality, or "value today".

Replacement counts measured below are falsifiers. They are not new pins. Do not write 7, 13, 14, 108, 116, 260, or 605 back into the original sentences.

## Claim-by-claim against the lane record

| Lane claim | Verdict | Why |
|---|---|---|
| Lesson: landed change is one file, 2 lines (`verify_harness_claims.py` `at_least` → `equal` on `oc.permission.skill_lines` and `oc.permission.skill_allow`; `expect` stays 0) | agree | `CHECKS` at `verifiers/verify_harness_claims.py:549-550` is `("equal", …)` for both ids. `git show --stat b0c7cb2e` is 2 deletions / 2 insertions in that file, plus the record files. |
| Lesson: baseline JSON `"mode": "at_least"` is documentary, unread by `evaluate()`, recorded rather than edited | agree | `verifiers/baseline.json:110` and `:114` still say `"mode": "at_least"` with `"expect": 0`. The lesson marks that string stale. Not an unmarked current claim. |
| Lesson: `SKILL.md` still teaches the v1 opencode model | agree | Present tense at `SKILL.md:99-101` and `:509-511`. Live `opencode` binary anchor counts for those literals are 0 (command below). |
| Lesson: lowercase `/home/vgpnk/projects/...` cites remain | agree | Still the cited base at `SKILL.md:97`, `:106`, `:144`, `:386`. `test -e /home/vgpnk/projects` is false. |
| Lesson: harness-verifier count prose is stale | agree, incomplete | True of `SKILL.md:539-547`, `corpus/README.md:34`, and `corpus/knowledge/harness-verifier-round10.md:93-130`. The lesson does not name the other clusters below. |
| Lesson: `verify_skill_checklist.py` exit 1 on 601 lines over budget 600 is pre-existing carried debt | not re-executed | `wc -l SKILL.md` at HEAD is 601. This seat did not run the checklist. The line count is observed; the exit code is the lesson's, not this seat's. |
| `LOG.md:908-916`: citations to upstream-deleted/moved files were 4, all marked, genuine lane defects 0 | disagree as a completeness claim | The four named markers are present (agree, next row). The sentence is false as a census of still-current claims. Round 19 did not append a residual. |
| Round-18 markers at `SKILL.md:35-38`, `LOG.md:469-471`, `harness-verifier-round10.md:112-114`, `opencode-extraction-round14.md:3-12` | agree the markers exist | Path facts still hold: `~/Projects/origin-work` absent, `ports/xbgst-codex` absent, moved ufo skill exists and its folded `description` is 605 chars, not 690. The 690-char length is described, not re-pinned. The path marker does not discharge the counts around it. The extraction header does not discharge `:96-97`. |
| `LOG.md:952-953`: checklist unchanged, exit 0, 552 lines | disagree | `git show 02302c521b933c55fc4be79193e61537e3380751:SKILL.md \| wc -l` and `git show HEAD:SKILL.md \| wc -l` are both 601. The 552-line claim was already false of the commit that contains it. Round 19 records the 601 overrun and does not mark 552 as a bad measurement. |
| `LOG.md:960-961`: extraction doc's live claims are discharged by errata | disagree for one sentence | Header `:3-12` marks the v1 rule set historical. `:96-97` still equates superseded sha `f9dab322…` to the live baseline field. |
| Census round-18 block `:22-23` pins `ff59fc1b…` / `d9123b9b…` as the re-derivation binaries | agree | Both match `sha256sum` of the live binaries. Those two full shas are current pins. |
| Census `:164-175` old class ids are historical, not live classes | agree for those ids | Does not discharge `:53-56` or `:222`. |
| `cold-run-round11.md:383` `a32da4a4…` is the current content hash of `verify_corpus_integrity.py` | agree | Live sha256 is `a32da4a4224e9810549016ec3000583f3068bf552d7a92b0666114c32476dd56`. |
| `independent-verification-round12.md:16` pins `a32da4a4…` and `430fe289…` | agree | Both match the live files. The fault-script pin on `:120` of the same file does not. |
| `checklist-execution-round17.md:221` and `:245` pin `02ccf1b3…` | agree | Live sha256 of `verifiers/verify_skill_checklist.py` is `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27`. |
| `cold-run-round11.md:19-28` and `claim-census-round12.md`: `631569277d…` / `2f07179c…` are unrecoverable and not current | agree | Marked. Not a current-identity assertion after the qualifier. `git cat-file -t 3b029b8` is `commit`; that is a different pin (below) and still resolves. |
| `claim-scope-audit-round9.md:15` md5 `143fe473…` of `SKILL.md` at commit `3b029b8` | agree | `git show 3b029b8:SKILL.md \| md5sum` is `143fe473368ec9e2bb7adde9d0425b1c`, 487 lines. Labeled md5, not a commit id. Historical pin of a blob that still exists. |

Round 19 did not introduce a new current pin of a superseded sha. The code delta is a comparator mode only.

## Missing-file content hash

No content hash of a deleted path is asserted as that path's current identity.

Checked and not a violation:

- `~/Projects/origin-work/ufo-fsd-alpha/skills/ufo/SKILL.md` is absent. `SKILL.md:35-38` and `LOG.md:469-471` describe the 690-char description and say it is not re-pinned. No sha of that missing file is offered as current identity.
- `ports/xbgst-codex` is absent. The marker at `harness-verifier-round10.md:112-114` keeps the observation as then-true. No content hash of that tree is offered as current identity.
- `/home/vgpnk/projects` is absent. The lowercase cites are paths and counts, not content hashes of the missing tree.
- `631569277d112e8effab3428ca89af53cbcf09f85ad5dad714827deefa2eb4aa` and `2f07179c07d19f96da822cea2d9cc945184ac94132cbcd05d9cd75169fc0f510` are content hashes of bytes that were never committed. `cold-run-round11.md:19-28` says they are not recoverable and not independently checkable today. `claim-census-round12.md:60` and `:68` label the matching claims FALSE at HEAD / the identity gate does not hold. Marked.

The hard rule holds for missing paths. It does not hold for superseded hashes of files that still exist, or for one unrecoverable hash asserted as the identity of a path that exists. Those are the counterexamples in the next section.

## Counterexamples

### Superseded content hash asserted as current identity

1. `corpus/knowledge/opencode-extraction-round14.md:96-97` — `f9dab32248695e9ebd56b16a1921798fd85112cf5a69c7dfd0cabc1e17be4a11` is "equal to `verifiers/baseline.json` `measured_against.opencode_binary_sha256`". Live field `verifiers/baseline.json:7` and live binary are `d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9`. Header `:3-12` marks the rule set historical. It does not strike this equality. `:99` dump sha `a7db30951351f16b821822e07c19cd55cb6ba300f6640f64dbb5b4c10eb7ac59` is inside the same historical body; the live cross-pin is the equality, not the dump line alone.

2. `corpus/knowledge/instruction-surface-census-round13.md:53-56` — binaries dated 2026-09-28, sha `55016ef5317af556…` and `f9dab32248695e9e…`, "identical to the binary hashes `verifiers/baseline.json` records". The date marks the binaries. The equality is present tense and false. Round-18 errata `:10-23` names the new shas and does not strike this sentence.

3. `corpus/knowledge/independent-verification-round12.md:120` — `verifiers/fault_injection_corpus.sh` sha256 `9bc80ae61cea…` in present-tense identity. Neither committed blob matches: round-12 `633859fb24b0` is `7026e73687692f98…`; HEAD `fad752b5c710` is `9db6c692c752f0fdeb912f1d77e0049312e97b66422bd1a7e10a63c519bb5d34`. `:124` says the row pins the sha of the script copy executed. That copy is not in git. No not-current marker. This is an unrecoverable content hash asserted as the identity of a path that exists, not a hash of a deleted path.

4. `corpus/knowledge/checklist-execution-round15.md:212-214` — artifact table pins `verify_skill_checklist.py` `f169f2479ca4a76df5eca4f900a77369ece3ed8a3521832a4edf01ef4f98272e`, `checklist-baseline.json` `6bccc6b2de9edaebb87031beb6138963c9f10720fde817fd6a0da32a6e9b7c26`, `checklist-command-vocabulary.json` `200f38dd0fdc27867e9dbdc29d96afb1847b41c0dff8fff542c622b47ccbf9cc`. Live shas are `02ccf1b3…`, `68831bb35f28f8dd19b41d36f6d8529768cccaa05275e22e52ff6487f641385e`, `76d16a9cb53e43db25ec4549465fd00bf1f11551384350c7761328a935eeb02b`. No not-current marker. `corpus/README.md:42` indexes this note as the description of the live verifier.

5. `corpus/knowledge/checklist-execution-round16.md:119-120` — pasted `sha256sum` of `verify_skill_checklist.py` is `70f8b38e9386ab1ee808c57aee29586887bad4320b899c954da1660ac020a8e4`. Live sha is `02ccf1b3…`. Round transcript, unmarked as not current.

6. `corpus/knowledge/harness-verifier-round10.md:34` — `omp` sha256 `55016ef5…`, mtime 2026-09-28 15:14, as the region the section is read from. Live omp is `ff59fc1b…`. The date is in the sentence. It does not say the hash is not the current binary, and the counts that follow are present tense (`:93` "on this host", `:124` "Value today").

### Counts and line numbers presented as current

Present tense, no same-file errata that covers the sentence. Measured falsifiers are not replacement pins.

| path:line | claim as written | measured | command |
|---|---|---|---|
| `SKILL.md:71-72` | godspeed is 18 lines; deferral "Read `directive.md` … apply verbatim" | host `~/.agents/skills/godspeed/SKILL.md` is 17 lines, `apply verbatim` 0, no `directive.md`. Source `~/Projects/ufo-fsd-alpha/skills/godspeed/SKILL.md` is 28 lines, `apply verbatim` 0, deferral is a different sentence | `wc` / count in the python measurement |
| `SKILL.md:98` | ~72 round files under the shokunin tree | 108 `*-round-*.md` under `/home/vgpnk/Projects/shokunin/.ufo/prompts`. Lowercase base absent. Do not adopt 108 | glob count |
| `SKILL.md:99-101` | opencode reads `CLAUDE.md` via `y[1]` and `~/.claude/CLAUDE.md` via `n[1]`, gated by `OPENCODE_DISABLE_CLAUDE_CODE`; priority list includes `CONTEXT.md`; `instructions: []` fetches `https://` | binary counts: `CONTEXT.md` 0, `OPENCODE_DISABLE_CLAUDE_CODE` 0, `Instruction.resolve` 0, `disableClaudeCodePrompt` 0. `~/.claude/CLAUDE.md` absent. `Instructions from:` is 3 and is the v2 read-hook, not this fetcher | byte count of `~/.opencode/bin/opencode` |
| `SKILL.md:103-107` | six child `AGENTS.md`; host `~/.agents/AGENTS.md` is 75 lines; line pins `:18` and `:55` | lowercase base absent. Host `~/.agents/AGENTS.md` absent, so the 75-line count and the `:18`/`:55` pins are of a missing file. Capital-P `*-shokunin/AGENTS.md` count is 14, not 6. Do not adopt 14 | `test -e`; glob list |
| `SKILL.md:109` | `~/.agents/godspeed-core/directive.md` at `:18` of the host AGENTS file | both paths absent | `test -e` |
| `SKILL.md:120` | `~/.omp/agent/agents/*.md` → 37 files | directory exists; `*.md` count is 13 | glob |
| `SKILL.md:137` | 3 files under `~/.config/opencode/command/` | directory absent | `test -e` |
| `SKILL.md:509-511` | `message=init count=N`, latest 18; `duplicate skill name` warns | both literals occur 0 times in the live opencode binary. `skills rescanned` occurs 2 | byte count |
| `SKILL.md:512-518` | upstream `packages/opencode/src/skill/index.ts:321-343`, `:105-139`, `:235-246`, `session/system.ts:107-119`, `dialog-skill.tsx:41` | no `packages/opencode/src/skill/index.ts` under `/home/vgpnk` at depth ≤4, and none under `Projects/**`. Unlocated line pins presented as current sources. Not proven deleted below depth 4. No absence marker | `find`, exit 0, empty |
| `SKILL.md:519` | `~/.omp/agent/sessions/**/*.jsonl` (5842 files) | name-count of `*.jsonl` under that directory is 260. Contents not read | `find -printf`, exit 0 |
| `SKILL.md:539-547` | 17 rows, 17/17, 27/27 checks; this file is the authority for every harness number in it | `CHECKS` has 28 keys, including `oc.log.skills_rescan_max`. Opening errata `:30-31` (live set is 7) does not cover this section. `:133-135` discharges the 18/14/11 agent-def counts only | key count of `CHECKS` |
| `corpus/knowledge/instruction-surface-census-round13.md:222` | `~/.omp/agent/agents` "(37 files live)" in the live exclusion table | 13 `*.md`. Errata says § A stays live and does not discharge this count | glob |
| `corpus/knowledge/instruction-surface-census-round13.md:232` | `.ufo/prompts/*.md` (197 files) | the only such directory measured is `/home/vgpnk/Projects/shokunin/.ufo/prompts`, 116 `*.md`. Lowercase base absent. Do not adopt 116 | glob |
| `corpus/knowledge/harness-verifier-round10.md:93-97` | offered 17, keys 17/17, over-cliff 17/17, "on this host" | `~/.agents/skills` has 7 directories: godspeed, omarchy, reverse-engineer-anything, shokunin, swarm, tower, ufo. No sekhmet, xbrd, wwkd, bailian. Baseline `omp.offered.skills` and `omp.cache.keys_reproduced` expect 7 | `iterdir`; `baseline.json:29`, `:37` |
| `corpus/knowledge/harness-verifier-round10.md:101-108` and `:116-118` | `~/.agents/skills` 15 live + 2 dangling sekhmet/xbrd; `~/.omp/agent/skills` adds skills; opencode/claude skills are symlink trees into `~/.bailian/skills`; dangling baseline = 2; 17 names vs 19 directories | `~/.omp/agent/skills` absent. `~/.config/opencode/skills` absent. `~/.bailian` absent. sekhmet/xbrd absent, not dangling. Baseline `omp.offered.dangling` expect 0 (`:33`). Path errata `:112-114` does not cover these counts | `test -e` |
| `corpus/knowledge/harness-verifier-round10.md:124-130` | "Value today": `init count` 18 == 17+1; permission lines 471/471 | baseline `oc.log.init_count_max` expect 0 (`:81`); `oc.log.skills_rescan_max` expect 3 (`:121`). Binary literals `message=init count=` and `duplicate skill name` are 0. Log bytes were not read, so 471 was not re-counted in the log | baseline read; binary byte count |
| `corpus/knowledge/agents-md-and-dispatch-surfaces.md:9-11` and `:26` | "Fact": 16 skills under `~/.agents/skills/` plus opencode skills; lowercase AGENTS glob; `~/.agents/AGENTS.md` ~60 lines | 7 skill dirs; opencode skills dir absent; lowercase glob absent; host AGENTS.md absent. `:3` "Sourced 2026-09-28" is a survey date, not an absence marker | `test -e`; `iterdir` |
| `corpus/knowledge/render-mechanism-round7.md:64-67` | `~/.omp/agent/skills/ufo/SKILL.md` wins over `~/.config/opencode/skills/ufo/`; `~/.agents/skills/{sekhmet,xbrd}` are dangling symlinks | all four paths absent. Directories are gone, not dangling. No errata | `test -e` |
| `corpus/knowledge/instruction-surface-remeasure-round13.md:23-25` | agreement table: opencode loads `CLAUDE.md` via `y[1]`/`n[1]`, walks AGENTS→CLAUDE→CONTEXT, fetches `https://` instructions | those anchors are 0 in opencode v2.0.26. No 2026-10-14 marker. Census § B contradicts the table. The table is a round-13 witness left readable as the agreement | binary byte count |
| `corpus/README.md:31` | offer trace keyed on `message=init count=N` as the standing basis | literal absent from the live binary | byte count |
| `corpus/README.md:34` | harness verifier "27 checks" and "17/17 reproduction", init-count == root union, as the standing basis | instrument has 28 `CHECKS` keys. Baseline expects offered 7, keys reproduced 7, init-count max 0 | key count; `baseline.json` |
| `corpus/README.md:38` | opencode's 9 classes "are now reproduced" by OC-1…OC-6 including `instruction-context` | extraction header and census `:175` say those ids are historical. Index basis was not marked | read |
| `corpus/README.md:39` | opencode model "quoted from its shipped JS" as AGENTS.md→CLAUDE.md→CONTEXT.md plus `~/.claude/CLAUDE.md` and fetched `https://` | census § B was rewritten. This index row was not | read |
| `verifiers/baseline.json:127` | "recorded dangling entries: sekhmet, xbrd" as the note on the live check | expect is 0 (`:33`). Those names are absent. Note was not marked historical | read + `test -e` |
| `verifiers/baseline.json:129` | `oc.log.init_count_max` is max of `` `message=init count=N` `` | expect is 0 (`:81`). Literal absent from the binary. Live analogue in the same file is `oc.log.skills_rescan_max`. Lesson marks the permission mode strings, not this note | read + byte count |
| `LOG.md:952-953` | checklist unchanged, exit 0, 552 lines, as the round-18 verdict | SKILL.md in that commit is 601 lines | `git show … \| wc -l`, exit 0 |

`verifiers/baseline.json:126` names `~/Projects/origin-work/ufo-fsd-alpha` inside a note prefixed "round 13:". That path example is dated. It is not a content hash. Not counted as a current-identity pin. The path is still absent.

### Pids

No `pid`, `MainPID`, or `process id` pin in the lane tree (`grep` over `kotoba-shokunin`, no matches). No pid counterexample.

## Not counted as current-tense pins

These are dated or explicitly qualified. Listing them so a later reader does not treat silence as a miss.

- `SCORECARD.md` axis cells cite 27/27 and 17/17 inside "round 15" / "Pre-round-15 evidence". Dated standing-cell residue. The move-log row 18 already says 28/28 against `ff59fc1b`/`d9123b9b`. Not an undated current pin.
- `LOG.md:243` and the round-10 section's `55016ef5…` sit in a dated round entry. Historical by section.
- `claim-census-round12.md:198-199` says HEAD hashed to `747b1226…`. That is the census instant. `cold-run-round11.md:383` already replaced "current" with `a32da4a4…`, which still matches. Not a standing identity claim.
- `sibling-description-rewrites-round8.md:63-70` md5 table is explicitly "mtime 2026-09-28" drift pins of then-bytes. Dated. Not re-checked as current identity, and not re-pinned.
- `SKILL.md:30-31` live-set errata (7) and `:35-38` describe-don't-pin of the 690-char byte. Hold.
- `SKILL.md:133-135` says the 18/14/11 agent-def counts are round-13-unverified and must be re-run before citing. That marker covers those three numerals only.

## Commands

All exit 0 unless noted. Cwd for git commands is `kotoba-shokunin`.

```
git rev-parse HEAD
→ b0c7cb2e248bccf692cf10e4d3c394e09944e83d

git status --porcelain   # first measurement
→ ?? plans/

git show --stat b0c7cb2e248bccf692cf10e4d3c394e09944e83d
→ LOG.md +7, SCORECARD.md +1, corpus/lessons/round-19-recensus.md +31,
  verifiers/verify_harness_claims.py 4 lines (2 insertions, 2 deletions)

git diff --stat 02302c521b933c55fc4be79193e61537e3380751 HEAD
→ same four files

sha256sum ~/.local/bin/omp ~/.opencode/bin/opencode
→ ff59fc1b484c1308a7247ad208305005627b3fac62b440737c2b1835ac32074e
→ d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9

# template: anchor "Compress into one routing hint" through the next NUL
→ 273 bytes, sha256 c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51
→ {{name}} and {{description}} present

wc -l SKILL.md
→ 601

git show 02302c521b933c55fc4be79193e61537e3380751:SKILL.md | wc -l
git show HEAD:SKILL.md | wc -l
git show d85982d:SKILL.md | wc -l
→ 601 / 601 / 599

git show 3b029b8:SKILL.md | md5sum
git show 3b029b8:SKILL.md | wc -l
git cat-file -t 3b029b8
→ 143fe473368ec9e2bb7adde9d0425b1c, 487, commit

git log --format=%H -- verifiers/fault_injection_corpus.sh
# then sha256 of each blob
→ fad752b5c710 9db6c692c752f0fd…   (does not start 9bc80ae61cea)
→ 633859fb24b0 7026e73687692f98…   (does not start 9bc80ae61cea)

test -e /home/vgpnk/projects; test -e ~/Projects/origin-work
test -e ~/Projects/ufo-fsd-alpha/ports/xbgst-codex
test -e ~/.agents/AGENTS.md; test -e ~/.config/opencode/agents
test -e ~/.config/opencode/command; test -e ~/.omp/agent/skills
test -e ~/.config/opencode/skills; test -e ~/.bailian
test -e ~/.claude/CLAUDE.md; test -e ~/.omp/agent/skills/ufo/SKILL.md
→ all false (printed NO / NOORIGIN / NOXBGST / NOAGENTS / NOOCAG / NOOCCMD / NOOMPSK)

# opencode binary anchor counts (byte count, not a log read)
CONTEXT.md 0
OPENCODE_DISABLE_CLAUDE_CODE 0
Instruction.resolve 0
message=init count= 0
duplicate skill name 0
skills rescanned 2
Instructions from: 3
disableClaudeCodePrompt 0
system-context-builtins 0

find /home/vgpnk -maxdepth 4 -path '*packages/opencode/src/skill/index.ts'
→ exit 0, empty

find ~/.omp/agent/sessions -name '*.jsonl' -printf . | wc -c
→ 260
# names only; file contents not read

# CHECKS key count in verifiers/verify_harness_claims.py
→ 28, including oc.log.skills_rescan_max
→ oc.permission.skill_lines and oc.permission.skill_allow are ("equal", …)

grep -i -E 'pid|MainPID|process id' kotoba-shokunin
→ no matches
```

Live file shas used as the comparison set (sha256 of the worktree files; none of these were in the late dirty set):

| file | sha256 |
|---|---|
| `verifiers/verify_skill_checklist.py` | `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27` |
| `verifiers/checklist-baseline.json` | `68831bb35f28f8dd19b41d36f6d8529768cccaa05275e22e52ff6487f641385e` |
| `verifiers/checklist-command-vocabulary.json` | `76d16a9cb53e43db25ec4549465fd00bf1f11551384350c7761328a935eeb02b` |
| `verifiers/verify_corpus_integrity.py` | `a32da4a4224e9810549016ec3000583f3068bf552d7a92b0666114c32476dd56` |
| `verifiers/verify_corpus_independent.py` | `430fe289feb07eff638e33326ac17554f19d7e0579363f9c90137e571671f0e5` |
| `verifiers/fault_injection_corpus.sh` | `9db6c692c752f0fdeb912f1d77e0049312e97b66422bd1a7e10a63c519bb5d34` |

Gates were not run. Lesson verdict lines for `verify_corpus_integrity.py`, `verify_surfaces.py`, `verify_corpus_independent.py`, `fault_injection_corpus.sh --self-test`, and `verify_harness_claims.py --self-test` are the lane's record, not this seat's exits.

## Named debt

Owner for every prose row: kotoba lane via parent. Unblock: append a not-current marker in the same file. Do not rewrite the original sentence. Do not delete the printed sha. Do not adopt a replacement count or sha from this report. No verifier expect should be moved to match a stale note.

| id | where | class | unblock |
|---|---|---|---|
| KHM-01 | `opencode-extraction-round14.md:96-97` | superseded hash equals live baseline field | append: equality was true of the round-14 baseline; field has moved; leave both printed hashes |
| KHM-02 | `instruction-surface-census-round13.md:53-56` | same equality, present tense | append: 2026-09-28 hashes are not what `baseline.json` records now; `:22-23` are the current pins |
| KHM-03 | `independent-verification-round12.md:120` | unrecoverable content hash as script identity | append: `9bc80ae61cea…` is the executed copy's sha, not HEAD; not in git |
| KHM-04 | `checklist-execution-round15.md:212-214`, `checklist-execution-round16.md:119-120` | round artifact shas unmarked | append: these identify that round's bytes, not HEAD. Current checklist pin, if required, is the round-17 recording, re-derived, not copied |
| KHM-05 | `harness-verifier-round10.md:34` and `:93-130` | dated binary hash plus present-tense counts | append: path marker `:112-114` does not cover counts or `55016ef5…`. Template sha `c1f03c8e…` still matches and stays a current pin |
| KHM-06 | `SKILL.md:71-72`, `:98-101`, `:103-109`, `:120`, `:137`, `:509-518`, `:539-547` | current-tense craft / sources | append. `:30-31` and `:35-38` stay and do not cover these rows. Do not retarget cites by editing them |
| KHM-07 | `instruction-surface-census-round13.md:222`, `:232` | live-table counts | append. Do not replace 37 or 197 in the row |
| KHM-08 | `agents-md-and-dispatch-surfaces.md:9-11`, `:26`; `render-mechanism-round7.md:64-67`; `instruction-surface-remeasure-round13.md:23-25` | fact / agreement left current | append. A survey date is not an absence marker |
| KHM-09 | `corpus/README.md:31`, `:34`, `:38`, `:39` | standing index basis | append. FILE-column paths were not the defect. Do not rewrite the rows |
| KHM-10 | `verifiers/baseline.json:127`, `:129` | live-gate notes describe the old host | notes vs expects. Do not fit expects to the notes. Permission `"mode": "at_least"` at `:110` and `:114` is already marked stale by the round-19 lesson; these two notes are not |
| KHM-11 | `LOG.md:908-916` and `:952-953` | completeness claim and a 552-line verdict false of its own commit | append a residual. Do not rewrite round 18 |

`SKILL.md:512-518` stays unresolved rather than confirmed line-drift: no local `index.ts` at search depth 4. Unblock is a declared opencode checkout before anyone treats those line numbers as current. Not a hash finding.

## What held

- Live template sha `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51`, 273 bytes, both placeholders present. Matches `baseline.json` `omp.elf.template_sha256`. Do not describe-don't-pin it.
- Live binary shas match `baseline.json:5` and `:7` and census `:22-23`.
- Round-17 checklist-verifier pin and the round-12 "current" corpus-verifier pins still match the files.
- Deleted-path content hashes are not asserted as current identity where the path is gone and the file says so.
- No pid pin.
- Round 19 did not re-pin a superseded sha as a new current pin.
