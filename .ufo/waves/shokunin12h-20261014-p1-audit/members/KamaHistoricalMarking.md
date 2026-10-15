# Kama historical marking — advisory audit

Seat: KamaHistoricalMarking. Read-only. No lane file edited. No probe gate re-run (that seat owns the gates). This report is data, not a receipt.

## Cutoff

Wave-named commit: `84a81304d7b0c77c84fe495f3bb728e8729faaff` (2026-10-14 21:15:36 -0300, `kama-shokunin`, subject `round-4: OMP-era freshness re-census`).

First observation of this checkout: that commit was HEAD; `git status --porcelain` was only `?? plans/`.

At write time HEAD had moved:

- `47f3aedd6fa3ccfdde47a03c11f9e1342a7d8f7f` 2026-10-14 21:23:34 -0300
- `0505b718dde47f7a85088795626d494619d30198` 2026-10-14 21:23:45 -0300 (HEAD)

`git diff --stat 84a81304 HEAD` is three files: `LOG.md` (path pointer), `corpus/knowledge/endpoint-identity.md` (one line pin), `corpus/lessons/round-4-recensus.md` (path pointer + appended erratum). Worktree vs HEAD is clean except untracked `plans/` (not in either commit; not scored). Findings below are against HEAD `0505b71` unless a line says the named commit differed.

## Rule applied

Superseded revisions are described, not pinned as current. Historical content hashes may live in a round section of `LOG.md`. A content hash of a missing file must not be asserted as current identity. Counts, pids, line numbers, and snapshot ids presented as current were re-measured. A dated census or a round-section log entry is historical. An undated present-tense sentence in `SKILL.md`, `PROVINCE.md`, `SCORECARD.md`, or a current contract section is not.

## Missing-file content hash as current identity

**Holds.** No md5 or sha256 in the lane is the digest of a path that does not exist, asserted as that path's current identity.

| Pin | Where | What it matches | Current? |
|---|---|---|---|
| md5 `1f81e859c2d7f43f87d1f7e01327b2cf` | `SCORECARD.md:10` | `tools/kama-probe.sh` now, and the blob at `84a81304` / `ea72c3e` | yes |
| md5 `860f26ac05938cdfc1a8816eff1570b4` | `SCORECARD.md:11`, `LOG.md:117-118` | `tools/test-snapshot.sh` now; unchanged since `83bee7f` | yes |
| md5 `aa033020d99d2e271d2eb0499ab8281f` | `SKILL.md:300-301` | `registry/endpoint-consumers.tsv` now | yes |
| md5 `932ea3dc365e066e740731cf6a939506` | `LOG.md:13` (round 1 After) | `c6199a2:tools/kama-probe.sh` (788 newlines) | historical, correctly placed |
| md5 `87eb156b7cc36e98f3cbfb37c00f5351` | `LOG.md:14` | `c6199a2` registry blob | historical, correctly placed |
| md5 `61e82ee22dc89292175c5431f1ed6dc1` | `LOG.md:113-114` (round 2 shipped build) | `83bee7f:tools/kama-probe.sh` (1051 newlines) | historical in LOG; not current |
| sha256 `fd98f07a2d845a31cdf0582aa0faf9180e0903754b33248897a7e4211d9843da` | `LOG.md:119-120` | `83bee7f:registry/history/latest.tsv` | historical in LOG; current file sha256 is `f9f8f3b5bb1bfa61e6737a7fe95f7d7e0d0b53e287eb9c7fbe25d6cd0b7c2a2e` |
| sha256 `493afecbd6dd85df0f08f4541ecd340b03dc5df797a73bf8744cfd94edebab5a` | `LOG.md:121-122` | `83bee7f:registry/history/DELTA.md` | historical in LOG; current file sha256 is `e9e57b9abcbc9229a42a211be823c008de333e4dc7503095d00c3b454f6db280` |

`SKILL.md:315` `commit d7bd3bf` is a llama-server version string, and the sentence is marked `historical — files deleted`. The binary is absent. That is not a content digest of the missing file, and it is not asserted as current. Not a violation.

`5725fa7d3` / `0522e67a` in `corpus/lessons/round-1.md:69` are git abbreviations of trees that are gone. The next paragraph (`round-1.md:73-75`) marks the second checkout deleted and points at the current map. Not asserted as current HEAD. Current ufo HEAD is `964f443ee53df0ce06bd689af01f0dea031b01f9`.

