# Routed-defect queue re-verification — round 11 (ScoutLedger)

Wall clock at run: 2026-09-28 18:56→19:06 -03:00.
Main repo HEAD at run: `8ec7a56` (drifted from the brief's `6deaeaa`; reflog shows
`6deaeaa` 18:49:13, `8ec7a56` "kengaku: round-9 report" 18:57:35).
Sources: `.ufo/reports/round-10/protocol.md` §Routing lines (49 rows) — canonical ledger
`.ufo/reports/AGGREGATE.md` was absent at 18:58 and EXISTS by 19:04:59 (see D-33).
Child repos, all read-only.

## Header answers (aggregator r6)

1. **Did aggregator r6 create `.ufo/reports/AGGREGATE.md`?** YES — by relocation, not a new file.
   `git status --porcelain` → `RM .ufo/reports/round-2/AGGREGATE.md -> .ufo/reports/AGGREGATE.md`
   (index rename staged, ctime 18:58:02). Content sha at staging equalled `HEAD:.ufo/reports/round-2/AGGREGATE.md`
   (`d457238ff7acba3614b582f06fc72fdb37594c3d4fc9d22f6cfef0a216d636f8` both) — i.e. the round-2 snapshot
   moved verbatim. Then refresh-4 §11 was appended: at 19:04:59 the file is 635 lines / 49 209 B,
   sha `563c80a5dc6378567d98298c60e9dd10cb606043221e6890b5716d224556f2bb`, `wc -l` → 635, and it contains
   "**Relocation — protocol duty discharged.** `git mv .ufo/reports/round-2/AGGREGATE.md .ufo/reports/AGGREGATE.md`".
   §11.2 (the 49-row reconciliation) was promised in prose but is **not yet on disk** — the file ends mid-§11.1.
   Uncommitted (index `R`, worktree ` M`).
2. **Did it commit its six `corpus/lessons/round-6-aggregator-audit.md` mirrors?** YES.
   `git -C <repo> ls-files -o --exclude-standard | grep -i aggregator` → **0 hits in all six** (exit 1).
   `git -C <repo> log --format='%h %an %ad %s' --date=iso --all --grep='aggregator' -5` →
   kagi `ad694a2`, kake `ab8c9e2`, kasegi `d341b48`, kengaku `3175e69`, kotoba `778310d`, kumitate `0ac2272`
   — all `aggregator-shokunin <aggregator@shokunin.local>` 2026-09-28 18:52:34 -0300; plus post-audit
   re-measurement `1bd17ec` (kengaku) / `31f09cd` (kumitate) at 18:56:38. `git -C <repo> rev-list --count
   origin/master..HEAD` → 0 in all six (pushed).

## Verdict table

