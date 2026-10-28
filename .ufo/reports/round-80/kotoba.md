# Kotoba round 80 — honest stop, sourced frontier landed

## Work performed

Declared claims: **C1 consistency/calibration** — the tip battery at the round base (1 of 6) should reach 6 of 6 under the frozen amended counter; **C2 depth, sourced** — a per-client `allowed-tools` matrix, with the form backbone measured and grant-semantics rider exploratory.

- Froze the plan and the one-v2-wave spec before dispatch (`kotoba-shokunin/plans/round-80.md`; freeze-shas receipt committed at `559919366daf521883d7eba53b4f3bacb06cf440`). Base was `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; round shape: one v2 wave, 64 seats. The canonical §3 planner seat was the L1; attack share was 17/64 = 26.6% (6 critics, 6 reviewers, 4 mutation-testers, 1 sentinel); 3 connector seats. Evidence: `.ufo/waves/round-80/w1-dispatch.json`, `.ufo/waves/round-80/w1-results.json`.
- All 64 seats settled; 0 dead seats. Role mix: executor 16, scribe 17, scout 9, connector 3, critic 6, reviewer 6, mutation-tester 4, sentinel 1, simplifier 1, revenger 1. See `.ufo/waves/round-80/w1-results.json` and `.ufo/waves/round-80/build/Kb80S14WaveRegistry.md`.
- C1 was falsified by critic C01: three new shortcut worlds each reached 6 of 6 on the frozen amended counter — a real absent lane commit masked by a lane marker, a dead hash in a lane-owned URL row, and a seven-byte marker substituted for the fleet report target. Receipts: `.ufo/waves/round-80/build/Kb80C01C1-canonical-lane-at-tipbattery.txt`, `.ufo/waves/round-80/build/Kb80C01C1-canonical-lane-url-tipbattery.txt`, `.ufo/waves/round-80/build/Kb80C01C1-canonical-fleet-marker-default.txt`. The kill rule fired; the unsafe E04/E05/E06 C1 stack was not landed.
- Landed the safe partial repairs and C2 documentary artifacts: the registry/citation/index fixes, C2 counter/entry, author-facing SKILL rule and PROVINCE Core bullet. No C1 battery pass is claimed. The final C2 counter reads 6 of 6 on form and prints a 6 of 6 generator score; this establishes documentary form only, not runtime permission semantics.
- Ran the sources census before and after and hand-checked the kotoba quarantine slice; no assimilation rows were adopted. `considerthese/2026-10-26.md` proposals 2–5 were dispositioned, not implemented.
- Fleet misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only unrelated chousa/mado/operator artifacts and `o.bin`; none named kotoba round 80, and none was touched. A lane-root stray `.ufo/wapes` is a C2 quote-probe artifact written outside the wave directory; it is left untouched and reported as a scope defect.

## Landed changes

- Safe partial C1 repairs plus C2 documentary package (C2 counter/registry row, entry, SKILL.md rule, PROVINCE.md Core bullet, SOURCES.md old→new cells and new rows, README coverage/frontier note, Q75): lane commit `9a16e9d7e3f239dc922508bed2ae09ceac318fb1`; LOG entry `LOG.md` § Round 80.
- Corpus baseline re-recorded with `report_dead` and `commit_unresolvable` explicitly carried at expectation 0 (residuals remain red): lane commit `26f7d7a8e76486e0f90831801edbeea056efb2b9`; receipt `.ufo/waves/round-80/receipts/baseline-refresh.txt`.
- Settled dispatch, 64 seat reports, build/control receipts and freeze evidence: lane commit `b5bd8b7aafd195ca2338486cb1ca1ce115b720bd`; wave results `.ufo/waves/round-80/w1-results.json`.
- Honest-stop lesson, scorecard annotations, LOG record and final-head measurement receipts: lane commit `40c7fb5ba2f635f16d014fc5ec4a9d615a3d36b1`; LOG entry `LOG.md:2835-2845`. Final lane remote reports the same hash.
- Not landed: the amended E5 counter and E04/E05 instrument stack. C01 W8–W10 falsified their external-classification/report-target assumptions; the amended scratch stack's 6 of 6 is not an admissible after-value.

## Before → after measurements

- **C1 consistency, killed / unprovable.** Frozen command: `python3 -B verifiers/check_tip_battery.py --rev <rev>` with the amended counter. Base `398cbe1...`: `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 (`receipts/tipbattery-base-dot.txt`). A scratch stack printed 6 of 6, but the predeclared adversarial controls W8–W10 also printed 6 of 6, so the target is control-reachable and the claim is killed. The safe partial final lane tip `bd036252567a0342e2dd29cdc9b1cbdccdcc876e` reads 4 of 6, guards 5 of 5, exit 1 under the original counter, in both forms (`receipts/final-head-dot.txt`, `final-head-abs.txt`); this diagnostic is not an admitted C1 after-value.
- **C2 depth, form measured / semantic rider unprovable.** `python3 -B verifiers/check_allowed_tools.py --rev <rev>`: base `398cbe1...` → `allowed-tools surfaces documented 0 of 6`, generator world 6 of 6, exit 1 (`build/Kb80E07C2Counter-base.txt`); final measured revision `bd036252567a0342e2dd29cdc9b1cbdccdcc876e` → `documented 6 of 6`, generator world 6 of 6, exit 0 (`receipts/final-head-c2.txt`). The generator reaches target, and the frozen headline is explicitly form-level. The grant-semantics rider has no named non-author reviewer on record; no depth score move is claimed.

