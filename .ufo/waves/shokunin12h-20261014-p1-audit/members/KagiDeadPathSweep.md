# Kagi dead-path sweep

Advisory data for the landed kagi tree. Not a judge verdict, receipt, or admission. No lane file was edited. No gate was re-run (that seat is `KagiGateRerun`). No `lsp` device is mounted in this seat; the sweep is literal path text, not semantic proof.

Swept tree: `/home/vgpnk/Projects/shokunin/kagi-shokunin` at `5b0d4b784624a15506d3c85c77c3ae619e07467f` (`git rev-parse HEAD`, exit 0). `git status --porcelain` exit 0, only `?? plans/`. `plans/` has no hits. `.git` excluded. 70 other files scanned.

## Host absence (measured)

`python3` `os.path.lexists` on expanded paths, exit 0:

| path | result |
|---|---|
| `/home/vgpnk/projects` | ABSENT |
| `/home/vgpnk/Projects` | EXISTS |
| `/home/vgpnk/Projects/shokunin` | EXISTS |
| `/home/vgpnk/Projects/origin-work` | ABSENT |
| `/home/vgpnk/Projects/webzites` | ABSENT |
| `/home/vgpnk/Projects/ds4cc-marketplace` | ABSENT |
| `/home/vgpnk/Projects/plazir-15-site` | ABSENT |
| `/home/vgpnk/.bailian` | ABSENT |
| `/home/vgpnk/archive` and `…/bench-arena` | ABSENT |
| `/home/vgpnk/.local/bin/the-janitor` | ABSENT |
| `/home/vgpnk/.config/the-janitor` | ABSENT |
| `/home/vgpnk/.local/state/the-janitor` | ABSENT |
| `/home/vgpnk/.local/bin/tac-check` | ABSENT |

`shutil.which("webzites")` is `None`. Case-sensitive full-tree count, exit 0: `ds4cc`, `ds4cc-marketplace`, `plazir`, `plazir-15-site`, `bailian`, `bench-arena`, `Projects/origin-work`, `Projects/webzites` are all 0.

Negative control (not a deleted path): capital-P `~/Projects/shokunin` is cited at `corpus/knowledge/adjacency-breadth.md:142` and `corpus/knowledge/adjacency-scope.md:252`. Those lines are not hits.

## Classification rule

A hit is a line containing the deleted token. One class per line.

- **live** — current lookup, pin, procedure, schema, evidence pointer, or identity, with no deadness mark on the line or its immediate sentence, and not inside a scratch harness.
- **marked-historical** — a same-file caption says the following text is the preserved historical record. Only `PROVINCE.md:10-17` covering `:19-44`, plus `corpus/lessons/round-18.md:58-62` covering its own path line `:59`.
- **labelled** — the line or the unbroken sentence says the path is absent / historical / nonexistent / deleted-path / `[substrate]` / may be absent, or the line is fixture text inside `selftest()` / `falsify()` and never opens the real host path.
- **unresolved** — the token is not a path a reader or gate opens (search needle, foreign-file content label, synthetic mutation payload that is not asserted to be the checkout).

The lane's own citation rule is line-local (`corpus/claim-ledger.sh:431-433`, markers at `:440`). A caption in another file does not reclassify a citing line. Host paths are outside `cite_class` (`claim-ledger.sh:442-450`), so a `CITATION_GATE: CLEAN` result would not see this sweep. That gate was not re-run here.

`echo absent` / runtime-class `ABSENT` does not label a path dead (`corpus/checklist.tsv:34` still greps `$HOME/.local/bin/the-janitor`). A prior TSV row's `[substrate]` does not label the next row (`corpus/claim-ledger.tsv:41` is live).

## Lane record vs this sweep

