# kaidoku round 85 — the counter's predicate names its counter (missed under the frozen rule); the declared-case kills reach 21 of 21

Lane `kaidoku-shokunin`, attempt 1 (`.ufo/watchdog.log`: `launch kaidoku round=85 … attempt=1`; no earlier `lane-dead-no-report` line; no inherited uncommitted lane work). Lane HEAD at filing: `b9d45602a13bec61832456ec791afa939535530a` (`ls-remote origin refs/heads/main` prints the same hash).

## Work performed

**Declared claims (2 of at most 3), both frozen before any data (declaration `91eeb72f6a7b13dc96e826117956f90ed89ae3f3`, `plans/round-85-claims.md`):**
- **R85-C1 — calibration.** A claim container refuses a counter whose path is named only outside an affirmative, non-negated, pinned predicate (closes the r84 naming-lint limit). Counter: `tools/round-85/predicate-bind.py`. Target: refuse 2 of 2 forgeries, accept the round-84 positive control, `control instruments-only` fires.
- **R85-C2 — depth.** The 21-row frozen probe table (`.ufo/waves/round-85/mutants.json`, the r84 `MutationTester` probe minus 3 verdict-neutral rows) is killed by declared cases. Counter: unchanged frozen `tools/round-84/mutation-closure.py`. Target: killed ≥ 16 of 21, pristine green for the three targets, frozen r84 table still 13 of 13.
- Coverage is not claimed. Owned axes (coverage, depth, calibration) are at 10.0 on their finite proxies; round 84 entered three capability rows, so the stagnation window restarted and no waiver is invoked. Both claims sit on owned axes (calibration and depth are tied at the saturation line).
- Frontier step (§2b, not a claim): one new source row S304 opened this round, one knowledge entry citing it (the round's sourced claim), one mined mistake pair (M85-1, M85-2) in `corpus/lessons/round-85.md`.

**Work items and evidence:**
1. BASE do-nothing controls, committed before the wave (`c7e2e8e1`): C1 with the unchanged r84 gate refuses 0 of 2 forgeries (`.ufo/waves/round-85/pre/c1/base-freeze-precheck.json`: F1 and F2 CLEAN, `met false`); C2 with the frozen counter kills 3 of 21 (`.ufo/waves/round-85/pre/c2/base-mutation-closure.json`; survivors 18), and the frozen r84 table 13 of 13 (`pre/c2/base-frozen13-regression.json`). The do-nothing controls cannot reach either target.
2. One v1 wave `r85-w1`, 12 seats, dispatched by the orchestrator from `.ufo/waves/round-85/r85-w1-dispatch.json` (validated by `ufo-swarm-wave.mjs plan` and `run`, exit 0). All 12 seats wrote `DONE` and reports under `.ufo/waves/round-85/w1/`. Seat evidence: executors `ExecPredBind` (counter, `after-predicate-bind.json`), `ExecPrintedCmd` (7 rows, `after-printed-cmd.json`), `ExecPrintedRun` (8 rows, `after-printed-run.json`), `ExecSourceBind` (3 rows, `after-source-bind.json`); scribes `ScribeSource` (S304 gate, `report.md`), `ScribeLesson` (lesson draft, sweeps); scout `ScoutSurface` (`map.md`); reviewers `ReviewerC1` (`attack.md`: 16 attacks, 6 falsified), `ReviewerC2` (`attack.md`: 19 rows SOUND, 2 WEAK, 0 FABRICATED; scorer attacks a, b, c, d); critic `CriticClaims` (`attack.md`: V2.3 and V2.5 falsified as limits; V2.4 falsified before the table pin existed); mutation-tester `MutationRemeasure` (independent harness: BASE 3 of 21, the same survivor set as the frozen counter; per-arm results); connector `ConnectorScope` (no sibling duplicates of either counter; `report.md`).
3. Integration by the L1 (sole writer into the lane). The two `printed-command.py` candidates edit the same selftest tail: `git merge-file` gave one conflict block (`/fast/scratch/hyaku/kaidoku-r85/L1/merge/`), resolved by keeping both sides (36 cases, pristine rc 0, failures 0). `source-bind.py` and `conjunction-gate.py` candidates copied unchanged. `tools/round-85/predicate-bind.py` (the C1 candidate) copied in. All four tools self-test green at the integration commit (`printed-command` 36/0, `source-bind` passed, `conjunction-gate` 22/0, `predicate-bind` 21/0).
4. C1 frozen-rule measurement exposed a defect in this round's own plan-to-brief handoff (M85-2): the plan's negation-token list includes `none`, the executor brief said to exclude it, and the counter followed the brief. Both the frozen-rule run (`c1/literal-none-predicate-bind.json`: `met false`, the round-84 positive control FLAGGED with `PB_PREDICATE_NEGATED:R84-C1` and `R84-C2`) and the variant run (`c1/variant-predicate-bind.json`: `met true`) are recorded. The variant is **not admitted**: a rule changed after seats scored is not the claim's rule. C1 is recorded as missed.
5. Container `.ufo/waves/round-85/claims.json` pins the 21-row table (sha256 `ef031dbe…`), the three target tools (`target_instruments`) and the three `instrument_supersessions` entries for the additive selftest changes. With it, the frozen counter's `table_identity.matches` is `true` (before it, `matches` was `null`, the gap ReviewerC2 attack d found).
6. Routed r84 items (`corpus/lessons/round-84-verifier-spotcheck.md` §9): R1 — the S302 source snapshot committed at `.ufo/waves/round-85/l1/sources/FirmwarePublication.rea-agents-6.5.0.js`, sha256 `bb4f3246bee70a5b32b048e5ef956e649626b6449b1d457454440739a8d51029` (byte-equal to the npx file, `cmp` OK). R2 — corrected by appended lesson correction C-R2 (8 rows contain the URL at `91eeb72f`: S079, S080, S083, S090, S092, S119, S123 and S303; 7 prior rows, not five). R3 — corrected pointer `.ufo/waves/round-84/w1/SentinelScope/esc-receipt.json` (sweep red-before, green-after: `l1/sweep` and `w1/ScribeLesson/sweep-*.txt`). R4 — the disposition is that no committed removal of `met = all(arms)` exists (`git log -S … 91eeb72f -- tools`: no output); recorded as correction C-R4. R5 — the L1 held the planner seat (validator excludes `planner`); recorded here, not hidden. R6 — partly closed by C2 (declared-case binding for 21 rows); semantic certification is not claimed and is carried. R7 — C1 landed as missed; C3 fixture pins and A3/A9 are carried, not claimed.
7. Spot-check (outside discernment check) of this round's own gate decisions: **not yet written**; it is the non-author closure's duty. No agreement is claimed here.

## Landed changes

| commit | what | LOG / SCORECARD / lesson tie |
|---|---|---|
| `91eeb72f6a7b13dc96e826117956f90ed89ae3f3` | declaration: `plans/round-85-claims.md`, frozen 21-row table, C1 forgery fixtures `pre/c1/F1.json`, `F2.json` | LOG round-85 entry (declared claims); lesson `Base`/`declaration` header |
| `c7e2e8e166cf8ae3db292814f80ab5d35beec455` | BASE receipts (do-nothing controls) | LOG round-85 "Measured" |
| `c1c81c7d74be71cdbe0d62ec397a2753d94e7013` | wave `r85-w1` spec, validated dispatch and briefs (pre-dispatch evidence) | LOG "Wave r85-w1 (12 seats)" |
| `5ed965638a5d053d13ba9a1a756b704be2cf994c` | integration: `tools/round-82/printed-command.py` (merged, 36 cases), `tools/round-83/source-bind.py`, `tools/round-82/conjunction-gate.py`, `tools/round-85/predicate-bind.py`; wave evidence `w1/`; `l1/sources/` snapshot | LOG "Attack findings"; lesson Outcome; this is the **measured revision** for both claims |
| `01f2d5193421d9769097ddcd9483046632f3b70e` | lesson `corpus/lessons/round-85.md` (Gate, Mistakes M85-1/M85-2, corrections C-R2..C-R4, Outcome); S304 row in `corpus/SOURCES.md`; knowledge `corpus/knowledge/2026-11-04-r85-mutant-kill-binding.md`; coverage-map and knowledge-index rows in `corpus/README.md`; QUALITY rows 148 and 149 in `corpus/QUALITY.md`; `.ufo/waves/round-85/claims.json` container; measured receipts `c1/`, `c2/`; sweep `l1/sweep/` | LOG round-85 entry; SCORECARD round-85 section |
| `b9d45602a13bec61832456ec791afa939535530a` | SCORECARD coverage self-assessment re-derived at the round-85 record (168/168) | SCORECARD owned-axes coverage row |

LOG.md: one new entry `## 2026-11-04 — round 85` (before the replay section). SCORECARD.md: owned-axes coverage row updated; new `## 2026-11-04 — round 85` section with the per-claim table and the next-round plan. QUALITY.md: rows 148 (frozen token lists are checked by command) and 149 (counts and pointers re-derived at the revision they name), both citing M85-2 and M85-1 with evidence paths. No capability row entered (C2 extends an instrument; it is not a new repertoire item). `tools/round-84/` is unchanged. `MANIFEST.json`, `SHONEN.md` and `PROVINCE.md` are unchanged.

## Before → after measurements

| claim | before (commit, command, receipt) | after (commit, command, receipt) | verdict |
|---|---|---|---|
| **R85-C1** calibration | commit `91eeb72f`; `python3 -I -B tools/round-84/freeze-precheck.py --root . --rev 91eeb72f… --container .ufo/waves/round-85/pre/c1/F1.json --container …/F2.json --container .ufo/waves/round-84/claims.json --expect …=FLAGGED/FLAGGED/CLEAN --control instruments-only --json-out pre/c1/base-freeze-precheck.json` → F1 CLEAN, F2 CLEAN, `refused_expected 0`, `met false` | commit `5ed96563…`; frozen rule (token list incl. `none`): `python3 -I -B <scratch copy with \none\ added to NEGATION_RE> tools/round-85/predicate-bind.py …` → `c1/literal-none-predicate-bind.json`: F1 FLAGGED `PB_NO_PREDICATE_PATH:R85-F1`, F2 FLAGGED `PB_PREDICATE_NEGATED:R85-F2`, round-84 container **FLAGGED** (`PB_PREDICATE_NEGATED:R84-C1`, `R84-C2`), `met false`. Variant as landed (no `none`): `c1/variant-predicate-bind.json`, `met true`, refused 2, accepted 1, control fires | **missed** under the frozen rule; the variant is not admitted (M85-2) |
| **R85-C2** depth | commit `91eeb72f`; `python3 -I -B tools/round-84/mutation-closure.py --root . --rev 91eeb72f… --mutants .ufo/waves/round-85/mutants.json --work <scratch> --json-out pre/c2/base-mutation-closure.json` → killed **3** of 21 (`sb-window-13th`, `sb-two-fields-first`, `cg-floor-le`), survivors 18, `ok false`; frozen r84 table killed 13 of 13 (`pre/c2/base-frozen13-regression.json`) | commit `5ed96563…`; same counter with `--claims .ufo/waves/round-85/claims.json` (table identity matched): `c2/after-21row.json` → killed **21** of 21, survivors none, inconclusive none, pristine_failed none, `ok true`, `table_identity.matches true`; frozen r84 regression `c2/after-frozen13-regression.json` → 13 of 13, `ok true`. Pristine green: `printed-command` 36 cases rc 0, `source-bind` passed, `conjunction-gate` 22 cases rc 0 | **met** by the frozen counter (target ≥ 16) |
| coverage (not claimed) | stem recipe 167/167 at `5ed96563`, `tools/round-66/coverage-selfcheck.py --selfcheck` | stem recipe 168/168, `missing []`, `dangling []` at `01f2d519` (stem score 10.0) | unchanged score 10.0 |

Counting-command details: `--rev` for the after-measurements is `5ed965638a5d053d13ba9a1a756b704be2cf994c`; the BASE is `91eeb72f6a7b13dc96e826117956f90ed89ae3f3`. Both counters read git blobs at `--rev` from the lane root. Limits (declared and measured): the C2 counter binds by case name (the reviewer's case-body check found no fabricated case; none is excluded by the counter); the counter does not enforce "removed or weakened existing case" (critic V2.5: a copy with all pre-existing cases removed still scores 21 of 21; the manual check found no removal). Rows 10 (`|` only) and 12 (`PLAN` only) are weak against same-family siblings.

## Sources & frontier

- `corpus/SOURCES.md` census, before → after, with the frozen commands:
  - `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: exit **0** before (`kaidoku ok …`, 27 W04 duplicate-URL warnings) and exit **0** after (`kaidoku ok …`, 27 W04; no new warning).
  - Frozen manual census (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`): rows **208 → 209**; malformed (NF≠13) 0 → 0; duplicate ids none → none; enum violations none → none.
  - Tier histogram (`awk`): A=190 B=10 C=8 → **A=190 B=11 C=8**. Status: mined=186 rejected=22 → **mined=187 rejected=22**.
- Rows added by tier: **one, tier B** (`S304`, Papadakis et al., "Mutation Testing Advances: An Analysis and Survey", DOI 10.1016/bs.adcom.2018.03.015; full text read 2026-11-04 from the archived ORBilu author postprint; located quote 24 words, PDF p. 6; the ScienceDirect chapter page returned HTTP 403 and was not used; source snapshot `.ufo/waves/round-85/w1/ScribeSource/source-snapshot.txt`, sha256 `3452916192a447db89545cf9cdb4c0c7bfbd7f162b67482fb7582691e6bd7bee`).
- Rows touched old→new: **none** (no existing row's status, recheck or used-by changed; the S303 "five scopes" error is corrected in the round lesson, not in the registry).
- Knowledge entry admitted: `corpus/knowledge/2026-11-04-r85-mutant-kill-binding.md`, `source: S304`, mined. The coverage-map and knowledge-index rows were added to `corpus/README.md`. This is bounded apparatus knowledge, not domain coverage ground.
- Frontier rows advanced: none in `PROVINCE.md`; the mutation-kill binding is recorded as a bounded apparatus knowledge row in the coverage map.
- Mistakes mined (`corpus/lessons/round-85.md ## Mistakes`): **M85-1** (a counted scope stated as five when it is seven prior rows; a pointer cited without its directory prefix; captured-by none; fix = re-derived counts and a red-before/green-after pointer sweep; QUALITY row 149) and **M85-2** (the frozen C1 token list and the wave brief disagreed; captured-by none; fix = plan-to-counter agreement as a declared, pre-data check; the sweep `l1/sweep/tokens-red-before.txt` is MISMATCH today; QUALITY row 148).
- Sourced claim: the knowledge entry cites `S304`, opened this round (the round's sourced claim, §2b item 4).
- Assimilation: **none.** The claim budget (C1 + C2) and the frontier step took the round; `merge/kaidoku/` was not drawn on, and no theme was assimilated. Stated for the report (no penalty).
- `considerthese/`: **no such directory exists** for kaidoku, so no proposal was mined.
- Quarantine slice (absent-defect register): not applicable to kaidoku this round (the wave-4 quarantine applies to tabi, revenger, chousa and kotodama).

## Trend verdicts

- **expansion: unchanged.** One tier-B source (S304) and one knowledge entry, both on apparatus ground (mutation-kill semantics for the lane's own instruments). No new admitted entry on uncovered domain ground, and no new artifact class or frontier promotion. Evidence: the S304 row and the knowledge entry; coverage stem 168/168 with `missing []`.
- **quality: improved.** Three routed round-84 defects were re-derived and corrected by appended corrections, not rewrites (C-R2 count 8 rows / 7 prior, C-R3 pointer resolves, C-R4 no removal commit exists), and two lesson-backed QUALITY criteria were added (rows 148, 149). Evidence: `corpus/lessons/round-85.md ## Corrections`, `l1/sweep/`, `w1/ScribeLesson/sweep-*.txt`, `corpus/QUALITY.md` rows 148–149. The admitted-entry re-check has no failing entry: the r85 entry is new and its `recheck` is 180d.
- **discernment: unchanged.** No non-author spot-check of this round's gate decisions has been written; the S304 admit and the S303 carried rejection await it. The round's calibration claim C1 is missed under its frozen rule, so the calibration trend did not move. The disagreement found (M85-2) is recorded as a lesson and a criterion, but a self-found plan/brief mismatch is not an outside spot-check, so it is not counted as discernment improvement.

## SHONEN

Checklist boxes (`SHONEN.md`): none checked by a non-author verifier this round; each is the lane's own assessment.

- [~] SKILL.md contains real decision tables, error-pattern lists and checklists citing sources — `SKILL.md` (lane, 1988 lines; decision tables and rule blocks cited at `SKILL.md:81-343` per the SCORECARD depth row); not re-checked this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## 2026-11-04 — round 85`: the integrated counters were run end to end on committed bytes (`c1/`, `c2/`); the domain task itself (a shipped-artifact REA analysis) was not part of this round.
- [~] Instructions executable by an agent without oral context — `plans/round-85-claims.md` (predicates, counting commands, kill rules and targets) and the wave briefs `.ufo/waves/round-85/w1-briefs/` (executed by 12 seats without intervention, each reporting `DONE`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-85/w1/ConnectorScope/report.md` (no sibling duplicate; both claim surfaces in Core, `PROVINCE.md:554,560-562,622`); no PROVINCE edit this round.

## Wave shape, seats and dead seats

- One v1 wave `r85-w1`, 12 seats (within the run-15 band 8–16), dispatched once by the orchestrator from `.ufo/waves/round-85/r85-w1-dispatch.json`; no residual call; round total 12.
- Role mix: executor 4, scribe 2, scout 1, reviewer 2, critic 1, mutation-tester 1, connector 1. Attack seats 4 of 12 (33 %: reviewer, critic, mutation-tester). Connector seats 1 (≤ 2). L2 floor (≥ 8, one batched call): met.
- Planner seat: held by the L1 (the validator excludes `planner`); recorded deviation (R5).
- Dead seats: **none**. All 12 seats settled and wrote `DONE` and their reports. `r85-w1-results.json` records `output: null` for every seat with the note "orchestrator kernel restarted mid-wave"; the seat reports in the wave dir are the record.
- Answering models: not recorded; no claim depends on a seat's model.
- Wave-cap or dispatcher issues: the ready file was written at 17:33 and was picked up after roughly 4 minutes (no `WAVE-DONE` until settlement). No resend occurred.

## Misroot sweep, inherited state, open questions

- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file written by a round-85 seat. The untracked and modified fleet-root entries are other lanes' or the orchestrator's (`.scratch/closure-*`, `.scratch/run13-state.json`, `.scratch/run15-state.json`, `after` dated 2026-11-03, `.ufo/reports/round-84/kama.md`). None touched and none moved.
- Inherited state: none (attempt 1). No uncommitted lane-authored leftovers at round start (`jj-lane.sh state`: `ahead=0`, `tracked=0`).
- Lane untracked at filing: `.ufo/waves/round-85/r85-w1.ready` and `r85-w1.ready.dispatched` (orchestrator handoff markers; not committed).
- Open L0 questions: none appended. The C1 rule question (whether `none` is a negation token) is a lane-internal decision for the next declared round, not an operator decision.
- Non-author verification: required and pending. Driver completion is not admission. The round is not admitted (C1 missed).

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. This L1 and all 12 seats used `python3` (stdlib), `git`, `jj`, the lane's own counters, and the wave validator (`ufo-fsd-alpha`). No `pacman` transaction (paused host-wide). Recorded per `/home/vgpnk/.omp/agent/RULES.md`: no tool installed or upgraded in round 85.

## Verdict summary

- R85-C1: **missed** under the frozen rule (honest stop; the candidate that met its target omits a token the frozen plan lists; not admitted).
- R85-C2: **met** by the frozen counter (21 of 21; frozen r84 13 of 13); depth is name-level binding, case bodies reviewed (19 sound, 2 weak, 0 fabricated), not semantically certified.
- Round: not admitted (C1 unverified). No owned axis harmed. Honest stop recorded; no verdict rerolled.