## Claim-by-claim against the lane record

Lane record = `corpus/lessons/round-4-recensus.md` plus the current-evidence cells in `SCORECARD.md`.

| Lane claim | Verdict | Evidence |
|---|---|---|
| `$UFO_SRC` tree HEAD `964f443e` | **agree** | `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`; subject starts `routing: regenerate omp-seat-routing mirror` |
| `origin-work/ufo-fsd-alpha` gone; relocated tree exists | **agree** | `test -d ~/Projects/origin-work/ufo-fsd-alpha` exit 1; relocated dir exit 0; inode `41021` matches the errata |
| probe md5 `1f81e859…` and 1092 lines | **agree** on the hash and on `wc -l` | `wc -l tools/kama-probe.sh` → 1092; md5 matches. File has no trailing newline, so a logical-line count is 1093. Their own round-1/2 pins use the `wc -l` convention. Not a superseded pin |
| registry 3 data rows, md5 `aa033020…` | **agree** | data rows `omp-llama-cpp-default`, `ufo-fsd-thetick`, `ufo-fsd-local-helper` |
| `test-snapshot.sh` md5 `860f26ac…`, 171 lines | **agree** | `wc -l` 171; md5 matches |
| freshness snapshot `20261014T124232Z`, 16 transitions | **agree** | `registry/history/latest.tsv:1` is that id; `DELTA.md:7-22` is 16 transition lines (8 field changes + 8 `row-absent`) |
| re-measured ufo anchors (`the-tick.machine.json:12,:13,:16,:17-18`; `local-helper.mjs:8,:9,:155-161,:312,:325`; `THE-TICK.md:29`; `the-tick.test.js:61,:125,:1457`; `local-helper.test.js:263-266`; nightcall json `:135,:144`) | **agree** | each cited line still holds the claimed string. Old round-1 lines `the-tick.test.js:87` and `:1858` do not. `:18` is `"contextTokens": 16384` |
| `opencode.json` is 5 lines with no `qwen-local` | **agree** with the errata | `wc -l` 5; counts of `qwen-local`, `baseURL`, `8080`, `34113`, `localhost` are 0. Disagree with every unmarked `:158` citation listed below |
| `config.yml` has no loopback `baseURL` | **agree** with the errata | 0 lines match `127.0.0.1` or `localhost`. Disagree with the `:24 m_flash` pin |
| `SKILL.md` still teaches a live 11-row `MODEL_OK` world | **agree**, and the drift is wider than that sentence | lines below |
| `PROVINCE.md:10-11` owns deleted host pins | **agree** | unit missing; `janitor.md` missing; `opencode.json` has no line 158 |
| `endpoint-identity.md` cites `:481-487` for `schema-unrecognized`, and that range is the match path | **agree at `84a81304`; repaired at HEAD** | HEAD `endpoint-identity.md:19` cites `:516`. `kama-probe.sh:516` is `C_REASON=schema-unrecognized`. `:481-487` is the match path (`served_ids`, `MODEL_OK` case). Lesson `:31` still states the old debt; erratum `:35` records the fix. Other probe line pins in the same file were not repaired |
| describe-don't-pin holds for the lane | **disagree** | no missing-file content hash is pinned as current, but superseded counts, pids, line numbers, and one "current hash" sentence are still unmarked. Counterexamples below |
| gates (consumers 0, check 2, listeners 0, snapshot 24/0) | **not re-measured by this seat** | port probes below are consistent with DEAD on 34113/8080. Do not treat the lesson's gate line as this seat's measurement |

## Commands and exits (this seat)

