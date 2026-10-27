# Mori — round 58, attempt 1

## Work performed

C1 targeted the **calibration** axis: a frozen counter intended to bind the two round-56 active-register rows to their evidence pointers and exact MANIFEST keys. C2 targeted **depth**: a source-located entry on driver-liveness parser implementation details. At entry (`b783d0b892637ce8d20f188cad20e4d8913ca635`), depth, freshness, and calibration were tied at 5 (coverage 6, operability 7, adjacency 6). No scalar score delta is claimed.

Protocol, controls, claims, and stop conditions were frozen in `fe8801120a67c1a6b8899d7d0423839caa09e7d0`; the validated dispatch was `4272736cfc5147586e1543413772f80daf44b04b`. The 64-seat v2 wave, `w1`, completed through the orchestrator handoff. Mix: reviewer 22, critic 10, mutation-tester 8, executor 8, scribe 6, scout 4, connector 2, sentinel 2, revenger 1, simplifier 1. Attack seats (reviewer + critic + mutation-tester + sentinel) were 42/64 = 65.6%. L1 held planner; connectors had overlap duties only, not a separate planning walk; no residual call. `w1-results.json` has 64 nonempty outputs and no status/error fields. The report-file settlement scan found 58/64 reports and state `partial` (6 absent); there are no per-seat death/error records, so the missing reports are not called dead. Receipts: `.ufo/waves/round-58/w1-results.json`, `.ufo/waves/round-58/w1/`, and `.ufo/waves/round-58/evidence/w1-settlement.json`.

## Landed changes

- Freeze and counters: commit `fe8801120a67c1a6b8899d7d0423839caa09e7d0` (contract, controls, C1/C2 instruments, census start).
- Validated wave specification and registry: commit `4272736cfc5147586e1543413772f80daf44b04b`.
- Host-route divergence recorded as an L0 question: commit `fac6534aba55f758607332c3ee973b6428de976e`.
- Data/evidence commit `7d317495245fec896c6ee7214d8eb995ad2302ba`: 11-claim knowledge entry, S550/S551/S552 source rows, round lesson, README/QUALITY updates, wave reports, settlement/census/selftest receipts.
- Scorecard, round LOG entry, and final measured-counter receipt: commit `76ad9cf30ddd626285ee34fb5a609020b02b3df6`. The Round-58 LOG entry is in `mori-shokunin/LOG.md`; the SCORECARD section cites the exact measurements below. `jj-lane.sh push` completed and `ls-remote origin refs/heads/master` returned `76ad9cf30ddd626285ee34fb5a609020b02b3df6`.

## Claim measurements and verdicts

**C1 — calibration.** Baseline: the C1 round-58 counter did not exist in the entering tree (`git cat-file -e b783d0b8:.ufo/waves/round-58/count-c1.py`, exit 128); the prior frozen counter returned `C1=unmet rows=0 evidence=bad`, exit 1, against entering bytes. Counting command: `python3 .ufo/waves/round-58/count-c1.py R`. At measured data commit `7d317495245fec896c6ee7214d8eb995ad2302ba`: `C1=met rows=2 pointers=ok manifest=ok binding=ok failed=none rev=7d317495245fec896c6ee7214d8eb995ad2302ba`, exit 0. **Unverified**: frozen contract line 30 requires `selftest=ok` in this output, but `count-c1.py` emits `failed=none` and cannot emit the required token. W1 also demonstrated false greens: pointer roots were not constrained to the allowed target; empty/unbackticked pointers and duplicate/missing keys passed; the MANIFEST arm used live fleet state and substring hints rather than exact revision-pinned binding; and a decoy register section could satisfy the search. Separate explicit-TMPDIR C1 selftest passed 4/4, but does not close those defects.