| lane claim | verdict | evidence |
|---|---|---|
| `corpus/lessons/round-19-recensus.md:38-39`: lowercase `~/projects/shokunin` strings are deleted-path spellings; resolver is script-derived (`scope-gate.sh:91`) | **agree on the resolver, disagree that the spellings are labelled** | `scope-gate.sh:91` is `LANE_ROOT=… "$SCRIPT_DIR/../.."`. 11 citing lines are still unmarked live citations, including a `cd` recipe and a schema comment that still names `~/projects` as the resolver. The round-19 sentence labels the class, not those lines. |
| `corpus/lessons/round-18.md:7-8`, `LOG.md:725-727`, `SCORECARD.md:314`: `grep origin-work\|ufo-fsd` is empty / zero citations | **disagree as a current substring claim; agree there is no path-shaped cite** | 4 lines contain the needle `origin-work` (the sentences themselves). `Projects/origin-work` count is 0. No `corpus/*.sh` hit. Read the empty-grep sentence as true only before the writeup that contains it. |
| `corpus/lessons/round-18.md:66`: stale `--src` / origin path failures = 0 | **agree for path-shaped origin-work; the substring claim is the row above** | zero `~/Projects/origin-work` citations. Gates do not derive a source root from that tree. |
| `PROVINCE.md:10-17`: surfaces below are HISTORICAL; unblock is reinstall | **agree for the surface list `:20-24,:33-34,:38`** | those 8 lines are marked-historical. The erratum does not cover `SKILL.md`, knowledge source-basis lines, or the gate data files. |
| `corpus/lessons/round-18.md:58-62`: round 9–17 evidence quotes remain historical via this erratum | **disagree that the erratum marks the quoting lines** | the word `historical` is on `round-18.md:58`. The quoted files do not carry it. 146 live prose lines still name janitor host paths as current. |
| substrate absence is named debt; do not re-pin to an empty host (`round-18.md:51-54`, `PROVINCE.md:16-17`) | **agree for the operational pin class** | 74 live operational citations remain. They are fail-closed lookups, not a silent pass. Unblock stays reinstall. Do not re-pin. |

## 1. Lowercase `~/projects` and `$HOME/projects`

16 hits. Capital-P `~/Projects` excluded.

### live (11) — unmarked current citations

- `corpus/README.md:25` — index evidence column cites `` `~/projects/shokunin/CORPUS.md` ``.
- `corpus/adjacency.tsv:19` — schema comment: `lane:` resolves under `~/projects/shokunin/<lane>-shokunin/`.
- `corpus/claim-ledger.tsv:22` — `R11-08` note says the gate requires `` `~/projects/shokunin/<lane>-shokunin` ``.
- `corpus/knowledge/adjacency-scope.md:92` — same resolver sentence as the TSV comment.
- `corpus/knowledge/adjacency-scope.md:130` — `# own $HOME/projects` called "the whole fleet checkout". Counterexample: that directory is absent; the checkout is `/home/vgpnk/Projects/shokunin`.
- `corpus/knowledge/surface-census.md:248` — reproduction recipe `cd ~/projects/shokunin/kagi-shokunin`. Following it is ENOENT. The capital-P recipe at `adjacency-scope.md:252` is the surviving spelling.
- `corpus/lessons/round-1-aggregator-audit.md:3` — scope path `` `~/projects/shokunin/CORPUS.md` ``.
- `corpus/lessons/round-1-aggregator-seed.md:10` — `` `~/projects/shokunin/MANIFEST.json` ``.
- `corpus/lessons/round-1-aggregator-seed.md:15` — `` `~/projects/shokunin/.ufo/watchdog.log` ``.
- `corpus/lessons/round-1-aggregator-seed.md:77` — `` `~/projects/shokunin/.ufo/reports/round-2/AGGREGATE.md` ``.
- `corpus/lessons/round-4-aggregator-audit.md:58` — present tense: the path resolves in `` `~/projects/shokunin/.ufo/…` ``. It does not.

Owner: kagi. Unblock: label each line deleted-path / historical, or point the schema comments at the script-derived grandparent. Do not retarget lesson evidence to a new hash. Do not treat round-19's one sentence as the mark on these lines.

### labelled (3)

- `LOG.md:711` — same sentence as `:710` "nonexistent lowercase".
- `corpus/lessons/round-19-recensus.md:38` — "deleted-path spellings".
- `corpus/scope-gate.sh:741` — scratch fixture inside `falsify()`: appends `# own $HOME/projects` to a temp TSV. Does not `stat` the host path.

