# kama round 51 report

author: kama L1 (agent `KamaR51a2`)
date: 2026-10-27
attempt: 2 (watchdog: `2026-10-27T00:16:15-03:00 lane-dead-no-report kama round=51` for attempt 1, which was killed in the orchestrator session exit and left no lane writes or waves; nothing inherited, nothing reused; `2026-10-27T00:16:24-03:00 launch kama round=51 ... attempt=2`)
base: `57a2e25bf702b03aa61f9265e968cf68058ecb82` (round-50 verifier spot-check; lane remote tip at launch)
freeze: `804bde75164444bdf0fe6783d7aa45774bf562bd` (preregistration `.ufo/waves/round-51/preregistration.json`; KQ64 receipt `freeze/prereg-time-check.out` → `RESULT fail`, exit 1: `frozen_at_utc` 03:38:30Z is 6 s after the 03:38:24Z commit time; erratum `freeze/frozen-at-erratum.md`; freeze time of record = commit time)
build: `b6bed925b032ac2c19b63ef4af358ebdd5922c26`; build-fix `73bf2a7a17104a62a3e442912c8776cbd8dedbd5`; build-fix 2 `138af25b963450b6520794995605fa7dbbcd87e0`
integration: `c5ec93d5b8b8759d5c2fa7a092c7375c875b04bc`; post-wave fixes = measured commit `be8169a667301dc2b8118615e262968266959303`
lane tip: `b1d7b7aee5d05ffb43f99cf4bc20af00fc6865c6` (`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` → `ahead=0 behind=0`)
Stale-lane: progressing. The driver respawns the lane each round; no other mission of this lane is open.

## Round shape
One v2 wave `kama-r51-a2w1` (fresh name; attempt 1 had no waves), 66 seats, validated under policy v2 with exit 0 (`.ufo/waves/round-51/a2w1/dispatch.json`, `validate.out`; spec committed `4eca4892`). Ready file written 2026-10-27T03:46Z; markers `a2w1.ready.partial` then `a2w1.ready.dispatched`.
- Role mix: executor 18, reviewer 11, critic 9, scribe 7, mutation-tester 5, scout 5, sentinel 4, connector 4, revenger 2, simplifier 1. Attack share (reviewer + critic + mutation-tester) 25/66 = 38%. Live route map recorded by seat Sen4Policy (config mtime 2026-10-27T02:39:08Z, sha256 `0d587466…`): executor `@m_mim`, reviewer/mutation-tester `@m_zfl`, critic/scout `@m_kfc`, connector `@m_antigravity`, scribe/sentinel/revenger/simplifier `@m_flash`.
- **Honest status at filing:** WAVE-DONE had **not** arrived. The run hit its request budget (operator budget notice), so the round was landed with **50 of 66 seat reports** in hand (committed in `1ab1de39`, `.ufo/waves/round-51/a2w1/out/`). Still running at filing: Sen1Exe, M1Ctr, M2Live, V1Review, K2Design, V3Review, Rev2Arow, Sen3Ledger, L6Slice, T1Lesson, T4Quality, T6Skill, X3R41, X5Census, Sim1, X8Restore. Their findings are not in this round's record; no seat has been reported dead. `w1-results.json` does not exist yet. This breaks the "no report before WAVE-DONE" rule; the operator budget notice took precedence. No residual call. **Round total: 66 seats dispatched.**
- Planner seat: held by the L1 (the validator rejects `planner`); planning data-walk rode on connectors N2Couple, N3Pattern and on seat T2Scorecard.

## Work performed
Two claims, frozen at `804bde75` before the build commit (preregistration discloses that both counters were written alongside the build and that C2 was dry-run once in a scratch-clone commit before the freeze):
- **C1, operability 8→8, sourced on S499 (proc_pid_exe(5)):** the replay's server is the file the replay extracted. The live tool records `server_exe` (the running image opened through `/proc/<pid>/exe`: dev, inode, digest), and the replay refuses a rerun whose image is not its own `<work>/server/<member>`. This closes round-50 closure R6 / seat J4Decoy (a host-install exec met the round-50 counter). Counter `tools/round51-replay-exe-audit.py`.
- **C2, calibration 7→7 (the lowest-scoring assigned axis):** append-only-audit v6. Default threshold 1 (v5 saw 5 of 106 deletion events). A-row status/recheck/used-by edits are `permitted`. `registry/append-only-disclosures.tsv` names every graded line gone at the tip; a bad row exits 1. This closes round-50 R6 (the sub-20 threshold hid the real `LOG.md` loss at `ed135b3c`) and takes `considerthese/2026-10-26.md` proposal 1. Counter `tools/round51-append-audit-v6-check.py`.

