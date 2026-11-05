# kake — round 94 report (attempt 1; hyaku run 15)

Lane: kake (operability + freshness; calibration sub-axis). Repo: `/home/vgpnk/Projects/shokunin/kake-shokunin`, branch `master`.
Freeze commit (instruments and controls, before any seat scored): `ba667b245f26125c13885958498b3b4999756d04`.
Round base: `0f7d9bbcdd6a9ed36f5bc62b2116ddd040e871a8` (lane tip at round open).
Lane tip cited by this report: `99a88dea1f4fade18af18de12b4d57d86a0224f5` (`git ls-remote origin refs/heads/master` = the same hash, checked after the landing).
Verdict on the round: **honest stop** — both claims unmet as frozen. No claim admitted.
Stale-lane: no other mission of this lane is open; the round was launched once (attempt 1, no prior attempt in `.ufo/watchdog.log`); progressing (commits `ba667b24` and `99a88dea`, wave `w1` settled).

## Work performed

Declared claims (2, distinct axes; C1 on the lowest owned non-retired axis), frozen in `.ufo/waves/round-94/freeze.md`:

- **C1 — calibration (score 2, HOLD): the lane's machine-checkable self-assessment matches the repo state, under a strict successor counter.** Counter `.ufo/waves/round-94/c94_selfassess.py` (sha256 `58028584…8306a`); predicate: `met <=> pins ok AND zero mismatches E1–E5 AND battery refused 8/8 AND predecessor admits ≥ 2 of 7`. Base control: `mismatches=15 E5=15 … met=false`, exit 1 (`.ufo/waves/round-94/controls/base-c1.txt`). **Unmet**: no honest repair landed (see Landed changes; the repair route that reached 0 was rejected).
- **C2 — freshness (score 10, HOLD), instrument capability: the conditional-request counter's frozen population kills the nine mutant classes the round-93 population let survive.** Counter `.ufo/waves/round-94/c94_conditional.py` (v2: 53 hand cases = 44 v1 + 9 new, one per class M11, M18, M19, M24, M28, M29, M32, M37, M40); population digests unchanged. Before (v1, `killed=31/40`); target v2 `killed=40/40`. **Unmet**: v2 kills 39/40; the survivor M11 is semantically equivalent to the base candidate.

Work items with evidence pointers:

- Load and freeze: the round's controls (`controls/base-c1.txt`, `controls/ctl-c1-selftest.txt`, `controls/base-c2-v1.txt`, `controls/base-c2-v2.txt`, `controls/ctl-c2-selftest.txt`, `controls/instrument-sha256.txt`) committed in `ba667b24` before the wave.
- Strict C1 counter built and self-tested: `c94_selfassess.py --selftest` → `selftest 9/9 planted findings, exit 1 on planted, exit 0 on repaired`. Battery of eight false-green routes built inside the counter: refused 8/8, the frozen round-93 counter admits 7/7 fixture routes (`controls/base-c1.txt` line 1).
- Wave `w1`: 11 seats, dispatch `.ufo/waves/round-94/w1-dispatch.json` (validated by `ufo-swarm-wave.mjs plan` then `run`), handoff `.ufo/waves/round-94/w1.ready` (dispatched), settled at WAVE-DONE; results `.ufo/waves/round-94/w1-results.json`; seat reports `.ufo/waves/round-94/w1/<seat>.md` (VERDICT first). Seat list and outcomes under Round shape.
- C1 repair attempt (ExecC1Repair): replaced the 13 directory references in SKILL.md by removing their backticks. The counter's path rule no longer sees them, so the counter reads 0 without naming any file. Rejected by the critic (`w1/CriticClaims.md` X4/X5); SKILL.md reverted to the freeze bytes (`git show ba667b24:SKILL.md`). The diff is kept as evidence (`w1/ExecC1Repair/skill.diff`). This is the central honesty point of the round.
- C1 counter attacked: ReviewC1 reproduced false-greens R02b (indented Mistakes table), R03 (two `source:` lines), R05 (SKILL path with `#L42`), R10b (absence span with an unclosed bracket) and R12 (locator `/tmp/scratch/…`), and weaknesses R01 (Gate of two junk lines), R08 (identity displacement through `--surfaces-file`), R09 (symlink named in SKILL.md), R18 (`--surfaces-file` escape); receipts `w1/ReviewC1/`. SentinelScope F1: a `subprocess.py` in the counter's own directory writes a marker and exits 7 at import, before either counter's guard (`w1/SentinelScope.md`). My own battery's F1 used a benign shadow; this is recorded as my mistake, not as F1 closed.
- C2 counter v2 population measured: `w1/ExecC2Mutants/summary.txt` → `v1 killed=31/40`, `v2 killed=39/40`, `v2 not killed: M11`. M11 is equivalent: exhaustive product of 115 200 inputs, zero differences (`w1/ExecC2Mutants.md` §Equivalence); critic grid check 28 512 inputs, zero differences (`w1/CriticClaims.md` §2.1).
- C2 nine cases checked against RFC 9110: `w1/ReviewC2.md` → 9/9 agree; the candidate agrees on 52 of 54 independent cases, and refuses two legal-per-RFC empty-member lists (R93-9, contract v2).
- Knowledge entry on the new ground (`corpus/knowledge/http-list-and-method-grammar.md`, cites S477 and S478): five quoted fragments re-verified by the lane against the retained body (`w1/ScoutRFC/rfc9110.txt`, sha256 `21c1cdce6ab0…`, 502 941 bytes, HTTP 200, 2026-11-05 — `w1/ScoutRFC/fetch.txt`). The scribe's report: `w1/ScribeEntry.md` (306 words).
- Sources: S477 (RFC 9110 §9.1) and S478 (RFC 9110 §5.6.1.2 and §5.6.3) appended after the mirror gate (`w1/ExecSourceRows/mirror-validate.txt`); two anchor defects found by ScoutRFC (D1 hyphenation break in S477; D2/D3 in S478) corrected before landing (`corpus/SOURCES.md` lines 223–224).
- Lesson: `corpus/lessons/round-94.md` — `## Gate`, `## Mistakes` (11 rows), `## Wave review and Routed` (R94-1…R94-8).
- SCORECARD and LOG: `SCORECARD.md` round-94 verdicts, move log and planned section; `LOG.md` round-94 entry (lines 3250–3257).
- L0 question appended: `.ufo/l0-questions.md` (`kake | round-94 | …`).

## Landed changes

| Commit | Change | LOG / evidence |
|---|---|---|
| `ba667b24` | freeze: `freeze.md`, `c94_selfassess.py`, `c94_conditional.py`, `frozen/c1-surfaces.json`, `controls/` | LOG round 94 (freeze); `controls/instrument-sha256.txt` |
| `99a88dea` | lane close: `corpus/lessons/round-94.md`, `corpus/knowledge/http-list-and-method-grammar.md`, `corpus/SOURCES.md` (rows S477, S478), `SCORECARD.md` round-94 section, `LOG.md` round-94 entry, `.ufo/waves/round-94/` (wave evidence: spec, dispatch, results, seat reports and receipts) | LOG round 94 lines 3250–3257; SCORECARD round 94 |

Not landed (rejected): the SKILL.md directory-to-prose repair (reverted; `w1/ExecC1Repair/skill.diff`). SKILL.md at `99a88dea` is byte-identical to the freeze.

## Before → after measurements

**C1 — calibration (HOLD 2).** Counter: `python3 -B .ufo/waves/round-94/c94_selfassess.py --root . --revision <REV>`.

- Base `0f7d9bbc` (do-nothing control, `controls/base-c1.txt`): `lessons=88 entries=81 rows=255 criteria=39 mismatches=15 E1=0 E2=0 E3=0 E4=0 E5=15 pins=ok battery=8/8 predecessor_admits=7/7 floor=2 self_pin=ok met=false`, exit 1.
- Landed `99a88dea` (final, run by the lane just now): `lessons=89 entries=82 rows=255 criteria=39 mismatches=15 E1=0 E2=0 E3=0 E4=0 E5=15 pins=ok battery=8/8 predecessor_admits=7/7 floor=2 self_pin=ok met=false`, exit 1. The two new files (the round-94 lesson, the knowledge entry) add no mismatch.
- Score: stays 2 (HOLD). No calibration move is claimed. The strict counter reads 15 mismatches that round 93 recorded as 0; this is the round's main calibration finding (round 93's `met=true` overstated the lane's self-assessment, because round 93's counter accepted directory paths).