### unresolved (2)

- `corpus/knowledge/adjacency-scope.md:285` — falsifier payload `Append # own $HOME/projects`. Not a checkout identity (that claim is `:130`, live).
- `corpus/lessons/round-16.md:80` — past-tense mutation token. Not a lookup. Not labelled dead.

## 2. `~/Projects/origin-work`

Path-shaped hits: **0** (`Projects/origin-work` count 0; directory ABSENT).

Substring `origin-work` (4), all **unresolved** needles, not paths a reader opens:

- `LOG.md:725`
- `SCORECARD.md:314`
- `corpus/lessons/round-18.md:7`
- `corpus/lessons/round-19-recensus.md:19`

`round-19:19-20` ("no `$UFO_SRC` / `--src` / `origin-work` derivation in the seven gates") matches this sweep: the four needles are not in `corpus/*.sh`. The empty-grep sentences at `LOG.md:725`, `round-18.md:7-8`, and `SCORECARD.md:314` are false as current substring claims because they contain the needle. Owner: kagi record. Unblock: describe-don't-pin those sentences as pre-writeup history. No path citation to retarget.

## 3. `webzites`

Path-shaped `Projects/webzites` or `~/webzites`: **0**. Directory and `which webzites` absent. 10 name hits.

### live (2)

- `corpus/knowledge/cdp-bridge-1password.md:78` — present tense: port 9222 is shared with the webzites kimi fleet.
- `corpus/knowledge/cdp-bridge-1password.md:79` — current command `` `webzites lease acquire` ``.

