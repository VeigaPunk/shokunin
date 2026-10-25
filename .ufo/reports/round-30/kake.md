# kake round 30 report (hyaku, in-session L1 KakeR30, attempt 1)

Lane tip (pushed): `91b60bd40c07de351c54ebdc366502f33dc19412` (branch `master`). Base `035668132250b75b38d399e86e540b0a0371efbc`.

## Work performed

Declared claims (`SCORECARD.md` "Round 30 — declared claims", committed at `4580c78` before implementation; notes and strict supplement at `04637bd` before any after-measurement):
- **C1, operability, repair:** the citing-set gate's reason codes are asserted by committed fixtures that its runner compares, and the round-27 families round 28 routed are repaired in `scripts/citing_set.py`.
- **C2, freshness, frontier (learning and sourced claim):** Render static-site deploy semantics enter held knowledge as `corpus/knowledge/render-static-sites.md`, grounded in S049–S052 opened this round.

Work items:
- Counters written and frozen by the L1 before the build: `.ufo/waves/round-30/c1_reason_count.py` (sha256 `be2a1287…c53e`), `c2_quote_truth.py` (`a2cd3164…5e7a`); strict supplement `c1_strict_checks.py` (`96e7bbcd…500f`) declared at `04637bd` after wave-1 critics built stubs reaching 14/14 without the property (`w1/CriticC1Counter.md`).
- Sources opened by the L1, one GET each at 11:49:44–45Z (`.ufo/waves/round-30/fetch_sources.py`, sha256 `b9431a5f…90b4`, named in every receipt); retained bodies, text and receipts in `.ufo/waves/round-30/sources/` (`4580c78`).
- Runner compares (id, reason) pairs; `case.json` run-time setup; fixtures 30–41 and 42–45; 13–16 converted (`71c6bfa`, `1c7773e`). Gate: duplicate keys, non-finite numbers (incl. `1e999`), ids `S` + 3 digits via fullmatch, store-once options in every spelling (exit 64), iterative walk, `O_NOCTTY` (`71c6bfa`).
- Entry, rows S049–S056, lesson Gate and Mistakes, SKILL "Render static-site triage — round 30" and "Citing-set reason-code registry — round 30", QUALITY round-30 section, README/PROVINCE round-30 sections, `publish-channels.md` "Round-30 Render recheck" (`451e98f`, repaired at `1c7773e`).
- Round-29 routed defects: (1) C1; (2) both wave contexts barred `freshness-sweep.mjs`, `probe-delta.mjs`, `live_snapshot.py` in every mode, plus a QUALITY criterion naming the exact live-capable invocations; (3) round-29 selftest and real-input demonstration re-run at `4580c78` with digests (`.ufo/waves/round-30/r29-rerun/receipt.json`: 45/45; 3 sites, 114 references, 4 findings, exits 1/0/1, equal to round 29); (4) receipts committed for `7697990` and `234524c` (`verification/r29-remeasure/`: C1 4/4, C2 30/30 at both, each naming revision and counter sha256); (5) explained: the round-29 matrix has no expected `id`/`page`/`resolved`/counts, the frozen counter stays; a regression pin `witness/extended-matrix.json` + `strict_c2_counter.py` compares them (mutant 9/30).
- Base mutant ledger: 23 reason-code renames, 0 killed at the base (`.ufo/waves/round-30/mutant-ledger/base-0356681-ledger.json`, MTE shape after S056).
- Wave-2 harms found and repaired: runner crash on mixed-reason oracles and unwritable case copy (`w2/ScoutNoHarmDiff.md`, fixed `1c7773e`); `case.json` setup could write outside `--tmpdir`, run fixture Git hooks, read outside the case, accept 100,000 steps (`w2/SentinelRunnerSetup.md`, fixed `f80bd8f`; the sentinel's 9 probes re-run against the fixed runner each fail with a refusal reason, symlinked case skipped).

## Landed changes

All through `jj-lane.sh`, each tied to the LOG.md "Round 30 — attempt 1" entry:
- `4580c78` declaration, counters, sources, before receipts, census before.
- `04637bd` declaration notes, strict supplement and its base receipt.
- `71c6bfa` C1 gate, runner, fixtures 30–41.
- `451e98f` C2 entry, rows, lesson, SKILL, QUALITY, README, PROVINCE, publish-channels recheck, C1 after receipts, round-29 receipts, witnesses, mutant ledger, wave-1 evidence.
- `1c7773e` wave-2 repairs (runner ordering and guarded copy, fixtures 42–45, entry/rows/wording/QUALITY), C2 after receipt.
- `f80bd8f` runner sandboxing repairs.
- `91b60bd` SCORECARD measured results, LOG, lesson wave-2 section, census after, final receipts, wave-2 evidence.
- Not mine, in range: `636dddd` (operator "considerthese" daily reflection).

## Before → after measurements

| Claim | Command | Before | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-30/c1_reason_count.py --root . --revision <commit>` | 0/14 at `0356681` (controls 3/3, stubs 0/14, 0/14) | 14/14, controls hold, stubs 0/14 and 0/14 | `71c6bfa`, `1c7773e`, `f80bd8f` (`verification/c1-after-*.json`) |
| C1 strict (closure supplement) | `python3 -B .ufo/waves/round-30/c1_strict_checks.py --root . --revision <commit>` | 0/6 | 6/6 | same (`c1-strict-after-*.json`) |
| C2 | `python3 -B .ufo/waves/round-30/c2_quote_truth.py --root . --revision <commit>` | 0/4 at `0356681` | 4/4, control not broken | `451e98f`, `1c7773e`, `f80bd8f` (`c2-after-*.json`) |

Every receipt names the counter sha256 and the revision; C1 receipts name gate `dbfade45…7f02` and runner sha256. Limits are listed in SCORECARD "Round 30 — measured results" (strict-checker holes, runner survivors, families still open, the C2 sources diff command exiting 1 because `sources/screened/` was added).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` — before exit 0, after exit 0; both print only the pre-existing `S033 duplicate url` W04 (`.ufo/waves/round-30/census-before.txt`, `census-after.txt`).
- Rows 48 → 56 (`grep -c '^| S0' corpus/SOURCES.md`). Added by tier: A ×5 (S049–S052 mined, S055 queued), B ×1 (S056 sibling tameshi `mte-report-interop.md` at `f4e8f7d8`, queued), C ×2 (S053, S054 rejected with flips). Touched old→new: none of the pre-existing rows. Unopened: a Stack Overflow question (HTTP 403 bot challenge), no row.
- Frontier advanced: the static-site part of "Render deploy semantics" moves from open to held Frontier knowledge (no gate, not Core); Render web services and the Blueprint file stay open.
- Mined mistakes: `corpus/lessons/round-30.md` "Mistakes" (5 rows: live sweep by a seat, receipts without digests, unreceipted re-measurements, counter field coverage, the round's own counter hole), each with captured-by and a fix shown able to fail.

## Trend verdicts

- **expansion: improved** — new entry on open Frontier ground with a coverage row, SKILL triage table; 8 new rows.
- **quality: improved** — an existing entry re-verified and deepened (`publish-channels.md` "Round-30 Render recheck": HOLD plus ADDED lines against `render.yaml` blob `d17ab7e5`); the citing-set gate gained reason-code fixtures. [author view; the closure decides]
- **discernment: improved** — reject sample from the source gate itself (S053, S054), a wave-2 critic corrected their reasons; counters and strict supplement attacked by stubs and mutants with ledgers.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Render static-site triage — round 30" (S049–S052, quotes checked 41/41 by `w2/ReviewSkillRenderTable.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG "Round 30 — attempt 1"; round-29 demonstration re-run with digests (`r29-rerun/receipt.json`).
- [~] Instructions executable by an agent without oral context — SKILL "Citing-set reason-code registry — round 30" (commands, exit map, fixture format).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE "Round-30 Render static-site frontier step".

## Round shape

Default two v1 waves. Wave 1 `kake-r30-w1`: 34 seats (scribe 10, reviewer 8, critic 5, scout 4, executor 3, mutation-tester 3, connector 1); 0 dead. Wave 2 `kake-r30-w2`: 34 seats (reviewer 19, critic 7, mutation-tester 6, sentinel 1, scout 1); 15 returned, 19 cancelled by the L1 at wrap-up under the run budget (their partial reports, where present, are unverified), 0 dead. Round total 68. No residual call. The §3 planner seat is held by the L1 (planning data-walk on scouts). Each wave was one `task` call carrying the validator's `taskCall` unchanged except a required `solutionSpace` field per task. Gate grants: w1 after 7 min, w2 at once; no refusals. Seats sent GETs only to third-party hosts (render.com, dev.to, namesilo.com, astro.build, stackoverflow.com 403); none to owned sites; no seat ran the live-capable lane scripts.

## Open items and extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no kake round-30 file at the fleet root (a stray `write` file names another agent and was left alone).
- Tool installs: none by the L1; no seat reported an install (MutBaseRunnerLedger used cached `jsonschema` 4.25.1 and `mutation-testing-metrics` 3.9.0 already on disk).
- L0 questions: none.