**C2 — depth.** Baseline at entry/freeze: `C2=unmet entry=absent failed=entry`, exit 1. Counting command: `python3 .ufo/waves/round-58/count-c2.py R`. At measured data commit `7d317495245fec896c6ee7214d8eb995ad2302ba`: `C2=met claims=11 located=11 copy=ok tree=ok rows=ok sources=ok failed=none rev=7d317495245fec896c6ee7214d8eb995ad2302ba`, exit 0. **Unverified under its frozen kill rule**: W1 showed that frontmatter-less body strings satisfy `sources=ok`/C2=met; it also demonstrated duplicate-claim, quote-laundering, substring-backlink, newline-normalization, and extra-column false greens. The 11 distinct K-claims were manually checked against their source lines, but the frozen instrument does not establish its specified target. Explicit-TMPDIR C2 selftest passed 6/6; it does not close the control failure. Neither contract nor counter was edited after freeze; neither claim is admitted and no score is raised. Exact outputs and control results: `.ufo/waves/round-58/evidence/landed-measurements.txt` and `selftest-scratch.txt`.

## Sources and frontier

SOURCES census started at 322 rows and ended at 325 rows; the final validator exited 0 (`census-start.txt`, `census-start-rows.txt`, `census-end.txt`). New rows by tier: A=2 (S550 own-work parser implementation, S552 full-text tracepoint); C=1 (S551 scope-rejected paper). No prior row status/recheck/used-by cells changed. S262 was reaffirmed present. Quarantine review: S244 unverifiable (no intended quote/locator in its row), S262 present, S268 present (W1 located the PDF; its page/quote is recorded without an unverified section label). No `merge/mori` assimilation and no frontier movement claimed. The S552/S262 duplicate-DOI/scope concern is recorded as a warning, not silently merged.

## Trend verdicts

- **Expansion — improved:** the entry adds 11 source-located implementation details and two A-tier source rows; this is content expansion, not a counter-validated admission.
- **Quality — unprovable-but-better:** explicit scratch-scoped selftests pass and W1 made frozen false-greens concrete, but both frozen claims remain unverified and no quality score was raised.
- **Discernment — improved:** kept S244 unresolved rather than upgrading it without a locator, reaffirmed S262/S268 on source evidence, and rejected S551's out-of-scope support rather than assimilating it.

## Controls, L0, and inherited state

Initial selftests inherited the environment TMPDIR, so that first scratch path is unknown. They were rerun under `/fast/scratch/hyaku/mori-r58/L1-controls` (C1 4/4, C2 6/6) and cleaned. The frozen counters honor TMPDIR but have no explicit `--scratch` CLI option; this residual is recorded in the lesson. QUALITY criterion 154 records the C1 output/target mismatch.

The live host role map differs from the prompt map: `~/.omp/agent/config.yml` routes connector `@m_haiku`, reviewer/mutation-tester `@m_zfl`, and critic/scout `@m_kfc`; no model overrides were passed. This was filed as an L0 question in `fac6534aba55f758607332c3ee973b6428de976e`. Earlier open L0 questions carried forward: R1 remote-URL disposition (an origin is present), R25 cap-text conflict, R26 public-history disposition, R38 grace-kill tradeoff, and R42 S262 tier policy. None prevented completing this round. No tools were installed; `/home/vgpnk/.omp/agent/RULES.md` was read and pacman was not run per the addendum guard.

Stale-lane observation: launched `2026-10-27T13:47:08-03:00`; filing at `2026-10-27T15:28:30-03:00` after incremental lane commits; no separate Mori mission remained open. Final fleet sweep showed only other-lane/unowned state: modified `.ufo/reports/round-58/chousa.md` and untracked `.scratch/closure-mado-r50.json`, `.scratch/source-routing-queue.md`, `.ufo/reports/round-76/kotoba.md`, `.ufo/waves/round-75/`, and `kotoba-shokukin/`. These were not edited or included in the lane commits.

## SHONEN

- [ ] `SKILL.md` decision tables, error patterns, checklists, and cited sources — untouched in R58; `kotodama-shokunin/SHONEN.md:5-6`.
- [ ] End-to-end domain task and LOG record for Kotodama — untouched in R58; `kotodama-shokunin/SHONEN.md:7-8`.
- [ ] Instructions executable without oral context — untouched in R58; `kotodama-shokunin/SHONEN.md:9-10`.
- [ ] No cross-domain bleed; PROVINCE.md accurate — untouched in R58; `kotodama-shokunin/SHONEN.md:11-12`.
