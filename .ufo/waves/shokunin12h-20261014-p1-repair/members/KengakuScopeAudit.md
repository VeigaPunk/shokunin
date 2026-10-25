# KengakuScopeAudit — baseline scope audit

Advisory only. Not a native judge verdict, not a lane round report, not a receipt, and not an admission. No lane file was edited. `grader.py` was not run.

Axes: freshness, operability, calibration, adjacency.
Milestone context: independent freshness re-census at steered round 16. This is the baseline inventory, not the post-integration acceptance wave.

## Identity measured

| Item | Measurement |
|---|---|
| Lane HEAD | `d84e48d525d6af6b1d137d608aea8c726f8bead4` (`git rev-parse HEAD`; `git log -1` = `2026-10-14 09:41:08 -0300` `round-15: OMP/ufo-fsd re-census — substrate drift does not reach this lane`) |
| Worktree | `git status --porcelain` = `?? plans/` only. `grader.py` not dirty. |
| `grader.py` | 5737 lines, 274855 bytes, sha256 `90c87c8865022681b1249a42ea580726932d2e97ec0de43e0c89efe0e5ae941f`. Re-hashed after `members/KengakuGateRepair.md` existed; digest unchanged. |
| Captured gate (not re-run) | `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kengaku-before.json`: argv `python3 grader.py`, exit 0, `CHECKS n=733 mismatches=0 errata_pinned=1`, revision `d84e48d`, finished `2026-10-14T23:34:59.554552+00:00`. |
| Round-15 diff | `git show --stat HEAD`: `LOG.md` +1, `SCORECARD.md` +50. `PROVINCE.md`, `SKILL.md`, `SHONEN.md`, `corpus/README.md`, and `grader.py` were not in that commit. |

LSP: `xd://lsp` is not mounted. Caller, definition, and diagnostics checks were not available. Path and token evidence below is literal (`git grep`, file reads, `test`-equivalent existence). It is not semantic proof of references.

## What the gate actually covers

`grader.py` has no `--src`, no `UFO_SRC`, and no `ufo-fsd` / `origin-work` string (`grader.py` token counts: `--src` 0, `UFO_SRC` 0, `ufo-fsd` 0, `origin-work` 0). Defaults are ten in-repo evidence paths (`grader.py:66-77`). Sidecars are joined from the script directory or from `_find_repo_root()` (`grader.py:78-80`, `811-824`, `1504-1511`).

`_find_repo_root()` (`grader.py:811-821`) walks at most three parents for `corpus/evidence/round11-power/` and otherwise returns the script directory. It does not consult `$UFO_SRC`, `~/Projects/ufo-fsd-alpha`, or `~/Projects/origin-work/ufo-fsd-alpha`. At the current checkout the script directory itself qualifies, so the walk binds this repo. A missing required sidecar dies with exit 2 (`grader.py:5699-5705`). That is fail-closed for absent in-repo inputs. It is not an external source-root resolver, and it should not be given one.

Pin skip is explicit and narrow: non-default `--r8-*`/`--r9-*`/`--r11-*`/`--r12-*` paths skip md5 pins (`grader.py:5508-5512`, `4004-4016`; living description at `SKILL.md:486-490`). `check_r12_ordering` is still called with only the overridden jsonl (`grader.py:5716-5719`); bundle hashes and script hashes stay on `REPO_ROOT` (`grader.py:3926-3953`). An explicit missing path fails closed. An explicit existing wrong path is graded as a mutated copy, not as a second source tree.

`ERRATA` has one key, `r9.failure_classes.state_error` (`grader.py:103-113`). That matches the captured `errata_pinned=1`. Round-13 strings `85.9`, `330/384`, `round13`, `ack-state`, and `0.047` occur 0 times in `grader.py`.

