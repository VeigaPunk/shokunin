# Kengaku historical marking — advisory

Data only. Not a judge verdict, receipt, or admission. Read-only. No lane file edited. `grader.py` was not re-run (gate seat). `~/.config/opencode` was not content-read.

Lane HEAD `7153e671b1581a4b705583656883b6af158257df` (`round-16: OMP-era freshness re-census…`, 2026-10-14 21:15:36 -0300). That commit adds only `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-16-recensus.md`. `?? plans/` is untracked. Worktree otherwise clean.

## Criterion 3

**Disagree that describe-don't-pin holds on the living surface.** The round-16 lesson does not claim it holds. It says the absent host paths are still written as current in `SKILL.md` / `PROVINCE.md`, and that the round-15 "resolves" sentences must not be re-pinned. Independent measurement agrees with that confession and finds pins the lesson does not list.

**Agree** that committed in-repo evidence hashes are identities of files that still exist and still match. Those are not missing-file current-identity claims.

## What still matches (not counterexamples)

Recomputed 2026-10-14 from lane-root bytes. All matched.

| Pin | Path | Result |
|---|---|---|
| md5 `df154cb524bf210782fb0f4a46fd1bdc` | `corpus/evidence/round8-horizon/results.jsonl` | match |
| md5 `fc3b232ffc532717e50c1d06e0549acc` | `corpus/evidence/round8-horizon/run.log` | match |
| md5 `1c157e2a5f5cd3b8516d30c3d4a9c01d` | `corpus/evidence/round8-horizon/horizon.py` (349 lines) | match |
| md5 `33864062dbd7314300577f38c87f97cf` | `corpus/evidence/round8-horizon/critic-defects.md` | match |
| md5 `f3c58218da27cc6b05dca5a4e10d7f52` | `corpus/evidence/round9-replication/results-r9.jsonl` | match |
| md5 `d9235e41f3ebfdcabd368c71cde878a1` | `corpus/evidence/round9-replication/replication.md` | match |
| sha256 `2a4f62ef20a65e7a7cb3b7414b54d0f995126209c3126ae674b7cc3af2bc1099` | `corpus/evidence/round9-replication/predictions-r9.md` | match |
| md5 `c42fe3d10b6d7a1ed14c4485af03357b` | `corpus/evidence/round11-power/results-r11.jsonl` | match |
| md5 `281cb530702995854f162e807ee66ff3` | `corpus/evidence/round11-power/run.log` | match |
| md5 `146633599d66257d47320fbc8a6bf4f4` | `corpus/evidence/round11-power/analysis_r11.md` | match |
| sha256 `d7fbeebe…` / `ecfe96de…` / `e912085c…` | r11 bundle members | match `prereg-bundle.sha256` |
| sha256 `cf754d78…` / `f012ab6e…` | `probe_r11.py` / `run_r11.py` | match |
| md5 `9dd8aa2b6a7aa7890aa802c37d5af0f9` | `results-r12.jsonl` | match |
| md5 `700d1ddd2ece50d7bdedd55859c59f3a` | r12 `run.log` | match |
| md5 `029c3bcdcf11209d575734742bf239f6` / sha256 `1ceebd75…` | `analysis_r12.md` | match |
| r12 `prereg-bundle.sha256` lines 1–9 | nine named in-repo files | all match |
| sha256 `ad0511f2b8a49d3f9bd597afd0b99f46bf84b587af044c98150bdae92dd803f8` | `corpus/evidence/round10-fleet/mutate_test.sh` | match |

`predictions-r9.sha256.repo` names `predictions-r9.md` and matches. Living re-verify text (`corpus/README.md:72`) points at that file, not at `/tmp`.

`SCORECARD.md:277-285` records md5 `01547cfa…` of a raw-stripped `results.jsonl` and says no committed byte-image of that copy exists. The landed file's pin is the other digest. That missing-copy hash is marked as not current identity. Holds.

`SKILL.md:109-110` (`horizon.py:288`, `:277-279`) and `:393` (`horizon.py:314`) still describe the bytes at those lines. `run.log:81-83` is still the A-INC / A-MONO / A-CKPT summary. Not line-drift.

`grader.py` is 5737 lines, sha256 `90c87c8865022681b1249a42ea580726932d2e97ec0de43e0c89efe0e5ae941f`. The round-10 pin (936 lines, sha256 `ce64f16aeee54376296b874ae9e6ee49f4191174a416eed0299a1e8e56665e96`) lives in the dated round-10 log/scorecard rows (`LOG.md:17`, `SCORECARD.md:128`). It is not reprinted as the current grader. Not a current-identity claim.

