# KamaDeadPathSweep — advisory

Seat: `KamaDeadPathSweep`. Data only. Not a judge verdict, receipt, or admission. No lane file was edited. No gate was run (gate rerun is another seat).

Lane: `kama-shokunin` @ `84a81304d7b0c77c84fe495f3bb728e8729faaff` (matches the assigned identity commit). Sweep root: `/home/vgpnk/Projects/shokunin/kama-shokunin`, every file, `.git` excluded.

## Rubric

A hit is a line whose text names one of the deleted path tokens. One line can hit two classes.

- **live** — a reader of that sentence, command, or table row would open the path as a current location. Neither the line nor the sentence it continues says historical, deleted, gone, relocated-from, or errata. A later note that does not name this line does not retract it.
- **marked-historical** — the line or the sentence it continues retracts the path (historical, deleted, gone, no longer exists, relocated-from, "the path/paragraph above is historical").
- **labelled** — not a same-sentence retraction, but a specific label keeps it from being an existence claim: fail-closed "first existing of" candidate; errata names this row number or "llm-wiki non-model rows"; dated round-log line whose later round in the same `LOG.md` records the same path gone.
- **unresolved** — token is not a filesystem path (unit name, nickname, SSH host alias, hostname).

If the bar is instead "no same-line mark ⇒ live", the labelled table rows in the upgrade note below become live. This seat did not use that bar.

## Host facts (this seat)

`test -e` exit 1 (absent) for: `/home/vgpnk/projects`, `/home/vgpnk/Projects/origin-work`, `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`, `/home/vgpnk/Projects/webzites`, `/home/vgpnk/Projects/ds4cc-marketplace`, `/home/vgpnk/Projects/plazir-15-site`, `/home/vgpnk/.bailian`, `/home/vgpnk/archive`, `/home/vgpnk/archive/bench-arena`, `/home/vgpnk/archive/bench-arena/loop.sh`, `/home/vgpnk/bench-arena`, `/home/vgpnk/bench-arena/loop.sh`, `/home/vgpnk/.config/the-janitor`, `/home/vgpnk/.config/the-janitor/opencode.json`, `/home/vgpnk/.local/bin/the-janitor`, `/home/vgpnk/.config/systemd/user/webzites-probe.timer`, `/home/vgpnk/.config/systemd/user/webzites-probe.service`.

Present: `/home/vgpnk/Projects` inode `27238`; `/home/vgpnk/Projects/ufo-fsd-alpha`; the nine `~/projects/shokunin/...` targets named in rows 22–30, at the capital root (`kengaku-shokunin/SKILL.md`, `kengaku-shokunin/PROVINCE.md`, four kagi knowledge files, two kumitate knowledge files, `.ufo/waves/round-9/seats/standing-tables.md`). Also present: `.ufo/reports/round-3/kagi.md`, `.ufo/reports/round-4/kengaku.md`.

## Headline

| Class | Path hits (lines) | Live lines |
|---|---|---|
| lowercase `~/projects` / `/home/vgpnk/projects` | 22 | 19 |
| `origin-work` | 26 | 2 |
| `webzites` path | 17 path + 1 unit-name | 0 |
| `ds4cc-marketplace` | 0 | 0 |
| `plazir-15-site` | 0 | 0 |
| `~/.bailian` | 0 | 0 |
| `bench-arena` | 8 | 1 |
| the-janitor host paths | 38 path-shaped + 4 shorthand | 25 |
| **unique live lines** | | **46** |

Zero live citations does not hold. The live set is named below with owner and unblock.

## Lane-record verdicts

