# souji — round 77 report (attempt 1, L1 `SoujiR77`)

Lane `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Work tip before the domain trial: `adc113893a327ba0f8771e818b877a8adc0bcd23`. The final lane hash, which adds only the domain-trial receipt, is the last line of this report. `git ls-remote origin refs/heads/master` prints that hash.

## Work performed

There are two declared claims. They were frozen in `census/round-77/preregistration.txt` at freeze `a9979807fd5d9f80851c0f1fc6481e9bf0334644` (Q99 grammar). Every control receipt was committed one commit earlier at `43822328ec27b429b68c21d9c3a995e0a09b9d77`, with `rev=` the lane base `d4f51563`, before any candidate byte.

- **C1 — operability** (surface: `tools/souji-pre-report-gate.sh` check 4; **sourced claim** on S321, git dir.c `add_patterns` at v2.56.0, opened this round).
  - Before: git opens exclude and attribute files with a blocking open(2), so a FIFO `.gitignore`, `.gitattributes`, `info/exclude`, `info/attributes`, `core.excludesFile` or `core.attributesFile` held the lane-base gate forever (S76Sentinel MEDIUM-2).
  - Now: the gate refuses any such source that is not a regular file, with `RECEIPT-NONREGULAR-SOURCE`.
  - Target: the frozen 16-row counter goes from mismatches 9 and hangs 8 to 0 and 0. Controls K-b, K-c and K-d stay red, r76 holds 30/30, r36 21/21 and r27 4/4, and a domain trial runs on the lane.
- **C2 — calibration** (the lowest owned axis, at 7; surface: the lane's self-assessment files compared with observed repo state).
  - Before: the lane's pointer check over SCORECARD.md, SKILL.md, SHONEN.md, corpus/QUALITY.md, corpus/README.md and PROVINCE.md printed `missing=35` at the base.
  - Now: each finding resolves to a class the frozen counter verifies against git objects, the lane disk and the fleet root. Local-only wave evidence with no committed copy is captured at the path the row cites.
  - Target: resolved goes from 0 to 35, four forgery controls stay red, and the pointer check moves from missing 35 to 31.

Work items:

- **Fresh state.** The watchdog shows `launch souji round=77 … attempt=1` and no `lane-dead-no-report souji round=77`. `jj-lane.sh state` at start read `local=remote=d4f51563… ahead=0 tracked=0 untracked=0`. There were no inherited leftovers.
- **r76 spot-check.** Routed defects 1-5 are mapped in `corpus/lessons/round-77.md` `## Inherited`:
  - 1 and 2 (the trial-script digest and the graded report bytes): `census/round-77/probes/domain-trial.sh` refuses to run except at its committed path. Its receipt binds `trial_script=… sha256`, the script blob at master, and `report_lines=N report_sha256` of the graded bytes, so a verifier can recompute them with `head -n N <filed report> | sha256sum`.
  - 3 (kill power): rows o1-o2 kill M09 (`controls/c1-K-c-m09-one-path.txt`). K03/K04 are routed to r78.
  - 4: taken as C1. The r75 excludesFile arm is partly addressed by n4, o3 and p2.
  - 5: report only.
- **Pre-freeze feasibility (Q70) in scratch** found three instrument or label errors before P (lesson M2, M3):
  - the C2 range rule;
  - C2 ABSENT accepting parse artefacts;
  - a `.gitmodules` row git never opens (dropped) and the o3 class.
