# kotoba — round 74 report (hyaku run 7, attempt 1)

Lane repo `kotoba-shokunin`, branch `master`, base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`, final lane tip
`ec2c1d3f2556ed88358aefa2b29322410e6b6253` (`jj-lane.sh state` → `local=ec2c1d3… remote=ec2c1d3… ahead=0`; `git ls-remote origin refs/heads/master` prints the same hash).
**This round is short of the floor: wave 2 (the falsify wave, 33 seats) was generated, validated under policy v1 and its `w2.ready` written, but never dispatched — the
orchestrator wrapped run 7 up (spawn cap 0). Round total 34 seats against the 64-seat floor; no fresh seat attacked the landed data. The next run re-dispatches the round.**

## Work performed

Declared claims (frozen `plans/round-74.md` at `329e7d9`; errata E1 and the counters at `d919179`): **C1 coverage** (sourced, assimilation) — the Agent Skills
`skill-creation/` guides best-practices, using-scripts and quickstart (S223–S225); **C2 freshness** — the sibling census re-pinned at 20 frozen fleet heads. C1 was
declared `depth` and relabelled `coverage` before data (`plans/round-74-addendum-1.md` E1.1).

- Round start: census exit 0, 148 rows (`.ufo/waves/round-74/receipts/census-before.txt`); tip battery `4 of 6` at base (the r73 closure file unindexed; `receipts/base-battery-l1.txt`); 15 of 20 sibling pins stale (`receipts/sibling-staleness-base.tsv`); id collision 20 (`assimilation/collisions`).
- Wave 1 (34 seats, all 34 reports present, `w1-results.json`): source opening ×3, counters, controls, 20-lane sibling reads, plan attacks. Its attacks changed the plan **before any data**: C2 clause (e) contradicted (a) (M134), "quotes die at moved lines" was false (M135), the no-harm line was reddened by C2 itself (M136), the C1 predicate admitted site chrome and 404 bodies (M137) — errata E1.1–E1.4 (`plans/round-74-addendum-1.md`), counters rebuilt (`verifiers/check_spec_craft.py` 250-assertion self-test, `verifiers/check_sibling_reread.py` 47).
- C1 data: entry `corpus/knowledge/spec-skill-creation-craft-round74.md`, rows S223–S225 (renumbered by document from staged S232/S237/S236), three snapshots pinned (`.ufo/waves/round-74/snapshots/`), `SKILL.md` § Body craft subsection, PROVINCE Core bullet.
- C2 data: `corpus/knowledge/sibling-overlap-census-round74.md` (nine-cell and 11-cell tables), PROVINCE § Adjacent re-pinned, tsukuroi `none` → `adjacent` (basis kotoba: `SKILL.md:127`, `corpus/knowledge/hook-files-round59.md:20`), `SKILL.md` description names tsukuroi (1,021 of 1,024 characters).
- Routed r73 items: index closure file (done at `329e7d9`); D2/D3 correction — `SKILL.md` was 570 lines at `1e03d19` (`git show 1e03d19:SKILL.md | wc -l`), and the r73 report/lesson M128 sentence "green-after … cited in the report" was not met (no green receipt existed) — corrected here, not rewritten; M129 "fix" label retracted; cross-vendor `.agents/skills/` decision row landed (`SKILL.md:79-81`); `compare_harness_independent.py` exit 2 diagnosed (baseline constants for 7 skills vs 75 offered) — L0 question appended, not a claim.
- Mined mistakes: M134–M139 (`corpus/lessons/round-74.md` § Mistakes); criteria Q70–Q73 (`corpus/QUALITY.md`). M138/M139 were found by my own post-landing run: `check_province_core.py` read `province core rows 0 of 2` and the first data commit had four gate reds; fixed in `559ee76` and by the `ADJACENT_ERRATA` ledger (`verifiers/check_province_core.py --self-test` 12 assertions).
- Round shape: two v1 waves planned, **wave 1 only run**. Wave 1: 34 dispatched, 34 settled — executor 15, scout 11, scribe 4, connector 2, reviewer 1, critic 1; dead seats 0; flash-routed roles (executor, scribe, critic, reviewer) 21 of 34; attack roles 2 of 34 (the wave was build-heavy by design). Wave 2 planned: 33 seats (reviewer 13, critic 5, mutation-tester 4, executor 4, scout 3, connector 2, scribe 2), `w2-spec.json`, never run. No residual call; the L1 held the planner seat.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open. Inherited state: none. Tool installs: none. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.ufo/state/kotoba.report-baseline` (driver file, untouched); seat scratch under `/tmp/k74*` that was mine removed.

## Landed changes

| commit | change | LOG.md entry |
|---|---|---|
| `329e7d9` | plan, base receipts, closure file indexed, id scratch, freeze heads | `## Round 74` |
| `d919179` | freeze 2: counters, addendum 1 (E1), registry rows, self-test receipts | `## Round 74` |
| `2c81137` | C1 and C2 data (first landing; four gate reds, M139) | `## Round 74` |
| `559ee76` | data-gate fixes (description, citation form, registry cells, baseline) | `## Round 74` |
| `88f18cd` | province-core Adjacent erratum ledger, M138–M139, Q73, wave evidence | `## Round 74` |
| `7cec017` | LOG, SCORECARD, README frontier note, data receipts | `## Round 74` |
| `1cf5afa` | corpus baseline re-record (commit_total 43) | `## Round 74` |
| `ec2c1d3` | tip receipts (lane HEAD) | `## Round 74` |