Work items:
- **Protocol load:** `skill://godspeed`, `skill://swarm`, `skill://shokunin`, the round prompt, AXES.md, SCORECARD (§Planned round 51, §Round 50), round-50 report, `corpus/lessons/round-50.md` and `round-50-verifier-spotcheck.md` (R1–R7), `considerthese/2026-10-26.md`.
- **Source opening (2026-10-27T03:27:36Z):** proc_pid_exe(5) (`.ufo/waves/round-51/c1/proc_pid_exe.5.txt`). Row S499 is in `corpus/SOURCES.md:252`.
- **Freeze `804bde75`:** both counters, preregistration, base controls (`controls/base.c1.out` `bind=1 own=0 teardown=1 newrow=0 met=False`; `controls/base.c2.out` `fixture=0 lane=0 scenarios=0/9 met=False`), start census, S499 capture.
- **Build `b6bed925`:** `server_exe()` and the replay's own-member check; aoa v6 with the ledger (`c2/build_ledger.py`); S499. A defect found during the build: the disclosure loop shadowed the commit index. The selftest `v6-two-files-one-commit` fails on the buggy copy (`c2/shadow-index-proof.out`).
- **Build-fix `73bf2a7a`:** the S499 edit restored the blank line `97c864be` had removed, so that line's ledger row became an over-count. Ledger regenerated.
- **Build-fix 2 `138af25b`:** digest-ledger leaves the disclosure ledger's line keys out of scope, because v6 re-derives them. Without this, unknown would have been 166.
- **Integration `c5ec93d5`:**
  - SCORECARD: round-51 section, banner, and re-anchors of the calibration row (37 spot-checks) and the depth row (SKILL `3b2425b7…`, 1541 lines, 39 headings); both rows now read `evidence re-anchored round 51`, which also closes R3. The round-49 banner, which round 50 replaced without appending (a v6 finding), is appended under §Superseded head banners.
  - SKILL `## Round-51 instrument registry`; LOG entry; lesson `corpus/lessons/round-51.md`; QUALITY KQ85–KQ88; README frontier disposition plus a stale-sentence correction (K4Calib).
  - Wave-driven hardening: the ledger discloses only commits before its own introduction (K2Cheat). The replay holds its member fd across exec and refuses `st_nlink != 1` (K1Design3, J4Hardlink). An unwritable `--out` now exits 2 (X1Fresh). Four selftest cases kill M3Tool survivors.
  - hexrun ledger rows for the two carried fleet-commit unknowns (X4Hexrun).
- **Post-wave `be8169a6`:** `server_exe` records read errors (V2Review LOW-1); digest-ledger in-scope selftest kills 5 surviving scope mutants (M5Digest).
- **Routed closure items:**
  - R1, R4, R5 → errata in the lesson.
  - R2 → receipts committed at the measured commit (`measured/*.out`).
  - R3 → depth and calibration `Last change` re-anchored.
  - R6 → C1/C2; the rest carried.
  - R7 → Sen4Policy recorded the route map and its mtime.
- **Assimilation:** none adopted. Pre-check by seat T8Assim: the guard is proven, and the same 9 staged-id collisions as round 50 remain, so nothing is appendable as shipped.
- **considerthese:** `2026-10-26.md` proposal 1 was taken (C2). Seat T9Considerthese: the "morning-after" monitoring part is not done.
- **Tooling:** no installs by the L1 or (per their reports) by seats. No pacman.

## Landed changes
Every hash is a `landed` line from `jj-lane.sh`; all are tied to `LOG.md` §Round 51.

| Change | Lane commit |
|---|---|
| Freeze: counters, preregistration, base controls, start census, S499 capture | `804bde75` |
| Build: server_exe + own-member check, aoa v6 + ledger, S499, freeze receipts | `b6bed925` |
| Build-fix: ledger regenerated | `73bf2a7a` |
| Build-fix 2: digest-ledger scope | `138af25b` |
| Wave a2w1 spec, dispatch, build battery receipts | `4eca4892` |
| Integration (SCORECARD, SKILL, LOG, lesson, QUALITY, README, tool hardening, hexrun rows, ledger) | `c5ec93d5` |
| Post-wave fixes (measured commit) | `be8169a6` |
| Measured results, receipts, wave seat outputs | `1ab1de39` |
| End census, misroot sweep | `b1d7b7ae` |

## Before → after measurements
- **C1 operability 8→8: met.**
  - Command: `python3 tools/round51-replay-exe-audit.py --repo <fresh clone> --tip <commit> --scratch <dir>`.
  - Base `57a2e25b`: `bind=1 own=0 teardown=1 newrow=0 bound=3/3 owned=0/3 met=False`, exit 1.
  - Measured `be8169a6`: `bind=1 own=1 teardown=1 newrow=1 bound=3/3 owned=3/3 met=True`, exit 0 (`.ufo/waves/round-51/measured/c1.out`). It is also met at `c5ec93d5` and `73bf2a7a`.
  - Independent: R1Rerun (2× met at build, base met=False). Controls met=False: J1NoRecord, J2DecoyHost (`own=0`).
  - Not shown: a byte-identical copy at the member path meets the counter (K1Cheat3, J3CopyDecoy; preregistered limit), and so does a hardlink of the host install in the counter's own leg (J4Hardlink; the replay now refuses it, the frozen counter does not check). Download is not observed. Snapshots are not atomic (K1Design3).
