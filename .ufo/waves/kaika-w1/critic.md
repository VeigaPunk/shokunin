# kaika W1 critic: adversarial review of `local://kaika-plan.md`

Reviewer: W1Critic (leaf member, no subagent dispatch). Date: 2026-10-19 (UTC ~21:05). Read-only: the only write is this file. Scope: the campaign plan against `PROTOCOL.md`, `PROTOCOL-APPENDIX.md` (rule keys only), `AXES.md`, `LEARNING.md`, `CORPUS.md`, `MISSION.md`, and the live fleet state under `/home/vgpnk/Projects/shokunin`.

## Verdict

The plan is not executable as written. Three critical defects make every W2 lane-round non-conformant by construction, and one operator ruling is required before any writer spawns. Nothing here needs new research. Rule text and live state are enough to decide it.

- **C1** Executors don't commit and the parent writes lane reports under lane identity. This inverts the protocol's landed-by-the-lane rule.
- **C2** The L2 floor (≥8 per lane, 21 lanes = ≥168 L2) is absent from the plan and exceeds its 64–100 budget.
- **C3** Round numbers are undefined. Three counters disagree, the driver has been dead since 2026-10-15, and `round-1` through `round-17` already hold filed reports.

Recommended order: operator L0 rulings → frozen SOURCES contract v1 with tested census gates → per-lane pre-flight → committed W1 dossiers → committed prompts → W2.

## Ground checked

