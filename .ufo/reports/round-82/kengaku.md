# kengaku round 82 — report

Lane `kengaku-shokunin`, round 82, hyaku run 15, attempt 1, 2026-11-04. L1 `KengakuR82`.
Base `a3a03ac31451e58f1742b9bccb73b72c2d90a95c` (round-81 verifier spot-check); freeze
`12f1029a45cf0097a3afd030d757bf93b87f8018`; instruments and repairs `c804dd41`; receipts and records
`82fe89d5`; final lane tip **`a44b2f083ee8b4115aea64598646f4bd9e3c1470`** (`ls-remote` matches).

**Round shape.** ONE v1 wave, **12 seats** under `ufo-wave-policy.json` (band 8–16, `maxLanes` 12):
executor 5, scribe 2, scout 1, connector 1, reviewer 1, critic 1, mutation-tester 1. Attack share
**3/12 = 25.0 %** over the campaign list (reviewer, critic, mutation-tester). The L1 holds the
canonical planner seat under the orchestrator ruling of 2026-10-19 (the validator rejects `planner`);
the bounded data-walk rode `PlansReconR82`. No residual task call; round total **12 seats**.
Spec, dispatch and the settled results: `.ufo/waves/round-82/w1-spec.json`,
`w1/w1-dispatch.json`, `w1/w1-results.json` (12 rows, role per row), `w1.ready`,
`w1.ready.dispatched`.

**Dead seats (named, not replaced).** Two seats never recovered from a provider 429
(`zai/glm-5.3-flashx`, `Retry budget exhausted after 5 retries`, errorStatus 429 type=1302):
`SweepGateR82` (09:54Z after one revive) and `RegistryCounterR82` (died ~07:24Z). Four more were
revived mid-wave and completed after the backoff: `SweepHarvestR82`, `ReviewerR82`, `CriticR82`,
`MutationR82`. The two dead seats' work — the sweep gate and the C1 counter — is carried by the L1
and marked as such in this report and in `LOG.md`.

## Work performed

The round declared **three claims** (`plans/round-82-claims.md`, frozen at `12f1029a`):
**R82-C1** coverage — registry completeness in the direction no counter had priced;
**R82-C2** calibration — the round-81 verifier spot-check's `V1`…`V7` discharged;
**R82-C3** capability acquisition (freshness instrument) — `sweep-at-one-tip`.

- **R82-C1 — the audit and its four rows.** `plans/round82_c1_plans_registry.py` derives the universe
  from `BASE_REV` bytes (`SCORECARD.md`, `LOG.md`, `corpus/README.md` × `git ls-tree` at base, minus
  `plans/fixtures/`), prices the eight-cell shape of every row added at the tip, and keeps a reverse
  leg (`ENTRY-MISSING`). `plans/round82-exclusions.json` carries the two support modules, each proved
  CLI-less from its own bytes (no `argparse`, no `__main__`). Four rows landed —
  `log-appendonly`, `round37-c1-attribution`, `round66-registry-check`, `round80-c1-remint` — drafted
  by `RegistryRowsR82` and independently re-run by `ReviewerR82` (all four entry argv reproduced; two
  are red at the tip by design and say so). Commit `c804dd41`.
- **R82-C1 — a defect the round caught on itself.** The first `round82-c3-sweep` row spelled its flag
  list with `|` separators; the row was visibly present at `SKILL.md:736` while
  `plans/round52_c2_registry.py` still printed `MISSING plans/round82_c3_sweep.py`, because every
  pipe splits an eight-cell row. Fixed (comma-separated flags) and recorded as mistake M82-2; the
  registry now re-reads `MISSING 0` (`SKILL.md`).
- **R82-C2 — seven repairs.** `corpus/evidence/round81/c2-after.txt` re-minted at a clean clone
  (`WORKTREE clean`, `C2RepairR82` §V1); `plans/round81_c2_spotcheck_debt.py` gains two attributed
  mutants so its `Six` docstring becomes true (`MUTANTS real=6 killed=6 survived=0`, §V4);
  `corpus/evidence/round81/determinism.txt` keeps its 313 original bytes and gains the two producing
  `COMMAND` lines plus `REV f6d5b864…` — the revision the legacy hash pair actually reproduces at
  (§V7, found by running both probes at each of 12 candidate revisions, not by substitution); the
  empty untracked `--lane/` directory is removed (§V5); the round-81 lesson's two counts are
  corrected in place; the S260/S261 anchors are corrected as **supersede rows** S265/S266 because
  `corpus/QUALITY.md` Q34 forbids editing an anchor cell in place, “even when the round wrote the row
  itself”. Commit `c804dd41`; `corpus/lessons/round-82.md` §Corrections, `corpus/SOURCES.md`.