- **C2 calibration 7→7: met.**
  - Command: `python3 tools/round51-append-audit-v6-check.py --repo <fresh clone> --tip <commit> --scratch <dir>`.
  - Base: `fixture=0 lane=0 scenarios=0/9 met=False`, exit 1.
  - Measured `be8169a6`: `fixture=1 lane=1 scenarios=9/9 lost=142 disclosed=165 met=True`, exit 0 (`measured/c2.out`).
  - Independent: R2Rerun (2× byte-identical, base met=False), X7Regen (an independent ledger regeneration matches exactly), X9Agree (3/3 and 2/2 deterministic), and slice audits L1–L5 (every class mechanically right, no moved line missed). Controls met=False: J5NoLedger, J6NoArow, J7Thresh20, J8OneClass ×3.
  - Not shown: region-restricted files (SCORECARD head, two `only=` entries) are only bound-checked by the counter (J8 p1). Disclosures carry mechanical classes, not judged reasons. As frozen, the counter would accept a fresh disclosed deletion; the tool's cutoff now refuses it, but the counter does not test it.
- **Regressions at `be8169a6`:**
  - gate `registered 48 unregistered 0 defective 0`; capability census `listed 11 observed 11 met True`; r41/r42/r43 `mismatches=0 met=True`.
  - digest `unknown=0`; hexrun `unknown=0` (base 2).
  - sao no violations; aoa exit 0; selftests AOA 51/51, KLR 27/27, live ok; round-50 C1 counter still met.
  - round-50 C2 counter `lane=0` (stated v6 supersession). Planned-pointer `met=True` at the final tip `1ab1de39`.

## Sources & frontier
- **Census validate** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`): start exit **0** (`.ufo/waves/round-51/census/start.out`); end exit **0** (`.ufo/waves/round-51/census/end.out`; codes `1 ok, 1 W01, 94 W04`, no `E`).
- **Row count** (`git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`): **239 → 240** (`57a2e25b` → `1ab1de39`). Correction for round 50 (R1): its line should read **236 → 239**.
- **Rows added:** S499 (tier A, mined, opened 2026-10-27T03:27:36Z; Gate in `corpus/lessons/round-51.md`). **Rows touched old→new:** none.
- **Frontier advanced:** the replay's server is bound to its own extracted file (exe identity); every append-only deletion is graded and every loss is named. Still frontier: the copy decoy and an unobserved download, the round-50 carried limits, the prerelease cliff (b11909 is still a prerelease while upstream is at b11913, Sc4Watch), and the b11906 population.
- **Sourced claim:** C1 rests on S499.
- **Mistakes mined:** five rows in the lesson:
  - the false prereg timestamp (KQ64 fired);
  - loop-index shadowing (selftest shown failing);
  - a same-round restoration that made a ledger row an over-count;
  - the round-50 banner sentence that was false for one round;
  - the R1 off-by-one.
- **Assimilation: none** (9 staged-id collisions persist; T8Assim).

## Trend verdicts
- **expansion: unchanged.** Capabilities stay 11 → 11 and no knowledge entry was added. One source row (S499) and the hexrun ledger rows were added.
- **quality: improved.** The replay's server identity is now the running file, not a digest. The audit sees every deletion, applies the A-row rule as declared, and binds each disclosure to a real line, with a cutoff against future laundering. Four harden-from-attack fixes landed. The battery is green and the hexrun unknowns went from 2 to 0.
- **discernment: unprovable-but-better (self-graded pending outside check).** Gate admit S499, plus four rejects grounded by controls. The slice audits judged 160+ historical in-place edits. Per KQ61, `improved` waits for the non-author spot-check.

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round-51 instrument registry and how-to; gate `registered 48 unregistered 0 defective 0` (`.ufo/waves/round-51/measured/gate.out`). Author assertion; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → three witnessed b11909 replays bound to their own extracted server (`.ufo/waves/round-51/measured/c1.out`; `LOG.md` §Round 51). A seat is not a non-author mark.
- [~] Instructions executable by an agent without oral context → seat X1Fresh replayed receipt-2 from the replay docstring alone (`match=True`, `server_exe`/`own_server` read; one `--out` defect fixed). A seat is not a non-author mark.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → seat Sc5Province: both surfaces are inside the province as written; seat N1Overlap: overlaps reported, not absorbed; `PROVINCE.md` unchanged.

Open L0 questions (routed around; none filed this round): `kama | round-35` (MISSION.md axes pair), `kama | round-39` (validator band and planner), `kama | round-41..43` (parked worktree).