## Before → after measurements

- **C1 coverage** — `python3 -B verifiers/check_spec_craft.py --rev <rev>`: `spec craft pages backed 0 of 3`, exit 1, `held at base: 0` @ `1e03d19` (`receipts/c1-base-freeze.txt`) → `3 of 3`, exit 0 @ `559ee76` (`receipts/c1-data-559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd.txt`; re-read at `1cf5afa` exit 0). Shortcut worlds: the self-test arms for site banner, subtitle, heading, link, wrong id, 404 fetch record, digest mismatch, re-signed snapshot, filler action cells (`receipts/c1-selftest-freeze.txt`). Bound: form, sources, tokens and pinned bytes are counted; whether a rule sentence is true of its page is a reviewer judgement **no non-author made** (wave 2 was to assign it).
- **C2 freshness** — `python3 -B verifiers/check_sibling_reread.py --rev <rev>`: `0 of 20`, exit 1 @ `1e03d19` (`receipts/c2-base-freeze.txt`) → `20 of 20`, exit 0 @ `559ee76` (`receipts/c2-data-559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd.txt`). **The carry-forward world (tsukuroi left `none`, evidence recomputed by script) also reads `20 of 20`** (`receipts/c2-carry-forward.txt`, a labelled sandbox revision): the counter measures mechanical re-verification; the one judged change and every boundary sentence were not independently re-derived by a non-author this round.
- No-harm at `1cf5afa` (`receipts/tip-battery-1cf5afa6c174fa3066619673f51fe696c212ccce.txt`): tip battery `6 of 6` in both invocation forms (`--repo .` and absolute), guards 5 of 5; `check_gate_registry.py` `60 of 60`; `check_province_core.py` `province core rows 2 of 2`; census exit 0; `SKILL.md` 590 of 600 lines (`wc -l SKILL.md`); `check_sibling_census.py` on the r74 entry with `--province` and `--skill`: `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes`, length 1021 of 1024. Not run at the final tip: the two new self-tests are unfloored (a known gap, addendum E1.3).

## Sources & frontier

- `corpus/SOURCES.md` rows: 148 → 151 — `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Added by tier: A 3 (S223–S225, all agentskills.io, scoped to each page's own guidance), B 0. Rows touched old→new: none; one Search-log note appended. Frontier row advanced: a new area (the specification's `skill-creation/` set) moved from unheld to Core in part (`corpus/README.md` § Frontier, round-74 note); sibling arbitration refreshed.
- Census before → after: exit 0 → exit 0 (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`; 20 W04 duplicate-URL warnings unchanged, the three new rows add none).
- **Assimilation:** one theme from `merge/kotoba/` (the read-only package at `/home/vgpnk/Projects/shokuknow/merge/kotoba/`): the Agent Skills `skill-creation/` guides; id collision 20 (`S203`–`S222`), lane ids 148, staged ids 188; renumber by document staged S232→S223, S237→S224, S236→S225; guard proof `.ufo/waves/round-74/assimilation/guard-proof/guard-proof.txt`; scratch census exit 0 `w1/build/ExecIdsR74/mirror-final-census.txt`. One entry admitted; refused with reason and flip: the staged spec-description-trigger-discipline entry (its source is held as S213), the staged skill-invocation-is-the-bottleneck entry (measured effect, kengaku's ground). Quarantine slice 13 rows re-checked with fresh fetches: 8 adoptable, 5 refused, none appended (no admitted entry cites them).
- Pointer gate: `python3 -B verifiers/check_report_pointers.py --report .ufo/reports/round-74/kotoba.md --repo kotoba-shokunin --rev ec2c1d3f2556ed88358aefa2b29322410e6b6253 --round 74` printed `unresolved 0` before filing.
- **considerthese:** `considerthese/2026-10-25.md` item 4 worked (`SKILL.md:23-25`); items 1, 2, 5 remain.
- The sourced claim is C1 (rows opened 2026-10-25, located quotes in `corpus/lessons/round-74.md` § Gate).

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the base sweep showed empty (`receipts/base-sweeps.txt`: 0 rows, 0 phrase hits), three mined tier-A rows; self-assessed only.
- **quality: unchanged** — M134–M139 resolved and Q70–Q73 added, but no entry was superseded or re-verified by a stronger one, and no fresh seat attacked any landed claim.
- **discernment: unchanged** — the wave-1 attacks turned two frozen claims into errata before data (a gain), but no non-author has checked this round's gate decisions; the sample for the closure is in the lesson (admit S225/S224; rejects of two staged entries; the tsukuroi change).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` § Gate registry now 60 rows (`python3 -B verifiers/check_gate_registry.py --rev 1cf5afa6c174fa3066619673f51fe696c212ccce` → `60 of 60`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 74`; C1 entry built from three re-fetched pages (`.ufo/waves/round-74/receipts/c1-data-559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd.txt`).
- [~] Instructions executable by an agent without oral context — no fresh cold run this round; `corpus/lessons/round-8-aggregator-box3-coldrun.md` remains the only record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` § Adjacent re-pinned at 20 heads (`corpus/knowledge/sibling-overlap-census-round74.md`); `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` exit 0.