In-repo evidence directories named by `PROVINCE.md:18` all exist (file counts): round8-horizon 4, round9-replication 8, round9-fleet 19, round10-fleet 22, round11-power 12, round11-fleet 18, round12-ladder 18, round12-fleet 22, round13-ack-state 2, round14-fleet 10. `corpus/README.md` index parity holds: knowledge 23/23, lessons 17/17, evidence rows 10/10, no unindexed or dangling rows.

Preserved and still true of the gate: hermetic replay of four trees; no ufo-fsd I/O; captured PASS is a self-agreement of committed probe bytes, which `SCORECARD.md:301-303` already says does not mean the model was live. That sentence is scoped to the round-10 149-check gate; the principle still matches the current I/O.

## Findings

### High — living province table still asserts surfaces that do not resolve

`PROTOCOL.md:411` requires declared surfaces to resolve, and a moved or absent surface to be corrected in `PROVINCE.md` and logged. The surface table header is still "re-verified round 14, 2026-09-29" (`PROVINCE.md:8`). Round 15 did not edit `PROVINCE.md`.

Existence checks this session (shape only; no file contents; no secret/session read):

| Declared surface | Living claim | This-session result |
|---|---|---|
| Research notes | `PROVINCE.md:12` `~/Projects/webzites/repos/llm-wiki` resolves; `~/wikillm/llm-wiki` absent | Both **ABSENT**. `~/Projects` listing (30 names) has no `webzites`. |
| Benchmark battery | `PROVINCE.md:13` `~/archive/bench-arena/` resolves, including `tasks/`, `grade.sh`, `loop.sh`, `report-grok45.csv`, `report-qwenlocal*.csv`, `telemetry-qwenlocal-v2.csv`; content no-drift vs 2026-09-28 | `~/archive` **ABSENT**. `find /home/vgpnk/archive/bench-arena` → `No such file or directory`. `~/bench-arena` also **ABSENT**. |
| Served model | `PROVINCE.md:14` present-tense `http://127.0.0.1:34113` plus pid 1299 / `qwen-coder.service` process pin | `curl -sS -m 5 http://127.0.0.1:34113/health` and `/v1/models` → HTTP 000, curl exit 7, connect failed. `pgrep -a llama-server` empty. `ps -p 1299` empty. `ss -ltn` has no `:34113`. `~/.config/systemd/user/qwen-coder.service` **ABSENT**. No `qwen`/`llama` unit name in that directory. |
| Route telemetry | `PROVINCE.md:15` marked **ABSENT** | Still **ABSENT**. This row is the one honest historical marker. |
| Client CLI telemetry | `PROVINCE.md:16` `~/.bailian/telemetry.jsonl`, `wiki-sync-state.json` | `~/.bailian` **ABSENT**. Not content-read. |
| Model catalogs | `PROVINCE.md:17` `~/.bailian/skills/bailian-docs-llm-wiki/models/{index.md,models.jsonl}` | Both path readings **ABSENT** (`models/models.jsonl` and `models.jsonl`). Remote HF/OpenRouter URLs were not fetched (wave forbids external fetches). |
| Own probe artifacts / in-repo gate | `PROVINCE.md:18-19` | In-repo paths exist. Gate I/O claim matches the source. |

Negative relocation sweep (name only, not a full-disk search): `find /home/vgpnk /scratch /tmp /mnt /opt /srv -maxdepth 5 \( -name llm-wiki -o -name bench-arena -o -name bailian -o -name webzites -o -name qwen-coder.service -o -name origin-work \)` printed no hits. `findmnt` had no archive/webzites/bailian/bench/wiki mount. Trash name sweep to depth 3 had no wiki/bench/bounty/bailian hits. The only `telemetry.jsonl` hit was `/home/vgpnk/.prime/agent/telemetry.jsonl` (exists, file, **not content-read**). That is a name collision, not `~/Projects/bounties/ledger/telemetry.jsonl`. Do not retarget the citation.