`~/Projects/ufo-fsd-alpha` `rev-parse HEAD` is still `964f443ee53df0ce06bd689af01f0dea031b01f9`. The round-15 prefix `964f443e` is not yet a false pin. Do not mark it superseded.

Knowledge README rows 23 = 23 files. Anti-patterns in `SKILL.md` still 19; planning-horizon rules still 13. Those counts were not superseded.

## Host measure (2026-10-14)

Absent: `~/Projects/webzites`, `~/Projects/webzites/repos/llm-wiki`, `~/archive/bench-arena`, `~/bench-arena`, `~/wikillm/llm-wiki`, `~/Projects/bounties`, `~/Projects/bounties/ledger/telemetry.jsonl`, `~/Projects/origin-work`, `~/.bailian` (telemetry, wiki-sync-state, model index), `~/.config/systemd/user/qwen-coder.service`, `~/.config/llama/qwen-coder-godspeed.jinja`, `/proc/1299`. `~/projects/shokunin/CORPUS.md` absent; `~/Projects/shokunin/CORPUS.md` exists.

`connect_ex` 127.0.0.1:8080, :34113, :18099 → 111. `pgrep -a llama-server` → no rows. `systemctl --user status qwen-coder.service` text: `Unit qwen-coder.service could not be found.` (piped; bare exit not kept).

## Counterexamples (path:line)

Presented as current, or as durable identity, after the revision they name is gone or replaced. Dated round-tables that a later section withdraws are not in this list.

1. **`PROVINCE.md:8-14`** — surfaces table header is "re-verified round 14" and is the current province. `:12` offers `~/Projects/webzites/repos/llm-wiki` as the SSOT (only `~/wikillm/llm-wiki` is marked absent). `:13` says `tasks/`, `grade.sh`, `loop.sh`, and the report/telemetry CSVs **all resolve** at `~/archive/bench-arena/`, and "content no-drift (0 files newer than 2026-09-28)". The tree is absent, so that 0 is the vacuous-zero `find` already documented for the old path in `r14-scout-surfaces.md:170-176`. `:14` puts pid 1299 and `/proc/1299/cmdline` == the unit ExecStart (41 tokens, EXACT_MATCH) in the current surface row. No round-16 historical banner.

2. **`PROVINCE.md:16-17`** — `~/.bailian/telemetry.jsonl`, `wiki-sync-state.json`, and the model index/jsonl are current surface rows. No ABSENT mark. The directory is absent. Not a printed content hash. A current path+corpus claim.

3. **`PROVINCE.md:91-92`** — present tense: endpoint id, pid 1299, 41-token argv, q4_0 KV, `--kv-unified`, `--parallel 2` **remain exact matches**. Pid 1299 is gone; :34113 refused. `SCORECARD.md:208-216` already calls those pins capture-time. The province sentence was not marked.

4. **`PROVINCE.md:24-25`** — "no lane owns" the serving plane, present tense. `kama-shokunin/PROVINCE.md:10` still names `qwen-coder.service` / `:34113` as kama's owned artifact (also unmarked there; not this lane's file). The kengaku sentence is a superseded ownership claim left current. Lesson agrees. Not absorbed.

5. **`SKILL.md:8`** — "Source of truth: `~/Projects/webzites/repos/llm-wiki`" with no absence mark. Path absent.

6. **`SKILL.md:222-227`** — "Two distinct corpora exist" and the ledger is "`7,218` lines". Present tense in the procedure a reader runs. The cited-sources bullet at `:564` does mark the path ABSENT and says the counts are historical (last live count 7,226). The procedure section does not. `7,218` was already superseded by the round-9 recount `7,224` (`corpus/knowledge/ledger-route-telemetry.md:61-64`) before the file disappeared.

7. **`SKILL.md:237-241` and `:330` and `:565` and `:568`** — `~/archive/bench-arena/telemetry-qwenlocal-v2.csv` and `grade.sh` are the current battery/grade command. Cited-sources `:565` records the round-14 relocation and does not mark the archive absent. Tree absent.