- **Staged chronology:** P `43822328` → F `a9979807` → W `9b496b08` (gate) → K `6690cb5a` (capture of 14 files) → L `8bf42fc6` (ledger) → A `ef04ca6c` (after-arms) → wave repair R `844b2d70` → integration `e104ef24` → `adc11389` (census-after) → domain-trial receipt (final hash).
- **Freeze check.** `python3 -B tools/souji-freeze-check.py --root . --prereg census/round-77/preregistration.txt --rev a9979807… --substance --chronology` → `SUMMARY claims=2 findings=0` (`census/round-77/records/freeze-check-at-F.txt`). S77Reviewer re-ran it at F and at A with the same result.
- **Wave w1:** 12 seats, 0 dead. Every frozen number was reproduced from committed bytes (`census/round-77/records/wave-w1/seats/`).
- **Wave repairs after measurement** (`844b2d70`; receipts in `census/round-77/records/wave-repair/`):
  - Fixes:
    - common-dir `info/exclude` and `info/attributes` via `rev-parse --git-path` (S77Reviewer MEDIUM-1, S77Sentinel MEDIUM-1);
    - symlinks counted by their target with `-xtype f` (S77CriticClaims, S77ScoutSources);
    - a failed scan now fails closed (S77MutGate F5);
    - `/dev/null` is allowed (S77Reviewer LOW-3);
    - the index and `info/sparse-checkout` are checked (S77ExecEvade f3/sp1);
    - the pre-check's git calls are timed (S77Sentinel MEDIUM-2, partly);
    - `git status` runs with `core.fsmonitor=false` (S77Sentinel LOW-4).
  - `repair-probes.txt`: `SUMMARY arms=10 as_expected=10` for W against R. The frozen counters still read 0 at the repair: `c1-at-repair.txt` 16/16, and `regress-r76/r36/r27-at-repair.txt` 30/30, 21/21 and 4/4.
- **Domain trial.** The repaired gate ran over the lane at the report tip through the committed trial script (`census/round-77/records/c1-domain-trial.txt`; result under Before → after).
- **Frontier step.** S321 and S322 were opened by the L1 and re-fetched by S77ScoutSources and S77Scribe; the sha256 values match. Six mistakes were mined (lesson M1–M6). The sourced claim is C1.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*` (orchestrator-owned) and `?? trail-ids.txt` (pre-existing, not this lane's). S77Sentinel self-reported one probe script briefly written at the fleet root and removed it the same minute; nothing remains.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `43822328ec27b429b68c21d9c3a995e0a09b9d77` | P: C1 counter and population, C2 counter and population (frozen disk digests), rec.sh, control variants, controls C1 K-a..K-d and C2 K-a..K-e, S321/S322 captures, census-before | LOG "## Round 77", bullet "Controls … freeze" |
| `a9979807fd5d9f80851c0f1fc6481e9bf0334644` | F: preregistration | same bullet |
| `9b496b0883b255573175726f1463ce5634960a04` | W: gate non-regular-source pre-check and timeout backstop | bullet "Candidates" |
| `6690cb5ad96d11a7b528a62a98ba42fad7783d35` | K: 14 local-only wave-evidence files captured at their cited paths | bullet "Candidates" |
| `8bf42fc6233cc4fee28c170d57e5d38a80f6d2bc` | L: pointer ledger (31 rows) | bullet "Candidates" |
| `ef04ca6c66af02b98bc061290b8028c6c0654a4b` | A: after-arms, regressions, freeze-check receipt | bullet "Candidates" |
| `844b2d70afebad97ba68c620c0d486c76cd84c2b` | R: wave repair of the gate; repair probes; domain-trial script; repair-probe run 1 (8/9) | bullet "Wave w1" |
| `e104ef24f5edacf5ff5a56d256b34fe1a5a495ad` | S321/S322, Q138/Q139, knowledge r77 and the new pointer-resolution entry, README frontier, SKILL/SCORECARD/LOG rows, lesson, repair receipts, wave mirror | bullets "Frontier", "Wave w1" |
| `adc113893a327ba0f8771e818b877a8adc0bcd23` | census-after; pointer-free wording in the new docs | bullet "Frontier" |
| final hash (last line) | domain-trial receipt | bullet "Domain trial" |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-77/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=16 mismatches=9 errors=0 hangs=8`, EXIT=1 (n1-n7 and n10 HANG at the 30 s bound; n8 is the policy row). Refuse-all `c1-K-b` 7, M09 `c1-K-c` 11, blanket `c1-K-d` 7, all EXIT=1 | `census/round-77/records/c1-after.txt`: `SUMMARY rows=16 mismatches=0 errors=0 hangs=0`, EXIT=0. `c1-regress-r76.txt` 30/30, `c1-regress-r36.txt` 21/21, `c1-regress-r27.txt` 4/4. Identical at the repair. Domain trial: `census/round-77/records/c1-domain-trial.txt` | `python3 -B census/round-77/c1-nonreg-counter.py --gate-dir DIR --work WORK` | `9b496b0883b255573175726f1463ce5634960a04` (gate blob `28a51355…16be`); repair `844b2d70` |
| C2 | `census/round-77/controls/c2-K-a-no-ledger.txt`: `SUMMARY items=35 resolved=0 unresolved=35`, EXIT=1. Blanket ABSENT refused 31, local-only refused 4, stub capture mismatched 4, name-only MOVED refused 3, all EXIT=1 | `census/round-77/records/c2-after.txt`: `SUMMARY items=35 resolved=35 unresolved=0 refused=0 mismatched=0 errors=0`, EXIT=0. Pointer check `records/c2-pointer-check-after.txt`: `missing=31` | `python3 -B census/round-77/c2-pointer-counter.py --root <lane> --rev <rev> --fleet-root /home/vgpnk/Projects/shokunin --ledger census/round-77/c2-pointer-ledger.tsv` | `8bf42fc6233cc4fee28c170d57e5d38a80f6d2bc` (re-run at A by S77ExecC2: identical) |