Cited wiki files under the declared SSOT, including every `SKILL.md:556-561` bullet and `wiki/ai/foundations/bitter-lesson.md`, are absent because the parent tree is absent.

Round 15's own scorecard still says the opposite for two of these rows: `SCORECARD.md:217-219` records `~/Projects/ufo-fsd-alpha`, `~/archive/bench-arena`, and `~/Projects/webzites/repos/llm-wiki` as resolving. ufo-fsd-alpha still resolves (below). The wiki and archive claims do not. `~/Projects` mtime is `2026-10-14 19:02:04 -0300` and `/home/vgpnk` mtime is `2026-10-14 19:30:32 -0300`, both after the round-15 commit (`09:41:08 -0300`) and before the captured gate receipt (`23:34:59Z` = `20:34 -0300`). Those mtimes are not a deletion log for a named child. They bound a host change in that window; they do not prove which entry changed. Current existence is the ground truth for this audit.

Counterexample to "grader PASS ⇒ province fresh": the captured gate exited 0 at `23:34:59Z` while this audit's later existence checks, and the pre-receipt directory mtimes, show the declared host surfaces already outside the gate. A green 733-check replay cannot see an absent `~/archive` or an absent wiki.

Proposed delta (parent / record prep, not GateRepair): append a dated `PROVINCE.md` surface erratum. Mark llm-wiki, `~/archive/bench-arena`, both bailian files, the local model-index paths, and `:34113` / `qwen-coder.service` **ABSENT** as of this measurement, with the sweep command. Do not invent a replacement path. Do not rewrite round-14 historical pins or the round-11 bounty paragraph in place. Log the correction (parent-owned). Unblock: operator restores or explicitly retires each surface.

Cross-domain owner: path restoration is operator-side. Endpoint/process liveness, if restored, is kama (below), not this gate.

### High — "no lane owns the serving plane" is a stale boundary

`PROVINCE.md:24-25` still says the model-serving plane is not owned and "no lane owns it." Round-10 through round-14 report-outs repeat "integrator / unowned serving plane" (`PROVINCE.md:43-48`, `67-72`, `90-92`). `git grep kama` in this lane does not hit `PROVINCE.md`.

Measured elsewhere, read-only:

- `MANIFEST.json:55-57` roster id `kama`, domain "local model serving & endpoint health".
- `ROADMAP.md:13` lists `kama-shokunin` on the roster.
- `kama-shokunin/PROVINCE.md:3-20` owns local serving processes and ports, names `~/.config/systemd/user/qwen-coder.service` and `127.0.0.1:34113`, and refuses model quality/eval (kengaku). Write boundary: kama does not edit systemd units.
- `kama-shokunin` HEAD `ea72c3e` (`2026-10-14 09:46:23 -0300`).

`SCORECARD.md:298-300` still says the kama mint decision is integrator-pending. That matched `ROADMAP.md:90-94`, which still says "decision pending" under Candidate domains even though the roster table already lists kama. The pending sentence is integrator-doc drift. It is not a reason for this lane to keep "unowned."

`corpus/evidence/round14-fleet/r14-connector.md:7` surveyed only kagi, kotoba, kumitate, kasegi, and kake. Kama was outside that negative-ownership search. The "unowned" ruling is not current-HEAD-scoped against the minted owner.

Living skill text still instructs the old plane as current procedure, not as a capture:

- `SKILL.md:318-323` "verified 2026-09-28" then present tense: live llama-server is `:34113` via `qwen-coder.service`; `qwen-local` "still points at `localhost:8080` (now Jitsi — listening but wrong)."
- `SKILL.md:330` `bash ~/archive/bench-arena/grade.sh` as the grade command.
- `SKILL.md:222-236` "verified on this host, 2026-09-28" presents `~/Projects/bounties/ledger/telemetry.jsonl` (7,218 lines) and `~/archive/bench-arena/telemetry-qwenlocal-v2.csv` as the two corpora that exist. No ABSENT marker in that section.