Owner: kagi for the sentence; kake owns the lease (`kake-shokunin/SKILL.md:159` still states the command; kake's own tree cites carry r18 absence markers, not re-audited here). Unblock: label `:78-79` historical. Do not absorb the lease. Integrator still owns the CDP ruling. Do not run the command.

### unresolved (8) — name or foreign-text label, not a filesystem path

- `SHONEN.md:12`
- `corpus/README.md:87`
- `corpus/scope-gate.sh:11`
- `corpus/scope-gate.sh:703`
- `corpus/knowledge/adjacency-scope.md:37`
- `corpus/lessons/round-16.md:15`
- `corpus/lessons/round-6-aggregator-audit.md:125`
- `corpus/lessons/round-6-aggregator-audit.md:132`

## 4. `ds4cc-marketplace`, `plazir-15-site`, `~/.bailian`, `~/archive/bench-arena`

**0 hits** for `ds4cc`, `plazir`, `bailian`, `bench-arena`, and the path forms. No live citation. No debt in this lane.

## 5. the-janitor host paths

296 hits. A host-path hit is a line naming `~/.local/bin/the-janitor`, `~/.config/the-janitor`, `~/.local/state/the-janitor`, `$HOME` forms of those, `bin/the-janitor` / `config/the-janitor` / `state/the-janitor` as path fragments, or `$CONFIG_DIR` / `$STATE_DIR` (this lane's names for those two trees). Bare `the-janitor <verb>` command mentions are not hits.

| class | n |
|---|---|
| live | 220 |
| labelled | 67 |
| marked-historical | 9 |
| unresolved | 0 |

Of the 220 live: **74 operational** (current pin or lookup; fail-closed by design) and **146 unmarked prose/procedure**.

### marked-historical (9)

Governing caption `PROVINCE.md:10-17` ("surfaces below are HISTORICAL … preserved verbatim"):

- `PROVINCE.md:20`
- `PROVINCE.md:21`
- `PROVINCE.md:22`
- `PROVINCE.md:23`
- `PROVINCE.md:24`
- `PROVINCE.md:33`
- `PROVINCE.md:34`
- `PROVINCE.md:38`

Own-sentence historical frame:

- `corpus/lessons/round-18.md:59` (sentence starts at `:58` "remain historical"; `:61` "no longer exists")

`PROVINCE.md:12` is the erratum's own absence list, classed labelled, not as a surface-list row.

### labelled, same-line or sentence (8)

- `PROVINCE.md:12` — continuation of `:11` "measured absent".
- `LOG.md:729` — sentence ends at `:731` "are all absent".
- `corpus/claim-ledger.sh:130` — "may be absent".
- `corpus/claim-ledger.tsv:26` — `[substrate]` on the `R12-01` note that names `$HOME/.local/bin/the-janitor`.
- `corpus/knowledge/substrate-deferral.md:5`
- `corpus/knowledge/substrate-deferral.md:6`
- `corpus/lessons/round-18.md:15` — `→ absent`.
- `corpus/lessons/round-18.md:16` — `no such dir`.

### labelled, scratch fixture (59)

Inside `falsify()` or `selftest()`. Temp tree or temp TSV. Not a host `stat`.

`corpus/scope-gate.sh` (24): `725,747,821,824,825,826,836,837,838,839,848,849,924,979,983,984,988,1012,1015,1019,1020,1062,1063,1088`

`corpus/surface-census.sh` (35): `701,702,704,705,706,707,709,710,713,714,715,716,717,721,724,725,736,737,738,739,740,741,742,743,745,768,769,770,771,772,773,774,775,789,790`

`scope-gate.sh:1088` is inside `selftest()` (the harness is still open there; `:1088` asserts a map line against `$R/host`, not `$HOME`). `surface-census.sh` `selftest()` closes at `:848`.

### live operational (74) — current pin or lookup

Owner: kagi. Unblock: reinstall the the-janitor tree, then one un-defer (`PROVINCE.md:16-17`, `corpus/knowledge/substrate-deferral.md:31-37`). Do not re-pin baselines to the empty host (`corpus/lessons/round-18.md:51-54`). These lines are live on purpose. They are not a pass.

- `corpus/adjacency.tsv:48,49,51`
- `corpus/checklist.tsv:22,34,36,41`
- `corpus/claim-ledger.sh:143` — `[[ -x "$HOME/.local/bin/the-janitor" ]]`
- `corpus/claim-ledger.tsv:41` — current owned-prefix names in the data file (not a host open)
- `corpus/drift-baseline.tsv:1,2,3,4,5,12`
- `corpus/drift-pins.sh:21,46,47,48,49,50,57,71,72,76`
- `corpus/drift-symbols.tsv:11,12,13,14,15,16,17,18,19,20,21,22,30`
- `corpus/op-ref-probe.sh:67` — `JAN_BIN` default
- `corpus/surface-census.sh:6,103,625` — `:625` is the `--deep` custody path `$HOME/.local/state/the-janitor/tac-daybreak-blue.json`
- `corpus/surface-census.tsv:11,17,18,19,21,22,23,24,25,30,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51`
- `corpus/transcript-scan.sh:5,15,34`
- `corpus/knowledge/substrate-deferral.md:31,84`

### live unmarked prose / procedure (146)

Owner: kagi. Unblock: same-line historical or absent label (describe-don't-pin). Do not delete the quotes. Do not re-pin hashes (hash identity is the historical-marking seat's question; this sweep only classes the path citation). `round-18.md:58-62` does not mark these lines. `PROVINCE.md:10-17` does not cover them.

Do not execute the falsify recipes. They name the real host path while saying "copy" or "scratch":

- `SKILL.md:618` — `touch ~/.config/the-janitor/notes.md` (sentence starts `:617`).
- `corpus/knowledge/surface-census.md:270,271,272,274` — `chmod` / move / `rm` / `touch` on the real tree. `:268` says "on a copy"; the commands are not rooted on a copy.

Other live prose lines:

- `LOG.md:8,9,36,68,76,79,634`
- `PROVINCE.md:50`
- `SCORECARD.md:39,96`
- `SKILL.md:28,33,39,42,93,103,139,142,226,387,390,432,477,493,573,576,580,593,618,645`
- `corpus/README.md:19,20,21,29`
- `corpus/knowledge/adjacency-scope.md:54,55,184`
- `corpus/knowledge/cdp-bridge-1password.md:3`
- `corpus/knowledge/checklist-execution.md:181`
- `corpus/knowledge/config-layering.md:3,8,9,19,20,22,58,86,97`
- `corpus/knowledge/control-plane-hardening.md:3,5,7,39,81,96,138,141`
- `corpus/knowledge/credential-isolation.md:3,25,31,74`
- `corpus/knowledge/drift-gate.md:27,28,38,39,153,175,182,186`
- `corpus/knowledge/handler-on-disk-state.md:3,5,18,29,43,54,166,200,221,222`
- `corpus/knowledge/handler-trust-boundary.md:3,5,127,174,198,213,228,234,245,262,263,264,274,285`
- `corpus/knowledge/janitor-command-surface.md:3,4,35,60`
- `corpus/knowledge/janitor-env-contract.md:3,14,15,16,81,83,84`
- `corpus/knowledge/janitor-lifecycle.md:3,24,63`
- `corpus/knowledge/op-cli-surface.md:4`
- `corpus/knowledge/op-env-refs.md:3,4,19,54`
- `corpus/knowledge/op-ref-consumption.md:3,230,305`
- `corpus/knowledge/surface-census.md:5,22,24,44,53,254,270,271,272,274`
- `corpus/knowledge/tac-evidence-integrity.md:4,15`
- `corpus/knowledge/transcript-hygiene.md:3,114,141`
- `corpus/lessons/round-1-aggregator-seed.md:31,32,41`
- `corpus/lessons/round-16.md:82`
- `corpus/lessons/round-4-aggregator-audit.md:22,28,53`
- `corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:15,20,28`
- `corpus/lessons/round-6-aggregator-audit.md:44,112`
- `corpus/lessons/round-6.md:6,47`
- `corpus/lessons/round-7.md:43,49`
- `corpus/lessons/round-8-aggregator-box3-coldrun.md:33`

`$CONFIG_DIR` / `$STATE_DIR` lines in that list are included because this lane defines them as the janitor config and state trees (`SKILL.md:93`, `corpus/surface-census.tsv:21,35`).

## Named debt

| id | what | class | owner | unblock |
|---|---|---|---|---|
| D1 | 11 unmarked lowercase `~/projects` / `$HOME/projects` citations, including `surface-census.md:248` (`cd`) and `adjacency-scope.md:130` ("the whole fleet checkout") | live | kagi | label each line, or point schema comments at `scope-gate.sh:91`. Do not retarget lesson hashes. |
| D2 | empty-grep sentences `LOG.md:725`, `round-18.md:7`, `SCORECARD.md:314` | unresolved needles; false as current substring claims | kagi record | describe-don't-pin. No path-shaped origin-work cite to repair. |
| D3 | `cdp-bridge-1password.md:78-79` `webzites lease acquire` | live command; path form absent | kagi prose; kake owns the lease | label historical. Do not run. Integrator owns the CDP ruling. |
| D4 | 74 live operational janitor host-path pins/lookups | live by design | kagi | reinstall substrate (`PROVINCE.md:16-17`). Do not re-pin to empty host. |
| D5 | 146 unmarked prose/procedure janitor host-path citations, including falsify recipes `SKILL.md:618` and `surface-census.md:270-274` | live | kagi | same-line historical label. Do not execute the recipes. Do not delete quotes. |

Zero-hit families (`ds4cc-marketplace`, `plazir-15-site`, `~/.bailian`, `~/archive/bench-arena`) have no debt here.

## Limits

- Command-only `the-janitor status` lines are not in the 296. A reader of `SKILL.md` still has many of those as current procedure; they are out of the path-shaped set.
- Scratch-fixture classification uses brace-matched `selftest()` / `falsify()` ranges, checked at `scope-gate.sh:1088` and `surface-census.sh:848`.
- No content of `op.env`, credentials, or session DBs was read. Absence is `lexists` / `which` only.
- Confidence: high on hit inventory and host absence. High on the live/labelled split for lines read in full. The operational-vs-prose split is a role tag on the live class, not a fifth class.