- **Agree** `corpus/lessons/round-4-recensus.md:29-30`: `SKILL.md` still teaches a live pin world. Counterexample: `SKILL.md:35-39` ("Six consumer surfaces still pin 8080") and checklist item 12 at `SKILL.md:222` grep deleted janitor paths as current procedure. Removed-row note at `SKILL.md:308-311` does not cover that checklist line.
- **Agree, adjacent, not this path set** `round-4-recensus.md:30` and `PROVINCE.md:10-11`: province still owns `~/.config/systemd/user/qwen-coder.service` and `~/.config/opencode/opencode.json:158` / `agents/janitor.md:21`. Those files are outside the eight named classes (`janitor.md` is the opencode agent, not `~/.config/the-janitor`). Not counted as hits here. Owner: kama province prose. Unblock: L0 province contraction, or an errata that the artifacts are absent. Do not reinstall to make the sentence true.
- **Disagree** `LOG.md:232-233` ("historical markers on the rest") as a lane-wide claim. Markers landed on the registry errata, some origin-work sentences, and webzites row 38. They did not land on the SKILL checklist, rows 22–30, `listener-census.md` §0.1 and the §3 remote paragraph, `cross-lane-scope.md` evidence column, `drift-timeline.md:18`, or `alias-endpoint-normalization.md:56`.
- **Agree inside one paragraph, not lane-wide** `corpus/knowledge/consumer-registry.md:38` ("Every `origin-work/` citation below names that relocated tree"). `consumer-registry.md:217-221` then marks the two-checkout paragraph historical. `listener-census.md:122` and `corpus/lessons/round-1.md:69` are outside that sentence and still read as a live second tree.
- **Agree** the probe candidate is not a live pin. `tools/kama-probe.sh:546-547` opens `origin-work` only after `[ -d ]`. First candidate `/home/vgpnk/Projects/ufo-fsd-alpha` exists; the second is absent. Fail-closed. Do not re-repair the resolver.
- **Agree** `LOG.md:248-251` absence list. Re-measured absent this seat, including `~/archive/bench-arena/loop.sh` and `~/Projects/webzites/`.

## Live citations (owner / unblock)

Owner for every row: kama corpus/SKILL prose. Unblock: append-only errata that names the line. Do not rewrite round-1 sentences. Do not restore deleted host files to make a citation resolve. Case-correct only where the capital-path file exists (rows 22–30). Operator owns substrate reinstall; that does not clear these lines.

### lowercase `~/projects` — 19 live

The directory is absent. Rows 22–30 name files that exist under `/home/vgpnk/Projects/shokunin/`. Errata `consumer-registry.md:30-80` re-anchors `origin-work` and marks webzites/archive gone. It does not mention this class. FleetBoundaryConnector already named `:111-119` and `:332-337`; this seat re-derived the same lines plus the others below.