## Sources & frontier

`SOURCES.md` rows before → after: **157 → 174**. Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 157 before, 174 after. Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0 before and after; final output `kotoba ok`, 31 W04 duplicate-URL warnings (`receipts/census-before.txt`, `receipts/census-after.txt`). Rows added by tier: A=0, B=1 (S248 queued), C=16 (S232–S247 rejected). Existing rows touched: S226–S231 `used-by` changed old `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md`; no existing status or recheck cell changed. Frontier advanced by one documentary `allowed-tools` form area into the coverage map/Core; no client runtime behaviour is held.

The sourced C2 entry rests on S226–S231, each re-opened this round. S230's inherited anchor misattributes a Mistral Vibe revision to pi-mono; the entry and lesson record the mismatch, and the append-only anchor cell was not rewritten. The staged shokuknow package was not adopted (ID overlap); the 13-row quarantine slice was hand-checked (7 payload-absent refusals, 6 unreachable, 0 adopted). Assimilation: none. `considerthese` proposals 2–5: dispositions recorded, none implemented.

## Trend verdicts

- **Expansion: improved** — one new documentary entry on previously uncovered `allowed-tools` surface ground, indexed and named in PROVINCE Core; 17 new source rows recorded.
- **Quality: unchanged** — no existing knowledge entry was re-verified, deepened or superseded; the new entry is documentary, not runtime evidence.
- **Discernment: unprovable-but-better** — the C1 false-green controls were turned into lesson M80-4 and Q75, but no outside non-author spot-check of this round's admits/rejects has yet occurred; the C2 semantics rider remains unprovable.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources — re-derivation `.ufo/waves/round-80/build/Kb80S06Shonen.md` Box 1; no promotion claim.
- [~] End-to-end domain task logged — `.ufo/waves/round-80/build/Kb80S06Shonen.md` Box 2; historical cold-run record remains the evidence.
- [~] Executable instructions — `.ufo/waves/round-80/build/Kb80S06Shonen.md` Box 3; no fresh non-author cold run.
- [~] No cross-domain bleed — `.ufo/waves/round-80/build/Kb80S06Shonen.md` Box 4; sibling scan `.ufo/waves/round-80/build/Kb80R04SiblingScan.md` found no lane-authored sibling matrix.

Stale-lane: respawn-per-round; no other lane mission is open. Final pushed lane HEAD: `2c231e575abbafb8826530b1822a5c16b5acfd12`.
Tool installs: none. Open L0 questions: none.