| Row | Owner | r10 | Verdict now | Re-executed command → output (trimmed) |
|---|---|---|---|---|
| D-01 | kasegi | OPEN | **PARTIAL** — SKILL.md half LANDED, LOG half stale-but-erratum | `python3 -c "glob(bounties/claims/*/*/status.json)"` → `280 {'PARKED':248,'DONE':15,'SUBMITTED':2,'BLOCKED':15}`; `find claims -mindepth 1 -maxdepth 1 -type d \| wc -l` → `274`; `-mindepth 2 -maxdepth 2 -type d` → `295`; `find evidence -maxdepth 2 -name status.json \| wc -l` → `275`. `SKILL.md:8-9` now "274 program dirs / 295 packages (280 status-gated)" → matches. `SKILL.md:163` "`status.json` 275" = evidence-store count → correct. `LOG.md:5` still "275 claim dirs", `LOG.md:224` "252/275"; errata appended `LOG.md:284-285` "claims denominator 275→274 program dirs, 295 packages" |
| D-02 | kasegi | OPEN | **STILL-OPEN** (text) with errata | `find claims -mindepth 3 -name receipt.md \| wc -l` → `1`; `grep -n receipt.md LOG.md` → `:163` still asserts all three submitted carry `+ submit/receipt.md`; errata `LOG.md:289` "only mozilla has one … LOG history not rewritten" |
| D-03 | kasegi | OPEN | **LANDED** | `SKILL.md:458-461` histogram "PARKED 248 / BLOCKED 15 / DONE 15 / SUBMITTED 2" over "the 280 gated" vs live `{PARKED:248, DONE:15, SUBMITTED:2, BLOCKED:15}` = 280 → exact match; `LOG.md:284-285` records "histogram BLOCKED 16→15 + OPERATOR_GATED nested-not-top-level" |
| D-04 | kasegi | OPEN | **STILL-OPEN** (both halves) | `ls -d fleets/ufo-archive-2026/missions/claim-*/ \| wc -l` → `20`; `corpus/knowledge/ufo-archive-2026.md:5` "20 `claim-*` L1 hardening missions" vs `:11` "`missions/claim-*/` — 19 hardening missions" → internal contradiction survives. `ls fleets/ufo-archive-2026/inquiries/bounty-fleet-2026-09-06/` → 18 entries = 15 per-program + `farmscout-hidden.md` + `feeder01-sources.md` + `dispatch.log`; `:36` still "16 per-program L0 mission briefs" |
| D-05 | kasegi | OPEN | **STILL-OPEN** | `.ufo/reports/round-8/kasegi.md:46` "`ledger/candidates.jsonl` do-not-re-hunt → git commits"; `grep -ci 'do-not-re-hunt' ledger/candidates.jsonl` → `0`; no LOG errata naming it (`grep -n candidates LOG.md` → 43,149,154 only) |
| D-06 | kasegi/external | LANDED doc | **UNCHANGED-CARRIER** (LANDED doc stands) | `corpus/knowledge/operator-queue.md:12-15,69-70` "`claim-hold/*` tags are inert … `claim-index.mjs` does not consume `claim-hold/*`"; `git -C bounties tag -l 'claim-hold/*' \| wc -l` → `9` (3 queued) |
| D-07 | kasegi/operator | LANDED doc | **UNCHANGED-CARRIER** (LANDED doc stands) | `operator-queue.md:26-28` "Do not file this row; it is a duplicate of the operator's own 2026-09-06 disclosure"; `submitted-registry.md:100` carries sha256 `ded642e8…69393`, `claim-check.mjs` still returns OK |
| D-08 | kagi | OPEN | **STILL-OPEN** | `grep -n handoff-status SKILL.md` @HEAD `ad694a2` → `185,213,244,321` — all bare (no path); absolute `~/.local/state/tac/handoff-status.json` appears only in corpus (`credential-isolation.md:64`, `tac-evidence-integrity.md:4`) |
| D-09 | kagi | OPEN | **STILL-OPEN** | `SKILL.md:28` "One-shot command with vault env … needs `~/.config/the-janitor/op.env` present" — no stop clause; `~/.local/bin/the-janitor` `cmd_refs` L228-231 `echo "the-janitor: missing $ENV_FILE"; exit 2` |
| D-10 | kagi | PARTIAL | **PARTIAL** | `git -C kagi-shokunin ls-files \| grep -E 'drift'` → `corpus/drift-baseline.tsv`, `corpus/drift-pins.sh`, `corpus/drift-symbols.tsv`, `corpus/knowledge/drift-gate.md` (committed at `e64e81b`, 18:20:49) → drift half LANDED. `git ls-files -o --exclude-standard` → `corpus/state-shape.tsv`, `corpus/surface-census.sh`, `corpus/surface-census.tsv` **still untracked** |
| D-11 | kagi | OPEN | **LANDED** | seed-diff: `diff seed(4 boxes) HEAD:SHONEN.md` → only `5,8c5,12` (marks + one evidence line per box); 4 canonical box labels present, regenerated at `e64e81b` (`244b8c1` had prose-variant boxes). Residual nuance: marks are `[x]` citing lane-dispatched L2 `KagiR9Reviewer`, not an external verifier |
| D-12 | kengaku | OPEN | **STILL-OPEN** | `git merge-base --is-ancestor 85b22e3 HEAD` → exit `1`; `git branch --contains 85b22e3` → empty; `git cat-file -t 85b22e3` → `commit` (unreachable object); `.ufo/reports/round-7/kengaku.md:3` still cites `kengaku-shokunin@85b22e3` |
| D-13 | kengaku | OPEN | **LANDED** | `LOG.md:15` (round-9 entry) *is* the appended note: "round 7's amendment rewrote `LOG.md:9` in place (`git diff 85b22e3 f147a27 -- LOG.md` → one −/+ pair, "status flips"→"status deltas")" |
| D-14 | kengaku | OPEN | **LANDED** (append-only errata; row wording re-scoped) | `grep -n discordance corpus/knowledge/bench-arena-round7-noise-n25.md` → `:24` unchanged "0/12 PASSes (discordance 0/25)"; appended errata `:78-84` "the PASS denominator is wrong: `0/12` → `0/17` … the `0/25` discordance figure is consistent and unchanged" (lane disputes the row's literal `0/25→0/17`) |
| D-15 | kengaku | OPEN | **LANDED** | `git show f147a27:SHONEN.md \| grep -cE '^- \[[ x~]\]'` → `3` (3-box variant, no oral-context box); HEAD (`2575be6`) → `4` boxes (3 `[~]` + `[ ]` oral-context) |
| D-16 | kengaku | OPEN | **STILL-OPEN** | `ls corpus/lessons/` → no `round-6.md` (has round-1,3,4,5,7,8,9 + audit files); aggregator audit row `corpus/lessons/round-6-aggregator-audit.md:154` "no corpus/lessons/round-6.md for the round-6 landing \| r9 \| open" |
| D-17 | kumitate | OPEN (5 overdue) | **STILL-OPEN** (6 overdue) | `sed -n '29,30p' corpus/lessons/round-1.md` → "The installed `ufo` skill text says the swarm cap is 128 lanes"; `grep -rn 128 ~/.config/opencode/skills/ufo/ ~/.grok/skills/ufo/` → **0 hits**; `grep -n 128 scripts/ufo-swarm-wave.mjs` → `:13,:203` "kimi's MAX_AGENT_SWARM_SUBAGENTS=128" |
| D-18 | kumitate (+bounties HQ) | OPEN | **STILL-OPEN** | `find kumitate-shokunin -name 'registry-check*'` → none (no `ops/`); file is `/home/vgpnk/Projects/bounties/ops/registry-check.mjs`; `node ops/registry-check.mjs` → 7× `@role: kx-*.md pin '…' resolves to '…' but lane primary is '…'` (kx-connector/distiller/executor/labrat/reviewer/scout/security), `exit=1` |
| D-19 | kumitate | OPEN | **STILL-OPEN** | `grep -rln 'local://kumitate-r6' . --include='*.md'` → 7 files: `sighting-wall.md:5`, `runtime-support.md:4`, `cost-and-profile.md:4`, `enqueue-admission.md:6`, `native-admission-detail.md:4`, `reconcile-and-cycle.md:4`, `lessons/round-6.md:61` |
| D-20 | kumitate | PARTIAL | **STILL-OPEN** (corpus unchanged) | `grep -rn 'commit \`round' .` → `lessons/round-1.md:4`, `round-3.md:3`, `round-4.md:3`, `round-5.md:3`, `round-6.md:3`, `corpus/README.md:48` — subject/tag cites survive (uncommitted r8/r9 LOG switches to sha256) |
| D-21 | kumitate | OPEN (5 missing) | **PARTIAL** | `comm -23 <ls corpus/lessons> <index rows>` at HEAD → 2 unindexed (`round-6-aggregator-audit.md`, `round-9.md`); same diff against the **working tree** `corpus/README.md` → 0. Worktree fix uncommitted (`git status` → ` M corpus/README.md`) |
| D-24 | kake | OPEN | **STILL-OPEN** | `grep -rn 21:15 corpus/` → `kimi-subpath-audit.md:3`, `lessons/round-8.md:4`; `git show -s --format=%aI 9544914` → `2026-09-28T16:49:59-03:00` (19:49:59Z) |
| D-25 | kake | OPEN | **STILL-OPEN** | `grep -rn 'same-origin\|non-200'` → `LOG.md:12` and `lessons/round-8.md:31-32` unchanged ("44 same-origin links, 0 real non-200"), still no counting command |
| D-26 | kake | OPEN | **STILL-OPEN** | `systemctl --user is-enabled webzites-keeper.timer` → `disabled` (exit 1); `is-active` → `inactive` (exit 3); `corpus/knowledge/ops-automation.md:13` still presents it as the daily keeper tick; no correction entry |
| D-27 | kake | OPEN | **STILL-OPEN** | `grep -rn '/tmp' corpus/` → `kimi-subpath-audit.md:3`, `ghp-subpath-spotcheck.md:3`, `sitemap-orphan-audit.md:3`, `vault-properties.md:11-12`, `lessons/round-7.md:4`, `lessons/round-8.md:4`, `lessons/round-10.md:4`; `SCORECARD.md` move-log Evidence = `/tmp/kake-r10/*` |
| D-28 | kotoba | VERIFY | **LANDED** | `git -C kotoba-shokunin log --format='%h %ad %s' -3 -- SHONEN.md` → `abef8aa` 18:55:41, `e997d45` 18:30:24, `3b029b8`; `git show HEAD:SHONEN.md` → canonical 4 boxes (4 `[~]`) |
| D-29 | kotoba | OPEN | **LANDED** | `git show HEAD:SKILL.md \| awk '/^## Anti-patterns/,/^## Refusals/' \| grep -c '^\|'` → `22` (20 data rows + header + separator); `SHONEN.md:6` now "20-data-row anti-pattern table (… → 22 lines)"; `corpus/README.md:21` disambiguates "12-item checklist (artifact numbering; `SKILL.md` renders the same set as 9 merged boxes)" |
| D-30 | kotoba | PARTIAL | **PARTIAL** | `git log -1 --format='%an <%ae>' 3b029b8` → `Joao Pedro Veiga <jpveigao10@gmail.com>`; `8c300ad` → `shokunin <shokunin@local>`; `e997d45/8e22a41/abef8aa/32e0d79/d49dfa5` → `kotoba-shokunin <kotoba@shokunin.local>` — historical commits unfixed (no history rewrite) |
| D-31 | kotoba→**kumitate** (RULED) | RULED | **STILL-OPEN** | `sqlite3 -readonly ~/.omp/agent/agent.db "pragma quick_check;"` → `*** in database main *** / Tree 6 page 1918 cell 25: 2nd reference to page 3278 / wrong # of entries in index sqlite_autoindex_cache_1 / wrong # of entries in index idx_usage_history_series`; kumitate has not acted since the ruling |
| D-32 | kotoba | VERIFY | **LANDED** | `git ls-files` → `corpus/knowledge/opencode-offer-trace-round8.md` and `corpus/lessons/round-8.md` both tracked; content present (`lessons/round-8.md:63-91` dedupe correction with `grep -c` → 154/18) |
| D-33 | aggregator | OPEN | **LANDED (in flight)** | `.ufo/reports/AGGREGATE.md` exists: `git status --porcelain` → `RM .ufo/reports/round-2/AGGREGATE.md -> .ufo/reports/AGGREGATE.md`; `wc -l` → 635, 49 209 B, mtime 19:04:59; §11 "Refresh 4 — round-6 aggregator audit (canonical path)" + "Relocation — protocol duty discharged" present; §11.2 row reconciliation **not yet written** |
| D-42 | kengaku | PARTIAL | **PARTIAL** | `grep -rn 'status flips\|flipped status' corpus SKILL.md LOG.md` → survivors `corpus/lessons/round-5.md:8` (+ self-note `:48`), `SKILL.md:387`; `corpus/README.md:22` now "8 status deltas" (swept). 2 of the 4 named spots swept, 2 residual (one self-annotated) |
| D-44 | kake | OPEN | **LANDED** | `grep -n 'probe-history\|/home/kake' scripts/probe-delta.mjs` → `:33 path.join(process.env.HOME \|\| '', 'Projects/webzites/state/probe-history.jsonl')`; `grep -rn '/home/kake' scripts corpus` → 0 hits |
| D-45 | kake | OPEN | **LANDED** | `grep -n pending SCORECARD.md` → 0 hits; Score cells `operability 8`, `freshness 8`, move-log Before/After numeric ("detector landed+verified (6 events/0 phantom …)"). Residual: move-log Evidence pointer `/tmp/kake-r10/*` (= D-27) |
| D-46 | kumitate (+OMP) | OPEN | **UNSUBSTANTIATED** | `grep -ni wait kumitate-shokunin/corpus/knowledge/loop-driver.md` → 0 hits (145-line file); `grep -n 'wait\|loop-driver\|subagent' .ufo/reports/round-10/kake.md` → 0 (only `:70` names "kumitate/" in a connector bullet); `git log --all -p --loop-driver.md \| grep -in wait` → 0. Filed pointer does not resolve at either end |
| D-47 | aggregator | OPEN | **PARTIAL (six mirrors LANDED)** | `git -C <each> ls-files -o --exclude-standard \| grep -i aggregator` → 0 hits in all six; aggregated commits 18:52:34 in all six (+18:56:38 re-measure ×2); `rev-list --count origin/master..HEAD` → 0 all six. Residual: kagi `corpus/{state-shape.tsv,surface-census.sh,surface-census.tsv}` still untracked (= D-10) |

## Rows not re-run (owner has not reported since 18:40)

| Row | Owner | Status carried |
|---|---|---|
| D-22, D-23 | external (ufo-fsd-alpha) | UNCHANGED-CARRIER |
| D-35 | operator/scripts | UNCHANGED-CARRIER (spot-checked: `scripts/shokunin-watchdog.sh` `lane_prompt()` still emits only the report path, no SHONEN/hash/ordering items; `report_of()` still existence-based at `:44`) |
| D-36, D-37 | integrator RULED | UNCHANGED-CARRIER (rulings stand) |
| D-38 | operator | UNCHANGED-CARRIER (LANDED: `MISSION.md:11-14` fleet model map present) |
| D-39 | operator | UNCHANGED-CARRIER (LANDED-serving: `curl 127.0.0.1:34113/health` → `200`) |
| D-40 | protocol/operator | UNCHANGED-CARRIER (L0 question 1 filed, `.ufo/l0-questions.md`) |
| D-41 | protocol | UNCHANGED-CARRIER (adjudicated) |
| D-43 | operator | UNCHANGED-CARRIER (PARTIAL: `git ls-files .ufo/prompts` → 63 tracked; untracked → `kengaku-round-10.md`, `kotoba-round-11.md`, `protocol-round-11.md`) |
| D-48 | protocol (self) | UNCHANGED-CARRIER (`wc -l PROTOCOL.md` → `583` — compaction not landed) |
| D-49 | protocol (self) | UNCHANGED-CARRIER (LANDED in `43342dd`; `PROTOCOL.md:179` "Progressing means observable activity") |

## Aggregate verdict counts (required rows + extensions)

- LANDED: D-03, D-11, D-13, D-14, D-15, D-28, D-29, D-32, D-33(in flight), D-44, D-45 (11)
- PARTIAL: D-01, D-10, D-21, D-30, D-42, D-47 (6)
- STILL-OPEN: D-02, D-04, D-05, D-08, D-09, D-12, D-16, D-17, D-18, D-19, D-20, D-24, D-25, D-26, D-27, D-31 (16)
- UNSUBSTANTIATED: D-46 (1)
- UNCHANGED-CARRIER (not re-run): D-06, D-07, D-22, D-23, D-35, D-36, D-37, D-38, D-39, D-40, D-41, D-43, D-48, D-49 (14)

## Notable deltas vs the round-10 queue

- The queue's own text drifted: report line numbers in D-08 (L134/193/254/270 → 185/213/244/321),
  D-03 (`SKILL.md:415` → 458), D-18 (file is not in kumitate at all), D-46 (pointer resolves to
  nothing) — line-anchored rows must be re-anchored or they cannot be falsified.
- New activity since 18:40 not in the queue: aggregator refresh-4 §11 (D-33/D-47 answers),
  kotoba r10 (`abef8aa`/`32e0d79`/`d49dfa5`, 18:55-18:56), kengaku r9 report `8ec7a56` (18:57:35),
  main-repo HEAD 8ec7a56 ≠ brief's 6deaeaa.