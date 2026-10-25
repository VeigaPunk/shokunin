# chousa — round 48

## Work performed

Declared claim: **R48-C1 operability** (lowest scored axis, 3/10) — the inference-ground polarity check gains a false-refusal regression floor and counter coverage for the five round-47 surviving mutants; before control 9/12, target ≥11/12, plus legacy and mutation legs. Frozen at `chousa-shokunin/corpus/evidence/round48/claims.md` (`4bbd2348578bb6288c0700dabf37cea04225bfb6`) before candidate changes and wave-2 scoring.

- The R47 verifier's routed false-refusal/documentation finding is addressed in the current tool Named limit and `corpus/QUALITY.md` criterion 69; after measurement is bound to code commit `671b096e2bd5d5b0994bcd7ab8c17abaf16c62c7` (`corpus/evidence/round48/measure-after.txt`). The fixed R47 regression set is reused, not a fresh estimate of natural-language precision. W2 `AttackPrecision.md` disputes the a05 label; the prior R47 non-author verdict called it a false refusal. The closure judge is asked to re-open a05 before generalizing this result.
- The five R47 survivor classes now have named refinement fixtures and a mutation probe: `measure-after.txt` → `REFINEMENT_CASES=5/5`, `MUTANTS_KILLED=5/5`. W2 independently reconstructed the implicit-neg, un-neg, repeated-figure and nested-key mutants (`w2/MutateImplicit.md`, `MutateFigure.md`, `MutateNested.md`). The cases-only repeated-figure cell misses the complementary skip-first direction; the unchanged legacy R47 leg catches the tested skip-first mutant. No claim of exhaustive mutation coverage is made.
- A name-keyed no-read substitute passes `c1-count.py` alone (`w2/AttackDoNothing.md`); the composite no-op control `corpus/evidence/round48/controls/name-key-control.py` installs such a substitute at the default tool path and shows the required frozen `mutation-check.py` rejects it (`MUTATION_NOT_APPLIED`). This demonstrates rejection of the tested shortcut, not every possible substitute.
- The `/usr/bin/true` row in frozen `controls/before.txt` had a contradictory per-cell rc/verdict. It is preserved as frozen evidence; `controls/before-erratum.txt` records the exact re-run (`observed_rc=1`, `0/5`) and `QUALITY.md` criterion 70 captures the mistake.
- All 24 chousa entries in the Wave-4 absent-defect-register slice were checked against local captures/artifacts only. The Gate verdict table and the S093 disagreement are in `chousa-shokunin/corpus/lessons/round-48.md:36-67`; W2 reports are under `.ufo/waves/round-48/w2/`.
- Rechecked all six active R39/R40 receipts at their adding commits (`6/6`) and the tip (`2/6`; four `gate-sha256-mismatch`) in `corpus/evidence/round48/receipt-recheck.txt`. The refusals are expected revision drift after round-41 commit `1bd9001` changed the gate from `4253c187…` to `2cb04bdd…`; no receipt bytes or historical bindings were rewritten.
- Re-ran the R47 scorecard registry count: `97/97`, zero mismatches after R48 gates were registered. The R47 `SCORECARD.md:2506` correction remains `94/94` final, `93/93` freeze; `92` was the floor, not a freeze ratio.
- No source-package knowledge was adopted. The still-unimplemented cloud-agent part of `considerthese/2026-10-24.md:64-66` is refused pending the operator approval it requires; no live fetch was made and L0 `8d77e6c1` remains open.

## Landed changes

- Frozen claim, C1 counters, precision fixtures and pre-control receipt: lane commit `4bbd2348578bb6288c0700dabf37cea04225bfb6`; documented in the Round-48 `LOG.md` entry (`LOG.md:1786-1796`).
- Polarity tool, error-pattern text, executable Gate registrations and QUALITY 69–70: lane commit `671b096e2bd5d5b0994bcd7ab8c17abaf16c62c7`; `tools/inference-ground.py` sha256 `fa2b4eb5fc29b4dd30f468d9409790ba55fa4b012851e5c9f3efce0074658b6e`.
- Round-48 lesson, S095 registry/search-log row, SCORECARD/LOG/README entries, wave reports/registries, census and after-measurement evidence: lane commit `73ea8110cea890188df4973b212f5441d4b19e89`.

## Before → after measurements