- **R82-C2 — the counters.** `plans/round82_c2_closure_debt.py` derives the universe from the
  *newest* `round-<n>-verifier-spotcheck.md` by round number (no hardcoded id list) and runs each
  row's `check`; `plans/round82_c2_checks.py` holds `u1`…`u7`, each of which fails on the base tree
  (`--sensitivity` → `SENSITIVITY n=7 failed_at_base=7`). Seven rows `R81-V1`…`R81-V7` in
  `corpus/routed-findings.jsonl`. A second, independent implementation by `C2CounterR82`
  (`.ufo/waves/round-82/w1/C2CounterR82.py`) reaches the same 7/7 — two implementations agreeing is
  the review signal, not a substitute for the counter.
- **R82-C3 — the instrument.** `plans/round82_c3_sweep.py`: frozen 26-member map; per-member argv
  expanded from the map; sequential execution (four instruments contend for port 8080); process-group
  kill on timeout (a direct-child kill left bwrap grandchildren holding the pipes — the round's first
  run found it); observation source = stdout, falling back to the instrument's own `--receipt`
  (nginx and torch-pipeline print nothing on stdout — the harvest seat found the same two
  independently); classification under the round-80 A2 projection; staged write; `COMMAND-MISMATCH`
  against the reconstructed argv; `--verify-at-tip`; `--selftest`, `--mutants`, three controls.