```text
git -C kama-shokunin rev-parse HEAD
  first observation: 84a81304d7b0c77c84fe495f3bb728e8729faaff
  at write:          0505b718dde47f7a85088795626d494619d30198
git -C kama-shokunin status --porcelain
  ?? plans/
git -C kama-shokunin diff --stat 84a81304 HEAD
  LOG.md | endpoint-identity.md | round-4-recensus.md   7 insertions, 3 deletions
git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD
  964f443ee53df0ce06bd689af01f0dea031b01f9
test -d ~/Projects/origin-work/ufo-fsd-alpha ; echo $?
  1
stat -c '%n inode=%i' /home/vgpnk/projects
  exit 2, No such file or directory
stat /home/vgpnk/Projects /home/vgpnk/Projects/ufo-fsd-alpha
  inode 27238 / inode 41021
systemctl --user show qwen-coder.service -p LoadState -p ActiveState -p SubState -p MainPID
  LoadState=not-found ActiveState=inactive SubState=dead MainPID=0
  exit 0
ss -ltn | filter 34113,8080,8888,8790,8791,4226,9222,40993,43999
  only 127.0.0.1:631 and [::1]:631 among the probed set
curl -sS --connect-timeout 2 --max-time 2 -o /dev/null http://127.0.0.1:34113/health
  exit 7  Could not connect
curl … http://127.0.0.1:8080/health
  exit 7
curl … http://127.0.0.1:8888/health
  exit 7
curl … http://127.0.0.1:8790/health
  exit 7
curl … http://127.0.0.1:8791/health
  exit 7
wc -l tools/kama-probe.sh tools/test-snapshot.sh SKILL.md registry/endpoint-consumers.tsv registry/history/latest.tsv registry/history/DELTA.md
  1092 / 171 / 329 / 36 / 4 / 22
```

Named pids 1299, 1297, 2997, 2245, 2416, 836055, 1228, 3080080, 1207, 2360094, 801987, 1671602, 1668421, 1859348, 1053353, 3636400, 3467459, 816: `/proc/<pid>` absent for all. The listener-census table is date-stamped `Measured: 2026-09-28` (`listener-census.md:3`), so those pids are a sample, not a current-identity pin. Copies of them into undated `SKILL.md` sentences are the counterexamples.

`~/.local/bin/omp` still contains `LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080"` at newline-line 1149391. Cited line 1544771 is `}` and does not contain the string.

## Counterexamples (path:line)

Presented as current. Not inside a round-section log entry, and not marked historical on the sentence.

### Hash called current

- `corpus/lessons/round-1-citations.md:78` — "Round-2's current hash and behavior are pinned in `SCORECARD.md` and `LOG.md`." Round-2 probe md5 `61e82ee2…` is the `83bee7f` blob, not the file on disk. `SCORECARD.md:10` pins the later md5 `1f81e859…`. Line 77 correctly calls the round-1 hash historical. Line 78 does not. The file still exists; this is a superseded revision presented as current, not a missing-file digest.

### Counts presented as current

- `SCORECARD.md:12` — `SKILL.md` "(323 lines … 11 verbatim error signatures)". `wc -l SKILL.md` is 329 (logical 330; no trailing newline). 323 newlines is the round-2 blob (`83bee7f`). The error-signature table is 12 data rows (`SKILL.md:152-163`). The 12-row decision table, 11 anti-patterns, and 14-step checklist in the same cell still match.
- `SKILL.md:203` — `consumer_rows_evaluated=11 exit=0` "today". Registry data rows = 3.
- `SKILL.md:213` — `summary` `{"registry_rows_evaluated":11,"model_ok":3,"drift":8,"exit":2}` as "EXIT=2 today".
- `SKILL.md:264-265` — "`check` now evaluates **11** registry rows" and the census "holds **37**". Registry is 3. `consumer-registry.md` has 38 numbered rows (`| 1 |` through `| 38 |`).
- `SKILL.md:326` — "37-row census". Same table is 38 rows.
- `SKILL.md:186-188` — "The final tracked baseline ended `snapshot=20260929T043044Z … rows=11 model_ok=3`". Tracked `latest.tsv:1` is `20261014T124232Z` with 3 data rows. The same id under `snapshot-history.md:59-64` ("## Round-2 measurements") is historically marked and is not a counterexample.

### Pids and live verdicts presented as current