Both frozen predicates are met, and each beat its committed do-nothing control. No owned axis score changed (calibration 7, coverage 8, operability 8).

Qualifications from the wave (for the operator to rule on):

- **C1 before count.** 9 = 8 hang rows plus n8, a FIFO in an ignored directory that git never opens and that is refused by ruling. On the hang rows alone the result is 8 → 0 (S77CriticClaims).
- **C1 rows that do not discriminate.** o1-o3 and p1-p4 pass on the base too. They guard against mutants and are not evidence of the change.
- **C1 branches without frozen rows.** The 300 s backstop and the XDG and relative-path branches have no frozen row (S77MutGate F1-F3). The repair probes now cover XDG, relative path and the fsmonitor timeout outside the frozen counter.
- **C1 out of surface.** FIFO `.git/config`, `include.path`, `HEAD`, `packed-refs` and `config.worktree` hang check 1 before the pre-check. SIGTERM leaves check-4 children running (S77ExecEvade, S77Sentinel MEDIUM-2/3). Routed to r78.
- **C2 is thin** (S77CriticClaims MEDIUM). 31 of 35 items resolve with no new byte, and a mechanical 30-line ledger generator reaches 35/35. Only 4 items (2 artifacts) are new bytes. 17 items are verified by bytes; 18 are verified by existence, absence or parse (S77CriticDiscern).
- **C2 counter kill power** (S77MutCounter HIGH-1..3). The controls are red only in aggregate, so 9 of 10 counter mutants survive them. Six forged single rows pass the frozen counter:
  - the QUARANTINED target is unbound;
  - TOKEN checks only the prefix;
  - MOVED checks byte identity but not location;
  - R0 is never exercised.

  Routed to r78 as a successor counter.
- **C2 durability.** P15/P16 rest on empty-directory digests and will stop resolving at the lane's next quarantine.

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Before: `census/round-77/records/census-before.txt`, `souji ok`, 86 W04, EXIT=0.
  - After: `census/round-77/records/census-after.txt`, `souji ok`, 86 W04, EXIT=0.
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 243 → 245.
  - Added: tier A ×2. S321 is git dir.c `add_patterns` at v2.56.0 (code, `mined`), cited by `corpus/knowledge/filter-filemode-witness.md` r77. S322 is git-add(1) `--force` at v2.56.0 (docs, `mined`), cited by `corpus/knowledge/self-assessment-pointer-resolution.md`.
  - Rejected: one anchor, dir.c line 1169, because its `||` breaks the census grammar; it is paraphrased instead.
  - Rows touched old→new: none.
  - Corrections from S77ScoutSources were applied before landing:
    - add_patterns never tests the file type;
    - S322 no longer attributes jj semantics to git-add(1).