8. **`SKILL.md:318-323`** — section heading is dated 2026-09-28, body is a current runbook: `qwen-local` "still points" at `localhost:8080` ("now Jitsi — listening but wrong"); "the live llama-server is `127.0.0.1:34113`". Both ports refused. Provider file not content-read, so the baseURL string itself was not re-measured. The listening claims were.

9. **`SKILL.md:412-413`** — "the same unchanged serving stack (pid 1299, argv re-pinned every round)". Present tense. Pid absent. `:450-451` dates the EXACT_MATCH to round 10, and `:462` says a restart invalidates the live pid. `:412` does not. The equality at `:451` is still an identity claim against two missing files (`/proc/1299/cmdline`, the unit). It is not a content hash. No content hash of the unit or the jinja file was found.

10. **`SKILL.md:56`** — anti-pattern 2 cites "shortlist note, lines 87–97" as the current source of that rule. The note lives under the absent wiki. Line numbers of a missing file, unmarked. In-repo line pins checked above still match; this one cannot.

11. **`SCORECARD.md:217-219`** — latest in-file host sweep says `~/archive/bench-arena` resolves and `~/Projects/webzites/repos/llm-wiki` resolves. Round 16 did not append an erratum next to those lines. The lesson (`corpus/lessons/round-16-recensus.md:29-30`) says current truth is negative and do not re-pin. That mark is not on the sentences. Both paths absent. Agree with the lesson's "do not re-pin"; disagree that the scorecard lines are marked.

12. **`SCORECARD.md:301-303`** — standing Confidence bullet, no round qualifier: "All 149 checks recompute…". The 733-check figure is the next bullet (`:342`), not this one. 149 is the pre-extension gate size. A reader of `:302` takes it as what PASS means now. Not re-executed here.

13. **`corpus/README.md:117`** — open-gaps standing line: the live tree relocated to `~/archive/bench-arena` "with content hashes unchanged" and "Living surface pointers use the archive path". Both trees absent. This is the living assertion that the missing archive's content hashes are still its current identity. The hex is not reprinted here.

14. **`corpus/evidence/round14-fleet/r14-scout-surfaces.md:209-218`** — "New durable md5 pins" of `~/archive/bench-arena/{grade.sh,loop.sh,telemetry-qwenlocal-v2.csv,report-qwenlocal-v2.v2.csv,report-qwenlocal.csv,report-grok45.csv}`: `a15b02f52d4459d0d198bf70b333d357`, `44427e241574ba23a712faae661484f3`, `dac11874502f7f3f05fb725035294d4e`, `c3bd7efe22630dcc6c47e8fa26f66235`, `57aab8982dcfc18c9d4b29b61acc380e`, `e0a42a2f1ab649f4430ebc5b2e380959`. Those paths are absent. No later line withdraws "durable". Round 16 did not edit this file. This is the printed content hash of missing files left as identity. `r10-scout-bench.md:17-24` is the earlier capture of the same digests at `~/bench-arena/`; round 14 already marked that prefix absent (`:170-176`). The r10 lines are a dated capture. The failure is the durable table plus `README.md:117`, not the r10 block alone.

15. **`corpus/knowledge/ledger-route-telemetry.md:3-5` and `:61-65`** — opening still calls the ledger "the host's live lane-routing corpus" at 7,218 lines. The round-9 errata says `:3` is a point-in-time count of a "live, growing surface" and records 7,224. That errata does not know the round-11 disappearance. `SKILL.md:564` marks the path absent; this note does not.

16. **`corpus/knowledge/bailian-cli-telemetry.md:3-6`** and **`local-model-index.md:3`** — source paths under `~/.bailian` with snapshot counts (4,274 records; 180 families / 413 models) and a `contentHash` field name, no printed hash, no absence line. Dated "profiled/verified 2026-09-28", which is a partial mark, not a withdrawal. Province rows `:16-17` are what make them current surfaces.

17. **`corpus/knowledge/bench-arena-fresh-run.md:6-17`** — "Harness facts (verified live)": 8080 occupied by Jitsi, llama-server listens on 34113. Both refused. The round-10 errata at `:72-80` repeats "the port facts reproduce exactly" and "false today" inside a section titled as a round-10 append. The header dates the errata; nothing withdraws it after the ports died.

## Residue, not a living current-identity claim

`corpus/evidence/round9-replication/predictions-r9.sha256:1` is `2a4f62ef…  /tmp/kengaku-r9/predictions-r9.md`. That path is absent. The same digest matches the committed `predictions-r9.md`. Living re-verify (`corpus/README.md:72`, knowledge note) uses `predictions-r9.sha256.repo`, whose target exists. Do not treat the `/tmp` checksum line as the current file. Do not re-pin it.