- `SKILL.md:33-54` — section "the live drift", pid 1299, Jitsi on 8080, `{"status":"ok"}` from 34113. All three ports refuse (curl exit 7). pid 1299 is dead. The date in the heading is 2026-09-28, but the body is present tense and is the operator worked example, not an errata.
- `SKILL.md:35-38` — "Six consumer surfaces still pin 8080". `janitor.md`, `distiller.md`, `the-janitor`, `the-janitor/opencode.json` are missing.
- `SKILL.md:66-67` — `opencode.json:158` "still reads `http://localhost:8080/v1`". File is 5 lines; those strings are absent.
- `SKILL.md:71-84` — current consumer table of those deleted files, plus fossil baks that are gone.
- `SKILL.md:90` — the-tick pin is `MODEL_OK`. Port 34113 refuses. The HEAD abbreviation on the same line is current. Split: HEAD agree, verdict disagree.
- `SKILL.md:95-96` — if the positive controls stop reading `MODEL_OK`, the probe is suspect. They are DEAD because nothing listens. That is the probe working.
- `SKILL.md:114` — `8790` = auth-broker pid 1297, `8791` = auth-gateway pid 2997. Both pids dead; both ports curl exit 7.
- `SKILL.md:161` — omp pids 3467459 / 1053353. Both dead.
- `SKILL.md:196-198` — pin classifications `34113` `MODEL_OK`, `8080` `FOREIGN_SERVICE`. Both refuse.
- `SKILL.md:222-223` — checklist items 12-13: grep deleted consumer files as "every live pin"; `MainPID` → `1299`. Unit is `not-found`, `MainPID=0`.
- `PROVINCE.md:10-11` — current owned surfaces are the missing unit and `opencode.json:158` / `janitor.md:21`. No historical marker. `SHONEN.md:17` says `PROVINCE.md` is still accurate; that accuracy claim is false for these two rows.

### Line numbers presented as current

- `SKILL.md:93` — the-tick census rows are `consumer-registry.md:54-55`. Those lines say the webzites checkout and row #38 are historical. The re-measured the-tick row is `consumer-registry.md:106`.
- `SKILL.md:101` — omp default cited at `consumer-registry.md:49`. Line 49 is the relocated remote map. The string claim is `consumer-registry.md:66-67`.
- `SKILL.md:120` and `SKILL.md:317` — `:24 m_flash: charm-hyper/deepseek-v4.1-flash:max`. `~/.omp/agent/config.yml:24` is a comment about effort suffixes. `m_flash:` is at `:433`, values `opencode-go/deepseek-v4.1-flash:max` and `devin/deepseek-v4-1-flash:max` (`:434-435`). No secret line was printed.
- `corpus/lessons/round-1.md:70-71` — "live line 24 is `m_flash: charm-hyper/…`". Same stale locator, present tense, no errata on this sentence.
- `corpus/knowledge/drift-timeline.md:24` — "the current `~/.config/opencode/opencode.json:158` retained `http://localhost:8080/v1`". No errata in this file. `:17` says "Current consumer still pins" inside a dated 2026-09-28 row; the date column anchors the row, but nothing says the timeline's last row is no longer live.
- `corpus/knowledge/consumer-registry.md:101` — row 12 locator `~/.local/bin/omp:1544771`. String is at newline-line 1149391. Errata `:66-67` correctly restates the string and does not repeat the line number; the table row still uses the old line as the locator.
- `corpus/knowledge/endpoint-identity.md:5` and `:97` — timeouts at `kama-probe.sh:47-48,83-85`. Those lines are persistence comments and the cleanup trap. Defaults are `:61-62`; help text `:107-108`; curl applies them at `:285`.
- `corpus/knowledge/endpoint-identity.md:9` — `kama-probe.sh:386` sends `GET /v1/models`. Line 386 is `[ "$found" -eq 0 ] && return 2`. The fetch is `:418`.
- `corpus/knowledge/endpoint-identity.md:9` — `--port`/`--expect` at `:80-85,723-733`. `:80-85` is `warn`/`die`/cleanup. Parse is `:120-123`. `--port` refusal is `:157-158`. `:723-733` is the resolver tail.
- `corpus/knowledge/endpoint-identity.md:13` — port 40961 with no listener at `listener-census.md:171`. Line 171 is the heading `## 4. Drift flags`. The 40961 row is `listener-census.md:179`.
- `corpus/knowledge/endpoint-identity.md:21` and `:127` — basename/`.gguf` normalization at `kama-probe.sh:32-34,338-350`. `:32-34` is an exit-code comment. `normalize_id()` is `:371`. `:338-350` is the python `group()` helper.
- `corpus/knowledge/endpoint-identity.md:97` — single identity fetch at `kama-probe.sh:253-256`. Those lines assign socket owners. The fetch is `:418` (one request, so the behavior may hold; the line pin does not).
- `corpus/knowledge/endpoint-identity.md:122` — `opencode.json:158` declares `http://localhost:8080/v1` as a current anti-pattern symptom. File has no such line.
- `corpus/knowledge/snapshot-history.md:15` — snapshot exit contract at `kama-probe.sh:932-1003`. That range is field diff through `flock`. `return "$exit_code"` is `:1071`.
- `corpus/knowledge/snapshot-history.md:21` — `snapshot --port` refusal at `:111-150`. Refusal is `:157-158`.
- `corpus/knowledge/snapshot-history.md:36` — row add/removal at `:833-903`. `row-added` is `:920`; `row-absent` is `:940`.
- `corpus/knowledge/snapshot-history.md:53` — userinfo/query/fragment strip at `:555-572`. That range is `expand_path`. The strip is `:609-612`.
- `corpus/knowledge/listener-census.md:284` — reproduction command expects inode `101125103` for `/home/vgpnk/projects`. That path is gone (stat exit 2). Line 283 was refreshed 2026-10-14; line 284 was not. `/home/vgpnk/Projects` inode `27238` still matches.