| Claim | Observed | How |
|---|---|---|
| 21 lane repos exist | 21 `*-shokunin` dirs | `ls -d *-shokunin \| wc -l` → 21 |
| MANIFEST roster | 13 rows (kasegi kengaku kake kumitate kotoba kagi kama audio game-dev-2d game-dev-3d lore revenger kaidoku) | `jq '.roster\|length'` → 13 |
| Roster-less lanes | chousa kotodama mado mori souji tabi tameshi tsukuroi (8), all with `type:"mint"` rows | `jq '[.roster[]\|select(.id==$i)]'` per id → 0 each |
| MANIFEST size / rows | 306,760 bytes; 294 `rounds[]` rows | `wc -c`; `jq '.rounds\|length'` |
| Driver | `.ufo/watchdog.log` last line `2026-10-15T01:58:27-03:00 tick=2`; no `shokunin-watchdog` process in `pgrep` | `tail`; `pgrep -af watchdog` |
| Live session in fleet root | pid 805967, `omp --resume …2026-10-19T19-22-21…`, elapsed 1:42 | `ps -o pid,etime,args -p 805967` |
| Round counters | game-dev-3d: state=1, MANIFEST lane max=73, LOG heading max=110 (heuristic). kagi: state=16, LOG 20. kasegi: state=17, LOG 35. kumitate: state=18, LOG 43. mori: state=2, LOG 17 | `cat .ufo/state/*.round`; `jq group_by(.lane)`; grep of LOG round tokens |
| Filed round dirs | `reports/round-1` holds kaidoku, kama, kasegi, kotoba, kumitate, mori, protocol, souji, plus misnamed `kengaku-shokunin.md` and `web-properties-publishing.md`. `round-2` and `round-17` also filled | `ls .ufo/reports/round-N` |
| Pre-existing kaika worktrees | `.tower/worktrees/kaika/<id>-shokunin` for 12 lanes, created 2026-10-19 18:01, branch `kaika/round` (not the plan's `kaika/<id>-r<N>`). Clean; HEAD equals lane HEAD for audio, kama, kotodama | `ls`; `git -C … worktree list`; `status --short` |
| Dirty trees are not live | lore `.scratch/` 26 files, newest 2026-10-18 00:16. kama `.ufo/round-10/` 2 files, 2026-10-18 15:43. game-dev-3d `reports/round-107/` 79 files, newest 2026-10-19 00:30 (about 21h before now) | `find … -printf '%TY-%Tm-%Td %TH:%TM'` |
| game-dev-3d r107 status | commit `7c4e589` subject says "r107-aborted", yet its report files remain uncommitted | `git log --oneline -3` |
| Lane identity | audio-shokunin `user.name=ci`, `user.email=ci@local`. Other lanes `<id>-shokunin` / `<id>@shokunin.local` | `git config user.name` |
| kimi-shokunin HEAD | `bc7d690` is the Craft-hours revert; no Craft-hours text in fleet-root essence files | `git log`; `grep -ci craft-hours` → 0 across PROTOCOL/APPENDIX/CORPUS/LEARNING/AXES/MISSION |
| Operator-side writes | PROTOCOL.md:201; :448–450; :102–103 name `scripts/`, `CORPUS.md`, `MISSION.md`, `AXES.md`, and `templates/round-prompt.md` as operator-side | read |
| L0 evidence | `.ufo/l0-questions.md:3` says `lane_prompt()` emits 1 of 5 child-lane items; `:26` and `:29–42` ask the operator to reconcile round namespaces; `:6` flags the `novelty`/`consistency` axis split | read |
| Count-command test | `grep -cE '^\| S[0-9]{3} '` on the contract's no-space example row returns **0**; spaced form returns 1 | piped `printf` tests |

---

## Findings, ranked by severity

### CRITICAL

**C1. Authorship and report inversion.** Plan `kaika-plan.md:56–62`: parent "commits with the lane git identity," "Executors do not commit; the parent commits after review," and parent "writes fleet reports."

- Rule: `PROTOCOL.md:117–122` (a lane report lands last, after the lane's own child-repo commit, citing its hash). `:125–127` ("Landed also means landed by the lane: the commit that adds … carries the lane identity"). `:473–479` (lane identity; main-repo commits use `git -c user.name=<lane>-shokunin`).
- Consequence: either every W2 report precedes its commit (a conformance defect for each of 21 rounds), or the parent launders its own commits under lane identities. That second outcome is fabricated attribution, which the contract forbids. Parent-authored reports also make each `SHONEN` assessment non-lane-authored, so `[~]` evidence is lost.
- Fix: each lane commits its own round work on `kaika/round` with `git -c user.name=<id>-shokunin -c user.email=<id>@shokunin.local commit -- <pathspec>`. Then the lane writes `.ufo/reports/round-<N>/<id>.md` citing its HEAD. The parent verifies with `git merge-base --is-ancestor <hash> HEAD`, merges, and writes only integrator artifacts under `-c user.name=protocol-shokunin`. The parent never commits lane work under a lane identity. Executors are not forbidden from committing; the plan's "executors do not commit" line is the defect.

**C2. L2 floor absent and arithmetically infeasible.** Plan `:11–12` (64–100 delegations) and `:45–52` (≤100 members; W2 "21 lane executors"). The plan never mentions the floor.

- Rule: `MISSION.md:53–59`. "Every L1 lane MUST dispatch **at least 8 L2 subagents per round**, in **one batched AgentSwarm call** … one call carrying all lanes." For 21 lanes that is ≥168 L2 dispatches. The plan's own ceiling is 100.
- Consequence: a W2 that honors the floor breaks the operator's 100 cap, and a W2 that honors the cap silently violates the floor. Either way the plan states neither.
- Fix: put the conflict to the operator as an L0 question before W2. Options: accept ≥168 L2 in one batch for W2 alone, or rule explicitly which lanes are `not-dispatched` this round (with `closed_at`, per `PROTOCOL.md:251–252`). Do not silently shrink the floor or the directive. Map each L2 role to a route bucket (`MISSION.md:61–65`), never to a bare alias (see M2).

**C3. Round identity undefined; numbering collides with filed records.** Plan `:57–62` and `:45–52` specify no round number per lane.

- Rule: `PROTOCOL.md:86–87` ("a lane must not claim a round other than the steered one"), `:113–116` (per-lane counters), `:138–141` (a report under any other name does not satisfy the contract).
- Evidence: the three counters disagree (table above). `.ufo/reports/round-1` through `round-17` already hold filed lane reports (ten files in round-1 alone). The steer driver has been silent since 2026-10-15, so no `launch`/`steer` dispatch evidence exists for W2 (`PROTOCOL.md:253–256`). L0 entries at `.ufo/l0-questions.md:26` (kumitate round-17) and `:29–42` (relaunch round-1 namespace) show lanes already asking the operator for a ruling.
- Consequence: a W2 writer that picks `round-N` from any plausible counter overwrites or misfiles a filed record. A non-steered number is also a protocol violation.
- Fix: the operator issues a steer table (lane → steered N, recorded in a committed answer artifact) before W2. Each W2 prompt carries its N. Before writing, the writer must confirm that no `.ufo/reports/round-N/<id>.md` and no lane `LOG.md` heading `round N` exists. The plan itself must not choose N.

### HIGH

**H1. Operator-side and essence files scheduled for writes.** Plan `:37–41`: D3 writes `CORPUS.md`, `LEARNING.md`, `templates/round-prompt.md`, and a `PROTOCOL.md` row. D4 creates `scripts/sources-census.sh`.

- Rule: `PROTOCOL.md:201` ("It never edits a prompt or the script, and `scripts/` … remain operator-side"). `:448–450` (`MISSION.md`, `AXES.md`, `CORPUS.md`, `scripts/` are operator-side). `:102–103` (`templates/round-prompt.md` is operator-side). `PROTOCOL.md` itself is protocol-lane-owned, not a W2 writer's file.
- Evidence: `.ufo/l0-questions.md:3` says the template alone does not reach lanes; `lane_prompt()` in `scripts/` must change too, and the integrator's report must carry the exact text.
- Fix: D3 and D4 become proposals: committed diffs under `.ufo/waves/kaika-*/` plus L0 requests for the operator to apply `CORPUS.md`, the template, `lane_prompt()`, and `scripts/`. The protocol lane lands any `PROTOCOL.md` change in its own integrator report. `LEARNING.md` is essence and needs an operator ruling; the plan does not list it as writable at all.

**H2. D5 writes the canonical upstream and imports fleet-specific material.** Plan `:42–43`: D5 brings `kimi-shokunin` into line with the fleet root.

- Rule: `PROTOCOL.md:463–470` and `:501–503` (upstream-bound work is the operator's; operator-gated artifacts are committed but not pushed). `kimi-shokunin/skills/shokunin/protocol/` mirrors `MISSION.md` and `AXES.md`, which carry fleet-specific lane config.
- Fix: D5 needs explicit operator approval and a file allowlist. Exclude `MISSION.md` and any fleet `shokunin.conf` content. Add a gate: `grep -cE 'm_(luna|haiku|flash|zfl|swe|antigravity)' <D5 diff>` must return 0, so host aliases never enter the substrate-neutral canonical copy.

**H3. W1 dossiers are not durable evidence.** Plan `:49`: W1 writes `local://kaika-w1-*.md` only.

- Rule: `PROTOCOL.md:341–343` ("session-scoped `local://` artifacts … are not evidence — commit the artifact or cite a reproducible command"). The wave context's own W2 consumes these dossiers.
- Fix: the integrator commits each W1 dossier to `.ufo/waves/kaika-w1/` (committed with the integration commit, `PROTOCOL.md:455–456`) before any W2 starts. W2 cites committed paths only.

**H4. Source rows with no proof of opening.** Plan `:29–30`: "Every row opened in the round that writes it." No mechanism backs it. W2 writers can copy W1 leads into rows, and the census cannot see "opened."

- Rule: wave context rule 3 ("a source row is a claim … opened in this session"); `CORPUS.md:23–26` (knowledge entries cite a resolvable source).
- Fix: each row needs a fetch record. Put `opened` = fetch date, and record the SHA-256 of the fetched reader output in the lane `LOG.md` entry that the round cites. Census gates: `opened` must fall on or after the round's start date; each `status=mined` row must have a `used-by` path that exists and contains the row id (tested form in the command block below).

**H5. The counting command returns 0 on the contract's own example format.** Wave context SOURCES contract: example row `|S001|Title — …|docs|A|…|queued|…`. Counting command: `grep -cE '^\| S[0-9]{3} '`. The spaces in the pattern don't match the example's no-space layout.

- Test: no-space example → **0**. Spaced layout → 1. A silent 0 reads as "no sources" or hides a loss.
- The tier awk also emits `A(blog)` as a separate category without failing, and the command never checks cell count, so malformed rows vanish. (Rule: `CORPUS.md:33–37`, "A count carries its command.")
- Fix: replace with the tested commands in the command block below.

**H6. Goodhart: row counts and tier inflation.** Plan: "15–30 rows" per lane (wave context). That is ≥315 registry rows across 21 lanes, and the success metric drifts to row count. `LEARNING.md:30` measures expansion as admitted `knowledge/` entries on uncovered ground, not registry rows.

- Tier inflation is not caught by the contract. Nothing forbids `kind=community|talk|own-work` at tier A. Tested: a community row at A is invisible to the stock command.
- Fix: census gates for tier/kind mismatch (command block below). Expansion verdicts computed from `corpus/knowledge/` entries whose `source:` resolves to a `mined` row. Rejected rows reported separately and excluded from the expansion count.

**H7. Verification independence and discernment gaps.** Plan `:61`: verifiers are "fresh agents on a different model."

- Rule: `AXES.md:46–48`: an exploratory claim verifies only with "a named non-author reviewer on record (reasons included; a dispatched subagent does not count)." `LEARNING.md:39–45`: each round needs a non-author spot-check of ≥1 admit and ≥1 reject, recorded `agree`/`disagree` with a reason in the lesson. `PROTOCOL.md:63–68`: only a named non-author `<id>` may write `[x]`.
- Consequence: W3 subagents cannot verify exploratory claims at all, and the plan has no spot-check table or verifier identities.
- Fix: W3 outputs include a spot-check table (≥1 admit, ≥1 reject per lane). Exploratory claims route to a named operator or fresh-lane reviewer, never a W3 subagent. Each `[x]` names a verifier id that is not the lane's own.

**H8. Aggregator and protocol lanes unassigned.** Plan's waves list no aggregator or protocol round. Parent writes "root LOG/SCORECARD" (`:57–58`), which the protocol assigns to those lanes.

- Rule: `PROTOCOL.md:311–326` (aggregator reviews every child `corpus/` each round, files `round-<N>-aggregator-*.md`, and refreshes `.ufo/reports/AGGREGATE.md`). `CORPUS.md:60–61` (per-repo verdict `conformant` / `not conformant`). `PROTOCOL.md:453–454` (main-repo `LOG.md`/`SCORECARD.md` belong to the protocol and aggregator lanes).
- Fix: add aggregator and protocol lane-rounds to W3 with their own identities, reports, and ledger refresh. The parent writes root files only as the protocol-lane integrator, under `protocol-shokunin` identity, and says so in round notes.

**H9. MANIFEST and roster ownership.** Plan `:57–58`: parent writes "MANIFEST entries." Plan calls all 21 "lanes" as if all are rostered.

- Rule: `PROTOCOL.md:48–53` (a mint never edits the MANIFEST roster; a roster row appears only after ≥3 verified rounds, written by the operator). `:237–252` (entry shape; `closed_at` required on any `not-dispatched` row; `lane_rounds` required on `not-dispatched` rows). `:299–310` (append-only, history pin).
- Consequence: 8 unrostered lanes would get roster writes they may not receive. Closure rows need dispatch evidence from the dead driver log. A live session (pid 805967) is attached to the fleet root with no lock.
- Fix: parent appends `rounds[]` only, as one atomic `jq` write under protocol-lane identity, after a fresh read and sha check. No roster edits. Probation state goes in `rounds[].notes`. Stop or confirm the other live session before writing. Never regenerate `.ufo/history-pin.json` inside this pass (`PROTOCOL.md:307–310`).

**H10. Worktrees, dirty trees, base SHAs, identity, and a false "live" claim.** Plan `:59–60` names `kaika/<id>-r<N>` worktrees. Twelve `kaika/round` worktrees already exist. Plan `:25` implies lore, kama, and game-dev-3d are live.

- Evidence: those trees are stale (table above), and worktrees branch from HEAD, so they exclude the uncommitted files. Closure requires "no participating repo left with uncommitted round work" (`PROTOCOL.md:216–217`). audio-shokunin commits as `ci`, which `PROTOCOL.md:473–476` calls a conformance defect.
- Fix, per lane, before worktree creation: (1) `git status --short` must be empty, or each file is classified (commit under the lane identity / archive / name in the lane report). (2) Record the base SHA in the plan. (3) Use the plan's branch naming; the operator decides what happens to the existing `kaika/round` worktrees (no destructive action by the planner). (4) audio sets `git config user.name audio-shokunin` and `user.email audio-shokunin@shokunin.local` once and logs it in `LOG.md` (`PROTOCOL.md:474–476`).

**H11. Dispatch prompts not generated; SHONEN not regenerated.** Plan has no prompt step. Closure fidelity check reads `.ufo/prompts/<lane>-round-N.md` (`PROTOCOL.md:217–221`, `:255–258`), and `lane_prompt()` emits 1 of 5 child items (L0 `:3`). `SHONEN.md` must be regenerated verbatim from the template per lane round (`PROTOCOL.md:417`).

- Fix: the integrator generates each W2 prompt from `templates/round-prompt.md` with the full round contract and all five child-lane items quoted verbatim, commits it, and each lane re-reads `PROTOCOL.md` at round start (`:90–92`). `SHONEN.md` is regenerated from the template in the same commit.

**H12. Credential and live-target guardrails missing.** Plan adds corpus text. `CORPUS.md:47–51`: "No credential material, ever. … vault ref paths (`op://…`) stay out of every corpus." L0 `:12` reports six child corpora already carry `op://` references (kagi included), and the rule is contested. Wave context rule 2 forbids live-target contact by security, bounty, vault, and serving lanes.

- Fix: a pre-commit sweep on every W2 diff, returning non-zero on any hit: `grep -rnE 'op://|-----BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}' <lane>/corpus .ufo/waves/kaika-*` (untested as a whole; sub-patterns follow the same grep semantics). Hits are reviewed, not weakened: rule 8 changes are an operator decision (L0 `:12`). Kasegi, kagi, and kake W2 prompts state the no-live-target rule verbatim.

### MEDIUM

**M1. Provider exhaustion and blocked rounds not planned.** Repo evidence: kama `35e9175` ("blocked dispatch"), kama `d0f5a2d` (glm free wire id absent from catalog), game-dev-3d `3ea02ff` ("xai credits exhausted"), kotodama `c42d675` ("64-seat dispatch on key-3 402'd"). The plan assumes 21 successful W2 lanes. Fix: pre-flight route catalog per lane; `blocked`/`failed` rows allowed with evidence (`PROTOCOL.md:154–156`, `:291–292`).

**M2. Bare model aliases against the route table.** Plan `:11–12` uses `m_luna`, `m_haiku`, `m_flash`, `m_zfl`, `m_swe`, `m_antigravity`. `MISSION.md:9–14` requires a route name "resolved through the host model route table, never a bare model alias." Connectors are mapped to `m_antigravity`, but `MISSION.md:61–65` assigns connectors to the heavy-reasoning bucket. Fix: map each role to its bucket; keep aliases only in the host table.

**M3. Member budget understated.** Plan `:49` says W1 = 32 members. The live roster this session shows 32 peers plus "16 more live peer(s) omitted," i.e. about 48 W1-prefixed peers. With W2 (~23) and W3 (~24), the plan's ≤100 cap is at risk and the plan has no member accounting. Fix: close W1 members at wave end and count live peers before each spawn.

**M4. Undefined axis vocabulary.** `novelty` (kengaku) and `consistency` (kotoba) are not among the six axes in `AXES.md`. L0 `:6` flags this as ledger row D-78. `PROTOCOL.md:494–496` allows a non-six axis name only with an in-row mapping to one of the six. Fix: W2 writers map in-row or wait for the operator; no writer adds axes (`AXES.md` is operator-side).

**M5. No baseline anchors or before→after discipline.** Plan does not freeze a base SHA per lane, and it does not require per-claim before/after with counting command and commit. `PROTOCOL.md:491–494` requires both. The three trend verdicts (`LEARNING.md:23–33`) are absent from the plan's W3 checks. Fix: record base SHA per lane at W2 start; each claim row carries command + commit; each round reports expansion, quality, and discernment verdicts.

**M6. "No push" conflict unnamed.** Plan `:13` declares a standing no-push rule. `MISSION.md:79` says commit then push. `PROTOCOL.md:501–503` says the protocol wins on process and the conflict must be named in round notes; `:467–470` allows operator-gated commits to stay local. The plan does neither. Fix: name the gate and the precedence in round notes; apply it uniformly.

**M7. Contract race between W2 and D3.** The SOURCES contract is still a draft ("draft — wave 2 creates…"). D3 changes contract text during W2. Changing the SHONEN template mid-wave makes lane regenerations drift. Fix: freeze SOURCES contract v1 and the census gates before W2 spawns; D3 changes apply to the next round.

### LOW

**L1. W4 remediation has no round semantics.** Plan `:51` says W4 "resumes." A `failed` row is terminal, and re-running a lane-round needs a new steered number or a `closure-correction` (`PROTOCOL.md:273–279`, `:299–301`). Fix: W4 is a closure-correction under a new steered N.

**L2. Bloat and stray artifacts unmeasured.** `LOG.md` 131,795 bytes; `SCORECARD.md` 59,226; `MANIFEST.json` 306,760. Root-tracked `.ufo/round-10/` and `.ufo/round-44/` are stray. `kama-shokunin/` is missing from `.gitignore` (L0 `:17`). Fix: record sizes before and after; cap SOURCES rows per lane (sized by H6 gates, not a quota); clean up stray artifacts only via the integrator.

## Tested replacement census commands

Run against a synthetic table (not repo files). Outputs are from the run.

```sh
# rows (spacing-tolerant); fails if zero
grep -cE '^\|[[:space:]]*S[0-9][0-9][0-9][[:space:]]*\|' corpus/SOURCES.md
# malformed data rows (NF must be 11 with leading/trailing empties)
awk -F'|' 'NR>1 && /^\|/ && NF!=11 {n++} END{print n+0}' corpus/SOURCES.md
# bad tier and tier-inflation (community/talk/own-work/book labelled A)
awk -F'|' 'NR>1 && /^\|[[:space:]]*S[0-9][0-9][0-9]/ {k=$4;t=$5;gsub(/ /,"",k);gsub(/ /,"",t); if(t!="A"&&t!="B"&&t!="C") bad++; if(t=="A"&&k~/^(community|talk|own-work|book)$/) infl++} END{print "bad_tier="bad+0, "tier_inflation="infl+0}' corpus/SOURCES.md
# duplicate ids (must print nothing)
awk -F'|' 'NR>1 && /^\|[[:space:]]*S[0-9][0-9][0-9]/ {id=$2; gsub(/ /,"",id); print id}' corpus/SOURCES.md | sort | uniq -d
# zero-row guard: exits 1 when no rows
grep -cE '^\|[[:space:]]*S[0-9][0-9][0-9][[:space:]]*\|' corpus/SOURCES.md | awk '{exit ($1==0)}'
```

Observed on the synthetic table (`|id|…|` header, five data rows including one malformed and one duplicate id):

- rows → 5 (includes the malformed and duplicate rows; reported separately below)
- malformed → 1
- bad_tier=2 tier_inflation=1
- duplicate ids → `S003`
- zero-row guard on a no-row table → exit 1

Known limits: the `used-by` cross-check for `mined` rows is specified in H4 but not coded here. The secret sweep in H12 is untested.

## Gating order before W2

1. **Operator L0 rulings:** L2 budget (C2); steer table per lane (C3); D3/D4/D5 scope and `LEARNING.md` (H1, H2); aggregator and protocol inclusion (H8); no-push precedence (M6).
2. **Freeze SOURCES contract v1** and census gates, using the tested commands (H4–H6, M7).
3. **Per-lane pre-flight:** clean or classify dirty trees; record base SHA; set audio identity; create worktrees under the plan's branch naming (H10).
4. **Commit W1 dossiers** to `.ufo/waves/kaika-w1/` (H3).
5. **Generate and commit prompts** from the template; regenerate `SHONEN.md` (H11).
6. **W2 lanes** commit their own work, write their own reports, and cite HEAD. Parent verifies ancestry and merges (C1).

## Limits

- No sibling gate, self-test, or repo write was run. Verification is the main agent's.
- The L0 queue was read in part; long lines were truncated at 768 characters, and I did not observe operator answers to the round-namespace or L2 questions.
- The W1 member count (~48) comes from the peer roster visible to this session.
- Dirty-tree content was judged by mtime and file count only; file contents were not read.
- The "No push (standing rule)" phrase was confirmed in MANIFEST notes at lines 4382, 4624, and 4702 by grep; the full line was truncated.
- I did not measure whether the driver can be restarted, and I did not assess the kimi-shokunin protocol copy beyond the Craft-hours check.