Port check: `curl` to `127.0.0.1:8080/` and `:8080/health` also HTTP 000 / curl exit 7. `ss -ltn` has no `:8080`. So the skill's "listening but wrong" contrast is also not the current listener state. `~/.config/opencode/opencode.json` exists (file). It was **not content-read** (credential-shaped consumer config; kagi/kama). This audit does not confirm or deny the `qwen-local` baseURL byte.

The cited-sources bullet does mark the ledger absent (`SKILL.md:564`). The operating section a reader would follow (`SKILL.md:222-236`) does not. That is a preserved historical claim interpreted as live.

Proposed delta: append, do not rewrite, a province boundary note: process/port/liveness is kama's; kengaku keeps historical capability interpretation of committed descriptors (pid 1299, q4_0 KV) as capture-time, which `SCORECARD.md:308-311` already limits. Append a SKILL banner on `SKILL.md:222` and `:318` that those procedures are 2026-09-28 capture, not a live runbook, until the named surfaces resolve. Do not absorb kama's probe registry or edit `~/.config`.

Cross-domain owner: kama for serving-plane liveness; kagi for consumer credential config; operator for unit restore. Integrator for the contradictory `ROADMAP.md:90-94` vs roster row.

### Medium — round-15 census classified the wrong inventory

`SCORECARD.md:188-200` and `LOG.md:22` say substrate drift never reached this lane, classification (a) stale `--src` (b) citation-to-deleted (c) line-drift (d) genuine defect = 0/0/0/0, and "nothing to re-derive and nothing to repair."

That is true of a narrow object, and false as a province census:

- True: `grader.py` has no `--src` and no ufo-fsd path. `git grep UFO_SRC` in the lane is empty (exit 1). `git grep ufo-fsd` hits only LOG, SCORECARD, `PROVINCE.md:55` (read-only rule), `corpus/evidence/round10-fleet/INTEGRATOR-NOTES.md:72`, and `corpus/evidence/round9-fleet/sibling-overlap.md:13`. None is a file:line citation into the ufo tree.
- True and re-measured: `~/Projects/origin-work` ABSENT. `~/Projects/ufo-fsd-alpha` EXISTS. `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` = `964f443ee53df0ce06bd689af01f0dea031b01f9`, which matches the recorded short hash `964f443e`. Commit subject `routing: regenerate omp-seat-routing mirror...` dated `2026-10-12 18:32:12 -0300`.
- Unprovable, not passed: "~50 upstream files deleted" (`SCORECARD.md:187`, `LOG.md:22`) has no counting command in the lane. Not re-derived here.
- False if read as "no living citation is stale": the same round-15 section claims wiki and bench-arena resolve (`SCORECARD.md:218-219`) and does not correct `PROVINCE.md` for the `:34113` absence it does record (`SCORECARD.md:208-216`). `PROTOCOL.md:411` made that a required correction. Round 15 edited only LOG and SCORECARD.

Survey method counterexample: `SCORECARD.md:196` says `grep -rln origin-work` had 1 hit (`r14-scout-surfaces.md`). Current `git grep -l origin-work` hits 3 files (`LOG.md`, `SCORECARD.md`, `r14-scout-surfaces.md`) because the erratum added mentions. The "1 hit" figure is a pre-edit snapshot, not a property of the tree a later reader greps. `r14-scout-surfaces.md:137` and `:148` were correctly left verbatim; the scorecard erratum (`SCORECARD.md:221-225`) is the right append-only shape. The method is not a stable absence proof after the write.

Implicit source assumption: "no `--src` ⇒ host drift cannot affect this lane." Counterexample is the declared SSOT `SKILL.md:8` / `PROVINCE.md:3`, which is llm-wiki, not ufo-fsd. The gate never opens it, so a deleted wiki cannot fail `grader.py`, and the round-15 taxonomy never looked.

