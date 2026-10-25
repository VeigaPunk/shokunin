# kake — round 41 (attempt 1, L1 `KakeR41`, hyaku in-session)

Lane `/home/vgpnk/Projects/shokunin/kake-shokunin`, base `8eb121c8`, lane HEAD `c93bf9a8b9acece1f9328548e279c27945bd1da9` (pushed; `jj-lane.sh state`: local = remote, ahead 0).

## Work performed

Declared claims: **one** — **C1, operability (repair of a held tool):** the URL judgment of `scripts/sitemap_audit.py` (`_parse_url`, contract sentences 4 and 22) follows the RFC 3986 `URI` grammar with an authority and a non-empty host before `urlsplit` splits the value. **Exploratory** — kill rule (1) fired on the frozen counter before the build. Frontier step (SOURCES curation, mined mistakes, sourced claim) inside the cap.

- Repair first (round-40 spot-check routed defects): (1) round-40 tally restated over live seats, **26 of 72** (SCORECARD "Round 40 — closure correction (appended in round 41)", lesson § Corrections, `w1/ReviewR40Restatement.md`); (2) the revised build got fresh seats before this report (`resid/`, QUALITY (t) check exit 0, `verification/criteria/fresh-review-r41-final.txt`); (3) counter names and mounts random, labels stay in the counter; round-40 key-finders score 0/1434 (`verification/r40standing/`); (4) interior C0 decided against RFC 3986 (C1).
- Independent oracle (session note): labels from a published RFC 3986 grammar (abnf 2.9.1, vendored wheel = PyPI digest, S118); second published implementation (rfc3987 1.3.8, S119) agrees on 14,340/14,340 cases (`verification/pre/oracle-crosscheck*.json`). Counter v1 `c1_count.py` (sha256 `2acc443a…67b4`) at `abf457d0` with L1 controls and the base receipt (1049/1434).
- Pre-freeze control wave (wave 1, 37 seats): L1 re-scored 141 returned tools; **15 meet** v1 (trailing-`%` partial repair `terminal_pct`, generator-template `v1_shape`, length/strip-gated mutants, allow-list-plus-delimiter tools, equivalent mutants) → C1 declared exploratory at `9e3c31d2`, before the build (SCORECARD "Round 41 — kill rule (1) fired on counter v1").
- Build `eae5ae2c` (tool `0b485431…`; reference revised before landing to leave IP literals to `urlsplit`). Wave 2 (33 seats) found a regression (TAB/LF/CR inside an IP literal accepted; `w2/CriticExploratoryBetter.md`, `w2/ReviewBuildDiffFresh.md`) → revised build `0c5ad2f6` (tool `50287ac6de5600ab1fca5a4cb77d9f3b8a170ad0a63f287512f9403bdb1dde7d`); selftest 183 → **225** fixtures (29 red on base, all `r41_*`; 6 red on the first build).
- Counter v2 `c1_count_v2.py` (information only; ends-included insertion, empty components, varied IP literals, loc strip, minimal bwrap env): the found gaps fail it (`verification/w1v2/`, 10/141 still meet, equivalent tools).
- Residual call (8 seats) on final bytes: no new acceptance over base on 770 IP-literal values, 0 RFC-valid regressions on 60,100 values, selftest/real run/counters/census reproduced (`resid/`).
- Mistakes mined, QUALITY (s), (t), (u), (n)-amended reading, (r) status; SKILL amendment "Sitemap file audit — round-41 URL rule".

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `abf457d0` | counter v1, oracles, L1 controls/receipts, pre-freeze SCORECARD section | Round 41 bullet 1 |
| `9e3c31d2` | wave-1 receipts, kill-rule record, S117–S119, counter v2 | bullet 2, 4 |
| `eae5ae2c` | build, 15 fixtures, SKILL amendment, real-run inputs retained | bullet 3 |
| `2653b629` | build receipts, lesson, QUALITY, LOG, row corrections | bullet 5 |
| `0c5ad2f6` | build revised (IP-literal repertoire), 6 fixtures, used-by/anchor fixes, r40 restatement | wave-2 bullet |
| `133257de` | selftest 225 | wave-2 bullet |
| `b9bf1a39`, `c4eb7e73`, `c93bf9a8` | lesson/SKILL wording, wave-2 and residual reports, results table, planned row, census after | wave-2 bullet |