| path:line | why live |
|---|---|
| `LOG.md:66` | Asserts `/home/vgpnk/projects` ≠ `/home/vgpnk/Projects` with inodes `101125103` / `27238`. Capital inode `27238` still holds. Lowercase path is absent, so the pair cannot be stat'd. No later LOG retraction. |
| `corpus/knowledge/consumer-registry.md:111` | Row 22 `~/projects/shokunin/kengaku-shokunin/SKILL.md:322-323`. Not in the historical row list (`:64` names #1–#11, #14–#16, #21, #31–#34). |
| `corpus/knowledge/consumer-registry.md:112` | Row 23 `~/projects/shokunin/kengaku-shokunin/PROVINCE.md:14`. Verdict cell still `MODEL_OK`. |
| `corpus/knowledge/consumer-registry.md:113` | Row 24 kagi `janitor-env-contract.md:55`. |
| `corpus/knowledge/consumer-registry.md:114` | Row 25 kagi `handler-trust-boundary.md`. |
| `corpus/knowledge/consumer-registry.md:115` | Row 26 kagi `credential-isolation.md`. |
| `corpus/knowledge/consumer-registry.md:116` | Row 27 kagi `drift-gate.md:185`. |
| `corpus/knowledge/consumer-registry.md:117` | Row 28 kumitate `ops-watchers.md:393`. |
| `corpus/knowledge/consumer-registry.md:118` | Row 29 kumitate `remaining-scripts-census.md:524`. |
| `corpus/knowledge/consumer-registry.md:119` | Row 30 `~/projects/shokunin/.ufo/waves/round-9/seats/standing-tables.md`. Also cites `~/.config/the-janitor/opencode.json:16` (janitor class, same line). |
| `corpus/knowledge/consumer-registry.md:191` | Same kengaku `PROVINCE.md` path. `*historical: port dead today*` retracts the port verdict, not the path. |
| `corpus/knowledge/consumer-registry.md:332` | Search-root command rooted at `~/projects/shokunin/...`. |
| `corpus/knowledge/consumer-registry.md:334` | "Lane-level pin counts across `~/projects/shokunin`". |
| `corpus/knowledge/consumer-registry.md:337` | Runnable `grep ... ~/projects/shokunin`. ENOENT today. |
| `corpus/knowledge/listener-census.md:35` | §0.1 trap: two distinct directories, inodes cited. Also claims (`:38-39`) this census's repo is under the lowercase tree. Repo is `/home/vgpnk/Projects/shokunin/kama-shokunin`. |
| `corpus/knowledge/listener-census.md:37` | `find /home/vgpnk/projects -maxdepth 3 -name ufo-fsd-alpha` taught as the proof. |
| `corpus/knowledge/listener-census.md:284` | Command ledger still runs `stat` on `/home/vgpnk/projects`. Comment at `:283` marks the second checkout historical; it does not mark these two lines. |
| `corpus/knowledge/listener-census.md:285` | Same ledger, `find /home/vgpnk/projects`. |
| `corpus/lessons/round-1.md:46` | Standing trap table: lowercase path "misses the entire family" because it is a different directory. 2026-10-14 errata at `:73-75` covers webzites, not this row. |

### `origin-work` — 2 live

| path:line | why live |
|---|---|
| `corpus/knowledge/listener-census.md:122` | Unmarked prose under the webzites row: "Only `origin-work` has more: `github`". Row `:118` marks the webzites checkout deleted. This paragraph does not. Parent `origin-work` is absent. |
| `corpus/lessons/round-1.md:69` | Peer ledger: github remote "on `origin-work` only". Errata `:73-75` deletes webzites and swaps surviving remotes. It does not say `origin-work` is gone. |

### `webzites` — 0 live

Every path hit is marked-historical or labelled. See full hit list. `LOG.md:170` `webzites-probe.timer` is unresolved (unit name, not a path). Unit file absent.

### `bench-arena` — 1 live

| path:line | why live |
|---|---|
| `corpus/lessons/round-1-citations.md:72` | Errata presents `~/archive/bench-arena/loop.sh:5` as the corrected current location ("default is unchanged"). That file is absent. No later sentence in this file records the second deletion. `LOG.md:250` does, but it does not name this line. |

### the-janitor host paths — 25 live

Host paths in scope: `~/.config/the-janitor/**`, `~/.local/bin/the-janitor`, `/home/vgpnk/.local/bin/the-janitor`, and line-number shorthand (`the-janitor:N`, `the-janitor/opencode.json`) that points at those files. All absent.

| path:line | why live |
|---|---|
| `SKILL.md:76` | Worked example "the live drift": CLI agrees `~/.local/bin/the-janitor:47`. Section `:35` present tense "still pin". |
| `SKILL.md:78` | Table row 4 `~/.local/bin/the-janitor:16-19` as a current consumer. |
| `SKILL.md:79` | Table row 5 `~/.config/the-janitor/opencode.json:5-6,8-9,16`. |
| `SKILL.md:121` | Decision table: `the-janitor:47` and `the-janitor/opencode.json:5-6` have no fallback. Shorthand path. |
| `SKILL.md:222` | Checklist item 12: `grep -rn ... ~/.config/the-janitor/opencode.json ~/.local/bin/the-janitor` — "every live pin in one shot". Current procedure. |
| `SKILL.md:292` | Cited sources, consumer list, not under the "Producer (historical — files deleted)" bullet at `:312`. |
| `corpus/knowledge/consumer-registry.md:119` | Row 30 evidence cell cites `~/.config/the-janitor/opencode.json:16`. Row 30 is not in the historical row-number list. |
| `corpus/knowledge/consumer-registry.md:136` | "Three independent executable sites declare" the bare id, including `~/.local/bin/the-janitor:17` and `~/.config/the-janitor/opencode.json:8-9`. Present tense. Not a table row the errata numbered. |
| `corpus/knowledge/consumer-registry.md:179` | "`~/.local/bin/the-janitor` is a consumer pin" and "must remain" covered. Registry no longer has that row (correctly removed). The sentence was not updated. |
| `corpus/knowledge/listener-census.md:112` | Reconciliation row: `~/.local/bin/the-janitor:19`, verdict "NO — drift", no historical mark. |
| `corpus/knowledge/listener-census.md:177` | Id-axis table: `the-janitor:17` as a current id site. |
| `corpus/knowledge/listener-census.md:179` | `the-janitor:15` `PORT=40961` as a current second-order pin. |
| `corpus/knowledge/listener-census.md:294` | Measured-facts list: `the-janitor` `PORT=40961` with no listener. Standing census, not retracted. |
| `corpus/knowledge/cross-lane-scope.md:16` | Ownership table evidence `/home/vgpnk/.local/bin/the-janitor:16-19`. No errata in this file. |
| `corpus/knowledge/cross-lane-scope.md:47` | Operator decision line evidence includes `/home/vgpnk/.local/bin/the-janitor:16-19`. Present-tense repoint recommendation. |
| `corpus/knowledge/drift-timeline.md:18` | Header `:3` says commands are shown so observations can be refreshed. Refresh command greps `~/.local/bin/the-janitor`. File absent. No deletion row. |
| `corpus/knowledge/alias-endpoint-normalization.md:56` | Present tense: the binary "sets `MODEL_ENDPOINT`" and "must remain covered by the endpoint-consumer registry". |
| `corpus/lessons/probe-mutation-matrix.md:4` | "Live census" includes `/home/vgpnk/.local/bin/the-janitor:16-19` and says it MUST be in the registry. No 2026-10 errata in this file. |
| `corpus/lessons/probe-mutation-matrix.md:41` | "Live census" repeats the same path as a fourth stale pin. |
| `corpus/lessons/round-1-citations.md:69` | Round-2 errata still asserts `~/.config/the-janitor/opencode.json:16` "is the 8080 baseURL" and lines 5–7 hold `enabled_providers`. File absent. |
| `corpus/lessons/round-1-safety.md:61` | Standing rule: do not repoint `~/.local/bin/the-janitor:16-19`. Evidence path gone. |
| `corpus/lessons/round-1-safety.md:62` | `nl -ba /home/vgpnk/.local/bin/the-janitor` cited as the live command. |
| `corpus/lessons/round-1-safety.md:73` | `/home/vgpnk/.local/bin/the-janitor:46-47` "states that it has no cloud or model fallback". Present tense. |
| `corpus/lessons/round-1-safety.md:82` | L0 approval still tied to `/home/vgpnk/.local/bin/the-janitor:19`. |
| `corpus/lessons/round-1.md:83` | Open round-2 seed: `~/.config/the-janitor/opencode.json` "declares `limit.context: 32768`". Not closed by the webzites errata at `:73`. |

## Upgrade note (not applied)

These are **labelled**, not live, because an errata names the row or the round log later records deletion. A same-line scanner that ignores row numbers would call them live. Do not treat this note as a second verdict.

- Janitor table rows, errata names #1–#11: `consumer-registry.md:93` `:94` `:95` `:96` `:97`. Cell text still says `FOREIGN_SERVICE` / `DEAD` with no `*historical*`.
- Bench-arena row 21, errata names #21: `consumer-registry.md:110`. Cell still says `FOREIGN_SERVICE`. File absent.
- llm-wiki rows, errata `:53-55` says "llm-wiki non-model rows are historical": `consumer-registry.md:239` `:240` `:241` `:242`. Lines themselves do not say deleted.
- Dated LOG lines later retracted at `LOG.md:248-251`, line itself unmarked: `LOG.md:46` `:47` `:93` `:163` `:164`.

## Full hit list

### lowercase `~/projects` (22)

| path:line | class |
|---|---|
| `LOG.md:66` | live |
| `corpus/knowledge/consumer-registry.md:111` | live |
| `corpus/knowledge/consumer-registry.md:112` | live |
| `corpus/knowledge/consumer-registry.md:113` | live |
| `corpus/knowledge/consumer-registry.md:114` | live |
| `corpus/knowledge/consumer-registry.md:115` | live |
| `corpus/knowledge/consumer-registry.md:116` | live |
| `corpus/knowledge/consumer-registry.md:117` | live |
| `corpus/knowledge/consumer-registry.md:118` | live |
| `corpus/knowledge/consumer-registry.md:119` | live |
| `corpus/knowledge/consumer-registry.md:191` | live |
| `corpus/knowledge/consumer-registry.md:212` | marked-historical (errata `:217` "the paragraph above is historical") |
| `corpus/knowledge/consumer-registry.md:213` | marked-historical (same paragraph) |
| `corpus/knowledge/consumer-registry.md:332` | live |
| `corpus/knowledge/consumer-registry.md:334` | live |
| `corpus/knowledge/consumer-registry.md:337` | live |
| `corpus/knowledge/listener-census.md:35` | live |
| `corpus/knowledge/listener-census.md:37` | live |
| `corpus/knowledge/listener-census.md:284` | live |
| `corpus/knowledge/listener-census.md:285` | live |
| `corpus/lessons/round-1.md:46` | live |
| `corpus/lessons/round-1-citations.md:18` | labelled (frozen Command/Observed-output record of a past audit; not a current open instruction; reports exist at the capital path) |

### `origin-work` (26)

| path:line | class |
|---|---|
| `SCORECARD.md:10` | labelled (resolver: first existing, then fail-closed `file=missing`) |
| `SKILL.md:91` | marked-historical ("relocated from `origin-work/`") |
| `SKILL.md:306` | labelled (first-existing candidate) |
| `LOG.md:52` | marked-historical (errata `:55-56` "the path above is historical") |
| `LOG.md:55` | marked-historical (the errata line) |
| `LOG.md:206` | marked-historical (relocation arrow, from → to) |
| `LOG.md:213` | marked-historical (before-survey: hardcoded path was the defect that was repaired) |
| `corpus/knowledge/consumer-registry.md:35` | marked-historical ("no longer exists") |
| `corpus/knowledge/consumer-registry.md:38` | marked-historical (names citations below as the relocated tree) |
| `corpus/knowledge/consumer-registry.md:79` | labelled (probe candidate list) |
| `corpus/knowledge/consumer-registry.md:106` | marked-historical (same line: "`origin-work/` path is historical") |
| `corpus/knowledge/consumer-registry.md:127` | marked-historical (checkout deleted; "origin-work tree additionally had") |
| `corpus/knowledge/consumer-registry.md:137` | marked-historical (same line: "path historical") |
| `corpus/knowledge/consumer-registry.md:193` | marked-historical (paragraph retracted at `:217`) |
| `corpus/knowledge/consumer-registry.md:198` | marked-historical (same paragraph; `git -C ~/Projects/origin-work/...`) |
| `corpus/knowledge/consumer-registry.md:206` | marked-historical (same paragraph) |
| `corpus/knowledge/listener-census.md:115` | marked-historical (same line: "path historical") |
| `corpus/knowledge/listener-census.md:122` | live |
| `corpus/knowledge/listener-census.md:270` | marked-historical (comment: "origin-work/ path historical") |
| `corpus/lessons/round-1.md:38` | marked-historical (same line: "historical path") |
| `corpus/lessons/round-1.md:69` | live |
| `corpus/lessons/round-4-recensus.md:20` | labelled (first-existing candidate; "re-repairing would be churn") |
| `registry/endpoint-consumers.tsv:14` | labelled (comment: first existing of) |
| `tools/kama-probe.sh:105` | labelled (usage text, first existing of) |
| `tools/kama-probe.sh:530` | labelled (comment: old root may exist again or not) |
| `tools/kama-probe.sh:546` | labelled (candidate walk, `[ -d ]` before use) |

### `webzites` (18)

| path:line | class |
|---|---|
| `MINT.md:25` | marked-historical (next sentence `:29` retracts "no longer exists") |
| `MINT.md:29` | marked-historical (errata line) |
| `LOG.md:170` | unresolved (`webzites-probe.timer` is a unit name, not a path; unit file absent) |
| `LOG.md:219` | marked-historical ("citations to deleted files … webzites second checkout") |
| `LOG.md:251` | marked-historical ("`~/Projects/webzites/` … are gone") |
| `corpus/knowledge/consumer-registry.md:53` | marked-historical ("does not exist"; rows historical) |
| `corpus/knowledge/consumer-registry.md:127` | marked-historical (same line: checkout deleted, historical evidence) |
| `corpus/knowledge/consumer-registry.md:189` | marked-historical (tree deleted, §Errata, *historical*) |
| `corpus/knowledge/consumer-registry.md:190` | marked-historical (tree deleted) |
| `corpus/knowledge/consumer-registry.md:194` | marked-historical (paragraph retracted at `:217`) |
| `corpus/knowledge/consumer-registry.md:202` | marked-historical (same paragraph) |
| `corpus/knowledge/consumer-registry.md:239` | labelled (errata `:53-55` names llm-wiki non-model rows; line itself has no deletion word) |
| `corpus/knowledge/consumer-registry.md:240` | labelled (same) |
| `corpus/knowledge/consumer-registry.md:241` | labelled (same) |
| `corpus/knowledge/consumer-registry.md:242` | labelled (same) |
| `corpus/knowledge/consumer-registry.md:330` | marked-historical (same line: tree deleted, historical) |
| `corpus/knowledge/listener-census.md:118` | marked-historical (checkout deleted 2026-10; historical) |
| `corpus/lessons/round-1.md:73` | marked-historical (errata: second checkout deleted) |

### `ds4cc-marketplace`, `plazir-15-site`, `~/.bailian`

Zero lines. Not even a nickname hit for `bailian` or `plazir-15-site` or `ds4cc-marketplace`.

Adjacent non-paths, not hits: `MINT.md:40` bare `ds4cc` (kake's remote surfaces, no path); `corpus/knowledge/listener-census.md:3` host `plazir27` (hostname, not `plazir-15-site`).

### `bench-arena` (8)

| path:line | class |
|---|---|
| `MINT.md:39` | unresolved (nickname in a roster cell, no path) |
| `SHONEN.md:20` | unresolved (nickname "bench-arena metrics scrape", no path) |
| `LOG.md:93` | labelled (round-1 adjacency cites `/home/vgpnk/bench-arena/loop.sh:5`; `:164` records the move; `:250` records the archive copy gone; line itself unmarked) |
| `LOG.md:164` | labelled (round-2: moved to `~/archive/bench-arena/loop.sh`; round 3 `:250` records that copy gone) |
| `LOG.md:250` | marked-historical ("`~/archive/bench-arena/loop.sh` … are gone") |
| `corpus/knowledge/consumer-registry.md:60` | marked-historical (deleted-since-round-2 list) |
| `corpus/knowledge/consumer-registry.md:110` | labelled (row 21 named historical at `:64`; cell still `FOREIGN_SERVICE`; file absent) |
| `corpus/lessons/round-1-citations.md:72` | live |

### the-janitor host paths

Path-shaped (38) plus shorthand not caught by the path regex (4): `SKILL.md:121`, `listener-census.md:177`, `listener-census.md:179`, `listener-census.md:294`.

| path:line | class |
|---|---|
| `SKILL.md:76` | live |
| `SKILL.md:78` | live |
| `SKILL.md:79` | live |
| `SKILL.md:121` | live (shorthand) |
| `SKILL.md:222` | live |
| `SKILL.md:292` | live |
| `LOG.md:46` | labelled (round-1 "live 2026-09-28"; deletion recorded at `:248`) |
| `LOG.md:47` | labelled (same) |
| `LOG.md:163` | labelled (round-2 line correction, present tense; directory gone at `:248`) |
| `LOG.md:248` | marked-historical ("are gone") |
| `corpus/README.md:29` | marked-historical (sentence continues `:31` "deleted or emptied") |
| `corpus/knowledge/alias-endpoint-normalization.md:56` | live |
| `corpus/knowledge/consumer-registry.md:58` | marked-historical (deleted-since-round-2 list) |
| `corpus/knowledge/consumer-registry.md:93` | labelled (row 4; errata names #1–#11; cell has no historical word) |
| `corpus/knowledge/consumer-registry.md:94` | labelled (row 5) |
| `corpus/knowledge/consumer-registry.md:95` | labelled (row 6) |
| `corpus/knowledge/consumer-registry.md:96` | labelled (row 7) |
| `corpus/knowledge/consumer-registry.md:97` | labelled (row 8) |
| `corpus/knowledge/consumer-registry.md:119` | live |
| `corpus/knowledge/consumer-registry.md:136` | live |
| `corpus/knowledge/consumer-registry.md:179` | live |
| `corpus/knowledge/cross-lane-scope.md:16` | live |
| `corpus/knowledge/cross-lane-scope.md:47` | live |
| `corpus/knowledge/drift-timeline.md:18` | live |
| `corpus/knowledge/listener-census.md:112` | live |
| `corpus/knowledge/listener-census.md:177` | live (shorthand `the-janitor:17`) |
| `corpus/knowledge/listener-census.md:179` | live (shorthand `the-janitor:15`) |
| `corpus/knowledge/listener-census.md:294` | live (shorthand) |
| `corpus/lessons/probe-mutation-matrix.md:4` | live |
| `corpus/lessons/probe-mutation-matrix.md:41` | live |
| `corpus/lessons/round-1-citations.md:33` | labelled (frozen command record) |
| `corpus/lessons/round-1-citations.md:43` | labelled (frozen MATCH record) |
| `corpus/lessons/round-1-citations.md:60` | labelled (frozen census output) |
| `corpus/lessons/round-1-citations.md:69` | live |
| `corpus/lessons/round-1-critic.md:240` | labelled (round-1 critic transcript command) |
| `corpus/lessons/round-1-critic.md:255` | labelled (round-1 verdict transcript) |
| `corpus/lessons/round-1-safety.md:61` | live |
| `corpus/lessons/round-1-safety.md:62` | live |
| `corpus/lessons/round-1-safety.md:73` | live |
| `corpus/lessons/round-1-safety.md:82` | live |
| `corpus/lessons/round-1.md:32` | marked-historical (past tense "were a shell script"; example, not an open instruction) |
| `corpus/lessons/round-1.md:83` | live |

Not path hits, listed so they are not dropped:

- `corpus/lessons/round-1-critic.md:104` — unresolved. Comment: `Host the-janitor` in `~/.ssh/config`. SSH alias, not a filesystem path. This seat did not open `~/.ssh/config`.
- `corpus/lessons/round-1-critic.md:258` — product name "the-janitor also pins", no path.
- `corpus/knowledge/consumer-registry.md:20` — present tense "the-janitor CLI still pin", no path. Superseded by §Errata `:56-58` in the same file. Not a path hit.

## Named debt

| Debt | Owner | Unblock |
|---|---|---|
| 46 unique live lines above | kama corpus / SKILL; parent appends errata | Name each live line historical, or case-correct rows 22–30 to `~/Projects/shokunin/...`. Do not rewrite filed round-1 text. Do not restore host files. |
| Labelled table rows whose cells still read `FOREIGN_SERVICE` (`consumer-registry.md:93-97`, `:110`, `:239-242`) | kama corpus | Optional: put `*historical*` on the cell. Errata already names the row numbers. Not required to clear the live set under this rubric. |
| `PROVINCE.md:10-11` deleted host pins outside this path set (`qwen-coder.service`, `opencode.json:158`, `agents/janitor.md:21`) | kama province; L0 if province contracts | Errata or province revision. Not a hit in the eight named classes. |
| Positive controls DEAD while pins `file=yes` | operator | Restart or replace `qwen-coder`. Not a dead-path citation. Do not re-repair `kama-probe.sh`. |
| `origin-work` fallback candidate | none | Already fail-closed. Re-repair would be churn. |

## Commands

```text
test -e <path>                         # exit 1 on every absent path listed above
stat -c '%n inode=%i' /home/vgpnk/Projects
                                       # /home/vgpnk/Projects inode=27238
test -e /home/vgpnk/projects           # exit 1
git -C kama-shokunin rev-parse HEAD    # 84a81304d7b0c77c84fe495f3bb728e8729faaff
```

Hit inventory was a full-tree line walk of `kama-shokunin` (patterns: `~/projects`, `/home/vgpnk/projects`, `origin-work`, `webzites`, `ds4cc-marketplace`, `plazir-15-site`, `bailian`, `bench-arena`, `.config/the-janitor`, `.local/bin/the-janitor`, `bin/the-janitor`, plus a second pass for `the-janitor` lines the path regex missed). No external fetch. No lane gate.