**C2 — freshness (HOLD 10), instrument.** Mutant driver over `.ufo/waves/round-93/w1/recovered-partial/MutConditional/mutants-posgood.json` (40 patches) scored by the v1 and v2 counters (`w1/ExecC2Mutants/mutants-v1.json`, `mutants-v2.json`).

- Before (v1, `c93_conditional.py`): `v1 killed=31/40` (survivors M11 M18 M19 M24 M28 M29 M32 M37 M40).
- After (v2, `c94_conditional.py`): `v2 killed=39/40`; survivor M11 (equivalent; exhaustive 115 200 cases, `ExecC2Mutants.md` §Equivalence).
- Landed `99a88dea` (final, run by the lane just now): `python3 -B .ufo/waves/round-94/c94_conditional.py --root . --revision 99a88dea… --work <scratch>` → `hand=53/53 generated=120/120 forgeries_refused=6/6 positive=admitted anti_table=ok population=ok seed=93 met=true`, exit 0 (the base candidate meets both counters; the claim is about instrument sensitivity). Note: the v2 stdout label still reads `C2v93` (a label not updated in the frozen file; recorded as a defect, not edited).
- Score: stays 10 (HOLD).

## Sources & frontier

- **`corpus/SOURCES.md` rows before → after.** `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 213 at `ba667b24`, 215 at `99a88dea`. Malformed rows (`awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13'`): 0.
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`: exit 0 at round start (213 rows) and exit 0 at the landed tip (215 rows; `/fast/scratch/hyaku/kake-r94/L1/census-final.txt`, last line `kake ok …/corpus/SOURCES.md`). Warnings (W04 duplicate URLs across scopes) are the existing RFC duplicates, now including the RFC 9110 rows S477/S478.
- **Rows added by tier.** A = 2 (S477, S478; kind `spec`; opened 2026-11-05 UTC). Status `mined`; used-by `corpus/knowledge/http-list-and-method-grammar.md`, `corpus/lessons/round-94.md`.
- **Rows touched old → new.** None. No existing row's `status`, `recheck` or `used-by` changed.
- **Frontier rows advanced.** RFC 9110 §9.1 (method token case-sensitivity) and §5.6.1.2 / §5.6.3 (list members, empty elements, OWS) moved from unheld to bounded held ground for the conditional-request grammar; the knowledge entry says what it does not decide (quoted commas, empty elements, obs-text: contract v2).
- **Sourced claim.** The C2 nine-case population rests on the rows opened this round for M37 (S477) and M40 (S478), and on S473 (§13.1.2, re-opened this round: lines 5928–5932 read the same).
- **Assimilation.** None. `merge/kake/SOURCES.append.md` collides with the registry on eight ids and was not adopted; no package row appended.
- **considerthese.** `considerthese/2026-11-05.md` proposal 3 (held-out vs frozen divergence) is partly implemented as the C2 nine-case population; no proposal was taken whole.
- **Mistake mined.** `corpus/lessons/round-94.md` `## Mistakes` rows 1–11 (captured-by and fix per row). The rows that the instruments did not capture are rows 5, 7, 8, 9, 10 (counter gaming, an equivalent target, a benign shadow, and the attack-found false-greens).

## Trend verdicts