Not counterexamples (checked, contained or historically marked):

- `snapshot-history.md:39` cites `:932-1007`; the JSON-before-advance comment is at `:1005-1007`, inside the range.
- `snapshot-history.md:51` cites `:911-928`; `:925-926` states basename persistence.
- `snapshot-history.md:59-64` is under `## Round-2 measurements`.
- `LOG.md` round-1 and round-2 hashes match the commits named above and sit in those round sections.
- `endpoint-identity.md` census pins `:50-60` still land on the dated census rows they name.
- `listener-census.md` pid table is dated 2026-09-28. Not scored as current identity.
- HEAD `964f443e` pins in the errata, the lesson, `SKILL.md:91`, and the registry note. Still current.
- `endpoint-identity.md:19` at HEAD cites `:516`, which is the `schema-unrecognized` line. The named-commit pin `:481-487` is gone.

## Named debt

| Debt | Owner | Unblock |
|---|---|---|
| `SKILL.md` worked example, checklist items 2-13, anti-pattern 10, and the `:49`/`:54-55` corpus pins still describe the 2026-09-28 11-row `MODEL_OK` box | kama | Mark that section historical and point the checklist at item 1's already-updated 3-row DEAD lines. No operator action |
| `PROVINCE.md:10-11` owns deleted paths as current surfaces | kama | Replace the rows with surviving surfaces or mark them historical. Restoring the unit is a different debt |
| Probe line pins in `endpoint-identity.md` (`:5,:9,:13,:21,:97,:122,:127`) and `snapshot-history.md` (`:15,:21,:36,:53`) | kama | Re-anchor to the lines measured above. The `:516` fix does not cover these |
| `SCORECARD.md:12` line count 323 and 11 error signatures | kama | Refresh the depth evidence cell. `wc -l` is 329; signatures are 12 |
| `round-1-citations.md:78` calls the round-2 hash current | kama | Say round-2 hashes are historical; the current probe digest is the SCORECARD md5 |
| `drift-timeline.md:24` and `consumer-registry.md:101` stale locators | kama | Append an errata. Do not restore deleted files or rewind the omp binary to make the old lines true |
| `config.yml` `m_flash` is not line 24 and is not `charm-hyper/…` | kama for the citation; route change is outside kama's write boundary | Re-measure. Do not restore the old route |
| Positive controls `ufo-fsd-thetick` and `ufo-fsd-local-helper` are DEAD | operator | Restore a serving unit. The pins verify; the endpoints do not. This is the lane's own named debt, and this seat agrees. It is not a historical-marking defect |

Adjacency, not scored here: lowercase `~/projects/shokunin/...` does not resolve (`/home/vgpnk/projects` is absent). The capital-P `kengaku-shokunin/SKILL.md:322-323` still contains the cited 8080/34113 sentences; `PROVINCE.md:14` still names `127.0.0.1:34113`. Those are path-case citations for the dead-path seat. This seat did not re-derive the erratum's "46 unique lines" count.

`plans/wwkd-round-4-recensus.md` is untracked and not in `84a81304` or `0505b71`. Not scored.
