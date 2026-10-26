# kengaku — round 36 report (hyaku run 7, 2026-10-25) — honest stop: wave 2 not dispatched

Lane `kengaku-shokunin`, baseline `b662a5d6`, landed lane tip `0fb87f88488839a923c28a777b9b69594259043c`
(`git -C kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash; `jj-lane.sh state`:
`ahead=0 behind=0 untracked=0`). Frozen claims `plans/round-36-claims.md` (freeze `3241b86c`,
Amendment 1 `acbda2f3`). The operator ended the run before the planned falsify wave was taken, so the round is
**wave 1 only: 40 seats, below the 64-seat floor of the run-7 directive.**

## Work performed

Declared claims: **C1 calibration** (axis score 8) — a hardened package gate `plans/pkg_gate.py` proven against a frozen
14-fixture junk battery, closing the four round-35 routed defects R35-D1..D4; **C2 coverage** (lowest, tied 7; L0-capped) —
the pinned Terminal-Bench 2.0 `regex-log` grader admitted with an executed 24-case offline probe (rows S108-S110).

- Frozen before any gate write, probe run or seat: claims, both counters, the battery, probe case table with predictions, ledger rows
  (open), six red controls — `3241b86c` (`plans/round-36-claims.md`; `.ufo/waves/round-36/claims/control-*.txt`:
  absent gate `unevaluated=14`; round-35 counter `LEGACY accepted=7/7`; accept-all gate `false_green=11`; reject-all gate
  `false_red=3`; C2 `checks=6 defects=4`).
- Amendment 1 (disclosed): the first real probe run showed two assertion texts carried a `mkdtemp` path, so the frozen
  byte-equal check could never hold (`corpus/evidence/round36/regex-log-probe-first-run.txt:21-22`). One-line repair
  (`plans/regex_log_probe.py:127`) before any seat existed; `--dry` case table byte-identical to the freeze
  (`corpus/evidence/round36/regex-log-dry-cases-freeze.txt`); all 24 predictions already matched. Whether a pre-scoring
  repair of a frozen instrument is a revision or a rule change is the open operator question (`revenger | round-69`, `kumitate | round-63/64`);
  `R36ConnAmendment.md` recommends `revision`. The C2 verdict stands only if the operator accepts it.
- Probe: `python3 plans/regex_log_probe.py --lane .` → `cases=24 observed_pass=8 observed_fail=16 mismatches=0`
  (`corpus/evidence/round36/regex-log-probe.txt`); byte-identical on Python 3.11/3.12/3.13 (`build/R36ProbeRerun.md`); independent
  re-implementation agrees 24/24 (`build/R36IndepRegexGrader.md`); five harness mutants detected (`build/R36ProbeHarnessMut.md`);
  five pinned files re-opened byte-identical (`build/R36ReopenPins.md`).
- Entry `corpus/knowledge/tb2-regex-log-grader.md`: a literal alternation of the nine expected dates passes; leading-zero octets,
  digit-adjacent dates, year width, month-length validity and the permitting side of Feb 29 are unobserved by the fixed 25-line log.
  Post-hoc (not frozen cases, labelled so): the task oracle admits `00`-`09` octets and is not line-scoped (`build/R36OracleRun.md`);
  four more requirement faces are free (`build/R36CritUnenforced.md`).
- Gate: four independent executor candidates each scored `false_green=0 false_red=0 unevaluated=0` (`build/R36Gate{A,B,C,D}.md`);
  `R36GateB` was installed as `plans/pkg_gate.py` (sha256 `ea638822…`).
- R35-D3: the 21 committed nested round-34 attack-mirror paths removed from the tip
  (`.ufo/waves/round-36/integrate/nested-paths-removed.sha256`); wave-1 scratch mirrors of `corpus/` (~22.5 MB) removed uncommitted
  (`integrate/scratch-removed.txt`; recorded as a Mistake).
- R35-D4: `Erratum (round 36):` in `corpus/lessons/round-36.md` `## Gate` (S130's package: denominator 38, rows recount `13 + 23 + 1 = 37`).
- Assimilation: mined `considerthese/2026-10-25.md` proposal 2(c) (tip-receipt validator): `pkg_gate.py --rerun` re-runs one receipt of
  156 (clause (b), block-at-second-recurrence, is still unbuilt; proposals 1 and 3 untouched). `merge/kengaku/` screened by `R36ScoutMergePkg`:
  `grader-predicate-input-types.md` held (admit-candidate for a later claim; §10 forbids widening frozen claims), `grader-fixture-probe-stage3.md`
  refused; nothing appended. Id guard run (`.ufo/waves/round-36/assimilation/`, 24 staged-vs-registry collisions, guard proof ok).
- Wave-1 attackers found limits that are **not repaired** (frozen predicates/battery are not edited): the battery is gameable by a fixture-keyed
  gate (`build/R36CritBattery.md`, 8 cues, scores the clean line) and leaves eight advertised gate clauses without a fixture (`build/R36RevClaims.md` FG1);
  the frozen C2 counter admits a junk package (`build/R36CritC2Counter.md`, `checks=6 defects=0`); the frozen-digest table went stale (FG3,
  corrected by an appended table in the claims file); two probe cases are confounded (`build/R36RevProbePred.md`).

**Round shape:** one v1 wave (build, 40 seats: executor 13, scribe 9, scout 5, critic 4, connector 3, reviewer 3, mutation-tester 3;
m_flash roles 26/40; attack-role share 10/40), 0 dead seats (`.ufo/waves/round-36/build-results.json`); no residual call. Planned wave 2
(34 seats: 9 executor, 7 critic, 1 scribe, 3 reviewer, 8 mutation-tester, 4 scout, 2 connector) is committed
(`falsify-spec.json`, `falsify-dispatch.json`, `falsify.ready`) and was **not dispatched**. Round total 40. Planner seat held by the L1.
The orchestrator's dispatcher was silent 23:15-00:xx -03; I reported it to `Main` and wave 1's WAVE-DONE arrived afterwards.
Stale-lane: respawn-per-round driver, no other mission of this lane open.

## Landed changes

| change | LOG.md | commit |
|---|---|---|
| freeze: claims, counters, battery, probe, spec, ledger (open), controls, captures | `LOG.md` `## Round 36` | `3241b86c` |
| Amendment 1 + first-run receipt | same | `acbda2f3` |
| wave-1 spec/dispatch | same | `f9efce3b` |
| integration: `plans/pkg_gate.py`, entry, S108-S110, README, QUALITY Q24/Q25, SKILL rows+section, PROVINCE, lesson, nested-path removal, wave-1 evidence | same | `805fe790` |
| SCORECARD/LOG sections, ledger rows closed | same | `7d1fa691` |
| lesson numbers measured, extra Mistakes rows, census after | same | `85655006` |
| wave-2 spec/dispatch, connector reports | same | `c16956d3`, `b85af35d` |
| close: wording fixes, digest correction, errata, wave-1 results | `LOG.md` `### Round 36 — close` | `612458f3` |
| final measurement receipt, census after | same | `0fb87f88` |

## Before → after measurements

Measured in a clean sparse clone of the tip (`.ufo/waves/round-36/integrate/measure.sh`; receipt `integrate/measure-final.txt`, master `612458f3`, `untracked_in_clone=0`).

- **C1 (calibration)** — `python3 plans/round36_c1_verify.py --lane .`: before `FIXTURES total=14 … unevaluated=14`, `rows=4 closed=0 observed_pass=0`, exit 1
  (`claims/control-c1-nothing.txt`; round-35 counter `LEGACY accepted=7/7`) → after `FIXTURES total=14 false_green=0 false_red=0 unevaluated=0`,
  `rows=4 closed=4 observed_pass=4 mismatches=0`, `PREDICATE C1 pass`, exit 0 (`R35-D3 committed_nested_wave_paths 21 → 0`). **Frozen predicate met; score 8 → 8 held.**
  Not a pass in substance: the battery is gameable and clause-incomplete (above), and no mutation wave ran.
- **C2 (coverage)** — `python3 plans/round36_c2_verify.py --lane .`: before `checks=6 defects=4`, exit 1 (`claims/control-c2-nothing.txt`) → after `checks=6 defects=0`,
  `PREDICATE C2 pass`, exit 0. **Frozen predicate met; score 7 → 7 held (L0 cap), contingent on the operator ruling on Amendment 1.** The counter admits a junk package,
  so the landing rests on wave-1 re-reads only.
- Admission: no axis harmed (no-harm baseline `build/R36TipSweep.md` 10/10 green before landing; **not re-run after landing** — wave 2's `F36NoHarm` did not run).
  `plans/round35_c1_verify.py` now fails V4 (42 knowledge files pinned; 43 now) — an expected freeze-only counter, recorded in the claims file.

## Sources & frontier

- `SOURCES.md` rows 100 → 103 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); added by tier: A +3 (S108, S109, S110, all `mined`, `used-by` the entry); tier A 85 → 88,
  status mined 84 → 87. Rows touched old→new: none. Frontier rows advanced: README §Frontier task-spec bullet gains a round-36 sub-bullet (second TB2 task only).
- Census before → after (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`): exit 0, 15 W04, `kengaku ok` (`claims/census-before.txt`) → exit 0, 15 W04, `kengaku ok`
  (`integrate/census-after.txt`). Knowledge files / index rows 42/42 → 43/43.
- Sourced claim: C2 cites S108-S110, opened 2026-10-25 (URL, date, ≤25-word quotes in the lesson `## Gate`). Mistake mined: `corpus/lessons/round-36.md` `## Mistakes` (8 rows, incl. the counters-accept-junk class
  with red-before `control-c1-legacy.txt`). Assimilation: considerthese proposal 2(c) (above); `merge/kengaku/`: 1 held, 1 refused, none appended.
- No tools installed (biopython 1.85 used through `uv run --with`, ephemeral).

## Trend verdicts

- **expansion — improved (modest).** One admitted entry on a second TB2 task (uncovered instance, same capability), rows S108-S110 `mined`; R36CritScope rates it an instance increment, not breadth.
- **quality — unprovable-but-better.** Gate measured against the junk battery (7/7 legacy false-greens → 0) and Amendment 1 / errata appended, but no non-author reviewer is on record and the gate's own limits (gameable battery, junk-admitting C2 counter) are open.
- **discernment — unchanged.** No outside spot-check this round; wave 1 found the counters' weaknesses after the freeze and Q24 records them as limits, but the lane did not learn them into a stronger criterion.

## Open L0 questions

None appended this round. Standing and relevant: `revenger | round-69` / `kumitate | round-63,64` (is a pre-scoring mechanical repair of a frozen instrument a ratchet within the rule or a new revision — Amendment 1 depends on it), and `kengaku | round-33` (coverage cap).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md (round-36 registry rows + `## TB2 regex-log grader — round36`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:7; LOG.md `## Round 36`
- [~] Instructions executable by an agent without oral context — corpus/lessons/round-8-aggregator-box3-coldrun.md:48
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md `## Round36 partial frontier admission`