| claim / axis | before → after | counting command and measured commit | verdict |
|---|---|---|---|
| C1 operability | R47 tool: `CORRECT_BULLETS_PASS=9/12`, `PRECISION_GATE=FAIL`, `LEGACY_R47=PASS`, composite C1 exit 1 → candidate: `CORRECT_BULLETS_PASS=12/12` (frozen floor 11), `REFINEMENT_CASES=5/5`, `LEGACY_R47=PASS`, `C1=PASS`; mutation probe `MUTANTS_KILLED=5/5`. | `python3 corpus/evidence/round48/c1-count.py` and `python3 corpus/evidence/round48/mutation-check.py`; measured over `git archive 671b096e2bd5d5b0994bcd7ab8c17abaf16c62c7`, with tool blob SHA matching the measured bytes (`measure-after.txt`). | **improved narrowly** on this recycled regression set; no general-language precision or entailment claim. Closure should resolve the a05 label dispute. |

## Sources & frontier

Round-start validator: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0, `ok`, five pre-existing W04 warnings. Start registry count: 94 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` over the lane's round-start commit `d4e6ef09`). Round-end: same validator command → exit 0, `ok`, same five W04 warnings; final manual count 95 rows, 0 malformed; tiers A=89, B=1, C=5; statuses mined=71, queued=19, rejected=5. One tier-A own-work row, S095, was added; no existing rows were touched (`status`/`recheck`/`used-by` changes: none). Frontier rows advanced: none; no uncovered-ground knowledge entry was admitted. `Assimilation: none` — wave-4 quarantine-first was completed, all 24 verdicts are in the lesson, and no staged row or entry was appended. The local spot-check source for S095 was opened this round; its Gate quotes and access date are recorded in the lesson.

Round-start validator output:

```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
exit=0
```

Round-end validator output:

```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
exit=0
```

Manual count commands (from the Sources-contract patterns; row/status counts are over data rows only):

```
Start: git -C /home/vgpnk/Projects/shokunin/chousa-shokunin show d4e6ef09b755a961bdae56566a7dcf0c9db0cfd7:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' → 94
Start: awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5;gsub(/[[:space:]]/,"",t);n[t]++} END{for(k in n)printf "%s=%d ",k,n[k];print ""}' → A=88 B=1 C=5
Start: same awk with s=$9 → mined=70 queued=19 rejected=5; malformed NF!=13 awk → 0
End: grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md → 95
End: same tier awk → A=89 B=1 C=5; same status awk → mined=71 queued=19 rejected=5; malformed NF!=13 awk → 0
```

## Trend verdicts

- **Expansion — unchanged:** no new knowledge entry on uncovered coverage-map ground; one own-work registry row is curation, not expansion.
- **Quality — unchanged:** no corpus knowledge entry was re-admitted, deepened or left failing; the measured change is the operability tool and its fixed regression set.
- **Discernment — unchanged at L1 delivery:** all dispatched seats are author-lane evidence. The hyaku closure judge is assigned the post-report admit/reject spot-check and the S093/a05 disagreements; no outside verdict is pre-claimed.

## SHONEN

- [~] Decision tables, error patterns and cited sources — `SKILL.md:13-50,76-129`; `corpus/QUALITY.md:687-713`.
- [~] End-to-end task executed and logged — `LOG.md:1786-1796`; committed round-48 counters and wave evidence.
- [~] Instructions executable without oral context — `tools/inference-ground.py`; `corpus/evidence/round48/measure-after.txt`.
- [~] Province fit — `PROVINCE.md:3-17`; `.ufo/waves/round-48/w2/SiblingFit.md` finds no sibling overlap.

## Round shape, stale lane and tooling

Two v1 waves, 32 + 32 = 64 seats, no residual call. W1: reviewer 13, critic 8, scout 7, executor 4; Attack04 died with `invalid_prompt` (policy flag) and was not replaced. W2: reviewer 14, critic 7, scout 6, mutation-tester 3, connector 1, scribe 1; no dead W2 seats. L1 held the planner/data-walk role. W1 did not include the required connector or scribe roles; those seats appeared in W2, so the W1 role-split floor is a conformance defect despite its 32-member batched dispatch. Routing remained host-owned; no model was pinned.

`Stale-lane`: launch `2026-10-25T10:17:46-03:00`; at report filing the mission was open over two driver ticks but **progressing** (lane commits `4bbd234`, `671b096`, `73ea811` and round-48 in-scope files), not silent. Round-end `jj-lane.sh state`: branch master, local=remote=`73ea8110cea890188df4973b212f5441d4b19e89`, ahead=0, behind=0. No tools installed or updated.

## Misroot sweep and L0

Before report creation, `git -C /home/vgpnk/Projects/shokunin status --porcelain` listed only the pre-existing operator/state changes, `.scratch`/`.omp` inputs and `m-rev-vs-rev.py`; no round-48 seat reports were misrooted in the fleet root. No fleet copy was deleted and no `.scratch`/`.ufo/state` path was touched. No new L0 question was appended; the existing fetch-scope question `8d77e6c1` remains open.