- **Frontier advanced.** README "Frontier (r77 non-regular exclude sources and self-assessment pointer resolution)". It stays frontier.
- **Mistakes mined:** six (`corpus/lessons/round-77.md` `## Mistakes` M1–M4 and `## Mistakes (wave)` M5–M6). Each fix was shown able to fail, or was caught by a computed verdict.
- **Assimilation: none.** `considerthese/` is absent in this lane, and no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved.** There are two new tier-A rows on ground the lane did not hold: how git opens exclude files, and capturing ignored files at their path. There is one new knowledge entry (pointer resolution) and one new section, plus QUALITY Q138/Q139 and two SKILL gate rows and two capability rows, each demonstrated running.
- **quality: improved.** Seats found seven gate defects (common dir, symlink-by-target, dead scan-failure path, `/dev/null`, index/sparse-checkout, untimed pre-check calls, fsmonitor in status). Each was repaired with W-vs-R receipts that can fail (`repair-probes.txt` 10/10, run 1 kept at 8/9). The frozen counters stay at 0 at the repair.
- **discernment: improved.** The lane self-assessment now carries verified receipts for every pointer it made. The L1 kept its own pre-freeze instrument errors and a wrong probe expectation on record (M2, M3, M5), and accepted the critics' "thin C2" and "aggregate-red controls" findings as qualifications instead of re-scoring.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r77 pre-report gate non-regular-source counter (C1)" and "r77 self-assessment pointer resolution counter (C2)" (`e104ef24`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 77". The pointer census over the lane's own artifacts captured 14 local-only files (`6690cb5a`), and the gate ran over the lane at the tip (`census/round-77/records/c1-domain-trial.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: seven seats re-ran the prereg commands as written and reproduced every predicate (`census/round-77/records/wave-w1/seats/S77ExecC1.md`, `S77ExecC2.md`, `S77Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling gates and self-assessments were documented, not edited (`census/round-77/records/wave-w1/seats/S77Connector.md`), and there is no fleet misroot.

## Other

- **Round shape:** one v1 wave `w1` of 12 seats, validated under `ufo-wave-policy.json` (band 8–16) and dispatched via the inline handoff (`census/round-77/records/wave-w1/w1.ready.dispatched`). WAVE-DONE was received. There was no residual call; the round total is 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1.
  - Attack seats: 5 of 12 (42 %).
  - The L1 holds the §3 planner seat.
- **Dead seats:** 0. All 12 wrote report files.
- **Routed to r78:** see the lesson section "Routed to round 78" (a)–(c) and SCORECARD "r78 (planned)".
- **Open L0 questions:** none new.
- **Tool installs:** none. There was no pacman transaction and no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r77/` was removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.

Domain trial (C1 conjunct): `census/round-77/records/c1-domain-trial.txt` — `check-tip=PASS check-report=PASS check-shonen=PASS check-clean=PASS check-prereg=PASS`, `EXIT=0`, gate blob `5d08f547…df55a` (the repaired gate, amendment over the W blob `28a51355…16be`), trial script sha256 `5f199c54…2e5d` equal to its blob at master; it graded the first `report_lines=131` lines of this report (`head -n 131 | sha256sum` = `6d56f71b…d669`); the lines from this paragraph on were appended afterwards. `wall_seconds=` is empty (the trial script calls `bc`, which this host lacks; routed r78).

Final lane hash: a5a186667ea8f790bdcb313e6acb06683bed345e