- **R82-C3 — the census.** `corpus/evidence/round82/sweep.txt`, measured from a clean
  `git clone --shared` at `c804dd41` (`WORKTREE clean`, `LANE_TIP c804dd41`):
  `HISTOGRAM status reproduced=18 diverged=7 unrunnable=1 total=26`; class histogram (multi-label)
  `HISTOGRAM-CLASS file-artifact=18 stdout-inspection=8 subprocess-exec=10 … sum=59`.
  Diverged: `kv-store-grpc` (50 lines — pids/ports in graded lines), `sqlite-with-gcov` (30 —
  its run receipt matches the committed one exactly while its stdout differs; the harvest seat
  measured both sides), `hf-model-inference` (25), `torch-tensor-parallelism` (10), `pypi-server` (6),
  `nginx-request-logging`, `torch-pipeline-parallelism`. Unrunnable: `protein-assembly`
  (`ModuleNotFoundError: No module named 'Bio'` — the frozen map's argv has no `uv … --with
  biopython`; honest stop, not patched after the freeze).
- **Determinism.** Two runs of the gate at `c804dd41`, same code, same tip:
  `DETERMINISM members=26 statuses_identical=yes divergence_counts_identical=yes
  exit_codes_identical=yes disagreements=0` (`corpus/evidence/round82/determinism.txt`, with both
  `COMMAND` lines and the `REV`). The independent harvest seat's own two-pass sweep agrees on every
  member (18/5/3 in both passes).
- **Mutation seat.** `MutationR82` (32m31s, revived after 429) found 16 survivors across the three
  counters; the actionable ones are now legs (`DUPLICATE`, `EXCLUDED-BUT-REGISTERED`,
  `PHANTOM-EXCLUSION`, `EVIDENCE-LITERAL-EMPTY`, `DUPLICATE-ROW`, `PROJECTION-EMPTY`, `MAP-EXTRA`),
  the two contract gaps are named for a successor round (`corpus/lessons/round-82.md`
  §Mutation results).
- **Mistakes mined this round.** M82-1: a probe is not read-only because it takes `--receipt` —
  `round68_c1_pypi_finish.py` wrote `corpus/evidence/round68/pypi/{server-log.txt,stderr/K1.txt,
  stderr/K3.txt}` inside the lane at 06:33 and dirtied the worktree until restored; caught by
  `PlansReconR82` §0.1, and the fix is that the sweep runs against a disposable clone and stamps
  `WORKTREE`. M82-2: the pipe-splitting row. M82-3 (mined from round 81): a receipt minted over a
  moving worktree is not a measurement of a tree. M82-4: three seat messages landed as a literal
  `agent:/` directory at the fleet root; relocated byte-exact to
  `.ufo/waves/round-82/misroot/agent/` and the fleet copies deleted.
- **Frontier.** S262/S263 admitted (pinned TB2 per-task grading entries), S264 rejected (HTTP 404 at
  the pin), S265/S266 supersede rows. Two knowledge entries: `tb2-replay-sweep-at-one-tip.md` (new)
  and the provenance trio added to `tb2-file-artifact-replay-classes.md`. Census rc 0 before and
  after.
- **Connector and critic.** `ConnectorR82` ruled no sibling owns a registry-completeness gate, a
  spot-check-derived debt counter or a population sweep; no SOURCES id or URL collision; and it
  surfaced the V2-versus-Q34 contradiction the round honours. `CriticR82` attacks the three frozen
  predicates; its findings are carried into the lesson and `Planned (round 83)`, not smoothed.

Assimilation: **none** this round (no `shokuknow` package adopted; the round's claims are
lane-internal and the campaign's quarantine-first rule does not apply to this lane).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: `plans/round-82-claims.md`, `plans/round82-sweep-map.json`, `corpus/evidence/round82/freeze-controls.txt` | §Round 82 bullet 1 | `12f1029a` |
| Instruments (`round82_c1_plans_registry.py`, `round82-exclusions.json`, `round82_c3_sweep.py`, `round82_c2_closure_debt.py`, `round82_c2_checks.py`), the seven round-81 repairs, four C1 rows + two r81-probe rows, S262–S266, the corrected lesson counts, the two knowledge entries, the lesson | §Round 82 bullets 2–3 | `c804dd41` |
| Receipts and records: the three counters' before/after/battery/control receipts, the sweep census, the determinism receipt, `SCORECARD.md` §Round 82, `LOG.md` §Round 82, `PROVINCE.md` §Round 82, the README index rows, the three round-82 counter registry rows, the wave evidence | §Round 82 bullets 4–6 | `82fe89d5` |
| The three claim verdicts measured at the landed tip | §Round 82 bullet 4 | `a44b2f08` |
| This report (fleet repo) | — | `fleet-commit.sh --as kengaku` |

## Before → after measurements

| claim | before | after | command | measured against |
|---|---|---|---|---|
| **R82-C1** | `DEFECTS n=6`; `TARGET missing=4 unclassified=2 excluded=0 rows=133 entry_missing=0`; exit 1 (`c1-before.txt`, base clone at `a3a03ac3` with the counter copied in) | `DEFECTS n=0`; `TARGET missing=0 unclassified=0 excluded=2 rows=143 entry_missing=0`; `PREDICATE R82-C1 pass`; exit 0 (`c1-final.txt`) | `python3 plans/round82_c1_plans_registry.py --lane .` | base `a3a03ac3`; tip `a44b2f08` |
| **R82-C2** | `DEBT-UNREGISTERED` ×7 + `INDEX-MISSING`, `DEFECTS n=8`, exit 1 (`c2-before.txt`, `--rev a3a03ac3`) | `TARGET ids=7 closed=7 checks_passed=7 indexed=yes`, `DEFECTS n=0`, `PREDICATE R82-C2 pass`; `SENSITIVITY n=7 failed_at_base=7` | `python3 plans/round82_c2_closure_debt.py --lane .`; `… --sensitivity --work DIR` | tip `a44b2f08`; sensitivity at `a3a03ac3` |
| **R82-C3** | no gate, no map, no receipt (three absences in `freeze-controls.txt`) | `TARGET members=26 located=26 status_lines=26 histogram_total=26 mismatches=0`, `PREDICATE R82-C3 pass`; `HISTOGRAM status reproduced=18 diverged=7 unrunnable=1 total=26`; `DETERMINISM … disagreements=0` | `python3 plans/round82_c3_sweep.py --lane . --check` | receipt measured from a clean clone at `c804dd41`; check at `a44b2f08` |

Batteries (receipts `corpus/evidence/round82/c{1,2,3}-*`): C1 `SELFTEST cases=8 red=7 failures=0`,
`MUTANTS real=7 killed=7 survived=0`; C2 `SELFTEST cases=7 red=6 failures=0`, `MUTANTS real=6
killed=6 survived=0`; C3 `SELFTEST cases=12 red=11 failures=0`, `MUTANTS real=11 killed=11
survived=0`. Seven controls, all `target_reached=False`: C1 `empty-rows`, `exclude-cli`, `name-only`;
C2 `presence`; C3 `ledger-copy` (`NO-RUN`), `exit-only` (`PROJECTION-UNCHECKED`), `fabricated-line`
(`VERIFY-MISMATCH`).

**Declared deviation, not laundered.** R82-C2's V2 sentence named S260/S261 as the locus of the count
fix; Q34 and the fleet contract forbid editing an anchor cell in place, so the fix lands as supersede
rows S265/S266 and the frozen rows keep their bytes. Both halves are checked (`u2`): the supersede
rows recompute and the frozen rows are unchanged. The claim's substance — the annotation no longer
misstates the quote — holds in the live registry.

**A second, honest gap.** `--verify-at-tip` is implemented and battery-covered, and its logic was
exercised by hand, but no receipt of record was minted for it this round; it is listed first in
`Planned (round 83)`.

## Sources & frontier

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

- **before:** exit **0**, final line `kengaku ok …/corpus/SOURCES.md`, 26 `W04` warnings
  (`corpus/evidence/round82/census-before.txt`).
- **after:** exit **0**, final line `kengaku ok …/corpus/SOURCES.md`, 26 `W04` warnings.
- Rows **253 → 258** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Added by tier: **5 tier A** (S262, S263, S264-rejected, S265, S266); 0 tier B/C.
- Rows touched old→new: none changed in place (Q34). `S260 → superseded by S265`
  (`:1-17`/`stamp 2-16`/`9 words` → `:1-15`/`stamp 2-14`/`OBSERVATIONS_BEGIN 15`/`7 words`),
  `S261 → superseded by S266` (`14/17 words` → `12/13 words`). Every change is logged in the lesson.
- Frontier rows advanced: S262/S263 move “how a TB2 verdict is produced” from the lane's own
  receipts (S260) to the pinned harness entry itself — the premise the sweep compares against.
- `corpus/lessons/round-82.md` `## Gate` carries URL, access date (2026-11-04T09:37:08Z) and a
  ≤25-word located quote per new row (S262: 12 + 6 words; S263: 1 + 2 words) and the reject's reason
  and flip condition (S264).
- Assimilation: **none** (see Work performed).

## Trend verdicts

- **expansion: improved.** The instrument index gained the direction it never had (four
  claim-referenced instruments and two support modules classified; `missing=0 unclassified=0
  excluded=2`), the executed population gained a full census (26 members: 18 reproduce, 7 diverge, 1
  unrunnable), five tier-A rows entered the registry, and two knowledge entries landed. Evidence: the
  three `TARGET` lines, `corpus/evidence/round82/sweep.txt`, `corpus/SOURCES.md`.
- **quality: improved.** Three gates landed with selftest + mutant + control batteries, a sensitivity
  leg that fails on the base tree, a census that cannot be minted without a `WORKDIR`, and a
  process-group kill a hung member cannot escape. The round also caught two of its own defects
  mid-flight (the pipe-splitting row, the pypi sidecar writes), one pre-existing rule conflict (V2
  versus Q34) and seven mutation survivors it then closed. Evidence: the battery tallies,
  `corpus/lessons/round-82.md` M82-1…M82-4 and §Mutation results.
- **discernment: improved.** The round refused to call the sweep “all green”: seven divergences and
  one unrunnable member are named with their line counts, the projection's drops are stated, the two
  independent implementations' disagreement about the *observation source* is explained rather than
  averaged, and the V2 locus deviation is reported against the frozen sentence. Evidence:
  `ConnectorR82.md` §5, `ReviewerR82.md`, `MutationR82.md`, the sweep receipt, this report's
  deviation paragraph.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  `## Gate/probe registry` (143 data rows, eight cells each; ten rows added this round, each with
  entry, verdict map, self-test, pins and write scope).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 82: the
  26-member sweep census and the registry audit, with the receipts they rest on.
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-82.md`
  (M82-1…M82-4 with commands) plus the three counters' docstrings; `corpus/README.md` indexes
  `lessons/round-81-verifier-spotcheck.md`, `lessons/round-82.md` and
  `knowledge/tb2-replay-sweep-at-one-tip.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round 82 adds no surface
  and re-declares none as resolving; `ConnectorR82.md` §4/§5 carries the sibling rulings.

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no pacman transaction; the host-wide pacman pause was respected; no
  `uv tool`/`npm`/binary install was reported by any seat).
- **Open L0 questions:** none added. `kengaku | round-33` (the coverage cap) stays open and is why
  every coverage verdict reads “held at its L0 cap”; `kengaku | round-80` (amendment admissibility) is
  untouched because this round amended nothing.
- **Inherited state:** the lane arrived clean at `a3a03ac3`; the only residue found at start was the
  empty `--lane/` directory the round-81 spot-check had already named, removed here under V5.