Proposed delta: do not rewrite the round-15 0/0/0/0 lines. Append an erratum that those counts are ufo-fsd `--src`/deleted-file/line-drift counts for this lane's gate, not a province-surface census. Parent records the new absences as named debt, not as a fabricated axis improvement.

Cross-domain owner: parent for the scorecard/log append. Not GateRepair.

### Medium — citation inventory does not carry absence next to the claim

`corpus/knowledge/ledger-route-telemetry.md:3-7` still calls `~/Projects/bounties/ledger/telemetry.jsonl` the host's live lane-routing corpus. The round-9 erratum (`:59-65`) says the 7,218 count is a point-in-time count of a "live, growing surface" and tells the reader to re-run `wc -l` before citing a total. There is no later erratum that the path went absent in round 11. Re-running that command now fails closed on a missing file, which the entry does not say.

`corpus/README.md:17` says "Live lane-routing corpus" and "(now absent)" in the same cell. `corpus/README.md:117` still says living pointers use `~/archive/bench-arena`. `corpus/knowledge/local-bench-arena.md` source line still cites `~/bench-arena/` (historical path, already known relocated, and now the archive path is absent too). `corpus/knowledge/local-model-index.md` and `bailian-cli-telemetry.md` cite `~/.bailian/...` with no absence note.

`CORPUS.md` / `LEARNING.md` ask each knowledge entry to open with `source:`, `verified-at:`, and `recheck:`. Of 23 knowledge files, none of the first eight lines carried `verified-at`. Only `bench-arena-round12-ladder.md` carried a `recheck` token in that window. `corpus/QUALITY.md` is absent. Historical-versus-live is therefore a prose convention, not a check the gate or a quality file can fail.

Case counterexample, separate from ufo-fsd line-drift: `corpus/README.md:4` cites `~/projects/shokunin/CORPUS.md`. `test`-equivalent: that path is **ABSENT**. `~/Projects/shokunin/CORPUS.md` **EXISTS**. `/home/vgpnk/projects` is absent and is not a symlink. Token counts of host-path mentions: living-contract docs 53, corpus knowledge/lessons 61, append-only LOG/SCORECARD 63, historical evidence 372. The lowercase `~/projects` form is the fleet pointer that does not resolve on this case-sensitive host.

`PROVINCE.md:79` (round-11 report-out) says `~/Projects/the-bounty-hunter/` exists. That directory is now **ABSENT**. The paragraph is dated, but it is present tense. Treat as historical narrative, not a surface-table row; still do not cite it as current.

`SHONEN.md:11-12` box 4 (`[~]`, author assertion) says surfaces were re-verified round 14 with endpoint/process pin EXACT_MATCH and the benchmark tree relocated intact to `~/archive/bench-arena`. As a current checklist statement that is false. Do not flip it to `[x]`.

Proposed delta: append absence errata to the ledger knowledge entry and the README index/gap lines. Point `corpus/README.md:4` at `~/Projects/shokunin/CORPUS.md` or spell the case split. Leave evidence bodies verbatim. RecordPrep may draft the SHONEN wording; a non-author has to mark any `[x]`.

Cross-domain owner: kasegi for ledger recovery; operator for bailian and bench-arena trees; aggregator if `QUALITY.md` / `verified-at` is to become a fleet check. Not this gate.

### Low — gate coverage holes that are honest if named, defects if the gate is read as a citation gate

1. Round-13 ack-state (2 scripts, headline rates in `LOG.md:20` and `SCORECARD.md:353-355`, and the planned next move at `SCORECARD.md:248-261`) is outside `grader.py`. Corrupting those rates does not change the 733-check verdict. `PROVINCE.md:19` already limits the gate to four trees. Keep that limit. Do not silently widen the gate in this wave.
2. Overriding `--r12-jsonl` to another directory does not retarget `prereg-bundle.sha256` or `probe_r12.py` (`grader.py:3926-3953`). A relocated study tree is not graded by flags alone. Documented pin-skip (`SKILL.md:489-490`) is not a source-root API.
3. `_find_repo_root` would bind a nearer ancestor that also contained `corpus/evidence/round11-power` if this file were nested. It is not nested today. Not a live mis-bind. Do not "fix" it by adding a ufo-fsd fallback.