## Before → after measurements

- C1 (information; exploratory): `python3 -B .ufo/waves/round-41/c1_count.py --root . --revision <rev> [--seed N] --out <receipt>` — before `8eb121c8` **1049/1434** (seed 41001; 1028–1078 over seeds), after `b9bf1a39` **1434/1434** (seeds 41001–41003 and random; `verification/build3/`, `resid/ResidCounterRerun.md`). Not an admission measure: 15/141 live-seat controls met v1 before the build.
- Harm: selftest `python3 -B scripts/sitemap_audit_selftest.py --tool scripts/sitemap_audit.py` → `PASS 225/225` (base 196/225); real run `jq -S . | sha256sum` = `fd985a41867ed31b…bc8a5` at base and final. **Frozen harm clause "new fixtures must be red on 8eb121c8" is NOT met as written** (13 of 42 `r41_*` green on base: valid-value controls, parity and regression guards); by its own wording it reads "operability harmed" — reported, not relabelled. Also: ×3–40 CPU cost on adversarial values (linear); zone ids with non-ASCII/`|` now rejected (RFC-invalid).

## Sources & frontier

Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`: start exit **0** (10 W04, `kake ok`, `.ufo/waves/round-41/census-before.txt`); end exit **0** (11 W04, `kake ok`, `census-after.txt`). Rows 116 → 119: +S117 (A, spec, RFC 3986 `URI`), +S118 (B, code, abnf 2.9.1), +S119 (B, code, rfc3987 1.3.8); Gate quotes and access 2026-10-23T09:39:11Z in `corpus/lessons/round-41.md` § Gate. Same-round corrections of the new rows logged old→new (lesson § Wave 2: S117 anchor/teaches, S118/S119 teaches, used-by E11 fix). No existing row's status/recheck/used-by changed. Sourced claim: C1 cites S117/S118 (and S102). Mistakes: lesson § Mistakes 1–3 (support narrower than class → QUALITY (u); dead-seat leftovers counted → (s), red on r40; revised build L1-only → (t), red on r40).

## Gate

Rejects: counter v1 as admission instrument (15/141 controls meet); RFC 3987 justification for non-ASCII (`ScoutIRIRule`); reference's own IP-literal check; "S098 already teaches URI"; reclassifying single-point mutants after scores. Full table in lesson § Gate.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry; rows ground the held tool.
- **quality: unprovable-but-better (pending non-author judgment)** — URL rule repaired with an independent oracle; but lane-seat advisory `ResidCriticBetter` says "not better as an unconditional no-harm move" (literal harm clause, adversarial cost, zone-id drift). The L1 self-awards nothing.
- **discernment: improved** — pre-freeze control wave caught the counter before data; regression caught and fixed before the report by fresh seats; (s)/(t)/(u) shown red on round 40 / v1 and green on round 41 / v2.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Sitemap file audit — round-41 URL rule" (S117, S118, S102).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG "Round 41" (real run byte-equal, `verification/build3/realrun-build3.json`).
- [~] Instructions executable by an agent without oral context — selftest 225 fixtures + SKILL text, reviewed by `resid/ResidReviewRecords.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged since `8eb121c8`.

## Round shape, seats, holds

- Shape: default two v1 waves + residual. Wave 1 `kake-r41-w1` 37 seats (12 executor, 12 mutation-tester, 4 reviewer, 3 scout, 2 critic, 2 scribe, 1 sentinel, 1 connector); wave 2 `kake-r41-w2` 33 seats (19 reviewer, 5 scout, 4 mutation-tester, 3 critic, 1 executor, 1 sentinel); residual 8 (6 reviewer, 2 critic). **Round total 78.** Planner seat held by the L1.
- Dead seats 0; refusals 0; cancelled 0. Misroot sweep: no fleet-root file from this round's seats.
- Inherited state: none (watchdog shows only the launch line). Not edited: `corpus/lessons/round-40-verifier-spotcheck.md`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: abnf 2.9.1 and rfc3987 1.3.8 (uv venv + `pip download`, PyPI, scratch `/fast/scratch/hyaku/kake-r41/oracle`; reason: independent RFC 3986 oracle; wheels vendored in the lane). Seat `ResidIPLiteralProbe`: stdlib venv with the local wheel (`--no-index`). No pacman.
L0 questions: none.