`corpus/README.md:4` cites `~/projects/shokunin/CORPUS.md` (lowercase). That path is absent; the capital-P file exists. Wrong-case contract path, not a hash pin. Dead-path seat, not re-pinned here.

Lessons index is 17 README rows and 18 files (`round-16-recensus.md` unindexed). `SCORECARD.md:161` "17/17" is a rounds-12–14 movement row, not restated after round 16. Record seat. Not a current-identity hash.

## Lane-record verdicts

| Lesson / record claim | Verdict |
|---|---|
| Host surfaces gone; still written as current in `SKILL.md` / `PROVINCE.md` (`round-16-recensus.md:23-26`) | **Agree.** Measured absent. Sentences above are still present tense. |
| Round-15 "resolves" sentences: current truth negative, do not re-pin (`:29-30`) | **Agree** on the facts. **Disagree** that the scorecard lines are marked. `SCORECARD.md:217-219` still says resolves. |
| `:34113` / pid 1299 historical (`SCORECARD.md:208-216`) | **Agree** for that paragraph. **Disagree** that the province and skill runbook inherited the mark (`PROVINCE.md:14`, `:91-92`, `SKILL.md:412`). |
| In-repo md5/sha256 pins of committed probe bytes | **Agree** they identify files that exist. Recomputed match. |
| `grader.py` 936 / `ce64f16a…` as current grader | **Not claimed** by a living sentence. Dated round-10 row only. Current file is the 5737-line digest above. |
| `964f443e` as ufo-fsd HEAD | **Still true** today. Not a superseded falsehood. |
| Gate lines `n=733` / selftest ALL PASS (`round-16-recensus.md:8-10`) | **Not re-run.** No agree/disagree on the verdict line. |

## Named debt

| Item | Owner | Unblock |
|---|---|---|
| Living SKILL/PROVINCE/README/knowledge sentences in items 1–10, 13, 15–17 | kengaku record (append-only). Do not rewrite the historical sentences. | Append a describe-don't-pin banner: capture-time counts, pids, and line cites; path absent; do not copy the number forward. |
| `SCORECARD.md:217-219` still says resolves | kengaku record | Append next to those lines. Lesson already says do not re-pin. Do not invent a new hash. |
| Archive md5 table `r14-scout-surfaces.md:209-218` left as durable identity of missing files | kengaku record, append-only on the evidence file or on the README open-gap | Mark the six digests as 2026-09-29 capture hashes. Do not re-hash a missing tree. Do not assert them as the current identity of `~/archive/bench-arena`. |
| Serving-plane "unowned" vs kama `PROVINCE.md:10` | kengaku for the "unowned" sentence; kama for its own unit row; operator for the unit | Describe capture-time argv. Do not restore the unit from this lane. |
| `qwen-local` baseURL string | not measured (config not content-read) | Whoever may read `~/.config/opencode` under the secrecy rule. Listening claims do not need that read: both ports refused. |
| Lessons index short one row | record-conformance seat | Not a hash. Do not "fix" by pinning 17. |

## Commands (this seat)

From `/home/vgpnk/Projects/shokunin/kengaku-shokunin` unless noted.

- `git rev-parse HEAD` → `7153e671b1581a4b705583656883b6af158257df`; `git status --porcelain` → `?? plans/`.
- `git show --stat 7153e671…` → 3 files, +43.
- Host `is_file`/`is_dir` over the paths in "Host measure" → ABSENT as listed; `~/Projects/ufo-fsd-alpha` is a directory.
- `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`.
- Python `socket.connect_ex(("127.0.0.1", port))` for 8080, 34113, 18099 → 111, 111, 111.
- `sha256sum grader.py` → `90c87c8865022681b1249a42ea580726932d2e97ec0de43e0c89efe0e5ae941f`; `wc -l grader.py` → 5737.
- In-process md5/sha256 of the pin table above → all match. `prereg-bundle.sha256` (r11 and r12) targets exist and match.
- `find corpus/knowledge -maxdepth 1 -type f | wc -l` → 23; README knowledge rows → 23. Lessons files → 18; lessons rows → 17.

Not run: `python3 grader.py`, `python3 grader.py --selftest`, any `sha256sum` of a missing host file, any read of `opencode.json`.