Proposed delta for GateRepair: none. No reproduced default-path defect. Adding `$UFO_SRC` → `~/Projects/ufo-fsd-alpha` → `~/Projects/origin-work/ufo-fsd-alpha` would invent a source dependency this lane does not have and would absorb kumitate/ufo scope. Explicit bad evidence paths already die. Leave `grader.py` unchanged.

## Unresolved debt

| Debt | Unblock | Owner |
|---|---|---|
| llm-wiki SSOT absent; no relocation inside the depth-5 sweep | Operator restores `~/Projects/webzites/repos/llm-wiki` or retires the surface in PROVINCE | Operator; lane appends the marker |
| `~/archive` and both bench-arena paths absent | Operator restores or retires; do not re-pin hashes from memory | Operator |
| `:34113`, pid 1299, `qwen-coder.service` absent; `:8080` also closed | Operator restores the unit; kama re-probes. Kengaku does not edit systemd | Operator + kama |
| `~/.bailian` absent | Operator restores or retires catalog/telemetry surfaces | Operator |
| Bounty ledger absent since round 11; `.prime` telemetry.jsonl is not a substitute | Operator/kasegi recover the ledger tree; do not content-read `.prime` | kasegi / operator |
| Serving-plane "unowned" text | Append kama ownership; do not take flag-change authority | kengaku record + kama |
| `ROADMAP.md:90-94` still "mint pending" while roster lists kama | Integrator appends the mint ruling; lanes must not edit ROADMAP | Integrator |
| "~50 upstream files deleted" | Not re-derivable from lane records; leave unprovable | Whoever holds the original deletion command; not this lane |
| Round-13 rates outside the gate | Future novelty round may extend the gate in the same round as a new probe; not this repair | Lane, later round |
| No `verified-at` / `QUALITY.md` | Corpus contract gap; do not pretend the 733-check gate is that check | Aggregator / lane corpus round |
| Wiki/bench absence vs round-15 "resolves" | mtime bound is not a deletion identity. Do not backdate a cause | Operator host log, if any |

## Residual risk

A later reader can still treat `SKILL.md:318-330` as a runbook and call a missing `grade.sh`, or treat `PROVINCE.md:14` as a live process pin. The captured PASS will not catch that. Remote catalog URLs (`PROVINCE.md:17`, `SKILL.md:567`) were not re-checked; "verified live 2026-09-28" (`SKILL.md:343`) must stay dated. Committed probe statistics (r8/r9/r11/r12) remain internally re-derivable by the gate; that does not transfer to host surfaces or to round-13 rates.

`analysis_r12.md` path-case erratum (`/home/vgpnk/projects` vs `Projects`, `SCORECARD.md:168-170`) is the same case split as `corpus/README.md:4`, already named for the analysis file and still live for the README pointer.

## Verification gaps

- Did not run `python3 grader.py`, `--selftest`, or `--selftest-r12` (wave: no tests while edits are in flight). Gate verdict cited only from the captured before receipt.
- No LSP diagnostics.
- Did not content-read `~/.bailian` (absent), `~/.config/opencode/opencode.json`, `~/.prime/agent/telemetry.jsonl`, credentials, oauth, or `server.token`.
- Did not fetch HF, OpenRouter, or arXiv.
- Relocation sweep was maxdepth 5 on named roots, plus Trash depth 3 and `findmnt`. A deeper or other-host copy would be outside this sweep.
- Did not re-derive the "~50 deleted files" count or round-15's morning `test -e` transcripts. Those transcripts are not in the commit (`git show --stat` is prose-only).