- **expansion: improved (bounded).** Two A-tier registry rows (S477, S478) and one knowledge entry on method-token and list-member ground not held before. Evidence: `corpus/SOURCES.md` lines 223–224; `corpus/knowledge/http-list-and-method-grammar.md`.
- **quality: unchanged.** No admitted entry changed; the knowledge entry's quotes are verified (five exact substrings). The strict counter's 15 base findings are recorded and not repaired, so the lane's SKILL.md is no better or worse than at round open.
- **discernment: unchanged.** The round's own gate calls were overturned by its attack seats: the 40/40 target (equivalent survivor), the C1 "0" route (counter gaming, rejected), and the battery's F1 proof (benign shadow). Each is recorded as a lesson mistake, none as an improvement. No non-author spot-check of this round's gate decisions exists yet; the outside closure's check is owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/shonen-ledger.json` box 1; SKILL.md unchanged this round (byte-identical to the freeze, `git show ba667b24:SKILL.md`), and the 15 E5 findings are open (`controls/base-c1.txt`).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched this round (`corpus/knowledge/shonen-ledger.json` box 2).
- [~] Instructions executable by an agent without oral context — pointer: `python3 -B scripts/conditional_eval.py --selftest` (round-93 receipt, 90/90) and `python3 -B .ufo/waves/round-94/c94_selfassess.py --selftest` (9/9), both runnable by a reviewer.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `.ufo/waves/round-94/w1/ConnectorScope.md` (two terms overlap in principle only; four sibling lanes hold adjacent ground, cited not absorbed).

## Round shape, seats and dead seats

- Round shape: ONE v1 wave `w1`, 11 seats (band 8–16 under `scripts/hyaku/ufo-wave-policy.json`). Planner held by the L1 (the validator refuses `planner`). Roles: scout 1 (ScoutRFC), executor 3 (ExecC1Repair, ExecC2Mutants, ExecSourceRows), scribe 1 (ScribeEntry), reviewer 2 (ReviewC1, ReviewC2), critic 1 (CriticClaims), mutation-tester 1 (MutC1), sentinel 1 (SentinelScope), connector 1 (ConnectorScope). Attack seats 5/11 = 45 % (≥ 25 %). Connectors 1 (≤ 2). No residual call; no wave 2 (the attack items were already in w1). Round total: 11 seats.
- Dead seats: none. WAVE-DONE received (`all 11 seats settled`); `w1-results.json` lists 11 entries, each with a verdict and a report.
- Seat counts drift: none (the freeze and the dispatch both say 11).
- Routing: seats were routed by the host's `task.agentModelOverrides`; the L1 did not pass a model.

## Pre-report checks

- Lane gate: `git -C /home/vgpnk/Projects/shokunin/kake-shokunin ls-remote origin refs/heads/master` = `99a88dea1f4fade18af18de12b4d57d86a0224f5`.
- `grep -c '^## SHONEN' .ufo/reports/round-94/kake.md` must print 1 (checked before commit).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root shows only items that are not kake round-94 content (` M .scratch/run15-state.json`, `?? .ufo/closure-kaidoku-r92.json`, both pre-existing and left untouched). No kake round-94 file was found at the fleet root; nothing was copied or deleted.
- Scratch: `/fast/scratch/hyaku/kake-r94/` (L1 receipts) removed after landing; every receipt cited is in the lane's wave dir `.ufo/waves/round-94/` or the lane tree.
- Host sysctls: no seat changed a host sysctl (SentinelScope read `/proc/sys/user/max_user_namespaces` only; the value is recorded in its report).
- Tool installs: none. No pacman, uv, npm or cargo was run.
- Defects recorded, not repaired (frozen instruments): the v2 counter's stdout label `C2v93`; the battery's F1 benign shadow; the counter's `skip_battery` path makes `met` true without the battery clause (ReviewC1/CriticClaims D5); `--surfaces-file` as an escape hatch (R18).

## Open L0 questions

- `kake | round-94 | Ruling wanted on two honest unmet claims` (appended to `.ufo/l0-questions.md`): C1's strict counter reads 15 base mismatches that round 93 recorded as 0, and the successor is falsified by ReviewC1 and SentinelScope; C2's 40/40 target is unattainable because M11 is equivalent (39/40). The operator rules on the instrument verdicts or routes R94-1…R94-8 to round 95.

## Routed to round 95 (none patched after scoring)

R94-1 (successor C1 counter closing ReviewC1 R01, R02b, R03, R05, R08, R09, R10b, R12, R18); R94-2 (no import from the counter's script directory before its guard; effectful shadow in the battery); R94-3 (a repair that removes a backticked path token must name a replacement path); R94-4 (equivalence check on every survivor before a kill target is frozen); R94-5 (13 SKILL.md directory references, a row-by-row file choice with a non-author reviewer; candidate files found: `.ufo/waves/round-29/real-input/out/summary.json`, `.ufo/waves/round-56/sources/receipts.json`, `.ufo/waves/round-61/capture/manifest.json`, `.ufo/waves/round-85/w1/ExecRegistry/registry-rows.md`); R94-6 (contract v2: empty list members, R93-9); R94-7 (a stronger battery for the counter: 4 of 12 counter mutants killed by its own battery); R94-8 (round-93 receipts cite the absent base `191dd0ed`).
